---
title: "Hotfix: Roaming profile users experience slow logons on Windows 7 or Windows Server 2008 R2 client computers"
date: 2011-06-07 22:49:07
author: admin
categories: ["hotfix"]
tags: ["AppData", "KB981830"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2011/06/hotfix_icon_thumb.png"
---

[![hotfix_icon](https://www.grouppolicy.biz/wp-content/uploads/2011/06/hotfix_icon_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/06/hotfix_icon.png>)Microsoft has just released a new hotfix to address an issue with slow logon performance when you use AppData folder redirection.

> Consider the following scenario in a network environment:

>
>   * You configure users to use roaming profiles to log on to a client computer that is running Windows 7 or Windows Server 2008 R2.

>   * You redirect the %AppData%\Roaming folder to a network share.

>   * You enable the **Do not automatically make redirected folders available offline** Group Policy setting on the client computer.

>   * You enable both of the following Group Policy settings for the %AppData%\Roaming folder:

>     * **Administratively assigned offline files**

>     * **Turn on economical application of administratively assigned Offline Files

> **

> This configuration specifies that only new files or folders in the %AppData%\Roaming folder are synchronized during the logon process.

>

>

> In this scenario, the users encounter slow logon behavior on the client computer.

In addition to this hotfix you will also need to make some registry changes which of course you can easily deploy this using the Group Policy Preferences [Registry Extension](<http://technet.microsoft.com/en-us/library/cc771589.aspx>).

Link <http://support.microsoft.com/kb/981830>