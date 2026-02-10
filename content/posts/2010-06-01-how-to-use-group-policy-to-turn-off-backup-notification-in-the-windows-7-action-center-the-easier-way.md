---
title: "How to use Group Policy to turn off Backup Notification in the Windows 7 Action Center &ndash; The Easier Way"
date: 2010-06-01 04:07:00
author: admin
categories: ["Best Practice", "Tutorials"]
tags: ["Action Center", "Backup", "Intermediate", "Set up Backup"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/06/image_thumb.png"
---

In this article I have will show you how to turn off the Backup Notification message in eh Windows 7 Action Center. I have previously blogged about how to do this using Group Policy Preferences here ([How to use Group Policy to turn off the Backup Notification in the Windows 7 Actions Center](<https://www.grouppolicy.biz/2010/03/how-to-use-group-policy-to-turn-off-the-backup-notification-in-the-windows-7-actions-center/>)) however since writing this post Microsoft has come out with a [new MSDN article](<http://msdn.microsoft.com/en-us/library/bb891959\(VS.85\).aspx>) explaining how to do this using a much simpler registry keys.

So as the first version of this article was my most popular post by far I thought it would be prudent to show people how to turn this notification off the now easier way.




In my previous post we were able to disable the Action Center notification by simply turning off the "Set up backup" message under the Maintenance section of the Windows 7 Action Center.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/06/image_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/06/image.png>)

Turning off this message in the Action Center in turn stopped the red cross message warning in the Action Center flag you can see in the system tray.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/06/image_thumb1.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/06/image1.png>)

This new MSDN article (<http://msdn.microsoft.com/en-us/library/bb891959(VS.85).aspx>) only states that this this use of the**DisableMonitoring** registry key should be used for "OEMs and developers of third-party backup applications "... to turn off these automatic notifications.". However in an SOE environment where no user data is stored on the local hard drive to the profile virtualisation and folder redirection then this registry key to stop the notification is perfect.

The problem with my [previous article](<https://www.grouppolicy.biz/2010/03/how-to-use-group-policy-to-turn-off-the-backup-notification-in-the-windows-7-actions-center/>) was that I showed you how to disable the action center notification using the very very very long registry key under **HKCU\Software\Microsoft\Windows\CurrentVersion\Action Center\Checks\\.** I only discovered this key to the work of people on the [Microsoft Forum](<http://social.technet.microsoft.com/Forums/en-US/w7itproui/thread/83dc3de6-70b7-450f-992c-60511e4a6c4f>) and thorough my own trial and error so this way was never exactly ideal.




The new way to do this as outlined in <http://msdn.microsoft.com/en-us/library/bb891959(VS.85).aspx> is to create the following registry key with the instructions as listed below:

### Registry Key Details

**Key:** HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsBackup
**Value:** DisableMonitoring
**Type:** REG_DWORD
**Data Enabled:** 0 (or not exist) = Disabled
**Data Disabled:** 1 = Enabled

**Step 1.** Edit a Group Policy Object (GPO) that is targeted to the computers that you want to disabled the backup notification.

**Step 2.** Navigate to Computer Configuration > Preferences > Windows Settings > Registry.

**Step 3.** Click on "Action" in the menu then "New" and then "New then Registry Item"

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/06/image_thumb2.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/06/image2.png>)

**Step 4.** Type "SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsBackup" into the Hive: text field and then "DisableMonitoring" in the Value Name then select the REG_DWORD Value Type and type "1" in the Value data: field.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/06/image_thumb3.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/06/image3.png>)

You should now see something like this in your Group Policy Editor.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/06/image_thumb4.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/06/image4.png>)

Now you will see that the Backup section of the Action Center has been disabled.




**Note:** This should happen by 10am the day after the policy setting is applied.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/06/image_thumb5.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/06/image5.png>)

You should also notice that the the "Set up Backup" has been removed from the Action Center Pop-up when the user hovers over the flag in the system tray.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/06/image_thumb6.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/06/image6.png>)