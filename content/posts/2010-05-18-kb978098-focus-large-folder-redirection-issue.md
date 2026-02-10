---
title: "KB978098 Focus: Large &ldquo;Folder Redirection&rdquo; issue"
date: 2010-05-18 05:14:16
author: admin
categories: ["KB Focus"]
tags: ["Folder Redirection", "KB978098"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/05/image_thumb21.png"
---

Microsoft recently released [KB978098](<http://support.microsoft.com/?kbid=978098>) which explains an issues with folder redirection when using the Advanced folder redirection setting (see image below). The advanced setting of this policy is used when you want to redirect users to different locations based on security group location. This is a very helpful if you have a large number of users in the same site and you don't want to store all their redirected folder to the same location similar to how Exchange Administrator distribute users amongst multiple mailbox databases.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/05/image_thumb21.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/05/image20.png>)

**Issue:**

This issues is not with the size of the data in the redirection folder ( as the name might suggest ) but the actual number of security groups you have used in the policy. The good news is that the number of groups you need to have configured before this becomes an issues is A LOT so this is likely only going to affect the large organisations.

Depending on the OS that you are editing the policy on it can change the number of groups you can use to configured before this issues occurs.

Windows Vista or Later = 670 (approx) Security Groups

Windows Server 2003 = 230 (approx) Security Groups

**Problem**

The problem occurs when the the fdeploy(?).ini file under Policies\GUID\User\Documents & Settings folder in the SYSVOL exceeds 32,767 characters due to the large number of GUID's listed in the file (see below).

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/05/image_thumb22.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/05/image21.png>)

**Workaround******

Option 1: The workaround in the KB is to split the Group Policy Object up so that each policy has fewer groups/redirected folders.

Option 2: If you have only edited the policy in Windows XP / 2003 then you can open then Group Policy Object with Windows Vista (or greater) as it will be "converted to a newer "... .ini file format" that "lets you redirect more folders".

**Disclaimer**

This information is to be used at your own risk and make sure you read the KB yourself and you test any changes in thoroughly before making changes in your environment.

Source: [Errors when you have a large "Folder Redirection" policy settings file in Windows Vista, in Windows 7, in Windows Server 2008, or in Windows Server 2008 R2](<http://support.microsoft.com/?kbid=978098>)