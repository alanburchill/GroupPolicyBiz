#!/usr/bin/env python3
"""Extract featured images from WordPress XML and update markdown files."""
import re
from pathlib import Path
import xml.etree.ElementTree as ET

def extract_featured_images_from_xml(xml_path):
    """Parse WordPress XML to get post slug -> featured image URL mapping."""
    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    # WordPress XML namespace
    ns = {
        'content': 'http://purl.org/rss/1.0/modules/content/',
        'wp': 'http://wordpress.org/export/1.2/',
        'excerpt': 'http://wordpress.org/export/1.2/excerpt/'
    }
    
    # First pass: collect all attachments by post_id
    attachments = {}
    for item in root.findall('.//item'):
        post_type = item.find('wp:post_type', ns)
        if post_type is not None and post_type.text == 'attachment':
            post_id = item.find('wp:post_id', ns)
            attachment_url = item.find('wp:attachment_url', ns)
            if post_id is not None and attachment_url is not None:
                attachments[post_id.text] = attachment_url.text
    
    # Second pass: get posts and their featured images
    featured_images = {}
    for item in root.findall('.//item'):
        post_type = item.find('wp:post_type', ns)
        if post_type is not None and post_type.text == 'post':
            post_name = item.find('wp:post_name', ns)
            if post_name is None or not post_name.text:
                continue
            
            # Look for _thumbnail_id in postmeta
            thumbnail_id = None
            for postmeta in item.findall('wp:postmeta', ns):
                meta_key = postmeta.find('wp:meta_key', ns)
                if meta_key is not None and meta_key.text == '_thumbnail_id':
                    meta_value = postmeta.find('wp:meta_value', ns)
                    if meta_value is not None:
                        thumbnail_id = meta_value.text
                        break
            
            if thumbnail_id and thumbnail_id in attachments:
                featured_images[post_name.text] = attachments[thumbnail_id]
    
    return featured_images

def update_markdown_files(featured_images, content_dir):
    """Update markdown files with featured_image in front matter."""
    updated_count = 0
    
    for md_file in Path(content_dir).glob('*.md'):
        # Extract slug from filename (YYYY-MM-DD-slug.md)
        filename = md_file.stem
        parts = filename.split('-', 3)
        if len(parts) >= 4:
            slug = parts[3]
        else:
            slug = filename
        
        if slug not in featured_images:
            continue
        
        # Read the file
        content = md_file.read_text(encoding='utf-8')
        
        # Check if it already has featured_image
        if 'featured_image:' in content:
            print(f"Skipping {md_file.name} - already has featured_image")
            continue
        
        # Parse front matter
        if not content.startswith('---'):
            print(f"Skipping {md_file.name} - no front matter")
            continue
        
        parts = content.split('---', 2)
        if len(parts) < 3:
            print(f"Skipping {md_file.name} - invalid front matter")
            continue
        
        front_matter = parts[1].strip()
        body = parts[2]
        
        # Get the featured image URL and convert to local path
        image_url = featured_images[slug]
        image_url = image_url.replace('http://www.grouppolicy.biz/wp-content/uploads/', '/uploads/')
        image_url = image_url.replace('https://www.grouppolicy.biz/wp-content/uploads/', '/uploads/')
        image_url = image_url.replace('http://www.endpointcentral.com/wp-content/uploads/', '/uploads/')
        
        # Add featured_image to front matter
        new_front_matter = front_matter + f'\nfeatured_image: "{image_url}"'
        
        # Reconstruct the file
        new_content = f"---\n{new_front_matter}\n---{body}"
        
        # Write back
        md_file.write_text(new_content, encoding='utf-8')
        print(f"Updated {md_file.name} with featured image: {image_url}")
        updated_count += 1
    
    return updated_count

def main():
    xml_path = r"E:\OneDrive\GroupPolicy Biz Export\grouppolicycentral.WordPress.2026-01-28.sanitized.xml"
    content_dir = "content/posts"
    
    print("Extracting featured images from WordPress XML...")
    featured_images = extract_featured_images_from_xml(xml_path)
    print(f"Found {len(featured_images)} posts with featured images")
    
    print("\nUpdating markdown files...")
    updated_count = update_markdown_files(featured_images, content_dir)
    print(f"\nUpdated {updated_count} markdown files")

if __name__ == '__main__':
    main()
