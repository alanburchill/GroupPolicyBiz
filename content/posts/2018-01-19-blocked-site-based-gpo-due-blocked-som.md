---
title: "Blocked Site Based GPO due to Blocked SOM"
date: 2018-01-19 03:58:51
author: admin
categories: ["Tip", "Tutorials"]
tags: ["Intermediate", "sites"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2018/01/BlockedSOM-800x424.png"
---

I recently came across a problem with applying a site linked GPO to some Citrix servers that were giving Blocked SOM (see below) as the reason for being denied. For the longest time I could not figure out why the GPO was being blocked. It was then with some help that I found out that the computer was in an OU that had blocked Inheritance enabled. This meant that Windows also blocked site link GPO if the computer is in an OU with inheritance blocked. ![](https://www.grouppolicy.biz/wp-content/uploads/2018/01/BlockedSOM-800x424.png)****____This behaviour was confusing to me as Site Based GPO on the surface seem to have nothing to do with OU's. But this behaviour is exactly as designed due to the order or precedents that GPO are applied (Local, Site, Domain then OU). As the OU based policy settings take precedence over the Site this also means that OU based blocking will take precedence over Site based GPO as well. So if you come across this same problem there a number of way that you can work around this problem:

  1. The obvious, and remove the the Blocked Inheritance on the OU that the computer object is located.
  2. Link the Site based GPO to an OU below the Blocked Inheritance. If you do this you lose the ability to dynamically apply the setting based on the site that the computer is located which then defeats the purpose of having the GPO linked at the site. But if it is something like a Citrix server, then you'll be able to create a Site based OU (e.g. PAW\_SiteName_) and then you can link the GPO to the _SiteName_ OU.
  3. You can enabled the "Enforced" option to ignore the "Blocked Inheritance" option.
  4. If it is a Group Policy Preference then you can also use the Item Level Targeting to apply the policy only when the computer is in the correct IP address range and/or Site (see below).

![](https://www.grouppolicy.biz/wp-content/uploads/2018/01/SiteBasedGPO-1.png)****____Reference for Order of Precedence:<https://blogs.technet.microsoft.com/musings_of_a_technical_tam/2012/02/15/group-policy-basics-part-2-understanding-which-gpos-to-apply/> Thanks to [Darren Mar-Elia](<https://twitter.com/grouppolicyguy>) for helping me figure this one out...