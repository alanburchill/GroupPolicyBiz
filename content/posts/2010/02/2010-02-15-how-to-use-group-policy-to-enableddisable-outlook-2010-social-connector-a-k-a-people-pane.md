---
title: "How to use Group Policy to Enabled/Disable Outlook 2010 Social Connector (a.k.a. People Pane)"
date: 2010-02-15 02:16:18
author: admin
categories: ["Tutorials"]
tags: ["Group Policy", "Intermediate", "Office 2010", "Outlook 2010", "Outlook Social Connector", "People Pane"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/02/Outlook2010_PeopleView_thumb.jpg"
---

There is an awesome new feature coming in Outlook 2010 call the [Outlook Social Connector](<http://blogs.msdn.com/outlook/archive/2009/11/18/announcing-the-outlook-social-connector.aspx>) (a.k.a. People Pane) that allows you to view all the recent relevant status updates and emails from that person. This feature also enables third parties (i.e. [Facebook](<http://www.facebook.com>), [Twitter](<http://www.twitter.com>) & [Linkedin](<http://www.linkedin.com>)) to make connectors so that the view can contain information from a variety of sources.

[![Outlook2010_PeopleView](https://www.grouppolicy.biz/wp-content/uploads/2010/02/Outlook2010_PeopleView_thumb.jpg)](<https://www.grouppolicy.biz/wp-content/uploads/2010/02/Outlook2010_PeopleView.jpg>)

User can turn this option on and off fairly easily under the "People Pane" option under the "View" tab in the Outlook Ribbon.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/02/image_thumb74.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/02/image74.png>)

However some (out of touch) IT organisations might not want this feature enabled in your organisation and so there is a registry kill switch that can be controlled via group policy to enable/disable this option.

**Key:** HKCU\Software\Microsoft\Office\Outlook\SocialConnector

**Value:** RunOSC (REG_DWORD)

**Data:** 0 = Disabled

**Data:** 1 = Enabled

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/02/image_thumb75.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/02/image75.png>)

[](<https://go.avanade.com/personal/bjarne_gram/Blog/Lists/Posts/Post.aspx?ID=4#Comments>)

To control this option edit a Group Policy Object that is applied to all the users in your organisation navigate to Users Configuration > Preferences >Windows Settings > Registry. Then click on Action > New > Registry Item type **Software\Microsoft\Office\Outlook\SocialConnector** into the Key Path field then type **RunOSC** into the Value Name field and **1** in the Value Data field and click **OK**.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/02/image_thumb76.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/02/image76.png>)

Alternatively you can click on the file image below to download the XML group policy preference file with this already setting configured. Once you downloaded the file just drag it into the Group Policy Preference Registry section and it will automatically create the setting.

Once this setting is applied you can see this "People Pane" option is no longer visible in the "View" tab.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/02/image_thumb77.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/02/image77.png>)

**Note** : This also fixes the issue of the People Pane not showing in for some users who installed Office 2010 Beta.