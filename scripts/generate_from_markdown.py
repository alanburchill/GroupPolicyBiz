#!/usr/bin/env python3
"""Generate static HTML site from Markdown files.

Usage: python scripts/generate_from_markdown.py --content content/posts --output _site --per-page 12
"""
import argparse
import re
import json
from pathlib import Path
from datetime import datetime
import markdown
from collections import defaultdict

# Import shared functions from the WordPress generator
import sys
sys.path.insert(0, str(Path(__file__).parent))

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
        <div class="nav-item"><a href="{url_func('/categories/')}">CATEGORIES</a></div>
        <div class="nav-item"><a href="{url_func('/tags/')}">TAGS</a></div>
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

def main():
    parser = argparse.ArgumentParser(description='Generate static site from Markdown files')
    parser.add_argument('--content', default='content/posts', help='Directory containing Markdown files')
    parser.add_argument('--output', default='_site', help='Output directory for generated site')
    parser.add_argument('--per-page', type=int, default=12, help='Posts per page')
    parser.add_argument('--base-path', default='/', help='Base path for GitHub Pages subdirectory deployment (e.g., "/" or "/GroupPolicyBiz/")')
    args = parser.parse_args()
    
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
        base = args.base_path
        
        # Normalize base_path: ensure it starts with / and ends with /
        if not base.startswith('/'):
            base = '/' + base
        if not base.endswith('/'):
            base = base + '/'
        
        # Normalize path: ensure it starts with /
        if not path.startswith('/'):
            path = '/' + path
        
        # If base_path is just '/', return path as-is
        if base == '/':
            return path
        
        # Remove leading slash from path since base already ends with /
        path = path.lstrip('/')
        
        return base + path
    
    content_dir = Path(args.content)
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Base URL for GitHub repository (used to point to source markdown files)
    repo_base = 'https://github.com/alanburchill/GroupPolicyBiz/blob/main'

    # Output subfolders
    posts_out = output_dir / 'posts'
    cat_out = output_dir / 'category'
    tag_out = output_dir / 'tag'

    print(f'Reading Markdown files from {content_dir}...')
    
    # Read all Markdown files
    posts = []
    md_files = sorted(content_dir.glob('*.md'), reverse=True)
    
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
            
            post = {
                'title': metadata.get('title', 'Untitled'),
                'slug': slug,
                'year': year,
                'month': month,
                'date': metadata.get('date', ''),
                'author': metadata.get('author', 'admin'),
                'categories': metadata.get('categories', []),
                'tags': metadata.get('tags', []),
                'img': url(featured_img) if featured_img else None,
                'html': html_content,
                'url': url(f'/posts/{slug}/'),
                'excerpt': body[:250].replace('\n', ' ').strip() + '...' if len(body) > 250 else body,
                # Link to the source markdown file on GitHub so readers can open a PR
                'source': f"{repo_base}/{content_dir.as_posix()}/{md_file.name}"
            }
            
            posts.append(post)
            
            if len(posts) % 50 == 0:
                print(f'  Read {len(posts)} posts...')
                
        except Exception as e:
            print(f'Error reading {md_file}: {e}')
            continue
    
    print(f'Read {len(posts)} posts')
    
    # Build category and tag maps
    cats_map = defaultdict(list)
    tags_map = defaultdict(list)
    year_map = defaultdict(list)
    
    for p in posts:
        for c in p['categories']:
            cats_map[c].append(p)
        for t in p['tags']:
            tags_map[t].append(p)
        if p['date']:
            year = p['date'][:4]
            year_map[year].append(p)
    
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
        
        page_html = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>GroupPolicy.biz — Page {page_num}</title>
  <link rel="stylesheet" href="{url('/styles.css')}">
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
        post_dir = posts_out / p['slug']
        post_dir.mkdir(parents=True, exist_ok=True)
        
        tags_html = ' '.join(f'<span class="tag-badge">{t}</span>' for t in p['tags'][:10])
        cats_html = ' '.join(f'<span class="category-badge">{c}</span>' for c in p['categories'])
        
        # Add an "Edit on GitHub" link at the bottom of the post so readers can open PRs
        edit_link_html = f'''<div class="repo-edit" style="margin-top:1.5rem; font-size:0.95rem;
            border-top:1px solid #eee; padding-top:0.75rem;">
            <a href="{p.get('source', 'https://github.com/alanburchill/GroupPolicyBiz')}" target="_blank" rel="noopener noreferrer">Edit this post on GitHub</a>
        </div>'''

        post_html = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{p['title']} — GroupPolicy.biz</title>
  <link rel="stylesheet" href="{url('/styles.css')}">
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
        (post_dir / 'index.html').write_text(post_html, encoding='utf-8')
    
    # Generate legacy WordPress URL redirects (/YYYY/MM/slug/ -> /posts/slug/)
    print(f'Generating legacy URL redirects for {len(posts)} posts...')
    
    for p in posts:
        if p['year'] and p['month']:
            # Create redirect at /YYYY/MM/slug/index.html
            legacy_dir = output_dir / p['year'] / p['month'] / p['slug']
            legacy_dir.mkdir(parents=True, exist_ok=True)
            
            redirect_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="0; url={url(f"/posts/{p['slug']}/")}">
  <link rel="canonical" href="{url(f"/posts/{p['slug']}/")}">
  <title>Redirecting to {p['title']}</title>
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
    <p>If you are not redirected automatically, <a href="{url(f"/posts/{p['slug']}/")}">click here</a>.</p>
  </div>
</body>
</html>'''
            (legacy_dir / 'index.html').write_text(redirect_html, encoding='utf-8')
    
    # Generate category pages
    print(f'Generating {len(cats_map)} category pages...')
    
    # Map category names to legacy URLs
    legacy_category_map = {
        'News': 'news',
        'Best Practice': 'best-practices',
        'Tutorials': 'tutorials'
    }
    
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
            category_dir = output_dir / legacy_category_map[c]
            category_dir.mkdir(parents=True, exist_ok=True)
            (category_dir / 'index.html').write_text(page, encoding='utf-8')
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
        (tag_out / slug / 'index.html').parent.mkdir(parents=True, exist_ok=True)
        (tag_out / slug / 'index.html').write_text(page, encoding='utf-8')
    
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
    
    # Generate categories landing page
    categories_dir = output_dir / 'categories'
    categories_dir.mkdir(exist_ok=True)
    
    # Map categories to their URLs (legacy URLs for main categories)
    legacy_category_map = {
        'News': '/news/',
        'Best Practice': '/best-practices/',
        'Tutorials': '/tutorials/'
    }
    
    category_links_html = '\n'.join(
        f'<div class="archive-year-link"><a href="{url(legacy_category_map.get(cat, "/category/" + re.sub(r"[^a-z0-9]+", "-", cat.lower()).strip("-") + "/"))}"><span class="year">{cat}</span><span class="count">{len(items)} posts</span></a></div>'
        for cat, items in sorted(cats_map.items())
    )
    
    categories_landing = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Categories — GroupPolicy.biz</title>
  <link rel="stylesheet" href="{url('/styles.css')}">
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
    <h1>Categories</h1>
    <p class="archive-count">Browse posts by category</p>
    <div class="archive-year-list">{category_links_html}</div>
  </div>
  <script src="{url('/search.js')}"></script>
</body>
</html>'''
    (categories_dir / 'index.html').write_text(categories_landing, encoding='utf-8')
    
    # Generate tags landing page with tag cloud
    tags_dir = output_dir / 'tags'
    tags_dir.mkdir(exist_ok=True)
    
    tag_counts = [(tag, len(items)) for tag, items in tags_map.items()]
    if tag_counts:
        min_count = min(count for _, count in tag_counts)
        max_count = max(count for _, count in tag_counts)
        count_range = max_count - min_count if max_count > min_count else 1
        
        tag_cloud_html = '\n'.join(
            f'<a href="{url("/tag/" + re.sub(r"[^a-z0-9]+", "-", tag.lower()).strip("-") + "/")}" class="tag-cloud-item" style="font-size: {0.8 + 1.2 * ((count - min_count) / count_range)}rem; padding: 0.25rem 0.6rem; margin: 0; line-height: 1.2; display: inline-block;" title="{count} posts">{tag}</a>'
            for tag, count in sorted(tag_counts, key=lambda x: x[0].lower())
        )
    else:
        tag_cloud_html = '<p>No tags found.</p>'
    
    tags_landing = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Tags — GroupPolicy.biz</title>
  <link rel="stylesheet" href="{url('/styles.css')}">
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
    <h1 style="margin-bottom: 0.5rem;">Tags</h1>
    <p class="archive-count" style="margin-bottom: 1rem;">Browse posts by tag - size indicates popularity</p>
    <div class="tag-cloud" style="line-height: 1.4; display: flex; flex-wrap: wrap; gap: 0.4rem; margin-top: 1rem;">{tag_cloud_html}</div>
  </div>
  <script src="{url('/search.js')}"></script>
</body>
</html>'''
    (tags_dir / 'index.html').write_text(tags_landing, encoding='utf-8')
    
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
    import shutil
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
        <h2>About This Site</h2>
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
        
        <hr style="margin: 3rem 0; border: none; border-top: 1px solid var(--border);">
        
        <h2>Privacy Policy</h2>
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
        
        <h3>Contact</h3>
        <p>This is an archived static site. For current information about Group Policy, please visit <a href="https://docs.microsoft.com/en-us/windows/client-management/group-policy-overview" target="_blank" rel="noopener">Microsoft's official Group Policy documentation</a>.</p>
      </div>
    </article>
  </div>
  <script src="{url('/search.js')}"></script>
</body>
</html>'''
    
    (about_dir / 'index.html').write_text(about_html, encoding='utf-8')
    
    print(f'\nGenerated {len(posts)} posts across {total_pages} pages')
    print(f'Generated {len(cats_map)} category pages')
    print(f'Generated {len(tags_map)} tag pages')
    print(f'Generated {len(year_map)} year archive pages')
    print(f'Created search index with {len(search_index)} entries')
    print(f'\nStatic site generated in: {output_dir.absolute()}')

if __name__ == '__main__':
    main()
