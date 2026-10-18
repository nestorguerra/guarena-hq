import fs from'node:fs';import assert from'node:assert/strict';import{runtime,read}from'./runtime.cpu.mjs';import{fixture}from'./fixture.cpu.mjs';
const root='.cache/calidad/cocina_t16/produccion_r1/',api=runtime(true),{ctx,seed}=fixture(2786)[0],K=api.data.KITS.vivienda_cocina,cfg=K.composicion_cocina;
const C=api.amueblar('vivienda_cocina',seed,ctx);assert(C.composicionCocina);
const removed=C.composicionCocina.retirados.find(p=>p.sop!=null),e=K.objetos[removed.e];assert(e);
const rows=[];
for(const kind of ['interaccion','vende']){
 const old=e[kind];e[kind]=kind==='interaccion'?{type:'read',label:'Prueba dirigida de función'}:'agua';
 try{
  delete K.composicion_cocina;const a=api.buildLocal('vivienda_cocina',seed,{x:0,z:0},'dirigida',null,ctx);K.composicion_cocina=cfg;const b=api.buildLocal('vivienda_cocina',seed,{x:0,z:0},'dirigida',null,ctx);
  const type=kind==='interaccion'?'read':'buy',before=a.inter.filter(x=>x.type===type).length,after=b.inter.filter(x=>x.type===type).length;
  rows.push({kind,entry:removed.e,seed,baseActions:before,composedActions:after,composition:!!b.local.composicionCocina});
  for(const h of[a,b])h.group.traverse(o=>{if(o.isMesh)o.geometry.dispose();});
 }finally{if(old===undefined)delete e[kind];else e[kind]=old;K.composicion_cocina=cfg;}
}
for(const row of rows){assert.ok(row.baseActions>0);assert.equal(row.composedActions,row.baseActions);assert.equal(row.composition,false);}
fs.writeFileSync(root+'revision_cierre_funciones_cpu.json',JSON.stringify({state:rows.some(x=>x.baseActions>x.composedActions)?'P2_FUNCTIONAL_ENTRY_REMOVED':'PASS',rows},null,2)+'\n');console.log(JSON.stringify(rows,null,2));
