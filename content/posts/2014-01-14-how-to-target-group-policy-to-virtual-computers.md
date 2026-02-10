---
title: "How to target Group Policy to Virtual Computers"
date: 2014-01-14 03:13:39
author: admin
categories: ["News", "Tutorials"]
tags: ["Hyper-V", "Virtualization", "VMWare", "WMI filtering"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2014/01/microsoft-hyper-v-logo_thumb.png"
---

[![microsoft-hyper-v-logo](https://www.grouppolicy.biz/wp-content/uploads/2014/01/microsoft-hyper-v-logo_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2014/01/microsoft-hyper-v-logo.png>)Fellow Australian and Microsoft Hyper-V Program Manager [Ben Armstrong](<http://twitter.com/virtualpcguy>) (a.k.a. Virtual PC Guy) has just published a blog explaining how you can deploy group policy object to be only targeting to virtual servers (see [Targeting Group Policy at Hyper-V VMs](<http://blogs.msdn.com/b/virtual_pc_guy/archive/2014/01/13/targeting-group-policy-at-hyper-v-vms.aspx> "http://blogs.msdn.com/b/virtual_pc_guy/archive/2014/01/13/targeting-group-policy-at-hyper-v-vms.aspx")). To do this he explains that you can create a WMI query filter that means the Group Policy object will only apply to Hyper-V guests.

> SELECT * FROM Win32_ComputerSystem WHERE Model = "Virtual Machine"

But what if you do not have Hyper-V guests deployed? Then you can running the following command on the virtual platform of choice to discover the model value to query.

> wmic computersystems get model

[![Untitled \(2\)](https://www.grouppolicy.biz/wp-content/uploads/2014/01/Untitled-2_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2014/01/Untitled-2.png>) In the example above you can see that this returns the vendor specific value of "VMWare Virtual Platform" (if you happen to be using VMWare). You can then take this model value to target the virtual platform of your choice (Hyper-V is of course the only valid choice).

> SELECT * FROM Win32_ComputerSystem WHERE Model = "VMWare Virtual Platform"

**TIP:** You can also use the same method to target Group Policy object to specific hardware models of servers and workstations.