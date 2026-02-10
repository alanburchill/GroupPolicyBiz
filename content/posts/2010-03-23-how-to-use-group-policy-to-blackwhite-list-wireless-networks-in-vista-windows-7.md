---
title: "How to use Group Policy to black/white list wireless networks in Vista & Windows 7"
date: 2010-03-23 11:53:00
author: admin
categories: ["Best Practice", "Tutorials"]
tags: ["Group Policy", "Intermediate", "Vista", "Windows 7", "Wireless"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb16.png"
---

I have seen an number of posts form IT Administrators on the Microsoft Group Policy forums asking how prevent their users from connecting to a wireless network. Maybe it is because they have an open WIFI network on the floor above that users keep connecting to so they can by pass the proxy server URL restrictions or they don't want their users from accessing the internet from well known WIFI hot spots.

In the tutorial below I am going to show you how to block your laptops from connecting to specific wireless networks with the example SSID of "dlink". This black list method is useful when you want to prevent users from connecting to networks such as "[Free Public WiFi](<http://www.winsupersite.com/paul/mailbag/100321.asp#1>)" which is nothing more than a trap set by hacker to steal people's passwords.

Then I will go through the way will to block all wireless networks except for one called "private_ab" using the White List method. This is very useful if you only want your users to connect to wireless network you know are safe to use.

Lastly I will then quickly show you how to totally disable your wireless adapter from being able to connect to any networks.

The instructions below are specific to Vista and Windows 7 as there were a whole heap of new group policy settings that were introduced back when Vista was released.

### How to Black List/White List Wireless Networks using Group Policy

**Note:** Steps 1 to 5 are common for setting up both black and white lists. Then the process branches and describes how to setup a black list then white list in steps 6 & 7.

Step 1. This is a computer based setting so edit a Group Policy Object (GPO) that is targeted to all the laptops in your network

Step 2. Navigate to Computer Configuration > Policies > Windows Settings > Security Settings > Wireless Network (IEEE 802.11) Policies

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb16.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image16.png>)

Step 3. Click on "Action" in the menu and then click on "Create A New Wireless Network Policy for Windows Vista and Later Releases".

**Note:** You can only create one Windows Vista and later and one Windows XP wireless setting within each GPO.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb17.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image17.png>)

Step 4. Now give the give the setting a Policy Name and Description. Ensure that the "Use Windows WLAN AutoCOnfig service for clients" is ticked so that Windows does not allow third-party software to control the wireless network adapter (e.g. Intel Wireless LAN configuration Tool).

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb18.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image18.png>)

Step 5. Now click on the Network Permission Tab and click "Add"..."

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb19.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image19.png>)

### Setting up a Wireless Network Black List using Group Policy

Step 6. Type in the name of the SSID you want to black list (e.g. "dlink") then select the type of Network Type (e.g. Infrastructure) and select "Deny" from the Permission type then click "OK"

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb67.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image67.png>)

Step 7. Click "OK"

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb68.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image68.png>)

Now the user views all the wireless network the will no longer be able to connect the network that has been configured as Deny. (e.g. "dlink")

[![wireless2](https://www.grouppolicy.biz/wp-content/uploads/2010/03/wireless2_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/wireless2.png>)

### Setting up a Wireless Network White List using Group Policy

Step 6. Type in the name of the SSID you want to white list (e.g. "private_ab") then select the type of Network Type (e.g. Infrastructure) and select "Allow" from the Permission type then click "OK"

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb70.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image70.png>)

Step 7. Tick "Prevent connections to ad-hoc networks" and tick "Prevent connections to infrastructure networks" then click "OK"

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb71.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image71.png>)

Now you will ONLY be able to connect to the wireless network called "private_ab" and all other networks will be denied.

[![wireless3](https://www.grouppolicy.biz/wp-content/uploads/2010/03/wireless3_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/wireless3.png>)

**Note:** Configuring a white list will not configure a wireless profile to connect to the allowed network, it simple allows the user to configure a profile for that particular SSID.

### How to disable your wireless networks access via Group Policy

Now if you want to totally deny you users from connecting to any network profile just skip step 6. from the White List procedure leave the "Prevent connections to ad-hoc networks" and "Prevent connections to infrastructure networks".

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb72.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image72.png>)

You users will no longer be able to connect to any wireless networks and when they click on the network in they will receive the message "Your network administrator has blocked you from connecting to this network".

[![wireless1](https://www.grouppolicy.biz/wp-content/uploads/2010/03/wireless1_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/wireless1.png>)

**Note:** Any network profile you have configured in the General tab will be automatically added as an allowed network having the two "Prevent connections" options tick will ensure that the user will not be able to connect to anything but your corporate wireless network.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb73.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image73.png>) [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb74.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image74.png>)