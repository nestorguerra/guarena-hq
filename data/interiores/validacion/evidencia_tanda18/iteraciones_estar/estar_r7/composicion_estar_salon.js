// Relaciona mesa y alfombra existentes con el sofá. No añade objetos ni usa azar.
import { OBJETOS } from './interiores_datos.js';
import { caja } from './objetos.js';
import { rot, partes, penetra, superficie, mapaPaso } from './interiores_geo.js';
export function componerEstar({P,K,ctx,planta,H,libres,inicio,aceptar}){
  const cfg=K.composicion_lectura;
  if(!cfg||K.tipologia!=='salon'||!ctx?.funciones||!cfg.perfiles.includes(ctx.perfil)||planta.W*planta.D<cfg.area_min)return null;
  const root=p=>p.sop==null&&p.de==null&&!['pared','techo'].includes(p.regla);
  const si=P.findIndex(p=>root(p)&&OBJETOS[p.obj].rol==='sofa'),ti=P.findIndex(p=>root(p)&&['mesa_centro','mesa_centro_cristal'].includes(p.obj));
  if(si<0||ti<0||P[si].zona!==P[ti].zona)return null;
  const ri=P.findIndex(p=>root(p)&&p.obj==='alfombra_salon'&&p.zona===P[si].zona),roots=ri<0?[ti]:[ti,ri],owner=new Map(roots.map(i=>[i,i])),visiting=new Set();
  const dependent=i=>{if(owner.has(i))return owner.get(i);if(visiting.has(i))throw Error('ciclo');visiting.add(i);const links=[P[i].sop,P[i].de].filter(j=>j!=null);if(links.some(j=>!Number.isInteger(j)||!P[j]))throw Error('referencia');const found=[...new Set(links.map(dependent).filter(j=>j!=null))];visiting.delete(i);if(found.length>1)throw Error('dependencia cruzada');const result=found[0]??null;owner.set(i,result);return result;};
  try{P.forEach((p,i)=>dependent(i));}catch{return null;}
  const moving=new Set([...owner].filter(([,root])=>root!=null).map(([i])=>i));
  if(moving.has(si)||[...moving].some(i=>!roots.includes(i)&&['sofa','sillon','silla','cama','cama_doble','tv'].includes(OBJETOS[P[i].obj].rol)))return null;
  const Z=planta.zonas[P[si].zona],sofa=P[si],sb=caja(sofa.obj),tb=caja(P[ti].obj);
  const volume=p=>{const b=caja(p.obj),[x,z]=rot((b.x0+b.x1)/2,(b.z0+b.z1)/2,p.ry);return{cx:p.x+x,cz:p.z+z,hw:b.w/2,hd:b.d/2,a:p.ry,y0:(p.y||0)+b.y0,y1:(p.y||0)+b.y1};};
  const inside=v=>v.y0>=-.005&&v.y1<=H+.005&&[[-1,-1],[-1,1],[1,-1],[1,1]].every(([a,b])=>{const[x,z]=rot(a*v.hw,b*v.hd,v.a);return v.cx+x>=Z.x0-.005&&v.cx+x<=Z.x1+.005&&v.cz+z>=Z.z0-.005&&v.cz+z<=Z.z1+.005;});
  const parts=Q=>Q.flatMap(p=>partes(p).concat(root(p)&&OBJETOS[p.obj].clase!=='PICKUP'&&caja(p.obj).h>=.3?[volume(p)]:[]));
  const baseline=mapaPaso(planta,parts(P),.05,.8,inicio);
  const distance=(map,x,z)=>{let d=Infinity;for(let i=0;i<map.reach.length;i++)if(map.reach[i])d=Math.min(d,Math.hypot(-planta.W/2+(i%map.nx+.5)*map.S-x,(Math.floor(i/map.nx)+.5)*map.S-z));return d;};
  const seats=P.flatMap(p=>['sofa','sillon','silla'].includes(OBJETOS[p.obj].rol)?(OBJETOS[p.obj].asientos||[]).map(a=>{const[x,z]=rot(a.p[0],a.p[2],p.ry);return{x:p.x+x,z:p.z+z};}):[]).filter(s=>distance(baseline,s.x,s.z)<1.2);
  const attempts=[];
  for(const gap of [.55,.65,.75,.85,.95])for(const lateral of [0,-.1,.1]){
    const[dx,dz]=rot((sb.x0+sb.x1)/2+lateral,sb.z1+gap-tb.z0,sofa.ry),target={x:sofa.x+dx,z:sofa.z+dz,ry:sofa.ry};
    
    const Q=P.map((p,i)=>{
      if(!moving.has(i))return p;
      let q;
      const base=P[owner.get(i)],to=target;
      const[x,z]=rot(p.x-base.x,p.z-base.z,-base.ry),[xx,zz]=rot(x,z,to.ry);q={...p,x:to.x+xx,z:to.z+zz,ry:p.ry-base.ry+to.ry};
      q.v=volume(q);return q;
    });
    const errors=[];
    for(const i of moving){const p=Q[i],bits=partes(p);
      if(!inside(p.v))errors.push('limites');
      if(bits.some(a=>libres.some(b=>penetra(a,b)>.005)))errors.push('hueco');
      if(Q.some((q,j)=>j!==i&&owner.get(j)!==owner.get(i)&&bits.some(a=>partes(q).some(b=>penetra(a,b)>.005))))errors.push('colision');
      if(p.sop!=null){const s=Q[p.sop],R=superficie(s.obj,p.sup);if(!R)errors.push('apoyo');else{const[x,z]=rot(p.x-s.x,p.z-s.z,-s.ry);if(Math.abs((p.y||0)-((s.y||0)+R.y))>.015||x<R.x0-.005||x>R.x1+.005||z<R.z0-.005||z>R.z1+.005)errors.push('apoyo');}}
    }
    if(!errors.length){const map=mapaPaso(planta,parts(Q),.05,.8,inicio),ix=Math.floor((inicio.x+planta.W/2)/map.S),iz=Math.floor(inicio.z/map.S),c=iz*map.nx+ix;
      if(ix<0||ix>=map.nx||iz<0||iz>=map.nz||!map.free[c]||!map.reach[c])errors.push('inicio');
      if(seats.some(s=>distance(map,s.x,s.z)>=1.2))errors.push('asiento');
      if(!aceptar(Q))errors.push('paso_o_uso');
    }
    attempts.push({gap,lateral,errores:[...new Set(errors)]});
    if(!errors.length)return{P:Q,metadata:{sofa:si,mesa:ti,alfombra:ri<0?null:ri,gap,lateral,movidos:[...moving].sort((a,b)=>a-b),intentos:attempts}};
  }
  return null;
}
