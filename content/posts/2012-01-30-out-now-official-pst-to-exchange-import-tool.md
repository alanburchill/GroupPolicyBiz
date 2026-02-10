---
title: "Out Now: Official PST to Exchange Import Tool"
date: 2012-01-30 22:57:07
author: admin
categories: ["News", "Tip"]
tags: ["Exchange", "Group Policy", "Import", "PST", "Tool"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2012/01/image_thumb6.png"
---

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/01/image_thumb6.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/01/image6.png>)If you have ever had anything to do with Outlook in your organisation you will no doubt have some experience (pain) with the use of PST files. PST files are of course the main way users can store their email information on their local hard drive or network share ([Network stored PST files don't do it](<http://blogs.technet.com/b/askperf/archive/2007/01/21/network-stored-pst-files-don-t-do-it.aspx> "http://blogs.technet.com/b/askperf/archive/2007/01/21/network-stored-pst-files-don-t-do-it.aspx")) thus avoiding the email mailbox size limits. Of course PST files have many problem and pose a nightmare for network admins when someone says they have either lost a PST file or worse it gets corrupt. While it is really easy for people to say lets just ban all PST files the reality of this is a lot more difficult"...

With the new Archives feature in Exchange 2010 and its support for lower cost storage this has started to allow users to have bigger mailboxes. Office 365 even gives users a default mailbox size of 25gb (up to unlimited) depending on the plan the user it signed up for. Problem is that users could still have PST files even thought they might now have plenty of space in their mailbox"...

Well Microsoft has [just announced](<http://blogs.technet.com/b/exchange/archive/2012/01/30/pst-time-to-walk-the-plank.aspx>) they have released a tool that allow admins to automatically crawl users computers and import PST files into Exchange Online or Exchange 2010.

Download [http://www.microsoft.com/download/en/details.aspx?displaylang=en&id=28767](<http://www.microsoft.com/download/en/details.aspx?displaylang=en&id=28767> "http://www.microsoft.com/download/en/details.aspx?displaylang=en&id=28767")

So you might be wondering what this has to do with Group Policy"... well"... once you have completed the migration of the PST files you can then implement the [Prevent users from adding new content to existing pst files](<http://gps.cloudapp.net/Default.aspx?PolicyID=6314>) policy setting to stop users ever, ever, ever, ever using PST file again"....