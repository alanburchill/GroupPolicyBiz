---
title: "Group Policy Setting of the Week 39 &ndash; Always use custom logon background"
date: 2010-08-16 12:00:00
author: admin
categories: ["Setting of the Week"]
tags: ["Background", "logon"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/08/image_thumb24.png"
---

This week setting of the week allows you to prefer a custom logon background image in Windows 7. This setting is called "Always use custom logon background" and can be found under Computer Configuration > Policies > Administrative Templates > System > Logon.

Microsoft brought back the option to easily customise the logon background in Windows 7 as this was previously possible in Windows XP but it was removed with Windows Vista which left people with some [pretty messy workaround](<http://social.technet.microsoft.com/Forums/en-US/itprovistasetup/thread/7c025b9d-6d37-45d4-9db5-2d7850e38232>)s.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/08/image_thumb24.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/08/image25.png>)

Once you have enabled this option all you have to do to create the "%windir%\system32\oobe\info\backgrounds" folder and populate it with a backgroundDefault.jpg image and your computer will then use that as the background image when logging on and off.

**Note:** Some sites will direct you to configured the **OEMBackground** or **UseOEMBackground** in the **HKLM\Software\Microsoft\Windows\CurrentVersion\Authentication\LogonUI\Background** however this setting will negate the need to set this key.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/08/image_thumb25.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/08/image26.png>)

For more info on how to configure a custom background check out [Windows 7 to officially support logon UI background customization](<http://www.withinwindows.com/2009/03/15/windows-7-to-officially-support-logon-ui-background-customization/>)