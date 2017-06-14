*This document will contain information about various types of malware*
**THIS DOC IS A WIP**

# **MALWARE**

## **Fake Firefox Updates**

*firefox-patch.js*
### Notes:

- Firefox has an automated background update mechanism which will never prompt you to manually download and execute a file

*Example of Fake Update Screen*

![Example of Fake Update](https://support.cdn.mozilla.net/media/uploads/gallery/images/2016-09-15-12-37-10-c81e72.png)

#### Sources:
[Mozilla Info Page](https://support.mozilla.org/en-US/kb/i-found-fake-firefox-update)

## **Gamarue/Andromeda**

### Notes:

**Symptoms**
* Registry:
  In subkey: HKCU\Software\Microsoft\Windows NT\CurrentVersion\Windows\
  Value: "load"
  Data: "<malware file name>"

* Infections from USB and phishing emails

**Type** : *Worm*

**Behavior**

* uses a .lnk to drop and run malicious .dll files from a temp folder, which drops a malicious .exe.  Persistence is then created
* .dlls in a CLSID format
* Communicates out to some malicious domains

**Other**

* 70-100mb size
* Contains a lot of junk code, random strings, obfuscated code, RETN being used as calls, JMPs to code sections in memory

#### Sources:
[Malware Breakdown](http://malwarenailed.blogspot.de/2017/01/gamarueandromeda-comeback.html)
[Gamarue/Andromeda Comeback](https://otx.alienvault.com/pulse/5900b4dba0117e3404052fe7/)


## **H-Worm (Houdini Worm)**

*also known as Jenxcus*

### Notes:

**Payload**
* VBS script based RAT
* Wrapped in PE executable dropper
* obfuscated with base 64 encryption

**Command and Control Behavior**
* installs and starts communication with C2
* Content sent :
```
User-Agent: {DiskVolumeSerial}<|>{Hostname}<|>{Username}<|>{OS}<|>plus<|>{AVProductInstalled or nan-av}<|>{USBSpread: true or false} - {CurrentSystemDate}
```
* Command format:  {command}<|>{param1}<|>{param2}

**Inner Workings**
* Control panel written in Delphi
* Control panel used to interact with infected machines
* Similar to NjWorm, njRAT, XtremeRAT & PoisonIvy

**Other Notes**
* njq8 might have helped develop H-Worm
#### Sources:
[Fireye H-Worm Report](https://www.fireeye.com/blog/threat-research/2013/09/now-you-see-me-h-worm-by-houdini.html)

[In Depth Breakdown](http://malwarenailed.blogspot.de/search?updated-max=2017-05-13T02:56:00%2B04:00&max-results=7)

[Autoit Sample](http://tinyurl.com/lw3dcjr)


## **Dumping Windows Credentials**

### Notes:

Core principles behind credential dumping:
* Safety
* Stealth
* Efficiency

**System Level** Privilege needed.  Credential gathering is the next move so a hacker can move through the network with greater access.

* If the host is part of an Active Directory domain hacker will be looking for **privileged domain accounts**. Preferably a member of the **Domain Admins** group.

#### **Credential Dumping Techniques**:

### **Registry Hives**

- Get a copy of SYSTEM, SECURITY, and SAM Hives
- Ex. C:\temp\sam.save or security.save or system.save

### **Password Hashes**

- Get password hashes, cached domain creds, and LSA secrets.
- Tool used is **secretsdump**

```
Ex. $ secretsdump.py -sam sam.save -security security.save -system system.save LOCAL
```

### **Local SAM Hashes**

- Crack **LM** hashes with Ophcrack
- Crack **NT** hashes with hashcat or JtR
- Pass the Hash against accounts with same password hash

### **Cached Domain Credentials**

- Passwords of domain users that have been logged on to the host previously.
- Also crack these using **JtR or hashcat**.  Format is mscash (xp, w2k3) or mscash2 (vista, w7, w2k8)
- You **cant** preform pass the hash attack with this type of hash

### **LSA Secrets**

- Passwords for services that are set to run under **actual Windows user accounts** (as opposed to Local System, Network Service, and Local service accounts)
- If host is part of a domain you will find **domain credentials of machine account**
- Authenticate to domain in order to list all domain users and Admins
- Use **pth** on Kali or **wce** on windows to use these credentials
```
Ex. $ pth-net rpc user -U 'securus\john-pc$%aad3b435b51404eeaad3b435b51404ee:2fb3672702973ac1b9ade0acbdab432f' -S dc1.securus.corp.com

```
- Browse shares for Passwords
- Look on **domain controller** for Passwords in Group Policy Preferences

### **In-Memory Credentials**

- Dump **clear-text** passwords from memory using **mimikatz**
- **Windows Task Manager** to dump LSASS properties
  - Right click lsass.exe and select create dump file
- If **wce** is pushed to a host the hacker is probably trying to dump passwords

[PowerShell-Fu Method](https://github.com/mattifestation/PowerSploit/blob/master/Exfiltration/Out-Minidump.ps1)

- Dump collected credentials offline via **mimikatz** minidump module

```
mimikatz.exe log "sekurlsa::minidump lsass.dmp" sekurlsa::logonPasswords exit
```

**Mimikatz must be run on the same architecture you pulled the dump from!!!**

![](http://blog.gentilkiwi.com/wp-content/uploads/2013/04/minidump_matrix.png)

### **Credential Manager**

- When you click "Remember my password" the password get stored in **Windows Data Protection API**

- All saved credentials can be seen in **credential manager** (access via control panel)
- Recover Stored Passwords with **Network Password Recovery**

[Network Password Recovery](http://www.nirsoft.net/utils/network_password_recovery.html)

### **Protected Storage**

- Dump passwords from IE, Outlook, etc. using:
[Protected Storage PassView](http://www.nirsoft.net/utils/pspv.html)
### Third Party Software
[Nirsoft](http://nirsoft.net/utils/index.html#password_utils)
- Tools to recover passwords from third party applications.

### MORE COMING SOON!

# Using Mimikatz to Dump Creds

#### Sources
[Securusglobal](https://www.securusglobal.com/community/2013/12/20/dumping-windows-credentials/)
# Other Research

## Commonly Used Malicious File Extensions

**MOST COMMON**
* .exe - program file
* .com - MS-DOS program
* .pif - shorcut to MS-DOS program
* .bat - batch file
* .scr - screen saver file

*Sometimes viruses attempt to use two file extensions to spoof looking legit.  EX. badfile.jpg.exe*

**ALL EXTENSIONS**
* .jpg, .png, .MP3, .gif and other media files do not contain code and are less suspect.
* .GADGET - file introduced in vista for desktop gadgets
* .MSI - Microsoft Installer File used to install apps, just like .exe's
* .MSP - Windows installer for patches on apps installed by .MSI
* .COM - Used by MS-DOS
* .SCR - Windows screen saver file that may contain executable code
* .HTA - HTML app
* .CPL - Control panel file
* .MSC - Microsoft management console file ex. Disk management tool
* .JAR - java executable
* .BAT - batch file that executes list of commands when run
* .CMD - similar to batch file introduced in windows NT
* .VB .VBS - VBScript file
* .VBE - encrypted VBScript
* .JS - Javascript file
* .JSE - encrypted .js
* .WS .WSF - Windows script file
* .PS1, .PS1XML, .PS2, .PS2XML, .PSC1, .PSC2 - A windows PowerShell script used to run PowerShell commands
* .MSH, .MSH1, .MSH2, .MSHXML, .MSH2XML - Monad script file (Old PowerShell)
* .SCF - Windows explorer command file, can be used to insert malicious commands to explorer
* .LNK - A link to a program on the PC, maybe used to delete files without permission
* .INF - Text file used by AutoRun.  Can launch evil apps
* .DOC, .XLS, .PPT - commonly used to target businesses if malicious
* .DOCM, .DOTM, .XLSM, .XLTM, .XLAM, .PPTM, .POTM, .PPAM, .PPSM, .SLDM - M stands for macros.  Introduced in Office 2007
* .CHM - HTML file compiled by Microsoft
* .DRV - Windows device driver
* .VXD - Windows virtual device driver
* .DLL - Dynamic link library file
* .SWF - Shockwave flash

**SOURCE** [Extensions](https://cfoc.org/windows-file-extension-list-types-of-files-exploited-by-malware/)
