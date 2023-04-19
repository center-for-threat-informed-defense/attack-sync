from itertools import combinations

from loguru import logger

from .changelog_helper import get_new_changelog_md


def main():
    versions = [
        "8.0",
        "8.1",
        "8.2",
        "9.0",
        "10.0",
        "10.1",
        "11.0",
        "11.1",
        "11.2",
        "11.3",
        "12.0",
        "12.1",
    ]
    domains = ["enterprise-attack", "mobile-attack", "ics-attack"]
    types = [
        "techniques",
        "software",
        "groups",
        "campaigns",
        "mitigations",
        "datasources",
        "datacomponents",
    ]

    for version_pair in combinations(versions, 2):
        old_version = version_pair[0]
        new_version = version_pair[1]

        output_folder = f"output/attack-changes/v{old_version}-v{new_version}"

        print(output_folder)
        for domain in domains:
            logger.warning("in domain " + domain + " of " + str(domains))
            logger.warning("output string is " + output_folder + domain + "index.html")

            for type in types:
                logger.warning("domain is " + domain + " type is  " + type)

                get_new_changelog_md(
                    domains=[domain],
                    types=type,
                    old=f"attack-releases/stix-2.0/v{old_version}",
                    new=f"attack-releases/stix-2.0/v{new_version}",
                    html_file_detailed=f"{output_folder}/{domain}/{type}/index.html",
                )

            get_new_changelog_md(
                domains=[domain],
                old=f"attack-releases/stix-2.0/v{old_version}",
                new=f"attack-releases/stix-2.0/v{new_version}",
                html_file=f"{output_folder}/{domain}/index.html",
            )


if __name__ == "__main__":
    main()
