import fs from 'node:fs';import assert from 'node:assert/strict';import crypto from 'node:crypto';
import {runtime,overrides} from '../postpaso_r3/runtime.cpu.mjs';
const folder='.cache/calidad/tanda18/postpaso_r3/',local=fs.readFileSync(folder+'locales.js','utf8'),helper=fs.readFileSync(folder+'composicion_lectura_salon.js','utf8');
const cfg=JSON.parse(fs.readFileSync(folder+'config.json'));overrides.set('src/locales.js',local);overrides.set('src/houses.js',fs.readFileSync(folder+'houses.js','utf8'));
const base=runtime(false),next=runtime(true,d=>d.KITS.vivienda_salon.composicion_lectura=cfg),h=base.H.buildVecino(3244,{x:-5200,z:-5200});
const e=h.estancias.find(e=>e.kit==='vivienda_salon');h.group.traverse(o=>{if(o.isMesh)o.geometry.dispose();});
const context=rt=>({W:e.W,D:e.D,H:e.H,inicio:e.inicio,libres:e.libres,funciones:true,perfil:e.hogar.perfil,filtro:x=>e.activas.includes(rt.data.KITS.vivienda_salon.objetos.indexOf(x))});
const a=base.amueblar(e.kit,e.seed,context(base)),b=next.amueblar(e.kit,e.seed,context(next));
assert(b.composicionLectura,'admisión no vacía');const ua=Array.from({length:12},()=>a.U([0,1])),ub=Array.from({length:12},()=>b.U([0,1]));assert.deepEqual(ua,ub);assert.equal(a.guardias,b.guardias);assert.deepEqual(a.activas,b.activas);assert.equal(b.K,next.data.KITS.vivienda_salon);assert.deepEqual(a.P.map(p=>[p.obj,p.e,p.sop,p.sup,p.de]),b.P.map(p=>[p.obj,p.e,p.sop,p.sup,p.de]));
const cb=local.slice(local.indexOf('aceptar:candidatos=>{')+'aceptar:'.length,local.indexOf('\n  }});',local.indexOf('aceptar:candidatos=>{'))+4);
const original=[{obj:'original',v:{cx:1}}],replacement=[{obj:'temporal'}];
const factory=new Function('P','cierra',`let guardias=7; const wrapped=()=>{guardias++;return cierra()};const callback=${cb.replace('cierra([])','wrapped()')};return {callback,get:()=>guardias};`);
let P=[...original],seen=false;const t=factory(P,()=>{seen=P[0]===replacement[0];throw Error('fallo_dirigido');});assert.throws(()=>t.callback(replacement),/fallo_dirigido/);assert(seen);assert.deepEqual(P,original);assert.equal(P[0],original[0]);assert.equal(t.get(),7);
const deps={...next.data,...next.geo,caja:next.caja},compose=new Function(...Object.keys(deps),helper.replace(/^import .*;\n/gm,'').replace('export function','function')+';return componerLectura;')(...Object.values(deps));
const roots=[a.P.findIndex(p=>cfg.biblioteca.includes(p.obj)),a.P.findIndex(p=>cfg.asiento.includes(p.obj)),a.P.findIndex(p=>cfg.mesita.includes(p.obj)),a.P.findIndex(p=>cfg.lampara.includes(p.obj))];assert(roots.every(i=>i>=0));
const child=a.P.findIndex(p=>p.sop===roots[0]);assert(child>=0);const chosen=[...roots,child],Q=chosen.map((ix,i)=>({...a.P[ix],sop:i===4?0:null,de:null}));
// Una fixture de giro, con las piezas reales y sin obstáculos ajenos. No es otra casa ni otro barrido.
const originalLibrary=a.P[roots[0]],old=Q[0],delta=-old.ry;
for(const i of [0,4]){const p=Q[i],[x,z]=next.geo.rot(p.x-originalLibrary.x,p.z-originalLibrary.z,delta);p.x=x;p.z=.3+z;p.ry+=delta;}
const room={W:9,D:9,zonas:{estancia:{id:'estancia',x0:-4.5,x1:4.5,z0:0,z1:9,publica:true}},tabiques:[]};Q.forEach(p=>p.zona='estancia');
const before=JSON.stringify(Q);const rotated=compose({P:Q,K:{...b.K,composicion_lectura:{...cfg,paredes:['E']}},ctx:{funciones:true,perfil:e.hogar.perfil},planta:room,H:2.95,libres:[],inicio:{x:0,z:7},aceptar:R=>Math.abs(Math.sin(R[0].ry-Q[0].ry))>.99});
assert(rotated,'giro90 admitido');assert.equal(before,JSON.stringify(Q));const rel=(p,parent)=>{const [x,z]=next.geo.rot(p.x-parent.x,p.z-parent.z,-parent.ry);return[x,z,p.y-parent.y,p.ry-parent.ry];};
const ra=rel(Q[4],Q[0]),rb=rel(rotated.P[4],rotated.P[0]);assert(ra.every((x,i)=>Math.abs(x-rb[i])<1e-10));assert.equal(rotated.P[4].sop,0);assert.equal(rotated.P[4].sup,Q[4].sup);
const output={state:'PASS',scope:'CPU dirigido: un amueblar real de3244 y fixture9x9 de giro con piezas reales; noGPU ni barrido.',sourceHashes:{helper:crypto.createHash('sha256').update(helper).digest('hex'),locales:crypto.createHash('sha256').update(local).digest('hex')},rng:{seed:e.seed,admitted:b.composicionLectura.pared,next12Equal:true,KIdentity:true,guardiasEqual:true,indicesEqual:true},exception:{literalCallback:true,temporaryPSeen:seen,PAndReferencesRestored:true,guardiasRestored:true},rotation:{wall:rotated.metadata.pared,quarterTurn:true,relativeBefore:ra,relativeAfter:rb,indicesPreserved:true,originalUnmutated:true}};
fs.writeFileSync('.cache/calidad/tanda18/revision_r3/atomicidad_rng_giro.json',JSON.stringify(output,null,2)+'\n');console.log(JSON.stringify(output));
