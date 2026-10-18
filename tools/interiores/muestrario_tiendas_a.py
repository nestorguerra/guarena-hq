# Sample sheets and room views of the «tiendas_a» family, for whoever builds and reviews it (muestrario_tiendas_a.js), in the
# headless muted Chrome (tools/perf/cdp.py, port 9333) on the development server. Pictures in .snaps/ (ta_hoja_*.jpg, ta_sala_*.jpg).
#   python3 tools/interiores/muestrario_tiendas_a.py hojas [--fila 6] [--por 12] [id …]   (without ids: every object of the family)
#   python3 tools/interiores/muestrario_tiendas_a.py sala <kit> <semilla> [etiqueta]
import json, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'perf'))
from cdp import Tab

def abrir():
    T = Tab(9333, 'http://localhost:8920/index.html?estilo=plastilina', w=1280, h=720, dpr=1)
    T.ev('''(async () => { const t0 = performance.now(); while (performance.now() - t0 < 180000) { if (window.game && window.game.state === 'play') break; await new Promise((r) => setTimeout(r, 250)); } })()''', timeout=240)
    return T

def main():
    a = sys.argv[1:]
    modo = a.pop(0)
    T = abrir()
    try:
        if modo == 'hojas':
            fila = int(a[a.index('--fila') + 1]) if '--fila' in a else 6
            por = int(a[a.index('--por') + 1]) if '--por' in a else 12
            for k in ('--fila', '--por'):
                if k in a: i = a.index(k); del a[i:i + 2]
            ids = a or [o['id'] for o in json.load(open(os.path.join(ROOT, 'data', 'objetos', 'tiendas_a.json')))['objetos']]
            # (grouped by size so that the camera fits them: tiny, small, medium, large)
            tam = json.loads(T.ev('(async () => { const M = await import("/src/objetos.js?" + Date.now()); const OB = (await import("/src/interiores_datos.js?" + Date.now())).OBJETOS; return JSON.stringify(%s.map((id) => { const b = M.caja(id); return [id, Math.max(b.w, b.h, b.d), OB[id].soporte]; })); })()' % json.dumps(ids)))
            grupos = {}
            for id, s, sop in tam: grupos.setdefault((0 if s < 0.12 else 1 if s < 0.35 else 2 if s < 0.9 else 3) + (10 if sop == 'pared' else 20 if sop == 'techo' else 0), []).append(id)
            n = 0
            for g, lst in sorted(grupos.items()):
                for i in range(0, len(lst), por):
                    sub = lst[i:i + por]
                    name = T.ev('(async () => { const M = await import("/tools/interiores/muestrario_tiendas_a.js?" + Date.now()); return await M.hoja(%s, %s, { fila: %d }); })()' % (json.dumps(sub), json.dumps('%d_%02d' % (g, i // por)), len(sub)), timeout=300)
                    print(name, sub)
        elif modo == 'plano':
            import base64
            kit = a[0]
            for seed in [int(q) for q in a[1].split(',')]:
                d = T.ev('(async () => { const M = await import("/tools/interiores/muestrario_tiendas_a.js?" + Date.now()); return await M.plano(%s, %d); })()' % (json.dumps(kit), seed), timeout=300)
                path = os.path.join(ROOT, '.snaps', 'ta_plano_%s_%d.png' % (kit, seed))
                open(path, 'wb').write(base64.b64decode(d.split(',')[1])); print(path)
        elif modo == 'sala':
            kit, seed = a[0], int(a[1]); tag = a[2] if len(a) > 2 else 'a'
            r = json.loads(T.ev('(async () => { const M = await import("/tools/interiores/muestrario_tiendas_a.js?" + Date.now()); return JSON.stringify(await M.sala(%s, %d, %s)); })()' % (json.dumps(kit), seed, json.dumps(tag)), timeout=300))
            print(json.dumps(r))
            from PIL import Image
            fs = r['fotos']
            for j in range(0, len(fs), 4):
                M = Image.new('RGB', (1280, 720))
                for q, name in enumerate(fs[j:j + 4]):
                    M.paste(Image.open(os.path.join(ROOT, '.snaps', name + '.jpg')).convert('RGB').resize((640, 360), Image.LANCZOS), ((q % 2) * 640, (q // 2) * 360))
                M.save(os.path.join(ROOT, '.snaps', 'ta_montaje_%s_%d_%s_%d.jpg' % (kit, seed, tag, j // 4)), quality=88)
                print('.snaps/ta_montaje_%s_%d_%s_%d.jpg' % (kit, seed, tag, j // 4))
    finally:
        T.close()

if __name__ == '__main__':
    main()
