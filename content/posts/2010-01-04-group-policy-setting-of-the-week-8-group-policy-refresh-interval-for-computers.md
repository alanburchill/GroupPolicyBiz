---
title: "Group Policy Setting of the Week 8 "“ Group Policy refresh interval for computers"
date: 2010-01-04 13:52:40
author: admin
categories: ["Setting of the Week"]
tags: ["Basic", "Group Policy"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb70.png"
---

This weeks (and first for the year) Group Policy Setting of the Week is a Group Policy setting that configures Group Policy. The "Group Policy refresh interval for computers" can be found under Computer Configuration > Policies > Administrative Templates > System > Group Policy and is used to control how often the background computer refresh interval of a performed. [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb70.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image72.png>) By default the refresh will happen every 90 minutes however it has a 30 minute random offset so it could potentially take between 1 to 2 hours for a policy refresh to occur. Keep in mind however that if configured the policy refresh to a shorter interval it will potentially not take affect to all your computers until the longest refresh interval of the last refresh interval setting. Normally this setting it set to a short interval before a major change to group policy setting is made to an SOE so that any rollback of the change can be implemented faster (example see [How to use Group Policy Preferences to set change Passwords](<http://abskb.spaces.live.com/blog/cns!8834054641A09100!1071.entry> "http://abskb.spaces.live.com/blog/cns!8834054641A09100!1071.entry")).