import multiprocessing
import os
import shutil
from argparse import ArgumentParser, Namespace
from collections import defaultdict
from itertools import combinations
from typing import TypeAlias

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
    parser.add_argument(
        "--no-parallel",
        action="store_true",
        help="Disable parallel build, which slows things down but may be useful for debugging build errors",
    )
    return parser.parse_args()


Version: TypeAlias = tuple[int, int]


def get_version_pairs(
    versions: list[Version],
) -> dict[Version, list[Version]]:
    """
    Create pairs of versions that we want to render.

    Currently, we are generating every version combination. However, in the past we have only generated major version comparisons.

    Args:
        versions - a list of (major, minor) version tuples

    Yields:
        a dictionary where the keys are versions and the values are the
        corresponding versions that we build
    """
    pairs: list[Version] = defaultdict(list)

    for major1, minor1 in sorted(versions):
        for major2, minor2 in sorted(versions):
            if (
                (major1 != minor2 or minor1 != minor2)
                and  (major1, minor1) !=  (major2, minor2)
                and (major1, minor1) not in pairs[(major2, minor2)]
            ):
                pairs[(major1, minor1)].append((major2, minor2))

    return pairs


def main():
    # Versions are expressed as (major, minor) tuples.
    args = parse_args()
    url_prefix = args.url_prefix.rstrip("/")
    versions: list[Version] = [
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
        (14, 0),
        (14, 1),
        (15, 0),
        (15, 1),
        (16, 0),
        (16, 1),
        (17, 0),
        (17, 1),
        (18, 0),
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
        "detectionstrategies",
        "analytics",
    ]

    # Copy static files.
    static_dir = PUBLIC_DIR / "static"
    logger.info("Copying static resources: {}", static_dir)
    shutil.copytree(TEMPLATE_DIR / "static", static_dir, dirs_exist_ok=True)

    # Build the site index.html
    version_pairs = get_version_pairs(versions)
    index_path = PUBLIC_DIR / "index.html"
    logger.info("Creating site index: {}", index_path)
    index_template = load_template("site-index.html.j2")
    index_stream = index_template.stream(
        versions=versions,
        version_pairs=version_pairs,
        domains=domains,
        domain_names=domain_names,
        url_prefix=url_prefix,
        google_analytics_tag=args.google_analytics,
    )
    index_stream.dump(str(index_path))

    # Build changelogs for each pair of versions.
    pair_count = sum(len(pairs) for pairs in version_pairs.values())
    build_list = list()
    for old_version, new_versions in version_pairs.items():
        for new_version in new_versions:
            build_list.append((old_version, new_version))

    if not args.no_changelogs:
        logger.info("Need to generate {} changelogs", pair_count)
        if args.no_parallel:
            # Run without multiprocessing
            logger.info("Running without parallelism...")
            for (old_major, old_minor), (new_major, new_minor) in build_list:
                build_worker(
                    old_major,
                    old_minor,
                    new_major,
                    new_minor,
                    domains,
                    types,
                    url_prefix,
                    args.google_analytics,
                )
        else:
            # Run with multiprocessing
            num_workers = os.cpu_count()
            pool = multiprocessing.Pool(num_workers)
            logger.info("Running with {} parallel processes", num_workers)
            jobs = list()
            for (old_major, old_minor), (new_major, new_minor) in build_list:
                jobs.append(
                    (
                        old_major,
                        old_minor,
                        new_major,
                        new_minor,
                        domains,
                        types,
                        url_prefix,
                        args.google_analytics,
                    )
                )
            pool.starmap(build_worker, jobs)


def build_worker(
    old_major,
    old_minor,
    new_major,
    new_minor,
    domains,
    types,
    url_prefix,
    google_analytics,
):
    """
    This worker is called for each version pair. It can be run in a separate process
    using multiprocessing.

    Note: all the arguments need to be pickle-able to be transferred across a process boundary.
    """
    old_version = f"v{old_major}.{old_minor}"
    new_version = f"v{new_major}.{new_minor}"
    logger.info("Building changelog for {} → {}", old_version, new_version)
    build_changelog(
        domains=domains,
        types=types,
        old=old_version,
        new=new_version,
        url_prefix=url_prefix,
        google_analytics_tag=google_analytics,
    )


if __name__ == "__main__":
    main()
