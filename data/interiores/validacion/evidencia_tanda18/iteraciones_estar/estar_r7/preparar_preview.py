from pathlib import Path
import json,hashlib,shutil,subprocess
r=Path.cwd();o=r/'.cache/calidad/tanda18';private=o/'estar_r7';base=o/'final_r6';p=o/'final_r7';p.mkdir(exist_ok=False);H=lambda f:hashlib.sha256(f.read_bytes()).hexdigest();freeze=json.loads((base/'preparado.json').read_text())['archivos'];assert all(H(base/f)==h for f,h in freeze.items())
for f in freeze:
 t=p/f;t.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(base/f,t)
for name,target in [('composicion_estar_salon.js','src/composicion_estar_salon.js'),('locales.js','src/locales.js'),('houses.js','src/houses.js'),('catalogo_vivienda.py','tools/interiores/catalogo_vivienda.py')]:shutil.copy2(private/name,p/target)
f=p/'tools/interiores/fotos_casa.py';s=f.read_text();assert s.count('localhost:8933')==1;f.write_text(s.replace('localhost:8933','localhost:8934'))
for gen in ['catalogo_vivienda.py','datos.py']:subprocess.run(['python3','-B','tools/interiores/'+gen],cwd=p,check=True)
old=json.loads((r/'data/objetos/vivienda.json').read_text())['objetos'];new=json.loads((p/'data/objetos/vivienda.json').read_text())['objetos'];assert len(old)==len(new)
modified=[]
for a,b in zip(old,new):
 assert a['id']==b['id']
 if a!=b:
  modified.append(a['id']);assert {k:v for k,v in a.items() if k not in ['partes','nombre','nota']}=={k:v for k,v in b.items() if k not in ['partes','nombre','nota']},a['id']
assert modified==['sofa_tres_plazas','sofa_dos_plazas','puff','alfombra_salon'],modified
state={'estado':'R7_PRIVADA_ESTARMODELOSTEXTILES','archivos':{f:H(p/f) for f in sorted(set(freeze)|{'src/composicion_estar_salon.js'})},'modelos_modificados':modified,'limites':'CopiaR6privada+programaestar/modelos, sin producto activo. Propiedades funcionales de los4modelos idénticas salvo nombre/nota/partes. Requiere revisión de cotas render/colisiones y capturas nuevas.'};(p/'preparado.json').write_text(json.dumps(state,ensure_ascii=False,indent=1)+'\n')
s=(o/'capturar_final_r6.py').read_text().replace('final_r6','final_r7').replace('R6_SALON_PRIVADA','R7_SALON_PRIVADA').replace('URL8933','URL8934').replace('R6 copia integrada','R7 copia privada con estar y modelos');(o/'capturar_final_r7.py').write_text(s)
print('R7 preparada',len(state['archivos']),modified)
