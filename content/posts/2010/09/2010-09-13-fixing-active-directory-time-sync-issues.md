---
title: "Fixing Active Directory Time Sync Issues"
date: 2010-09-13 08:00:00
author: admin
categories: ["Other Site Links"]
tags: ["Group Policy Preferences", "scheduled task", "Time Sync"]
---

You might think that AD time sync in your organisation is something that just works out of the box but [Sander Berkouwer](<http://blogs.dirteam.com/blogs/sanderberkouwer/about.aspx>) has just done a post about what you need to do to setup time sync for Windows Server 2008 & R2. Apparently the default time sync server for Windows Server 2003 (time.windows.com) no long works so you need to make sure that you DC are configured with a valid time source.

Check out the whole article here [The things that are better left unspoken : Active Directory Time Sync (broken by default)](<http://blogs.dirteam.com/blogs/sanderberkouwer/archive/2010/09/10/active-directory-time-sync-broken-by-default.aspx>)

**Tip:** One of the steps in the article is to configure the time server using the "w32tim" command on your PDC emulator. You can do this via [Group Policy Preferences](<https://www.grouppolicy.biz/2010/03/what-are-group-policy-preferences/>) using the [scheduled task](<http://technet.microsoft.com/en-us/library/cc770904.aspx>) option and then use [Item-Level Targeting](<http://technet.microsoft.com/en-us/library/cc733022.aspx>) to only apply the command to the computer name of your PDC Emulator. By scheduling this command on a regular basis you can ensure that the time zone list of the server gets refreshed to the proper values periodically.