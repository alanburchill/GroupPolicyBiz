---
title: "Internet Explorer 11 Group Policy Preferences"
date: 2013-11-13 09:27:00
author: admin
categories: ["News", "Tip"]
tags: ["Group Policy Preferences", "Internet Explorer 11"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2013/11/ieLogo_h_Web_thumb1.jpg"
---

[![ieLogo_h_Web](https://www.grouppolicy.biz/wp-content/uploads/2013/11/ieLogo_h_Web_thumb1.jpg)](<https://www.grouppolicy.biz/wp-content/uploads/2013/11/ieLogo_h_Web1.jpg>)

With the release of Internet Explorer 11 from Microsoft for Windows 7 I have seen a number of question asking where are the Group Policy Preferences are for this new version of the browser? The good news is that the current Internet Explorer 10 Group Policy Preferences officially supported see <http://support.microsoft.com/kb/2898604> .

This works as the default version checking goes from 10 to 99, meaning that it will happily apply the IE 10 settings to IE11.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/11/image_thumb3.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/11/image3.png>)

**Note:** This does not mean that the IE 10 Group Policy Preferences have any of the new options in IE 11.

The really good news is that this has always been the default behaviour of the IE 10 Group Policy Preferences in Windows Server 2012 meaning that if you already have IE 10 Group Policy Preferences configured you don't have to do anything to make them work for IE 11.

There is of course many ways to configured Internet Explorer and if you want to configured some of the new setting you can download the new IE 11 administrator templates to update your existing Group Policy Object or Central Store (see [Internet Explorer 11 Administrator Templates](<https://www.grouppolicy.biz/2013/11/internet-explorer-11-administrator-templates/> "https://www.grouppolicy.biz/2013/11/internet-explorer-11-administrator-templates/") ). But this is only required if you want to configure any of the 54 new Group Policy setting in the administrative templates.

**Tip:** You can get a full list of these IE setting from the [Group Policy Settings Spread Sheet](<https://www.grouppolicy.biz/2013/11/out-now-group-policy-settings-spread-sheet-for-windows-8-1-windows-server-2012-r2-and-internet-explorer-11/> "Permanent Link to Out Now- Group Policy Settings spread sheet for Windows 8.1, Windows Server 20").

It's also worth remembering that since Internet Explorer 10 the Internet Explorer Maintenance has been removed from Group Policy. If you have the option setting configured in a policy it will still apply but the UI to edit these policy settings is now removed on any computer with Internet Explorer 10 or greater installed. The good news is that you can replace this functionality with combination of Administrative Templates, Group Policy Preferences and Group Policy Preferences Registry Keys. While this sounds a little klunky I still definitely recommend stop using IE Maintenance as its days are well and truly over. I show you how to duplicate the setting from IE Maintenance to the newer ways in my TechEd New Zealand 2013 session [The Browser You Love to Hate](<https://www.grouppolicy.biz/2013/09/teched-the-browser-you-love-to-hate/> "https://www.grouppolicy.biz/2013/09/teched-the-browser-you-love-to-hate/").

**TIP:** Once you are done with the Internet Explorer Maintenance be sure to clean up the old setting by doing a "Rest Browser Settings" see [How to remove imported Internet Explorer Group Policy Settings](<https://www.grouppolicy.biz/2010/04/how-to-remove-imported-internet-explorer-group-policy-settings/>)

For additional info see:

<http://sdmsoftware.com/group-policy-blog/group-policy-preferences/gp-preferences-for-internet-explorer-11/>