---
title: "How to use Group Policy to disable the EU Browser Choice"
date: 2010-03-02 05:30:31
author: admin
categories: ["Tutorials"]
tags: ["Advanced", "Browser Ballot", "EU", "Group Policy Preferences", "KB2019411", "KB976002", "Popular"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb10.png"
---

In case you had not already heard Microsoft have had to release an update for all European users to prompt display a ballot screen about what version of browser they want to use (see below). This is one of the actions Microsoft had to do to comply with the EU anti-trust case. [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb10.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image10.png>) Microsoft have released article [KB2019411](<http://support.microsoft.com/kb/2019411>) explaining how IT administrators can disable a Browser Choice screen for their users using a simple registry key. **Key:** HKLM\Software\BrowserChoice **Value:** Enable **Data:** 1 (REG_DWORD) = Enabled **Data:** 0 = Disabled Now of course you can deploy registry key using Group Policy Preferences which will make it much easier for IT administrators disable this screen. Step 1. Edit a Group Policy Object that is applied to all the workstation you want this Browser Ballot disabled. Step 2. Navigate to Computer Configuration > Preferences > Windows Settings > Registry and create a "New Registry Item" Step 3. Type "Software\BrowserChoice" in the Key Path then type "Enable" in the Value name, then select REG_DWORD as the value type "0" in the value data and then click "OK". [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb15.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image15.png>) If all that is to much hassle to do all that below is a link to the Group Policy Preference XML file you can just copy into the policy. Links:

  * More information on the Brower Choice <http://support.microsoft.com/kb/976002>
  * More information on the Disable registry key <http://support.microsoft.com/kb/2019411>
  * Also check out Aaron Parkers blog here for more information <http://blog.stealthpuppy.com/windows/disable-the-browser-choice-screen>