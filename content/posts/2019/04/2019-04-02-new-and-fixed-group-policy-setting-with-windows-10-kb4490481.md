---
title: "New and Fixed Group Policy Setting with Windows 10 KB4490481"
date: 2019-04-02 22:32:38
author: admin
categories: ["News"]
tags: ["hotfix", "Soft-Disconnect", "Windows 10"]
featured_image: "/uploads/2019/04/Lan.png"
---

Microsoft has just released a new rollout KB hotfix for Windows 10 on the 1st April (not joking). What is notable about this update is there is a couple of Group Policy settings that have been fixed and added.

First one is only minor and they have resolved an issues with the policy setting "Turn off app notifications on the lock screen" which can be found under Computer Configuration > Administrative Templates > System > Logo.

The second Group Policy change is they have now added support to configure "Enable Windows to soft-disconnect a computer from a network". What is "[soft-disconnect"](<https://docs.microsoft.com/en-us/windows-hardware/drivers/mobilebroadband/understanding-and-configuring-windows-connection-manager>) you ask? Put simple its a way for a computer to notify application to stop using a specific network interface. If there is an active TCP connection then it will not interrupt that connection. Then after 30 seconds if it still sees that someone or something is using the connection in a significant way (e.g. Skype Call) it will not close the connection. This is far better experience for users, however it can also lead to computer not swapping from wireless to wired connections. It is a default option for Windows 8 and later, so if you want to ensure that network connection are closed then you should disable this policy.

You can download the new update via Windows Update or via the Windows Update Catalog at <https://www.catalog.update.microsoft.com/Search.aspx?q=KB4490481> .

You can read more about "soft-disconnect" at [https://docs.microsoft.com/en-us/windows-hardware/drivers/mobilebroadband/understanding-and-configuring-windows-connection-manager ](<https://docs.microsoft.com/en-us/windows-hardware/drivers/mobilebroadband/understanding-and-configuring-windows-connection-manager>)