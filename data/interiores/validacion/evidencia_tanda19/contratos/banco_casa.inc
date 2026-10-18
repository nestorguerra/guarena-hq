      const bancos=e.colocados.filter(p=>p.obj==='vb_banco_equipo_campo');
      exigir(bancos.length===(seed===2162?0:1),seed+': banco canónico ausente o presente bajo13m2');
      for(const p of bancos){
        const ob=OBJETOS[p.obj],entry=K.objetos[p.e];
        exigir(entry.obligatorio===false&&entry.si_no===false&&entry.area_min===13&&entry.grupo_pared==='guardado_campo'&&p.de===bajo.i&&cerca(p.ry,bajo.ry),seed+': banco pierde condición optativa o relación');
        const[lateral,fondo]=rot(p.v.cx-bajo.v.cx,p.v.cz-bajo.v.cz,-bajo.ry);exigir(cerca(Math.abs(lateral),p.v.hw+bajo.v.hw+.04,1e-5)&&Math.abs(fondo)<.12,seed+': banco fuera de frente modular');
        exigir(ob.rol==='silla'&&ob.clase==='CARRY'&&ob.asientos?.length===1,seed+': banco sin asiento propio');
        const st=ob.asientos[0],[sx,sz]=rot(st.p[0],st.p[2],p.ry),registrado=h.pieces.seat.filter(s=>Math.hypot(s.x-e.origen.x-p.x-sx,s.z-e.origen.z-p.z-sz)<1e-6&&cerca(s.h,p.ry));
        exigir(registrado.length===1&&registrado[0].chair,seed+': banco sin registro real de asiento');
        const asiento=solido(ob.partes.find(q=>q.m==='tela'&&q.d[0]>.6)).bounds;
        exigir(cerca(st.p[1],asiento.max.y)&&st.p[0]>asiento.min.x&&st.p[0]<asiento.max.x&&st.p[2]>asiento.min.z&&st.p[2]<asiento.max.z,seed+': punto de asiento fuera de cojín');
        const reserva=espacioFrontal(p,caja(p.obj),entry.espacio_frontal);exigir(reserva&&entry.espacio_frontal[0]>=.70&&entry.espacio_frontal[1]>=.65,seed+': banco sin reserva frontal');
        exigir(e.colocados.filter(q=>q.i!==p.i).flatMap(partes).every(q=>penetra(q,reserva)<=.005)&&e.libres.every(q=>penetra(q,reserva)<=.005),seed+': reserva banco ocupada');
        // Punto literal, sin buscar una celda vecina que repare una obstrucción.
        const[fx,fz]=rot(st.p[0],caja(p.obj).z1+.4,p.ry),front={x:p.x+fx,z:p.z+fz};
        const acceso=extra=>{const m=mapaPaso(e,[...e.colocados.flatMap(partes),...extra],.05,.8,e.inicio),i=Math.floor((front.x+e.W/2)/m.S),j=Math.floor(front.z/m.S),c=j*m.nx+i;return i>=0&&i<m.nx&&j>=0&&j<m.nz&&m.free[c]&&m.reach[c];};
        exigir(acceso([])&&Math.hypot(fx-sx,fz-sz)<1.25,seed+': banco sin selección accesible con paso80');
        exigir(!acceso([{cx:front.x,cz:front.z,hw:.15,hd:.15,a:0,y0:0,y1:1}]),'negativo frente banco bloqueado aceptado');
      }
