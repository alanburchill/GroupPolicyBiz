---
title: "Group Policy Setting of the Week 28 &ndash; Maximum wait time for Group Policy scripts"
date: 2010-06-08 02:00:00
author: admin
categories: ["Setting of the Week"]
tags: ["Basic", "Group Policy", "logon", "scripts"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/06/image_thumb11.png"
---

This weeks Group Policy setting should be used in environments where you still use a logon script. While I implore you stop using logon scripts (see <http://www.ihatelogonscripts.com> ) they are still out there for a majority of customers and as such still need to be properly managed. This setting is called "Maximum wait time for Group Policy scripts" but it can also be referred to as a "[dead man's switch](<http://en.wikipedia.org/wiki/Dead_man_switch>)" which will kill any logons script from running if it ever locks up <sarcasm> which of course NEVER happens </sarcasm> . This setting can be found under Computer Configuration > Policies > Administrative Templates > System >Scripts.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/06/image_thumb11.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/06/image11.png>)

The default value for this option is 600 seconds (10 minutes) but I recommend that you do configured this to something more reasonable between 60 seconds (1 minute) to 180 seconds (3 minutes) depending on your environment.

For more information on this option check out <http://technet.microsoft.com/en-us/library/cc780635(WS.10).aspx>