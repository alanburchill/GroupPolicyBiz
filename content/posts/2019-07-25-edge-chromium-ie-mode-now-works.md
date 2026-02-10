---
title: "Edge Chromium IE Mode Now Works"
date: 2019-07-25 01:17:05
author: admin
categories: ["News", "Tip"]
tags: ["Chromium", "Edge", "Enterprise", "IE Mode", "Internet Explorer 11"]
featured_image: "/uploads/2019/07/Edge-Logo.png"
---

In the past few weeks there has been a lot of post about the new Enterprise features coming with the new Edge Chromium version of the browser. Unfortunately the main feature that enterprises were waiting for did not work... until today.

One of the key new policy setting that came with the Edge 77 ADMX/ADML files is called "Configure Internet Explorer integration". This setting can be found under "Administrative Settings\Microsoft Edge". What this policy enabled, in conjunction with other settings, was the ability to enable IE mode for Edge.

While IE Mode for original Edge has always been a thing, this new version is designed to launch Internet Explorer in another tab of the current browser. Meaning users only had to go to another tab of Edge to see a site running in IE Mode. This was opposed to how the original IE Mode worked in Edge where it would launch a full copy of IE in another window.

![](http://www.grouppolicy.biz/wp-content/uploads/2019/07/Configure-Internet-Explore-intergration-800x742.png)Configure Internet Explorer intergration

This new integrated IE tab in Edge Chromium is a far more pleasing user experience as the only visual difference now is a small IE logo in the address bar (see below).

![](http://www.grouppolicy.biz/wp-content/uploads/2019/07/Chromium-IE-Mode-800x566.png)

So IT admins could finally allow users to give users both a compatible and modern experience without having to having to using a dual browser environment. While the combination of Traditional Edge / IE was something I talked about at Ignite 2017 (see [https://](<https://channel9.msdn.com/events/Ignite/Australia-2017/WIN342?term=burchill&lang-en=true>)[channel9.msdn.com](<https://channel9.msdn.com/events/Ignite/Australia-2017/WIN342>)[/events/Ignite/Australia-2017/WIN342](<https://channel9.msdn.com/events/Ignite/Australia-2017/WIN342?term=burchill&lang-en=true>) ) it still was a far from ideal solution.

The problem was, in first release of v77 of Edge Chromium this feature did not fully work. IE Mode would still open in a separate windows similar to how the original IE mode worked.

Since then I have had feedback from Microsoft and they have confirmed that it was being fixed.

" We want to let you know that we fixed an issue that's related to this feedback in an upcoming update to Microsoft Edge. "

Well, we did not have to wait long and as of today Edge Chromium Dev Channel version 77.0.223.0 has been fixed and IE Mode will now work as expected. Now you can run all your old "important" work related web sites without having to run them in a different window (see below).

![](http://www.grouppolicy.biz/wp-content/uploads/2019/07/Chromium-IE-Mode-SJ-800x621.png)Edge Chromium running IE Mode for the Space Jam web site

But serious, this is a fantastic feature that should remove a lot of barriers for most origination use Edge Chromium as a single browser strategy once it is released.

See <https://docs.microsoft.com/en-us/DeployEdge/edge-ie-mode> for more information on how to implement IE Mode for Edge Chromium.