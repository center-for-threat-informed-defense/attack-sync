import pytest

from attack_sync.changelog_builder import StixDiff


@pytest.mark.parametrize("section", ["additions", "revocations", "deletions"])
@pytest.mark.parametrize(
    "has_relationship,parent_exists,parent_changed",
    [
        (False, True, False),
        (True, False, False),
        (True, True, False),
        (True, True, True),
    ],
)
def test_export_preserves_subtechniques(
    section, has_relationship, parent_exists, parent_changed
):
    parent = {
        "id": "attack-pattern--parent",
        "name": "Z Parent",
        "external_references": [{"external_id": "T1000"}],
    }
    child = {
        "id": "attack-pattern--child",
        "name": "A Child",
        "x_mitre_is_subtechnique": True,
        "external_references": [{"external_id": "T1000.001"}],
    }
    relationships = (
        {"relationship": {"source_ref": child["id"], "target_ref": parent["id"]}}
        if has_relationship
        else {}
    )
    objects = {child["id"]: child}
    if parent_exists:
        objects[parent["id"]] = parent
    state = {
        "relationships": {"subtechniques": relationships},
        "attack_objects": {
            "techniques": objects,
            "datacomponents": {},
            "datasources": {},
        },
    }
    changes = [child, parent] if parent_changed else [child]
    diff = StixDiff.__new__(StixDiff)
    diff.domains = ["enterprise-attack"]
    diff.release_contributors = {}
    diff.data = {
        # Only provide the appropriate version to also check deletion handling.
        "old" if section == "deletions" else "new": {"enterprise-attack": state},
        "changes": {"techniques": {"enterprise-attack": {section: changes}}},
    }

    exported = diff.get_changes_dict()["enterprise-attack"]["techniques"][section]

    # The parent is exported only if it changed, and remains ahead of its child.
    assert exported == ([parent, child] if parent_changed else [child])
