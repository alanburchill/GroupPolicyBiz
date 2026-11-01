# Cloudflare deployment and rollback

As of 1 November 2026, Cloudflare Pages serves the public site at https://grouppolicy.biz/. Cloudflare is also authoritative for DNS. The Pages project retains the historical name `grouppolicy-central-staging`; its default Pages URL now serves the production build and is not an isolated staging environment. Deployment-specific preview URLs may carry Cloudflare's noindex header. GitHub Pages and its custom-domain configuration remain available for rollback.

Production Pages settings:

- Repository: `alanburchill/GroupPolicyBiz`; production branch: `main`; automatic production deployments enabled and branch preview builds disabled.
- Project: `grouppolicy-central-staging`; root directory: repository root.
- Build command: `python -m pip install -r requirements-cloudflare.txt && python scripts/build_docs_preview.py --production --output _cloudflare_site --site-url https://grouppolicy.biz`
- Build output directory: `_cloudflare_site`.
- Environment variables: `PYTHON_VERSION=3.14.7` and `SKIP_DEPENDENCY_INSTALL=1`.
- DNS: proxied apex CNAME to `grouppolicy-central-staging.pages.dev`; proxied www CNAME to `grouppolicy.biz`. The zone enforces HTTPS and redirects HTTPS www requests to the apex, preserving path and query.

Production mode omits the staging noindex directives and uses the public origin in canonical links, feeds and sitemap. The build removes the legacy Google Analytics include; Cloudflare injects its Web Analytics script. A local staging-style build without `--production` remains possible, but do not publish it to the production hostname.

At launch, verify the public domain, redirects, canonical links and sitemap all agree, missing URLs return HTTP 404, no noindex header or meta tag remains, robots.txt permits intended search crawlers, and Cloudflare security rules allow verified crawlers. Submit the sitemap through search-engine webmaster tools and inspect representative live URLs. These checks do not guarantee indexing, ranking or AI citations. Article summaries and structured metadata are tracked separately in issue #7.

## Rollback to GitHub Pages

The prior DNS-only apex records were four A records (`185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`) and four AAAA records (`2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153`). The previous DNS-only www CNAME targeted `alanburchill.github.io`. The prior TTL was 300 seconds. Preserve unrelated DNS records.

If rollback is needed, replace the apex Pages CNAME with those eight DNS-only GitHub records, and restore the DNS-only www CNAME to `alanburchill.github.io`. Verify the GitHub Pages custom-domain and HTTPS settings, both names and redirects, and monitor multiple resolvers for the cache window; some clients may retain older answers longer. Do not remove the GitHub Pages domain configuration while it remains the fallback. Test the GitHub origin directly with a hostname-preserving `curl --resolve` request before relying on it. Cloudflare Web Analytics and Google Analytics have separate reports; the legacy GitHub Pages build has its own Google Analytics include.

The historical image accessibility gaps and other outstanding findings are documented in the local conversion review and must not be represented as resolved by deployment.
