import fs from 'node:fs';import assert from 'node:assert/strict';import crypto from 'node:crypto';
import{runtime,overrides}from'./runtime.cpu.mjs';
for(const p of ['src/locales.js','src/houses.js'])overrides.set(p,fs.readFileSync('.cache/calidad/tanda18/postpaso_r3/'+p.split('/').at(-1),'utf8'));
const cfg={area_min:22,perfiles:['artista','estudiante','familia','rico'],biblioteca:['estanteria_libros','estanteria_libros_ancha'],asiento:['sillon_moderno','puff'],mesita:['mesita_auxiliar'],lampara:['lampara_pie'],paredes:['E','W','N','S']};
const base=runtime(false),next=runtime(true,d=>d.KITS.vivienda_salon.composicion_lectura=cfg),seeds=JSON.parse(fs.readFileSync('.cache/calidad/tanda18/medidas/salones_base.json')).rows.map(r=>r.seed),rows=[];
fs.writeFileSync('.cache/calidad/tanda18/postpaso_r3/config.json',JSON.stringify(cfg,null,2)+'\n');
const core=['mueble_tv','mueble_tv_pequeno','sofa_tres_plazas','sofa_dos_plazas','mesa_camilla','mesa_centro','mesa_centro_cristal'];
const flat=i=>JSON.parse(JSON.stringify(i,(k,v)=>['mesh','rm','group'].includes(k)?undefined:v));
for(const seed of seeds){let a,b;try{
 a=base.H.buildVecino(seed,{x:-5200,z:-5200});b=next.H.buildVecino(seed,{x:-5200,z:-5200});
 const x=a.estancias.find(e=>e.kit==='vivienda_salon'),e=b.estancias.find(e=>e.kit==='vivienda_salon'),meta=e.composicionLectura;
 assert.deepEqual(e.colocados.map(p=>[p.obj,p.e,p.sop,p.sup,p.de]),x.colocados.map(p=>[p.obj,p.e,p.sop,p.sup,p.de]),'identidades');
 assert.deepEqual(x.colocados.filter(p=>core.includes(p.obj)),e.colocados.filter(p=>core.includes(p.obj)),'núcleo');
 assert.deepEqual(a.estancias.filter(q=>q!==x),b.estancias.filter(q=>q!==e),'otras estancias');
 assert.deepEqual(a.inter.map(i=>[i.type,i.label,i.def]),b.inter.map(i=>[i.type,i.label,i.def]),'acciones y botín');
 if(!meta)assert.deepEqual(e.colocados,x.colocados,'fallback');
 const use=next.V.revisarUso(b);assert.equal(use.errores.length,0,JSON.stringify(use.errores));
 rows.push({seed,perfil:b.profile.id,aplicado:!!meta,metadata:meta??null,placed:e.colocados,frame:{W:e.W,D:e.D,H:e.H},libres:e.libres,inicio:e.inicio,zonas:e.zonas,origen:e.origen,seatsBefore:flat(a.pieces.seat),seatsAfter:flat(b.pieces.seat),actionsBefore:a.inter.filter(i=>i.sala===x.sala).map(flat),actionsAfter:b.inter.filter(i=>i.sala===e.sala).map(flat),use});
 console.log(seed,meta?'APLICADO '+meta.pared+' '+meta.movidos.length:'BASE');
}catch(err){rows.push({seed,error:String(err.stack||err)});console.log(seed,String(err));}finally{for(const h of[a,b])if(h)h.group.traverse(o=>{if(o.isMesh)o.geometry.dispose();});}}
for(const[p,h]of Object.entries(JSON.parse(fs.readFileSync('.cache/calidad/tanda17/estado_candidato.json')).archivos))assert.equal(crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex'),h,p);
fs.writeFileSync('.cache/calidad/tanda18/postpaso_r3/resultados.json',JSON.stringify({estado:'PRIVADO_R3_CPU',rows},null,2)+'\n');assert.equal(rows.filter(r=>r.error).length,0);fs.writeFileSync('.cache/calidad/tanda18/postpaso_r3/diagnostico.json',JSON.stringify(globalThis.__lecturaDebug??[],null,2)+'\n');assert(rows.some(r=>r.aplicado),'cero admisiones');
