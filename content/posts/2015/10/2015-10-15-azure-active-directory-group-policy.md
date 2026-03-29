---
title: "Azure Active Directory Group Policy"
date: 2015-10-15 05:47:39
author: admin
categories: ["News"]
tags: ["Active Directory", "Azure", "Cloud", "Group Policy", "IaaS"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2015/10/AADLogo-150x116.png"
---

[![AADLogo](https://www.grouppolicy.biz/wp-content/uploads/2015/10/AADLogo-150x116.png)](<https://www.grouppolicy.biz/wp-content/uploads/2015/10/AADLogo.png>)Today Microsoft announced Azure AD Domain Services Preview that allows Azure IaaS system to be joined to a cloud (Azure) based Active Directory. This feature also enables you to sync your on premise AD with the cloud so that users can logon to both on premise and in cloud with the same set of synchronised credentials. Conceptual, think of this as a separate AD that is in the cloud that is synchronised with your on premise AD. The users and objects in the cloud are essentially "clones" of the on premise objects so they behave similar to an account that has SidHistory of another account from a previous old domain. But as this is essentially a separate full AD this also means you now have the ability to deploy Group Policy settings to your servers and users in Azure IaaS. This is certainly a great step forward for Azure AD however for now you need to be aware there are some caveats to this Group Policy functionality:

  * > Managed domains provided by Azure AD Domain Services support only a flat OU (Organizational Unit) structure. All domain-joined machines reside in a single flat OU and hierarchical OU structures are not supported.

  * > Azure AD Domain Services supports simple Group Policy in the form of a built-in GPO each for the users and computers containers. You cannot target GP by OU/department, perform WMI filtering or create custom GPOs.


While it is certainly not a fully functional version of Group Policy for Azure IaaS, it's a start and you can now at least deploy a default set of policies to your servers and users in the cloud. Also bear in mind that this is a preview version of the service and Microsoft are always adding more functionality so its possible that this cloud change in the future. Source: <https://azure.microsoft.com/en-us/documentation/articles/active-directory-ds-overview/>