# The captures' cameras where they really stood. Google's GPS puts many of them metres off — inside a house, against a
# front, in the next street — and the links of the Maps API give the point asked for, not the panorama's: the agents
# that matched houses to buildings put each such camera back where its corners and party walls fall on the map's
# (one JSON per group of streets: {view: {x, z, heading, eye, nota}}). Merged here into .cache/calles/camaras.json,
# which tools/callelab.js lays over the poses (numbers only, outside the repository, like the poses).
#   python3 tools/fachadas/camaras.py <dir of fitted cameras>
import json, os, sys
REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SRC = sys.argv[1]
P = json.load(open(os.path.join(REPO, '.cache', 'calles', 'poses.json')))
out = {}
for f in sorted(os.listdir(SRC)):
    if not f.endswith('.json'): continue
    for k, c in json.load(open(os.path.join(SRC, f))).items():
        try: i = int(k)
        except ValueError: continue
        if not (0 <= i < len(P)) or not all(isinstance(c.get(a), (int, float)) for a in ('x', 'z')): continue
        v = P[i]
        moved = ((c['x'] - v['x']) ** 2 + (c['z'] - v['z']) ** 2) ** 0.5
        if moved > 40: print('vista', i, 'movida', round(moved, 1), 'm: no se toma', f); continue
        out[str(i)] = {'x': round(float(c['x']), 2), 'z': round(float(c['z']), 2), 'heading': float(c.get('heading', v['heading'])),
                       'eye': float(c.get('eye') or 2.5), 'moved': round(moved, 1), 'from': f[:-5]}
        if isinstance(c.get('fov'), (int, float)): out[str(i)]['fov'] = float(c['fov'])
json.dump(out, open(os.path.join(REPO, '.cache', 'calles', 'camaras.json'), 'w'), ensure_ascii=False, indent=1)
print(len(out), 'cámaras recolocadas; media', round(sum(o['moved'] for o in out.values()) / max(1, len(out)), 1), 'm')
