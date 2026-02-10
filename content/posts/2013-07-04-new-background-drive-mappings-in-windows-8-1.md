---
title: "New Background Drive Mappings in Windows 8.1"
date: 2013-07-04 18:08:00
author: admin
categories: ["News"]
tags: ["Asynchronous", "Drive Mapping", "Windows 8.1"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2013/07/image_thumb4.png"
---

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/07/image_thumb4.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/07/image4.png>)As I briefly mention in my previous blog post about Group Policy Caching (<https://www.grouppolicy.biz/2013/07/group-policy-caching-in-windows-8-1/>) both Group Policy Preferences Drive Mappings and Disk Quotas are no longer processed as a Synchronous policy setting. But what does this exactly mean"....

Put simply Drive Mappings (and Disk Quota) policy settings will now apply in the background for the users without them having to reboot or log off their computers. This mean you can now update users drive mappings dynamically in background without them ever have to log off"... Sounds great but how does this work in practice? Glad you asked"...

Before".... No drive mapping"...

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/07/image_thumb5.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/07/image5.png>)

After the next background policy update (or manual "GPUPDATE") then"... TADA, the Drive Mapping has appeared.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/07/image_thumb6.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/07/image6.png>)

An interesting side affect of making this policy setting a background asynchronous setting is that it reduces the need for a computer to process a Foreground Synchronous policy refresh. Meaning it is less likely that you will encounter the performance issues over slow WAN link that Group Policy Caching improvement addresses. So"... Not only has made Group Policy Synchronous much faster they have greatly reduced the likeliness of it ever happening in the first place.

**WARNING:** As of the Windows 8.1 Preview if you set a drive mapping to "Remove" or "Replace" it will forcefully disconnect the drive and close any open files you have to that location.