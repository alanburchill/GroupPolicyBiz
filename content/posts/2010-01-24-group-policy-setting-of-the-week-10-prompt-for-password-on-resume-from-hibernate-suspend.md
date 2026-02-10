---
title: "Group Policy Setting of the Week 11 "“ Prompt for password on resume from hibernate /suspend"
date: 2010-01-24 22:00:00
author: admin
categories: ["Security", "Setting of the Week"]
tags: ["bacis", "Power Plan"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb101.png"
---

The setting of the week this time highlights the one and ONLY power management policy that has been around since Windows 2000. The "Prompt for password on resume from hibernate / suspend" can be found under User Configuration > Administrative Templates > System > Power Management. Until Windows Vista came along this was the only power management setting that could be deployed via group policy so many people had to resort to many third party tools to manage power plans in windows via Group Policy. Note: For more information about configuring power plans using group policy see my other article [HERE](<https://www.grouppolicy.biz/2010/01/how-to-use-group-policy-preferences-to-manage-windows-power-plans/>). None the less this is still a very important setting that most SOE's I have seen have enabled to ensure that users are prompted for a password whenever their computers wake from hibernate or suspend . [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb101.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image106.png>) Not having this enabled could allow a uses to configured the laptop to auto-login during resume. As you can imagine this is not very good as a bad guy could steal a laptop while it is hibernating/sleeping and then power it on and have access to all the data with no effort. **Recommended Configuration:** Enabled