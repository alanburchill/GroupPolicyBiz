---
title: "Microsoft release two new Group Policy hot fixes"
date: 2010-01-11 22:03:20
author: admin
categories: ["News"]
tags: ["GPMC", "Group Policy Preferences", "hot fix", "KB971357", "KB977983"]
---

Microsoft just released two new hot fixes for the Group Policy Preferences (GPP) client-side extensions and the Group Policy Management Console (GPMC). **Group Policy preferences client-side extension hotfix rollup for Windows Vista** This hotfix resolves numerous issues with the client-side extensions for Vista and required Service Pack 1 or 2 to be installed. Download from <http://support.microsoft.com/?kbid=977983>

  * You cannot create a GPP folder when the target path is a Distributed File System (DFS) path.
  * Item-Level Targeting for the security group does not recognize nested groups for computer objects.
  * When you configure Item-Level Targeting for GPP to match a registry value, the match fails.
  * The GPP data source name (DSN) requires a password if a username is specified in the DSN connection information. After you apply this hotfix rollup, you can use a blank password in the DSN connection information.
  * You experience a significant delay when you log on to an Active Directory site that has a read-only domain controller (RODC). This issue occurs when you implement Item-Level Filtering for Lightweight Directory Access Protocol (LDAP) by using GPP.
  * GPP cannot be deployed on a printer when the printer owner is not specified as "System" or "Administrators."
  * When you configure Item-Level Targeting for GPP with Terminal Services, Item-Level Targeting fails.
  * A memory leak occurs in the GPP client every time that Item-Level Targeting is processed.

**User password is set to NULL when you use Group Policy Preferences to create a user account** This hotfix resolves an issues with creating user accounts with the User and Groups option in preferences. This is an issues with the Group Policy Management Console therefore you need to apply it to all you computers that have it installed. Keep in mind that this will include any computer that has the Remote Server Admin tools installed on any server (including domain controller) that has the Group Policy Management console installed. Microsoft have classified this as a security issues as it allows a password to be set that does not comply with a strong password policy. This hotfix affect Windows Vista and Windows Server 2008 and required Service Pack 1 or 2 for Vista or Service Pack 2 for Windows Server 2008 to be installed. Download from <http://support.microsoft.com/?kbid=971357>

  * The user account password is set to NULL when you update some of its properties and then press the **Apply** button.
  * The user account password is set to NULL when you set the length of the user account password to a range of 16-23 characters.
  * The whole setting file (groups.xml) file is deleted when you create a user account and then press the **Apply** button. Therefore, all user settings are lost.

As always be sure to thoroughly test these patches before when you deploy them.