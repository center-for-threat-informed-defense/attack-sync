# ATT&CK Sync

ATT&CK Sync...

- [ATT\&CK Sync](#attck-sync)
  - [Pre-requisites](#pre-requisites)
  - [Run Locally](#run-locally)
  - [Samples](#samples)
  - [Wiki](#wiki)
  - [Notice](#notice)
  - [License](#license)
  - [Acknowledgements](#acknowledgements)

## Pre-requisites

- Python 3.10 or later is recommended for running the scripts in this repository.
- The following files need to be downloaded and placed in the `data/` directory
  - `nist800-53-r4-mappings.xlsx` from the [center-for-threat-informed-defense/attack-control-framework-mappings](https://github.com/center-for-threat-informed-defense/attack-control-framework-mappings/tree/main/frameworks/attack_10_1/nist800_53_r4) repository.
  - `nist800-53-r5-mappings.xlsx` from the [center-for-threat-informed-defense/attack-control-framework-mappings](https://github.com/center-for-threat-informed-defense/attack-control-framework-mappings/tree/main/frameworks/attack_10_1/nist800_53_r5) repository.

## Run Locally

```bash
  # Install project requirements (in a virtual environment)
  pip install -r requirements.txt

  # Download ATT&CK STIX files. This command comes from https://github.com/mitre-attack/mitreattack-python
  download_attack_stix --stix20 --all -d attack-releases

  # Create ATT&CK changelogs in output/attack-changes/
  python create_attack_changelogs.py

  # Create Excel file based on previous ATT&CK mapping in output/mapping_diff_attack_v<old_version>-v<new_version>.xlsx
  python generate_mapping_excel.py
```

## Samples

There is some sample output in the [samples](samples/) directory which includes the following:

- `samples/attack-changes/v10.1-v12.1/`: Output from `create_attack_changelogs.py` for ATT&CK v10.1 and v12.1
- `samples/mapping_diff_attack_v10.1-v12.1.xlsx`: Output from `generate_mapping_excel.py`

## Wiki

Check out our [wiki](https://github.com/center-for-threat-informed-defense/attack-sync/wiki) for more information about how to [contribute](/CONTRIBUTING.md) and set up a development environment.

## Notice

Copyright 2023 MITRE Engenuity. Approved for public release. Document number XXXXX

## License

[Apache 2.0](https://choosealicense.com/licenses/apache-2.0/)

## Acknowledgements

This project makes use of ATT&CK®

[ATT&CK Terms of Use](https://attack.mitre.org/resources/terms-of-use/)
