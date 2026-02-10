---
title: "Group Policy Setting of the Week 33 "“ Set up a work schedule to limit the maximum network bandwidth used for BITS background transfers"
date: 2010-06-28 08:00:00
author: admin
categories: ["Setting of the Week"]
tags: ["BITS", "Intermediate", "WAN"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/06/image_thumb43.png"
---

This weeks setting of the week is called "Set up a work schedule to limit the maximum network bandwidth used for BITS background transfers"... Phew".... This policy is used to configure the bandwidth allocation of BITS network transfers in your environment. This is obviously very handy setting manage your bandwidth if you are working in a bandwidth constrained environment such as a remote branch office. Some of the more likely application you have installed in your environment that use BITS are [Windows Server Update Services](<http://blogs.technet.com/b/wsus>) or [Branch Cache](<http://www.microsoft.com/windows/enterprise/products/windows-7/features.aspx#branchcache>) however third-party application can also use the BITS to transfer information.

This setting is used to control 3 of the 4 levels (see below) of BITS transfer priority that can be used by applications.

  * FOREGROUND
  * HIGH
  * NORMAL
  * LOW


The foreground transfer is always meant to be performed in real time so there is no option to control what amount of bandwidth this transfer method uses. For more info on BITS transfer priority see <http://msdn.microsoft.com/en-us/library/aa362805(VS.85).aspx>.

This setting can be found under Computer Configuration > Administrative Templates > Network > Background Intelligent Transfer Services (BITS) and will only apply to Windows 7 or computers with BITS 3.5 installed.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/06/image_thumb43.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/06/image37.png>)

If you are considering this setting then also look at the other setting called "Set up a maintenance schedule to limit the maximum network bandwidth used for BITS background transfers" which will take precedence over the work schedule rule. You may want to use this maintenance schedule to allow the use of more bandwidth after hours when the network is not as busy.