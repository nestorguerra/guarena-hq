// The yard walls of the old town (tapias): where its streets' captures show a whitewashed wall between two houses —
// a corral, a vacant lot — and the map has nothing, only the gap. Along a street of the centre (calles.js tapias), on
// each side, the stretches where the kerbs found no front within reach (kerbs.js: fp, fm) between two houses, from
// 2.5 to 30 m long, are closed on the line of the fronts either side: a wall of lime, two and a half to three metres,
// a grey painted plinth, its coping, and its gate if it is long enough. Never where another street comes in, nor in a
// square or a park. They stop you, as walls do.
import * as THREE from 'three';
import { mergeGeometries } from 'three/addons/utils/BufferGeometryUtils.js';
import { polySample, pointInRing, hash1, ringBounds } from './util.js';
import { STYLES as CALLES } from './calles.js';
import { TAPIAS as TAPIAS0 } from './calles_tapias.js';
import { TAPIAS as TAPIAS_ARREGLOS, SIN_TAPIAS } from './calles_arreglos.js';
const TAPIAS = TAPIAS0.concat(TAPIAS_ARREGLOS); // (and those the audit of 2026-10-13 found missing: tools/fachadas/arreglos.py)

const MIN = 2.5, MAX = 30, T = 0.35;
// a colour as a multiplier of another (both hex, compared in linear light): a hedge's green over the clipped hedge's own
const lin1 = (v) => { v /= 255; return v <= 0.04045 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; };
const linHex = (h) => [1, 3, 5].map((i) => lin1(parseInt(h.slice(i, i + 2), 16)));
function tint(hex, base) { const a = linHex(hex), b = linHex(base); return a.map((v, i) => Math.min(3, v / Math.max(1e-4, b[i]))); }

function box(w, h, d) {
  const g = new THREE.BoxGeometry(w, h, d);
  const uv = g.attributes.uv, p = g.attributes.position, nm = g.attributes.normal;
  for (let i = 0; i < uv.count; i++) {
    const ax = Math.abs(nm.getX(i)), ay = Math.abs(nm.getY(i));
    const x = p.getX(i) + w / 2, y = p.getY(i) + h / 2, z = p.getZ(i) + d / 2;
    uv.setXY(i, ax > 0.5 ? z / 1.5 : x / 1.5, ay > 0.5 ? z / 1.5 : y / 1.5);
  }
  return g;
}
// a box from a to b (world x-z), its street face on the line a→b and its body `d` behind it (towards nx, nz), y0..y1
function slab(a, b, nx, nz, d, y0, y1, out = 0) {
  const dx = b[0] - a[0], dz = b[1] - a[1], L = Math.hypot(dx, dz);
  const g = box(L + 0.02, y1 - y0, d);
  g.applyMatrix4(new THREE.Matrix4().makeRotationY(Math.atan2(-dz, dx)));
  g.translate((a[0] + b[0]) / 2 + nx * (d / 2 - out), (y0 + y1) / 2, (a[1] + b[1]) / 2 + nz * (d / 2 - out));
  return g;
}

// a fence along P ([x, z, nx, nz] a metre apart, n towards what it closes): 'verja' a low wall 0.6 m with iron bars a hand
// apart on it, 'murete' the low wall alone, 'malla' a wire fence on posts, 'celosia' lattice slats on a low wall — and a
// gate of the fence's colour half-way along when it is long enough; it stops you as a wall does
function fence(add, segs, P, h, kind, col, murete, gate) {
  const lowH = kind === 'malla' ? 0.15 : kind === 'murete' ? h : 0.6;
  const keyLow = 'cal|' + murete, keyTop = (kind === 'malla' ? 'malla|' : kind === 'celosia' ? 'celosia|' : 'hierro|') + col;
  for (let k = 0; k < P.length - 1; k++) {
    const p0 = P[k], p1 = P[k + 1], nx = p0[2], nz = p0[3];
    add(keyLow, slab(p0, p1, nx, nz, 0.25, 0, lowH));
    add(keyLow + '|cope', slab(p0, p1, nx, nz, 0.3, lowH, lowH + 0.05, 0.025));
    segs.push(p0[0], p0[1], p1[0], p1[1], h, -12);
    if (kind === 'murete') continue;
    const dx = p1[0] - p0[0], dz = p1[1] - p0[1], L = Math.hypot(dx, dz) || 1;
    if (kind === 'verja') {
      for (let s = 0.06; s < L; s += 0.12) { const a = [p0[0] + (dx / L) * s, p0[1] + (dz / L) * s]; add(keyTop, slab(a, [a[0] + (dx / L) * 0.02, a[1] + (dz / L) * 0.02], nx, nz, 0.02, lowH + 0.05, h, -0.115)); }
      add(keyTop, slab(p0, p1, nx, nz, 0.04, h - 0.04, h, -0.105));
      add(keyTop, slab(p0, p1, nx, nz, 0.03, lowH + 0.12, lowH + 0.15, -0.11));
    } else if (kind === 'celosia') {
      for (let y = lowH + 0.1; y < h; y += 0.14) add(keyTop, slab(p0, p1, nx, nz, 0.03, y, y + 0.08, -0.11));
    } else { // (malla: a post every metre, the mesh between)
      add(keyTop, slab(p0, [p0[0] + (dx / L) * 0.05, p0[1] + (dz / L) * 0.05], nx, nz, 0.05, 0, h, -0.1));
      add('mallaTela|' + col, slab(p0, p1, nx, nz, 0.01, lowH, h - 0.05, -0.12));
    }
  }
  if (gate && P.length > 6) {
    const g = Math.floor(P.length / 2) - 1, p0 = P[g], p1 = P[g + 1];
    add('gate|' + gate, slab(p0, p1, p0[2], p0[3], 0.05, 0, Math.min(2.1, h + 0.1), -0.08));
  }
}

export function buildTapias(world, map) {
  const M = world.landmarks && world.landmarks.mat;
  if (!M) return { n: 0 };
  const open = map.areas.filter((a) => /^(leisure:park|place:square|highway:pedestrian|amenity:marketplace|amenity:parking)$/.test(a.kind));
  const wall = [], plinth = [], cope = [], gates = [], segs = [], t = {}, t2 = {};
  let n = 0, metres = 0;
  const noWall = SIN_TAPIAS.map((r) => ({ r, bb: ringBounds(r) }));
  for (const e of map.edges) {
    const cs = CALLES[e.name], kb = e.kerb;
    if (!cs || !cs.tapias || !kb) continue;
    for (const side of [1, -1]) {
      const F = side > 0 ? kb.fp : kb.fm;
      for (let i = 1; i < kb.n - 1; ) {
        if (F[i] === F[i]) { i++; continue; }
        let j = i;
        while (j + 1 < kb.n && F[j + 1] !== F[j + 1]) j++;
        const a = i - 1, b = j + 1, len = (b - a) * kb.st;
        i = j + 1;
        if (b >= kb.n || F[a] !== F[a] || F[b] !== F[b] || len < MIN || len > MAX) continue;
        // (where another street comes in, or the gap is a square, a park, a car park: open, as it is)
        polySample(e.pts, e.cum, ((a + b) / 2) * kb.st, t);
        const nx = -t.dz * side, nz = t.dx * side, fm = (F[a] + F[b]) / 2;
        const px = t.x + nx * (fm + 2.5), pz = t.z + nz * (fm + 2.5);
        const q = map.nearestEdge(px, pz, 8, (o) => o !== e && (o.drive || o.walk) && !o.dirt);
        if (q && q.d < q.edge.w / 2 + 3) continue;
        if (open.some((ar) => pointInRing(px, pz, ar.ring))) continue;
        if (noWall.some((o) => { const qx = t.x + nx * fm, qz = t.z + nz * fm; return qx > o.bb[0] && qx < o.bb[2] && qz > o.bb[1] && qz < o.bb[3] && pointInRing(qx, qz, o.r); })) continue; // (none where the captures show the gap open: calles_arreglos.js SIN_TAPIAS)
        // the wall, metre by metre on the line of the fronts either side
        const H = 2.5 + hash1(e.id * 13 + a * 7 + side) * 0.6, pts = [];
        for (let k = a; k <= b; k++) {
          polySample(e.pts, e.cum, k * kb.st, t2);
          const f = F[a] + ((F[b] - F[a]) * (k - a)) / (b - a), wx = -t2.dz * side, wz = t2.dx * side;
          pts.push([t2.x + wx * (f + 0.02), t2.z + wz * (f + 0.02), wx, wz]);
        }
        for (let k = 0; k < pts.length - 1; k++) {
          const p0 = pts[k], p1 = pts[k + 1];
          wall.push(slab(p0, p1, p0[2], p0[3], T, 0.6, H));
          plinth.push(slab(p0, p1, p0[2], p0[3], T + 0.02, 0, 0.6, 0.01));
          cope.push(slab(p0, p1, p0[2], p0[3], T + 0.12, H, H + 0.1, 0.06));
          segs.push(p0[0], p0[1], p1[0], p1[1], H, -12);
        }
        // its gate, if it is long enough: a wooden one, two and a half metres wide, off the middle
        if (len >= 5) {
          const g = Math.max(1, Math.min(pts.length - 4, Math.floor(pts.length * (0.3 + hash1(e.id + a) * 0.4))));
          const p0 = pts[g], p1 = pts[g + 2] || pts[pts.length - 1];
          gates.push(slab(p0, p1, p0[2], p0[3], 0.06, 0, 2.3, 0.04));
        }
        n++; metres += len;
      }
    }
  }
  // ---- and the long ones the captures show where the map has no building at all (calles_tapias.js): lime, old ochre
  // render, stone, unrendered brick — each its colour and height, at the pavement's back
  const own = new Map(); // (material key → geometries)
  const add = (k, g) => { let a = own.get(k); if (!a) own.set(k, (a = [])); a.push(g); };
  const extra = world.extraTrees || (world.extraTrees = []);
  for (const tp of TAPIAS) {
    const P = tp.pts, h = tp.h, key = tp.mat + '|' + tp.col;
    if (tp.mat === 'verja' || tp.mat === 'malla' || tp.mat === 'celosia') {
      fence(add, segs, P, h, tp.mat, tp.col, tp.murete || '#efede6', tp.gate);
      n++; metres += P.length - 1;
      continue;
    }
    if (tp.mat === 'seto') {
      // a tall clipped hedge of Arizona cypress instead of a wall: the clipped hedge's pieces (trees.js 'seto', 2 × 0.8 m)
      // end to end along its line, half a metre behind it, as tall as it stands, in its dull olive green (vegetation.js
      // plants them); it stops you as a wall does
      const c = tint(tp.col, '#548453');
      // (and only where it can grow: a piece on a carriageway is not planted — vegetation.js, its road clear — and a
      // hedge measured from a camera the game has elsewhere fell on the Carretera de Don Benito's lanes, an invisible
      // wall across them: neither the piece nor its stop there)
      const grows = (x, z) => { const q = map.nearestEdge(x, z, 14); return !(q && q.d < q.edge.w / 2 + 0.2); };
      for (let k = 0; k < P.length - 1; k += 2) {
        const p0 = P[k], p1 = P[Math.min(P.length - 1, k + 2)], nx = p0[2], nz = p0[3];
        const dx = p1[0] - p0[0], dz = p1[1] - p0[1], L = Math.hypot(dx, dz) || 1;
        extra.push({ kind: 'seto', x: (p0[0] + p1[0]) / 2 + nx * 0.5, z: (p0[1] + p1[1]) / 2 + nz * 0.5, s: Math.max(0.6, L / 2) * 1.08, sy: h / 1.2, rot: Math.atan2(-dz / L, dx / L), tint: c, pad: 0.2, trunk: 0 });
      }
      for (let k = 0; k < P.length - 1; k++) {
        const ax = P[k][0] + P[k][2] * 0.5, az = P[k][1] + P[k][3] * 0.5, bx = P[k + 1][0] + P[k][2] * 0.5, bz = P[k + 1][1] + P[k][3] * 0.5;
        if (grows((ax + bx) / 2, (az + bz) / 2)) segs.push(ax, az, bx, bz, h, -12);
      }
      n++; metres += P.length - 1;
      continue;
    }
    for (let k = 0; k < P.length - 1; k++) {
      const p0 = P[k], p1 = P[k + 1], nx = p0[2], nz = p0[3];
      add(key, slab(p0, p1, nx, nz, T + 0.05, 0, h));
      add(key + '|cope', slab(p0, p1, nx, nz, T + 0.15, h, h + 0.1, 0.05));
      segs.push(p0[0], p0[1], p1[0], p1[1], h, -12);
    }
    if (tp.gate && P.length > 4) {
      const g = Math.floor(P.length / 2) - 1, p0 = P[g], p1 = P[g + 1];
      add('gate|' + tp.gate, slab(p0, p1, p0[2], p0[3], 0.06, 0, Math.min(2.3, h - 0.2), 0.04));
    }
    n++; metres += P.length - 1;
  }
  // ---- the front fences of the houses that stand back from their pavement, as their captures show them (calles.js
  // cerramiento: a railing on a low wall, a low wall alone, a wire fence, lattice), on the line where the pavement ends,
  // as long as the front it closes; the ground behind it a garden's earth
  const gardens = world.extraGround || (world.extraGround = []);
  for (const r of world.facadeRuns || []) {
    const cz = r.calle && r.calle.cerramiento;
    if (!cz) continue;
    const mx = (r.ax + r.bx) / 2, mz = (r.az + r.bz) / 2;
    const q = map.nearestEdge(mx + r.nx * 4, mz + r.nz * 4, 30, (o) => o.drive && !o.dirt);
    if (!q) continue;
    const e = q.edge, sp = polySample(e.pts, e.cum, q.s, t), side = (mx - sp.x) * -sp.dz + (mz - sp.z) * sp.dx >= 0 ? 1 : -1;
    const kerb = map.kerbAt ? map.kerbAt(e, q.s, side) : e.w / 2, sw = (side > 0 ? e.swP : e.swM) ?? e.sw ?? 1.2;
    const line = kerb + 0.15 + Math.max(0.9, sw), front = Math.abs((mx - sp.x) * -sp.dz + (mz - sp.z) * sp.dx);
    // (its garden as deep as seen — cerramiento.fondo — even where the map's pavement reaches its front: the fence then
    // stands on the pavement, never nearer the kerb than 0.6 m)
    const deep = cz.fondo && (!r.calle.frente || !r.front || r.front === r.calle.frente) ? Math.min(cz.fondo, front - kerb - 0.6) : 0; // (on its front to its own street)
    if (deep < 0.4 && front - line < 1.0) continue; // (it stands at the pavement: no fence)
    // the run's two ends brought forward onto the fence line, along the house's own normal
    const back = deep >= 0.4 ? deep : front - line, A = [r.ax + r.nx * back, r.az + r.nz * back], Bp = [r.bx + r.nx * back, r.bz + r.nz * back];
    const L = Math.hypot(Bp[0] - A[0], Bp[1] - A[1]), nseg = Math.max(1, Math.round(L)), Q = [];
    for (let k = 0; k <= nseg; k++) Q.push([A[0] + ((Bp[0] - A[0]) * k) / nseg, A[1] + ((Bp[1] - A[1]) * k) / nseg, -r.nx, -r.nz]);
    fence(add, segs, Q, cz.h || 1.5, cz.tipo === 'murete' ? 'murete' : cz.tipo, cz.col || '#1e1e1e', cz.murete || '#efede6', cz.col);
    gardens.push({ ring: [A[0], A[1], Bp[0], Bp[1], r.bx, r.bz, r.ax, r.az], mat: 'tierra', col: null });
    n++; metres += L;
  }
  if (!n) return { n: 0 };
  map.collider.appendSegments(segs); // (the wall grid again, with them: it was built)
  const lime = M.cal, grey = M.cal.clone(), wood = M.wood;
  grey.color.setRGB(0.62, 0.62, 0.6);
  const root = new THREE.Group();
  const mesh = (list, mat) => {
    if (!list.length) return;
    const m = new THREE.Mesh(mergeGeometries(list.map((g) => g.toNonIndexed()), false), mat);
    m.castShadow = true; m.receiveShadow = true; m.matrixAutoUpdate = false;
    root.add(m);
  };
  for (const [list, mat] of [[wall, lime], [plinth, grey], [cope, lime], [gates, wood]]) mesh(list, mat);
  const mats = new Map();
  for (const [key, list] of own) {
    const [kind, col, part] = key.split('|');
    // (lime and render: the lime's own material in that colour; stone the rubble's, brick the coursed blocks'; a gate wood)
    const k2 = key;
    let m = mats.get(k2);
    if (!m) {
      const base = kind === 'gate' ? M.wood : kind === 'piedra' ? M.mamp : kind === 'ladrillo' ? M.sillar : kind === 'hierro' || kind === 'malla' ? M.iron : kind === 'celosia' ? M.wood : M.cal;
      m = base.clone();
      if (kind === 'mallaTela') { m = M.iron.clone(); m.transparent = true; m.opacity = 0.32; m.depthWrite = false; } // (wire mesh: seen through)
      m.color.set(part === 'cope' && kind !== 'piedra' ? '#e9e5dc' : col);
      if (kind === 'piedra' || kind === 'ladrillo') m.color.multiplyScalar(1.25); // (their textures are darker than their colour)
      mats.set(k2, m);
    }
    mesh(list, m);
  }
  world.root.add(root);
  return { n, metres: Math.round(metres) };
}
