  if(opts.tanda>=22)await caso('junto_a: separación frontal optativa conserva default, RNG y reservas',async()=>{
    const id='__contrato_t22_frente',anterior=KITS[id],base={tipologia:'fixture_frente',superficie:{ancho:[5,5],fondo:[5,5],alto:3},puerta:0,paso_libre:.8,zonas:[{id:'estancia',publica:true,rect:['-W/2','0','W/2','D']}],objetos:[{zona:'estancia',obj:'sillon_orejero',regla:'contra_pared',pared:'N',centrado:true,cantidad:[1,1],obligatorio:true},{zona:'estancia',obj:'mesa_baja',regla:'junto_a',de:'sillon_orejero',lados:['frente'],cantidad:[1,1],obligatorio:true,si_no:false}]};
    const ctx={W:5,D:5,H:3,funciones:true,inicio:{x:0,z:.5},libres:[{cx:0,cz:.5,hw:.58,hd:.5,a:0,y0:0,y1:2.4}]};
    const run=(edit=()=>{},reservas=[])=>{KITS[id]=structuredClone(base);edit(KITS[id].objetos[1]);return amueblar(id,4,{...ctx,libres:[...ctx.libres,...reservas]});};
    const gap=A=>{exigir(A.P.length===2&&A.P[0].obj==='sillon_orejero'&&A.P[1].obj==='mesa_baja','fixture frontal vacía o incompleta');const[s,t]=A.P,[,z]=rot(t.v.cx-s.x,t.v.cz-s.z,-s.ry);return z-t.v.hd-caja(s.obj).z1;};
    try{
      const a=run(),b=run(e=>e.separacion_frontal=.06);
      exigir(JSON.stringify(a.P)===JSON.stringify(b.P)&&JSON.stringify(a.activas)===JSON.stringify(b.activas)&&a.guardias===b.guardias&&a.U([0,1])===b.U([0,1]),'default frontal altera colocación o azar');
      exigir(Math.abs(gap(a)-.06)<1e-6&&Math.abs(gap(b)-.06)<1e-6,'default frontal no mide seis cm');
      const c=run(e=>e.separacion_frontal=.38);exigir(Math.abs(gap(c)-.38)<1e-6,'holgura frontal optativa ignorada');
      const reserva={...c.P[1].v},antes=JSON.stringify(reserva),d=run(e=>e.separacion_frontal=.38,[reserva]);
      exigir(d.P.length===1&&d.P[0].obj==='sillon_orejero'&&JSON.stringify(reserva)===antes,'frente invade reserva o altera referencia');
      for(const edit of[e=>e.separacion_frontal=.01,e=>e.separacion_frontal=1.01,e=>{e.separacion_frontal=.38;e.regla='contra_pared';},e=>{e.separacion_frontal=.38;e.lados=['derecha'];},e=>{e.separacion_frontal=.38;e.grupo_pared='g';}]){
        let error=null;try{run(edit);}catch(e){error=e;}exigir(error&&String(error).includes('separacion_frontal'),'opción frontal inválida aceptada');
      }
    }finally{if(anterior===undefined)delete KITS[id];else KITS[id]=anterior;}
  });
