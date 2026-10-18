// Pruebas de contrato: ejercitan los constructores reales; los kits alterados se restauran siempre.
import * as H from '/src/houses.js';
import { KITS, OBJETOS } from '/src/interiores_datos.js';
import { filtroHogar, amueblar, buildLocal } from '/src/locales.js';
import { validarCasas, revisarUso, revisar } from '/tools/interiores/validar.js';
import * as THREE from 'three';
import { programaLuzDomestica, HouseBuilder } from '/src/housekit.js';
import { construir, caja } from '/src/objetos.js';
import { partes, penetra, espacioFrontal } from '/src/interiores_geo.js';

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
  if(opts.tanda>=11)await caso('grupo con opcional preferido conserva fallback y aleatorio sin compromiso parcial',()=>{
    const id='__grupo_opcional',base=KITS.vivienda_bano,objetos=[
      {zona:'estancia',regla:'contra_pared',obj:'va_lavabo_amplio',pared:'N',cantidad:[1,1],obligatorio:true,grupo_pared:'aseo'},
      {zona:'estancia',regla:'junto_a',obj:'va_armario_bano',de:'va_lavabo_amplio',cantidad:[0,1],preferir:true,si_no:false,grupo_pared:'aseo'},
    ];
    const kit={...base,objetos},plain={...base,objetos:objetos.map(({grupo_pared,...e})=>e)};
    const W=caja('va_lavabo_amplio').w+.10,ctx={W,D:3,H:2.75,libres:[],inicio:{x:0,z:.5},funciones:true};
    try{for(const seed of [1,37,81]){
      KITS[id]=kit;const A=amueblar(id,seed,ctx);KITS[id]=plain;const B=amueblar(id,seed,ctx);
      exigir(JSON.stringify(A.P)===JSON.stringify(B.P)&&JSON.stringify(A.activas)===JSON.stringify(B.activas),'grupo fallido altera fallback '+seed);
      exigir(A.U([0,1])===B.U([0,1]),'grupo fallido consume RNG '+seed);
      exigir(A.P.some(p=>p.obj==='va_lavabo_amplio')&&!A.P.some(p=>p.obj==='va_armario_bano'),'no conserva el armario opcional omitido');
    }
    KITS[id]=kit;const A=amueblar(id,37,{...ctx,W:4});
    const l=A.P.find(p=>p.obj==='va_lavabo_amplio'),a=A.P.find(p=>p.obj==='va_armario_bano');
    exigir(l&&a&&a.e===1&&A.P[a.de]===l,'no coloca el opcional preferido con su referencia');
    exigir(Math.abs(Math.abs(a.v.cx-l.v.cx)-a.v.hw-l.v.hw-.04)<.001,'armario separado del lavabo');
    exigir(!objetos[1].obligatorio&&objetos[1].cantidad[0]===0,'convierte el armario en obligatorio');
    }finally{delete KITS[id];}
  });
  if(opts.tanda>=11)await caso('el grupo de aseo rechaza un rincón sin pared para su toalla',()=>{
    const id='__aseo_pared_toalla',base=KITS.vivienda_bano,objetos=[
      {zona:'estancia',regla:'contra_pared',obj:'va_lavabo_amplio',pared:'N',cantidad:[1,1],obligatorio:true,grupo_pared:'aseo',reserva_lateral:{obj:'va_toallero',lado:'izquierda'}},
      {zona:'estancia',regla:'junto_a',obj:'va_armario_bano',de:'va_lavabo_amplio',cantidad:[0,1],preferir:true,si_no:false,grupo_pared:'aseo'},
      {zona:'estancia',regla:'junto_a',obj:'va_toallero',de:'va_lavabo_amplio',cantidad:[1,1],obligatorio:true,lados:['izquierda'],si_no:false},
    ];
    const ctx={W:3.8,D:3,H:2.75,libres:[],inicio:{x:0,z:.5},funciones:true};
    try{
      KITS[id]={...base,objetos};const A=amueblar(id,37,ctx);
      exigir(A.P.length===3&&A.P.some(p=>p.obj==='va_toallero'),'pierde toalla al aceptar la primera pareja');
      const l=A.P.find(p=>p.obj==='va_lavabo_amplio'),t=A.P.find(p=>p.obj==='va_toallero');
      exigir(Math.abs(l.ry-t.ry)<.001,'manda la toalla a otra pared');
      KITS[id]={...base,objetos:objetos.map(({reserva_lateral,...e})=>e)};const B=amueblar(id,37,ctx);
      exigir(!B.P.some(p=>p.obj==='va_toallero'),'la muestra no reproduce el rincón sin reserva');
    }finally{delete KITS[id];}
  });
  if(opts.tanda>=11)await caso('banos grandes conservan conjuntos de aseo, espejo y reserva frontal WC',()=>{
    const pres={interior:{triangulos_max:Infinity,mallas_max:Infinity,luces_max:Infinity}};
    for(const seed of [2786,3244,1594]){const h=H.buildVecino(seed);try{
      const e=h.estancias.find(e=>e.kit==='vivienda_bano');exigir(e,'sin bano '+seed);
      const l=e.colocados.find(p=>['va_lavabo','va_lavabo_amplio'].includes(p.obj)),m=e.colocados.find(p=>OBJETOS[p.obj].rol==='espejo');
      exigir(l&&m&&Math.hypot(l.x-m.x,l.z-m.z)<.4&&Math.abs(l.ry-m.ry)<.01,'espejo sin relacion '+seed);
      exigir(e.colocados.some(p=>p.obj==='va_inodoro')&&e.colocados.some(p=>p.obj==='va_ducha')&&e.colocados.some(p=>p.obj==='va_toallero'),'pierde un sanitario/toalla obligatorio '+seed);
      const r=revisar({local:e,group:{traverse(){}}},pres);exigir(!r.errores.length,seed+': '+r.errores.join('; '));
      if(e.W*e.D>=10){
        const a=e.colocados.find(p=>p.obj==='va_armario_bano');exigir(a,'muestra grande sin armario '+seed);
        const tx=Math.cos(l.ry),tz=-Math.sin(l.ry),nx=Math.sin(l.ry),nz=Math.cos(l.ry);
        const sep=Math.abs((a.v.cx-l.v.cx)*tx+(a.v.cz-l.v.cz)*tz)-a.v.hw-l.v.hw;
        const respaldo=p=>p.v.cx*nx+p.v.cz*nz-p.v.hd;
        exigir(Math.abs(a.ry-l.ry)<.001&&Math.abs(sep-.04)<.01&&Math.abs(respaldo(a)-respaldo(l))<.01,'aseo sigue disperso '+seed);
        const b=e.colocados.find(p=>p.obj==='va_banera');exigir(b,'muestra grande pierde banera '+seed);
        const t=e.colocados.find(p=>p.obj==='va_toallero'),d=e.colocados.find(p=>p.obj==='va_ducha');
        const separacion=(p,q)=>Math.abs((p.v.cx-q.v.cx)*Math.cos(q.ry)-(p.v.cz-q.v.cz)*Math.sin(q.ry))-p.v.hw-q.v.hw;
        exigir(Math.abs(t.ry-l.ry)<.001&&Math.abs(separacion(t,l)-.04)<.01,'toalla fuera del conjunto de aseo '+seed);
        exigir(Math.abs(d.ry-b.ry)<.001&&Math.abs(separacion(d,b)-.04)<.01,'ducha y banera siguen dispersas '+seed);
      }
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
      for(const area of [limite-.0005,limite,limite+.0005]){const A=amueblar('vivienda_'+kit,37,{W:4,D:area/4,H:2.75});exigir(A.P.filter(p=>ids.includes(kit==='cocina'?p.obj.replace(/_(rustico|liso|vajillero)$/,''):p.obj)).length===1,kit+'/'+area+': falta el mueble esencial en el umbral');}
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
  if(opts.tanda>=12)await caso('trastero compone pareja alta y baja antes de prolongar el almacenaje',()=>{
    const K=KITS.vivienda_trastero;
    exigir(K.objetos[0].regla==='contra_pared'&&K.objetos[1].regla==='junto_a'&&K.objetos[1].buscar_refs,'no prioriza la pareja');
    exigir(K.objetos[1].obligatorio&&K.objetos[1].si_no!==false,'pierde el fallback del obligatorio');
    const id='__trastero_pareja',ctx={W:5,D:4,H:2.75,libres:[],inicio:{x:0,z:1},funciones:true};
    const entradas=K.objetos.slice(0,2).map(e=>({...e}));entradas[0]={...entradas[0],pared:'N',obj:'va_estante_trastero_0',variantes:undefined};entradas[1]={...entradas[1],obj:'va_bicicleta_guardada',variantes:undefined};
    const junto=(a,b)=>Math.abs(a.ry-b.ry)<.001&&Math.abs(Math.abs(a.v.cx-b.v.cx)-a.v.hw-b.v.hw-.04)<.001;
    try{
      KITS[id]={...K,objetos:entradas};const A=amueblar(id,37,ctx),B=amueblar(id,37,ctx);
      exigir(A.P.length===2&&junto(A.P[0],A.P[1]),'pareja separada con pared libre');
      exigir(JSON.stringify(A.P)===JSON.stringify(B.P),'pareja no reproducible');
      const alto=A.P[0],bajo=A.P[1];exigir(alto.v.y1>1.9&&bajo.v.y1<1.1,'no hay volúmenes de dos alturas');
      const libres=[{...bajo.v,y0:0,y1:2.4}];
      const C=amueblar(id,37,{...ctx,libres});
      exigir(C.P.length===2&&!C.P.some(p=>p.obj==='va_bicicleta_guardada'&&junto(C.P[0],p)),'el obligatorio no conserva otra pared ante hueco reservado');
      const todas=[{cx:0,cz:2,hw:2.5,hd:2,a:0,y0:0,y1:3}];
      exigir(amueblar(id,37,{...ctx,libres:todas}).P.length===0,'fuerza piezas en sala completamente reservada');
    }finally{delete KITS[id];}
  });
  if(opts.tanda>=11)await caso('altos de cocina proporcionados, estilos excluyentes y huecos protegidos',()=>{
    const familias={rustico:'',antiguo:'',joven:'_liso',moderno:'_liso',lujo:'_liso',bohemio:'_abierto',alegre:'_abierto'};
    for(const [estilo,sufijo] of Object.entries(familias))for(const [W,D,amplio] of [[3,4,false],[5,4,true]]){
      const filtro=filtroHogar({perfil:'familia',estilo,habitacion:'cocina',botin:[]});
      const activas=KITS.vivienda_cocina.objetos.filter(e=>e.obj?.startsWith('va_alto_cocina')&&filtro(e)&&!(e.area_min!=null&&W*D<e.area_min)&&!(e.area_max!=null&&W*D>=e.area_max));
      exigir(activas.length===1&&activas[0].obj==='va_alto_cocina'+sufijo+(amplio?'_amplio':''),'selección ambigua de alto '+estilo);
      const b=caja(activas[0].obj),bajo=caja(amplio?'va_encimera_amplia':'va_encimera');
      exigir(b.w<=bajo.w&&b.w/bajo.w>.90&&b.y0>1.2&&b.y1<2.2,'alto fuera de proporción o paso');
    }
    const id='__alto_cocina_hueco';try{
      for(const estilo of Object.keys(familias)){
        const alto=KITS.vivienda_cocina.objetos.find(e=>e.obj==='va_alto_cocina'+familias[estilo]+'_amplio');
        KITS[id]={...KITS.vivienda_cocina,objetos:[{zona:'estancia',regla:'contra_pared',obj:'va_encimera_amplia',pared:'N',cantidad:1,centrado:true},alto]};
        const ctx={W:5,D:4,H:2.75,filtro:filtroHogar({perfil:'familia',estilo,habitacion:'cocina',botin:[]})};
        const A=amueblar(id,37,ctx),u=A.P.find(p=>p.obj===alto.obj);exigir(u,'falta alto con pared libre '+estilo);
        const B=amueblar(id,37,{...ctx,libres:[u.v]});exigir(!B.P.some(p=>p.obj===alto.obj),'invade reserva de ventana '+estilo);
        KITS[id].objetos=[alto];exigir(amueblar(id,37,ctx).P.length===0,'alto huérfano sin preparación');
      }
    }finally{delete KITS[id];}
  });
  if(opts.ninos||opts.tanda>=13)await caso('infantil 5045 y fichas conservan puesto unido, usos y paso real',()=>{
    for(const seed of [4007,5045,1296]){
      const h=H.buildVecino(seed,{x:0,z:0});
      try{
        const e=h.estancias.find(e=>e.kit==='vivienda_ninos'),C=e.colocados;
        const mi=C.findIndex(p=>p.obj==='vb_mesa_ninos'),s=C.filter(p=>p.obj==='vb_silla_ninos');
        exigir(mi>=0&&s.length===1&&s[0].de===mi&&s[0].e===C[mi].e,seed+': silla dispersa o ausente');
        const m=C[mi],b=caja(m.obj),sb=caja(s[0].obj),dx=s[0].x-m.x,dz=s[0].z-m.z;
        exigir(Math.abs(dx*Math.cos(m.ry)-dz*Math.sin(m.ry))<.001,'silla fuera del eje de la mesa');
        exigir(Math.abs(dx*Math.sin(m.ry)+dz*Math.cos(m.ry)-(b.z1+sb.d/2+.06))<.001,'separación frontal alterada');
        exigir(e.ancho===.8,'paso reducido');
        exigir(h.pieces.bed.some(p=>p.rm.id===e.sala)&&h.pieces.table.some(p=>p.rm.id===e.sala)&&h.pieces.seat.some(p=>p.rm.id===e.sala),'función cama, mesa o asiento perdida');
        exigir(h.inter.some(p=>p.sala===e.sala&&p.type==='hide'),'interacción del armario perdida');
        exigir(!revisarUso(h).errores.some(x=>x.startsWith(e.sala+'/')),'uso infantil inaccesible');
        for(const id of ['vb_cama_ninos','vb_armario_ninos','vb_osito','vb_bloques'])exigir(C.some(p=>p.obj===id),'obligatorio perdido '+id);
      }finally{tirar(h);}
    }
  });
  if(opts.ninos||opts.tanda>=13)await caso('infantil conserva volumen, roles y reservas negativas del puesto',()=>{
    const b=caja('vb_cama_ninos'),a=caja('vb_cama_individual');
    exigir(b.w>=a.w-.00001&&b.d>=a.d-.00001,'cama encogida');
    exigir(OBJETOS.vb_cama_ninos.rol==='cama'&&OBJETOS.vb_armario_ninos.rol==='armario'&&OBJETOS.vb_estante_ninos.rol==='libros','rol perdido');
    const w=caja('vb_armario_ninos');exigir(w.h>=1.49&&w.h<1.51&&.95*.42*1.5>=.8*.4*1.85,'armario sin volumen de ropa');
    const id='__ninos_puesto';try{
      const puesto=KITS.vivienda_ninos.objetos.find(e=>e.silla_frontal);
      KITS[id]={...KITS.vivienda_ninos,objetos:[{...puesto,pared:'N',centrado:true}]};
      const ctx={W:3,D:2.15,H:2.75,funciones:true},A=amueblar(id,37,ctx);
      exigir(A.P.length===2&&A.P[1].de===0,'puesto libre incompleto');
      const frontal=[{cx:0,cz:1.38,hw:1.5,hd:.2,a:0,y0:0,y1:1.5}];
      exigir(amueblar(id,37,{...ctx,libres:frontal}).P.length===0,'acepta mesa sin hueco para su silla');
      const reservas=[{cx:0,cz:1.075,hw:1.5,hd:1.075,a:0,y0:0,y1:3}],B=amueblar(id,37,{...ctx,libres:reservas});
      exigir(B.P.length===0,'fuerza puesto dentro de reserva');
    }finally{delete KITS[id];}
  });
  if(opts.tanda>=13)await caso('despensa: cada envase cabe bajo las baldas reales de sus soportes',async()=>{
    const {partes,penetra,superficie}=await import('/src/interiores_geo.js');
    // Recorre el pool completo, no sólo las variantes sorteadas en tres fotografías.
    // La tapa superior también cuenta: su hueco puede ser menor que el paso entre baldas.
    let comprobados=0;
    for(const e of KITS.vivienda_despensa.objetos.filter(e=>e.regla==='sobre'))for(const sid of e.en){
      const soporte=partes({obj:sid,x:0,y:0,z:0,ry:0});
      for(let k=0;k<OBJETOS[sid].superficies.length;k++){
        const s=superficie(sid,k);if(!s)continue;
        for(const id of e.variantes||[e.obj]){
          const b=caja(id);if(b.w>s.x1-s.x0||b.d>s.z1-s.z0)continue;
          const it={obj:id,x:(s.x0+s.x1-b.x0-b.x1)/2,z:(s.z0+s.z1-b.z0-b.z1)/2,y:s.y-b.y0,ry:0};
          const piezas=partes(it);comprobados++;
          exigir(piezas.every(p=>soporte.every(q=>penetra(p,q)<=.0001)),id+' atraviesa '+sid+' en superficie '+k);
        }
      }
    }
    exigir(comprobados>0,'no se comprobó ningún envase sobre baldas');
  });
  if(opts.tanda>=13)await caso('despensa: fichas, perfiles y fallback conservan el programa obligatorio',async()=>{
    const {partes,penetra}=await import('/src/interiores_geo.js'),K=KITS.vivienda_despensa;
    for(const seed of [2786,1689,2132]){
      const h=H.buildVecino(seed,{x:0,z:0});try{
        const e=h.estancias.find(e=>e.kit==='vivienda_despensa');exigir(e,seed+': falta despensa');
        const C=e.colocados;
        for(const id of ['va_estante','aparador',...(e.W*e.D>=14?['va_cajas_apiladas']:[])])exigir(C.some(p=>p.obj===id),seed+': falta '+id);
        exigir(e.ancho>=.8&&!revisarUso(h).errores.some(x=>x.startsWith(e.sala+'/')),seed+': programa inaccesible');
        for(const p of C.filter(p=>p.sop!=null)){
          const soporte=C[p.sop];exigir(soporte&&OBJETOS[soporte.obj].superficies[p.sup],seed+': apoyo inexistente');
          exigir(Math.abs(p.v.y0-(soporte.y+OBJETOS[soporte.obj].superficies[p.sup].y))<.001,seed+': envase sin apoyo');
          exigir(partes(p).every(a=>partes(soporte).every(b=>penetra(a,b)<=.0001)),seed+': '+p.obj+' atraviesa su soporte');
        }
      }finally{tirar(h);}
    }
    for(const perfil of ['agricultor','cazador','matrimonio','familia','estudiante','artista','anciana']){
      const activas=K.objetos.filter(e=>e.regla==='sobre'&&e.en?.includes('aparador')&&filtroHogar({perfil,estilo:'rustico',habitacion:'despensa'})(e));
      exigir(activas.length===1,perfil+': desayuno/provisión duplicado o ausente');
      const ids=activas[0].variantes||[activas[0].obj],campo=['agricultor','cazador'].includes(perfil);
      exigir(ids.includes(campo?'va_alimento_garrafa_aceite':'va_alimento_pan_molde')&&!ids.includes(campo?'va_alimento_pan_molde':'va_alimento_garrafa_aceite'),perfil+': filtro de exclusión invertido');
    }
    const id='__despensa_fallback';try{
      // El frente no cabe en esta pared de 2 m; los muebles esenciales sí caben en otras.
      KITS[id]={...K,objetos:K.objetos.map((e,i)=>i===0?{...e,pared:'N',centrado:true}:e)};
      for(const area of [13.999,14,14.001]){
        const ctx={W:2,D:area/2,H:2.75,funciones:true},A=amueblar(id,37,ctx),B=amueblar(id,37,ctx);
        exigir(JSON.stringify(A.P)===JSON.stringify(B.P),'fallback no reproducible');
        const estante=A.P.find(p=>p.obj==='va_estante'),bajo=A.P.find(p=>p.obj==='aparador');
        exigir(estante&&bajo&&Math.abs(Math.sin(estante.ry-bajo.ry))>.9,'no se ejercita fallback a otra pared');
        const cajas=A.activas.filter(i=>K.objetos[i].obj==='va_cajas_apiladas');
        exigir(cajas.length===1,'entradas de cajas solapadas o hueco en umbral');
        exigir(!!K.objetos[cajas[0]].obligatorio===(area>=14),'mínimo de cajas incorrecto en '+area);
        if(area>=14)exigir(A.P.some(p=>p.obj==='va_cajas_apiladas'),'cajas obligatorias ausentes');
      }
      const libres=[{cx:0,cz:3.5,hw:1,hd:3.5,a:0,y0:0,y1:2.4}];
      exigir(amueblar(id,37,{W:2,D:7,H:2.75,funciones:true,libres}).P.filter(p=>p.regla!=='techo').length===0,'el fallback fuerza piezas dentro de una reserva total');
    }finally{delete KITS[id];}
  });
  if(opts.tanda>=14)await caso('identidad infantil conserva dibujos distintos y variación textil al montar',()=>{
    const grupos=[],crear=(obj,seed,paleta)=>{const g=construir([{obj,x:0,y:0,z:0,ry:0,seed,paleta}],{domestico:true});grupos.push(g);return g;};
    const mapas=g=>{const out=[];g.traverse(o=>{if(o.isMesh&&o.material.map)out.push(o.material.map);});return out;};
    try{
      const a=mapas(crear('vb_dibujos_ninos',1)),b=mapas(crear('vb_dibujos_ninos',18));
      exigir(a.length===3&&new Set(a).size===3,'la galería reutiliza una textura para dibujos distintos');
      exigir(new Set(a.map(t=>t.image.toDataURL())).size===3,'las tres texturas dibujan la misma imagen');
      exigir(b.length===3&&a.every((t,i)=>t===b[i]),'la misma lámina/semilla equivalente pierde la caché');
      const rugs=[1,2,3].map(seed=>mapas(crear('vb_alfombra_juego',seed)));
      exigir(rugs.every(a=>a.length===1)&&new Set(rugs.map(a=>a[0].image.toDataURL())).size===3,'la alfombra pierde sus tres paletas');
      const colores=g=>{const out=[];g.traverse(o=>{if(o.isMesh&&o.geometry.attributes.color)out.push(Array.from(o.geometry.attributes.color.array));});return JSON.stringify(out);};
      const paleta={tela:['#aa3333','#3344aa']};
      exigir(colores(crear('vb_cama_ninos',2,paleta))!==colores(crear('vb_cama_ninos',3,paleta)),'la colcha ignora la tela de la casa');
      for(const [id,ref] of [['vb_cama_ninos','vb_cama_individual'],['vb_alfombra_juego','vb_alfombra']]){
        const a=caja(id),b=caja(ref);for(const k of ['x0','x1','y0','y1','z0','z1'])exigir(Math.abs(a[k]-b[k])<.00001,id+': cambia la envolvente '+k);
      }
    }finally{
      // Geometrías y materiales de lámina son propios; caché de texturas y mate son compartidos.
      for(const g of grupos)g.traverse(o=>{if(o.isMesh){o.geometry.dispose();if(o.material.map)o.material.dispose();}});
    }
  });
  if(opts.tanda>=14)await caso('galería infantil sigue la cama y respeta paredes bloqueadas',()=>{
    const id='__infantil_galeria',K=KITS.vivienda_ninos,galeria=K.objetos.find(e=>e.obj==='vb_dibujos_ninos');
    exigir(galeria,'falta la entrada de galería');
    try{
      for(const pared of ['N','S','E','W']){
        KITS[id]={...K,objetos:[{zona:'estancia',regla:'contra_pared',obj:'vb_cama_ninos',pared,cantidad:1,centrado:true},galeria]};
        const ctx={W:4,D:4,H:2.75,funciones:true},A=amueblar(id,37,ctx),c=A.P.find(p=>p.obj==='vb_cama_ninos'),g=A.P.find(p=>p.obj==='vb_dibujos_ninos');
        exigir(c&&g,pared+': no coloca cama y galería en pared libre');
        exigir(g.v.y0>c.v.y1&&g.v.y1<2.1&&g.v.hw<=c.v.hw,pared+': galería invade cama o sale de escala');
        exigir(Math.abs(Math.sin(g.ry-c.ry))<.001&&Math.cos(g.ry-c.ry)>.99,pared+': galería mira al lado incorrecto');
        exigir(Math.abs((g.v.cx-c.v.cx)*Math.cos(c.ry)-(g.v.cz-c.v.cz)*Math.sin(c.ry))<.001,pared+': galería descentrada');
        const b=caja(g.obj),lx=(b.x0+b.x1)/2,lz=b.z0,x=g.x+lx*Math.cos(g.ry)+lz*Math.sin(g.ry),z=g.z-lx*Math.sin(g.ry)+lz*Math.cos(g.ry),Z=A.zonas.estancia;
        const apoyo=Math.min(Math.abs(x-Z.x0),Math.abs(x-Z.x1),Math.abs(z-Z.z0),Math.abs(z-Z.z1));
        exigir(apoyo<.01,pared+': galería flotando lejos de pared');
        const B=amueblar(id,37,{...ctx,libres:[g.v]});
        exigir(B.P.some(p=>p.obj==='vb_cama_ninos')&&!B.P.some(p=>p.obj==='vb_dibujos_ninos'),pared+': galería invade hueco o se dispersa');
        exigir(JSON.stringify(A.P)===JSON.stringify(amueblar(id,37,ctx).P),'galería no reproducible');
      }
      KITS[id]={...K,objetos:[galeria]};
      exigir(amueblar(id,37,{W:4,D:4,H:2.75}).P.length===0,'galería huérfana sin cama');
    }finally{delete KITS[id];}
  });
  if(opts.tanda>=16)await caso('comedor doméstico ofrece mesa y sillas reales, comida servida y paso',()=>{
    for(const seed of [2786,5157,2606]){
      const h=H.buildVecino(seed,{x:0,z:0});try{
        const e=h.estancias.find(e=>e.kit==='vivienda_comedor');exigir(e,seed+': falta comedor');
        const C=e.colocados,mesas=C.map((p,i)=>({p,i})).filter(({p})=>['va_mesa_comedor','va_mesa_familiar'].includes(p.obj));
        exigir(mesas.length===1,seed+': mesa principal ausente o duplicada');const {p:mesa,i}=mesas[0],grande=e.W*e.D>=12;
        exigir(mesa.obj===(grande?'va_mesa_familiar':'va_mesa_comedor'),seed+': mesa inadecuada a la capacidad prevista');
        exigir(C.filter(p=>p.obj==='silla_comedor'&&p.de===i).length===(grande?4:2),seed+': sillas ausentes o sueltas');
        const encima=C.filter(p=>p.sop===i);
        const servicio=encima.filter(p=>p.obj==='va_servicio_comedor_'+(grande?4:2));
        exigir(servicio.length===1,seed+': falta el servicio completo relacionado con la capacidad');
        exigir(Math.hypot(servicio[0].x-mesa.x,servicio[0].z-mesa.z)<.001&&Math.abs(servicio[0].ry-mesa.ry)<.001,seed+': el servicio no está centrado y alineado con la mesa');
        const piezas=OBJETOS[servicio[0].obj].partes,n=grande?4:2;
        exigir(piezas.filter(p=>p.f==='cil'&&p.m==='ceramica').length===n&&piezas.filter(p=>p.f==='cil'&&p.m==='cristal'&&Math.abs(p.d[2]-.1)<.0001).length===n,seed+': no hay plato y vaso por puesto');
        exigir(piezas.some(p=>p.m==='comida')&&piezas.some(p=>p.f==='cil'&&p.m==='cristal'&&Math.abs(p.d[2]-.18)<.0001),seed+': falta pan/comida compartida o jarra de agua del servicio');
        exigir(piezas.filter(p=>p.f==='caja'&&p.m==='metal'&&Math.abs(p.d[1]-.003)<.0001).length===3*n,seed+': faltan cubiertos en algún puesto');
        const colgados=C.filter(p=>p.regla==='techo');exigir(colgados.length===1&&Math.hypot(colgados[0].x-mesa.x,colgados[0].z-mesa.z)<.001,seed+': luminaria duplicada o sin relación con la mesa');
        const lam=colgados[0],emisor=OBJETOS[lam.obj].partes.find(p=>p.luz),l=h.lights.find(l=>Math.abs(l.position.x-e.origen.x-lam.x)<.001&&Math.abs(l.position.z-e.origen.z-lam.z)<.001);
        exigir(l&&Math.abs(l.position.y-e.origen.y-lam.y-emisor.p[1])<.001&&l.userData.base>0,seed+': el foco real no coincide con la luminaria o pierde su intensidad de programa');
        for(const id of ['cuadro_paisaje','fotos_familia','cuadro_virgen'])exigir(C.filter(p=>p.obj===id).length<=1,seed+': cuadro duplicado '+id);
        exigir(!C.some(p=>p.obj.startsWith('va_alimento_')||p.obj.startsWith('prod_')),seed+': el comedor conserva provisiones de tienda');
        exigir(e.ancho>=.8&&!revisarUso(h).errores.some(x=>x.startsWith(e.sala+'/')),seed+': programa inaccesible');
      }finally{tirar(h);}
    }
    const b=caja('va_mesa_comedor'),g=caja('va_mesa_familiar');
    exigir(Math.abs(b.w-1.05)<.0001&&Math.abs(b.d-.7)<.0001,'se ha agrandado la mesa compartida de cocinas');
    exigir(g.w>=1.3499&&g.d>=.7999,'la mesa familiar mantiene superficie insuficiente');
  });
  if(opts.tanda>=16)await caso('comedor conserva capacidad en umbral y no fuerza cuatro sillas donde no caben',()=>{
    const id='__comedor_capacidad',K=KITS.vivienda_comedor;
    try{
      for(const area of [11.999,12,12.001]){
        const A=amueblar('vivienda_comedor',37,{W:4,D:area/4,H:2.75,funciones:true});
        const activas=A.activas.filter(i=>K.objetos[i].regla==='conjunto');
        exigir(activas.length===1,area+': hueco o solapamiento en programa de mesa');
        exigir(K.objetos[activas[0]].obj===(area>=12?'va_mesa_familiar':'va_mesa_comedor'),area+': capacidad incorrecta');
      }
      const grande=K.objetos.find(e=>e.obj==='va_mesa_familiar');
      KITS[id]={...K,objetos:[{...grande,area_min:undefined}]};
      const A=amueblar(id,37,{W:1,D:5,H:2.75,funciones:true});
      exigir(A.P.length===0,'se acepta mesa familiar con sólo dos sillas dentro de corredor estrecho');
      const ctx={W:4,D:4,H:2.75,funciones:true,libres:[{cx:0,cz:2,hw:2,hd:2,a:0,y0:0,y1:2.4}]};
      exigir(amueblar('vivienda_comedor',37,ctx).P.every(p=>p.regla==='techo'),'se fuerza mesa o vajilla sin soporte dentro de una reserva total');
    }finally{delete KITS[id];}
  });
  if(opts.tanda>=16)await caso('comedor conserva todo el botín y lo apoya fuera de la mesa puesta',()=>{
    for(const seed of [2786,5157,2606]){
      const h=H.buildVecino(seed);try{
        const ids=h.loot.map(i=>i.id).sort();exigir(JSON.stringify(ids)===JSON.stringify([...h.profile.loot].sort()),seed+': se pierde o duplica una pertenencia');
        const modelos={joyero:'va_joyero_guardado',lata:'va_lata_guardada',reloj:'va_reloj_guardado'};
        h.group.updateMatrixWorld(true);
        for(const i of h.loot){
          exigir(i.def&&i.label&&i.r>0,seed+': botín sin acción o definición');
          if(!modelos[i.id])continue;
          exigir(i.mesh?.userData.objetoBotin===modelos[i.id],seed+': pertenencia sin modelo legible '+i.id);
          const e=h.estancias.find(e=>e.sala===i.sala),p=e?.colocados.find(p=>p.obj===modelos[i.id]),b=new THREE.Box3().setFromObject(i.mesh);
          if(p){const soporte=e.colocados[p.sop],sup=OBJETOS[soporte.obj].superficies[p.sup];exigir(!['va_mesa_comedor','va_mesa_familiar'].includes(soporte.obj),seed+': pertenencia sobre mesa puesta');exigir(Math.abs(b.min.y-e.origen.y-soporte.y-sup.y)<.001,seed+': pertenencia enterrada o flotante');}
          else exigir(i.mesh.userData.apoyoBotin?.distanciaUso<=1.25,seed+': fallback sin acceso medido');
        }
        exigir(!revisarUso(h).errores.length,seed+': botín inaccesible');
      }finally{tirar(h);}
    }
  });
  if(opts.tanda>=16)await caso('comedor sin aparador ni alacena conserva pertenencias con fallback visible y accesible',()=>{
    const K=KITS.vivienda_comedor,original=K.objetos;
    try{
      K.objetos=original.filter(e=>!['aparador','va_alacena'].includes(e.obj));
      for(const seed of [2786,5157,2606]){
        const h=H.buildVecino(seed);try{
          exigir(JSON.stringify(h.loot.map(i=>i.id).sort())===JSON.stringify([...h.profile.loot].sort()),seed+': se borra botín al faltar apoyo');
          for(const i of h.loot.filter(i=>['joyero','lata','reloj'].includes(i.id))){
            exigir(i.mesh?.visible!==false&&i.mesh.userData.apoyoBotin?.distanciaUso<=1.25,seed+': fallback invisible o sin acceso');
            const a=i.mesh.userData.apoyoBotin;exigir(a.tipo==='suelo'||!['va_mesa_comedor','va_mesa_familiar'].includes(a.obj),seed+': fallback invade mesa puesta');
            h.group.updateMatrixWorld(true);const b=new THREE.Box3().setFromObject(i.mesh);exigir(Math.abs(b.min.y-a.superficieY)<.001,seed+': apoyo de fallback incorrecto');
          }
          exigir(!revisarUso(h).errores.length,seed+': fallback no accesible');
        }finally{tirar(h);}
      }
    }finally{K.objetos=original;}
  });
  if(opts.tanda>=16)await caso('botín sobre un mueble bajo no invade la reserva alta de una ventana',()=>{
    const id='__reserva_botin',base=KITS.vivienda_comedor;
    try{
      KITS[id]={...base,objetos:[
        {zona:'estancia',regla:'contra_pared',obj:'aparador',pared:'S',cantidad:[1,1],obligatorio:true},
        {zona:'estancia',regla:'sobre',obj:'va_joyero_guardado',en:['aparador'],cantidad:[1,1],botin:'joyero',preferir:true},
      ]};
      const A=amueblar(id,37,{W:4,D:4,H:2.75,funciones:true,filtro:()=>true,libres:[{cx:0,cz:.4,hw:2,hd:.4,a:0,y0:.91,y1:2.4}]});
      exigir(A.P.some(p=>p.obj==='aparador'),'negativo sin el soporte bajo que debe caber');
      exigir(!A.P.some(p=>p.obj==='va_joyero_guardado'),'el botín alto ocupa el hueco reservado de ventana');
    }finally{delete KITS[id];}
  });
  if(opts.tanda>=16)await caso('jarra de un servicio centrado respeta la reserva alta aunque la mesa quepa debajo',()=>{
    const id='__reserva_servicio',base=KITS.vivienda_comedor;
    try{
      KITS[id]={...base,objetos:[
        {zona:'estancia',regla:'conjunto',obj:'va_mesa_comedor',cantidad:[1,1],centrado:true,sillas:{variantes:[],n:0}},
        {zona:'estancia',regla:'sobre',obj:'va_servicio_comedor_2',en:['va_mesa_comedor'],cantidad:[1,1],centrado:true},
      ]};
      const A=amueblar(id,37,{W:4,D:4,H:2.75,funciones:true,libres:[{cx:0,cz:2,hw:2,hd:2,a:0,y0:.92,y1:2.4}]});
      exigir(A.P.some(p=>p.obj==='va_mesa_comedor'),'negativo sin mesa baja bajo la reserva');
      exigir(!A.P.some(p=>p.obj==='va_servicio_comedor_2'),'la jarra atraviesa la reserva alta de ventana');
    }finally{delete KITS[id];}
  });
  if(opts.tanda>=16)await caso('laboratorio comedor usa el foco doméstico real y conserva el mínimo de luz',async()=>{
    const presupuesto=await(await fetch('/data/quality_budgets.json')).json(),K=KITS.vivienda_comedor,ids=Object.keys(H.PROFILES);
    for(const seed of [1,69,81]){
      const id=ids[(seed-1)%ids.length],P=H.PROFILES[id],hogar={perfil:id,estilo:P.styles[Math.floor((seed-1)/ids.length)%P.styles.length],botin:P.loot,habitacion:Math.floor((seed-1)/(ids.length*2))%2?'dorm2':'dorm'};
      const puerta=K.puerta??0,origin={x:-9400,z:-9400},h=buildLocal('vivienda_comedor',seed,origin,'Validación',hogar,{libres:[{cx:puerta,cz:.5,hw:.58,hd:.5,a:0,y0:0,y1:2.4}],inicio:{x:puerta,z:.5}});
      try{
        const L=h.local,programa=programaLuzDomestica(L.W*L.D),lam=L.colocados.filter(p=>p.regla==='techo');
        exigir(L.modoLuz==='casa'&&h.lights.length===1&&L.luces.length===1&&lam.length===1,seed+': programa o número de fuentes incorrecto');
        const l=h.lights[0],m=L.luces[0],emisor=OBJETOS[lam[0].obj].partes.find(p=>p.luz);
        exigir(l.intensity===programa.intensidad&&l.distance===programa.alcance&&l.userData.base===l.intensity,seed+': foco distinto del programa doméstico');
        exigir(Math.abs(l.position.x-origin.x-lam[0].x)<.001&&Math.abs(l.position.z-origin.z-lam[0].z)<.001&&Math.abs(l.position.y-lam[0].y-emisor.p[1])<.001,seed+': foco separado de la luminaria');
        exigir(m.x===l.position.x-origin.x&&m.y===l.position.y&&m.z===l.position.z-origin.z&&m.intensidad===l.intensity&&m.alcance===l.distance,seed+': metadatos distintos del foco real');
        exigir(m.k>=K.iluminacion.temperatura_k[0]&&m.k<=K.iluminacion.temperatura_k[1],seed+': temperatura fuera del kit');
        const rep=revisar(h,presupuesto);exigir(!rep.errores.length,seed+': '+rep.errores.join('; '));
      }finally{tirar(h);}
    }
  });
  if(opts.tanda>=17)await caso('biblioteca infantil conserva los apoyos internos de cuentos y manualidades',()=>{
    const EPS=1e-6;
    const sinApoyo=id=>{
      const P=partes({obj:id,x:0,y:0,z:0,ry:0});
      return P.flatMap((p,i)=>{
        exigir(p.f==='caja'&&Math.abs(p.a)<EPS,'oráculo acotado a cajas sin giro: '+id);
        if(Math.abs(p.y0)<EPS)return [];
        const apoyo=P.some((q,j)=>j!==i&&Math.abs(q.y1-p.y0)<EPS&&
          p.cx-p.hw>=q.cx-q.hw-EPS&&p.cx+p.hw<=q.cx+q.hw+EPS&&
          p.cz-p.hd>=q.cz-q.hd-EPS&&p.cz+p.hd<=q.cz+q.hd+EPS);
        return apoyo?[]:[i];
      });
    };
    const solapes=id=>{
      const P=partes({obj:id,x:0,y:0,z:0,ry:0}),mal=[];
      for(let i=0;i<P.length;i++)for(let j=i+1;j<P.length;j++){
        const profundidad=penetra(P[i],P[j]);
        if(profundidad>EPS)mal.push({i,j,profundidad});
      }
      return mal;
    };
    for(const id of ['vb_cuentos_biblioteca','vb_hacer_biblioteca']){
      exigir(OBJETOS[id], 'falta la pertenencia '+id);
      exigir(!sinApoyo(id).length,'subpieza sin contacto o huella completa: '+id);
      exigir(!solapes(id).length,'subpiezas interpenetradas: '+id);
    }
    const obj=OBJETOS.vb_hacer_biblioteca,original=structuredClone(obj.partes);
    try{
      obj.partes[0].d[1]=.18;obj.partes[0].p[1]=.09;
      exigir(sinApoyo(obj.id).includes(1),'no detecta el cuaderno original flotante');
      obj.partes=structuredClone(original);obj.partes[1].p[1]+=.01;
      exigir(sinApoyo(obj.id).includes(1),'no detecta elevar el cuaderno');
      obj.partes=structuredClone(original);obj.partes.splice(0,1);
      exigir(sinApoyo(obj.id).includes(0),'no detecta retirar la caja de apoyo');
      obj.partes=structuredClone(original);
      obj.partes[2].d[0]=.26;obj.partes[2].p[0]=.13;obj.partes[3].p[0]=.13;
      const mal=solapes(obj.id);
      exigir(!sinApoyo(obj.id).length,'el negativo de solape debe seguir apoyado');
      exigir(mal.some(p=>p.i===0&&p.j===2&&p.profundidad>.02)&&mal.some(p=>p.i===0&&p.j===3&&p.profundidad>.01),'no detecta las dos penetraciones originales de la pila');
    }finally{obj.partes=original;}
  });
  if(opts.tanda>=17)await caso('infantil agrupa biblioteca con puesto y conserva salida exacta del armario',async()=>{
    const {Interiors}=await import('/src/interiors.js'),EPS=1e-6;
    const css=document.body.classList.contains('hiding');
    const dentro=(p,b,x,z)=>{
      const dx=x-p.x,dz=z-p.z,lx=dx*Math.cos(p.ry)-dz*Math.sin(p.ry),lz=dx*Math.sin(p.ry)+dz*Math.cos(p.ry);
      return lx>b.x0+EPS&&lx<b.x1-EPS&&lz>b.z0+EPS&&lz<b.z1-EPS;
    };
    const libre=(h,e,p)=>{
      const col=h.levels?h.levels[p.y>h.split?1:0]:h.collider,q=p.clone(),r=col.resolveCircle(q,.34);
      if(Math.hypot(q.x-p.x,q.z-p.z)>EPS||r.depth>EPS)return false;
      if(p.x<e.origen.x-e.W/2||p.x>e.origen.x+e.W/2||p.z<e.origen.z||p.z>e.origen.z+e.D)return false;
      for(const sala of h.estancias){
        if(Math.abs(sala.origen.y-p.y)>.2)continue;
        for(const c of sala.colocados){
          const b=caja(c.obj);
          if(c.sop!=null||['pared','techo'].includes(c.regla)||OBJETOS[c.obj].clase==='PICKUP'||b.h<.3)continue;
          if(dentro(c,b,p.x-sala.origen.x,p.z-sala.origen.z))return false;
        }
      }
      return true;
    };
    try{for(const seed of [4007,5045,1296,3405,1555,4034]){
      const h=H.buildVecino(seed,{x:-5200,z:-5200});try{
        const e=h.estancias.find(e=>e.kit==='vivienda_ninos');exigir(e,seed+': falta cuarto infantil');
        const C=e.colocados,m=C.find(p=>p.obj==='vb_mesa_ninos'),b=C.find(p=>p.obj==='vb_biblioteca_ninos'),a=C.find(p=>p.obj==='vb_armario_ninos'),c=C.find(p=>p.obj==='vb_silla_ninos');
        exigir(m&&b&&a&&c,seed+': pierde un volumen esencial');
        exigir(b.de===C.indexOf(m)&&c.de===C.indexOf(m)&&c.e===m.e&&C.indexOf(c)===C.indexOf(m)+1,seed+': grupo o vínculo inmediato de silla incorrectos');
        exigir(a.de==null,seed+': armario vuelve a formar parte del grupo de estudio');
        exigir(Math.abs(Math.sin(b.ry-m.ry))<EPS&&Math.cos(b.ry-m.ry)>.99,seed+': biblioteca gira fuera del frente');
        const dx=b.v.cx-m.v.cx,dz=b.v.cz-m.v.cz,lateral=Math.abs(dx*Math.cos(m.ry)-dz*Math.sin(m.ry));
        exigir(Math.abs(lateral-b.v.hw-m.v.hw-.04)<.001,seed+': biblioteca separada del puesto');
        const baldas=OBJETOS[b.obj].superficies,pertenencias=C.filter(p=>['vb_cuentos_biblioteca','vb_hacer_biblioteca'].includes(p.obj)&&p.sop===C.indexOf(b));
        exigir(baldas.length===2&&baldas[1].y-baldas[0].y>.4,seed+': faltan dos baldas útiles');
        exigir(pertenencias.length===2&&new Set(pertenencias.map(p=>p.sup)).size===2&&pertenencias.every(p=>[0,1].includes(p.sup)),seed+': balda sin pertenencia apoyada');
        exigir(C.some(p=>p.obj==='vb_bloques'&&p.sop===C.indexOf(b)),seed+': juego sin apoyo en biblioteca');
        exigir(C.some(p=>p.obj==='vb_cama_ninos')&&C.some(p=>p.obj==='vb_mesita')&&h.pieces.bed.some(p=>p.rm.id===e.sala)&&h.pieces.table.some(p=>p.rm.id===e.sala)&&h.pieces.seat.some(p=>p.rm.id===e.sala),seed+': pérdida de descanso, mesa o asiento');
        const wb=caja(a.obj);exigir(wb.w>=.949&&wb.d>=.419&&wb.h>=1.49,seed+': armario encogido');
        const R=espacioFrontal(a,wb,[.7,.6]),Z=e.zonas.estancia;
        for(const sx of [-1,1])for(const sz of [-1,1]){
          const x=R.cx+sx*R.hw*Math.cos(R.a)+sz*R.hd*Math.sin(R.a),z=R.cz-sx*R.hw*Math.sin(R.a)+sz*R.hd*Math.cos(R.a);
          exigir(x>=Z.x0-EPS&&x<=Z.x1+EPS&&z>=Z.z0-EPS&&z<=Z.z1+EPS,seed+': reserva de armario sale del cuarto');
        }
        exigir(!C.some(p=>p!==a&&partes(p).some(q=>penetra(R,q)>.005)),seed+': reserva frontal invadida');
        if([4007,5045].includes(seed)){
          exigir(Math.abs(Math.sin(m.ry))<EPS,seed+': cambió el eje de la sección estrecha');
          const norte=Math.cos(m.ry)<0,d=norte?c.v.cz-c.v.hd:e.D-c.v.cz-c.v.hd;
          // Conservar una sección de .8 x .8 junto a la silla, sin exigir
          // que también quede vacío el fondo sobrante hasta la pared opuesta.
          const paso={cx:c.v.cx,cz:norte?d-.4:e.D-d+.4,hw:.4,hd:.4,a:0,y0:.08,y1:1.2};
          const librePaso=lista=>!lista.some(p=>p!==c&&p.sop==null&&!['pared','techo'].includes(p.regla)&&caja(p.obj).h>=.3&&partes(p).some(q=>penetra(paso,q)>EPS));
          exigir(d>=.8-EPS&&librePaso(C),seed+': sección física de paso0,8 invadida');
          const banco=C.find(p=>p.obj==='vb_banco_lectura_ninos');
          if(banco){
            const frente=p=>{const extremos=partes(p).map(q=>q.cz+(norte?1:-1)*(Math.abs(Math.cos(q.a))*q.hd+Math.abs(Math.sin(q.a))*q.hw));return norte?Math.max(...extremos):Math.min(...extremos);};
            const hueco=p=>norte?d-frente(p):frente(p)-(e.D-d);
            exigir(hueco(banco)>=.8-EPS,seed+': banco reduce el paso por debajo de0,8');
            const avance=hueco(banco)-.79,adelantado={...banco,z:banco.z+(norte?avance:-avance)};
            exigir(hueco(adelantado)<.8-EPS&&!librePaso(C.map(p=>p===banco?adelantado:p)),seed+': negativo de hueco0,79 no detectado');
          }
        }
        exigir(e.ancho>=.8&&!revisarUso(h).errores.length,seed+': pierde paso o acceso');
        const it=h.inter.find(i=>i.sala===e.sala&&i.type==='hide');exigir(it&&h.inter.some(i=>i.sala===e.sala&&i.type==='read'),seed+': pierde ocultación o lectura');
        const p={pos:new THREE.Vector3(it.x,e.origen.y,it.z),hidden:false},start=p.pos.clone(),cam={fovOverride:0,setFirstPerson(v){this.firstPerson=v;}},owner=Object.create(Interiors.prototype);
        owner.game={player:p,audio:{sfx(){}},cam};
        exigir(libre(h,e,p.pos),seed+': entrada real del armario ocupada');
        owner.hideIn(it);
        exigir(p.hidden&&owner.hiding===it&&cam.fovOverride===55&&cam.firstPerson&&document.body.classList.contains('hiding'),seed+': no entra en ocultación real');
        exigir(p.pos.x===it.hx&&p.pos.y===e.origen.y&&p.pos.z===it.hz&&dentro(a,wb,p.pos.x-e.origen.x,p.pos.z-e.origen.z),seed+': centro oculto fuera del armario');
        owner.unhide();
        exigir(!p.hidden&&owner.hiding==null&&cam.fovOverride===0&&!document.body.classList.contains('hiding')&&p.pos.equals(start),seed+': no restaura la salida real');
        exigir(libre(h,e,p.pos),seed+': salida exacta ocupada para radio0,34');
        const malo={...it,x:it.hx,z:it.hz};owner.hideIn(malo);owner.unhide();
        exigir(!libre(h,e,p.pos),seed+': negativo acepta salida al interior de una huella sólida');
      }finally{tirar(h);}
    }}finally{document.body.classList.toggle('hiding',css);}
  });
  if(opts.tanda>=17)await caso('grupo de estudio comprueba ambos órdenes y conserva fallback y RNG',()=>{
    const id='__infantil_grupo_asiento',K=KITS.vivienda_ninos,puesto=K.objetos.find(e=>e.obj==='vb_mesa_ninos'),biblioteca=K.objetos.find(e=>e.obj==='vb_biblioteca_ninos');
    const base=[{...puesto,pared:['N']},{...biblioteca}],ctx={W:2,D:2.8,H:2.75,funciones:true,inicio:{x:0,z:.5}};
    const pareja=A=>{const m=A.P.find(p=>p.obj==='vb_mesa_ninos'),b=A.P.find(p=>p.obj==='vb_biblioteca_ninos'),c=A.P.find(p=>p.obj==='vb_silla_ninos');return m&&b&&c&&b.de===A.P.indexOf(m)&&c.de===A.P.indexOf(m)&&c.e===m.e;};
    try{
      KITS[id]={...K,objetos:base};const A=amueblar(id,7,ctx);
      exigir(pareja(A)&&A.P.find(p=>p.obj==='vb_mesa_ninos').x<A.P.find(p=>p.obj==='vb_biblioteca_ninos').x,'no compone el primer orden');
      const libres=[{cx:-.5,cz:2.8-.675,hw:.32,hd:.22,a:0,y0:0,y1:2.4}],B=amueblar(id,7,{...ctx,libres});
      exigir(pareja(B)&&B.P.find(p=>p.obj==='vb_mesa_ninos').x>B.P.find(p=>p.obj==='vb_biblioteca_ninos').x,'no prueba el orden inverso al bloquear la silla');
      for(const seed of [1,37,81])for(const contexto of [{...ctx,W:1.6},{...ctx,libres:[{cx:0,cz:2.8-.675,hw:1,hd:.22,a:0,y0:0,y1:2.4}]}]){
        const objetos=base.concat(K.objetos.filter(e=>e.regla==='techo'||(e.regla==='sobre'&&e.en?.includes('vb_mesa_ninos'))));
        KITS[id]={...K,objetos};const agrupado=amueblar(id,seed,contexto);
        KITS[id]={...K,objetos:objetos.map(({grupo_pared,...e})=>e)};const individual=amueblar(id,seed,contexto);
        exigir(!pareja(agrupado)&&JSON.stringify(agrupado.P)===JSON.stringify(individual.P)&&JSON.stringify(agrupado.activas)===JSON.stringify(individual.activas),seed+': fallback alterado');
        exigir(agrupado.U([0,1])===individual.U([0,1]),seed+': el grupo imposible consume RNG externo');
      }
    }finally{delete KITS[id];}
  });
  if(opts.tanda>=18)await caso('el acabado infantil usa la cama real para colorear una sola pared alta',()=>{
    const proto=HouseBuilder.prototype,add=proto.add,mat=proto.mat;
    let planos=[],materiales=new Map();
    proto.mat=function(...args){const key=mat.apply(this,args);if(key.startsWith('infantil_'))materiales.set(key,this.mats.get(key));return key;};
    proto.add=function(key,geo,x,y,z,ry=0){
      if(key.startsWith('infantil_')&&geo.type==='PlaneGeometry')planos.push({key,x:this.ox+x,y,z:this.oz+z,ry,w:geo.parameters.width,h:geo.parameters.height,ny:geo.attributes.normal.getY(0)});
      return add.call(this,key,geo,x,y,z,ry);
    };
    try{for(const seed of [4007,5045,1296,3405,1555,4034]){
      planos=[];materiales=new Map();let h;
      try{
        h=H.buildVecino(seed,{x:-5200,z:-5200});
        const salas=h.estancias.filter(e=>e.kit==='vivienda_ninos');exigir(salas.length===1,seed+': falta la sala infantil dirigida');
        const e=salas[0],cama=e.colocados.find(p=>p.obj==='vb_cama_ninos');exigir(cama,seed+': falta cama para probar el caller');
        const x0=e.origen.x-e.W/2,x1=e.origen.x+e.W/2,z0=e.origen.z,z1=z0+e.D,y=e.origen.y;
        const deSala=p=>p.x>=x0-1e-6&&p.x<=x1+1e-6&&p.z>=z0-1e-6&&p.z<=z1+1e-6&&p.y>=y-1e-6&&p.y<=y+e.H+1e-6;
        const paredes=planos.filter(p=>deSala(p)&&Math.abs(p.ny)<1e-6);
        const bajos=paredes.filter(p=>p.y+p.h/2<=y+.92+1e-6),altos=paredes.filter(p=>p.y-p.h/2>=y+.92-1e-6);
        const techo=planos.filter(p=>deSala(p)&&p.ny<-.99&&Math.abs(p.y-(y+e.H-.008))<1e-6);
        const keys=[...new Set(bajos.map(p=>p.key))];exigir(keys.length===1&&techo.length===1&&altos.length>=4,seed+': evidencia incompleta de bandas y techo');
        const bajo=keys[0],cal=techo[0].key;
        exigir(bajo!==cal&&materiales.get(bajo)&&materiales.get(cal)&&!materiales.get(bajo).color.equals(materiales.get(cal).color),seed+': pared de uso indistinguible del techo');
        // La normal frontal de la cama apunta al interior. La pared de cabecero
        // tiene esa misma normal, con independencia del número de fragmentos.
        const nx=Math.sin(cama.ry),nz=Math.cos(cama.ry);let area=0,opuestos=0;
        for(const p of altos){
          const cabecero=Math.sin(p.ry)*nx+Math.cos(p.ry)*nz>.999;
          exigir(p.key===(cabecero?bajo:cal),seed+': acabado alto no sigue la cama amueblada');
          if(cabecero)area+=p.w*p.h;else opuestos++;
        }
        exigir(area>.25&&opuestos>=3,seed+': falta una pared alta de uso y tres paredes claras');
      }finally{if(h)tirar(h);}
    }}finally{proto.add=add;proto.mat=mat;}
  });
  if(opts.tanda>=18)await caso('infantil recupera juego libre y banco de lectura utilizable sin invadir cortinas',()=>{
    const EPS=1e-6,ids=['vb_alfombra_juego','vb_alfombra_juego_compacta'];
    const libre=(h,e,p)=>{
      const col=h.levels?h.levels[p.y>h.split?1:0]:h.collider,q=p.clone(),r=col.resolveCircle(q,.34);
      if(Math.hypot(q.x-p.x,q.z-p.z)>EPS||r.depth>EPS)return false;
      for(const sala of h.estancias){if(Math.abs(sala.origen.y-p.y)>.2)continue;
        for(const c of sala.colocados){const b=caja(c.obj);if(c.sop!=null||['pared','techo'].includes(c.regla)||OBJETOS[c.obj].clase==='PICKUP'||b.h<.3)continue;
          const dx=p.x-sala.origen.x-c.x,dz=p.z-sala.origen.z-c.z,lx=dx*Math.cos(c.ry)-dz*Math.sin(c.ry),lz=dx*Math.sin(c.ry)+dz*Math.cos(c.ry);
          if(lx>b.x0+EPS&&lx<b.x1-EPS&&lz>b.z0+EPS&&lz<b.z1-EPS)return false;
        }
      }
      return p.x>=e.origen.x-e.W/2&&p.x<=e.origen.x+e.W/2&&p.z>=e.origen.z&&p.z<=e.origen.z+e.D;
    };
    for(const seed of [4007,5045,1296,4034,3072,4848,5144,6291,8030]){
      const h=H.buildVecino(seed,{x:-5200,z:-5200});try{
        const e=h.estancias.find(e=>e.kit==='vivienda_ninos');exigir(e,seed+': sin cuarto infantil');
        const C=e.colocados,rugs=C.filter(p=>ids.includes(p.obj)),bank=C.find(p=>p.obj==='vb_banco_lectura_ninos'),books=C.find(p=>p.obj==='vb_biblioteca_ninos');
        exigir(rugs.length===1,seed+': debe tener una huella de juego');
        const rug=rugs[0],rb=caja(rug.obj);exigir(rb.w*rb.d>=1.02-EPS,seed+': alfombra sin area de juego reconocible');
        exigir(!C.some(p=>p!==rug&&p.sop==null&&!['pared','techo'].includes(p.regla)&&partes(rug).some(v=>partes(p).some(q=>penetra(v,q)>.005))),seed+': alfombra bajo otro mueble');
        exigir(books&&C.filter(p=>p.sop===C.indexOf(books)&&['vb_cuentos_biblioteca','vb_hacer_biblioteca'].includes(p.obj)).length===2,seed+': pierde dos baldas ocupadas');
        if([4007,5045,1296].includes(seed))exigir(bank,seed+': no aprovecha el area con banco');
        if(bank){
          exigir(Math.cos(bank.ry-books.ry)<-.999,seed+': asiento sin relacion frontal con los libros');
          const b=caja(bank.obj),asiento=OBJETOS[bank.obj].asientos[0],sx=asiento.p[0]*Math.cos(bank.ry)+asiento.p[2]*Math.sin(bank.ry),sz=-asiento.p[0]*Math.sin(bank.ry)+asiento.p[2]*Math.cos(bank.ry);
          exigir(h.pieces.seat.some(s=>s.rm.id===e.sala&&!s.chair&&Math.hypot(s.x-e.origen.x-bank.x-sx,s.z-e.origen.z-bank.z-sz)<EPS),seed+': banco sin asiento real de vida domestica');
          const R=espacioFrontal(bank,b,[.7,.55]);exigir(!C.some(p=>p!==bank&&partes(p).some(v=>penetra(R,v)>.005)),seed+': banco sin espacio frontal');
          const p=new THREE.Vector3(e.origen.x+bank.x+Math.sin(bank.ry)*(b.z1+.5),e.origen.y,e.origen.z+bank.z+Math.cos(bank.ry)*(b.z1+.5));
          exigir(libre(h,e,p),seed+': cuerpo radio0,34 no cabe delante del banco');
          const curtains=[];
          // La reserva real de ventana tiene .38m de fondo y .05m extra
          // en cada extremo. Reconstruimos desde ella la abertura, no desde
          // una lista de ventanas por semilla que pudiera ocultar un cambio.
          // curtainGeo(.38,2.05): pliegue .035, centro .1m/altura1.2;
          // restar inset .075 y pared exterior .03 sitúa el centro a .055.
          for(const w of e.libres.filter(w=>Math.abs(w.y0-.92)<EPS)){
            const side=Math.abs(w.cz-.19)<EPS?'s':Math.abs(w.cz-e.D+.19)<EPS?'n':Math.abs(w.cx+e.W/2-.19)<EPS?'w':Math.abs(w.cx-e.W/2+.19)<EPS?'e':null;
            exigir(side,seed+': reserva de ventana no reconocible');
            const a=({s:0,n:Math.PI,w:Math.PI/2,e:-Math.PI/2})[side],mid=side==='s'||side==='n'?w.cx:w.cz,width=2*(side==='s'||side==='n'?w.hw:w.hd)-.1;
            const x=side==='w'?-e.W/2+.055:side==='e'?e.W/2-.055:mid,z=side==='s'?.055:side==='n'?e.D-.055:mid;
            for(const sign of [-1,1])curtains.push({cx:x+sign*(width/2+.06)*Math.cos(a),cz:z-sign*(width/2+.06)*Math.sin(a),hw:.19,hd:.035,a,y0:.175,y1:2.225});
          }
          exigir(!curtains.some(c=>partes(bank).some(v=>penetra(v,c)>EPS)),seed+': banco corta el volumen de cortina');
        }
        exigir(!revisarUso(h).errores.length,seed+': pierde acceso funcional');
        let mallas=0;h.group.traverse(o=>{if(o.isMesh&&o.visible)mallas++;});exigir(mallas<=60,seed+': supera60mallas');
      }finally{tirar(h);}
    }
  });
  if(opts.tanda>=18)await caso('banco conserva apoyos y separacion optativa sin hueco en frontera de alfombras',()=>{
    const EPS=1e-6,id='__infantil_bv3',K=structuredClone(KITS.vivienda_ninos),base=OBJETOS.vb_banco_lectura_ninos;
    const mal=()=>{const P=partes({obj:base.id,x:0,y:0,z:0,ry:0}),errores=[];
      const contacto=(i,j)=>Math.abs(P[i].y0-P[j].y1)<EPS&&Math.min(P[i].cx+P[i].hw,P[j].cx+P[j].hw)-Math.max(P[i].cx-P[i].hw,P[j].cx-P[j].hw)>EPS&&Math.min(P[i].cz+P[i].hd,P[j].cz+P[j].hd)-Math.max(P[i].cz-P[i].hd,P[j].cz-P[j].hd)>EPS;
      for(let i=0;i<P.length;i++){if(P[i].y0>EPS&&!P.some((_,j)=>j!==i&&contacto(i,j)))errores.push('apoyo'+i);for(let j=i+1;j<P.length;j++)if(penetra(P[i],P[j])>EPS)errores.push('solape'+i+'/'+j);}
      for(const j of [1,2,4])if(!contacto(5,j))errores.push('puente'+j);return errores;
    };
    const original=structuredClone(base.partes);
    try{
      exigir(!mal().length,'banco sin apoyo o con penetracion');base.partes[5].p[1]+=.01;exigir(mal().some(s=>s==='apoyo5'),'no detecta asiento flotante');base.partes=structuredClone(original);base.partes[6].p[0]=0;exigir(mal().some(s=>s.startsWith('solape')),'no detecta caja dentro de la division');
    }finally{base.partes=original;}
    try{
      KITS[id]={...K,objetos:K.objetos.filter(e=>['vb_alfombra_juego','vb_alfombra_juego_compacta'].includes(e.obj))};
      for(const D of [3.9999999,4,4.0000001]){const A=amueblar(id,43,{W:3,D,funciones:true,libres:[],inicio:{x:0,z:.5}}),es=A.activas.map(i=>A.K.objetos[i]);exigir(es.length===1&&es[0].obj===(D<4?'vb_alfombra_juego_compacta':'vb_alfombra_juego'),'frontera de12m2 activa cero o dos alfombras');}
      const ctx={W:4,D:4,funciones:true,libres:[],inicio:{x:0,z:2}};
      for(const pared of ['N','S','E','W'])for(const d of [undefined,0,.14]){
        KITS[id]={...K,objetos:[{zona:'estancia',regla:'contra_pared',obj:base.id,pared,centrado:true,cantidad:[1,1],...(d===undefined?{}:{separacion_pared:d})}]};
        const A=amueblar(id,1,ctx),p=A.P[0];exigir(p,'sin banco en fixture vacia');
        const ex=Math.abs(p.v.hw*Math.cos(p.ry))+Math.abs(p.v.hd*Math.sin(p.ry)),ez=Math.abs(p.v.hw*Math.sin(p.ry))+Math.abs(p.v.hd*Math.cos(p.ry)),dist=pared==='S'?p.v.cz-ez:pared==='N'?4-p.v.cz-ez:pared==='W'?p.v.cx-ex+2:2-p.v.cx-ex;
        exigir(Math.abs(dist-(d??.01))<EPS,'separador suma holgura o falla en pared '+pared);
      }
      for(const cfg of [{regla:'contra_pared',grupo_pared:'no'},{regla:'suelo_libre'}]){
        KITS[id]={...K,objetos:[{zona:'estancia',obj:base.id,cantidad:[1,1],separacion_pared:.14,...cfg}]};let falla=false;try{amueblar(id,1,ctx);}catch(e){falla=/separacion_pared/.test(String(e));}exigir(falla,'separador se ignora fuera de su contrato');
      }
    }finally{delete KITS[id];}
  });
  if(opts.tanda>=18)await caso('laboratorio infantil resuelve29/51/63 sin cambiar el marco original',async()=>{
    const B=await(await fetch('/data/quality_budgets.json')).json(),ctx={libres:[{cx:-.75,cz:.5,hw:.58,hd:.5,a:0,y0:0,y1:2.4}],inicio:{x:-.75,z:.5}},contexto=JSON.stringify(ctx),ids=Object.keys(H.PROFILES);
    const hogar=seed=>{const id=ids[(seed-1)%ids.length],p=H.PROFILES[id];return{perfil:id,estilo:p.styles[Math.floor((seed-1)/ids.length)%p.styles.length],botin:p.loot,habitacion:'ninos'};};
    for(const[seed,W,D]of[[29,5.9,2.1],[51,3.5,2.1],[63,3.5,3.6]]){
      const h=buildLocal('vivienda_ninos',seed,{x:-5200,z:-5200},'Regresión',hogar(seed),ctx),a=buildLocal('vivienda_ninos',seed,{x:-5200,z:-5200},'Regresión',hogar(seed),ctx);
      try{
        const r=revisar(h,B),L=h.local,g=L.generacion;exigir(!r.errores.length,seed+': '+r.errores.join('; '));
        exigir(L.seed===seed&&L.W===W&&L.D===D&&L.H===2.75&&L.puertaX===-.75,seed+': cambió semilla solicitada o marco');
        exigir(g&&!g.agotado&&g.maximo===12&&g.intento<12&&g.marco.W===W&&g.marco.D===D&&g.marco.H===2.75&&g.marco.puertaX===-.75,seed+': falta traza del marco fijo');
        exigir(g.semillaEfectiva===((seed+g.intento*104729)>>>0)&&g.intentos.length===g.intento+1,seed+': semilla efectiva no corresponde al intento');
        exigir(g.intentos.every((t,i)=>t.seed===((seed+i*104729)>>>0)&&(i===g.intento?t.faltan.length===0:t.faltan.length>0)),seed+': elige un intento saltándose un éxito');
        exigir(g.intentos.every(t=>!t.busquedasSuelo||t.busquedasSuelo.every(b=>b.probados<=16000&&b.limite===16000)),seed+': búsqueda sin límite');
        exigir(JSON.stringify(L)===JSON.stringify(a.local),seed+': montaje no determinista');
      }finally{tirar(h);tirar(a);}
    }
    // Si los200tiros ya daban una solución, el opt-in no cambia P ni U posterior.
    const K=KITS.vivienda_ninos,flags=K.objetos.filter(e=>e.suelo_determinista),save=flags.map(e=>e.suelo_determinista),filtro=filtroHogar(hogar(1));let viejo,h;
    try{
      for(const e of flags)delete e.suelo_determinista;
      const A=amueblar('vivienda_ninos',1,{...ctx,filtro});viejo={P:JSON.stringify(A.P),U:A.U([0,1])};
      flags.forEach((e,i)=>{e.suelo_determinista=save[i];});const A2=amueblar('vivienda_ninos',1,{...ctx,filtro});
      exigir(JSON.stringify(A2.P)===viejo.P&&A2.U([0,1])===viejo.U,'opt-in modifica una colocación previa válida o su RNG');
      h=buildLocal('vivienda_ninos',1,{x:-5200,z:-5200},'Control',hogar(1),ctx);exigir(!h.local.generacion,'reintenta el laboratorio que ya cumplía mínimos');
    }finally{flags.forEach((e,i)=>{e.suelo_determinista=save[i];});if(h)tirar(h);}
    exigir(JSON.stringify(ctx)===contexto,'mutación del contexto original');
  });
  if(opts.tanda>=18)await caso('laboratorio bloqueado conserva el error tras12 intentos y dimensiones fijas',async()=>{
    const B=await(await fetch('/data/quality_budgets.json')).json(),seed=51,ids=Object.keys(H.PROFILES),id=ids[(seed-1)%ids.length],p=H.PROFILES[id],hogar={perfil:id,estilo:p.styles[Math.floor((seed-1)/ids.length)%p.styles.length],botin:p.loot,habitacion:'ninos'};
    const ctx={W:3.5,D:2.1,H:2.75,libres:[{cx:0,cz:1.05,hw:1.75,hd:1.05,a:0,y0:0,y1:3}],inicio:{x:-.75,z:.5}},original=JSON.stringify(ctx),h=buildLocal('vivienda_ninos',seed,{x:-5200,z:-5200},'Bloqueado',hogar,ctx);
    try{
      const L=h.local,g=L.generacion,r=revisar(h,B);
      exigir(r.errores.some(e=>e.includes('obligatorio:')&&e.includes('alfombra')),'convierte la cuota incumplida en un verde');
      exigir(g?.agotado&&g.intento===11&&g.intentos.length===12&&g.intentos.every(t=>t.faltan.length>0),'no agota exactamente12 intentos fallidos');
      exigir(g.semillaEfectiva===((seed+11*104729)>>>0)&&L.seed===seed,'traza incorrecta del fallo agotado');
      exigir(L.W===3.5&&L.D===2.1&&L.H===2.75&&L.puertaX===-.75&&g.marco.W===3.5&&g.marco.D===2.1&&g.marco.H===2.75,'ensancha o cambia el marco para pasar');
      exigir(JSON.stringify(ctx)===original,'mutación de reservas o entrada');
    }finally{tirar(h);}
  });
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
  return { pruebas, errores };
}
