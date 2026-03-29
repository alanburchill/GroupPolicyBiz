#!/usr/bin/env python3
"""Crawl sitemap URLs, discover additional links from HTML, and report broken links.

The crawler starts from the provided sitemap URL, fetches all sitemap entries (including
nested sitemap indexes), crawls same-site HTML pages, extracts HTTP(S) links/assets, and
checks the status of every discovered URL.

Example:
    python scripts/check_site_links.py \
        --sitemap-url https://www.grouppolicy.biz/sitemap.xml \
        --output-json docs/site-link-check.json \
        --output-markdown docs/site-link-check.md
"""
from __future__ import annotations

import argparse
import json
import sys
import time
import xml.etree.ElementTree as ET
from collections import Counter, deque
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.parse import urldefrag, urljoin, urlparse

import requests
from bs4 import BeautifulSoup

SITEMAP_NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
DEFAULT_SITEMAP_URL = "https://www.grouppolicy.biz/sitemap.xml"
DEFAULT_JSON_OUTPUT = Path("docs/site-link-check.json")
DEFAULT_MARKDOWN_OUTPUT = Path("docs/site-link-check.md")
USER_AGENT = "GroupPolicyBiz Link Checker/1.0 (+https://www.grouppolicy.biz)"
HTML_CONTENT_TYPES = ("text/html", "application/xhtml+xml")
IGNORED_SCHEMES = {"mailto", "tel", "javascript", "data", "ftp"}
HTML_LINK_TAGS: tuple[tuple[str, str], ...] = (
    ("a", "href"),
    ("link", "href"),
    ("script", "src"),
    ("img", "src"),
    ("iframe", "src"),
    ("source", "src"),
    ("audio", "src"),
    ("video", "src"),
)


def attribute_text(value: object) -> str | None:
    if value is None:
        return None
    if isinstance(value, str):
        return value
    if isinstance(value, (list, tuple)):
        flattened = " ".join(str(item) for item in value if item is not None).strip()
        return flattened or None
    return str(value)


@dataclass(frozen=True)
class CheckResult:
    url: str
    final_url: str | None
    status_code: int | None
    ok: bool
    error: str | None
    content_type: str | None
    source_count: int
    sources: list[str]


class LinkChecker:
    def __init__(
        self,
        sitemap_url: str,
        timeout: float,
        max_workers: int,
        limit_pages: int | None,
    ) -> None:
        self.sitemap_url = sitemap_url
        parsed = urlparse(sitemap_url)
        self.root_host = parsed.netloc.lower()
        self.root_scheme = parsed.scheme or "https"
        bare_host = self.root_host[4:] if self.root_host.startswith("www.") else self.root_host
        self.allowed_hosts = {bare_host, f"www.{bare_host}"}
        self.timeout = timeout
        self.max_workers = max_workers
        self.limit_pages = limit_pages
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": USER_AGENT})
        self.discovered_sources: dict[str, set[str]] = {}
        self.html_cache: dict[str, str] = {}
        self.checked_results: dict[str, CheckResult] = {}

    def log(self, message: str) -> None:
        print(message, flush=True)

    def add_discovered_url(self, url: str, source: str) -> None:
        self.discovered_sources.setdefault(url, set()).add(source)

    def fetch_bytes(self, url: str) -> bytes:
        response = self.session.get(url, timeout=self.timeout)
        response.raise_for_status()
        return response.content

    def parse_sitemap(self, xml_bytes: bytes) -> tuple[str, list[str]]:
        root = ET.fromstring(xml_bytes)
        root_name = root.tag.rsplit("}", 1)[-1]
        if root_name == "sitemapindex":
            urls = [node.text.strip() for node in root.findall(".//sm:sitemap/sm:loc", SITEMAP_NS) if node.text]
            return root_name, urls
        if root_name == "urlset":
            urls = [node.text.strip() for node in root.findall(".//sm:url/sm:loc", SITEMAP_NS) if node.text]
            return root_name, urls
        return root_name, []

    def collect_sitemap_urls(self) -> list[str]:
        pending = deque([self.sitemap_url])
        seen_sitemaps: set[str] = set()
        collected: set[str] = set()

        self.log(f"[sitemap] starting from {self.sitemap_url}")

        while pending:
            sitemap_url = pending.popleft()
            if sitemap_url in seen_sitemaps:
                continue
            seen_sitemaps.add(sitemap_url)

            self.log(
                f"[sitemap] loading {len(seen_sitemaps)}: {sitemap_url} "
                f"(queued {len(pending)})"
            )

            xml_bytes = self.fetch_bytes(sitemap_url)
            root_name, urls = self.parse_sitemap(xml_bytes)
            if root_name == "sitemapindex":
                self.log(f"[sitemap] found index with {len(urls)} child sitemap(s)")
                for child in urls:
                    if child not in seen_sitemaps:
                        pending.append(child)
            elif root_name == "urlset":
                collected.update(urls)
                self.log(f"[sitemap] collected {len(urls)} URL(s); total {len(collected)}")

        self.log(f"[sitemap] completed with {len(collected)} total URL(s)")

        return sorted(collected)

    def normalize_url(self, candidate: str, base_url: str) -> str | None:
        if not candidate:
            return None

        joined = urljoin(base_url, candidate.strip())
        joined, _fragment = urldefrag(joined)
        parsed = urlparse(joined)

        if parsed.scheme.lower() in IGNORED_SCHEMES:
            return None
        if parsed.scheme.lower() not in {"http", "https"}:
            return None
        if not parsed.netloc:
            return None

        normalized_path = parsed.path or "/"
        normalized = parsed._replace(path=normalized_path)
        return normalized.geturl()

    def should_crawl_html(self, url: str) -> bool:
        parsed = urlparse(url)
        return parsed.netloc.lower() in self.allowed_hosts

    def extract_links_from_html(self, page_url: str, html: str) -> set[str]:
        soup = BeautifulSoup(html, "lxml")
        links: set[str] = set()

        for tag_name, attribute in HTML_LINK_TAGS:
            for tag in soup.find_all(tag_name):
                value = attribute_text(tag.get(attribute))
                normalized = self.normalize_url(value, page_url) if value else None
                if normalized:
                    links.add(normalized)

        for source_tag in soup.find_all(srcset=True):
            srcset = attribute_text(source_tag.get("srcset")) or ""
            for entry in srcset.split(","):
                candidate = entry.strip().split(" ", 1)[0]
                normalized = self.normalize_url(candidate, page_url) if candidate else None
                if normalized:
                    links.add(normalized)

        for meta_tag in soup.find_all("meta"):
            http_equiv = (attribute_text(meta_tag.get("http-equiv")) or "").lower()
            if http_equiv == "refresh":
                content = attribute_text(meta_tag.get("content")) or ""
                marker = "url="
                idx = content.lower().find(marker)
                if idx != -1:
                    candidate = content[idx + len(marker):].strip().strip("'\"")
                    normalized = self.normalize_url(candidate, page_url)
                    if normalized:
                        links.add(normalized)

        return links

    def fetch_html(self, url: str) -> tuple[str | None, requests.Response | None, str | None]:
        try:
            response = self.session.get(url, timeout=self.timeout, allow_redirects=True)
        except requests.RequestException as exc:
            return None, None, str(exc)

        content_type = response.headers.get("content-type", "")
        if not any(kind in content_type.lower() for kind in HTML_CONTENT_TYPES):
            return None, response, None

        response.encoding = response.encoding or response.apparent_encoding or "utf-8"
        return response.text, response, None

    def record_result(self, url: str, response: requests.Response | None, error: str | None = None) -> None:
        sources = sorted(self.discovered_sources.get(url, set()))
        if response is None:
            self.checked_results[url] = CheckResult(
                url=url,
                final_url=None,
                status_code=None,
                ok=False,
                error=error,
                content_type=None,
                source_count=len(sources),
                sources=sources,
            )
            return

        self.checked_results[url] = CheckResult(
            url=url,
            final_url=response.url,
            status_code=response.status_code,
            ok=response.status_code < 400,
            error=error,
            content_type=response.headers.get("content-type"),
            source_count=len(sources),
            sources=sources,
        )

    def crawl(self) -> tuple[list[str], int]:
        sitemap_urls = self.collect_sitemap_urls()
        queue = deque(sitemap_urls)
        queued = set(sitemap_urls)
        crawled_html_pages: set[str] = set()
        processed = 0

        for url in sitemap_urls:
            self.add_discovered_url(url, "sitemap")

        self.log(f"[crawl] starting crawl across {len(sitemap_urls)} sitemap URL(s)")

        while queue:
            current_url = queue.popleft()
            processed += 1
            if current_url in crawled_html_pages:
                continue
            if not self.should_crawl_html(current_url):
                continue
            if self.limit_pages is not None and len(crawled_html_pages) >= self.limit_pages:
                self.log(f"[crawl] reached page limit of {self.limit_pages}")
                break

            if processed == 1 or processed % 25 == 0:
                self.log(
                    f"[crawl] processed {processed} queue item(s); "
                    f"crawled {len(crawled_html_pages)} HTML page(s); "
                    f"discovered {len(self.discovered_sources)} URL(s); queue {len(queue)}"
                )

            html, response, error = self.fetch_html(current_url)
            if response is not None:
                self.add_discovered_url(current_url, "crawl")
                self.record_result(current_url, response)
            if error or response is None:
                self.record_result(current_url, response, error)
                crawled_html_pages.add(current_url)
                continue
            if response.status_code >= 400 or html is None:
                crawled_html_pages.add(current_url)
                continue

            self.html_cache[current_url] = html
            extracted_links = self.extract_links_from_html(current_url, html)
            for extracted in extracted_links:
                self.add_discovered_url(extracted, current_url)
                if self.should_crawl_html(extracted) and extracted not in queued and extracted not in crawled_html_pages:
                    queue.append(extracted)
                    queued.add(extracted)
            crawled_html_pages.add(current_url)

            if extracted_links:
                self.log(
                    f"[crawl] {current_url} -> extracted {len(extracted_links)} link(s); "
                    f"total discovered {len(self.discovered_sources)}"
                )

        self.log(
            f"[crawl] completed: crawled {len(crawled_html_pages)} HTML page(s), "
            f"discovered {len(self.discovered_sources)} URL(s)"
        )

        return sorted(self.discovered_sources), len(crawled_html_pages)

    def check_one_url(self, url: str) -> CheckResult:
        cached = self.checked_results.get(url)
        if cached is not None:
            sources = sorted(self.discovered_sources.get(url, set()))
            if cached.sources != sources:
                cached = CheckResult(
                    url=cached.url,
                    final_url=cached.final_url,
                    status_code=cached.status_code,
                    ok=cached.ok,
                    error=cached.error,
                    content_type=cached.content_type,
                    source_count=len(sources),
                    sources=sources,
                )
                self.checked_results[url] = cached
            return cached

        sources = sorted(self.discovered_sources.get(url, set()))
        try:
            response = self.session.get(url, timeout=self.timeout, allow_redirects=True)
            content_type = response.headers.get("content-type")
            ok = response.status_code < 400
            result = CheckResult(
                url=url,
                final_url=response.url,
                status_code=response.status_code,
                ok=ok,
                error=None,
                content_type=content_type,
                source_count=len(sources),
                sources=sources,
            )
            self.checked_results[url] = result
            return result
        except requests.RequestException as exc:
            result = CheckResult(
                url=url,
                final_url=None,
                status_code=None,
                ok=False,
                error=str(exc),
                content_type=None,
                source_count=len(sources),
                sources=sources,
            )
            self.checked_results[url] = result
            return result

    def check_all_urls(self, urls: Iterable[str]) -> list[CheckResult]:
        unique_urls = sorted(set(urls))
        results: list[CheckResult] = []
        completed = 0

        self.log(f"[check] checking {len(unique_urls)} unique URL(s) with {self.max_workers} worker(s)")
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_map = {executor.submit(self.check_one_url, url): url for url in unique_urls}
            for future in as_completed(future_map):
                results.append(future.result())
                completed += 1
                if completed == 1 or completed % 50 == 0 or completed == len(unique_urls):
                    broken_so_far = sum(1 for item in results if not item.ok)
                    self.log(
                        f"[check] completed {completed}/{len(unique_urls)}; "
                        f"broken so far {broken_so_far}"
                    )
        results.sort(key=lambda item: item.url)
        self.checked_results = {result.url: result for result in results}
        self.log("[check] status checks complete")
        return results


def build_markdown_report(
    sitemap_url: str,
    crawled_page_count: int,
    sitemap_url_count: int,
    discovered_url_count: int,
    results: list[CheckResult],
    elapsed_seconds: float,
) -> str:
    broken = [result for result in results if not result.ok]
    redirects = [result for result in results if result.ok and result.final_url and result.final_url.rstrip("/") != result.url.rstrip("/")]
    status_counts = Counter(str(result.status_code) if result.status_code is not None else "error" for result in results)

    lines = [
        "# Site link check report",
        "",
        f"- Sitemap: `{sitemap_url}`",
        f"- Sitemap URLs: **{sitemap_url_count}**",
        f"- Crawled HTML pages: **{crawled_page_count}**",
        f"- Total discovered HTTP(S) URLs: **{discovered_url_count}**",
        f"- Broken URLs: **{len(broken)}**",
        f"- Redirecting URLs: **{len(redirects)}**",
        f"- Elapsed seconds: **{elapsed_seconds:.1f}**",
        "",
        "## Status summary",
        "",
    ]

    for status, count in sorted(status_counts.items()):
        lines.append(f"- `{status}`: {count}")

    lines.extend(["", "## Broken URLs", ""])
    if broken:
        for item in broken:
            status = item.status_code if item.status_code is not None else "error"
            details = item.error or item.content_type or "no additional details"
            lines.append(f"- `{item.url}` — status `{status}` — {details}")
            for source in item.sources[:10]:
                lines.append(f"  - source: `{source}`")
            if len(item.sources) > 10:
                lines.append(f"  - source: and {len(item.sources) - 10} more")
    else:
        lines.append("- No broken HTTP(S) URLs were found.")

    if redirects:
        lines.extend(["", "## Redirecting URLs", ""])
        for item in redirects[:50]:
            lines.append(f"- `{item.url}` → `{item.final_url}` ({item.status_code})")
        if len(redirects) > 50:
            lines.append(f"- ... plus {len(redirects) - 50} more redirecting URLs")

    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sitemap-url", default=DEFAULT_SITEMAP_URL, help="Sitemap URL to crawl")
    parser.add_argument("--output-json", type=Path, default=DEFAULT_JSON_OUTPUT, help="Path to write the JSON report")
    parser.add_argument("--output-markdown", type=Path, default=DEFAULT_MARKDOWN_OUTPUT, help="Path to write the Markdown report")
    parser.add_argument("--timeout", type=float, default=20.0, help="HTTP timeout in seconds per request")
    parser.add_argument("--max-workers", type=int, default=12, help="Max concurrent status checks")
    parser.add_argument("--limit-pages", type=int, default=None, help="Optional max same-site HTML pages to crawl")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    start = time.perf_counter()

    checker = LinkChecker(
        sitemap_url=args.sitemap_url,
        timeout=args.timeout,
        max_workers=args.max_workers,
        limit_pages=args.limit_pages,
    )

    try:
        sitemap_urls = checker.collect_sitemap_urls()
    except requests.RequestException as exc:
        print(f"Failed to load sitemap: {exc}", file=sys.stderr)
        return 1
    except ET.ParseError as exc:
        print(f"Failed to parse sitemap XML: {exc}", file=sys.stderr)
        return 1

    for url in sitemap_urls:
        checker.add_discovered_url(url, "sitemap")

    discovered_urls, crawled_page_count = checker.crawl()
    results = checker.check_all_urls(discovered_urls)
    elapsed = time.perf_counter() - start
    broken = [result for result in results if not result.ok]

    payload = {
        "sitemap_url": args.sitemap_url,
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "elapsed_seconds": round(elapsed, 3),
        "counts": {
            "sitemap_urls": len(sitemap_urls),
            "crawled_html_pages": crawled_page_count,
            "discovered_urls": len(discovered_urls),
            "broken_urls": len(broken),
        },
        "broken_urls": [
            {
                "url": item.url,
                "final_url": item.final_url,
                "status_code": item.status_code,
                "error": item.error,
                "content_type": item.content_type,
                "sources": item.sources,
            }
            for item in broken
        ],
        "all_results": [
            {
                "url": item.url,
                "final_url": item.final_url,
                "status_code": item.status_code,
                "ok": item.ok,
                "error": item.error,
                "content_type": item.content_type,
                "sources": item.sources,
            }
            for item in results
        ],
    }

    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_markdown.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    args.output_markdown.write_text(
        build_markdown_report(
            sitemap_url=args.sitemap_url,
            crawled_page_count=crawled_page_count,
            sitemap_url_count=len(sitemap_urls),
            discovered_url_count=len(discovered_urls),
            results=results,
            elapsed_seconds=elapsed,
        ),
        encoding="utf-8",
    )

    print(f"Sitemap URLs: {len(sitemap_urls)}")
    print(f"Crawled HTML pages: {crawled_page_count}")
    print(f"Discovered URLs: {len(discovered_urls)}")
    print(f"Broken URLs: {len(broken)}")
    print(f"JSON report: {args.output_json}")
    print(f"Markdown report: {args.output_markdown}")

    return 0 if not broken else 2


if __name__ == "__main__":
    raise SystemExit(main())
