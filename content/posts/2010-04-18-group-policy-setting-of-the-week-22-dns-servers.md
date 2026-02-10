---
title: "Group Policy Setting of the Week 22b "“ DNS Servers"
date: 2010-04-18 20:00:00
author: admin
categories: ["Setting of the Week", "Tutorials"]
tags: ["Basic", "DNS", "Group Policy", "Windows XP"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/04/image_thumb10.png"
---

I used to think that it was not possible to set IP address information via Group Policy however I did some checking this week and was pleased to find that there was a way to configure your computers DNS Server addresses. Unfortunately this setting only applies to Windows XP, however lots of people still use XP so it is still somewhat relevant. This setting is simple called "DNS Servers" and can be found under Computer Configuration > Administrative Template > Network > DNS Client.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/04/image_thumb10.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/04/image14.png>)

Figure 1.

To configure this setting simple check Enabled and type each IP address of the DNS Servers with a space between them.

While DNS Server settings are normally configured via DHCP this option can be really handy when you have two separate Active Directory forests on the same LAN. This is common where two companies have physically merged but still run separate AD's forests connected to the same network. Now for name resolution you can setup DNS forwarders from forest A to forest B however this does not work for dynamic DNS registrations of the computer names.

**Note:** When this setting is applied its a little bit tricky to confirm that it has actually applied as both the network properties (see figure 2.) and even and ipconfig /all will show the manually configured IP DNS setting (see figure 3.). However if you do a NSLOOKUP (also see figure 3.) you will notice that the DNS server that it uses is the DNS Server that is configured in the Group Policy or alternatively you can just rely upon an rsop.msc report.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/04/image_thumb11.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/04/image16.png>)

Figure 2.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/04/image_thumb12.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/04/image17.png>)

Figure 3.