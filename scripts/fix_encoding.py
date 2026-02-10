#!/usr/bin/env python3
"""Fix common UTF-8 encoding issues in Markdown files.

These occur when smart quotes and special characters are incorrectly encoded.
"""
import re
from pathlib import Path

def fix_encoding_issues(text):
    """Fix common UTF-8 encoding problems."""
    replacements = {
        # Smart quotes (corrupted)
        'â€œ': '"',  # Left double quote
        'â€': '"',   # Right double quote
        'â€™': "'",  # Right single quote/apostrophe
        'â€˜': "'",  # Left single quote
        '"™': "'",   # Corrupted apostrophe (shows as trademark symbol)
        '"˜': "'",   # Corrupted left single quote
        
        # Smart quotes (proper Unicode - convert to ASCII)
        '"': '"',    # U+201C Left double quotation mark
        '"': '"',    # U+201D Right double quotation mark
        ''': "'",    # U+2018 Left single quotation mark  
        ''': "'",    # U+2019 Right single quotation mark
        
        # Control characters (corrupted quotes)
        '\x9d': '"',  # U+009D Operating System Command (corrupted closing quote)
        '\x9c': '"',  # U+009C String Terminator (corrupted opening quote)
        
        # Special symbols
        '¦': '...',   # U+00A6 Broken bar (corrupted ellipsis)
        
        # Dashes
        'â€"': '—',  # Em dash
        'â€"': '–',  # En dash
        'â€"': '-',  # Alternative dash encoding
        
        # Other common characters
        'â€¦': '...',  # Ellipsis
        'â€¢': '•',    # Bullet
        'Â': '',       # Non-breaking space artifact
        'Â ': ' ',     # Non-breaking space with space
        
        # Degree symbol
        'Â°': '°',
        
        # Copyright/trademark
        'Â©': '©',
        'â„¢': '™',
        'Â®': '®',
        
        # Fractions
        'Â½': '½',
        'Â¼': '¼',
        'Â¾': '¾',
        
        # Currency
        'Â£': '£',
        'â‚¬': '€',
    }
    
    result = text
    for bad, good in replacements.items():
        result = result.replace(bad, good)
    
    # Fix consecutive duplicate quotes caused by conversion
    result = result.replace('""', '"')  # Double quotes to single
    result = result.replace("''", "'")  # Double apostrophes to single
    # Run twice to catch triple quotes
    result = result.replace('""', '"')
    result = result.replace("''", "'")
    
    return result

def process_file(filepath):
    """Process a single Markdown file."""
    try:
        content = filepath.read_text(encoding='utf-8')
        original = content
        
        # Fix encoding issues
        fixed = fix_encoding_issues(content)
        
        # Check if changes were made
        if fixed != original:
            filepath.write_text(fixed, encoding='utf-8')
            return True
        return False
        
    except Exception as e:
        print(f'Error processing {filepath}: {e}')
        return False

def main():
    content_dir = Path('content/posts')
    
    if not content_dir.exists():
        print(f'Error: Directory not found: {content_dir}')
        return
    
    print(f'Scanning Markdown files in {content_dir}...\n')
    
    md_files = list(content_dir.glob('*.md'))
    fixed_count = 0
    
    for md_file in md_files:
        if process_file(md_file):
            fixed_count += 1
            if fixed_count <= 10:  # Show first 10
                print(f'Fixed: {md_file.name}')
    
    if fixed_count > 10:
        print(f'... and {fixed_count - 10} more files')
    
    print(f'\nTotal: {fixed_count} files fixed out of {len(md_files)} files')
    
    if fixed_count > 0:
        print('\nRegenerate the site to apply changes:')
        print('python scripts/generate_from_markdown.py --content content/posts --output _site --per-page 12')
    else:
        print('\nNo encoding issues found!')

if __name__ == '__main__':
    main()
