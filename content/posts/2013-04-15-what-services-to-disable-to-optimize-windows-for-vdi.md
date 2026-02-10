---
title: "What services to disable to optimize Windows for VDI"
date: 2013-04-15 10:27:00
author: admin
categories: ["Tip"]
tags: ["Services", "VDI"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2011/11/image_thumb.png"
---

![](https://www.grouppolicy.biz/wp-content/uploads/2011/11/image_thumb.png)In my [previous VDI blog post](<https://www.grouppolicy.biz/2011/11/best-practice-group-policy-for-virtual-desktops-vdi/>) about configuring Windows to work best in a VDI environment I mentioned a few service that should be disabled to improve performance. However a a recent session at [Microsoft Management Summit 2013](<http://channel9.msdn.com/Events/MMS/2013>) called [Optimizing Windows 8 for Virtual Desktop Infrastructure](<http://channel9.msdn.com/Events/MMS/2013/DV-B308> "http://channel9.msdn.com/Events/MMS/2013/DV-B308") has provided a substantially longer list of recommend services configuration for VDI.

Below is a list of services as outlined from the session with their recommended configuration. While you don't "have" to configure all these services doing so will mean that you VDI guests will be running as "lite" as possible meaning you will get higher virtual machine density.

Service Name | Default | Recommended | Details
---|---|---|---
Application Layer Gateway Service | Manual | Disabled | This service manages mobile broadband (GSM & CDMA) data card/embedded module adapters and connections by auto-configuring the networks. It is strongly recommended that this service be kept running for best user experience of mobile broadband devices.
Background Intelligent Transfer Service | Manual | Disabled | VDI infrastructure is usually connected to fast LAN/WAN links to infrastructure servers hosting data
BitLocker Drive Encryption Service | Manual (TS) | Disabled | BitLocker is not available to be used on a virtual machines
Block Level Backup Engine Service | Manual | Disabled | Service is used to backup data on the workstation "“ not used for virtual machines
Bluetooth Support Service | Manual (TS) | Disabled | Bluetooth Wireless not supported from a virtual machine
BranchCache | Manual | Consider | This service caches network content from peers on the local subnet.
Computer Browser | Manual (TS) | Disabled | Maintains an updated list of computers on the network and supplies this list to computers designated as browsers.
Device Association Service | Manual (TS) | Disabled | Enables pairing between the system and wired or wireless devices.
Device Setup Manager | Manual (TS) | Disabled | Enables the detection, download and installation of device-related software. If this service is disabled, devices may be configured with outdated software, and may not work correctly.
Diagnostic Policy Service | Automatic | Disabled | The Diagnostic Policy Service enables problem detection, troubleshooting and resolution for Windows components. If this service is stopped, diagnostics will no longer function.
Diagnostic Service Host | Manual | Disabled | The Diagnostic Service Host is used by the Diagnostic Policy Service to host diagnostics that need to run in a Local Service context. If this service is stopped, any diagnostics that depend on it will no longer function.
Distributed Link Tracking Client | Automatic | Consider | Tracks NTFS links locally and across the network (but only if the service is also running on the remote system)
Encrypting File System (EFS) | Manual (TS) | Consider | Provides the core file encryption technology used to store encrypted files on NTFS file system volumes. If this service is stopped or disabled, applications will be unable to access encrypted files.
Extensible Authentication Protocol | Manual | Consider | The Extensible Authentication Protocol (EAP) service provides network authentication in such scenarios as 802.1x wired and wireless, VPN, and Network Access Protection (NAP).
Family Safety | Manual | Disabled | This service is a stub for Windows Parental Control functionality that existed in Vista. It is provided for backward compatibility only.
Fax | Manual | Disabled | Enables you to send and receive faxes, utilizing fax resources available on this computer or on the network.
Function Discovery Resource Publication | Manual | Disabled | Publishes this computer and resources attached to this computer so they can be discovered over the network. If this service is stopped, network resources will no longer be published and they will not be discovered by other computers on the network.
File History Service | Manual (TS) | Consider | Protects user files from accidental loss by copying them to a backup location
Home Group Listener | Manual | Disabled | Used to establish Home Groups, not used with virtual machines in a corporate environment
Home Group Provider | Manual (TS) | Disabled | Used to establish Home Groups, not used with virtual machines in a corporate environment
Internet Connection Sharing (ICS) | Disabled | Disabled | Provides network address translation, addressing, name resolution and/or intrusion prevention services for a home or small office network.
Microsoft Account Sign-in Assistant | Manual (TS) | Consider | Enables user sign-in through Microsoft account identity services. If this service is stopped, users will not be able to logon to the computer with their Microsoft account.
Microsoft iSCSI Initiator Service | Manual | Disabled | iSCSI will not be used on virtual desktops
Microsoft Software Shadow Copy Provider | Manual | Disabled | Manages software-based volume shadow copies taken by the Volume Shadow Copy service. If this service is stopped, software-based volume shadow copies cannot be managed. If this service is disabled, any services that explicitly depend on it will fail to start.
Network List Service | Manual | Automatic | Identifies the networks to which the computer has connected, collects and stores properties for these networks, and notifies applications when these properties change.
Offline Files | Manual (TS) | Disabled "“ REQUIRES GPO | The Offline Files service performs maintenance activities on the Offline Files cache, responds to user logon and logoff events, implements the internals of the public API, and dispatches interesting events to those interested in Offline Files activities and changes in cache state.
Optimize Drives | Manual | Disabled | Helps the computer run more efficiently by optimizing files on storage drives.
Sensor Monitoring Service | Manual (TS) | Consider | Monitors various sensors in order to expose data and adapt to system and user state. If this service is stopped or disabled, the display brightness will not adapt to lighting conditions. Stopping this service may affect other system functionality and features as well.
Secure Socket Tunneling Protocol Service | Manual | Disabled | This service publishes a machine name using the Peer Name Resolution Protocol. Configuration is managed via the netsh context 'p2p pnrp peer'
Shell Hardware Detection | Automatic | Disabled | Provides notifications for AutoPlay hardware events.
SNMP Trap | Manual | Disabled | Receives trap messages generated by local or remote Simple Network Management Protocol (SNMP) agents and forwards the messages to SNMP management programs running on this computer. If this service is stopped, SNMP-based programs on this computer will not receive SNMP trap messages. If this service is disabled, any services that explicitly depend on it will fail to start.
SSDP Discovery | Manual | Disabled | Discovers networked devices and services that use the SSDP discovery protocol, such as UPnP devices. Also announces SSDP devices and services running on the local computer. If this service is stopped, SSDP-based devices will not be discovered. If this service is disabled, any services that explicitly depend on it will fail to start.
Telephony | Manual | Disabled | Provides Telephony API (TAPI) support for programs that control telephony devices on the local computer and, through the LAN, on servers that are also running the service.
Themes | Automatic | Consider | Provides user experience theme management.
UPnP Device Host | Manual | Disabled | Allows UPnP devices to be hosted on this computer. If this service is stopped, any hosted UPnP devices will stop functioning and no additional hosted devices can be added. If this service is disabled, any services that explicitly depend on it will fail to start.
Volume Shadow Copy | Manual | Consider | Manages and implements Volume Shadow Copies used for backup and other purposes. If this service is stopped, shadow copies will be unavailable for backup and the backup may fail. If this service is disabled, any services that explicitly depend on it will fail to start.
Windows Backup | Manual | Disabled | Provides Windows Backup and Restore capabilities.
Windows Color System | Manual | Disabled | The WcsPlugInService service hosts third-party Windows Color System color device model and gamut map model plug-in modules.
Windows Connect Now - Config Registrar | Manual | Disable | WCNCSVC hosts the Windows Connect Now Configuration which is Microsoft's Implementation of Wi-Fi Protected Setup (WPS) protocol.
Windows Defender | Automatic (TS) | Consider "“ REQUIRES GPO | Helps protect users from malware and other potentially unwanted software
Windows Error Reporting Service | Manual (TS) | Disabled | Allows errors to be reported when programs stop working or responding and allows existing solutions to be delivered. Also allows logs to be generated for diagnostic and repair services.
Windows Media Player Network Sharing Service | Manual | Disabled | Shares Windows Media Player libraries to other networked players and media devices using Universal Plug and Play
Windows Search | Automatic (Delayed) | Consider | Provides content indexing, property caching, and search results for files, e-mail, and other content.
WLAN AutoConfig | Manual | Disabled | The WLANSVC service provides the logic required to configure, discover, connect to, and disconnect from a wireless local area network (WLAN) as defined by IEEE 802.11 standards.
WWAN AutoConfig | Manual | Disabled | This service manages mobile broadband (GSM & CDMA) data card/embedded module adapters and connections by auto-configuring the networks. It is strongly recommended that this service be kept running for best user experience of mobile broadband devices.

To make it really easy for you to apply this to your environment I have done all the hard work and created a Group Policy Preference template with all the above services listed. Simply download the below file to the computer you edit your group policy object on and drag it into the Group Policy Preferences services section of your GPO.

**Note:** All services set to "Consider" do exist but their status will not be changed.

**_WARNING!!!!_** Group Policy Preferences will TATOO all changes. Meaning one you have applied this setting it WILL NOT rollback the services configuration to default. So"... Apply carefully and after proper testing.

Once you have applied the template you can see a drop in ram usage but as well as that you will prevent 36 schedule system tasks from running thus milking the last drops of performance out of your VDI environment.