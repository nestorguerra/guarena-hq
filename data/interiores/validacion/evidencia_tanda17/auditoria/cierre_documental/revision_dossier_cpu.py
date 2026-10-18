from pathlib import Path
import hashlib,json,datetime,math,subprocess
R=Path.cwd();D=R/'data/interiores/validacion/evidencia_tanda17';C=R/'.cache/calidad/tanda17'
def H(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def J(p):return json.loads(Path(p).read_text())
rows=[]
def ck(name,value,**extra):rows.append(dict(check=name,PASS=bool(value),**extra))
m=J(D/'manifest.json');actual={str(p.relative_to(D)) for p in D.rglob('*') if p.is_file() and p!=D/'manifest.json'}
ck('seal_identity',H(D/'manifest.json')=='127241ea73700f0b86f413889645a9ade73a9a5279f67c4e1b63f4edef8a9e88',sha256=H(D/'manifest.json'))
ck('inventory_exact',actual==set(m['archivos']) and len(actual)==294,files=len(actual),missing=sorted(set(m['archivos'])-actual),extra=sorted(actual-set(m['archivos'])))
bad=[k for k,v in m['archivos'].items() if H(D/k)!=v];ck('all_hashes',not bad,mismatch=bad)
freeze=J(D/'gates_finales/estado_candidato.json');ck('freeze415',len(freeze['archivos'])==415 and all(H(R/k)==v for k,v in freeze['archivos'].items()))
ck('freeze_copies_exact',(D/'gates_finales/estado_candidato.json').read_bytes()==(C/'estado_candidato.json').read_bytes()==(D/'auditoria/estado_candidato.json').read_bytes())
regen=J(D/'gates_finales/regeneracion.json');ck('regen22',regen['estado']=='PASS' and len(regen['generadores'])==5 and regen['archivos_identicos']==len(regen['archivos'])==22 and all(H(R/k)==v for k,v in regen['archivos'].items()))
gates=J(D/'gates_finales/validacion_ejecuciones.json');ck('gates9',len(gates)==9 and all(g['exit_code']==0 for g in gates))
for p in (D/'gates_finales').iterdir():
 source=R/'data/interiores/validacion'/p.name if p.name in ['casas.json','vivienda_estudio.json','integracion_juego.json','integracion_paquete.json'] else C/p.name
 ck('copy:'+str(p.relative_to(D)),p.read_bytes()==source.read_bytes())
contracts=J(D/'gates_finales/contratos.json')['pruebas'];ck('contracts73',len(contracts)==73 and all(c['estado']=='PASS' for c in contracts))
casas=J(D/'gates_finales/casas.json');ck('casas200',casas['casas']==len(casas['resultados'])==200 and casas['habitables']==1166 and casas['pendientes']==casas['errores']==0)
lab=J(D/'gates_finales/vivienda_estudio.json');ck('lab81',lab['semillas']==list(range(1,82)) and len(lab['resultados'])==81 and lab['errores']==0 and all(not x['errores'] for x in lab['resultados']))
lines=(D/'gates_finales/kits5.log').read_text().splitlines();ls=[x for x in lines if ' · s1' in x];ck('40kits5',len(ls)==40 and all(sum(x.count('s'+str(i)+' ') +x.count('s'+str(i)+':') for i in range(1,6))==5 and x.count('0 err')==5 for x in ls))
source=J(D/'gates_finales/integracion_juego.json');package=J(D/'gates_finales/integracion_paquete.json');routes=source['colisiones']+[source['colisiones_annie']]
ck('source96routes',[x['runs'] for x in routes]==[16,32,16,32] and all(not x['tunnels'] and not x['escapes'] for x in routes))
ck('integration_clean',all(not d['errores'] and not d['consola'] and d['carga_partida']==d['recarga_partida'] for d in [source,package]))
quality=J(R/'data/interiores/validacion/calidad_tanda17.json');ck('quality_copy',J(D/'calidad_tanda17.json')==quality)
ck('quality_maxima',all(max(x[k] for x in casas['resultados'])==v for k,v in quality['maximos'].items()),observed={k:max(x[k] for x in casas['resultados']) for k in quality['maximos']})
image=H(D/'capturas/final_R3/casa_estudio.jpg');ck('image_chain',image==H(R/'data/interiores/fichas/casa_estudio.jpg')=='cfe597964fc9e1c5626c9886a1521b01780fc4b5f558526003287dc4c7b04fc2')
for side in 'AB':
 f=J(D/f'juicios/visual_estudio_{side}.json');prefix=D/'juicios'/('estudio_'+side+'_'+f['request_sha256']);meta=J(str(prefix)+'.http-meta.json');raw=Path(str(prefix)+'.http-body');body=J(raw);normal=J(str(prefix)+'.json')
 ck('formal_bytes:'+side,meta['body_sha256']==H(raw) and meta['bytes_conservados']==raw.stat().st_size and meta['http_status']==200 and not meta['supera_limite'] and meta['request_id']==f['request_id'] and meta['ficha_sha256']==f['ficha_sha256']==image)
 ck('formal_answers:'+side,body['answers']==f['respuestas'] and body['model']==f['modelo'] and body['usage']==f['uso'] and normal['respuesta']==body and all(normal[k]==f[k]==meta[k] for k in ['request_id','request_sha256','ficha_sha256']))
 ok=len(f['respuestas'])==5 and len({a['name'] for a in f['respuestas']})==5
 scores=[]
 for a in f['respuestas']:
  ps=a['probabilities'];ok &= a['type']=='score' and 0<=a['confidence']<=1 and sorted(p['value'] for p in ps)==list(range(5)) and all(p['label']==str(p['value']+1) and 0<=p['probability']<=1 for p in ps)
  n=sum(p['value']*p['probability'] for p in ps);ok &= abs(sum(p['probability'] for p in ps)-1)<1e-9 and abs(n-a['score'])<1e-9 and abs(f['puntuaciones'][a['name']]-1-n)<1e-9;scores.append(n+1)
 ok &= abs(sum(scores)/5-f['media'])<1e-9 and not f['supera_umbral'] and quality['kits']['estudio']['ahora'][side]==f['media']
 ck('formal_schema_math:'+side,ok,mean=f['media'])
 ck('formal_active_equal:'+side,f==J(R/f'data/interiores/validacion/visual_estudio_{side}.json'))
ck('previous_review_exact',(D/'revisiones/cierre_integrado.md').read_bytes()==(R/'.cache/calidad_tanda17_revision.md').read_bytes()==(R/'data/interiores/revision_calidad_tanda17_2026-10-18.md').read_bytes())
old=J(D/'revisiones/revision_integracion_cpu.json');ck('previous36',old['state']=='PASS' and len(old['rows'])==36 and all(x['pass_'] for x in old['rows']))
result={'state':'PASS' if all(x['PASS'] for x in rows) else 'FAIL','scope':'Auditoría documental CPU, sin ejecución de tests/GPU/API/build/generadores. No CI/publicación ni puntuación artística nueva.','date':datetime.datetime.now(datetime.timezone.utc).isoformat(),'rows':rows}
(C/'revision_dossier_cpu.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(result['state'],len(rows));print([x for x in rows if not x['PASS']])
