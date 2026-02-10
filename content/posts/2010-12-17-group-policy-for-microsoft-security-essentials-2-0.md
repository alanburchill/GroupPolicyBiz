---
title: "Group Policy for Microsoft Security Essentials 2.0"
date: 2010-12-17 04:30:00
author: admin
categories: ["Best Practice", "Security", "Tutorials"]
tags: ["Group Policy", "Microsoft Security Essentials", "MSE", "registry"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb48.png"
---

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb48.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image50.png>)Microsoft have now released Microsoft Security Essentials 2.0 to the web which has a number of new features over the previous version.

  * **Windows Firewall integration** "“ During setup, Microsoft Security Essentials will now ask if you would like to turn the Windows Firewall on or off.
  * **Enhanced protection for web-based threats "“** Microsoft Security Essentials now integrates with Internet Explorer to provide protection against web-based threats.
  * **New protection engine "“** The updated anti-malware engine offers enhanced detection and cleanup capabilities with better performance.
  * **Network inspection system* "“** Protection against network-based exploits is now built in to Microsoft Security Essentials.


Therefore I have updated my previous post based [Group Policy for Microsoft Security Essentials](<https://www.grouppolicy.biz/2010/09/group-policy-for-microsoft-security-essentials/>) to support configuring the newly added features.

If you want more general info about MSE v2 see: [Security Garden: Microsoft Security Essentials 2.0 Released](<http://securitygarden.blogspot.com/2010/12/microsoft-security-essentials-20.html> "http://securitygarden.blogspot.com/2010/12/microsoft-security-essentials-20.html")

If you want to download it visit <http://www.microsoft.com/downloads/en/details.aspx?FamilyID=e1605e70-9649-4a87-8532-33d813687a7f>

Before I begin I should remind you that Microsoft only allows MSE to be used for free in small businesses with less that 10 seats (see [here](<http://windowsteamblog.com/windows/b/windowssecurity/archive/2010/09/22/microsoft-security-essentials-now-available-for-small-businesses.aspx>)). But MSE does not natively support Group Policy and having to configured even 10 copies of Microsoft Security Essentials (MSE) manually can be a pain. So the instructions below is simply a way to configure the registry keys of the application using the [Group Policy Preferences Registry](<http://technet.microsoft.com/en-us/library/cc771589.aspx>) key setting.

**Tip:** If the below instructions to create the registry keys seems like to much work you will be glad to know that I have put a link at the bottom to an XML Group Policy Preferences Registry file. You can use this file to import the all the Policy Registry setting I talk about below automatically.

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

#### Limit CPU Usage

**Key:** HKLM\Software\Microsoft\Microsoft Antimalware\Scan
**Value:** AvgCPULoadFactor (REG_DWORD)
**Data (Decimal):** 10 (10%)
**Data (Decimal):** 50 (20%)
**Data (Decimal):** 90 (90%)

Now all your computers will have the scheduled scan option configured as the following image below.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/12/image_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/12/image2.png>)

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

#### Scan all downloaded files and attachments

**Key:** HKLM\Software\Microsoft\Microsoft Antimalware\Real-Time Protection
**Value:** DisableOnAccessProtection (REG_DWORD)
**Data:** **0** (Scan Enabled)
**Data:** 1 (Scan Disabled)

#### Disabled Real Time Monitoring

**Key:** HKLM\Software\Microsoft\Microsoft Antimalware\Real-Time Protection
**Value:** DisableRealtimeMonitoring(REG_DWORD)
**Data:** **0** (Scan Enabled)
**Data:** 1 (Scan Disabled - but why would you want to disable it...?)

#### Disabled Intrusion Prevention System

**Key:** HKLM\Software\Microsoft\Microsoft Antimalware\Real-Time Protection
**Value:** DisableIntrusionPreventionSystem(REG_DWORD)
**Data:** **0** (IPS Enabled)
**Data:** 1 (IPS Disabled)

#### Real Time File Scanning Direction

**Key:** HKLM\Software\Microsoft\Microsoft Antimalware\Real-Time Protection
**Value:** DisableIntrusionPreventionSystem(REG_DWORD)
**Data:** **0** (Both)
**Data:** 1 (Incoming)
**Data:** 2 (Outgoing)

You real time protection should now be configured as shown below.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/12/image_thumb1.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/12/image3.png>)

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

#### Remove Quarantine file after (x days):

**Key:** HKLM\Software\Microsoft\Microsoft Antimalware\Quarantine
**Value:** PurgeItemsAfterDelay (REG_DWORD)
**Data (Decimal):** 30 (30 Days)

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/12/image_thumb2.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/12/image4.png>)

###

### Importing Group Policy Preferences

For your convenience I have provided you a link to a XML Group Policy Preferences Registry file for all the above settings.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/12/image5.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/MSE_Settings_2.xml>)

Or here <https://www.grouppolicy.biz/wp-content/uploads/2010/MSE_Settings_2.xml> if the link on the image above does not work.

Simply save the file to your desktop and then drag it into the empty pane on the right hand side, click "Yes" to confirm the import and you will have all the registry keys automatically created.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb54.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image56.png>)

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/12/image_thumb3.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/12/image6.png>)