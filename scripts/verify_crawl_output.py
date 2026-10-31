#!/usr/bin/env python3
"""Validate crawler-facing output for a documentation staging or production build."""
import argparse
import json
from pathlib import Path
from urllib.parse import urlsplit
from xml.etree import ElementTree

from bs4 import BeautifulSoup


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('output', type=Path)
    parser.add_argument('--origin', required=True)
    parser.add_argument('--production', action='store_true')
    args = parser.parse_args()
    root, origin = args.output, args.origin.rstrip('/')
    robots = (root / 'robots.txt').read_text(encoding='utf-8')
    if 'User-agent: *' not in robots or 'Allow: /' not in robots or f'Sitemap: {origin}/sitemap.xml' not in robots:
        raise SystemExit('robots.txt does not advertise this origin and allow crawlers')
    if not (root / '404.html').is_file():
        raise SystemExit('Missing top-level 404.html')
    headers = root / '_headers'
    header_noindex = headers.exists() and 'noindex' in headers.read_text(encoding='utf-8').lower()
    if header_noindex == args.production:
        raise SystemExit('Unexpected staging/production indexing header')
    entries = [el.text for el in ElementTree.parse(root / 'sitemap.xml').iter() if el.tag.endswith('}loc')]
    posts = json.loads((root / 'search-index.json').read_text(encoding='utf-8'))
    if len(entries) < len(posts) or len(set(entries)) != len(entries):
        raise SystemExit('Sitemap is incomplete or contains duplicate URLs')
    for entry in entries:
        parsed = urlsplit(entry)
        if not entry.startswith(origin + '/') or parsed.query or parsed.fragment:
            raise SystemExit(f'Invalid sitemap origin: {entry}')
        path = root / parsed.path.lstrip('/') / 'index.html'
        if not path.is_file():
            raise SystemExit(f'Missing sitemap page: {entry}')
        soup = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')
        canonical = soup.select_one('link[rel="canonical"]')
        if not canonical or canonical.get('href') != entry:
            raise SystemExit(f'Sitemap and canonical disagree: {entry}')
        if not soup.select_one('main'):
            raise SystemExit(f'Missing article content: {entry}')
        meta_noindex = any('noindex' in tag.get('content', '').lower() for tag in soup.select('meta[name="robots"]'))
        if meta_noindex == args.production:
            raise SystemExit(f'Unexpected staging/production robots meta: {entry}')
    print(f'Validated {len(entries)} sitemap pages and {len(posts)} posts for {origin}.')


if __name__ == '__main__':
    main()
