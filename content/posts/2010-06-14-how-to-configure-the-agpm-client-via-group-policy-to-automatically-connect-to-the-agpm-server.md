---
title: "AGPM Part 4: How to configure the AGPM client via Group Policy to automatically connect to the AGPM server"
date: 2010-06-14 10:22:00
author: admin
categories: ["Tutorials"]
tags: ["Advanced Group Policy Management", "AGPM", "Intermediate"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb124.png"
---

This post is part of a series of posts about Advanced Group Policy Management. If you want to see the other post in this series you can use the links below:

  1. [Introduction to Advanced Group Policy Management (a.k.a AGPM) v4](<https://www.grouppolicy.biz/2010/06/introduction-to-advanced-group-policy-management-a-k-a-agpm-v4>)
  2. [How to install the Advanced Group Policy Management Client v4](<https://www.grouppolicy.biz/2010/06/how-to-install-the-advanced-group-policy-management-agpm-client-v4>)
  3. [How to install the Advanced Group Policy Management (AGPM) Server v4](<https://www.grouppolicy.biz/2010/06/how-to-install-advanced-group-policy-management-server-v4>)
  4. How to configure the AGPM client via Group Policy to automatically connect to the AGPM server
  5. [Delegating permission to Review/Edit GPO's in AGPM](<https://www.grouppolicy.biz/2010/06/delegating-permission-to-reviewedit-gpos-in-agpm>)
  6. [How to create make changes to Group Policy Objects in AGPM](<https://www.grouppolicy.biz/2010/06/how-to-create-make-changes-to-group-policy-objects-in-agpm>)
  7. [How to makes changes to existing uncontrolled GPO's in AGPM](<https://www.grouppolicy.biz/2010/06/how-to-makes-changes-to-existing-uncontrolled-gpos-in-agpm>)


### Configuring the AGPM Client

This section describes the process of how to automatically connect AGPM client to the AGPM server you have in your forest. If you do not perform this option step then each person that uses the AGPM will need to manually configure the Client to the correct AGPM server. **Step 1.** Edit the Default Domain Policy using the Group Policy Management Editor (GPME) and navigate to Users Configuration > Policies > Administrative Templates > Windows Components > **AGPM then edit the AGPM: Specify default AGPM Server (all domains)** **** [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb124.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image129.png>) **Step 2.** Tick Enable and then type the name/IP address then :_Port_ number of the AGPM Server in the text field then click **OK** (Hopefully this is the last non-managed GPO change you ever make again) [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb125.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image130.png>) NEXT > [Delegating permission to Review/Edit GPO's in AGPM](<https://www.grouppolicy.biz/2010/06/delegating-permission-to-reviewedit-gpos-in-agpm>)