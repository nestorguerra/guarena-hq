  if(opts.tanda>=21)await caso('salon: lectura conserva inventario, acciones y fallbacks y registra asiento real',async()=>{
    const K=KITS.vivienda_salon,cfg=K.composicion_lectura;
    exigir(cfg,'falta configuración de lectura');
    const igual=(a,b,m)=>exigir(JSON.stringify(a)===JSON.stringify(b),m);
    const identidad=p=>[p.obj,p.e,p.sop,p.sup,p.de,p.clase];
    const accion=i=>[i.id,i.type,i.label,i.def,i.r,i.crack];
    const asiento=s=>[s.x,s.y,s.z,s.h,!!s.chair];
    const presupuesto=await(await fetch('/data/quality_budgets.json')).json();
    try{for(const seed of [3244,1594,4007,4685,2786]){
      let a,b;
      try{
        delete K.composicion_lectura;a=H.buildVecino(seed);K.composicion_lectura=cfg;b=H.buildVecino(seed);
        const x=a.estancias.find(e=>e.kit==='vivienda_salon'),e=b.estancias.find(e=>e.kit==='vivienda_salon');
        exigir(x&&e,seed+': falta salón');const meta=e.composicionLectura,estar=e.composicionEstar,movidos=new Set([...(meta?.movidos||[]),...(estar?.movidos||[])]);
        igual(x.colocados.map(identidad),e.colocados.map(identidad),seed+': cambia identidad/soporte');
        igual(a.inter.map(accion),b.inter.map(accion),seed+': pierde acción o recompensa');
        igual(a.estancias.filter(q=>q!==x),b.estancias.filter(q=>q!==e),seed+': altera otras habitaciones');
        exigir(!revisarUso(b).errores.length,seed+': uso inaccesible');
        exigir(!revisar({local:e,group:{traverse(){}}},presupuesto).errores.length,seed+': programa inválido');
        let mallas=0;b.group.traverse(o=>{if(o.isMesh&&o.visible)mallas++;});exigir(mallas<=presupuesto.interior.mallas_max,seed+': coste excedido');
        exigir(!!meta===(seed===3244||seed===1594),seed+': cambia admisión de lectura');
        if(meta||estar){
          exigir(movidos.size>0&&[...movidos].every(i=>Number.isInteger(i)&&i>=0&&i<e.colocados.length),seed+': unión de movidos inválida');
          for(let i=0;i<x.colocados.length;i++)if(!movidos.has(i))igual(x.colocados[i],e.colocados[i],seed+': mueve pieza ajena '+i);
          if(meta){
          exigir(meta.movidos.length>4,seed+': admisión/dependientes vacíos');
          const p=e.colocados[meta.asiento],o=OBJETOS[p.obj];exigir(p.obj==='puff'&&o.asientos?.length===1,seed+': cambia fixture de asiento');
          const st=o.asientos[0],[dx,dz]=rot(st.p[0],st.p[2],p.ry),sx=e.origen.x+p.x+dx,sz=e.origen.z+p.z+dz;
          const nuevos=b.pieces.seat.filter(s=>Math.hypot(s.x-sx,s.z-sz)<1e-6&&Math.abs(s.h-p.ry)<1e-6);
          exigir(nuevos.length===1&&b.pieces.seat.length===a.pieces.seat.length+1,seed+': puff sin asiento real o duplicado');
          igual(a.pieces.seat.map(asiento),b.pieces.seat.filter(s=>s!==nuevos[0]).map(asiento),seed+': altera asientos existentes');
          }else igual(a.pieces.seat.map(asiento),b.pieces.seat.map(asiento),seed+': estar altera asientos');
        }else{
          exigir(!meta,seed+': fallback/no optante alterado');igual(x.colocados,e.colocados,seed+': fallback parcial');igual(x.activas,e.activas,seed+': activas sin rollback');
          igual(a.inter.map(i=>[...accion(i),i.x,i.y,i.z]),b.inter.map(i=>[...accion(i),i.x,i.y,i.z]),seed+': desplaza acciones en fallback');
          igual(a.pieces.seat.map(asiento),b.pieces.seat.map(asiento),seed+': añade asiento en fallback');
        }
        if(seed===4007||seed===4685)for(const type of ['phone','drawer'])exigir(b.inter.some(i=>i.sala===e.sala&&i.type===type),seed+': pierde '+type);
      }finally{K.composicion_lectura=cfg;if(a)tirar(a);if(b)tirar(b);}
    }}finally{K.composicion_lectura=cfg;}
  });
