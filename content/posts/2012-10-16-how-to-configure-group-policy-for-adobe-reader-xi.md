---
title: "How to configure Group Policy for Adobe Reader XI"
date: 2012-10-16 00:26:12
author: admin
categories: ["Tutorials"]
tags: ["adobe", "adobe reader", "Adober Reader XI", "Beginner"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2012/10/reader_128_thumb1.jpg"
---

[![reader_128](https://www.grouppolicy.biz/wp-content/uploads/2012/10/reader_128_thumb1.jpg)](<https://www.grouppolicy.biz/wp-content/uploads/2012/10/reader_1281.jpg>)The next version Adobe has just [released](<http://get.adobe.com/reader/>) the latest version Acrobat Reader XI. One of the new features of this version is that it now has official group policy support with the release of administrator templates.

**Update:** As you are about to read the Group Policy support for now is some what limited and is not a true group policy setting in all cases. BUT"... If you want to be able to truly lock down and configure Adobe Reader in your environment then I would definitely check out the third party tool called Policy Pak. This tool allows you to configure and lock down the UI of a vast number of applications including Adobe Reader but also in house written custom applications. If you want to find out more about how to configure Adobe Reader with Policy Pak then go to <http://www.policypak.com/products/manage-acrobat-reader-with-group-policy.html>

### How to install administrative templates for Adobe Reader XI

Step 1. Download and extract the administrative templates from <ftp://ftp.adobe.com/pub/adobe/reader/win/11.x/11.0.00/misc/ReaderADMTemplate.zip>

Step 2a (Local adm/admx). Copy the extracted files to C:\Windows\PolicyDefinitions including the "EN-US" sub folder folder on your computer you normally edit your GPO's on.

Step 2 b(Central Store). If you have a [central store configured](<http://support.microsoft.com/kb/929841/en-gb>) in your environment then copy the files to \\\FQDN DOMAIN\SYSVOL\FQDN DOMAIN\policies folder.

And your done..

Once installed you can see below there are both computer and users based setting in the administrator templates when you edit a new GPO.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/10/image10_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/10/image10.png>)[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/10/image_thumb5.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/10/image6.png>)

As you can see below the computer settings are actual "policy" settings and as such do act and behave as normal group policy settings. That is they disable the UI of the program when applied and revert back to the original setting when removed.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/10/image_thumb1.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/10/image1.png>)

Below is an example of the "Auto-Complete" UI that has been disabled as shown configured above.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/10/image_thumb2.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/10/image2.png>)

If you have ever read my previous blog post [How to make Adobe Reader more secure using Group Policy](<https://www.grouppolicy.biz/2010/06/updated-how-to-make-adobe-reader-more-secure-using-group-policy/>) you will know that one of the quickest settings you can do to improve the security of Reader is to simply turn off the rarely used JavaScript functionality. Thankfully this is one of the users settings that is provided in the admin template.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/10/image_thumb3.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/10/image3.png>)

But as this is a "Non-Managed" as shown by the black down arrow on the icon next to the setting. This also means that the users can temporarily override the setting as you can see below the UI is not disabled. It also means that when the policy is no longer applied to the computer the setting will not revert back to the original setting.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/10/image_thumb4.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/10/image5.png>)

While it is nice that Adobe is finally offering group policy support for its productions the settings that it does provide are somewhat limited. However this is only the first release of the admin templates and hopefully we will see Adobe continue to add more group policy support into all of its production going forward.

### Additional Information

If you want more information about how to deploy Adobe Reader XI in your environment including how to lock down some of UI then check out [Aaron Parkers](<http://www.twitter.com/stealthpuppy>) blog post at <http://blog.stealthpuppy.com/deployment/adobe-reader-xi-deployment/>

### Adobe Reader XI Download Links

Program <ftp://ftp.adobe.com/pub/adobe/reader/win/11.x/11.0.00/en_US/>

Tools <ftp://ftp.adobe.com/pub/adobe/reader/win/11.x/11.0.00/misc/>