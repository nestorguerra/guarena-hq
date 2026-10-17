"""Runtime quality checks in a private Chrome context; hardware hints remain local.

Emulated hints check the selection logic, not performance of a different physical machine.
"""
import argparse,json,time,re
from pathlib import Path
from beta import PrivateTab,LISTO,install_test_importmap

p=argparse.ArgumentParser();p.add_argument('--url',required=True);p.add_argument('--out',required=True);p.add_argument('--seconds',type=int,default=90);a=p.parse_args()
out=Path(a.out);out.mkdir(parents=True,exist_ok=False)
report={'url':a.url,'runtime':{},'hint_scenarios':[]}
try:
 with PrivateTab() as T:
  T.call('Page.addScriptToEvaluateOnNewDocument',{'source':"if(!sessionStorage.getItem('fixture')){localStorage.setItem('guarena_hq_save',JSON.stringify({qualityMode:'auto',dynRes:true,weatherLive:false,pick:'annie',money:321}));sessionStorage.setItem('fixture','1');}"})
  T.call('Page.navigate',{'url':a.url});T.ev(LISTO,timeout=300)
  report['initial']=T.ev('({quality:game.qKey,auto:game.autoQuality,pr:game.renderer.getPixelRatio(),profile:game.machineProfile,hints:game.machine})')
  report['test_importmap']=install_test_importmap(T)
  T.ev("(async()=>{await import('/src/traffic.js');await import('/tools/playtest.js');window.__P=await import('/tools/perflab.js');game.perfGrace(3);return true;})()")
  T.ev("window.__autoTrace=[];window.__traceTimer=setInterval(()=>__autoTrace.push({ms:performance.now(),pr:game.renderer.getPixelRatio(),level:game.perf?.level,ema_fps:1/game.perf?.avg,visibility:document.visibilityState}),1000);true")
  report['runtime']['settling_walk']=T.ev('(async()=>await __P.live('+json.dumps(dict(route='walk',sec=a.seconds,warm=3,dynRes=True))+'))()',timeout=300)
  report['runtime']['steady_spin']=T.ev("(async()=>await __P.live({route:'spin',sec:20,warm:3,dynRes:true}))()",timeout=120)
  report['trace']=T.ev('clearInterval(__traceTimer);__autoTrace')
  T.shot(str(out/'automatic.jpg'))
  # Changing CSS viewport and native density must retain the configured pixel budget.
  T.call('Emulation.setDeviceMetricsOverride',dict(width=3840,height=2160,deviceScaleFactor=2,mobile=False))
  report['resize_4k']=T.ev("(async()=>{await new Promise(r=>setTimeout(r,1500));return {pr:game.renderer.getPixelRatio(),budget:game.machineProfile.maxPixels,canvas:[game.canvas.width,game.canvas.height],base:game.perf.base,ceiling:game.perf.ceiling};})()")
  x=report['resize_4k'];assert x['canvas'][0]*x['canvas'][1]<=x['budget']+8000,'Pixel budget lost on resize'
  T.call('Emulation.setDeviceMetricsOverride',dict(width=1440,height=900,deviceScaleFactor=2,mobile=False))
  # Freeze/resume exercises raw long intervals; deterministic tests separately cover hidden visibility events.
  T.call('Page.setWebLifecycleState',{'state':'frozen'});time.sleep(2);T.call('Page.setWebLifecycleState',{'state':'active'})
  # Headless Chrome leaves the page hidden after lifecycle activation. Explicitly
  # emulate the foreground return; otherwise its timers remain throttled.
  T.call('Emulation.setFocusEmulationEnabled',{'enabled':True})
  report['resume']=T.ev("(async()=>{await new Promise(r=>setTimeout(r,1200));return {pr:game.renderer.getPixelRatio(),controller:game.perf.pr,visibility:document.visibilityState,errors:window.__errs};})()")
  assert report['resume']['visibility']=='visible'
  assert abs(report['resume']['pr']-report['resume']['controller'])<.001,'Renderer/controller mismatch'
  T.ev("game.setQuality('alta');window.__oldDocument=true")
  T.call('Page.reload',{})
  for _ in range(600):
   try:
    if T.ev('!window.__oldDocument&&!!window.game'):break
   except RuntimeError:pass
   time.sleep(.1)
  else:raise RuntimeError('Reload not observed')
  T.ev(LISTO,timeout=300)
  report['manual_reload']=T.ev('({quality:game.qKey,auto:game.autoQuality,money:game.player.money,errors:window.__errs})')
  assert report['manual_reload']['quality']=='alta' and report['manual_reload']['auto'] is False
  assert report['manual_reload']['money']==321
  assert not report['resume']['errors'] and not report['manual_reload']['errors']
 for label,cores,ram,expected in [('unknown',None,None,'media'),('limited_hints',2,2,'baja')]:
  with PrivateTab() as T:
   script="Object.defineProperty(navigator,'hardwareConcurrency',{get:()=>CORE});Object.defineProperty(navigator,'deviceMemory',{get:()=>RAM});localStorage.setItem('guarena_hq_save',JSON.stringify({qualityMode:'auto',dynRes:true,weatherLive:false,pick:'annie'}));".replace('CORE',json.dumps(cores)).replace('RAM',json.dumps(ram))
   T.call('Page.addScriptToEvaluateOnNewDocument',{'source':script});T.call('Page.navigate',{'url':a.url});T.ev(LISTO,timeout=300)
   d=T.ev('({quality:game.qKey,auto:game.autoQuality,pr:game.renderer.getPixelRatio(),hints:game.machine,errors:window.__errs})');d['scenario']=label
   report['hint_scenarios'].append(d)
   if label=='unknown' and (re.search(r'swiftshader|llvmpipe|software rasterizer',d['hints']['gpu'] or '',re.I) or (d['hints']['maxTextureSize'] is not None and d['hints']['maxTextureSize']<4096)):expected='baja'
   assert d['quality']==expected and d['auto'] and not d['errors']
except Exception as error:
 report['error']=type(error).__name__+': '+str(error)
 raise
finally:
 (out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=1)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='trace'},ensure_ascii=False,indent=1))
