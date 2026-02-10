---
title: "Group Policy Setting of the Week 18 - Allow file download (Internet Explorer)"
date: 2010-03-16 10:47:49
author: admin
categories: ["Setting of the Week"]
tags: ["Group Policy", "Internet Explorer", "Security"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb53.png"
---

This weeks setting is one that you would use if you are in an environment that you want a very high level of security (e.g. Kiosk computers). The "Allow file download" option is used to prevent the downloading of files via Internet Explorer. This setting does not prevent the browser form downloading files such as images to display in the browser page but it does prevent users from downloading of files when a user click on a file download link. This could also be useful if you want to help limit the security attack vector of users being tricked into download and running malicious files on their computers from the internet which could help mitigate some [Zero day attacks](<http://en.wikipedia.org/wiki/Zero_day_attack>).

**Note:** This does not prevent users from running Firefox or Chrome to get around this restriction (although they would have difficulty in downloading it) therefore you may also want to consider deploying AppLocker or Software Restriction Policies to prevent the running of those apps.

To enable this restriction you need to first "Enable" the policy and then set the Allow file downloads option to "Disable" . This setting can be found under Configuration > Policies > Administrative Templates > Windows Components > Internet Explorer > Internet Control Panel > Security Page > Internet Zone. This setting can also be configured on the other zone's under the Security Page section however the Internet Zone is what most web sites are classified as and therefore will have the largest affect.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb53.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image53.png>)

When this policy is applied to a user and the user clicks on a hyperlink to a file to download they will then receive this dialogue box.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb54.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image54.png>)

If you did enabled this setting and you wanted to let users download file from particular web sites you could add the site URL to the trusted sites zone list. I have previously blogged how to do here <https://www.grouppolicy.biz/2010/03/how-to-use-group-policy-to-configure-internet-explorer-security-zone-sites/>

P.S. Sorry i am a day late with this one"... have been a bit busy lately. But don't worry i will make sure that i always have time to do a setting of the week post each week.