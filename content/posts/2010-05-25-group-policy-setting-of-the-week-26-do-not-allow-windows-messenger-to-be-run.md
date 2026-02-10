---
title: "Group Policy Setting of the Week 26b "“ Do not allow Windows Messenger to be Run"
date: 2010-05-25 00:10:08
author: admin
categories: ["Setting of the Week"]
tags: ["Group Policy", "SOE", "Windows Messenger", "Windows XP"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/05/image_thumb23.png"
---

(Wow"... I have been doing this for 6 months now"... how time flies"... )

This weeks setting of the week is another old one however it is very important for any environment that is still running Windows XP SOE. The "Do not allow Windows Messenger to be run" will prevent any user from running Windows Messenger that comes out of the box with Windows XP. Now Windows Messenger 4.6 that comes with Windows XP is no longer supported but disabling the program should help avoid any confusion for user that also have Windows Live Messenger installed.

This is a user setting that can be found under User Configuration > Policies > Administrative Templates > Windows Components > Windows Messenger and while it does say it applied to Windows XP this in reality is only a Windows XP setting as there is no Windows Messenger in Windows Vista or above.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/05/image_thumb23.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/05/image22.png>)

While most organisation already have this program removed from the SOE (see image below) this is a good safety net setting for anyone who has joined their non-SOE version of messenger to the domain.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/05/image_thumb24.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/05/image23.png>)

Now to be clear this will only prevent the user running Windows Messenger and not the live of Windows Live Messenger or other third-party messenger programs.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/05/image_thumb25.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/05/image24.png>)

This setting will not remove messenger from the computer but when the users clicks on the Windows Messenger link.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/05/image_thumb26.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/05/image25.png>) ,