from .changelog_builder import build_changelog


def test_changelog():
    """A dummy test to measure coverage in changelog_builder.py"""
    build_changelog(
        "v10.0",
        "v12.0",
        ["enterprise-attack", "mobile-attack", "ics-attack"],
        [
            "techniques",
            "software",
            "groups",
            "campaigns",
            "mitigations",
            "datasources",
            "datacomponents",
        ],
        "/public",
    )
