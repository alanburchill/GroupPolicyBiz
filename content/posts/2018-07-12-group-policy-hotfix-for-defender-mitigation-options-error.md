---
title: "Group Policy Hotfix for Defender Mitigation Options Error"
date: 2018-07-12 07:54:00
author: admin
categories: ["KB Focus"]
tags: ["Defender", "hotfix", "KB4338819", "Mitigation Option"]
---

Just a quick note that Microsoft has recently release a hot fix KB4338819 that fixes and issue with the Mitigation option. This is a Windows Defender setting that can be found under the Administrative Templates>Computers>System>Mitigation Options setting. The fix is described as:

> Addresses an issue that may cause the Mitigation Options Group Policy client-side extension to fail during GPO processing. The error message is "Windows failed to apply the MitigationOptions settings. MitigationOptions settings might have its own log file" or "ProcessGPOList: Extension MitigationOptions returned 0xea." This issue occurs when Mitigation Options has been defined either manually or by Group Policy on a machine using Windows Defender Security Center or the PowerShell Set-ProcessMitigation cmdlet.

Source: <https://support.microsoft.com/en-us/help/4338819/windows-10-update-kb4338819>