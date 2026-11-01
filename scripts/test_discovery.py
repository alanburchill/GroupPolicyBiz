"""Check discovery output for origin, XML escaping and feed dates."""
import tempfile
import unittest
from pathlib import Path
from xml.etree import ElementTree as ET

from generate_discovery import write_discovery


class DiscoveryTests(unittest.TestCase):
    def test_feeds_and_guide_use_build_origin(self):
        posts = [{'title': 'Policies & settings', 'date': '2020-01-02T03:04:05+10:00',
                  'canonical_path': '/2020/01/example/', 'html': '<p>A &amp; B</p>'}]
        for origin in ('https://example.pages.dev', 'https://grouppolicy.biz'):
            with self.subTest(origin=origin), tempfile.TemporaryDirectory() as tmp:
                path = Path(tmp)
                write_discovery(path, posts, lambda suffix: origin + suffix)
                rss = ET.parse(path / 'feed.xml').getroot()
                item = rss.find('./channel/item')
                self.assertEqual(item.findtext('title'), 'Policies & settings')
                self.assertEqual(item.findtext('description'), 'A & B')
                self.assertEqual(item.findtext('link'), origin + '/2020/01/example/')
                self.assertEqual(item.findtext('pubDate'), 'Wed, 01 Jan 2020 17:04:05 GMT')
                atom = ET.parse(path / 'atom.xml').getroot()
                ns = {'a': 'http://www.w3.org/2005/Atom'}
                self.assertEqual(atom.findtext('a:entry/a:published', namespaces=ns), '2020-01-01T17:04:05Z')
                self.assertEqual(atom.find('a:entry/a:link', ns).get('href'), origin + '/2020/01/example/')
                self.assertIn(origin + '/feed.xml', (path / 'llms.txt').read_text(encoding='utf-8'))


if __name__ == '__main__':
    unittest.main()
