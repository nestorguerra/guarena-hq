from pathlib import Path
import json,hashlib,subprocess,tempfile,datetime
R=Path.cwd();D=R/'.cache/calidad/tanda17';S=D/'preview_final_r3'
def sha(x):return hashlib.sha256(x).hexdigest()
def H(p):return sha(Path(p).read_bytes())
def load(p):return json.loads(Path(p).read_text())
rows=[]
def check(label,ok,**details):
 rows.append(dict(check=label,pass_=bool(ok),**details))
 if not ok: print('FAIL',label,details)
base=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()
integ=load(D/'integracion_R3.json');freeze=load(D/'estado_candidato.json')
check('base_git',base==integ['base_git']==freeze['base_git'],base=base)
bad=[k for k,v in freeze['archivos'].items() if not (R/k).is_file() or H(R/k)!=v]
check('active_frozen',not bad,count=len(freeze['archivos']),mismatches=bad)
for k,v in integ['cambios_fuente'].items():
 before=subprocess.check_output(['git','show',base+':'+k]);active=(R/k).read_bytes();snap=(S/k).read_bytes()
 if k.endswith('fotos_casa.py'):snap=snap.replace(b'http://localhost:8926',b'http://localhost:8920')
 check('integration:'+k,sha(before)==v['antes'] and sha(active)==v['ahora'] and active==snap,sha256=sha(active))
for k in ['tools/interiores/catalogo_vivienda_b.py','tools/interiores/kits_vivienda_b.py','src/texturas/vivienda_b.js','src/houses.js']:
 check('sealed_R1_unchanged:'+k,(R/k).read_bytes()==(D/'estudio_final_r1/candidata'/k).read_bytes())
for k in ['data/objetos/vivienda_b.json','data/kits/vivienda_estudio.json','data/interiores/datos.json','src/interiores_datos.js']:
 check('derived_equals_preview:'+k,(R/k).read_bytes()==(S/k).read_bytes(),sha256=H(R/k))
patch=D/'validacion_t20_r3.patch'
check('validation_patch_seal',H(patch)==load(D/'validacion_t20_r3_preparada.json')['sha256'],sha256=H(patch))
with tempfile.TemporaryDirectory(prefix='t17_review_',dir=D) as td:
 for k in ['tools/interiores/casas_pruebas.js','.github/workflows/validar.yml']:
  p=Path(td)/k;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(subprocess.check_output(['git','show',base+':'+k]))
 out=subprocess.run(['git','apply','--unsafe-paths',str(patch)],cwd=td,text=True,capture_output=True)
 check('apply_sealed_patch_private',out.returncode==0,error=out.stderr)
 for k in ['tools/interiores/casas_pruebas.js','.github/workflows/validar.yml']:
  check('exact_patch_integrated:'+k,(Path(td)/k).read_bytes()==(R/k).read_bytes(),sha256=H(R/k))
active=(R/'tools/interiores/casas_pruebas.js').read_text()
for k in ['contratos_estudio_r2.fragment.js','contratos_tela.fragment.js']:
 text=(D/k).read_text().strip();check('literal_fragment:'+k,text in active,callbacks=text.count('await caso('),sha256=H(D/k))
for name in ['casa_estudio.jpg','casa_estudio.json','visual_estudio_A.json','visual_estudio_B.json']:
 orig=('data/interiores/fichas/' if name.startswith('casa') else 'data/interiores/validacion/')+name
 old=(R/'data/interiores/validacion/historico/calidad_tanda17_base'/name).read_bytes()
 check('history_exact_base:'+name,old==subprocess.check_output(['git','show',base+':'+orig]),sha256=sha(old))
image=R/'data/interiores/fichas/casa_estudio.jpg'
check('image_preview_active_archive',H(image)==integ['ficha'] and image.read_bytes()==(S/'data/interiores/fichas/casa_estudio.jpg').read_bytes() and image.read_bytes()==(R/('data/interiores/validacion/imagenes/'+integ['ficha']+'.jpg')).read_bytes(),sha256=H(image))
for letter in 'AB':
 f=load(R/f'data/interiores/validacion/visual_estudio_{letter}.json'); vals=[];ok=f['ficha_sha256']==H(image)
 for a in f['respuestas']:
  ps=a['probabilities'];score=sum(p['value']*p['probability'] for p in ps)
  ok &= len(ps)==5 and sorted(p['value'] for p in ps)==list(range(5)) and abs(sum(p['probability'] for p in ps)-1)<1e-8 and abs(score-a['score'])<1e-8 and abs(f['puntuaciones'][a['name']]-(score+1))<1e-8
  vals.append(score+1)
 ok &= abs(sum(vals)/len(vals)-f['media'])<1e-8 and f['supera_umbral']==False
 check('formal_arithmetic:'+letter,ok,mean=f['media'],request_id=f['request_id'])
regen=load(D/'regeneracion.json')
check('regeneration_receipt',regen['estado']=='PASS' and len(regen['generadores'])==5 and len(regen['archivos'])==regen['archivos_identicos']==22 and regen['entradas_congeladas_estables']==415 and all(H(R/k)==v for k,v in regen['archivos'].items()),count=22)
gates=load(D/'validacion_ejecuciones.json')
check('nine_gate_exits',len(gates)==9 and all(g['exit_code']==0 for g in gates),gates=gates)
contracts=load(D/'contratos.json')['pruebas']
check('browser_contracts_receipt',len(contracts)==73 and all(c['estado']=='PASS' for c in contracts),count=len(contracts))
for file in ['integracion_juego.json','integracion_paquete.json']:
 d=load(R/'data/interiores/validacion'/file)
 check('integration_receipt:'+file,d['errores']==[] and d['consola']==[],sha256=H(R/'data/interiores/validacion'/file))
 if file=='integracion_juego.json':
  routes=d['colisiones']+[d['colisiones_annie']]
  check('source_routes', [x['runs'] for x in routes]==[16,32,16,32] and all(not x['tunnels'] and not x['escapes'] for x in routes),runs=[x['runs'] for x in routes])
result={'state':'PASS' if all(r['pass_'] for r in rows) else 'FAIL','scope':'CPU de hashes y procedencia. Sin GPU/build/API ni repetición de gates. No evaluación artística.','date':datetime.datetime.now(datetime.timezone.utc).isoformat(),'rows':rows,'gates_snapshot':load(D/'validacion_ejecuciones.json')}
(D/'revision_integracion_cpu.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(result['state'],len(rows),'checks')
