---
title: "New Group Policy Hotfix&rsquo;s"
date: 2010-10-19 08:00:00
author: admin
categories: ["News"]
tags: ["hotfix", "Internet Explorer", "KB2379592", "KB970840"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/10/image_thumb20.png"
---

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/10/image_thumb20.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/10/image20.png>)The guys at the [Ask the Directory Services Team](<http://blogs.technet.com/b/askds/>) blog have just published the list of latest Directory Services related hotfixes ( see <http://blogs.technet.com/b/askds/archive/2010/10/18/new-directory-services-content-10-10-10-16.aspx> ). For your convenience I have put in a direct link and a short description for the two Group Policy related hotfixes.

[KB2379592](<http://support.microsoft.com/kb/2379592>) \- "Object reference not set to an instance of an object" error message when you view the GPO backup settings in the Group Policy Management Console.

#### **Description**

Resolves an "Object reference not set to an instance of an object." when you select the "View Settings" of a GPO that has an advanced audit policy setting configured that you have also backed up.

[KB970840](<http://support.microsoft.com/kb/970840>) \- Some settings in Group Policy Preferences for Internet Explorer do not deploy correctly to computers that are running Windows Server 2008, Windows Vista, Windows 7 or Windows Server 2008 R2

#### Description

Resolves the following IE8 preference settings from not working:

  * Check boxes under **Accessibility**
    * "Reset text size to medium while zooming"
    * "Reset Zoom level to 100% for new windows and tabs"
  * Check boxes under **Security**
    * "Allow active content to run in files"
    * "Allow software to run or install even..."
  * Check boxes under **International**
    * "Send IDN Server Names"
    * "Send UTF -8 URL"
    * "Show information bar for encoded address"


It also resolves a freeze/crash in the Group Policy Object Editor when you are editing an Internet Explorer Group Policy Preferences setting.