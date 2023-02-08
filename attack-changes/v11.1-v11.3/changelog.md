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

#### New Techniques

* [Abuse Elevation Control Mechanism](/techniques/T1626) <small style="color:#929393">(v1.0)</small>
    * [Device Administrator Permissions](/techniques/T1626/001) <small style="color:#929393">(v1.0)</small>
* [Account Access Removal](/techniques/T1640) <small style="color:#929393">(v1.0)</small>
* [Adversary-in-the-Middle](/techniques/T1638) <small style="color:#eb6635">(v2.0)</small>
* Application Layer Protocol: [Web Protocols](/techniques/T1437/001) <small style="color:#929393">(v1.0)</small>
* [Command and Scripting Interpreter](/techniques/T1623) <small style="color:#929393">(v1.0)</small>
    * [Unix Shell](/techniques/T1623/001) <small style="color:#929393">(v1.0)</small>
* [Compromise Client Software Binary](/techniques/T1645) <small style="color:#929393">(v1.0)</small>
* [Credentials from Password Store](/techniques/T1634) <small style="color:#929393">(v1.0)</small>
    * [Keychain](/techniques/T1634/001) <small style="color:#929393">(v1.0)</small>
* [Data Manipulation](/techniques/T1641) <small style="color:#929393">(v1.0)</small>
    * [Transmitted Data Manipulation](/techniques/T1641/001) <small style="color:#929393">(v1.0)</small>
* [Dynamic Resolution](/techniques/T1637) <small style="color:#929393">(v1.0)</small>
    * [Domain Generation Algorithms](/techniques/T1637/001) <small style="color:#929393">(v1.0)</small>
* Encrypted Channel: [Asymmetric Cryptography](/techniques/T1521/002) <small style="color:#929393">(v1.0)</small>
* Encrypted Channel: [Symmetric Cryptography](/techniques/T1521/001) <small style="color:#929393">(v1.0)</small>
* [Endpoint Denial of Service](/techniques/T1642) <small style="color:#929393">(v1.0)</small>
* [Event Triggered Execution](/techniques/T1624) <small style="color:#929393">(v1.0)</small>
    * [Broadcast Receivers](/techniques/T1624/001) <small style="color:#929393">(v1.0)</small>
* [Execution Guardrails](/techniques/T1627) <small style="color:#929393">(v1.0)</small>
    * [Geofencing](/techniques/T1627/001) <small style="color:#929393">(v1.0)</small>
* [Exfiltration Over Alternative Protocol](/techniques/T1639) <small style="color:#929393">(v1.0)</small>
    * [Exfiltration Over Unencrypted Non-C2 Protocol](/techniques/T1639/001) <small style="color:#929393">(v1.0)</small>
* [Exfiltration Over C2 Channel](/techniques/T1646) <small style="color:#929393">(v1.0)</small>
* [Generate Traffic from Victim](/techniques/T1643) <small style="color:#929393">(v1.0)</small>
* [Hide Artifacts](/techniques/T1628) <small style="color:#929393">(v1.0)</small>
    * [Suppress Application Icon](/techniques/T1628/001) <small style="color:#929393">(v1.0)</small>
    * [User Evasion](/techniques/T1628/002) <small style="color:#929393">(v1.0)</small>
* [Hijack Execution Flow](/techniques/T1625) <small style="color:#929393">(v1.0)</small>
    * [System Runtime API Hijacking](/techniques/T1625/001) <small style="color:#929393">(v1.0)</small>
* [Impair Defenses](/techniques/T1629) <small style="color:#929393">(v1.0)</small>
    * [Device Lockout](/techniques/T1629/002) <small style="color:#929393">(v1.0)</small>
    * [Disable or Modify Tools](/techniques/T1629/003) <small style="color:#929393">(v1.0)</small>
    * [Prevent Application Removal](/techniques/T1629/001) <small style="color:#929393">(v1.0)</small>
* [Indicator Removal on Host](/techniques/T1630) <small style="color:#929393">(v1.0)</small>
    * [Disguise Root/Jailbreak Indicators](/techniques/T1630/003) <small style="color:#929393">(v1.0)</small>
    * [File Deletion](/techniques/T1630/002) <small style="color:#929393">(v1.0)</small>
    * [Uninstall Malicious Application](/techniques/T1630/001) <small style="color:#929393">(v1.0)</small>
* Input Capture: [GUI Input Capture](/techniques/T1417/002) <small style="color:#929393">(v1.0)</small>
* Input Capture: [Keylogging](/techniques/T1417/001) <small style="color:#929393">(v1.0)</small>
* Location Tracking: [Impersonate SS7 Nodes](/techniques/T1430/002) <small style="color:#929393">(v1.0)</small>
* Location Tracking: [Remote Device Management Services](/techniques/T1430/001) <small style="color:#929393">(v1.0)</small>
* Obfuscated Files or Information: [Software Packing](/techniques/T1406/002) <small style="color:#929393">(v1.0)</small>
* Obfuscated Files or Information: [Steganography](/techniques/T1406/001) <small style="color:#929393">(v1.0)</small>
* [Out of Band Data](/techniques/T1644) <small style="color:#eb6635">(v2.0)</small>
* [Process Injection](/techniques/T1631) <small style="color:#929393">(v1.0)</small>
    * [Ptrace System Calls](/techniques/T1631/001) <small style="color:#929393">(v1.0)</small>
* [Protected User Data](/techniques/T1636) <small style="color:#929393">(v1.0)</small>
    * [Calendar Entries](/techniques/T1636/001) <small style="color:#929393">(v1.0)</small>
    * [Call Log](/techniques/T1636/002) <small style="color:#929393">(v1.0)</small>
    * [Contact List](/techniques/T1636/003) <small style="color:#929393">(v1.0)</small>
    * [SMS Messages](/techniques/T1636/004) <small style="color:#929393">(v1.0)</small>
* Software Discovery: [Security Software Discovery](/techniques/T1418/001) <small style="color:#929393">(v1.0)</small>
* [Steal Application Access Token](/techniques/T1635) <small style="color:#929393">(v1.0)</small>
    * [URI Hijacking](/techniques/T1635/001) <small style="color:#929393">(v1.0)</small>
* [Subvert Trust Controls](/techniques/T1632) <small style="color:#929393">(v1.0)</small>
    * [Code Signing Policy Modification](/techniques/T1632/001) <small style="color:#929393">(v1.0)</small>
* Supply Chain Compromise: [Compromise Hardware Supply Chain](/techniques/T1474/002) <small style="color:#929393">(v1.0)</small>
* Supply Chain Compromise: [Compromise Software Dependencies and Development Tools](/techniques/T1474/001) <small style="color:#929393">(v1.0)</small>
* Supply Chain Compromise: [Compromise Software Supply Chain](/techniques/T1474/003) <small style="color:#929393">(v1.0)</small>
* [Virtualization/Sandbox Evasion](/techniques/T1633) <small style="color:#929393">(v1.0)</small>
    * [System Checks](/techniques/T1633/001) <small style="color:#929393">(v1.0)</small>
* Web Service: [Bidirectional Communication](/techniques/T1481/002) <small style="color:#929393">(v1.0)</small>
* Web Service: [Dead Drop Resolver](/techniques/T1481/001) <small style="color:#929393">(v1.0)</small>
* Web Service: [One-Way Communication](/techniques/T1481/003) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* [Archive Collected Data](/techniques/T1532) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Audio Capture](/techniques/T1429) <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* [Boot or Logon Initialization Scripts](/techniques/T1398) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Clipboard Data](/techniques/T1414) <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* [Drive-By Compromise](/techniques/T1456) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Encrypted Channel](/techniques/T1521) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Exploitation for Privilege Escalation](/techniques/T1404) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Foreground Persistence](/techniques/T1541) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Ingress Tool Transfer](/techniques/T1544) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Native API](/techniques/T1575) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Non-Standard Port](/techniques/T1509) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Obfuscated Files or Information](/techniques/T1406) <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* [Process Discovery](/techniques/T1424) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Replication Through Removable Media](/techniques/T1458) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Software Discovery](/techniques/T1418) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Stored Application Data](/techniques/T1409) <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* [Supply Chain Compromise](/techniques/T1474) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Video Capture](/techniques/T1512) <small style="color:#929393">(v1.0&#8594;v2.0)</small>

#### Minor Version Changes

* [Access Notifications](/techniques/T1517) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Application Layer Protocol](/techniques/T1437) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Data Encrypted for Impact](/techniques/T1471) <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* [Data from Local System](/techniques/T1533) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Download New Code at Runtime](/techniques/T1407) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Exploitation of Remote Services](/techniques/T1428) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [File and Directory Discovery](/techniques/T1420) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Input Capture](/techniques/T1417) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [Location Tracking](/techniques/T1430) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Lockscreen Bypass](/techniques/T1461) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Network Denial of Service](/techniques/T1464) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Network Service Scanning](/techniques/T1423) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Screen Capture](/techniques/T1513) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [System Information Discovery](/techniques/T1426) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [System Network Configuration Discovery](/techniques/T1422) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [System Network Connections Discovery](/techniques/T1421) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Web Service](/techniques/T1481) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

#### Revocations

* Access Calendar Entries (revoked by Protected User Data: [Calendar Entries](/techniques/T1636/001)) <small style="color:#929393">(v1.0)</small>
* Access Call Log (revoked by Protected User Data: [Call Log](/techniques/T1636/002)) <small style="color:#929393">(v1.1)</small>
* Access Contact List (revoked by Protected User Data: [Contact List](/techniques/T1636/003)) <small style="color:#929393">(v1.0)</small>
* Broadcast Receivers (revoked by Event Triggered Execution: [Broadcast Receivers](/techniques/T1624/001)) <small style="color:#929393">(v2.0)</small>
* Capture SMS Messages (revoked by Protected User Data: [SMS Messages](/techniques/T1636/004)) <small style="color:#929393">(v1.1)</small>
* Carrier Billing Fraud (revoked by [Generate Traffic from Victim](/techniques/T1643)) <small style="color:#929393">(v2.0)</small>
* Clipboard Modification (revoked by Data Manipulation: [Transmitted Data Manipulation](/techniques/T1641/001)) <small style="color:#929393">(v1.0)</small>
* Code Injection (revoked by Process Injection: [Ptrace System Calls](/techniques/T1631/001)) <small style="color:#929393">(v1.0)</small>
* Command-Line Interface (revoked by Command and Scripting Interpreter: [Unix Shell](/techniques/T1623/001)) <small style="color:#929393">(v1.0)</small>
* Delete Device Data (revoked by Indicator Removal on Host: [File Deletion](/techniques/T1630/002)) <small style="color:#929393">(v2.1)</small>
* Device Administrator Permissions (revoked by Abuse Elevation Control Mechanism: [Device Administrator Permissions](/techniques/T1626/001)) <small style="color:#929393">(v2.0)</small>
* Device Lockout (revoked by Impair Defenses: [Device Lockout](/techniques/T1629/002)) <small style="color:#929393">(v2.0)</small>
* Disguise Root/Jailbreak Indicators (revoked by Indicator Removal on Host: [Disguise Root/Jailbreak Indicators](/techniques/T1630/003)) <small style="color:#929393">(v1.1)</small>
* Domain Generation Algorithms (revoked by Dynamic Resolution: [Domain Generation Algorithms](/techniques/T1637/001)) <small style="color:#929393">(v1.0)</small>
* Downgrade to Insecure Protocols (revoked by [Adversary-in-the-Middle](/techniques/T1638)) <small style="color:#929393">(v1.1)</small>
* Eavesdrop on Insecure Network Communication (revoked by [Adversary-in-the-Middle](/techniques/T1638)) <small style="color:#929393">(v1.1)</small>
* Evade Analysis Environment (revoked by Virtualization/Sandbox Evasion: [System Checks](/techniques/T1633/001)) <small style="color:#929393">(v1.0)</small>
* Exfiltration Over Other Network Medium (revoked by [Out of Band Data](/techniques/T1644)) <small style="color:#929393">(v2.0)</small>
* Exploit SS7 to Track Device Location (revoked by Location Tracking: [Impersonate SS7 Nodes](/techniques/T1430/002)) <small style="color:#929393">(v1.1)</small>
* Generate Fraudulent Advertising Revenue (revoked by [Generate Traffic from Victim](/techniques/T1643)) <small style="color:#929393">(v1.0)</small>
* Geofencing (revoked by Execution Guardrails: [Geofencing](/techniques/T1627/001)) <small style="color:#929393">(v1.0)</small>
* Input Prompt (revoked by Input Capture: [GUI Input Capture](/techniques/T1417/002)) <small style="color:#929393">(v2.1)</small>
* Install Insecure or Malicious Configuration (revoked by Subvert Trust Controls: [Code Signing Policy Modification](/techniques/T1632/001)) <small style="color:#929393">(v1.0)</small>
* Keychain (revoked by Credentials from Password Store: [Keychain](/techniques/T1634/001)) <small style="color:#929393">(v1.0)</small>
* Manipulate App Store Rankings or Ratings (revoked by [Generate Traffic from Victim](/techniques/T1643)) <small style="color:#929393">(v1.0)</small>
* Manipulate Device Communication (revoked by [Adversary-in-the-Middle](/techniques/T1638)) <small style="color:#929393">(v1.1)</small>
* Modify System Partition (revoked by Hijack Execution Flow: [System Runtime API Hijacking](/techniques/T1625/001)) <small style="color:#929393">(v1.2)</small>
* Network Information Discovery (revoked by [System Network Connections Discovery](/techniques/T1421)) <small style="color:#929393">(v1.0)</small>
* Network Traffic Capture or Redirection (revoked by [Adversary-in-the-Middle](/techniques/T1638)) <small style="color:#929393">(v1.0)</small>
* Remotely Track Device Without Authorization (revoked by Location Tracking: [Remote Device Management Services](/techniques/T1430/001)) <small style="color:#929393">(v1.1)</small>
* Rogue Cellular Base Station (revoked by [Adversary-in-the-Middle](/techniques/T1638)) <small style="color:#929393">(v1.1)</small>
* Rogue Wi-Fi Access Points (revoked by [Adversary-in-the-Middle](/techniques/T1638)) <small style="color:#929393">(v1.1)</small>
* Suppress Application Icon (revoked by Hide Artifacts: [Suppress Application Icon](/techniques/T1628/001)) <small style="color:#929393">(v1.1)</small>
* URI Hijacking (revoked by Steal Application Access Token: [URI Hijacking](/techniques/T1635/001)) <small style="color:#929393">(v2.0)</small>
* Uninstall Malicious Application (revoked by Indicator Removal on Host: [Uninstall Malicious Application](/techniques/T1630/001)) <small style="color:#929393">(v1.0)</small>
* User Evasion (revoked by Hide Artifacts: [User Evasion](/techniques/T1628/002)) <small style="color:#929393">(v1.0)</small>

#### Deprecations

* [Access Sensitive Data in Device Logs](/techniques/T1413) <small style="color:#929393">(v1.0)</small>
* [Attack PC via USB Connection](/techniques/T1427) <small style="color:#929393">(v1.1)</small>
* [Commonly Used Port](/techniques/T1436) <small style="color:#929393">(v1.0)</small>
* [Deliver Malicious App via Authorized App Store](/techniques/T1475) <small style="color:#929393">(v1.1)</small>
* [Deliver Malicious App via Other Means](/techniques/T1476) <small style="color:#929393">(v1.2)</small>
* [Exploit SS7 to Redirect Phone Calls/SMS](/techniques/T1449) <small style="color:#929393">(v1.2)</small>
* [Exploit TEE Vulnerability](/techniques/T1405) <small style="color:#929393">(v1.0)</small>
* [Exploit via Radio Interfaces](/techniques/T1477) <small style="color:#929393">(v1.1)</small>
* [Masquerade as Legitimate Application](/techniques/T1444) <small style="color:#929393">(v2.1)</small>
* [Modify Cached Executable Code](/techniques/T1403) <small style="color:#929393">(v1.1)</small>
* [Modify Trusted Execution Environment](/techniques/T1399) <small style="color:#929393">(v1.1)</small>
* [Obtain Device Cloud Backups](/techniques/T1470) <small style="color:#929393">(v1.0)</small>
* [Remotely Wipe Data Without Authorization](/techniques/T1469) <small style="color:#929393">(v1.0)</small>
* [SIM Card Swap](/techniques/T1451) <small style="color:#929393">(v1.2)</small>

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

#### Minor Version Changes

* [FinFisher](/software/S0182) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [XLoader for iOS](/software/S0490) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

#### Other Version Changes

* [Adups](/software/S0309) <small style="color:#eb6635">(v1.1&#8594;v1.0)</small>
* [Allwinner](/software/S0319) <small style="color:#eb6635">(v1.1&#8594;v1.0)</small>
* [AndroRAT](/software/S0292) <small style="color:#eb6635">(v1.1&#8594;v1.0)</small>
* [BrainTest](/software/S0293) <small style="color:#eb6635">(v1.1&#8594;v1.0)</small>
* [DressCode](/software/S0300) <small style="color:#eb6635">(v1.1&#8594;v1.0)</small>
* [DualToy](/software/S0315) <small style="color:#eb6635">(v1.1&#8594;v1.0)</small>
* [HummingBad](/software/S0322) <small style="color:#eb6635">(v1.1&#8594;v1.0)</small>
* [HummingWhale](/software/S0321) <small style="color:#eb6635">(v1.1&#8594;v1.0)</small>
* [Judy](/software/S0325) <small style="color:#eb6635">(v1.1&#8594;v1.0)</small>
* [KeyRaider](/software/S0288) <small style="color:#eb6635">(v1.1&#8594;v1.0)</small>
* [Marcher](/software/S0317) <small style="color:#eb6635">(v1.1&#8594;v1.0)</small>
* [MazarBOT](/software/S0303) <small style="color:#eb6635">(v1.1&#8594;v1.0)</small>
* [NotCompatible](/software/S0299) <small style="color:#eb6635">(v1.1&#8594;v1.0)</small>
* [OBAD](/software/S0286) <small style="color:#eb6635">(v1.1&#8594;v1.0)</small>
* [OldBoot](/software/S0285) <small style="color:#eb6635">(v1.1&#8594;v1.0)</small>
* [PJApps](/software/S0291) <small style="color:#eb6635">(v1.1&#8594;v1.0)</small>
* [RuMMS](/software/S0313) <small style="color:#eb6635">(v1.1&#8594;v1.0)</small>
* [ShiftyBug](/software/S0294) <small style="color:#eb6635">(v1.1&#8594;v1.0)</small>
* [Trojan-SMS.AndroidOS.Agent.ao](/software/S0307) <small style="color:#eb6635">(v1.1&#8594;v1.0)</small>
* [Trojan-SMS.AndroidOS.FakeInst.a](/software/S0306) <small style="color:#eb6635">(v1.1&#8594;v1.0)</small>
* [Trojan-SMS.AndroidOS.OpFake.a](/software/S0308) <small style="color:#eb6635">(v1.1&#8594;v1.0)</small>
* [WireLurker](/software/S0312) <small style="color:#eb6635">(v1.1&#8594;v1.0)</small>
* [X-Agent for Android](/software/S0314) <small style="color:#eb6635">(v1.1&#8594;v1.0)</small>
* [Xbot](/software/S0298) <small style="color:#eb6635">(v1.1&#8594;v1.0)</small>
* [XcodeGhost](/software/S0297) <small style="color:#eb6635">(v1.1&#8594;v1.0)</small>
* [YiSpecter](/software/S0311) <small style="color:#eb6635">(v1.1&#8594;v1.0)</small>
* [ZergHelper](/software/S0287) <small style="color:#eb6635">(v1.1&#8594;v1.0)</small>

#### Metadata-only Changes

* [DroidJack](/software/S0320) <small style="color:#929393">(v1.2)</small>

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

#### Major Version Changes

* [APT28](/groups/G0007) <small style="color:#929393">(v3.2&#8594;v4.0)</small>

#### Minor Version Changes

* [Sandworm Team](/groups/G0034) <small style="color:#929393">(v2.1&#8594;v2.2)</small>

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

#### Deprecations

* [Application Vetting](/mitigations/M1005) <small style="color:#929393">(v1.0)</small>
* [Caution with Device Administrator Access](/mitigations/M1007) <small style="color:#929393">(v1.0)</small>

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

* Alex Hinchliffe, Palo Alto Networks
* Center for Threat-Informed Defense (CTID)
* Dragos  Threat  Intelligence
* Dragos Threat Intelligence
* Drew Church, Splunk
* Edward Millington
* Emily Ratliff, IBM
* Hiroki Nagahama, NEC Corporation
* Joe Slowik -  Dragos
* Krishnan Subramanian, @krish203
* Leo Zhang, Trend Micro
* Manikantan Srinivasan, NEC Corporation India
* Oleksiy Gayda
* Steven Du, Trend Micro
* Thijn Bukkems, Amazon
* Vinay Pidathala
* Zur Ulianitzky, XM Cyber
