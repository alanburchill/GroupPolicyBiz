---
title: "Group Policy Setting of the Week 22 "“ Configure Background Sync (offline files)"
date: 2010-04-05 11:04:44
author: admin
categories: ["Setting of the Week"]
tags: ["Basic", "Offline Files", "Windows 7"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/04/image_thumb1.png"
---

This weeks setting of the week is second is another one of the new Windows 7 offline file settings called "Configure Background Sync" which can be found under Computer Configuration > Policies > Administrative Templates > Networks > Offline Files. This setting allows you to configured the new Windows 7 feature that background sync's offline file when a computer is in "Slow Link" mode.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/04/image_thumb1.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/04/image1.png>)

Configured this setting would be very useful if you have a large number of computers at a single site that sync their files over a WAN link. In this case the background sync of a large number of users could cause a large amount of traffic. You could then use this setting to back off the sync interval. You may also want to do the opposite and crank up the sync interval to ensure that users files are being saved to the server as soon as possible.

The other scenario where this could be used if for users that are running Direct Access mode or a VPN and you just want to control the amount of traffic they push via their connection.

There is also and option called "Enabled Background Sync for shares in users selected "Work Offline" mode" which forces offline files to sync even when the users has manually chosen offline mode. I would be careful of this setting however as this behaviour might confuse as they might create the document thinking that it was not going to be saved to the server straight away for other people to view.