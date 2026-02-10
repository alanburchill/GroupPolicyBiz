---
title: "Group Policy Setting of the Week 35 "“ Display information about previous logons during user logon"
date: 2010-07-18 11:34:22
author: admin
categories: ["Setting of the Week"]
tags: ["Basic", "Last Interactive Logon", "lastLogontimeStamp", "logon", "Security"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb24.png"
---

This weeks setting is one that has just been mentioned in the [AD Blogs Friday mail sack](<http://blogs.technet.com/b/askds/archive/2010/07/17/friday-mail-sack-saturday-edition.aspx>) and until today was a setting/feature of Windows Vista/7 that I didn't know existed. This setting display information about previous logons during a user logon and is very similar to the last logon screen I see when logging onto an online banking web site. This setting can be found under Computer Configuration > Policies > Administrative Templates > Windows Components > Windows Logon Options and must be applied to workstations AND domain controllers for it to work. The only down side for this setting is that you need to be in 2008 native mode to work so this might exclude some organisations for now.

**WARNING:** Be sure that you apply this setting to your domain controllers first otherwise they will not be able to logon.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb24.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image26.png>)

Below is the message a users will see when after the logon successfully when the previous logon was also successful.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb25.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image27.png>)

In this example we see the message when someone logon successfully where the 5 previous logon events had failed. Obviously this logon count number (see highlighted below) would raise a really big red flag for a users especially if you are sure that you were not the one to logon incorrectly.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb26.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image28.png>)

For more information check out:

<http://blogs.technet.com/b/askds/archive/2009/04/15/the-lastlogontimestamp-attribute-what-it-was-designed-for-and-how-it-works.aspx>

<http://technet.microsoft.com/en-us/library/dd446680(WS.10).aspx>