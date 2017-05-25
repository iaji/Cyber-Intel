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
