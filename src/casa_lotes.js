// Lotes de una casa de vecinos. Mantiene separados botín, pantallas, ventanas y cada hoja de puerta móvil.
import * as THREE from 'three';
import { mergeGeometries } from 'three/addons/utils/BufferGeometryUtils.js';

export function agruparCasa(h) {
  const materiales=[];
  const protegidos=new Set();
  for(const i of h.inter) if(i.mesh) i.mesh.traverse(o=>protegidos.add(o));
  for(const t of h.pieces.tv) if(t.mesh) protegidos.add(t.mesh);
  // Las imágenes de canvas pequeñas se reúnen en un atlas privado de esta casa. Nunca se añaden fotografías.
  const imagenes=new Map();
  h.group.traverse(o=>{
    const m=o.material,t=m?.map;
    if(o.isMesh&&o.visible&&!protegidos.has(o)&&m!==h.winMat&&t?.isCanvasTexture&&t.wrapS===THREE.ClampToEdgeWrapping&&t.wrapT===THREE.ClampToEdgeWrapping&&!m.transparent&&!m.emissiveMap)imagenes.set(t.uuid,t);
  });
  let atlas=null,slots=new Map();
  if(imagenes.size>1) {
    const celda=132,cols=Math.ceil(Math.sqrt(imagenes.size)),size=2**Math.ceil(Math.log2(cols*celda));
    const canvas=document.createElement('canvas');canvas.width=canvas.height=size;const ctx=canvas.getContext('2d');
    let i=0;
    for(const [id,t] of imagenes){const x=(i%cols)*celda+2,y=Math.floor(i/cols)*celda+2;ctx.drawImage(t.image,x-2,y-2,132,132);ctx.drawImage(t.image,x,y,128,128);slots.set(id,{x,y,size});i++;}
    atlas=new THREE.CanvasTexture(canvas);atlas.colorSpace=THREE.SRGBColorSpace;atlas.anisotropy=4;
  }
  const grupos=[h.group,...h.doors.map(d=>d.pivot)];
  const puertas=new Set(h.doors.map(d=>d.pivot));
  // Los hijos de una puerta se agrupan en el marco de su pivote, que sigue animándose como antes.
  for(const raiz of grupos) {
    raiz.updateMatrixWorld(true);const inv=raiz.matrixWorld.clone().invert(),bins=new Map(),candidatos=[];
    const recorrer=o=>{
      if(o!==raiz&&puertas.has(o))return;
      if(o.isMesh&&o.visible&&!protegidos.has(o)&&o.material!==h.winMat&&!Array.isArray(o.material)&&o.material.isMeshStandardMaterial)candidatos.push(o);
      for(const hijo of o.children)recorrer(hijo);
    };recorrer(raiz);
    for(const o of candidatos) {
      const m=o.material,t=m.map,slot=atlas&&slots.get(t?.uuid),map=slot?atlas:t;
      const key=JSON.stringify([map?.uuid,m.normalMap?.uuid,m.defines||null,!!o.userData.lamp,m.roughness,m.metalness,m.side,m.transparent,m.opacity,m.alphaTest,m.depthWrite,m.emissive.getHex(),m.emissiveIntensity,m.emissiveMap?.uuid,o.castShadow,o.receiveShadow]);
      if(!bins.has(key)){const material=m.clone();material.color.set(0xffffff);material.vertexColors=true;if(slot)material.map=atlas;bins.set(key,{material,geos:[],originales:[],cast:o.castShadow,receive:o.receiveShadow});}
      const bin=bins.get(key),g=o.geometry.index?o.geometry.toNonIndexed():o.geometry.clone();
      g.applyMatrix4(inv.clone().multiply(o.matrixWorld));
      const n=g.attributes.position.count,old=g.attributes.color,col=new Float32Array(n*3);
      for(let i=0;i<n;i++){col[i*3]=m.color.r*(old?old.getX(i):1);col[i*3+1]=m.color.g*(old?old.getY(i):1);col[i*3+2]=m.color.b*(old?old.getZ(i):1);}
      g.setAttribute('color',new THREE.BufferAttribute(col,3));
      if(!g.attributes.uv)g.setAttribute('uv',new THREE.BufferAttribute(new Float32Array(n*2),2));
      if(slot){const uv=g.attributes.uv;for(let i=0;i<uv.count;i++)uv.setXY(i,(slot.x+Math.max(0,Math.min(1,uv.getX(i)))*128)/slot.size,1-(slot.y+(1-Math.max(0,Math.min(1,uv.getY(i))))*128)/slot.size);}
      for(const a of Object.keys(g.attributes))if(!['position','normal','color','uv'].includes(a))g.deleteAttribute(a);
      bin.geos.push(g);bin.originales.push(o);
    }
    for(const b of bins.values()) {
      if(b.originales.length<2){for(const g of b.geos)g.dispose();b.material.dispose();continue;}
      const geometry=mergeGeometries(b.geos,false);for(const g of b.geos)g.dispose();
      if(!geometry){b.material.dispose();continue;}
      const mesh=new THREE.Mesh(geometry,b.material);mesh.castShadow=b.cast;mesh.receiveShadow=b.receive;raiz.add(mesh);
      if(b.originales[0].userData.lamp)mesh.userData.lamp=true;
      materiales.push(b.material);
      for(const o of b.originales){o.removeFromParent();o.geometry.dispose();}
    }
  }
  h.group.addEventListener('removed',()=>{for(const m of materiales)m.dispose();});
  if(atlas){
    h.group.userData.atlasCasa=atlas;
    h.group.addEventListener('removed',()=>atlas.dispose());
  }
}
