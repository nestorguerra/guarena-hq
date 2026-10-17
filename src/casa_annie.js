// Mobiliario por kit en el plano propio de Annie. El dormitorio conserva su decoración y caja fuerte.
import { amueblar, filtroHogar } from './locales.js';
import { construir, caja } from './objetos.js';
import { OBJETOS } from './interiores_datos.js';
import { rot, mapaPaso, partes } from './interiores_geo.js';
import { revestirEstancia } from './acabados_vivienda.js';

export function amueblarAnnie(B, seed, segs0, segs1) {
  const f=.09, estancias=[], rooms=[], tv=[];
  const specs=[
    {id:'saloncito',tipo:'salon',rect:[-3.2,0,3.2,3.8],lv:0,puertas:[['s',-.55,.55],['n',1.5,2.4]],ventanas:[['s',-2.8,-1.5]]},
    {id:'cocina',tipo:'cocina',rect:[-3.2,3.8,.9,8.4],lv:0,puertas:[['e',4.25,5.15]]},
    {id:'bano',tipo:'bano',rect:[-3.2,8.4,.9,10.5],lv:0,puertas:[['e',9.3,10.1]],ventanas:[['n',-2.4,-1.4]]},
    {id:'banoAlto',tipo:'bano',rect:[-3.2,5,.9,7.4],lv:1,puertas:[['e',5.85,6.75]]},
    {id:'estudio',tipo:'estudio',rect:[-3.2,7.4,.9,10.5],lv:1,puertas:[['e',9.5,10.4]],ventanas:[['n',-2.3,-1.4]]},
  ];
  for(const [ri,s] of specs.entries()) {
    const [x0,z0,x1,z1]=s.rect,ox=(x0+x1)/2,oz=z0+f,y=s.lv*3.1,W=x1-x0-2*f,D=z1-z0-2*f;
    revestirEstancia(B,{type:s.tipo,x0,z0,x1,z1,lv:s.lv,open:[...s.puertas.map(([side,a,b])=>({side,a,b,door:true})),...(s.ventanas||[]).map(([side,a,b])=>({side,a,b,door:false}))]},{seed:seed+ri,perfil:'annie',estilo:'alegre',altura:s.lv?2.75:2.95,inset:.086});
    const libres=[];
    for(const [side,a,b] of [...s.puertas,...(s.ventanas||[])]){
      const puerta=s.puertas.some(q=>q[0]===side&&q[1]===a),d=puerta?1:.38,ancho=(b-a)/2+(puerta?.15:.05);
      libres.push(side==='s'||side==='n'?{cx:(a+b)/2-ox,cz:side==='s'?d/2:D-d/2,hw:ancho,hd:d/2,a:0,y0:puerta?0:.92,y1:2.4}:{cx:side==='w'?-W/2+d/2:W/2-d/2,cz:(a+b)/2-oz,hw:d/2,hd:ancho,a:0,y0:puerta?0:.92,y1:2.4});
    }
    const [side,a,b]=s.puertas[0],inicio=side==='s'?{x:(a+b)/2-ox,z:.5}:side==='n'?{x:(a+b)/2-ox,z:D-.5}:{x:side==='e'?W/2-.5:-W/2+.5,z:(a+b)/2-oz};
    const filtro=filtroHogar({perfil:'familia',estilo:'alegre',habitacion:s.tipo,botin:[]});
    let A, faltan;
    for(let n=0;n<24;n++){
      A=amueblar('vivienda_'+s.tipo,seed*131+ri*17+5+n*104729,{W,D,H:s.lv?2.75:2.95,inicio,libres,filtro,funciones:true});
      faltan=A.activas.filter(ei=>{const e=A.K.objetos[ei],num=A.P.filter(p=>p.e===ei&&(e.regla!=='conjunto'||p.de==null)).length;return num<Math.max(e.obligatorio?1:0,e.cantidad?.[0]||0);});
      if(!faltan.length)break;
    }
    if(faltan.length)throw Error('Annie/'+s.id+': faltan entradas '+faltan.join(','));
    const colocados=A.P.map((p,i)=>({i,...p,clase:OBJETOS[p.obj].clase,de:p.de??null}));
    const e={kit:'vivienda_'+s.tipo,sala:s.id,tipologia:A.K.tipologia,seed:A.seed,W,D,H:A.H,origen:{x:B.ox+ox,y,z:B.oz+oz},inicio,ancho:A.ancho,zonas:A.zonas,tabiques:[],libres,luces:[],activas:A.activas,debe:A.debe,avisos:A.avisos,hogar:{perfil:'annie',estilo:'alegre'},colocados};
    estancias.push(e);rooms.push({id:s.id,type:s.tipo,lv:s.lv,x0:B.ox+x0,z0:B.oz+z0,x1:B.ox+x1,z1:B.oz+z1});
    // Proyectar cada acción a suelo alcanzable del kit, antes de añadir la pared de la casa.
    const mp=mapaPaso(e,colocados.flatMap(partes),.05,e.ancho,inicio),celdas=[];
    for(let c=0;c<mp.reach.length;c++)if(mp.reach[c])celdas.push({x:-W/2+(c%mp.nx+.5)*mp.S,z:(Math.floor(c/mp.nx)+.5)*mp.S});
    const punto=(p,bb)=>{
      const [dx,dz]=rot((bb.x0+bb.x1)/2,bb.z1+.45,p.ry),x=p.x+dx,z=p.z+dz;
      const q=celdas.reduce((best,q)=>!best||Math.hypot(q.x-x,q.z-z)<Math.hypot(best.x-x,best.z-z)?q:best,null);
      if(!q||Math.hypot(q.x-x,q.z-z)>.95)throw Error('Annie/'+s.id+': acción inaccesible '+p.obj);
      return {x:ox+q.x,z:oz+q.z,y};
    };
    B.segs=s.lv?segs1:segs0;
    const items=A.P.map((p,i)=>({obj:p.obj,x:B.ox+ox+p.x,y:y+(p.y||0),z:B.oz+oz+p.z,ry:p.ry,seed:seed+ri*97+i,paleta:{madera:'#b58d70',tela:['#a9bdc9','#d6a5b5','#d2c7ad']}}));
    const g=construir(items);B.extra.push(g);
    for(const [i,p] of A.P.entries()){
      const o=OBJETOS[p.obj],bb=caja(p.obj);
      if(p.sop==null&&!['pared','techo'].includes(p.regla)&&o.clase!=='PICKUP'&&bb.h>=.3){const [dx,dz]=rot((bb.x0+bb.x1)/2,(bb.z0+bb.z1)/2,p.ry);B.footprint(bb.w,bb.d,ox+p.x+dx,oz+p.z+dz,p.ry,Math.min(bb.h,2.2));}
      const tipos={tv:['tv','Encender la tele'],cocina:['eat','Picar algo de la cocina'],nevera:['fridge','Abrir la nevera'],comoda:['drawer','Registrar los cajones'],espejo:['mirror','Mirarse al espejo'],libros:['read','Hojear un libro']};
      if(tipos[o.rol]){
        const [type,label]=tipos[o.rol],q=punto(p,bb),mesh=o.rol==='tv'?g.userData.aparte.find(a=>a.i===i)?.mesh:undefined;
        B.interact({...q,sala:s.id,type,label,r:.9,...(mesh?{mesh}:{})});if(mesh)tv.push({mesh});
      }
    }
    const l=B.light(ox,y+A.H-.33,oz+D/2,s.tipo==='bano'?0xf4f1e8:0xffe5cd,Math.max(5,D*1.5),Math.max(6,D+1));
    B.extra[B.extra.length-1].visible=false;
    e.modoLuz='casa';e.luces=[{x:0,y:A.H-.33,z:D/2,color:l.color.getHex(),intensidad:l.intensity,alcance:l.distance}];
  }
  return {estancias,rooms,tv};
}
