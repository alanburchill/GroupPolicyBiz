---
title: "What is new in Windows 8"
date: 2011-09-26 23:29:17
author: admin
categories: ["News"]
tags: ["Features", "Windows 8"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2011/09/BUILD_Logo_thumb2.jpg"
---

[![BUILD_Logo](https://www.grouppolicy.biz/wp-content/uploads/2011/09/BUILD_Logo_thumb2.jpg)](<https://www.grouppolicy.biz/wp-content/uploads/2011/09/BUILD_Logo2.jpg>)Over the past few days in my spare time I have been watching some of the BUILD session video's about Windows 8. Below are just some of the notes around Windows 8 that I have been able to find out what is new in Windows 8. Some of these features are consumer and/or server orientated but all of these features are pretty impressive if they work as advertised. I can't wait!!!

  * sub-32bit video colour is no longer supported in Windows 8
  * XDDM video driver will no longer work in Windows 8
  * Upgrade of video drive in Windows 8 will not lose SYNC with monitor...
  * Display Drivers can be Full, Render Only and Display Only
  * True Headless Server are now supported. Int10 is handled by stub driver of VGA drive.
  * Video Drive crashes can be isolated to a specific engine rather than the whole driver.
  * Windows To Go "“ You will be able to run full copy of Windows of any 32gb USB Storage device. This means you will be able to take your computer with you in your pocket and just plug it into almost any computer.
  * USB 3 is now fully supported.
  * WiFi Direct is now supported. This will allow you to connect any two WiFi direct devices without an access point.
  * You can project any HTML5 video to a play-to device with Windows
  * NVIDIA Windows 8 ARM based systems an support TPM (This was a channel 9 video).
  * Bitlocker Network Unlock in Windows 8 will be great. If the computer is plugged into the LAN no start-up PIN will be required.
  * 15.6ms wake timer is gone during sleep mode therefore better battery life.
  * Connected standby allows you apps to sleep but then periodicly wake up and check for new information so they stay up to date.
  * SMB 2.2 will allow you to load balance all SMB traffic over multiple NIC's
  * In build NIC Teaming Support
  * Server comes in 3 modes. Full Shell, No Shell (only management tools) & Server Core. This means all certified server products must be able to run without a Windows Shell.
  * Servers are now configured using PowerShell and this is driven using Server Manager.
  * Server Manager will allow you to manage multiple server at the same time.
  * Using PowerShell or DISM you can move add/remove the shell
  * Windows 8 will have an AppStore, very similar to windows phone.
  * Hyper-V servers will support VHD's on SMB Shares. This means you can run a live migration fail over cluster without the need to iSCSI or Fibre Channel SAN's.
  * All Metro App's will be able to save Applications configuration to SkyDrive. This allows your metro settings to roam between computers. This does NOT replace traditional AppData.
  * RemoteFX will work over a WAN and has greatly reduced bandwidth requirements. It can also us UDP packets for transmission of videos.
  * Hyper-V Virtual Network allows you to migrate hosts from on-site to off-site without having to re-IP the servers. A virtual network tunnel will be established between both sites that allows the same subnet to span multiple geographical locations.
  * Single instance storage is now support. This is MASSIVE!!! Put you VHD files on a SMB file share and enable de-duplication and reduce the storage requirements overnight. But this also works for all other files types such as office file format.
  * Hyper-V is now support on the Windows 8 (Client)
  * Secure Boot ensures that the whole boot process is secure. This prevents malware/rootkits from being able to install before the OS starts. This leverages systems with a TPM chip.
  * TPM can now be used to store certificates to ensure that malware cannot access these certificates. The is protected via a password with a hammer timeout
  * Add multiple USB 3 devices and then pool them together for high performance disk drive.
  * Memory chips can now be put into low power mode saving power on a system.


Update:

  * Windows Server and Windows Client will be released on the same schedule.
  * Windows Server certified apps should not require reboot and must allow administrator to postpone if required.
  * All PCI Express drivers must Advanced Error Reporting that should report hardware issues to the OS


Update #2:

  * Windows 8 version number is 6.2 "“ This is to resolve a large number of compatibility issues.
  * Desktop Windows Manager (DWM) is always turned on.
  * 8 and 16 bit color apps are emulated in the 32bit color space.
  * Flight Simulator 2002 a DirectX 7 app will work on Windows 8
  * Users will be able to easily disable or enabled start-up apps via task manager.
  * .Net 4.5 will be installed by default.
  * .Net 3.5 can be installed as a feature on demand from Windows Update.
  * All applications that work with Windows 7 will work with Windows 8
  * All apps in the Windows AppStore must be Windows App Certified


Update #3:

  * Stereo 3D now supported
  * Computer screen wont flicker during boot, resume form sleep and driver upgrade
  * All Slate devices must support 3D Accelerometer,3D Gyro,3D Magnetometer & Sensor Fusion (Location via GPS and WIFI)


Update #4:

  * Support for Bluetooth LE which can enable keyboards that only needs battery changes every few years"...
  * Fill associations for programs will be automatically cleaned up when a metro app is removed.


There is a lot more videos to watch"... So I will update this post as I find out more information.

**Note:** To be clear all of this information is from the BUILD and Channel9 Videos.