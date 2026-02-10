---
title: "What you need to know about KB3148812"
date: 2016-04-22 03:41:13
author: admin
categories: ["News"]
tags: ["Feedly", "Group Policy", "IFTTT", "Recently Read"]
---

This update introduces two changes that require additional manual steps in order to complete the installation: those who installed it right away had a bit of a panic because the guidance was not yet published. We try not to require post-update manual effort whenever possible, and unfortunately in this case it was unavoidable. This post describes the symptoms you’ll see, details how to resolve them, and then provides some background on this change.

## Issue #1: Loss of WSUS admin console

After installing KB3148812 and rebooting your WSUS server, you will notice that your console is no longer available, and that resetting the server node does not fix the issue.

The errors in the log will read something like this:

“The WSUS administration console was unable to connect to the WSUS Server via the remote API… The handshake failed due to an unexpected packet format.SourceSystemStack Trace:

at System.Net.Security.SslState.StartReadFrame(Byte[] buffer, Int32 readBytes, AsyncProtocolRequest asyncRequest)”

To recover your console, run the following in an elevated command prompt (assuming Windows is installed on drive C):

cd C:\Program Files\Update Services\Tools

Wsusutil.exe postinstall /servicing

Then reset the server node or reboot WSUS, and you’re back in business.

## Issue #2: Clients cannot scan WSUS

After installing KB3148812 and rebooting, you may find that client scans against WSUS no longer succeed.

To restore client-server communication, enable HTTP Activation on your WSUS server via the Add Features and Roles Wizard in your Server Manager:

[![](http://ift.tt/1VJZjZY)](<http://ift.tt/1YJJwZs>)

Give it a minute, and then try your scans against WSUS again. After installing this feature, they should succeed.

Why you need KB3148812

Windows 10 builds are staged in encrypted packages to Windows Update several days prior to the actual go-live date. This is to ensure that we can release to all regions simultaneously when the time comes. The Windows 10 client has been able to decrypt these packages since RTM; however, WSUS was not able to do this. Until now, we have been manually decrypting these packages prior to releasing to the WSUS channel, the process of which is both time consuming and prone to errors. KB3148812 introduces this functionality to WSUS for Windows Server 2012/R2, such that it can now natively decrypt this content. Skipping this KB means not being able to distribute the Windows 10 Anniversary Update, or any subsequent feature update, via these platforms. Note that Windows Server 2016 will have this functionality at RTM.

Why WCF with HTTP activation

ASMX was introduced in .NET 2.0, and is an aging technology at this point. WCF is generally more [capable and flexible](<http://ift.tt/1YJJxfG>) than ASMX, and other Microsoft services already use WCF, so it made sense to migrate Microsoft Update (and thus WSUS) to the same.

In closing

This post details the steps required to complete the installation of KB3148812, and covers all known issues that might arise. Should you hit an issue not listed here after performing the steps above, please reach out to us via Email Blog Author so that we can investigate.

![](http://ift.tt/1VJZiFs)

from WSUS Product Team Blog http://ift.tt/1YJJyjX
via [IFTTT](<http://ift.tt/1c4nCfM>)