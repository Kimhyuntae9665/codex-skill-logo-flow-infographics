import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from render_logo_flow import build, local_svg

NS = {'s': 'http://www.w3.org/2000/svg'}


class RendererContracts(unittest.TestCase):
    def test_all_examples_rebuild_with_pinned_assets(self):
        graphs = sorted((ROOT / 'examples').glob('*/graph.json'))
        self.assertEqual(len(graphs), 6)
        for graph_path in graphs:
            with self.subTest(example=graph_path.parent.name):
                svg, manifest = build(graph_path)
                graph = json.loads(graph_path.read_text(encoding='utf-8'))
                self.assertEqual(manifest['nodes'], len(graph['nodes']))
                self.assertEqual(manifest['edges'], len(graph['edges']))
                self.assertEqual(manifest['status'], 'proposed')
                self.assertEqual(svg, (graph_path.parent / 'output.svg').read_text(encoding='utf-8'))
                stored = json.loads((graph_path.parent / 'output.manifest.json').read_text(encoding='utf-8'))
                self.assertEqual(manifest, stored)

    def test_labels_below_cards_and_images_embedded(self):
        svg, _ = build(ROOT / 'examples/04-diamond/graph.json')
        tree = ET.fromstring(svg)
        for group in tree.findall('s:g', NS):
            card = group.find('s:rect', NS)
            label = group.find('s:text', NS)
            logo = group.find('s:image', NS)
            self.assertGreater(float(label.get('y')), float(card.get('y')) + float(card.get('height')))
            self.assertEqual(float(label.get('x')), float(card.get('x')) + 50)
            self.assertEqual(label.text, group.get('aria-label'))
            self.assertTrue(logo.get('{http://www.w3.org/1999/xlink}href').startswith('data:image/svg+xml;base64,'))

    def test_asset_tampering_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            (folder/'logo.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 10"/>', encoding='utf-8')
            entry = {'name':'Fixture','path':'logo.svg','sha256':'0'*64,'source':'Original fixture','license_note':'Original test fixture'}
            with self.assertRaisesRegex(ValueError, 'hash mismatch'):
                local_svg(entry, folder)

    def test_nonsquare_logo_keeps_proportions(self):
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            raw = b'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 20"><rect width="40" height="20"/></svg>'
            (folder/'logo.svg').write_bytes(raw)
            entry = {'name':'Wide','path':'logo.svg','sha256':hashlib.sha256(raw).hexdigest(),'source':'Original fixture','license_note':'Original test fixture'}
            (folder/'assets.json').write_text(json.dumps({'wide':entry}),encoding='utf-8')
            graph = {'title':'Wide fixture','status':'synthetic','basis':'Original test','description':'One wide glyph','asset_manifest':'assets.json','width':400,'height':300,'disclaimer':'Synthetic fixture','nodes':[{'id':'a','asset':'wide','x':100,'y':70}],'edges':[]}
            path = folder/'graph.json'
            path.write_text(json.dumps(graph),encoding='utf-8')
            svg, _ = build(path)
            logo = ET.fromstring(svg).find('s:g/s:image', NS)
            self.assertEqual(float(logo.get('width')), 64)
            self.assertEqual(float(logo.get('height')), 32)
            self.assertEqual(float(logo.get('y')), 104)

    def modified_graph(self, change, error):
        # Keep the original asset path because this temporary graph lives elsewhere.
        graph = json.loads((ROOT/'examples/01-linear/graph.json').read_text(encoding='utf-8'))
        graph['asset_manifest'] = str(ROOT/'examples/assets/manifest.json')
        change(graph)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/'graph.json'
            path.write_text(json.dumps(graph),encoding='utf-8')
            with self.assertRaisesRegex(ValueError, error):
                build(path)

    def test_backwards_edge_rejected(self):
        self.modified_graph(lambda g: g.update(edges=[{'source':'db','target':'ui'}]), 'forward left-to-right')

    def test_proposal_requires_disclaimer(self):
        self.modified_graph(lambda g: g.pop('disclaimer'), 'explicit disclaimer')

    def test_wrong_brand_label_rejected(self):
        self.modified_graph(lambda g: g['nodes'][0].update(label='Wrong brand'), 'accurate name')

    def test_external_resource_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            raw = b'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><use href="https://example.invalid/external.svg"/></svg>'
            (folder/'logo.svg').write_bytes(raw)
            entry = {'name':'Fixture','path':'logo.svg','sha256':hashlib.sha256(raw).hexdigest(),'source':'Original fixture','license_note':'Original test fixture'}
            with self.assertRaisesRegex(ValueError, 'internal SVG references'):
                local_svg(entry, folder)


if __name__ == '__main__':
    unittest.main()
