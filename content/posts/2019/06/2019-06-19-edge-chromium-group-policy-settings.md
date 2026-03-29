---
title: "Edge Chromium Group Policy Settings"
date: 2019-06-19 23:00:17
author: admin
categories: ["News", "Tip"]
tags: ["ADMX", "Chromium", "Group Policy", "IE Enterprise Mode", "Mac", "Windows 7"]
featured_image: "/uploads/2019/06/EdgeGPOSettingSmall.png"
---

For all of its issues, Internet Explorer has been the most prolific Group Policy enabled applications ever released. Even the recent versions of Edge with Windows 10 still does not hold up to the old versions of IE when it comes to sheer number of supported settings. This rightly or wrongly gave Group Policy administrators a near infinite of ways to configure the browser.

However the far more popular browser Chrome from Google also has Group Policy support. So when Microsoft replaced Edge with the Chromium browser a lot IT people started to ask if there would be any similar Group Policy support. As it turns out the answer to this question is YES!

Sean Lyndersay from Microsoft has just [recently posted](<ttps://techcommunity.microsoft.com/t5/Discussions/Early-preview-of-Microsoft-Edge-group-policies/m-p/693929>) about the new policies that are coming with Edge Chromium edition. In the post he also releases a ZIP file that has a ADM and ADMX templates that can be used to implement the new policy settings. To use the file simple download and unzip the file and copy the ADMX/ADML files into your local C:\Windows\PolicyDefinitions folder. Alternativly you could also copy the files into your Active Directory Central Store, however as these are early templates with limited language support you might want to hold off doing that for now.

Once you have done this open the Group Policy Editor on your computer and you will now see there are new setting under both User and Computer "Administrative Templates > Microsoft Edge".

![](http://www.grouppolicy.biz/wp-content/uploads/2019/06/EdgeGPO.png)Microsoft Edge Chromium Group Policy Settings

Note: This is not to be confused with the existing Group Policy settings for the original version of Edge that can be found under "Administrative Templates > Windows Components > Microsoft Edge"

Thankfully most of the Group Policy setting that were previously in Chrome have been preserved. This give his new version of Edge a huge head start when provide policy support. Especially when compared to the original version of Edge that had [servery lacking policy support](<https://www.grouppolicy.biz/2015/07/edge-group-policy-settings/>) with only 10 settings.

The ZIP file provided that has been release is only localized for English US and there are no policy settings to manage the update of browser. The update feature will be a very important addition as many organisation might not yet be used to the rapid 6 week release schedule of Chromium.

Also missing are polices to implement IE Enterprise Site Mode list. This is the feature that Edge currently use that can dictate if a web site is opened in the new Edge engine or using the old legacy IE render engine. Unlike previous version of IE Enterprise Site Mode list the new version will run IE in Edge like a normal tab.

![](http://www.grouppolicy.biz/wp-content/uploads/2019/06/EdgeIEMode-800x372.png)Microsoft Edge Chromium IE Enterprise Mode

"IE mode does not run a separate window. It's not even a separate tab. It's fully integrated into Edge"

Once you configure a setting then you will notice that you will get a "Managed by" section appear at the bottom of your Managed tab. As you can see below it also shows the source of where the policy setting. In my example below it lists the domain name of the Microsoft Account I am signed into on my computer.

![](http://www.grouppolicy.biz/wp-content/uploads/2019/06/EdgeGPO-1.png)How to tell if Edge Chromium is being managed by Group Policy

Then if you then click on this option it will take you to <edge://management> you then get e description of how the browser is being managed.

![](http://www.grouppolicy.biz/wp-content/uploads/2019/06/image-2-800x469.png)Microsoft Edge Management

Finally you can then open <edge://policy> and actually see all the setting that have been applied to the browser (similar to Chrome). This will be a super handy feature for help desk users and they can easily and quickly see what policy setting are being applied.

In the example below I just have SmartScreenEnable set to true.

![](http://www.grouppolicy.biz/wp-content/uploads/2019/06/image-3-800x475.png)Microsoft Edge Chromium Policy Settings

I have been a die hard IE and Edge fan all my life. But the new Edge Chromium browser is certainly a great direction for Microsoft. Now with the inclusion of Group Policy Settings, and the future IE Enterprise Mode it certainly makes it compelling for any corporate to seriously look at making Edge the default corporate browser once it is released.

Its also not just for Windows 10 users as you can now download Edge Chromium for Mac, Windows 7, 8.0, and 8.1 <https://blogs.windows.com/msedgedev/2019/06/19/introducing-microsoft-edge-preview-builds-for-windows-7-windows-8-and-windows-8-1/>

So if you want to give the new policy setting a try then download Edge Chromium from <https://www.microsoftedgeinsider.com/en-us/> and get the zip file <https://techcommunity.microsoft.com/t5/Discussions/Early-preview-of-Microsoft-Edge-group-policies/m-p/693929> today.