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
* [Debugger Evasion](/techniques/T1622) <small style="color:#929393">(v1.0)</small>
* Hide Artifacts: [Process Argument Spoofing](/techniques/T1564/010) <small style="color:#929393">(v1.0)</small>
* Hijack Execution Flow: [KernelCallbackTable](/techniques/T1574/013) <small style="color:#929393">(v1.0)</small>
* Inter-Process Communication: [XPC Services](/techniques/T1559/003) <small style="color:#929393">(v1.0)</small>
* Modify Authentication Process: [Reversible Encryption](/techniques/T1556/005) <small style="color:#929393">(v1.0)</small>
* [Multi-Factor Authentication Request Generation](/techniques/T1621) <small style="color:#929393">(v1.0)</small>
* [Plist File Modification](/techniques/T1647) <small style="color:#929393">(v1.0)</small>
* Process Injection: [ListPlanting](/techniques/T1055/015) <small style="color:#929393">(v1.0)</small>
* Server Software Component: [Terminal Services DLL](/techniques/T1505/005) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* Account Manipulation: [Additional Cloud Roles](/techniques/T1098/003) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* Account Manipulation: [Additional Email Delegate Permissions](/techniques/T1098/002) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* Boot or Logon Initialization Scripts: [Login Hook](/techniques/T1037/002) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* Exfiltration Over Alternative Protocol: [Exfiltration Over Unencrypted Non-C2 Protocol](/techniques/T1048/003) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Multi-Factor Authentication Interception](/techniques/T1111) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Network Service Discovery](/techniques/T1046) <small style="color:#929393">(v2.2&#8594;v3.0)</small>
* Scheduled Task/Job: [At](/techniques/T1053/002) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [System Binary Proxy Execution](/techniques/T1218) <small style="color:#929393">(v2.1&#8594;v3.0)</small>
    * [CMSTP](/techniques/T1218/003) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
    * [Compiled HTML File](/techniques/T1218/001) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
    * [Control Panel](/techniques/T1218/002) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
    * [InstallUtil](/techniques/T1218/004) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
    * [MMC](/techniques/T1218/014) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
    * [Mavinject](/techniques/T1218/013) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
    * [Mshta](/techniques/T1218/005) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
    * [Msiexec](/techniques/T1218/007) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
    * [Odbcconf](/techniques/T1218/008) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
    * [Regsvcs/Regasm](/techniques/T1218/009) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
    * [Regsvr32](/techniques/T1218/010) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
    * [Rundll32](/techniques/T1218/011) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
    * [Verclsid](/techniques/T1218/012) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [System Script Proxy Execution](/techniques/T1216) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
    * [PubPrn](/techniques/T1216/001) <small style="color:#929393">(v1.1&#8594;v2.0)</small>

#### Minor Version Changes

* Abuse Elevation Control Mechanism: [Setuid and Setgid](/techniques/T1548/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Account Access Removal](/techniques/T1531) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Account Manipulation](/techniques/T1098) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
    * [Additional Cloud Credentials](/techniques/T1098/001) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
    * [SSH Authorized Keys](/techniques/T1098/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Adversary-in-the-Middle](/techniques/T1557) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Application Window Discovery](/techniques/T1010) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Archive Collected Data: [Archive via Utility](/techniques/T1560/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Automated Collection](/techniques/T1119) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Boot or Logon Autostart Execution: [Kernel Modules and Extensions](/techniques/T1547/006) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Boot or Logon Autostart Execution: [Port Monitors](/techniques/T1547/010) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Boot or Logon Autostart Execution: [Re-opened Applications](/techniques/T1547/007) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Brute Force](/techniques/T1110) <small style="color:#929393">(v2.3&#8594;v2.4)</small>
    * [Password Cracking](/techniques/T1110/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Password Guessing](/techniques/T1110/001) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Build Image on Host](/techniques/T1612) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Cloud Infrastructure Discovery](/techniques/T1580) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Command and Scripting Interpreter](/techniques/T1059) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
    * [PowerShell](/techniques/T1059/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Visual Basic](/techniques/T1059/005) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Compromise Infrastructure](/techniques/T1584) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [DNS Server](/techniques/T1584/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Domains](/techniques/T1584/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Container Administration Command](/techniques/T1609) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Create Account: [Cloud Account](/techniques/T1136/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Create or Modify System Process](/techniques/T1543) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Windows Service](/techniques/T1543/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Credentials from Password Stores: [Keychain](/techniques/T1555/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Credentials from Password Stores: [Securityd Memory](/techniques/T1555/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Data Encrypted for Impact](/techniques/T1486) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Data Manipulation](/techniques/T1565) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Runtime Data Manipulation](/techniques/T1565/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Stored Data Manipulation](/techniques/T1565/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Transmitted Data Manipulation](/techniques/T1565/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Data Staged](/techniques/T1074) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
    * [Local Data Staging](/techniques/T1074/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Data from Local System](/techniques/T1005) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Defacement](/techniques/T1491) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
    * [External Defacement](/techniques/T1491/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Internal Defacement](/techniques/T1491/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Deploy Container](/techniques/T1610) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Drive-by Compromise](/techniques/T1189) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* Endpoint Denial of Service: [Application Exhaustion Flood](/techniques/T1499/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Endpoint Denial of Service: [Application or System Exploitation](/techniques/T1499/004) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Endpoint Denial of Service: [OS Exhaustion Flood](/techniques/T1499/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Endpoint Denial of Service: [Service Exhaustion Flood](/techniques/T1499/002) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Escape to Host](/techniques/T1611) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Event Triggered Execution: [PowerShell Profile](/techniques/T1546/013) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Exfiltration Over Other Network Medium: [Exfiltration Over Bluetooth](/techniques/T1011/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [File and Directory Discovery](/techniques/T1083) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Firmware Corruption](/techniques/T1495) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Gather Victim Identity Information: [Email Addresses](/techniques/T1589/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Hardware Additions](/techniques/T1200) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Hide Artifacts: [Email Hiding Rules](/techniques/T1564/008) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Hide Artifacts: [Hidden Users](/techniques/T1564/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Hide Artifacts: [Hidden Window](/techniques/T1564/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Hijack Execution Flow](/techniques/T1574) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Impair Defenses: [Disable Cloud Logs](/techniques/T1562/008) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Impair Defenses: [Downgrade Attack](/techniques/T1562/010) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Impair Defenses: [Impair Command History Logging](/techniques/T1562/003) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Implant Internal Image](/techniques/T1525) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Indicator Removal on Host](/techniques/T1070) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
    * [Clear Command History](/techniques/T1070/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Clear Windows Event Logs](/techniques/T1070/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [File Deletion](/techniques/T1070/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Ingress Tool Transfer](/techniques/T1105) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Inhibit System Recovery](/techniques/T1490) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Input Capture: [GUI Input Capture](/techniques/T1056/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Inter-Process Communication](/techniques/T1559) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Dynamic Data Exchange](/techniques/T1559/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Internal Spearphishing](/techniques/T1534) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Lateral Tool Transfer](/techniques/T1570) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Modify Authentication Process](/techniques/T1556) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Network Boundary Bridging](/techniques/T1599) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Network Denial of Service: [Direct Network Flood](/techniques/T1498/001) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Network Denial of Service: [Reflection Amplification](/techniques/T1498/002) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Network Sniffing](/techniques/T1040) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* OS Credential Dumping: [NTDS](/techniques/T1003/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Obfuscated Files or Information: [Software Packing](/techniques/T1027/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Password Policy Discovery](/techniques/T1201) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Peripheral Device Discovery](/techniques/T1120) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Phishing: [Spearphishing Link](/techniques/T1566/002) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* Phishing for Information: [Spearphishing Link](/techniques/T1598/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Pre-OS Boot: [Component Firmware](/techniques/T1542/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Process Injection: [Process Hollowing](/techniques/T1055/012) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Remote Access Software](/techniques/T1219) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Remote Services: [Remote Desktop Protocol](/techniques/T1021/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Remote System Discovery](/techniques/T1018) <small style="color:#929393">(v3.2&#8594;v3.3)</small>
* [Resource Hijacking](/techniques/T1496) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Rogue Domain Controller](/techniques/T1207) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Scheduled Task/Job](/techniques/T1053) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
    * [Container Orchestration Job](/techniques/T1053/007) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Scheduled Task](/techniques/T1053/005) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Server Software Component](/techniques/T1505) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Software Discovery: [Security Software Discovery](/techniques/T1518/001) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Stage Capabilities: [Drive-by Target](/techniques/T1608/004) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Steal Application Access Token](/techniques/T1528) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Steal or Forge Kerberos Tickets](/techniques/T1558) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
    * [Kerberoasting](/techniques/T1558/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Subvert Trust Controls: [Mark-of-the-Web Bypass](/techniques/T1553/005) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Supply Chain Compromise](/techniques/T1195) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [System Information Discovery](/techniques/T1082) <small style="color:#929393">(v2.3&#8594;v2.4)</small>
* [System Network Configuration Discovery](/techniques/T1016) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [System Network Connections Discovery](/techniques/T1049) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* [System Service Discovery](/techniques/T1007) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [System Services](/techniques/T1569) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [System Shutdown/Reboot](/techniques/T1529) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Template Injection](/techniques/T1221) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Traffic Signaling](/techniques/T1205) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* [Transfer Data to Cloud Account](/techniques/T1537) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Unsecured Credentials: [Bash History](/techniques/T1552/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Unsecured Credentials: [Cloud Instance Metadata API](/techniques/T1552/005) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Unsecured Credentials: [Container API](/techniques/T1552/007) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Use Alternate Authentication Material: [Application Access Token](/techniques/T1550/001) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [User Execution](/techniques/T1204) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
    * [Malicious File](/techniques/T1204/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Valid Accounts](/techniques/T1078) <small style="color:#929393">(v2.3&#8594;v2.4)</small>
    * [Cloud Accounts](/techniques/T1078/004) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Video Capture](/techniques/T1125) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

#### Other Version Changes

* Create or Modify System Process: [Launch Agent](/techniques/T1543/001) <small style="color:#eb6635">(v1.2&#8594;v1.4)</small>
* [Exploitation for Client Execution](/techniques/T1203) <small style="color:#eb6635">(v1.2&#8594;v1.4)</small>
* [Gather Victim Identity Information](/techniques/T1589) <small style="color:#eb6635">(v1.0&#8594;v1.2)</small>

#### Metadata-only Changes

* [Abuse Elevation Control Mechanism](/techniques/T1548) <small style="color:#929393">(v1.0)</small>
    * [Bypass User Account Control](/techniques/T1548/002) <small style="color:#929393">(v2.0)</small>
    * [Sudo and Sudo Caching](/techniques/T1548/003) <small style="color:#929393">(v1.0)</small>
* [Active Scanning](/techniques/T1595) <small style="color:#929393">(v1.0)</small>
* [Archive Collected Data](/techniques/T1560) <small style="color:#929393">(v1.0)</small>
* [Automated Exfiltration](/techniques/T1020) <small style="color:#929393">(v1.2)</small>
    * [Traffic Duplication](/techniques/T1020/001) <small style="color:#929393">(v1.1)</small>
* [Boot or Logon Autostart Execution](/techniques/T1547) <small style="color:#929393">(v1.1)</small>
    * [Authentication Package](/techniques/T1547/002) <small style="color:#929393">(v1.0)</small>
    * [LSASS Driver](/techniques/T1547/008) <small style="color:#929393">(v1.0)</small>
    * [Registry Run Keys / Startup Folder](/techniques/T1547/001) <small style="color:#929393">(v1.1)</small>
    * [Time Providers](/techniques/T1547/003) <small style="color:#929393">(v1.0)</small>
    * [Winlogon Helper DLL](/techniques/T1547/004) <small style="color:#929393">(v1.0)</small>
* [Boot or Logon Initialization Scripts](/techniques/T1037) <small style="color:#929393">(v2.1)</small>
    * [Startup Items](/techniques/T1037/005) <small style="color:#929393">(v1.0)</small>
* [Browser Extensions](/techniques/T1176) <small style="color:#929393">(v1.2)</small>
* [Browser Session Hijacking](/techniques/T1185) <small style="color:#929393">(v2.0)</small>
* [Cloud Storage Object Discovery](/techniques/T1619) <small style="color:#929393">(v1.0)</small>
* Command and Scripting Interpreter: [AppleScript](/techniques/T1059/002) <small style="color:#929393">(v1.1)</small>
* Command and Scripting Interpreter: [Network Device CLI](/techniques/T1059/008) <small style="color:#929393">(v1.1)</small>
* Compromise Infrastructure: [Botnet](/techniques/T1584/005) <small style="color:#929393">(v1.0)</small>
* [Credentials from Password Stores](/techniques/T1555) <small style="color:#929393">(v1.0)</small>
    * [Credentials from Web Browsers](/techniques/T1555/003) <small style="color:#929393">(v1.1)</small>
    * [Password Managers](/techniques/T1555/005) <small style="color:#929393">(v1.0)</small>
* [Data from Configuration Repository](/techniques/T1602) <small style="color:#929393">(v1.0)</small>
    * [Network Device Configuration Dump](/techniques/T1602/002) <small style="color:#929393">(v1.0)</small>
* [Data from Information Repositories](/techniques/T1213) <small style="color:#929393">(v3.2)</small>
* Develop Capabilities: [Malware](/techniques/T1587/001) <small style="color:#929393">(v1.2)</small>
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
    * [Windows Management Instrumentation Event Subscription](/techniques/T1546/003) <small style="color:#929393">(v1.2)</small>
* [Exfiltration Over Other Network Medium](/techniques/T1011) <small style="color:#929393">(v1.1)</small>
* [Exploit Public-Facing Application](/techniques/T1190) <small style="color:#929393">(v2.3)</small>
* [Exploitation of Remote Services](/techniques/T1210) <small style="color:#929393">(v1.1)</small>
* [Hide Artifacts](/techniques/T1564) <small style="color:#929393">(v1.1)</small>
* [Impair Defenses](/techniques/T1562) <small style="color:#929393">(v1.2)</small>
* [Input Capture](/techniques/T1056) <small style="color:#929393">(v1.2)</small>
* Modify Authentication Process: [Network Device Authentication](/techniques/T1556/004) <small style="color:#929393">(v2.0)</small>
* [Native API](/techniques/T1106) <small style="color:#929393">(v2.1)</small>
* [Network Denial of Service](/techniques/T1498) <small style="color:#929393">(v1.1)</small>
* [Non-Application Layer Protocol](/techniques/T1095) <small style="color:#929393">(v2.1)</small>
* [OS Credential Dumping](/techniques/T1003) <small style="color:#929393">(v2.1)</small>
* [Obfuscated Files or Information](/techniques/T1027) <small style="color:#929393">(v1.2)</small>
* Permission Groups Discovery: [Cloud Groups](/techniques/T1069/003) <small style="color:#929393">(v1.3)</small>
* [Phishing](/techniques/T1566) <small style="color:#929393">(v2.2)</small>
* [Phishing for Information](/techniques/T1598) <small style="color:#929393">(v1.1)</small>
* [Pre-OS Boot](/techniques/T1542) <small style="color:#929393">(v1.1)</small>
* [Process Injection](/techniques/T1055) <small style="color:#929393">(v1.2)</small>
    * [VDSO Hijacking](/techniques/T1055/014) <small style="color:#929393">(v1.0)</small>
* [Reflective Code Loading](/techniques/T1620) <small style="color:#929393">(v1.0)</small>
* [Remote Services](/techniques/T1021) <small style="color:#929393">(v1.2)</small>
* Scheduled Task/Job: [Cron](/techniques/T1053/003) <small style="color:#929393">(v1.1)</small>
* [Shared Modules](/techniques/T1129) <small style="color:#929393">(v2.1)</small>
* [Software Discovery](/techniques/T1518) <small style="color:#929393">(v1.3)</small>
* [Stage Capabilities](/techniques/T1608) <small style="color:#929393">(v1.1)</small>
* [Subvert Trust Controls](/techniques/T1553) <small style="color:#929393">(v1.1)</small>
* Supply Chain Compromise: [Compromise Software Dependencies and Development Tools](/techniques/T1195/001) <small style="color:#929393">(v1.0)</small>
* Supply Chain Compromise: [Compromise Software Supply Chain](/techniques/T1195/002) <small style="color:#929393">(v1.0)</small>
* [System Owner/User Discovery](/techniques/T1033) <small style="color:#929393">(v1.3)</small>
* Traffic Signaling: [Port Knocking](/techniques/T1205/001) <small style="color:#929393">(v1.1)</small>
* [Unsecured Credentials](/techniques/T1552) <small style="color:#929393">(v1.2)</small>
* [Use Alternate Authentication Material](/techniques/T1550) <small style="color:#929393">(v1.2)</small>
* Valid Accounts: [Domain Accounts](/techniques/T1078/002) <small style="color:#929393">(v1.2)</small>
* [Windows Management Instrumentation](/techniques/T1047) <small style="color:#929393">(v1.2)</small>

#### Revocations


### Mobile

#### Metadata-only Changes

* [Install Insecure or Malicious Configuration](/techniques/T1478) <small style="color:#929393">(v1.0)</small>

### ICS

#### Major Version Changes

* [Activate Firmware Update Mode](/Technique/T0800) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Alarm Suppression](/Technique/T0878) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Automated Collection](/Technique/T0802) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Block Command Message](/Technique/T0803) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Block Reporting Message](/Technique/T0804) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Block Serial COM](/Technique/T0805) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Brute Force I/O](/Technique/T0806) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Change Operating Mode](/Technique/T0858) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Command-Line Interface](/Technique/T0807) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Commonly Used Port](/Technique/T0885) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Connection Proxy](/Technique/T0884) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Damage to Property](/Technique/T0879) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Data Destruction](/Technique/T0809) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Data from Information Repositories](/Technique/T0811) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Default Credentials](/Technique/T0812) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Denial of Control](/Technique/T813) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Denial of Service](/Technique/T0814) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Denial of View](/Technique/T0815) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Detect Operating Mode](/Technique/T0868) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Device Restart/Shutdown](/Technique/T0816) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Drive-by Compromise](/Technique/T0817) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Execution through API](/Technique/T0871) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Exploit Public-Facing Application](/Technique/T0819) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Exploitation for Evasion](/Technique/T0820) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Exploitation for Privilege Escalation](/Technique/T0890) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Exploitation of Remote Services](/Technique/T0866) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [External Remote Services](/Technique/T0822) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Graphical User Interface](/Technique/T0823) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Hooking](/Technique/T0874) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [I/O Image](/Technique/T0877) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Indicator Removal on Host](/Technique/T0872) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Internet Accessible Device](/Technique/T0883) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Lateral Tool Transfer](/Technique/T0867) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Loss of Availability](/Technique/T0826) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Loss of Control](/Technique/T0827) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Loss of Productivity and Revenue](/Technique/T0828) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Loss of Protection](/Technique/T0837) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Loss of Safety](/Technique/T0880) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Loss of View](/Technique/T0829) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Man in the Middle](/Technique/T0830) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Manipulate I/O Image](/Technique/T835) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Manipulation of Control](/Technique/T0831) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Manipulation of View](/Technique/T0832) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Masquerading](/Technique/T0849) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Modify Alarm Settings](/Technique/T0838) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Modify Controller Tasking](/Technique/T0821) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Modify Parameter](/Technique/T0836) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Modify Program](/Technique/T0889) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Module Firmware](/Technique/T0839) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Monitor Process State](/Technique/T0801) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Native API](/Technique/T0834) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Network Connection Enumeration](/Technique/T0840) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Network Sniffing](/Technique/T0842) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Point & Tag Identification](/Technique/T0861) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Program Download](/Technique/T0843) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Program Upload](/Technique/T0845) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Project File Infection](/Technique/T0873) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Remote Services](/Technique/T0886) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Remote System Discovery](/Technique/T0846) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Remote System Information Discovery](/Technique/T0888) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Replication Through Removable Media](/Technique/T0847) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Rogue Master](/Technique/T0848) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Rootkit](/Technique/T0851) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Screen Capture](/Technique/T0852) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Scripting](/Technique/T0853) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Service Stop](/Technique/T0881) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Spearphishing Attachment](/Technique/T0865) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Spoof Reporting Message](/Technique/T0856) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Standard Application Layer Protocol](/Technique/T0869) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Supply Chain Compromise](/Technique/T0862) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [System Firmware](/Technique/T0857) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Theft of Operational Information](/Technique/T0882) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Transient Cyber Asset](/Technique/T0864) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Unauthorized Command Message](/Technique/T0855) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [User Execution](/Technique/T0863) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Valid Accounts](/Technique/T0859) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Wireless Compromise](/Technique/T0860) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>
* [Wireless Sniffing](/Technique/T0887) <small style="color:#eb6635">(v0.0&#8594;v1.0)</small>

## Software

### Enterprise

#### New Software

* [AADInternals](/software/S0677) <small style="color:#929393">(v1.0)</small>
* [CaddyWiper](/software/S0693) <small style="color:#929393">(v1.0)</small>
* [CharmPower](/software/S0674) <small style="color:#929393">(v1.0)</small>
* [Chrommme](/software/S0667) <small style="color:#929393">(v1.0)</small>
* [Clambling](/software/S0660) <small style="color:#929393">(v1.0)</small>
* [Cyclops Blink](/software/S0687) <small style="color:#929393">(v1.0)</small>
* [DRATzarus](/software/S0694) <small style="color:#929393">(v1.0)</small>
* [DarkWatchman](/software/S0673) <small style="color:#929393">(v1.0)</small>
* [Diavol](/software/S0659) <small style="color:#929393">(v1.0)</small>
* [Donut](/software/S0695) <small style="color:#929393">(v1.0)</small>
* [Ferocious](/software/S0679) <small style="color:#929393">(v1.0)</small>
* [Flagpro](/software/S0696) <small style="color:#929393">(v1.0)</small>
* [FoggyWeb](/software/S0661) <small style="color:#929393">(v1.0)</small>
* [Gelsemium](/software/S0666) <small style="color:#929393">(v1.0)</small>
* [Green Lambert](/software/S0690) <small style="color:#929393">(v1.0)</small>
* [HermeticWiper](/software/S0697) <small style="color:#929393">(v1.0)</small>
* [HermeticWizard](/software/S0698) <small style="color:#929393">(v1.0)</small>
* [KOCTOPUS](/software/S0669) <small style="color:#929393">(v1.0)</small>
* [LitePower](/software/S0680) <small style="color:#929393">(v1.0)</small>
* [Lizar](/software/S0681) <small style="color:#929393">(v1.0)</small>
* [Meteor](/software/S0688) <small style="color:#929393">(v1.0)</small>
* [Mythic](/software/S0699) <small style="color:#929393">(v1.0)</small>
* [Neoichor](/software/S0691) <small style="color:#929393">(v1.0)</small>
* [Pandora](/software/S0664) <small style="color:#929393">(v1.0)</small>
* [Peirates](/software/S0683) <small style="color:#929393">(v1.0)</small>
* [PowerPunch](/software/S0685) <small style="color:#929393">(v1.0)</small>
* [QuietSieve](/software/S0686) <small style="color:#929393">(v1.0)</small>
* [RCSession](/software/S0662) <small style="color:#929393">(v1.0)</small>
* [ROADTools](/software/S0684) <small style="color:#929393">(v1.0)</small>
* [SILENTTRINITY](/software/S0692) <small style="color:#929393">(v1.0)</small>
* [SysUpdate](/software/S0663) <small style="color:#929393">(v1.0)</small>
* [ThreatNeedle](/software/S0665) <small style="color:#929393">(v1.0)</small>
* [TinyTurla](/software/S0668) <small style="color:#929393">(v1.0)</small>
* [Tomiris](/software/S0671) <small style="color:#929393">(v1.0)</small>
* [Torisma](/software/S0678) <small style="color:#929393">(v1.0)</small>
* [TrailBlazer](/software/S0682) <small style="color:#929393">(v1.0)</small>
* [WarzoneRAT](/software/S0670) <small style="color:#929393">(v1.0)</small>
* [WhisperGate](/software/S0689) <small style="color:#929393">(v1.0)</small>
* [Zox](/software/S0672) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* [Backdoor.Oldrea](/software/S0093) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Bisonal](/software/S0268) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* [Conti](/software/S0575) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [EKANS](/software/S0605) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [GoldMax](/software/S0588) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Hydraq](/software/S0203) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [KONNI](/software/S0356) <small style="color:#929393">(v1.4&#8594;v2.0)</small>
* [Koadic](/software/S0250) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [LockerGoga](/software/S0372) <small style="color:#929393">(v1.3&#8594;v2.0)</small>
* [PLEAD](/software/S0435) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [PlugX](/software/S0013) <small style="color:#929393">(v2.1&#8594;v3.0)</small>
* [PoisonIvy](/software/S0012) <small style="color:#929393">(v1.3&#8594;v2.0)</small>
* [Pteranodon](/software/S0147) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [REvil](/software/S0496) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* [Trojan.Karagany](/software/S0094) <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* [Winnti for Windows](/software/S0141) <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* [ftp](/software/S0095) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [gh0st RAT](/software/S0032) <small style="color:#929393">(v2.3&#8594;v3.0)</small>

#### Minor Version Changes

* [AppleSeed](/software/S0622) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Arp](/software/S0099) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [BloodHound](/software/S0521) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Brave Prince](/software/S0252) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [CHOPSTICK](/software/S0023) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [Cobalt Strike](/software/S0154) <small style="color:#929393">(v1.7&#8594;v1.8)</small>
* [Derusbi](/software/S0021) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Empire](/software/S0363) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [FinFisher](/software/S0182) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Gold Dragon](/software/S0249) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Hikit](/software/S0009) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [HyperBro](/software/S0398) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [InvisiMole](/software/S0260) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [KillDisk](/software/S0607) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Mimikatz](/software/S0002) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [Ngrok](/software/S0508) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [OSX_OCEANLOTUS.D](/software/S0352) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [Orz](/software/S0229) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [Ping](/software/S0097) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [PoetRAT](/software/S0428) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Prikormka](/software/S0113) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [QuasarRAT](/software/S0262) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [ROKRAT](/software/S0240) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* [Remcos](/software/S0332) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Responder](/software/S0174) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Ryuk](/software/S0446) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [SUNBURST](/software/S0559) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [SombRAT](/software/S0615) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Stuxnet](/software/S0603) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [ThiefQuest](/software/S0595) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [USBStealer](/software/S0136) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Waterbear](/software/S0579) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [XCSSET](/software/S0658) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [ZxShell](/software/S0412) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [at](/software/S0110) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [njRAT](/software/S0385) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [route](/software/S0103) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [schtasks](/software/S0111) <small style="color:#929393">(v1.1&#8594;v1.2)</small>

#### Metadata-only Changes

* [Anchor](/software/S0504) <small style="color:#929393">(v1.0)</small>
* [BS2005](/software/S0014) <small style="color:#929393">(v1.1)</small>
* [BoomBox](/software/S0635) <small style="color:#929393">(v1.0)</small>
* [Bundlore](/software/S0482) <small style="color:#929393">(v1.1)</small>
* [China Chopper](/software/S0020) <small style="color:#929393">(v2.3)</small>
* [EVILNUM](/software/S0568) <small style="color:#929393">(v1.0)</small>
* [Industroyer](/software/S0604) <small style="color:#929393">(v1.0)</small>
* [Kobalos](/software/S0641) <small style="color:#929393">(v1.0)</small>
* [MarkiRAT](/software/S0652) <small style="color:#929393">(v1.0)</small>
* [Maze](/software/S0449) <small style="color:#929393">(v1.2)</small>
* [Mis-Type](/software/S0084) <small style="color:#929393">(v1.1)</small>
* [Misdat](/software/S0083) <small style="color:#929393">(v1.1)</small>
* [Nidiran](/software/S0118) <small style="color:#929393">(v1.1)</small>
* [Octopus](/software/S0340) <small style="color:#929393">(v2.0)</small>
* [S-Type](/software/S0085) <small style="color:#929393">(v1.1)</small>
* [SYNful Knock](/software/S0519) <small style="color:#929393">(v1.0)</small>
* [TSCookie](/software/S0436) <small style="color:#929393">(v1.0)</small>
* [WindTail](/software/S0466) <small style="color:#929393">(v1.0)</small>
* [ZLib](/software/S0086) <small style="color:#929393">(v1.1)</small>

#### Deprecations

* [TRITON](/software/S0609) <small style="color:#929393">(v1.0)</small>

### Mobile

#### Metadata-only Changes

* [Monokle](/software/S0407) <small style="color:#929393">(v1.2)</small>

### ICS

#### Major Version Changes

* [Backdoor.Oldrea](/software/S0093) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [EKANS](/software/S0605) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [LockerGoga](/software/S0372) <small style="color:#929393">(v1.3&#8594;v2.0)</small>
* [REvil](/software/S0496) <small style="color:#929393">(v1.2&#8594;v2.0)</small>

#### Minor Version Changes

* [KillDisk](/software/S0607) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Ryuk](/software/S0446) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Stuxnet](/software/S0603) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

#### Metadata-only Changes

* [ACAD/Medre.A](/Software/S0018) <small style="color:#929393">(v1.0)</small>
* [Industroyer](/software/S0604) <small style="color:#929393">(v1.0)</small>
* [PLC-Blaster](/Software/S0009) <small style="color:#929393">(v1.0)</small>
* [Triton](/Software/S0013) <small style="color:#929393">(v1.0)</small>
* [VPNFilter](/Software/S0002) <small style="color:#929393">(v1.0)</small>

## Groups

### Enterprise

#### New Groups

* [Aquatic Panda](/groups/G0143) <small style="color:#929393">(v1.0)</small>
* [Confucius](/groups/G0142) <small style="color:#929393">(v1.0)</small>
* [Gelsemium](/groups/G0141) <small style="color:#929393">(v1.0)</small>
* [LazyScripter](/groups/G0140) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* [APT28](/groups/G0007) <small style="color:#929393">(v3.2&#8594;v4.0)</small>
* [APT29](/groups/G0016) <small style="color:#929393">(v2.1&#8594;v3.0)</small>
* [Axiom](/groups/G0001) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* [BlackTech](/groups/G0098) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Dragonfly](/groups/G0035) <small style="color:#929393">(v2.1&#8594;v3.0)</small>
* [Gamaredon Group](/groups/G0047) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* [Ke3chang](/groups/G0004) <small style="color:#929393">(v1.4&#8594;v2.0)</small>
* [Lazarus Group](/groups/G0032) <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* [Mustang Panda](/groups/G0129) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Threat Group-3390](/groups/G0027) <small style="color:#929393">(v1.5&#8594;v2.0)</small>
* [Turla](/groups/G0010) <small style="color:#929393">(v2.1&#8594;v3.0)</small>
* [WIRTE](/groups/G0090) <small style="color:#929393">(v1.2&#8594;v2.0)</small>

#### Minor Version Changes

* [FIN7](/groups/G0046) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [HAFNIUM](/groups/G0125) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Indrik Spider](/groups/G0119) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Kimsuky](/groups/G0094) <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* [Magic Hound](/groups/G0059) <small style="color:#929393">(v4.0&#8594;v4.1)</small>
* [Sandworm Team](/groups/G0034) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [TeamTNT](/groups/G0139) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Tonto Team](/groups/G0131) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Volatile Cedar](/groups/G0123) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Winnti Group](/groups/G0044) <small style="color:#929393">(v1.1&#8594;v1.2)</small>

#### Metadata-only Changes

* [APT38](/groups/G0082) <small style="color:#929393">(v2.0)</small>
* [Ajax Security Team](/groups/G0130) <small style="color:#929393">(v1.0)</small>
* [Chimera](/groups/G0114) <small style="color:#929393">(v2.1)</small>
* [Dust Storm](/groups/G0031) <small style="color:#929393">(v1.0)</small>
* [Ferocious Kitten](/groups/G0137) <small style="color:#929393">(v1.0)</small>
* [Leviathan](/groups/G0065) <small style="color:#929393">(v3.0)</small>
* [OilRig](/groups/G0049) <small style="color:#929393">(v3.0)</small>
* [Operation Wocao](/groups/G0116) <small style="color:#929393">(v1.0)</small>
* [Orangeworm](/groups/G0071) <small style="color:#929393">(v1.1)</small>
* [Patchwork](/groups/G0040) <small style="color:#929393">(v1.4)</small>
* [Suckfly](/groups/G0039) <small style="color:#929393">(v1.1)</small>
* [TA505](/groups/G0092) <small style="color:#929393">(v1.3)</small>
* [Transparent Tribe](/groups/G0134) <small style="color:#929393">(v1.0)</small>

#### Revocations

* Dragonfly 2.0 (revoked by [Dragonfly](/groups/G0035)) <small style="color:#929393">(v2.1)</small>

### Mobile

### ICS

#### Major Version Changes

* [Dragonfly](/groups/G0035) <small style="color:#929393">(v2.1&#8594;v3.0)</small>
* [Lazarus Group](/groups/G0032) <small style="color:#929393">(v2.0&#8594;v3.0)</small>

#### Minor Version Changes

* [Sandworm Team](/groups/G0034) <small style="color:#929393">(v2.1&#8594;v2.2)</small>

#### Other Version Changes

* [HEXANE](/Group/G0005) <small style="color:#eb6635">(v1.1&#8594;v1.0)</small>

#### Metadata-only Changes

* [ALLANITE](/Group/G0009) <small style="color:#929393">(v1.0)</small>
* [OilRig](/groups/G0049) <small style="color:#929393">(v3.0)</small>

## Campaigns

### Enterprise

### Mobile

### ICS

## Mitigations

### Enterprise

#### Minor Version Changes

* [Execution Prevention](/mitigations/M1038) <small style="color:#929393">(v1.1&#8594;v1.2)</small>

### Mobile

### ICS

#### Other Version Changes

* [Filter Network Traffic](/Mitigation/M0937) <small style="color:#eb6635">(v1.1&#8594;v1.0)</small>

#### Metadata-only Changes

* [Access Management](/Mitigation/M0801) <small style="color:#929393">(v1.0)</small>
* [Account Use Policies](/Mitigation/M0936) <small style="color:#929393">(v1.0)</small>
* [Active Directory Configuration](/Mitigation/M0915) <small style="color:#929393">(v1.0)</small>
* [Antivirus/Antimalware](/Mitigation/M0949) <small style="color:#929393">(v1.0)</small>
* [Application Developer Guidance](/Mitigation/M0913) <small style="color:#929393">(v1.0)</small>
* [Application Isolation and Sandboxing](/Mitigation/M0948) <small style="color:#929393">(v1.0)</small>
* [Audit](/Mitigation/M0947) <small style="color:#929393">(v1.0)</small>
* [Authorization Enforcement](/Mitigation/M0800) <small style="color:#929393">(v1.0)</small>
* [Boot Integrity](/Mitigation/M0946) <small style="color:#929393">(v1.0)</small>
* [Code Signing](/Mitigation/M0945) <small style="color:#929393">(v1.0)</small>
* [Communication Authenticity](/Mitigation/M0802) <small style="color:#929393">(v1.0)</small>
* [Data Backup](/Mitigation/M0953) <small style="color:#929393">(v1.0)</small>
* [Data Loss Prevention](/Mitigation/M0803) <small style="color:#929393">(v1.0)</small>
* [Disable or Remove Feature or Program](/Mitigation/M0942) <small style="color:#929393">(v1.0)</small>
* [Encrypt Network Traffic](/Mitigation/M0808) <small style="color:#929393">(v1.0)</small>
* [Encrypt Sensitive Information](/Mitigation/M0941) <small style="color:#929393">(v1.0)</small>
* [Execution Prevention](/Mitigation/M0938) <small style="color:#929393">(v1.0)</small>
* [Exploit Protection](/Mitigation/M0950) <small style="color:#929393">(v1.0)</small>
* [Human User Authentication](/Mitigation/M0804) <small style="color:#929393">(v1.0)</small>
* [Limit Access to Resource Over Network](/Mitigation/M0935) <small style="color:#929393">(v1.0)</small>
* [Limit Hardware Installation](/Mitigation/M0934) <small style="color:#929393">(v1.0)</small>
* [Mechanical Protection Layers](/Mitigation/M0805) <small style="color:#929393">(v1.0)</small>
* [Minimize Wireless Signal Propagation](/Mitigation/M0806) <small style="color:#929393">(v1.0)</small>
* [Mitigation Limited or Not Effective](/Mitigation/M0816) <small style="color:#929393">(v1.0)</small>
* [Multi-factor Authentication](/Mitigation/M0932) <small style="color:#929393">(v1.0)</small>
* [Network Allowlists](/Mitigation/M0807) <small style="color:#929393">(v1.0)</small>
* [Network Intrusion Prevention](/Mitigation/M0931) <small style="color:#929393">(v1.0)</small>
* [Network Segmentation](/Mitigation/M0930) <small style="color:#929393">(v1.0)</small>
* [Operating System Configuration](/Mitigation/M0928) <small style="color:#929393">(v1.0)</small>
* [Operational Information Confidentiality](/Mitigation/M0809) <small style="color:#929393">(v1.0)</small>
* [Out-of-Band Communications Channel](/Mitigation/M0810) <small style="color:#929393">(v1.0)</small>
* [Password Policies](/Mitigation/M0927) <small style="color:#929393">(v1.0)</small>
* [Privileged Account Management](/Mitigation/M0926) <small style="color:#929393">(v1.0)</small>
* [Redundancy of Service](/Mitigation/M0811) <small style="color:#929393">(v1.0)</small>
* [Restrict File and Directory Permissions](/Mitigation/M0922) <small style="color:#929393">(v1.0)</small>
* [Restrict Library Loading](/Mitigation/M0944) <small style="color:#929393">(v1.0)</small>
* [Restrict Registry Permissions](/Mitigation/M0924) <small style="color:#929393">(v1.0)</small>
* [Restrict Web-Based Content](/Mitigation/M0921) <small style="color:#929393">(v1.0)</small>
* [SSL/TLS Inspection](/Mitigation/M0920) <small style="color:#929393">(v1.0)</small>
* [Safety Instrumented Systems](/Mitigation/M0812) <small style="color:#929393">(v1.0)</small>
* [Software Configuration](/Mitigation/M0954) <small style="color:#929393">(v1.0)</small>
* [Software Process and Device Authentication](/Mitigation/M0813) <small style="color:#929393">(v1.0)</small>
* [Static Network Configuration](/Mitigation/M0814) <small style="color:#929393">(v1.0)</small>
* [Supply Chain Management](/Mitigation/M0817) <small style="color:#929393">(v1.0)</small>
* [Threat Intelligence Program](/Mitigation/M0919) <small style="color:#929393">(v1.0)</small>
* [Update Software](/Mitigation/M0951) <small style="color:#929393">(v1.0)</small>
* [User Account Management](/Mitigation/M0918) <small style="color:#929393">(v1.0)</small>
* [User Training](/Mitigation/M0917) <small style="color:#929393">(v1.0)</small>
* [Vulnerability Scanning](/Mitigation/M0916) <small style="color:#929393">(v1.0)</small>
* [Watchdog Timers](/Mitigation/M0815) <small style="color:#929393">(v1.0)</small>

## Data Sources

### Enterprise

#### Metadata-only Changes

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

#### Metadata-only Changes

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

* Abhijit Mohanta, @abhijit_mohanta, Uptycs
* Akshat Pradhan, Qualys
* Alex Parsons, Crowdstrike
* Alex Spivakovsky, Pentera
* Andrew Northern, @ex_raritas
* Antonio Piazza, @antman1p
* Austin Clark, @c2defense
* Bryan Campbell, @bry_campbell
* Center for Threat-Informed Defense (CTID)
* Chris Romano, Crowdstrike
* Clément Notin, Tenable
* Cody Thomas, SpecterOps
* Craig Smith, BT Security
* Csaba Fitzl @theevilbit of Offensive Security
* Daisuke Suzuki
* Daniel Acevedo, Blackbot
* Daniel Feichter, @VirtualAllocEx, Infosec Tirol
* Daniyal Naeem, BT Security
* Darin Smith, Cisco
* Dragos Threat Intelligence
* Dror Alon, Palo Alto Networks
* Edward Millington
* Elvis Veliz, Citi
* Eric Kaiser @ideologysec
* ESET
* ExtraHop
* Hannah Simes, BT Security
* Harshal Tupsamudre, Qualys
* Hiroki Nagahama, NEC Corporation
* Isif Ibrahima, Mandiant
* James_inthe_box, Me
* Jan Petrov, Citi
* Jannie Li, Microsoft Threat Intelligence Center (MSTIC)
* Jen Burns, HubSpot
* Jeremy Galloway
* Joas Antonio dos Santos, @C0d3Cr4zy, Inmetrics
* John Page (aka hyp3rlinx), ApparitionSec
* Jon Sternstein, Stern Security
* Kobi Haimovich, CardinalOps
* Krishnan Subramanian, @krish203
* Kyaw Pyiyt Htet, @KyawPyiytHtet
* Lior Ribak, SentinelOne
* Manikantan Srinivasan, NEC Corporation India
* Massimiliano Romano, BT Security
* Matthew Green
* Mayan Arora aka Mayan Mohan
* Mayuresh Dani, Qualys
* Michael Raggi @aRtAGGI
* Mohamed Kmal
* NEC
* NST Assure Research Team, NetSentries Technologies
* Oleg Kolesnikov, Securonix
* Or Kliger, Palo Alto Networks
* Pawel Partyka, Microsoft 365 Defender
* Phil Taylor, BT Security
* Pià Consigny, Tenable
* Pooja Natarajan, NEC Corporation India
* Praetorian
* Prasad Somasamudram, McAfee
* Ram Pliskin, Microsoft Azure Security Center
* Richard Julian, Citi
* Runa Sandvik
* Sekhar Sarukkai, McAfee 
* Selena Larson, @selenalarson
* Shilpesh Trivedi, Uptycs
* Sittikorn Sangrattanapitak
* Suzy Schapperle - Microsoft Azure Red Team
* Syed Ummar Farooqh, McAfee
* Taewoo Lee, KISA
* The Wover, @TheRealWover
* Tiago Faria, 3CORESec
* Tony Lee
* Travis Smith, Qualys
* TruKno
* Tsubasa Matsuda, NEC Corporation
* Vinay Pidathala
* Wes Hurd
* Wietze Beukema, @wietze
* Wojciech Lesicki
* Zachary Abzug, @ZackDoesML
* Zachary Stanford, @svch0st
