from itertools import combinations
from pathlib import Path
import shutil

from loguru import logger

from .changelog_builder import build_changelog
from .template import PUBLIC_DIR, TEMPLATE_DIR, load_template


def main():
    # Versions are expressed as (major, minor) tuples.
    versions = [
        (8, 0),
        (8, 1),
        (8, 2),
        (9, 0),
        (10, 0),
        (10, 1),
        (11, 0),
        (11, 1),
        (11, 2),
        (11, 3),
        (12, 0),
        (12, 1),
        (13, 0),
    ]
    domains = [
        "enterprise-attack",
        "mobile-attack",
        "ics-attack",
    ]
    domain_names = {
        "enterprise-attack": "Enterprise ATT&CK",
        "mobile-attack": "Mobile ATT&CK",
        "ics-attack": "ICS ATT&CK",
    }
    types = [
        "techniques",
        "software",
        "groups",
        "campaigns",
        "mitigations",
        "datasources",
        "datacomponents",
    ]

    # Copy static files.
    static_dir = PUBLIC_DIR / "static"
    logger.info("Copying static resources: {}", static_dir)
    shutil.copytree(TEMPLATE_DIR / "static", static_dir, dirs_exist_ok=True)

    # Build the site index.html
    index_path = PUBLIC_DIR / "index.html"
    logger.info("Creating site index: {}", index_path)
    index_template = load_template("site-index.html.j2")
    index_stream = index_template.stream(
        versions=versions, domains=domains, domain_names=domain_names
    )
    index_stream.dump(str(index_path))

    # Build the about page
    about_dir = PUBLIC_DIR / "about"
    about_dir.mkdir(parents=True, exist_ok=True)
    about_path = about_dir / "index.html"
    logger.info("Creating site about page: {}", about_path)
    index_template = load_template("site-about.html.j2")
    index_template.stream().dump(str(about_path))

    # Build changelogs for each pair of versions.
    changelog_count = int((len(versions) * (len(versions) - 1)) / 2)
    logger.info("Need to generate {} changelogs", changelog_count)
    for (old_major, old_minor), (new_major, new_minor) in combinations(versions, 2):
        old_version = f"v{old_major}.{old_minor}"
        new_version = f"v{new_major}.{new_minor}"
        logger.info("Building changelog for {} → {}", old_version, new_version)
        build_changelog(
            domains=domains,
            types=types,
            old=old_version,
            new=new_version,
        )


if __name__ == "__main__":
    main()