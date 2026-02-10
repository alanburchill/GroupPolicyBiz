---
title: "Silverlight 5 Group Policy"
date: 2011-04-14 13:00:00
author: admin
categories: ["Tutorials"]
tags: ["5", "AllowElevatedTrustAppsInBrowser", "Group Policy", "Silverlight"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2011/04/logoSilverlight_thumb.jpg"
---

[![logoSilverlight](https://www.grouppolicy.biz/wp-content/uploads/2011/04/logoSilverlight_thumb.jpg)](<https://www.grouppolicy.biz/wp-content/uploads/2011/04/logoSilverlight.jpg>)Microsoft have just released the Silverlight 5 beta during the MIX 2011 summit in Las Vegas and one of the new features is Group Policy support. However this "Group Policy" support at the moment is more like a suggested way of configuration the program. What this really is that you can now control the running on Signed/Trusted Elevated applications from within the browser via a registry key.

For more on trusted in browser applications see <http://timheuer.com/blog/archive/2011/04/13/whats-new-in-silverlight-5-a-guide.aspx#trustinbrowser>

> A new feature we are bringing is the ability to do some of the "trusted" features in Silverlight _in the browser_. This brings the current functionality of trusted applications in current form to be used in the browser context without having to be installed. This still requires the XAP to have the ElevatedPermissions security setting in the manifest as it would exist with out-of-browser applications as well as the XAP being signed (and the certificate in the user's trusted publisher store).

>
> Additionally the requirement would be that a registry key be set on the machine to enable this. This could be deployed via Group Policy or other desktop-management techniques.

Below I have listed this registry key and how you can use a Group Policy Preferences Registry Item to configure this setting in your organisation.

### Allow Elevated Trust Apps In Browser

**Key (Machine):** HKLM\SOFTWARE\Microsoft\Silverlight\
**Value:** AllowElevatedTrustAppsInBrowser (REG_DWORD32)
**Data:** 0 (Disabled)
**Data:** 1 (Enabled)

**Step 1.** Edit a group policy object that targets all the computers in your organisation that you want to apply this setting.

**Step 2.** Navigate to "Computer Configuration > Preferences > Windows Settings" then right click on "Registry" and click on "New > Registry Item"

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/04/image_thumb36.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/04/image37.png>)

**Step 3.** Change the Action to "Replace" add the key path "SOFTWARE\Microsoft\Silverlight" type "AllowElevatedTrustAppsInBrowser" select the Value type to "REG_DWORD" and the value to "1".

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/04/image_thumb37.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/04/image38.png>)

**Step 4.** Click on the common tab and tick "Remove this item when it is no longer applied" and add a description.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/04/image_thumb38.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/04/image39.png>)

Done"... the registry key should be now deployed to all your computers and they will be able to run Trusted (Signed) application in the web browser.

To see what other features are coming in Silverlight v5 go to <http://www.microsoft.com/silverlight/future/>