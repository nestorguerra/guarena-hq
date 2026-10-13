# The buildings each capture's camera sees along the street, side by side and in order (tools/fachadas/capturas.py
# poses): walking up the view's axis, at every half metre the first Catastro building a sideways ray meets on the left
# and on the right — so «the 2nd house on the right» of a capture is a building of the map.
#   python3 tools/fachadas/lados.py [view ids…]   → .cache/calles/lados.json  {view: {izq: [{bid, t0, t1, d}], der: […]}}
import json, math, os, sys
REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
M = json.load(open(os.path.join(REPO, 'data', 'map.json')))
P = json.load(open(os.path.join(REPO, '.cache', 'calles', 'poses.json')))
B = [[v / 10 for v in b['p']] for b in M['buildings']]
# a coarse grid of the buildings' bounding boxes
G = {}
CELL = 20.0
for i, r in enumerate(B):
    xs, zs = r[0::2], r[1::2]
    for gx in range(int(math.floor(min(xs) / CELL)), int(math.floor(max(xs) / CELL)) + 1):
        for gz in range(int(math.floor(min(zs) / CELL)), int(math.floor(max(zs) / CELL)) + 1):
            G.setdefault((gx, gz), []).append(i)
def inside(x, z, r):
    n = len(r) // 2; c = False; j = n - 1
    for i in range(n):
        xi, zi, xj, zj = r[i * 2], r[i * 2 + 1], r[j * 2], r[j * 2 + 1]
        if (zi > z) != (zj > z) and x < (xj - xi) * (z - zi) / (zj - zi + 1e-12) + xi: c = not c
        j = i
    return c
def at(x, z):
    for i in G.get((int(math.floor(x / CELL)), int(math.floor(z / CELL))), []):
        if inside(x, z, B[i]): return i
    return None
def side_list(v, sgn, far=45.0, reach=14.0):
    h = math.radians(v['heading'])
    fx, fz = math.sin(h), -math.cos(h)          # forward (compass heading; z points south)
    rx, rz = math.cos(h) * sgn, math.sin(h) * sgn  # right (sgn 1) or left (sgn −1)
    seq = []
    t = 0.5
    while t < far:
        cx, cz = v['x'] + fx * t, v['z'] + fz * t
        hit = None; dd = None
        s = 0.5
        while s < reach:
            b = at(cx + rx * s, cz + rz * s)
            if b is not None: hit, dd = b, s; break
            s += 0.25
        if hit is not None:
            if seq and seq[-1]['bid'] == hit: seq[-1]['t1'] = t; seq[-1]['d'] = min(seq[-1]['d'], dd)
            else: seq.append({'bid': hit, 't0': t, 't1': t, 'd': dd})
        t += 0.5
    return [q for q in seq if q['t1'] - q['t0'] >= 1.0 or q['d'] < 6]
ids = [int(a) for a in sys.argv[1:]] or [p['id'] for p in P]
out = {}
for i in ids:
    v = P[i]
    out[i] = {'folder': v['folder'], 'file': v['file'], 'izq': side_list(v, -1), 'der': side_list(v, 1)}
path = os.path.join(REPO, '.cache', 'calles', 'lados.json')
old = {}
try: old = json.load(open(path))
except Exception: pass
old.update({str(k): v for k, v in out.items()})
json.dump(old, open(path, 'w'), ensure_ascii=False, indent=1)
for i in ids[:3]:
    print(i, out[i]['folder'], 'izq', [(q['bid'], q['t0'], q['t1']) for q in out[i]['izq']][:6], 'der', [(q['bid'], q['t0'], q['t1']) for q in out[i]['der']][:6])
print(len(ids), 'vistas')
