# The inventory of the signs (technical backlog, R-01): the game loaded in a headless Chrome (muted: --mute-audio,
# tools/perf/cdp.py, port 9333) from the development server, and every sign it put up written to
# data/rotulos/signs_inventory.json — a stable UUID, its building, its place in the game's metres and in latitude and
# longitude, its kind, its faces, its words and its state (vacio, marcador, rellenado). Sorted and rounded: the same town
# gives the same file, byte for byte (its hash printed).
#   python3 tools/rotulos/inventario.py [URL]        (default http://localhost:8920/index.html?estilo=plastilina)
#   python3 tools/rotulos/inventario.py --control    (R-01's check: 50 signs seeded in a scratch street file, all found)
import hashlib, json, math, os, re, subprocess, sys, uuid
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'perf'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rotulos import MARCADORES

LAT0, LON0, R = 38.8596, -6.1025, 6378137.0  # (the game's frame: tools/build_map.py)
KX, KZ = math.cos(math.radians(LAT0)) * R * math.pi / 180.0, R * math.pi / 180.0
NS = uuid.UUID('6b1f2d0e-6a1e-4a52-9c1c-6775617265f1')  # (the namespace of the signs' ids: uuid5 of their place in the town)
TIPO = {'fachada': 'fachada', 'banderola': 'banderola', 'placa_calle': 'placa_informativa', 'placa': 'placa_informativa',
        'cartel': 'placa_informativa', 'placa_informativa': 'placa_informativa', 'monolito': 'monolito'}

def tomar(url):
    from cdp import Tab
    T = Tab(9333, url, w=1280, h=720, dpr=1)
    try:
        return json.loads(T.ev('''(async () => { const t0 = performance.now(); while (performance.now() - t0 < 180000) { if (window.game && window.game.state === 'play' && !document.getElementById('hud').hidden) break; await new Promise((r) => setTimeout(r, 250)); }
          const R = window.__rotulos; R.recoger(window.game.scene);
          return JSON.stringify({ modo: R.modo, errs: (window.__errs || []).slice(0, 5), lista: R.inventario }); })()''', timeout=240))
    finally:
        T.close()

def estado(t):
    if not (t or '').strip(): return 'vacio'
    if MARCADORES.search(t): return 'marcador'
    return 'rellenado'

def inventario(raw):
    out = []
    for s in raw['lista']:
        x, z = s['x'], s['z']
        out.append({
            'sign_id': str(uuid.uuid5(NS, s['id'])), 'clave': s['id'], 'building_id': s.get('bid'),
            'mundo': {'x': round(x, 2), 'y': round(s.get('y') or 0, 2), 'z': round(z, 2), 'nx': round(s.get('nx') or 0, 3), 'nz': round(s.get('nz') or 0, 3)},
            'geo': {'lat': round(LAT0 - z / KZ, 7), 'lon': round(LON0 + x / KX, 7)},
            'tipo': TIPO.get(s['tipo'], s['tipo']), 'subtipo': s['tipo'], 'caras': s.get('caras') or 1,
            'medidas': {'ancho': round(s['w'], 2) if s.get('w') else None, 'alto': round(s['h'], 2) if s.get('h') else None},
            'texto': s.get('texto') or '', 'estado': estado(s.get('texto')), 'poi': s.get('poi'), 'poi_mapa': s.get('poi_mapa'),
            'generico': bool(s.get('generico')), 'motivo_generico': s.get('motivo'),
            **({'calle': s['calle'], 'nodo': s.get('nodo'), 'cruce': s.get('cruce'), 'soporte': s.get('soporte')} if s['tipo'] == 'placa_calle' else {}),
        })
    out.sort(key=lambda r: r['sign_id'])
    return out

def escribir(lista, modo):
    # (the published copy's words: the inventory kept in the repository is the one of a copy with no real names)
    body = json.dumps({'version': 1, 'modo': modo, 'total': len(lista), 'rotulos': lista}, ensure_ascii=False, indent=1, sort_keys=True)
    p = os.path.join(ROOT, 'data', 'rotulos', 'signs_inventory.json')
    open(p, 'w', encoding='utf-8').write(body + '\n')
    return hashlib.sha256(body.encode()).hexdigest()

def control():
    # 50 signs seeded along one street (a scratch file of the street fixes, removed after): all 50 must be found
    f = os.path.join(ROOT, 'tools', 'fachadas', 'arreglos', 'zzz_control_rotulos.json')
    items = [{'tipo': 'cartel', 'vista': 211, 'lado': 'izq' if k % 2 else 'der', 'en': 2 + k * 1.5, 'lateral': 9 + (k % 3), 'ancho': 1.2, 'alto': 0.6, 'suelo': 1.0,
              'color': '#f4f4f0', 'texto': 'CONTROL %02d' % k, 'letra': '#1f3f7a', 'mira': 'camara'} for k in range(50)]
    json.dump({'items': items}, open(f, 'w'), ensure_ascii=False)
    try:
        subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'fachadas', 'arreglos.py')], check=True, capture_output=True)
        raw = tomar(sys.argv[2] if len(sys.argv) > 2 else 'http://localhost:8920/index.html?estilo=plastilina')
        got = sorted({s['texto'] for s in raw['lista'] if (s.get('texto') or '').startswith('CONTROL ')})
        print(json.dumps({'sembrados': 50, 'encontrados': len(got), 'errs': raw['errs']}, ensure_ascii=False))
        return len(got) == 50
    finally:
        os.remove(f)
        subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'fachadas', 'arreglos.py')], check=True, capture_output=True)

if __name__ == '__main__':
    if '--control' in sys.argv: sys.exit(0 if control() else 1)
    url = sys.argv[1] if len(sys.argv) > 1 else 'http://localhost:8920/index.html?estilo=plastilina'
    raw = tomar(url)
    lista = inventario(raw)
    h = escribir(lista, raw['modo'])
    by = {}
    for r in lista: by[r['estado']] = by.get(r['estado'], 0) + 1
    print(json.dumps({'modo': raw['modo'], 'total': len(lista), 'estados': by, 'errs': raw['errs'], 'sha256': h}, ensure_ascii=False))
