---
title: "Native Boot to Desktop Group Policy Support for Windows 8.1"
date: 2013-09-09 21:45:25
author: admin
categories: ["News", "Tip"]
tags: ["Boot to Desktop", "Windows 8.1"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2013/09/image_thumb.png"
---

Microsoft has just released the RTM version for people who have MSDN or TechNet subscriptions of Windows 8.1 and Windows Server 2012 R2 (see <http://blogs.technet.com/b/windowsserver/archive/2013/09/09/attention-technet-and-msdn-subscribers-windows-server-2012-r2-available-for-download-today.aspx>). The really great new about this release is that there are a few new Group Policy setting, most notably NATIVE support for IT Administrators to configured boot to desktop.

The setting name is called "Go to the desktop instead of Start when signing in or when all the apps on a screen are closed" and can be found under the User Configuration > Policies > Administrative Templates > Start Menu and Taskbar. Certainly Microsoft has gone out an made the policy setting name a bit long but I am sure it will become to be know as the "Boot to desktop" group policy setting.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/09/image_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/09/image.png>)

Its pretty simple to implement just check the "enable" option and apply the policy to all your Windows 8.1 accounts and they will go straight to the desktop when they logon.

So there you have it you can natively configure your users computers so they can boot straight to the desktop using fully supported group policy settings. Is this a feature that has been sorely missed? do you think organisation will configured this by default for there 8.1 rollouts? let me know what you think in the comments below.