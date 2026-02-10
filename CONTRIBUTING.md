# Contributing to GroupPolicy.biz Archive

Thank you for your interest in improving this archive of Group Policy content! This repository preserves historical articles from 2009-2026, and we welcome contributions that improve accuracy, fix errors, or enhance readability.

## How to Contribute

### Quick Edits

1. **Find an error or typo?** Click the "Edit this page on GitHub" link at the bottom of any article
2. Make your changes directly in the GitHub editor
3. Submit a pull request with a clear description of what you fixed

### Larger Contributions

1. **Fork this repository** to your own GitHub account
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/GroupPolicyBiz.git
   cd GroupPolicyBiz
   ```
3. **Create a branch** for your changes:
   ```bash
   git checkout -b fix/article-name-issue
   ```
4. **Make your changes** to markdown files in `content/posts/`
5. **Test locally** (see below)
6. **Commit and push** your changes
7. **Submit a pull request** from your fork

## Testing Your Changes Locally

Before submitting a pull request, test that the site builds correctly:

### Prerequisites
- Python 3.11 or higher
- Required packages: `pip install -r requirements.txt`

### Build the Site
```bash
python scripts/generate_from_markdown.py
```

This generates the site in the `_site/` directory. Open `_site/index.html` in your browser to preview.

### Check for Errors
- Ensure no Python errors occur during generation
- Verify your edited articles render correctly
- Check that links and formatting work as expected

## Contribution Guidelines

### What We Accept
✅ Fixing typos, grammar, or formatting errors  
✅ Correcting technical inaccuracies  
✅ Improving code examples or explanations  
✅ Adding missing links or references  
✅ Updating broken external links (use archive.org when possible)

### What We Don't Accept
❌ Removing or significantly altering historical content  
❌ Adding new articles (this is an archive of past content)  
❌ Promotional content or spam  
❌ Changes that alter the historical record without clear justification

### Markdown Style Guidelines
- Use standard Markdown syntax
- Keep front matter intact (title, date, categories, tags)
- Preserve the original publication date
- Use relative links for internal references
- Code blocks should specify language: ` ```powershell ` or ` ```xml `

### Commit Messages
Write clear, concise commit messages:
- **Good**: `Fix typo in GPO precedence article`
- **Good**: `Correct registry path in Windows 10 lockdown post`
- **Bad**: `Fixed stuff`

## Questions or Issues?

- **Found a bug?** [Open an issue](https://github.com/alanburchill/GroupPolicyBiz/issues)
- **Have a question?** [Start a discussion](https://github.com/alanburchill/GroupPolicyBiz/discussions)
- **Need help?** Open a pull request anyway - we're happy to help refine contributions

## License

By contributing, you agree that your contributions will be licensed under the same license as this project:
- Code and scripts: [MIT License](LICENSE)
- Content and articles: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

Your contributions must be your own work and not violate any copyrights.

---

Thank you for helping preserve and improve this Group Policy knowledge base! 🙏
