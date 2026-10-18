import fs from 'node:fs';import assert from 'node:assert/strict';
import {runtime} from '../postpaso_r3/runtime.cpu.mjs';
const rt=runtime(false),{geo,caja,data}=rt;
const src=fs.readFileSync('.cache/calidad/tanda18/postpaso_r3/composicion_lectura_salon.js','utf8');
const deps={...geo,caja,...data};const compose=new Function(...Object.keys(deps),src.replace(/^import .*;\n/gm,'').replace('export function','function')+';return componerLectura;')(...Object.values(deps));
const base=JSON.parse(fs.readFileSync('.cache/calidad/tanda18/medidas/salones_base.json')).rows.find(r=>r.seed===3244),P=structuredClone(base.placed),cfg=JSON.parse(fs.readFileSync('.cache/calidad/tanda18/postpaso_r3/config.json'));
const planta={...base.frame,zonas:base.zonas,tabiques:[]},K={...data.KITS.vivienda_salon,composicion_lectura:cfg};
const params={P,K,ctx:{funciones:true,perfil:base.perfil},planta,H:base.frame.H,libres:base.libres,inicio:base.inicio,aceptar:()=>true};
const before=JSON.stringify(P),out=compose(params);assert(out);assert.equal(before,JSON.stringify(P));
const vol=p=>{const b=caja(p.obj),[x,z]=geo.rot((b.x0+b.x1)/2,(b.z0+b.z1)/2,p.ry);return{cx:p.x+x,cz:p.z+z,hw:b.w/2,hd:b.d/2,a:p.ry,y0:p.y+b.y0,y1:p.y+b.y1};};
const walk=Q=>Q.flatMap(p=>{const b=caja(p.obj);return geo.partes(p).concat(p.sop==null&&!['pared','techo'].includes(p.regla)&&data.OBJETOS[p.obj].clase!=='PICKUP'&&b.h>=.3?[vol(p)]:[]);});
const cell=(map,x,z)=>Math.floor(z/map.S)*map.nx+Math.floor((x+planta.W/2)/map.S);
const bm=geo.mapaPaso(planta,walk(P),.05,.8,base.inicio),am=geo.mapaPaso(planta,walk(out.P),.05,.8,base.inicio);
let repro=null;
for(let k=1;k<am.nz-1&&!repro;k++)for(let j=1;j<am.nx-1&&!repro;j++){
 const index=k*am.nx+j;if(!bm.free[index]||am.free[index])continue;
 const inicio={x:-planta.W/2+(j+.5)*.05,z:(k+.5)*.05};
 let near=false;for(let dz=-2;dz<=2;dz++)for(let dx=-2;dx<=2;dx++)if(am.reach[(k+dz)*am.nx+j+dx])near=true;if(!near)continue;
 const candidate=compose({...params,inicio});if(!candidate)continue;
 const actual=geo.mapaPaso(planta,walk(candidate.P),.05,.8,inicio),ix=cell(actual,inicio.x,inicio.z);
 if(!actual.free[ix])repro={inicio,beforeFree:!!bm.free[index],afterFree:!!actual.free[ix],afterReach:!!actual.reach[ix],admitted:candidate.metadata.pared,offset:candidate.metadata.offset};
}
const result={scope:'Helper exacto y mapaPaso/partes/caja reales. aceptar neutral: reproduce guarda de inicio del helper, no un buildVecino completo.',baselineAdmitted:out.metadata.pared,baseUnmutated:JSON.stringify(P)===before,blockedStartAccepted:repro};
fs.writeFileSync('.cache/calidad/tanda18/revision_r3/dirigida.json',JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result));
