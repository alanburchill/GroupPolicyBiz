---
title: "Update: How to workaround KB2286198/MS10-046 .lnk Icon security issues with Group Policy"
date: 2010-08-02 23:00:00
author: admin
categories: ["Security", "Tutorials"]
tags: [".lnk", "2286198", "Intermediate", "KB2286198", "MS10-046", "Security", "Workaround"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/07/2290360_thumb.png"
---

**Update:** Microsoft have now released the patch to the .lnk vulnerability [MS10-046: Vulnerability in Windows Shell could allow remote code execution](<http://support.microsoft.com/kb/2286198> "http://support.microsoft.com/kb/2286198") . If you have previously deployed the workaround using this article then it is now time to reverse the change you made by simple jumping to [Removing the KB2286198 Workaround via Group Policy](<#remove>) section and following the instructions. Needless to say this is a particular bad security issue and that you should be deploying this patch to all the computers in your environment ASAP. **You have been Warned!!!**

There is currently a [Microsoft Security Advisory KB2286198](<http://www.microsoft.com/technet/security/advisory/2286198.mspx>) out that affects all copies of Windows about a security issues with displaying icons on shortcuts via non-local drives (e.g. Removable, Network and WebDav folders). The security advisory lists the workaround to the issues that effectively disables displaying all shortcuts. While this is not exactly a prettiest workaround (see image below) it does prevent you from being vulnerable to the security exploit.

[![2290360](https://www.grouppolicy.biz/wp-content/uploads/2010/07/2290360_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/2290360.png>)

There is a [Microsoft Fix It for the issues](<http://support.microsoft.com/kb/2286198>) if you just want to apply this workaround to a handful of computers but below I will show how you can apply the same workaround to all your domain computers using Group Policy.

### KB2286198 Workaround via Group Policy Instructions

First we are going to create a policy that we can use at a later stage to restore the icon handler. The value that we are

**Step 1.** Edit a Group Policy Object that applies to all the computers you want to apply the workaround

**Step 2.** Navigate to Computer Configuration > Preferences > Windows Settings > Registry and in the menu click on Action > New > Registry Item

**Step 4.** Change the Hive to "HKEY_CLASSES_ROOT" then type "lnkfile\shellex\IconHandler" in the Key Path then tick Default and type "{00021401-0000-0000-C000-000000000046}" in the "Value Data" field and then click OK

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb53.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image55.png>)

We now want to disable this entry as we are going to use to to restore the Icon Handler once you the patch for this issue is out.

**Step 5.** Click on the IconHandler item in the right hand column and then click "Disable this item" (Red Circle) in the toolbar.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb54.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image56.png>)

Now we create the entry that disables the Icon Handler"...

**Step 6.** Right click on the IconHandler registry item you just created and click "Copy"

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb55.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image57.png>)

**Step 7.** Right click somewhere in the blank in the right column and click "Paste"

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb56.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image58.png>)

**Step 8.** Click Yes

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb57.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image59.png>)

**Step 9.** Click on the second IconHandler registry item and click "Enable this item" (Green Circle) in the toolbar.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb58.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image60.png>)

**Step 10.** Double click on the second IconHandler registry item and clear the "Value Data" field then click Ok.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb59.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image61.png>)

**Step 11.** Now select and copy both IconHandler 1 & 2 and paste them again into a blank area (see step 6,7 & 8).

**Step 12.** Double click on IconHandler 3 & 4 and change the "lnkfile" in the Key Path to "piffile" (should now look like below image).

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb60.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image62.png>)

Now we are going to disable the WebClient Service that is the second part of this workaround"...

**Step 13.** In the same GPO navigate to Computer Configuration > Preferences > Control Panel Settings > Services and in the menu Action > New > Service

**Step 14.** Change the Startup value to "Disabled" and type "WebClient" in the Service Name text field then change the Service Action to "Stop Service" and click OK.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb61.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image63.png>)

Done"...

The workaround will now push out to all you workstations and become affective on the next reboot (see image below).

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb62.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image64.png>)

Removing the KB2286198 Workaround via Group Policy

**Step** **1.** In the GPO you set this up in navigate back to Computer Configuration > Preferences > Windows Settings > Registry and delete enabled registry entries (probably the second and fourth) and then click on the remaining two registry entries and click on Enable this item in the toolbar (see image below).

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb63.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image65.png>)

**Step 2.** In the same GPO navigate to Computer Configuration > Preferences > Control Panel Settings > Services and double click on the WebClient service item and change the Startup to "Manual" and the Service Action to "No change" then click OK.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb64.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image66.png>)

Hopefully this will keep you secure until Microsoft release a patch for this security issue. As always implement these fixes at your own risk and I make no guarantees that these workaround will necessarily work in your environment.

### Further References

  * <http://securitygarden.blogspot.com/2010/07/fix-it-released-for-security-advisory.html>
  * <http://securitygarden.blogspot.com/2010/08/critical-out-of-band-update-released.html>
  * <http://support.microsoft.com/kb/2286198>
  * <http://www.microsoft.com/technet/security/advisory/2286198.mspx>
  * <http://www.microsoft.com/technet/security/bulletin/ms10-046.mspx>