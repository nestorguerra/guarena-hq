(async()=>{
  const g=game,rows=[];window.__t19Trofeos=rows;
  const exigir=(ok,m)=>{if(!ok)throw Error(m);};
  const rot=(x,z,a)=>[x*Math.cos(a)+z*Math.sin(a),-x*Math.sin(a)+z*Math.cos(a)];
  const cerca=(a,b)=>Number.isFinite(a)&&Number.isFinite(b)&&Math.abs(a-b)<1e-6;
  const patrimonio=()=>JSON.stringify({money:g.player.money,bank:g.homeSafe.bank,bag:g.save.bag,decor:g.save.homeDecor,hq:localStorage.getItem('guarena_hq_save'),evo:localStorage.getItem('guarena_evo_save'),fija:localStorage.getItem('guarena_save')});
  for(const seed of[2132,4204,1679,2162]){
    const row={seed,estado:'EN_CURSO'};rows.push(row);let saved=null;
    try{
      const door=g.interiors.doors.find(d=>d.seed===seed&&!d.owner&&!d.venue&&!d.church);
      exigir(door,'puerta real ausente '+seed);
      const started=performance.now(),h=await g.interiors.enter(door,{mode:'visit',silent:true});
      exigir(h&&g.interior===h,'entrada no confirmada');row.entrada_ms=+(performance.now()-started).toFixed(1);
      exigir(row.entrada_ms<=1500,'entrada superior a1500ms');
      const e=h.estancias.find(e=>e.kit==='vivienda_trofeos');exigir(e,'sin cuarto de trofeos');
      const uno=id=>{const ps=e.colocados.filter(p=>p.obj===id);exigir(ps.length===1,'cantidad '+id);return ps[0];};
      const ar=uno('vb_armero'),bajo=uno('vb_guardado_campo'),sillon=uno('vb_sillon_campo'),mesa=uno('vb_mesa_consulta_campo');
      uno('vb_biblioteca_campo');exigir(bajo.de===ar.i&&Math.cos(bajo.ry-ar.ry)>.999999,'frente desligado');
      const gap=(mesa.v.cx-sillon.v.cx)*Math.sin(sillon.ry)+(mesa.v.cz-sillon.v.cz)*Math.cos(sillon.ry)-mesa.v.hd-sillon.v.hd;
      exigir(Math.cos(mesa.ry-sillon.ry)>.999999&&Number.isFinite(gap)&&Math.abs(gap-.32)<1e-5,'consulta sin holgura .32');
      const rifle=h.loot.filter(p=>p.id==='rifle'),prismas=h.loot.filter(p=>p.id==='prismaticos');
      exigir(rifle.length===1&&prismas.length===1&&rifle[0].sala===e.sala&&prismas[0].sala===e.sala,'pertenencias sin vínculo a sala');
      exigir(rifle[0].def.weapon==='rifle'&&rifle[0].def.ammo===12&&JSON.stringify(prismas[0].def.value)==='[20,60]','premios alterados');
      for(const type of['read','drawer'])exigir(h.inter.some(p=>p.sala===e.sala&&p.type===type),'acción ausente '+type);
      const bancos=e.colocados.filter(p=>p.obj==='vb_banco_equipo_campo');
      row.programa={perfil:h.profile.id,area:e.W*e.D,gap_real:gap,banco:bancos.length,botin:['rifle','prismaticos'],acciones:['read','drawer']};
      if(seed===2162){exigir(bancos.length===0,'2162 ganó banco');row.estado='PASS';continue;}
      exigir(bancos.length===1,'amplia sin banco único');const p=bancos[0];
      // Offset explícito del único asiento de la fixture R8; no importar /src en el paquete Pages.
      exigir(cerca(p.y,0)&&Math.abs(p.v.hd-.22)<1e-6&&cerca(p.v.a,p.ry),'fixture de banco cambió');
      const[dx,dz]=rot(-.19,.04,p.ry),sx=e.origen.x+p.x+dx,sz=e.origen.z+p.z+dz;
      const matches=h.pieces.seat.filter(s=>Math.hypot(s.x-sx,s.z-sz)<1e-6&&cerca(s.y,e.origen.y)&&cerca(s.h,p.ry)&&s.chair===true);
      exigir(matches.length===1,'asiento de banco ausente/duplicado');const seat=matches[0];
      const rm=h.rooms.find(q=>q.id===e.sala),col=h.levels?.[rm.lv]||h.collider;
      exigir(g.map.collider===col,'collider activo no corresponde a planta del banco');
      const[ax0,az0]=rot(-.19,p.v.hd+.4,p.ry),ax=e.origen.x+p.x+ax0,az=e.origen.z+p.z+az0;
      const dentro=(x,z)=>x>=e.origen.x-e.W/2+.34&&x<=e.origen.x+e.W/2-.34&&z>=e.origen.z+.34&&z<=e.origen.z+e.D-.34;
      const libre=(x,z)=>{const q={x,z},hit=col.resolveCircle(q,.34);return Math.hypot(q.x-x,q.z-z)<1e-6&&hit.depth<1e-6;};
      exigir(dentro(ax,az)&&libre(ax,az),'aproximación física ocupada/fuera de sala');
      const player=g.player;exigir(player.mode==='foot'&&!player.seat&&!g.seats.cur,'estado inicial no disponible');
      saved={pos:player.pos.clone(),vel:player.vel.clone(),heading:player.heading,input:g.input.enabled,collider:g.map.collider,patrimonio:patrimonio()};
      // Reposición privada a un punto validado; no se afirma recorrido desde la puerta.
      player.pos.set(ax,e.origen.y,az);player.vel.set(0,0,0);player.syncChar();
      const selected=g.seats.near(ax,az);exigir(selected?.ref===seat&&selected.kind==='casa','selector real elige otro asiento');
      g.seats.sit(selected);
      exigir(player.mode==='sit'&&player.seat===selected&&g.seats.cur===selected&&selected.taken,'no se sentó por la API real');
      exigir(cerca(player.pos.x,sx)&&cerca(player.pos.z,sz)&&cerca(player.pos.y,e.origen.y)&&cerca(player.heading,p.ry),'pose de asiento incorrecta');
      player.char.update(1/30,0,{});player.syncChar();g.render();
      exigir(!g.renderer.info.programs?.some(p=>p.diagnostics?.runnable===false),'shader no ejecutable sentado');
      row.asiento={x:sx,y:e.origen.y,z:sz,h:p.ry,registros:matches.length,distancia_seleccion:Math.hypot(sx-ax,sz-az),seleccion_real:true,sentado:true};
      const fx=sx+Math.sin(p.ry)*.6,fz=sz+Math.cos(p.ry)*.6;
      const frontal=g.map.collider.raycast(sx,sz,fx,fz,.5,.5)>.95&&!g.map.buildingAt(fx,fz),esperada=frontal?{x:fx,z:fz}:{x:ax,z:az};
      g.seats.standUp();
      exigir(player.mode==='foot'&&player.seat===null&&g.seats.cur===null&&!selected.taken,'no se levantó por la API real');
      exigir(cerca(player.pos.x,esperada.x)&&cerca(player.pos.z,esperada.z),'salida distinta del flujo real standUp');
      exigir(dentro(player.pos.x,player.pos.z)&&libre(player.pos.x,player.pos.z),'salida real ocupada/fuera de sala');
      exigir(g.input.enabled===saved.input&&g.map.collider===saved.collider,'controles/collider alterados');
      exigir(patrimonio()===saved.patrimonio,'acción de banco altera patrimonio/guardado');
      row.asiento.levantado=true;row.asiento.salida_libre=true;row.asiento.salida={x:player.pos.x,y:player.pos.y,z:player.pos.z,ruta:frontal?'frontal':'standPos'};
      player.pos.copy(saved.pos);player.vel.copy(saved.vel);player.heading=saved.heading;player.syncChar();
      exigir(player.pos.distanceTo(saved.pos)<1e-8,'posición fixture no restaurada');
      row.asiento.posicion_restaurada=true;row.estado='PASS';g.render();
    }catch(err){row.estado='FAIL';row.error=String(err.stack||err);}
    finally{
      try{if(g.player.mode==='sit'||g.seats.cur)g.seats.standUp();if(saved){g.player.pos.copy(saved.pos);g.player.vel.copy(saved.vel);g.player.heading=saved.heading;g.player.syncChar();}if(g.interior)g.interiors.leave(true);}
      catch(err){row.estado='FAIL';row.limpieza_error=String(err.stack||err);}
    }
  }
  return JSON.stringify({estado:rows.length===4&&rows.every(r=>r.estado==='PASS')?'PASS':'FAIL',alcance:'Cuatro puertas reales; tres bancos selección/sit/stand por métodos de producto, collider .34 y restauración; 2162 sin banco. Reposición privada al acceso; no recorrido desde entrada ni evaluación visual de animación. Residentes conservados. No compras ni recogida.',rows});
})()
