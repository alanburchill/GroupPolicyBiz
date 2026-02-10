---
title: "How to use Group Policy to remove the Adobe Reader desktop shortcut"
date: 2010-03-10 08:00:00
author: admin
categories: ["Tutorials"]
tags: ["adobe reader", "Basic", "Group Policy Preferences"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb41.png"
---

One of the most annoying things about Adobe Reader is that it is in need for constant updating to newer version due to security issues. While this is true for most software packages whenever you install an Adobe Reader update it also restores the desktop icon even if it has already been deleted. (Annoying!!!).

**Note:** for more information on using Group Policy to secure Adobe Reader see my previous article [Permanent Link to How to make Adobe Reader more secure using Group Policy](<https://www.grouppolicy.biz/2010/01/how-to-make-adobe-reader-more-secure-using-group-policy/> "Permanent Link to How to make Adobe Reader more secure using Group Policy")

So below I go through how to use one of the new Group Policy Preferences options is called "Shortcuts" to remove the icon when ever it is re-instated (see below). While in this example I use (pick on) Adobe Reader it can also be used as a guide for removing any other shortcut that you so desire.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb41.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image41.png>)

**Step 1.** Edit a GPO that targets the computers that you want to apply the home page setting.

**Step 2.** Navigate to User Configuration > Preferences > Control Panel Settings > Windows Settings

**Step 3.** Click on the "Action" menu and click on "New" and then click on "Shortcut"

**Step 4.** Change the Action to "Delete" then select "All Users Desktop" and then type "Adobe Reader 9" in the name field.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb42.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image42.png>)

Now wait time you install an Adobe Reader update all you have to do is wait for the next group policy refresh and the shortcut will be gone"... (Yes).

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb43.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image43.png>)