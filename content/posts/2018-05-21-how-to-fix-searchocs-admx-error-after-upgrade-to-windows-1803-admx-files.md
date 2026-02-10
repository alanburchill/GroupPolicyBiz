---
title: "How to fix SearchOCS.ADMX Error after upgrade to Windows 1803 ADMX files"
date: 2018-05-21 00:09:27
author: admin
categories: ["News", "Tip"]
tags: ["ADML", "ADMX", "Error", "GPMC", "SearchOCR.ADMX", "Windows 10"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2018/05/SearchOCRError1-800x587.png"
---

With the recent release of the Windows 10 1803 Microsoft also released a new version of the ADMX/ADML files that corresponds to the new Group Polices with the OS (see <https://www.grouppolicy.biz/2018/05/administrative-template-for-windows-10-1803/> ) . Normally upgrading these policy files are as simple overwriting them into your "PolicyDefinitions" folder in your SYSVOL. However the SearchOCR.ADMX file that is not part of the ADMX/ADML nor is it included by default in the local "C:\Windows\PoliciyDefinitions" folder. But the same PolicyDefinitions pack does have the corresponding SearchOCR.ADML files. This means even if you have extracted the ADMX/ADML files and overwritten them in the ADMX/ADML Central Store then the SearchOCR.ADMX file won't updated but the SearchOCR.ADML file will be. This version mismatch until lately this has not been an issues, but the latest version of the ADML has a line missing that does not working with older versions of the SearchOCR.ADMX (see below). ![Resource '$\(string.Win7Only\)' referenced in attribute displayName could not be found. File \\\\corp.local\\SysVol\\corp.local\\Policies\\PolicyDefinitions\\SearchOCR.admx, line 12, column 69](https://www.grouppolicy.biz/wp-content/uploads/2018/05/SearchOCRError1-800x587.png) I can confirm with my testing that this is a problem if you still have a copy of the SearchOCR.ADMX file that is as old or older that Windows 10 1503. So where does this SearchOCR.ADMX file come from if it does not come with Windows out of the box?  The answer is that it's installed if you have the "Windows TIFF Ifilter" component installed. This then adds the SearchOCR.ADMX file to the local "C:\Windows\PolicyDefinitions" folder. ![Install Windows TIFF IFilter](https://www.grouppolicy.biz/wp-content/uploads/2018/05/TIFFSearch1-300x267.png) If you then at some stage copied the "PolicyDefinitions" folder from a computer with the "Windows TIFF IFilter" installed then you will have the "SearchOCR.ADMX" file in your central store. But as the ADMX/ADML policy pack or new version of Windows does not have this ADMX included by default when you overwrite the store this SearchOCR.ADMX file is not updated. So to fix this problem there are a number of choices:

  1. You can hand edit the relevant SearchOCR.ADML file and search for:


> <string id="OCR">OCR</string> <string id="OCREveryPage">Force TIFF IFilter to perform OCR for every page in a TIFF document

then add the line given below between them:

> <string id="OCR">OCR</string> **< string id="Win7Only">Microsoft Windows 7 or later</string>** <string id="OCREveryPage">Force TIFF IFilter to perform OCR for every page in a TIFF document

**Note:** I don't recommend this method as hand editing a file even as benign as an ADML file can have issues. To fix the problem properly you also have to change it for all language versions would take a lot of effort.

  2. If you do not use the Windows TIFF Ifilter group policy setting you can simply delete the "SearchOCR.ADMX" file. This of course means you will not longer have these relevant search settings listed in GPMC editor.
  3. You can install the "Windows TIFF IFilter" component on any version of Windows greater than Windows 10/Server 1603 and then manually copy the latest "SearchOCR.ADMX" file to the "PolicyDefinitions" folder. This will give you a matching version of the ADMX and ADML file which will resolve the problem.

So it's a simple enough issue, just remove or replace the relevant "SearchOCR.ADMX" file and the problem will be fixed. Reference: <https://social.technet.microsoft.com/Forums/en-US/cb97affb-9724-457b-a113-32cbd3d53331/searchocradmx-error-after-installing-win101803-admx-templates?forum=winserverGP>