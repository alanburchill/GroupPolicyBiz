---
title: "How to show or hide Control Panel items in Windows 7 using Group Policy"
date: 2010-11-17 13:59:00
author: admin
categories: ["Best Practice", "Tutorials"]
tags: ["Canonical", "Control Panel", "Group Policy", "Windows 7"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/11/image_thumb.png"
---

One of the common lock down's that administrator apply to Remote Desktop Services Servers (a.k.a. Terminal Services (a.k.a. Citrix)) is to remove all but the essential control panel items.

Previous to Windows 7 you had to specify the .cpl (e.g. timedate.cpl) file name of the control panel item you wanted to show or hide however this has changed in Windows 7 and you now need to use the Canonical Name when hiding or showing specific items.

Below I will explain the new way of configuring control panel items for Windows 7 and show you the affect that this has on the control panel.

Before you begin I recommend that you take a look at <http://msdn.microsoft.com/en-us/library/ee330741(VS.85).aspx> which lists all the Canonical names for the control panel items for Windows 7. You will need to know what CN of the item you want to restrict or allow.

**Note:** In this example we are only going to show the control panel items we want to see (white list) however if you use the [**Hide specified Control Panel items**](<http://gpsearch.azurewebsites.net/Default.aspx?PolicyID=4694>) policy setting you can black list only the items you don't want listed.

Step 1. Edit the Group Policy object that is applied to the users that you want to apply the Control Panel configuration.

Step 2. Navigate to User Configuration > Policies > Administrative Templates > Control Panel

Step 3. Double click on the [**Show only specified Control Panel**](<http://gpsearch.azurewebsites.net/Default.aspx?PolicyID=4697>) items setting then check **Enabled** and then click then **Show** button.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/11/image_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/11/image.png>)

Step 4. Now you have the Show Contents dialog box open you need to visit the web site that list the names at [Canonical Names of Control Panel Items](<http://msdn.microsoft.com/en-us/library/ee330741\(VS.85\).aspx> "http://msdn.microsoft.com/en-us/library/ee330741\(VS.85\).aspx") and copy the Canonical name for the control panel item you want to display.

Paste the name into the value field enter the canonical name of the control panel item you want to show in the Value field and click **OK**.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/11/image_thumb1.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/11/image1.png>)

You will now see that the only available control panel item is the Region and Language options (see below).

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/11/image_thumb2.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/11/image2.png>)

However this view is somewhat confusing for users as they can still click on the category but there are not items to display (see below).

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/11/image_thumb3.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/11/image3.png>)

To get around this problem also enable the Always open All Control Panel Items (a.k.a [Force classic Control Panel](<http://gpsearch.azurewebsites.net/Default.aspx?PolicyID=4695>)) when opening Control Panel setting in the same GPO.

**Note:** This option is probably not needed if you used the [**Show only specified Control Panel**](<http://gpsearch.azurewebsites.net/Default.aspx?PolicyID=4697>) setting instead.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/11/image_thumb4.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/11/image4.png>)

Now when the users open control panel they will only see the specific control panel items you have allowed without the empty categories.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/11/image_thumb5.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/11/image5.png>)