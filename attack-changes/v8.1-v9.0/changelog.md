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

* Boot or Logon Autostart Execution: [Active Setup](/techniques/T1547/014) <small style="color:#929393">(v1.0)</small>
* Boot or Logon Autostart Execution: [XDG Autostart Entries](/techniques/T1547/013) <small style="color:#929393">(v1.0)</small>
* [Build Image on Host](/techniques/T1612) <small style="color:#929393">(v1.0)</small>
* [Container Administration Command](/techniques/T1609) <small style="color:#929393">(v1.0)</small>
* [Container and Resource Discovery](/techniques/T1613) <small style="color:#929393">(v1.0)</small>
* Credentials from Password Stores: [Password Managers](/techniques/T1555/005) <small style="color:#929393">(v1.0)</small>
* Credentials from Password Stores: [Windows Credential Manager](/techniques/T1555/004) <small style="color:#929393">(v1.0)</small>
* [Deploy Container](/techniques/T1610) <small style="color:#929393">(v1.0)</small>
* Domain Policy Modification: [Domain Trust Modification](/techniques/T1484/002) <small style="color:#929393">(v1.0)</small>
* Domain Policy Modification: [Group Policy Modification](/techniques/T1484/001) <small style="color:#929393">(v1.0)</small>
* [Escape to Host](/techniques/T1611) <small style="color:#929393">(v1.0)</small>
* [Forge Web Credentials](/techniques/T1606) <small style="color:#eb6635">(v1.1)</small>
    * [SAML Tokens](/techniques/T1606/002) <small style="color:#eb6635">(v1.1)</small>
    * [Web Cookies](/techniques/T1606/001) <small style="color:#929393">(v1.0)</small>
* Scheduled Task/Job: [Container Orchestration Job](/techniques/T1053/007) <small style="color:#929393">(v1.0)</small>
* [Stage Capabilities](/techniques/T1608) <small style="color:#929393">(v1.0)</small>
    * [Drive-by Target](/techniques/T1608/004) <small style="color:#929393">(v1.0)</small>
    * [Install Digital Certificate](/techniques/T1608/003) <small style="color:#929393">(v1.0)</small>
    * [Link Target](/techniques/T1608/005) <small style="color:#929393">(v1.0)</small>
    * [Upload Malware](/techniques/T1608/001) <small style="color:#929393">(v1.0)</small>
    * [Upload Tool](/techniques/T1608/002) <small style="color:#929393">(v1.0)</small>
* Subvert Trust Controls: [Code Signing Policy Modification](/techniques/T1553/006) <small style="color:#929393">(v1.0)</small>
* Subvert Trust Controls: [Mark-of-the-Web Bypass](/techniques/T1553/005) <small style="color:#929393">(v1.0)</small>
* [System Location Discovery](/techniques/T1614) <small style="color:#929393">(v1.0)</small>
* System Network Configuration Discovery: [Internet Connection Discovery](/techniques/T1016/001) <small style="color:#929393">(v1.0)</small>
* Unsecured Credentials: [Container API](/techniques/T1552/007) <small style="color:#929393">(v1.0)</small>
* User Execution: [Malicious Image](/techniques/T1204/003) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* Boot or Logon Initialization Scripts: [RC Scripts](/techniques/T1037/004) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* Command and Scripting Interpreter: [JavaScript](/techniques/T1059/007) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Domain Policy Modification](/techniques/T1484) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* Event Triggered Execution: [Unix Shell Configuration Modification](/techniques/T1546/004) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* Hijack Execution Flow: [DLL Side-Loading](/techniques/T1574/002) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* Hijack Execution Flow: [Dylib Hijacking](/techniques/T1574/004) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* Hijack Execution Flow: [Dynamic Linker Hijacking](/techniques/T1574/006) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Implant Internal Image](/techniques/T1525) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Modify Authentication Process](/techniques/T1556) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
    * [Domain Controller Authentication](/techniques/T1556/001) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
    * [Network Device Authentication](/techniques/T1556/004) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
    * [Password Filter DLL](/techniques/T1556/002) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
    * [Pluggable Authentication Modules](/techniques/T1556/003) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* Virtualization/Sandbox Evasion: [System Checks](/techniques/T1497/001) <small style="color:#929393">(v1.0&#8594;v2.0)</small>

#### Minor Version Changes

* [Account Discovery](/techniques/T1087) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
    * [Cloud Account](/techniques/T1087/004) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Email Account](/techniques/T1087/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Local Account](/techniques/T1087/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Account Manipulation](/techniques/T1098) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [BITS Jobs](/techniques/T1197) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Boot or Logon Autostart Execution: [Kernel Modules and Extensions](/techniques/T1547/006) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Boot or Logon Autostart Execution: [Shortcut Modification](/techniques/T1547/009) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Browser Extensions](/techniques/T1176) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Brute Force](/techniques/T1110) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
    * [Credential Stuffing](/techniques/T1110/004) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Password Guessing](/techniques/T1110/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Password Spraying](/techniques/T1110/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Cloud Infrastructure Discovery](/techniques/T1580) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Cloud Service Dashboard](/techniques/T1538) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Cloud Service Discovery](/techniques/T1526) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Command and Scripting Interpreter: [Windows Command Shell](/techniques/T1059/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Create Account](/techniques/T1136) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
    * [Cloud Account](/techniques/T1136/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Credentials from Password Stores: [Credentials from Web Browsers](/techniques/T1555/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Data Destruction](/techniques/T1485) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Data Encrypted for Impact](/techniques/T1486) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Data Staged](/techniques/T1074) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
    * [Remote Data Staging](/techniques/T1074/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Data from Cloud Storage Object](/techniques/T1530) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Data from Information Repositories](/techniques/T1213) <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* [Defacement](/techniques/T1491) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [External Defacement](/techniques/T1491/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Develop Capabilities: [Digital Certificates](/techniques/T1587/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Develop Capabilities: [Malware](/techniques/T1587/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Email Collection](/techniques/T1114) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
    * [Email Forwarding Rule](/techniques/T1114/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Remote Email Collection](/techniques/T1114/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Endpoint Denial of Service](/techniques/T1499) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Application Exhaustion Flood](/techniques/T1499/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Application or System Exploitation](/techniques/T1499/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Service Exhaustion Flood](/techniques/T1499/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Establish Accounts](/techniques/T1585) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Event Triggered Execution: [Windows Management Instrumentation Event Subscription](/techniques/T1546/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Exploit Public-Facing Application](/techniques/T1190) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* [Exploitation for Privilege Escalation](/techniques/T1068) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [External Remote Services](/techniques/T1133) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [Hijack Execution Flow](/techniques/T1574) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [DLL Search Order Hijacking](/techniques/T1574/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Impair Defenses](/techniques/T1562) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Disable Cloud Logs](/techniques/T1562/008) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Disable or Modify Cloud Firewall](/techniques/T1562/007) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Disable or Modify Tools](/techniques/T1562/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Indicator Removal on Host](/techniques/T1070) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Internal Spearphishing](/techniques/T1534) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Masquerading](/techniques/T1036) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
    * [Match Legitimate Name or Location](/techniques/T1036/005) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Modify Cloud Compute Infrastructure](/techniques/T1578) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Create Cloud Instance](/techniques/T1578/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Create Snapshot](/techniques/T1578/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Delete Cloud Instance](/techniques/T1578/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Revert Cloud Instance](/techniques/T1578/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Network Denial of Service](/techniques/T1498) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Direct Network Flood](/techniques/T1498/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Reflection Amplification](/techniques/T1498/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Network Service Scanning](/techniques/T1046) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [Network Sniffing](/techniques/T1040) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Obtain Capabilities: [Digital Certificates](/techniques/T1588/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Permission Groups Discovery](/techniques/T1069) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
    * [Cloud Groups](/techniques/T1069/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Phishing](/techniques/T1566) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
    * [Spearphishing Attachment](/techniques/T1566/001) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
    * [Spearphishing Link](/techniques/T1566/002) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Phishing for Information](/techniques/T1598) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Spearphishing Attachment](/techniques/T1598/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Spearphishing Link](/techniques/T1598/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Remote System Discovery](/techniques/T1018) <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* [Resource Hijacking](/techniques/T1496) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Scheduled Task/Job](/techniques/T1053) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Service Stop](/techniques/T1489) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Signed Binary Proxy Execution: [Msiexec](/techniques/T1218/007) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Software Discovery](/techniques/T1518) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
    * [Security Software Discovery](/techniques/T1518/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Steal Application Access Token](/techniques/T1528) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Steal Web Session Cookie](/techniques/T1539) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Steal or Forge Kerberos Tickets](/techniques/T1558) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Golden Ticket](/techniques/T1558/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [System Information Discovery](/techniques/T1082) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [System Network Connections Discovery](/techniques/T1049) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [System Time Discovery](/techniques/T1124) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Traffic Signaling](/techniques/T1205) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [Transfer Data to Cloud Account](/techniques/T1537) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Trusted Developer Utilities Proxy Execution: [MSBuild](/techniques/T1127/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Unsecured Credentials](/techniques/T1552) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Cloud Instance Metadata API](/techniques/T1552/005) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Credentials In Files](/techniques/T1552/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Unused/Unsupported Cloud Regions](/techniques/T1535) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Use Alternate Authentication Material](/techniques/T1550) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Application Access Token](/techniques/T1550/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Pass the Hash](/techniques/T1550/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Pass the Ticket](/techniques/T1550/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Web Session Cookie](/techniques/T1550/004) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [User Execution](/techniques/T1204) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Valid Accounts](/techniques/T1078) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
    * [Cloud Accounts](/techniques/T1078/004) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Default Accounts](/techniques/T1078/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Local Accounts](/techniques/T1078/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Virtualization/Sandbox Evasion: [Time Based Evasion](/techniques/T1497/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

#### Other Version Changes

* Account Manipulation: [Additional Cloud Credentials](/techniques/T1098/001) <small style="color:#eb6635">(v2.0&#8594;v2.2)</small>
* [Trusted Relationship](/techniques/T1199) <small style="color:#eb6635">(v2.0&#8594;v2.2)</small>

#### Metadata-only Changes

* [Access Token Manipulation](/techniques/T1134) <small style="color:#929393">(v2.0)</small>
    * [Parent PID Spoofing](/techniques/T1134/004) <small style="color:#929393">(v1.0)</small>
    * [SID-History Injection](/techniques/T1134/005) <small style="color:#929393">(v1.0)</small>
* [Acquire Infrastructure](/techniques/T1583) <small style="color:#929393">(v1.0)</small>
    * [Botnet](/techniques/T1583/005) <small style="color:#929393">(v1.0)</small>
    * [DNS Server](/techniques/T1583/002) <small style="color:#929393">(v1.0)</small>
    * [Domains](/techniques/T1583/001) <small style="color:#929393">(v1.0)</small>
    * [Server](/techniques/T1583/004) <small style="color:#929393">(v1.0)</small>
    * [Virtual Private Server](/techniques/T1583/003) <small style="color:#929393">(v1.0)</small>
    * [Web Services](/techniques/T1583/006) <small style="color:#929393">(v1.0)</small>
* [Active Scanning](/techniques/T1595) <small style="color:#929393">(v1.0)</small>
    * [Scanning IP Blocks](/techniques/T1595/001) <small style="color:#929393">(v1.0)</small>
    * [Vulnerability Scanning](/techniques/T1595/002) <small style="color:#929393">(v1.0)</small>
* [Automated Exfiltration](/techniques/T1020) <small style="color:#929393">(v1.2)</small>
* [Boot or Logon Autostart Execution](/techniques/T1547) <small style="color:#929393">(v1.1)</small>
    * [Plist Modification](/techniques/T1547/011) <small style="color:#929393">(v1.0)</small>
    * [Registry Run Keys / Startup Folder](/techniques/T1547/001) <small style="color:#929393">(v1.1)</small>
* [Boot or Logon Initialization Scripts](/techniques/T1037) <small style="color:#929393">(v2.1)</small>
* [Command and Scripting Interpreter](/techniques/T1059) <small style="color:#929393">(v2.1)</small>
* [Compromise Accounts](/techniques/T1586) <small style="color:#929393">(v1.0)</small>
    * [Email Accounts](/techniques/T1586/002) <small style="color:#929393">(v1.0)</small>
    * [Social Media Accounts](/techniques/T1586/001) <small style="color:#929393">(v1.0)</small>
* [Compromise Infrastructure](/techniques/T1584) <small style="color:#929393">(v1.0)</small>
    * [Botnet](/techniques/T1584/005) <small style="color:#929393">(v1.0)</small>
    * [DNS Server](/techniques/T1584/002) <small style="color:#929393">(v1.0)</small>
    * [Domains](/techniques/T1584/001) <small style="color:#929393">(v1.0)</small>
    * [Server](/techniques/T1584/004) <small style="color:#929393">(v1.0)</small>
    * [Virtual Private Server](/techniques/T1584/003) <small style="color:#929393">(v1.0)</small>
    * [Web Services](/techniques/T1584/006) <small style="color:#929393">(v1.0)</small>
* [Credentials from Password Stores](/techniques/T1555) <small style="color:#929393">(v1.0)</small>
* [Data Manipulation](/techniques/T1565) <small style="color:#929393">(v1.0)</small>
* [Develop Capabilities](/techniques/T1587) <small style="color:#929393">(v1.0)</small>
    * [Code Signing Certificates](/techniques/T1587/002) <small style="color:#929393">(v1.0)</small>
    * [Exploits](/techniques/T1587/004) <small style="color:#929393">(v1.0)</small>
* [Direct Volume Access](/techniques/T1006) <small style="color:#929393">(v2.0)</small>
* Dynamic Resolution: [Domain Generation Algorithms](/techniques/T1568/002) <small style="color:#929393">(v1.0)</small>
* [Encrypted Channel](/techniques/T1573) <small style="color:#929393">(v1.0)</small>
    * [Asymmetric Cryptography](/techniques/T1573/002) <small style="color:#929393">(v1.0)</small>
* Establish Accounts: [Email Accounts](/techniques/T1585/002) <small style="color:#929393">(v1.0)</small>
* Establish Accounts: [Social Media Accounts](/techniques/T1585/001) <small style="color:#929393">(v1.0)</small>
* [Event Triggered Execution](/techniques/T1546) <small style="color:#929393">(v1.1)</small>
    * [AppCert DLLs](/techniques/T1546/009) <small style="color:#929393">(v1.0)</small>
    * [AppInit DLLs](/techniques/T1546/010) <small style="color:#929393">(v1.0)</small>
    * [Application Shimming](/techniques/T1546/011) <small style="color:#929393">(v1.0)</small>
    * [Component Object Model Hijacking](/techniques/T1546/015) <small style="color:#929393">(v1.0)</small>
    * [Image File Execution Options Injection](/techniques/T1546/012) <small style="color:#929393">(v1.1)</small>
    * [LC_LOAD_DYLIB Addition](/techniques/T1546/006) <small style="color:#929393">(v1.0)</small>
* Execution Guardrails: [Environmental Keying](/techniques/T1480/001) <small style="color:#929393">(v1.0)</small>
* [Exploitation of Remote Services](/techniques/T1210) <small style="color:#929393">(v1.1)</small>
* [Gather Victim Host Information](/techniques/T1592) <small style="color:#929393">(v1.0)</small>
    * [Client Configurations](/techniques/T1592/004) <small style="color:#929393">(v1.0)</small>
    * [Firmware](/techniques/T1592/003) <small style="color:#929393">(v1.0)</small>
    * [Hardware](/techniques/T1592/001) <small style="color:#929393">(v1.0)</small>
    * [Software](/techniques/T1592/002) <small style="color:#929393">(v1.0)</small>
* [Gather Victim Identity Information](/techniques/T1589) <small style="color:#929393">(v1.0)</small>
    * [Credentials](/techniques/T1589/001) <small style="color:#929393">(v1.0)</small>
    * [Email Addresses](/techniques/T1589/002) <small style="color:#929393">(v1.0)</small>
    * [Employee Names](/techniques/T1589/003) <small style="color:#929393">(v1.0)</small>
* [Gather Victim Network Information](/techniques/T1590) <small style="color:#929393">(v1.0)</small>
    * [DNS](/techniques/T1590/002) <small style="color:#929393">(v1.0)</small>
    * [Domain Properties](/techniques/T1590/001) <small style="color:#929393">(v1.0)</small>
    * [IP Addresses](/techniques/T1590/005) <small style="color:#929393">(v1.0)</small>
    * [Network Security Appliances](/techniques/T1590/006) <small style="color:#929393">(v1.0)</small>
    * [Network Topology](/techniques/T1590/004) <small style="color:#929393">(v1.0)</small>
    * [Network Trust Dependencies](/techniques/T1590/003) <small style="color:#929393">(v1.0)</small>
* [Gather Victim Org Information](/techniques/T1591) <small style="color:#929393">(v1.0)</small>
    * [Business Relationships](/techniques/T1591/002) <small style="color:#929393">(v1.0)</small>
    * [Determine Physical Locations](/techniques/T1591/001) <small style="color:#929393">(v1.0)</small>
    * [Identify Business Tempo](/techniques/T1591/003) <small style="color:#929393">(v1.0)</small>
    * [Identify Roles](/techniques/T1591/004) <small style="color:#929393">(v1.0)</small>
* [Hardware Additions](/techniques/T1200) <small style="color:#929393">(v1.1)</small>
* Impair Defenses: [Impair Command History Logging](/techniques/T1562/003) <small style="color:#929393">(v2.0)</small>
* Impair Defenses: [Indicator Blocking](/techniques/T1562/006) <small style="color:#929393">(v1.0)</small>
* Indicator Removal on Host: [Network Share Connection Removal](/techniques/T1070/005) <small style="color:#929393">(v1.0)</small>
* Input Capture: [Credential API Hooking](/techniques/T1056/004) <small style="color:#929393">(v1.0)</small>
* [Man in the Browser](/techniques/T1185) <small style="color:#929393">(v1.0)</small>
* Man-in-the-Middle: [ARP Cache Poisoning](/techniques/T1557/002) <small style="color:#929393">(v1.0)</small>
* Masquerading: [Masquerade Task or Service](/techniques/T1036/004) <small style="color:#929393">(v1.0)</small>
* Masquerading: [Rename System Utilities](/techniques/T1036/003) <small style="color:#929393">(v1.0)</small>
* [Network Share Discovery](/techniques/T1135) <small style="color:#929393">(v3.0)</small>
* [OS Credential Dumping](/techniques/T1003) <small style="color:#929393">(v2.0)</small>
    * [DCSync](/techniques/T1003/006) <small style="color:#929393">(v1.0)</small>
    * [LSA Secrets](/techniques/T1003/004) <small style="color:#929393">(v1.0)</small>
    * [NTDS](/techniques/T1003/003) <small style="color:#929393">(v1.0)</small>
* [Obfuscated Files or Information](/techniques/T1027) <small style="color:#929393">(v1.1)</small>
* [Obtain Capabilities](/techniques/T1588) <small style="color:#929393">(v1.0)</small>
    * [Code Signing Certificates](/techniques/T1588/003) <small style="color:#929393">(v1.0)</small>
    * [Exploits](/techniques/T1588/005) <small style="color:#929393">(v1.0)</small>
    * [Malware](/techniques/T1588/001) <small style="color:#929393">(v1.0)</small>
    * [Tool](/techniques/T1588/002) <small style="color:#929393">(v1.0)</small>
    * [Vulnerabilities](/techniques/T1588/006) <small style="color:#929393">(v1.0)</small>
* Phishing for Information: [Spearphishing Service](/techniques/T1598/001) <small style="color:#929393">(v1.0)</small>
* [Process Injection](/techniques/T1055) <small style="color:#929393">(v1.1)</small>
    * [Asynchronous Procedure Call](/techniques/T1055/004) <small style="color:#929393">(v1.0)</small>
    * [Dynamic-link Library Injection](/techniques/T1055/001) <small style="color:#929393">(v1.0)</small>
    * [Extra Window Memory Injection](/techniques/T1055/011) <small style="color:#929393">(v1.0)</small>
    * [Portable Executable Injection](/techniques/T1055/002) <small style="color:#929393">(v1.0)</small>
    * [Process Doppelgänging](/techniques/T1055/013) <small style="color:#929393">(v1.0)</small>
    * [Process Hollowing](/techniques/T1055/012) <small style="color:#929393">(v1.0)</small>
    * [Thread Execution Hijacking](/techniques/T1055/003) <small style="color:#929393">(v1.0)</small>
    * [Thread Local Storage](/techniques/T1055/005) <small style="color:#929393">(v1.0)</small>
* [Rogue Domain Controller](/techniques/T1207) <small style="color:#929393">(v2.0)</small>
* Scheduled Task/Job: [Scheduled Task](/techniques/T1053/005) <small style="color:#929393">(v1.0)</small>
* [Search Closed Sources](/techniques/T1597) <small style="color:#929393">(v1.0)</small>
    * [Purchase Technical Data](/techniques/T1597/002) <small style="color:#929393">(v1.0)</small>
    * [Threat Intel Vendors](/techniques/T1597/001) <small style="color:#929393">(v1.0)</small>
* [Search Open Technical Databases](/techniques/T1596) <small style="color:#929393">(v1.0)</small>
    * [CDNs](/techniques/T1596/004) <small style="color:#929393">(v1.0)</small>
    * [DNS/Passive DNS](/techniques/T1596/001) <small style="color:#929393">(v1.0)</small>
    * [Digital Certificates](/techniques/T1596/003) <small style="color:#929393">(v1.0)</small>
    * [Scan Databases](/techniques/T1596/005) <small style="color:#929393">(v1.0)</small>
    * [WHOIS](/techniques/T1596/002) <small style="color:#929393">(v1.0)</small>
* [Search Open Websites/Domains](/techniques/T1593) <small style="color:#929393">(v1.0)</small>
    * [Search Engines](/techniques/T1593/002) <small style="color:#929393">(v1.0)</small>
    * [Social Media](/techniques/T1593/001) <small style="color:#929393">(v1.0)</small>
* [Search Victim-Owned Websites](/techniques/T1594) <small style="color:#929393">(v1.0)</small>
* [Signed Binary Proxy Execution](/techniques/T1218) <small style="color:#929393">(v2.1)</small>
    * [Mshta](/techniques/T1218/005) <small style="color:#929393">(v1.0)</small>
    * [Rundll32](/techniques/T1218/011) <small style="color:#929393">(v1.0)</small>
* [Software Deployment Tools](/techniques/T1072) <small style="color:#929393">(v2.1)</small>
* [Subvert Trust Controls](/techniques/T1553) <small style="color:#929393">(v1.0)</small>
    * [SIP and Trust Provider Hijacking](/techniques/T1553/003) <small style="color:#929393">(v1.0)</small>
* [Supply Chain Compromise](/techniques/T1195) <small style="color:#929393">(v1.2)</small>
* [System Network Configuration Discovery](/techniques/T1016) <small style="color:#929393">(v1.2)</small>
* [Trusted Developer Utilities Proxy Execution](/techniques/T1127) <small style="color:#929393">(v1.2)</small>
* [Virtualization/Sandbox Evasion](/techniques/T1497) <small style="color:#929393">(v1.2)</small>
* [XSL Script Processing](/techniques/T1220) <small style="color:#929393">(v1.2)</small>

#### Unknown Changes

* Command and Scripting Interpreter: [Visual Basic](/techniques/T1059/005) <small style="color:#eb6635">(v1.1&#8594;v1.1)</small>
* [File and Directory Permissions Modification](/techniques/T1222) <small style="color:#eb6635">(v2.1&#8594;v2.1)</small>
    * [Linux and Mac File and Directory Permissions Modification](/techniques/T1222/002) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* Process Injection: [Proc Memory](/techniques/T1055/009) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>

### Mobile

#### New Techniques

* [Command-Line Interface](/techniques/T1605) <small style="color:#929393">(v1.0)</small>
* [Proxy Through Victim](/techniques/T1604) <small style="color:#929393">(v1.0)</small>
* [Scheduled Task/Job](/techniques/T1603) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* [Device Administrator Permissions](/techniques/T1401) <small style="color:#929393">(v1.1&#8594;v2.0)</small>

#### Metadata-only Changes

* [Deliver Malicious App via Other Means](/techniques/T1476) <small style="color:#929393">(v1.2)</small>
* [Supply Chain Compromise](/techniques/T1474) <small style="color:#929393">(v1.1)</small>

### ICS

#### New Techniques

* [Exploitation for Privilege Escalation](/Technique/T0890) <small style="color:#eb6635">(v0.0)</small>
* [Loss of Protection](/Technique/T0837) <small style="color:#eb6635">(v0.0)</small>
* [Modify Controller Tasking](/Technique/T0821) <small style="color:#eb6635">(v0.0)</small>
* [Modify Program](/Technique/T0889) <small style="color:#eb6635">(v0.0)</small>
* [Native API](/Technique/T0834) <small style="color:#eb6635">(v0.0)</small>
* [Remote Services](/Technique/T0886) <small style="color:#eb6635">(v0.0)</small>
* [Remote System Information Discovery](/Technique/T0888) <small style="color:#eb6635">(v0.0)</small>
* [Wireless Sniffing](/Technique/T0887) <small style="color:#eb6635">(v0.0)</small>

#### Metadata-only Changes

* [Activate Firmware Update Mode](/Technique/T0800) <small style="color:#929393">(v0.0)</small>
* [Change Operating Mode](/Technique/T0858) <small style="color:#929393">(v0.0)</small>
* [Data from Information Repositories](/Technique/T0811) <small style="color:#929393">(v0.0)</small>
* [Denial of Control](/Technique/T813) <small style="color:#929393">(v0.0)</small>
* [Detect Operating Mode](/Technique/T0868) <small style="color:#929393">(v0.0)</small>
* [Engineering Workstation Compromise](/Technique/T0818) <small style="color:#929393">(v0.0)</small>
* [Exploitation of Remote Services](/Technique/T0866) <small style="color:#929393">(v0.0)</small>
* [Lateral Tool Transfer](/Technique/T0867) <small style="color:#929393">(v0.0)</small>
* [Man in the Middle](/Technique/T0830) <small style="color:#929393">(v0.0)</small>
* [Masquerading](/Technique/T0849) <small style="color:#929393">(v0.0)</small>
* [Program Download](/Technique/T0843) <small style="color:#929393">(v0.0)</small>
* [Rogue Master](/Technique/T0848) <small style="color:#929393">(v0.0)</small>
* [Service Stop](/Technique/T0881) <small style="color:#929393">(v0.0)</small>
* [Supply Chain Compromise](/Technique/T0862) <small style="color:#929393">(v0.0)</small>
* [Unauthorized Command Message](/Technique/T0855) <small style="color:#929393">(v0.0)</small>

#### Unknown Changes

* [Block Command Message](/Technique/T0803) <small style="color:#eb6635">(v0.0&#8594;v0.0)</small>
* [Block Reporting Message](/Technique/T0804) <small style="color:#eb6635">(v0.0&#8594;v0.0)</small>
* [Device Restart/Shutdown](/Technique/T0816) <small style="color:#eb6635">(v0.0&#8594;v0.0)</small>
* [Execution through API](/Technique/T0871) <small style="color:#eb6635">(v0.0&#8594;v0.0)</small>
* [Exploit Public-Facing Application](/Technique/T0819) <small style="color:#eb6635">(v0.0&#8594;v0.0)</small>
* [External Remote Services](/Technique/T0822) <small style="color:#eb6635">(v0.0&#8594;v0.0)</small>
* [Graphical User Interface](/Technique/T0823) <small style="color:#eb6635">(v0.0&#8594;v0.0)</small>
* [Internet Accessible Device](/Technique/T0883) <small style="color:#eb6635">(v0.0&#8594;v0.0)</small>
* [Loss of Control](/Technique/T0827) <small style="color:#eb6635">(v0.0&#8594;v0.0)</small>
* [Loss of Safety](/Technique/T0880) <small style="color:#eb6635">(v0.0&#8594;v0.0)</small>
* [Manipulation of Control](/Technique/T0831) <small style="color:#eb6635">(v0.0&#8594;v0.0)</small>
* [Remote System Discovery](/Technique/T0846) <small style="color:#eb6635">(v0.0&#8594;v0.0)</small>
* [System Firmware](/Technique/T0857) <small style="color:#eb6635">(v0.0&#8594;v0.0)</small>
* [Valid Accounts](/Technique/T0859) <small style="color:#eb6635">(v0.0&#8594;v0.0)</small>

#### Deprecations

* [Change Program State](/Technique/T875) <small style="color:#929393">(v0.0)</small>
* [Control Device Identification](/Technique/T808) <small style="color:#929393">(v0.0)</small>
* [Detect Program State](/Technique/T870) <small style="color:#929393">(v0.0)</small>
* [I/O Module Discovery](/Technique/T824) <small style="color:#929393">(v0.0)</small>
* [Location Identification](/Technique/T825) <small style="color:#929393">(v0.0)</small>
* [Modify Control Logic](/Technique/T0833) <small style="color:#929393">(v0.0)</small>
* [Network Service Scanning](/Technique/T841) <small style="color:#929393">(v0.0)</small>
* [Program Organization Units](/Technique/T844) <small style="color:#929393">(v0.0)</small>
* [Role Identification](/Technique/T850) <small style="color:#929393">(v0.0)</small>
* [Serial Connection Enumeration](/Technique/T854) <small style="color:#929393">(v0.0)</small>

## Software

### Enterprise

#### New Software

* [AdFind](/software/S0552) <small style="color:#929393">(v1.0)</small>
* [AppleJeus](/software/S0584) <small style="color:#929393">(v1.0)</small>
* [BLINDINGCAN](/software/S0520) <small style="color:#929393">(v1.0)</small>
* [Bazar](/software/S0534) <small style="color:#929393">(v1.0)</small>
* [BendyBear](/software/S0574) <small style="color:#929393">(v1.0)</small>
* [BitPaymer](/software/S0570) <small style="color:#929393">(v1.0)</small>
* [BlackMould](/software/S0564) <small style="color:#929393">(v1.0)</small>
* [BloodHound](/software/S0521) <small style="color:#929393">(v1.0)</small>
* [CSPY Downloader](/software/S0527) <small style="color:#929393">(v1.0)</small>
* [Caterpillar WebShell](/software/S0572) <small style="color:#929393">(v1.0)</small>
* [ConnectWise](/software/S0591) <small style="color:#929393">(v1.0)</small>
* [Conti](/software/S0575) <small style="color:#929393">(v1.0)</small>
* [Crutch](/software/S0538) <small style="color:#929393">(v1.0)</small>
* [Doki](/software/S0600) <small style="color:#929393">(v1.0)</small>
* [DropBook](/software/S0547) <small style="color:#929393">(v1.0)</small>
* [Dtrack](/software/S0567) <small style="color:#929393">(v1.0)</small>
* [ECCENTRICBANDWAGON](/software/S0593) <small style="color:#929393">(v1.0)</small>
* [EVILNUM](/software/S0568) <small style="color:#929393">(v1.0)</small>
* [Egregor](/software/S0554) <small style="color:#929393">(v1.0)</small>
* [Explosive](/software/S0569) <small style="color:#929393">(v1.0)</small>
* [GoldFinder](/software/S0597) <small style="color:#929393">(v1.0)</small>
* [GoldMax](/software/S0588) <small style="color:#929393">(v1.0)</small>
* [Grandoreiro](/software/S0531) <small style="color:#929393">(v1.0)</small>
* [GuLoader](/software/S0561) <small style="color:#929393">(v1.0)</small>
* [Hildegard](/software/S0601) <small style="color:#929393">(v1.0)</small>
* [HyperStack](/software/S0537) <small style="color:#929393">(v1.0)</small>
* [IronNetInjector](/software/S0581) <small style="color:#929393">(v1.0)</small>
* [Javali](/software/S0528) <small style="color:#929393">(v1.0)</small>
* [KGH_SPY](/software/S0526) <small style="color:#929393">(v1.0)</small>
* [Kerrdown](/software/S0585) <small style="color:#929393">(v1.0)</small>
* [Kinsing](/software/S0599) <small style="color:#929393">(v1.0)</small>
* [LookBack](/software/S0582) <small style="color:#929393">(v1.0)</small>
* [Lucifer](/software/S0532) <small style="color:#929393">(v1.0)</small>
* [MegaCortex](/software/S0576) <small style="color:#929393">(v1.0)</small>
* [Melcoz](/software/S0530) <small style="color:#929393">(v1.0)</small>
* [MoleNet](/software/S0553) <small style="color:#929393">(v1.0)</small>
* [NBTscan](/software/S0590) <small style="color:#929393">(v1.0)</small>
* [Out1](/software/S0594) <small style="color:#929393">(v1.0)</small>
* [P.A.S. Webshell](/software/S0598) <small style="color:#929393">(v1.0)</small>
* [Pay2Key](/software/S0556) <small style="color:#929393">(v1.0)</small>
* [Penquin](/software/S0587) <small style="color:#929393">(v1.0)</small>
* [Pysa](/software/S0583) <small style="color:#929393">(v1.0)</small>
* [Raindrop](/software/S0565) <small style="color:#eb6635">(v1.1)</small>
* [RemoteUtilities](/software/S0592) <small style="color:#929393">(v1.0)</small>
* [SLOTHFULMEDIA](/software/S0533) <small style="color:#929393">(v1.0)</small>
* [SUNBURST](/software/S0559) <small style="color:#eb6635">(v2.0)</small>
* [SUNSPOT](/software/S0562) <small style="color:#eb6635">(v1.1)</small>
* [SUPERNOVA](/software/S0578) <small style="color:#929393">(v1.0)</small>
* [ShadowPad](/software/S0596) <small style="color:#929393">(v1.0)</small>
* [SharpStage](/software/S0546) <small style="color:#929393">(v1.0)</small>
* [Sibot](/software/S0589) <small style="color:#929393">(v1.0)</small>
* [Spark](/software/S0543) <small style="color:#929393">(v1.0)</small>
* [TAINTEDSCRIBE](/software/S0586) <small style="color:#929393">(v1.0)</small>
* [TEARDROP](/software/S0560) <small style="color:#eb6635">(v1.1)</small>
* [ThiefQuest](/software/S0595) <small style="color:#929393">(v1.0)</small>
* [Waterbear](/software/S0579) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* [Astaroth](/software/S0373) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* [Machete](/software/S0409) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* [Matryoshka](/software/S0167) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [More_eggs](/software/S0284) <small style="color:#929393">(v2.1&#8594;v3.0)</small>
* [NotPetya](/software/S0368) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* [OSX_OCEANLOTUS.D](/software/S0352) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* [Olympic Destroyer](/software/S0365) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* [PoetRAT](/software/S0428) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [SDBbot](/software/S0461) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [SEASHARPEE](/software/S0185) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Zebrocy](/software/S0251) <small style="color:#929393">(v2.1&#8594;v3.0)</small>

#### Minor Version Changes

* [Agent Tesla](/software/S0331) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [BabyShark](/software/S0414) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [BlackEnergy](/software/S0089) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Carbon](/software/S0335) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [China Chopper](/software/S0020) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [Cobalt Strike](/software/S0154) <small style="color:#929393">(v1.5&#8594;v1.6)</small>
* [ComRAT](/software/S0126) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Ebury](/software/S0377) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Empire](/software/S0363) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [EvilBunny](/software/S0396) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Exaramel for Linux](/software/S0401) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [FALLCHILL](/software/S0181) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Fysbis](/software/S0410) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Gazer](/software/S0168) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [HTRAN](/software/S0040) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [HiddenWasp](/software/S0394) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Hikit](/software/S0009) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Kazuar](/software/S0265) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [LaZagne](/software/S0349) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Mimikatz](/software/S0002) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [NETWIRE](/software/S0198) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Net](/software/S0039) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [PoisonIvy](/software/S0012) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [PowerSploit](/software/S0194) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Proton](/software/S0279) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [REvil](/software/S0496) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [ROKRAT](/software/S0240) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [Ragnar Locker](/software/S0481) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Ramsay](/software/S0458) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Ryuk](/software/S0446) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [TrickBot](/software/S0266) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Ursnif](/software/S0386) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Valak](/software/S0476) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [gh0st RAT](/software/S0032) <small style="color:#929393">(v2.2&#8594;v2.3)</small>

#### Metadata-only Changes

* [BONDUPDATER](/software/S0360) <small style="color:#929393">(v1.2)</small>
* [BOOTRASH](/software/S0114) <small style="color:#929393">(v1.1)</small>
* [Briba](/software/S0204) <small style="color:#929393">(v1.0)</small>
* [Carbanak](/software/S0030) <small style="color:#929393">(v1.1)</small>
* [Catchamas](/software/S0261) <small style="color:#929393">(v1.1)</small>
* [DustySky](/software/S0062) <small style="color:#929393">(v1.1)</small>
* [Emotet](/software/S0367) <small style="color:#929393">(v1.3)</small>
* [HAMMERTOSS](/software/S0037) <small style="color:#929393">(v1.2)</small>
* [Hi-Zor](/software/S0087) <small style="color:#929393">(v1.1)</small>
* [Hydraq](/software/S0203) <small style="color:#929393">(v1.1)</small>
* [KeyBoy](/software/S0387) <small style="color:#929393">(v1.2)</small>
* [Linfo](/software/S0211) <small style="color:#929393">(v1.1)</small>
* [Linux Rabbit](/software/S0362) <small style="color:#929393">(v1.2)</small>
* [Naid](/software/S0205) <small style="color:#929393">(v1.0)</small>
* [Nerex](/software/S0210) <small style="color:#929393">(v1.0)</small>
* [Net Crawler](/software/S0056) <small style="color:#929393">(v1.1)</small>
* [Orz](/software/S0229) <small style="color:#929393">(v2.1)</small>
* [PUNCHBUGGY](/software/S0196) <small style="color:#929393">(v2.1)</small>
* [Pasam](/software/S0208) <small style="color:#929393">(v1.1)</small>
* [PoshC2](/software/S0378) <small style="color:#929393">(v1.2)</small>
* [PowerStallion](/software/S0393) <small style="color:#929393">(v1.1)</small>
* [ROCKBOOT](/software/S0112) <small style="color:#929393">(v1.1)</small>
* [Reaver](/software/S0172) <small style="color:#929393">(v1.1)</small>
* [SeaDuke](/software/S0053) <small style="color:#929393">(v1.1)</small>
* [Shamoon](/software/S0140) <small style="color:#929393">(v2.1)</small>
* [TURNEDUP](/software/S0199) <small style="color:#929393">(v1.1)</small>
* [TinyZBot](/software/S0004) <small style="color:#929393">(v1.1)</small>
* [Vasport](/software/S0207) <small style="color:#929393">(v1.1)</small>
* [WellMess](/software/S0514) <small style="color:#929393">(v1.0)</small>
* [Wiarp](/software/S0206) <small style="color:#929393">(v1.1)</small>
* [jRAT](/software/S0283) <small style="color:#929393">(v2.1)</small>
* [meek](/software/S0175) <small style="color:#929393">(v1.0)</small>
* [spwebmember](/software/S0227) <small style="color:#929393">(v1.1)</small>

#### Unknown Changes

* [Get2](/software/S0460) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>

### Mobile

#### New Software

* [Android/AdDisplay.Ashas](/software/S0525) <small style="color:#929393">(v1.0)</small>
* [AndroidOS/MalLocker.B](/software/S0524) <small style="color:#929393">(v1.0)</small>
* [Asacub](/software/S0540) <small style="color:#929393">(v1.0)</small>
* [CHEMISTGAMES](/software/S0555) <small style="color:#929393">(v1.0)</small>
* [CarbonSteal](/software/S0529) <small style="color:#929393">(v1.0)</small>
* [Circles](/software/S0602) <small style="color:#929393">(v1.0)</small>
* [DoubleAgent](/software/S0550) <small style="color:#929393">(v1.0)</small>
* [Exobot](/software/S0522) <small style="color:#929393">(v1.0)</small>
* [FrozenCell](/software/S0577) <small style="color:#929393">(v1.0)</small>
* [GPlayed](/software/S0536) <small style="color:#929393">(v1.0)</small>
* [Golden Cup](/software/S0535) <small style="color:#929393">(v1.0)</small>
* [GoldenEagle](/software/S0551) <small style="color:#929393">(v1.0)</small>
* [HenBox](/software/S0544) <small style="color:#929393">(v1.0)</small>
* [Red Alert 2.0](/software/S0539) <small style="color:#929393">(v1.0)</small>
* [SilkBean](/software/S0549) <small style="color:#929393">(v1.0)</small>
* [TERRACOTTA](/software/S0545) <small style="color:#929393">(v1.0)</small>
* [Tiktok Pro](/software/S0558) <small style="color:#929393">(v1.0)</small>

#### Minor Version Changes

* [Anubis](/software/S0422) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Desert Scorpion](/software/S0505) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

### ICS

#### New Software

* [BlackEnergy](/software/S0089) <small style="color:#eb6635">(v1.3)</small>
* [EKANS](/Software/S0017) <small style="color:#929393">(v1.0)</small>
* [REvil](/software/S0496) <small style="color:#eb6635">(v1.1)</small>

#### Major Version Changes

* [NotPetya](/software/S0368) <small style="color:#929393">(v1.2&#8594;v2.0)</small>

#### Minor Version Changes

* [Ryuk](/software/S0446) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

#### Deletions

* BlackEnergy 3 <small style="color:#eb6635">(v1.0)</small>

## Groups

### Enterprise

#### New Groups

* [Ajax Security Team](/groups/G0130) <small style="color:#929393">(v1.0)</small>
* [Evilnum](/groups/G0120) <small style="color:#929393">(v1.0)</small>
* [Fox Kitten](/groups/G0117) <small style="color:#929393">(v1.0)</small>
* [HAFNIUM](/groups/G0125) <small style="color:#929393">(v1.0)</small>
* [Higaisa](/groups/G0126) <small style="color:#929393">(v1.0)</small>
* [Indrik Spider](/groups/G0119) <small style="color:#929393">(v1.0)</small>
* [Mustang Panda](/groups/G0129) <small style="color:#929393">(v1.0)</small>
* [Operation Wocao](/groups/G0116) <small style="color:#929393">(v1.0)</small>
* [Sidewinder](/groups/G0121) <small style="color:#929393">(v1.0)</small>
* [Silent Librarian](/groups/G0122) <small style="color:#929393">(v1.0)</small>
* [TA551](/groups/G0127) <small style="color:#929393">(v1.0)</small>
* [UNC2452](/groups/G0118) <small style="color:#eb6635">(v0.0)</small>
* [Volatile Cedar](/groups/G0123) <small style="color:#929393">(v1.0)</small>
* [Windigo](/groups/G0124) <small style="color:#929393">(v1.0)</small>
* [ZIRCONIUM](/groups/G0128) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* [APT29](/groups/G0016) <small style="color:#929393">(v1.4&#8594;v2.0)</small>
* [APT39](/groups/G0087) <small style="color:#929393">(v2.3&#8594;v3.0)</small>
* [APT41](/groups/G0096) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Chimera](/groups/G0114) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Darkhotel](/groups/G0012) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* [Dragonfly 2.0](/groups/G0074) <small style="color:#929393">(v1.3&#8594;v2.0)</small>
* [GALLIUM](/groups/G0093) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Kimsuky](/groups/G0094) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Machete](/groups/G0095) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* [Magic Hound](/groups/G0059) <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* [Molerats](/groups/G0021) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [MuddyWater](/groups/G0069) <small style="color:#929393">(v2.3&#8594;v3.0)</small>
* [OilRig](/groups/G0049) <small style="color:#929393">(v1.4&#8594;v2.0)</small>
* [Sandworm Team](/groups/G0034) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Silence](/groups/G0091) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Turla](/groups/G0010) <small style="color:#929393">(v1.4&#8594;v2.0)</small>
* [menuPass](/groups/G0045) <small style="color:#929393">(v1.5&#8594;v2.0)</small>

#### Minor Version Changes

* [APT28](/groups/G0007) <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* [APT32](/groups/G0050) <small style="color:#929393">(v2.3&#8594;v2.4)</small>
* [BRONZE BUTLER](/groups/G0060) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [BlackTech](/groups/G0098) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Carbanak](/groups/G0008) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Cobalt Group](/groups/G0080) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [CopyKittens](/groups/G0052) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Elderwood](/groups/G0066) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [FIN6](/groups/G0037) <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* [GOLD SOUTHFIELD](/groups/G0115) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Lazarus Group](/groups/G0032) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [PLATINUM](/groups/G0068) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Stealth Falcon](/groups/G0038) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [TA505](/groups/G0092) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Threat Group-3390](/groups/G0027) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Tropic Trooper](/groups/G0081) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Windshift](/groups/G0112) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Wizard Spider](/groups/G0102) <small style="color:#929393">(v1.2&#8594;v1.3)</small>

#### Metadata-only Changes

* [APT19](/groups/G0073) <small style="color:#929393">(v1.3)</small>
* [APT3](/groups/G0022) <small style="color:#929393">(v1.3)</small>
* [Cleaver](/groups/G0003) <small style="color:#929393">(v1.2)</small>
* [DarkHydrus](/groups/G0079) <small style="color:#929393">(v1.2)</small>
* [Deep Panda](/groups/G0009) <small style="color:#929393">(v1.2)</small>
* [Dragonfly](/groups/G0035) <small style="color:#929393">(v2.0)</small>
* [FIN8](/groups/G0061) <small style="color:#929393">(v1.1)</small>
* [Gamaredon Group](/groups/G0047) <small style="color:#929393">(v1.2)</small>
* [Gorgon Group](/groups/G0078) <small style="color:#929393">(v1.4)</small>
* [Ke3chang](/groups/G0004) <small style="color:#929393">(v1.3)</small>
* [TEMP.Veles](/groups/G0088) <small style="color:#929393">(v1.2)</small>

#### Deletions

* Charming Kitten <small style="color:#eb6635">(v1.0)</small>

### Mobile

#### New Groups

* [Sandworm Team](/groups/G0034) <small style="color:#eb6635">(v2.0)</small>
* [Windshift](/groups/G0112) <small style="color:#eb6635">(v1.1)</small>

#### Minor Version Changes

* [APT28](/groups/G0007) <small style="color:#929393">(v3.0&#8594;v3.1)</small>

### ICS

#### Major Version Changes

* [OilRig](/groups/G0049) <small style="color:#929393">(v1.4&#8594;v2.0)</small>
* [Sandworm Team](/groups/G0034) <small style="color:#929393">(v1.0&#8594;v2.0)</small>

#### Minor Version Changes

* [Lazarus Group](/groups/G0032) <small style="color:#929393">(v1.4&#8594;v1.5)</small>

#### Metadata-only Changes

* [Dragonfly](/groups/G0035) <small style="color:#929393">(v2.0)</small>
* [TEMP.Veles](/groups/G0088) <small style="color:#929393">(v1.2)</small>

#### Deletions

* Leafminer <small style="color:#eb6635">(v1.0)</small>

## Campaigns

### Enterprise

### Mobile

### ICS

## Mitigations

### Enterprise

#### Metadata-only Changes

* [Audit](/mitigations/M1047) <small style="color:#929393">(v1.1)</small>

#### Deletions

* Group Policy Modification Mitigation <small style="color:#eb6635">(v1.0)</small>

### Mobile

#### Metadata-only Changes

* [Application Vetting](/mitigations/M1005) <small style="color:#929393">(v1.0)</small>

### ICS

#### New Mitigations

* [Account Use Policies](/Mitigation/M0936) <small style="color:#929393">(v1.0)</small>
* [Active Directory Configuration](/Mitigation/M0915) <small style="color:#929393">(v1.0)</small>
* [Antivirus/Antimalware](/Mitigation/M0949) <small style="color:#929393">(v1.0)</small>
* [Application Developer Guidance](/Mitigation/M0913) <small style="color:#929393">(v1.0)</small>
* [Application Isolation and Sandboxing](/Mitigation/M0948) <small style="color:#929393">(v1.0)</small>
* [Audit](/Mitigation/M0947) <small style="color:#929393">(v1.0)</small>
* [Boot Integrity](/Mitigation/M0946) <small style="color:#929393">(v1.0)</small>
* [Code Signing](/Mitigation/M0945) <small style="color:#929393">(v1.0)</small>
* [Data Backup](/Mitigation/M0953) <small style="color:#929393">(v1.0)</small>
* [Disable or Remove Feature or Program](/Mitigation/M0942) <small style="color:#929393">(v1.0)</small>
* [Encrypt Sensitive Information](/Mitigation/M0941) <small style="color:#929393">(v1.0)</small>
* [Execution Prevention](/Mitigation/M0938) <small style="color:#929393">(v1.0)</small>
* [Exploit Protection](/Mitigation/M0950) <small style="color:#929393">(v1.0)</small>
* [Filter Network Traffic](/Mitigation/M0937) <small style="color:#eb6635">(v1.1)</small>
* [Limit Access to Resource Over Network](/Mitigation/M0935) <small style="color:#929393">(v1.0)</small>
* [Limit Hardware Installation](/Mitigation/M0934) <small style="color:#929393">(v1.0)</small>
* [Multi-factor Authentication](/Mitigation/M0932) <small style="color:#929393">(v1.0)</small>
* [Network Intrusion Prevention](/Mitigation/M0931) <small style="color:#929393">(v1.0)</small>
* [Network Segmentation](/Mitigation/M0928) <small style="color:#929393">(v1.0)</small>
* [Operating System Configuration](/Mitigation/M0928) <small style="color:#929393">(v1.0)</small>
* [Password Policies](/Mitigation/M0927) <small style="color:#929393">(v1.0)</small>
* [Privileged Account Management](/Mitigation/M0926) <small style="color:#929393">(v1.0)</small>
* [Restrict File and Directory Permissions](/Mitigation/M0922) <small style="color:#929393">(v1.0)</small>
* [Restrict Library Loading](/Mitigation/M0944) <small style="color:#929393">(v1.0)</small>
* [Restrict Registry Permissions](/Mitigation/M0924) <small style="color:#929393">(v1.0)</small>
* [Restrict Web-Based Content](/Mitigation/M0921) <small style="color:#929393">(v1.0)</small>
* [SSL/TLS Inspection](/Mitigation/M0920) <small style="color:#929393">(v1.0)</small>
* [Software Configuration](/Mitigation/M0954) <small style="color:#929393">(v1.0)</small>
* [Supply Chain Management](/Mitigation/M0817) <small style="color:#929393">(v1.0)</small>
* [Threat Intelligence Program](/Mitigation/M0919) <small style="color:#929393">(v1.0)</small>
* [Update Software](/Mitigation/M0951) <small style="color:#929393">(v1.0)</small>
* [User Account Management](/Mitigation/M0918) <small style="color:#929393">(v1.0)</small>
* [User Training](/Mitigation/M0917) <small style="color:#929393">(v1.0)</small>
* [Vulnerability Scanning](/Mitigation/M0916) <small style="color:#929393">(v1.0)</small>

#### Metadata-only Changes

* [Access Management](/Mitigation/M0801) <small style="color:#929393">(v1.0)</small>
* [Network Allowlists](/Mitigation/M0807) <small style="color:#929393">(v1.0)</small>
* [Redundancy of Service](/Mitigation/M0811) <small style="color:#929393">(v1.0)</small>
* [Software Process and Device Authentication](/Mitigation/M0813) <small style="color:#929393">(v1.0)</small>
* [Static Network Configuration](/Mitigation/M0814) <small style="color:#929393">(v1.0)</small>
* [Watchdog Timers](/Mitigation/M0815) <small style="color:#929393">(v1.0)</small>

#### Deletions

* Account Use Policies <small style="color:#eb6635">(v1.0)</small>
* Active Directory Configuration <small style="color:#eb6635">(v1.1)</small>
* Antivirus/Antimalware <small style="color:#eb6635">(v1.1)</small>
* Application Developer Guidance <small style="color:#eb6635">(v1.0)</small>
* Application Isolation and Sandboxing <small style="color:#eb6635">(v1.1)</small>
* Audit <small style="color:#eb6635">(v1.1)</small>
* Boot Integrity <small style="color:#eb6635">(v1.0)</small>
* Code Signing <small style="color:#eb6635">(v1.1)</small>
* Data Backup <small style="color:#eb6635">(v1.1)</small>
* Disable or Remove Feature or Program <small style="color:#eb6635">(v1.1)</small>
* Encrypt Sensitive Information <small style="color:#eb6635">(v1.0)</small>
* Execution Prevention <small style="color:#eb6635">(v1.1)</small>
* Exploit Protection <small style="color:#eb6635">(v1.1)</small>
* Filter Network Traffic <small style="color:#eb6635">(v1.1)</small>
* Limit Access to Resource Over Network <small style="color:#eb6635">(v1.0)</small>
* Limit Hardware Installation <small style="color:#eb6635">(v1.0)</small>
* Multi-factor Authentication <small style="color:#eb6635">(v1.0)</small>
* Network Intrusion Prevention <small style="color:#eb6635">(v1.0)</small>
* Network Segmentation <small style="color:#eb6635">(v1.1)</small>
* Operating System Configuration <small style="color:#eb6635">(v1.1)</small>
* Password Policies <small style="color:#eb6635">(v1.0)</small>
* Privileged Account Management <small style="color:#eb6635">(v1.1)</small>
* Restrict File and Directory Permissions <small style="color:#eb6635">(v1.1)</small>
* Restrict Library Loading <small style="color:#eb6635">(v1.0)</small>
* Restrict Registry Permissions <small style="color:#eb6635">(v1.0)</small>
* Restrict Web-Based Content <small style="color:#eb6635">(v1.0)</small>
* SSL/TLS Inspection <small style="color:#eb6635">(v1.0)</small>
* Software Configuration <small style="color:#eb6635">(v1.1)</small>
* Threat Intelligence Program <small style="color:#eb6635">(v1.0)</small>
* Update Software <small style="color:#eb6635">(v1.0)</small>
* User Account Management <small style="color:#eb6635">(v1.1)</small>
* User Training <small style="color:#eb6635">(v1.1)</small>
* Vulnerability Scanning <small style="color:#eb6635">(v1.1)</small>

## Data Sources

### Enterprise

### Mobile

### ICS

## Data Components

### Enterprise

### Mobile

### ICS

## Contributors to this release

* Abel Morales, Exabeam
* Alex Soler, AttackIQ
* Alexandros Pappas
* Alfredo Oliveira, Trend Micro
* Anastasios Pingios
* Antonio Villani, @LDO_CyberSec, Leonardo's Cyber Security Division
* Ariel Shuper, Cisco
* Assaf Morag, @MoragAssaf, Team Nautilus Aqua Security
* Bencherchali Nasreddine, @nas_bench, ELIT Security Team (DSSD)
* Bernaldo Penas Antelo
* Blake Strom, Microsoft 365 Defender
* Bobby, Filar, Elastic
* Brad Geesaman, @bradgeesaman
* Brent Murphy, Elastic
* Carrie Roberts, @OrOneEqualsOne
* Center for Threat-Informed Defense (CTID)
* Chris Ross @xorrior
* Christiaan Beek, @ChristiaanBeek
* Cody Thomas, SpecterOps
* Cybereason Nocturnus, @nocturnus
* Daniel Stepanic, Elastic
* Daniyal Naeem, BT Security
* David Fiser, @anu4is, Trend Micro
* David French, Elastic
* Edward Millington
* Erik Schamper, @Schamperr, Fox-IT
* ExtraHop
* FIRST.ORG's Cyber Threat Intelligence SIG
* Gal Singer, @galsinger29, Team Nautilus Aqua Security
* Harry Kim, CODEMIZE
* Harry, CODEMIZE
* Harshal Tupsamudre, Qualys
* Hiroki Nagahama, NEC Corporation
* ICSCoE Japan
* Idan Frimark, Cisco
* Idan Revivo, @idanr86, Team Nautilus Aqua Security
* Itamar Mizrahi, Cymptom
* Jay Chen, Palo Alto Networks
* Joas Antonio dos Santos, @C0d3Cr4zy, Inmetrics
* Katie Nickels, Red Canary
* Kobi Haimovich, CardinalOps
* Kyaw Pyiyt Htet, @KyawPyiytHtet
* Lacework Labs
* Lorin Wu, Trend Micro
* Maarten van Dantzig, @MaartenVDantzig, Fox-IT
* Magno Logan, @magnologan, Trend Micro
* Manikantan Srinivasan, NEC Corporation India
* Martin Sohn Christensen, Improsec
* Matt Brenton, Zurich Insurance Group
* Matt Burrough, @mattburrough, Microsoft
* Mayuresh Dani, Qualys
* Michael Katchinskiy, @michael64194968, Team Nautilus Aqua Security
* Mugdha Peter Bansode
* Nathaniel Quist, Palo Alto Networks
* Nino Verde, @LDO_CyberSec, Leonardo's Cyber Security Division
* Oleg Kolesnikov, Securonix
* Pawan Kinger, @kingerpawan, Trend Micro
* Philip Winther
* Pooja Natarajan, NEC Corporation India
* Prasad Somasamudram, McAfee
* Robert Wilson
* Roi Kol, @roykol1, Team Nautilus Aqua Security
* Rory McCune, Aqua Security
* Ryo Tamura, SecureBrain Corporation
* Sekhar Sarukkai, McAfee 
* Shotaro Hamamoto, NEC Solution Innovators, Ltd
* Shuhei Sasada, Cyber Defense Institute, Inc
* Silvio La Porta, @LDO_CyberSec, Leonardo's Cyber Security Division
* Syed Ummar Farooqh, McAfee
* Takuma Matsumoto, LAC Co., Ltd
* The DFIR Report, @TheDFIRReport
* Thijn Bukkems, Amazon
* Tony Lambert, Red Canary
* Tristan Bennett, Seamless Intelligence
* Varonis Threat Labs
* Vishwas Manral, McAfee
* Wayne Silva, F-Secure Countercept
* Wes Hurd
* Yaniv Agman, @AgmanYaniv, Team Nautilus Aqua Security
* Yossi Weizman, Azure Defender Research Team
* Yusuke Niwa, ITOCHU Corporation
* Yuval Avrahami, Palo Alto Networks
* Ziv Karliner, @ziv_kr, Team Nautilus Aqua Security
