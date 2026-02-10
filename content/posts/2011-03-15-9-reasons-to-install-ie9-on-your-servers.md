---
title: "9 reasons to install IE9 on your Servers"
date: 2011-03-15 13:00:00
author: admin
categories: ["News"]
tags: ["IE9", "Internet Explorer", "Internet Explorer 9", "Windows Server"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2011/03/image_thumb29.png"
---

[![Windows Server and Internet Explorer 9 Logo](https://www.grouppolicy.biz/wp-content/uploads/2011/03/image_thumb29.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/03/image28.png>)Microsoft have [just released Internet Explorer 9 to the web](<http://www.beautyoftheweb.com/>) and so Windows users around the world will now be truly able to enjoy the "[Beauty of the Web](<http://www.beautyoftheweb.com/>)". While IE9's [hardware acceleration](<http://blogs.msdn.com/b/ie/archive/2011/02/08/focusing-on-real-world-web-performance-with-internet-explorer-9.aspx>) and new [un-cluttered UI](<http://blogs.msdn.com/b/ie/archive/2011/02/15/user-experiences-listen-learn-refine.aspx>) is really enjoyable for consumers this browser also has a number of new features that makes it very compelling to install on your servers. So below I have listed 9 reasons why you should also consider deploying IE9 to your servers in your organisation"...

**#1 Group Policy** \- Internet Explorer 9 is still the only browser that has comprehensive Group Policy Support with over 1500 setting. This allows you as an administrator to have the power to configure the browser on their servers to ensure they are correctly and securely configured.

**#2 Memory Security Enhancements** "“ As administrator we sometimes find our self having to use the internet on a server probably to look up an error message or to download some tool we need to install to complete out work. IE8 by default has ASLR****(Address Space Layout Randomization) and DEP/NX (Data Execution Prevention / No eXecute) enabled by default which provided very good protection for the browser. However even with these two layers of protection [Stephen Fewer at Pwn2Own 2011](<http://www.zdnet.com/blog/security/pwn2own-2011-ie8-on-windows-7-hijacked-with-3-vulnerabilities/8367>) was able to get around this security by using a combination of not 1, not 2 but 3 different vulnerabilities.

But Microsoft then quickly [tweeted](<http://twitter.com/#!/msftsecresponse/status/45939417998831617>) out that the same attack would not work on IE9 RC. While there are no details as to why the IE9 RC browser was not vulnerable to the same attack certainly the additional protection of having been compiled with SafeSEH (Safe Structured Exception Handling) would have helped.

> "(SafeSEH) helps ensure that structured exception handling cannot be used as an exploit vector"

More info see <http://blogs.msdn.com/b/ie/archive/2011/03/07/internet-explorer-9-security-part-1-enhanced-memory-protections.aspx>

**#3 Tab Isolation** "“ [Tab Isolation](<http://blogs.msdn.com/b/ie/archive/2010/03/04/tab-isolation.aspx>) or hang recovery is another feature of IE9 that allows you to keep using your browser when a particular web pages causes IE to crash. While this is generally just an inconvenience for users on workstations this can be a life saver if you are on a server as your browser will now more likely to only lose your work in your current tab rather than the 11 other things you were doing in the browser at the same time.

**#4 Simpler UI** "“ Using a browser on a server is a lot different experience than on a workstation. You really don't need fancy tool bars in your browsers to do your job and some times you have limited screen resolution as you might be working on the server via a console with only a 1024x768 screen resolution due to not having the proper video card drives loaded. Therefore the new simpler, cleaner and smaller UI makes give you more real-estate on screen for you web pages and a lot less clutter getting in the way than any other browser.

[![Opera Safari Firefox Chrome Internet Explorer UI Compared](http://ie.microsoft.com/testdrive/IEBlog/2011/Feb/uellr-image1.png)](<http://blogs.msdn.com/b/ie/archive/2011/02/15/user-experiences-listen-learn-refine.aspx>)

However if you are a fan of the clutter however you can still enable your toolbars and menu bars.

For more info see <http://blogs.msdn.com/b/ie/archive/2011/02/15/user-experiences-listen-learn-refine.aspx>

**#5 ActiveX Filtering "“** Browser add-on's and ActiveX control are just a bad idea on servers. Weather it is slow performance due to the bloat of running so many add-on products or its the multiple security vulnerabilities that make add-on the new security attack vector. Therefore the new ActiveX Filtering that allows you run ActiveX controls in an opt-in mode meaning you only explicitly run the controls you trust. This setting is not on by default but you can enabled using the "Turn on ActiveX Filtering" group policy (see image below and point #1).

[![Turn on ActiveX Filtering](https://www.grouppolicy.biz/wp-content/uploads/2011/02/image_thumb10.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/02/image10.png>)

**#6 Web Tracking Protection** "“ Almost all sites on the Internet (this site included) have some sort of embedded web tracking to allow site owners monitor the activity of their visitors. However if you are using your browser on a server it is not desirable that you activities are tracked. To help with this problem IE9 has introduced a feature called [Web Tracking Protection](<http://blogs.msdn.com/b/ie/archive/2011/02/24/web-tracking-protection-an-emerging-internet-standard-that-helps-protect-consumers-from-tracking.aspx>) that allow users to block certain third party web sites. Therefore an administrator can subscribe to a [third party tracking lists](<http://ie.microsoft.com/testdrive/Browser/TrackingProtectionLists/Default.html>) or even create their own to prevent their browser from contacting any undesirable web sites from the client.

**#7 Add On Performance Monitor** "“ I know that in #5 I said that installing browser add-on's on a server is a bad idea however sometimes this is just a necessary evil. In this case IE9 will [monitor your add-on performance](<http://blogs.msdn.com/b/ie/archive/2010/09/17/add-ons-staying-in-control-of-your-browsing-experience.aspx>) and give you a warning when any of them are running slow and then let you selectively disable them (see below).

![Choose Add-ons dialog - performance characteristics of add-ons are listed with the choice to disable them.](http://ieblog.members.winisp.net/images/Herman_AddOnAdvisor_5.png)

**#8 Automatic Update "“** It holds true that all web browsers will need updating on a regular basis as they are the most exposed attack surface on your computer. However Internet Explorer is the only one that is integrated with Windows Update, allowing you to use the same standard update and reporting process. This means that that reporting tools such as WSUS or SCCM can give you a status reports as to see what computers still have out of date software and thus make sure all your software is up to date without any slipping through the gate. This helps avoids a scenario that I am sure that many IT admins can relate to of logging on to a server only to see that a grossly out of date versions of Adobe Read installed because no one ever new it was installed and had to be updated"...

**#9 Install Updates without reboot "“** __and saving the best for last, this reasons is the BIG ONE!!!!__ Also continuing on from #8 and as I [previously mentioned](<https://www.grouppolicy.biz/2011/02/windows-7-sp1-ie9-install-does-not-require-reboot/>) you no longer to you need to reboot your server to install updates to your browsers (see image below). Gone are the mandatory reboots of the server you have had to endure every month after patch Tuesday which will make your life SO MUCH EASIER!!!

**Note:** You will need to be running Windows 2008 R2 service pack 1 to be able to do this so it is not going to help if you are still running Server 2008 (sorry).

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/02/image_thumb15.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/02/image15.png>)

As I mentioned before there is of course many other reasons why IE9 is such a great product for consumers that I have not talked about (hardware acceleration, video tag support, Aero Snap and Pinned sites) however as you can see this is still a compelling for your server as well"...

Did I mention no reboots to install updates!!!