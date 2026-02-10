---
title: "Updated - MS16-072 may break your User Group Policies "by-design"
date: 2016-06-15 22:20:10
author: admin
categories: ["hotfix", "News"]
---

This is a PSA for all Group Policy administrator about [MS16-072 ](<https://support.microsoft.com/en-gb/kb/3163622>)that was release yesterday. This patch fixed a man in the middle attack using Group Policy Update however it appears that it has also changed the behavior that Group Policy is applied. If you have a security filtered group policy that are applied to users AND you have also removed "Authenticated Users" group from the GPO then this GPO will no longer apply to the user. To workaround this problem you can either remove the patch or add "read" permissions to the "Authenticated Users" group back to the GPO. This allows the computer object to read the policy setting and the policy will then work again. As a reminder I stressed back in 2010 that you should never just remove "Authenticated Users" from your GPO's and that you should instead simply remove the "Apply" permission for the group. See <https://www.grouppolicy.biz/2010/05/how-to-apply-a-group-policy-object-to-individual-users-or-computer/> ~~No word yet if this is deliberate change in behavior to fix the man in the middle attack or if this is something that will be fixed.~~ Update: Thanks to Darren Mar-Elia he had discovered that this was actually a documented change in behavior

> **MS16-072 changes the security context with which user group policies are retrieved. This by-design** behavior change protects customers' computers from a security vulnerability. Before MS16-072 is installed, user group policies were retrieved by using the user's security context. After MS16-072 is installed, user group policies are retrieved by using the machines security context.

Forum post <https://social.technet.microsoft.com/Forums/en-US/e2ebead9-b30d-4789-a151-5c7783dbbe34/patch-tuesday-kb3159398?forum=winserverGP>