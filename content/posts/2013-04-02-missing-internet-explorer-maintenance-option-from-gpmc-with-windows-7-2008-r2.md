---
title: "Missing Internet Explorer Maintenance option from GPMC with Windows 7 / 2008 R2"
date: 2013-04-02 02:11:07
author: admin
categories: ["News", "Tip"]
tags: ["Internet Explorer 10", "Internet Explorer Maintainence", "Windows 7", "Windows Server 2008 R2"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2013/04/IE9answer_thumb.png"
---

[![IE9answer](https://www.grouppolicy.biz/wp-content/uploads/2013/04/IE9answer_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/04/IE9answer.png>)One of the changes with Windows 8 and Group Policy was that the Internet Explorer Maintenance section of GPMC was removed from under Windows Settings (see [Interesting Change to Group Policy in Server 2012/Windows 8](<http://sdmsoftware.com/group-policy-management-2/interesting-change-to-group-policy-in-server-2012windows-8/> "http://sdmsoftware.com/group-policy-management-2/interesting-change-to-group-policy-in-server-2012windows-8/")). However people have been [noticing](<http://social.technet.microsoft.com/Forums/en-US/winserverGP/thread/42060454-1e1d-492f-b774-836f6fd1e5bf/>) that the same Internet Explorer Maintenance option is removed from GPMC when they now install IE 10 on Windows 7 / Serve 2008 R2 (See image below).

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/04/image_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/04/image.png>)

So if you still use the Internet Explorer Maintenance section in Group Policy be aware that you will lose access to the ability to edit these policy setting if you update to IE10.

Alternatively you can simply reset the Internet Explorer Maintenance settings (see [How to remove imported Internet Explorer Group Policy Settings](<https://www.grouppolicy.biz/2010/04/how-to-remove-imported-internet-explorer-group-policy-settings/>)) and just use the standard Group Policy Administrative Templates or Group Policy preferences. In which case you will also want to read my other post about controlling IE Site Zone mappings using preferences [How to configuring IE Site Zone mapping using group policy without locking out the user](<https://www.grouppolicy.biz/2012/07/how-to-configuring-ie-site-zone-mapping-using-group-policy-without-locking-out-the-user/>)

**TIP:** I have not verified this but some people say that un-installing IE10 will restore the Internet Explore Maintenance option in GPMC

**Warning:** Some people are having issues with just removing IE10. So if you are having issues check out the comment in Darren Mar-Elia blog post [WARNING: Installing IE 10 on your Windows 7 Workstation Removes IE Maintenance Policy from Group Policy](<http://sdmsoftware.com/ie-policy/warning-installing-ie-10-on-your-windows-7-workstation-removes-ie-maintenance-policy-from-group-policy/> "http://sdmsoftware.com/ie-policy/warning-installing-ie-10-on-your-windows-7-workstation-removes-ie-maintenance-policy-from-group-policy/")