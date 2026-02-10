---
title: "Remote Server Admin Tools (a.k.a RSAT) for Windows 10 v1803 Redstone 4"
date: 2018-03-27 23:11:55
author: admin
categories: ["News"]
tags: ["1803", "Honolulu", "Redstone 4", "Remote Server Admin Tools", "RSAT"]
---

Microsoft has release a new version of the Windows 10 Remote Server Admin Tools for builds of Windows 10 17110 or higher. While it was normally practice for Microsoft to release a new RSAT version with every release of a Windows client OS in recent years they have been releasing these tools less frequently (see <https://www.grouppolicy.biz/2017/04/microsoft-will-not-be-releasing-remote-server-admin-tools-rsat-for-windows-10-redstone-2/> ) While it does not seem like there is much in this new version I still always recommend that admin run the latest version of RSAT on their computer to ensure the least amount of problem, especially with Group Policy Management Console. What's new:

  * _FIXED: DNS server tools are now correctly installed as part of the RSAT package._
  * _FIXED: Shielding data files and template disks can now be created by their respective wizards in the RSAT package._
  * _KNOWN ISSUE: The x86 RSAT package may fail during installation on Windows 10 builds older than 17110, and on builds other than the 171xx series._

Also note that Microsoft is already moving away from using RSAT tools for management and with a new tool called codename "Honolulu". This tool currently only comes with Windows Server 2016 and is a replacement for Windows Server Manage. Its an extensible PowerShell based single management pane tool that can be used to perform many of the admin tasks across multiple servers. For an overview of the tool check out the video below"...