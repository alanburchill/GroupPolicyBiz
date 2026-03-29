---
title: "New Windows 7 / Server 2008 R2 Group Policy hotfix round up"
date: 2010-04-22 11:17:09
author: admin
categories: ["News"]
tags: ["hotfix", "KB981054", "KB981177", "KB981265", "KB981750", "Windows 7", "Windows Server 2008 R2"]
---

Last week Microsoft released a few new Group Policy hot fixes for Windows 7 and Windows Server 2008 R2, below is a link to each KB article and my own short description hotfix.

> [KB981054](<http://support.microsoft.com/kb/981054>) The Group Policy preference settings for the "Terminal Session" item-level targeting item are not applied in Windows 7 or in Windows Server 2008 R2."

This is a fix for a really cool feature of Group Policy Preferences which allow IT administrator to target settings based on the IP address of the RDP client. For more info see <http://support.microsoft.com/kb/981054>

> [KB981177](<http://support.microsoft.com/kb/981177>) You can still unpin a program from the taskbar unexpectedly when you enable the "Do not allow pinning programs to the Taskbar" Group Policy on a computer that is running Windows 7 or Windows Server 2008 R2.

This hot fix is just a minor UI bug. For more info see <http://support.microsoft.com/kb/981177>

> [KB981265](<http://support.microsoft.com/kb/981265>) You cannot create a software installation Group Policy setting on a read-only domain controller in Windows Server 2008 R2.

This fixes a problem with GPMC trying to make a policy change against a read-only domain controller when someone tries to create and "assigned" software deployment. For more info see <http://support.microsoft.com/kb/981265>

> [KB981750](<http://support.microsoft.com/kb/981750>) Error message occurs when you use GPMC to view a software restriction Group Policy setting in Windows 7 and in Windows Server 2008 R2: "An error has occurred while collecting data for Software Restriction Policies".

This fixes the following error message when you error message when you access Computer Configuration > Windows Setting > Security Settings > Software Restriction Policies due to a bug in GPMC calling an incorrect function when reading multiple string type registry key. For more info see <http://support.microsoft.com/kb/981750> Hope you find these users but as always make sure you thoroughly test any hotfix before you deploy them into production.