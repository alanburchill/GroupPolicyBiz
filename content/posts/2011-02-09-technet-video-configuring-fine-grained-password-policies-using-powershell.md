---
title: "TechNet Video: Configuring Fine-Grained Password Policies using PowerShell"
date: 2011-02-09 10:06:16
author: admin
categories: ["Video"]
tags: ["Fine Grain Password Policies", "Powershell"]
---

Fine Grained Password Polices (FGPP) allow IT administrator to apply password and account lockout policies to different users or groups of users in you domain. The major pain about FGPP is that you cant just use Group Policy to use them instead you have to use [ADSIEDIT](<http://technet.microsoft.com/en-us/edge/fine-grained-password-policy-screencast.aspx>) to make the changes"... Major PITA.

But lucky some of the pain about making changes to the FGPP can be reduce by using PowerShell to Automate the process to make it easier to apply multiple FGPP. So to see how to do this [Manoj Ravikumar Nair](<http://technet.microsoft.com/edge/ff832960.aspx?category=Manoj Ravikumar Nair>) has just done a video on [TechNet Edge](<http://technet.microsoft.com/>) showing how to do the whole process.

[ ![Get Microsoft Silverlight](http://go.microsoft.com/fwlink/?LinkId=161376) ](<http://go.microsoft.com/fwlink/?LinkID=149156&v=4.0.50424.0>) Download link <http://content1.catalog.video.msn.com/e2/ds/alt-en-us/ALTENUS_TECHNET/ALTENUS_TECHNET_EDGE/67178ab1-7708-4d25-8921-2e50e6014570.mp4>

> In this video, I use the Active Directory Module for Windows PowerShell introduced in Server 2008 R2 to create and configure Fine-Grained Password Policy, a new feature introduced in Server 2008 that allows having multiple password and account lockout policies in a Domain. I also walk you through the process of raising the domain functional level using PowerShell.