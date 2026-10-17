# the errors of a kit's last validation: python3 tools/interiores/tb_err.py <kit>
import json, sys
d = json.load(open('data/interiores/validacion/%s.json' % sys.argv[1]))
tot = {}
for r in d['resultados']:
    for e in r['errores']:
        k = e.split(' — ')[0] if 'obligatorio' in e else e[:90]
        tot.setdefault(k, []).append((r['seed'], round(r['W'], 1), round(r['D'], 1)))
print(len(d['resultados']), 'builds,', d['errores'], 'errors')
for k, v in tot.items(): print(len(v), k, v[:6])
mx = max(d['resultados'], key=lambda r: r['triangulos']); mm = max(d['resultados'], key=lambda r: r['mallas'])
print('max tris', mx['triangulos'], 'seed', mx['seed'], '| max meshes', mm['mallas'], '| objs', min(r['objetos'] for r in d['resultados']), '-', max(r['objetos'] for r in d['resultados']), '| distinct', min(r['distintos'] for r in d['resultados']), '-', max(r['distintos'] for r in d['resultados']))
dif = [r.get('diferencia_con_semilla_1') for r in d['resultados'] if r.get('diferencia_con_semilla_1') is not None]
print('min difference vs seed 1', min(dif) if dif else None)
