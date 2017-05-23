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
