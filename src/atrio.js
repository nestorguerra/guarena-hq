// The atrium of Santa María: the raised forecourt along the church's south side (the Plaza de los Castillejos), as the
// user's captures show it (2026-10-13; docs/calles.md): a retaining wall rendered the colour of sand with a granite
// coping, a wrought-iron railing crossed with saltires between granite pillars, granite steps on its east side, a
// granite cross on a stepped pedestal, two-armed cast-iron lamps, two big pines, and inside it irregular granite
// paving. Its outline in the church's own frame (landmarks.js poi.churchFrame: x along the axis towards the apse, z
// across, south positive): from the south wall to the pavement of the Calle de la Cuesta, and from the Calle de Santa
// María to the steps — measured against the PNOA orthophoto and the streets of the map. In both looks: the hyperreal
// church (hiper.js) hides only the church's own group.
import * as THREE from 'three';
import { mergeGeometries } from 'three/addons/utils/BufferGeometryUtils.js';
import { doubleLamp } from './townplus.js';

// the outline (church frame, metres): the church's south wall and its chapel to the north, the Cuesta to the south
const NORTH = [[-19, 13.4], [9.6, 12.55], [10, 17.7], [20.5, 17.6]];
const SOUTH = [[-19, 34.2], [3, 35.4], [20.5, 33.2]];
const STEPS = [21.2, 25.4]; // (z: the opening in the east wall, with its flight down to the square)
const WALL_H = 0.7, RAIL_H = 0.95, WALL_T = 0.45;

function box(w, h, d, tile = 1.5) {
  const g = new THREE.BoxGeometry(w, h, d);
  const uv = g.attributes.uv, p = g.attributes.position, nm = g.attributes.normal;
  for (let i = 0; i < uv.count; i++) {
    const ax = Math.abs(nm.getX(i)), ay = Math.abs(nm.getY(i));
    const x = p.getX(i) + w / 2, y = p.getY(i) + h / 2, z = p.getZ(i) + d / 2;
    if (ax > 0.5) uv.setXY(i, z / tile, y / tile);
    else if (ay > 0.5) uv.setXY(i, x / tile, z / tile);
    else uv.setXY(i, x / tile, y / tile);
  }
  return g;
}
// a box placed along the segment a→b (church frame), its middle at height y, pushed sideways by `off`
function along(a, b, w, h, d, y, off = 0, tile) {
  const dx = b[0] - a[0], dz = b[1] - a[1], L = Math.hypot(dx, dz), g = box(w ?? L, h, d, tile);
  const ang = Math.atan2(-dz, dx), nx = -dz / L, nz = dx / L;
  g.applyMatrix4(new THREE.Matrix4().makeRotationY(ang));
  g.translate((a[0] + b[0]) / 2 + nx * off, y, (a[1] + b[1]) / 2 + nz * off);
  return g;
}
const merge = (list) => mergeGeometries(list.map((g) => (g.index ? g.toNonIndexed() : g)), false);

export function atrio(L) {
  const f = L.poi.churchFrame;
  if (!f) return;
  const g = new THREE.Group();
  g.position.copy(f.group.position); g.rotation.y = f.group.rotation.y;
  L.root.add(g); g.updateMatrixWorld(true);
  const toW = (x, z) => { const v = new THREE.Vector3(x, 0, z).applyMatrix4(g.matrixWorld); return [v.x, v.z]; };
  const M = L.mat;
  const arena = M.cal.clone(); arena.color.setRGB(0.78, 0.64, 0.46); // (the wall's render, the colour of sand)
  // ---- the walls: south along the Cuesta, west along the Calle de Santa María, east with its opening for the steps
  const E = SOUTH[SOUTH.length - 1][0];
  const runs = [];
  for (let i = 0; i < SOUTH.length - 1; i++) runs.push([SOUTH[i], SOUTH[i + 1]]);
  runs.push([NORTH[0], SOUTH[0]]);
  runs.push([[E, SOUTH[SOUTH.length - 1][1]], [E, STEPS[1]]], [[E, STEPS[0]], [E, NORTH[NORTH.length - 1][1]]]);
  const wall = [], cope = [], stone = [], iron = [];
  for (const [a, b] of runs) {
    const len = Math.hypot(b[0] - a[0], b[1] - a[1]);
    wall.push(along(a, b, len, WALL_H, WALL_T, WALL_H / 2, 0, 2));
    cope.push(along(a, b, len + 0.1, 0.09, WALL_T + 0.12, WALL_H + 0.045, 0, 1.2));
    // pillars of granite every 2.6 m, and between them the railing: two rails, bars a hand apart and a saltire
    const n = Math.max(1, Math.round(len / 2.6)), ux = (b[0] - a[0]) / len, uz = (b[1] - a[1]) / len;
    const y0 = WALL_H + 0.09;
    for (let k = 0; k <= n; k++) {
      const t = (k / n) * len, p = [a[0] + ux * t, a[1] + uz * t];
      stone.push(along([p[0] - ux * 0.2, p[1] - uz * 0.2], [p[0] + ux * 0.2, p[1] + uz * 0.2], 0.4, RAIL_H + 0.12, 0.4, y0 + (RAIL_H + 0.12) / 2, 0, 0.8));
      if (k === n) break;
      const q = [a[0] + ux * (t + len / n), a[1] + uz * (t + len / n)], pa = [p[0] + ux * 0.2, p[1] + uz * 0.2], qa = [q[0] - ux * 0.2, q[1] - uz * 0.2];
      const pl = Math.hypot(qa[0] - pa[0], qa[1] - pa[1]);
      iron.push(along(pa, qa, pl, 0.05, 0.05, y0 + 0.08), along(pa, qa, pl, 0.05, 0.05, y0 + RAIL_H - 0.04));
      for (let s = 0.07; s < pl - 0.03; s += 0.13) {
        const c = [pa[0] + ux * s, pa[1] + uz * s];
        iron.push(along([c[0] - ux * 0.01, c[1] - uz * 0.01], [c[0] + ux * 0.01, c[1] + uz * 0.01], 0.02, RAIL_H - 0.1, 0.02, y0 + RAIL_H / 2));
      }
      const diag = Math.hypot(pl, RAIL_H - 0.12), tilt = Math.atan2(RAIL_H - 0.12, pl);
      for (const sgn of [-1, 1]) {
        const d = box(diag, 0.035, 0.035);
        d.applyMatrix4(new THREE.Matrix4().makeRotationZ(sgn * tilt));
        d.applyMatrix4(new THREE.Matrix4().makeRotationY(Math.atan2(-uz, ux)));
        d.translate((pa[0] + qa[0]) / 2, y0 + RAIL_H / 2, (pa[1] + qa[1]) / 2);
        iron.push(d);
      }
    }
    // (you cannot walk through it: the wall and its railing stop you)
    const A = toW(a[0], a[1]), B = toW(b[0], b[1]);
    L.seg(A[0], A[1], B[0], B[1], WALL_H + RAIL_H);
  }
  // ---- the steps: a short flight of granite in the opening of the east wall, out to the square
  for (let s = 0; s < 3; s++) stone.push(along([E + 0.3 + s * 0.34, STEPS[0]], [E + 0.3 + s * 0.34, STEPS[1]], STEPS[1] - STEPS[0], 0.13 * (3 - s), 0.34, (0.13 * (3 - s)) / 2, 0, 1));
  // ---- the cross: a shaft and its arms of granite on a pedestal of three steps
  const cx = 12.5, cz = 25.5;
  for (let s = 0; s < 3; s++) { const w = 1.9 - s * 0.5; const st = box(w, 0.26, w, 0.8); st.translate(cx, 0.13 + s * 0.26, cz); stone.push(st); }
  const shaft = box(0.3, 3.1, 0.3, 0.8); shaft.translate(cx, 0.78 + 1.55, cz); stone.push(shaft);
  const arms = box(1.3, 0.3, 0.3, 0.8); arms.translate(cx, 0.78 + 2.45, cz); stone.push(arms);
  for (const [geo, mat] of [[merge(wall), arena], [merge(cope), M.sillar], [merge(stone), M.sillar], [merge(iron), M.iron]]) {
    const m = new THREE.Mesh(geo, mat); m.castShadow = true; m.receiveShadow = true; g.add(m);
  }
  const C = toW(cx, cz); L.circle(C[0], C[1], 0.95, 1.6);
  // ---- the lamps: cast iron with two arms, four metres and a half (the avenue's, smaller)
  const { iron: li, glow: lg } = doubleLamp(), glowMat = new THREE.MeshStandardMaterial({ color: 0xfff4d8, emissive: 0xffe8b0, emissiveIntensity: 1.2 });
  for (const [x, z] of [[-6, 31.5], [6.5, 31.8]]) {
    for (const [geo, mat] of [[li, M.iron], [lg, glowMat]]) { const m = new THREE.Mesh(geo, mat); m.position.set(x, 0, z); m.scale.setScalar(0.6); m.castShadow = mat === M.iron; g.add(m); }
    const P = toW(x, z); L.circle(P[0], P[1], 0.2, 4.5);
    const ux = Math.cos(g.rotation.y), uz = -Math.sin(g.rotation.y);
    for (const sx of [-1, 1]) L.world.lampPoints.push(P[0] + ux * sx * 0.93, 4.4, P[1] + uz * sx * 0.93);
  }
  // ---- its two big pines (one leaning), and its floor of granite slabs: a pedestrian area of the map (ground.js)
  const extra = L.world.extraTrees || (L.world.extraTrees = []);
  for (const [x, z, s] of [[-13, 25.5, 1.2], [-6.5, 29.5, 1.05]]) { const P = toW(x, z); extra.push({ kind: 'pino', x: P[0], z: P[1], s, pad: 0.3 }); }
  const ring = [];
  for (const [x, z] of NORTH.concat(SOUTH.slice().reverse())) ring.push(...toW(x, z));
  L.map.areas.push({ kind: 'highway:pedestrian', ring: new Float32Array(ring), holes: null, name: 'Atrio de Santa María', sport: '' });
  if (L.map.buildAreaIndex) L.map.buildAreaIndex();
  L.poi.atrio = { x: C[0], z: C[1] };
}
