---
title: "Hotfix: A mapped drive that has the non-persistent flag set is displayed as a disconnected drive"
date: 2011-08-11 05:56:45
author: admin
categories: ["News"]
tags: ["drive", "hotfix", "mapping", "non-persistent", "reconnect"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2011/08/hotfix_icon_thumb.png"
---

[![hotfix_icon](https://www.grouppolicy.biz/wp-content/uploads/2011/08/hotfix_icon_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/08/hotfix_icon.png>)I have seen this issue be raised [many](<http://social.technet.microsoft.com/Forums/en-US/winserverGP/thread/5c2e7bd6-2b7c-4cbb-8592-40dcb34834b4>) [many](<http://social.technet.microsoft.com/Forums/en-US/winserverGP/thread/53405b24-8273-43ff-8aa6-27c8fdd953a2>) [many](<http://social.technet.microsoft.com/Forums/en-US/winserverGP/thread/1294080e-ceb3-478b-8c1f-bc8fc8e10356>) [many](<http://social.technet.microsoft.com/Forums/en-US/winserverGP/thread/b41e9e70-9dc2-4f67-9139-1cd36c1470e5>) [many](<http://social.technet.microsoft.com/Forums/en-US/winserverGP/thread/44a8bec5-1160-400f-b336-0b4b269a390c>) [many](<http://social.technet.microsoft.com/Forums/en-US/winserverGP/thread/1aa489d5-4ab0-406f-ae34-e00912c116f1>) times on the Group Policy forums so I thought I would quick do a blog post about this new fix from Microsoft to make the "reconnect" flag work properly for drive mappings. The hotfix [KB2551503](<http://support.microsoft.com/kb/2551503/>) fixes "A mapped drive that has the non-persistent flag set is displayed as a disconnected drive in Windows 7 or in Windows Server 2008 R2".

Description:

> Assume that you use Group Policy Preferences (GPP) to manage the mapping of drives in a network environment. Additionally, you set the non-persistent flag when you map a drive on a client computer that is running Windows 7 or Windows Server 2008 R2. However, when the client computer is not connected to the network, the mapped drive is displayed unexpectedly as a disconnected drive in Windows Explorer.

So what are you waiting for [View and request hotfix downloads](<http://support.microsoft.com/hotfix/KBHotfix.aspx?kbnum=2551503&kbln=en-us>) NOW!