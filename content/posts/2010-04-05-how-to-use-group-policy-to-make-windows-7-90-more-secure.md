---
title: "How to use Group Policy to make Windows 7 90% more secure"
date: 2010-04-05 12:12:56
author: admin
categories: ["News", "Security"]
tags: ["News", "Security", "Windows 7"]
---

[BeyondTrust](<http://www.beyondtrust.com/>) has just come out with a white paper entitled "90% of Critical Microsoft Windows 7 Vulnerabilities are Mitigated by Eliminating Admin Rights". This paper has some very interesting statistics around the percentages of security issues that are mitigate if a users is not running as administrator.

> "¢ 90% of Critical Windows 7 vulnerabilities reported to date

> "¢ 100% of Microsoft Office vulnerabilities reported in 2009

> "¢ 94% of Internet Explorer and 100% of IE 8 vulnerabilities reported in 2009

> "¢ 64% of all Microsoft vulnerabilities reported in 2009

Obviously Microsoft has pushed very hard to not have users run with administrator access with the introduction of User Account Control (UAC) in Windows Vista. This forced any users even if they were administrator to run in normal privilege mode unless required and only then grant them administrator access via a prompt.

So if your environment is ready for you users to have admin access removed and you want an easily way to lock down the local administrator groups on all your computers you can achieve this using Group Polices in one of two ways.

### Method 1. Restricted Groups

The first and most common method is called "restricted groups" which can be found under Computer Configuration > Policies > Windows Settings > Security Settings > Restricted Groups. This policy has a mode called "Members" can be used to tightly control who is a member of any local group on a computer (e.g. "administrators" and "power users") however this is also not very granular. The "Member of" option of the "restricted groups" will add an additional member to the local group but it will not remove any un-authorised members. So while both modes are very powerful they certainly have their limitations. One advantage of this option however is that it is a native setting and therefore will work out of the box with Windows 2000, XP and Vista.

### Method 2. Group Policy Preferences

You can use Group Policy Preferences to secure local administrator groups in a ways that still removes any au-authorised users but still have the flexibility to granularly grant permission for a single user to a single local group on a particular computer. While this does not get around the problem of having to grant a users administrator access to their own workstation it does prevent them from being administrator of other workstation on the LAN. This greatly mitigates the possibility of one users infecting the entire network quickly as they will NOT have admin access to all the other computers around them. For more instructions on how to use Group Policy Preference to secure the local admin group you can read my previous blog here <https://www.grouppolicy.biz/2010/01/how-to-use-group-policy-preferences-to-secure-local-administrator-groups/>

Of course removing administrator access is certainly a big step in one direction but whenever considering security make sure you take a "[Defence In-depth](<http://en.wikipedia.org/wiki/Defense_in_Depth_%28computing%29>)" approach. To do this you should start by making sure you also regularly install security updates; have current Anti-Virus software installed and consider enabling host based firewalls even when connected to the corporate LAN.

You can download the BeyondTrust whitepaper from <http://www.beyondtrust.com/downloads/whitepapers/Microsoft_Vulnerability_Analysis_2009.asp>