---
title: "How to &ldquo;Set users home folder&rdquo; via group policy in Windows 8"
date: 2012-07-09 13:15:00
author: admin
categories: ["Tutorials"]
tags: ["home directory", "home drive", "home folder", "Intermediate", "Windows 8"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2012/07/image_thumb.png"
---

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/07/image_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/07/image.png>)If your company is like most organisation i have come across you all users to have a home drive (typically H: ) that is give to the users that allows them to store private information that only they have access. Ever since the days of at least NT4 (or possibly earlier) administrators have had the option to configure their users home drives via a setting in their AD account (see image below below).

[![nt4lgsc4](https://www.grouppolicy.biz/wp-content/uploads/2012/07/nt4lgsc4_thumb.gif)](<https://www.grouppolicy.biz/wp-content/uploads/2012/07/nt4lgsc4.gif>)

Even today with Windows Server 2012 this is this is still an option for administrators to configured users home drives via their users accounts (see image below).

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/07/image_thumb1.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/07/image1.png>)

When the home drive is set on a user account via Active Directory Users and Computers the tool actually goes out and creates the home drive in ready for the user to map the next time the log onto a computer.

The main problem with configuring users home drive this way is that it is configured on a one by one basis which means that it is difficult to configure these setting and it is another step in the user creation process that can be forgotten to be done. Certainly this is a lot easier with the advent of Windows Server 2003 admin tools that allowed you to select multiple users and configured the home drive on mass.

![](https://www.grouppolicy.biz/wp-content/uploads/2010/08/image49.png)

However the idea of setting the home drive as an individual attribute in todays policy driven, economy of scale management style is just not ideal. Such as a user account is moved from one location to another in AD the users home drive setting is not automatically updated as its a static configuration on the users account.

If you have read my blog post [Best Practice: Roaming Profiles and Folder Redirection (a.k.a. User State Virtualization)](<https://www.grouppolicy.biz/2010/08/best-practice-roaming-profiles-and-folder-redirection-a-k-a-user-virtualization/>) you might have realised that you can already create the users home drive automatically using folder redirection (specifically Documents) and then you can simply use the Group Policy Preferences [Drive Mapping Extension](<http://technet.microsoft.com/en-us/library/cc731729.aspx>) to map the user home drive to the same location as the folder is redirected. This method does allow for the users account to moved around and have policy automatically update their home drive. But in reality it is just a workaround to the lack of any other way of setting the users home drive automatically via policy"... until now..

With the introduction of Windows 8 and Windows Server 2012 there is now a new group policy setting called "Set user home folder" and is found under Computer Configuration > Policies > Administrative Templates > System > User Profiles.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/07/image_thumb2.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/07/image2.png>)

One the policy is applied to a computer anyone logos onto this computer will get a home drive mapped to the path above"...

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/07/image_thumb3.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/07/image3.png>)

**Warning:** As this policy can only be applied to the computer object this will apply to everyone who logs on the computer that have this setting applied"... including Domain admins and alike so be carefully how you apply it"...

**TIP:** If you have your workstations segmented in your OU structure by site you may want to apply this policy setting at each site to the nearest file server you want to use for storing your home drives. This means that users will not have home drive re-map if they travel for a short time to other locations"... Alternately you MIGHT want to apply this setting to your AD site however if you do this make sure you put a WMI filter on the policy so it does not apply to Windows Servers in the same site.. .