---
title: "More Group Policy hot fixes"
date: 2010-04-24 01:47:52
author: admin
categories: ["News"]
tags: ["hotfix", "KB979621", "KB979731", "KB980628", "KB981877", "Windows 7", "Windows Server 2008 R2"]
---

Just found out about a few more hot fixes that Microsoft recently released for Group Policy.

> [KB979621](<http://support.microsoft.com/?kbid=979621>) A removable storage device is disabled when you enable a Group Policy to deny write access or to deny read access to the device on a computer that is running Windows Vista or Windows Server 2008

Fixes an issues with removable storage devices being totally disabled when you configure the "Deny write" option for removable devices. This will happen when configure the option and shutdown the computer. You will also get the following error message "The device is disabled. (Code 22)" when you go to the properties of the device. This applies to the following types of devices:

  * CD and DVD
  * Floppy Drives
  * Removable Disks
  * Tape Drives
  * WPD Devices

For more info see <http://support.microsoft.com/?kbid=979621>

> [KB980628](<http://support.microsoft.com/?kbid=980628>) The "Load a specific theme" Group Policy setting is not applied correctly on a computer that is running Windows 7 or Windows Server 2008 R2

Fixes a problem with specifying a them to load when you also enable the **Prevent changing desktop background** option. For more info see <http://support.microsoft.com/?kbid=980628>

> [KB979731](<http://support.microsoft.com/?kbid=979731>) Some Group Policy preferences are not applied successfully on computers that are running Windows 7 or Windows Server 2008 R2

For more info see <http://support.microsoft.com/?kbid=980628>

> [KB981877](<http://support.microsoft.com/kb/981877> "http://support.microsoft.com/kb/981877") You cannot open an HTML GPO report that is created by the German version of Windows Server 2008 R2 or of Windows 7

This hot fixe resolves a problem creating a HTML report with a German version of GPMC. For more info see <http://support.microsoft.com/kb/981877> Thanks to Aaron Parker for the [heads up](<http://twitter.com/stealthpuppy/status/12695391591>) on the KB981877