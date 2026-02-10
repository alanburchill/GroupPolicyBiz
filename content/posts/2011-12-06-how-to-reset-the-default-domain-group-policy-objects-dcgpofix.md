---
title: "How to reset the Default Domain Group Policy Objects (DCGPOFIX)"
date: 2011-12-06 13:00:00
author: admin
categories: ["Tutorials"]
tags: ["dcgpofix", "Default Domain", "Reset"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2011/12/gp_logo_thumb.png"
---

[![gp_logo](https://www.grouppolicy.biz/wp-content/uploads/2011/12/gp_logo_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/12/gp_logo.png>)If you have ever read my [Best Practice for Group Policy](<https://www.grouppolicy.biz/2010/07/best-practice-group-policy-design-guidelines-part-2/>) blog post then you will know that I encourage you to edit the default domain GPO's sparingly. The only exception I would make to this rule is when you want to modify the default domain password policy but even then you can create a new password policy GPO linked at the domain level (See [Tutorial: How to setup Default and Fine Grain Password Policy](<https://www.grouppolicy.biz/2011/08/tutorial-how-to-setup-default-and-fine-grain-password-policy/>) )

Even if you don't want to take my word for it here is a reference on the TechNet web site say pretty much the same thing"...

[TechNet: Establishing Group Policy Operational Guidelines](<http://technet.microsoft.com/en-us/library/cc779159\(WS.10\).aspx>)

> Do not modify the default domain policy or default domain controller policy unless necessary. Instead, create a new GPO at the domain level and set it to override the default settings in the default policies.

So"... Lets assume you have done everything wrong and either the Default Domain and/or the Default Domain Controller Group Policy objects have been modified and you want to reset them back. Of course you have a backup of the GPO's which are good and you simply restore them".... ![Winking smile](https://www.grouppolicy.biz/wp-content/uploads/2011/12/wlEmoticon-winkingsmile.png)

BUT"... You have never backed up the default GPO's and you need to reset the setting".... Well the tool that allows you to do this is called DCGPOFIX and it can be found on any Windows Server 2003 or later windows server.

**NOTE:** Even though we are restoring the default domain GPO's back to a default setting doing so may still cause more issues. Therefore make sure you have a current back of your default domain so you can easily undo this change if needed (see below).

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/12/image_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/12/image.png>)

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/12/image_thumb1.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/12/image1.png>)

**TIP:** Even if you are not going to run this command I would still make of these Default Domain GPO's now"... right now".... Go on"... Its not going to hurt and this will at least give you something to roll back if you need to in the future.

The command to restore the GPO's to default is as simple as running the "DCGPOFIX.exe" from a command line and press "Y" twice when prompted.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/12/image_thumb2.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/12/image2.png>)

Now you are done. You will notice any changes to the GPO have now been removed or reverted back to the default settings. Monitor your systems for any adverse affect and make sure that you have another backup of the GPO's for future reference.

**Note:** By default this command will not run if the version of the OS does not match that of the Schema version in AD.

References:

  * [The Dcgpofix tool does not restore security settings in the Default Domain Controller Policy to their original state](<http://technet.microsoft.com/en-us/library/cc784165\(WS.10\).aspx> "http://technet.microsoft.com/en-us/library/cc784165\(WS.10\).aspx")
  * [Core Group Policy Tools and Settings](<http://technet.microsoft.com/en-us/library/cc784165\(WS.10\).aspx> "http://support.microsoft.com/kb/833783")