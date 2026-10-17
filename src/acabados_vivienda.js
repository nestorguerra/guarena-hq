// Acabados domésticos propios: superficies serenas que dejan leer muebles y usos.
// Son láminas de pocos milímetros; no cambian el plano, los huecos ni los colliders.
import { planeGeo, std } from './housekit.js';
import { mulberry32 } from './util.js';

// Rectángulos de una pared, descontando puertas y ventanas, también si se solapan.
export function panosPared(a, b, y0, y1, huecos) {
  let rects=[[a,b,y0,y1]];
  for(const h of huecos) {
    const next=[];
    for(const p of rects) {
      const x0=Math.max(p[0],h[0]),x1=Math.min(p[1],h[1]),v0=Math.max(p[2],h[2]),v1=Math.min(p[3],h[3]);
      if(x0>=x1||v0>=v1){next.push(p);continue;}
      for(const q of [[p[0],x0,p[2],p[3]],[x1,p[1],p[2],p[3]],[x0,x1,p[2],v0],[x0,x1,v1,p[3]]])if(q[1]-q[0]>.001&&q[3]-q[2]>.001)next.push(q);
    }
    rects=next;
  }
  return rects;
}

export function revestirEstancia(B, rm, {seed=1, perfil='', estilo='', altura=2.95, inset=.076}={}) {
  const bath=rm.type==='bano',work=rm.type==='taller'&&perfil!=='artista';
  if(!bath&&!work)return;
  const r=mulberry32(seed*347+rm.x0*13+rm.z0*53),y=(rm.lv||0)*3.1;
  const mat=c=>B.mat('acabado_domestico_'+c,()=>std(c,{roughness:.92,defines:{CLAY_TONE:.10,CLAY_CAV:.015,CLAY_RELIEF:.12,CLAY_AMP:.0003}}));
  const tonos=bath?[
    ['#7e9891','#e4e0d3','#c9c6b9','#678078'],
    ['#8297a2','#e5e1d7','#cbc9bf','#667d87'],
    ['#b39880','#eee4d4','#d3c4b2','#91775e'],
  ][Math.abs(seed)%3]:[['#e4d8bd','#617568','#aaa28b','#4c5f53'],['#ddd8c8','#667b80','#b3ac9b','#4f6468']][Math.abs(seed)%2];
  const limite=bath?1.28:1.02;
  const alto=mat(tonos[0]),bajo=mat(tonos[1]),junta=mat(tonos[2]),borde=mat(tonos[3]);
  for(const side of ['s','n','w','e']) {
    const horizontal=side==='s'||side==='n',a=horizontal?rm.x0:rm.z0,b=horizontal?rm.x1:rm.z1;
    const huecos=(rm.open||[]).filter(o=>o.side===side).map(o=>[o.a,o.b,o.door?0:.92,o.door?2.1:2.08]);
    const ry={s:0,n:Math.PI,w:Math.PI/2,e:-Math.PI/2}[side];
    const dibujo=(key,q,offset=0)=>{
      const c=(q[0]+q[1])/2,px=horizontal?c:side==='w'?rm.x0+inset+offset:rm.x1-inset-offset,pz=horizontal?(side==='s'?rm.z0+inset+offset:rm.z1-inset-offset):c;
      B.add(key,planeGeo(q[1]-q[0],q[3]-q[2]),px,y+(q[2]+q[3])/2,pz,ry);
    };
    for(const p of panosPared(a,b,limite,altura,huecos))dibujo(alto,p);
    for(const p of panosPared(a,b,0,limite,huecos)) {
      if(bath) {
        // Junta y azulejo comparten plano y ocupan áreas disjuntas. Sin láminas
        // superpuestas que produzcan sombras propias o bandas al mirar de lado.
        for(let u=Math.floor(p[0]/.25)*.25;u<p[1];u+=.25)for(let v=0;v<p[3];v+=.125){
          const x0=Math.max(p[0],u),x1=Math.min(p[1],u+.25),v0=Math.max(p[2],v),v1=Math.min(p[3],v+.125);
          if(x1-x0<.001||v1-v0<.001)continue;
          const j=Math.min(.0015,(x1-x0)/3,(v1-v0)/3);
          dibujo(bajo,[x0+j,x1-j,v0+j,v1-j]);
          for(const q of [[x0,x1,v0,v0+j],[x0,x1,v1-j,v1],[x0,x0+j,v0+j,v1-j],[x1-j,x1,v0+j,v1-j]])dibujo(junta,q);
        }
      }else dibujo(bajo,p);
    }
    for(const p of panosPared(a,b,limite-.014,limite+.014,huecos))dibujo(borde,p,.005);
    if(bath)for(const o of (rm.open||[]).filter(o=>o.side===side&&!o.door)) {
      // Vidrio de privacidad: parte del baño visible también durante el juego,
      // con cerco claro y acabado mate; no una modificación de la fotografía.
      const l=o.a+.02,h=o.b-.02,v0=.96,v1=2.04,j=.035;
      dibujo(mat('#c5d7d1'),[l+j,h-j,v0+j,v1-j],.017);
      for(const q of [[l,l+j,v0,v1],[h-j,h,v0,v1],[l+j,h-j,v0,v0+j],[l+j,h-j,v1-j,v1]])dibujo(mat('#e2dac7'),q,.017);
    }

  }
  // Suelo y techo locales: el antiguo estampado no domina estas salas de servicio.
  const w=rm.x1-rm.x0,d=rm.z1-rm.z0,cx=(rm.x0+rm.x1)/2,cz=(rm.z0+rm.z1)/2;
  B.add(mat(bath?'#a8aaa1':'#a89c84'),planeGeo(w-.15,d-.15).rotateX(-Math.PI/2),cx,y+.009,cz);
  const paso=bath?.3:.6;
  for(let x=rm.x0+.076;x<rm.x1-.076;x+=paso)for(let z=rm.z0+.076;z<rm.z1-.076;z+=paso){
    const tw=Math.min(paso-.004,rm.x1-.076-x),td=Math.min(paso-.004,rm.z1-.076-z);
    if(tw<.001||td<.001)continue;
    const col=bath?['#c8c8bd','#c2c4b9','#cecec2'][Math.floor(r()*3)]:['#b7ac96','#b4a891','#beb29b'][Math.floor(r()*3)];
    B.add(mat(col),planeGeo(tw,td).rotateX(-Math.PI/2),x+tw/2,y+.0095,z+td/2);
  }
  B.add(mat('#e9e3d4'),planeGeo(w-.15,d-.15).rotateX(Math.PI/2),cx,y+altura-.008,cz);
}
