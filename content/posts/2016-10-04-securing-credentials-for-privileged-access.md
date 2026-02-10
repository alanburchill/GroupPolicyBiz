---
title: "Securing Credentials for Privileged Access"
date: 2016-10-04 23:50:21
author: admin
categories: ["News"]
tags: ["Feedly", "Group Policy", "IFTTT"]
---



Hello, Paul Bergson back again. I have been on the road a bit more than normal doing security training/POC deliveries (POP-SLAM *1) for our customers related to Pass-the-Hash and credential protection. I have noticed an alarming trend in how credential protection is thought to resolve a customer's credentials from being compromised. Enterprises that are investing in vaulting software, and not ensuring the users of this vault have workstations that are isolated from internet and e-mail, are being **_lulled into a false sense of security_**!

Credential randomization and vaulting software has begun to expand; this is a great step as enterprises move to protect their assets from exposure but accessing the vault, from an insecure workstation, bypasses the protective steps taken to secure these credentials. "Securing privileged access is a critical first step to establishing security assurances for business assets in a modern organization." *2

By randomizing passwords, the task for an administrator to use these credentials requires them to open the vault and check them out. As soon as an insecure workstation connects to the vault any of the credentials retrieved can no longer have their integrity assured. Making matters worse, I have seen administrators want to reduce their trips to the vault by foreseeing possible future activity and copying **_ALL_** their privileged accounts to their desktop at the start of their day and pasting them in the clear to an open application such as Notepad. Capturing pasted credentials to the clipboard or an application is trivial on a compromised workstation.

If an enterprise allows administrators to use their workstation for both unprivileged activities that have public e-mail & internet browsing available as well as remote administration they have **_NOT_** increased their credential protection. All the labor and expense that has been committed to vault and protect credentials has been wasted.

Looking at the example at the end of this document you can see that an engineer without a protected/isolated workstation, that is saving their password locally, can easily have their secrets harvested. Even if a user is safe and brings up a browser and only reads their password (never placing on the clipboard or into a text based app) the result is the same, the password can be harvested.

An engineer's workstation should be isolated and protected from any potential malware threats. Microsoft has a published a document that guides our customers on how to configure their engineer's workstation. The guidance is called Privileged Access Workstation (PAW *3). Customers can use this guidance without any further assistance from Microsoft, to secure their workstations.

A Microsoft **PAW implementation won't require any additional hardware** , as long as the current hardware can run a virtualization stack such as Windows 10. So, there should be no new net expense just a requirement to rebuild the user's/Administrator's workstation. If the current workstation is using Win10, it should be fully licensed for the Win10 guests of a PAW implementation, at no additional cost.

"Any user of a Licensed Device, or any device used by a Licensed User; may remotely access up to four Instances of the Software Running in Virtual OSEs or one Instance of the Software Running in one Physical OSE on (a) device(s) dedicated to Customer's use." *4

##### Why a dedicated workstation?

"The current threat environment for organizations is rife with sophisticated phishing and other internet attacks that create continuous risk of security compromise for internet exposed accounts and workstations.

This threat environment requires an organization to adopt an "assume breach" security posture when designing protections for high value assets like administrative accounts and sensitive business assets. These high value assets need to be protected against both direct internet threats as well as attacks mounted from other workstations, servers, and devices in the environment." *5

As a part of protecting credentials within a vault, "Credential Tiering" should also be deployed. Credential Tiering is a configuration where credentials are only allowed to be used within a predefined Tier. Tiering will compliment network isolation when the isolation isn't effective by restricting what administrators can control and where they can log on.

"The Tier model is composed of three levels and only includes administrative accounts, not standard user accounts". *6

· Tier 0 "“ Manage the identity store and a small number of systems that are in effective control of it

o DC's, PKI, Radius, etc"...

· Tier 1 "“ Manage enterprise servers, services, and applications

· Tier 2 "“ Manage enterprise desktops, laptops, printers, and other user devices

PAW workstations should only be allowed to extract credentials and manage assets of a single Tier. This protects against Tier escalation via what an account can manage and control.

### Attack scenario example below:

It is trivial to retrieve the password from memory using a debugger, once a host has been compromised.

[![clip_image001](http://ift.tt/2dtjfPS)](<http://ift.tt/2cQuLqv>)

1\. What the heck is a POP-SLAM?

a. <http://ift.tt/1MUxuFY>

2\. <http://ift.tt/2dtlG4A>

3\. Plat blog on PAW

a. <http://ift.tt/1TIOre9>

4\. <http://ift.tt/1fkGjhz>

5\. <http://ift.tt/2bqGcmY>

6\. <http://ift.tt/2dtk8HR>

Hopefully this has sparked some thought and gotten you to understand that simply purchasing a vault product (Or using our free LAPS tool) isn't enough to protect your secured credentials. I would suggest folks that aren't following this guidance to form a plan to protect any workstations that have access to credentials.

from Ask Premier Field Engineering (PFE) Platforms http://ift.tt/2cQuJyR
via [IFTTT](<http://ift.tt/1c4nCfM>)