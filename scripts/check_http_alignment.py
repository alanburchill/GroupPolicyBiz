#!/usr/bin/env python3
"""HTTP alignment checker for the local static site and https://www.grouppolicy.biz.

This script discovers candidate page routes from the generated local site and the
live production sitemap, then performs real HTTP checks against both endpoints.
It writes a Markdown summary plus a JSON artifact so you can inspect mismatches
and optionally fail a CI or cutover validation step.

Typical usage:

    python scripts/check_http_alignment.py \
        --local-base http://127.0.0.1:8001 \
        --live-base https://www.grouppolicy.biz

For stricter validation:

    python scripts/check_http_alignment.py \
        --local-base http://127.0.0.1:8001 \
        --fail-on-mismatch
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict, deque
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass
from pathlib import Path, PurePosixPath
from typing import Iterable
from urllib.parse import urldefrag, urljoin, urlparse

import requests
from bs4 import BeautifulSoup

NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
DEFAULT_REPO = Path(__file__).resolve().parents[1]
DEFAULT_LOCAL_BASE = "http://127.0.0.1:8001"
DEFAULT_LIVE_BASE = "https://www.grouppolicy.biz"
DEFAULT_LIVE_SITEMAP = "https://www.grouppolicy.biz/sitemap.xml"
DEFAULT_MARKDOWN_REPORT = "docs/http-alignment-report.md"
DEFAULT_JSON_REPORT = "docs/http-alignment-results.json"
PAGE_ASSET_SUFFIXES = {
    ".css",
    ".js",
    ".json",
    ".xml",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".svg",
    ".ico",
    ".woff",
    ".woff2",
    ".ttf",
    ".eot",
    ".pdf",
    ".zip",
    ".txt",
    ".mp4",
    ".mov",
    ".avi",
    ".mp3",
    ".wav",
    ".rss",
}
USER_AGENT = "GroupPolicyBiz HTTP Alignment Checker/1.0"


@dataclass(slots=True)
class CheckResult:
    path: str
    base_name: str
    requested_url: str
    status_code: int | None
    ok: bool
    final_url: str | None
    final_path: str | None
    canonical_url: str | None
    canonical_path: str | None
    meta_refresh_url: str | None
    meta_refresh_path: str | None
    effective_target_path: str | None
    title: str | None
    content_type: str | None
    elapsed_ms: int | None
    error: str | None


@dataclass(slots=True)
class AlignmentRecord:
    path: str
    sources: list[str]
    live: CheckResult
    local: CheckResult
    availability_match: bool
    status_match: bool
    target_match: bool
    aligned: bool
    note: str


def normalize_path(value: str) -> str:
    parsed = urlparse(value)
    path = parsed.path or "/"
    if not path.startswith("/"):
        path = "/" + path
    suffix = PurePosixPath(path).suffix
    if not suffix and not path.endswith("/"):
        path += "/"
    return path


def path_from_url(value: str | None) -> str | None:
    if not value:
        return None
    return normalize_path(value)


def is_probably_page_path(path: str) -> bool:
    suffix = PurePosixPath(path).suffix.lower()
    return not suffix or suffix == ".html"


def is_internal_page_url(base_url: str, candidate_url: str) -> bool:
    base = urlparse(base_url)
    candidate = urlparse(candidate_url)
    if candidate.scheme not in {"http", "https"}:
        return False
    if candidate.netloc != base.netloc:
        return False
    return is_probably_page_path(normalize_path(candidate_url))


def attr_value_to_string(value: object) -> str | None:
    if isinstance(value, str):
        return value
    if isinstance(value, (list, tuple)):
        parts = [item for item in value if isinstance(item, str) and item.strip()]
        if parts:
            return " ".join(parts)
    return None


def fetch_xml(url: str, timeout: float) -> bytes:
    response = requests.get(url, timeout=timeout, headers={"User-Agent": USER_AGENT})
    response.raise_for_status()
    return response.content


def parse_locs(xml_bytes: bytes) -> list[str]:
    root = ET.fromstring(xml_bytes)
    root_name = root.tag.rsplit("}", 1)[-1]
    if root_name == "sitemapindex":
        return [node.text.strip() for node in root.findall(".//sm:sitemap/sm:loc", NS) if node.text]
    if root_name == "urlset":
        return [node.text.strip() for node in root.findall(".//sm:url/sm:loc", NS) if node.text]
    return []


def fetch_live_sitemap_paths(index_url: str, timeout: float) -> list[str]:
    live_index_children = parse_locs(fetch_xml(index_url, timeout))
    live_page_sitemaps = sorted(url for url in live_index_children if "image-sitemap" not in url)

    live_urls: list[str] = []
    for sitemap_url in live_page_sitemaps:
        live_urls.extend(parse_locs(fetch_xml(sitemap_url, timeout)))

    return sorted({normalize_path(url) for url in live_urls})


def collect_local_rendered_paths(root: Path) -> list[str]:
    paths: set[str] = set()

    for index_file in root.rglob("index.html"):
        rel = index_file.relative_to(root)
        if rel.parts == ("index.html",):
            paths.add("/")
            continue

        route = "/" + "/".join(rel.parts[:-1]) + "/"
        paths.add(route)

    return sorted(paths)


def collect_local_sitemap_paths(local_sitemap: Path) -> list[str]:
    if not local_sitemap.exists():
        return []
    return sorted({normalize_path(url) for url in parse_locs(local_sitemap.read_bytes())})


def derive_intermediate_compatibility_paths(paths: Iterable[str]) -> list[str]:
    derived: set[str] = set()

    for path in paths:
        legacy_post = re.fullmatch(r"/(\d{4})/(\d{2})/[^/]+/", path)
        if not legacy_post:
            continue

        year = legacy_post.group(1)
        month = legacy_post.group(2)
        derived.add(f"/{year}/")
        derived.add(f"/{year}/{month}/")

    return sorted(derived)


def crawl_internal_paths(base_url: str, timeout: float, max_pages: int) -> list[str]:
    discovered: set[str] = {"/"}
    visited: set[str] = set()
    queue: deque[str] = deque(["/"])

    while queue and len(visited) < max_pages:
        path = queue.popleft()
        if path in visited:
            continue
        visited.add(path)

        try:
            response = requests.get(
                urljoin(base_url, path),
                timeout=timeout,
                allow_redirects=True,
                headers={"User-Agent": USER_AGENT},
            )
            response.raise_for_status()
        except requests.RequestException:
            continue

        content_type = response.headers.get("Content-Type", "")
        if "html" not in content_type.lower():
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        for tag in soup.select("a[href], link[href]"):
            href = attr_value_to_string(tag.get("href"))
            if not href:
                continue

            href, _fragment = urldefrag(href)
            if not href or href.startswith(("mailto:", "tel:", "javascript:")):
                continue

            absolute = urljoin(response.url, href)
            if not is_internal_page_url(base_url, absolute):
                continue

            candidate_path = normalize_path(absolute)
            if candidate_path not in discovered:
                discovered.add(candidate_path)
                queue.append(candidate_path)

    return sorted(discovered)


def parse_meta_refresh_url(content_value: str | None) -> str | None:
    if not content_value:
        return None
    match = re.search(r"url\s*=\s*(.+)$", content_value, re.IGNORECASE)
    if not match:
        return None
    return match.group(1).strip().strip("'\"")


def fetch_check(base_name: str, base_url: str, path: str, timeout: float) -> CheckResult:
    requested_url = urljoin(base_url.rstrip("/") + "/", path.lstrip("/"))

    try:
        response = requests.get(
            requested_url,
            timeout=timeout,
            allow_redirects=True,
            headers={"User-Agent": USER_AGENT},
        )
    except requests.RequestException as exc:
        return CheckResult(
            path=path,
            base_name=base_name,
            requested_url=requested_url,
            status_code=None,
            ok=False,
            final_url=None,
            final_path=None,
            canonical_url=None,
            canonical_path=None,
            meta_refresh_url=None,
            meta_refresh_path=None,
            effective_target_path=None,
            title=None,
            content_type=None,
            elapsed_ms=None,
            error=str(exc),
        )

    content_type = response.headers.get("Content-Type", "")
    canonical_url = None
    canonical_path = None
    meta_refresh_url = None
    meta_refresh_path = None
    title = None

    if "html" in content_type.lower():
        soup = BeautifulSoup(response.text, "html.parser")
        if soup.title and soup.title.string:
            title = soup.title.string.strip()

        for candidate_tag in soup.find_all("link"):
            rel_value = attr_value_to_string(candidate_tag.get("rel"))
            if not rel_value or "canonical" not in rel_value.lower():
                continue

            canonical_href = attr_value_to_string(candidate_tag.get("href"))
            if canonical_href:
                canonical_url = urljoin(response.url, canonical_href)
                canonical_path = path_from_url(canonical_url)
                break

        refresh_tag = None
        for candidate_tag in soup.find_all("meta"):
            http_equiv = attr_value_to_string(candidate_tag.get("http-equiv"))
            if http_equiv and http_equiv.lower() == "refresh":
                refresh_tag = candidate_tag
                break

        if refresh_tag:
            refresh_target = parse_meta_refresh_url(attr_value_to_string(refresh_tag.get("content")))
            if refresh_target:
                meta_refresh_url = urljoin(response.url, refresh_target)
                meta_refresh_path = path_from_url(meta_refresh_url)

    final_url = response.url
    final_path = path_from_url(final_url)
    effective_target_path = meta_refresh_path or final_path or canonical_path or path

    return CheckResult(
        path=path,
        base_name=base_name,
        requested_url=requested_url,
        status_code=response.status_code,
        ok=response.ok,
        final_url=final_url,
        final_path=final_path,
        canonical_url=canonical_url,
        canonical_path=canonical_path,
        meta_refresh_url=meta_refresh_url,
        meta_refresh_path=meta_refresh_path,
        effective_target_path=effective_target_path,
        title=title,
        content_type=content_type,
        elapsed_ms=int(response.elapsed.total_seconds() * 1000),
        error=None,
    )


def classify_note(live: CheckResult, local: CheckResult) -> tuple[bool, bool, bool, bool, str]:
    availability_match = live.ok == local.ok
    status_match = live.status_code == local.status_code
    target_match = live.effective_target_path == local.effective_target_path

    if live.error or local.error:
        aligned = False
        return availability_match, status_match, target_match, aligned, "Request error"

    if live.ok and not local.ok:
        aligned = False
        return availability_match, status_match, target_match, aligned, "Live route is available but local route failed"

    if local.ok and not live.ok:
        aligned = False
        return availability_match, status_match, target_match, aligned, "Local route is available but live route failed"

    if not live.ok and not local.ok:
        aligned = status_match
        note = "Both endpoints failed with the same HTTP status" if aligned else "Both endpoints failed, but with different HTTP status codes"
        return availability_match, status_match, target_match, aligned, note

    if not status_match:
        aligned = False
        return availability_match, status_match, target_match, aligned, "Both routes responded, but the HTTP status codes differ"

    if not target_match:
        aligned = False
        return availability_match, status_match, target_match, aligned, "Both routes responded, but the effective target paths differ"

    return availability_match, status_match, target_match, True, "Aligned"


def markdown_row(record: AlignmentRecord) -> str:
    source_text = ", ".join(record.sources)
    live_target = record.live.effective_target_path or "-"
    local_target = record.local.effective_target_path or "-"
    live_status = str(record.live.status_code) if record.live.status_code is not None else "ERR"
    local_status = str(record.local.status_code) if record.local.status_code is not None else "ERR"
    return f"| `{record.path}` | `{source_text}` | `{live_status}` | `{local_status}` | `{live_target}` | `{local_target}` | {record.note} |"


def write_reports(records: list[AlignmentRecord], path_sources: dict[str, set[str]], markdown_path: Path, json_path: Path) -> None:
    total = len(records)
    aligned = sum(1 for record in records if record.aligned)
    mismatched = total - aligned
    live_only_success = sum(1 for record in records if record.live.ok and not record.local.ok)
    local_only_success = sum(1 for record in records if record.local.ok and not record.live.ok)
    target_mismatches = sum(1 for record in records if record.live.ok and record.local.ok and not record.target_match)
    request_errors = sum(1 for record in records if record.live.error or record.local.error)

    source_counts = Counter(source for sources in path_sources.values() for source in sources)
    mismatches = [record for record in records if not record.aligned]

    markdown_lines = [
        "# HTTP alignment report",
        "",
        "This report compares real HTTP responses for the discovered route set on the local preview server and `https://www.grouppolicy.biz`.",
        "",
        "## Summary",
        "",
        f"- Total checked paths: {total}",
        f"- Fully aligned paths: {aligned}",
        f"- Mismatched paths: {mismatched}",
        f"- Live available, local unavailable: {live_only_success}",
        f"- Local available, live unavailable: {local_only_success}",
        f"- Effective target mismatches: {target_mismatches}",
        f"- Request errors: {request_errors}",
        "",
        "## Discovery sources",
        "",
    ]

    for source_name, count in sorted(source_counts.items()):
        markdown_lines.append(f"- {source_name}: {count}")

    markdown_lines.extend([
        "",
        "## Mismatches",
        "",
    ])

    if mismatches:
        markdown_lines.extend([
            "| Path | Sources | Live | Local | Live target | Local target | Note |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ])
        markdown_lines.extend(markdown_row(record) for record in mismatches)
    else:
        markdown_lines.append("- None. Every checked path currently aligns across local and live.")

    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.write_text("\n".join(markdown_lines) + "\n", encoding="utf-8")

    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_payload = {
        "summary": {
            "total_paths": total,
            "aligned_paths": aligned,
            "mismatched_paths": mismatched,
            "live_available_local_unavailable": live_only_success,
            "local_available_live_unavailable": local_only_success,
            "target_mismatches": target_mismatches,
            "request_errors": request_errors,
        },
        "source_counts": dict(sorted(source_counts.items())),
        "records": [
            {
                "path": record.path,
                "sources": record.sources,
                "availability_match": record.availability_match,
                "status_match": record.status_match,
                "target_match": record.target_match,
                "aligned": record.aligned,
                "note": record.note,
                "live": asdict(record.live),
                "local": asdict(record.local),
            }
            for record in records
        ],
    }
    json_path.write_text(json.dumps(json_payload, indent=2), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compare local and live HTTP route alignment.")
    parser.add_argument("--repo-root", default=str(DEFAULT_REPO), help="Repository root. Defaults to the current repo.")
    parser.add_argument("--local-base", default=DEFAULT_LOCAL_BASE, help="Base URL for the locally served site.")
    parser.add_argument("--live-base", default=DEFAULT_LIVE_BASE, help="Base URL for the live site.")
    parser.add_argument("--live-sitemap", default=DEFAULT_LIVE_SITEMAP, help="Live sitemap index URL.")
    parser.add_argument("--local-sitemap", default="_site_local/sitemap.xml", help="Local sitemap path relative to the repo root.")
    parser.add_argument("--local-output", default="_site_local", help="Local generated site directory relative to the repo root.")
    parser.add_argument("--markdown-report", default=DEFAULT_MARKDOWN_REPORT, help="Markdown report path relative to the repo root.")
    parser.add_argument("--json-report", default=DEFAULT_JSON_REPORT, help="JSON report path relative to the repo root.")
    parser.add_argument("--timeout", type=float, default=15.0, help="HTTP timeout in seconds.")
    parser.add_argument("--workers", type=int, default=12, help="Concurrent HTTP workers.")
    parser.add_argument("--crawl-live", action="store_true", help="Crawl the live site over HTTP and add discovered internal page routes.")
    parser.add_argument("--crawl-local", action="store_true", help="Crawl the local site over HTTP and add discovered internal page routes.")
    parser.add_argument("--max-crawl-pages", type=int, default=5000, help="Maximum pages to crawl per site when crawl flags are enabled.")
    parser.add_argument("--fail-on-mismatch", action="store_true", help="Exit with code 1 if any route is not fully aligned.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()
    local_output = repo_root / args.local_output
    local_sitemap = repo_root / args.local_sitemap
    markdown_report = repo_root / args.markdown_report
    json_report = repo_root / args.json_report

    if not local_output.exists():
        print(f"Local output directory does not exist: {local_output}", file=sys.stderr)
        return 2

    path_sources: dict[str, set[str]] = defaultdict(set)

    local_rendered_paths = collect_local_rendered_paths(local_output)
    for path in local_rendered_paths:
        path_sources[path].add("local_rendered")

    local_sitemap_paths = collect_local_sitemap_paths(local_sitemap)
    for path in local_sitemap_paths:
        path_sources[path].add("local_sitemap")

    live_sitemap_paths = fetch_live_sitemap_paths(args.live_sitemap, args.timeout)
    for path in live_sitemap_paths:
        path_sources[path].add("live_sitemap")

    derived_paths = derive_intermediate_compatibility_paths(live_sitemap_paths)
    for path in derived_paths:
        path_sources[path].add("derived_intermediate")

    if args.crawl_live:
        for path in crawl_internal_paths(args.live_base, args.timeout, args.max_crawl_pages):
            path_sources[path].add("live_crawl")

    if args.crawl_local:
        for path in crawl_internal_paths(args.local_base, args.timeout, args.max_crawl_pages):
            path_sources[path].add("local_crawl")

    candidate_paths = sorted(path_sources)
    records_by_path: dict[str, dict[str, CheckResult]] = {path: {} for path in candidate_paths}

    checks: list[tuple[str, str, str]] = []
    for path in candidate_paths:
        checks.append(("live", args.live_base, path))
        checks.append(("local", args.local_base, path))

    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        future_map = {
            executor.submit(fetch_check, base_name, base_url, path, args.timeout): (base_name, path)
            for base_name, base_url, path in checks
        }
        for future in as_completed(future_map):
            base_name, path = future_map[future]
            result = future.result()
            records_by_path[path][base_name] = result

    alignment_records: list[AlignmentRecord] = []
    for path in candidate_paths:
        live = records_by_path[path]["live"]
        local = records_by_path[path]["local"]
        availability_match, status_match, target_match, aligned, note = classify_note(live, local)
        alignment_records.append(
            AlignmentRecord(
                path=path,
                sources=sorted(path_sources[path]),
                live=live,
                local=local,
                availability_match=availability_match,
                status_match=status_match,
                target_match=target_match,
                aligned=aligned,
                note=note,
            )
        )

    write_reports(alignment_records, path_sources, markdown_report, json_report)

    total = len(alignment_records)
    mismatches = sum(1 for record in alignment_records if not record.aligned)
    print(f"Checked paths: {total}")
    print(f"Aligned paths: {total - mismatches}")
    print(f"Mismatched paths: {mismatches}")
    print(f"Markdown report: {markdown_report}")
    print(f"JSON report: {json_report}")

    if args.fail_on_mismatch and mismatches:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
