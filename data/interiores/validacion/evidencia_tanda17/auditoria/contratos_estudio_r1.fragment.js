  if(opts.tanda>=20)await caso('estudio: programa adulto completo, apoyos y usos en tres marcos reales',async()=>{
    const B=await(await fetch('/data/quality_budgets.json')).json();
    for(const seed of[3244,1594,1481]){
      const h=H.buildVecino(seed);try{
        const e=h.estancias.find(e=>e.kit==='vivienda_estudio'),C=e?.colocados||[];
        const mesa=C.find(p=>p.obj==='vb_puesto_estudio_amplio'),bajo=C.find(p=>p.obj==='vb_guardado_estudio'),biblioteca=C.find(p=>p.obj==='vb_biblioteca_estudio');
        exigir(mesa&&bajo&&biblioteca,seed+': falta programa adulto de trabajo/consulta');
        const silla=C.find(p=>p.de===C.indexOf(mesa)&&OBJETOS[p.obj].rol==='silla');
        exigir(silla,seed+': puesto sin asiento frontal ligado');
        exigir(bajo.de===C.indexOf(mesa)&&biblioteca.de===C.indexOf(bajo),seed+': relación mesa/bajo/biblioteca perdida en la muestra');
        const pantallas=C.filter(p=>p.obj==='vb_ordenador');
        exigir(pantallas.length===1&&pantallas[0].sop===C.indexOf(mesa)&&OBJETOS.vb_ordenador.clase==='PICKUP',seed+': pantalla duplicada o sin apoyo/identidad independiente');
        for(const p of C)if(p.sop!=null)exigir(OBJETOS[C[p.sop]?.obj]?.superficies?.[p.sup],seed+': superficie de apoyo ausente');
        exigir(e.ancho===.8,seed+': rebaja paso doméstico');
        const r=revisar({local:e,group:{traverse(){}}},B);exigir(!r.errores.length,seed+': '+r.errores.join('; '));
        exigir(!revisarUso(h).errores.length,seed+': uso real inaccesible');
        let mallas=0;h.group.traverse(o=>{if(o.isMesh&&o.visible)mallas++;});exigir(mallas<=B.interior.mallas_max,seed+': presupuesto global excedido');
        const sinBiblioteca={...e,colocados:C.filter(p=>p!==biblioteca)};
        exigir(revisar({local:sinBiblioteca,group:{traverse(){}}},B).errores.some(s=>s.includes('obligatorio:')&&s.includes('vb_biblioteca_estudio')),seed+': acepta estudio sin biblioteca obligatoria');
      }finally{tirar(h);}
    }
  });
  if(opts.tanda>=20)await caso('estudio: caller real entrega mesa y pinta su pared con huecos',()=>{
    const proto=HouseBuilder.prototype,add=proto.add,mat=proto.mat;
    let planos=[],materiales=new Map();
    proto.mat=function(...args){const key=mat.apply(this,args);if(key.startsWith('acabado_domestico_'))materiales.set(key,this.mats.get(key));return key;};
    proto.add=function(key,geo,x,y,z,ry=0){
      if(key.startsWith('acabado_domestico_')&&geo.type==='PlaneGeometry')planos.push({key,x:this.ox+x,y,z:this.oz+z,ry,w:geo.parameters.width,h:geo.parameters.height,ny:geo.attributes.normal.getY(0)});
      return add.call(this,key,geo,x,y,z,ry);
    };
    try{for(const[seed,color]of[[3244,'#657b71'],[1594,'#637b86'],[1481,'#81735e']]){
      planos=[];materiales=new Map();let h;
      try{
        h=H.buildVecino(seed,{x:-5200,z:-5200});
        const e=h.estancias.find(e=>e.kit==='vivienda_estudio'),mesa=e?.colocados.find(p=>p.obj==='vb_puesto_estudio_amplio');exigir(mesa,seed+': falta mesa del caller');
        const x0=e.origen.x-e.W/2,x1=e.origen.x+e.W/2,z0=e.origen.z,z1=z0+e.D,y=e.origen.y;
        const dentro=p=>p.x>=x0-1e-6&&p.x<=x1+1e-6&&p.z>=z0-1e-6&&p.z<=z1+1e-6&&p.y>=y-1e-6&&p.y<=y+e.H+1e-6;
        const paredes=planos.filter(p=>dentro(p)&&Math.abs(p.ny)<1e-6),acento='acabado_domestico_'+color,cal='acabado_domestico_#e9e3d4';
        exigir(paredes.length>=4&&materiales.has(acento)&&materiales.has(cal),seed+': faltan paredes reales de estudio');
        let area=0;const opuestas=new Set();
        for(const p of paredes){
          const uso=Math.sin(p.ry)*Math.sin(mesa.ry)+Math.cos(p.ry)*Math.cos(mesa.ry)>.999;
          exigir(p.key===(uso?acento:cal),seed+': acento no sigue orientación de mesa real');
          if(uso)area+=p.w*p.h;else opuestas.add(Math.round(Math.sin(p.ry))+','+Math.round(Math.cos(p.ry)));
        }
        exigir(area>.5&&opuestas.size>=3,seed+': falta paño de uso o tres paredes claras');
        exigir(planos.some(p=>dentro(p)&&p.key===cal&&p.ny<-.99&&Math.abs(p.y-(y+e.H-.008))<1e-6),seed+': techo no pertenece a esta planta/estancia');
      }finally{if(h)tirar(h);}
    }}finally{proto.add=add;proto.mat=mat;}
  });
  if(opts.tanda>=20)await caso('estudio: fallback no vacio conserva programa y paso en marco pequeño fijo',async()=>{
    const B=await(await fetch('/data/quality_budgets.json')).json(),K=KITS.vivienda_estudio,id='vivienda___estudio_individual_contrato';
    const hogar={perfil:'estudiante',estilo:'joven',botin:H.PROFILES.estudiante.loot,habitacion:'estudio'},ctx={W:3.2,D:2.8,H:2.75,libres:[{cx:-.75,cz:.5,hw:.58,hd:.5,a:0,y0:0,y1:2.4}],inicio:{x:-.75,z:.5}};
    let h;
    try{
      h=buildLocal('vivienda_estudio',4,{x:-5200,z:-5200},'Contrato de estudio',hogar,ctx);
      const e=h.local,C=e.colocados;
      exigir(e.W===3.2&&e.D===2.8&&e.H===2.75&&e.puertaX===-.75&&e.ancho===.8,'se altera marco/puerta/paso del caso4');
      for(const id of['vb_puesto_estudio_amplio','vb_guardado_estudio','vb_biblioteca_estudio','vb_ordenador'])exigir(C.some(p=>p.obj===id),'falta '+id+' en fallback pequeño');
      exigir(C.some(p=>p.obj==='vb_biblioteca_estudio'&&p.regla==='contra_pared'),'no ejercita recuperación de biblioteca en otra pared');
      exigir(!revisar(h,B).errores.length,'programa individual inválido: '+revisar(h,B).errores.join('; '));
      exigir(e.seed===4&&!e.generacion?.agotado,'se pierde solicitada4 o agota programa pequeño');
      const seed=e.generacion?.semillaEfectiva??e.seed,con={...ctx,filtro:filtroHogar(hogar)};
      const A=amueblar('vivienda_estudio',seed,con);
      const biblioteca=A.P.find(p=>p.obj==='vb_biblioteca_estudio'),frente=espacioFrontal(biblioteca,caja(biblioteca.obj),[.75,.8]);
      const M=mapaPaso({W:A.W,D:A.D,zonas:A.zonas,tabiques:A.tabiques},A.P.flatMap(partes),.05,.8,ctx.inicio);
      const celda=(x,z)=>Math.floor(z/M.S)*M.nx+Math.floor((x+A.W/2)/M.S),entrada=celda(ctx.inicio.x,ctx.inicio.z),uso=celda(frente.cx,frente.cz);
      exigir(M.free[entrada]===1&&M.reach[entrada]===1&&M.free[uso]===1&&M.reach[uso]===1,'entrada o frente de biblioteca sin paso real .80');
      KITS[id]={...K,objetos:K.objetos.map(({grupo_pared,...e})=>e)};
      const I=amueblar(id,seed,con);
      exigir(A.P.length>4&&JSON.stringify(A.P)===JSON.stringify(I.P)&&JSON.stringify(A.activas)===JSON.stringify(I.activas),'rechazo de grupo cambia receta individual o la vacía');
      exigir(A.U([0,1])===I.U([0,1])&&A.U([0,1])===I.U([0,1]),'rechazo de grupo consume RNG compartido');
    }finally{delete KITS[id];if(h)tirar(h);}
  });
