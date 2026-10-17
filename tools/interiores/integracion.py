"""Juego real, inventario, entrada y partida de prueba en un contexto privado del Chrome de ensayos."""
import argparse, collections, json, os, sys, time, urllib.request
ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
sys.path.insert(0,os.path.join(ROOT,'tools','perf'))
from cdp import Tab, WS, ERRS

LISTO="""(async()=>{const t=performance.now();let pulsado=false;while(performance.now()-t<180000){const g=window.game,l=document.getElementById('loading');if(g?.player&&(!l||l.hidden)){const intro=window.guarenaIntroTimes;if(intro&&!intro.flight){await new Promise(r=>setTimeout(r,100));continue;}if(window.guarenaIntro?.flying){for(let i=0;i<8;i++)window.guarenaIntro.step(.1);await new Promise(r=>setTimeout(r,10));continue;}if(g.state==='play'&&g.player.char&&!g.cam.cinematic)return true;if(!intro&&!pulsado){document.getElementById('bPlay')?.click();pulsado=true;}}await new Promise(r=>setTimeout(r,100));}throw Error('juego no preparado: '+JSON.stringify(window.__errs));})()"""


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--paquete',action='store_true');parser.add_argument('--colisiones',action='store_true');opts=parser.parse_args()
    v=json.load(urllib.request.urlopen('http://127.0.0.1:9333/json/version'));browser=WS(v['webSocketDebuggerUrl']);mid=0
    def command(method,params):
        nonlocal mid
        mid+=1;browser.send(json.dumps(dict(id=mid,method=method,params=params)))
        while True:
            r=json.loads(browser.recv())
            if r.get('id')==mid:
                if 'error' in r:raise RuntimeError(r['error'])
                return r['result']
    contexto=command('Target.createBrowserContext',{'disposeOnDetach':True})['browserContextId']
    informe={'url':'http://localhost:8920/'+('dist/test.html' if opts.paquete else 'index.html')+'?estilo=plastilina','errores':[]}
    try:
        tid=command('Target.createTarget',{'url':'about:blank','browserContextId':contexto})['targetId']
        tabs=json.load(urllib.request.urlopen('http://127.0.0.1:9333/json/list'));endpoint=next(t['webSocketDebuggerUrl'] for t in tabs if t['id']==tid)
        T=Tab.__new__(Tab);T.id=tid;T.port=9333;T.ws=WS(endpoint);T.ws.s.settimeout(1800);T.mid=0
        T.call('Page.enable');T.call('Emulation.setDeviceMetricsOverride',dict(width=960,height=540,deviceScaleFactor=1,mobile=False))
        T.call('Page.addScriptToEvaluateOnNewDocument',{'source':ERRS})
        # Datos ficticios solo en el contexto privado; comprueba que HQ no escribe las otras dos partidas.
        fixture="localStorage.setItem('guarena_hq_save',JSON.stringify({money:321,bag:[],pick:'annie',modePref:'normal',bank:700,homeDecor:[{id:'cuadro',x:0,y:4.7,z:4.9,ry:Math.PI,seed:23}]}));localStorage.setItem('guarena_evo_save',JSON.stringify({testigo:'evo'}));localStorage.setItem('guarena_save',JSON.stringify({testigo:'fija'}));"
        T.call('Page.addScriptToEvaluateOnNewDocument',{'source':"if(location.origin==='http://localhost:8920'&&!sessionStorage.getItem('fixture')){"+fixture+"sessionStorage.setItem('fixture','1');}"})
        T.call('Page.navigate',{'url':informe['url']});T.ev(LISTO,timeout=240)
        informe['carga_partida']=json.loads(T.ev("JSON.stringify({dinero:game.player.money,banco:game.homeSafe.bank,decoracion:game.save.homeDecor,evo:localStorage.getItem('guarena_evo_save'),fija:localStorage.getItem('guarena_save')})"))
        if informe['carga_partida']['dinero']!=321:informe['errores'].append('no carga el dinero de la partida HQ')
        if not opts.paquete:
            inv=json.loads(T.ev("(async()=>{const I=await import('/tools/interiores/inventario.js');return JSON.stringify(await I.inventario());})()",timeout=600))
            rows=inv['interiors'];inv['resumen']={'puertas':inv['puertas'],'interiores':len(rows),'por_estado':dict(collections.Counter(r['estado'] for r in rows))}
            json.dump({'version':1,**inv},open(os.path.join(ROOT,'data','interiors_inventory.json'),'w'),ensure_ascii=False,indent=1)
            informe['inventario']=inv['resumen'];informe['errores']+=inv['errores']
            informe['pueblo']=json.loads(T.ev("(async()=>{const V=await import('/tools/interiores/validar.js');const seeds=game.interiors.doors.filter(d=>d.seed>=1000&&!d.owner&&!d.venue&&!d.church).map(d=>d.seed);return JSON.stringify(await V.validarCasas(seeds,{exigirTodas:true}));})()",timeout=900))
            p=informe['pueblo'];json.dump(dict(alcance='pueblo',exigencia=dict(exigirTodas=True),casas=len(p),habitables=sum(r['cobertura']['habitables'] for r in p),pendientes=sum(len(r['cobertura']['faltantes']) for r in p),errores=sum(len(r['errores']) for r in p),resultados=p),open(os.path.join(ROOT,'data','interiores','validacion','casas_pueblo.json'),'w'),ensure_ascii=False,indent=1)
            for r in p:informe['errores']+=r['errores']
        informe['entradas']=json.loads(T.ev("""(async()=>{const out=[];let elegidas=0;for(const d of game.interiors.doors.filter(d=>d.seed>=1000&&!d.owner&&!d.venue&&!d.church)){const t=performance.now();const h=await game.interiors.enter(d,{mode:'visit',silent:true});const ms=performance.now()-t;const tv=h.pieces.tv[0];if(tv){const m=tv.mesh.material;m.emissiveIntensity=.85;if(m.emissiveIntensity!==.85)throw Error('pantalla no responde');m.emissiveIntensity=0;}const L=game.interiors.life;if(L&&L.people[0]&&h.pieces.bed[0]){L.lieOnBed(L.people[0],h.pieces.bed[0]);if(L.people[0].state!=='sleep')throw Error('no duerme');}out.push({seed:d.seed,plano:h.profile.layout,plantas:h.levels?.length||1,entrada_ms:+ms.toFixed(1),habitaciones:h.estancias.length});game.interiors.leave(true);if(++elegidas>=8)break;}return JSON.stringify(out);})()""",timeout=600))
        if any(r['entrada_ms']>1500 for r in informe['entradas']):informe['errores'].append('entrada real superior a 1500 ms')
        informe['annie']=json.loads(T.ev("""(async()=>{
          const d=game.interiors.doors.find(d=>d.owner==='annie'),t=performance.now(),h=await game.interiors.enter(d,{silent:true}),ms=performance.now()-t;
          const safe=h.inter.find(i=>i.type==='safe'),bed=h.inter.find(i=>i.type==='bed');if(!safe||!bed)throw Error('Annie sin caja fuerte o cama');
          const guardado=JSON.stringify(game.save.homeDecor),decor=game.decor.items.map(i=>({id:i.rec.id,x:i.obj.position.x-h.origin.x,y:i.obj.position.y,z:i.obj.position.z-h.origin.z}));
          if(decor.length!==1||Math.abs(decor[0].y-4.7)>1e-8||Math.abs(decor[0].z-4.9)>1e-8)throw Error('decoración guardada de Annie alterada');
          game.homeSafe.option(safe).run();game.homeSafe.move(50);if(game.homeSafe.bank!==750||game.player.money!==271)throw Error('depósito en caja fuerte');
          game.homeSafe.move(-50);game.homeSafe.menu.close();if(game.homeSafe.bank!==700||game.player.money!==321)throw Error('retirada de caja fuerte');
          const hora=game.sky.hour;game.player.health=60;await game.interiors.nap();if(game.player.health!==100||Math.abs(((game.sky.hour-hora+24)%24)-2)>.1)throw Error('siesta de Annie');
          const datos={entrada_ms:+ms.toFixed(1),kits:h.estancias.length,personalizadas:h.personalizadas,acciones:[...new Set(h.inter.map(i=>i.type))],decoracion:decor,banco:game.homeSafe.bank,siesta:true};
          game.interiors.leave(true);await game.interiors.enter(d,{silent:true});if(JSON.stringify(game.save.homeDecor)!==guardado||game.decor.items.length!==1)throw Error('decoración no persiste al volver');game.interiors.leave(true);return JSON.stringify(datos);
        })()""",timeout=300))
        if informe['annie']['entrada_ms']>1500:informe['errores'].append('entrada de Annie superior a 1500 ms')
        informe['comercios']=json.loads(T.ev("""(async()=>{const out=[];for(const tipo of ['bar','cafeteria','farmacia']){const s=game.shops.list.find(s=>s.type===tipo);if(!s)throw Error('sin muestra comercial '+tipo);const h=await game.interiors.enter({shop:s.type,seed:s.seed,name:s.title,x:s.x,z:s.z,fx:s.fx,fz:s.fz,shopRef:s},{silent:true,mode:'shop'});game.frame(1/30);game.render();const acciones=h.inter.filter(i=>['buy','counter'].includes(i.type)).length;if(!acciones)throw Error('comercio sin compra '+tipo);out.push({tipo,acciones});game.interiors.leave(true);}return JSON.stringify(out);})()""",timeout=300))
        if opts.colisiones:
            informe['colisiones']=json.loads(T.ev("""(async()=>{const H=await import('/tools/housetest.js');const out=[],vistos=new Set();for(const d of game.interiors.doors.filter(d=>d.seed>=1000&&!d.owner&&!d.venue&&!d.church)){const h=await game.interiors.enter(d,{silent:true,mode:'visit'});const plano=h.profile.layout;game.interiors.leave(true);if(vistos.has(plano))continue;vistos.add(plano);out.push(await H.house(d,{step:1.5,duracion:.35,maxRunsPorPlanta:16}));if(vistos.size===3)break;}return JSON.stringify(out);})()""",timeout=1200))
            informe['colisiones_annie']=json.loads(T.ev("(async()=>{const H=await import('/tools/housetest.js');return JSON.stringify(await H.house(game.interiors.doors.find(d=>d.owner==='annie'),{step:1.5,duracion:.35,maxRunsPorPlanta:16}));})()",timeout=600))
            a=informe['colisiones_annie']
            if a.get('error') or a.get('tunnels') or a.get('escapes') or a.get('runs')!=32:informe['errores'].append('colisiones de Annie')
            for r in informe['colisiones']:
                if r.get('error') or r.get('tunnels') or r.get('escapes') or not r['runs']:informe['errores'].append('colisión: '+r['name'])
        informe['consola']=json.loads(T.ev('JSON.stringify(window.__errs||[])'));informe['errores']+=informe['consola']
        T.ev('game.persist();window.__documentoAnterior=true;');T.call('Page.reload',{})
        for intento in range(100):
            try:
                if T.ev("!window.__documentoAnterior&&document.readyState==='complete'"):break
            except RuntimeError as e:
                if 'context' not in str(e).lower():raise
            time.sleep(.1)
        else:raise RuntimeError('no se confirma un documento nuevo tras recargar')
        T.ev(LISTO,timeout=240)
        informe['recarga_partida']=json.loads(T.ev("JSON.stringify({dinero:game.player.money,banco:game.homeSafe.bank,decoracion:game.save.homeDecor,evo:localStorage.getItem('guarena_evo_save'),fija:localStorage.getItem('guarena_save')})"))
        if informe['recarga_partida']!=informe['carga_partida']:informe['errores'].append('la partida no conserva sus valores al recargar')
    except Exception as e:informe['errores'].append(type(e).__name__+': '+str(e))
    finally:command('Target.disposeBrowserContext',{'browserContextId':contexto})
    dest=os.path.join(ROOT,'data','interiores','validacion','integracion_paquete.json' if opts.paquete else 'integracion_juego.json')
    json.dump(informe,open(dest,'w'),ensure_ascii=False,indent=1)
    print(json.dumps({k:v for k,v in informe.items() if k not in ['pueblo','colisiones']},ensure_ascii=False,indent=1))
    return not informe['errores']

if __name__=='__main__':sys.exit(0 if main() else 1)
