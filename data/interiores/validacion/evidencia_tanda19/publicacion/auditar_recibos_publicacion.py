"""Auditoría local sólo lectura; no importa ni ejecuta los helpers de publicación."""
from pathlib import Path
import json, hashlib, subprocess, math
r=Path.cwd(); p=r/'data/interiores/validacion'; d=p/'evidencia_tanda19'; out=r/'.cache/calidad/tanda19'
H=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
J=lambda f:json.loads(f.read_text())
def git(*args):return subprocess.check_output(['git',*args],text=True).strip()
checks=[]
def check(name,value):
 assert value,name
 checks.append(name)
status=git('status','--porcelain');head=git('rev-parse','HEAD');expected='c486ed205510c1b94ba013846d17a2a1ad55ed4c'
check('HEAD producto',head==expected)
m=J(d/'manifest.json'); mh=H(d/'manifest.json'); files=m['archivos'];actual={str(f.relative_to(d)) for f in d.rglob('*') if f.is_file() and f!=d/'manifest.json'}
check('169 entradas exactas sin ausentes ni extras',len(files)==169 and set(files)==actual)
check('169 hashes',all(H(d/f)==h for f,h in files.items()))
old=J(d/'publicacion/manifest_pre_publicacion.json')['archivos'];check('159 anteriores conservados literalmente',len(old)==159 and all(files.get(f)==h and H(d/f)==h for f,h in old.items()))
check('sello previo coincide con HEAD',subprocess.check_output(['git','show',expected+':data/interiores/validacion/evidencia_tanda19/manifest.json'])==(d/'publicacion/manifest_pre_publicacion.json').read_bytes())
frozen=J(d/'auditoria/estado_candidato.json')['archivos'];check('417 fuentes activas exactas',len(frozen)==417 and all(H(r/f)==h for f,h in frozen.items()))
check('fuentes sin diff frente a HEAD',not git('diff','HEAD','--',*frozen.keys()))
ci=J(d/'publicacion/ci_final.json');pages=J(d/'publicacion/pages_final.json');tree=J(d/'publicacion/ci_arbol.json');main=J(d/'publicacion/main_actualizado_completo.json');workflow=J(d/'publicacion/pages_workflow_verificado.json')
check('CI exacto concluido success',ci['databaseId']==39099689341 and ci['headSha']==expected and ci['status']=='completed' and ci['conclusion']=='success')
check('CI dos jobs y pasos success',set(j['name'] for j in ci['jobs'])=={'validate_signs','validate_interiors'} and all(j['conclusion']=='success' and all(s['conclusion']=='success' for s in j['steps']) for j in ci['jobs']))
check('Pages exacto concluido success',pages['databaseId']==39099907357 and pages['headSha']==expected and pages['status']=='completed' and pages['conclusion']=='success')
check('Pages build/deploy y pasos success',set(j['name'] for j in pages['jobs'])=={'build','deploy'} and all(j['conclusion']=='success' and all(s['conclusion']=='success' for s in j['steps']) for j in pages['jobs']))
check('paths de workflows verificados',workflow['path']=='.github/workflows/pages.yml' and workflow['id']==pages['databaseId'] and workflow['head_sha']==expected and main['workflow_verificado']['path']=='.github/workflows/validar.yml' and main['workflow_verificado']['id']==ci['databaseId'])
check('CI raw idéntico a main completo',main['ci']==ci)
check('trees producto y merge CI idénticos',git('rev-parse',expected+'^{tree}')==git('rev-parse',tree['merge_ci']+'^{tree}')==tree['arbol_ci_y_producto'])
act=J(p/'publicacion_tanda19.json');x=J(p/'integracion_publica_tanda19.json');xh=H(p/'integracion_publica_tanda19.json')
check('acta enlaza hash exacto de integración',act['commit']==expected and act['integracion']['sha256']==xh)
check('copias de recibo público exactas',all(H(f)==xh for f in [out/'integracion_publica_producto.json',out/'revision_publicacion/ejecuciones/integracion_publica_producto.json']))
check('HTTP y revisión antes/después',x['http_status']==200 and x['revision_esperada']==x['revision_servida']==x['revision_tras_recarga']==expected)
check('errores y consola vacíos',not x['errores'] and not x['consola'] and not x['consola_tras_recarga'])
check('8 entradas genéricas',len(x['entradas'])==8 and len({v['seed'] for v in x['entradas']})==8)
rows=x['trofeos']['rows'];check('4 trofeos reales PASS',x['trofeos']['estado']=='PASS' and sorted(v['seed'] for v in rows)==[1679,2132,2162,4204] and all(v['estado']=='PASS' for v in rows))
check('programas y recompensas declarados',all(abs(v['programa']['gap_real']-.32)<1e-6 and v['programa']['botin']==['rifle','prismaticos'] and v['programa']['acciones']==['read','drawer'] for v in rows))
check('3 bancos near sit stand con restauración; 2162 ausente',all(v['programa']['banco']==0 and 'asiento' not in v if v['seed']==2162 else v['programa']['banco']==1 and v['asiento']['registros']==1 and all(v['asiento'][k] is True for k in ['seleccion_real','sentado','levantado','salida_libre','posicion_restaurada']) and v['asiento']['distancia_seleccion']<1.25 for v in rows))
check('Annie5 y 3 comercios',x['annie']['kits']==5 and x['annie']['siesta'] is True and {a['tipo'] for a in x['comercios']}=={'bar','cafeteria','farmacia'} and all(a['acciones']>0 for a in x['comercios']))
check('persistencia ficticia tras recarga',x['carga_partida']==x['recarga_partida'] and x['recarga_partida']['dinero']==321 and x['recarga_partida']['banco']==700)
check('máximos acta calculados',max(a['entrada_ms'] for a in x['entradas'])==act['integracion']['maximo_entrada_ms']==172.7 and max(a['entrada_ms'] for a in rows)==act['integracion']['maximo_trofeos_entrada_ms']==91 and x['annie']['entrada_ms']==89.5)
for name in ['verificar_publico.py','trofeos_publico.js','cerrar_publicacion.py']:
 check('helper copiado exacto '+name,H(d/'publicacion'/name)==H(out/'revision_publicacion'/name))
contracts=J(d/'gates/contratos.json');gates=J(d/'gates/validacion_ejecuciones.json')
check('82 contratos previos PASS',len(contracts['pruebas'])==82 and all(t['estado']=='PASS' for t in contracts['pruebas']) and not contracts['errores'])
check('10 gates previos exit0',len(gates)==10 and len({g['nombre'] for g in gates})==10 and all(g['exit_code']==0 for g in gates))
cases=J(d/'gates/casas.json');kits=J(d/'gates/vivienda_trofeos.json');regen=J(d/'gates/regeneracion.json')
check('200 casas1166 y81 trofeos',cases['casas']==200 and cases['habitables']==1166 and cases['errores']==cases['pendientes']==0 and len(kits['semillas'])==81 and kits['errores']==0)
check('22 derivados actuales exactos',regen['estado']=='PASS' and regen['archivos_identicos']==len(regen['archivos'])==22 and all(H(r/f)==h for f,h in regen['archivos'].items()))
for side,score in [('A',3.306),('B',3.368)]:
 v=J(p/('visual_trofeos_'+side+'.json'));check('arte '+side+' imagen exacta sin4',H(r/v['ficha'])==H(r/v['ficha_snapshot'])==v['ficha_sha256'] and v['media']==score and v['supera_umbral'] is False and act['visual'][side]==score)
 check('arte '+side+' media/schema coherente',len(v['respuestas'])==5 and abs(sum(v['puntuaciones'].values())/5-score)<1e-8 and all(len(a['probabilities'])==5 and {b['value'] for b in a['probabilities']}==set(range(5)) and abs(sum(b['probability'] for b in a['probabilities'])-1)<1e-8 and abs(sum(b['value']*b['probability'] for b in a['probabilities'])-a['score'])<1e-8 and abs(v['puntuaciones'][a['name']]-(a['score']+1))<1e-8 for a in v['respuestas']))
check('objetivo4 no alcanzado',act['visual']['objetivo_4_alcanzado'] is False)
for name in ['calidad-viviendas-4-2026-10-17.md','hiperrealismo-registro.md']:
 before=subprocess.check_output(['git','show',expected+':docs/'+name]).decode();current=(r/'docs'/name).read_text();check('docs append conserva historia '+name,current.startswith(before.rstrip()) and current.count('Tanda 19 publicada y verificada:')==1)
check('estado local y manifiesto no mutados por auditoría',status==git('status','--porcelain') and mh==H(d/'manifest.json') and head==git('rev-parse','HEAD'))
result={'estado':'PASS','alcance':'Auditoría documental local y hashes; no repetición pública ni red/GPU/API/build','producto':head,'manifest_sha256':mh,'entradas_dossier':169,'anteriores_preservadas':159,'fuentes_congeladas':417,'integracion_sha256':xh,'checks':checks,'git_status_observado':status,'limites':['Recibos CI/Pages almacenados, no consulta remota nueva','Entradas genéricas8 y trofeos4 se solapan en2132: once semillas distintas, no doce','game.persist explícito antes de reload: persistencia explícita, no prueba de autoguardado','No juicios artísticos nuevos ni objetivo4 alcanzado']}
(out/'revision_recibos_publicacion_cpu.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ['checks','git_status_observado']},ensure_ascii=False));print('checks',len(checks))
