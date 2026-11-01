"""Generate public discovery files from the same posts as the site."""
from datetime import datetime, timezone
from email.utils import format_datetime
from html.parser import HTMLParser
from pathlib import Path
from xml.etree import ElementTree as ET

ATOM = 'http://www.w3.org/2005/Atom'
ET.register_namespace('atom', ATOM)


class PlainText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def published_date(value):
    date = datetime.fromisoformat(value.replace('Z', '+00:00'))
    # Treat archive dates without a recorded offset as UTC for feed formatting.
    return date.replace(tzinfo=timezone.utc) if date.tzinfo is None else date.astimezone(timezone.utc)


def write_discovery(output_dir: Path, posts, absolute_url):
    """Write recent-post feeds and a short, origin-aware agent guide."""
    recent = posts[:30]
    rss = ET.Element('rss', {'version': '2.0'})
    channel = ET.SubElement(rss, 'channel')
    ET.SubElement(channel, 'title').text = 'Group Policy Central'
    ET.SubElement(channel, 'link').text = absolute_url('/')
    ET.SubElement(channel, 'description').text = 'Historical tutorials, news and guidance for Windows Group Policy administrators.'
    ET.SubElement(channel, f'{{{ATOM}}}link', {'href': absolute_url('/feed.xml'), 'rel': 'self', 'type': 'application/rss+xml'})
    feed = ET.Element(f'{{{ATOM}}}feed')
    ET.SubElement(feed, f'{{{ATOM}}}title').text = 'Group Policy Central'
    ET.SubElement(feed, f'{{{ATOM}}}id').text = absolute_url('/atom.xml')
    ET.SubElement(feed, f'{{{ATOM}}}link', {'href': absolute_url('/')})
    ET.SubElement(feed, f'{{{ATOM}}}link', {'href': absolute_url('/atom.xml'), 'rel': 'self'})
    ET.SubElement(feed, f'{{{ATOM}}}subtitle').text = 'Historical tutorials, news and guidance for Windows Group Policy administrators.'
    author = ET.SubElement(feed, f'{{{ATOM}}}author')
    ET.SubElement(author, f'{{{ATOM}}}name').text = 'Group Policy Central'
    ET.SubElement(feed, f'{{{ATOM}}}updated').text = (published_date(recent[0]['date']) if recent else datetime(1970, 1, 1, tzinfo=timezone.utc)).isoformat().replace('+00:00', 'Z')
    for post in recent:
        date = published_date(post['date'])
        address = absolute_url(post['canonical_path'])
        parser = PlainText()
        parser.feed(post['html'])
        summary = ' '.join(' '.join(parser.parts).split())[:400]
        item = ET.SubElement(channel, 'item')
        for key, value in [('title', post['title']), ('link', address), ('guid', address), ('pubDate', format_datetime(date, usegmt=True)), ('description', summary)]:
            ET.SubElement(item, key).text = value
        entry = ET.SubElement(feed, f'{{{ATOM}}}entry')
        for key, value in [('title', post['title']), ('id', address), ('published', date.isoformat().replace('+00:00', 'Z')), ('updated', date.isoformat().replace('+00:00', 'Z')), ('summary', summary)]:
            ET.SubElement(entry, f'{{{ATOM}}}{key}').text = value
        ET.SubElement(entry, f'{{{ATOM}}}link', {'href': address})
    ET.ElementTree(rss).write(output_dir / 'feed.xml', encoding='utf-8', xml_declaration=True)
    ET.ElementTree(feed).write(output_dir / 'atom.xml', encoding='utf-8', xml_declaration=True)
    guide = f'''# Group Policy Central

> An independent archive of tutorials, news and field notes for Windows Group Policy administrators.

Articles are historical and may describe obsolete products or guidance. Check current Microsoft documentation before applying them.

## Browse the archive

- [Home]({absolute_url('/')})
- [Tutorials]({absolute_url('/tutorials/')})
- [Best practices]({absolute_url('/best-practices/')})
- [News]({absolute_url('/news/')})
- [Browse by year]({absolute_url('/archives/')})
- [Sitemap]({absolute_url('/sitemap.xml')})
- [RSS feed]({absolute_url('/feed.xml')})
- [Atom feed]({absolute_url('/atom.xml')})
- [About the archive]({absolute_url('/about/')})
'''
    (output_dir / 'llms.txt').write_text(guide, encoding='utf-8')
