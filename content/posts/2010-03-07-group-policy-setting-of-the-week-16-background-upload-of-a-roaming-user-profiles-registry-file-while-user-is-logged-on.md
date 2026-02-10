---
title: "Group Policy Setting of the Week 17 "“ Background upload of a roaming user profile's registry file while user is logged on"
date: 2010-03-07 16:00:00
author: admin
categories: ["Setting of the Week"]
tags: ["Background", "Basic", "Profile", "roaming profile", "Windows 7"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb13.png"
---

Another one"...? yes"... Another roaming profiles group policy for this weeks setting of the week. But this is a really super cool policy I found while reading the "[What's New in Folder Redirection and User Profiles](<http://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=7ffc1f61-f63b-4250-9d30-e44ca824b651>)" (via [@stealthpuppy](<http://www.twitter.com/stealthpuppy>) ) document that Microsoft recently published. This document mainly goes through the new features with folder redirections in Windows 7 however it also mentions the new group policy/feature called "Background upload of a roaming users profile's registry file while user is logged on". This setting can be found under Computer Configuration > Administrative Templates > System > User Profiles and is specific to Windows 7 or Windows Server 2008 R2. [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb13.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image13.png>) This policy setting would be very useful as a way to ensure that at least part of a users profile is save to the network if they are they type that never like to log off their computer at night. There are a few points about this policy which I have summarised below:

  * Only synchronises the users registry profile (ntuser.dat) so things like desktop icons and favourites wont sync. (This is what folder redirection is for any way).
  * There are two modes of scheduling the update
    * Run at set interval "“ Between 1 hour and 720 hours (30 days).
    * Run at specified time of day "“ useful if you only want to run this at 3am so that it only applies to users who stay logged on over night.
  * The schedule will run randomly any time up to an hour after it is supposed to run so to not load the file server with a large number of concurrent requests.
  * If you choose one method of scheduling then it will ignore the set value of the other schedule.

I also have a very strong suspicion that this setting is only compatible if you have Windows 2008 (or later) as the file server so that it can handle the copying of the locked file (ntuser.dat). Please ping me if you can confirm this.