  if(opts.tanda>=21)await caso('salon: estar aislado conserva núcleo, dependientes, selección y rollback',async()=>{
    const K=KITS.vivienda_salon,cfg=K.composicion_lectura,B=await(await fetch('/data/quality_budgets.json')).json();exigir(cfg,'falta programa');
    const igual=(a,b,m)=>exigir(JSON.stringify(a)===JSON.stringify(b),m);
    try{for(const seed of[3244,1594,2786]){let h;try{
      delete K.composicion_lectura;h=H.buildVecino(seed);const e=h.estancias.find(e=>e.kit==='vivienda_salon');exigir(e,seed+': sin fixture');
      const ctx={W:e.W,D:e.D,H:e.H,inicio:e.inicio,libres:e.libres,funciones:true,perfil:e.hogar.perfil,filtro:x=>e.activas.includes(K.objetos.indexOf(x))};
      const legacy=amueblar(e.kit,e.seed,ctx);K.composicion_lectura=cfg;
      const planta={W:e.W,D:e.D,zonas:e.zonas,tabiques:e.tabiques},aceptar=Q=>!revisar({local:{...e,colocados:Q},group:{traverse(){}}},B).errores.length;
      const common={K,ctx,planta,H:e.H,libres:e.libres,inicio:e.inicio,aceptar};
      const lectura=componerLectura({...common,P:legacy.P}),P=lectura?.P||legacy.P,sello=JSON.stringify(P),params={...common,P,asientoLectura:lectura?.metadata.asiento};
      const estar=componerEstar(params),A=amueblar(e.kit,e.seed,ctx);
      exigir(A.K===K,seed+': cambia identidad K');igual(legacy.activas,A.activas,seed+': cambia activas');exigir(legacy.guardias===A.guardias,seed+': deja guardias');
      for(let i=0;i<12;i++)exigir(legacy.U([0,1])===A.U([0,1]),seed+': consume RNG conjunto');
      exigir(!!estar===(seed!==2786)&&!!A.composicionEstar===(seed!==2786),seed+': admisión/fallback inesperado');
      if(!estar){igual(P,A.P,seed+': fallback cambia poses');continue;}
      exigir(lectura&&estar.metadata.movidos.some(i=>Math.hypot(estar.P[i].x-P[i].x,estar.P[i].z-P[i].z)>.1),seed+': prueba vacía de estar');
      igual(estar.P,A.P,seed+': helper aislado difiere de integración real');
      for(let i=0;i<P.length;i++){
        const q=estar.P[i],p=P[i];igual([q.obj,q.e,q.sop,q.sup,q.de,q.clase],[p.obj,p.e,p.sop,p.sup,p.de,p.clase],seed+': cambia identidad/referencia');
        if(!estar.metadata.movidos.includes(i))igual(q,p,seed+': mueve núcleo ajeno');
        if(estar.metadata.movidos.includes(i)&&p.sop!=null){
          const relativo=(v,s)=>[...rot(v.x-s.x,v.z-s.z,-s.ry),v.y-s.y,v.ry-s.ry],a=relativo(p,P[p.sop]),b=relativo(q,estar.P[q.sop]);
          exigir(a.every((n,k)=>Math.abs(n-b[k])<1e-8),seed+': dependiente pierde apoyo relativo');
        }
      }
      const caminar=Q=>Q.flatMap(p=>partes(p).concat(p.sop==null&&!['pared','techo'].includes(p.regla)&&OBJETOS[p.obj].clase!=='PICKUP'&&caja(p.obj).h>=.3?[p.v]:[]));
      const antes=mapaPaso(planta,caminar(P),.05,.8,e.inicio),despues=mapaPaso(planta,caminar(estar.P),.05,.8,e.inicio);
      const distancia=(m,x,z)=>{let d=Infinity;for(let i=0;i<m.reach.length;i++)if(m.reach[i])d=Math.min(d,Math.hypot(-e.W/2+(i%m.nx+.5)*m.S-x,(Math.floor(i/m.nx)+.5)*m.S-z));return d;};
      let puff=false;
      P.forEach((p,i)=>{if(!['sofa','sillon','silla'].includes(OBJETOS[p.obj].rol)&&i!==params.asientoLectura)return;for(const a of OBJETOS[p.obj].asientos||[]){const[x,z]=rot(a.p[0],a.p[2],p.ry);if(i===params.asientoLectura)puff=true;if(distancia(antes,p.x+x,p.z+z)<1.25)exigir(distancia(despues,p.x+x,p.z+z)<1.25,seed+': pierde asiento seleccionable');}});
      exigir(puff,seed+': no comprueba asiento real de lectura');
      let rechazos=0;exigir(componerEstar({...params,aceptar:()=>{rechazos++;return false;}})===null&&rechazos>0,seed+': rechazo vacío o ignorado');
      let excepcion=false;try{componerEstar({...params,aceptar:()=>{throw Error('estar_rechazo');}});}catch(err){exigir(err.message==='estar_rechazo','excepción ajena');excepcion=true;}
      exigir(excepcion&&JSON.stringify(P)===sello,seed+': excepción/rechazo muta base');
      exigir(!componerEstar({...params,inicio:{x:-999,z:-999}}),seed+': acepta inicio exterior');
      exigir(!componerEstar({...params,libres:[{cx:0,cz:e.D/2,hw:e.W/2,hd:e.D/2,a:0,y0:0,y1:e.H}]}),seed+': invade reserva total');
    }finally{K.composicion_lectura=cfg;if(h)tirar(h);}}}finally{K.composicion_lectura=cfg;}
  });
