# The user's Google Maps captures of the old town's streets (~/Desktop/Guareña: one folder per street or square, an
# indice_capturas.json): the street-level ones as camera poses in the game's frame, for tools/callelab.js to photograph
# the game from the same spot. The captures are a reference for modelling by hand only: not a pixel of them goes into
# the game, and the poses file holds numbers and names only (.cache/calles/poses.json, outside the repository).
#   python3 tools/fachadas/capturas.py [folder]
import json, math, os, re, sys
from urllib.parse import unquote
REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SRC = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser('~/Desktop/Guareña')
LAT0, LON0, R = 38.8596, -6.1025, 6378137.0
KX, KZ = math.cos(math.radians(LAT0)) * R * math.pi / 180, R * math.pi / 180
W, H = 1440, 693  # (every capture's size)

def pose(url):
    u = unquote(url)
    # the Maps URLs API: viewpoint=lat,lon&heading=&pitch=&fov=. Its fov is not what the captures show: they were taken
    # with the viewer's own 90° up and down, as the 90y ones (measured on round manhole covers: views 49, 58, 13)
    m = re.search(r'viewpoint=([-\d.]+),([-\d.]+)', u)
    if m:
        q = dict(re.findall(r'[?&](heading|pitch|fov)=([-\d.]+)', u))
        return float(m[1]), float(m[2]), float(q.get('heading', 0)), float(q.get('pitch', 0)), 90.0
    # the web app's own: @lat,lon,<alt>a,<fov>y,<heading>h,<tilt>t (90t level) — y the vertical field of view
    m = re.search(r'@([-\d.]+),([-\d.]+),[\d.]+a,([\d.]+)y,(?:([-\d.]+)h,)?([\d.]+)t', u)
    if m and ('!1e1' in u or '!2e0' in u or '!1e2' in u):
        return float(m[1]), float(m[2]), float(m[4] or 0), float(m[5]) - 90, float(m[3])
    return None

idx = json.load(open(os.path.join(SRC, 'indice_capturas.json')))
# (the folder keeps growing: a view keeps its number from one run to the next — its folder and file name it — and the
# new ones are numbered on after the last, so that everything written about view n (lados.json, the labelled sheets,
# the profiles) still means the same view; a view that left the index keeps its place, marked gone)
OUTP = os.path.join(REPO, '.cache', 'calles', 'poses.json')
prev = []
try: prev = json.load(open(OUTP))
except Exception: pass
ids = {(o['folder'], o['file']): o['id'] for o in prev}
byid = {o['id']: o for o in prev}
seen, nxt = set(), max(ids.values(), default=-1) + 1
for c in idx:
    p = pose(c['url'])
    if not p or not c.get('folder'): continue
    key = (c['folder'], c['file'])
    if key in seen: continue
    seen.add(key)
    if key not in ids: ids[key] = nxt; nxt += 1
    lat, lon, h, pitch, fv = p
    byid[ids[key]] = {'id': ids[key], 'folder': c['folder'], 'file': c['file'], 'label': c.get('label', ''), 'date': c.get('date_display', ''),
                      'x': round((lon - LON0) * KX, 2), 'z': round(-(lat - LAT0) * KZ, 2), 'heading': h, 'pitch': pitch, 'fov': round(fv, 2)}
for k, i in ids.items():
    if k not in seen: byid[i]['gone'] = True
out = [byid[i] for i in range(nxt)]
json.dump(out, open(OUTP, 'w'), ensure_ascii=False, indent=1)
from collections import Counter
print(len(out), 'vistas a pie de calle;', sum(1 for o in out if o.get('gone')), 'fuera del índice;', len(out) - len(prev), 'nuevas;',
      dict(Counter(o['folder'] for o in out if not o.get('gone'))))
