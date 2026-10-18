from pathlib import Path
import json,hashlib,subprocess
r=Path.cwd();o=r/'.cache/calidad/tanda20';H=lambda p:hashlib.sha256((r/p).read_bytes()).hexdigest();old=json.loads((r/'.cache/calidad/tanda17/regeneracion.json').read_text());names=list(old['archivos']);before={p:H(p) for p in names};freeze=json.loads((o/'estado_candidato.json').read_text())['archivos'];assert all(H(p)==h for p,h in freeze.items())
gens=['catalogo_vivienda.py','kits_vivienda.py','catalogo_vivienda_a.py','kits_vivienda_a.py','catalogo_vivienda_b.py','kits_vivienda_b.py','datos.py']
for g in gens:
 q=subprocess.run(['python3','-B','tools/interiores/'+g],cwd=r,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True);(o/('regenerar_'+g+'.log')).write_text(q.stdout);assert q.returncode==0,(g,q.stdout[-1000:])
assert all(H(p)==h for p,h in before.items());assert all(H(p)==h for p,h in freeze.items())
d={'estado':'PASS','generadores':gens,'archivos_identicos':len(before),'archivos':before,'entradas_congeladas_estables':len(freeze)};(o/'regeneracion.json').write_text(json.dumps(d,ensure_ascii=False,indent=1)+'\n');print(json.dumps(d,ensure_ascii=False,indent=1))
