# The interiors' validator (technical backlog, I-04, I-03, V-01: validate_interiors), in a headless Chrome (muted:
# tools/perf/cdp.py, port 9333) on the development server: every kit built with a few seeds and checked by
# tools/interiores/validar.js. Writes data/interiores/validacion/<kit>.json; exit 1 on any blocking error.
#   python3 tools/interiores/validar.py [kit …] [--semillas 1,2,3,4,5] [--juego]
import glob, json, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'perf'))
from cdp import Tab

def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--') and not a[0].isdigit()]
    seeds = [int(s) for s in sys.argv[sys.argv.index('--semillas') + 1].split(',')] if '--semillas' in sys.argv else [1, 2, 3, 4, 5]
    tips = args or sorted(os.path.basename(f)[:-5] for f in glob.glob(os.path.join(ROOT, 'data', 'kits', '*.json')) if not f.endswith('.schema.json'))
    # (a page of its own, with nothing drawn: fast, and no WebGL needed; --juego, inside the game itself)
    juego = '--juego' in sys.argv
    T = Tab(9333, 'http://localhost:8920/' + ('index.html?estilo=plastilina' if juego else 'tools/interiores/validar.html'), w=1280, h=720, dpr=1)
    try:
        T.ev('''(async () => { const t0 = performance.now(); while (performance.now() - t0 < 180000) { if (%s) break; await new Promise((r) => setTimeout(r, 250)); } })()''' % ("window.game && window.game.state === 'play'" if juego else 'window.__listo'), timeout=240)
        res = {}
        for t in tips:
            res[t] = json.loads(T.ev('(async () => { const V = await import("/tools/interiores/validar.js?" + Date.now()); return JSON.stringify(await V.validar(%s, %s)); })()' % (json.dumps(t), json.dumps(seeds)), timeout=600))
    finally:
        T.close()
    total = sum(len(r['errores']) for rr in res.values() for r in rr)
    # (one file per kit: several kits can be checked at once without treading on each other)
    os.makedirs(os.path.join(ROOT, 'data', 'interiores', 'validacion'), exist_ok=True)
    for t, rr in res.items():
        json.dump({'kit': t, 'semillas': seeds, 'errores': sum(len(r['errores']) for r in rr), 'resultados': rr}, open(os.path.join(ROOT, 'data', 'interiores', 'validacion', t + '.json'), 'w'), ensure_ascii=False, indent=1)
    for t, rr in res.items():
        print(t, '·', ' | '.join(f"s{r['seed']}: {r['objetos']} obj, {r['distintos']} dist., {len(r['errores'])} err" for r in rr))
        for r in rr[:2]:
            for e in r['errores'][:12]: print('   ', e)
    return total == 0

if __name__ == '__main__':
    sys.exit(0 if main() else 1)
