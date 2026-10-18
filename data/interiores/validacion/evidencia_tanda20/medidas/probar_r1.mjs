import fs from 'node:fs';import assert from 'node:assert/strict';
import {runtime,overrides} from './runtime.cpu.mjs';
const prefix='.cache/calidad/tanda20/prototipo_r1/';
for(const f of ['src/houses.js','src/acabados_vivienda.js'])overrides.set(f,fs.readFileSync(prefix+f,'utf8'));
const base=runtime(false),cand=runtime(true,data=>{
 for(const o of JSON.parse(fs.readFileSync(prefix+'data/objetos/vivienda_b.json')).objetos)data.OBJETOS[o.id]=o;
 data.KITS.vivienda_dormitorio=JSON.parse(fs.readFileSync(prefix+'data/kits/vivienda_dormitorio.json'));
});
const B=JSON.parse(fs.readFileSync('data/quality_budgets.json')).interior;
const seeds=[...new Set([...JSON.parse(fs.readFileSync('data/interiores/validacion/casas_pueblo.json')).resultados.map(r=>r.seed),2786,3244,1689,2132,5157])];
const rows=[],errores=[];
for(const seed of seeds){const a=base.H.buildVecino(seed,{x:-5200,z:-5200}),h=cand.H.buildVecino(seed,{x:-5200,z:-5200});
 try{
  let meshes=0,tris=0;h.group.traverse(o=>{if(o.isMesh&&o.visible){meshes++;tris+=(o.geometry.index?.count||o.geometry.attributes.position.count)/3;}});
  const rooms=[];
  for(const e of h.estancias.filter(e=>e.kit==='vivienda_dormitorio')){
   const old=a.estancias.find(q=>q.sala===e.sala),rm=h.rooms.find(q=>q.id===e.sala);
   const before=a.inter.filter(i=>i.sala===e.sala).map(i=>i.type),after=h.inter.filter(i=>i.sala===e.sala).map(i=>i.type);
   const lost=before.filter((t,i)=>before.slice(0,i+1).filter(x=>x===t).length>after.filter(x=>x===t).length);
   const report=cand.V.revisar({local:e,group:{traverse(){}}},{interior:B}),usage=cand.V.revisarUso(h);
   const bs=old.colocados.filter(p=>['cama','cama_doble'].includes(base.data.OBJETOS[p.obj].rol)),cs=e.colocados.filter(p=>['cama','cama_doble'].includes(cand.data.OBJETOS[p.obj].rol));
   const result={tipo:rm.type,sala:e.sala,W:e.W,D:e.D,baseline_beds:bs.map(p=>p.obj),beds:cs.map(p=>p.obj),perdidas:lost,errores:report.errores,uso:usage.errores,placed:e.colocados,acciones:after};rooms.push(result);
   if(lost.length||report.errores.length||usage.errores.length||JSON.stringify(result.baseline_beds)!==JSON.stringify(result.beds))errores.push({seed,...result});
  }
  if(meshes>B.mallas_max||tris>B.triangulos_max||h.fallosKit.length)errores.push({seed,coste:{meshes,tris},limites:B,fallos:h.fallosKit});
  rows.push({seed,perfil:h.profile.id,meshes,tris,rooms});
 }finally{for(const q of[a,h])q.group.traverse(o=>{if(o.isMesh)o.geometry.dispose();});}
}
const models=['vb_cama_doble','vb_cama_individual','vb_cama_amplia'].map(id=>{const a=base.caja(id),b=cand.caja(id),keys=['x0','x1','y0','y1','z0','z1'];return{id,antes:a,despues:b,envolvente_igual:keys.every(k=>Math.abs(a[k]-b[k])<1e-6)};});
for(const m of models)if(!m.envolvente_igual)errores.push({modelo:m.id,envolvente:m});
fs.writeFileSync('.cache/calidad/tanda20/medidas/resultado_r1.json',JSON.stringify({estado:errores.length?'FAIL':'PASS',alcance:'CPU constructores/Three/colliders reales, Canvasstub sin raster/FPS; conserva cantidad/tipo camas y multiconjunto de acciones por sala.',rows,models,errores},null,2)+'\n');
console.log(JSON.stringify({casas:rows.length,habitaciones:rows.reduce((s,r)=>s+r.rooms.length,0),errores:errores.map(e=>({seed:e.seed,sala:e.sala,perdidas:e.perdidas,errores:e.errores,uso:e.uso,coste:e.coste,modelo:e.modelo})),max_mallas:Math.max(...rows.map(r=>r.meshes)),max_tris:Math.max(...rows.map(r=>r.tris)),envolventes:models.map(m=>[m.id,m.envolvente_igual])},null,2));
assert.equal(errores.length,0);
