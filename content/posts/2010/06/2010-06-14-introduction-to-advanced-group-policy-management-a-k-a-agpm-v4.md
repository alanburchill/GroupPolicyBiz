---
title: "AGPM Part 1: Introduction to Advanced Group Policy Management (a.k.a AGPM) v4"
date: 2010-06-14 10:19:00
author: admin
categories: ["Tutorials"]
tags: ["Advanced Group Policy Management", "AGPM", "Intermediate", "MDOP"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/06/image_thumb19.png"
---

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/06/image_thumb19.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/06/image17.png>)

In this series of post I will show you how to install and user [Advanced Group Policy Management](<http://technet.microsoft.com/library/ee532079.aspx>) (AGPM) v4 tool which part of the [Microsoft Desktop Optimisation Pack](<http://technet.microsoft.com/en-us/windows/bb899442.aspx>) (MDOP). You qualify to use AGPM (and all the MDOP) tools if you have a subscription advantage (SA) licence agreement with Microsoft. The whole suite of MDOP tools are very handy for any organisation wanting to streamline the management of their desktop SOE fleet. It is my intention that once you have read all these post your should be familiar enough specifically with AGPM to install and use it in your environment.

Both for your convenience and improved load times I have broken this article into it's separate sections. You can jump to each section you want by simply clicking on the link's below or you can just click on the link at the both of each posting to go to the next article in the series:

  1. Introduction to Advanced Group Policy Management (a.k.a AGPM) v4
  2. [How to install the Advanced Group Policy Management Client v4](<https://www.grouppolicy.biz/2010/06/how-to-install-the-advanced-group-policy-management-agpm-client-v4>)
  3. [How to install the Advanced Group Policy Management (AGPM) Server v4](<https://www.grouppolicy.biz/2010/06/how-to-install-advanced-group-policy-management-server-v4>)
  4. [How to configure the AGPM client via Group Policy to automatically connect to the AGPM server](<https://www.grouppolicy.biz/2010/06/how-to-configure-the-agpm-client-via-group-policy-to-automatically-connect-to-the-agpm-server>)
  5. [Delegating permission to Review/Edit GPO's in AGPM](<https://www.grouppolicy.biz/2010/06/delegating-permission-to-reviewedit-gpos-in-agpm>)
  6. [How to create make changes to Group Policy Objects in AGPM](<https://www.grouppolicy.biz/2010/06/how-to-create-make-changes-to-group-policy-objects-in-agpm>)
  7. [How to makes changes to existing uncontrolled GPO's in AGPM](<https://www.grouppolicy.biz/2010/06/how-to-makes-changes-to-existing-uncontrolled-gpos-in-agpm>)


### What is AGPM?

Advanced Group Policy Management (AGPM) allows organisation to implement change control and versioning to their Active Directory Group Policies. This allows multiple people to edit Group Policy Object (GPO) with their changes going live the instant the change is made. Any changes to a GPO needs to be check-in, deployed then approved before ever making it to production. This product effectively sits between Active Directory (AD) and Group Policy Administrator so that they never directly need to modify a GPO. To prevent circumventing AGPM a proper implementation should include the removal of all edit/modify permission from all GPO's for everyone except say the service account and the built-in Administrator domain account.

We will now go through a scenario where an administrator (called Alan) will install the AGPM Client and Server. Alan will then delegate another administrator John Reviewer/Editor access in AGPM. John will then create a new Managed GPO and make a change to it and then deploy it for use in production. Alan will then review the GPO and Approve the change. Then Alan will also convert an existing unmanaged GPO to "managed" status so it can be controlled via AGPM.

NEXT > [How to install the Advanced Group Policy Management Client v4](<https://www.grouppolicy.biz/2010/06/how-to-install-the-advanced-group-policy-management-agpm-client-v4>)