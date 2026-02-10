---
title: "Why Passwords in Group Policy Preference are VERY BAD"
date: 2013-11-25 22:00:40
author: admin
categories: ["Security"]
tags: ["cpassword", "Group Policy Preferences", "MetaSploit", "Password"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2013/11/image_thumb4.png"
---

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/11/image_thumb4.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/11/image4.png>) A long time ago did a blog post explaining how to use the Group Policy [Preferences Local Users](<http://technet.microsoft.com/en-us/library/cc771917.aspx>) setting to manager the password of the local accounts. This post explained how to do it in a way that minimised the exposure of the password in Active Directory (see [How to use Group Policy Preferences to change account Passwords](<https://www.grouppolicy.biz/2010/01/how-to-use-group-policy-preferences-to-set-change-passwords/> "Permanent Link to Best Practice- How to use Group Policy Preferences to change account Passwords") ) for anyone that knew what they were doing. At least as far back as 2009 (and certainly earlier) it was well known that the password was only weakly encrypted and as such could be easily reverse engineer to recover the password. However, for a long time this was much better than the alternative as a lot of administrators would often revert to using scripts that had the password stored as clear text. **Update:** Microsoft has now released MS14-025 which explicitly blocks the configuration of passwords in Group Policy Preferences. See more about this at [Group Policy Preferences Password Behaviour Change "“ MS14-025](<https://www.grouppolicy.biz/2014/05/group-policy-preferences-password-behaviour-change-ms14-025/> "Group Policy Preferences Password Behaviour Change "“ MS14-025") Microsoft has also gone to extensive lengths over the years to warn users about risks of using password in Group Policy preferences: 1\. Via blog posts at [Passwords in Group Policy Preferences (updated)](<http://blogs.technet.com/b/grouppolicy/archive/2009/04/22/passwords-in-group-policy-preferences-updated.aspx> "http://blogs.technet.com/b/grouppolicy/archive/2009/04/22/passwords-in-group-policy-preferences-updated.aspx")

> A password in a preference item is stored in SYSVOL in the GPO containing that preference item. To obscure the password from casual users, it is not stored as clear text in the XML source code of the preference item. However, the password is not secured. Because the password is stored in SYSVOL, all authenticated users have read access to it. Additionally, it can be read by the client in transit if the user has the necessary permissions.

2\. When you look up the Local Users Group Policy Preferences warning it says this"... [![image](https://www.grouppolicy.biz/wp-content/uploads/2013/11/image5.png)](<http://technet.microsoft.com/en-us/library/cc771917.aspx>) 3\. And when you actually configure the password you are warned again before setting the password. [![image](https://www.grouppolicy.biz/wp-content/uploads/2013/11/image_thumb5.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/11/image6.png>)

### So how weakly encrypted is the cpassword?

The CPASSWORD is the filed that is used in the Group Policy Preferences XML configuration file that contains the password. Being an XML file this makes it very easy if find the field by simply looking a the contents of the XML files stored in you SYSVOL. [![image](https://www.grouppolicy.biz/wp-content/uploads/2013/11/image_thumb6.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/11/image7.png>) AND.... Microsoft documents the password that us used to encrypt/decrypt using AES 32-byte encryption (VERY WEAK). If you would like to see the password for yourself it can be found in the official technical specification at <http://msdn.microsoft.com/en-us/library/cc232587.aspx> or"... in the modified screenshot provided below (yes that is the ACTUAL key used to encrypt password in Group Policy). [![image](https://www.grouppolicy.biz/wp-content/uploads/2013/11/image_thumb7.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/11/image8.png>) Now you might be thinking that it is absurd that Microsoft are publishing the key used to encrypt the password however due to the [DOJ settlement with Microsoft ](<http://en.wikipedia.org/wiki/United_States_v._Microsoft_Corp.#Settlement>)back in 2001 Microsoft are required to document its application programming interfaces with third-party companies. This means that the Microsoft are compelled to document this information...

### And now for the REALLY BAD NEWS"....

Since [June 11th 2012](<https://github.com/rapid7/metasploit-framework/commits/master/modules/post/windows/gather/credentials/gpp.rb?page=2>) there has been a [Group Policy Preferences Password](<https://www.rapid7.com/db/modules/post/windows/gather/credentials/gpp>) module added to [MetaSploit](<http://www.metasploit.com/>) that allows you to scan you to discover all the uses of passwords saved in your Active Directory (see description below).

> This module enumerates the victim machine's domain controller and connects to it via SMB. It then looks for Group Policy Preference XML files containing local user accounts and passwords and decrypts them using Microsofts public AES key. Tested on WinXP SP3 Client and Win2k8 R2 DC.

Reference: <https://www.rapid7.com/db/modules/post/windows/gather/credentials/gpp>

### **So what does this really mean?**

Any users that has the MetaSpoit tool installed on their computer and has an account on your domain can scan your Active Directory and decrypt the stored value of password in a Group Policy Preference . Of course once they have the password of the account they can probably use that account which quite often has elevated privileges...

### What Group Policy Preferences are affected ?

While in this post I have focused on the Local Users account password option this is not the only location that you can save a password. In fact there are five separate location in Group Policy Preferences that a save password option can be found.

  * **Local User preference items**

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/11/image_thumb8.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/11/image9.png>)

  * **Data Source preference items**

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/11/image_thumb9.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/11/image10.png>)

  * **Mapped Drive preference items**

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/11/image_thumb10.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/11/image11.png>)

  * **Scheduled Task or Immediate Task preference items**

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/11/image_thumb11.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/11/image12.png>)

  * **Service preference items**

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/11/image_thumb12.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/11/image13.png>)

### Update: How do I know here I have this password configured?

[Darren Mar-Elia](<http://www.twitter.com/grouppolicyguy>) at [SDMSoftware](<http://sdmsoftware.com/>) has now written a PowerShell script that allows you to identify all the location in your domain that the Group Policy Preference password exists. Check it out at <http://sdmsoftware.com/group-policy-blog/tips-tricks/getting-rid-of-passwords-in-group-policy-preferences/>

### Should I blame Microsoft for this security issue?

In my opinion, No. This security risk as been in Group Policy Preferences ever since Microsoft bought PolicyMaker. They have also documented a number of time (see above) the risks associated with using this option. Security is also an ever changing field and at the time even weakly encrypted password was better than what most IT administrators otherwise did to do the same task.

### So what do I do?

Firstly"... Stop configuring any new password in Group Policy Preferences. Then to find any XML files stored in your SYSVOL (yes there will be a LOT). Open the XML files and then find any that have a configured CPASSWORD value and remove them using either using the Group Policy Preferences UI or by just delete the value our of the XML manually. Once this is done the password value is set to null thus removing the value from Active Directory and mitigating the risk. [![image](https://www.grouppolicy.biz/wp-content/uploads/2013/11/image_thumb13.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/11/image14.png>) As they are Group Policy Preferences the value will persist on the computers/accounts that are already configured. However any new computers will not get the new value configured so keep this in mind as it will probably affect any computer build process you already have in place that uses this setting. And yes"... this means you will need to implement an alternative way to manage password on your computers in your organisation. Certainly all this news a PITA, however it is something as a Group Policy administrator you must be aware of and actively stop in your organisation... Additional References: [Group Policy Preferences Password Behaviour Change "“ MS14-025](<https://www.grouppolicy.biz/2014/05/group-policy-preferences-password-behaviour-change-ms14-025/> "Group Policy Preferences Password Behaviour Change "“ MS14-025")NICE