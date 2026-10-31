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

For a future, separately authorised public cutover, build an indexable artifact with `python scripts/build_docs_preview.py --production --output _cloudflare_site --site-url https://grouppolicy.biz`. Production mode accepts only that public origin and omits the staging noindex directives. The build emits a robots.txt sitemap address for its own origin and a top-level 404 page for missing routes. The existing crawler policy allows all user agents, including search and AI crawlers; decide separately if training crawlers should be restricted. Do not enable the production command or attach the public hostname until cutover is authorised.

At launch, verify the public domain, redirects, canonical links and sitemap all agree, missing URLs return HTTP 404, no noindex header or meta tag remains, robots.txt permits intended search crawlers, and Cloudflare security rules allow verified crawlers. Submit the sitemap through search-engine webmaster tools and inspect representative live URLs. These checks do not guarantee indexing, ranking or AI citations. Article summaries and structured metadata are tracked separately in issue #7.

Before enabling the build, ensure the exact Pages project name is available. If Cloudflare assigns another name, update the build command's origin accordingly. Check the build, deployment commit, homepage, representative historical posts and redirects, search, media, theme, noindex response header, and absence of production analytics. Check that subsequent `main` pushes trigger a new build. Preserve the existing GitHub Pages deployment, DNS and domain settings.

The historical image accessibility gaps and other outstanding findings are documented in the local conversion review and must not be represented as resolved by deployment.
