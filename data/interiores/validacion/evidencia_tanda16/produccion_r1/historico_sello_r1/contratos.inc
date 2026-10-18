  if(opts.tanda>=19)await caso('cocina: programa compuesto conserva núcleo, puestos, cuotas y receta efectiva',async()=>{
    const B=await(await fetch('/data/quality_budgets.json')).json(),K=KITS.vivienda_cocina,sello=JSON.stringify(K),cfg=K.composicion_cocina;
    const normal=id=>id.replace(/_(rustico|liso|vajillero)$/,''),ids=['va_cocina','va_cocina_amplia','va_encimera','va_encimera_amplia','va_nevera','va_lavadora','mesa_camilla','va_mesa_comedor','silla_comedor'];
    const nucleo=C=>C.filter(p=>ids.includes(normal(p.obj))).map(p=>({obj:normal(p.obj),x:p.x,y:p.y,z:p.z,ry:p.ry}));
    for(const seed of[2786,3244,1594]){
      let base,h;
      try{
        delete K.composicion_cocina;base=H.buildVecino(seed);K.composicion_cocina=cfg;h=H.buildVecino(seed);
        const e=h.estancias.find(e=>e.kit==='vivienda_cocina'),old=base.estancias.find(e=>e.kit==='vivienda_cocina'),C=e.colocados;
        exigir(e.composicionCocina&&e.entradasEfectivas?.length===K.objetos.length,seed+': sin receta efectiva');
        exigir(JSON.stringify(h.loot.map(({mesh,...o})=>o))===JSON.stringify(base.loot.map(({mesh,...o})=>o)),seed+': botin IDs/definiciones cambiados');
        const acciones=x=>x.inter.filter(i=>i.sala===e.sala&&['eat','fridge','hide'].includes(i.type)).map(i=>i.type).sort();
        exigir(JSON.stringify(acciones(h))===JSON.stringify(acciones(base)),seed+': pierde acciones cocina/nevera/guardado');
        exigir(JSON.stringify(nucleo(C))===JSON.stringify(nucleo(old.colocados)),seed+': núcleo o mesa movidos');
        const pan=C.find(p=>p.obj===cfg.actividad),columna=C.filter(p=>p.obj.startsWith('va_guardar_')),alto=C.filter(p=>p.obj.startsWith('va_banda_'));
        exigir(pan&&columna.length===1&&alto.length===1,seed+': programa incompleto');
        exigir(C[pan.sop]?.obj.startsWith('va_encimera_')&&pan.sup===0,seed+': actividad sin preparación');
        exigir(e.activas.includes(pan.e)&&e.entradasEfectivas[pan.e].obligatorio,seed+': actividad sin mínimo efectivo');
        for(const[i,p]of C.entries()){
          exigir(e.entradasEfectivas[p.e],seed+': e desconocido');
          for(const k of['sop','de'])if(p[k]!=null)exigir(Number.isInteger(p[k])&&p[k]>=0&&p[k]<C.length&&p[k]!==i,seed+': '+k+' huérfano');
          if(p.sop!=null)exigir(OBJETOS[C[p.sop].obj].superficies?.[p.sup],seed+': sup huérfana');
        }
        const r=revisar({local:e,group:{traverse(){}}},B);exigir(!r.errores.length,seed+': '+r.errores.join('; '));exigir(!revisarUso(h).errores.length,seed+': usos reales');
        let meshes=0;h.group.traverse(o=>{if(o.isMesh&&o.visible)meshes++;});exigir(meshes<=60,seed+': presupuesto de mallas');
        const ie=C.find(p=>p.obj==='va_nevera').e,ausente={...e,activas:e.activas.filter(i=>i!==ie)};
        exigir(revisar({local:ausente,group:{traverse(){}}},B).errores.some(s=>s.includes('activa obligatoria omitida')),seed+': oculta entrada global obligatoria desde activas');
        const reservas={...e,entradasEfectivas:structuredClone(e.entradasEfectivas)};reservas.entradasEfectivas[ie].espacio_frontal=[.1,.1];
        exigir(revisar({local:reservas,group:{traverse(){}}},B).errores.some(s=>s.includes('reserva de programa')),seed+': puede reducir reserva efectiva');
        const sinPan={...e,colocados:C.filter(p=>p!==pan)};exigir(revisar({local:sinPan,group:{traverse(){}}},B).errores.some(s=>s.includes('obligatorio:')&&s.includes(cfg.actividad)),seed+': validador omite mínimo efectivo');
        const falso={...e,entradasEfectivas:structuredClone(e.entradasEfectivas)};falso.entradasEfectivas[pan.e].cantidad=[0,0];falso.entradasEfectivas[pan.e].obligatorio=false;
        exigir(revisar({local:falso,group:{traverse(){}}},B).errores.some(s=>s.includes('receta efectiva: altera contrato')),seed+': receta efectiva permite rebajar cuota global');
        const objeto='__cocina_bloqueo',p=columna[0],R=espacioFrontal(p,caja(p.obj),e.entradasEfectivas[p.e].espacio_frontal);
        OBJETOS[objeto]={...OBJETOS.va_nevera,id:objeto,partes:[{f:'caja',d:[.2,1,.2],p:[0,.5,0],c:'#888888',m:'madera'}]};
        try{const bloque={obj:objeto,e:pan.e,zona:p.zona,regla:'suelo_libre',x:R.cx,y:0,z:R.cz,ry:0,sop:null,sup:null,de:null,v:{cx:R.cx,cz:R.cz,hw:.1,hd:.1,a:0,y0:0,y1:1}};
          exigir(revisar({local:{...e,colocados:C.concat(bloque)},group:{traverse(){}}},B).errores.some(s=>s.includes('uso frontal:')),seed+': no detecta bloqueo de reserva');
        }finally{delete OBJETOS[objeto];}
      }finally{K.composicion_cocina=cfg;if(base)tirar(base);if(h)tirar(h);}
    }
    exigir(JSON.stringify(K)===sello,'reescribe la receta global para validar');
  });
  if(opts.tanda>=19)await caso('cocina: rollback no vacío conserva cuatro fallbacks y aleatorio íntegros',()=>{
    const K=KITS.vivienda_cocina,cfg=K.composicion_cocina;
    for(const seed of[3627,2606,4007,4216]){
      const h=H.buildVecino(seed);try{
        const e=h.estancias.find(e=>e.kit==='vivienda_cocina'),ctx={W:e.W,D:e.D,H:e.H,libres:e.libres,inicio:e.inicio,funciones:true,filtro:filtroHogar({...e.hogar,habitacion:'cocina'})};
        const A=amueblar('vivienda_cocina',e.seed,ctx);delete K.composicion_cocina;const B=amueblar('vivienda_cocina',e.seed,ctx);K.composicion_cocina=cfg;
        exigir(A.P.length>10&&!A.composicionCocina,seed+': fallback vacío o compromiso parcial');
        exigir(JSON.stringify(A.P)===JSON.stringify(B.P)&&JSON.stringify(A.activas)===JSON.stringify(B.activas)&&A.guardias===B.guardias&&A.U([0,1])===B.U([0,1]),seed+': rollback modifica P/activas/guardas/RNG');
      }finally{K.composicion_cocina=cfg;tirar(h);}
    }
    const h=H.buildVecino(2786);try{
      const e=h.estancias.find(e=>e.kit==='vivienda_cocina'),banda=e.colocados.find(p=>p.obj.startsWith('va_banda_'));
      const ctx={W:e.W,D:e.D,H:e.H,libres:e.libres.concat(banda.v),inicio:e.inicio,funciones:true,filtro:filtroHogar({...e.hogar,habitacion:'cocina'})};
      const A=amueblar('vivienda_cocina',e.seed,ctx);delete K.composicion_cocina;const B=amueblar('vivienda_cocina',e.seed,ctx);K.composicion_cocina=cfg;
      exigir(A.P.length>=4&&!A.composicionCocina&&!A.P.some(p=>p.obj.startsWith('va_banda_')||p.obj.startsWith('va_guardar_')),'reserva alta se ignora o vacía todo el programa');
      exigir(JSON.stringify(A.P)===JSON.stringify(B.P)&&A.U([0,1])===B.U([0,1]),'rechazo por hueco cambia rollback/RNG');
      delete K.composicion_cocina;
      const limpio={...ctx,libres:e.libres},old=amueblar('vivienda_cocina',e.seed,limpio),objetivo=old.P.find(p=>p.sop!=null&&['va_encimera','va_encimera_amplia','va_alacena','va_lavadora'].includes(old.P[p.sop]?.obj)),o=OBJETOS[objetivo.obj],prev=o.interaccion;
      try{o.interaccion='__uso_futuro';K.composicion_cocina=cfg;const nuevo=amueblar('vivienda_cocina',e.seed,limpio);delete K.composicion_cocina;const referencia=amueblar('vivienda_cocina',e.seed,limpio);
        exigir(nuevo.P.length>10&&!nuevo.composicionCocina&&JSON.stringify(nuevo.P)===JSON.stringify(referencia.P)&&nuevo.U([0,1])===referencia.U([0,1]),'retira dependiente funcional o altera rollback');
      }finally{if(prev===undefined)delete o.interaccion;else o.interaccion=prev;K.composicion_cocina=cfg;}
    }finally{K.composicion_cocina=cfg;tirar(h);}
  });
  if(opts.tanda>=19)await caso('cocina: nicho, vajilla y pan conservan apoyos sin penetración interna',()=>{
    const EPS=1e-6,ids=Object.keys(OBJETOS).filter(id=>/^va_(guardar_|banda_|preparar_pan)/.test(id));
    const auditar=id=>{const o=OBJETOS[id],P=partes({obj:id,x:0,y:0,z:0,ry:0}),err=[];
      for(let i=0;i<P.length;i++){
        for(let j=i+1;j<P.length;j++)if(penetra(P[i],P[j])>EPS)err.push('solape'+i+'/'+j);
        if(!['ceramica','comida'].includes(o.partes[i].m)||P[i].y0<EPS)continue;
        const v=P[i];if(!P.some((a,j)=>j!==i&&Math.abs(a.y1-v.y0)<EPS&&a.cx-a.hw<=v.cx-v.hw+EPS&&a.cx+a.hw>=v.cx+v.hw-EPS&&a.cz-a.hd<=v.cz-v.hd+EPS&&a.cz+a.hd>=v.cz+v.hd-EPS))err.push('apoyo'+i);
      }return err;
    };
    exigir(ids.length===13,'familias nuevas incompletas');for(const id of ids)exigir(!auditar(id).length,id+': '+auditar(id).join(';'));
    const pan=OBJETOS.va_preparar_pan,original=structuredClone(pan.partes),taza=OBJETOS.va_guardar_liso,save=structuredClone(taza.partes);
    try{pan.partes[1].p[1]+=.036;exigir(auditar(pan.id).includes('apoyo1'),'no detecta pan flotante');taza.partes.at(-1).p[0]=taza.partes.at(-2).p[0];exigir(auditar(taza.id).some(s=>s.startsWith('solape')),'no detecta taza dentro de platos');}
    finally{pan.partes=original;taza.partes=save;}
  });
