import subprocess,json,hashlib,sys
from pathlib import Path
root=Path(__file__).resolve().parents[3]
out=root/'.cache/calidad/tanda16'
frozen=json.loads((out/'estado_candidato.json').read_text())['archivos']
for p,h in frozen.items():assert hashlib.sha256((root/p).read_bytes()).hexdigest()==h,p
seeds=','.join(map(str,range(1,82)))
commands=[
('contratos',['python3','-B','tools/interiores/casas_pruebas.py','--tanda','19','--informe',str(out/'contratos.json')]),
('kits5',['python3','-B','tools/interiores/validar.py','--semillas','1,2,3,4,5']),
('casas200',['python3','-B','tools/interiores/validar.py','--casas','200','--exigir-todas']),
('kits81',['python3','-B','tools/interiores/validar.py','vivienda_cocina','--semillas',seeds]),
('integracion_fuente',['python3','-B','tools/interiores/integracion.py','--colisiones']),
('build',['python3','-B','tools/build.py']),
('recursos',['python3','-B','tools/perf/tests/carga_assets.py']),
('marcas',['python3','-B','tools/rotulos/rotulos.py','validar','dist/test.html']),
('integracion_paquete',['python3','-B','tools/interiores/integracion.py','--paquete'])]
res=[]
for name,cmd in commands:
 print('Inicia',name,flush=True)
 with (out/(name+'.log')).open('w') as f:r=subprocess.run(cmd,cwd=root,stdout=f,stderr=subprocess.STDOUT)
 res.append({'nombre':name,'exit_code':r.returncode});(out/'validacion_ejecuciones.json').write_text(json.dumps(res,indent=2)+'\n')
 print('Finaliza',name,r.returncode,flush=True)
 if r.returncode:sys.exit(r.returncode)
for p,h in frozen.items():assert hashlib.sha256((root/p).read_bytes()).hexdigest()==h,p
