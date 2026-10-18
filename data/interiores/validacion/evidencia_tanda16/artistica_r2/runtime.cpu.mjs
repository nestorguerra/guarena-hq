import fs from 'node:fs';import assert from 'node:assert/strict';import crypto from 'node:crypto';
import * as THREE from '../../tanda11_three_r170.mjs';
import {mergeGeometries} from '../../infantil_lectura_juego_bv3/dependencias/BufferGeometryUtils.mjs';
import {RoundedBoxGeometry} from '../../infantil_lectura_juego_bv3/dependencias/RoundedBoxGeometry.mjs';
const root='.cache/calidad/cocina_t16/produccion_r1/',entry=JSON.parse(fs.readFileSync(root+'base.json','utf8')),clean=s=>s.replace(/^import .*;\n/gm,'').replace(/\bexport /g,''),sha=s=>crypto.createHash('sha256').update(s).digest('hex'),source=new Map();
for(const[p,h]of Object.entries(entry.sha256)){const b=fs.readFileSync(root+'base/'+p);assert.equal(sha(b),h,'snapshot base alterado: '+p);if(!p.endsWith('.jpg'))source.set(p,b.toString('utf8'));}
const read=(p,after=false)=>after?fs.readFileSync('.cache/calidad/cocina_t16/artistica_r2/candidata/'+p,'utf8'):source.get(p);
const raw=after=>({OBJETOS:Object.fromEntries([...source.keys()].filter(p=>p.startsWith('data/objetos/')).flatMap(p=>JSON.parse(read(p,after)).objetos.map(o=>[o.id,o]))),KITS:Object.fromEntries([...source.keys()].filter(p=>p.startsWith('data/kits/')&&!p.endsWith('kit.schema.json')).map(p=>[p.split('/').pop().replace('.json',''),JSON.parse(read(p,after))]))});
const textNames=['comercio','servicios','tiendas_a','tiendas_b','vivienda_a','vivienda_b'];
function canvas(){
 const c={width:0,height:0,toDataURL(){return 'trace_only_no_raster';}};
 const ctx=new Proxy({canvas:c,measureText:t=>({width:String(t).length*8}),createLinearGradient:()=>({addColorStop(){}}),createRadialGradient:()=>({addColorStop(){}}),getImageData:(x,y,w,h)=>({data:new Uint8ClampedArray(w*h*4),width:w,height:h}),createImageData:(w,h)=>({data:new Uint8ClampedArray(w*h*4),width:w,height:h}),getLineDash:()=>[]},{get(o,k){if(k in o)return o[k];return ()=>{};},set(o,k,v){o[k]=v;return true;}});
 c.getContext=()=>ctx;return c;
}
const classSet=new Set();
const document={body:{classList:{add:c=>classSet.add(c),remove:c=>classSet.delete(c)}},createElement:tag=>{assert.equal(tag,'canvas');return canvas();}};
const make=(s,deps,exp)=>new Function(...Object.keys(deps),clean(s)+';return {'+exp+'};')(...Object.values(deps));
const util=make(read('src/util.js'),{},'clamp,mulberry32,hash1');
const {StaticCollider}=make(read('src/collision.js'),util,'StaticCollider');

const textures=Object.fromEntries(textNames.map(n=>['TEX_'+n.toUpperCase(),make(read('src/texturas/'+n+'.js'),{THREE,document,...util},'TEXTURAS').TEXTURAS]));
function runtime(after,mutate=null){
 const objectsSource=read('src/objetos.js');
 const data=raw(after);if(mutate)mutate(data);
 const finishesSource=read('src/acabados_vivienda.js');
 const assetTextureCache=new Map();
 const loadTexture=(name,suffix='_d',{srgb=true,repeat=1}={})=>{const key=name+suffix;if(assetTextureCache.has(key))return assetTextureCache.get(key);const t=new THREE.Texture();t.wrapS=t.wrapT=THREE.RepeatWrapping;t.anisotropy=8;if(srgb)t.colorSpace=THREE.SRGBColorSpace;t.repeat.set(repeat,repeat);assetTextureCache.set(key,t);return t;};
 const HK=make(read('src/housekit.js'),{THREE,document,mergeGeometries,StaticCollider,loadTexture,...util},'INTERIOR_ORIGIN,WALL_H,T,boxGeo,planeGeo,cylGeo,pictureTexture,rugTexture,HouseBuilder,std,texMat,glassMat,ringSegs,programaLuzDomestica');
 const objetos=make(objectsSource,{THREE,document,mergeGeometries,RoundedBoxGeometry,OBJETOS:data.OBJETOS,pictureTexture:HK.pictureTexture,...util,...textures},'caja,construir,kelvin');
 const geo=make(read('src/interiores_geo.js'),{...data,...objetos},'rot,partes,penetra,superficie,mapaPaso,espacioFrontal');
 const locales=make(read('src/locales.js',after),{THREE,...data,...HK,...objetos,...geo,...util,MURO:HK.T},'amueblar,encaja,filtroHogar,buildLocal');
 const acabado=make(finishesSource,{THREE,document,...HK,...objetos,...util,TEXTURAS:textures.TEX_VIVIENDA_B},'revestirEstancia');
 const {agruparCasa}=make(read('src/casa_lotes.js'),{THREE,document,mergeGeometries},'agruparCasa');
 const H=make(read('src/houses.js',after),{THREE,document,StaticCollider,...util,...HK,...data,...objetos,...geo,...locales,...acabado,agruparCasa},'buildVecino,PROFILES,kitDeEstancia');
 const V=make(read('tools/interiores/validar.js',after),{...H,...locales,...data,...objetos,...geo},'revisar,revisarUso');
 return {H,acabado,HK,V,data,geo,...locales,...objetos};
}

export{runtime,THREE,read,source,sha,entry};
