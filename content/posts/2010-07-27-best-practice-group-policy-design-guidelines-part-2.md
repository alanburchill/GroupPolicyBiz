---
title: "Group Policy Design Guidelines &ndash; Part 2"
date: 2010-07-27 09:00:00
author: admin
categories: ["Best Practice", "Tutorials"]
tags: ["Active Directory", "AD", "Advanced", "AGPM", "Design", "DFS-R", "Enforced", "GPMC", "GPO", "Group Policy", "Guidelines", "RSAT", "Secuirty Filtering", "SYSVOL", "WMI filtering"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb84.png"
---

In my previous article In this article [Best Practice:Active Directory Structure Guidelines "“ Part 1](<https://www.grouppolicy.biz/2010/07/best-practice-active-directory-structure-guidelines-part-1/>) I spoke about some of the guidelines I personally use when developing an Active Directory OU structure. In this next part I will discuss some guidelines I use when designing a Group Policy Object infrastructure.

Ideally you should make the the Active Directory OU and GPO design decision together to best ensure that you have the most efficient design possible. However if you have an existing OU structure designed a lot of these guidelines can still be applied to most existing environments. As in [Part 1](<https://www.grouppolicy.biz/2010/07/best-practice-active-directory-structure-guidelines-part-1/>) these are simply guidelines that I use and should not be taken as hard an fast rules. I quite often finding myself having to break these rules due to real world conflicts or just because one rule might conflict with the other rule. If you do find your self in a situation where you are not sure which path to take try to chose the option that will result in the least administrative effort in the long term.

## Active Directory Group Policy Design Guidelines

### Keep the GPO's name consistent with the OU names

When naming the GPO try to keep the name of the policy the same as the concatenated name of all the OU's to where the group policy object is applied. Having the fully concatenated name will make it intently know what that policy is applied when just looking at the GPO name. This is very handy to know when looking at a Group Policy Results report which only gives you the name of the GPO without the linked OU details.  **Bad Example "Workstations"** | **Good Example "Sydney Workstations"**
---|---
[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb84.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image89.png>) | [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb85.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image90.png>)
In keeping with having names consistent this also means you should adhere to the same naming conventions as mentioned in [Part 1](<https://www.grouppolicy.biz/2010/07/best-practice-active-directory-structure-guidelines-part-1/>) with the OU's (i.e. "Keep it short", "Be Intuitive" & "Most to least signification from left to right"... So in saying that please read the next guideline"...

#### References

[TechNet: Establishing Group Policy Operational Guidelines](<http://technet.microsoft.com/en-us/library/cc779159\(WS.10\).aspx> "http://technet.microsoft.com/en-us/library/cc779159\(WS.10\).aspx")

> Define a meaningful naming convention for GPOs that clearly identifies the purpose of each GPO

### Don't use the work "POLICY" or "GPO" in the GPO name

Nothing annoys me more to see a group policy called "Workstations Policy" or "Workstation GPO".... I KNOW ITS A POLICY!!!! I AM LOOKING AT IT IN THE GROUP POLICY MANAGEMENT CONSOLE. Please drop the work "policy" or "GPO" from the name of the Group Policy object as you are simple adding more characters to what might already be a long name only for the sake of pointing out the obvious. I also realise that the two GPO's that come with AD are called "Default Domain Policy" and "Default Domain Controller Policy" which goes against this rule"... [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb116.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image121.png>) Remember at the start of [part 1](<https://www.grouppolicy.biz/2010/07/best-practice-active-directory-structure-guidelines-part-1/>) how rules were meant to be broken"... So I do NOT recommend that you rename these polices there is just to much risk and confusion that doing this might cause. But this would have to be the only exception to this rule that I would be happy to let though"...

### Treat your terminal servers like workstations

Terminal Servers (now known as Remote Desktop Services) are essentially a multi-user workstation and as such should be treated more as a workstation than a server. Ideally you should configure you Terminal Server to be as close as possible as your workstations to provide your users with a consistent experience. The best way to make sure the configuration is consistent is to apply the same policy settings to the Terminal Serves as your workstations. That being said don't apply the same computer Group Policy Object to the Terminal Servers if for no other reason than it helps reduce the risk of making a change to a workstation that could affect the stability of the servers (e.g. Automatic Update reboot schedule). Therefore you will need to maintain some level of manually synchronisation between you default workstation and terminal server policy. Unlike computer GPO's it far more acceptable to apply the same user GPO's to your users when logging on to the Terminal Server as the GPO are applied to the User Object rather than the computer account. Using the same policy means that any changes made to the user policies will automatically apply to terminal servers without the administrative overhead of making duplicate updates when there are policy changes. If you have any user configuration that you want to configure that is specific to the terminal servers (e.g. [disable adding PST file](<http://support.microsoft.com/kb/896515>)) then you can override this policy using the [Group Policy Loopback](<http://support.microsoft.com/kb/260370>) option on the computer GPO you apply to the Terminal Server. This is another reason why you would want to have a separate computer GPO as it allow you to apply specific Terminal Server user settings via a loopback policy. For more information on troubleshooting Loop back policies check out [Loopback Policy Processing Debug Series | CB5 Blog](<https://www.grouppolicy.biz/2010/02/loopback-policy-processing-debug-series-replace-mode-cb5-blog/>) and [Aaron Parker's StealthPuppy](<http://blog.stealthpuppy.com/> "http://blog.stealthpuppy.com/") blog.

#### Reference

[TechNet: Using Loopback Processing to Configure User Settings](<http://technet.microsoft.com/en-us/library/cc757470\(WS.10\).aspx> "http://technet.microsoft.com/en-us/library/cc757470\(WS.10\).aspx")

> The **User Group Policyloopback processing mode** policy setting is an advanced option that is intended to keep the configuration of the computer the same regardless of who logs on. This option is appropriate in certain closely managed environments, such as servers, terminal servers, classrooms, public kiosks, and reception areas.

### New GPO's only when scope is different

I have seen some organisations apply many Group Policy Objects (GPO's) to the same OU. There are a number of reason why you might want to do this however you should really consider why you want spawn another GPO as each one will add about 5mb to you Active Directory SYSVOL. But if you start creating lots of GPO objects then you can quickly blow out your the size and performance of your SYSVOL. This is not such a problem if you have [upgraded to a DFS-R SYSVOL](<http://blogs.technet.com/b/notesfromthefield/archive/2008/04/27/upgrading-your-sysvol-to-dfs-r-replication.aspx>) replication or you have configured a [Group Policy Central Store](<http://support.microsoft.com/kb/929841/en-gb>) for your Windows Vista and later computers but its still good practice to keep the number of GPO's as low as possible.

### Monolithic vs. Functional GPOs

Now that I have just told you that you should load up your GPO's with lots of setting rather than having lots and lots of separate GPO's [Mike Kline](<http://adisfun.blogspot.com/>) has referred me to the this great article [Best Practice for Optimizing Group Policy Performance](<http://technet.microsoft.com/en-us/magazine/2008.01.gpperf.aspx> "http://technet.microsoft.com/en-us/magazine/2008.01.gpperf.aspx") by Darren Mar-Elia that talks about Monolithic vs. Functional GPOs.

> The terms "monolithic" and "functional" refer to how you design them. Monolithic GPOs contain settings from many different areas. For example, a monolithic GPO might contain settings from Administrative Templates, Internet Explorer Maintenance, and Software Installation policies"”all within a single GPO. By contrast, functional GPOs typically do one thing. For example, a functional GPO may do only Software Installation or enforce Security settings.

I totally agree with this and my advice to you when trying to decide which to use that your should pick the type of policy configuration that suites your needs. This also maps very nicely to the 80/20 examples you will see below where you take a more Monolithic approach to the 80% GPO's and more Functional to the 20%. The 80% policies are going to have more setting in them but they will be relatively static where the 20% policies will have fewer settings but probably need to be updated more frequently. This way you should be able to balance the pro's and con's of each policy type in your environment.

#### References

[TechNet: Complying with Service Level Agreements](<http://technet.microsoft.com/en-us/library/cc787003\(WS.10\).aspx> "http://technet.microsoft.com/en-us/library/cc787003\(WS.10\).aspx")

> If you have large or complex GPOs that require frequent changes, consider creating a new GPO that contains only the sections that you update regularly.

### Setting (not policies) = Slower SOE

It is often a misconception that splitting up your group policy setting into a lot of Group Policy Objects (GPO's) will slow down Group Policy on your computers. While this might be true if you have many 100's (or thousands) of GPO's applied to your computer this is not normally the reason why computer may slow down processing Group Policies. Normally you will find that its the number of settings you have applied that will cause performance issues and even then you will find that particular setting that will cause more of a performance hit than other. In my experience the policy setting that cause the most likely affect performance are:

  1. Printer Mappings (100+)
  2. Folder Redirection (Especially with Windows XP and AppData Redirection)

You should also expect that the first time a users logs on with a new account that they should expect a slow logon as the computer will need to apply all policy setting. However subsequent logon's should be much faster as the computer is then only checking the policy is still applied. This is similar to the difference between running a "GPUPDATE" and a "GPUPDATE /FORCE" . You should also check out the [Best Practice for Optimizing Group Policy Performance](<http://technet.microsoft.com/en-us/magazine/2008.01.gpperf.aspx> "http://technet.microsoft.com/en-us/magazine/2008.01.gpperf.aspx") post by Darren Mar-Elia as this post explains in detail how GPO are applied and what you can do to tweak performance. While it would be fairly rare to have an environment that has more than a 999 GPO's applied to a single computer still be aware there is a hard limit on the number of GPO's you can apply to any user or computer. Thus trying to keep the number GPO's to a as few as possible is a good idea especially in very large organisations that may uses separate GPO's for installing software packages.

#### Reference

[TechNet: Determining the Number of Group Policy Objects](<http://technet.microsoft.com/en-us/library/cc758134\(WS.10\).aspx> "http://technet.microsoft.com/en-us/library/cc758134\(WS.10\).aspx")

> Note that a maximum of 999 GPOs is supported for processing GPOs on any one user or computer. If you exceed the maximum, no GPOs will be processed.

### Disable User/Computer settings if not in use

If you are creating a GPO that is only meant to be applied to computers (and vice versa for users) then you should disable the unused portion of the GPO. This not only helps guards against accidental change to the section of the GPO that should not be applied it should also give you a small performance boost processing policies on your computers as the GPO does not un-necessarily evaluate parts of the policy that are not configured with any settings. While I have never seen a performance benefit in disabling the unused portion of a GPO or based on the number of GPO's applied to a computers (see "Settings (not polices) = Slower SOE)" section above) I do encourage that you adhere to these principals to avoid [Death of a thousand cuts](<http://en.wikipedia.org/wiki/Death_of_a_thousand_cuts> "http://en.wikipedia.org/wiki/Death_of_a_thousand_cuts") when it comes to the performance of your systems. [TechNet: Complying with Service Level Agreements](<http://technet.microsoft.com/en-us/library/cc787003\(WS.10\).aspx> "http://technet.microsoft.com/en-us/library/cc787003\(WS.10\).aspx")

> If a GPO contains only computer or user settings, disable the portion of the policy that does not apply. The destination computer does not scan the portions of a GPO that you disable, which reduces processing time

### Avoid using Enforced

In all my time as an Group Policy Administrator I cannot real once a scenario that I required the use of the Enforced feature of Group Policy. At all cost you should avoid this setting as doing so is like using big hammer to a problem that you can probably avoid if designed right. (RESIST THE URGE) [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb117.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image122.png>)

#### References

[TechNet: Designing Your Group Policy Model](<http://technet.microsoft.com/en-us/library/cc736938\(WS.10\).aspx> "http://technet.microsoft.com/en-us/library/cc736938\(WS.10\).aspx")

> Use the **Enforced** and **Block Policy Inheritance** features sparingly. Routine use of these features can make it difficult to troubleshoot policy because it is not immediately clear to administrators of other GPOs why certain settings do or do not apply

### Reuse GPO's where possible

If you are in a situation that you want have the same settings you want to apply to all the users or computers in specific OU's your organisation then consider linking the same GPO to these OU's. When naming the GPO chose a name that represents what is common to what you are applying. This is shown in the image below (and in "80/16/4 Example 2") where the policy is named "People Manufacturing" as this is the common two values to where to policy is being applied.  [![image\[62\]](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image62_thumb1.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image622.png>) The means the "Sydney" and "Coolangatta" is ignored as that would result in a long policy name of "People Sydney and Coolangatta" Manufacturing". It would be obviously longer again if you had the policy linked to many more sites.

### If you have Software Assurance use the Advance Group Policy Management (AGPM) tool

Advanced Group Policy Management (a.k.a. AGPM) is a tool that is available to anyone who is licensed to have Software Assurance. This programs is a change management tool that allows you to check-in and check-out GPO as well as create a list of changes and an audit trail of change to GPO's. You can check out my AGPM install and configuration series at [AGPM Part 1: Introduction to Advanced Group Policy Management (a.k.a AGPM) v4](<https://www.grouppolicy.biz/2010/06/introduction-to-advanced-group-policy-management-a-k-a-agpm-v4/>). If you have a Group Policy infrastructure of any size or if you have more than one person who is responsible for making changes to GPO's then this is definitely something you should consider. AGPM is also very good at avoiding GPO editing conflicts as you will find that the "last writer will win" when making policy changes. This means that in an environment that has multiple GPO admins you might find that you could be overwriting each other changes with un-expected results. AGPM gets around this issues as it support the method of checking in and out GPO's for editing meaning that now two GPO administrators can edit a GPO at the same time thus eliminating the possibility of overwriting each other changes. For even more information on AGPM check out the following links: [Microsoft MDOP Blog](<http://blogs.technet.com/mdop>) [TechNet: Overview of Advanced Group Policy Management](<http://technet.microsoft.com/en-au/library/ee532079.aspx>) [TechNet: A Video tour of Advanced Group Policy Management](<http://technet.microsoft.com/en-us/windows/ee526426.aspx>) [TechNet: Technical Overview of AGPM](<http://technet.microsoft.com/en-au/library/ee390978.aspx>) [TechNet: What's New in AGPM](<http://technet.microsoft.com/en-us/library/ee390977.aspx>) [TechNet: Choosing Which Version of AGPM to Install](<http://technet.microsoft.com/en-au/library/dd553090.aspx>) [TechNet: Step-by-Step Guide for Microsoft Advanced Group Policy Management 4.0](<http://technet.microsoft.com/en-us/library/ee378482.aspx>) [TechNet: Operation Guide for Microsoft Advanced Group Policy Management 4.0](<http://technet.microsoft.com/en-us/library/ee390965.aspx>) [Group Policy Blog: Importing and Exporting with AGPM](<http://blogs.technet.com/b/grouppolicy/archive/2010/06/11/importing-and-exporting-with-agpm.aspx>)

### Create a Test Group Policy Structure

Implement something like AGPM is an excellent way to make sure you have a proper rollback strategy for making changes to Group Policy but sometimes you just want somewhere to test the policy functionality before you put it into production. I would definitely recommend having an isolated replica of the AD structure in for making test however the problem with these environment is that they are normally not a 100% representation of the production environment. Therefore as a second step in your testing of policy changes before being applied to productions systems you should create a test GP structure that will allow have a selection of users and computers that are in production but are not mission critical. Best to select users that you know are easy to get along with and wont scream to loud when you break something. You can even apply your own computer and users account to this test GP structure but make sure that this is not your only account as you want your computer to still be able to work so you can undo your changes in case you royally stuff something up.

#### OU Method

The image below shows how you could implement a Test OU/GP structure however by creating a separate OU structure to test your group policy. This method provides excellent isolation of your test computers and users to production which may be desired if you want to lessen the impact of any bad configuration changes. However this would mean that you would have the overhead of needing to ensure that all configuration changes to the production GPO's are also replicated to these. Otherwise you may end up with your test environment being configured differently to your production GPO. [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/08/image_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/08/image.png>)

#### Security Group Filtered Method

The Security Group Filtered method applies the test GPO's to the existing OU structure but they are security filtered so they will only apply to the users or computers you want to test. The test GPO will only have the delta configuration changes applied to it for the policy setting that you are testing therefore all other production policies will be implicitly applied to the test objects. Therefore you test computers and users are as close as possible representation of production because they are subject to the production policies. This also mean you do not need to make duplication configuration changes to the GPO's when you do make production changes as the test computers will automatically have the production policies applied. The down side to this method is that unless you are carful in how you apply your security filtering you may inadvertently apply the test changes to your computers users and computers as they are all under the same scope of the test GPO. Another disadvantage of this method is that as you are relying upon security groups to apply the users or computer to the test policy it is possible that you could be a member of multiple test groups and thus be subject to multiple conflicting test GPO's which may make the results somewhat unpredictable. When not testing GPO changes the Test GPO's should remain configured without any settings and/or the link to the OU should be disable to avoided any extra policy processing overhead to the production users and computers. [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/08/image_thumb1.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/08/image1.png>)

#### Hybrid Method

This method combines both a separate OU structure and separate GPO's but avoids having to use security group filtering. The advantage of this method is that you test environment is still subject to the production GPO's however the test policies are only applied to the users and computers that are located in the Test OU structure. This method totally mitigates accidently applying a test configuration to your production computers and it also eliminates the need to duplicate configuration changes to your production environment. [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/08/image_thumb2.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/08/image2.png>)

#### Reference

[TechNet: Establishing Group Policy Operational Guidelines](<http://technet.microsoft.com/en-us/library/cc779159\(WS.10\).aspx> "http://technet.microsoft.com/en-us/library/cc779159\(WS.10\).aspx")

> Always stage Group Policy deployments using the following pre-deployment process

[TechNet: Designing Your Group Policy Model](<http://technet.microsoft.com/en-us/library/cc736938\(WS.10\).aspx> "http://technet.microsoft.com/en-us/library/cc736938\(WS.10\).aspx")

> Prepare a staging environment to test your Group Policy-based management strategy before deploying GPOs into your production environment.

[TechNet: Deploying Group Policy](<http://technet.microsoft.com/en-us/library/cc737330\(WS.10\).aspx> "http://technet.microsoft.com/en-us/library/cc737330\(WS.10\).aspx")

> Always fully test your GPOs in safe (nonproduction) environments prior to production deployment

### Backup Often

Especially if you don't have something like AGPM installed in your environment you should seriously consider making a PowerShell script that simple backs up all your new GPO's in your Active Directory every night. Having back up copies of you GPO is very handy especially if you have miss-configured something and you quickly want to rollback to last known good policy setting. For more information on how to do this with PowerShell visit [PowerShell Script: Backup all GPOs that have been modified this month](<http://blogs.technet.com/b/grouppolicy/archive/2009/03/26/powershell-script-backup-all-gpos-that-have-been-modified-this-month.aspx> "http://blogs.technet.com/b/grouppolicy/archive/2009/03/26/powershell-script-backup-all-gpos-that-have-been-modified-this-month.aspx") from the [Group Policy Team Blog](<http://blogs.technet.com/b/grouppolicy/>).

#### References

[TechNet: Defining Group Policy Operational Procedures](<http://technet.microsoft.com/en-us/library/cc738553\(WS.10\).aspx> "http://technet.microsoft.com/en-us/library/cc738553\(WS.10\).aspx")

> You should also create regular backups of your GPOs

### Edit Default Domain Policies Sparingly

Unless you are changing the default domain password policy then it is strongly recommended that you do not modify the Default Domain or Default Domain Controller group policy objects as making a mistake in these two policies up can really mess up your Active Directory. If you want to make a change to all your DC or your entire domain then consider making a separate new group policy at the same level as the default policies. This will at least allow you to un-do any change selectively disabling the offending policies if something does go wrong.

#### Reference

[TechNet: Linking GPOs](<http://technet.microsoft.com/en-us/library/cc736813\(WS.10\).aspx> "http://technet.microsoft.com/en-us/library/cc736813\(WS.10\).aspx")

> If you need to modify some of the settings contained in the **Default Domain Policy GPO** , it is recommended that you create a new GPO for this purpose, link it to the domain, and set the **Enforce** option. In general, do not modify this or the **Default Domain Controller Policy GPO**. If you do, be sure to back up these and any other GPOs in your network by using GPMC to ensure you can restore them.

[TechNet: Establishing Group Policy Operational Guidelines](<http://technet.microsoft.com/en-us/library/cc779159\(WS.10\).aspx> "http://technet.microsoft.com/en-us/library/cc779159\(WS.10\).aspx")

> Do not modify the default domain policy or default domain controller policy unless necessary. Instead, create a new GPO at the domain level and set it to override the default settings in the default policies.

**Update:** Here is another post I have found that confirms this <http://jorgequestforknowledge.wordpress.com/2011/10/23/best-practices-for-the-default-domain-policy-and-the-default-domain-controllers-policy-gpos/>

### Avoid using Group Policy Software Assignment

I know it sounds strange for a Group Policy expert to say avoid using Group Policy but this is definite one case where you should consider using other software deployment products due to their vastly superior features. Group Policy Software Installations (a.k.a. GPSI) is a way you can deploy an MSI based application to your computers using Group Policy. This can be very useful way of deploying a standard set of applications to your computers however when compared to the advanced targeting features of SCCM software deployment or App-V this limitations of this method of software deployment quickly becomes evident. One common problem I see when deploying software this way is the "Un-install when falls out of scope" options. This can be very handy when you want to move a computer to another OU and you want all the software packages that are not needed any more to un-install. This is even worse when you try to move an computer between domains as the computer will then un-install and re-install all the applications assigned to it which can take a VERY LONG time. Even when you have the "Un-install when falls out of scope" not ticked on the source domain and you move the computer to a new domain you will find that the installer service will still need to do a repair/check install of all the applications of the new domain even if the applications are already installed. However this also means that when the computer is removed from a domain then you have to wait for all the application's to un-install during the next reboot. The un-installing of application can obviously take a long time if you have many applications install via this method. If you don't select this options then you will find that your computer will over time build up the a number of installed applications installed on your computers that will affect performance, stability and licensing costs. The other inflexibility of doing software assignment to the computers via GPSI is that they will only install on the next reboot of the computer. Meaning that a user will need to do a full reboot of their computer before they will be able to start using the new applications. The other restriction of GPSI is that you are limited to deploying only Microsoft Software Install (a.k.a. MSI) packages. Where tools like SCCM and App-V will allow you to deploy application via a silent command line option or via a [sequenced application](<http://download.microsoft.com/download/F/7/8/F784A197-73BE-48FF-83DA-4102C05A6D44/App-46_Sequencing_Guide_Final.docx>). So due to all these targeting issues with GPSI software then I strongly recommend that you consider using either Microsoft SCCM package deployment or Microsoft App-V due to the superior targeting and features these products offer. For more information on the advantages of Microsoft App-V then i strongly recommend that you checkout the series of App-V FAQ at <http://blog.stealthpuppy.com/tag/appvfaq> .

#### References

[Office 2007 Deployment via Group Policy](<http://blog.stealthpuppy.com/group-policy/office-2007-deployment-via-group-policy> "http://blog.stealthpuppy.com/group-policy/office-2007-deployment-via-group-policy")

> Office 2007 is no longer deployed using transform files

Below are the only scenarios that should be used when deploying Office 2007 via GPSI. While this article is specific to Office 2007 I would also say that the same limitations should be used when considering GPSI for other applications as well. [TechNet: Use Group Policy Software Installation to deploy the 2007 Office system](<http://technet.microsoft.com/en-us/library/cc179214\(office.12\).aspx> "http://technet.microsoft.com/en-us/library/cc179214\(office.12\).aspx")

> You can use the Software Installation extension of Group Policy to deploy the 2007 Office system to _computers_ if the following conditions exist:

>
>   * Small organizations that have already deployed and configured Active Directory

>   * Organizations or departments that comprise a single geographic area

>   * Organizations with consistent hardware and software configurations on both clients and servers

>


### Never edit Group Policy Objects from the Domain Controller

To often I see people editing their GPO's directly from a Domain Controller in their organisation as they are not aware they can do this remotely. The Remote Server Admins Tools (a.k.a. RSAT) have will give you the option to install (See [instructions here](<https://www.grouppolicy.biz/2010/03/how-to-download-and-install-the-group-policy-management-console-gpmc/>)) the Group Policy Management Console on any workstation or server running Vista/2008 or greater. I strongly encourage you to do this as if you are performance day to day management of your active directory (e.g. Creating users, editing Group Policy and adding/removing users from groups) then sooner or later you will find that you might affect the stability of your DC (which would be BAD).

### Apply policies as high as possible

When given the choice of applying the same policy at multiple lower locations or just one locations higher always try to link the policy as high up as possible in the OU tree. If there are cases where you want to apply the policy setting at all levels except for a minority of the lower sub-OU's then simple apply a different policy on the fewer OU's to make the exception.  **Bad Example** | **Good Example**
---|---
[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb86.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image91.png>) | [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb87.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image92.png>)

### Linking GPO's

Essentially there are three ways ways you can link a GPO to an AD structure firstly is to apply it to a OU secondly is to apply it to an AD Site and finally is to link it to a domain.

#### Linking to AD Site

I have to say that you should NEVER consider applying a Group Policy to an AD site EVER!!!. Not only does applying a GPO to an AD site make troubleshooting an absolute pain you frequently finding yourself inadvertently applying a user or workstation GPO to your servers (This can be VERY BAD). AD Sites are based on IP subnets and I agree it can be very handy to apply settings based on the IP address of the computer (see [How to use Group Policy Preferences to dynamically map printers with Roaming Profiles](<https://www.grouppolicy.biz/2010/01/how-to-use-group-policy-preferences-to-dynamically-map-printers-with-roaming-profiles/>) ) and thankfully there is a way to now do this with [Group Policy Preferences](<https://www.grouppolicy.biz/2010/03/what-are-group-policy-preferences/>). Any of the new preference settings can be targeted using [Preference Item-Level Targeting](<http://technet.microsoft.com/en-us/library/cc733022.aspx>) which gives you 27 different ways you can target your setting. The [IP Address Range Targeting](<http://technet.microsoft.com/en-us/library/cc732310.aspx>) and [Site Targeting](<http://technet.microsoft.com/en-us/library/cc732583.aspx>) target options will allow you to achieve the same targeting as applying the GPO to an AD Site however you are far less likely to make a mistake using this method as the GPO should be linked to resource OU that limits the scope of the policy to only a particular type of AD Objects (e.g. just workstations not servers).

#### Linking to OU

Linking a GPO to an OU is by far and away the most popular method of linking a GPO. This method allows for easily change the users configuration my moving them into the appropriate OU structure to have them configured. This method also fits well with the resource OU structure (see [Part 1](<https://www.grouppolicy.biz/2010/07/best-practice-active-directory-structure-guidelines-part-1/>)) so that you can disable parts of the GPO that don't apply to the object that you are apply the policy.

#### Linking to a Domain

Technically you can apply a GPO to the Domain however this is more or less like linking it to the Root Organisational Unit. Linking it here will apply the policy to the entire domain so make sure that you are very careful when link a policy to this location. Policies should only be linked to the domain if you have a setting that you want to be applied to all users and/or computer in your entire domain. (See "Edit Default Domain Policies Sparingly" section above). The other scenario that you might want to link a policy here is if you want to make sure that you have at least your core policy setting applied to your "Users" or "Computers" container. But I would also recommend that you redirect these default locations for new objects so that you don't have to setup GPO's at the domain to cover these objects.

#### References

[TechNet: Linking GPOs](<http://technet.microsoft.com/en-us/library/cc736813\(WS.10\).aspx> "http://technet.microsoft.com/en-us/library/cc736813\(WS.10\).aspx")

> If, however, the settings do not clearly correspond to computers in a single site, it is better to assign the GPO to the domain or OU structure rather than to the site.

[TechNet: Linking GPOs](<http://technet.microsoft.com/en-us/library/cc736813\(WS.10\).aspx> "http://technet.microsoft.com/en-us/library/cc736813\(WS.10\).aspx")

> Most GPOs are normally linked to the OU structure because this provides the most flexibility and manageability

### When to filter

There are two ways you can filter your GPO when you apply then to your AD structure. Predominantly I find that Security Filtered Group Policy Objects is the most common way you can filter. Either way you should be filtering a GPO only when you want to exclude or include exceptions to the scope of the policy.

#### Security Filtered

This method allow you to apply Group Policy Objects to a cross section of users or computers in your organisation. I quite often have a security filtered policy that has my pilot users computers as members so that I can selectively apply settings to their computers first for testing (see "[Create a Test Group Policy Structure](<#TestGPO>)" section above). As computers and users can also be a member of multiple GPO this also allows you to configure a users environment without having to spawn many number of levels of OU's that would other wise be necessary for every combination of GPO assignment (see "80/16/4 Example 3 & 4"). You can in theory apply a single user or computer to a GPO by adding them explicitly to the GPO under Advanced security (see image below). [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb118.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image123.png>) However this is extremely poor practice and I would strongly recommend that you should always create a security group that has the "Apply Group Policy" permission assigned to it so that at a later stage you can assign users or computer to the GPO without modify the permission on the GPO itself (see image below). [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb119.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image124.png>) I know the name "Workstation GPO" might seem to conflicting with the "Don't use the work "POLICY" or "GPO" in the GPO name" rule that however in this case "GPO" is justified as this is the name of a security group and so it is not obvious that a the security group is used as part of a Group Policy Object. **Recommendation:** When removing "Authenticated Users" from the security filtering of a GPO ensure that you only remove the "Apply Group Policy" permission and not the "Read" permission as this will cause "Inaccessible GPO" error when any non domain admin tries to look a the GPO's via GPMC. See my previous post [How to apply a Group Policy Object to individual users or computer](<https://www.grouppolicy.biz/2010/05/how-to-apply-a-group-policy-object-to-individual-users-or-computer/>) for detail instructions on how to do this correctly.

#### Reference

[TechNet: Defining the Scope of Application of Group Policy](<http://technet.microsoft.com/en-us/library/cc787661\(WS.10\).aspx> "http://technet.microsoft.com/en-us/library/cc787661\(WS.10\).aspx")

> If you have Read access to the domain, site, or OU, but not on one of the GPOs linked there, it will appear as **Inaccessible GPO** , and you will not be able to read the name or other information for that GPO

The exception to where you want to do this is if you have many GPO's that are security filtered and you want to ensure as fast a possible security processing then removing the read permission will "slightly" improve performance. So unless GPO processing time is an issues this doing removing the read is still not recommended. [TechNet: Determining the Number of Group Policy Objects](<http://technet.microsoft.com/en-us/library/cc758134\(WS.10\).aspx> "http://technet.microsoft.com/en-us/library/cc758134\(WS.10\).aspx")

> If the Apply Group Policy permission is not set, but the Read permission is, the GPO is still inspected (although not applied) by any user or computer that is in the OU hierarchy where the GPO is linked. This inspection process increases logon time slightly.

**Recommendation:** You should only security filter GPO when the setting in the policy are mutually exclusive with all the other GPO in your organisation. If you have two GPO's that are security filtered that configure the same setting and the user or computer are in both the group for that policy then only one policy will win out and you could end up with some fairly un-predictable results.

#### [WMI Filters](<http://support.microsoft.com/kb/555253>)

WMI Filters have been around since Windows XP/2003 and are a [great way to filter your Group Policy Objects based](<http://blogs.technet.com/b/askds/archive/2008/09/11/fun-with-wmi-filters-in-group-policy.aspx>) on the hardware of the computer that the policy is applied. However performing a WMI queries can take a substantial amount of time and if you have multiple WMI filters applying to your computers you have a significant performance decrease. Once again you can get around having to resort to using WMI Filters as Group Policy [Preference Item-Level Targeting](<http://technet.microsoft.com/en-us/library/cc733022.aspx>) also have a number of options you can target hardware. Unlike WMI the Preference targeting engine has the performance advantage of being written in native code so it is much faster at determining what setting to apply. They hardware targeting options are:

  * [Battery Present Targeting](<http://technet.microsoft.com/en-us/library/cc730947.aspx>)
  * [CPU Speed Targeting](<http://technet.microsoft.com/en-us/library/cc732436.aspx>)
  * [Disk Space Targeting](<http://technet.microsoft.com/en-us/library/cc730743.aspx>)
  * [MAC Address Range Targeting](<http://technet.microsoft.com/en-us/library/cc731568.aspx>)
  * [Operating System Targeting](<http://technet.microsoft.com/en-us/library/cc753566.aspx>)
  * [PCMCIA Present Targeting](<http://technet.microsoft.com/en-us/library/cc754260.aspx>)
  * [Portable Computer Targeting](<http://technet.microsoft.com/en-us/library/cc754547.aspx>)
  * [RAM Targeting](<http://technet.microsoft.com/en-us/library/cc732170.aspx>)
  * As a legacy option you can even do [WMI Query Targeting](<http://technet.microsoft.com/en-us/library/cc771819.aspx>) which allows you to easily port your pre-existing WMI queries into preferences. But be warned the WMI Query Targeting still suffers from the same performance issues.

So as you can see WMI Filters applied to the GPO object itself however just as in the "Where to Link" section above you will see Group Policy Preference will help you avoided having to rely upon WMI to often.

#### Reference

[TechNet: Applying WMI Filters](<http://technet.microsoft.com/en-us/library/cc758471\(WS.10\).aspx> "http://technet.microsoft.com/en-us/library/cc758471\(WS.10\).aspx")

> WMI filters can take significant time to evaluate, so they can slow down logon and startup time.

### Always create a deny "Apply group policy" security group

When creating a GPO always consider creating a security group and assigning it the Deny "Apply group policy" permissions (see image below) so that you have a simply way to exclude a particular user or computer from the policy in the future. Having this deny group applied to the GPO in advanced can save you a lot of time as it is often much easier and quicker to added a users to a security group than it is to modify the security on a GPO. [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb120.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image125.png>) (Same as above) I know the name "Workstation GPO Deny" might seem to conflicting with the "Don't use the work "POLICY" or "GPO" in the GPO name" rule that however in this case "GPO" is justified as this is the name of a security group and so it is not obvious that a the security group is used as part of a Group Policy Object.

### Apply GPO to New Users and Computers OU

In [part 1](<https://www.grouppolicy.biz/2010/07/best-practice-active-directory-structure-guidelines-part-1/>) I recommended about setting up a new OU structure for any new user and computer that is created in your AD under the "Redirect New User and Computer Accounts" section. The reason why this was recommended was to enable you to easily apply a GPO to the default locations for these objects without having to resort to modifying the Default Domain Policy or by linking a new GPO to the entire domain. It the example below I have created a simple GPO for each Users and Computers OU. Using this method your default user and computers will still receive the "Default Domain Policy" GPO and any additions settings in the two "New" GPO's. [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/08/image_thumb5.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/08/image5.png>) I don't recommending linking the "People" or "Workstations" GPO's (See "Example Group Policy Designs" section below) as the New\Users and New\Computers OU as they could contain objects other than People and Workstations (e.g. Service Accounts or Servers). Instead I recommend that you only configured some basic security setting for the "New Computers" such as a default WSUS and patch install schedule so that any computers that are left in these OU's are at least kept up to date with security patches. Then for the "New Users" GPO you may want to configure a delayed logon script (see [How to schedule a delayed start logon script with Group Policy](<https://www.grouppolicy.biz/2010/01/how-to-schedule-a-delayed-start-logon-script-with-group-policy/>)) that notifies the users that they are not properly configured and they need to contact the help desk. In any case even though you have configured these locations it is still very important that you establish some sort of regular process by which someone reviews the objects in these OU's and ensures they are moved into the appropriate locations so the proper policies are applied.

#### References

[Designing an OU Structure that Supports Group Policy](<http://technet.microsoft.com/en-us/library/cc783140\(WS.10\).aspx> "http://technet.microsoft.com/en-us/library/cc783140\(WS.10\).aspx")

> "...change the default location where new user and computer accounts are created so you can more easily scope GPOs directly to newly created user and computer objects

### Use the 80/20 rule

Ok"... this is the a [rule in name only](<http://en.wikipedia.org/wiki/Pareto_principle>) as it should also be considered as a guideline. Essentially you should try to put the vast majority of setting in a policy that applied to all your computer or users. Then you should apply the exception to the default policy to the subset only to the computers you want to apply these settings (see 80/20 Conceptual Design). If two scopes/levels of applying policies is not flexible for your organisation then you can even consider the 80/16/4 to give you more flexibility (4% equals 20% of 20%). Also note the smaller 4% scope does not necessarily need to be a complete subset of the 16% as it is possible that you want to apply location specific settings that have nothing to do with the organisational structure (see 80/16/4 Conceptual Design below). When deciding what policy settings to put in the 80% of 20% GPO's make sure that you take another look at the "Monolithic vs. Functional GPOs" section above that talks about the different approaches you can take when configuration settings. As I said before the 80% policies are going lend them self to have more setting in them but they will probably be relatively static (i.e. Monolithic) where the 20% policies will have fewer settings but probably need to be updated more frequently (i.e. Functional).  **80/20 Conceptual Design** | **80/16/4 Conceptual Design**
---|---
[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image13_thumb1.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image132.png>) | [![image\[39\]](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image39_thumb1.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image392.png>)
The conceptual designs above shows that there is only one level 2 and level 3 scopes to apply GPO but in reality there could be many different lower level policies that can be applied to your environment as seen in "80/16/4 Example 4".

### Example Group Policy Designs

The organisation below that I use in the examples conveniently has 100 setting that they need to apply. Therefore they number of setting equals the percentage break down of the number of settings that are applied. In real world the number of setting are obviously going to vary greatly from single digits perhaps many thousands of settings. "80/20 Example" is a simple representation of how you would actually apply this in the real world. As you can see 80 setting are applied at the top level to all "People" OU and there then there are 20 settings site specific user settings. These location setting are typically drive and printer mapping setting that are specific to the site. While the "People" Group Policy Object will have setting that need to be applied to all users universally (e.g. screensaver time out value.)  **80/20 Example 1**
---
[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb100.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image105.png>)
"80/20 Example 2" is the same as Example 1 except in this scenario the business has decided to have a top level organisational OU structure so that it will be easy in the future to separate parts of the organisation from the AD in the future. This illustrates that you do not need to have the same number of levels of OU's in your AD as the number of level of scope that you apply GPO's.  **80/20 Example 2**
---
[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb110.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image115.png>)
"80/16/4 Example 1" shows you how you would apply this to a "Three Tier OU Structure" (see [part 1](<https://www.grouppolicy.biz/2010/07/best-practice-active-directory-structure-guidelines-part-1/>)). The advantage of this model is that all setting are applied base on the OU structure and which means all policies are applied simple based on the location of the AD object in the OU structure. This is useful as you don't that you don't need to add and users (or computers) to security group.  **80/16/4 Example 1 **
---
[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb111.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image116.png>)
"80/16/4 Example 2" shows you what you can do when you only want to apply the same "Manufacturing" setting to all the users across all the sites. This takes into consideration the "Reuse GPO's where possible" rule (see above) and link a single manufacturing GPO  **80/16/4 Example 2**
---
[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb112.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image117.png>)
"80/16/4 Example 3" shows you how you could apply the policy differently using a single security group filtered policy at the top level but still have the same affect as the "80/16/4 Example 1". This is an example of applying a 3 level GPO structure to a 2 level OU structure as the "Manufacturing" simple by applying it at the top level but then applying a security group filter. The advantage of doing it this way is that you don't need to have as many OU deep (see "Go Wide not Deep" in [part 1](<https://www.grouppolicy.biz/2010/07/best-practice-active-directory-structure-guidelines-part-1/>)) and it avoids having to create a new Group Policy for the manufacturing users at each site (especially when they might be the same settings).  **80/16/4 Example 3**
---
[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb113.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image118.png>)
"80/16/4 Example 4" shows a combination of "80/16/4 Example 1" and "80/16/4 Example 2" where the organisation has generally the same requirements of "Example 1" however they need to apply 1 high security setting (e.g. shorter screensaver timeout) that need to be applied to the managers computer because they normally deal with sensitive corporate information. This also illustrates that you can have multiple level 2 and level 3 GPO in the same environment and that level 3 GPO policies do not necessarily need to be a subset of level 2 policies (see conceptual circles above).  **80/16/4 Example 4**
---
[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb114.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image119.png>)

### Apply default settings on your 80% level one policy just in case

I know I have just gone though above that you should apply 80% of your settings in the highest policy however there is one problem with this. If for some reason a computer or users is placed in a top level OU or a second level OU is created without a policy applied to it or a user or computer has not been added to the correct security group this could leave gaps with the coverage of settings. So to get around this issue be sure that your level one 80% policies are configured with a default setting to cover your more essential configurations such as Screensaver timeout or WSUS servers. In the example below we have 95 settings (or 95%) of the setting being applied to the users with the 20% being applied at the second level policy. Effectively only 80 settings (or 80%) will be actually be applied to the users from the top level policy as there is a 15% overlap of settings the settings. However a user in the "People" or the miss configured "Brisbane" OU will at least get 95 setting (or 95%) of the settings applied. This might not be a perfect configuration for them however it will at least mean they are compliant to the mandatory corporate configuration settings (e.g. Screensaver on and WSUS server configured). [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb121.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image126.png>) In closing I hope this documents has helped you design your Group Policy infrastructure in your environment. If you have any other questions you want covered or you simply have a question about what I talked about above please feel free to post a comment"...

### Other References

Here is a list of link to other web sites that I have found useful in guiding my design decisions with group policy.

  * [Appendix A: GPO Scenario Policy Settings](<http://technet.microsoft.com/en-us/library/cc738195%28WS.10%29.aspx> "http://technet.microsoft.com/en-us/library/cc738195%28WS.10%29.aspx")
  * [TechNet: Designing a Group Policy Infrastructure](<http://technet.microsoft.com/en-us/library/cc786524\(WS.10\).aspx> "http://technet.microsoft.com/en-us/library/cc786524\(WS.10\).aspx")


### Change Log

I plan for this to be a dynamic article that I will change over time and I am sure there will be a few errors along the way that will need correcting so below are the list of changes that I made to this article since it was originally published: 28/07/2010 "“ Add section for "Monolithic vs. Functional GPOs" from <http://technet.microsoft.com/en-us/magazine/2008.01.gpperf.aspx> by Darren Mar-Elia via [Mike Kline](<http://adisfun.blogspot.com/>) 28/07/2010 "“ Corrected error in the WMI Filter sections that said they had been around since Windows 2000 (Should have said XP/2003). Thanks to [Aaron Parker](<http://blog.stealthpuppy.com>) 2/08/2010 "“ Added mention to "How to Link" that you can link to the domain. Added more references to Microsoft TechNet articles. Added "Create a Test OU Structure" 3/08/2010 "“ Added "Apply GPO to New Users and Computers OU" section. 24/10/2011 - Added refrencec to Best Practices for Defautl Domain policies...