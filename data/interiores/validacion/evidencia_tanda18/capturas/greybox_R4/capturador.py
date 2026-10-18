# Photographs of the rooms of the neighbours' houses (epic I, vivienda por estancia), as the game builds them: the houses
# of the town's doors that have a room of that kind (src/houses.js types: salon, cocina, bano, dorm, dorm2, ninos,
# dormJoven, comedor, estudio, despacho, musica, trofeos, taller, costura, despensa, trastero), entered in the game's page
# (a headless muted Chrome, tools/perf/cdp.py, port 9333) and shot from two corners of the room, looking across it.
# Writes .snaps/casa_<tipo>_<seed>_<k>.jpg and a sheet data/interiores/fichas/casa_<tipo>.jpg.
#   python3 tools/interiores/fotos_casa.py <tipo> [n]          (n houses, 3 by default; town doors first, then others)
import argparse, json, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'perf'))
from beta import PrivateTab
from PIL import Image, ImageDraw
from integracion import LISTO

JS = r'''(async () => {
  const H = await import('/src/houses.js');
  const THREE=await import('three');
  const {caja}=await import('/src/objetos.js');
  const {OBJETOS}=await import('/src/interiores_datos.js');
  // Physical clearance only: never resolve the actual candidate/camera in place.
  function cameraClearance(h,est,col,position){
    if(!est||!col?.resolveCircle)throw Error('faltan estancia o colisionador de planta');
    const radius=.34,tolerance=1e-6;
    const bounds={x0:est.origen.x-est.W/2+radius,x1:est.origen.x+est.W/2-radius,
      z0:est.origen.z+radius,z1:est.origen.z+est.D-radius};
    if(![position.x,position.z,est.origen.y,...Object.values(bounds)].every(Number.isFinite))throw Error('pose o límites de estancia no finitos');
    const inBounds=position.x>=bounds.x0-tolerance&&position.x<=bounds.x1+tolerance&&position.z>=bounds.z0-tolerance&&position.z<=bounds.z1+tolerance;
    const q={x:position.x,z:position.z},contact=col.resolveCircle(q,radius);
    const delta=Math.hypot(q.x-position.x,q.z-position.z),insideFloorFurniture=[],circleCentres=[];
    // Match the floor-footprint exclusions in houses.js; borders alone miss deep interiors.
    for(const room of h.estancias){
      if(Math.abs(room.origen.y-est.origen.y)>tolerance)continue;
      for(const p of room.colocados){
        const b=caja(p.obj);
        if(p.sop!=null||p.regla==='pared'||p.regla==='techo'||OBJETOS[p.obj].clase==='PICKUP'||b.h<.3)continue;
        const dx=position.x-room.origen.x-p.x,dz=position.z-room.origen.z-p.z;
        const cs=Math.cos(p.ry),sn=Math.sin(p.ry),x=dx*cs-dz*sn,z=dx*sn+dz*cs;
        if(x>=b.x0-tolerance&&x<=b.x1+tolerance&&z>=b.z0-tolerance&&z<=b.z1+tolerance)
          insideFloorFurniture.push({room:room.sala,obj:p.obj,index:p.i,local:[x,z],bounds:[b.x0,b.z0,b.x1,b.z1]});
      }
    }
    // resolveCircle ignores exact circle centres (d2<=1e-8), including live props.
    for(let i=0;i<col.nCirc;i++)if(col.circleAlive[i]){
      const at=i*5,dx=position.x-col.circles[at],dz=position.z-col.circles[at+1];
      if(dx*dx+dz*dz<=1e-8)circleCentres.push(i);
    }
    return {free:inBounds&&Number.isFinite(delta)&&Number.isFinite(contact.depth)&&delta<=tolerance&&contact.depth<=tolerance&&!insideFloorFurniture.length&&!circleCentres.length,
      position:{x:position.x,z:position.z},radius,tolerance,bounds,inBounds,delta,contact:!!contact.hit,depth:contact.depth,
      insideFloorFurniture,circleCentres,testedOnlyOnClone:true,cameraMoved:false};
  }
  function requireCameraClearance(h,est,col,position,stage){
    const result=cameraClearance(h,est,col,position);
    if(!result.free)throw Error('cámara ocupada '+stage+': '+JSON.stringify(result));
    return result;
  }
  // End physical clearance helpers.
  const g = window.game, tipo = %s, n = %d, kid = %s, perfil = %s, out = [];
  g.sky.hour = 12;
  const r = g.renderer; r.setSize(1280, 720, false); if (g.composer) g.composer.setSize(1280, 720);
  const cam = g.camera; cam.aspect = 16 / 9; cam.fov = 75; cam.updateProjectionMatrix();
  // the town's doors first, then any house: those with a room of that kind
  const seeds = [...g.interiors.doors.filter((d) => d.seed >= 1000).map((d) => d.seed)];
  for (let s = 1000; s < 9000 && seeds.length < 400; s += 37) seeds.push(s);
  for (const s of seeds) {
    if (out.length >= n) break;
    const prof = H.houseProfile(s);
    if(perfil && prof.id!==perfil) continue;
    const h0 = H.buildVecino(s, { x: -9700, z: -9700 });
    const has = h0.rooms.some((q) => q.type === tipo && (!kid || H.kitDeEstancia(q.type,prof.id)===kid));
    h0.group.traverse((o) => { if (o.isMesh) o.geometry.dispose(); });
    if (!has) continue;
    const door = g.interiors.doors.find((d) => d.seed === s) || { name: 'Casa', seed: s, x: g.player.pos.x, z: g.player.pos.z };
    await g.interiors.enter(door, { mode: 'visit', silent: true, seed: s });
    await new Promise((res) => setTimeout(res, 500));
    if(g.interiors.life){g.interiors.life.dispose();g.interiors.life=null;}
    const h = g.interior, rm = h.rooms.find((q) => q.type === tipo), y = rm.lv ? 3.1 : 0;
    const body = g.player.char && g.player.char.object; if (body) body.visible = false;
    const grey=new THREE.MeshStandardMaterial({color:0x9a9a92,roughness:.9});
    h.group.traverse(o=>{if(o.isMesh&&!o.material?.transparent)o.material=grey;});
    const vistas=[];
    for (const [k, f] of [[0, 0.12], [1, 0.88]]) {
      let x = rm.x0 + (rm.x1 - rm.x0) * f, z = rm.z0 + (rm.z1 - rm.z0) * f;
      const est=h.estancias.find(e=>e.sala===rm.id),foco=(k===0&&tipo==='trastero'?est?.colocados.find(p=>['va_bicicleta_guardada','va_bicicleta_carga','va_escalera_guardada'].includes(p.obj)):null)||est?.colocados.find(p=>p.obj==='vb_caballete'||(k===0&&(p.obj.startsWith('va_banco')||p.obj.startsWith('va_lavabo')||p.obj.startsWith('vb_mesa_despacho')||p.obj.startsWith('va_estante_trastero')||p.obj.startsWith('va_cocina')||p.obj.startsWith('va_costura'))));
      const hitos=(est?.colocados||[]).filter(p=>p.sop==null&&!['pared','techo'].includes(p.regla)&&caja(p.obj).h>.28).map(p=>{const b=caja(p.obj),lx=(b.x0+b.x1)/2,lz=(b.z0+b.z1)/2;return {x:est.origen.x+p.x+lx*Math.cos(p.ry)+lz*Math.sin(p.ry),z:est.origen.z+p.z-lx*Math.sin(p.ry)+lz*Math.cos(p.ry),y:y+Math.min(b.h*.65,1.25),w:b.w,peso:Math.min(2,b.w*b.h)+(['va_banco','va_lavabo'].includes(p.obj)?1.5:0)};});
      const suma=hitos.reduce((a,p)=>a+p.peso,0)||1;
      // La segunda vista complementa el detalle: preparación y nevera en cocina,
      // sanitario completo en baño. Se conservan altura humana y campo de visión.
      const sanitario=k===1&&tipo==='bano'?est?.colocados.find(p=>p.obj==='va_inodoro'):null;
      const preparacion=k===1&&tipo==='cocina'?est?.colocados.find(p=>['va_encimera','va_encimera_amplia'].includes(p.obj.replace(/_(rustico|liso|vajillero)$/,''))):null;
      const mesaComedor=k===0&&tipo==='comedor'?est?.colocados.find(p=>['va_mesa_comedor','va_mesa_familiar'].includes(p.obj)):null;
      if(tipo==='comedor'&&k===0&&!mesaComedor)throw Error('comedor sin mesa para documentar: '+s);
      const puestosComedor=mesaComedor?[mesaComedor,...est.colocados.filter(p=>p.de===est.colocados.indexOf(mesaComedor))]:[];
      const objetivos=puestosComedor.length?puestosComedor:preparacion?[preparacion,est.colocados.find(p=>p.obj==='va_nevera')].filter(Boolean):sanitario?[sanitario]:[];
      const centros=objetivos.map(p=>{const b=caja(p.obj),lx=(b.x0+b.x1)/2,lz=(b.z0+b.z1)/2;return {p,x:est.origen.x+p.x+lx*Math.cos(p.ry)+lz*Math.sin(p.ry),z:est.origen.z+p.z-lx*Math.sin(p.ry)+lz*Math.cos(p.ry)};});
      const cx = foco?est.origen.x+foco.x:centros.length?centros.reduce((a,p)=>a+p.x,0)/centros.length:(rm.x0+rm.x1)/2, cz = foco?est.origen.z+foco.z:centros.length?centros.reduce((a,p)=>a+p.z,0)/centros.length:(rm.z0+rm.z1)/2,col=h.levels?.[rm.lv]||h.collider;
      const centroAlturaComedor=puestosComedor.length?(Math.min(...puestosComedor.map(p=>(p.y||0)+caja(p.obj).y0))+Math.max(...puestosComedor.map(p=>(p.y||0)+caja(p.obj).y1)))/2:.75;
      const alturaObjetivo=k===0?(tipo==='trastero'?.85:tipo==='comedor'?centroAlturaComedor:1.05):tipo==='bano'?.8:tipo==='comedor'?1.05:1.4;
      const fov=foco?(tipo==='trastero'?68:60):['bano','comedor'].includes(tipo)?75:68;
      const pruebaCam=objetivos.length||tipo==='comedor'?new THREE.PerspectiveCamera(fov,16/9,.05,1000):null;
      const esquinas=objetivos.flatMap(p=>{const b=caja(p.obj),out=[];for(const lx of [b.x0,b.x1])for(const ly of [b.y0,b.y1])for(const lz of [b.z0,b.z1])out.push(new THREE.Vector3(est.origen.x+p.x+lx*Math.cos(p.ry)+lz*Math.sin(p.ry),y+(p.y||0)+ly,est.origen.z+p.z-lx*Math.sin(p.ry)+lz*Math.cos(p.ry)));return out;});
      h.group.updateMatrixWorld(true);let mejor=-Infinity,puertaElegida=null,recortesElegidos=null,clearanceElegido=null;
      const opacos=[];h.group.traverse(o=>{if(o.isMesh&&o.visible&&!o.material?.transparent)opacos.push(o);});
      const hojas=h.doors.flatMap(d=>{const m=[];d.pivot.traverse(o=>{if(o.isMesh)m.push(o);});return m;});
      const rejilla=tipo==='comedor'?[.08,.1,.12,.18,.25,.35,.5,.65,.75,.82,.88,.9,.92]:[.2,.3,.4,.5,.6,.7,.8];
      for(const [fx,fz] of [[f,f],[1-f,f],[f,1-f],[f,.5],[.5,f],...rejilla.flatMap(fx=>rejilla.map(fz=>[fx,fz]))]){
        const q={x:rm.x0+(rm.x1-rm.x0)*fx,z:rm.z0+(rm.z1-rm.z0)*fz};
        const clearance=cameraClearance(h,est,col,q);if(!clearance.free)continue;
        if(!foco&&Math.hypot(q.x-cx,q.z-cz)<Math.min(1.15,Math.min(rm.x1-rm.x0,rm.z1-rm.z0)*.4))continue;
        if(!foco&&vistas.length&&Math.hypot(q.x-vistas[0].x,q.z-vistas[0].z)<.5)continue;
        if(preparacion&&centros.some(p=>(Math.sin(p.p.ry)*(q.x-p.x)+Math.cos(p.p.ry)*(q.z-p.z))/Math.max(.001,Math.hypot(q.x-p.x,q.z-p.z))<Math.cos(55*Math.PI/180)))continue;
        const pos=new THREE.Vector3(q.x,y+1.6,q.z),dest=new THREE.Vector3(cx,y+(pruebaCam?alturaObjetivo:1),cz),dir=dest.clone().sub(pos),dist=dir.length();
        let recortes=0,puertaPrimerPlano=0;
        if(pruebaCam){
          pruebaCam.position.copy(pos);pruebaCam.lookAt(cx,y+alturaObjetivo,cz);pruebaCam.updateMatrixWorld(true);
          // En comedor, una hoja próxima no puede tapar la evidencia del conjunto.
          if(tipo==='comedor'){
            const rr=new THREE.Raycaster();rr.near=.05;rr.far=1.25;
            for(let iy=0;iy<5;iy++)for(let ix=0;ix<7;ix++){
              rr.setFromCamera(new THREE.Vector2(-.9+ix*.3,-.8+iy*.4),pruebaCam);
              if(rr.intersectObjects(hojas,false).length)puertaPrimerPlano++;
            }
            puertaPrimerPlano/=35;
            if(puertaPrimerPlano>.12)continue;
          }
          for(const v of esquinas){const p=v.clone().project(pruebaCam);if(p.z< -1||p.z>1||Math.abs(p.x)>.94||Math.abs(p.y)>.94)recortes++;}
        }
        const ray=new THREE.Raycaster(pos,dir.normalize(),0,dist);let tapa=ray.intersectObjects(hojas,false).length;
        if(foco){const b=caja(foco.obj);ray.far=Math.max(0,dist-Math.max(b.w,b.d)*.55-.05);tapa+=ray.intersectObjects(opacos,false).length;}
        if(foco&&(Math.sin(foco.ry)*(q.x-cx)+Math.cos(foco.ry)*(q.z-cz)<(tipo==='costura'?.15:.7)))continue;
        let lectura=0;
        const eje=new THREE.Vector2(cx-q.x,cz-q.z).normalize();
        for(const p of hitos){const dx=p.x-q.x,dz=p.z-q.z,dd=Math.hypot(dx,dz);if(dd<.5||(dx*eje.x+dz*eje.y)/dd<Math.cos(38*Math.PI/180))continue;
          const v=new THREE.Vector3(p.x,y+1,p.z).sub(pos),d0=v.length(),rr=new THREE.Raycaster(pos,v.normalize(),0,d0-.08);
          if(!rr.intersectObjects(hojas,false).length)lectura+=p.peso*Math.min(1.3,p.w/dd*2.5);
        }
        const separacion=vistas.length?Math.min(2,Math.hypot(q.x-vistas[0].x,q.z-vistas[0].z)):0;
        const similitud=vistas.length?Math.max(0,((q.x-cx)*(vistas[0].x-cx)+(q.z-cz)*(vistas[0].z-cz))/Math.max(.001,Math.hypot(q.x-cx,q.z-cz)*Math.hypot(vistas[0].x-cx,vistas[0].z-cz))):0;
        const nota=(foco?(k===0?-Math.abs(dist-(tipo==='trastero'?2.1:1.6)):dist)-(tapa?10:0):lectura*3+separacion-similitud*5-(tapa?4:0)-Math.abs(dist-2)*.15)-recortes*100-(sanitario?Math.max(0,1.1-Math.hypot(q.x-cx,q.z-cz))*8:0);
        if(nota>mejor){mejor=nota;x=q.x;z=q.z;puertaElegida=puertaPrimerPlano;recortesElegidos=recortes;clearanceElegido=clearance;}
      }
      if(!Number.isFinite(mejor))throw Error('sin cámara libre: '+tipo+'/'+s);
      for (let i = 0; i < 3; i++) g.frame(1 / 30);
      cam.fov=fov;cam.updateProjectionMatrix();cam.position.set(x, y + 1.6, z); cam.lookAt(cx, y + alturaObjetivo, cz); cam.updateMatrixWorld(true);
      if(tipo==='comedor'){
        // La pose final puede cambiar tras frame: comprobar lo que se va a fotografiar.
        h.group.updateMatrixWorld(true);
        const rr=new THREE.Raycaster();rr.near=.05;rr.far=1.25;let tapaFinal=0;
        for(let iy=0;iy<5;iy++)for(let ix=0;ix<7;ix++){
          rr.setFromCamera(new THREE.Vector2(-.9+ix*.3,-.8+iy*.4),cam);
          if(rr.intersectObjects(hojas,false).length)tapaFinal++;
        }
        puertaElegida=tapaFinal/35;
        recortesElegidos=esquinas.length?esquinas.filter(v=>{const p=v.clone().project(cam);return p.z< -1||p.z>1||Math.abs(p.x)>.94||Math.abs(p.y)>.94;}).length:null;
        if(puertaElegida>.12||recortesElegidos>0)throw Error('cobertura final incompleta: '+tipo+'/'+s+'/'+k+' puerta='+puertaElegida+' recortes='+recortesElegidos+' cam='+JSON.stringify({x,y:y+1.6,z,objetivo:[cx,y+alturaObjetivo,cz],fuera:esquinas.map((v,i)=>({i,p:v.clone().project(cam)})).filter(q=>Math.abs(q.p.x)>.94||Math.abs(q.p.y)>.94)}));
      }
      const clearanceAntes=requireCameraClearance(h,est,col,cam.position,tipo+'/'+s+'/'+k+' antes de render');
      const poseAntes=JSON.stringify({position:cam.position.toArray(),quaternion:cam.quaternion.toArray(),fov:cam.fov});
      vistas.push({clearance:{candidate:clearanceElegido,beforeRender:clearanceAntes},encuadre:k===0?'uso':'conjunto',x,y:y+1.6,z,objetivo:[cx,y+alturaObjetivo,cz],fov:cam.fov,...(tipo==='comedor'?{cobertura:{hoja_cercana_fraccion:puertaElegida,muestras:35,distancia_max:1.25,limite:.12,medido:'pose_final_antes_render',esquinas_evaluadas:esquinas.length,esquinas_recortadas:recortesElegidos}}:{}),...(objetivos.length?{objetos_objetivo:objetivos.map(p=>p.obj)}:{})});
      if(window.__errs?.length)throw Error('errores antes de captura: '+JSON.stringify(window.__errs));
      g.render();
      if(window.__errs?.length)throw Error('errores de render: '+JSON.stringify(window.__errs));
      if(r.info.programs?.some(p=>p.diagnostics?.runnable===false))throw Error('programa WebGL no ejecutable');
      vistas[vistas.length-1].clearance.afterRender=requireCameraClearance(h,est,col,cam.position,tipo+'/'+s+'/'+k+' después de render');
      if(JSON.stringify({position:cam.position.toArray(),quaternion:cam.quaternion.toArray(),fov:cam.fov})!==poseAntes)throw Error('render cambió la pose de cámara: '+tipo+'/'+s+'/'+k);
      const snapResponse=await fetch('/__snap?name=casa_' + tipo + '_' + s + '_' + k, { method: 'POST', body: r.domElement.toDataURL('image/jpeg', 0.86) });if(!snapResponse.ok)throw Error('captura HTTP '+snapResponse.status);
    }
    out.push({ seed: s, kit:H.kitDeEstancia(rm.type,prof.id),perfil: prof.id, estilo: prof.style, plano: prof.layout, sala: [+(rm.x1 - rm.x0).toFixed(1), +(rm.z1 - rm.z0).toFixed(1)], planta: rm.lv, quality:g.qKey, dpr:r.getPixelRatio(), vistas });
    await g.interiors.exit();
    await new Promise((res) => setTimeout(res, 300));
  }
  return JSON.stringify(out);
})()'''

def main():
    parser=argparse.ArgumentParser(description='Capturas reales de una o varias estancias, separadas por coma.')
    parser.add_argument('tipos');parser.add_argument('n',nargs='?',type=int,default=3)
    parser.add_argument('--kit');parser.add_argument('--perfil');parser.add_argument('--estilo',default='plastilina',choices=['plastilina','real'])
    opts=parser.parse_args();n=opts.n
    with PrivateTab() as T:
        T.call('Emulation.setDeviceMetricsOverride',dict(width=1280,height=720,deviceScaleFactor=1,mobile=False))
        T.call('Page.addScriptToEvaluateOnNewDocument',{'source':"localStorage.setItem('guarena_hq_save',JSON.stringify({quality:'alta',qualityMode:'manual',dynRes:false,weatherLive:false,pick:'annie'}));"})
        T.call('Page.navigate',{'url':'http://localhost:8929/index.html?estilo='+opts.estilo})
        T.ev(LISTO,timeout=240)
        if not T.ev("game.qKey==='alta'&&!game.autoQuality&&game.renderer.getPixelRatio()===1"):raise RuntimeError('La ficha requiere calidad alta fija y DPR1')
        for tipo in opts.tipos.split(','):
            res = json.loads(T.ev(JS % (json.dumps(tipo), n,json.dumps(opts.kit or ('vivienda_taller' if tipo=='taller' else None)),json.dumps(opts.perfil)), timeout=600))
            if not res:raise RuntimeError('ninguna casa para '+tipo+'/'+str(opts.kit))
            hoja = Image.new('RGB', (1280, 386 * len(res)))
            for j,c in enumerate(res):
                for k in range(2):hoja.paste(Image.open(os.path.join(ROOT,'.snaps',f"casa_{tipo}_{c['seed']}_{k}.jpg")).resize((640,360)),(k*640,j*386+26))
                ImageDraw.Draw(hoja).text((8,j*386+5),str({k:v for k,v in c.items() if k!='vistas'})+' / '+opts.estilo,fill='white')
            dest=os.path.join(ROOT,'data','interiores','fichas');os.makedirs(dest,exist_ok=True)
            etiqueta=opts.kit.removeprefix('vivienda_') if opts.kit else tipo
            nombre=f'casa_{etiqueta}'+('_realista' if opts.estilo=='real' else '')
            hoja.save(os.path.join(dest,nombre+'.jpg'),quality=85)
            json.dump(res,open(os.path.join(dest,nombre+'.json'),'w'),ensure_ascii=False,indent=1)
            print(len(res),'casas capturadas:',nombre,flush=True)

if __name__ == '__main__':
    main()
