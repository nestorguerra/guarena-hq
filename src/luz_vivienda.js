// Luz doméstica acotada por distancia, con transición continua entre focos.
// Se restaura al terminar cada vista y se liberan sus mapas al quitar la casa.
const preparadas=new WeakSet();
export function prepararLuzVivienda(h, cam, sombras=true) {
  if(!h||!['vecino','annie'].includes(h.kind))return ()=>{};
  if(!preparadas.has(h)){
    preparadas.add(h);
    h.group.addEventListener('removed',()=>{for(const l of h.lights)l.shadow?.dispose();});
  }
  const luces=h.lights.filter(l=>!l.userData.fire&&l.intensity>0);
  if(!luces.length)return ()=>{};
  const orden=luces.map(l=>({l,d:Math.sqrt(l.position.distanceToSquared(cam.position))})).sort((a,b)=>a.d-b.d);
  const principal=orden[0].l,d0=orden[0].d;
  if(d0>25)return ()=>{}; // vista exterior por una ventana
  const antes=h.lights.map(l=>[l,l.intensity,l.castShadow,l.shadow?.intensity]);
  for(const {l,d} of orden){
    const delta=(d-d0)/2.25;
    l.intensity*=.08+.92*Math.exp(-delta*delta);
  }
  for(const l of h.lights)l.castShadow=l===principal&&sombras;
  if(sombras){
    // En la bisectriz entre dos focos la sombra se desvanece antes de cambiar
    // de origen. No hay salto de brillo ni siluetas que salten de una pared a otra.
    const t=Math.min(1,((orden[1]?.d??d0+2)-d0)/.8);
    principal.shadow.intensity=.75*t*t*(3-2*t);
    principal.shadow.mapSize.set(512,512);
    principal.shadow.camera.near=.08;
    principal.shadow.bias=-.0003;
    principal.shadow.normalBias=.025;
    principal.shadow.radius=2;
  }
  return ()=>{for(const [l,i,s,a] of antes){l.intensity=i;l.castShadow=s;if(l.shadow)l.shadow.intensity=a;}};
}

// La oclusión de dos metros del exterior ennegrecía el suelo bajo sillas pequeñas.
// Se acota a contactos domésticos y se restaura para la siguiente vista.
export function prepararOclusionVivienda(h, cam, ao, grade) {
  const U=ao?.gtaoMaterial?.uniforms, mezcla=grade?.uniforms?.uAO;
  if(!h||!['vecino','annie'].includes(h.kind)||!ao?.enabled||!U||!mezcla)return ()=>{};
  if(h.origin&&Math.hypot(cam.position.x-h.origin.x,cam.position.z-h.origin.z)>25)return ()=>{};
  const perfil={radius:.85,thickness:.6,scale:1.4},antes={};
  for(const k of Object.keys(perfil)){antes[k]=U[k].value;U[k].value=perfil[k];}
  const intensidad=mezcla.value;mezcla.value=.85;
  return ()=>{for(const k of Object.keys(antes))U[k].value=antes[k];mezcla.value=intensidad;};
}
