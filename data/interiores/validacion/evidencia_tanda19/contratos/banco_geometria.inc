    // Apoyo de botas y bolsa contra los triángulos de la balda/tablero reales.
    // Se muestrea la zona plana interior de cada pieza redondeada, no sus AABB.
    const apoyoBanco=(pieza,soporte)=>{
      const q=solido(pieza).bounds,t=solido(soporte).bounds;if(Math.abs(q.min.y-t.max.y)>1e-6)return false;
      const id='__contrato_t22_apoyo_banco',prev=OBJETOS[id];let g;
      try{
        OBJETOS[id]={...OBJETOS.vb_banco_equipo_campo,partes:[soporte]};g=construir([{obj:id,x:0,y:0,z:0,ry:0}],{domestico:true});g.updateMatrixWorld(true);
        const m=(pieza.redondeo||0)+.002,xx=[q.min.x+m,q.max.x-m],zz=[q.min.z+m,q.max.z-m],ray=new THREE.Raycaster();
        return [...xx.flatMap(x=>zz.map(z=>[x,z])),[(q.min.x+q.max.x)/2,(q.min.z+q.max.z)/2]].every(([x,z])=>{ray.set(new THREE.Vector3(x,q.min.y+.01,z),new THREE.Vector3(0,-1,0));ray.far=.02;const hit=ray.intersectObject(g,true)[0];return hit&&Math.abs(hit.point.y-q.min.y)<1e-6;});
      }finally{if(g)tirar({group:g});if(prev)OBJETOS[id]=prev;else delete OBJETOS[id];}
    };
    const equipoApoyado=ps=>{
      const suelas=ps.filter(p=>p.m==='goma'),bolsa=ps.find(p=>p.m==='tela'&&p.d[1]>.15&&p.d[0]>.2&&p.d[0]<.3),balda=ps.find(p=>p.m==='madera'&&p.d[0]>1&&p.p[1]<.2),tablero=ps.find(p=>p.m==='madera'&&p.d[0]>1&&p.p[1]>.4);
      return suelas.length===2&&bolsa&&balda&&tablero&&suelas.every(p=>apoyoBanco(p,balda))&&apoyoBanco(bolsa,tablero);
    };
    exigir(equipoApoyado(OBJETOS.vb_banco_equipo_campo.partes),'banco: botas o bolsa sin apoyo físico');
    for(const modo of['botas','bolsa','fuera']){const ps=structuredClone(OBJETOS.vb_banco_equipo_campo.partes);for(const p of ps){if(modo==='botas'&&p.m==='goma')p.p[1]+=.02;if(modo==='bolsa'&&p.m==='tela'&&p.d[1]>.15&&p.d[0]>.2&&p.d[0]<.3)p.p[1]+=.02;if(modo==='fuera'&&p.m==='goma')p.p[0]+=1;}exigir(!equipoApoyado(ps),'negativo apoyo banco aceptado: '+modo);}
