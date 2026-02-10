---
title: "What&rsquo;s changed with the Group Policy Client Service in Windows 8"
date: 2012-04-19 13:46:00
author: admin
categories: ["Tutorials"]
tags: ["AOAC", "Group Policy Client", "Services", "Windows 8"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2012/04/image_thumb25.png"
---

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/04/image_thumb25.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/04/image25.png>)With the release of Windows 8 Microsoft has gone back and worked on the fundamentals of the OS to make it more efficient than even Windows 7. This means that the OS does the same (if not more) using less system resources. One of the ways that they achieve this is the way they control the "Group Policy Client" service to only run when required. This "Always On Always Connected" (a.k.a. AOAC) optimization of the service manages basically means that the service shuts down when ever it is not being used thus not using any idle ram or CPU cycles.

So in this post I will take a deeper look at this new AOAC optimisation actually works "...

Firstly the most obvious change you may notice that the Group Policy Client Service will normally not be running. This is entirely fine and there is no reason to worry that the service is not running"...

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/04/image_thumb26.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/04/image26.png>)

So when a computer does a Group Policy Refresh the Group Policy Client service will start on demand to process the policy update and then stay running for 5 minutes (see image below). This 5 minute delay shutdown is to avoid having to load and unload the service is you are performing multiple GPUPDATE'S in quick succession say for testings"...

**Note:** This service also starts on demand when you perform a GPUPDATE or a remote [Group Policy Update](<https://www.grouppolicy.biz/2012/04/how-to-configure-and-use-group-policy-update-in-windows-8/>).

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/04/image_thumb27.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/04/image27.png>)

This service start up is probably going to be sub 1 second any way on most systems it is not an impact you are likely to see.

So you might wounder then how it is still doing its background refresh of the Group Policy if the service is no longer running".... The answer is Scheduled Tasks. Rather than having the service sit idle and check periodically to see if it need to run a schedule task is created for the next time the service need to perform a refresh. But".... Jumping into the schedule tasks Group Policy section will NOT show this however as it is scheduled as the "SYSTEM" account.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/04/image_thumb28.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/04/image28.png>)

However if you use the [PSEXEC](<http://technet.microsoft.com/en-us/sysinternals/bb897553>) tool to run as "SYSTEM" you can see this task in the task scheduler"...

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/04/image_thumb29.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/04/image29.png>)

If you take a look at the history of this task you will see that the task is deleted and a new one is registered during each policy update"...

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/04/image_thumb30.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/04/image30.png>)

This AOAC optimization behaviour of the Group Policy Client service is only seen on the workstation version of Windows 8 and in Windows Server 2012 the service will stay running as per normal. If you want this service to stay on all the time like it did before then you can do this by enabling the "Turn off Group Policy Client Service AOAC optimization" policy found under Computer Configuration > Policies > Administrative Templates > System > Group Policy.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/04/image_thumb31.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/04/image31.png>)

However this new optimization is pretty much and all Pro and No con's change and I am hard pressed to wounder why you would ever want to revert this behaviour"...