import fs from 'node:fs';import assert from 'node:assert/strict';import crypto from 'node:crypto';import {runtime} from './runtime.cpu.mjs';
const root='.cache/calidad/cocina_t16/produccion_r1/',before=runtime(false),after=runtime(true),rows=[];
const inventory=h=>h.inter.filter(i=>i.type==='loot').map(i=>({id:i.id,def:i.def}));
const actions=(h,sala)=>h.inter.filter(i=>i.sala===sala).map(i=>({type:i.type,id:i.id,label:i.label,def:i.def}));
for(const seed of [2786,3244,1594]){
 const a=before.H.buildVecino(seed,{x:-5200,z:-5200}),b=after.H.buildVecino(seed,{x:-5200,z:-5200}),ea=a.estancias.find(e=>e.kit==='vivienda_cocina'),eb=b.estancias.find(e=>e.kit==='vivienda_cocina');
 const ia=inventory(a),ib=inventory(b);assert.deepEqual(ib,ia,'loot identity/value '+seed);
 const aa=actions(a,ea.sala),ab=actions(b,eb.sala);assert.deepEqual(ab,aa,'kitchen actions '+seed);
 const lootPose=h=>h.inter.filter(i=>i.type==='loot').map(i=>({id:i.id,x:i.x,y:i.y,z:i.z}));
 rows.push({seed,lootIDs:ib.map(i=>i.id),lootIdentityAndDefsExact:true,kitchenActionsExact:true,kitchenTypes:ab.map(i=>i.type),lootPosesExact:JSON.stringify(lootPose(a))===JSON.stringify(lootPose(b))});
 for(const h of [a,b])h.group.traverse(o=>{if(o.isMesh)o.geometry.dispose();});
}
const hashes=Object.fromEntries(['src/locales.js','src/houses.js','tools/interiores/validar.js','data/kits/vivienda_cocina.json','data/objetos/vivienda_a.json'].map(p=>[p,crypto.createHash('sha256').update(fs.readFileSync(root+'candidata/'+p)).digest('hex')]));
fs.writeFileSync(root+'revision_funciones_cpu.json',JSON.stringify({state:'PASS_PRELIMINARY_NOT_FROZEN',scope:'3 actual constructors CPU; Canvas stub, no action execution or persistence browser',hashes,rows},null,2)+'\n');console.log(JSON.stringify(rows,null,2));
