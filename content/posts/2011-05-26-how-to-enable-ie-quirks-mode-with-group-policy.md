---
title: "How to enable IE Quirks Mode with Group Policy"
date: 2011-05-26 10:00:00
author: admin
categories: ["Tutorials"]
tags: ["Group Policy", "Internet Explorer", "Quicks Mode"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2011/05/IE6Logo_thumb.jpg"
---

[![IE6Logo](https://www.grouppolicy.biz/wp-content/uploads/2011/05/IE6Logo_thumb.jpg)](<https://www.grouppolicy.biz/wp-content/uploads/2011/05/IE6Logo.jpg>)If you are looking at moving to Windows 7 or you are looking upgrading IE6 in your organisation you have probably discovered that a lot of your intranet web sites don't work properly. Well apparently 80% of IE app compatibility issues are cause by website that do not have the <!DOCTYPE> header as the with IE8 (See below).

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/05/image_thumb1.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/05/image4.png>)

This problem is due to a bug in IE6 that it ignores the <!DOCTYPE> if it is not on the first row and then default back to rendering the page in Quirks mode. The problem is that newer browsers do read this <!DOCTYPE> tag if it is not on the first line and it then starts to renders the page in standards mode as requested. So to address this issue Microsoft have released a hotfix for IE8 and include in IE9 a feature that lets you force pages to render in Quicks Mode thus ignoring the <!DOCTYPE> line.

> A webpage is not displayed correctly in Internet Explorer when any of the following is true:

>
>   * You use Windows Internet Explorer 8 Standards mode to browse the webpage.

>   * You enable Compatibility View in Internet Explorer 7 to browse the webpage.

>

>

> Additionally, if you do not have the permissions to implement the Meta tag or the HTTP header for browser emulation, you cannot force the browser to work in QUIRKS mode from the client-side.

Microsoft KB [A webpage is not displayed correctly when you browse the webpage by using Internet Explorer 8 Standards mode or Compatibility View in Internet Explorer 7](<http://support.microsoft.com/kb/982063/en-gb> "http://support.microsoft.com/kb/982063/en-gb")

Once you have the hotfix deployed or you have installed IE9 on your computers you can then use the policy "[Use Policy List of Quirks Mode sites](<http://gps.cloudapp.net/Default.aspx?PolicyID=7079>)" under Software\Policies\Microsoft\Internet Explorer\BrowserEmulation\QuirksPolicyList to add specific sites to render as quirks mode.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/05/image_thumb2.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/05/image5.png>)

This will now force your browser to render the page using IE5.5 (a.k.a. Quirks) mode so that the page now renders correctly.

**TIP:** If you are still having issues with your Intranet pages not working correctly one of the other big compatibility fixes you can try is to make sure that the page is properly placed in the "Intranet Zone". For instructions on how to do this see my other post [How to use Group Policy to configure Internet Explorer security zone sites](<https://www.grouppolicy.biz/2010/03/how-to-use-group-policy-to-configure-internet-explorer-security-zone-sites/> "https://www.grouppolicy.biz/2010/03/how-to-use-group-policy-to-configure-internet-explorer-security-zone-sites/") .

Thanks to Chris Jackson "The App Compat Guy" for his TechEd 2011 video that had the details for me to write this article at <http://channel9.msdn.com/Events/TechEd/NorthAmerica/2011/WCL315>