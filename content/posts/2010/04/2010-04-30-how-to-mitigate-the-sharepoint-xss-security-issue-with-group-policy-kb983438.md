---
title: "How to mitigate the SharePoint XSS security issue with Group Policy - KB983438"
date: 2010-04-30 05:11:13
author: admin
categories: ["Security"]
tags: ["Basic", "IE8", "Internet Explorer", "KB983438", "SharePoint", "XSS"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/04/image_thumb15.png"
---

There is currently a Cross Site Scripting issue with SharePoint 3.0 and 2007 which could allow someone to maliciously run an arbitrary script that could allow elevation of privilege in the SharePoint site. There is currently no hotfix out for this issues however you can mitigate this issue by enabling the [XSS Filter in Internet Explorer 8](<http://blogs.msdn.com/ie/archive/2008/07/02/ie8-security-part-iv-the-xss-filter.aspx>). Unfortunately this is not turned on by default for the Intranet Zone which is how the majority of SharePoint sites are accessed. So if you are an IT administrator and you want to protect against this issue before Microsoft releases a hotfix then below are the instruction showing how to enable this via Group Policy.

**Step 1.** Edit the Group Policy object that applies to all the user accounts you want to migrate this issue.

**Note:** If you want complete coverage of all users in your organisation then make this change the the default domain policy or another policy link to the top of the domain.

**Step 2.** Navigate to User Configuration > Windows Components > Internet Explorer > Internet Control Panel > Security Page > Intranet Zone and enabled the "Turn on Cross-Site Scripting (XSS) Filter" then ensure you set the drop down menu to "Enabled" then press OK.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/04/image_thumb15.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/04/image22.png>)

To confirm the setting is applied you should now see that the "Enable XSS filter" option is configured to "Enabled" and it is greyed out as the setting has now been configured by group policy.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/04/image_thumb16.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/04/image23.png>)

Unfortunately this setting cannot be enabled via Group Policy Preferences as you can see if does not have the XSS filter option.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/04/image_thumb17.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/04/image25.png>)

To keep up to date with this issue and for more information on this issues see <http://blogs.technet.com/msrc/archive/2010/04/29/security-advisory-983438-released.aspx> and <http://www.microsoft.com/technet/security/advisory/983438.mspx>