---
title: "How to fix AD PowerShell error &ldquo;Unable to find a default server with Active Directory Web Services running.&rdquo;"
date: 2011-12-13 00:07:28
author: admin
categories: ["Tip"]
tags: ["ADAC", "ADWS", "Powershell", "Windows 7"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2011/12/image_thumb3.png"
---

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/12/image_thumb3.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/12/image3.png>)Today I experienced [Serendipity](<http://en.wikipedia.org/wiki/Serendipity> "http://en.wikipedia.org/wiki/Serendipity") with the error "Unable to find a default server with Active Directory Web Services running." in PowerShell with Windows 7. This message was occurring when trying to create some new OU's using the New-ADOrganizationalUnit command. Initially I thought it was due to not having the required Active Directory Powershell commands installed but then I realised that the "Import-Module ActiveDirectory" command was loading find so that couldn't be the problem.

About this time I then noticed a new blog post <http://jorgequestforknowledge.wordpress.com/2011/12/12/the-active-directory-web-service-adws/> about the new Active Directory Web Services (ADWS) feature with 2008 R2 which explained why I was getting this message. The environment I was dealing with was a Windows 2008 only domain environment meaning that there was no ADWS for PowerShell in Windows 7 to utilise. This article explained that both PowerShell and the the Active Directory Administrative Center (ADAC) in Windows 7/2008 R2 used the WS-* protocols and therefore needed a ADWS server somewhere in the domain to work. Not having an ADWS DC in the environment meant that these tools would not work"...

So to get around this issues you will need to ~~either need to spin up a Windows Server 2008 computer to run the commands or~~ apply the necessary KB's to some of the domain controllers your environment to enable ADWS.

**Update:** I just learnt that the AD PowerShell commands are only supported on Windows 7/2008 R2.

The moral of this story is that its always good practice to make sure that your server and client infrastructure are upgraded together due to the advantages of the tight integration the two product have with one another.

Related KB's:

[Windows 7 clients cannot locate the Active Directory Management Gateway service that is installed on Windows Server 2003-based domain controllers](<http://support.microsoft.com/kb/969429>)

[Windows 7 clients cannot locate the Active Directory Management Gateway service that is installed on Windows Server 2008-based domain controllers](<http://support.microsoft.com/kb/967574>)

**Note:** ADWS was included with Windows Server 2008 Service Pack 2.