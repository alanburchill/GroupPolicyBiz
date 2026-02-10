---
title: "Group Policy Setting of the Week 23 &ndash; Outlook 2003 RPC Encryption"
date: 2010-04-26 09:56:18
author: admin
categories: ["Setting of the Week"]
tags: ["Encryption", "Exchange 2010", "Outlook 2003", "RPC"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/04/image_thumb13.png"
---

This weeks setting is a little bit different as this is the first time that I have selected a non-managed policy setting, but I have chosen this one as it is probably a setting that will be used in a lot of organisations as they start to rollout Exchange 2010. This setting is called "Enable RPC Encryption" and it is a Outlook 2003 specific setting that enables encrypted RPC communication with the exchange server. The reason why this setting is now so important is that starting with Exchange 2010 all RPC communication with the server requires encryption by default. This setting can be found under User Configuration > Policies > Administrative Templates > Classic Administrative Templates > Outlook 2003 RPC Encryption > Exchange Settings however remember as this is a non-managed policy you may need to enable option to see non-managed settings.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/04/image_thumb13.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/04/image19.png>)

For more information on how to install this custom adm see [Outlook connection issues with Exchange 2010 mailboxes because of the RPC encryption requirement](<http://support.microsoft.com/kb/2006508> "http://support.microsoft.com/kb/2006508") and for more information about making Outlook 2003 with with Exchange 2010 then see [Common Client Access Considerations for Outlook 2003 and Exchange 2010](<http://msexchangeteam.com/archive/2010/04/23/454711.aspx> "http://msexchangeteam.com/archive/2010/04/23/454711.aspx") .