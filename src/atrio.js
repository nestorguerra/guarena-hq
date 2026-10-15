// The atrium of Santa María: the forecourt along the church's south side (the Plaza de los Castillejos), as the user's
// captures show it (2026-10-13/14; docs/calles.md): enclosed by a retaining wall — rendered the colour of sand along the
// Cuesta and the Castillejos, granite along the Calle de Santa María — with a granite coping, an iron railing of
// saltires between granite pillars, a flight of granite steps at its east end, a tall granite cross on its stepped base,
// two cast-iron lamps with two lanterns, one big tree at the north-west corner, a stone bench, and inside it irregular
// slabs of granite. Its outline in the church's own frame (landmarks.js poi.churchFrame: x along the axis towards the
// apse, z across, south positive): the church's south wall and the sacristy to the north, the walls at x = −23.8
// (Calle de Santa María), along the Cuesta (z 34 at the west, 29.5 from x = 6 to the east) and x = 23.3 (Castillejos).
// 2026-10-14: measured again on the captures (views 8, 11, 35, 38, 10) and the PNOA — the south wall stands 4–5 m
// further north than it was drawn (the pavement beside the Cuesta was taken for the atrium), the west wall 5 m further
// west, and the street stands below the atrium (the walls here are 1–1.6 m: the game's ground is one level, so its floor
// stays at the street's and the wall rises from it). In both looks: the hyperreal church (hiper.js) hides only the church's own group.
import * as THREE from 'three';
import { mergeGeometries } from 'three/addons/utils/BufferGeometryUtils.js';
import { mulberry32 } from './util.js';

// the walls' middle lines (church frame, metres): a wall is { pts, h (its height above the street), granite }
const WEST = [[-23.8, 13.6], [-23.8, 34.2]];
const SOUTH = [[-23.8, 34.2], [-10, 32.95], [-4.5, 32.7], [6, 32.4], [23.3, 32.2]];
const EAST = [[23.3, 32.2], [23.3, 26.9]];
const EAST2 = [[23.3, 22.5], [23.3, 17.7]];
const NORTH = [[-23.8, 13.6], [9.6, 12.55], [10, 17.7], [23.3, 17.7]]; // (the church's south wall, its sacristy: the floor's north edge)
const STEPS = [22.5, 26.9];                                              // (z: the opening in the east wall, with its flight down to the square)
const RAIL_H = 0.95, WALL_T = 0.5;
const CROSS = [-13.7, 23.6];
const TREE = [-20.3, 16.2];

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
const merge = (list) => mergeGeometries(list.map((g) => (g.index ? g.toNonIndexed() : g)).map((g) => { for (const k of Object.keys(g.attributes)) if (!['position', 'normal', 'uv'].includes(k)) g.deleteAttribute(k); return g; }), false);
// a material cloned from another, its clay-look defines kept (a clone starts again from the standard ones)
function variant(m, r, g, b) { const c = m.clone(); c.defines = Object.assign({}, m.defines); if (r !== undefined) c.color.setRGB(r, g, b); return c; }

// the floor: slabs of granite laid in loose courses, irregular, grey with a little ochre, the joints dark (view 38: «enlosado de lanchas»)
function flagTexture() {
  const S = 512, c = document.createElement('canvas'); c.width = c.height = S;
  const x = c.getContext('2d'), r = mulberry32(2026);
  x.fillStyle = '#6a6355'; x.fillRect(0, 0, S, S);
  const rows = 5, rh = S / rows;
  for (let i = 0; i < rows; i++) {
    let px = -r() * rh;
    const y0 = i * rh;
    while (px < S) {
      const w = rh * (0.7 + r() * 0.9), j = () => (r() - 0.5) * rh * 0.12;
      const k = r(), v = 0.9 + r() * 0.2, base = k < 0.55 ? [150, 143, 130] : k < 0.85 ? [160, 145, 120] : [124, 119, 110];
      for (const ox of [0, -S, S]) {
        const x0 = px + ox;
        if (x0 > S || x0 + w < 0) continue;
        x.fillStyle = `rgb(${base.map((q) => Math.round(q * v)).join(',')})`;
        x.beginPath();
        x.moveTo(x0 + 3 + j(), y0 + 3 + j()); x.lineTo(x0 + w - 3 + j(), y0 + 3 + j()); x.lineTo(x0 + w - 3 + j(), y0 + rh - 3 + j()); x.lineTo(x0 + 3 + j(), y0 + rh - 3 + j());
        x.closePath(); x.fill();
        x.fillStyle = 'rgba(255,255,255,0.07)'; x.fillRect(x0 + 5, y0 + 5, w - 10, 3);
        for (let q = 0; q < 14; q++) { x.fillStyle = r() < 0.5 ? 'rgba(70,64,54,0.14)' : 'rgba(235,228,214,0.16)'; x.fillRect(x0 + r() * w, y0 + r() * rh, 1 + r() * 3, 1 + r() * 2); }
      }
      px += w;
    }
  }
  const t = new THREE.CanvasTexture(c); t.wrapS = t.wrapT = THREE.RepeatWrapping; t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8;
  return t;
}

// a cast-iron lamp with two lanterns, as in the captures (grey, slender, scrolled arms): its iron, and its glass
function fernandina() {
  const iron = [], glow = [];
  const cyl = (rt, rb, h, seg, y) => new THREE.CylinderGeometry(rt, rb, h, seg).translate(0, y, 0);
  iron.push(cyl(0.2, 0.3, 0.9, 12, 0.45), cyl(0.27, 0.27, 0.1, 12, 0.95), cyl(0.12, 0.16, 0.2, 12, 1.08), cyl(0.05, 0.075, 2.8, 10, 2.55), cyl(0.12, 0.12, 0.08, 10, 3.9));
  for (const s of [-1, 1]) {
    const curve = new THREE.CatmullRomCurve3([new THREE.Vector3(0, 3.85, 0), new THREE.Vector3(s * 0.3, 3.82, 0), new THREE.Vector3(s * 0.62, 3.95, 0), new THREE.Vector3(s * 0.85, 4.15, 0)]);
    iron.push(new THREE.TubeGeometry(curve, 12, 0.022, 5));
    const scroll = new THREE.TorusGeometry(0.12, 0.016, 5, 12, Math.PI * 1.5); scroll.rotateZ(s > 0 ? Math.PI : -Math.PI * 0.5); scroll.translate(s * 0.4, 3.72, 0); iron.push(scroll);
    iron.push(cyl(0.2, 0.1, 0.1, 6, 4.17).translate(s * 0.85, 0, 0), new THREE.ConeGeometry(0.24, 0.2, 6).translate(s * 0.85, 4.68, 0), new THREE.SphereGeometry(0.05, 6, 5).translate(s * 0.85, 4.84, 0));
    glow.push(cyl(0.19, 0.14, 0.42, 6, 4.43).translate(s * 0.85, 0, 0));
  }
  iron.push(new THREE.SphereGeometry(0.07, 8, 6).translate(0, 4.0, 0));
  return { iron: merge(iron), glow: merge(glow) };
}

export function atrio(L) {
  const f = L.poi.churchFrame;
  if (!f) return;
  const g = new THREE.Group();
  g.position.copy(f.group.position); g.rotation.y = f.group.rotation.y;
  L.root.add(g); g.updateMatrixWorld(true);
  const toW = (x, z) => { const v = new THREE.Vector3(x, 0, z).applyMatrix4(g.matrixWorld); return [v.x, v.z]; };
  const M = L.mat;
  const arena = variant(M.cal, 0.5, 0.37, 0.26); // (the wall's render, the colour of sand: ≈ 200,170,140 as sRGB)
  const granite = variant(M.sillar, 0.86, 0.82, 0.76), iron = variant(M.iron, 0.1, 0.075, 0.06); // (the railing: rusted dark iron)
  iron.roughness = 0.75; iron.metalness = 0.25;
  // ---- the floor: the paving of the atrium, in a mesh of its own over the ground (its pale area, below), irregular granite slabs
  const ring = NORTH.concat(SOUTH.slice().reverse());
  {
    const sh = new THREE.Shape(ring.map(([x, z]) => new THREE.Vector2(x, -z)));
    const fg = new THREE.ShapeGeometry(sh); fg.rotateX(-Math.PI / 2);
    const u = fg.attributes.uv, p = fg.attributes.position; for (let i = 0; i < u.count; i++) u.setXY(i, p.getX(i) / 4, p.getZ(i) / 4);
    const fm = new THREE.MeshStandardMaterial({ map: flagTexture(), roughness: 0.95, polygonOffset: true, polygonOffsetFactor: -3, polygonOffsetUnits: -6 });
    if (M.mamp && M.mamp.defines) fm.defines = Object.assign({}, M.mamp.defines, { CLAY_TILE: '1.6', CLAY_SET: '1' });
    const fl = new THREE.Mesh(fg, fm); fl.position.y = 0.012; fl.receiveShadow = true; g.add(fl);
  }
  // ---- the walls: west (granite), south along the Cuesta, east with its opening for the steps (rendered): each a wall with its
  // coping, granite pillars every four bays and between them the railing of saltires
  const wall = [], cope = [], stone = [], bars = [], wallG = [];
  const runs = [[WEST, 1.0, true], [SOUTH.slice(0, 2), 1.1, false], [SOUTH.slice(1, 3), 1.35, false], [SOUTH.slice(2, 4), 1.55, false], [SOUTH.slice(3), 1.6, false], [EAST, 1.35, false], [EAST2, 1.35, false]];
  for (const [pts, wh, gran] of runs) for (let i = 0; i < pts.length - 1; i++) {
    const a = pts[i], b = pts[i + 1], len = Math.hypot(b[0] - a[0], b[1] - a[1]);
    (gran ? wallG : wall).push(along(a, b, len, wh, WALL_T, wh / 2, 0, 2));
    cope.push(along(a, b, len + 0.1, 0.1, WALL_T + 0.16, wh + 0.05, 0, 1.2));
    const y0 = wh + 0.1, n = Math.max(1, Math.round(len / 4.8)), ux = (b[0] - a[0]) / len, uz = (b[1] - a[1]) / len, yaw = Math.atan2(-uz, ux);
    const nb = Math.max(1, Math.round(len / n / 1.2));
    for (let k = 0; k <= n; k++) {
      const t = (k / n) * len, p = [a[0] + ux * t, a[1] + uz * t];
      // (a pillar: a shaft and its capstone)
      stone.push(box(0.42, RAIL_H + 0.3, 0.42, 0.8).translate(p[0], y0 + (RAIL_H + 0.3) / 2, p[1]), box(0.54, 0.1, 0.54, 0.8).translate(p[0], y0 + RAIL_H + 0.35, p[1]));
      if (k === n) break;
      const seg = len / n, pa = [p[0] + ux * 0.21, p[1] + uz * 0.21], qa = [p[0] + ux * (seg - 0.21), p[1] + uz * (seg - 0.21)], pl = Math.hypot(qa[0] - pa[0], qa[1] - pa[1]);
      bars.push(along(pa, qa, pl, 0.04, 0.04, y0 + 0.1), along(pa, qa, pl, 0.04, 0.04, y0 + RAIL_H - 0.04), along(pa, qa, pl, 0.03, 0.03, y0 + RAIL_H - 0.16));
      const bl = pl / nb, th = RAIL_H - 0.16, diag = Math.hypot(bl, th), tilt = Math.atan2(th, bl);
      for (let j = 0; j <= nb; j++) { const c = [pa[0] + ux * j * bl, pa[1] + uz * j * bl]; bars.push(along([c[0] - ux * 0.01, c[1] - uz * 0.01], [c[0] + ux * 0.01, c[1] + uz * 0.01], 0.03, RAIL_H - 0.1, 0.03, y0 + RAIL_H / 2 - 0.0)); }
      for (let j = 0; j < nb; j++) {
        const c = [pa[0] + ux * (j + 0.5) * bl, pa[1] + uz * (j + 0.5) * bl];
        for (const sgn of [-1, 1]) {
          const d = box(diag, 0.03, 0.03);
          d.applyMatrix4(new THREE.Matrix4().makeRotationZ(sgn * tilt));
          d.applyMatrix4(new THREE.Matrix4().makeRotationY(yaw));
          d.translate(c[0], y0 + 0.1 + th / 2, c[1]);
          bars.push(d);
        }
      }
    }
    // (you cannot walk through it: the wall and its railing stop you)
    const A = toW(a[0], a[1]), B = toW(b[0], b[1]);
    L.seg(A[0], A[1], B[0], B[1], wh + RAIL_H);
  }
  // ---- the steps: a short flight of granite in the opening of the east wall, out to the street, its cheeks either side
  const E = EAST[0][0], mid = (STEPS[0] + STEPS[1]) / 2, wid = STEPS[1] - STEPS[0];
  for (let s = 0; s < 4; s++) stone.push(along([E + 0.1 + s * 0.34, STEPS[0]], [E + 0.1 + s * 0.34, STEPS[1]], wid, 0.15 * (4 - s), 0.34, (0.15 * (4 - s)) / 2, 0, 1));
  for (const zc of [STEPS[0] - 0.15, STEPS[1] + 0.15]) stone.push(box(1.6, 0.8, 0.3, 1).translate(E + 0.7, 0.4, zc));
  // ---- the cross: a tall Latin cross of granite on a plinth and three steps (the captures: ≈ 9 m in all, its arms 2 m across)
  const [cx, cz] = CROSS;
  for (let s = 0; s < 3; s++) { const w = 3.4 - s * 0.5; stone.push(box(w, 0.22, w, 0.8).translate(cx, 0.11 + s * 0.22, cz)); }
  stone.push(box(1.7, 1.95, 1.7, 0.9).translate(cx, 0.66 + 0.975, cz), box(2.0, 0.2, 2.0, 0.8).translate(cx, 0.76, cz), box(2.0, 0.2, 2.0, 0.8).translate(cx, 2.51, cz));
  stone.push(box(0.95, 3.8, 0.95, 0.9).translate(cx, 2.61 + 1.9, cz), box(1.2, 0.16, 1.2, 0.8).translate(cx, 4.4, cz), box(1.15, 0.2, 1.15, 0.8).translate(cx, 6.5, cz));
  stone.push(box(0.5, 2.8, 0.5, 0.9).translate(cx, 6.6 + 1.4, cz), box(2.1, 0.46, 0.5, 0.9).translate(cx, 8.1, cz), box(0.34, 0.34, 0.54, 0.5).translate(cx, 8.1, cz));
  for (const [geo, mat] of [[merge(wall), arena], [merge(wallG), granite], [merge(cope), M.sillar], [merge(stone), M.sillar], [merge(bars), iron]]) {
    const m = new THREE.Mesh(geo, mat); m.castShadow = true; m.receiveShadow = true; g.add(m);
  }
  const C = toW(cx, cz); L.circle(C[0], C[1], 1.7, 3);
  // ---- the lamps: cast iron with two lanterns, standing inside the south wall (views 8, 11, 35)
  const { iron: li, glow: lg } = fernandina(), glowMat = new THREE.MeshStandardMaterial({ color: 0xfff4d8, emissive: 0xffe8b0, emissiveIntensity: 1.2 });
  const lampIron = variant(M.iron, 0.3, 0.32, 0.31);
  for (const [x, z] of [[-6.7, 31.7], [8.2, 31.4]]) {
    for (const [geo, mat] of [[li, lampIron], [lg, glowMat]]) { const m = new THREE.Mesh(geo, mat); m.position.set(x, 0, z); m.castShadow = mat === lampIron; g.add(m); }
    const P = toW(x, z); L.circle(P[0], P[1], 0.28, 4.8);
    const ux = Math.cos(g.rotation.y), uz = -Math.sin(g.rotation.y);
    for (const sx of [-1, 1]) L.world.lampPoints.push(P[0] + ux * sx * 0.85, 4.4, P[1] + uz * sx * 0.85);
  }
  // ---- a stone bench against the church's south wall, by the tower (view 38), and a shrub by the cross's steps (views 8, 35)
  {
    const bn = [box(1.9, 0.12, 0.5, 1).translate(0, 0.5, 0), box(0.18, 0.46, 0.46, 1).translate(-0.8, 0.23, 0), box(0.18, 0.46, 0.46, 1).translate(0.8, 0.23, 0)];
    const bm = new THREE.Mesh(merge(bn), M.sillar); bm.position.set(-20.9, 0, 14.6); bm.castShadow = true; bm.receiveShadow = true; g.add(bm);
    const B = toW(-20.9, 14.6); L.circle(B[0], B[1], 0.5, 1);
  }
  // ---- its one big tree at the north-west corner, over the bench and the wall (view 38; from the Cuesta its lower crown shows
  // beside the cross, view 35)
  const extra = L.world.extraTrees || (L.world.extraTrees = []);
  { const P = toW(TREE[0], TREE[1]); extra.push({ kind: 'encina', x: P[0], z: P[1], s: 1.3, pad: 0.3 }); }
  const rg = [];
  for (const [x, z] of ring) rg.push(...toW(x, z));
  L.map.areas.push({ kind: 'highway:pedestrian', ring: new Float32Array(rg), holes: null, name: 'Atrio de Santa María', sport: '' });
  if (L.map.buildAreaIndex) L.map.buildAreaIndex();
  L.poi.atrio = { x: C[0], z: C[1] };
}
