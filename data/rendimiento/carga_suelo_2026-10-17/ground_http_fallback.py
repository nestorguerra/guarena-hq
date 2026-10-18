"""Prepared private HTTP-404 integration probe; run only when the GPU owner authorizes it."""
import argparse
import base64
import hashlib
import json
import re
import sys
import threading
import time
import traceback
import types
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools/perf'))
from beta import PrivateTab, LISTO

NAMES = ['asphalt_02', 'dirty_concrete', 'dry_ground_01', 'gravel_floor_02', 'sparse_grass', 'withered_grass']
PATHS = ['/assets/tex/' + n + s + '.jpg' for n in NAMES for s in ('_d', '_n')]
FAILED = ['/assets/tex/asphalt_02_d.jpg', '/assets/tex/dirty_concrete_n.jpg']

PROBE = r"""(async()=>{
 const g=game, fx=g.world.groundFx;
 const layers=async(t,failed,flat)=>{
  if(!t?.image?.data)return {observable:false};
  const {width:w,height:h,depth,data:d}=t.image, stride=w*h*4, out=[];
  for(let j=0;j<depth;j++){
   const a=d.subarray(j*stride,(j+1)*stride); let mismatches=0;
   for(let i=0;i<a.length;i++)if(a[i]!==flat[i%4])mismatches++;
   out.push({layer:j,expectedMissing:j===failed,flat,mismatchedBytes:mismatches,
    sha256:Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256',a))).map(v=>v.toString(16).padStart(2,'0')).join('')});
  }
  return {observable:true,width:w,height:h,depth,bytes:d.byteLength,layers:out};
 };
 return {control:g.state==='play'&&!!g.player.char?.ready&&!g.cam.cinematic&&!window.guarenaIntro?.flying,
  quality:g.qKey,qualityMode:g.save.qualityMode,dynRes:g.save.dynRes,weatherLive:g.save.weatherLive,
  plastilina:window.GUARENA_PLASTILINA===true, intro:window.guarenaIntroTimes,
  control_ms:performance.now(),player:g.player.pos.toArray(),
  ground:{on:!!fx?.on,normals:!!fx?.normals,mean:fx?.mean,
   albedo:await layers(fx?.det,0,[128,128,128,255]),normal:await layers(fx?.detN,1,[128,128,255,255])},
  church:!!g.scene.getObjectByName('hiper:iglesia'),errors:window.__errs,
  resources:performance.getEntriesByType('resource').filter(r=>r.name.startsWith(location.origin)).map(r=>({url:r.name,status:r.responseStatus,decoded:r.decodedBodySize})),
  glError:g.renderer.getContext().getError()};
})()"""


def main():
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('--candidate',type=Path,default=ROOT/'.cache/perf-beta/candidate-ground/dist')
 p.add_argument('--out',type=Path,default=ROOT/'.cache/perf-beta/ground-http-fallback')
 p.add_argument('--execute',action='store_true',help='Explicitly use the existing muted Chrome on 9333 / GPU')
 a=p.parse_args()
 if not a.execute:p.error('Prepared instrument only; --execute is required to use Chrome/GPU')
 candidate=a.candidate.resolve(); out=a.out.resolve()
 out.mkdir(parents=True,exist_ok=False)
 report={'status':'STARTED','scope':'real HTTP 404, normal intro, private browser context','expected404':FAILED,
         'candidate':str(candidate),'http':[],'events':[],'checks':{},'limits':['No test of indefinitely pending requests','No visual quality approval','No performance claim']}
 server=None; thread=None
 def save():
  (out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 def check(name,value):
  report['checks'][name]=bool(value)
  if not value:raise AssertionError(name)
 try:
  html=(candidate/'test.html').read_text()
  report['html_sha256']=hashlib.sha256(html.encode()).hexdigest()
  match=re.search(r'<script\b[^>]*\bid=["\']assetdata["\'][^>]*>(.*?)</script>',html,re.S)
  check('assetdata_present',match is not None)
  embedded=json.loads(match.group(1))
  check('12_ground_files_external',all(path.removeprefix('/assets/') not in embedded for path in PATHS))
  check('all_12_original_files_exist',all((candidate/path.lstrip('/')).is_file() for path in PATHS))
  report['asset_sha256']={path:hashlib.sha256((candidate/path.lstrip('/')).read_bytes()).hexdigest() for path in PATHS}
  class Handler(SimpleHTTPRequestHandler):
   def log_message(self,*args):pass
   def log_request(self,code='-',size='-'):
    report['http'].append({'method':self.command,'path':self.path,'status':int(code),'size':size,'time':time.time()})
   def end_headers(self):
    self.send_header('Cache-Control','no-store');super().end_headers()
   def do_GET(self):
    path=urlsplit(self.path).path
    if path in FAILED:
     self.send_error(404,'Intentional missing ground JPEG');return
    if path=='/favicon.ico':
     # No product favicon exists; answer a non-error to avoid an unrelated synthetic 404.
     self.send_response(204);self.end_headers();return
    super().do_GET()
  server=ThreadingHTTPServer(('127.0.0.1',0),partial(Handler,directory=str(candidate)))
  thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
  origin='http://127.0.0.1:'+str(server.server_address[1]);url=origin+'/test.html?estilo=real'
  report['url']=url
  with PrivateTab() as T:
   requests={}
   def tracked_call(self,method,params=None):
    self.mid+=1; mid=self.mid
    self.ws.send(json.dumps({'id':mid,'method':method,'params':params or {}}))
    while True:
     m=json.loads(self.ws.recv())
     if m.get('id')==mid:
      if 'error' in m:raise RuntimeError(m['error'])
      return m
     name=m.get('method',''); q=m.get('params',{})
     if name=='Network.requestWillBeSent':
      u=q['request']['url'];requests[q['requestId']]=u
      if u.startswith(('http://','https://')):report['events'].append({'method':name,'id':q['requestId'],'url':u})
     elif name=='Network.responseReceived':
      r=q['response'];u=r['url']
      if u.startswith(('http://','https://')):report['events'].append({'method':name,'id':q['requestId'],'url':u,'status':r['status'],'fromDiskCache':r.get('fromDiskCache',False),'fromServiceWorker':r.get('fromServiceWorker',False)})
     elif name=='Network.loadingFailed':
      report['events'].append({'method':name,'url':requests.get(q['requestId']),'details':q})
     elif name in ('Runtime.exceptionThrown','Runtime.consoleAPICalled','Log.entryAdded'):
      report['events'].append({'method':name,'details':q})
   T.call=types.MethodType(tracked_call,T)
   T.ws.s.settimeout(330)
   for domain in ('Runtime','Log','Network'):T.call(domain+'.enable')
   T.call('Network.setCacheDisabled',{'cacheDisabled':True})
   T.call('Emulation.setDeviceMetricsOverride',dict(width=1280,height=720,deviceScaleFactor=1,mobile=False))
   fixture={'quality':'alta','qualityMode':'manual','dynRes':False,'weatherLive':False,'pick':'annie'}
   T.call('Page.addScriptToEvaluateOnNewDocument',{'source':'localStorage.setItem("guarena_hq_save",'+json.dumps(json.dumps(fixture))+');'})
   T.call('Page.navigate',{'url':url})
   T.ev(LISTO,timeout=300)  # Unmodified beta.py readiness; no intro.step/frame/time mutation.
   report['state']=state=T.ev(PROBE,timeout=30)
   save()
   check('normal_control_and_high_quality',state['control'] and state['quality']=='alta' and not state['plastilina'])
   check('manual_no_adaptation_no_live_weather',state['qualityMode']=='manual' and state['dynRes'] is False and state['weatherLive'] is False)
   intro=state.get('intro') or {}
   check('intro_normal_timing_present',all(k in intro for k in ('start','figure','skin','street','flight')) and list(intro[k] for k in ('start','figure','skin','street','flight'))==sorted(intro[k] for k in ('start','figure','skin','street','flight')) and state['control_ms']>intro['flight'])
   check('ground_active_and_church',state['ground']['on'] and state['ground']['normals'] and state['church'])
   for kind in ('albedo','normal'):
    tex=state['ground'][kind]
    check(kind+'_observable_six_layers',tex['observable'] and tex['depth']==6 and tex['bytes']==tex['width']*tex['height']*6*4)
    check(kind+'_exact_flat_only_missing',all((layer['mismatchedBytes']==0)==layer['expectedMissing'] for layer in tex['layers']))
   check('missing_albedo_mean',state['ground']['mean'][0]==128/255)
   # Real input after landing, no teleportation nor assignment to game control flags.
   T.call('Input.dispatchKeyEvent',{'type':'keyDown','key':'s','code':'KeyS','windowsVirtualKeyCode':83})
   try:
    report['movement']=T.ev('(async()=>{const p=game.player.pos.clone();const input=game.input.moveY;await new Promise(r=>setTimeout(r,400));return {input,before:p.toArray(),after:game.player.pos.toArray(),distance:Math.hypot(game.player.pos.x-p.x,game.player.pos.z-p.z)};})()',timeout=10)
   finally:T.call('Input.dispatchKeyEvent',{'type':'keyUp','key':'s','code':'KeyS','windowsVirtualKeyCode':83})
   check('player_input_moves',report['movement']['input']<0 and .02<report['movement']['distance']<5)
   report['end']=T.ev('({errors:window.__errs,control:game.state==="play"&&!game.cam.cinematic&&!window.guarenaIntro?.flying,glError:game.renderer.getContext().getError()})')
   check('no_js_exceptions_or_gl_error',not state['errors'] and not state['glError'] and not report['end']['errors'] and not report['end']['glError'] and report['end']['control'])
   (out/'after-fallback.png').write_bytes(base64.b64decode(T.call('Page.captureScreenshot',{'format':'png'})['result']['data']))
   T.ev('true') # Drain events queued before the final evaluation response.
  expected_urls={origin+p for p in FAILED}
  expected=[]; unexpected=[]
  for ev in report['events']:
   name=ev['method'];q=ev.get('details',{})
   if name=='Network.responseReceived' and ev['status']>=400:
    (expected if ev['url'] in expected_urls and ev['status']==404 else unexpected).append(ev)
   elif name=='Network.loadingFailed':
    (expected if ev['url'] in expected_urls and q.get('errorText')=='net::ERR_HTTP_RESPONSE_CODE_FAILURE' else unexpected).append(ev)
   elif name=='Runtime.exceptionThrown' or name=='Runtime.consoleAPICalled' and q.get('type')=='error':unexpected.append(ev)
   elif name=='Log.entryAdded' and q['entry'].get('level')=='error':
    e=q['entry'];known=e.get('source')=='network' and e.get('url') in expected_urls and re.search(r'\b404\b',e.get('text','')) is not None
    (expected if known else unexpected).append(ev)
  report['expectedErrors']=expected;report['unexpectedErrors']=unexpected
  check('no_unexpected_console_or_network_errors',not unexpected)
  for path in PATHS+['/assets/hq/iglesia.glb']:
   status=404 if path in FAILED else 200
   http=[x for x in report['http'] if urlsplit(x['path']).path==path]
   net=[e for e in report['events'] if e['method']=='Network.responseReceived' and e['url']==origin+path]
   check('http:'+path,len(http)==1 and http[0]['status']==status and len(net)==1 and net[0]['status']==status and not net[0]['fromDiskCache'] and not net[0]['fromServiceWorker'])
  check('only_two_server_errors',all(r['status']<400 or urlsplit(r['path']).path in FAILED and r['status']==404 for r in report['http']))
  report['status']='FUNCTIONAL_CHECKS_PASSED_VISUAL_PENDING'
 except Exception:
  report['status']='FAILED';report['failure']=traceback.format_exc();raise
 finally:
  if server:server.shutdown();server.server_close()
  if thread:thread.join(timeout=2)
  save()
 print(str(out/'report.json'))

if __name__=='__main__':main()
