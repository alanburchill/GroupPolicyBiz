---
title: "How to manage Windows Firewall settings using Group Policy"
date: 2010-07-21 13:00:00
author: admin
categories: ["Best Practice", "Tutorials"]
tags: ["Export", "Firewall", "Import", "Intermediate", "Security"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/07/Firewall_thumb.png"
---

In this article I am going to talk about how you can use Group Policy to control the firewall that comes out of the box with Windows but first I want to give you a bit of history of the evolution of host based firewall in Windows. [Firewalls](<http://en.wikipedia.org/wiki/Firewall_\(computing\)>) have long been around for year protecting internal corporate networks from outside attackers (see image below).

[![Firewall](https://www.grouppolicy.biz/wp-content/uploads/2010/07/Firewall_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/Firewall.png>)

With the explosion of mobile workers in the late 90's more and more people were connecting their laptops directly to the internet without the benefit of protection of a corporate firewall. As a result back in the early 2000's third-party firewall products such as [ZoneAlarm](<http://en.wikipedia.org/wiki/ZoneAlarm> "http://en.wikipedia.org/wiki/ZoneAlarm") became a very popular way to security against attacks. Microsoft then added a host based firewall with the release of Windows XP/2003 that was unfortunately turned off by default. As a result of having the firewall turned off by default in there were a number of [computer worms](<http://en.wikipedia.org/wiki/Computer_worm>) of which most notably were the [Blaster worm](<http://en.wikipedia.org/wiki/Blaster_\(computer_worm\)>) and [Sasser worm](<http://en.wikipedia.org/wiki/Sasser_\(computer_worm\)>) that spread like wildfire to pretty much any Windows computer that had not been specifically secured.

As a result Microsoft decided to make a major change with how Windows XP was configured with the release of Service Pack 2. When users installed service pack 2 they were now prompted to turn on the firewall thus protecting them from malicious communications. The problem with enabling a firewall however is that you generally block all incoming traffic by default which means product such as Skype and/or Windows Messenger could no longer receive incoming call's or messages. To get around this issues end users would be prompted when an application wanted to open up a incoming port on the network. Corporate IT staff could control this for the users using Group Policy via the Windows Firewall section under Administrative Templates > Network > Network Connections.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb27.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image29.png>)

This was a good first step however creating a set of firewall rules using the native group policy setting under Windows Firewall was challenging at best as there most setting had to be configured manually.

With the release of Windows Vista/2008 Microsoft totally revamped the Windows Firewall to allow for much easier administration. IT Admins now have much more granular control over how they can manage the firewall rules and they now have the ability to control both inbound and outbound communication as well as being able to selective enable rules depending on what network the computer is connected. They also changed where you configured the firewall via group policy to Windows Settings > Security Settings > Windows Firewall with Advanced Security which has enable some cool features such as importing and exporting firewall rules which I will go into later.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb28.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image30.png>)

Below I will go though an example of a IT administrator wanting to setup a default set of firewall rules for a Windows 7 laptop computers and with a rule to allow Skype when connected at home and on the Internet but not when connected to the domain. Normally in the real world you would have many more inbound exceptions however you should be able to use this as a guide to get you started to build your firewall rule setup specifically for your environment.

**Before you begin:** If you have already configured firewall setting under the older "Windows Firewall" section these policy rule will also apply and the two rule sets will try to merge with unpredictable results. I recommend that you make sure that no "Windows Firewall" setting are applied to your Vista/2008 or greater computers and that you solely apply the firewall setting to these newer computers via the "Windows Firewall with Advanced Security" group policy security option.

### Configuring Windows Firewall Rule

First we will setup a reference computer with the firewall rule the way we want and then explore them so we can import them into a group policy. Configuring the firewall rules on the PC first gives us an opportunity to properly test the rules before deploying them to other computers. If also allows us to export all the rules in one action so that you don't have to go through the lengthy process of setting up all the rules manually one by one.

In this example this computer is running Windows 7 and already has Skype 4.2 installed.

**Step 1.** Right click on the network status icon in the system tray and click on "Open Network and Sharing Center"

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb29.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image31.png>)

**Step 2.** Click on "Windows Firewall" in the lower left hand corner.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb30.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image32.png>)

**Step 3 optional.** We are going to have a quick high level overview of the firewall rules by clicking on on "Allow a program or feature through Windows Firewall" in the left hand pane.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb31.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image33.png>)

As you can see Skype has been setup to work in the Domain, Private and Public profiles. In this example we are going to configure this so that it will only work in the Home/Work and Public profiles so that users cannot use Skype when they are connected to the corporate domain via the LAN.

**Note:** that the options here are locked out as you have not yet elevated your credentials.

**Step 4 optional.** Click Cancel

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb32.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image34.png>)

**Step 5.** Click on "Advanced Settings" on the left hand pane.

[![image\[76\]](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image76_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image76.png>)

**Step 6.** Click on "Inbound Rules" and then double click on the "Skype" firewall rule entry on the right hand column.

**Note:** The currently configured Profile is set to "All"

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb33.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image35.png>)

Now we will configure the Skype rule to be disable using the domain profile however you can also use this properties dialogue box to configured other granular setting. I recommend that you go though all these tabs and become familiar with all the setting you can control using this dialogue box.

**Step 7.** Click on the "Advanced" tab

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb34.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image36.png>)

**Step 8.** Un-tick the "Domain" check box and then click "OK"

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb35.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image37.png>)

**Note:** The Profile is now configured to "Private, Public"

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb36.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image38.png>)

If you go back into the "Allow programs to communicate thought Windows Firewall" option you will now see that the Domain options for Skype has been un-ticked.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb37.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image39.png>)

Now you need to test your firewall rule set to make sure that it behaves as you expect. Assuming everything is OK then you export your firewall rules so you can import them into a Group Policy. You may also want to save export the rule set before you begin to make sure you have something to role back to in case you totally stuff up the rule set and break your network.

### Exporting Windows Firewall Rules

**Step 1**. In the Windows Firewall with Advance Security section click on "Action" in the menu and then "Export Policy"

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb38.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image40.png>)

**Step 2.** Select a location to save your firewall rules and then type the name of the file you want to save them as (e.g. default_rules.wfw) then click "Save".

**Note:** If you have had to elevate as another user to modify the firewall rules then you will be saving the file in the administrator accounts profile.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb39.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image41.png>)

**Step 3.** Click "OK"

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb40.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image42.png>)

### Importing Windows Firewall Rules into a Group Policy

Now that you have exported the firewall rules we will now import the exported file into a group policy so that you can apply the same rule set to all the workstations on your network.

**Step 1.** Edit a Group Policy Object (GPO) that targets the computer that you want apply these firewall rules applied.

**Step 2.** Open Computer Configuration > Policies > Windows Settings > Security Settings > Windows Firewall with Advanced Security and click on "Windows Firewall with Advanced Security"

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb41.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image43.png>)

**Step 3.** In the menu click on "Action" and then "Import Policy"..."

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb42.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image44.png>)

**Step 4.** Click "Yes"

**Note:** This is ok if you have not done this before however if this is the second time you have done this you might want to create a new GPO and import the rules into that one so as to not to blow away your existing policy rules.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb43.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image45.png>)

**Step 5.** Select the firewall rule export file that created before and click "Open"

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb44.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image46.png>)

Wait"...

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb45.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image47.png>)

**Step 6.** Click "OK"

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb46.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image48.png>)

Done.

You can now review the rules that have been imported into the GPO.

**Note:** You can see how the Skype rule is configured as Private, Public as we configured before on the local computer. If you want to change the again you can simple double click on the rule and customise the rule how you want from within here.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb47.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image49.png>)

You can also selectively disable rules and cut, copy & paste rules between separate GPO's. This is how you would merge rules if you imported the rule set from into a new GPO back in step 4.
****

**How to copy, delete or disable a rule"...**
[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb48.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image50.png>)


**How to paste a rule into an existing policy"...**
[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb49.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image51.png>)

You should now be notified that in all the firewall dialogue boxes (see images below) on the workstation that the firewall policy is now being controlled via group policy.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb50.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image52.png>)

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb51.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image53.png>)

Note the new column that states weather this is configured by Group Policy. Each rule is list twice as one represent the firewall rule controlled via Group Policy that cannot be configured and the other represent the local rule which can still be enabled by the local administrator.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb52.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image54.png>)

### How to exclusively apply Group Policy Firewall rules

If you don't want the local administrator to be able to apply additional firewall rules to the network then you can also configured it so that the Group Policy rules are exclusively applied to the local firewall.

**Step 1.** Again open the same GPO that you have the firewall rules applied and navigate to Computer Configuration > Policies > Windows Settings > Security Settings > Windows Firewall with Advanced Security and right click on "Windows Firewall with Advanced Security" and click "Properties"

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb65.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image67.png>)

**Step 2.** Click on the "Customize.." button in the Setting section

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb66.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image68.png>)

**Step 3.** Change the "Apply local firewall rules:" option to "No" and click OK

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb67.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image69.png>)

Now if you go back to the "Allowed Programs" under "Windows Firewall" you will notice that the Domain column is now totally greyed out and no rules can be applied to the domain profile even if you are a local admin.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb68.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image70.png>)

Hopefully you this will have given enough to start controlling your windows firewall using group policy.

If you are feeling really adventurous you can also do the same thing to your servers to keep them secure as they are a lot more static with the firewall rule requirements which makes them even easier to manage. For example you could export the firewall rules of your SQL server and then import them into a GPO that is applied to all your other SQL Servers. This way when ever you move a computer object into the SQL Server OU the firewall rules are automatically setup and enforced"... Nice..