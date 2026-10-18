  if(opts.tanda>=21)await caso('salon: alfombra interior y borde quedan visibles sobre el suelo agrupado',()=>{
    for(const [seed,centro]of [[3244,'#c8bda5'],[1594,'#c8bda5'],[2786,null]]){
      let h;try{
        h=H.buildVecino(seed,{x:-5200,z:-5200});h.group.updateMatrixWorld(true);
        const e=h.estancias.find(e=>e.kit==='vivienda_salon');exigir(e,seed+': falta salón');
        const rugs=e.colocados.filter(p=>p.obj==='alfombra_salon');
        if(centro===null){
          exigir(!e.colocados.some(p=>OBJETOS[p.obj].rol==='sofa')&&rugs.length===0,seed+': fixture sin sofá recibió alfombra');
          exigir(!revisarUso(h).errores.length,seed+': uso del caso sin alfombra');continue;
        }
        exigir(rugs.length===1,seed+': falta alfombra real');const p=rugs[0];
        exigir(p.sop==null&&p.clase==='PICKUP'&&e.ancho===.8,seed+': cambia soporte, clase o paso');
        for(const [x,z,top,ex,ez,col]of [[.85,.55,.004,.9,.6,centro],[.95,.65,.003,1,.7,'#687565']]){
          const [dx,dz]=rot(x,z,p.ry),ray=new THREE.Raycaster(new THREE.Vector3(e.origen.x+p.x+dx,e.origen.y+.04,e.origen.z+p.z+dz),new THREE.Vector3(0,-1,0),0,.05);
          const visible=o=>{for(;o;o=o.parent)if(!o.visible)return false;return true;};
          const hits=ray.intersectObject(h.group,true).filter(i=>visible(i.object)),hit=hits[0];
          const piso=hits.find(i=>Math.abs(i.point.y-e.origen.y-.0095)<1e-6);
          exigir(piso&&hit&&hit.point.y>piso.point.y+.0001,seed+': alfombra oculta por suelo en '+x+','+z);
          exigir(Math.abs(hit.point.y-(e.origen.y+p.y+top))<1e-6,seed+': primer triángulo no es la cara del textil');
          const g=hit.object.geometry,c=g.attributes.color,pos=g.attributes.position,m=hit.object.material,expected=new THREE.Color(col);
          exigir(hit.face&&c&&m.vertexColors&&!Array.isArray(m),seed+': color/triángulo real ausente');
          for(const i of [hit.face.a,hit.face.b,hit.face.c]){
            const v=new THREE.Vector3().fromBufferAttribute(pos,i).applyMatrix4(hit.object.matrixWorld),[lx,lz]=rot(v.x-e.origen.x-p.x,v.z-e.origen.z-p.z,-p.ry);
            exigir(Math.abs(Math.abs(lx)-ex)<.001&&Math.abs(Math.abs(lz)-ez)<.001&&Math.abs(v.y-(e.origen.y+p.y+top))<1e-6,seed+': triángulo ajeno al rectángulo del textil');
            exigir(Math.abs(c.getX(i)*m.color.r-expected.r)<1e-6&&Math.abs(c.getY(i)*m.color.g-expected.g)<1e-6&&Math.abs(c.getZ(i)*m.color.b-expected.b)<1e-6,seed+': pierde color propio del textil');
          }
        }
        exigir(Math.abs(p.v.y0-p.y)<1e-6&&Math.abs(p.v.y1-p.y-.004)<1e-6,seed+': volumen y render discrepan');
        exigir(!revisarUso(h).errores.length,seed+': alfombra altera usos');
      }finally{if(h)tirar(h);}
    }
  });
