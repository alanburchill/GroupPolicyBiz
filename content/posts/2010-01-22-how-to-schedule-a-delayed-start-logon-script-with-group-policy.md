---
title: "How to schedule a delayed start logon script with Group Policy"
date: 2010-01-22 01:15:39
author: admin
categories: ["Best Practice", "Tutorials"]
tags: ["Group Policy Preferences", "Intermediate", "logon", "scheduled task", "scripts", "SOE"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb91.png"
---

Logon Scripts!!! I hear you yelling at me about why I am doing a tutorial about logon scripts when Group Policy Preferences is supposed to allow me to stop using my logon scripts. Well in a utopian world there would be no logon scripts to maintain however there are still some situations that you might have to execute a program at logon. One example I recently saw on the [Group Policy Forums](<http://social.technet.microsoft.com/Forums/en-US/winserverGP/threads>) was a person who wanted a way to delay the launching of the browser so as to not add additional delay to the users logon to what was already a slow computer. Somewhat similar to the Delay Start option for services that was introduced in Windows 7.

Prerequisites: This is a Windows Vista+ configuration as Windows XP has a more limited scheduling engine. If you really want to do this via Windows XP (sucks to be you) you could run the script with some delay/timeout third party tool in it and just have it run from the users "Startup" start menu folder"...

**Step 1.** In a Group Policy Object (GPO) that you have targeted at all the users (or most of them) that you want the delayed start program/action to run on go to "Users Configuration" > "Preferences" > "Scheduled Task" then go "Action" > "New" > "Scheduled Task (Windows Vista and later)". Then type the display name of the script in the "Name" field (see image 1) and click on the "Triggers" tab.

Note: In this example we are just going to be running a command prompt so the Name is "CMD.exe".

[![Image 1: Scheduled Task Properties](https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb91.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image96.png>)

**Image 1: Scheduled Task Properties**

**Step 2.** On the Triggers tab click the "New" button". Change the "Begin the task" drop down option to "At log on" and then tick "Delay task for:" and configure the delay from the pop down menu (see image 2). Then click "OK"

Note: Unfortunately this option does not seem to be user configurable so for the use of a logon script "30 seconds" and "1 minute" are the only practical options.

[![Image 2: New Trigger](https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb92.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image97.png>)

**Image 2: New Trigger**

**Step 3.** You should now have the trigger configured for your event that looks like the image below (see image 3). Now click on the "Actions" tab.

[![Image 3: Configured Trigger](https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb93.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image98.png>)

**Image 3: Configured Trigger**

**Step 3.** In the "Actions" tab click on the "New" button and then configure the action you want to take. Again in this example we are just going to be running a command prompt so configure the "Action" to "Start a program" (see image 4).

Note: You can also use this option to send and e-mail or even display a pop-up message to the users. Very handy if you used to use the "net send" program in Windows XP before Service Pack 2 as it was disabled due to security issues.

[![Image 4: New Action](https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb94.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image99.png>)

**Image 4: New Action**

**Step 4.** Configure the "Program/Script" to run to "C:\Windows\system32\cmd.exe" then click "OK" (see image 5).

[![Image 5: New Action](https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb95.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image100.png>)

**Image 5: New Action**

**Step 5.** Click "OK" (see image 6)

[![Image 6: Actions Tab](https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb96.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image101.png>)

**Image 6: Actions Tab**

Now you are done. The task is scheduled and it will be pushed out to all your users at the new Group Policy refresh. (see image 7).

Note: If you don't want this to apply to all your user accounts you can also use Group Policy Preferences targeting options to refine the targeting.

[![Image 7: Scheduled Tasks](https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb97.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image102.png>)

**Image 7: Scheduled Tasks**

Below is the view of the scheduled task as configured on the computer (see image 8,9 & 10).

Note: The settings tab are greyed out because it is being controlled by Group Policy.

[![Image 8: Scheduled Tasks General Tab](https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb98.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image103.png>)

**Image 8: Scheduled Tasks General Tab**

[![Image 9: Scheduled Tasks Triggers Tab](https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb99.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image104.png>)

**Image 9: Scheduled Tasks Triggers Tab**

[![Image 10: Scheduled Tasks Actions Tab](https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb100.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image105.png>)

**Image 10: Scheduled Tasks Actions Tab**