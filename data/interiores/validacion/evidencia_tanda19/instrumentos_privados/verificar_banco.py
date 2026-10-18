from pathlib import Path
import sys,json
r=Path.cwd();sys.path.insert(0,str(r/'tools/perf'));sys.path.insert(0,str(r/'tools/interiores'))
from beta import PrivateTab
from integracion import LISTO
js=r'''(async()=>{
 const g=game,{caja}=await import('/src/objetos.js'),rows=[];
 for(const seed of[2132,4204,1679,2162]){
  const door=g.interiors.doors.find(d=>d.seed===seed);if(!door)throw Error('puerta ausente');
  await g.interiors.enter(door,{mode:'visit',silent:true,seed});
  if(g.interiors.life){g.interiors.life.dispose();g.interiors.life=null;}
  const h=g.interior,e=h.estancias.find(e=>e.kit==='vivienda_trofeos'),p=e.colocados.find(p=>p.obj==='vb_banco_equipo_campo');
  if(seed===2162){if(p)throw Error('compacta ganó banco');rows.push({seed,banco:false});await g.interiors.exit();continue;}
  if(!p)throw Error('amplia sin banco');
  const sx=e.origen.x+p.x-.19*Math.cos(p.ry)+.04*Math.sin(p.ry),sz=e.origen.z+p.z+.19*Math.sin(p.ry)+.04*Math.cos(p.ry);
  const st=h.pieces.seat.filter(s=>Math.hypot(s.x-sx,s.z-sz)<1e-6);if(st.length!==1)throw Error('registro asiento');
  const b=caja(p.obj),ax=e.origen.x+p.x-.19*Math.cos(p.ry)+(b.z1+.4)*Math.sin(p.ry),az=e.origen.z+p.z+.19*Math.sin(p.ry)+(b.z1+.4)*Math.cos(p.ry),q={x:ax,z:az};
  const rm=h.rooms.find(r=>r.id===e.sala),col=h.levels?.[rm.lv]||h.collider,contact=col.resolveCircle(q,.34);
  if(![q.x,q.z,contact.depth].every(Number.isFinite)||Math.hypot(q.x-ax,q.z-az)>1e-6||contact.depth>1e-6)throw Error('acceso banco ocupado');
  g.player.pos.set(ax,e.origen.y,az);g.player.syncChar();
  const selected=g.seats.near(ax,az);if(!selected||selected.ref!==st[0])throw Error('selector no encuentra banco');
  g.seats.sit(selected);if(g.player.mode!=='sit'||Math.hypot(g.player.pos.x-sx,g.player.pos.z-sz)>1e-6)throw Error('no se sentó');
  g.render();g.seats.standUp();
  if(g.player.mode!=='foot'||g.seats.cur!==null||g.player.seat!==null)throw Error('no se levantó');
  const exit={x:g.player.pos.x,z:g.player.pos.z},clone={...exit},hit=col.resolveCircle(clone,.34);
  if(![clone.x,clone.z,hit.depth].every(Number.isFinite)||Math.hypot(exit.x-clone.x,exit.z-clone.z)>1e-6||hit.depth>1e-6)throw Error('salida de banco ocupada');
  rows.push({seed,banco:true,seleccion_real:true,sentado:true,levantado:true,acceso_libre:true,salida_libre:true,distancia_seleccion:Math.hypot(sx-ax,sz-az)});
  await g.interiors.exit();
 }
 if(window.__errs?.length)throw Error(JSON.stringify(window.__errs));
 return JSON.stringify({estado:'PASS',alcance:'Interacción real del selector, sentarse y levantarse, con collider .34; no certifica animación en todas las máquinas.',rows});
})()'''
with PrivateTab() as t:
 t.call('Page.addScriptToEvaluateOnNewDocument',{'source':"localStorage.setItem('guarena_hq_save',JSON.stringify({quality:'alta',qualityMode:'manual',dynRes:false,weatherLive:false,pick:'annie'}));"})
 t.call('Page.navigate',{'url':'http://localhost:8920/index.html'})
 t.ev(LISTO,timeout=240)
 result=json.loads(t.ev(js,timeout=240));(r/'.cache/calidad/tanda19/banco_jugador.json').write_text(json.dumps(result,ensure_ascii=False,indent=1)+'\n');print(json.dumps(result,ensure_ascii=False))
