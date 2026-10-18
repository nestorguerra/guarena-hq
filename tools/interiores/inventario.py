# The inventory of the interiors (technical backlog, I-01), from the game itself in a headless Chrome (muted:
# tools/perf/cdp.py, port 9333) on the development server: tools/interiores/inventario.js lists every door and the
# interior it leads to, and every business of the map with or without a door. Writes data/interiors_inventory.json;
# exit 1 if a door leads nowhere, an accessible interior has no typology, or a door is missing from the list.
#   python3 tools/interiores/inventario.py
import collections, json, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'perf'))
from cdp import Tab

def main():
    T = Tab(9333, 'http://localhost:8920/index.html?estilo=plastilina', w=960, h=540, dpr=1)
    try:
        T.ev('''(async () => { const t0 = performance.now(); while (performance.now() - t0 < 180000) { if (window.game && window.game.state === 'play') break; await new Promise((r) => setTimeout(r, 250)); } })()''', timeout=240)
        inv = json.loads(T.ev('(async () => { const I = await import("/tools/interiores/inventario.js?" + Date.now()); return JSON.stringify(await I.inventario()); })()', timeout=600))
    finally:
        T.close()
    rows = inv['interiors']
    resumen = {'interiores': len(rows), 'puertas': inv['puertas'], 'accesibles': sum(r['accesible'] for r in rows),
               'por_estado': dict(collections.Counter(r['estado'] for r in rows)),
               'por_tipologia': {t: dict(collections.Counter(r['estado'] for r in rows if r['tipologia'] == t)) for t in sorted({r['tipologia'] for r in rows})}}
    json.dump({'version': 1, 'resumen': resumen, 'errores': inv['errores'], 'interiors': rows}, open(os.path.join(ROOT, 'data', 'interiors_inventory.json'), 'w'), ensure_ascii=False, indent=1)
    print(json.dumps(resumen, ensure_ascii=False, indent=1))
    for e in inv['errores'][:20]: print('  ✗', e)
    return not inv['errores']

if __name__ == '__main__':
    sys.exit(0 if main() else 1)
