// Extrudes Catastro building parts into textured Extremaduran houses: facades, party walls, hip/tile/flat roofs.
import * as THREE from 'three';
import { FACADE_STYLES, FACADE_LAYERS_PER_STYLE, ROOF_BASE, BAY_W, FLOOR_H, STYLE_DEF } from './textures.js';
import { ringArea, orientedRect, hash1, mulberry32, pointInRing, ringBounds, polyNearest } from './util.js';
import { PolyIndex } from './collision.js';
// (the look — plastilina / real — as LOOK: STYLE here is the façade styles' layers)
import { STYLE as LOOK } from './style.js';
import { planPart, holeRect, recessDepth, styleHasHoles, CT } from './facades.js';
import { matchRun, emitMeasuredRun, lin } from './fachadas.js';
import { streetsOf, houseStyle, seenWall, seenMuros, seenNave, seenNotNave, seenFloors, seenRoof, seenTile, seenHeight, seenPeel, STYLES as CALLES } from './calles.js';

const STYLE = Object.fromEntries(FACADE_STYLES.map((s, i) => [s, i * FACADE_LAYERS_PER_STYLE]));
const ROOF = { teja: ROOF_BASE + 0, azotea: ROOF_BASE + 1, chapa: ROOF_BASE + 2, uralita: ROOF_BASE + 3 };
const SHOP_KINDS = /^(shop:|amenity:(bar|cafe|bank|pharmacy|restaurant|fast_food|pub|post_office|driving_school|dentist|clinic|library|casino)|office:|craft:)/;

const NORECT = [0, 0, 0, 0];
// a house's own plinth (calles.js: its street's style), for the shader: its colour (linear) and its kind × 10 plus its
// height in metres (kinds: 1 painted, 2 granite, 3 rough stone, 4 glazed tiles, 5 cement, 6 none — the wall to the
// ground); all zero: the plinth of its façade kind (textures.js)
export const ZOC_KINDS = { pintado: 1, granito: 2, piedra: 3, azulejo: 4, cemento: 5, ninguno: 6 };
const ZOC0 = [0, 0, 0, 0];
const CHAPA = '#b5bbbd'; // (the corrugated sheet's own grey, as painted: textures.js)
class Chunk {
  constructor() {
    this.pos = []; this.nor = []; this.uv = []; this.tex = []; this.tint = []; this.idx = []; this.rect = []; this.wall = []; this.zoc = [];
    this.zocNow = ZOC0; // (the plinth of the house being laid: every vertex takes it)
    this.edge = LOOK.plastilina ? [] : null; // (claymation: where each wall runs to its corners, to round them in the shader)
  }
  get vcount() { return this.pos.length / 3; }
  // a-b bottom, c-d top; ks: optional per-vertex tint multipliers (baked occlusion)
  quad(ax, ay, az, bx, by, bz, cx, cy, cz, dx, dy, dz, nx, ny, nz, u0, v0, u1, v1, tex, tint, rect = NORECT, wallH = 0, ks = null, edge = null, nrm = null) {
    const i = this.vcount;
    // nrm: [na, nb] the normals at the a/d and b/c sides (a wall bending round a rounded corner shades smoothly)
    // edge: [s at a/d, s at b/c, code] — s the distance along the wall from its first corner, code its length plus which
    // of its two ends are corners to round (1e4: the first, 2e4: the second)
    if (this.edge) { if (edge) this.edge.push(edge[0], edge[2], edge[1], edge[2], edge[1], edge[2], edge[0], edge[2]); else this.edge.push(0, 0, 0, 0, 0, 0, 0, 0); }
    this.pos.push(ax, ay, az, bx, by, bz, cx, cy, cz, dx, dy, dz);
    for (let k = 0; k < 4; k++) {
      const m = ks ? ks[k] : 1;
      if (nrm) { const q = k === 1 || k === 2 ? nrm[1] : nrm[0]; this.nor.push(q[0], q[1], q[2]); } else this.nor.push(nx, ny, nz);
      this.tex.push(tex[0], tex[1], tex[2], tex[3]); this.tint.push(tint[0] * m, tint[1] * m, tint[2] * m);
      this.rect.push(rect[0], rect[1], rect[2], rect[3]); this.wall.push(wallH);
      const z = this.zocNow; this.zoc.push(z[0], z[1], z[2], z[3]);
    }
    this.uv.push(u0, v0, u1, v0, u1, v1, u0, v1);
    // orient triangles so their geometric normal agrees with the requested one
    const e1x = bx - ax, e1y = by - ay, e1z = bz - az, e2x = cx - ax, e2y = cy - ay, e2z = cz - az;
    const gx = e1y * e2z - e1z * e2y, gy = e1z * e2x - e1x * e2z, gz = e1x * e2y - e1y * e2x;
    if (gx * nx + gy * ny + gz * nz >= 0) this.idx.push(i, i + 1, i + 2, i, i + 2, i + 3);
    else this.idx.push(i, i + 2, i + 1, i, i + 3, i + 2);
  }
  tri(a, b, c, n, uva, uvb, uvc, tex, tint) {
    const i = this.vcount;
    if (this.edge) this.edge.push(0, 0, 0, 0, 0, 0);
    this.pos.push(a[0], a[1], a[2], b[0], b[1], b[2], c[0], c[1], c[2]);
    const z = this.zocNow;
    for (let k = 0; k < 3; k++) { this.nor.push(n[0], n[1], n[2]); this.tex.push(tex[0], tex[1], tex[2], tex[3]); this.tint.push(tint[0], tint[1], tint[2]); this.rect.push(0, 0, 0, 0); this.wall.push(0); this.zoc.push(z[0], z[1], z[2], z[3]); }
    this.uv.push(uva[0], uva[1], uvb[0], uvb[1], uvc[0], uvc[1]);
    const e1x = b[0] - a[0], e1y = b[1] - a[1], e1z = b[2] - a[2], e2x = c[0] - a[0], e2y = c[1] - a[1], e2z = c[2] - a[2];
    const gx = e1y * e2z - e1z * e2y, gy = e1z * e2x - e1x * e2z, gz = e1x * e2y - e1y * e2x;
    if (gx * n[0] + gy * n[1] + gz * n[2] >= 0) this.idx.push(i, i + 1, i + 2);
    else this.idx.push(i, i + 2, i + 1);
  }
  geometry() {
    const g = new THREE.BufferGeometry();
    g.setAttribute('position', new THREE.Float32BufferAttribute(this.pos, 3));
    g.setAttribute('normal', new THREE.Float32BufferAttribute(this.nor, 3));
    g.setAttribute('aUv', new THREE.Float32BufferAttribute(this.uv, 2));
    g.setAttribute('aTex', new THREE.Float32BufferAttribute(this.tex, 4));
    g.setAttribute('aTint', new THREE.Float32BufferAttribute(this.tint, 3));
    const r8 = new Uint8Array(this.rect.length);
    for (let i = 0; i < r8.length; i++) r8[i] = Math.round(Math.min(1, Math.max(0, this.rect[i])) * 255);
    g.setAttribute('aRect', new THREE.BufferAttribute(r8, 4, true));
    g.setAttribute('aWallH', new THREE.Float32BufferAttribute(this.wall, 1));
    g.setAttribute('aZoc', new THREE.Float32BufferAttribute(this.zoc, 4));
    if (this.edge) g.setAttribute('aEdge', new THREE.Float32BufferAttribute(this.edge, 2));
    g.setIndex(this.vcount > 65535 ? new THREE.Uint32BufferAttribute(this.idx, 1) : new THREE.Uint16BufferAttribute(this.idx, 1));
    g.computeBoundingSphere();
    g.computeBoundingBox();
    return g;
  }
}

const WHITES = [[1, 1, 1], [0.99, 0.985, 0.97], [0.985, 0.98, 0.99], [1, 0.975, 0.94], [0.97, 0.965, 0.95]];
const COLORS = [[0.97, 0.9, 0.76], [0.95, 0.84, 0.6], [0.95, 0.78, 0.66], [0.9, 0.74, 0.52], [0.97, 0.92, 0.68], [0.86, 0.9, 0.8], [0.84, 0.89, 0.92], [0.96, 0.87, 0.8]];
// the claymation's: since 2026-10-12 the real town's — whitewash that is white, a little warm; the coloured houses in
// the creams, ochres and pale salmons of the old town's captures (they were peach and straw, after the user's first
// retouched reference pictures)
const WHITES_CLAY = [[1, 1, 1], [1, 0.99, 0.975], [0.99, 0.985, 0.97], [1, 0.995, 0.98], [0.98, 0.975, 0.96]];
const COLORS_CLAY = [[0.95, 0.9, 0.8], [0.93, 0.85, 0.7], [0.96, 0.92, 0.78], [0.94, 0.86, 0.78], [0.9, 0.88, 0.84], [0.96, 0.93, 0.86], [0.92, 0.82, 0.66], [0.97, 0.95, 0.9]];

// (the kinds of a house no capture shows, by its age: in the shares the 51 streets seen in the captures have — half of
// it whitewash, a quarter cream, a sixth a colour, one front in twenty bare brick; the brick was a quarter to a half of
// the newer houses and the blocks, and the audit of 2026-10-13 found it in the background of view after view)
function chooseStyle(b, rnd) {
  const y = b.year || 1960;
  if ((b.use === 1 || b.use === 2) && !seenNotNave(b.id)) return 'nave';
  const r = rnd();
  if (b.floors >= 3 && y >= 1965) return r < 0.12 ? 'ladrillo' : r < 0.7 ? 'moderna' : 'color';
  if (y >= 2005) return r < 0.4 ? 'moderna' : r < 0.75 ? 'renovada' : r < 0.95 ? 'color' : 'ladrillo';
  if (y >= 1970) return r < 0.06 ? 'ladrillo' : r < 0.48 ? 'renovada' : r < 0.74 ? 'color' : r < 0.87 ? 'trad_verde' : 'trad_ocre';
  return r < 0.36 ? 'trad_verde' : r < 0.64 ? 'trad_ocre' : r < 0.86 ? 'renovada' : 'color';
}

// inset a CCW ring by d (inward). Returns flat array or null if degenerate.
function insetRing(r, d) {
  const n = r.length / 2;
  const out = new Array(r.length);
  for (let i = 0; i < n; i++) {
    const p = (i + n - 1) % n, q = (i + 1) % n;
    const ax = r[p * 2], az = r[p * 2 + 1], bx = r[i * 2], bz = r[i * 2 + 1], cx = r[q * 2], cz = r[q * 2 + 1];
    let d1x = bx - ax, d1z = bz - az, l1 = Math.hypot(d1x, d1z);
    let d2x = cx - bx, d2z = cz - bz, l2 = Math.hypot(d2x, d2z);
    if (l1 < 1e-4 || l2 < 1e-4) return null;
    d1x /= l1; d1z /= l1; d2x /= l2; d2z /= l2;
    // inward normals for CCW: (-dz, dx)
    const n1x = -d1z, n1z = d1x, n2x = -d2z, n2z = d2x;
    let mx = n1x + n2x, mz = n1z + n2z;
    const ml = Math.hypot(mx, mz);
    if (ml < 1e-4) return null;
    mx /= ml; mz /= ml;
    const cosH = mx * n1x + mz * n1z;
    if (cosH < 0.3) return null; // too sharp
    const k = d / cosH;
    out[i * 2] = bx + mx * k; out[i * 2 + 1] = bz + mz * k;
  }
  // validity: same orientation, all inside, edges not flipped, not crossing each other
  if (ringArea(out) <= 0.5) return null;
  for (let i = 0; i < n; i++) {
    if (!pointInRing(out[i * 2], out[i * 2 + 1], r)) return null;
    const q = (i + 1) % n;
    const ox = r[q * 2] - r[i * 2], oz = r[q * 2 + 1] - r[i * 2 + 1];
    const ix = out[q * 2] - out[i * 2], iz = out[q * 2 + 1] - out[i * 2 + 1];
    if (ox * ix + oz * iz <= 0) return null;
  }
  if (selfCrossing(out)) return null;
  return out;
}

// does the outline cross itself?
function selfCrossing(r) {
  const n = r.length / 2;
  for (let i = 0; i < n; i++) {
    const ax = r[i * 2], az = r[i * 2 + 1], bx = r[((i + 1) % n) * 2], bz = r[((i + 1) % n) * 2 + 1];
    for (let j = i + 2; j < n; j++) {
      if (i === 0 && j === n - 1) continue;
      const cx = r[j * 2], cz = r[j * 2 + 1], dx = r[((j + 1) % n) * 2], dz = r[((j + 1) % n) * 2 + 1];
      const d1 = (bx - ax) * (cz - az) - (bz - az) * (cx - ax), d2 = (bx - ax) * (dz - az) - (bz - az) * (dx - ax);
      const d3 = (dx - cx) * (az - cz) - (dz - cz) * (ax - cx), d4 = (dx - cx) * (bz - cz) - (dz - cz) * (bx - cx);
      if (d1 * d2 < 0 && d3 * d4 < 0) return true;
    }
  }
  return false;
}
// the outline without the corners that are not corners: those on a straight wall (where a neighbour's party wall meets
// it, solidez.js), within 3 cm of the line through the two either side — for the roof, which looks at its true shape
function cleanRing(r, tol = 0.03) {
  let pts = [];
  for (let i = 0; i < r.length; i += 2) pts.push(r[i], r[i + 1]);
  for (let guard = 0; guard < 400; guard++) {
    const n = pts.length / 2;
    if (n <= 3) break;
    let drop = -1;
    for (let i = 0; i < n; i++) {
      const h = (i - 1 + n) % n, j = (i + 1) % n;
      const ax = pts[h * 2], az = pts[h * 2 + 1], bx = pts[j * 2], bz = pts[j * 2 + 1], px = pts[i * 2], pz = pts[i * 2 + 1];
      const dx = bx - ax, dz = bz - az, L = Math.hypot(dx, dz);
      if (L < 1e-6) { drop = i; break; }
      const t = ((px - ax) * dx + (pz - az) * dz) / (L * L);
      if (t <= 0 || t >= 1) continue;
      if (Math.abs((px - ax) * dz - (pz - az) * dx) / L < tol) { drop = i; break; }
    }
    if (drop < 0) break;
    pts.splice(drop * 2, 2);
  }
  return pts.length >= 6 && ringArea(pts) > 0 ? pts : r;
}

// drop near-duplicate and nearly collinear vertices (cadastral outlines are full of them)
function simplifyRing(r) {
  let pts = [];
  for (let i = 0; i < r.length; i += 2) pts.push([r[i], r[i + 1]]);
  for (let pass = 0; pass < 3; pass++) {
    const out = [];
    const n = pts.length;
    if (n <= 4) break;
    for (let i = 0; i < n; i++) {
      const a = pts[(i + n - 1) % n], b = pts[i], c = pts[(i + 1) % n];
      const abx = b[0] - a[0], abz = b[1] - a[1], bcx = c[0] - b[0], bcz = c[1] - b[1];
      const lab = Math.hypot(abx, abz), lbc = Math.hypot(bcx, bcz);
      if (lab < 0.25) continue;
      const cross = Math.abs(abx * bcz - abz * bcx) / (lab * lbc + 1e-9);
      if (cross < 0.06 && abx * bcx + abz * bcz > 0) continue; // almost straight: skip the middle vertex
      out.push(b);
    }
    if (out.length < 3 || out.length === n) { if (out.length >= 3) pts = out; break; }
    pts = out;
  }
  const res = [];
  for (const q of pts) res.push(q[0], q[1]);
  return ringArea(res) > 0 ? res : r;
}

function outsetRing(r, d) {
  const n = r.length / 2;
  const out = new Array(r.length);
  for (let i = 0; i < n; i++) {
    const p = (i + n - 1) % n, q = (i + 1) % n;
    let d1x = r[i * 2] - r[p * 2], d1z = r[i * 2 + 1] - r[p * 2 + 1];
    let d2x = r[q * 2] - r[i * 2], d2z = r[q * 2 + 1] - r[i * 2 + 1];
    const l1 = Math.hypot(d1x, d1z) || 1, l2 = Math.hypot(d2x, d2z) || 1;
    d1x /= l1; d1z /= l1; d2x /= l2; d2z /= l2;
    let mx = d1z + d2z, mz = -d1x - d2x; // outward normals sum
    const ml = Math.hypot(mx, mz) || 1;
    mx /= ml; mz /= ml;
    const cosH = Math.max(0.4, mx * d1z + mz * -d1x);
    out[i * 2] = r[i * 2] + (mx * d) / cosH;
    out[i * 2 + 1] = r[i * 2 + 1] + (mz * d) / cosH;
  }
  return out;
}

// claymation: an outline with its convex corners rounded — each replaced by a short arc (a quadratic curve with the
// corner as its control point), ~0.32 m round; nrm: the curve's own outward normal at its points (NaN elsewhere), so
// the bend shades smooth and meets the straight walls with their own normal
// sharp(x, z): a corner another house shares (the end of a party wall): kept square, or a notch would open between them
function roundRing(r, sharp = null, R = 0.32, seg = 6) {
  const n = r.length / 2, pts = [], nrm = [];
  for (let i = 0; i < n; i++) {
    const h = (i - 1 + n) % n, j = (i + 1) % n;
    const px = r[i * 2], pz = r[i * 2 + 1];
    const ax = r[h * 2] - px, az = r[h * 2 + 1] - pz, bx = r[j * 2] - px, bz = r[j * 2 + 1] - pz;
    const la = Math.hypot(ax, az), lb = Math.hypot(bx, bz);
    const cr = la > 1e-6 && lb > 1e-6 ? (-ax * bz + az * bx) / (la * lb) : 0; // (> 0: a convex corner)
    if (la < 0.5 || lb < 0.5 || cr < 0.35 || (sharp && sharp(px, pz))) { pts.push(px, pz); nrm.push(NaN, NaN); continue; }
    const theta = Math.acos(Math.max(-1, Math.min(1, (ax * bx + az * bz) / (la * lb))));
    const t = Math.min(R / Math.tan(theta / 2), la * 0.35, lb * 0.35);
    // (as many pieces as the arc is long, none under 7 cm: the walls leave out pieces shorter than 5 cm, and a shallow
    // corner's six pieces were — a slit from the eaves to the ground opened there, 2026-10-14; a corner barely bent stays)
    const ns = Math.min(seg, Math.floor((2 * t) / 0.07));
    if (ns < 1) { pts.push(px, pz); nrm.push(NaN, NaN); continue; }
    const p0x = px + (ax / la) * t, p0z = pz + (az / la) * t, p1x = px + (bx / lb) * t, p1z = pz + (bz / lb) * t;
    for (let k = 0; k <= ns; k++) {
      const s = k / ns, a = (1 - s) * (1 - s), b = 2 * (1 - s) * s, c = s * s;
      pts.push(a * p0x + b * px + c * p1x, a * p0z + b * pz + c * p1z);
      const tx = 2 * (1 - s) * (px - p0x) + 2 * s * (p1x - px), tz = 2 * (1 - s) * (pz - p0z) + 2 * s * (p1z - pz), tl = Math.hypot(tx, tz) || 1;
      nrm.push(tz / tl, -tx / tl); // (outward, as the walls': (dz, -dx))
    }
  }
  return { pts, nrm };
}

// The pieces of a wall (from a, along d, outward n) and how high the parts behind it hide each: [t0, t1, cy] in order,
// cy 0 where nothing stands behind it, H where a part as tall stands there. A part stands behind the wall where the line
// 0.2 mm outside it runs inside that part's outline (not in its courtyards); its ends found exactly, where the line
// crosses the part's walls — so a wall is hidden exactly as far as its neighbour reaches, never a hand's breadth more
// (the old half-metre samples hid a notch of wall beside every house a little shorter than its plot). Two walls the
// welding made one (solidez.js) hide each other; two that are a crack apart are both drawn, and the crack shows a wall,
// never the void behind it.
export const COVER_OFF = 0.0002;
const _cands = [];
function coverOf(partIndex, p, ax, az, dx, dz, nx, nz, L, H) {
  const ox = ax + nx * COVER_OFF, oz = az + nz * COVER_OFF, ex = ox + dx, ez = oz + dz;
  _cands.length = 0;
  partIndex.query(Math.min(ox, ex) - 0.01, Math.min(oz, ez) - 0.01, Math.max(ox, ex) + 0.01, Math.max(oz, ez) + 0.01, _cands);
  const spans = []; // [t0, t1, h]
  for (const q of _cands) {
    const d = q.data;
    if (d === p) continue;
    const ts = [0, 1];
    const cut = (r) => {
      const n = r.length / 2;
      for (let i = 0; i < n; i++) {
        const j = (i + 1) % n, cx = r[i * 2], cz = r[i * 2 + 1], fx = r[j * 2] - cx, fz = r[j * 2 + 1] - cz;
        const den = dx * fz - dz * fx;
        if (Math.abs(den) < 1e-12) continue;
        const t = ((cx - ox) * fz - (cz - oz) * fx) / den, u = ((cx - ox) * dz - (cz - oz) * dx) / den;
        if (t > 1e-6 && t < 1 - 1e-6 && u >= -1e-9 && u <= 1 + 1e-9) ts.push(t);
      }
    };
    cut(d.ring);
    if (d.holes) for (const h of d.holes) cut(h);
    ts.sort((a, b) => a - b);
    for (let k = 0; k + 1 < ts.length; k++) {
      const t0 = ts[k], t1 = ts[k + 1];
      if (t1 - t0 < 1e-7) continue;
      const tm = (t0 + t1) / 2, x = ox + dx * tm, z = oz + dz * tm;
      if (!pointInRing(x, z, d.ring) || (d.holes && d.holes.some((h) => pointInRing(x, z, h)))) continue;
      spans.push([t0, t1, d.H]);
    }
  }
  if (!spans.length) return [[0, 1, 0]];
  // the height behind each stretch: the tallest part there
  const cuts = [0, 1];
  for (const s of spans) cuts.push(s[0], s[1]);
  cuts.sort((a, b) => a - b);
  const out = [];
  for (let k = 0; k + 1 < cuts.length; k++) {
    const t0 = cuts[k], t1 = cuts[k + 1];
    if (t1 - t0 < 1e-7) continue;
    const tm = (t0 + t1) / 2;
    let h = 0;
    for (const s of spans) if (tm > s[0] && tm < s[1] && s[2] > h) h = s[2];
    const cy = h >= H - 0.05 ? H : Math.round(h * 10) / 10;
    const last = out[out.length - 1];
    if (last && Math.abs(last[2] - cy) <= 0.05) last[1] = t1;
    else out.push([t0, t1, cy]);
  }
  // slivers under 2 cm join their neighbour, the wall drawn where in doubt (the lower of the two hides less)
  for (let k = 0; k < out.length && out.length > 1; k++) {
    const s = out[k];
    if ((s[1] - s[0]) * L >= 0.02) continue;
    const prev = out[k - 1], next = out[k + 1];
    const into = !prev ? next : !next ? prev : prev[2] <= next[2] ? prev : next;
    into[2] = Math.min(into[2], s[2]);
    if (into === prev) prev[1] = s[1]; else next[0] = s[0];
    out.splice(k, 1); k = -1;
  }
  for (let k = 1; k < out.length; k++) if (Math.abs(out[k][2] - out[k - 1][2]) <= 0.05) { out[k - 1][1] = out[k][1]; out.splice(k, 1); k--; }
  return out;
}

function triangulate(ring, holes) {
  const toV = (r) => { const a = []; for (let i = 0; i < r.length; i += 2) a.push(new THREE.Vector2(r[i], r[i + 1])); return a; };
  const contour = toV(ring);
  const hs = holes ? holes.map(toV) : [];
  const faces = THREE.ShapeUtils.triangulateShape(contour, hs);
  const all = contour.concat(...hs);
  return { faces, pts: all };
}

// facade: { holes: bool, forcedDoors: [{x, z}], openings: [], runs: [] } — real openings + records for the 3D details
// measured: the houses modelled from photographs (fachadas.js resolveMeasured): their fronts, part heights and roofs
const BAY_RANK = { P: 5, C: 4, T: 3, B: 2, V: 1 };
function squeezeFront(fz, k) {
  const out = {};
  for (const [f, row] of Object.entries(fz)) {
    if (row.length <= k) { out[f] = row; continue; }
    let s = '';
    for (let j = 0; j < k; j++) {
      const a = Math.floor((j * row.length) / k), b = Math.max(a + 1, Math.floor(((j + 1) * row.length) / k));
      let best = '-';
      for (const ch of row.slice(a, b)) if ((BAY_RANK[ch] || 0) > (BAY_RANK[best] || 0)) best = ch;
      s += best;
    }
    out[f] = s;
  }
  return out;
}
export function buildBuildings(map, { chunkSize = 220, skipPart = null, onBuilding = null, overrides = null, facade = null, measured = null, church = null } = {}) {
  const chunks = new Map();
  const chunkOf = (x, z) => {
    const k = Math.floor(x / chunkSize) + ':' + Math.floor(z / chunkSize);
    let c = chunks.get(k);
    if (!c) chunks.set(k, (c = new Chunk()));
    return c;
  };
  const ao = []; // ground AO strips: x,z pairs of quads
  // ---- per-building attributes
  const shopPoi = map.pois.filter((p) => SHOP_KINDS.test(p.kind));
  const streets = streetsOf(map, church); // (the street each building looks onto: its style, calles.js)
  const bInfo = map.buildings.map((b) => {
    const rnd = mulberry32((b.id * 2654435761) >>> 0);
    let style = chooseStyle(b, rnd);
    let tint;
    const PL = LOOK.plastilina, CO = PL ? COLORS_CLAY : COLORS, WH = PL ? WHITES_CLAY : WHITES;
    if (style === 'color') tint = CO[Math.floor(rnd() * CO.length)];
    else if (style === 'ladrillo' || style === 'piedra') tint = [1, 1, 1];
    else if (style === 'nave') tint = rnd() < 0.5 ? [1, 1, 1] : [0.95, 0.93, 0.88];
    else tint = WH[Math.floor(rnd() * WH.length)];
    const rt = 0.85 + rnd() * 0.25;
    // (the claymation's roofs: fired clay, terracotta)
    const roofTint = PL ? [rt * 0.98, rt * (0.84 + rnd() * 0.06), rt * (0.76 + rnd() * 0.08)] : [rt, rt * (0.95 + rnd() * 0.08), rt * (0.9 + rnd() * 0.12)];
    const info = { style, tint, roofTint, seed: rnd(), shop: b.use === 4 ? 1 : 0, rnd, pitch: 0.42 + rnd() * 0.16, minFloors: 0 };
    // a house on one of the old town's streets as they really are (calles.js): its kind, its paint and its plinth from
    // its street's style — the paint exactly the hex measured, over its kind's own painted wall
    const hs = style !== 'nave' ? houseStyle(streets[b.id], b.id) : null;
    // a shed seen in the captures: its colour at least (the newer quarters' are of cream or white block, not grey sheet)
    const sw = style === 'nave' && seenWall(b.id);
    if (sw) { const w = lin(sw), s0 = lin('#c9cdce'); info.tint = [0, 1, 2].map((k) => Math.min(3, w[k] / s0[k])); }
    if (style === 'nave') { const sn = seenNave(b.id); if (sn) info.calle = sn; } // (its doors, windows and mouldings as seen)
    const swm = style === 'nave' && seenMuros(b.id);
    if (swm) { const s0 = lin('#c9cdce'); info.muros = {}; for (const [k, hx] of Object.entries(swm)) { const w = lin(hx); info.muros[k] = [0, 1, 2].map((q) => Math.min(3, w[q] / s0[q])); } }
    if (hs) {
      if (hs.kind && STYLE_DEF[hs.kind]) info.style = hs.kind;
      // (bare brick and stone fronts in their own colour too — the old town's brick red, the newer quarters' buff and
      // ochre: tinted from the painted brick's and ashlar's own, textures.js paintWall)
      const base = STYLE_DEF[info.style].wall, own = base === 'brick' ? '#9a5839' : base === 'stone' ? '#b9ad98' : base;
      if (hs.wall && own && own[0] === '#') { const w = lin(hs.wall), s0 = lin(own); info.tint = [0, 1, 2].map((k) => Math.min(5, w[k] / s0[k])); }
      // (its wall another colour on its front to another street, as seen: calles_casas.js muros — by that street's name)
      // (one building of the map that is several houses: their paints left to right along its front, as seen — pinturas)
      if (hs.pinturas && own && own[0] === '#') { const s0 = lin(own); let m = 0; info.pinturas = hs.pinturas.map((q) => { m += q.m; const w = lin(q.hex); return { m, tint: [0, 1, 2].map((k) => Math.min(5, w[k] / s0[k])) }; }); }
      if (hs.muros && own && own[0] === '#') { const s0 = lin(own); info.muros = {}; for (const [k, hx] of Object.entries(hs.muros)) { const w = lin(hx); info.muros[k] = [0, 1, 2].map((q) => Math.min(5, w[q] / s0[q])); } }
      // (and no shop fronts just because the Catastro registers the ground floor as commercial: in the old town's
      // captures there are few shops; only a shop the map knows by name gets its front, below)
      info.shop = 0;
      if (hs.plinth === 'none') info.zoc = [0, 0, 0, ZOC_KINDS.ninguno * 10 + 0.01];
      else if (hs.plinth && ZOC_KINDS[hs.plinth.kind]) { const z = lin(hs.plinth.col || '#9a958e'); info.zoc = [z[0], z[1], z[2], ZOC_KINDS[hs.plinth.kind] * 10 + Math.min(3, Math.max(0.1, hs.plinth.h || 0.9))]; }
      info.calle = hs;
      // (its front read in the captures with no shop front on it — no T —: no shop, though the map knows one there)
      const fzAll = hs.fachadas ? Object.values(hs.fachadas) : hs.fachada ? [hs.fachada] : [];
      if (fzAll.length && !fzAll.some((f) => /T/.test(f.pb || ''))) info.noShop = true;
      // a row of terraced houses (adosados) that the map has as one long building: each house of it its own paint and
      // plinth from its street's (calles.js adosados — the newer quarters' promotions of the 70s to the 2000s), the
      // first the one seen, if it was
      const S = CALLES[streets[b.id]];
      if (S && S.adosados && (b.floors || 2) <= 3 && base && base[0] === '#') {
        const s0 = lin(base), paints = (S.walls || []).filter((w) => !w[2]).map((w) => lin(w[0]).map((v, k) => Math.min(5, v / s0[k])));
        const zocs = (S.plinth || []).map((z) => (z.kind && ZOC_KINDS[z.kind] ? [...lin(z.col || '#9a958e'), ZOC_KINDS[z.kind] * 10 + Math.min(3, Math.max(0.1, z.h || 0.9))] : [0, 0, 0, ZOC_KINDS.ninguno * 10 + 0.01]));
        if (paints.length > 1) info.hilera = { w: S.adosados.w || 6.5, paints, zocs, first: [info.tint, info.zoc || null] };
      }
    }
    // a roof of corrugated sheet in its colour, as seen (calles_casas.js cubierta: the red sheds — una, one slope down to
    // the street), tinted from the sheet's own grey (textures.js paintRoof 'chapa'); a third darker than the colour read
    // off a wall, as a slope open to the whole sky and the sun takes more light than a front (it came out pink)
    // (its tiles as seen — the old ones gone grey or brown —: tinted from the tile texture's own red, a fifth darker as
    // the sheet's above, a slope taking more light than a front)
    const tj = seenTile(b.id);
    if (tj) { const w = lin(tj), s0 = lin('#a5512f'); info.roofTint = [0, 1, 2].map((k) => Math.min(3, (0.8 * w[k]) / s0[k])); }
    const cub = seenRoof(b.id);
    if (cub) { const w = lin(cub.col), s0 = lin(CHAPA); info.cubierta = { ...cub, tint: [0, 1, 2].map((k) => Math.min(3, (0.68 * w[k]) / s0[k])) }; }
    // the whitewash peeling off, as seen or as its street has it (calles.js peel): for the wall's shader, in the hundreds
    // of the plinth's attribute (materials.js)
    const pk = (hs && hs.peel) || seenPeel(b.id);
    if (pk) { const z = info.zoc || ZOC0; info.zoc = [z[0], z[1], z[2], z[3] + pk * 100]; }
    // a block on its arcade (soportal, calles_casas.js): its street fronts' ground floor set back behind pillars (below)
    if (hs && hs.soportal) info.soportal = hs.soportal;
    const ov = overrides && overrides.get(b.id);
    if (ov) Object.assign(info, ov);
    // a measured house: its walls take the paint of its front (sides and back too)
    const ms = measured && measured.byB.get(b.id);
    if (ms) { info.measured = ms; info.style = 'color'; info.tint = lin(ms[0].spec.side || ms[0].spec.wall); info.noShop = true; info.shop = 0; }
    return info;
  });
  for (const p of shopPoi) {
    const b = map.buildingAt(p.x, p.z) || nearestBuilding(map, p.x, p.z, 6);
    if (b && !bInfo[b.id].noShop) bInfo[b.id].shop = 1; // (a public building with its own front: no shop fronts)
  }
  // ---- part heights
  const partIndex = new PolyIndex(map.bounds.x0 - 400, map.bounds.z0 - 400, map.bounds.x1 + 400, map.bounds.z1 + 400, 16);
  const parts = [];
  // (a house seen in the captures stands as many storeys as are seen there: its tallest parts so, the rest no taller)
  const topF = new Float32Array(map.buildings.length);
  for (const p of map.parts) if (p.b >= 0) topF[p.b] = Math.max(topF[p.b], p.floors);
  for (const p of map.parts) {
    if (skipPart && skipPart(p)) continue;
    const bi = p.b >= 0 ? bInfo[p.b] : null, sf = p.b >= 0 ? seenFloors(p.b) : 0;
    const fl = sf ? (p.floors >= topF[p.b] || (bi && bi.soportal) ? sf : Math.min(p.floors, sf)) : p.floors; // (a block on its arcade: all of it as seen — the Catastro leaves the open ground floor out of most of its parts)
    let H = Math.max(fl, bi ? bi.minFloors : 0) * FLOOR_H;
    if (bi && bi.style === 'nave') {
      const big = Math.sqrt(p.area);
      H = Math.max(H, 4.2 + Math.min(4, big * 0.12) + (hash1(p.id) - 0.5));
    }
    if (bi && bi.cubierta && bi.cubierta.alto) H = bi.cubierta.alto; // (a shed's walls as high as seen)
    const ht = p.b >= 0 ? seenHeight(p.b) : 0;
    if (ht) H = ht; // (a house's walls as high as seen, every part of it: calles_casas.js alto)
    if (p.alto) H = p.alto; // (or this part of it, where it is two of different heights: calles_casas.js partir)
    const mp = measured && measured.parts.get(p.id); // (a measured part: its real height and roof)
    if (mp && mp.H) H = mp.H;
    const part = { ...p, H, info: bi || { style: 'renovada', tint: [1, 1, 1], roofTint: [1, 1, 1], seed: hash1(p.id), shop: 0, rnd: mulberry32(p.id), pitch: 0.5 } };
    if (mp) part.roofSpec = mp;
    if (p.filler) part.roofSpec = { roof: 'flat', parapet: 0 };
    part.pi = partIndex.add(p.ring, part);
    parts.push(part);
  }
  // (a house whose street front was read bay by bay in its captures — calles.js fachada —: on its largest part)
  for (const q of parts) {
    const bi = q.b >= 0 ? bInfo[q.b] : null;
    if (!bi || !bi.calle || !bi.calle.fachada || q.filler) continue;
    if (bi.mainPart == null || q.area > bi.mainArea) { bi.mainPart = q.id; bi.mainArea = q.area; }
  }
  // the pieces of wall that close a crack between two houses (solidez.js fillCracks): as tall as the lower of the two
  // (twice over: a piece may stand between a house and another piece)
  const byId = new Map(parts.map((q) => [q.id, q]));
  for (let it = 0; it < 2; it++) for (const q of parts) {
    if (!q.filler) continue;
    const hs = q.between.map((id) => byId.get(id)).filter(Boolean).map((o) => o.H);
    if (hs.length) q.H = Math.max(2.4, Math.min(...hs));
  }
  // collisions: what stands is what is drawn — each part to its own height. A building's Catastro outline can be larger
  // than its parts (a petrol station's canopy, a porch, a yard registered with it): walls nobody can see stop nobody
  const bH = new Float32Array(map.buildings.length);
  for (const p of parts) if (p.b >= 0) bH[p.b] = Math.max(bH[p.b], p.H + 1.5);
  const kept = new Uint8Array(map.buildings.length);
  for (const b of map.buildings) {
    if (onBuilding && onBuilding(b) === false) continue;
    kept[b.id] = 1;
    b.height = bH[b.id] || b.floors * FLOOR_H;
  }
  // (the walls themselves go in once each roof is built: they stand as high as its ridge, so the camera, a bullet or a
  // thrown thing never ends up inside a roof)
  map.useDrawnParts(parts.filter((p) => p.b < 0 || kept[p.b]));

  // does a facade run look onto a street or a square? (backyards and inner courtyards keep the light painted facade)
  const squares = map.areas.filter((a) => ['place:square', 'highway:pedestrian', 'amenity:marketplace', 'leisure:park'].includes(a.kind)).map((a) => ({ ring: a.ring, bb: ringBounds(a.ring) }));
  const streetFacing = (run) => {
    const tm = (run.t0 + run.t1) / 2;
    const mx = run.ax + run.dx * tm, mz = run.az + run.dz * tm;
    for (const off of [2.2, 5.5, 9.5]) {
      const px = mx + run.nx * off, pz = mz + run.nz * off;
      if (off > 3 && map.buildingAt(px, pz)) return false;
      for (const id of map.edgesNear(px, pz, 4)) {
        const e = map.edges[id];
        if (!(e.walk || e.drive) || e.cls === 'track' || e.dirt) continue;
        if (polyNearest(e.pts, e.cum, px, pz).d < 2.5 + e.w / 2) return true;
      }
      for (const sq of squares) if (px > sq.bb[0] && px < sq.bb[2] && pz > sq.bb[1] && pz < sq.bb[3] && pointInRing(px, pz, sq.ring)) return true;
    }
    return false;
  };
  // the name of the street a run looks onto (the first street found straight out from its middle)
  const streetNameOf = (run) => {
    const tm = (run.t0 + run.t1) / 2, mx = run.ax + run.dx * tm, mz = run.az + run.dz * tm;
    for (const off of [2.2, 5.5, 9.5]) {
      const px = mx + run.nx * off, pz = mz + run.nz * off;
      for (const id of map.edgesNear(px, pz, 4)) {
        const e = map.edges[id];
        if ((e.walk || e.drive) && e.name && polyNearest(e.pts, e.cum, px, pz).d < 2.5 + e.w / 2) return e.name;
      }
    }
    return '';
  };
  let tris = 0;
  const sharp = map.sharedCorner || null; // (corners two houses share: never rounded, solidez.js)
  for (const p of parts) {
    const info = p.info;
    const c = chunkOf(p.c[0], p.c[1]);
    c.zocNow = info.zoc || ZOC0;
    const H = p.H;
    const rings = [p.ring].concat(p.holes || []);
    // (claymation: the walls follow the outline with its corners rounded, as a clay model's — the roof keeps the true
    // outline, its eaves cover the difference; what stops you, the colliders, too)
    const smooths = LOOK.plastilina && !p.filler ? [] : null; // (a piece of wall closing a slot: square, flush with both)
    if (smooths) for (let ri = 0; ri < rings.length; ri++) { const rr = roundRing(rings[ri], sharp); rings[ri] = rr.pts; smooths[ri] = rr.nrm; }
    // ---------------- walls
    // Each edge is hidden where a neighbour part stands right behind it (coverOf: exactly as far as it reaches, up to
    // its own height), so a party wall is drawn nowhere it would be seen through, and left open nowhere.
    const runs = [];
    for (let ri = 0; ri < rings.length; ri++) {
      const r = rings[ri];
      const n = r.length / 2;
      // (claymation) the ring's convex corners — the building's own corners, rounded like a clay model's
      const convex = LOOK.plastilina && !p.filler ? new Uint8Array(n) : null;
      if (convex) for (let i = 0; i < n; i++) {
        const h = (i - 1 + n) % n, j = (i + 1) % n;
        const e0x = r[i * 2] - r[h * 2], e0z = r[i * 2 + 1] - r[h * 2 + 1], e1x = r[j * 2] - r[i * 2], e1z = r[j * 2 + 1] - r[i * 2 + 1];
        const l0 = Math.hypot(e0x, e0z), l1 = Math.hypot(e1x, e1z);
        convex[i] = l0 > 0.05 && l1 > 0.05 && (e0x * e1z - e0z * e1x) / (l0 * l1) > 0.85 && !(sharp && sharp(r[i * 2], r[i * 2 + 1])) ? 1 : 0; // (a sharp corner left: the shader rounds it)
      }
      // (claymation) the normal at each vertex of a rounded corner: its curve's own (NaN where the outline is straight)
      const vN = smooths ? smooths[ri] : null;
      for (let i = 0; i < n; i++) {
        const j = (i + 1) % n;
        const ax = r[i * 2], az = r[i * 2 + 1], bx = r[j * 2], bz = r[j * 2 + 1];
        const dx = bx - ax, dz = bz - az;
        const L = Math.hypot(dx, dz);
        if (L < 0.05) continue;
        const nx = dz / L, nz = -dx / L; // outward
        const uTot = L < 1.8 ? 0.3 : Math.max(1, Math.round(L / BAY_W));
        const emit = (t0, t1, cy) => {
          if (cy >= H - 0.05) return; // fully hidden behind a taller neighbour
          const run = { ax, az, dx, dz, L, nx, nz, uTot, t0, t1, cy, ri, exposed: cy === 0 };
          if (convex) run.code = L + (t0 < 1e-6 && convex[i] ? 1e4 : 0) + (t1 > 1 - 1e-6 && convex[j] ? 2e4 : 0);
          if (vN) { // the normals at the run's two ends (smoothed where the outline bends round a corner)
            const sA = isNaN(vN[i * 2]) ? [nx, nz] : [vN[i * 2], vN[i * 2 + 1]], sB = isNaN(vN[j * 2]) ? [nx, nz] : [vN[j * 2], vN[j * 2 + 1]];
            const at = (t) => { const x = sA[0] + (sB[0] - sA[0]) * t, z = sA[1] + (sB[1] - sA[1]) * t, l = Math.hypot(x, z) || 1; return [x / l, 0, z / l]; };
            run.nrmAt = at;
          }
          if (run.exposed) { run.street = streetFacing(run) || !!(info.calle && info.calle.todas_fachadas); run.exposed = run.street; run.back = !run.street; } // (todas_fachadas: a house onto open ground, every wall a front)
          // a wall measured from the photographs: its own holes and paint (fachadas.js)
          if (info.measured && ri === 0) { run.mf = matchRun(info.measured, run); if (run.mf) { run.exposed = true; run.street = true; run.back = false; } }
          // a block on its arcade (soportal): along a street front its ground floor stands back behind square pillars, as
          // deep as seen where the part is deep enough (one of the block's thin slabs, a balcony's strip, keeps its wall)
          if (info.soportal && run.street && !run.mf && ri === 0 && cy === 0 && !p.filler && H >= 2 * FLOOR_H - 0.05 && (t1 - t0) * L >= 3.5) markArcade(run, p.ring, info.soportal);
          runs.push(run);
          const D = run.arcade ? run.arcade.D : 0; // (its contact shade at the foot of the wall behind the arcade)
          if (cy === 0 && ri === 0 && (t1 - t0) * L > 1) ao.push(ax + dx * t0 - nx * D, az + dz * t0 - nz * D, ax + dx * t1 - nx * D, az + dz * t1 - nz * D, nx, nz);
        };
        // what stands behind the wall, exactly: the pieces of it (t0..t1) with the height that hides them
        for (const [t0, t1, cy] of coverOf(partIndex, p, ax, az, dx, dz, nx, nz, L, H)) emit(t0, t1, cy);
      }
    }
    // (its street front as seen: the longest wall of its main part to the street, whole, cut in as many bays as the
    // captures show openings — each a bay's width within reason; facades.js planPart lays them)
    // (each front read in the captures — a corner house, one to each street: calles_casas.js fachadas — on the wall to
    // its street; one whose street the walls do not match, as before, on the longest still free)
    const fzs = info.calle && (info.calle.fachadas || (info.calle.fachada ? { [info.calle.frente || '']: info.calle.fachada } : null));
    if (fzs && info.mainPart === p.id) {
      const used = new Set();
      for (const [frente, fz] of Object.entries(fzs)) {
        let main = null, mainOn = false;
        for (const r of runs) {
          if (used.has(r) || !(r.street && r.ri === 0 && r.cy === 0 && !r.mf && r.t0 < 1e-6 && r.t1 > 1 - 1e-6)) continue;
          const on = !!frente && streetNameOf(r) === frente;
          if (!main || (on && !mainOn) || (on === mainOn && r.L > main.L)) { main = r; mainOn = on; }
        }
        let nb = Math.max(...Object.values(fz).map((v) => v.length)), f2 = fz;
        // (read finer than its wall takes — bays under 1.4 m —: neighbouring bays taken together, a door or a garage
        // before a window and a window before blank wall; much finer than that, it was read on another wall)
        if (main && main.L / nb < 1.4 && main.L / nb >= 0.6) { nb = Math.max(1, Math.floor(main.L / 1.4)); f2 = squeezeFront(fz, nb); }
        // (and up to 8 m a bay: a shed's front read as its few garage doors along its whole wall)
        if (main && main.L / nb >= 1.4 && main.L / nb <= (info.style === 'nave' ? 8 : 6.5)) { main.uTot = nb; main.fachada = f2; used.add(main); }
      }
    }
    // (a front in its own colour where it looks onto the street named — a side wall over a lot as well)
    if (info.muros) for (const r of runs) if (r.ri === 0 && !r.mf) { const t = info.muros[streetNameOf(r)]; if (t) r.tint = t; }
    if (info.pinturas) { // (on its front to its street: the longest wall that looks onto it)
      const own = info.calle.frente || info.calle.street;
      let best = null;
      for (const r of runs) if (r.street && r.ri === 0 && !r.mf && r.cy === 0 && (!best || r.L * (r.t1 - r.t0) > best.L * (best.t1 - best.t0)) && (!own || streetNameOf(r) === own)) best = r;
      if (best) best.pint = info.pinturas;
    }
    if (!p.filler) planPart(p, info, runs, H, facade && facade.forcedDoors); // (a filler: plain wall, no doors)
    for (const run of runs) tris += emitRun(c, run, p, info, H, facade);
    if (info.calle && (info.calle.pilastras || info.calle.impostas || info.calle.cornisa)) for (const run of runs) if (run.street && run.ri === 0 && !run.mf && (run.t1 - run.t0) * run.L > 1.5) tris += bands(c, run, info, H);
    // ---------------- roof
    tris += buildRoof(c, p, info, H, runs);
    if (p.b < 0 || kept[p.b]) {
      const hc = Math.max(H + 1.5, (p.top || H) + 0.4);
      const arcs = runs.filter((q) => q.arcade);
      if (arcs.length) p.walkRing = arcadeCollider(map.collider, p.ring, arcs, hc, p.b); // (open under its arcades, its pillars in the way)
      else map.collider.addRing(p.ring, hc, p.b);
      if (p.holes) for (const h of p.holes) map.collider.addRing(h, hc, p.b);
    }
    // runs for the 3D extras (downpipes, cornices)
    if (facade && facade.runs && info.style !== 'nave' && !p.filler) {
      for (const run of runs) {
        if (!run.exposed || run.ri !== 0 || (run.t1 - run.t0) * run.L < 1.5) continue;
        const shopEnds = !!info.shop;
        facade.runs.push({
          ax: run.ax + run.dx * run.t0, az: run.az + run.dz * run.t0, bx: run.ax + run.dx * run.t1, bz: run.az + run.dz * run.t1,
          nx: run.nx, nz: run.nz, H, pitched: p.roofKind === 'hip' || p.roofKind === 'lip', shopEnds,
          style: info.style, tint: info.tint, bid: p.b, pid: p.id, seed: info.seed, measured: !!run.mf, calle: info.calle || null, arcade: run.arcade ? run.arcade.D : 0,
          front: info.calle && (info.calle.rotulo || info.calle.cerramiento) ? streetNameOf(run) : undefined, // (the street it looks onto: detalles.js, tapias.js)
        });
      }
    }
  }
  // (and once the arcades are known, what is inside a building again: without them — mapdata.js)
  if (parts.some((p) => p.walkRing)) map.useDrawnParts(parts.filter((p) => p.b < 0 || kept[p.b]));
  const meshes = [];
  for (const [k, ch] of chunks) {
    if (!ch.vcount) continue;
    meshes.push(ch.geometry());
  }
  return { geometries: meshes, ao, parts, tris };
}

// One wall run: party walls are a single blank quad; street facades are split in cells (bay x floor) with the layer
// chosen by planPart. Cells holding a door, window, balcony, garage or shop get a real hole when facade.holes is on.
function emitRun(c, run, p, info, H, facade) {
  if (!run.tint) return emitRun0(c, run, p, info, H, facade);
  const t = info.tint; info.tint = run.tint; // (this front in its own colour: info.muros)
  try { return emitRun0(c, run, p, info, H, facade); } finally { info.tint = t; }
}
function emitRun0(c, run, p, info, H, facade) {
  if (run.mf) return emitMeasuredRun(c, run, p, info, H, facade);
  const { ax, az, dx, dz, nx, nz, uTot, t0, t1, cy } = run;
  const sBase = STYLE[info.style];
  if (!run.exposed) {
    // party walls: blank (kind 2); backyard / courtyard facades: painted cells picked in the shader (kind 3), one quad
    const x0 = ax + dx * t0, z0 = az + dz * t0, x1 = ax + dx * t1, z1 = az + dz * t1;
    c.quad(x0, cy, z0, x1, cy, z1, x1, H, z1, x0, H, z0, nx, 0, nz, uTot * t0, cy / FLOOR_H, uTot * t1, H / FLOOR_H, [sBase, run.back ? 3 : 2, info.seed, 0], info.tint, NORECT, H, null, run.code ? [t0 * run.L, t1 * run.L, run.code] : null, run.nrmAt ? [run.nrmAt(t0), run.nrmAt(t1)] : null);
    return 2;
  }
  const u0 = uTot * t0, u1 = uTot * t1;
  const nF = Math.floor(H / FLOOR_H + 0.02);
  const holes = !!(facade && facade.holes && styleHasHoles(info.style));
  const at = (u) => [ax + dx * (u / uTot), az + dz * (u / uTot)], at0 = at;
  let tris = 0;
  // every piece overlaps its neighbours by 4 mm: the texture mapping is continuous, so the overlap is invisible,
  // and it seals the T-junction cracks that otherwise sparkle around the holes
  const eu = 0.004 * uTot / run.L, ev = 0.004 / FLOOR_H;
  const piece = (ua, ub, ya, yb, layer, rect) => {
    ua -= eu; ub += eu; ya = Math.max(0, ya - ev * FLOOR_H); yb += ev * FLOOR_H;
    const [x0, z0] = at(ua), [x1, z1] = at(ub);
    c.quad(x0, ya, z0, x1, ya, z1, x1, yb, z1, x0, yb, z0, nx, 0, nz, ua, ya / FLOOR_H, ub, yb / FLOOR_H, [layer, 0, info.seed, 0], info.tint, rect, H, null, run.code ? [(ua / uTot) * run.L, (ub / uTot) * run.L, run.code] : null, run.nrmAt ? [run.nrmAt(ua / uTot), run.nrmAt(ub / uTot)] : null);
    tris += 2;
  };
  const piece0 = piece;
  // (on its arcade: the ground floor's cells on the wall behind the pillars, as they would be on the front — markArcade)
  const A = run.arcade, D = A ? A.D : 0;
  const atA = A ? (u) => { const q = at(u); return [q[0] - nx * D, q[1] - nz * D]; } : at;
  const pieceA = A ? (ua, ub, ya, yb, layer, rect) => {
    ua -= eu; ub += eu; ya = Math.max(0, ya - ev * FLOOR_H); yb += ev * FLOOR_H;
    const [x0, z0] = atA(ua), [x1, z1] = atA(ub);
    c.quad(x0, ya, z0, x1, ya, z1, x1, yb, z1, x0, yb, z0, nx, 0, nz, ua, ya / FLOOR_H, ub, yb / FLOOR_H, [layer, 0, info.seed, 0], info.tint, rect, H);
    tris += 2;
  } : piece;
  // (a row of terraced houses, the map's one building: each house's own paint and plinth, a whole number of bays wide)
  const row = info.hilera && run.street && run.L >= 14 ? info.hilera : null, hb = row ? Math.max(1, Math.round(row.w / (run.L / uTot))) : 0;
  const tint0 = info.tint, zoc0 = c.zocNow;
  for (let b = Math.floor(u0 + 1e-6); b < u1 - 1e-6; b++) {
    const ua = Math.max(u0, b), ub = Math.min(u1, b + 1);
    if (ub - ua < 1e-4) continue;
    if (row) {
      const k = Math.floor(b / hb), h = (x) => { const v = Math.sin(x) * 43758.5453; return v - Math.floor(v); };
      if (k === 0) { info.tint = tint0; c.zocNow = zoc0; }
      else {
        info.tint = row.paints[Math.floor(h(k * 12.9898 + info.seed * 78.233 + run.ax * 0.071) * row.paints.length)];
        if (row.zocs.length) c.zocNow = row.zocs[Math.floor(h(k * 7.233 + info.seed * 31.7 + run.az * 0.053) * row.zocs.length)];
      }
    }
    if (run.pint) { // (its house's paint where this bay stands, metres from the front's left end as seen from the street)
      const m = (1 - (ua + ub) / 2 / uTot) * run.L, q = run.pint.find((o) => m <= o.m) || run.pint[run.pint.length - 1];
      info.tint = q.tint;
    }
    const complete = uTot >= 1 && ua - b < 1e-4 && b + 1 - ub < 1e-4;
    let lit = null; // (the ground floor behind an arcade is in its shade: a darker paint and plinth while it is laid)
    for (let f = 0; f < nF; f++) {
      if (A && f === 0) { lit = [info.tint, c.zocNow]; info.tint = shade(info.tint, ARC_SHADE); c.zocNow = shadeZoc(c.zocNow, ARC_SHADE); }
      else if (lit && f === 1) { info.tint = lit[0]; c.zocNow = lit[1]; lit = null; }
      const ya = f * FLOOR_H, yb = ya + FLOOR_H;
      const plain = sBase + (f === 0 ? CT.BLANK_G : CT.BLANK_U);
      const type = complete && run.cells ? run.cells.get(b * 64 + f) : undefined;
      const at = f === 0 ? atA : at0, piece = f === 0 ? pieceA : piece0; // (the ground floor behind its arcade, if it has one)
      if (type === undefined || type === CT.BLANK_G || type === CT.BLANK_U) { piece(ua, ub, ya, yb, plain, NORECT); continue; }
      const rect = holeRect(type, info.style, f > 0);
      // ground-floor doors, garages and shop fronts are recorded whatever the quality (street props, neighbours, markers)
      if (f === 0 && facade && facade.ground && (type === CT.DOOR || type === CT.GARAGE || type === CT.SHOP) && info.style !== 'nave') {
        const bw = run.L / uTot;
        const rr = rect || [0.3, 0, 0.7, 0.74];
        const [wx, wz] = at(b + (rr[0] + rr[2]) / 2);
        facade.ground.push({ x: wx, z: wz, nx, nz, r: ((rr[2] - rr[0]) * bw) / 2 + 0.35, type, bid: p.b, style: info.style, calle: info.calle || null });
      }
      // (claymation: the ground-floor windows too, for the pots set out under them — the user's pictures)
      if (LOOK.plastilina && f === 0 && facade && type === CT.WIN_G && info.style !== 'nave') {
        const bw = run.L / uTot, rr = rect || [0.3, 0.3, 0.7, 0.8], [wx, wz] = at(b + (rr[0] + rr[2]) / 2);
        (facade.groundWin || (facade.groundWin = [])).push({ x: wx, z: wz, nx, nz, w: (rr[2] - rr[0]) * bw, calle: info.calle || null });
      }
      if (!holes || !rect) { piece(ua, ub, ya, yb, sBase + type, rect || NORECT); continue; }
      tris += emitHoleCell(c, run, at, piece, b, f, type, rect, p, info, sBase, H, nF, facade);
    }
    if (lit) { info.tint = lit[0]; c.zocNow = lit[1]; lit = null; }
    if (H - nF * FLOOR_H > 0.02) piece(ua, ub, nF * FLOOR_H, H, sBase + CT.BLANK_U, NORECT);
  }
  info.tint = tint0; c.zocNow = zoc0;
  if (A) tris += arcadeShell(c, run, at, info, sBase, H);
  return tris;
}

// ---------------------------------------------------------------- bands (calles.js pilastras, impostas, cornisa)
// The painted mouldings a front is framed with in its captures: a pilaster at each end of the wall (35 cm, 3 cm proud),
// a string course at each floor line (18 cm) and a cornice band along the top (26 cm, 6 cm proud) — each in its colour,
// as a tint of the wall's own plain plaster.
function bands(c, run, info, H) {
  const { ax, az, dx, dz, nx, nz, t0, t1, L } = run, cs = info.calle, sBase = STYLE[info.style];
  const base = STYLE_DEF[info.style].wall, b0 = base && base[0] === '#' ? lin(base) : [0.85, 0.83, 0.8];
  const tintOf = (hex) => { const w = lin(hex); return [0, 1, 2].map((k) => Math.min(4, w[k] / Math.max(0.02, b0[k]))); };
  const x0 = ax + dx * t0, z0 = az + dz * t0, x1 = ax + dx * t1, z1 = az + dz * t1, len = (t1 - t0) * L, tx = dx / L, tz = dz / L;
  const tex = [sBase + CT.BLANK_U, 0, info.seed, 0], zoc = c.zocNow;
  c.zocNow = ZOC0; // (a band is not its plinth)
  let tris = 0;
  // a slab proud of the wall from a to b along it (distances from the run's start), y0..y1, out by o: its front and sides
  const slab = (sa, sb, y0, y1, o, tint) => {
    const A = [x0 + tx * sa, z0 + tz * sa], B = [x0 + tx * sb, z0 + tz * sb];
    c.quad(A[0] + nx * o, y0, A[1] + nz * o, B[0] + nx * o, y0, B[1] + nz * o, B[0] + nx * o, y1, B[1] + nz * o, A[0] + nx * o, y1, A[1] + nz * o, nx, 0, nz, sa / BAY_W, 1.02, sb / BAY_W, 1.06, tex, tint);
    c.quad(A[0], y0, A[1], A[0] + nx * o, y0, A[1] + nz * o, A[0] + nx * o, y1, A[1] + nz * o, A[0], y1, A[1], -tx, 0, -tz, 0, 1.02, 0.02, 1.06, tex, tint);
    c.quad(B[0] + nx * o, y0, B[1] + nz * o, B[0], y0, B[1], B[0], y1, B[1], B[0] + nx * o, y1, B[1] + nz * o, tx, 0, tz, 0, 1.02, 0.02, 1.06, tex, tint);
    c.quad(A[0], y1, A[1], B[0], y1, B[1], B[0] + nx * o, y1, B[1] + nz * o, A[0] + nx * o, y1, A[1] + nz * o, 0, 1, 0, 0, 1.02, 0.02, 1.06, tex, tint);
    tris += 8;
  };
  if (cs.pilastras) { const t = tintOf(cs.pilastras); slab(0, 0.35, 0, H, 0.03, t); slab(len - 0.35, len, 0, H, 0.03, t); }
  if (cs.impostas) { const t = tintOf(cs.impostas); for (let f = 1; f * FLOOR_H < H - 0.5; f++) slab(0, len, f * FLOOR_H - 0.09, f * FLOOR_H + 0.09, 0.025, t); }
  if (cs.cornisa) slab(-0.04, len + 0.04, H - 0.26, H, 0.06, tintOf(cs.cornisa));
  c.zocNow = zoc;
  return tris;
}

// ---------------------------------------------------------------- arcades (soportales)
// A street front of a block on its arcade (calles_casas.js soportal: the blocks of flats of 1983 in Gerardo Diego and
// Miguel Hernández): its ground floor stands D back behind square pillars, one at each end and one at every bay between
// (3.2 m, as there), under the first floor's underside; the pillars and the wall behind take the house's plinth paint as
// high as seen (terracotta, ochre). Only where the part is deep enough behind it for a room: the wall, otherwise.
function markArcade(run, ring, sp) {
  const D = Math.min(sp.fondo || 2.5, depthBehind(ring, run) - 1.5);
  if (!(D >= 1.5)) return;
  const u0 = run.uTot * run.t0, u1 = run.uTot * run.t1, hu = 0.21 / (run.L / run.uTot), pillars = [u0 + hu];
  for (let b = Math.ceil(u0 + 0.35); b < u1 - 0.35; b++) pillars.push(b);
  pillars.push(u1 - hu);
  run.arcade = { D, pillars, arcos: !!sp.arcos }; // (arcos: round arches from pillar to pillar, as seen)
}
// how deep the part is behind the middle of a wall: to the first wall the line straight in meets
function depthBehind(ring, run) {
  const tm = (run.t0 + run.t1) / 2, mx = run.ax + run.dx * tm - run.nx * 0.02, mz = run.az + run.dz * tm - run.nz * 0.02;
  const n = ring.length / 2, rx = -run.nx, rz = -run.nz;
  let best = 99;
  for (let i = 0; i < n; i++) {
    const j = (i + 1) % n, ax = ring[i * 2], az = ring[i * 2 + 1], ex = ring[j * 2] - ax, ez = ring[j * 2 + 1] - az;
    const den = rx * ez - rz * ex;
    if (Math.abs(den) < 1e-9) continue;
    const t = ((ax - mx) * ez - (az - mz) * ex) / den, u = ((ax - mx) * rz - (az - mz) * rx) / den;
    if (t > 0.05 && u >= 0 && u <= 1 && t < best) best = t;
  }
  return best;
}
// the arcade itself: its pillars, the first floor's underside over it, and its two ends closed
function arcadeShell(c, run, at, info, sBase, H) {
  const { nx, nz, uTot, t0, t1, L } = run, D = run.arcade.D, bw = L / uTot, tx = run.dx / L, tz = run.dz / L;
  const u0 = uTot * t0, u1 = uTot * t1, y1 = FLOOR_H, hp = 0.21, hu = hp / bw;
  const texG = [sBase + CT.BLANK_G, 0, info.seed, 0], texU = [sBase + CT.BLANK_U, 0, info.seed, 0];
  let tris = 0;
  const z0 = c.zocNow, faceShade = [1, 0.8, ARC_SHADE, 0.8]; // (front, side, back — under the arcade —, side)
  for (const u of run.arcade.pillars) {
    const [px, pz] = at(u), cx = px - nx * hp, cz = pz - nz * hp;
    const k = [[-1, 1], [1, 1], [1, -1], [-1, -1]].map(([a, b]) => [cx + tx * hp * a + nx * hp * b, cz + tz * hp * a + nz * hp * b]);
    [[k[0], k[1], nx, nz], [k[1], k[2], tx, tz], [k[2], k[3], -nx, -nz], [k[3], k[0], -tx, -tz]].forEach(([a, b, fx, fz], i) => {
      c.zocNow = shadeZoc(z0, faceShade[i]);
      c.quad(a[0], 0, a[1], b[0], 0, b[1], b[0], y1, b[1], a[0], y1, a[1], fx, 0, fz, u - hu, 0, u + hu, 0.995, texG, shade(info.tint, faceShade[i]), NORECT, H);
      tris += 2;
    });
  }
  // (round arches from pillar to pillar: the wall over each in the front's plane, down to its curve — a half circle where
  // the floor is high enough, flattened where not — and its soffit, as deep as the pillars)
  if (run.arcade.arcos) {
    const P = run.arcade.pillars, top = y1 - 0.12, deep = 2 * hp;
    for (let i = 0; i + 1 < P.length; i++) {
      const ua = P[i] + hu, ub = P[i + 1] - hu, w = (ub - ua) * bw;
      if (w < 0.8) continue;
      const ry = Math.min(w / 2, top - 1.9), spring = top - ry, N = 12;
      const pt = (k) => { const a = Math.PI * (1 - k / N); return [ua + ((1 + Math.cos(a)) / 2) * (ub - ua), spring + Math.sin(a) * ry]; };
      c.zocNow = z0;
      for (let k = 0; k < N; k++) {
        const [u, y] = pt(k), [u2, y2] = pt(k + 1), [x, z] = at(u), [x2, z2] = at(u2);
        c.quad(x, y, z, x2, y2, z2, x2, y1, z2, x, y1, z, nx, 0, nz, u, y / FLOOR_H, u2, 0.995, texG, info.tint, NORECT, H);
        const sx = x - nx * deep, sz = z - nz * deep, sx2 = x2 - nx * deep, sz2 = z2 - nz * deep; // (its soffit, facing in and down)
        c.quad(x2, y2, z2, x, y, z, sx, y, sz, sx2, y2, sz2, 0, -1, 0, u, 0.9, u2, 0.95, texG, shade(info.tint, 0.75), NORECT, H);
        tris += 4;
      }
      // (and the springing: the wall from the pillar's side down to the arch's foot is the pillar itself — nothing to add)
    }
  }
  const [ax, az] = at(u0), [bx, bz] = at(u1), tS = shade(info.tint, ARC_SHADE);
  c.zocNow = shadeZoc(z0, ARC_SHADE);
  c.quad(ax, y1, az, bx, y1, bz, bx - nx * D, y1, bz - nz * D, ax - nx * D, y1, az - nz * D, 0, -1, 0, u0, 1.02, u1, 1.02 + D / FLOOR_H, texU, shade(info.tint, 0.55), NORECT, H);
  c.quad(ax - nx * D, 0, az - nz * D, ax, 0, az, ax, y1, az, ax - nx * D, y1, az - nz * D, tx, 0, tz, u0 - D / bw, 0, u0, 0.995, texG, tS, NORECT, H);
  c.quad(bx, 0, bz, bx - nx * D, 0, bz - nz * D, bx - nx * D, y1, bz - nz * D, bx, y1, bz, -tx, 0, -tz, u1, 0, u1 + D / bw, 0.995, texG, tS, NORECT, H);
  c.zocNow = z0;
  return tris + 6;
}
// the arcade's shade: how much darker what stands under it is than what the sun and sky light outside (its paint, and
// its plinth's own colour, which the shader takes from the plinth attribute, not from the tint)
const ARC_SHADE = 0.62;
const shade = (t, k) => [t[0] * k, t[1] * k, t[2] * k];
const shadeZoc = (z, k) => [z[0] * k, z[1] * k, z[2] * k, z[3]];
// what stops you round a part with arcades: its outline open where each arcade's front is, the arcade's ends and the wall
// behind it, and its pillars. Returns the outline with the arcades cut out of it — what is "inside the building" for the
// rest of the game (mapdata.js useDrawnParts: the player is never taken out of an arcade as if trapped in a house)
function arcadeCollider(col, ring, arcs, hc, owner) {
  const n = ring.length / 2, out = [];
  for (let i = 0; i < n; i++) {
    const j = (i + 1) % n, ax = ring[i * 2], az = ring[i * 2 + 1], bx = ring[j * 2], bz = ring[j * 2 + 1];
    const L = Math.hypot(bx - ax, bz - az);
    out.push(ax, az);
    if (L < 1e-3) continue;
    const ux = (bx - ax) / L, uz = (bz - az) / L, cut = [];
    for (const q of arcs) {
      const x0 = q.ax + q.dx * q.t0, z0 = q.az + q.dz * q.t0, x1 = q.ax + q.dx * q.t1, z1 = q.az + q.dz * q.t1;
      if (Math.abs((x0 - ax) * -uz + (z0 - az) * ux) > 0.08 || Math.abs((x1 - ax) * -uz + (z1 - az) * ux) > 0.08) continue; // (not on this wall's line)
      let s0 = (x0 - ax) * ux + (z0 - az) * uz, s1 = (x1 - ax) * ux + (z1 - az) * uz;
      if (s0 > s1) { const t = s0; s0 = s1; s1 = t; }
      if (s1 > 0.01 && s0 < L - 0.01) cut.push([Math.max(0, s0), Math.min(L, s1), q]);
    }
    cut.sort((p, q) => p[0] - q[0]);
    let s = 0;
    for (const [c0, c1, q] of cut) {
      if (c0 > s + 0.01) col.addSegment(ax + ux * s, az + uz * s, ax + ux * c0, az + uz * c0, hc, owner);
      s = Math.max(s, c1);
      const D = q.arcade.D, A = [ax + ux * c0, az + uz * c0], B = [ax + ux * c1, az + uz * c1];
      if (c0 > 0.01) out.push(A[0], A[1]);
      out.push(A[0] - q.nx * D, A[1] - q.nz * D, B[0] - q.nx * D, B[1] - q.nz * D);
      if (c1 < L - 0.01) out.push(B[0], B[1]);
    }
    if (L > s + 0.01) col.addSegment(ax + ux * s, az + uz * s, bx, bz, hc, owner);
  }
  for (const q of arcs) {
    const D = q.arcade.D, at = (u) => [q.ax + q.dx * (u / q.uTot), q.az + q.dz * (u / q.uTot)];
    const [ax, az] = at(q.uTot * q.t0), [bx, bz] = at(q.uTot * q.t1);
    col.addSegment(ax, az, ax - q.nx * D, az - q.nz * D, hc, owner);
    col.addSegment(ax - q.nx * D, az - q.nz * D, bx - q.nx * D, bz - q.nz * D, hc, owner);
    col.addSegment(bx - q.nx * D, bz - q.nz * D, bx, bz, hc, owner);
    const tx = q.dx / q.L, tz = q.dz / q.L, hp = 0.21;
    for (const u of q.arcade.pillars) {
      const [px, pz] = at(u), cx = px - q.nx * hp, cz = pz - q.nz * hp, r = [];
      for (const [a, b] of [[-1, 1], [1, 1], [1, -1], [-1, -1]]) r.push(cx + tx * hp * a + q.nx * hp * b, cz + tz * hp * a + q.nz * hp * b);
      col.addRing(r, hc, owner);
    }
  }
  return out;
}

// wall around the hole, four plaster reveals with baked occlusion and the painted fill at the back
function emitHoleCell(c, run, at, piece, b, f, type, rect, p, info, sBase, H, nF, facade) {
  const { nx, nz, L, uTot } = run;
  const bw = L / uTot;
  const [rx0, ry0, rx1, ry1] = rect;
  const ya = f * FLOOR_H, yb = ya + FLOOR_H;
  const plain = sBase + (f === 0 ? CT.BLANK_G : CT.BLANK_U);
  const D = recessDepth(info.style, type, info.seed);
  const uL = b + rx0, uR = b + rx1;
  const yL = ya + ry0 * FLOOR_H, yT = ya + ry1 * FLOOR_H;
  piece(b, uL, ya, yb, plain, rect);
  piece(uR, b + 1, ya, yb, plain, rect);
  if (ry0 > 0.001) piece(uL, uR, ya, yL, plain, rect);
  piece(uL, uR, yT, yb, plain, rect);
  const T = info.tint;
  const [xl, zl] = at(uL), [xr, zr] = at(uR);
  const ix = -nx * D, iz = -nz * D;
  const tx = run.dx / L, tz = run.dz / L;
  const texP = [plain, 0, info.seed, 0];
  const dU = D / bw, dV = D / FLOOR_H;
  // jambs
  c.quad(xl, yL, zl, xl + ix, yL, zl + iz, xl + ix, yT, zl + iz, xl, yT, zl, tx, 0, tz, uL, yL / FLOOR_H, uL + dU, yT / FLOOR_H, texP, T, rect, H, [0.97, 0.7, 0.7, 0.97]);
  c.quad(xr, yL, zr, xr + ix, yL, zr + iz, xr + ix, yT, zr + iz, xr, yT, zr, -tx, 0, -tz, uR, yL / FLOOR_H, uR + dU, yT / FLOOR_H, texP, T, rect, H, [0.97, 0.7, 0.7, 0.97]);
  // lintel soffit
  c.quad(xl, yT, zl, xr, yT, zr, xr + ix, yT, zr + iz, xl + ix, yT, zl + iz, 0, -1, 0, uL, yT / FLOOR_H, uR, yT / FLOOR_H + dV, texP, T, rect, H, [0.86, 0.86, 0.6, 0.6]);
  // sill / threshold
  const yS = ry0 > 0.001 ? yL : 0.012;
  c.quad(xl, yS, zl, xr, yS, zr, xr + ix, yS, zr + iz, xl + ix, yS, zl + iz, 0, 1, 0, uL, yS / FLOOR_H, uR, yS / FLOOR_H + dV, texP, T, rect, H, [1, 1, 0.78, 0.78]);
  // painted fill (what far houses show; near the camera the material turns it into glass / a dark hall)
  c.quad(xl + ix, yL, zl + iz, xr + ix, yL, zr + iz, xr + ix, yT, zr + iz, xl + ix, yT, zl + iz, nx, 0, nz, uL, f + ry0, uR, f + ry1, [sBase + type, 0, info.seed, 2], T, rect, H);
  if (facade.openings) {
    const [ox, oz] = at(b);
    facade.openings.push({
      ox, oz, oy: ya, tx, tz, nx, nz, bw, b, f, type, style: info.style,
      x0: rx0 * bw, y0: ry0 * FLOOR_H, x1: rx1 * bw, y1: ry1 * FLOOR_H, D,
      seed: info.seed, tint: T, pid: p.id, bid: p.b, H, floors: nF, calle: info.calle || null,
    });
  }
  return 18;
}

function nearestBuilding(map, x, z, r) {
  let best = null, bd = r;
  for (const b of map.buildings) {
    const d = Math.hypot(b.c[0] - x, b.c[1] - z);
    if (d < bd + 12) {
      // distance to ring edges
      const ring = b.ring;
      for (let i = 0; i < ring.length; i += 2) {
        const j = (i + 2) % ring.length;
        const ex = ring[j] - ring[i], ez = ring[j + 1] - ring[i + 1];
        const l2 = ex * ex + ez * ez || 1;
        let t = ((x - ring[i]) * ex + (z - ring[i + 1]) * ez) / l2;
        t = Math.max(0, Math.min(1, t));
        const dd = Math.hypot(x - ring[i] - ex * t, z - ring[i + 1] - ez * t);
        if (dd < bd) { bd = dd; best = b; }
      }
    }
  }
  return best;
}

function buildRoof(c, p, info, H, runs = null) {
  const rnd = info.rnd;
  // a front parapet (pretil) before the tiled roof, on its street's houses that have one (calles.js): from the street the
  // white parapet and its coping, not the row of tile ends; the roof's eaves drawn in, behind it
  const pretil = !!(info.calle && info.calle.pretil) && runs && runs.some((q) => q.exposed && q.ri === 0);
  // (a roof of corrugated sheet in its colour, as seen — calles_casas.js cubierta: a shed's roof, low and plain; one slope
  // down to the street where it is so)
  const cub = info.cubierta;
  if (cub && (cub.una || cub.calle) && runs) { const t = streetRoof(c, p, info, H, runs, !!cub.calle); if (t) return t; }
  const nave = info.style === 'nave' || !!cub;
  const r = cleanRing(p.ring);
  const area = p.area;
  const ob = orientedRect(r);
  const fill = ob ? area / (4 * ob.hw * ob.hd) : 0;
  const rs = p.roofSpec && p.roofSpec.roof; // (measured: 'flat' with its parapet, or 'tile')
  let flatTop = rs ? rs === 'flat' : (p.floors >= 3 && info.style !== 'color' && rnd() < 0.8) || (p.holes && p.holes.length);
  if (!rs && info.calle && info.calle.azotea != null) flatTop = !!info.calle.azotea; // (a flat roof behind its parapet, or a tiled one, as its captures show it)
  const tint = cub ? cub.tint : info.roofTint;
  let tris = 0;
  if (!flatTop && ob && fill > (nave ? 0.9 : 0.92) && Math.min(ob.hw, ob.hd) > 1.0 && Math.max(ob.hw, ob.hd) < 40 && r.length / 2 <= 10) {
    // ---- hip / gable roof over oriented rectangle
    let { cx, cz, ang, hw, hd } = ob;
    let ux = Math.cos(ang), uz = Math.sin(ang);
    if (hd > hw) { const t = hw; hw = hd; hd = t; const tx = ux; ux = -uz; uz = tx; }
    // (its gable end to the street, as seen — calles_casas.js tejado hastial: the ridge square to its longest street front)
    if (info.calle && info.calle.tejado === 'hastial' && runs) {
      let best = null;
      for (const q of runs) if (q.street && q.ri === 0 && (!best || q.L * (q.t1 - q.t0) > best.L * (best.t1 - best.t0))) best = q;
      if (best && Math.abs((ux * best.dx + uz * best.dz) / (Math.hypot(best.dx, best.dz) || 1)) > 0.7) { const t = hw; hw = hd; hd = t; const tx = ux; ux = -uz; uz = tx; }
    }
    const vx = -uz, vz = ux;
    const e = nave ? 0.15 : pretil ? 0.03 : 0.24;
    const A = hw + e, B = hd + e;
    const tanP = nave ? 0.2 : info.pitch;
    const rh = Math.min(B * tanP, nave ? 1.6 : 3.2);
    const g0 = nave || (A > B * 2.2 && rnd() < 0.5), tj = info.calle && info.calle.tejado, gable = tj === 'dos_aguas' || tj === 'hastial' ? true : tj === 'cuatro_aguas' ? false : g0; // (as seen when its notes say)
    const rl = gable ? A : Math.max(0, A - B);
    const y = H - 0.02;
    const P = (a, b, yy) => [cx + ux * a + vx * b, yy, cz + uz * a + vz * b];
    const c1 = P(-A, -B, y), c2 = P(A, -B, y), c3 = P(A, B, y), c4 = P(-A, B, y);
    const r1 = P(-rl, 0, y + rh), r2 = P(rl, 0, y + rh);
    p.roofKind = 'hip'; p.top = y + rh;
    const layer = cub ? ROOF.chapa : nave ? (rnd() < 0.55 ? ROOF.chapa : ROOF.uralita) : ROOF.teja;
    const tex = [layer, 1, info.seed, 0];
    const S = 3.2; // metres per roof texture tile
    const slope = Math.hypot(B, rh);
    // long side (-v): normal
    const nL = norm([-vx * rh, B, -vz * rh]);
    c.tri(c1, c2, r2, nL, [-A / S, 0], [A / S, 0], [rl / S, slope / S], tex, tint);
    c.tri(c1, r2, r1, nL, [-A / S, 0], [rl / S, slope / S], [-rl / S, slope / S], tex, tint);
    const nR = norm([vx * rh, B, vz * rh]);
    c.tri(c3, c4, r1, nR, [-A / S, 0], [A / S, 0], [rl / S, slope / S], tex, tint);
    c.tri(c3, r1, r2, nR, [-A / S, 0], [rl / S, slope / S], [-rl / S, slope / S], tex, tint);
    tris += 4;
    if (!gable) {
      const eL = Math.hypot(A - rl, rh);
      const nE = norm([ux * rh, A - rl, uz * rh]);
      c.tri(c2, c3, r2, nE, [-B / S, 0], [B / S, 0], [0, eL / S], tex, tint);
      const nW = norm([-ux * rh, A - rl, -uz * rh]);
      c.tri(c4, c1, r1, nW, [-B / S, 0], [B / S, 0], [0, eL / S], tex, tint);
      tris += 2;
    } else {
      // gable end walls (triangles) with plain wall texture
      const tp = [STYLE[info.style], 2, info.seed, 0];
      const g1 = P(A - e, -B + e, y), g2 = P(A - e, B - e, y), g3 = P(A - e, 0, y + rh - e * tanP);
      c.tri(g1, g2, g3, [ux, 0, uz], [0, H / FLOOR_H], [1, H / FLOOR_H], [0.5, (H + rh) / FLOOR_H], tp, info.tint);
      const g4 = P(-A + e, B - e, y), g5 = P(-A + e, -B + e, y), g6 = P(-A + e, 0, y + rh - e * tanP);
      c.tri(g4, g5, g6, [-ux, 0, -uz], [0, H / FLOOR_H], [1, H / FLOOR_H], [0.5, (H + rh) / FLOOR_H], tp, info.tint);
      tris += 2;
    }
    // soffits (underside of the overhang), so eaves don't look paper-thin from the street
    const w1 = P(-A + e, -B + e, y), w2 = P(A - e, -B + e, y), w3 = P(A - e, B - e, y), w4 = P(-A + e, B - e, y);
    const st = [STYLE[info.style], 2, info.seed, 0];
    const soff = (a, b, wa, wb) => { c.quad(wa[0], wa[1], wa[2], wb[0], wb[1], wb[2], b[0], b[1], b[2], a[0], a[1], a[2], 0, -1, 0, 0, 0.5, 1, 0.6, st, info.tint); tris += 2; };
    soff(c1, c2, w1, w2); soff(c2, c3, w2, w3); soff(c3, c4, w3, w4); soff(c4, c1, w4, w1);
    // the front row of tiles seen from the street (tile ends along every eave; gables get it on the long sides)
    const tileEdge = (a, b) => {
      const ex = b[0] - a[0], ez = b[2] - a[2], L = Math.hypot(ex, ez) || 1;
      const nx = ez / L, nz = -ex / L;
      // (claymation: a deeper row of tile ends, a little out over the wall: they hang over the eave, cut in scallops)
      const lo = LOOK.plastilina ? 0.13 : 0.075, hi = LOOK.plastilina ? 0.05 : 0.03, o = LOOK.plastilina ? 0.04 : 0;
      c.quad(a[0] + nx * o, a[1] - lo, a[2] + nz * o, b[0] + nx * o, b[1] - lo, b[2] + nz * o, b[0] + nx * o, b[1] + hi, b[2] + nz * o, a[0] + nx * o, a[1] + hi, a[2] + nz * o, nx, 0, nz, 0, 0, L / S, 0.035, tex, tint);
      tris += 2;
    };
    const outward = (a, b) => { const ex = b[0] - a[0], ez = b[2] - a[2]; const mx = (a[0] + b[0]) / 2 - cx, mz = (a[2] + b[2]) / 2 - cz; return ez * mx - ex * mz > 0 ? [a, b] : [b, a]; };
    if (!pretil) for (const [a, b] of gable ? [[c1, c2], [c3, c4]] : [[c1, c2], [c2, c3], [c3, c4], [c4, c1]]) { const [p0, p1] = outward(a, b); tileEdge(p0, p1); }
    if (pretil) tris += frontParapets(c, info, H, runs, 0.55 + rnd() * 0.35);
    // chimney (chimenea) on a share of the houses, rising from one slope
    // (as many as its captures show when its notes say — calles_casas.js chimeneas, 0 none —; the draw kept either way)
    const want = !nave && rnd() < 0.42, nCh = info.calle && info.calle.chimeneas != null ? (info.mainPart == null || info.mainPart === p.id ? info.calle.chimeneas : 0) : want ? 1 : 0; // (the house's own count on its main part only: a row registered as one has many)
    if (!nave && B > 2 && (want || nCh)) {
      const r2 = mulberry32(((p.id + 5) * 2654435761) >>> 0);
      for (let k = 0; k < Math.max(want ? 1 : 0, nCh); k++) {
        const first = k === 0 && want, ca = first ? (rnd() - 0.5) * rl * 1.4 : (r2() - 0.5) * rl * 1.4, cb = -B * (0.35 + (first ? rnd() : r2()) * 0.25);
        const base = P(ca, cb, 0), yRoof = y + rh * (1 - Math.abs(cb) / B), top = yRoof + 0.9 + (first ? rnd() : r2()) * 0.5;
        if (k < nCh) tris += chimney(c, base[0], base[2], ux, uz, yRoof - 0.4, top, info);
      }
    }
    return tris;
  }
  // ---- irregular: tiled lip around the perimeter + terrace, or plain flat roof with parapet
  let lipD = 0, inner = null;
  let rr0 = r;
  if (!flatTop && !nave && !(p.holes && p.holes.length)) {
    rr0 = simplifyRing(r);
    for (const d of [Math.min(3.4, Math.sqrt(area) * 0.32), 2.3, 1.5, 0.9, 0.6]) {
      inner = insetRing(rr0, d);
      if (inner) { lipD = d; break; }
    }
  }
  if (inner) {
    p.roofKind = 'lip';
    const outer = outsetRing(rr0, 0.2);
    const n = rr0.length / 2;
    const rise = lipD * info.pitch;
    p.top = H + rise;
    const tex = [ROOF.teja, 1, info.seed, 0];
    const S = 2.6;
    for (let i = 0; i < n; i++) {
      const j = (i + 1) % n;
      const ax = outer[i * 2], az = outer[i * 2 + 1], bx = outer[j * 2], bz = outer[j * 2 + 1];
      const cx = inner[j * 2], cz = inner[j * 2 + 1], dx = inner[i * 2], dz = inner[i * 2 + 1];
      const ex = bx - ax, ez = bz - az, L = Math.hypot(ex, ez) || 1;
      const nx = ez / L, nz = -ex / L;
      const nn = norm([nx * rise, lipD, nz * rise]);
      c.quad(ax, H, az, bx, H, bz, cx, H + rise, cz, dx, H + rise, dz, nn[0], nn[1], nn[2], 0, 0, L / S, Math.hypot(lipD, rise) / S, tex, tint);
      const lo = LOOK.plastilina ? 0.13 : 0.075, hi = LOOK.plastilina ? 0.05 : 0.02, o = LOOK.plastilina ? 0.04 : 0; // (claymation: the tile ends hang over)
      c.quad(ax + nx * o, H - lo, az + nz * o, bx + nx * o, H - lo, bz + nz * o, bx + nx * o, H + hi, bz + nz * o, ax + nx * o, H + hi, az + nz * o, nx, 0, nz, 0, 0, L / S, 0.035, tex, tint);
      tris += 4;
    }
    tris += flatCap(c, inner, null, H + rise, ROOF.azotea, info, tint);
    return tris;
  }
  // flat roof with parapet
  p.roofKind = 'flat';
  const parH = p.roofSpec && p.roofSpec.parapet != null ? p.roofSpec.parapet : nave ? 0.35 : 0.8;
  p.top = H + parH + 0.04;
  const tp = [STYLE[info.style], 2, info.seed, 0];
  const rings = parH > 0.01 ? [r].concat(p.holes || []) : [];
  for (const rr of rings) {
    const n = rr.length / 2;
    for (let i = 0; i < n; i++) {
      const j = (i + 1) % n;
      const ax = rr[i * 2], az = rr[i * 2 + 1], bx = rr[j * 2], bz = rr[j * 2 + 1];
      const ex = bx - ax, ez = bz - az, L = Math.hypot(ex, ez);
      if (L < 0.05) continue;
      const nx = ez / L, nz = -ex / L;
      c.quad(ax, H, az, bx, H, bz, bx, H + parH, bz, ax, H + parH, az, nx, 0, nz, 0, H / FLOOR_H, L / BAY_W, (H + parH) / FLOOR_H, tp, info.tint);
      // inner face
      c.quad(bx, H, bz, ax, H, az, ax, H + parH, az, bx, H + parH, bz, -nx, 0, -nz, 0, H / FLOOR_H, L / BAY_W, (H + parH) / FLOOR_H, tp, info.tint);
      // coping on top (albardilla): a slab slightly wider than the wall with a small drip on the street side
      const yc = H + parH, o1 = 0.045, o2 = 0.2, cap = [info.tint[0] * 0.9, info.tint[1] * 0.9, info.tint[2] * 0.88];
      const gx = (ex / L) * 0.02, gz = (ez / L) * 0.02;
      c.quad(ax + nx * o1 - gx, yc + 0.04, az + nz * o1 - gz, bx + nx * o1 + gx, yc + 0.04, bz + nz * o1 + gz, bx - nx * o2 + gx, yc + 0.04, bz - nz * o2 + gz, ax - nx * o2 - gx, yc + 0.04, az - nz * o2 - gz, 0, 1, 0, 0, yc / FLOOR_H, L / BAY_W, yc / FLOOR_H + 0.05, tp, cap);
      c.quad(ax + nx * o1 - gx, yc - 0.03, az + nz * o1 - gz, bx + nx * o1 + gx, yc - 0.03, bz + nz * o1 + gz, bx + nx * o1 + gx, yc + 0.04, bz + nz * o1 + gz, ax + nx * o1 - gx, yc + 0.04, az + nz * o1 - gz, nx, 0, nz, 0, yc / FLOOR_H, L / BAY_W, yc / FLOOR_H + 0.02, tp, cap);
      c.quad(bx - nx * o2 + gx, yc - 0.01, bz - nz * o2 + gz, ax - nx * o2 - gx, yc - 0.01, az - nz * o2 - gz, ax - nx * o2 - gx, yc + 0.04, az - nz * o2 - gz, bx - nx * o2 + gx, yc + 0.04, bz - nz * o2 + gz, -nx, 0, -nz, 0, yc / FLOOR_H, L / BAY_W, yc / FLOOR_H + 0.02, tp, cap);
      tris += 10;
    }
  }
  tris += flatCap(c, r, p.holes, H + 0.02, nave ? ROOF.chapa : ROOF.azotea, info, tint);
  return tris;
}

// a roof of corrugated sheet laid by the street it looks onto (calles_casas.js cubierta), over the whole outline whatever
// its shape: una — one slope down to the street, its low edge along the fronts the street sees, rising a tenth away from
// them; calle — two, their ridge along the street half-way back, the slope towards the street steep enough to be seen
// over the front (Gerardo Diego's big shed, its gable at the far end), at most 6.5 m up. The walls carried up under it in
// their paint. 0 when the part looks onto no street.
function streetRoof(c, p, info, H, runs, tent) {
  let Nx = 0, Nz = 0;
  for (const q of runs) if (q.street && q.ri === 0) { const l = (q.t1 - q.t0) * q.L; Nx += q.nx * l; Nz += q.nz * l; }
  const nl = Math.hypot(Nx, Nz);
  if (nl < 1e-3) return 0;
  Nx /= nl; Nz /= nl;
  const r = p.ring, n = r.length / 2;
  let F = -Infinity, G = Infinity;
  for (let i = 0; i < n; i++) { const d = r[i * 2] * Nx + r[i * 2 + 1] * Nz; F = Math.max(F, d); G = Math.min(G, d); }
  const R = tent ? (F + G) / 2 : G, k = tent ? Math.min(0.45, 6.5 / Math.max(1, F - R)) : 0.1;
  const pr = (x, z) => x * Nx + z * Nz;
  const yAt = (x, z) => { const d = pr(x, z); return H + k * Math.min(F - d, d - G + (tent ? 0 : 1e9)); };
  // (each slope its own piece of the outline: the half on its side of the ridge)
  const half = (above) => {
    const out = [];
    for (let i = 0; i < n; i++) {
      const j = (i + 1) % n, si = (pr(r[i * 2], r[i * 2 + 1]) - R) * (above ? 1 : -1), sj = (pr(r[j * 2], r[j * 2 + 1]) - R) * (above ? 1 : -1);
      if (si >= 0) out.push(r[i * 2], r[i * 2 + 1]);
      if ((si >= 0) !== (sj >= 0)) { const t = si / (si - sj); out.push(r[i * 2] + (r[j * 2] - r[i * 2]) * t, r[i * 2 + 1] + (r[j * 2 + 1] - r[i * 2 + 1]) * t); }
    }
    return out.length >= 6 ? out : null;
  };
  const slopes = tent ? [[half(true), 1], [half(false), -1]] : [[r, 1]];
  const tex = [ROOF.chapa, 1, info.seed, 0], tint = info.cubierta.tint, S = 3.2;
  let tris = 0;
  for (const [ring, sgn] of slopes) {
    if (!ring) continue;
    let t;
    try { t = triangulate(ring, null); } catch (e) { return 0; }
    const i0 = c.vcount, nn = norm([Nx * k * sgn, 1, Nz * k * sgn]);
    for (const v of t.pts) {
      c.pos.push(v.x, yAt(v.x, v.y), v.y);
      c.nor.push(nn[0], nn[1], nn[2]);
      c.uv.push((v.x * -Nz + v.y * Nx) / S, (v.x * Nx + v.y * Nz) / S); // (its corrugations running down the slope)
      c.tex.push(tex[0], tex[1], tex[2], tex[3]); c.tint.push(tint[0], tint[1], tint[2]);
      c.rect.push(0, 0, 0, 0); c.wall.push(0); c.zoc.push(0, 0, 0, 0);
      if (c.edge) c.edge.push(0, 0);
    }
    for (const f of t.faces) {
      const a = t.pts[f[0]], b = t.pts[f[1]], d = t.pts[f[2]];
      const cy = -((b.x - a.x) * (d.y - a.y) - (b.y - a.y) * (d.x - a.x));
      if (cy >= 0) c.idx.push(i0 + f[0], i0 + f[1], i0 + f[2]);
      else c.idx.push(i0 + f[0], i0 + f[2], i0 + f[1]);
    }
    tris += t.faces.length;
  }
  // the walls carried up under it (a wall that crosses the ridge, in two: up to it and down from it)
  const tp = [STYLE[info.style], 2, info.seed, 0];
  for (let i = 0; i < n; i++) {
    const j = (i + 1) % n, ax = r[i * 2], az = r[i * 2 + 1], bx = r[j * 2], bz = r[j * 2 + 1];
    const L = Math.hypot(bx - ax, bz - az);
    if (L < 0.05) continue;
    const ex = (bx - ax) / L, ez = (bz - az) / L, pa = pr(ax, az) - R, pb = pr(bx, bz) - R;
    const pts = [[ax, az]];
    if (tent && pa * pb < 0) { const t = pa / (pa - pb); pts.push([ax + (bx - ax) * t, az + (bz - az) * t]); }
    pts.push([bx, bz]);
    for (let q = 0; q < pts.length - 1; q++) {
      const [x0, z0] = pts[q], [x1, z1] = pts[q + 1], y0 = yAt(x0, z0), y1 = yAt(x1, z1);
      if (y0 < H + 0.03 && y1 < H + 0.03) continue;
      const l = Math.hypot(x1 - x0, z1 - z0);
      c.quad(x0, H - 0.02, z0, x1, H - 0.02, z1, x1, y1, z1, x0, y0, z0, ez, 0, -ex, 0, H / FLOOR_H, l / BAY_W, Math.max(y0, y1) / FLOOR_H, tp, info.tint);
      tris += 2;
    }
  }
  p.roofKind = 'mono'; p.top = H + k * (tent ? F - R : F - G);
  return tris;
}

// the parapet along a house's street fronts (its outer ring's exposed runs), from the top of the wall up h: both faces in
// the wall's paint, a coping on top (albardilla) a little proud of the wall, as on the flat roofs
function frontParapets(c, info, H, runs, h) {
  const tp = [STYLE[info.style], 2, info.seed, 0], cap = [info.tint[0] * 0.92, info.tint[1] * 0.92, info.tint[2] * 0.9];
  let tris = 0;
  for (const q of runs) {
    if (!q.exposed || q.ri !== 0 || (q.t1 - q.t0) * q.L < 0.5) continue;
    const ax = q.ax + q.dx * q.t0, az = q.az + q.dz * q.t0, bx = q.ax + q.dx * q.t1, bz = q.az + q.dz * q.t1;
    const ex = bx - ax, ez = bz - az, L = Math.hypot(ex, ez);
    const nx = q.nx, nz = q.nz, y0 = H - 0.05, y1 = H + h;
    c.quad(ax, y0, az, bx, y0, bz, bx, y1, bz, ax, y1, az, nx, 0, nz, 0, y0 / FLOOR_H, L / BAY_W, y1 / FLOOR_H, tp, info.tint);
    c.quad(bx - nx * 0.18, y0, bz - nz * 0.18, ax - nx * 0.18, y0, az - nz * 0.18, ax - nx * 0.18, y1, az - nz * 0.18, bx - nx * 0.18, y1, bz - nz * 0.18, -nx, 0, -nz, 0, y0 / FLOOR_H, L / BAY_W, y1 / FLOOR_H, tp, info.tint);
    const o1 = 0.05, o2 = 0.23, gx = (ex / L) * 0.02, gz = (ez / L) * 0.02, yc = y1;
    c.quad(ax + nx * o1 - gx, yc + 0.05, az + nz * o1 - gz, bx + nx * o1 + gx, yc + 0.05, bz + nz * o1 + gz, bx - nx * o2 + gx, yc + 0.05, bz - nz * o2 + gz, ax - nx * o2 - gx, yc + 0.05, az - nz * o2 - gz, 0, 1, 0, 0, yc / FLOOR_H, L / BAY_W, yc / FLOOR_H + 0.05, tp, cap);
    c.quad(ax + nx * o1 - gx, yc - 0.03, az + nz * o1 - gz, bx + nx * o1 + gx, yc - 0.03, bz + nz * o1 + gz, bx + nx * o1 + gx, yc + 0.05, bz + nz * o1 + gz, ax + nx * o1 - gx, yc + 0.05, az + nz * o1 - gz, nx, 0, nz, 0, yc / FLOOR_H, L / BAY_W, yc / FLOOR_H + 0.02, tp, cap);
    tris += 8;
  }
  return tris;
}

// small whitewashed chimney with a tiled cap
function chimney(c, x, z, ux, uz, y0, y1, info) {
  const w = 0.32, vx = -uz, vz = ux;
  const tex = [STYLE[info.style], 2, info.seed, 0];
  const P = (a, b) => [x + ux * a + vx * b, z + uz * a + vz * b];
  const q = [P(-w, -w), P(w, -w), P(w, w), P(-w, w)];
  let t = 0;
  for (let i = 0; i < 4; i++) {
    const a = q[i], b = q[(i + 1) % 4];
    const ex = b[0] - a[0], ez = b[1] - a[1], L = Math.hypot(ex, ez);
    const nx = ez / L, nz = -ex / L;
    c.quad(a[0], y0, a[1], b[0], y0, b[1], b[0], y1, b[1], a[0], y1, a[1], nx, 0, nz, 0, y0 / FLOOR_H, 0.25, y1 / FLOOR_H, tex, info.tint);
    t += 2;
  }
  // cap slab
  const cw = w + 0.08, capT = [ROOF.teja, 1, info.seed, 0];
  const k = [P(-cw, -cw), P(cw, -cw), P(cw, cw), P(-cw, cw)];
  c.quad(k[0][0], y1 + 0.12, k[0][1], k[1][0], y1 + 0.12, k[1][1], k[2][0], y1 + 0.12, k[2][1], k[3][0], y1 + 0.12, k[3][1], 0, 1, 0, 0, 0, 0.3, 0.3, capT, info.roofTint);
  for (let i = 0; i < 4; i++) {
    const a = k[i], b = k[(i + 1) % 4];
    const ex = b[0] - a[0], ez = b[1] - a[1], L = Math.hypot(ex, ez);
    c.quad(a[0], y1, a[1], b[0], y1, b[1], b[0], y1 + 0.12, b[1], a[0], y1 + 0.12, a[1], ez / L, 0, -ex / L, 0, 0, 0.3, 0.05, capT, info.roofTint);
  }
  return t + 10;
}

function flatCap(c, ring, holes, y, layer, info, tint) {
  let t;
  try { t = triangulate(ring, holes); } catch (e) { return 0; }
  const tex = [layer, 1, info.seed, 0];
  const S = 3;
  const i0 = c.vcount;
  for (const v of t.pts) {
    c.pos.push(v.x, y, v.y);
    c.nor.push(0, 1, 0);
    c.uv.push(v.x / S, v.y / S);
    c.tex.push(tex[0], tex[1], tex[2], tex[3]);
    c.tint.push(tint[0], tint[1], tint[2]);
    c.rect.push(0, 0, 0, 0);
    c.wall.push(0);
    c.zoc.push(0, 0, 0, 0);
    if (c.edge) c.edge.push(0, 0);
  }
  for (const f of t.faces) {
    const a = t.pts[f[0]], b = t.pts[f[1]], d = t.pts[f[2]];
    // y-component of (b-a)x(d-a) with (x,z) mapped from 2D (x,y): -( (b.x-a.x)*(d.y-a.y) - (b.y-a.y)*(d.x-a.x) )
    const cy = -((b.x - a.x) * (d.y - a.y) - (b.y - a.y) * (d.x - a.x));
    if (cy >= 0) c.idx.push(i0 + f[0], i0 + f[1], i0 + f[2]);
    else c.idx.push(i0 + f[0], i0 + f[2], i0 + f[1]);
  }
  return t.faces.length;
}

function norm(v) {
  const l = Math.hypot(v[0], v[1], v[2]) || 1;
  return [v[0] / l, v[1] / l, v[2] / l];
}

// Ground contact shadow strips along facades (baked AO look)
export function buildAOGeometry(ao, width = 1.3) {
  const n = ao.length / 6;
  const pos = new Float32Array(n * 4 * 3);
  const alpha = new Float32Array(n * 4);
  const idx = new Uint32Array(n * 6);
  for (let i = 0; i < n; i++) {
    const ax = ao[i * 6], az = ao[i * 6 + 1], bx = ao[i * 6 + 2], bz = ao[i * 6 + 3], nx = ao[i * 6 + 4], nz = ao[i * 6 + 5];
    const o = i * 12;
    pos.set([ax, 0.03, az, bx, 0.03, bz, bx + nx * width, 0.03, bz + nz * width, ax + nx * width, 0.03, az + nz * width], o);
    alpha.set([0.42, 0.42, 0, 0], i * 4);
    idx.set([i * 4, i * 4 + 2, i * 4 + 1, i * 4, i * 4 + 3, i * 4 + 2], i * 6);
  }
  const g = new THREE.BufferGeometry();
  g.setAttribute('position', new THREE.BufferAttribute(pos, 3));
  g.setAttribute('aAlpha', new THREE.BufferAttribute(alpha, 1));
  g.setIndex(new THREE.BufferAttribute(idx, 1));
  return g;
}
