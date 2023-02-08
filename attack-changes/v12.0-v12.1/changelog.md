## Key

* New objects: ATT&CK objects which are present in the new STIX data but not the old.
* Major version changes: ATT&CK objects that have a major version change. (e.g. 1.0 → 2.0)
* Minor version changes: ATT&CK objects that have a minor version change. (e.g. 1.0 → 1.1)
* Other version changes: ATT&CK objects that have an unexpected version change. (e.g. 1.0 → 1.3)
* Metadata changes: ATT&CK objects that have at least one field changed, but not the version.
* Unknown changes: ATT&CK objects that have changed while the modified time stayed the same.
* Object revocations: ATT&CK objects which are revoked by a different object.
* Object deprecations: ATT&CK objects which are deprecated and no longer in use, and not replaced.
* Object deletions: ATT&CK objects which are no longer found in the STIX data.


## Techniques

### Enterprise

#### Minor Version Changes

* Adversary-in-the-Middle: [LLMNR/NBT-NS Poisoning and SMB Relay](/techniques/T1557/001) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* Establish Accounts: [Cloud Accounts](/techniques/T1585/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

#### Metadata-only Changes

* [Multi-Factor Authentication Interception](/techniques/T1111) <small style="color:#929393">(v2.0)</small>
* Search Open Websites/Domains: [Code Repositories](/techniques/T1593/003) <small style="color:#929393">(v1.0)</small>
* Stage Capabilities: [SEO Poisoning](/techniques/T1608/006) <small style="color:#929393">(v1.0)</small>

### Mobile

### ICS

## Software

### Enterprise

#### Metadata-only Changes

* [DCSrv](/software/S1033) <small style="color:#929393">(v1.0)</small>
* [Heyoka Backdoor](/software/S1027) <small style="color:#929393">(v1.0)</small>
* [MacMa](/software/S1016) <small style="color:#929393">(v1.0)</small>
* [Mongall](/software/S1026) <small style="color:#929393">(v1.0)</small>
* [PingPull](/software/S1031) <small style="color:#929393">(v1.0)</small>
* [PsExec](/software/S0029) <small style="color:#929393">(v1.3)</small>
* [PyDCrypt](/software/S1032) <small style="color:#929393">(v1.0)</small>
* [WhisperGate](/software/S0689) <small style="color:#929393">(v1.0)</small>

### Mobile

### ICS

## Groups

### Enterprise

#### Metadata-only Changes

* [Aoqin Dragon](/groups/G1007) <small style="color:#929393">(v1.0)</small>
* [EXOTIC LILY](/groups/G1011) <small style="color:#929393">(v1.0)</small>
* [Moses Staff](/groups/G1009) <small style="color:#929393">(v1.0)</small>
* [SideCopy](/groups/G1008) <small style="color:#929393">(v1.0)</small>

### Mobile

### ICS

## Campaigns

### Enterprise

### Mobile

### ICS

## Mitigations

### Enterprise

### Mobile

### ICS

## Data Sources

### Enterprise

### Mobile

### ICS

## Data Components

### Enterprise

#### Deprecations

* [Container Metadata](/datasources/DS0032/#Container%20Metadata) <small style="color:#929393">(v1.0)</small>
* [Pod Metadata](/datasources/DS0014/#Pod%20Metadata) <small style="color:#929393">(v1.0)</small>

### Mobile

### ICS

## Contributors to this release

* Manikantan Srinivasan, NEC Corporation India
* Phill Taylor, BT Security
* Vinayak Wadhwa, SAFE Security
* Will Jolliffe
