---
title: "How to find and use WMI values for Group Policy Filtering"
date: 2010-02-03 09:00:00
author: admin
categories: ["News", "Tutorials"]
tags: ["GPMC", "Group Policy", "Intermediate", "WMI filtering"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/02/image_thumb.png"
---

The [Ask the Performance](<http://blogs.technet.com/askperf>) Team has published a [WMI Code Creator](<http://blogs.technet.com/askperf/archive/2010/02/02/two-minute-drill-wmi-code-creator.aspx>) tool that allows queries your local WMI repository on your computer. This too can be useful if you want to find the WMI values to use with a WQL query filter for your Group Policy Objects (GPO). The tool itself does not actually create a WQL query for WMI filtering however you can it to get the required values and then then plug them into an existing WQL query.

Here I will take you though the WMI Code Creator tool to get the values to make a filter to apply a GPO only to Latitude D830 computers. You can customize the query by simply substituting the Class and Property values of your choice.

Step 1. Open the WMI Code Creator tool.

Step 2. Select the Class you want to use and then select the properties you want to filter on.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/02/image_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/02/image.png>)

Step 3. Click the "Execute Code" button and you will see the value of the property

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/02/image_thumb1.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/02/image1.png>)

Take the highlighted values in the screen shots above and replace them in the query below.

> Select * from **Win32_ComputerSystem** where **model** = '**Latitude D830'**

Step 4. Open Group Policy Management Console (GPMC) and navigate to Group Policy Management > Forest > Domains > _DomainName_ > WMI Filters

Step 5. Click Action menu and then New"...

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/02/image_thumb2.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/02/image2.png>)

Step 6. Enter the name of the WMI Filter then click Add (e.g. Latitude D830)

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/02/image_thumb3.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/02/image3.png>)

Step 7. Now enter the WQL query into the Query field and click OK

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/02/image_thumb4.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/02/image4.png>)

Step 8. Click Save

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/02/image_thumb5.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/02/image5.png>)

The filter will now be listed in the WMI Filters section of GPMC for use by other Group Policy Objects.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/02/image_thumb6.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/02/image6.png>)

To use the Group Policy WMI filter select a GPO in GPMC and you will be able to select the filter in the "WMI Filtering" section at the bottom of the Scope tab.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/02/image_thumb7.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/02/image7.png>)

So now you have applied a WMI filter to an existing GPO so that it will only be applied to Latitude D830 computers. This can be especially useful if you want to deploy hardware specific updates (e.g. drivers) to a particular type of computer.

Here are two other useful example of a WMI filter query:

Windows Vista or greater

SELECT Version, ProductType FROM Win32_OperatingSystem WHERE Version >= '6.0' AND ProductType = '1'

Windows 7 of Greater

SELECT Version, ProductType FROM Win32_OperatingSystem WHERE Version >= '6.1' AND ProductType = '1'

Additional Links

  * To get the WMI Code Creator tool visit [Ask the Performance Team : Two Minute Drill "“ WMI Code Creator](<http://blogs.technet.com/askperf/archive/2010/02/02/two-minute-drill-wmi-code-creator.aspx>)
  * For more information about group policy filtering see [Security Filtering, WMI Filtering, and Item-level Targeting in Group Policy Preferences](<http://blogs.technet.com/grouppolicy/archive/2009/07/30/security-filtering-wmi-filtering-and-item-level-targeting-in-group-policy-preferences.aspx> "http://blogs.technet.com/grouppolicy/archive/2009/07/30/security-filtering-wmi-filtering-and-item-level-targeting-in-group-policy-preferences.aspx")
  * Another use of WMI filtering is in SCCM Operating System Deployment see [Driver Management (Part 1) - Configuration Manager](<http://blogs.technet.com/deploymentguys/archive/2008/02/15/driver-management-part-1-configuration-manager.aspx> "http://blogs.technet.com/deploymentguys/archive/2008/02/15/driver-management-part-1-configuration-manager.aspx")