---
title: "How to reset a Roaming Profile in Windows 7"
date: 2011-07-14 09:00:00
author: admin
categories: ["Best Practice", "Tutorials"]
tags: ["Intermediate", "Profile", "roaming profile"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2011/07/image_thumb15.png"
---

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/07/image_thumb15.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/07/image14.png>)If you have are one of the many people who have checked out my [Best Practice: Roaming Profiles and Folder Redirection (a.k.a. User State Virtualization)](<https://www.grouppolicy.biz/2010/08/best-practice-roaming-profiles-and-folder-redirection-a-k-a-user-virtualization/> "https://www.grouppolicy.biz/2010/08/best-practice-roaming-profiles-and-folder-redirection-a-k-a-user-virtualization/") post you probably know that roaming profiles can be super useful feature to implement. However over the years roaming profiles have got a bit of a bad wrap as sometime things can and do go wrong. In these case the IT administrator is usually left with no other option than to reset the users profile to solve a issue with their account.

**Tip:** Make sure that the issue is related to the users roaming profile by testing another account with the same or similar privileges on the same computer. If the other computer account also has the same issues or if the issues seems to does not follow them to other computers then it is highly unlikely it is a roaming profile issue.

So lets assume you have troubleshoot this issue for many hours and you are at your wits end about to rip out your hair (if you have any) and have decided to reset the users profile"... how do you do it?

In Windows XP days you could just delete the users local and roaming profile files and the next time the user logged on they would generate a new profile. However if you do this in Windows 7 you will find that this no longer works"...

### So what is the correct way to reset a roaming profile in Windows 7?

Step 1. Open Active Directory Users and Computers and to the profile tab of the user account you want to reset. Now take note of the roaming profile path"....

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/07/image_thumb16.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/07/image15.png>)

Step 2. Reboot the users computer that is having issues and logon with an account that has local admin and is NOT the account you are tyring to fix.

Step 3. Open control panel and type "Advanced" in the search field then click on "View advanced system settings"

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/07/image_thumb17.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/07/image16.png>)

Step 4. Click on the "Advanced" tab and under User Profiles click the "Settings" button

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/07/image_thumb18.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/07/image17.png>)

Step 5. Now select the user you want to reset the profile and press the "Delete" button.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/07/image_thumb19.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/07/image18.png>)

Step 6. Press "Yes"

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/07/image_thumb20.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/07/image19.png>)

And now the local copy of the roaming profile is deleted you also need to remove the network copy"...

**Note:** If you have implemented folder redirection as per my [Best Practice: Roaming Profiles and Folder Redirection (a.k.a. User State Virtualization)](<https://www.grouppolicy.biz/2010/08/best-practice-roaming-profiles-and-folder-redirection-a-k-a-user-virtualization/> "https://www.grouppolicy.biz/2010/08/best-practice-roaming-profiles-and-folder-redirection-a-k-a-user-virtualization/") then the vast majority of the users information will not be part of the users roaming profile. This means other than a few program setting the users is unlikely to lose any work. The exception to this is the AppData folder however if you are trying to preserve this folder as well note you may be copying over the issues that are trying to fix.

WARNING: Always be careful you have everything backed up before deleting any users profile.

Step 7. Before you log off that computer go to the path you noted in step 1 and delete (or rename) the roaming profile for that users on the network.

**Note:** You many need to take ownership of the folder before it can be deleted.

**Tip:** To avoid having to take owner ship of the roaming profile be sure you have enabled the [Add the Administrator security group to roaming users profiles](<https://www.grouppolicy.biz/2010/02/group-policy-setting-of-the-week-15-add-the-administrator-security-group-to-roaming-users-profiles/> "https://www.grouppolicy.biz/2010/02/group-policy-setting-of-the-week-15-add-the-administrator-security-group-to-roaming-users-profiles/") setting.

### How to fix the "You have been logged on with a temporary profile" issue in Windows 7

So"... that was the easy way"... But what do you do if just deleted the users profile files and now the users is "logged on with temporary profile" like you did back in the Windows XP days"....

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/07/image_thumb21.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/07/image20.png>)

Step 1. Reboot the computer again and logon as the local admin.

Step 2. Open Regedit and go following registry key path:

> HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/07/image_thumb22.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/07/image21.png>)

Step 3. Find the Profile that has the ProfileImagePath of the users you are fixing and delete that entire key.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/07/image_thumb23.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/07/image22.png>)

Step 4. Log off and logon as the user you are trying to fix.

**TIP:** If this is successful make sure you get the use to log off straight away so the new profile is save to the network which will then propagate to any other computer when then log on.

Hopefully this will have fixed your roaming profile issues and the users is now back up and running with a minimum of fuss"... Of course some of the users personal settings may have been lost but hopefully a well managed SOE should allow them to run all the essential programs with little to no additional set up.

**Source:** I found the registry key trick from this TechNet Forum article <http://social.technet.microsoft.com/Forums/en-US/w7itprogeneral/thread/5ec0b949-effa-4e30-ba09-dc948a4c7a8b>