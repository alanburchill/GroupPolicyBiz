---
title: "Group Policy Setting of the Week 5 "“ Add Logoff to the Start Menu"
date: 2009-12-07 13:48:14
author: admin
categories: ["Setting of the Week"]
tags: ["Basic", "Group Policy"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb68.png"
---

This weeks simple Group Policy Setting of the Week (GPSW) is called "Add Logoff to the Start Menu" which can be found under User Configuration > Policies > Administrative Templates > Start Menu and Taskbar. This option adds the "Log Off <username>" to the users start menu and is normally configured to be enabled on Terminal Servers where you don't want them accidently shutdown the server. [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb68.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image70.png>) Now hopefully your normal users don't have admin access to your Terminal Servers however if you are a Server Administrator then you could have admin access and as such having the shutdown button on a desktop that looks a LOT like you local computer could be very dangerous. So this is one of the few group policy settings that should be configured to loopback that should be applied to the server administrator via a Loopback merge setting (we will talk about Loopback setting another day). But how do I shutdown the server then I hear you ask? No prob you can either run the "shutdown.exe" command line (tshutdn.exe on Windows 2003) or by CTRL-ALT-END and then shutdown from the secure desktop.