---
title: "Updated: How to download and install the Group Policy Management Console (GPMC)"
date: 2010-03-01 09:00:00
author: admin
categories: ["Tutorials"]
tags: ["Basic", "GPMC", "RSAT", "Windows 7", "Windows Server 2008 R2"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/02/image_thumb88.png"
---

One of the common task that Group Policy administrators need to do is download and install the Group Policy Management Console (GPMC) on their computer to allow them to make changes to Group Policy. This tool is by default not installed on Windows Server 2008 R2 or Windows 7. Below I first go through the Windows 7 and then the Windows Server 2008 R2 install procedure"...

### Windows 7

The install is slightly different for Windows 7 as the install file for the GPMC are not actually part of the Windows 7 installation so you first need to download and install the the Remote Server Administrator Tools (RSAT) on your computer.

Step 1. Downloads for either the 32bit or 64 bit of the RSAT for Windows 7 from the link below.

**Update:** RSAT now supports Windows 7 Service Pack 1"...

[http://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=7d2f6ad7-656b-4313-a005-4e344e43997d](<http://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=7d2f6ad7-656b-4313-a005-4e344e43997d> "http://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=7d2f6ad7-656b-4313-a005-4e344e43997d")

Step 2. Once you have download the RSAT Microsoft Update Standalone Package (.MSU) for your platform install it by simply double clicking on the file.

Step 3. You will then be prompted to install this update onto your computer

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/02/image_thumb88.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/02/image88.png>)

Step 4. Read the licence terms and click "I Accept" (if you accept the terms).

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/02/image_thumb89.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/02/image89.png>)

Step 5. Click Close

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/02/image_thumb93.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/02/image93.png>)

Now you could follow the rather lame text only instructions for installing the RSAT tools"...

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/02/image_thumb94.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/02/image94.png>)

Or you can follow the nice instructions I have done below with text and IMAGE!!!

Step 1. Open Control Panel and type "features" in the search bar and click on "Turn Windows features on or off".

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/02/image_thumb95.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/02/image95.png>)

Click 2. Expand "Remote Server Administration Tools"

**Note:** You can see the "Remote Server Administration Tools" in the Feature List after you install the MSU file.

New | Old
---|---
[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/02/image_thumb96.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/02/image96.png>) | [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/02/image9_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/02/image97.png>)

Step 3. Expand "Feature Administration Tools" and tick "Group Policy Management Tools" and click "OK"

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/02/image_thumb97.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/02/image98.png>)

Step 4. One its finished installing you can now go to the "Administrative Tools" and you will find the "Group Management Tools" is now listed.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/02/image_thumb98.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/02/image99.png>)

Alternatively"... I find a quicker way to launch the GPMC is to just click start and type "gpmc.msc" and press "Enter"

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/02/image_thumb99.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/02/image100.png>)

### Windows Server 2008 R2

Thankfully its a LOT easier to install GPMC on Windows Server 2008 (and R2) and the install file for the Remote Server Administrator Tools are already on the drive.

Step 1. Open "Server Manager"

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/02/image_thumb100.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/02/image101.png>)

Step 2. Then click on the "Action" menu and then click "Add Features"

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/02/image_thumb101.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/02/image102.png>)

Step 3. Tick "Group Policy Management" and click "Next"

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/02/image_thumb102.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/02/image103.png>)

Step 4. Click "Install"

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/02/image_thumb103.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/02/image104.png>)

Step 5. Click "Close"

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/02/image_thumb104.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/02/image105.png>)

You can now run the Group Policy Management Console from within Server Manager (see below) or launch it as a standalone console the same as with Windows 7.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/02/image_thumb105.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/02/image106.png>)

Happy group policy editing"...