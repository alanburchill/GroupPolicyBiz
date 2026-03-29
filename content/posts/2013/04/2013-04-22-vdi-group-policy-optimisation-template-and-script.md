---
title: "VDI Group Policy Optimisation Template and Script"
date: 2013-04-22 03:20:57
author: admin
categories: ["Tutorials"]
tags: ["VDI"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2011/11/ximage_thumb.png.pagespeed.ic.ynV-y0xXTT.png"
---

![](https://www.grouppolicy.biz/wp-content/uploads/2011/11/ximage_thumb.png.pagespeed.ic.ynV-y0xXTT.png)Continuing on with my [last post](<https://www.grouppolicy.biz/2013/04/what-services-to-disable-to-optimize-windows-for-vdi/>) about optimising VDI guest services based on the [Optimizing Windows 8 for Virtual Desktop Infrastructure](<http://channel9.msdn.com/Events/MMS/2013/DV-B308>) session at MSS I have now created a Group Policy Object that performs all the services, registry and other customisations that was mentioned in the session.

So.. What I have done is taken Carl Luberti and Jeff Stokes [Windows 8 VDI optimisation script](<http://blogs.technet.com/b/jeff_stokes/archive/2013/04/09/hot-off-the-presses-get-it-now-the-windows-8-vdi-optimization-script-courtesy-of-pfe.aspx>) and then removed all the section that can be implemented by Group Policy i.e. registry keys, services, power settings and control panel settings. What this means is that you can now run the optimisation script on you VDI guest computers after they have been built and then have most of the settings re-apply if necessary at each group policy refresh. Meaning that users making changes to your VDI guest will not be able to configure their computer that undo's your optimisation changes. This would be most useful for you persistent VDI guest computers where the configuration of the computers can change over time.

Below is a setting report of the setting in the GPO policy

Download the zip backup of GPO below and then import it into your VID Group Policy object.

Then run this script on you VDI image before it is sys preped and then link to GPO to the computers where they are in AD.

**__Warning:__** I have conducted limited testing on this group policy object. As always be sure to test it thoroughly before you implement it in your environment.

**Update:** The original VDI Optimisation script is based upon one generated VDI Optimizer tool by Jonathan Bennett at <http://www.autoitscript.com/site/autoit-tools/vdi-optimizer/>