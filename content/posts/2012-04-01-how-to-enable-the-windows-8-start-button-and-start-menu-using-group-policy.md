---
title: "Updated: How to enable the Windows 8 Start Button and Start Menu using Group Policy"
date: 2012-04-01 02:31:34
author: admin
categories: ["Funny"]
tags: ["Start Button", "start menu", "Windows 8"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2012/04/image_thumb.png"
---

**Update:** In case you did not realise".... This is an April Fools".... @slooflirpa is @aprilfools backwards"...

Thanks to a tip off via twitter from [@slooflirpa](<http://twitter.com/slooflirpa>) I have discovered some hidden Group Policy setting in the Windows Server 8 Beta that configures that restores the start button and optionally the traditional start menu in Windows 8. Even thought there have been some reports that the Windows 8 start button is not coming back (see ["Microsoft will not be adding back the Start Button"](<http://seattletimes.nwsource.com/html/microsoftpri0/2017873245_nomura_on_windows_8_microsoft_will_not_be_adding_b.html> "http://seattletimes.nwsource.com/html/microsoftpri0/2017873245_nomura_on_windows_8_microsoft_will_not_be_adding_b.html") ) it seems there is code still in from the developer preview and it allows IT administrators to restore the setting via Group Policy. Seems that this is a concession that is being made from corporation and not consumers as the same policy setting are not present in the local Group Policy ADMX files. The two particular Group Policy setting that I have found are called "Force Start Menu" and "Add Start Button to the task bar" and can be found under both users and computer Administrative Templates>Start Menu and Desktop.

What is also very interesting there is the "Force Start Menu" button option also disabled the ability to run an WinRT (a.k.a. Metro) style apps presumably as there is not way to launch these apps without the metro start menu.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/04/image_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/04/image.png>)

[![windows_8_start_menu_toggle](https://www.grouppolicy.biz/wp-content/uploads/2012/04/windows_8_start_menu_toggle.jpg)](<http://www.winsupersite.com/article/windows8/tip-improve-windows-8-party-utilities-140692>)

This is certainly a welcome relief for all those Enterprises out there that have been asking for a way to restore the more traditional UI to ease the learning curve for their user when upgrading to Windows 8.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/04/image_thumb1.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/04/image1.png>)

[![win8_tp_0022](https://www.grouppolicy.biz/wp-content/uploads/2012/04/win8_tp_0022.jpg)](<http://www.winsupersite.com/article/windows8/windows-8-developer-preview-screenshots-part-2-140549>)

To view these setting for your self you will need to make sure you to change the Managed file to No under the Filter Option the the Group Policy Editor.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/04/image_thumb2.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/04/image2.png>)

Of course there is no telling if Microsoft will keep theses setting in Windows 8 for the final version but for now users can at least run for now.

This article is bound to produce a lot of comments so please ensure that you mind what you say to not "[offend](<http://en.wikipedia.org/wiki/Aprilfools>)" other readers"...