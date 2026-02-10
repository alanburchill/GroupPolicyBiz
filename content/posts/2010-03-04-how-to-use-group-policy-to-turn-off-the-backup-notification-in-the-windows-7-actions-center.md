---
title: "How to use Group Policy to turn off the Backup Notification in the Windows 7 Actions Center"
date: 2010-03-04 02:23:23
author: admin
categories: ["Tutorials"]
tags: ["Action Center", "Advanced", "Backup", "Notification", "Popular"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb28.png"
---

**UPDATE: Since I published this article Microsoft published an new[MSDN article ](<http://msdn.microsoft.com/en-us/library/bb891959\(VS.85\).aspx>)showing a simple registry key that can turn this backup notification. Therefore please go to this article "**[**How to use Group Policy to turn off Backup Notification in the Windows 7 Action Center "“ The Easier Way**](<https://www.grouppolicy.biz/2010/06/how-to-use-group-policy-to-turn-off-backup-notification-in-the-windows-7-action-center-the-easier-way/> "Permanent Link to How to use Group Policy to turn off Backup Notification in the Windows 7 Action Center "“ The Easier Way")**. " for the best way to turn off this notification.**

One of the new features in Windows 7 is called the Action Center which is now you one stop shop for all system notifications to the users. One of the alerts that you will get by default out of the box with Windows 7 is the "Set Up Backup" Maintenance notice (see below).

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb28.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image28.png>)

For home PC's this is really important that this message be displayed as the data on the hard drive is usually the only copy. However in an networking environment a users should be configured with roaming profiles, redirections folders and a home drive to ensure all their personal data is store safely on a file servers. Therefore you dont really need to remind them to back up their PC's so you probably don't want them to get messages asking them to configure their backups.




The Action Center icon can be entirely removed from the Notification Area using the "Remove the Action Center icon" native group policy.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb29.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image29.png>)

However this is a bit extreme as you may still want to enable this feature for other notification such as windows updates or if you have an out of date anti-virus definition. So the problem is there is no native way to use Group Policy to enable/disable specific notification events such as the backup notifications.

That's ok"... Thanks to the power of Group Policy Preferences and some help from the people on the [Microsoft support forums](<http://social.technet.microsoft.com/Forums/en-US/w7itproui/thread/83dc3de6-70b7-450f-992c-60511e4a6c4f>) I have figured out a way to control this via Group Policy.

Normally I will step you through the process of creating the Group Policy Preferences manually and then I sometimes provide you with the XML file that is already preconfigured with the settings. However in this case the value is a complicated Binary string that would be very hard to type out manually so I am just providing the preconfigured XML file for you. As this is an XML file feel free to open up with notepad and inspect the file before you apply it to your own systems.

**Step 1.** Edit a Group Policy Object (GPO) that is targeted to the users that you want to disabled the backup notification.

**Step 2.** Navigate to User Configuration > Preferences > Windows Settings > Registry

**Step 3.** Download the file below and then drag (or copy/paste) it into the pane on the right.

Now you are pretty much done and you should then see something like this (Image below).

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb30.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image30.png>)

Now the user should no longer get any backup notifications in the Action Center or in the Notification Icon.

**Note:** User will need to log off and on again for it to become affective.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb31.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image31.png>)

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb32.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image32.png>)

(Sorry"... no fix for the virus notification as you really need to install some sort of AV software)




### More Information

This first item in the list will disable the Backup Notification in the Action Center and the second one will enabled it. Notice however how the second one is greyed out as it is disabled by default. These settings are also configured to "Apply once and do not reapply" as this may be some you want to enabled/disable manually on some computers. I have also put a description in each setting to keep track of what each setting does.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb33.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image33.png>)

If you want to re-enabled the Backup Notification setting for all your users then highlight the enabled item and click on "disabled" in the toolbar.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb34.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image34.png>)

Then highlight the original disabled item and click "enabled" in the tool bar.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb35.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image35.png>)

It should then appear like this"...

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb36.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image36.png>)

### Registry Key Details

In case you were wondering I have put in the partial details of the registry key that control the backup notification however the value are WAY to long to fit in this page so the Data has been truncated (A LOT).

**Key:** HKCU\Software\Microsoft\Windows\CurrentVersion\Action Center\Checks\\{01979c6a-42fa-414c-b8aa-eee2c8202018}.check.100
**Value:** CheckSetting
**Type:** REG_BINARY
**Data Enabled:** 1 (REG_DWORD) = Enabled
**Data Disabled:** 01000000D08C9DDF0115D1118C7A00C04".... (Way to long to fit in here)
**Data Enabled:** 23004100430042006C006F0062000000000".... (Way to long to fit in here)