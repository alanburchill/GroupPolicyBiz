---
title: "Group Policy for Microsoft Security Essentials"
date: 2010-09-27 15:00:00
author: admin
categories: ["Best Practice", "Security", "Tutorials"]
tags: ["Group Policy", "Group Policy Prefereces", "Intermediate", "Microsoft Security Essentials"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb48.png"
---

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb48.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image50.png>)Microsoft have just [announced](<http://windowsteamblog.com/windows/b/windowssecurity/archive/2010/09/22/microsoft-security-essentials-now-available-for-small-businesses.aspx>) they will allow small business with less that 10 seats to use [Microsoft Security Essentials](<http://www.microsoft.com/security_essentials/>) for free. But even having to configured 10 copies of Microsoft Security Essentials (MSE) can be a pain so below is a quick tutorial on how you can Group Policy Enable Microsoft Security Essentials.

**Update:** Microsoft have now updated their [Microsoft Security Essentials](<http://www.microsoft.com/security_essentials/>) web site to say small business can now "officially" use MSE.

[![Microsoft Security Essentials Download](https://www.grouppolicy.biz/wp-content/uploads/2010/10/image_thumb5.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/10/image5.png>)

Before we begin I want to be clear that MSE does NOT natively support group policy this is simply a way to configure the registry keys of the application using the [Group Policy Preferences Registry](<http://technet.microsoft.com/en-us/library/cc771589.aspx>) key setting.

**Note:** If the below instructions to create the registry keys seems like to much work you will be glad to know that I have put a link at the bottom to an XML Group Policy Preferences Registry file. You can use this file to import the all the Policy Registry setting I talk about below automatically.

### How to use [Group Policy Preferences](<https://www.grouppolicy.biz/2010/03/what-are-group-policy-preferences/>) Registry key setting.

Before we begin we first need to know how to create a Group Policy Preferences Registry Key setting that we will use to control each of the registry keys we need to configured MSE. The following steps will need to be repeated for each registry key below.

**Step 1.** Edit a Group Policy Object that is applied to the computers you want this setting applied.

**Step 2.** Navigate to Computer Configuration > Preferences > Windows Settings > Registry

[![Group Policy Management Editor](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb49.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image51.png>)

**Step 3.** In the Menu click on Action > New > Registry Item

[![New Registry Properties](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb50.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image52.png>)

Now you know how to configure a registry key setting using Group Policy Preferences you can create a new Registry Item for each registry key listed below.

**Note:** The Data values below that are highlighted in BOLD are the values you need to use to replication the examples shown.

### How to configured Scheduled Scan using Group Policy for Microsoft Security Essentials

Now you need to create a registry few specific registry keys. In this example we are going to configured a Full Scheduled scan to run each day at 8am. We are also going to enable the option to check for an update before scanning and we are going to configure the scan to

#### Scheduled Day

**Key:** HKLM\Software\Microsoft\Microsoft Antimalware\Scan
**Value:** ScheduleDay (REG_DWORD)
**Data:** **0** (Every Day)
**Data:** 1 (Sunday)
**Data:** 2 (Monday)
**Data:** 3 (Tuesday)
**Data:** 4 (Wednesday)
**Data:** 5 (Thursday)
**Data:** 6 (Friday)
**Data:** 7 (Saturday)

#### Scheduled Time

**Key:** HKLM\Software\Microsoft\Microsoft Antimalware\Scan
**Value:** ScheduleTime (REG_DWORD)
**Data:** 0 (12am)
**Data:** **000001e0** (8am)

The data of this value represents the number of minutes from 12am in hex"... therefore if you want 8am configured the data to "000001e0"

#### Full or Quick Scan

**Key:** HKLM\Software\Microsoft\Microsoft Antimalware\Scan
**Value:** ScanParameters (REG_DWORD)
**Data:** 1 (Quick Scan)
**Data:** **2** (Full Scan)

#### Check for Update before scanning

**Key:** HKLM\Software\Microsoft\Microsoft Antimalware\Scan
**Value:** CheckForSignaturesBeforeRunningScan (REG_DWORD)
**Data:** 0 (Disabled)
**Data:** **1** (Enabled)

#### Scan only when idle

**Key:** HKLM\Software\Microsoft\Microsoft Antimalware\Scan
**Value:** ScanOnlyIfIdle (REG_DWORD)
**Data:** 0 (Scan when idle)
**Data:** **1**(Scan when active)

Now all your computers will have the scheduled scan option configured as the following image below.

[![Microsoft Security Essentials Settings](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb51.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image53.png>)

### How to configure Real-Time Protection options using Group Policy for Microsoft Security Essentials

Below are the registry keys for configuring the "Rea-Time Scanning" settings for Microsoft Security Essentials.

#### Monitor file and program activity

**Key:** HKLM\Software\Microsoft\Microsoft Antimalware\Real-Time Protection
**Value:** DisableIOAVProtection (REG_DWORD)
**Data:** **0** (Real-Time scan Enabled)
**Data:** 1 (Real-Time scan Disabled)

#### Scan all downloaded files and attachments

**Key:** HKLM\Software\Microsoft\Microsoft Antimalware\Real-Time Protection
**Value:** DisableOnAccessProtection (REG_DWORD)
**Data:** **0** (Scan Enabled)
**Data:** 1 (Scan Disabled)

You real time protection should now be configured as shown below.

[![Microsoft Security Essenitals Settings Real-time protection](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb52.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image54.png>)

### How to configure Advanced Real-Time Protection options using Group Policy for Microsoft Security Essentials

Below are the registry keys for configuring the "Advanced" settings for Microsoft Security Essentials.

#### Scan archive files

**Key:** HKLM\Software\Microsoft\Microsoft Antimalware\Scan
**Value:** DisableArchiveScanning (REG_DWORD)
**Data:** **0** (Enable Archive Scanning)
**Data:** 1 (Disable Archive Scanning)

#### Scan Removable Drives

**Key:** HKLM\Software\Microsoft\Microsoft Antimalware\Scan
**Value:** DisableRemovableDriveScanning (REG_DWORD)
**Data:** **0** (Scan Enabled)
**Data:** 1 (Scan Disabled)

#### Create a system restore point

**Key:** HKLM\Software\Microsoft\Microsoft Antimalware\Scan
**Value:** DisableRestorePoint (REG_DWORD)
**Data:** **0** (Create Restore Point)
**Data:** 1 (Do not create Restore Point)

[![Microsoft Security Essenitals Settings Advanced](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb53.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image55.png>)

###

### Importing Group Policy Preferences

For your convenience I have provided you a link to a XML Group Policy Preferences Registry file for all the above settings.

[![image\[41\]](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image411.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/MSE_Settings.xml> "Microsoft Security Essentials XML Group Policy Preferences Settings")

Simply save the file to your desktop and then drag it into the empty pane on the right hand side, click "Yes" to confirm the import and you will have all the registry keys automatically created.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb54.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image56.png>)

[![Group Policy Management Editor](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb55.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image57.png>)