---
title: "Group Policy Setting of the Week 13 "“ Files"
date: 2010-02-08 04:44:34
author: admin
categories: ["Setting of the Week"]
tags: ["Basic", "CRUD", "files", "folder", "Group Policy Preferences"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/02/image_thumb54.png"
---

This week I have selected the Group Policy preference "Files" setting which can be found under either Users or Computers > Preferences > Windows Settings > Files. I commonly see the file update option used where a licence file or a single .exe application needs to be updated on all the computers in an organisation. Here a central copy of the file(s) is stored on a central server and when then central version is updated all the computers will receive the new version of the file at the next policy update. Much better than a logon script!!!! You also have to ensure that the destination folder in the Create, Replate and Update options already exists as it will not automatically create the folder if it doesn't exist. If you do need to create the folder for the destination then use the "Folders" option. Also make sure that if you are copying the file(s) to a location that its under the correct context (e.g. User context for files into their local profile and Computer context if it is being copied into the program files folder). This option is a Create Replace Update and Delete ([CRUD](<http://blogs.technet.com/grouppolicy/archive/2009/11/02/group-policy-preferences-colorful-and-mysteriously-powerful-just-like-windows-7.aspx>)) enabled setting so the behaviour is a little different depending on your action. All these options support wild cards so you can use it to copy (or delete) multiple files.

### Create

This option will copy a file from a location (like a network share) to another location (like on the local computer) only if the destination file does not already exist. [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/02/image_thumb54.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/02/image54.png>)

### Replace

Again, this option will copy a file from a location (like a network share) to another location (like on the local computer) but this option will delete and overwrite the destination if it already exists. [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/02/image_thumb55.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/02/image55.png>)

### Update

This one is very similar to Replace however it only changes the individual attributes that changes. If the file does not already exist then it does the same as the Create option. [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/02/image_thumb56.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/02/image56.png>)

### Delete

As the name suggests it will delete what ever file you specify in the "Delete file(s):" field. Remember this also include wild cards so you can use "C:\Path\\*.*" [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/02/image_thumb57.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/02/image57.png>)