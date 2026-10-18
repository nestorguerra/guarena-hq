"""Juego real, inventario, entrada y partida de prueba en un contexto privado del Chrome de ensayos."""
import argparse, json, os, re, sys, time, urllib.request
from pathlib import Path
ROOT=str(Path(__file__).resolve().parents[4])
OUTPUT=str(Path(__file__).resolve().parent / 'ejecuciones')
sys.path.insert(0,os.path.join(ROOT,'tools','perf'))
from cdp import Tab, WS, ERRS

LISTO="""(async()=>{const t=performance.now();let pulsado=false;while(performance.now()-t<180000){const g=window.game,l=document.getElementById('loading');if(g?.player&&(!l||l.hidden)){const intro=window.guarenaIntroTimes;if(intro&&!intro.flight){await new Promise(r=>setTimeout(r,100));continue;}if(window.guarenaIntro?.flying){for(let i=0;i<8;i++)window.guarenaIntro.step(.1);await new Promise(r=>setTimeout(r,10));continue;}if(g.state==='play'&&g.player.char&&!g.cam.cinematic)return true;if(!intro&&!pulsado){document.getElementById('bPlay')?.click();pulsado=true;}}await new Promise(r=>setTimeout(r,100));}throw Error('juego no preparado: '+JSON.stringify(window.__errs));})()"""


def main():
    parser=argparse.ArgumentParser(description='T20: comprueba únicamente el paquete publicado en Pages, sin modificar datos durables.')
    parser.add_argument('--sha',required=True,help='SHA Git completo del candidato aprobado; nunca se infiere de HEAD')
    parser.add_argument('--paquete',action='store_true',help='Compatibilidad con T10: esta versión siempre comprueba el paquete')
    parser.add_argument('--informe',default='integracion_publica.json',help='Nombre nuevo de informe dentro de revision_publicacion/ejecuciones')
    opts=parser.parse_args()
    if not re.fullmatch(r'[0-9a-f]{40}',opts.sha):parser.error('--sha debe ser un SHA completo de 40 caracteres hexadecimales en minúscula')
    if os.path.basename(opts.informe)!=opts.informe:parser.error('--informe debe ser sólo un nombre de archivo')
    os.makedirs(OUTPUT,exist_ok=True);dest=os.path.join(OUTPUT,opts.informe)
    if os.path.exists(dest):parser.error('El informe ya existe; use otro --informe para conservar la evidencia anterior')
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
    informe={'url':'https://nestorguerra.github.io/guarena-hq/?estilo=plastilina&v='+opts.sha,'revision_esperada':opts.sha,'alcance':'paquete Pages: ocho vecinos, cuatro casas reales de trofeos y tres bancos, cinco vecinos dormitorio y joven1594, Annie, tres comercios y persistencia','errores':[]}
    try:
        with urllib.request.urlopen(urllib.request.Request(informe['url'],method='HEAD'),timeout=30) as response:
            informe['http_status']=response.status
            if response.status!=200:raise RuntimeError('HTTP público no es 200')
        tid=command('Target.createTarget',{'url':'about:blank','browserContextId':contexto})['targetId']
        tabs=json.load(urllib.request.urlopen('http://127.0.0.1:9333/json/list'));endpoint=next(t['webSocketDebuggerUrl'] for t in tabs if t['id']==tid)
        T=Tab.__new__(Tab);T.id=tid;T.port=9333;T.ws=WS(endpoint);T.ws.s.settimeout(1800);T.mid=0
        T.call('Page.enable');T.call('Emulation.setFocusEmulationEnabled',{'enabled':True});T.call('Emulation.setDeviceMetricsOverride',dict(width=960,height=540,deviceScaleFactor=1,mobile=False))
        T.call('Page.addScriptToEvaluateOnNewDocument',{'source':ERRS})
        # Datos ficticios solo en el contexto privado; comprueba que HQ no escribe las otras dos partidas.
        fixture="localStorage.setItem('guarena_hq_save',JSON.stringify({money:321,bag:[],pick:'annie',modePref:'normal',quality:'alta',qualityMode:'manual',dynRes:false,weatherLive:false,bank:700,homeDecor:[{id:'cuadro',x:0,y:4.7,z:4.9,ry:Math.PI,seed:23}]}));localStorage.setItem('guarena_evo_save',JSON.stringify({testigo:'evo'}));localStorage.setItem('guarena_save',JSON.stringify({testigo:'fija'}));"
        T.call('Page.addScriptToEvaluateOnNewDocument',{'source':"if(location.origin==='https://nestorguerra.github.io'&&!sessionStorage.getItem('fixture')){"+fixture+"sessionStorage.setItem('fixture','1');}"})
        T.call('Page.navigate',{'url':informe['url']});T.ev(LISTO,timeout=240)
        informe['revision_servida']=T.ev("document.querySelector('meta[name=guarena-revision]')?.content")
        if informe['revision_servida']!=opts.sha:raise RuntimeError('La página no sirve el commit esperado')
        informe['carga_partida']=json.loads(T.ev("JSON.stringify({dinero:game.player.money,banco:game.homeSafe.bank,decoracion:game.save.homeDecor,evo:localStorage.getItem('guarena_evo_save'),fija:localStorage.getItem('guarena_save')})"))
        if informe['carga_partida']['dinero']!=321:informe['errores'].append('no carga el dinero de la partida HQ')
        informe['entradas']=json.loads(T.ev("""(async()=>{const out=[];let elegidas=0;for(const d of game.interiors.doors.filter(d=>d.seed>=1000&&!d.owner&&!d.venue&&!d.church)){const t=performance.now();const h=await game.interiors.enter(d,{mode:'visit',silent:true});const ms=performance.now()-t;const tv=h.pieces.tv[0];if(tv){const m=tv.mesh.material;m.emissiveIntensity=.85;if(m.emissiveIntensity!==.85)throw Error('pantalla no responde');m.emissiveIntensity=0;}const L=game.interiors.life;if(L&&L.people[0]&&h.pieces.bed[0]){L.lieOnBed(L.people[0],h.pieces.bed[0]);if(L.people[0].state!=='sleep')throw Error('no duerme');}const estudio=h.estancias.find(e=>e.kit==='vivienda_estudio');let programaEstudio=null;if(estudio&&['artista','estudiante','musico'].includes(h.profile.id)){for(const id of['vb_puesto_estudio_amplio','vb_guardado_estudio','vb_biblioteca_estudio'])if(!estudio.colocados.some(p=>p.obj===id))throw Error('estudio público incompleto '+d.seed+'/'+id);if(estudio.colocados.filter(p=>p.obj==='vb_ordenador').length!==1)throw Error('pantalla de estudio pública duplicada/ausente');game.frame(1/30);game.render();programaEstudio={perfil:h.profile.id,objetos:estudio.colocados.map(p=>p.obj)};}const salon=h.estancias.find(e=>e.kit==='vivienda_salon');let programaSalon=null;if([3244,1594].includes(d.seed)){if(!salon?.composicionLectura)throw Error('composición de lectura pública ausente '+d.seed);const rug=salon.colocados.find(p=>p.obj==='alfombra_salon');if(!rug||Math.abs(rug.y-.008)>1e-7)throw Error('alfombra pública no elevada '+d.seed);const estar=salon.composicionEstar;if(!estar?.movidos?.length)throw Error('programa estar público ausente');const sofa=salon.colocados[estar.sofa],mesa=salon.colocados[estar.mesa];if(!sofa||!mesa||salon.colocados[estar.alfombra]!==rug||Math.cos(mesa.ry-sofa.ry)<.999999||Math.cos(rug.ry-mesa.ry)<.999999||Math.hypot(mesa.x-rug.x,mesa.z-rug.z)>1e-6)throw Error('estar público desarticulado');const gapReal=(mesa.v.cx-sofa.v.cx)*Math.sin(sofa.ry)+(mesa.v.cz-sofa.v.cz)*Math.cos(sofa.ry)-sofa.v.hd-mesa.v.hd;if(Math.abs(gapReal-estar.gap)>1e-5)throw Error('separación pública no coincide');const puff=salon.colocados[salon.composicionLectura.asiento];if(puff?.obj!=='puff')throw Error('fixture asiento público cambió');const sx=salon.origen.x+puff.x,sz=salon.origen.z+puff.z,readingSeats=h.pieces.seat.filter(st=>Math.hypot(st.x-sx,st.z-sz)<1e-6&&Math.abs(st.y-salon.origen.y)<1e-6&&Math.abs(st.h-puff.ry)<1e-6);if(readingSeats.length!==1)throw Error('asiento de lectura público ausente/duplicado');programaSalon={perfil:h.profile.id,composicion:salon.composicionLectura,composicionEstar:estar,gap_real:gapReal,alfombra_y:rug.y,asiento_lectura:{x:sx,y:salon.origen.y,z:sz,h:puff.ry,registros:readingSeats.length},alcance_asiento:'registro pieces.seat consumido por terrace; no ejecuta sentarse'};game.frame(1/30);game.render();if(game.renderer.info.programs?.some(p=>p.diagnostics?.runnable===false))throw Error('shader público fallido');}out.push({seed:d.seed,plano:h.profile.layout,plantas:h.levels?.length||1,entrada_ms:+ms.toFixed(1),habitaciones:h.estancias.length,programaEstudio,programaSalon});game.interiors.leave(true);if(++elegidas>=8)break;}return JSON.stringify(out);})()""",timeout=600))
        if len(informe['entradas'])!=8:informe['errores'].append('no se completaron las ocho entradas de vecinos')
        if sorted(r['seed'] for r in informe['entradas'] if r.get('programaEstudio'))!=[1594,3244]:informe['errores'].append('no se confirmaron los dos estudios reales de la tanda')
        if sorted(r['seed'] for r in informe['entradas'] if r.get('programaSalon'))!=[1594,3244]:informe['errores'].append('no se confirmaron ambos salones públicos')
        if any(r['entrada_ms']>1500 for r in informe['entradas']):informe['errores'].append('entrada real superior a 1500 ms')
        # Probe adicional literal sin imports de /src: también sirve al paquete Pages.
        informe['trofeos']=json.loads(T.ev(Path(__file__).with_name('trofeos_publico.js').read_text(),timeout=300))
        if informe['trofeos']['estado']!='PASS':informe['errores'].append('trofeos/bancos públicos: FAIL; ver rows')
        informe['dormitorios']=json.loads(T.ev(Path(__file__).with_name('dormitorios_publico.js').read_text(),timeout=300))
        if informe['dormitorios']['estado']!='PASS':informe['errores'].append('dormitorios públicos: FAIL; ver rows')
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
        informe['consola']=json.loads(T.ev('JSON.stringify(window.__errs||[])'));informe['errores']+=informe['consola']
        T.ev('game.persist();window.__documentoAnterior=true;');T.call('Page.reload',{})
        for intento in range(1000):
            try:
                if T.ev("!window.__documentoAnterior&&!!window.game"):break
            except RuntimeError as e:
                if 'context' not in str(e).lower():raise
            time.sleep(.1)
        else:raise RuntimeError('no se confirma un documento nuevo tras recargar')
        T.ev(LISTO,timeout=240)
        informe['revision_tras_recarga']=T.ev("document.querySelector('meta[name=guarena-revision]')?.content")
        if informe['revision_tras_recarga']!=opts.sha:raise RuntimeError('La recarga no sirve el commit esperado')
        informe['consola_tras_recarga']=json.loads(T.ev('JSON.stringify(window.__errs||[])'));informe['errores']+=informe['consola_tras_recarga']
        informe['recarga_partida']=json.loads(T.ev("JSON.stringify({dinero:game.player.money,banco:game.homeSafe.bank,decoracion:game.save.homeDecor,evo:localStorage.getItem('guarena_evo_save'),fija:localStorage.getItem('guarena_save')})"))
        if informe['recarga_partida']!=informe['carga_partida']:informe['errores'].append('la partida no conserva sus valores al recargar')
    except Exception as e:
        informe['errores'].append(type(e).__name__+': '+str(e))
        try:informe['trofeos_parcial']=json.loads(T.ev('JSON.stringify(window.__t19Trofeos||[])'))
        except Exception as parcial:informe['error_lectura_parcial']=str(parcial)
        try:informe['dormitorios_parcial']=json.loads(T.ev('JSON.stringify(window.__t20Dormitorios||[])'))
        except Exception as parcial:informe['error_dormitorios_parcial']=str(parcial)
    finally:
        try:command('Target.disposeBrowserContext',{'browserContextId':contexto})
        except Exception as e:informe['errores'].append('dispose: '+str(e))
    json.dump(informe,open(dest,'w'),ensure_ascii=False,indent=1)
    print(json.dumps({k:v for k,v in informe.items() if k not in []},ensure_ascii=False,indent=1))
    return not informe['errores']

if __name__=='__main__':sys.exit(0 if main() else 1)
