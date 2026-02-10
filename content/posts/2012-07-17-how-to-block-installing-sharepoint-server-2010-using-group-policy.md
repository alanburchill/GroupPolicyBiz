---
title: "How to block installing SharePoint Server 2010 using Group Policy"
date: 2012-07-17 13:00:00
author: admin
categories: ["Tutorials"]
tags: ["Basic", "Group Policy", "SharePoint"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2012/07/SharePoint_Logo_Web_thumb.jpg"
---

[![SharePoint_Logo_Web](https://www.grouppolicy.biz/wp-content/uploads/2012/07/SharePoint_Logo_Web_thumb.jpg)](<https://www.grouppolicy.biz/wp-content/uploads/2012/07/SharePoint_Logo_Web.jpg>)SharePoint 2010 is quickly being coming a very popular web platforms for many organisation for collaborating and sharing information. In some cases it is almost to popular in some medium to large organisation with many SharePoint server farms popping up all over the place as each department or business unit see's a need. As a quote from a Microsoft article says:

> Because deployments of Microsoft SharePoint 2010 Products are managed at the farm level, a single SharePoint deployment has no information about other SharePoint deployments that might exist in the same enterprise.

Therefore Microsoft has provided a registry key you can create on your server to ensure that SharePoint will not install.

**Key:** HKLM\Software\Policies\Microsoft\Shared Tools\Web Server Extensions\14.0\ SharePoint\
**Value:** DisableInstall (REG_DWORD)
**Data:** 00000001

**Step 1.** To deploy this key create a new GPO with the following Group Policy Preferences [Registry Extension](<http://technet.microsoft.com/en-us/library/cc771589.aspx>) and link it at the domain in your organisation.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/07/image_thumb6.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/07/image6.png>)

Then if anyone tries to install SharePoint 2010 on a server in your organisation they will get this message:

> SharePoint installation is blocked in your organization. Please contact your network administrator for more details.

However you may want to have SharePoint 2010 installed on your approved server so you will need a way for this setting to be removed for these approved servers.

**Step 2.** To do this go to the common tab and tick the "Remove this item when it is no longer applied" option. This way the registry key will be deleted for any server that is approved to have SharePoint 2010. Then tick "Item-level targeting" and then click the "Targeting"..." button. (Hence the Replace is used in step 1).

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/07/image_thumb7.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/07/image7.png>)

**Step 3.** Option #1 would be to target the setting to **__NOT__** apply if the server computer account is in the "SharePoint" server OU. This is obviously only practical if all you SharePoint servers were grouped together in one OU.

[![sharepoint1](https://www.grouppolicy.biz/wp-content/uploads/2012/07/sharepoint1_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/07/sharepoint1.png>)

**Step 3.** Option #2 would be to target the setting to **__NOT__** apply if the server computer account is in the "SharePoint Servers" security group. This option is more suited if you have servers spread out over your organisation.

[![sharepoint1](https://www.grouppolicy.biz/wp-content/uploads/2012/07/sharepoint1_thumb1.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/07/sharepoint11.png>)

**Note:** In both examples I have added a condition that this setting will only apply to server operating systems therefore avoiding the key to get pushed to on to any of the workstations in the organisations.

Now hopefully armed with this information you can control the sprawl of SharePoint in your organisation"...

References: <http://technet.microsoft.com/en-us/library/ff730261.aspx>