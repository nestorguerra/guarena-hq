# The textures of Santa María inside (docs/hiperrealismo.md, «El interior (fase 6)»), made in Blender's Python (numpy)
# from the CC0 scans in .cache (ambientCG, Poly Haven) into assets/hq/interior/tex as seamless JPEG tiles, the only
# copies that ship (the game loads them beside the model: hiperinterior.js):
#   /Applications/Blender.app/Contents/MacOS/Blender --background --factory-startup --python tools/blender/texturas_interior.py
# - cal (1,4 m): the whitewash — ambientCG's «Plaster003» limed: an even, faintly warm white, the trowel's passes and a
#   few greyer patches of older coats left in it;
# - granito (0,7 m): the grey granite of the columns, arches and ribs — ambientCG's «Granite002A», grey with black mica
#   and white feldspar, as it is; the scan is of a polished worktop: here it is matt and tooled (its relief made from
#   its own crystals, a fine pitting over them);
# - suelo (4,1 m): the floor's slabs of grey granite (the user: «losas de granito gris») in courses across the nave, each
#   slab 0,7–1,3 m long and its own piece of the granite, darker with the years and polished by feet, its arrises worn;
#   the scratches and wear of Poly Haven's «Large Floor Tiles 02» over them;
# - vidrio (1 m): the windows' leaded glass — clear panes, faintly green or amber, seeded with bubbles, in lead cames.
# Albedo in sRGB; normal (OpenGL, +Y up) and roughness linear. Credit: ambientCG (ambientcg.com) and Poly Haven
# (polyhaven.com), CC0.
import bpy, numpy as np, os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SRC = os.path.join(ROOT, '.cache')
OUT = os.path.join(ROOT, 'assets', 'hq', 'interior', 'tex')
os.makedirs(OUT, exist_ok=True)

def load(rel, res):
    """a scan as a float array (rows down), averaged down to res"""
    img = bpy.data.images.load(os.path.join(SRC, rel)); img.colorspace_settings.name = 'Non-Color'
    w, h = img.size; px = np.empty(w * h * 4, np.float32); img.pixels.foreach_get(px)
    a = px.reshape(h, w, 4)[::-1, :, :3]
    k = w // res
    return a.reshape(res, k, res, k, 3).mean((1, 3)) if k > 1 else a

def save(name, arr, srgb, res, quality=86):
    """a JPEG (resized to res), its colour space as given"""
    n = arr.shape[0]
    img = bpy.data.images.new(name, n, n, alpha=False); img.colorspace_settings.name = 'sRGB' if srgb else 'Non-Color'
    if arr.ndim == 2: arr = np.repeat(arr[..., None], 3, -1)
    img.pixels.foreach_set(np.concatenate([arr[::-1], np.ones((n, n, 1))], -1).astype(np.float32).ravel())
    if res != n: img.scale(res, res)
    img.file_format = 'JPEG'
    img.save(filepath=os.path.join(OUT, name + '.jpg'), quality=quality)
    print(f'  {name}.jpg {res}px {os.path.getsize(os.path.join(OUT, name + ".jpg")) // 1024} KB', flush=True)

def to_srgb(a):
    a = np.clip(a, 0, 1)
    return np.where(a <= 0.0031308, a * 12.92, 1.055 * np.power(a, 1 / 2.4) - 0.055)

def to_lin(a):
    return np.where(a <= 0.04045, a / 12.92, np.power((a + 0.055) / 1.055, 2.4))

def blur(a, r):
    """a wrap-around box blur, three times (≈ gaussian)"""
    for _ in range(3):
        for ax in (0, 1):
            c = np.cumsum(np.concatenate([a.take(range(-r, 0), ax), a, a.take(range(0, r + 1), ax)], ax), ax)
            n = a.shape[ax]
            a = (c.take(range(2 * r + 1, n + 2 * r + 1), ax) - c.take(range(0, n), ax)) / (2 * r + 1)
    return a

def normals(h, metres):
    """a tangent-space normal map from a height field (metres over the tile), wrapping round"""
    px = metres / h.shape[0]
    dx = (np.roll(h, -1, 1) - np.roll(h, 1, 1)) / (2 * px); dy = (np.roll(h, -1, 0) - np.roll(h, 1, 0)) / (2 * px)
    n = np.stack([-dx, dy, np.ones_like(h)], -1)
    return n / np.linalg.norm(n, axis=-1, keepdims=True)

LUM = np.array([0.2126, 0.7152, 0.0722])

# ---------------------------------------------------------------- cal (the whitewash)
def cal(res=2048):
    d = to_lin(load('ambientcg/Plaster003/Plaster003_2K-JPG_Color.jpg', res))
    L = d @ LUM
    # (the scan's patches of a greyer coat stay, faint; its overall grey goes to the lime's white)
    rel = L / L.mean()
    broad = blur(rel, res // 40)
    fine = rel - broad
    white = np.array([0.77, 0.775, 0.785])   # (a neutral, faintly cool white: the photo's walls are grey, not cream)
    v = 1 + 0.45 * (broad - 1) + 0.6 * fine
    alb = white[None, None] * v[..., None]
    alb = np.clip(alb, 0, 0.9)
    nor = load('ambientcg/Plaster003/Plaster003_2K-JPG_NormalGL.jpg', res) * 2 - 1
    # (the trowel's relief a little softer: lime laid over the years fills it)
    nor[..., :2] *= 0.7; nor /= np.linalg.norm(nor, axis=-1, keepdims=True)
    rough = np.clip(0.86 + 0.08 * (load('ambientcg/Plaster003/Plaster003_2K-JPG_Roughness.jpg', res)[..., 0] - 0.5), 0.78, 0.97)
    print(f'  cal: albedo medio {alb.mean(axis=(0, 1)).round(3)}')
    save('cal_diff', to_srgb(alb), True, 2048)
    save('cal_nor', nor * 0.5 + 0.5, False, 2048, 90)
    save('cal_rough', rough, False, 1024)

# ---------------------------------------------------------------- granito
def granite_base(res):
    """the granite's colour (linear) and its crystals' height, from the scan (its 2048 px over 0,7 m), at res px"""
    if res == 2048: d = load('ambientcg/Granite002A/Granite002A_2K-JPG_Color.jpg', res)
    else:
        img = bpy.data.images.load(os.path.join(SRC, 'ambientcg/Granite002A/Granite002A_2K-JPG_Color.jpg')); img.colorspace_settings.name = 'Non-Color'
        img.scale(res, res)  # (still seamless: the whole tile scaled)
        px = np.empty(res * res * 4, np.float32); img.pixels.foreach_get(px); d = px.reshape(res, res, 4)[::-1, :, :3]
    d = to_lin(d)
    return d, d @ LUM

def granito(res=2048):
    d, L = granite_base(res)
    # (weathered and tooled, not a polished worktop: its speckle half as contrasted and a little softened, its colour
    # all but gone — a light, neutral grey, as the photo's columns and arches; mean ≈ 0,56)
    m = L.mean()
    Ls = blur(L, 1)
    alb = (d - L[..., None]) * 0.2 + (m + (Ls - m) * 0.5)[..., None]
    alb = alb * (0.56 / alb.mean())
    alb = alb * np.array([0.995, 1.0, 1.01])
    # the tooled face: the crystals stand a fraction of a millimetre, the tool's fine pitting over them
    rng = np.random.default_rng(5)
    pits = blur(rng.standard_normal((res, res)).astype(np.float32), 1)
    hgt = (L - blur(L, res // 64)) * 0.0012 + pits * 0.00035
    nor = normals(hgt, 0.7)
    rough = np.clip(0.8 - 0.12 * (L - m) / (L.std() + 1e-6) * 0.25 + 0.03 * pits, 0.62, 0.92)
    print(f'  granito: albedo medio {alb.mean(axis=(0, 1)).round(3)}')
    save('granito_diff', to_srgb(alb), True, 1024)
    save('granito_nor', nor * 0.5 + 0.5, False, 1024, 90)
    save('granito_rough', rough, False, 512)

# ---------------------------------------------------------------- suelo (granite slabs)
def suelo(res=2048, tile=4.1):
    rng = np.random.default_rng(23)
    G = int(round(0.7 / (tile / res)))                            # (the granite at its own scale: 0,7 m)
    d, L = granite_base(G)
    gm = L.mean()
    grey = (d - L[..., None]) * 0.45 + L[..., None]               # (a little of the scan's colour: grey granite)
    gl = to_lin(load('polyhaven/large_floor_tiles_02_diff_2k.jpg', 2048)) @ LUM
    wear = gl - blur(gl, 2048 // 64); wear /= (np.abs(wear).max() + 1e-6)   # (the scan's scratches and scuffs, its slabs' grid gone)
    wn = load('polyhaven/large_floor_tiles_02_nor_gl_2k.jpg', 2048) * 2 - 1
    px = tile / res
    yy, xx = np.mgrid[0:res, 0:res]
    # the courses: across the nave (the image's rows run along x, its columns along z), each 0,55–0,75 m wide, the
    # widths adding up to the tile; along each, slabs of 0,7–1,3 m, their joints staggered
    widths = []
    while True:
        w = rng.uniform(0.55, 0.75)
        if sum(widths) + w > tile - 0.5: widths.append(tile - sum(widths)); break
        widths.append(w)
    ID = np.zeros((res, res), np.int32); EX = np.zeros((res, res), np.float32)
    sid = 0; y0 = 0.0; info = []
    for w in widths:
        r0, r1 = int(round(y0 / px)), int(round((y0 + w) / px))
        lens = []
        while True:
            L_ = rng.uniform(0.7, 1.3)
            if sum(lens) + L_ > tile - 0.6: lens.append(tile - sum(lens)); break
            lens.append(L_)
        off = rng.uniform(0, tile)
        x0 = off
        for L_ in lens:
            a, b = x0, x0 + L_
            cols = np.arange(res) * px
            inside = ((cols - a) % tile) < L_
            dx = np.minimum((cols - a) % tile, (b - cols) % tile)       # (distance to the slab's ends, along x)
            for r in range(r0, min(r1, res)):
                ID[r, inside] = sid
                dy = min(r * px - y0, y0 + w - r * px)
                EX[r, inside] = np.minimum(dx[inside], dy)
            info.append(sid); sid += 1; x0 += L_
        y0 += w
    n = sid
    tone = rng.uniform(0.78, 1.12, n); tone[rng.uniform(0, 1, n) < 0.08] *= 0.82        # (a few replaced, darker)
    warm = rng.uniform(-0.02, 0.03, n)
    oy, ox = rng.integers(0, G, n), rng.integers(0, G, n)
    gy = (yy + oy[ID]) % G; gx = (xx + ox[ID]) % G
    face = grey[gy, gx]
    alb = face * (0.27 / gm) * tone[ID][..., None] * (1 + np.stack([warm[ID], 0 * warm[ID], -warm[ID]], -1))
    alb = alb * (1 + 0.18 * wear[..., None])
    # the joints: 5 mm of dark mortar and dust; the arrises worn round over a centimetre
    joint = np.clip(1 - (EX - 0.0025) / 0.0015, 0, 1)
    alb = alb * (1 - joint[..., None]) + np.array([0.07, 0.065, 0.06])[None, None] * joint[..., None]
    bevel = np.clip(EX / 0.012, 0, 1)
    hgt = 0.004 * np.sqrt(bevel) + (L[gy, gx] - gm) * 0.0004 + 0.0004 * wear
    # (each slab not quite level: a millimetre or two of tilt)
    tx, ty = rng.uniform(-0.002, 0.002, n), rng.uniform(-0.002, 0.002, n)
    hgt = hgt + (xx * px) * tx[ID] + (yy * px) * ty[ID]
    nor = normals(hgt, tile)
    wn2 = wn[(yy + oy[ID]) % 2048, (xx + ox[ID]) % 2048]
    nor[..., :2] += 0.35 * wn2[..., :2]; nor /= np.linalg.norm(nor, axis=-1, keepdims=True)
    rough = np.clip(0.58 + 0.12 * (1 - tone[ID]) + 0.1 * wear + 0.3 * joint, 0.35, 0.95)
    print(f'  suelo: {n} losas en la tesela de {tile} m; albedo medio {alb.mean(axis=(0, 1)).round(3)}')
    save('suelo_diff', to_srgb(alb), True, 2048)
    save('suelo_nor', nor * 0.5 + 0.5, False, 2048, 90)
    save('suelo_rough', rough, False, 1024)

# ---------------------------------------------------------------- vidrio (leaded glass)
def vidrio(res=1024):
    rng = np.random.default_rng(8)
    # panes of 20 × 25 cm in a 1 m tile (5 × 4), the cames 1,2 cm wide
    nx, ny = 5, 4
    yy, xx = np.mgrid[0:res, 0:res] / res
    cx, cy = (xx * nx).astype(np.int32), (yy * ny).astype(np.int32)
    fx, fy = xx * nx - cx, yy * ny - cy
    ex = np.minimum(fx, 1 - fx) / nx; ey = np.minimum(fy, 1 - fy) / ny     # (metres to the came)
    e = np.minimum(ex, ey)
    lead = np.clip(1 - (e - 0.006) / 0.002, 0, 1)
    pid = cy * nx + cx
    tint = rng.uniform(0, 1, nx * ny)
    base = np.array([0.93, 0.95, 0.9])
    col = base[None, None] * np.ones((res, res, 1))
    green = np.array([0.86, 0.95, 0.86]); amber = np.array([0.98, 0.93, 0.8])
    t = tint[pid]
    col = np.where((t < 0.3)[..., None], green[None, None], np.where((t > 0.8)[..., None], amber[None, None], col))
    # (cylinder glass: a slight ripple, bubbles here and there)
    ripple = 0.03 * np.sin((yy * 37 + np.sin(xx * 23) * 0.4) * 6.283)
    bub = (blur(rng.standard_normal((res, res)).astype(np.float32), 1) > 2.6) * 0.15
    col = col * (1 + ripple[..., None] - bub[..., None])
    col = col * (1 - lead[..., None]) + np.array([0.04, 0.04, 0.045])[None, None] * lead[..., None]
    save('vidrio_diff', to_srgb(col * 0.95), True, res)

# ---------------------------------------------------------------- the furniture (6b): Poly Haven's CC0 scans,
# .cache/polyhaven/muebles_6b
def load_sq(rel, res, srgb_to_lin=False):
    """a scan scaled to res × res (some are not square), as floats (rows down)"""
    img = bpy.data.images.load(os.path.join(SRC, rel)); img.colorspace_settings.name = 'Non-Color'
    img.scale(res, res)
    px = np.empty(res * res * 4, np.float32); img.pixels.foreach_get(px)
    a = px.reshape(res, res, 4)[::-1, :, :3]
    return to_lin(a) if srgb_to_lin else a

def lum(a): return a @ np.array([0.2126, 0.7152, 0.0722])

def retint(lin, target, keep=0.25):
    """a scan's colour moved to `target` (linear): its own light and dark kept (luminance over its mean), and a little of
    its own colour (keep), brought to the target's brightness"""
    y = lum(lin); m = max(1e-6, float(y.mean()))
    t = np.array(target)[None, None] * (y / m)[..., None]
    own = lin * (float(lum(np.array(target))) / m)
    return t * (1 - keep) + own * keep

def madera(res=1024):
    """the pews' oak, stained dark (Poly Haven «Dark Wood», 2 m): its reddish mahogany brought to a dark walnut brown;
    varnished — a satin sheen, rougher where hands and years have dulled it"""
    D = 'polyhaven/muebles_6b/'
    alb = load_sq(D + 'dark_wood_diff_2k.jpg', res, True)
    alb = retint(alb, (0.12, 0.064, 0.032), keep=0.3)   # (a medium walnut: dark-stained oak, not black)
    arm = load_sq(D + 'dark_wood_arm_2k.jpg', res)
    alb *= (0.75 + 0.25 * arm[..., 0])[..., None]                    # (its own occlusion, in the grain)
    nor = load_sq(D + 'dark_wood_nor_gl_2k.jpg', res)
    rough = np.clip(0.32 + 0.45 * (arm[..., 1] - arm[..., 1].mean()) + 0.12, 0.22, 0.75)
    save('madera_diff', to_srgb(alb), True, res)
    save('madera_nor', nor, False, res, 90)
    save('madera_rough', rough, False, res // 2)

def terciopelo(res=512):
    """the kneelers' and curtains' velvet (Poly Haven «Velour Velvet», 0,28 m): from pink to a deep garnet"""
    D = 'polyhaven/muebles_6b/'
    alb = load_sq(D + 'velour_velvet_diff_2k.jpg', res, True)
    alb = retint(alb, (0.13, 0.008, 0.016), keep=0.1)
    arm = load_sq(D + 'velour_velvet_arm_2k.jpg', res)
    nor = load_sq(D + 'velour_velvet_nor_gl_2k.jpg', res)
    rough = np.clip(arm[..., 1] * 0.9 + 0.08, 0.5, 0.95)
    save('terciopelo_diff', to_srgb(alb), True, res)
    save('terciopelo_nor', nor, False, res, 90)
    save('terciopelo_rough', rough, False, res // 2)

def gold_leaf(res, seed, tile, wear):
    """gilding over a tile of `tile` metres: the leaves (8 × 8 cm, laid in rows, each a hair different, their edges
    overlapping in faint lines), and where wear has taken the gold, the red bole under it"""
    rng = np.random.default_rng(seed)
    n = max(1, round(tile / 0.08)); px = res / n
    yy, xx = np.mgrid[0:res, 0:res].astype(np.float32)
    row = (yy / px).astype(np.int32); off = (row % 2) * 0.5 * px
    cx = (((xx + off) / px).astype(np.int32)) % n
    lid = row * n + cx
    tone = rng.normal(0, 1, n * n + n)[lid]
    gold = np.array([1.0, 0.76, 0.36])
    alb = gold[None, None] * (1 + 0.035 * tone)[..., None]
    fx = ((xx + off) / px) % 1; fy = (yy / px) % 1
    edge = np.minimum(np.minimum(fx, 1 - fx), np.minimum(fy, 1 - fy)) * px
    line = np.clip(1 - edge / 1.6, 0, 1)
    alb *= (1 - 0.06 * line)[..., None]
    # wear: a cloudy mask, its high spots worn through to the bole
    w = blur(rng.standard_normal((res, res)).astype(np.float32), max(2, res // 96))
    w = (w - w.mean()) / (w.std() + 1e-6)
    fine = blur(rng.standard_normal((res, res)).astype(np.float32), 1); fine = (fine - fine.mean()) / (fine.std() + 1e-6)
    worn = np.clip((w * 0.8 + fine * 0.35 - (2.4 - wear)) * 2.5, 0, 1)
    bole = np.array([0.32, 0.07, 0.04])
    alb = alb * (1 - worn[..., None]) + bole[None, None] * worn[..., None]
    h = -line * 0.00015 + worn * -0.0002 + fine * 0.00002
    return alb, worn, h, line

def dorado(res=1024):
    """the retablos' burnished gilding (0,5 m tile): gold leaf, a little worn"""
    alb, worn, h, line = gold_leaf(res, 31, 0.5, 0.25)
    rough = np.clip(0.2 + 0.08 * line + 0.4 * worn, 0.12, 0.8)
    save('dorado_diff', to_srgb(alb), True, res)
    save('dorado_nor', normals(h, 0.5) * 0.5 + 0.5, False, res, 90)
    save('dorado_rough', rough, False, res // 2)

def talla(res=1024):
    """gilding over carving (0,5 m tile): the leaf duller, the ground punched in small dots (as a retablo's grounds),
    more of the bole where the wear goes"""
    alb, worn, h, line = gold_leaf(res, 47, 0.5, 0.6)
    yy, xx = np.mgrid[0:res, 0:res].astype(np.float32)
    k = res / 0.5 * 0.006   # (a dot every 6 mm)
    d = np.sqrt(((xx % k) - k / 2) ** 2 + ((yy % k) - k / 2) ** 2) / (k / 2)
    dots = np.clip(1 - d, 0, 1) ** 2
    h = h - dots * 0.0003
    alb = alb * (1 - 0.12 * dots)[..., None]
    rough = np.clip(0.34 + 0.2 * dots + 0.35 * worn, 0.2, 0.85)
    save('talla_diff', to_srgb(alb), True, res)
    save('talla_nor', normals(h, 0.5) * 0.5 + 0.5, False, res, 90)
    save('talla_rough', rough, False, res // 2)

def plata(res=512):
    """the exhibitor's and the chalice's silver, a little tarnished in its hollows"""
    rng = np.random.default_rng(5)
    w = blur(rng.standard_normal((res, res)).astype(np.float32), res // 48); w = (w - w.mean()) / (w.std() + 1e-6)
    alb = np.array([0.93, 0.93, 0.95])[None, None] * (1 - 0.1 * np.clip(w, 0, 3) / 3)[..., None]
    rough = np.clip(0.22 + 0.1 * w, 0.1, 0.5)
    save('plata_diff', to_srgb(alb), True, res)
    save('plata_rough', rough, False, res // 2)

def azul(res=1024):
    """the back of the Virgin's niche (0,8 m tile): a deep blue, darker at its foot, sown with gilded eight-pointed
    stars (they read as gold: the game gives them the metal's sheen by their mask, in the roughness' green)"""
    rng = np.random.default_rng(12)
    yy, xx = np.mgrid[0:res, 0:res].astype(np.float32) / res
    base = np.array([0.03, 0.06, 0.24])[None, None] * (0.8 + 0.2 * np.sin(yy * np.pi))[..., None]
    star = np.zeros((res, res), np.float32)
    for _ in range(22):
        cx, cy, r = rng.uniform(0, 1), rng.uniform(0, 1), rng.uniform(0.012, 0.022)
        dx = (xx - cx + 0.5) % 1 - 0.5; dy = (yy - cy + 0.5) % 1 - 0.5
        a = np.arctan2(dy, dx); rr = np.hypot(dx, dy)
        lim = r * (0.45 + 0.55 * np.abs(np.cos(4 * a)) ** 6)
        star = np.maximum(star, np.clip((lim - rr) / 0.0015, 0, 1))
    gold = np.array([0.85, 0.6, 0.25])
    alb = base * (1 - star[..., None]) + gold[None, None] * star[..., None]
    rough = 0.85 - 0.6 * star
    save('azul_diff', to_srgb(alb), True, res)
    save('azul_rough', rough, False, res // 2)

def blanco(res=256):
    """white painted wood (the dove, the glory's disc, the host): an even ivory, a faint brush"""
    rng = np.random.default_rng(3)
    w = blur(rng.standard_normal((res, res)).astype(np.float32), 2); w = (w - w.mean()) / (w.std() + 1e-6)
    alb = np.array([0.86, 0.84, 0.78])[None, None] * (1 + 0.02 * w)[..., None]
    save('blanco_diff', to_srgb(alb), True, res)

def lino(res=512):
    """the altars' cloths (Poly Haven «Rough Linen», 0,27 m): its blue taken out — an off-white linen, its weave kept"""
    D = 'polyhaven/muebles_6b/'
    alb = load_sq(D + 'rough_linen_diff_2k.jpg', res, True)
    alb = retint(alb, (0.78, 0.76, 0.7), keep=0.0)
    arm = load_sq(D + 'rough_linen_arm_2k.jpg', res)
    nor = load_sq(D + 'rough_linen_nor_gl_2k.jpg', res)
    save('lino_diff', to_srgb(alb), True, res)
    save('lino_nor', nor, False, res, 90)
    save('lino_rough', np.clip(arm[..., 1], 0.6, 1.0), False, res // 2)

def marmol(res=1024):
    """white marble (1,2 m tile), own: a warm white with a cloud of grey and fine grey veins (Macael's)"""
    rng = np.random.default_rng(21)
    def fbm(r0, oct=5):
        a = np.zeros((res, res), np.float32); amp = 1.0; tot = 0.0
        for o in range(oct):
            k = max(1, r0 >> o)
            n = blur(rng.standard_normal((res, res)).astype(np.float32), k); n = (n - n.mean()) / (n.std() + 1e-6)
            a += n * amp; tot += amp; amp *= 0.55
        return a / tot
    cloud = fbm(res // 12)
    warp = fbm(res // 24)
    yy, xx = np.mgrid[0:res, 0:res].astype(np.float32) / res
    v = np.abs(np.sin((xx * 3 + yy * 1.5 + warp * 0.9) * np.pi * 2))
    vein = np.clip(1 - v / 0.035, 0, 1) ** 2 * np.clip(cloud * 0.6 + 0.6, 0, 1)
    base = np.array([0.82, 0.8, 0.77])
    alb = base[None, None] * (1 - 0.06 * np.clip(cloud, -2, 2)[..., None]) * (1 - 0.45 * vein[..., None])
    save('marmol_diff', to_srgb(alb), True, res)
    save('marmol_rough', np.clip(0.12 + 0.06 * np.abs(cloud) + 0.15 * vein, 0.05, 0.5), False, res // 2)

def hierro(res=256):
    """wrought iron, painted black long ago: its paint worn on the edges to the dark metal"""
    rng = np.random.default_rng(9)
    w = blur(rng.standard_normal((res, res)).astype(np.float32), 3); w = (w - w.mean()) / (w.std() + 1e-6)
    alb = np.array([0.035, 0.034, 0.036])[None, None] * (1 + 0.25 * w)[..., None]
    save('hierro_diff', to_srgb(alb), True, res)
    save('hierro_rough', np.clip(0.5 + 0.12 * w, 0.3, 0.8), False, res // 2)

# ---------------------------------------------------------------- the images' polychromy (6c): estofado
ESTOFADO = {   # (base colour, gold, how dense the flowers) — the robes' colours of tools/blender/imagenes.py
    'tunica_blanca': ((0.86, 0.84, 0.78), (0.85, 0.62, 0.25), 1.0), 'manto_azul': ((0.06, 0.11, 0.36), (0.88, 0.66, 0.28), 0.8),
    'tunica_negra': ((0.03, 0.03, 0.035), (0.75, 0.76, 0.8), 0.6), 'manto_negro': ((0.022, 0.022, 0.026), (0.72, 0.74, 0.78), 0.5),
    'tunica_roja': ((0.42, 0.05, 0.06), (0.88, 0.66, 0.28), 0.9), 'manto_crema': ((0.8, 0.72, 0.56), (0.8, 0.58, 0.22), 0.7),
    'tunica_morada': ((0.24, 0.11, 0.27), (0.88, 0.66, 0.28), 0.9), 'manto_ocre': ((0.6, 0.4, 0.13), (0.95, 0.78, 0.4), 1.1),
}
def estofado(res=512):
    """estofado: gold leaf under the paint, scratched through it in flowers and scrolls (esgrafiado) — a 25 cm tile:
    rosettes in a lozenge net, a stem of scrolls winding between them, a fine hatching over the gold"""
    yy, xx = np.mgrid[0:res, 0:res].astype(np.float32) / res
    for name, (base, gold, dense) in ESTOFADO.items():
        n = 3 if dense >= 0.9 else 2
        u, v = xx * n, yy * n
        fu, fv = u % 1, v % 1; cu, cv = np.floor(u), np.floor(v)
        off = (cv % 2) * 0.5
        du, dv = (u + off) % 1 - 0.5, fv - 0.5
        r = np.sqrt(du * du + dv * dv); a = np.arctan2(dv, du)
        petals = r < (0.17 + 0.07 * np.cos(a * 6))           # (a rosette of six petals)
        eye = r < 0.05
        stem = np.abs(np.sin((u + 0.25) * np.pi * 2 + np.sin(v * np.pi * 2) * 1.2)) < 0.06   # (the winding stem)
        hatch = (np.sin((xx + yy) * res * 0.9) > 0.3)        # (the fine hatching scratched in the gold)
        g = (petals & ~eye) | stem
        g = g.astype(np.float32) * (0.75 + 0.25 * hatch)
        g = blur(g, 1)
        col = np.array(base)[None, None] * (1 - g[..., None]) + np.array(gold)[None, None] * g[..., None]
        save(f'{name}_diff', to_srgb(col), True, res)
        save(f'{name}_rough', np.clip(0.62 - 0.35 * g, 0.2, 0.8), False, res // 2)

def ojo(res=256):
    """a glass eye: the white, the iris (a dark brown, its fibres), the pupil, a gleam"""
    yy, xx = np.mgrid[0:res, 0:res].astype(np.float32) / res
    r = np.sqrt((xx - 0.5) ** 2 + (yy - 0.5) ** 2) * 2
    a = np.arctan2(yy - 0.5, xx - 0.5)
    white = np.array([0.82, 0.8, 0.76]); iris = np.array([0.16, 0.09, 0.05]) * (0.8 + 0.25 * np.sin(a * 40)[..., None] * (r[..., None] > 0.18))
    col = np.where((r < 0.42)[..., None], iris, white[None, None])
    col = np.where((r < 0.17)[..., None], np.array([0.01, 0.01, 0.01])[None, None], col)
    col = col * (1 - 0.35 * np.clip((r - 0.36) / 0.08, 0, 1) * (r < 0.46))[..., None]
    save('ojo_diff', to_srgb(col), True, res)

import sys
WHICH = sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else []
print('texturas del interior →', OUT, flush=True)
for name in (WHICH or ['cal', 'granito', 'suelo', 'vidrio', 'madera', 'terciopelo', 'dorado', 'talla', 'plata', 'azul', 'blanco', 'lino', 'marmol', 'hierro', 'estofado', 'ojo']): globals()[name]()
