---
title: "Group Policy Setting of the Week 16 "“ Prevent Roaming Profile changes from propagating to the server"
date: 2010-02-28 23:00:00
author: admin
categories: ["Setting of the Week"]
tags: ["Basic", "Group Policy", "Profile"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/02/image_thumb79.png"
---

This setting is another profile related setting however I think the focus is warranted as so many organisations use roaming profiles. This setting is called "Prevent Roaming Profile changes from propagating to the server" and can be found under Computer Configuration > Policies > Administrative Templates > System > User Profiles and like the previous setting work on Windows XP / 2003 or above.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/02/image_thumb79.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/02/image79.png>)

This setting would be very useful to apply to computer that have un-usual configuration that might other wise make unwanted changes to a users roaming profile. This setting would essential prevent any changes made to the users profile propagating to other workstations. One example where this could be used is when you want to test a new application with a real users account.