# Santa María's furniture in high definition (docs/hiperrealismo.md, «La 6b: los muebles»): the pews, the presbytery,
# the retablos, the pulpit, the confessionals, the font, the organ — each a function, at src/church.js's measures and
# places (its colliders, its seats and the mass keep fitting). Built inside interior.py's Blender run (--muebles-hd):
# they are baked with the architecture (their own lightmap islands) and exported with it.
#   build(K) → objects; K is interior.py's namespace (its Mesh, its roles, its measures)
import math
from mathutils import Vector

K = None  # (interior.py's module, set by build)

# ---------------------------------------------------------------- shapes with rounded edges and their UVs
def rrect(w, h, r, seg=2):
    """a rectangle w × h (centred), its corners rounded r — a closed outline, counter-clockwise"""
    r = min(r, w / 2 - 1e-4, h / 2 - 1e-4)
    pts = []
    for cx, cy, a0 in ((w / 2 - r, h / 2 - r, 0.0), (-w / 2 + r, h / 2 - r, 90.0), (-w / 2 + r, -h / 2 + r, 180.0), (w / 2 - r, -h / 2 + r, 270.0)):
        for k in range(seg + 1):
            a = math.radians(a0 + 90.0 * k / seg)
            pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts

def perimeter(pts, closed=True):
    s = [0.0]
    for i in range(1, len(pts)): s.append(s[-1] + math.dist(pts[i], pts[i - 1]))
    if closed: s.append(s[-1] + math.dist(pts[0], pts[-1]))
    return s

def bar(name, role, a, b, across, up, prof):
    """a bar along a → b (church frame): its cross-section `prof` [(across, up)] closed and swept straight, its ends
    capped. UVs in metres with the grain along the bar (u = along); the light's atlas, one island round it"""
    a, b = Vector(a), Vector(b); X, Y = Vector(across).normalized(), Vector(up).normalized()
    L = (b - a).length; per = perimeter(prof)
    m = K.Mesh(name, role); rows, uvs = [], []
    for t in (0.0, 1.0):
        p = a + (b - a) * t
        row = [m.vert(p + X * u + Y * v) for u, v in prof]; row.append(row[0])
        rows.append(row); uvs.append([(t * L, per[k]) for k in range(len(prof) + 1)])
    for i in range(len(prof)):
        uv = [uvs[0][i], uvs[0][i + 1], uvs[1][i + 1], uvs[1][i]]
        lm = [(q[1], q[0]) for q in uv]
        m.face([rows[0][i], rows[0][i + 1], rows[1][i + 1], rows[1][i]], uvs=uv, lm=lm)
    cap = [(u, v) for u, v in prof]
    m.face(rows[0][:len(prof)][::-1], uvs=[(v, u) for u, v in cap][::-1])
    m.face(rows[1][:len(prof)], uvs=[(v, u) for u, v in cap])
    return K.closed(m.build())

def board(name, role, outline, origin, U, V, N, t, r=0.006, seg=2, grain='v'):
    """a board: a flat outline [(u, v)] on the plane (origin, U, V), thickness t along N (centred), its edges rounded r.
    Its edge is a band swept round the outline (one island in the light's atlas), its two faces flat; the grain along
    its v (or u)"""
    o, U, V = Vector(origin), Vector(U).normalized(), Vector(V).normalized()
    N = U.cross(V).normalized()   # (its faces turned by the outline's own sense: the thickness is centred, N's sign free)
    r = min(r, t * 0.45)          # (a rounding of half the thickness or more would fold the edge on itself)
    n = len(outline)
    # the outline's outward normals (in u, v), averaged at each corner
    def nrm(i):
        (x0, y0), (x1, y1) = outline[i], outline[(i + 1) % n]
        dx, dy = x1 - x0, y1 - y0; l = math.hypot(dx, dy) or 1.0
        return (dy / l, -dx / l)   # (counter-clockwise outline: right of the direction is out)
    ns = []
    for i in range(n):
        a, b = nrm(i - 1), nrm(i)
        x, y = a[0] + b[0], a[1] + b[1]; l = math.hypot(x, y) or 1.0
        c = max(0.35, (a[0] * x + a[1] * y) / l)   # (a corner's offset grows as 1/cos of half its angle)
        ns.append((x / l / c, y / l / c))
    # the edge's profile, from the front face round to the back: (in, along N)
    prof = []
    for k in range(seg + 1):
        a = math.radians(90.0 * k / seg); prof.append((-r + r * math.sin(a), t / 2 - r + r * math.cos(a)))
    for k in range(seg + 1):
        a = math.radians(90.0 * k / seg); prof.append((-r + r * math.cos(a), -t / 2 + r - r * math.sin(a)))
    m = K.Mesh(name, role)
    rows = []
    for i in range(n + 1):
        j = i % n; (u, v), (nu, nv) = outline[j], ns[j]
        rows.append([m.vert(o + U * (u + nu * d) + V * (v + nv * d) + N * w) for d, w in prof])
    per = perimeter(outline); ple = perimeter([(d, w) for d, w in prof], closed=False)
    for i in range(n):
        for k in range(len(prof) - 1):
            uv = [(per[i], ple[k]), (per[i + 1], ple[k]), (per[i + 1], ple[k + 1]), (per[i], ple[k + 1])]
            m.face([rows[i][k], rows[i + 1][k], rows[i + 1][k + 1], rows[i][k + 1]], uvs=uv, lm=uv)
    gu = (lambda u, v: (v, u)) if grain == 'v' else (lambda u, v: (u, v))
    front = [rows[i][0] for i in range(n)]; back = [rows[i][-1] for i in range(n)]
    fuv = [gu(outline[i][0] + ns[i][0] * prof[0][0], outline[i][1] + ns[i][1] * prof[0][0]) for i in range(n)]
    m.face(front, uvs=fuv); m.face(back[::-1], uvs=fuv[::-1])
    return K.closed(m.build())

def cushion(name, role, a, b, across, up, w, h, seg=4):
    """a padded cushion along a → b: its section a rounded loaf w × h (flat underneath)"""
    prof = []
    for k in range(seg * 2 + 1):
        t = math.pi * k / (seg * 2)
        prof.append((w / 2 * math.cos(t), h * 0.15 + h * 0.85 * math.sin(t) ** 0.7))
    prof.append((-w / 2, 0.0)); prof.append((w / 2, 0.0))
    return bar(name, role, a, b, across, up, prof)

# ---------------------------------------------------------------- the pews
def pew_positions():
    """church.js's pews: from 2 m in front of the choir to the first step, 0,98 m apart, the aisle from door to door left
    clear; two blocks, from 1,25 m to 7 m off the axis"""
    xa, xb = K.XC + K.DOOR_BAY * K.BAY, K.XC + (K.DOOR_BAY + 1) * K.BAY
    out, x = [], K.XC + 2.0
    while x < K.XP - 1.2:
        if not (xa + 1.6 < x < xb - 1.6): out.append(x)
        x += 0.98
    return out

END = [(0.3, 0.0), (0.3, 0.6), (0.29, 0.68), (0.25, 0.725), (0.2, 0.74), (0.02, 0.75), (-0.07, 0.77), (-0.14, 0.82),
       (-0.18, 0.9), (-0.2, 0.98), (-0.22, 1.035), (-0.26, 1.055), (-0.3, 1.02), (-0.31, 0.0)]  # (church.js's scroll)

def pew(x, s, zIn=1.25, zOut=None):
    """one pew of oak: two scrolled ends (the aisle's with a fielded panel), the seat with its rounded front, a panelled
    back leaning 7°, its top rail where hands rest, the shelf for the missals behind it, a stretcher low down; and the
    padded kneeler in front"""
    zOut = zOut if zOut is not None else K.HW - 1.0
    z0, z1 = s * zIn, s * zOut
    za, zb = min(z0, z1), max(z0, z1)
    obs = []
    nm = f'banco_{x:.2f}_{s:+d}'
    X, Y, Z = Vector((1, 0, 0)), Vector((0, 1, 0)), Vector((0, 0, 1))
    lean = 0.13; ux, uy = -math.sin(lean), math.cos(lean)   # (the back's up, leaning towards −x)
    UPB, ACB = Vector((ux, uy, 0)), Vector((uy, -ux, 0))   # (its up and its across, in x-y)
    # the ends, at the block's two sides
    for e, ze in ((0, za - 0.03), (1, zb + 0.03)):
        aisle = (s > 0 and e == 0) or (s < 0 and e == 1)
        obs.append(board(f'{nm}_testero{e}', 'madera', END, (x - 0.02, 0, ze), X, Y, Z, 0.055, r=0.008, grain='v'))
        if aisle:   # the fielded panel on the aisle side: a raised field and its moulded frame
            side = -s   # (towards the central aisle)
            zf = ze + side * 0.0275
            pan = [(-0.19, 0.13), (0.19, 0.13), (0.19, 0.55), (-0.19, 0.55)]
            obs.append(board(f'{nm}_cuarteron{e}', 'madera', pan, (x - 0.02, 0, zf + side * 0.006), X, Y, Z, 0.012, r=0.005, grain='v'))
            fld = [(-0.15, 0.17), (0.15, 0.17), (0.15, 0.51), (-0.15, 0.51)]
            obs.append(board(f'{nm}_campo{e}', 'madera', fld, (x - 0.02, 0, zf + side * 0.016), X, Y, Z, 0.012, r=0.006, seg=3, grain='v'))
    zl, zr = za - 0.003, zb + 0.003
    sect = lambda w, h, r: rrect(w, h, r)
    # the seat, its front rounded
    obs.append(bar(f'{nm}_asiento', 'madera', (x + 0.01, 0.44, zl), (x + 0.01, 0.44, zr), X, Y, rrect(0.42, 0.045, 0.02, 3)))
    # the back: a board leaning, its rails, the top rail
    bc = Vector((x - 0.22, 0.73, 0))
    obs.append(bar(f'{nm}_respaldo', 'madera', bc + Vector((0, 0, zl)), bc + Vector((0, 0, zr)), ACB, UPB, rrect(0.03, 0.46, 0.006)))
    for hh in (-0.12, 0.12):
        c = bc + UPB * hh + ACB * 0.022
        obs.append(bar(f'{nm}_peinazo{hh:+.2f}', 'madera', c + Vector((0, 0, zl + 0.03)), c + Vector((0, 0, zr - 0.03)), ACB, UPB, rrect(0.018, 0.045, 0.006)))
    # the stiles between its panels, every 0,6 m or so
    nP = max(2, round((zb - za) / 0.62))
    for i in range(1, nP):
        zz = za + (zb - za) * i / nP
        c = bc + ACB * 0.022 + Vector((0, 0, zz))
        obs.append(bar(f'{nm}_montante{i}', 'madera', c - UPB * 0.15, c + UPB * 0.15, ACB, Z, rrect(0.018, 0.05, 0.006)))
    tr = Vector((x - 0.2, 0.985, 0))
    obs.append(bar(f'{nm}_pasamanos', 'madera', tr + Vector((0, 0, zl)), tr + Vector((0, 0, zr)), X, Y, rrect(0.095, 0.055, 0.02, 3)))
    # the shelf behind for the missals, its lip, its brackets
    obs.append(bar(f'{nm}_repisa', 'madera', (x - 0.31, 0.8, zl + 0.04), (x - 0.31, 0.8, zr - 0.04), X, Y, rrect(0.13, 0.022, 0.006)))
    obs.append(bar(f'{nm}_reborde', 'madera', (x - 0.372, 0.835, zl + 0.04), (x - 0.372, 0.835, zr - 0.04), X, Y, rrect(0.016, 0.06, 0.006)))
    for i in range(nP + 1):
        zz = za + 0.08 + (zb - za - 0.16) * i / nP
        obs.append(board(f'{nm}_mensula{i}', 'madera', [(-0.06, -0.06), (0.06, -0.0), (0.06, 0.01), (-0.06, 0.01)], (x - 0.31, 0.79, zz), X, Y, Z, 0.02, r=0.004, grain='u'))
    # a stretcher low down between the ends, and a leg under the seat's middle
    obs.append(bar(f'{nm}_travesano', 'madera', (x - 0.05, 0.1, zl), (x - 0.05, 0.1, zr), X, Y, rrect(0.05, 0.07, 0.008)))
    zm = (za + zb) / 2
    obs.append(board(f'{nm}_pata', 'madera', [(-0.19, 0.0), (0.2, 0.0), (0.2, 0.06), (0.05, 0.12), (0.03, 0.4), (-0.15, 0.4), (-0.19, 0.3)], (x, 0, zm), X, Y, Z, 0.045, r=0.006, grain='v'))
    # the kneeler in front: a board on two arms, its velvet cushion
    obs.append(bar(f'{nm}_reclinatorio', 'madera', (x + 0.47, 0.095, zl + 0.02), (x + 0.47, 0.095, zr - 0.02), X, Y, rrect(0.17, 0.022, 0.006)))
    obs.append(cushion(f'{nm}_cojin', 'terciopelo', (x + 0.47, 0.105, zl + 0.05), (x + 0.47, 0.105, zr - 0.05), X, Y, 0.15, 0.065))
    return obs

def pews():
    obs = []
    for x in pew_positions():
        for s in (-1, 1): obs += pew(x, s)
    return obs

# ---------------------------------------------------------------- shapes turned and swept (the retablos' carving)
def lathe_fn(name, role, centre, rfn, h, seg=48, rows=12, cap0=True, cap1=True):
    """a turned piece whose radius is a function rfn(a, t) of the angle and the height fraction (lobes, flutes, leaves);
    centre: its foot (church frame), h its height. UVs round × up in metres; the light's atlas, one island round it"""
    c = Vector(centre); m = K.Mesh(name, role); grid, uvs = [], []
    for j in range(rows + 1):
        t = j / rows; row, ur = [], []
        for i in range(seg + 1):
            a = 2 * math.pi * i / seg; r = rfn(a % (2 * math.pi), t)
            row.append(m.vert(c + Vector((r * math.cos(a), t * h, r * math.sin(a))))); ur.append((a * 0.2, t * h))
        grid.append(row); uvs.append(ur)
    m.grid(grid, uvs, lmrows=uvs)
    if cap0: m.face([grid[0][i] for i in range(seg)])
    if cap1: m.face([grid[-1][i] for i in range(seg)][::-1])
    return K.closed(m.build())

def turned(name, role, centre, prof, seg=32):
    """a turned piece from a profile [(r, h)] that starts and ends on the axis (a closed solid)"""
    return K.lathe(name, prof, centre, role, seg=seg)

def ring(name, role, centre, R, r, seg=40, sides=10, axis='y', a0=0.0, a1=2 * math.pi):
    """a torus (or a part of one): round `axis` through centre, radius R, its section r"""
    c = Vector(centre); m = K.Mesh(name, role); grid, uvs = [], []
    full = abs(a1 - a0 - 2 * math.pi) < 1e-6
    for i in range(seg + 1):
        a = a0 + (a1 - a0) * i / seg
        if axis == 'y': d, up = Vector((math.cos(a), 0, math.sin(a))), Vector((0, 1, 0))
        elif axis == 'x': d, up = Vector((0, math.cos(a), math.sin(a))), Vector((1, 0, 0))
        else: d, up = Vector((math.cos(a), math.sin(a), 0)), Vector((0, 0, 1))
        row, ur = [], []
        for k in range(sides + 1):
            b = 2 * math.pi * k / sides
            row.append(m.vert(c + d * (R + r * math.cos(b)) + up * (r * math.sin(b)))); ur.append(((a - a0) * R, b * r))
        grid.append(row); uvs.append(ur)
    m.grid(grid, uvs, lmrows=uvs)
    if not full:
        m.face([grid[0][k] for k in range(sides)][::-1]); m.face([grid[-1][k] for k in range(sides)])
    return K.closed(m.build())

def frame_path(name, role, pts, normals_out, W, prof):
    """a moulding swept round a closed outline in a plane: pts (church frame), each point's outward direction in the
    plane, W the plane's normal (out towards you); prof [(out, towards you)] a closed section"""
    pts = list(pts) + [pts[0]]; ns = list(normals_out) + [normals_out[0]]
    return K.sweep(name, pts, ns, [W] * len(pts), prof, role, close_profile=True, caps=False)

# ---------------------------------------------------------------- the retablo mayor (Diego López Cabrera, 1945–49)
# After src/retablo.js (its measures from the photographs): three planes — the middle one flat across the apse, the
# outer streets turned in with the wall's curve — five streets on a predella, three tiers and an attic.
TIERS = [(2.15, 2.85, 0.15), (5.62, 2.68, 0.14), (8.9, 2.4, 0.13)]   # (the tier's foot, its height, its columns' radius)
ENT = 0.62
UC, UH, WING, ALPHA = 1.4, 3.45, 1.95, 0.55
TOP = TIERS[2][0] + TIERS[2][1] + 0.66

class Plano:
    """u across (to the right as you look at it), v up from its floor (the presbytery's, unless given), w out towards you"""
    def __init__(self, theta, ox, oz, y0=None):
        self.c, self.s, self.ox, self.oz = math.cos(theta), math.sin(theta), ox, oz
        self.y0 = K.P if y0 is None else y0
        self.U, self.V, self.W = Vector((self.c, 0, -self.s)), Vector((0, 1, 0)), Vector((self.s, 0, self.c))
    def p(self, u, v, w): return Vector((self.ox + u * self.c + w * self.s, self.y0 + v, self.oz - u * self.s + w * self.c))

def gbox(name, role, pl, w, h, d, u, v, wz, r=0.008):
    """church.js's box(): w across, h up from v, d deep centred at wz — its edges rounded"""
    c = pl.p(u, v + h / 2, wz)
    return bar(name, role, c - pl.U * (w / 2), c + pl.U * (w / 2), pl.W, pl.V, rrect(d, h, r))

def moulding(name, role, pl, u0, u1, v, prof):
    """a profile [(out, up)] (from the back, w = 0) run across the plane from u0 to u1 at height v"""
    return bar(name, role, pl.p(u0, v, 0), pl.p(u1, v, 0), pl.W, pl.V, prof)

def arch_pts(u, v, w, h, n=20):
    """a round-headed opening (centre u, foot v): its outline counter-clockwise, and each point's outward direction"""
    R = w / 2; pts, ns = [(u + R, v)], [(0.7071, -0.7071)]
    for i in range(n + 1):
        a = math.pi * i / n; pts.append((u + R * math.cos(a), v + h - R + R * math.sin(a))); ns.append((math.cos(a), math.sin(a)))
    pts.append((u - R, v)); ns.append((-0.7071, -0.7071))
    return pts, ns

FRAME = [(0.0, 0.0), (0.0, 0.03), (0.012, 0.048), (0.035, 0.058), (0.06, 0.05), (0.08, 0.06), (0.1, 0.045), (0.12, 0.02), (0.12, 0.0)]
def arch_frame(name, pl, u, v, w, h, wz, prof=FRAME, role='dorado'):
    pts, ns = arch_pts(u, v, w, h)
    P3 = [pl.p(a, b, wz) for a, b in pts]; N3 = [(pl.U * x + pl.V * y).normalized() for x, y in ns]
    return frame_path(name, role, P3, N3, pl.W, prof)

def rect_frame(name, pl, u, v, w, h, wz, prof=FRAME, role='dorado'):
    """a moulded frame round a rectangle (centre u, foot v)"""
    pts = [(u + w / 2, v), (u + w / 2, v + h), (u - w / 2, v + h), (u - w / 2, v)]
    ns = [(0.7071, -0.7071), (0.7071, 0.7071), (-0.7071, 0.7071), (-0.7071, -0.7071)]
    P3 = [pl.p(a, b, wz) for a, b in pts]; N3 = [(pl.U * x + pl.V * y).normalized() for x, y in ns]
    return frame_path(name, role, P3, N3, pl.W, [(a * 1.0, b) for a, b in prof])

def cherub(name, pl, u, v, w, s=1.0):
    """a cherub's head between two wings"""
    out = [K.lathe(name + '_cabeza', [(0, -0.075 * s)] + [(0.075 * s * math.sin(math.pi * k / 10), -0.075 * s * math.cos(math.pi * k / 10)) for k in range(1, 10)] + [(0, 0.075 * s)], pl.p(u, v, w + 0.06), 'talla', seg=16)]
    wing = [(0.0, -0.02), (0.06, -0.05), (0.12, -0.04), (0.17, 0.0), (0.19, 0.05), (0.14, 0.04), (0.1, 0.06), (0.05, 0.04), (0.0, 0.02)]
    for sx in (-1, 1):
        o = [(sx * a * s + (0 if sx > 0 else 0), b * s) for a, b in wing]
        if sx < 0: o = o[::-1]
        out.append(board(f'{name}_ala{sx:+d}', 'talla', o, pl.p(u + sx * 0.03 * s, v + 0.01 * s, w + 0.03), pl.U, pl.V, pl.W, 0.03 * s, r=0.008 * s))
    return out

def column(name, pl, u, v0, h, rr, w=0.32):
    """base, the carved lower third (leaves round it), the fluted shaft, the Corinthian capital and its abacus"""
    out = []
    third, capH = h * 0.3, 0.32
    shaftH = h - 0.18 - capH
    foot = pl.p(u, v0, w)
    out.append(turned(name + '_basa', 'dorado', foot, [(0, 0), (rr * 1.5, 0), (rr * 1.5, 0.07), (rr * 1.42, 0.08)] +
                      [(rr * 1.22 + rr * 0.22 * math.cos(b), 0.12 + rr * 0.22 * math.sin(b)) for b in [math.radians(x) for x in (-80, -40, 0, 40, 80)]] +
                      [(rr * 1.12, 0.16), (0, 0.16)], seg=40))
    lob = lambda a, t: rr * 1.08 * (1 + 0.12 * max(0.0, math.sin(a * 5 + t * 2.4)) * math.sin(math.pi * t))
    out.append(lathe_fn(name + '_tercio', 'talla', foot + Vector((0, 0.16, 0)), lob, third, seg=60, rows=10))
    out.append(ring(name + '_collarino', 'dorado', foot + Vector((0, 0.16 + third, 0)), rr * 1.08, rr * 0.12, seg=40, sides=8))
    fl = shaftH - third
    flute = lambda a, t: rr * (1 - 0.1 * t) * (1 - 0.1 * max(0.0, math.cos(a * 16)) ** 2)
    out.append(lathe_fn(name + '_fuste', 'dorado', foot + Vector((0, 0.16 + third, 0)), flute, fl, seg=128, rows=3))
    vc = v0 + h - capH - 0.02
    leaf = lambda a, t: rr * (0.92 + 0.43 * t) * (1 + 0.16 * max(0.0, math.cos(a * 8 + (0 if t < 0.5 else math.pi))) * math.sin(((t * 2) % 1) * math.pi))
    cap0 = pl.p(u, vc, w)
    out.append(lathe_fn(name + '_capitel', 'talla', cap0, leaf, capH * 0.78, seg=64, rows=12))
    for sx, sz in ((-1, 1), (1, 1), (-1, -1), (1, -1)):
        c = cap0 + pl.U * (sx * rr * 1.15) + pl.W * (sz * rr * 1.15) + Vector((0, capH * 0.75, 0))
        out.append(ring(f'{name}_voluta{sx:+d}{sz:+d}', 'talla', c, rr * 0.26, rr * 0.09, seg=20, sides=8, axis='x'))
    out.append(gbox(name + '_abaco', 'dorado', pl, rr * 3.1, 0.07, rr * 3.1, u, vc + capH - 0.035, w, r=0.01))
    return out

ENT_PROF = [(0.0, 0.0), (0.34, 0.0), (0.34, 0.06), (0.31, 0.06), (0.31, 0.14), (0.28, 0.14), (0.28, 0.41), (0.36, 0.41),
            (0.36, 0.44), (0.4, 0.46), (0.48, 0.46), (0.48, 0.53), (0.5, 0.56), (0.54, 0.56), (0.54, 0.6), (0.52, 0.62), (0.0, 0.62)]
def entablature(name, pl, u0, u1, v, us, big=False):
    """architrave in two fasciae, a carved frieze, the cornice (bed moulding, corona, cymatium), broken forward over the
    columns; the main one on dentils"""
    out = [moulding(name, 'dorado', pl, u0, u1, v, ENT_PROF)]
    out.append(moulding(name + '_friso', 'talla', pl, u0 + 0.01, u1 - 0.01, v + 0.15, [(0.27, 0.0), (0.3, 0.0), (0.3, 0.25), (0.27, 0.25)]))
    if big:
        n = max(2, int((u1 - u0) / 0.14))
        for i in range(n):
            uu = u0 + 0.07 + i * (u1 - u0 - 0.14) / (n - 1)
            out.append(gbox(f'{name}_dentellon{i}', 'dorado', pl, 0.06, 0.07, 0.07, uu, v + 0.36, 0.38, r=0.006))
    for j, u in enumerate(us):   # (the breaks over the columns)
        out.append(gbox(f'{name}_resalte{j}a', 'dorado', pl, 0.5, 0.14, 0.26, u, v, 0.45))
        out.append(gbox(f'{name}_resalte{j}b', 'talla', pl, 0.5, 0.27, 0.22, u, v + 0.14, 0.44))
        out.append(gbox(f'{name}_resalte{j}c', 'dorado', pl, 0.62, 0.1, 0.34, u, v + 0.46, 0.5))
        out.append(gbox(f'{name}_resalte{j}d', 'dorado', pl, 0.68, 0.06 + (0.06 if big else 0), 0.4, u, v + 0.56, 0.52))
    return out

def painting_frame(name, pl, u, v, w, h):
    """a canvas under a round head (church.js's painting, which stays in it until 6c): its moulded frame, the carved
    cartouche under it, a cherub in each spandrel"""
    out = [arch_frame(name + '_marco', pl, u, v - 0.0, w + 0.02, h + 0.01, 0.03)]
    ct = [(-0.26, 0.0)] + [(-0.26 + (-0.04) * math.sin(math.pi * k / 6) + 0.12 * k / 6, -0.22 * k / 6) for k in range(1, 6)] + \
         [(0.12 * math.cos(math.pi * (1 - k / 6)), -0.22 - 0.1 * math.sin(math.pi * k / 6)) for k in range(0, 7)] + \
         [(0.26 - 0.12 * (1 - k / 6) + 0.04 * math.sin(math.pi * k / 6), -0.22 * (1 - k / 6)) for k in range(1, 6)] + [(0.26, 0.0)]
    out.append(board(name + '_cartela', 'talla', ct, pl.p(u, v - 0.1, 0.07), pl.U, pl.V, pl.W, 0.06, r=0.015, seg=2, grain='u'))
    for sx in (-1, 1): out += cherub(f'{name}_querube{sx:+d}', pl, u + sx * (w / 2 + 0.06), v + h - 0.02, 0.06)
    return out

def niche(name, pl, u, v, w, h, back_role, shell=True, wb=-0.38, d=0.42):
    """a round-headed hollow: its back lined (at wb), gilded reveals d deep, a half-round soffit, a shell at its head,
    a moulded frame at its mouth"""
    out = []; R = w / 2
    pts, ns = arch_pts(0, 0, w, h)
    out.append(board(name + '_fondo', back_role, [(a, b) for a, b in pts], pl.p(u, v, wb - 0.01), pl.U, pl.V, pl.W, 0.02, r=0.004))
    for sx in (-1, 1): out.append(gbox(f'{name}_jamba{sx:+d}', 'dorado', pl, 0.04, h - R, d, u + sx * (R + 0.02), v, wb + d / 2))
    def soffit(a, t):
        ang = math.pi * a
        return pl.p(u + R * math.cos(ang), v + h - R + R * math.sin(ang), wb + d * t)
    out.append(K.surface(name + '_intrados', soffit, 20, 2, 'dorado', lambda q: (pl.p(u, v + h - R, wb + d / 2) - q)))
    if shell:   # a scallop: ridges fanning from its hinge, its edge scalloped
        def sh(a, t):
            ang = math.pi * a; rr = R * 0.95 * t
            return pl.p(u + rr * math.cos(ang), v + h - R + rr * math.sin(ang), wb + 0.02 + 0.05 * t * (0.6 + 0.4 * math.cos(13 * ang)) * math.sin(math.pi * min(1, t * 1.2)))
        out.append(K.surface(name + '_venera', sh, 52, 8, 'talla', lambda q: pl.W))
    out.append(arch_frame(name + '_marco', pl, u, v - 0.08, w + 0.24, h + 0.2, wb + d, prof=[(a * 1.4, b * 1.2) for a, b in FRAME]))
    return out

def finial(name, pl, u, v, w, s=1.0, flame=True):
    out = [turned(name + '_peana', 'dorado', pl.p(u, v, w), [(0, 0), (0.14 * s, 0), (0.12 * s, 0.06 * s), (0.1 * s, 0.12 * s), (0, 0.12 * s)], seg=16)]
    out.append(turned(name + '_jarron', 'talla', pl.p(u, v + 0.12 * s, w), [(0, 0), (0.12 * s, 0.02 * s), (0.16 * s, 0.12 * s), (0.1 * s, 0.24 * s), (0.06 * s, 0.28 * s), (0.11 * s, 0.34 * s), (0, 0.36 * s)], seg=20))
    if flame:
        fl = lambda a, t: 0.09 * s * (1 - t) ** 0.8 * (1 + 0.25 * math.sin(a * 3 + t * 9))
        out.append(lathe_fn(name + '_llama', 'dorado', pl.p(u, v + 0.48 * s, w), fl, 0.4 * s, seg=16, rows=8, cap1=False))
    return out

def pedestal(name, pl, u, v0, v1, w=0.3):
    out = [gbox(name, 'dorado', pl, 0.5, v1 - v0, 0.5, u, v0, w)]
    out.append(gbox(name + '_tablero', 'talla', pl, 0.38, (v1 - v0) * 0.66, 0.04, u, v0 + (v1 - v0) * 0.17, w + 0.27))
    out += cherub(name + '_querube', pl, u, v0 + (v1 - v0) * 0.55, w + 0.24, 0.9)
    out.append(gbox(name + '_tapa', 'dorado', pl, 0.6, 0.08, 0.6, u, v1 - 0.08, w))
    return out

def retablo_mayor():
    xb = K.XA + K.AR - 1.15
    C = Plano(-math.pi / 2, xb, 0.0); R = Plano(-math.pi / 2 - ALPHA, xb, UH); L = Plano(-math.pi / 2 + ALPHA, xb, -UH)
    out = []
    cols = {'C': [-UH, -UC, UC, UH], 'R': [WING], 'L': [-WING]}
    for nm, pl, u0, u1 in (('C', C, -UH, UH), ('R', R, 0.0, WING), ('L', L, -WING, 0.0)):
        W, um = u1 - u0, (u0 + u1) / 2; b = f'retablo_{nm}'
        # the sotabanco and the predella
        out.append(gbox(b + '_sotabanco', 'dorado', pl, W + 0.1, 0.12, 0.62, um, 0, 0.31))
        out.append(gbox(b + '_banco', 'talla', pl, W, 0.6, 0.5, um, 0.12, 0.25))
        out.append(gbox(b + '_banco_cornisa', 'dorado', pl, W + 0.08, 0.08, 0.58, um, 0.72, 0.29))
        out.append(gbox(b + '_predela', 'talla', pl, W, 1.27, 0.12, um, 0.8, -0.06))
        out.append(gbox(b + '_predela_cornisa', 'dorado', pl, W + 0.12, 0.08, 0.5, um, 2.07, 0.22))
        for j, u in enumerate(cols[nm]): out += pedestal(f'{b}_pedestal{j}', pl, u, 0.8, 2.07)
        # the tiers' back boards (the middle street's two lower ones with their niches)
        for ti, (v0, h, rr) in enumerate(TIERS):
            if nm != 'C' or ti == 2: out.append(gbox(f'{b}_tablero{ti}', 'talla', pl, W, h, 0.1, um, v0, -0.05)); continue
            for sx in (-1, 1): out.append(gbox(f'{b}_tablero{ti}{sx:+d}', 'talla', pl, UH - UC, h, 0.1, sx * (UC + UH) / 2, v0, -0.05))
            nv = v0 + 0.25 if ti == 0 else v0 + 0.12; nw = 1.62 if ti == 0 else 1.55; nh = h - 0.42 if ti == 0 else h - 0.3
            # the wall round the niche: four boards round its arch
            Rn = nw / 2
            out.append(gbox(f'{b}_nicho{ti}_pie', 'talla', pl, 2 * UC, nv - v0, 0.1, 0, v0, -0.05))
            for sx in (-1, 1): out.append(gbox(f'{b}_nicho{ti}_lado{sx:+d}', 'talla', pl, UC - Rn, h - (nv - v0), 0.1, sx * (UC + Rn) / 2, nv, -0.05))
            out.append(gbox(f'{b}_nicho{ti}_cima', 'talla', pl, 2 * UC, v0 + h - (nv + nh), 0.1, 0, nv + nh, -0.05))
            # the two spandrels between the arch and the line of its crown (counter-clockwise, each)
            arc = lambda th: (Rn * math.cos(th), nh - Rn + Rn * math.sin(th))
            left = [arc(math.pi - (math.pi / 2) * k / 8) for k in range(9)] + [(-Rn, nh)]
            right = [(Rn, nh - Rn), (Rn, nh)] + [arc(math.pi / 2 - (math.pi / 2) * k / 8) for k in range(9)][:-1]
            for sx, outl in ((-1, left), (1, right)):
                out.append(board(f'{b}_nicho{ti}_enjuta{sx:+d}', 'talla', outl, pl.p(0, nv, -0.05), pl.U, pl.V, pl.W, 0.1, r=0.006))
        cu = cols[nm]
        for ti, (v0, h, rr) in enumerate(TIERS):
            for j, u in enumerate(cu): out += column(f'{b}_col{ti}{j}', pl, u, v0, h, rr)
            out += entablature(f'{b}_cornisa{ti}', pl, u0 - 0.04, u1 + 0.04, v0 + h, cu, big=(ti == 2))
    # the apostles' frames (their canvases are church.js's until 6c): the inner and outer streets, three tiers
    slots = [(L, -WING / 2, 1.18), (C, -(UC + UH) / 2, 1.3), (C, (UC + UH) / 2, 1.3), (R, WING / 2, 1.18)]
    for ti, (v0, h, rr) in enumerate(TIERS):
        for si, (pl, u, w) in enumerate(slots): out += painting_frame(f'retablo_apostol{ti}{si}', pl, u, v0 + 0.38, w, h - 0.6)
    # the four Doctors' frames in the predella (eared)
    for j, (pl, u) in enumerate(((L, -WING / 2), (C, -(UC + UH) / 2), (C, (UC + UH) / 2), (R, WING / 2))):
        out.append(rect_frame(f'retablo_doctor{j}', pl, u, 1.43 - 0.39, 0.8, 0.8, 0.0))
        for sx in (-1, 1): out.append(gbox(f'retablo_doctor{j}_oreja{sx:+d}', 'dorado', pl, 0.08, 0.1, 0.06, u + sx * 0.5, 1.43 + 0.34, 0.03))
    # the middle street. Bottom: the tabernacle, the exhibitor's niche (velvet), the exhibitor in silver
    out.append(gbox('retablo_sagrario', 'dorado', C, 1.1, 1.2, 0.62, 0, 0.8, 0.31))
    out.append(gbox('retablo_sagrario_puerta', 'talla', C, 0.8, 0.86, 0.04, 0, 0.97, 0.64))
    out.append(turned('retablo_caliz', 'plata', C.p(0, 1.15, 0.68), [(0, 0), (0.09, 0.01), (0.04, 0.05), (0.025, 0.18), (0.06, 0.2), (0.12, 0.36), (0.1, 0.36), (0.0, 0.25)], seg=24))
    out.append(gbox('retablo_sagrario_cornisa', 'dorado', C, 1.24, 0.1, 0.7, 0, 2.0, 0.33))
    v0, h, rr = TIERS[0]
    out += niche('retablo_nicho_expositor', C, 0, v0 + 0.25, 1.62, h - 0.42, 'terciopelo', shell=False)
    ev, ew = v0 + 0.25, -0.04
    out.append(turned('expositor_base', 'plata', C.p(0, ev, ew), [(0, 0), (0.34, 0), (0.34, 0.04), (0.32, 0.12), (0.33, 0.16), (0, 0.16)], seg=32))
    for i in range(6):
        a = i / 6 * 2 * math.pi + math.pi / 6
        out.append(turned(f'expositor_col{i}', 'plata', C.p(math.cos(a) * 0.25, ev + 0.16, ew + math.sin(a) * 0.25), [(0, 0), (0.035, 0), (0.03, 0.04), (0.026, 0.06), (0.024, 0.9), (0.034, 0.95), (0, 0.95)], seg=12))
    out.append(turned('expositor_cornisa', 'plata', C.p(0, ev + 1.1, ew), [(0, 0), (0.3, 0), (0.33, 0.04), (0.32, 0.09), (0, 0.09)], seg=32))
    out.append(turned('expositor_cupula', 'plata', C.p(0, ev + 1.19, ew), [(0.29 * math.cos(math.pi / 2 * k / 10), 0.29 * math.sin(math.pi / 2 * k / 10)) for k in range(11)] + [(0, 0.29)], seg=32))
    out.append(turned('expositor_remate', 'dorado', C.p(0, ev + 1.48, ew), [(0, 0), (0.06, 0), (0.045, 0.16), (0, 0.16)], seg=12))
    out.append(gbox('expositor_cruz_v', 'dorado', C, 0.025, 0.2, 0.025, 0, ev + 1.64, ew))
    out.append(gbox('expositor_cruz_h', 'dorado', C, 0.12, 0.025, 0.025, 0, ev + 1.72, ew))
    for i in range(16):   # the monstrance's sun inside it
        a = i / 16 * 2 * math.pi; L2 = 0.14 + (i % 2) * 0.06; c0 = Vector((math.sin(a), math.cos(a)))
        p0 = C.p(c0.x * 0.06, ev + 0.68 + c0.y * 0.06, ew); p1 = C.p(c0.x * (0.06 + L2), ev + 0.68 + c0.y * (0.06 + L2), ew)
        out.append(bar(f'expositor_rayo{i}', 'dorado', p0, p1, C.W, C.W.cross((p1 - p0).normalized()), rrect(0.012, 0.014, 0.004)))
    out.append(bar('expositor_hostia', 'blanco', C.p(0, ev + 0.68, ew - 0.01), C.p(0, ev + 0.68, ew + 0.01), C.U, C.V, [(0.05 * math.cos(2 * math.pi * k / 24), 0.05 * math.sin(2 * math.pi * k / 24)) for k in range(24)]))
    # middle: the Virgin's niche (blue, starred), its shell, the sunburst behind her (her image is church.js's)
    v0, h, rr = TIERS[1]
    out += niche('retablo_nicho_virgen', C, 0, v0 + 0.12, 1.55, h - 0.3, 'azul', shell=True)
    for i in range(28):
        a = i / 28 * 2 * math.pi; L2 = 0.42 + (i % 2) * 0.16; c0 = Vector((math.sin(a), math.cos(a)))
        p0 = C.p(c0.x * 0.36, v0 + 0.12 + 1.6 + c0.y * 0.36, -0.3); p1 = C.p(c0.x * (0.36 + L2), v0 + 0.12 + 1.6 + c0.y * (0.36 + L2), -0.3)
        out.append(bar(f'retablo_resplandor{i}', 'dorado', p0, p1, C.W, C.W.cross((p1 - p0).normalized()), rrect(0.012, 0.035, 0.004)))
    # top: the Crucifixion's eared frame (its canvas is church.js's)
    v0, h, rr = TIERS[2]
    ch = h - 0.5; cw = ch * 636 / 1024; cv = v0 + 0.25   # (El Greco's canvas, taller than church.js's: its frame made to it)
    out.append(rect_frame('retablo_calvario_marco', C, 0, cv, cw + 0.04, ch + 0.04, 0.0, prof=[(a * 1.3, b * 1.2) for a, b in FRAME]))
    for sx in (-1, 1): out.append(gbox(f'retablo_calvario_oreja{sx:+d}', 'dorado', C, 0.12, 0.34, 0.07, sx * (cw / 2 + 0.2), cv + ch - 0.2, 0.035))
    # (either side of it, to the street's columns: carved panels, a cherub on each)
    pw = UC - cw / 2 - 0.32
    for sx in (-1, 1):
        uu = sx * (cw / 2 + 0.3 + pw / 2)
        out.append(gbox(f'retablo_calvario_tablero{sx:+d}', 'talla', C, pw, ch * 0.7, 0.05, uu, cv + ch * 0.15, 0.02, r=0.01))
        out.append(rect_frame(f'retablo_calvario_tablero{sx:+d}_marco', C, uu, cv + ch * 0.15, pw, ch * 0.7, 0.03, prof=[(a * 0.5, b * 0.6) for a, b in FRAME]))
        out += cherub(f'retablo_calvario_tablero{sx:+d}_querube', C, uu, cv + ch * 0.5, 0.08, 0.9)
    out += cherub('retablo_calvario_querube', C, 0, cv + ch + 0.2, 0.08, 1.4)
    # the attic: the dove in its glory, scrolls either side, the broken pediment, the globe and the cross
    v, aw, ah = TOP - 0.02, 2.3, 1.7
    out.append(gbox('retablo_atico', 'talla', C, aw, ah, 0.12, 0, v, -0.02))
    for sx in (-1, 1): out.append(gbox(f'retablo_atico_pilastra{sx:+d}', 'dorado', C, 0.2, ah, 0.3, sx * (aw / 2 - 0.1), v, 0.14))
    out.append(bar('retablo_gloria', 'blanco', C.p(0, v + ah * 0.52, 0.05), C.p(0, v + ah * 0.52, 0.07), C.U, C.V, [(0.55 * math.cos(2 * math.pi * k / 40), 0.55 * math.sin(2 * math.pi * k / 40)) for k in range(40)]))
    for i in range(24):
        a = i / 24 * 2 * math.pi; L2 = 0.3 + (i % 2) * 0.18; c0 = Vector((math.sin(a), math.cos(a)))
        p0 = C.p(c0.x * 0.55, v + ah * 0.52 + c0.y * 0.55, 0.07); p1 = C.p(c0.x * (0.55 + L2), v + ah * 0.52 + c0.y * (0.55 + L2), 0.07)
        out.append(bar(f'retablo_gloria_rayo{i}', 'dorado', p0, p1, C.W, C.W.cross((p1 - p0).normalized()), rrect(0.02, 0.03, 0.005)))
    dv = v + ah * 0.52
    # (the dove's body across the retablo — the middle plane's u runs along z)
    out.append(K.lathe('retablo_paloma', [(0, 0)] + [(0.075 * math.sin(math.pi * k / 10), 0.32 * k / 10) for k in range(1, 10)] + [(0, 0.32)], C.p(0, dv, 0.15) - C.U * 0.16, 'blanco', seg=16, axis='z'))
    wingp = [(0.0, 0.0), (0.12, 0.05), (0.24, 0.12), (0.3, 0.2), (0.22, 0.17), (0.12, 0.13), (0.03, 0.08)]
    for sx in (-1, 1):
        o = [(sx * a, b) for a, b in wingp]
        if sx < 0: o = o[::-1]
        out.append(board(f'retablo_paloma_ala{sx:+d}', 'blanco', o, C.p(sx * 0.02, dv + 0.02, 0.13), C.U, C.V, C.W, 0.025, r=0.006))
    for sx in (-1, 1):   # the scrolls down to the inner streets' cornice, a flaming urn on each
        a0, a1 = (-0.15, -0.15 + math.pi * 1.3) if sx > 0 else (math.pi + 0.15 - math.pi * 1.3, math.pi + 0.15)
        c = C.p(sx * (aw / 2 + 0.38), v + 0.42, 0.1)
        n = 24; pts = [c + C.U * (0.38 * math.cos(a0 + (a1 - a0) * k / n)) + C.V * (0.38 * math.sin(a0 + (a1 - a0) * k / n)) for k in range(n + 1)]
        nrm = [((pts[k] - c).normalized()) for k in range(n + 1)]
        out.append(K.sweep(f'retablo_voluta{sx:+d}', pts, nrm, [C.W] * len(pts), [(0.09 * math.cos(2 * math.pi * k / 10), 0.09 * math.sin(2 * math.pi * k / 10)) for k in range(10)], 'dorado', close_profile=True, caps=True))
        out += finial(f'retablo_remate_atico{sx:+d}', C, sx * (UC + 0.1), v, 0.35, 0.9)
    for sx in (-1, 1):   # the broken pediment's two halves
        a0, a1 = (math.pi * 0.1, math.pi * 0.42) if sx > 0 else (math.pi * 0.58, math.pi * 0.9)
        c = C.p(0, v + ah - 0.55, 0.12)
        n = 16; pts = [c + C.U * (aw * 0.5 * math.cos(a0 + (a1 - a0) * k / n)) + C.V * (aw * 0.5 * math.sin(a0 + (a1 - a0) * k / n)) for k in range(n + 1)]
        nrm = [((pts[k] - c).normalized()) for k in range(n + 1)]
        out.append(K.sweep(f'retablo_fronton{sx:+d}', pts, nrm, [C.W] * len(pts), [(0.09 * math.cos(2 * math.pi * k / 10), 0.09 * math.sin(2 * math.pi * k / 10)) for k in range(10)], 'dorado', close_profile=True, caps=True))
    out.append(gbox('retablo_atico_cornisa', 'dorado', C, aw + 0.3, 0.12, 0.42, 0, v + ah, 0.12))
    out.append(turned('retablo_globo', 'dorado', C.p(0, v + ah + 0.14, 0.12), [(0, 0)] + [(0.16 * math.sin(math.pi * k / 12), 0.16 - 0.16 * math.cos(math.pi * k / 12)) for k in range(1, 12)] + [(0, 0.32)], seg=24))
    out.append(gbox('retablo_cruz_v', 'dorado', C, 0.06, 0.62, 0.06, 0, v + ah + 0.42, 0.12))
    out.append(gbox('retablo_cruz_h', 'dorado', C, 0.34, 0.06, 0.06, 0, v + ah + 0.83, 0.12))
    # crests over the other streets, pinnacles on the outer columns
    for j, (pl, u) in enumerate(((C, -(UC + UH) / 2), (C, (UC + UH) / 2), (L, -WING / 2), (R, WING / 2))):
        c = pl.p(u, TOP, 0.12); n = 16
        pts = [c + pl.U * (0.55 * math.cos(math.pi * k / n)) + pl.V * (0.55 * math.sin(math.pi * k / n)) for k in range(n + 1)]
        out.append(K.sweep(f'retablo_copete{j}', pts, [(q - c).normalized() for q in pts], [pl.W] * len(pts), [(0.07 * math.cos(2 * math.pi * k / 8), 0.07 * math.sin(2 * math.pi * k / 8)) for k in range(8)], 'dorado', close_profile=True, caps=True))
        out += finial(f'retablo_remate{j}', pl, u, TOP, 0.12, 0.85)
    for j, (pl, u) in enumerate(((C, -UH), (C, UH), (L, -WING), (R, WING))):
        out.append(gbox(f'retablo_pinaculo{j}_dado', 'dorado', pl, 0.32, 0.22, 0.32, u, TOP, 0.4))
        out.append(turned(f'retablo_pinaculo{j}', 'talla', pl.p(u, TOP + 0.22, 0.4), [(0, 0), (0.15, 0), (0.0, 0.6)], seg=4))
        out.append(turned(f'retablo_pinaculo{j}_bola', 'dorado', pl.p(u, TOP + 0.79, 0.4), [(0, 0)] + [(0.07 * math.sin(math.pi * k / 8), 0.07 - 0.07 * math.cos(math.pi * k / 8)) for k in range(1, 8)] + [(0, 0.14)], seg=12))
    return out

# ---------------------------------------------------------------- the organ in the choir
ORGAN = {'oz': -5.3, 'W': 5.0, 'D': 1.2}   # (moved north of church.js's, off the oculus: the reviewer's request)
def organo():
    """the organ against the west wall of the choir: a panelled case with its console, three towers of tin pipes (the
    middle one tallest) on moulded shelves, carved gilded crests over them"""
    out = []
    y0, oz, W, D = K.CHY, ORGAN['oz'], ORGAN['W'], ORGAN['D']
    x0 = K.X0 + 0.3; x1 = x0 + D; xm = (x0 + x1) / 2
    X, Y, Z = Vector((1, 0, 0)), Vector((0, 1, 0)), Vector((0, 0, 1))
    za, zb = oz - W / 2, oz + W / 2
    # the lower case and its plinth
    out.append(bar('organo_caja', 'madera', (xm, y0 + 1.5, za), (xm, y0 + 1.5, zb), X, Y, rrect(D, 3.0, 0.02)))
    out.append(bar('organo_zocalo', 'madera', (xm + 0.02, y0 + 0.09, za - 0.03), (xm + 0.02, y0 + 0.09, zb + 0.03), X, Y, rrect(D + 0.06, 0.18, 0.01)))
    # its front: fielded panels in two rows, the console's opening between them
    for row, (v0, v1) in enumerate(((0.3, 1.0), (1.9, 2.75))):
        n = 5
        for i in range(n):
            if row == 1 and i == 2: continue
            u0 = -W / 2 + 0.15 + i * (W - 0.3) / n; u1 = u0 + (W - 0.3) / n - 0.1
            pan = [(u0, v0), (u1, v0), (u1, v1), (u0, v1)]
            out.append(board(f'organo_cuarteron{row}{i}', 'madera', pan, (x1 + 0.006, y0, oz), Z, Y, X, 0.012, r=0.004, grain='v'))
            fld = [(u0 + 0.05, v0 + 0.05), (u1 - 0.05, v0 + 0.05), (u1 - 0.05, v1 - 0.05), (u0 + 0.05, v1 - 0.05)]
            out.append(board(f'organo_campo{row}{i}', 'madera', fld, (x1 + 0.016, y0, oz), Z, Y, X, 0.012, r=0.006, seg=3, grain='v'))
    # the console: a recess with two manuals and the music desk, the bench before it
    kz = oz
    out.append(bar('organo_consola', 'madera', (x1 + 0.02, y0 + 1.15, kz - 0.75), (x1 + 0.02, y0 + 1.15, kz + 0.75), X, Y, rrect(0.12, 0.06, 0.01)))
    for j, (yy, xx) in enumerate(((1.2, 0.18), (1.32, 0.1))):
        out.append(bar(f'organo_teclado{j}', 'blanco', (x1 + xx, y0 + yy, kz - 0.6), (x1 + xx, y0 + yy, kz + 0.6), X, Y, rrect(0.16, 0.025, 0.004)))
    out.append(board('organo_atril', 'madera', [(-0.55, 0.0), (0.55, 0.0), (0.55, 0.3), (-0.55, 0.3)], (x1 + 0.02, y0 + 1.42, kz), Z, Y, X, 0.02, r=0.004))
    for sz in (-1, 1):
        out.append(board(f'organo_banqueta_pata{sz:+d}', 'madera', [(-0.16, 0.0), (0.16, 0.0), (0.16, 0.48), (-0.16, 0.48)], (x1 + 0.55, y0, kz + sz * 0.6), X, Y, Z, 0.04, r=0.006, grain='v'))
    out.append(bar('organo_banqueta', 'madera', (x1 + 0.55, y0 + 0.5, kz - 0.7), (x1 + 0.55, y0 + 0.5, kz + 0.7), X, Y, rrect(0.34, 0.05, 0.01)))
    # the cornice over the lower case
    prof = [(0.0, 0.0), (0.08, 0.0), (0.08, 0.04), (0.12, 0.07), (0.18, 0.1), (0.18, 0.16), (0.22, 0.2), (0.22, 0.24), (0.0, 0.24)]
    out.append(bar('organo_cornisa', 'madera', (x1, y0 + 3.0, za - 0.1), (x1, y0 + 3.0, zb + 0.1), X, Y, [(a - 0.0, b) for a, b in prof]))
    # the upper case: its back and its two side flats
    out.append(bar('organo_trasera', 'madera', (x0 + 0.15, y0 + 4.8, za), (x0 + 0.15, y0 + 4.8, zb), X, Y, rrect(0.08, 3.4, 0.01)))
    for sz in (-1, 1):
        zz = oz + sz * (W / 2 - 0.05)
        out.append(bar(f'organo_costado{sz:+d}', 'madera', (xm, y0 + 4.6, zz - 0.05), (xm, y0 + 4.6, zz + 0.05), X, Y, rrect(D, 3.2, 0.01)))
    # the towers: a moulded shelf, the pipes in a V (the tallest in the middle), a carved crest and a cornice over them
    for t, (dz, n, hp) in enumerate(((-1.75, 7, 2.2), (0.0, 9, 2.9), (1.75, 7, 2.2))):
        zc = oz + dz; wt = n * 0.17 + 0.2
        out.append(bar(f'organo_torre{t}_repisa', 'madera', (x1 - 0.25, y0 + 3.3, zc - wt / 2), (x1 - 0.25, y0 + 3.3, zc + wt / 2), X, Y, rrect(0.55, 0.12, 0.02)))
        for i in range(n):
            zz = zc + (i - (n - 1) / 2) * 0.17
            hh = hp * (1 - abs(i - (n - 1) / 2) / n * 0.6)
            pr = 0.062
            out.append(turned(f'organo_tubo{t}_{i}', 'plata', (x1 - 0.25, y0 + 3.36, zz), [(0, 0), (0.014, 0), (pr * 0.9, 0.34), (pr, 0.4), (pr, hh), (pr * 0.92, hh + 0.005), (0, hh + 0.005)], seg=18))
            # (its mouth: the flattened lip where the air speaks)
            out.append(board(f'organo_boca{t}_{i}', 'talla', [(-0.03, 0.0), (0.03, 0.0), (0.03, 0.05), (0.0, 0.07), (-0.03, 0.05)], (x1 - 0.25 + pr * 0.95, y0 + 3.36 + 0.42, zz), Z, Y, X, 0.006, r=0.002, grain='u'))
        top = y0 + 3.36 + hp
        out.append(board(f'organo_torre{t}_cresta', 'talla', [(-wt / 2, 0.0), (wt / 2, 0.0)] + [((wt / 2) * math.cos(math.pi * k / 12), 0.12 + 0.34 * math.sin(math.pi * k / 12)) for k in range(13)], (x1 - 0.2, top + 0.08, zc), Z, Y, X, 0.05, r=0.012))
        out.append(bar(f'organo_torre{t}_cornisa', 'dorado', (x1 - 0.22, top + 0.04, zc - wt / 2 - 0.04), (x1 - 0.22, top + 0.04, zc + wt / 2 + 0.04), X, Y, rrect(0.6, 0.08, 0.02)))
        out += finial(f'organo_torre{t}_remate', Plano(-math.pi / 2, x1 - 0.2, zc, 0.0), 0.0, top + 0.52, 0.0, 0.7)
    return out

# ---------------------------------------------------------------- the chapels' retablos (the collaterals)
CHAPELS = [(0, 1, 'dolorosa'), (1, -1, 'cristo'), (1, 1, 'corazon'), (3, -1, 'jose'), (3, 1, 'inmaculada')]   # (bay, side, kind) — church.js's

def solomonic(name, pl, u, v0, h, rr, w):
    """a Solomonic column: a base, its shaft twisted in five turns (a vine of leaves in its hollow), a capital"""
    out = [turned(name + '_basa', 'dorado', pl.p(u, v0, w), [(0, 0), (rr * 1.5, 0), (rr * 1.5, 0.05), (rr * 1.3, 0.07), (rr * 1.32, 0.1), (rr * 1.1, 0.13), (0, 0.13)], seg=28)]
    sh = h - 0.13 - 0.22
    twist = lambda a, t: rr * (1 + 0.22 * math.cos(a - t * 5 * 2 * math.pi)) * (1 - 0.08 * t)
    out.append(lathe_fn(name + '_fuste', 'dorado', pl.p(u, v0 + 0.13, w), twist, sh, seg=32, rows=60))
    vine = lambda a, t: rr * (1.02 + 0.1 * math.cos(a - t * 5 * 2 * math.pi + math.pi)) * (1 + 0.12 * max(0.0, math.sin(a * 6 + t * 40)))
    out.append(lathe_fn(name + '_parra', 'talla', pl.p(u, v0 + 0.13 + 0.02, w), lambda a, t: min(vine(a, t), rr * 1.05), sh - 0.04, seg=32, rows=60))
    leaf = lambda a, t: rr * (0.95 + 0.45 * t) * (1 + 0.14 * max(0.0, math.cos(a * 8)) * math.sin(math.pi * t))
    out.append(lathe_fn(name + '_capitel', 'talla', pl.p(u, v0 + h - 0.22, w), leaf, 0.17, seg=32, rows=6))
    out.append(gbox(name + '_abaco', 'dorado', pl, rr * 3.0, 0.05, rr * 3.0, u, v0 + h - 0.05, w, r=0.008))
    return out

def altar_table(name, pl, w=2.2, h=0.95, d=0.9):
    """an altar of stone: a moulded base and frontal, its mensa slab, a linen cloth falling over its front"""
    out = [gbox(name + '_pie', 'piedra', pl, w, 0.12, d + 0.06, 0, 0, d / 2 - 0.03, r=0.01)]
    out.append(gbox(name + '_cuerpo', 'piedra', pl, w - 0.08, h - 0.2, d - 0.1, 0, 0.12, d / 2 - 0.05, r=0.008))
    for j in range(3):   # (three sunk panels on its front)
        uu = -w / 3 + j * w / 3
        out.append(gbox(f'{name}_tablero{j}', 'piedra', pl, w / 3 - 0.16, h - 0.42, 0.02, uu, 0.23, d - 0.09, r=0.005))
    out.append(gbox(name + '_mesa', 'piedra', pl, w + 0.1, 0.08, d + 0.1, 0, h - 0.08, d / 2, r=0.012))
    out.append(gbox(name + '_mantel', 'lino', pl, w + 0.2, 0.012, d + 0.06, 0, h, d / 2, r=0.004))
    out.append(gbox(name + '_caida', 'lino', pl, w + 0.2, 0.32, 0.008, 0, h - 0.31, d + 0.04, r=0.002))
    return out

def colateral(i, b, s, kind):
    """a chapel's retablo of gilded wood (church.js's measures): a predella, one body of three streets between four
    Solomonic columns — the image's niche in the middle, a canvas each side —, a cornice, an attic with its crest"""
    xa, xb, xm = K.BAYS[b]
    zb = s * (K.HW + K.CD - 0.15)
    pl = Plano(0.0 if s < 0 else math.pi, xm, zb - s * 0.12, 0.0)
    nm = f'colateral{i}'; out = []
    W2 = 4.2
    # the altar before it
    alt = Plano(0.0 if s < 0 else math.pi, xm, zb - s * 0.85 - s * 0.45, 0.0)
    out += altar_table(nm + '_altar', alt)
    # the predella, the body's back, the frieze
    out.append(gbox(nm + '_banco', 'talla', pl, W2, 1.0, 0.4, 0, 1.0, 0.05))
    out.append(moulding(nm + '_banco_cornisa', 'dorado', pl, -W2 / 2 - 0.04, W2 / 2 + 0.04, 1.96, [(0.0, 0.0), (0.3, 0.0), (0.3, 0.04), (0.33, 0.07), (0.33, 0.1), (0.0, 0.1)]))
    out.append(gbox(nm + '_tablero', 'dorado', pl, W2, 3.6, 0.25, 0, 2.0, -0.05))
    out.append(moulding(nm + '_cornisa', 'dorado', pl, -W2 / 2 - 0.15, W2 / 2 + 0.15, 5.22, [(a * 0.9, b * 0.85) for a, b in ENT_PROF]))
    # the four Solomonic columns
    for j, u in enumerate((-W2 / 2 + 0.2, -0.75, 0.75, W2 / 2 - 0.2)):
        out += solomonic(f'{nm}_col{j}', pl, u, 2.08, 3.14, 0.1, 0.2)
        out.append(gbox(f'{nm}_col{j}_peana', 'talla', pl, 0.34, 0.08, 0.34, u, 2.0, 0.2))
    # the niche in the middle (its velvet back; church.js's image stands in it) with its shell
    out += niche(nm + '_nicho', pl, 0, 2.25, 1.2, 2.9, 'terciopelo', shell=True, wb=0.08, d=0.22)   # (shallow: the image stands out of it, at church.js's place)
    # the side canvases' frames (the canvases are church.js's until 6c), a cartouche under each
    for sx in (-1, 1):
        out.append(rect_frame(f'{nm}_marco{sx:+d}', pl, sx * 1.45, 3.22, 0.84, 1.34, 0.1))
        out += cherub(f'{nm}_querube{sx:+d}', pl, sx * 1.45, 4.72, 0.12, 0.8)
    # the attic: a panel framed between scrolls, a curved crest, a finial
    out.append(gbox(nm + '_atico', 'talla', pl, 1.6, 1.4, 0.25, 0, 5.75, -0.05))
    out.append(rect_frame(nm + '_atico_marco', pl, 0, 5.9, 1.1, 0.95, 0.09))
    for sx in (-1, 1):
        c = pl.p(sx * 1.0, 6.0, 0.05); n = 18
        pts = [c + pl.U * (sx * 0.22 * math.cos(math.pi * k / n)) + pl.V * (0.4 * math.sin(math.pi * k / n)) for k in range(n + 1)]
        out.append(K.sweep(f'{nm}_atico_voluta{sx:+d}', pts, [(q - c).normalized() if (q - c).length > 1e-6 else pl.V for q in pts], [pl.W] * len(pts), [(0.05 * math.cos(2 * math.pi * k / 8), 0.05 * math.sin(2 * math.pi * k / 8)) for k in range(8)], 'dorado', close_profile=True, caps=True))
    c = pl.p(0, 7.15, 0.0); n = 16
    pts = [c + pl.U * (0.8 * math.cos(math.pi * k / n)) + pl.V * (0.35 * math.sin(math.pi * k / n)) for k in range(n + 1)]
    out.append(K.sweep(nm + '_copete', pts, [(q - c).normalized() for q in pts], [pl.W] * len(pts), [(0.07 * math.cos(2 * math.pi * k / 8), 0.07 * math.sin(2 * math.pi * k / 8)) for k in range(8)], 'dorado', close_profile=True, caps=True))
    out += finial(nm + '_remate', pl, 0, 7.5, 0.0, 0.8)
    return out

def colaterales():
    out = []
    for i, (b, s, kind) in enumerate(CHAPELS): out += colateral(i, b, s, kind)
    return out

# ---------------------------------------------------------------- the presbytery: the altar, the ambo, the chairs
def presbiterio():
    """the altar of the Eucharist (marble, a moulded mensa on a body of sunk panels, its linen), the ambo on the
    Gospel side (a lectern of wood, its desk sloping), the presider's chair and two more against the apse (velvet)"""
    out = []
    ax = K.XA - 0.6
    pl = Plano(-math.pi / 2, ax + 0.525, 0.0)   # (facing the nave: w towards −x; u across, +z)
    # the altar: 1,05 deep, 1 high, 2,4 long (church.js's block and collider)
    W, D, H = 2.4, 1.05, 1.0
    out.append(gbox('altar_pie', 'marmol', pl, W + 0.08, 0.1, D + 0.08, 0, 0, D / 2, r=0.01))
    out.append(gbox('altar_cuerpo', 'marmol', pl, W - 0.06, H - 0.18, D - 0.08, 0, 0.1, D / 2, r=0.008))
    for j in range(3):
        uu = -W / 3 + j * W / 3
        out.append(gbox(f'altar_tablero{j}', 'marmol', pl, W / 3 - 0.18, H - 0.42, 0.02, uu, 0.22, D - 0.03, r=0.006))
        out.append(rect_frame(f'altar_tablero{j}_marco', pl, uu, 0.22, W / 3 - 0.18, H - 0.42, D - 0.04, prof=[(a * 0.4, b * 0.5) for a, b in FRAME], role='marmol'))
    out.append(gbox('altar_mesa', 'marmol', pl, W + 0.12, 0.08, D + 0.1, 0, H - 0.08, D / 2, r=0.015))
    out.append(gbox('altar_mantel', 'lino', pl, W + 0.2, 0.012, D + 0.14, 0, H, D / 2, r=0.004))
    out.append(gbox('altar_caida', 'lino', pl, W + 0.1, 0.48, 0.008, 0, H - 0.47, D + 0.075, r=0.002))
    # the ambo: on the Gospel side (north), facing the nave
    am = Plano(-math.pi / 2, K.XP + 2.6 + 0.3, -K.HW + 2.4)
    out.append(gbox('ambon_pie', 'madera', am, 0.7, 0.08, 0.6, 0, 0, 0.3, r=0.01))
    out.append(gbox('ambon_cuerpo', 'madera', am, 0.56, 1.0, 0.46, 0, 0.08, 0.28, r=0.012))
    for sx in (-1, 0, 1):
        out.append(rect_frame(f'ambon_cuarteron{sx:+d}', am, sx * 0.17, 0.28, 0.12, 0.6, 0.51, prof=[(a * 0.3, b * 0.4) for a, b in FRAME], role='madera'))
    desk = [(-0.4, 0.0), (0.4, 0.0), (0.4, 0.05), (-0.4, 0.05)]
    c = am.p(0, 1.14, 0.28)
    out.append(bar('ambon_atril', 'madera', c - am.U * 0.42, c + am.U * 0.42, (am.W * math.cos(0.3) + am.V * math.sin(0.3)), (am.V * math.cos(0.3) - am.W * math.sin(0.3)), rrect(0.6, 0.04, 0.01)))
    # the chairs: the presider's (tall), two beside it — velvet seats, carved wooden backs and arms
    for j, (cz, hh) in enumerate(((5.2, 1.5), (4.3, 1.1), (6.1, 1.1))):
        ch = Plano(-math.pi / 2, K.XA - 1.9, cz)
        out.append(gbox(f'silla{j}_asiento', 'terciopelo', ch, 0.56, 0.1, 0.5, 0, 0.42, 0.3, r=0.03))
        out.append(gbox(f'silla{j}_marco', 'madera', ch, 0.6, 0.06, 0.56, 0, 0.38, 0.3, r=0.01))
        for su in (-1, 1):
            for sw in (0.06, 0.52):
                out.append(gbox(f'silla{j}_pata{su:+d}{sw}', 'madera', ch, 0.05, 0.38, 0.05, su * 0.27, 0.0, sw, r=0.008))
            if j == 0:
                out.append(gbox(f'silla{j}_brazo{su:+d}', 'madera', ch, 0.06, 0.05, 0.5, su * 0.3, 0.68, 0.3, r=0.015))
                out.append(gbox(f'silla{j}_apoyo{su:+d}', 'madera', ch, 0.05, 0.26, 0.05, su * 0.3, 0.44, 0.52, r=0.01))
        out.append(gbox(f'silla{j}_respaldo', 'madera', ch, 0.6, hh - 0.4, 0.06, 0, 0.44, 0.03, r=0.012))
        out.append(gbox(f'silla{j}_tapiz', 'terciopelo', ch, 0.46, hh - 0.62, 0.03, 0, 0.56, 0.065, r=0.012))
        crest = [(-0.3, 0.0), (0.3, 0.0)] + [(0.3 * math.cos(math.pi * k / 10), 0.1 + 0.12 * math.sin(math.pi * k / 10)) for k in range(11)]
        out.append(board(f'silla{j}_copete', 'madera', crest, ch.p(0, hh + 0.04, 0.03), ch.U, ch.V, ch.W, 0.05, r=0.01))
    return out

# ---------------------------------------------------------------- the pulpit
def pulpito():
    """on the Gospel side, against the pier between the second and third bays: a granite cup on its column (mouldings
    round it), an iron stair with its handrail and balusters, the sounding board of wood under a gilded crown"""
    out = []
    px, pz = K.BAYS[1][1], -K.HW + 1.25
    prof = [(0, 0), (0.3, 0), (0.3, 0.06), (0.22, 0.1), (0.2, 0.3), (0.18, 0.35), (0.18, 1.9), (0.22, 1.95), (0.24, 2.05),
            (0.32, 2.2), (0.5, 2.32), (0.62, 2.42), (0.66, 2.48), (0.66, 2.55), (0.7, 2.6), (0.7, 3.32), (0.76, 3.38),
            (0.76, 3.46), (0.72, 3.5), (0.62, 3.5), (0.62, 3.42), (0, 3.42)]
    out.append(turned('pulpito_copa', 'piedra', (px, 0, pz), prof, seg=40))
    # the sounding board: a wooden disc with its moulded edge, a gilded crown and finial over it; its back panel
    tb = (px, 5.8, pz - 0.3)
    out.append(turned('pulpito_tornavoz', 'madera', tb, [(0, 0), (0.95, 0), (0.98, 0.03), (0.98, 0.09), (0.92, 0.13), (0, 0.13)], seg=40))
    out.append(turned('pulpito_corona', 'talla', (px, 5.93, pz - 0.3), [(0, 0)] + [(0.88 * math.cos(math.pi / 2 * k / 8), 0.42 * math.sin(math.pi / 2 * k / 8)) for k in range(9)][:-1] + [(0.0, 0.42)], seg=40))
    out += finial('pulpito_remate', Plano(-math.pi / 2, px, pz - 0.3, 0.0), 0.0, 6.35, 0.0, 0.9)
    out.append(board('pulpito_respaldo', 'madera', [(-0.4, 0.0), (0.4, 0.0), (0.4, 1.9), (0.0, 2.2), (-0.4, 1.9)], (px, 3.5, pz - 0.72), Vector((0, 0, 1)), Vector((0, 1, 0)), Vector((1, 0, 0)), 0.08, r=0.01))
    # the stair: ten iron treads on two stringers, balusters, a handrail
    for i in range(10):
        x = px + 0.9 + i * 0.22; y = 0.34 * (i + 1)
        out.append(gbox(f'pulpito_peldano{i}', 'hierro', Plano(-math.pi / 2, x, pz + 0.2, 0.0), 0.7, 0.03, 0.26, 0, y - 0.015, 0.0, r=0.006))
        out.append(bar(f'pulpito_balaustre{i}', 'hierro', (x, y, pz + 0.52), (x, y + 0.9, pz + 0.52), Vector((1, 0, 0)), Vector((0, 0, 1)), rrect(0.018, 0.018, 0.004)))
    for sz in (-0.13, 0.53):
        out.append(bar(f'pulpito_zanca{sz}', 'hierro', (px + 0.75, 0.2, pz + sz), (px + 3.0, 3.6, pz + sz), Vector((0, 0, 1)), Vector((-0.83, 0.55, 0)), rrect(0.02, 0.12, 0.006)))
    out.append(bar('pulpito_pasamanos', 'hierro', (px + 0.75, 1.25, pz + 0.52), (px + 3.0, 4.45, pz + 0.52), Vector((0, 0, 1)), Vector((-0.82, 0.57, 0)), rrect(0.04, 0.04, 0.015)))
    return out

# ---------------------------------------------------------------- the confessionals
def confesionarios():
    """two, in the doors' bay, against the chapels' backs: a booth of wood with its half-door of lattice and its
    curtain, a kneeler each side behind a pierced grille, a cornice and a crest"""
    out = []
    cx = K.BAYS[K.DOOR_BAY][0] + K.PW / 2 + 0.6
    for s in (-1, 1):
        cz = s * (K.HW + K.CD - 0.75)
        pl = Plano(0.0 if s < 0 else math.pi, cx, cz - s * 0.0, 0.0)   # (facing the nave)
        nm = f'confesionario{"N" if s < 0 else "S"}'
        out.append(gbox(nm + '_zocalo', 'madera', pl, 1.66, 0.1, 1.14, 0, 0, 0.0, r=0.01))
        out.append(gbox(nm + '_caja', 'madera', pl, 1.6, 2.2, 1.0, 0, 0.1, -0.04, r=0.012))
        out.append(moulding(nm + '_cornisa', 'madera', pl, -0.86, 0.86, 2.3, [(a * 0.5 - 0.5, b * 0.45) for a, b in ENT_PROF]))
        # the middle: the priest's half-door (lattice above, a panel below) and the curtain behind
        out.append(gbox(nm + '_puerta', 'madera', pl, 0.62, 0.9, 0.04, 0, 0.12, 0.48, r=0.008))
        for k in range(6):
            out.append(gbox(f'{nm}_celosia_v{k}', 'madera', pl, 0.02, 0.5, 0.025, -0.25 + k * 0.1, 1.02, 0.48, r=0.004))
        out.append(gbox(nm + '_cortina', 'terciopelo', pl, 0.6, 1.6, 0.02, 0, 0.55, 0.44, r=0.006))
        # the kneelers each side: a step, an arm, a grille of pierced wood
        for su in (-1, 1):
            out.append(gbox(f'{nm}_reclinatorio{su:+d}', 'madera', pl, 0.42, 0.14, 0.32, su * 0.62, 0.1, 0.56, r=0.01))
            out.append(gbox(f'{nm}_rejilla{su:+d}', 'madera', pl, 0.3, 0.42, 0.03, su * 0.62, 1.02, 0.47, r=0.006))
            for k in range(4):
                out.append(gbox(f'{nm}_rejilla{su:+d}_{k}', 'hierro', pl, 0.012, 0.36, 0.012, su * 0.62 - 0.11 + k * 0.073, 1.05, 0.49, r=0.003))
        crest = [(-0.75, 0.0), (0.75, 0.0)] + [(0.75 * math.cos(math.pi * k / 14), 0.12 + 0.3 * math.sin(math.pi * k / 14)) for k in range(15)]
        out.append(board(nm + '_copete', 'madera', crest, pl.p(0, 2.58, 0.0), pl.U, pl.V, pl.W, 0.06, r=0.012))
        out += finial(nm + '_remate', pl, 0, 2.98, 0.0, 0.6, flame=False)
    return out

# ---------------------------------------------------------------- the font and its chapel's grille
def bautismo():
    """the baptismal chapel: the font (a gadrooned granite cup on a baluster foot, a wooden lid, a brass cross), the
    frame of its painting, the wrought-iron grille across its arch"""
    out = []
    xa, xb, xm = K.BAYS[0]; s = -1
    fz = s * (K.HW + 1.6)
    out.append(turned('pila_pie', 'piedra', (xm, 0, fz), [(0, 0), (0.32, 0), (0.32, 0.08), (0.24, 0.14), (0.18, 0.3), (0.16, 0.5), (0.22, 0.58), (0.2, 0.62), (0, 0.62)], seg=32))
    gad = lambda a, t: (0.2 + 0.42 * math.sin(t * math.pi / 2) ** 0.8) * (1 + 0.05 * max(0.0, math.cos(a * 12)) * (1 - t))
    out.append(lathe_fn('pila_copa', 'piedra', (xm, 0.6, fz), gad, 0.42, seg=96, rows=10, cap1=True))
    out.append(turned('pila_borde', 'piedra', (xm, 1.0, fz), [(0, 0), (0.64, 0), (0.66, 0.03), (0.64, 0.06), (0, 0.06)], seg=48))
    out.append(turned('pila_tapa', 'madera', (xm, 1.06, fz), [(0, 0), (0.64, 0), (0.6, 0.06), (0.3, 0.26), (0.08, 0.36), (0.06, 0.42), (0, 0.42)], seg=40))
    out.append(gbox('pila_cruz_v', 'dorado', Plano(0.0, xm, fz, 0.0), 0.03, 0.26, 0.03, 0, 1.46, 0.0))
    out.append(gbox('pila_cruz_h', 'dorado', Plano(0.0, xm, fz, 0.0), 0.14, 0.03, 0.03, 0, 1.62, 0.0))
    # the painting's frame (the canvas is church.js's)
    zb = s * (K.HW + K.CD - 0.15)
    out.append(rect_frame('bautismo_marco', Plano(0.0, xm, zb + 0.02, 0.0), 0, 1.9, 1.84, 2.64, 0.0, prof=[(a * 1.2, b) for a, b in FRAME]))
    # the grille: bars with spear tips, two rails, scrolls along its top
    gz = s * (K.HW + 0.35)
    x0, x1 = xa + K.PW / 2 + 0.3, xb - K.PW / 2 - 0.2
    n = int((x1 - x0) / 0.14)
    for i in range(n + 1):
        x = x0 + i * 0.14
        out.append(bar(f'reja_barrote{i}', 'hierro', (x, 0.08, gz), (x, 2.05, gz), Vector((1, 0, 0)), Vector((0, 0, 1)), rrect(0.022, 0.022, 0.004)))
        out.append(turned(f'reja_lanza{i}', 'hierro', (x, 2.05, gz), [(0, 0), (0.016, 0), (0.03, 0.05), (0, 0.14)], seg=6))
    for y in (0.15, 1.95):
        out.append(bar(f'reja_travesano{y}', 'hierro', (x0 - 0.05, y, gz), (x1 + 0.05, y, gz), Vector((0, 1, 0)), Vector((0, 0, 1)), rrect(0.05, 0.03, 0.006)))
    for i in range(0, n, 2):
        c = Vector((x0 + (i + 1) * 0.14, 1.75, gz)); m = 12
        pts = [c + Vector((0.07 * math.cos(2 * math.pi * k / m * 0.85), 0.07 * math.sin(2 * math.pi * k / m * 0.85), 0)) for k in range(m + 1)]
        out.append(K.sweep(f'reja_voluta{i}', pts, [(q - c).normalized() for q in pts], [Vector((0, 0, 1))] * len(pts), [(0.007 * math.cos(2 * math.pi * k / 6), 0.007 * math.sin(2 * math.pi * k / 6)) for k in range(6)], 'hierro', close_profile=True, caps=True))
    return out

# ---------------------------------------------------------------- the small things: stoups, the collection box, the Stations
def menores():
    """holy water stoups at the doors (a scalloped granite shell on a baluster), the collection box by the main door (oak
    with iron straps, on an iron post), the fourteen Stations' frames on the piers, a wooden cross over each (their
    pictures are church.js's)"""
    out = []
    sx3 = K.BAYS[K.DOOR_BAY][2]
    for j, (x, z) in enumerate(((K.X0 + 3.0, -2.6), (K.X0 + 3.0, 2.6), (sx3 - 2.4, K.HW + K.CD - 2.9))):
        out.append(turned(f'pila_agua{j}_pie', 'piedra', (x, 0, z), [(0, 0), (0.2, 0), (0.2, 0.06), (0.13, 0.12), (0.1, 0.3), (0.12, 0.55), (0.09, 0.66), (0.11, 0.78), (0, 0.78)], seg=24))
        shell = lambda a, t: (0.08 + 0.3 * math.sin(t * math.pi / 2) ** 0.9) * (1 + 0.07 * abs(math.cos(a * 8)) * t)
        out.append(lathe_fn(f'pila_agua{j}_concha', 'piedra', (x, 0.76, z), shell, 0.24, seg=96, rows=8))
    # the collection box
    bx, bz = K.X0 + 0.5, 2.5
    out.append(bar('cepillo_poste', 'hierro', (bx, 0.0, bz), (bx, 0.78, bz), Vector((1, 0, 0)), Vector((0, 0, 1)), rrect(0.08, 0.08, 0.01)))
    out.append(gbox('cepillo_caja', 'madera', Plano(-math.pi / 2, bx, bz, 0.0), 0.25, 0.42, 0.33, 0, 0.78, 0.0, r=0.012))
    for yy in (0.84, 1.12):
        out.append(gbox(f'cepillo_fleje{yy}', 'hierro', Plano(-math.pi / 2, bx, bz, 0.0), 0.27, 0.025, 0.35, 0, yy, 0.0, r=0.004))
    out.append(gbox('cepillo_tapa', 'madera', Plano(-math.pi / 2, bx, bz, 0.0), 0.29, 0.05, 0.37, 0, 1.2, 0.0, r=0.015))
    # the Stations: church.js's places (on the piers, either side, fourteen)
    n = 0
    for s in (-1, 1):
        for i in range(K.NB + 1):
            for dx in (-0.75, 0.75):
                if n >= 14: break
                x = K.XC + i * K.BAY + dx
                if x > K.XP - 1 or x < K.XC: continue
                pl = Plano(0.0 if s < 0 else math.pi, x, s * (K.HW + 0.8), 0.0)
                out.append(rect_frame(f'via{n}_marco', pl, 0, 2.9 - 0.27, 0.46, 0.56, 0.0, prof=[(a * 0.45, b * 0.5) for a, b in FRAME]))
                out.append(gbox(f'via{n}_cruz_v', 'madera', pl, 0.035, 0.28, 0.03, 0, 3.27, 0.01, r=0.006))
                out.append(gbox(f'via{n}_cruz_h', 'madera', pl, 0.17, 0.035, 0.03, 0, 3.44, 0.01, r=0.006))
                n += 1
    return out

# ---------------------------------------------------------------- all of it
ROLES = {
    # (colour, roughness, the texture's tile in metres) — as interior.py's ROLE
    'madera': ((0.30, 0.17, 0.10), 0.55, 2.0),       # (Poly Haven «Dark Wood»: a 2 m tile)
    'terciopelo': ((0.35, 0.05, 0.08), 0.8, 0.28),   # («Velour Velvet»: 0,28 m)
    'dorado': ((0.78, 0.56, 0.22), 0.3, 0.5),       # (gilding, burnished: own texture)
    'talla': ((0.72, 0.5, 0.2), 0.45, 0.5),         # (gilding over carving: own texture, the bole in its hollows)
    'plata': ((0.8, 0.8, 0.82), 0.3, 0.5),
    'blanco': ((0.85, 0.83, 0.78), 0.5, 0.5),
    'azul': ((0.06, 0.12, 0.35), 0.8, 0.8),
    'lino': ((0.86, 0.85, 0.82), 0.9, 0.27),        # («Rough Linen»: 0,27 m, whitened)
    'piedra': ((0.5, 0.5, 0.49), 0.78, 0.7),        # (the altars' granite: the architecture's texture, a role of its own)
    'marmol': ((0.86, 0.85, 0.83), 0.35, 1.2),      # (white marble with grey veins: own texture)
    'hierro': ((0.05, 0.05, 0.055), 0.55, 0.5),     # (wrought iron, black)
}

TEXTURE = {'piedra': 'granito'}   # (a role dressed in another's texture)
GROUPS = {'bancos': lambda: pews(), 'retablo': lambda: retablo_mayor(), 'organo': lambda: organo(), 'colaterales': lambda: colaterales(), 'presbiterio': lambda: presbiterio(), 'pulpito': lambda: pulpito(), 'confesionarios': lambda: confesionarios(), 'bautismo': lambda: bautismo(), 'menores': lambda: menores()}
BUILT = []   # (the groups made: interior.json's 'muebles' — the game hides church.js's own of each)

def build(kit, only=None):
    global K
    K = kit
    for r, v in ROLES.items(): K.ROLE.setdefault(r, v)
    out = []
    for name, make in GROUPS.items():
        if not only or name in only:
            out += make(); BUILT.append(name)
    return out
