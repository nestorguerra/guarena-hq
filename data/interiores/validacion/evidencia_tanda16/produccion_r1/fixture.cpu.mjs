// Prueba CPU: misma planta, muebles y reservas; sólo identidad de descanso y juego.
import fs from 'node:fs';import assert from 'node:assert/strict';import crypto from 'node:crypto';
import * as THREE from '../../tanda11_three_r170.mjs';
import {source,read,sha,runtime}from'./runtime.cpu.mjs';
const {data:{OBJETOS,KITS}}=runtime(false),candidate=KITS.vivienda_cocina;
const clean=s=>s.replace(/^import .*;\n/gm,'').replace(/\bexport /g,'');
import {RoundedBoxGeometry} from '../../infantil_lectura_juego_bv3/dependencias/RoundedBoxGeometry.mjs';
const obj=read('src/objetos.js'),geometry=clean(obj.slice(obj.indexOf('const DEG ='),obj.indexOf('// ---------------------------------------------------------------- the pictures'))),geo=clean(read('src/interiores_geo.js')),util=clean(read('src/util.js')),local=clean(read('src/locales.js').split('export function buildLocal')[0]);
function engine(O,K){const caja=new Function('THREE','RoundedBoxGeometry','OBJETOS',geometry+';return caja;')(THREE,RoundedBoxGeometry,O);return new Function('KITS','OBJETOS','caja',`const MURO=.14;${util}\n${geo}\n${local};return {amueblar,caja,choca,rot,partes,penetra,superficie,mapaPaso,filtroHogar,espacioFrontal};`)({room:K},O,caja);}
const now=engine(OBJETOS,candidate),filtroHogar=now.filtroHogar;
// La planta conserva código real hasta concluir sus ramas. Se descarta la geometría
// dibujada y se conserva el consumo de RNG de patrones/ventanas/materiales de la casa.
// No se ejecuta el montaje de mallas, luces ni navegación global de buildVecino.
const canvasCtx=new Proxy({}, {get(o,k){if(k in o)return o[k];if(k==='createLinearGradient'||k==='createRadialGradient')return ()=>({addColorStop(){}});return ()=>{};},set(o,k,v){o[k]=v;return true;}});
const document={createElement:()=>({getContext:()=>canvasCtx})};
class LayoutBuilder{
 constructor(x,z){this.ox=x;this.oz=z;this.mats=new Map();this.extra=[];}
 mat(k,f){if(!this.mats.has(k))this.mats.set(k,f());return k;}
 add(k,g){g?.dispose();}wall(){}view(){}light(){}interact(){}
 extraMesh(m){m.geometry?.dispose();}doorLeaf(){return {pivot:new THREE.Object3D()};}
}
const house=read('src/houses.js'),head=clean(house.slice(0,house.indexOf('// ---------------------------------------------------------------- the builder for one house'))),body=house.slice(house.indexOf('export function buildVecino'),house.indexOf('  const D = D1 + P;')).replace('export ','');
const layout=new Function('THREE','document','HouseBuilder','std','texMat','boxGeo','planeGeo','cylGeo',`${util}\nconst WALL_H=2.95;\n${head}\n${body}\n for(const m of B.extra)m.geometry?.dispose();return {prof,rooms};}\nreturn {build:buildVecino,profiles:PROFILES};`)(THREE,document,LayoutBuilder,()=>new THREE.MeshStandardMaterial(),()=>new THREE.MeshStandardMaterial(),(w,h,d)=>new THREE.BoxGeometry(w,h,d),(w,h)=>new THREE.PlaneGeometry(w,h),(a,b,h,s)=>new THREE.CylinderGeometry(a,b,h,s));
function fixture(seed){
 const {prof,rooms}=layout.build(seed,{x:-5200,z:-5200});return rooms.flatMap((rm,i)=>{
 if(rm.type!=='cocina')return [];
 const W=rm.w-.15,D=rm.d-.15,ox=rm.cx,oz=rm.z0+.075,libres=[];
 for(const o of rm.open){const fondo=o.door?1:.38,ancho=(o.b-o.a)/2+(o.door?.15:.05),y0=o.door?0:.92;
  if(o.side==='s'||o.side==='n')libres.push({cx:(o.a+o.b)/2-ox,cz:o.side==='s'?fondo/2:D-fondo/2,hw:ancho,hd:fondo/2,a:0,y0,y1:2.4});
  else libres.push({cx:o.side==='w'?-W/2+fondo/2:W/2-fondo/2,cz:(o.a+o.b)/2-oz,hw:fondo/2,hd:ancho,a:0,y0,y1:2.4});
 }
 for(const bx of rm.boxes)libres.push({cx:(bx[0]+bx[2])/2-ox,cz:(bx[1]+bx[3])/2-oz,hw:(bx[2]-bx[0])/2,hd:(bx[3]-bx[1])/2,a:0,y0:0,y1:3});
 const d=rm.open.find(o=>o.door),m=d?(d.a+d.b)/2:0,inicio=!d?{x:0,z:D/2}:d.side==='s'?{x:m-ox,z:.5}:d.side==='n'?{x:m-ox,z:D-.5}:d.side==='w'?{x:-W/2+.5,z:m-oz}:{x:W/2-.5,z:m-oz};
 return [{houseSeed:seed,roomIndex:i,perfil:prof.id,estilo:prof.style,plano:prof.layout,room:rm,seed:(prof.seed*131+i*17+5)>>>0,ctx:{W,D,H:rm.lv?2.75:2.95,libres,inicio,filtro:filtroHogar({perfil:prof.id,estilo:prof.style,habitacion:'cocina'}),funciones:true}}];
 });
}


export {fixture};
