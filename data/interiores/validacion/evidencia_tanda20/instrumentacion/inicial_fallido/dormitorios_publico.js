(async()=>{
 const g=game,rows=[];window.__t20Dormitorios=rows;
 const ok=(v,m)=>{if(!v)throw Error(m)},near=(a,b)=>Number.isFinite(a)&&Number.isFinite(b)&&Math.abs(a-b)<1e-5;
 const rot=(x,z,a)=>[x*Math.cos(a)+z*Math.sin(a),-x*Math.sin(a)+z*Math.cos(a)];
 const render=()=>{g.render();ok(!g.renderer.info.programs?.some(p=>p.diagnostics?.runnable===false),'shader no ejecutable');};
 for(const seed of[2786,3244,1689,2132,5157,1594]){
  const row={seed,estado:'EN_CURSO',salas:[]};rows.push(row);let saved;
  try{
   const d=g.interiors.doors.find(d=>d.seed===seed&&!d.owner&&!d.venue&&!d.church);ok(d,'sin puerta real '+seed);
   const h=await g.interiors.enter(d,{mode:'visit',silent:true});ok(g.interior===h,'entrada no confirmada');
   const es=h.estancias.filter(e=>e.kit===(seed===1594?'vivienda_joven':'vivienda_dormitorio'));ok(es.length,'sin kit requerido');
   saved={pos:g.player.pos.clone(),vel:g.player.vel.clone(),heading:g.player.heading,input:g.input.enabled,fp:g.cam.fp,fov:g.cam.fov,fovOverride:g.cam.fovOverride};
   const L=g.interiors.life;ok(L?.people.length,'sin residente real para probar cama');const npc=L.people[0];
   for(const e of es){
    const rm=h.rooms.find(r=>r.id===e.sala),col=h.levels?.[rm.lv]||h.collider;
    const free=(x,z)=>{ok(Number.isFinite(x)&&Number.isFinite(z),'coordenada no finita');const q={x,z},hit=col.resolveCircle(q,.34);ok(Number.isFinite(hit.depth)&&hit.depth<1e-6&&Math.hypot(q.x-x,q.z-z)<1e-6,'punto de uso ocupado');};
    const beds=e.colocados.filter(p=>['vb_cama_doble','vb_cama_amplia','vb_cama_individual'].includes(p.obj));ok(beds.length,'cama compartida ausente');
    if(seed===1594)ok(beds.some(p=>p.obj==='vb_cama_individual'),'joven real sin individual');
    const r={sala:e.sala,tipo:rm.type,kit:e.kit,camas:[],ocultacion:[],lectura:null};row.salas.push(r);
    ok(!h.fallosUso?.some(x=>x.startsWith(e.sala+':')||x.startsWith(e.sala+'/')),'fallos de uso en habitación');
    for(const p of beds){
     const matches=h.pieces.bed.filter(b=>b.rm.id===e.sala&&b.indiceKit===p.i);ok(matches.length===1,'registro actual de cama ausente/duplicado');const b=matches[0];free(b.side.x,b.side.z);
     L.lieOnBed(npc,b);ok(npc.bed===b&&npc.state==='sleep'&&near(npc.y,b.y+.64),'lieOnBed real falló');
     L.wake(npc);ok(npc.state==='idle'&&near(npc.x,b.side.x)&&near(npc.z,b.side.z)&&near(npc.y,b.y),'wake real falló');free(npc.x,npc.z);
     r.camas.push({obj:p.obj,indice:p.i,actualBed:true,lieOnBed:true,wake:true,salida_libre:true});
    }
    const hides=h.inter.filter(i=>i.sala===e.sala&&i.type==='hide');ok(hides.length,'armario sin hide');
    for(const it of hides){
     free(it.x,it.z);g.player.pos.set(it.x,e.origen.y,it.z);g.player.vel.set(0,0,0);g.player.syncChar();
     g.interiors.hideIn(it);ok(g.interiors.hiding===it&&g.player.hidden&&near(g.player.pos.x,it.hx)&&near(g.player.pos.z,it.hz),'hideIn real falló');render();
     g.interiors.unhide();ok(!g.interiors.hiding&&!g.player.hidden&&near(g.player.pos.x,it.x)&&near(g.player.pos.z,it.z),'unhide real falló');free(g.player.pos.x,g.player.pos.z);ok(g.input.enabled===saved.input,'controles alterados');
     r.ocultacion.push({hideIn:true,unhide:true,salida_libre:true});
    }
    if(seed===3244){
     const chair=e.colocados.find(p=>p.obj==='sillon_orejero'),table=e.colocados.find(p=>p.obj==='mesa_auxiliar_lectura'),shelf=e.colocados.find(p=>p.obj==='estanteria_libros');ok(chair&&table&&shelf,'lectura3244 incompleta');ok(table.de===chair.i,'mesa desligada del sillón');
     // Superficies nominales exactas del catálogo activo; no se presenta como raycast de triángulos.
     const tops={mesa_auxiliar_lectura:[.555],estanteria_libros:[.04,.42,.8,1.18,1.56]},supports=[];
     for(const parent of[table,shelf]){
      const books=e.colocados.filter(p=>p.sop===parent.i&&(p.obj==='libro_tumbado'||p.obj.startsWith('lb_')||p.obj.startsWith('hilera_libros')));ok(books.length,'sin libros sobre '+parent.obj);
      for(const b of books){const y=tops[parent.obj][b.sup];ok(Number.isFinite(y)&&near(b.v.y0,(parent.y||0)+y),'libro sin apoyo nominal');supports.push({obj:b.obj,padre:parent.obj,sup:b.sup,y0:b.v.y0,apoyo_nominal:true});}
     }
     const[dx,dz]=rot(0,.08,chair.ry),sx=e.origen.x+chair.x+dx,sz=e.origen.z+chair.z+dz;
     const seats=h.pieces.seat.filter(s=>near(s.x,sx)&&near(s.z,sz)&&near(s.y,e.origen.y)&&near(s.h,chair.ry));ok(seats.length===1,'asiento de lectura no registrado exactamente');
     ok(h.inter.some(i=>i.sala===e.sala&&i.type==='read'),'sin acción read');
     r.lectura={sillon:true,mesa_vinculada:true,biblioteca:true,apoyos:supports,asiento_registros:1,accion_read:true,limite:'Registro del asiento y acción presentes; no ejecuta sentarse/leer en este bloque. Apoyos por cotas de catálogo, sin raycast.'};
    }
    render();
   }
   row.estado='PASS';
  }catch(err){row.estado='FAIL';row.error=String(err.stack||err);}
  finally{
   try{if(g.interiors.hiding)g.interiors.unhide();if(saved){g.player.pos.copy(saved.pos);g.player.vel.copy(saved.vel);g.player.heading=saved.heading;g.player.syncChar();g.cam.setFirstPerson(saved.fp);g.cam.fov=saved.fov;g.cam.fovOverride=saved.fovOverride;}if(g.interior)g.interiors.leave(true);}catch(err){row.estado='FAIL';row.limpieza_error=String(err.stack||err);}
  }
 }
 const types=new Set(rows.flatMap(r=>r.salas.map(s=>s.tipo)));
 return JSON.stringify({estado:rows.length===6&&rows.every(r=>r.estado==='PASS')&&types.has('dorm')&&types.has('dorm2')?'PASS':'FAIL',rows,alcance:'Cinco vecinos dormitorio más joven real1594; camas mediante HouseLife.lieOnBed/wake y armarios mediante hideIn/unhide. Fixture privada reposicionada; sin recorrido desde entrada, evaluación visual dentro del armario ni siesta del jugador en cama ajena. Lectura3244: enlaces, apoyos nominales y registro de asiento; no activación de leer/sentarse. Render/veto shader. Persistencia global comparada por wrapper.'});
})()
