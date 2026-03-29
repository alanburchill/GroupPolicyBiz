#!/usr/bin/env python3
"""Generate static HTML site from Markdown files.

Usage: python scripts/generate_from_markdown.py --content content/posts --output _site --per-page 12

The content directory may contain Markdown files directly or nested beneath date folders
such as content/posts/YYYY/MM/*.md.
"""
import argparse
import re
import json
import os
import shutil
from pathlib import Path
from datetime import datetime, timedelta
import markdown
from collections import defaultdict

# Import shared functions from the WordPress generator
import sys
sys.path.insert(0, str(Path(__file__).parent))

def load_env_file(env_path):
  """Load simple KEY=VALUE pairs from a .env file without overriding existing env vars."""
  if not env_path.exists():
    return

  for raw_line in env_path.read_text(encoding='utf-8').splitlines():
    line = raw_line.strip()
    if not line or line.startswith('#') or '=' not in line:
      continue

    key, value = line.split('=', 1)
    key = key.strip()
    value = value.strip().strip('"').strip("'")

    if key and key not in os.environ:
      os.environ[key] = value

def normalize_base_path(base_path):
  """Normalize base path to begin and end with a slash."""
  base = (base_path or '/').strip()
  if not base:
    return '/'
  if not base.startswith('/'):
    base = '/' + base
  if not base.endswith('/'):
    base = base + '/'
  return base

def parse_front_matter(content):
    """Parse YAML front matter from Markdown content."""
    if not content.startswith('---'):
        return {}, content
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}, content
    
    front_matter_text = parts[1].strip()
    body = parts[2].strip()
    
    # Simple YAML parser for our specific format
    metadata = {}
    for line in front_matter_text.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            
            # Handle lists [item1, item2]
            if value.startswith('[') and value.endswith(']'):
                items = value[1:-1].split(',')
                items = [item.strip().strip('"').strip("'") for item in items if item.strip()]
                metadata[key] = items
            else:
                # Remove quotes
                value = value.strip('"').strip("'")
                metadata[key] = value
    
    return metadata, body

def markdown_to_html(md_content):
    """Convert Markdown to HTML."""
    md = markdown.Markdown(extensions=['extra', 'codehilite', 'tables', 'fenced_code'])
    return md.convert(md_content)

def generate_nav_html(url_func):
    """Generate navigation HTML.
    
    Args:
        url_func: Function to prepend base path to URLs
    """
    return f'''
    <nav class="main-nav">
      <div class="container">
        <div class="nav-item"><a href="{url_func('/')}">HOME</a></div>
        <div class="nav-item"><a href="{url_func('/news/')}">NEWS</a></div>
        <div class="nav-item"><a href="{url_func('/best-practices/')}">BEST PRACTICES</a></div>
        <div class="nav-item"><a href="{url_func('/tutorials/')}">TUTORIALS</a></div>
        <div class="nav-item"><a href="{url_func('/archives/')}">ARCHIVES</a></div>
        <div class="nav-item"><a href="{url_func('/about/')}">ABOUT</a></div>
      </div>
    </nav>
    <div class="secondary-nav">
      <div class="container">
        <div class="search-box">
          <input type="text" id="site-search" placeholder="Search posts..." aria-label="Search">
        </div>
      </div>
    </div>
    '''

def generate_pagination_html(current_page, total_pages, base_url, url_func):
    """Generate pagination HTML (WordPress-style).
    
    Args:
        current_page: Current page number
        total_pages: Total number of pages
        base_url: Base URL for pagination (e.g., '/page/')
        url_func: Function to prepend base path to URLs
    """
    if total_pages <= 1:
        return ''
    
    links = []
    
    # Previous link
    if current_page > 1:
        prev_url = url_func('/') if current_page == 2 else url_func(f'{base_url}{current_page - 1}/')
        links.append(f'<a href="{prev_url}" class="page-link prev">← Previous</a>')
    
    # Page numbers with ellipsis
    for i in range(1, total_pages + 1):
        if i == 1 or i == total_pages or (i >= current_page - 2 and i <= current_page + 2):
            page_url = url_func('/') if i == 1 else url_func(f'{base_url}{i}/')
            active = ' active' if i == current_page else ''
            links.append(f'<a href="{page_url}" class="page-number{active}">{i}</a>')
        elif i == current_page - 3 or i == current_page + 3:
            links.append('<span class="page-ellipsis">...</span>')
    
    # Next link
    if current_page < total_pages:
        next_url = url_func(f'{base_url}{current_page + 1}/')
        links.append(f'<a href="{next_url}" class="page-link next">Next →</a>')
    
    return f'<div class="pagination">{"".join(links)}</div>'


def write_redirect_page(target_url, title):
    """Create a simple HTML redirect page to preserve legacy routes."""
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="0; url={target_url}">
  <link rel="canonical" href="{target_url}">
  <title>Redirecting to {title}</title>
  <style>
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      margin: 0;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: white;
    }}
    .container {{
      text-align: center;
      padding: 2rem;
    }}
    a {{
      color: white;
      text-decoration: underline;
    }}
  </style>
</head>
<body>
  <div class="container">
    <h1>Redirecting...</h1>
    <p>If you are not redirected automatically, <a href="{target_url}">click here</a>.</p>
  </div>
</body>
</html>'''


def write_post_page(post_dir, post_html):
    """Write a generated post HTML page to its target directory."""
    (post_dir / 'index.html').write_text(post_html, encoding='utf-8')


def collect_markdown_files(content_dir: Path) -> list[Path]:
  """Collect Markdown files recursively so flat and YYYY/MM layouts both work."""
  return sorted(content_dir.rglob('*.md'), reverse=True)


def markdown_source_repo_path(md_file: Path) -> str:
  """Return a repository-relative path suitable for GitHub source links."""
  if not md_file.is_absolute():
    return md_file.as_posix()

  try:
    return md_file.resolve().relative_to(Path.cwd().resolve()).as_posix()
  except ValueError:
    return md_file.name

def main():
    parser = argparse.ArgumentParser(description='Generate static site from Markdown files')
    parser.add_argument('--content', default='content/posts', help='Directory containing Markdown files (supports nested YYYY/MM/*.md layouts)')
    parser.add_argument('--output', default='_site', help='Output directory for generated site')
    parser.add_argument('--per-page', type=int, default=12, help='Posts per page')
    parser.add_argument('--base-path', default=None, help='Base path for deployment (e.g., "/" or "/GroupPolicyBiz/"). Defaults to SITE_BASE_PATH or "/".')
    parser.add_argument('--site-url', default=None, help='Canonical site URL (e.g., "https://alanburchill.github.io" or "https://www.grouppolicy.biz"). Defaults to SITE_URL if set.')
    parser.add_argument('--ga-id', default='', help='Google Analytics tracking ID (e.g., G-XXXXXXXXXX or UA-XXXXXXXXX-X)')
    args = parser.parse_args()

    load_env_file(Path('.env'))

    configured_base_path = normalize_base_path(args.base_path or os.environ.get('SITE_BASE_PATH', '/'))
    configured_site_url = (args.site_url or os.environ.get('SITE_URL', '')).strip().rstrip('/')
    
    # Helper function to prepend base path to URLs
    def url(path):
        """Prepend base path to a given path, handling slashes correctly.
        
        Args:
            path: The path to prepend base_path to (e.g., '/posts/', '/styles.css')
        
        Returns:
            The full path with base_path prepended.
        
        Examples:
            url('/posts/') with base_path='/' -> '/posts/'
            url('/posts/') with base_path='/GroupPolicyBiz/' -> '/GroupPolicyBiz/posts/'
        """
        base = configured_base_path
        
        # Normalize path: ensure it starts with /
        if not path.startswith('/'):
            path = '/' + path
        
        # If base_path is just '/', return path as-is
        if base == '/':
            return path
        
        # Remove leading slash from path since base already ends with /
        path = path.lstrip('/')
        
        return base + path

    def absolute_url(path):
        """Return absolute site URL when configured, otherwise return the path."""
        relative_path = url(path)
        if not configured_site_url:
            return relative_path
        return f'{configured_site_url}{relative_path}'

    def canonical_post_path(year, month, slug):
      """Return the canonical post path, matching the legacy live permalink shape when possible."""
      if year and month:
        return f'/{year}/{month}/{slug}/'
      return f'/posts/{slug}/'

    def resolve_post_permalink_date(metadata_date, fallback_year, fallback_month):
      """Resolve the permalink year/month using the historical local publish time used on the live site."""
      if metadata_date:
        try:
          local_publish_time = datetime.fromisoformat(metadata_date) + timedelta(hours=10)
          return f'{local_publish_time.year:04d}', f'{local_publish_time.month:02d}'
        except ValueError:
          pass

      return fallback_year, fallback_month
    
    # Generate Google Analytics tracking code
    def ga_tracking_script():
        """Generate Google Analytics tracking script if GA ID is provided."""
        if not args.ga_id:
            return ''
        
        # Detect if it's GA4 (G-) or Universal Analytics (UA-)
        if args.ga_id.startswith('G-'):
            # Google Analytics 4 (GA4)
            return f'''<!-- Google Analytics 4 -->
  <script async src="https://www.googletagmanager.com/gtag/js?id={args.ga_id}"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', '{args.ga_id}');
  </script>'''
        elif args.ga_id.startswith('UA-'):
            # Universal Analytics (legacy)
            return f'''<!-- Google Analytics -->
  <script async src="https://www.googletagmanager.com/analytics.js"></script>
  <script>
    window.ga=window.ga||function(){{(ga.q=ga.q||[]).push(arguments)}};ga.l=+new Date;
    ga('create', '{args.ga_id}', 'auto');
    ga('send', 'pageview');
  </script>'''
        else:
            return ''

    site_config_json = json.dumps({
        'basePath': configured_base_path,
        'siteUrl': configured_site_url,
    })
    head_extras_html = f'<script>window.__SITE_CONFIG__ = {site_config_json};</script>'
    ga_script_html = ga_tracking_script()
    if ga_script_html:
        head_extras_html += f'\n  {ga_script_html}'
    
    content_dir = Path(args.content)
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    for obsolete_dir_name in ['categories', 'tags']:
      obsolete_dir = output_dir / obsolete_dir_name
      if obsolete_dir.exists():
        shutil.rmtree(obsolete_dir)
    
    # Base URL for GitHub repository (used to point to source markdown files)
    repo_base = 'https://github.com/alanburchill/GroupPolicyBiz/blob/main'

    # Output subfolders
    posts_out = output_dir / 'posts'
    cat_out = output_dir / 'category'
    tag_out = output_dir / 'tag'

    print(f'Reading Markdown files recursively from {content_dir}...')
    
    # Read all Markdown files
    posts = []
    md_files = collect_markdown_files(content_dir)
    
    for md_file in md_files:
        try:
            content = md_file.read_text(encoding='utf-8')
            metadata, body = parse_front_matter(content)
            
            if not metadata.get('title'):
                continue
            
            # Replace old WordPress image URLs with local paths
            body = body.replace('http://www.grouppolicy.biz/wp-content/uploads/', '/uploads/')
            body = body.replace('https://www.grouppolicy.biz/wp-content/uploads/', '/uploads/')
            
            # Extract featured image from metadata or first image in body
            featured_img = metadata.get('featured_image')
            if featured_img:
                # Update featured image URL if it's from old site
                featured_img = featured_img.replace('http://www.grouppolicy.biz/wp-content/uploads/', '/uploads/')
                featured_img = featured_img.replace('https://www.grouppolicy.biz/wp-content/uploads/', '/uploads/')
            else:
                # Try to extract first image from body
                import re
                img_match = re.search(r'!\[.*?\]\((.*?)\)', body)
                if img_match:
                    featured_img = img_match.group(1)
            
            # Convert markdown to HTML
            html_content = markdown_to_html(body)
            
            # Extract slug from filename (YYYY-MM-DD-slug.md)
            filename = md_file.stem
            parts = filename.split('-', 3)
            if len(parts) >= 4:
                year = parts[0]
                month = parts[1]
                slug = parts[3]
            else:
                year = ''
                month = ''
                slug = filename

            permalink_year, permalink_month = resolve_post_permalink_date(metadata.get('date', ''), year, month)
            post_path = canonical_post_path(permalink_year, permalink_month, slug)
            
            post = {
                'title': metadata.get('title', 'Untitled'),
                'slug': slug,
              'year': permalink_year,
              'month': permalink_month,
                'date': metadata.get('date', ''),
                'author': metadata.get('author', 'admin'),
                'categories': metadata.get('categories', []),
                'tags': metadata.get('tags', []),
                'img': url(featured_img) if featured_img else None,
                'html': html_content,
                'canonical_path': post_path,
                'url': url(post_path),
                'excerpt': body[:250].replace('\n', ' ').strip() + '...' if len(body) > 250 else body,
                # Link to the source markdown file on GitHub so readers can open a PR
                'source': f"{repo_base}/{markdown_source_repo_path(md_file)}"
            }
            
            posts.append(post)
            
            if len(posts) % 50 == 0:
                print(f'  Read {len(posts)} posts...')
                
        except Exception as e:
            print(f'Error reading {md_file}: {e}')
            continue
    
    posts.sort(key=lambda post: (post['date'], post['canonical_path']), reverse=True)

    print(f'Read {len(posts)} posts')
    
    # Build category and tag maps
    cats_map = defaultdict(list)
    tags_map = defaultdict(list)
    year_map = defaultdict(list)
    month_map = defaultdict(list)
    
    for p in posts:
        for c in p['categories']:
            cats_map[c].append(p)
        for t in p['tags']:
            tags_map[t].append(p)
        if p['year']:
          year_map[p['year']].append(p)
          if p['month']:
            month_map[(p['year'], p['month'])].append(p)
    
    # Map category names to legacy URLs (used for links and category pages)
    legacy_category_map = {
        'News': '/news/',
        'Best Practice': '/best-practices/',
      'Tutorials': '/tutorials/',
      'Setting of the Week': '/setting-of-the-week/',
      'TechEd': '/teched/'
    }
    legacy_tag_map = {
      'Group Policy Preferences': '/group-policy-preferences/'
    }
    live_sitemap_category_names = {'News', 'Best Practice', 'Tutorials', 'TechEd'}
    live_sitemap_tag_names = set(legacy_tag_map)
    
    nav_html = generate_nav_html(url)
    
    # Card template
    def card_template(p):
        img_html = f'<img src="{p["img"]}" class="thumb" loading="lazy">' if p.get('img') else ''
        cats_str = ', '.join(p['categories'][:2]) if p['categories'] else 'Uncategorized'
        return f'''<article class="post-card">
{img_html}
<div class="card-body">
  <p class="meta">{p['date'][:10]} • {cats_str}</p>
  <h3><a href="{p['url']}">{p['title']}</a></h3>
  <p>{p['excerpt']}</p>
  <a class="button" href="{p['url']}">Continue Reading →</a>
</div>
</article>'''
    
    # Compact list template
    def compact_list_template(p):
        cats_str = ', '.join(p['categories'][:2]) if p['categories'] else 'Uncategorized'
        return f'''<article class="compact-post">
<div class="compact-meta">{p['date'][:10]} • {cats_str}</div>
<h3><a href="{p['url']}">{p['title']}</a></h3>
</article>'''

    extra_sitemap_pages = []

    def register_extra_sitemap_page(route_path, priority='0.4', changefreq='monthly'):
        extra_sitemap_pages.append({
            'loc': absolute_url(route_path),
            'lastmod': datetime.now().strftime('%Y-%m-%d'),
            'changefreq': changefreq,
            'priority': priority
        })

    def render_compact_list(items, empty_message='No posts found for this section yet.'):
        if not items:
            return f'<p>{empty_message}</p>'
        return '\n'.join(compact_list_template(p) for p in items)

    def unique_posts(items):
        seen = set()
        unique = []
        for item in items:
            key = item['canonical_path']
            if key in seen:
                continue
            seen.add(key)
            unique.append(item)
        return unique

    def post_has_category(post, category_name):
        return any(category.lower() == category_name.lower() for category in post['categories'])

    def post_has_tag(post, tag_name):
        return any(tag.lower() == tag_name.lower() for tag in post['tags'])

    def write_standard_page(route_path, page_title, heading, body_html, canonical_path=None,
                            include_in_sitemap=True, priority='0.4', changefreq='monthly'):
        route_dir = output_dir / Path(route_path.strip('/'))
        route_dir.mkdir(parents=True, exist_ok=True)
        canonical_target = canonical_path or route_path

        page_html = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{page_title} — GroupPolicy.biz</title>
  <link rel="canonical" href="{absolute_url(canonical_target)}">
  <link rel="stylesheet" href="{url('/styles.css')}">
  {head_extras_html}
</head>
<body>
  <div class="topbar">
    <div class="container">
      <div class="brand-section">
        <h1 class="site-title"><a href="{url('/')}">Group Policy Central</a></h1>
        <p class="site-tagline">News, Tips and Tutorials for all your Group Policy needs</p>
      </div>
      <div class="actions">
        <button id="theme-toggle" aria-label="Toggle theme">🌙</button>
      </div>
    </div>
  </div>
  {nav_html}
  <div class="container main-container">
    <article class="post-full">
      <header>
        <h1>{heading}</h1>
      </header>
      <div class="post-content">
        {body_html}
      </div>
    </article>
  </div>
  <script src="{url('/search.js')}"></script>
</body>
</html>'''

        (route_dir / 'index.html').write_text(page_html, encoding='utf-8')
        if include_in_sitemap:
            register_extra_sitemap_page(route_path, priority=priority, changefreq=changefreq)

    def write_collection_page(route_path, page_title, heading, intro_html, items, canonical_path=None,
                              priority='0.4', changefreq='monthly', empty_message='No matching posts were found.'):
        compact_html = render_compact_list(items, empty_message=empty_message)
        count_html = f'<p class="archive-count">{len(items)} posts</p>' if items else ''
        body_html = f'''
        {intro_html}
        {count_html}
        <div class="compact-list">{compact_html}</div>
        '''
        write_standard_page(
            route_path,
            page_title,
            heading,
            body_html,
            canonical_path=canonical_path,
            include_in_sitemap=True,
            priority=priority,
            changefreq=changefreq,
        )
    
    # Generate paginated index pages
    per_page = args.per_page
    total_pages = (len(posts) + per_page - 1) // per_page
    
    print(f'Generating {total_pages} paginated index pages...')
    
    for page_num in range(1, total_pages + 1):
        start_idx = (page_num - 1) * per_page
        end_idx = min(start_idx + per_page, len(posts))
        page_posts = posts[start_idx:end_idx]
        
        cards_html = '\n'.join(card_template(p) for p in page_posts)
        pagination_html = generate_pagination_html(page_num, total_pages, '/page/', url)
        
        # Archive notice only on first page
        archive_notice = ''
        if page_num == 1:
            archive_notice = f'''
    <div class="archive-notice" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 2rem; border-radius: 12px; margin-bottom: 2rem; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
      <h2 style="margin-top: 0; font-size: 1.75rem; margin-bottom: 1rem;">📚 Archive Notice</h2>
      <p style="font-size: 1.1rem; line-height: 1.6; margin-bottom: 1rem;">
        This site has been migrated to a <strong>GitHub repository</strong> to enable community contributions and long-term preservation.
        The content you see here is a <strong>legacy archive</strong> of Group Policy resources spanning 2009-2019.
      </p>
      <p style="font-size: 1rem; line-height: 1.6; margin-bottom: 1.25rem;">
        While the archive remains accessible here, we encourage contributors to submit corrections, updates, and improvements 
        via pull requests on GitHub. The site is now generated from Markdown files, making it easier than ever to contribute.
      </p>
      <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
        <a href="https://github.com/alanburchill/GroupPolicyBiz" style="display: inline-block; background: rgba(255,255,255,0.2); color: white; padding: 0.75rem 1.5rem; border-radius: 6px; text-decoration: none; font-weight: 600; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.3); transition: all 0.3s;" onmouseover="this.style.background='rgba(255,255,255,0.3)'" onmouseout="this.style.background='rgba(255,255,255,0.2)'">
          View on GitHub →
        </a>
        <a href="{url('/about/')}" style="display: inline-block; background: rgba(255,255,255,0.2); color: white; padding: 0.75rem 1.5rem; border-radius: 6px; text-decoration: none; font-weight: 600; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.3); transition: all 0.3s;" onmouseover="this.style.background='rgba(255,255,255,0.3)'" onmouseout="this.style.background='rgba(255,255,255,0.2)'">
          Learn More About This Archive
        </a>
      </div>
    </div>'''
        
        page_title = (
            'Group Policy Central - News, Tips and Tutorials for all your Group Policy needs'
            if page_num == 1
            else f'GroupPolicy.biz — Page {page_num}'
        )

        page_html = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{page_title}</title>
  <link rel="stylesheet" href="{url('/styles.css')}">
  {head_extras_html}
</head>
<body>
  <div class="topbar">
    <div class="container">
      <div class="brand-section">
        <h1 class="site-title"><a href="{url('/')}">Group Policy Central</a></h1>
        <p class="site-tagline">News, Tips and Tutorials for all your Group Policy needs</p>
      </div>
      <div class="actions">
        <button id="theme-toggle" aria-label="Toggle theme">🌙</button>
      </div>
    </div>
  </div>
  {nav_html}
  <div class="container main-container">
    {archive_notice}
    <h1>Latest Posts</h1>
    <div class="cards">{cards_html}</div>
    {pagination_html}
  </div>
  <script src="{url('/search.js')}"></script>
</body>
</html>'''
        
        # Add a footer to paginated index pages linking to the source posts directory on GitHub
        page_edit_footer = f"\n<footer style=\"margin-top:2rem; padding-top:1rem; border-top:1px solid #eee;\">\n  <div style=\"text-align:center; font-size:0.95rem;\">\n    <a href=\"{repo_base}/content/posts\" target=\"_blank\" rel=\"noopener noreferrer\">View source posts on GitHub</a>\n  </div>\n</footer>\n"

        if page_num == 1:
            (output_dir / 'index.html').write_text(page_html + page_edit_footer, encoding='utf-8')
        else:
            page_dir = output_dir / 'page' / str(page_num)
            page_dir.mkdir(parents=True, exist_ok=True)
            (page_dir / 'index.html').write_text(page_html + page_edit_footer, encoding='utf-8')
    
    # Generate individual post pages
    print(f'Generating {len(posts)} individual post pages...')
    
    for p in posts:
        if p['year'] and p['month']:
            post_dir = output_dir / p['year'] / p['month'] / p['slug']
        else:
            post_dir = posts_out / p['slug']
        post_dir.mkdir(parents=True, exist_ok=True)
        
        # Create clickable tag and category links
        tags_html = ' '.join(
            f'<a href="{url(legacy_tag_map.get(t, "/tag/" + re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-") + "/"))}" class="tag-badge">{t}</a>'
            for t in p['tags'][:10]
        )
        cats_html = ' '.join(
            f'<a href="{url(legacy_category_map.get(c, "/category/" + re.sub(r"[^a-z0-9]+", "-", c.lower()).strip("-") + "/"))}" class="category-badge">{c}</a>'
            for c in p['categories']
        )
        
        # Add a GitHub source link at the bottom of the post
        edit_link_html = f'''<div class="repo-edit" style="margin-top:1.5rem; font-size:0.95rem;
            border-top:1px solid #eee; padding-top:0.75rem;">
          <a href="{p.get('source', 'https://github.com/alanburchill/GroupPolicyBiz')}" target="_blank" rel="noopener noreferrer">View on GitHub</a>
        </div>'''

        post_html = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{p['title']} — GroupPolicy.biz</title>
  <link rel="canonical" href="{absolute_url(p['canonical_path'])}">
  <link rel="stylesheet" href="{url('/styles.css')}">
  {head_extras_html}
</head>
<body>
  <div class="topbar">
    <div class="container">
      <div class="brand-section">
        <h1 class="site-title"><a href="{url('/')}">Group Policy Central</a></h1>
        <p class="site-tagline">News, Tips and Tutorials for all your Group Policy needs</p>
      </div>
      <div class="actions">
        <button id="theme-toggle" aria-label="Toggle theme">🌙</button>
      </div>
    </div>
  </div>
  {nav_html}
  <div class="container main-container">
    <article class="post-full">
      <header>
        <div class="post-header-content">
          <div class="post-header-text">
            <h1>{p['title']}</h1>
            <p class="meta">{p['date']} • by {p['author']}</p>
            <div class="post-meta">
              {('<div class="post-categories">' + cats_html + '</div>') if cats_html else ''}
              {('<div class="post-tags">' + tags_html + '</div>') if tags_html else ''}
            </div>
          </div>
          {(f'<div class="post-header-image"><img src="{p["img"]}" alt="{p["title"]}" /></div>') if p.get('img') else ''}
        </div>
      </header>
      <div class="post-content">
{p['html']}
      </div>
      {edit_link_html}
    </article>
  </div>
  <script src="{url('/search.js')}"></script>
</body>
</html>'''
        write_post_page(post_dir, post_html)
    
    # Generate compatibility redirects from /posts/slug/ to the dated canonical permalink
    print(f'Generating compatibility redirects for {len(posts)} posts...')
    
    for p in posts:
        compatibility_path = f"/posts/{p['slug']}/"
        if compatibility_path == p['canonical_path']:
            continue

        compatibility_dir = posts_out / p['slug']
        compatibility_dir.mkdir(parents=True, exist_ok=True)

        redirect_html = write_redirect_page(p['url'], p['title'])
        (compatibility_dir / 'index.html').write_text(redirect_html, encoding='utf-8')
    
    # Generate category pages
    print(f'Generating {len(cats_map)} category pages...')
    
    for c, items in cats_map.items():
        slug = re.sub(r'[^a-z0-9]+','-', c.lower()).strip('-')
        compact_html = '\n'.join(compact_list_template(p) for p in items)
        
        page = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Category: {c} — GroupPolicy.biz</title>
  <link rel="stylesheet" href="{url('/styles.css')}">
  {head_extras_html}
</head>
<body>
  <div class="topbar">
    <div class="container">
      <div class="brand-section">
        <h1 class="site-title"><a href="{url('/')}">Group Policy Central</a></h1>
        <p class="site-tagline">News, Tips and Tutorials for all your Group Policy needs</p>
      </div>
      <div class="actions">
        <button id="theme-toggle" aria-label="Toggle theme">🌙</button>
      </div>
    </div>
  </div>
  {nav_html}
  <div class="container main-container">
    <h1>Category: {c}</h1>
    <p class="archive-count">{len(items)} posts</p>
    <div class="compact-list">{compact_html}</div>
  </div>
  <script src="{url('/search.js')}"></script>
</body>
</html>'''
        
        # Use legacy URL for specific categories, otherwise use /category/ prefix
        if c in legacy_category_map:
            # Strip leading/trailing slashes from legacy path for directory creation
            legacy_path = legacy_category_map[c].strip('/')
            category_dir = output_dir / legacy_path
            category_dir.mkdir(parents=True, exist_ok=True)
            (category_dir / 'index.html').write_text(page, encoding='utf-8')

            redirect_html = write_redirect_page(url(legacy_category_map[c]), f'Category: {c}')
            category_redirect_dir = cat_out / slug
            category_redirect_dir.mkdir(parents=True, exist_ok=True)
            (category_redirect_dir / 'index.html').write_text(redirect_html, encoding='utf-8')
        else:
            (cat_out / slug / 'index.html').parent.mkdir(parents=True, exist_ok=True)
            (cat_out / slug / 'index.html').write_text(page, encoding='utf-8')
    
    # Generate tag pages
    print(f'Generating {len(tags_map)} tag pages...')
    
    for t, items in tags_map.items():
        slug = re.sub(r'[^a-z0-9]+','-', t.lower()).strip('-')
        compact_html = '\n'.join(compact_list_template(p) for p in items)
        
        page = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Tag: {t} — GroupPolicy.biz</title>
  <link rel="stylesheet" href="{url('/styles.css')}">
  {head_extras_html}
</head>
<body>
  <div class="topbar">
    <div class="container">
      <div class="brand-section">
        <h1 class="site-title"><a href="{url('/')}">Group Policy Central</a></h1>
        <p class="site-tagline">News, Tips and Tutorials for all your Group Policy needs</p>
      </div>
      <div class="actions">
        <button id="theme-toggle" aria-label="Toggle theme">🌙</button>
      </div>
    </div>
  </div>
  {nav_html}
  <div class="container main-container">
    <h1>Tag: {t}</h1>
    <p class="archive-count">{len(items)} posts</p>
    <div class="compact-list">{compact_html}</div>
  </div>
  <script src="{url('/search.js')}"></script>
</body>
</html>'''
        tag_index = tag_out / slug / 'index.html'
        tag_index.parent.mkdir(parents=True, exist_ok=True)
        tag_index.write_text(page, encoding='utf-8')

        if t in legacy_tag_map:
            legacy_path = legacy_tag_map[t].strip('/')
            legacy_dir = output_dir / legacy_path
            legacy_dir.mkdir(parents=True, exist_ok=True)
            (legacy_dir / 'index.html').write_text(page, encoding='utf-8')

            redirect_html = write_redirect_page(url(legacy_tag_map[t]), f'Tag: {t}')
            tag_index.write_text(redirect_html, encoding='utf-8')
    
    # Generate year archives
    print(f'Generating {len(year_map)} year archive pages...')
    
    archives_out = output_dir / 'archives'
    archives_out.mkdir(exist_ok=True)
    
    for year, items in sorted(year_map.items(), reverse=True):
        compact_html = '\n'.join(compact_list_template(p) for p in items)
        
        page = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Archive: {year} — GroupPolicy.biz</title>
  <link rel="stylesheet" href="{url('/styles.css')}">
  {head_extras_html}
</head>
<body>
  <div class="topbar">
    <div class="container">
      <div class="brand-section">
        <h1 class="site-title"><a href="{url('/')}">Group Policy Central</a></h1>
        <p class="site-tagline">News, Tips and Tutorials for all your Group Policy needs</p>
      </div>
      <div class="actions">
        <button id="theme-toggle" aria-label="Toggle theme">🌙</button>
      </div>
    </div>
  </div>
  {nav_html}
  <div class="container main-container">
    <h1>Archive: {year}</h1>
    <p class="archive-count">{len(items)} posts</p>
    <div class="compact-list">{compact_html}</div>
  </div>
  <script src="{url('/search.js')}"></script>
</body>
</html>'''
        year_dir = archives_out / year
        year_dir.mkdir(parents=True, exist_ok=True)
        (year_dir / 'index.html').write_text(page, encoding='utf-8')

    # Generate live-style compatibility pages for year/month archive routes.
    print(f'Generating {len(year_map)} live-style year archive compatibility pages...')

    for year, items in sorted(year_map.items(), reverse=True):
        write_standard_page(
            f'/{year}/',
            f'{year}',
            f'Year: {year}',
            f'''
            <p>This preserved compatibility route matches the legacy live year archive path.</p>
            <p class="archive-count">{len(items)} posts</p>
            <div class="compact-list">{render_compact_list(items)}</div>
            ''',
            canonical_path=f'/{year}/',
            include_in_sitemap=False,
            priority='0.4',
            changefreq='monthly',
        )

    print(f'Generating {len(month_map)} live-style month archive compatibility pages...')

    for (year, month), items in sorted(month_map.items(), reverse=True):
        month_name = datetime.strptime(month, '%m').strftime('%B')
        write_standard_page(
            f'/{year}/{month}/',
            f'{month_name} {year}',
            f'Month: {month_name} {year}',
            f'''
            <p>This preserved compatibility route matches the legacy live month archive path.</p>
            <p class="archive-count">{len(items)} posts</p>
            <div class="compact-list">{render_compact_list(items)}</div>
            ''',
            canonical_path=f'/{year}/{month}/',
            include_in_sitemap=False,
            priority='0.4',
            changefreq='monthly',
        )
    
    # Generate archives landing page
    year_links_html = '\n'.join(
        f'<div class="archive-year-link"><a href="{url(f"/archives/{year}/")}"><span class="year">{year}</span><span class="count">{len(items)} posts</span></a></div>'
        for year, items in sorted(year_map.items(), reverse=True)
    )
    
    archives_landing = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Archives — GroupPolicy.biz</title>
  <link rel="stylesheet" href="{url('/styles.css')}">
  {head_extras_html}
</head>
<body>
  <div class="topbar">
    <div class="container">
      <div class="brand-section">
        <h1 class="site-title"><a href="{url('/')}">Group Policy Central</a></h1>
        <p class="site-tagline">News, Tips and Tutorials for all your Group Policy needs</p>
      </div>
      <div class="actions">
        <button id="theme-toggle" aria-label="Toggle theme">🌙</button>
      </div>
    </div>
  </div>
  {nav_html}
  <div class="container main-container">
    <h1>Archives</h1>
    <p class="archive-count">Browse posts by year</p>
    <div class="archive-year-list">{year_links_html}</div>
  </div>
  <script src="{url('/search.js')}"></script>
</body>
</html>'''
    (archives_out / 'index.html').write_text(archives_landing, encoding='utf-8')
    
    # Do not generate /categories/ or /tags/ hub pages.
    # The live site exposes individual category and tag archives, but these landing pages return 404.
    
    # Generate search index JSON
    search_index = []
    for p in posts:
        search_index.append({
            'title': p['title'],
            'url': p['url'],
            'excerpt': p['excerpt'],
            'date': p['date'][:10],
            'categories': p['categories'],
            'tags': p['tags']
        })
    
    (output_dir / 'search-index.json').write_text(json.dumps(search_index, indent=2), encoding='utf-8')
    
    # Copy static assets
    print('Copying static assets...')
    for asset in ['styles.css', 'search.js']:
        src = Path('static') / asset
        if src.exists():
            shutil.copy2(src, output_dir / asset)
    
    # Copy uploads directory
    uploads_src = Path('uploads')
    if uploads_src.exists():
        uploads_dest = output_dir / 'uploads'
        if uploads_dest.exists():
            shutil.rmtree(uploads_dest)
        shutil.copytree(uploads_src, uploads_dest)
        print(f'Copied uploads directory')
    
    # Generate about page with proper base path
    print('Generating about page...')
    about_dir = output_dir / 'about'
    about_dir.mkdir(exist_ok=True)
    
    nav_html = generate_nav_html(url)
    
    about_html = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>About & Privacy Policy — GroupPolicy.biz</title>
  <link rel="stylesheet" href="{url('/styles.css')}">
  {head_extras_html}
</head>
<body>
  <div class="topbar">
    <div class="container">
      <div class="brand-section">
        <h1 class="site-title"><a href="{url('/')}">Group Policy Central</a></h1>
        <p class="site-tagline">News, Tips and Tutorials for all your Group Policy needs</p>
      </div>
      <div class="actions">
        <button id="theme-toggle" aria-label="Toggle theme">🌙</button>
      </div>
    </div>
  </div>
  {nav_html}
  <div class="container main-container">
    <article class="post-full">
      <header>
        <h1>About Group Policy Central</h1>
      </header>
      <div class="post-content">
        <h2 id="about-this-site">About This Site</h2>
        <p>Welcome to Group Policy Central (GroupPolicy.biz), your comprehensive resource for Windows Group Policy news, tips, tutorials, and best practices.</p>
        
        <h3>Our Mission</h3>
        <p>This site is dedicated to helping IT professionals, system administrators, and Windows enthusiasts master Group Policy management. We provide:</p>
        <ul>
          <li><strong>Latest News:</strong> Stay updated with the latest Group Policy features, updates, and Microsoft announcements</li>
          <li><strong>Best Practices:</strong> Learn proven strategies for implementing and managing Group Policy in your organization</li>
          <li><strong>Tutorials:</strong> Step-by-step guides to help you configure and troubleshoot Group Policy settings</li>
          <li><strong>Security Baselines:</strong> Information about Microsoft security templates and recommendations</li>
          <li><strong>Administrative Templates:</strong> Resources for the latest ADMX files and policy settings</li>
        </ul>
        
        <h3>What We Cover</h3>
        <p>Our content includes information about:</p>
        <ul>
          <li>Windows Group Policy for Windows 7, 8, 10, and 11</li>
          <li>Windows Server Group Policy management</li>
          <li>Active Directory integration</li>
          <li>Group Policy Preferences</li>
          <li>Security baselines and compliance</li>
          <li>Internet Explorer and Microsoft Edge policies</li>
          <li>Windows Update policies</li>
          <li>Remote Desktop Services policies</li>
        </ul>
        
        <h3>Archive</h3>
        <p>This site contains archived content from 2009 through 2019, covering the evolution of Group Policy across multiple Windows versions. Browse our <a href="{url('/archives/')}">archives</a> to explore historical content and see how Group Policy management has evolved over the years.</p>

        <h3 id="disclaimer">Disclaimer</h3>
        <p>This archive is provided for informational and educational purposes only. Historical posts may describe products, settings, or best practices that have changed over time.</p>
        
        <hr style="margin: 3rem 0; border: none; border-top: 1px solid var(--border);">
        
        <h2 id="privacy-policy">Privacy Policy</h2>
        <p><em>Last Updated: February 10, 2026</em></p>
        
        <h3>Information Collection</h3>
        <p>This is a static archive website. We do not collect, store, or process any personal information from visitors. This site does not use:</p>
        <ul>
          <li>Cookies or tracking technologies</li>
          <li>Analytics services</li>
          <li>User accounts or registration</li>
          <li>Forms or data submission</li>
          <li>Third-party advertising networks</li>
        </ul>
        
        <h3>Content</h3>
        <p>All content on this site is provided for informational and educational purposes only. The information is based on historical blog posts about Windows Group Policy and may not reflect current best practices or software versions.</p>
        
        <h3>External Links</h3>
        <p>This site may contain links to external websites, including Microsoft documentation and other resources. We are not responsible for the privacy practices or content of external sites.</p>
        
        <h3>Local Storage</h3>
        <p>This site uses browser local storage only to save your theme preference (light/dark mode) on your device. This data never leaves your browser and is not transmitted to any server.</p>
        
        <h3>Copyright</h3>
        <p>Content on this site is provided as-is from archived blog posts. Windows, Group Policy, Active Directory, and related trademarks are property of Microsoft Corporation.</p>
        
        <h3>Changes to This Policy</h3>
        <p>As this is a static archive site, this privacy policy is unlikely to change. Any updates will be reflected in the "Last Updated" date above.</p>
        
        <h3 id="contact">Contact</h3>
        <p>This is an archived static site. For current information about Group Policy, please visit <a href="https://docs.microsoft.com/en-us/windows/client-management/group-policy-overview" target="_blank" rel="noopener">Microsoft's official Group Policy documentation</a>.</p>
      </div>
    </article>
  </div>
  <script src="{url('/search.js')}"></script>
</body>
</html>'''
    
    (about_dir / 'index.html').write_text(about_html, encoding='utf-8')

    # Generate legacy utility, resource, and archive routes that existed on the live site.
    print('Generating legacy utility and resource pages...')

    setting_posts = unique_posts(cats_map.get('Setting of the Week', []))
    video_posts = unique_posts(cats_map.get('Video', []) + [p for p in posts if post_has_tag(p, 'videos')])
    tech_ed_video_posts = unique_posts([p for p in video_posts if post_has_category(p, 'TechEd')])
    other_video_posts = [p for p in video_posts if p['canonical_path'] not in {item['canonical_path'] for item in tech_ed_video_posts}]
    usb_posts = unique_posts([p for p in posts if post_has_tag(p, 'USB')])
    kb_focus_posts = unique_posts(cats_map.get('KB Focus', []))
    hotfix_posts = unique_posts(
      cats_map.get('hotfix', []) +
      [p for p in posts if post_has_tag(p, 'hotfix')] +
      kb_focus_posts
    )

    write_standard_page(
      '/about/about-this-site/',
      'About this site',
      'About this site',
      f'''
      <p>Group Policy Central was originally published as a WordPress site and is now preserved as a static archive generated from Markdown sources.</p>
      <p>The goal is to keep historical Group Policy articles, tutorials, videos, and reference pages available at stable URLs while making long-term maintenance easier on GitHub.</p>
      <p>Browse the <a href="{url('/archives/')}">archives</a>, follow category links such as <a href="{url('/news/')}">News</a> and <a href="{url('/best-practices/')}">Best Practices</a>, or open tag links directly from any post.</p>
      <p>Where practical, legacy URLs from the original live site are preserved so cutover does not leave readers stranded in 404 country.</p>
      ''',
      priority='0.4',
    )

    write_standard_page(
      '/about/disclaimer/',
      'Disclaimer',
      'Disclaimer',
      '''
      <p>This archive is provided for informational and educational purposes only.</p>
      <p>Many articles describe products, settings, downloads, or best practices that may have changed over time. Always validate historical guidance against current Microsoft documentation and your own change-control processes.</p>
      <p>External links are retained where useful, but some destinations may have moved or been retired since the original posts were published.</p>
      ''',
      priority='0.3',
    )

    write_standard_page(
      '/about/privacy-policy/',
      'Privacy Policy',
      'Privacy Policy',
      '''
      <p>This archive site does not require accounts, forms, or comments, and it does not collect personal information from readers.</p>
      <p>The only client-side storage used by the current site is the theme preference saved in your own browser for light and dark mode.</p>
      <p>Some pages link to third-party sites such as Microsoft downloads and documentation. Those external sites have their own policies and behaviours.</p>
      ''',
      priority='0.3',
    )

    write_standard_page(
      '/contact/',
      'Contact',
      'Contact',
      f'''
      <p>The original contact form from the WordPress site has been retired as part of the static archive migration.</p>
      <p>For archive fixes or content improvements, please use the <a href="https://github.com/alanburchill/GroupPolicyBiz" target="_blank" rel="noopener noreferrer">GitHub repository</a>.</p>
      <p>For current Group Policy guidance, see <a href="https://learn.microsoft.com/windows/client-management/group-policy-overview" target="_blank" rel="noopener noreferrer">Microsoft's Group Policy documentation</a>.</p>
      ''',
      priority='0.3',
    )

    write_standard_page(
      '/search/',
      'Search',
      'Search',
      '''
      <p>Use the search box in the site header to search titles, excerpts, categories, and tags across the archive.</p>
      <p>Results appear as you type once the local search index has loaded.</p>
      ''',
      priority='0.4',
      changefreq='weekly',
    )

    resources_links_html = f'''
    <p>This route preserves the old resource hub from the live site and points to the closest local equivalents.</p>
    <div class="archive-year-list">
      <div class="archive-year-link"><a href="{url('/resources/videos2/')}"><span class="year">Videos</span><span class="count">Curated video resources and session roundups</span></a></div>
      <div class="archive-year-link"><a href="{url('/archives/videos/')}"><span class="year">Video Archive</span><span class="count">All archived posts in the Video collection</span></a></div>
      <div class="archive-year-link"><a href="{url('/files/')}"><span class="year">Files</span><span class="count">Legacy tools, templates, and download references</span></a></div>
      <div class="archive-year-link"><a href="{url('/resources/hotfixes/')}"><span class="year">Group Policy Hotfixes</span><span class="count">Hotfix roundups and KB-focused posts</span></a></div>
      <div class="archive-year-link"><a href="{url('/archives/group-policy-for-usb/')}"><span class="year">USB</span><span class="count">Posts about removable storage and USB policy controls</span></a></div>
      <div class="archive-year-link"><a href="{url('/archives/microsft-kb-focus/')}"><span class="year">KB Focus</span><span class="count">Preserved knowledge-base deep dives</span></a></div>
    </div>
    '''
    write_standard_page('/resources/', 'Resources', 'Resources', resources_links_html, priority='0.5', changefreq='weekly')

    files_body = f'''
    <p>This page preserves the legacy file and download references that were linked from the original site. Some downloads may have moved over time, but the route remains available for cutover compatibility.</p>

    <h2>Remote Server Admin Tools</h2>
    <ul>
      <li><a href="http://www.microsoft.com/downloads/details.aspx?displaylang=en&amp;FamilyID=9ff6e897-23ce-4a36-b7fc-d52065de9960">Windows Vista</a></li>
      <li><a href="http://www.microsoft.com/downloads/details.aspx?displaylang=en&amp;FamilyID=d647a60b-63fd-4ac5-9243-bd3c497d2bc5">Windows Vista x64</a></li>
      <li><a href="http://www.microsoft.com/downloads/details.aspx?FamilyID=7d2f6ad7-656b-4313-a005-4e344e43997d&amp;displaylang=en">Windows 7</a></li>
      <li><a href="http://www.microsoft.com/en-us/download/details.aspx?id=28972">Windows 8</a></li>
      <li><a href="http://www.microsoft.com/en-us/download/details.aspx?id=39296">Windows 8.1</a></li>
    </ul>

    <h2>Client-Side Extensions</h2>
    <ul>
      <li><a href="http://www.microsoft.com/downloads/details.aspx?displaylang=en&amp;FamilyID=e60b5c8f-d7dc-4b27-a261-247ce3f6c4f8">Windows XP</a></li>
      <li><a href="http://www.microsoft.com/downloads/details.aspx?displaylang=en&amp;FamilyID=249c1aed-c1f1-4a0b-872e-ef0a32170625">Windows XP x64</a></li>
      <li><a href="http://www.microsoft.com/downloads/details.aspx?familyid=AB60DC87-884C-46D5-82CD-F3C299DAC7CC&amp;displaylang=en">Windows Vista</a></li>
      <li><a href="http://www.microsoft.com/downloads/details.aspx?familyid=B10A7AF4-8BEE-4ADC-8BBE-9949DF77A3CF&amp;displaylang=en">Windows Vista x64</a></li>
      <li><a href="http://www.microsoft.com/downloads/details.aspx?familyid=BFE775F9-5C34-44D0-8A94-44E47DB35ADD&amp;displaylang=en">Windows Server 2003</a></li>
      <li><a href="http://www.microsoft.com/downloads/details.aspx?familyid=29E83503-7686-49F3-B42D-8E5ED23D5D79&amp;displaylang=en">Windows Server 2003 x64</a></li>
    </ul>

    <h2>Useful Tools</h2>
    <ul>
      <li><a href="http://www.microsoft.com/downloads/details.aspx?FamilyID=35791cb6-710b-48c4-aaa1-90db170bcf2a&amp;displaylang=en">Group Policy Preferences Migration Tool (GPPMIG)</a></li>
      <li><a href="http://www.microsoft.com/downloads/details.aspx?displaylang=en&amp;FamilyID=18c90c80-8b0a-4906-a4f5-ff24cc2030fb">Group Policy Settings Reference for Windows and Windows Server</a></li>
      <li><a href="http://www.microsoft.com/scm">Security Compliance Manager</a></li>
    </ul>

    <h2>Administrative Templates</h2>
    <ul>
      <li><a href="http://www.microsoft.com/en-us/download/details.aspx?id=37009">Internet Explorer 10</a></li>
      <li><a href="http://www.microsoft.com/en-us/download/details.aspx?id=36991">Windows 8 / Windows Server 2012</a></li>
      <li><a href="http://www.microsoft.com/en-us/download/details.aspx?id=40905">Internet Explorer 11 ADMX</a></li>
      <li><a href="http://www.microsoft.com/en-US/download/details.aspx?id=41193">Windows 8.1 ADMX</a></li>
    </ul>

    <h2>Hotfix References</h2>
    <p>For the historical hotfix roundups and KB-focused write-ups from the archive, see <a href="{url('/resources/hotfixes/')}">Group Policy Hotfixes</a>.</p>
    '''
    write_standard_page('/files/', 'Files', 'Files', files_body, priority='0.5')

    write_collection_page(
      '/group-policy-setting-of-the-week/',
      'Group Policy Setting of the Week',
      'Group Policy Setting of the Week',
      f'''
      <p>This preserved legacy landing page collects the Group Policy Setting of the Week series.</p>
      <p>The shorter local route <a href="{url('/setting-of-the-week/')}">/setting-of-the-week/</a> remains available as the main archive listing, while this page keeps the original live-style URL working.</p>
      ''',
      setting_posts,
      canonical_path='/setting-of-the-week/',
      priority='0.4',
      changefreq='weekly',
      empty_message='No Setting of the Week posts were found in the archive.',
    )

    write_collection_page(
      '/archives/videos/',
      'Videos',
      'Videos',
      f'''
      <p>This preserved archive route lists posts from the Video collection.</p>
      <p>For TechEd-heavy content specifically, also see <a href="{url('/teched/')}">/teched/</a>.</p>
      ''',
      video_posts,
      priority='0.4',
      changefreq='weekly',
      empty_message='No video posts were found in the archive.',
    )

    videos2_body = f'''
    <p>This route preserves the old curated videos page from the live site.</p>
    <p>It now groups the archive's video content into TechEd sessions and other video posts.</p>

    <h2>TechEd Sessions</h2>
    <div class="compact-list">{render_compact_list(tech_ed_video_posts, empty_message='No TechEd videos were found in the archive.')}</div>

    <h2>Other Video Posts</h2>
    <div class="compact-list">{render_compact_list(other_video_posts, empty_message='No additional video posts were found in the archive.')}</div>
    '''
    write_standard_page('/resources/videos2/', 'Videos', 'Videos', videos2_body, priority='0.4', changefreq='weekly')

    write_collection_page(
      '/resources/hotfixes/',
      'Hotfixes',
      'Hotfixes',
      '''
      <p>The original site maintained a manually curated hotfix page. This preserved route now points to the archive's hotfix roundups and KB-focused articles.</p>
      <p>Some original Microsoft hotfix downloads may have moved or been retired, but the supporting write-ups remain here.</p>
      ''',
      hotfix_posts,
      priority='0.4',
      changefreq='weekly',
      empty_message='No hotfix-related posts were found in the archive.',
    )

    write_collection_page(
      '/archives/group-policy-for-usb/',
      'Group Policy settings for USB',
      'Group Policy settings for USB',
      '''
      <p>This preserved archive route gathers posts tagged with USB, including removable storage controls, BitLocker To Go, and related policy settings.</p>
      ''',
      usb_posts,
      priority='0.4',
      changefreq='monthly',
      empty_message='No USB-related posts were found in the archive.',
    )

    write_collection_page(
      '/archives/microsft-kb-focus/',
      'Microsft KB Focus',
      'Microsft KB Focus',
      f'''
      <p>This route keeps the original live-site slug, typo and all, while surfacing the archive's KB Focus posts.</p>
      <p>If you prefer the cleaner archive taxonomy, you can also browse <a href="{url('/category/kb-focus/')}">the KB Focus category</a>.</p>
      ''',
      kb_focus_posts,
      priority='0.3',
      changefreq='monthly',
      empty_message='No KB Focus posts were found in the archive.',
    )

    # Generate compatibility redirects for legacy utility pages that still existed on the live site.
    legacy_redirect_routes = {
      '/archives/setting-of-the-week/': '/group-policy-setting-of-the-week/',
      '/search-2/': '/search/',
      '/search_gcse/': '/search/',
    }

    legacy_redirect_sitemap_routes = {
      '/archives/setting-of-the-week/': ('0.3', 'monthly'),
      '/search-2/': ('0.2', 'monthly'),
      '/search_gcse/': ('0.2', 'monthly'),
    }

    for legacy_path, target_path in legacy_redirect_routes.items():
        legacy_dir = output_dir / Path(legacy_path.strip('/'))
        legacy_dir.mkdir(parents=True, exist_ok=True)
        (legacy_dir / 'index.html').write_text(
            write_redirect_page(url(target_path), 'Group Policy Central'),
            encoding='utf-8'
        )

    for legacy_path, (priority, changefreq) in legacy_redirect_sitemap_routes.items():
      register_extra_sitemap_page(legacy_path, priority=priority, changefreq=changefreq)
    
    # Generate sitemap.xml
    print('Generating sitemap.xml...')
    
    # Use relative URLs so sitemap works with both subdirectory deployment and custom domains.
    # Dated post permalinks are now canonical when the source filename includes year/month data.
    
    sitemap_urls = []
    
    # Homepage (highest priority)
    sitemap_urls.append({
      'loc': absolute_url("/"),
        'lastmod': datetime.now().strftime('%Y-%m-%d'),
        'changefreq': 'weekly',
        'priority': '1.0'
    })
    
    # All individual posts
    for p in posts:
        sitemap_urls.append({
      'loc': absolute_url(p['canonical_path']),
            'lastmod': p['date'][:10] if p['date'] else datetime.now().strftime('%Y-%m-%d'),
            'changefreq': 'monthly',
            'priority': '0.8'
        })
    
    # Category pages
    for c in cats_map.keys():
      if c not in live_sitemap_category_names:
        continue
      slug = re.sub(r'[^a-z0-9]+', '-', c.lower()).strip('-')
      if c in legacy_category_map:
          cat_url = legacy_category_map[c]
      else:
          cat_url = f'/category/{slug}/'
      sitemap_urls.append({
        'loc': absolute_url(cat_url),
          'lastmod': datetime.now().strftime('%Y-%m-%d'),
          'changefreq': 'weekly',
          'priority': '0.6'
      })
    
    # Tag pages
    for t in tags_map.keys():
      if t not in live_sitemap_tag_names:
        continue
      slug = re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')
      sitemap_urls.append({
        'loc': absolute_url(legacy_tag_map.get(t, f"/tag/{slug}/")),
          'lastmod': datetime.now().strftime('%Y-%m-%d'),
          'changefreq': 'monthly',
          'priority': '0.5'
      })
    
    # Main archive and about pages
    for page_url, priority in [
        ('/archives/', '0.7'),
        ('/about/', '0.6')
    ]:
        sitemap_urls.append({
          'loc': absolute_url(page_url),
            'lastmod': datetime.now().strftime('%Y-%m-%d'),
            'changefreq': 'weekly',
            'priority': priority
        })

    sitemap_urls.extend(extra_sitemap_pages)
    
    # Build XML sitemap
    sitemap_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
'''
    for url_entry in sitemap_urls:
        sitemap_xml += f'''  <url>
    <loc>{url_entry['loc']}</loc>
    <lastmod>{url_entry['lastmod']}</lastmod>
    <changefreq>{url_entry['changefreq']}</changefreq>
    <priority>{url_entry['priority']}</priority>
  </url>
'''
    sitemap_xml += '</urlset>\n'
    
    (output_dir / 'sitemap.xml').write_text(sitemap_xml, encoding='utf-8')
    print(f'Generated sitemap.xml with {len(sitemap_urls)} URLs')
    
    print(f'\nGenerated {len(posts)} posts across {total_pages} pages')
    print(f'Generated {len(cats_map)} category pages')
    print(f'Generated {len(tags_map)} tag pages')
    print(f'Generated {len(year_map)} year archive pages')
    print(f'Generated {len(month_map)} live-style month archive compatibility pages')
    print(f'Created search index with {len(search_index)} entries')
    print(f'\nStatic site generated in: {output_dir.absolute()}')

if __name__ == '__main__':
    main()
