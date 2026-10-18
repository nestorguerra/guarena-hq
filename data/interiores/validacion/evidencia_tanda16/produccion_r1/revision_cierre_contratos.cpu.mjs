import fs from'node:fs';import assert from'node:assert/strict';
import{runtime,read,THREE,entry,sha}from'./runtime.cpu.mjs';
const root='.cache/calidad/cocina_t16/produccion_r1/',api=runtime(true),rows=[],{data:{KITS,OBJETOS},H,V,amueblar,buildLocal,filtroHogar,caja,construir,geo:{partes,penetra,espacioFrontal}}=api;
const exigir=(ok,s)=>assert(ok,s),tirar=h=>h.group.traverse(o=>{if(o.isMesh)o.geometry.dispose();}),caso=async(name,fn)=>{try{await fn();rows.push({name,pass:true});}catch(e){rows.push({name,pass:false,error:String(e.stack)});}};
const fetch=async()=>({json:async()=>JSON.parse(read('data/quality_budgets.json'))});
const source=read('tools/interiores/casas_pruebas.js',true),inc=fs.readFileSync(root+'contratos.inc','utf8');assert(source.includes(inc));const begin=source.indexOf("  if(opts.tanda>=9)await caso('los umbrales"),end=source.indexOf("  if(opts.tanda>=9)await caso('el puesto",begin);const contract=inc+source.slice(begin,end);
await new Function('opts','caso','exigir','tirar','fetch','H','KITS','OBJETOS','THREE','amueblar','buildLocal','filtroHogar','caja','partes','penetra','espacioFrontal','revisar','revisarUso','return(async()=>{'+contract+'})();')({tanda:19},caso,exigir,tirar,fetch,H,KITS,OBJETOS,THREE,amueblar,buildLocal,filtroHogar,caja,partes,penetra,espacioFrontal,V.revisar,V.revisarUso);
fs.writeFileSync(root+'revision_cierre_contratos_cpu.json',JSON.stringify({state:rows.every(r=>r.pass)?'PASS_CPU_NEW_CALLBACKS_LITERAL':'FAIL_PRESERVED',rows},null,2)+'\n');console.log(JSON.stringify(rows,null,2));assert(rows.every(r=>r.pass));
