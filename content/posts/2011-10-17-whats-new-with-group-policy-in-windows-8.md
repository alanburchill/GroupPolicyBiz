---
title: "Updated: What&rsquo;s new with Group Policy in Windows 8"
date: 2011-10-17 09:11:55
author: admin
categories: ["News"]
tags: ["Group Policy", "Windows 8"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2011/10/image_thumb2.png"
---

The Windows Developer Preview version of Windows Server 8 has been on MSDN now for a while therefore I setup a Domain Controller and found some very interesting new Group Policy features lurking"...

### Group Policy Infrastructure Status

If you click on the domain name in GPMC you will notice there is a new tab called "Infra Status". As the page says "The page shows the status of Active Directory and Sysvol (DFSR) replication for this domain as it relates to Group Policy". This will obviously be a great troubleshooting tool for Group Policy settings that are not applying to the computers in your organisation due to AD replication issues.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/10/image_thumb2.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/10/image2.png>)

### Group Policy Update

If you right click on any OU in you AD you will see a new menu option called "Group Policy Update"...".

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/10/image_thumb3.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/10/image3.png>)

Clicking on this option with an OU with no computers in it gives you an interesting explanation of the feature.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/10/image_thumb4.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/10/image4.png>)

> You have chose to force a Group Policy update on all computers within Workstations and all sub containers.

What is particularly interesting is the text "FORCE A GROUP POLICY UPDATE" meaning that you can now force the group policy update to all computers in a Organisations Unit. This would effectively mean that administrators can now make changes to their computers without having to wait the default 90 minutes to wait for group policy to refresh on a computer.

~~After trying to make the option work by populating the OU with a few computer accounts I simply got the same message again and again. I can only assume that this is a feature that has yet to be implement in this build"...~~

I have been able to get the wizard to working by building a real Windows 8 computer and added to the "Workstations" OU.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/10/image_thumb9.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/10/image9.png>)

After click yes it has found the "real" computers in the OU and forces a Group Policy update to run within two minutes on these computer.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/10/image_thumb10.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/10/image10.png>)

Seeing the task was scheduled I then took a look at the scheduled tasks on the computer being targeted and found that it had created two scheduled tasks to perform a gpupdate in the user and computer context.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/10/image_thumb11.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/10/image11.png>)

**Note:** You will need to configure the client firewall on the workstations being targeted to allow these command to be created"... More info coming on that"...

So I have also found that the UI for the Internet Explorer Group Policy Preference has been updated to include IE8 and IE9 (see image below). This support would have been nice update to the hotfix that was just released for windows 7 to support Internet Explorer 9 (see [Hotfix: Internet Explorer Group Policy Preferences do not apply to Internet Explorer 9](<https://www.grouppolicy.biz/2011/10/hotfix-internet-explorer-group-policy-preferences-do-not-apply-to-internet-explorer-9/>))

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/10/image_thumb12.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/10/image12.png>)

~~I have not found anything else in this build that is Group Policy related but~~ I will keep digging"... But it is great to see that Redmond is still adding improvements to Group Policy with the latest version of Windows.