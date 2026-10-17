// The validator of an interior (technical backlog, I-04 and I-03), run in the game's page: an interior is built from its
// kit and seed, and checked —
//  - obligatorios: every mandatory entry of the kit laid out, its count within the kit's range (densities included);
//  - flotando: nothing more than 1 cm off what it stands on (the floor, its surface, its wall, the ceiling);
//  - interpenetración: no two objects' parts into each other by more than 1 cm (what stands on another excepted);
//  - paso libre: from the street door, a body 0.9 m wide reaches every public zone (an occupancy grid of 5 cm);
//  - luz: as many lights as the kit says, of its colour temperature, and no public zone under its minimum;
//  - rendimiento: triangles, meshes and lights within data/quality_budgets.json;
//  - variación: the same seed gives the same layout (its hash), another seed a different one (≥ 30 % of it).
//   const V = await import('/tools/interiores/validar.js'); await V.validar('cafeteria', 7)
import { buildLocal } from '/src/locales.js';
import { PROFILES, buildVecino, kitDeEstancia } from '/src/houses.js';
import { KITS, OBJETOS } from '/src/interiores_datos.js';
import { caja } from '/src/objetos.js';
import { rot, partes, penetra, mapaPaso } from '/src/interiores_geo.js';

const ORIGIN = { x: -9400, z: -9400 };
const DEG = Math.PI / 180;

export function revisar(h, presupuesto) {
  const L = h.local, K = KITS[L.kit], C = L.colocados, err = [], av = [];
  const { W, D, H } = L;
  // ---- obligatorios y densidades
  const porEntrada = new Map();
  for (const c of C) porEntrada.set(c.e, (porEntrada.get(c.e) || 0) + 1);
  const recuento = [];
  for (const [ei, e] of K.objetos.entries()) {
    if (L.activas && !L.activas.includes(ei)) continue; // (an entry of another household)
    const n = e.silla_frontal?C.filter(c=>c.e===ei&&c.de===null).length:(porEntrada.get(ei)||0), Z = L.zonas[e.zona], area = (Z.x1 - Z.x0) * (Z.z1 - Z.z0), largo = Math.max(Z.x1 - Z.x0, Z.z1 - Z.z0);
    if(e.silla_frontal){
      const puestos=C.map((c,i)=>({c,i})).filter(({c})=>c.e===ei&&c.de===null);
      for(const {i} of puestos)if(C.filter(c=>c.e===ei&&c.obj===e.silla_frontal&&c.de===i).length!==1)err.push(`asiento: entrada ${ei} sin una silla frontal vinculada al puesto ${i}`);
      if(C.filter(c=>c.e===ei&&c.de!==null).length!==puestos.length)err.push(`asiento: entrada ${ei} con auxiliares sin correspondencia`);
    }
    let lo = e.obligatorio ? 1 : 0, hi = Infinity;
    if (e.cantidad) { lo = Math.max(lo, e.cantidad[0]); hi = e.cantidad[1]; }
    if (e.regla === 'conjunto' && !e.por_m2) { // (sets so many: the tables counted)
      const mesas = C.filter((c) => c.e === ei && c.de === null).length;
      recuento.push({ entrada: ei, obj: e.obj, mesas });
      if (mesas < Math.max(lo, (e.cantidad || [0])[0])) err.push(`obligatorio: ${e.zona}/${e.obj} — ${mesas} mesas, el kit pide ${Math.max(lo, (e.cantidad || [0])[0])}`);
      if (e.cantidad && mesas > e.cantidad[1]) err.push(`exceso: ${e.zona}/${e.obj} — ${mesas} mesas, el kit admite ${e.cantidad[1]}`);
      continue;
    }
    if (e.regla === 'conjunto' && e.por_m2) { // (a set: its table and its chairs; the tables counted)
      const mesas = C.filter((c) => c.e === ei && c.de === null).length;
      const dens = mesas / area;
      recuento.push({ entrada: ei, obj: e.obj, mesas, densidad: +dens.toFixed(3), rango: e.por_m2 });
      if (dens < e.por_m2[0] - 1 / area || dens > e.por_m2[1] + 1 / area) err.push(`densidad: ${e.zona}/${e.obj} ${mesas} mesas en ${area.toFixed(1)} m² (${dens.toFixed(2)}/m², el kit pide ${e.por_m2.join('–')})`);
      continue;
    }
    if (e.por_m2 && e.regla !== 'techo') { lo = Math.max(lo, Math.floor(area * e.por_m2[0])); hi = Math.ceil(area * e.por_m2[1]) + 1; }
    recuento.push({ entrada: ei, obj: e.obj || (e.variantes || []).join('|').slice(0, 40), n });
    if (n < lo) err.push(`obligatorio: ${e.zona}/${e.obj || e.variantes[0] + '…'} — ${n} colocados, el kit pide ${lo}`);
    if (n > hi) err.push(`exceso: ${e.zona}/${e.obj} — ${n} colocados, el kit admite ${hi}`);
  }
  // ---- flotando (≤ 1 cm de su apoyo)
  let flot = 0;
  const muros = [];
  for (const c of C) {
    const v = c.v, b = caja(c.obj);
    let gap;
    if (c.sop != null) { const s = C[c.sop], sup = OBJETOS[s.obj].superficies[c.sup]; gap = Math.abs(v.y0 - ((s.y || 0) + sup.y)); }
    else if (c.regla === 'techo') gap = Math.abs(v.y1 - H);
    else if (c.regla === 'pared') {
      // (its back against a wall of its zone, or of the room)
      const Z = L.zonas[c.zona];
      const [bx, bz] = rot((b.x0 + b.x1) / 2, b.z0, c.ry), px = c.x + bx, pz = c.z + bz;
      gap = Math.min(Math.abs(px - Z.x0), Math.abs(px - Z.x1), Math.abs(pz - Z.z0), Math.abs(pz - Z.z1));
    } else gap = Math.abs(v.y0);
    if (gap > 0.01) { flot++; if (flot <= 8) err.push(`flotando: ${c.obj} (${c.zona}) a ${(gap * 100).toFixed(1)} cm de su apoyo`); }
  }
  // ---- interpenetraciones (> 1 cm), por piezas, de los objetos cuyas cajas se tocan
  const PZ = C.map(partes);
  let inter = 0;
  for (let i = 0; i < C.length; i++) for (let j = i + 1; j < C.length; j++) {
    const a = C[i], b = C[j];
    if (a.sop === j || b.sop === i || (a.sop != null && a.sop === b.sop && false)) continue;
    const va = a.v, vb = b.v;
    if (Math.abs(va.cx - vb.cx) > va.hw + va.hd + vb.hw + vb.hd || Math.abs(va.cz - vb.cz) > va.hw + va.hd + vb.hw + vb.hd) continue;
    let worst = 0;
    for (const pa of PZ[i]) for (const pb of PZ[j]) worst = Math.max(worst, penetra(pa, pb));
    if (worst > 0.01) { inter++; if (inter <= 10) err.push(`interpenetración: ${a.obj} y ${b.obj} (${a.zona}) ${(worst * 100).toFixed(1)} cm`); }
  }
  // ---- paso libre (0,9 m) desde la puerta a cada zona pública (rejilla de 5 cm, la misma geometría que el montaje);
  // las zonas de trabajo (trasbarra, almacén), aviso si el personal no llega
  const mapa = mapaPaso({ W, D, zonas: L.zonas, tabiques: L.tabiques }, PZ.flat(), 0.05, L.ancho || 0.9, L.inicio || L.puertaX || 0);
  const zonasPaso = {};
  for (const Z of Object.values(L.zonas)) {
    const m = mapa.zonas[Z.id];
    zonasPaso[Z.id] = { alcanzable_m2: m.alcanzable_m2, libre_m2: m.libre_m2 };
    if (!m.alcanzable && (Z.publica || !L.debe || L.debe.includes(Z.id))) (Z.publica ? err : av).push(`paso: la zona ${Z.publica ? 'pública' : 'de trabajo'} «${Z.id}» no se alcanza desde la puerta con ${L.ancho || 0.9} m de paso`);
  }
  for (const a of L.avisos || []) av.push(a);
  // ---- luz
  const K_ = K.iluminacion, nl = L.luces.length;
  if (nl < K_.fuentes[0] || nl > K_.fuentes[1]) err.push(`luz: ${nl} fuentes, el kit pide ${K_.fuentes.join('–')}`);
  for (const l of L.luces) {
    if(L.modoLuz==='casa'){if(!(l.intensidad>0)||!(l.alcance>0))err.push('luz: luminaria doméstica sin intensidad o alcance');}
    else if (l.k < K_.temperatura_k[0] || l.k > K_.temperatura_k[1]) err.push(`luz: ${l.k} K fuera de ${K_.temperatura_k.join('–')}`);
  }
  const luzZona = {};
  for (const Z of Object.values(L.zonas)) {
    if (!Z.publica) continue;
    let min = Infinity;
    for (let x = Z.x0 + 0.3; x < Z.x1 - 0.2; x += 0.6) for (let z = Z.z0 + 0.3; z < Z.z1 - 0.2; z += 0.6) {
      let e = 0;
      for (const l of L.luces) { const dx = l.x - x, dz = l.z - z, dy = l.y - 0.8, d2 = dx * dx + dy * dy + dz * dz; e += (dy / Math.sqrt(d2)) / d2 * (L.modoLuz==='casa'?l.intensidad/5.5:1); }
      min = Math.min(min, e);
    }
    luzZona[Z.id] = +min.toFixed(3);
    if (min < (K_.iluminancia_min ?? 0.03)) err.push(`luz: la zona «${Z.id}» se queda a oscuras (${min.toFixed(3)} < ${K_.iluminancia_min ?? 0.03})`);
  }
  // ---- rendimiento
  let tris = 0, mallas = 0;
  h.group.traverse((o) => { if (o.isMesh) { mallas++; const g = o.geometry; tris += (g.index ? g.index.count : g.attributes.position.count) / 3; } });
  const B = presupuesto.interior;
  if (tris > B.triangulos_max) err.push(`rendimiento: ${Math.round(tris)} triángulos > ${B.triangulos_max}`);
  if (mallas > B.mallas_max) err.push(`rendimiento: ${mallas} mallas > ${B.mallas_max}`);
  if (nl > B.luces_max) err.push(`rendimiento: ${nl} luces > ${B.luces_max}`);
  const distintos = new Set(C.map((c) => c.obj)).size;
  return { kit: L.kit, tipologia: L.tipologia, seed: L.seed, W, D, guardias: L.guardias, objetos: C.length, distintos, hash: L.hash, errores: err, avisos: av, recuento, paso: zonasPaso, luz: luzZona, flotando: flot, interpenetraciones: inter, triangulos: Math.round(tris), mallas, luces: nl };
}

// how different two layouts are: the share of the objects of one with no match in the other (the same object within
// 5 cm and 8°)
function diferencia(A, B) {
  let match = 0;
  const used = new Set();
  for (const a of A) {
    const j = B.findIndex((b, k) => !used.has(k) && b.obj === a.obj && Math.hypot(b.x - a.x, b.z - a.z) < 0.05 && Math.abs(b.y - a.y) < 0.05 && Math.abs(((b.ry - a.ry + Math.PI) % (2 * Math.PI)) - Math.PI) < 8 * DEG);
    if (j >= 0) { used.add(j); match++; }
  }
  return 1 - match / Math.max(A.length, B.length);
}

// the households a home's room is laid out for, one per seed: every profile of neighbour in turn, with its styles and
// what it has to take (src/houses.js PROFILES)
function hogarDe(K, s, tip) {
  if (!K.objetos.some((e) => e.perfil || e.estilo || e.botin || e.habitacion)) return null;
  const ids = Object.keys(PROFILES), id = ids[(s - 1) % ids.length], P = PROFILES[id];
  const habitacion=tip==='vivienda_ninos'?'ninos':tip==='vivienda_joven'?'dormJoven':Math.floor((s - 1) / (ids.length * 2)) % 2 ? 'dorm2' : 'dorm';
  return { perfil: id, estilo: P.styles[Math.floor((s - 1) / ids.length) % P.styles.length], botin: P.loot, habitacion };
}

export async function validar(tip, seeds = [1, 2, 3]) {
  const presupuesto = await (await fetch('/data/quality_budgets.json')).json();
  const out = [];
  for (const s of seeds) {
    const hogar = hogarDe(KITS[tip], s,tip);
    // Las estancias usan puerta doméstica (0,86 m + sus márgenes), no el acceso de 1,5 m de un comercio.
    const puertaLab = KITS[tip].puerta ?? 0;
    const contexto = tip.startsWith('vivienda_') ? { libres: [{ cx: puertaLab, cz: 0.5, hw: 0.58, hd: 0.5, a: 0, y0: 0, y1: 2.4 }], inicio: { x: puertaLab, z: 0.5 } } : null;
    const h = buildLocal(tip, s, ORIGIN, 'Validación', hogar, contexto);
    const rep = revisar(h, presupuesto);
    // (I-03: the same seed again, the same layout)
    const h2 = buildLocal(tip, s, ORIGIN, 'Validación', hogar, contexto);
    if (hogar) {rep.hogar = `${hogar.perfil} · ${hogar.estilo}`;rep.contexto_hogar=hogar;}
    rep.determinista = h2.local.hash === h.local.hash;
    if (!rep.determinista) rep.errores.push(`variación: la semilla ${s} da otro trazado la segunda vez`);
    rep._c = h.local.colocados.map((c) => ({ obj: c.obj, x: c.x, y: c.y, z: c.z, ry: c.ry }));
    h.group.traverse((o) => { if (o.isMesh) o.geometry.dispose(); }); h2.group.traverse((o) => { if (o.isMesh) o.geometry.dispose(); });
    out.push(rep);
  }
  for (let i = 1; i < out.length; i++) {
    const d = diferencia(out[0]._c, out[i]._c);
    out[i].diferencia_con_semilla_1 = +d.toFixed(3);
    if (d < 0.3) out[i].errores.push(`variación: con la semilla ${out[i].seed} solo cambia un ${(d * 100).toFixed(0)} % (el backlog pide ≥ 30 %)`);
  }
  for (const r of out) delete r._c;
  return out;
}

// the neighbours' houses (epic I, vivienda por estancia): each house built as the game builds it, and every room of it
// furnished from a kit checked as an interior is — its household's entries, nothing floating or run into another, the way
// through from its door — (its light is the house's: not checked here), and the house within the interior budget
export async function validarCasas(seeds, opts = {}) {
  const presupuesto = await (await fetch('/data/quality_budgets.json')).json(), B = presupuesto.interior, out = [];
  for (const s of seeds) {
    const t0=performance.now(),h = buildVecino(s, ORIGIN), err = [],montaje=performance.now()-t0;
    let tris = 0,mallas=0;
    h.group.traverse((o) => { if (o.isMesh&&o.visible) {mallas++;tris += (o.geometry.index ? o.geometry.index.count : o.geometry.attributes.position.count) / 3;} });
    if (tris > B.triangulos_max) err.push(`rendimiento: ${Math.round(tris)} triángulos > ${B.triangulos_max}`);
    if(mallas>B.mallas_max)err.push(`rendimiento: ${mallas} mallas > ${B.mallas_max}`);
    if(h.lights.length>B.luces_max)err.push(`rendimiento: ${h.lights.length} luces > ${B.luces_max}`);
    if(montaje>B.entrada_ms_max)err.push(`rendimiento: montaje ${montaje.toFixed(1)} ms > ${B.entrada_ms_max}`);
    const salas = [];
    const habitables = h.rooms.filter((q) => q.type !== 'pasillo' && q.type !== 'hall');
    const faltantes = habitables.filter((q) => !h.estancias.some((e) => e.sala === q.id)).map((q) => ({ sala: q.id, tipo: q.type, kit: kitDeEstancia(q.type, h.profile.id) }));
    const cobertura = { habitables: habitables.length, porKit: h.estancias.length, faltantes };
    for (const f of h.fallosKit || []) err.push(`montaje: ${f.sala} (${f.kit}): ${f.motivo}`);
    for(const f of h.fallosUso||[])err.push('uso: '+f);
    const uso=revisarUso(h);err.push(...uso.errores.map(e=>'uso: '+e));
    for (const f of faltantes) if (opts.exigirTodas || (opts.exigirKits || []).includes(f.kit)) err.push(`cobertura: ${f.sala} sin ${f.kit || 'kit de habitación conocido'}`);
    for (const est of h.estancias) {
      const rep = revisar({ local: est, group: { traverse() {} } }, { interior: { triangulos_max: Infinity, mallas_max: Infinity, luces_max: Infinity } });
      const e = rep.errores;
      for (const x of e) err.push(`${est.sala} (${est.kit}): ${x}`);
      salas.push({ sala: est.sala, kit: est.kit, objetos: est.colocados.length, distintos: rep.distintos,luces:est.luces,luz:rep.luz, errores: e.length });
    }
    out.push({ seed: s, perfil: h.profile.id, estilo: h.profile.style, plano: h.profile.layout, triangulos: Math.round(tris),mallas,luces:h.lights.length,montaje_ms:+montaje.toFixed(1), cobertura, salas, errores: err });
    h.group.traverse((o) => { if (o.isMesh) o.geometry.dispose(); });
  }
  return out;
}

// Distancia de uso desde celdas alcanzables por un cuerpo de 0,8 m, incluida la planta alta.
// Los muebles conservan sus anclajes; esto no confunde el centro de una cama con el sitio donde se despierta.
export function revisarUso(h){
  const errores=[],puntos=[],comprobados=new Set();
  for(const est of h.estancias){
    if(!est.origen){errores.push(est.sala+': falta marco mundial');continue;}
    const M=mapaPaso(est,est.colocados.flatMap(partes),.05,est.ancho,est.inicio),or=est.origen;
    const cerca=(x,z)=>{let d=Infinity;for(let c=0;c<M.reach.length;c++)if(M.reach[c])d=Math.min(d,Math.hypot(or.x-est.W/2+(c%M.nx+.5)*M.S-x,or.z+(Math.floor(c/M.nx)+.5)*M.S-z));return d;};
    const rm=h.rooms.find(r=>r.id===est.sala);
    for(const i of h.inter){
      if(!['eat','fridge','hide','drawer','piano','guitar','read','mirror','loot'].includes(i.type)||Math.abs((i.y||0)-or.y)>.2)continue;
      if(i.sala?i.sala!==est.sala:i.x<rm.x0||i.x>rm.x1||i.z<rm.z0||i.z>rm.z1)continue;
      comprobados.add(i);
      const d=cerca(i.x,i.z),ok=d<=(i.r||.8)-.05;puntos.push({sala:est.sala,tipo:i.type,distancia:+d.toFixed(3),ok});
      if(!ok)errores.push(est.sala+'/'+i.type+': sin acceso a distancia de uso');
    }
    for(const b of h.pieces.bed.filter(b=>b.rm.id===est.sala)){
      const d=cerca(b.side.x,b.side.z),ok=d<=.18;puntos.push({sala:est.sala,tipo:'despertar',distancia:+d.toFixed(3),ok});
      if(!ok)errores.push(est.sala+'/despertar: salida de cama ocupada');
    }
  }
  for(const i of h.inter)if(['eat','fridge','hide','drawer','piano','guitar','mirror','loot'].includes(i.type)&&!comprobados.has(i)){
    const rm=h.rooms.find(r=>['hall','pasillo'].includes(r.type)&&r.lv===((i.y||0)>2?1:0)&&i.x>=r.x0&&i.x<=r.x1&&i.z>=r.z0&&i.z<=r.z1);
    if(rm){
      const q={x:i.x,z:i.z},col=h.levels?.[rm.lv]||h.collider;col.resolveCircle(q,.4);
      const d=Math.hypot(q.x-i.x,q.z-i.z),ok=d<(i.r||.8)-.05;
      puntos.push({sala:rm.id,tipo:i.type,distancia:+d.toFixed(3),ok});
      if(!ok)errores.push(rm.id+'/'+i.type+': pasillo ocupado');
    }else errores.push(i.type+': interacción fuera de su habitación o planta');
  }
  return {errores,puntos};
}
