import fs from 'node:fs';import assert from 'node:assert/strict';import{runtime,overrides}from'./runtime.cpu.mjs';
for(const p of ['src/locales.js','src/houses.js'])overrides.set(p,fs.readFileSync('.cache/calidad/tanda18/estar_r7/'+p.split('/').at(-1),'utf8'));
const base=runtime(false),next=runtime(true),seeds=JSON.parse(fs.readFileSync('.cache/calidad/tanda18/medidas/salones_base.json')).rows.map(r=>r.seed),rows=[];
for(const seed of seeds){let a,b;try{
 a=base.H.buildVecino(seed,{x:-5200,z:-5200});b=next.H.buildVecino(seed,{x:-5200,z:-5200});
 const x=a.estancias.find(e=>e.kit==='vivienda_salon'),e=b.estancias.find(e=>e.kit==='vivienda_salon'),meta=e.composicionEstar;
 assert.deepEqual(e.colocados.map(p=>[p.obj,p.e,p.sop,p.sup,p.de,p.clase]),x.colocados.map(p=>[p.obj,p.e,p.sop,p.sup,p.de,p.clase]),'identidades');
 assert.deepEqual(a.estancias.filter(q=>q!==x),b.estancias.filter(q=>q!==e),'otras estancias');
 assert.deepEqual(a.inter.map(i=>[i.type,i.label,i.def]),b.inter.map(i=>[i.type,i.label,i.def]),'acciones');
 if(!meta)assert.deepEqual(e.colocados,x.colocados,'fallback');
 else for(let i=0;i<e.colocados.length;i++)if(!meta.movidos.includes(i))assert.deepEqual(e.colocados[i],x.colocados[i],'mueve pieza ajena');
 const use=next.V.revisarUso(b);assert.equal(use.errores.length,0,JSON.stringify(use.errores));
 let meshes=0,tris=0;b.group.traverse(o=>{if(o.isMesh){meshes++;tris+=(o.geometry.index?.count||o.geometry.attributes.position.count)/3;}});
 rows.push({seed,perfil:b.profile.id,aplicado:!!meta,metadata:meta??null,placed:e.colocados,frame:{W:e.W,D:e.D,H:e.H},meshes,tris,use});
 console.log(seed,meta?'APLICADO gap'+meta.gap:'BASE');
}catch(err){rows.push({seed,error:String(err.stack||err)});console.log(seed,String(err));}finally{for(const h of[a,b])if(h)h.group.traverse(o=>{if(o.isMesh)o.geometry.dispose();});}}
fs.writeFileSync('.cache/calidad/tanda18/estar_r7/resultados.json',JSON.stringify({estado:'PRIVADO_ESTARR7_CPU_NO_RASTER',rows},null,2)+'\n');assert.equal(rows.filter(r=>r.error).length,0);assert(rows.some(r=>r.aplicado),'cero admisiones');
