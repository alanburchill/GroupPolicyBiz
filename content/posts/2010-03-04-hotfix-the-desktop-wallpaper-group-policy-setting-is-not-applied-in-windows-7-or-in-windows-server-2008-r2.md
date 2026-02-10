---
title: "Hotfix: The &quot;Desktop Wallpaper&quot; Group Policy setting is not applied in Windows 7 or in Windows Server 2008 R2"
date: 2010-03-04 22:14:52
author: admin
categories: ["News"]
tags: ["hotfix", "KB977944", "Wallpaper", "Windows 7"]
---

Just stumbled across this Microsoft KB that seem like a fairly common problem that may affect anyone who tries to apply a desktop wallpaper to a Windows 7 computer via Group Policy. Description:

> In an Active Directory domain network environment, you apply a "Desktop Wallpaper" Group Policy setting to the domain users. However, the setting is not applied to domain users who log on to client computers that are running Windows 7 or Windows Server 2008 R2. This issue varies if the following conditions are true:

>
>   * If the domain user logs on the domain after you deploy the "Desktop Wallpaper" Group Policy setting, the desktop background changes to black.

>   * **Note** The color of the desktop background varies, depending on the color scheme that you set.

>   * If the domain user logs on the domain before you apply the "Desktop Wallpaper" Group Policy setting, the desktop background does not change.

>
Additionally, in the **Personalization** window of the client computer, the desktop background is displayed as being changed to the setting that you applied.

For more info and links to the hotfix go to [The "Desktop Wallpaper" Group Policy setting is not applied in Windows 7 or in Windows Server 2008 R2](<http://support.microsoft.com/kb/977944>)