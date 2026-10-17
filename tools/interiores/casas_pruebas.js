// Pruebas de contrato: ejercitan los constructores reales; los kits alterados se restauran siempre.
import * as H from '/src/houses.js';
import { KITS, OBJETOS } from '/src/interiores_datos.js';
import { filtroHogar, amueblar } from '/src/locales.js';
import { validarCasas, revisarUso, revisar } from '/tools/interiores/validar.js';
import * as THREE from 'three';
import { construir, caja } from '/src/objetos.js';

const exigir = (ok, mensaje) => { if (!ok) throw new Error(mensaje); };
const tirar = (h) => h.group.traverse((o) => { if (o.isMesh) o.geometry.dispose(); });

export async function probarCasas(opts = {}) {
  const pruebas = [], errores = [];
  const caso = async (nombre, fn) => {
    try { await fn(); pruebas.push({ nombre, estado: 'PASS' }); }
    catch (e) { pruebas.push({ nombre, estado: 'FAIL', motivo: String(e.message || e) }); errores.push(nombre + ': ' + String(e.message || e)); }
  };
  if(opts.tanda>=10)await caso('grupo ramificado respeta referencia inmediata y si_no sin alterar fallback',()=>{
    const id='__grupo_rama',base=KITS.vivienda_cocina,objetos=[
      {zona:'estancia',regla:'contra_pared',obj:'va_cocina',pared:'N',cantidad:[1,1],obligatorio:true,grupo_pared:'frente'},
      {zona:'estancia',regla:'junto_a',obj:'va_encimera',de:'va_cocina',cantidad:[1,1],obligatorio:true,si_no:false,grupo_pared:'frente'},
      {zona:'estancia',regla:'junto_a',obj:'va_nevera',de:'va_cocina',cantidad:[1,1],obligatorio:true,si_no:false,grupo_pared:'frente'},
    ];
    const ctx={W:8,D:4,H:2.75};
    try{for(const seed of [1,37,81]){
      KITS[id]={...base,objetos};const A=amueblar(id,seed,ctx);
      KITS[id]={...base,objetos:objetos.map(({grupo_pared,...e})=>e)};const B=amueblar(id,seed,ctx);
      exigir(JSON.stringify(A.P)===JSON.stringify(B.P)&&JSON.stringify(A.activas)===JSON.stringify(B.activas),seed+': la rama se convirtió en una cadena ajena a de');
      exigir(A.U([0,1])===B.U([0,1]),seed+': rechazar la rama consume el aleatorio compartido');
    }
    objetos[2].de=['va_cocina','va_encimera'];KITS[id]={...base,objetos};
    const A=amueblar(id,37,ctx);
    exigir(A.P.length===3,'rechaza la cadena inmediata válida');
    for(const p of A.P.filter(p=>p.e>0)){
      const ref=A.P[p.de];exigir(ref&&ref.e===p.e-1,'de no apunta al vecino inmediato');
      const a=p.v,b=ref.v;
      exigir(Math.abs(Math.abs(a.cx-b.cx)-a.hw-b.hw-.04)<.001,'referencia de separada de su vecino');
    }
    }finally{delete KITS[id];}
  });
  if(opts.tanda>=10)await caso('el grupo rechaza el hueco aislado y compromete tres entradas originales',()=>{
    const id='__grupo_frente',base=KITS.vivienda_cocina,objetos=[
      {zona:'estancia',regla:'contra_pared',obj:'va_cocina',pared:'N',cantidad:[1,1],obligatorio:true,grupo_pared:'frente'},
      {zona:'estancia',regla:'junto_a',obj:'va_encimera',de:'va_cocina',cantidad:[1,1],obligatorio:true,grupo_pared:'frente'},
      {zona:'estancia',regla:'junto_a',obj:'va_nevera',de:['va_cocina','va_encimera'],cantidad:[1,1],obligatorio:true,buscar_refs:true,grupo_pared:'frente'},
    ];
    KITS[id]={...base,objetos};
    try{
      const total=objetos.reduce((a,e)=>a+caja(e.obj).w,0)+.08,W=total*2+1,D=4.5;
      const barrera={cx:-W/2+.03+caja('va_cocina').w+.18,cz:D-.4,hw:.12,hd:.4,a:0,y0:0,y1:3};
      const ctx={W,D,H:2.75,libres:[barrera],inicio:{x:0,z:.5},funciones:true};
      const A=amueblar(id,37,ctx),B=amueblar(id,37,ctx);
      exigir(A.P.length===3&&JSON.stringify(A.P)===JSON.stringify(B.P),'el frente no es completo o determinista');
      exigir(JSON.stringify(A.activas)==='[0,1,2]','pierde entradas activas');
      for(const [i,e] of objetos.entries())exigir(A.P.filter(p=>p.e===i&&p.obj===e.obj).length===1,'entrada perdida o duplicada '+i);
      exigir(A.P.every(p=>Math.abs(p.ry-Math.PI)<1e-8&&p.v.cx-p.v.hw>barrera.cx+barrera.hw),'se acepta el hueco que sólo admite el fuego');
      const sorted=[...A.P].sort((a,b)=>a.v.cx-b.v.cx);
      for(let i=1;i<sorted.length;i++)exigir(Math.abs((sorted[i].v.cx-sorted[i].v.hw)-(sorted[i-1].v.cx+sorted[i-1].v.hw)-.04)<.001,'frente discontinuo');
      KITS[id]={...base,objetos:objetos.map(({grupo_pared,...e})=>e)};
      const previo=amueblar(id,37,ctx);exigir(previo.P[0].v.cx<barrera.cx,'la prueba no reproduce la primera elección incompleta');
    }finally{delete KITS[id];}
  });
  if(opts.tanda>=10)await caso('grupo imposible conserva colocación individual y estado aleatorio',()=>{
    const id='__grupo_fallback',base=KITS.vivienda_cocina,objetos=[
      {zona:'estancia',regla:'contra_pared',obj:'va_cocina',pared:'*',cantidad:[1,1],obligatorio:true,grupo_pared:'frente'},
      {zona:'estancia',regla:'junto_a',obj:'va_encimera',de:'va_cocina',cantidad:[1,1],obligatorio:true,grupo_pared:'frente'},
      {zona:'estancia',regla:'junto_a',obj:'va_nevera',de:['va_cocina','va_encimera'],cantidad:[1,1],obligatorio:true,grupo_pared:'frente'},
      {zona:'estancia',regla:'suelo_libre',variantes:['va_cesto_ropa','va_cajas_apiladas'],cantidad:[0,1]},
    ];
    try{for(const seed of [1,2,3,37,81]){
      KITS[id]={...base,objetos};const A=amueblar(id,seed,{W:2.1,D:2.1,H:2.75});
      KITS[id]={...base,objetos:objetos.map(({grupo_pared,...e})=>e)};const B=amueblar(id,seed,{W:2.1,D:2.1,H:2.75});
      exigir(JSON.stringify(A.P)===JSON.stringify(B.P)&&JSON.stringify(A.activas)===JSON.stringify(B.activas),seed+': cambia el fallback compacto');
      exigir(A.U([0,1])===B.U([0,1]),seed+': la búsqueda fallida consume el aleatorio compartido');
    }}finally{delete KITS[id];}
  });
  if(opts.tanda>=10)await caso('frentes reales completos respetan obligatorios y accesos',()=>{
    const pres={interior:{triangulos_max:Infinity,mallas_max:Infinity,luces_max:Infinity}};
    for(const seed of [2786,3244,1594]){const h=H.buildVecino(seed);try{
      const e=h.estancias.find(e=>e.kit==='vivienda_cocina'),frente=e.colocados.filter(p=>KITS.vivienda_cocina.objetos[p.e]?.grupo_pared==='frente_trabajo');
      exigir(frente.length===3&&new Set(frente.map(p=>p.e)).size===3,seed+': frente sin tres entradas distintas');
      exigir(frente.every(p=>Math.abs(p.ry-frente[0].ry)<.001),seed+': el frente sigue disperso');
      const r=revisar({local:e,group:{traverse(){}}},pres);exigir(!r.errores.length,seed+': '+r.errores.join('; '));
      const a=frente[0].ry,tx=Math.cos(a),tz=-Math.sin(a),nx=Math.sin(a),nz=Math.cos(a);
      const vistas=frente.map(p=>({s:p.v.cx*tx+p.v.cz*tz,w:p.v.hw,b:p.v.cx*nx+p.v.cz*nz-p.v.hd})).sort((a,b)=>a.s-b.s);
      exigir(Math.max(...vistas.map(v=>v.b))-Math.min(...vistas.map(v=>v.b))<.01,seed+': módulos fuera de la misma pared');
      for(let i=1;i<vistas.length;i++)exigir(Math.abs((vistas[i].s-vistas[i].w)-(vistas[i-1].s+vistas[i-1].w)-.04)<.01,seed+': separación del frente');
    }finally{tirar(h);}}
  });
  await caso('selecciona dormitorio, pintura y taller sin confundirlos', () => {
    exigir(typeof H.kitDeEstancia === 'function', 'falta la selección compartida de kits');
    for (const [tipo, perfil, esperado] of [
      ['dorm', 'familia', 'vivienda_dormitorio'], ['dorm2', 'familia', 'vivienda_dormitorio'],
      ['taller', 'artista', 'vivienda_pintura'], ['taller', 'agricultor', 'vivienda_taller'],
      ['hall', 'familia', null], ['pasillo', 'abuela', null],
    ]) exigir(H.kitDeEstancia(tipo, perfil) === esperado, tipo + '/' + perfil + ': kit equivocado');
  });
  await caso('el filtro de dormitorio no coloca muebles exclusivos de otra habitacion', () => {
    const filtro = filtroHogar({ perfil: 'familia', estilo: 'alegre', botin: [], habitacion: 'dorm2' });
    exigir(!filtro({ habitacion: ['dorm'] }), 'una entrada del dormitorio principal se activa en el secundario');
    exigir(filtro({ habitacion: ['dorm2'] }) && filtro({}), 'rechaza entradas aplicables');
  });
  await caso('la cobertura cuenta tambien habitaciones sin kit', async () => {
    const [r] = await validarCasas([1000]);
    exigir(r.cobertura && r.cobertura.habitables > 1, 'no informa la cobertura de todas las habitaciones');
    exigir(r.cobertura.porKit + r.cobertura.faltantes.length === r.cobertura.habitables, 'la cobertura pierde habitaciones');
  });
  await caso('exigir todas detecta un kit ausente aunque el mobiliario anterior funcione', async () => {
    const anterior = KITS.vivienda_bano;
    try {
      delete KITS.vivienda_bano;
      const [r] = await validarCasas([1000], { exigirTodas: true });
      exigir(r.errores.some((e) => e.includes('vivienda_bano')), 'devuelve verde con el baño sin kit');
    } finally { if (anterior) KITS.vivienda_bano = anterior; }
  });
  await caso('un kit fallido conserva el diagnostico y hace fallar la validacion', async () => {
    const anterior = KITS.vivienda_salon;
    try {
      KITS.vivienda_salon = { ...anterior, objetos: null };
      const h = H.buildVecino(1000);
      try { exigir(h.fallosKit && h.fallosKit.some((e) => e.kit === 'vivienda_salon' && e.motivo), 'se ha ocultado la causa del retorno al mobiliario anterior'); }
      finally { tirar(h); }
      const [r] = await validarCasas([1000]);
      exigir(r.errores.some((e) => e.includes('vivienda_salon')), 'el fallo de un kit instalado no bloquea la aceptación');
    } finally { KITS.vivienda_salon = anterior; }
  });
  if ((opts.tanda || 0) >= 1) {
    await caso('tanda 1: cama apoyada y mesita junto al cabecero; espejo sobre lavabo', () => {
      const cama = OBJETOS.vb_cama_doble;
      exigir(cama.partes.some(p=>p.p[1]-p.d[1]/2<.01 && p.p[2]>.4), 'la cama no apoya los pies en el suelo');
      const A = amueblar('vivienda_dormitorio',37,{W:6,D:5,H:2.75,filtro:filtroHogar({perfil:'familia',estilo:'alegre',habitacion:'dorm',botin:[]})});
      const b=A.P.find(p=>OBJETOS[p.obj].rol==='cama_doble'), m=A.P.find(p=>p.obj==='vb_mesita');
      exigir(b && m && Math.hypot(b.x-m.x,b.z-m.z)<1.35, 'mesita ausente o lejos de la cama');
      const B=amueblar('vivienda_bano',37,{W:5,D:3,H:2.75});
      const l=B.P.find(p=>['va_lavabo','va_lavabo_amplio'].includes(p.obj)), e=B.P.find(p=>OBJETOS[p.obj].rol==='espejo');
      exigir(l && e && Math.hypot(l.x-e.x,l.z-e.z)<.4 && Math.abs(l.ry-e.ry)<.01, 'espejo ausente o separado del lavabo');
    });
    await caso('tanda 1: las casas no superponen pantalla heredada y lámpara del kit', () => {
      const h=H.buildVecino(1000);
      try { h.group.traverse(o=>{
        if(!o.isMesh || !o.visible || !o.userData.lamp) return;
        const x=o.position.x, z=o.position.z;
        exigir(!h.rooms.some(r=>h.estancias.some(e=>e.sala===r.id)&& x>r.x0&&x<r.x1&&z>r.z0&&z<r.z1), 'pantalla heredada visible en habitación por kit');
      }); } finally { tirar(h); }
    });
    await caso('tanda 1: cocina, baño y dormitorio se montan en casas reales', async () => {
      const res = await validarCasas([1000,1037,1074,1111,1148,1185], { exigirKits: ['vivienda_salon','vivienda_cocina','vivienda_bano','vivienda_dormitorio'] });
      exigir(res.every(r => !r.errores.length), res.flatMap(r=>r.errores).slice(0,5).join('; '));
    });
    await caso('tanda 1: los muebles conservan sueño, comida, nevera y ocultacion', () => {
      for (const seed of [1000,1037,1074,1111,1148,1185]) {
        const h = H.buildVecino(seed);
        try {
          exigir(h.pieces.kitchen.length > 0, seed + ': sin cocina funcional');
          exigir(h.inter.some(i=>i.type==='fridge'), seed + ': sin nevera funcional');
          for (const rm of h.rooms.filter(r=>r.type==='dorm' || r.type==='dorm2')) {
            exigir(h.pieces.bed.some(b=>b.rm.id===rm.id), seed + '/' + rm.id + ': sin cama funcional');
            if (rm.type==='dorm') exigir(h.pieces.bed.some(b=>b.rm.id===rm.id && b.double), seed + ': dormitorio principal sin cama doble');
          }
          exigir(h.inter.some(i=>i.type==='hide'), seed + ': sin armario para ocultarse');
          exigir(h.loot.filter(i=>i.id==='colchon').length <= 1, seed + ': ahorros duplicados');
        } finally { tirar(h); }
      }
    });
  }
  if ((opts.tanda || 0) >= 2) {
    await caso('tanda 2: comedor, niños, joven, estudio y despacho por kit', async () => {
      const res=await validarCasas(Array.from({length:40},(_,i)=>1000+37*i),{exigirKits:['vivienda_comedor','vivienda_ninos','vivienda_joven','vivienda_estudio','vivienda_despacho']});
      exigir(res.every(r=>!r.errores.length),res.flatMap(r=>r.errores).slice(0,5).join('; '));
    });
    await caso('tanda 2: camas, mesa y asientos, escritorio y lectura por habitación', () => {
      for(let seed=1000;seed<2500;seed+=37) {
        const h=H.buildVecino(seed);
        try {
          for(const rm of h.rooms) {
            if(['ninos','dormJoven'].includes(rm.type)) exigir(h.pieces.bed.some(b=>b.rm.id===rm.id),seed+'/'+rm.type+': falta cama');
            if(['comedor','estudio','despacho','ninos','dormJoven'].includes(rm.type)) {
              exigir(h.pieces.table.some(t=>t.rm.id===rm.id),seed+'/'+rm.type+': falta mesa');
              exigir(h.pieces.seat.some(t=>t.rm.id===rm.id),seed+'/'+rm.type+': falta asiento');
            }
            if(['estudio','despacho'].includes(rm.type)) {
              const e=h.estancias.find(e=>e.sala===rm.id);
              exigir(e && e.colocados.some(c=>OBJETOS[c.obj].rol==='libros'),seed+'/'+rm.type+': falta lectura');
            }
          }
          const ids=h.loot.map(l=>l.id);
          exigir(new Set(ids).size===ids.length,seed+': botín duplicado');
          exigir(ids.every(id=>h.profile.loot.includes(id)),seed+': botín ajeno al perfil');
        } finally { tirar(h); }
      }
    });
  }
  if ((opts.tanda || 0) >= 3) {
    await caso('tanda 3: ninguna habitación de vecinos vuelve al mobiliario anterior', async () => {
      const res=await validarCasas(Array.from({length:40},(_,i)=>1000+37*i),{exigirTodas:true});
      exigir(res.every(r=>!r.errores.length),res.flatMap(r=>r.errores).slice(0,5).join('; '));
    });
    await caso('tanda 3: instrumentos, pintura, costura y botín del cazador', () => {
      const vistas=new Set();
      for(let seed=1000;seed<5000;seed+=37) {
        const h=H.buildVecino(seed);
        try {
          for(const rm of h.rooms) {
            if(['hall','pasillo'].includes(rm.type))continue;
            const kid=H.kitDeEstancia(rm.type,h.profile.id),e=h.estancias.find(e=>e.sala===rm.id);
            exigir(e && e.kit===kid,seed+'/'+rm.type+': kit incorrecto');vistas.add(kid);
            if(rm.type==='musica') exigir(e.colocados.some(c=>OBJETOS[c.obj].rol==='piano')&&e.colocados.some(c=>OBJETOS[c.obj].rol==='guitarra'),'música sin instrumentos utilizables');
          }
          if(h.profile.id==='cazador' && h.rooms.some(r=>r.type==='trofeos')) exigir(h.loot.some(l=>l.id==='rifle'),'trofeos sin rifle del perfil');
          const ids=h.loot.map(l=>l.id);exigir(new Set(ids).size===ids.length,'botín repetido');
          exigir(ids.every(id=>h.profile.loot.includes(id)),'botín de otro hogar');
        } finally {tirar(h);}
      }
      for(const k of ['pintura','taller','costura','musica','trofeos','trastero','despensa'])exigir(vistas.has('vivienda_'+k),'sin muestra de '+k);
    });
  }
  if ((opts.tanda || 0) >= 4) {
    await caso('integración: un cuadro accesible en hall o pasillo no es una habitación sin kit',()=>{
      for(const seed of [1013,1703]){const h=H.buildVecino(seed);try{const r=revisarUso(h);exigir(!r.errores.length,r.errores.join('; '));exigir(r.puntos.some(p=>['hall','pasillo'].includes(p.sala)&&p.tipo==='loot'&&p.ok),'no se ha comprobado el botín del paso');}finally{tirar(h);}}
    });
    await caso('integración: comida, nevera, ocultación, cajones y despertar alcanzables', () => {
      for(let seed=1000;seed<2500;seed+=37){const h=H.buildVecino(seed);try {const r=revisarUso(h);exigir(!r.errores.length,seed+': '+r.errores.slice(0,3).join('; '));}finally{tirar(h);}}
    });
    await caso('integración: la casa completa respeta mallas, luces y montaje', async () => {
      const res=await validarCasas([1000,1037,1074,1111,1148,1185],{exigirTodas:true});
      for(const r of res){
        exigir(Number.isFinite(r.mallas)&&Number.isFinite(r.luces)&&Number.isFinite(r.montaje_ms),'faltan mediciones de casa completa');
        exigir(r.mallas<=60&&r.luces<=9&&r.montaje_ms<=1500,r.seed+': presupuesto de casa excedido '+JSON.stringify({mallas:r.mallas,luces:r.luces,ms:r.montaje_ms}));
      }
    });
  }
  if ((opts.tanda || 0) >= 5) {
    await caso('acabado: cocina amplia con mesa y joven con tele apoyada y sofá',()=>{
      for(const seed of [1594,1851,2813,3244]){
        const h=H.buildVecino(seed);try{for(const e of h.estancias){
          if(e.kit==='vivienda_cocina'&&e.W*e.D>17)exigir(e.colocados.some(p=>['va_mesa_comedor','mesa_camilla'].includes(p.obj)),seed+': cocina amplia sin mesa');
          if(e.kit==='vivienda_joven'&&e.W*e.D>30){
            exigir(e.colocados.some(p=>p.obj==='televisor_plano'&&p.sop!=null),seed+': TV ausente o en el suelo');
            exigir(e.colocados.some(p=>p.obj==='sofa_dos_plazas'),seed+': rincón joven sin sofá');
            const tele=e.colocados.find(p=>p.obj==='televisor_plano'),sofa=e.colocados.find(p=>p.obj==='sofa_dos_plazas');exigir(Math.cos(tele.ry-sofa.ry)<-.9,seed+': sofá no orientado hacia TV');
          }
        }}finally{tirar(h);}
      }
    });
    await caso('acabado: el color de catálogo solo se convierte una vez a lineal',()=>{
      const g=construir([{obj:'vb_armario',x:0,z:0,seed:1}]);
      try {const m=g.children.find(m=>m.geometry?.attributes.color),esperado=new THREE.Color(OBJETOS.vb_armario.partes[0].c);exigir(Math.abs(m.geometry.attributes.color.getX(0)-esperado.r)<.00001,'la madera se oscurece por una conversión sRGB duplicada');}
      finally{g.traverse(m=>m.geometry?.dispose());}
    });
    await caso('acabado: dos lienzos de semillas distintas conservan sus dibujos',()=>{
      const gs=[1,2].map(seed=>construir([{obj:'vb_caballete',x:0,z:0,seed}]));
      try {const images=gs.map(g=>g.children.find(m=>m.material.map)?.material.map.image.toDataURL());exigir(images[0]&&images[1]&&images[0]!==images[1],'la caché repite el mismo lienzo en todos los caballetes');}
      finally{gs.forEach(g=>g.traverse(m=>m.geometry?.dispose()));}
    });
    await caso('Annie: habitaciones renovadas sin perder escalera ni funciones propias',async()=>{
      const {buildAnnieHouse}=await import('/src/interiors.js');
      const h=buildAnnieHouse(12,{x:-9700,z:-9700});
      try {
        exigir(h.estancias?.length===5&&h.personalizadas?.includes('dormitorio'),'faltan las cinco estancias por kit o el dormitorio personalizado');
        exigir(h.levels.length===2&&h.doors.length===7,'se han alterado plantas o puertas');
        exigir(Math.abs(h.floorY(-9697.4,-9692.8,0)-1.55)<.01,'ha cambiado la rampa de la escalera');
        for(const tipo of ['safe','bed','mirror','tv','drawer','fridge','eat','read','exit'])exigir(h.inter.some(i=>i.type===tipo),'Annie sin acción '+tipo);
        const caja=h.inter.find(i=>i.type==='safe');exigir(caja.y===3.1&&Math.abs(caja.x-(-9697.84))<.01,'ha cambiado la caja fuerte o su planta');
        exigir(!h.fallosKit?.length,'kit de Annie fallido');
        for(const e of h.estancias){const r=revisar({local:e,group:{traverse(){}}},{interior:{triangulos_max:Infinity,mallas_max:Infinity,luces_max:Infinity}});exigir(!r.errores.length,e.sala+': '+r.errores.join('; '));}
        // Alcance real por los colliders de cada planta; no basta con alcanzar una zona del kit aislado.
        for(const lv of [0,1]){
          const S=.1,nx=64,nz=lv?105:135,libre=new Uint8Array(nx*nz),visit=new Uint8Array(nx*nz),col=h.levels[lv];
          for(let z=0;z<nz;z++)for(let x=0;x<nx;x++){
            const p={x:h.origin.x-3.2+(x+.5)*S,z:h.origin.z+(z+.5)*S,y:lv*3.1},q={...p};
            if(lv&&x>51&&z>49&&z<94)continue;col.resolveCircle(q,.34);if(Math.hypot(q.x-p.x,q.z-p.z)<.005)libre[z*nx+x]=1;
          }
          const inicio=lv?{x:h.origin.x+2.56,z:h.origin.z+9.9}:h.spots.entrada;
          const idx=p=>Math.max(0,Math.min(nz-1,Math.floor((p.z-h.origin.z)/S)))*nx+Math.max(0,Math.min(nx-1,Math.floor((p.x-h.origin.x+3.2)/S)));
          const cola=[idx(inicio)];exigir(libre[cola[0]],'inicio de planta ocupado');visit[cola[0]]=1;
          for(let k=0;k<cola.length;k++){const c=cola[k],x=c%nx,z=Math.floor(c/nx);for(const [dx,dz] of [[1,0],[-1,0],[0,1],[0,-1]]){const xx=x+dx,zz=z+dz,j=zz*nx+xx;if(xx>=0&&xx<nx&&zz>=0&&zz<nz&&libre[j]&&!visit[j]){visit[j]=1;cola.push(j);}}}
          const cerca=(p,r)=>cola.some(c=>Math.hypot(h.origin.x-3.2+(c%nx+.5)*S-p.x,h.origin.z+(Math.floor(c/nx)+.5)*S-p.z)<=r);
          exigir(lv||cerca({x:h.origin.x+2.56,z:h.origin.z+4.6},.2),'no se alcanza el pie de la escalera');
          for(const i of h.inter.filter(i=>((i.y||0)>2?1:0)===lv))exigir(cerca(i,(i.r||.8)-.05),'acción de Annie inaccesible: '+i.type+'/'+lv);
        }
        let mallas=0;h.group.traverse(o=>{if(o.isMesh&&o.visible)mallas++;});
        exigir(mallas<=60&&h.lights.length<=9,'Annie excede presupuesto '+mallas+'/'+h.lights.length);
      }finally{tirar(h);}
    });
  }
  if(opts.tanda>=6)await caso('los revestimientos dejan libres los huecos de puertas y ventanas',async()=>{
    const {panosPared}=await import('/src/acabados_vivienda.js');
    const huecos=[[.8,1.7,0,2.1],[2,2.8,.92,2.08]],p=panosPared(0,4,0,2.95,huecos);
    const area=p.reduce((a,q)=>a+(q[1]-q[0])*(q[3]-q[2]),0);
    exigir(Math.abs(area-(4*2.95-.9*2.1-.8*1.16))<1e-8,'el revestimiento cambia el área de los huecos');
    for(const q of p)for(const h of huecos)exigir(Math.min(q[1],h[1])<=Math.max(q[0],h[0])||Math.min(q[3],h[3])<=Math.max(q[2],h[2]),'un paño tapa un hueco');
  });
  if(opts.tanda>=6)await caso('los lotes conservan el acabado sereno de los materiales domésticos',()=>{
    const h=H.buildVecino(3244,{x:-9700,z:-9700});
    try{let n=0;h.group.traverse(o=>{if(o.isMesh&&o.material?.defines?.CLAY_RELIEF===.12)n++;});exigir(n>0,'la agrupación ha perdido los parámetros de relieve y contraste del material');}finally{tirar(h);}
  });
  if(opts.tanda>=7)await caso('el bisel conserva la envolvente física de una pieza',()=>{
    const id='prueba_bisel_temporal';OBJETOS[id]={partes:[{f:'caja',d:[1,1,1],p:[0,.5,0],c:'#b99770',m:'madera',redondeo:.04}]};
    let g;try{g=construir([{obj:id,x:0,y:0,z:0,ry:0}]);g.updateMatrixWorld(true);const b=new THREE.Box3().setFromObject(g);exigir(Math.abs(b.min.x+.5)<1e-6&&Math.abs(b.max.x-.5)<1e-6&&Math.abs(b.min.y)<1e-6&&Math.abs(b.max.y-1)<1e-6,'el bisel altera el volumen que usa la colisión');let n=0;g.traverse(o=>{if(o.isMesh)n+=(o.geometry.index?o.geometry.index.count:o.geometry.attributes.position.count)/3;});exigir(n===108,'el coste geométrico del bisel no coincide con el catálogo');}finally{if(g)tirar({group:g});delete OBJETOS[id];}
  });
  if(opts.tanda>=8)await caso('la luz por habitación se restaura y respeta apagones',async()=>{
    const {prepararLuzVivienda}=await import('/src/luz_vivienda.js');
    const h=H.buildVecino(3244,{x:-9700,z:-9700});
    try{
      const rm=h.rooms.find(r=>r.type==='bano'),cam={position:new THREE.Vector3((rm.x0+rm.x1)/2,(rm.lv||0)*3.1+1.6,(rm.z0+rm.z1)/2)},antes=h.lights.map(l=>[l.intensity,l.castShadow]);
      const fin=prepararLuzVivienda(h,cam);exigir(h.lights.filter(l=>l.castShadow).length===1,'más de una luz puntual con sombras por vista');
      exigir(h.lights.some((l,i)=>l.intensity<antes[i][0]),'no se limita el relleno de habitaciones vecinas');fin();
      exigir(h.lights.every((l,i)=>l.intensity===antes[i][0]&&l.castShadow===antes[i][1]),'el render altera permanentemente las lámparas');
      for(const l of h.lights)l.intensity=0;const f=prepararLuzVivienda(h,cam);f();exigir(h.lights.every(l=>l.intensity===0),'el render enciende una lámpara apagada');
    }finally{tirar(h);}
  });
  if(opts.tanda>=8)await caso('el cruce entre dos luces no produce un salto de brillo',async()=>{
    const {prepararLuzVivienda}=await import('/src/luz_vivienda.js');
    const lights=[-1,1].map(x=>{const l=new THREE.PointLight(0xffffff,10,8);l.position.set(x,2.6,0);return l;});
    const h={kind:'vecino',group:new THREE.Group(),lights,rooms:[]};
    const muestra=x=>{const fin=prepararLuzVivienda(h,{position:new THREE.Vector3(x,1.6,0)}),r=lights.map(l=>({i:l.intensity,s:l.castShadow?l.shadow.intensity:0}));fin();return r;};
    const a=muestra(-.001),b=muestra(.001);
    exigir(a.every((v,i)=>Math.abs(v.i-b[i].i)<.02),'un desplazamiento de 2 mm intercambia bruscamente las intensidades');
    exigir([...a,...b].every(v=>v.s<.01),'la sombra cambia de origen sin desvanecerse en el cruce');
  });
  if(opts.tanda>=9)await caso('las cocinas usan unidades domésticas sin bloques de stock comercial',()=>{
    for(const seed of [2786,3244,1594]){
      const h=H.buildVecino(seed,{x:-9700,z:-9700});
      try{const e=h.estancias.find(e=>e.kit==='vivienda_cocina');exigir(e&&!e.colocados.some(p=>p.obj.startsWith('prod_')),seed+': una cocina contiene hileras o bloques de stock de tienda');}finally{tirar(h);}
    }
    const a=caja('va_alimento_arroz');exigir(a.w<.12&&a.d<.08,'la unidad de arroz conserva la envolvente del lote comercial');
  });
  if(opts.tanda>=9)await caso('costura conserva el asiento frente al puesto de trabajo',()=>{
    for(const seed of [2606,4216,3981]){const h=H.buildVecino(seed,{x:-9700,z:-9700});try{const e=h.estancias.find(e=>e.kit==='vivienda_costura'),m=e?.colocados.find(p=>p.obj.startsWith('va_costura')),s=e?.colocados.find(p=>p.obj==='silla_comedor');exigir(m&&s&&Math.hypot(m.x-s.x,m.z-s.z)<1.1,seed+': asiento alejado del puesto de costura');exigir(Math.sin(m.ry)*(s.x-m.x)+Math.cos(m.ry)*(s.z-m.z)>.35,seed+': silla detrás del puesto');exigir(m.regla==='contra_pared',seed+': panel de carretes sin pared detrás');}finally{tirar(h);}}
  });
  if(opts.tanda>=9)await caso('la oclusión doméstica conserva el exterior y restaura cada vista',async()=>{
    const {prepararOclusionVivienda}=await import('/src/luz_vivienda.js');
    const U={radius:{value:2},thickness:{value:2.5},scale:{value:1.7}},ao={enabled:true,gtaoMaterial:{uniforms:U}},grade={uniforms:{uAO:{value:1}}},cam={position:{x:0,z:0}};
    const fuera=prepararOclusionVivienda({kind:'bar'},cam,ao,grade);exigir(U.radius.value===2&&grade.uniforms.uAO.value===1,'el comercio cambia');fuera();
    const fin=prepararOclusionVivienda({kind:'vecino',origin:{x:0,z:0}},cam,ao,grade);exigir(U.radius.value===.85&&grade.uniforms.uAO.value===.85,'no se acota la sombra de contacto');fin();
    exigir(U.radius.value===2&&U.thickness.value===2.5&&U.scale.value===1.7&&grade.uniforms.uAO.value===1,'la siguiente vista hereda ajustes domésticos');
    ao.enabled=false;prepararOclusionVivienda({kind:'annie'},cam,ao,grade)();exigir(U.radius.value===2&&grade.uniforms.uAO.value===1,'se altera la oclusión desactivada');
  });
  if(opts.tanda>=9)await caso('los umbrales de superficie conservan los muebles esenciales',()=>{
    for(const [kit,limite,ids] of [['cocina',14,['va_cocina','va_cocina_amplia']],['bano',10,['va_lavabo','va_lavabo_amplio']],['taller',10.5,['va_banco','va_banco_carpinteria','va_banco_mecanica','va_banco_amplio','va_banco_carpinteria_amplio','va_banco_mecanica_amplio']]]){
      for(const area of [limite-.0005,limite,limite+.0005]){const A=amueblar('vivienda_'+kit,37,{W:4,D:area/4,H:2.75});exigir(A.P.filter(p=>ids.includes(p.obj)).length===1,kit+'/'+area+': falta el mueble esencial en el umbral');}
    }
    const patas=OBJETOS.va_isla_cocina.partes.filter(p=>p.f==='caja'&&p.d[1]===.08&&p.p[1]===.04);exigir(new Set(patas.map(p=>p.p[0]+':'+p.p[2])).size===4,'la isla no tiene cuatro apoyos distintos');
  });
  if(opts.tanda>=9)await caso('el puesto con silla se cuenta una vez y exige su asiento vinculado',()=>{
    const h=H.buildVecino(2606);try{const e=h.estancias.find(e=>e.kit==='vivienda_costura'),pres={interior:{triangulos_max:Infinity,mallas_max:Infinity,luces_max:Infinity}},r=revisar({local:e,group:{traverse(){}}},pres);exigir(!r.errores.length,r.errores.join('; '));const roto={...e,colocados:e.colocados.map(p=>p.obj==='silla_comedor'?{...p,de:null}:p)},rr=revisar({local:roto,group:{traverse(){}}},pres);exigir(rr.errores.some(e=>e.startsWith('asiento:')),'se acepta el puesto sin silla');}finally{tirar(h);}
  });
  if(opts.tanda>=9)await caso('el frente modular prueba el extremo libre antes de dispersarse',()=>{
    const id='__prueba_modulos',base=KITS.vivienda_cocina;
    KITS[id]={...base,objetos:[
      {zona:'estancia',regla:'contra_pared',obj:'va_cocina',pared:'N',cantidad:[1,1],centrado:true},
      {zona:'estancia',regla:'junto_a',obj:'va_encimera',de:'va_cocina',lados:['derecha'],cantidad:[1,1]},
      {zona:'estancia',regla:'junto_a',obj:'va_nevera',de:['va_cocina','va_encimera'],cantidad:[1,1],buscar_refs:true,si_no:false},
    ]};
    try{
      const A=amueblar(id,37,{W:3.3,D:3,H:2.75}),c=A.P.find(p=>p.obj==='va_cocina'),n=A.P.find(p=>p.obj==='va_nevera');
      exigir(c&&n&&Math.abs(c.ry-n.ry)<.01&&Math.abs(c.z-n.z)<.08,'la nevera no prolonga el extremo libre del frente');
      KITS[id].objetos[2].buscar_refs=false;
      exigir(!amueblar(id,37,{W:3.3,D:3,H:2.75}).P.some(p=>p.obj==='va_nevera'),'la muestra no reproduce el extremo bloqueado');
    }finally{delete KITS[id];}
  });
  if(opts.tanda>=9)await caso('un armario alto preferido se intenta sobre la encimera',()=>{
    const id='__prueba_alto',base=KITS.vivienda_cocina;
    KITS[id]={...base,objetos:[
      {zona:'estancia',regla:'contra_pared',obj:'va_encimera',pared:'N',cantidad:[1,1],centrado:true},
      {zona:'estancia',regla:'pared',obj:'va_alto_cocina',pared:'*',sobre_de:'va_encimera',cantidad:[0,1],preferir:true},
    ]};
    try{for(const seed of [1,2,3,4,5,37])exigir(amueblar(id,seed,{W:4,D:3,H:2.75}).P.some(p=>p.obj==='va_alto_cocina'),seed+': se sortea un armario que cabe y se prefiere');}
    finally{delete KITS[id];}
  });
  if(opts.tanda>=9)await caso('el inodoro conserva espacio frontal y el validador detecta su bloqueo',()=>{
    const pres={interior:{triangulos_max:Infinity,mallas_max:Infinity,luces_max:Infinity}};
    for(const seed of [2786,3244,1594]){const h=H.buildVecino(seed);try{
      const e=h.estancias.find(e=>e.kit==='vivienda_bano'),r=revisar({local:e,group:{traverse(){}}},pres);
      exigir(!r.errores.length,seed+': '+r.errores.join('; '));
      const wc=e.colocados.find(p=>p.obj==='va_inodoro'),b=caja(wc.obj),dx=Math.sin(wc.ry)*(b.z1+.3),dz=Math.cos(wc.ry)*(b.z1+.3);
      const roto={...e,colocados:e.colocados.map(p=>p.obj==='va_ducha'?{...p,x:wc.x+dx,z:wc.z+dz}:p)},rr=revisar({local:roto,group:{traverse(){}}},pres);
      exigir(rr.errores.some(e=>e.startsWith('uso frontal:')),'se acepta el inodoro bloqueado por la ducha');
    }finally{tirar(h);}}
  });
  if(opts.tanda>=10)await caso('el útil suspendido exige su referencia sólo cuando se solicita',()=>{
    const id='__prueba_pared_referencia',base=KITS.vivienda_trastero;
    KITS[id]={...base,objetos:[{zona:'estancia',regla:'pared',obj:'va_soporte_ciclismo',pared:'*',sobre_de:'va_bicicleta_guardada',cantidad:[0,1],preferir:true,si_no:false}]};
    try{
      exigir(amueblar(id,37,{W:4,D:3,H:2.75}).P.length===0,'útiles sin bicicleta en otra pared');
      delete KITS[id].objetos[0].si_no;
      exigir(amueblar(id,37,{W:4,D:3,H:2.75}).P.length===1,'se rompe el fallback anterior de otros kits');
      KITS[id].objetos[0].si_no=false;
      KITS[id].objetos.unshift({zona:'estancia',regla:'contra_pared',obj:'va_bicicleta_guardada',pared:'N',cantidad:[1,1],centrado:true});
      const P=amueblar(id,37,{W:4,D:3,H:2.75}).P,b=P.find(p=>p.obj==='va_bicicleta_guardada'),u=P.find(p=>p.obj==='va_soporte_ciclismo');
      exigir(b&&u&&Math.abs(b.ry-u.ry)<.001&&Math.abs(b.v.cx-u.v.cx)<.02,'útiles sin relación vertical con bicicleta');
      const bloqueado=amueblar(id,37,{W:4,D:3,H:2.75,libres:[u.v]}).P;
      exigir(bloqueado.some(p=>p.obj==='va_bicicleta_guardada')&&!bloqueado.some(p=>p.obj==='va_soporte_ciclismo'),'el accesorio invade la reserva o se recoloca en otra pared');
    }finally{delete KITS[id];}
  });
  if(opts.tanda>=10)await caso('las pertenencias de trastero conservan huella y apoyo',()=>{
    const a=caja('va_bicicleta_guardada'),b=caja('va_bicicleta_carga');
    exigir(b.w<=a.w+.001&&b.d<=a.d+.001&&b.h<=a.h+.001,'la variante consume más paso');
    const bolsa=OBJETOS.va_bicicleta_carga.partes.find(p=>p.tinte==='tela');
    exigir(bolsa&&Math.abs(bolsa.p[1]-bolsa.d[1]/2-.6925)<.001,'bolsa sin apoyo sobre portaequipajes');
    const piezas=OBJETOS.va_bicicleta_carga.partes,sillin=piezas.find(p=>p.f==='caja'&&p.p[0]===-.22&&p.p[1]===.865);
    exigir(sillin&&sillin.p[0]-sillin.d[0]/2-(bolsa.p[0]+bolsa.d[0]/2)>=.009,'bolsa dentro del sillín');
    const eje=piezas.find(p=>p.f==='cil'&&p.p[0]===-.45&&p.p[1]===.325&&p.d[2]>=.20&&p.r?.[0]===90);
    const tirantes=piezas.filter(p=>p.f==='cil'&&p.c==='#69776c'&&p.r?.[0]===0);
    exigir(eje&&tirantes.length===4,'portaequipajes sin eje o tirantes');
    for(const t of tirantes){const a=t.r[2]*Math.PI/180,x=t.p[0]+Math.sin(a)*t.d[2]/2,y=t.p[1]-Math.cos(a)*t.d[2]/2;
      exigir(Math.hypot(x-eje.p[0],y-eje.p[1])<=eje.d[0]+.001&&Math.abs(t.p[2]-eje.p[2])<=eje.d[2]/2,'tirante desconectado del eje');
    }
    exigir(OBJETOS.va_soporte_ciclismo.soporte==='pared'&&OBJETOS.va_soporte_pintura.soporte==='pared','se ocupó el suelo con accesorios de pared');
    exigir(caja('va_soporte_ciclismo').y0>a.y1&&caja('va_soporte_pintura').y0>caja('va_escalera_guardada').y1,'accesorios dentro de la pertenencia');
    exigir(KITS.vivienda_trastero.paso_libre>=.8,'se redujo el paso');
  });
  if(opts.tanda>=10)await caso('trastero ofrece pertenencias reproducibles sin seleccionar la ficha',()=>{
    const ids=new Set();
    for(let seed=1;seed<=24;seed++){
      const a=amueblar('vivienda_trastero',seed,{W:5,D:4,H:2.75}),b=amueblar('vivienda_trastero',seed,{W:5,D:4,H:2.75});
      exigir(JSON.stringify(a.P)===JSON.stringify(b.P),'la misma semilla cambia de pertenencias');
      for(const p of a.P)if(['va_bicicleta_guardada','va_bicicleta_carga','va_escalera_guardada'].includes(p.obj))ids.add(p.obj);
    }
    for(const id of ['va_bicicleta_guardada','va_bicicleta_carga','va_escalera_guardada'])exigir(ids.has(id),'nunca se coloca la variante '+id);
  });
  return { pruebas, errores };
}
