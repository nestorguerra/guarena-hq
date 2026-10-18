import fs from'node:fs';import assert from'node:assert/strict';
import{runtime,read,THREE,sha}from'./runtime.cpu.mjs';
const root='.cache/calidad/cocina_t16/produccion_r1/',old=read('tools/interiores/fotos_casa.py'),now=read('tools/interiores/fotos_casa.py',true),predicate="['va_encimera','va_encimera_amplia'].includes(p.obj.replace(/_(rustico|liso|vajillero)$/,''))",prior="['va_encimera','va_encimera_amplia'].includes(p.obj)";
assert.equal(now.replace(predicate,prior),old,'delta de capturador excede selector de identidad');
const api=runtime(false),after=runtime(true),O=api.data.OBJETOS;
function selector(src){
 const helper=src.slice(src.indexOf('  function cameraClearance'),src.indexOf('  // End physical clearance helpers.'));
 const a=src.indexOf('    for (const [k, f]'),b=src.indexOf('      for (let i = 0; i < 3; i++) g.frame',a),body=src.slice(a,b);
 return new Function('THREE','caja','OBJETOS',helper+';return function(h,rm,s){const tipo="cocina",y=rm.lv?3.1:0,vistas=[];'+body+'vistas.push({x,y:y+1.6,z,fov,objetivo:[cx,y+alturaObjetivo,cz],objetivos:objetivos.map(p=>p.obj),clearance:clearanceElegido});}return vistas;};')(THREE,api.caja,O);
}
const a=selector(old),b=selector(now),rows=[];
for(const seed of[2786,3244,1594]){
 const h=api.H.buildVecino(seed,{x:-9700,z:-9700});try{const rm=h.rooms.find(r=>r.type==='cocina'),before=a(h,rm,seed),candidate=b(h,rm,seed);assert.deepEqual(candidate,before,'pose BASE cambia '+seed);rows.push({seed,sixBasePosesPreserved:true,poses:before});}finally{h.group.traverse(o=>{if(o.isMesh)o.geometry.dispose();});}
}
const check=new Function('p','return '+predicate),inputs=['va_encimera','va_encimera_amplia',...after.data.KITS.vivienda_cocina.composicion_cocina.versiones.flatMap(v=>[v.preparacion,v.preparacion_amplia])];
for(const id of inputs)assert(check({obj:id}),id);
for(const id of['va_mesa_comedor','mesa_camilla','va_isla_cocina','va_cocina_rustico','vb_mesa_despacho_0','va_encimera_falsa','va_encimera_amplia_falsa','va_encimera_rustico_rustico'])assert(!check({obj:id}),id);
fs.writeFileSync(root+'capturador.json',JSON.stringify({state:'PASS_CPU_SELECTOR_AND_BASE_POSES_NO_BROWSER',old_sha256:sha(old),candidate_sha256:sha(now),delta:'one identity predicate only; full CPU camera search reused literally, with actual baseline geometry/collider, no GPU/render; future candidate may select different poses because geometry changed',recognizedPreparations:inputs,rows},null,2)+'\n');console.log(JSON.stringify({state:'PASS',basePoses:6,recognizedPreparations:inputs}));
