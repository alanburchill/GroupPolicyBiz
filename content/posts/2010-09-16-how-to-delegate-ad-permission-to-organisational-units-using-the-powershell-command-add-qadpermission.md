---
title: "How to delegate AD permission to Organisational Units using the PowerShell command Add-QADPermission"
date: 2010-09-16 15:00:00
author: admin
categories: ["Best Practice", "Tutorials"]
tags: ["Add-QADPermission", "Advanced", "DACL", "Delegate Control", "Powershell", "Quest"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb43.png"
---

Recently, I have been working a lot with PowerShell to automate the creation of a full AD site OU structure (with Group Policy and all) along with all the necessary delegated permissions. One of the limitation of the out of the box AD PowerShell commands is there is no easy way (but apparently there is a [really hard way](<http://blogs.msdn.com/b/adpowershell/archive/2009/10/13/add-object-specific-aces-using-active-directory-powershell.aspx>)) to delegate permission to Active Directory OU's. Luckily [Quest Software](<http://www.quest.com>) have helped a lot here and they have offered a set of FREE PowerShell commands for Active Directory called "[ActiveRoles Management Shell for Active Directory](<http://www.quest.com/powershell/activeroles-server.aspx>)" one of which is called Add-QADPermission which greatly simplifies the process of delegation security in AD. The Add-QADPermission command can be used to add an [DACL security descriptor](<http://technet.microsoft.com/en-us/library/cc785913\(WS.10\).aspx>) permission to any AD object with a distinguished name such as users, computer or OU's. Therefore you can use this to delegate permission to OU similarly to running a "[Delegation of Control Wizard](<http://technet.microsoft.com/en-us/library/cc732524.aspx>)" in [Active Directory Users and Computers](<http://technet.microsoft.com/en-us/library/cc754217.aspx>) console (see image below). This wizard allows you to delegate some common tasks (see below) to your OU's in you Active Directory however the permissions they apply are not straight forward simple permissions.  [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb43.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image43.png>) | [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb18.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image18.png>)
---|---
What I will show you how to do is how to perform some of the common delegation tasks that the "Delegation of Control Wizard" using a PowerShell command so you can automate the process for creating new OU's in your environment. I know this is not strictly an Group Policy topic but it is one closely related and one I think many Group Policy admins will find useful. The Command tasks I will show you are the one's that I almost exclusively use when delegating permissions to Active Directory, they are:

  * Create, delete and manage user accounts
    * and Groups
    * and Computers
  * Reset user passwords and force password change at next logon
  * Modify the membership of a group


### Getting started "“ Installing the [ActiveRoles Management Shell for Active Directory](<http://www.quest.com/powershell/activeroles-server.aspx>)

The Add-QADPermission command is a third party PowerShell command so you will need to first download and install the new commands from the Quest site on the computer that you will be running the PowerShell commands. You can download the Quest ActiveRoles Management Shell for Active Directory from here [http://www.quest.com/PowerShell/activeroles-server.aspx](<http://www.quest.com/powershell/activeroles-server.aspx>) and then install the MSI file.

#### Installing ActiveRoles Management Shell for Active Directory

Step 1. After launching the MSI click "Next" [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb19.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image19.png>) Step 2. Tick "I accept the terms in the Licence Agreement" and click "Next" [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb20.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image20.png>) Step 2. 3lick "Next" [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb21.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image21.png>) Step 4. Click "Next" Note: By ticking the "Change PowerShell execution policy from 'Restricted' to 'AllSigned' you are relaxing the execution policy of PowerShell. However you will still need to turn this off entirely for the testing of your script. [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb22.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image22.png>) Step 5. Click "Install" [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb23.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image23.png>) Step 6. Click "Finish" [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb24.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image24.png>) You have now successfully install the Quest ActiveRoles Management Shell for Active Directory. Now it is time to use the new PowerShell Command.

### Running the add-QADPermission PowerShell command

Step 1. To run the add-QADPermissions PowerShell command click on the PowerShell shortcut (that blue one in the taskbar if you are running 2008/R2). [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb25.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image25.png>) Step 2. Run the command the following command to load the Quest PowerShell commands.

> Add-PSSnapin Quest.ActiveRoles.ADManagement

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb26.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image26.png>) Step 3. To test that the new PSSnapin is loaded type "add-qadper" and then press the "Tab" key to complete the command. [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb27.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image27.png>) This should auto-complete the command to "Add-QADPermission" [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb28.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image28.png>) **REMEMBER:** Every time you launch a new PowerShell window you are going to need to run "Add-PSSnapin Quest.ActiveRoles.ADManagement" to load to load the Quest PowerShell Snapin's otherwise you will see a message like the image below. [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb29.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image29.png>) Now that we have verified that the new Quest AD PowerShell commands lets take a look at the command that will replicate some of the common tasks in the "Delegation of Control Wizard". In our example environment that we have an AD with three top level OU's called "People" "Groups" and "Workstations" (see below). These OU only contain the same type of objects that match the name of the OU (e.g. "People" contains User AD Objects) but it is possible to delegate all the permissions to the same single OU if it contains objects of multiple types (e.g. user,computers and groups). [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb30.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image30.png>)

### Delegating Create, delete and manage user accounts permissions using add-QADPermission

To delegate the same permission as the "Create, delete, and mange user accounts" (effectively Full Control) option in the "Delegation of Control Wizard" (see below) you need to delegate two permissions to the OU. [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb31.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image31.png>)

  1. Allow access to all the properties of the user objects
  2. Create / Delete permission of the user object

The first command will delegate Allow access to all the properties to the group called "User Admins" to all User objects in the OU with the distinguished name of "OU=People,DC=Contoso,DC=Local".

> Add-QADPermission "OU=People,DC=Contoso,DC=Local" "“Account "CONTOSO\User Admins" -Rights GenericAll -ApplyTo ChildObjects -ApplyToType User

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb32.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image32.png>) The second command will delegate Create / Delete permission for the User objects to the same OU for the same group.

> Add-QADPermission "OU=People,DC=Contoso,DC=Local" -Account "CONTOSO\User Admins" -Rights CreateChild,DeleteChild -ApplyTo All -ChildType User

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb33.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image33.png>) Now we can check the security on the People OU in Active Directory Users and Computer to verify the permission has been added correctly. [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb34.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image34.png>)[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb35.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image35.png>) **Note:** See how we have used the "-ApplyTo ChildObjects" parameter and the "ApplyTo All" to ensure that these permission will inherit to all objects in this OU and sub-OU's. If the OU that you want to give the same Full Control permission to a Computers or Groups AD Object type all you need to do is change the -ApplyToType and -ChildType parameter to "computer" or "group" (See examples below)

#### Example delegation Create, delete and manage (a.k.a. Full Control) Groups permissions using add-QADPermission

> Add-QADPermission "OU=Workstations,DC=Contoso,DC=Local" "“Account "CONTOSO\Workstations Admins" -Rights GenericAll -ApplyTo ChildObjects -ApplyToType **Computer** Add-QADPermission "OU=Workstations,DC=Contoso,DC=Local" -Account "CONTOSO\Workstations Admins" -Rights CreateChild,DeleteChild -ApplyTo All -ChildType **Computer**

#### Example delegation Create, delete and manage (a.k.a. Full Control) Computers permissions using add-QADPermission

> Add-QADPermission "OU=Groups,DC=Contoso,DC=Local" "“Account "CONTOSO\Groups Admins" -Rights GenericAll -ApplyTo ChildObjects -ApplyToType **Group** Add-QADPermission "OU=Groups,DC=Contoso,DC=Local" -Account "CONTOSO\Groups Admins" -Rights CreateChild,DeleteChild -ApplyTo All -ChildType **Group**

### Delegating Reset user passwords and force password change at next logon using add-QADPermission

To delegate the same permission as the "Reset user passwords and force password change at next logon" option in the "Delegation of Control Wizard" (see below) you again need to delegate two permissions to the OU. [![image\[48\]](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image48_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image48.png>)

  1. Allow Read/Write to the Password Last Set Attribute
  2. Allow access to the "User-Change-Password" Extended Right

In this example we are going to delegate Allow Read and Write permission to the [Pwd-Last-Set Attribute](<http://msdn.microsoft.com/en-us/library/ms679430\(VS.85\).aspx> "http://msdn.microsoft.com/en-us/library/ms679430\(VS.85\).aspx") to all User objects to the OU with the distinguished name of "OU=People,DC=Contoso,DC=Local" to the group called "User Operators".

> Add-QADPermission "OU=People,DC=Contoso,DC=Local" -Account "CONTOSO\User Operators" -Rights ReadProperty,WriteProperty -Property ('PwdLastSet') -ApplyTo ChildObjects -ApplyToType User

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb36.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image36.png>) Now we are going to delegate permissions to the [Extended Right](<http://msdn.microsoft.com/en-us/library/ms683985\(VS.85\).aspx>) [User-Change-Password](<http://msdn.microsoft.com/en-us/library/ms684413\(VS.85\).aspx>) for the User objects to the same OU for the same group.

> Add-QADPermission "OU=People,DC=Contoso,DC=Local" -Account "CONTOSO\User Operators" -ExtendedRight User-Change-Password -ApplyTo ChildObjects -ApplyToType User

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb37.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image37.png>) Again check the security on the People OU in Active Directory Users and Computer to verify the permission has been added correctly. [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb38.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image38.png>)[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb39.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image39.png>)

### Delegating Modify the membership of a group using add-QADPermission

To delegate the same permission as the "Modify the membership of a group" option in the "Delegation of Control Wizard" (see below) you only need to apply one command to delegate the appropriate permissions. [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb40.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image40.png>)

  1. Allow access to the Read/Write Members property on the Group

In this example we are going to delegate Change group membership permissions on all the Group objects to the OU with the distinguished name of "OU=Groups,DC=Contoso,DC=Local" to the group called "Group Operators"

> Add-QADPermission "OU=Groups,DC=Contoso,DC=Local" -Account "CONTOSO\Group Operators" -Rights ReadProperty,WriteProperty -Property ('member') -ApplyTo ChildObjects -ApplyToType Group

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb41.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image41.png>) As always check the security on the People OU in Active Directory Users and Computer to verify the permission has been added correctly. [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/09/image_thumb42.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/09/image42.png>)

### Summary

When used with the other out of the box AD PowerShell commands you should now be able to fully automate the creation AND delegation of permissions to a new OU structure for your environment.

### References Sites

Below are some useful links to pages that show you how to use PowerShell when working with Active Directory.

  * [Automating Group Policy Management with Windows PowerShell](<http://technet.microsoft.com/en-us/magazine/2009.06.gpmanagement.aspx> "http://technet.microsoft.com/en-us/magazine/2009.06.gpmanagement.aspx")
  * [PowerShell Get-ADUserGroupMembership](<http://www.isaacoben.com/2010/09/14/powershell-get-adusergroupmembership/> "http://www.isaacoben.com/2010/09/14/powershell-get-adusergroupmembership/")
  * [Group Policy Team Blog: Group Policy & Scripting](<http://blogs.technet.com/b/grouppolicy/archive/2010/07/23/group-policy-amp-scripting.aspx> "http://blogs.technet.com/b/grouppolicy/archive/2010/07/23/group-policy-amp-scripting.aspx")
  * [Group Policy Team Blog: PowerShell Script with GP cmdlets: Registry setting, Link](<http://blogs.technet.com/b/grouppolicy/archive/2009/04/28/powershell-script.aspx> "http://blogs.technet.com/b/grouppolicy/archive/2009/04/28/powershell-script.aspx")
  * [TechNet: Active Directory Administration with Windows PowerShell](<http://technet.microsoft.com/en-us/library/dd378937\(WS.10\).aspx> "http://technet.microsoft.com/en-us/library/dd378937\(WS.10\).aspx")
  * [MSDN Blog: Extending Active Directory Powershell](<http://blogs.msdn.com/b/adpowershell/archive/2009/03/20/extending-active-directory-powershell.aspx> "http://blogs.msdn.com/b/adpowershell/archive/2009/03/20/extending-active-directory-powershell.aspx")
  * [The Experts Community: Delegating the PowerShell Way](<http://theexpertscommunity.com/item/view/id/4546> "http://theexpertscommunity.com/item/view/id/4546")

Other AD Security Related Pages
  * [TechNet: Access control in Active Directory](<http://technet.microsoft.com/en-us/library/cc785913\(WS.10\).aspx> "http://technet.microsoft.com/en-us/library/cc785913\(WS.10\).aspx")
  * [TechNet: Delegating administration](<http://technet.microsoft.com/en-us/library/cc778807\(WS.10\).aspx> "http://technet.microsoft.com/en-us/library/cc778807\(WS.10\).aspx")
  * TechNet: Delegate Control of an Organizational Unit