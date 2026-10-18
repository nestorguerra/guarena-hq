from pathlib import Path
import sys,json,importlib.util
r=Path(__file__).resolve().parents[3];o=r/'.cache/calidad/tanda20';p=o/'prototipo_r1';f=p/'tools/interiores/fotos_casa.py'
spec=importlib.util.spec_from_file_location('dormitorio_r1_comun',f);photo=importlib.util.module_from_spec(spec);spec.loader.exec_module(photo)
commons=json.loads((o/'medidas/camaras_comunes_r1.json').read_text())['rows']
marker="        const clearance=cameraClearance(h,est,col,q);if(!clearance.free)continue;"
hook="        if(!COMMON[s+'|'+tipo]?.points.some(p=>Math.hypot(p.x-q.x,p.z-q.z)<1e-6))continue;\n".replace('COMMON',json.dumps(commons))
assert photo.JS.count(marker)==1;photo.JS=photo.JS.replace(marker,hook+marker)
sys.argv=[str(f),'dorm,dorm2','3'];photo.main()
