# The long yard walls the user's captures show where the map has no building at all (the per-house notes: casas/*.json,
# «tapia … en el mapa no hay edificio ahí»): for each, the view it was seen from, the side, how far along, its height,
# what it is made of and its colour — written by hand below from those notes. From the view's camera (fitted where
# Google's GPS was off: .cache/calles/camaras.json) along its axis, metre by metre, the street beside it and the line its
# houses would stand on (half the carriageway and the pavement out), wherever no building stands: the wall's line, in
# the game's metres. Numbers and words only. → src/calles_tapias.js (tapias.js builds them)
#   python3 tools/fachadas/tapias.py
import json, math, os
REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
M = json.load(open(os.path.join(REPO, 'data', 'map.json')))
P = json.load(open(os.path.join(REPO, '.cache', 'calles', 'poses.json')))
try: C = json.load(open(os.path.join(REPO, '.cache', 'calles', 'camaras.json')))
except Exception: C = {}

# (view, side, from, to (m along its axis), height (m), made of, colour, gate colour or None) — the notes, abridged
TAPIAS = [
    (63, 'izq', 0, 30, 6.0, 'enfoscado', '#b9966f', None),     # Fuentes: a high wall of old ochre render, rust stains
    (73, 'der', 15, 25, 2.6, 'cal', '#eeebe3', '#f2f0ea'),     # Hornillos: whitewashed, a coping of red brick, a white door
    (75, 'izq', 0, 30, 2.2, 'ladrillo', '#c98a5f', None),      # Hornillos: hollow orange brick, unrendered, before a lot
    (88, 'izq', 0, 30, 3.0, 'cal', '#eeebe3', None),           # Pozo Dulce: the long wall of a yard
    (89, 'izq', 0, 30, 2.2, 'piedra', '#ddd4c2', None),        # Pozo Pajares: stone blocks, faded lime, at the pavement
    (34, 'der', 0, 30, 2.5, 'piedra', '#b29b80', None),        # Cuesta: rubble and rammed earth, never whitewashed
    (40, 'izq', 0, 12, 2.6, 'cal', '#efede6', None),           # Derecha: the white wall before the houses
    (46, 'izq', 0, 8, 2.6, 'cal', '#efede6', '#5a3a24'),       # Don Manuel Dorado: the wall before the houses, its gate
]

B = [[v / 10 for v in b['p']] for b in M['buildings']]
G, CELL = {}, 20.0
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
def building_at(x, z):
    return any(inside(x, z, B[i]) for i in G.get((int(math.floor(x / CELL)), int(math.floor(z / CELL))), []))
E = []
for e in M['edges']:
    if e.get('n', -1) < 0 and not e.get('w'): continue
    p = [v / 10 for v in e['p']]
    E.append((list(zip(p[0::2], p[1::2])), e.get('w', 50) / 10, e.get('sw', 10) / 10))
def nearest(x, z):
    best = None
    for pts, w, sw in E:
        for (ax, az), (bx, bz) in zip(pts, pts[1:]):
            dx, dz = bx - ax, bz - az; L2 = dx * dx + dz * dz or 1e-9
            t = max(0, min(1, ((x - ax) * dx + (z - az) * dz) / L2)); qx, qz = ax + dx * t, az + dz * t
            d = math.hypot(x - qx, z - qz)
            if best is None or d < best[0]: L = math.sqrt(L2); best = (d, qx, qz, dx / L, dz / L, w, sw)
    return best

out = []
for vid, side, t0, t1, h, mat, col, gate in TAPIAS:
    v = dict(P[vid]); v.update(C.get(str(vid), {}))
    hd = math.radians(v['heading'])
    fx, fz = math.sin(hd), -math.cos(hd)
    sx, sz = math.cos(hd) * (1 if side == 'der' else -1), math.sin(hd) * (1 if side == 'der' else -1)
    run, runs = [], []
    t = t0 + 0.5
    while t <= t1:
        cx, cz = v['x'] + fx * t, v['z'] + fz * t
        d, qx, qz, ux, uz, w, sw = nearest(cx, cz)
        nx, nz = -uz, ux
        if nx * sx + nz * sz < 0: nx, nz = -nx, -nz
        off = w / 2 + max(sw, 0.9) + 0.1
        px, pz = qx + nx * off, qz + nz * off
        if building_at(px, pz) or building_at(px + nx * 0.4, pz + nz * 0.4):
            if len(run) > 1: runs.append(run)
            run = []
        else: run.append([round(px, 2), round(pz, 2), round(nx, 3), round(nz, 3)])  # (and which way is away from the street)
        t += 1.0
    if len(run) > 1: runs.append(run)
    for r in runs:
        out.append({'pts': r, 'h': h, 'mat': mat, 'col': col, **({'gate': gate} if gate else {}), 'vista': vid})
    print(vid, side, mat, [len(r) for r in runs])
js = ["// The long yard walls the user's Google Maps captures show where the map has no building (2026-10-13): their line in",
      "// the game's metres, their height, what they are made of and their colour — tools/fachadas/tapias.py, from the",
      "// per-house notes. Nothing of the captures is in it. Built by tapias.js.",
      'export const TAPIAS = [']
for o in out: js.append('  ' + json.dumps(o, ensure_ascii=False) + ',')
js.append('];')
open(os.path.join(REPO, 'src', 'calles_tapias.js'), 'w').write('\n'.join(js) + '\n')
print(len(out), 'tapias')
