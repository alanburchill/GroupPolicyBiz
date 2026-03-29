---
title: "KB274274 Focus: The Cross-Forest program deployment problem using Group Policy"
date: 2010-04-29 11:00:00
author: admin
categories: ["KB Focus"]
tags: ["Intermediate", "KB274274", "Kerberos", "NTLM"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/04/image_thumb14.png"
---

I have decided to start posting about some specific group policy related KB's that I have found useful in my time. I will make these posting whenever I come across them so they I will only post them on a semi regular basis.

This KB Focus is [KB274274](<http://support.microsoft.com/kb/274274> "http://support.microsoft.com/kb/274274") which talks about a problem you will encounter if you are trying to deploy a machine targeted application from install source that is on a server in another Forest that you have an external trust configured. The problem is that all authentication traffic that goes via an external domain trust is only NTLM based, however computer account authentication is only Kerberos based. This will present as a access denied in the event log whenever the computer tries to install an application no matter how much permission you try to apply to the source files. What's even more confusing about this problem is when you are logged on as a user you will probably be able to access the file share fine which makes this all the more confusing to troubleshoot.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/04/image_thumb14.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/04/image20.png>)

Unfortunately if you are in this situation you are pretty much left with no alternative other than to move the file share to a serve that is located in the same forest as the computer to install the software as "this behaviour is by design". While it is not mentioned in the article you might be able to get away with enabling guest access on the file server however this would require some pretty serious security relaxations which is why it is definitely not recommended.