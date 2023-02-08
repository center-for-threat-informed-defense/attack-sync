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
* Boot or Logon Autostart Execution: [Login Items](/techniques/T1547/015) <small style="color:#929393">(v1.0)</small>
* Boot or Logon Autostart Execution: [XDG Autostart Entries](/techniques/T1547/013) <small style="color:#929393">(v1.0)</small>
* [Build Image on Host](/techniques/T1612) <small style="color:#eb6635">(v1.1)</small>
* [Cloud Storage Object Discovery](/techniques/T1619) <small style="color:#929393">(v1.0)</small>
* [Container Administration Command](/techniques/T1609) <small style="color:#929393">(v1.0)</small>
* [Container and Resource Discovery](/techniques/T1613) <small style="color:#929393">(v1.0)</small>
* Credentials from Password Stores: [Password Managers](/techniques/T1555/005) <small style="color:#929393">(v1.0)</small>
* Credentials from Password Stores: [Windows Credential Manager](/techniques/T1555/004) <small style="color:#929393">(v1.0)</small>
* Data from Information Repositories: [Code Repositories](/techniques/T1213/003) <small style="color:#929393">(v1.0)</small>
* [Deploy Container](/techniques/T1610) <small style="color:#929393">(v1.0)</small>
* [Escape to Host](/techniques/T1611) <small style="color:#eb6635">(v1.1)</small>
* [Group Policy Discovery](/techniques/T1615) <small style="color:#929393">(v1.0)</small>
* Hide Artifacts: [Email Hiding Rules](/techniques/T1564/008) <small style="color:#929393">(v1.0)</small>
* Hide Artifacts: [Resource Forking](/techniques/T1564/009) <small style="color:#929393">(v1.0)</small>
* Impair Defenses: [Downgrade Attack](/techniques/T1562/010) <small style="color:#929393">(v1.0)</small>
* Impair Defenses: [Safe Mode Boot](/techniques/T1562/009) <small style="color:#929393">(v1.0)</small>
* Masquerading: [Double File Extension](/techniques/T1036/007) <small style="color:#929393">(v1.0)</small>
* Obfuscated Files or Information: [HTML Smuggling](/techniques/T1027/006) <small style="color:#929393">(v1.0)</small>
* [Reflective Code Loading](/techniques/T1620) <small style="color:#929393">(v1.0)</small>
* Scheduled Task/Job: [Container Orchestration Job](/techniques/T1053/007) <small style="color:#eb6635">(v1.1)</small>
* Server Software Component: [IIS Components](/techniques/T1505/004) <small style="color:#929393">(v1.0)</small>
* Signed Binary Proxy Execution: [MMC](/techniques/T1218/014) <small style="color:#929393">(v1.0)</small>
* Signed Binary Proxy Execution: [Mavinject](/techniques/T1218/013) <small style="color:#929393">(v1.0)</small>
* [Stage Capabilities](/techniques/T1608) <small style="color:#eb6635">(v1.1)</small>
    * [Drive-by Target](/techniques/T1608/004) <small style="color:#eb6635">(v1.1)</small>
    * [Install Digital Certificate](/techniques/T1608/003) <small style="color:#eb6635">(v1.1)</small>
    * [Link Target](/techniques/T1608/005) <small style="color:#eb6635">(v1.1)</small>
    * [Upload Malware](/techniques/T1608/001) <small style="color:#eb6635">(v1.1)</small>
    * [Upload Tool](/techniques/T1608/002) <small style="color:#eb6635">(v1.1)</small>
* Subvert Trust Controls: [Code Signing Policy Modification](/techniques/T1553/006) <small style="color:#929393">(v1.0)</small>
* Subvert Trust Controls: [Mark-of-the-Web Bypass](/techniques/T1553/005) <small style="color:#929393">(v1.0)</small>
* [System Location Discovery](/techniques/T1614) <small style="color:#929393">(v1.0)</small>
    * [System Language Discovery](/techniques/T1614/001) <small style="color:#929393">(v1.0)</small>
* System Network Configuration Discovery: [Internet Connection Discovery](/techniques/T1016/001) <small style="color:#929393">(v1.0)</small>
* Unsecured Credentials: [Container API](/techniques/T1552/007) <small style="color:#929393">(v1.0)</small>
* User Execution: [Malicious Image](/techniques/T1204/003) <small style="color:#eb6635">(v1.1)</small>

#### Major Version Changes

* [Adversary-in-the-Middle](/techniques/T1557) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* Boot or Logon Initialization Scripts: [RC Scripts](/techniques/T1037/004) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Browser Session Hijacking](/techniques/T1185) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* Hijack Execution Flow: [DLL Side-Loading](/techniques/T1574/002) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* Hijack Execution Flow: [Dylib Hijacking](/techniques/T1574/004) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* Hijack Execution Flow: [Dynamic Linker Hijacking](/techniques/T1574/006) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Implant Internal Image](/techniques/T1525) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Modify Authentication Process](/techniques/T1556) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
    * [Domain Controller Authentication](/techniques/T1556/001) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
    * [Network Device Authentication](/techniques/T1556/004) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
    * [Password Filter DLL](/techniques/T1556/002) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
    * [Pluggable Authentication Modules](/techniques/T1556/003) <small style="color:#929393">(v1.0&#8594;v2.0)</small>

#### Minor Version Changes

* Access Token Manipulation: [Create Process with Token](/techniques/T1134/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Account Discovery](/techniques/T1087) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
    * [Cloud Account](/techniques/T1087/004) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Email Account](/techniques/T1087/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Account Manipulation](/techniques/T1098) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
    * [Additional Cloud Credentials](/techniques/T1098/001) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
    * [Exchange Email Delegate Permissions](/techniques/T1098/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Acquire Infrastructure](/techniques/T1583) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Domains](/techniques/T1583/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Server](/techniques/T1583/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Virtual Private Server](/techniques/T1583/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Web Services](/techniques/T1583/006) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Adversary-in-the-Middle: [ARP Cache Poisoning](/techniques/T1557/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Automated Exfiltration: [Traffic Duplication](/techniques/T1020/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [BITS Jobs](/techniques/T1197) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Boot or Logon Autostart Execution: [Plist Modification](/techniques/T1547/011) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Boot or Logon Autostart Execution: [Shortcut Modification](/techniques/T1547/009) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Browser Extensions](/techniques/T1176) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Brute Force: [Credential Stuffing](/techniques/T1110/004) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Brute Force: [Password Guessing](/techniques/T1110/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Brute Force: [Password Spraying](/techniques/T1110/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Cloud Service Dashboard](/techniques/T1538) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Cloud Service Discovery](/techniques/T1526) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Command and Scripting Interpreter](/techniques/T1059) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
    * [Network Device CLI](/techniques/T1059/008) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [PowerShell](/techniques/T1059/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Unix Shell](/techniques/T1059/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Visual Basic](/techniques/T1059/005) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Compromise Accounts](/techniques/T1586) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Social Media Accounts](/techniques/T1586/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Compromise Infrastructure](/techniques/T1584) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [DNS Server](/techniques/T1584/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Domains](/techniques/T1584/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Server](/techniques/T1584/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Virtual Private Server](/techniques/T1584/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Web Services](/techniques/T1584/006) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Create Account](/techniques/T1136) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
    * [Cloud Account](/techniques/T1136/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Local Account](/techniques/T1136/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Create or Modify System Process: [Launch Daemon](/techniques/T1543/004) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Credentials from Password Stores: [Credentials from Web Browsers](/techniques/T1555/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Data Destruction](/techniques/T1485) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Data Staged](/techniques/T1074) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
    * [Remote Data Staging](/techniques/T1074/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Data from Cloud Storage Object](/techniques/T1530) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Data from Local System](/techniques/T1005) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Data from Removable Media](/techniques/T1025) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Defacement](/techniques/T1491) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [External Defacement](/techniques/T1491/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Develop Capabilities](/techniques/T1587) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Code Signing Certificates](/techniques/T1587/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Drive-by Compromise](/techniques/T1189) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Email Collection: [Remote Email Collection](/techniques/T1114/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Endpoint Denial of Service](/techniques/T1499) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Application Exhaustion Flood](/techniques/T1499/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Application or System Exploitation](/techniques/T1499/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Service Exhaustion Flood](/techniques/T1499/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Establish Accounts: [Social Media Accounts](/techniques/T1585/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Exfiltration Over Alternative Protocol](/techniques/T1048) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
    * [Exfiltration Over Asymmetric Encrypted Non-C2 Protocol](/techniques/T1048/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Exfiltration Over Unencrypted/Obfuscated Non-C2 Protocol](/techniques/T1048/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Exfiltration Over C2 Channel](/techniques/T1041) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Exfiltration Over Physical Medium](/techniques/T1052) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Exfiltration over USB](/techniques/T1052/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Exfiltration Over Web Service](/techniques/T1567) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Exploit Public-Facing Application](/techniques/T1190) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* [Exploitation for Client Execution](/techniques/T1203) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Exploitation for Privilege Escalation](/techniques/T1068) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* File and Directory Permissions Modification: [Linux and Mac File and Directory Permissions Modification](/techniques/T1222/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Forge Web Credentials: [Web Cookies](/techniques/T1606/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
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
* [Hijack Execution Flow](/techniques/T1574) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [DLL Search Order Hijacking](/techniques/T1574/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Services Registry Permissions Weakness](/techniques/T1574/011) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Impair Defenses: [Disable Cloud Logs](/techniques/T1562/008) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Impair Defenses: [Disable Windows Event Logging](/techniques/T1562/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Impair Defenses: [Disable or Modify Cloud Firewall](/techniques/T1562/007) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Indicator Removal on Host](/techniques/T1070) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Input Capture: [GUI Input Capture](/techniques/T1056/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Inter-Process Communication](/techniques/T1559) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Component Object Model](/techniques/T1559/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Dynamic Data Exchange](/techniques/T1559/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Internal Spearphishing](/techniques/T1534) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Lateral Tool Transfer](/techniques/T1570) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Masquerading](/techniques/T1036) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
    * [Masquerade Task or Service](/techniques/T1036/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Match Legitimate Name or Location](/techniques/T1036/005) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Right-to-Left Override](/techniques/T1036/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Modify Cloud Compute Infrastructure](/techniques/T1578) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Create Cloud Instance](/techniques/T1578/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Create Snapshot](/techniques/T1578/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Delete Cloud Instance](/techniques/T1578/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Revert Cloud Instance](/techniques/T1578/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Native API](/techniques/T1106) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Network Denial of Service](/techniques/T1498) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Direct Network Flood](/techniques/T1498/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Reflection Amplification](/techniques/T1498/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Network Service Scanning](/techniques/T1046) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [Network Share Discovery](/techniques/T1135) <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* [Network Sniffing](/techniques/T1040) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [OS Credential Dumping](/techniques/T1003) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
    * [LSASS Memory](/techniques/T1003/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Obfuscated Files or Information](/techniques/T1027) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Binary Padding](/techniques/T1027/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Software Packing](/techniques/T1027/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Steganography](/techniques/T1027/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Obtain Capabilities](/techniques/T1588) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Code Signing Certificates](/techniques/T1588/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
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
* Phishing: [Spearphishing Link](/techniques/T1566/002) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Phishing for Information](/techniques/T1598) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Spearphishing Attachment](/techniques/T1598/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Spearphishing Link](/techniques/T1598/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
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
* [Replication Through Removable Media](/techniques/T1091) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Resource Hijacking](/techniques/T1496) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Scheduled Task/Job](/techniques/T1053) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
    * [At (Linux)](/techniques/T1053/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Cron](/techniques/T1053/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Systemd Timers](/techniques/T1053/006) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Server Software Component](/techniques/T1505) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Web Shell](/techniques/T1505/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Service Stop](/techniques/T1489) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Shared Modules](/techniques/T1129) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Signed Binary Proxy Execution: [Mshta](/techniques/T1218/005) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Signed Binary Proxy Execution: [Msiexec](/techniques/T1218/007) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Signed Binary Proxy Execution: [Rundll32](/techniques/T1218/011) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Signed Script Proxy Execution: [PubPrn](/techniques/T1216/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Software Discovery](/techniques/T1518) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
    * [Security Software Discovery](/techniques/T1518/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Steal Application Access Token](/techniques/T1528) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Steal or Forge Kerberos Tickets: [Golden Ticket](/techniques/T1558/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Subvert Trust Controls](/techniques/T1553) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Gatekeeper Bypass](/techniques/T1553/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Install Root Certificate](/techniques/T1553/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [System Network Configuration Discovery](/techniques/T1016) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [System Network Connections Discovery](/techniques/T1049) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [System Owner/User Discovery](/techniques/T1033) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [System Service Discovery](/techniques/T1007) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [System Services](/techniques/T1569) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Launchctl](/techniques/T1569/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Service Execution](/techniques/T1569/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [System Time Discovery](/techniques/T1124) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Taint Shared Content](/techniques/T1080) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Traffic Signaling](/techniques/T1205) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [Transfer Data to Cloud Account](/techniques/T1537) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Unsecured Credentials](/techniques/T1552) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Cloud Instance Metadata API](/techniques/T1552/005) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Credentials In Files](/techniques/T1552/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Unused/Unsupported Cloud Regions](/techniques/T1535) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Use Alternate Authentication Material: [Application Access Token](/techniques/T1550/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Use Alternate Authentication Material: [Pass the Hash](/techniques/T1550/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Use Alternate Authentication Material: [Pass the Ticket](/techniques/T1550/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* User Execution: [Malicious File](/techniques/T1204/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Valid Accounts: [Default Accounts](/techniques/T1078/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Valid Accounts: [Domain Accounts](/techniques/T1078/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Virtualization/Sandbox Evasion](/techniques/T1497) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
    * [User Activity Based Checks](/techniques/T1497/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Windows Management Instrumentation](/techniques/T1047) <small style="color:#929393">(v1.1&#8594;v1.2)</small>

#### Other Version Changes

* Account Discovery: [Local Account](/techniques/T1087/001) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
* Adversary-in-the-Middle: [LLMNR/NBT-NS Poisoning and SMB Relay](/techniques/T1557/001) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
* Boot or Logon Autostart Execution: [Kernel Modules and Extensions](/techniques/T1547/006) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
* [Brute Force](/techniques/T1110) <small style="color:#eb6635">(v2.1&#8594;v2.3)</small>
* [Cloud Infrastructure Discovery](/techniques/T1580) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
* Command and Scripting Interpreter: [JavaScript](/techniques/T1059/007) <small style="color:#eb6635">(v1.0&#8594;v2.1)</small>
* Command and Scripting Interpreter: [Windows Command Shell](/techniques/T1059/003) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
* Create or Modify System Process: [Launch Agent](/techniques/T1543/001) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
* [Data Encrypted for Impact](/techniques/T1486) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
* [Data from Information Repositories](/techniques/T1213) <small style="color:#eb6635">(v3.0&#8594;v3.2)</small>
* Develop Capabilities: [Digital Certificates](/techniques/T1587/003) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
* Develop Capabilities: [Malware](/techniques/T1587/001) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
* [Email Collection](/techniques/T1114) <small style="color:#eb6635">(v2.1&#8594;v2.3)</small>
    * [Email Forwarding Rule](/techniques/T1114/003) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
* [Establish Accounts](/techniques/T1585) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
* Event Triggered Execution: [Unix Shell Configuration Modification](/techniques/T1546/004) <small style="color:#eb6635">(v1.0&#8594;v2.1)</small>
* Event Triggered Execution: [Windows Management Instrumentation Event Subscription](/techniques/T1546/003) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
* [External Remote Services](/techniques/T1133) <small style="color:#eb6635">(v2.1&#8594;v2.3)</small>
* [Forge Web Credentials](/techniques/T1606) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
    * [SAML Tokens](/techniques/T1606/002) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
* [Impair Defenses](/techniques/T1562) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
    * [Disable or Modify Tools](/techniques/T1562/001) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
* Obtain Capabilities: [Digital Certificates](/techniques/T1588/004) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
* [Permission Groups Discovery](/techniques/T1069) <small style="color:#eb6635">(v2.2&#8594;v2.4)</small>
    * [Cloud Groups](/techniques/T1069/003) <small style="color:#eb6635">(v1.1&#8594;v1.3)</small>
* [Phishing](/techniques/T1566) <small style="color:#eb6635">(v2.0&#8594;v2.2)</small>
    * [Spearphishing Attachment](/techniques/T1566/001) <small style="color:#eb6635">(v2.0&#8594;v2.2)</small>
* [Remote System Discovery](/techniques/T1018) <small style="color:#eb6635">(v3.0&#8594;v3.2)</small>
* [Steal Web Session Cookie](/techniques/T1539) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
* [Steal or Forge Kerberos Tickets](/techniques/T1558) <small style="color:#eb6635">(v1.1&#8594;v1.3)</small>
* [System Information Discovery](/techniques/T1082) <small style="color:#eb6635">(v2.1&#8594;v2.3)</small>
* Trusted Developer Utilities Proxy Execution: [MSBuild](/techniques/T1127/001) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
* [Trusted Relationship](/techniques/T1199) <small style="color:#eb6635">(v2.0&#8594;v2.2)</small>
* [Use Alternate Authentication Material](/techniques/T1550) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
    * [Web Session Cookie](/techniques/T1550/004) <small style="color:#eb6635">(v1.1&#8594;v1.3)</small>
* [User Execution](/techniques/T1204) <small style="color:#eb6635">(v1.2&#8594;v1.4)</small>
* [Valid Accounts](/techniques/T1078) <small style="color:#eb6635">(v2.1&#8594;v2.3)</small>
    * [Cloud Accounts](/techniques/T1078/004) <small style="color:#eb6635">(v1.1&#8594;v1.3)</small>
    * [Local Accounts](/techniques/T1078/003) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
* Virtualization/Sandbox Evasion: [System Checks](/techniques/T1497/001) <small style="color:#eb6635">(v1.0&#8594;v2.1)</small>
* Virtualization/Sandbox Evasion: [Time Based Evasion](/techniques/T1497/003) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>

#### Metadata-only Changes

* [Access Token Manipulation](/techniques/T1134) <small style="color:#929393">(v2.0)</small>
    * [Parent PID Spoofing](/techniques/T1134/004) <small style="color:#929393">(v1.0)</small>
    * [SID-History Injection](/techniques/T1134/005) <small style="color:#929393">(v1.0)</small>
* Account Discovery: [Domain Account](/techniques/T1087/002) <small style="color:#929393">(v1.0)</small>
* Acquire Infrastructure: [Botnet](/techniques/T1583/005) <small style="color:#929393">(v1.0)</small>
* Acquire Infrastructure: [DNS Server](/techniques/T1583/002) <small style="color:#929393">(v1.0)</small>
* [Active Scanning](/techniques/T1595) <small style="color:#929393">(v1.0)</small>
    * [Scanning IP Blocks](/techniques/T1595/001) <small style="color:#929393">(v1.0)</small>
    * [Vulnerability Scanning](/techniques/T1595/002) <small style="color:#929393">(v1.0)</small>
* [Automated Exfiltration](/techniques/T1020) <small style="color:#929393">(v1.2)</small>
* [Boot or Logon Autostart Execution](/techniques/T1547) <small style="color:#929393">(v1.1)</small>
    * [Registry Run Keys / Startup Folder](/techniques/T1547/001) <small style="color:#929393">(v1.1)</small>
* [Boot or Logon Initialization Scripts](/techniques/T1037) <small style="color:#929393">(v2.1)</small>
* Command and Scripting Interpreter: [Python](/techniques/T1059/006) <small style="color:#929393">(v1.0)</small>
* Compromise Accounts: [Email Accounts](/techniques/T1586/002) <small style="color:#929393">(v1.0)</small>
* [Compromise Client Software Binary](/techniques/T1554) <small style="color:#929393">(v1.0)</small>
* Compromise Infrastructure: [Botnet](/techniques/T1584/005) <small style="color:#929393">(v1.0)</small>
* [Create or Modify System Process](/techniques/T1543) <small style="color:#929393">(v1.0)</small>
* [Credentials from Password Stores](/techniques/T1555) <small style="color:#929393">(v1.0)</small>
* [Data Manipulation](/techniques/T1565) <small style="color:#929393">(v1.0)</small>
* Data from Information Repositories: [Confluence](/techniques/T1213/001) <small style="color:#929393">(v1.0)</small>
* Data from Information Repositories: [Sharepoint](/techniques/T1213/002) <small style="color:#929393">(v1.0)</small>
* Develop Capabilities: [Exploits](/techniques/T1587/004) <small style="color:#929393">(v1.0)</small>
* [Direct Volume Access](/techniques/T1006) <small style="color:#929393">(v2.0)</small>
* [Domain Policy Modification](/techniques/T1484) <small style="color:#929393">(v2.0)</small>
    * [Group Policy Modification](/techniques/T1484/001) <small style="color:#929393">(v1.0)</small>
* Dynamic Resolution: [Domain Generation Algorithms](/techniques/T1568/002) <small style="color:#929393">(v1.0)</small>
* [Encrypted Channel](/techniques/T1573) <small style="color:#929393">(v1.0)</small>
    * [Asymmetric Cryptography](/techniques/T1573/002) <small style="color:#929393">(v1.0)</small>
* Establish Accounts: [Email Accounts](/techniques/T1585/002) <small style="color:#929393">(v1.0)</small>
* [Event Triggered Execution](/techniques/T1546) <small style="color:#929393">(v1.1)</small>
    * [AppCert DLLs](/techniques/T1546/009) <small style="color:#929393">(v1.0)</small>
    * [AppInit DLLs](/techniques/T1546/010) <small style="color:#929393">(v1.0)</small>
    * [Application Shimming](/techniques/T1546/011) <small style="color:#929393">(v1.0)</small>
    * [Component Object Model Hijacking](/techniques/T1546/015) <small style="color:#929393">(v1.0)</small>
    * [Image File Execution Options Injection](/techniques/T1546/012) <small style="color:#929393">(v1.1)</small>
    * [LC_LOAD_DYLIB Addition](/techniques/T1546/006) <small style="color:#929393">(v1.0)</small>
* [Execution Guardrails](/techniques/T1480) <small style="color:#929393">(v1.1)</small>
    * [Environmental Keying](/techniques/T1480/001) <small style="color:#929393">(v1.0)</small>
* [Exploitation of Remote Services](/techniques/T1210) <small style="color:#929393">(v1.1)</small>
* [File and Directory Discovery](/techniques/T1083) <small style="color:#929393">(v1.3)</small>
* [File and Directory Permissions Modification](/techniques/T1222) <small style="color:#929393">(v2.1)</small>
* Gather Victim Host Information: [Firmware](/techniques/T1592/003) <small style="color:#929393">(v1.0)</small>
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
* Gather Victim Org Information: [Business Relationships](/techniques/T1591/002) <small style="color:#929393">(v1.0)</small>
* Gather Victim Org Information: [Identify Business Tempo](/techniques/T1591/003) <small style="color:#929393">(v1.0)</small>
* Gather Victim Org Information: [Identify Roles](/techniques/T1591/004) <small style="color:#929393">(v1.0)</small>
* Hijack Execution Flow: [COR_PROFILER](/techniques/T1574/012) <small style="color:#929393">(v1.0)</small>
* Impair Defenses: [Impair Command History Logging](/techniques/T1562/003) <small style="color:#929393">(v2.0)</small>
* Impair Defenses: [Indicator Blocking](/techniques/T1562/006) <small style="color:#929393">(v1.0)</small>
* Indicator Removal on Host: [Network Share Connection Removal](/techniques/T1070/005) <small style="color:#929393">(v1.0)</small>
* [Input Capture](/techniques/T1056) <small style="color:#929393">(v1.2)</small>
    * [Credential API Hooking](/techniques/T1056/004) <small style="color:#929393">(v1.0)</small>
* Masquerading: [Rename System Utilities](/techniques/T1036/003) <small style="color:#929393">(v1.0)</small>
* OS Credential Dumping: [DCSync](/techniques/T1003/006) <small style="color:#929393">(v1.0)</small>
* OS Credential Dumping: [LSA Secrets](/techniques/T1003/004) <small style="color:#929393">(v1.0)</small>
* OS Credential Dumping: [NTDS](/techniques/T1003/003) <small style="color:#929393">(v1.0)</small>
* Obtain Capabilities: [Exploits](/techniques/T1588/005) <small style="color:#929393">(v1.0)</small>
* Obtain Capabilities: [Vulnerabilities](/techniques/T1588/006) <small style="color:#929393">(v1.0)</small>
* Phishing for Information: [Spearphishing Service](/techniques/T1598/001) <small style="color:#929393">(v1.0)</small>
* Process Injection: [Extra Window Memory Injection](/techniques/T1055/011) <small style="color:#929393">(v1.0)</small>
* Process Injection: [Process Doppelgänging](/techniques/T1055/013) <small style="color:#929393">(v1.0)</small>
* [Proxy](/techniques/T1090) <small style="color:#929393">(v3.1)</small>
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
* Server Software Component: [Transport Agent](/techniques/T1505/002) <small style="color:#929393">(v1.0)</small>
* [Signed Binary Proxy Execution](/techniques/T1218) <small style="color:#929393">(v2.1)</small>
* [Signed Script Proxy Execution](/techniques/T1216) <small style="color:#929393">(v1.1)</small>
* [Software Deployment Tools](/techniques/T1072) <small style="color:#929393">(v2.1)</small>
* Steal or Forge Kerberos Tickets: [AS-REP Roasting](/techniques/T1558/004) <small style="color:#929393">(v1.0)</small>
* Subvert Trust Controls: [SIP and Trust Provider Hijacking](/techniques/T1553/003) <small style="color:#929393">(v1.0)</small>
* [Supply Chain Compromise](/techniques/T1195) <small style="color:#929393">(v1.2)</small>
* [Trusted Developer Utilities Proxy Execution](/techniques/T1127) <small style="color:#929393">(v1.2)</small>
* [XSL Script Processing](/techniques/T1220) <small style="color:#929393">(v1.2)</small>

#### Unknown Changes

* Process Injection: [Proc Memory](/techniques/T1055/009) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>

#### Deprecations

* Scheduled Task/Job: [Launchd](/techniques/T1053/004) <small style="color:#929393">(v1.0)</small>

### Mobile

#### New Techniques

* [Call Control](/techniques/T1616) <small style="color:#929393">(v1.0)</small>
* [Command-Line Interface](/techniques/T1605) <small style="color:#929393">(v1.0)</small>
* [Hooking](/techniques/T1617) <small style="color:#929393">(v1.0)</small>
* [Proxy Through Victim](/techniques/T1604) <small style="color:#929393">(v1.0)</small>
* [Scheduled Task/Job](/techniques/T1603) <small style="color:#929393">(v1.0)</small>
* [User Evasion](/techniques/T1618) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* [Device Administrator Permissions](/techniques/T1401) <small style="color:#929393">(v1.1&#8594;v2.0)</small>

#### Minor Version Changes

* [Exploit SS7 to Redirect Phone Calls/SMS](/techniques/T1449) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Manipulate Device Communication](/techniques/T1463) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [SIM Card Swap](/techniques/T1451) <small style="color:#929393">(v1.1&#8594;v1.2)</small>

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
* [Transient Cyber Asset](/Technique/T0864) <small style="color:#eb6635">(v0.0)</small>
* [Wireless Sniffing](/Technique/T0887) <small style="color:#eb6635">(v0.0)</small>

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
* [Denial of Control](/Technique/T813) <small style="color:#929393">(v0.0)</small>
* [Denial of Service](/Technique/T0814) <small style="color:#929393">(v0.0)</small>
* [Detect Operating Mode](/Technique/T0868) <small style="color:#929393">(v0.0)</small>
* [Device Restart/Shutdown](/Technique/T0816) <small style="color:#929393">(v0.0)</small>
* [Drive-by Compromise](/Technique/T0817) <small style="color:#929393">(v0.0)</small>
* [Execution through API](/Technique/T0871) <small style="color:#929393">(v0.0)</small>
* [Exploit Public-Facing Application](/Technique/T0819) <small style="color:#929393">(v0.0)</small>
* [Exploitation for Evasion](/Technique/T0820) <small style="color:#929393">(v0.0)</small>
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
* [Modify Parameter](/Technique/T0836) <small style="color:#929393">(v0.0)</small>
* [Module Firmware](/Technique/T0839) <small style="color:#929393">(v0.0)</small>
* [Monitor Process State](/Technique/T0801) <small style="color:#929393">(v0.0)</small>
* [Network Connection Enumeration](/Technique/T0840) <small style="color:#929393">(v0.0)</small>
* [Network Sniffing](/Technique/T0842) <small style="color:#929393">(v0.0)</small>
* [Point & Tag Identification](/Technique/T0861) <small style="color:#929393">(v0.0)</small>
* [Program Download](/Technique/T0843) <small style="color:#929393">(v0.0)</small>
* [Program Upload](/Technique/T0845) <small style="color:#929393">(v0.0)</small>
* [Project File Infection](/Technique/T0873) <small style="color:#929393">(v0.0)</small>
* [Remote System Discovery](/Technique/T0846) <small style="color:#929393">(v0.0)</small>
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

#### Unknown Changes

* [Loss of Control](/Technique/T0827) <small style="color:#eb6635">(v0.0&#8594;v0.0)</small>

#### Deprecations

* [Change Program State](/Technique/T875) <small style="color:#929393">(v0.0)</small>
* [Control Device Identification](/Technique/T808) <small style="color:#929393">(v0.0)</small>
* [Data Historian Compromise](/Technique/T0810) <small style="color:#929393">(v0.0)</small>
* [Detect Program State](/Technique/T870) <small style="color:#929393">(v0.0)</small>
* [Engineering Workstation Compromise](/Technique/T0818) <small style="color:#929393">(v0.0)</small>
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

* [AppleJeus](/software/S0584) <small style="color:#929393">(v1.0)</small>
* [AppleSeed](/software/S0622) <small style="color:#929393">(v1.0)</small>
* [Avaddon](/software/S0640) <small style="color:#929393">(v1.0)</small>
* [BADFLICK](/software/S0642) <small style="color:#929393">(v1.0)</small>
* [BLINDINGCAN](/software/S0520) <small style="color:#929393">(v1.0)</small>
* [BLUELIGHT](/software/S0657) <small style="color:#929393">(v1.0)</small>
* [Babuk](/software/S0638) <small style="color:#929393">(v1.0)</small>
* [Bad Rabbit](/software/S0606) <small style="color:#929393">(v1.0)</small>
* [Bazar](/software/S0534) <small style="color:#eb6635">(v1.1)</small>
* [BendyBear](/software/S0574) <small style="color:#929393">(v1.0)</small>
* [BitPaymer](/software/S0570) <small style="color:#929393">(v1.0)</small>
* [BlackMould](/software/S0564) <small style="color:#929393">(v1.0)</small>
* [BoomBox](/software/S0635) <small style="color:#929393">(v1.0)</small>
* [BoxCaon](/software/S0651) <small style="color:#929393">(v1.0)</small>
* [CSPY Downloader](/software/S0527) <small style="color:#929393">(v1.0)</small>
* [Caterpillar WebShell](/software/S0572) <small style="color:#929393">(v1.0)</small>
* [Chaes](/software/S0631) <small style="color:#929393">(v1.0)</small>
* [Clop](/software/S0611) <small style="color:#929393">(v1.0)</small>
* [Conficker](/software/S0608) <small style="color:#929393">(v1.0)</small>
* [ConnectWise](/software/S0591) <small style="color:#929393">(v1.0)</small>
* [Conti](/software/S0575) <small style="color:#eb6635">(v1.1)</small>
* [CostaBricks](/software/S0614) <small style="color:#929393">(v1.0)</small>
* [Crutch](/software/S0538) <small style="color:#929393">(v1.0)</small>
* [Cuba](/software/S0625) <small style="color:#929393">(v1.0)</small>
* [DEATHRANSOM](/software/S0616) <small style="color:#929393">(v1.0)</small>
* [Doki](/software/S0600) <small style="color:#929393">(v1.0)</small>
* [DropBook](/software/S0547) <small style="color:#eb6635">(v1.1)</small>
* [Dtrack](/software/S0567) <small style="color:#929393">(v1.0)</small>
* [ECCENTRICBANDWAGON](/software/S0593) <small style="color:#929393">(v1.0)</small>
* [EKANS](/software/S0605) <small style="color:#929393">(v1.0)</small>
* [EVILNUM](/software/S0568) <small style="color:#929393">(v1.0)</small>
* [Ecipekac](/software/S0624) <small style="color:#929393">(v1.0)</small>
* [Egregor](/software/S0554) <small style="color:#929393">(v1.0)</small>
* [EnvyScout](/software/S0634) <small style="color:#929393">(v1.0)</small>
* [Explosive](/software/S0569) <small style="color:#929393">(v1.0)</small>
* [FIVEHANDS](/software/S0618) <small style="color:#929393">(v1.0)</small>
* [FYAnti](/software/S0628) <small style="color:#929393">(v1.0)</small>
* [GoldFinder](/software/S0597) <small style="color:#929393">(v1.0)</small>
* [GoldMax](/software/S0588) <small style="color:#929393">(v1.0)</small>
* [Grandoreiro](/software/S0531) <small style="color:#929393">(v1.0)</small>
* [GrimAgent](/software/S0632) <small style="color:#929393">(v1.0)</small>
* [GuLoader](/software/S0561) <small style="color:#eb6635">(v2.0)</small>
* [HELLOKITTY](/software/S0617) <small style="color:#929393">(v1.0)</small>
* [Hildegard](/software/S0601) <small style="color:#eb6635">(v1.1)</small>
* [HyperStack](/software/S0537) <small style="color:#929393">(v1.0)</small>
* [Industroyer](/software/S0604) <small style="color:#929393">(v1.0)</small>
* [IronNetInjector](/software/S0581) <small style="color:#929393">(v1.0)</small>
* [JSS Loader](/software/S0648) <small style="color:#929393">(v1.0)</small>
* [Javali](/software/S0528) <small style="color:#929393">(v1.0)</small>
* [KGH_SPY](/software/S0526) <small style="color:#929393">(v1.0)</small>
* [Kerrdown](/software/S0585) <small style="color:#eb6635">(v2.0)</small>
* [KillDisk](/software/S0607) <small style="color:#929393">(v1.0)</small>
* [Kinsing](/software/S0599) <small style="color:#eb6635">(v1.1)</small>
* [Kobalos](/software/S0641) <small style="color:#929393">(v1.0)</small>
* [LiteDuke](/software/S0513) <small style="color:#929393">(v1.0)</small>
* [LookBack](/software/S0582) <small style="color:#929393">(v1.0)</small>
* [Lucifer](/software/S0532) <small style="color:#eb6635">(v1.1)</small>
* [MarkiRAT](/software/S0652) <small style="color:#929393">(v1.0)</small>
* [MegaCortex](/software/S0576) <small style="color:#929393">(v1.0)</small>
* [Melcoz](/software/S0530) <small style="color:#929393">(v1.0)</small>
* [MoleNet](/software/S0553) <small style="color:#929393">(v1.0)</small>
* [NBTscan](/software/S0590) <small style="color:#929393">(v1.0)</small>
* [NativeZone](/software/S0637) <small style="color:#929393">(v1.0)</small>
* [Nebulae](/software/S0630) <small style="color:#929393">(v1.0)</small>
* [ObliqueRAT](/software/S0644) <small style="color:#929393">(v1.0)</small>
* [Out1](/software/S0594) <small style="color:#929393">(v1.0)</small>
* [P.A.S. Webshell](/software/S0598) <small style="color:#929393">(v1.0)</small>
* [P8RAT](/software/S0626) <small style="color:#929393">(v1.0)</small>
* [PS1](/software/S0613) <small style="color:#929393">(v1.0)</small>
* [Pay2Key](/software/S0556) <small style="color:#929393">(v1.0)</small>
* [Penquin](/software/S0587) <small style="color:#929393">(v1.0)</small>
* [Peppy](/software/S0643) <small style="color:#929393">(v1.0)</small>
* [ProLock](/software/S0654) <small style="color:#929393">(v1.0)</small>
* [Pysa](/software/S0583) <small style="color:#929393">(v1.0)</small>
* [QakBot](/software/S0650) <small style="color:#929393">(v1.0)</small>
* [RainyDay](/software/S0629) <small style="color:#929393">(v1.0)</small>
* [RemoteUtilities](/software/S0592) <small style="color:#929393">(v1.0)</small>
* [SLOTHFULMEDIA](/software/S0533) <small style="color:#929393">(v1.0)</small>
* [SMOKEDHAM](/software/S0649) <small style="color:#929393">(v1.0)</small>
* [SUPERNOVA](/software/S0578) <small style="color:#929393">(v1.0)</small>
* [Seth-Locker](/software/S0639) <small style="color:#929393">(v1.0)</small>
* [ShadowPad](/software/S0596) <small style="color:#929393">(v1.0)</small>
* [SharpStage](/software/S0546) <small style="color:#eb6635">(v1.1)</small>
* [Sibot](/software/S0589) <small style="color:#929393">(v1.0)</small>
* [SideTwist](/software/S0610) <small style="color:#929393">(v1.0)</small>
* [Siloscape](/software/S0623) <small style="color:#929393">(v1.0)</small>
* [Sliver](/software/S0633) <small style="color:#929393">(v1.0)</small>
* [SodaMaster](/software/S0627) <small style="color:#929393">(v1.0)</small>
* [SombRAT](/software/S0615) <small style="color:#929393">(v1.0)</small>
* [Spark](/software/S0543) <small style="color:#eb6635">(v1.1)</small>
* [SpicyOmelette](/software/S0646) <small style="color:#929393">(v1.0)</small>
* [Stuxnet](/software/S0603) <small style="color:#929393">(v1.0)</small>
* [TAINTEDSCRIBE](/software/S0586) <small style="color:#929393">(v1.0)</small>
* [TRITON](/software/S0609) <small style="color:#929393">(v1.0)</small>
* [ThiefQuest](/software/S0595) <small style="color:#eb6635">(v1.1)</small>
* [Turian](/software/S0647) <small style="color:#929393">(v1.0)</small>
* [VaporRage](/software/S0636) <small style="color:#929393">(v1.0)</small>
* [WastedLocker](/software/S0612) <small style="color:#929393">(v1.0)</small>
* [Waterbear](/software/S0579) <small style="color:#929393">(v1.0)</small>
* [Wevtutil](/software/S0645) <small style="color:#929393">(v1.0)</small>
* [XCSSET](/software/S0658) <small style="color:#929393">(v1.0)</small>
* [xCaon](/software/S0653) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* [Astaroth](/software/S0373) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* [Bandook](/software/S0234) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Dok](/software/S0281) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Dridex](/software/S0384) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Lokibot](/software/S0447) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Machete](/software/S0409) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* [Matryoshka](/software/S0167) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Metamorfo](/software/S0455) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [More_eggs](/software/S0284) <small style="color:#929393">(v2.1&#8594;v3.0)</small>
* [NotPetya](/software/S0368) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* [Octopus](/software/S0340) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Olympic Destroyer](/software/S0365) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* [PoetRAT](/software/S0428) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [SDBbot](/software/S0461) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [SEASHARPEE](/software/S0185) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Taidoor](/software/S0011) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [TrickBot](/software/S0266) <small style="color:#929393">(v1.3&#8594;v2.0)</small>
* [Zebrocy](/software/S0251) <small style="color:#929393">(v2.1&#8594;v3.0)</small>

#### Minor Version Changes

* [Agent Tesla](/software/S0331) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Aria-body](/software/S0456) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [BabyShark](/software/S0414) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Bisonal](/software/S0268) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [BlackEnergy](/software/S0089) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [BloodHound](/software/S0521) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Bundlore](/software/S0482) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Carberp](/software/S0484) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Carbon](/software/S0335) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [ComRAT](/software/S0126) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Crimson](/software/S0115) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Ebury](/software/S0377) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Emissary](/software/S0082) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [EvilBunny](/software/S0396) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Exaramel for Linux](/software/S0401) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [FALLCHILL](/software/S0181) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [FatDuke](/software/S0512) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Fysbis](/software/S0410) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Gazer](/software/S0168) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [HTRAN](/software/S0040) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [HiddenWasp](/software/S0394) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Hikit](/software/S0009) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Impacket](/software/S0357) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Kazuar](/software/S0265) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Keydnap](/software/S0276) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [LoudMiner](/software/S0451) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Maze](/software/S0449) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [MimiPenguin](/software/S0179) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [MiniDuke](/software/S0051) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Nltest](/software/S0359) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [OSX/Shlayer](/software/S0402) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [OwaAuth](/software/S0072) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Proton](/software/S0279) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [PsExec](/software/S0029) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [QuasarRAT](/software/S0262) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [RGDoor](/software/S0258) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [ROKRAT](/software/S0240) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [Ragnar Locker](/software/S0481) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Raindrop](/software/S0565) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Ramsay](/software/S0458) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [SUNSPOT](/software/S0562) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [SynAck](/software/S0242) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [TEARDROP](/software/S0560) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Ursnif](/software/S0386) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Valak](/software/S0476) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Zeus Panda](/software/S0330) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [certutil](/software/S0160) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [esentutl](/software/S0404) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [gh0st RAT](/software/S0032) <small style="color:#929393">(v2.2&#8594;v2.3)</small>

#### Other Version Changes

* [China Chopper](/software/S0020) <small style="color:#eb6635">(v2.1&#8594;v2.3)</small>
* [Cobalt Strike](/software/S0154) <small style="color:#eb6635">(v1.5&#8594;v1.7)</small>
* [Empire](/software/S0363) <small style="color:#eb6635">(v1.1&#8594;v1.3)</small>
* [LaZagne](/software/S0349) <small style="color:#eb6635">(v1.1&#8594;v1.3)</small>
* [Mimikatz](/software/S0002) <small style="color:#eb6635">(v1.2&#8594;v1.4)</small>
* [NETWIRE](/software/S0198) <small style="color:#eb6635">(v1.2&#8594;v1.4)</small>
* [Net](/software/S0039) <small style="color:#eb6635">(v2.1&#8594;v2.3)</small>
* [OSX_OCEANLOTUS.D](/software/S0352) <small style="color:#eb6635">(v1.2&#8594;v2.1)</small>
* [PoisonIvy](/software/S0012) <small style="color:#eb6635">(v1.1&#8594;v1.3)</small>
* [PowerSploit](/software/S0194) <small style="color:#eb6635">(v1.2&#8594;v1.4)</small>
* [REvil](/software/S0496) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
* [Ryuk](/software/S0446) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
* [SUNBURST](/software/S0559) <small style="color:#eb6635">(v1.0&#8594;v2.1)</small>

#### Metadata-only Changes

* [BADNEWS](/software/S0128) <small style="color:#929393">(v1.2)</small>
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
* [HyperBro](/software/S0398) <small style="color:#929393">(v1.1)</small>
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
* [Reg](/software/S0075) <small style="color:#929393">(v1.0)</small>
* [SeaDuke](/software/S0053) <small style="color:#929393">(v1.1)</small>
* [Shamoon](/software/S0140) <small style="color:#929393">(v2.1)</small>
* [TURNEDUP](/software/S0199) <small style="color:#929393">(v1.1)</small>
* [TinyZBot](/software/S0004) <small style="color:#929393">(v1.1)</small>
* [Vasport](/software/S0207) <small style="color:#929393">(v1.1)</small>
* [WellMess](/software/S0514) <small style="color:#929393">(v1.0)</small>
* [Wiarp](/software/S0206) <small style="color:#929393">(v1.1)</small>
* [WindTail](/software/S0466) <small style="color:#929393">(v1.0)</small>
* [jRAT](/software/S0283) <small style="color:#929393">(v2.1)</small>
* [meek](/software/S0175) <small style="color:#929393">(v1.0)</small>
* [spwebmember](/software/S0227) <small style="color:#929393">(v1.1)</small>
* [zwShell](/software/S0350) <small style="color:#929393">(v1.1)</small>

#### Unknown Changes

* [Get2](/software/S0460) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>

### Mobile

#### New Software

* [Android/AdDisplay.Ashas](/software/S0525) <small style="color:#929393">(v1.0)</small>
* [AndroidOS/MalLocker.B](/software/S0524) <small style="color:#929393">(v1.0)</small>
* [Asacub](/software/S0540) <small style="color:#929393">(v1.0)</small>
* [BusyGasper](/software/S0655) <small style="color:#929393">(v1.0)</small>
* [CHEMISTGAMES](/software/S0555) <small style="color:#929393">(v1.0)</small>
* [CarbonSteal](/software/S0529) <small style="color:#eb6635">(v1.1)</small>
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

* [Desert Scorpion](/software/S0505) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Monokle](/software/S0407) <small style="color:#929393">(v1.1&#8594;v1.2)</small>

#### Other Version Changes

* [Anubis](/software/S0422) <small style="color:#eb6635">(v1.1&#8594;v1.3)</small>

### ICS

#### New Software

* [Bad Rabbit](/software/S0606) <small style="color:#929393">(v1.0)</small>
* [BlackEnergy](/software/S0089) <small style="color:#eb6635">(v1.3)</small>
* [Conficker](/software/S0608) <small style="color:#929393">(v1.0)</small>
* [EKANS](/software/S0605) <small style="color:#929393">(v1.0)</small>
* [Industroyer](/software/S0604) <small style="color:#929393">(v1.0)</small>
* [KillDisk](/software/S0607) <small style="color:#929393">(v1.0)</small>
* [REvil](/software/S0496) <small style="color:#eb6635">(v1.2)</small>
* [Stuxnet](/software/S0603) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* [NotPetya](/software/S0368) <small style="color:#929393">(v1.2&#8594;v2.0)</small>

#### Other Version Changes

* [Ryuk](/software/S0446) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>

#### Deletions

* Bad Rabbit <small style="color:#eb6635">(v1.0)</small>
* BlackEnergy 3 <small style="color:#eb6635">(v1.0)</small>
* Conficker <small style="color:#eb6635">(v1.0)</small>
* Industroyer <small style="color:#eb6635">(v1.0)</small>
* Killdisk <small style="color:#eb6635">(v1.0)</small>
* Stuxnet <small style="color:#eb6635">(v1.0)</small>

## Groups

### Enterprise

#### New Groups

* [Ajax Security Team](/groups/G0130) <small style="color:#929393">(v1.0)</small>
* [Andariel](/groups/G0138) <small style="color:#929393">(v1.0)</small>
* [BackdoorDiplomacy](/groups/G0135) <small style="color:#929393">(v1.0)</small>
* [CostaRicto](/groups/G0132) <small style="color:#929393">(v1.0)</small>
* [Evilnum](/groups/G0120) <small style="color:#929393">(v1.0)</small>
* [Ferocious Kitten](/groups/G0137) <small style="color:#929393">(v1.0)</small>
* [Fox Kitten](/groups/G0117) <small style="color:#929393">(v1.0)</small>
* [HAFNIUM](/groups/G0125) <small style="color:#929393">(v1.0)</small>
* [Higaisa](/groups/G0126) <small style="color:#929393">(v1.0)</small>
* [IndigoZebra](/groups/G0136) <small style="color:#929393">(v1.0)</small>
* [Indrik Spider](/groups/G0119) <small style="color:#eb6635">(v2.0)</small>
* [Mustang Panda](/groups/G0129) <small style="color:#eb6635">(v1.1)</small>
* [Nomadic Octopus](/groups/G0133) <small style="color:#929393">(v1.0)</small>
* [Operation Wocao](/groups/G0116) <small style="color:#929393">(v1.0)</small>
* [Sidewinder](/groups/G0121) <small style="color:#929393">(v1.0)</small>
* [Silent Librarian](/groups/G0122) <small style="color:#929393">(v1.0)</small>
* [TA551](/groups/G0127) <small style="color:#eb6635">(v1.1)</small>
* [TeamTNT](/groups/G0139) <small style="color:#929393">(v1.0)</small>
* [Tonto Team](/groups/G0131) <small style="color:#929393">(v1.0)</small>
* [Transparent Tribe](/groups/G0134) <small style="color:#929393">(v1.0)</small>
* [Volatile Cedar](/groups/G0123) <small style="color:#929393">(v1.0)</small>
* [Windigo](/groups/G0124) <small style="color:#929393">(v1.0)</small>
* [ZIRCONIUM](/groups/G0128) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* [APT37](/groups/G0067) <small style="color:#929393">(v1.5&#8594;v2.0)</small>
* [APT38](/groups/G0082) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* [Carbanak](/groups/G0008) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Cobalt Group](/groups/G0080) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* [Darkhotel](/groups/G0012) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* [FIN7](/groups/G0046) <small style="color:#929393">(v1.5&#8594;v2.0)</small>
* [GALLIUM](/groups/G0093) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Lazarus Group](/groups/G0032) <small style="color:#929393">(v1.4&#8594;v2.0)</small>
* [Leviathan](/groups/G0065) <small style="color:#929393">(v2.1&#8594;v3.0)</small>
* [Machete](/groups/G0095) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* [Molerats](/groups/G0021) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [MuddyWater](/groups/G0069) <small style="color:#929393">(v2.3&#8594;v3.0)</small>
* [Naikon](/groups/G0019) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Wizard Spider](/groups/G0102) <small style="color:#929393">(v1.2&#8594;v2.0)</small>

#### Minor Version Changes

* [APT-C-36](/groups/G0099) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [APT1](/groups/G0006) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [APT19](/groups/G0073) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [APT3](/groups/G0022) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [APT33](/groups/G0064) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [BlackTech](/groups/G0098) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Blue Mockingbird](/groups/G0108) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Cleaver](/groups/G0003) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Dark Caracal](/groups/G0070) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [DarkHydrus](/groups/G0079) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [DarkVishnya](/groups/G0105) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Dragonfly](/groups/G0035) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Elderwood](/groups/G0066) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [FIN10](/groups/G0051) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [FIN4](/groups/G0085) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [FIN5](/groups/G0053) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [FIN8](/groups/G0061) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Frankenstein](/groups/G0101) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [GOLD SOUTHFIELD](/groups/G0115) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Gorgon Group](/groups/G0078) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [Inception](/groups/G0100) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Ke3chang](/groups/G0004) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Leafminer](/groups/G0077) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* [Night Dragon](/groups/G0014) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [PLATINUM](/groups/G0068) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Patchwork](/groups/G0040) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [PittyTiger](/groups/G0011) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Stealth Falcon](/groups/G0038) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [TEMP.Veles](/groups/G0088) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Thrip](/groups/G0076) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Tropic Trooper](/groups/G0081) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [WIRTE](/groups/G0090) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Whitefly](/groups/G0107) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Windshift](/groups/G0112) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

#### Other Version Changes

* [APT28](/groups/G0007) <small style="color:#eb6635">(v3.0&#8594;v3.2)</small>
* [APT29](/groups/G0016) <small style="color:#eb6635">(v1.4&#8594;v2.1)</small>
* [APT32](/groups/G0050) <small style="color:#eb6635">(v2.3&#8594;v2.5)</small>
* [APT39](/groups/G0087) <small style="color:#eb6635">(v2.3&#8594;v3.1)</small>
* [APT41](/groups/G0096) <small style="color:#eb6635">(v1.1&#8594;v3.0)</small>
* [BRONZE BUTLER](/groups/G0060) <small style="color:#eb6635">(v1.1&#8594;v1.3)</small>
* [Chimera](/groups/G0114) <small style="color:#eb6635">(v1.0&#8594;v2.1)</small>
* [CopyKittens](/groups/G0052) <small style="color:#eb6635">(v1.3&#8594;v1.5)</small>
* [Dragonfly 2.0](/groups/G0074) <small style="color:#eb6635">(v1.3&#8594;v2.1)</small>
* [FIN6](/groups/G0037) <small style="color:#eb6635">(v3.0&#8594;v3.2)</small>
* [Kimsuky](/groups/G0094) <small style="color:#eb6635">(v1.1&#8594;v3.0)</small>
* [Magic Hound](/groups/G0059) <small style="color:#eb6635">(v2.0&#8594;v4.0)</small>
* [OilRig](/groups/G0049) <small style="color:#eb6635">(v1.4&#8594;v3.0)</small>
* [Sandworm Team](/groups/G0034) <small style="color:#eb6635">(v1.0&#8594;v2.1)</small>
* [Silence](/groups/G0091) <small style="color:#eb6635">(v1.1&#8594;v2.1)</small>
* [TA505](/groups/G0092) <small style="color:#eb6635">(v1.1&#8594;v1.3)</small>
* [Threat Group-3390](/groups/G0027) <small style="color:#eb6635">(v1.3&#8594;v1.5)</small>
* [Turla](/groups/G0010) <small style="color:#eb6635">(v1.4&#8594;v2.1)</small>
* [menuPass](/groups/G0045) <small style="color:#eb6635">(v1.5&#8594;v2.1)</small>

#### Metadata-only Changes

* [Deep Panda](/groups/G0009) <small style="color:#929393">(v1.2)</small>
* [Gamaredon Group](/groups/G0047) <small style="color:#929393">(v1.2)</small>

#### Revocations

* Stolen Pencil (revoked by [Kimsuky](/groups/G0094)) <small style="color:#929393">(v0.0)</small>
* UNC2452 (revoked by [APT29](/groups/G0016)) <small style="color:#929393">(v0.0)</small>

#### Deprecations

* [Taidoor](/groups/G0015) <small style="color:#929393">(v1.0)</small>

#### Deletions

* Charming Kitten <small style="color:#eb6635">(v1.0)</small>

### Mobile

#### New Groups

* [Sandworm Team](/groups/G0034) <small style="color:#eb6635">(v2.1)</small>
* [Windshift](/groups/G0112) <small style="color:#eb6635">(v1.1)</small>

#### Minor Version Changes

* [Dark Caracal](/groups/G0070) <small style="color:#929393">(v1.2&#8594;v1.3)</small>

#### Other Version Changes

* [APT28](/groups/G0007) <small style="color:#eb6635">(v3.0&#8594;v3.2)</small>

### ICS

#### Major Version Changes

* [Lazarus Group](/groups/G0032) <small style="color:#929393">(v1.4&#8594;v2.0)</small>

#### Minor Version Changes

* [APT33](/groups/G0064) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Dragonfly](/groups/G0035) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [TEMP.Veles](/groups/G0088) <small style="color:#929393">(v1.2&#8594;v1.3)</small>

#### Other Version Changes

* [Dragonfly 2.0](/groups/G0074) <small style="color:#eb6635">(v1.3&#8594;v2.1)</small>
* [OilRig](/groups/G0049) <small style="color:#eb6635">(v1.4&#8594;v3.0)</small>
* [Sandworm Team](/groups/G0034) <small style="color:#eb6635">(v1.0&#8594;v2.1)</small>

#### Deletions

* Leafminer <small style="color:#eb6635">(v1.0)</small>

## Campaigns

### Enterprise

### Mobile

### ICS

## Mitigations

### Enterprise

#### New Mitigations

* [Data Loss Prevention](/mitigations/M1057) <small style="color:#929393">(v1.0)</small>

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
* [Network Segmentation](/Mitigation/M0930) <small style="color:#929393">(v1.0)</small>
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
* Abel Morales, Exabeam
* Achute Sharma, Keysight
* Alex Soler, AttackIQ
* Alexandros Pappas
* Alfredo Oliveira, Trend Micro
* Anastasios Pingios
* Antonio Villani, @LDO_CyberSec, Leonardo's Cyber Security Division
* Ariel Shuper, Cisco
* Arnim Rupp, Deutsche Lufthansa AG
* Assaf Morag, @MoragAssaf, Team Nautilus Aqua Security
* Atul Nair, Qualys
* Austin Clark
* Ayan Saha, Keysight
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
* Christoffer Strömblad
* Christopher Glyer, Mandiant, @cglyer
* Cody Thomas, SpecterOps
* CTID
* Cybereason Nocturnus, @nocturnus
* Dan Borges, @1njection
* Daniel Prizmant, Palo Alto Networks
* Daniel Stepanic, Elastic
* Daniyal Naeem, BT Security
* David Fiser, @anu4is, Trend Micro
* David French, Elastic
* Dor Edry, Microsoft
* Edward Millington
* Eli Salem, @elisalem9
* Erik Schamper, @Schamperr, Fox-IT
* ExtraHop
* FIRST.ORG's Cyber Threat Intelligence SIG
* Gaetan van Diemen, ThreatFabric
* Gal Singer, @galsinger29, Team Nautilus Aqua Security
* Gareth Phillips, Seek Ltd.
* Gordon Long, Box, Inc., @ethicalhax
* Harry Kim, CODEMIZE
* Harry, CODEMIZE
* Harshal Tupsamudre, Qualys
* Hiroki Nagahama, NEC Corporation
* ICSCoE Japan
* Idan Frimark, Cisco
* Idan Revivo, @idanr86, Team Nautilus Aqua Security
* Isif Ibrahima
* Itamar Mizrahi, Cymptom
* Ivan Sinyakov
* Janantha Marasinghe
* Jaron Bradley @jbradley89
* Jay Chen, Palo Alto Networks
* Jeff Felling, Red Canary
* Jen Burns, HubSpot
* Joas Antonio dos Santos, @C0d3Cr4zy
* Joas Antonio dos Santos, @C0d3Cr4zy, Inmetrics
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
* Katie Nickels, Red Canary
* Kiyohito Yamamoto, RedLark, NTT Communications
* Kobi Haimovich, CardinalOps
* Kyaw Pyiyt Htet, @KyawPyiytHtet
* Kyoung-ju Kwak (S2W)
* Lacework Labs
* Lior Ribak , SentinelOne
* Lorin Wu, Trend Micro
* Maarten van Dantzig, @MaartenVDantzig, Fox-IT
* Magno Logan, @magnologan, Trend Micro
* Manikantan Srinivasan, NEC Corporation India
* Maril Vernon @shewhohacks
* Martin Sohn Christensen, Improsec
* Matt Brenton, Zurich Global Information Security
* Matt Brenton, Zurich Insurance Group
* Matt Burrough, @mattburrough, Microsoft
* Mayuresh Dani, Qualys
* Michael Katchinskiy, @michael64194968, Team Nautilus Aqua Security
* Microsoft Detection and Response Team (DART)
* Microsoft Security
* Mike Burns, Mandiant
* Mnemonic AS
* Mugdha Peter Bansode
* Nagahama Hiroki, NEC Corporation
* Nathaniel Quist, Palo Alto Networks
* Naveen Vijayaraghavan, Nilesh Dherange (Gurucul)
* Nick Carr, Mandiant
* Nino Verde, @LDO_CyberSec, Leonardo's Cyber Security Division
* Oleg Kolesnikov, Securonix
* Omkar Gudhate
* Patrick Sungbahadoor
* Pawan Kinger, @kingerpawan, Trend Micro
* Philip Winther
* Pooja Natarajan, NEC Corporation India
* Prasad Somasamudram, McAfee
* Prasanth Sadanala, Cigna Information Protection (CIP) - Threat Response Engineering Team
* Regina Elwell
* Rex Guo, @Xiaofei_REX, Confluera
* Rick Cole, Mandiant
* Robert Wilson
* Roi Kol, @roykol1, Team Nautilus Aqua Security
* Rory McCune, Aqua Security
* Ruben Dodge, @shotgunner101
* Ryo Tamura, SecureBrain Corporation
* Sekhar Sarukkai, McAfee 
* Shlomi Salem, SentinelOne
* Shotaro Hamamoto, NEC Solution Innovators, Ltd
* Shuhei Sasada, Cyber Defense Institute, Inc
* Silvio La Porta, @LDO_CyberSec, Leonardo's Cyber Security Division
* SOCCRATES
* Stan Hegt, Outflank
* Syed Ummar Farooqh, McAfee
* Takuma Matsumoto, LAC Co., Ltd
* Ted Samuels, Rapid7
* The DFIR Report, @TheDFIRReport
* Thijn Bukkems, Amazon
* Tim (Wadhwa-)Brown
* Toby Kohlenberg
* Tony Lambert, Red Canary
* Vadim Khrykov
* Varonis Threat Labs
* Viren Chaudhari, Qualys
* Vishwas Manral, McAfee
* Wayne Silva, F-Secure Countercept
* Wes Hurd
* Will Thomas, Cyjax
* William Cain
* Yaniv Agman, @AgmanYaniv, Team Nautilus Aqua Security
* Yoshihiro Kori, NEC Corporation
* Yossi Nisani, Cymptom
* Yossi Weizman, Azure Defender Research Team
* Yusuke Kubo, RedLark, NTT Communications
* Yusuke Niwa, ITOCHU Corporation
* Yuval Avrahami, Palo Alto Networks
* Zaw Min Htun, @Z3TAE
* Ziv Karliner, @ziv_kr, Team Nautilus Aqua Security
* Ziv Kaspersky, Cymptom
