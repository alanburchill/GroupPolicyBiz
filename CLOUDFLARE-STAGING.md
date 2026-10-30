# Cloudflare staging build

The staging site is a separate Cloudflare Pages Git project. It must not be attached to `grouppolicy.biz` or its DNS. The GitHub Pages workflow remains the owner of the current public site.

Cloudflare Pages settings for the intended project:

- Repository: `alanburchill/GroupPolicyBiz`; production branch: `main`.
- Project name: `grouppolicy-central-staging` (verify availability before creating).
- Framework preset: none; root directory: repository root.
- Build command: `python -m pip install -r requirements-cloudflare.txt && python scripts/build_docs_preview.py --output _cloudflare_site --site-url https://grouppolicy-central-staging.pages.dev`
- Build output directory: `_cloudflare_site`.
- Environment variables: `PYTHON_VERSION=3.14.7` and `SKIP_DEPENDENCY_INSTALL=1`. The build command installs the pinned staging requirements explicitly.
- Enable automatic production builds on every push to `main`; disable branch preview builds unless explicitly needed.

The command builds the Markdown archive, checks the generated post inventory, applies the documentation theme, suppresses the existing Google Analytics include and creates an `_headers` file that asks search engines not to index the staging site. A Pages default URL is publicly accessible: noindex is not access control. This staging artifact is approximately 428 MB and contains the public site's full uploaded media archive.

Before enabling the build, ensure the exact Pages project name is available. If Cloudflare assigns another name, update the build command's origin accordingly. Check the build, deployment commit, homepage, representative historical posts and redirects, search, media, theme, noindex response header, and absence of production analytics. Check that subsequent `main` pushes trigger a new build. Preserve the existing GitHub Pages deployment, DNS and domain settings.

The historical image accessibility gaps and other outstanding findings are documented in the local conversion review and must not be represented as resolved by deployment.
