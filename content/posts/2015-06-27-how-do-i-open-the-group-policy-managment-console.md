---
title: "How do I open the Group Policy Managment Console?"
date: 2015-06-27 03:12:19
author: admin
categories: ["Group Policy FAQ"]
---

The Group Policy Managment Console (a.k.a. GPMC) is the tool that is used to modify Group Policy Objects. By default it is _not_ installed on Windows computers. If you are running a version of Windows before Windows 10 1803 you will need to first install the Remote Server Admin Tools (a.k.a. RSAT). This will install the nessessary file for you to run the GPMC. If you are still running Windows 7 you may also need to go into "Programs and Feature" then "Turn Windows Features On or Off" and install the "Group Policy Managagment Console". Once you have GPMC install you can simple press start and type "Group Policy Managment". You should then see the option "Group Policy Management - Desktop app" that you can then run. Alternativly you can open the "All Programs" from the start menu and expand "Windows Administrative Tools" and then click on "Group Policy Management". Group Policy Managment Console should now be open and if you have the correct permissions you should be able to modify Group Policy Objects. _Warning_ Do not edit Group Policy Settings if you are not experience. These settings can break _ALL_ your comptuers in your organisation.