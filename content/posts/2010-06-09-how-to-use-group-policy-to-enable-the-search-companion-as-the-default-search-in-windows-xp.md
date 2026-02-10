---
title: "How to use Group Policy to enable the &ldquo;Search Companion&rdquo; as the default search in Windows XP"
date: 2010-06-09 11:50:31
author: admin
categories: ["Tutorials"]
tags: ["Basic", "Office 2007", "Search Companion", "Windows Desktop Search", "Windows XP"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/06/image_thumb14.png"
---

[Windows Desktop Search 4.0](<http://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=55c18cb3-c916-4298-aba3-5b98904f7cda>) is a fantastic local search engine for Windows XP that allows users to quickly search all their local files and network file servers. This is also a requirement for anyone that want to use the instant search feature in Outlook 2007 as it utilises this search engine to perform an index of your inbox.

However as you can see the user interface for the search is much different and by default will not perform non-indexed search's of network file share without setting up a search location. The problem is that for some users this is a lot to get used to and they quite often go back to using the "Search Companion" (see circled in red).

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/06/image_thumb14.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/06/image13.png>)

So there is a registry key you can configure if you want to make the "Search Companion" the default search provider for Windows XP but you don't want to remove the Windows Desktop Search because of all the goodness it give you in Outlook 2007

### Search Companion Registry Key Details

**Key:** HKCU\Software\Microsoft\Windows Desktop Search\DS
**Value:** ShowStartSearchBand (REG_DWORD)
**Data:** 0 (zero)

### How to enable Search Companion

**Step 1.** Edit a Group Policy Object that is targeted to the users that you want to enable the search companion option.
**Step 2.** Navigate to User Configuration > Preferences > Windows Settings > Registry
**Step 3.** In the menu click on Action > New > Registry Item
**Step 4.** Setup the following for your new registry item

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/06/image_thumb15.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/06/image14.png>)

Once the policy is applied to your users the search command from explorer or from the start menu you will launch the "search companion" by default.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/06/image_thumb17.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/06/image15.png>)

Source: <http://jamielesouef.com/microsoft/change-windows-desktop-search-to-search-companion/>