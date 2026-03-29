---
title: "Windows 10 Administrative Templates"
date: 2015-08-05 05:52:33
author: admin
categories: ["News"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2015/07/img0_768x1366-150x150.jpg"
---

[![img0_768x1366](https://www.grouppolicy.biz/wp-content/uploads/2015/07/img0_768x1366-150x150.jpg)](<https://www.grouppolicy.biz/wp-content/uploads/2015/07/img0_768x1366.jpg>)Microsoft has now release the Windows 10 Administrative templates. These are similar to the files in the Policy Definitions folder under the Windows directory. However Microsoft also releases the templates as a separate download so you can install the new policy setting without having to first install Windows 10. These administrative templates also contain 10 additional ADMX files that are not shipped in the box with Windows 10.

  * Fileserverssagent.admx
  * grouppolicypreferences.admx
  * gamedvr.admx
  * terminalserver-server.admx
  * userdatabackup.admx
  * deliveryoptimization.admx
  * grouppolicy-server.admx
  * mmcsnapins1.admx
  * textinput.admx
  * windowsserver.admx

After you have downloaded and installed the file you will then need to copy the files from the "C:\Program Files (x86)\Microsoft Group Policy\Windows 10\PolicyDefinitions" to the Policy Definitions Central Store. Also note that this only adds Administrative Templates settings and you will still not get any change Group Policy Preferences by installing these files. For example you still need to have Windows 8.1 installed if you want to modify the IE 10/11 Group Policy Preferences. Download Link <http://www.microsoft.com/en-us/download/details.aspx?id=48257>