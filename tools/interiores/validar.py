# The interiors' validator (technical backlog, I-04, I-03, V-01: validate_interiors), in a headless Chrome (muted:
# tools/perf/cdp.py, port 9333) on the development server: every kit built with a few seeds and checked by
# tools/interiores/validar.js. Writes data/interiores/validacion/<kit>.json; exit 1 on any blocking error.
#   python3 tools/interiores/validar.py [kit …] [--semillas 1,2,3,4,5] [--juego]
#   python3 tools/interiores/validar.py --casas [n]     (the neighbours' houses: every room furnished from a kit)
import argparse, glob, json, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'perf'))
from cdp import Tab

def main():
    parser = argparse.ArgumentParser(description='Valida kits y cobertura real de las viviendas.')
    parser.add_argument('kits', nargs='*')
    parser.add_argument('--semillas', default='1,2,3,4,5')
    parser.add_argument('--juego', action='store_true')
    parser.add_argument('--casas', nargs='?', const=60, type=int)
    parser.add_argument('--casas-pueblo', action='store_true')
    parser.add_argument('--exigir-kits', default='')
    parser.add_argument('--exigir-todas', action='store_true')
    opts = parser.parse_args()
    seeds = [int(s) for s in opts.semillas.split(',')]
    tips = opts.kits or sorted(os.path.basename(f)[:-5] for f in glob.glob(os.path.join(ROOT, 'data', 'kits', '*.json')) if not f.endswith('.schema.json'))
    juego = opts.juego or opts.casas_pueblo
    T = Tab(9333, 'http://localhost:8920/' + ('index.html?estilo=plastilina' if juego else 'tools/interiores/validar.html'), w=1280, h=720, dpr=1)
    try:
        if juego:
            T.ev('''(async () => { const t0 = performance.now(); while (performance.now()-t0 < 180000) { const b = document.getElementById('bPlay'); if (window.game && b && document.getElementById('loading').hidden) { b.click(); break; } await new Promise(r=>setTimeout(r,250)); } })()''', timeout=240)
        T.ev('''(async () => { const t0 = performance.now(); while (performance.now() - t0 < 180000) { if (%s) break; await new Promise((r) => setTimeout(r, 250)); } })()''' % ("window.game && window.game.state === 'play'" if juego else 'window.__listo'), timeout=240)
        res = {}
        if opts.casas is not None or opts.casas_pueblo:
            house_seeds = json.loads(T.ev('JSON.stringify(window.game.interiors.doors.filter(d => d.seed >= 1000 && !d.owner && !d.venue && !d.church).map(d => d.seed))')) if opts.casas_pueblo else [1000 + 37 * k for k in range(opts.casas)]
            rules = {'exigirKits': [k for k in opts.exigir_kits.split(',') if k], 'exigirTodas': opts.exigir_todas}
            casas = json.loads(T.ev('(async () => { const V = await import("/tools/interiores/validar.js?" + Date.now()); return JSON.stringify(await V.validarCasas(%s, %s)); })()' % (json.dumps(house_seeds), json.dumps(rules)), timeout=900))
            os.makedirs(os.path.join(ROOT, 'data', 'interiores', 'validacion'), exist_ok=True)
            json.dump({'alcance': 'pueblo' if opts.casas_pueblo else 'sinteticas', 'exigencia': rules, 'casas': len(casas), 'habitables': sum(c['cobertura']['habitables'] for c in casas), 'pendientes': sum(len(c['cobertura']['faltantes']) for c in casas), 'errores': sum(len(c['errores']) for c in casas), 'resultados': casas}, open(os.path.join(ROOT, 'data', 'interiores', 'validacion', 'casas_pueblo.json' if opts.casas_pueblo else 'casas.json'), 'w'), ensure_ascii=False, indent=1)
            if not casas: raise RuntimeError('la selección de casas está vacía')
            print('cobertura:', sum(c['cobertura']['porKit'] for c in casas), '/', sum(c['cobertura']['habitables'] for c in casas), 'habitaciones por kit')
            mal = [c for c in casas if c['errores']]
            print('casas ·', len(casas), 'construidas,', sum(len(c['salas']) for c in casas), 'estancias por kit,', len(mal), 'con errores')
            for c in mal[:8]: print('   ', c['seed'], c['perfil'], c['estilo'], c['errores'][:3])
            return not mal
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
        print(t, '·', ' | '.join(f"s{r['seed']}{' (' + r['hogar'] + ')' if r.get('hogar') else ''}: {r['objetos']} obj, {r['distintos']} dist., {len(r['errores'])} err" for r in rr))
        for r in rr[:2]:
            for e in r['errores'][:12]: print('   ', e)
    return total == 0

if __name__ == '__main__':
    sys.exit(0 if main() else 1)
