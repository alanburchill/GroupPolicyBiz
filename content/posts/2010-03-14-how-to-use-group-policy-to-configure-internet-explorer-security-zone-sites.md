---
title: "How to use Group Policy to configure Internet Explorer security zone sites"
date: 2010-03-14 06:00:00
author: admin
categories: ["Best Practice", "Tutorials"]
tags: ["Group Policy", "Intermediate", "Internet Explorer", "Popular", "Security", "sites", "Zone"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb44.png"
---

As you know [Group Policy Preferences](<https://www.grouppolicy.biz/2010/03/what-are-group-policy-preferences/>) are these fantastic new settings that allow IT administrators perform any configuration they want on a users group using Group Policy"... well almost.. In this tutorial I will show you how to configured one of the few settings that are not controlled by preferences but can be configured using a native Group Policy.

The Internet Explore site zone assignment is one of the few settings you specifically can't configured using preferences, as you can see (image below) the User Interface to this options has been disabled.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb44.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image44.png>)

There is a native Group Policy that allows you to control Internet Explorer site zone list is called "Site to Zone Assignment List" which I will go thought below how to use.

**Step 1.** Edit the Group Policy Object that is targeted to the users you whish this setting to be applied.

**Step 2**. Navigate to User Configuration > Administrative Templates > Windows Components > Internet Explorer > Internet Control Panel > Security Page and double click on the "Site to Zone Assignment List" and check the "Enable" option then click on the "Show.." button.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image6_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image61.png>)

**Step 3.** Now type the URL in the "Value name" field with the **> *** on the far left and then type the zone number (see table below) you want to assign to that zone.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb45.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image45.png>)




#### Internet Explorer Group Policy Zone Number Mapping

Zone Number | Zone Name
---|---
1 | Intranet Zone
2 | Trusted Sites zone
3 | Internet zone
4 | Restricted Sites zone

As soon as you start typing the URL a new line will appear for the next URL.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb46.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image46.png>)

**Step 4.** One you have finished assigning adding the URL's and site zone number click OK

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb47.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image47.png>)

**Tip:** If you want to delete a row click on the button on the far left to select the row you want to delete (see image below) and then press the "Delete" key.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb48.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image48.png>)

(sites in above list are example only)

Now the Internet Explorer Site zone list will now be populated with the zone you configured above and as you can see in the images below the Internet Explorer status bar now show the correct zone based on the that the URL's in the address bar.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb49.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image49.png>)

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb50.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image50.png>)

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb51.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image51.png>)

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb52.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image52.png>)