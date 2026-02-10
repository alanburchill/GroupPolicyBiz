---
title: "How to mitigate Windows Help Security Issue KB2219475 with Group Policy"
date: 2010-06-15 09:00:00
author: admin
categories: ["Security", "Tutorials"]
tags: ["2219475", "Google", "Group Policy Prefereces", "HCP", "KB2219475"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/06/image_thumb20.png"
---

A [Google Engineer recently](<http://www.eweek.com/c/a/Security/Microsoft-Warns-of-Windows-Security-Bug-Found-by-Google-Engineer-545236>) [irresponsibly](<http://www.sophos.com/blogs/gc/g/2010/06/11/google-engineer-act-irresponsibly-microsoft-zeroday-disclosure/>) [disclosed](<http://it.slashdot.org/story/10/06/16/0021225/Miscreants-Exploit-Google-Outed-Windows-XP-Zero-Day>) to the public after only warning Microsoft 5 days earlier of a vulnerabilities that allows a malicious third-party to take advantage of a security issue with the Help and Support Center in Windows XP/2003 after. As a result this has left many users (and organisations) open to attack using this exploit. Thankfully Microsoft have quickly responded and they have published an security advisory (<http://www.microsoft.com/technet/security/advisory/2219475.mspx>) about this issue with workaround instructions while they are working on a security fix.

**Update:** This security vulnerability is now being [actively used by hackers](<http://www.computerworld.com/s/article/9178084/Hackers_exploit_Windows_XP_zero_day_Microsoft_confirms>).

For your benefit I have written instructions below showing you how you can mitigate this security issue using Group Policy Preferences. As this workaround involves in deleting a registry key (and sub-keys) I have also put in instructions on how to backup and restore this key after you have deployed a the fix for this issue in your organisation.

### How to backup the affected registry

In these steps you will create a registry keys backup file for later use to restore the functionality of the Help and Support Center after you are deploy the related hotfix. Normally you can backup the registry using the Registry Wizard in Group Policy Preferences however this is a Windows XP specific key and you cannot remotely import a HKEY_CLASSES_ROOT remotely via Group Policy Management Console therefore we need to Export (a.k.a backup) the registry key via the traditional Regedit method.

**Step 1.** Go to a Windows XP computer that you want to use for a template to backup the registry.

**Step 2.** Run Regedit and navigate to the HKEY_CLASSES_ROOT\HCP key then click on **File** and then **Export**

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/06/image_thumb20.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/06/image18.png>)

Step 4. Save the registry as key a file (example HCP_Backup.reg)

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/06/image_thumb22.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/06/image19.png>)

**Note:** Keep this file safe as you will need it to restore the HCP key once you have deployed the hotfix.

### How to delete the HCP registry key

These instruction will show you how to delete the HKEY_CLASSES_ROOT\HCP key that is the suggested workaround to this security issue.

**Step 1**. Create a new Group Policy Object that is targeted to the computer object you want to apply this workaround.

**Step 2.** Navigate to Computer Configuration > Preferences > Windows Settings > Registry and then from the menu click on Action > New > Registry Item

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/06/image_thumb23.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/06/image20.png>)

**Step 3.** Select **Delete** from the Action pop-down menu and then **HKEY_CLASSES_ROOT** from the HIVE: menu and type **HCP** in the Key Path:

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/06/image_thumb24.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/06/image21.png>)

**Step 4 (Optional):** Then click on the Common Tab and tick **Apply once and do not reapply**.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/06/image_thumb25.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/06/image22.png>)

**Note:** Doing this will allow you to restore the functionality for selected users if required by simply running the previously

The HCP functionality will now be broken when you click on any HCP:// link. While this is not an often used feature of Windows XP I have seen it some organisations that use a link to the just straight to the "Offer Remote Assistance" feature.


### How to restore the HCP registry key

Once Microsoft releases an security hotfix for this issues then you may want to restore the registry key we deleted above. Unfortunately (as I mentioned before) we are not able to easily import the registry key using the "Registry Wizard" option of Group Policy Preferences as you can only import HKLM_CLASSES_ROOT keys locally on a PC. Therefore we will need to use a logon script (OH NO!!!) to import the original HCP keys.

**Step 1.** Edit the same GPO that you previously deleted the HCP key.

**Step 2.** Navigate to Computer Configuration > Windows Settings > Scripts (Startup/Shutdown) and double click on Startup in the right hand pane.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/06/image_thumb26.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/06/image23.png>)

**Step 3.** Click on **Show files"...**

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/06/image_thumb27.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/06/image24.png>)

**Step 4.** Paste a copy of the **HCP_Backup.reg** file we created in the backup steps then close the folder.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/06/image_thumb28.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/06/image25.png>)

**Step 5.** Back on the Startup Properties windows click on the **Add"...** button.

**Step 6.** Type **regedit.exe** in the Script Name: field and **/s HCP_Backup.reg** in the Script Parameters: field then click OK

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/06/image_thumb29.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/06/image26.png>)

This will now import the backup registry key the next time the computer reboots.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/06/image_thumb30.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/06/image27.png>)

**Step 7 (CLEAN UP).** Finally go navigate to Computer Configuration > Preferences > Windows Settings > Registry in the Group Policy Management Editor and either disable or delete the HCP Delete key preference item previously created.

Hope it helps"...