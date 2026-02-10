---
title: "Customising Windows 8.1 Start Screen Layout with Group Policy"
date: 2013-06-04 10:19:00
author: admin
categories: ["Tutorials"]
tags: ["Start Screen", "Windows 8.1"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2013/06/image_thumb.png"
---

In the keynote presentation of TechEd North America 2013 a new Group Policy setting was demonstrated that showed how you can now configure the layout of the Windows 8.1 Start Screen. For your convenience I have summarised the list of steps shown in the demo so you can configure this option for yourself"... when the beta is release".... on June 26th.

Ok"... So its not very useful right now but at least you know it can be done once it is released

We start with the user "Sarah" below who has configured her start screen the way she wanted. IT Admins could configure this as a default out of the box configuration layout but after the users logs on they can change it anyway they want"...

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/06/image_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/06/image.png>)

**Step 1.** So logon as another user and configure your computer Start Screen layout the way you want.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/06/image_thumb1.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/06/image1.png>)

Step 2. Export the Start Screen Layout using the "export-startlayout" PowerShell command.

**Side Note:** See the new Start ~~Button~~ Tip in the bottom left hand corner.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/06/image_thumb2.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/06/image2.png>)

Step 3. Open the User Configuration > Policies > Administrative Templates > Start Menu and Taskbar and edit the "Start Screen Layout" policy setting.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/06/image_thumb3.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/06/image3.png>)

**Note:** You may notice above some other new Group Policy settings

  * Default App
  * Default Search
  * Default
  * Multimon


Step 4. Enable the policy setting and type in the path to the XML configuration file you created before.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/06/image_thumb4.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/06/image4.png>)

Now the users start screen will be configured as per the XML configuration file next time they logon to the computer.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/06/image_thumb5.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/06/image5.png>)

So"... there you go you can now configure the user start screen layout with Windows 8.1 via Group Policy"...