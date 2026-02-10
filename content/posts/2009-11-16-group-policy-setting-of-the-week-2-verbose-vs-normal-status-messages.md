---
title: "Group Policy Setting of the Week 2 "“ Verbose vs normal status messages"
date: 2009-11-16 13:41:47
author: admin
categories: ["Setting of the Week"]
tags: ["Basic", "Group Policy"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb61.png"
---

This weeks Group Policy Setting of the Week (GPSW) can be found under Computer > Policies > Administrative Templates > System and is called "Verbose vs normal status message". It is a really simple setting that doesn't actually do much but I dub this setting the "Make my computer start faster" setting which give users the illusion that their computer are working faster. [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb61.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image63.png>) So what does it do and how does it make my Computer start faster? This setting displays a number of extra status messages during the start up and shutdown of the computer and when the user is logging on and off. Some of the verbose status messages you will see are (but not limited to):

  * Mapping Drives
  * Playing Logon Sound
  * Mapping Printers
  * Applying Power Settings
  * Stopping Services

You will still see your Applying Computer settings and Preparing Desktop messages however these will be shown for a lot shorter time. Unfortunately it will not actually make your computer start any quicker but I have generally found that by enabling this option users seem to perceive that their computers are starting up quicker. Why? Well I think its because the extra status messages are holding their attention for a few seconds each time a new one is displayed something like the opposite of watching grass grow or a watched pot that never boils"... In any case this is still a handy setting to enable as at the very least will help your IT support troubleshoot logon performance issues. This setting will work on Windows 2000 and above and it will also show the processing of newer Group Policy Preferences.