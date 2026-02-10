---
title: "More Microsoft Guidance on MS16-072"
date: 2016-07-05 21:45:46
author: admin
categories: ["News"]
tags: ["hotfix", "ms16-072"]
---

So Microsoft PFE team have just released a blog called "Who broke my user GPO?" which is rather ironically title as the answer was "Microsoft did". But anyhow, this new post has a detail description of the problem and what can be done to fix the issues and what to do if you have AGPM deployed in your environment.. It also points out that you need to added either "Authenticated Users" or "Domain Computers" Read permission to fix the problem. But if you have a multiple domain environment you are going to need to add "Domain Computers" multiple times for the GPO's to work cross forest. See the full article here <https://blogs.technet.microsoft.com/askpfeplat/2016/07/05/who-broke-my-user-gpos/>