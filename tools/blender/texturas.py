# The church's textures (docs/hiperrealismo.md, «Materiales»), made in Blender's Python (numpy) from the CC0 scans in
# .cache/polyhaven into .cache/hq/tex as seamless JPEG tiles, which iglesia.py packs into the model (assets/hq/iglesia.glb:
# the only copy that ships):
#   /Applications/Blender.app/Contents/MacOS/Blender --background --factory-startup --python tools/blender/texturas.py
# - mamposteria (6 m): Santa María's rubble as the photo shows it — a golden-ochre mass of stones of 20–70 cm, nearly
#   the mortar's tone, each wearing its own piece of a real stone's face (Poly Haven's «Large Sandstone Blocks 01»), the
#   grain of «Yellow Stone Wall» over all, and scattered dark stones of 10–45 cm (≈13 % of the wall; ≈4 % in the
#   west front's variant, «mamposteria_pies», as the photo's sunlit front); laid out on wrap-around jittered grids, so
#   the tile repeats with no seam;
# - silleria (3 m, the scan's own size): Poly Haven's «Large Sandstone Blocks 01» turned from grey to the photo's golden
#   sandstone;
# - teja (2,5 m): Poly Haven's «Clay Roof Tiles 02», as it is.
# Albedo in sRGB; normal (OpenGL, +Y up) and roughness linear. Credit: textures from Poly Haven (polyhaven.com), CC0.
import bpy, numpy as np, os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SRC = os.path.join(ROOT, '.cache', 'polyhaven')
OUT = os.path.join(ROOT, '.cache', 'hq', 'tex')
os.makedirs(OUT, exist_ok=True)
rng = np.random.default_rng(11)

def load(name, res):
    """a scan as a float array (rows down), averaged down to res"""
    img = bpy.data.images.load(os.path.join(SRC, name)); img.colorspace_settings.name = 'Non-Color'
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
    print(f'  {name}.jpg {res}px {os.path.getsize(os.path.join(OUT, name + ".jpg")) // 1024} KB')

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
    """a tangent-space normal map from a height field (metres), wrapping round"""
    px = metres / h.shape[0]
    dx = (np.roll(h, -1, 1) - np.roll(h, 1, 1)) / (2 * px); dy = (np.roll(h, -1, 0) - np.roll(h, 1, 0)) / (2 * px)
    n = np.stack([-dx, dy, np.ones_like(h)], -1)
    return n / np.linalg.norm(n, axis=-1, keepdims=True)

# ---------------------------------------------------------------- mampostería
def jittered(res, tile, spacing, jit, seed_rng):
    """a jittered grid of seeds over a wrap-around tile: per pixel, the nearest seeds among the 5 × 5 cells round it
    (F1, F2 with each seed's weight subtracted: a power diagram) and the nearest's index"""
    g = int(round(tile / spacing)); cell = res / g
    jx, jy = seed_rng.uniform(-jit, jit, (g, g)), seed_rng.uniform(-jit, jit, (g, g))
    wt = seed_rng.uniform(0, 1, (g, g))
    iy, ix = np.mgrid[0:res, 0:res].astype(np.float32)
    cy, cx = (iy // cell).astype(np.int32), (ix // cell).astype(np.int32)
    F1 = np.full((res, res), 1e9, np.float32); F2 = np.full((res, res), 1e9, np.float32); ID = np.zeros((res, res), np.int32)
    for dy in range(-2, 3):
        for dx in range(-2, 3):
            ny, nx = cy + dy, cx + dx
            my, mx = ny % g, nx % g
            sy = (ny + 0.5 + jy[my, mx]) * cell; sx = (nx + 0.5 + jx[my, mx]) * cell
            d = np.sqrt((ix - sx) ** 2 + ((iy - sy) * 1.25) ** 2) / cell - 0.35 * wt[my, mx]   # (stones a little wider than tall)
            idx = my * g + mx
            closer = d < F1
            F2 = np.where(closer, F1, np.minimum(F2, d)); ID = np.where(closer, idx, ID); F1 = np.where(closer, d, F1)
    return F1, F2, ID, g * g, cell

def mamposteria(res=3072, tile=6.0, dark_share=0.17, name='mamposteria'):
    """Santa María's rubble as the photo shows it (and the reviewer measured it): a golden-ochre mass of stones of
    20–70 cm, nearly the mortar's tone, their joints just darker; and, scattered, dark stones of 10–45 cm, some 13 % of
    the wall (11–13 % in the shaded north wall, 3–5 % in the sunlit front: dark_share picks the cells, the same golden
    mass every time — the generator is seeded afresh — so the front's dark stones are a few of the sides' ones)"""
    rng = np.random.default_rng(11)
    ysw = load('yellow_stone_wall_diff_2k.jpg', 2048)
    lum = ysw @ np.array([0.3, 0.59, 0.11])
    det = lum - blur(lum, 2048 // 85); det /= (np.abs(det).max() + 1e-6)
    sb = load('large_sandstone_blocks_01_diff_2k.jpg', 2048)
    sl = sb @ np.array([0.3, 0.59, 0.11]); sl = sl - blur(sl, 2048 // 40); sl /= (np.abs(sl).max() + 1e-6)
    up = lambda a: np.repeat(np.repeat(a, 3, 0), 3, 1)[::2, ::2] if res == 3072 else a          # (2048 → 3072)
    det, sl = up(det), up(sl)
    yy, xx = np.mgrid[0:res, 0:res]
    # the golden mass: stones of 20–70 cm (spacing 0.42 m, sizes spread by their weights)
    F1, F2, ID, nG, cell = jittered(res, tile, 0.42, 0.42, rng)
    edge = (F2 - F1) * cell * tile / res                       # (metres from the joint's middle, roughly)
    tint = rng.uniform(0.86, 1.12, nG); warmth = rng.uniform(-0.04, 0.05, nG)
    oy, ox = rng.integers(0, res, nG), rng.integers(0, res, nG)
    face = sl[(yy + oy[ID]) % res, (xx + ox[ID]) % res]       # each stone its own piece of a real stone's face
    joint = np.clip(1 - edge / 0.022, 0, 1)                    # (thin joints, ~2–4 cm)
    base = np.array([0.46, 0.30, 0.12])
    gold = base[None, None] * tint[ID][..., None] * (1 + np.stack([warmth[ID], 0 * warmth[ID], -warmth[ID]], -1))
    gold = gold * (1 + 0.28 * face[..., None]) * (1 + 0.22 * det[..., None])
    mort = base[None, None] * np.array([1.04, 1.02, 0.98]) * (1 + 0.3 * det[..., None])
    alb = gold * (1 - joint[..., None]) + mort * 0.86 * joint[..., None]
    # the dark stones, scattered: cells of a finer, independent diagram (0,28 m), about one in six of them, each shrunk
    # from its edges (crisp, angular, 10–45 cm across)
    G1, G2, GID, nD, cellD = jittered(res, tile, 0.28, 0.45, rng)
    dedge = (G2 - G1) * cellD * tile / res
    pick = rng.uniform(0, 1, nD) < dark_share
    margin = rng.uniform(0.012, 0.035, nD)
    dark = np.clip((dedge - margin[GID]) / 0.006, 0, 1) * pick[GID]
    shade = rng.uniform(0, 1, nD); blue = rng.uniform(0, 1, nD)
    dshade, dblue = shade[GID], blue[GID]
    dh = np.sqrt(np.clip((dedge - margin[GID]) / 0.05, 0, 1))
    # (grey-brown, not black: in the photo's shaded wall they stand at ≈0,55 of the mortar's brightness)
    dcol = np.array([0.085, 0.075, 0.065])[None, None] * (1 - dshade[..., None]) + np.array([0.19, 0.16, 0.13])[None, None] * dshade[..., None]
    dcol = dcol * (1 + np.stack([-0.08 * dblue, 0 * dblue, 0.12 * dblue], -1))   # (some slaty, bluish)
    dcol = dcol * (1 + 0.5 * face[..., None])
    alb = alb * (1 - dark[..., None]) + dcol * dark[..., None]
    # (the mortar darkens a little round each dark stone, where it was pressed in)
    halo = np.clip(1 - (dedge - margin[GID] + 0.015) / 0.015, 0, 1) * pick[GID] * (1 - dark)
    alb = alb * (1 - 0.18 * halo[..., None])
    print(f'  {name}: piedra oscura {float((dark > 0.5).mean()) * 100:.1f} % del muro')
    # relief: the golden stones' faces swell a little, the joints sink, the dark stones stand out
    h = (1 - joint) * 0.006 * np.sqrt(np.clip(edge / 0.06, 0, 1)) + dark * dh * 0.012 + det * 0.002 + face * 0.002
    n = normals(h, tile)
    rough = np.clip(0.9 - 0.06 * dark + 0.04 * det, 0, 1)
    save(f'{name}_diff', to_srgb(alb), True, res)
    save(f'{name}_nor', n * 0.5 + 0.5, False, res // 2, 92)
    save(f'{name}_rough', rough, False, res // 2)

# ---------------------------------------------------------------- sillería
def silleria(res=2048):
    d = to_lin(load('large_sandstone_blocks_01_diff_2k.jpg', res))
    L = d @ np.array([0.2126, 0.7152, 0.0722])
    # (its lichen and stains make broad blotches that cross the joints; the photo's ashlar is an even gold that changes
    # from block to block: the broad blotches go, the joints and the grain stay)
    L = L - blur(L, res // 24) + L.mean()
    lo, hi = np.percentile(L, 2), np.percentile(L, 98)
    t = 0.25 + 0.6 * np.clip((L - lo) / (hi - lo), 0, 1) ** 0.9
    gold = np.array([0.19, 0.11, 0.045])[None, None] * (1 - t[..., None]) + np.array([0.64, 0.46, 0.25])[None, None] * t[..., None]
    chroma = d - L[..., None]                                  # its lichen and stains, toned well down (they read green)
    alb = gold + 0.05 * chroma
    nor = load('large_sandstone_blocks_01_nor_gl_2k.jpg', res)
    rough = load('large_sandstone_blocks_01_rough_2k.jpg', res)[..., 0]
    save('silleria_diff', to_srgb(alb), True, 2048)
    save('silleria_nor', nor, False, 1024, 92)
    save('silleria_rough', rough, False, 1024)

# ---------------------------------------------------------------- teja
def teja(res=2048):
    # (old Extremaduran roofs are weathered: browner and duller than the scan's new orange — the orthophoto's roofs)
    tj = to_lin(load('clay_roof_tiles_02_diff_2k.jpg', res)); tl = tj @ np.array([0.2126, 0.7152, 0.0722])
    tj = 0.72 * tj + 0.28 * tl[..., None]; tj = tj * np.array([0.88, 0.84, 0.82])
    save('teja_diff', to_srgb(tj), True, 1024)
    save('teja_nor', load('clay_roof_tiles_02_nor_gl_2k.jpg', res), False, 1024, 92)
    save('teja_rough', load('clay_roof_tiles_02_rough_2k.jpg', res)[..., 0], False, 1024)

print('texturas →', OUT)
mamposteria(); mamposteria(dark_share=0.05, name='mamposteria_pies'); silleria(); teja()
