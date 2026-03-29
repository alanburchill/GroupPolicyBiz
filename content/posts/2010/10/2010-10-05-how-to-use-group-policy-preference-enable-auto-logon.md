---
title: "How to use Group Policy Preference enable auto-logon"
date: 2010-10-05 14:30:00
author: admin
categories: ["Best Practice", "Tutorials"]
tags: ["auto-logon", "automatic logon", "Basic", "Group Policy Preferences", "registry"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/10/image_thumb4.png"
---

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/10/image_thumb4.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/10/image4.png>)The below article shows you how to use Group Policy Preference to setup the registry keys on a computer so that it automatically logs onto when its turned on. While doing this is potentially huge security issue and not something I would generally recommend IT staff might want to implement on computers that are highly locked down and used for only a specific propose.

### How to set a registry key using [Group Policy Preferences](<https://www.grouppolicy.biz/2010/03/what-are-group-policy-preferences/>)

Before we begin I will show you how create the required registry keys using group policy preference. After this I will list the registry keys you need to use with the instruction below to configure automatic logon.

**Step 1.** Edit a Group Policy Object that is applied to the computers you want this setting applied.

**WARNING:** Make sure you have not applied this policy to any computers before you begin as this will obviously logon any computer that this policy is applied to automatically.

**Step 2.** Navigate to Computer Configuration > Preferences > Windows Settings > Registry

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/10/image_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/10/image.png>)

**Step 3.** In the Menu click on Action > New > Registry Item

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb50.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image52.png>)

Now you know how to configure a registry key setting using Group Policy Preferences you can create a new Registry Item for each registry key listed below.

### How to configure Windows to automatically logon

Now we need to create the below registry keys to enable the automatic logon process.

**Note:** You will need to substitute you own specific values for all the text in italic below.

#### Enable AutoLogon

**Key:** HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon
**Value:** AutoAdminLogon (REG_SZ)
**Data:** 1 (Enabled)


#### Default Domain Name

**Key:** HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon
**Value:** DefaultDomainName (REG_SZ)
**Data:** _DOMAINNAME_


#### Default User Name

**Key:** HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon
**Value:** DefaultUserName (REG_SZ)
**Data:** _USERNAME_

#### Default Password

**Key:** HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon
**Value:** DefaultPassword (REG_SZ)
**Data:** _PASSWORD_

You should now have 4 registry keys configured as the image below.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/10/image_thumb1.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/10/image1.png>)

**Warning:** Be sure to also block the regedit tool on the user that logos onto this computer as anyone logged on the computer will be able to see the account password stored in the registry as clear text (see below).

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/10/image_thumb2.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/10/image2.png>)

Now when ever this computer is turned on it will start up and logon automatically with the credentials that you specified in the policy (see below).

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/10/image_thumb3.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/10/image3.png>)

### Related Links

[Creating a Steady State by Using Microsoft Technologies](<http://www.microsoft.com/downloads/en/details.aspx?FamilyID=ef232619-7600-4768-b111-f60ba13862ea> "http://www.microsoft.com/downloads/en/details.aspx?FamilyID=ef232619-7600-4768-b111-f60ba13862ea")