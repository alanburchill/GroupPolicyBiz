---
title: "Group Policy Caching in Windows 8.1"
date: 2013-07-03 23:40:21
author: admin
categories: ["News"]
tags: ["Group Policy Caching", "Windows 8.1"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2013/07/clock_thumb.jpg"
---

[![clock](https://www.grouppolicy.biz/wp-content/uploads/2013/07/clock_thumb.jpg)](<https://www.grouppolicy.biz/wp-content/uploads/2013/07/clock.jpg>)Another new feature of Group Policy in Windows 8.1 is the ability for it to now cache Group Policy to improve performance when processing synchronous policy settings. Now before you say Windows 8 already starts [REALLY FAST](<http://blogs.msdn.com/b/b8/archive/2011/09/08/delivering-fast-boot-times-in-windows-8.aspx>) how can this make it any faster, this caching only really kicks in some very specific fringe cases. Specifically it improves performance when you computer is connected via a high latency link (e.g. WAN) to the domain controller.

To under stand how much of improvement this will give you need to be aware that each GPO download from the domain controller required 5 LDAP queries all of which have to happen in serial. This means if you have one GPO on a 200ms latency WAN link then a single GPO will take about 1 second to download and process. BUT"... If you have a LOT of GPO's in your organisation, say 200. This will be 1 seconds x 200 GPO's meaning it will give you over a 3 minute delay at logon.

**Tip:** This is why it is always a good idea to try to keep the number of GPO's you have apply to your computers to a reasonable number.

As I mentioned before this slow logon is a bit of a fringe case and unless your network is initialised while the computer is starting (e.g. Wired LAN or Enterprise WiFi) you are not likely to see this issue. But for those who are affected, this can represent a significant saving in logon speed performance when computers start up after you next change a GPO with a synchronous policy setting.

In case you were wondering the only policy setting that are now synchronous in Windows 8.1 are Software Installation and Folder Redirection. Previously Drive Mappings and Disk Quotas were sync settings but they have not been made async meaning they can apply in the background.

For a more in-depth look at this feature also check out [Darren Mar-Eila](<https://twitter.com/grouppolicyguy>) blog post at <http://sdmsoftware.com/group-policy-blog/group-policy/understanding-group-policy-caching-in-windows-8-1/>