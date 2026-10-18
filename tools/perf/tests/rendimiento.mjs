import assert from 'node:assert/strict';
import { machineHints, initialProfile, automaticQuality, pixelBudget, QualityController } from '../../../src/rendimiento.js';
let checks = 0;
function test(name, fn) { fn(); console.log('OK', name); checks++; }
const hint = (cores, ram, gpu = null) => machineHints({hardwareConcurrency: cores, deviceMemory: ram});
const run = (c, dt, seconds, work = 4) => { const changes = []; for(let t=0;t<seconds;t+=dt) { const x=c.observe(dt,work); if(x)changes.push(x); } return changes; };
test('Ausencia de datos no inventa memoria/CPU/GPU y elige media', () => {
 const h=machineHints({}); assert.equal(h.memoryGiBApprox,null); assert.equal(h.logicalCores,null); assert.equal(h.gpu,null); assert.equal(initialProfile(h).quality,'media');
});
test('La privacidad WebGL no bloquea el inicio', () => { assert.doesNotThrow(()=>machineHints({}, {getExtension(){throw Error('oculto');}})); });
test('Perfil acotado por memoria y GPU software', () => {
 assert.equal(initialProfile(hint(16,4)).quality,'baja'); assert.equal(initialProfile({...hint(16,16),gpu:'SwiftShader'}).quality,'baja'); assert.equal(initialProfile(hint(8,16)).quality,'alta');
});
test('Retina/4K respeta presupuesto de píxeles', () => {
 const p=initialProfile(hint(8,16));const d=pixelBudget(3840,2160,2,p);assert.ok(3840*2160*d*d<=p.maxPixels+1); assert.ok(pixelBudget(1280,720,1,p)<=1);
});
test('Calidad antigua manual y elección explícita automática', () => {
 assert.equal(automaticQuality({quality:'alta'}),false);assert.equal(automaticQuality({quality:'alta',qualityMode:'auto'}),true);assert.equal(automaticQuality({}),true);
});
test('120ms/fotograma sigue adaptando: regresión del corte a100ms', () => {
 const c=new QualityController(1.5);const changes=run(c,.12,20);assert.ok(changes.some(x=>x.pr<1.5));assert.ok(c.pr>=c.floor);
});
test('Un tirón aislado y la pestaña oculta no degradan', () => {
 const c=new QualityController(1.5);run(c,1/60,8);c.observe(.2);run(c,1/60,4);assert.equal(c.pr,1.5);for(let n=0;n<30;n++)c.observe(.5,1,false);assert.equal(c.pr,1.5);assert.ok(c.grace>=3);
});
test('Volver después de60s no contamina las medidas', () => {
 const c=new QualityController(1.5);c.observe(60);run(c,1/60,8);assert.equal(c.pr,1.5);assert.equal(c.level,0);
});
test('La reducción tiene límite y alcanza efectos si sigue lento', () => {
 const c=new QualityController(1.2);for(let t=0;t<100;){const dt=.28*(c.pr/1.2)**2;t+=dt;c.observe(dt,4);}assert.equal(c.pr,c.floor);assert.equal(c.level,2);
});
test('En manual no cambia los efectos y recupera resolución despacio', () => {
 const c=new QualityController(1,{effects:false});for(let t=0;t<60;){const dt=.18*c.pr*c.pr;t+=dt;c.observe(dt,4);}assert.equal(c.level,0);const low=c.pr;run(c,1/60,35);assert.ok(c.pr>low);assert.ok(c.pr<=1);
});
test('Un intervalo rápido no produce oscilación', () => {
 const c=new QualityController(1);run(c,.08,12);const low=c.pr;run(c,1/60,4);assert.ok(c.pr<=low, "cuatro segundos rápidos no bastan para subir y volver a bajar");
});
test('Reducir píxeles sin ganar fluidez se deshace, también con CPU saturada', () => {
 const c=new QualityController(1.5);run(c,.08,18,80);assert.equal(c.pr,1.5);assert.equal(c.level,0);assert.ok(c.pixelHold>0);
});
test('Resize recalcula techo, suelo y gracia para4K', () => {
 const p=initialProfile(hint(8,16)),c=new QualityController(pixelBudget(1280,720,2,p));
 c.resize(pixelBudget(3840,2160,2,p));assert.ok(c.pr*c.pr*3840*2160<=p.maxPixels+1);assert.ok(c.floor<=c.pr);assert.ok(c.grace>=3);
});
test('Lentitud sostenida inferior a1fps se mide; un tirón aislado no', () => {
 const c=new QualityController(1.5);assert.ok(run(c,1.2,90).some(x=>x.pr<1.5));
 const mixed=new QualityController(1.5),changes=[];
 for(let n=0;n<90;n++){const x=mixed.observe(n%2?.8:1.2);if(x)changes.push(x);}
 assert.ok(changes.some(x=>x.pr<1.5));
});
test('Datos incompletos permiten explorar nitidez sin superar presupuesto', () => {
 const p=initialProfile(machineHints({hardwareConcurrency:12}));
 const base=pixelBudget(1440,900,2,p),ceiling=pixelBudget(1440,900,2,{...p,maxDpr:p.exploreDpr});
 const c=new QualityController(base,{ceiling});run(c,1/60,100);assert.ok(c.pr>base);assert.ok(c.pr<=ceiling);assert.ok(c.pr*c.pr*1440*900<=p.maxPixels+1);
});
test('Una promoción que pierde fluidez se revierte sin insistir', () => {
 const c=new QualityController(1,{ceiling:1.4});
 for(let t=0;t<45;){const dt=c.pr>1?1/40:1/60;t+=dt;c.observe(dt,4);}
 assert.equal(c.pr,1);assert.ok(c.promotionHold>0);
});
test('Resize conserva el techo explorable y la suspensión limpia medidas', () => {
 const c=new QualityController(1,{ceiling:1.4});run(c,1/60,30);assert.ok(c.pr>1);
 c.resize(.7,.85);assert.ok(c.pr<=.85);assert.ok(c.pr>=c.floor);c.observe(1.2);c.observe(1.2,0,false);assert.equal(c.longFrames,0);assert.equal(c.probe,null);
});
test('Ocultar o redimensionar durante una promoción restaura el estado validado', () => {
 for(const resize of [false,true]) {
  const c=new QualityController(1,{ceiling:1.4});while(!c.probe)c.observe(1/60,4);
  const change=resize?c.resize(.95,1.3):c.observe(1,0,false);
  assert.equal(change.pr,resize?.95:1);run(c,1/50,200);assert.equal(c.pr,resize?.95:1);
 }
});
console.log(JSON.stringify({checks,errors:0}));
