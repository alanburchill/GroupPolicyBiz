---
title: "Group Policy FAQ #1: What are the Group Policy Preferences Prerequisites?"
date: 2010-12-21 13:00:00
author: admin
categories: ["FAQ"]
tags: ["Basic", "GPMC", "Group Policy Preferences", "RSAT"]
---

Even though Group Policy Preference have been out for a number of years (since Windows Server 2008) it is still a relatively unknown feature of group policy. Therefore this is the first of a few articles I am going to be writing about some of the basic features of Group Policy Preferences. So to start off with I am going to cover a few FAQ on what you need to do start using all the Group Policy Preference goodness.

#### Do I need to extend the schema to use Group Policy Preferences?

NO. There are no schema extensions required to support Group Policy Preferences as they work by only creating a folder called "Preference" under the User and/or Computer folder in the SYSVOL.

#### What are the minimum version of domain mode or domain controllers I need to support Group Policy Preferences?

Unofficially Windows 2000 Domain Mode with Windows 2000 DC's will work fine. However officially it is what ever the minimum support OS and domain mode of Active Directory is at the time.

#### What software do I need to install to use Group Policy Preference?

To make it easy the table below outlines what software you need to install to enabled group policy preference on the client and to make changes to the

**Operating System** | **Client Side Extensions Required** | **Group Policy Management Console**
---|---|---
Windows XP | Yes (SP2 also requires XmlLite) | Not Supported
Windows Server 2003 | Yes (SP2 also required XmLite) | Not Supported
Windows Vista | Yes | Yes (via Remote Server Admin Tools)
Windows Server 2008 | Included | Yes
Windows 7 | Included | Yes (via Remote Server Admins Tools)
Windows Server 2008 R2 | Included | Yes

#### How do I get the client side extensions?

Below is a list of links to the download page for the client side extensions for the versions of Windows that do not have it install out of the box.

  * Windows XP [http://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=e60b5c8f-d7dc-4b27-a261-247ce3f6c4f8](<http://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=e60b5c8f-d7dc-4b27-a261-247ce3f6c4f8>)
  * Windows XP x64 [http://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=249c1aed-c1f1-4a0b-872e-ef0a32170625](<http://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=249c1aed-c1f1-4a0b-872e-ef0a32170625>)
  * Windows Server 2003 [http://www.microsoft.com/downloads/details.aspx?familyid=BFE775F9-5C34-44D0-8A94-44E47DB35ADD&displaylang=en](<http://www.microsoft.com/downloads/details.aspx?familyid=BFE775F9-5C34-44D0-8A94-44E47DB35ADD&displaylang=en>)
  * Windows Server 2003 x64 [http://www.microsoft.com/downloads/details.aspx?familyid=29E83503-7686-49F3-B42D-8E5ED23D5D79&displaylang=en](<http://www.microsoft.com/downloads/details.aspx?familyid=29E83503-7686-49F3-B42D-8E5ED23D5D79&displaylang=en>)
  * Windows Vista [http://www.microsoft.com/downloads/details.aspx?familyid=AB60DC87-884C-46D5-82CD-F3C299DAC7CC&displaylang=en](<http://www.microsoft.com/downloads/details.aspx?familyid=AB60DC87-884C-46D5-82CD-F3C299DAC7CC&displaylang=en>)
  * Windows Vista x64 [http://www.microsoft.com/downloads/details.aspx?familyid=B10A7AF4-8BEE-4ADC-8BBE-9949DF77A3CF&displaylang=en](<http://www.microsoft.com/downloads/details.aspx?familyid=B10A7AF4-8BEE-4ADC-8BBE-9949DF77A3CF&displaylang=en>)


If you are still running Windows XP or Windows Server 2003 Service Pack 2 (OMG THAT IS SO BAD) then you will also need to install the XmlLite to make preference work.

  * Windows XP <http://www.microsoft.com/downloads/details.aspx?FamilyId=D7B5DC81-AD14-4DE2-8AD5-8C4A9AAB5992>
  * Windows XP x64 <http://www.microsoft.com/downloads/details.aspx?FamilyId=C7CB26E9-68F1-4F80-B231-79D044431E8E>
  * Windows Server 2003 <http://www.microsoft.com/downloads/details.aspx?FamilyId=611D1FDE-C8D0-4D80-96DA-B5B20F7BA159>
  * Windows Server 2003 x64 <http://www.microsoft.com/downloads/details.aspx?FamilyId=406777E6-79DA-4414-A329-22A435A95D9D>


#### How do I install the client side extensions?

You can install the client side extensions a number of ways in your environment:

  * Logon Scripts "“ See [GPAnswers - Scripting GPPE Installations](<http://gpanswers.com/tiparchive/130-miscellaneous/549-scripting-gppe-installations.html> "http://gpanswers.com/tiparchive/130-miscellaneous/549-scripting-gppe-installations.html")
  * via WSUS
  * via SCCM
  * Slip Stream into image


**Tip:** If you want to do limited testing of Group Policy Preference in your environment and you are still running Windows XP or Vista then you can selectively just rollout the extensions to the computer you want to do testing. This is because there will be no affect in applying a preferences setting to a computer that does not have the client side extensions installed.

#### Do I need to install the client side extensions for Windows Server 2008, Windows 7 or Windows Server 2008 R2?

No. It is part of the operating system.

#### Why cant I edit Group Policy Preference from Windows XP or Windows Server 2003?

While the client side extensions for Group Policy Preferences are supported on Windows XP and Windows Server 2003 the version of Group Policy Management Console (GPMC) for XP/2003 has not been updated and therefore does not allow the editing of GPP's in any way shape or form. This therefore means you need at minimum at least 1 Windows Vista (yuck) or Windows Server 2008 server with Group Policy Management Console installed to edit Group Policy Preferences in your environment even if every other server and workstation is running 2003 and XP.

#### How do I install the Group Policy Management Console?

GPMC is a component of the Remote Server Admin Tools for Windows 7 / Vista and is an optional feature that needs to be installed with Windows Server 2008 & R2. See my instructions for installing GPMC on Windows 7 and 2008 R2 at [How to download and install the Group Policy Management Console (GPMC)](<https://www.grouppolicy.biz/2010/03/how-to-download-and-install-the-group-policy-management-console-gpmc/>)

#### Summary

So if you are thinking about using Group Policy Preference in your environment don't stress"... Its a really simple process and as soon as you have GPMC on one or two computers and the client side extensions install on all the computers you want to apply preference to then you ready to go"...