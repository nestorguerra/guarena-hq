# Santa María de Guareña inside, in high definition (docs/hiperrealismo.md, «El interior (fase 6)», is the source of
# truth). The measures are src/church.js's — its doors, colliders, spots, pews and the mass keep fitting — and the
# model replaces only its architecture, in the Realista look (src/hiperinterior.js). Built in Blender, headless:
#   /Applications/Blender.app/Contents/MacOS/Blender --background --factory-startup --python tools/blender/interior.py -- \
#       [--greybox] [--sin-luz] [--muebles .cache/hq/interior/muebles.glb] [--muestras 1024] [--out assets/hq/interior]
# --greybox: grey, no light (the volumes, to compare with church.js and the photo). Without it, the light is baked in
# Cycles over a second UV set (--sin-luz skips it): the sky through the windows, the sun's bounce at five hours of the
# game's day, and the night's lamps — each into its own lightmap (luz/*.jpg, their scales in interior.json). The
# church's furniture, exported from the game (--muebles), stands in the bake to cast its shadows; it is not exported.
# Blender is Z-up: a point (x, y up, z) of the church's inside (x towards the altar, z south) is made at Blender
# (x, -z, y); the glTF exporter gives three.js back its (x, y, z) on INTERIOR_ORIGIN.
import bpy, bmesh, json, math, os, sys
from mathutils import Vector

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
ARGS = sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else []
def arg(k, d=None): return ARGS[ARGS.index(k) + 1] if k in ARGS else d
GREY = '--greybox' in ARGS
LIGHT = not GREY and '--sin-luz' not in ARGS
OUT = os.path.abspath(arg('--out', os.path.join(ROOT, 'assets', 'hq', 'interior')))
MUEBLES = arg('--muebles')
# (--muebles-hd [grupos,separados]: the furniture in high definition, tools/blender/muebles.py — baked and exported
# with the architecture; without a list, all of it)
MUEBLES_HD = (arg('--muebles-hd', '') or 'todo') if '--muebles-hd' in ARGS else None
if MUEBLES_HD and MUEBLES_HD.startswith('--'): MUEBLES_HD = 'todo'
SAMPLES = int(arg('--muestras', '1024'))
LM_RES = int(arg('--lm', '3072'))          # the sky's and the lamps' lightmaps
SUN_RES = int(arg('--lm-sol', str(min(2048, LM_RES))))  # the sun's bounce (smoother: smaller maps)
# (the sun's bounce comes off a few small, very bright patches — the sunlit floor — and a path finds them seldom: four
# times the samples, or the denoiser leaves blotches the size of a hand on columns and corners)
SUN_SAMPLES = int(arg('--muestras-sol', str(4 * SAMPLES)))
BILATERAL = '--sin-bilateral' not in ARGS   # (the joint bilateral filter after the denoiser: see bilateral())

# ---------------------------------------------------------------- the measures (src/church.js; docs/hiperrealismo.md)
HW = 8.0                 # half the nave between the columns
X0 = -26.5               # the west wall's inner face
XC = -19.5               # the front of the choir
BAY, NB = 9.5, 4         # four bays
XA = XC + BAY * NB       # 18.5: the triumphal arch; the apse beyond (a semicircle round (XA, 0))
AR = HW                  # the apse's radius
S = 12.4                 # the vaults' springing
CD = 3.1                 # the chapels' depth
PW = 2.4                 # the piers' width along x
CHY = 6.2                # the choir's floor
P = 0.9                  # the presbytery's floor (five steps)
XP = 13.6                # its first step
NS = 5
CH_H = 10.2              # the chapels' walls
WALL_H = S + 9.0         # the walls' top (above the vaults)
TH = 1.2                 # the outer walls (the doors' reveals are 1,05 deep in church.js)
THN = 1.4                # the nave's upper walls
PIERS = [XC + i * BAY for i in range(NB + 1)]
BAYS = [(PIERS[i], PIERS[i + 1], (PIERS[i] + PIERS[i + 1]) / 2) for i in range(NB)]
DOOR_BAY = 2
# the nave's windows (the photo outside: the light 1,4 × 3,8 m, sills at 14,6, crowns at 18,4); inside, the splay opens
# them to 2,1 m, from 13,4 to 18,6 — in the vault's lunette, over the impost (church.js had them lower, across it)
WIN = {'w': 2.1, 'y0': 13.4, 'y1': 18.6, 'light': 1.4, 'ly0': 14.6, 'ly1': 18.4}
LUNETTE = 7.0            # the lunettes' rise over the springing (their wall ribs clear the windows)
APSE_WIN = {'w': 0.88, 'y0': 8.6, 'y1': 11.6, 'a': 1.30}   # two, at the apse's sides by the arch's columns (the photo shows none beside the retablo: its light comes in at the edges)
OCULUS = {'y': 10.0, 'r': 1.6, 'splay': 2.05}              # the great oculus over the west door (the photo: centre at 10 m)
DOORS = {'oeste': {'w': 2.6, 'spring': 3.7}, 'sur': {'w': 2.3, 'spring': 3.3}, 'norte': {'w': 2.2, 'spring': 3.2}}
SACRISTY_A = 1.32        # the sacristy's door in the apse wall (the Backrooms)
STAIR_DOOR = (X0 + 3.2, X0 + 4.4, 2.3)
COL = {'h0': 1.5, 'r0': 0.67, 'r1': 0.62, 'cap': S - 1.15}  # the columns: pedestal, shaft radii, the capital's foot

# ---------------------------------------------------------------- the scene
bpy.ops.wm.read_factory_settings(use_empty=True)
SC = bpy.context.scene
COLL = SC.collection
def B(p): return Vector((p[0], -p[2], p[1]))  # (x, height, z) → Blender
def F(v): return Vector((v[0], v[2], -v[1]))  # Blender → (x, height, z)

# the roles: (colour, roughness, the texture's tile in metres). Their names are the materials the game dresses
# (hiperinterior.js): cal — whitewash; granito — granite without joints (capitals, bases, mouldings, coffers); tambor —
# granite in drums or voussoirs (joints across v); sillar — granite ashlar (joints both ways); suelo — the floor's slabs;
# oro — gilded; vidrio — the windows; oclusor — only in the bake (the roof, doors, furniture)
ROLE = {
    'cal': ((0.80, 0.79, 0.76), 0.92, 1.6),
    'granito': ((0.50, 0.50, 0.49), 0.78, 0.7),
    'tambor': ((0.50, 0.50, 0.49), 0.78, 0.7),
    'fuste': ((0.50, 0.50, 0.49), 0.78, 0.7),
    'caseton': ((0.50, 0.50, 0.49), 0.78, 0.7),
    'caseton_fondo': ((0.40, 0.40, 0.40), 0.85, 0.7),
    'sillar': ((0.48, 0.48, 0.47), 0.8, 0.7),
    'suelo': ((0.40, 0.40, 0.39), 0.6, 4.1),
    'oro': ((0.75, 0.52, 0.2), 0.35, 0.5),
    'vidrio': ((0.85, 0.88, 0.84), 0.3, 1.0),
    'oclusor': ((0.25, 0.2, 0.16), 0.8, 1.0),
    'sonda': ((0.8, 0.8, 0.8), 1.0, 1.0),
}
MATS = {}
def M(role):
    if role in MATS: return MATS[role]
    m = bpy.data.materials.new(role); m.use_nodes = True
    p = m.node_tree.nodes['Principled BSDF']
    col, rough, _ = ROLE[role]
    if GREY and role not in ('vidrio', 'oclusor'): col, rough = (0.55, 0.55, 0.53), 0.9
    p.inputs['Base Color'].default_value = (*col, 1); p.inputs['Roughness'].default_value = rough
    if role == 'oro' and not GREY: p.inputs['Metallic'].default_value = 1.0
    MATS[role] = m
    return m

# ---------------------------------------------------------------- building blocks (each with its UVs in metres)
class Mesh:
    """a piece being built: verts in the church's frame, faces, a UV (in metres) per face corner or none (box-projected)
    — and, for a carved piece the light's atlas would cut into slivers (a fluted shaft, a coffered dome), a lightmap UV
    of its own in metres (lm): a projection that keeps it one island (its faces marked 'lm_fijo')"""
    def __init__(self, name, role):
        self.name, self.role = name, role
        self.v, self.f, self.ao = [], [], []
    def vert(self, p, ao=1.0):
        self.v.append(Vector(p)); self.ao.append(ao); return len(self.v) - 1
    def face(self, idx, uvs=None, lm=None):
        self.f.append((tuple(idx), uvs, lm))
    def grid(self, rows, uvrows=None, close=False, lmrows=None):
        """rows of vertex indices, each the same length, joined in quads (close: the last point of a row to its first)"""
        for r in range(len(rows) - 1):
            a, b = rows[r], rows[r + 1]
            n = len(a) if close else len(a) - 1
            for i in range(n):
                j = (i + 1) % len(a)
                uv = lm = None
                if uvrows:
                    ua, ub = uvrows[r], uvrows[r + 1]
                    uv = [ua[i], ua[j], ub[j], ub[i]]
                if lmrows:
                    la, lb = lmrows[r], lmrows[r + 1]
                    lm = [la[i], la[j], lb[j], lb[i]]
                self.face([a[i], a[j], b[j], b[i]], uv, lm)
    def build(self):
        bm = bmesh.new()
        # (each vertex's occlusion, 1 but in a carved recess: the game darkens the baked light by it — 'Col', exported
        # as the glTF's COLOR_0; the layers before the geometry: a new layer moves the data and loses its references)
        col = bm.verts.layers.color.new('Col')
        uvl = bm.loops.layers.uv.new('UVMap')
        haslm = any(f[2] for f in self.f)
        lml = bm.loops.layers.uv.new('LM') if haslm else None
        fijo = bm.faces.layers.int.new('lm_fijo') if haslm else None
        vs = [bm.verts.new(B(p)) for p in self.v]
        for v, ao in zip(vs, self.ao): v[col] = (ao, ao, ao, 1.0)
        t = ROLE[self.role][2]
        for idx, uvs, lm in self.f:
            if len(set(idx)) < 3: continue
            try: f = bm.faces.new([vs[i] for i in idx])
            except ValueError: continue
            if lm:
                for l, uv in zip(f.loops, lm): l[lml].uv = uv
                f[fijo] = 1
            if uvs:
                for l, uv in zip(f.loops, uvs): l[uvl].uv = (uv[0] / t, uv[1] / t)
            else:
                f.normal_update(); n = f.normal
                for l in f.loops:
                    p = l.vert.co
                    if abs(n.z) > max(abs(n.x), abs(n.y)): l[uvl].uv = (p.x / t, p.y / t)
                    elif abs(n.x) > abs(n.y): l[uvl].uv = (p.y / t, p.z / t)
                    else: l[uvl].uv = (p.x / t, p.z / t)
        bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=1e-5)
        bmesh.ops.dissolve_degenerate(bm, edges=bm.edges, dist=1e-6)
        me = bpy.data.meshes.new(self.name); bm.to_mesh(me); bm.free()
        ob = bpy.data.objects.new(self.name, me); COLL.objects.link(ob)
        me.materials.append(M(self.role))
        return ob

def closed(ob):
    """a closed solid: its faces turned out"""
    bm = bmesh.new(); bm.from_mesh(ob.data)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bm.to_mesh(ob.data); bm.free()
    return ob

def facing(ob, want):
    """an open surface (its winding consistent) turned to face where `want(centre)` says — a direction in the church's
    frame — by the vote of its faces, by area"""
    me = ob.data; vote = 0.0
    for p in me.polygons:
        c = F(p.center); n = F(p.normal)
        vote += p.area * n.dot(Vector(want(c)))
    if vote < 0:
        bm = bmesh.new(); bm.from_mesh(me)
        bmesh.ops.reverse_faces(bm, faces=bm.faces)
        bm.to_mesh(me); bm.free()
    return ob

def solid(name, pts, y0, y1, role):
    """an upright prism over a plan polygon [(x, z)]"""
    m = Mesh(name, role); n = len(pts)
    lo = [m.vert((x, y0, z)) for x, z in pts]; hi = [m.vert((x, y1, z)) for x, z in pts]
    for i in range(n):
        j = (i + 1) % n
        m.face([lo[i], lo[j], hi[j], hi[i]])
    m.face(hi[::-1]); m.face(lo)
    return closed(m.build())

def cube(name, x0, x1, z0, z1, y0, y1, role):
    x0, x1 = min(x0, x1), max(x0, x1); z0, z1 = min(z0, z1), max(z0, z1)
    return solid(name, [(x0, z0), (x1, z0), (x1, z1), (x0, z1)], y0, y1, role)

def plate(name, shape, origin, ax_u, ax_v, ax_n, d0, d1, role):
    """a 2D outline (u, v) set on a plane (origin, axes u and v), made solid from d0 to d1 along its normal n"""
    o, U, Vv, N = Vector(origin), Vector(ax_u), Vector(ax_v), Vector(ax_n)
    m = Mesh(name, role); n = len(shape)
    a = [m.vert(o + U * u + Vv * v + N * d0) for u, v in shape]
    b = [m.vert(o + U * u + Vv * v + N * d1) for u, v in shape]
    for i in range(n):
        j = (i + 1) % n
        m.face([a[i], a[j], b[j], b[i]])
    m.face(a[::-1]); m.face(b)
    return closed(m.build())

def lathe(name, profile, centre, role, seg=32, a0=0.0, a1=2 * math.pi, axis='y'):
    """a profile [(r, h)] turned round an axis through `centre` (up y; or along x, or z), from angle a0 to a1. UVs: round
    the arc at its radius, and along the profile. A whole turn whose profile ends on the axis is a closed solid;
    otherwise its faces are turned away from the axis"""
    c = Vector(centre); full = abs(a1 - a0 - 2 * math.pi) < 1e-6
    m = Mesh(name, role); rows, uvs = [], []
    s = 0.0
    for k, (r, h) in enumerate(profile):
        if k: s += math.hypot(r - profile[k - 1][0], h - profile[k - 1][1])
        row, uvr = [], []
        for i in range(seg + 1):
            a = a0 + (a1 - a0) * i / seg
            if axis == 'y': p = c + Vector((r * math.cos(a), h, r * math.sin(a)))
            elif axis == 'x': p = c + Vector((h, r * math.sin(a), r * math.cos(a)))
            else: p = c + Vector((r * math.cos(a), r * math.sin(a), h))
            row.append(m.vert(p)); uvr.append(((a - a0) * max(r, 0.05), s))
        rows.append(row); uvs.append(uvr)
    m.grid(rows, uvs, lmrows=uvs)   # (the light's atlas: one island, unrolled round the axis)
    ob = m.build()
    if full and profile[0][0] < 1e-6 and profile[-1][0] < 1e-6: return closed(ob)
    ax = {'y': Vector((0, 1, 0)), 'x': Vector((1, 0, 0)), 'z': Vector((0, 0, 1))}[axis]
    def away(p):
        d = p - c; d -= ax * d.dot(ax)
        return d
    return facing(ob, away)

def sweep(name, path, n1s, n2s, profile, role, close_profile=True, caps=True, want=None):
    """a profile [(a, b)] carried along a path: at each point p the vertex p + n1·a + n2·b (n1, n2 given per point).
    UVs: u along the profile, v along the path (in metres: the drums' and voussoirs' joints run across v). A closed
    profile with its two ends capped is a solid; else `want` turns its faces"""
    path = [Vector(p) for p in path]
    m = Mesh(name, role)
    along = [0.0]
    for i in range(1, len(path)): along.append(along[-1] + (path[i] - path[i - 1]).length)
    plen = [0.0]
    for k in range(1, len(profile)): plen.append(plen[-1] + math.hypot(profile[k][0] - profile[k - 1][0], profile[k][1] - profile[k - 1][1]))
    if close_profile: plen.append(plen[-1] + math.hypot(profile[0][0] - profile[-1][0], profile[0][1] - profile[-1][1]))
    rows, uvs = [], []
    for i, p in enumerate(path):
        a1, a2 = Vector(n1s[i]), Vector(n2s[i])
        row = [m.vert(p + a1 * a + a2 * b) for a, b in profile]
        uv = [(plen[k], along[i]) for k in range(len(profile))]
        if close_profile: row.append(row[0]); uv.append((plen[-1], along[i]))
        rows.append(row); uvs.append(uv)
    m.grid(rows, uvs, lmrows=uvs)   # (the light's atlas: one island, unrolled — its seam where the profile closes)
    if caps:
        m.face(rows[0][:len(profile)][::-1]); m.face(rows[-1][:len(profile)])
    ob = m.build()
    if close_profile and caps: return closed(ob)
    return facing(ob, want) if want else ob

def surface(name, f, nu, nv, role, want, uv=None):
    """a surface p = f(u, v) over a grid, turned to face `want`; uv(u, v) → (u, v) in metres, or box-projected. Its
    unwrap for the light: each grid row along its own arc length, each column along its own — one island, no folds"""
    m = Mesh(name, role); rows, uvs = [], []
    P = [[Vector(f(i / nu, j / nv)) for i in range(nu + 1)] for j in range(nv + 1)]
    for j in range(nv + 1):
        rows.append([m.vert(P[j][i]) for i in range(nu + 1)])
        if uv: uvs.append([uv(i / nu, j / nv) for i in range(nu + 1)])
    U = [[0.0] * (nu + 1) for _ in range(nv + 1)]; V = [[0.0] * (nu + 1) for _ in range(nv + 1)]
    for j in range(nv + 1):
        for i in range(1, nu + 1): U[j][i] = U[j][i - 1] + (P[j][i] - P[j][i - 1]).length
    for i in range(nu + 1):
        for j in range(1, nv + 1): V[j][i] = V[j - 1][i] + (P[j][i] - P[j - 1][i]).length
    lms = [[(U[j][i], V[j][i]) for i in range(nu + 1)] for j in range(nv + 1)]
    m.grid(rows, uvs if uv else None, lmrows=lms)
    return facing(m.build(), want)

def cut(target, *cutters):
    """booleans (Manifold): the faces each cutter leaves take the cutter's material (a window's or door's reveal: granite)"""
    for c in cutters:
        md = target.modifiers.new('hueco', 'BOOLEAN'); md.operation = 'DIFFERENCE'; md.object = c
        md.solver = 'EXACT'
        try: md.material_mode = 'TRANSFER'
        except Exception: pass
        bpy.context.view_layer.objects.active = target
        try: bpy.ops.object.modifier_apply(modifier=md.name)
        except RuntimeError as e: print('corte fallido', target.name, c.name, e)
        bpy.data.objects.remove(c)
    return target

def arch_outline(w, spring, bottom=0.0, seg=24):
    """a round-headed opening (u across, v up): its jambs from `bottom`, a semicircle over them centred at `spring`"""
    r = w / 2
    return [(-r, bottom), (r, bottom)] + [(r * math.cos(math.pi * k / seg), spring + r * math.sin(math.pi * k / seg)) for k in range(seg + 1)]

def pointed_outline(w, y0, rise, n=12):
    """a pointed (two-centred) arch from u −w/2 to w/2, springing at y0, rising `rise` (church.js's pointedArch)"""
    R = (w * w / 4 + rise * rise) / w
    out = []
    for i in range(n + 1):
        u = -w / 2 + (w / 2) * i / n; cu = -w / 2 + R
        out.append((u, y0 + math.sqrt(max(0.0, R * R - (u - cu) ** 2))))
    for i in range(n - 1, -1, -1): out.append((-out[i][0], out[i][1]))
    return out, R

def circle(r, n, cu, cv):
    return [(cu + r * math.cos(2 * math.pi * k / n), cv + r * math.sin(2 * math.pi * k / n)) for k in range(n)]

def wall_cutter(name, outline, cx, cz, nx, nz, d0, d1, role='sillar'):
    """a prism of an opening's outline (u along the wall, v up) through a wall at (cx, cz) whose inward normal is (nx,
    nz), from d0 to d1 outward"""
    return plate(name, outline, (cx, 0, cz), (-nz, 0, nx), (0, 1, 0), (-nx, 0, -nz), d0, d1, role)

def splayed_cutter(name, inner, outer, cx, cz, nx, nz, d_in, d_mid, d_out, role='sillar'):
    """an opening that narrows from its inner outline (at the wall's face) to the outer one (at d_mid), and goes on so
    to d_out: a window's splay. Both outlines the same number of points"""
    U, N, o = Vector((-nz, 0, nx)), Vector((-nx, 0, -nz)), Vector((cx, 0, cz))
    m = Mesh(name, role); n = len(inner)
    rings = [[m.vert(o + U * u + Vector((0, v, 0)) + N * d) for u, v in shape] for shape, d in ((inner, d_in), (outer, d_mid), (outer, d_out))]
    for a, b in zip(rings, rings[1:]):
        for i in range(n):
            j = (i + 1) % n
            m.face([a[i], a[j], b[j], b[i]])
    m.face(rings[0][::-1]); m.face(rings[-1])
    return closed(m.build())

def outline_normals(pts2):
    """for a 2D polyline (an opening's edge, u across, v up), each point's normal in its plane pointing away from the
    opening (the edge runs over it from the left springing to the right: its left-hand side is outside)"""
    out = []
    for i, p in enumerate(pts2):
        a = pts2[max(i - 1, 0)]; b = pts2[min(i + 1, len(pts2) - 1)]
        t = (b[0] - a[0], b[1] - a[1]); l = math.hypot(*t) or 1
        out.append((-t[1] / l, t[0] / l))
    return out

def edge_moulding(name, pts2, origin, U, Vv, N, profile, role):
    """a moulding round an opening's edge on a wall (pts2: the edge in the wall's (u, v), anticlockwise from the left
    springing): profile (a, b) — a away from the opening in the wall's plane, b out of the wall (along N)"""
    o, U, Vv, N = Vector(origin), Vector(U), Vector(Vv), Vector(N)
    path = [o + U * u + Vv * v for u, v in pts2]
    nrm = outline_normals(pts2)
    n1 = [U * a + Vv * b for a, b in nrm]
    return sweep(name, path, n1, [N] * len(path), profile, role)

def join(name, obs):
    obs = [o for o in obs if o]
    if not obs: return None
    bpy.ops.object.select_all(action='DESELECT')
    for o in obs: o.select_set(True)
    bpy.context.view_layer.objects.active = obs[0]
    if len(obs) > 1: bpy.ops.object.join()
    obs[0].name = name
    return obs[0]

# ================================================================ the vault's shape
def vault_y(x, z, xa, xb, rT=HW, dome=0.5, lun=LUNETTE):
    """the web of a nave bay over [xa, xb] × [−HW, HW]: a barrel across the nave (radius HW) and the lunettes along it
    (rising `lun` over the springing, for the windows), meeting in groins, a little domed (church.js's vaultY, its
    lunettes raised)"""
    L = xb - xa; u = (x - xa) / L; v = max(-1.0, min(1.0, z / HW))
    T = rT * math.sqrt(max(0.0, 1 - v * v))
    Lb = lun * math.sqrt(max(0.0, 1 - (2 * u - 1) ** 2))
    return S + max(T, Lb) + dome * math.sin(math.pi * max(0.0, min(1.0, u))) * (1 - v * v)

def vault_up(x, z, xa, xb, **k):
    """the web's normal pointing up, into the stone (away from the nave)"""
    e = 0.01
    gx = (vault_y(x + e, z, xa, xb, **k) - vault_y(x - e, z, xa, xb, **k)) / (2 * e)
    gz = (vault_y(x, z + e, xa, xb, **k) - vault_y(x, z - e, xa, xb, **k)) / (2 * e)
    return Vector((-gx, 1.0, -gz)).normalized()

def dense(t):
    """0..1 → 0..1, crowded at both ends (where the webs rise steeply against the walls)"""
    return 0.5 - 0.5 * math.cos(math.pi * t)

DOWN = lambda c: (0, -1, 0)
UP = lambda c: (0, 1, 0)

# ================================================================ the architecture
def build_floors():
    out = []
    xs = XP + 1.5
    out.append(cube('suelo_nave', X0 - 0.05, XP, -(HW + CD) - 0.05, HW + CD + 0.05, -0.3, 0.0, 'suelo'))
    for s in (-1, 1): out.append(cube(f'suelo_capilla_cabecera_{s}', XP, PIERS[-1] - PW / 2 + 0.05, s * HW, s * (HW + CD + 0.05), -0.3, 0.0, 'suelo'))
    rise, tread = P / NS, 1.5 / NS
    for i in range(NS): out.append(step_block(f'grada_{i}', XP + i * tread, xs + 0.02, rise * (i + 1)))
    pts = [(xs, -HW), (XA, -HW)] + [(XA + AR * math.cos(a), AR * math.sin(a)) for a in [-math.pi / 2 + math.pi * k / 64 for k in range(1, 64)]] + [(XA, HW), (xs, HW)]
    out.append(solid('presbiterio', pts, -0.3, P, 'suelo'))
    return out

def step_block(name, x0, x1, top):
    """a step: a granite block from x0 to x1 (under the next ones) up to `top`, its front edge rounded (a nosing)"""
    prof = [(x1, -0.02), (x0, -0.02), (x0, top - 0.03), (x0 + 0.008, top - 0.008), (x0 + 0.03, top), (x1, top)]
    m = Mesh(name, 'sillar')
    a = [m.vert((x, y, -HW)) for x, y in prof]; b = [m.vert((x, y, HW)) for x, y in prof]
    n = len(prof)
    for i in range(n):
        j = (i + 1) % n
        m.face([a[i], a[j], b[j], b[i]])
    m.face(a[::-1]); m.face(b)
    return closed(m.build())

def build_walls():
    """the walls, solid, their openings cut: the west wall (the main door, the oculus), the choir bay's sides (the tower
    stair's door), the chapels' outer walls (the side doors in the door bay), the nave's upper walls (a window in each
    bay), the apse (its two windows)"""
    out = []
    w = cube('muro_oeste', X0 - TH, X0, -(HW + 0.3), HW + 0.3, 0.0, WALL_H, 'cal')
    D = DOORS['oeste']
    cut(w, wall_cutter('c_puerta_oeste', arch_outline(D['w'], D['spring'], bottom=-0.1), X0, 0.0, 1, 0, -0.5, TH + 0.5),
        splayed_cutter('c_oculo', circle(OCULUS['splay'], 48, 0, OCULUS['y']), circle(OCULUS['r'], 48, 0, OCULUS['y']), X0, 0.0, 1, 0, -0.01, 0.6, TH + 0.5))
    out.append(w)
    for s in (-1, 1):
        w = cube(f'muro_coro_{s}', X0 - TH, XC - PW / 2 + 0.05, s * HW, s * (HW + TH), 0.0, WALL_H, 'cal')
        if s > 0:
            a, b, h = STAIR_DOOR
            cut(w, wall_cutter('c_escalera', [(-(b - a) / 2, -0.1), ((b - a) / 2, -0.1), ((b - a) / 2, h), (-(b - a) / 2, h)], (a + b) / 2, HW, 0, -1, -0.3, 0.12))
        out.append(w)
    for i, x in enumerate(PIERS):
        for s in (-1, 1):
            out.append(cube(f'pilar_{i}_{s}', x - PW / 2, x + PW / 2, s * HW, s * (HW + CD + 0.05), 0.0, WALL_H if i == len(PIERS) - 1 else CH_H + 0.65, 'cal'))
    for bi, (xa, xb, xm) in enumerate(BAYS):
        x0, x1 = xa + PW / 2, xb - PW / 2
        for s in (-1, 1):
            zo = s * (HW + CD)
            w = cube(f'muro_capilla_{bi}_{s}', x0 - 0.2, x1 + 0.2, zo, zo + s * TH, 0.0, CH_H + 0.65, 'cal')
            if bi == DOOR_BAY:
                D = DOORS['sur' if s > 0 else 'norte']
                cut(w, wall_cutter('c_puerta', arch_outline(D['w'], D['spring'], bottom=-0.1), xm, zo, 0, -s, -0.5, TH + 0.5))
            out.append(w)
            out.append(chapel_vault(f'boveda_capilla_{bi}_{s}', x0, x1, s))
            # the wall over the chapel's arch, as thick as the nave's upper wall
            arch, _ = pointed_outline(x1 - x0 - 0.2, 6.6, 3.3, 12)
            half = (x1 - x0) / 2
            shape = [(-half, 6.6)] + [(u, y) for u, y in arch] + [(half, 6.6), (half, 10.05), (-half, 10.05)]
            out.append(plate(f'timpano_{bi}_{s}', shape, (xm, 0, s * HW), (1, 0, 0), (0, 1, 0), (0, 0, s), 0.0, THN, 'cal'))
    for s in (-1, 1):
        w = cube(f'muro_alto_{s}', XC - PW / 2, XA + 0.3, s * HW, s * (HW + THN), 10.0, WALL_H, 'cal')
        cs = []
        for bi, (xa, xb, xm) in enumerate(BAYS):
            inner = arch_outline(WIN['w'], WIN['y1'] - WIN['w'] / 2, bottom=WIN['y0'])
            outer = arch_outline(WIN['light'], WIN['ly1'] - WIN['light'] / 2, bottom=WIN['ly0'])
            cs.append(splayed_cutter(f'c_ventana_{bi}_{s}', inner, outer, xm, s * HW, 0, -s, -0.01, THN * 0.7, THN + 0.5))
        cut(w, *cs)
        out.append(w)
    out.append(apse_wall())
    return out

def chapel_vault(name, x0, x1, s):
    """a chapel's ceiling: a pointed barrel across its depth, running along x — it springs at 8,4 and its crown is at
    10,4, over the arch to the nave (whose crown is at 9,9)"""
    z0, z1 = s * HW, s * (HW + CD)
    ys, rise = 8.4, 2.0
    def f(u, v):
        x = x0 - 0.05 + (x1 - x0 + 0.1) * u
        t = v * 2 - 1
        return (x, ys + rise * (1 - abs(t) ** 1.6), (z0 + z1) / 2 + t * (z1 - z0) / 2)
    return surface(name, f, 24, 18, 'cal', DOWN)

def apse_wall():
    """the apse's wall: granite ashlar, as the photo shows it (its courses unrolled round the curve)"""
    m = Mesh('abside', 'sillar'); n = 96
    rings = []
    angs = [-math.pi / 2 + math.pi * k / n for k in range(n + 1)]
    for y in (0.0, S + 0.3):
        for r in (AR, AR + 1.5):
            rings.append([m.vert((XA + r * math.cos(a), y, r * math.sin(a))) for a in angs])
    lo_in, lo_out, hi_in, hi_out = rings
    for i in range(n):
        u0, u1 = (angs[i] + math.pi / 2) * AR, (angs[i + 1] + math.pi / 2) * AR
        m.face([lo_in[i], hi_in[i], hi_in[i + 1], lo_in[i + 1]], [(u0, 0.0), (u0, S + 0.3), (u1, S + 0.3), (u1, 0.0)], lm=[(u0, 0.0), (u0, S + 0.3), (u1, S + 0.3), (u1, 0.0)])
        m.face([lo_out[i + 1], hi_out[i + 1], hi_out[i], lo_out[i]])
        m.face([hi_in[i], hi_out[i], hi_out[i + 1], hi_in[i + 1]])
        m.face([lo_in[i + 1], lo_out[i + 1], lo_out[i], lo_in[i]])
    for k in (0, n): m.face([lo_in[k], lo_out[k], hi_out[k], hi_in[k]])
    ob = closed(m.build())
    cs = []
    for sgn in (-1, 1):
        a = sgn * APSE_WIN['a']
        cx, cz = XA + AR * math.cos(a), AR * math.sin(a)
        wi = APSE_WIN['w'] + 0.5
        inner = arch_outline(wi, APSE_WIN['y1'] + 0.2 - wi / 2, bottom=APSE_WIN['y0'] - 0.3, seg=20)
        outer = arch_outline(APSE_WIN['w'], APSE_WIN['y1'] - APSE_WIN['w'] / 2, bottom=APSE_WIN['y0'], seg=20)
        cs.append(splayed_cutter(f'c_ventana_abside_{sgn}', inner, outer, cx, cz, -math.cos(a), -math.sin(a), -0.05, 1.0, 2.0))
    return cut(ob, *cs)

# ---------------------------------------------------------------- the columns
FLUTES = 24
def flute(a):
    """the fluted shaft's radius factor round its axis: 24 hollow flutes between narrow fillets"""
    k = (a * FLUTES / (2 * math.pi)) % 1.0
    w = 0.82
    if k > w: return 1.0
    t = (k / w) * 2 - 1
    return 1.0 - 0.055 * math.sqrt(max(0.0, 1 - t * t))

def block_moulding(name, cx, cz, hx, front, back, y0, profile, role):
    """a moulding round the three outer sides of a block (centred at x cx, its front face at z `front`, its back at
    `back` in the wall): profile [(d, h)] — d out of the faces, h up — closed, its two ends capped in the wall"""
    m = Mesh(name, role)
    sgn = 1 if back > front else -1   # (the wall lies towards +z when back > front)
    rows, lms, s_ = [], [], 0.0
    for k, (d, h) in enumerate(profile):
        if k: s_ += math.hypot(d - profile[k - 1][0], h - profile[k - 1][1])
        fz = front - sgn * d
        pts = [(cx - hx - d, y0 + h, back), (cx - hx - d, y0 + h, fz), (cx + hx + d, y0 + h, fz), (cx + hx + d, y0 + h, back)]
        rows.append([m.vert(q) for q in pts])
        u = [0.0]
        for q0, q1 in zip(pts, pts[1:]): u.append(u[-1] + math.dist(q0, q1))
        lms.append([(x, s_) for x in u])
    rows.append(rows[0]); lms.append([(x, s_ + math.hypot(profile[0][0] - profile[-1][0], profile[0][1] - profile[-1][1])) for x, _ in lms[0]])
    for r in range(len(rows) - 1):
        a, b = rows[r], rows[r + 1]
        for i in range(3): m.face([a[i], a[i + 1], b[i + 1], b[i]], lm=[lms[r][i], lms[r][i + 1], lms[r + 1][i + 1], lms[r + 1][i]])
    m.face([row[0] for row in rows[:-1]]); m.face([row[3] for row in rows[:-1]][::-1])
    return closed(m.build())

def column(i, s):
    """a giant Ionic half column against pier i, side s, its front to the nave: the pedestal (base moulding, die,
    cornice), the Attic base, the fluted shaft with its entasis, the Ionic capital (astragal, echinus carved with eggs,
    two volutes facing the nave, the abacus) and the impost block over it, where the transverse arch springs"""
    x, z = PIERS[i], s * (HW + 0.05)
    out = []
    h0 = COL['h0']
    a_front = math.atan2(-s, 0)
    a0, a1 = a_front - math.radians(118), a_front + math.radians(118)
    front, back = z - s * 0.9, s * (HW + 0.6)
    out.append(cube(f'pedestal_{i}_{s}', x - 0.9, x + 0.9, front, back, 0.0, h0, 'sillar'))
    out.append(block_moulding(f'pedestal_base_{i}_{s}', x, z, 0.9, front, back, 0.0,
                              [(0.0, 0.0), (0.12, 0.0), (0.12, 0.12), (0.08, 0.16), (0.04, 0.2), (0.02, 0.26), (0.0, 0.3)], 'granito'))
    out.append(block_moulding(f'pedestal_cornisa_{i}_{s}', x, z, 0.9, front, back, h0 - 0.26,
                              [(0.0, 0.0), (0.03, 0.05), (0.07, 0.12), (0.1, 0.16), (0.12, 0.2), (0.12, 0.26), (0.0, 0.26)], 'granito'))
    out.append(cube(f'plinto_{i}_{s}', x - 0.82, x + 0.82, z - s * 0.82, back, h0, h0 + 0.16, 'granito'))
    base = [(0.82, 0.0), (0.84, 0.03), (0.85, 0.08), (0.83, 0.13), (0.78, 0.16), (0.74, 0.17), (0.71, 0.2), (0.7, 0.25),
            (0.72, 0.28), (0.75, 0.3), (0.76, 0.33), (0.74, 0.36), (0.7, 0.38), (0.68, 0.4)]
    out.append(lathe(f'basa_{i}_{s}', base, (x, h0 + 0.16, z), 'granito', seg=48, a0=a0, a1=a1))
    out.append(fluted_shaft(f'fuste_{i}_{s}', x, z, h0 + 0.56, COL['cap'] - 0.12, a0, a1))
    yc = COL['cap'] - 0.12
    out.append(lathe(f'astragalo_{i}_{s}', [(0.62, 0.0), (0.66, 0.025), (0.668, 0.05), (0.66, 0.075), (0.62, 0.1)], (x, yc, z), 'granito', seg=48, a0=a0, a1=a1))
    out.append(echinus(f'equino_{i}_{s}', x, yc + 0.1, z, a0, a1))
    out += volutes(f'voluta_{i}_{s}', x, yc + 0.1, z, s)
    out.append(cube(f'abaco_{i}_{s}', x - 0.92, x + 0.92, z - s * 0.95, back, yc + 0.42, yc + 0.54, 'granito'))
    out.append(block_moulding(f'imposta_{i}_{s}', x, z, 1.1, s * HW - s * 1.0, back, yc + 0.54, impost_profile(S - 0.2 - (yc + 0.54)), 'granito'))
    return out

def fluted_shaft(name, x, z, ya, yb, a0, a1, per_flute=6, rings=18):
    """the fluted shaft ('fuste'): its light is baked on a smooth cylinder (its own unwrap round it, its normals the
    cylinder's: a lightmap cannot draw 17 cm flutes), the flutes' own shading the game's (hiperinterior.js)"""
    m = Mesh(name, 'fuste')
    n = int(FLUTES * (a1 - a0) / (2 * math.pi) * per_flute)
    rows, uvs, lms = [], [], []
    for j in range(rings + 1):
        t = j / rings
        y = ya + (yb - ya) * t
        R = COL['r0'] if t < 1 / 3 else COL['r0'] + (COL['r1'] - COL['r0']) * ((t - 1 / 3) / (2 / 3)) ** 1.2
        row, uvr = [], []
        for i in range(n + 1):
            a = a0 + (a1 - a0) * i / n
            r = R * flute(a)
            row.append(m.vert((x + r * math.cos(a), y, z + r * math.sin(a)))); uvr.append(((a - a0) * COL['r0'], y))
        rows.append(row); uvs.append(uvr); lms.append([((a0 + (a1 - a0) * i / n - a0) * COL['r0'], y) for i in range(n + 1)])
    m.grid(rows, uvs, lmrows=lms)
    c = Vector((x, 0, z))
    return facing(m.build(), lambda p: Vector((p.x - c.x, 0, p.z - c.z)))

def echinus(name, x, y, z, a0, a1):
    """the ovolo under the volutes, carved with egg-and-dart (the eggs as bulges round it)"""
    m = Mesh(name, 'granito')
    n, rows, uvs = 144, [], []
    prof = [(0.62, 0.0), (0.7, 0.05), (0.76, 0.12), (0.79, 0.2), (0.78, 0.27), (0.74, 0.32)]
    eggs = 16
    for k, (r, h) in enumerate(prof):
        row, uvr = [], []
        bell = math.sin(math.pi * k / (len(prof) - 1))
        for i in range(n + 1):
            a = a0 + (a1 - a0) * i / n
            e = (a * eggs / (2 * math.pi)) % 1.0
            bulge = 0.035 * math.sin(math.pi * e / 0.8) * bell if e < 0.8 else -0.012 * bell
            row.append(m.vert((x + (r + bulge) * math.cos(a), y + h, z + (r + bulge) * math.sin(a)))); uvr.append(((a - a0) * 0.75, h))
        rows.append(row); uvs.append(uvr)
    m.grid(rows, uvs)
    return facing(m.build(), lambda p: Vector((p.x - x, 0, p.z - z)))

def volutes(name, x, y, z, s):
    """the Ionic capital's two volutes on its face to the nave: at each end a scroll, a rounded ribbon winding three turns
    from its rim to its eye on a backing disc, the cushion (pulvinus) running back into the pier; between them the
    channel (canalis) over the echinus"""
    out = []
    nz = -s
    zf = z + nz * 0.78
    for sx in (-1, 1):
        cx, cy, R = x + sx * 0.62, y + 0.12, 0.26
        prof = [(0.0, 0.0), (R, 0.0), (R * 0.95, -0.3 * nz), (R * 0.88, -0.75 * nz), (R * 0.85, -1.1 * nz), (0.0, -1.1 * nz)]
        out.append(lathe(f'{name}_almohadilla_{sx}', prof, (cx, cy, zf), 'granito', seg=32, axis='z'))
        turns, nseg = 3.0, 110
        path, n1, n2 = [], [], []
        for k in range(nseg + 1):
            t = k / nseg
            ang = -sx * 2 * math.pi * turns * t + math.pi / 2
            rr = R * 0.95 * (1 - t) ** 1.15 + 0.045 * t
            path.append(Vector((cx + rr * math.cos(ang), cy + rr * math.sin(ang), zf + nz * 0.004)))
            n1.append(Vector((math.cos(ang), math.sin(ang), 0)))
            n2.append(Vector((0, 0, nz)))
        out.append(sweep(f'{name}_espiral_{sx}', path, n1, n2, [(-0.02, 0.0), (-0.016, 0.022), (0.0, 0.032), (0.016, 0.022), (0.02, 0.0)], 'granito'))
        out.append(lathe(f'{name}_ojo_{sx}', [(0.0, 0.05 * nz), (0.035, 0.04 * nz), (0.05, 0.0), (0.0, 0.0)], (cx, cy, zf), 'granito', seg=16, axis='z'))
    out.append(plate(f'{name}_canal', [(-0.62, -0.02), (0.62, -0.02), (0.62, 0.14), (-0.62, 0.14)], (x, y + 0.24, zf), (1, 0, 0), (0, 1, 0), (0, 0, -nz), -0.02, 0.9, 'granito'))
    return out

def impost_profile(h):
    """(out, up) round the impost: two fasciae, a frieze, a cornice with its corona and cyma, h tall — closed back to
    the wall"""
    k = h / 0.66
    return [(0.0, 0.0), (0.0, 0.12 * k), (0.03, 0.13 * k), (0.03, 0.24 * k), (0.06, 0.26 * k), (0.06, 0.28 * k),
            (0.03, 0.3 * k), (0.03, 0.44 * k), (0.07, 0.47 * k), (0.11, 0.5 * k), (0.15, 0.52 * k), (0.15, 0.58 * k),
            (0.19, 0.6 * k), (0.22, 0.63 * k), (0.22, 0.66 * k), (-0.05, 0.66 * k), (-0.05, 0.0)]

def wall_band(name, ax, az, bx, bz, nx, nz, y0, profile, role):
    """a moulding run straight along a wall (from a to b) whose face looks along (nx, nz): profile (out, up), closed"""
    n1 = Vector((nx, 0, nz)); n2 = Vector((0, 1, 0))
    return sweep(name, [(ax, y0, az), (bx, y0, bz)], [n1, n1], [n2, n2], profile, role)

def impost_band():
    """the impost's profile along the nave's walls between the columns' blocks, at the springing (it ties the bays
    under the lunettes), and along the choir bay's"""
    out = []
    y0 = COL['cap'] + 0.42
    prof = impost_profile(S - 0.2 - y0)
    for s in (-1, 1):
        for bi, (xa, xb, xm) in enumerate(BAYS):
            out.append(wall_band(f'imposta_muro_{bi}_{s}', xa + 1.1, s * HW, xb - 1.1, s * HW, 0, -s, y0, prof, 'granito'))
        out.append(wall_band(f'imposta_coro_{s}', X0, s * HW, XC - 1.1, s * HW, 0, -s, y0, prof, 'granito'))
    out.append(wall_band('imposta_oeste', X0, -HW, X0, HW, 1, 0, y0, prof, 'granito'))
    return out

# ---------------------------------------------------------------- arches and vaults
ARCH_PROF = [(-0.5, 0.75), (-0.5, 0.18), (-0.44, 0.12), (-0.4, 0.1), (-0.4, 0.04), (-0.36, 0.0), (0.36, 0.0), (0.4, 0.04),
             (0.4, 0.1), (0.44, 0.12), (0.5, 0.18), (0.5, 0.75)]   # (from its extrados, over the webs: the light's seam there)
def transverse_arch(i):
    """a semicircular granite arch from column to column across the nave (its soffit at radius 7,75 from the imposts'
    top), a metre wide, stepped at its edges; its voussoirs: the drum texture's joints, run along it"""
    x = PIERS[i]
    R, yc = HW - 0.25, S - 0.2
    path, n1, n2 = [], [], []
    for k in range(97):
        a = math.pi * k / 96
        rad = Vector((0, math.sin(a), -math.cos(a)))
        path.append(Vector((x, yc, 0)) + rad * R); n1.append(Vector((1, 0, 0))); n2.append(rad)
    return [sweep(f'fajon_{i}', path, n1, n2, ARCH_PROF, 'tambor')]

RIB = [(-0.13, 0.0), (-0.13, -0.05), (-0.09, -0.1), (-0.075, -0.18), (-0.05, -0.24), (-0.025, -0.27), (0.0, -0.28),
       (0.025, -0.27), (0.05, -0.24), (0.075, -0.18), (0.09, -0.1), (0.13, -0.05), (0.13, 0.0), (0.13, 0.12), (-0.13, 0.12)]
def rib_path(name, pts3, ups, r=0.15, role='tambor'):
    """a moulded rib (a roll between two hollows) along a path hung from a surface whose up (into the stone) is given"""
    k = r / 0.15
    prof = [(a * k, b * k) for a, b in RIB]
    path = [Vector(p) for p in pts3]
    n1, n2 = [], []
    for i, p in enumerate(path):
        t = (path[min(i + 1, len(path) - 1)] - path[max(i - 1, 0)]).normalized()
        up = Vector(ups[i])
        side = t.cross(up).normalized()
        n1.append(side); n2.append(side.cross(t).normalized())
    return sweep(name, path, n1, n2, prof, role)

def rib(name, a, b, xa, xb, r=0.15, lun=LUNETTE, dome=0.5, n=28):
    pts, ups = [], []
    for k in range(n + 1):
        t = k / n
        x, z = a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t
        pts.append((x, vault_y(x, z, xa, xb, dome=dome, lun=lun) + 0.015, z)); ups.append(vault_up(x, z, xa, xb, dome=dome, lun=lun))
    return rib_path(name, pts, ups, r)

def boss(name, x, y, z, r, role='oro'):
    """a boss: a carved rosette — eight petals round a button, on a ring"""
    out = [lathe(f'{name}_aro', [(0.0, 0.03), (r, 0.03), (r, -0.06), (r * 0.9, -0.12), (0.0, -0.12)], (x, y, z), role, seg=32)]
    m = Mesh(f'{name}_petalos', role)
    petals, n, rings = 8, 64, 4
    rows = []
    for j in range(rings + 1):
        t = j / rings
        row = []
        for i in range(n + 1):
            a = 2 * math.pi * i / n
            lobe = math.sin(math.pi * ((a * petals / (2 * math.pi)) % 1.0)) ** 0.6
            rr = r * 0.88 * (1 - t) * (0.55 + 0.45 * lobe) + 0.001
            row.append(m.vert((x + rr * math.cos(a), y - 0.12 - 0.13 * r / 0.5 * math.sin(math.pi * t * 0.9) * (0.6 + 0.4 * lobe), z + rr * math.sin(a))))
        rows.append(row)
    m.grid(rows)
    out.append(facing(m.build(), DOWN))
    out.append(lathe(f'{name}_boton', [(0.0, -0.36 * r / 0.5 - 0.1), (r * 0.18, -0.34 * r / 0.5 - 0.1), (r * 0.25, -0.27 * r / 0.5 - 0.1), (r * 0.2, -0.1), (0.0, -0.1)], (x, y, z), role, seg=20))
    return out

def web(name, xa, xb, dome, lun, nx=56, nz=48, ext=0.18):
    """a bay's web, its grid crowded against the walls and the arches where it rises steeply; it runs on a little into
    the walls and under the arches (`ext`), so no crack shows where they meet (the reviewer's specks of sky)"""
    L = xb - xa
    def f(u, v):
        x = xa - ext + (L + 2 * ext) * dense(u); z = -(HW + ext) + 2 * (HW + ext) * dense(v)
        return (x, vault_y(x, z, xa, xb, dome=dome, lun=lun) + 0.03, z)
    return surface(name, f, nx, nz, 'cal', DOWN)

def nave_vault(bi):
    xa, xb, xm = BAYS[bi]
    out = [web(f'plemento_{bi}', xa, xb, 0.5, LUNETTE)]
    L = xb - xa
    K, Kn, Ks, Kw, Ke = (xm, 0), (xm, -HW * 0.5), (xm, HW * 0.5), (xa + L * 0.25, 0), (xb - L * 0.25, 0)
    C = [(xa, -HW), (xa, HW), (xb, -HW), (xb, HW)]
    R = lambda nm, a, b, rr=0.15: out.append(rib(f'nervio_{bi}_{nm}', a, b, xa, xb, r=rr))
    for k, c in enumerate(C): R(f'diag{k}', c, K, 0.17)
    R('t0', C[0], Kn); R('t1', C[0], Kw); R('t2', C[1], Ks); R('t3', C[1], Kw)
    R('t4', C[2], Kn); R('t5', C[2], Ke); R('t6', C[3], Ks); R('t7', C[3], Ke)
    R('l0', Kw, K, 0.12); R('l1', K, Ke, 0.12); R('l2', Kn, K, 0.12); R('l3', K, Ks, 0.12)
    R('l4', (xa + 0.7, 0), Kw, 0.12); R('l5', Ke, (xb - 0.7, 0), 0.12); R('l6', (xm, -HW + 0.25), Kn, 0.12); R('l7', Ks, (xm, HW - 0.25), 0.12)
    if bi == NB - 1:
        # the presbytery's bay (the photo): a star of curved liernes ('combados') in rhombi — a curved rhombus through the
        # tiercerons' ends, bulging out, and a curved square through the diagonals, bulging in — with a boss where they
        # meet the ribs and at the middle of each curve
        def combado(name, p0, p1, bulge, r=0.11):
            mx, mz = (p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2
            dx, dz = mx - xm, mz; dl = math.hypot(dx, dz) or 1
            px, pz = mx + dx / dl * bulge, mz + dz / dl * bulge
            cx_, cz_ = 2 * px - mx, 2 * pz - mz   # (the control point of a quadratic curve through the bulged middle)
            pts, ups = [], []
            for k in range(33):
                t = k / 32
                x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * cx_ + t * t * p1[0]
                z = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * cz_ + t * t * p1[1]
                pts.append((x, vault_y(x, z, xa, xb) + 0.015, z)); ups.append(vault_up(x, z, xa, xb))
            out.append(rib_path(name, pts, ups, r))
            return (px, pz)
        D = [(c[0] + (xm - c[0]) * 0.62, c[1] * 0.38) for c in C]   # (on the diagonals, 62 % of the way to the crown)
        mids = [combado(f'nervio_{bi}_combado_{k}', p0, p1, 0.9) for k, (p0, p1) in enumerate(((Kw, Kn), (Kn, Ke), (Ke, Ks), (Ks, Kw)))]
        mids += [combado(f'nervio_{bi}_combado_i{k}', p0, p1, -0.5, 0.1) for k, (p0, p1) in enumerate(((D[0], D[2]), (D[2], D[3]), (D[3], D[1]), (D[1], D[0])))]
        for k, q in enumerate(D + mids[:4]):
            out += boss(f'clave_{bi}_estrella_{k}', q[0], vault_y(q[0], q[1], xa, xb) - 0.2, q[1], 0.2 if k < 4 else 0.17)
    # the wall ribs over the lunettes, framing the windows
    for s in (-1, 1):
        pts, ups = [], []
        for k in range(49):
            x = xa + PW / 2 + (BAY - PW) * k / 48
            zz = s * (HW - 0.14)
            y = vault_y(x, zz, xa, xb)
            pts.append((x, y + 0.02, zz))
            d = Vector((x - xm, (y - S) * 0.65, 0)).normalized()
            ups.append(d)
        out.append(rib_path(f'formero_{bi}_{s}', pts, ups, 0.12))
    for q, rr in ((K, 0.5), (Kn, 0.3), (Ks, 0.3), (Kw, 0.3), (Ke, 0.3)):
        out += boss(f'clave_{bi}_{q[0]:.1f}_{q[1]:.1f}', q[0], vault_y(q[0], q[1], xa, xb) - 0.2, q[1], rr)
    return out

def choir_bay_vault():
    xa, xb = X0, XC
    xm, L = (xa + xb) / 2, xb - xa
    out = [web('plemento_coro', xa, xb, 0.4, 5.0, 40, 48)]
    K = (xm, 0)
    for k, c in enumerate([(xa, -HW), (xa, HW), (xb, -HW), (xb, HW)]):
        out.append(rib(f'nervio_coro_d{k}', c, K, xa, xb, r=0.16, lun=5.0, dome=0.4))
    out.append(rib('nervio_coro_l0', (xa + 0.3, 0), K, xa, xb, r=0.11, lun=5.0, dome=0.4))
    out.append(rib('nervio_coro_l1', K, (xb - 0.7, 0), xa, xb, r=0.11, lun=5.0, dome=0.4))
    out += boss('clave_coro', xm, vault_y(xm, 0, xa, xb, dome=0.4, lun=5.0) - 0.2, 0, 0.45)
    return out

def rosette(name, c, n, r, role='granito'):
    """a little carved flower facing n: eight petals round a button"""
    n = Vector(n).normalized()
    t = n.cross(Vector((0, 1, 0)))
    if t.length < 1e-3: t = n.cross(Vector((1, 0, 0)))
    t.normalize(); b = n.cross(t).normalized()
    m = Mesh(name, role)
    petals, seg, rings = 8, 32, 3
    rows = []
    for j in range(rings + 1):
        tt = j / rings
        row = []
        for i in range(seg + 1):
            a = 2 * math.pi * i / seg
            lobe = math.sin(math.pi * ((a * petals / (2 * math.pi)) % 1.0)) ** 0.7
            rr = r * (1 - tt) * (0.5 + 0.5 * lobe) + 0.0005
            hh = r * 0.5 * math.sin(math.pi * tt * 0.85) * (0.5 + 0.5 * lobe)
            row.append(m.vert(c + t * rr * math.cos(a) + b * rr * math.sin(a) + n * hh))
        rows.append(row)
    m.grid(rows)
    return [facing(m.build(), lambda p: n)]

def apse_dome():
    """the half dome over the apse (a quarter sphere from the springing), coffered: 12 columns × 5 rows of sunk panels,
    smaller towards the top, framed in two steps, a rosette in each; a plain cap over them; a cornice round its foot"""
    out = []
    R0, yd = AR - 0.02, S + 0.25
    cols, rows = 12, 5
    w = [1.0, 0.9, 0.8, 0.7, 0.6]
    els = [0.0]
    for k in range(rows): els.append(els[-1] + (math.pi / 2) * 0.86 * w[k] / sum(w))
    centre = Vector((XA, yd, 0))
    def P_(az, el, r): return Vector((XA + r * math.cos(el) * math.cos(az), yd + r * math.sin(el), r * math.cos(el) * math.sin(az)))
    def sinus(az, el): return (az * R0 * math.cos(el), el * R0)   # (the light's atlas: an equal-area unwrap, one island)
    frame = 0.11
    m_f = Mesh('casetones', 'caseton'); m_p = Mesh('casetones_fondo', 'caseton_fondo')
    for j in range(rows):
        for i in range(cols):
            az0, az1 = -math.pi / 2 + math.pi * i / cols, -math.pi / 2 + math.pi * (i + 1) / cols
            el0, el1 = els[j], els[j + 1]
            steps = [(0.0, 0.0), (frame * 0.5, 0.0), (frame * 0.5, 0.07), (frame, 0.07), (frame, 0.16)]
            loops = []
            ne = 6
            loops, lmloops, uvloops = [], [], []
            AO = {(0.0, 0.0): 1.0, (frame * 0.5, 0.0): 1.0, (frame * 0.5, 0.07): 1.0, (frame, 0.07): 1.0, (frame, 0.16): 1.0}  # (the bake has their recesses)
            for inset, depth in steps:
                ia = inset / (R0 * max(0.2, math.cos((el0 + el1) / 2))); ie = inset / R0
                a_lo, a_hi, e_lo, e_hi = az0 + ia, az1 - ia, el0 + ie, el1 - ie
                pts = [(a_lo + (a_hi - a_lo) * k / ne, e_lo) for k in range(ne)] + [(a_hi, e_lo + (e_hi - e_lo) * k / ne) for k in range(ne)] + \
                      [(a_hi - (a_hi - a_lo) * k / ne, e_hi) for k in range(ne)] + [(a_lo, e_hi - (e_hi - e_lo) * k / ne) for k in range(ne)]
                loops.append([m_f.vert(P_(a, e, R0 + depth), AO[(inset, depth)]) for a, e in pts]); lmloops.append([sinus(a, e) for a, e in pts])
                uvloops.append([(u, v + depth) for u, v in lmloops[-1]])
            for (a, b), (la, lb), (ua, ub) in zip(zip(loops, loops[1:]), zip(lmloops, lmloops[1:]), zip(uvloops, uvloops[1:])):
                nn = len(a)
                for k in range(nn): m_f.face([a[k], a[(k + 1) % nn], b[(k + 1) % nn], b[k]], uvs=[ua[k], ua[(k + 1) % nn], ub[(k + 1) % nn], ub[k]], lm=[la[k], la[(k + 1) % nn], lb[(k + 1) % nn], lb[k]])
            # (the panel: a greyer lime, the photo's darker centres — a piece of its own)
            cen = m_p.vert(P_((az0 + az1) / 2, (el0 + el1) / 2, R0 + 0.16)); lc = sinus((az0 + az1) / 2, (el0 + el1) / 2)
            last = [m_p.vert(m_f.v[q]) for q in loops[-1]]; ll = lmloops[-1]; ul = uvloops[-1]; uc = (lc[0], lc[1] + 0.16)
            for k in range(len(last)): m_p.face([last[k], last[(k + 1) % len(last)], cen], uvs=[ul[k], ul[(k + 1) % len(last)], uc], lm=[ll[k], ll[(k + 1) % len(last)], lc])
            cp = P_((az0 + az1) / 2, (el0 + el1) / 2, R0 + 0.15)
            out += rosette(f'roseta_{i}_{j}', cp, (centre - cp).normalized(), 0.09 + 0.06 * (rows - j) / rows)
    out.append(facing(m_f.build(), lambda p: centre - p)); out.append(facing(m_p.build(), lambda p: centre - p))
    top = els[-1]
    m_t = Mesh('cupula_tapa', 'granito'); rows, lms = [], []
    for j in range(9):
        row, lr = [], []
        for i in range(33):
            az, el = -math.pi / 2 + math.pi * i / 32, top + (math.pi / 2 - top) * j / 8
            row.append(m_t.vert(P_(az, el, R0))); lr.append(sinus(az, el))
        rows.append(row); lms.append(lr)
    m_t.grid(rows, lmrows=lms)
    out.append(facing(m_t.build(), lambda p: centre - p))
    # its rims: a band under its foot, into the wall and the cornice, and one at each side, into the triumphal arch (no
    # crack between them: the sun's dotted lines, the specks of sky)
    out.append(surface('cupula_pie', lambda u, v: P_(-math.pi / 2 - 0.06 + (math.pi + 0.12) * u, -0.06 + 0.06 * v, R0), 64, 2, 'caseton', lambda p: centre - p))
    for sgn in (-1, 1):
        out.append(surface(f'cupula_lado_{sgn}', lambda u, v, sgn=sgn: P_(sgn * (math.pi / 2 + 0.06 * u), (math.pi / 2) * v, R0), 2, 24, 'caseton', lambda p: centre - p))
    # (the crown: a small round boss, as the photo shows something hanging there)
    out += boss('clave_cupula', XA + 0.02, yd + R0 - 0.02, 0.0, 0.35)
    # the cornice at its foot, on the apse wall
    path, n1, n2 = [], [], []
    for k in range(97):
        a = -math.pi / 2 + math.pi * k / 96
        path.append(Vector((XA + AR * math.cos(a), S - 0.45, AR * math.sin(a))))
        n1.append(Vector((-math.cos(a), 0, -math.sin(a)))); n2.append(Vector((0, 1, 0)))
    prof = [(-0.05, 0.0), (0.05, 0.02), (0.06, 0.15), (0.1, 0.18), (0.12, 0.25), (0.12, 0.33), (0.2, 0.37), (0.26, 0.43), (0.28, 0.55), (-0.05, 0.55)]
    out.append(sweep('cornisa_abside', path, n1, n2, prof, 'granito'))
    return out

def triumphal_arch():
    """the arch into the apse (the photo: broad, its soffit coffered): the last piers' arch, its soffit as deep as the
    pier (2,4 m) in square sunk panels, 3 across × 16 round, a moulded archivolt on each face"""
    x = PIERS[-1]
    R, yc = HW - 0.25, S - 0.2
    out = []
    n_r, n_a = 16, 3
    m_f = Mesh('triunfal', 'caseton'); m_p = Mesh('triunfal_fondo', 'caseton_fondo')
    def P_(a, xx, d): return Vector((xx, yc + (R + d) * math.sin(a), -(R + d) * math.cos(a)))
    for i in range(n_r):
        for j in range(n_a):
            a0, a1 = math.pi * i / n_r, math.pi * (i + 1) / n_r
            x0, x1 = x - PW / 2 + PW * j / n_a, x - PW / 2 + PW * (j + 1) / n_a
            loops, lmloops, uvloops = [], [], []
            for inset, depth, ao in ((0.0, 0.0, 1.0), (0.06, 0.0, 1.0), (0.06, 0.06, 1.0), (0.11, 0.06, 1.0), (0.11, 0.13, 1.0)):
                ia = inset / R
                pts = ((a0 + ia, x0 + inset), (a0 + ia, x1 - inset), (a1 - ia, x1 - inset), (a1 - ia, x0 + inset))
                loops.append([m_f.vert(P_(a, xx, depth), ao) for a, xx in pts]); lmloops.append([(a * R, xx) for a, xx in pts])
                uvloops.append([(a * R, xx + depth) for a, xx in pts])
            for (a, b), (la, lb), (ua, ub) in zip(zip(loops, loops[1:]), zip(lmloops, lmloops[1:]), zip(uvloops, uvloops[1:])):
                for k in range(4): m_f.face([a[k], a[(k + 1) % 4], b[(k + 1) % 4], b[k]], uvs=[ua[k], ua[(k + 1) % 4], ub[(k + 1) % 4], ub[k]], lm=[la[k], la[(k + 1) % 4], lb[(k + 1) % 4], lb[k]])
            m_p.face([m_p.vert(m_f.v[q]) for q in loops[-1]], uvs=uvloops[-1], lm=lmloops[-1])
            cp = P_((a0 + a1) / 2, (x0 + x1) / 2, 0.12)
            out += rosette(f'roseta_arco_{i}_{j}', cp, (Vector((cp.x, yc, 0)) - cp).normalized(), 0.1)
    out.append(facing(m_f.build(), lambda p: Vector((0, yc - p.y, -p.z)))); out.append(facing(m_p.build(), lambda p: Vector((0, yc - p.y, -p.z))))
    # the arch's body behind its coffers, up to the webs and the dome (it closes the gap between them)
    path, n1, n2 = [], [], []
    for k in range(97):
        a = math.pi * k / 96
        rad = Vector((0, math.sin(a), -math.cos(a)))
        path.append(Vector((x, yc, 0)) + rad * R); n1.append(Vector((1, 0, 0))); n2.append(rad)
    out.append(sweep('triunfal_cuerpo', path, n1, n2, [(-PW / 2, 0.14), (PW / 2, 0.14), (PW / 2, 1.3), (-PW / 2, 1.3)], 'granito'))
    for sx in (-1, 1):
        path, n1, n2 = [], [], []
        for k in range(97):
            a = math.pi * k / 96
            rad = Vector((0, math.sin(a), -math.cos(a)))
            path.append(Vector((x + sx * PW / 2, yc, 0)) + rad * R); n1.append(rad); n2.append(Vector((sx, 0, 0)))
        prof = [(0.0, -0.05), (0.0, 0.06), (0.05, 0.08), (0.08, 0.14), (0.08, 0.3), (0.12, 0.34), (0.16, 0.42), (0.16, 0.5), (0.3, 0.5), (0.3, -0.05)]
        out.append(sweep(f'arquivolta_triunfal_{sx}', path, n1, n2, prof, 'granito'))
    return out

def chapel_arches():
    """the pointed arches into the chapels: a granite lining over their soffit (through the wall), a moulded archivolt on
    the nave's face, the jambs as granite pilasters with an impost at the springing"""
    out = []
    for bi, (xa, xb, xm) in enumerate(BAYS):
        x0, x1 = xa + PW / 2, xb - PW / 2
        w = x1 - x0 - 0.2
        for s in (-1, 1):
            zf = s * HW
            arch, _ = pointed_outline(w, 6.6, 3.3, 16)
            # the archivolt: on the nave's face (the wall's plane, u along x), standing out towards the nave (−s)
            out.append(edge_moulding(f'arquivolta_{bi}_{s}', arch, (xm, 0, zf), (1, 0, 0), (0, 1, 0), (0, 0, -s),
                                     [(0.0, -0.02), (0.0, 0.06), (0.04, 0.08), (0.07, 0.13), (0.11, 0.15), (0.15, 0.2), (0.19, 0.22), (0.23, 0.22), (0.23, -0.02)], 'granito'))
            # the soffit's lining, the wall's depth through
            path = [Vector((xm + u, y, zf)) for u, y in arch]
            nrm = outline_normals(arch)
            n1 = [Vector((a, b, 0)) for a, b in nrm]
            out.append(sweep(f'intrados_{bi}_{s}', path, n1, [Vector((0, 0, s))] * len(path), [(-0.04, 0.0), (-0.04, THN), (0.02, THN), (0.02, 0.0)], 'tambor'))
            for sx in (-1, 1):
                jx = xm + sx * (w / 2 + 0.15)
                out.append(cube(f'jamba_{bi}_{s}_{sx}', jx - 0.18, jx + 0.18, zf - s * 0.04, zf + s * THN, 0.95, 6.4, 'sillar'))
                out.append(cube(f'imposta_jamba_{bi}_{s}_{sx}', jx - 0.26, jx + 0.26, zf - s * 0.1, zf + s * (THN + 0.05), 6.4, 6.62, 'granito'))
    return out

def choir():
    """the raised choir at the foot: the under-choir's star vault of fine ribs, the choir's floor and its front — a low
    arch across the nave, the parapet, a granite balustrade"""
    out = []
    y0, rise = 4.5, 1.25
    def sv(x, z): return y0 + rise * math.sqrt(max(0.0, 1 - (z / HW) ** 2)) * (0.75 + 0.25 * math.sin(math.pi * max(0.0, min(1.0, (x - X0) / (XC - X0)))))
    def svu(x, z):
        e = 0.01
        return Vector((-(sv(x + e, z) - sv(x - e, z)) / (2 * e), 1.0, -(sv(x, z + e) - sv(x, z - e)) / (2 * e))).normalized()
    L = XC - X0
    out.append(surface('sotocoro', lambda u, v: (X0 + L * u, sv(X0 + L * u, -HW + 2 * HW * dense(v)) + 0.02, -HW + 2 * HW * dense(v)), 36, 48, 'cal', DOWN))
    cx, rxs = (X0 + XC) / 2, L / 2
    def ribp(name, pts2, r=0.09):
        out.append(rib_path(name, [(x, sv(x, z), z) for x, z in pts2], [svu(x, z) for x, z in pts2], r, 'granito'))
    ribp('sotocoro_anillo', [(cx + math.cos(2 * math.pi * k / 96) * rxs * 0.55, math.sin(2 * math.pi * k / 96) * HW * 0.55) for k in range(97)])
    star = [(cx + math.cos(2 * math.pi * k / 8) * rxs * 0.55, math.sin(2 * math.pi * k / 8) * HW * 0.55) for k in range(8)]
    corners = [(X0, -HW), (X0, HW), (XC, -HW), (XC, HW), (cx, -HW), (cx, HW), (X0, 0), (XC, 0)]
    for k, c in enumerate(corners):
        best = min(star, key=lambda q: math.hypot(q[0] - c[0], (q[1] - c[1]) * 0.6))
        ribp(f'sotocoro_n{k}', [(c[0] + (best[0] - c[0]) * t / 16, c[1] + (best[1] - c[1]) * t / 16) for t in range(17)])
    for k, q in enumerate(star):
        ribp(f'sotocoro_r{k}', [(q[0] + (cx - q[0]) * t / 16, q[1] * (1 - t / 16)) for t in range(17)], 0.07)
        out += boss(f'clave_sotocoro_{k}', q[0], sv(q[0], q[1]) - 0.1, q[1], 0.14)
    out += boss('clave_sotocoro', cx, sv(cx, 0) - 0.1, 0, 0.26)
    # the fill over the under-choir's vault up to the choir's floor
    out.append(cube('coro_suelo', X0, XC, -HW, HW, CHY - 0.25, CHY, 'suelo'))
    # the choir's front: the low arch's band across the nave along the vault's edge, the parapet up to the floor
    zs = [-HW + 2 * HW * k / 96 for k in range(97)]
    path = [Vector((XC, sv(XC, z), z)) for z in zs]
    out.append(sweep('coro_arco', path, [Vector((0, -1, 0))] * len(path), [Vector((1, 0, 0))] * len(path),
                     [(-0.02, -0.05), (0.35, -0.05), (0.4, 0.04), (0.4, 0.1), (0.35, 0.14), (-0.02, 0.14)], 'granito'))
    m = Mesh('coro_antepecho', 'cal')
    rows = [[m.vert((XC + 0.02, sv(XC, z), z)) for z in zs], [m.vert((XC + 0.02, CHY - 0.25, z)) for z in zs]]
    m.grid(rows)
    out.append(facing(m.build(), lambda p: (1, 0, 0)))
    out.append(cube('coro_cornisa', XC - 0.1, XC + 0.14, -HW, HW, CHY - 0.27, CHY + 0.04, 'granito'))
    out.append(cube('balaustrada_zocalo', XC - 0.2, XC + 0.06, -HW, HW, CHY, CHY + 0.18, 'granito'))
    out.append(cube('balaustrada_pasamanos', XC - 0.24, XC + 0.09, -HW, HW, CHY + 0.86, CHY + 1.0, 'granito'))
    bal = [(0.0, 0.0), (0.07, 0.0), (0.085, 0.03), (0.085, 0.06), (0.06, 0.1), (0.065, 0.16), (0.1, 0.3), (0.11, 0.38), (0.09, 0.48), (0.055, 0.56), (0.05, 0.6), (0.065, 0.63), (0.07, 0.68), (0.0, 0.68)]
    zz, k = -HW + 0.3, 0
    while zz <= HW - 0.3:
        out.append(lathe(f'balaustre_{k}', bal, (XC - 0.08, CHY + 0.18, zz), 'granito', seg=12))
        zz += 0.34; k += 1
    return out

def windows_and_glass():
    """the glass of the windows, set in their splays (at 70 % of the wall's depth), and the oculus's, with the
    oculus's mouldings round it on the inside"""
    out = []
    outer = arch_outline(WIN['light'], WIN['ly1'] - WIN['light'] / 2, bottom=WIN['ly0'])
    for s in (-1, 1):
        for bi, (xa, xb, xm) in enumerate(BAYS):
            out.append(plate(f'vidrio_{bi}_{s}', outer, (xm, 0, s * (HW + THN * 0.7 + 0.03)), (1, 0, 0), (0, 1, 0), (0, 0, s), -0.01, 0.01, 'vidrio'))
    outer_a = arch_outline(APSE_WIN['w'], APSE_WIN['y1'] - APSE_WIN['w'] / 2, bottom=APSE_WIN['y0'], seg=20)
    for sgn in (-1, 1):
        a = sgn * APSE_WIN['a']
        cx, cz = XA + (AR + 1.03) * math.cos(a), (AR + 1.03) * math.sin(a)
        out.append(plate(f'vidrio_abside_{sgn}', outer_a, (cx, 0, cz), (-math.sin(a), 0, math.cos(a)), (0, 1, 0), (math.cos(a), 0, math.sin(a)), -0.01, 0.01, 'vidrio'))
    out.append(plate('vidrio_oculo', circle(OCULUS['r'], 48, 0, OCULUS['y']), (X0 - 0.63, 0, 0), (0, 0, -1), (0, 1, 0), (-1, 0, 0), -0.01, 0.01, 'vidrio'))
    for k, (r, d) in enumerate(((OCULUS['splay'] + 0.06, 0.08), (OCULUS['splay'] + 0.22, 0.15), (OCULUS['splay'] + 0.36, 0.06))):
        out.append(lathe(f'oculo_anillo_{k}', [(r - 0.08, -0.02), (r - 0.04, d), (r + 0.04, d), (r + 0.08, -0.02)], (X0, OCULUS['y'], 0), 'granito', seg=72, axis='x'))
    return out

def plinth():
    """the granite plinth along the walls: 0,95 m of ashlar a few centimetres out, a rounded moulding on top"""
    out = []
    def run(name, ax, az, bx, bz, nx, nz, y0=0.0, h=0.95):
        if math.hypot(bx - ax, bz - az) < 0.15: return
        prof = [(-0.05, 0.0), (0.05, 0.0), (0.05, h - 0.06), (0.07, h - 0.04), (0.075, h - 0.02), (0.06, h), (-0.05, h)]
        out.append(wall_band(name, ax, az, bx, bz, nx, nz, y0, prof, 'sillar'))
    D = DOORS['oeste']
    run('zocalo_oeste_n', X0, -HW, X0, -D['w'] / 2 - 0.25, 1, 0); run('zocalo_oeste_s', X0, D['w'] / 2 + 0.25, X0, HW, 1, 0)
    a, b, _ = STAIR_DOOR
    run('zocalo_coro_n', X0, -HW, XC - PW / 2 - 0.9, -HW, 0, 1)
    run('zocalo_coro_s1', X0, HW, a - 0.25, HW, 0, -1); run('zocalo_coro_s2', b + 0.25, HW, XC - PW / 2 - 0.9, HW, 0, -1)
    for bi, (xa, xb, xm) in enumerate(BAYS):
        x0, x1 = xa + PW / 2, xb - PW / 2
        for s in (-1, 1):
            zo = s * (HW + CD)
            if bi == DOOR_BAY:
                Dd = DOORS['sur' if s > 0 else 'norte']
                run(f'zocalo_cap_{bi}_{s}_a', x0, zo, xm - Dd['w'] / 2 - 0.25, zo, 0, -s); run(f'zocalo_cap_{bi}_{s}_b', xm + Dd['w'] / 2 + 0.25, zo, x1, zo, 0, -s)
            else: run(f'zocalo_cap_{bi}_{s}', x0, zo, x1, zo, 0, -s)
            run(f'zocalo_pil_{bi}_{s}_a', x0, s * (HW + THN), x0, zo, 1, 0)
            run(f'zocalo_pil_{bi}_{s}_b', x1, s * (HW + THN), x1, zo, -1, 0)
    n = 32
    for k in range(n):
        a0, a1 = -math.pi / 2 + math.pi * k / n, -math.pi / 2 + math.pi * (k + 1) / n
        am = (a0 + a1) / 2
        if abs(am - SACRISTY_A) < 0.11: continue
        run(f'zocalo_abside_{k}', XA + AR * math.cos(a0), AR * math.sin(a0), XA + AR * math.cos(a1), AR * math.sin(a1), -math.cos(am), -math.sin(am), y0=P, h=0.8)
    return out

def door_frames():
    """granite frames round the two small doors whose leaves church.js hangs flat on the wall: the tower stair's and the
    sacristy's (the Backrooms)"""
    out = []
    a, b, h = STAIR_DOOR
    w = b - a
    shape = [(-w / 2 - 0.22, 0.0), (-w / 2, 0.0), (-w / 2, h), (w / 2, h), (w / 2, 0.0), (w / 2 + 0.22, 0.0), (w / 2 + 0.22, h + 0.22), (-w / 2 - 0.22, h + 0.22)]
    out.append(plate('marco_escalera', shape, ((a + b) / 2, 0, HW), (1, 0, 0), (0, 1, 0), (0, 0, -1), -0.02, 0.06, 'sillar'))
    A = SACRISTY_A
    cx, cz = XA + AR * math.cos(A), AR * math.sin(A)
    w, h = 1.3, 2.4
    shape = [(-w / 2 - 0.22, 0.0), (-w / 2, 0.0), (-w / 2, h), (w / 2, h), (w / 2, 0.0), (w / 2 + 0.22, 0.0), (w / 2 + 0.22, h + 0.25), (-w / 2 - 0.22, h + 0.25)]
    out.append(plate('marco_sacristia', shape, (cx, P, cz), (-math.sin(A), 0, math.cos(A)), (0, 1, 0), (-math.cos(A), 0, -math.sin(A)), -0.02, 0.06, 'sillar'))
    return out

def build_architecture():
    obs = []
    for fn in (build_floors, build_walls, impost_band, triumphal_arch, choir_bay_vault, apse_dome, chapel_arches, choir, windows_and_glass, plinth, door_frames):
        t = len(obs); obs += fn(); print(f'  {fn.__name__}: {len(obs) - t} piezas', flush=True)
    for i in range(len(PIERS)):
        for s in (-1, 1): obs += column(i, s)
    for i in range(len(PIERS) - 1): obs += transverse_arch(i)
    for bi in range(NB): obs += nave_vault(bi)
    print(f'  columnas, arcos y bóvedas: {len(obs)} piezas en total', flush=True)
    return obs

# ================================================================ only in the bake: what closes the church and stands in it
def build_occluders():
    out = []
    out.append(cube('o_tejado', X0 - TH - 0.5, XA + AR + 2.0, -HW - CD - TH - 0.5, HW + CD + TH + 0.5, WALL_H, WALL_H + 0.5, 'oclusor'))
    for s in (-1, 1):
        out.append(cube(f'o_capillas_techo_{s}', XC - PW / 2 - 0.3, XA + PW / 2, s * HW, s * (HW + CD + TH + 0.3), CH_H + 0.65, CH_H + 0.95, 'oclusor'))
    # a shell round the apse from its wall's top up to the roof: without it the sun came in over the half dome, and through
    # its cracks (the reviewer's dotted lines of sun)
    m = Mesh('o_abside_alto', 'oclusor'); n = 48
    angs = [-math.pi / 2 + math.pi * k / n for k in range(n + 1)]
    rings = [[m.vert((XA + r * math.cos(a), y, r * math.sin(a))) for a in angs] for y in (S + 0.1, WALL_H + 0.5) for r in (HW + THN, HW + THN + 0.4)]
    lo_in, lo_out, hi_in, hi_out = rings
    for i in range(n):
        m.face([lo_in[i], hi_in[i], hi_in[i + 1], lo_in[i + 1]]); m.face([lo_out[i + 1], hi_out[i + 1], hi_out[i], lo_out[i]])
        m.face([hi_in[i], hi_out[i], hi_out[i + 1], hi_in[i + 1]]); m.face([lo_in[i + 1], lo_out[i + 1], lo_out[i], lo_in[i]])
    for k in (0, n): m.face([lo_in[k], lo_out[k], hi_out[k], hi_in[k]])
    out.append(closed(m.build()))
    D = DOORS['oeste']
    out.append(cube('o_puerta_oeste', X0 - 1.0, X0 - 0.86, -D['w'] / 2 - 0.1, D['w'] / 2 + 0.1, 0, D['spring'] + D['w'] / 2 + 0.1, 'oclusor'))
    xm = BAYS[DOOR_BAY][2]
    for s, key in ((1, 'sur'), (-1, 'norte')):
        D = DOORS[key]; zo = s * (HW + CD)
        out.append(cube(f'o_puerta_{key}', xm - D['w'] / 2 - 0.1, xm + D['w'] / 2 + 0.1, zo + s * 0.86, zo + s * 1.0, 0, D['spring'] + D['w'] / 2 + 0.1, 'oclusor'))
    out.append(cube('o_calle', X0 - 40, XA + 40, -60, 60, -0.6, -0.4, 'oclusor'))
    return out

def import_furniture(path):
    """the church's furniture as the game builds it (src/church.js; exported by tools/hipermuebles.py): it casts its
    shadows in the bake and is not exported"""
    before = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=path)
    new = [o for o in bpy.data.objects if o not in before and o.type == 'MESH']
    for o in new:
        o.data.materials.clear(); o.data.materials.append(M('oclusor')); o.name = 'o_mueble_' + o.name
    return new

# ================================================================ one mesh per material
DETAIL = ('roseta_', 'clave_', 'balaustre_', 'voluta_', 'equino_', 'astragalo_', 'basa_', 'oculo_anillo_')
def merge(obs):
    """one mesh per material (each a draw call) — and the small carved details (rosettes, bosses, balusters, the capitals'
    volutes and eggs, the bases) in a mesh of their own per material: they take less of the light's atlas"""
    groups = {}
    for o in obs:
        if not o or o.type != 'MESH' or not o.data.polygons: continue
        det = o.name.startswith(DETAIL)
        groups.setdefault(det, []).append(o)
    out = {}
    for det, group in groups.items():
        allm = join('todo_det' if det else 'todo', group)
        bpy.ops.object.select_all(action='DESELECT'); allm.select_set(True); bpy.context.view_layer.objects.active = allm
        bpy.ops.object.mode_set(mode='EDIT'); bpy.ops.mesh.select_all(action='SELECT'); bpy.ops.mesh.separate(type='MATERIAL'); bpy.ops.object.mode_set(mode='OBJECT')
        for o in [o for o in COLL.objects if o.type == 'MESH' and o.name.startswith('todo_det' if det else 'todo') and (det or not o.name.startswith('todo_det'))]:
            used = {o.data.materials[p.material_index].name for p in o.data.polygons} if o.data.polygons else set()
            if len(used) != 1: continue
            role = used.pop()
            while len(o.data.materials) > 1:
                idx = next(i for i, m in enumerate(o.data.materials) if m.name != role)
                o.data.materials.pop(index=idx)
            for p in o.data.polygons: p.material_index = 0
            key = role + ('_det' if det else '')
            o.name = key; o.data.name = key
            out[key] = o
    return out

def interior_seeds():
    """points in the church's air (its frame): the nave and the choir bay under their vaults, the chapels, the apse, the
    under-choir and the choir, inside the windows' splays and the doors' reveals"""
    pts = []
    def add(x, y, z): pts.append(B((x, y, z)))
    x = X0 + 0.5
    while x < XA:
        z = -7.5
        while z <= 7.5:
            if x < XC: top = vault_y(x, z, X0, XC, dome=0.4, lun=5.0) - 0.4
            else:
                bi = min(NB - 1, int((x - XC) // BAY)); xa, xb, _ = BAYS[bi]
                top = vault_y(x, z, xa, xb) - 0.4
            y = 0.4
            while y < top:
                if not (x < XC and 4.2 < y < CHY + 0.1): add(x, y, z)
                y += 1.5
            z += 1.5
        x += 1.5
    for bi, (xa, xb, xm) in enumerate(BAYS):
        for s in (-1, 1):
            x = xa + PW / 2 + 0.4
            while x < xb - PW / 2 - 0.3:
                for dz in (0.4, 1.3, 2.2, 2.8):
                    y = 0.4
                    while y < 9.6: add(x, y, s * (HW + dz)); y += 1.2
                x += 1.2
        for s in (-1, 1):
            for y in (13.8, 15.2, 16.6, 17.8): add(xm, y, s * (HW + 0.45)); add(xm, y, s * (HW + 0.9))
    for k in range(25):
        a = -math.pi / 2 + math.pi * k / 24
        for r in (1.0, 3.0, 5.0, 7.2):
            y = P + 0.4
            while y < S + math.sqrt(max(0.0, AR * AR - r * r)) - 0.4: add(XA + r * math.cos(a), y, r * math.sin(a)); y += 1.2
    for y in (1.0, 2.5, 4.0): add(X0 - 0.5, y, 0.0)
    xm = BAYS[DOOR_BAY][2]
    for s in (-1, 1):
        for y in (1.0, 2.5, 4.0): add(xm, y, s * (HW + CD + 0.5))
    for y in (9.0, 10.0, 11.0): add(X0 - 0.3, y, 0.0)
    for sgn in (-1, 1):
        a = sgn * APSE_WIN['a']
        for y in (8.8, 10.0, 11.2): add(XA + (AR + 0.4) * math.cos(a), y, (AR + 0.4) * math.sin(a))
    return pts

def cull_hidden(meshes):
    """the faces nobody inside can see — the walls' outer faces and tops, what lies in the stone or over the vaults —
    out of the model (into an occluder: they still close the church in the bake). A face is seen if, from just in front
    of it, a ray reaches one of the nearest of the points in the church's air (or, for a big face, from one of its
    corners)"""
    from mathutils.bvhtree import BVHTree
    from mathutils.kdtree import KDTree
    import time
    t0 = time.time()
    bm_all = bmesh.new()
    for o in meshes.values(): bm_all.from_mesh(o.data)
    bvh = BVHTree.FromBMesh(bm_all); bm_all.free()
    seeds = interior_seeds()
    kd = KDTree(len(seeds))
    for i, p in enumerate(seeds): kd.insert(p, i)
    kd.balance()
    def seen(q):
        for co, idx, dist in kd.find_n(q, 16):
            d = co - q; L = d.length
            if L < 1e-6: return True
            if bvh.ray_cast(q, d / L, L - 0.005)[0] is None: return True
        return False
    occl, gone = [], 0
    for key, o in list(meshes.items()):
        if key.startswith('vidrio'): continue
        bm = bmesh.new(); bm.from_mesh(o.data); bm.faces.ensure_lookup_table()
        hid = []
        for f in bm.faces:
            n = f.normal; c = f.calc_center_median()
            if seen(c + n * 0.02): continue
            if f.calc_area() > 0.05 and any(seen(v.co * 0.97 + c * 0.03 + n * 0.02) for v in f.verts): continue
            hid.append(f.index)
        if not hid: bm.free(); continue
        gone += len(hid)
        # the hidden faces out of the mesh, and into an occluder of their own
        bm2 = bm.copy(); bm2.faces.ensure_lookup_table()
        hs = set(hid)
        bmesh.ops.delete(bm, geom=[bm.faces[i] for i in hid], context='FACES')
        bmesh.ops.delete(bm2, geom=[f for f in bm2.faces if f.index not in hs], context='FACES')
        bm.to_mesh(o.data); bm.free()
        me2 = bpy.data.meshes.new('o_oculto_' + key); bm2.to_mesh(me2); bm2.free()
        x = bpy.data.objects.new('o_oculto_' + key, me2); COLL.objects.link(x)
        me2.materials.append(M('oclusor')); occl.append(x)
    print(f'  caras ocultas: {gone} fuera del modelo ({len(seeds)} puntos de aire, {time.time() - t0:.0f} s)', flush=True)
    return occl

# ================================================================ the light, baked in Cycles (phase 6a)
TEXDIR = os.path.join(ROOT, 'assets', 'hq', 'interior', 'tex')
BAKED = ('cal', 'granito', 'tambor', 'fuste', 'caseton', 'caseton_fondo', 'sillar', 'suelo', 'oro')
ALBEDO = {'cal': 'cal', 'granito': 'granito', 'tambor': 'granito', 'fuste': 'granito', 'caseton': 'cal', 'caseton_fondo': 'cal', 'sillar': 'granito', 'suelo': 'suelo'}  # (the coffers: whitewashed, as the photo's light dome)
HOURS = (9.5, 12.0, 14.5, 17.0, 19.5)

def sun_direction(hour):
    """sky.js's sunDirection: the real sun over Guareña in late September (solar noon at 14:42), in the church's frame
    (x east, y up, z south — the inside is built square to the world's axes)"""
    LAT, DECL, NOON = math.radians(38.86), math.radians(-0.8), 14.42
    H = math.radians((hour - NOON) * 15)
    alt = math.asin(math.sin(LAT) * math.sin(DECL) + math.cos(LAT) * math.cos(DECL) * math.cos(H))
    az = math.acos(max(-1.0, min(1.0, (math.sin(DECL) - math.sin(alt) * math.sin(LAT)) / (math.cos(alt) * math.cos(LAT)))))
    if H > 0: az = 2 * math.pi - az
    return Vector((math.sin(az) * math.cos(alt), math.sin(alt), -math.cos(az) * math.cos(alt)))

def bake_materials():
    """for the bake: each material's albedo from its texture (the bounce takes its colour), no normal map (a lightmap is
    baked smooth: the textures' relief is the game's to light), the gold not metallic (its lightmap is the light that
    reaches it), the glass out of the light's way. And every surface purely diffuse — the stone's, the furniture's: a
    lightmap holds the light that reaches a surface from all round; the sheen of the floor or of the gilding is the
    game's (its reflections). With a specular layer the sun's patches on the floor glinted onto columns, arches and
    coffers as caustics — sharp-edged blotches that no number of samples smoothed"""
    for m in bpy.data.materials:
        if not m.node_tree: continue
        for p in m.node_tree.nodes:
            if p.type != 'BSDF_PRINCIPLED': continue
            p.inputs['Metallic'].default_value = 0.0
            for k in ('Specular IOR Level', 'Coat Weight', 'Sheen Weight', 'Transmission Weight'):
                if k in p.inputs: p.inputs[k].default_value = 0.0
    for role in BAKED:
        m = M(role); nt = m.node_tree; p = nt.nodes['Principled BSDF']
        p.inputs['Metallic'].default_value = 0.0
        tex = ALBEDO.get(role)
        if tex and os.path.exists(os.path.join(TEXDIR, f'{tex}_diff.jpg')):
            n = nt.nodes.new('ShaderNodeTexImage'); n.image = bpy.data.images.load(os.path.join(TEXDIR, f'{tex}_diff.jpg'), check_existing=True)
            uv = nt.nodes.new('ShaderNodeUVMap'); uv.uv_map = 'UVMap'
            nt.links.new(uv.outputs['UV'], n.inputs['Vector']); nt.links.new(n.outputs['Color'], p.inputs['Base Color'])

def island_colours(objs):
    """the denoiser's guide (its 'albedo'), in a face-corner attribute 'isla': each point's place in the church as a
    colour (x, height, z over the church's size). Pieces side by side in the church get near colours — the denoiser
    smooths across them —, pieces side by side in the atlas but far apart in the church get different ones — it
    does not (a random colour per island stopped it smoothing even between a coffer and the next). Removed before the
    export"""
    n = 0
    for o in objs:
        me = o.data; mw = o.matrix_world
        if 'isla' in me.color_attributes: me.color_attributes.remove(me.color_attributes['isla'])
        ca = me.color_attributes.new('isla', 'FLOAT_COLOR', 'CORNER')
        co = [F(mw @ v.co) for v in me.vertices]
        data = []
        for l in me.loops:
            p = co[l.vertex_index]
            data.extend(((p.x + 27.0) / 56.0, p.y / 24.0, (p.z + 12.0) / 24.0, 1.0))
        ca.data.foreach_set('color', data)
        n += len(me.loops)
    print(f'  guía del quitarruido: el sitio de {n} esquinas', flush=True)

def lightmap_uv(objs):
    """a second UV set, 'LM': every baked surface unwrapped into one atlas, at one density"""
    for o in objs:
        me = o.data
        if 'LM' not in me.uv_layers: me.uv_layers.new(name='LM')
        me.uv_layers['LM'].active = True
    if bpy.context.object and bpy.context.object.mode != 'OBJECT': bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')
    for o in objs: o.select_set(True)
    bpy.context.view_layer.objects.active = objs[0]
    bpy.ops.object.mode_set(mode='EDIT')
    # (the pieces with a projection of their own — 'lm_fijo' — keep it; the rest is smart-projected)
    for o in objs:
        bm = bmesh.from_edit_mesh(o.data); fx = bm.faces.layers.int.get('lm_fijo')
        for f in bm.faces: f.select = not (fx and f[fx])
        bmesh.update_edit_mesh(o.data)
    bpy.ops.uv.smart_project(angle_limit=math.radians(60), island_margin=0.0, area_weight=0.0, correct_aspect=True, scale_to_bounds=False)
    bpy.ops.object.mode_set(mode='OBJECT')
    # their density: the smart-projected faces' UV area per square metre; the projected islands (in metres) scaled to it
    uv_a = geo_a = 0.0
    for o in objs:
        bm = bmesh.new(); bm.from_mesh(o.data); lay = bm.loops.layers.uv['LM']; fx = bm.faces.layers.int.get('lm_fijo')
        for f in bm.faces:
            if fx and f[fx]: continue
            uv = [l[lay].uv for l in f.loops]
            uv_a += sum(abs((uv[k].x - uv[0].x) * (uv[k + 1].y - uv[0].y) - (uv[k + 1].x - uv[0].x) * (uv[k].y - uv[0].y)) / 2 for k in range(1, len(uv) - 1))
            geo_a += f.calc_area()
        bm.free()
    k_m = math.sqrt(uv_a / max(geo_a, 1e-9))
    for o in objs:
        bm = bmesh.new(); bm.from_mesh(o.data); lay = bm.loops.layers.uv['LM']; fx = bm.faces.layers.int.get('lm_fijo')
        if fx:
            for f in bm.faces:
                if f[fx]:
                    for l in f.loops: l[lay].uv = l[lay].uv * k_m
        bm.to_mesh(o.data); bm.free()
    # (one density for all: the vaults and arches as the walls — the reviewer, 2026-10-12)
    bpy.ops.object.mode_set(mode='EDIT'); bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.uv.pack_islands(rotate=True, margin_method='FRACTION', margin=4.0 / min(LM_RES, SUN_RES))  # (4 px of the smallest map)
    bpy.ops.object.mode_set(mode='OBJECT')
    for o in objs:
        o.data.uv_layers['UVMap'].active = True; o.data.uv_layers['UVMap'].active_render = True
    area = sum(p.area for o in objs for p in o.data.polygons)
    print(f'  atlas de luz: {area:.0f} m² en {LM_RES}² → ≈{math.sqrt(area / (LM_RES * LM_RES * 0.6)) * 100:.1f} cm por texel', flush=True)

def uv_stats(objs):
    """how the atlas is used: its islands, and how much of the square they fill"""
    from bpy_extras.bmesh_utils import bmesh_linked_uv_islands
    tot_isl, uv_area, lo, hi = 0, 0.0, [1e9, 1e9], [-1e9, -1e9]
    for o in objs:
        bm = bmesh.new(); bm.from_mesh(o.data)
        lay = bm.loops.layers.uv['LM']
        isl = bmesh_linked_uv_islands(bm, lay)
        sizes = sorted((len(i) for i in isl), reverse=True)
        a = 0.0
        for f in bm.faces:
            uv = [l[lay].uv for l in f.loops]
            for k in range(1, len(uv) - 1):
                a += abs((uv[k].x - uv[0].x) * (uv[k + 1].y - uv[0].y) - (uv[k + 1].x - uv[0].x) * (uv[k].y - uv[0].y)) / 2
            for v in uv: lo[0] = min(lo[0], v.x); lo[1] = min(lo[1], v.y); hi[0] = max(hi[0], v.x); hi[1] = max(hi[1], v.y)
        print(f'  {o.name:8s} {len(bm.faces):7d} caras, {len(isl):6d} islas (las mayores: {sizes[:5]}), área UV {a:.4f}', flush=True)
        tot_isl += len(isl); uv_area += a
        bm.free()
    print(f'  total: {tot_isl} islas, área UV ocupada {uv_area:.3f} de 1; caja {lo} → {hi}', flush=True)

def gpu():
    try:
        prefs = bpy.context.preferences.addons['cycles'].preferences
        prefs.compute_device_type = 'METAL'; prefs.get_devices()
        if any(d.type == 'METAL' for d in prefs.devices):
            for d in prefs.devices: d.use = d.type == 'METAL'
            SC.cycles.device = 'GPU'; return 'GPU'
    except Exception as e: print('Cycles en CPU:', e)
    return 'CPU'

def window_frames():
    """each window's light (its glass) as a centre, a width and height, and the inward normal (Blender's frame)"""
    out = []
    for s in (-1, 1):
        for xa, xb, xm in BAYS:
            c = (xm, (WIN['ly0'] + WIN['ly1']) / 2, s * (HW + THN * 0.7 + 0.1))
            out.append((c, WIN['light'], WIN['ly1'] - WIN['ly0'], (0, 0, -s), (1, 0, 0)))
    for sgn in (-1, 1):
        a = sgn * APSE_WIN['a']
        c = (XA + (AR + 1.1) * math.cos(a), (APSE_WIN['y0'] + APSE_WIN['y1']) / 2, (AR + 1.1) * math.sin(a))
        out.append((c, APSE_WIN['w'], APSE_WIN['y1'] - APSE_WIN['y0'], (-math.cos(a), 0, -math.sin(a)), (-math.sin(a), 0, math.cos(a))))
    out.append(((X0 - 0.7, OCULUS['y'], 0), 2 * OCULUS['r'], 2 * OCULUS['r'], (1, 0, 0), (0, 0, -1)))
    return out

def add_portals():
    """Cycles' light portals in the windows: the sky's light is looked for through them (a church lit by its windows
    bakes clean in a tenth of the samples)"""
    obs = []
    for k, (c, w, h, n, u) in enumerate(window_frames()):
        L = bpy.data.lights.new(f'portal_{k}', 'AREA'); L.shape = 'RECTANGLE'; L.size = w; L.size_y = h
        L.cycles.is_portal = True
        ob = bpy.data.objects.new(f'portal_{k}', L); COLL.objects.link(ob)
        ob.location = B(c)
        ob.rotation_euler = B(n).normalized().to_track_quat('-Z', 'Y').to_euler()  # (an area light shines along its −Z: into the church)
        obs.append(ob)
    return obs

def night_lamps():
    """the night's lights, as church.js hangs them: four chandeliers over the nave, the retablo's two spots, the
    under-choir's and the apse's lamps, the candles at three stands, the sanctuary lamp (red)"""
    obs = []
    def point(name, p, watts, radius, col=(1.0, 0.82, 0.6)):
        L = bpy.data.lights.new(name, 'POINT'); L.energy = watts; L.shadow_soft_size = radius; L.color = col
        ob = bpy.data.objects.new(name, L); COLL.objects.link(ob); ob.location = B(p); obs.append(ob)
    for k, (xa, xb, xm) in enumerate(BAYS): point(f'arana_{k}', (xm, 7.4, 0), 2400, 1.1)
    point('sotocoro', (XC - 3.5, 4.0, 0), 500, 0.3)
    point('abside', (XA + 3, 10, 0), 900, 0.4)
    for bi, s in ((0, 1), (1, -1), (3, 1)):
        point(f'velas_{bi}', (BAYS[bi][2] + 2.0, 1.2, s * (HW + 0.9)), 60, 0.25, (1.0, 0.65, 0.3))
    point('lampara', (XA + 3.2, P + 3.3, -2.6), 25, 0.12, (1.0, 0.25, 0.15))
    for z in (-3.5, 3.5):
        L = bpy.data.lights.new(f'foco_{z}', 'SPOT'); L.energy = 6000; L.spot_size = 1.1; L.spot_blend = 0.6; L.color = (1.0, 0.85, 0.63); L.shadow_soft_size = 0.15
        ob = bpy.data.objects.new(f'foco_{z}', L); COLL.objects.link(ob)
        p, t = B((XP + 1.6, 4.2, z)), B((XA + AR - 1.2, 7.5, z * 0.3))
        ob.location = p; ob.rotation_euler = (t - p).to_track_quat('-Z', 'Y').to_euler(); obs.append(ob)
    return obs

def denoise(img, nimg=None, aimg=None):
    """Open Image Denoise through the compositor, on its own little scene (HDR, the lightmap's own), guided by the
    surfaces' normals (nimg, in −1…1) so that it does not smear the light across an edge or from one island to the next"""
    N = img.size[0]
    sc = bpy.data.scenes.get('quitarruido') or bpy.data.scenes.new('quitarruido')
    sc.render.engine = 'BLENDER_WORKBENCH'
    sc.render.resolution_x = sc.render.resolution_y = N; sc.render.resolution_percentage = 100
    if not sc.camera:
        cam = bpy.data.objects.new('cam_qr', bpy.data.cameras.new('cam_qr')); sc.collection.objects.link(cam); sc.camera = cam
    tree = bpy.data.node_groups.new('qr', 'CompositorNodeTree'); sc.compositing_node_group = tree
    tree.interface.new_socket('Image', in_out='OUTPUT', socket_type='NodeSocketColor')
    a = tree.nodes.new('CompositorNodeImage'); a.image = img
    d = tree.nodes.new('CompositorNodeDenoise')
    try: d.inputs['HDR'].default_value = True
    except Exception: pass
    # (the guides are baked, free of noise: taken as they are, at the best quality)
    for sock, val in (('Prefilter', 'None'), ('Quality', 'High')):
        try: d.inputs[sock].default_value = val
        except Exception: pass
    o = tree.nodes.new('NodeGroupOutput')
    tree.links.new(a.outputs['Image'], d.inputs['Image']); tree.links.new(d.outputs['Image'], o.inputs[0])
    if nimg is not None:
        nn = tree.nodes.new('CompositorNodeImage'); nn.image = nimg
        tree.links.new(nn.outputs['Image'], d.inputs['Normal'])
    if aimg is not None:   # (each island its own colour: no blending across them)
        na = tree.nodes.new('CompositorNodeImage'); na.image = aimg
        tree.links.new(na.outputs['Image'], d.inputs['Albedo'])
    sc.render.image_settings.file_format = 'OPEN_EXR'; sc.render.image_settings.color_depth = '32'
    path = os.path.join(bpy.app.tempdir, img.name + '_qr.exr'); sc.render.filepath = path
    bpy.ops.render.render(write_still=True, scene=sc.name)
    r = bpy.data.images.load(path)
    import numpy as np
    px = np.empty(N * N * 4, np.float32); r.pixels.foreach_get(px)
    bpy.data.node_groups.remove(tree)
    return px.reshape(N, N, 4)[..., :3]

def bilateral(rgb, pos, nrm, cover, radius, s_pos=0.22, s_nrm=0.25):
    """a joint bilateral filter over the atlas: each texel the average of its neighbours within `radius` texels, each
    weighed by how near it is in the church (s_pos, metres) and how alike its facing (s_nrm) — the noise the denoiser
    leaves in the dim light (the sun's bounce late in the day, the coffers) smoothed within a surface, never across an
    edge or into a piece far away"""
    import numpy as np
    acc = np.zeros_like(rgb); ws = np.zeros(rgb.shape[:2], np.float32)
    cv = cover.astype(np.float32)
    k2 = 2 * (radius / 2.0) ** 2
    for dy in range(-radius, radius + 1):
        for dx in range(-radius, radius + 1):
            sh = lambda a: np.roll(np.roll(a, dy, 0), dx, 1)
            dp = sh(pos) - pos; dn = 1.0 - (sh(nrm) * nrm).sum(-1)
            w = np.exp(-(dp * dp).sum(-1) / (2 * s_pos * s_pos) - dn * dn / (2 * s_nrm * s_nrm) - (dx * dx + dy * dy) / k2) * sh(cv)
            acc += w[..., None] * sh(rgb); ws += w
    out = acc / np.maximum(ws, 1e-6)[..., None]
    return np.where(cover[..., None], out, rgb)

def save_lightmap(name, rgb, cover, cap=None):
    """a lightmap to a JPEG: its values over a scale, in sRGB — the game reads it back with the scale (interior.json).
    The scale is the 99,7th percentile of what the light reaches, or `cap` if lower: what lies over it (a window's
    splay in the sky's full light, a hundred times the nave's) is white on the screen anyway, and the eight bits are
    kept for the church's half-light"""
    import numpy as np
    N = rgb.shape[0]
    lum = rgb @ np.array([0.2126, 0.7152, 0.0722])
    scale = float(np.percentile(lum[cover], 99.7)) if cover.any() else 1.0
    if cap: scale = min(scale, cap)
    # (its luminance only, R = G = B: the stone and the lime are grey, the light baked on them all but colourless — the game
    # gives it the sky's, the sun's or the lamps' colour; lossless WebP packs three equal channels into about one)
    v = np.clip(np.repeat(lum[..., None], 3, -1) / max(scale, 1e-6), 0, 1)
    v = np.where(v <= 0.0031308, v * 12.92, 1.055 * np.power(v, 1 / 2.4) - 0.055)
    img = bpy.data.images.new('lm_' + name, N, N, alpha=False); img.colorspace_settings.name = 'Non-Color'
    img.pixels.foreach_set(np.concatenate([v, np.ones((N, N, 1))], -1).astype(np.float32).ravel())
    os.makedirs(os.path.join(OUT, 'luz'), exist_ok=True)
    # (WebP at quality 100 is lossless: no JPEG blocks in the light — the reviewer's pixelated mouldings)
    st = SC.render.image_settings; st.file_format = 'WEBP'; st.quality = 100; st.color_mode = 'RGB'   # (a Non-Color image saves its values as they are)
    path = os.path.join(OUT, 'luz', name + '.webp')
    img.save_render(path, scene=SC)
    med = float(np.median(lum[cover]))
    print(f'  luz/{name}.webp: escala {scale:.4f}, mediana {med:.4f} ({os.path.getsize(path) // 1024} KB)', flush=True)
    return {'escala': round(scale, 6), 'mediana': round(med, 6)}


# ---------------------------------------------------------------- the light probes (for what is not baked)
PROBE = 1.5          # the grid's step
PROBE_RES = 512      # their image: a 2 × 2 px block a face
DIRS = [((1, 0, 0), (0, 1, 0), (0, 0, 1)), ((-1, 0, 0), (0, 0, 1), (0, 1, 0)), ((0, 1, 0), (0, 0, 1), (1, 0, 0)),
        ((0, -1, 0), (1, 0, 0), (0, 0, 1)), ((0, 0, 1), (1, 0, 0), (0, 1, 0)), ((0, 0, -1), (0, 1, 0), (1, 0, 0))]  # (d, u, v: u × v = d)

def probe_grid():
    gx0, gy0, gz0 = X0 - 0.5, 0.5, -(HW + CD + 0.5)
    nx = int((XA + AR + 0.5 - gx0) / PROBE) + 1; ny = int((WALL_H - 0.4 - gy0) / PROBE) + 1; nz = int((HW + CD + 0.5 - gz0) / PROBE) + 1
    return gx0, gy0, gz0, nx, ny, nz

def build_probes(meshes, occl):
    """the light probes for what is not baked (the furniture, the people), as the engines' probe grids: a point every
    1,5 m through the church; each in its air (it sees one of the points of the air) gets a cube of 2 cm whose six
    faces bake the light from their side — an «ambient cube» — each into a 2 × 2 px block of its own image. The cubes
    are seen by the bake alone (no shadow, no bounce)"""
    from mathutils.bvhtree import BVHTree
    from mathutils.kdtree import KDTree
    bm_all = bmesh.new()
    for o in list(meshes.values()) + [o for o in occl if o.name.startswith('o_oculto_')]: bm_all.from_mesh(o.data)
    bvh = BVHTree.FromBMesh(bm_all); bm_all.free()
    seeds = interior_seeds(); kd = KDTree(len(seeds))
    for i, p in enumerate(seeds): kd.insert(p, i)
    kd.balance()
    gx0, gy0, gz0, nx, ny, nz = probe_grid()
    valid = []
    for k in range(nz):
        for j in range(ny):
            for i in range(nx):
                q = B((gx0 + i * PROBE, gy0 + j * PROBE, gz0 + k * PROBE))
                for co, idx, dist in kd.find_n(q, 8):
                    d = co - q; L = d.length
                    if L < 1e-6 or bvh.ray_cast(q, d / L, L - 0.005)[0] is None: valid.append((i, j, k)); break
    m = Mesh('sondas', 'sonda'); h = 0.01; W2 = PROBE_RES // 2
    for n, (i, j, k) in enumerate(valid):
        c = Vector((gx0 + i * PROBE, gy0 + j * PROBE, gz0 + k * PROBE))
        for f, (d, u, v) in enumerate(DIRS):
            d, u, v = Vector(d), Vector(u), Vector(v)
            q = [m.vert(c + d * h + (-u - v) * h), m.vert(c + d * h + (u - v) * h), m.vert(c + d * h + (u + v) * h), m.vert(c + d * h + (-u + v) * h)]
            b = n * 6 + f; bx, by = (b % W2) * 2, (b // W2) * 2
            lo, hi = (bx + 0.05) / PROBE_RES, (bx + 1.95) / PROBE_RES
            lo_y, hi_y = (by + 0.05) / PROBE_RES, (by + 1.95) / PROBE_RES
            m.face(q, lm=[(lo, lo_y), (hi, lo_y), (hi, hi_y), (lo, hi_y)])
    ob = m.build()
    for kk in ('visible_diffuse', 'visible_glossy', 'visible_transmission', 'visible_volume_scatter', 'visible_shadow'): setattr(ob, kk, False)
    print(f'  sondas de luz: {len(valid)} de {nx * ny * nz} puntos de la rejilla ({nx} × {ny} × {nz}, cada {PROBE} m)', flush=True)
    return ob, valid

def probe_values(img, valid):
    """the six faces' light of each probe: the mean of its 2 × 2 px blocks"""
    import numpy as np
    R = img.size[0]
    px = np.empty(R * R * 4, np.float32); img.pixels.foreach_get(px); px = px.reshape(R, R, 4)[..., :3]
    W2 = R // 2; out = np.zeros((len(valid), 6, 3), np.float32)
    for n in range(len(valid)):
        for f in range(6):
            b = n * 6 + f; bx, by = (b % W2) * 2, (b // W2) * 2
            out[n, f] = px[by:by + 2, bx:bx + 2].mean((0, 1))
    return out

def save_probes(valid, values, luz):
    """the probes for the game (luz/sondas.bin): the whole grid, the points outside the air filled from their
    neighbours in it (the game interpolates between eight), each value over its lightmap's scale in sRGB, one byte"""
    import numpy as np
    gx0, gy0, gz0, nx, ny, nz = probe_grid()
    names = ['cielo'] + [f'sol_{int(hh):02d}{int(round(hh % 1 * 60)):02d}' for hh in HOURS] + ['noche']
    scales = [luz['cielo']['escala']] + [x['escala'] for x in luz['sol']] + [luz['noche']['escala']]
    out = np.zeros((len(names), nz, ny, nx, 6, 3), np.uint8)
    for c, (nm, sc) in enumerate(zip(names, scales)):
        grid = np.zeros((nz, ny, nx, 6, 3), np.float32); have = np.zeros((nz, ny, nx), bool)
        for n, (i, j, k) in enumerate(valid): grid[k, j, i] = values[nm][n]; have[k, j, i] = True
        for _ in range(6):   # (fill outwards, a step at a time, from the points that have light)
            if have.all(): break
            acc = np.zeros_like(grid); cnt = np.zeros(have.shape, np.float32)
            for ax in range(3):
                for sh in (-1, 1):
                    g2 = np.roll(grid, sh, axis=ax); h2 = np.roll(have, sh, axis=ax)
                    edge = [slice(None)] * 3; edge[ax] = 0 if sh == 1 else -1
                    h2 = h2.copy(); h2[tuple(edge)] = False
                    acc += g2 * h2[..., None, None]; cnt += h2
            fill = (~have) & (cnt > 0)
            grid[fill] = acc[fill] / cnt[fill][..., None, None]; have = have | fill
        v = np.clip(grid / max(sc, 1e-9), 0, 1)
        v = np.where(v <= 0.0031308, v * 12.92, 1.055 * np.power(v, 1 / 2.4) - 0.055)
        out[c] = np.round(v * 255).astype(np.uint8)
    os.makedirs(os.path.join(OUT, 'luz'), exist_ok=True)
    out.tofile(os.path.join(OUT, 'luz', 'sondas.bin'))
    print(f'  luz/sondas.bin: {out.nbytes // 1024} KB', flush=True)
    return {'origen': [gx0, gy0, gz0], 'paso': PROBE, 'n': [nx, ny, nz], 'orden': names}

def smooth_shaft_normals(f, on):
    """the shafts baked as smooth cylinders: their normals round each column's axis (on), or back as they were"""
    bpy.ops.object.select_all(action='DESELECT'); f.select_set(True); bpy.context.view_layer.objects.active = f
    if on:
        cols = [(x, s * (HW + 0.05)) for x in PIERS for s in (-1, 1)]
        nrm = []
        for v in f.data.vertices:
            c = F(v.co)
            cx, cz = min(cols, key=lambda q: (q[0] - c.x) ** 2 + (q[1] - c.z) ** 2)
            nrm.append(B(Vector((c.x - cx, 0.0, c.z - cz)).normalized()))
        f.data.normals_split_custom_set_from_vertices(nrm)
    else:
        bpy.ops.mesh.customdata_custom_splitnormals_clear()
        bpy.ops.object.shade_smooth_by_angle(angle=math.radians(38), keep_sharp_edges=True)

def bake_light(meshes, occl):
    """the bakes: the sky through the windows (white, radiance 1, the street under it: direct and bounced), the sun's
    bounce alone at each of HOURS (a sun of strength 1; its direct light is the game's, in real time), and the night's
    lamps (direct and bounced). Each is denoised and saved as a lightmap over the 'LM' UVs"""
    import numpy as np, time
    objs = [o for k, o in meshes.items() if k.split('_')[0] in BAKED]
    bake_materials()
    lightmap_uv(objs)
    if '--diag-uv' in ARGS: uv_stats(objs); return None
    if 'vidrio' in meshes:
        g = meshes['vidrio']
        for k in ('visible_camera', 'visible_diffuse', 'visible_glossy', 'visible_transmission', 'visible_volume_scatter', 'visible_shadow'): setattr(g, k, False)
    SC.render.engine = 'CYCLES'; dev = gpu()
    SC.cycles.samples = SAMPLES; SC.cycles.max_bounces = 6; SC.cycles.diffuse_bounces = 5; SC.cycles.glossy_bounces = 0
    SC.cycles.caustics_reflective = False; SC.cycles.caustics_refractive = False  # (diffuse light only: see bake_materials)
    SC.cycles.transmission_bounces = 0; SC.cycles.transparent_max_bounces = 2
    SC.render.bake.margin = 8; SC.render.bake.margin_type = 'EXTEND'
    SC.render.bake.use_pass_color = False
    targets = []
    for o in objs:
        for m in o.data.materials:
            nt = m.node_tree; n = nt.nodes.new('ShaderNodeTexImage'); nt.nodes.active = n; targets.append(n)
    probes, valid = build_probes(meshes, occl)
    pnt = M('sonda').node_tree; pnode = pnt.nodes.new('ShaderNodeTexImage'); pnt.nodes.active = pnode
    pvals = {}
    if 'fuste' in meshes: smooth_shaft_normals(meshes['fuste'], True)
    world = bpy.data.worlds.new('mundo'); world.use_nodes = True; SC.world = world
    bg = world.node_tree.nodes['Background']
    portals = add_portals()
    lamps = night_lamps()
    sun = bpy.data.objects.new('sol', bpy.data.lights.new('sol', 'SUN')); COLL.objects.link(sun)
    sun.data.energy = 1.0; sun.data.angle = math.radians(0.53)
    covers, guides, isles = {}, {}, {}
    ISLES = '--sin-islas' not in ARGS
    if ISLES: island_colours(objs)
    def isle_guide(res):
        """the denoiser's guide over the atlas (baked as light, once a resolution): each texel's place in the church —
        it keeps the denoiser from blending the light of pieces far apart in the church but side by side in the atlas
        (the sun's bounce, noisy, came out in sharp-edged blotches)"""
        if res in isles: return isles[res]
        img = bpy.data.images.new(f'islas_{res}', res, res, alpha=False, float_buffer=True); img.colorspace_settings.name = 'Non-Color'
        mat = bpy.data.materials.get('islas_bake') or bpy.data.materials.new('islas_bake')
        mat.use_nodes = True; nt = mat.node_tree; nt.nodes.clear()
        at = nt.nodes.new('ShaderNodeAttribute'); at.attribute_name = 'isla'
        em = nt.nodes.new('ShaderNodeEmission'); outn = nt.nodes.new('ShaderNodeOutputMaterial')
        nt.links.new(at.outputs['Color'], em.inputs['Color']); nt.links.new(em.outputs['Emission'], outn.inputs['Surface'])
        tn = nt.nodes.new('ShaderNodeTexImage'); tn.image = img; nt.nodes.active = tn
        keep = {o: [sl.material for sl in o.material_slots] for o in objs}
        for o in objs:
            for sl in o.material_slots: sl.material = mat
        bpy.ops.object.select_all(action='DESELECT')
        for o in objs: o.select_set(True)
        bpy.context.view_layer.objects.active = objs[0]
        # (on the CPU: one sample of flat colour; and Cycles' Metal kernels crashed compiling for this bake)
        # (gpu() leaves only the Metal devices on: the CPU's, on for this bake alone)
        samples, device = SC.cycles.samples, SC.cycles.device
        prefs = bpy.context.preferences.addons['cycles'].preferences
        used = {d.name: d.use for d in prefs.devices}
        for d in prefs.devices:
            if d.type == 'CPU': d.use = True
        SC.cycles.samples = 1; SC.cycles.device = 'CPU'
        bpy.ops.object.bake(type='EMIT', uv_layer='LM', use_clear=True, margin=8)
        SC.cycles.samples = samples; SC.cycles.device = device
        for d in prefs.devices: d.use = used.get(d.name, d.use)
        px = np.empty(res * res * 4, np.float32); img.pixels.foreach_get(px); px = px.reshape(res, res, 4)
        print(f'  guía de islas {res}: media {px[..., :3].mean():.3f}, NaN {int(np.isnan(px).sum())}, ceros {int((px[..., :3].sum(-1) == 0).sum())}', flush=True)
        for o, ms in keep.items():
            for sl, m in zip(o.material_slots, ms): sl.material = m
        isles[res] = img
        return img
    def guide(res):
        """the surfaces' normals over the atlas, for the denoiser (baked once a resolution)"""
        if res in guides: return guides[res]
        g = bpy.data.images.new(f'normales_{res}', res, res, alpha=False, float_buffer=True)
        for n in targets: n.image = g
        bpy.ops.object.select_all(action='DESELECT')
        for o in objs: o.select_set(True)
        bpy.context.view_layer.objects.active = objs[0]
        bpy.ops.object.bake(type='NORMAL', normal_space='OBJECT', uv_layer='LM', use_clear=True, margin=8)
        px = np.empty(res * res * 4, np.float32); g.pixels.foreach_get(px); px = px.reshape(res, res, 4)
        px[..., :3] = px[..., :3] * 2 - 1
        g2 = bpy.data.images.new(f'normales_{res}_n', res, res, alpha=False, float_buffer=True); g2.colorspace_settings.name = 'Non-Color'
        g2.pixels.foreach_set(px.ravel())
        guides[res] = g2
        return g2
    def run(name, sky, sun_dir, night, passes, cap=None, res=LM_RES, samples=SAMPLES):
        SC.cycles.samples = samples
        bg.inputs['Color'].default_value = (1, 1, 1, 1); bg.inputs['Strength'].default_value = sky
        for p in portals: p.hide_render = sky == 0
        for l in lamps: l.hide_render = not night
        sun.hide_render = sun_dir is None
        if sun_dir is not None: sun.rotation_euler = B(sun_dir).normalized().to_track_quat('Z', 'Y').to_euler()
        ng = guide(res)
        img = bpy.data.images.new(name, res, res, alpha=False, float_buffer=True)
        for n in targets: n.image = img
        pimg = bpy.data.images.new('sondas_' + name, PROBE_RES, PROBE_RES, alpha=False, float_buffer=True); pnode.image = pimg
        bpy.ops.object.select_all(action='DESELECT')
        for o in objs + [probes]: o.select_set(True)
        bpy.context.view_layer.objects.active = objs[0]
        t0 = time.time()
        bpy.ops.object.bake(type='DIFFUSE', pass_filter=passes, uv_layer='LM', use_clear=True, margin=8)
        # (the half dome's and the arch's coffers: deep, small, lit only by what bounces into them — again, with four
        # times the samples, over their own texels; the rest of the atlas is kept)
        deep = [o for k, o in meshes.items() if k.startswith('caseton')]
        if deep and samples < 4 * SAMPLES:
            SC.cycles.samples = 4 * samples
            bpy.ops.object.select_all(action='DESELECT')
            for o in deep: o.select_set(True)
            bpy.context.view_layer.objects.active = deep[0]
            bpy.ops.object.bake(type='DIFFUSE', pass_filter=passes, uv_layer='LM', use_clear=False, margin=8)
            SC.cycles.samples = samples
        raw = np.empty(res * res * 4, np.float32); img.pixels.foreach_get(raw); raw = raw.reshape(res, res, 4)
        if res not in covers: covers[res] = raw[..., :3].sum(-1) > 1e-7
        cover = covers[res]
        pvals[name] = probe_values(pimg, valid)
        rgb = denoise(img, ng, isle_guide(res) if ISLES else None)
        if not np.isfinite(rgb).all():
            print(f'  {name}: el quitarruido dio {int((~np.isfinite(rgb)).sum())} valores no finitos; sin la guía de islas', flush=True)
            rgb = denoise(img, ng)
        if ISLES and BILATERAL:
            t1 = time.time()
            pg = np.empty(res * res * 4, np.float32); isles[res].pixels.foreach_get(pg); pg = pg.reshape(res, res, 4)[..., :3]
            pos = np.stack([pg[..., 0] * 56.0 - 27.0, pg[..., 1] * 24.0, pg[..., 2] * 24.0 - 12.0], -1)
            nn = np.empty(res * res * 4, np.float32); ng.pixels.foreach_get(nn); nn = nn.reshape(res, res, 4)[..., :3]
            nn = nn / np.maximum(np.linalg.norm(nn, axis=-1, keepdims=True), 1e-6)
            geo = pg.sum(-1) > 0   # (every texel of an island, lit or not: the guide covers them all)
            rgb = bilateral(rgb.astype(np.float32), pos.astype(np.float32), nn.astype(np.float32), geo, radius=6 if res <= 2048 else 4)
            print(f'  {name}: filtro bilateral {time.time() - t1:.0f} s', flush=True)
        print(f'  horneado {name} ({dev}, {samples} muestras): {time.time() - t0:.0f} s — crudo {float(raw[..., :3].mean()):.4g}, cubiertos {int(cover.sum())}, quitarruido {float(np.nanmean(rgb)):.4g}', flush=True)
        return save_lightmap(name, rgb, cover, cap(rgb, cover) if callable(cap) else cap)
    luz = {'res': LM_RES, 'muestras': SAMPLES, 'muestras_sol': SUN_SAMPLES, 'horas': list(HOURS), 'formato': 'webp'}
    # (the caps: 24 times the half-light's median for the sky and the lamps; the sun's bounce, three times the sky's
    # median — in the game its light is about as strong as the sky's at noon, π × 4,4 against 0,5)
    med = lambda rgb, cover: float(np.median((rgb @ np.array([0.2126, 0.7152, 0.0722]))[cover]))
    luz['cielo'] = run('cielo', 1.0, None, False, {'DIRECT', 'INDIRECT'}, lambda rgb, c: 24 * med(rgb, c))
    sky_med = luz['cielo']['mediana']
    luz['sol'] = [run(f'sol_{int(h):02d}{int(round(h % 1 * 60)):02d}', 0.0, sun_direction(h), False, {'INDIRECT'}, 3 * sky_med, SUN_RES, SUN_SAMPLES) for h in HOURS]
    luz['noche'] = run('noche', 0.0, None, True, {'DIRECT', 'INDIRECT'}, lambda rgb, c: 24 * med(rgb, c))
    luz['res_sol'] = SUN_RES
    luz['sondas'] = save_probes(valid, pvals, luz)
    bpy.data.objects.remove(probes)
    if 'fuste' in meshes: smooth_shaft_normals(meshes['fuste'], False)
    return luz

# ================================================================ main
def smooth(meshes):
    """smooth where the surface is curved, sharp at its edges (a box's corners, a moulding's arrises); the furniture's
    rounded edges (two or three faces round a corner) smooth too"""
    for furn in (False, True):
        group = [o for k, o in meshes.items() if (k.split('_')[0] in FURN_ROLES) == furn]
        if not group: continue
        bpy.ops.object.select_all(action='DESELECT')
        for o in group: o.select_set(True)
        bpy.context.view_layer.objects.active = group[0]
        bpy.ops.object.shade_smooth_by_angle(angle=math.radians(61 if furn else 38), keep_sharp_edges=True)

def marks():
    """what the game must know of the model (interior.json): its windows, where the beams of sunlight come in (the
    light of each, on the wall's inner line, its normal outwards)"""
    win = []
    for s in (-1, 1):
        for xa, xb, xm in BAYS: win.append({'x': xm, 'z': s * HW, 'nx': 0, 'nz': s, 'w': WIN['light'], 'y0': WIN['ly0'], 'y1': WIN['ly1']})
    for sgn in (-1, 1):
        a = sgn * APSE_WIN['a']
        win.append({'x': round(XA + AR * math.cos(a), 3), 'z': round(AR * math.sin(a), 3), 'nx': round(math.cos(a), 4), 'nz': round(math.sin(a), 4), 'w': APSE_WIN['w'], 'y0': APSE_WIN['y0'], 'y1': APSE_WIN['y1'], 'apse': True})
    win.append({'x': X0, 'z': 0, 'nx': -1, 'nz': 0, 'w': 2 * OCULUS['r'], 'y0': OCULUS['y'] - OCULUS['r'], 'y1': OCULUS['y'] + OCULUS['r'], 'round': True})
    return {'ventanas': win}

print('interior: construyendo', flush=True)
obs = build_architecture()
FURN_ROLES = ()
if MUEBLES_HD:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import muebles
    furn = muebles.build(sys.modules[__name__], None if MUEBLES_HD == 'todo' else MUEBLES_HD.split(','))
    FURN_ROLES = tuple(muebles.ROLES)
    BAKED = BAKED + FURN_ROLES
    ALBEDO.update({r: muebles.TEXTURE.get(r, r) for r in FURN_ROLES})
    print(f'interior: {len(furn)} piezas de muebles', flush=True)
    obs += furn
meshes = merge(obs)
smooth(meshes)
occl = build_occluders()
if MUEBLES and os.path.exists(MUEBLES): occl += import_furniture(MUEBLES)
# (only the architecture's hidden faces go: the furniture stays whole — it is seen from where the air's points are not,
# between the pews — and it does not hide the floor under it)
if not GREY: occl += cull_hidden({k: o for k, o in meshes.items() if k.split('_')[0] not in FURN_ROLES})
LUZ = bake_light(meshes, occl) if LIGHT else None
for role, o in sorted(meshes.items()): print(f'  {role:9s} {len(o.data.polygons):7d} caras')

os.makedirs(OUT, exist_ok=True)
# the faces nobody inside sees still cast the sun's shadows in the game (without them the walls are paper-thin to its
# shadow map, and the sun creeps in at the corners): they go out as 'sombra', a mesh that only casts shadows
hid = [o for o in COLL.objects if o.type == 'MESH' and (o.name.startswith('o_oculto_') or o.name.startswith('o_tejado') or o.name.startswith('o_capillas_techo') or o.name.startswith('o_abside_alto'))]
if hid:
    sombra = join('sombra', hid)  # (the bake is done: the occluders can be spent)
    sombra.data.materials.clear(); sombra.data.materials.append(bpy.data.materials.get('sombra') or bpy.data.materials.new('sombra'))
    sombra.data.name = 'sombra'
    for uvl in list(sombra.data.uv_layers): sombra.data.uv_layers.remove(uvl)
    meshes['sombra'] = sombra
for m in bpy.data.materials:
    if m.use_nodes:
        for n in list(m.node_tree.nodes):
            if n.type in ('TEX_IMAGE', 'UVMAP'): m.node_tree.nodes.remove(n)
bpy.ops.object.select_all(action='DESELECT')
for role, o in meshes.items(): o.select_set(True)
glb = os.path.join(OUT, 'interior.glb')
for k, o in meshes.items():
    for nm in ('Col', 'isla'):
        ca = o.data.color_attributes.get(nm)
        if ca: o.data.color_attributes.remove(ca)   # (no colours: the bake has the recesses; the islands' were the denoiser's)
bpy.ops.export_scene.gltf(filepath=glb, export_format='GLB', use_selection=True, export_yup=True, export_apply=True,
                          export_texcoords=True, export_normals=True, export_materials='EXPORT', export_vertex_color='ACTIVE', export_all_vertex_colors=False,
                          export_meshopt_compression_enable=True)
MK = marks()
if LUZ: MK['luz'] = LUZ
if MUEBLES_HD: MK['muebles'] = list(muebles.BUILT)
json.dump(MK, open(os.path.join(OUT, 'interior.json'), 'w'), indent=1)
tris = sum(len(o.data.polygons) for o in meshes.values())
print(f'interior: {tris} caras → {glb} ({os.path.getsize(glb) // 1024} KB)')
