from typing import Dict, List, Optional
import json
import re

from jinja2 import Environment, FileSystemLoader;

environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("accordian-item.html")

def buildAccordianItem(changeItem, name, domain, changeType, objectType, index):
    attack_id = get_attack_id(changeItem)
    object_version = get_attack_object_version(stix_obj=changeItem)
    version_change = changeItem.get("version_change")

    revoked_by_name = ""
    revoked_by_id = ""
    revoked_by_description = ""
    values_changed = []
    iterable_added = []
    iterable_removed = []
    dict_added = []
    dict_removed = []
    if changeType == "revocations":
        revoked_by_id = get_attack_id(changeItem["revoked_by"])
        revoked_by_name = changeItem["revoked_by"]["name"]
        revoked_by_description = changeItem["revoked_by"]["description"]

    detailed_diff = json.loads(changeItem.get("detailed_diff", "{}"))
    if detailed_diff:
        # the deepdiff library displays differences with a prefix of: root['<top-level-key-we-care-about>']
        regex = r"^root\['(?P<top_stix_key>[^\']*)'\](?P<the_rest>.*)$"
        for detailed_change_type, detailed_changes in detailed_diff.items():
            if detailed_change_type == "values_changed":
                for detailed_change, values in detailed_changes.items():
                    matches = re.search(regex, detailed_change)
                    top_stix_key = matches.group("top_stix_key")
                    the_rest = matches.group("the_rest")
                    stix_field = f"{top_stix_key}{the_rest}"
                    old_value = values["old_value"]
                    new_value = values["new_value"]
                    values_changed.append({'stix':stix_field, 'old': old_value, 'new': new_value})
                    
            elif detailed_change_type == "iterable_item_added":
                for detailed_change, new_value in detailed_changes.items():
                    stix_field = re.search(regex, detailed_change).group("top_stix_key")
                    iterable_added.append({'stix':stix_field, 'old': "", 'new': new_value})

            elif detailed_change_type == "iterable_item_removed":
                for detailed_change, old_value in detailed_changes.items():
                    stix_field = re.search(regex, detailed_change).group("top_stix_key")
                    iterable_removed.append({'stix':stix_field, 'old': old_value, 'new': ""})

            elif detailed_change_type == "dictionary_item_added":
                for detailed_change, new_value in detailed_changes.items():
                    stix_field = re.search(regex, detailed_change).group("top_stix_key")
                    dict_added.append({'stix':stix_field, 'old': "", 'new': new_value})


            elif detailed_change_type == "dictionary_item_removed":
                for detailed_change, old_value in detailed_changes.items():
                    stix_field = re.search(regex, detailed_change).group("top_stix_key")
                    dict_removed.append({'stix':stix_field, 'old': old_value, 'new': ""})

    content = template.render(
        stix_object = changeItem,
        itemId = attack_id,
        accordianId=index,
        itemTitle =  name,
        itemVersionChange = version_change,
        itemVersionOld = "",
        itemVersionNew =  object_version,
        itemDescriptionOld=changeItem['description'],
        itemDescriptionNew= changeItem['description'],
        domain=domain,
        changeType=changeType,
        objectType = objectType,
        revoked_by_id = revoked_by_id,
        revoked_by_description = revoked_by_description,
        revoked_by_name= revoked_by_name,
        detailed_diff=detailed_diff,
        values_changed=values_changed,
        iterable_added=iterable_added,
        iterable_removed=iterable_removed,
        dict_added=dict_added,
        dict_removed=dict_removed
    )
    return content

def get_attack_id(stix_obj: dict) -> Optional[str]:
    """Get the object's ATT&CK ID.

    Parameters
    ----------
    stix_obj : dict
        An ATT&CK STIX Domain Object (SDO).

    Returns
    -------
    str (optional)
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


def get_attack_object_version(stix_obj: dict) -> Optional[float]:
    """Get the object's ATT&CK version.

    Parameters
    ----------
    stix_obj : dict
        An ATT&CK STIX Domain Object (SDO).

    Returns
    -------
    Optional[float]
        The object version of the ATT&CK object. Defaults to 0.0
    """
    # ICS objects didn't have x_mitre_version until v11.0, so pretend they were version 0.0
    version = stix_obj.get("x_mitre_version", 0)
    return float(version)
