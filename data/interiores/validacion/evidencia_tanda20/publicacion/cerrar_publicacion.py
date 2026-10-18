from pathlib import Path
import json,hashlib,subprocess,shutil,datetime
r=Path.cwd();o=r/'.cache/calidad/tanda20';v=r/'data/interiores/validacion';e=v/'evidencia_tanda20'
J=lambda f:json.loads(f.read_text());H=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
def W(f,d):f.parent.mkdir(parents=True,exist_ok=True);f.write_text(json.dumps(d,ensure_ascii=False,indent=1)+'\n')
def cp(f,q):q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(f,q)
sha=(o/'commit_producto.txt').read_text().strip();assert len(sha)==40
assert subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()==sha
assert not subprocess.check_output(['git','status','--porcelain'],text=True).strip()
assert all(H(r/f)==h for f,h in J(o/'estado_candidato.json')['archivos'].items())
x=J(o/'revision_publicacion/ejecuciones/integracion_publica_producto.json');ci=J(o/'main_actualizado.json');pages=J(o/'pages_final.json')
assert x['revision_servida']==x['revision_tras_recarga']==sha
assert x['http_status']==200 and not x['errores'] and not x['consola'] and not x['consola_tras_recarga']
assert x['carga_partida']==x['recarga_partida']
assert len(x['entradas'])==8 and x['trofeos']['estado']=='PASS' and x['dormitorios']['estado']=='PASS'
assert [row['seed'] for row in x['dormitorios']['rows']]==[2786,3244,1689,2132,5157,1594]
assert all(row['estado']=='PASS' for row in x['dormitorios']['rows'])
assert x['annie']['kits']==5 and len(x['comercios'])==3
assert ci['main_verificado']==ci['commit']==pages['headSha']==sha and pages['conclusion']=='success' and pages['status']=='completed'
assert ci['ci']['headSha']==sha and ci['ci']['status']=='completed' and ci['ci']['conclusion']=='success'
assert {'validate_signs','validate_interiors'}<={j['name'] for j in ci['ci']['jobs']}
assert all(j['conclusion']=='success' for j in ci['ci']['jobs'])
assert {'build','deploy'}<={j['name'] for j in pages['jobs']} and all(j['conclusion']=='success' for j in pages['jobs'])
workflow=json.loads(subprocess.check_output(['/opt/homebrew/bin/gh','api','repos/nestorguerra/guarena-hq/actions/runs/'+str(pages['databaseId']),'--jq','{id,path,head_sha,status,conclusion}'],text=True));assert workflow['path']=='.github/workflows/pages.yml' and workflow['head_sha']==sha and workflow['conclusion']=='success'
assert subprocess.check_output(['/opt/homebrew/bin/gh','api','repos/nestorguerra/guarena-hq/branches/main','--jq','.commit.sha'],text=True).strip()==sha
old=J(e/'manifest.json')['archivos'];assert all(H(e/f)==h for f,h in old.items())
assert len(J(o/'validacion_ejecuciones.json'))==10 and all(i['exit_code']==0 for i in J(o/'validacion_ejecuciones.json'))
assert not (e/'publicacion').exists() and not (v/'publicacion_tanda20.json').exists()
cp(e/'manifest.json',e/'publicacion/manifest_pre_publicacion.json')
for f in ['main_actualizado.json','pages_final.json','cerrar_publicacion.py','publicar_tras_ci.py']:cp(o/f,e/'publicacion'/f)
W(e/'publicacion/pages_workflow.json',workflow)
for f in ['verificar_publico.py','trofeos_publico.js','dormitorios_publico.js','preparado.json']:cp(o/'revision_publicacion'/f,e/'publicacion'/f)
cp(o/'revision_publicacion/ejecuciones/integracion_publica_producto.json',v/'integracion_publica_tanda20.json')
cp(v/'integracion_publica_tanda20.json',e/'publicacion/integracion_publica_tanda20.json')
rep={'fecha':datetime.datetime.now(datetime.timezone.utc).isoformat(),'tanda':20,'estado':'publicada_y_verificada_mejoras_pausadas_por_usuario','commit':sha,'url':x['url'],'ci':{'run':ci['ci']['databaseId'],'estado':'success','url':ci['ci']['url']},'pages':{'run':pages['databaseId'],'estado':'success','url':pages['url']},'prueba_publica':{'informe':'data/interiores/validacion/integracion_publica_tanda20.json','sha256':H(v/'integracion_publica_tanda20.json'),'sha_antes_y_despues':sha,'vecinos':8,'trofeos_reales':4,'dormitorios_puertas':[2786,3244,1689,2132,5157],'joven_individual':1594,'camas_residente_y_salida':True,'hide_unhide_y_salida':True,'annie_kits':5,'comercios_con_acciones':3,'partida_ficticia_persistencia_explicita':True},'visual':{'nueva_nota_formal':False,'objetivo_4_alcanzado':False,'revisiones_independientes':'Aceptan publicación parcial; pendientes documentados.'},'limites':'No4/5,25%,FPS ni beta terminada. Reposición privada al punto de uso, no recorrido desde puerta. Prueba dormir por residente; siesta jugador en Annie. Lectura dormitorio por enlaces/soportes nominales/registro, sin sentarse/leer. Persistencia por game.persist() explícito, no certifica autoguardado. Mejoras pausadas por orden del usuario.'}
W(v/'publicacion_tanda20.json',rep);cp(v/'publicacion_tanda20.json',e/'publicacion/publicacion_tanda20.json')
text=f'''\n\nTanda20 parcial publicada y verificada: `{sha}`, CI {ci['ci']['databaseId']} y Pages {pages['databaseId']} en verde. El paquete público sirve el SHA exacto antes/después de recargar. Pasan ocho vecinos, cuatro salas de trofeos y bancos previos, cinco puertas dormitorio y la individual joven1594: camas mediante residente real lieOnBed/wake, hideIn/unhide con salida libre. Lectura3244 conserva mesa/biblioteca/libros y registro de asiento; no se ejecuta leer/sentarse allí. Annie mantiene cinco kits/caja/siesta/decoración, tres comercios con acciones sin compras y partida ficticia conservada tras persistencia explícita y recarga, consola vacía. Se pausa el trabajo por orden del usuario. Sin nueva puntuación formal;4/5,25% y beta completa pendientes. Recibo: data/interiores/validacion/publicacion_tanda20.json.\n'''
for name in ['docs/calidad-viviendas-4-2026-10-17.md','docs/hiperrealismo-registro.md']:
 q=r/name;s=q.read_text();assert 'Tanda20 parcial publicada y verificada:' not in s;q.write_text(s.rstrip()+text)
s=J(v/'resumen_viviendas.json');s['publicacion']=rep;W(v/'resumen_viviendas.json',s)
assert all(H(e/f)==h for f,h in old.items())
W(e/'manifest.json',{'fecha':'2026-10-18','archivos':{str(f.relative_to(e)):H(f) for f in sorted(e.rglob('*')) if f.is_file() and f!=e/'manifest.json'}})
print(json.dumps(rep,ensure_ascii=False,indent=1))
