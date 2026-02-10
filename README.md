# 🌐 GroupPolicy.biz - Source Repository

**Welcome!** This is the official source repository for [www.grouppolicy.biz](https://www.grouppolicy.biz), a comprehensive archive of Windows Group Policy knowledge spanning from 2009 to 2026.

## 📖 About This Site

For over 15 years, GroupPolicy.biz has been a trusted resource for Windows system administrators, providing:

- **424+ technical articles** covering Group Policy fundamentals, advanced configurations, and troubleshooting
- **In-depth tutorials** on Active Directory integration, security filtering, WMI filtering, and more
- **Best practice guides** for GPO design, deployment, and management
- **Historical documentation** tracking the evolution of Group Policy from Windows Server 2008 to modern Windows

This repository contains all the source Markdown files, scripts, and assets that power the live site. By open sourcing this content, we're preserving years of community knowledge and making it accessible for future generations of IT professionals.

## 🎯 What's Inside

- **Content**: 424 blog posts converted from WordPress to Markdown
- **Timeframe**: July 2009 - January 2026
- **Topics**: Group Policy, Active Directory, Windows Server, Security, AGPM, PowerShell
- **Images**: 16+ years of screenshots, diagrams, and examples
- **Format**: Clean, searchable Markdown with proper formatting

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

- **Fix errors**: Found a typo or technical error? Submit a PR
- **Update content**: Have updated information for older posts? Let us know
- **Add modern context**: Many posts reference older Windows versions - add notes about current equivalents
- **Improve formatting**: Help make content more readable
- **Share knowledge**: Found this helpful? Star the repo and share with others

### How to Contribute

1. **Fork this repository**
2. **Edit Markdown files** in `content/posts/`
3. **Submit a Pull Request** with your changes
4. **Automated build** will generate the updated static site

### Markdown File Format

Each post is a Markdown file with front matter:

```markdown
---
title: "Your Post Title"
date: 2019-07-25 10:30:00
author: admin
categories: ["News", "Tip"]
tags: ["Windows 10", "Group Policy", "Edge"]
featured_image: "/uploads/2019/07/image.png"
---

Your content here in Markdown format...
```

### File Naming Convention

Files should be named: `YYYY-MM-DD-post-slug.md`

Example: `2019-07-25-edge-chromium-ie-mode-now-works.md`

## Local Development

### Prerequisites

- Python 3.11+
- pip packages: `beautifulsoup4`, `lxml`, `html2text`, `requests`, `markdown`, `pyyaml`

### Generate Site Locally

```bash
# Install dependencies
pip install beautifulsoup4 lxml html2text requests markdown pyyaml

# Generate site from Markdown files
python scripts/generate_from_markdown.py \
  --content content/posts \
  --output _site \
  --per-page 12

# Serve locally (requires Python 3)
python -m http.server 8000 --directory _site
```

Then open http://localhost:8000 in your browser.

## Repository Structure

```
├── .github/
│   └── workflows/
│       └── build-deploy.yml        # GitHub Actions workflow
├── content/
│   └── posts/                      # Markdown source files (424 posts)
│       ├── 2019-07-25-post-1.md
│       ├── 2019-06-20-post-2.md
│       └── ...
├── static/                         # Static assets
│   ├── styles.css                  # Site stylesheet
│   ├── search.js                   # Client-side search
│   └── about.html                  # About page content
├── uploads/                        # Images and media files
│   ├── 2019/
│   ├── 2018/
│   └── ...
├── scripts/
│   └── generate_from_markdown.py   # Site generator (Markdown → HTML)
└── _site/                      # Generated static site (not in Git)
    ├── index.html
    ├── posts/
    ├── category/
    └── ...
```

## GitHub Actions Workflow

The site automatically rebuilds and deploys when:

- You push changes to the `main` branch
- Someone's Pull Request is merged
- Files in `content/` or `scripts/` are modified

The workflow:
1. Checks out the repository
2. Sets up Python 3.11
3. Installs dependencies
4. Runs the static site generator
5. Deploys to GitHub Pages

## GitHub Pages Setup

1. Go to **Settings** → **Pages**
2. Set **Source** to "GitHub Actions"
3. Your site will be available at: `https://alanburchill.github.io/GroupPolicyBiz/`

## ✨ Site Features

The generated static site includes:

- 🔍 **Full-text search** across all 424 posts
- 🏷️ **509 tags** for granular topic filtering
- 📁 **19 categories** for browsing by subject
- 📅 **Year archives** (2009-2026)
- 🔗 **Legacy URL redirects** maintaining original WordPress paths
- 🌓 **Dark mode support** for comfortable reading
- 📱 **Mobile responsive** design
- ⚡ **Lightning fast** static site generation

## 🚀 Automation

✅ **Automatic builds** on content changes  
✅ **Pull Request previews** (builds run on PRs)  
✅ **Zero server maintenance** (GitHub handles hosting)  
✅ **Free hosting** via GitHub Pages  

## 🏗️ Technology Stack

- **Content**: Markdown with YAML front matter
- **Generation**: Python 3.11+ with html2text, BeautifulSoup, markdown
- **Hosting**: GitHub Pages (static site)
- **Deployment**: GitHub Actions (automated)
- **Search**: Client-side JavaScript with search index
- **Styling**: Custom CSS with Defender-inspired design

## Cleanup checklist before public release

Before making this repository publicly discoverable, please review and complete the following items:

1. Remove or relocate private backups and local-only files
   - Confirm `private_md/` and `tools/` contain no sensitive or private data (they are ignored by Git).
2. Sanitize scripts and config files
   - Remove absolute paths and local file references (e.g., OneDrive paths in conversion scripts).
   - Remove any credentials, tokens, or personal email addresses.
3. Review the `uploads/` directory for copyrighted or personal images
   - Decide whether to publish images under the repository or host them separately with proper attribution.
4. Verify there are no large binary files tracked in Git
   - Use `git ls-files` and `git rev-list` to find large files; remove or replace with links if necessary.
5. Run content QA checks
   - Run the site generator locally and browse the generated site at `_site/` to check links and navigation.
   - Use `tools/check_sitemap_coverage.py` to ensure legacy URLs map correctly.
6. Add repository metadata and governance files
   - Add `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md` if you plan to accept external contributions.
7. Audit `.gitignore` and local excludes
   - Ensure files you intend to keep private are only in local excludes (`.git/info/exclude` or global `~/.gitignore_global`).
8. Add attribution and disclaimers
   - Explicitly note trademarks, and include a short disclaimer about archived content being provided "as-is".
9. Final testing
   - Run `python scripts/generate_from_markdown.py --content content/posts --output _site --per-page 12` and spot-check posts and images.


## 📜 License

**Code and scripts** in this repository are licensed under the **MIT License**. See [LICENSE](LICENSE) for full details.

**Content (blog posts)** is licensed under **Creative Commons Attribution 4.0 International (CC BY 4.0)**. You are free to share and adapt the content for any purpose, including commercially, as long as you provide attribution to Alan Burchill.

Windows, Group Policy, Active Directory, and related trademarks are property of Microsoft Corporation.

## 📚 Additional Resources

For current Group Policy documentation, also visit:
- [Microsoft Group Policy Documentation](https://docs.microsoft.com/en-us/windows/client-management/group-policy-overview)
- [Group Policy Administrative Templates Catalog](https://admx.help/)
- [Group Policy PowerShell Cmdlets](https://docs.microsoft.com/en-us/powershell/module/grouppolicy/)

## 🙏 Acknowledgments

Thank you to everyone who has contributed to Group Policy knowledge over the years, and to the Windows administration community for making this resource valuable.

---

**Questions or Issues?** Open an [Issue](https://github.com/alanburchill/GroupPolicyBiz/issues) or submit a [Pull Request](https://github.com/alanburchill/GroupPolicyBiz/pulls).

**Live Site**: [www.grouppolicy.biz](https://www.grouppolicy.biz)
