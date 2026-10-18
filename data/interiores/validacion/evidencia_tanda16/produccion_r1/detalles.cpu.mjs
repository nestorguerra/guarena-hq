import fs from'node:fs';import assert from'node:assert/strict';
import{runtime,read,sha,entry}from'./runtime.cpu.mjs';import{fixture}from'./fixture.cpu.mjs';
const root='.cache/calidad/cocina_t16/produccion_r1/',A=runtime(false),B=runtime(true),O=B.data.OBJETOS,checks=[];
const pass=(name,data)=>checks.push({name,pass:true,...data});
const q=o=>JSON.parse(JSON.stringify(o,(k,v)=>typeof v==='function'?undefined:v));
const core=['va_encimera','va_encimera_amplia','va_cocina','va_cocina_amplia'];
for(const v of B.data.KITS.vivienda_cocina.composicion_cocina.versiones)for(const[id,key]of core.map((id,i)=>[id,['preparacion','preparacion_amplia','cocina','cocina_amplia'][i]])){
 const a=A.data.OBJETOS[id],b=O[v[key]],strip=p=>p.map(({c,tinte,...rest})=>rest);assert.deepEqual(strip(b.partes),strip(a.partes));for(const k of['rol','masa','clase','soporte','superficies'])assert.deepEqual(b[k],a[k]);assert.deepEqual(B.caja(b.id),A.caja(a.id));
}pass('12 frentes conservan geometria/funcion/superficies exactas');
function compounds(objects){
 const errors=[];
 for(const o of objects){
  const model=o.partes.map((p,i)=>{const id='__pieza_'+i;const data={...o,id,partes:[p]},prior=O[id];O[id]=data;
   // partes() utiliza el catálogo cerrado de este runtime, con objeto nuevo real.
   const v=B.geo.partes({obj:id,x:0,y:0,z:0,ry:0})[0];if(prior)O[id]=prior;else delete O[id];return v;});
  for(let i=0;i<model.length;i++)for(let j=i+1;j<model.length;j++)if(B.geo.penetra(model[i],model[j])>.001)errors.push({id:o.id,tipo:'penetracion',i,j,depth:B.geo.penetra(model[i],model[j])});
  // Contenido apoyado: sólo subpiezas de comida/cerámica. Puertas/bastidores son uniones laterales.
  o.partes.forEach((p,i)=>{if(!['ceramica','comida'].includes(p.m))return;const v=model[i];if(v.y0<.001)return;
   const apoyo=model.some((a,j)=>j!==i&&Math.abs(a.y1-v.y0)<1e-6&&a.cx-a.hw<=v.cx-v.hw+1e-6&&a.cx+a.hw>=v.cx+v.hw-1e-6&&a.cz-a.hd<=v.cz-v.hd+1e-6&&a.cz+a.hd>=v.cz+v.hd-1e-6);
   if(!apoyo)errors.push({id:o.id,tipo:'sin_apoyo',i,bottom:v.y0});
  });
 }
 return errors;
}
const modeled=Object.values(O).filter(o=>/^va_(guardar_|banda_|preparar_pan)/.test(o.id));let errs=compounds(modeled);fs.writeFileSync(root+'geometria_interna.json',JSON.stringify(errs,null,2)+'\n');assert.deepEqual(errs,[]);pass('13 compuestos nuevos sin interpenetraciones >1mm; ceramica/pan con apoyo completo');
const floating=structuredClone(O.va_preparar_pan);floating.partes[1].p[1]+=.036;assert(compounds([floating]).some(e=>e.tipo==='sin_apoyo'));pass('negativo hogaza flotante3.6cm detectada');
const overlap=structuredClone(O.va_guardar_liso);overlap.partes.at(-1).p[0]=overlap.partes.at(-2).p[0];assert(compounds([overlap]).some(e=>e.tipo==='penetracion'));pass('negativo taza dentro de pila detectado');
let nonOpt=0;for(const id of Object.keys(A.data.KITS).filter(k=>k!=='vivienda_cocina')){
 const a=A.amueblar(id,1),b=B.amueblar(id,1);assert.deepEqual(q(a),q(b),id);assert.equal(a.U([0,1]),b.U([0,1]),id+' U');nonOpt++;
}pass('consumidores no optantes invariantes resultado completo y siguienteU',{count:nonOpt});
const rows=JSON.parse(fs.readFileSync(root+'cpu.json')).rows;
for(const row of rows){
 const f=fixture(row.seed)[0];
 // La comprobacion exacta usa las colocaciones literales finales ya registradas.
 const P=row.items;
 if(!row.accepted)continue;
 const compoundObjects=P.filter(p=>p.obj.startsWith('va_guardar_')||p.obj.startsWith('va_banda_')||p.obj==='va_preparar_pan');
 for(const p of compoundObjects){for(const sx of[-1,1])for(const sz of[-1,1]){const[dx,dz]=B.geo.rot(sx*p.v.hw,sz*p.v.hd,p.ry);assert(p.v.cx+dx>=-row.W/2-1e-6&&p.v.cx+dx<=row.W/2+1e-6&&p.v.cz+dz>=-1e-6&&p.v.cz+dz<=row.D+1e-6,'limites estrictos '+row.seed);}
 for(const l of f.ctx.libres)for(const v of B.geo.partes(p))assert(B.geo.penetra(l,v)<=.005,'hueco '+row.seed);}
 const prep=P.find(p=>p.obj.startsWith('va_encimera_')),fridge=P.find(p=>p.obj==='va_nevera'),pantry=P.find(p=>p.obj.startsWith('va_guardar_'));
 for(const[p,width]of[[prep,Math.min(.8,B.caja(prep.obj).w-.05)],[fridge,.7],[pantry,Math.min(.7,B.caja(pantry.obj).w)]]){
 const R=B.geo.espacioFrontal(p,B.caja(p.obj),[width,.8]);
 for(const sx of[-1,1])for(const sz of[-1,1]){const[dx,dz]=B.geo.rot(sx*R.hw,sz*R.hd,R.a);assert(R.cx+dx>=-row.W/2-1e-6&&R.cx+dx<=row.W/2+1e-6&&R.cz+dz>=-1e-6&&R.cz+dz<=row.D+1e-6,'frente0.8 '+row.seed);}
 for(const z of P)if(z!==p&&z.obj!=='va_preparar_pan')for(const v of B.geo.partes(z))assert(B.geo.penetra(R,v)<=.005,'frente bloqueado '+row.seed);
 }
}
pass('18 composiciones: limites/huecos exactos y frente0.8m libres');
const four=rows.filter(r=>!r.accepted).map(r=>r.seed);assert.deepEqual(four,[3627,2606,4007,4216]);pass('4 fallbacks exactos conservados',{seeds:four});
for(const p of['src/locales.js','src/houses.js','src/acabados_vivienda.js'])assert.equal(sha(fs.readFileSync(p)),entry.sha256[p],'activo modificado '+p);
fs.writeFileSync(root+'detalles.json',JSON.stringify({state:'PASS_CPU',scope:'Source literal; no GPU, no visual approval',checks},null,2)+'\n');console.log(JSON.stringify(checks,null,2));
