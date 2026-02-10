---
title: "Microsoft will not be releasing Remote Server Admin Tools (RSAT) for Windows 10 Redstone 2"
date: 2017-04-09 22:35:02
author: admin
categories: ["News", "Tip"]
tags: ["1703", "GPMC", "Redstone 2", "RSAT", "Windows 10"]
featured_image: "/uploads/2016/06/Icons6-e1478546087731.png"
---

Every time Microsoft releases a version of Windows 10 they also release a new version of the Remote Server Admin Tools. These tools are of course very important for any Group Policy Administrator as they contain the latest version of the Group Policy Management Console (GPMC). However, with this release of Windows 10 history is going to change. This time, Microsoft is _NOT_ going to be releasing a new version of the Remote Server Admin Tools (RSAT) with Windows 10 1703. That's right, there will be NO RSAT for Windows 10 Redstone 2. This may leave you wondering, how you are going to use Windows 10 if none of the RSAT tools can be installed in the OS. Well luckily there is an answer and all you need to do is download and re-install the Windows 10 1607 RSAT tools instead to get the admin tools back. Note, I said re-install as there is now an issues that removes the RSAT tools when you do an in place upgrade of the OS from 1607 to 1703. Microsoft has confirmed this is a problem and are working on fixing it however in the mean time you will need to re-installed the Tool Pack if you upgrade. Otherwise if its a clean install you can just install the old 1607 RSAT tools fresh. So if you do need to use one of the RSAT tools on your Windows 10 computer you can still can download it from <https://www.microsoft.com/en-us/download/details.aspx?id=45520>