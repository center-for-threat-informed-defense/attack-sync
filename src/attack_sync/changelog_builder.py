"""A helper script to generate changelogs between different versions of ATT&CK."""

import argparse
import datetime
import json
import math
import os
import re
import sys
import typing
from difflib import SequenceMatcher
from operator import itemgetter
from pathlib import Path

import stix2
from dateutil import parser as dateparser
from deepdiff import DeepDiff
from loguru import logger
from mitreattack import release_info
from stix2 import Filter, MemoryStore

from .template import ATTACK_DATA_DIR, PUBLIC_DIR, load_template

# TODO layers
# this_month = date.strftime("%B_%Y")
# layer_defaults = [
#     os.path.join("output", f"{this_month}_Updates_Enterprise.json"),
#     os.path.join("output", f"{this_month}_Updates_Mobile.json"),
#     os.path.join("output", f"{this_month}_Updates_ICS.json"),
#     os.path.join("output", f"{this_month}_Updates_Pre.json"),
# ]


DOMAIN_NAME_TO_LABEL = {
    "enterprise-attack": "Enterprise",
    "mobile-attack": "Mobile",
    "ics-attack": "ICS",
}
TYPE_NAME_TO_LABEL = {
    "techniques": "Techniques",
    "software": "Software",
    "groups": "Groups",
    "campaigns": "Campaigns",
    "mitigations": "Mitigations",
    "datasources": "Data Sources",
    "datacomponents": "Data Components",
}

# The deepdiff library displays differences with a prefix of: root['<top-level-key-we-care-about>']
STIX_KEY_RE = re.compile(r"^root\['(?P<top_stix_key>[^\']*)'\](?P<the_rest>.*)$")


class StixDiff:
    """
    Represents the set of differences between two ATT&CK STIX bundles.
    """

    def __init__(
        self,
        old_path: Path,
        new_path: Path,
        domains: typing.List[str],
        types: typing.List[str],
        layers: typing.List[str] = [],  # TODO
    ):
        """
        Constructor.

        Args:
            old_path - path to old version of ATT&CK data
            new_path - path to new version of ATT&CK data
            domains - list of domains to parse
            types - list of object types to parse
            layers - TODO
        """
        self.old_path = old_path
        self.new_path = new_path
        self.domains = domains
        self.types = types
        self.layers = layers
        self.release_contributors: typing.Dict[str, int] = {}
        self.section_headers = {}
        for object_type in self.types:
            self.section_headers[object_type] = {
                "additions": f"New {TYPE_NAME_TO_LABEL[object_type]}",
                "version_changes": f"Changed {TYPE_NAME_TO_LABEL[object_type]}",
                "deprecations": "Deprecations",
                "revocations": "Revocations",
                "deletions": "Deletions",
                "unchanged": "Unchanged",
            }
        self.domain_cache: typing.Dict[str, dict] = dict()
        self.load_data()

    def load_data(self):
        """Load data from files into data dict."""
        # Initialize data structures.
        self.data = {
            "old": {},
            "new": {},
            "changes": {},
        }

        for domain in self.domains:
            for datastore_version in ["old", "new"]:
                self.data[datastore_version][domain] = {
                    "attack_objects": {},
                    "attack_release_version": None,
                    "stix_datastore": None,
                    "relationships": {
                        "subtechniques": {},
                        "revoked-by": {},
                    },
                }

                for type_ in self.types:
                    self.data[datastore_version][domain]["attack_objects"][type_] = {}

        for domain in self.domains:
            self.load_domain(domain=domain)

            logger.info("Diffing domain: {domain}", domain=domain)
            for obj_type in self.types:
                logger.info(f"Diffing type: {domain}/{obj_type}")

                old_attack_objects = self.data["old"][domain]["attack_objects"][
                    obj_type
                ]
                new_attack_objects = self.data["new"][domain]["attack_objects"][
                    obj_type
                ]

                intersection = old_attack_objects.keys() & new_attack_objects.keys()
                additions = new_attack_objects.keys() - old_attack_objects.keys()
                deletions = old_attack_objects.keys() - new_attack_objects.keys()

                # sets to store the ids of objects for each section
                version_changes = set()
                revocations = set()
                deprecations = set()
                unchanged = set()

                # find changes, revocations and deprecations
                for stix_id in intersection:
                    old_stix_obj = old_attack_objects[stix_id]
                    new_stix_obj = new_attack_objects[stix_id]
                    attack_id = get_attack_id(new_stix_obj)

                    ddiff = DeepDiff(old_stix_obj, new_stix_obj, verbose_level=2)
                    detailed_diff = ddiff.to_json()
                    new_stix_obj["detailed_diff"] = detailed_diff

                    # Newly revoked objects
                    if new_stix_obj.get("revoked"):
                        # only work with newly revoked objects
                        if not old_stix_obj.get("revoked"):
                            if (
                                stix_id
                                not in self.data["new"][domain]["relationships"][
                                    "revoked-by"
                                ]
                            ):
                                logger.error(
                                    f"[{stix_id}] revoked object has no revoked-by relationship"
                                )
                                continue

                            revoked_by_key = self.data["new"][domain]["relationships"][
                                "revoked-by"
                            ][stix_id][0]["target_ref"]
                            if revoked_by_key not in new_attack_objects:
                                logger.error(
                                    f"{stix_id} revoked by {revoked_by_key}, but {revoked_by_key} not found in new STIX bundle!!"
                                )
                                continue

                            revoking_object = new_attack_objects[revoked_by_key]
                            new_stix_obj["revoked_by"] = revoking_object

                            revocations.add(stix_id)

                    # Newly deprecated objects
                    elif new_stix_obj.get("x_mitre_deprecated"):
                        # if previously deprecated, not a change
                        if "x_mitre_deprecated" not in old_stix_obj:
                            deprecations.add(stix_id)

                    # Objects shared between old and new STIX bundles by STIX IDs
                    else:
                        # Verify if there are new contributors on the object
                        self.update_contributors(
                            old_object=old_stix_obj, new_object=new_stix_obj
                        )

                        old_version = get_attack_object_version(old_stix_obj)
                        new_version = get_attack_object_version(new_stix_obj)
                        new_stix_obj["previous_version"] = old_version

                        # Version number didn't change
                        if new_version == old_version:
                            # check for modification date increase but not version
                            old_date = dateparser.parse(old_stix_obj["modified"])
                            new_date = dateparser.parse(new_stix_obj["modified"])
                            if new_date != old_date:
                                version_changes.add(stix_id)
                            else:
                                unchanged.add(stix_id)

                        # Version number changed
                        else:
                            version_changes.add(stix_id)
                            new_stix_obj[
                                "version_change"
                            ] = f"{old_version} → {new_version}"

                        # Description changes
                        old_description = old_stix_obj["description"].split()
                        new_description = new_stix_obj["description"].split()

                        if old_description != new_description:
                            if stix_id not in version_changes:
                                logger.debug(
                                    "Object has a description change without the version "
                                    "being incremented or the last modified date changing: "
                                    f"{stix_id} ({attack_id})"
                                )
                                version_changes.add(stix_id)

                            new_stix_obj["old_description"] = " ".join(old_description)
                            new_stix_obj["description_diff"] = self._get_text_diff(
                                old_description, new_description
                            )

                        if new_stix_obj["type"] == "attack-pattern":
                            self.find_technique_mitigation_changes(new_stix_obj, domain)
                            self.find_technique_detection_changes(new_stix_obj, domain)

                # New objects
                for stix_id in additions:
                    new_stix_obj = new_attack_objects[stix_id]
                    attack_id = get_attack_id(new_stix_obj)

                    # Add contributions from additions
                    self.update_contributors(old_object=None, new_object=new_stix_obj)

                    # verify version is 1.0
                    x_mitre_version = new_stix_obj.get("x_mitre_version")
                    if not version_increment_is_valid(
                        None, x_mitre_version, "additions"
                    ):
                        logger.debug(
                            f"Expected version 1.0 for new object, but got {x_mitre_version} "
                            f"instead: {stix_id} ({attack_id})"
                        )

                # Deleted objects
                for stix_id in deletions:
                    old_stix_obj = old_attack_objects[stix_id]
                    attack_id = get_attack_id(old_stix_obj)

                # Create self.data["changes"]
                if obj_type not in self.data["changes"]:
                    self.data["changes"][obj_type] = {}

                self.data["changes"][obj_type][domain] = {
                    "additions": sorted(
                        [new_attack_objects[stix_id] for stix_id in additions],
                        key=lambda stix_object: stix_object["name"],
                    ),
                    "version_changes": sorted(
                        [new_attack_objects[stix_id] for stix_id in version_changes],
                        key=lambda stix_object: stix_object["name"],
                    ),
                    "revocations": sorted(
                        [new_attack_objects[stix_id] for stix_id in revocations],
                        key=lambda stix_object: stix_object["name"],
                    ),
                    "deprecations": sorted(
                        [new_attack_objects[stix_id] for stix_id in deprecations],
                        key=lambda stix_object: stix_object["name"],
                    ),
                    "deletions": sorted(
                        [old_attack_objects[stix_id] for stix_id in deletions],
                        key=lambda stix_object: stix_object["name"],
                    ),
                }

    def _get_text_diff(
        self, old_text: typing.List[str], new_text: typing.List[str]
    ) -> typing.List[typing.Dict]:
        """
        Compute the diff between two texts and return a list of edits.

        The return value is a list of dicts. Each dict contains a "text" key and a
        "disposition" key indicating whether the text is "added", "removed", or
        "unchanged".

        Args:
            old_text - the original text
            new_text - the updated text

        Returns:
            a list of edits
        """

        edits: typing.List[typing.Dict] = list()
        diff = SequenceMatcher(None, old_text, new_text, autojunk=False)

        for opcode, old_start, old_end, new_start, new_end in diff.get_opcodes():
            old = " " + " ".join(old_text[old_start:old_end]) + " "
            new = " " + " ".join(new_text[new_start:new_end]) + " "
            match opcode:
                case "replace":
                    edits.append({"text": old, "disposition": "removed"})
                    edits.append({"text": new, "disposition": "added"})
                case "delete":
                    edits.append({"text": old, "disposition": "removed"})
                case "insert":
                    edits.append({"text": new, "disposition": "added"})
                case "equal":
                    edits.append({"text": new, "disposition": "unchanged"})

        return edits

    def find_technique_mitigation_changes(self, new_stix_obj: dict, domain: str):
        """
        Find changes in the relationships between Techniques and Mitigations.

        Args:
            new_stix_obj: An ATT&CK Technique (attack-pattern) STIX Domain Object (SDO).
            domain: An ATT&CK domain from the following list ["enterprise-attack", "mobile-attack", "ics-attack"]
        """
        stix_id = new_stix_obj["id"]
        all_old_domain_mitigations = self.data["old"][domain]["attack_objects"][
            "mitigations"
        ]
        all_new_domain_mitigations = self.data["new"][domain]["attack_objects"][
            "mitigations"
        ]
        old_mitigations = {}
        new_mitigations = {}

        for _, mitigation_relationship in self.data["old"][domain]["relationships"][
            "mitigations"
        ].items():
            if mitigation_relationship.get(
                "x_mitre_deprecated"
            ) or mitigation_relationship.get("revoked"):
                continue
            if stix_id == mitigation_relationship["target_ref"]:
                old_mitigation_id = mitigation_relationship["source_ref"]
                old_mitigation = all_old_domain_mitigations[old_mitigation_id]
                old_mitigations[old_mitigation["id"]] = old_mitigation

        for _, mitigation_relationship in self.data["new"][domain]["relationships"][
            "mitigations"
        ].items():
            if mitigation_relationship.get(
                "x_mitre_deprecated"
            ) or mitigation_relationship.get("revoked"):
                continue
            if stix_id == mitigation_relationship["target_ref"]:
                new_mitigation_id = mitigation_relationship["source_ref"]
                new_mitigation = all_new_domain_mitigations[new_mitigation_id]
                new_mitigations[new_mitigation["id"]] = new_mitigation

        shared_mitigations = old_mitigations.keys() & new_mitigations.keys()
        brand_new_mitigations = new_mitigations.keys() - old_mitigations.keys()
        dropped_mitigations = old_mitigations.keys() - new_mitigations.keys()

        new_stix_obj["changelog_mitigations"] = {
            "shared": [
                f"{get_attack_id(stix_obj=new_mitigations[stix_id])}: {new_mitigations[stix_id]['name']}"
                for stix_id in shared_mitigations
            ],
            "new": [
                f"{get_attack_id(stix_obj=new_mitigations[stix_id])}: {new_mitigations[stix_id]['name']}"
                for stix_id in brand_new_mitigations
            ],
            "dropped": [
                f"{get_attack_id(stix_obj=old_mitigations[stix_id])}: {old_mitigations[stix_id]['name']}"
                for stix_id in dropped_mitigations
            ],
        }

    def find_technique_detection_changes(self, new_stix_obj: dict, domain: str):
        """
        Find changes in the relationships between Techniques and Datacomponents.

        Parameters
        ----------
            new_stix_obj: An ATT&CK Technique (attack-pattern) STIX Domain Object (SDO).
            domain: An ATT&CK domain from the following list ["enterprise-attack", "mobile-attack", "ics-attack"]
        """
        stix_id = new_stix_obj["id"]
        all_old_domain_datasources = self.data["old"][domain]["attack_objects"][
            "datasources"
        ]
        all_old_domain_datacomponents = self.data["old"][domain]["attack_objects"][
            "datacomponents"
        ]
        all_new_domain_datasources = self.data["new"][domain]["attack_objects"][
            "datasources"
        ]
        all_new_domain_datacomponents = self.data["new"][domain]["attack_objects"][
            "datacomponents"
        ]
        old_detections = {}
        new_detections = {}

        for _, detection_relationship in self.data["old"][domain]["relationships"][
            "detections"
        ].items():
            if detection_relationship.get(
                "x_mitre_deprecated"
            ) or detection_relationship.get("revoked"):
                continue
            if stix_id == detection_relationship["target_ref"]:
                old_datacomponent_id = detection_relationship["source_ref"]
                old_datacomponent = all_old_domain_datacomponents[old_datacomponent_id]
                old_datasource_id = old_datacomponent["x_mitre_data_source_ref"]
                old_datasource = all_old_domain_datasources[old_datasource_id]
                old_datasource_attack_id = get_attack_id(stix_obj=old_datasource)
                old_detections[
                    old_datacomponent_id
                ] = f"{old_datasource_attack_id}: {old_datasource['name']} ({old_datacomponent['name']})"

        for _, detection_relationship in self.data["new"][domain]["relationships"][
            "detections"
        ].items():
            if detection_relationship.get(
                "x_mitre_deprecated"
            ) or detection_relationship.get("revoked"):
                continue
            if stix_id == detection_relationship["target_ref"]:
                new_datacomponent_id = detection_relationship["source_ref"]
                new_datacomponent = all_new_domain_datacomponents[new_datacomponent_id]
                new_datasource_id = new_datacomponent["x_mitre_data_source_ref"]
                new_datasource = all_new_domain_datasources[new_datasource_id]
                new_datasource_attack_id = get_attack_id(stix_obj=new_datasource)
                new_detections[
                    new_datacomponent_id
                ] = f"{new_datasource_attack_id}: {new_datasource['name']} ({new_datacomponent['name']})"

        shared_detections = old_detections.keys() & new_detections.keys()
        brand_new_detections = new_detections.keys() - old_detections.keys()
        dropped_detections = old_detections.keys() - new_detections.keys()

        new_stix_obj["changelog_detections"] = {
            "shared": [f"{new_detections[stix_id]}" for stix_id in shared_detections],
            "new": [f"{new_detections[stix_id]}" for stix_id in brand_new_detections],
            "dropped": [f"{old_detections[stix_id]}" for stix_id in dropped_detections],
        }

    def load_domain(self, domain: str):
        """
        Load data from directory according to domain.

        Args:
            domain: An ATT&CK domain from the following list ["enterprise-attack", "mobile-attack", "ics-attack"]
        """
        for datastore_version in ["old", "new"]:
            directory = self.old_path if datastore_version == "old" else self.new_path
            stix_file = os.path.join(directory, f"{domain}.json")
            logger.info("Loading domain: {}", stix_file)

            attack_version = release_info.get_attack_version(
                domain=domain, stix_file=stix_file
            )
            self.data[datastore_version][domain][
                "attack_release_version"
            ] = attack_version

            data_store = self.domain_cache.get(str(stix_file))
            if not data_store:
                data_store = MemoryStore()
                data_store.load_from_file(stix_file)
            self.data[datastore_version][domain]["stix_datastore"] = data_store
            self.parse_extra_data(
                data_store=data_store,
                domain=domain,
                datastore_version=datastore_version,
            )

    def parse_extra_data(
        self, data_store: stix2.MemoryStore, domain: str, datastore_version: str
    ):
        """
        Parse STIX datastore objects and relationships.

        Args:
            data_store: STIX MemoryStore object representing an ATT&CK domain.
            domain: An ATT&CK domain from the following list ["enterprise-attack", "mobile-attack", "ics-attack"]
            datastore_version: The comparative version of the ATT&CK datastore. Choices are either "old" or "new".
        """
        attack_type_to_stix_filter = {
            "techniques": [Filter("type", "=", "attack-pattern")],
            "software": [Filter("type", "=", "malware"), Filter("type", "=", "tool")],
            "groups": [Filter("type", "=", "intrusion-set")],
            "campaigns": [Filter("type", "=", "campaign")],
            "mitigations": [Filter("type", "=", "course-of-action")],
            "datasources": [Filter("type", "=", "x-mitre-data-source")],
            "datacomponents": [Filter("type", "=", "x-mitre-data-component")],
        }
        for object_type, stix_filters in attack_type_to_stix_filter.items():
            raw_data = []
            for stix_filter in stix_filters:
                temp_filtered_list = data_store.query(stix_filter)
                raw_data.extend(temp_filtered_list)

            raw_data = deep_copy_stix(raw_data)
            self.data[datastore_version][domain]["attack_objects"][object_type] = {
                attack_object["id"]: attack_object for attack_object in raw_data
            }

        subtechnique_relationships = data_store.query(
            [
                Filter("type", "=", "relationship"),
                Filter("relationship_type", "=", "subtechnique-of"),
            ]
        )
        self.data[datastore_version][domain]["relationships"]["subtechniques"] = {
            relationship["id"]: relationship
            for relationship in subtechnique_relationships
        }

        revoked_by_relationships = data_store.query(
            [
                Filter("type", "=", "relationship"),
                Filter("relationship_type", "=", "revoked-by"),
            ]
        )

        # use list in case STIX object was revoked more than once
        for relationship in revoked_by_relationships:
            source_id = relationship["source_ref"]
            if (
                source_id
                not in self.data[datastore_version][domain]["relationships"][
                    "revoked-by"
                ]
            ):
                self.data[datastore_version][domain]["relationships"]["revoked-by"][
                    source_id
                ] = []
            self.data[datastore_version][domain]["relationships"]["revoked-by"][
                source_id
            ].append(relationship)

        mitigating_relationships = data_store.query(
            [
                Filter("type", "=", "relationship"),
                Filter("relationship_type", "=", "mitigates"),
            ]
        )
        self.data[datastore_version][domain]["relationships"]["mitigations"] = {
            relationship["id"]: relationship
            for relationship in mitigating_relationships
        }

        detection_relationships = data_store.query(
            [
                Filter("type", "=", "relationship"),
                Filter("relationship_type", "=", "detects"),
            ]
        )
        self.data[datastore_version][domain]["relationships"]["detections"] = {
            relationship["id"]: relationship for relationship in detection_relationships
        }

    def update_contributors(self, old_object: typing.Optional[dict], new_object: dict):
        """
        Update contributors list if new object has contributors.

        Args:
            old_object: An ATT&CK STIX Domain Object (SDO).
            new_object: An ATT&CK STIX Domain Object (SDO).
        """
        if new_object.get("x_mitre_contributors"):
            new_object_contributors = set(new_object["x_mitre_contributors"])

            # Check if old objects had contributors
            if old_object is None or not old_object.get("x_mitre_contributors"):
                old_object_contributors = set()
            else:
                old_object_contributors = set(old_object["x_mitre_contributors"])

            # Remove old contributors from showing up
            # if contributors are the same the result will be empty
            new_contributors = new_object_contributors - old_object_contributors

            # Update counter of contributor to track contributions
            for new_contributor in new_contributors:
                if self.release_contributors.get(new_contributor):
                    self.release_contributors[new_contributor] += 1
                else:
                    self.release_contributors[new_contributor] = 1

    def get_groupings(
        self, object_type: str, stix_objects: typing.List, section: str, domain: str
    ) -> typing.List[typing.Dict[str, object]]:
        """
        Group STIX objects together within a section.

        A "group" in this sense is a set of STIX objects that are all in the same
        section, e.g. new minor version. In this case, since a domain/object type are
        implied before we get here, it would be e.g. "All Enterprise Techniques &
        Subtechniques, grouped alphabetically by name, and the sub-techniques are
        'grouped' under their parent technique"

        Args:
            object_type: Type of STIX object that is being worked with.
            stix_objects: List of STIX objects that need to be grouped.
            section: Section of the changelog that is being created with the objects, e.g. new major version, revocation, etc.

        Returns:
            A list of sorted, complex dictionary objects that tell if this "group" of
            objects have their parent objects in the same section.
        """
        datastore_version = "old" if section == "deletions" else "new"
        subtechnique_relationships = self.data[datastore_version][domain][
            "relationships"
        ]["subtechniques"]
        techniques = self.data[datastore_version][domain]["attack_objects"][
            "techniques"
        ]
        datacomponents = self.data[datastore_version][domain]["attack_objects"][
            "datacomponents"
        ]
        datasources = self.data[datastore_version][domain]["attack_objects"][
            "datasources"
        ]

        childless = []
        parents = []
        children = {}
        # get parents which have children
        if object_type == "datasource":
            for stix_object in stix_objects:
                if stix_object.get("x_mitre_data_source_ref"):
                    children[stix_object["id"]] = stix_object
                else:
                    parents.append(stix_object)
        else:
            for stix_object in stix_objects:
                is_subtechnique = stix_object.get("x_mitre_is_subtechnique")

                if is_subtechnique:
                    children[stix_object["id"]] = stix_object
                elif has_subtechniques(
                    stix_object=stix_object,
                    subtechnique_relationships=subtechnique_relationships,
                ):
                    parents.append(stix_object)
                else:
                    childless.append(stix_object)

        parentToChildren: typing.Dict[str, typing.List] = {}
        # subtechniques
        for relationship in subtechnique_relationships.values():
            if not relationship["source_ref"] in children:
                continue

            parent_technique_stix_id = relationship["target_ref"]
            the_subtechnique = children[relationship["source_ref"]]
            if parent_technique_stix_id not in parentToChildren:
                parentToChildren[parent_technique_stix_id] = []
            parentToChildren[parent_technique_stix_id].append(the_subtechnique)

        # datacomponents
        for datacomponent in datacomponents.values():
            if datacomponent["id"] not in children:
                continue

            parent_datasource_id = datacomponent["x_mitre_data_source_ref"]
            the_datacomponent = children[datacomponent["id"]]
            if parent_datasource_id not in parentToChildren:
                parentToChildren[parent_datasource_id] = []
            parentToChildren[parent_datasource_id].append(the_datacomponent)

        # now group parents and children
        groupings = []
        for parent_stix_object in childless + parents:
            child_objects = (
                parentToChildren.pop(parent_stix_object["id"])
                if parent_stix_object["id"] in parentToChildren
                else []
            )
            groupings.append(
                {
                    "parent": parent_stix_object,
                    "parentInSection": True,
                    "children": child_objects,
                }
            )

        for parent_stix_id, child_objects in parentToChildren.items():
            parent_stix_object = None
            if parent_stix_id in techniques:
                parent_stix_object = techniques[parent_stix_id]
            elif parent_stix_id in datasources:
                parent_stix_object = datasources[parent_stix_id]

            if parent_stix_object:
                groupings.append(
                    {
                        "parent": parent_stix_object,
                        "parentInSection": False,
                        "children": child_objects,
                    }
                )

        groupings = sorted(groupings, key=lambda grouping: grouping["parent"]["name"])
        return groupings

    def get_parent_stix_object(
        self, stix_object: dict, datastore_version: str, domain: str
    ) -> dict:
        """
        Given an ATT&CK STIX object, find and return it's parent STIX object.

        Args:
            stix_object: An ATT&CK STIX Domain Object (SDO).
            datastore_version: The comparative version of the ATT&CK datastore. Choices are either "old" or "new".
            domain: An ATT&CK domain from the following list ["enterprise-attack", "mobile-attack", "ics-attack"]

        Returns:
            The parent STIX object, if one can be found. Otherwise an empty dictionary is returned.
        """
        subtechnique_relationships = self.data[datastore_version][domain][
            "relationships"
        ]["subtechniques"]
        techniques = self.data[datastore_version][domain]["attack_objects"][
            "techniques"
        ]
        datasources = self.data[datastore_version][domain]["attack_objects"][
            "datasources"
        ]

        if stix_object.get("x_mitre_is_subtechnique"):
            for subtechnique_relationship in subtechnique_relationships.values():
                if subtechnique_relationship["source_ref"] == stix_object["id"]:
                    parent_id = subtechnique_relationship["target_ref"]
                    return techniques[parent_id]
        elif stix_object["type"] == "x-mitre-data-component":
            return datasources[stix_object.get("x_mitre_data_source_ref")]

        # possible reasons for no parent object: deprecated/revoked/wrong object type passed in
        return {}

    def get_layers_dict(self) -> typing.Dict:
        """
        Return ATT&CK Navigator layers in dict format summarizing detected differences.

        Returns:
            A dict mapping domain to its layer dict.
        """
        logger.info("Generating ATT&CK Navigator layers")

        colors = {
            "additions": "#a1d99b",  # granny smith apple
            "major_version_changes": "#fcf3a2",  # yellow-ish
            "minor_version_changes": "#c7c4e0",  # light periwinkle
            "other_version_changes": "#B5E5CF",  # mint
            "metadata_changes": "#B99095",  # mauve
            "unknown_changes": "#3D5B59",  # teal green
            "deletions": "#ff00e1",  # hot magenta
            "revocations": "#ff9000",  # dark orange
            "deprecations": "#ff6363",  # bittersweet red
            "unchanged": "#ffffff",  # white
        }

        layers = {}
        thedate = datetime.datetime.today().strftime("%B %Y")
        # for each layer file in the domains mapping
        for domain in self.domains:
            logger.info(f"Generating ATT&CK Navigator layer for domain: {domain}")
            # build techniques list
            techniques = []
            for section, technique_stix_objects in self.data["changes"]["techniques"][
                domain
            ].items():
                if section == "revocations" or section == "deprecations":
                    continue

                for technique in technique_stix_objects:
                    problem_detected = False
                    if "kill_chain_phases" not in technique:
                        logger.error(
                            f"{technique['id']}: technique missing a tactic!! {technique['name']}"
                        )
                        problem_detected = True
                    if "external_references" not in technique:
                        logger.error(
                            f"{technique['id']}: technique missing external references!! {technique['name']}"
                        )
                        problem_detected = True

                    if problem_detected:
                        continue

                    for phase in technique["kill_chain_phases"]:
                        techniques.append(
                            {
                                "techniqueID": technique["external_references"][0][
                                    "external_id"
                                ],
                                "tactic": phase["phase_name"],
                                "enabled": True,
                                # "color": colors[section],
                                # trim the 's' off end of word
                                "comment": section[:-1]
                                if section != "unchanged"
                                else section,
                            }
                        )

            legendItems = []
            # for section, description in self.section_descriptions.items():
            #     legendItems.append({"color": colors[section], "label": f"{section}: {description}"})

            # build layer structure
            layer_json = {
                "versions": {
                    "layer": "4.4",
                    "navigator": "4.8.0",
                    "attack": self.data["new"][domain]["attack_release_version"],
                },
                "name": f"{thedate} {DOMAIN_NAME_TO_LABEL[domain]} Updates",
                "description": f"{DOMAIN_NAME_TO_LABEL[domain]} updates for the {thedate} release of ATT&CK",
                "domain": domain,
                "techniques": techniques,
                "sorting": 0,
                "hideDisabled": False,
                "legendItems": legendItems,
                "showTacticRowBackground": True,
                "tacticRowBackground": "#205b8f",
                "selectTechniquesAcrossTactics": True,
            }
            layers[domain] = layer_json

        return layers

    def get_changes_dict(self) -> typing.Dict:
        """
        Initializes a dict structure for representing changes.

        Returns:
            A blank dict structure
        """
        logger.info("Generating changes info")

        changes_dict = {}
        for domain in self.domains:
            changes_dict[domain] = {}

        for object_type, domains in self.data["changes"].items():
            for domain, sections in domains.items():
                changes_dict[domain][object_type] = {}

                for section, stix_objects in sections.items():
                    groupings = self.get_groupings(
                        object_type=object_type,
                        stix_objects=stix_objects,
                        section=section,
                        domain=domain,
                    )
                    # new_values includes parents & children mixed (e.g. techniques/sub-techniques, data sources/components)
                    new_values = cleanup_values(groupings=groupings)
                    changes_dict[domain][object_type][section] = new_values

        # always add contributors
        changes_dict["new-contributors"] = []
        sorted_contributors = sorted(self.release_contributors, key=lambda v: v.lower())
        for contributor in sorted_contributors:
            # do not include ATT&CK as contributor
            if contributor == "ATT&CK":
                continue
            changes_dict["new-contributors"].append(contributor)

        return changes_dict


def has_subtechniques(
    stix_object: dict, subtechnique_relationships: typing.Dict
) -> bool:
    """
    Return true or false depending on whether the SDO has sub-techniques.

    Args:
        stix_object: An ATT&CK STIX Domain Object (SDO).
        subtechnique_relationships: List of STIX Relationship Object (SRO) dictionaries.

    Returns:
        Returns True if the stix_object has Subtechniques.
    """
    for relationship in subtechnique_relationships.values():
        if relationship["target_ref"] == stix_object["id"]:
            return True

    return False


def cleanup_values(groupings: typing.List[dict]) -> typing.List[dict]:
    """
    Clean the values found in the initial groupings of ATT&CK Objects.

    Args:
        groupings: Whatever comes out of StixDiff.get_groupings()

    Returns:
        A cleaned up version of groupings.
    """
    new_values = []
    for grouping in groupings:
        if grouping["parentInSection"]:
            new_values.append(grouping["parent"])

        for child in sorted(grouping["children"], key=lambda child: child["name"]):
            new_values.append(child)

    return new_values


def version_increment_is_valid(
    old_version: typing.Optional[str], new_version: str, section: str
) -> bool:
    """
    Validate version increment between old and new STIX objects.

    Valid increments include the following:

        * Major version increases: e.g. 1.2 → 2.0
        * Minor version increases: e.g. 1.2 → 1.3
        * New version for new objects must be 1.0
        * Any value when section is "revocations" or "deprecations"

    Args:
        old_version: Old version of an ATT&CK STIX Domain Object (SDO).
        new_version: New version of an ATT&CK STIX Domain Object (SDO).
        section: Section change type, e.g major_version_change, revocations, etc.

    Returns:
        True if the version increment is valid, otherwise False
    """
    if section in ["revocations", "deprecations"]:
        return True
    if section == "additions":
        if new_version != "1.0":
            return False
        return True
    if not (old_version and new_version):
        return False

    major_change = is_major_version_change(
        old_version=float(old_version), new_version=float(new_version)
    )
    minor_change = is_minor_version_change(
        old_version=float(old_version), new_version=float(new_version)
    )

    if major_change or minor_change:
        return True
    return False


def is_major_version_change(old_version: float, new_version: float) -> bool:
    """
    Determine if the new version is a major change or not.

    Args:
        old_version: the old object version
        new_version: the new object version

    Returns:
        True if it's a major version change, otherwise False
    """
    next_major = float(math.floor(old_version + 1))
    if next_major == new_version:
        return True
    return False


def is_minor_version_change(old_version: float, new_version: float) -> bool:
    """
    Determine if the new version is a minor change or not.

    Args:
        old_version: the old object version
        new_version: the new object version

    Returns:
        True if it's a minor version change, otherwise False
    """
    diff = round(new_version - old_version, 1)
    if diff == 0.1:
        return True
    return False


def deep_copy_stix(stix_objects: typing.List[dict]) -> typing.List[dict]:
    """
    Transform STIX to dict and deep copy the dict.

    Args:
        stix_objects: A list of Python dictionaries of ATT&CK STIX Domain Objects.

    Returns:
        A slightly easier to work with list of Python dictionaries of ATT&CK STIX Domain Objects.
    """
    result = []
    for stix_object in stix_objects:
        stix_object = dict(stix_object)
        if "external_references" in stix_object:
            for i in range(len(stix_object["external_references"])):
                stix_object["external_references"][i] = dict(
                    stix_object["external_references"][i]
                )
        if "kill_chain_phases" in stix_object:
            for i in range(len(stix_object["kill_chain_phases"])):
                stix_object["kill_chain_phases"][i] = dict(
                    stix_object["kill_chain_phases"][i]
                )

        if "modified" in stix_object:
            stix_object["modified"] = str(stix_object["modified"])
        if "first_seen" in stix_object:
            stix_object["first_seen"] = str(stix_object["first_seen"])
        if "last_seen" in stix_object:
            stix_object["last_seen"] = str(stix_object["last_seen"])

        if "definition" in stix_object:
            stix_object["definition"] = dict(stix_object["definition"])
        stix_object["created"] = str(stix_object["created"])
        result.append(stix_object)
    return result


def get_attack_id(stix_obj: dict) -> typing.Optional[str]:
    """
    Get the object's ATT&CK ID.

    Args:
        stix_obj: An ATT&CK STIX Domain Object (SDO).

    Returns:
        The ATT&CK ID of the object. Returns None if not found
    """
    attack_id = None
    external_references = stix_obj.get("external_references")
    if external_references:
        attack_source = external_references[0]
        if attack_source.get("external_id") and attack_source.get("source_name") in [
            "mitre-attack",
            "mitre-mobile-attack",
            "mitre-ics-attack",
        ]:
            attack_id = attack_source["external_id"]
    return attack_id


def get_attack_object_version(stix_obj: dict) -> float:
    """
    Get the object's ATT&CK version.

    Args:
        stix_obj: An ATT&CK STIX Domain Object (SDO).

    Returns:
        The object version of the ATT&CK object. Defaults to 0.0
    """
    # ICS objects didn't have x_mitre_version until v11.0, so pretend they were version 0.0
    version = stix_obj.get("x_mitre_version", "0")
    return float(version)


def layers_dict_to_files(outfiles, layers):
    """
    Print the layers dict passed in to layer files.

    Args:
        outfiles: list of file paths to write
        layers: dictionary of layer data
    """
    logger.info("Writing ATT&CK Navigator layers to JSON files")

    # write each layer to separate files
    if "enterprise-attack" in layers:
        enterprise_attack_layer_file = outfiles[0]
        Path(enterprise_attack_layer_file).parent.mkdir(parents=True, exist_ok=True)
        json.dump(
            layers["enterprise-attack"],
            open(enterprise_attack_layer_file, "w"),
            indent=4,
        )

    if "mobile-attack" in layers:
        mobile_attack_layer_file = outfiles[1]
        Path(mobile_attack_layer_file).parent.mkdir(parents=True, exist_ok=True)
        json.dump(
            layers["mobile-attack"], open(mobile_attack_layer_file, "w"), indent=4
        )

    if "ics-attack" in layers:
        ics_attack_layer_file = outfiles[2]
        Path(ics_attack_layer_file).parent.mkdir(parents=True, exist_ok=True)
        json.dump(layers["ics-attack"], open(ics_attack_layer_file, "w"), indent=4)


def render_changelog_landing_page(
    stix_diff: StixDiff,
    output_dir: Path,
    domain: str,
    url_prefix: str,
    google_analytics_tag: typing.Optional[str],
):
    """
    Write high level overview of changes between ATT&CK versions as a landing page.

    Args:
        html_file: File to write HTML for the index.
        stix_diff: An instance of a stix_diff object.
        domain: ATT&CK domain
        url_prefix: a prefix to place in front of any constructed URL
        google_analytics_tag: a GA tag to emit in rendered pages
    """
    output_path = output_dir / domain / "index.html"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    logger.info("Creating changelog landing page: {}", output_path)

    # Compute the data needed to render the page.
    old_version = stix_diff.data["old"][stix_diff.domains[0]]["attack_release_version"]
    new_version = stix_diff.data["new"][stix_diff.domains[0]]["attack_release_version"]

    type_summaries = list()
    for object_type in stix_diff.data["changes"].keys():
        if object_type in stix_diff.types:
            changes = stix_diff.data["changes"][object_type][domain]
            type_summary = {
                "type": object_type,
                "added": len(changes["additions"]),
                "modified": len(changes["version_changes"]),
                "revoked": len(changes["revocations"]),
                "deprecated": len(changes["deprecations"]),
            }
            if any(
                [
                    type_summary["added"],
                    type_summary["modified"],
                    type_summary["revoked"],
                    type_summary["deprecated"],
                ]
            ):
                type_summaries.append(type_summary)

    # Render the page.
    template = load_template("changelog-landing.html.j2")
    stream = template.stream(
        url_prefix=url_prefix,
        old_version=old_version,
        new_version=new_version,
        current_domain=domain,
        domains=stix_diff.domains,
        domain_name_to_label=DOMAIN_NAME_TO_LABEL,
        types=stix_diff.types,
        type_name_to_label=TYPE_NAME_TO_LABEL,
        change_types=[
            "added",
            "modified",
            "revoked",
            "deprecated",
        ],
        type_summaries=type_summaries,
        google_analytics_tag=google_analytics_tag,
    )
    stream.dump(str(output_path))


def render_changelog_detail_page(
    stix_diff: StixDiff,
    output_dir: Path,
    domain: str,
    type_: str,
    url_prefix: str,
    google_analytics_tag: typing.Optional[str],
):
    """
    Create the HTML changelog for the provided diff.

    Args:
        stix_diff: the diff object to generate a changelog from
        output_dir: where to save the changelog
        domain: the ATT&CK domain to render
        type_: the ATT&CK object type to render
        url_prefix: a prefix to place in front of any constructed URL
        google_analytics_tag: a GA tag to emit in rendered pages
    """
    output_path = output_dir / domain / type_ / "index.html"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    logger.info("Creating changelog detail pages: {}", output_path)

    # Compute the data needed to render the page.
    old_version = stix_diff.data["old"][stix_diff.domains[0]]["attack_release_version"]
    new_version = stix_diff.data["new"][stix_diff.domains[0]]["attack_release_version"]
    change_types = stix_diff.data["changes"][type_][domain]

    # Map StixDiff key names to ATT&CK Sync key names, the keys that are used in
    # changelog_dict.
    stix_to_sync_map = {
        "additions": "added",
        "version_changes": "modified",
        "deprecations": "deprecated",
        "revocations": "revoked",
        "deletions": None,
        "unchanged": None,
    }
    changelog_dict = {
        "added": [],
        "modified": [],
        "deprecated": [],
        "revoked": [],
    }

    for change_type, change_data in change_types.items():
        datastore_version = "old" if change_type == "deletions" else "new"
        sync_change_type = stix_to_sync_map[change_type]
        if sync_change_type is None:
            continue
        changelog = changelog_dict[sync_change_type]

        for stix_object in change_data:
            attack_id = get_attack_id(stix_object) or "Missing ATT&CK ID"
            title = _get_attack_title(
                stix_diff, stix_object, attack_id, datastore_version, domain
            )
            item = _build_accordion_item(stix_object, attack_id, title, change_type)
            changelog.append(item)

        changelog.sort(key=itemgetter("attack_id"))

    # Render the page.
    template = load_template("changelog-detail.html.j2")
    changelog = [
        ("added", "Added", changelog_dict["added"]),
        ("modified", "Modified", changelog_dict["modified"]),
        ("revoked", "Revoked", changelog_dict["revoked"]),
        ("deprecated", "Deprecated", changelog_dict["deprecated"]),
    ]
    stream = template.stream(
        url_prefix=url_prefix,
        old_version=old_version,
        new_version=new_version,
        current_domain=domain,
        domains=stix_diff.domains,
        domain_name_to_label=DOMAIN_NAME_TO_LABEL,
        current_domains=domain,
        types=stix_diff.types,
        type_name_to_label=TYPE_NAME_TO_LABEL,
        current_type=type_,
        changelog=changelog,
        google_analytics_tag=google_analytics_tag,
    )
    stream.dump(str(output_path))


def _get_attack_title(
    stix_diff: StixDiff,
    stix_object: dict,
    attack_id: str,
    datastore_version: str,
    domain: str,
) -> str:
    """
    Get a title for an ATT&CK object

    Args:
        stix_diff: the diff object
        stix_object: an instance from the diff changes
        attack_id: ATT&CK object id
        datastore_version: the store to look up parent object in ("old" or "new")
        domain: the ATT&CK domain

    Returns:
        A title
    """
    if stix_object["type"] == "x-mitre-data-component" or stix_object.get(
        "x_mitre_is_subtechnique"
    ):
        parent_object = stix_diff.get_parent_stix_object(
            stix_object=stix_object,
            datastore_version=datastore_version,
            domain=domain,
        )
        if parent_object:
            title = f"{parent_object.get('name')}: {stix_object['name']}"
        else:
            logger.warning(f"[{stix_object['id']}] {attack_id} has no parent!")
            title = f"{stix_object['name']} (No parent object identified. It is likely revoked or deprecated)"
    else:
        title = stix_object["name"]

    return title


def _build_accordion_item(stix_object, attack_id, title, change_type) -> dict:
    """
    Populate a dict with all of the properties needed to render a changelog accordion.

    Args:
        stix_object: the stix object to render
        attack_id: ATT&CK object id
        title: object title
        change_type: e.g. "additions", "revocations", etc.

    Returns:
        an item that can be rendered as an accordion in the changelog template
    """
    object_version = get_attack_object_version(stix_obj=stix_object)
    version_change = stix_object.get("version_change")

    revoked_by_name = ""
    revoked_by_id = ""
    revoked_by_description = ""
    values_changed = []
    iterable_added = []
    iterable_removed = []
    dict_added = []
    dict_removed = []
    if change_type == "revocations":
        revoked_by_id = get_attack_id(stix_object["revoked_by"]) or "N/A"
        revoked_by_name = stix_object["revoked_by"]["name"]
        revoked_by_description = stix_object["revoked_by"]["description"]

    if detailed_diff := json.loads(stix_object.get("detailed_diff", "{}")):
        for detailed_change_type, detailed_changes in detailed_diff.items():
            if detailed_change_type == "values_changed":
                for detailed_change, values in detailed_changes.items():
                    if matches := STIX_KEY_RE.search(detailed_change):
                        top_stix_key = matches.group("top_stix_key")
                        the_rest = matches.group("the_rest")
                        stix_field = f"{top_stix_key}{the_rest}"
                        old_value = values["old_value"]
                        new_value = values["new_value"]
                        values_changed.append(
                            {"stix": stix_field, "old": old_value, "new": new_value}
                        )

            elif detailed_change_type == "iterable_item_added":
                for detailed_change, new_value in detailed_changes.items():
                    if matches := STIX_KEY_RE.search(detailed_change):
                        stix_field = matches.group("top_stix_key")
                        iterable_added.append(
                            {"stix": stix_field, "old": "", "new": new_value}
                        )

            elif detailed_change_type == "iterable_item_removed":
                for detailed_change, old_value in detailed_changes.items():
                    if matches := STIX_KEY_RE.search(detailed_change):
                        stix_field = matches.group("top_stix_key")
                        iterable_removed.append(
                            {"stix": stix_field, "old": old_value, "new": ""}
                        )

            elif detailed_change_type == "dictionary_item_added":
                for detailed_change, new_value in detailed_changes.items():
                    if matches := STIX_KEY_RE.search(detailed_change):
                        stix_field = matches.group("top_stix_key")
                        dict_added.append(
                            {"stix": stix_field, "old": "", "new": new_value}
                        )

            elif detailed_change_type == "dictionary_item_removed":
                for detailed_change, old_value in detailed_changes.items():
                    if matches := STIX_KEY_RE.search(detailed_change):
                        stix_field = matches.group("top_stix_key")
                        dict_removed.append(
                            {"stix": stix_field, "old": old_value, "new": ""}
                        )

    return {
        "stix_object": stix_object,
        "attack_id": attack_id,
        "title": title,
        "version_hange": version_change,
        "version": object_version,
        "change_type": change_type,
        "revoked_by_id": revoked_by_id,
        "revoked_by_description": revoked_by_description,
        "revoked_by_name": revoked_by_name,
        "detailed_diff": detailed_diff,
        "values_changed": values_changed,
        "iterable_added": iterable_added,
        "iterable_removed": iterable_removed,
        "dict_added": dict_added,
        "dict_removed": dict_removed,
    }


def build_changelog(
    old: str,
    new: str,
    domains: typing.List[str],
    types: typing.List[str],
    url_prefix: str,
    google_analytics_tag: typing.Optional[str],
    # layers: typing.List[str] = layer_defaults,
):
    """
    Build the changelog for a specified version pair in HTML and JSON formats.

    Args:
        old: the old version number to use as a base of comparison
        new: the new version number to compare against
        domains: list of domains to parse
        types: list of object types to parse
        url_prefix: a prefix to place in front of any constructed URL
        google_analytics_tag: a GA tag to emit in rendered pages
        layers: TODO
    """
    old_path = ATTACK_DATA_DIR / old

    if not old_path.is_dir():
        logger.error(
            "The OLD version was not found. Make sure it is a valid ATT&CK version and "
            "has been downloaded to {dir_}.",
            dir_=ATTACK_DATA_DIR,
        )
        sys.exit(1)

    new_path = ATTACK_DATA_DIR / new
    if not new_path.is_dir():
        logger.error(
            "The NEW version was not found. Make sure it is a valid ATT&CK version and "
            "has been downloaded to {dir_}.",
            dir_=ATTACK_DATA_DIR,
        )
        sys.exit(1)

    # TODO layers
    stix_diff = StixDiff(old_path, new_path, domains, types, layers=[])

    for domain in domains:
        # Create HTML landing page
        changelog_name = f"{old}-{new}"
        changelog_dir = PUBLIC_DIR / changelog_name
        changelog_dir.mkdir(parents=True, exist_ok=True)
        render_changelog_landing_page(
            stix_diff, changelog_dir, domain, url_prefix, google_analytics_tag
        )

        # Create HTML changelog
        for type_ in types:
            render_changelog_detail_page(
                stix_diff,
                changelog_dir,
                domain,
                type_,
                url_prefix,
                google_analytics_tag,
            )

    # Create JSON changelog
    # logger.info("Creating JSON changelog")
    # changes_dict = stix_diff.get_changes_dict()
    # logger.info("Writing JSON updates to file")
    # Path(json_file).parent.mkdir(parents=True, exist_ok=True)
    # json.dump(changes_dict, open(json_file, "w"), indent=4)

    # TODO layers
    # if layers:
    #     if len(layers) == 0:
    #         # no files specified, e.g. '-layers', use defaults
    #         stix_diff.layers = layer_defaults
    #         layers = layer_defaults
    #     elif len(layers) == 3:
    #         # files specified, e.g. '-layers file.json file2.json file3.json', use specified
    #         # assumes order of files is enterprise, mobile, pre attack (same order as defaults)
    #         stix_diff.layers = layers

    #     layers_dict = stix_diff.get_layers_dict()
    #     layers_dict_to_files(outfiles=layers, layers=layers_dict)


def main():
    """Main entry point."""
    # Parse command line arguments.
    parser = argparse.ArgumentParser(
        description="Build the changelog HTML for a pair of old and new ATT&CK versions."
    )

    parser.add_argument(
        "old",
        type=str,
        help="Name of old ATT&CK version to compare against",
    )
    parser.add_argument(
        "new",
        type=str,
        help="Name of new ATT&CK version to build the changelog for.",
    )
    domain_choices = ["enterprise-attack", "mobile-attack", "ics-attack"]
    parser.add_argument(
        "-d",
        "--domain",
        nargs="+",
        choices=domain_choices,
        default=domain_choices,
        help="Which domains to report on. Defaults to all domains.",
    )
    parser.add_argument(
        "--url-prefix",
        default="/public",
        help="A prefix to apply to generated (default: /public)",
    )
    parser.add_argument(
        "--google-analytics",
        help="Optional: a Google Analytics tracking tag",
    )
    type_choices = [
        "techniques",
        "software",
        "groups",
        "campaigns",
        "mitigations",
        "datasources",
        "datacomponents",
    ]
    parser.add_argument(
        "-t",
        "--type",
        nargs="+",
        choices=type_choices,
        default=type_choices,
        help="Which object types to report on. Defaults to all types.",
    )

    # TODO layers
    # parser.add_argument(
    #     "--layers",
    #     type=str,
    #     nargs="*",
    #     help=f"""
    #         Create layer files showing changes in each domain
    #         expected order of filenames is 'enterprise', 'mobile', 'ics', 'pre attack'.
    #         If values are unspecified, defaults to {", ".join(layer_defaults)}
    #         """,
    # )

    args = parser.parse_args()
    # TODO layers
    # if args.layers is not None:
    #     if len(args.layers) not in [0, 3]:
    #         parser.error(
    #             "-layers requires exactly three files to be specified or none at all"
    #         )

    url_prefix = args.url_prefix.rstrip("/")
    build_changelog(
        old=args.old,
        new=args.new,
        domains=args.domain,
        types=args.type,
        url_prefix=url_prefix,
        google_analytics_tag=args.google_analytics,
        # layers=args.layers, # TODO
    )


if __name__ == "__main__":
    main()
