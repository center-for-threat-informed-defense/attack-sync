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

* Obfuscated Files or Information: [Indicator Removal from Tools](/techniques/T1027/005) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Supply Chain Compromise: [Compromise Hardware Supply Chain](/techniques/T1195/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Supply Chain Compromise: [Compromise Software Dependencies and Development Tools](/techniques/T1195/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Supply Chain Compromise: [Compromise Software Supply Chain](/techniques/T1195/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

#### Other Version Changes

* [Exploitation for Credential Access](/techniques/T1212) <small style="color:#eb6635">(v1.1&#8594;v1.4)</small>
* [Exploitation for Defense Evasion](/techniques/T1211) <small style="color:#eb6635">(v1.1&#8594;v1.3)</small>
* [Hardware Additions](/techniques/T1200) <small style="color:#eb6635">(v1.3&#8594;v1.6)</small>
* [Supply Chain Compromise](/techniques/T1195) <small style="color:#eb6635">(v1.3&#8594;v1.5)</small>

#### Metadata-only Changes

* [Access Token Manipulation](/techniques/T1134) <small style="color:#929393">(v2.0)</small>
    * [Parent PID Spoofing](/techniques/T1134/004) <small style="color:#929393">(v1.0)</small>
* Account Manipulation: [Additional Cloud Credentials](/techniques/T1098/001) <small style="color:#929393">(v2.3)</small>
* Account Manipulation: [Additional Cloud Roles](/techniques/T1098/003) <small style="color:#929393">(v2.0)</small>
* Account Manipulation: [Device Registration](/techniques/T1098/005) <small style="color:#929393">(v1.0)</small>
* Boot or Logon Autostart Execution: [Registry Run Keys / Startup Folder](/techniques/T1547/001) <small style="color:#929393">(v1.1)</small>
* Create or Modify System Process: [Windows Service](/techniques/T1543/003) <small style="color:#929393">(v1.2)</small>
* Credentials from Password Stores: [Windows Credential Manager](/techniques/T1555/004) <small style="color:#929393">(v1.0)</small>
* [Data from Local System](/techniques/T1005) <small style="color:#929393">(v1.4)</small>
* [Deobfuscate/Decode Files or Information](/techniques/T1140) <small style="color:#929393">(v1.1)</small>
* [Execution Guardrails](/techniques/T1480) <small style="color:#929393">(v1.1)</small>
    * [Environmental Keying](/techniques/T1480/001) <small style="color:#929393">(v1.0)</small>
* Hide Artifacts: [Resource Forking](/techniques/T1564/009) <small style="color:#929393">(v1.0)</small>
* [Hijack Execution Flow](/techniques/T1574) <small style="color:#929393">(v1.2)</small>
    * [DLL Side-Loading](/techniques/T1574/002) <small style="color:#929393">(v2.0)</small>
    * [Dylib Hijacking](/techniques/T1574/004) <small style="color:#929393">(v2.0)</small>
    * [Path Interception by PATH Environment Variable](/techniques/T1574/007) <small style="color:#929393">(v1.0)</small>
    * [Services Registry Permissions Weakness](/techniques/T1574/011) <small style="color:#929393">(v1.1)</small>
* Impair Defenses: [Downgrade Attack](/techniques/T1562/010) <small style="color:#929393">(v1.1)</small>
* [Indirect Command Execution](/techniques/T1202) <small style="color:#929393">(v1.1)</small>
* [Ingress Tool Transfer](/techniques/T1105) <small style="color:#929393">(v2.1)</small>
* [Masquerading](/techniques/T1036) <small style="color:#929393">(v1.4)</small>
    * [Match Legitimate Name or Location](/techniques/T1036/005) <small style="color:#929393">(v1.1)</small>
* [Network Boundary Bridging](/techniques/T1599) <small style="color:#929393">(v1.1)</small>
* [Network Sniffing](/techniques/T1040) <small style="color:#929393">(v1.3)</small>
* OS Credential Dumping: [LSASS Memory](/techniques/T1003/001) <small style="color:#929393">(v1.1)</small>
* [Obfuscated Files or Information](/techniques/T1027) <small style="color:#929393">(v1.2)</small>
    * [HTML Smuggling](/techniques/T1027/006) <small style="color:#929393">(v1.0)</small>
* [Rootkit](/techniques/T1014) <small style="color:#929393">(v1.1)</small>
* [Subvert Trust Controls](/techniques/T1553) <small style="color:#929393">(v1.1)</small>
    * [Code Signing Policy Modification](/techniques/T1553/006) <small style="color:#929393">(v1.0)</small>
    * [Gatekeeper Bypass](/techniques/T1553/001) <small style="color:#929393">(v1.1)</small>
    * [Mark-of-the-Web Bypass](/techniques/T1553/005) <small style="color:#929393">(v1.1)</small>
    * [SIP and Trust Provider Hijacking](/techniques/T1553/003) <small style="color:#929393">(v1.0)</small>
* System Binary Proxy Execution: [MMC](/techniques/T1218/014) <small style="color:#929393">(v2.0)</small>
* System Binary Proxy Execution: [Verclsid](/techniques/T1218/012) <small style="color:#929393">(v2.0)</small>
* [System Network Configuration Discovery](/techniques/T1016) <small style="color:#929393">(v1.4)</small>
* [Trusted Developer Utilities Proxy Execution](/techniques/T1127) <small style="color:#929393">(v1.2)</small>
* Use Alternate Authentication Material: [Application Access Token](/techniques/T1550/001) <small style="color:#929393">(v1.3)</small>
* User Execution: [Malicious File](/techniques/T1204/002) <small style="color:#929393">(v1.2)</small>
* [Valid Accounts](/techniques/T1078) <small style="color:#929393">(v2.4)</small>
* [XSL Script Processing](/techniques/T1220) <small style="color:#929393">(v1.2)</small>

### Mobile

### ICS

#### Metadata-only Changes

* [Activate Firmware Update Mode](/techniques/T0800) <small style="color:#929393">(v1.0)</small>
* [Alarm Suppression](/techniques/T0878) <small style="color:#929393">(v1.0)</small>
* [Automated Collection](/techniques/T0802) <small style="color:#929393">(v1.0)</small>
* [Block Command Message](/techniques/T0803) <small style="color:#929393">(v1.0)</small>
* [Block Reporting Message](/techniques/T0804) <small style="color:#929393">(v1.0)</small>
* [Block Serial COM](/techniques/T0805) <small style="color:#929393">(v1.0)</small>
* [Brute Force I/O](/techniques/T0806) <small style="color:#929393">(v1.0)</small>
* [Change Operating Mode](/techniques/T0858) <small style="color:#929393">(v1.0)</small>
* [Command-Line Interface](/techniques/T0807) <small style="color:#929393">(v1.0)</small>
* [Commonly Used Port](/techniques/T0885) <small style="color:#929393">(v1.0)</small>
* [Connection Proxy](/techniques/T0884) <small style="color:#929393">(v1.0)</small>
* [Damage to Property](/techniques/T0879) <small style="color:#929393">(v1.0)</small>
* [Data Destruction](/techniques/T0809) <small style="color:#929393">(v1.0)</small>
* [Data from Information Repositories](/techniques/T0811) <small style="color:#929393">(v1.0)</small>
* [Default Credentials](/techniques/T0812) <small style="color:#929393">(v1.0)</small>
* [Denial of Control](/techniques/T0813) <small style="color:#929393">(v1.0)</small>
* [Denial of Service](/techniques/T0814) <small style="color:#929393">(v1.0)</small>
* [Denial of View](/techniques/T0815) <small style="color:#929393">(v1.0)</small>
* [Detect Operating Mode](/techniques/T0868) <small style="color:#929393">(v1.0)</small>
* [Device Restart/Shutdown](/techniques/T0816) <small style="color:#929393">(v1.0)</small>
* [Drive-by Compromise](/techniques/T0817) <small style="color:#929393">(v1.0)</small>
* [Execution through API](/techniques/T0871) <small style="color:#929393">(v1.0)</small>
* [Exploit Public-Facing Application](/techniques/T0819) <small style="color:#929393">(v1.0)</small>
* [Exploitation for Evasion](/techniques/T0820) <small style="color:#929393">(v1.0)</small>
* [Exploitation for Privilege Escalation](/techniques/T0890) <small style="color:#929393">(v1.0)</small>
* [Exploitation of Remote Services](/techniques/T0866) <small style="color:#929393">(v1.0)</small>
* [External Remote Services](/techniques/T0822) <small style="color:#929393">(v1.0)</small>
* [Graphical User Interface](/techniques/T0823) <small style="color:#929393">(v1.0)</small>
* [Hooking](/techniques/T0874) <small style="color:#929393">(v1.0)</small>
* [I/O Image](/techniques/T0877) <small style="color:#929393">(v1.0)</small>
* [Indicator Removal on Host](/techniques/T0872) <small style="color:#929393">(v1.0)</small>
* [Internet Accessible Device](/techniques/T0883) <small style="color:#929393">(v1.0)</small>
* [Lateral Tool Transfer](/techniques/T0867) <small style="color:#929393">(v1.0)</small>
* [Loss of Availability](/techniques/T0826) <small style="color:#929393">(v1.0)</small>
* [Loss of Control](/techniques/T0827) <small style="color:#929393">(v1.0)</small>
* [Loss of Productivity and Revenue](/techniques/T0828) <small style="color:#929393">(v1.0)</small>
* [Loss of Protection](/techniques/T0837) <small style="color:#929393">(v1.0)</small>
* [Loss of Safety](/techniques/T0880) <small style="color:#929393">(v1.0)</small>
* [Loss of View](/techniques/T0829) <small style="color:#929393">(v1.0)</small>
* [Man in the Middle](/techniques/T0830) <small style="color:#929393">(v1.0)</small>
* [Manipulate I/O Image](/techniques/T0835) <small style="color:#929393">(v1.0)</small>
* [Manipulation of Control](/techniques/T0831) <small style="color:#929393">(v1.0)</small>
* [Manipulation of View](/techniques/T0832) <small style="color:#929393">(v1.0)</small>
* [Masquerading](/techniques/T0849) <small style="color:#929393">(v1.0)</small>
* [Modify Alarm Settings](/techniques/T0838) <small style="color:#929393">(v1.0)</small>
* [Modify Controller Tasking](/techniques/T0821) <small style="color:#929393">(v1.0)</small>
* [Modify Parameter](/techniques/T0836) <small style="color:#929393">(v1.0)</small>
* [Modify Program](/techniques/T0889) <small style="color:#929393">(v1.0)</small>
* [Module Firmware](/techniques/T0839) <small style="color:#929393">(v1.0)</small>
* [Monitor Process State](/techniques/T0801) <small style="color:#929393">(v1.0)</small>
* [Native API](/techniques/T0834) <small style="color:#929393">(v1.0)</small>
* [Network Connection Enumeration](/techniques/T0840) <small style="color:#929393">(v1.0)</small>
* [Network Sniffing](/techniques/T0842) <small style="color:#929393">(v1.0)</small>
* [Point & Tag Identification](/techniques/T0861) <small style="color:#929393">(v1.0)</small>
* [Program Download](/techniques/T0843) <small style="color:#929393">(v1.0)</small>
* [Program Upload](/techniques/T0845) <small style="color:#929393">(v1.0)</small>
* [Project File Infection](/techniques/T0873) <small style="color:#929393">(v1.0)</small>
* [Remote Services](/techniques/T0886) <small style="color:#929393">(v1.0)</small>
* [Remote System Discovery](/techniques/T0846) <small style="color:#929393">(v1.0)</small>
* [Remote System Information Discovery](/techniques/T0888) <small style="color:#929393">(v1.0)</small>
* [Replication Through Removable Media](/techniques/T0847) <small style="color:#929393">(v1.0)</small>
* [Rogue Master](/techniques/T0848) <small style="color:#929393">(v1.0)</small>
* [Rootkit](/techniques/T0851) <small style="color:#929393">(v1.0)</small>
* [Screen Capture](/techniques/T0852) <small style="color:#929393">(v1.0)</small>
* [Scripting](/techniques/T0853) <small style="color:#929393">(v1.0)</small>
* [Service Stop](/techniques/T0881) <small style="color:#929393">(v1.0)</small>
* [Spearphishing Attachment](/techniques/T0865) <small style="color:#929393">(v1.0)</small>
* [Spoof Reporting Message](/techniques/T0856) <small style="color:#929393">(v1.0)</small>
* [Standard Application Layer Protocol](/techniques/T0869) <small style="color:#929393">(v1.0)</small>
* [Supply Chain Compromise](/techniques/T0862) <small style="color:#929393">(v1.0)</small>
* [System Firmware](/techniques/T0857) <small style="color:#929393">(v1.0)</small>
* [Theft of Operational Information](/techniques/T0882) <small style="color:#929393">(v1.0)</small>
* [Transient Cyber Asset](/techniques/T0864) <small style="color:#929393">(v1.0)</small>
* [Unauthorized Command Message](/techniques/T0855) <small style="color:#929393">(v1.0)</small>
* [User Execution](/techniques/T0863) <small style="color:#929393">(v1.0)</small>
* [Valid Accounts](/techniques/T0859) <small style="color:#929393">(v1.0)</small>
* [Wireless Compromise](/techniques/T0860) <small style="color:#929393">(v1.0)</small>
* [Wireless Sniffing](/techniques/T0887) <small style="color:#929393">(v1.0)</small>

## Software

### Enterprise

#### Metadata-only Changes

* [AdFind](/software/S0552) <small style="color:#929393">(v1.0)</small>
* [Backdoor.Oldrea](/software/S0093) <small style="color:#929393">(v2.0)</small>
* [Bad Rabbit](/software/S0606) <small style="color:#929393">(v1.0)</small>
* [BlackEnergy](/software/S0089) <small style="color:#929393">(v1.3)</small>
* [Chrommme](/software/S0667) <small style="color:#929393">(v1.0)</small>
* [Conficker](/software/S0608) <small style="color:#929393">(v1.0)</small>
* [Duqu](/software/S0038) <small style="color:#929393">(v1.2)</small>
* [EKANS](/software/S0605) <small style="color:#929393">(v2.0)</small>
* [Flame](/software/S0143) <small style="color:#929393">(v1.1)</small>
* [Gelsemium](/software/S0666) <small style="color:#929393">(v1.0)</small>
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

* [ACAD/Medre.A](/software/S0018) <small style="color:#929393">(v1.0)</small>
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
* [PLC-Blaster](/software/S0009) <small style="color:#929393">(v1.0)</small>
* [REvil](/software/S0496) <small style="color:#929393">(v2.0)</small>
* [Ryuk](/software/S0446) <small style="color:#929393">(v1.3)</small>
* [Stuxnet](/software/S0603) <small style="color:#929393">(v1.1)</small>
* [Triton](/software/S0013) <small style="color:#929393">(v1.0)</small>
* [VPNFilter](/software/S0002) <small style="color:#929393">(v1.0)</small>
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

#### Deprecations

* [Gelsemium](/groups/G0141) <small style="color:#929393">(v1.0)</small>

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

#### Metadata-only Changes

* [Access Management](/mitigations/M0801) <small style="color:#929393">(v1.0)</small>
* [Account Use Policies](/mitigations/M0936) <small style="color:#929393">(v1.0)</small>
* [Active Directory Configuration](/mitigations/M0915) <small style="color:#929393">(v1.0)</small>
* [Antivirus/Antimalware](/mitigations/M0949) <small style="color:#929393">(v1.0)</small>
* [Application Developer Guidance](/mitigations/M0913) <small style="color:#929393">(v1.0)</small>
* [Application Isolation and Sandboxing](/mitigations/M0948) <small style="color:#929393">(v1.0)</small>
* [Audit](/mitigations/M0947) <small style="color:#929393">(v1.0)</small>
* [Authorization Enforcement](/mitigations/M0800) <small style="color:#929393">(v1.0)</small>
* [Boot Integrity](/mitigations/M0946) <small style="color:#929393">(v1.0)</small>
* [Code Signing](/mitigations/M0945) <small style="color:#929393">(v1.0)</small>
* [Communication Authenticity](/mitigations/M0802) <small style="color:#929393">(v1.0)</small>
* [Data Backup](/mitigations/M0953) <small style="color:#929393">(v1.0)</small>
* [Data Loss Prevention](/mitigations/M0803) <small style="color:#929393">(v1.0)</small>
* [Disable or Remove Feature or Program](/mitigations/M0942) <small style="color:#929393">(v1.0)</small>
* [Encrypt Network Traffic](/mitigations/M0808) <small style="color:#929393">(v1.0)</small>
* [Encrypt Sensitive Information](/mitigations/M0941) <small style="color:#929393">(v1.0)</small>
* [Execution Prevention](/mitigations/M0938) <small style="color:#929393">(v1.0)</small>
* [Exploit Protection](/mitigations/M0950) <small style="color:#929393">(v1.0)</small>
* [Filter Network Traffic](/mitigations/M0937) <small style="color:#929393">(v1.0)</small>
* [Human User Authentication](/mitigations/M0804) <small style="color:#929393">(v1.0)</small>
* [Limit Access to Resource Over Network](/mitigations/M0935) <small style="color:#929393">(v1.0)</small>
* [Limit Hardware Installation](/mitigations/M0934) <small style="color:#929393">(v1.0)</small>
* [Mechanical Protection Layers](/mitigations/M0805) <small style="color:#929393">(v1.0)</small>
* [Minimize Wireless Signal Propagation](/mitigations/M0806) <small style="color:#929393">(v1.0)</small>
* [Mitigation Limited or Not Effective](/mitigations/M0816) <small style="color:#929393">(v1.0)</small>
* [Multi-factor Authentication](/mitigations/M0932) <small style="color:#929393">(v1.0)</small>
* [Network Allowlists](/mitigations/M0807) <small style="color:#929393">(v1.0)</small>
* [Network Intrusion Prevention](/mitigations/M0931) <small style="color:#929393">(v1.0)</small>
* [Network Segmentation](/mitigations/M0930) <small style="color:#929393">(v1.0)</small>
* [Operating System Configuration](/mitigations/M0928) <small style="color:#929393">(v1.0)</small>
* [Operational Information Confidentiality](/mitigations/M0809) <small style="color:#929393">(v1.0)</small>
* [Out-of-Band Communications Channel](/mitigations/M0810) <small style="color:#929393">(v1.0)</small>
* [Password Policies](/mitigations/M0927) <small style="color:#929393">(v1.0)</small>
* [Privileged Account Management](/mitigations/M0926) <small style="color:#929393">(v1.0)</small>
* [Redundancy of Service](/mitigations/M0811) <small style="color:#929393">(v1.0)</small>
* [Restrict File and Directory Permissions](/mitigations/M0922) <small style="color:#929393">(v1.0)</small>
* [Restrict Library Loading](/mitigations/M0944) <small style="color:#929393">(v1.0)</small>
* [Restrict Registry Permissions](/mitigations/M0924) <small style="color:#929393">(v1.0)</small>
* [Restrict Web-Based Content](/mitigations/M0921) <small style="color:#929393">(v1.0)</small>
* [SSL/TLS Inspection](/mitigations/M0920) <small style="color:#929393">(v1.0)</small>
* [Safety Instrumented Systems](/mitigations/M0812) <small style="color:#929393">(v1.0)</small>
* [Software Configuration](/mitigations/M0954) <small style="color:#929393">(v1.0)</small>
* [Software Process and Device Authentication](/mitigations/M0813) <small style="color:#929393">(v1.0)</small>
* [Static Network Configuration](/mitigations/M0814) <small style="color:#929393">(v1.0)</small>
* [Supply Chain Management](/mitigations/M0817) <small style="color:#929393">(v1.0)</small>
* [Threat Intelligence Program](/mitigations/M0919) <small style="color:#929393">(v1.0)</small>
* [Update Software](/mitigations/M0951) <small style="color:#929393">(v1.0)</small>
* [User Account Management](/mitigations/M0918) <small style="color:#929393">(v1.0)</small>
* [User Training](/mitigations/M0917) <small style="color:#929393">(v1.0)</small>
* [Vulnerability Scanning](/mitigations/M0916) <small style="color:#929393">(v1.0)</small>
* [Watchdog Timers](/mitigations/M0815) <small style="color:#929393">(v1.0)</small>

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

#### Metadata-only Changes

* [Active DNS](/datasources/DS0038/#Active%20DNS) <small style="color:#929393">(v1.0)</small>

### Mobile

### ICS

#### Metadata-only Changes

* [Device Alarm](/datasources/DS0040/#Device%20Alarm) <small style="color:#929393">(v1.0)</small>
* [Process History/Live Data](/datasources/DS0040/#Process%20History/Live%20Data) <small style="color:#929393">(v1.0)</small>
* [Process/Event Alarm](/datasources/DS0040/#Process/Event%20Alarm) <small style="color:#929393">(v1.0)</small>

## Contributors to this release

* Center for Threat-Informed Defense (CTID)
* Dongwook Kim, KISA
* Dragos  Threat  Intelligence
* Dragos Threat Intelligence
* Drew Church, Splunk
* Edward Millington
* Hiroki Nagahama, NEC Corporation
* Joe Slowik -  Dragos
* Krishnan Subramanian, @krish203
* Manikantan Srinivasan, NEC Corporation India
* Mike Moran
* Oleksiy Gayda
* Thijn Bukkems, Amazon
* Vinay Pidathala
* Zur Ulianitzky, XM Cyber
