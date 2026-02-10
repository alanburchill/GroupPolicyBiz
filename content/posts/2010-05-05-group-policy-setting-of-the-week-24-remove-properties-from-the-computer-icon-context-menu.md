---
title: "Group Policy Setting of the Week 24 &ndash; Remove Properties from the Computer icon context menu"
date: 2010-05-05 06:26:19
author: admin
categories: ["Setting of the Week"]
tags: ["Group Policy", "RSAT", "Support Tools", "Windows"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/05/image_thumb.png"
---

Sorry that this weeks setting of the week was a little late however [as you can see I have been a little busy](<https://www.grouppolicy.biz/2010/04/introducing/>).

This weeks setting is called "Remote Properties from the Computer icon context menu" and can be found under User Configuration > Policies > Administrative Templates > Desktop. This setting might seem a little mundane compared some other setting however it could be very useful if you are in an environment where many of your users have admin access to their computers. Enabling this setting makes it much more difficult for users to remove their computer from the domain which they might want to do because of those pesky restrictive group policies. ;)

**Note:** If you do enabled this option be sure not to apply it to specific IT staff so that they can still manage the computer account. You could do this by using using the Deny "Apply Group Policy" of the Advanced security setting of the policy.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/05/image_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/05/image.png>)

Setting Enabled on Windows 7

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/05/image_thumb4.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/05/image4.png>)

Setting Enabled on Windows XP

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/05/image_thumb2.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/05/image2.png>)

Note that this does not prevent users from removing the computer from the domain as all you are doing is disabling the System Properties dialogue box that has the computer name tab (see image below) where domain membership is normally configured. While just disabling the UI is not a 100% effective it should at least stumble most users from changing this setting.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/05/image_thumb3.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/05/image3.png>)

In case you were wondering, a user with admin access to their computer could still install either the [Windows XP Support tools](<http://www.microsoft.com/downloads/details.aspx?FamilyID=49ae8576-9bb9-4126-9761-ba8011fabf38&displayLang=en>) or the [Remote Server Admin Tools (RSAT)](<http://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=7d2f6ad7-656b-4313-a005-4e344e43997d>) to use the [NETDOM JOIN](<http://technet.microsoft.com/en-us/library/cc788049\(WS.10\).aspx>) and [NETDOM REMOVE](<http://technet.microsoft.com/en-us/library/cc788074\(WS.10\).aspx>) commands to change the computer domain membership.