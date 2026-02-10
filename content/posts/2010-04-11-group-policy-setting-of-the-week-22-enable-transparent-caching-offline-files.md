---
title: "Group Policy Setting of the Week 22 "“ Enable Transparent Caching (Offline Files)"
date: 2010-04-11 21:00:00
author: admin
categories: ["Setting of the Week"]
tags: ["Intermediate", "Offline Files", "Windows 7"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/04/image_thumb2.png"
---

This week is another setting that controls a new offline files settings that was introduced in Windows 7 and this setting seems to be nothing short of AMAZING!!!

This setting is used to "Enabled Transparent Caching" and can be found under Computer Configuration > Policies > Administrative Templates > Networks > Offline Files. Unfortunately I have not had a chance to try this option for my self but reading the description it seems to be nothing short of hidden killer feature for Windows 7. The transparent cache feature kicks in on any offline files whenever latency to the file server goes above a certain limit. Now everyone's environment is going to be different based on file server performance and network latency so be sure you do some testing first to get the right balance. When this setting is combined with last weeks "Configure Background Sync" option then you could drastically reduce latency to the file server and decrease bandwidth consumption. This options sound ideal for Direct Access and VPN users as their latency to the file server could vary drastically depending on the networking conditions or it could be configured to mask any performance issues that are noticed when a file server is being backed up.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/04/image_thumb2.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/04/image2.png>)

If you are working in an environment that has Windows 7 deployed then this is definitely one setting you need to look at enabling. That being said deploy a Brach Cache to a remote site would still deliver more benefits as files that are cached as one computers cache can be users for other computers on the same LAN segment. This is as opposed to this option which only gives a bandwidth saving benefit for any files that have already been made available offline on that particular computer.