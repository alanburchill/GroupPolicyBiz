---
title: "Group Policy Hotfix Round Up"
date: 2011-06-15 22:42:52
author: admin
categories: ["hotfix"]
tags: ["Group Policy"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2011/06/hotfix_icon_thumb1.png"
---

[![hotfix_icon](https://www.grouppolicy.biz/wp-content/uploads/2011/06/hotfix_icon_thumb1.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/06/hotfix_icon1.png>)Microsoft have just released ~~another two~~ a few more Group Policy related hotfixes'. Below is the description of each issue that it resolves and link to the related KB Article.

[GetGPOList function does not return all GPOs in Windows 7 or in Windows Server 2008 R2](<http://support.microsoft.com/kb/2553771>)

> Consider the following scenario:

>
>   * You have a computer that is running Windows 7 or Windows Server 2008 R2.

>   * You use the **LocalSystem** account to run a service on the computer.

>   * The service calls the **GetGPOList** function to query all Group Policy objects (GPO) that are applied on a computer.

>   * The ****Authenticated Users**** group is removed from the access control list (ACL) in an applied GPO.

>

>

> In this scenario, the **GetGPOList** function does not return all applied GPOs. The function returns only GPOs that have the **Authenticated Users******group in the ACL of the GPO.

[When you use a GPO for application deployment in Windows 7 or in Windows Server 2008 R2, the deployment fails](<http://support.microsoft.com/kb/2537556/>)

> In an Active Directory Domain Services (AD DS) environment, you cannot use a Group Policy Object (GPO) to deploy applications for installation on client computers that are running Windows 7 or Windows Server 2008 R2. When you try to apply the GPO, you receive an error message that resembles the following:

>
>   * Windows failed to apply the Software Installation settings

>


[Group Policy logon scripts do not run in Windows 7 or in Windows Server 2008 R2](<http://support.microsoft.com/kb/2550944/>)

> Consider the following scenario in an Active Directory domain environment:

>
>   * You deploy logon scripts by using Group Policy.

>   * You set logon scripts to run synchronously.

>   * You try to log on to a client computer that is running Windows 7 or Windows Server 2008 R2.

>

>

> In this scenario, the logon scripts do not run before the logon process.

[A user who has administrator permission can delete printers on a computer that is running Windows 7 or Windows Server 2008 R2 after you deploy the "Prevent deletion of printers" Group Policy](<http://support.microsoft.com/kb/2549067/>)

> Consider the following scenario:

>
>   * You deploy the ****Prevent deletion of printers**** Group Policy in your environment.

>   * You have a client computer that is running Windows 7 or Windows Server 2008 R2.

>   * A user who has administrator permission logs on to the client computer.

>

>

> In this scenario, the user can still delete printers in **Devices and Printers** unexpectedly.