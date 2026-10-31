# Group Policy Central

Source for [Group Policy Central](https://grouppolicy.biz/), an independent archive of Windows Group Policy articles published between 2009 and 2019. The repository contains 424 Markdown articles, historical uploads and the static-site build tools. Older articles describe the products and guidance available when they were written; check current Microsoft documentation before applying them.

## Websites and deployment

| Site | Purpose | How it is deployed |
| --- | --- | --- |
| [grouppolicy.biz](https://grouppolicy.biz/) | Current public site | GitHub Actions generates and deploys the legacy layout to GitHub Pages from `main` when matching paths change. |
| [Cloudflare staging](https://grouppolicy-central-staging.pages.dev/) | Documentation-style redesign for review | Cloudflare Pages builds from `main` automatically. It is publicly accessible but sends `noindex, nofollow`; this is not access control. |

The staging project is not the public domain and DNS has not been cut over. Branch preview deployments are disabled. Pull requests run a build-only validation job; they do not deploy the GitHub Pages site. The GitHub Pages production job runs on qualifying pushes to `main`. See [Cloudflare staging and cutover notes](CLOUDFLARE-STAGING.md) before changing the build command, custom domain or DNS.

The current public build includes Google Analytics. The documentation-style builder removes that include in both staging and production mode; Cloudflare Web Analytics is currently disabled on the staging project. Choose and test an analytics setup and update the privacy notices before cutover if measurement continuity is required.

## Content and search

Articles live under `content/posts/YYYY/MM/`, with a date and slug in each filename. Posts have Markdown bodies and front matter containing their title, date, author, categories, tags and, where available, a featured image. The generated site preserves dated article routes and includes archive, category and tag pages, plus compatibility routes.

The browser search index covers **titles, the first approximately 250 characters of each article, categories and tags**. Search is case-insensitive substring matching, displays up to 10 results in archive order, and runs in the browser. It is not full-article, semantic or vector search.

## Local preview

The documentation-style build uses Python and the pinned packages in `requirements-cloudflare.txt`. Use a new, empty output directory: the builder refuses to overwrite an existing non-empty directory.

```bash
python -m venv .venv
# Activate .venv for your shell, then:
python -m pip install -r requirements-cloudflare.txt
python scripts/build_docs_preview.py --output _docs_preview --site-url http://127.0.0.1:8002
python -m http.server 8002 --bind 127.0.0.1 --directory _docs_preview
```

Open [http://127.0.0.1:8002/](http://127.0.0.1:8002/). PowerShell activation is `.\.venv\Scripts\Activate.ps1`; on macOS/Linux use `source .venv/bin/activate`.

To build the current GitHub Pages layout instead, install `requirements.txt` and run:

```bash
python scripts/generate_from_markdown.py --content content/posts --output _site_local --base-path / --site-url http://127.0.0.1:8001
python -m http.server 8001 --bind 127.0.0.1 --directory _site_local
```

The tracked `.env` contains the current public origin and root base path. The GitHub Actions workflow imports those defaults during deployment; explicit generator arguments are useful for local builds. Avoid publishing local or staging builds to the public domain.

## Build and crawler checks

For a staging-style build, use an origin that matches where the output will be served. Run the crawler check after building:

```bash
python scripts/verify_crawl_output.py _docs_preview --origin http://127.0.0.1:8002
```

The check verifies sitemap/canonical agreement, crawler directives, the staging `noindex` header and a 404 page. A separate `--production` build mode is documented in the [cutover notes](CLOUDFLARE-STAGING.md); it produces an indexable artifact for the public origin and does not itself deploy or change DNS. Review crawler access, analytics, URL compatibility and rollback before a cutover.

## Repository layout

- `content/posts/` — article source in Markdown.
- `uploads/` — historical images and downloadable files.
- `static/` — site styles, client-side search and other static assets.
- `scripts/generate_from_markdown.py` — legacy site generator and content conversion.
- `scripts/build_docs_preview.py` — documentation-style build layered on the generator.
- `scripts/verify_crawl_output.py` — crawler and sitemap checks for documentation builds.
- `.github/workflows/deploy-pages.yml` — pull request validation and GitHub Pages deployment.
- `CLOUDFLARE-STAGING.md` — staging settings and future cutover checks.

## Contributing

Corrections, accessibility improvements and context for older articles are welcome. Edit the relevant Markdown or source file and open a pull request. Preserve historical URLs and original content where practical; explain factual changes and link authoritative sources. See [CONTRIBUTING.md](CONTRIBUTING.md) and the [Code of Conduct](.github/CODE_OF_CONDUCT.md).

## Licence and attribution

Code and scripts are licensed under the [MIT License](LICENSE). Blog content is licensed under Creative Commons Attribution 4.0 International (CC BY 4.0); attribute Alan Burchill. Windows, Group Policy, Active Directory and related trademarks belong to Microsoft Corporation.
