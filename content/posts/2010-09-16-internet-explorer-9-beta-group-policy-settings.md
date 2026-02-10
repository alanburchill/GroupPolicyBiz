---
title: "Internet Explorer 9 (Beta) Group Policy Settings"
date: 2010-09-16 01:00:00
author: admin
categories: ["News", "Tutorials"]
tags: ["GPMC", "Group Policy", "Group Policy Prefereces", "IE9", "Intermediate", "Internet Explorer 9"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/09/IE9banner2.jpg"
---

[![IE9-banner2](https://www.grouppolicy.biz/wp-content/uploads/2010/09/IE9banner2.jpg)](<http://www.beautyoftheweb.com/>)

Microsoft has now released to the public ([download it here](<http://www.beautyoftheweb.com/#/download>)) the newest version of Internet Explorer 9 Beta to the public. If you want to know more about the new features in IE9 then i recommend that you check out <http://www.beautyoftheweb.com/> to see some of the fantastic stuff that this browser enables. If the new functionality alone is not enough to get you to use it is just remember that it is now a [Fully Hardware accelerated](<http://blogs.msdn.com/b/ie/archive/2010/09/10/the-architecture-of-full-hardware-acceleration-of-all-web-page-content.aspx>) which makes it much faster than any [other browser](<http://www.smartergeek.info/2010/09/microsoft-shows-off-ie9-hardware-acceleration-beating-the-pants-off-chrome-7/>) on the market!!!

With any new version IE there comes new features and with new features comes new group policy settings so below I go through the new policy settings and how you can get started right now with managing IE9 using Group Policy.

To get started you will need to download and install IE9 on whatever computer you are using Group Policy Management Console (a.k.a. GPMC) to edit your Group Policy settings as with anything to do with Group Policy it is normally best to make changes from a systems that has the newest software on it in your organisation.

**WARNING:** This software is still Beta so you are strongly recommended to isolate any testing you do with IE9 and Group Policy from your production environment.

### Internet Explorer 9 Administrative Template Group Policy Settings

There are only 8 new Admin Template group policy setting but remember that just like previous version most of the other older IE policy settings will still apply to this newer of IE. Theses settings are of course not final and Microsoft could change or added/remove more setting before the product goes RTW.

As IE 9 only supports Windows Vista and Windows 7 you now only get ADMX files for the new policy settings which will automatically get placed into the C:\Windows\PolicyDefenitions folder on the computer you install IE9. **Note:** You will need to upload "inetres" the ADMX and ADML file to the if you are using a admin template [central store](<http://support.microsoft.com/kb/929841>). So once the new ADMX files are loaded you will be able to configured the new IE setting under Administrative Templates in the Group Policy Editor. Sweet!

To save you the time of trying to find where the new policy settings are yourself I have listed the 8 new Administrative Template settings with the location that they can be found so you can check them out yourself.

#### Disable add-on performance notification

Administrative Templates > Windows Components > Internet Explorer

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb8.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image8.png>)

#### Turn off Managing SmartScreen Filter

Administrative Templates > Windows Components > Internet Explorer

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb9.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image9.png>)

#### Allow Internet Explorer 8 Shutdown Behaviour

Administrative Templates > Windows Components > Internet Explorer

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb10.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image10.png>)

#### Automatically enable newly installed add-ons

Administrative Templates > Windows Components > Internet Explorer

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb11.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image11.png>)

#### Prevent Deleting Download History

Administrative Templates > Windows Components > Internet Explorer > Delete Browsing History

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb12.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image12.png>)

#### Enable WebM software (when available)

Administrative Templates > Windows Components > Internet Explorer > Advanced Settings > Multimedia

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb13.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image13.png>)

#### Prevent configuration of search from the Address bar

Administrative Templates > Windows Components > Internet Explorer > Advanced Settings > Searching

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb14.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image14.png>)

#### Install binaries signed by MD2 and MD4 signing technologies

Administrative Templates > Windows Components > Internet Explorer > Security Features > Binary Behaviour Security Restrictions

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb15.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image15.png>)

### Internet Explorer 9 Internet Explorer Maintenance Group Policy

The other way you can configured IE9 with Group policy is by going to Windows Settings > Internet Explorer Maintenance section and as with previous version you can configure you IE setting (e.g. Home Page) or you can Import the current Program and/or Security using the Import Program Setting option.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb16.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image16.png>)

### Internet Explorer 9 Group Policy Preferences Group Policy

Umm"... err"... Unfortunately at this point in time there is no support for Group Policy Preferences with Interne Explorer 9. This may or may not change in the future but at least for now you can use Admin Templates and IE Maintenance mode to keep you going.

As the beta has only just been released then it is highly likely that there will be more information coming soon"... If this does happen I will be sure to post a new article to keep you up to date.