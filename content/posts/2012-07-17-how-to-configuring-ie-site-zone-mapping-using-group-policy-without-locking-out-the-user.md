---
title: "How to configuring IE Site Zone mapping using group policy without locking out the user"
date: 2012-07-17 01:48:02
author: admin
categories: ["Tutorials"]
tags: ["Intermediate", "Internet Explorer", "Internet Explorer Maintainence", "Zones"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2012/07/071712_0138_Howtoconfig12.png"
---

![](https://www.grouppolicy.biz/wp-content/uploads/2012/07/071712_0138_Howtoconfig12.png)If you saw my [tweet](<https://twitter.com/alanburchill/status/223590041522421760>) or Darren Mar-Elia [blog post](<http://www.sdmsoftware.com/group-policy-management-2/interesting-change-to-grouppolicy-in-server-2012windows-8/>) you may be glad to know that the legacy Internet Explorer Maintenance section of group policy has now been removed in Windows 8. Unfortunately this means that you can now longer natively configured the IE Site to Zone mapping using native group policy setting without still allowing the user to customise the URL list. So below I will show you how you can still use Group Policy to configure the IE Zone via group policy while still allowing the user the ability to add additional sites. Put simply we are going to setup the IE Zone registry keys manually using Group Policy Preferences"... However it's a little complicated as the URL that is in the Site to Zone mapping is actually stored as the name of the key. Finally the protocol is the registry value with a number that assigns it to the corresponding zone. In the example we use we will first look at the currently site that the users has setup in the trusted site list ([www.bing.com](<http://www.bing.com>)). As you can see below the zone is store at **HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\Domains** then the domain is stored as a key "Bing.com" then "www". Within the "www" key the protocol (http and/or https) is the value name with the value representing what zone it should be a member. **Note:** We are just using bing.com as an example as you would never add at search engine as a trusted site. ![](https://www.grouppolicy.biz/wp-content/uploads/2012/07/071712_0138_Howtoconfig22.png) Now we will add the additional site [www.google.com.au](<http://www.google.com.au>) also to the trusted sites list using group policy. **Step 1**. Edit a Group Policy that is targeted to the users that you want the IE Zones applied. **Step 2.** Create a new Group Policy Preferences [Registry Extension](<http://technet.microsoft.com/en-us/library/cc771589.aspx>) then select the "HKEY_CURRENT_USERS" Hive and then type "Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\Domains\google.com.au\www" in the Key path. Then enter the Value name of "HTTP" and selected the Value Type as "REG_DWORD" and set the value data as "00000002". ![](https://www.grouppolicy.biz/wp-content/uploads/2012/07/071712_0138_Howtoconfig32.png) And you're Done"... **TIP:** For your reference the values and their corresponding Zones are listed below in the table.

Value | Zone Name
---|---
00000000 | My Computer
00000001 | Local Intranet
00000002 | Trusted Site
00000003 | Internet
00000004 | Restricted

As you can see below the IE zone will push out to your users and it will be added to the trusted zone list, while still allowing them to add and remove other zones from the list. ![](https://www.grouppolicy.biz/wp-content/uploads/2012/07/071712_0138_Howtoconfig42.png) **TIP:** As always the native group policy settings will take precedence over Group Policy Preferences therefore if you have the "Site to Zone Assignment List" setting configured as well this will override (not merge) the above settings (See image below). ![](https://www.grouppolicy.biz/wp-content/uploads/2012/07/071712_0138_Howtoconfig52.png)