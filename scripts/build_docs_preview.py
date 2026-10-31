#!/usr/bin/env python3
"""Build an isolated documentation-style preview from the Markdown archive.

The existing generator remains responsible for conversion and legacy routes.
Never point --output at a production build or the baseline preview.
"""
import argparse
import subprocess
import sys
import json
from pathlib import Path
from urllib.parse import urlsplit
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--site-url', default='http://127.0.0.1:8002',
                        help='Origin for canonical URLs and sitemap')
    args = parser.parse_args()
    origin = urlsplit(args.site_url)
    if origin.scheme not in ('http', 'https') or not origin.netloc or origin.path not in ('', '/') or origin.query or origin.fragment:
        parser.error('--site-url must be an HTTP(S) origin without a path, query or fragment')
    output = args.output.resolve()
    if output.exists() and any(output.iterdir()):
        parser.error('Output must be an empty directory')
    output.mkdir(parents=True, exist_ok=True)
    subprocess.run([sys.executable, str(ROOT / 'scripts/generate_from_markdown.py'),
                    '--content', str(ROOT / 'content/posts'), '--output', str(output),
                    '--base-path', '/', '--site-url', args.site_url.rstrip('/')],
                   cwd=ROOT, check=True)
    source_count = len(list((ROOT / 'content/posts').rglob('*.md')))
    index = json.loads((output / 'search-index.json').read_text(encoding='utf-8'))
    if len(index) != source_count:
        raise RuntimeError(f'Generated {len(index)} posts from {source_count} Markdown files')
    urls = [post['url'] for post in index]
    if len(set(urls)) != len(urls):
        raise RuntimeError('Duplicate post URLs in generated search index')
    for post in index:
        if not (output / post['url'].lstrip('/') / 'index.html').is_file():
            raise RuntimeError(f'Missing generated post: {post["url"]}')
    # This deployment is an isolated staging site, not a DNS cutover.
    (output / '_headers').write_text('/*\n  X-Robots-Tag: noindex, nofollow\n', encoding='utf-8')
    (output / 'docs.css').write_text((ROOT / 'static/docs.css').read_text(encoding='utf-8'), encoding='utf-8')
    (output / 'docs.js').write_text((ROOT / 'static/docs.js').read_text(encoding='utf-8'), encoding='utf-8')
    count = 0
    for path in output.rglob('*.html'):
        soup = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')
        main = soup.select_one('.main-container')
        if not main or not soup.head or not soup.body:
            continue  # Preserve redirects and special pages exactly.
        for tag in soup.select('script[src*="googletagmanager"], script'):
            if 'googletagmanager' in str(tag) or 'gtag(' in tag.get_text():
                tag.decompose()
        style = soup.new_tag('link', rel='stylesheet', href='/docs.css')
        soup.head.append(style)
        meta = soup.new_tag('meta', attrs={'name': 'robots', 'content': 'noindex, nofollow'})
        soup.head.append(meta)
        top = soup.select_one('.topbar')
        nav = soup.select_one('.main-nav')
        secondary = soup.select_one('.secondary-nav')
        for element in (top, nav, secondary):
            if element:
                element.decompose()
        shell = BeautifulSoup('''<header class="docs-header"><a class="docs-brand" href="/">Group Policy <span>Central</span></a><span class="header-divider"></span><span class="header-label">Documentation</span><button class="menu-toggle" aria-expanded="false" aria-controls="docs-sidebar">☰ <span>Browse</span></button><a class="header-github" href="https://github.com/alanburchill/GroupPolicyBiz">GitHub ↗</a></header><div class="docs-layout"><aside id="docs-sidebar" class="docs-sidebar"><div class="sidebar-heading">GROUP POLICY CENTRAL</div><label class="sidebar-search" for="site-search">Search the archive</label><input id="site-search" placeholder="Search articles..." autocomplete="off"><nav aria-label="Documentation navigation"><div class="nav-label">EXPLORE</div><a href="/">Overview</a><a href="/news/">News</a><a href="/best-practices/">Best practices</a><a href="/tutorials/">Tutorials</a><a href="/setting-of-the-week/">Setting of the week</a><div class="nav-label">LIBRARY</div><a href="/archives/">Browse all archives</a><a href="/group-policy-preferences/">Group Policy Preferences</a><a href="/teched/">TechEd</a><div class="nav-label">ABOUT</div><a href="/about/">About this archive</a></nav><p class="sidebar-note">Independent guides and historical resources for Windows administrators.</p></aside><main id="main-content" class="docs-main"></main><aside class="docs-toc" aria-label="On this page"><div>IN THIS ARTICLE</div><nav></nav></aside></div>''', 'html.parser')
        # Give archive search space in the header while keeping its accessible label.
        search_box = shell.new_tag('div', attrs={'class': 'docs-search-box', 'role': 'search'})
        search_label = shell.select_one('label[for="site-search"]')
        search_label['class'] = ['visually-hidden']
        search_box.append(search_label.extract())
        search_box.append(shell.select_one('#site-search').extract())
        shell.select_one('.header-github').insert_before(search_box)
        skip = soup.new_tag('a', href='#main-content', attrs={'class': 'skip-link'})
        skip.string = 'Skip to main content'
        soup.body.insert(0, skip)
        theme_button = shell.new_tag('button', attrs={'class': 'docs-theme-toggle', 'type': 'button', 'aria-label': 'Switch colour theme'})
        theme_button.string = 'Dark theme'
        shell.select_one('.header-github').insert_before(theme_button)
        main.replace_with(shell)
        target = soup.select_one('.docs-main')
        target['tabindex'] = '-1'
        main.attrs['class'] = ['docs-content']
        target.append(main)
        for thumbnail in main.select('.post-card img.thumb:not([alt])'):
            thumbnail['alt'] = ''  # The adjacent article title names this link.
        if main.select_one('.post-full header h1'):
            for heading in main.select('.post-content h1'):
                heading.name = 'h2'
        crumb = soup.new_tag('div', attrs={'class':'breadcrumbs'})
        crumb.append(BeautifulSoup('<a href="/">Group Policy Central</a> <span>/</span> <span>Archive</span>', 'html.parser'))
        target.insert(0, crumb)
        if path == output / 'index.html':
            notice = soup.select_one('.archive-notice')
            # Replace the old promotional banner with a compact editorial introduction.
            if notice:
                notice.decompose()
            intro = BeautifulSoup('''<section class="docs-hero"><div class="eyebrow">THE GROUP POLICY ARCHIVE</div><h1>Practical guidance for<br>Group Policy administrators.</h1><p>Explore tutorials, best practices and field notes from the Group Policy Central archive.</p><div class="hero-actions"><a class="primary-action" href="/tutorials/">Explore tutorials <span>→</span></a><a href="/archives/">Browse the archive →</a></div></section><section class="quick-links" aria-label="Explore topics"><a href="/best-practices/"><span>01 / GUIDANCE</span><strong>Best practices →</strong><small>Design and manage policies with confidence.</small></a><a href="/tutorials/"><span>02 / HOW TO</span><strong>Step-by-step tutorials →</strong><small>Practical walkthroughs for everyday tasks.</small></a><a href="/archives/"><span>03 / ARCHIVE</span><strong>Browse by year →</strong><small>Explore the complete historical collection.</small></a></section><div class="section-kicker">FROM THE ARCHIVE</div>''', 'html.parser')
            main.insert(0, intro)
            for heading in main.select(':scope > h1'):
                heading.name = 'h2'
        toc = soup.select_one('.docs-toc nav')
        headings = main.select('.post-content h2, .post-content h3')
        used_ids = {tag['id'] for tag in soup.select('[id]')}
        for index, heading in enumerate(headings):
            if not heading.get('id'):
                candidate = f'section-{index + 1}'
                while candidate in used_ids:
                    candidate += '-heading'
                heading['id'] = candidate
                used_ids.add(candidate)
            link = soup.new_tag('a', href='#' + heading['id'])
            link.string = heading.get_text(' ', strip=True)
            if heading.name == 'h3': link['class'] = 'toc-sub'
            toc.append(link)
        if not headings:
            soup.select_one('.docs-toc').decompose()
        script = soup.new_tag('script', src='/docs.js', defer=True)
        soup.body.append(script)
        path.write_text(str(soup), encoding='utf-8')
        count += 1
    print(f'Documentation preview styled {count} pages in {output}; redirects preserved.')

if __name__ == '__main__':
    main()
