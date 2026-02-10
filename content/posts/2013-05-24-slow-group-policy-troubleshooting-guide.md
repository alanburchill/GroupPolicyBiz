---
title: "Slow Group Policy Troubleshooting Guide"
date: 2013-05-24 04:03:07
author: admin
categories: ["Tip"]
tags: ["Performance", "TechNet"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2013/05/clock_thumb.jpg"
---

[![clock](https://www.grouppolicy.biz/wp-content/uploads/2013/05/clock_thumb.jpg)](<https://www.grouppolicy.biz/wp-content/uploads/2013/05/clock.jpg>)Ever wondered why the computers in your organisation are so slow? Well [Darren Mar-Elia](<http://twitter.com/grouppolicyguy>) has just posted an extensive article on TechNet called [Group Policy and Logon Impact](<http://blogs.technet.com/b/grouppolicy/archive/2013/05/23/group-policy-and-logon-impact.aspx>). His blog goes into great detail explaining many of the pit fall's IT Admins can do that cause large impact to logon speed and group policy processing.

The summary tips of the actions are as follows:

  * Avoid synchronous CSEs and don't force synchronous policy, or if CSE usage is necessary, minimize changes to these policies.
  * Avoid costly WMI filters such as LDAP queries.
  * Look for costly scripts by running them in isolation, and work to improve the scripts' performance or avoid these scripts.
  * Don't run ITL evaluations such as OU, LDAP Query, Domain, Site, or Computer Security Groups.
    * If you need to use security group filters, consider this [KB article](<http://support.microsoft.com/kb/2561285/en-us>).
  * Don't use "Replace" with Group Policy Preferences Printers.
  * Disable synchronous logins when on a slow link.


For full context on each of these actions I recommend you a full read of the article at: <http://blogs.technet.com/b/grouppolicy/archive/2013/05/23/group-policy-and-logon-impact.aspx>