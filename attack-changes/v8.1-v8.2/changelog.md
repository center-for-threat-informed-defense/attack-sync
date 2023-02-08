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

#### New Techniques

* Domain Policy Modification: [Domain Trust Modification](/techniques/T1484/002) <small style="color:#929393">(v1.0)</small>
* Domain Policy Modification: [Group Policy Modification](/techniques/T1484/001) <small style="color:#929393">(v1.0)</small>
* [Forge Web Credentials](/techniques/T1606) <small style="color:#929393">(v1.0)</small>
    * [SAML Tokens](/techniques/T1606/002) <small style="color:#929393">(v1.0)</small>
    * [Web Cookies](/techniques/T1606/001) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* [Domain Policy Modification](/techniques/T1484) <small style="color:#929393">(v1.1&#8594;v2.0)</small>

#### Minor Version Changes

* Account Manipulation: [Additional Cloud Credentials](/techniques/T1098/001) <small style="color:#929393">(v2.0&#8594;v2.1)</small>

### Mobile

### ICS

## Software

### Enterprise

#### New Software

* [AdFind](/software/S0552) <small style="color:#929393">(v1.0)</small>
* [BloodHound](/software/S0521) <small style="color:#929393">(v1.0)</small>
* [Raindrop](/software/S0565) <small style="color:#929393">(v1.0)</small>
* [Sunburst](/software/S0559) <small style="color:#929393">(v1.0)</small>
* [Sunspot](/software/S0562) <small style="color:#929393">(v1.0)</small>
* [Teardrop](/software/S0560) <small style="color:#929393">(v1.0)</small>

### Mobile

### ICS

## Groups

### Enterprise

#### New Groups

* [UNC2452](/groups/G0118) <small style="color:#929393">(v1.0)</small>

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

### Mobile

### ICS

## Contributors to this release

* Blake Strom, Microsoft 365 Defender
* Itamar Mizrahi, Cymptom
* Katie Nickels, Red Canary
* Matt Brenton, Zurich Insurance Group
* Oleg Kolesnikov, Securonix
* Tristan Bennett, Seamless Intelligence
