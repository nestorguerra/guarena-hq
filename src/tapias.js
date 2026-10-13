// The yard walls of the old town (tapias): where its streets' captures show a whitewashed wall between two houses —
// a corral, a vacant lot — and the map has nothing, only the gap. Along a street of the centre (calles.js tapias), on
// each side, the stretches where the kerbs found no front within reach (kerbs.js: fp, fm) between two houses, from
// 2.5 to 30 m long, are closed on the line of the fronts either side: a wall of lime, two and a half to three metres,
// a grey painted plinth, its coping, and its gate if it is long enough. Never where another street comes in, nor in a
// square or a park. They stop you, as walls do.
import * as THREE from 'three';
import { mergeGeometries } from 'three/addons/utils/BufferGeometryUtils.js';
import { polySample, pointInRing, hash1 } from './util.js';
import { STYLES as CALLES } from './calles.js';
import { TAPIAS } from './calles_tapias.js';

const MIN = 2.5, MAX = 30, T = 0.35;

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

export function buildTapias(world, map) {
  const M = world.landmarks && world.landmarks.mat;
  if (!M) return { n: 0 };
  const open = map.areas.filter((a) => /^(leisure:park|place:square|highway:pedestrian|amenity:marketplace|amenity:parking)$/.test(a.kind));
  const wall = [], plinth = [], cope = [], gates = [], segs = [], t = {}, t2 = {};
  let n = 0, metres = 0;
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
  for (const tp of TAPIAS) {
    const P = tp.pts, h = tp.h, key = tp.mat + '|' + tp.col;
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
      const base = kind === 'gate' ? M.wood : kind === 'piedra' ? M.mamp : kind === 'ladrillo' ? M.sillar : M.cal;
      m = base.clone();
      m.color.set(part === 'cope' && kind !== 'piedra' ? '#e9e5dc' : col);
      if (kind === 'piedra' || kind === 'ladrillo') m.color.multiplyScalar(1.25); // (their textures are darker than their colour)
      mats.set(k2, m);
    }
    mesh(list, m);
  }
  world.root.add(root);
  return { n, metres: Math.round(metres) };
}
