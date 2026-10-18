from pathlib import Path
import sys,json,importlib.util
r=Path(__file__).resolve().parents[3];o=r/'.cache/calidad/tanda18';p=o/'final_r8';f=p/'tools/interiores/fotos_casa.py'
spec=importlib.util.spec_from_file_location('captura_salon_r8',f);photo=importlib.util.module_from_spec(spec);spec.loader.exec_module(photo)
poses=json.loads((o/'final_r6/capturas/casa_salon.json').read_text())
marker="      if(!Number.isFinite(mejor))throw Error('sin cámara libre: '+tipo+'/'+s);"
hook='''
      const canonical=POSES.find(row=>row.seed===s)?.vistas[k];
      if(!canonical||canonical.fov!==fov||Math.abs(canonical.y-y-1.6)>1e-6||Math.hypot(canonical.objetivo[0]-cx,canonical.objetivo[1]-y-alturaObjetivo,canonical.objetivo[2]-cz)>1e-6)throw Error('marco R6 no coincide con sala R8');
      x=canonical.x;z=canonical.z;
      clearanceElegido=requireCameraClearance(h,est,col,{x,z},'pose fija R6 antes de fotografiar');
'''.replace('POSES',json.dumps(poses))
assert photo.JS.count(marker)==1;photo.JS=photo.JS.replace(marker,marker+hook)
sys.argv=[str(f),'salon','3'];photo.main()
