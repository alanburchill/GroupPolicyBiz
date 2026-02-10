---
title: "Tip: How to ensure Organisation Unit are protected from accidental deletion"
date: 2010-11-23 01:00:00
author: admin
categories: ["Tip"]
tags: ["Active Directory Users and Computers", "ADUC", "GPMC", "Group Policy Managment Console", "Organisationl Unit", "Protect container from accidential deletion"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/11/image_thumb6.png"
---

This is a simple tip that I want to share about the right way to Organisation Units to ensure that you always have them protected from accidental deletion.

Ever since Windows Server 2008/Vista there has been an option in ADUC called "[Protect container from accidental deletion](<http://technet.microsoft.com/en-us/library/cc739350\(WS.10\).aspx>)" (see image below).

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/11/image_thumb6.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/11/image6.png>)

The affect of ticking this check box was that the "Everyone" group would be granted deny delete permission (see below) on the object so that it would be very hard for you to accidently delete an OU (and all of its contents) even if you are a Domain Admin. NICE!!!

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/11/image_thumb7.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/11/image7.png>)

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/11/image_thumb8.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/11/image8.png>)

This is a very handy option to have enabled on all you OU's (groups and users) as we all know that it quite easy to accidently delete something when you are working late or just under the pump with a million things on your plate.

However"...

You may also be aware that the Group Policy Management Console also has as option to create new new Organisation Unit (see below).

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/11/image_thumb9.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/11/image9.png>)

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/11/image_thumb10.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/11/image10.png>)

The problem with using GPMC is that the tool does not implement "[Protect container from accidental deletion](<http://technet.microsoft.com/en-us/library/cc739350\(WS.10\).aspx>)" deny security permission on the OU as the ADUC tool does (see below).

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/11/image_thumb11.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/11/image11.png>)

So in summary, even though it might be really convenient to create OU's in GPMC I recommend that you do NOT do this as you might end up regretting you ever did when you accidently pressed delete one to many times"...