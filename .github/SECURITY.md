# Security Policy

## Supported Scope

This repository is a static site and content archive. Security support currently applies to:

- The `main` branch source code and build scripts
- GitHub Actions workflows in `.github/workflows/`
- The deployed site at <https://www.grouppolicy.biz>
- Dependencies listed in `requirements.txt`

The following are generally **out of scope** unless they create a real security risk in the current site or build pipeline:

- Historical article content accuracy issues
- Broken links, typos, or formatting defects
- Third-party websites linked from archived posts
- Old generated folders kept only for local validation or comparison

## Reporting a Vulnerability

Please **do not open a public issue** for suspected security vulnerabilities.

Instead, use one of the following:

1. **Preferred:** Use GitHub's private vulnerability reporting for this repository, if the **Report a vulnerability** option is available under the repository's **Security** tab.
2. If private reporting is not available, contact the repository owner via GitHub:
   - <https://github.com/alanburchill>

When reporting, please include:

- A clear description of the issue
- Affected files, URLs, or workflow steps
- Reproduction steps or proof of concept
- Potential impact
- Any suggested remediation, if known

Please avoid publicly disclosing the issue until it has been reviewed and a fix or mitigation is in place.

## What to Expect

We will try to:

- Acknowledge receipt within **7 days**
- Confirm whether the issue is in scope
- Share remediation status when practical
- Credit responsible disclosure when appropriate and desired

Response times may vary because this is a community-maintained archive project.

## Good-Faith Research

We appreciate responsible disclosure and good-faith security research. Please:

- Avoid actions that would degrade site availability
- Do not exfiltrate, alter, or destroy data
- Do not access accounts or private systems
- Limit testing to what is necessary to demonstrate the issue

## Security Hardening Priorities

Issues are most helpful when they relate to:

- Dependency vulnerabilities
- Cross-site scripting or unsafe HTML/script injection
- GitHub Actions or deployment workflow weaknesses
- Credential, secret, or token exposure
- Supply-chain or build integrity concerns
