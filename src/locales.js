// The town's businesses inside, from their kit (technical backlog, epic I): a kit (data/kits/<tipología>.json) says the
// room's size, its zones — the counter, behind it, the tables, the toilet, the storeroom —, its partitions and, zone by
// zone, which objects of the catalogue (data/objetos) go there, how many and by what rule; buildLocal lays them out with
// the interior's own seed (I-03: the same seed, the same room) and builds the room around them. Nothing it lays down
// may shut a zone off from the street door (a body 0.9 m wide, src/interiores_geo.js). What it laid out stays on the
// result (h.local.colocados) for the validator (tools/interiores/validar.py, I-04).
// Frame: the street door at z = 0, the back wall at z = D, x from -W/2 to W/2 (metres, from the interior's origin): the
// walls' inner faces, so a zone that runs to a wall ends at its face.
import * as THREE from 'three';
import { INTERIOR_ORIGIN, planeGeo, boxGeo, HouseBuilder, std, texMat, glassMat, T as MURO } from './housekit.js';
import { KITS, OBJETOS } from './interiores_datos.js';
import { caja, construir, kelvin } from './objetos.js';
import { rot, partes, penetra, superficie, mapaPaso, espacioFrontal } from './interiores_geo.js';
import { mulberry32, hash1 } from './util.js';

const TOL = 0.005; // (half the validator's centimetre: what the layout lets touch, the validator lets pass)
const MIRA = { '+z': 0, '-z': Math.PI, '+x': Math.PI / 2, '-x': -Math.PI / 2 };
// a wall of a zone: where it runs, the way into the room (n), the facing of what stands against it
const PARED = {
  E: (z) => ({ fijo: z.x1, a: z.z0, b: z.z1, eje: 'z', n: [-1, 0], ry: -Math.PI / 2 }),
  W: (z) => ({ fijo: z.x0, a: z.z0, b: z.z1, eje: 'z', n: [1, 0], ry: Math.PI / 2 }),
  N: (z) => ({ fijo: z.z1, a: z.x0, b: z.x1, eje: 'x', n: [0, -1], ry: Math.PI }),
  S: (z) => ({ fijo: z.z0, a: z.x0, b: z.x1, eje: 'x', n: [0, 1], ry: 0 }),
};

// ---------------------------------------------------------------- an object's footprint and volume where it stands
function volumen(it) {
  const b = caja(it.obj);
  const [cx, cz] = rot((b.x0 + b.x1) / 2, (b.z0 + b.z1) / 2, it.ry);
  return { cx: it.x + cx, cz: it.z + cz, hw: b.w / 2, hd: b.d / 2, a: it.ry, y0: (it.y || 0) + b.y0, y1: (it.y || 0) + b.y1 };
}
// do two volumes overlap by more than a centimetre? (heights, then the two footprints by separating axes)
export function choca(A, B, tol = TOL) {
  if (Math.min(A.y1, B.y1) - Math.max(A.y0, B.y0) <= tol) return false;
  const axes = [[Math.cos(A.a), -Math.sin(A.a)], [Math.sin(A.a), Math.cos(A.a)], [Math.cos(B.a), -Math.sin(B.a)], [Math.sin(B.a), Math.cos(B.a)]];
  const dx = B.cx - A.cx, dz = B.cz - A.cz;
  for (const [ux, uz] of axes) {
    const ra = A.hw * Math.abs(Math.cos(A.a) * ux - Math.sin(A.a) * uz) + A.hd * Math.abs(Math.sin(A.a) * ux + Math.cos(A.a) * uz);
    const rb = B.hw * Math.abs(Math.cos(B.a) * ux - Math.sin(B.a) * uz) + B.hd * Math.abs(Math.sin(B.a) * ux + Math.cos(B.a) * uz);
    if (Math.abs(dx * ux + dz * uz) >= ra + rb - tol) return false;
  }
  return true;
}
const grow = (v, m) => ({ ...v, hw: v.hw + m, hd: v.hd + m });

// does a household fit an entry's list (perfil, estilo)? a list of names, or of «!name» left out
export const encaja = (lista, valor) => !lista || (lista.some((t) => t.startsWith('!')) ? !lista.includes('!' + valor) : lista.includes(valor));
// the entries of a kit that belong to a household { perfil, estilo, botin: [what it has to take] } (src/houses.js does
// its own, taking the loot from the house's pool as it goes)
export const filtroHogar = (hogar) => (e) => encaja(e.perfil, hogar.perfil) && encaja(e.estilo, hogar.estilo) && encaja(e.habitacion, hogar.habitacion) && (!e.botin || (hogar.botin || []).includes(e.botin));

// the layout alone, with no room built: the kit's objects in its frame, laid out with this seed. ctx, for a room of a
// house (src/houses.js): { W, D, H } its size instead of the kit's ranges, inicio { x, z } where one comes in (the way
// through starts there), libres the house's own clear areas (the swing of its doors; its windows: nothing tall or hung
// there), filtro (whether an entry belongs to this household: its profile, its style)
export function amueblar(kit, seed = 1, ctx = null) {
  const K = KITS[kit];
  if (!K) throw new Error('sin kit: ' + kit);
  const tipologia = K.tipologia, reservaUso=K.objetos.some(e=>e.espacio_frontal);
  const r = mulberry32((seed * 2654435761 + 97) >>> 0);
  const U = (a) => (Array.isArray(a) ? a[0] + r() * (a[1] - a[0]) : a);
  const N = (a) => (Array.isArray(a) ? a[0] + Math.floor(r() * (a[1] - a[0] + 1)) : a);
  // (a shuffle of its own: sort() with a random comparator asks for a different number of draws from one run to the next)
  const baraja = (a) => { for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(r() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
  const q3 = (a) => a[0] + Math.round((r() * (a[1] - a[0])) / 0.3) * 0.3;
  const W = ctx && ctx.W != null ? ctx.W : q3(K.superficie.ancho), D = ctx && ctx.D != null ? ctx.D : q3(K.superficie.fondo), H = (ctx && ctx.H) || K.superficie.alto || 3.3;
  const env = { W, D, H };
  const ev = (e) => (typeof e === 'number' ? e : Function(...Object.keys(env), `return (${e});`)(...Object.values(env)));
  for (const [k, v] of Object.entries(K.variables || {})) env[k] = ev(v);
  const puertaX = K.puerta != null ? ev(K.puerta) : 0, ancho = K.paso_libre || 0.9, avisos = [];

  // ---- the partitions, the zones (up to the partitions' faces) and what is kept clear: the street door's way in, both
  // sides of each partition door (as deep as its leaf swings), and the kit's own (the place to order at the counter)
  const libres = ctx && ctx.libres ? [...ctx.libres] : [{ cx: puertaX, cz: 0.6, hw: 0.75, hd: 0.6, a: 0, y0: 0, y1: 2.2 }];
  const inicio = ctx && ctx.inicio ? ctx.inicio : puertaX; // (where the way through starts: the street door, or the room's)
  const tabiques = (K.tabiques || []).map((t) => {
    const [ax, az] = t.de.map(ev), [bx, bz] = t.a.map(ev);
    const o = { ax, az, bx, bz };
    if (t.puerta) {
      const L = Math.hypot(bx - ax, bz - az), ux = (bx - ax) / L, uz = (bz - az) / L, s = ev(t.puerta[0]), w = t.puerta[1], fondo = Math.max(0.75, w + 0.05);
      o.hueco = [s, s + w];
      const mx = ax + ux * (s + w / 2), mz = az + uz * (s + w / 2);
      libres.push({ cx: mx, cz: mz, hw: Math.abs(ux) * (w / 2 + 0.05) + Math.abs(uz) * fondo, hd: Math.abs(uz) * (w / 2 + 0.05) + Math.abs(ux) * fondo, a: 0, y0: 0, y1: 2.2 });
    }
    return o;
  });
  for (const l of K.libres || []) { const [x0, z0, x1, z1] = l.rect.map(ev); libres.push({ cx: (x0 + x1) / 2, cz: (z0 + z1) / 2, hw: Math.abs(x1 - x0) / 2, hd: Math.abs(z1 - z0) / 2, a: 0, y0: 0, y1: 2.2 }); }
  const zonas = {};
  for (const z of K.zonas) { const [x0, z0, x1, z1] = z.rect.map(ev); zonas[z.id] = { id: z.id, publica: !!z.publica, x0: Math.min(x0, x1), z0: Math.min(z0, z1), x1: Math.max(x0, x1), z1: Math.max(z0, z1) }; }
  const t2 = MURO / 2;
  for (const Z of Object.values(zonas)) for (const t of tabiques) {
    if (Math.abs(t.ax - t.bx) < 1e-6) { // (a partition along z)
      if (Math.min(Z.z1, Math.max(t.az, t.bz)) - Math.max(Z.z0, Math.min(t.az, t.bz)) <= 0.05) continue;
      if (Math.abs(Z.x1 - t.ax) < 0.1) Z.x1 = t.ax - t2;
      if (Math.abs(Z.x0 - t.ax) < 0.1) Z.x0 = t.ax + t2;
    } else if (Math.abs(t.az - t.bz) < 1e-6) { // (along x)
      if (Math.min(Z.x1, Math.max(t.ax, t.bx)) - Math.max(Z.x0, Math.min(t.ax, t.bx)) <= 0.05) continue;
      if (Math.abs(Z.z1 - t.az) < 0.1) Z.z1 = t.az - t2;
      if (Math.abs(Z.z0 - t.az) < 0.1) Z.z0 = t.az + t2;
    }
  }
  // is there a wall (the room's or a partition's face) along x = const or z = const at this point?
  const muroX = (x, z) => Math.abs(Math.abs(x) - W / 2) < 0.1 || tabiques.some((t) => Math.abs(t.ax - t.bx) < 1e-6 && Math.abs(Math.abs(x - t.ax) - t2) < 0.1 && z > Math.min(t.az, t.bz) - 0.1 && z < Math.max(t.az, t.bz) + 0.1);
  const muroZ = (x, z) => Math.abs(z) < 0.1 || Math.abs(z - D) < 0.1 || tabiques.some((t) => Math.abs(t.az - t.bz) < 1e-6 && Math.abs(Math.abs(z - t.az) - t2) < 0.1 && x > Math.min(t.ax, t.bx) - 0.1 && x < Math.max(t.ax, t.bx) + 0.1);

  // ---- what is laid out: [{ obj, zona, regla, x, y, z, ry, sop (index of what it stands on), sup (its surface), v }]
  const P = [];
  const planta = { W, D, zonas, tabiques };
  // the zones a body reaches from the door (in the empty room, then with the kit's fixed build: the counter): whatever
  // else is laid out must leave them all within reach
  const alcanza = (extra = [], sin = -1) => {
    const piezas = [];
    P.forEach((p, j) => { if (j !== sin) for (const q of partes(p)) piezas.push(q); });
    for (const it of extra) for (const q of partes(it)) piezas.push(q);
    const z = mapaPaso(planta, piezas, 0.05, ancho, inicio).zonas;
    return Object.keys(z).filter((id) => z[id].alcanzable > 0);
  };
  let debe = alcanza(), guardias = 0;
  for (const Z of Object.values(zonas)) if (Z.publica && !debe.includes(Z.id)) avisos.push(`la zona pública «${Z.id}» no se alcanza ni con el local vacío`);
  const cierra = (nuevos, sin = -1) => {
    guardias++;
    if(reservaUso){
      const candidatos=P.filter((p,i)=>i!==sin).concat(nuevos);
      for(const p of candidatos){
        const e=K.objetos[p.e??entrada];
        if(!e?.espacio_frontal)continue;
        const R=espacioFrontal(p,caja(p.obj),e.espacio_frontal);
        if(!dentro(R,zonas[e.zona])||candidatos.some(q=>q!==p&&partes(q).some(v=>penetra(R,v)>TOL)))return true;
      }
    }
    if(!ctx?.funciones){const a=alcanza(nuevos,sin);return debe.some(id=>!a.includes(id));}
    const objetos=P.filter((p,i)=>i!==sin).concat(nuevos),mapa=mapaPaso(planta,objetos.flatMap(partes),.05,ancho,inicio);
    if(debe.some(id=>!mapa.zonas[id]?.alcanzable))return true;
    const llega=(x,z,radio)=>{const x0=Math.max(0,Math.floor((x-radio+W/2)/mapa.S)),x1=Math.min(mapa.nx-1,Math.ceil((x+radio+W/2)/mapa.S)),z0=Math.max(0,Math.floor((z-radio)/mapa.S)),z1=Math.min(mapa.nz-1,Math.ceil((z+radio)/mapa.S));for(let k=z0;k<=z1;k++)for(let i=x0;i<=x1;i++)if(mapa.reach[k*mapa.nx+i]&&Math.hypot(-W/2+(i+.5)*mapa.S-x,(k+.5)*mapa.S-z)<=radio)return true;return false;};
    for(const p of objetos){
      if(K.objetos[p.e]?.botin){const b=caja(p.obj);if(!llega(p.x+(b.x0+b.x1)/2,p.z+(b.z0+b.z1)/2,.85))return true;}
      const rol=OBJETOS[p.obj].rol;if(!rol)continue;
      const b=caja(p.obj),punto=(x,z)=>{const [dx,dz]=rot(x,z,p.ry);return [p.x+dx,p.z+dz];};
      if(rol==='cama'||rol==='cama_doble'){
        if(![[b.x1+.45,(b.z0+b.z1)/2],[b.x0-.45,(b.z0+b.z1)/2],[(b.x0+b.x1)/2,b.z1+.45]].some(q=>llega(...punto(...q),.3)))return true;
      }else if(['cocina','nevera','armario','comoda','libros','piano','guitarra','espejo','tv','telefono'].includes(rol)&&!llega(...punto((b.x0+b.x1)/2,b.z1+.5),.65))return true;
    }
    return false;
  };
  // (how far an object's parts run into another's)
  const hunde = (A, B) => { let m = 0; for (const a of partes(A)) for (const b of partes(B)) m = Math.max(m, penetra(a, b)); return m; };
  const dentro = (v, z) => {
    // the footprint's corners inside the zone (a hand of slack)
    for (const [sx, sz] of [[-1, -1], [1, -1], [1, 1], [-1, 1]]) {
      const [ox, oz] = rot(sx * v.hw, sz * v.hd, v.a);
      const x = v.cx + ox, zz = v.cz + oz;
      if (x < z.x0 - TOL || x > z.x1 + TOL || zz < z.z0 - TOL || zz > z.z1 + TOL) return false;
    }
    return true;
  };
  const libre = (v) => !P.some((p) => p.v && choca(p.v, v)) && !libres.some((l) => choca(l, v, 0));
  let entrada = -1; // (the kit's entry being laid out: the validator counts by it)
  const poner = (obj, zona, regla, x, y, z, ry, sop = null, sup = null) => {
    const it = { obj, zona, regla, x, y, z, ry, sop, sup, e: entrada };
    it.v = volumen(it);
    P.push(it);
    return it;
  };
  // the object's origin for its footprint's centre to land at (cx, cz) turned ry
  const origen = (obj, cx, cz, ry) => { const b = caja(obj); const [ox, oz] = rot((b.x0 + b.x1) / 2, (b.z0 + b.z1) / 2, ry); return [cx - ox, cz - oz]; };
  const tantos = (e, len = 0, area = 0, sops = 0) => (e.cantidad ? N(e.cantidad) : e.por_m ? Math.max(1, Math.round(len * U(e.por_m))) : e.por_m2 ? Math.max(1, Math.round(area * U(e.por_m2))) : e.por_soporte && !Array.isArray(e.por_soporte) ? sops * e.por_soporte : 1);
  const cantidadPreferida=e=>e.preferir&&Array.isArray(e.cantidad)?e.cantidad[1]:N(e.cantidad||1);
  const variante = (e, k) => (e.variantes ? (e.todas && k < e.variantes.length ? e.variantes[k] : e.variantes[Math.floor(r() * e.variantes.length)]) : e.obj);
  const cursores = {}, estantes = {}, activas = []; // (activas: the entries laid out for this household)

  const reglas = {
    // Acompañantes en el mismo marco: módulos de cocina, mesitas junto al cabecero y sillas de escritorio.
    // Si una puerta impide la relación, solo las entradas que lo permiten buscan otra pared.
    junto_a(e, Z) {
      const ids = [].concat(e.de), n = cantidadPreferida(e);
      for(let k=0;k<n;k++) {
        const refs=[...P].reverse().filter(p=>p.zona===Z.id && ids.includes(p.obj));
        if(!refs.length) break;
        if(!e.buscar_refs)refs.splice(1);
        const obj=variante(e,k), b=caja(obj), lados=e.lados || ['derecha','izquierda'];
        let ok=false;
        // Un frente modular puede prolongarse por cualquiera de sus extremos.
        // Los demás kits conservan su referencia anterior por defecto.
        referencias: for(const ref of refs) for(const lado of lados) {
          const rb=caja(ref.obj);
          const lx=lado==='derecha'?rb.x1+b.w/2+.04:lado==='izquierda'?rb.x0-b.w/2-.04:(rb.x0+rb.x1)/2;
          const lz=lado==='frente'?rb.z1+b.d/2+.06:rb.z0+b.d/2;
          const [dx,dz]=rot(lx,lz,ref.ry), ry=ref.ry+(lado==='frente'&&e.mira_ref?Math.PI:0);
          let [x,z]=origen(obj,ref.x+dx,ref.z+dz,ry);
          if(OBJETOS[obj].soporte==='pared'){
            const [bx,bz]=rot(0,b.z0,ry),sn=Math.sin(ry),cs=Math.cos(ry);
            if(Math.abs(sn)>.5)x=(sn>0?Z.x0:Z.x1)+sn*.003-bx;
            else z=(cs>0?Z.z0:Z.z1)+cs*.003-bz;
          }
          const it={obj,x,y:0,z,ry}, v=volumen(it);
          if(dentro(v,Z)&&libre(v)&&!cierra([it])) {poner(obj,Z.id,OBJETOS[obj].soporte==='pared'?'pared':'junto_a',x,0,z,ry);ok=true;break referencias;}
        }
        if(!ok) {if(e.si_no!==false) (OBJETOS[obj].soporte==='pared'?reglas.pared:reglas.contra_pared)({...e,pared:'*',cantidad:1},Z);break;}
      }
    },
    // the counter's modules, end to end along a line (the kit's own design: never moved, never refused)
    modulos(e, Z) {
      const [fijo, a, b] = e.linea.map(ev), ry = MIRA[e.mira || '+z'], w = caja(e.obj).w, n = Math.floor((b - a + 1e-6) / w), s0 = a + (b - a - n * w) / 2;
      for (let i = 0; i < n; i++) { const c = s0 + w * (i + 0.5); const [x, z] = origen(e.obj, e.eje === 'z' ? fijo : c, e.eje === 'z' ? c : fijo, ry); poner(e.obj, Z.id, 'modulos', x, 0, z, ry); }
    },
    fila(e, Z) {
      const [fijo, a, b] = e.linea.map(ev), ry = MIRA[e.mira || '+z'];
      for (let c = a, k = 0; c <= b + 1e-6; c += e.cada, k++) {
        const obj = variante(e, k), [x, z] = origen(obj, e.eje === 'z' ? fijo : c, e.eje === 'z' ? c : fijo, ry);
        const it = { obj, x, y: 0, z, ry };
        if (libre(volumen(it)) && !cierra([it])) poner(obj, Z.id, 'fila', x, 0, z, ry);
      }
    },
    contra_pared(e, Z) {
      // (a list of walls, or '*' any of the four: each piece against the first that takes it — a room's, whose door and
      // windows the kit cannot know)
      if (typeof e.pared !== 'string' || e.pared === '*') {
        const lados = e.pared === '*' ? baraja(['N', 'S', 'E', 'W']) : e.pared, n = cantidadPreferida(e);
        for (let puestos = 0, k = 0; puestos < n && k < n + 3; k++) {
          const n0 = P.length;
          for (const lado of lados) { reglas.contra_pared({ ...e, pared: lado, cantidad: 1, llenar: false, variantes: e.variantes ? [variante(e, puestos)] : undefined }, Z); if (P.length > n0) break; }
          if (P.length > n0) puestos++; else break;
        }
        return;
      }
      const pw = PARED[e.pared](Z), key = Z.id + e.pared;
      const n = e.llenar ? 99 : cantidadPreferida(e);
      let puestos = 0;
      for (let k = 0; puestos < n && k < 40; k++) {
        const obj = variante(e, k), b = caja(obj);
        let s = cursores[key] ?? pw.a + 0.03, ok = false;
        const slots=[];
        while(s+b.w<=pw.b-.03+1e-6){slots.push(s);s+=.1;}
        if(e.centrado) slots.sort((a,b0)=>Math.abs(a+b.w/2-(pw.a+pw.b)/2)-Math.abs(b0+b.w/2-(pw.a+pw.b)/2));
        for (s of slots) {
          const c = s + b.w / 2, off = pw.fijo + (pw.eje === 'z' ? pw.n[0] : pw.n[1]) * (b.d / 2 + 0.01);
          const [x, z] = origen(obj, pw.eje === 'z' ? off : c, pw.eje === 'z' ? c : off, pw.ry);
          const it = { obj, x, y: 0, z, ry: pw.ry }, v = volumen(it);
          if (!dentro(v,Z)||!libre(v))continue;
          // Un puesto de trabajo se acepta junto con su asiento frontal. Si no
          // cabe, se prueba otro hueco: la silla no acaba en otra pared.
          let silla=null;
          if(e.silla_frontal){
            const sb=caja(e.silla_frontal),[dx,dz]=rot((b.x0+b.x1)/2,b.z1+sb.d/2+.06,pw.ry);
            const [sx,sz]=origen(e.silla_frontal,x+dx,z+dz,pw.ry+Math.PI);
            silla={obj:e.silla_frontal,x:sx,y:0,z:sz,ry:pw.ry+Math.PI};const sv=volumen(silla);
            if(!dentro(sv,Z)||!libre(sv)||hunde(silla,it)>.005)continue;
          }
          if(cierra(silla?[it,silla]:[it]))continue;
          const puesto=poner(obj,Z.id,'contra_pared',x,0,z,pw.ry);
          if(silla){const asiento=poner(silla.obj,Z.id,'junto_a',silla.x,0,silla.z,silla.ry);asiento.de=P.indexOf(puesto);}
          cursores[key]=s+b.w+.03;ok=true;break;
        }
        if (!ok) break;
        puestos++;
      }
    },
    // against the wall facing the one `de` stands against (the sofa across from the telly)
    enfrente(e, Z) {
      const es = (q, id) => (Array.isArray(id) ? id.includes(q.obj) : q.obj === id);
      const ref = [...P].reverse().find((q) => q.zona === Z.id && es(q, e.de));
      if (!ref) return;
      const a = Math.atan2(Math.sin(ref.ry), Math.cos(ref.ry)), lado = Math.abs(a) < 0.3 ? 'S' : Math.abs(Math.abs(a) - Math.PI) < 0.3 ? 'N' : a > 0 ? 'W' : 'E';
      const n0 = P.length;
      reglas.contra_pared({ ...e, pared: { S: 'N', N: 'S', W: 'E', E: 'W' }[lado] }, Z);
      if (P.length === n0 && e.si_no !== false) reglas.contra_pared({ ...e, pared: '*' }, Z); // (no room across: against any wall)
    },
    // between two pieces, facing as the second (the coffee table between the sofa and the telly; the rug under it)
    entre(e, Z) {
      const es = (q, id) => (Array.isArray(id) ? id.includes(q.obj) : q.obj === id);
      const A = [...P].reverse().find((q) => q.zona === Z.id && es(q, e.a)), Bq = [...P].reverse().find((q) => q.zona === Z.id && es(q, e.b));
      if (!A || !Bq) return;
      const dx = Bq.v.cx - A.v.cx, dz = Bq.v.cz - A.v.cz, L = Math.hypot(dx, dz) || 1;
      for (const d of [0, 0.12, -0.12, 0.25, -0.25]) {
        const obj = variante(e, 0), ry = Bq.ry + Math.PI, [x, z] = origen(obj, (A.v.cx + Bq.v.cx) / 2 + (dx / L) * d, (A.v.cz + Bq.v.cz) / 2 + (dz / L) * d, ry);
        const it = { obj, x, y: 0, z, ry }, v = volumen(it);
        if (dentro(v, Z) && libre(v) && !cierra([it])) { poner(obj, Z.id, 'entre', x, 0, z, ry); return; }
      }
      if (e.si_no !== false) reglas.suelo_libre({ ...e, cantidad: [1, 1] }, Z); // (no room between them: wherever it fits)
    },
    // hung on a wall, its back flat on the face: at random, in a row `cada` metres apart (round what is there already),
    // or over its fellow below (sobre_de)
    pared(e, Z) {
      // (one wall, or a list of them to go on to when the first is full; a row stops at `maximo` if the kit says so)
      const ref = e.sobre_de ? P.find((p) => p.zona === Z.id && p.obj === e.sobre_de) : null;
      if(e.sobre_de&&!ref&&e.si_no===false)return; // acompañante opcional: no inventar otra pared sin su referencia
      const a=ref?Math.atan2(Math.sin(ref.ry),Math.cos(ref.ry)):0;
      const paredes = ref ? [Math.abs(a)<.3?'S':Math.abs(Math.abs(a)-Math.PI)<.3?'N':a>0?'W':'E'] : e.pared === '*' ? baraja(['N', 'S', 'E', 'W']) : [].concat(e.pared);
      const colocar = (pw, obj, s) => {
        const b = caja(obj), c = s + b.w / 2, off = pw.fijo + (pw.eje === 'z' ? pw.n[0] : pw.n[1]) * (-b.z0 + 0.003);
        const [ox, oz] = rot((b.x0 + b.x1) / 2, 0, pw.ry);
        const x = pw.eje === 'z' ? off : c - ox, z = pw.eje === 'z' ? c - oz : off;
        const it = { obj, x, y: 0, z, ry: pw.ry }, v = volumen(it);
        if (!dentro(grow(v, -0.005), Z) || !libre(v) || (b.y0 < 1.2 && cierra([it]))) return false;
        poner(obj, Z.id, 'pared', x, 0, z, pw.ry);
        return true;
      };
      if (e.cada) {
        let k = 0;
        for (const nombre of paredes) {
          const pw = PARED[nombre](Z);
          for (let s = pw.a + 0.05; !(e.maximo && k >= e.maximo);) { const obj = variante(e, k), w = caja(obj).w; if (s + w > pw.b - 0.05 + 1e-6) break; if (colocar(pw, obj, s)) { s += Math.max(e.cada, w + 0.02); k++; } else s += 0.05; }
        }
        return;
      }
      const n = cantidadPreferida(e);
      for (let puestos = 0, k = 0; puestos < n && k < n + 4; k++) {
        const obj = variante(e, puestos), w = caja(obj).w;
        let ok = false;
        for (const nombre of paredes) {
          const pw = PARED[nombre](Z), slots = [];
          if (ref) slots.push((pw.eje === 'z' ? ref.v.cz : ref.v.cx) - w / 2);
          else { const m = Math.min(0.1, Math.max(0, (pw.b - pw.a - w) / 2)); for (let s = pw.a + m; s + w <= pw.b - m + 1e-6; s += 0.15) slots.push(s); baraja(slots); }
          if (slots.some((s) => colocar(pw, obj, s))) { ok = true; break; }
        }
        if (ok) puestos++;
        else if (ref) break;
      }
    },
    // in the zone's corners that stand against a wall (both walls first), facing out of it
    esquina(e, Z) {
      const n = N(e.cantidad || 1);
      const corners = baraja([[Z.x0, Z.z0], [Z.x1, Z.z0], [Z.x0, Z.z1], [Z.x1, Z.z1]])
        .map(([cx, cz]) => ({ cx, cz, mx: muroX(cx, cz), mz: muroZ(cx, cz) }))
        .filter((c) => c.mx || c.mz)
        .sort((a, b) => b.mx + b.mz - (a.mx + a.mz));
      let puestos = 0;
      for (const { cx, cz, mz } of corners) {
        if (puestos >= n) break;
        const obj = variante(e, puestos), b = caja(obj);
        const ry = mz ? PARED[cz === Z.z0 ? 'S' : 'N'](Z).ry : PARED[cx === Z.x0 ? 'W' : 'E'](Z).ry;
        const ex = cx === Z.x0 ? 1 : -1, ez = cz === Z.z0 ? 1 : -1;
        const hx = Math.abs(Math.cos(ry)) * b.w / 2 + Math.abs(Math.sin(ry)) * b.d / 2, hz = Math.abs(Math.sin(ry)) * b.w / 2 + Math.abs(Math.cos(ry)) * b.d / 2;
        const [x, z] = origen(obj, cx + ex * (hx + 0.04), cz + ez * (hz + 0.04), ry);
        const it = { obj, x, y: 0, z, ry }, v = volumen(it);
        if (dentro(v, Z) && libre(v) && !cierra([it])) { poner(obj, Z.id, 'esquina', x, 0, z, ry); puestos++; }
      }
      // (no corner free: against any wall of the zone, wherever it fits)
      for (const lado of ['N', 'S', 'E', 'W']) {
        if (puestos >= n) break;
        const pw = PARED[lado](Z), mid = (pw.a + pw.b) / 2;
        if (!(pw.eje === 'z' ? muroX(pw.fijo, mid) : muroZ(mid, pw.fijo))) continue;
        const obj = variante(e, puestos), b = caja(obj);
        for (let s = pw.a + 0.04; s + b.w <= pw.b - 0.04 + 1e-6 && puestos < n; s += 0.15) {
          const c = s + b.w / 2, off = pw.fijo + (pw.eje === 'z' ? pw.n[0] : pw.n[1]) * (b.d / 2 + 0.03);
          const [x, z] = origen(obj, pw.eje === 'z' ? off : c, pw.eje === 'z' ? c : off, pw.ry);
          const it = { obj, x, y: 0, z, ry: pw.ry }, v = volumen(it);
          if (dentro(v, Z) && libre(v) && !cierra([it])) { poner(obj, Z.id, 'esquina', x, 0, z, pw.ry); puestos++; }
        }
      }
    },
    suelo_libre(e, Z) {
      const n = N(e.cantidad || 1);
      let puestos = 0;
      for (let t = 0; puestos < n && t < 200; t++) {
        const obj = variante(e, puestos), b = caja(obj), ry = (Math.floor(r() * 4) * Math.PI) / 2 + (r() - 0.5) * 0.28;
        const cx = Z.x0 + b.w / 2 + 0.1 + r() * Math.max(0, Z.x1 - Z.x0 - b.w - 0.2), cz = Z.z0 + b.d / 2 + 0.1 + r() * Math.max(0, Z.z1 - Z.z0 - b.d - 0.2);
        const [x, z] = origen(obj, cx, cz, ry);
        const it = { obj, x, y: 0, z, ry }, v = volumen(it);
        if (dentro(v, Z) && libre(v) && !cierra([it])) { poner(obj, Z.id, 'suelo_libre', x, 0, z, ry); puestos++; }
      }
    },
    // rows of units end to end, back to back in pairs (doble), an aisle between and at both ends: a supermarket's gondolas,
    // a shop's island shelving. eje: the way the rows run ('z', the default, or 'x'); pasillo: the aisles (1.2 m)
    filas(e, Z) {
      const b = caja(e.obj), prof = b.d, w = b.w, pas = e.pasillo || 1.2, doble = e.doble !== false, porZ = e.eje !== 'x';
      const [a0, a1] = porZ ? [Z.z0, Z.z1] : [Z.x0, Z.x1], [c0, c1] = porZ ? [Z.x0, Z.x1] : [Z.z0, Z.z1];
      const [m0, m1] = e.margen || [pas, pas], n = Math.floor((a1 - a0 - m0 - m1 + 1e-6) / w);
      const paso = (doble ? 2 * prof : prof) + pas, nf = Math.floor((c1 - c0 - pas + 1e-6) / paso);
      if (n < 1 || nf < 1) return;
      const s0 = a0 + m0 + (a1 - a0 - m0 - m1 - n * w) / 2, ini = c0 + pas + (c1 - c0 - pas - nf * paso) / 2;
      for (let f = 0; f < nf; f++) {
        const base = ini + f * paso;
        for (const [c, lado] of doble ? [[base + prof / 2, -1], [base + prof * 1.5, 1]] : [[base + prof / 2, 1]]) {
          const ry = porZ ? (lado < 0 ? -Math.PI / 2 : Math.PI / 2) : (lado < 0 ? Math.PI : 0); // (facing its aisle)
          for (let i = 0; i < n; i++) {
            const t = s0 + w * (i + 0.5), [x, z] = origen(e.obj, porZ ? c : t, porZ ? t : c, ry);
            const it = { obj: e.obj, x, y: 0, z, ry }, v = volumen(it);
            if (dentro(v, Z) && libre(v) && !cierra([it])) poner(e.obj, Z.id, 'filas', x, 0, z, ry);
          }
        }
      }
    },
    // a table with its chairs round it (where they fit: two at least, or the kit's own sides — a desk's chair behind it —,
    // or none), each set a clear way from anything else on the floor; tried first on a grid a set and an aisle apart
    // (shifted at random), then anywhere. giro: the turns the table may take (degrees; 0 by default)
    conjunto(e, Z) {
      const area = (Z.x1 - Z.x0) * (Z.z1 - Z.z0), n = e.preferir && e.cantidad ? e.cantidad[1] : tantos(e, 0, area), paso = ancho + 0.1;
      const lejos = (v) => !P.some((p) => p.v && p.v.y0 < 0.5 && choca(p.v, grow(v, paso)));
      const cand = [], pitch = 1.6 + paso, gx0 = Z.x0 + 0.8 + r() * 0.4, gz0 = Z.z0 + 0.8 + r() * 0.4;
      for (let x = gx0; x <= Z.x1 - 0.6; x += pitch) for (let z = gz0; z <= Z.z1 - 0.6; z += pitch) cand.push([x + (r() - 0.5) * 0.3, z + (r() - 0.5) * 0.3]);
      baraja(cand);
      for (let t = 0; t < 250; t++) cand.push([Z.x0 + 0.5 + r() * (Z.x1 - Z.x0 - 1.0), Z.z0 + 0.5 + r() * (Z.z1 - Z.z0 - 1.0)]);
      let puestos = 0;
      for (const [cx, cz] of cand) {
        if (puestos >= n) break;
        const giros = e.giro || [0], mesa = variante(e, puestos), mb = caja(mesa), ry = (giros[Math.floor(r() * giros.length)] * Math.PI) / 180 + (r() - 0.5) * 0.28;
        const [mx, mz] = origen(mesa, cx, cz, ry);
        const mesaIt = { obj: mesa, x: mx, y: 0, z: mz, ry }, mv = volumen(mesaIt);
        if (!dentro(mv, Z) || !libre(mv) || !lejos(mv)) continue;
        const S = e.sillas || { variantes: [], n: 0 }, silla = S.variantes.length ? S.variantes[Math.floor(r() * S.variantes.length)] : null, sb = silla && caja(silla), ns = silla ? N(S.n) : 0;
        const LADO = { '+z': [0, 1], '-z': [0, -1], '+x': [1, 0], '-x': [-1, 0] };
        const sillas = [];
        for (const [sx, sz] of S.lados ? S.lados.map((l) => LADO[l]) : baraja([[0, 1], [0, -1], [1, 0], [-1, 0]])) {
          if (sillas.length >= ns) break;
          let dist = (sx ? mb.w : mb.d) / 2 + sb.d / 2 - 0.1 + (r() - 0.5) * 0.06, it;
          const sesgo = (r() - 0.5) * 0.28; // (facing the table, a little askew)
          let suelta = false;
          for (let t = 0; t < 10; t++, dist += 0.02) { // (tucked in, but clear of the table's legs, foot or skirts)
            const [ox, oz] = rot(sx * dist, sz * dist, ry), sry = Math.atan2(-ox, -oz) + sesgo;
            const [x, z] = origen(silla, cx + ox, cz + oz, sry);
            it = { obj: silla, x, y: 0, z, ry: sry };
            if (hunde(it, mesaIt) <= 0.005) { suelta = true; break; }
          }
          if (!suelta) continue;
          const v = volumen(it);
          if (dentro(v, Z) && libre(v) && lejos(v) && !sillas.some((s) => choca(s.v, v))) sillas.push({ ...it, v });
        }
        if (sillas.length < Math.min(S.lados ? S.lados.length : 2, ns) || cierra([mesaIt, ...sillas])) continue;
        const it0 = poner(mesa, Z.id, 'conjunto', mx, 0, mz, ry);
        for (const s of sillas) { const c = poner(s.obj, Z.id, 'conjunto', s.x, 0, s.z, s.ry); c.de = P.indexOf(it0); }
        puestos++;
      }
    },
    // on the surfaces of what stands in the zone (the counter, the shelves, the tables)
    sobre(e, Z, vida = false) {
      const sops = P.map((p, i) => [p, i]).filter(([p]) => p.zona === Z.id && e.en.includes(p.obj));
      if (!sops.length) return;
      // every surface of each, as a rectangle in its own frame
      const sups = [];
      for (const [p, i] of sops) (OBJETOS[p.obj].superficies || []).forEach((s, k) => { const R = superficie(p.obj, k); if (R) sups.push({ p, i, k, ...R }); });
      const usar = e.fraccion ? sups.filter(() => r() < U(e.fraccion)) : sups;
      if (!usar.length && sups.length) usar.push(sups[Math.floor(r() * sups.length)]); // (a share of them, but one at least)
      const lenTot = sups.reduce((s, q) => s + (q.x1 - q.x0), 0);
      const total = e.relleno ? 9999 : e.por_soporte ? (Array.isArray(e.por_soporte) ? 9999 : usar.length * e.por_soporte) : tantos(e, lenTot, 0, usar.length);
      let puestos = 0, k = 0;
      const enSup = (q, obj) => {
        const b = caja(obj);
        for (let t = 0; t < (q.estante ? 1 : 30); t++) {
          let lx, lz;
          if (q.estante) { // (on a shelf: side by side from one end, the next free stretch)
            const ek = q.i + '#' + q.k;
            q.cur = q.cur ?? estantes[ek] ?? q.x0 + r() * 0.06;
            if (q.cur + b.w > q.x1 || b.d > q.z1 - q.z0 + 0.02) return false;
            lx = q.cur + b.w / 2 - (b.x0 + b.x1) / 2; lz = (q.z0 + q.z1) / 2 - (b.z0 + b.z1) / 2;
            q.cur += b.w + 0.015 + r() * 0.03;
            estantes[ek] = q.cur;
          } else {
            if (q.x1 - q.x0 < b.w || q.z1 - q.z0 < b.d) return false;
            lx = q.x0 + b.w / 2 + r() * (q.x1 - q.x0 - b.w) - (b.x0 + b.x1) / 2; lz = q.z0 + b.d / 2 + r() * (q.z1 - q.z0 - b.d) - (b.z0 + b.z1) / 2;
          }
          const lry = q.estante || OBJETOS[obj].clase === 'FIXED' ? 0 : (r() - 0.5) * 0.6;
          const [wx, wz] = rot(lx, lz, q.p.ry), ry = q.p.ry + lry;
          const it = { obj, x: q.p.x + wx, y: (q.p.y || 0) + q.y, z: q.p.z + wz, ry,e:entrada };
          const v = volumen(it);
          if (!P.some((p, j) => j !== q.i && p.v && choca(p.v, v)) && !(ctx?.funciones&&e.botin&&cierra([it]))) { const c = poner(obj, Z.id, vida ? 'vida' : 'sobre', it.x, it.y, it.z, ry, q.i, q.k); c.v = v; return true; }
        }
        return false;
      };
      if (e.relleno) { // (shelves full to so much of their length)
        for (const q of usar) {
          const lim = q.x0 + (q.x1 - q.x0) * U(e.relleno);
          const x1 = q.x1; q.x1 = lim;
          for (let t = 0, fallos = 0; t < 80 && fallos < 4; t++) { if (enSup(q, variante(e, k))) { fallos = 0; k++; } else { fallos++; k++; } } // (one that does not fit: the next kind)
          q.x1 = x1;
        }
        return;
      }
      if (e.por_soporte) {
        for (const q of usar) {
          const m = Array.isArray(e.por_soporte) ? N(e.por_soporte) : e.por_soporte, used = new Set();
          for (let j = 0; j < m; j++) {
            // (each a different thing; one that does not fit on what is left of the top: another, up to three)
            for (let intento = 0; intento < 3; intento++) {
              let obj = variante(e, k);
              for (let t = 0; t < 6 && used.has(obj); t++) obj = variante(e, k + t + 1);
              k++;
              if (enSup(q, obj)) { used.add(obj); puestos++; break; }
            }
          }
        }
        return;
      }
      for (let t = 0; puestos < total && t < total * 8; t++) { const q = usar[Math.floor(r() * usar.length)]; if (enSup(q, variante(e, k))) { puestos++; k++; } }
    },
    vida(e, Z) { this.sobre(e, Z, true); },
    techo(e, Z) {
      const lx = Z.x1 - Z.x0, lz = Z.z1 - Z.z0, n = e.cantidad ? N(e.cantidad) : e.por_m ? Math.max(1, Math.round(Math.max(lx, lz) * U(e.por_m))) : Math.max(1, Math.round(lx * lz * U(e.por_m2)));
      const cols = Math.max(1, Math.round(Math.sqrt((n * lx) / Math.max(lz, 0.1)))), rows = Math.max(1, Math.ceil(n / cols));
      let k = 0;
      // (on a grid over the zone; a slot taken by another hanging thing — a lamp, a ham —: a little along the zone)
      const largo = lx >= lz, colgados = P.filter((p) => p.regla === 'techo'), abajo = P.filter((p) => p.regla !== 'techo' && p.v);
      for (let i = 0; i < rows; i++) for (let j = 0; j < cols && k < n; j++, k++) {
        const x0 = Z.x0 + (lx * (j + 0.5)) / cols, z0 = Z.z0 + (lz * (i + 0.5)) / rows;
        const pasos = [0, 0.35, -0.35, 0.7, -0.7, 1.05, -1.05, 1.4, -1.4];
        for (const [d, t] of [...pasos.map((d) => [d, 0]), ...pasos.slice(1).map((d) => [0, d])]) {
          const obj = variante(e, k), x = Math.min(Z.x1 - 0.2, Math.max(Z.x0 + 0.2, x0 + (largo ? d : t))), z = Math.min(Z.z1 - 0.2, Math.max(Z.z0 + 0.2, z0 + (largo ? t : d))), it = { obj, x, y: H, z, ry: 0 }, v = volumen(it);
          if (colgados.some((p) => choca(grow(p.v, 0.05), v)) || abajo.some((p) => choca(p.v, v)) || (v.y0 < 1.2 && cierra([it]))) continue;
          colgados.push(poner(obj, Z.id, 'techo', x, H, z, 0)); break;
        }
      }
    },
  };
  // Grupos de módulos: probar el frente completo antes de comprometer su primera pieza.
  // La búsqueda no consume r ni modifica P/cursores si falla: conserva el fallback anterior.
  const aplicable = e => zonas[e.zona] && reglas[e.regla] && !(e.area_min != null && W*D < e.area_min) && !(e.area_max != null && W*D >= e.area_max) && !(ctx?.filtro && !ctx.filtro(e));
  const entradasActivas = [...K.objetos.entries()].filter(([,e]) => aplicable(e));
  const gruposIntentados = new Set(), entradasAgrupadas = new Set();
  const probarGrupoPared = (miembros, Z) => {
    const [raiz] = miembros, e0 = raiz[1];
    // Contrato deliberadamente pequeño: módulos fijos, obligatorios y unitarios.
    if(miembros.length<2 || miembros.length>4 || e0.regla!=='contra_pared')return false;
    if(miembros.some(([i,e],k)=>!e.obj || e.variantes || !e.obligatorio || !(e.cantidad===1 || (Array.isArray(e.cantidad)&&e.cantidad[0]===1&&e.cantidad[1]===1)) || e.silla_frontal || e.llenar || OBJETOS[e.obj]?.soporte!=='suelo' || (k>0 && (e.regla!=='junto_a' || e.mira_ref || (e.lados && (e.lados.length!==2 || !e.lados.includes('derecha') || !e.lados.includes('izquierda'))) || ![].concat(e.de).includes(miembros[k-1][1].obj)))))return false;
    // Sólo cadenas inmediatas: no convertir A<-B y A<-C en A-B-C.
    // Si falta esa referencia adyacente, se ejecutan las reglas originales (incluido si_no).
    let semilla=(seed*2654435761+97)>>>0;
    for(const ch of Z.id+'|'+e0.grupo_pared)semilla=Math.imul(semilla^ch.charCodeAt(0),16777619)>>>0;
    const azar=mulberry32(semilla);
    const lados=e0.pared==='*'?['N','S','E','W']:Array.isArray(e0.pared)?[...e0.pared]:[e0.pared];
    if(e0.pared==='*')for(let i=lados.length-1;i>0;i--){const j=Math.floor(azar()*(i+1));[lados[i],lados[j]]=[lados[j],lados[i]];}
    const anchoGrupo=miembros.reduce((a,[,e])=>a+caja(e.obj).w,0)+.04*(miembros.length-1);
    for(const lado of lados){
      if(!PARED[lado])continue;
      const pw=PARED[lado](Z),key=Z.id+lado,inicioGrupo=cursores[key]??pw.a+.03,fin=pw.b-.03-anchoGrupo;
      if(inicioGrupo>fin+TOL)continue;
      const slots=[];for(let s=inicioGrupo;s<=fin+1e-6;s+=.1)slots.push(s);
      if(!slots.length||fin-slots[slots.length-1]>.001)slots.push(fin);
      if(e0.centrado)slots.sort((a,b)=>Math.abs(a+anchoGrupo/2-(pw.a+pw.b)/2)-Math.abs(b+anchoGrupo/2-(pw.a+pw.b)/2));
      for(const s of slots)for(const orden of [miembros,[...miembros].reverse()]){
        let cursor=s;const nuevos=[];
        for(const [ei,e] of orden){
          const b=caja(e.obj),c=cursor+b.w/2,off=pw.fijo+(pw.eje==='z'?pw.n[0]:pw.n[1])*(b.d/2+.01);
          const [x,z]=origen(e.obj,pw.eje==='z'?off:c,pw.eje==='z'?c:off,pw.ry);
          const it={obj:e.obj,x,y:0,z,ry:pw.ry,e:ei,zona:Z.id},v=volumen(it);
          if(!dentro(v,Z)||!libre(v)||nuevos.some(q=>choca(volumen(q),v)))break;
          nuevos.push(it);cursor+=b.w+.04;
        }
        // También se comprueban usos frontales y accesos de las tres piezas juntas.
        if(nuevos.length!==miembros.length||cierra(nuevos))continue;
        const anterior=entrada;let previo=null;
        for(const [ei,e] of miembros){
          const it=nuevos.find(p=>p.e===ei);entrada=ei;
          const puesto=poner(it.obj,Z.id,ei===raiz[0]?'contra_pared':'junto_a',it.x,it.y,it.z,it.ry);
          if(previo)puesto.de=P.indexOf(previo);
          previo=puesto;entradasAgrupadas.add(ei);
        }
        entrada=anterior;cursores[key]=s+anchoGrupo+.03;return true;
      }
    }
    return false;
  };
  // (I-03: what stands loose on the floor a little off true — a few centimetres, a few degrees —; never what stands
  // against a wall, on something, or holds something; the table sets are askew of their own)
  const SUELTA = new Set(['fila', 'esquina', 'suelo_libre']);
  for (const [ei, e] of entradasActivas) {
    const Z = zonas[e.zona];
    activas.push(ei);
    entrada = ei;
    if(e.grupo_pared){
      const key=JSON.stringify([e.zona,e.grupo_pared]);
      if(!gruposIntentados.has(key)){
        gruposIntentados.add(key);
        const miembros=entradasActivas.filter(([,q])=>q.zona===e.zona&&q.grupo_pared===e.grupo_pared);
        // No adelantar el grupo por encima de otras entradas activas intercaladas.
        const pos=entradasActivas.findIndex(([i])=>i===ei);
        if(miembros.every(([i],k)=>entradasActivas[pos+k]?.[0]===i))probarGrupoPared(miembros,Z);
      }
      if(entradasAgrupadas.has(ei))continue;
    }
    const n0 = P.length;
    reglas[e.regla](e, Z);
    if (e.regla === 'modulos') { const a = alcanza(); for (const Z2 of Object.values(zonas)) if (Z2.publica && debe.includes(Z2.id) && !a.includes(Z2.id)) avisos.push(`la barra deja la zona pública «${Z2.id}» sin paso`); debe = a; }
    for (let i = n0; i < P.length; i++) {
      const p = P[i];
      if (!SUELTA.has(p.regla) || OBJETOS[p.obj].clase === 'FIXED' || P.some((q) => q.sop === i)) continue;
      const it = { obj: p.obj, x: p.x + (r() - 0.5) * 0.1, y: p.y, z: p.z + (r() - 0.5) * 0.1, ry: p.ry + ((r() - 0.5) * 16 * Math.PI) / 180 };
      const v = volumen(it);
      if (dentro(v, Z) && !P.some((q, j) => j !== i && q.v && choca(q.v, v)) && !libres.some((l) => choca(l, v, 0)) && !cierra([it], i)) Object.assign(p, it, { v });
    }
  }

  return { K, tipologia, seed, W, D, H, ev, U, puertaX, inicio, ancho, avisos, zonas, tabiques, libres, P, guardias, debe, activas };
}

// a business, built round its kit's layout. hogar (the validator, for the kits of a home's rooms): lay it out for that
// household only
export function buildLocal(kit, seed = 1, origin = INTERIOR_ORIGIN, title = null, hogar = null, contexto = null) {
  const { K, tipologia, W, D, H, ev, U, puertaX, ancho, avisos, zonas, tabiques, libres, P, guardias, debe, activas } = amueblar(kit, seed, contexto || hogar ? { ...contexto, ...(hogar ? { filtro: filtroHogar(hogar) } : {}) } : null);
  const t2 = MURO / 2;
  // ---- the room (its walls outside the frame: their faces at its edges)
  const B = new HouseBuilder(origin.x, origin.z, false);
  const mWall = B.mat('pared', () => std(new THREE.Color(K.pared || '#ece6da').getHex(), { roughness: 0.92 }));
  const mFloor = B.mat('suelo', () => texMat(K.suelo || 'floor_tiles_06', new THREE.Color(K.suelo_color || '#d8d0c4').getHex(), 0.5));
  const mCeil = B.mat('techo', () => std(0xf4f2ec, { roughness: 0.95 }));
  const mMetal = B.mat('metal', () => std(0x9aa0a4, { roughness: 0.35, metalness: 0.7 }));
  const mDoor = B.mat('puerta', () => texMat('dark_wood', 0xd8b890, 0.6));
  const mKnob = B.mat('pomo', () => std(0xc8b070, { roughness: 0.3, metalness: 0.8 }));
  B.add(mFloor, planeGeo(W, D, 1.4).rotateX(-Math.PI / 2), 0, 0.005, D / 2);
  B.add(mCeil, planeGeo(W, D, 2).rotateX(Math.PI / 2), 0, H, D / 2);
  const hw = W / 2, X0 = -hw - t2, d0 = hw + t2 + puertaX - 0.65, d1 = hw + t2 + puertaX + 0.65;
  const holes = [[d0, d1, 0, 2.35]];
  if (d0 - 0.4 > 0.9) holes.push([0.4 + t2, d0 - 0.35, 0.45, 2.6]);
  if (W + t2 - 0.4 - (d1 + 0.35) > 0.9) holes.push([d1 + 0.35, W + t2 - 0.4, 0.45, 2.6]);
  B.wall(mWall, X0, -t2, hw + t2, -t2, H, holes.sort((a, b) => a[0] - b[0]));
  const glass = glassMat();
  for (const [a, b, y0, y1] of holes) {
    const w = b - a, cx = X0 + (a + b) / 2;
    B.extraMesh(new THREE.Mesh(planeGeo(w, y1 - y0, 1), glass), cx, (y0 + y1) / 2, -t2, 0);
    B.add(mMetal, boxGeo(w, 0.06, 0.1, 1), cx, y1, -t2);
    B.view('f', cx - w / 2, y0, -t2 - 0.12, cx + w / 2, y1, -t2 + 0.12);
    B.segs.push([B.ox + cx - w / 2, B.oz - t2, B.ox + cx + w / 2, B.oz - t2, y1]);
  }
  B.interact({ type: 'exit', x: puertaX, z: 0.7, r: 1.1, label: 'Salir a la calle' });
  B.wall(mWall, X0, -t2, X0, D + t2, H); B.wall(mWall, hw + t2, -t2, hw + t2, D + t2, H); B.wall(mWall, X0, D + t2, hw + t2, D + t2, H);
  for (const t of tabiques) {
    const L = Math.hypot(t.bx - t.ax, t.bz - t.az);
    B.wall(mWall, t.ax, t.az, t.bx, t.bz, H, t.hueco ? [[t.hueco[0], t.hueco[1], 0, 2.1]] : []);
    if (t.hueco) { const ux = (t.bx - t.ax) / L, uz = (t.bz - t.az) / L; B.doorLeaf(mDoor, mKnob, t.ax + ux * t.hueco[0], t.az + uz * t.hueco[0], ux, uz, -1, 1.3, t.hueco[1] - t.hueco[0] - 0.04); }
  }
  // skirting along the back wall
  B.add(mWall, boxGeo(W, 0.1, 0.02, 1), 0, 0.05, D - 0.01);
  // the objects: geometry in world metres
  const items = P.map((p, i) => ({ obj: p.obj, x: B.ox + p.x, y: p.y || 0, z: B.oz + p.z, ry: p.ry, seed: seed + i, titulo: title }));
  B.extra.push(construir(items));
  // what you walk into: the footprints of what stands on the floor (not the little things)
  for (const p of P) {
    if (p.sop != null || p.regla === 'pared' || p.regla === 'techo') continue;
    const o = OBJETOS[p.obj], b = caja(p.obj);
    if (b.h < 0.3 || o.clase === 'PICKUP') continue;
    B.footprint(b.w, b.d, p.v.cx, p.v.cz, p.ry, Math.min(b.h, 2.2));
  }
  // its lights: a point light at a lamp of each zone in turn, as many as the kit allows, of the kit's colour
  const Tk = U(K.iluminacion.temperatura_k), col = kelvin(Tk), maxL = K.iluminacion.fuentes[1];
  const porZona = new Map();
  for (const p of P) if (p.regla === 'techo' && OBJETOS[p.obj].partes.some((q) => q.luz)) { if (!porZona.has(p.zona)) porZona.set(p.zona, []); porZona.get(p.zona).push(p); }
  const total = [...porZona.values()].reduce((s, l) => s + l.length, 0), lamps = [];
  for (let ronda = 0; lamps.length < Math.min(maxL, total); ronda++) for (const l of porZona.values()) if (l[ronda] && lamps.length < maxL) lamps.push(l[ronda]);
  const luces = [];
  for (const p of lamps) {
    const yl = Math.min(...OBJETOS[p.obj].partes.filter((q) => q.luz).map((q) => q.p[1]));
    B.light(p.x, H + yl - 0.15, p.z, col.getHex(), 5.5, 7.5);
    luces.push({ x: p.x, y: H + yl, z: p.z, k: Math.round(Tk), zona: p.zona });
  }
  // (the light fittings HouseBuilder.light adds — a shade each — are not wanted: the lamp is the catalogue's)
  B.extra = B.extra.filter((m) => !(m.userData && m.userData.lamp));
  B.spots.entrada = { x: B.ox + puertaX, z: B.oz + 0.9 };
  const dep = K.puntos && K.puntos.dependiente ? K.puntos.dependiente.map(ev) : [0, D * 0.6];
  B.spots.keeper = { x: B.ox + dep[0], z: B.oz + dep[1] };
  if (K.puntos && K.puntos.mostrador) { const [mx, mz] = K.puntos.mostrador.map(ev); B.interact({ type: 'counter', x: mx, z: mz, r: 1.3, label: K.pedir || 'Pedir en la barra' }); }
  // what is sold where it stands (vende: an item of src/items.js, or several): a buy point in front of the first few
  // pieces of that entry, as the hand-made shops have (src/shops.js optionAt)
  K.objetos.forEach((e, ei) => {
    // (or something to do there, the game's own: { "type": "train", "label": "Entrenar" } on a gym's machines)
    if (e.interaccion) P.filter((p) => p.e === ei).slice(0, 3).forEach((p) => { const b = caja(p.obj), [fx, fz] = rot(0, b.z1 + 0.45, p.ry); B.interact({ r: 0.9, ...e.interaccion, x: p.v.cx + fx, z: p.v.cz + fz }); });
    if (!e.vende) return;
    const vende = [].concat(e.vende);
    P.filter((p) => p.e === ei).slice(0, Math.max(3, vende.length)).forEach((p, k) => {
      const b = caja(p.obj), [fx, fz] = rot(0, b.z1 + 0.45, p.ry);
      B.interact({ type: 'buy', item: vende[k % vende.length], x: p.v.cx + fx, z: p.v.cz + fz, r: 0.9, y: p.y || 0 });
    });
  });
  // ---- the seats of the public zones (X: SEAT): sit down on any free one; in a bar or a café the barman takes the order
  // and brings it to the table or the counter in front (src/terrace.js Seats); the customers take some (below)
  const HOSTELERIA = ['bar', 'cafeteria', 'restaurante'].includes(K.tipologia);
  const asientos = [];
  P.forEach((p, i) => {
    const o = OBJETOS[p.obj];
    if (!o.asientos || !zonas[p.zona] || !zonas[p.zona].publica || p.sop != null) return;
    for (const a of o.asientos) {
      const [ax, az] = rot(a.p[0], a.p[2], p.ry), sx = p.x + ax, sz = p.z + az;
      // (what it faces: its set's table, or the counter or shelf right in front)
      let mesa = p.de != null ? P[p.de] : null;
      if (!mesa) { const [fx, fz] = rot(0, 0.55, p.ry); mesa = P.find((q) => q !== p && OBJETOS[q.obj].superficies && choca(q.v, { cx: sx + fx, cz: sz + fz, hw: 0.05, hd: 0.05, a: 0, y0: 0, y1: 3 }, 0)) || null; }
      const sup = mesa && OBJETOS[mesa.obj].superficies ? Math.max(...OBJETOS[mesa.obj].superficies.map((q) => q.y)) : null;
      const [fx, fz] = rot(0, 0.5, p.ry);
      const seat = { kind: 'local', x: B.ox + sx, z: B.oz + sz, y: (p.y || 0) + a.h - 0.46, h: p.ry, sirve: HOSTELERIA,
        tx: B.ox + (mesa ? (p.de != null ? mesa.v.cx : sx + fx) : sx + fx), tz: B.oz + (mesa ? (p.de != null ? mesa.v.cz : sz + fz) : sz + fz), mesaY: sup != null ? (mesa.y || 0) + sup : null };
      asientos.push(seat);
      B.interact({ type: 'asiento', x: sx, z: sz, r: 0.7, seat, label: sup != null && sup > 0.95 ? 'Sentarse en la barra' : mesa ? 'Sentarse a la mesa' : 'Sentarse' });
    }
  });
  const h = B.finish();
  h.pieces = { seat: [] }; // (the houses' own seats: none here, the room's are interactions)
  // ---- the customers (I-08): on the seats of the public zones, so many at each hour (a seat taken or not stays so for
  // the hour), each with a few of the kit's lines; src/venues.js VenueLife seats them when you come in
  const CL = K.ambiente && K.ambiente.clientela;
  if (CL && CL.maximo) {
    const frases = CL.frases || [];
    const ocup = (hora) => { const f = CL.horas.find(([a, b]) => hora >= a && hora < b); return f ? f[2] : 0; };
    h.cast = asientos.map((a, k) => {
      const dice = frases.length ? [0, 1, 2].map((j) => frases[Math.floor(hash1(seed * 977 + k * 31 + j) * frases.length)]) : null;
      return { id: 'cliente' + k, crowd: true, x: a.x - origin.x, z: a.z - origin.z, y: a.y, h: a.h, asiento: a, pose: hash1(seed * 53 + k) < 0.4 ? 'sitTalk' : 'sit', lines: dice,
        when: (hora) => hash1(seed * 131 + k * 17 + Math.floor(hora)) < ocup(hora) && rank(k, hora) < CL.maximo };
    });
    // (no more than the kit's maximum at once: the seats taken this hour, in a shuffled order)
    const rank = (k, hora) => { let n = 0; for (let j = 0; j < k; j++) if (hash1(seed * 131 + j * 17 + Math.floor(hora)) < ocup(hora)) n++; return n; };
  }
  // ---- what the validator reads (and the hash of the layout: I-03, the same seed, the same room)
  const colocados = P.map((p, i) => ({ i, e: p.e, obj: p.obj, zona: p.zona, regla: p.regla, x: +p.x.toFixed(3), y: +(p.y || 0).toFixed(3), z: +p.z.toFixed(3), ry: +p.ry.toFixed(4), sop: p.sop, sup: p.sup, de: p.de ?? null, clase: OBJETOS[p.obj].clase, v: p.v }));
  let hh = 2166136261;
  for (const c of colocados) for (const ch of `${c.obj}|${c.x}|${c.y}|${c.z}|${c.ry};`) { hh ^= ch.charCodeAt(0); hh = Math.imul(hh, 16777619) >>> 0; }
  h.local = { kit, tipologia, seed, W, D, H, puertaX, ancho, zonas, tabiques, libres, colocados, luces, avisos, guardias, debe, activas, hogar, hash: hh.toString(16), title };
  h.venue = false;
  // (what the game asks of any interior: where it stands, its extent, what it is; the street seen from its windows)
  h.origin = { x: origin.x, z: origin.z };
  h.bounds = { x0: origin.x - W / 2, x1: origin.x + W / 2, z0: origin.z, z1: origin.z + D };
  h.kind = 'local';
  // (a lit room looks the same by day and by night: a soft halo round the bulbs, not the street's night bloom, which
  // washes its pale walls out under nine lamps)
  h.bloom = { strength: 0.16, threshold: 0.95, radius: 0.55 };
  h.spots.floor = { local: { x: origin.x, z: origin.z + D / 2 } };
  return h;
}
