import json
import re
from pathlib import Path
from typing import Dict

from loguru import logger
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment
from openpyxl.worksheet.table import Table, TableStyleInfo


def get_attack_id(changelog_attack_object: dict):
    attack_id = None
    external_references = changelog_attack_object.get("external_references")

    if external_references:
        attack_source = external_references[0]
        if attack_source.get("external_id") and attack_source.get("source_name") == "mitre-attack":
            attack_id = attack_source["external_id"]

    return attack_id


def get_changed_techniques(changelog: Dict[str, dict]):
    logger.debug("Getting techniques that have changes between ATT&CK versions")
    changed_techniques = {}
    for domain, change_info in changelog.items():
        if domain == "new-contributors":
            continue

        technique_changes = change_info["techniques"]
        for change_type, changes in technique_changes.items():
            for technique_object in changes:
                attack_id = get_attack_id(technique_object)
                technique_object["CHANGE_TYPE"] = change_type
                technique_object["DOMAIN"] = domain
                changed_techniques[attack_id] = technique_object

    return changed_techniques


def main():
    old_version = "10.1"
    new_version = "12.1"
    changelog_json_file = f"data/attack-changelog-v{old_version}-v{new_version}.json"
    original_mapping_file = "data/nist800-53-r4-mappings.xlsx"
    output_dir = "output"
    final_workbook = f"{output_dir}/mapping_diff_attack_v{old_version}-v{new_version}.xlsx"

    with open(changelog_json_file, "r") as file:
        changelog = json.load(file)

    changed_techniques = get_changed_techniques(changelog=changelog)

    logger.debug(f"Loading: {original_mapping_file}")
    mapping_workbook = load_workbook(filename=original_mapping_file)
    mapping_sheet = mapping_workbook["Sheet1"]

    mapping_diff_workbook = Workbook()
    mapping_diff_worksheet = mapping_diff_workbook.active

    rows_to_insert = []

    logger.debug("Providing context for ATT&CK Techniques that have changed")
    for row in mapping_sheet.rows:
        control_id = row[0].value
        technique_id = row[3].value

        # skip parsing header
        if control_id == "Control ID":
            continue

        if technique_id in changed_techniques:
            changed_technique = changed_techniques[technique_id]
            change_type = changed_technique["CHANGE_TYPE"]

            if change_type == "additions":
                continue

            detailed_diff = json.loads(changed_technique.get("detailed_diff", "{}"))
            if detailed_diff:
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

                            if stix_field == "description":
                                rows_to_insert.append(
                                    {
                                        "A": control_id,
                                        "B": technique_id,
                                        "C": "Description",
                                        "D": old_value,
                                        "E": new_value,
                                    }
                                )

            changelog_mitigations = changed_technique.get("changelog_mitigations")
            if changelog_mitigations:
                if changelog_mitigations["new"]:
                    new_value = ""
                    for new_mitigation in changelog_mitigations["new"]:
                        new_value += f"{new_mitigation}\n"
                    rows_to_insert.append(
                        {
                            "A": control_id,
                            "B": technique_id,
                            "C": "New Mitigations",
                            "D": "",
                            "E": new_value.strip(),
                        }
                    )
                if changelog_mitigations["dropped"]:
                    new_value = ""
                    for dropped_mitigation in changelog_mitigations["dropped"]:
                        new_value += f"{dropped_mitigation}\n"
                    rows_to_insert.append(
                        {
                            "A": control_id,
                            "B": technique_id,
                            "C": "Dropped Mitigations",
                            "D": "",
                            "E": new_value.strip(),
                        }
                    )

            changelog_detections = changed_technique.get("changelog_detections")
            if changelog_detections:
                if changelog_detections["new"]:
                    new_value = ""
                    for new_detection in changelog_detections["new"]:
                        new_value += f"{new_detection}\n"
                    rows_to_insert.append(
                        {
                            "A": control_id,
                            "B": technique_id,
                            "C": "New Detections",
                            "D": "",
                            "E": new_value.strip(),
                        }
                    )
                if changelog_detections["dropped"]:
                    new_value = ""
                    for dropped_detections in changelog_detections["dropped"]:
                        new_value += f"{dropped_detections}\n"
                    rows_to_insert.append(
                        {
                            "A": control_id,
                            "B": technique_id,
                            "C": "Dropped Detections",
                            "D": "",
                            "E": new_value.strip(),
                        }
                    )

    logger.debug("Sorting by ATT&CK Technique ID")
    sorted_rows = sorted(rows_to_insert, key=lambda x: x["B"])

    mapping_diff_worksheet.append(
        {
            "A": "Control ID",
            "B": "ATT&CK Technique ID",
            "C": "Technique Field Change",
            "D": f"ATT&CK v{old_version}",
            "E": f"ATT&CK v{new_version}",
        }
    )

    logger.debug(f"Writing data to: {final_workbook}")
    for row in sorted_rows:
        mapping_diff_worksheet.append(row)

    ###########
    # Style it!
    ###########
    logger.debug("Widening columns D & E")
    mapping_diff_worksheet.column_dimensions["D"].width = 100
    mapping_diff_worksheet.column_dimensions["E"].width = 100

    # display data as an Excel table
    final_cell = None
    logger.debug("Wrapping text for Columns D & E")
    for row in mapping_diff_worksheet.rows:
        final_cell = row[4]
        row[3].alignment = Alignment(wrap_text=True)
        row[4].alignment = Alignment(wrap_text=True)

    logger.debug("Setting data as an Excel Table")
    tab = Table(displayName="Table1", ref=f"A1:{final_cell.coordinate}")
    style = TableStyleInfo(
        name="TableStyleLight10",
        showFirstColumn=False,
        showLastColumn=False,
        showRowStripes=True,
        showColumnStripes=True,
    )
    tab.tableStyleInfo = style
    mapping_diff_worksheet.add_table(tab)

    logger.debug(f"Creating output directory: {output_dir}")
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # save workbook
    logger.debug(f"Saving file: {final_workbook}")
    mapping_diff_workbook.save(filename=final_workbook)


if __name__ == "__main__":
    main()
