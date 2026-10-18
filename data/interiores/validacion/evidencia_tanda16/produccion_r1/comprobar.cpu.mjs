import fs from'node:fs';import assert from'node:assert/strict';
import{runtime,read,sha,entry,THREE}from'./runtime.cpu.mjs';import{fixture}from'./fixture.cpu.mjs';
const root='.cache/calidad/cocina_t16/produccion_r1/',before=runtime(false),after=runtime(true),rows=[],B=JSON.parse(read('data/quality_budgets.json')).interior;
const count=h=>{let meshes=0,triangles=0;const materials=new Set();h.group.traverse(o=>{if(o.isMesh&&o.visible){meshes++;triangles+=(o.geometry.index?.count||o.geometry.attributes.position.count)/3;materials.add(o.material);}});return{meshes,triangles,materials:materials.size,lights:h.lights.length};};
const src=read('src/interiors.js'),methods=src.slice(src.indexOf('  hideIn(it) {'),src.indexOf('  // the Guardia Civil comes in after you'));
const css=new Set(),document={body:{classList:{add:v=>css.add(v),remove:v=>css.delete(v)}}},Wardrobe=new Function('document','return class {'+methods+'};')(document);
function free(api,h,p,e){
 const col=h.levels?h.levels[p.y>h.split?1:0]:h.collider,q=p.clone(),hit=col.resolveCircle(q,.34),moved=Math.hypot(q.x-p.x,q.z-p.z);
 const occupied=e.colocados.filter(v=>v.sop==null&&!['pared','techo'].includes(v.regla)&&api.data.OBJETOS[v.obj].clase!=='PICKUP'&&api.caja(v.obj).h>=.3).some(v=>{const b=api.caja(v.obj),[dx,dz]=api.geo.rot(p.x-e.origen.x-v.x,p.z-e.origen.z-v.z,-v.ry);return dx>b.x0+1e-6&&dx<b.x1-1e-6&&dz>b.z0+1e-6&&dz<b.z1-1e-6;});
 return {moved,depth:hit.depth,occupied,pass:moved<=1e-6&&hit.depth<=1e-6&&!occupied};
}
function hide(api,h,e){
 const records=[];for(const it of h.inter.filter(i=>i.type==='hide'&&i.sala===e.sala)){
 const p={pos:new THREE.Vector3(it.x,e.origen.y,it.z),hidden:false},owner=new Wardrobe();owner.game={player:p,cam:{setFirstPerson(){}},audio:{sfx(){}}};
 const entry=free(api,h,p.pos,e);owner.hideIn(it);assert.deepEqual(p.pos.toArray(),[it.hx,e.origen.y,it.hz]);assert(p.hidden);owner.unhide();const exit=free(api,h,p.pos,e);assert(!p.hidden);records.push({entry,exit,pass:entry.pass&&exit.pass});}return records;
}
const dispose=h=>h.group.traverse(o=>{if(o.isMesh)o.geometry.dispose();});
const ids=['va_cocina','va_cocina_amplia','va_encimera','va_encimera_amplia','va_nevera','va_lavadora','mesa_camilla','va_mesa_comedor','silla_comedor'];
const identity=o=>[...ids].sort((a,b)=>b.length-a.length).find(id=>o===id||o.startsWith(id+'_'))||o;
const pose=C=>C.filter(p=>ids.includes(identity(p.obj))).map(({obj,x,y,z,ry})=>({obj:identity(obj),x,y,z,ry}));
for(const seed of JSON.parse(read('data/interiores/validacion/casas_pueblo.json')).resultados.map(r=>r.seed)){
 const ha=before.H.buildVecino(seed,{x:-5200,z:-5200}),hb=after.H.buildVecino(seed,{x:-5200,z:-5200}),A=count(ha),C=count(hb),ea=ha.estancias.find(e=>e.kit==='vivienda_cocina'),eb=hb.estancias.find(e=>e.kit==='vivienda_cocina');
 const f=fixture(seed)[0],a=before.amueblar('vivienda_cocina',ea.seed,f.ctx),b=after.amueblar('vivienda_cocina',eb.seed,f.ctx);
 assert.deepEqual(pose(eb.colocados),pose(ea.colocados),'pose nucleo/mesa '+seed);
 assert.deepEqual(hb.loot.map(({mesh,...o})=>o),ha.loot.map(({mesh,...o})=>o),'botin IDs/defs '+seed);
 const actions=h=>h.inter.filter(i=>i.sala===eb.sala&&['eat','fridge','hide'].includes(i.type)).map(i=>i.type).sort();assert.deepEqual(actions(hb),actions(ha),'acciones cocina '+seed);
 assert.deepEqual(b.P.map(p=>({obj:p.obj,x:p.x,y:p.y||0,z:p.z,ry:p.ry})),eb.colocados.map(p=>({obj:p.obj,x:p.x,y:p.y||0,z:p.z,ry:p.ry})),'fixture y constructor literal difieren '+seed);
 assert.equal(a.U([0,1]),b.U([0,1]),'RNG amueblar '+seed);
 let indexOK=true;for(const[i,p]of b.P.entries()){
  assert(b.K.objetos[p.e],'e ausente');for(const k of['sop','de'])if(p[k]!=null)assert(Number.isInteger(p[k])&&p[k]>=0&&p[k]<b.P.length&&p[k]!==i,k+' invalido '+seed);
  if(p.sop!=null){const o=after.data.OBJETOS[b.P[p.sop].obj];assert(o.superficies?.[p.sup],'sup ausente');}
 }
 for(const e of hb.estancias.filter(e=>e.kit!=='vivienda_cocina'))assert.deepEqual(e,ha.estancias.find(q=>q.sala===e.sala),'otra estancia '+seed);
 assert.deepEqual(hb.lights.map(l=>[l.position.toArray(),l.intensity,l.color.toArray(),l.distance]),ha.lights.map(l=>[l.position.toArray(),l.intensity,l.color.toArray(),l.distance]),'luces '+seed);
 const hideBefore=hide(before,ha,ea),hideAfter=hide(after,hb,eb);
 const local=after.V.revisar({local:eb,group:{traverse(){}}},{interior:B}),uso=after.V.revisarUso(hb),changed=!!b.composicionCocina;
 if(!changed){assert.deepEqual(b.P,a.P,'fallback P '+seed);assert.deepEqual(b.activas,a.activas);assert.equal(b.guardias,a.guardias);assert.deepEqual(C,A,'fallback geometria '+seed);}
 const row={seed,style:f.estilo,W:b.W,D:b.D,accepted:changed,mode:b.composicionCocina?.modo||'base_exacta',before:A,after:C,coreTableUnchanged:true,lootUnchanged:true,actionTypesUnchanged:true,otherRoomsUnchanged:true,lightsUnchanged:true,rngUnchanged:true,indexOK,localErrors:local.errores,useErrors:uso.errores,hideBefore,hideAfter,budget:C.meshes<=60&&C.triangles<=B.triangulos_max&&C.lights<=B.luces_max,composition:b.composicionCocina,items:b.P.map(p=>({...p,caja:after.caja(p.obj),role:after.data.OBJETOS[p.obj].rol}))};rows.push(row);dispose(ha);dispose(hb);
 fs.writeFileSync(root+'cpu.json',JSON.stringify({state:'IN_PROGRESS_PRESERVING_ROWS',rows},null,2)+'\n');
}
const report={state:rows.every(r=>r.budget&&!r.localErrors.length&&!r.useErrors.length)?'PASS_LITERAL_FINAL_SOURCE_CPU_NOT_VISUAL':'FAIL_PRESERVED',scope:'Raw final candidate JSON and literal production amueblar/buildVecino/constructor/validator. No furnishing wrapper, no dimensions changed, no pixels rasterized. Mesh budget actual merged geometry. Source snapshots private; no product writes.',baseHead:entry.head,rows};
fs.writeFileSync(root+'cpu.json',JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({state:report.state,accepted:rows.filter(r=>r.accepted).length,maxMeshes:Math.max(...rows.map(r=>r.after.meshes)),fallbacks:rows.filter(r=>!r.accepted).map(r=>r.seed),errors:rows.filter(r=>r.localErrors.length||r.useErrors.length||!r.budget).map(r=>({seed:r.seed,local:r.localErrors,use:r.useErrors,budget:r.budget})),canonical:rows.filter(r=>[2786,3244,1594].includes(r.seed)).map(r=>({seed:r.seed,mode:r.mode,before:r.before,after:r.after}))},null,2));
