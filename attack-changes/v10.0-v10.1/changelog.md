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

* Create or Modify System Process: [Launch Agent](/techniques/T1543/001) <small style="color:#929393">(v1.2&#8594;v1.3)</small>

#### Metadata-only Changes

* [Create or Modify System Process](/techniques/T1543) <small style="color:#929393">(v1.0)</small>
* [Reflective Code Loading](/techniques/T1620) <small style="color:#929393">(v1.0)</small>

### Mobile

#### Metadata-only Changes

* [Install Insecure or Malicious Configuration](/techniques/T1478) <small style="color:#929393">(v1.0)</small>

### ICS

## Software

### Enterprise

#### Metadata-only Changes

* [BS2005](/software/S0014) <small style="color:#929393">(v1.1)</small>
* [Kobalos](/software/S0641) <small style="color:#929393">(v1.0)</small>
* [MarkiRAT](/software/S0652) <small style="color:#929393">(v1.0)</small>

#### Deprecations

* [TRITON](/software/S0609) <small style="color:#929393">(v1.0)</small>

### Mobile

#### Metadata-only Changes

* [Monokle](/software/S0407) <small style="color:#929393">(v1.2)</small>

### ICS

## Groups

### Enterprise

#### Metadata-only Changes

* [Ferocious Kitten](/groups/G0137) <small style="color:#929393">(v1.0)</small>
* [Ke3chang](/groups/G0004) <small style="color:#929393">(v1.4)</small>
* [Orangeworm](/groups/G0071) <small style="color:#929393">(v1.1)</small>
* [Patchwork](/groups/G0040) <small style="color:#929393">(v1.4)</small>
* [Transparent Tribe](/groups/G0134) <small style="color:#929393">(v1.0)</small>
* [Winnti Group](/groups/G0044) <small style="color:#929393">(v1.1)</small>

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

#### Metadata-only Changes

* [Active Directory](/datasources/DS0026) <small style="color:#929393">(v1.0)</small>
* [Cloud Service](/datasources/DS0025) <small style="color:#929393">(v1.0)</small>
* [Cloud Storage](/datasources/DS0010) <small style="color:#929393">(v1.0)</small>
* [Cluster](/datasources/DS0031) <small style="color:#929393">(v1.0)</small>
* [Command](/datasources/DS0017) <small style="color:#929393">(v1.0)</small>
* [Container](/datasources/DS0032) <small style="color:#929393">(v1.0)</small>
* [Drive](/datasources/DS0016) <small style="color:#929393">(v1.0)</small>
* [Driver](/datasources/DS0027) <small style="color:#929393">(v1.0)</small>
* [File](/datasources/DS0022) <small style="color:#929393">(v1.0)</small>
* [Firewall](/datasources/DS0018) <small style="color:#929393">(v1.0)</small>
* [Firmware](/datasources/DS0001) <small style="color:#929393">(v1.0)</small>
* [Group](/datasources/DS0036) <small style="color:#929393">(v1.0)</small>
* [Image](/datasources/DS0007) <small style="color:#929393">(v1.0)</small>
* [Kernel](/datasources/DS0008) <small style="color:#929393">(v1.0)</small>
* [Logon Session](/datasources/DS0028) <small style="color:#929393">(v1.0)</small>
* [Module](/datasources/DS0011) <small style="color:#929393">(v1.0)</small>
* [Named Pipe](/datasources/DS0023) <small style="color:#929393">(v1.0)</small>
* [Network Share](/datasources/DS0033) <small style="color:#929393">(v1.0)</small>
* [Network Traffic](/datasources/DS0029) <small style="color:#929393">(v1.0)</small>
* [Pod](/datasources/DS0014) <small style="color:#929393">(v1.0)</small>
* [Process](/datasources/DS0009) <small style="color:#929393">(v1.0)</small>
* [Scheduled Job](/datasources/DS0003) <small style="color:#929393">(v1.0)</small>
* [Script](/datasources/DS0012) <small style="color:#929393">(v1.0)</small>
* [Sensor Health](/datasources/DS0013) <small style="color:#929393">(v1.0)</small>
* [Service](/datasources/DS0019) <small style="color:#929393">(v1.0)</small>
* [Snapshot](/datasources/DS0020) <small style="color:#929393">(v1.0)</small>
* [User Account](/datasources/DS0002) <small style="color:#929393">(v1.0)</small>
* [Volume](/datasources/DS0034) <small style="color:#929393">(v1.0)</small>
* [WMI](/datasources/DS0005) <small style="color:#929393">(v1.0)</small>

### Mobile

### ICS

## Data Components

### Enterprise

### Mobile

### ICS

## Contributors to this release

* Center for Threat-Informed Defense (CTID)
* Hiroki Nagahama, NEC Corporation
* Lior Ribak, SentinelOne
* Manikantan Srinivasan, NEC Corporation India
* Pooja Natarajan, NEC Corporation India
