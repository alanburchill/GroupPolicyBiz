---
title: "Edge Group Policy Settings"
date: 2015-07-08 09:21:04
author: admin
categories: ["News", "Tutorials"]
tags: ["Basic"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2015/07/EdgeLogo-150x150.jpg"
---

[![EdgeLogo](https://www.grouppolicy.biz/wp-content/uploads/2015/07/EdgeLogo-150x150.jpg)](<https://www.grouppolicy.biz/wp-content/uploads/2015/07/EdgeLogo.jpg>)With the release of Windows 10, Microsoft has now also released their new web browser call Edge. This browser will be installed side Internet Explore by default on most installs of Windows 10. This is essentially a new browser that has been mostly re-built from the ground up for improved security, performance and HTML compatibility. But unlike its distant cousin browser ( IE ) that had over 1600 native Group policy settings. The new Edge browser currently only has 10 (ten) unique Group Policy settings. These Edge Group Policy Settings can be found under (User or Computer)\Administrative Template\Windows Components\Microsoft Edge\ are:

  * Allows you to run scripts, like Javascript
  * Allows you to let people use autofill on websites
  * Allows you to let people send Do Not Track headers
  * Allows you to configured password manager
  * Allows you to run pop-ups
  * Stops address bar from showing search suggestions
  * Allows you to configure SmartScreen
  * Configure how Microsoft Edge treats cookies
  * Allows you to configured the Enterprise Site list
  * Sends all intranet traffic over to Internet Explorer

While most of the settings sem straight forward I would call out the last policy settings called "Sends all intranet traffic over to Internet Explore". This policy setting is very similar to the "Chrome Legacy Browser Support" which redirect users web traffic to Internet Explorer if the web site needs is located on the Intranet. This will allow your users to use Edge for any external web sites but then drop back to the more Intranet friendly Internet Explorer when they visit any internal web sites. Now I can already hear you say that only ten group policy settings does not seem like many. However, the key things to remember is that this is a new browser and Microsoft has said at the recent Ignite conference that more group settings will be coming. This also combine with the fact that the new Edge browser has far fewer settings and that it treats all web sites as "Internet" zones there is simply far fewer settings that need to be configured. Another thing to also remember is that InTune will also soon be updated to configured similar policy settings for the Edge browser. This essentially allows you to also manage the Edge Browser on all your non-domain joined computers as well. Either way new Edge browser can be managed via Group Policy or InTune, so if you are thinking about deploying Windows 10 in your organisaion you certainly have options to manage Microsoft's newest browser.