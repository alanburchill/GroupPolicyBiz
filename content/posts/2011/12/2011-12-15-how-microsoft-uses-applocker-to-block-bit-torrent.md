---
title: "How Microsoft uses AppLocker to block Bit Torrent"
date: 2011-12-15 13:27:00
author: admin
categories: ["News"]
tags: ["AppLocker", "Case Study", "Deployment", "Microsoft"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2011/12/image_thumb5.png"
---

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/12/image_thumb5.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/12/image5.png>)Microsoft has just released a report (see [AppLocker Deployment at Microsoft](<http://www.microsoft.com/download/en/details.aspx?id=28372&WT.mc_id=rss_alldownloads_all> "http://www.microsoft.com/download/en/details.aspx?id=28372&WT.mc_id=rss_alldownloads_all")) describing the process they used to implementation of AppLocker via Group Policy. This was done to so that Microsoft would maintaining compliance with the U.S. Digital Millennium Copyright Act ([DMCA](<http://en.wikipedia.org/wiki/Dmca>)) by preventing all their computers from running P2P software.

The report shows that after they fully rolled out the AppLocker policy setting the number of P2P cases dropped to nearly 0%. It was also interesting that the report noted that there was not a single support call regarding AppLocker for all 200,000 computers when the settings were rolled out.

> Not a single support call for an AppLocker-related problem has occurred.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/12/image_thumb6.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/12/image6.png>)

This document focus's more on the process for testing and deployment of AppLocker in a large environment rather than the exact technical steps. I assume what made this a lot easier for Microsoft is that the most popular BitTorrent clients [uTorrent](<http://www.utorrent.com>) is a digitally signed program. This makes it a lot easier for AppLocker to identify the application as it only need to look at the digital signature to determine if the program should be blocked. Meaning that they do not have to constantly update the Group Policy setting with a new hash value whenever a new version of the client is released.

[![clip_image001](https://www.grouppolicy.biz/wp-content/uploads/2011/12/clip_image001_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/12/clip_image001.png>)

Personally I certainly think BitTorrent software has a legitimate and legal place. For example check out [The Tunnel Movie](<http://www.thetunnelmovie.net/>) which was a full length movie that was released freely using BitTorrent. Rather ironically Windows has its P2P service built-in called [Background Intelligent Transfer Service](<http://msdn.microsoft.com/en-us/library/windows/desktop/bb968799\(v=vs.85\).aspx>) (BITS) which is used for distributing software updates to computers efficiently over WAN and LAN links.

However this is still good case study at the process you need to take to rollout AppLocker to prevent users from running particular programs that say may not be a secure version. e.g. Adobe Reader v9 see <http://blog.stealthpuppy.com/virtualisation/dont-virtualize-adobe-reader-x/>).

If you are interested for instructions for using AppLocker then check out my other blog post [Best Practice: How to configure AppLocker Group Policy in Windows 7 to block third-party browsers](<https://www.grouppolicy.biz/2010/04/how-to-configure-applocker-group-policy-in-windows-7-to-block-third-party-browsers/>)