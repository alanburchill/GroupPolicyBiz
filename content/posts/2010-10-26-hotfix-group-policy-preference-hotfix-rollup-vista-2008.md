---
title: "Hotfix: Group Policy Preference Hotfix Rollup (Vista / 2008)"
date: 2010-10-26 22:59:12
author: admin
categories: ["News"]
tags: ["Client Side Extentions", "Group Policy Preferences", "hotfix", "KB974266", "KB977983", "rollup", "Vista", "Windows Server 2008"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/10/image_thumb20.png"
---

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/10/image_thumb20.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/10/image20.png>)A new Windows Vista / 2008 Group Policy Preference client side extension hotfix rollup has been released. Below I have listed the details of the hotfix including a complete list of all issues it resolved.

[KB977983](<http://support.microsoft.com/kb/977983> "http://support.microsoft.com/kb/977983") \- Group Policy preferences client-side extension hotfix rollup for Windows Vista and Windows Server 2008

**New Issues Resolved**

  * You cannot create a GPP folder when the target path is a Distributed File System (DFS) path.
  * Item-Level Targeting for the security group does not recognize nested groups for computer objects.
  * When you configure Item-Level Targeting for GPP to match a registry value, the match fails.
  * The GPP data source name (DSN) requires a password if a username is specified in the DSN connection information. After you apply this hotfix rollup, you can use a blank password in the DSN connection information.
  * You experience a significant delay when you log on to an Active Directory site that has a read-only domain controller (RODC). This issue occurs when you implement Item-Level Filtering for Lightweight Directory Access Protocol (LDAP) by using GPP.
  * GPP cannot be deployed on a printer when the printer owner is not specified as "System" or "Administrators."
  * When you configure Item-Level Targeting for GPP with Terminal Services, Item-Level Targeting fails.
  * A memory leak occurs in the GPP client every time that Item-Level Targeting is processed.


**Previous[KB974266](<http://support.microsoft.com/kb/974266/>) Issues Resolved**

  * The Windows Event Log service crashes when the regional options preferences are set to English (United Kingdom).
  * If the regional options preference is set to English (United Kingdom) or to anything other than United States, it cannot be applied. The regional options preference setting still shows **United States**.
    * **Note** A non-administrator user cannot log on to a domain from a computer that is running Windows Vista SP2, if the user's locale information is set by using a Group Policy preference and set the regional options preference as English (United Kingdom).
  * If you create or update a virtual private network (VPN) connection by using a Group Policy object, the connection does not bind to IP Version 4 (TCP/IPv4) or IP Version 6 (TCP/IPv6).
  * A Lightweight Directory Access Protocol (LDAP) query that is used by item level targeting uses an incorrect base distinguish name.
  * Group Policy Service (GPSVC) stops responding during the GPSVC shutdown process if third-party printer drivers are installed by Group Policy Preferences.
  * The **%GPTPATH%** variable is not resolved correctly when Group Policy Preferences are processed.
  * Group Policy Preferences stops responding when you try to configure the printer item for printers that use third-party drivers. For more information, click the following article number to view the article in the Microsoft Knowledge Base:

[973772](<http://support.microsoft.com/kb/973772/>) (http://support.microsoft.com/kb/973772/ ) Group Policy Preferences stops responding when you try to configure the printer item for printers that use third-party drivers on a Windows Vista or Windows Server 2008-based computer


Source <http://blogs.technet.com/b/askds/>