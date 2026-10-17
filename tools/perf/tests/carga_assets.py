#!/usr/bin/env python3
"""Read-only contracts for an already built package; does not build or open a browser.

After a normal build:
  python3 tools/perf/tests/carga_assets.py
After a --split build in an isolated checkout:
  python3 tools/perf/tests/carga_assets.py --root /path/to/checkout --split

Functional check planned after applying the proposal (not performed by this test):
- Open Pages' dist/test.html?estilo=real in a fresh private browser context,
  quality alta, with the complete introduction and no fast-forward.
- Require successful HTTP responses and nonempty bodies for all 12 ground JPEGs;
  groundFx.on and groundFx.normals must be true. Inspect the ground at the same
  camera/hour/quality as the baseline and reject missing or changed textures.
- Require hiper:iglesia in the scene and successful loading of hq/iglesia.glb.
- Repeat Plastilina: no requests for these 12 JPEGs, normal introduction, no errors.
- Run the alternate cold-load A/B later. Fewer bytes do not certify 25% faster load.
"""
import argparse
import json
from pathlib import Path
import re
import runpy

# An explicit contract independent of build.py's selection logic.
GROUND = (
    'tex/asphalt_02_d.jpg', 'tex/asphalt_02_n.jpg',
    'tex/dirty_concrete_d.jpg', 'tex/dirty_concrete_n.jpg',
    'tex/dry_ground_01_d.jpg', 'tex/dry_ground_01_n.jpg',
    'tex/gravel_floor_02_d.jpg', 'tex/gravel_floor_02_n.jpg',
    'tex/sparse_grass_d.jpg', 'tex/sparse_grass_n.jpg',
    'tex/withered_grass_d.jpg', 'tex/withered_grass_n.jpg',
)
PATHS = ('hq/iglesia.glb',) + GROUND
VARIANTS = ('dist/test.html', 'dist/guarena-hq.html', 'multijugador/guarena.html')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument('--split', action='store_true')
    args = parser.parse_args()
    root = args.root.resolve()
    # run_path does not invoke main; reuse the encoder without executing a build.
    encode = runpy.run_path(str(root / 'tools/build.py'))['b85']
    source = {rel: (root / 'assets' / rel).read_bytes() for rel in PATHS}
    expected = {rel: encode(data) for rel, data in source.items()} if not args.split else {}
    for rel, data in source.items():
        assert (root / 'dist/assets' / rel).read_bytes() == data, 'External bytes differ: ' + rel
    for variant in VARIANTS:
        html = (root / variant).read_text()
        matches = re.findall(r'<script type="application/json" id="assetdata">(.*?)</script>', html, re.S)
        if args.split:
            assert not matches, 'Split build unexpectedly embeds assets: ' + variant
            continue
        assert len(matches) == 1, 'Missing or duplicate assetdata: ' + variant
        assets = json.loads(matches[0])
        assert assets.get('__enc') == 'b85', 'Unexpected encoding: ' + variant
        portable = variant != 'dist/test.html'
        for rel in PATHS:
            assert (rel in assets) == portable, 'Wrong embedded presence: ' + variant + ' / ' + rel
            if portable:
                assert assets[rel] == expected[rel], 'Embedded bytes differ: ' + variant + ' / ' + rel
    print('PASS: 12 ground JPEGs + church, 3 HTML variants, exact external/embedded bytes; split=' + str(args.split))


if __name__ == '__main__':
    main()
