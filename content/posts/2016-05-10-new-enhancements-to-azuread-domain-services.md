---
title: "New enhancements to #AzureAD Domain Services"
date: 2016-05-10 00:28:22
author: admin
categories: ["News"]
tags: ["Feedly", "Group Policy", "IFTTT"]
---

Howdy folks,

Today we're announcing a cool set of enhancements to Azure AD Domain Services (AAD DS). With > 3500 customers already actively using this new service (while it's still in preview!), AAD DS has been a unexpected hit. Those customers have given us a lot of helpful feedback and today we're announcing some new features based on their requests:

  * Secure LDAP access
  * Custom OU support
  * Administer DNS for your managed domain
  * Domain join for Linux VM's (no, that is not a typo!)


And in case you didn't see the news when we originally announced it AAD DS is now available in Australia!

Mahesh Unnikrishnan, the Program Manager who leads our AAD DS efforts, has written up some details on these enhancements which you'll find below.

I hope you'll find these new capabilities useful. As always, we'd love to receive any feedback or suggestions you have.

Best regards,

Alex Simons (Twitter: [Alex_A_Simons](<https://twitter.com/Alex_A_Simons>))

Director of Program Management

Microsoft Identity Division

"”"”"”"”"”"”"“

Hi there!

I'm Mahesh Unnikrishnan, a Program Manager in the Identity division at Microsoft. Late last year, we [announced the public preview](<http://ift.tt/1ObPFNA>) of an exciting new service called Azure AD Domain Services. We've seen incredible customer demand for this service. The past few months have been a great learning experience for us and we've gotten a ton of valuable feedback from our preview customers. We continue to evolve the service and refine it based on this feedback.

Today, I'm thrilled to announce updates to our public preview. We have quite a few new features for you to try out.

**Secure LDAP access to your managed domain
**

Many directory-connected applications use LDAP (Lightweight Directory Access Protocol) to connect to Active Directory, in order to authenticate users or to lookup additional information about the user. Secure LDAP, also known as 'LDAP over Secure Sockets Layer (SSL)/Transport Layer Security (TLS)', provides a secure way to do this. Secure LDAP ensures that sensitive LDAP traffic in your domain is not visible to anyone with a network packet analyzer. This level of security is indispensable, if you want to connect to your directory from an external network or over the internet.

We're excited to deliver support for Secure LDAP in Azure AD Domain Services. You can now connect over secure LDAP from any virtual machine within the virtual network in which you've enabled Azure AD Domain Services. You can also configure your managed domain to allow Secure LDAP connections over the internet. This is useful if you need to connect to your directory from another network or from a different location. This cool new functionality enables you to lift-and-shift applications that rely on Secure LDAP from your on-premises infrastructure and deploy them confidently in Azure.

Get started "“ [Configure secure LDAP (LDAPS) for your managed domain](<http://ift.tt/1ZxApLI>)

**Create and administer custom organizational units (OUs)
**

Some customers told us they would like to lift-and-shift legacy on-premises line of business applications, which rely on service accounts to authenticate with the directory, to Azure. Some of these service accounts are configured with password policies that differ from those for end-user accounts. An example of this is configuring service account passwords to never expire. Other customers have told us how they would prefer to put sets of their domain-joined computers into different organizational units (eg. all web-servers in a single OU, database servers in a different OU etc.) for ease of administration.

With this nifty new feature, members of the 'AAD DC Administrators' group can now create a custom Organizational Unit (OU) on your managed domain. Further, they get full administrative privileges for the custom OU they've created and can perform tasks such as creating service accounts within the OU.

Get started "“ [Create an organizational unit on your managed domain](<http://ift.tt/1ObPIsO>)

**Administer DNS for your managed domain
**

Many of our Azure Infrastructure Services customers deploy workloads that require them to configure and deploy load-balancers or other non-domain joined virtual machines. They need to configure DNS in order to ensure these machines are reachable from other machines.

Azure Active Directory Domain Services provide DNS resolution for your managed domain within the virtual network in which you've enabled the service. Occasionally, it may be necessary to configure DNS on the managed domain in order to create records for machines that are not joined to the domain, create virtual IP addresses for load-balancers or configure external DNS forwarders. Members of the 'AAD DC Administrators' group can now administer DNS on the managed domain using DNS administration tools.

Get started "“ [Administer DNS on your managed domain](<http://ift.tt/1ZxAsav>)

**Domain join Linux virtual machines
**

We've engineered Azure AD Domain Services to make it easy for you to join your Azure Infrastructure Services virtual machines to the managed domain. You can then manage these virtual machines using Group Policy and users can sign-in to the virtual machines using their corporate credentials.

We've published a [step-by-step guide for joining a Windows virtual machine to your managed domain](<http://ift.tt/1ObPFNE>).

We've also collaborated with our friends at Red Hat to show you how to [join a Red Hat Enterprise Linux (RHEL 7) virtual machine to your managed domain](<http://ift.tt/1ZxAsqN>).

**We're now in Australia!
**

After launching the public preview, we've seen a lot of customer requests to add support for the Australia regions of Azure. We're excited to announce that Azure AD Domain Services is now available in Azure's Australia East and Australia Southeast regions.

We're thrilled about the opportunity to evolve Azure AD Domain Services based on your feedback. We'd love for you to try out the service, especially these new features and [share your feedback with us](<http://ift.tt/1ObPFNL>).

Thanks,

Mahesh Unnikrishnan

Principal Program Manager

Microsoft Identity Division

from Active Directory Team Blog http://ift.tt/1ZxAsqP
via [IFTTT](<http://ift.tt/1c4nCfM>)