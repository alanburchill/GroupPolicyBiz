---
title: "Disappearing Folder Redirection Issues with Windows 7"
date: 2013-03-25 13:28:00
author: admin
categories: ["Best Practice", "hotfix", "Tip"]
tags: ["Folder Redirection", "Windows 7"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2013/03/image_thumb1.png"
---

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/03/image_thumb1.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/03/image2.png>)Thanks to a [tip off](<https://twitter.com/grouppolicyguy/status/314743287204429825>) from fellow MVP [Darren Mar-Elia](<https://twitter.com/grouppolicyguy>) about fairly common issues with Folder Redirection in Windows 7. In short there is a pretty significant issue in Folder Redirection if configured incorrectly that could result in a loss of data for users. There is a mitigation of this issues however this is broken in Windows 7 Service Pack 1. This [form post](<http://sdmsoftware.com/bugs/interesting-bug-in-grouppolicy-folder-redirection-results-in-lost-data/>) on the SDM Software web site goes into some very specific details about the problem but below I am going to attempt to summaries the problem and fix for the issue so you can get Folder Redirection working more reliably in your organisation"...

### Folder Redirection Problem

You have Windows 7 with folder redirection enabled with the "Move contents to new location" option enabled and you then configure a new UNC path for redirection. This NEW path is simply a variation of the path the server that actually points to the exact same location. e.g. [\\\servername\share](<file://\\\\servername\\share>) to [\\\DFSNAME\Share](<file://\\\\DFSNAME\\Share>) . Then when the computer tries to moves the contents of folder to the new (same) location it deletes what it thinks is the old (same) location and thus the users files are deleted. This is BAD! (I hope you have a recent backup)

### How to prevent the Folder Redirection from deleting files on move

So to prevent this from happening in Windows there is a Group Policy setting called [Verify old and new Folder Redirection targets point to the same share before redirecting](<http://gpsearch.azurewebsites.net/Default.aspx?PolicyID=2673>) that checks if the new and old locations are the same before moving the files. In theory if it detects the source and destination are the same it only move the registry pointer to the new location on the server and leaves all the files in place"... However"... In Windows 7 Service Pack 1 this option is broken".... BOTHER!!! **Side Note:** As pointed out in the forum post it is CRAZY that this is NOT the default behaviour as if you do not configure this option you could inadvertently delete user data. So"... Even if this problem does not affect you I would still be seriously be considering enabling this option for your environment.

### How to fix the Verify Old and New Folder redirection option

Thankfully earlier this month Microsoft released a KB that fixes this issue <https://support.microsoft.com/kb/2799904> . So you can now implement Folder Redirection in your environment configured in a way that will not result in a loss of data".... Phew"... So what does all this mean"... ? 1\. If you have folder redirection enable, it is (in my opinion) MANDATORY to enable the [Verify old and new Folder Redirection targets point to the same share before redirecting](<http://gpsearch.azurewebsites.net/Default.aspx?PolicyID=2673>) option to prevent the possibility of losing user data. Thanks again to Darren for the tip... and I hope this helps in your environment in avoiding the issues with using folder redirection. 2\. But you also need to apply [KB2799904](<https://support.microsoft.com/kb/2799904>) to fix the Verify Old and New Folder Redirection Target option if you are running Windows 7 Service Pack 1