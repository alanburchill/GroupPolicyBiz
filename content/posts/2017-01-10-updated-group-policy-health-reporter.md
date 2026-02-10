---
title: "Updated Group Policy Health Reporter"
date: 2017-01-10 22:53:01
author: admin
categories: ["News"]
tags: ["Feedly", "Group Policy", "IFTTT"]
---

The post [Updated Group Policy Health Reporter](<http://ift.tt/2jrMAuW>) appeared first on [SDM Software | Configuration Experts](<https://sdmsoftware.com>). Happy New Year Everyone! I hope everyone made it safely through the holidays. To start off 2017, we've been working to update some of our existing freeware tools. The first beneficiary of that work is our [Group Policy Health Reporter](<http://ift.tt/2j56qiS>) utility, now at version 1.9 (see screenshot):

![Group Policy Health Reporter 1.9](http://ift.tt/2j57hjz)

Group Policy Health Reporter 1.9

This new version fixes issues we had reporting against Windows 10 and Server 2016, upgrades the utility to 64-bit, upgrades the required .Net Framework version to 4.0 and cleans up a weird issue that seems to have been introduced at some point in Windows 7 and 2008-R2. Namely, one of the pieces of information we return is the list of GPOs that have been processed by a computer or user, and those corresponding Group Policy Container (GPC) and Group Policy Template (GPT) versions. The idea here is that, in the days of NTFRS SYSVOL replication, you often got into scenarios where the AD part of the GPO replicated to DCs at a different rate (or sometimes not at all!) than the SYSVOL part"“resulting in GPOs being incorrectly processed by some clients. Health Reporter has always called out this difference as a potential problem, by mining information in the client's registry under HKLM\Software\Microsoft\Windows\CurrentVersion\Group Policy. However, at some point Windows 7 and 2008-R2 stopped properly updating the GPT version in that registry metadata"“always reporting it as 'FFFF', which means that the GPT version couldn't be resolved. This led to false positives in GP Health Reporter that were annoying at best. So we've essentially now cleaned that up so that these errors don't get flagged for Windows 7 and 2008-R2 target systems. Not a perfect solution, since you could still have SYSVOL replication issues that could be completely legitimate, but for now, at least a partial solution. And of course, if you need a more full-featured, enterprise-strength GP reporting solution that remotely grabs GP health and even SETTINGs from your Windows systems, our commercial [Group Policy Compliance Manager](<http://ift.tt/2j50sib>) is your solution! Enjoy! Darren Mar-Elia The post [Updated Group Policy Health Reporter](<http://ift.tt/2jrMAuW>) appeared first on [SDM Software | Configuration Experts](<https://sdmsoftware.com>). from SDM Software | Group Policy Management & Administration Tools http://ift.tt/2jrMAuW via [IFTTT](<http://ift.tt/1c4nCfM>)