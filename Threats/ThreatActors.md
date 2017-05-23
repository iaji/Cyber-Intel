# **Threat Actors**

*This document is continuously updated as I find more information*

## 1. **Venomous Bear (Turla Group)**
Updated: 5/17/2017
### Aliases:
```
- Snake
- Group 88
- Waterbug
- WRAITH
- Uroburos
- Pfinet
- TAG_0530
- KRYPTON
- Hippo Team
```
### Targets:
![](https://cdn.securelist.com/files/2015/09/satellite_Internet_en_5.png)
```
Embassies of Eastern Bloc Nations:
- Belgium
- Ukraine
- China
- Jordan
- Greece
- Kazakhstan
- Armenia
- Poland
- Germany
```
### Other Relevant Info:
[Microsoft office Exploit](https://otx.alienvault.com/pulse/5911ff9cdbd6ea04445af363/)

[Carbon: 2nd stage backdoor](https://otx.alienvault.com/pulse/58dd14f8e88c7c13038460ba/)

[Info on Turla's satellite based CnC](https://otx.alienvault.com/pulse/55f08e374637f26df8744429)

[Snake Malware Framework For Mac OS X](https://otx.alienvault.com/pulse/5909fc8d28fba172cbbb89cf/)

## 2. **Fancy Bear**
Updated: 5/18/2017
### Aliases:
```
APT28
Pawn Storm
Sofacy Group
Sednit
STRONTIUM
Tsar Team
Threat Group-4127
Grizzly Steppe
```

### Targets:
```
Military
Political entities
```

### Other Relevant Info:
[Ukraine Artillary Hack](https://www.crowdstrike.com/wp-content/brochures/FancyBearTracksUkrainianArtillery.pdf)

Utilize Spear Phishing, Zero Days, and Malware

**Affiliated with Cozy Bear**

## 3. **OceanLotus Group (APT32)**
Updated: 5/19/2017
### Aliases:
```
```
### Targets:
```
Countries:

  Vietnam
  Germany
  Philippines
  China
  United States

Fields of Interest:

  Government
  Manufacturing
  Media
  Consumer Products
  Banking
  Hospitality
  Network Security
  Tech. Infrastructure
```
### Other Relevant Info:

**Malware Used - WINDSHIELD, KOMPROGO, SOUNDBITE, BEACON**

**Malware Capabilities**

**WINDSHIELD**

- Command and control (C2) communications via TCP raw sockets
- Four configured C2s and six configured ports randomly-chosen C2/port for communications
- Registry manipulation
- Get the current module's file name
- Gather system information including registry values, user name, computer name, and current code page
- File system interaction including directory creation, file deletion, reading, and writing files
- Load additional modules and execute code
- Terminate processes
- Anti-disassembly

**KOMPROGO**

- Fully-featured backdoor capable of process, file, and registry management
- Creating a reverse shell
- File transfers
- Running WMI queries
- Retrieving information about the infected system

**SOUNDBITE**

- C2 communications via DNS
- Process creation
- File upload
- Shell command execution
- File and directory enumeration/manipulation
- Window enumeration
- Registry manipulation
- System information gathering

**PHOREAL**

- C2 communications via ICMP
- Reverse shell creation
- Filesystem manipulation
- Registry manipulation
- Process creation
- File upload

**BEACON (Cobalt Strike)**

- Publicly available payload that can inject and execute arbitrary code into processes
- Impersonating the security context of users
- Importing Kerberos tickets
- Uploading and downloading files
- Executing shell commands
- Configured with malleable C2 profiles to blend in with normal network traffic
- Co-deployment and interoperability with Metasploit framework
- SMB Named Pipe in-memory backdoor payload that enables peer-to-peer C2 and pivoting over SMB

[APT32 a Threat to Global Corporations](https://www.fireeye.com/blog/threat-research/2017/05/cyber-espionage-apt32.html)



# References
*This section contains supporting information to the above list of APTs*

**CrowdStrike Naming Convention**

Made by Dmitri Alperovitch

![CrowdStrike Naming Convention](https://www.crowdstrike.com/blog/wp-content/uploads/2014/09/Picture1.png)

**Nation-State-Based Adversaries**

Panda = China

Bear = Russia

Kitten = Iran

Tiger = India

Chollima (a mythical winged horse) = North Korea


**Non-Nation-State Adversaries**

Jackal = Activist groups

Spider = Criminal groups

(Adjective) (Country)

**APT's**

APT = Advanced Persistent Threat

How APTs work:

1. The cyber criminal, or threat actor, gains entry through an email, network, file, or application vulnerability and inserts malware into an organization's network. The network is considered compromised, but not breached.

2. The advanced malware probes for additional network access and vulnerabilities or communicates with command-and-control (CnC) servers to receive additional instructions and/or malicious code.

3. The malware typically establishes additional points of compromise to ensure that the cyber attack can continue if one point is closed.

4. Once a threat actor determines that they have established reliable network access, they gather target data, such as account names and passwords. Even though passwords are often encrypted, encryption can be cracked. Once that happens, the threat actor can identify and access data.

5. The malware collects data on a staging server, then exfiltrates the data off the network and under the full control of the threat actor. At this point, the network is considered breached.

6. Evidence of the APT attack is removed, but the network remains compromised. The cyber criminal can return at any time to continue the data breach.

[Anatomy of APTs](https://www.fireeye.com/current-threats/anatomy-of-a-cyber-attack.html)
