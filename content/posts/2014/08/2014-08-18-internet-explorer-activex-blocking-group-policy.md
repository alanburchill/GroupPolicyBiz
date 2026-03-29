---
title: "Internet Explorer ActiveX Blocking Group Policy"
date: 2014-08-18 12:15:00
author: admin
categories: ["News"]
tags: ["ActiveX", "Internet Explorer 11"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2014/08/IE9answer_thumb.png"
---

[![IE9answer](https://www.grouppolicy.biz/wp-content/uploads/2014/08/IE9answer_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2014/08/IE9answer.png>)Microsoft has just released a patch MS14-051 (<https://support.microsoft.com/kb/2976627>) for Internet Explore on Windows 7 and Windows 8 that allows IT Admins to block out of date ActiveX controls from running in the browser. This move aligns IE with other browsers that actively block out of date version of plug-ins such as Java but is still very similar to the ActiveX kill list that Microsoft used to issue to block controls with known vulnerabilities. The key difference with this change is that it now uses an XML configuration file (see [here](<https://iecvlist.microsoft.com/ie11blocklist/1401746408/versionlist.xml>)) to publish what controls are out of date rather than hard coding them into a patch. Interesting to note that while the name of blog post and update specifically say this is a ActiveX blocking update it is currently only going to be configured to block out of date versions of Java. Of course having and XML configuration file also means that Microsoft can also use the same mechanism for blocking other out of date controls (Flash, Silverlight etc) in the future. It is also good to know that this change does *NOT* apply to web sites that are configured to run in the Intranet Zone or Trusted Zones meaning that all your our of date ActiveX controls you run on your intranet are not affected by this change. In addition to this Microsoft has now said they will give a grace period before they block the controls until September 9th. To manage this new security feature Microsoft has also create four new group policy settings under Administrative Templates > Windows Components > Internet Explorer > Security Features > Add-on Management

  * Turn on ActiveX control logging in Internet Explorer
  * Remove Run this time button for outdated ActiveX controls in Internet Explorer
  * Turn off blocking of outdated ActiveX controls for Internet Explorer on specific domains
  * Turn off blocking of outdated ActiveX controls for Internet Explorer

For more details on these setting check out <http://technet.microsoft.com/en-us/library/dn761713.aspx> To get these new Group Policy setting for your organisation you either need to install the MS14-051 update on the computer that you edit your GPO's on OR you need to download the ADMX files from [htp://www.microsoft.com/en-us/download/details.aspx?id=40905](<http://www.microsoft.com/en-us/download/details.aspx?id=40905> "http://www.microsoft.com/en-us/download/details.aspx?id=40905") and update your Group Policy Policydefenitions central or local store. Additional Reference: <http://blogs.msdn.com/b/ie/archive/2014/08/06/internet-explorer-begins-blocking-out-of-date-activex-controls.aspx>