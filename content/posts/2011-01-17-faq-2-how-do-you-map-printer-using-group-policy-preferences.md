---
title: "Group Policy FAQ #2: How do you map a printer using Group Policy Preferences?"
date: 2011-01-17 05:34:56
author: admin
categories: ["FAQ"]
tags: ["Group Policy Preferences", "Printer"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2011/01/image_thumb.png"
---

In this second of what I am sure are many FAQ posts, I am going to show you how you can use Group Policy Preferences to map printers in your organisation to help you do away with mapping printers via logon scrips.

Firstly this is only a brief introduction to printer mappings. If you want a more advanced tutorial on using Printer Preference then I recommend you take a look at my other post [How to use Group Policy Preferences to dynamically map printers with Roaming Profiles](<https://www.grouppolicy.biz/2010/01/how-to-use-group-policy-preferences-to-dynamically-map-printers-with-roaming-profiles/>).

Firstly you will need to check that you have already have got the [Group Policy Preference Prerequisites](<https://www.grouppolicy.biz/2010/12/group-policy-preferences-prerequisites/>) installed and you also have the [Group policy Management Console Installed](<https://www.grouppolicy.biz/2010/03/how-to-download-and-install-the-group-policy-management-console-gpmc/>) on a management computer in your environment.

Now to map the printers all you need to do is go to the [Printer Extension](<http://technet.microsoft.com/en-us/library/cc731562.aspx>) option of the Group Policy you want to apply the setting from (see below).

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/01/image_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/01/image.png>)

All you need to do now is put the UNC Path of the printer in the "Shared path:" text field and your done. No more batch files, vbscripts or KIX scripts to edit and maintain for mapping printers".... NICE!!!

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/01/image_thumb1.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/01/image1.png>)

Also remember that you can also target this setting using [Preference Item-Level Targeting](<http://technet.microsoft.com/en-us/library/cc733022.aspx> "http://technet.microsoft.com/en-us/library/cc733022.aspx") using the traditional [Security Group Targeting](<http://technet.microsoft.com/en-us/library/cc772471.aspx>) or you can be a little more dynamic and use [IP Address Range Targeting](<http://technet.microsoft.com/en-us/library/cc732310.aspx>) or [Site Targeting](<http://technet.microsoft.com/en-us/library/cc732583.aspx>).