---
title: "Installing IE9 on Windows 7 Service Pack 1 doesn't require a reboot"
date: 2011-02-18 11:25:27
author: admin
categories: ["News"]
tags: ["IE9", "Internet Explorer", "Service Pack 1", "Windows 7", "Windows Server 2008 R2"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2011/02/IE9answer_thumb1.png"
---

[![IE9answer](https://www.grouppolicy.biz/wp-content/uploads/2011/02/IE9answer_thumb1.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/02/IE9answer1.png>)

**Update:** Now that I have installed the final version of IE9 on 6 computers 2 of them needed to rebook so it would seem that it may or may not require a reboot. This seems to be dependent on what application you are running at the time. Therefore it would still be prudent to plan for a reboot but not always expect it to happen.

I have just install IE9 on a Windows 7 and a Windows Server 2008 R2 computer running Service Pack 1 and I was very pleased to see that in both cases it does not required a reboot to install. Previously I have installed IE9 on 3 Windows 7 computers that were not running service pack 1 however they all required a reboot to install IE9. Therefore it seems that with Windows 7 / 2008 R2 Service Pack 1 installed it is now possible to install IE9 without a reboot. (see images below).

**Disclaimer:** ~~I have only seem this behaviour on one computer so far but I am testing it one more really soon.~~ I have now repeated this process on a Windows Server 2008 R2 SP1 and Windows 7 SP1. It looks more likely that this option to install IE9 without a reboot is a new feature of Service Pack 1.

One of the dialogue boxes (see below) on Windows Server 2008 R2 Service Pack 1 during the IE9 install asks if you want to the installer to close your running programs to install it without a reboot. So if you select the "Close programs for me (I already save my work)" opting the browser will be installed without a reboot.\

( FYI: The screenshots below are from a computer running Windows Server 2008 R2 Service Pack 1 with the Domain Controller role installed and running. )

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/02/image_thumb15.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/02/image15.png>)

The next screen is the dialogue box during install of IE9. As you can see IE8 and the Explorer shell has been closed during the install but the OS has NOT rebooted.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/02/image_thumb16.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/02/image16.png>)

After IE9 is installed the Explorer Shell is launched again still without interruption to the OS.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/02/image_thumb17.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/02/image17.png>)

This is a huge deal as it means that it is likely that updates to the browser will be able to be installed without having to require a reboot of the OS. Now this may be a nice have for end users however this is a much bigger deal for Windows Servers as IT administrators as they can now patch what is the most vulnerable part of the server OS (the browser) without any down time. This should hopefully mean that IT administrators will not need to revert to installed "Server Core" versions of the server OS's just to ensure that they don't have to reboot them every patch Tuesday to keep them secure.

I know this is not specifically a Group Policy topic however this is a really super cool find that I just had to share with everyone"...