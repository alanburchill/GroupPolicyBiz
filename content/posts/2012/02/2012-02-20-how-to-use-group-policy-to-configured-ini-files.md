---
title: "How to use Group Policy to configured INI files"
date: 2012-02-20 13:30:00
author: admin
categories: ["Tutorials"]
tags: ["Group Policy Preferences", "INI"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2012/02/image_thumb1.png"
---

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/02/image_thumb1.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/02/image1.png>)INI Files are one of those things that most administrators probably still need to mange in your environment due to one of those (crapy) apps that still not made the jump to registry keys. This is were there INI feature of Group Policy Preferences can be a great help in managing these files. What is really great about this option is that it also allows you to modify existing files without losing any existing custom modification.

Below I show you just a few examples of how you can use the GPP INI option when working with these files.

In my example I already have a file created called C:\test.ini with the following values.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/02/image_thumb2.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/02/image2.png>)

**TIP** : If the INI file is a global configuration file you will probably need to make this change as a computer policy as standard users probably won't need have the permission to make changes to the file.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/02/image_thumb3.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/02/image3.png>)

Select the "Update" action and fill out the fields as you need. I have circled the related fields in the same colour to show how they values match up.

**Note** : See that the existing information in the file is preserved.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/02/image_thumb4.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/02/image4.png>) [![image](https://www.grouppolicy.biz/wp-content/uploads/2012/02/image_thumb5.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/02/image5.png>)

Its also really easy to setup a new section by just specifying a different "Section Name".

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/02/image_thumb6.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/02/image6.png>) [![image](https://www.grouppolicy.biz/wp-content/uploads/2012/02/image_thumb7.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/02/image7.png>)

If you want to remove a Property from the INI file simply select the "Delete" action and the name of the property.

**Tip** : If you want to delete the entire INI file use the GPP [File Extensions](<http://technet.microsoft.com/en-us/library/cc771102.aspx>) option.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2012/02/image_thumb8.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/02/image8.png>) [![image](https://www.grouppolicy.biz/wp-content/uploads/2012/02/image_thumb9.png)](<https://www.grouppolicy.biz/wp-content/uploads/2012/02/image9.png>)

For more information on the INI file Group Policy Preference check out <http://technet.microsoft.com/en-us/library/cc772027.aspx>