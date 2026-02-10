---
title: "How to prevent x86 (32bit) applications installing via Group Policy on Windows x64"
date: 2010-03-25 21:00:00
author: admin
categories: ["Tutorials"]
tags: ["application deployment", "Group Policy", "Intermediate", "x64", "x86"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb75.png"
---

One of the powerful feature of Group Policy that have been around since its inception has been the ability to deploy and manage MSI based applications. Once senario you might find yourself in due to increasing popularity of Windows x64 is how do you deploy the right version of an application to your SOE however you are still running a mixture x86/x64 environments. Normally you can just deploy the x86 version of an application to both x86/x64 platforms however there are some scenarios where this might not be possible or simply not ideal.

Below I will show you how to prevent the deployment of the example application the "[Geosense for Windows](<http://geosenseforwindows.com/>)" to computer running Windows x64. Now this program is a good example as it come in both x86 and x64 bit versions as it comes with software-driven location sensor driver for Windows 7. Drivers are of course one of the few types of x86 applications you can install on a x64 versions of Windows. You may also want to use this option if you have a high performance x64 version of an application that can take advantage of the system with greater than 4gb of ram.

**Step 1.** Open the properties of the x86 application you want to prevent deploying to x64 Windows

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb75.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image75.png>)

**Step 2.** Click on the "Deployment" tab

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb76.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image76.png>)

**Step 3.** Click on "Advanced"..."

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb77.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image77.png>)

Notice that by default that Make 32-bit X86 application available to Win64 machines is ticked"...

**Step 4.** Un-tick "Make 32-bit X86 application available to Win64 machines"

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb78.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image78.png>)

**Step 5.** Click "OK"

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb79.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image79.png>)

Now the application will no longer try to install on x64 version of Windows.

So now you have prevent installing 32-bit version of the application on 64bit version of Windows how do I prevent x64 version of application from installing on 32-bit versions of Windows? Nothing.

As you can see below when you add an MSI for a 64bit application it detects the platform that it has been compiled so that it wont try and deploy x64 applications to x86 versions of Windows.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb80.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image80.png>)

Also note the "Make 32-bit X86 application available to Win64 machines" is not shown as option does not apply.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/03/image_thumb81.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/03/image81.png>)