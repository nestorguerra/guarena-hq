import fs from'node:fs';import assert from'node:assert/strict';
import{runtime as runtimeR1}from'../produccion_r1/runtime.cpu.mjs';import{runtime,sha}from'./runtime.cpu.mjs';
const root='.cache/calidad/cocina_t16/artistica_r2/',A=runtimeR1(true),B=runtime(true),O=B.data.OBJETOS,EPS=1e-6;
const changed=Object.keys(O).filter(id=>JSON.stringify(O[id])!==JSON.stringify(A.data.OBJETOS[id]));assert.deepEqual(changed.sort(),['va_banda_vajillero','va_banda_vajillero_amplio','va_preparar_pan'].sort());
const rows=[],internal=[];
for(const id of changed){
 const o=O[id],P=B.geo.partes({obj:id,x:0,y:0,z:0,ry:0});
 for(let i=0;i<P.length;i++)for(let j=i+1;j<P.length;j++)assert(B.geo.penetra(P[i],P[j])<=EPS,id+' solape '+i+'/'+j);
 const supported=[];o.partes.forEach((p,i)=>{if(!(id==='va_preparar_pan'||['comida','ceramica'].includes(p.m))||P[i].y0<EPS)return;const v=P[i];
 const support=P.findIndex((a,j)=>j!==i&&Math.abs(a.y1-v.y0)<EPS&&[-1,1].every(sx=>[-1,1].every(sz=>{const[dx,dz]=B.geo.rot(sx*v.hw,sz*v.hd,v.a),[x,z]=B.geo.rot(v.cx+dx-a.cx,v.cz+dz-a.cz,-a.a);return Math.abs(x)<=a.hw+EPS&&Math.abs(z)<=a.hd+EPS;})));
 assert(support>=0,id+' sin apoyo '+i);supported.push({part:i,on:support});});
 // Las tres incisiones están realmente sobre la zona plana del pan redondeado.
 if(id==='va_preparar_pan')for(const i of[2,3,4]){const p=P[i],loaf=o.partes[1];for(const sx of[-1,1])for(const sz of[-1,1]){const[dx,dz]=B.geo.rot(sx*p.hw,sz*p.hd,p.a);assert(Math.abs(p.cx+dx-loaf.p[0])<=loaf.d[0]/2-loaf.redondeo+EPS);assert(Math.abs(p.cz+dz-loaf.p[2])<=loaf.d[2]/2-loaf.redondeo+EPS);}}
 for(const k of['rol','masa','clase','soporte','superficies'])assert.deepEqual(o[k],A.data.OBJETOS[id][k]);
 const a=A.caja(id),b=B.caja(id);for(const k of['x0','x1','y0','y1','z0','z1'])assert(Math.abs(a[k]-b[k])<=EPS,id+' envolvente '+k);
 internal.push({id,parts:P.length,supported,penetrations:0,bboxBefore:a,bboxAfter:b});
}
const count=h=>{let meshes=0,triangles=0;const materials=new Set();h.group.traverse(o=>{if(o.isMesh&&o.visible){meshes++;triangles+=(o.geometry.index?.count||o.geometry.attributes.position.count)/3;materials.add(o.material);}});return{meshes,triangles,materials:materials.size,lights:h.lights.length};};
for(const seed of[2786,3244,1594]){
 const a=A.H.buildVecino(seed),b=B.H.buildVecino(seed),ea=a.estancias.find(e=>e.kit==='vivienda_cocina'),eb=b.estancias.find(e=>e.kit==='vivienda_cocina');
 const pose=C=>C.map(({v,...p})=>p);assert.deepEqual(pose(ea.colocados),pose(eb.colocados));assert.deepEqual(ea.entradasEfectivas,eb.entradasEfectivas);assert.deepEqual(a.lights.map(l=>[l.position.toArray(),l.intensity,l.color.toArray(),l.distance]),b.lights.map(l=>[l.position.toArray(),l.intensity,l.color.toArray(),l.distance]));
 const ca=count(a),cb=count(b);assert(cb.meshes<=60);assert.equal(cb.meshes,ca.meshes);assert.equal(cb.materials,ca.materials);assert.equal(cb.lights,ca.lights);
 const budget=JSON.parse(fs.readFileSync('.cache/calidad/cocina_t16/produccion_r1/base/data/quality_budgets.json')),local=B.V.revisar({local:eb,group:{traverse(){}}},budget),use=B.V.revisarUso(b);assert.deepEqual(local.errores,[]);assert.deepEqual(use.errores,[]);
 rows.push({seed,beforeR1:ca,afterR2:cb,posesAndReferencesUnchanged:true,rolesAndRecipesUnchanged:true,lightsUnchanged:true,localErrors:local.errores,useErrors:use.errores});for(const h of[a,b])h.group.traverse(o=>{if(o.isMesh)o.geometry.dispose();});
}
for(const f of['src/locales.js','src/houses.js','tools/interiores/validar.js','tools/interiores/kits_vivienda_a.py'])assert.equal(sha(fs.readFileSync(root+'candidata/'+f)),sha(fs.readFileSync('.cache/calidad/cocina_t16/produccion_r1/candidata/'+f)),'motor/receta alterados '+f);
fs.writeFileSync(root+'cpu.json',JSON.stringify({state:'PASS_AFFECTED_MODELS_CPU_NOT_VISUAL',scope:'Only3model deltas; actual3canonical full constructors/batching/validators; no GPU, no rerun22, no game publication',changed,internal,rows},null,2)+'\n');console.log(JSON.stringify({state:'PASS',changed,rows},null,2));
