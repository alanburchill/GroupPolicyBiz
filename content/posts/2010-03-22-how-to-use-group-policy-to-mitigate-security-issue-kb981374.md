---
title: "How to use Group Policy to mitigate security issue KB981374"
date: 2010-03-22 20:20:05
author: admin
categories: ["Security", "Tutorials"]
tags: ["Intermediate", "Internet Explorer", "KB981374", "mitigation", "Security"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb58.png"
---

There is currently a security advisory out about a Zero Day vulnerability in Internet Explore 6 & 7 on Windows XP and Vista. While there is no patch out for this issues so far you can mitigate the security a number ways using Group Policy. Below I have listed two ways to implement the workaround as listed by Microsoft using Group Policy.

### Method 1. Modify the Access Control List (ACL) on iepeers.dll

Step 1. Edit a Group Policy Object (GPO) that is targeted to the computer accounts you want to apply this setting. Then navigate to Computer Configurations > Windows Settings > Security Settings > File System.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb58.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image58.png>)

Step 2. Click on "Action" in the menu and then "Add File"..."

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image3_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image310.png>)

Step 3. Type "%WINDIR%\System32\iepeers.DLL" into the Folder: field then click "OK"

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb59.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image59.png>)

Step 4. Click "Add"and then add the "Everyone" group and click "OK"

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb60.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image60.png>)

Step 5. Tick the Full Control "Deny" tick box. This will then tick all the Deny tick boxes.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb61.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image62.png>)

Step 6. Click "Yes" to the Deny warning.

![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb62.png)

Step 7. Click "OK" to the permissions option.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb63.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image63.png>)

Note: If you want to apply this to x64 version of Windows as well repeat step 2 thought 7 but type "%WINDIR%\SYSWOW64\iepeers.DLL" instead in the Folder: field.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb64.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image64.png>)

You have now denied permissions to the file that has the issues.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb65.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image65.png>)

Once you have applied the patch to fix this vulnerability be sure to go into each of file security settings and remove the "Everyone" deny permission from the setting.

### Method 2: Configure Internet Explorer to prompt before running Active Scripting or to disable Active Scripting in the Internet and Local intranet security zone

Step 1. Edit a GPO that is targeted to the users accounts you want to apply security setting. Then Enabled both the "Allow active scripting" under User Configuration > Policies > Administrative Templates > Windows Components > Internet Explorer > Security Page > Internet Zone and the Intranet Zone. Then configure the Options to either "Prompt" or "Disable".

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb66.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image66.png>)

Once you have performed the above configuration changes be sure to add ***.windowsupdate.microsoft.com,** ***.update.microsoft.com** and any other site you require to run Active Scripting on to the trusted sites zone list. Instructions on how to do this can be found here [How to use Group Policy to configure Internet Explorer security zone sites](<https://www.grouppolicy.biz/2010/03/how-to-use-group-policy-to-configure-internet-explorer-security-zone-sites/>)

**Disclaimer:** I do not guarantee that this information will work. All the above information is to be used at your own risk.

For more details on the security vulnerability and other ways to mitigate this issue see [Microsoft Security Advisory (981374)](<http://www.microsoft.com/technet/security/advisory/981374.mspx> "http://www.microsoft.com/technet/security/advisory/981374.mspx")