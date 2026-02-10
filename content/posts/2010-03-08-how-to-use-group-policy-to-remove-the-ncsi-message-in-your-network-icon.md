---
title: "How to use Group Policy to remove the Network Connectivity Status Indicator message in your network icon"
date: 2010-03-08 16:00:00
author: admin
categories: ["Tutorials"]
tags: ["Basic", "Group Policy", "Group Policy Preferences", "NCSI", "Network Connectivity Status Indicator", "Vista", "Windows 7"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb37.png"
---

Windows has a cool feature that allows you to tell if your computer has Internet connectivity when you are connected to a network (see image below). This feature is called Network Connectivity Status Indicator (NCSI) it uses a combination of DNS and/or HTTP look ups to tell if you are connected to the Internet. The way does this is either via a HTTP request for <http://www.msftncsi.com/ncsi.txt> or a DNS look up for **dns.msftncsi.com** that resoles to **131.107.255.255** [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb37.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image37.png>)

### Windows 7

However if you find this error message really annoying there is now a Windows 7 group policy will turn it off. This is a machine setting so edit a Group Policy Object that is applied to all the workstations you want to turn this message off. Then navigate to Computer Configuration > Policies > Administrative Templates > Network Connections and enabled the "Do not show the "local access only" network icon" policy setting. [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb38.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image38.png>) TADA"... Now you will no longer see the exclamation icon on the network icon. [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb39.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image39.png>) For more information on how NCSI works and this Windows 7 policy see <http://technet.microsoft.com/en-us/library/ee126135(WS.10).aspx>

### Windows Vista

Unfortunately Windows Vista does not have the same Group Policy however there is a registry key that can be applied using Group Policy Preferences that has the same affect. **Key:** HKLM\SYSTEM\CurrentControlSet\Services\NlaSvc\Parameters\Internet **Value:** EnableActiveProbing **Data:** 1 (REG_DWORD) = Enabled **Data:** 0 = Disabled **Step 1.** Edit a Group Policy Object that is applied to all the workstation you want this Browser Ballot disabled. **Step 2.** Navigate to Computer Configuration > Preferences > Windows Settings > Registry and create a "New Registry Item" **Step 3.** Type "SYSTEM\CurrentControlSet\Services\NlaSvc\Parameters\Internet" in the Key Path then type "EnableActiveProbing" in the Value name, then select REG_DWORD as the value type "0" in the value data and then click "OK". [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb40.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image40.png>) For more information on how NCSI works and this Windows Vista policy see <http://technet.microsoft.com/en-us/library/cc766017(WS.10).aspx>