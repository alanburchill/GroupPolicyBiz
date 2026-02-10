---
title: "Group Policy Setting of the Week 26 &ndash; Do not automatically make redirected folders available offline"
date: 2010-05-16 20:00:00
author: admin
categories: ["Setting of the Week"]
tags: ["Offline Files"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/05/image_thumb12.png"
---

This weeks setting is called "Do not automatically make redirected folders available offline and can be found under User Configuration > Policies > Administrative Templates > System > Folder Redirections and will work with Windows XP or later. As the name suggest this prevents any users redirected folder from being made available for offline use which is enabled by default.

![image](https://www.grouppolicy.biz/wp-content/uploads/2010/05/image_thumb12.png)

This setting is particularly useful to configure on computers that are as used by multiple users as it eliminates the build up of multiple offline file caches on the hard drive. This is particularly important on Windows XP as all offline files try to synchronise even if the user does not have access to the files which causes file sync errors. The option also improves logon performance as it does not attempt a full offline sync of the cache when the user log's on for the first time.