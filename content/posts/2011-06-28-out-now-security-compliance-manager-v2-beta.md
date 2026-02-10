---
title: "Out Now: Security Compliance Manager v2 Beta"
date: 2011-06-28 00:08:00
author: admin
categories: ["News"]
tags: ["Beta", "SCM v2", "Security Compliance Manager"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2011/06/image_thumb41.png"
---

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/06/image_thumb41.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/06/image41.png>)A new version of the super awesome Security Compliance Manager v2 has now been [released to the pub](<https://connect.microsoft.com/site715/InvitationUse.aspx?ProgramID=2663&InvitationID=SCM2-QCDB-CWPV>)lic on the connect web site. If you may [remember](<https://www.grouppolicy.biz/2011/03/out-now-microsoft-security-compliance-manager-v2-ctp/>) Microsoft released the CTP version of this product back in march which had some of the new features:

  * Ability to Import GPO's into Custom Baseline Templates
  * Ability to install without having to install SQL Express Instance


Well the new version is now out and besides being a lot more stable it has a super new look and feel with a few more features"...

### New Look

Well the new beta is out sporting a fantastic new interface with more more features making it much easier to use with a great new (and useful) home screen. As you can see below the new layout is very different to the previous v1 and v2 CTP and has a more horizontal layout that makes it much easier for it to find the setting you are trying to find.

SO PRETTY!!!!

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/06/image_thumb42.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/06/image42.png>)

### Attachments and Guidelines

Another new feature you might notice is that there is now a section called Attachments and Guidelines that has a lot of support documentation that relate to the Security baseline. This section also allows you to add your own supporting documentation to your custom baseline templates.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/06/image_thumb43.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/06/image43.png>)

### New Security Baseline Templates

You will also find that there are 4 long awaited security (beta) baseline template being released with the SCM v2 beta, they are:

  1. Internet-Explorer-9-Security-Compliance-Baseline-Beta
  2. Windows-Server-2003-SP2-Security-Compliance-Baseline-Beta
  3. Windows-Server-2008-R2-SP1-Security-Compliance-Baseline-Beta
  4. Windows-Server-2008-SP2-Security-Compliance-Baseline-Beta


[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/06/image_thumb44.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/06/image44.png>)

### SCM Settings Library

One of the under the hood features that you might not necessarily notice straight away is that SCM has has its own settings database about all the Group Policy Setting. This "Settings Library" is where the additional information such as "Risk's" and "Mitigations" is stored and matched to the Group Policy Setting in the baseline templates or imported GPO's. This "Settings Library" can also be update when any new guidance comes out around any of the settings or when new settings are added to support future OS's such as "Codename" Windows 8.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/06/image_thumb45.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/06/image45.png>)

### LocalGPO

LocalGPO is a tool that allows you to do a whole bunch of stuff like import,export the local GPO setting to and from a Domain Based GPO backup. This feature is great if you want to apply a domain based policy to a non-domain computer. It also allows you to export the local settings so that you can then import and compare it against a baseline in SCM v2.

A super cool new feature of this tool is the "GPOPack" options that allows you to create a self contained/extracting file that you can use to apply security setting to a computer. This can be very useful if you want to apply a security baseline during the build of a computer using WDS or a SCCM Task Sequence.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/06/image_thumb46.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/06/image46.png>)

**Note:** you will need to manual install this program from "C:\Program Files (x86)\Microsoft Security Compliance Manager\LGPO" after you have install the SCM v2 beta.

~~**Note2:** I cant seem to get the /GPOPack option to work. I have ~~[~~submitted a bug~~](<https://connect.microsoft.com/site715/feedback/details/677165/localgpo-wsf-gpopack-switch-does-not-work>)~~and will update when I get confirmation.~~

**Update:** To make the /GPOPack option to work you also need to use the /path and /export switch (see image below).

> LocalGPO.wsf /path:"c:\GPOPack" /export

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/06/image_thumb47.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/06/image47.png>)

Now you have exported the GPOPack you can apply it via a SCCM Operating System Task Sequence using the command line option. This is a great way to apply a security baseline to a computer if it is not destined to be domain joined"...

> GPOPack.wsf /silent

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/06/image_thumb48.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/06/image48.png>)

### Summary

Needless to say the product is beta and it may still have a few bugs"... however if you can put up with the fact that it may have some issues the reports that it can generate can be really valuable. So check out the beta by [Registering Here](<https://connect.microsoft.com/site715/InvitationUse.aspx?ProgramID=2663&InvitationID=SCM2-QCDB-CWPV>) and then download it at [SCM v2 Beta Download](<https://connect.microsoft.com/site715/Downloads/DownloadDetails.aspx?DownloadID=34361> "SCM v2 Beta Download") .