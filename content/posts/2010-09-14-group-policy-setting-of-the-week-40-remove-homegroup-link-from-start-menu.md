---
title: "Group Policy Setting of the Week 40 &ndash; Remove Homegroup link from Start Menu"
date: 2010-09-14 08:00:00
author: admin
categories: ["Setting of the Week"]
tags: ["Homegroup", "start menu"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb2.png"
---

[Homegroup](<http://windows.microsoft.com/en-us/windows7/products/features/homegroup>) is a new feature in Windows 7 that allows users on a small network to easily share all their files and printers with each other with a single share password. This greatly simplifies the process to securely share information on a home network and it can include both domain and non-domain joined computers. As an IT administrator you may not want to encourage the use of this feature for your domain joined computers so there is an option to remove the Homegroup link from the Start Menu. This setting can be found under User Configuration > Policies > Administrative Templates > Start Menu and Taskbar and as a Homegroup is a Windows 7 feature this can obviously only be configured on Windows 7 computers.

**Start Menu with Homegroup "“ Before** | **Start Menu with** **Homegroup "“ Before**
---|---
[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb2.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image2.png>) | [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb3.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image3.png>)
**Start Menu without Homegroup "“ Enabled** | **Customize Start Menu "“ Enabled**
[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb4.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image4.png>) | [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb5.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image5.png>)

****

**Note:** This only removes the shortcut from menu so users can still configure a homegroup via the control panel.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb1.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image1.png>)

For more information on this setting see <http://gps.cloudapp.net/Default.aspx?PolicyID=4668>