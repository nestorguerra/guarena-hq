"""Preparado T19. Sólo ejecutar tras publicación y prueba pública reales; no publica."""
from pathlib import Path
import datetime
import hashlib
import json
import math
import re
import shutil
import subprocess

r = Path(__file__).resolve().parents[4]
p = r / '.cache/calidad/tanda19'
a = Path(__file__).resolve().parent
v = r / 'data/interiores/validacion'
e = v / 'evidencia_tanda19'
J = lambda path: json.loads(path.read_text())
H = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()

def W(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n')

def command(*args):
    return subprocess.check_output(args, cwd=r, text=True).strip()

def close(value, target, tolerance=1e-5):
    return isinstance(value, (int, float)) and math.isfinite(value) and abs(value-target) < tolerance

expected = (p / 'commit_producto.txt').read_text().strip()
assert re.fullmatch('[0-9a-f]{40}', expected), 'SHA producto inválido'
source = J(p / 'estado_candidato.json')['archivos']
assert all(H(r/f) == h for f, h in source.items()), 'Freeze alterado'
# Raíz copia una sola vez el recibo PASS del directorio real de ejecución.
report_path = p / 'integracion_publica_producto.json'
x = J(report_path)
ci = J(p / 'main_actualizado.json')
pages = J(p / 'pages_final.json')
assert not x['errores'] and not x['consola'] and not x['consola_tras_recarga']
assert x['http_status'] == 200
assert x['revision_servida'] == x['revision_tras_recarga'] == expected
assert x['recarga_partida'] == x['carga_partida']
assert len(x['entradas']) == 8 and x['annie']['kits'] == 5 and len(x['comercios']) == 3
salones = [row for row in x['entradas'] if row.get('programaSalon')]
assert sorted(row['seed'] for row in salones) == [1594, 3244]
assert all(close(row['programaSalon']['gap_real'], .55) and row['programaSalon']['asiento_lectura']['registros'] == 1 for row in salones)
trofeos = x['trofeos']
assert trofeos['estado'] == 'PASS'
rows = trofeos['rows']
assert len(rows) == 4 and sorted(row['seed'] for row in rows) == [1679, 2132, 2162, 4204]
for row in rows:
    assert row['estado'] == 'PASS' and close(row['programa']['gap_real'], .32)
    assert row['programa']['botin'] == ['rifle', 'prismaticos']
    assert row['programa']['acciones'] == ['read', 'drawer']
    assert row['programa']['banco'] == (0 if row['seed'] == 2162 else 1)
    if row['seed'] != 2162:
        seat = row['asiento']
        assert seat['registros'] == 1
        assert all(seat[k] is True for k in ['seleccion_real', 'sentado', 'levantado', 'salida_libre', 'posicion_restaurada'])
        assert all(math.isfinite(seat[k]) for k in ['x', 'y', 'z', 'h', 'distancia_seleccion'])
        assert all(math.isfinite(seat['salida'][k]) for k in ['x', 'y', 'z'])
assert ci['commit'] == ci['main_verificado'] == pages['headSha'] == expected
assert pages['status'] == 'completed' and pages['conclusion'] == 'success'
assert ci['ci']['headSha'] == expected and ci['ci']['status'] == 'completed' and ci['ci']['conclusion'] == 'success'
workflow = ci['workflow_verificado']
assert workflow['path'] == '.github/workflows/validar.yml'
assert workflow['id'] == ci['ci']['databaseId'] and workflow['head_sha'] == expected
assert workflow['status'] == 'completed' and workflow['conclusion'] == 'success'
ci_jobs = {job['name']: job for job in ci['ci']['jobs']}
assert {'validate_signs', 'validate_interiors'} <= ci_jobs.keys()
assert all(job['conclusion'] == 'success' for job in ci['ci']['jobs'])
page_jobs = {job['name']: job for job in pages['jobs']}
assert {'build', 'deploy'} <= page_jobs.keys()
assert all(job['conclusion'] == 'success' for job in pages['jobs'])
assert command('/opt/homebrew/bin/gh', 'api', 'repos/nestorguerra/guarena-hq/branches/main', '--jq', '.commit.sha') == expected
page_workflow = json.loads(command('/opt/homebrew/bin/gh', 'api', 'repos/nestorguerra/guarena-hq/actions/runs/' + str(pages['databaseId']), '--jq', '{id,path,head_sha,status,conclusion}'))
assert page_workflow['id'] == pages['databaseId'] and page_workflow['path'] == '.github/workflows/pages.yml'
assert page_workflow['head_sha'] == expected and page_workflow['status'] == 'completed' and page_workflow['conclusion'] == 'success'
assert command('git', 'rev-parse', expected + '^{tree}') == ci['arbol_ci_y_producto']
assert command('git', 'rev-parse', ci['merge_ci'] + '^{tree}') == ci['arbol_ci_y_producto']
contracts = J(p/'contratos.json')
assert len(contracts['pruebas']) == 82 and all(t['estado'] == 'PASS' for t in contracts['pruebas'])
assert not contracts.get('errores', [])
gates = J(p/'validacion_ejecuciones.json')
assert len(gates) == 10 and len({g['nombre'] for g in gates}) == 10 and all(g['exit_code'] == 0 for g in gates)
judgments = {side: J(v/('visual_trofeos_'+side+'.json'))['media'] for side in ['A', 'B']}
assert close(judgments['A'], 3.306, .00001) and close(judgments['B'], 3.368, .00001), judgments
original = J(e/'manifest.json')
assert all(H(e/f) == h for f, h in original['archivos'].items()), 'Dossier previo alterado'
dest = v/'integracion_publica_tanda19.json'
acta = v/'publicacion_tanda19.json'
pub = e/'publicacion'
assert not dest.exists() and not acta.exists() and not pub.exists(), 'Cierre de un solo uso: no sobrescribir'
doc_paths = [r/'docs/calidad-viviendas-4-2026-10-17.md', r/'docs/hiperrealismo-registro.md']
docs = {q: q.read_text() for q in doc_paths}
assert all('Tanda 19 publicada y verificada:' not in s for s in docs.values())
# Todas las precondiciones anteriores son de lectura. A partir de aquí se añaden recibos.
pub.mkdir()
shutil.copy2(e/'manifest.json', pub/'manifest_pre_publicacion.json')
W(pub/'ci_final.json', ci['ci'])
W(pub/'ci_arbol.json', {k: ci[k] for k in ['commit', 'main_anterior', 'arbol_ci_y_producto', 'merge_ci', 'main_verificado']})
shutil.copy2(p/'pages_final.json', pub/'pages_final.json')
W(pub/'pages_workflow_verificado.json', page_workflow)
W(pub/'main_actualizado_completo.json', ci)
for name in ['verificar_publico.py', 'trofeos_publico.js', 'cerrar_publicacion.py']:
    shutil.copy2(a/name, pub/name)
shutil.copy2(report_path, dest)
(pub/'LEEME.md').write_text(f'''# Publicación T19

Producto {expected}. Prueba pública ejecutada desde .cache/calidad/tanda19/revision_publicacion/verificar_publico.py, que carga trofeos_publico.js desde el mismo directorio. Su salida original se guarda en revision_publicacion/ejecuciones; raíz copia el informe PASS una vez a .cache/calidad/tanda19/integracion_publica_producto.json antes de este cierre. Las copias del dossier son evidencia; no deben ejecutarse desde aquí porque resuelven rutas relativas a su ubicación original.

Ocho vecinos y cuatro cuartos de trofeos reales; selección, sentarse y levantarse mediante métodos del juego en tres bancos, 2162 sin banco. Aproximación mediante reposición privada a punto validado, no recorrido desde la puerta. Residentes conservados. Se comprueba collider y restauración; no se certifica calidad visual de la animación. Annie cinco kits, acciones comerciales sin compras, partida ficticia y recarga. El botín se comprueba por identidad/premio, sin recogerlo en público.

manifest_pre_publicacion.json conserva {len(original['archivos'])} entradas previas. El manifiesto ampliado no reemplaza ni reescribe esos archivos. El cierre es de un solo uso; si falla durante escritura, conservar el estado parcial y revisar antes de reintentar. No efectúa commit, push ni despliegue.
''')
rep = {'tanda':19, 'fecha':datetime.datetime.now(datetime.timezone.utc).isoformat(), 'estado':'publicada_y_verificada', 'commit':expected, 'url':x['url'],
 'ci':{'run':ci['ci']['databaseId'], 'estado':'success', 'url':ci['ci']['url'], 'arbol_ci_y_head_identico':ci['arbol_ci_y_producto']},
 'pages':{'run':pages['databaseId'], 'estado':'success', 'url':pages['url']},
 'integracion':{'informe':'data/interiores/validacion/integracion_publica_tanda19.json', 'sha256':H(dest), 'estado':'PASS', 'casas':8, 'trofeos_reales':[2132,4204,1679,2162], 'bancos_seleccion_sentarse_levantarse':[2132,4204,1679], 'sin_banco':2162, 'gap_consulta':.32, 'annie_kits':5, 'comercios_con_acciones':3, 'partida_ficticia_y_recarga':True, 'revision_antes_y_despues':expected, 'maximo_entrada_ms':max(row['entrada_ms'] for row in x['entradas']), 'maximo_trofeos_entrada_ms':max(row['entrada_ms'] for row in rows), 'annie_entrada_ms':x['annie']['entrada_ms']},
 'validacion_previa':{'contratos':82, 'gates':10}, 'visual':{**judgments, 'objetivo_4_alcanzado':False},
 'limites':'Avance parcial. No acredita 4/5, reducción de carga del25% ni FPS. Entrada medida localmente; no rendimiento universal. Bancos por métodos reales con reposición a un acceso validado, sin certificar recorrido desde puerta ni aspecto de animación. Acciones comerciales presentes sin compras. Botín por identidad/premio sin recoger públicamente.'}
W(acta, rep)
append = f'''\n\nTanda 19 publicada y verificada: `{expected}`, CI {rep['ci']['run']} y Pages {rep['pages']['run']} completados con éxito. SHA público exacto antes y después de recargar; ocho vecinos, cuatro cuartos de trofeos reales, tres bancos con selección/sentarse/levantarse y salida libre, 2162 sin banco. La prueba repone al jugador en un acceso validado; no certifica recorrido desde puerta. Annie conserva cinco kits y funciones propias; acciones de tres comercios sin compras y partida ficticia persistente, sin errores de consola. Máximo vecinal {rep['integracion']['maximo_entrada_ms']} ms, trofeos {rep['integracion']['maximo_trofeos_entrada_ms']} ms y Annie {rep['integracion']['annie_entrada_ms']} ms en esta ejecución local; no son FPS. Recibo: `data/interiores/validacion/publicacion_tanda19.json`. Calidad de trofeos3,306/3,368: avance parcial, objetivo4/5 pendiente; no acredita el25% de carga.\n'''
for q, previous in docs.items():
    q.write_text(previous.rstrip()+append)
assert all(H(e/f) == h for f,h in original['archivos'].items())
W(e/'manifest.json', {'fecha':datetime.datetime.now(datetime.timezone.utc).date().isoformat(), 'archivos':{str(f.relative_to(e)):H(f) for f in sorted(e.rglob('*')) if f.is_file() and f != e/'manifest.json'}})
assert all(H(e/f) == h for f,h in original['archivos'].items())
print(json.dumps(rep, ensure_ascii=False, indent=1))
