---
title: "How to configure and use &ldquo;Group Policy Update&rdquo; in Windows 8"
date: 2012-04-04 13:00:00
author: admin
categories: ["Tutorials"]
tags: ["Group Policy Update", "Intermediate", "Windows 8"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2012/04/image_thumb3.png"
---

"Group Policy Update" is a feature that allow IT admins to forcibly update group policy on all the computer in an OU. This feature works by creating a scheduled task on the workstations to run the gpupdate command within the next 10 minutes. This feature is fairly simple implementation with the GPMC console just scheduling the task to run remotely on any computer that is online at the time is run.

**Note:** This means if the computer is offline for any reason then they policy will not be updated on the computer.

I have mentioned this feature in my previous post [What's new with Group Policy in Windows 8](<https://www.grouppolicy.biz/2011/10/whats-new-with-group-policy-in-windows-8/>) but I have now updated the screen shots and added the required firewall configuration changes to enabled this feature.

### Firewall Prerequisites for Group Policy Update

Before this feature works you first need to configure the firewall to on all the remote client computers to allow GPMC to configure the remote task to perform the remote policy update. To configure this you need to make sure that this is done at least two hours in advanced to allow the policy changes to propagate.

The required firewall rules that need to be enabled on the client are:

  * Remote Scheduled Tasks Management (RPC)
  * Remote Scheduled Tasks Management (RPC-EPMAP)
  * Windows Management Instrumentation (WMI-IN)


**Step 1.** Edit a Group Policy Object that is targeted to the computer objects that you want to enabled this feature.

**Tip:** It is conceivable that you will want to create a new GPO linked at the domain level so that it will be enabled automatically for all computers but this is of course up to you.

**Step 2.** Open the policy to Computer Configurations>Policies> Windows Settings> Security Settings> Windows Firewall with Advanced Security then right click on Windows Firewall with Advanced Security and click on "New Rule"..."

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/04/image_thumb3.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/04/image3.png>)

**Step 3.** Click on "Predefined" option and then select the "Remote Scheduled Tasks Management" rule then click "Next"

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/04/image_thumb4.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/04/image4.png>)

**Step 4.** Now click "Next"

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/04/image_thumb5.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/04/image5.png>)

**Step 5.** Click "Finish"

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/04/image_thumb6.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/04/image6.png>)

Now repeat steps 2 to 5 and this time select the "Windows Management Instrument (WMI)" option.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/04/image_thumb7.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/04/image7.png>)

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/04/image_thumb8.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/04/image8.png>)

**Optional:** Now that you have enabled the firewall rules it is advisable that you go back and change the scope of the rule change to only apply in the Domain Profile. This ensures that these ports are now open when you are connect on a public or home network connection.

**Step 6.** Right click on the firewall rules and click on the Properties of the firewall rule.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/04/image_thumb9.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/04/image9.png>)

**Step 7.** Click on the "Advanced" tab and un-check the "Private" and "Public" profiles.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/04/image_thumb10.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/04/image10.png>)

Now repeat steps 6 and 7 for each of the 5 rules to make sure each rule only applies to the "Domain" profile.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/04/image_thumb11.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/04/image11.png>)

Now that the firewall rules are created you will need to wait at least 2 hours to ensure that rules have propagated"...

To confirm the settings have applied you can view the Firewall rules configured on the computer affected (see images below).

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/04/image_thumb12.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/04/image12.png>)

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/04/image_thumb13.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/04/image13.png>)

### How to perform Group Policy Update using GPMC

The following explains how to run the "Group Policy Update" against a group of computers.

**Step 1.** Open GPMC

**Step 2.** Simply right click on the OU that you want to perform the update on and click on the "Group Policy Update"..." option.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/04/image_thumb14.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/04/image14.png>)

**Note:** If there are no computers in the OU that you selected you will get this message (see image below).

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/04/image_thumb15.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/04/image15.png>)

You will now be information how many computers are about to affect. If you are concerned about what this do to your network load then of course make sure that only do this on a few computer at first and then ramp up when you become more confident that it will not grind you network to a halt.

**Step 3.** Click on "Yes"

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/04/image_thumb16.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/04/image16.png>)

You will now see the results of the Policy Update

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/04/image_thumb17.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/04/image17.png>)

To check that the Group Policy Update has been pushed out check the "Group Policy" scheduled task section.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/04/image_thumb18.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/04/image18.png>)

You will notice there are two scheduled task created, one for the computer the other for the user that is logged onto the computer.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/04/image_thumb19.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/04/image19.png>)

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/04/image_thumb20.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/04/image20.png>)

**Warning:** If the Group Policy Update that you are running asks for them to reboot of log off the computer then they will be prompted to log off.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/04/image_thumb21.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/04/image21.png>)

### How to perform Group Policy Update using Powershell

You can also run the Group Policy Update via a Power Shell command to target this command against a single computer. You could then use this command with other PowerShell commands to apply it to all computers in an OU or even a domain.

The command "Invoke-GPUpdate" also enables a few more options such as running the Group Policy Update with the "“boot "“force or "“logoff options.

**TIP:** You need to run the "Import-Module GroupPolicy" before the "Invoke-GPUpdate" command.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/04/image_thumb22.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/04/image22.png>)

As always be careful before making any changes in your environment"... If the changes you are making to the computer can possibly have a large load on the network then running this command could potentially cause a lot of performance issues for your network.

That being said it is still nice to have this feature at your disposal in case there is a setting that you need to push out an change quickly"...

Additional Reference See: <http://technet.microsoft.com/library/hh831791.aspx>