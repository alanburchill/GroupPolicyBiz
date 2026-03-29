---
title: "Why can it take 10+ hours for Group Policy settings to Apply?"
date: 2013-11-01 08:08:00
author: admin
categories: ["Tutorials"]
tags: ["Group Policy Refresh", "Kerberos"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2013/11/clock_thumb.jpg"
---

[![clock](https://www.grouppolicy.biz/wp-content/uploads/2013/11/clock_thumb.jpg)](<https://www.grouppolicy.biz/wp-content/uploads/2013/11/clock.jpg>)Have you ever applied a Group Policy and then waited the standard 90 minutes for the setting to apply only to find out that after a few hours the policy still has not been set yet. Even trying to force a GPUPDATE still does not trigger the change but then the next day the policy has applied as expected. What is going on here?

This is a situation that is commonly caused if you are using security group filtering for applying policy settings. The problem is that the Group Policy object you have applied to the user or computer requires security group membership to evaluate that it can apply to that computer. The group membership will have been replicated in Active Directory however the Kerberos Ticket Granting Ticket (TGT) on the local computer also needs to be updated. This TGT refresh is by default is configured to only happen every 10 hours in Active Directory.

A way to check this is to do a Group Policy Result report against the user of computer and then check the "Security Group Membership" by clicking the "Show" option under the "Details" tab.

**Note:** In older version of the Group Policy Management Console, this will be visible under the "Security Group Membership when Group Policy was applied" under the "Summary" tab.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/11/image_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/11/image.png>)

As you can see below this will show you all the security group memberships that were used when the Group Policy was last processed on that computer.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/11/image_thumb1.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/11/image1.png>)

As this is only showing the membership when the policy has been applied it is possible that the Group Membership on the local computer has updated since the last policy upgrade depending on the refresh timing. Performing a GPUPDATE *MIGHT* make the policy settings applied if the Kerberos token on the computer/user has updated since the last Group Policy Update. But, the only sure fire way to be sure that the new group membership straight away is to either log off as the user or reboot the computer to refresh the Kerberos token.

You do have the option to reduce or increase this refresh value you can do this by modifying the "Maximum lifetime for user ticket Properties" setting under Computer Configuration > Windows Settings > Security Settings > Account Policies > Kerberos Policy. But unless you have a REALLY good reason I would not recommend that you change this value from the default.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/11/image_thumb2.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/11/image2.png>)

As I already mention in my [Group Policy Design Guidelines](<https://www.grouppolicy.biz/2010/07/best-practice-group-policy-design-guidelines-part-2/3/> "https://www.grouppolicy.biz/2010/07/best-practice-group-policy-design-guidelines-part-2/3/") post, applying filtering Group Policy Objects via security groups can have its issues and should only be used for applying setting by exception. But if you do apply your policy settings this way just be aware that the users/computers will probably be waiting a while for them to get the new settings if they are applied via group membership.