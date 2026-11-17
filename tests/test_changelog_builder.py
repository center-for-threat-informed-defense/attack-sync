import json
from pathlib import Path

import pytest
from deepdiff import DeepDiff

from attack_sync.changelog_builder import (
    StixDiff,
    _get_attack_source_path,
    _load_stix_with_homeland_justice_date_fix,
    build_changelog,
    deep_copy_stix,
)


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


@pytest.fixture
def homeland_justice_bundle():
    return {
        "type": "bundle",
        "id": "bundle--22cc8244-0209-46b4-97d4-9b55c1bfc6b4",
        "objects": [
            {
                "type": "campaign",
                "spec_version": "2.1",
                "id": "campaign--7e21077d-2589-43a7-a5f9-490061289526",
                "name": "HomeLand Justice",
                "created": "2024-01-01T00:00:00.000Z",
                "modified": "2024-01-01T00:00:00.000Z",
                "first_seen": "2021-05-01T04:00:00.000Z",
                "last_seen": "2002-09-01T04:00:00.000Z",
            }
        ],
    }


def test_preserve_historical_campaign_date(
    tmp_path, monkeypatch, homeland_justice_bundle
):
    path = tmp_path / "v16.0" / "enterprise-attack.json"
    path.parent.mkdir()
    original = json.dumps(homeland_justice_bundle)
    path.write_text(original)
    warnings = []
    monkeypatch.setattr(
        "attack_sync.changelog_builder.logger.warning",
        lambda message, *args: warnings.append(message.format(*args)),
    )

    store = _load_stix_with_homeland_justice_date_fix(path)
    campaign = store.get(homeland_justice_bundle["objects"][0]["id"])

    assert campaign["last_seen"].year == 2002
    assert json.loads(campaign.serialize())["last_seen"] == "2002-09-01T04:00:00.000Z"
    assert path.read_text() == original
    assert len(warnings) == 1
    assert campaign["id"] in warnings[0]
    assert "parsing only" in warnings[0]
    assert "restored original 2002-09-01T04:00:00.000Z" in warnings[0]

    # Exercise the same dictionary conversion and comparison used by Sync.
    old = deep_copy_stix([campaign])[0]
    new = dict(old, last_seen="2022-09-01 04:00:00+00:00")
    changes = json.loads(DeepDiff(old, new, ignore_order=True).to_json())
    assert changes["values_changed"]["root['last_seen']"] == {
        "old_value": "2002-09-01 04:00:00+00:00",
        "new_value": "2022-09-01 04:00:00+00:00",
    }
    assert "9999" not in json.dumps(old)


@pytest.mark.parametrize(
    "variation", ["version", "domain", "id", "first_seen", "last_seen"]
)
def test_campaign_correction_does_not_relax_other_validation(
    tmp_path, homeland_justice_bundle, variation
):
    campaign = homeland_justice_bundle["objects"][0]
    version = "v16.1" if variation == "version" else "v16.0"
    domain = "mobile-attack" if variation == "domain" else "enterprise-attack"
    if variation == "id":
        campaign["id"] = "campaign--22cc8244-0209-46b4-97d4-9b55c1bfc6b4"
    elif variation == "first_seen":
        campaign["first_seen"] = "2020-05-01T04:00:00.000Z"
    elif variation == "last_seen":
        campaign["last_seen"] = "2003-09-01T04:00:00.000Z"
    path = tmp_path / version / f"{domain}.json"
    path.parent.mkdir()
    path.write_text(json.dumps(homeland_justice_bundle))

    with pytest.raises(ValueError, match="last_seen.*first_seen"):
        _load_stix_with_homeland_justice_date_fix(path)


def test_correct_campaign_date_is_left_alone(
    tmp_path, monkeypatch, homeland_justice_bundle
):
    homeland_justice_bundle["objects"][0]["last_seen"] = "2023-09-01T04:00:00.000Z"
    path = tmp_path / "v16.0" / "enterprise-attack.json"
    path.parent.mkdir()
    path.write_text(json.dumps(homeland_justice_bundle))
    warnings = []
    monkeypatch.setattr(
        "attack_sync.changelog_builder.logger.warning",
        lambda *args: warnings.append(args),
    )

    store = _load_stix_with_homeland_justice_date_fix(path)

    assert (
        store.get(homeland_justice_bundle["objects"][0]["id"])["last_seen"].year == 2023
    )
    assert not warnings


@pytest.mark.parametrize("version", ["v11.0", "v11.1", "v11.2"])
def test_mobile_beta_comparison_keeps_numeric_urls(tmp_path, monkeypatch, version):
    data_dir = tmp_path / "stix-2.1"
    public_dir = tmp_path / "public"
    (data_dir / version).mkdir(parents=True)
    beta_dir = data_dir / f"{version}-beta"
    beta_dir.mkdir()
    final_dir = data_dir / "v11.3"
    final_dir.mkdir()
    bundle = {
        "type": "bundle",
        "id": "bundle--22cc8244-0209-46b4-97d4-9b55c1bfc6b4",
        "objects": [],
    }
    for directory in (beta_dir, final_dir):
        (directory / "mobile-attack.json").write_text(json.dumps(bundle))
    monkeypatch.setattr("attack_sync.changelog_builder.ATTACK_DATA_DIR", data_dir)
    monkeypatch.setattr("attack_sync.changelog_builder.PUBLIC_DIR", public_dir)
    releases = []

    def detect_release(**kwargs):
        releases.append(kwargs)
        return Path(kwargs["stix_file"]).parent.name.removeprefix("v")

    monkeypatch.setattr(
        "attack_sync.changelog_builder.release_info.get_attack_version", detect_release
    )

    build_changelog(
        old=version,
        new="v11.3",
        domains=["mobile-attack"],
        types=["techniques"],
        url_prefix="",
        google_analytics_tag=None,
    )

    assert [r["stix_file"] for r in releases] == [
        str(beta_dir / "mobile-attack.json"),
        str(final_dir / "mobile-attack.json"),
    ]
    assert all(r["stix_version"] == "2.1" for r in releases)
    output = public_dir / f"{version}-v11.3"
    for page in ["mobile-attack/index.html", "mobile-attack/techniques/index.html"]:
        html = (output / page).read_text()
        assert f"{version}-beta beta release" in html
        assert f"/{version}-v11.3/" in html
    assert (output / f"attack-changelog-{version}-v11.3.json.gz").exists()
    assert not (data_dir / version / "mobile-attack.json").exists()


@pytest.mark.parametrize(
    "format_,version,domain",
    [
        ("stix-2.1", "v11.0", "enterprise-attack"),
        ("stix-2.1", "v11.1", "ics-attack"),
        ("stix-2.0", "v11.0", "mobile-attack"),
        ("stix-2.1", "v11.3", "mobile-attack"),
        ("stix-2.1", "v12.0", "mobile-attack"),
    ],
)
def test_other_sources_are_not_mapped(tmp_path, format_, version, domain):
    directory = tmp_path / format_ / version
    assert _get_attack_source_path(directory, domain) == directory / f"{domain}.json"
    diff = StixDiff.__new__(StixDiff)
    diff.old_path = directory
    diff.new_path = directory.with_name("v20.1")
    assert diff.get_source_notes(domain) == []
