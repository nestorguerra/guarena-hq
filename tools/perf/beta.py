"""Private, alternating before/after runs; never clears or loads a user's saved game.

python3 tools/perf/beta.py --before URL --after URL --out .cache/perf-beta/ab
--load-only --mbps 12: cold page/network, until the player has control after the intro.
--auto: measures adaptive experience separately from fixed-quality optimization.
"""
import argparse,json,sys,time,urllib.request
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'interiores'))
from cdp import Tab,WS,ERRS
LISTO = """(async()=>{const start=performance.now();let clicked=false;
while(performance.now()-start<240000){
 const g=window.game,l=document.getElementById('loading');
 if(g?.player&&(!l||l.hidden)){
  if(g.state==='play'&&g.player.char?.ready&&!g.cam.cinematic&&!window.guarenaIntro?.flying)return true;
  if(!window.guarenaIntroTimes&&!clicked){document.getElementById('bPlay')?.click();clicked=true;}
 }
 await new Promise(r=>setTimeout(r,50));
}throw Error('No control normal después de la carga: '+JSON.stringify(window.__errs));})()"""

class PrivateTab:
 def __enter__(self):
  v=json.load(urllib.request.urlopen('http://127.0.0.1:9333/json/version'))
  self.browser=WS(v['webSocketDebuggerUrl']);self.mid=0
  self.context=self.cmd('Target.createBrowserContext',{'disposeOnDetach':True})['browserContextId']
  tid=self.cmd('Target.createTarget',{'url':'about:blank','browserContextId':self.context})['targetId']
  pages=json.load(urllib.request.urlopen('http://127.0.0.1:9333/json/list'))
  T=Tab.__new__(Tab);T.id=tid;T.port=9333;T.ws=WS(next(p['webSocketDebuggerUrl'] for p in pages if p['id']==tid));T.ws.s.settimeout(1800);T.mid=0
  self.tab=T;T.call('Page.enable');T.call('Emulation.setFocusEmulationEnabled',{'enabled':True});T.call('Emulation.setDeviceMetricsOverride',dict(width=1440,height=900,deviceScaleFactor=2,mobile=False));T.call('Page.addScriptToEvaluateOnNewDocument',{'source':ERRS})
  return T
 def cmd(self,method,params):
  self.mid+=1;self.browser.send(json.dumps(dict(id=self.mid,method=method,params=params)))
  while True:
   m=json.loads(self.browser.recv())
   if m.get('id')==self.mid:
    if 'error' in m:raise RuntimeError(m['error'])
    return m['result']
 def __exit__(self,*args):
  self.cmd('Target.disposeBrowserContext',{'browserContextId':self.context});self.tab.ws.s.close();self.browser.s.close()

def install_test_importmap(T):
 # The packed game resolves its own dependencies, while external test helpers use
 # bare Three imports. Reuse the development page's exact mapping in this context.
 return T.ev("""(async()=>{const existing=document.querySelector('script[type="importmap"]');if(existing)return JSON.parse(existing.textContent);const html=await(await fetch('/index.html')).text();const source=new DOMParser().parseFromString(html,'text/html').querySelector('script[type="importmap"]');if(!source)throw Error('Test import map unavailable');const mapping=JSON.parse(source.textContent);const packed=[...document.scripts].map(s=>s.textContent).join('\\n').match(/https:\/\/cdn\\.jsdelivr\\.net\/npm\/three@[^/'"]+\/\\+esm/);if(packed)mapping.imports.three=packed[0];const script=document.createElement('script');script.type='importmap';script.textContent=JSON.stringify(mapping);document.head.append(script);return mapping;})()""")

def run(url,args):
 with PrivateTab() as T:
  fixture={'quality':'alta','qualityMode':'auto' if args.auto else 'manual','dynRes':args.auto,'money':321,'pick':'annie','modePref':'normal','weatherLive':False}
  T.call('Page.addScriptToEvaluateOnNewDocument',{'source':"{let seed=388;Math.random=()=>{seed|=0;seed=(seed+0x6d2b79f5)|0;let t=Math.imul(seed^(seed>>>15),1|seed);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}localStorage.setItem('guarena_hq_save',"+json.dumps(json.dumps(fixture))+');'})
  T.call('Network.enable');T.call('Network.setCacheDisabled',{'cacheDisabled':True})
  if args.mbps:
   T.call('Network.emulateNetworkConditions',dict(offline=False,latency=40,downloadThroughput=args.mbps*1000000/8,uploadThroughput=2000000/8))
  T.call('Page.navigate',{'url':url});T.ev(LISTO,timeout=300)
  out=T.ev("({control_ms:performance.now(),navigation:performance.getEntriesByType('navigation').map(r=>({bytes:r.transferSize,encoded:r.encodedBodySize,decoded:r.decodedBodySize,response_ms:r.responseEnd,dom_ms:r.domContentLoadedEventEnd})),motor:window.guarenaLoadLog,intro:window.guarenaIntroTimes,world:game.world.timings,quality:game.qKey,pr:game.renderer.getPixelRatio(),machine:game.machine||null,resources:performance.getEntriesByType('resource').map(r=>({name:r.name,bytes:r.transferSize,ms:r.duration})),errors:window.__errs})")
  if not args.load_only:
   install_test_importmap(T)
   T.ev("(async()=>{window.__P=await import('/tools/perflab.js');return true;})()")
   for route in ['walk','spin','drive']:
    out[route]=T.ev("(async()=>await __P.live("+json.dumps(dict(route=route,sec=args.seconds,warm=3,dynRes=args.auto))+"))()")
   out['end']=T.ev('({pr:game.renderer.getPixelRatio(),level:game.perf?.level||0,errors:window.__errs})')
  if out['errors'] or out.get('end',{}).get('errors'):raise RuntimeError('Console errors: '+str(out))
  return out

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--before',required=True);p.add_argument('--after',required=True);p.add_argument('--rounds',type=int,default=3);p.add_argument('--seconds',type=int,default=20);p.add_argument('--load-only',action='store_true');p.add_argument('--mbps',type=float,default=0);p.add_argument('--auto',action='store_true');p.add_argument('--out',required=True);a=p.parse_args()
 dest=Path(a.out);dest.mkdir(parents=True,exist_ok=True)
 (dest/'setup.json').write_text(json.dumps({**vars(a),'ready_method':'normal_intro_no_fast_forward','boot_seed':388,'weather_live':False},indent=1))
 for n in range(a.rounds):
  versions=[('before',a.before),('after',a.after)]
  for label,url in versions if n%2==0 else versions[::-1]:
   f=dest/(label+'_'+str(n)+'.json')
   if f.exists():raise RuntimeError('Output already exists; choose another run directory')
   d=run(url,a);f.write_text(json.dumps(d,ensure_ascii=False,indent=1));print(label,n,'control_ms',round(d['control_ms']),{k:d[k]['fps'] for k in ['walk','spin','drive'] if k in d},flush=True)
