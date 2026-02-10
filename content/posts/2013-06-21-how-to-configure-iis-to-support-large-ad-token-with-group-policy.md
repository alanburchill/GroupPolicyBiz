---
title: "How to configure IIS to support large AD Token with Group Policy"
date: 2013-06-21 09:17:00
author: admin
categories: ["Tutorials"]
tags: ["AD Token", "Bloat", "IIS", "MaxFieldLength", "MaxRequestBytes", "MaxTokenSize", "WMI filtering"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2013/06/image_thumb6.png"
---

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/06/image_thumb6.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/06/image6.png>)Active Directory Token Bloat is an issue in AD where user are is a member of too many security groups. As such their account exceed the default 12k token size limit in Windows that is set on their internal AD Security Token. This is a common problem for many large organisation that have many security groups and in most situation this problem is fixed by configuring a larger "MaxTokenSize" registry key on all the computers. The side affect of making this change is that some other systems that use AD authentication may have issues with user with a token size larger that 12k. Specifically IIS has a http header default buffer size that is only large enough to allow users with the authenticate with a default AD token size. If a users has a large token than the default, then they will receive an "HTTP Error 400. The size of the request headers is too long." error message.

As you can see below you can confirm if this is the case by installing the [Fiddler](<http://fiddler2.com/>) tool to capture the raw data being passed back from IIS.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/06/image_thumb7.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/06/image7.png>)

The reasoning behind this restricted buffer size in IIS is to help mitigate the extra resource it would take to handle a large buffer thus making it easier for the bad guys to launch a denial of service attack. But if you IIS servers are only used on the Intranet then configuring a larger buffer to allow larger AD token sizes is something that you might want to consider"....

So below I will explain how you can target the necessary registry key settings to just you IIS servers in your organisation that could potentially be affected by the issue.

To increase the header size you need to configure the following registry keys in a Group Policy Object that is applied to all your servers.

**HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\HTTP\Parameters**

**MaxFieldLength
** Default Value: 16384
Min "“ Max Value to set: 64 - 65534 (64kb) bytes
Sets an upper limit for each header. See MaxRequestBytes. This limit translates to approximately 32k characters for a URL.

**HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\HTTP\Parameters**

****

**MaxRequestBytes**
Default value: 16384
Min-Max value to set: 256 - 16777216 (16MB) bytes
Determines the upper limit for the total size of the Request line and the headers.
Its default setting is 16KB.

If this value is lower than MaxFieldLength, the MaxFieldLength value is adjusted.

Also note that these registry keys do not current exist by default so they will always assume the default value if key do not exist (see below)

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/06/image_thumb8.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/06/image8.png>)

So we need to apply these registry key setting to your servers, but rather than just applying this key to all your servers globally we will use a WMI filter to avoid unnecessary settings.

In the Group Policy Management Console create a new WMI filter under the "WMI Filters" section:

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/06/image_thumb9.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/06/image9.png>)

In the example below we do a test to see if the Windows Feature called "Windows Authentication" is installed.

> select * from Win32_ServerFeature where name = "Windows Authentication"

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/06/image_thumb10.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/06/image10.png>)

This feature is a sub role of IIS and is required to perform Kerberos authentication in IIS. Therefore if this component is not installed then the users will not be able to use Windows integrated authentication thus they will not be able to authenticate let along have this "header too long" error. (See below)

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/06/image_thumb11.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/06/image11.png>)

Configure the registry key change as listed above as Group Policy Preferences. As you can see I have selected the "Create" action as these values are not created by default (as mentioned before) but this also ensure that if anyone else has configured another value this will not overwrite this value as the "Create" action will only work if there is no other value.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/10/image_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/10/image.png>) [![image](https://www.grouppolicy.biz/wp-content/uploads/2013/10/image_thumb1.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/10/image1.png>)

On top of this you should also enable the "Apply once and do not reapply" option so that you if for some reason you want to return the compute to the default value all you have to do is delete the registry key and it will not be applied again.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/06/image_thumb15.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/06/image15.png>)

So now you should have a group policy that looks something like the one below that is linked to your Servers Organisational Unit.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/06/image_thumb16.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/06/image16.png>)

Below is a GP report of a computer that does _not_ have "Windows Authentication" as you can see the WMI filter will evaluate as False and the registry key will not apply.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/06/image_thumb17.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/06/image17.png>)

Then as soon as the "Windows Authentication" option is install the WMI filter will evaluate as true and the two registry key changes will apply to the server.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/06/image_thumb18.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/06/image18.png>)

As you can see the end result is that the MaxFieldLength and MaxRequestBytes registry keys are applied to the server.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2013/10/image_thumb2.png)](<https://www.grouppolicy.biz/wp-content/uploads/2013/10/image2.png>)

**Note:** Once this setting has applied you will need to schedule a reboot of the server for the setting to take affect.

#### Additional Information References

<http://support.microsoft.com/default.aspx?scid=kb;EN-US;2020943>

<http://blogs.technet.com/b/surama/archive/2009/04/06/kerberos-authentication-problem-with-active-directory.aspx>