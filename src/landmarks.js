// Hand-modelled landmarks of Guareña placed on their real Catastro footprints:
// Iglesia de Santa María (tower 32 m), Ayuntamiento (Plaza de España), Iglesia de San Gregorio, Ermita de San Isidro,
// gas station, cooperative tanks, stadium La Noria, Guardia Civil, Centro de Salud, entry signs, plaza furniture.
import * as THREE from 'three';
import { stoneCanvas, flagCanvas, textCanvas, FLOOR_H } from './textures.js';
import { orientedRect, ringArea, ringCentroid, pointInRing, mulberry32, clamp, ringBounds } from './util.js';
import { SIN_TERRAZA } from './calles_arreglos.js';
import { shared, makeNightGlowMaterial } from './materials.js';
import { makeFurnitureGeometries } from './props.js';
import { mergeGeometries } from 'three/addons/utils/BufferGeometryUtils.js';
import { westPortal, southPortal, northPortal } from './churchdoors.js';
import { fountain, plazaDetails, updateWater, cultura, venueFront, corbacho, pabellonFront, entranceLetters, meridaRoad, avenida, bulevar } from './townplus.js';
import { buildSchools } from './schools.js';
import { STYLES as CALLES } from './calles.js';
import { atrio } from './atrio.js';
import { buildPools } from './pools.js';
import { STYLE } from './style.js';

const toLocal = (lat, lon, origin) => {
  const R = 6378137, KX = Math.cos((origin[0] * Math.PI) / 180) * R * Math.PI / 180, KZ = R * Math.PI / 180;
  return [(lon - origin[1]) * KX, -(lat - origin[0]) * KZ];
};

const at = (m, x, y, z) => { m.position.set(x, y, z); return m; };
function mergeGeos(list) {
  const clean = list.map((g) => {
    let q = g.index ? g.toNonIndexed() : g;
    if (!q.attributes.uv) q.setAttribute('uv', new THREE.Float32BufferAttribute(new Float32Array(q.attributes.position.count * 2), 2));
    for (const k of Object.keys(q.attributes)) if (!['position', 'normal', 'uv'].includes(k)) q.deleteAttribute(k);
    return q;
  });
  return mergeGeometries(clean, false);
}

function canvasTex(c, repeat = false, srgb = true) {
  const t = new THREE.CanvasTexture(c);
  if (repeat) t.wrapS = t.wrapT = THREE.RepeatWrapping;
  if (srgb) t.colorSpace = THREE.SRGBColorSpace;
  t.anisotropy = 8;
  return t;
}
// the town hall's plaque: «AYUNTAMIENTO» in two lines on cream
function aytoPlaque() {
  const c = document.createElement('canvas'); c.width = c.height = 128;
  const x = c.getContext('2d');
  x.fillStyle = '#e9e1cf'; x.fillRect(0, 0, 128, 128);
  x.fillStyle = '#3a2a1a'; x.font = 'bold 22px Arial, sans-serif'; x.textAlign = 'center'; x.textBaseline = 'middle';
  x.fillText('AYUNTA-', 64, 64 - 12.1); x.fillText('MIENTO', 64, 64 + 12.1);
  return c;
}

// Extrude a ring into walls with world-scaled UVs (tile metres) + optional flat roof
function extrudeRing(ring, y0, y1, tile = 3, withTop = false, edgeFn = null) {
  const pos = [], uv = [], nor = [], idx = [];
  const n = ring.length / 2;
  let acc = 0;
  for (let i = 0; i < n; i++) {
    const j = (i + 1) % n;
    const ax = ring[i * 2], az = ring[i * 2 + 1], bx = ring[j * 2], bz = ring[j * 2 + 1];
    const L = Math.hypot(bx - ax, bz - az);
    if (L < 0.01) continue;
    const nx = (bz - az) / L, nz = -(bx - ax) / L;
    const ef = edgeFn && edgeFn(i, ax, az, bx, bz);
    if (ef === 'skip') { acc += L; continue; }
    if (ef && ef.length) { // arched doorways through this wall: the wall as a shape with holes
      // (the doorways as notches in the outline, not holes: they stand on the ground)
      const sh = new THREE.Shape(); sh.moveTo(0, y0);
      for (const o of ef.slice().sort((p, q) => p.s - q.s)) { const r = o.w / 2; sh.lineTo(o.s - r, y0); sh.lineTo(o.s - r, y0 + o.spring); sh.absarc(o.s, y0 + o.spring, r, Math.PI, 0, true); sh.lineTo(o.s + r, y0); }
      sh.lineTo(L, y0); sh.lineTo(L, y1); sh.lineTo(0, y1); sh.closePath();
      const sg = new THREE.ShapeGeometry(sh, 16), sp = sg.attributes.position, si = sg.index.array, k = pos.length / 3;
      for (let q = 0; q < sp.count; q++) { const u = sp.getX(q), v = sp.getY(q); pos.push(ax + ((bx - ax) * u) / L, v, az + ((bz - az) * u) / L); nor.push(nx, 0, nz); uv.push((acc + u) / tile, v / tile); }
      // (the shape lies in the edge's plane; wind its faces to look out along the normal)
      for (let q = 0; q < si.length; q += 3) idx.push(k + si[q], k + si[q + 2], k + si[q + 1]);
      acc += L;
      continue;
    }
    const k = pos.length / 3;
    pos.push(ax, y0, az, bx, y0, bz, bx, y1, bz, ax, y1, az);
    for (let q = 0; q < 4; q++) nor.push(nx, 0, nz);
    uv.push(acc / tile, y0 / tile, (acc + L) / tile, y0 / tile, (acc + L) / tile, y1 / tile, acc / tile, y1 / tile);
    idx.push(k, k + 2, k + 1, k, k + 3, k + 2);
    acc += L;
  }
  if (withTop) {
    const pts = [];
    for (let i = 0; i < n; i++) pts.push(new THREE.Vector2(ring[i * 2], ring[i * 2 + 1]));
    const faces = THREE.ShapeUtils.triangulateShape(pts, []);
    const k = pos.length / 3;
    for (const p of pts) { pos.push(p.x, y1, p.y); nor.push(0, 1, 0); uv.push(p.x / tile, p.y / tile); }
    for (const f of faces) idx.push(k + f[0], k + f[2], k + f[1]);
  }
  const g = new THREE.BufferGeometry();
  g.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
  g.setAttribute('normal', new THREE.Float32BufferAttribute(nor, 3));
  g.setAttribute('uv', new THREE.Float32BufferAttribute(uv, 2));
  g.setIndex(idx);
  return g;
}

// Box with UVs scaled in metres
function sbox(w, h, d, tile = 2) {
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

// Gable roof prism along local x: length L, width W, rise H
function gableRoof(L, W, H, over = 0.4, tile = 2.6) {
  const x0 = -L / 2 - over, x1 = L / 2 + over, z0 = -W / 2 - over, z1 = W / 2 + over;
  const slope = Math.hypot(W / 2 + over, H);
  const pos = [x0, 0, z0, x1, 0, z0, x1, H, 0, x0, H, 0, x1, 0, z1, x0, 0, z1, x0, H, 0, x1, H, 0];
  const uv = [0, 0, (x1 - x0) / tile, 0, (x1 - x0) / tile, slope / tile, 0, slope / tile, 0, 0, (x1 - x0) / tile, 0, (x1 - x0) / tile, slope / tile, 0, slope / tile];
  const idx = [0, 3, 2, 0, 2, 1, 4, 7, 6, 4, 6, 5];
  const g = new THREE.BufferGeometry();
  g.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
  g.setAttribute('uv', new THREE.Float32BufferAttribute(uv, 2));
  g.setIndex(idx);
  g.computeVertexNormals();
  return g;
}
// triangular gable-end wall (in local XY plane, facing +z)
function gableEnd(W, H, tile = 3) {
  const s = new THREE.Shape();
  s.moveTo(-W / 2, 0); s.lineTo(W / 2, 0); s.lineTo(0, H); s.closePath();
  const g = new THREE.ShapeGeometry(s);
  const uv = g.attributes.uv, p = g.attributes.position;
  for (let i = 0; i < uv.count; i++) uv.setXY(i, p.getX(i) / tile, p.getY(i) / tile);
  return g;
}
// round arch frame (half torus-ish ring) in XY plane
function archRing(r, thick, depth, seg = 12) {
  const s = new THREE.Shape();
  s.absarc(0, 0, r + thick, 0, Math.PI, false);
  s.lineTo(-r, 0);
  s.absarc(0, 0, r, Math.PI, 0, true);
  s.closePath();
  const g = new THREE.ExtrudeGeometry(s, { depth, bevelEnabled: false, curveSegments: seg });
  g.translate(0, 0, -depth / 2);
  return g;
}
// dark arched opening panel
function archPanel(w, h, seg = 12) {
  const s = new THREE.Shape();
  const r = w / 2;
  s.moveTo(-r, 0); s.lineTo(r, 0); s.lineTo(r, h - r); s.absarc(0, h - r, r, 0, Math.PI, false); s.lineTo(-r, 0);
  return new THREE.ShapeGeometry(s, seg);
}

// a stone material tinted from another's, keeping the clay look's defines (a clone starts again from the standard ones)
function tinted(m, r, g, b) {
  const c = m.clone();
  c.defines = Object.assign({}, m.defines);
  c.color.setRGB(r, g, b);
  return c;
}
// where a wall of an outline (the edges of church()) stands at x, on one side of it: s = −1 the north one, +1 the south one
function zAtEdges(edges, x, s) {
  let best = null;
  for (const e of edges) {
    const lo = Math.min(e.a[0], e.b[0]), hi = Math.max(e.a[0], e.b[0]);
    if (hi - lo < 0.5 || x < lo || x > hi) continue;
    const z = e.a[1] + ((e.b[1] - e.a[1]) * (x - e.a[0])) / (e.b[0] - e.a[0]);
    if (best === null || (s > 0 ? z > best : z < best)) best = z;
  }
  return best === null ? s * 13.5 : best;
}

export function buildLandmarks(world, map) {
  return new Landmarks(world, map);
}

class Landmarks {
  constructor(world, map) {
    this.world = world;
    this.map = map;
    this.root = new THREE.Group();
    this.root.name = 'landmarks';
    world.root.add(this.root);
    this.claimed = [];       // rings whose generic parts must be skipped
    this.claimedB = new Set();
    this.colliders = [];     // rings for collision
    this.animated = [];
    this.flags = [];
    this.poi = {};           // named positions for gameplay
    this.overrides = new Map();
    const q = world.q;
    // materials
    const bumps = {};
    const tex = (kind, seed) => { const cv = stoneCanvas(kind, q.texSize >= 512 ? 512 : 256, seed); if (cv.bump) bumps[kind] = canvasTex(cv.bump, true, false); return canvasTex(cv, true); };
    this.mat = {
      mamp: new THREE.MeshStandardMaterial({ map: tex('mamposteria', 11), roughness: 0.95 }),
      sillar: new THREE.MeshStandardMaterial({ map: tex('sillar', 12), roughness: 0.9 }),
      revoco: new THREE.MeshStandardMaterial({ map: tex('revoco', 13), roughness: 0.95 }),
      teja: new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 0.85 }),
      cal: new THREE.MeshStandardMaterial({ color: 0xf7f5ef, roughness: 0.95 }),
      dark: new THREE.MeshStandardMaterial({ color: 0x15130f, roughness: 1 }),
      glass: new THREE.MeshStandardMaterial({ color: 0x1b2430, roughness: 0.1, metalness: 0.3 }),
      iron: new THREE.MeshStandardMaterial({ color: 0x1c1c1e, roughness: 0.5, metalness: 0.6 }),
      bronze: new THREE.MeshStandardMaterial({ color: 0x6b4a2a, roughness: 0.35, metalness: 0.85 }),
      wood: new THREE.MeshStandardMaterial({ color: 0x5a3a22, roughness: 0.8 }),
      steel: new THREE.MeshStandardMaterial({ color: 0xc8ccd0, roughness: 0.35, metalness: 0.7 }),
      white: new THREE.MeshStandardMaterial({ color: 0xf2f2ee, roughness: 0.6 }),
      green: new THREE.MeshStandardMaterial({ color: 0x1f7a3d, roughness: 0.6 }),
      red: new THREE.MeshStandardMaterial({ color: 0xc8202a, roughness: 0.6 }),
    };
    // roof tile texture from facade array would need the array; draw a small canvas instead
    this.mat.teja.map = canvasTex(this.tileCanvas(), true);
    // (claymation: the church, the town hall and the rest worked by hand like the houses: their marks deeper and in the colour)
    if (STYLE.plastilina) for (const k of ['mamp', 'sillar', 'revoco', 'teja', 'cal', 'white']) this.mat[k].defines = { CLAY_RELIEF: '2.3', CLAY_TONE: '2.4', CLAY_SET: '0', CLAY_TILE: '2.4', CLAY_AMP: '0.012', CLAY_CAV: '0.22' };
    // (claymation: the church's stones swell from their bed — the relief painted with them, textures.js clayStones)
    if (bumps.mamposteria) { this.mat.mamp.bumpMap = bumps.mamposteria; this.mat.mamp.bumpScale = 5; }
    if (bumps.sillar) { this.mat.sillar.bumpMap = bumps.sillar; this.mat.sillar.bumpScale = 4; }
    this.build();
  }

  tileCanvas() {
    const S = 256, c = document.createElement('canvas');
    c.width = c.height = S;
    const x = c.getContext('2d');
    const rnd = mulberry32(5);
    x.fillStyle = '#8f452a'; x.fillRect(0, 0, S, S);
    const cols = 10, rows = 5, cw = S / cols, rh = S / rows;
    for (let i = 0; i < cols; i++) for (let j = 0; j < rows; j++) {
      const v = 0.8 + rnd() * 0.3;
      const g = x.createLinearGradient(i * cw, 0, (i + 1) * cw, 0);
      const conv = i % 2 === 0;
      g.addColorStop(0, `rgb(${120 * v | 0},${58 * v | 0},${36 * v | 0})`);
      g.addColorStop(0.5, `rgb(${(conv ? 190 : 150) * v | 0},${(conv ? 95 : 72) * v | 0},${(conv ? 58 : 45) * v | 0})`);
      g.addColorStop(1, `rgb(${120 * v | 0},${58 * v | 0},${36 * v | 0})`);
      x.fillStyle = g;
      x.fillRect(i * cw, j * rh + (i % 2) * rh * 0.5, cw, rh);
      x.fillStyle = 'rgba(30,10,5,0.35)';
      x.fillRect(i * cw, j * rh + (i % 2) * rh * 0.5 + rh - 3, cw, 3);
    }
    return c;
  }

  // ---------------------------------------------------------------- helpers
  add(geo, mat, x, y, z, ry = 0, cast = true) {
    const m = new THREE.Mesh(geo, mat);
    m.position.set(x, y, z);
    m.rotation.y = ry;
    m.castShadow = cast; m.receiveShadow = true;
    this.root.add(m);
    return m;
  }
  frame(cx, cz, ux, uz) {
    // local frame: +x along u, +z along v = (-uz, ux) rotated; returns group positioned & rotated
    const g = new THREE.Group();
    g.position.set(cx, 0, cz);
    g.rotation.y = Math.atan2(ux, uz) - Math.PI / 2; // local +x -> u
    this.root.add(g);
    g.updateMatrixWorld(true);
    return g;
  }
  put(group, geo, mat, x, y, z, ry = 0, cast = true) {
    const m = new THREE.Mesh(geo, mat);
    m.position.set(x, y, z);
    m.rotation.y = ry;
    m.castShadow = cast; m.receiveShadow = true;
    group.add(m);
    return m;
  }
  building(x, z) { return this.map.buildingAt(x, z); }
  claim(b) {
    if (!b) return;
    this.claimed.push(b.ring);
    this.claimedB.add(b.id);
    this.colliders.push({ ring: b.ring, h: 30 });
  }
  claims(x, z) {
    for (const r of this.claimed) if (pointInRing(x, z, r)) return true;
    return false;
  }
  claimsBuilding(b) { return this.claimedB.has(b.id); }
  addColliders(map) {
    for (const c of this.colliders) map.collider.addRing(c.ring, c.h, -10);
    for (const c of this.circleColliders || []) map.collider.addCircle(c[0], c[1], c[2], c[3], -11);
    for (const s of this.segColliders || []) map.collider.addSegment(s[0], s[1], s[2], s[3], s[4], -11);
  }
  circle(x, z, r, h) { (this.circleColliders || (this.circleColliders = [])).push([x, z, r, h]); }
  seg(ax, az, bx, bz, h) { (this.segColliders || (this.segColliders = [])).push([ax, az, bx, bz, h]); }

  build() {
    const o = this.map.raw.origin;
    this.church(toLocal(38.8601623, -6.104399, o));
    atrio(this); // (its atrium, on the south side: atrio.js)
    this.ayuntamiento(toLocal(38.85952, -6.10286, o));
    this.sanGregorio(toLocal(38.8593944, -6.0999634, o));
    this.ermita(toLocal(38.8484523, -6.0775261, o));
    this.mercado(toLocal(38.85949, -6.10063, o));
    this.ermitaPlazaVieja();
    this.plaza();
    fountain(this); plazaDetails(this);
    cultura(this);
    buildPools(this);
    corbacho(this);
    pabellonFront(this);
    if (!(CALLES['Avenida de la Constitución'] || {}).mediana) avenida(this); // (its own, as seen, below — not both: it had two sets of trees and lamps until 2026-10-14)
    // (and the medians of the streets whose captures show one: calles.js mediana)
    for (const [name, st] of Object.entries(CALLES)) if (st.mediana) avenida(this, name, st.mediana);
    for (const [name, st] of Object.entries(CALLES)) if (st.bulevar) for (const bv of [].concat(st.bulevar)) bulevar(this, bv, name); // (in pieces where crossings break it)
    entranceLetters(this);
    meridaRoad(this);
    this.gasStation();
    this.tanks();
    this.stadium();
    this.services();
    buildSchools(this); // (src/schools.js: fences, gates, flags and yards of the schools)
    // traffic signs and the town entry boards now come from signs.js (built with the street furniture)
    this.terraces();
    this.plazaTrees();
  }

  // ================================================================ bar terraces (mesas, sillas y sombrillas)
  terraces() {
    const map = this.map;
    const bars = map.pois.filter((p) => /amenity:(bar|cafe|pub|restaurant|ice_cream)/.test(p.kind) && map.inTown(p.x, p.z));
    const tables = [], chairs = [], umbrellas = [], poles = [];
    const rnd = mulberry32(31);
    const cols = [0xf2efe6, 0xc8202a, 0x1f6b3a, 0x2659a6, 0xe6b422];
    const umbrellaMats = cols.map((c) => new THREE.MeshStandardMaterial({ color: c, roughness: 0.8, side: THREE.DoubleSide }));
    const byColor = umbrellaMats.map(() => []);
    const noTerrace = SIN_TERRAZA.map((r) => ({ r, bb: ringBounds(r) }));
    for (const b of bars) {
      // (the Café/Bar El Parque on the EX-338: its capture — view 288, May 2024 — shows its pavement bare, shop fronts under awnings
      // and no table, chair or sunshade: it keeps its place on the map but puts none out)
      if (/El Parque$/.test(b.name)) continue;
      // walk from the bar towards the nearest street/plaza to find open ground
      const q = map.nearestEdge(b.x, b.z, 30, (e) => !e.dirt);
      if (!q) continue;
      const dx = q.x - b.x, dz = q.z - b.z, L = Math.hypot(dx, dz) || 1;
      const ux = dx / L, uz = dz / L;
      const ed = map.sample(q.edge, q.s, {});
      const plazaNear = map.areas.some((a) => (a.kind === 'highway:pedestrian' || a.kind === 'place:square' || a.kind === 'leisure:park') && pointInRing(q.x, q.z, a.ring));
      const wide = q.edge.cls === 'pedestrian' || q.edge.walkOnly || plazaNear || q.edge.sw >= 1.8;
      if (!wide) continue;
      const color = Math.floor(rnd() * cols.length);
      const n = 2 + Math.floor(rnd() * 3);
      const mute = noTerrace.some((o) => b.x > o.bb[0] - 6 && b.x < o.bb[2] + 6 && b.z > o.bb[1] - 6 && b.z < o.bb[3] + 6 && (pointInRing(b.x, b.z, o.r) || pointInRing(b.x + ux * 3, b.z + uz * 3, o.r))), keep = [tables.length, chairs.length, byColor[color].length, (this.circleColliders || []).length];
      for (let k = 0; k < n; k++) {
        const along = (k - (n - 1) / 2) * 2.6;
        const base = q.edge.walkOnly || plazaNear ? L * 0.5 : Math.max(0.2, L - q.edge.w / 2 - 1.4);
        const x = b.x + ux * base + ed.dx * along, z = b.z + uz * base + ed.dz * along;
        if (map.buildingAt(x, z)) continue;
        const nq = map.nearestEdge(x, z, 12, (e) => e.drive);
        if (nq && nq.d < nq.edge.w / 2 + 0.4 && !nq.edge.walkOnly) continue;
        tables.push([x, z]);
        for (let c = 0; c < 3; c++) {
          const a = (c / 3) * Math.PI * 2 + rnd();
          chairs.push([x + Math.cos(a) * 0.62, z + Math.sin(a) * 0.62, -a + Math.PI / 2]);
        }
        byColor[color].push([x, z]);
        this.circle(x, z, 0.45, 1);
      }
      // (none where the captures show none — calles_arreglos.js SIN_TERRAZA: laid as before, the draw unchanged for the
      // others, then taken back)
      if (mute) { tables.length = keep[0]; chairs.length = keep[1]; byColor[color].length = keep[2]; if (this.circleColliders) this.circleColliders.length = keep[3]; }
    }
    if (!tables.length) return;
    const mk = (geo, mat, list, rotIdx = -1) => {
      const im = new THREE.InstancedMesh(geo, mat, list.length);
      const m = new THREE.Matrix4(), qq = new THREE.Quaternion(), up = new THREE.Vector3(0, 1, 0);
      list.forEach((p, i) => { qq.setFromAxisAngle(up, rotIdx >= 0 ? p[rotIdx] : 0); m.compose(new THREE.Vector3(p[0], 0, p[1]), qq, new THREE.Vector3(1, 1, 1)); im.setMatrixAt(i, m); });
      im.castShadow = true; im.receiveShadow = true;
      this.root.add(im);
      return im;
    };
    const table = mergeGeos([new THREE.CylinderGeometry(0.38, 0.38, 0.03, 16).translate(0, 0.74, 0), new THREE.CylinderGeometry(0.03, 0.03, 0.74, 6).translate(0, 0.37, 0), new THREE.CylinderGeometry(0.25, 0.25, 0.03, 12).translate(0, 0.015, 0)]);
    const chair = mergeGeos([new THREE.BoxGeometry(0.42, 0.04, 0.42).translate(0, 0.45, 0), new THREE.BoxGeometry(0.42, 0.42, 0.04).translate(0, 0.68, -0.2), ...[[-0.18, -0.18], [0.18, -0.18], [-0.18, 0.18], [0.18, 0.18]].map(([a, b]) => new THREE.CylinderGeometry(0.015, 0.015, 0.45, 5).translate(a, 0.225, b))]);
    mk(table, this.mat.steel, tables);
    mk(chair, new THREE.MeshStandardMaterial({ color: 0xb9bcbf, roughness: 0.4, metalness: 0.6 }), chairs, 2);
    const canopy = new THREE.ConeGeometry(1.35, 0.45, 8, 1, true); canopy.translate(0, 2.35, 0);
    const pole = new THREE.CylinderGeometry(0.025, 0.025, 2.4, 6); pole.translate(0, 1.2, 0);
    byColor.forEach((list, i) => { if (list.length) mk(canopy, umbrellaMats[i], list); });
    mk(pole, this.mat.white, tables);
  }

  // ================================================================ the hermitage of the Plaza Vieja
  // As the user's captures show it (2026-10-13): a whitewashed single nave, building 1260 (calles_casas.js keeps its
  // walls blind and one tall storey), its baroque portal of granite facing the park to the west — a round arch on
  // pilasters, an entablature and a curved crown with its niche — and at its south end, by the corner of the Calle
  // Fuentes, a bell-gable with its bell and an iron cross.
  ermitaPlazaVieja() {
    const b = this.map.buildings[1260];
    if (!b) return;
    const r = b.ring, n = r.length / 2, park = [-150, 156], ccw = ringArea(r) > 0, M = this.mat;
    let best = null;
    for (let i = 0; i < n; i++) {
      const j = (i + 1) % n, ax = r[i * 2], az = r[i * 2 + 1], bx = r[j * 2], bz = r[j * 2 + 1], L = Math.hypot(bx - ax, bz - az);
      if (L < 4) continue;
      let nx = (bz - az) / L, nz = -(bx - ax) / L;
      if (!ccw) { nx = -nx; nz = -nz; }
      const mx = (ax + bx) / 2, mz = (az + bz) / 2, tx = park[0] - mx, tz = park[1] - mz, tl = Math.hypot(tx, tz) || 1;
      const score = ((nx * tx + nz * tz) / tl) * L; // (the front that looks onto the park, the longer the better)
      if (!best || score > best.score) best = { score, ax, az, bx, bz, L, nx, nz, mx, mz };
    }
    if (!best) return;
    const { L, nx, nz, mx, mz } = best;
    const g = this.frame(mx, mz, nz, -nx); // (local x along the front, z out of it)
    // the portal (the captures, 2026-10-14: at the front's north end, ≈ 2 m from its corner; granite the dark brown-grey of
    // the town's old stone): an arch of voussoirs between jambs of alternating blocks, a moulded cornice, over it a
    // cartouche with its niche between volutes, and behind it the whitewashed wall's shaped gable, curving up over the eaves
    const H = 2 * FLOOR_H, gran = tinted(M.sillar, 0.5, 0.4, 0.34), px = -1.9;
    const pg = new THREE.Group(); pg.position.set(px, 0, 0); g.add(pg);
    const door = new THREE.Mesh(archPanel(1.5, 2.9), M.wood); door.position.set(0, 0, 0.03); pg.add(door);
    const stone = [];
    for (const s of [-1, 1]) for (let k = 0; k < 4; k++) { const w = k % 2 ? 0.6 : 0.85; stone.push(sbox(w, 0.55, 0.42, 1).translate(s * (0.75 + w / 2), 0.275 + k * 0.55, 0.21)); }
    stone.push(archRing(0.75, 0.42, 0.42).translate(0, 2.15, 0.21), sbox(0.46, 0.7, 0.5, 1).translate(0, 2.15 + 0.75 + 0.35, 0.25));
    for (const s of [-1, 1]) stone.push(sbox(0.55, 0.14, 0.46, 1).translate(s * 1.0, 2.15, 0.23));
    stone.push(sbox(3.0, 0.28, 0.58, 1).translate(0, 3.3, 0.29), sbox(3.2, 0.12, 0.74, 1).translate(0, 3.5, 0.37));
    stone.push(sbox(1.3, 1.55, 0.34, 1).translate(0, 3.56 + 0.78, 0.2), sbox(1.7, 0.16, 0.46, 1).translate(0, 5.18, 0.26));
    for (const s of [-1, 1]) { const vo = new THREE.TorusGeometry(0.34, 0.08, 6, 14, Math.PI * 1.5); vo.rotateZ(s > 0 ? -Math.PI * 0.25 : Math.PI * 1.25); stone.push(vo.translate(s * 1.0, 3.95, 0.2)); stone.push(sbox(0.34, 0.5, 0.3, 1).translate(s * 0.95, 3.82, 0.18)); }
    stone.push(new THREE.SphereGeometry(0.2, 10, 8).translate(0, 5.5, 0.26), sbox(0.18, 0.2, 0.18, 1).translate(0, 5.36, 0.26));
    { const pm = new THREE.Mesh(mergeGeos(stone), gran); pm.castShadow = true; pm.receiveShadow = true; pg.add(pm); }
    const niche = new THREE.Mesh(archPanel(0.5, 1.05), M.dark); niche.position.set(0, 3.72, 0.375); pg.add(niche);
    { const sh = new THREE.Shape(); // (the gable: a shaped profile, a quarter-round either side of a straight top)
      sh.moveTo(-1.9, 0); sh.lineTo(-1.9, 0.3); sh.quadraticCurveTo(-1.5, 0.35, -1.1, 0.9); sh.quadraticCurveTo(-0.85, 1.4, -0.55, 1.45); sh.lineTo(0.55, 1.45); sh.quadraticCurveTo(0.85, 1.4, 1.1, 0.9); sh.quadraticCurveTo(1.5, 0.35, 1.9, 0.3); sh.lineTo(1.9, 0); sh.closePath();
      const gm = new THREE.Mesh(new THREE.ExtrudeGeometry(sh, { depth: 0.3, bevelEnabled: false, curveSegments: 8 }), M.cal); gm.position.set(0, H - 0.1, -0.1); gm.castShadow = true; pg.add(gm);
    }
    // the grey painted footing along the faces that look at the park and the street (1.1 m, the captures' «zócalo gris corrido»)
    { const plinth = tinted(M.cal, 0.5, 0.5, 0.49), pr = this.map.buildings[1260].ring, np = pr.length / 2;
      for (let i = 0; i < np; i++) {
        const j = (i + 1) % np, ax = pr[i * 2], az = pr[i * 2 + 1], bx = pr[j * 2], bz = pr[j * 2 + 1], el = Math.hypot(bx - ax, bz - az);
        if (el < 1.5) continue;
        let ex = (bz - az) / el, ez = -(bx - ax) / el; if (!ccw) { ex = -ex; ez = -ez; }
        const tl2 = Math.hypot(park[0] - (ax + bx) / 2, park[1] - (az + bz) / 2) || 1;
        if ((ex * (park[0] - (ax + bx) / 2) + ez * (park[1] - (az + bz) / 2)) / tl2 < 0.25 && ez < 0.6) continue;
        this.add(sbox(el, 1.1, 0.16, 1.2), plinth, (ax + bx) / 2 + ex * 0.07, 0.55, (az + bz) / 2 + ez * 0.07, Math.atan2(-(bz - az), bx - ax));
      } }
    // a wall lantern on the next face along (the captures: an iron bracket and a glass lantern over the footing's line, at the
    // height of the eaves' first storey), lit at night
    { const pr = this.map.buildings[1260].ring, np = pr.length / 2;
      let bestE = null;
      for (let i = 0; i < np; i++) { const j = (i + 1) % np, ax = pr[i * 2], az = pr[i * 2 + 1], bx = pr[j * 2], bz = pr[j * 2 + 1], el = Math.hypot(bx - ax, bz - az); if (el < 2.5 || (ax + bx) / 2 > mx - 3) continue; if (!bestE || el < bestE.el) bestE = { ax, az, bx, bz, el }; }
      if (bestE) {
        let ex = (bestE.bz - bestE.az) / bestE.el, ez = -(bestE.bx - bestE.ax) / bestE.el; if (!ccw) { ex = -ex; ez = -ez; }
        const lx = (bestE.ax + bestE.bx) / 2, lz = (bestE.az + bestE.bz) / 2, lg = new THREE.Group();
        lg.add(at(new THREE.Mesh(new THREE.BoxGeometry(0.05, 0.05, 0.7), M.iron), 0, 4.3, 0.35));
        lg.add(at(new THREE.Mesh(new THREE.CylinderGeometry(0.17, 0.12, 0.42, 6), makeNightGlowMaterial(0xfff0cc, { dayLevel: 0.85, nightLevel: 2.4 })), 0, 4.28, 0.7));
        lg.add(at(new THREE.Mesh(new THREE.ConeGeometry(0.24, 0.2, 6), M.iron), 0, 4.6, 0.7));
        lg.position.set(lx, 0, lz); lg.rotation.y = Math.atan2(ex, ez); lg.traverse((q) => { if (q.isMesh) q.castShadow = true; }); this.root.add(lg);
        this.world.lampPoints.push(lx + ex * 0.7, 4.3, lz + ez * 0.7);
      } }
    // the bell-gable, at the south end of the roof, over the south wall (the captures: toward the right of the front, well past the portal)
    const x = 7.4;
    this.put(g, sbox(2.4, 2.6, 0.5, 1.5), M.cal, x, H + 1.3, -0.25);
    this.put(g, sbox(1.3, 0.55, 0.5, 1.5), M.cal, x, H + 2.88, -0.25);
    this.put(g, sbox(2.5, 0.12, 0.6, 1), M.sillar, x, H + 2.6, -0.25);
    for (const s of [-1, 1]) { const open = new THREE.Mesh(archPanel(0.7, 1.2), M.dark); open.position.set(x + s * 0.6, H + 0.8, 0.01); g.add(open); }
    const bell = new THREE.Mesh(new THREE.CylinderGeometry(0.16, 0.3, 0.45, 10, 1, true), M.bronze); bell.position.set(x - 0.6, H + 1.45, -0.25); g.add(bell);
    for (const sx of [-1.1, 1.1]) this.put(g, new THREE.SphereGeometry(0.17, 8, 6), M.sillar, x + sx, H + 2.78, -0.25);
    this.put(g, new THREE.SphereGeometry(0.19, 8, 6), M.sillar, x, H + 3.3, -0.25);
    this.put(g, sbox(0.08, 0.9, 0.08), M.iron, x, H + 3.8, -0.25);
    this.put(g, sbox(0.45, 0.08, 0.08), M.iron, x, H + 3.95, -0.25);
    // (no palm over the ermita: vegetation.js plants one in the garden behind it, at (−112, 165.9), where the captures show sky)
    this.claimed.push([-113.2, 164.7, -110.8, 164.7, -110.8, 167.1, -113.2, 167.1]);
    this.poi.ermitaPlazaVieja = { x: mx + nx * 2, z: mz + nz * 2 };
  }

  // ================================================================ orange trees around the plazas
  plazaTrees() {
    const extra = this.world.extraTrees || (this.world.extraTrees = []);
    for (const a of this.map.areas) {
      if (!(a.kind === 'highway:pedestrian' || a.kind === 'place:square' || a.kind === 'amenity:marketplace')) continue;
      // (a square seen in its captures has the trees they show: calles.js — the atrium of Santa María its two pines, the
      // Plaza de Abastos none)
      const cs = CALLES[a.name];
      if (cs && !cs.arboles) continue;
      const kind = (cs && cs.arboles.kind) || 'naranjo';
      const r = a.ring;
      const n = r.length / 2;
      for (let i = 0; i < n; i++) {
        const j = (i + 1) % n;
        const ax = r[i * 2], az = r[i * 2 + 1], bx = r[j * 2], bz = r[j * 2 + 1];
        const L = Math.hypot(bx - ax, bz - az);
        if (L < 8) continue;
        const ix = -(bz - az) / L, iz = (bx - ax) / L; // inward for CCW rings
        for (let s = 4; s < L - 3; s += 9) {
          const x = ax + ((bx - ax) * s) / L + ix * 2.2, z = az + ((bz - az) * s) / L + iz * 2.2;
          if (!pointInRing(x, z, r) || this.map.buildingAt(x, z) || this.claims(x, z)) continue;
          // (none before the town hall: its arcade looks onto the bars' terraces, as its photograph shows)
          const af = this.poi.ayto && this.poi.ayto.front;
          if (af && Math.abs((x - af.mx) * af.ux + (z - af.mz) * af.uz) < af.half && ((x - af.mx) * this.poi.ayto.nx + (z - af.mz) * this.poi.ayto.nz) < 10) continue;
          extra.push({ kind, x, z, s: 1 });
        }
      }
    }
  }

  // ================================================================ Iglesia de Santa María
  church([x, z]) {
    const b = this.building(x, z);
    if (!b) return;
    this.claim(b);
    const ob = orientedRect(b.ring);
    let ux = Math.cos(ob.ang), uz = Math.sin(ob.ang);
    let L = ob.hw, W = ob.hd;
    if (W > L) { [L, W] = [W, L]; [ux, uz] = [-uz, ux]; }
    if (ux < 0) { ux = -ux; uz = -uz; } // u points east (towards the apse)
    const vx = -uz, vz = ux;             // v perpendicular; make it point south (+z)
    const south = vz > 0 ? 1 : -1;
    const g = this.frame(ob.cx, ob.cz, ux, uz);
    // in frame: local x along u (east), local z along ±v
    const M = this.mat;
    // base annexes: extrude real footprint (chapels, sacristy)
    const ringLocal = [];
    const ang = -(Math.atan2(ux, uz) - Math.PI / 2);
    const ca = Math.cos(ang), sa = Math.sin(ang);
    for (let i = 0; i < b.ring.length; i += 2) {
      const dx = b.ring[i] - ob.cx, dz = b.ring[i + 1] - ob.cz;
      ringLocal.push(dx * ca + dz * sa, -dx * sa + dz * ca);
    }
    // the nave's own axis: half way between its north and south walls — the sacristy pulls the outline's rectangle off
    // it (2 m at Santa María): the frame moves onto it, so the portal, the oculus and the nave stand where they are
    {
      let xmin = Infinity, xmax = -Infinity, zmin = Infinity, zmax = -Infinity;
      for (let i = 0; i < ringLocal.length; i += 2) { xmin = Math.min(xmin, ringLocal[i]); xmax = Math.max(xmax, ringLocal[i]); }
      const xcut = xmin + 0.6 * (xmax - xmin); // (the west part, before the sacristy and the apse)
      for (let i = 0; i < ringLocal.length; i += 2) { const z2 = ringLocal[i + 1]; zmin = Math.min(zmin, z2); if (ringLocal[i] < xcut) zmax = Math.max(zmax, z2); }
      const zc = (zmin + zmax) / 2;
      for (let i = 1; i < ringLocal.length; i += 2) ringLocal[i] -= zc;
      g.position.x += -uz * zc; g.position.z += ux * zc; g.updateMatrixWorld(true);
      ob.cx = g.position.x; ob.cz = g.position.z;
    }
    // where a line across the footprint meets its outline (local frame): along z at a given x, or along x at a given z
    const cross = (axis, at, pick) => {
      let best = null;
      for (let i = 0, n = ringLocal.length / 2; i < n; i++) {
        const j = (i + 1) % n, ax = ringLocal[i * 2], az = ringLocal[i * 2 + 1], bx = ringLocal[j * 2], bz = ringLocal[j * 2 + 1];
        const [pa, pb, qa, qb] = axis === 'x' ? [az, bz, ax, bx] : [ax, bx, az, bz];
        if ((pa - at) * (pb - at) > 0 || pa === pb) continue;
        const v = qa + ((qb - qa) * (at - pa)) / (pb - pa);
        if (best === null || pick(v, best.v)) best = { v, i };
      }
      return best;
    };
    // ---- the body, as the Catastro and the captures give it (2026-10-14; the measures are in docs/hiperrealismo.md): the
    // outline IS the walls, up to the cornice at 22 m, all in one plane — a block 27 m across. It was a low annex on the
    // outline and a narrower nave set back on top of it, which showed as a stepped wall from the north (audit n59). Over
    // its middle the nave's own roof, 18 m wide, between the flat roofs of the aisles' chapels; the tower at the
    // south-west corner, the polygonal head at the east, and the sacristy, lower, round the head's south side
    const nw = 9, H = 22;
    const xw = cross('x', 0, (v, b2) => v < b2);
    const x0 = clamp(xw ? xw.v - 0.05 : -L + 1.2, -L + 0.1, -L + 2.4), xa = L - nw - 1.5; // nave from the west front to the head
    const BX = [-11.1, -2.35, 6.1, 14.9]; // the flat bands of ashlar up the long walls (PNOA's rhythm, the captures' bands)
    const WX = [-16.3, -6.9, 1.6, 10.5];  // a window in each bay, high up
    // the side doors in the third bay, between its bands: the Mediodía (south) one onto its atrium, the Gospel one shut
    const xs = (BX[1] + BX[2]) / 2;
    const sHit = cross('z', xs, (v, b2) => (south > 0 ? v > b2 : v < b2)), nHit = cross('z', xs, (v, b2) => (south > 0 ? v < b2 : v > b2));
    const doorEdges = new Map();
    const addDoor = (i, ax, az, at2, wDoor, sp2) => (doorEdges.get(i) || doorEdges.set(i, []).get(i)).push({ s: Math.hypot(at2[0] - ax, at2[1] - az), w: wDoor, spring: sp2 });
    for (const [hit, wDoor, sp2] of [[sHit, 2.3, 3.3], [nHit, 2.2, 3.2]]) {
      if (!hit) continue;
      const i = hit.i, n = ringLocal.length / 2, j = (i + 1) % n;
      const ax = ringLocal[i * 2], az = ringLocal[i * 2 + 1], bx = ringLocal[j * 2], bz = ringLocal[j * 2 + 1];
      const sAlong = Math.hypot(xs - ax, hit.v - az);
      if (sAlong > wDoor && Math.hypot(bx - ax, bz - az) - sAlong > wDoor) {
        addDoor(i, ax, az, [xs, hit.v], wDoor, sp2);
        const ex = bx - ax, ez = bz - az, el = Math.hypot(ex, ez), side = Math.sign(hit.v) || 1;
        let nx = ez / el, nz = -ex / el; if (Math.sign(nz) !== side) { nx = -nx; nz = -nz; }
        hit.ok = true; hit.nx = nx; hit.nz = nz;
      }
    }
    // the main door at the foot, through the middle plane of the west front
    if (xw) addDoor(xw.i, ringLocal[xw.i * 2], ringLocal[xw.i * 2 + 1], [xw.v, 0], 2.6, 3.7);
    // the outline split in two: the main body, and the sacristy (the Catastro's last 14 points, x > 9.5 and z > 7.4). The
    // head's south side is hidden under the sacristy in the Catastro, so it is drawn as the north's, in mirror
    const R2 = ringLocal, n2 = R2.length / 2, pt = (i) => [R2[i * 2], R2[i * 2 + 1]];
    let mainPts = Array.from({ length: n2 }, (_, i) => pt(i)), sacPts = null, mainIdx = (i) => i;
    if (n2 === 34 && south > 0) {
      const mir = (i) => [pt(i)[0], -pt(i)[1]];
      mainPts = [...Array.from({ length: 20 }, (_, i) => pt(i)), mir(11), mir(10), mir(9), [pt(8)[0], pt(33)[1] - (pt(8)[0] - pt(33)[0]) * 0.0293], pt(33)];
      sacPts = [...Array.from({ length: 15 }, (_, i) => pt(19 + i)), [pt(33)[0], pt(19)[1]]];
      mainIdx = (i) => (i === 33 ? mainPts.length - 1 : i);
    }
    const origIdx = (i) => (sacPts && i === mainPts.length - 1 ? 33 : i);
    const mainEdges = mainPts.map((a, i) => { const b = mainPts[(i + 1) % mainPts.length], dx = b[0] - a[0], dz = b[1] - a[1], len = Math.hypot(dx, dz); return { i, a, b, dx, dz, len, nx: dz / len, nz: -dx / len, yaw: Math.atan2(-dz, dx), gaps: doorEdges.get(origIdx(i)) || [] }; }).filter((e) => e.len > 0.05);
    const sacEdges = sacPts ? sacPts.map((a, i) => { const b = sacPts[(i + 1) % sacPts.length], dx = b[0] - a[0], dz = b[1] - a[1], len = Math.hypot(dx, dz); return { i, a, b, dx, dz, len, nx: dz / len, nz: -dx / len, yaw: Math.atan2(-dz, dx), gaps: [] }; }).filter((e) => e.len > 0.05) : [];
    const doorMap = new Map(); for (const [i, v] of doorEdges) doorMap.set(mainIdx(i), v);
    // the walls, to the cornice, in the rubble masonry; the flat roofs of the chapels and aisles at the cornice's height
    this.put(g, extrudeRing(mainPts.flat(), 0, H, 3.2, false, (i) => doorMap.get(i) || null), M.mamp, 0, 0, 0);
    this.put(g, extrudeRing(mainPts.flat(), H, H, 2.6, true), M.teja, 0, 0, 0);
    // the stones that are not the rubble: the warm sandstone of the quoins, bands and frames, and the dark footing
    const quoin = tinted(M.sillar, 1.0, 0.9, 0.78), zocalo = tinted(M.sillar, 0.74, 0.7, 0.66);
    this.mat.quoin = quoin; this.mat.zocalo = zocalo;
    // a box along a wall segment (from s0 to s1 along the edge e), its middle at height y, pushed out of the wall by off
    const along = (e, s0, s1, h, d, y, off, tile) => {
      const ux = e.dx / e.len, uz = e.dz / e.len, mid = (s0 + s1) / 2, geo = sbox(s1 - s0, h, d, tile);
      geo.rotateY(e.yaw); geo.translate(e.a[0] + ux * mid + e.nx * off, y, e.a[1] + uz * mid + e.nz * off);
      return geo;
    };
    // the stretches of an edge that are not in a doorway (a door's width and a step either side stay free)
    const runs = (e) => {
      const cuts = e.gaps.map((o) => [o.s - o.w / 2 - 1.0, o.s + o.w / 2 + 1.0]).sort((p, q) => p[0] - q[0]), out = []; let s = 0;
      for (const [c0, c1] of cuts) { if (c0 - s > 0.3) out.push([s, c0]); s = c1; }
      if (e.len - s > 0.3) out.push([s, e.len]);
      return out;
    };
    // the footing: a battered bank of dark stone along the foot of every wall (the captures' «zarpa»: a metre and a bit
    // high, leaning back into the wall, a granite coping on it), broken at the doors
    const foot = [], cope = [];
    for (const e of mainEdges) {
      if (e.len < 1.5) continue;
      for (const [s0, s1] of runs(e)) {
        const sh = new THREE.Shape(); sh.moveTo(-0.3, 0); sh.lineTo(0.5, 0); sh.lineTo(0.5, 0.42); sh.lineTo(0.12, 1.15); sh.lineTo(-0.3, 1.15); sh.closePath();
        const ge = new THREE.ExtrudeGeometry(sh, { depth: s1 - s0, bevelEnabled: false });
        const p = ge.attributes.position, u = ge.attributes.uv;
        for (let q = 0; q < p.count; q++) u.setXY(q, p.getZ(q) / 1.6 + p.getX(q) * 0.3, p.getY(q) / 1.6);
        ge.translate(0, 0, -(s1 - s0) / 2); ge.rotateY(Math.atan2(e.dx, e.dz));
        const ux = e.dx / e.len, uz = e.dz / e.len, mid = (s0 + s1) / 2; ge.translate(e.a[0] + ux * mid, 0, e.a[1] + uz * mid);
        foot.push(ge);
        cope.push(along(e, s0, s1, 0.1, 0.56, 1.2, 0.04, 1.2));
      }
    }
    // the sacristy's: a smooth stone base two metres and a bit high, a moulded string course on it (capture 10)
    for (const e of sacEdges) if (e.len > 1.5) { foot.push(along(e, 0, e.len, 2.2, 0.4, 1.1, 0.12, 1.6)); cope.push(along(e, 0, e.len, 0.2, 0.62, 2.3, 0.12, 1.2)); }
    this.put(g, mergeGeos(foot), zocalo, 0, 0, 0); this.put(g, mergeGeos(cope), quoin, 0, 0, 0);
    // the cornice: moulded sandstone, 0.45 m out of the wall, its top at 22.05
    this.put(g, mergeGeos(mainEdges.filter((e) => e.len > 1).map((e) => along(e, 0, e.len, 0.55, 0.95, H - 0.22, 0.25, 1.2))), quoin, 0, 0, 0);
    // the corners of the outline: ashlar quoins, the length of both walls a metre and a half either way; the NW block's, two metres
    // (the captures: big squared granite at every corner, the rubble between)
    const turn = mainEdges.reduce((s, e) => s + (e.a[0] * e.b[1] - e.b[0] * e.a[1]), 0) > 0 ? 1 : -1;
    const qs = [];
    for (let k = 0; k < mainEdges.length; k++) {
      const e1 = mainEdges[(k + mainEdges.length - 1) % mainEdges.length], e2 = mainEdges[k];
      const c = (e1.dx * e2.dz - e1.dz * e2.dx) / (e1.len * e2.len);
      if (c * turn < 0.35) continue; // (a corner that turns less than 20°, or a hollow one: none)
      const q = 1.1, w2 = e2.a[0] < -20 && e2.a[1] < -10 ? 2.0 : q;
      qs.push(along(e1, e1.len - Math.min(w2, e1.len), e1.len, H - 0.5, 0.4, (H - 0.5) / 2, 0.02, 1.6), along(e2, 0, Math.min(w2, e2.len), H - 0.5, 0.4, (H - 0.5) / 2, 0.02, 1.6));
    }
    // the flat bands up the long walls and a window in each bay: round-headed, with a stone mullion and a carved bracket
    for (const s of [-1, 1]) for (const bxx of BX) {
      const z = zAtEdges(mainEdges, bxx, s);
      qs.push(sbox(2.0, H - 0.5, 0.5, 1.6).translate(bxx, (H - 0.5) / 2, z));
    }
    // the tower's string course at 8.6 m round its south and west faces, a row of corbels under it on the west one (the
    // photograph's «canecillos»; capture 38 shows the moulding across the south face)
    { const e1 = mainEdges[mainEdges.length - 1], e0 = mainEdges[0];
      qs.push(along(e1, e1.len - 6.4, e1.len, 0.3, 0.95, 8.6, 0.25, 1.2), along(e0, 0, e0.len, 0.3, 0.95, 8.6, 0.25, 1.2));
      for (let s = 0.4; s < e0.len - 0.3; s += 0.55) qs.push(along(e0, s, s + 0.3, 0.3, 0.55, 8.3, 0.15, 1));
    }
    this.put(g, mergeGeos(qs), quoin, 0, 0, 0);
    WX.forEach((wx, k) => {
      for (const s of [-1, 1]) {
        const z = zAtEdges(mainEdges, wx, s), y0 = k === 0 ? 15.1 : 14.6, ry = s > 0 ? 0 : Math.PI;
        this.put(g, archPanel(1.4, 3.8), M.glass, wx, y0, z + s * 0.03, ry, false);
        this.put(g, archRing(0.7, 0.26, 0.3), quoin, wx, y0 + 3.8 - 0.7, z + s * 0.12, ry, false);
        const fr = [sbox(0.26, 3.1, 0.3, 1).translate(-0.83, 1.55, 0), sbox(0.26, 3.1, 0.3, 1).translate(0.83, 1.55, 0), sbox(0.12, 3.2, 0.16, 1).translate(0, 1.6, -0.06), sbox(1.9, 0.16, 0.42, 1).translate(0, -0.08, 0.04), sbox(1.0, 0.9, 0.36, 1).translate(0, -0.62, 0.02)];
        this.put(g, mergeGeos(fr), quoin, wx, y0, z + s * 0.14, ry, false);
      }
    });
    // the little openings the captures show: two on the tower's south face, four slits and four small windows on the north-west block
    // (docs/hiperrealismo.md: measured on the photograph), one in the sacristy's east wall
    const hole = (w, h, x, y, z, ry, arch, grille) => {
      const p = arch ? archPanel(w, h, 8) : new THREE.PlaneGeometry(w, h).translate(0, h / 2, 0);
      this.put(g, p, M.dark, x, y, z, ry, false);
      const fr = [sbox(w + 0.36, 0.16, 0.2, 1).translate(0, -0.08, 0), sbox(0.16, h, 0.2, 1).translate(-(w + 0.16) / 2, h / 2, 0), sbox(0.16, h, 0.2, 1).translate((w + 0.16) / 2, h / 2, 0), sbox(w + 0.36, 0.16, 0.2, 1).translate(0, h + 0.08, 0)];
      this.put(g, mergeGeos(fr), quoin, x, y, z, ry, false);
      if (grille) for (let q = 1; q < 4; q++) this.put(g, new THREE.BoxGeometry(0.025, h, 0.025).translate(0, h / 2, 0.03), M.iron, x - w / 2 + (q * w) / 4, y, z, ry, false);
    };
    hole(0.55, 0.6, -23.3, 5.8, 13.78, 0, false, true); hole(0.5, 0.8, -23.7, 3.6, 13.78, 0, true, false);
    for (const y of [12.5, 14.9, 17.2, 19.4]) this.put(g, new THREE.PlaneGeometry(0.2, 0.9), M.dark, -26.92, y, -9.6, -Math.PI / 2, false);
    for (const [x, y] of [[-23.5, 18.6], [-24.5, 15.2], [-23.1, 12.2], [-22.5, 5.6]]) hole(0.6, 0.9, x, y, -11.35, Math.PI, false, false);
    hole(0.7, 1.4, 24.72 + 0.03, 5.6, 13.2, Math.PI / 2, false, false);
    // the nave's roof over its middle (20°, the ridge at 25.3), its gables at both ends; the head's roof a fan, a half cone
    const roof = gableRoof(xa - x0, nw * 2, 3.3, 0.5);
    this.put(g, roof, M.teja, (x0 + xa) / 2, H, 0);
    this.put(g, gableEnd(nw * 2, 3.3), M.mamp, xa + 0.02, H, 0, Math.PI / 2);
    this.put(g, gableEnd(nw * 2, 3.3), M.mamp, x0 - 0.02, H, 0, -Math.PI / 2);
    const aH = STYLE.plastilina ? 4.2 : 3.8; // (in the claymation a touch taller: the tiles at their size)
    const aroof = new THREE.ConeGeometry(L - xa + 0.1, aH, 7, 1, true, 0, Math.PI);
    if (STYLE.plastilina) { const ru = aroof.attributes.uv; for (let i = 0; i < ru.count; i++) ru.setXY(i, ru.getX(i) * 9, ru.getY(i) * 3); }
    this.put(g, aroof, M.teja, xa, H - 0.1 + aH / 2, 0);
    // the sacristy's lean-to: its eaves to the south, rising to the nave's wall (a wedge: its two ends in rubble, its slope in tile)
    if (sacPts) {
      const HS = 8.4, ex0 = 9.3, ex1 = 25.5, zl = 18.3, zh = 12.3, yl = HS - 0.05, yh = HS + 1.6;
      this.put(g, extrudeRing(sacPts.flat(), 0, HS, 3.2), M.mamp, 0, 0, 0);
      const sl = Math.hypot(zl - zh, yh - yl), pos = [ex0, yl, zl, ex1, yl, zl, ex1, yh, zh, ex0, yh, zh];
      const slope = new THREE.BufferGeometry();
      slope.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
      slope.setAttribute('uv', new THREE.Float32BufferAttribute([0, 0, (ex1 - ex0) / 2.6, 0, (ex1 - ex0) / 2.6, sl / 2.6, 0, sl / 2.6], 2));
      slope.setIndex([0, 2, 1, 0, 3, 2]); slope.computeVertexNormals();
      this.put(g, slope, M.teja, 0, 0, 0);
      const ends = [];
      for (const [ex, sg] of [[ex0 + 0.3, -1], [ex1 - 0.3, 1]]) {
        const tri = new THREE.BufferGeometry(); // (the triangle under the slope at this end)
        tri.setAttribute('position', new THREE.Float32BufferAttribute([ex, HS, zl - 0.3, ex, HS, zh, ex, yh, zh], 3));
        tri.setAttribute('uv', new THREE.Float32BufferAttribute([0, 0, 2, 0, 2, 0.5], 2));
        tri.setIndex(sg > 0 ? [0, 2, 1] : [0, 1, 2]); tri.computeVertexNormals(); ends.push(tri);
      }
      this.put(g, mergeGeos(ends), M.mamp, 0, 0, 0);
    }
    // west front: the great oculus over the main door (its leaves really open: churchdoors.js)
    const PS = STYLE.plastilina ? quoin : M.sillar; // (the portals' granite as the captures show it: the warm tone of the church's, not grey)
    const wP = westPortal(PS);
    wP.group.position.set(x0, 0, 0); wP.group.rotation.y = -Math.PI / 2; g.add(wP.group);
    {
      const og = new THREE.Group(); og.position.set(x0 - 0.02, 12.5, 0); og.rotation.y = -Math.PI / 2; g.add(og);
      const gl = new THREE.Mesh(new THREE.CircleGeometry(1.56, 40), M.glass); gl.position.z = 0.02; og.add(gl);
      const parts = [];
      for (const [r, t, zz] of [[1.62, 0.15, 0.08], [1.85, 0.12, 0.16], [2.04, 0.1, 0.09], [0.42, 0.07, 0.08]]) parts.push(new THREE.TorusGeometry(r, t, 8, 44).translate(0, 0, zz));
      for (let i = 0; i < 16; i++) { const sp = new THREE.BoxGeometry(0.07, 1.16, 0.08); sp.translate(0, 0.42 + 0.58, 0.06); sp.rotateZ((i / 16) * Math.PI * 2); parts.push(sp); } // a wheel of granite spokes
      for (let i = 0; i < 16; i++) { const a2 = ((i + 0.5) / 16) * Math.PI * 2, ar = new THREE.TorusGeometry(0.2, 0.035, 5, 10, Math.PI); ar.rotateZ(a2 - Math.PI / 2); ar.translate(Math.cos(a2) * 1.32, Math.sin(a2) * 1.32, 0.06); parts.push(ar); }
      const om = new THREE.Mesh(mergeGeos(parts), M.sillar); om.castShadow = true; og.add(om);
    }
    // the side portals, on the outline in the third bay: the Mediodía (open: its leaf stands ajar by day), the Gospel one
    const sideP = (hit, make) => {
      if (!hit || !hit.ok) return null;
      const P = make(PS, { room: 2.6 }); // (behind the door, the dark of the church)
      P.group.position.set(xs, 0, hit.v); P.group.rotation.y = Math.atan2(hit.nx, hit.nz);
      g.add(P.group);
      return P;
    };
    const sP = sideP(sHit, southPortal), nP = sideP(nHit, northPortal);
    // the tower, at the south-west corner: its body is the block's own, to the cornice (x −26.34 → −19.0, z 6.16 → 13.54);
    // over it the belfry, 5.7 m square, and over that the upper body, the pedestal, the stone spire with its ball and its
    // cross, 41.5 m in all (the photograph's; it was a 7.4 m shaft of stages under a dome of red tile, at 37 m)
    const tx = -22.6, tz = 9.6;
    const tw = 5.7, bellY = 26.0;
    this.put(g, sbox(tw, 9.2, tw, 3.2), M.mamp, tx, H + 4.6, tz);
    const tq = [];
    for (const sx of [-1, 1]) for (const sz of [-1, 1]) tq.push(sbox(0.8, 9.2, 0.8, 1.6).translate(tx + sx * (tw / 2 - 0.3), H + 4.6, tz + sz * (tw / 2 - 0.3)));
    tq.push(sbox(tw + 0.7, 0.45, tw + 0.7, 1.6).translate(tx, 31.2 + 0.0, tz));          // the belfry's cornice
    for (const sx of [-1, 1]) for (const sz of [-1, 1]) { tq.push(sbox(0.5, 0.3, 0.5, 1).translate(tx + sx * (tw / 2 + 0.1), 31.6, tz + sz * (tw / 2 + 0.1))); }
    this.put(g, mergeGeos(tq), quoin, 0, 0, 0);
    for (const sx of [-1, 1]) for (const sz of [-1, 1]) this.put(g, new THREE.SphereGeometry(0.3, 10, 8), M.sillar, tx + sx * (tw / 2 + 0.1), 32.0, tz + sz * (tw / 2 + 0.1));
    this.put(g, sbox(2.4, 4.05, 2.4, 3.2), M.sillar, tx, 31.45 + 2.025, tz);
    this.put(g, sbox(3.0, 0.3, 3.0, 1.6), quoin, tx, 35.5 + 0.1, tz);
    this.put(g, sbox(1.2, 1.65, 1.2, 1.6), quoin, tx, 35.75 + 0.825, tz);
    { const sp = new THREE.ConeGeometry(0.72, 2.0, 4, 1); sp.rotateY(Math.PI / 4); this.put(g, sp, M.sillar, tx, 37.4 + 1.0, tz); }
    this.put(g, new THREE.SphereGeometry(0.22, 10, 8), M.sillar, tx, 39.55, tz);
    this.put(g, sbox(0.1, 1.9, 0.1), M.iron, tx, 40.5, tz);
    this.put(g, sbox(0.8, 0.1, 0.1), M.iron, tx, 40.9, tz);
    this.put(g, sbox(0.5, 0.18, 0.05), M.iron, tx + 0.28, 41.4, tz); // (the vane)
    // the belfry's openings, two arches a face, and a small one a face in the upper body; the bells hang in the two nearer faces
    for (let side = 0; side < 4; side++) {
      const a = (side * Math.PI) / 2, d = tw / 2 + 0.02;
      for (const off of [-1.45, 1.45]) {
        const op = new THREE.Mesh(archPanel(1.4, 3.0), M.dark);
        op.position.set(tx + Math.sin(a) * d + Math.cos(a) * off, bellY, tz + Math.cos(a) * d - Math.sin(a) * off);
        op.rotation.y = a; g.add(op);
        if (side % 2 === 0) {
          const bell = new THREE.Mesh(new THREE.CylinderGeometry(0.35, 0.6, 1.0, 12, 1, true), M.bronze);
          bell.position.set(tx + Math.sin(a) * (d - 0.8) + Math.cos(a) * off, bellY + 1.7, tz + Math.cos(a) * (d - 0.8) - Math.sin(a) * off);
          g.add(bell);
          this.animated.push({ kind: 'bell', mesh: bell, phase: off });
        }
      }
      const op2 = new THREE.Mesh(archPanel(0.8, 1.6), M.dark), d2 = 1.2 + 0.02;
      op2.position.set(tx + Math.sin(a) * d2, 32.3, tz + Math.cos(a) * d2); op2.rotation.y = a; g.add(op2);
    }
    // stork nests on the belfry's cornice & the nave's ridge
    const F = makeFurnitureGeometries();
    const nestMat = new THREE.MeshStandardMaterial({ vertexColors: true, roughness: 1 });
    this.put(g, F.nido, nestMat, tx + 2.0, 31.45, tz - 2.0);
    this.put(g, F.nido, nestMat, xa - 2, H + 3.4, 0);
    const towerWorld = new THREE.Vector3(tx, 0, tz).applyMatrix4(g.matrixWorld);
    this.poi.churchTower = { x: towerWorld.x, z: towerWorld.z, top: 41 };
    // the church's frame and the measures taken from its outline, for the hyperreal model (hiper.js, tools/blender):
    // local x along the axis (east, towards the apse), local z across (south when south > 0), metres
    this.poi.churchFrame = { group: g, cx: ob.cx, cz: ob.cz, rotY: g.rotation.y, L, W, south, x0, xa, nw, xs, H, ring: ringLocal.slice(), portals: [] };
    const doorWorld = new THREE.Vector3(x0 - 6, 0, 0).applyMatrix4(g.matrixWorld);
    this.poi.churchDoor = { x: doorWorld.x, z: doorWorld.z };
    // the doors (the inside: church.js): the main one at the foot and the Mediodía one go in; the Gospel one is shut. For
    // each: its threshold on the facade (thr), the way out to the street (nx, nz), where to stand (x, z: a step out), a
    // point inside (f), its leaves (door)
    const toW = (lx, lz) => { const v = new THREE.Vector3(lx, 0, lz).applyMatrix4(g.matrixWorld); return { x: v.x, z: v.z }; };
    const dirW = (dx, dz) => { const a2 = toW(0, 0), b2 = toW(dx, dz); return { x: b2.x - a2.x, z: b2.z - a2.z }; };
    this.poi.churchPortal = toW(x0 + 0.4, 0);
    const doorPoi = (P, lx, lz, nlx, nlz) => {
      const thr = toW(lx, lz), n = dirW(nlx, nlz);
      return { x: thr.x + n.x * 1.1, z: thr.z + n.z * 1.1, f: toW(lx - nlx * 0.8, lz - nlz * 0.8), thr, nx: n.x, nz: n.z, door: P.door, half: P.w / 2 };
    };
    this.poi.churchWest = doorPoi(wP, x0, 0, -1, 0);
    if (sP) this.poi.churchSouth = doorPoi(sP, xs, sHit.v, sHit.nx, sHit.nz);
    if (nP) this.poi.churchNorth = doorPoi(nP, xs, nHit.v, nHit.nx, nHit.nz);
    // the portals' pedestals stand out into the street: you walk round them (the west portal's first: hiper.js may
    // resize that portal, and its pedestals with it)
    this.poi.churchFrame.westPosts = { from: (this.circleColliders || []).length, n: wP.posts.length, origin: toW(x0, 0) };
    for (const [P, lx, lz] of [[wP, x0, 0], [sP, xs, sHit && sHit.v], [nP, xs, nHit && nHit.v]]) {
      if (!P) continue;
      const ry = P.group.rotation.y, c = Math.cos(ry), s2 = Math.sin(ry);
      for (const [px, pz, pr] of P.posts) { const q = toW(lx + px * c + pz * s2, lz - px * s2 + pz * c); this.circle(q.x, q.z, pr, 3); }
    }
    this.churchDoors = [wP.door, sP && sP.door, nP && nP.door].filter(Boolean);
    this.poi.churchFrame.portals = [wP.group, sP && sP.group, nP && nP.group].filter(Boolean);
    this.storkSpots = [new THREE.Vector3(tx + 2.0, 31.95, tz - 2.0).applyMatrix4(g.matrixWorld), new THREE.Vector3(xa - 2, H + 3.9, 0).applyMatrix4(g.matrixWorld)];
    // collider: full footprint is already claimed
  }

  // ================================================================ Ayuntamiento (Plaza de España 1)
  ayuntamiento([x, z]) {
    const b = this.building(x, z) || this.building(x, z + 5);
    if (!b) return;
    this.claim(b);
    const M = this.mat;
    // facade edge: the one facing the plaza (south)
    const plaza = this.map.areas.find((a) => a.name === 'Plaza de España');
    const pc = plaza ? ringCentroid(plaza.ring) : [x, z + 30];
    this.poi.plaza = { x: pc[0], z: pc[1] };
    const r = b.ring;
    let best = null;
    for (let i = 0; i < r.length; i += 2) {
      const j = (i + 2) % r.length;
      const ax = r[i], az = r[i + 1], bx = r[j], bz = r[j + 1];
      const L = Math.hypot(bx - ax, bz - az);
      if (L < 8) continue;
      const nx = (bz - az) / L, nz = -(bx - ax) / L;
      const mx = (ax + bx) / 2, mz = (az + bz) / 2;
      const toP = (pc[0] - mx) * nx + (pc[1] - mz) * nz;
      const score = toP / Math.hypot(pc[0] - mx, pc[1] - mz) + L * 0.01;
      if (!best || score > best.score) best = { score, i, j, ax, az, bx, bz, L, nx, nz, mx, mz };
    }
    const Hb = 11.5;
    if (!best) { this.add(extrudeRing(r, 0, Hb, 2.4, true), M.sillar, 0, 0, 0); return; }
    const { L, nx, nz, mx, mz } = best;
    const f = new THREE.Group();
    f.position.set(mx + nx * 0.02, 0, mz + nz * 0.02);
    f.rotation.y = Math.atan2(nx, nz); // local +z = outward normal, local +x along the front
    this.root.add(f); f.updateMatrixWorld(true);
    const W = (x, z) => { const v = f.localToWorld(new THREE.Vector3(x, 0, z)); return [v.x, v.z]; };
    // its front as its photograph shows it (2026-10-13): seven bays, symmetrical about the clock — below, three round
    // arches of the arcade (soportal) alternating with four square-headed openings framed in granite, one on each pier
    // and one at each end; above, a balcony running across the three middle bays, a blind recessed panel with a lantern
    // over each side arch and a balcony of its own at each end; a heavy moulded cornice, a parapet with a granite ball
    // over each bay (two at the corners), and in the middle an attic with the clock between volutes, crowned by a
    // broken curved pediment and a pinnacle, a flame-urn either side
    const FW = Math.min(L - 0.6, 23);
    const k = FW / 23, A = 6.7 * k, P = 3.35 * k, E = 10.05 * k; // (bay centres: arches 0, ±A; piers ±P; ends ±E)
    const aw = 3.3 * k, ah = 5.0;
    // ---- the arcade you walk into (the user, 2026-10-13: «dentro de los arcos se puede pasear… la entrada al edificio
    // está debajo de los arcos»): behind the front wall, a gallery the whole width of the arcade, its ceiling at the
    // string course, its floor of granite, and at its back the town hall's own door. The body below is the footprint
    // with the gallery cut out of it; above, the whole footprint. The front wall a slab with its arches and its four
    // square-headed openings cut through it — you can walk in by any of them.
    const HG = 5.6, TW = 0.6, D = 4.2, GX = FW / 2 - 0.6; // (ceiling, front wall's thickness, depth to the back wall, half width)
    const sideA = (f.worldToLocal(new THREE.Vector3(best.ax, 0, best.az)).x > 0 ? 1 : -1);
    // its end towards Calle Túnel (the 2009 captures 05 and 06): the gallery does not stop at a wall there but opens onto
    // the street by a big round arch as deep as itself, in the side wall of the corner where the front begins (in this
    // footprint's order, its east side) — found where that wall reaches the gallery's back
    let open = null;
    if (best.j > best.i && best.i >= 2) {
      const qx = r[best.i - 2], qz = r[best.i - 1];
      const a = f.worldToLocal(new THREE.Vector3(qx, 0, qz)), c = f.worldToLocal(new THREE.Vector3(best.ax, 0, best.az));
      const t = (-D - c.z) / (a.z - c.z);
      if (t > 0 && t < 1) open = { pe: [best.ax + (qx - best.ax) * t, best.az + (qz - best.az) * t], xs: Math.abs(c.x + ((a.x - c.x) * (-D / 2 - c.z)) / (a.z - c.z)), qx, qz };
    }
    const notch = [W(sideA * GX, 0), W(sideA * GX, -D), W(-sideA * GX, -D), W(-sideA * GX, 0)].flat();
    const ringG = open ? [...r.slice(0, best.i), ...open.pe, ...W(-sideA * GX, -D), ...W(-sideA * GX, 0), ...r.slice(best.j)]
      : best.j > best.i ? [...r.slice(0, best.i + 2), ...notch, ...r.slice(best.j)] : [...r, ...notch];
    // (its front of granite, as the 2026 photograph shows it; its sides and back lime-washed, the joints barely marked,
    // as the 2009 captures do: the walls on the front or round the gallery in granite, the rest in render)
    const facing = (want) => (i, ax, az, bx, bz) => ((f.worldToLocal(new THREE.Vector3((ax + bx) / 2, 0, (az + bz) / 2)).z > -D - 0.1) === want ? null : 'skip');
    this.add(extrudeRing(ringG, 0, HG, 2.4, false, facing(true)), M.sillar, 0, 0, 0);
    this.add(extrudeRing(ringG, 0, HG, 2.4, false, facing(false)), M.revoco, 0, 0, 0);
    this.add(extrudeRing(r, HG, Hb, 2.4, true, facing(true)), M.sillar, 0, 0, 0);
    this.add(extrudeRing(r, HG, Hb, 2.4, false, facing(false)), M.revoco, 0, 0, 0);
    const col = this.colliders.find((c) => c.ring === b.ring);
    if (col) col.ring = ringG; // (what stops you: the body without its gallery…)
    const holes = [...[-A, 0, A].map((cx) => ({ cx, w: aw, arch: true })), ...[-E, -P, P, E].map((cx) => ({ cx, w: 1.1, h: 2.6 }))].sort((p, q) => p.cx - q.cx);
    // (the front wall runs to the corner on the open side: its end is the corner pier)
    const xL = open && sideA < 0 ? -open.xs : -FW / 2, xR = open && sideA > 0 ? open.xs : FW / 2;
    const sh = new THREE.Shape(); sh.moveTo(xL, 0);
    for (const o of holes) {
      const x0 = o.cx - o.w / 2, x1 = o.cx + o.w / 2;
      sh.lineTo(x0, 0);
      if (o.arch) { sh.lineTo(x0, ah - o.w / 2); sh.absarc(o.cx, ah - o.w / 2, o.w / 2, Math.PI, 0, true); }
      else { sh.lineTo(x0, o.h); sh.lineTo(x1, o.h); }
      sh.lineTo(x1, 0);
    }
    sh.lineTo(xR, 0); sh.lineTo(xR, HG); sh.lineTo(xL, HG); sh.closePath();
    const fw = new THREE.ExtrudeGeometry(sh, { depth: TW, bevelEnabled: false, curveSegments: 18 });
    const fuv = fw.attributes.uv; for (let q = 0; q < fuv.count; q++) fuv.setXY(q, fuv.getX(q) / 2.4, fuv.getY(q) / 2.4);
    const front = new THREE.Mesh(fw, M.sillar); front.position.z = -TW; front.castShadow = true; front.receiveShadow = true; f.add(front);
    // (…and its front wall between the openings: a pier at a time)
    let px = xL;
    for (const o of [...holes, { cx: xR, w: 0 }]) {
      const x0 = o.cx - o.w / 2;
      if (x0 - px > 0.05) this.colliders.push({ ring: [W(px, 0), W(x0, 0), W(x0, -TW), W(px, -TW)].flat(), h: 6 });
      px = o.cx + o.w / 2;
    }
    // the gallery: its coffered ceiling, its granite floor, its lanterns hung from the arches' keys
    const g0 = open && sideA < 0 ? TW - open.xs : -GX, g1 = open && sideA > 0 ? open.xs - TW : GX; // (its ends: to the side wall where open)
    const ceil = new THREE.Mesh(new THREE.PlaneGeometry(g1 - g0, D - TW), M.cal); ceil.rotation.x = Math.PI / 2; ceil.position.set((g0 + g1) / 2, HG - 0.01, -(D + TW) / 2); f.add(ceil);
    for (let bx2 = g0 + 1.6; bx2 < g1 - 0.5; bx2 += 3.2) f.add(at(new THREE.Mesh(sbox(0.3, 0.28, D - TW, 1), M.sillar), bx2, HG - 0.14, -(D + TW) / 2));
    const floor = new THREE.Mesh(new THREE.PlaneGeometry(g1 - g0, D), M.sillar); floor.rotation.x = -Math.PI / 2; floor.position.set((g0 + g1) / 2, 0.03, -D / 2); floor.receiveShadow = true; f.add(floor);
    // the side wall where the gallery opens: a slab with its round arch (3.1 m wide, its key at 4.75 m, as capture 06
    // measures it), a plain moulding round it and the impost band at its springing; above, as over the front's side
    // arches, a blind panel with its lantern; the string course carried round; further back, two narrow windows one over
    // the other, the lower one grilled
    if (open) {
      const sx = best.ax, sz = best.az, Ls = Math.hypot(open.qx - sx, open.qz - sz);
      const ux = (open.qx - sx) / Ls, uz = (open.qz - sz) / Ls, onx = -uz, onz = ux; // (along it from the front corner; out)
      const e = new THREE.Group();
      e.position.set(sx + onx * 0.02, 0, sz + onz * 0.02);
      e.rotation.y = Math.atan2(onx, onz); // local +z = out of the wall, local +x = back along it from the front corner
      this.root.add(e); e.updateMatrixWorld(true);
      const We = (x, z) => { const v = e.localToWorld(new THREE.Vector3(x, 0, z)); return [v.x, v.z]; };
      const De = Math.hypot(open.pe[0] - sx, open.pe[1] - sz), sc = (TW + De) / 2, sw = 3.1, sk = 4.75, ssp = sk - sw / 2;
      const ss = new THREE.Shape(); ss.moveTo(TW, 0);
      ss.lineTo(sc - sw / 2, 0); ss.lineTo(sc - sw / 2, ssp); ss.absarc(sc, ssp, sw / 2, Math.PI, 0, true); ss.lineTo(sc + sw / 2, 0);
      ss.lineTo(De, 0); ss.lineTo(De, HG); ss.lineTo(TW, HG); ss.closePath();
      const sg = new THREE.ExtrudeGeometry(ss, { depth: TW, bevelEnabled: false, curveSegments: 18 });
      const suv = sg.attributes.uv; for (let q = 0; q < suv.count; q++) suv.setXY(q, suv.getX(q) / 2.4, suv.getY(q) / 2.4);
      const side = new THREE.Mesh(sg, M.revoco); side.position.z = -TW; side.castShadow = true; side.receiveShadow = true; e.add(side);
      for (const [p0, p1] of [[TW, sc - sw / 2], [sc + sw / 2, De]]) if (p1 - p0 > 0.05) this.colliders.push({ ring: [We(p0, 0), We(p1, 0), We(p1, -TW), We(p0, -TW)].flat(), h: 6 });
      e.add(at(new THREE.Mesh(archRing(sw / 2, 0.22, 0.16), M.revoco), sc, ssp, 0.06));
      for (const [p0, p1] of [[0, sc - sw / 2 - 0.22], [sc + sw / 2 + 0.22, Ls - 0.3]]) e.add(at(new THREE.Mesh(sbox(p1 - p0, 0.2, 0.12, 1), M.revoco), (p0 + p1) / 2, ssp, 0.04));
      e.add(at(new THREE.Mesh(sbox(Ls, 0.45, 0.3, 1.6), M.revoco), Ls / 2, 5.9, 0.1));
      e.add(at(new THREE.Mesh(sbox(1.9, 2.6, 0.12, 1), M.revoco), sc, 7.9, -0.04));
      e.add(at(new THREE.Mesh(new THREE.BoxGeometry(0.26, 0.4, 0.26), M.iron), sc, 9.0, 0.45));
      e.add(at(new THREE.Mesh(new THREE.BoxGeometry(0.05, 0.05, 0.45), M.iron), sc, 9.25, 0.22));
      for (const [y0, y1, grille] of [[1.0, 2.9, true], [6.6, 8.4, false]]) {
        const wx = Math.min(9.0, Ls - 1.2), hh2 = y1 - y0;
        e.add(at(new THREE.Mesh(new THREE.PlaneGeometry(0.7, hh2), M.glass), wx, (y0 + y1) / 2, 0.03));
        e.add(at(new THREE.Mesh(sbox(0.9, 0.12, 0.16, 1), M.revoco), wx, y0 - 0.06, 0.06));
        if (grille) for (let q = 0; q < 5; q++) e.add(at(new THREE.Mesh(new THREE.BoxGeometry(0.025, hh2, 0.025), M.iron), wx - 0.28 + q * 0.14, (y0 + y1) / 2, 0.1));
      }
      // just past the arch, the tall barred window the 2009 capture 93 shows from the mouth of the Túnel (its columns 490–555:
      // 4.0 to 5.3 m along the wall from the corner, from the pavement to ≈ 3.9 m): a grille of bars in a frame, the sill on a block
      { const wx2 = De + 0.75, ww = 1.15, wy0 = 0.35, wy1 = 3.85, wh = wy1 - wy0;
        e.add(at(new THREE.Mesh(new THREE.PlaneGeometry(ww, wh), M.glass), wx2, (wy0 + wy1) / 2, 0.03));
        e.add(at(new THREE.Mesh(mergeGeos([sbox(ww + 0.3, 0.14, 0.2, 1).translate(0, -0.07, 0.04), sbox(0.14, wh, 0.12, 1).translate(-ww / 2 - 0.07, wh / 2, 0.03), sbox(0.14, wh, 0.12, 1).translate(ww / 2 + 0.07, wh / 2, 0.03), sbox(ww + 0.3, 0.14, 0.14, 1).translate(0, wh + 0.07, 0.03)]), M.revoco), wx2, wy0, 0));
        for (let q = 0; q <= 8; q++) e.add(at(new THREE.Mesh(new THREE.BoxGeometry(0.025, wh, 0.025), M.iron), wx2 - ww / 2 + 0.07 + (q * (ww - 0.14)) / 8, (wy0 + wy1) / 2, 0.1));
        for (const fy of [0.3, 0.62]) e.add(at(new THREE.Mesh(new THREE.BoxGeometry(ww, 0.025, 0.025), M.iron), wx2, wy0 + wh * fy, 0.1));
      }
      // the cornice along the whole side, as the capture shows it (a moulded course on corbels, its columns 600–750 to the top):
      // the front's, 0.95 m out, carried back to the far corner
      { const cn = [sbox(Ls, 0.7, 1.2, 1.6).translate(Ls / 2, Hb - 0.2, 0.35)];
        for (let q = 0.5; q < Ls - 0.3; q += 0.9) cn.push(sbox(0.3, 0.32, 0.7, 1).translate(q, Hb - 0.72, 0.38));
        const cm = new THREE.Mesh(mergeGeos(cn), M.sillar); cm.castShadow = true; cm.receiveShadow = true; e.add(cm); }
    }
    // the back wall's openings: the town hall's own door behind the middle arch — two leaves of dark wood in a granite
    // frame with its lintel and cornice — and a door either side, behind the side arches, and grilled windows
    const doorAt = (cx, w, h, main) => {
      const dz = -D + 0.03;
      for (const sd of [-1, 1]) {
        const leaf = new THREE.Mesh(new THREE.PlaneGeometry(w / 2 - 0.02, h), M.wood); leaf.position.set(cx + sd * (w / 4), h / 2, dz); f.add(leaf);
        for (let q = 0; q < 3; q++) f.add(at(new THREE.Mesh(new THREE.BoxGeometry(w / 2 - 0.25, h / 3 - 0.25, 0.04), M.wood), cx + sd * (w / 4), h / 6 + (q * h) / 3, dz + 0.03)); // (its panels)
        f.add(at(new THREE.Mesh(sbox(0.32, h + 0.3, 0.2, 1), M.sillar), cx + sd * (w / 2 + 0.16), (h + 0.3) / 2, dz + 0.08));
      }
      f.add(at(new THREE.Mesh(sbox(w + 0.64, 0.38, 0.24, 1), M.sillar), cx, h + 0.3 + 0.19, dz + 0.1));
      if (main) f.add(at(new THREE.Mesh(sbox(w + 1.0, 0.18, 0.4, 1), M.sillar), cx, h + 0.95, dz + 0.18));
    };
    doorAt(0, 2.1, 3.3, true);
    for (const cx of [-A, A]) doorAt(cx, 1.3, 2.6, false);
    for (const cx of [-P, P, -E, E]) {
      const win = new THREE.Mesh(new THREE.PlaneGeometry(1.0, 1.5), M.glass); win.position.set(cx, 1.9, -D + 0.03); f.add(win);
      for (let q = 0; q < 6; q++) f.add(at(new THREE.Mesh(new THREE.BoxGeometry(0.025, 1.5, 0.025), M.iron), cx - 0.45 + q * 0.18, 1.9, -D + 0.1));
    }
    for (const cx of [-A, 0, A]) {
      const ring = new THREE.Mesh(archRing(aw / 2, 0.35, 0.5), M.sillar); ring.position.set(cx, ah - aw / 2, 0.25); f.add(ring);
      const lamp = new THREE.Mesh(new THREE.BoxGeometry(0.28, 0.42, 0.28), M.iron); lamp.position.set(cx, ah - 0.75, -TW / 2); f.add(lamp);
      f.add(at(new THREE.Mesh(new THREE.BoxGeometry(0.03, 0.3, 0.03), M.iron), cx, ah - 0.4, -TW / 2));
      const lp = W(cx, -TW / 2); this.world.lampPoints && this.world.lampPoints.push(lp[0], ah - 0.8, lp[1]);
    }
    // Tuscan pilasters either side of each arch, and the square-headed openings between them and at the ends
    for (const cx of [-A, 0, A]) for (const sd of [-1, 1]) f.add(at(new THREE.Mesh(sbox(0.45, 5.6, 0.45, 1.2), M.sillar), cx + sd * (aw / 2 + 0.28), 2.8, 0.25));
    for (const cx of [-E, -P, P, E]) {
      for (const sd of [-1, 1]) f.add(at(new THREE.Mesh(sbox(0.22, 2.6, 0.2, 1), M.sillar), cx + sd * 0.66, 1.6, 0.1));
      f.add(at(new THREE.Mesh(sbox(1.55, 0.25, 0.22, 1), M.sillar), cx, 2.95, 0.11));
    }
    f.add(at(new THREE.Mesh(sbox(FW, 0.1, 0.6, 1.6), M.sillar), 0, 0.05, 0.3)); // (the granite step along the arcade, low: you walk over it)
    f.add(at(new THREE.Mesh(sbox(FW, 0.6, 0.7, 1.6), M.sillar), 0, 5.9, 0.3));
    // upper floor (its balcony doors dark in their granite frames, no shutters: the 2026 photograph)
    const door = (cx) => {
      const op = new THREE.Mesh(new THREE.PlaneGeometry(1.3, 2.6), M.glass); op.position.set(cx, 7.9, 0.03); f.add(op);
      for (const sd of [-1, 1]) f.add(at(new THREE.Mesh(sbox(0.22, 2.75, 0.16, 1), M.sillar), cx + sd * 0.76, 7.95, 0.08));
      f.add(at(new THREE.Mesh(sbox(1.9, 0.3, 0.3, 1), M.sillar), cx, 9.35, 0.15)); // (its moulded hood)
    };
    const railing = (cx, w) => {
      f.add(at(new THREE.Mesh(sbox(w, 0.25, 1.0, 1), M.sillar), cx, 6.55, 0.5));
      for (let x = -w / 2 + 0.05; x <= w / 2 - 0.04; x += 0.2) f.add(at(new THREE.Mesh(new THREE.BoxGeometry(0.03, 1.0, 0.03), M.iron), cx + x, 7.15, 0.95));
      f.add(at(new THREE.Mesh(new THREE.BoxGeometry(w, 0.06, 0.06), M.iron), cx, 7.65, 0.95));
    };
    for (const cx of [-P, 0, P]) door(cx);
    railing(0, 2 * P + 2.2);
    for (const cx of [-E, E]) { door(cx); railing(cx, 2.0); }
    for (const cx of [-A, A]) {
      const pan = new THREE.Mesh(sbox(1.9, 2.6, 0.12, 1), M.sillar); pan.position.set(cx, 7.9, -0.04); f.add(pan); // (the blind panel, set in)
      const lan = new THREE.Mesh(new THREE.BoxGeometry(0.26, 0.4, 0.26), M.iron); lan.position.set(cx, 9.0, 0.45); f.add(lan);
      f.add(at(new THREE.Mesh(new THREE.BoxGeometry(0.05, 0.05, 0.45), M.iron), cx, 9.25, 0.22));
    }
    // cornice and parapet, a ball over each bay and two at each corner
    f.add(at(new THREE.Mesh(sbox(FW + 0.8, 0.7, 1.2, 1.6), M.sillar), 0, Hb - 0.2, 0.35));
    f.add(at(new THREE.Mesh(sbox(FW, 0.75, 0.45, 1.6), M.sillar), 0, Hb + 0.52, 0.2));
    for (const cx of [-E, -A, -P, P, A, E, -FW / 2 + 0.3, FW / 2 - 0.3]) {
      f.add(at(new THREE.Mesh(sbox(0.55, 0.9, 0.55, 1), M.sillar), cx, Hb + 0.6, 0.3));
      f.add(at(new THREE.Mesh(new THREE.SphereGeometry(0.27, 10, 8), M.sillar), cx, Hb + 1.32, 0.3));
    }
    // the coat of arms over the middle window, crowned, under the clock
    const arms = new THREE.Mesh(new THREE.PlaneGeometry(1.4, 1.4), new THREE.MeshStandardMaterial({ map: canvasTex(stoneCanvas('escudo', 256)), transparent: true, roughness: 0.6 }));
    arms.position.set(0, Hb - 1.05, 0.98); f.add(arms);
    // the attic with the clock: between two volutes, a broken curved pediment and its pinnacle; a flame-urn either side
    f.add(at(new THREE.Mesh(sbox(3.0, 2.9, 0.7, 1.6), M.sillar), 0, Hb + 1.45 + 0.9, 0.15));
    for (const sd of [-1, 1]) {
      const vol = new THREE.Mesh(new THREE.CylinderGeometry(0.75, 0.75, 0.6, 14, 1, false, sd > 0 ? 0 : Math.PI / 2, Math.PI / 2), M.sillar);
      vol.rotation.x = Math.PI / 2; vol.position.set(sd * 1.5, Hb + 0.9, 0.15); f.add(vol);
      const half = new THREE.Mesh(archRing(1.1, 0.24, 0.7, 10), M.sillar); half.position.set(sd * 0.22, Hb + 3.4, 0.15); half.scale.set(1, 0.75, 1); f.add(half);
      f.add(at(new THREE.Mesh(sbox(0.5, 0.7, 0.5, 1), M.sillar), sd * 2.2, Hb + 1.25, 0.2));
      const urn = new THREE.Mesh(new THREE.ConeGeometry(0.22, 0.9, 8), M.sillar); urn.position.set(sd * 2.2, Hb + 2.05, 0.2); f.add(urn);
    }
    const pin = new THREE.Mesh(new THREE.ConeGeometry(0.2, 1.2, 8), M.sillar); pin.position.set(0, Hb + 4.55, 0.15); f.add(pin);
    f.add(at(new THREE.Mesh(new THREE.SphereGeometry(0.16, 8, 6), M.sillar), 0, Hb + 5.2, 0.15));
    const clock = new THREE.Mesh(new THREE.CircleGeometry(0.55, 24), new THREE.MeshStandardMaterial({ map: canvasTex(stoneCanvas('reloj', 256)), roughness: 0.4 }));
    clock.position.set(0, Hb + 2.45, 0.51); f.add(clock);
    const hh = new THREE.Mesh(new THREE.BoxGeometry(0.05, 0.3, 0.02), M.iron); hh.geometry.translate(0, 0.13, 0); hh.position.set(0, Hb + 2.45, 0.53); f.add(hh);
    const mh = new THREE.Mesh(new THREE.BoxGeometry(0.035, 0.45, 0.02), M.iron); mh.geometry.translate(0, 0.21, 0); mh.position.set(0, Hb + 2.45, 0.54); f.add(mh);
    this.animated.push({ kind: 'clock', hh, mh });
    // flags on the balcony: four, on slanting poles ≈ 2.8 m apart (the 2026 photograph and the 2009 capture 05 count four), from the
    // west: the town's, Extremadura, Spain, the EU. The town's is not in textures.js: a hanging cloth of crimson over navy, as the
    // photograph's first flag reads (its colours sampled; its arms, if it has any, are not seen)
    const muniFlag = () => {
      const c = document.createElement('canvas'); c.width = 192; c.height = 128;
      const x = c.getContext('2d'); x.fillStyle = '#a3243c'; x.fillRect(0, 0, 192, 52); x.fillStyle = '#1b3d7d'; x.fillRect(0, 52, 192, 76);
      return c;
    };
    ['mu', 'ex', 'es', 'eu'].forEach((k, i) => {
      const fx = -4.2 + i * 2.8;
      const pole = new THREE.Mesh(new THREE.CylinderGeometry(0.03, 0.03, 2.4, 6), M.iron);
      pole.position.set(fx, 8.5, 1.3); pole.rotation.x = 0.6; f.add(pole);
      const fg = new THREE.PlaneGeometry(1.35, 0.9, 12, 4);
      fg.translate(0.675, -0.45, 0);
      const fm = new THREE.MeshStandardMaterial({ map: canvasTex(k === 'mu' ? muniFlag() : flagCanvas(k)), side: THREE.DoubleSide, roughness: 0.8 });
      const flag = new THREE.Mesh(fg, fm);
      flag.position.set(fx, 9.45, 1.95); f.add(flag);
      this.flags.push({ mesh: flag, base: fg.attributes.position.array.slice(), phase: i });
    });
    // sign
    const s = new THREE.Mesh(new THREE.PlaneGeometry(0.9, 0.9), new THREE.MeshStandardMaterial({ map: canvasTex(aytoPlaque()), roughness: 0.5, side: THREE.DoubleSide })); s.position.set(-E, 4.1, 0.05); f.add(s); // (over the end opening)
    this.poi.ayto = { x: mx + nx * 4, z: mz + nz * 4, nx, nz, front: { mx, mz, ux: -nz, uz: nx, half: FW / 2 + 1 } };
    // in through its own door, at the back of the arcade (venues.js: the hall, the stairs, the Salón de Plenos)
    const dIn = W(0, -D + 1.2), dBack = W(0, -D - 3);
    (this.poi.venues || (this.poi.venues = [])).push({ kind: 'ayto', name: 'Ayuntamiento de Guareña', sub: 'Casa Consistorial · Plaza de España', x: dIn[0], z: dIn[1], fx: dBack[0], fz: dBack[1], seed: 9 });
  }

  // ================================================================ Iglesia de San Gregorio (Plaza de San Gregorio)
  sanGregorio([x, z]) {
    const b = this.building(x, z);
    if (!b) return;
    this.claim(b);
    const small = this.building(238.9, 29.4);
    if (small && small !== b) this.claim(small);
    const M = this.mat;
    const ob = orientedRect(b.ring);
    let ux = Math.cos(ob.ang), uz = Math.sin(ob.ang), L = ob.hw, W = ob.hd;
    if (W > L) { [L, W] = [W, L]; [ux, uz] = [-uz, ux]; }
    if (ux < 0) { ux = -ux; uz = -uz; }
    const g = this.frame(ob.cx, ob.cz, ux, uz);
    const H = 8.8;
    this.put(g, sbox(L * 2, H, W * 2, 3), M.cal, 0, H / 2, 0);
    // granite plinth & corners
    this.put(g, sbox(L * 2 + 0.1, 1.0, W * 2 + 0.1, 1.6), M.sillar, 0, 0.5, 0);
    for (const sx of [-1, 1]) for (const sz of [-1, 1]) this.put(g, sbox(0.7, H, 0.7, 1.6), M.sillar, sx * (L - 0.3), H / 2, sz * (W - 0.3));
    this.put(g, gableRoof(L * 2, W * 2, 3.2, 0.35), M.teja, 0, H, 0);
    this.put(g, gableEnd(W * 2, 3.2), M.cal, L + 0.02, H, 0, Math.PI / 2);
    // west facade (towards the plaza): bell-gable with baroque scrolls + portal
    const fx = -L - 0.02;
    this.put(g, gableEnd(W * 2, 3.2), M.cal, fx, H, 0, -Math.PI / 2);
    const esp = this.put(g, sbox(0.7, 4.2, 4.2, 1.6), M.sillar, fx + 0.3, H + 3.3, 0);
    for (const s of [-1, 1]) {
      const scroll = new THREE.Mesh(new THREE.TorusGeometry(0.7, 0.22, 6, 12, Math.PI), M.sillar);
      scroll.position.set(fx + 0.3, H + 1.9, s * 2.5); scroll.rotation.y = Math.PI / 2; scroll.rotation.z = s > 0 ? 0 : Math.PI;
      g.add(scroll);
    }
    const eh = new THREE.Mesh(archPanel(1.4, 2.2), M.dark); eh.position.set(fx - 0.07, H + 2.2, 0); eh.rotation.y = -Math.PI / 2; g.add(eh);
    const bell = new THREE.Mesh(new THREE.CylinderGeometry(0.25, 0.45, 0.7, 10, 1, true), M.bronze); bell.position.set(fx + 0.3, H + 3.4, 0); g.add(bell);
    this.put(g, new THREE.SphereGeometry(0.3, 8, 6), M.sillar, fx + 0.3, H + 5.7, 0);
    this.put(g, sbox(0.08, 1.1, 0.08), M.iron, fx + 0.3, H + 6.4, 0);
    this.put(g, sbox(0.08, 0.08, 0.6), M.iron, fx + 0.3, H + 6.6, 0);
    // porch: three arches on granite columns
    const porch = new THREE.Group();
    porch.position.set(fx - 3.2, 0, 0);
    porch.rotation.y = -Math.PI / 2;
    g.add(porch);
    for (let k = -1; k <= 1; k++) {
      const ar = new THREE.Mesh(archRing(1.35, 0.3, 0.5), M.sillar); ar.position.set(k * 3.1, 3.4, 0); porch.add(ar);
    }
    for (let k = -2; k <= 1; k++) {
      const col = new THREE.Mesh(new THREE.CylinderGeometry(0.22, 0.25, 3.4, 12), M.sillar); col.position.set((k + 0.5) * 3.1, 1.7, 0); porch.add(col);
    }
    const pb = new THREE.Mesh(sbox(10, 1.1, 0.55, 1.6), M.cal); pb.position.set(0, 5.35, 0); porch.add(pb);
    const pr = new THREE.Mesh(sbox(10.2, 0.2, 3.6, 2.6), M.teja); pr.position.set(0, 6.0, -1.6); pr.rotation.x = 0.28; porch.add(pr);
    const door = new THREE.Mesh(new THREE.PlaneGeometry(2.4, 4.2), M.wood); door.position.set(fx - 0.04, 2.1, 0); door.rotation.y = -Math.PI / 2; g.add(door);
    // lantern dome over the east part
    this.put(g, new THREE.CylinderGeometry(3.0, 3.0, 2.4, 8), M.cal, L * 0.45, H + 2.2, 0);
    this.put(g, new THREE.SphereGeometry(3.05, 16, 8, 0, Math.PI * 2, 0, Math.PI / 2), M.teja, L * 0.45, H + 3.4, 0);
    this.put(g, new THREE.CylinderGeometry(0.7, 0.7, 1.4, 8), M.cal, L * 0.45, H + 6.8, 0);
    this.put(g, new THREE.ConeGeometry(0.9, 0.9, 8), M.teja, L * 0.45, H + 7.9, 0);
    for (let k = 0; k < 8; k++) {
      const a = (k / 8) * Math.PI * 2;
      const w = new THREE.Mesh(new THREE.PlaneGeometry(0.6, 1.1), M.glass);
      w.position.set(L * 0.45 + Math.cos(a) * 3.02, H + 2.2, Math.sin(a) * 3.02); w.rotation.y = -a + Math.PI / 2; g.add(w);
    }
    // columns collide
    for (let k = -2; k <= 1; k++) {
      const p = new THREE.Vector3(fx - 3.2, 0, (k + 0.5) * 3.1).applyMatrix4(g.matrixWorld);
      this.circle(p.x, p.z, 0.3, 4);
    }
    const front = new THREE.Vector3(fx - 8, 0, 0).applyMatrix4(g.matrixWorld);
    this.poi.sanGregorio = { x: front.x, z: front.z };
    // in by the west door, under the porch (venues.js: the nave, the dome, the retablo of San Gregorio)
    { g.updateMatrixWorld(true); const out = new THREE.Vector3(fx - 1.0, 0, 0).applyMatrix4(g.matrixWorld), inn = new THREE.Vector3(fx + 3, 0, 0).applyMatrix4(g.matrixWorld), l = Math.hypot(out.x - inn.x, out.z - inn.z) || 1;
      (this.poi.venues || (this.poi.venues = [])).push({ kind: 'sangregorio', name: 'Iglesia de San Gregorio', sub: 'Plaza de San Gregorio', x: out.x, z: out.z, fx: inn.x, fz: inn.z, seed: 13, nx: (out.x - inn.x) / l, nz: (out.z - inn.z) / l }); }
    // bust of Juan Durán Palomares facing the church + Tarteso centre totem
    this.poi.bustDuran = { x: front.x - 1, z: front.z, face: Math.atan2(ob.cx - front.x, ob.cz - front.z) };
    const totem = new THREE.Group();
    const tt = new THREE.Mesh(sbox(1.2, 2.4, 0.25, 1), new THREE.MeshStandardMaterial({ color: 0x2b2a28, roughness: 0.6 }));
    tt.position.y = 1.2; totem.add(tt);
    const label = new THREE.Mesh(new THREE.PlaneGeometry(1.1, 2.0), new THREE.MeshStandardMaterial({ map: canvasTex(this.tartesoCanvas()), roughness: 0.6 }));
    label.position.set(0, 1.3, 0.13); totem.add(label);
    const tp = new THREE.Vector3(fx - 6, 0, W + 2.5).applyMatrix4(g.matrixWorld);
    totem.position.set(tp.x, 0, tp.z);
    totem.rotation.y = Math.atan2(-ux, -uz);
    this.root.add(totem);
    this.circle(tp.x, tp.z, 0.6, 2.4);
  }
  tartesoCanvas() {
    const c = document.createElement('canvas'); c.width = 256; c.height = 470;
    const x = c.getContext('2d');
    x.fillStyle = '#2b2a28'; x.fillRect(0, 0, 256, 470);
    x.fillStyle = '#c9a44c'; x.fillRect(20, 20, 216, 6);
    x.font = 'bold 30px Georgia, serif'; x.textAlign = 'center';
    x.fillText('TARTESO', 128, 80);
    x.font = '18px Arial'; x.fillStyle = '#e8e2d0';
    ['Centro de', 'Interpretación', 'de la cultura', 'tartésica', '', 'El Turuñuelo', 'Guareña'].forEach((t, i) => x.fillText(t, 128, 130 + i * 30));
    // stylised face (Turuñuelo busts)
    x.strokeStyle = '#c9a44c'; x.lineWidth = 4;
    x.beginPath(); x.ellipse(128, 390, 34, 44, 0, 0, Math.PI * 2); x.stroke();
    x.beginPath(); x.arc(114, 382, 5, 0, 7); x.arc(142, 382, 5, 0, 7); x.fill();
    return c;
  }

  // ================================================================ Ermita de San Isidro (Pantano de San Roque)
  ermita([x, z]) {
    const b = this.building(x, z);
    if (!b) return;
    this.claim(b);
    const M = this.mat;
    const ob = orientedRect(b.ring);
    let ux = Math.cos(ob.ang), uz = Math.sin(ob.ang), L = ob.hw, W = ob.hd;
    if (W > L) { [L, W] = [W, L]; [ux, uz] = [-uz, ux]; }
    const g = this.frame(ob.cx, ob.cz, ux, uz);
    const nw = W * 0.55, H = 6.5;
    // raised forecourt with steps
    this.put(g, sbox(L * 2 + 2, 0.8, W * 2 + 2, 2), M.sillar, 0, 0.4, 0);
    for (let s = 0; s < 4; s++) this.put(g, sbox(0.35, 0.2 * (s + 1), 5, 1), M.sillar, -L - 1.2 - (3 - s) * 0.35, 0.1 * (s + 1), 0);
    this.put(g, sbox(L * 2 - 1, H, nw * 2, 3), M.cal, 0, 0.8 + H / 2, 0);
    this.put(g, gableRoof(L * 2 - 1, nw * 2, 2.6, 0.4), M.teja, 0, 0.8 + H, 0);
    this.put(g, gableEnd(nw * 2, 2.6), M.cal, L - 0.48, 0.8 + H, 0, Math.PI / 2);
    this.put(g, gableEnd(nw * 2, 2.6), M.cal, -L + 0.48, 0.8 + H, 0, -Math.PI / 2);
    // arcaded side porches (portales)
    for (const s of [-1, 1]) {
      for (let k = 0; k < 5; k++) {
        const px = -L + 2 + (k * (L * 2 - 4)) / 4;
        this.put(g, sbox(0.45, 3.2, 0.45, 1), M.cal, px, 0.8 + 1.6, s * (nw + 2.4));
      }
      const pr = this.put(g, sbox(L * 2 - 2, 0.2, 2.9, 2.6), M.teja, 0, 0.8 + 3.6, s * (nw + 1.3));
      pr.rotation.x = s * 0.25;
    }
    // bell-gable with three openings and one bell
    const fx = -L + 0.45;
    this.put(g, sbox(0.6, 3.4, 4.4, 1.6), M.cal, fx, 0.8 + H + 2.2, 0);
    for (let k = -1; k <= 1; k++) {
      const op = new THREE.Mesh(archPanel(0.9, 1.5), M.dark);
      op.position.set(fx - 0.32, 0.8 + H + 1.3 + (k === 0 ? 0.9 : 0), k * 1.3);
      op.rotation.y = -Math.PI / 2; g.add(op);
    }
    const bell = new THREE.Mesh(new THREE.CylinderGeometry(0.2, 0.36, 0.55, 10, 1, true), M.bronze); bell.position.set(fx, 0.8 + H + 2.7, 0); g.add(bell);
    const door = new THREE.Mesh(archPanel(1.8, 3.2), M.wood); door.position.set(fx - 0.33, 0.8, 0); door.rotation.y = -Math.PI / 2; g.add(door);
    this.put(g, sbox(0.1, 1.2, 0.1), M.iron, fx, 0.8 + H + 4.5, 0);
    this.put(g, sbox(0.1, 0.1, 0.7), M.iron, fx, 0.8 + H + 4.8, 0);
    const front = new THREE.Vector3(-L - 6, 0, 0).applyMatrix4(g.matrixWorld);
    this.poi.ermita = { x: front.x, z: front.z };
  }

  // ================================================================ Mercado de Abastos (1924-25): sign + tweak
  mercado([x, z]) {
    const b = this.building(x, z);
    if (!b) return;
    this.overrides.set(b.id, { style: 'color', tint: [0.96, 0.86, 0.66], minFloors: 2 });
    const c = ringCentroid(b.ring);
    this.poi.mercado = { x: c[0], z: c[1] };
    // its front as the 2009 captures show it (225): a round arch for the entrance, its surround and two pilasters in ochre
    // against the lime-washed wall, and over it a crest of ochre with a panel of blue and white tiles — no classical
    // portal with a pediment and a fan-light, no board with its name (venueFront: the door, and the entry for the Interiors)
    venueFront(this, {
      kind: 'mercado', name: 'Mercado de Abastos', sub: 'Desde 1925', x: c[0], z: c[1], seed: 31, doorStyle: 'none',
      override: { minFloors: 2 },
      extra: (g) => {
        const M = this.mat, ocher = tinted(M.cal, 0.46, 0.28, 0.07), recess = tinted(M.cal, 0.5, 0.49, 0.46);
        const pl = (m, x, y, z) => { m.position.set(x, y, z); return m; };
        g.add(pl(new THREE.Mesh(archPanel(2.4, 3.5), recess), 0, 0, 0.03)); // (a recess, painted pale, as the capture shows it)
        const oc = [archRing(1.2, 0.42, 0.28).translate(0, 2.3, 0.14), sbox(0.42, 2.3, 0.28, 1).translate(-1.41, 1.15, 0.14), sbox(0.42, 2.3, 0.28, 1).translate(1.41, 1.15, 0.14)];
        for (const sx of [-1, 1]) oc.push(sbox(0.5, 5.4, 0.22, 1).translate(sx * 2.45, 2.7, 0.11), sbox(0.7, 0.2, 0.3, 1).translate(sx * 2.45, 5.5, 0.15), sbox(0.62, 0.16, 0.3, 1).translate(sx * 1.41, 2.3, 0.15));
        oc.push(sbox(5.9, 0.3, 0.42, 1).translate(0, 5.55, 0.2), sbox(0.5, 0.5, 0.3, 1).translate(0, 3.55, 0.15));
        { const sh = new THREE.Shape(); // (the crest: a scalloped top over the entrance)
          sh.moveTo(-2.6, 0); sh.lineTo(-2.6, 0.4); sh.quadraticCurveTo(-2.1, 0.5, -1.6, 0.95); sh.quadraticCurveTo(-1.2, 1.5, -0.6, 1.5); sh.lineTo(0.6, 1.5); sh.quadraticCurveTo(1.2, 1.5, 1.6, 0.95); sh.quadraticCurveTo(2.1, 0.5, 2.6, 0.4); sh.lineTo(2.6, 0); sh.closePath();
          oc.push(new THREE.ExtrudeGeometry(sh, { depth: 0.3, bevelEnabled: false, curveSegments: 8 }).translate(0, 5.7, 0.05)); }
        const om = new THREE.Mesh(mergeGeos(oc), ocher); om.castShadow = true; om.receiveShadow = true; g.add(om);
        const tc = document.createElement('canvas'); tc.width = 256; tc.height = 96; const tx = tc.getContext('2d');
        tx.fillStyle = '#f4f1ea'; tx.fillRect(0, 0, 256, 96);
        for (let i = 0; i < 4; i++) for (let j = 0; j < 2; j++) { const x0 = i * 64, y0 = j * 48; tx.strokeStyle = '#2c5da8'; tx.lineWidth = 3; tx.strokeRect(x0 + 3, y0 + 3, 58, 42); tx.fillStyle = '#2c5da8'; for (let k = 0; k < 4; k++) { const a = k * Math.PI / 2 + Math.PI / 4; tx.beginPath(); tx.ellipse(x0 + 32 + Math.cos(a) * 10, y0 + 24 + Math.sin(a) * 10, 7, 4, a, 0, 6.283); tx.fill(); } tx.fillStyle = '#7fa6dd'; tx.beginPath(); tx.arc(x0 + 32, y0 + 24, 4, 0, 6.283); tx.fill(); }
        const tt = new THREE.CanvasTexture(tc); tt.colorSpace = THREE.SRGBColorSpace;
        g.add(pl(new THREE.Mesh(new THREE.PlaneGeometry(2.4, 0.9), new THREE.MeshStandardMaterial({ map: tt, roughness: 0.4 })), 0, 6.45, 0.37));
        // the flight of granite steps up to the entrance, between the pilasters (the 2009 captures 224 and 225: three risers of
        // ≈ 0.18 m — twenty pixels each at 3.3 m — and the door's sill ≈ 0.55 m over the pavement), the treads ≈ 0.35 m deep
        const sb = [];
        for (let k = 0; k < 3; k++) sb.push(sbox(4.4, 0.18 * (3 - k), 0.35 * (k + 1), 1).translate(0, (0.18 * (3 - k)) / 2, (0.35 * (k + 1)) / 2));
        const sm = new THREE.Mesh(mergeGeos(sb), M.sillar); sm.castShadow = true; sm.receiveShadow = true; g.add(sm);
      },
    });
    // the cast-iron pump of the Plaza de Abastos (capture 224: a dark column ≈ 1.6 m with a ball on its head on a round stone
    // foot, its spout towards the square; seen 7.3 m ahead and 11 m to the left of the camera as fitted, that is here, in the square)
    {
      const M = this.mat, pg = new THREE.Group(); pg.position.set(195.6, 0, -6.5);
      pg.add(at(new THREE.Mesh(new THREE.CylinderGeometry(0.42, 0.48, 0.28, 12), M.sillar), 0, 0.14, 0));
      pg.add(at(new THREE.Mesh(new THREE.CylinderGeometry(0.1, 0.16, 1.2, 10), M.iron), 0, 0.88, 0));
      pg.add(at(new THREE.Mesh(new THREE.CylinderGeometry(0.17, 0.17, 0.08, 10), M.iron), 0, 1.05, 0));
      pg.add(at(new THREE.Mesh(new THREE.CylinderGeometry(0.1, 0.12, 0.1, 10), M.iron), 0, 1.53, 0));
      pg.add(at(new THREE.Mesh(new THREE.SphereGeometry(0.13, 10, 8), M.iron), 0, 1.66, 0));
      pg.add(at(new THREE.Mesh(new THREE.BoxGeometry(0.05, 0.05, 0.36), M.iron), 0, 1.0, 0.24));
      pg.add(at(new THREE.Mesh(new THREE.BoxGeometry(0.05, 0.12, 0.05), M.iron), 0, 0.93, 0.4));
      pg.traverse((q) => { if (q.isMesh) { q.castShadow = true; q.receiveShadow = true; } });
      this.root.add(pg);
      this.circle(195.6, -6.5, 0.4, 1.7);
    }
  }

  // ================================================================ Plaza de España: cast-iron lamps, benches, trees
  plaza() {
    const plaza = this.map.areas.find((a) => a.name === 'Plaza de España');
    if (!plaza) return;
    const r = plaza.ring;
    const [cx, cz] = ringCentroid(r);
    const M = this.mat;
    // its lamps as its captures show them (views 1, 2: 2026-10-14): tall grey cast iron, four lanterns, each standing in
    // the middle of a round stone bench — the black fernandinas of before were the town's street model
    const lampG = new THREE.Group(), grey = new THREE.MeshStandardMaterial({ color: 0x8c9092, roughness: 0.45, metalness: 0.6 });
    const post = new THREE.Mesh(new THREE.CylinderGeometry(0.1, 0.18, 5.0, 12), grey); post.position.y = 2.5; lampG.add(post);
    const base = new THREE.Mesh(new THREE.CylinderGeometry(0.3, 0.38, 1.0, 12), grey); base.position.y = 0.5; lampG.add(base);
    const seat = new THREE.Mesh(new THREE.CylinderGeometry(1.2, 1.25, 0.45, 28), M.sillar); seat.position.y = 0.225; lampG.add(seat);
    const lip = new THREE.Mesh(new THREE.CylinderGeometry(1.28, 1.28, 0.07, 28), M.sillar); lip.position.y = 0.48; lampG.add(lip);
    const heads = [];
    for (let k = 0; k < 4; k++) {
      const a = (k / 4) * Math.PI * 2;
      const arm = new THREE.Mesh(new THREE.BoxGeometry(0.9, 0.06, 0.06), grey); arm.position.set(Math.cos(a) * 0.45, 4.9, Math.sin(a) * 0.45); arm.rotation.y = -a; lampG.add(arm);
      const lan = new THREE.Mesh(new THREE.CylinderGeometry(0.2, 0.12, 0.5, 6), makeNightGlowMaterial(0xfff0cc, { dayLevel: 0.85, nightLevel: 2.4 }));
      lan.position.set(Math.cos(a) * 0.9, 5.05, Math.sin(a) * 0.9); lampG.add(lan);
      const cap = new THREE.Mesh(new THREE.ConeGeometry(0.28, 0.25, 6), grey); cap.position.set(Math.cos(a) * 0.9, 5.4, Math.sin(a) * 0.9); lampG.add(cap);
      heads.push([Math.cos(a) * 0.9, 5.05, Math.sin(a) * 0.9]);
    }
    lampG.traverse((m) => { if (m.isMesh) { m.castShadow = true; } });
    const spots = [];
    const [x0, z0, x1, z1] = [Math.min(...r.filter((_, i) => i % 2 === 0)), Math.min(...r.filter((_, i) => i % 2)), Math.max(...r.filter((_, i) => i % 2 === 0)), Math.max(...r.filter((_, i) => i % 2))];
    for (let gx = x0 + 6; gx < x1 - 4; gx += 12) for (let gz = z0 + 6; gz < z1 - 4; gz += 12) {
      if (pointInRing(gx, gz, r) && !this.map.buildingAt(gx, gz) && !this.map.roadAt(gx, gz, 1.5)) spots.push([gx, gz]);
    }
    const fu = this.map.pois.find((q) => q.kind === 'amenity:fountain' && pointInRing(q.x, q.z, r)); // (not by the fountain)
    // (the four nearest the middle of the square, clear of the fountain: no forest of them)
    const near = spots.filter(([sx, sz]) => !fu || Math.hypot(sx - fu.x, sz - fu.z) > 8).sort((p, q) => Math.hypot(p[0] - cx, p[1] - cz) - Math.hypot(q[0] - cx, q[1] - cz));
    for (const [lx, lz] of near.slice(0, 4)) {
      const l = lampG.clone(); l.position.set(lx, 0, lz); this.root.add(l);
      this.circle(lx, lz, 1.25, 0.6); this.circle(lx, lz, 0.35, 4);
      for (const h of heads) this.world.lampPoints.push(lx + h[0], h[1], lz + h[2]);
    }
    this.poi.plaza = { x: cx, z: cz };
  }

  // ================================================================ Gas station (Sangar, Ctra. de Don Benito)
  gasStation() {
    const p = this.map.pois.find((p) => p.kind === 'amenity:fuel' && /Sangar/.test(p.name));
    if (!p) return;
    const q = this.map.nearestEdge(p.x, p.z, 40, (e) => e.drive && e.cls === 'primary');
    if (!q) return;
    const d = this.map.sample(q.edge, q.s, {});
    let nx = -d.dz, nz = d.dx;
    if ((p.x - q.x) * nx + (p.z - q.z) * nz < 0) { nx = -nx; nz = -nz; }
    const off = q.edge.w / 2 + 7;
    const cx = q.x + nx * off, cz = q.z + nz * off;
    const g = new THREE.Group();
    g.position.set(cx, 0, cz);
    g.rotation.y = Math.atan2(d.dx, d.dz);
    this.root.add(g);
    g.updateMatrixWorld(true);
    const M = this.mat;
    const canopy = new THREE.Mesh(sbox(8, 0.8, 16, 2), M.white); canopy.position.y = 5.2; g.add(canopy);
    const band = new THREE.Mesh(sbox(8.1, 0.35, 16.1, 2), new THREE.MeshStandardMaterial({ color: 0xd4202c, roughness: 0.5 })); band.position.y = 4.95; g.add(band);
    const under = new THREE.Mesh(new THREE.PlaneGeometry(7.8, 15.8), makeNightGlowMaterial(0xfaf6ea, { dayLevel: 0.9, nightLevel: 1.8 }));
    under.rotation.x = Math.PI / 2; under.position.y = 4.79; g.add(under);
    for (const sx of [-2, 2]) for (const sz of [-5, 5]) {
      const c = new THREE.Mesh(new THREE.BoxGeometry(0.35, 4.8, 0.35), M.white); c.position.set(sx, 2.4, sz); g.add(c);
      const w = g.localToWorld(new THREE.Vector3(sx, 0, sz));
      this.circle(w.x, w.z, 0.3, 5);
    }
    for (const sz of [-5, 5]) {
      const pump = new THREE.Mesh(sbox(0.7, 1.8, 1.2, 1), new THREE.MeshStandardMaterial({ color: 0xeeeeea, roughness: 0.4 })); pump.position.set(0, 0.9, sz); g.add(pump);
      const scr = new THREE.Mesh(new THREE.PlaneGeometry(0.5, 0.35), makeNightGlowMaterial(0x6fd0ff, { dayLevel: 0.6, nightLevel: 1.6 })); scr.position.set(0.36, 1.4, sz); scr.rotation.y = Math.PI / 2; g.add(scr);
      const w = g.localToWorld(new THREE.Vector3(0, 0, sz));
      this.circle(w.x, w.z, 0.7, 2);
    }
    const tot = new THREE.Mesh(sbox(0.5, 6, 1.8, 1), new THREE.MeshStandardMaterial({ color: 0xd4202c, roughness: 0.5 })); tot.position.set(-6, 3, 9); g.add(tot);
    const tl = new THREE.Mesh(new THREE.PlaneGeometry(1.5, 1.5), new THREE.MeshStandardMaterial({ map: canvasTex(textCanvas('GASOLINERA', { w: 512, h: 512, bg: '#d4202c', fg: '#ffffff', font: 'bold 70px Arial' })) }));
    tl.position.set(-5.74, 4.8, 9); tl.rotation.y = Math.PI / 2; g.add(tl);
    g.traverse((m) => { if (m.isMesh) { m.castShadow = true; m.receiveShadow = true; } });
    this.poi.gasolinera = { x: cx, z: cz };
  }

  // ================================================================ Cooperativa del Campo San Pedro (tanks)
  tanks() {
    for (const a of this.map.areas) {
      if (a.kind !== 'man_made:storage_tank') continue;
      const [cx, cz] = ringCentroid(a.ring);
      let r = 0;
      for (let i = 0; i < a.ring.length; i += 2) r = Math.max(r, Math.hypot(a.ring[i] - cx, a.ring[i + 1] - cz));
      r = Math.min(r, 8);
      const h = 9 + r * 0.6;
      this.add(new THREE.CylinderGeometry(r, r, h, 24), this.mat.steel, cx, h / 2, cz);
      this.add(new THREE.ConeGeometry(r * 1.02, r * 0.35, 24), this.mat.steel, cx, h + r * 0.17, cz);
      this.circle(cx, cz, r, h);
    }
    const coop = this.map.areas.find((a) => /Cooperativa/.test(a.name));
    if (coop) { const [cx, cz] = ringCentroid(coop.ring); this.poi.cooperativa = { x: cx, z: cz }; }
  }

  // ================================================================ Estadio Municipal "La Noria": floodlights + stand
  stadium() {
    const pitches = this.map.areas.filter((a) => a.kind === 'leisure:pitch' && a.sport === 'soccer');
    let best = null;
    for (const a of pitches) { const ar = Math.abs(ringArea(a.ring)); if (!best || ar > best.ar) best = { a, ar }; }
    if (!best) return;
    const ob = orientedRect(best.a.ring);
    let ux = Math.cos(ob.ang), uz = Math.sin(ob.ang), L = ob.hw, W = ob.hd;
    if (W > L) { [L, W] = [W, L]; [ux, uz] = [-uz, ux]; }
    const g = this.frame(ob.cx, ob.cz, ux, uz);
    const M = this.mat;
    for (const sx of [-1, 1]) for (const sz of [-1, 1]) {
      this.put(g, new THREE.CylinderGeometry(0.2, 0.35, 22, 8), M.steel, sx * (L + 3), 11, sz * (W + 3));
      const head = this.put(g, sbox(2.4, 1.4, 0.4, 1), M.steel, sx * (L + 3), 22, sz * (W + 3));
      head.lookAt(g.localToWorld(new THREE.Vector3(0, 0, 0)));
      const lamp = new THREE.Mesh(new THREE.PlaneGeometry(2.2, 1.2), makeNightGlowMaterial(0xffffff, { dayLevel: 0.7, nightLevel: 3 }));
      lamp.position.set(sx * (L + 2.7), 22, sz * (W + 2.7)); lamp.lookAt(g.localToWorld(new THREE.Vector3(0, 0, 0)));
      g.add(lamp);
    }
    // stand (grada) along one side
    for (let s = 0; s < 6; s++) this.put(g, sbox(L * 1.4, 0.45, 0.8, 1), M.white, 0, 0.225 + s * 0.45, W + 2 + s * 0.8);
    const roof = this.put(g, sbox(L * 1.45, 0.2, 5.6, 2), new THREE.MeshStandardMaterial({ color: 0x1f5aa0, roughness: 0.5 }), 0, 6.4, W + 4.2);
    roof.rotation.x = -0.08;
    for (let k = 0; k < 5; k++) this.put(g, new THREE.CylinderGeometry(0.1, 0.1, 6.4, 6), M.steel, -L * 0.7 + k * (L * 0.35), 3.2, W + 6.8);
    // goals
    for (const sx of [-1, 1]) {
      this.put(g, sbox(0.12, 2.44, 0.12), M.white, sx * (L - 0.5), 1.22, -3.66);
      this.put(g, sbox(0.12, 2.44, 0.12), M.white, sx * (L - 0.5), 1.22, 3.66);
      this.put(g, sbox(0.12, 0.12, 7.44), M.white, sx * (L - 0.5), 2.44, 0);
    }
    // field lines
    const lm = new THREE.MeshBasicMaterial({ color: 0xf2f2f2, polygonOffset: true, polygonOffsetFactor: -6, polygonOffsetUnits: -24 });
    const line = (w, d, x, z) => { const m = new THREE.Mesh(new THREE.PlaneGeometry(w, d), lm); m.rotation.x = -Math.PI / 2; m.position.set(x, 0.03, z); g.add(m); };
    line(L * 2 - 2, 0.12, 0, -W + 1); line(L * 2 - 2, 0.12, 0, W - 1); line(0.12, W * 2 - 2, -L + 1, 0); line(0.12, W * 2 - 2, L - 1, 0); line(0.12, W * 2 - 2, 0, 0);
    const ring = new THREE.Mesh(new THREE.RingGeometry(8.9, 9.05, 40), lm); ring.rotation.x = -Math.PI / 2; ring.position.y = 0.03; g.add(ring);
    this.poi.estadio = { x: ob.cx, z: ob.cz };
  }

  // ================================================================ services: Guardia Civil, Centro de Salud, Correos
  services() {
    const gc = this.map.areas.find((a) => a.kind === 'landuse:military');
    if (gc) {
      const [cx, cz] = ringCentroid(gc.ring);
      this.poi.guardia = { x: cx, z: cz };
      this.flagPole(cx, cz, 'es');
      this.signTotem(cx + 3, cz, 'GUARDIA CIVIL', '#1f5a2e', '#ffffff');
    }
    const cs = this.map.areas.find((a) => a.kind === 'amenity:clinic');
    if (cs) {
      const [cx, cz] = ringCentroid(cs.ring);
      this.poi.salud = { x: cx, z: cz };
      this.signTotem(cx, cz, 'CENTRO DE SALUD', '#1a7a46', '#ffffff');
    }
  }
  flagPole(x, z, kind) {
    const pole = this.add(new THREE.CylinderGeometry(0.06, 0.08, 9, 8), this.mat.steel, x, 4.5, z);
    const fg = new THREE.PlaneGeometry(2.2, 1.4, 14, 5);
    fg.translate(1.1, -0.7, 0);
    const flag = new THREE.Mesh(fg, new THREE.MeshStandardMaterial({ map: canvasTex(flagCanvas(kind)), side: THREE.DoubleSide, roughness: 0.8 }));
    flag.position.set(x, 8.9, z);
    flag.castShadow = true;
    this.root.add(flag);
    this.flags.push({ mesh: flag, base: fg.attributes.position.array.slice(), phase: x });
    this.circle(x, z, 0.2, 9);
  }
  signTotem(x, z, txt, bg, fg) {
    // free spot nearby (outside buildings)
    let px = x, pz = z;
    for (let k = 0; k < 30 && this.map.buildingAt(px, pz); k++) { px = x + Math.cos(k) * (2 + k); pz = z + Math.sin(k) * (2 + k); }
    const g = new THREE.Group();
    const post = new THREE.Mesh(sbox(0.25, 2.8, 0.25), this.mat.steel); post.position.y = 1.4; g.add(post);
    const board = new THREE.Mesh(new THREE.PlaneGeometry(2.8, 0.8), new THREE.MeshStandardMaterial({ map: canvasTex(textCanvas(txt, { w: 700, h: 200, bg, fg, font: 'bold 64px Arial' })), side: THREE.DoubleSide, roughness: 0.5 }));
    board.position.y = 2.6; g.add(board);
    g.position.set(px, 0, pz);
    const q = this.map.nearestEdge(px, pz, 60, (e) => e.drive);
    if (q) g.rotation.y = Math.atan2(q.x - px, q.z - pz);
    g.traverse((m) => { if (m.isMesh) m.castShadow = true; });
    this.root.add(g);
    this.circle(px, pz, 0.3, 3);
  }

  // called after vegetation; statues need the character module (set by game)
  finish() {}

  update(dt, night) {
    const t = shared.uTime.value;
    updateWater(this, dt, night);
    // floodlights on the stone monuments at night (Santa María's walls and tower glow warm)
    for (const k of ['mamp', 'sillar', 'quoin', 'zocalo']) {
      const m = this.mat[k];
      if (!m) continue;
      if (!m.emissiveMap && m.map) { m.emissiveMap = m.map; m.emissive.setRGB(1, 0.8, 0.56); m.needsUpdate = true; }
      m.emissiveIntensity = night * 0.34;
    }
    // (and the church doors in the same floodlight)
    for (const d of this.churchDoors || []) {
      const m = d.mats.outer;
      if (!m.emissiveMap && m.map) { m.emissiveMap = m.map; m.emissive.setRGB(1, 0.8, 0.56); m.needsUpdate = true; }
      m.emissiveIntensity = night * 0.3;
    }
    for (const f of this.flags) {
      const p = f.mesh.geometry.attributes.position;
      const b = f.base;
      for (let i = 0; i < p.count; i++) {
        const x = b[i * 3];
        p.setZ(i, b[i * 3 + 2] + Math.sin(x * 3 - t * 5 + f.phase) * 0.12 * x);
      }
      p.needsUpdate = true;
    }
    for (const a of this.animated) {
      if (a.kind === 'clock' && this.hour !== undefined) {
        const h = this.hour % 12, m = (this.hour % 1) * 60;
        a.hh.rotation.z = -(h / 12) * Math.PI * 2;
        a.mh.rotation.z = -(m / 60) * Math.PI * 2;
      } else if (a.kind === 'bell') {
        a.mesh.rotation.x = this.bellSwing ? Math.sin(t * 3 + a.phase) * 0.5 * this.bellSwing : 0;
      }
    }
    if (this.bellSwing) this.bellSwing = Math.max(0, this.bellSwing - dt * 0.2);
  }
}
