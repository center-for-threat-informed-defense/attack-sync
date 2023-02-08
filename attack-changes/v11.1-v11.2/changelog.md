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

#### Metadata-only Changes

* Account Manipulation: [Additional Cloud Credentials](/techniques/T1098/001) <small style="color:#929393">(v2.3)</small>
* Account Manipulation: [Additional Cloud Roles](/techniques/T1098/003) <small style="color:#929393">(v2.0)</small>
* Boot or Logon Autostart Execution: [Registry Run Keys / Startup Folder](/techniques/T1547/001) <small style="color:#929393">(v1.1)</small>
* Create or Modify System Process: [Windows Service](/techniques/T1543/003) <small style="color:#929393">(v1.2)</small>
* Credentials from Password Stores: [Windows Credential Manager](/techniques/T1555/004) <small style="color:#929393">(v1.0)</small>
* [Data from Local System](/techniques/T1005) <small style="color:#929393">(v1.4)</small>
* Impair Defenses: [Downgrade Attack](/techniques/T1562/010) <small style="color:#929393">(v1.1)</small>
* [Ingress Tool Transfer](/techniques/T1105) <small style="color:#929393">(v2.1)</small>
* [Network Sniffing](/techniques/T1040) <small style="color:#929393">(v1.3)</small>
* OS Credential Dumping: [LSASS Memory](/techniques/T1003/001) <small style="color:#929393">(v1.1)</small>
* Obfuscated Files or Information: [HTML Smuggling](/techniques/T1027/006) <small style="color:#929393">(v1.0)</small>
* System Binary Proxy Execution: [MMC](/techniques/T1218/014) <small style="color:#929393">(v2.0)</small>
* System Binary Proxy Execution: [Verclsid](/techniques/T1218/012) <small style="color:#929393">(v2.0)</small>
* [System Network Configuration Discovery](/techniques/T1016) <small style="color:#929393">(v1.4)</small>
* Use Alternate Authentication Material: [Application Access Token](/techniques/T1550/001) <small style="color:#929393">(v1.3)</small>
* User Execution: [Malicious File](/techniques/T1204/002) <small style="color:#929393">(v1.2)</small>

### Mobile

### ICS

#### Metadata-only Changes

* [Change Operating Mode](/techniques/T0858) <small style="color:#929393">(v1.0)</small>
* [Commonly Used Port](/techniques/T0885) <small style="color:#929393">(v1.0)</small>
* [Detect Operating Mode](/techniques/T0868) <small style="color:#929393">(v1.0)</small>
* [Man in the Middle](/techniques/T0830) <small style="color:#929393">(v1.0)</small>
* [Manipulation of Control](/techniques/T0831) <small style="color:#929393">(v1.0)</small>
* [Modify Parameter](/techniques/T0836) <small style="color:#929393">(v1.0)</small>
* [Module Firmware](/techniques/T0839) <small style="color:#929393">(v1.0)</small>
* [Network Connection Enumeration](/techniques/T0840) <small style="color:#929393">(v1.0)</small>
* [Rootkit](/techniques/T0851) <small style="color:#929393">(v1.0)</small>
* [Unauthorized Command Message](/techniques/T0855) <small style="color:#929393">(v1.0)</small>
* [Valid Accounts](/techniques/T0859) <small style="color:#929393">(v1.0)</small>

#### Unknown Changes

* [Damage to Property](/techniques/T0879) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [Data from Information Repositories](/techniques/T0811) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [Loss of Control](/techniques/T0827) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [Remote Services](/techniques/T0886) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [Spearphishing Attachment](/techniques/T0865) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [User Execution](/techniques/T0863) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>

## Software

### Enterprise

#### Metadata-only Changes

* [AdFind](/software/S0552) <small style="color:#929393">(v1.0)</small>
* [Backdoor.Oldrea](/software/S0093) <small style="color:#929393">(v2.0)</small>
* [Bad Rabbit](/software/S0606) <small style="color:#929393">(v1.0)</small>
* [BlackEnergy](/software/S0089) <small style="color:#929393">(v1.3)</small>
* [Conficker](/software/S0608) <small style="color:#929393">(v1.0)</small>
* [Duqu](/software/S0038) <small style="color:#929393">(v1.2)</small>
* [EKANS](/software/S0605) <small style="color:#929393">(v2.0)</small>
* [Flame](/software/S0143) <small style="color:#929393">(v1.1)</small>
* [Industroyer](/software/S0604) <small style="color:#929393">(v1.0)</small>
* [IronNetInjector](/software/S0581) <small style="color:#929393">(v1.0)</small>
* [KillDisk](/software/S0607) <small style="color:#929393">(v1.1)</small>
* [LockerGoga](/software/S0372) <small style="color:#929393">(v2.0)</small>
* [NotPetya](/software/S0368) <small style="color:#929393">(v2.0)</small>
* [Stuxnet](/software/S0603) <small style="color:#929393">(v1.1)</small>
* [WannaCry](/software/S0366) <small style="color:#929393">(v1.1)</small>

### Mobile

### ICS

#### New Software

* [Bad Rabbit](/Software/S0005) <small style="color:#929393">(v1.0)</small>
* [BlackEnergy 3](/Software/S0004) <small style="color:#929393">(v1.0)</small>
* [Conficker](/Software/S0012) <small style="color:#929393">(v1.0)</small>
* [EKANS](/Software/S0017) <small style="color:#929393">(v1.0)</small>
* [Industroyer](/Software/S0001) <small style="color:#929393">(v1.0)</small>
* [Killdisk](/Software/S0016) <small style="color:#929393">(v1.0)</small>
* [Stuxnet](/Software/S0010) <small style="color:#929393">(v1.0)</small>

#### Metadata-only Changes

* [Backdoor.Oldrea](/software/S0093) <small style="color:#929393">(v2.0)</small>
* [Bad Rabbit](/software/S0606) <small style="color:#929393">(v1.0)</small>
* [BlackEnergy](/software/S0089) <small style="color:#929393">(v1.3)</small>
* [Conficker](/software/S0608) <small style="color:#929393">(v1.0)</small>
* [Duqu](/software/S0038) <small style="color:#929393">(v1.2)</small>
* [EKANS](/software/S0605) <small style="color:#929393">(v2.0)</small>
* [Flame](/software/S0143) <small style="color:#929393">(v1.1)</small>
* [Industroyer](/software/S0604) <small style="color:#929393">(v1.0)</small>
* [KillDisk](/software/S0607) <small style="color:#929393">(v1.1)</small>
* [LockerGoga](/software/S0372) <small style="color:#929393">(v2.0)</small>
* [NotPetya](/software/S0368) <small style="color:#929393">(v2.0)</small>
* [REvil](/software/S0496) <small style="color:#929393">(v2.0)</small>
* [Ryuk](/software/S0446) <small style="color:#929393">(v1.3)</small>
* [Stuxnet](/software/S0603) <small style="color:#929393">(v1.1)</small>
* [WannaCry](/software/S0366) <small style="color:#929393">(v1.1)</small>

## Groups

### Enterprise

#### Metadata-only Changes

* [APT33](/groups/G0064) <small style="color:#929393">(v1.4)</small>
* [Andariel](/groups/G0138) <small style="color:#929393">(v1.0)</small>
* [Dragonfly](/groups/G0035) <small style="color:#929393">(v3.0)</small>
* [Ke3chang](/groups/G0004) <small style="color:#929393">(v2.0)</small>
* [Kimsuky](/groups/G0094) <small style="color:#929393">(v3.1)</small>
* [Lazarus Group](/groups/G0032) <small style="color:#929393">(v3.0)</small>
* [OilRig](/groups/G0049) <small style="color:#929393">(v3.0)</small>
* [Sandworm Team](/groups/G0034) <small style="color:#929393">(v2.2)</small>
* [TEMP.Veles](/groups/G0088) <small style="color:#929393">(v1.3)</small>

### Mobile

### ICS

#### New Groups

* [APT34](/groups/G0057) <small style="color:#929393">(v1.0)</small>
* [APT38](/groups/G0082) <small style="color:#eb6635">(v2.0)</small>
* [FIN6](/groups/G0037) <small style="color:#eb6635">(v3.2)</small>
* [FIN7](/groups/G0046) <small style="color:#eb6635">(v2.1)</small>
* [GOLD SOUTHFIELD](/groups/G0115) <small style="color:#eb6635">(v1.1)</small>
* [Wizard Spider](/groups/G0102) <small style="color:#eb6635">(v2.0)</small>

#### Metadata-only Changes

* [ALLANITE](/groups/G1000) <small style="color:#929393">(v1.0)</small>
* [APT33](/groups/G0064) <small style="color:#929393">(v1.4)</small>
* [Dragonfly](/groups/G0035) <small style="color:#929393">(v3.0)</small>
* [HEXANE](/groups/G1001) <small style="color:#929393">(v1.0)</small>
* [Lazarus Group](/groups/G0032) <small style="color:#929393">(v3.0)</small>
* [OilRig](/groups/G0049) <small style="color:#929393">(v3.0)</small>
* [Sandworm Team](/groups/G0034) <small style="color:#929393">(v2.2)</small>
* [TEMP.Veles](/groups/G0088) <small style="color:#929393">(v1.3)</small>

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

* [Application Log](/datasources/DS0015) <small style="color:#929393">(v1.0)</small>
* [Windows Registry](/datasources/DS0024) <small style="color:#929393">(v1.0)</small>

### Mobile

### ICS

#### Metadata-only Changes

* [Application Log](/datasources/DS0015) <small style="color:#929393">(v1.0)</small>
* [Operational Databases](/datasources/DS0040) <small style="color:#929393">(v1.0)</small>
* [Windows Registry](/datasources/DS0024) <small style="color:#929393">(v1.0)</small>

#### Deletions

* Assets <small style="color:#eb6635">(v1.0)</small>

## Data Components

### Enterprise

### Mobile

### ICS

#### Metadata-only Changes

* [Device Alarm](/datasources/DS0040/#Device%20Alarm) <small style="color:#929393">(v1.0)</small>
* [Process History/Live Data](/datasources/DS0040/#Process%20History/Live%20Data) <small style="color:#929393">(v1.0)</small>
* [Process/Event Alarm](/datasources/DS0040/#Process/Event%20Alarm) <small style="color:#929393">(v1.0)</small>

## Contributors to this release

* Center for Threat-Informed Defense (CTID)
* Dragos  Threat  Intelligence
* Dragos Threat Intelligence
* Drew Church, Splunk
* Edward Millington
* Hiroki Nagahama, NEC Corporation
* Joe Slowik -  Dragos
* Krishnan Subramanian, @krish203
* Manikantan Srinivasan, NEC Corporation India
* Oleksiy Gayda
* Thijn Bukkems, Amazon
* Vinay Pidathala
* Zur Ulianitzky, XM Cyber
