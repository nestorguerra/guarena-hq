# Can every sign be read? (technical backlog, R-09 and R-10): the game in a headless Chrome (muted, tools/perf/cdp.py,
# port 9333), every sign of its inventory photographed square on from 10 m — or from as far as the street lets, when a
# front stands nearer —, at 1080p, by day (12:30) and by night (22:00); the sign's part of the picture read by macOS's
# own OCR (tools/rotulos/ocr.swift, compiled once to .cache/rotulos/ocr) and compared with its words: a match when the
# Levenshtein distance is ≤ 1 (case, accents and spacing aside). Writes data/rotulos/legibilidad.json; exit 1 under 98 %.
#   python3 tools/rotulos/legibilidad.py [URL] [--solo N]      (default: the published copy, http://localhost:8926/test.html)
import base64, json, os, re, subprocess, sys, unicodedata
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'perf'))
from cdp import Tab
OUT = os.path.join(ROOT, '.cache', 'rotulos')
OCR = os.path.join(OUT, 'ocr')

JS = r'''(async (lista, hour, W, H) => {
  const G = window.game, r = G.renderer, cam = G.camera, map = G.map, V3 = cam.position.constructor; // (the page's own three.js: the published copy has no import map)
  if (!window.__legSetup) {
    window.__legSetup = true;
    if (G.player.vehicle) G.player.exitVehicle(true);
    const body = G.player.char && G.player.char.object; if (body) body.visible = false;
    if (G.weather) { const Wt = G.weather; clearTimeout(Wt.timer); Wt.on = false; Wt.data = null; Object.assign(Wt.now, { cover: 0.1, over: 0, rain: 0, snow: 0, fog: 0, storm: 0, fogFar: 3000 }); }
    for (const c of (G.fleet && G.fleet.vehicles) || []) if (c.parked) { c.x += 1e4; c.writeMatrix(G.fleet.renderer, G.fleet.tmp); } // (no parked car in front of a sign)
  }
  // (the hour first — the game's frames may size the picture to the window —, then the picture's size)
  if (G.sky.hour !== hour) { G.sky.hour = hour; for (let k = 0; k < 3; k++) G.frame(1 / 30); }
  r.setSize(W, H, false); if (G.composer) { G.composer.setSize(W, H); if (G.bloom) G.bloom.setSize(W, H); }
  cam.aspect = W / H; cam.fov = 50; cam.updateProjectionMatrix();
  const out = [], v = new V3(), rc = new window.__rotulos.Raycaster(); rc.camera = cam; rc.params.Line.threshold = 0.01; rc.params.Points.threshold = 0.01;
  for (const s of lista) {
    // (back from its face along its normal, at a person's eye height; a front nearer than 10 m stops the camera short)
    const t = map.collider.raycast(s.x + s.nx * 0.3, s.z + s.nz * 0.3, s.x + s.nx * 10, s.z + s.nz * 10, 1.2, 2.2);
    let d = Math.max(2, Math.min(10, 0.3 + 9.7 * t - 0.4));
    // (and where nothing stands in the line of sight — a tree, an awning, a lamp —: nearer, a metre at a time, down to 2 m)
    for (; d > 2; d -= 1) {
      const o = new V3(s.x + s.nx * d, 1.7, s.z + s.nz * d), to = new V3(s.x + s.nx * 0.05, s.y, s.z + s.nz * 0.05), dir = to.clone().sub(o), L = dir.length();
      rc.set(o, dir.normalize()); rc.far = L - 0.12; cam.position.copy(o); cam.updateMatrixWorld(true);
      const h = rc.intersectObjects(G.scene.children, true).find((q) => q.object.visible && q.object.isMesh && !(q.object.material && q.object.material.transparent && q.object.material.opacity < 0.5) && q.object.type !== 'Sprite');
      if (!h) break;
    }
    d = Math.max(2, d);
    // (from nearer than 10 m a wide sign may not fit: the lens opened as far as needed to frame it whole, 50° at least)
    const half = Math.atan(((s.w || 1) / 2 + 0.4) / d), fovV = Math.max(50, Math.min(100, (2 * Math.atan(Math.tan(half) / (W / H)) * 180) / Math.PI * 1.05));
    cam.fov = fovV; cam.updateProjectionMatrix();
    cam.position.set(s.x + s.nx * d, 1.7, s.z + s.nz * d); cam.lookAt(s.x, s.y, s.z); cam.updateMatrixWorld(true);
    G.sky.update(0, cam.position); G.world.update(0, G.sky.night, cam.position); G.render();
    // the sign's corners on the picture: its part of it, a quarter more round
    const tx = s.nz, tz = -s.nx, hw = (s.w || 1) / 2, hh = (s.h || 0.3) / 2;
    let x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9;
    for (const [a, b] of [[-hw, -hh], [hw, -hh], [hw, hh], [-hw, hh]]) {
      v.set(s.x + tx * a, s.y + b, s.z + tz * a).project(cam);
      const px = (v.x + 1) / 2 * W, py = (1 - v.y) / 2 * H;
      x0 = Math.min(x0, px); x1 = Math.max(x1, px); y0 = Math.min(y0, py); y1 = Math.max(y1, py);
    }
    const mx = (x1 - x0) * 0.25 + 8, my = (y1 - y0) * 0.6 + 8;
    x0 = Math.max(0, x0 - mx); y0 = Math.max(0, y0 - my); x1 = Math.min(W, x1 + mx); y1 = Math.min(H, y1 + my);
    if (x1 - x0 < 4 || y1 - y0 < 4) { out.push({ id: s.id, d, img: null }); continue; }
    // (the sign's part of the 1080p picture, enlarged 3× with smoothing for the OCR — it reads small print better so;
    // no detail is added: the pixels are the picture's)
    const c = document.createElement('canvas'); c.width = Math.round(x1 - x0) * 3; c.height = Math.round(y1 - y0) * 3;
    const cx2 = c.getContext('2d'); cx2.imageSmoothingEnabled = true; cx2.imageSmoothingQuality = 'high';
    cx2.drawImage(r.domElement, x0, y0, x1 - x0, y1 - y0, 0, 0, c.width, c.height);
    out.push({ id: s.id, d: +d.toFixed(2), px: [Math.round(x1 - x0), Math.round(y1 - y0)], img: c.toDataURL('image/png') });
  }
  return JSON.stringify(out);
})'''

# (letters and digits only, in capitals, accents and punctuation aside — an OCR's «CTRA:» or «LA]» is not a misreading of the words)
norm = lambda s: re.sub(r'\s+', ' ', re.sub(r'[^A-Z0-9 ]', ' ', unicodedata.normalize('NFD', (s or '').upper()).encode('ascii', 'ignore').decode())).strip()
def lev(a, b):
    p = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        c = [i]
        for j, cb in enumerate(b, 1): c.append(min(p[j] + 1, c[j - 1] + 1, p[j - 1] + (ca != cb)))
        p = c
    return p[-1]

def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    url = args[0] if args else 'http://localhost:8926/test.html'
    solo = int(sys.argv[sys.argv.index('--solo') + 1]) if '--solo' in sys.argv else None
    os.makedirs(os.path.join(OUT, 'leg'), exist_ok=True)
    if not os.path.exists(OCR):
        subprocess.run(['xcrun', 'swiftc', '-O', os.path.join(ROOT, 'tools', 'rotulos', 'ocr.swift'), '-o', OCR], check=True)
    T = Tab(9333, url, w=1920, h=1080, dpr=1)
    try:
        lista = json.loads(T.ev('''(async () => { const t0 = performance.now(); while (performance.now() - t0 < 180000) { if (window.game && window.game.state === 'play' && !document.getElementById('hud').hidden) break; await new Promise((r) => setTimeout(r, 250)); }
          await new Promise((r) => setTimeout(r, 1500));
          const R = window.__rotulos; R.recoger(window.game.scene);
          return JSON.stringify(R.inventario.filter((s) => (s.texto || '').trim()).map((s) => ({ id: s.id, tipo: s.tipo, texto: s.texto, x: s.x, y: s.y, z: s.z, nx: s.nx, nz: s.nz, w: s.w, h: s.h }))); })()''', timeout=240))
        if solo: lista = lista[:solo]
        files = {}
        for hour, tag in ((12.5, 'dia'), (22, 'noche')):
            for k in range(0, len(lista), 25):
                part = lista[k:k + 25]
                res = json.loads(T.ev('(' + JS + ')(' + json.dumps(part) + ', ' + str(hour) + ', 1920, 1080)', timeout=600))
                for s, q in zip(part, res):
                    f = None
                    if q['img']:
                        f = os.path.join(OUT, 'leg', '%s_%04d.png' % (tag, lista.index(s)))
                        open(f, 'wb').write(base64.b64decode(q['img'].split(',', 1)[1]))
                    files[(s['id'], tag)] = (f, q['d'], q.get('px'))
                print(tag, min(k + 25, len(lista)), '/', len(lista), flush=True)
    finally:
        T.close()
    paths = [f for f, _, _ in files.values() if f]
    read = {}
    for k in range(0, len(paths), 200):
        r = subprocess.run([OCR] + paths[k:k + 200], capture_output=True, text=True)
        for line in r.stdout.splitlines():
            o = json.loads(line); read[o['f']] = o['t']
    rows, ok = [], {'dia': 0, 'noche': 0}
    for s in lista:
        row = {'id': s['id'], 'tipo': s['tipo'], 'texto': s['texto']}
        for tag in ('dia', 'noche'):
            f, d, px = files[(s['id'], tag)]
            lines = read.get(f, [])
            want = norm(s['texto'])
            # (a street plate: its name is what must read; the kind of way over it — CALLE, AVDA. — is smaller)
            alt = norm(re.sub(r'^(CALLE|AVDA\.|PLAZA|TRVA\.|CTRA\.|CAMINO|PASEO|RONDA|PASAJE|CALLEJÓN)\s+', '', s['texto'])) if s['tipo'] == 'placa_calle' else want
            # (any run of the lines read, joined: a sign of several lines — the kind of way over a street's name — is read line by line)
            cands = [norm(' '.join(lines[i:j])) for i in range(len(lines)) for j in range(i + 1, len(lines) + 1)]
            best = min((min(lev(c, want), lev(c, alt)) for c in cands), default=len(want))
            row[tag] = {'leido': lines, 'distancia': best, 'ok': best <= 1, 'metros': d, 'px': px}
            ok[tag] += best <= 1
        rows.append(row)
    n = len(rows)
    res = {'url': url, 'rotulos': n, 'umbral': '≥ 98 % con distancia de Levenshtein ≤ 1', 'dia': round(100 * ok['dia'] / max(1, n), 1), 'noche': round(100 * ok['noche'] / max(1, n), 1),
           'fallos': [r for r in rows if not (r['dia']['ok'] and r['noche']['ok'])]}
    json.dump(res | {'todos': rows}, open(os.path.join(ROOT, 'data', 'rotulos', 'legibilidad.json'), 'w'), ensure_ascii=False, indent=1)
    by = {}
    for r in res['fallos']: by[r['tipo']] = by.get(r['tipo'], 0) + 1
    print(json.dumps({'rotulos': n, 'dia_%': res['dia'], 'noche_%': res['noche'], 'fallos': len(res['fallos']), 'fallos_por_tipo': by}, ensure_ascii=False))
    return res['dia'] >= 98 and res['noche'] >= 98

if __name__ == '__main__':
    sys.exit(0 if main() else 1)
