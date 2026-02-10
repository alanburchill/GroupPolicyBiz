---
title: "How to setup Work Folder using Group Policy"
date: 2013-07-22 13:54:00
author: admin
categories: ["Tutorials"]
tags: ["iPad", "Windows 7", "Windows 8.1", "Windows Server 2012 R2", "Work Folders"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2013/07/image_thumb9.png"
---

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/07/image_thumb9.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/07/image9.png>)Work Folders is a great new server role feature with Windows Server 2012 R2 that allows your end user to sync their files over multiple device at work and at home. Think of it as SkyDrive hosted on Windows Server in your own server room rather than by a third party. While there are a lot more technically impressive features in the new OS I think this will be the one that that will get the most traction. The ability for you to now host your own "private cloud" file synchronisation service but do it in a way that is secure and manageable is going to be the greatest thing since you could get email via ActiveSync. In the following post I will show you how to setup this new feature automatically via Group Policy so that you client workstation can automatically (or on demand) to simplify the setup for your users.

But first the basics"...

### Setting up the Work Folders Server Role and Share

The Work Folder server is just another file server role that can be added to the OS. Once it is setup you then need to create a work folder share on this server with its associated security group. For full instructions on setting this up I would refer to the setup lab instructions at <http://blogs.technet.com/b/filecab/archive/2013/07/10/work-folders-test-lab-deployment.aspx>

### Work Folder Client Setup Process

Microsoft has announced that the Work Folders client will be in the box for Windows 8.1 and Windows 8.1 RT both domain and non-domain joined. They will also be releasing a add-on client for Windows 7 and an App for the iPad (yes, iPad). Due to wide range of clients that this feature support Microsoft have a number or different scenarios for setting up the clients. Below is process work flow for setting up the client, as you can see it can be implemented in both manually by the user, automatically or a mix of both.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/07/image_thumb21.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/07/image21.png>)

For the purpose of this article I will be covering the client group policy setting that will be applied to the domain joined computers however the DNS configuration change will also cover the non-domain joined computers.

### How Auto Discover DNS for Work Folders

The Auto Discover process for Work Folders is actually similar to how exchange Auto Discover process works via DNS"... That is the address that Work Folders tries to find is a DNS address based on the email entered by the user when they follow the setup wizard.

During the manual setup of the Work Folder they will be prompted for their work email address.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/07/image_thumb11.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/07/image11.png>)

The setup wizard then takes the email address and remove everything before the @ symbol and adds the "workfolders" to the address to <http://workfolders.domainname.com/sync/1.0>

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/07/image_thumb12.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/07/image12.png>)

This means a user with an email of [username@domainname.com](<mailto:username@domainname.com>) will need to have a DNS record (see image below) of workfolders.domainname.com setup that points to the discovery work folder server. While the setup of the DNS address for work folders address is not mandatory if you are using group policy (or SCCM) to configure the URL it does make it a lot easier for setting up if you have a mixture of non-domain joined (non managed) devices and domain joined devices.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/07/image_thumb13.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/07/image13.png>)

Work Folders is also smart enough to route the user to their own work folder servers seamlessly when the user first connected (similar to exchange). This means you simply need to point all your work folders server users to the same address and then it will be smart enough for it to work out what server the user need to connect.

**Note:** As the address is based on the users email the DNS zone will need to be a publicly addressable name space. Therefore you probably need to have a split brain DNS setup in your environment so the external DNS zone points to the externally published IP address and the Internet DNS Zone points to the internal IP address of the main work folders server.

### How to configured the Work Folders client via Group Policy

Now that you have the server and the DNS auto discovery setup its time to configured the Group Policy for the domain joined computers. We now have two options to either set it up either fully automatically or manually initiated by the user. The manually initiated by the user option simply provides a hardcoded URL for the user if the Work folders DNS address is not setup.

**Tip:** As all work folders user need to be in a security group you could filter this group policy object using the same security group to target just the users that are work folders enabled.

Enable the "Specify Work Folders settings" all users under Users > Policies > Administrative Templates > Windows Components > Work Folders to all your workstations then type in the URL (example. <https://workfolders.corp2.local/sync/1.0>). If you then want the policy to automatically configure with Work Folders client also check the "Force automatic setup" option.

**Note:** Example provided will not work externally as it is a private namespace. However if you are just setting it up for a test lab or internally the use of an internal name space is fine.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/07/image_thumb14.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/07/image14.png>)

**Tip:** I do not recommend that you try to apply multiple GPO / URLs to your users to route them manually to the correct work folder server. Doing it this way would take a lot more administrative effort and could mean you get multiple orphan work folders spread out your organisation.

If you did not enable the "Force automatic setup" you also have the option to override this base on a computer policy by enabling the "Force automatic setup for all users" under Computer > Policies > Administrative Templates > Windows Components > Work Folders to all your workstations.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/07/image_thumb15.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/07/image15.png>)

If you have not enabled the Force Setup option the user just needs to go to the work folders control panel item and click on "Set up Work Folders" it will then just confirm the work folders location and security policies and it will be all setup.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/07/image_thumb16.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/07/image16.png>)


If you have enabled the Force Setup option the user will now have work folders configured.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/07/image_thumb17.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/07/image17.png>)

If the user tries to stop using work folder by clicking on the "Stop using Work Folders" option then it will say that it is allowed, but they will then be told that it will be setup again then next time they logon (see below).

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/07/image_thumb18.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/07/image18.png>)[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/07/image_thumb19.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/07/image19.png>)

So there you have it"... Some rather simple policy settings that get Work Folder working quickly in your organisation"...

**Note:** The information in this blog post is based on the Windows 8.1 Preview and Windows Server 2012 R2 Preview. I will update this post if there are any changes in the RTM version once it is released.

**Reference** : **msDS-SyncServerUrl attribute** <http://blogs.technet.com/b/filecab/archive/2013/10/09/a-new-user-attribute-for-work-folders-server-url.aspx>