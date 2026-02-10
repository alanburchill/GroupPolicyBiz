---
title: "Windows 8.1 and Windows Server 2012 R2 Administrative Templates (ADMX)"
date: 2013-12-05 21:50:58
author: admin
categories: ["News"]
tags: ["ADML", "ADMX", "Windows 8.1", "Windows Server 2012 R2"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2013/03/COG.png"
---

![](https://www.grouppolicy.biz/wp-content/uploads/2013/03/COG.png)

Microsoft has just released the Administrative Templates (ADMX/ADML) files that allow you to configure their newest Group Policy Administrative Template setting for Windows 8.1 and Windows Server 2012 R2 on down level Operating Systems. To be clear this just enables you to edit the Group Policy objects on a down level computer, not make them apply.

To install both of these administrative template simply install them on the computer that you are editing the GPO's. Then the GPO's you edit from the computer will be automatically upgrade next time you open the via GP Editor.

This might seem fairly handy if you manage you group policy object from a Windows 7 computer. However, as always it is still "BEST PRACTICE" (yes i said the "B" word) to edit Group Policy Objects from the most recent OS in your environment.

**Note:** Also remember that the Internet Explore 11 administrator templates were also recently made available.

Internet Explorer 11 ADMX <http://www.microsoft.com/en-us/download/details.aspx?id=40905>

Windows 8.1 ADMX <http://www.microsoft.com/en-US/download/details.aspx?id=41193>