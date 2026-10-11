# Santa María de Guareña, hyperreal (docs/hiperrealismo.md is the source of truth; SPEC copies its table). Built in
# Blender, headless, on the church's own frame as the game works it out (data/hq/iglesia_marco.json: its Catastro
# outline in local metres — x along the axis towards the apse, z across, + south — and the west front's line x0):
#   /Applications/Blender.app/Contents/MacOS/Blender --background --factory-startup --python tools/blender/iglesia.py -- [--greybox] [--sin-ao] [--out assets/hq/iglesia.glb]
# --greybox: the volumes only, in grey (phase 1). Without it (phases 2–4): every piece in its material, the openings cut
# for real, the textures of tools/blender/texturas.py (run it first: .cache/hq/tex), the stone's ambient occlusion baked
# in Cycles over a second UV set (--sin-ao skips it), one mesh per material, and assets/hq/iglesia.json beside the model
# with what the game must know (the buttresses for colliders, the bells, the nests).
# Blender is Z-up: a local point (x, y up, z) is made at Blender (x, -z, y); the glTF exporter turns it back to
# three.js's (x, y, z), so the model drops straight into the church's frame (hiper.js).
import bpy, bmesh, json, math, os, sys
from mathutils import Vector

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
ARGS = sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else []
GREY = '--greybox' in ARGS
OUT = ARGS[ARGS.index('--out') + 1] if '--out' in ARGS else os.path.join(ROOT, 'assets', 'hq', 'iglesia.glb')
FRAME = json.load(open(os.path.join(ROOT, 'data', 'hq', 'iglesia_marco.json')))
RING = [(FRAME['ring'][i], FRAME['ring'][i + 1]) for i in range(0, len(FRAME['ring']), 2)]
X0 = FRAME['x0']   # the west front's line

# ---------------------------------------------------------------- the table of docs/hiperrealismo.md
SPEC = {
    # the cornice's top: its edge (0,45 m out) where the photo's line is — the greybox's wall top (22,5 on the wall's
    # plane) matched that line; seen from below, an edge 0,45 m nearer the eye sits that much lower: 22,05
    'cornice': 22.05,
    # the long walls run between the west block and the apse (the Catastro's points 7 and 8 on the north side)
    'walls': (-20.68, 16.66),
    # the tower's west face runs straight from the Catastro's point 1 to its corner: the Catastro draws point 0 skewed
    # 8,8°, the photo shows the face straight (x −26,34) — the photo rules, and it is written down
    'sw_corner': (-26.337, 13.536),
    # the buttresses are flat bands of ashlar on the wall (the cornice runs straight over them); a metre behind the
    # cornice rise the heads of the walls between the side chapels, capped with tiles (the photo's «remates», the
    # orthophoto's «⌐»). The photo's refitted camera and the orthophoto put them at x −11,1, −2,35 and 6,1; a fourth at
    # 14,9, where the row of chapels ends, its band running on to the apse
    'butt': {'xs': (-11.1, -2.35, 6.1, 14.9), 'w': 2.0, 'out': 0.25, 'head': {'back': 0.7, 'to': 9.0, 'w': 1.2, 'top': 23.6}},  # (heads: from 0,7 m behind the face in to |z| 9, the roof's eave; their tiled gables show over the cornice, as in the photo)
    # the nave's own roof, hidden from the street: two slopes over the nave's 18 m, hipped at the west, fanned over the
    # apse (centred at x 15,5); the side chapels' tops round it are flat
    'roof': {'half': 9.0, 'pitch': math.radians(20), 'x0': -20.5, 'apse': 15.5},
    # the windows' openings (the surround and the relief under the sill come in phase 2), one a bay, each in its
    # bay's middle, measured on the photo; the first stands ≈0,5 m higher than the others (the choir inside, likely)
    'window': {'xs': (-16.3, -6.9, 1.6, 10.5), 'sills': (15.1, 14.6, 14.6, 14.6), 'w': 1.4, 'h': 3.8},
    'oculus': {'r': 2.3, 'y': 10.0, 'z': 0.5},       # the great rose over the portal
    'oculus2': {'r': 1.0, 'y': 19.7, 'z': -0.2},     # a small one under the cornice
    'plinth': 1.0,
    # the tower: its body is the outline's corner up to the cornice; above, on one axis (c), the belfry (its cornice
    # 0,25 m over y1, a ball on each corner), the upper stage, a pedestal, the pyramid, the cross
    'tower': {'x0': -26.34, 'x1': -19.0, 'z0': 6.16, 'z1': 13.54, 'c': (-22.6, 9.6),
              'belfry': {'w': 5.7, 'y1': 31.2, 'arch': (1.4, 3.0)},
              'upper': {'w': 2.4, 'y1': 35.5, 'arch': (0.8, 1.6)},
              'pedestal': {'w': 1.2, 'y1': 37.4}, 'spire': {'w': 1.0, 'y1': 39.4}, 'top': 41.5},  # (the cross's top: the photo, ±1 m)
    # the north-west turret: 2 m square, a little back from the corner; over its cornice a curved stone pediment on each
    # face and a pinnacle on each corner (the photo)
    'turret': {'x0': -26.13, 'x1': -24.13, 'z0': -10.45, 'z1': -8.45, 'cornice': 23.75, 'top': 26.2},   # (its pediments' crowns and pinnacles' tips: 26,2, the photo)
    # the gargoyles: eight a side, every 4,8 m from x −19,1 (the photo's two nearest, at −19,1 and −14,3), their spouts
    # ≈2 m under the cornice's edge
    'gargoyles': {'x0': -19.1, 'step': 4.8, 'n': 8, 'y': 19.45},
    # the north-west block (its stair): four slits up its west face, four small windows in its north face, and the
    # ashlar it is dressed with — a 2 m band at the corner of the front, the notch's step, the north wall's end (the photo)
    'nw_block': {'slits': {'z': -9.6, 'ys': (12.5, 14.9, 17.2, 19.4)},
                 'windows': ((-23.48, 18.56), (-24.5, 15.23), (-23.09, 12.16), (-22.47, 5.64)),
                 'band': 2.0},
    'sacristy': 9.0,
    # the west portal stays the game's (churchdoors.js, its door opens), at the photo's size: its pediment ≈7 m up
    'west_portal': {'scale': 0.85},
}

# ---------------------------------------------------------------- the scene
bpy.ops.wm.read_factory_settings(use_empty=True)
COL = bpy.context.scene.collection
MATS = {}
def mat(name, rgb, rough=0.9):
    if name in MATS: return MATS[name]
    m = bpy.data.materials.new(name); m.use_nodes = True
    b = m.node_tree.nodes['Principled BSDF']
    b.inputs['Base Color'].default_value = (*rgb, 1); b.inputs['Roughness'].default_value = rough
    MATS[name] = m
    return m
GREY_M = lambda: mat('greybox', (0.55, 0.55, 0.53))
DARK_M = lambda: mat('hueco', (0.03, 0.03, 0.03))
TILE = {'greybox': 2.0, 'hueco': 1.0}

def B(x, y, z): return (x, -z, y)  # local (x, height, z) → Blender

def finish(name, bm, material):
    """a mesh object from a bmesh, its UVs in metres over the material's tile, faces from the three sides"""
    uv = bm.loops.layers.uv.new('UVMap')
    t = TILE.get(material.name, 2.0)
    bm.normal_update()
    for f in bm.faces:
        n = f.normal
        for l in f.loops:
            p = l.vert.co
            if abs(n.z) > max(abs(n.x), abs(n.y)): l[uv].uv = (p.x / t, p.y / t)
            elif abs(n.x) > abs(n.y): l[uv].uv = (p.y / t, p.z / t)
            else: l[uv].uv = (p.x / t, p.z / t)
    me = bpy.data.meshes.new(name); bm.to_mesh(me); bm.free()
    ob = bpy.data.objects.new(name, me); COL.objects.link(ob)
    me.materials.append(material)
    return ob

def prism(name, pts, y0, y1, material, top=True, bottom=False):
    """an upright prism over a polygon of local (x, z) points, from y0 to y1"""
    bm = bmesh.new()
    lo = [bm.verts.new(B(x, y0, z)) for x, z in pts]
    hi = [bm.verts.new(B(x, y1, z)) for x, z in pts]
    n = len(pts)
    for i in range(n):
        j = (i + 1) % n
        bm.faces.new((lo[i], lo[j], hi[j], hi[i]))
    if top: bm.faces.new(hi)
    if bottom: bm.faces.new(list(reversed(lo)))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    return finish(name, bm, material)

def box(name, x0, x1, z0, z1, y0, y1, material):
    return prism(name, [(x0, z0), (x1, z0), (x1, z1), (x0, z1)], y0, y1, material, top=True, bottom=True)

def poly_area(pts):
    return sum(pts[i][0] * pts[(i + 1) % len(pts)][1] - pts[(i + 1) % len(pts)][0] * pts[i][1] for i in range(len(pts))) / 2

# ---------------------------------------------------------------- the masses (on the Catastro outline)
SW = SPEC['sw_corner']

def south_wall_z(x):
    """the south wall's line, from the tower's corner past the sacristy's (point 33): the Catastro draws it 1,6° off the
    axis"""
    (xa, za), (xb, zb) = SW, RING[33]
    return za + (zb - za) * (x - xa) / (xb - xa)

def west_x(z):
    """the west front's central plane (the Catastro's points 2–3), where the portal and the oculi are"""
    (xa, za), (xb, zb) = RING[2], RING[3]
    return xa + (xb - xa) * (z - za) / (zb - za)

def outline():
    """the main block (the outline less the sacristy, its points 20–32) and the sacristy. The sacristy hides the nave's
    south wall and the apse's south side from the Catastro: the wall runs on to the end of the fourth bay, the apse's
    side mirrors its north one (points 9 and 10)"""
    wb = SPEC['walls'][1]
    hidden = [(RING[10][0], -RING[10][1]), (RING[9][0], -RING[9][1]), (wb, south_wall_z(wb))]
    main = [SW] + RING[1:20] + hidden + [RING[33]]
    if poly_area(main) < 0: main = main[::-1]
    sac = RING[19:34] + hidden[::-1]
    return main, sac

def build_greybox():
    H = SPEC['cornice']
    main, sac = outline()
    prism('nave', main, 0, H, GREY_M())
    prism('sacristia', sac, 0, SPEC['sacristy'], GREY_M())
    # the roof: hipped at the west, its ridge on the axis, fanned over the apse; the rest of the top is flat
    Rf = SPEC['roof']; hw = Rf['half']; yr = H + hw * math.tan(Rf['pitch'])
    xw, xe = Rf['x0'], Rf['apse']
    bm = bmesh.new()
    v = lambda x, y, z: bm.verts.new(B(x, y + 0.02, z))
    nw2, sw, r0, r1 = v(xw, H, -hw), v(xw, H, hw), v(xw + hw, yr, 0), v(xe, yr, 0)
    fan = [v(xe + hw * math.sin(a), H, -hw * math.cos(a)) for a in [math.pi * i / 6 for i in range(7)]]
    bm.faces.new((nw2, fan[0], r1, r0)); bm.faces.new((fan[-1], sw, r0, r1)); bm.faces.new((sw, nw2, r0))
    for i in range(6): bm.faces.new((fan[i], fan[i + 1], r1))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    finish('cubierta', bm, mat('tejado_gris', (0.42, 0.36, 0.33)))
    zn = RING[7][1]  # the north wall's line
    # the tower: the body is the outline's corner; the belfry, the upper stage, the pedestal, the pyramid, the cross
    T = SPEC['tower']; cx, cz = T['c']
    Bf, Up, Pd, Sp = T['belfry'], T['upper'], T['pedestal'], T['spire']
    sq = lambda name, w, y0, y1, m=None: box(name, cx - w / 2, cx + w / 2, cz - w / 2, cz + w / 2, y0, y1, m or GREY_M())
    sq('campanario', Bf['w'], H, Bf['y1']); sq('campanario_cornisa', Bf['w'] + 0.5, Bf['y1'], Bf['y1'] + 0.25)
    y_up = Bf['y1'] + 0.25
    sq('cuerpo_alto', Up['w'], y_up, Up['y1']); sq('cuerpo_alto_cornisa', Up['w'] + 0.4, Up['y1'], Up['y1'] + 0.25)
    y_pd = Up['y1'] + 0.25
    sq('pedestal', Pd['w'], y_pd, Pd['y1'])
    bm = bmesh.new(); h = Sp['w'] / 2
    base = [bm.verts.new(B(cx + a * h, Pd['y1'], cz + c * h)) for a, c in [(-1, -1), (1, -1), (1, 1), (-1, 1)]]
    apex = bm.verts.new(B(cx, Sp['y1'], cz))
    for i in range(4): bm.faces.new((base[i], base[(i + 1) % 4], apex))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces); finish('remate', bm, GREY_M())
    box('cruz', cx - 0.06, cx + 0.06, cz - 0.06, cz + 0.06, Sp['y1'], T['top'], DARK_M())
    # the arches: two a face in the belfry, one in the upper stage; dark recesses for now
    def arches(tag, w, y1, n, aw, ah, below):
        for face in range(4):
            for k in ([-w / 4, w / 4] if n == 2 else [0.0]):
                y0 = y1 - below - ah
                ax, az, nx = {0: (cx + w / 2, cz + k, 1), 1: (cx - w / 2, cz + k, 1), 2: (cx + k, cz + w / 2, 0), 3: (cx + k, cz - w / 2, 0)}[face]
                if nx: box(f'{tag}_{face}_{k}', ax - 0.07, ax + 0.07, az - aw / 2, az + aw / 2, y0, y0 + ah, DARK_M())
                else: box(f'{tag}_{face}_{k}', ax - aw / 2, ax + aw / 2, az - 0.07, az + 0.07, y0, y0 + ah, DARK_M())
    arches('arco', Bf['w'], Bf['y1'], 2, *Bf['arch'], 0.8)
    arches('arco_alto', Up['w'], Up['y1'], 1, *Up['arch'], 0.7)
    # the north-west turret
    Tu = SPEC['turret']; box('torreon', Tu['x0'], Tu['x1'], Tu['z0'], Tu['z1'], H, Tu['top'], GREY_M())
    # the buttresses: flat bands on both long walls (the last one runs on to the apse; on the south, above the
    # sacristy's roof), and a metre behind the cornice the heads of the walls between the chapels
    Bt = SPEC['butt']; Hd = Bt['head']; wa, wb = SPEC['walls']
    for k, x in enumerate(Bt['xs']):
        last = k == len(Bt['xs']) - 1
        x0, x1 = x - Bt['w'] / 2, (wb if last else x + Bt['w'] / 2)
        box(f'contrafuerte_n{k}', x0, x1, zn - Bt['out'], zn, 0, H, GREY_M())
        ys = SPEC['sacristy'] if x1 > RING[33][0] else 0
        zs0, zs1 = south_wall_z(x0), south_wall_z(x1)
        box(f'contrafuerte_s{k}', x0, x1, min(zs0, zs1), max(zs0, zs1) + Bt['out'], ys, H, GREY_M())
        for side, za, zb in (('n', zn + Hd['back'], -Hd['to']), ('s', Hd['to'], south_wall_z(x) - Hd['back'])):
            box(f'cabeza_{side}{k}', x - Hd['w'] / 2, x + Hd['w'] / 2, za, zb, H, Hd['top'], GREY_M())
    # the windows, one a bay on each side (on the south, the last one looks over the sacristy's roof), and the oculi:
    # dark recesses
    W = SPEC['window']
    for k, (x, y0) in enumerate(zip(W['xs'], W['sills'])):
        box(f'ventana_n{k}', x - W['w'] / 2, x + W['w'] / 2, zn - 0.03, zn + 0.02, y0, y0 + W['h'], DARK_M())
        zs = south_wall_z(x)
        box(f'ventana_s{k}', x - W['w'] / 2, x + W['w'] / 2, zs - 0.02, zs + 0.03, y0, y0 + W['h'], DARK_M())
    for name in ('oculus', 'oculus2'):
        O = SPEC[name]
        bpy.ops.mesh.primitive_cylinder_add(vertices=48, radius=O['r'], depth=0.1, location=B(west_x(O['z']) - 0.03, O['y'], O['z']), rotation=(0, math.pi / 2, 0))
        oc = bpy.context.object; oc.name = name; oc.data.materials.append(DARK_M())

# ================================================================ phase 2: the detail (docs/hiperrealismo.md, «Detalle»)
# Every piece on the table's measures, in the materials it will wear (phase 3 gives them their textures: the UVs are
# already in metres over each material's tile). Openings are real: booleans cut the windows, the oculi and the doors'
# pockets out of the walls, so the portals' reveals, doors and vestibules (churchdoors.js) show inside them.
ROLE = {  # role: (colour, roughness, metres per texture tile)
    'mamposteria': ((0.34, 0.25, 0.15), 0.93, 6.0),
    'mamposteria_pies': ((0.34, 0.25, 0.15), 0.93, 6.0),   # (the west front: the same stone, fewer dark ones — the photo's sunlit front)
    'silleria': ((0.56, 0.44, 0.29), 0.86, 3.0),
    'zocalo': ((0.36, 0.29, 0.20), 0.9, 3.0),
    'teja': ((0.40, 0.18, 0.10), 0.82, 2.5),
    'hueco': ((0.010, 0.009, 0.008), 1.0, 1.0),
    'vidrio': ((0.018, 0.022, 0.026), 0.12, 1.0),
    'hierro': ((0.025, 0.025, 0.025), 0.55, 1.0),
    'bronce': ((0.28, 0.17, 0.07), 0.45, 1.0),
    'nido': ((0.13, 0.09, 0.05), 1.0, 1.0),
}
TEXTURED = {'mamposteria': 'mamposteria', 'mamposteria_pies': 'mamposteria_pies', 'silleria': 'silleria', 'zocalo': 'silleria', 'teja': 'teja'}  # (.cache/hq/tex)
def R_(role):
    """the role's material: its colour and roughness, and from phase 3 its textures (tools/blender/texturas.py), over
    the UVs, which are in metres over the tile; the plinth wears the ashlar's, darkened"""
    new = role not in MATS
    m = mat(role, ROLE[role][0], ROLE[role][1])
    TILE[role] = ROLE[role][2]
    if not new: return m
    p = m.node_tree.nodes['Principled BSDF']
    if role in ('hierro', 'bronce'): p.inputs['Metallic'].default_value = 1.0
    if role in TEXTURED and not GREY:
        nt = m.node_tree; tex = TEXTURED[role]
        def img(kind, color):
            n = nt.nodes.new('ShaderNodeTexImage'); n.image = bpy.data.images.load(os.path.join(ROOT, '.cache', 'hq', 'tex', f'{tex}_{kind}.jpg'), check_existing=True)
            if not color: n.image.colorspace_settings.name = 'Non-Color'
            return n
        d = img('diff', True)
        if role == 'zocalo':
            mix = nt.nodes.new('ShaderNodeMix'); mix.data_type = 'RGBA'; mix.blend_type = 'MULTIPLY'; mix.inputs['Factor'].default_value = 1.0
            mix.inputs['B'].default_value = (0.62, 0.58, 0.55, 1)
            nt.links.new(d.outputs['Color'], mix.inputs['A']); nt.links.new(mix.outputs['Result'], p.inputs['Base Color'])
        else: nt.links.new(d.outputs['Color'], p.inputs['Base Color'])
        r = img('rough', False); nt.links.new(r.outputs['Color'], p.inputs['Roughness'])
        nm = nt.nodes.new('ShaderNodeNormalMap'); nt.links.new(img('nor', False).outputs['Color'], nm.inputs['Color']); nt.links.new(nm.outputs['Normal'], p.inputs['Normal'])
    return m

def link_bm(name, bm, role):
    """a mesh object from a bmesh, in a role's material (UVs set later, for every piece at once)"""
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    me = bpy.data.meshes.new(name); bm.to_mesh(me); bm.free()
    ob = bpy.data.objects.new(name, me); COL.objects.link(ob); me.materials.append(R_(role))
    return ob

def solid(name, pts, y0, y1, role):
    bm = bmesh.new()
    lo = [bm.verts.new(B(x, y0, z)) for x, z in pts]; hi = [bm.verts.new(B(x, y1, z)) for x, z in pts]
    n = len(pts)
    for i in range(n): bm.faces.new((lo[i], lo[(i + 1) % n], hi[(i + 1) % n], hi[i]))
    bm.faces.new(hi); bm.faces.new(list(reversed(lo)))
    return link_bm(name, bm, role)

def cube(name, x0, x1, z0, z1, y0, y1, role):
    return solid(name, [(x0, z0), (x1, z0), (x1, z1), (x0, z1)], y0, y1, role)

def obox(name, cx, cz, nx, nz, along, across, y0, y1, role, out0=0.0):
    """a box on a wall at (cx, cz) whose outward normal is (nx, nz): `along` wide along the wall, from out0 to
    out0 + across out of it"""
    tx, tz = -nz, nx
    pts = [(cx + tx * s + nx * o, cz + tz * s + nz * o) for s, o in ((-along / 2, out0), (along / 2, out0), (along / 2, out0 + across), (-along / 2, out0 + across))]
    return solid(name, pts, y0, y1, role)

def offset(pts, d):
    """a closed outline moved d outward, its corners mitred (sharp ones cut short)"""
    s = 1 if poly_area(pts) > 0 else -1
    n = len(pts); out = []
    for i in range(n):
        p0, p1, p2 = pts[i - 1], pts[i], pts[(i + 1) % n]
        e0 = (p1[0] - p0[0], p1[1] - p0[1]); e1 = (p2[0] - p1[0], p2[1] - p1[1])
        l0, l1 = math.hypot(*e0) or 1e-9, math.hypot(*e1) or 1e-9
        n0 = (e0[1] / l0 * s, -e0[0] / l0 * s); n1 = (e1[1] / l1 * s, -e1[0] / l1 * s)
        bx, bz = n0[0] + n1[0], n0[1] + n1[1]; bl = math.hypot(bx, bz)
        if bl < 1e-6: out.append((p1[0] + n0[0] * d, p1[1] + n0[1] * d)); continue
        bx, bz = bx / bl, bz / bl
        k = d / max(bx * n0[0] + bz * n0[1], 0.4)
        out.append((p1[0] + bx * k, p1[1] + bz * k))
    return out

def clean(pts, jog):
    """the outline without its little jogs (edges shorter than `jog` merged into their midpoints): for mouldings, which
    would fold back on themselves at a jog smaller than their projection"""
    pts = list(pts)
    while len(pts) > 4:
        n = len(pts); i = min(range(n), key=lambda k: math.dist(pts[k], pts[(k + 1) % n]))
        if math.dist(pts[i], pts[(i + 1) % n]) >= jog: break
        a, b = pts[i], pts[(i + 1) % n]
        pts[i] = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2); del pts[(i + 1) % n]
    return pts

def sweep(name, pts, profile, role, top=True):
    """a moulding round a closed outline: for each (d, y) of the profile, the outline moved d outward at height y"""
    bm = bmesh.new()
    rings = [[bm.verts.new(B(x, y, z)) for x, z in offset(pts, d)] for d, y in profile]
    n = len(pts)
    for a, b in zip(rings, rings[1:]):
        for i in range(n):
            j = (i + 1) % n
            try: bm.faces.new((a[i], a[j], b[j], b[i]))
            except ValueError: pass
    if top: bm.faces.new(rings[-1])
    return link_bm(name, bm, role)

def arch_pts(w, h, seg=16):
    """a round-arched opening's outline: w wide, h to the crown, from its sill (u across, v up)"""
    r = w / 2
    return [(-r, 0.0), (r, 0.0)] + [(r * math.cos(math.pi * k / seg), h - r + r * math.sin(math.pi * k / seg)) for k in range(seg + 1)]

def wall_prism(name, shape, cx, cz, nx, nz, y0, d0, d1, role):
    """a 2D shape (u along the wall, v up) on a wall at (cx, cz) with outward normal (nx, nz), from d0 to d1 outward"""
    tx, tz = -nz, nx
    bm = bmesh.new()
    a = [bm.verts.new(B(cx + tx * u + nx * d0, y0 + v, cz + tz * u + nz * d0)) for u, v in shape]
    b = [bm.verts.new(B(cx + tx * u + nx * d1, y0 + v, cz + tz * u + nz * d1)) for u, v in shape]
    n = len(shape)
    for i in range(n): bm.faces.new((a[i], a[(i + 1) % n], b[(i + 1) % n], b[i]))
    bm.faces.new(a); bm.faces.new(list(reversed(b)))
    return link_bm(name, bm, role)

def cut(target, *cutters):
    for c in cutters:
        m = target.modifiers.new('hueco', 'BOOLEAN'); m.operation = 'DIFFERENCE'; m.solver = 'EXACT'; m.object = c
        bpy.context.view_layer.objects.active = target; bpy.ops.object.modifier_apply(modifier=m.name)
        bpy.data.objects.remove(c)
    return target

def lathe_wall(name, cx, y, cz, nx, nz, profile, role, seg=64):
    """a ring moulding on a wall, round the axis through (cx, y, cz) along the outward normal: profile [(r, d), ...]"""
    tx, tz = -nz, nx
    bm = bmesh.new(); rings = []
    for r, d in profile:
        rings.append([bm.verts.new(B(cx + tx * r * math.cos(a) + nx * d, y + r * math.sin(a), cz + tz * r * math.cos(a) + nz * d))
                      for a in [2 * math.pi * k / seg for k in range(seg)]])
    for a, b in zip(rings, rings[1:]):
        for k in range(seg): bm.faces.new((a[k], a[(k + 1) % seg], b[(k + 1) % seg], b[k]))
    return link_bm(name, bm, role)

def disc(name, cx, y, cz, nx, nz, r, d0, d1, role, seg=48):
    return wall_prism(name, [(r * math.cos(2 * math.pi * k / seg), r * math.sin(2 * math.pi * k / seg)) for k in range(seg)], cx, cz, nx, nz, y, d0, d1, role)

def ball(name, x, y, z, r, role):
    bm = bmesh.new(); bmesh.ops.create_uvsphere(bm, u_segments=16, v_segments=10, radius=r)
    for v in bm.verts: v.co += Vector(B(x, y, z))
    return link_bm(name, bm, role)

def gable_cap(name, cx, cz, nx, nz, along, across, y0, rise, role, out0=-0.2):
    """a little gabled roof on a buttress: its ridge runs outward (along the normal), its slopes fall along the wall"""
    tx, tz = -nz, nx
    bm = bmesh.new()
    P = lambda s, o, y: bm.verts.new(B(cx + tx * s + nx * o, y, cz + tz * s + nz * o))
    a0, a1 = P(-along / 2, out0, y0), P(along / 2, out0, y0)
    b0, b1 = P(-along / 2, across, y0), P(along / 2, across, y0)
    r0, r1 = P(0, out0, y0 + rise), P(0, across, y0 + rise)
    bm.faces.new((a0, b0, r1, r0)); bm.faces.new((b1, a1, r0, r1)); bm.faces.new((a0, r0, a1)); bm.faces.new((b0, b1, r1))
    return link_bm(name, bm, role)

def bell(name, x, y, z, h, role):
    """a church bell: its profile turned round (crown at the top), mouth down at y"""
    prof = [(0.0, h * 1.0), (0.18 * h, h * 1.0), (0.3 * h, 0.92 * h), (0.34 * h, 0.7 * h), (0.38 * h, 0.4 * h), (0.5 * h, 0.12 * h), (0.6 * h, 0.0), (0.5 * h, 0.03 * h), (0.0, 0.25 * h)]
    bm = bmesh.new(); seg = 20; rings = []
    for r, v in prof: rings.append([bm.verts.new(B(x + r * math.cos(2 * math.pi * k / seg), y + v, z + r * math.sin(2 * math.pi * k / seg))) for k in range(seg)])
    for a, b in zip(rings, rings[1:]):
        for k in range(seg): bm.faces.new((a[k], a[(k + 1) % seg], b[(k + 1) % seg], b[k]))
    return link_bm(name, bm, role)

def nest(name, x, y, z, r, role):
    """a stork's nest: a low ragged drum of sticks"""
    bm = bmesh.new(); seg = 14
    import random; rnd = random.Random(int(abs(x * 100 + z * 10)))
    rings = []
    for (rr, yy) in ((r * 0.75, 0.0), (r * 1.05, 0.35 * r), (r * 0.95, 0.62 * r), (r * 0.55, 0.5 * r)):
        rings.append([bm.verts.new(B(x + rr * (1 + rnd.uniform(-0.12, 0.12)) * math.cos(2 * math.pi * k / seg), y + yy + rnd.uniform(-0.05, 0.05), z + rr * (1 + rnd.uniform(-0.12, 0.12)) * math.sin(2 * math.pi * k / seg))) for k in range(seg)])
    for a, b in zip(rings, rings[1:]):
        for k in range(seg): bm.faces.new((a[k], a[(k + 1) % seg], b[(k + 1) % seg], b[k]))
    bm.faces.new(list(reversed(rings[0]))); bm.faces.new(rings[-1])
    return link_bm(name, bm, role)

def reuv(ob):
    """UVs in metres over the face's material's tile, each face from the side it faces most (box projection), in the
    frame's own axes so the courses run level"""
    me = ob.data; tiles = [TILE.get(m.name, 2.0) if m else 2.0 for m in me.materials] or [2.0]
    bm = bmesh.new(); bm.from_mesh(me)
    uv = bm.loops.layers.uv.verify(); bm.normal_update()
    for f in bm.faces:
        n = f.normal; t = tiles[f.material_index] if f.material_index < len(tiles) else tiles[0] # (each face its own material's tile)
        for l in f.loops:
            p = l.vert.co
            if abs(n.z) > max(abs(n.x), abs(n.y)): l[uv].uv = (p.x / t, p.y / t)
            elif abs(n.x) > abs(n.y): l[uv].uv = (p.y / t, p.z / t)
            else: l[uv].uv = (p.x / t, p.z / t)
    bm.to_mesh(me); bm.free()

def build_detail():
    H = SPEC['cornice']; C0 = H - 0.75  # (the cornice moulding: 0,75 m under the top)
    wa, wb = SPEC['walls']; Bt = SPEC['butt']; Hd = Bt['head']; W = SPEC['window']
    main, sac = outline()
    if poly_area(sac) < 0: sac = sac[::-1]
    zn = RING[7][1]
    def south_n(x):
        """the south wall's outward normal (it runs 1,6° off the axis)"""
        (xa, za), (xb, zb) = SW, RING[33]; dx, dz = xb - xa, zb - za; l = math.hypot(dx, dz)
        return (-dz / l, dx / l)
    # ---- the walls: rubble masonry up to the cornice; the plinth and the cornice swept round them in ashlar
    nave = solid('nave', main, 0, C0, 'mamposteria')
    sweep('zocalo', main, [(0.12, 0.0), (0.12, 0.88), (0.04, 0.96), (0.0, 1.0)], 'zocalo', top=False)
    sweep('cornisa', clean(main, 0.8), [(-0.05, C0), (0.08, C0), (0.08, C0 + 0.16), (0.2, C0 + 0.28), (0.32, C0 + 0.46), (0.45, C0 + 0.52), (0.45, H), (-0.3, H)], 'silleria')
    # ---- the openings: the windows, the doors' pockets (the arch of each door and, behind, the room its vestibule
    # stands in: churchdoors.js), the oculi
    win = []
    for k, (x, y0) in enumerate(zip(W['xs'], W['sills'])):
        win.append((f'n{k}', x, zn, 0.0, -1.0, y0))
        win.append((f's{k}', x, south_wall_z(x), *south_n(x), y0))
    # (the openings' cuts leave their own faces: stone where the stone shows — the windows' reveals down to the glass,
    # the oculi's, the belfry's arches —, the black «hueco» only where it is dark: the doors' pockets and the slits.
    # Cut in black, the reveals stayed black whatever the light: Unity's comparison and the reviewer, 2026-10-11)
    cutters = [wall_prism('c', arch_pts(W['w'], W['h']), x, z, nx, nz, y0, 0.3, -1.0, 'silleria') for tag, x, z, nx, nz, y0 in win]
    X0w = FRAME['x0']; xs = FRAME['xs']
    kw = SPEC['west_portal']['scale']
    doors = [('oeste', X0w, 0.0, -1.0, 0.0, 2.6 * kw, 3.7 * kw, 0.65 * kw, 1.85 * kw), ('sur', xs, south_wall_z(xs), *south_n(xs), 2.3, 3.3, 0.6, 2.4), ('norte', xs, zn, 0.0, -1.0, 2.2, 3.2, 0.4, 0.0)]
    for tag, x, z, nx, nz, w, sp, z0, dep in doors:
        cutters.append(wall_prism('c', arch_pts(w, sp + w / 2), x, z, nx, nz, 0.0, 0.3, -(z0 + 0.25), 'hueco'))
        if dep > 0:
            Wv, Hv = w + 0.8, sp + w / 2 + 0.4
            cutters.append(wall_prism('c', [(-Wv / 2, 0), (Wv / 2, 0), (Wv / 2, Hv), (-Wv / 2, Hv)], x, z, nx, nz, 0.0, -(z0 - 0.05), -(z0 + dep + 0.2), 'hueco'))
    O1, O2 = SPEC['oculus'], SPEC['oculus2']
    for O, r_in in ((O1, 1.72), (O2, 0.72)):
        cutters.append(disc('c', west_x(O['z']), O['y'], O['z'], -1.0, 0.0, r_in, 0.3, -1.0, 'silleria'))
    cut(nave, *cutters)
    # ---- the windows: surround, sill, the relief under it, glass and bars at the back of the reveal
    for tag, x, z, nx, nz, y0 in win:
        fr = wall_prism(f'recercado_{tag}', arch_pts(W['w'] + 0.56, W['h'] + 0.28), x, z, nx, nz, y0 - 0.02, -0.02, 0.07, 'silleria')
        cut(fr, wall_prism('c', arch_pts(W['w'], W['h']), x, z, nx, nz, y0, 0.3, -0.3, 'silleria'))
        wall_prism(f'alfeizar_{tag}', [(-(W['w'] + 0.7) / 2, 0), ((W['w'] + 0.7) / 2, 0), ((W['w'] + 0.7) / 2, 0.16), (-(W['w'] + 0.7) / 2, 0.16)], x, z, nx, nz, y0 - 0.16, -0.05, 0.16, 'silleria')
        # the cartouche under the sill: a moulded frame and an oval boss
        fr2 = wall_prism(f'cartela_{tag}', [(-0.58, 0), (0.58, 0), (0.58, 0.64), (-0.58, 0.64)], x, z, nx, nz, y0 - 0.86, -0.02, 0.05, 'silleria')
        # (its sunk panel is carved stone: cut with the «hueco» of the openings, its sides came out black — a slot round
        # the boss, which Unity's baked light, 2026-10-11, showed as the stone it is)
        # (and its floor stops 2 cm short of the wall: on the wall's own plane the two faces lay one on the other, and
        # the bake gave it no light at all)
        cut(fr2, wall_prism('c', [(-0.44, 0), (0.44, 0), (0.44, 0.42), (-0.44, 0.42)], x, z, nx, nz, y0 - 0.75, 0.2, 0.02, 'silleria'))
        wall_prism(f'cartela_ovalo_{tag}', [(0.3 * math.cos(2 * math.pi * k / 24), 0.13 * math.sin(2 * math.pi * k / 24) + 0.21) for k in range(24)], x, z, nx, nz, y0 - 0.75, -0.02, 0.08, 'silleria')
        wall_prism(f'vidrio_{tag}', arch_pts(W['w'], W['h']), x, z, nx, nz, y0, -0.82, -0.85, 'vidrio')
        # the tracery: a stone mullion, and over it a plate under the arch pierced by two small arches and a round eye
        ys = W['h'] - 1.2
        wall_prism(f'parteluz_{tag}', [(-0.07, 0), (0.07, 0), (0.07, ys), (-0.07, ys)], x, z, nx, nz, y0, -0.42, -0.6, 'silleria')
        tym = wall_prism(f'traceria_{tag}', arch_pts(W['w'] + 0.02, 1.2), x, z, nx, nz, y0 + ys, -0.42, -0.6, 'silleria')
        cut(tym, wall_prism('c', [(u - 0.35, v) for u, v in arch_pts(0.56, 0.63)], x, z, nx, nz, y0 + ys - 0.01, 0.3, -1.0, 'silleria'),
            wall_prism('c', [(u + 0.35, v) for u, v in arch_pts(0.56, 0.63)], x, z, nx, nz, y0 + ys - 0.01, 0.3, -1.0, 'silleria'),
            wall_prism('c', [(0.14 * math.cos(2 * math.pi * k / 20), 0.14 * math.sin(2 * math.pi * k / 20) + 0.86) for k in range(20)], x, z, nx, nz, y0 + ys, 0.3, -1.0, 'silleria'))
    # ---- the oculi: the great one with four moulded rings and a wheel; the small one with two rings
    xo = west_x(O1['z']); yo, zo = O1['y'], O1['z']
    lathe_wall('oculo_anillo1', xo, yo, zo, -1, 0, [(2.32, 0.0), (2.32, 0.12), (2.24, 0.2), (2.12, 0.2), (2.05, 0.1)], 'silleria')
    lathe_wall('oculo_anillo2', xo, yo, zo, -1, 0, [(2.05, 0.1), (1.98, 0.02), (1.96, -0.1), (1.9, -0.1)], 'silleria')
    lathe_wall('oculo_anillo3', xo, yo, zo, -1, 0, [(1.9, -0.1), (1.86, -0.05), (1.8, -0.05), (1.76, -0.22)], 'silleria')
    lathe_wall('oculo_anillo4', xo, yo, zo, -1, 0, [(1.76, -0.22), (1.73, -0.18), (1.72, -0.3), (1.72, -1.0)], 'silleria')
    for k in range(30):  # the ring of balls just inside the mouldings
        a = 2 * math.pi * (k + 0.5) / 30
        ball('oculo_bola', xo + 0.3, yo + 1.62 * math.sin(a), zo - 1.62 * math.cos(a), 0.075, 'silleria')
    lathe_wall('oculo_lecho_bolas', xo, yo, zo, -1, 0, [(1.72, -0.36), (1.52, -0.36), (1.52, -0.42)], 'silleria')
    for k in range(-11, 12):  # the lattice: thin upright bars across the opening
        u = k * 0.135; hh = math.sqrt(max(1.53 ** 2 - u * u, 0.0))
        if hh < 0.1: continue
        wall_prism('oculo_reja', [(u - 0.018, -hh), (u + 0.018, -hh), (u + 0.018, hh), (u - 0.018, hh)], xo, zo, -1, 0, yo, -0.5, -0.55, 'hierro')
    lathe_wall('oculo_reja_aro', xo, yo, zo, -1, 0, [(1.56, -0.48), (1.5, -0.48), (1.5, -0.57), (1.56, -0.57)], 'hierro')
    disc('oculo_vidrio', xo, yo, zo, -1, 0, 1.75, -0.85, -0.88, 'vidrio')
    xo2 = west_x(O2['z'])
    lathe_wall('oculo2_anillo1', xo2, O2['y'], O2['z'], -1, 0, [(1.02, 0.0), (1.02, 0.1), (0.95, 0.16), (0.86, 0.16), (0.8, 0.05)], 'silleria')
    lathe_wall('oculo2_anillo2', xo2, O2['y'], O2['z'], -1, 0, [(0.8, 0.05), (0.76, -0.05), (0.72, -0.12), (0.72, -1.0)], 'silleria')
    disc('oculo2_vidrio', xo2, O2['y'], O2['z'], -1, 0, 0.74, -0.7, -0.73, 'vidrio')
    # ---- the buttresses: flat bands of ashlar (the cornice runs over them; the last one on to the apse; on the south,
    # above the sacristy's roof); a metre behind the cornice the heads of the walls between the chapels, rubble with an
    # ashlar coping and a tiled gable; gargoyles over each window
    for k, x in enumerate(Bt['xs']):
        last = k == len(Bt['xs']) - 1
        x0, x1 = x - Bt['w'] / 2, (wb if last else x + Bt['w'] / 2)
        xm, wl = (x0 + x1) / 2, x1 - x0
        for side, z, nx, nz, y0 in (('n', zn, 0.0, -1.0, 0.0), ('s', south_wall_z(xm), *south_n(xm), SPEC['sacristy'] if x1 > RING[33][0] else 0.0)):
            obox(f'contrafuerte_{side}{k}', xm, z, nx, nz, wl, Bt['out'] + 0.05, y0, C0, 'silleria', out0=-0.05)
            if y0 == 0: obox(f'contrafuerte_zocalo_{side}{k}', xm, z, nx, nz, wl + 0.2, Bt['out'] + 0.17, 0, 1.0, 'zocalo', out0=-0.05)
        for side, z_out, sgn in (('n', zn, 1), ('s', south_wall_z(x), -1)):
            za = z_out + sgn * Hd['back']; zb = -sgn * Hd['to']
            z0, z1 = min(za, zb), max(za, zb)
            cube(f'cabeza_{side}{k}', x - Hd['w'] / 2, x + Hd['w'] / 2, z0, z1, H - 0.3, Hd['top'] - 0.5, 'mamposteria')
            cube(f'cabeza_albardilla_{side}{k}', x - Hd['w'] / 2 - 0.08, x + Hd['w'] / 2 + 0.08, z0 - 0.08, z1 + 0.08, Hd['top'] - 0.5, Hd['top'] - 0.35, 'silleria')
            # the tiled gable along the head, its ridge running across the wall
            gable_cap(f'cabeza_remate_{side}{k}', x, (z0 + z1) / 2, 0.0, 1.0, Hd['w'] + 0.3, (z1 - z0) / 2 + 0.15, Hd['top'] - 0.35, 0.45, 'teja', out0=-((z1 - z0) / 2 + 0.15))
    Gg = SPEC['gargoyles']; yg = Gg['y']
    garg = []
    for k in range(Gg['n']):
        x = Gg['x0'] + k * Gg['step']
        on_band = any(abs(x - bx) < Bt['w'] / 2 + 0.2 for bx in Bt['xs'])   # (on a buttress band: out of its face)
        off = Bt['out'] if on_band else 0.0
        garg.append((f'n{k}', x, zn, 0.0, -1.0, off)); garg.append((f's{k}', x, south_wall_z(x), *south_n(x), off))
    for tag, x, z, nx, nz, off in garg:
        z = z + nz * off; x = x + nx * off
        obox(f'gargola_base_{tag}', x, z, nx, nz, 0.36, 0.32, yg - 0.2, yg + 0.2, 'silleria')
        bm = bmesh.new()
        bmesh.ops.create_cone(bm, cap_ends=True, segments=12, radius1=0.13, radius2=0.11, depth=1.1)
        rot = Vector((nx, -nz, 0)).to_track_quat('Z', 'Y').to_matrix().to_4x4()
        for v in bm.verts: v.co = rot @ v.co
        for v in bm.verts: v.co += Vector(B(x + nx * 0.7, yg, z + nz * 0.7))
        link_bm(f'gargola_{tag}', bm, 'silleria')
    # ---- the quoins: big ashlar at the outer corners, long and short in turn, a little proud of the rubble
    sgn = 1 if poly_area(main) > 0 else -1
    def quoin(i):
        p, a, c = main[i], main[i - 1], main[(i + 1) % len(main)]
        for j, q in enumerate((a, c)):
            dx, dz = q[0] - p[0], q[1] - p[1]; l = math.hypot(dx, dz); dx, dz = dx / l, dz / l
            e = (q[0] - p[0], q[1] - p[1]) if j == 1 else (p[0] - q[0], p[1] - q[1]); el = math.hypot(*e)
            nx, nz = e[1] / el * sgn, -e[0] / el * sgn
            for k in range(int((C0 - 1.0) / 0.45)):
                y0 = 1.0 + 0.45 * k; L = min(0.72 if (k + j) % 2 == 0 else 0.42, l * 0.45)
                solid('esquina', [(p[0], p[1]), (p[0] + dx * L, p[1] + dz * L), (p[0] + dx * L + nx * 0.035, p[1] + dz * L + nz * 0.035), (p[0] + nx * 0.035, p[1] + nz * 0.035)], y0, y0 + 0.43, 'silleria')
    for i in (0, 1, 8):  # the tower's SW and NW corners, the north wall's east end (the NW corners wear whole bands)
        quoin(i)
    # ---- the north-west block (its stair): the ashlar bands, its four slits, its four small windows
    NB = SPEC['nw_block']; bw2 = NB['band']
    (ax, az), (bx, bz) = RING[5], RING[4]                          # the block's west face, from its corner
    fl = math.hypot(bx - ax, bz - az); fx, fz = (bx - ax) / fl, (bz - az) / fl
    band_w = obox('banda_esquina', ax + fx * bw2 / 2, az + fz * bw2 / 2, -fz, fx, bw2, 0.04, 1.0, C0, 'silleria', out0=0.0)
    band_s = obox('banda_escalon', -20.69, (RING[6][1] + RING[7][1]) / 2, -1.0, 0.0, abs(RING[6][1] - RING[7][1]) + 0.02, 0.04, 1.0, C0, 'silleria', out0=0.0)
    obox('banda_muro_n', RING[7][0] + bw2 / 2, zn, 0.0, -1.0, bw2, 0.04, 1.0, C0, 'silleria', out0=0.0)
    slit = lambda: [(-0.08, 0), (0.08, 0), (0.08, 0.9), (-0.08, 0.9)]
    zsl = NB['slits']['z']; xsl = ax + (bx - ax) * (zsl - az) / (bz - az)
    for k, yc in enumerate(NB['slits']['ys']):
        for target in (nave, band_w):
            cut(target, wall_prism('c', slit(), xsl, zsl, -1.0, 0.0, yc - 0.45, 0.4, -0.7, 'hueco'))
    nfz = lambda x: RING[5][1] + (RING[6][1] - RING[5][1]) * (x - RING[5][0]) / (RING[6][0] - RING[5][0])
    for k, (xw2, yw) in enumerate(NB['windows']):
        zw = nfz(xw2)
        cut(nave, wall_prism('c', [(-0.3, 0), (0.3, 0), (0.3, 0.9), (-0.3, 0.9)], xw2, zw, 0.0, -1.0, yw - 0.45, 0.3, -0.6, 'silleria'))
        frw = wall_prism(f'ventanita_{k}', [(-0.48, 0), (0.48, 0), (0.48, 1.2), (-0.48, 1.2)], xw2, zw, 0.0, -1.0, yw - 0.6, -0.02, 0.05, 'silleria')
        cut(frw, wall_prism('c', [(-0.3, 0), (0.3, 0), (0.3, 0.9), (-0.3, 0.9)], xw2, zw, 0.0, -1.0, yw - 0.45, 0.3, -0.3, 'silleria'))
        wall_prism(f'ventanita_vidrio_{k}', [(-0.3, 0), (0.3, 0), (0.3, 0.9), (-0.3, 0.9)], xw2, zw, 0.0, -1.0, yw - 0.45, -0.5, -0.52, 'vidrio')
    # ---- the west front wears the masonry's variant with few dark stones (the photo's sunlit front: 3–5 %)
    # (its own slot: the booleans have already added others to the wall — the openings' 'hueco')
    nave.data.materials.append(R_('mamposteria_pies')); pies = len(nave.data.materials) - 1
    for f in nave.data.polygons:
        if f.normal.x < -0.85 and f.center.x < -20.0 and f.material_index == 0: f.material_index = pies
    # ---- on the tower's west face (x −26,34): a row of corbels at ≈8,6 m and a loophole, as the photo shows them
    xt = SPEC['tower']['x0']
    for k in range(12):
        zc = 6.5 + k * 0.48
        cube('canecillo', xt - 0.32, xt + 0.02, zc - 0.11, zc + 0.11, 8.45, 8.75, 'silleria')
    cut(nave, wall_prism('c', [(-0.13, 0), (0.13, 0), (0.13, 0.9), (-0.13, 0.9)], xt, 9.9, -1.0, 0.0, 9.95, 0.3, -0.6, 'hueco'))
    wall_prism('saetera', [(-0.3, 0), (0.3, 0), (0.3, 1.3), (-0.3, 1.3)], xt, 9.9, -1.0, 0.0, 9.75, -0.02, 0.05, 'silleria')
    cut(bpy.data.objects['saetera'], wall_prism('c', [(-0.13, 0), (0.13, 0), (0.13, 0.9), (-0.13, 0.9)], xt, 9.9, -1.0, 0.0, 9.95, 0.3, -0.3, 'hueco'))
    # ---- the tower above the cornice, on its own axis: the belfry and the upper stage (hollow, open, pilasters,
    # cornice, balls), the pedestal, the pyramid, the ball, the cross and the vane
    T = SPEC['tower']; cx, cz = T['c']
    Bf, Up, Pd, Sp = T['belfry'], T['upper'], T['pedestal'], T['spire']
    def stage(tag, w, y0, y1, n_arch, aw, ah, below, wall, ball_r):
        ay = y1 - below - ah - y0
        outer = cube(f'{tag}', cx - w / 2, cx + w / 2, cz - w / 2, cz + w / 2, y0, y1, 'silleria')
        imp = cube(f'{tag}_imposta', cx - w / 2 - 0.1, cx + w / 2 + 0.1, cz - w / 2 - 0.1, cz + w / 2 + 0.1, y0 + ay + ah - aw / 2 - 0.1, y0 + ay + ah - aw / 2 + 0.05, 'silleria')
        offs = [0.0] if n_arch == 1 else [-w / 4, w / 4]
        def arches():
            out = []
            for o in offs:
                for nx, nz in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    tx, tz = -nz, nx
                    out.append(wall_prism('c', arch_pts(aw, ah), cx + nx * w / 2 + tx * o, cz + nz * w / 2 + tz * o, nx, nz, y0 + ay, 0.5, -wall - 0.3, 'silleria'))
            return out
        cut(outer, cube('c', cx - w / 2 + wall, cx + w / 2 - wall, cz - w / 2 + wall, cz + w / 2 - wall, y0 + 0.4, y1 + 1, 'silleria'), *arches())
        cut(imp, cube('c', cx - w / 2 + wall, cx + w / 2 - wall, cz - w / 2 + wall, cz + w / 2 - wall, y0, y1, 'silleria'), *arches())  # (round the piers, not across the arches)
        pw = min(0.6, w * 0.13)
        for sx in (-1, 1):
            for sz in (-1, 1):
                cube(f'{tag}_pilastra', cx + sx * (w / 2 - pw / 2) - pw / 2 - 0.04 * sx, cx + sx * (w / 2 - pw / 2) + pw / 2 - 0.04 * sx, cz + sz * (w / 2 - pw / 2) - pw / 2 - 0.04 * sz, cz + sz * (w / 2 - pw / 2) + pw / 2 - 0.04 * sz, y0, y1, 'silleria')
        cube(f'{tag}_cornisa', cx - w / 2 - 0.3, cx + w / 2 + 0.3, cz - w / 2 - 0.3, cz + w / 2 + 0.3, y1, y1 + 0.15, 'silleria')
        cube(f'{tag}_cornisa2', cx - w / 2 - 0.15, cx + w / 2 + 0.15, cz - w / 2 - 0.15, cz + w / 2 + 0.15, y1 + 0.15, y1 + 0.25, 'silleria')
        for sx in (-1, 1):
            for sz in (-1, 1):
                cube(f'{tag}_pedestal', cx + sx * (w / 2) - ball_r * 0.8, cx + sx * (w / 2) + ball_r * 0.8, cz + sz * (w / 2) - ball_r * 0.8, cz + sz * (w / 2) + ball_r * 0.8, y1 + 0.25, y1 + 0.25 + ball_r * 1.1, 'silleria')
                ball(f'{tag}_bola', cx + sx * (w / 2), y1 + 0.25 + ball_r * 2.1, cz + sz * (w / 2), ball_r, 'silleria')
    cube('torre_imposta', cx - Bf['w'] / 2 - 0.25, cx + Bf['w'] / 2 + 0.25, cz - Bf['w'] / 2 - 0.25, cz + Bf['w'] / 2 + 0.25, H, H + 0.25, 'silleria')
    stage('campanario', Bf['w'], H + 0.25, Bf['y1'], 2, *Bf['arch'], 0.8, 0.7, 0.3)
    y_up = Bf['y1'] + 0.25
    stage('cuerpo_alto', Up['w'], y_up, Up['y1'], 1, *Up['arch'], 0.7, 0.4, 0.17)
    for o, nm in ((-Bf['w'] / 4, 'n'), (Bf['w'] / 4, 's')):
        bell(f'campana_{nm}', cx + o, Bf['y1'] - 0.8 - 1.1 - 0.15, cz, 1.0, 'bronce')
    bell('campana_alta', cx, Up['y1'] - 0.7 - 0.75, cz, 0.6, 'bronce')
    y_pd = Up['y1'] + 0.25
    cube('pedestal', cx - Pd['w'] / 2, cx + Pd['w'] / 2, cz - Pd['w'] / 2, cz + Pd['w'] / 2, y_pd, Pd['y1'] - 0.15, 'silleria')
    cube('pedestal_cornisa', cx - Pd['w'] / 2 - 0.12, cx + Pd['w'] / 2 + 0.12, cz - Pd['w'] / 2 - 0.12, cz + Pd['w'] / 2 + 0.12, Pd['y1'] - 0.15, Pd['y1'], 'silleria')
    bm = bmesh.new(); h = Sp['w'] / 2
    base = [bm.verts.new(B(cx + a * h, Pd['y1'], cz + c * h)) for a, c in [(-1, -1), (1, -1), (1, 1), (-1, 1)]]
    apex = bm.verts.new(B(cx, Sp['y1'], cz))
    for i in range(4): bm.faces.new((base[i], base[(i + 1) % 4], apex))
    bm.faces.new(list(reversed(base))); link_bm('chapitel', bm, 'silleria')
    ball('chapitel_bola', cx, Sp['y1'] + 0.12, cz, 0.18, 'silleria')
    cube('cruz_v', cx - 0.04, cx + 0.04, cz - 0.04, cz + 0.04, Sp['y1'] + 0.28, T['top'], 'hierro')
    cube('cruz_h', cx - 0.04, cx + 0.04, cz - 0.35, cz + 0.35, T['top'] - 0.45, T['top'] - 0.37, 'hierro')
    cube('veleta', cx - 0.015, cx + 0.015, cz + 0.05, cz + 0.6, T['top'] - 0.9, T['top'] - 0.7, 'hierro')
    # the storks' nests on the belfry's cornice, at two of its corners
    nest('nido_1', cx + Bf['w'] / 2 - 0.6, Bf['y1'] + 0.25, cz - Bf['w'] / 2 + 0.6, 0.55, 'nido')
    nest('nido_2', cx - Bf['w'] / 2 + 0.6, Bf['y1'] + 0.25, cz + Bf['w'] / 2 - 0.6, 0.5, 'nido')
    # ---- the north-west turret: a small stage by the corner, its cornice, a stone cap and four balls
    Tu = SPEC['turret']
    tcx, tcz = (Tu['x0'] + Tu['x1']) / 2, (Tu['z0'] + Tu['z1']) / 2; hw2 = (Tu['x1'] - Tu['x0']) / 2
    yb = Tu['cornice']; yt = yb - 0.2                            # (the turret's own cornice)
    cube('torreon', Tu['x0'], Tu['x1'], Tu['z0'], Tu['z1'], H, yt, 'silleria')
    cube('torreon_cornisa', Tu['x0'] - 0.14, Tu['x1'] + 0.14, Tu['z0'] - 0.14, Tu['z1'] + 0.14, yt, yb, 'silleria')
    # a stilted round pediment on each face, 1,5 m wide, its crown at the photo's height
    rp = 0.75; st = (Tu['top'] - yb) - rp
    shape = lambda r, s2: [(r, 0.0), (r, s2)] + [(r * math.cos(math.pi * k / 16), s2 + r * math.sin(math.pi * k / 16)) for k in range(1, 16)] + [(-r, s2), (-r, 0.0)]
    for nx, nz in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        fx2, fz2 = tcx + nx * (hw2 - 0.15), tcz + nz * (hw2 - 0.15)
        wall_prism('torreon_fronton', shape(rp, st), fx2, fz2, nx, nz, yb, -0.15, 0.15, 'silleria')
        ring = wall_prism('torreon_fronton_moldura', shape(rp + 0.09, st), fx2, fz2, nx, nz, yb, 0.1, 0.2, 'silleria')
        cut(ring, wall_prism('c', shape(rp - 0.02, st), fx2, fz2, nx, nz, yb - 0.01, 0.3, 0.0, 'silleria'))
    # (behind the four pediments, the cap they frame: a cross vault, seen as a pyramid)
    bm = bmesh.new()
    base = [bm.verts.new(B(tcx + a * (hw2 - 0.3), yb, tcz + c * (hw2 - 0.3))) for a, c in [(-1, -1), (1, -1), (1, 1), (-1, 1)]]
    apex = bm.verts.new(B(tcx, Tu['top'] - 0.3, tcz))
    for i in range(4): bm.faces.new((base[i], base[(i + 1) % 4], apex))
    link_bm('torreon_bovedilla', bm, 'silleria')
    # a pinnacle on each corner: pedestal, obelisk, ball, their tips at the pediments' height
    for sx in (-1, 1):
        for sz in (-1, 1):
            px2, pz2 = tcx + sx * (hw2 - 0.02), tcz + sz * (hw2 - 0.02)
            cube('torreon_pinaculo_base', px2 - 0.18, px2 + 0.18, pz2 - 0.18, pz2 + 0.18, yb, yb + 0.5, 'silleria')
            bm = bmesh.new(); hp = 0.13
            base = [bm.verts.new(B(px2 + a * hp, yb + 0.5, pz2 + c * hp)) for a, c in [(-1, -1), (1, -1), (1, 1), (-1, 1)]]
            apex = bm.verts.new(B(px2, Tu['top'] - 0.17, pz2))
            for i in range(4): bm.faces.new((base[i], base[(i + 1) % 4], apex))
            link_bm('torreon_pinaculo', bm, 'silleria')
            ball('torreon_pinaculo_bola', px2, Tu['top'] - 0.09, pz2, 0.09, 'silleria')
    # ---- the roof (tiles) over the nave and the apse, its ridge; the side chapels' tops are flat
    Rf = SPEC['roof']; hw = Rf['half']; yr = H + hw * math.tan(Rf['pitch'])
    xw, xe = Rf['x0'], Rf['apse']
    bm = bmesh.new()
    v = lambda x, y, z: bm.verts.new(B(x, y + 0.02, z))
    nw2, sw, r0, r1 = v(xw, H, -hw), v(xw, H, hw), v(xw + hw, yr, 0), v(xe, yr, 0)
    fan = [v(xe + hw * math.sin(a), H, -hw * math.cos(a)) for a in [math.pi * i / 6 for i in range(7)]]
    bm.faces.new((nw2, fan[0], r1, r0)); bm.faces.new((fan[-1], sw, r0, r1)); bm.faces.new((sw, nw2, r0))
    for i in range(6): bm.faces.new((fan[i], fan[i + 1], r1))
    link_bm('cubierta', bm, 'teja')
    bm = bmesh.new(); bmesh.ops.create_cone(bm, cap_ends=True, segments=10, radius1=0.13, radius2=0.13, depth=xe - xw - hw)
    rot = Vector((1, 0, 0)).to_track_quat('Z', 'Y').to_matrix().to_4x4()
    for vv in bm.verts: vv.co = rot @ vv.co
    for vv in bm.verts: vv.co += Vector(B((xw + hw + xe) / 2, yr + 0.06, 0))
    link_bm('cumbrera', bm, 'teja')
    # ---- the sacristy: rubble, its plinth and cornice, a flat roof
    solid('sacristia', sac, 0, SPEC['sacristy'] - 0.5, 'mamposteria')
    sweep('sacristia_zocalo', sac, [(0.1, 0.0), (0.1, 0.85), (0.03, 0.93), (0.0, 0.95)], 'zocalo', top=False)
    sweep('sacristia_cornisa', clean(sac, 0.8), [(-0.05, SPEC['sacristy'] - 0.5), (0.08, SPEC['sacristy'] - 0.5), (0.25, SPEC['sacristy'] - 0.3), (0.3, SPEC['sacristy']), (-0.2, SPEC['sacristy'])], 'silleria')
    # ---- every piece: its UVs in metres over its material's tile
    for ob in list(COL.objects):
        if ob.type == 'MESH': reuv(ob)
    merge()

def merge():
    """one mesh per material (one draw call each); the bells stay apart (they swing), the nests (the storks land on
    them) and the buttresses (the game gives them colliders) are marked by name in the JSON beside the model"""
    keep = ('campana_',)
    marks = {'contrafuertes': [], 'nidos': [], 'campanas': [], 'portadaOeste': {'escala': SPEC['west_portal']['scale']}}
    for ob in COL.objects:
        if ob.type != 'MESH': continue
        bb = [ob.matrix_world @ Vector(c) for c in ob.bound_box]
        lo = [min(v[i] for v in bb) for i in range(3)]; hi = [max(v[i] for v in bb) for i in range(3)]
        # (back to the frame's x, y, z from Blender's x, -z, y)
        box3 = {'x': [lo[0], hi[0]], 'y': [lo[2], hi[2]], 'z': [-hi[1], -lo[1]]}
        if ob.name.startswith('contrafuerte_') and not any(k in ob.name for k in ('zocalo', 'base', 'remate')): marks['contrafuertes'].append(box3)
        if ob.name.startswith('nido'): marks['nidos'].append([(lo[0] + hi[0]) / 2, hi[2], -(lo[1] + hi[1]) / 2])
        if ob.name.startswith('campana_'): marks['campanas'].append({'name': ob.name, 'top': [(lo[0] + hi[0]) / 2, hi[2], -(lo[1] + hi[1]) / 2]})
    by = {}
    for ob in list(COL.objects):
        if ob.type != 'MESH' or any(ob.name.startswith(k) for k in keep): continue
        by.setdefault(ob.data.materials[0].name, []).append(ob)
    for name, obs in by.items():
        bpy.ops.object.select_all(action='DESELECT')
        for o in obs: o.select_set(True)
        bpy.context.view_layer.objects.active = obs[0]
        if len(obs) > 1: bpy.ops.object.join()
        obs[0].name = name
    json.dump(marks, open(os.path.splitext(OUT)[0] + '.json', 'w'), indent=1)

# ================================================================ phase 4: the light — ambient occlusion baked in Cycles
def bake_ao(res=2048, samples=48, rebote=256):
    """the light of the sky as the stone gets it, baked once in Cycles into an atlas over a second UV set, which the
    exporter hands to three.js as the occlusion map (aoMap: it darkens the sky's and the bounce's light, not the sun's).
    First the bare occlusion — the sky each point sees: corners, reveals, under the cornice and the buttresses' caps —
    as approved in phase 4. Then the light that bounces into those places off the stone round them and off the street,
    added on: ao + (1 − ao)·bounce. Bare, a reveal or a cartouche came out near black; Unity's baked light showed them
    shaded, not black (2026-10-11). The open walls hardly change: there is little left to add there"""
    import numpy as np
    targets = [o for o in COL.objects if o.type == 'MESH' and o.data.materials and o.data.materials[0].name in ('mamposteria', 'silleria', 'zocalo', 'teja')]
    # a ground under the church, so its foot gets the dark of the ground (removed after the bake)
    bpy.ops.mesh.primitive_plane_add(size=200, location=(0, 0, 0)); ground = bpy.context.object
    for o in targets:
        if 'AO' not in o.data.uv_layers: o.data.uv_layers.new(name='AO')
        o.data.uv_layers['AO'].active = True
    bpy.ops.object.select_all(action='DESELECT')
    for o in targets: o.select_set(True)
    bpy.context.view_layer.objects.active = targets[0]
    bpy.ops.object.mode_set(mode='EDIT'); bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.uv.smart_project(angle_limit=math.radians(60), island_margin=0.003, area_weight=0.0, scale_to_bounds=False)
    bpy.ops.object.mode_set(mode='OBJECT')
    img = bpy.data.images.new('ao', res, res, alpha=False); img.colorspace_settings.name = 'Non-Color'
    nodes = []
    for m in {m for o in targets for m in o.data.materials if m}:
        nt = m.node_tree
        n = nt.nodes.new('ShaderNodeTexImage'); n.image = img; nt.nodes.active = n; nodes.append((nt, n))
    sc = bpy.context.scene; sc.render.engine = 'CYCLES'; sc.cycles.device = 'CPU'; sc.cycles.samples = samples
    sc.render.bake.margin = 6
    bpy.ops.object.select_all(action='DESELECT')
    for o in targets: o.select_set(True)
    bpy.context.view_layer.objects.active = targets[0]
    bpy.ops.object.bake(type='AO', uv_layer='AO')
    ao = np.array(img.pixels[:], dtype=np.float32).reshape(-1, 4)[:, 0].copy()
    # the bounce: under a white sky, the street as dark as a street, Cycles' indirect diffuse alone
    gm = bpy.data.materials.new('calle_horneado'); gm.use_nodes = True
    bsdf = gm.node_tree.nodes.get('Principled BSDF')
    bsdf.inputs['Base Color'].default_value = (0.25, 0.23, 0.21, 1.0); bsdf.inputs['Roughness'].default_value = 1.0
    ground.data.materials.append(gm)
    wd = bpy.data.worlds.new('cielo_blanco'); wd.use_nodes = True
    bg = wd.node_tree.nodes.get('Background'); bg.inputs['Color'].default_value = (1, 1, 1, 1); bg.inputs['Strength'].default_value = 1.0
    sc.world = wd
    try: # the Mac's GPU (Metal) when there is one: the same bake, minutes sooner
        prefs = bpy.context.preferences.addons['cycles'].preferences
        prefs.compute_device_type = 'METAL'; prefs.get_devices()
        if any(d.type == 'METAL' for d in prefs.devices):
            for d in prefs.devices: d.use = d.type == 'METAL'
            sc.cycles.device = 'GPU'
    except Exception as e: print('rebote en CPU:', e)
    sc.cycles.samples = rebote; sc.cycles.max_bounces = 4; sc.cycles.diffuse_bounces = 3
    sc.render.bake.use_pass_direct = False; sc.render.bake.use_pass_indirect = True; sc.render.bake.use_pass_color = False
    bpy.ops.object.bake(type='DIFFUSE', pass_filter={'INDIRECT'}, uv_layer='AO')
    bpy.data.objects.remove(ground); sc.world = None
    px = np.array(img.pixels[:], dtype=np.float32).reshape(-1, 4)
    rb = np.clip(0.2126 * px[:, 0] + 0.7152 * px[:, 1] + 0.0722 * px[:, 2], 0.0, 1.0) # (one grey: the bounce off the golden stone is warm)
    v = np.clip(ao + (1.0 - ao) * rb, 0.0, 1.0)
    px[:, 0] = px[:, 1] = px[:, 2] = v; px[:, 3] = 1.0
    img.pixels[:] = px.ravel()
    cov = ao > 0.012
    print(f'oclusión con rebote ({sc.cycles.device}): rebote mediano {np.median(rb[cov]):.3f}; oclusión p5/50/95 {np.percentile(ao[cov], 5):.2f}/{np.median(ao[cov]):.2f}/{np.percentile(ao[cov], 95):.2f} → {np.percentile(v[cov], 5):.2f}/{np.median(v[cov]):.2f}/{np.percentile(v[cov], 95):.2f}')
    img.filepath_raw = os.path.join(ROOT, '.cache', 'hq', 'tex', 'ao.png'); img.file_format = 'PNG'; img.save()
    # hand it to the exporter: a «glTF Material Output» group with an Occlusion socket, fed by the AO map's red, UV 'AO'
    grp = bpy.data.node_groups.get('glTF Material Output')
    if not grp:
        grp = bpy.data.node_groups.new('glTF Material Output', 'ShaderNodeTree')
        grp.interface.new_socket('Occlusion', in_out='INPUT', socket_type='NodeSocketFloat')
    for nt, n in nodes:
        uvn = nt.nodes.new('ShaderNodeUVMap'); uvn.uv_map = 'AO'; nt.links.new(uvn.outputs['UV'], n.inputs['Vector'])
        sep = nt.nodes.new('ShaderNodeSeparateColor'); nt.links.new(n.outputs['Color'], sep.inputs[0])
        g = nt.nodes.new('ShaderNodeGroup'); g.node_tree = grp; nt.links.new(sep.outputs[0], g.inputs['Occlusion'])
    # the UV set the textures read stays the first one
    for o in targets: o.data.uv_layers[0].active = True; o.data.uv_layers[0].active_render = True
    return img


if GREY: build_greybox()
else:
    build_detail()
    if '--sin-ao' not in ARGS: bake_ao()

# ---------------------------------------------------------------- out
os.makedirs(os.path.dirname(OUT), exist_ok=True)
bpy.ops.export_scene.gltf(filepath=OUT, export_format='GLB', export_yup=True, export_apply=True, export_texcoords=True, export_normals=True, export_materials='EXPORT', export_image_format='JPEG', export_image_quality=88)
tris = sum(len(o.data.polygons) for o in bpy.data.objects if o.type == 'MESH')
print(f'iglesia: {len([o for o in bpy.data.objects if o.type == "MESH"])} piezas, {tris} caras → {OUT} ({os.path.getsize(OUT) // 1024} KB)')
