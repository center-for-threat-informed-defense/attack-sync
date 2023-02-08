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

* Boot or Logon Autostart Execution: [Login Items](/techniques/T1547/015) <small style="color:#929393">(v1.0)</small>
* [Cloud Storage Object Discovery](/techniques/T1619) <small style="color:#929393">(v1.0)</small>
* Data from Information Repositories: [Code Repositories](/techniques/T1213/003) <small style="color:#929393">(v1.0)</small>
* [Group Policy Discovery](/techniques/T1615) <small style="color:#929393">(v1.0)</small>
* Hide Artifacts: [Email Hiding Rules](/techniques/T1564/008) <small style="color:#929393">(v1.0)</small>
* Hide Artifacts: [Resource Forking](/techniques/T1564/009) <small style="color:#929393">(v1.0)</small>
* Impair Defenses: [Downgrade Attack](/techniques/T1562/010) <small style="color:#929393">(v1.0)</small>
* Impair Defenses: [Safe Mode Boot](/techniques/T1562/009) <small style="color:#929393">(v1.0)</small>
* Masquerading: [Double File Extension](/techniques/T1036/007) <small style="color:#929393">(v1.0)</small>
* Obfuscated Files or Information: [HTML Smuggling](/techniques/T1027/006) <small style="color:#929393">(v1.0)</small>
* [Reflective Code Loading](/techniques/T1620) <small style="color:#929393">(v1.0)</small>
* Server Software Component: [IIS Components](/techniques/T1505/004) <small style="color:#929393">(v1.0)</small>
* Signed Binary Proxy Execution: [MMC](/techniques/T1218/014) <small style="color:#929393">(v1.0)</small>
* Signed Binary Proxy Execution: [Mavinject](/techniques/T1218/013) <small style="color:#929393">(v1.0)</small>
* System Location Discovery: [System Language Discovery](/techniques/T1614/001) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* [Adversary-in-the-Middle](/techniques/T1557) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Browser Session Hijacking](/techniques/T1185) <small style="color:#929393">(v1.0&#8594;v2.0)</small>

#### Minor Version Changes

* Access Token Manipulation: [Create Process with Token](/techniques/T1134/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Account Discovery: [Local Account](/techniques/T1087/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Account Manipulation: [Exchange Email Delegate Permissions](/techniques/T1098/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Acquire Infrastructure](/techniques/T1583) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Domains](/techniques/T1583/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Server](/techniques/T1583/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Virtual Private Server](/techniques/T1583/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Web Services](/techniques/T1583/006) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Adversary-in-the-Middle: [ARP Cache Poisoning](/techniques/T1557/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Automated Exfiltration: [Traffic Duplication](/techniques/T1020/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Boot or Logon Autostart Execution: [Kernel Modules and Extensions](/techniques/T1547/006) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Boot or Logon Autostart Execution: [Plist Modification](/techniques/T1547/011) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Brute Force](/techniques/T1110) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* [Build Image on Host](/techniques/T1612) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Cloud Infrastructure Discovery](/techniques/T1580) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Command and Scripting Interpreter](/techniques/T1059) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
    * [JavaScript](/techniques/T1059/007) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
    * [Network Device CLI](/techniques/T1059/008) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [PowerShell](/techniques/T1059/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Unix Shell](/techniques/T1059/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Visual Basic](/techniques/T1059/005) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Windows Command Shell](/techniques/T1059/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Compromise Accounts](/techniques/T1586) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Social Media Accounts](/techniques/T1586/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Compromise Infrastructure](/techniques/T1584) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [DNS Server](/techniques/T1584/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Domains](/techniques/T1584/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Server](/techniques/T1584/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Virtual Private Server](/techniques/T1584/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Web Services](/techniques/T1584/006) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Create Account: [Local Account](/techniques/T1136/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Create or Modify System Process: [Launch Daemon](/techniques/T1543/004) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Data Encrypted for Impact](/techniques/T1486) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Data from Information Repositories](/techniques/T1213) <small style="color:#929393">(v3.1&#8594;v3.2)</small>
* [Data from Local System](/techniques/T1005) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Data from Removable Media](/techniques/T1025) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Develop Capabilities](/techniques/T1587) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Code Signing Certificates](/techniques/T1587/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Digital Certificates](/techniques/T1587/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Malware](/techniques/T1587/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Drive-by Compromise](/techniques/T1189) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Email Collection](/techniques/T1114) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
    * [Email Forwarding Rule](/techniques/T1114/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Escape to Host](/techniques/T1611) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Establish Accounts](/techniques/T1585) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Social Media Accounts](/techniques/T1585/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Event Triggered Execution: [Unix Shell Configuration Modification](/techniques/T1546/004) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Event Triggered Execution: [Windows Management Instrumentation Event Subscription](/techniques/T1546/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Exfiltration Over Alternative Protocol](/techniques/T1048) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
    * [Exfiltration Over Asymmetric Encrypted Non-C2 Protocol](/techniques/T1048/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Exfiltration Over Unencrypted/Obfuscated Non-C2 Protocol](/techniques/T1048/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Exfiltration Over C2 Channel](/techniques/T1041) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Exfiltration Over Physical Medium](/techniques/T1052) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Exfiltration over USB](/techniques/T1052/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Exfiltration Over Web Service](/techniques/T1567) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Exploitation for Client Execution](/techniques/T1203) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [External Remote Services](/techniques/T1133) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* File and Directory Permissions Modification: [Linux and Mac File and Directory Permissions Modification](/techniques/T1222/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Forge Web Credentials](/techniques/T1606) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [SAML Tokens](/techniques/T1606/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Web Cookies](/techniques/T1606/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Gather Victim Host Information](/techniques/T1592) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Client Configurations](/techniques/T1592/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Hardware](/techniques/T1592/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Software](/techniques/T1592/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Gather Victim Org Information](/techniques/T1591) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Determine Physical Locations](/techniques/T1591/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Hardware Additions](/techniques/T1200) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Hide Artifacts](/techniques/T1564) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Hidden Users](/techniques/T1564/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Run Virtual Instance](/techniques/T1564/006) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [VBA Stomping](/techniques/T1564/007) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Hijack Execution Flow: [Services Registry Permissions Weakness](/techniques/T1574/011) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Impair Defenses](/techniques/T1562) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Disable Windows Event Logging](/techniques/T1562/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Disable or Modify Tools](/techniques/T1562/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Input Capture: [GUI Input Capture](/techniques/T1056/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Inter-Process Communication](/techniques/T1559) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Component Object Model](/techniques/T1559/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Dynamic Data Exchange](/techniques/T1559/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Lateral Tool Transfer](/techniques/T1570) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Masquerading: [Masquerade Task or Service](/techniques/T1036/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Masquerading: [Right-to-Left Override](/techniques/T1036/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Native API](/techniques/T1106) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Network Share Discovery](/techniques/T1135) <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* [OS Credential Dumping](/techniques/T1003) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
    * [LSASS Memory](/techniques/T1003/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Obfuscated Files or Information](/techniques/T1027) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Binary Padding](/techniques/T1027/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Software Packing](/techniques/T1027/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Steganography](/techniques/T1027/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Obtain Capabilities](/techniques/T1588) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Code Signing Certificates](/techniques/T1588/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Digital Certificates](/techniques/T1588/004) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Malware](/techniques/T1588/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Tool](/techniques/T1588/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Office Application Startup](/techniques/T1137) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
    * [Add-ins](/techniques/T1137/006) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Office Template Macros](/techniques/T1137/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Office Test](/techniques/T1137/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Outlook Forms](/techniques/T1137/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Outlook Home Page](/techniques/T1137/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Outlook Rules](/techniques/T1137/005) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Password Policy Discovery](/techniques/T1201) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Permission Groups Discovery](/techniques/T1069) <small style="color:#929393">(v2.3&#8594;v2.4)</small>
    * [Cloud Groups](/techniques/T1069/003) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Phishing](/techniques/T1566) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
    * [Spearphishing Attachment](/techniques/T1566/001) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [Process Injection](/techniques/T1055) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Asynchronous Procedure Call](/techniques/T1055/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Dynamic-link Library Injection](/techniques/T1055/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Portable Executable Injection](/techniques/T1055/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Process Hollowing](/techniques/T1055/012) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Ptrace System Calls](/techniques/T1055/008) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Thread Execution Hijacking](/techniques/T1055/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Thread Local Storage](/techniques/T1055/005) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Remote Services](/techniques/T1021) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Distributed Component Object Model](/techniques/T1021/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [SSH](/techniques/T1021/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [VNC](/techniques/T1021/005) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Windows Remote Management](/techniques/T1021/006) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Remote System Discovery](/techniques/T1018) <small style="color:#929393">(v3.1&#8594;v3.2)</small>
* [Replication Through Removable Media](/techniques/T1091) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Scheduled Task/Job: [At (Linux)](/techniques/T1053/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Scheduled Task/Job: [Container Orchestration Job](/techniques/T1053/007) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Scheduled Task/Job: [Cron](/techniques/T1053/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Scheduled Task/Job: [Systemd Timers](/techniques/T1053/006) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Server Software Component](/techniques/T1505) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Web Shell](/techniques/T1505/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Shared Modules](/techniques/T1129) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Signed Binary Proxy Execution: [Mshta](/techniques/T1218/005) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Signed Binary Proxy Execution: [Rundll32](/techniques/T1218/011) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Signed Script Proxy Execution: [PubPrn](/techniques/T1216/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Stage Capabilities](/techniques/T1608) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Drive-by Target](/techniques/T1608/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Install Digital Certificate](/techniques/T1608/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Link Target](/techniques/T1608/005) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Upload Malware](/techniques/T1608/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Upload Tool](/techniques/T1608/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Steal Web Session Cookie](/techniques/T1539) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Steal or Forge Kerberos Tickets](/techniques/T1558) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Subvert Trust Controls](/techniques/T1553) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Gatekeeper Bypass](/techniques/T1553/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Install Root Certificate](/techniques/T1553/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [System Information Discovery](/techniques/T1082) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* [System Network Configuration Discovery](/techniques/T1016) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [System Owner/User Discovery](/techniques/T1033) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [System Service Discovery](/techniques/T1007) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [System Services](/techniques/T1569) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Launchctl](/techniques/T1569/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Service Execution](/techniques/T1569/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Taint Shared Content](/techniques/T1080) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Trusted Developer Utilities Proxy Execution: [MSBuild](/techniques/T1127/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Use Alternate Authentication Material](/techniques/T1550) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Web Session Cookie](/techniques/T1550/004) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [User Execution](/techniques/T1204) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
    * [Malicious File](/techniques/T1204/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Malicious Image](/techniques/T1204/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Valid Accounts](/techniques/T1078) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
    * [Cloud Accounts](/techniques/T1078/004) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
    * [Domain Accounts](/techniques/T1078/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Local Accounts](/techniques/T1078/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Virtualization/Sandbox Evasion](/techniques/T1497) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
    * [System Checks](/techniques/T1497/001) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
    * [Time Based Evasion](/techniques/T1497/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [User Activity Based Checks](/techniques/T1497/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Windows Management Instrumentation](/techniques/T1047) <small style="color:#929393">(v1.1&#8594;v1.2)</small>

#### Other Version Changes

* Adversary-in-the-Middle: [LLMNR/NBT-NS Poisoning and SMB Relay](/techniques/T1557/001) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
* Create or Modify System Process: [Launch Agent](/techniques/T1543/001) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>

#### Metadata-only Changes

* [Access Token Manipulation](/techniques/T1134) <small style="color:#929393">(v2.0)</small>
* [Account Discovery](/techniques/T1087) <small style="color:#929393">(v2.3)</small>
    * [Domain Account](/techniques/T1087/002) <small style="color:#929393">(v1.0)</small>
* [Account Manipulation](/techniques/T1098) <small style="color:#929393">(v2.2)</small>
* [Automated Exfiltration](/techniques/T1020) <small style="color:#929393">(v1.2)</small>
* [Boot or Logon Autostart Execution](/techniques/T1547) <small style="color:#929393">(v1.1)</small>
* Command and Scripting Interpreter: [Python](/techniques/T1059/006) <small style="color:#929393">(v1.0)</small>
* [Compromise Client Software Binary](/techniques/T1554) <small style="color:#929393">(v1.0)</small>
* [Create Account](/techniques/T1136) <small style="color:#929393">(v2.2)</small>
* [Create or Modify System Process](/techniques/T1543) <small style="color:#929393">(v1.0)</small>
* [Credentials from Password Stores](/techniques/T1555) <small style="color:#929393">(v1.0)</small>
    * [Password Managers](/techniques/T1555/005) <small style="color:#929393">(v1.0)</small>
* Data from Information Repositories: [Confluence](/techniques/T1213/001) <small style="color:#929393">(v1.0)</small>
* Data from Information Repositories: [Sharepoint](/techniques/T1213/002) <small style="color:#929393">(v1.0)</small>
* [Event Triggered Execution](/techniques/T1546) <small style="color:#929393">(v1.1)</small>
* [Execution Guardrails](/techniques/T1480) <small style="color:#929393">(v1.1)</small>
    * [Environmental Keying](/techniques/T1480/001) <small style="color:#929393">(v1.0)</small>
* [Exploit Public-Facing Application](/techniques/T1190) <small style="color:#929393">(v2.3)</small>
* [File and Directory Discovery](/techniques/T1083) <small style="color:#929393">(v1.3)</small>
* [File and Directory Permissions Modification](/techniques/T1222) <small style="color:#929393">(v2.1)</small>
* [Hijack Execution Flow](/techniques/T1574) <small style="color:#929393">(v1.1)</small>
    * [COR_PROFILER](/techniques/T1574/012) <small style="color:#929393">(v1.0)</small>
* [Indicator Removal on Host](/techniques/T1070) <small style="color:#929393">(v1.2)</small>
* [Input Capture](/techniques/T1056) <small style="color:#929393">(v1.2)</small>
* [Masquerading](/techniques/T1036) <small style="color:#929393">(v1.4)</small>
* [Modify Authentication Process](/techniques/T1556) <small style="color:#929393">(v2.0)</small>
    * [Pluggable Authentication Modules](/techniques/T1556/003) <small style="color:#929393">(v2.0)</small>
* [Proxy](/techniques/T1090) <small style="color:#929393">(v3.1)</small>
* [Scheduled Task/Job](/techniques/T1053) <small style="color:#929393">(v2.1)</small>
* Server Software Component: [Transport Agent](/techniques/T1505/002) <small style="color:#929393">(v1.0)</small>
* [Signed Binary Proxy Execution](/techniques/T1218) <small style="color:#929393">(v2.1)</small>
    * [Msiexec](/techniques/T1218/007) <small style="color:#929393">(v1.1)</small>
* [Signed Script Proxy Execution](/techniques/T1216) <small style="color:#929393">(v1.1)</small>
* Steal or Forge Kerberos Tickets: [AS-REP Roasting](/techniques/T1558/004) <small style="color:#929393">(v1.0)</small>
* [System Location Discovery](/techniques/T1614) <small style="color:#929393">(v1.0)</small>
* [Trusted Developer Utilities Proxy Execution](/techniques/T1127) <small style="color:#929393">(v1.2)</small>
* Use Alternate Authentication Material: [Application Access Token](/techniques/T1550/001) <small style="color:#929393">(v1.2)</small>
* Use Alternate Authentication Material: [Pass the Hash](/techniques/T1550/002) <small style="color:#929393">(v1.1)</small>
* Use Alternate Authentication Material: [Pass the Ticket](/techniques/T1550/003) <small style="color:#929393">(v1.1)</small>

#### Deprecations

* Scheduled Task/Job: [Launchd](/techniques/T1053/004) <small style="color:#929393">(v1.0)</small>

### Mobile

#### New Techniques

* [Call Control](/techniques/T1616) <small style="color:#929393">(v1.0)</small>
* [Hooking](/techniques/T1617) <small style="color:#929393">(v1.0)</small>
* [User Evasion](/techniques/T1618) <small style="color:#929393">(v1.0)</small>

#### Minor Version Changes

* [Exploit SS7 to Redirect Phone Calls/SMS](/techniques/T1449) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Manipulate Device Communication](/techniques/T1463) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [SIM Card Swap](/techniques/T1451) <small style="color:#929393">(v1.1&#8594;v1.2)</small>

### ICS

#### New Techniques

* [Transient Cyber Asset](/Technique/T0864) <small style="color:#eb6635">(v0.0)</small>

#### Metadata-only Changes

* [Activate Firmware Update Mode](/Technique/T0800) <small style="color:#929393">(v0.0)</small>
* [Alarm Suppression](/Technique/T0878) <small style="color:#929393">(v0.0)</small>
* [Automated Collection](/Technique/T0802) <small style="color:#929393">(v0.0)</small>
* [Block Command Message](/Technique/T0803) <small style="color:#929393">(v0.0)</small>
* [Block Reporting Message](/Technique/T0804) <small style="color:#929393">(v0.0)</small>
* [Block Serial COM](/Technique/T0805) <small style="color:#929393">(v0.0)</small>
* [Brute Force I/O](/Technique/T0806) <small style="color:#929393">(v0.0)</small>
* [Change Operating Mode](/Technique/T0858) <small style="color:#929393">(v0.0)</small>
* [Command-Line Interface](/Technique/T0807) <small style="color:#929393">(v0.0)</small>
* [Commonly Used Port](/Technique/T0885) <small style="color:#929393">(v0.0)</small>
* [Connection Proxy](/Technique/T0884) <small style="color:#929393">(v0.0)</small>
* [Damage to Property](/Technique/T0879) <small style="color:#929393">(v0.0)</small>
* [Data Destruction](/Technique/T0809) <small style="color:#929393">(v0.0)</small>
* [Data from Information Repositories](/Technique/T0811) <small style="color:#929393">(v0.0)</small>
* [Default Credentials](/Technique/T0812) <small style="color:#929393">(v0.0)</small>
* [Denial of Service](/Technique/T0814) <small style="color:#929393">(v0.0)</small>
* [Detect Operating Mode](/Technique/T0868) <small style="color:#929393">(v0.0)</small>
* [Device Restart/Shutdown](/Technique/T0816) <small style="color:#929393">(v0.0)</small>
* [Drive-by Compromise](/Technique/T0817) <small style="color:#929393">(v0.0)</small>
* [Execution through API](/Technique/T0871) <small style="color:#929393">(v0.0)</small>
* [Exploit Public-Facing Application](/Technique/T0819) <small style="color:#929393">(v0.0)</small>
* [Exploitation for Evasion](/Technique/T0820) <small style="color:#929393">(v0.0)</small>
* [Exploitation for Privilege Escalation](/Technique/T0890) <small style="color:#929393">(v0.0)</small>
* [Exploitation of Remote Services](/Technique/T0866) <small style="color:#929393">(v0.0)</small>
* [External Remote Services](/Technique/T0822) <small style="color:#929393">(v0.0)</small>
* [Graphical User Interface](/Technique/T0823) <small style="color:#929393">(v0.0)</small>
* [Hooking](/Technique/T0874) <small style="color:#929393">(v0.0)</small>
* [I/O Image](/Technique/T0877) <small style="color:#929393">(v0.0)</small>
* [Indicator Removal on Host](/Technique/T0872) <small style="color:#929393">(v0.0)</small>
* [Internet Accessible Device](/Technique/T0883) <small style="color:#929393">(v0.0)</small>
* [Lateral Tool Transfer](/Technique/T0867) <small style="color:#929393">(v0.0)</small>
* [Loss of Availability](/Technique/T0826) <small style="color:#929393">(v0.0)</small>
* [Loss of Productivity and Revenue](/Technique/T0828) <small style="color:#929393">(v0.0)</small>
* [Loss of Safety](/Technique/T0880) <small style="color:#929393">(v0.0)</small>
* [Loss of View](/Technique/T0829) <small style="color:#929393">(v0.0)</small>
* [Man in the Middle](/Technique/T0830) <small style="color:#929393">(v0.0)</small>
* [Manipulate I/O Image](/Technique/T835) <small style="color:#929393">(v0.0)</small>
* [Manipulation of Control](/Technique/T0831) <small style="color:#929393">(v0.0)</small>
* [Manipulation of View](/Technique/T0832) <small style="color:#929393">(v0.0)</small>
* [Masquerading](/Technique/T0849) <small style="color:#929393">(v0.0)</small>
* [Modify Alarm Settings](/Technique/T0838) <small style="color:#929393">(v0.0)</small>
* [Modify Controller Tasking](/Technique/T0821) <small style="color:#929393">(v0.0)</small>
* [Modify Parameter](/Technique/T0836) <small style="color:#929393">(v0.0)</small>
* [Modify Program](/Technique/T0889) <small style="color:#929393">(v0.0)</small>
* [Module Firmware](/Technique/T0839) <small style="color:#929393">(v0.0)</small>
* [Monitor Process State](/Technique/T0801) <small style="color:#929393">(v0.0)</small>
* [Native API](/Technique/T0834) <small style="color:#929393">(v0.0)</small>
* [Network Connection Enumeration](/Technique/T0840) <small style="color:#929393">(v0.0)</small>
* [Network Sniffing](/Technique/T0842) <small style="color:#929393">(v0.0)</small>
* [Point & Tag Identification](/Technique/T0861) <small style="color:#929393">(v0.0)</small>
* [Program Download](/Technique/T0843) <small style="color:#929393">(v0.0)</small>
* [Program Upload](/Technique/T0845) <small style="color:#929393">(v0.0)</small>
* [Project File Infection](/Technique/T0873) <small style="color:#929393">(v0.0)</small>
* [Remote Services](/Technique/T0886) <small style="color:#929393">(v0.0)</small>
* [Remote System Discovery](/Technique/T0846) <small style="color:#929393">(v0.0)</small>
* [Remote System Information Discovery](/Technique/T0888) <small style="color:#929393">(v0.0)</small>
* [Replication Through Removable Media](/Technique/T0847) <small style="color:#929393">(v0.0)</small>
* [Rogue Master](/Technique/T0848) <small style="color:#929393">(v0.0)</small>
* [Rootkit](/Technique/T0851) <small style="color:#929393">(v0.0)</small>
* [Screen Capture](/Technique/T0852) <small style="color:#929393">(v0.0)</small>
* [Scripting](/Technique/T0853) <small style="color:#929393">(v0.0)</small>
* [Service Stop](/Technique/T0881) <small style="color:#929393">(v0.0)</small>
* [Spearphishing Attachment](/Technique/T0865) <small style="color:#929393">(v0.0)</small>
* [Spoof Reporting Message](/Technique/T0856) <small style="color:#929393">(v0.0)</small>
* [Standard Application Layer Protocol](/Technique/T0869) <small style="color:#929393">(v0.0)</small>
* [Supply Chain Compromise](/Technique/T0862) <small style="color:#929393">(v0.0)</small>
* [System Firmware](/Technique/T0857) <small style="color:#929393">(v0.0)</small>
* [Theft of Operational Information](/Technique/T0882) <small style="color:#929393">(v0.0)</small>
* [Unauthorized Command Message](/Technique/T0855) <small style="color:#929393">(v0.0)</small>
* [User Execution](/Technique/T0863) <small style="color:#929393">(v0.0)</small>
* [Valid Accounts](/Technique/T0859) <small style="color:#929393">(v0.0)</small>
* [Wireless Compromise](/Technique/T0860) <small style="color:#929393">(v0.0)</small>

#### Deprecations

* [Data Historian Compromise](/Technique/T0810) <small style="color:#929393">(v0.0)</small>
* [Engineering Workstation Compromise](/Technique/T0818) <small style="color:#929393">(v0.0)</small>

## Software

### Enterprise

#### New Software

* [AppleSeed](/software/S0622) <small style="color:#929393">(v1.0)</small>
* [Avaddon](/software/S0640) <small style="color:#929393">(v1.0)</small>
* [BADFLICK](/software/S0642) <small style="color:#929393">(v1.0)</small>
* [BLUELIGHT](/software/S0657) <small style="color:#929393">(v1.0)</small>
* [Babuk](/software/S0638) <small style="color:#929393">(v1.0)</small>
* [Bad Rabbit](/software/S0606) <small style="color:#929393">(v1.0)</small>
* [BoomBox](/software/S0635) <small style="color:#929393">(v1.0)</small>
* [BoxCaon](/software/S0651) <small style="color:#929393">(v1.0)</small>
* [Chaes](/software/S0631) <small style="color:#929393">(v1.0)</small>
* [Clop](/software/S0611) <small style="color:#929393">(v1.0)</small>
* [Conficker](/software/S0608) <small style="color:#929393">(v1.0)</small>
* [CostaBricks](/software/S0614) <small style="color:#929393">(v1.0)</small>
* [Cuba](/software/S0625) <small style="color:#929393">(v1.0)</small>
* [DEATHRANSOM](/software/S0616) <small style="color:#929393">(v1.0)</small>
* [EKANS](/software/S0605) <small style="color:#929393">(v1.0)</small>
* [Ecipekac](/software/S0624) <small style="color:#929393">(v1.0)</small>
* [EnvyScout](/software/S0634) <small style="color:#929393">(v1.0)</small>
* [FIVEHANDS](/software/S0618) <small style="color:#929393">(v1.0)</small>
* [FYAnti](/software/S0628) <small style="color:#929393">(v1.0)</small>
* [GrimAgent](/software/S0632) <small style="color:#929393">(v1.0)</small>
* [HELLOKITTY](/software/S0617) <small style="color:#929393">(v1.0)</small>
* [Industroyer](/software/S0604) <small style="color:#929393">(v1.0)</small>
* [JSS Loader](/software/S0648) <small style="color:#929393">(v1.0)</small>
* [KillDisk](/software/S0607) <small style="color:#929393">(v1.0)</small>
* [Kobalos](/software/S0641) <small style="color:#929393">(v1.0)</small>
* [LiteDuke](/software/S0513) <small style="color:#929393">(v1.0)</small>
* [MarkiRAT](/software/S0652) <small style="color:#929393">(v1.0)</small>
* [NativeZone](/software/S0637) <small style="color:#929393">(v1.0)</small>
* [Nebulae](/software/S0630) <small style="color:#929393">(v1.0)</small>
* [ObliqueRAT](/software/S0644) <small style="color:#929393">(v1.0)</small>
* [P8RAT](/software/S0626) <small style="color:#929393">(v1.0)</small>
* [PS1](/software/S0613) <small style="color:#929393">(v1.0)</small>
* [Peppy](/software/S0643) <small style="color:#929393">(v1.0)</small>
* [ProLock](/software/S0654) <small style="color:#929393">(v1.0)</small>
* [QakBot](/software/S0650) <small style="color:#929393">(v1.0)</small>
* [RainyDay](/software/S0629) <small style="color:#929393">(v1.0)</small>
* [SMOKEDHAM](/software/S0649) <small style="color:#929393">(v1.0)</small>
* [Seth-Locker](/software/S0639) <small style="color:#929393">(v1.0)</small>
* [SideTwist](/software/S0610) <small style="color:#929393">(v1.0)</small>
* [Siloscape](/software/S0623) <small style="color:#929393">(v1.0)</small>
* [Sliver](/software/S0633) <small style="color:#929393">(v1.0)</small>
* [SodaMaster](/software/S0627) <small style="color:#929393">(v1.0)</small>
* [SombRAT](/software/S0615) <small style="color:#929393">(v1.0)</small>
* [SpicyOmelette](/software/S0646) <small style="color:#929393">(v1.0)</small>
* [Stuxnet](/software/S0603) <small style="color:#929393">(v1.0)</small>
* [TRITON](/software/S0609) <small style="color:#929393">(v1.0)</small>
* [Turian](/software/S0647) <small style="color:#929393">(v1.0)</small>
* [VaporRage](/software/S0636) <small style="color:#929393">(v1.0)</small>
* [WastedLocker](/software/S0612) <small style="color:#929393">(v1.0)</small>
* [Wevtutil](/software/S0645) <small style="color:#929393">(v1.0)</small>
* [XCSSET](/software/S0658) <small style="color:#929393">(v1.0)</small>
* [xCaon](/software/S0653) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* [Bandook](/software/S0234) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Dok](/software/S0281) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Dridex](/software/S0384) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [GuLoader](/software/S0561) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Kerrdown](/software/S0585) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Lokibot](/software/S0447) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Metamorfo](/software/S0455) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Octopus](/software/S0340) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Taidoor](/software/S0011) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [TrickBot](/software/S0266) <small style="color:#929393">(v1.4&#8594;v2.0)</small>

#### Minor Version Changes

* [Aria-body](/software/S0456) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Bazar](/software/S0534) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Bisonal](/software/S0268) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [BloodHound](/software/S0521) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Bundlore](/software/S0482) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Carberp](/software/S0484) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [China Chopper](/software/S0020) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* [Cobalt Strike](/software/S0154) <small style="color:#929393">(v1.6&#8594;v1.7)</small>
* [Conti](/software/S0575) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Crimson](/software/S0115) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [DropBook](/software/S0547) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Emissary](/software/S0082) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Empire](/software/S0363) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [FatDuke](/software/S0512) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Hildegard](/software/S0601) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Impacket](/software/S0357) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Keydnap](/software/S0276) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Kinsing](/software/S0599) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [LaZagne](/software/S0349) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [LoudMiner](/software/S0451) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Lucifer](/software/S0532) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Maze](/software/S0449) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [MimiPenguin](/software/S0179) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Mimikatz](/software/S0002) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [MiniDuke](/software/S0051) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [NETWIRE](/software/S0198) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Net](/software/S0039) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* [Nltest](/software/S0359) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [OSX/Shlayer](/software/S0402) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [OSX_OCEANLOTUS.D](/software/S0352) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [OwaAuth](/software/S0072) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [PoisonIvy](/software/S0012) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [PowerSploit](/software/S0194) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [PsExec](/software/S0029) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [QuasarRAT](/software/S0262) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [REvil](/software/S0496) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [RGDoor](/software/S0258) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Ryuk](/software/S0446) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [SUNBURST](/software/S0559) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [SharpStage](/software/S0546) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Spark](/software/S0543) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [SynAck](/software/S0242) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [ThiefQuest](/software/S0595) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Zeus Panda](/software/S0330) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [certutil](/software/S0160) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [esentutl](/software/S0404) <small style="color:#929393">(v1.1&#8594;v1.2)</small>

#### Metadata-only Changes

* [BADNEWS](/software/S0128) <small style="color:#929393">(v1.2)</small>
* [BOOTRASH](/software/S0114) <small style="color:#929393">(v1.1)</small>
* [ECCENTRICBANDWAGON](/software/S0593) <small style="color:#929393">(v1.0)</small>
* [Egregor](/software/S0554) <small style="color:#929393">(v1.0)</small>
* [Hikit](/software/S0009) <small style="color:#929393">(v1.2)</small>
* [HyperBro](/software/S0398) <small style="color:#929393">(v1.1)</small>
* [Reg](/software/S0075) <small style="color:#929393">(v1.0)</small>
* [WindTail](/software/S0466) <small style="color:#929393">(v1.0)</small>
* [zwShell](/software/S0350) <small style="color:#929393">(v1.1)</small>

### Mobile

#### New Software

* [BusyGasper](/software/S0655) <small style="color:#929393">(v1.0)</small>

#### Minor Version Changes

* [Anubis](/software/S0422) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [CarbonSteal](/software/S0529) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Monokle](/software/S0407) <small style="color:#929393">(v1.1&#8594;v1.2)</small>

### ICS

#### New Software

* [Bad Rabbit](/software/S0606) <small style="color:#929393">(v1.0)</small>
* [Conficker](/software/S0608) <small style="color:#929393">(v1.0)</small>
* [EKANS](/software/S0605) <small style="color:#929393">(v1.0)</small>
* [Industroyer](/software/S0604) <small style="color:#929393">(v1.0)</small>
* [KillDisk](/software/S0607) <small style="color:#929393">(v1.0)</small>
* [Stuxnet](/software/S0603) <small style="color:#929393">(v1.0)</small>

#### Minor Version Changes

* [REvil](/software/S0496) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Ryuk](/software/S0446) <small style="color:#929393">(v1.1&#8594;v1.2)</small>

#### Deletions

* Bad Rabbit <small style="color:#eb6635">(v1.0)</small>
* Conficker <small style="color:#eb6635">(v1.0)</small>
* EKANS <small style="color:#eb6635">(v1.0)</small>
* Industroyer <small style="color:#eb6635">(v1.0)</small>
* Killdisk <small style="color:#eb6635">(v1.0)</small>
* Stuxnet <small style="color:#eb6635">(v1.0)</small>

## Groups

### Enterprise

#### New Groups

* [Andariel](/groups/G0138) <small style="color:#929393">(v1.0)</small>
* [BackdoorDiplomacy](/groups/G0135) <small style="color:#929393">(v1.0)</small>
* [CostaRicto](/groups/G0132) <small style="color:#929393">(v1.0)</small>
* [Ferocious Kitten](/groups/G0137) <small style="color:#929393">(v1.0)</small>
* [IndigoZebra](/groups/G0136) <small style="color:#929393">(v1.0)</small>
* [Nomadic Octopus](/groups/G0133) <small style="color:#929393">(v1.0)</small>
* [TeamTNT](/groups/G0139) <small style="color:#929393">(v1.0)</small>
* [Tonto Team](/groups/G0131) <small style="color:#929393">(v1.0)</small>
* [Transparent Tribe](/groups/G0134) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* [APT37](/groups/G0067) <small style="color:#929393">(v1.5&#8594;v2.0)</small>
* [APT38](/groups/G0082) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* [APT41](/groups/G0096) <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* [Carbanak](/groups/G0008) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* [Cobalt Group](/groups/G0080) <small style="color:#929393">(v1.3&#8594;v2.0)</small>
* [FIN7](/groups/G0046) <small style="color:#929393">(v1.5&#8594;v2.0)</small>
* [Indrik Spider](/groups/G0119) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Kimsuky](/groups/G0094) <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* [Lazarus Group](/groups/G0032) <small style="color:#929393">(v1.5&#8594;v2.0)</small>
* [Leviathan](/groups/G0065) <small style="color:#929393">(v2.1&#8594;v3.0)</small>
* [Magic Hound](/groups/G0059) <small style="color:#929393">(v3.0&#8594;v4.0)</small>
* [Naikon](/groups/G0019) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [OilRig](/groups/G0049) <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* [Wizard Spider](/groups/G0102) <small style="color:#929393">(v1.3&#8594;v2.0)</small>

#### Minor Version Changes

* [APT-C-36](/groups/G0099) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [APT1](/groups/G0006) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [APT19](/groups/G0073) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [APT28](/groups/G0007) <small style="color:#929393">(v3.1&#8594;v3.2)</small>
* [APT29](/groups/G0016) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [APT3](/groups/G0022) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [APT32](/groups/G0050) <small style="color:#929393">(v2.4&#8594;v2.5)</small>
* [APT33](/groups/G0064) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [APT39](/groups/G0087) <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* [BRONZE BUTLER](/groups/G0060) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Blue Mockingbird](/groups/G0108) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Chimera](/groups/G0114) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Cleaver](/groups/G0003) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [CopyKittens](/groups/G0052) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [Dark Caracal](/groups/G0070) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [DarkHydrus](/groups/G0079) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [DarkVishnya](/groups/G0105) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Dragonfly](/groups/G0035) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Dragonfly 2.0](/groups/G0074) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [FIN10](/groups/G0051) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [FIN4](/groups/G0085) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [FIN5](/groups/G0053) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [FIN6](/groups/G0037) <small style="color:#929393">(v3.1&#8594;v3.2)</small>
* [FIN8](/groups/G0061) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Frankenstein](/groups/G0101) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Gorgon Group](/groups/G0078) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [Inception](/groups/G0100) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Ke3chang](/groups/G0004) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Leafminer](/groups/G0077) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* [Mustang Panda](/groups/G0129) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Night Dragon](/groups/G0014) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Patchwork](/groups/G0040) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [PittyTiger](/groups/G0011) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Sandworm Team](/groups/G0034) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Silence](/groups/G0091) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [TA505](/groups/G0092) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [TA551](/groups/G0127) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [TEMP.Veles](/groups/G0088) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Threat Group-3390](/groups/G0027) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [Thrip](/groups/G0076) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Turla](/groups/G0010) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [WIRTE](/groups/G0090) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Whitefly](/groups/G0107) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [menuPass](/groups/G0045) <small style="color:#929393">(v2.0&#8594;v2.1)</small>

#### Metadata-only Changes

* [Machete](/groups/G0095) <small style="color:#929393">(v2.0)</small>

#### Revocations

* Stolen Pencil (revoked by [Kimsuky](/groups/G0094)) <small style="color:#929393">(v0.0)</small>

#### Deprecations

* [Taidoor](/groups/G0015) <small style="color:#929393">(v1.0)</small>

### Mobile

#### Minor Version Changes

* [APT28](/groups/G0007) <small style="color:#929393">(v3.1&#8594;v3.2)</small>
* [Dark Caracal](/groups/G0070) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Sandworm Team](/groups/G0034) <small style="color:#929393">(v2.0&#8594;v2.1)</small>

### ICS

#### Major Version Changes

* [Lazarus Group](/groups/G0032) <small style="color:#929393">(v1.5&#8594;v2.0)</small>
* [OilRig](/groups/G0049) <small style="color:#929393">(v2.0&#8594;v3.0)</small>

#### Minor Version Changes

* [APT33](/groups/G0064) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Dragonfly](/groups/G0035) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Sandworm Team](/groups/G0034) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [TEMP.Veles](/groups/G0088) <small style="color:#929393">(v1.2&#8594;v1.3)</small>

#### Other Version Changes

* [Dragonfly 2.0](/groups/G0074) <small style="color:#eb6635">(v1.3&#8594;v2.1)</small>

## Campaigns

### Enterprise

### Mobile

### ICS

## Mitigations

### Enterprise

#### New Mitigations

* [Data Loss Prevention](/mitigations/M1057) <small style="color:#929393">(v1.0)</small>

### Mobile

### ICS

## Data Sources

### Enterprise

#### New Data Sources

* [Active Directory](/datasources/DS0026) <small style="color:#929393">(v1.0)</small>
* [Application Log](/datasources/DS0015) <small style="color:#929393">(v1.0)</small>
* [Certificate](/datasources/DS0037) <small style="color:#929393">(v1.0)</small>
* [Cloud Service](/datasources/DS0025) <small style="color:#929393">(v1.0)</small>
* [Cloud Storage](/datasources/DS0010) <small style="color:#929393">(v1.0)</small>
* [Cluster](/datasources/DS0031) <small style="color:#929393">(v1.0)</small>
* [Command](/datasources/DS0017) <small style="color:#929393">(v1.0)</small>
* [Container](/datasources/DS0032) <small style="color:#929393">(v1.0)</small>
* [Domain Name](/datasources/DS0038) <small style="color:#929393">(v1.0)</small>
* [Drive](/datasources/DS0016) <small style="color:#929393">(v1.0)</small>
* [Driver](/datasources/DS0027) <small style="color:#929393">(v1.0)</small>
* [File](/datasources/DS0022) <small style="color:#929393">(v1.0)</small>
* [Firewall](/datasources/DS0018) <small style="color:#929393">(v1.0)</small>
* [Firmware](/datasources/DS0001) <small style="color:#929393">(v1.0)</small>
* [Group](/datasources/DS0036) <small style="color:#929393">(v1.0)</small>
* [Image](/datasources/DS0007) <small style="color:#929393">(v1.0)</small>
* [Instance](/datasources/DS0030) <small style="color:#929393">(v1.0)</small>
* [Internet Scan](/datasources/DS0035) <small style="color:#929393">(v1.0)</small>
* [Kernel](/datasources/DS0008) <small style="color:#929393">(v1.0)</small>
* [Logon Session](/datasources/DS0028) <small style="color:#929393">(v1.0)</small>
* [Malware Repository](/datasources/DS0004) <small style="color:#929393">(v1.0)</small>
* [Module](/datasources/DS0011) <small style="color:#929393">(v1.0)</small>
* [Named Pipe](/datasources/DS0023) <small style="color:#929393">(v1.0)</small>
* [Network Share](/datasources/DS0033) <small style="color:#929393">(v1.0)</small>
* [Network Traffic](/datasources/DS0029) <small style="color:#929393">(v1.0)</small>
* [Persona](/datasources/DS0021) <small style="color:#929393">(v1.0)</small>
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
* [Web Credential](/datasources/DS0006) <small style="color:#929393">(v1.0)</small>
* [Windows Registry](/datasources/DS0024) <small style="color:#929393">(v1.0)</small>

### Mobile

### ICS

## Data Components

### Enterprise

#### New Data Components

* [Active DNS](/datasources/DS0038/#Active%20DNS) <small style="color:#929393">(v1.0)</small>
* [Active Directory Credential Request](/datasources/DS0026/#Active%20Directory%20Credential%20Request) <small style="color:#929393">(v1.0)</small>
* [Active Directory Object Access](/datasources/DS0026/#Active%20Directory%20Object%20Access) <small style="color:#929393">(v1.0)</small>
* [Active Directory Object Creation](/datasources/DS0026/#Active%20Directory%20Object%20Creation) <small style="color:#929393">(v1.0)</small>
* [Active Directory Object Deletion](/datasources/DS0026/#Active%20Directory%20Object%20Deletion) <small style="color:#929393">(v1.0)</small>
* [Active Directory Object Modification](/datasources/DS0026/#Active%20Directory%20Object%20Modification) <small style="color:#929393">(v1.0)</small>
* [Application Log Content](/datasources/DS0015/#Application%20Log%20Content) <small style="color:#929393">(v1.0)</small>
* [Certificate Registration](/datasources/DS0037/#Certificate%20Registration) <small style="color:#929393">(v1.0)</small>
* [Cloud Service Disable](/datasources/DS0025/#Cloud%20Service%20Disable) <small style="color:#929393">(v1.0)</small>
* [Cloud Service Enumeration](/datasources/DS0025/#Cloud%20Service%20Enumeration) <small style="color:#929393">(v1.0)</small>
* [Cloud Service Metadata](/datasources/DS0025/#Cloud%20Service%20Metadata) <small style="color:#929393">(v1.0)</small>
* [Cloud Service Modification](/datasources/DS0025/#Cloud%20Service%20Modification) <small style="color:#929393">(v1.0)</small>
* [Cloud Storage Access](/datasources/DS0010/#Cloud%20Storage%20Access) <small style="color:#929393">(v1.0)</small>
* [Cloud Storage Creation](/datasources/DS0010/#Cloud%20Storage%20Creation) <small style="color:#929393">(v1.0)</small>
* [Cloud Storage Deletion](/datasources/DS0010/#Cloud%20Storage%20Deletion) <small style="color:#929393">(v1.0)</small>
* [Cloud Storage Enumeration](/datasources/DS0010/#Cloud%20Storage%20Enumeration) <small style="color:#929393">(v1.0)</small>
* [Cloud Storage Metadata](/datasources/DS0010/#Cloud%20Storage%20Metadata) <small style="color:#929393">(v1.0)</small>
* [Cloud Storage Modification](/datasources/DS0010/#Cloud%20Storage%20Modification) <small style="color:#929393">(v1.0)</small>
* [Cluster Metadata](/datasources/DS0031/#Cluster%20Metadata) <small style="color:#929393">(v1.0)</small>
* [Command Execution](/datasources/DS0017/#Command%20Execution) <small style="color:#929393">(v1.0)</small>
* [Container Creation](/datasources/DS0032/#Container%20Creation) <small style="color:#929393">(v1.0)</small>
* [Container Enumeration](/datasources/DS0032/#Container%20Enumeration) <small style="color:#929393">(v1.0)</small>
* [Container Metadata](/datasources/DS0032/#Container%20Metadata) <small style="color:#929393">(v1.0)</small>
* [Container Start](/datasources/DS0032/#Container%20Start) <small style="color:#929393">(v1.0)</small>
* [Domain Registration](/datasources/DS0038/#Domain%20Registration) <small style="color:#929393">(v1.0)</small>
* [Drive Access](/datasources/DS0016/#Drive%20Access) <small style="color:#929393">(v1.0)</small>
* [Drive Creation](/datasources/DS0016/#Drive%20Creation) <small style="color:#929393">(v1.0)</small>
* [Drive Modification](/datasources/DS0016/#Drive%20Modification) <small style="color:#929393">(v1.0)</small>
* [Driver Load](/datasources/DS0027/#Driver%20Load) <small style="color:#929393">(v1.0)</small>
* [Driver Metadata](/datasources/DS0027/#Driver%20Metadata) <small style="color:#929393">(v1.0)</small>
* [File Access](/datasources/DS0022/#File%20Access) <small style="color:#929393">(v1.0)</small>
* [File Creation](/datasources/DS0022/#File%20Creation) <small style="color:#929393">(v1.0)</small>
* [File Deletion](/datasources/DS0022/#File%20Deletion) <small style="color:#929393">(v1.0)</small>
* [File Metadata](/datasources/DS0022/#File%20Metadata) <small style="color:#929393">(v1.0)</small>
* [File Modification](/datasources/DS0022/#File%20Modification) <small style="color:#929393">(v1.0)</small>
* [Firewall Disable](/datasources/DS0018/#Firewall%20Disable) <small style="color:#929393">(v1.0)</small>
* [Firewall Enumeration](/datasources/DS0018/#Firewall%20Enumeration) <small style="color:#929393">(v1.0)</small>
* [Firewall Metadata](/datasources/DS0018/#Firewall%20Metadata) <small style="color:#929393">(v1.0)</small>
* [Firewall Rule Modification](/datasources/DS0018/#Firewall%20Rule%20Modification) <small style="color:#929393">(v1.0)</small>
* [Firmware Modification](/datasources/DS0001/#Firmware%20Modification) <small style="color:#929393">(v1.0)</small>
* [Group Enumeration](/datasources/DS0036/#Group%20Enumeration) <small style="color:#929393">(v1.0)</small>
* [Group Metadata](/datasources/DS0036/#Group%20Metadata) <small style="color:#929393">(v1.0)</small>
* [Group Modification](/datasources/DS0036/#Group%20Modification) <small style="color:#929393">(v1.0)</small>
* [Host Status](/datasources/DS0013/#Host%20Status) <small style="color:#929393">(v1.0)</small>
* [Image Creation](/datasources/DS0007/#Image%20Creation) <small style="color:#929393">(v1.0)</small>
* [Image Deletion](/datasources/DS0007/#Image%20Deletion) <small style="color:#929393">(v1.0)</small>
* [Image Metadata](/datasources/DS0007/#Image%20Metadata) <small style="color:#929393">(v1.0)</small>
* [Image Modification](/datasources/DS0007/#Image%20Modification) <small style="color:#929393">(v1.0)</small>
* [Instance Creation](/datasources/DS0030/#Instance%20Creation) <small style="color:#929393">(v1.0)</small>
* [Instance Deletion](/datasources/DS0030/#Instance%20Deletion) <small style="color:#929393">(v1.0)</small>
* [Instance Enumeration](/datasources/DS0030/#Instance%20Enumeration) <small style="color:#929393">(v1.0)</small>
* [Instance Metadata](/datasources/DS0030/#Instance%20Metadata) <small style="color:#929393">(v1.0)</small>
* [Instance Modification](/datasources/DS0030/#Instance%20Modification) <small style="color:#929393">(v1.0)</small>
* [Instance Start](/datasources/DS0030/#Instance%20Start) <small style="color:#929393">(v1.0)</small>
* [Instance Stop](/datasources/DS0030/#Instance%20Stop) <small style="color:#929393">(v1.0)</small>
* [Kernel Module Load](/datasources/DS0008/#Kernel%20Module%20Load) <small style="color:#929393">(v1.0)</small>
* [Logon Session Creation](/datasources/DS0028/#Logon%20Session%20Creation) <small style="color:#929393">(v1.0)</small>
* [Logon Session Metadata](/datasources/DS0028/#Logon%20Session%20Metadata) <small style="color:#929393">(v1.0)</small>
* [Malware Content](/datasources/DS0004/#Malware%20Content) <small style="color:#929393">(v1.0)</small>
* [Malware Metadata](/datasources/DS0004/#Malware%20Metadata) <small style="color:#929393">(v1.0)</small>
* [Module Load](/datasources/DS0011/#Module%20Load) <small style="color:#929393">(v1.0)</small>
* [Named Pipe Metadata](/datasources/DS0023/#Named%20Pipe%20Metadata) <small style="color:#929393">(v1.0)</small>
* [Network Connection Creation](/datasources/DS0029/#Network%20Connection%20Creation) <small style="color:#929393">(v1.0)</small>
* [Network Share Access](/datasources/DS0033/#Network%20Share%20Access) <small style="color:#929393">(v1.0)</small>
* [Network Traffic Content](/datasources/DS0029/#Network%20Traffic%20Content) <small style="color:#929393">(v1.0)</small>
* [Network Traffic Flow](/datasources/DS0029/#Network%20Traffic%20Flow) <small style="color:#929393">(v1.0)</small>
* [OS API Execution](/datasources/DS0009/#OS%20API%20Execution) <small style="color:#929393">(v1.0)</small>
* [Passive DNS](/datasources/DS0038/#Passive%20DNS) <small style="color:#929393">(v1.0)</small>
* [Pod Creation](/datasources/DS0014/#Pod%20Creation) <small style="color:#929393">(v1.0)</small>
* [Pod Enumeration](/datasources/DS0014/#Pod%20Enumeration) <small style="color:#929393">(v1.0)</small>
* [Pod Metadata](/datasources/DS0014/#Pod%20Metadata) <small style="color:#929393">(v1.0)</small>
* [Pod Modification](/datasources/DS0014/#Pod%20Modification) <small style="color:#929393">(v1.0)</small>
* [Process Access](/datasources/DS0009/#Process%20Access) <small style="color:#929393">(v1.0)</small>
* [Process Creation](/datasources/DS0009/#Process%20Creation) <small style="color:#929393">(v1.0)</small>
* [Process Metadata](/datasources/DS0009/#Process%20Metadata) <small style="color:#929393">(v1.0)</small>
* [Process Modification](/datasources/DS0009/#Process%20Modification) <small style="color:#929393">(v1.0)</small>
* [Process Termination](/datasources/DS0009/#Process%20Termination) <small style="color:#929393">(v1.0)</small>
* [Response Content](/datasources/DS0035/#Response%20Content) <small style="color:#929393">(v1.0)</small>
* [Response Metadata](/datasources/DS0035/#Response%20Metadata) <small style="color:#929393">(v1.0)</small>
* [Scheduled Job Creation](/datasources/DS0003/#Scheduled%20Job%20Creation) <small style="color:#929393">(v1.0)</small>
* [Scheduled Job Metadata](/datasources/DS0003/#Scheduled%20Job%20Metadata) <small style="color:#929393">(v1.0)</small>
* [Scheduled Job Modification](/datasources/DS0003/#Scheduled%20Job%20Modification) <small style="color:#929393">(v1.0)</small>
* [Script Execution](/datasources/DS0012/#Script%20Execution) <small style="color:#929393">(v1.0)</small>
* [Service Creation](/datasources/DS0019/#Service%20Creation) <small style="color:#929393">(v1.0)</small>
* [Service Metadata](/datasources/DS0019/#Service%20Metadata) <small style="color:#929393">(v1.0)</small>
* [Service Modification](/datasources/DS0019/#Service%20Modification) <small style="color:#929393">(v1.0)</small>
* [Snapshot Creation](/datasources/DS0020/#Snapshot%20Creation) <small style="color:#929393">(v1.0)</small>
* [Snapshot Deletion](/datasources/DS0020/#Snapshot%20Deletion) <small style="color:#929393">(v1.0)</small>
* [Snapshot Enumeration](/datasources/DS0020/#Snapshot%20Enumeration) <small style="color:#929393">(v1.0)</small>
* [Snapshot Metadata](/datasources/DS0020/#Snapshot%20Metadata) <small style="color:#929393">(v1.0)</small>
* [Snapshot Modification](/datasources/DS0020/#Snapshot%20Modification) <small style="color:#929393">(v1.0)</small>
* [Social Media](/datasources/DS0021/#Social%20Media) <small style="color:#929393">(v1.0)</small>
* [User Account Authentication](/datasources/DS0002/#User%20Account%20Authentication) <small style="color:#929393">(v1.0)</small>
* [User Account Creation](/datasources/DS0002/#User%20Account%20Creation) <small style="color:#929393">(v1.0)</small>
* [User Account Deletion](/datasources/DS0002/#User%20Account%20Deletion) <small style="color:#929393">(v1.0)</small>
* [User Account Metadata](/datasources/DS0002/#User%20Account%20Metadata) <small style="color:#929393">(v1.0)</small>
* [User Account Modification](/datasources/DS0002/#User%20Account%20Modification) <small style="color:#929393">(v1.0)</small>
* [Volume Creation](/datasources/DS0034/#Volume%20Creation) <small style="color:#929393">(v1.0)</small>
* [Volume Deletion](/datasources/DS0034/#Volume%20Deletion) <small style="color:#929393">(v1.0)</small>
* [Volume Enumeration](/datasources/DS0034/#Volume%20Enumeration) <small style="color:#929393">(v1.0)</small>
* [Volume Metadata](/datasources/DS0034/#Volume%20Metadata) <small style="color:#929393">(v1.0)</small>
* [Volume Modification](/datasources/DS0034/#Volume%20Modification) <small style="color:#929393">(v1.0)</small>
* [WMI Creation](/datasources/DS0005/#WMI%20Creation) <small style="color:#929393">(v1.0)</small>
* [Web Credential Creation](/datasources/DS0006/#Web%20Credential%20Creation) <small style="color:#929393">(v1.0)</small>
* [Web Credential Usage](/datasources/DS0006/#Web%20Credential%20Usage) <small style="color:#929393">(v1.0)</small>
* [Windows Registry Key Access](/datasources/DS0024/#Windows%20Registry%20Key%20Access) <small style="color:#929393">(v1.0)</small>
* [Windows Registry Key Creation](/datasources/DS0024/#Windows%20Registry%20Key%20Creation) <small style="color:#929393">(v1.0)</small>
* [Windows Registry Key Deletion](/datasources/DS0024/#Windows%20Registry%20Key%20Deletion) <small style="color:#929393">(v1.0)</small>
* [Windows Registry Key Modification](/datasources/DS0024/#Windows%20Registry%20Key%20Modification) <small style="color:#929393">(v1.0)</small>

### Mobile

### ICS

## Contributors to this release

* @ionstorm
* Achute Sharma, Keysight
* Arnim Rupp, Deutsche Lufthansa AG
* Atul Nair, Qualys
* Austin Clark
* Ayan Saha, Keysight
* Christoffer Strömblad
* Christopher Glyer, Mandiant, @cglyer
* Cody Thomas, SpecterOps
* CTID
* Dan Borges, @1njection
* Daniel Prizmant, Palo Alto Networks
* Daniyal Naeem, BT Security
* Dor Edry, Microsoft
* Edward Millington
* Eli Salem, @elisalem9
* ExtraHop
* Gaetan van Diemen, ThreatFabric
* Gareth Phillips, Seek Ltd.
* Gordon Long, Box, Inc., @ethicalhax
* Harshal Tupsamudre, Qualys
* Hiroki Nagahama, NEC Corporation
* Isif Ibrahima
* Itamar Mizrahi, Cymptom
* Ivan Sinyakov
* Janantha Marasinghe
* Jaron Bradley @jbradley89
* Jeff Felling, Red Canary
* Jen Burns, HubSpot
* Joas Antonio dos Santos, @C0d3Cr4zy
* Johann Rehberger
* Jon Sheedy
* Jon Sternstein, Stern Security
* Jonathan Boucher, @crash_wave, Bank of Canada
* Jonhnathan Ribeiro, 3CORESec, @_w0rk3r
* Jorell Magtibay, National Australia Bank Limited
* Jorge Orchilles, SCYTHE
* Jose Luis Sánchez Martinez
* Josh Liburdi, @jshlbrd
* João Paulo de A. Filho, @Hug1nN__
* Jörg Abraham, EclecticIQ
* Karim Hasanen, @_karimhasanen
* Kiyohito Yamamoto, RedLark, NTT Communications
* Kyaw Pyiyt Htet, @KyawPyiytHtet
* Kyoung-ju Kwak (S2W)
* Lior Ribak , SentinelOne
* Manikantan Srinivasan, NEC Corporation India
* Maril Vernon @shewhohacks
* Matt Brenton, Zurich Global Information Security
* Microsoft Detection and Response Team (DART)
* Microsoft Security
* Mike Burns, Mandiant
* Mnemonic AS
* Nagahama Hiroki, NEC Corporation
* Naveen Vijayaraghavan, Nilesh Dherange (Gurucul)
* Nick Carr, Mandiant
* Omkar Gudhate
* Patrick Sungbahadoor
* Pooja Natarajan, NEC Corporation India
* Prasanth Sadanala, Cigna Information Protection (CIP) - Threat Response Engineering Team
* Regina Elwell
* Rex Guo, @Xiaofei_REX, Confluera
* Rick Cole, Mandiant
* Ruben Dodge, @shotgunner101
* Shlomi Salem, SentinelOne
* SOCCRATES
* Stan Hegt, Outflank
* Ted Samuels, Rapid7
* Tim (Wadhwa-)Brown
* Toby Kohlenberg
* Vadim Khrykov
* Viren Chaudhari, Qualys
* Wes Hurd
* Will Thomas, Cyjax
* William Cain
* Yoshihiro Kori, NEC Corporation
* Yossi Nisani, Cymptom
* Yusuke Kubo, RedLark, NTT Communications
* Yuval Avrahami, Palo Alto Networks
* Zaw Min Htun, @Z3TAE
* Ziv Kaspersky, Cymptom
