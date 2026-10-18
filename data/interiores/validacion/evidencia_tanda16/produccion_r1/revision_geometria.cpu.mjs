import fs from'node:fs';import assert from'node:assert/strict';import {runtime} from './runtime.cpu.mjs';
const a=runtime(true),b=runtime(false),ids=Object.keys(a.data.OBJETOS).filter(x=>/^va_(guardar_|banda_|preparar_pan)/.test(x)),rows=[];assert.equal(ids.length,13);
for(const id of ids){const o=a.data.OBJETOS[id],ps=a.geo.partes({obj:id,x:0,y:0,z:0,ry:0});let contents=0;
 for(let i=0;i<ps.length;i++){for(let j=i+1;j<ps.length;j++)assert(a.geo.penetra(ps[i],ps[j])<=1e-6,id+' overlap '+i+'/'+j);
 if(['ceramica','comida'].includes(o.partes[i].m)){contents++;const v=ps[i];assert(ps.some((q,j)=>j!==i&&Math.abs(q.y1-v.y0)<1e-6&&q.cx-q.hw<=v.cx-v.hw+1e-6&&q.cx+q.hw>=v.cx+v.hw-1e-6&&q.cz-q.hd<=v.cz-v.hd+1e-6&&q.cz+q.hd>=v.cz+v.hd-1e-6),id+' floating '+i);}}
 rows.push({id,parts:ps.length,contents,bounds:a.caja(id)});
}
const variants=[];for(const base of ['va_cocina','va_cocina_amplia','va_encimera','va_encimera_amplia'])for(const suffix of ['rustico','liso','vajillero']){const o=a.data.OBJETOS[base+'_'+suffix],original=b.data.OBJETOS[base],strip=ps=>ps.map(({c,tinte,...p})=>p);assert.deepEqual(strip(o.partes),strip(original.partes));assert.deepEqual(a.caja(o.id),b.caja(base));for(const k of ['rol','superficies','clase','masa','soporte'])assert.deepEqual(o[k],original[k]);variants.push(o.id);}
fs.writeFileSync('.cache/calidad/cocina_t16/produccion_r1/revision_geometria_cpu.json',JSON.stringify({state:'PASS_GEOMETRY_ONLY',rows,variants},null,2)+'\n');console.log('PASS',rows.length,'compound models',variants.length,'variants');
