from itertools import combinations

from mitreattack.diffStix.changelog_helper import get_new_changelog_md


def main():
    versions = [
        # "8.0",
        # "8.1",
        # "8.2",
        "9.0",
        # "10.0",
        "10.1",
        # "11.0",
        # "11.1",
        # "11.2",
        # "11.3",
        # "12.0",
        "12.1",
    ]

    for version_pair in combinations(versions, 2):
        old_version = version_pair[0]
        new_version = version_pair[1]

        output_folder = f"output/attack-changes/v{old_version}-v{new_version}"

        print(output_folder)

        get_new_changelog_md(
            domains=["enterprise-attack", "mobile-attack", "ics-attack"],
            layers=[
                f"{output_folder}/layer-enterprise.json",
                f"{output_folder}/layer-mobile.json",
                f"{output_folder}/layer-ics.json",
            ],
            old=f"attack-releases/stix-2.0/v{old_version}",
            new=f"attack-releases/stix-2.0/v{new_version}",
            show_key=True,
            verbose=True,
            include_contributors=True,
            markdown_file=f"{output_folder}/changelog.md",
            html_file=f"{output_folder}/index.html",
            html_file_detailed=f"{output_folder}/changelog-detailed.html",
            json_file=f"{output_folder}/changelog.json",
        )


if __name__ == "__main__":
    main()
