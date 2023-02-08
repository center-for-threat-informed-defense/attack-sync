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

* Account Manipulation: [Device Registration](/techniques/T1098/005) <small style="color:#929393">(v1.0)</small>
* Active Scanning: [Wordlist Scanning](/techniques/T1595/003) <small style="color:#929393">(v1.0)</small>
* Adversary-in-the-Middle: [DHCP Spoofing](/techniques/T1557/003) <small style="color:#929393">(v1.0)</small>
* Boot or Logon Autostart Execution: [Login Items](/techniques/T1547/015) <small style="color:#929393">(v1.0)</small>
* [Cloud Storage Object Discovery](/techniques/T1619) <small style="color:#929393">(v1.0)</small>
* Data from Information Repositories: [Code Repositories](/techniques/T1213/003) <small style="color:#929393">(v1.0)</small>
* [Debugger Evasion](/techniques/T1622) <small style="color:#929393">(v1.0)</small>
* [Group Policy Discovery](/techniques/T1615) <small style="color:#929393">(v1.0)</small>
* Hide Artifacts: [Email Hiding Rules](/techniques/T1564/008) <small style="color:#eb6635">(v1.1)</small>
* Hide Artifacts: [Process Argument Spoofing](/techniques/T1564/010) <small style="color:#929393">(v1.0)</small>
* Hide Artifacts: [Resource Forking](/techniques/T1564/009) <small style="color:#929393">(v1.0)</small>
* Hijack Execution Flow: [KernelCallbackTable](/techniques/T1574/013) <small style="color:#929393">(v1.0)</small>
* Impair Defenses: [Downgrade Attack](/techniques/T1562/010) <small style="color:#eb6635">(v1.1)</small>
* Impair Defenses: [Safe Mode Boot](/techniques/T1562/009) <small style="color:#929393">(v1.0)</small>
* Inter-Process Communication: [XPC Services](/techniques/T1559/003) <small style="color:#929393">(v1.0)</small>
* Masquerading: [Double File Extension](/techniques/T1036/007) <small style="color:#929393">(v1.0)</small>
* Modify Authentication Process: [Reversible Encryption](/techniques/T1556/005) <small style="color:#929393">(v1.0)</small>
* [Multi-Factor Authentication Request Generation](/techniques/T1621) <small style="color:#929393">(v1.0)</small>
* Obfuscated Files or Information: [HTML Smuggling](/techniques/T1027/006) <small style="color:#929393">(v1.0)</small>
* [Plist File Modification](/techniques/T1647) <small style="color:#929393">(v1.0)</small>
* Process Injection: [ListPlanting](/techniques/T1055/015) <small style="color:#929393">(v1.0)</small>
* [Reflective Code Loading](/techniques/T1620) <small style="color:#929393">(v1.0)</small>
* Server Software Component: [IIS Components](/techniques/T1505/004) <small style="color:#929393">(v1.0)</small>
* Server Software Component: [Terminal Services DLL](/techniques/T1505/005) <small style="color:#929393">(v1.0)</small>
* System Binary Proxy Execution: [MMC](/techniques/T1218/014) <small style="color:#eb6635">(v2.0)</small>
* System Binary Proxy Execution: [Mavinject](/techniques/T1218/013) <small style="color:#eb6635">(v2.0)</small>
* System Location Discovery: [System Language Discovery](/techniques/T1614/001) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* Account Manipulation: [Additional Cloud Roles](/techniques/T1098/003) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* Account Manipulation: [Additional Email Delegate Permissions](/techniques/T1098/002) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* Boot or Logon Initialization Scripts: [Login Hook](/techniques/T1037/002) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Browser Session Hijacking](/techniques/T1185) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* Exfiltration Over Alternative Protocol: [Exfiltration Over Unencrypted Non-C2 Protocol](/techniques/T1048/003) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Multi-Factor Authentication Interception](/techniques/T1111) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Network Service Discovery](/techniques/T1046) <small style="color:#929393">(v2.2&#8594;v3.0)</small>
* Scheduled Task/Job: [At](/techniques/T1053/002) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [System Binary Proxy Execution](/techniques/T1218) <small style="color:#929393">(v2.1&#8594;v3.0)</small>
    * [CMSTP](/techniques/T1218/003) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
    * [Compiled HTML File](/techniques/T1218/001) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
    * [Control Panel](/techniques/T1218/002) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
    * [InstallUtil](/techniques/T1218/004) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
    * [Mshta](/techniques/T1218/005) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
    * [Msiexec](/techniques/T1218/007) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
    * [Odbcconf](/techniques/T1218/008) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
    * [Regsvcs/Regasm](/techniques/T1218/009) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
    * [Regsvr32](/techniques/T1218/010) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
    * [Rundll32](/techniques/T1218/011) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
    * [Verclsid](/techniques/T1218/012) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [System Script Proxy Execution](/techniques/T1216) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
    * [PubPrn](/techniques/T1216/001) <small style="color:#929393">(v1.0&#8594;v2.0)</small>

#### Minor Version Changes

* Abuse Elevation Control Mechanism: [Setuid and Setgid](/techniques/T1548/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Access Token Manipulation: [Create Process with Token](/techniques/T1134/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Account Access Removal](/techniques/T1531) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Account Discovery: [Local Account](/techniques/T1087/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Account Manipulation](/techniques/T1098) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
    * [Additional Cloud Credentials](/techniques/T1098/001) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
    * [SSH Authorized Keys](/techniques/T1098/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Acquire Infrastructure](/techniques/T1583) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Domains](/techniques/T1583/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Server](/techniques/T1583/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Virtual Private Server](/techniques/T1583/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Web Services](/techniques/T1583/006) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Adversary-in-the-Middle: [ARP Cache Poisoning](/techniques/T1557/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Application Window Discovery](/techniques/T1010) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Archive Collected Data: [Archive via Utility](/techniques/T1560/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Automated Collection](/techniques/T1119) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Automated Exfiltration: [Traffic Duplication](/techniques/T1020/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Boot or Logon Autostart Execution: [Port Monitors](/techniques/T1547/010) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Boot or Logon Autostart Execution: [Re-opened Applications](/techniques/T1547/007) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Brute Force: [Password Cracking](/techniques/T1110/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Brute Force: [Password Guessing](/techniques/T1110/001) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Command and Scripting Interpreter: [JavaScript](/techniques/T1059/007) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Command and Scripting Interpreter: [Network Device CLI](/techniques/T1059/008) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Command and Scripting Interpreter: [Unix Shell](/techniques/T1059/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Command and Scripting Interpreter: [Windows Command Shell](/techniques/T1059/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Compromise Accounts](/techniques/T1586) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Social Media Accounts](/techniques/T1586/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Compromise Infrastructure: [Server](/techniques/T1584/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Compromise Infrastructure: [Virtual Private Server](/techniques/T1584/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Compromise Infrastructure: [Web Services](/techniques/T1584/006) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Container Administration Command](/techniques/T1609) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Create Account: [Cloud Account](/techniques/T1136/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Create Account: [Local Account](/techniques/T1136/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Create or Modify System Process](/techniques/T1543) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Launch Daemon](/techniques/T1543/004) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Windows Service](/techniques/T1543/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Credentials from Password Stores: [Keychain](/techniques/T1555/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Credentials from Password Stores: [Securityd Memory](/techniques/T1555/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Data Manipulation](/techniques/T1565) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Runtime Data Manipulation](/techniques/T1565/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Stored Data Manipulation](/techniques/T1565/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Transmitted Data Manipulation](/techniques/T1565/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Data Staged](/techniques/T1074) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
    * [Local Data Staging](/techniques/T1074/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Data from Information Repositories](/techniques/T1213) <small style="color:#929393">(v3.1&#8594;v3.2)</small>
* [Data from Removable Media](/techniques/T1025) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Defacement](/techniques/T1491) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
    * [External Defacement](/techniques/T1491/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Internal Defacement](/techniques/T1491/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Deploy Container](/techniques/T1610) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Develop Capabilities](/techniques/T1587) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Code Signing Certificates](/techniques/T1587/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Digital Certificates](/techniques/T1587/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Malware](/techniques/T1587/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Email Collection](/techniques/T1114) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
    * [Email Forwarding Rule](/techniques/T1114/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Endpoint Denial of Service: [Application Exhaustion Flood](/techniques/T1499/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Endpoint Denial of Service: [Application or System Exploitation](/techniques/T1499/004) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Endpoint Denial of Service: [OS Exhaustion Flood](/techniques/T1499/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Endpoint Denial of Service: [Service Exhaustion Flood](/techniques/T1499/002) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Establish Accounts](/techniques/T1585) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Social Media Accounts](/techniques/T1585/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Event Triggered Execution: [PowerShell Profile](/techniques/T1546/013) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Event Triggered Execution: [Unix Shell Configuration Modification](/techniques/T1546/004) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Event Triggered Execution: [Windows Management Instrumentation Event Subscription](/techniques/T1546/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Exfiltration Over Alternative Protocol](/techniques/T1048) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
    * [Exfiltration Over Asymmetric Encrypted Non-C2 Protocol](/techniques/T1048/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Exfiltration Over C2 Channel](/techniques/T1041) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Exfiltration Over Other Network Medium: [Exfiltration Over Bluetooth](/techniques/T1011/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Exfiltration Over Physical Medium](/techniques/T1052) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Exfiltration over USB](/techniques/T1052/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Exfiltration Over Web Service](/techniques/T1567) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [External Remote Services](/techniques/T1133) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* [File and Directory Discovery](/techniques/T1083) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* File and Directory Permissions Modification: [Linux and Mac File and Directory Permissions Modification](/techniques/T1222/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Firmware Corruption](/techniques/T1495) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Forge Web Credentials](/techniques/T1606) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [SAML Tokens](/techniques/T1606/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Web Cookies](/techniques/T1606/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Gather Victim Host Information](/techniques/T1592) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Client Configurations](/techniques/T1592/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Hardware](/techniques/T1592/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Software](/techniques/T1592/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Gather Victim Identity Information: [Email Addresses](/techniques/T1589/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Gather Victim Org Information](/techniques/T1591) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Determine Physical Locations](/techniques/T1591/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Hide Artifacts](/techniques/T1564) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Hidden Window](/techniques/T1564/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Run Virtual Instance](/techniques/T1564/006) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [VBA Stomping](/techniques/T1564/007) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Hijack Execution Flow](/techniques/T1574) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Services Registry Permissions Weakness](/techniques/T1574/011) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Impair Defenses](/techniques/T1562) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Disable Cloud Logs](/techniques/T1562/008) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Disable Windows Event Logging](/techniques/T1562/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Disable or Modify Tools](/techniques/T1562/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Impair Command History Logging](/techniques/T1562/003) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Implant Internal Image](/techniques/T1525) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Indicator Removal on Host](/techniques/T1070) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
    * [Clear Command History](/techniques/T1070/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Clear Windows Event Logs](/techniques/T1070/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [File Deletion](/techniques/T1070/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Ingress Tool Transfer](/techniques/T1105) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Inhibit System Recovery](/techniques/T1490) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Inter-Process Communication: [Component Object Model](/techniques/T1559/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Internal Spearphishing](/techniques/T1534) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Masquerading: [Masquerade Task or Service](/techniques/T1036/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Masquerading: [Right-to-Left Override](/techniques/T1036/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Modify Authentication Process](/techniques/T1556) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Native API](/techniques/T1106) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Network Boundary Bridging](/techniques/T1599) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Network Denial of Service: [Direct Network Flood](/techniques/T1498/001) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Network Denial of Service: [Reflection Amplification](/techniques/T1498/002) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Network Share Discovery](/techniques/T1135) <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* [Network Sniffing](/techniques/T1040) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [OS Credential Dumping](/techniques/T1003) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
    * [LSASS Memory](/techniques/T1003/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [NTDS](/techniques/T1003/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Obfuscated Files or Information](/techniques/T1027) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Binary Padding](/techniques/T1027/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Indicator Removal from Tools](/techniques/T1027/005) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
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
* [Peripheral Device Discovery](/techniques/T1120) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Permission Groups Discovery](/techniques/T1069) <small style="color:#929393">(v2.3&#8594;v2.4)</small>
    * [Cloud Groups](/techniques/T1069/003) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Phishing](/techniques/T1566) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
    * [Spearphishing Attachment](/techniques/T1566/001) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
    * [Spearphishing Link](/techniques/T1566/002) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* Phishing for Information: [Spearphishing Link](/techniques/T1598/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Pre-OS Boot: [Component Firmware](/techniques/T1542/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Process Injection](/techniques/T1055) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Asynchronous Procedure Call](/techniques/T1055/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Dynamic-link Library Injection](/techniques/T1055/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Portable Executable Injection](/techniques/T1055/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Ptrace System Calls](/techniques/T1055/008) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Thread Execution Hijacking](/techniques/T1055/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Thread Local Storage](/techniques/T1055/005) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Remote Access Software](/techniques/T1219) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Remote Services](/techniques/T1021) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Distributed Component Object Model](/techniques/T1021/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Remote Desktop Protocol](/techniques/T1021/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [SSH](/techniques/T1021/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [VNC](/techniques/T1021/005) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Windows Remote Management](/techniques/T1021/006) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Replication Through Removable Media](/techniques/T1091) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Resource Hijacking](/techniques/T1496) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Rogue Domain Controller](/techniques/T1207) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Scheduled Task/Job](/techniques/T1053) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
    * [Cron](/techniques/T1053/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Scheduled Task](/techniques/T1053/005) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Systemd Timers](/techniques/T1053/006) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Server Software Component: [Web Shell](/techniques/T1505/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Shared Modules](/techniques/T1129) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Software Discovery: [Security Software Discovery](/techniques/T1518/001) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Stage Capabilities](/techniques/T1608) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Install Digital Certificate](/techniques/T1608/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Link Target](/techniques/T1608/005) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Upload Malware](/techniques/T1608/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Upload Tool](/techniques/T1608/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Steal Application Access Token](/techniques/T1528) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Steal Web Session Cookie](/techniques/T1539) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Steal or Forge Kerberos Tickets: [Kerberoasting](/techniques/T1558/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Subvert Trust Controls](/techniques/T1553) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Gatekeeper Bypass](/techniques/T1553/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Install Root Certificate](/techniques/T1553/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Mark-of-the-Web Bypass](/techniques/T1553/005) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Supply Chain Compromise: [Compromise Hardware Supply Chain](/techniques/T1195/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Supply Chain Compromise: [Compromise Software Dependencies and Development Tools](/techniques/T1195/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Supply Chain Compromise: [Compromise Software Supply Chain](/techniques/T1195/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [System Network Connections Discovery](/techniques/T1049) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* [System Owner/User Discovery](/techniques/T1033) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* System Services: [Launchctl](/techniques/T1569/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* System Services: [Service Execution](/techniques/T1569/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [System Shutdown/Reboot](/techniques/T1529) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Taint Shared Content](/techniques/T1080) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Template Injection](/techniques/T1221) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Traffic Signaling](/techniques/T1205) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* [Transfer Data to Cloud Account](/techniques/T1537) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Trusted Developer Utilities Proxy Execution: [MSBuild](/techniques/T1127/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Unsecured Credentials: [Bash History](/techniques/T1552/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Unsecured Credentials: [Cloud Instance Metadata API](/techniques/T1552/005) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Unsecured Credentials: [Container API](/techniques/T1552/007) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Use Alternate Authentication Material](/techniques/T1550) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Application Access Token](/techniques/T1550/001) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
    * [Web Session Cookie](/techniques/T1550/004) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* User Execution: [Malicious Image](/techniques/T1204/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Valid Accounts: [Domain Accounts](/techniques/T1078/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Valid Accounts: [Local Accounts](/techniques/T1078/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Video Capture](/techniques/T1125) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Virtualization/Sandbox Evasion](/techniques/T1497) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
    * [System Checks](/techniques/T1497/001) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
    * [Time Based Evasion](/techniques/T1497/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [User Activity Based Checks](/techniques/T1497/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Windows Management Instrumentation](/techniques/T1047) <small style="color:#929393">(v1.1&#8594;v1.2)</small>

#### Other Version Changes

* [Adversary-in-the-Middle](/techniques/T1557) <small style="color:#eb6635">(v1.1&#8594;v2.1)</small>
    * [LLMNR/NBT-NS Poisoning and SMB Relay](/techniques/T1557/001) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
* Boot or Logon Autostart Execution: [Kernel Modules and Extensions](/techniques/T1547/006) <small style="color:#eb6635">(v1.1&#8594;v1.3)</small>
* [Brute Force](/techniques/T1110) <small style="color:#eb6635">(v2.2&#8594;v2.4)</small>
* [Build Image on Host](/techniques/T1612) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
* [Cloud Infrastructure Discovery](/techniques/T1580) <small style="color:#eb6635">(v1.1&#8594;v1.3)</small>
* [Command and Scripting Interpreter](/techniques/T1059) <small style="color:#eb6635">(v2.1&#8594;v2.3)</small>
    * [PowerShell](/techniques/T1059/001) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
    * [Visual Basic](/techniques/T1059/005) <small style="color:#eb6635">(v1.1&#8594;v1.3)</small>
* [Compromise Infrastructure](/techniques/T1584) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
    * [DNS Server](/techniques/T1584/002) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
    * [Domains](/techniques/T1584/001) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
* Create or Modify System Process: [Launch Agent](/techniques/T1543/001) <small style="color:#eb6635">(v1.0&#8594;v1.4)</small>
* [Data Encrypted for Impact](/techniques/T1486) <small style="color:#eb6635">(v1.1&#8594;v1.3)</small>
* [Data from Local System](/techniques/T1005) <small style="color:#eb6635">(v1.2&#8594;v1.4)</small>
* [Drive-by Compromise](/techniques/T1189) <small style="color:#eb6635">(v1.2&#8594;v1.4)</small>
* [Escape to Host](/techniques/T1611) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
* [Exploitation for Client Execution](/techniques/T1203) <small style="color:#eb6635">(v1.1&#8594;v1.4)</small>
* [Exploitation for Credential Access](/techniques/T1212) <small style="color:#eb6635">(v1.1&#8594;v1.4)</small>
* [Exploitation for Defense Evasion](/techniques/T1211) <small style="color:#eb6635">(v1.1&#8594;v1.3)</small>
* [Gather Victim Identity Information](/techniques/T1589) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
* [Hardware Additions](/techniques/T1200) <small style="color:#eb6635">(v1.1&#8594;v1.6)</small>
* Hide Artifacts: [Hidden Users](/techniques/T1564/002) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
* Input Capture: [GUI Input Capture](/techniques/T1056/002) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
* [Inter-Process Communication](/techniques/T1559) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
    * [Dynamic Data Exchange](/techniques/T1559/002) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
* [Lateral Tool Transfer](/techniques/T1570) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
* Obfuscated Files or Information: [Software Packing](/techniques/T1027/002) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
* [Password Policy Discovery](/techniques/T1201) <small style="color:#eb6635">(v1.2&#8594;v1.4)</small>
* Process Injection: [Process Hollowing](/techniques/T1055/012) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
* [Remote System Discovery](/techniques/T1018) <small style="color:#eb6635">(v3.1&#8594;v3.3)</small>
* Scheduled Task/Job: [Container Orchestration Job](/techniques/T1053/007) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
* [Server Software Component](/techniques/T1505) <small style="color:#eb6635">(v1.1&#8594;v1.3)</small>
* Stage Capabilities: [Drive-by Target](/techniques/T1608/004) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
* [Steal or Forge Kerberos Tickets](/techniques/T1558) <small style="color:#eb6635">(v1.2&#8594;v1.4)</small>
* [Supply Chain Compromise](/techniques/T1195) <small style="color:#eb6635">(v1.2&#8594;v1.5)</small>
* [System Information Discovery](/techniques/T1082) <small style="color:#eb6635">(v2.2&#8594;v2.4)</small>
* [System Network Configuration Discovery](/techniques/T1016) <small style="color:#eb6635">(v1.2&#8594;v1.4)</small>
* [System Service Discovery](/techniques/T1007) <small style="color:#eb6635">(v1.1&#8594;v1.3)</small>
* [System Services](/techniques/T1569) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
* [User Execution](/techniques/T1204) <small style="color:#eb6635">(v1.3&#8594;v1.5)</small>
    * [Malicious File](/techniques/T1204/002) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
* [Valid Accounts](/techniques/T1078) <small style="color:#eb6635">(v2.2&#8594;v2.4)</small>
    * [Cloud Accounts](/techniques/T1078/004) <small style="color:#eb6635">(v1.2&#8594;v1.4)</small>

#### Metadata-only Changes

* [Abuse Elevation Control Mechanism](/techniques/T1548) <small style="color:#929393">(v1.0)</small>
    * [Bypass User Account Control](/techniques/T1548/002) <small style="color:#929393">(v2.0)</small>
    * [Sudo and Sudo Caching](/techniques/T1548/003) <small style="color:#929393">(v1.0)</small>
* [Access Token Manipulation](/techniques/T1134) <small style="color:#929393">(v2.0)</small>
    * [Parent PID Spoofing](/techniques/T1134/004) <small style="color:#929393">(v1.0)</small>
* [Account Discovery](/techniques/T1087) <small style="color:#929393">(v2.3)</small>
    * [Domain Account](/techniques/T1087/002) <small style="color:#929393">(v1.0)</small>
* [Active Scanning](/techniques/T1595) <small style="color:#929393">(v1.0)</small>
* [Archive Collected Data](/techniques/T1560) <small style="color:#929393">(v1.0)</small>
* [Automated Exfiltration](/techniques/T1020) <small style="color:#929393">(v1.2)</small>
* [Boot or Logon Autostart Execution](/techniques/T1547) <small style="color:#929393">(v1.1)</small>
    * [Authentication Package](/techniques/T1547/002) <small style="color:#929393">(v1.0)</small>
    * [LSASS Driver](/techniques/T1547/008) <small style="color:#929393">(v1.0)</small>
    * [Registry Run Keys / Startup Folder](/techniques/T1547/001) <small style="color:#929393">(v1.1)</small>
    * [Time Providers](/techniques/T1547/003) <small style="color:#929393">(v1.0)</small>
    * [Winlogon Helper DLL](/techniques/T1547/004) <small style="color:#929393">(v1.0)</small>
* [Boot or Logon Initialization Scripts](/techniques/T1037) <small style="color:#929393">(v2.1)</small>
    * [Startup Items](/techniques/T1037/005) <small style="color:#929393">(v1.0)</small>
* [Browser Extensions](/techniques/T1176) <small style="color:#929393">(v1.2)</small>
* Command and Scripting Interpreter: [AppleScript](/techniques/T1059/002) <small style="color:#929393">(v1.1)</small>
* Command and Scripting Interpreter: [Python](/techniques/T1059/006) <small style="color:#929393">(v1.0)</small>
* [Compromise Client Software Binary](/techniques/T1554) <small style="color:#929393">(v1.0)</small>
* Compromise Infrastructure: [Botnet](/techniques/T1584/005) <small style="color:#929393">(v1.0)</small>
* [Create Account](/techniques/T1136) <small style="color:#929393">(v2.2)</small>
* [Credentials from Password Stores](/techniques/T1555) <small style="color:#929393">(v1.0)</small>
    * [Credentials from Web Browsers](/techniques/T1555/003) <small style="color:#929393">(v1.1)</small>
    * [Password Managers](/techniques/T1555/005) <small style="color:#929393">(v1.0)</small>
* [Data from Configuration Repository](/techniques/T1602) <small style="color:#929393">(v1.0)</small>
    * [Network Device Configuration Dump](/techniques/T1602/002) <small style="color:#929393">(v1.0)</small>
* Data from Information Repositories: [Confluence](/techniques/T1213/001) <small style="color:#929393">(v1.0)</small>
* Data from Information Repositories: [Sharepoint](/techniques/T1213/002) <small style="color:#929393">(v1.0)</small>
* [Deobfuscate/Decode Files or Information](/techniques/T1140) <small style="color:#929393">(v1.1)</small>
* [Domain Trust Discovery](/techniques/T1482) <small style="color:#929393">(v1.1)</small>
* [Dynamic Resolution](/techniques/T1568) <small style="color:#929393">(v1.0)</small>
    * [Domain Generation Algorithms](/techniques/T1568/002) <small style="color:#929393">(v1.0)</small>
* [Endpoint Denial of Service](/techniques/T1499) <small style="color:#929393">(v1.1)</small>
* [Event Triggered Execution](/techniques/T1546) <small style="color:#929393">(v1.1)</small>
    * [Change Default File Association](/techniques/T1546/001) <small style="color:#929393">(v1.0)</small>
    * [Emond](/techniques/T1546/014) <small style="color:#929393">(v1.0)</small>
    * [LC_LOAD_DYLIB Addition](/techniques/T1546/006) <small style="color:#929393">(v1.0)</small>
    * [Netsh Helper DLL](/techniques/T1546/007) <small style="color:#929393">(v1.0)</small>
    * [Screensaver](/techniques/T1546/002) <small style="color:#929393">(v1.0)</small>
* [Execution Guardrails](/techniques/T1480) <small style="color:#929393">(v1.1)</small>
    * [Environmental Keying](/techniques/T1480/001) <small style="color:#929393">(v1.0)</small>
* [Exfiltration Over Other Network Medium](/techniques/T1011) <small style="color:#929393">(v1.1)</small>
* [Exploit Public-Facing Application](/techniques/T1190) <small style="color:#929393">(v2.3)</small>
* [Exploitation of Remote Services](/techniques/T1210) <small style="color:#929393">(v1.1)</small>
* [File and Directory Permissions Modification](/techniques/T1222) <small style="color:#929393">(v2.1)</small>
* Hijack Execution Flow: [COR_PROFILER](/techniques/T1574/012) <small style="color:#929393">(v1.0)</small>
* Hijack Execution Flow: [DLL Side-Loading](/techniques/T1574/002) <small style="color:#929393">(v2.0)</small>
* Hijack Execution Flow: [Dylib Hijacking](/techniques/T1574/004) <small style="color:#929393">(v2.0)</small>
* Hijack Execution Flow: [Path Interception by PATH Environment Variable](/techniques/T1574/007) <small style="color:#929393">(v1.0)</small>
* [Indirect Command Execution](/techniques/T1202) <small style="color:#929393">(v1.1)</small>
* [Input Capture](/techniques/T1056) <small style="color:#929393">(v1.2)</small>
* [Masquerading](/techniques/T1036) <small style="color:#929393">(v1.4)</small>
    * [Match Legitimate Name or Location](/techniques/T1036/005) <small style="color:#929393">(v1.1)</small>
* Modify Authentication Process: [Network Device Authentication](/techniques/T1556/004) <small style="color:#929393">(v2.0)</small>
* Modify Authentication Process: [Pluggable Authentication Modules](/techniques/T1556/003) <small style="color:#929393">(v2.0)</small>
* [Network Denial of Service](/techniques/T1498) <small style="color:#929393">(v1.1)</small>
* [Non-Application Layer Protocol](/techniques/T1095) <small style="color:#929393">(v2.1)</small>
* [Phishing for Information](/techniques/T1598) <small style="color:#929393">(v1.1)</small>
* [Pre-OS Boot](/techniques/T1542) <small style="color:#929393">(v1.1)</small>
* Process Injection: [VDSO Hijacking](/techniques/T1055/014) <small style="color:#929393">(v1.0)</small>
* [Proxy](/techniques/T1090) <small style="color:#929393">(v3.1)</small>
* [Rootkit](/techniques/T1014) <small style="color:#929393">(v1.1)</small>
* Server Software Component: [Transport Agent](/techniques/T1505/002) <small style="color:#929393">(v1.0)</small>
* [Software Discovery](/techniques/T1518) <small style="color:#929393">(v1.3)</small>
* Steal or Forge Kerberos Tickets: [AS-REP Roasting](/techniques/T1558/004) <small style="color:#929393">(v1.0)</small>
* Subvert Trust Controls: [Code Signing Policy Modification](/techniques/T1553/006) <small style="color:#929393">(v1.0)</small>
* Subvert Trust Controls: [SIP and Trust Provider Hijacking](/techniques/T1553/003) <small style="color:#929393">(v1.0)</small>
* [System Location Discovery](/techniques/T1614) <small style="color:#929393">(v1.0)</small>
* Traffic Signaling: [Port Knocking](/techniques/T1205/001) <small style="color:#929393">(v1.1)</small>
* [Trusted Developer Utilities Proxy Execution](/techniques/T1127) <small style="color:#929393">(v1.2)</small>
* [Unsecured Credentials](/techniques/T1552) <small style="color:#929393">(v1.2)</small>
* Use Alternate Authentication Material: [Pass the Hash](/techniques/T1550/002) <small style="color:#929393">(v1.1)</small>
* Use Alternate Authentication Material: [Pass the Ticket](/techniques/T1550/003) <small style="color:#929393">(v1.1)</small>
* [XSL Script Processing](/techniques/T1220) <small style="color:#929393">(v1.2)</small>

#### Revocations


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

#### Metadata-only Changes

* [Install Insecure or Malicious Configuration](/techniques/T1478) <small style="color:#929393">(v1.0)</small>

### ICS

#### New Techniques

* [Transient Cyber Asset](/techniques/T0864) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* [Activate Firmware Update Mode](/techniques/T0800) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Alarm Suppression](/techniques/T0878) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Automated Collection](/techniques/T0802) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Block Command Message](/techniques/T0803) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Block Reporting Message](/techniques/T0804) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Block Serial COM](/techniques/T0805) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Brute Force I/O](/techniques/T0806) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Change Operating Mode](/techniques/T0858) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Command-Line Interface](/techniques/T0807) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Commonly Used Port](/techniques/T0885) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Connection Proxy](/techniques/T0884) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Damage to Property](/techniques/T0879) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Data Destruction](/techniques/T0809) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Data from Information Repositories](/techniques/T0811) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Default Credentials](/techniques/T0812) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Denial of Control](/techniques/T0813) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Denial of Service](/techniques/T0814) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Denial of View](/techniques/T0815) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Detect Operating Mode](/techniques/T0868) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Device Restart/Shutdown](/techniques/T0816) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Drive-by Compromise](/techniques/T0817) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Execution through API](/techniques/T0871) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Exploit Public-Facing Application](/techniques/T0819) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Exploitation for Evasion](/techniques/T0820) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Exploitation for Privilege Escalation](/techniques/T0890) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Exploitation of Remote Services](/techniques/T0866) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [External Remote Services](/techniques/T0822) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Graphical User Interface](/techniques/T0823) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Hooking](/techniques/T0874) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [I/O Image](/techniques/T0877) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Indicator Removal on Host](/techniques/T0872) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Internet Accessible Device](/techniques/T0883) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Lateral Tool Transfer](/techniques/T0867) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Loss of Availability](/techniques/T0826) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Loss of Control](/techniques/T0827) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Loss of Productivity and Revenue](/techniques/T0828) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Loss of Protection](/techniques/T0837) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Loss of Safety](/techniques/T0880) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Loss of View](/techniques/T0829) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Man in the Middle](/techniques/T0830) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Manipulate I/O Image](/techniques/T0835) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Manipulation of Control](/techniques/T0831) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Manipulation of View](/techniques/T0832) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Masquerading](/techniques/T0849) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Modify Alarm Settings](/techniques/T0838) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Modify Controller Tasking](/techniques/T0821) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Modify Parameter](/techniques/T0836) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Modify Program](/techniques/T0889) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Module Firmware](/techniques/T0839) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Monitor Process State](/techniques/T0801) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Native API](/techniques/T0834) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Network Connection Enumeration](/techniques/T0840) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Network Sniffing](/techniques/T0842) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Point & Tag Identification](/techniques/T0861) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Program Download](/techniques/T0843) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Program Upload](/techniques/T0845) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Project File Infection](/techniques/T0873) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Remote Services](/techniques/T0886) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Remote System Discovery](/techniques/T0846) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Remote System Information Discovery](/techniques/T0888) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Replication Through Removable Media](/techniques/T0847) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Rogue Master](/techniques/T0848) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Rootkit](/techniques/T0851) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Screen Capture](/techniques/T0852) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Scripting](/techniques/T0853) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Service Stop](/techniques/T0881) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Spearphishing Attachment](/techniques/T0865) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Spoof Reporting Message](/techniques/T0856) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Standard Application Layer Protocol](/techniques/T0869) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Supply Chain Compromise](/techniques/T0862) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [System Firmware](/techniques/T0857) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Theft of Operational Information](/techniques/T0882) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Unauthorized Command Message](/techniques/T0855) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [User Execution](/techniques/T0863) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Valid Accounts](/techniques/T0859) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Wireless Compromise](/techniques/T0860) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Wireless Sniffing](/techniques/T0887) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>

#### Deprecations

* [Data Historian Compromise](/techniques/T0810) <small style="color:#929393">(v0.0)</small>
* [Engineering Workstation Compromise](/techniques/T0818) <small style="color:#929393">(v0.0)</small>

## Software

### Enterprise

#### New Software

* [AADInternals](/software/S0677) <small style="color:#929393">(v1.0)</small>
* [AppleSeed](/software/S0622) <small style="color:#eb6635">(v1.1)</small>
* [Avaddon](/software/S0640) <small style="color:#929393">(v1.0)</small>
* [BADFLICK](/software/S0642) <small style="color:#929393">(v1.0)</small>
* [BLUELIGHT](/software/S0657) <small style="color:#929393">(v1.0)</small>
* [Babuk](/software/S0638) <small style="color:#929393">(v1.0)</small>
* [Bad Rabbit](/software/S0606) <small style="color:#929393">(v1.0)</small>
* [BoomBox](/software/S0635) <small style="color:#929393">(v1.0)</small>
* [BoxCaon](/software/S0651) <small style="color:#929393">(v1.0)</small>
* [CaddyWiper](/software/S0693) <small style="color:#929393">(v1.0)</small>
* [Chaes](/software/S0631) <small style="color:#929393">(v1.0)</small>
* [CharmPower](/software/S0674) <small style="color:#929393">(v1.0)</small>
* [Chrommme](/software/S0667) <small style="color:#929393">(v1.0)</small>
* [Clambling](/software/S0660) <small style="color:#929393">(v1.0)</small>
* [Clop](/software/S0611) <small style="color:#929393">(v1.0)</small>
* [Conficker](/software/S0608) <small style="color:#929393">(v1.0)</small>
* [CostaBricks](/software/S0614) <small style="color:#929393">(v1.0)</small>
* [Cuba](/software/S0625) <small style="color:#929393">(v1.0)</small>
* [Cyclops Blink](/software/S0687) <small style="color:#929393">(v1.0)</small>
* [DEATHRANSOM](/software/S0616) <small style="color:#929393">(v1.0)</small>
* [DRATzarus](/software/S0694) <small style="color:#929393">(v1.0)</small>
* [DarkWatchman](/software/S0673) <small style="color:#929393">(v1.0)</small>
* [Diavol](/software/S0659) <small style="color:#929393">(v1.0)</small>
* [Donut](/software/S0695) <small style="color:#929393">(v1.0)</small>
* [EKANS](/software/S0605) <small style="color:#eb6635">(v2.0)</small>
* [Ecipekac](/software/S0624) <small style="color:#929393">(v1.0)</small>
* [EnvyScout](/software/S0634) <small style="color:#929393">(v1.0)</small>
* [FIVEHANDS](/software/S0618) <small style="color:#929393">(v1.0)</small>
* [FYAnti](/software/S0628) <small style="color:#929393">(v1.0)</small>
* [Ferocious](/software/S0679) <small style="color:#929393">(v1.0)</small>
* [Flagpro](/software/S0696) <small style="color:#929393">(v1.0)</small>
* [FoggyWeb](/software/S0661) <small style="color:#929393">(v1.0)</small>
* [Gelsemium](/software/S0666) <small style="color:#929393">(v1.0)</small>
* [Green Lambert](/software/S0690) <small style="color:#929393">(v1.0)</small>
* [GrimAgent](/software/S0632) <small style="color:#929393">(v1.0)</small>
* [HELLOKITTY](/software/S0617) <small style="color:#929393">(v1.0)</small>
* [HermeticWiper](/software/S0697) <small style="color:#929393">(v1.0)</small>
* [HermeticWizard](/software/S0698) <small style="color:#929393">(v1.0)</small>
* [Industroyer](/software/S0604) <small style="color:#929393">(v1.0)</small>
* [JSS Loader](/software/S0648) <small style="color:#929393">(v1.0)</small>
* [KOCTOPUS](/software/S0669) <small style="color:#929393">(v1.0)</small>
* [KillDisk](/software/S0607) <small style="color:#eb6635">(v1.1)</small>
* [Kobalos](/software/S0641) <small style="color:#929393">(v1.0)</small>
* [LiteDuke](/software/S0513) <small style="color:#929393">(v1.0)</small>
* [LitePower](/software/S0680) <small style="color:#929393">(v1.0)</small>
* [Lizar](/software/S0681) <small style="color:#929393">(v1.0)</small>
* [MarkiRAT](/software/S0652) <small style="color:#929393">(v1.0)</small>
* [Meteor](/software/S0688) <small style="color:#929393">(v1.0)</small>
* [Mythic](/software/S0699) <small style="color:#929393">(v1.0)</small>
* [NativeZone](/software/S0637) <small style="color:#929393">(v1.0)</small>
* [Nebulae](/software/S0630) <small style="color:#929393">(v1.0)</small>
* [Neoichor](/software/S0691) <small style="color:#929393">(v1.0)</small>
* [ObliqueRAT](/software/S0644) <small style="color:#929393">(v1.0)</small>
* [P8RAT](/software/S0626) <small style="color:#929393">(v1.0)</small>
* [PS1](/software/S0613) <small style="color:#929393">(v1.0)</small>
* [Pandora](/software/S0664) <small style="color:#929393">(v1.0)</small>
* [Peirates](/software/S0683) <small style="color:#929393">(v1.0)</small>
* [Peppy](/software/S0643) <small style="color:#929393">(v1.0)</small>
* [PowerPunch](/software/S0685) <small style="color:#929393">(v1.0)</small>
* [ProLock](/software/S0654) <small style="color:#929393">(v1.0)</small>
* [QakBot](/software/S0650) <small style="color:#929393">(v1.0)</small>
* [QuietSieve](/software/S0686) <small style="color:#929393">(v1.0)</small>
* [RCSession](/software/S0662) <small style="color:#929393">(v1.0)</small>
* [ROADTools](/software/S0684) <small style="color:#929393">(v1.0)</small>
* [RainyDay](/software/S0629) <small style="color:#929393">(v1.0)</small>
* [SILENTTRINITY](/software/S0692) <small style="color:#929393">(v1.0)</small>
* [SMOKEDHAM](/software/S0649) <small style="color:#929393">(v1.0)</small>
* [Seth-Locker](/software/S0639) <small style="color:#929393">(v1.0)</small>
* [SideTwist](/software/S0610) <small style="color:#929393">(v1.0)</small>
* [Siloscape](/software/S0623) <small style="color:#929393">(v1.0)</small>
* [Sliver](/software/S0633) <small style="color:#929393">(v1.0)</small>
* [SodaMaster](/software/S0627) <small style="color:#929393">(v1.0)</small>
* [SombRAT](/software/S0615) <small style="color:#eb6635">(v1.1)</small>
* [SpicyOmelette](/software/S0646) <small style="color:#929393">(v1.0)</small>
* [Stuxnet](/software/S0603) <small style="color:#eb6635">(v1.1)</small>
* [SysUpdate](/software/S0663) <small style="color:#929393">(v1.0)</small>
* [TRITON](/software/S0609) <small style="color:#929393">(v1.0)</small>
* [ThreatNeedle](/software/S0665) <small style="color:#929393">(v1.0)</small>
* [TinyTurla](/software/S0668) <small style="color:#929393">(v1.0)</small>
* [Tomiris](/software/S0671) <small style="color:#929393">(v1.0)</small>
* [Torisma](/software/S0678) <small style="color:#929393">(v1.0)</small>
* [TrailBlazer](/software/S0682) <small style="color:#929393">(v1.0)</small>
* [Turian](/software/S0647) <small style="color:#929393">(v1.0)</small>
* [VaporRage](/software/S0636) <small style="color:#929393">(v1.0)</small>
* [WarzoneRAT](/software/S0670) <small style="color:#929393">(v1.0)</small>
* [WastedLocker](/software/S0612) <small style="color:#929393">(v1.0)</small>
* [Wevtutil](/software/S0645) <small style="color:#929393">(v1.0)</small>
* [WhisperGate](/software/S0689) <small style="color:#929393">(v1.0)</small>
* [XCSSET](/software/S0658) <small style="color:#eb6635">(v1.1)</small>
* [Zox](/software/S0672) <small style="color:#929393">(v1.0)</small>
* [xCaon](/software/S0653) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* [Backdoor.Oldrea](/software/S0093) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Bandook](/software/S0234) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Bisonal](/software/S0268) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Conti](/software/S0575) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Dok](/software/S0281) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Dridex](/software/S0384) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [GoldMax](/software/S0588) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [GuLoader](/software/S0561) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Hydraq](/software/S0203) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [KONNI](/software/S0356) <small style="color:#929393">(v1.4&#8594;v2.0)</small>
* [Kerrdown](/software/S0585) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Koadic](/software/S0250) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [LockerGoga](/software/S0372) <small style="color:#929393">(v1.3&#8594;v2.0)</small>
* [Lokibot](/software/S0447) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Metamorfo](/software/S0455) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Octopus](/software/S0340) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [PLEAD](/software/S0435) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [PlugX](/software/S0013) <small style="color:#929393">(v2.1&#8594;v3.0)</small>
* [PoisonIvy](/software/S0012) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* [Pteranodon](/software/S0147) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [REvil](/software/S0496) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Taidoor](/software/S0011) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [TrickBot](/software/S0266) <small style="color:#929393">(v1.4&#8594;v2.0)</small>
* [Trojan.Karagany](/software/S0094) <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* [Winnti for Windows](/software/S0141) <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* [ftp](/software/S0095) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [gh0st RAT](/software/S0032) <small style="color:#929393">(v2.3&#8594;v3.0)</small>

#### Minor Version Changes

* [Aria-body](/software/S0456) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Arp](/software/S0099) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Bazar](/software/S0534) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Brave Prince](/software/S0252) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Bundlore](/software/S0482) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [CHOPSTICK](/software/S0023) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [Carberp](/software/S0484) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [China Chopper](/software/S0020) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* [Crimson](/software/S0115) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Derusbi](/software/S0021) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [DropBook](/software/S0547) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Emissary](/software/S0082) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [FatDuke](/software/S0512) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [FinFisher](/software/S0182) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Gold Dragon](/software/S0249) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Hikit](/software/S0009) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Hildegard](/software/S0601) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [HyperBro](/software/S0398) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Impacket](/software/S0357) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [InvisiMole](/software/S0260) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Keydnap](/software/S0276) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Kinsing](/software/S0599) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [LaZagne](/software/S0349) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [LoudMiner](/software/S0451) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Lucifer](/software/S0532) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Maze](/software/S0449) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [MimiPenguin](/software/S0179) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [MiniDuke](/software/S0051) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [NETWIRE](/software/S0198) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Net](/software/S0039) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* [Ngrok](/software/S0508) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Nltest](/software/S0359) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [OSX/Shlayer](/software/S0402) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Orz](/software/S0229) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [OwaAuth](/software/S0072) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Ping](/software/S0097) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [PoetRAT](/software/S0428) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [PowerSploit](/software/S0194) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Prikormka](/software/S0113) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [PsExec](/software/S0029) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [RGDoor](/software/S0258) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [ROKRAT](/software/S0240) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* [Remcos](/software/S0332) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Responder](/software/S0174) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [SharpStage](/software/S0546) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Spark](/software/S0543) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [SynAck](/software/S0242) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [USBStealer](/software/S0136) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Waterbear](/software/S0579) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Zeus Panda](/software/S0330) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [ZxShell](/software/S0412) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [at](/software/S0110) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [certutil](/software/S0160) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [esentutl](/software/S0404) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [njRAT](/software/S0385) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [route](/software/S0103) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [schtasks](/software/S0111) <small style="color:#929393">(v1.1&#8594;v1.2)</small>

#### Other Version Changes

* [BloodHound](/software/S0521) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>
* [Cobalt Strike](/software/S0154) <small style="color:#eb6635">(v1.6&#8594;v1.8)</small>
* [Empire](/software/S0363) <small style="color:#eb6635">(v1.2&#8594;v1.4)</small>
* [Mimikatz](/software/S0002) <small style="color:#eb6635">(v1.3&#8594;v1.5)</small>
* [OSX_OCEANLOTUS.D](/software/S0352) <small style="color:#eb6635">(v2.0&#8594;v2.2)</small>
* [QuasarRAT](/software/S0262) <small style="color:#eb6635">(v1.1&#8594;v1.3)</small>
* [Ryuk](/software/S0446) <small style="color:#eb6635">(v1.1&#8594;v1.3)</small>
* [SUNBURST](/software/S0559) <small style="color:#eb6635">(v2.0&#8594;v2.2)</small>
* [ThiefQuest](/software/S0595) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>

#### Metadata-only Changes

* [Anchor](/software/S0504) <small style="color:#929393">(v1.0)</small>
* [BADNEWS](/software/S0128) <small style="color:#929393">(v1.2)</small>
* [BOOTRASH](/software/S0114) <small style="color:#929393">(v1.1)</small>
* [BS2005](/software/S0014) <small style="color:#929393">(v1.1)</small>
* [ECCENTRICBANDWAGON](/software/S0593) <small style="color:#929393">(v1.0)</small>
* [EVILNUM](/software/S0568) <small style="color:#929393">(v1.0)</small>
* [Egregor](/software/S0554) <small style="color:#929393">(v1.0)</small>
* [Mis-Type](/software/S0084) <small style="color:#929393">(v1.1)</small>
* [Misdat](/software/S0083) <small style="color:#929393">(v1.1)</small>
* [Nidiran](/software/S0118) <small style="color:#929393">(v1.1)</small>
* [Reg](/software/S0075) <small style="color:#929393">(v1.0)</small>
* [S-Type](/software/S0085) <small style="color:#929393">(v1.1)</small>
* [SYNful Knock](/software/S0519) <small style="color:#929393">(v1.0)</small>
* [TSCookie](/software/S0436) <small style="color:#929393">(v1.0)</small>
* [WindTail](/software/S0466) <small style="color:#929393">(v1.0)</small>
* [ZLib](/software/S0086) <small style="color:#929393">(v1.1)</small>
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
* [EKANS](/software/S0605) <small style="color:#eb6635">(v2.0)</small>
* [Industroyer](/software/S0604) <small style="color:#929393">(v1.0)</small>
* [KillDisk](/software/S0607) <small style="color:#eb6635">(v1.1)</small>
* [Stuxnet](/software/S0603) <small style="color:#eb6635">(v1.1)</small>

#### Major Version Changes

* [Backdoor.Oldrea](/software/S0093) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [LockerGoga](/software/S0372) <small style="color:#929393">(v1.3&#8594;v2.0)</small>
* [REvil](/software/S0496) <small style="color:#929393">(v1.1&#8594;v2.0)</small>

#### Other Version Changes

* [Ryuk](/software/S0446) <small style="color:#eb6635">(v1.1&#8594;v1.3)</small>

#### Metadata-only Changes

* [ACAD/Medre.A](/software/S0018) <small style="color:#929393">(v1.0)</small>
* [PLC-Blaster](/software/S0009) <small style="color:#929393">(v1.0)</small>
* [Triton](/software/S0013) <small style="color:#929393">(v1.0)</small>
* [VPNFilter](/software/S0002) <small style="color:#929393">(v1.0)</small>

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
* [Aquatic Panda](/groups/G0143) <small style="color:#929393">(v1.0)</small>
* [BackdoorDiplomacy](/groups/G0135) <small style="color:#929393">(v1.0)</small>
* [Confucius](/groups/G0142) <small style="color:#929393">(v1.0)</small>
* [CostaRicto](/groups/G0132) <small style="color:#929393">(v1.0)</small>
* [Ferocious Kitten](/groups/G0137) <small style="color:#929393">(v1.0)</small>
* [Gelsemium](/groups/G0141) <small style="color:#929393">(v1.0)</small>
* [IndigoZebra](/groups/G0136) <small style="color:#929393">(v1.0)</small>
* [LazyScripter](/groups/G0140) <small style="color:#929393">(v1.0)</small>
* [Nomadic Octopus](/groups/G0133) <small style="color:#929393">(v1.0)</small>
* [TeamTNT](/groups/G0139) <small style="color:#eb6635">(v1.1)</small>
* [Tonto Team](/groups/G0131) <small style="color:#eb6635">(v1.1)</small>
* [Transparent Tribe](/groups/G0134) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* [APT28](/groups/G0007) <small style="color:#929393">(v3.1&#8594;v4.0)</small>
* [APT29](/groups/G0016) <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* [APT37](/groups/G0067) <small style="color:#929393">(v1.5&#8594;v2.0)</small>
* [APT38](/groups/G0082) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* [APT41](/groups/G0096) <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* [Axiom](/groups/G0001) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* [BlackTech](/groups/G0098) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Carbanak](/groups/G0008) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* [Cobalt Group](/groups/G0080) <small style="color:#929393">(v1.3&#8594;v2.0)</small>
* [Dragonfly](/groups/G0035) <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* [Gamaredon Group](/groups/G0047) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* [Ke3chang](/groups/G0004) <small style="color:#929393">(v1.3&#8594;v2.0)</small>
* [Leviathan](/groups/G0065) <small style="color:#929393">(v2.1&#8594;v3.0)</small>
* [Mustang Panda](/groups/G0129) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Naikon](/groups/G0019) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [OilRig](/groups/G0049) <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* [Threat Group-3390](/groups/G0027) <small style="color:#929393">(v1.4&#8594;v2.0)</small>
* [Turla](/groups/G0010) <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* [WIRTE](/groups/G0090) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Wizard Spider](/groups/G0102) <small style="color:#929393">(v1.3&#8594;v2.0)</small>

#### Minor Version Changes

* [APT-C-36](/groups/G0099) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [APT1](/groups/G0006) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [APT19](/groups/G0073) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
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
* [FIN10](/groups/G0051) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [FIN4](/groups/G0085) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [FIN5](/groups/G0053) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [FIN6](/groups/G0037) <small style="color:#929393">(v3.1&#8594;v3.2)</small>
* [FIN8](/groups/G0061) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Frankenstein](/groups/G0101) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Gorgon Group](/groups/G0078) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [HAFNIUM](/groups/G0125) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Inception](/groups/G0100) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Leafminer](/groups/G0077) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* [Night Dragon](/groups/G0014) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Patchwork](/groups/G0040) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [PittyTiger](/groups/G0011) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Silence](/groups/G0091) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [TA505](/groups/G0092) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [TA551](/groups/G0127) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [TEMP.Veles](/groups/G0088) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Thrip](/groups/G0076) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Volatile Cedar](/groups/G0123) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Whitefly](/groups/G0107) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Winnti Group](/groups/G0044) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [menuPass](/groups/G0045) <small style="color:#929393">(v2.0&#8594;v2.1)</small>

#### Other Version Changes

* [FIN7](/groups/G0046) <small style="color:#eb6635">(v1.5&#8594;v2.1)</small>
* [Indrik Spider](/groups/G0119) <small style="color:#eb6635">(v1.0&#8594;v2.1)</small>
* [Kimsuky](/groups/G0094) <small style="color:#eb6635">(v2.0&#8594;v3.1)</small>
* [Lazarus Group](/groups/G0032) <small style="color:#eb6635">(v1.5&#8594;v3.0)</small>
* [Magic Hound](/groups/G0059) <small style="color:#eb6635">(v3.0&#8594;v4.1)</small>
* [Sandworm Team](/groups/G0034) <small style="color:#eb6635">(v2.0&#8594;v2.2)</small>

#### Metadata-only Changes

* [Ajax Security Team](/groups/G0130) <small style="color:#929393">(v1.0)</small>
* [Dust Storm](/groups/G0031) <small style="color:#929393">(v1.0)</small>
* [Machete](/groups/G0095) <small style="color:#929393">(v2.0)</small>
* [Operation Wocao](/groups/G0116) <small style="color:#929393">(v1.0)</small>
* [Orangeworm](/groups/G0071) <small style="color:#929393">(v1.1)</small>
* [Suckfly](/groups/G0039) <small style="color:#929393">(v1.1)</small>

#### Revocations

* Dragonfly 2.0 (revoked by [Dragonfly](/groups/G0035)) <small style="color:#929393">(v2.1)</small>
* Stolen Pencil (revoked by [Kimsuky](/groups/G0094)) <small style="color:#929393">(v1.1)</small>

#### Deprecations

* [Taidoor](/groups/G0015) <small style="color:#929393">(v1.0)</small>

### Mobile

#### Minor Version Changes

* [APT28](/groups/G0007) <small style="color:#929393">(v3.1&#8594;v3.2)</small>
* [Dark Caracal](/groups/G0070) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Sandworm Team](/groups/G0034) <small style="color:#929393">(v2.0&#8594;v2.1)</small>

### ICS

#### Major Version Changes

* [Dragonfly](/groups/G0035) <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* [OilRig](/groups/G0049) <small style="color:#929393">(v2.0&#8594;v3.0)</small>

#### Minor Version Changes

* [APT33](/groups/G0064) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [TEMP.Veles](/groups/G0088) <small style="color:#929393">(v1.2&#8594;v1.3)</small>

#### Other Version Changes

* [HEXANE](/groups/G1001) <small style="color:#eb6635">(v1.1&#8594;v1.0)</small>
* [Lazarus Group](/groups/G0032) <small style="color:#eb6635">(v1.5&#8594;v3.0)</small>
* [Sandworm Team](/groups/G0034) <small style="color:#eb6635">(v2.0&#8594;v2.2)</small>

#### Metadata-only Changes

* [ALLANITE](/groups/G1000) <small style="color:#929393">(v1.0)</small>

## Campaigns

### Enterprise

### Mobile

### ICS

## Mitigations

### Enterprise

#### New Mitigations

* [Data Loss Prevention](/mitigations/M1057) <small style="color:#929393">(v1.0)</small>

#### Minor Version Changes

* [Execution Prevention](/mitigations/M1038) <small style="color:#929393">(v1.1&#8594;v1.2)</small>

### Mobile

### ICS

#### Other Version Changes

* [Filter Network Traffic](/mitigations/M0937) <small style="color:#eb6635">(v1.1&#8594;v1.0)</small>

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

#### New Data Sources

* [Active Directory](/datasources/DS0026) <small style="color:#929393">(v1.0)</small>
* [Application Log](/datasources/DS0015) <small style="color:#929393">(v1.0)</small>
* [Certificate](/datasources/DS0037) <small style="color:#929393">(v1.0)</small>
* [Cloud Service](/datasources/DS0025) <small style="color:#929393">(v1.0)</small>
* [Cloud Storage](/datasources/DS0010) <small style="color:#929393">(v1.0)</small>
* [Cluster](/datasources/DS0031) <small style="color:#929393">(v1.0)</small>
* [Command](/data-sources/DS0017) <small style="color:#929393">(v1.0)</small>
* [Container](/datasources/DS0032) <small style="color:#929393">(v1.0)</small>
* [Domain Name](/datasources/DS0038) <small style="color:#929393">(v1.0)</small>
* [Drive](/datasources/DS0016) <small style="color:#929393">(v1.0)</small>
* [Driver](/datasources/DS0027) <small style="color:#929393">(v1.0)</small>
* [File](/data-sources/DS0022) <small style="color:#929393">(v1.0)</small>
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

#### New Data Sources

* [Application Log](/datasources/DS0015) <small style="color:#929393">(v1.0)</small>
* [Assets](/datasources/DS0039) <small style="color:#929393">(v1.0)</small>
* [Command](/data-sources/DS0017) <small style="color:#929393">(v1.0)</small>
* [Drive](/datasources/DS0016) <small style="color:#929393">(v1.0)</small>
* [File](/data-sources/DS0022) <small style="color:#929393">(v1.0)</small>
* [Firmware](/datasources/DS0001) <small style="color:#929393">(v1.0)</small>
* [Logon Session](/datasources/DS0028) <small style="color:#929393">(v1.0)</small>
* [Module](/datasources/DS0011) <small style="color:#929393">(v1.0)</small>
* [Network Share](/datasources/DS0033) <small style="color:#929393">(v1.0)</small>
* [Network Traffic](/datasources/DS0029) <small style="color:#929393">(v1.0)</small>
* [Operational Databases](/datasources/DS0040) <small style="color:#929393">(v1.0)</small>
* [Process](/datasources/DS0009) <small style="color:#929393">(v1.0)</small>
* [Scheduled Job](/datasources/DS0003) <small style="color:#929393">(v1.0)</small>
* [Script](/datasources/DS0012) <small style="color:#929393">(v1.0)</small>
* [Service](/datasources/DS0019) <small style="color:#929393">(v1.0)</small>
* [User Account](/datasources/DS0002) <small style="color:#929393">(v1.0)</small>
* [Windows Registry](/datasources/DS0024) <small style="color:#929393">(v1.0)</small>

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
* [Command Execution](/data-sources/DS0017/#Command%20Execution) <small style="color:#929393">(v1.0)</small>
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
* [File Access](/data-sources/DS0022/#File%20Access) <small style="color:#929393">(v1.0)</small>
* [File Creation](/data-sources/DS0022/#File%20Creation) <small style="color:#929393">(v1.0)</small>
* [File Deletion](/data-sources/DS0022/#File%20Deletion) <small style="color:#929393">(v1.0)</small>
* [File Metadata](/data-sources/DS0022/#File%20Metadata) <small style="color:#929393">(v1.0)</small>
* [File Modification](/data-sources/DS0022/#File%20Modification) <small style="color:#929393">(v1.0)</small>
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

#### New Data Components

* [Application Log Content](/datasources/DS0015/#Application%20Log%20Content) <small style="color:#929393">(v1.0)</small>
* [Command Execution](/data-sources/DS0017/#Command%20Execution) <small style="color:#929393">(v1.0)</small>
* [Device Alarm](/datasources/DS0040/#Device%20Alarm) <small style="color:#929393">(v1.0)</small>
* [Drive Creation](/datasources/DS0016/#Drive%20Creation) <small style="color:#929393">(v1.0)</small>
* [Drive Modification](/datasources/DS0016/#Drive%20Modification) <small style="color:#929393">(v1.0)</small>
* [File Access](/data-sources/DS0022/#File%20Access) <small style="color:#929393">(v1.0)</small>
* [File Creation](/data-sources/DS0022/#File%20Creation) <small style="color:#929393">(v1.0)</small>
* [File Deletion](/data-sources/DS0022/#File%20Deletion) <small style="color:#929393">(v1.0)</small>
* [File Metadata](/data-sources/DS0022/#File%20Metadata) <small style="color:#929393">(v1.0)</small>
* [File Modification](/data-sources/DS0022/#File%20Modification) <small style="color:#929393">(v1.0)</small>
* [Firmware Modification](/datasources/DS0001/#Firmware%20Modification) <small style="color:#929393">(v1.0)</small>
* [Logon Session Creation](/datasources/DS0028/#Logon%20Session%20Creation) <small style="color:#929393">(v1.0)</small>
* [Logon Session Metadata](/datasources/DS0028/#Logon%20Session%20Metadata) <small style="color:#929393">(v1.0)</small>
* [Module Load](/datasources/DS0011/#Module%20Load) <small style="color:#929393">(v1.0)</small>
* [Network Connection Creation](/datasources/DS0029/#Network%20Connection%20Creation) <small style="color:#929393">(v1.0)</small>
* [Network Share Access](/datasources/DS0033/#Network%20Share%20Access) <small style="color:#929393">(v1.0)</small>
* [Network Traffic Content](/datasources/DS0029/#Network%20Traffic%20Content) <small style="color:#929393">(v1.0)</small>
* [Network Traffic Flow](/datasources/DS0029/#Network%20Traffic%20Flow) <small style="color:#929393">(v1.0)</small>
* [OS API Execution](/datasources/DS0009/#OS%20API%20Execution) <small style="color:#929393">(v1.0)</small>
* [Process Creation](/datasources/DS0009/#Process%20Creation) <small style="color:#929393">(v1.0)</small>
* [Process History/Live Data](/datasources/DS0040/#Process%20History/Live%20Data) <small style="color:#929393">(v1.0)</small>
* [Process Metadata](/datasources/DS0009/#Process%20Metadata) <small style="color:#929393">(v1.0)</small>
* [Process Termination](/datasources/DS0009/#Process%20Termination) <small style="color:#929393">(v1.0)</small>
* [Process/Event Alarm](/datasources/DS0040/#Process/Event%20Alarm) <small style="color:#929393">(v1.0)</small>
* [Scheduled Job Metadata](/datasources/DS0003/#Scheduled%20Job%20Metadata) <small style="color:#929393">(v1.0)</small>
* [Scheduled Job Modification](/datasources/DS0003/#Scheduled%20Job%20Modification) <small style="color:#929393">(v1.0)</small>
* [Script Execution](/datasources/DS0012/#Script%20Execution) <small style="color:#929393">(v1.0)</small>
* [Service Creation](/datasources/DS0019/#Service%20Creation) <small style="color:#929393">(v1.0)</small>
* [Service Metadata](/datasources/DS0019/#Service%20Metadata) <small style="color:#929393">(v1.0)</small>
* [User Account Authentication](/datasources/DS0002/#User%20Account%20Authentication) <small style="color:#929393">(v1.0)</small>
* [Windows Registry Key Deletion](/datasources/DS0024/#Windows%20Registry%20Key%20Deletion) <small style="color:#929393">(v1.0)</small>
* [Windows Registry Key Modification](/datasources/DS0024/#Windows%20Registry%20Key%20Modification) <small style="color:#929393">(v1.0)</small>

## Contributors to this release

* @ionstorm
* Abhijit Mohanta, @abhijit_mohanta, Uptycs
* Achute Sharma, Keysight
* Akshat Pradhan, Qualys
* Alex Parsons, Crowdstrike
* Alex Spivakovsky, Pentera
* Andrew Northern, @ex_raritas
* Antonio Piazza, @antman1p
* Arnim Rupp, Deutsche Lufthansa AG
* Atul Nair, Qualys
* Austin Clark, @c2defense
* Ayan Saha, Keysight
* Bryan Campbell, @bry_campbell
* Center for Threat-Informed Defense (CTID)
* Chris Romano, Crowdstrike
* Christoffer Strömblad
* Christopher Glyer, Mandiant, @cglyer
* Clément Notin, Tenable
* Cody Thomas, SpecterOps
* Craig Smith, BT Security
* Csaba Fitzl @theevilbit of Offensive Security
* Daisuke Suzuki
* Dan Borges, @1njection
* Daniel Acevedo, Blackbot
* Daniel Feichter, @VirtualAllocEx, Infosec Tirol
* Daniel Prizmant, Palo Alto Networks
* Daniyal Naeem, BT Security
* Darin Smith, Cisco
* Dongwook Kim, KISA
* Dor Edry, Microsoft
* Dragos Threat Intelligence
* Dror Alon, Palo Alto Networks
* Edward Millington
* Eli Salem, @elisalem9
* Elvis Veliz, Citi
* Eric Kaiser @ideologysec
* ESET
* ExtraHop
* Gaetan van Diemen, ThreatFabric
* Gareth Phillips, Seek Ltd.
* Gordon Long, Box, Inc., @ethicalhax
* Hannah Simes, BT Security
* Harshal Tupsamudre, Qualys
* Hiroki Nagahama, NEC Corporation
* Isif Ibrahima, Mandiant
* Itamar Mizrahi, Cymptom
* Ivan Sinyakov
* James_inthe_box, Me
* Jan Petrov, Citi
* Janantha Marasinghe
* Jannie Li, Microsoft Threat Intelligence Center (MSTIC)
* Jaron Bradley @jbradley89
* Jeff Felling, Red Canary
* Jen Burns, HubSpot
* Jeremy Galloway
* Joas Antonio dos Santos, @C0d3Cr4zy, Inmetrics
* Johann Rehberger
* John Page (aka hyp3rlinx), ApparitionSec
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
* Kobi Haimovich, CardinalOps
* Krishnan Subramanian, @krish203
* Kyaw Pyiyt Htet, @KyawPyiytHtet
* Kyoung-ju Kwak (S2W)
* Lior Ribak, SentinelOne
* Manikantan Srinivasan, NEC Corporation India
* Maril Vernon @shewhohacks
* Massimiliano Romano, BT Security
* Matt Brenton, Zurich Global Information Security
* Matthew Green
* Mayan Arora aka Mayan Mohan
* Mayuresh Dani, Qualys
* Michael Raggi @aRtAGGI
* Microsoft Detection and Response Team (DART)
* Microsoft Security
* Mike Burns, Mandiant
* Mike Moran
* Mnemonic AS
* Mohamed Kmal
* Naveen Vijayaraghavan, Nilesh Dherange (Gurucul)
* NEC
* Nick Carr, Mandiant
* NST Assure Research Team, NetSentries Technologies
* Oleg Kolesnikov, Securonix
* Omkar Gudhate
* Or Kliger, Palo Alto Networks
* Patrick Sungbahadoor
* Pawel Partyka, Microsoft 365 Defender
* Phil Taylor, BT Security
* Pià Consigny, Tenable
* Pooja Natarajan, NEC Corporation India
* Praetorian
* Prasad Somasamudram, McAfee
* Prasanth Sadanala, Cigna Information Protection (CIP) - Threat Response Engineering Team
* Ram Pliskin, Microsoft Azure Security Center
* Regina Elwell
* Rex Guo, @Xiaofei_REX, Confluera
* Richard Julian, Citi
* Rick Cole, Mandiant
* Ruben Dodge, @shotgunner101
* Runa Sandvik
* Sekhar Sarukkai, McAfee 
* Selena Larson, @selenalarson
* Shilpesh Trivedi, Uptycs
* Shlomi Salem, SentinelOne
* Sittikorn Sangrattanapitak
* SOCCRATES
* Stan Hegt, Outflank
* Suzy Schapperle - Microsoft Azure Red Team
* Syed Ummar Farooqh, McAfee
* Taewoo Lee, KISA
* Ted Samuels, Rapid7
* The Wover, @TheRealWover
* Tiago Faria, 3CORESec
* Tim (Wadhwa-)Brown
* Toby Kohlenberg
* Tony Lee
* Travis Smith, Qualys
* TruKno
* Tsubasa Matsuda, NEC Corporation
* Vadim Khrykov
* Vinay Pidathala
* Viren Chaudhari, Qualys
* Wes Hurd
* Wietze Beukema, @wietze
* Will Thomas, Cyjax
* William Cain
* Wojciech Lesicki
* Yoshihiro Kori, NEC Corporation
* Yossi Nisani, Cymptom
* Yusuke Kubo, RedLark, NTT Communications
* Yuval Avrahami, Palo Alto Networks
* Zachary Abzug, @ZackDoesML
* Zachary Stanford, @svch0st
* Zaw Min Htun, @Z3TAE
* Ziv Kaspersky, Cymptom
