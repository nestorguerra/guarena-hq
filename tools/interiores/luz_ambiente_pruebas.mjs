// Contratos offline: helper real y cuerpo real de Game.renderView, sin WebGL.
// Ejecutar: node --test tools/interiores/luz_ambiente_pruebas.mjs
import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
const fuenteLuz=readFileSync(new URL('../../src/luz_vivienda.js',import.meta.url),'utf8');
const L=await import('data:text/javascript;base64,'+Buffer.from(fuenteLuz).toString('base64'));
const fuenteGame=readFileSync(new URL('../../src/game.js',import.meta.url),'utf8');
const cuerpo=fuenteGame.match(/  renderView\(cam\) \{([\s\S]*?)\n  \}\n  \/\//)?.[1];
assert.ok(cuerpo,'No se encuentra el método real Game.renderView');
const vista=plastilina=>new Function('prepararLuzVivienda','prepararOclusionVivienda','prepararAmbienteVivienda','STYLE',
  'return function(cam){'+cuerpo+'}')(L.prepararLuzVivienda,L.prepararOclusionVivienda,L.prepararAmbienteVivienda,{plastilina});
const cam={position:{x:2,y:1.6,z:2}};
const casa=kind=>({kind,origin:{x:0,z:0},group:{addEventListener(){}},lights:[]});
const estado=()=>({scene:{environmentIntensity:.73},sky:{bounce:{intensity:.91}}});
const igual=(s,a=.73,b=.91)=>{assert.equal(s.scene.environmentIntensity,a);assert.equal(s.sky.bounce?.intensity,b);};

test('vecino y Annie: factores relativos, apagón y restauración exacta',()=>{
  for(const kind of ['vecino','annie'])for(const powered of [true,false]){
    const s=estado(),h={...casa(kind),powered};
    const fin=L.prepararAmbienteVivienda(h,cam,s.scene,s.sky);
    igual(s,.73*(powered?.55:1),.91*(powered?.25:1));assert.equal(h.powered,powered);fin();igual(s);
    const otra=L.prepararAmbienteVivienda(h,cam,s.scene,s.sky);otra();igual(s);
  }
});
test('comercios, iglesia, ausencia de casa y cámara exterior no cambian',()=>{
  for(const h of [null,casa('local'),casa('bar'),casa('church'),{kind:'vecino'}]){
    const s=estado(),fin=L.prepararAmbienteVivienda(h,cam,s.scene,s.sky);igual(s);fin();igual(s);
  }
  const s=estado(),fin=L.prepararAmbienteVivienda(casa('vecino'),{position:{x:100,z:100}},s.scene,s.sky);igual(s);fin();igual(s);
});
test('sin bounce y con intensidades cero no crea luz',()=>{
  const scene={environmentIntensity:0},sky={};
  const fin=L.prepararAmbienteVivienda(casa('vecino'),cam,scene,sky);assert.equal(scene.environmentIntensity,0);fin();assert.equal(scene.environmentIntensity,0);assert.equal(sky.bounce,undefined);
  sky.bounce={intensity:0};L.prepararAmbienteVivienda(casa('annie'),cam,scene,sky)();assert.equal(sky.bounce.intensity,0);
});
test('el perfil se puede sustituir en un único punto',()=>{
  const s=estado(),fin=L.prepararAmbienteVivienda(casa('vecino'),cam,s.scene,s.sky,{ambiente:.8,rebote:.4});igual(s,.73*.8,.91*.4);fin();igual(s);
});
for(const composer of [false,true])for(const falla of [false,true])test(`renderView real: compositor=${composer}, excepción=${falla}`,()=>{
  const s=estado(),error=new Error('render simulado'),h=casa('vecino');let dibujados=0;
  const dibujar=()=>{dibujados++;igual(s,.73*.55,.91*.25);if(falla)throw error;};
  const g={...s,interior:h,renderer:{shadowMap:{enabled:true},render:dibujar},composer:composer?{passes:[{camera:cam}],render:dibujar}:null};
  // WindowView dibuja antes de renderView: estado exterior previo y posterior intacto.
  igual(s);if(falla)assert.throws(()=>vista(true).call(g,cam),e=>e===error);else vista(true).call(g,cam);
  assert.equal(dibujados,1);igual(s);
});
test('renderView real no modifica Realista ni interiores no domésticos',()=>{
  for(const [plastilina,h] of [[false,casa('vecino')],[true,casa('local')],[true,null]]){
    const s=estado(),g={...s,interior:h,renderer:{shadowMap:{enabled:true},render:()=>igual(s)}};
    vista(plastilina).call(g,cam);igual(s);
  }
});
