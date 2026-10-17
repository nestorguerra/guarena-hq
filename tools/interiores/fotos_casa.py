# Photographs of the rooms of the neighbours' houses (epic I, vivienda por estancia), as the game builds them: the houses
# of the town's doors that have a room of that kind (src/houses.js types: salon, cocina, bano, dorm, dorm2, ninos,
# dormJoven, comedor, estudio, despacho, musica, trofeos, taller, costura, despensa, trastero), entered in the game's page
# (a headless muted Chrome, tools/perf/cdp.py, port 9333) and shot from two corners of the room, looking across it.
# Writes .snaps/casa_<tipo>_<seed>_<k>.jpg and a sheet data/interiores/fichas/casa_<tipo>.jpg.
#   python3 tools/interiores/fotos_casa.py <tipo> [n]          (n houses, 3 by default; town doors first, then others)
import argparse, json, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'perf'))
from cdp import Tab
from PIL import Image, ImageDraw
from integracion import LISTO

JS = r'''(async () => {
  const H = await import('/src/houses.js');
  const THREE=await import('three');
  const {caja}=await import('/src/objetos.js');
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
    const vistas=[];
    for (const [k, f] of [[0, 0.12], [1, 0.88]]) {
      let x = rm.x0 + (rm.x1 - rm.x0) * f, z = rm.z0 + (rm.z1 - rm.z0) * f;
      const est=h.estancias.find(e=>e.sala===rm.id),foco=est?.colocados.find(p=>p.obj==='vb_caballete');
      const hitos=(est?.colocados||[]).filter(p=>p.sop==null&&!['pared','techo'].includes(p.regla)&&caja(p.obj).h>.28).map(p=>{const b=caja(p.obj),lx=(b.x0+b.x1)/2,lz=(b.z0+b.z1)/2;return {x:est.origen.x+p.x+lx*Math.cos(p.ry)+lz*Math.sin(p.ry),z:est.origen.z+p.z-lx*Math.sin(p.ry)+lz*Math.cos(p.ry),y:y+Math.min(b.h*.65,1.25),w:b.w,peso:Math.min(2,b.w*b.h)+(['va_banco','va_lavabo'].includes(p.obj)?1.5:0)};});
      const suma=hitos.reduce((a,p)=>a+p.peso,0)||1;
      const cx = foco?est.origen.x+foco.x:(rm.x0+rm.x1)/2, cz = foco?est.origen.z+foco.z:(rm.z0+rm.z1)/2,col=h.levels?.[rm.lv]||h.collider;
      h.group.updateMatrixWorld(true);let mejor=-Infinity;
      const hojas=h.doors.flatMap(d=>{const m=[];d.pivot.traverse(o=>{if(o.isMesh)m.push(o);});return m;});
      for(const [fx,fz] of [[f,f],[1-f,f],[f,1-f],[f,.5],[.5,f],...[.2,.3,.4,.5,.6,.7,.8].flatMap(fx=>[.2,.3,.4,.5,.6,.7,.8].map(fz=>[fx,fz]))]){
        const q={x:rm.x0+(rm.x1-rm.x0)*fx,z:rm.z0+(rm.z1-rm.z0)*fz},antes={...q};col.resolveCircle(q,.34);
        if(Math.hypot(q.x-antes.x,q.z-antes.z)>.05)continue;
        if(!foco&&Math.hypot(q.x-cx,q.z-cz)<Math.min(1.15,Math.min(rm.x1-rm.x0,rm.z1-rm.z0)*.4))continue;
        if(!foco&&vistas.length&&Math.hypot(q.x-vistas[0].x,q.z-vistas[0].z)<.5)continue;
        const pos=new THREE.Vector3(q.x,y+1.6,q.z),dest=new THREE.Vector3(cx,y+1,cz),dir=dest.clone().sub(pos),dist=dir.length();
        const ray=new THREE.Raycaster(pos,dir.normalize(),0,dist),tapa=ray.intersectObjects(hojas,false).length;
        if(foco&&(Math.sin(foco.ry)*(q.x-cx)+Math.cos(foco.ry)*(q.z-cz)<.7))continue;
        let lectura=0;
        const eje=new THREE.Vector2(cx-q.x,cz-q.z).normalize();
        for(const p of hitos){const dx=p.x-q.x,dz=p.z-q.z,dd=Math.hypot(dx,dz);if(dd<.5||(dx*eje.x+dz*eje.y)/dd<Math.cos(38*Math.PI/180))continue;
          const v=new THREE.Vector3(p.x,y+1,p.z).sub(pos),d0=v.length(),rr=new THREE.Raycaster(pos,v.normalize(),0,d0-.08);
          if(!rr.intersectObjects(hojas,false).length)lectura+=p.peso*Math.min(1.3,p.w/dd*2.5);
        }
        const separacion=vistas.length?Math.min(2,Math.hypot(q.x-vistas[0].x,q.z-vistas[0].z)):0;
        const similitud=vistas.length?Math.max(0,((q.x-cx)*(vistas[0].x-cx)+(q.z-cz)*(vistas[0].z-cz))/Math.max(.001,Math.hypot(q.x-cx,q.z-cz)*Math.hypot(vistas[0].x-cx,vistas[0].z-cz))):0;
        const nota=foco?(k===0?-Math.abs(dist-1.6):dist)-(tapa?10:0):lectura*3+separacion-similitud*5-(tapa?4:0)-Math.abs(dist-2)*.15;
        if(nota>mejor){mejor=nota;x=q.x;z=q.z;}
      }
      if(!Number.isFinite(mejor))throw Error('sin cámara libre: '+tipo+'/'+s);
      for (let i = 0; i < 3; i++) g.frame(1 / 30);
      cam.fov=foco?60:tipo==='bano'?75:68;cam.updateProjectionMatrix();cam.position.set(x, y + 1.6, z); cam.lookAt(cx, y + 1.05, cz); cam.updateMatrixWorld(true);
      vistas.push({x,y:y+1.6,z,objetivo:[cx,y+1.05,cz],fov:cam.fov});
      g.render();
      await fetch('/__snap?name=casa_' + tipo + '_' + s + '_' + k, { method: 'POST', body: r.domElement.toDataURL('image/jpeg', 0.86) });
    }
    out.push({ seed: s, kit:H.kitDeEstancia(rm.type,prof.id),perfil: prof.id, estilo: prof.style, plano: prof.layout, sala: [+(rm.x1 - rm.x0).toFixed(1), +(rm.z1 - rm.z0).toFixed(1)], planta: rm.lv, vistas });
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
    T = Tab(9333, 'http://localhost:8920/index.html?estilo='+opts.estilo, w=1280, h=720, dpr=1)
    try:
        T.ev(LISTO,timeout=240)
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
    finally:
        T.close()

if __name__ == '__main__':
    main()
