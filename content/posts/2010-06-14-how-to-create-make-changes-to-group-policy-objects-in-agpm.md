---
title: "AGPM Part 6: How to create make changes to Group Policy Objects in AGPM"
date: 2010-06-14 10:24:00
author: admin
categories: ["Tutorials"]
tags: ["Advanced Group Policy Management", "AGPM", "Intermediate"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb129.png"
---

This post is part of a series of posts about Advanced Group Policy Management. If you want to see the other post in this series you can use the links below:

  1. [Introduction to Advanced Group Policy Management (a.k.a AGPM) v4](<https://www.grouppolicy.biz/2010/06/introduction-to-advanced-group-policy-management-a-k-a-agpm-v4>)
  2. [How to install the Advanced Group Policy Management Client v4](<https://www.grouppolicy.biz/2010/06/how-to-install-the-advanced-group-policy-management-agpm-client-v4>)
  3. [How to install the Advanced Group Policy Management (AGPM) Server v4](<https://www.grouppolicy.biz/2010/06/how-to-install-advanced-group-policy-management-server-v4>)
  4. [How to configure the AGPM client via Group Policy to automatically connect to the AGPM server](<https://www.grouppolicy.biz/2010/06/how-to-configure-the-agpm-client-via-group-policy-to-automatically-connect-to-the-agpm-server>)
  5. [Delegating permission to Review/Edit GPO's in AGPM](<https://www.grouppolicy.biz/2010/06/delegating-permission-to-reviewedit-gpos-in-agpm>)
  6. How to create make changes to Group Policy Objects in AGPM
  7. [How to makes changes to existing uncontrolled GPO's in AGPM](<https://www.grouppolicy.biz/2010/06/how-to-makes-changes-to-existing-uncontrolled-gpos-in-agpm>)


### Creating and Editing GPO's in AGPM

Now you are going to logon as John and create a fresh new Controlled GPO to have it then approved by Alan. **Step 1.** Logon as John to a computer that has GPMC and the AGPM client **Step 2.** Open GPMC and right click on **Change Control** and then click on **New Controlled GPO"...** **** [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb129.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image134.png>) **Step 3.** Fill in the submission field so that an email will be sent to the AGPM administrator to review the New Controlled GPO Request then click **Submit** **** [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb130.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image135.png>) **Step 4.** Click **Close** **** Note: In this example I don't have a mail serve configured so the sending the of the email failed. [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb131.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image136.png>) **Step 5.** Click on the **Pending Tab**. You can now see the Pending request waiting for approval. [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb132.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image137.png>) Now we will approve the New Controlled GPO request. **Step 6.** Logon as Alan to a computer that has GPMC and the AGPM client **Step 7.** Open GPMC and right click on **Change Control** then click on the **Pending** tab and the right click on the pending request and click on **Approve"...** **** [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb159.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image164.png>) **Step 8.** Add a comment before you confirm the Approval action then click **Yes** **** [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb134.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image139.png>) **Step 9.** Wait for it to Approve and then click **Close** **** [](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image140.png>) [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/01/image_thumb135.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/01/image140.png>) Note: It is this stage that Alan can link the GPO manually to the Organisational Unit (OU). NEXT > [How to makes changes to existing uncontrolled GPO's in AGPM](<https://www.grouppolicy.biz/2010/06/how-to-makes-changes-to-existing-uncontrolled-gpos-in-agpm>)