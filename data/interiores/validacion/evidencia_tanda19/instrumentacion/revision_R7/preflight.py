from pathlib import Path
from types import SimpleNamespace
import ast,sys,json,hashlib,subprocess
R=Path.cwd();F=R/'.cache/calidad/tanda19/capturador_consulta_r7.py';D=F.parent/'revision_capturador_consulta';src=F.read_text();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
old="spec=importlib.util.spec_from_file_location('consulta_completa',f)\nphoto=importlib.util.module_from_spec(spec);spec.loader.exec_module(photo)"
assert src.count(old)==1
src=src.replace(old,'photo=PHOTO');tail="sys.argv=[str(f),'trofeos','3'];photo.main()";assert src.count(tail)==1;src=src.replace(tail,'')
rows=[];saved=sys.argv[:]
try:
 for base in [False,True]:
  p=F.parent/('base_T18' if base else 'prototipo_r7');tree=ast.parse((p/'tools/interiores/fotos_casa.py').read_text());node=next(n for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='JS'for t in n.targets));photo=SimpleNamespace(JS=ast.literal_eval(node.value));sys.argv=[str(F)]+(['--base']if base else [])
  env={'__file__':str(F),'PHOTO':photo};exec(compile(src,str(F),'exec'),env)
  js=photo.JS%('"trofeos"',3,'null','null');out=D/('base.js'if base else'candidata.js');out.write_text(js)
  subprocess.run(['/Users/nestorguerra/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node','--check',str(out)],check=True,capture_output=True)
  if base:assert 'const consulta=false?'in js and 'x=canonical.x;z=canonical.z;'in js
  else:assert "consulta.length!==2"in js and 'if(consulta.length&&recortes)continue;'in js
  rows.append({'base':base,'sintaxis':'PASS','generated_sha':sha(out),'snapshot':str(p),'seal':sha(p/'preparado.json')})
finally:sys.argv=saved
P=F.parent/'comparativa_r7_consulta';receipt=json.loads((P/'procedencia.json').read_text());assert sha(F)==receipt['archivos']['capturador.py']
for f,h in receipt['archivos'].items():assert sha(P/f)==h,f
A=json.loads((P/'antes/casa_trofeos.json').read_text());B=json.loads((P/'despues/casa_trofeos.json').read_text());assert len(A)==len(B)==3
poses=[]
for a,b in zip(A,B):
 assert a['seed']==b['seed'];assert a['quality']==b['quality']=='alta';assert a['dpr']==b['dpr']==1
 assert len(a['vistas'])==len(b['vistas'])==2
 for k,(x,y)in enumerate(zip(a['vistas'],b['vistas'])):
  assert all(x[t]==y[t]for t in ['x','y','z','objetivo','fov']);assert x['clearance']['beforeRender']['free']and x['clearance']['afterRender']['free']and y['clearance']['beforeRender']['free']and y['clearance']['afterRender']['free']
  assert 'cobertura_consulta'not in x
  if k==1:
   q=y['cobertura_consulta'];assert q['esquinas_evaluadas']==16 and q['esquinas_recortadas']==0 and len(q['visibilidad'])==2 and all(v['muestras']>=3 and v['fraccion']>=.6 for v in q['visibilidad'])
  poses.append({'seed':a['seed'],'k':k,'pose_exacta':True,'libre_ambas':True})
seals=[]
for p in [F.parent/'base_T18',F.parent/'prototipo_r7']:
 m=json.loads((p/'preparado.json').read_text())['archivos'];assert len(m)==494
 for f,h in m.items():assert sha(p/f)==h,f
 seals.append({'path':str(p),'archivos':len(m),'estado_actual':'COINCIDE','limite':'Lectura actual del revisor; no observación propia de la captura pasada.'})
result={'estado':'PASS_PREFLIGHT_Y_RECIBOS','capturador':sha(F),'ramas':rows,'poses':poses,'archivos_recibo':len(receipt['archivos']),'fuentes_actuales':seals,'limites':'No ejecución JS/browser/GPU/API. K0 general sin guardia de cobertura del frente. Historial de estabilidad antes/durante capture depende del wrapper de raíz.'}
(D/'preflight.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'estado':result['estado'],'poses':len(poses),'fuentes':sum(s['archivos']for s in seals),'recibos':len(receipt['archivos'])}))
