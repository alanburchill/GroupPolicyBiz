---
title: "How to use Group Policy to allow the users to chose any screensaver except (None)"
date: 2010-07-14 10:00:00
author: admin
categories: ["Tutorials"]
tags: ["Group Policy", "Group Policy Prefereces", "Intermediate", "Screensaver", "SOE"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb13.png"
---

During Kevin Sullivan [Group Policy session at TechEd 2010](<http://www.msteched.com/2010/NorthAmerica/WCL323>) in the USA this year he mentioned an example of a being able to configure group policy to allow users to select whatever screensaver they want except the one called "(None)" (see image below). While this method does not prevent the users from select the (None) from the screensaver options list it will set it back to a screensaver of your choice when the user selects (None) option.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb13.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image13.png>)

The logic to implement this policy is to test if the SCRNSAVE.EXE registry key exists and if it doesn't then create the key with the screensaver that you want to enable.

**Note:** You can also use this tutorial as a guide for applying other group policy preferences settings based on weather a registry key exists or not. A good example you might want to do this for is to test to see if a specific application registry key exists before you apply an application specific registry setting. This helps you keep a cleaner configured SOE by not un-necessarily applying configuration settings.

### How to use Group Policy to allow the users to chose any screensaver except (None)

**Step 1.** Edit a Group Policy Object (GPO) that is targeted to the users accounts you wan to apply this policy

**Step 2**. Navigate to User Configuration > Preferences > Windows Settings > Registry then from the menu click on Action > New > Registry Item

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb14.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image14.png>)

**Step 3.** Select "Update" from the Action then type "Control Panel\Desktop" in the Key Path: text field then type "SCRNSAVE.EXE" in the Value Name text field and "C:\Windows\System32\scrnsave.scr" in the Value data: text field.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb15.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image15.png>)

**Step 4.** Click on the Common tab and then tick "Item-level targeting" and then click the "Targeting"..." button.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb16.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image16.png>)

Now we will target the screen saver to apply only when the "HKCU\Control Panel\Desktop\SCRNSAVE.EXE" registry key does NOT exist as this means the screen saver has been configured to "(None)".

**Step 5.** Click on "New Item" then the "Registry Match" option.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb17.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image17.png>)

**Step 6.** Select the "Value exists" Match type" then type "Control Panel\Desktop" in the key path field and then type "SCRNSAVE.EXE" in the value name field

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb18.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image18.png>)

**Step 7**. Click back on the targeting setting in the top pane and press "F8" which changes the option to "does not exist" then click OK and OK.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb19.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image19.png>)

This policy will now apply the blank screen saver on the next group policy refresh to all targeted users whenever they select the "(None)".

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb20.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image20.png>)

Below is a table that shows the screensaver set to "(None)" (before column) and then the after a policy refresh the screensaver is configured as "Blank" (After column). Then the users has selected the "Photos" (Custom column) screensaver and the policy is refreshed again however this time there is no change as the screensaver is configured with a value so it is not set back to "Blank".

Before | After | Custom
---|---|---
[](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image21.png>)[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb21.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image22.png>) | [](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image23.png>)[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb22.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image24.png>) | [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb23.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image25.png>)