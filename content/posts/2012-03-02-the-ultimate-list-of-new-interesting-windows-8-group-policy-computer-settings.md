---
title: "The ultimate list of new Interesting Windows 8 Group Policy Computer Settings"
date: 2012-03-02 05:05:34
author: admin
categories: ["Tip"]
tags: ["settings", "Windows 8"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2012/03/win8_logo_0_thumb.jpg"
---

[![win8_logo_0](https://www.grouppolicy.biz/wp-content/uploads/2012/03/win8_logo_0_thumb.jpg)](<https://www.grouppolicy.biz/wp-content/uploads/2012/03/win8_logo_0.jpg>)As you know along with Windows 8 Consumer Preview and Windows Server 8 Beta has been released and of course I have taken a look at the list of new Group Policy setting that apply to Windows 8. From the list of new Windows 8 Consumer Previews settings I have selected some policy setting that talk about features that look really interesting.

The list of new Windows 8 Consumer Preview settings is very long so below is a list of just computer based setting, I will make another blog post soon about the user specific settings.

Note: I have not had a chance to implement any of these setting yet so I am using a bit of interpretation of the help details about these setting.

The next two settings are obviously really important if you want to implement a standard Corporate UI look and feel.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/03/image_thumb36.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/03/image36.png>)

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/03/image_thumb2.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/03/image2.png>)

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/03/image_thumb3.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/03/image3.png>)

Effect of enabling the above options"...

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/03/image_thumb37.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/03/image37.png>)

The next two policy setting looks like you can specify a Internet and Intranet proxy server for Metro Style apps.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/03/image_thumb4.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/03/image4.png>)

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/03/image_thumb5.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/03/image5.png>)

Windows 8 introduces the idea of costed networks (3G/4G) and allow IT admins to chose to uses these networks for background file synchronisation.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/03/image_thumb6.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/03/image6.png>)

AFAIK the "Work offline" options was something that was removed from Vista/7, well it looks like the option is now back.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/03/image_thumb7.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/03/image7.png>)

The next few settings are REALLY interesting"... These appear to allow IT admins to restrict second connections to the internet if it is already connected to the domain. I have seen this feature requested many times on the forum and allows IT admins to disable a second network connection if the computer is already connected to the domain. What this means is that if someone in a corporate environment has a BYO wireless 3G device they cannot use it to surf the internet and bypass the corporate firewall. Previously you had to have third party software and/or enable this in the BIOS to do the same things.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/03/image_thumb8.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/03/image8.png>)

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/03/image_thumb9.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/03/image9.png>)

This option allows IT admins to prevent access to any sort of mobile broadband connection. However it probably wont work if the computer is connected to such device wirelessly.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/03/image_thumb10.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/03/image10.png>)

More mobile broadband options, this time is allows you to configure the cost mode on a WLAN connection.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/03/image_thumb11.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/03/image11.png>)

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/03/image_thumb12.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/03/image12.png>)

Interesting to see that there is a differentiation between 3G and 4G (not that there is any network in the world outside of Japan that has TRUE 4G networks).

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/03/image_thumb13.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/03/image13.png>)

This policy relates to the security boot features of Windows 8 and allows you to set the boot level security to something lower"... Why on earth you would allow the "Bad" options however is beyond me.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/03/image_thumb14.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/03/image14.png>)

Looks like there is an option now to only have redirected folder enabled on primary computers, meaning that users can quickly logon to kiosk or remote computers without them having to have sync their redirected on a computer they only use once"... Very Nice

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/03/image_thumb15.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/03/image15.png>)[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/03/image_thumb16.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/03/image16.png>)

More on this soon"... but this policy prevents Windows 8 from stopping the Group Policy Service from stopping when it is idle.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/03/image_thumb17.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/03/image17.png>)

One that many corporations will probably want to implement to prevent their users from downloading any metro apps from the Store.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/03/image_thumb18.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/03/image18.png>)

I THINK"... this policy options stops you from automatically selecting the local administrator account if you try logon on using the administration account on a domain. Handy for when you have local users accounts with the same name as a domain account.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/03/image_thumb19.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/03/image19.png>)

Hybrid boot"... that think that allows you to start REALLY fast"... why would you want to disable this option. Still nice to have the option"...

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/03/image_thumb20.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/03/image20.png>)

Windows 8 devices are going to come with RFID tag's and thus this policy allows you to disable them.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/03/image_thumb21.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/03/image21.png>)

New feature in BitLocker allows the computer to start without a PIN if they are connected to the corporate network.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/03/image_thumb22.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/03/image22.png>)

That little dot with a line around it reveals the password in password fields"... You might not want to have this option on corporate PC's.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/03/image_thumb23.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/03/image23.png>)

If you want a really boring background image then enable this option"...

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/03/image_thumb25.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/03/image25.png>)


Disable the new file history option for files on the local HDD.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/03/image_thumb26.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/03/image26.png>)

Helps prevent user from booting their own Windows To Go USB OS image on a corporate PC.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/03/image_thumb27.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/03/image27.png>)

Number of options here to prevent the synchronisation of these setting with other computers.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/03/image_thumb29.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/03/image29.png>)

Show to hide the new Ribbon in Windows Explorer"...

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/03/image_thumb30.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/03/image30.png>)

Finally a group policy that allows you to configure Libraries"...

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/03/image_thumb34.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/03/image34.png>)

This one seems to be names wrong"... it says "Let the service shut down" where it should really say "Let the Windows Update Services shut down". But this is to control if the Windows Update service shutdown when not needed"....

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/03/image_thumb35.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/03/image35.png>)

I am going to be exploring some of these settings in some more detail soon so stay tune for more posts"...