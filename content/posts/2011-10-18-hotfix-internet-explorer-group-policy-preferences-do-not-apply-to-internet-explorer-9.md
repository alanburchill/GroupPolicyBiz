---
title: "Hotfix: Internet Explorer Group Policy Preferences do not apply to Internet Explorer 9"
date: 2011-10-18 02:11:15
author: admin
categories: ["hotfix"]
tags: ["Group Policy Preferences", "hotfix", "Internet Explorer 9", "KB2530309"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2011/10/hotfix_icon_thumb.png"
---

[![hotfix_icon](https://www.grouppolicy.biz/wp-content/uploads/2011/10/hotfix_icon_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/10/hotfix_icon.png>)[![IE9answer](https://www.grouppolicy.biz/wp-content/uploads/2011/10/IE9answer_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/10/IE9answer.png>)If you have have been using the some what simple hack I mentioned to make Group Policy Preference work with Internet Explorer 9 you will be relieved to know that Microsoft have now fixed an official hotfix to make this work.

You can get read the full Microsoft Kb article at <http://support.microsoft.com/kb/2530309> .

However you should take special attention at the two notes:

> This update does not re-write the version information for existing settings. Instead, you must define a new set of Internet Explorer settings in a new or existing Group Policy Object.

Meaning you will need to re-created the Group Policy Preference before the policy will apply to a computer running IE9.

> This update does not create a new Internet Explorer 9 UI item. However, when define new Group Policy Preferences settings, and you select the **Internet Explorer 8** option, this setting now applies both to Internet Explorer 8 and to Internet Explorer 9

This means that you will NOT see an Internet Explorer 9 option in the Internet Settings menu (see image below), however using the IE8 option will work with IE9.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/10/image_thumb5.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/10/image5.png>)

If we take a closer look at the "InternetSettings.xml" after the hotfix has been applied shows the maximum version number is now set to "10.0.0.0" where previously this version was "9.0.0.0". However you existing Internet Explorer Preferences will remain unaffected"...

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/10/image_thumb6.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/10/image6.png>)

Thanks to Mark Feetham [MSFT] for leaving a [comment](<https://www.grouppolicy.biz/2011/03/how-to-enable-group-policy-preferences-support-for-ie9/comment-page-1/#comment-3572>) on my previous [blog post](<https://www.grouppolicy.biz/2011/03/how-to-enable-group-policy-preferences-support-for-ie9/>) about this new hotfix.

Download it now from <http://support.microsoft.com/kb/2530309>