  if(opts.tanda>=20)await caso('estudio: tela real libre del puesto y ordenador, con negativo de paño largo',()=>{
    const proto=HouseBuilder.prototype,add=proto.add;
    let telas=[];
    // add transforma la geometría recibida: copiar ANTES conserva el paño real.
    proto.add=function(key,g,x,y,z,ry=0){
      if(key==='curtain'){
        const copia=g.clone();telas.push(copia);
        copia.rotateY(ry).translate(this.ox+x,y,this.oz+z);
      }
      return add.call(this,key,g,x,y,z,ry);
    };
    try{for(const seed of[3244,1594,1481]){
      telas=[];let h;
      try{
        h=H.buildVecino(seed,{x:-5200,z:-5200});
        const salas=h.estancias.filter(e=>e.kit==='vivienda_estudio');exigir(salas.length===1,seed+': falta estudio dirigido');
        const e=salas[0],C=e.colocados,mesas=C.filter(p=>OBJETOS[p.obj]?.rol==='mesa'),ordenadores=C.filter(p=>p.obj==='vb_ordenador');
        exigir(mesas.length===1&&ordenadores.length===1,seed+': falta puesto u ordenador real');
        const mesa=mesas[0];exigir(ordenadores[0].sop===C.indexOf(mesa),seed+': ordenador no apoyado en el puesto');
        const paneles=C.filter(p=>/^vb_panel_estudio_/.test(p.obj));
        const objetivos=[mesa,ordenadores[0],...paneles];
        const marco=new THREE.Box3(new THREE.Vector3(e.origen.x-e.W/2,e.origen.y,e.origen.z),new THREE.Vector3(e.origen.x+e.W/2,e.origen.y+e.H,e.origen.z+e.D));
        const locales=telas.filter(g=>{g.computeBoundingBox();return g.boundingBox.intersectsBox(marco);});
        // rooms no expone open: views conserva los huecos exteriores físicos del
        // constructor. La cota inferior excluye puertas; no inferir ventana de tela.
        const room=h.rooms.find(r=>r.id===e.sala);exigir(room,seed+': falta marco arquitectónico del estudio');
        const ventanas=h.views.filter(v=>{
          const c=v.box.getCenter(new THREE.Vector3());
          return v.box.min.y>e.origen.y+.4&&v.box.max.y<e.origen.y+e.H+.01&&c.x>=room.x0-.08&&c.x<=room.x1+.08&&c.z>=room.z0-.08&&c.z<=room.z1+.08;
        });
        if(!ventanas.length){exigir(!locales.length,seed+': tela local sin ventana real');continue;}
        exigir(locales.length>=2*ventanas.length,seed+': faltan paños reales de ventanas del estudio');
        const paños=locales.map(g=>{
          const pos=g.attributes.position,idx=g.index?.array,n=idx?idx.length:pos.count,tri=[];
          exigir(n>=3&&n%3===0,seed+': tela sin triángulos');
          for(let i=0;i<n;i+=3)tri.push([0,1,2].map(k=>new THREE.Vector3().fromBufferAttribute(pos,idx?idx[i+k]:i+k)));
          return {tri,min:g.boundingBox.min.y,max:g.boundingBox.max.y};
        });
        const intersecciones=paños=>{
          const hits=[];
          for(const item of objetivos)for(const[k,b]of partes(item).entries()){
            const cs=Math.cos(b.a),sn=Math.sin(b.a),box=new THREE.Box3(new THREE.Vector3(-b.hw+.001,b.y0+.001,-b.hd+.001),new THREE.Vector3(b.hw-.001,b.y1-.001,b.hd-.001));
            if(box.isEmpty())continue;
            for(const paño of paños)for(const t of paño.tri){
              const local=t.map(v=>{const x=v.x-e.origen.x-b.cx,z=v.z-e.origen.z-b.cz;return new THREE.Vector3(x*cs-z*sn,v.y-e.origen.y,x*sn+z*cs);});
              if(box.intersectsTriangle(new THREE.Triangle(...local))){hits.push(item.obj+' parte '+k);break;}
            }
          }
          return hits;
        };
        const hits=intersecciones(paños);exigir(!hits.length,seed+': tela atraviesa '+hits.join(', '));
        const cortos=paños.filter(p=>Math.abs(p.max-p.min-.945)<1e-5&&Math.abs(p.max-e.origen.y-2.225)<1e-5&&Math.abs(p.min-e.origen.y-1.28)<1e-5);
        exigir(cortos.length>=2,seed+': faltan paños cortos reales con top conservado');
        if(seed===3244){
          // Sólo un doble de los triángulos capturados: recuperar altura antigua,
          // conservando top y todos los x/z. No tocar geometría ni muebles vivos.
          const largos=cortos.map(p=>({...p,tri:p.tri.map(t=>t.map(v=>new THREE.Vector3(v.x,p.max+(v.y-p.max)*2.05/(p.max-p.min),v.z)))}));
          exigir(intersecciones(largos).length>0,'3244: negativo de paño largo dejó de reproducir el defecto real');
        }
      }finally{try{if(h)tirar(h);}finally{for(const g of telas)g.dispose();telas=[];}}
    }}finally{proto.add=add;for(const g of telas)g.dispose();}
  });
