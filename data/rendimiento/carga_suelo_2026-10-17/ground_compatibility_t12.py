import sys,json,base64,hashlib
from pathlib import Path
sys.path.insert(0,'tools/perf')
from beta import PrivateTab,LISTO

out=Path('.cache/perf-beta/ground-compatibility-t12')
out.mkdir(exist_ok=False)
root=Path('.cache/perf-beta/candidate-ground-t12')
names=[n+s for n in ('asphalt_02','dirty_concrete','dry_ground_01','gravel_floor_02','sparse_grass','withered_grass') for s in ('_d.jpg','_n.jpg')]
report={}
for style in ('plastilina','real'):
 with PrivateTab() as T:
  T.call('Emulation.setDeviceMetricsOverride',dict(width=1280,height=720,deviceScaleFactor=1,mobile=False))
  T.call('Page.addScriptToEvaluateOnNewDocument',{'source':"localStorage.setItem('guarena_hq_save',JSON.stringify({quality:'alta',qualityMode:'manual',dynRes:false,weatherLive:false,pick:'annie'}));"})
  T.call('Network.enable');T.call('Network.setCacheDisabled',{'cacheDisabled':True})
  T.call('Page.navigate',{'url':'http://localhost:8920/.cache/perf-beta/candidate-ground-t12/dist/test.html?estilo='+style})
  T.ev(LISTO,timeout=300)
  state=T.ev("""(async()=>{const g=game,fx=g.world.groundFx,hash=async t=>{if(!t)return null;const i=t.image,d=i.data;return {width:i.width,height:i.height,depth:i.depth,bytes:d.byteLength,sha256:Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256',d))).map(v=>v.toString(16).padStart(2,'0')).join('')};};return {style:window.GUARENA_PLASTILINA,quality:g.qKey,pr:g.renderer.getPixelRatio(),control:g.state==='play'&&!g.cam.cinematic&&!window.guarenaIntro?.flying,ground:{on:fx?.on??false,normals:fx?.normals??false,albedo:await hash(fx?.det),normal:await hash(fx?.detN)},church:!!g.scene.getObjectByName('hiper:iglesia'),resources:performance.getEntriesByType('resource').filter(r=>r.name.includes('/tex/')||r.name.includes('/hq/iglesia.glb')).map(r=>({url:r.name,bytes:r.decodedBodySize,status:r.responseStatus})),errors:window.__errs,glError:g.renderer.getContext().getError()};})()""")
  report[style]=state;(out/'report.json').write_text(json.dumps(report,indent=1)+'\n')
  assert state['control'] and state['quality']=='alta' and not state['errors'] and not state['glError'],state
  requests=[x for x in state['resources'] if x['url'].split('/')[-1] in names]
  if style=='plastilina':assert not requests and not state['ground']['on']
  else:
   assert state['ground']['on'] and state['ground']['normals'] and state['church'],state
   assert sorted(x['url'].split('/')[-1] for x in requests)==sorted(names),requests
   for x in requests:
    name=x['url'].split('/')[-1];assert x['status']==200 and x['bytes']==(root/'assets/tex'/name).stat().st_size,x
   church=[x for x in state['resources'] if x['url'].endswith('/hq/iglesia.glb')]
   assert len(church)==1 and church[0]['status']==200 and church[0]['bytes']==(root/'assets/hq/iglesia.glb').stat().st_size
  png=base64.b64decode(T.call('Page.captureScreenshot',{'format':'png'})['result']['data']);(out/(style+'.png')).write_bytes(png)
  state['screenshot_sha256']=hashlib.sha256(png).hexdigest();(out/'report.json').write_text(json.dumps(report,indent=1)+'\n')
  print(style,'PASS',len(requests),'ground requests',flush=True)
