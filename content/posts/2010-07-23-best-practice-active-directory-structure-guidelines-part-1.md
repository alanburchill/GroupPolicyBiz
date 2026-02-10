---
title: "Active Directory Structure Guidelines &ndash; Part 1"
date: 2010-07-23 10:00:00
author: admin
categories: ["Best Practice", "Tutorials"]
tags: ["Active Directory", "ADUC", "Advanced", "Group Policy", "Naming Convention", "Organisational Unit"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2010/07/image23_thumb.png"
---

I have been doing Active Directory and Group Policy work for a while now and I have developed my own set of rules that I try to use where ever possible. So below I have written down all my rules in no particular order for you to go over and use for yourself. You may only chose to use only some of these rules or you might want to use them all depending on your circumstance. This is a two part series where I will first talk about designing you Active Directory Organisation Unit structure and then in part 2 ([Best Practice: Group Policy Design Guidelines "“ Part 2](<https://www.grouppolicy.biz/2010/07/best-practice-group-policy-design-guidelines-part-2/>)) I will discuss some more ideas for applying Group Policy to the OU structure.

I want to be clear that these are only guidelines and not rules that need to be strictly adhered to. In almost all case there are exceptions to these guidelines and you might even find your self implementing them in a hybrid approach. I intend for this web page to be updated on a regular basis as none of these rules are set in stone and thing obviously change all the time.




### Active Directory Organisation Unit Design Guidelines

****

### Before you begin

Before you begin the process of designing your Group Policy (and AD) structure you should first try to fully understand the requirements of the environment. Below are some points that I recommend that you find out before you begin:

  * How is the company structured
  * Where are the physical sites
  * Who support the organisation
    * What are the support boundaries (e.g. Location and/or Workstations and/or Servers )
  * What are the computer types
    * Highly Secured
    * Standard SOE
    * Process Control/Automation
    * Server Roles (e.g. Exchange, SQL or File Server)
  * Network Topology
    * Bandwidth / Latency
  * Who will be responsible for Group Policy changes
  * What are the security requirements (password policy, auditing etc.)
  * What is the change management process
  * What are the auditing requirements for Group Policy


### **Keep it short**

When naming your Organisational Unit make sure the name you are using are short and to the point. There is technically nothing wrong with having long OU names but it is a pain to document and just leave you open to more chance of references then name wrong as their are more characters to type.

**Bad Example** |  **Good Example**
---|---
[![image\[23\]](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image23_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image231.png>) | [![image\[21\]](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image21_thumb.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image211.png>)

### **Be intuitive**

Naming OU to something that is intuitive is good for new starters in the organisation. If you name a OU "OOG" a new starter in your organisation might not realise that this is the three letter international designation for [Coolangatta AirPort](<http://en.wikipedia.org/wiki/Gold_Coast_Airport>) which is the same suburb where your office is located. I know this is in conflict with rule 1 however it is also a balancing act your will have to carefully tread.

**Bad Example** | **Good Example**
---|---
[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb69.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image72.png>) | [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb70.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image73.png>)

****

### **Most to least significant from left to right**

OU structures in AD are [hierarchical](<http://en.wikipedia.org/wiki/Hierarchy>) therefore you need make your design fit to this structure. When deciding how your want to organise your OU structure you are probably going decide to make it either organisational or geographical. This is most important when you are going to a Geographical design as it is a physical impossibility to have one location located in two difference cities,states,countries or regions.

**Bad Example** | **Good Example**
---|---
[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb71.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image74.png>) | [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb72.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image75.png>)

****

### **Go wide not deep**

As a general rule you should only start creating another OU level if you are actually going to do something to that OU (e.g. delegate security or apply a group policy). Don't be tempted to create an elaborate structure to organise you AD object if there is not reason to do so. Having a deep OU structure also makes it very difficult to delegate security in the same delegating security on multiple folders deep to folder on a file share.

**Bad Example** | **Good Example**
---|---
[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb73.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image77.png>) | [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb96.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image101.png>)

****

### **Be consistent**

Don't mix your terms when naming our OU Structure as this leads to confusion if for IT admins that leads them to believe that something might be different about the two OU's where they actually contain the same type of objects. The example below shows how two different sites calls the OU for the computer in the organisation Workstations and Desktops.

**Bad Example** | **Good Example**
---|---
[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb97.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image102.png>) | [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb98.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image103.png>)

### Reserved Names

While it would be nice to have an OU called Computers and/or Users at the top level of your AD structure remember these are already container names and therefore cannot be used at the top level.

### Redirect New User and Computer Accounts

When a new user and or computer is created in Active Directory then by default they are created in the "Users" and "Computers" container. As a result these objects are not subject to any group policy except for the Default Domain Policy or any GPO that are linked to the domain (see [Part 2](<https://www.grouppolicy.biz/2010/07/best-practice-group-policy-design-guidelines-part-2/>)). Therefore you may want to consider redirecting where the default location for creating these new AD objects to a location that will allow you to easily apply GPO's specific for new users and computers. Before you do this however you will need to create a OU that you can designate as the default creation location. Consider creating a top level OU called "New" or "Default" and then create a Sub-OU called Users and Computers.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/08/image_thumb3.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/08/image4.png>)

You may have picked up that I have called the Sub-OU's Computers and Users which is in conflict with "Be Consistent" section above. However in this case we are not creating a default location for just workstations and just people we are creating a location for all new computers (workstations or servers) and user accounts (service accounts, people accounts or resource accounts). This naming convention is also consistent with the names of the default containers in the top of the AD so there is some logic with keeping the name.

See "Apply GPO to New Users and Computers" [Part 2](<https://www.grouppolicy.biz/2010/07/best-practice-group-policy-design-guidelines-part-2/>) where I will show you how to apply the Group Policy to these new default OU 's.

For more information on how to redirect the default Users and Computers Containers see [KB324949 Redirecting the users and computers containers in Active Directory domains](<http://support.microsoft.com/kb/324949> "http://support.microsoft.com/kb/324949")

#### References

[Designing an OU Structure that Supports Group Policy](<http://technet.microsoft.com/en-us/library/cc783140\(WS.10\).aspx> "http://technet.microsoft.com/en-us/library/cc783140\(WS.10\).aspx")

> "...change the default location where new user and computer accounts are created so you can more easily scope GPOs directly to newly created user and computer objects

### **Deciding what OU structure to use**

When designing your OU structure you need to keep in mind that companies do often change in size and often acquire or sell off divisions. Below I go thought the basic designs and then I show you how they can be combined into hybrid structures. For most organisation you will probably use hybrid of the various method that best suit your requirements.

Below I have listed some of the consideration for choosing an OU structure design (in no particular order):

  * Delegation of security
  * Application of Group Policy
  * Likeliness of divesting or acquiring other business
  * Geographical Locations "“ Global Region, Country, Weather Region, Closest International Airport, State, City, Suburb, Building, Floor
  * Risk Mitigation "“ You might not want to have 1 OU with 10,000 computers in it even if they are all configured the same as this makes it very easy to break all your computers with one easy mistake. In these extreme cases you might want to setup sub-OU's only with duplicate polices applied to them but this would only be done in extreme situations.


#### Organisational OU Structure

This method of organising your OU structure should be used if your have very clear and stable organisational boundaries. You are highly unlikely to use this type of structure by itself as this would have you lump all your users, groups, contacts and computer objects together in the same OU.

**Organisational**
---
[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb77.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image81.png>)

#### Geographical OU Structure

This method would be used where your company has many physical locations that perhaps have multiple divisions/departments in the same location. This would also be used if you did not have much variance between the configuration of computers in each physical location.

**Geographical**
---
[![image\[30\]](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image30_thumb1.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image302.png>)

#### References

[Designing an OU Structure that Supports Group Policy](<http://technet.microsoft.com/en-us/library/cc783140\(WS.10\).aspx> "http://technet.microsoft.com/en-us/library/cc783140\(WS.10\).aspx")

> you might consider geographically based OUs either as children or parents of the other OUs, and then duplicate the structure for each location

#### Resources OU Structure

When you are placing you AD objects in you OU structure it is very good idea to not lump your object types together in the same OU an in a few cases you might also want to consider splitting you resources up as separate sub-resource types. Having your resources separate greatly simplifies the permission you delegate to your specific types of AD objects and also allows you to more easily apply group policy objects to your computers and users accounts.

In most circumstances it is likely that the Resource OU's are and the lower end of the OU structure and are the OU that directly contain the AD objects (users,groups,contacts & computers)

Below is a list of example resource OU's and how you can break them down.

**Colour** | **Type of object it contains**
---|---
Yellow | Organisational Unit "“ No objects except for other OU's are direct members
Red | User Objects
Blue | Computer Objects
Green | Group Objects
Purple | Contact Objects
**Resource Structure Example**
---
[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb78.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image82.png>)

#### Reference

[TechNet: Designing Your Group Policy Model](<http://technet.microsoft.com/en-us/library/cc736938\(WS.10\).aspx> "http://technet.microsoft.com/en-us/library/cc736938\(WS.10\).aspx")

> Classify the types of computers and the roles or job function of users in your organization, group them into OUs, create GPOs to configure the environment for each as needed, and then link the GPOs to those OUs.

[Designing an OU Structure that Supports Group Policy](<http://technet.microsoft.com/en-us/library/cc783140\(WS.10\).aspx> "http://technet.microsoft.com/en-us/library/cc783140\(WS.10\).aspx")

> Think primarily about the objects you want to manage when you approach the design of an OU structure. You might want to create a structure that has OUs organized by workstations, servers, and users near the top level

> By using a structure in which OUs contain homogeneous objects, such as either user or computer objects but not both, you can easily disable those sections of a GPO that do not apply to a particular type of object.

### Two Level Hybrid Location / Resource OU Structure

In this example we see what happens when we combine the two Resource and Location OU structure designs. The decision to make it a Location/Resource or Resource/Location structure would be heavily based on how you configured your computers and users. If you configuration your users fairly consistently across the organisation and there is not much variation in how you configured you computers then you may want to consider a Resource/Location structure. Inversely if you make a lot custom configuration changes based on the location of the user and computer then you should consider using a Location/Resource structure.


**Two Level Hybrid (Location / Resource)** | **Two Level Hybrid (Resource / Location)**
---|---
[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb79.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image84.png>) | [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb80.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image85.png>)


### Two Level Hybrid Organisation / Resource OU Structure

This is similar to this example we saw above (Location / Resource) where we see what happens when we combine both Organisational and Location OU structure designs. The decision to make it a Organisational/Resource or Organisational/Location structure would be heavily based on wither how you configure your computers and users and the chance that you may divest or acquirer other businesses. If you consider there is a high chance of your company selling off or buying a certain department then you should consider using the Two Level Hybrid (Organisation / Resources) model. However if you are physically based in one location then and you think you will mainly apply configuration to all your users and computer consistently and only configured a small number of setting based on the organisation then you may want to consider the Two Level Hybrid (Resources / Organisational) model.

**Two Level Hybrid (Organisation / Resource)** | **Two Level Hybrid (Resource / Organisational)**
---|---
[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb81.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image86.png>) | [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb82.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image87.png>)

### Three Level Hybrid Organisation / Location / Resource OU Structure

The example below is called a Three Level Hybrid (Organisational / Location / Resource) model that would be used for most likely used for large organisation that have many sites and departments all of which have different configuration requirements. It is unlikely that you will want to use this three layer model of design unless you are a very large company with many divisions, locations.

**Three Level Hybrid (Organisation / Location / Resource )** | **Three Level Hybrid (Organisation / Location / Resource)**
---|---
[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb90.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image95.png>) | [![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb91.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image96.png>)

### Mixed-Hybrid OU Structure

This is the most complicated OU model you can deploy in your organisation. The below example shows a Organisational / Location / Resource for the users accounts however it has a two level Resource / Location model for the computers. You may want to have the Organisational / Location / Resource for the user accounts because they have very specific configuration requirements for the organisation. This example also has "Distribution Lists" group OU under the Organisational OU which is absent on the other examples but is shown here to demonstrate that there could be other non-users & non-computer at this bottom level. This would necessitate keeping the bottom third level OU to separate the resource of different types.

The other difference in this example is having the Resource / Workstation as a separate structure. This could be required if you have outsourced the maintenance of these computers to a third-party and you want to easily delegate administration access. This would also allow for the granular delegation to the third-party site based IT support staff without them having access to computers not in their local site.

**Mixed-Hybrid**
---
[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb92.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image97.png>)

### Isolate your Administrator Resources

If you are an organisation of any significant size you probably have a delegated cretin duties to specific teams (e.g. help desk or desktop support) via the way of administrator groups. This would allow you to easily grant the required permission for a IT support person to a specific user by only adding them to one group. However one of the permissions that is normally delegated is the ability to change group membership.

If all the groups in your organisation were in one location then a person who simply has the ability to add and remove member from group could in theory given them self more administrator access by adding them self to a higher level administrators group. To prevent this from happening you should segment all administrator or higher level permission group in the AD structure so that only the most trusted administrators can make changes to these admin groups.

Also remember there is a difference from having administrator or delegated access to the Active Directory object and local administrator access to a computer. Therefore under each Workstations and Servers resources OU you may also want to consider creating an Administrators OU that contains the local administrator security group of the computers accounts in the top level OU's. This would also assist and being able to easily delegate administrator access to both the computers AD object but also local administration as they are all contained in the one location in AD.

Another reason to you have a dedicated Administrators OU at the top level is so that your administrator accounts are not subject to the same SOE Group Policy setting than the rest of your users. Administrator accounts should also be a separate accounts for IT administrators as their normal day to day accounts should be subject to the same configuration as the rest of the staff. While this is something that a lot of IT staff loath I think it is very good idea for IT staff to set the example as to how computers are configured and [dogfood](<http://en.wikipedia.org/wiki/Dogfooding>) their own configuration. Ensuring that IT staff also have a separate administrator account also reduces greatly reduces the security risk associated with doing day to day operations (checking email, surfing web) with administrator permissions (see [How to use Group Policy to make Windows 7 90% more secure](<https://www.grouppolicy.biz/2010/04/how-to-use-group-policy-to-make-windows-7-90-more-secure/>)).

For more information on assigning local administrator access to computers via group policy check out my other article [How to use Group Policy Preferences to Secure Local Administrator Groups](<https://www.grouppolicy.biz/2010/01/how-to-use-group-policy-preferences-to-secure-local-administrator-groups/>)

**Isolated Administrator OU Structure**
---
[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb95.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image100.png>)

#### Reference

[TechNet: Using Security Filtering to Apply GPOs to Selected Groups](<http://technet.microsoft.com/en-us/library/cc728301\(WS.10\).aspx> "http://technet.microsoft.com/en-us/library/cc728301\(WS.10\).aspx")

> Create a separate OU for administrators and keep this OU out of the hierarchy to which you apply most of your management. In this way administrators do not receive most of the settings that that you provide for managed users.

>
> Have administrators use separate administrative accounts for use only when they perform administrative tasks. When not performing administrative tasks, they would still be managed.

### Do you REALLY need more than 4 levels?

Below is an example of a combined Organisational / Location / Resources / Sub Resource model that you could consider for 4 level deep this structure or a variation of these levels should pretty much handle most any requirements of any organisation. As you can see from my examples below you would be fairly pushed to require an OU structure more than 4 level deep so ask yourself this question if you start to contemplate a 5+ level structure.

4 Level OU Structure
---
[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/07/image_thumb94.png)](<https://www.grouppolicy.biz/wp-content/uploads/2010/07/image99.png>)

### I am so confused"... how about you just tell me what OU structure to use?

Ok. So your brain is probably about to explode with all the different OU types and you just don't know where to start. Well in the TechNet article [Designing an OU Structure that Supports Group Policy](<http://technet.microsoft.com/en-us/library/cc783140\(WS.10\).aspx>) we see a really good OU structure in Figure 2.3 Example OU Structure (see image below). You should be able to see how this is an three level OU structure combining Location/Resource/Sub-Recourse and that the naming convention of the structure match closely with guidelines we discussed above. You may find that this example will fit all your needs exactly or you may end up customising the design over time but either way this is a pretty good design that I have seen work in may organisations.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2010/08/image6.png)](<http://technet.microsoft.com/en-us/library/cc783140\(WS.10\).aspx>)

I hope the above AD design ideas have helped you design your organisations OU structure. Certainly there is no one size fits all model and you need to carefully consider your requirements before committing to a design.

Now I recommend that you you should visit the [second part in this series](<https://www.grouppolicy.biz/2010/07/best-practice-group-policy-design-guidelines-part-2/>) where I list my Group Policy design rules which heavily depend upon. This should hopefully show you how designing a good OU structure can help you substantially make administering Group Policy (and your entire AD) a lot more easier.

### Other References

  * [TechNet: Designing an OU Structure that Supports Group Policy](<http://technet.microsoft.com/en-us/library/cc783140\(WS.10\).aspx> "http://technet.microsoft.com/en-us/library/cc783140\(WS.10\).aspx")
  * [Designing an OU Structure that Supports Group Policy](<http://technet.microsoft.com/en-us/library/cc783140\(WS.10\).aspx> "http://technet.microsoft.com/en-us/library/cc783140\(WS.10\).aspx")


NEXT > [Best Practice: Group Policy Design Guidelines "“ Part 2](<https://www.grouppolicy.biz/2010/07/best-practice-group-policy-design-guidelines-part-2/>)