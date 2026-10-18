import fs from 'node:fs';import crypto from 'node:crypto';import assert from 'node:assert/strict';
import {runtime} from './runtime.cpu.mjs';
const out='.cache/calidad/tanda18/medidas/',freeze=JSON.parse(fs.readFileSync('.cache/calidad/tanda17/estado_candidato.json')).archivos,hash=p=>crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const verify=()=>{for(const[p,h]of Object.entries(freeze))assert.equal(hash(p),h,p);};verify();
const api=runtime(true),seeds=JSON.parse(fs.readFileSync('data/interiores/validacion/casas_pueblo.json')).resultados.map(r=>r.seed),rows=[];
assert.equal(new Set(seeds).size,22);
for(const seed of seeds){const h=api.H.buildVecino(seed,{x:-5200,z:-5200});try{
 const e=h.estancias.find(e=>e.kit==='vivienda_salon');assert(e,seed+': sin salón');let meshes=0,tris=0;h.group.traverse(o=>{if(o.isMesh&&o.visible){meshes++;tris+=(o.geometry.index?.count||o.geometry.attributes.position.count)/3;}});
 rows.push({seed,perfil:h.profile.id,estilo:h.profile.style,sala:e.sala,frame:{W:e.W,D:e.D,H:e.H},inicio:e.inicio,libres:e.libres,origen:e.origen,zonas:e.zonas,placed:e.colocados,objects:e.colocados.map(p=>{const b=api.caja(p.obj);return{...p,footprint:{x0:b.x0,x1:b.x1,z0:b.z0,z1:b.z1,h:b.h},rol:api.data.OBJETOS[p.obj].rol};}),meshes,tris,actions:h.inter.filter(i=>i.sala===e.sala).map(i=>({type:i.type,label:i.label,x:i.x,y:i.y,z:i.z})),use:api.V.revisarUso(h)});
}finally{h.group.traverse(o=>{if(o.isMesh)o.geometry.dispose();});}}
verify();const d={state:'BASE_T17_MEASURES_CPU',scope:'22 town salon identities, actual sources and catalogue, Three170 constructor/Canvas tracing substitute. Not raster/performance; independent browser base is separate.',sourceInputsStable:Object.keys(freeze).length,rows};fs.writeFileSync(out+'salones_base.json',JSON.stringify(d,null,2)+'\n');console.log(JSON.stringify(rows.map(({seed,perfil,frame,meshes,objects,actions})=>({seed,perfil,frame,meshes,principal:objects.filter(o=>o.sop==null).map(o=>o.obj),acciones:actions.length})),null,2));
