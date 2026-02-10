---
title: "Group Policy Setting of the Week 27 &ndash; Turn off numerical sorting in Windows Explorer"
date: 2010-05-30 22:54:45
author: admin
categories: ["Setting of the Week"]
tags: ["Basic", "Group Policy", "Literal Sort", "Windows 7", "Windows Explorer"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/05/image_thumb27.png"
---

In this weeks setting I look at a new Windows 7 setting that reverts the sort order of folders back to the old way it would sort files and folder the same as Windows 2000 (and earlier). This policy setting is called "Turn off numerical sorting in Windows Explorer and can be found under User Configuration > Policies > Administrative Templates > Windows Components > Windows Explorer.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/05/image_thumb27.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/05/image26.png>)

As you can see from the "Numerical Sorting" example below the folder list will sort based on the numerical value of the folder name. This means that a single digit number will be ordered higher than a two or more digit number when sorting alphabetically.

Numerical Sorting (Setting Disabled or Not Configured)

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/05/image_thumb28.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/05/image27.png>)

If you take a look at the Literal Sorting example you can see that the number "10" is in position 2 because the sorting is treating the number as a literal text. You can get around this sorting problem by padding with zero's however you need to add enough zero's to match the same number of digits as the largest number.

Literal Sorting (Setting Enabled) |  Literal Sorting with padded Zero's (Setting Enable)
---|---
[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/05/image_thumb29.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/05/image28.png>) | [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/05/image_thumb30.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/05/image29.png>)

While it is unlikely that you will need to turn this on for all users in your organisation it is possible that you have some folder on your file server that have been created in such a ways that the new view method would cause a problem. Obviously in this case you would need to consider carefully if you just need to turn this on for [selected users](<How to apply a Group Policy Object to individual users or computer>).