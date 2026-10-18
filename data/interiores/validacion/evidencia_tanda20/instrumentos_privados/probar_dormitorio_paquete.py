from pathlib import Path
import sys,json
r=Path.cwd();sys.path.insert(0,str(r/'tools/perf'));sys.path.insert(0,str(r/'tools/interiores'))
from beta import PrivateTab
from integracion import LISTO
o=r/'.cache/calidad/tanda20';js=(o/'revision_publicacion/dormitorios_publico.js').read_text()
with PrivateTab() as t:
 t.call('Page.addScriptToEvaluateOnNewDocument',{'source':"localStorage.setItem('guarena_hq_save',JSON.stringify({money:321,bank:700,quality:'alta',qualityMode:'manual',dynRes:false,weatherLive:false,pick:'annie'}));"})
 t.call('Page.navigate',{'url':'http://localhost:8920/dist/test.html?estilo=plastilina'})
 t.ev(LISTO,timeout=240)
 result=json.loads(t.ev(js,timeout=300));errors=json.loads(t.ev('JSON.stringify(window.__errs||[])'))
 (o/'dormitorio_paquete.json').write_text(json.dumps({'resultado':result,'consola':errors,'limites':'Paquete local previo al commit; no prueba Pages ni SHA público.'},ensure_ascii=False,indent=1)+'\n')
 print(json.dumps({'estado':result['estado'],'consola':errors,'rows':result['rows']},ensure_ascii=False))
 if result['estado']!='PASS' or errors:raise SystemExit(1)
