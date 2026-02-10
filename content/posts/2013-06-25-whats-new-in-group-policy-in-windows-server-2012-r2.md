---
title: "What&rsquo;s new in Group Policy in Windows Server 2012 R2"
date: 2013-06-25 03:03:26
author: admin
categories: ["News"]
tags: ["Widnows Server 2012 R2"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2013/06/image_thumb21.png"
---

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/06/image_thumb21.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/06/image22.png>)Thanks to Orin Thomas blog about [Windows Server 2012 R2](<http://windowsitpro.com/blog/server-2012-r2-preview-available-windows-azure>) I have discovered that Microsoft has released a Windows Server 2012 R2 image on Azure. This has allowed me to run up a Windows 2012 R2 Active Directory so I can crack open and see what is new in Group Policy. Below is a summary of only a VERY quick look at this new server OS highlighting some of the more interesting settings"... I will definitely take a deeper dive into some of these features soon.

**Update:**

  * You can now restart and shutdown the computer from the start button by Right Click Start Button > Shutdown


[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/06/image_thumb32.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/06/image33.png>)

**Update2:**

  * There is also a "cversion.ini" file meaning that it is somewhat likely that you will be able to hack this file to upgrade from Beta to RTM once it is released. (see <http://blogs.msdn.com/b/e7/archive/2009/04/07/delivering-a-quality-upgrade-experience.aspx> which was a hack to upgrade to Windows 7 from the Beta that also worked with Windows 8 beta).


[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/06/image_thumb34.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/06/image35.png>)

  * In case you were wondering the Start Button (not menu) is also back in server (see below).


[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/06/image_thumb22.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/06/image23.png>)

  * A Group Policy specific feature is called "Group Policy Caching" specifically it is described as


> This cache saves applicable GPOs and the settings contained within them. When Group Policy runs in synchronous foreground mode, it refers to this cache, which enables it to run faster

This should allow users to more quickly apply group policy to their computers when the DC is only available over a slow link such as WAN's or via Direct Access.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/06/image_thumb23.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/06/image24.png>)

  * Another new Group Policy Feature is the ability to delay a logon script from executing when a computer starts up or a user log's on. This is handy if you still need to run a legacy logon script for some reason but allows it to run slightly delayed as to now slow down the start-up process.


[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/06/image_thumb24.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/06/image25.png>)

  * Here is the full details for the Start Menu configuration that i mentioned in a previous blow post [Customising Windows 8.1 Start Screen Layout with Group Policy](<https://www.grouppolicy.biz/2013/06/customising-windows-8-1-start-screen-layout-with-group-policy/>)


[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/06/image_thumb25.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/06/image26.png>)

  * Confirmed support for SPDY/3 protocol in Internet Explorer 11


[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/06/image_thumb26.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/06/image27.png>)

  * Pre-emptive loading of web pages in IE 11 which sounds similar to how Chrome background loads web pages before you visit.


[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/06/image_thumb27.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/06/image28.png>)

  * Anti Malware software can now scan Active-X controls before they run in the browser.


[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/06/image_thumb28.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/06/image29.png>)

  * Phone number detection in IE11 means apps can be registered as the default dialler app for phone numbers in web pages without the need for plugins


[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/06/image_thumb29.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/06/image30.png>)

  * Work Folders URI configuration is what allows you to setup a SkyDrive like file sync experience


[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/06/image_thumb30.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/06/image31.png>)

That's it for my very quick take of this new server OS. Unfortunately there does not appear to be any "Boot to Desktop" Group Policy setting or Internet Explorer 11 Group Policy Preferences"... However this is the Beta of the OS and these setting could still be tucked away some where I have not found yet.