# The medians the map has no room for (2026-10-13): the Calle Don Benito is two carriageways either side of a raised
# median with a row of young trees (its captures, views 171–173), and the map has its two one-way carriageways (edges
# 436 east, 442 and 443 west) drawn on top of each other along that median, 14–17 m wide each — the game made one wide
# road of them, its traffic driving down the row of trees. Here: the median's line, from the crowns of its trees as the
# PNOA orthophoto shows them (tools/aceras/pnoa.py, measured by eye on a 2 m grid: numbers only, the tiles stay in
# .cache), and each carriageway moved to its own side of it, 6 m wide, its ends left at the junctions they meet. →
# src/calles_medianas.js (mapdata.js moves the carriageways, ground.js and townplus.js lay the median)
#   python3 tools/fachadas/medianas.py
import json, math, os
REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
M = json.load(open(os.path.join(REPO, 'data', 'map.json')))

# the crowns of the median's trees (x, z), west to east; the median breaks for the crossing at x 567–590
TREES = [(479.1, -67.3), (485.1, -65.8), (492.6, -65.4), (498.7, -64.5), (508.5, -64.3), (519.6, -64.1), (532.3, -62.9),
         (538.1, -62.8), (543.5, -62.6), (549.5, -61.7), (555.6, -61.7), (560.7, -61.4), (566.7, -60.9),
         (589.9, -60.7), (594.4, -59.9), (601.0, -59.2), (606.4, -59.4), (614.6, -58.3), (620.6, -59.0), (627.0, -57.9),
         (634.0, -57.6), (640.0, -57.2), (645.7, -57.6), (651.7, -56.8), (658.4, -56.1), (665.0, -55.7), (673.4, -55.7),
         (678.0, -55.3), (684.0, -54.9)]
HALF = 1.1     # the median, 2.2 m kerb to kerb
CW = 6.0       # each carriageway, kerb to kerb (a lane and the cars parked along the houses)
OFF = HALF + CW / 2
PIECES = [(476.0, 567.0, '#c4beb2', 'adoquin'), (590.0, 687.0, '#c9c1b2', 'losa')]  # (light grey setts, their trees in pits; the east piece in grey-beige slabs, view 172)
KERB = '#9a958c'  # (its kerbs of grey granite, views 172, 54 — not the white of the town's)
RED = {'desde': 67, 'hasta': 99, 'col': '#b46e5c', 'suelo': 'losa'}  # (the east piece's last 30 m: red concrete tiles, view 173)
X0, X1 = 463.0, 706.0  # the junctions at either end

# the line: a quadratic through the crowns (the street bends a little), z(x)
n = len(TREES)
sx = [sum(t[0] ** k for t in TREES) for k in range(5)]
sy = [sum(t[1] * t[0] ** k for t in TREES) for k in range(3)]
A = [[sx[i + j] for j in range(3)] for i in range(3)]
def solve(A, b):
    A = [r[:] + [v] for r, v in zip(A, b)]
    for i in range(3):
        p = max(range(i, 3), key=lambda r: abs(A[r][i])); A[i], A[p] = A[p], A[i]
        for r in range(3):
            if r != i:
                f = A[r][i] / A[i][i]
                A[r] = [a - f * c for a, c in zip(A[r], A[i])]
    return [A[i][3] / A[i][i] for i in range(3)]
c0, c1, c2 = solve(A, sy)
z = lambda x: c0 + c1 * x + c2 * x * x
res = [t[1] - z(t[0]) for t in TREES]
print('median fit: rms %.2f m, max %.2f m' % (math.sqrt(sum(r * r for r in res) / n), max(abs(r) for r in res)))
def line(xa, xb, off=0.0, step=3.0):
    k = max(1, int(round(abs(xb - xa) / step)))
    out = []
    for i in range(k + 1):
        x = xa + (xb - xa) * i / k
        d = c1 + 2 * c2 * x; L = math.hypot(1, d)
        nx, nz = -d / L, 1 / L  # (the normal towards +z: south)
        out.append([round(x + nx * off, 2), round(z(x) + nz * off, 2)])
    return out

node = lambda i: [M['nodes'][i * 2] / 10, M['nodes'][i * 2 + 1] / 10]
E = M['edges']
# each carriageway: its own junction at each end, its own side of the median between (eastbound south, westbound north:
# they keep to the right); its pavement on the houses' side only (+1 is the side to (−dz, dx)), its cars parked there
calzadas = {
    436: {'pts': [node(E[436]['a'])] + line(478, 688, +OFF) + [node(E[436]['b'])]},
    443: {'pts': [node(E[443]['a'])] + line(570, 478, -OFF) + [node(E[443]['b'])]},
    442: {'pts': [node(E[442]['a'])] + line(688, 588, -OFF) + [node(E[442]['b'])]},
}
for k, c in calzadas.items():
    c.update({'w': CW, 'sp': 1.6, 'sm': 0, 'park': 1})
    p = c['pts']; print(k, len(p), 'pts', p[0], '→', p[-1])
bulevar = []
for i, (xa, xb, col, suelo) in enumerate(PIECES):
    b = {'pts': line(xa, xb), 'ancho': 2 * HALF, 'col': col, 'suelo': suelo, 'arbol': ['platano', 'ciruelo'], 'cada': 7.5, 'escala': 0.55,
         'farolas': {'cada': 30, 'kind': 'baculo'}, 'bordillo': KERB}
    if i == 0: b['base'] = {'pts': line(X0, X1), 'ancho': 2 * HALF + 0.6}  # (asphalt under it, from junction to junction)
    if i == 1: b['tramos'] = [RED]
    bulevar.append(b)
# ---- the Calle El Rollo (2026-10-15, views 154–156): its two one-way carriageways drawn on top of each other as well
# (edges 426–431 south-east, 454–459 north-west, 12–17 m wide each), and the PNOA shows its median's young trees right
# on that line, from its west end to the last junction east, broken at each crossing. The median down the mean of the
# two lines, 1.4 m kerb to kerb; each carriageway 6.2 m on its own side (they keep to the right), its ends at its
# junctions; 18.9 m between the fronts, so a pavement of 2.2 m on the houses' side
RA, RB = [426, 427, 428, 429, 430, 431], [454, 455, 456, 457, 458, 459]
R_HALF, R_CW = 0.7, 6.2
R_OFF, R_T, R_GAP = R_HALF + R_CW / 2, 8.0, 10.0  # (each carriageway eases out over 8 m from its junction; the median stops 10 m short)
def chain(ids):
    P = []
    for i in ids:
        p = [v / 10 for v in E[i]['p']]; q = list(zip(p[0::2], p[1::2]))
        P += q if not P else q[1:]
    return P
def cumof(P):
    c = [0.0]
    for (ax, az), (bx, bz) in zip(P, P[1:]): c.append(c[-1] + math.hypot(bx - ax, bz - az))
    return c
def sample(P, c, s):
    s = max(0.0, min(c[-1], s))
    for i in range(len(P) - 1):
        if c[i + 1] >= s:
            t = (s - c[i]) / max(1e-9, c[i + 1] - c[i]); (ax, az), (bx, bz) = P[i], P[i + 1]
            L = max(1e-9, c[i + 1] - c[i])
            return ax + (bx - ax) * t, az + (bz - az) * t, (bx - ax) / L, (bz - az) / L
    (ax, az), (bx, bz) = P[-2], P[-1]; L = math.hypot(bx - ax, bz - az) or 1
    return bx, bz, (bx - ax) / L, (bz - az) / L
def nearest_on(P, x, z):
    best = None
    for (ax, az), (bx, bz) in zip(P, P[1:]):
        dx, dz = bx - ax, bz - az; L2 = dx * dx + dz * dz or 1e-9
        t = max(0, min(1, ((x - ax) * dx + (z - az) * dz) / L2)); q = (ax + dx * t, az + dz * t)
        d = math.hypot(x - q[0], z - q[1])
        if best is None or d < best[0]: best = (d, q)
    return best[1]
A_, B_ = chain(RA), chain(RB)[::-1]
ca = cumof(A_)
AX = []
for k in range(int(ca[-1] // 2) + 1):
    x, z, _, _ = sample(A_, ca, k * 2.0); qx, qz = nearest_on(B_, x, z); AX.append(((x + qx) / 2, (z + qz) / 2))
AX = [AX[0]] + [tuple(sum(p[j] for p in AX[i - 2:i + 3]) / 5 for j in (0, 1)) for i in range(2, len(AX) - 2)] + [AX[-1]]  # (a little smoothed)
cx_ = cumof(AX)
def s_of(x, z):
    best = None
    for i, ((ax, az), (bx, bz)) in enumerate(zip(AX, AX[1:])):
        dx, dz = bx - ax, bz - az; L2 = dx * dx + dz * dz or 1e-9
        t = max(0, min(1, ((x - ax) * dx + (z - az) * dz) / L2)); d = math.hypot(x - ax - dx * t, z - az - dz * t)
        if best is None or d < best[0]: best = (d, cx_[i] + t * math.sqrt(L2))
    return best[1]
def rline(s0, s1, off, step=3.0):
    k = max(1, int(round(abs(s1 - s0) / step))); out = []
    for i in range(k + 1):
        x, z, dx, dz = sample(AX, cx_, s0 + (s1 - s0) * i / k)
        out.append([round(x - dz * off, 2), round(z + dx * off, 2)])  # (off along (−dz, dx): the right of the axis's run, south-east)
    return out
for ids, sgn in ((RA, 1), (RB, -1)):
    for i in ids:
        a, b = node(E[i]['a']), node(E[i]['b']); sa, sb = s_of(*a), s_of(*b)
        if abs(sb - sa) < 2 * R_T + 4: continue  # (a stretch between two crossings close together: left as it is)
        d = 1 if sb > sa else -1
        pts = [a] + rline(sa + d * R_T, sb - d * R_T, sgn * R_OFF) + [b]
        calzadas[i] = {'pts': pts, 'w': R_CW, 'sp': 2.2, 'sm': 0, 'park': 1}
        print(i, 'El Rollo', len(pts), 'pts', round(abs(sb - sa)), 'm')
cuts = sorted({round(s_of(*node(E[i][k])), 1) for i in RA for k in ('a', 'b')})
rollo = []
for s0, s1 in zip(cuts, cuts[1:]):
    if s1 - s0 < 2 * R_GAP + 12: continue
    rollo.append({'pts': rline(s0 + R_GAP, s1 - R_GAP, 0.0), 'ancho': 2 * R_HALF, 'col': '#a9a59c', 'suelo': 'adoquin', 'arbol': ['morera', 'ciruelo'],
                  'cada': 7.5, 'escala': 0.45, 'farolas': {'cada': 27, 'kind': 'baculo'}, 'bordillo': '#a8a49d'})
rollo[0]['base'] = {'pts': rline(0, cx_[-1], 0.0), 'ancho': 2 * R_HALF + 0.6}  # (asphalt under it, end to end)
print('El Rollo: median', len(rollo), 'pieces', [round(cumof([tuple(p) for p in b['pts']])[-1]) for b in rollo], 'm')
js = ["// The medians the map has no room for (2026-10-13): tools/fachadas/medianas.py — the line of each, from the crowns of",
      "// its trees on the PNOA orthophoto (numbers only), and its two carriageways moved to either side of it (mapdata.js).",
      "// CALZADAS: by edge index — its points, width, pavements (+ side, − side) and the side its cars park on.",
      'export const CALZADAS = {']
for k in sorted(calzadas): js.append(f'  {k}: {json.dumps(calzadas[k])},')
js += ['};', "// the medians themselves, as a street's style's bulevar (calles.js): ground.js lays them, townplus.js plants them",
       'export const BULEVARES = {', f"  'Calle Don Benito': {json.dumps(bulevar, ensure_ascii=False)},", f"  'Calle El Rollo': {json.dumps(rollo, ensure_ascii=False)},", '};']
open(os.path.join(REPO, 'src', 'calles_medianas.js'), 'w').write('\n'.join(js) + '\n')
print('ok')
