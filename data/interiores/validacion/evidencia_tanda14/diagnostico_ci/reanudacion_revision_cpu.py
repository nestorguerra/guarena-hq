import contextlib,hashlib,io,json,sys,types
from pathlib import Path
ROOT=Path.cwd();source=ROOT/'tools/interiores/botin_pruebas.py'
ns={'__name__':'review_diagnostic','__file__':str(source)};exec(compile(source.read_text(),str(source),'exec'),ns)
out=ROOT/'.cache/calidad/botin_sin_intro_ci_revision_cpu';out.mkdir(exist_ok=True)
rows=[]
def probe(name,fail=None,diagnostic_fail=False,close_fail=False,quality=None,wrong=None,sin_intro=False,intro_fail=None):
 requested=quality or 'alta'
 events=[];live=[False];ready=[0]
 class T:
  def call(self,method,params=None):
   events.append(method)
   if method=='Page.addScriptToEvaluateOnNewDocument':
    encoded=params['source'].split("localStorage.setItem('guarena_hq_save',",1)[1].split(");localStorage.",1)[0]
    assert ('window.claude={hot:{data:{resume:true}}}' in params['source'])==sin_intro
    (out/(name+'_init.js')).write_text(params['source'])
    fixture=json.loads(json.loads(encoded));assert fixture['quality']==requested and fixture['qualityMode']=='manual' and fixture['dynRes'] is False and fixture['money']==321 and fixture['bag']==[]
   return {}
  def ev(self,text,timeout=None):
   if text.startswith('({documento:'):
    events.append('diagnose');assert live[0];assert timeout==5
    if diagnostic_fail:raise RuntimeError('diagnostic-only')
    return {'documento':'complete','estado':'loading','errores':['test-only']}
   if text.startswith('!!window.guarenaIntroTimes'):
    events.append('introguard'+str(ready[0]));assert sin_intro;return intro_fail==('initial' if ready[0]==1 else 'reload')
   if text==ns['RENDER']:
    events.append('render'+str(ready[0]));q=requested;auto=False
    if wrong==('initial' if ready[0]==1 else 'reload'):q='media'
    if wrong==('autoInitial' if ready[0]==1 else 'autoReload'):auto=True
    return {'calidad':q,'automatica':auto,'dpr':1,'tamano':[1280,720],'renderer':None}
   if text==ns['LISTO']:
    ready[0]+=1;events.append('ready'+str(ready[0]))
    if fail==('initial' if ready[0]==1 else 'reload'):raise RuntimeError('original-'+fail)
    return True
   if text.startswith('// Acciones reales'):
    events.append('pickup')
    if fail=='pickup':raise RuntimeError('original-pickup')
    return {'dinero':400,'mochila':[{'id':'joyero','name':'joyero','value':100}],'errores':[]}
   if text.startswith('!window.__documentoAnterior'):return True
   if text.startswith('({dinero:'):return {'dinero':400,'mochila':[{'id':'joyero','name':'joyero','value':100}],'evo':'testigo_evo','fija':'testigo_fija','errores':[]}
   return None
 class P:
  def __enter__(self):events.append('enter');live[0]=True;return T()
  def __exit__(self,*a):events.append('close');live[0]=False
 # Make close error explicit without suppressing any original exception.
 oldexit=P.__exit__
 def exit_(self,*a):
  oldexit(self,*a)
  if close_fail:raise RuntimeError('close-only')
 P.__exit__=exit_;ns['PrivateTab']=P
 oldargv=sys.argv;sys.argv=['botin_pruebas.py','--informe',str(out/(name+'.json'))]+(['--calidad',quality] if quality else [])+(['--sin-intro'] if sin_intro else [])
 log=io.StringIO()
 try:
  with contextlib.redirect_stdout(log):code=ns['main']()
 finally:sys.argv=oldargv
 report=json.loads((out/(name+'.json')).read_text());bad=bool(fail or close_fail or wrong or intro_fail)
 assert code==(1 if bad else 0),(name,code,report)
 assert report['estado']==('FAIL' if bad else 'PASS')
 if fail:
  assert events.index('diagnose')<events.index('close');assert any('original-'+fail in s for s in report['errores']);assert 'original-'+fail in log.getvalue()
  assert ('diagnostico_error' in report)==diagnostic_fail
 elif wrong or intro_fail:assert events.index('diagnose')<events.index('close')
 else:assert 'diagnose' not in events
 rows.append({'name':name,'pass':True,'events':events,'exit':code,'state':report['estado'],'errors':report['errores'],'diagnosticError':report.get('diagnostico_error'),'stdout':log.getvalue()})
for name,kw in [('success',{}),('initial_failure',{'fail':'initial'}),('pickup_failure',{'fail':'pickup'}),('reload_failure',{'fail':'reload'}),('diagnostic_failure',{'fail':'initial','diagnostic_fail':True}),('close_failure_after_success',{'close_fail':True})]:probe(name,**kw)
for name,kw in [('baja_success',{'quality':'baja'}),('wrong_initial_profile',{'quality':'baja','wrong':'initial'}),('wrong_reloaded_profile',{'quality':'baja','wrong':'reload'}),('auto_initial',{'quality':'baja','wrong':'autoInitial'}),('auto_reloaded',{'quality':'baja','wrong':'autoReload'})]:probe(name,**kw)
for name,kw in [('resume_success',{'quality':'baja','sin_intro':True}),('resume_initial_intro',{'sin_intro':True,'intro_fail':'initial'}),('resume_reload_intro',{'sin_intro':True,'intro_fail':'reload'})]:probe(name,**kw)
result={'scope':'actual main/diagnosticar with fake PrivateTab/CDP; no browser or GPU; no claim about CI failure cause','sourceSHA':hashlib.sha256(source.read_bytes()).hexdigest(),'cases':rows};(out/'report.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'sourceSHA':result['sourceSHA'],'cases':len(rows),'allPass':True}))
