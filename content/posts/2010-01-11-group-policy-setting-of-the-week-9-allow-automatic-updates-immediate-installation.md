---
title: "Group Policy Setting of the Week 9 "“ Allow Automatic Updates immediate installation"
date: 2010-01-11 04:20:02
author: admin
categories: ["Setting of the Week"]
tags: ["Basic", "patches", "wsus"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb71.png"
---

First of all thank you for coming to my new web site [www.grouppolicy.biz](<https://www.grouppolicy.biz>) this site is still rather new and if you have any issues and/or suggesting please feel free to post a comment. This weeks GPSW covers another product that I use a lot and love to talk about, [Windows Server Update Services ](<http://technet.microsoft.com/en-au/wsus/default.aspx>)(a.k.a. WSUS). The "Allow Automatic Updates immediate installation" is very handy for deploying non-windows (but still Microsoft) patches from WSUS. While the idea of installing patches in the background of users sound a little scary for an IT administrator there are a couple of benefit in turning this option on. Applying these patches sooner speeds up the deployment of patches and it shortens the length of time needed to install/reboot time of the other patches that do require a reboot of the operating system. [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb71.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image73.png>) Often these types of "no reboot required" patches are for applications (e.g. Office) rather than the OS as these more often require a reboot for them to be applied. One of the few disappointments of Windows 7 was the lack of hot patching that has long been talked about but hey"... we can wait and see what Windows 8 brings. Alan Burchill