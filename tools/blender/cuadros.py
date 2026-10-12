# The paintings of Santa María in high definition (docs/hiperrealismo.md, «La 6c»): reproductions of public-domain
# works from Wikimedia Commons (.cache/commons/cuadros_6c; their sources and licences in cuadros_6c_fuentes.json), each
# cut to its place's proportion — as a canvas made to measure fills its frame — and saved for the game in
# assets/hq/interior/cuadros/<kind>.jpg (hiperinterior.js lays them on church.js's canvases). Blender's Python:
#   /Applications/Blender.app/Contents/MacOS/Blender --background --factory-startup --python tools/blender/cuadros.py
import bpy, numpy as np, os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SRC = os.path.join(ROOT, '.cache', 'commons', 'cuadros_6c')
OUT = os.path.join(ROOT, 'assets', 'hq', 'interior', 'cuadros')
os.makedirs(OUT, exist_ok=True)

# each place: its proportion (width / height), where the cut sits (0 at the top … 1 at the bottom), a margin to drop
# first (the photo's own frame or arch, in fractions: top, right, bottom, left) and the height in pixels. The retablo's apostles (src/retablo.js: their slot's width over the tier's height less 0,6 m), the
# Doctors (square), the Crucifixion (its eared frame, made to the painting's proportion), the chapels' canvases
# (0,8 × 1,3 m) and the baptistery's (1,8 × 2,6 m); and, if given, where across (0 the left … 1 the right; the middle)
A = lambda w, h: w / h
PLACES = {
    'pedro': (A(1.3, 2.25), 0.12, None, 1024), 'pablo': (A(1.3, 2.25), 0.12, None, 1024),
    'andres': (A(1.18, 2.25), 0.12, None, 1024), 'santiago': (A(1.18, 2.25), 0.12, None, 1024),
    'juan': (A(1.3, 2.08), 0.12, None, 1024), 'tomas': (A(1.3, 2.08), 0.12, None, 1024),
    'mateo': (A(1.18, 2.08), 0.12, None, 1024), 'bartolome': (A(1.18, 2.08), 0.12, None, 1024),
    'felipe': (A(1.3, 1.8), 0.12, None, 1024), 'menor': (A(1.3, 1.8), 0.12, None, 1024),
    'simon': (A(1.18, 1.8), 0.12, None, 1024), 'tadeo': (A(1.18, 1.8), 0.12, None, 1024),
    'crucifixion': (A(1.18, 1.9), 0.4, None, 1024),
    'jeronimo': (1.0, 0.05, None, 512, 0.3), 'ambrosio': (1.0, 0.03, None, 512), 'gregorio': (1.0, 0.04, None, 512),
    'agustin': (1.0, 0.2, None, 512),
    'bautismo': (A(1.8, 2.6), 0.4, (0.13, 0.0, 0.0, 0.0), 1024),
    'isidro': (A(0.8, 1.3), 0.35, None, 768), 'ana': (A(0.8, 1.3), 0.45, None, 768), 'roque': (A(0.8, 1.3), 0.3, None, 768),
    'isabel': (A(0.8, 1.3), 0.3, None, 768), 'francisco': (A(0.8, 1.3), 0.4, None, 768), 'antonio': (A(0.8, 1.3), 0.35, None, 768),
    'lucia': (A(0.8, 1.3), 0.0, (0.1, 0.04, 0.07, 0.04), 768),
}

def load(name):
    img = bpy.data.images.load(os.path.join(SRC, name + '.jpg'))
    w, h = img.size
    px = np.empty(w * h * 4, np.float32); img.pixels.foreach_get(px)
    return px.reshape(h, w, 4)[::-1]          # (rows from the top)

def cut(a, aspect, anchor, margin, across=0.5):
    h, w = a.shape[:2]
    if margin:
        t, r, b, l = margin
        a = a[int(t * h): h - int(b * h), int(l * w): w - int(r * w)]
        h, w = a.shape[:2]
    if w / h > aspect:                         # (too wide: the sides go, the middle stays)
        nw = int(round(h * aspect)); x0 = int(round((w - nw) * across))
        return a[:, x0:x0 + nw]
    nh = int(round(w / aspect)); y0 = int(round((h - nh) * anchor))
    return a[y0:y0 + nh]

def save(name, a, height):
    h, w = a.shape[:2]
    img = bpy.data.images.new(name, w, h, alpha=False)
    img.pixels.foreach_set(a[::-1].astype(np.float32).ravel())
    W = max(8, int(round(height * w / h)))
    img.scale(W, height)
    img.file_format = 'JPEG'
    path = os.path.join(OUT, name + '.jpg')
    img.save(filepath=path, quality=86)
    print(f'  {name}.jpg {W}×{height} {os.path.getsize(path) // 1024} KB', flush=True)

print('cuadros →', OUT, flush=True)
for name, (aspect, anchor, margin, height, *across) in PLACES.items():
    save(name, cut(load(name), aspect, anchor, margin, *across), height)
