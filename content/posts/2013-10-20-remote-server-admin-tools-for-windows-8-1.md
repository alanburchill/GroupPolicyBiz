---
title: "Remote Server Admin Tools for Windows 8.1"
date: 2013-10-20 22:04:29
author: admin
categories: ["News"]
tags: ["GPMC", "RSAT", "Windows 8.1"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2013/10/win8_logo_0_thumb.jpg"
---

[![win8_logo_0](https://www.grouppolicy.biz/wp-content/uploads/2013/10/win8_logo_0_thumb.jpg)](<https://www.grouppolicy.biz/wp-content/uploads/2013/10/win8_logo_0.jpg>) With yet another release of Windows (seems like it was only last year"... errr"... wait), Microsoft has also released a new version of the remote server admin tools (a.k.a. RSAT). RSAT allow you to install the tools needed to manage your servers from a Windows 8.1 computer. You might not think you need the RSAT installed as you are just remote desktop of the server you want to configure when needed to perform changes. Needless to say always logging onto a server to configure it is generally poor practice as it can lead to system stability issues. Once you install the tools on your PC you can use them to remotely perform these configuration without even having to logon to the server. This is even more practical now as all of the new tools are written via PowerShell meaning they can be run remotely against servers just as effectively as on the local machine. Of course the real reason why you want the RSAT tools install on your computer it so you can run the latest version of the Group Policy Management Console (a.k.a. GPMC). **Tip:** Always edit group polices using the latest version of GPMC as this will support all the features and cause the least amount of compatibility issues. As an example you might have noticed that there is no Internet Explorer 11 Group Policy Preferences however the IE10 GPP does support IE11 in the new revision. In fact I talk about this in detail in my [TechEd New Zealand ](<https://www.grouppolicy.biz/2013/09/teched-the-browser-you-love-to-hate/>)session where I show that the version checking for IE 10 group policy preferences now check for version 10 to version 99. As with the previous version of the Remote Server Admin Tools Microsoft will also be automatically installing all the tools once the Windows Update is applied..

> **NOTE:** In this release of Remote Server Administration Tools, all tools are enabled by default. There is no need to open **Turn Windows features on or off** in Windows 8.1, and enable the tools that you want to use.

Downloat RSAT Link <http://www.microsoft.com/en-us/download/details.aspx?id=39296>