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

* Acquire Infrastructure: [Serverless](/techniques/T1583/007) <small style="color:#929393">(v1.0)</small>
* Compromise Accounts: [Cloud Accounts](/techniques/T1586/003) <small style="color:#929393">(v1.0)</small>
* Compromise Infrastructure: [Serverless](/techniques/T1584/007) <small style="color:#929393">(v1.0)</small>
* Establish Accounts: [Cloud Accounts](/techniques/T1585/003) <small style="color:#929393">(v1.0)</small>
* Event Triggered Execution: [Installer Packages](/techniques/T1546/016) <small style="color:#929393">(v1.0)</small>
* Indicator Removal: [Clear Mailbox Data](/techniques/T1070/008) <small style="color:#929393">(v1.0)</small>
* Indicator Removal: [Clear Network Connection History and Configurations](/techniques/T1070/007) <small style="color:#929393">(v1.0)</small>
* Indicator Removal: [Clear Persistence](/techniques/T1070/009) <small style="color:#929393">(v1.0)</small>
* Modify Authentication Process: [Hybrid Identity](/techniques/T1556/007) <small style="color:#929393">(v1.0)</small>
* Modify Authentication Process: [Multi-Factor Authentication](/techniques/T1556/006) <small style="color:#929393">(v1.0)</small>
* Obfuscated Files or Information: [Dynamic API Resolution](/techniques/T1027/007) <small style="color:#929393">(v1.0)</small>
* Obfuscated Files or Information: [Embedded Payloads](/techniques/T1027/009) <small style="color:#929393">(v1.0)</small>
* Obfuscated Files or Information: [Stripped Payloads](/techniques/T1027/008) <small style="color:#929393">(v1.0)</small>
* Search Open Websites/Domains: [Code Repositories](/techniques/T1593/003) <small style="color:#929393">(v1.0)</small>
* [Serverless Execution](/techniques/T1648) <small style="color:#929393">(v1.0)</small>
* Stage Capabilities: [SEO Poisoning](/techniques/T1608/006) <small style="color:#929393">(v1.0)</small>
* [Steal or Forge Authentication Certificates](/techniques/T1649) <small style="color:#929393">(v1.0)</small>
* Traffic Signaling: [Socket Filters](/techniques/T1205/002) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* [Data from Cloud Storage](/techniques/T1530) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Indicator Removal](/techniques/T1070) <small style="color:#929393">(v1.3&#8594;v2.0)</small>

#### Minor Version Changes

* Account Discovery: [Domain Account](/techniques/T1087/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Account Discovery: [Local Account](/techniques/T1087/001) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Account Manipulation](/techniques/T1098) <small style="color:#929393">(v2.3&#8594;v2.4)</small>
    * [Additional Cloud Credentials](/techniques/T1098/001) <small style="color:#929393">(v2.3&#8594;v2.4)</small>
    * [Additional Cloud Roles](/techniques/T1098/003) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Acquire Infrastructure: [Domains](/techniques/T1583/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Adversary-in-the-Middle](/techniques/T1557) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
    * [DHCP Spoofing](/techniques/T1557/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [LLMNR/NBT-NS Poisoning and SMB Relay](/techniques/T1557/001) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Application Layer Protocol: [DNS](/techniques/T1071/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [BITS Jobs](/techniques/T1197) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Boot or Logon Autostart Execution: [Registry Run Keys / Startup Folder](/techniques/T1547/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Boot or Logon Autostart Execution: [Shortcut Modification](/techniques/T1547/009) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Credentials from Password Stores: [Windows Credential Manager](/techniques/T1555/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Data Encrypted for Impact](/techniques/T1486) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* Data from Information Repositories: [Code Repositories](/techniques/T1213/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Data from Local System](/techniques/T1005) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [Data from Network Shared Drive](/techniques/T1039) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Domain Policy Modification: [Domain Trust Modification](/techniques/T1484/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Domain Trust Discovery](/techniques/T1482) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Escape to Host](/techniques/T1611) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Event Triggered Execution](/techniques/T1546) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Exfiltration Over Web Service](/techniques/T1567) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Exfiltration to Cloud Storage](/techniques/T1567/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Exploitation for Privilege Escalation](/techniques/T1068) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [External Remote Services](/techniques/T1133) <small style="color:#929393">(v2.3&#8594;v2.4)</small>
* [File and Directory Discovery](/techniques/T1083) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [File and Directory Permissions Modification](/techniques/T1222) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [Firmware Corruption](/techniques/T1495) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Gather Victim Identity Information: [Email Addresses](/techniques/T1589/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Gather Victim Network Information: [DNS](/techniques/T1590/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Gather Victim Network Information: [Domain Properties](/techniques/T1590/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Impair Defenses](/techniques/T1562) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
    * [Disable or Modify Tools](/techniques/T1562/001) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
    * [Impair Command History Logging](/techniques/T1562/003) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
    * [Indicator Blocking](/techniques/T1562/006) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Indicator Removal: [Clear Command History](/techniques/T1070/003) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Modify Authentication Process](/techniques/T1556) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [Obfuscated Files or Information](/techniques/T1027) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Password Policy Discovery](/techniques/T1201) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* Permission Groups Discovery: [Domain Groups](/techniques/T1069/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Permission Groups Discovery: [Local Groups](/techniques/T1069/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Phishing: [Spearphishing Link](/techniques/T1566/002) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* Phishing for Information: [Spearphishing Link](/techniques/T1598/003) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Process Injection](/techniques/T1055) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
    * [Dynamic-link Library Injection](/techniques/T1055/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [VDSO Hijacking](/techniques/T1055/014) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Remote System Discovery](/techniques/T1018) <small style="color:#929393">(v3.3&#8594;v3.4)</small>
* [Replication Through Removable Media](/techniques/T1091) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Scheduled Task/Job: [Scheduled Task](/techniques/T1053/005) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Search Open Websites/Domains](/techniques/T1593) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Server Software Component](/techniques/T1505) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
    * [Web Shell](/techniques/T1505/003) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Stage Capabilities](/techniques/T1608) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Link Target](/techniques/T1608/005) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Upload Tool](/techniques/T1608/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Subvert Trust Controls: [Code Signing](/techniques/T1553/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Subvert Trust Controls: [Gatekeeper Bypass](/techniques/T1553/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [System Information Discovery](/techniques/T1082) <small style="color:#929393">(v2.4&#8594;v2.5)</small>
* [System Network Configuration Discovery](/techniques/T1016) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [System Network Connections Discovery](/techniques/T1049) <small style="color:#929393">(v2.3&#8594;v2.4)</small>
* [System Service Discovery](/techniques/T1007) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [System Shutdown/Reboot](/techniques/T1529) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Traffic Signaling](/techniques/T1205) <small style="color:#929393">(v2.3&#8594;v2.4)</small>
* [Transfer Data to Cloud Account](/techniques/T1537) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Trusted Relationship](/techniques/T1199) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* Use Alternate Authentication Material: [Application Access Token](/techniques/T1550/001) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Valid Accounts](/techniques/T1078) <small style="color:#929393">(v2.4&#8594;v2.5)</small>

#### Metadata-only Changes

* Abuse Elevation Control Mechanism: [Elevated Execution with Prompt](/techniques/T1548/004) <small style="color:#929393">(v1.0)</small>
* Adversary-in-the-Middle: [ARP Cache Poisoning](/techniques/T1557/002) <small style="color:#929393">(v1.1)</small>
* Brute Force: [Password Guessing](/techniques/T1110/001) <small style="color:#929393">(v1.3)</small>
* Command and Scripting Interpreter: [AppleScript](/techniques/T1059/002) <small style="color:#929393">(v1.1)</small>
* [Compromise Infrastructure](/techniques/T1584) <small style="color:#929393">(v1.2)</small>
* Create or Modify System Process: [Windows Service](/techniques/T1543/003) <small style="color:#929393">(v1.2)</small>
* [Data Staged](/techniques/T1074) <small style="color:#929393">(v1.4)</small>
* Defacement: [Internal Defacement](/techniques/T1491/001) <small style="color:#929393">(v1.1)</small>
* [Disk Wipe](/techniques/T1561) <small style="color:#929393">(v1.0)</small>
    * [Disk Content Wipe](/techniques/T1561/001) <small style="color:#929393">(v1.0)</small>
* Hijack Execution Flow: [Path Interception by Unquoted Path](/techniques/T1574/009) <small style="color:#929393">(v1.1)</small>
* Impair Defenses: [Downgrade Attack](/techniques/T1562/010) <small style="color:#929393">(v1.1)</small>
* [Ingress Tool Transfer](/techniques/T1105) <small style="color:#929393">(v2.1)</small>
* [Multi-Factor Authentication Request Generation](/techniques/T1621) <small style="color:#929393">(v1.0)</small>
* [Network Sniffing](/techniques/T1040) <small style="color:#929393">(v1.3)</small>
* OS Credential Dumping: [LSASS Memory](/techniques/T1003/001) <small style="color:#929393">(v1.1)</small>
* OS Credential Dumping: [Security Account Manager](/techniques/T1003/002) <small style="color:#929393">(v1.0)</small>
* Obfuscated Files or Information: [HTML Smuggling](/techniques/T1027/006) <small style="color:#929393">(v1.0)</small>
* [Search Open Technical Databases](/techniques/T1596) <small style="color:#929393">(v1.0)</small>
* [Service Stop](/techniques/T1489) <small style="color:#929393">(v1.2)</small>
* System Binary Proxy Execution: [MMC](/techniques/T1218/014) <small style="color:#929393">(v2.0)</small>
* System Binary Proxy Execution: [Verclsid](/techniques/T1218/012) <small style="color:#929393">(v2.0)</small>
* User Execution: [Malicious File](/techniques/T1204/002) <small style="color:#929393">(v1.2)</small>

#### Unknown Changes

* Active Scanning: [Wordlist Scanning](/techniques/T1595/003) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>

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

#### Metadata-only Changes

* [Call Control](/techniques/T1616) <small style="color:#929393">(v1.0)</small>
* [Compromise Application Executable](/techniques/T1577) <small style="color:#929393">(v1.0)</small>
* [Hooking](/techniques/T1617) <small style="color:#929393">(v1.0)</small>
* [Input Injection](/techniques/T1516) <small style="color:#929393">(v1.1)</small>
* [Proxy Through Victim](/techniques/T1604) <small style="color:#929393">(v1.0)</small>
* [SMS Control](/techniques/T1582) <small style="color:#929393">(v1.0)</small>
* [Scheduled Task/Job](/techniques/T1603) <small style="color:#929393">(v1.0)</small>

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

#### New Techniques

* [Hardcoded Credentials](/techniques/T0891) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* [Adversary-in-the-Middle](/techniques/T0830) <small style="color:#929393">(v1.0&#8594;v2.0)</small>

#### Minor Version Changes

* [Alarm Suppression](/techniques/T0878) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Block Serial COM](/techniques/T0805) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Command-Line Interface](/techniques/T0807) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Commonly Used Port](/techniques/T0885) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Connection Proxy](/techniques/T0884) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Data from Information Repositories](/techniques/T0811) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Device Restart/Shutdown](/techniques/T0816) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Execution through API](/techniques/T0871) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Exploitation for Evasion](/techniques/T0820) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Exploitation for Privilege Escalation](/techniques/T0890) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Graphical User Interface](/techniques/T0823) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Hooking](/techniques/T0874) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [I/O Image](/techniques/T0877) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Lateral Tool Transfer](/techniques/T0867) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Manipulate I/O Image](/techniques/T0835) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Masquerading](/techniques/T0849) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Modify Alarm Settings](/techniques/T0838) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Modify Controller Tasking](/techniques/T0821) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Modify Parameter](/techniques/T0836) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Modify Program](/techniques/T0889) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Module Firmware](/techniques/T0839) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Network Connection Enumeration](/techniques/T0840) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Point & Tag Identification](/techniques/T0861) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Program Download](/techniques/T0843) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Remote Services](/techniques/T0886) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Remote System Discovery](/techniques/T0846) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Remote System Information Discovery](/techniques/T0888) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Rogue Master](/techniques/T0848) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Rootkit](/techniques/T0851) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Spearphishing Attachment](/techniques/T0865) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Spoof Reporting Message](/techniques/T0856) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Supply Chain Compromise](/techniques/T0862) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [System Firmware](/techniques/T0857) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Transient Cyber Asset](/techniques/T0864) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Unauthorized Command Message](/techniques/T0855) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [User Execution](/techniques/T0863) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Valid Accounts](/techniques/T0859) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Wireless Compromise](/techniques/T0860) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Wireless Sniffing](/techniques/T0887) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

#### Metadata-only Changes

* [Activate Firmware Update Mode](/techniques/T0800) <small style="color:#929393">(v1.0)</small>
* [Automated Collection](/techniques/T0802) <small style="color:#929393">(v1.0)</small>
* [Block Command Message](/techniques/T0803) <small style="color:#929393">(v1.0)</small>
* [Block Reporting Message](/techniques/T0804) <small style="color:#929393">(v1.0)</small>
* [Brute Force I/O](/techniques/T0806) <small style="color:#929393">(v1.0)</small>
* [Change Operating Mode](/techniques/T0858) <small style="color:#929393">(v1.0)</small>
* [Damage to Property](/techniques/T0879) <small style="color:#929393">(v1.0)</small>
* [Data Destruction](/techniques/T0809) <small style="color:#929393">(v1.0)</small>
* [Default Credentials](/techniques/T0812) <small style="color:#929393">(v1.0)</small>
* [Denial of Control](/techniques/T0813) <small style="color:#929393">(v1.0)</small>
* [Denial of Service](/techniques/T0814) <small style="color:#929393">(v1.0)</small>
* [Denial of View](/techniques/T0815) <small style="color:#929393">(v1.0)</small>
* [Detect Operating Mode](/techniques/T0868) <small style="color:#929393">(v1.0)</small>
* [Drive-by Compromise](/techniques/T0817) <small style="color:#929393">(v1.0)</small>
* [Exploit Public-Facing Application](/techniques/T0819) <small style="color:#929393">(v1.0)</small>
* [Exploitation of Remote Services](/techniques/T0866) <small style="color:#929393">(v1.0)</small>
* [External Remote Services](/techniques/T0822) <small style="color:#929393">(v1.0)</small>
* [Indicator Removal on Host](/techniques/T0872) <small style="color:#929393">(v1.0)</small>
* [Internet Accessible Device](/techniques/T0883) <small style="color:#929393">(v1.0)</small>
* [Loss of Availability](/techniques/T0826) <small style="color:#929393">(v1.0)</small>
* [Loss of Control](/techniques/T0827) <small style="color:#929393">(v1.0)</small>
* [Loss of Productivity and Revenue](/techniques/T0828) <small style="color:#929393">(v1.0)</small>
* [Loss of Protection](/techniques/T0837) <small style="color:#929393">(v1.0)</small>
* [Loss of Safety](/techniques/T0880) <small style="color:#929393">(v1.0)</small>
* [Loss of View](/techniques/T0829) <small style="color:#929393">(v1.0)</small>
* [Manipulation of Control](/techniques/T0831) <small style="color:#929393">(v1.0)</small>
* [Manipulation of View](/techniques/T0832) <small style="color:#929393">(v1.0)</small>
* [Monitor Process State](/techniques/T0801) <small style="color:#929393">(v1.0)</small>
* [Native API](/techniques/T0834) <small style="color:#929393">(v1.0)</small>
* [Network Sniffing](/techniques/T0842) <small style="color:#929393">(v1.0)</small>
* [Program Upload](/techniques/T0845) <small style="color:#929393">(v1.0)</small>
* [Project File Infection](/techniques/T0873) <small style="color:#929393">(v1.0)</small>
* [Replication Through Removable Media](/techniques/T0847) <small style="color:#929393">(v1.0)</small>
* [Screen Capture](/techniques/T0852) <small style="color:#929393">(v1.0)</small>
* [Scripting](/techniques/T0853) <small style="color:#929393">(v1.0)</small>
* [Service Stop](/techniques/T0881) <small style="color:#929393">(v1.0)</small>
* [Standard Application Layer Protocol](/techniques/T0869) <small style="color:#929393">(v1.0)</small>
* [Theft of Operational Information](/techniques/T0882) <small style="color:#929393">(v1.0)</small>

## Software

### Enterprise

#### New Software

* [Action RAT](/software/S1028) <small style="color:#929393">(v1.0)</small>
* [Amadey](/software/S1025) <small style="color:#929393">(v1.0)</small>
* [AuTo Stealer](/software/S1029) <small style="color:#929393">(v1.0)</small>
* [Bumblebee](/software/S1039) <small style="color:#929393">(v1.0)</small>
* [Chinoxy](/software/S1041) <small style="color:#929393">(v1.0)</small>
* [CreepyDrive](/software/S1023) <small style="color:#929393">(v1.0)</small>
* [CreepySnail](/software/S1024) <small style="color:#929393">(v1.0)</small>
* [DCSrv](/software/S1033) <small style="color:#929393">(v1.0)</small>
* [DanBot](/software/S1014) <small style="color:#929393">(v1.0)</small>
* [DnsSystem](/software/S1021) <small style="color:#929393">(v1.0)</small>
* [FunnyDream](/software/S1044) <small style="color:#929393">(v1.0)</small>
* [Heyoka Backdoor](/software/S1027) <small style="color:#929393">(v1.0)</small>
* [IceApple](/software/S1022) <small style="color:#929393">(v1.0)</small>
* [Kevin](/software/S1020) <small style="color:#929393">(v1.0)</small>
* [MacMa](/software/S1016) <small style="color:#929393">(v1.0)</small>
* [Milan](/software/S1015) <small style="color:#929393">(v1.0)</small>
* [Mongall](/software/S1026) <small style="color:#929393">(v1.0)</small>
* [Mori](/software/S1047) <small style="color:#929393">(v1.0)</small>
* [OutSteel](/software/S1017) <small style="color:#929393">(v1.0)</small>
* [PcShare](/software/S1050) <small style="color:#929393">(v1.0)</small>
* [PingPull](/software/S1031) <small style="color:#929393">(v1.0)</small>
* [PowGoop](/software/S1046) <small style="color:#929393">(v1.0)</small>
* [PowerLess](/software/S1012) <small style="color:#929393">(v1.0)</small>
* [PyDCrypt](/software/S1032) <small style="color:#929393">(v1.0)</small>
* [Rclone](/software/S1040) <small style="color:#929393">(v1.0)</small>
* [STARWHALE](/software/S1037) <small style="color:#929393">(v1.0)</small>
* [SUGARDUMP](/software/S1042) <small style="color:#929393">(v1.0)</small>
* [SUGARUSH](/software/S1049) <small style="color:#929393">(v1.0)</small>
* [Saint Bot](/software/S1018) <small style="color:#929393">(v1.0)</small>
* [Shark](/software/S1019) <small style="color:#929393">(v1.0)</small>
* [Small Sieve](/software/S1035) <small style="color:#929393">(v1.0)</small>
* [Squirrelwaffle](/software/S1030) <small style="color:#929393">(v1.0)</small>
* [StrifeWater](/software/S1034) <small style="color:#929393">(v1.0)</small>
* [Tarrask](/software/S1011) <small style="color:#929393">(v1.0)</small>
* [ZxxZ](/software/S1013) <small style="color:#929393">(v1.0)</small>
* [ccf32](/software/S1043) <small style="color:#929393">(v1.0)</small>
* [macOS.OSAMiner](/software/S1048) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* [QuasarRAT](/software/S0262) <small style="color:#929393">(v1.3&#8594;v2.0)</small>
* [Rising Sun](/software/S0448) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [zwShell](/software/S0350) <small style="color:#929393">(v1.1&#8594;v2.0)</small>

#### Minor Version Changes

* [AADInternals](/software/S0677) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [ASPXSpy](/software/S0073) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [AdFind](/software/S0552) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [AppleJeus](/software/S0584) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Azorult](/software/S0344) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [BITSAdmin](/software/S0190) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Bazar](/software/S0534) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [BloodHound](/software/S0521) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Cobalt Strike](/software/S0154) <small style="color:#929393">(v1.8&#8594;v1.9)</small>
* [ComRAT](/software/S0126) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Conti](/software/S0575) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [CostaBricks](/software/S0614) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Crimson](/software/S0115) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Dtrack](/software/S0567) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Empire](/software/S0363) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [FlawedAmmyy](/software/S0381) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Goopy](/software/S0477) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [GrimAgent](/software/S0632) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Impacket](/software/S0357) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Industroyer](/software/S0604) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Invoke-PSImage](/software/S0231) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [KOCTOPUS](/software/S0669) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [MCMD](/software/S0500) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Mimikatz](/software/S0002) <small style="color:#929393">(v1.5&#8594;v1.6)</small>
* [Mis-Type](/software/S0084) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Misdat](/software/S0083) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [OSX/Shlayer](/software/S0402) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [POWERSTATS](/software/S0223) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [PS1](/software/S0613) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Penquin](/software/S0587) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Pillowmint](/software/S0517) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Ping](/software/S0097) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [PoisonIvy](/software/S0012) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [PoshC2](/software/S0378) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [PowerSploit](/software/S0194) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [PsExec](/software/S0029) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Pteranodon](/software/S0147) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [RTM](/software/S0148) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Reg](/software/S0075) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Remcos](/software/S0332) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [S-Type](/software/S0085) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [SDBbot](/software/S0461) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [SMOKEDHAM](/software/S0649) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [SUNBURST](/software/S0559) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* [SYSCON](/software/S0464) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [ShadowPad](/software/S0596) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [SombRAT](/software/S0615) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Stuxnet](/software/S0603) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Systeminfo](/software/S0096) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Tasklist](/software/S0057) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Tor](/software/S0183) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Wevtutil](/software/S0645) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [XCSSET](/software/S0658) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [ZLib](/software/S0086) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [at](/software/S0110) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [cmd](/software/S0106) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [dsquery](/software/S0105) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [gh0st RAT](/software/S0032) <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* [gsecdump](/software/S0008) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [ipconfig](/software/S0100) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [netstat](/software/S0104) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [njRAT](/software/S0385) <small style="color:#929393">(v1.3&#8594;v1.4)</small>

#### Metadata-only Changes

* [Backdoor.Oldrea](/software/S0093) <small style="color:#929393">(v2.0)</small>
* [Bad Rabbit](/software/S0606) <small style="color:#929393">(v1.0)</small>
* [BlackEnergy](/software/S0089) <small style="color:#929393">(v1.3)</small>
* [CSPY Downloader](/software/S0527) <small style="color:#929393">(v1.0)</small>
* [Conficker](/software/S0608) <small style="color:#929393">(v1.0)</small>
* [DarkWatchman](/software/S0673) <small style="color:#929393">(v1.0)</small>
* [Duqu](/software/S0038) <small style="color:#929393">(v1.2)</small>
* [EKANS](/software/S0605) <small style="color:#929393">(v2.0)</small>
* [ELMER](/software/S0064) <small style="color:#929393">(v1.1)</small>
* [Flame](/software/S0143) <small style="color:#929393">(v1.1)</small>
* [Grandoreiro](/software/S0531) <small style="color:#929393">(v1.0)</small>
* [HermeticWiper](/software/S0697) <small style="color:#929393">(v1.0)</small>
* [IronNetInjector](/software/S0581) <small style="color:#929393">(v1.0)</small>
* [KillDisk](/software/S0607) <small style="color:#929393">(v1.1)</small>
* [LockerGoga](/software/S0372) <small style="color:#929393">(v2.0)</small>
* [Metamorfo](/software/S0455) <small style="color:#929393">(v2.0)</small>
* [MirageFox](/software/S0280) <small style="color:#929393">(v1.1)</small>
* [Mivast](/software/S0080) <small style="color:#929393">(v1.1)</small>
* [Net Crawler](/software/S0056) <small style="color:#929393">(v1.1)</small>
* [NotPetya](/software/S0368) <small style="color:#929393">(v2.0)</small>
* [POWERSOURCE](/software/S0145) <small style="color:#929393">(v1.1)</small>
* [REvil](/software/S0496) <small style="color:#929393">(v2.0)</small>
* [RawDisk](/software/S0364) <small style="color:#929393">(v1.0)</small>
* [Ryuk](/software/S0446) <small style="color:#929393">(v1.3)</small>
* [Sibot](/software/S0589) <small style="color:#929393">(v1.0)</small>
* [TEXTMATE](/software/S0146) <small style="color:#929393">(v1.1)</small>
* [TinyZBot](/software/S0004) <small style="color:#929393">(v1.1)</small>
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

* [ANDROIDOS_ANSERVER.A](/software/S0310) <small style="color:#929393">(v1.3)</small>
* [Android/Chuli.A](/software/S0304) <small style="color:#929393">(v1.2)</small>
* [Charger](/software/S0323) <small style="color:#929393">(v1.1)</small>
* [Dendroid](/software/S0301) <small style="color:#929393">(v2.0)</small>
* [DroidJack](/software/S0320) <small style="color:#929393">(v1.2)</small>
* [Gooligan](/software/S0290) <small style="color:#929393">(v1.2)</small>
* [Pegasus for Android](/software/S0316) <small style="color:#929393">(v1.2)</small>
* [Pegasus for iOS](/software/S0289) <small style="color:#929393">(v1.1)</small>
* [RCSAndroid](/software/S0295) <small style="color:#929393">(v1.2)</small>
* [RedDrop](/software/S0326) <small style="color:#929393">(v1.2)</small>
* [Skygofree](/software/S0327) <small style="color:#929393">(v1.2)</small>
* [SpyDealer](/software/S0324) <small style="color:#929393">(v1.2)</small>
* [SpyNote RAT](/software/S0305) <small style="color:#929393">(v1.2)</small>
* [Stealth Mango](/software/S0328) <small style="color:#929393">(v1.3)</small>
* [Tangelo](/software/S0329) <small style="color:#929393">(v1.2)</small>
* [Twitoor](/software/S0302) <small style="color:#929393">(v2.0)</small>
* [XLoader for Android](/software/S0318) <small style="color:#929393">(v2.0)</small>

### ICS

#### New Software

* [Bad Rabbit](/Software/S0005) <small style="color:#929393">(v1.0)</small>
* [BlackEnergy 3](/Software/S0004) <small style="color:#929393">(v1.0)</small>
* [Conficker](/Software/S0012) <small style="color:#929393">(v1.0)</small>
* [EKANS](/Software/S0017) <small style="color:#929393">(v1.0)</small>
* [INCONTROLLER](/software/S1045) <small style="color:#929393">(v1.0)</small>
* [Industroyer](/Software/S0001) <small style="color:#929393">(v1.0)</small>
* [Killdisk](/Software/S0016) <small style="color:#929393">(v1.0)</small>
* [Stuxnet](/Software/S0010) <small style="color:#929393">(v1.0)</small>

#### Minor Version Changes

* [Industroyer](/software/S0604) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Stuxnet](/software/S0603) <small style="color:#929393">(v1.1&#8594;v1.2)</small>

#### Metadata-only Changes

* [ACAD/Medre.A](/software/S1000) <small style="color:#929393">(v1.0)</small>
* [Backdoor.Oldrea](/software/S0093) <small style="color:#929393">(v2.0)</small>
* [Bad Rabbit](/software/S0606) <small style="color:#929393">(v1.0)</small>
* [BlackEnergy](/software/S0089) <small style="color:#929393">(v1.3)</small>
* [Conficker](/software/S0608) <small style="color:#929393">(v1.0)</small>
* [Duqu](/software/S0038) <small style="color:#929393">(v1.2)</small>
* [EKANS](/software/S0605) <small style="color:#929393">(v2.0)</small>
* [Flame](/software/S0143) <small style="color:#929393">(v1.1)</small>
* [KillDisk](/software/S0607) <small style="color:#929393">(v1.1)</small>
* [LockerGoga](/software/S0372) <small style="color:#929393">(v2.0)</small>
* [NotPetya](/software/S0368) <small style="color:#929393">(v2.0)</small>
* [PLC-Blaster](/software/S1006) <small style="color:#929393">(v1.0)</small>
* [REvil](/software/S0496) <small style="color:#929393">(v2.0)</small>
* [Ryuk](/software/S0446) <small style="color:#929393">(v1.3)</small>
* [Triton](/software/S1009) <small style="color:#929393">(v1.0)</small>
* [VPNFilter](/software/S1010) <small style="color:#929393">(v1.0)</small>
* [WannaCry](/software/S0366) <small style="color:#929393">(v1.1)</small>

## Groups

### Enterprise

#### New Groups

* [Aoqin Dragon](/groups/G1007) <small style="color:#929393">(v1.0)</small>
* [BITTER](/groups/G1002) <small style="color:#929393">(v1.0)</small>
* [EXOTIC LILY](/groups/G1011) <small style="color:#929393">(v1.0)</small>
* [Earth Lusca](/groups/G1006) <small style="color:#929393">(v1.0)</small>
* [Ember Bear](/groups/G1003) <small style="color:#929393">(v1.0)</small>
* [HEXANE](/groups/G1001) <small style="color:#eb6635">(v2.0)</small>
* [LAPSUS$](/groups/G1004) <small style="color:#929393">(v1.0)</small>
* [Moses Staff](/groups/G1009) <small style="color:#929393">(v1.0)</small>
* [POLONIUM](/groups/G1005) <small style="color:#929393">(v1.0)</small>
* [SideCopy](/groups/G1008) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* [GALLIUM](/groups/G0093) <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* [Magic Hound](/groups/G0059) <small style="color:#929393">(v4.1&#8594;v5.0)</small>
* [MuddyWater](/groups/G0069) <small style="color:#929393">(v3.0&#8594;v4.0)</small>
* [TA505](/groups/G0092) <small style="color:#929393">(v1.3&#8594;v2.0)</small>

#### Minor Version Changes

* [APT29](/groups/G0016) <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* [CopyKittens](/groups/G0052) <small style="color:#929393">(v1.5&#8594;v1.6)</small>
* [Darkhotel](/groups/G0012) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Dragonfly](/groups/G0035) <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* [HAFNIUM](/groups/G0125) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Lazarus Group](/groups/G0032) <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* [TeamTNT](/groups/G0139) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Transparent Tribe](/groups/G0134) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

#### Metadata-only Changes

* [APT16](/groups/G0023) <small style="color:#929393">(v1.1)</small>
* [APT33](/groups/G0064) <small style="color:#929393">(v1.4)</small>
* [APT39](/groups/G0087) <small style="color:#929393">(v3.1)</small>
* [APT41](/groups/G0096) <small style="color:#929393">(v3.0)</small>
* [Andariel](/groups/G0138) <small style="color:#929393">(v1.0)</small>
* [Aquatic Panda](/groups/G0143) <small style="color:#929393">(v1.0)</small>
* [Cleaver](/groups/G0003) <small style="color:#929393">(v1.3)</small>
* [Confucius](/groups/G0142) <small style="color:#929393">(v1.0)</small>
* [Deep Panda](/groups/G0009) <small style="color:#929393">(v1.2)</small>
* [FIN6](/groups/G0037) <small style="color:#929393">(v3.2)</small>
* [FIN7](/groups/G0046) <small style="color:#929393">(v2.1)</small>
* [Fox Kitten](/groups/G0117) <small style="color:#929393">(v1.0)</small>
* [Indrik Spider](/groups/G0119) <small style="color:#929393">(v2.1)</small>
* [Ke3chang](/groups/G0004) <small style="color:#929393">(v2.0)</small>
* [Kimsuky](/groups/G0094) <small style="color:#929393">(v3.1)</small>
* [Nomadic Octopus](/groups/G0133) <small style="color:#929393">(v1.0)</small>
* [OilRig](/groups/G0049) <small style="color:#929393">(v3.0)</small>
* [Patchwork](/groups/G0040) <small style="color:#929393">(v1.4)</small>
* [Sandworm Team](/groups/G0034) <small style="color:#929393">(v2.2)</small>
* [Silence](/groups/G0091) <small style="color:#929393">(v2.1)</small>
* [TEMP.Veles](/groups/G0088) <small style="color:#929393">(v1.3)</small>
* [Turla](/groups/G0010) <small style="color:#929393">(v3.0)</small>
* [menuPass](/groups/G0045) <small style="color:#929393">(v2.1)</small>

#### Deprecations

* [CostaRicto](/groups/G0132) <small style="color:#929393">(v1.0)</small>
* [Dust Storm](/groups/G0031) <small style="color:#929393">(v1.0)</small>
* [Frankenstein](/groups/G0101) <small style="color:#929393">(v1.1)</small>
* [Honeybee](/groups/G0072) <small style="color:#929393">(v1.1)</small>
* [Night Dragon](/groups/G0014) <small style="color:#929393">(v1.4)</small>
* [Operation Wocao](/groups/G0116) <small style="color:#929393">(v1.0)</small>
* [Sharpshooter](/groups/G0104) <small style="color:#929393">(v1.0)</small>

### Mobile

#### New Groups

* [Earth Lusca](/groups/G1006) <small style="color:#929393">(v1.0)</small>

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

#### Major Version Changes

* [HEXANE](/groups/G1001) <small style="color:#929393">(v1.0&#8594;v2.0)</small>

#### Minor Version Changes

* [Dragonfly](/groups/G0035) <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* [Lazarus Group](/groups/G0032) <small style="color:#929393">(v3.0&#8594;v3.1)</small>

#### Metadata-only Changes

* [ALLANITE](/groups/G1000) <small style="color:#929393">(v1.0)</small>
* [APT33](/groups/G0064) <small style="color:#929393">(v1.4)</small>
* [OilRig](/groups/G0049) <small style="color:#929393">(v3.0)</small>
* [Sandworm Team](/groups/G0034) <small style="color:#929393">(v2.2)</small>
* [TEMP.Veles](/groups/G0088) <small style="color:#929393">(v1.3)</small>

## Campaigns

### Enterprise

#### New Campaigns

* [C0010](/campaigns/C0010) <small style="color:#929393">(v1.0)</small>
* [C0011](/campaigns/C0011) <small style="color:#929393">(v1.0)</small>
* [C0015](/campaigns/C0015) <small style="color:#929393">(v1.0)</small>
* [CostaRicto](/campaigns/C0004) <small style="color:#929393">(v1.0)</small>
* [Frankenstein](/campaigns/C0001) <small style="color:#929393">(v1.0)</small>
* [FunnyDream](/campaigns/C0007) <small style="color:#929393">(v1.0)</small>
* [Night Dragon](/campaigns/C0002) <small style="color:#929393">(v1.0)</small>
* [Operation CuckooBees](/campaigns/C0012) <small style="color:#929393">(v1.0)</small>
* [Operation Dust Storm](/campaigns/C0016) <small style="color:#929393">(v1.0)</small>
* [Operation Honeybee](/campaigns/C0006) <small style="color:#929393">(v1.0)</small>
* [Operation Sharpshooter](/campaigns/C0013) <small style="color:#929393">(v1.0)</small>
* [Operation Spalax](/campaigns/C0005) <small style="color:#929393">(v1.0)</small>
* [Operation Wocao](/campaigns/C0014) <small style="color:#929393">(v1.0)</small>

### Mobile

#### New Campaigns

* [Operation Dust Storm](/campaigns/C0016) <small style="color:#929393">(v1.0)</small>

### ICS

#### New Campaigns

* [Oldsmar Treatment Plant Intrusion](/campaigns/C0009) <small style="color:#929393">(v1.0)</small>

## Mitigations

### Enterprise

#### Metadata-only Changes

* [Account Use Policies](/mitigations/M1036) <small style="color:#929393">(v1.0)</small>
* [Audit](/mitigations/M1047) <small style="color:#929393">(v1.1)</small>
* [Credential Access Protection](/mitigations/M1043) <small style="color:#929393">(v1.1)</small>
* [Multi-factor Authentication](/mitigations/M1032) <small style="color:#929393">(v1.0)</small>
* [Password Policies](/mitigations/M1027) <small style="color:#929393">(v1.0)</small>

### Mobile

#### Deprecations

* [Application Vetting](/mitigations/M1005) <small style="color:#929393">(v1.0)</small>
* [Caution with Device Administrator Access](/mitigations/M1007) <small style="color:#929393">(v1.0)</small>

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

#### Minor Version Changes

* [Command](/data-sources/DS0017) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Logon Session](/data-sources/DS0028) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Malware Repository](/data-sources/DS0004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Network Traffic](/data-sources/DS0029) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Process](/data-sources/DS0009) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Script](/data-sources/DS0012) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Sensor Health](/data-sources/DS0013) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [User Account](/data-sources/DS0002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

#### Metadata-only Changes

* [Application Log](/datasources/DS0015) <small style="color:#929393">(v1.0)</small>
* [Windows Registry](/datasources/DS0024) <small style="color:#929393">(v1.0)</small>

#### Deprecations

* [Cluster](/data-sources/DS0031) <small style="color:#929393">(v1.0)</small>

### Mobile

### ICS

#### Minor Version Changes

* [Command](/data-sources/DS0017) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Logon Session](/data-sources/DS0028) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Network Traffic](/data-sources/DS0029) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Process](/data-sources/DS0009) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Script](/data-sources/DS0012) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [User Account](/data-sources/DS0002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

#### Metadata-only Changes

* [Application Log](/datasources/DS0015) <small style="color:#929393">(v1.0)</small>
* [Asset](/data-sources/DS0039) <small style="color:#929393">(v1.0)</small>
* [Operational Databases](/datasources/DS0040) <small style="color:#929393">(v1.0)</small>
* [Windows Registry](/datasources/DS0024) <small style="color:#929393">(v1.0)</small>

## Data Components

### Enterprise

#### Minor Version Changes

* [Command Execution](/data-sources/DS0017/#Command%20Execution) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Host Status](/data-sources/DS0013/#Host%20Status) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Logon Session Creation](/data-sources/DS0028/#Logon%20Session%20Creation) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Malware Content](/data-sources/DS0004/#Malware%20Content) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Malware Metadata](/data-sources/DS0004/#Malware%20Metadata) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Network Connection Creation](/data-sources/DS0029/#Network%20Connection%20Creation) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Process Creation](/data-sources/DS0009/#Process%20Creation) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Script Execution](/data-sources/DS0012/#Script%20Execution) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [User Account Authentication](/data-sources/DS0002/#User%20Account%20Authentication) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

#### Deprecations

* [Cluster Metadata](/data-sources/DS0031/#Cluster%20Metadata) <small style="color:#929393">(v1.0)</small>

### Mobile

### ICS

#### New Data Components

* [Asset Inventory](/data-sources/DS0039/#Asset%20Inventory) <small style="color:#929393">(v1.0)</small>
* [Scheduled Job Creation](/datasources/DS0003/#Scheduled%20Job%20Creation) <small style="color:#929393">(v1.0)</small>
* [Service Modification](/datasources/DS0019/#Service%20Modification) <small style="color:#929393">(v1.0)</small>
* [Software](/data-sources/DS0039/#Software) <small style="color:#929393">(v1.0)</small>

#### Minor Version Changes

* [Command Execution](/data-sources/DS0017/#Command%20Execution) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Logon Session Creation](/data-sources/DS0028/#Logon%20Session%20Creation) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Network Connection Creation](/data-sources/DS0029/#Network%20Connection%20Creation) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Process Creation](/data-sources/DS0009/#Process%20Creation) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Script Execution](/data-sources/DS0012/#Script%20Execution) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [User Account Authentication](/data-sources/DS0002/#User%20Account%20Authentication) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

#### Metadata-only Changes

* [Device Alarm](/datasources/DS0040/#Device%20Alarm) <small style="color:#929393">(v1.0)</small>
* [Process History/Live Data](/datasources/DS0040/#Process%20History/Live%20Data) <small style="color:#929393">(v1.0)</small>
* [Process/Event Alarm](/datasources/DS0040/#Process/Event%20Alarm) <small style="color:#929393">(v1.0)</small>

## Contributors to this release

* Aagam Shah, @neutrinoguy, ABB
* Alex Hinchliffe, Palo Alto Networks
* Alex Soler, AttackIQ
* Andrea Serrano Urea, Telefónica Tech
* Andrew Allen, @whitehat_zero
* AppOmni
* Austin Clark, @c2defense
* Awake Security
* Blake Strom, Microsoft 365 Defender
* Boominathan Sundaram
* Brandon Dalton @PartyD0lphin
* Catherine Williams, BT Security
* Center for Threat-Informed Defense (CTID)
* Chris Heald
* Cian Heasley
* Cisco
* CrowdStrike
* CrowdStrike Falcon OverWatch
* Daniel Feichter, @VirtualAllocEx, Infosec Tirol
* Daniyal Naeem, BT Security
* Darin Smith, Cisco
* David Hughes, BT Security
* David Tayouri
* Dragos  Threat  Intelligence
* Dragos Threat Intelligence
* Dray Agha, @Purp1eW0lf, Huntress Labs
* Drew Church, Splunk
* Edward Millington
* Emily Ratliff, IBM
* Eran Ayalon, Cybereason
* Erik Schamper, @Schamperr, Fox-IT
* ExtraHop
* Flavio Costa, Cisco
* Francesco Bigarella
* Goldstein Menachem
* Hannah Simes, BT Security
* Harry Hill, BT Security
* Harshal Tupsamudre, Qualys
* Hiroki Nagahama, NEC Corporation
* Ian Davila, Tidal Cyber
* Ian McKay
* Ilan Sokol, Cybereason
* Jannie Li, Microsoft Threat Intelligence Center (MSTIC)
* Joas Antonio dos Santos, @Cr4zyC0d3
* Joe Slowik -  Dragos
* Krishnan Subramanian, @krish203
* Kyaw Pyiyt Htet, @KyawPyiytHtet
* Lee Christensen, SpecterOps
* Leo Zhang, Trend Micro
* Liran Ravich, CardinalOps
* Lucas Heiligenstein
* Maarten van Dantzig, @MaartenVDantzig, Fox-IT
* Manikanran Srinivasan, NEC Corporation India
* Manikantan Srinivasan , NEC Corporation India
* Manikantan Srinivasan, NEC Corporation India
* Matt Brenton, Zurich Insurance Group
* Matt Burrough, @mattburrough, Microsoft
* Menachem Goldstein
* Mindaugas Gudzis, BT Security
* Miriam Wiesner, @miriamxyra, Microsoft Security
* Nick Cairns, @grotezinfosec
* Oleg Kolesnikov, Securonix
* Oleksiy Gayda
* Oren Ofer, Cybereason
* Ozer Sarilar, @ozersarilar, STM
* Phil Taylor, BT Security
* Phill Taylor, BT Security
* Pooja Natarajan, NEC Corporation India
* Praetorian
* Raphaël Lheureux
* Sarathkumar Rajendran, Microsoft Defender365
* Sebastian Showell-Westrip, BT Security
* Sekhar Sarukkai, McAfee
* Shailesh Tiwary (Indian Army)
* Shanief Webb
* Sittikorn Sangrattanapitak
* Steven Du, Trend Micro
* Swasti Bhushan Deb, IBM India Pvt. Ltd.
* Thijn Bukkems, Amazon
* Thirumalai Natarajan, Mandiant
* Tim (Wadhwa-)Brown
* Tristan Bennett, Seamless Intelligence
* Uriel Kosayev
* Vadim Khrykov
* Varonis Threat Labs
* Vijay Lalwani
* Vinay Pidathala
* Vinayak Wadhwa, Lucideus
* Will Thomas, Equinix Threat Analysis Center (ETAC)
* Yoshihiro Kori, NEC Corporation
* Zur Ulianitzky, XM Cyber
