---
title: "Configuration Management on Servers"
date: 2016-05-10 02:13:30
author: admin
categories: ["News"]
tags: ["Feedly", "Group Policy", "IFTTT"]
---

Nano Server is [a remotely administered headless server operating system optimized for private clouds and datacenters](<http://ift.tt/1zXP6A9>). Nano Server is significantly physically smaller than Server Core, has no local logon capability and only supports 64-bit applications, tools and agents. As we prepare to release Windows Server 2016 Technical Preview 5, I wanted to provide more information on how to properly configure Nano Server at scale "“ without Group Policy.

One of the things that makes Nano Server so interesting is that it takes up far less disk space, installs significantly faster, and requires far fewer updates and restarts than Windows Server. When it does require a restart, it restarts much faster. To achieve this speed and small physical footprint, Nano Server has the absolute minimum amount of inbox components. As a result, Group Policy and the associated Group Policy Management Console (GPMC), editor (GPMC), Group Policy client and local policy editor (GPEdit) tools are not present on Nano Server. This is expected as they are graphical components and Nano Server is headless and remotely managed. [Even when domain joined](<http://ift.tt/1zXP6A9>), Nano Server will not consume and enact Group Policy settings.

So, without Group Policy, how do you apply security policies to Nano Server? We have a series of documents coming out to answer this question. The first one can be found here: <http://ift.tt/1T7Romf>.

Windows Server 2016 Technical Preview 5 still has complete Group Policy controls, of course. In fact, it has [its fair share of new Group Policy Settings, even over Technical Preview 4](<http://ift.tt/1qWPonc>). You can [find the updated Windows 10 / Windows Server 2016 TP5 group policy settings here](<http://ift.tt/1gJIblI>). Client SKUs also have Group Policy in full.

To sum up:

  * Nano Server has different capabilities than Windows Server 2016
  * Nano Server does not have the Group Policy editing, management, or client service.
  * To manage Nano Server security policy, refer to this post: <http://ift.tt/1T7Romf>
  * Windows Server 2016 and Windows 10 clients continue to have full support for Group Policy.




from Group Policy Team Blog http://ift.tt/1XhZ8VR
via [IFTTT](<http://ift.tt/1c4nCfM>)