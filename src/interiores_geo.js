// The geometry the interiors are laid out and checked with (technical backlog, I-04): an object's parts as boxes turned
// about y, how far two of them run into each other, and the way a body 0.9 m wide can walk from the street door —
// shared by the layout (src/locales.js, which never shuts a public zone off) and the validator (tools/interiores).
import { OBJETOS } from './interiores_datos.js';

const DEG = Math.PI / 180;
export const rot = (x, z, a) => [x * Math.cos(a) + z * Math.sin(a), -x * Math.sin(a) + z * Math.cos(a)];

// the parts of a placed object { obj, x, y, z, ry } as { cx, cz, hw, hd, a, y0, y1 } (a part turned about x or z: the
// box round it)
export function partes(it) {
  const o = OBJETOS[it.obj], out = [];
  for (const p of o.partes) {
    let hw, hh, hd;
    const d = p.d, s = p.s || [1, 1, 1];
    if (p.f === 'caja') { hw = d[0] / 2; hh = d[1] / 2; hd = d[2] / 2; }
    else if (p.f === 'cil') { const rr = Math.max(d[0], d[1]); hw = rr; hh = d[2] / 2; hd = rr; }
    else if (p.f === 'esfera') { hw = d[0]; hh = d[0]; hd = d[0]; }
    else if (p.f === 'cono') { hw = d[0]; hh = d[1] / 2; hd = d[0]; }
    else { hw = d[0] / 2; hh = d[1] / 2; hd = 0.002; }
    hw *= s[0]; hh *= s[1]; hd *= s[2];
    if (p.r && (p.r[0] || p.r[2])) {
      const rx = (p.r[0] || 0) * DEG, rz = (p.r[2] || 0) * DEG;
      const nh = Math.abs(hh * Math.cos(rx) * Math.cos(rz)) + Math.abs(hd * Math.sin(rx)) + Math.abs(hw * Math.sin(rz));
      const nd = Math.abs(hd * Math.cos(rx)) + Math.abs(hh * Math.sin(rx));
      const nw = Math.abs(hw * Math.cos(rz)) + Math.abs(hh * Math.sin(rz));
      hw = nw; hh = nh; hd = nd;
    }
    const a = it.ry + (p.r ? (p.r[1] || 0) * DEG : 0);
    const [ox, oz] = rot(p.p[0], p.p[2], it.ry);
    out.push({ cx: it.x + ox, cz: it.z + oz, hw, hd, a, y0: (it.y || 0) + p.p[1] - hh, y1: (it.y || 0) + p.p[1] + hh, f: p.f });
  }
  return out;
}
// how far two turned boxes run into each other (the least overlap along the separating axes; 0 if apart)
export function penetra(A, B) {
  const dy = Math.min(A.y1, B.y1) - Math.max(A.y0, B.y0);
  if (dy <= 0) return 0;
  let least = dy;
  const axes = [[Math.cos(A.a), -Math.sin(A.a)], [Math.sin(A.a), Math.cos(A.a)], [Math.cos(B.a), -Math.sin(B.a)], [Math.sin(B.a), Math.cos(B.a)]];
  const dx = B.cx - A.cx, dz = B.cz - A.cz;
  for (const [ux, uz] of axes) {
    const ra = A.hw * Math.abs(Math.cos(A.a) * ux - Math.sin(A.a) * uz) + A.hd * Math.abs(Math.sin(A.a) * ux + Math.cos(A.a) * uz);
    const rb = B.hw * Math.abs(Math.cos(B.a) * ux - Math.sin(B.a) * uz) + B.hd * Math.abs(Math.sin(B.a) * ux + Math.cos(B.a) * uz);
    const o = ra + rb - Math.abs(dx * ux + dz * uz);
    if (o <= 0) return 0;
    least = Math.min(least, o);
  }
  return least;
}

// the rectangle of an object's k-th surface in its own frame — { y, x0, x1, z0, z1, estante } —, from the parts whose top
// is at its height (a round top: the square inside it), less its margin; a shelf (fondo) from its back
const SUP = new Map();
export function superficie(id, k) {
  const key = id + '#' + k;
  if (SUP.has(key)) return SUP.get(key);
  const s = OBJETOS[id].superficies[k];
  let x0 = Infinity, x1 = -Infinity, z0 = Infinity, z1 = -Infinity;
  for (const p of partes({ obj: id, x: 0, y: 0, z: 0, ry: 0 })) {
    if (Math.abs(p.y1 - s.y) > 0.012) continue;
    const red = p.f === 'cil' ? Math.SQRT1_2 : 1;
    const ex = (Math.abs(p.hw * Math.cos(p.a)) + Math.abs(p.hd * Math.sin(p.a))) * red, ez = (Math.abs(p.hw * Math.sin(p.a)) + Math.abs(p.hd * Math.cos(p.a))) * red;
    x0 = Math.min(x0, p.cx - ex); x1 = Math.max(x1, p.cx + ex); z0 = Math.min(z0, p.cz - ez); z1 = Math.max(z1, p.cz + ez);
  }
  let R = null;
  if (x0 < x1) {
    const m = s.margen ?? 0.02;
    R = s.fondo ? { y: s.y, x0: x0 + m, x1: x1 - m, z0: z0 + 0.01, z1: Math.min(z1 - 0.005, z0 + s.fondo), estante: true } : { y: s.y, x0: x0 + m, x1: x1 - m, z0: z0 + m, z1: z1 - m, estante: false };
  }
  SUP.set(key, R);
  return R;
}

// squared distances to the nearest zero of g[0..n) (Felzenszwalb & Huttenlocher's lower envelope of parabolas)
const INF = 1e20;
function pase(g, n, d, v, zz) {
  let k = 0;
  v[0] = 0; zz[0] = -INF; zz[1] = INF;
  for (let q = 1; q < n; q++) {
    let s = (g[q] + q * q - (g[v[k]] + v[k] * v[k])) / (2 * q - 2 * v[k]);
    while (s <= zz[k]) { k--; s = (g[q] + q * q - (g[v[k]] + v[k] * v[k])) / (2 * q - 2 * v[k]); }
    k++; v[k] = q; zz[k] = s; zz[k + 1] = INF;
  }
  k = 0;
  for (let q = 0; q < n; q++) { while (zz[k + 1] < q) k++; d[q] = (q - v[k]) * (q - v[k]) + g[v[k]]; }
}

// where a body `ancho` m wide can stand and walk to from the street door (puertaX, z = 0): a grid of `S` m over the room
// { W, D, zonas, tabiques } (its walls' faces at its edges), with the parts laid out [{ cx, cz, hw, hd, a, y0, y1 }];
// → { nx, nz, S, free, reach, zonas: { id: { alcanzable, libre, … } } }. A body stands where nothing is nearer than half
// its width (the exact distance, by a distance transform: cheap enough to ask after every piece the layout puts down).
export function mapaPaso(room, piezas, S = 0.05, ancho = 0.9, puertaX = 0) {
  const { W, D } = room, nx = Math.ceil(W / S - 1e-9), nz = Math.ceil(D / S - 1e-9), N = nx * nz, occ = new Uint8Array(N);
  const mark = (x0, z0, x1, z1) => {
    const i0 = Math.max(0, Math.floor((x0 + W / 2) / S)), i1 = Math.min(nx - 1, Math.floor((x1 + W / 2) / S)), k0 = Math.max(0, Math.floor(z0 / S)), k1 = Math.min(nz - 1, Math.floor(z1 / S));
    for (let k = k0; k <= k1; k++) for (let i = i0; i <= i1; i++) occ[k * nx + i] = 1;
  };
  for (const p of piezas) {
    if (p.y0 > 1.2 || p.y1 < 0.08) continue; // (what a body walks into: from the ankles to the chest)
    const ex = Math.abs(p.hw * Math.cos(p.a)) + Math.abs(p.hd * Math.sin(p.a)), ez = Math.abs(p.hw * Math.sin(p.a)) + Math.abs(p.hd * Math.cos(p.a));
    mark(p.cx - ex, p.cz - ez, p.cx + ex, p.cz + ez);
  }
  const th = 0.07; // (half a partition)
  for (const t of room.tabiques || []) {
    const L = Math.hypot(t.bx - t.ax, t.bz - t.az), ux = (t.bx - t.ax) / L, uz = (t.bz - t.az) / L;
    for (const [s0, s1] of t.hueco ? [[0, t.hueco[0]], [t.hueco[1], L]] : [[0, L]]) {
      if (s1 - s0 < 1e-6) continue;
      const xa = t.ax + ux * s0, za = t.az + uz * s0, xb = t.ax + ux * s1, zb = t.az + uz * s1;
      if (Math.abs(ux) < 1e-6 || Math.abs(uz) < 1e-6) mark(Math.min(xa, xb) - th * Math.abs(uz), Math.min(za, zb) - th * Math.abs(ux), Math.max(xa, xb) + th * Math.abs(uz), Math.max(za, zb) + th * Math.abs(ux));
      else for (let s = s0; s <= s1; s += S / 2) { const x = t.ax + ux * s, z = t.az + uz * s; mark(x - th, z - th, x + th, z + th); }
    }
  }
  // (the squared distance, in cells, from each cell to the nearest taken one: by columns, then by rows)
  const f = new Float64Array(N), M = Math.max(nx, nz), g = new Float64Array(M), d = new Float64Array(M), v = new Int32Array(M), zz = new Float64Array(M + 1);
  for (let c = 0; c < N; c++) f[c] = occ[c] ? 0 : INF;
  for (let i = 0; i < nx; i++) { for (let k = 0; k < nz; k++) g[k] = f[k * nx + i]; pase(g, nz, d, v, zz); for (let k = 0; k < nz; k++) f[k * nx + i] = d[k]; }
  for (let k = 0; k < nz; k++) { for (let i = 0; i < nx; i++) g[i] = f[k * nx + i]; pase(g, nx, d, v, zz); for (let i = 0; i < nx; i++) f[k * nx + i] = d[i]; }
  // (a body's centre: half its width clear all round, the room's walls included)
  const R = Math.round(ancho / 2 / S), R2 = R * R, free = new Uint8Array(N);
  for (let k = R; k < nz - R; k++) for (let i = R; i < nx - R; i++) if (f[k * nx + i] >= R2) free[k * nx + i] = 1;
  const reach = new Uint8Array(N), q = [];
  const di0 = Math.floor((puertaX + W / 2) / S);
  for (let k = R; k < nz && !q.length; k++) for (let dd = 0; dd < 30 && !q.length; dd++) for (const i of [di0 + dd, di0 - dd]) if (i >= 0 && i < nx && free[k * nx + i]) { q.push(k * nx + i); reach[k * nx + i] = 1; break; }
  while (q.length) {
    const c = q.pop(), i = c % nx, k = (c / nx) | 0;
    if (i > 0 && free[c - 1] && !reach[c - 1]) { reach[c - 1] = 1; q.push(c - 1); }
    if (i < nx - 1 && free[c + 1] && !reach[c + 1]) { reach[c + 1] = 1; q.push(c + 1); }
    if (k > 0 && free[c - nx] && !reach[c - nx]) { reach[c - nx] = 1; q.push(c - nx); }
    if (k < nz - 1 && free[c + nx] && !reach[c + nx]) { reach[c + nx] = 1; q.push(c + nx); }
  }
  const zonas = {};
  for (const Z of Object.values(room.zonas)) {
    let n = 0, fr = 0;
    for (let i = Math.max(0, Math.floor((Z.x0 + W / 2) / S)); i < Math.min(nx, Math.ceil((Z.x1 + W / 2) / S)); i++) for (let k = Math.max(0, Math.floor(Z.z0 / S)); k < Math.min(nz, Math.ceil(Z.z1 / S)); k++) { if (free[k * nx + i]) fr++; if (reach[k * nx + i]) n++; }
    zonas[Z.id] = { alcanzable: n, libre: fr, alcanzable_m2: +(n * S * S).toFixed(2), libre_m2: +(fr * S * S).toFixed(2) };
  }
  return { nx, nz, S, free, reach, zonas };
}
