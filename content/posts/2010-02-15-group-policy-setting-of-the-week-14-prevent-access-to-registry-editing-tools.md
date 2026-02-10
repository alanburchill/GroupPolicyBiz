---
title: "Group Policy Setting of the Week 14 "“ Prevent access to registry editing tools"
date: 2010-02-15 01:16:29
author: admin
categories: ["Setting of the Week"]
tags: ["Basic", "Group Policy", "regedit"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/02/image_thumb72.png"
---

This weeks setting is another is another oldie but a goodie that is commonly used to lock down SOE's so that users can use the registry editor. It is called "Prevent access to registry editing tools" which us a user setting found under User Configuration > Policies > Administrative Template > System and will work on all platforms since Windows 2000.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/02/image_thumb72.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/02/image72.png>)

The affect is pretty simple"... It stops users from running regedit.exe so they cant make registry changes to their computer or profile. This will also work even if a user take a copy of the regedit.exe command and rename it to something else.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/02/image_thumb73.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/02/image73.png>)

If you select "No" for the "Disable regedit from running silently?" this will allow user to apply registry keys via a preconfigured .REG file using the "regedit.exe /s" silent switch so make sure you select "Yes" unless you need to this back door for something like a logon script.