---
title: "Windows 8 Group Policy Performance Troubleshooting Feature"
date: 2012-01-23 13:00:00
author: admin
categories: ["News"]
tags: ["GPResult", "Performance", "Report", "Troubleshooting", "Windows 8"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2012/01/clock_thumb.jpg"
---

[![clock](https://www.grouppolicy.biz/wp-content/uploads/2012/01/clock_thumb.jpg)](<https://www.grouppolicy.biz/wp-content/uploads/2012/01/clock.jpg>)One of the most common complaints I hear about Group Policy is that it make the log on slow"... Well.. I have been using the Windows Developer Preview of Windows 8 for a while now and I have only just discovered a cool new feature that might just help address this issue.

When you run a GPRESULT report on a computer you will now show the the time it take to process the individual components of Group Policy so you can much more easily determine what is making your computer run "SLOW"... If you notice under the "Component Status" section of the GPResult report it now lists the "Time Taken" to process the core Group Policy Infrastructure and each of the extensions. Now you can tell if it is actually group policy and/or one of the many, many, many, many".... many"... setting you apply to your computer that is slowing down your computer start up"...

TIP: Clicking on the blue date time will give you the "Processing Details" window.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/01/image_thumb2.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/01/image2.png>)