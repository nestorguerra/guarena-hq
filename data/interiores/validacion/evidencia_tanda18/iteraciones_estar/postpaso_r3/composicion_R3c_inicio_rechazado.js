// Postpaso optativo: sólo tras terminar la receta. No llama filtros ni azar.
import { OBJETOS } from './interiores_datos.js';
import { caja } from './objetos.js';
import { rot, partes, penetra, superficie, mapaPaso, espacioFrontal } from './interiores_geo.js';

export function componerLectura({P, K, ctx, planta, H, libres, inicio, aceptar,diagnostico=()=>{}}) {
  const cfg=K.composicion_lectura;
  if(!cfg||!ctx?.funciones||!cfg.perfiles.includes(ctx.perfil)||planta.W*planta.D<cfg.area_min)return null;
  const floor=p=>p.sop==null&&p.de==null&&!['pared','techo'].includes(p.regla);
  const roots=[cfg.biblioteca,cfg.asiento,cfg.mesita,cfg.lampara].map(ids=>P.findIndex(p=>floor(p)&&ids.includes(p.obj)));
  if(roots.some(i=>i<0)||new Set(roots).size!==4)return null;
  const zone=P[roots[0]].zona,Z=planta.zonas[zone];
  if(roots.some(i=>P[i].zona!==zone))return null;
  const owner=new Map(roots.map(i=>[i,i])),visiting=new Set();
  const buscar=i=>{
    if(owner.has(i))return owner.get(i);
    if(visiting.has(i))throw new Error('ciclo de soporte');
    visiting.add(i);const p=P[i],links=[p.sop,p.de].filter(j=>j!=null);
    if(links.some(j=>!Number.isInteger(j)||!P[j]))throw new Error('referencia de soporte inválida');
    const found=[...new Set(links.map(buscar).filter(v=>v!=null))];visiting.delete(i);
    if(found.length>1||found.length&&P[i].zona!==zone)throw new Error('dependientes incompatibles');
    const o=found[0]??null;owner.set(i,o);return o;
  };
  try{P.forEach((p,i)=>buscar(i));}catch{return null;}
  const moved=[...owner].filter(([,r])=>r!=null).map(([i])=>i).sort((a,b)=>a-b),moving=new Set(moved);
  if(moved.some(i=>!roots.includes(i)&&['sofa','sillon','silla','mesa','tv','cama','cama_doble'].includes(OBJETOS[P[i].obj].rol)))return null;
  const volume=p=>{const b=caja(p.obj),[x,z]=rot((b.x0+b.x1)/2,(b.z0+b.z1)/2,p.ry);return{cx:p.x+x,cz:p.z+z,hw:b.w/2,hd:b.d/2,a:p.ry,y0:p.y+b.y0,y1:p.y+b.y1};};
  const inside=(v)=>v.y0>=-.005&&v.y1<=H+.005&&[[-1,-1],[-1,1],[1,-1],[1,1]].every(([a,b])=>{const[x,z]=rot(a*v.hw,b*v.hd,v.a);return v.cx+x>=Z.x0-.005&&v.cx+x<=Z.x1+.005&&v.cz+z>=Z.z0-.005&&v.cz+z<=Z.z1+.005;});
  // El mapa de la casa usa envolventes en muebles de suelo. Se añaden a las partes.
  const walkParts=Q=>Q.flatMap(p=>{const b=caja(p.obj);return partes(p).concat(p.sop==null&&!['pared','techo'].includes(p.regla)&&OBJETOS[p.obj].clase!=='PICKUP'&&b.h>=.3?[volume(p)]:[]);});
  const reachable=(map,x,z,r=.15)=>{for(let k=Math.max(0,Math.floor((z-r)/map.S));k<Math.min(map.nz,Math.ceil((z+r)/map.S));k++)for(let j=Math.max(0,Math.floor((x-r+planta.W/2)/map.S));j<Math.min(map.nx,Math.ceil((x+r+planta.W/2)/map.S));j++)if(map.reach[k*map.nx+j]&&Math.hypot(-planta.W/2+(j+.5)*map.S-x,(k+.5)*map.S-z)<=r)return true;return false;};
  const front=p=>{const b=caja(p.obj),[x,z]=rot((b.x0+b.x1)/2,b.z1+.5,p.ry);return[p.x+x,p.z+z];};
  const before=mapaPaso(planta,walkParts(P),.05,.8,inicio),seats=P.flatMap((p,i)=>!moving.has(i)&&['sofa','sillon','silla'].includes(OBJETOS[p.obj].rol)&&reachable(before,...front(p),.65)?[i]:[]);
  const sizes=roots.map(i=>caja(P[i].obj)),[lb,sb,tb,ab]=sizes;
  // Biblioteca, mesa y asiento juntos; lámpara a su lado, sin invadir su frente.
  const positions=[{cx:0,back:.03},{cx:lb.w/2+.10+tb.w+.22+sb.w/2,back:.20},{cx:lb.w/2+.10+tb.w/2,back:.22},{cx:lb.w/2+.10+tb.w+.22+sb.w+.10+ab.w/2,back:.03}];
  const min=-lb.w/2,max=positions[3].cx+ab.w/2,span=max-min,mid=(min+max)/2;
  const walls={E:{ry:-Math.PI/2,x:Z.x1,z:(Z.z0+Z.z1)/2,len:Z.z1-Z.z0},W:{ry:Math.PI/2,x:Z.x0,z:(Z.z0+Z.z1)/2,len:Z.z1-Z.z0},N:{ry:Math.PI,x:(Z.x0+Z.x1)/2,z:Z.z1,len:Z.x1-Z.x0},S:{ry:0,x:(Z.x0+Z.x1)/2,z:Z.z0,len:Z.x1-Z.x0}};
  const attempts=[];
  const candidates=[];
  // Rincón junto a la biblioteca existente: conserva su pared y toda la galería.
  const library=P[roots[0]];
  for(const mirror of [1,-1])for(const depth of [1.0,1.2]){
    const positions=[{cx:0,z:0},{cx:-.85*mirror,z:depth-sb.z0},{cx:-.05*mirror,z:1.25-tb.z0},{cx:.65*mirror,z:.5-ab.z0}];
    const targets=new Map(roots.map((i,k)=>{const p=positions[k],[x,z]=rot(p.cx,p.z,library.ry);return[i,{x:library.x+x,z:library.z+z,ry:library.ry}];}));
    candidates.push({side:'biblioteca_actual',offset:mirror*depth,targets});
  }
  for(const side of cfg.paredes){const wall=walls[side];if(span>wall.len-.08)continue;
    const slack=(wall.len-span)/2-.04,offsets=[0];for(let n=1;n*.1<=slack;n++)offsets.push(n*.1,-n*.1);
    for(const offset of offsets){const targets=new Map(roots.map((i,k)=>{const b=sizes[k],[x,z]=rot(positions[k].cx-mid+offset,positions[k].back-b.z0,wall.ry);return[i,{x:wall.x+x,z:wall.z+z,ry:wall.ry}];}));candidates.push({side,offset,targets});}
  }
  for(const {side,offset,targets} of candidates){
      const Q=P.map((p,i)=>{if(!moving.has(i))return p;const r=owner.get(i),old=P[r],to=targets.get(r),[lx,lz]=rot(p.x-old.x,p.z-old.z,-old.ry),[x,z]=rot(lx,lz,to.ry),q={...p,x:to.x+x,z:to.z+z,ry:p.ry-old.ry+to.ry};q.v=volume(q);return q;});
      const error=[];
      for(const i of moved){const p=Q[i],bits=partes(p);
        if(!inside(p.v))error.push('fuera');
        if(libres.some(l=>bits.some(b=>penetra(l,b)>.005)))error.push('hueco');
        if(Q.some((q,j)=>i!==j&&owner.get(i)!==owner.get(j)&&bits.some(a=>partes(q).some(b=>penetra(a,b)>.005))))error.push('colision');
        if(p.sop!=null){const s=Q[p.sop],R=superficie(s.obj,p.sup);if(!R)error.push('apoyo');else{const[x,z]=rot(p.x-s.x,p.z-s.z,-s.ry);if(Math.abs(p.y-(s.y+R.y))>.015||x<R.x0-.005||x>R.x1+.005||z<R.z0-.005||z>R.z1+.005)error.push('apoyo');}}
      }
      for(const i of roots.slice(0,3)){const p=Q[i],b=caja(p.obj),F=espacioFrontal(p,b,[i===roots[1]?.8:Math.min(.8,b.w),.8]);
        if(!inside(F)||Q.some((q,j)=>j!==i&&partes(q).some(v=>penetra(F,v)>.005)))error.push('frente');
      }
      if(!error.length){const map=mapaPaso(planta,walkParts(Q),.05,.8,inicio);
        if(typeof inicio==='object'&&!reachable(map,inicio.x,inicio.z,.15))error.push('inicio');
        for(const i of roots.slice(0,3)){const F=espacioFrontal(Q[i],caja(Q[i].obj),[.8,.8]);if(!reachable(map,F.cx,F.cz))error.push('acceso');}
        if(seats.some(i=>!reachable(map,...front(Q[i]),.65)))error.push('asiento_existente');
      }
      if(!error.length&&!aceptar(Q))error.push('paso_o_funcion');
      attempts.push({pared:side,offset,errores:[...new Set(error)],detalle:diagnostico.detallado?{frentes:roots.slice(0,3).map(i=>{const F=espacioFrontal(Q[i],caja(Q[i].obj),[i===roots[1]?.8:Math.min(.8,caja(Q[i].obj).w),.8]);return{indice:i,contra:Q.flatMap((q,j)=>j!==i&&partes(q).some(v=>penetra(F,v)>.005)?[{i:j,obj:q.obj}]:[])}}),colisiones:moved.flatMap(i=>Q.flatMap((q,j)=>j!==i&&partes(Q[i]).some(a=>partes(q).some(b=>penetra(a,b)>.005))?[{i,j,a:Q[i].obj,b:q.obj}]:[]))}:undefined});
      if(!error.length)return{P:Q,metadata:{pared:side,offset,biblioteca:roots[0],asiento:roots[1],mesita:roots[2],lampara:roots[3],movidos:moved,intentos:attempts}};
  }
  diagnostico({roots,moved,attempts});return null;
}
