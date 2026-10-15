// What the second round of the audit (2026-10-14) found the town lacking, drawn from numbers and words only: along the
// house fronts (calles_casas.js, and a street's own calles_estilos.js `cables`) the wiring stapled under the first floor's
// balconies, the shops' and bars' signs over their ground floor or on a bracket, the television aerials and dishes on
// the roofs and the letter boxes by the doors; and where the captures show them (calles_arreglos.js) the cooperatives'
// metal silos, the water towers, the wires strung across a street and the bars' terraces with their sunshades or awning.
import * as THREE from 'three';
import { mergeGeometries } from 'three/addons/utils/BufferGeometryUtils.js';
import { paint } from './props.js';
import { STYLES } from './calles.js';
import { SILOS, DEPOSITOS, TERRAZAS, CABLES, BANDERINES, POSTES, ESPEJOS, MASTILES, PLACAS_CALLE, CARTELES, ESCALONES, PLAZAS_AZULES, TAPAS, MARCAS, BANDAS, SEMAFOROS, BAJANTES, SIERRAS } from './calles_arreglos.js';
import { mulberry32 } from './util.js';
import { CASAS } from './calles_casas.js';
import { rotulo, registrar } from './rotulos.js';

const at = (g, x, y, z) => { g.translate(x, y, z); return g; };
// a geometry turned to face (fx, fz) — its +z towards it — and set at (x, y, z)
function place(g, x, y, z, fx, fz) {
  g.applyMatrix4(new THREE.Matrix4().makeRotationY(Math.atan2(fx, fz)));
  return at(g, x, y, z);
}
// a round rod from a to b (world), r thick, in its colour
const _up = new THREE.Vector3(0, 1, 0), _d = new THREE.Vector3(), _q = new THREE.Quaternion();
function rod(ax, ay, az, bx, by, bz, r, col) {
  _d.set(bx - ax, by - ay, bz - az);
  const L = _d.length() || 1e-3, g = paint(new THREE.CylinderGeometry(r, r, L, 5), col);
  _q.setFromUnitVectors(_up, _d.normalize());
  g.applyQuaternion(_q);
  return at(g, (ax + bx) / 2, (ay + by) / 2, (az + bz) / 2);
}
// a wire from a to b sagging `sag` m at its middle, in n pieces: pushed as line segments
function wire(out, ax, ay, az, bx, by, bz, sag, n = 8) {
  let px = ax, py = ay, pz = az;
  for (let k = 1; k <= n; k++) {
    const t = k / n, x = ax + (bx - ax) * t, z = az + (bz - az) * t, y = ay + (by - ay) * t - Math.sin(t * Math.PI) * sag;
    out.push(px, py, pz, x, y, z);
    px = x; py = y; pz = z;
  }
}

// the signs' lettering: one canvas, a cell each — the text in bold capitals on its colour, as large as it fits
function signAtlas(list) {
  const CW = 512, CH = 112, cols = 2, rows = Math.max(1, Math.ceil(list.length / cols));
  let H = 128;
  while (H < rows * CH) H *= 2;
  const c = document.createElement('canvas');
  c.width = CW * cols; c.height = H;
  const x = c.getContext('2d');
  const uv = [];
  list.forEach((s, i) => {
    const cx = (i % cols) * CW, cy = Math.floor(i / cols) * CH;
    x.fillStyle = s.fondo; x.fillRect(cx, cy, CW, CH);
    x.fillStyle = 'rgba(0,0,0,0.18)'; x.fillRect(cx, cy + CH - 6, CW, 6); // (its lower edge in shade)
    if (s.texto) {
      x.fillStyle = s.letra; x.textAlign = 'center'; x.textBaseline = 'middle';
      let fs = 76;
      do { x.font = `800 ${fs}px "Arial Narrow", Arial, Helvetica, sans-serif`; fs -= 4; } while (fs > 22 && x.measureText(s.texto).width > CW * 0.9);
      x.fillText(s.texto, cx + CW / 2, cy + CH / 2 + 3);
    }
    uv.push([cx / c.width, 1 - (cy + CH) / H, (cx + CW) / c.width, 1 - cy / H]);
  });
  const tex = new THREE.CanvasTexture(c);
  tex.colorSpace = THREE.SRGBColorSpace;
  tex.anisotropy = 4;
  return { tex, uv };
}

export function buildDetalles(world, map) {
  const solid = [], wires = [], signs = [], murals = [], decals = [], col = map.collider;
  const stats = { cables: 0, rotulos: 0, antenas: 0, buzones: 0, silos: 0, depositos: 0, terrazas: 0, cruces: 0 };
  // ---- along the house fronts
  const runsOf = new Map(), all = (world.facadeRuns || []).slice();
  // (a building with no house front of its own — a shed, a warehouse: buildings.js lays none — its walls from its
  // outline instead, each one that looks onto a street, at its part's height)
  const has = new Set(all.map((r) => r.bid));
  for (const k in CASAS) {
    const bid = +k, h = CASAS[k];
    if (has.has(bid) || !(h.rotulo || h.antenas || h.parabolica || h.buzones || h.cables)) continue;
    for (const p of world.buildingParts || []) {
      if (p.b !== bid) continue;
      const R = p.ring, n = R.length / 2;
      for (let i = 0; i < n; i++) {
        const j = (i + 1) % n, ax = R[i * 2], az = R[i * 2 + 1], bx = R[j * 2], bz = R[j * 2 + 1], L = Math.hypot(bx - ax, bz - az);
        if (L < 2) continue;
        const nx = (bz - az) / L, nz = -(bx - ax) / L, mx = (ax + bx) / 2 + nx * 3, mz = (az + bz) / 2 + nz * 3; // (outward, as buildings.js)
        if (map.buildingAt(mx, mz)) continue;
        // (a shed often stands back behind its yard: any wall with a street up to 18 m out in front of it; the nearest wins)
        const q = map.nearestEdge(mx, mz, 22, (e) => e.walk || e.drive);
        if (!q || q.d > 15 + q.edge.w / 2) continue;
        all.push({ ax, az, bx, bz, nx, nz, H: p.H, bid, calle: { ...h, street: null }, front: q.edge.name || '', sd: q.d });
      }
    }
  }
  for (const r of all) {
    const cs = r.calle;
    if (!cs || r.measured) continue;
    const L = Math.hypot(r.bx - r.ax, r.bz - r.az);
    if (L < 1.5) continue;
    if (!runsOf.has(r.bid)) runsOf.set(r.bid, []);
    runsOf.get(r.bid).push(r);
    // the wiring, a black cable stapled 5 cm off the wall under the first floor (or under the eaves of a low house), a hook
    // every three metres and a little sag between
    const S = cs.street && STYLES[cs.street];
    if ((cs.cables ?? (S && S.cables)) && r.H >= 2.8) {
      const y = Math.min(2.95, r.H - 0.3), o = 0.05, n = Math.max(1, Math.round(L / 3));
      for (let k = 0; k < n; k++) {
        const t0 = k / n, t1 = (k + 1) / n;
        wire(wires, r.ax + (r.bx - r.ax) * t0 + r.nx * o, y, r.az + (r.bz - r.az) * t0 + r.nz * o, r.ax + (r.bx - r.ax) * t1 + r.nx * o, y, r.az + (r.bz - r.az) * t1 + r.nz * o, 0.035, 4);
      }
      stats.cables++;
    }
  }
  const doors = world.facadeDoors || [];
  for (const [bid, runs] of runsOf) {
    const cs = runs[0].calle;
    if (!(cs.rotulo || cs.antenas || cs.parabolica || cs.buzones || cs.cierro || cs.celosia || cs.mural || cs.pergola || cs.canecillos)) continue;
    // its front: the one to the street the notes name, or its longest
    let main = null;
    for (const r of runs) {
      const L = Math.hypot(r.bx - r.ax, r.bz - r.az), on = !!cs.frente && r.front === cs.frente;
      // (a house: the longest wall to its street; a shed's walls from its outline: the one nearest a street, if long enough)
      const better = r.sd != null && main && main.r.sd != null ? (L >= 4 ? r.sd + 3 / L < main.r.sd + 3 / main.L : false) : L > (main ? main.L : 0);
      if (!main || (on && !main.on) || (on === main.on && better)) main = { r, L, on };
    }
    const r = main.r, L = main.L, tx = (r.bx - r.ax) / L, tz = (r.bz - r.az) / L, nx = r.nx, nz = r.nz;
    const P = (a, o) => [r.ax + tx * a + nx * o, r.az + tz * a + nz * o];
    // the shop's sign: a panel 6 cm proud over its ground floor, as wide as its words want; or on a bracket at its end
    if (cs.rotulo) {
      // (a brand's or a business's: its name for this copy of the game — src/rotulos.js)
      const ro = cs.rotulo.poi ? { ...cs.rotulo, texto: rotulo(cs.rotulo.poi) || cs.rotulo.texto } : cs.rotulo, k = signs.length;
      if (ro.donde === 'banderola') {
        const a = typeof ro.pos === 'number' ? Math.max(0.5, Math.min(L - 0.5, (1 - ro.pos) * L)) : Math.max(0.5, L - 0.9), [x, z] = P(a, 0.55), y0 = Math.min(2.7, r.H - 0.75); // (pos as on the front's sign; else at its left end)
        signs.push({ ...ro, k, quads: [[x, y0, z, tx, tz, 0.72, 0.52], [x, y0, z, -tx, -tz, 0.72, 0.52]] });
        registrar({ id: 'casa:' + bid, tipo: 'banderola', texto: ro.texto, poi: ro.poi || null, bid, x, y: y0 + 0.26, z, nx: tx, nz: tz, caras: 2, w: 0.72, h: 0.52 });
        solid.push(place(paint(new THREE.BoxGeometry(0.72, 0.52, 0.04), ro.fondo), x, y0 + 0.26, z, tx, tz));
        const [bx, bz] = P(a, 0.5); // (its iron bracket from the wall)
        solid.push(place(paint(new THREE.BoxGeometry(0.03, 0.03, 1.0), '#2a2a2a'), bx, y0 + 0.56, bz, nx, nz));
      } else {
        const w = Math.min(L * 0.85, Math.max(1.4, 0.3 * (ro.texto || '').length + 0.9), 6.5), h = 0.5;
        // (where along its front as seen: pos 0 its left end, 1 its right — from the street; the middle if not said)
        const pos = typeof ro.pos === 'number' ? Math.max(0, Math.min(1, ro.pos)) : 0.5, cxm = Math.max(w / 2 + 0.1, Math.min(L - w / 2 - 0.1, (1 - pos) * L));
        const y0 = r.H >= 4.6 ? 2.5 : Math.max(2.1, r.H - 0.75), [x, z] = P(cxm, 0.03);
        signs.push({ ...ro, k, quads: [[x, y0, z, nx, nz, w, h, true]] });
        registrar({ id: 'casa:' + bid, tipo: 'fachada', texto: ro.texto, poi: ro.poi || null, bid, x, y: y0 + h / 2, z, nx, nz, caras: 1, w, h });
        solid.push(place(paint(new THREE.BoxGeometry(w + 0.04, h + 0.04, 0.05), ro.fondo), x, y0 + h / 2, z, nx, nz));
      }
      stats.rotulos++;
    }
    // the television aerials on the roof, a mast with its two crossed rods, set back from the front; and the dish
    const roofY = r.H;
    for (let k = 0; k < (cs.antenas || 0); k++) {
      const [x, z] = P((L * (k + 1)) / ((cs.antenas || 0) + 1), -2.2);
      solid.push(at(paint(new THREE.CylinderGeometry(0.025, 0.03, 3.4, 5), '#55585b'), x, roofY + 1.5, z));
      for (const [y, len] of [[roofY + 2.95, 1.3], [roofY + 2.45, 0.9]]) {
        solid.push(place(paint(new THREE.BoxGeometry(0.03, 0.03, len), '#6a6d70'), x, y, z, tx, tz));
        for (let e = -2; e <= 2; e++) solid.push(place(paint(new THREE.BoxGeometry(0.42 - Math.abs(e) * 0.05, 0.015, 0.015), '#6a6d70'), x + tx * e * len * 0.2, y, z + tz * e * len * 0.2, tx, tz));
      }
      stats.antenas++;
    }
    if (cs.parabolica) { // (a dish on its arm by the top of the front, its hollow out to the sky over the street)
      const [x, z] = P(L * 0.8, 0.45), y = Math.max(2.6, r.H - 1.1), [ax, az] = P(L * 0.8, 0.2);
      const dish = paint(new THREE.SphereGeometry(0.45, 14, 8), '#e6e6e2');
      dish.scale(1, 1, 0.22); dish.rotateX(-0.45);
      solid.push(place(dish, x, y, z, nx, nz));
      solid.push(place(paint(new THREE.BoxGeometry(0.05, 0.05, 0.42), '#9a9c9e'), ax, y - 0.25, az, nx, nz));
    }
    // where along the front, from its left end as seen from the street (pos 0–1), and at what floor
    const along = (pos, w) => Math.max(w / 2 + 0.05, Math.min(L - w / 2 - 0.05, (1 - pos) * L)), FH = 3.0;
    // a glazed bay (cierro, mirador) standing out 0.55 m from the wall at its floor, dark frames, panes of glass
    if (cs.cierro) {
      const c = cs.cierro, w = c.ancho, h = c.alto, y0 = c.planta * FH + 0.75, [x, z] = P(along(c.pos, w), 0.28);
      solid.push(place(paint(new THREE.BoxGeometry(w, 0.1, 0.6), c.hex), x, y0 - 0.05, z, nx, nz), place(paint(new THREE.BoxGeometry(w + 0.05, 0.1, 0.62), c.hex), x, y0 + h + 0.05, z, nx, nz));
      const g = paint(new THREE.BoxGeometry(w - 0.06, h, 0.52), '#9fb4bf'); solid.push(place(g, x, y0 + h / 2, z, nx, nz));
      for (let k = 0; k <= Math.round(w / 0.5); k++) { const a = -w / 2 + (w * k) / Math.round(w / 0.5); solid.push(place(paint(new THREE.BoxGeometry(0.05, h, 0.05), c.hex), x + (nz) * a + nx * 0.27, y0 + h / 2, z - nx * a + nz * 0.27, nx, nz)); }
    }
    // a lattice of pierced blocks (or a reed screen) on its front: rows of little open squares
    if (cs.celosia) {
      const c = cs.celosia, w = c.ancho, h = c.alto, y0 = c.planta * FH + 0.4, [x, z] = P(along(c.pos, w), 0.05), cell = 0.2;
      for (let yy = 0; yy < h - 0.01; yy += cell) for (let xx = -w / 2; xx < w / 2 - 0.01; xx += cell) {
        const cx = x + nz * (xx + cell / 2), cz = z - nx * (xx + cell / 2), cy = y0 + yy + cell / 2;
        solid.push(place(paint(new THREE.BoxGeometry(cell, 0.04, 0.08), c.hex), cx, cy - cell / 2 + 0.02, cz, nx, nz), place(paint(new THREE.BoxGeometry(0.04, cell, 0.08), c.hex), cx - nz * (cell / 2 - 0.02), cy, cz + nx * (cell / 2 - 0.02), nx, nz));
      }
    }
    // a painted panel (a mural, a tiled picture): its colours in soft patches, 2 cm proud of the wall
    if (cs.mural) {
      const c = cs.mural, w = c.ancho, h = c.alto, [x, z] = P(along(c.pos, w), 0.03);
      murals.push({ x, y: c.y + c.planta * FH + h / 2, z, nx, nz, w, h, cols: c.colores, seed: bid });
    }
    // a metal pergola over part of its flat roof: four posts, its beams and slats
    if (cs.pergola) {
      const col2 = cs.pergola.hex, y = r.H + 0.1, hh = 2.3, w = Math.min(L * 0.5, 5), d = 3.0, [x, z] = P(L * 0.5, -d / 2 - 0.6);
      for (const a of [-1, 1]) for (const b of [-1, 1]) solid.push(at(paint(new THREE.BoxGeometry(0.08, hh, 0.08), col2), x + nz * a * w / 2 + nx * b * d / 2, y + hh / 2, z - nx * a * w / 2 + nz * b * d / 2));
      for (let k = 0; k <= 8; k++) { const a = -w / 2 + (w * k) / 8; solid.push(place(paint(new THREE.BoxGeometry(0.05, 0.08, d + 0.3), col2), x + nz * a, y + hh + 0.04, z - nx * a, nx, nz)); }
    }
    // wooden corbels under the eaves along its front, a hand apart (canecillos), in their colour
    if (cs.canecillos) {
      const col2 = typeof cs.canecillos === 'string' ? cs.canecillos : '#6b4a32';
      for (let a = 0.3; a < L - 0.2; a += 0.5) { const [x, z] = P(a, 0.17); solid.push(place(paint(new THREE.BoxGeometry(0.09, 0.12, 0.34), col2), x, r.H - 0.1, z, nx, nz)); }
    }
    // the letter boxes beside its door (or at the front's start), aluminium, two to three in a row
    if (cs.buzones) {
      let a = 0.45;
      const d = doors.find((q) => q.bid === bid && Math.abs((q.wx - r.ax) * nx + (q.wz - r.az) * nz) < 0.6);
      if (d) a = (d.wx - r.ax) * tx + (d.wz - r.az) * tz + 0.95;
      a = Math.min(Math.max(0.4, a), L - 0.4);
      const n = L > 6 ? 3 : 2;
      for (let k = 0; k < n; k++) {
        const [x, z] = P(a + (k - (n - 1) / 2) * 0.36, 0.07);
        solid.push(place(paint(new THREE.BoxGeometry(0.32, 0.36, 0.12), '#c9cbcc'), x, 1.35, z, nx, nz));
        solid.push(place(paint(new THREE.BoxGeometry(0.22, 0.02, 0.02), '#2a2c2e'), x + nx * 0.065, 1.45, z + nz * 0.065, nx, nz));
      }
      stats.buzones++;
    }
  }
  // ---- where the captures show them: the silos, in galvanised sheet on a cone, with a ladder up the side
  for (const [x, z, rad, h, c] of SILOS) {
    const body = h * 0.84;
    solid.push(at(paint(new THREE.CylinderGeometry(rad, rad, body, 24, 1, false), c), x, body / 2, z));
    solid.push(at(paint(new THREE.ConeGeometry(rad * 1.03, h - body, 24), c), x, body + (h - body) / 2, z));
    for (let y = 1.5; y < body - 0.5; y += 1.9) solid.push(at(paint(new THREE.CylinderGeometry(rad * 1.012, rad * 1.012, 0.08, 24, 1, true), '#8f9396'), x, y, z));
    solid.push(at(paint(new THREE.BoxGeometry(0.45, body, 0.05), '#6d7174'), x + rad + 0.08, body / 2, z));
    col.addCircle(x, z, rad, h, -11);
    stats.silos++;
  }
  // the water towers: a shaft of brick or concrete with a cylindrical tank on a cone at the top
  for (const [x, z, h, mat, c] of DEPOSITOS) {
    const tankH = Math.max(3, h * 0.22), shaft = h - tankH - 1.4, R = Math.min(5, 2 + h * 0.08), r0 = Math.max(1.3, R * 0.42);
    solid.push(at(paint(new THREE.CylinderGeometry(r0, r0 * 1.12, shaft, 18), c), x, shaft / 2, z));
    solid.push(at(paint(new THREE.CylinderGeometry(R, r0, 1.4, 18), c), x, shaft + 0.7, z));
    solid.push(at(paint(new THREE.CylinderGeometry(R, R, tankH, 22), mat === 'ladrillo' ? '#c9c2b4' : c), x, shaft + 1.4 + tankH / 2, z));
    solid.push(at(paint(new THREE.ConeGeometry(R * 1.04, 1.1, 22), '#8d8a84'), x, h + 0.55, z));
    col.addCircle(x, z, r0 * 1.12, h, -11);
    stats.depositos++;
  }
  // the wires across a street, from front to front, sagging half a metre
  for (const [x0, z0, x1, z1, h, h1] of CABLES) { wire(wires, x0, h, z0, x1, h1 ?? h, z1, 0.5, 12); stats.cruces++; }
  // the bars' terraces: their tables and chairs (streetlife.js's), under sunshades of their colour or one awning on posts
  const G = world.streetGeoms;
  if (G && world.facades) for (const [x, z, ux, uz, nx, nz, m, somb, toldo, onPave] of TERRAZAS) {
    const per = Math.min(m, 6), rows = Math.ceil(m / per), tint = (h) => { const c = new THREE.Color(h); return [c.r, c.g, c.b]; };
    let k = 0;
    for (let row = 0; row < rows; row++) for (let i = 0; i < per && k < m; i++, k++) {
      const a = (i - (per - 1) / 2) * 2.1, o = row * 1.7 * (onPave ? 1 : -1);
      const tx = x + ux * a + nx * o, tz = z + uz * a + nz * o;
      world.facades.addProp(G.mesaTerraza, tx, 0, tz, 0, 1, 1, null, false);
      col.addCircle(tx, tz, 0.42, 0.8, -4);
      for (let c = 0; c < 4; c++) { const q = (c / 4) * Math.PI * 2 + Math.PI / 4; world.facades.addProp(G.sillaTerraza, tx + Math.sin(q) * 0.62, 0, tz + Math.cos(q) * 0.62, q + Math.PI, 1, 1, null, false); }
      if (somb && !toldo) world.facades.addProp(G.sombrilla, tx, 0, tz, 0, 1, 1, tint(somb), false);
    }
    if (toldo) { // (one awning over them all, on four posts)
      const len = per * 2.1 + 0.6, dep = rows * 1.7 + 1.2, oc = ((rows - 1) * 1.7 * (onPave ? 1 : -1)) / 2;
      const cx = x + nx * oc, cz = z + nz * oc;
      solid.push(place(paint(new THREE.BoxGeometry(len, 0.06, dep), toldo), cx, 2.55, cz, nx, nz));
      for (const sa of [-1, 1]) for (const sb of [-1, 1]) {
        const px = cx + ux * sa * (len / 2 - 0.1) + nx * sb * (dep / 2 - 0.1), pz = cz + uz * sa * (len / 2 - 0.1) + nz * sb * (dep / 2 - 0.1);
        solid.push(at(paint(new THREE.CylinderGeometry(0.035, 0.035, 2.55, 6), '#3a3c3e'), px, 1.275, pz));
      }
    }
    stats.terrazas++;
  }
  // granite steps up from the kerb onto a square (one: its raised edge), the top one's riser painted if seen so
  for (const E of ESCALONES) {
    const Pp = E.pts, n = E.n, rise = E.alto / n;
    for (let i = 0; i + 7 < Pp.length; i += 4) {
      const a = [Pp[i], Pp[i + 1]], b = [Pp[i + 4], Pp[i + 5]], nx = Pp[i + 2], nz = Pp[i + 3], L2 = Math.hypot(b[0] - a[0], b[1] - a[1]);
      if (L2 < 0.05) continue;
      const mx = (a[0] + b[0]) / 2, mz = (a[1] + b[1]) / 2;
      for (let k = 0; k < n; k++) {
        const depth = 0.35 * (n - k) + 0.4, off = 0.35 * k + depth / 2, top = rise * (k + 1);
        // (its length along the street, its depth out from it: the box faces out, nx nz — a continuous band, not blocks)
        const g = paint(new THREE.BoxGeometry(L2 + 0.02, top, depth), k === n - 1 && E.borde ? '#c9c3b6' : '#b9b4aa');
        solid.push(place(g, mx + nx * off, top / 2, mz + nz * off, nx, nz));
        if (k === 0 && E.borde) solid.push(place(paint(new THREE.BoxGeometry(L2 + 0.02, top * 0.98, 0.012), E.borde), mx - nx * 0.007, top / 2, mz - nz * 0.007, nx, nz)); // (the first riser's face, painted)
      }
    }
    stats.escalones = (stats.escalones || 0) + 1;
  }
  // disabled parking bays painted blue in the lane by the kerb, with their white outline (paint on the road: its own
  // mesh, drawn over the road's surface, which the ground pulls forward)
  for (const [x, z, ux, uz, len] of PLAZAS_AZULES) {
    decals.push(place(paint(new THREE.BoxGeometry(2.3, 0.01, len), '#2f5fa8'), x, 0.045, z, ux, uz));
    for (const sgn of [-1, 1]) decals.push(place(paint(new THREE.BoxGeometry(0.1, 0.012, len), '#f2f2ee'), x - uz * sgn * 1.12, 0.047, z + ux * sgn * 1.12, ux, uz));
  }
  // covers, gratings and lids on the road or the pavement, little painted marks, bands across the carriageway
  const groundY = (pave) => (pave ? 0.175 : 0.047);
  for (const [x, z, ux, uz, f, t, c, pave] of TAPAS) {
    const y = groundY(pave);
    if (f === 'redonda') decals.push(at(paint(new THREE.CylinderGeometry(t / 2, t / 2, 0.012, 18), c), x, y, z));
    else decals.push(place(paint(new THREE.BoxGeometry(t, 0.012, f === 'rejilla' ? t * 0.45 : t), c), x, y, z, ux, uz));
    if (f === 'rejilla') for (let k = -3; k <= 3; k++) decals.push(place(paint(new THREE.BoxGeometry(0.025, 0.014, t * 0.4), '#151515'), x + uz * k * t * 0.13, y + 0.002, z - ux * k * t * 0.13, ux, uz));
  }
  for (const [x, z, ux, uz, L, W, c, pave] of MARCAS) decals.push(place(paint(new THREE.BoxGeometry(W, 0.012, L), c), x, groundY(pave), z, ux, uz));
  for (const [x, z, ux, uz, w, mod, d] of BANDAS) {
    if (mod === 'damero') { // (a chequer of red and white squares across the road)
      const n = Math.max(4, Math.round(w / 0.5));
      for (let i = 0; i < n; i++) for (let j = 0; j < 2; j++) {
        const a = -w / 2 + (w * (i + 0.5)) / n, b = (j - 0.5) * (d / 2);
        decals.push(place(paint(new THREE.BoxGeometry(w / n, 0.012, d / 2), (i + j) % 2 ? '#f2f2ee' : '#c8202a'), x - uz * a + ux * b, 0.047, z + ux * a + uz * b, ux, uz));
      }
    } else decals.push(place(paint(new THREE.BoxGeometry(w - 0.4, 0.012, d), mod === 'alerta' ? '#e8c43a' : '#f2f2ee'), x, 0.047, z, ux, uz));
  }
  // traffic lights: a grey post with its three-light head (or a mast arm out over the road), facing the traffic
  for (const [x, z, nx, nz, yaw, arm] of SEMAFOROS) {
    const fx = Math.sin(yaw), fz = Math.cos(yaw);
    solid.push(at(paint(new THREE.CylinderGeometry(0.06, 0.08, arm ? 6.2 : 3.4, 8), '#6f7477'), x, arm ? 3.1 : 1.7, z));
    const hx = arm ? x + nx * 3.5 : x, hz = arm ? z + nz * 3.5 : z, hy = arm ? 5.4 : 2.7;
    if (arm) solid.push(rod(x, 5.9, z, hx, 5.9, hz, 0.05, '#6f7477'));
    solid.push(place(paint(new THREE.BoxGeometry(0.32, 0.9, 0.28), '#1e2022'), hx, hy, hz, fx, fz));
    ['#c8202a', '#e8a320', '#2f9a4a'].forEach((c, k) => solid.push(place(paint(new THREE.CylinderGeometry(0.09, 0.09, 0.05, 12).rotateX(Math.PI / 2), c), hx + fx * 0.15, hy + 0.28 - k * 0.28, hz + fz * 0.15, fx, fz)));
    map.collider.addCircle(x, z, 0.1, 3.4, -5);
  }
  // a downpipe on a wall where its captures show one, its brackets every metre and a half
  for (const [x, z, h, c] of BAJANTES) {
    solid.push(at(paint(new THREE.CylinderGeometry(0.045, 0.045, h - 0.2, 8), c), x, (h - 0.2) / 2 + 0.1, z));
    for (let y = 1; y < h - 0.5; y += 1.5) solid.push(at(paint(new THREE.CylinderGeometry(0.06, 0.06, 0.04, 8), c), x, y, z));
  }
  // the strings of little flags across a street: a cord sagging 0.6 m, a pennant every 40 cm in turn of its colours
  for (const [x0, z0, x1, z1, h, cols] of BANDERINES) {
    wire(wires, x0, h, z0, x1, h, z1, 0.6, 16);
    const L = Math.hypot(x1 - x0, z1 - z0) || 1, dx = (x1 - x0) / L, dz = (z1 - z0) / L, n = Math.max(2, Math.floor(L / 0.4));
    for (let i = 1; i < n; i++) {
      const t = i / n, y = h - Math.sin(t * Math.PI) * 0.6, f = new THREE.ConeGeometry(0.13, 0.3, 3);
      f.rotateX(Math.PI); f.scale(1, 1, 0.1); // (a pennant hanging point down, flat)
      solid.push(place(paint(f, cols[i % cols.length]), x0 + (x1 - x0) * t, y - 0.17, z0 + (z1 - z0) * t, -dz, dx));
    }
    stats.banderines = (stats.banderines || 0) + 1;
  }
  // power poles: wood with its crossarm and insulators, a concrete one, or a lattice pylon with its arms
  for (const [x, z, mod, h] of POSTES) {
    if (mod === 'celosia') {
      const b = 1.6, t = 0.45, col = '#9aa0a3', corner = (k, y) => { const w = b + (t - b) * (y / h); return [x + (k & 1 ? w : -w), z + (k & 2 ? w : -w)]; };
      for (let k = 0; k < 4; k++) { const [ax, az] = corner(k, 0), [bx, bz] = corner(k, h); solid.push(rod(ax, 0, az, bx, h, bz, 0.06, col)); }
      for (let y = 0; y < h - 1; y += 2.2) {
        const y2 = Math.min(h, y + 2.2), ring = [0, 1, 3, 2, 0];
        for (let i = 0; i < 4; i++) {
          const [ax, az] = corner(ring[i], y), [bx, bz] = corner(ring[i + 1], y), [cx2, cz2] = corner(ring[i + 1], y2);
          solid.push(rod(ax, y, az, bx, y, bz, 0.03, col), rod(ax, y, az, cx2, y2, cz2, 0.025, col));
        }
      }
      for (const y of [h - 0.3, h - 3]) solid.push(rod(x - 3.2, y, z, x + 3.2, y, z, 0.07, col));
      map.collider.addCircle(x, z, 1.7, h, -11);
    } else {
      const wood = mod === 'madera', c = wood ? '#6b5038' : '#aaa69d';
      solid.push(at(paint(new THREE.CylinderGeometry(wood ? 0.11 : 0.09, wood ? 0.14 : 0.17, h, wood ? 8 : 4), c), x, h / 2, z));
      solid.push(at(paint(new THREE.BoxGeometry(1.5, 0.09, 0.09), wood ? '#5a4330' : '#8f8b84'), x, h - 0.5, z));
      for (const k of [-0.6, 0, 0.6]) solid.push(at(paint(new THREE.CylinderGeometry(0.05, 0.06, 0.18, 6), '#e6e6e0'), x + k, h - 0.36, z));
      map.collider.addCircle(x, z, 0.18, h, -5);
    }
    stats.postes = (stats.postes || 0) + 1;
  }
  // convex traffic mirrors on their grey post, an orange rim round the glass
  for (const [x, z, yaw] of ESPEJOS) {
    const fx = Math.sin(yaw), fz = Math.cos(yaw);
    solid.push(at(paint(new THREE.CylinderGeometry(0.045, 0.05, 2.9, 6), '#8f9396'), x, 1.45, z));
    const rim = paint(new THREE.CylinderGeometry(0.43, 0.43, 0.07, 22), '#e0662a'); rim.rotateX(Math.PI / 2);
    const glass = paint(new THREE.SphereGeometry(0.39, 18, 10), '#d8e4ea'); glass.scale(1, 1, 0.25);
    solid.push(place(rim, x, 2.75, z, fx, fz), place(glass, x + fx * 0.04, 2.75, z + fz * 0.04, fx, fz));
    map.collider.addCircle(x, z, 0.1, 2.9, -5);
  }
  // flagpoles: standing (white, a flag at the top of each) or slanting out from a wall over a balcony, side by side
  for (const [x, z, nx, nz, h, flags, wall] of MASTILES) {
    const tx = nz, tz = -nx;
    flags.forEach((c, i) => {
      const o = (i - (flags.length - 1) / 2) * (wall ? 0.9 : 1.6), bx = x + tx * o, bz = z + tz * o;
      if (wall) { // (from the wall at h, 40° up and out 1.5 m; the flag hangs from its end)
        const ex = bx + nx * 1.5, ey = h + 1.2, ez = bz + nz * 1.5;
        solid.push(rod(bx, h, bz, ex, ey, ez, 0.025, '#d8d8d4'));
        solid.push(place(paint(new THREE.BoxGeometry(0.02, 0.9, 1.25), c), (bx + ex) / 2 + nx * 0.1, (h + ey) / 2 - 0.4, (bz + ez) / 2 + nz * 0.1, tx, tz));
      } else {
        solid.push(at(paint(new THREE.CylinderGeometry(0.045, 0.06, h, 8), '#ecece8'), bx, h / 2, bz));
        solid.push(place(paint(new THREE.BoxGeometry(1.5, 1.0, 0.02), c), bx + nx * 0.8, h - 0.6, bz + nz * 0.8, tx, tz));
        map.collider.addCircle(bx, bz, 0.08, h, -5);
      }
    });
    stats.mastiles = (stats.mastiles || 0) + 1;
  }
  // street name plates on the wall, as seen: its words on its ground, 2.8 m up
  for (const [x, z, nx, nz, texto, fondo, letra] of PLACAS_CALLE) {
    const w = texto ? Math.min(1.7, Math.max(0.6, 0.075 * texto.length + 0.3)) : 0.7, h = 0.3, k = signs.length;
    signs.push({ texto: texto.toUpperCase(), fondo, letra, k, quads: [[x, 2.75, z, nx, nz, w, h, true]] });
    registrar({ id: `placa:${x.toFixed(1)},${z.toFixed(1)}`, tipo: 'placa', texto: texto.toUpperCase(), poi: null, x, y: 2.75 + h / 2, z, nx, nz, caras: 1, w, h });
    solid.push(place(paint(new THREE.BoxGeometry(w + 0.03, h + 0.03, 0.03), fondo), x, 2.75 + h / 2, z, nx, nz));
  }
  // billboards: a panel on two grey legs (on its foot at the ground if it stands low), its face as seen
  for (const [x, z, yaw, w, h, y0, colr, texto, letra] of CARTELES) {
    const fx = Math.sin(yaw), fz = Math.cos(yaw), tx = fz, tz = -fx;
    // (one against a wall hangs from it: no posts from the ground — they stood in front of a front like loose pipes)
    const onWall = !!(map.buildingAt(x - fx * 0.5, z - fz * 0.5) || map.buildingAt(x - fx * 1.2, z - fz * 1.2));
    if (y0 > 0.3 && !onWall) for (const sgn of [-1, 1]) { solid.push(at(paint(new THREE.CylinderGeometry(0.06, 0.07, y0 + h * 0.5, 6), '#8a8e90'), x + tx * sgn * w * 0.35 - fx * 0.12, (y0 + h * 0.5) / 2, z + tz * sgn * w * 0.35 - fz * 0.12)); map.collider.addCircle(x + tx * sgn * w * 0.35, z + tz * sgn * w * 0.35, 0.1, y0 + h, -5); }
    solid.push(place(paint(new THREE.BoxGeometry(w, h, 0.12), colr), x, y0 + h / 2, z, fx, fz));
    if (texto) {
      const k = signs.length; signs.push({ texto, fondo: colr, letra, k, quads: [[x + fx * 0.04, y0, z + fz * 0.04, fx, fz, w, h, true]] });
      registrar({ id: `cartel:${x.toFixed(1)},${z.toFixed(1)}`, tipo: 'cartel', texto, poi: null, x, y: y0 + h / 2, z, nx: fx, nz: fz, caras: 1, w, h });
    }
    stats.carteles = (stats.carteles || 0) + 1;
  }
  // ---- into the scene: the solid pieces one mesh (the street furniture's material), the wires lines, the signs lettered
  const root = new THREE.Group();
  if (solid.length) {
    const m = new THREE.Mesh(mergeGeometries(solid.map((g) => (g.index ? g.toNonIndexed() : g)), false), world.furnMat || new THREE.MeshStandardMaterial({ vertexColors: true, roughness: 0.7 }));
    m.castShadow = true; m.receiveShadow = true; m.matrixAutoUpdate = false;
    root.add(m);
  }
  if (wires.length) {
    const g = new THREE.BufferGeometry();
    g.setAttribute('position', new THREE.Float32BufferAttribute(wires, 3));
    root.add(new THREE.LineSegments(g, new THREE.LineBasicMaterial({ color: 0x1e1e1e, transparent: true, opacity: 0.85 })));
  }
  if (signs.length) {
    const { tex, uv } = signAtlas(signs);
    const pos = [], nor = [], uvs = [];
    for (const s of signs) {
      const [u0, v0, u1, v1] = uv[s.k];
      for (const [x, y0, z, fx, fz, w, h, flat] of s.quads) {
        const ax = fz, az = -fx; // (along the face, left to right as seen from in front)
        const lx = -ax, lz = -az, off = flat ? 0.031 : 0.021;
        const cx = x + fx * off, cz = z + fz * off;
        const A = [cx + lx * (w / 2), y0, cz + lz * (w / 2)], B = [cx - lx * (w / 2), y0, cz - lz * (w / 2)];
        pos.push(...A, ...B, B[0], y0 + h, B[2], ...A, B[0], y0 + h, B[2], A[0], y0 + h, A[2]);
        for (let q = 0; q < 6; q++) nor.push(fx, 0, fz);
        uvs.push(u0, v0, u1, v0, u1, v1, u0, v0, u1, v1, u0, v1);
      }
    }
    const g = new THREE.BufferGeometry();
    g.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
    g.setAttribute('normal', new THREE.Float32BufferAttribute(nor, 3));
    g.setAttribute('uv', new THREE.Float32BufferAttribute(uvs, 2));
    const m = new THREE.Mesh(g, new THREE.MeshStandardMaterial({ map: tex, roughness: 0.45, side: THREE.FrontSide, polygonOffset: true, polygonOffsetFactor: -2, polygonOffsetUnits: -4 }));
    m.receiveShadow = true; m.matrixAutoUpdate = false;
    root.add(m);
  }
  if (decals.length) {
    const m = new THREE.Mesh(mergeGeometries(decals.map((g) => (g.index ? g.toNonIndexed() : g)), false), new THREE.MeshStandardMaterial({ vertexColors: true, roughness: 0.8, polygonOffset: true, polygonOffsetFactor: -10, polygonOffsetUnits: -40 }));
    m.receiveShadow = true; m.matrixAutoUpdate = false; m.renderOrder = 2; root.add(m);
  }
  // hills on the horizon as their captures show them: a soft crest at the same apparent height, far off in the haze —
  // brought in to 3.8 km (the camera sees 4.2), drawn without fog, its colour the distance's
  for (const [cx, cz, a0, a1, D0, H0, v] of SIERRAS) {
    const D = Math.min(D0, 3800), Hc = (H0 * D) / D0, n = Math.max(8, Math.round((a1 - a0) * 60)), rr = mulberry32(v * 7919 + 3), pos = [], idx = [];
    let h = 0.7 + rr() * 0.3;
    for (let k = 0; k <= n; k++) {
      // (its two ends sloping down to the plain: seen from another street, a crest cut off square looked like a block)
      const az = a0 + ((a1 - a0) * k) / n, ex = cx + Math.sin(az) * D, ez = cz - Math.cos(az) * D, e = Math.min(1, Math.min(k, n - k) / (n * 0.22 + 1)), end = e * e * (3 - 2 * e);
      h = Math.max(0.35, Math.min(1, h + (rr() - 0.5) * 0.18));
      pos.push(ex, -20, ez, ex, Hc * h * end, ez);
      if (k) { const b = (k - 1) * 2; idx.push(b, b + 2, b + 1, b + 1, b + 2, b + 3); }
    }
    const g = new THREE.BufferGeometry(); g.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3)); g.setIndex(idx);
    const m = new THREE.Mesh(g, new THREE.MeshBasicMaterial({ color: 0x9fadbd, fog: false, side: THREE.DoubleSide }));
    m.frustumCulled = false; m.renderOrder = -1; root.add(m);
  }
  // the murals: each its own little canvas, soft patches of its colours over the first
  for (const m of murals) {
    const c = document.createElement('canvas'); c.width = 256; c.height = Math.max(64, Math.round(256 * m.h / m.w));
    const x = c.getContext('2d'), rr = mulberry32(m.seed * 977 + 13);
    x.fillStyle = m.cols[0]; x.fillRect(0, 0, c.width, c.height);
    for (let i = 0; i < 26; i++) {
      x.fillStyle = m.cols[1 + (i % Math.max(1, m.cols.length - 1))] || m.cols[0]; x.globalAlpha = 0.85;
      x.beginPath(); x.ellipse(rr() * c.width, rr() * c.height, 8 + rr() * 40, 8 + rr() * 30, rr() * 3, 0, Math.PI * 2); x.fill();
    }
    const tex = new THREE.CanvasTexture(c); tex.colorSpace = THREE.SRGBColorSpace;
    const mesh = new THREE.Mesh(new THREE.PlaneGeometry(m.w, m.h), new THREE.MeshStandardMaterial({ map: tex, roughness: 0.85, polygonOffset: true, polygonOffsetFactor: -2, polygonOffsetUnits: -4 }));
    mesh.position.set(m.x, m.y, m.z); mesh.rotation.y = Math.atan2(m.nx, m.nz); mesh.receiveShadow = true; root.add(mesh);
  }
  world.root.add(root);
  return stats;
}
