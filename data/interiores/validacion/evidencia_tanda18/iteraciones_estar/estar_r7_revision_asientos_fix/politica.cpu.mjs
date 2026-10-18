import fs from'node:fs';import assert from'node:assert/strict';import{runtime}from'../../estar_r7/runtime.cpu.mjs';
const folder='.cache/calidad/tanda18/estar_r7_revision/asientos_fix/',rt=runtime(false),h=rt.H.buildVecino(3244),e=h.estancias.find(e=>e.kit==='vivienda_salon'),P=structuredClone(e.colocados),K=rt.data.KITS.vivienda_salon,source=fs.readFileSync(folder+'composicion_estar_salon.js','utf8'),rows=[];
const clean=s=>s.replace(/^import .*;\n/gm,'').replace('export function','function');
const params={P,K,ctx:{funciones:true,perfil:e.hogar.perfil},planta:{W:e.W,D:e.D,zonas:e.zonas,tabiques:e.tabiques},H:e.H,libres:e.libres,inicio:e.inicio,aceptar:()=>true,asientoLectura:e.composicionLectura.asiento};
const seatPoint=(p,i=0)=>{const a=rt.data.OBJETOS[p.obj].asientos[i],[x,z]=rt.geo.rot(a.p[0],a.p[2],p.ry);return{x:p.x+x,z:p.z+z};};
const sofa=P.find(p=>rt.data.OBJETOS[p.obj].rol==='sofa'),puff=P[e.composicionLectura.asiento];
function run(name,target,rad0,rad1,mutate,expected){let calls=0,dist=[];
 // Doble explícito del mapa de alcanzabilidad: controla sólo la política de
 // alcance, conserva inicio literal. Geometría/owner/colisiones siguen reales.
 const mapaPaso=()=>{const S=.05,nx=Math.ceil(e.W/S),nz=Math.ceil(e.D/S),free=new Uint8Array(nx*nz).fill(1),reach=new Uint8Array(nx*nz),rad=calls++===0?rad0:rad1;let nearest=Infinity;
 for(let i=0;i<reach.length;i++){const x=-e.W/2+(i%nx+.5)*S,z=(Math.floor(i/nx)+.5)*S,d=Math.hypot(x-target.x,z-target.z);if(d>=rad){reach[i]=1;nearest=Math.min(nearest,d);}}
 const ix=Math.floor((e.inicio.x+e.W/2)/S),iz=Math.floor(e.inicio.z/S);assert(reach[iz*nx+ix],'fixture debe dejar entrada');dist.push(nearest);return{S,nx,nz,free,reach};};
 const deps={...rt.data,...rt.geo,caja:rt.caja,mapaPaso},helper=new Function(...Object.keys(deps),clean(mutate(source))+';return componerEstar;')(...Object.values(deps)),result=helper(params);assert.equal(!!result,expected,name);rows.push({name,accepted:!!result,nearest:dist.slice(0,2),calls,state:'PASS'});
}
try{
 run('puff exacto protegido',seatPoint(puff),.95,1.26,s=>s,false);
 run('RED al omitir puff',seatPoint(puff),.95,1.26,s=>s.replace('||i===asientoLectura',''),true);
 run('baseline seleccionable 1.20..1.25 protegido',seatPoint(sofa,1),1.205,1.26,s=>s,false);
 run('RED al excluir baseline desde1.2',seatPoint(sofa,1),1.205,1.26,s=>s.replace('distance(baseline,s.x,s.z)<1.25','distance(baseline,s.x,s.z)<1.2'),true);
 run('candidato seleccionable entre1.20..1.25 válido',seatPoint(sofa,1),.95,1.205,s=>s,true);
 const result={state:'PASS',scope:'Política de alcance: mapas reach controlados explícitos, geometría/catálogo reales3244. No prueba ruta física nueva ni navegador.',rows};fs.writeFileSync(folder+'politica_cpu.json',JSON.stringify(result,null,2)+'\n');console.log(result);
}finally{h.group.traverse(o=>{if(o.isMesh)o.geometry.dispose();});}
