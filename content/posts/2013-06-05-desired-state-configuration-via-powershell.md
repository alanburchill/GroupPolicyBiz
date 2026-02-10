---
title: "Desired State Configuration via Powershell"
date: 2013-06-05 22:49:34
author: admin
categories: ["News"]
tags: ["Desired State Configuration", "Powershell"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2013/06/powershell_thumb.jpg"
---

[![powershell](https://www.grouppolicy.biz/wp-content/uploads/2013/06/powershell_thumb.jpg)](<https://www.grouppolicy.biz/wp-content/uploads/2013/06/powershell.jpg>)At TechEd North America 2013 the Powershell team have showcased a new under the covers feature with Windows 8.1 and Server 2012 R2 call Desired State Configuration via Powershell. While you may recognise this feature name as something out of that is in System Center Configuration Manager the technology is somewhat different and has no SCCM requirements.

Simply put DCS via Powershell allows you to apply a configuration to a computer and have that configuration re-applied on a schedule. Now if you are thinking that this sounds a big like Group Policy you would be right"... But as I see it because this is PowerShell you are pretty much unlimited by what settings and configuration you can apply via this method. An example of this was demo that was shown on stage at TechEd they were installing the IIS feature on windows and then configured the web server via a custom "resource". It would seem that these "resources" are custom function that are used to configure your computer specific features.

While some of the details of this feature still seem a little vague it does show great promise of a way to really powerful to configure a large number of system at scale but not within the pre-defined constraints of Group Policy. I just hope that they enable a way to apply these DCS scripts with the pre-existing targeting features of Group Policy so people can leverage their existing Organisational Unit structure to apply these scripts.

For another view of this feature I would check out [Darren Mar-Elia](<http://sdmsoftware.com/>) blog post at <http://sdmsoftware.com/group-policy/desired-state-configuration-in-windows-8-1-and-group-policy/>

Source: <http://channel9.msdn.com/Events/TechEd/NorthAmerica/2013/MDC-B302#fbid=DPdjjFNcril>