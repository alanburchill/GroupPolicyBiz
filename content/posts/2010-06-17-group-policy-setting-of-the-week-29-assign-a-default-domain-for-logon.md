---
title: "Group Policy Setting of the Week 29 &ndash; Assign a default domain for logon"
date: 2010-06-17 00:13:56
author: admin
categories: ["Setting of the Week"]
tags: ["Default Domain", "Group Policy"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/06/image_thumb32.png"
---

This weeks setting is a native policy for Windows Vista (or greater) called "Assign a default domain for logon". As the name suggest it configured the default domain name when a user logs on to the computer. This is very handy in a multi domain environment or if you want to make sure that your newly built computer default to the correct domain when the users logon for the first time. This setting can be found under Computer Configuration > Administrative Templates > System > Logon and it requires requires at least Windows Vista. [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/06/image_thumb32.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/06/image28.png>) [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/06/image_thumb35.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/06/image29.png>)

### How to set Default Logon Domain Name for Windows XP via Group Policy

Its nice that this is now a native policy as you use to have to set the registry manually for you to set this option in Windows XP but I often find that this method is very often hit an miss. If you do want to try configuring this for Windows XP you could set it via Group Policy Preferences then here are the key you would set **Key:** HKLM\software\microsoft\windows nt\currentversion\winlogon\ **Value:** altdefaultdomainname (REG_SZ) **Data:** _DOMAINNAME_ and **Key:** HKLM\software\microsoft\windows nt\currentversion\winlogon\ **Value:** defaultdomainname (REG_SZ) **Data:** _DOMAINNAME_