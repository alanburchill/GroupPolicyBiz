---
title: "How to use Group Policy to control Services"
date: 2010-08-11 08:00:00
author: admin
categories: ["Best Practice", "Tutorials"]
tags: ["Basic", "Services"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/08/image_thumb15.png"
---

Services are programs that are configured to run in the background of a Windows computer weather or not there is a users that is logged on. They are essential part of windows and are essential to the operation of any windows computers. Without services computer could not perform automatic updates, run scheduled tasks or even connect to a file share. Therefore the ability to control Windows Services is a vita task for IT administrators.

Quite often disabling services on a computer is the best way to reduce the security surface of a computer or to improve performance by turning off un-used components of the OS. Inversely it is also very important to have the ability to turn on services to enable certain functionality or to ensure that certain services are not turned off.

Below I will go through the two ways you can control services in windows by using Group Policy each ways has its own advantages and/disadvantages but together you can pretty much control any system service the way you want.

In the examples below I am going to show you how to enable the "Applications Identification" service that is required to be enabled to make AppLocker work in Windows 7. If you want to learn more about AppLocker then check out my other post

### Using Group Policy to configured a Service

Even since Group Policy was introduced to Windows 2000 you have been able to configured some aspects of services using native group policy.

Now that you can control service using Group Policy Preference there are only two reason that you will still want to use this method.

  1. You want to control services on Windows 2000 or a computer that does not have the client side extensions installed.
  2. You want to configure the security so that non-administrators can start,stop and pause the service.


**Step 1.** Edit a computer Group Policy Object that is targeted at the computer that you want to configure

**Step 2.** Select the services that you want to configure.

**Note:** If the service that you want to configure is not present in the list you will need to install GPMC on a computer that has the service running. This is a painful restriction of controlling services this way and

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/08/image_thumb15.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/08/image15.png>)

**Step 3.** From the menu click on Action > Properties then tick "Define this policy setting" and then configured the service startup mode to what you want it configured.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/08/image_thumb16.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/08/image16.png>)

**Step 4.** If you click on the "Edit Security"..." button you can also configured who has control over the service. This would be useful if you want to give end users the ability to start and stop specific services. **Tip:** Tick "Start, stop and pause" for INTERACTIVE if you want the logged on user to control the services.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/08/image_thumb17.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/08/image17.png>)

Now that you have configured the services via group policy you will need to reboot the computer for the new startup mode to take affect. This means if you are disabling a service then it will not stop until your next reboot which could be may days, weeks or even months after you made the policy change.

### Using [Group Policy Preferences](<https://www.grouppolicy.biz/2010/03/what-are-group-policy-preferences/>) to configure a Service

The newer and almost always better way to configure service now is to you the Group Policy Preference Services options. As opposed to the native method which only allowed you to control the startup and security of service, preference now allows you much greater control.

The only reasons you would not want to use Group Policy Preference to control services are:

  1. You need to configured the startup mode of a service on a computer running Windows 2000 or one that is not running the client side extensions.
  2. You want to be able to configured the security to allow non-admin to start, stop or pause the service.


Always remember that when you do configure a service startup mode using the native method that this will take precedence over Group Policy Preferences and you can use the security options in conjunction with preferences.

**Step 1.** Edit a computer Group Policy Object that is targeted to the computers that you want to control the service.

**Step 2.** Navigate to Computer Configuration > Preferences > Control Panel Settings > Services

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/08/image_thumb18.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/08/image18.png>)

**Step 3.** In the menu click on Action > New > Service and now click on the "..." button next to the Service Name field.

Note: From here you can either type in the service name in the "Service Name" field or click on the "..." button to chose the service from a predefined list of services.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/08/image_thumb19.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/08/image20.png>)

**Step 4**. Select the service name that you want to configured and then click "Select"

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/08/image_thumb21.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/08/image21.png>)

**Step 5.** Now you can configure the Startup mode from the Startup mode drop down box and you can configure a service action.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/08/image_thumb22.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/08/image22.png>)

Service Action will take place each time there is a group policy refresh so that you do not need to wait for the computer to reboot for the latest startup mode to take affect. This can also be handy to configure if you want a service to start if it crashes or if you have a pesky service that requires restarting on a regular basis to keep running properly.

**Step 6.** Click on the "Recovery" tab to configure the recovery options of the service as you would configure in the service control panel.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/08/image_thumb23.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/08/image23.png>)

**Step 7.** As this is a preference you can also configure the standard "Common" options from such as item level targeting which will allow you to granularly control what computer you target this setting.

As you can see with the combination of Group Policy Preferences and the native policies there is nothing you cant configure to your system services"... Enjoy