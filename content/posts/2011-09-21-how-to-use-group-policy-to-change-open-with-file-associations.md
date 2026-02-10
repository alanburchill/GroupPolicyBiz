---
title: "How to use group policy to change open with file associations"
date: 2011-09-21 13:00:00
author: admin
categories: ["Tutorials"]
tags: ["file association", "Group Policy"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2011/09/image_thumb.png"
---

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/09/image_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/09/image.png>)Changing file association windows by hacking the registry can be a very challenging task even if you are using Group Policy Preferences Registry option to apply the changes. However there is an option with Group Policy Preferences that allows you to change the Open With (i.e. File association) for any file type.

Below I show you how you can do this using the simple, yet powerful Folder Options by showing you how to change the default association for .TXT files from Notepad to WordPad.

**Step 1**. Edit a GPO that is targeted to the used that you want to apply this setting.

**Step 2.** Navigate User Configuration > Preferences > Control Panel Settings then right click on Folder Options and Navigate to New > Open With .

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/09/image_thumb1.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/09/image1.png>)

**Step 3.** Type in the extension in the [File Extension](<http://technet.microsoft.com/en-us/library/cc771102.aspx>) and then put in the path to the program you want to have open the file. Then optionally tick "Set as default" and press "OK"

**TIP:** When specifying the file path keep in mind that it may be different for x86 and x64 platforms therefore it may be best to use the %ProgramFilesDir% variable.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/09/image_thumb2.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/09/image2.png>)

Your done"... Now when you click on that file type it will open it in the new default open with program you specified.

Before
---
[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/09/image_thumb3.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/09/image3.png>)
After
[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/09/image_thumb4.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/09/image4.png>)