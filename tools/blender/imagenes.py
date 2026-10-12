# Santa María's images in high definition (docs/hiperrealismo.md, «La 6c»): polychrome carvings as Spanish imaginería
# is made — the Virgin of the retablo, the Dolorosa, the Christ on his cross, the Sacred Heart, Saint Joseph with the
# Child, the Immaculate —, carved in Blender: MakeHuman's body (CC0: base mesh hm08, its default skeleton and weights;
# .cache/mh) posed on its own skeleton, its heads given their features (the women's from assets/mh/head.bin.gz, the
# game's own MakeHuman targets), robes cut from MakeHuman's own clothing helpers (the tights, the long skirt — they move
# with the body) thickened and folded as a carver folds wood, and the polychromy of the carnations and the estofado.
#   /Applications/Blender.app/Contents/MacOS/Blender --background --factory-startup --python tools/blender/imagenes.py -- \
#       [--solo virgen,dolorosa] [--out assets/hq/interior] [--vista .snaps/vista_imagen.png]
import bpy, bmesh, gzip, json, math, os, struct, sys
from mathutils import Vector, Matrix, Quaternion

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from mhlib import read_obj, read_target, apply_targets

ARGS = sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else []
def arg(k, d=None): return ARGS[ARGS.index(k) + 1] if k in ARGS else d
MH = next(p for p in (os.path.join(ROOT, '.cache', 'mh'), os.path.join(ROOT, '..', '.cache', 'mh')) if os.path.isdir(p))
OUT = os.path.abspath(arg('--out', os.path.join(ROOT, 'assets', 'hq', 'interior')))
ONLY = arg('--solo', '').split(',') if arg('--solo') else None

SC = bpy.context.scene
COLL = SC.collection

def B(p):
    """MakeHuman (decimetres, y up, facing +z) → Blender (metres, z up, facing −y)"""
    return Vector((p[0] * 0.1, -p[2] * 0.1, p[1] * 0.1))

# ---------------------------------------------------------------- the body
KEEP = {'body': 'carne', 'helper-tights': 'tunica', 'helper-skirt': 'falda', 'helper-l-eye': 'ojo', 'helper-r-eye': 'ojo'}   # (the hair helper is a fitting guide, spiky: the hair is carved apart)

def head_targets():
    """the head and neck's own MakeHuman targets, as the game keeps them (assets/mh/head.bin.gz, 'MHH3'): {name: {base
    vertex: delta (decimetres)}} — the women's faces come from its female macros"""
    b = gzip.open(os.path.join(ROOT, 'assets', 'mh', 'head.bin.gz')).read(); o = 0
    def rd(fmt):
        nonlocal o
        v = struct.unpack_from('<' + fmt, b, o); o += struct.calcsize('<' + fmt); return v
    def rs():
        n, = rd('H'); s = b[o:o + n].decode()
        return s, n
    assert b[:4] == b'MHH3'; o = 4
    nreg, = rd('I'); o += nreg * 12   # (the region's positions: the base mesh's, read from base.obj instead)
    # (the region: the base vertex indices it holds — mh_import.py's sorted 'need'; rebuilt from the joints' counts is not
    # possible here, so the file is read for its render indices, joints, landmarks, then the targets keyed by region index)
    nrv, = rd('I'); nri, = rd('I'); nbody, = rd('I')
    rvreg = list(rd(f'{nrv}H')); o += nrv * 4; o += nri * 2
    nj, = rd('H')
    for _ in range(nj):
        s, n = rs(); o += n; cnt, = rd('H'); o += cnt * 2
    nt, = rd('H'); out = {}
    for _ in range(nt):
        s, n = rs(); o += n; scale, = rd('f'); cnt, = rd('I')
        idx = rd(f'{cnt}H'); dv = rd(f'{cnt * 3}b')
        out[s[:]] = (scale, idx, dv)
    return nreg, out

def region_map(V):
    """the head file's region (its vertices sorted by base index) is mh_import.py's: every base vertex the head needs —
    rebuilt the same way it was made is not possible without its helpers' lists, so it is matched by position: the
    region's own positions are in the file"""
    b = gzip.open(os.path.join(ROOT, 'assets', 'mh', 'head.bin.gz')).read()
    nreg, = struct.unpack_from('<I', b, 4)
    P = struct.unpack_from(f'<{nreg * 3}f', b, 8)
    key = lambda x, y, z: (round(x, 4), round(y, 4), round(z, 4))
    where = {key(*V[i]): i for i in range(len(V))}
    return [where.get(key(P[3 * k], P[3 * k + 1], P[3 * k + 2]), -1) for k in range(nreg)]

def macros(female=False, age=0.5, weight=0.4):
    """the body's targets: a young man of average build (MakeHuman's caucasian-male-young, the universal targets for
    weight); a woman keeps the man's body — the robes hide it — and takes the female macros on her head"""
    T = os.path.join(MH, 'targets', 'macrodetails')
    out = [(read_target(os.path.join(T, 'caucasian-male-young.target')), 1.0)]
    lo = max(0.0, (0.5 - weight) * 2)
    if lo: out.append((read_target(os.path.join(T, 'universal-male-young-averagemuscle-minweight.target')), lo))
    return out

def build_body(name, female=False, weight=0.4):
    V, VT, F, FG = read_obj(os.path.join(MH, '3dobjs', 'base.obj'))
    P = apply_targets(V, macros(female, weight=weight))
    sk = json.load(open(os.path.join(MH, 'rigs', 'default.mhskel')))
    at = lambda j: [sum(P[i][c] for i in sk['joints'][j]) / len(sk['joints'][j]) for c in range(3)]
    if female:   # (the head's female macros, from the game's head file, over the man's head)
        reg = region_map(V)
        nreg, T = head_targets()
        D = {}
        for tname, w in (('macrodetails/universal-female-young-averagemuscle-averageweight', 1.0), ('macrodetails/caucasian-female-young', 1.0),
                         ('macrodetails/universal-male-young-averagemuscle-averageweight', -1.0), ('macrodetails/caucasian-male-young', -1.0)):
            if tname not in T: continue
            scale, idx, dv = T[tname]
            for k, r in enumerate(idx):
                vi = reg[r]
                if vi < 0: continue
                d = D.setdefault(vi, [0.0, 0.0, 0.0])
                for c in range(3): d[c] += dv[3 * k + c] * scale * w
        # (those macros are a whole woman's, shorter than the man: they carry her head and neck 13–15 cm down — on his
        # body, into his shoulders, under his tunic's collar: «la cabeza metida en los hombros». Only her face is kept:
        # the deltas taken from the skull's root, in full on the head and fading to nothing down the neck, from the
        # chin to the neck's root, so that his neck holds her head where his was)
        R = [i for i in sk['joints']['head____head'] if i in D]
        ref = [sum(D[i][c] for i in R) / len(R) for c in range(3)]
        hi = at('jaw____tail')[1]; lo = hi - 0.9   # (decimetres, MakeHuman's up axis)
        for vi, d in D.items():
            t = min(1.0, max(0.0, (P[vi][1] - lo) / (hi - lo))); t = t * t * (3 - 2 * t)
            P[vi] = [P[vi][c] + t * (d[c] - ref[c]) for c in range(3)]
    # the mesh: the body and the helpers kept, each a material slot by its part
    used = {}
    faces = []
    for f, g in zip(F, FG):
        if g in KEEP: faces.append(([v for v, _ in f], KEEP[g]))
    vids = sorted({v for f, _ in faces for v in f})
    remap = {v: i for i, v in enumerate(vids)}
    me = bpy.data.meshes.new(name)
    mats = sorted(set(KEEP.values()))
    me.from_pydata([B(P[v]) for v in vids], [], [[remap[v] for v in f] for f, _ in faces])
    for m in mats: me.materials.append(bpy.data.materials.get(m) or bpy.data.materials.new(m))
    for poly, (_, part) in zip(me.polygons, faces): poly.material_index = mats.index(part)
    ob = bpy.data.objects.new(name, me); COLL.objects.link(ob)
    # the skeleton: each bone from the centre of its head joint's vertices to its tail's
    J = {k: sum((B(P[i]) for i in ids), Vector()) / len(ids) for k, ids in sk['joints'].items()}
    arm = bpy.data.armatures.new(name + '_esqueleto'); rig = bpy.data.objects.new(name + '_esqueleto', arm); COLL.objects.link(rig)
    bpy.context.view_layer.objects.active = rig; bpy.ops.object.mode_set(mode='EDIT')
    for bn, d in sk['bones'].items():
        eb = arm.edit_bones.new(bn); eb.head = J[d['head']]; eb.tail = J[d['tail']]
        if (eb.tail - eb.head).length < 1e-4: eb.tail = eb.head + Vector((0, 0, 0.01))
    for bn, d in sk['bones'].items():
        if d.get('parent'): arm.edit_bones[bn].parent = arm.edit_bones[d['parent']]
    bpy.ops.object.mode_set(mode='OBJECT')
    # the weights
    W = json.load(open(os.path.join(MH, 'rigs', 'default_weights.mhw'))); W = W.get('weights', W)
    for bn, lst in W.items():
        vg = ob.vertex_groups.new(name=bn)
        for v, w in lst:
            if v in remap: vg.add([remap[v]], w, 'REPLACE')
    mod = ob.modifiers.new('esqueleto', 'ARMATURE'); mod.object = rig
    return ob, rig

# ---------------------------------------------------------------- posing
def _turn(rig, bone, q):
    """turn a posed bone by the world rotation q about its own head (the rig stands at the origin)"""
    pb = rig.pose.bones[bone]
    M = pb.matrix.copy()
    T = Matrix.Translation(M.translation)
    pb.matrix = T @ q.to_matrix().to_4x4() @ T.inverted() @ M
    bpy.context.view_layer.update()

def aim(rig, bone, direction, twist=0.0):
    """turn a bone so that it points along `direction` (world), after its parents have been posed; twist: then about
    itself"""
    bpy.context.view_layer.update()
    pb = rig.pose.bones[bone]
    cur = (pb.matrix.to_3x3() @ Vector((0, 1, 0))).normalized()
    d = Vector(direction).normalized()
    _turn(rig, bone, cur.rotation_difference(d))
    if twist: _turn(rig, bone, Quaternion(d, twist))

def bend(rig, bone, axis, angle):
    """a rotation of a bone about a world axis through its head"""
    bpy.context.view_layer.update()
    _turn(rig, bone, Quaternion(Vector(axis).normalized(), angle))

POSES = {
    # the hands joined in prayer before the breast: the upper arms down and a little forward, the forearms raised and
    # in, the hands upright, palm to palm
    'manos_juntas': [('upperarm01.L', (0.1, -0.08, -1.0)), ('upperarm01.R', (-0.1, -0.08, -1.0)),
                     ('lowerarm01.L', (-0.6, -0.75, 0.12)), ('lowerarm01.R', (0.6, -0.75, 0.12)),
                     ('wrist.L', (-0.22, -0.3, 1.0)), ('wrist.R', (0.22, -0.3, 1.0))],
    # the Sacred Heart: the left hand on the breast, at the heart; the right arm a little out and down, the palm open
    'corazon': [('upperarm01.L', (0.12, -0.1, -1.0)), ('lowerarm01.L', (-0.75, -0.55, 0.35)), ('wrist.L', (-0.6, -0.5, 0.6)),
                ('upperarm01.R', (-0.35, -0.25, -1.0)), ('lowerarm01.R', (-0.35, -0.75, -0.55)), ('wrist.R', (-0.25, -0.8, -0.5))],
    # Saint Joseph: the left forearm across before him (the Child sits on it), the right hand holding the staff
    'jose': [('upperarm01.L', (0.15, -0.15, -1.0)), ('lowerarm01.L', (-0.55, -0.8, 0.05)), ('wrist.L', (-0.6, -0.7, 0.2)),
             ('upperarm01.R', (-0.25, -0.2, -1.0)), ('lowerarm01.R', (-0.05, -0.85, -0.2)), ('wrist.R', (0.0, -0.9, 0.1))],
    # on the cross: the arms spread and raised, the palms open to the nails
    'cruz': [('upperarm01.L', (1.0, 0.0, 0.42)), ('lowerarm01.L', (1.0, 0.0, 0.48)), ('wrist.L', (1.0, 0.0, 0.5)),
             ('upperarm01.R', (-1.0, 0.0, 0.42)), ('lowerarm01.R', (-1.0, 0.0, 0.48)), ('wrist.R', (-1.0, 0.0, 0.5))],
    # the Child: his right hand raised in blessing, the left holding the world
    'nino': [('upperarm01.R', (-0.35, -0.3, -0.6)), ('lowerarm01.R', (-0.1, -0.4, 1.0)), ('upperarm01.L', (0.45, -0.3, -0.8)), ('lowerarm01.L', (-0.2, -0.9, 0.3))],
}

def pose(rig, name):
    for bone, d in POSES[name]:
        if bone in rig.pose.bones: aim(rig, bone, d)
    bpy.context.view_layer.update()

def stretch_neck(rig, d):
    """a longer neck by d (metres): the head bone drawn up out of it — the head follows whole, the neck's skin, blended
    between them, stretches"""
    rig.pose.bones['head'].location = (0, d, 0); bpy.context.view_layer.update()

def bake_pose(ob):
    bpy.context.view_layer.objects.active = ob
    for m in list(ob.modifiers):
        if m.type == 'ARMATURE': bpy.ops.object.modifier_apply(modifier=m.name)

# ---------------------------------------------------------------- the cloth: draped, then carved
def grid_mesh(name, rows):
    """a mesh from rows of points (each row the same length): quads between them"""
    me = bpy.data.meshes.new(name)
    n = len(rows[0]); verts = [p for r in rows for p in r]
    faces = [(j * n + i, j * n + i + 1, (j + 1) * n + i + 1, (j + 1) * n + i) for j in range(len(rows) - 1) for i in range(n - 1)]
    me.from_pydata(verts, [], faces)
    ob = bpy.data.objects.new(name, me); COLL.objects.link(ob)
    return ob

def drape(cloth, body, pin_rows, frames=70, mass=0.35, stiff=12.0, thick=0.012, others=()):
    """let a cloth fall over the posed body (its pinned rows held), as heavy cloth with its own folds; then the folds
    are kept, thickened and smoothed — as a carver would cut them"""
    vg = cloth.vertex_groups.new(name='pin')
    vg.add(pin_rows, 1.0, 'REPLACE')
    col = body.modifiers.new('choque', 'COLLISION'); body.collision.thickness_outer = 0.008; body.collision.cloth_friction = 8
    extra = [(o, o.modifiers.new('choque', 'COLLISION')) for o in others]   # (what else it lies on: the hair under a veil)
    for o, _ in extra: o.collision.thickness_outer = 0.005; o.collision.cloth_friction = 8
    cm = cloth.modifiers.new('tela', 'CLOTH'); st = cm.settings
    st.quality = 6; st.mass = mass; st.tension_stiffness = stiff; st.compression_stiffness = stiff; st.shear_stiffness = stiff * 0.5
    st.bending_stiffness = 0.6; st.air_damping = 2.0; st.vertex_group_mass = 'pin'
    cm.collision_settings.use_self_collision = True; cm.collision_settings.distance_min = 0.006; cm.collision_settings.self_distance_min = 0.005
    SC.frame_start, SC.frame_end = 1, frames
    cm.point_cache.frame_start, cm.point_cache.frame_end = 1, frames
    for f in range(1, frames + 1): SC.frame_set(f)
    bpy.context.view_layer.objects.active = cloth
    bpy.ops.object.modifier_apply(modifier=cm.name)
    body.modifiers.remove(col)
    for o, m in extra: o.modifiers.remove(m)
    so = cloth.modifiers.new('grosor', 'SOLIDIFY'); so.thickness = thick; so.offset = 1.0
    su = cloth.modifiers.new('suave', 'SUBSURF'); su.levels = 1; su.render_levels = 1
    for m in (so, su): bpy.ops.object.modifier_apply(modifier=m.name)
    return cloth

def joint(rig, bone, end='head'):
    bpy.context.view_layer.update()
    pb = rig.pose.bones[bone]
    return (rig.matrix_world @ (pb.head if end == 'head' else pb.tail)).copy()

def mantle(name, rig, floor_z, open_front=0.75, flare=0.16, n=48, m=60):
    """a mantle over the shoulders, open at the front, falling to the floor"""
    sl, sr = joint(rig, 'upperarm01.L'), joint(rig, 'upperarm01.R'); nk = joint(rig, 'neck01')
    top = (sl.z + sr.z) / 2 + 0.03; cx, cy = nk.x, nk.y + 0.02
    rows = []
    for j in range(m + 1):
        t = j / m; z = top + (floor_z + 0.02 - top) * t
        r = 0.2 + (abs(sl.x - sr.x) / 2 + 0.06 - 0.2) * min(1, t * 6) + flare * t
        row = []
        for i in range(n + 1):
            a = -math.pi * open_front + 2 * math.pi * open_front * i / n   # (0 the back)
            row.append(Vector((cx + r * math.sin(a), cy + r * math.cos(a) * (0.85 if t > 0.05 else 0.7), z)))
        rows.append(row)
    ob = grid_mesh(name, rows)
    return ob, list(range(n + 1))

# ---------------------------------------------------------------- a look
def vista(path, target, dist=2.6, height=1.0):
    sc = SC; sc.render.engine = 'CYCLES'; sc.cycles.device = 'CPU'; sc.cycles.samples = 48; sc.cycles.use_denoising = True
    sc.render.resolution_x, sc.render.resolution_y = 800, 1100
    w = bpy.data.worlds.new('w'); w.use_nodes = True; sc.world = w; w.node_tree.nodes['Background'].inputs['Strength'].default_value = 0.5
    for loc, e in (((1.5, -2.5, 2.4), 300), ((-2.0, -1.0, 1.8), 120)):
        L = bpy.data.objects.new('l', bpy.data.lights.new('l', 'AREA')); COLL.objects.link(L); L.data.energy = e; L.data.size = 1.5
        L.location = loc; L.rotation_euler = (Vector(target) - Vector(loc)).to_track_quat('-Z', 'Y').to_euler()
    cam = bpy.data.objects.new('cam', bpy.data.cameras.new('cam')); COLL.objects.link(cam); sc.camera = cam
    cam.location = Vector(target) + Vector((0.4, -dist, height - target[2] + 0.1)); cam.data.lens = 50
    cam.rotation_euler = (Vector(target) - cam.location).to_track_quat('-Z', 'Y').to_euler()
    sc.render.filepath = path
    bpy.ops.render.render(write_still=True)

# ---------------------------------------------------------------- the parts of a figure
def part(ob, mat, name):
    """a copy of the posed body holding only the faces of one of its parts (by material)"""
    me = ob.data.copy(); o = bpy.data.objects.new(name, me); COLL.objects.link(o)
    idx = me.materials.find(mat)
    bm = bmesh.new(); bm.from_mesh(me)
    bmesh.ops.delete(bm, geom=[f for f in bm.faces if f.material_index != idx], context='FACES')
    bm.to_mesh(me); bm.free()
    o.vertex_groups.clear()
    return o

def keep_only(ob, mat):
    me = ob.data; idx = me.materials.find(mat)
    bm = bmesh.new(); bm.from_mesh(me)
    bmesh.ops.delete(bm, geom=[f for f in bm.faces if f.material_index != idx], context='FACES')
    bm.to_mesh(me); bm.free()

def set_material(ob, name, color, rough=0.6, metal=0.0):
    m = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    m.use_nodes = True; p = m.node_tree.nodes['Principled BSDF']
    p.inputs['Base Color'].default_value = (*color, 1); p.inputs['Roughness'].default_value = rough; p.inputs['Metallic'].default_value = metal
    ob.data.materials.clear(); ob.data.materials.append(m)
    return m

def mods(ob, *spec):
    bpy.context.view_layer.objects.active = ob
    for kind, kw in spec:
        m = ob.modifiers.new(kind.lower(), kind)
        for k, v in kw.items(): setattr(m, k, v)
        bpy.ops.object.modifier_apply(modifier=m.name)

def neckline(rig):
    """the tunic's neck: MakeHuman's tights are a whole body stocking, up the neck and the nape to the skull like a
    hood — the heads looked sunk in the shoulders. The tunic is cut round the root of the neck: low in front (at the
    sternum's notch), where the neck meets the shoulders at the sides, at the seventh vertebra behind; all of it above
    the chin goes. A test on a point: is it above the neckline?"""
    nk = joint(rig, 'neck01'); jw = joint(rig, 'jaw', 'tail')
    cx, cy = nk.x, nk.y - 0.01                       # (the neck's own axis: a centimetre before the joints')
    def above(co):
        dx, dy = co.x - cx, co.y - cy; r = math.hypot(dx, dy)
        if r > 0.17: return False
        if co.z > jw.z - 0.005: return True
        front = max(0.0, -dy / r) if r > 1e-6 else 0.0   # (1 straight in front … 0 at the sides and behind)
        return r < 0.1 + 0.008 * front and co.z > nk.z - 0.05 - 0.04 * front ** 1.5
    return above

def drop_crumbs(bm, keep=200):
    """after a cut: the little islands it left go"""
    seen = set(); out = []
    for v in bm.verts:
        if v in seen: continue
        isl = [v]; seen.add(v); k = 0
        while k < len(isl):
            for e in isl[k].link_edges:
                w = e.other_vert(isl[k])
                if w not in seen: seen.add(w); isl.append(w)
            k += 1
        if len(isl) < keep: out += isl
    if out: bmesh.ops.delete(bm, geom=out, context='VERTS')

def tunic(body, floor, rig, folds=11, flare=0.32, seed=1):
    """the tunic: MakeHuman's tights above the waist (thickened off the body), cut round the neck, and its long skirt
    let down to the floor, flared and pleated — the folds deeper towards the hem, as carved"""
    up = part(body, 'tunica', 'tunica_alta'); sk = part(body, 'falda', 'tunica_falda')
    ztop = max(v.co.z for v in sk.data.vertices); zhem = min(v.co.z for v in sk.data.vertices)
    cx = sum(v.co.x for v in sk.data.vertices) / len(sk.data.vertices); cy = sum(v.co.y for v in sk.data.vertices) / len(sk.data.vertices)
    # the tights: only above the waist (the legs are in the skirt), and below the neckline
    above = neckline(rig)
    bm = bmesh.new(); bm.from_mesh(up.data)
    bmesh.ops.delete(bm, geom=[v for v in bm.verts if v.co.z < ztop - 0.12 or above(v.co)], context='VERTS')
    drop_crumbs(bm)
    # the neckline's edge: its steps (the mesh's faces) smoothed along the cut; and there the cloth is drawn in to the
    # neck, as a hem holds it — no gap to see into between the tunic and the skin
    nk = joint(rig, 'neck01')
    ring = [v for v in bm.verts if v.co.z > nk.z - 0.16 and math.hypot(v.co.x - nk.x, v.co.y - nk.y) < 0.2
            and any(e.is_boundary for e in v.link_edges)]
    rs = set(ring)
    for _ in range(12):
        new = {}
        for v in ring:
            nb = [e.other_vert(v) for e in v.link_edges if e.is_boundary and e.other_vert(v) in rs]
            if len(nb) == 2: new[v] = v.co * 0.5 + (nb[0].co + nb[1].co) * 0.25
        for v, c in new.items(): v.co = c
    from mathutils.kdtree import KDTree
    kd = KDTree(max(1, len(ring)))
    for i, v in enumerate(ring): kd.insert(v.co, i)
    kd.balance()
    bm.normal_update()
    for v in bm.verts:
        d = kd.find(v.co)[2] if ring else 1.0
        t = min(1.0, d / 0.04); t = t * t * (3 - 2 * t)
        v.co += v.normal * (0.004 + 0.008 * t)
    bm.to_mesh(up.data); bm.free()
    # the skirt: down to the floor, flared, pleated
    import random
    rnd = random.Random(seed); ph = [rnd.uniform(0, 6.283) for _ in range(4)]
    for v in sk.data.vertices:
        t = (ztop - v.co.z) / max(1e-6, ztop - zhem)
        z = ztop - t * (ztop - (floor + 0.005))
        dx, dy = v.co.x - cx, v.co.y - cy; r = math.hypot(dx, dy); a = math.atan2(dy, dx)
        fold = math.sin(a * folds + ph[0] + 0.6 * math.sin(a * 3 + ph[1])) * 0.5 + 0.5
        r2 = r * (1 + flare * t * t) + 0.014 + (0.012 + 0.06 * t) * fold ** 2
        v.co = Vector((cx + r2 * math.cos(a), cy + r2 * math.sin(a), z))
    for o in (up, sk):
        mods(o, ('SUBSURF', {'levels': 1}), ('SOLIDIFY', {'thickness': 0.006, 'offset': 1.0}))
    return up, sk, ztop

def veil(name, rig, body, n=48, m=40):
    """a veil: a hood round the head — open over the face — falling to the shoulders and down the back; started close to
    its place, it settles on the head and shoulders"""
    hd = joint(rig, 'head', 'tail'); hb = joint(rig, 'head', 'head'); sl, sr = joint(rig, 'upperarm01.L'), joint(rig, 'upperarm01.R')
    jw = joint(rig, 'jaw', 'tail'); zs = (sl.z + sr.z) / 2
    c = Vector(((hd.x + hb.x) / 2, (hd.y + hb.y) / 2 + 0.01, hd.z))
    rh = 0.115; rs = abs(sl.x - sr.x) / 2 + 0.04
    bottom = (sl.z + sr.z) / 2 - 0.32
    rows = []
    top = c.z + 0.03
    for j in range(m + 1):
        t = j / m
        z = top - (top - bottom) * t
        # (round the crown of the head in its first 11 cm, close by its sides down to the chin, then out to the
        # shoulders and down: measured on the head, so that a longer neck does not stretch the hood above it)
        u = (top - z) / 0.11
        if u < 1: r = rh * math.sin(u * math.pi / 2)
        elif z > jw.z: r = rh + 0.01 * (top - 0.11 - z) / max(0.01, top - 0.11 - jw.z)
        else: r = rh + 0.01 + (rs - rh - 0.01) * min(1.0, (jw.z - z) / max(0.05, jw.z - zs)) ** 0.8 + 0.04 * max(0.0, zs - z) / 0.3
        r += 0.01
        # (the face's opening: as wide as the face down to the chin, then opening out over the neck and the breast — the
        # neck seen, the veil falling on the shoulders and down the back)
        ext = 0.82 - 0.24 * min(1.0, max(0.0, (jw.z - z) / max(0.05, jw.z - zs)))
        row = []
        for i in range(n + 1):
            a = -math.pi * ext + 2 * math.pi * ext * i / n      # (0 the back; the face's opening in front)
            yy = c.y + r * math.cos(a) * (1.1 if math.cos(a) > 0 else 0.9)
            row.append(Vector((c.x + r * math.sin(a), yy, z)))
        rows.append(row)
    ob = grid_mesh(name, rows)
    pins = list(range(n + 1)) + list(range(n + 1, 2 * (n + 1)))   # (the crown of the head)
    return ob, pins

def mantle2(name, rig, floor, open_front=0.72, n=60, m=72, waves=9, amp=0.035):
    """the mantle: over the shoulders and down the back to the floor, open in front; started with more cloth than it
    needs, in waves, so that it falls into folds"""
    sl, sr = joint(rig, 'upperarm01.L'), joint(rig, 'upperarm01.R'); nk = joint(rig, 'neck01')
    top = max(sl.z, sr.z) + 0.05; cx, cy = nk.x, nk.y + 0.03
    half = abs(sl.x - sr.x) / 2 + 0.07
    rows = []
    for j in range(m + 1):
        t = j / m; z = top + (floor - 0.04 - top) * t
        r = 0.16 + (half - 0.16) * min(1, t * 7) + 0.22 * t
        row = []
        for i in range(n + 1):
            a = -math.pi * open_front + 2 * math.pi * open_front * i / n
            rr = r + amp * t * math.sin(a * waves + 3 * t)
            row.append(Vector((cx + rr * math.sin(a), cy + rr * math.cos(a) * (0.8 if t > 0.06 else 0.65), z)))
        rows.append(row)
    return grid_mesh(name, rows), list(range(n + 1))

def lined(ob, outer, inner, thick=0.01):
    """a cloth's two faces: its colour outside, its lining in"""
    ob.data.materials.clear(); ob.data.materials.append(outer); ob.data.materials.append(inner)
    mods(ob, ('SOLIDIFY', {'thickness': thick, 'offset': 1.0, 'material_offset': 1, 'material_offset_rim': 1}), ('SUBSURF', {'levels': 1}))

def crown(name, centre, r=0.11, h=0.12, mat=None):
    """a royal crown of gilded silver: a band, eight fleurons, arches closing over it, the orb and its cross"""
    out = []
    c = Vector(centre)
    def lathe_b(nm, prof, at, seg=32):
        me = bpy.data.meshes.new(nm); verts, faces = [], []
        for i, (rr, hh) in enumerate(prof):
            for k in range(seg): a = 2 * math.pi * k / seg; verts.append(at + Vector((rr * math.cos(a), rr * math.sin(a), hh)))
        for i in range(len(prof) - 1):
            for k in range(seg): faces.append((i * seg + k, i * seg + (k + 1) % seg, (i + 1) * seg + (k + 1) % seg, (i + 1) * seg + k))
        me.from_pydata(verts, [], faces); o = bpy.data.objects.new(nm, me); COLL.objects.link(o); return o
    out.append(lathe_b(name + '_aro', [(r, 0), (r + 0.006, 0.005), (r + 0.006, 0.035), (r, 0.04), (r - 0.004, 0.04), (r - 0.004, 0.0)], c))
    for k in range(8):
        a = 2 * math.pi * k / 8
        p = c + Vector((r * math.cos(a), r * math.sin(a), 0.04))
        bpy.ops.mesh.primitive_uv_sphere_add(radius=0.016, segments=10, ring_count=6, location=p + Vector((0, 0, 0.015))); out.append(bpy.context.object)
    for k in range(4):   # the arches
        a = math.pi * k / 4
        pts = []
        for i in range(17):
            t = math.pi * i / 16
            pts.append(c + Vector((r * math.cos(t) * math.cos(a), r * math.cos(t) * math.sin(a), 0.04 + (h - 0.04) * math.sin(t))))
        cu = bpy.data.curves.new(name + f'_arco{k}', 'CURVE'); cu.dimensions = '3D'; cu.bevel_depth = 0.005
        sp = cu.splines.new('POLY'); sp.points.add(len(pts) - 1)
        for i, q in enumerate(pts): sp.points[i].co = (*q, 1)
        o = bpy.data.objects.new(name + f'_arco{k}', cu); COLL.objects.link(o); out.append(o)
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.022, segments=12, ring_count=8, location=c + Vector((0, 0, h + 0.02))); out.append(bpy.context.object)
    for d in ((0, 0, 0.035), ):
        bpy.ops.mesh.primitive_cube_add(size=1, location=c + Vector((0, 0, h + 0.06))); o = bpy.context.object; o.scale = (0.008, 0.008, 0.05); out.append(o)
        bpy.ops.mesh.primitive_cube_add(size=1, location=c + Vector((0, 0, h + 0.07))); o = bpy.context.object; o.scale = (0.03, 0.008, 0.008); out.append(o)
    for o in out:
        bpy.context.view_layer.objects.active = o
        if o.type == 'CURVE': o.select_set(True); bpy.ops.object.convert(target='MESH'); o.select_set(False)
        o.data.materials.clear(); o.data.materials.append(mat)
    return out

def clouds(name, centre, r=0.36, n=11, cherubs=3, mat=None, flesh=None, seed=3):
    """a bank of clouds under the feet (metaballs), cherubs' heads among them"""
    import random
    rnd = random.Random(seed)
    mb = bpy.data.metaballs.new(name); mb.resolution = 0.03; mb.render_resolution = 0.03
    o = bpy.data.objects.new(name, mb); COLL.objects.link(o)
    c = Vector(centre)
    for k in range(n):
        a = 2 * math.pi * k / n + rnd.uniform(-0.2, 0.2)
        e = mb.elements.new(); e.co = c + Vector((r * math.cos(a), r * 0.8 * math.sin(a), rnd.uniform(0.04, 0.12))); e.radius = rnd.uniform(0.12, 0.17)
    for k in range(4):
        e = mb.elements.new(); e.co = c + Vector((rnd.uniform(-0.12, 0.12), rnd.uniform(-0.1, 0.1), 0.1)); e.radius = 0.2
    bpy.context.view_layer.update()
    bpy.ops.object.select_all(action='DESELECT'); o.select_set(True); bpy.context.view_layer.objects.active = o
    bpy.ops.object.convert(target='MESH'); o = bpy.context.object; o.name = name
    o.data.materials.clear(); o.data.materials.append(mat)
    out = [o]
    for k in range(cherubs):   # (heads in front)
        a = -math.pi / 2 + (k - (cherubs - 1) / 2) * 0.55
        p = c + Vector(((r + 0.05) * math.cos(a), (r + 0.05) * 0.8 * math.sin(a), 0.12))
        bpy.ops.mesh.primitive_uv_sphere_add(radius=0.055, segments=16, ring_count=10, location=p); h = bpy.context.object
        h.data.materials.append(flesh); out.append(h)
        for sx in (-1, 1):
            bpy.ops.mesh.primitive_uv_sphere_add(radius=0.06, segments=12, ring_count=8, location=p + Vector((sx * 0.07, 0.01, 0.02)))
            w = bpy.context.object; w.scale = (1.0, 0.3, 0.45); w.rotation_euler = (0, sx * 0.4, 0); w.data.materials.append(mat); out.append(w)
    return out

def eye_uv(eye):
    """the glass eyes: a projection from the front, the iris and pupil in the middle of their texture"""
    me = eye.data
    if not me.uv_layers: me.uv_layers.new(name='UVMap')
    uv = me.uv_layers[0]
    # (each eye's centre: its vertices split by side)
    L = [v.co for v in me.vertices if v.co.x > 0]; R = [v.co for v in me.vertices if v.co.x <= 0]
    cL = sum(L, Vector()) / max(1, len(L)); cR = sum(R, Vector()) / max(1, len(R))
    rad = max((v - cL).length for v in L) if L else 0.012
    for poly in me.polygons:
        for li in poly.loop_indices:
            co = me.vertices[me.loops[li].vertex_index].co; c = cL if co.x > 0 else cR
            d = (co - c) / rad
            uv.data[li].uv = (0.5 + 0.5 * d.x, 0.5 + 0.5 * d.z) if d.y < 0 else (0.02, 0.02)

def join(name, obs):
    bpy.ops.object.select_all(action='DESELECT')
    for o in obs: o.select_set(True)
    bpy.context.view_layer.objects.active = obs[0]
    bpy.ops.object.join(); o = bpy.context.object; o.name = name
    return o

# ---------------------------------------------------------------- the polychromy (for the looks here; the game dresses
# the figures by these names)
PAINT = {
    'encarnado': ((0.78, 0.56, 0.44), 0.42, 0.0), 'ojo': ((0.9, 0.88, 0.84), 0.15, 0.0),
    'tunica_blanca': ((0.86, 0.84, 0.78), 0.55, 0.0), 'manto_azul': ((0.08, 0.14, 0.42), 0.5, 0.0),
    'forro_oro': ((0.8, 0.58, 0.24), 0.35, 0.9), 'velo': ((0.9, 0.89, 0.85), 0.6, 0.0),
    'dorado': ((0.9, 0.68, 0.3), 0.3, 1.0), 'nube': ((0.82, 0.83, 0.86), 0.7, 0.0), 'pelo': ((0.16, 0.09, 0.05), 0.6, 0.0),
    'tunica_negra': ((0.03, 0.03, 0.035), 0.55, 0.0), 'manto_negro': ((0.025, 0.025, 0.03), 0.5, 0.0), 'forro_rojo': ((0.4, 0.04, 0.05), 0.6, 0.0),
    'toca': ((0.9, 0.89, 0.86), 0.6, 0.0), 'plata': ((0.85, 0.86, 0.88), 0.25, 1.0), 'tunica_roja': ((0.45, 0.05, 0.06), 0.55, 0.0),
    'manto_crema': ((0.82, 0.74, 0.58), 0.55, 0.0), 'tunica_morada': ((0.25, 0.12, 0.28), 0.55, 0.0), 'manto_ocre': ((0.62, 0.42, 0.14), 0.45, 0.3),
    'pano': ((0.88, 0.86, 0.8), 0.6, 0.0), 'madera_cruz': ((0.18, 0.1, 0.05), 0.6, 0.0), 'corazon': ((0.55, 0.04, 0.05), 0.35, 0.0),
    'lirio': ((0.92, 0.91, 0.86), 0.6, 0.0),
}
def paint(name):
    col, rough, metal = PAINT[name]
    m = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    m.use_nodes = True; p = m.node_tree.nodes['Principled BSDF']
    p.inputs['Base Color'].default_value = (*col, 1); p.inputs['Roughness'].default_value = rough; p.inputs['Metallic'].default_value = metal
    return m

def virgen():
    """the Virgin of the retablo: standing on clouds among cherubs, her hands joined, a white tunic, a veil, the blue
    mantle lined in gold over her shoulders, crowned"""
    body, rig = build_body('virgen', female=True)
    pose(rig, 'manos_juntas')
    bend(rig, 'neck01', (1, 0, 0), 0.12)   # (her head a little bowed)
    bpy.context.view_layer.update()
    bake_pose(body)
    floor = min(v.co.z for v in body.data.vertices)
    up, sk, zw = tunic(body, floor, rig)
    eyes = part(body, 'ojo', 'virgen_ojos'); eye_uv(eyes)
    keep_only(body, 'carne')
    for o, m in ((body, 'encarnado'), (eyes, 'ojo'), (up, 'tunica_blanca'), (sk, 'tunica_blanca')):
        o.data.materials.clear(); o.data.materials.append(paint(m))
    coll = join('virgen_choque', [o.copy() for o in ()] or [body]) if False else body
    hr = hair(body, rig, 'virgen', female=True)   # (her hair, parted, under the veil)
    vl, pins = veil('virgen_velo', rig, body)
    drape(vl, body, pins, frames=50, mass=0.15, stiff=6.0, thick=0.006, others=hr)
    vl.data.materials.clear(); vl.data.materials.append(paint('velo'))
    mt, mpins = mantle2('virgen_manto', rig, floor)
    drape(mt, body, mpins, frames=80, mass=0.4, stiff=10.0, thick=0.001)
    lined(mt, paint('manto_azul'), paint('forro_oro'), thick=0.012)
    hd = joint(rig, 'head', 'tail')
    cr = crown('virgen_corona', (hd.x, hd.y + 0.015, hd.z - 0.035), r=0.1, h=0.13, mat=paint('dorado'))
    cl = clouds('virgen_nubes', (0, 0, floor - 0.2), mat=paint('nube'), flesh=paint('encarnado'))
    parts = [body, eyes, up, sk, vl, mt] + hr + cr + cl
    fig = join('virgen', parts)
    # (its feet on the floor of its place: the clouds' foot at 0)
    zmin = min(v.co.z for v in fig.data.vertices)
    for v in fig.data.vertices: v.co.z -= zmin
    bpy.data.objects.remove(rig)
    return fig

def head_info(rig):
    hd = joint(rig, 'head', 'tail'); hb = joint(rig, 'head', 'head')
    el, er = joint(rig, 'eye.L'), joint(rig, 'eye.R'); jw = joint(rig, 'jaw', 'tail')
    return hd, hb, (el + er) / 2, jw

def grown(bm, lift, edge=0.02):
    """a cut of the skin lifted off it by lift(v) — but grown out of it: its edge's steps smoothed along the cut, and the
    lift brought down to nothing over the last `edge` metres, as hair and beard grow from the skin, no rim"""
    ring = [v for v in bm.verts if any(e.is_boundary for e in v.link_edges)]
    rs = set(ring)
    for _ in range(8):
        new = {}
        for v in ring:
            nb = [e.other_vert(v) for e in v.link_edges if e.is_boundary and e.other_vert(v) in rs]
            if len(nb) == 2: new[v] = v.co * 0.5 + (nb[0].co + nb[1].co) * 0.25
        for v, c in new.items(): v.co = c
    from mathutils.kdtree import KDTree
    kd = KDTree(max(1, len(ring)))
    for i, v in enumerate(ring): kd.insert(v.co, i)
    kd.balance(); bm.normal_update()
    moves = []
    for v in bm.verts:
        d = kd.find(v.co)[2] if ring else 1.0
        t = min(1.0, d / edge); t = t * t * (3 - 2 * t)
        moves.append((v, v.normal * (lift(v) * t)))
    for v, m in moves: v.co += m

def hair(body, rig, name, long=False, beard=False, seed=5, female=False):
    """the hair, carved: the scalp's own faces lifted off the head in locks — parted in the middle, falling in waves to
    the sides, the grooves between them cut deep — grown out of the skin at the hairline; long, a fall behind to the
    shoulders; the beard over the jaw, in curls. Their faces copied from the head, so it fits"""
    import random
    rnd = random.Random(seed)
    hd, hb, eye, jw = head_info(rig)
    me = body.data
    def region(test):
        bm = bmesh.new(); bm.from_mesh(me); bm.normal_update()
        bmesh.ops.delete(bm, geom=[f for f in bm.faces if not test(f.calc_center_median())], context='FACES')
        loose = [v for v in bm.verts if not v.link_faces]; bmesh.ops.delete(bm, geom=loose, context='VERTS')
        return bm
    out = []
    # the scalp: behind the hairline — high in the middle of the forehead, lower at the temples — and over the ears
    front = eye.y - 0.02; mid = 0.06 if female else 0.055
    line = lambda x: eye.z + mid - 0.022 * min(1.0, (abs(x - eye.x) / 0.06) ** 2)
    bm = region(lambda c: (c.z > line(c.x) and c.y > front - 0.05) or (c.z > eye.z - 0.06 and c.y > eye.y + 0.06 and c.z < hd.z + 0.01 and abs(c.x - eye.x) < 0.11))
    cx, cy = eye.x, eye.y + 0.08
    k = 0.7 if female else 1.0
    def locks(v):
        a = math.atan2(v.co.x - cx, -(v.co.y - cy))                       # (0 straight in front: the parting)
        ph = abs(a) * 24 + 1.8 * math.sin((hd.z - v.co.z) * 28 + a * 2)  # (the locks: from the parting, waving down)
        lump = 0.5 + 0.5 * math.sin(v.co.x * 90 + rnd.uniform(0, 0.4)) * math.sin(v.co.z * 70 + v.co.y * 40)
        return k * (0.006 + 0.007 * (0.5 + 0.5 * math.cos(ph)) ** 0.7 + 0.003 * lump)
    grown(bm, locks, 0.022)
    me2 = bpy.data.meshes.new(name + '_pelo'); bm.to_mesh(me2); bm.free()
    o = bpy.data.objects.new(name + '_pelo', me2); COLL.objects.link(o); out.append(o)
    if long:   # (a fall of hair behind, from the nape to the shoulders: a sheet, let fall on them)
        sl, sr = joint(rig, 'upperarm01.L'), joint(rig, 'upperarm01.R')
        n, m = 24, 20; rows = []
        for j in range(m + 1):
            t = j / m; z = eye.z + 0.02 - (eye.z + 0.02 - (sl.z - 0.06)) * t
            w = 0.09 + 0.05 * t
            rows.append([Vector((eye.x - w + 2 * w * i / n, hb.y + 0.075 + 0.02 * t, z)) for i in range(n + 1)])
        sh = grid_mesh(name + '_melena', rows)
        drape(sh, body, list(range(n + 1)), frames=40, mass=0.3, stiff=20.0, thick=0.02)
        out.append(sh)
    if beard:   # (the lower face: the cheeks below the mouth's corners and the chin, lifted in curls)
        bm = region(lambda c: c.z < eye.z - 0.075 and c.z > jw.z - 0.035 and c.y < eye.y + 0.06 and abs(c.x - eye.x) < 0.07 and not (abs(c.x - eye.x) < 0.025 and c.z > eye.z - 0.1))
        grown(bm, lambda v: 0.008 + 0.006 * (0.5 + 0.5 * math.sin(v.co.x * 120) * math.sin(v.co.z * 110)), 0.015)
        me3 = bpy.data.meshes.new(name + '_barba'); bm.to_mesh(me3); bm.free()
        o3 = bpy.data.objects.new(name + '_barba', me3); COLL.objects.link(o3); out.append(o3)
    for o in out:
        if o.name.endswith('_melena'): continue
        mods(o, ('SOLIDIFY', {'thickness': 0.006, 'offset': -1.0}), ('SUBSURF', {'levels': 1}))
    for o in out: o.data.materials.clear(); o.data.materials.append(paint('pelo'))
    return out

def rays(name, centre, n=24, r0=0.13, r1=0.3, mat=None, ring=True, facing=Vector((0, -1, 0))):
    """a resplendence behind the head: a ring and its rays, long and short"""
    out = []
    c = Vector(centre)
    up = Vector((0, 0, 1)); side = facing.cross(up).normalized()
    if ring:
        bpy.ops.mesh.primitive_torus_add(major_radius=r0, minor_radius=0.006, major_segments=48, minor_segments=8, location=c)
        t = bpy.context.object; t.rotation_euler = (math.pi / 2, 0, 0); out.append(t)
    for k in range(n):
        a = 2 * math.pi * k / n; L = r1 if k % 2 == 0 else r1 * 0.72
        d = side * math.cos(a) + up * math.sin(a)
        p0 = c + d * (r0 + 0.01); p1 = c + d * L
        bpy.ops.mesh.primitive_cone_add(vertices=4, radius1=0.008, radius2=0.0, depth=(p1 - p0).length, location=(p0 + p1) / 2)
        o = bpy.context.object; o.rotation_euler = d.to_track_quat('Z', 'Y').to_euler(); out.append(o)
    for o in out: o.data.materials.clear(); o.data.materials.append(mat)
    return out

def on_breast(cloth, at, out=0.02):
    """the point of the breast's cloth straight before `at` (a ray from the front), brought out by `out`"""
    ok, hit, nrm, _ = cloth.ray_cast(Vector((at.x, at.y - 0.8, at.z)), Vector((0, 1, 0)))
    return (hit if ok else at + Vector((0, -0.16, 0))) + Vector((0, -out, 0))

def rod(name, p0, p1, r, mat, verts=8):
    """a round bar from p0 to p1"""
    d = p1 - p0
    bpy.ops.mesh.primitive_cylinder_add(vertices=verts, radius=r, depth=d.length, location=(p0 + p1) / 2)
    o = bpy.context.object; o.name = name; o.rotation_euler = d.to_track_quat('Z', 'Y').to_euler(); o.data.materials.append(mat)
    return o

def heart(name, c):
    """the Sacred Heart: its two lobes and its point, girt with the crown of thorns, flames out of its top and the
    little cross in them"""
    out = []
    for sx in (-1, 1):
        bpy.ops.mesh.primitive_uv_sphere_add(radius=0.03, segments=20, ring_count=12, location=c + Vector((sx * 0.021, 0, 0.012)))
        out.append(bpy.context.object)
    bpy.ops.mesh.primitive_cone_add(vertices=24, radius1=0.046, radius2=0.003, depth=0.066, location=c + Vector((0, 0, -0.028)), rotation=(math.pi, 0, 0))
    out.append(bpy.context.object)
    for o in out: o.scale = (1.0, 0.6, 1.0); o.data.materials.append(paint('corazon'))
    bpy.ops.mesh.primitive_torus_add(major_radius=0.047, minor_radius=0.005, major_segments=40, minor_segments=8, location=c + Vector((0, 0, 0.004)))
    t = bpy.context.object; t.scale = (1.0, 0.66, 1.0); t.data.materials.append(paint('madera_cruz')); out.append(t)
    bpy.ops.mesh.primitive_cone_add(vertices=10, radius1=0.02, radius2=0.0, depth=0.06, location=c + Vector((0, 0, 0.062)))
    f = bpy.context.object; f.data.materials.append(paint('dorado')); out.append(f)
    out.append(rod(name + '_cruz', c + Vector((0, 0, 0.08)), c + Vector((0, 0, 0.125)), 0.0035, paint('dorado')))
    out.append(rod(name + '_cruz2', c + Vector((-0.014, 0, 0.112)), c + Vector((0.014, 0, 0.112)), 0.0035, paint('dorado')))
    return out

def peana(name, r=0.3, h=0.16, mat=None):
    """a gilded base: a moulded drum on a plinth"""
    prof = [(0, 0), (r + 0.03, 0), (r + 0.03, 0.025), (r, 0.04), (r - 0.02, 0.07), (r - 0.04, h - 0.04), (r - 0.01, h - 0.02), (r, h), (0, h)]
    me = bpy.data.meshes.new(name); seg = 40; verts, faces = [], []
    for i, (rr, hh) in enumerate(prof):
        for k in range(seg): a = 2 * math.pi * k / seg; verts.append((rr * math.cos(a), rr * math.sin(a) * 0.8, hh))
    for i in range(len(prof) - 1):
        for k in range(seg): faces.append((i * seg + k, i * seg + (k + 1) % seg, (i + 1) * seg + (k + 1) % seg, (i + 1) * seg + k))
    me.from_pydata(verts, [], faces); o = bpy.data.objects.new(name, me); COLL.objects.link(o)
    o.data.materials.append(mat)
    return o, h

def finish(name, parts, base_h=0.0):
    fig = join(name, parts)
    zmin = min(v.co.z for v in fig.data.vertices)
    for v in fig.data.vertices: v.co.z -= zmin
    return fig

def figure(name, female, pose_name, tunic_m, mantle_m, lining_m, veil_m=None, tilt=0.1, turn=0.0, long_hair=False, beard=False, hood=False):
    """a standing figure: posed, its tunic, its mantle (and veil, or hair), on a gilded base"""
    body, rig = build_body(name, female=female, weight=0.35 if female else 0.42)
    pose(rig, pose_name)
    if tilt: bend(rig, 'neck01', (1, 0, 0), tilt)
    if turn: bend(rig, 'neck01', (0, 0, 1), turn)
    bake_pose(body)
    floor = min(v.co.z for v in body.data.vertices)
    up, sk, zw = tunic(body, floor, rig)
    eyes = part(body, 'ojo', name + '_ojos'); eye_uv(eyes)
    keep_only(body, 'carne')
    for o, m in ((body, 'encarnado'), (eyes, 'ojo'), (up, tunic_m), (sk, tunic_m)):
        o.data.materials.clear(); o.data.materials.append(paint(m))
    parts = [body, eyes, up, sk]
    if veil_m:
        hr = hair(body, rig, name, female=True); parts += hr   # (her hair, parted, under the veil)
        vl, pins = veil(name + '_velo', rig, body)
        drape(vl, body, pins, frames=50, mass=0.15, stiff=6.0, thick=0.006, others=hr)
        vl.data.materials.clear(); vl.data.materials.append(paint(veil_m)); parts.append(vl)
    else:
        parts += hair(body, rig, name, long=long_hair, beard=beard)
    mt, mpins = mantle2(name + '_manto', rig, floor)
    drape(mt, body, mpins, frames=80, mass=0.4, stiff=10.0, thick=0.001)
    lined(mt, paint(mantle_m), paint(lining_m), thick=0.012); parts.append(mt)
    return body, rig, parts, floor

def inmaculada():
    body, rig, parts, floor = figure('inmaculada', True, 'manos_juntas', 'tunica_blanca', 'manto_azul', 'forro_oro', 'velo', tilt=0.16)
    hd, hb, eye, jw = head_info(rig)
    # twelve stars round her head
    for k in range(12):
        a = 2 * math.pi * k / 12
        c = Vector((hd.x + 0.2 * math.cos(a), hd.y + 0.03, hd.z - 0.02 + 0.2 * math.sin(a)))
        bpy.ops.mesh.primitive_cone_add(vertices=5, radius1=0.025, radius2=0.0, depth=0.01, location=c, rotation=(math.pi / 2, 0, 0))
        st = bpy.context.object; st.data.materials.append(paint('dorado')); parts.append(st)
    # the crescent moon under her feet, on clouds with cherubs
    bpy.ops.mesh.primitive_torus_add(major_radius=0.3, minor_radius=0.05, major_segments=48, minor_segments=12, location=(0, 0, floor - 0.02))
    mo = bpy.context.object; mo.scale = (1.0, 0.75, 0.6)
    bm = bmesh.new(); bm.from_mesh(mo.data); bmesh.ops.delete(bm, geom=[v for v in bm.verts if v.co.y < -0.12], context='VERTS'); bm.to_mesh(mo.data); bm.free()
    mo.data.materials.append(paint('plata')); parts.append(mo)
    parts += clouds('inmaculada_nubes', (0, 0, floor - 0.22), mat=paint('nube'), flesh=paint('encarnado'), seed=9)
    bpy.data.objects.remove(rig)
    return finish('inmaculada', parts)

def dolorosa():
    body, rig, parts, floor = figure('dolorosa', True, 'manos_juntas', 'tunica_negra', 'manto_negro', 'forro_rojo', 'toca', tilt=-0.18, turn=0.12)
    hd, hb, eye, jw = head_info(rig)
    parts += rays('dolorosa_resplandor', (hd.x, hd.y + 0.09, hd.z - 0.04), n=28, r0=0.15, r1=0.34, mat=paint('plata'))
    # the dagger in her breast
    sp = joint(rig, 'spine02', 'tail')
    e = on_breast(parts[2], Vector((sp.x + 0.06, sp.y, sp.z + 0.04)), 0.0)
    d = Vector((0.4, -0.5, 0.75)).normalized()        # (the hilt's way out: up, forwards, to her left)
    sd = d.cross(Vector((0, -1, 0))).normalized()
    g = e + d * 0.025
    parts += [rod('dolorosa_hoja', e - d * 0.02, g, 0.005, paint('plata'), 4), rod('dolorosa_guarda', g - sd * 0.03, g + sd * 0.03, 0.0045, paint('plata')),
              rod('dolorosa_puno', g, g + d * 0.065, 0.006, paint('plata'))]
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.01, segments=12, ring_count=8, location=g + d * 0.072)
    pm = bpy.context.object; pm.data.materials.append(paint('plata')); parts.append(pm)
    pe, ph = peana('dolorosa_peana', mat=paint('dorado'))
    for v in pe.data.vertices: v.co.z += floor - ph
    parts.append(pe)
    bpy.data.objects.remove(rig)
    return finish('dolorosa', parts)

def corazon():
    body, rig, parts, floor = figure('corazon', False, 'corazon', 'tunica_roja', 'manto_crema', 'forro_oro', tilt=0.1, long_hair=True, beard=True)
    hd, hb, eye, jw = head_info(rig)
    parts += rays('corazon_resplandor', (hd.x, hd.y + 0.09, hd.z - 0.05), n=3 * 4, r0=0.0, r1=0.26, mat=paint('dorado'), ring=False)
    # the heart on his breast, in flames, a little cross over it
    sp = joint(rig, 'spine02', 'tail')
    parts += heart('corazon_corazon', on_breast(parts[2], Vector((sp.x + 0.05, sp.y, sp.z + 0.03)), 0.022))
    pe, ph = peana('corazon_peana', mat=paint('dorado'))
    for v in pe.data.vertices: v.co.z += floor - ph
    parts.append(pe)
    bpy.data.objects.remove(rig)
    return finish('corazon', parts)

def jose():
    body, rig, parts, floor = figure('jose', False, 'jose', 'tunica_morada', 'manto_ocre', 'forro_oro', tilt=0.18, turn=0.15, long_hair=False, beard=True)
    hd, hb, eye, jw = head_info(rig)
    parts += rays('jose_resplandor', (hd.x, hd.y + 0.09, hd.z - 0.04), n=24, r0=0.14, r1=0.26, mat=paint('dorado'))
    # the Child, sitting on his left forearm
    la = joint(rig, 'lowerarm01.L', 'tail')
    child, crig = build_body('jose_nino', female=False, weight=0.6)
    for bn, sc in (('head', 1.55), ('neck01', 1.2)):
        pb = crig.pose.bones[bn]; pb.scale = (sc, sc, sc)
    pose(crig, 'nino')
    for leg in ('upperleg01.L', 'upperleg01.R'): aim(crig, leg, (0, -1, -0.15))
    for leg in ('lowerleg01.L', 'lowerleg01.R'): aim(crig, leg, (0, -0.2, -1))
    bake_pose(child)
    ch_eyes = part(child, 'ojo', 'jose_nino_ojos'); eye_uv(ch_eyes)
    loin = part(child, 'falda', 'jose_nino_pano')
    keep_only(child, 'carne')
    child.data.materials.clear(); child.data.materials.append(paint('encarnado'))
    ch_eyes.data.materials.clear(); ch_eyes.data.materials.append(paint('ojo'))
    bm = bmesh.new(); bm.from_mesh(loin.data); zt = max(v.co.z for v in bm.verts)
    bmesh.ops.delete(bm, geom=[v for v in bm.verts if v.co.z < zt - 0.22], context='VERTS'); bm.normal_update()
    for v in bm.verts: v.co += v.normal * 0.012
    bm.to_mesh(loin.data); bm.free(); loin.data.materials.clear(); loin.data.materials.append(paint('pano'))
    cp = [child, ch_eyes, loin]
    for o in cp:
        o.scale = (0.36, 0.36, 0.36); o.location = la + Vector((0.05, -0.08, 0.06))
        bpy.context.view_layer.objects.active = o; o.select_set(True); bpy.ops.object.transform_apply(location=True, scale=True); o.select_set(False)
    parts += cp
    bpy.data.objects.remove(crig)
    # the flowering staff in his right hand
    rw = joint(rig, 'wrist.R', 'tail')
    bpy.ops.mesh.primitive_cylinder_add(vertices=8, radius=0.012, depth=1.5, location=(rw.x, rw.y, rw.z + 0.2))
    stf = bpy.context.object; stf.data.materials.append(paint('dorado')); parts.append(stf)
    for k in range(5):
        bpy.ops.mesh.primitive_cone_add(vertices=6, radius1=0.035, radius2=0.004, depth=0.07, location=(rw.x + 0.03 * math.cos(k * 1.3), rw.y + 0.03 * math.sin(k * 1.3), rw.z + 0.95 + 0.05 * k), rotation=(math.pi, 0, 0))
        fl = bpy.context.object; fl.data.materials.append(paint('lirio')); parts.append(fl)
    pe, ph = peana('jose_peana', mat=paint('dorado'))
    for v in pe.data.vertices: v.co.z += floor - ph
    parts.append(pe)
    bpy.data.objects.remove(rig)
    return finish('jose', parts)

def cristo():
    """Christ on the cross: his arms spread, his head bowed on his right shoulder, the loincloth knotted at his hip, the
    crown of thorns; the cross of dark wood with its title"""
    body, rig = build_body('cristo', female=False, weight=0.3)
    pose(rig, 'cruz')
    bend(rig, 'neck01', (1, 0, 0), 0.26); bend(rig, 'neck01', (0, 1, 0), 0.24); stretch_neck(rig, 0.025)
    for leg, d in (('upperleg01.L', (0.03, -0.22, -1)), ('upperleg01.R', (-0.03, -0.22, -1)), ('lowerleg01.L', (-0.02, 0.12, -1)), ('lowerleg01.R', (0.02, 0.12, -1))):
        aim(rig, leg, d)
    bake_pose(body)
    floor = min(v.co.z for v in body.data.vertices)
    eyes = part(body, 'ojo', 'cristo_ojos'); eye_uv(eyes)
    loin = part(body, 'falda', 'cristo_pano')
    bm = bmesh.new(); bm.from_mesh(loin.data); zt = max(v.co.z for v in bm.verts)
    bmesh.ops.delete(bm, geom=[v for v in bm.verts if v.co.z < zt - 0.32 or v.co.z > zt - 0.02], context='VERTS'); bm.normal_update()
    for v in bm.verts: v.co += v.normal * (0.018 + 0.01 * math.sin(v.co.x * 60 + v.co.z * 30) ** 2)
    bm.to_mesh(loin.data); bm.free()
    mods(loin, ('SUBSURF', {'levels': 1}), ('SOLIDIFY', {'thickness': 0.006, 'offset': 1.0}))
    keep_only(body, 'carne')
    body.data.materials.clear(); body.data.materials.append(paint('encarnado'))
    eyes.data.materials.clear(); eyes.data.materials.append(paint('ojo'))
    loin.data.materials.clear(); loin.data.materials.append(paint('pano'))
    parts = [body, eyes, loin] + hair(body, rig, 'cristo', long=True, beard=True)
    hd, hb, eye, jw = head_info(rig)
    bpy.ops.mesh.primitive_torus_add(major_radius=0.105, minor_radius=0.012, major_segments=40, minor_segments=8, location=(hd.x, hd.y + 0.01, hd.z - 0.045))
    cr = bpy.context.object; cr.rotation_euler = (0.35, 0.28, 0); cr.data.materials.append(paint('pelo')); parts.append(cr)
    # the cross: its foot below his feet, the arms behind his hands
    hl, hr = joint(rig, 'wrist.L', 'tail'), joint(rig, 'wrist.R', 'tail')
    cy = max(v.co.y for v in body.data.vertices) + 0.07
    top = hd.z + 0.45; arm_z = (hl.z + hr.z) / 2
    for nm, c, sc in (('cruz_palo', (0, cy, (floor - 0.3 + top) / 2), (0.075, 0.055, (top - floor + 0.3) / 2)), ('cruz_brazo', (0, cy, arm_z), ((abs(hl.x - hr.x) / 2 + 0.25), 0.055, 0.07))):
        bpy.ops.mesh.primitive_cube_add(size=2, location=c); o = bpy.context.object; o.scale = sc; o.name = nm
        mods(o, ('BEVEL', {'width': 0.008, 'segments': 2}))
        o.data.materials.append(paint('madera_cruz')); parts.append(o)
    bpy.ops.mesh.primitive_cube_add(size=2, location=(0, cy - 0.06, top - 0.12)); o = bpy.context.object; o.scale = (0.16, 0.01, 0.07)
    o.data.materials.append(paint('tunica_blanca')); parts.append(o)
    bpy.data.objects.remove(rig)
    return finish('cristo', parts)

FIGURES = {'virgen': virgen, 'inmaculada': inmaculada, 'dolorosa': dolorosa, 'corazon': corazon, 'jose': jose, 'cristo': cristo}

def bake_ao(fig, samples=64):
    """the occlusion of the folds and hollows, baked into the figure's vertices (its colour attribute 'AO', the glTF's
    COLOR_0: the game darkens the probes' light by it)"""
    SC.render.engine = 'CYCLES'; SC.cycles.device = 'CPU'; SC.cycles.samples = samples
    me = fig.data
    for a in list(me.color_attributes): me.color_attributes.remove(a)
    ca = me.color_attributes.new('AO', 'BYTE_COLOR', 'POINT'); me.color_attributes.active_color = ca
    bpy.ops.object.select_all(action='DESELECT'); fig.select_set(True); bpy.context.view_layer.objects.active = fig
    SC.render.bake.target = 'VERTEX_COLORS'
    bpy.ops.object.bake(type='AO')
    SC.render.bake.target = 'IMAGE_TEXTURES'

def export(figs, path):
    bpy.ops.object.select_all(action='DESELECT')
    for f in figs: f.select_set(True)
    bpy.ops.export_scene.gltf(filepath=path, export_format='GLB', use_selection=True, export_yup=True, export_apply=True,
                              export_texcoords=True, export_normals=True, export_materials='EXPORT', export_vertex_color='ACTIVE',
                              export_all_vertex_colors=False, export_meshopt_compression_enable=True)

if __name__ == '__main__':
    bpy.ops.wm.read_factory_settings(use_empty=True)
    SC = bpy.context.scene; COLL = SC.collection
    made = []
    for k, f in FIGURES.items():
        if ONLY and k not in ONLY: continue
        fig = f()
        # (each figure apart from the others, side by side, for the looks; the game places them by their names)
        fig.location.x = len(made) * 1.4
        made.append(fig)
        print(f'imagenes: {k} hecha, {len(fig.data.polygons)} caras', flush=True)
    if '--exportar' in ARGS:
        for fig in made:
            dec = fig.modifiers.new('menos', 'DECIMATE'); dec.ratio = float(arg('--diezmar', '0.35'))
            bpy.context.view_layer.objects.active = fig; bpy.ops.object.modifier_apply(modifier=dec.name)
            bake_ao(fig)
            fig.location.x = 0
        os.makedirs(OUT, exist_ok=True)
        path = os.path.join(OUT, 'imagenes.glb'); export(made, path)
        print(f'imagenes: {sum(len(f.data.polygons) for f in made)} caras → {path} ({os.path.getsize(path) // 1024} KB)', flush=True)
    if arg('--vista'):
        fig = made[0]; zt = max(v.co.z for v in fig.data.vertices)
        vista(os.path.abspath(arg('--vista')), (0, 0, zt * 0.55), dist=3.0, height=zt * 0.6)
