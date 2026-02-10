---
title: "Security Baseline template for Windows 1903"
date: 2019-05-27 00:40:18
author: admin
categories: ["News", "Security"]
tags: ["1903", "Maximum Password Age", "Password", "Policy", "Security Template", "Windows 10", "Windows Server"]
featured_image: "/uploads/2017/03/Icons31.png"
---

Microsoft has released the latest security template for Windows version (Windows 10 and Windows Server) 1903. These templates contain updated guidance and recommendations as to what setting should or should not be configured to your domain joined PC. The security template is actually just a bunch of reports, documents, GPO backups and tools that are consolidated in a s single ZIP file. They are released with every new version of the OS, which ensure that they are also kept up to date with the latest guidance. If you are using Azure AD joined computer the templates are also published via the MDM admin portal.

One of the most notable changes this time is that Microsoft has now dropped the Maximum Password age all together. This means that by default passwords should never naturally expire. 10 years ago suggesting such a change would seem unthinkable but in the past few years many security experts such as Troy Hun have started to recommend this new approach ( <https://www.troyhunt.com/passwords-evolved-authentication-guidance-for-the-modern-era/> ). Even the UK government has changed their recommendation to also not have users password expire ( <https://www.ncsc.gov.uk/collection/passwords> ) . If you are wondering, the logic behind this change is that users that are force to change passwords regularly are by human nature pick something that only change slightly e or simple store the password in secure like a piece of paper. This of course does not mean users will never have to change passwords, and it is important that you have tools in place for suspicious activity with accounts. So when bad activities are detected like a brute force attempt or when passwords match those on know compromised password lists then users should be prompted to change their password.

There are also a number of other minor changes, these changes are summaries conveniently in a spreadsheet contained in the zip file.

Even if you are not yet looking at rolling out Windows 1903 the new guidance and setting can still apply to your older computers and domain policy security settings. So this is a must have download of all security administrators in your organisation.

Download it via <https://www.microsoft.com/en-us/download/confirmation.aspx?id=55319>