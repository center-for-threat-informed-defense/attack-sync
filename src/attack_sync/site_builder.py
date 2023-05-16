import shutil
from argparse import ArgumentParser, Namespace
from itertools import combinations
from pathlib import Path

from loguru import logger

from .changelog_builder import build_changelog
from .template import PUBLIC_DIR, TEMPLATE_DIR, load_template


def parse_args() -> Namespace:
    parser = ArgumentParser(description="Build the ATT&CK Sync website.")
    parser.add_argument(
        "--url-prefix",
        default="",
        help="Optional: a prefix to apply to generated URLs, e.g. if hosting on GitHub "
        "Pages (with no trailing slash)",
    )
    parser.add_argument(
        "--google-analytics",
        help="Optional: a Google Analytics tracking tag",
    )
    parser.add_argument(
        "--no-changelogs",
        action="store_true",
        help="Copy static and create indexes, but do not create changelogs (for development)",
    )
    return parser.parse_args()


def main():
    # Versions are expressed as (major, minor) tuples.
    args = parse_args()
    url_prefix = args.url_prefix.rstrip("/")
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
        (13, 1),
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
        versions=versions,
        domains=domains,
        domain_names=domain_names,
        url_prefix=url_prefix,
        google_analytics_tag=args.google_analytics,
    )
    index_stream.dump(str(index_path))

    # Build changelogs for each pair of versions.
    if not args.no_changelogs:
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
                url_prefix=url_prefix,
                google_analytics_tag=args.google_analytics,
            )


if __name__ == "__main__":
    main()
