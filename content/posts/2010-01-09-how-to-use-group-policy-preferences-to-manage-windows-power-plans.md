---
title: "How to use Group Policy Preferences to manage Windows Power Plans"
date: 2010-01-09 12:54:01
author: admin
categories: ["Best Practice", "Tutorials"]
tags: ["Advanced", "Group Policy Preferences", "Power Plan", "Windows"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/01/image1_thumb.png"
---

One of the new feature of Group Policy Preferences in Windows 7 and Windows Server 2008 R2 is support for configuring power plans using preferences for Windows Vista and later (see Image 1). You used to be able to control power management in Vista using native policies however the advanced targeting of preferences now enables lot of new scenarios with power savings. AWSOME!

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/01/image1_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image1.png>)

****

****

****

****

****

****

****

****

****

****

****

****

****

****

****

****

****

****

****

**Image 1. Creating a new Windows Vista and Later Power Plan**

One of the really neat things that you can do with Group Policy Preferences (GPP's) and Targeting is change the power scheme of a computer based on the time of the day and the day of the week. This allows you to apply more aggressive power plans to your workstations after hours but then then back off during the day when people are working. Even though that Windows Vista (and Windows 7) support adaptive display time out which backs off the screen saver timeout when a user is still sitting at a computer but not actively using it they still have to wake up the computer by before the timeout started to back off. Applying the less aggressive power plan during working hours means that the user is less likely to have to keep waking up their computer in the first place as you have configured longer time out values.

Now if this sounds familiar you'd be right as I did demo some of this during my TechEd Australia Group Policies session that I did with Lilia Gutnik and it is similar to the [TechNet Edge video](<http://edge.technet.com/Media/Power-Management-and-Troubleshooting-Group-Policy/>) by Michael Kleef and Mark Gray. But in this article I am going to diving a lot deeper than my demo or in the TechNet Edge video.

So before we talk about how to do this first lets go over what we are trying to achieve. We are assuming you manage a fleet of workstations that are only used during standard business hours and afterhours you want the computers to go to use as little as power as possible. You want to apply different power plans to the computers not only based on the day of the week but also the time of the day to make sure you get maximum possible power savings (see Image 2).

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image.png>)

**Image 2. Example power plan timetable**

So to do this we setup two separate power plans, with one that is applied by default all the time and the other one that will take precedence and apply during business hours.

**How to setup the Default Power Plan Policy**

Step 1. Create a Power Plan under the User Configuration option of a GPO that has has aggressive power savings configured without any targeting other than being applied to all the users you want to control the power plans. I will leave the exact details of the power plan up to you but I will recommend that if you are going to set the "Sleep" timeout for Windows Vista (or greater) then make sure you also enable the "Allow hybrid sleep" option (even on your desktops) (see Image 3.) as this will protect your computers from data loss if you lose power to your office environment afterhours.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb1.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image2.png>)

****

****

****

****

****

****

****

****

****

****

****

****

****

****

****

****

****

****

**Image 3. Enable hybrid sleep mode**

Step 2. Rename the item to be called something like "Default Power Plan" (see Image 4) and also make sure that it is always set to order number one.

WARNING "“ If you do this make sure you either immediately disable the item (tool bar > red circle "disable this item") or setup the Business Hours Power Plan straight away so that you don't start shutting down all your computer during the middle of the day.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb2.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image3.png>)

**Image 4. Default Power Plan at Order 1**

**How to setup the Business Hours Power Plan Policy**

Step 3. Create another Power Plan setting item called "Business Hours Power Plan" (see Image 5.) making sure it is lower order than the default power plan. Again I will leave the exact settings up to you but this one should be less aggressive than your default power plan.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb3.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image4.png>)

**Image 5. Business Hours Power Plan**

Step 4. Now go into the properties of the "Business Hours Power Plan"

Step 5. Click on the Common Tab and tick "Item-Level Targeting"

Step 6. Click on the targeting button

First of all we are going to create a collection that will target the Business House Power Plan to only the weekdays of the week.

Step 7. In the targeting Editor click on "Add Collection" (see Image 6.)

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb4.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image5.png>)

**Image 6. Creating a targeting collection**

Step 8. Click on the "New Item" and then click on "Date Match" (see Image 7 & 8.)

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb5.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image6.png>)

**Image 7. Creating a Date Match rule**

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/01/image27_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image27.png>)

****

****

****

****

****

****

****

****

****

****

****

****

****

****

****

**Image 8. Date match rule before being dragged into a Collection**

Step 9. Now you will need to drag the "AND the day of the week is Sunday" onto the "the collection is true" and change the day to "Monday" (see Image 9.)

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb6.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image7.png>)

**Image 9. Date Match rule after being dragged in the collection.**

Step 10. Now make sure that "the day of the week is Monday" is highlighted and click CTRL-C once and CTRL-V four times to copy and paste the date match rule once for each weekday (see Image 10).

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb7.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image8.png>)

**Image 10. Five date match rules in one collection**

Step 11. Now click on each of the "AND the day of the week is Monday" and press F6 to change each date match rule from and "AND" to a "OR" and then change the days to Tuesday , Wednesday, Thursday and Friday (see Image 11).

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb8.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image9.png>)

**Image 11. Data Range Collection configured to apply only during weekdays**

Now we will add a Time Range option that will refine when we target the Business House Power Plan to just working hours of the weekdays.

Step 12. Click on the "this collection is true" and then click on "New Item" and then click on "Time Range" (see Image 12).

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb9.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image10.png>)

**Image 12. Adding Time Range to targeting**

Step 13. Now configured the time range to when during the day you want to Business Hours Power Plan to apply (see Image 13).

Note - Make sure you allow for the policy refresh interval (default 90 minutes with a 20% random offset) when configuring the start and end time. This means you might want to start applying the policy 2 hours before the start of business (e.g. 6:30am) to make sure all the computers are configured with the Business Hours Power Plan before people login in the morning (e.g. 8:30am).

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb10.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image11.png>)

**Image 13. Targeting configured with Date Range collection and a Time Range**

Now you have configured a Group Policy Preference to apply less aggressive power plans to your computer during business hours while still having more aggressive power plans applied after hours.

**Other Option - More user Control**

In the example above we just modified the "Balanced" power plan setting when we wanted to make changes to the power settings. If you did not want to give your users some more control and not force specific power plans you could just select the "High performance" plan and tick "Set as the active power plan" for the Business Hours Power Plan (see Image 14) and the "Power Saver" plan as active in the Default Power plan (see Image 15).

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb11.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image12.png>)

**Image 14. Setting the High Performance plan as active**

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb12.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image13.png>)

**Image 15. Setting the Power Saver plan as active**

This way your users can still configure each of the power plans to their own preference but you will still make sure that the "Power Saver" plan will be applied to your computers after hours. However as you are only setting which plan is active then your users could get around the power plan as by configure both plans to never time out thus negating the benefit of any of the plan's.

**Other Options "“ Less aggressive Default Power Plan**

You may also want to set the default power policy to be less aggressive by default and then apply the aggressive power as the second item in the list using a little more complicated targeting (see Image 16). The advantage of this method is you can easily turn off the aggressive power savings plan when you want to do afterhours by just disabling the "Afterhours Power Plan".

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb13.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image14.png>)

**Image 16. Targeting to apply plan only afterhours**