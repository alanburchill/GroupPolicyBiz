---
title: "Hotfix: &ldquo;Configure new tab page default behavior&rdquo; does not work"
date: 2010-03-19 07:46:42
author: admin
categories: ["News"]
tags: ["hotfix", "Internet Explorer", "KB980959"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb55.png"
---

Microsoft have just released a hotfix ([KB980959](<http://support.microsoft.com/?kbid=980959>)) to fix the problem with the "Configured new tab page default behaviour" group policy setting not working for Internet Explorer 8. Apparently the Intetres.admx had the wrong path configured path is configured to "Software\Policies\Microsoft\Internet Explorer\Main" where it should be configured to "Software\Microsoft\Internet Explorer\TabbedBrowsing\NewTabbedPageShow". If you want to see the setting for your self just look for the text "NewTabAction" in the Inetres.admx file. [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb55.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image55.png>) For details on getting the hot fix and to see the full article "The "Configure new tab page default behavior" Group Policy setting does not work on a computer that is running Windows 7 or Windows Server 2008 R2 and that has Internet Explorer 8 installed" here <http://support.microsoft.com/?kbid=980959>