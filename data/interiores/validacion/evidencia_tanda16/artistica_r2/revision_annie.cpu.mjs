import fs from'node:fs';import assert from'node:assert/strict';import crypto from'node:crypto';import{runtime}from'./revision_annie_runtime.cpu.mjs';
const root='.cache/calidad/tanda16/annie_metadata/',before=fs.readFileSync(root+'casa_annie_antes.js','utf8'),after=fs.readFileSync('src/casa_annie.js','utf8'),sha=s=>crypto.createHash('sha256').update(s).digest('hex'),api=runtime(true),oldBuild=api.annieBuilder(before),newBuild=api.annieBuilder(after),rows=[];
assert.equal(sha(before),'843af3240a9f23dfb51399261e2fb35c22b994bba71d4224e072fda64ccf52ff');assert.equal(sha(after),'7364d553829e4a86b470d266ef9849cf3498e3cec584404e6d5e5dbd0fd8ff09');
const delta="...(A.composicionCocina?{entradasEfectivas:A.K.objetos,composicionCocina:A.composicionCocina}:{}),";assert.equal(after.replace(delta,''),before);
const hashArray=a=>sha(Buffer.from(a.buffer,a.byteOffset,a.byteLength)),mesh=m=>({type:m.type,name:m.name,pose:[m.position.toArray(),m.quaternion.toArray(),m.scale.toArray()],visible:m.visible,cast:m.castShadow,receive:m.receiveShadow,...(m.isMesh?{attributes:Object.fromEntries(Object.entries(m.geometry.attributes).map(([k,v])=>[k,hashArray(v.array)])),index:m.geometry.index?hashArray(m.geometry.index.array):null}:{}),children:m.children.map(mesh)}),plain=o=>JSON.parse(JSON.stringify(o,(k,v)=>k==='mesh'?undefined:v)),strip=e=>{const{entradasEfectivas,composicionCocina,...p}=e;return p;};
for(const seed of[12,13]){
 const a=oldBuild(seed,{x:-9700,z:-9700}),b=newBuild(seed,{x:-9700,z:-9700}),budget={interior:{triangulos_max:Infinity,mallas_max:Infinity,luces_max:Infinity}};
 const er=x=>x.estancias.flatMap(e=>api.V.revisar({local:e,group:{traverse(){}}},budget).errores.map(s=>e.sala+': '+s)),red=er(a),green=er(b);
 assert.deepEqual(green,[]);assert(b.estancias.find(e=>e.sala==='cocina').composicionCocina);assert(red.length>0);
 assert.deepEqual(a.estancias,b.estancias.map(strip));assert.deepEqual(mesh(a.group),mesh(b.group));
 const interactions=x=>x.inter.map(i=>({...plain(i),mesh:i.mesh?mesh(i.mesh):null}));assert.deepEqual(interactions(a),interactions(b));
 for(const k of['rooms','personalizadas','bounds','origin','spots','fallosKit','level','split'])assert.deepEqual(a[k],b[k]);
 assert.deepEqual(a.levels.map(c=>[Array.from(c.segs),Array.from(c.circles)]),b.levels.map(c=>[Array.from(c.segs),Array.from(c.circles)]));
 assert.deepEqual(a.lights.map(l=>[l.position.toArray(),l.intensity,l.color.toArray(),l.distance,l.decay,l.castShadow]),b.lights.map(l=>[l.position.toArray(),l.intensity,l.color.toArray(),l.distance,l.decay,l.castShadow]));
 assert.deepEqual(a.doors.map(d=>({...plain({...d,pivot:undefined,mesh:undefined}),pivot:mesh(d.pivot)})),b.doors.map(d=>({...plain({...d,pivot:undefined,mesh:undefined}),pivot:mesh(d.pivot)})));
 for(const y of[0,3.1])for(const z of[1,5,7.2,9.39,10]){assert.equal(a.floorY(-9697.4,-9700+z,y),b.floorY(-9697.4,-9700+z,y));assert.equal(a.ceilY(-9697.4,-9700+z,y),b.ceilY(-9697.4,-9700+z,y));}
 assert(Math.abs(b.floorY(-9697.4,-9692.8,0)-1.55)<.01);for(const t of['safe','bed','mirror','tv','drawer','fridge','eat','read','exit'])assert(b.inter.some(i=>i.type===t));
 const safe=b.inter.find(i=>i.type==='safe');assert.equal(safe.y,3.1);assert(Math.abs(safe.x+9697.84)<.01);
 let count=0;b.group.traverse(o=>{if(o.isMesh&&o.visible)count++;});rows.push({seed,red,green,onlyMetadataAdded:true,meshGeometryAndPosesExact:true,collidersExact:true,doors:b.doors.length,lights:b.lights.length,meshes:count,actions:interactions(b).map(({mesh,...i})=>i),stairsHeight:b.floorY(-9697.4,-9692.8,0)});for(const h of[a,b])h.group.traverse(o=>o.geometry?.dispose());
}
fs.writeFileSync(root+'revision_cpu.json',JSON.stringify({state:'PASS_CPU_NOT_BROWSER',before:sha(before),after:sha(after),rows},null,2)+'\n');console.log(rows.map(({actions,...r})=>r));
