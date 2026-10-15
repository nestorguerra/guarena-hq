// The shops' sign bands (technical backlog, R-06): every shop front the game builds has a band over its window
// (facades.js buildShop, a box in its colour), and they were all blank. Each now has its words: the name of the
// business the map places at it — OpenStreetMap's, the real one in a local copy of the game, its kind's generic in the
// published one (tools/build.py sanitises the map it packs) —; with none within 15 m, a generic from a short list of the
// shops a small town has, marked as such. A front with its own sign read in the captures (calles_casas.js rotulo)
// keeps that one. The band is drawn again as a panel of its own, with its words, so it reads from afar too (the
// facade's 3D details are only built near), and lit at night (R-09: src/world.js lights the signs after dusk).
import * as THREE from 'three';
import { CT, fasciaHex } from './facades.js';
import { registrar, rotulo, entidadPorNombre } from './rotulos.js';
import { GENERICOS_TIPO } from './rotulos_datos.js';
import { mulberry32 } from './util.js';

const COMERCIO = /^(shop:|amenity:(bank|bar|pub|cafe|restaurant|fast_food|pharmacy|dentist|driving_school|car_wash|language_school)$|office:(company|insurance)$|craft:)/;
const SIN_NOMBRE = ['ALIMENTACIÓN', 'MERCERÍA', 'PAPELERÍA', 'ZAPATERÍA', 'FRUTERÍA', 'MODA', 'BAZAR', 'REGALOS', 'PANADERÍA', 'DROGUERÍA'];

export function buildShopSigns(world, map, openings) {
  // the shop bays with a band (ground floor, a front over 2.95 m), the bays of one front side by side as one band
  const bays = openings.filter((o) => o.type === CT.SHOP && o.f === 0 && o.H > 2.95 && !(o.calle && o.calle.rotulo));
  const key = (o) => `${o.pid}|${o.tx.toFixed(3)}|${o.tz.toFixed(3)}|${(o.ox * o.nx + o.oz * o.nz).toFixed(1)}`;
  const fronts = new Map();
  for (const o of bays) { const k = key(o); if (!fronts.has(k)) fronts.set(k, []); fronts.get(k).push(o); }
  const bands = [];
  for (const list of fronts.values()) {
    list.sort((a, b) => (a.ox * a.tx + a.oz * a.tz) - (b.ox * b.tx + b.oz * b.tz));
    let run = [list[0]];
    const close = () => {
      const a = run[0], b = run[run.length - 1];
      const x0 = a.ox + a.tx * 0.06, z0 = a.oz + a.tz * 0.06, x1 = b.ox + b.tx * (b.bw - 0.06), z1 = b.oz + b.tz * (b.bw - 0.06);
      // (the sign over a shop window stands on the front of its shutter box — facades.js buildShop: 30 cm high, 17 cm
      // proud —, as a real one does: from the window's head to 50 cm over it, short of the first floor's slab; set
      // flat on the wall it was hidden behind that box)
      const top = Math.max(...run.map((o) => o.y1)), y0 = a.oy + top - 0.02, y1 = a.oy + Math.min(top + 0.5, a.floors > 1 ? 3.0 : a.H - 0.1);
      const w = Math.hypot(x1 - x0, z1 - z0);
      if (w > 0.8 && y1 - y0 > 0.25) bands.push({ o: a, x: (x0 + x1) / 2 + a.nx * 0.185, z: (z0 + z1) / 2 + a.nz * 0.185, y: (y0 + y1) / 2, w, h: y1 - y0, tx: a.tx, tz: a.tz, nx: a.nx, nz: a.nz });
    };
    for (let i = 1; i < list.length; i++) {
      const p = run[run.length - 1], o = list[i];
      const gap = (o.ox * o.tx + o.oz * o.tz) - (p.ox * p.tx + p.oz * p.tz + p.bw);
      if (gap < 0.3) run.push(o); else { close(); run = [o]; }
    }
    close();
  }
  if (!bands.length) return 0;
  // the business at each band: one of the map's within 15 m — the one inside its own building first (it signs all the
  // fronts of its building), else the nearest not inside another building, each of those one band at most
  const pois = map.pois.map((p, i) => ({ p, i, b: (map.buildingAt(p.x, p.z) || {}).id })).filter(({ p }) => COMERCIO.test(p.kind));
  const pairs = [];
  bands.forEach((b, j) => {
    let own = null;
    for (const q of pois) {
      const d = Math.hypot(q.p.x - b.x, q.p.z - b.z);
      if (d >= 15) continue;
      if (q.b === b.o.bid) { if (!own || d < own.d) own = { i: q.i, p: q.p, d }; } else if (q.b == null) pairs.push([d, j, q.i]);
    }
    if (own) b.poi = own;
  });
  pairs.sort((a, b) => a[0] - b[0]);
  const usedP = new Set();
  for (const [d, j, i] of pairs) { if (bands[j].poi || usedP.has(i)) continue; usedP.add(i); bands[j].poi = { i, p: map.pois[i], d }; }
  // the words and the colours of each
  for (const b of bands) {
    const p = b.poi && b.poi.p;
    const ent = p && entidadPorNombre(p.name); // (one the registry knows: its name for this copy — R-05's corrections)
    const name = p ? (ent ? rotulo(ent) : p.name || GENERICOS_TIPO[p.kind] || '') : '';
    b.generico = !name;
    b.texto = (name || SIN_NOMBRE[Math.floor(mulberry32((b.o.bid + 13) * 2654435761 >>> 0)() * SIN_NOMBRE.length)]).toUpperCase();
    b.fondo = fasciaHex(b.o);
    const v = parseInt(b.fondo.slice(1), 16), l = 0.299 * (v >> 16) + 0.587 * ((v >> 8) & 255) + 0.114 * (v & 255);
    b.letra = l > 150 ? '#22262a' : '#f6f3ec';
  }
  // one canvas, a cell each; one mesh of panels
  const CW = 512, CH = 96, cols = 2, rows = Math.ceil(bands.length / cols);
  let HH = 128; while (HH < rows * CH) HH *= 2;
  const c = document.createElement('canvas'); c.width = CW * cols; c.height = HH;
  const x = c.getContext('2d');
  const pos = [], nor = [], uv = [], idx = [];
  bands.forEach((b, i) => {
    const cx = (i % cols) * CW, cy = Math.floor(i / cols) * CH;
    x.fillStyle = b.fondo; x.fillRect(cx, cy, CW, CH);
    x.fillStyle = b.letra; x.textAlign = 'center'; x.textBaseline = 'middle';
    // (the cell is stretched over the band: its letters drawn narrower or wider by as much, to keep their shape there)
    const sx = (CW / CH) / (b.w / b.h);
    let fs = 66;
    do { x.font = `800 ${fs}px "Arial Narrow", Arial, Helvetica, sans-serif`; fs -= 3; } while (fs > 16 && x.measureText(b.texto).width * sx > CW * 0.9);
    x.save(); x.translate(cx + CW / 2, cy + CH / 2 + 2); x.scale(sx, 1); x.fillText(b.texto, 0, 0); x.restore();
    const u0 = cx / c.width, u1 = (cx + CW) / c.width, v0 = 1 - (cy + CH) / HH, v1 = 1 - cy / HH;
    const k = pos.length / 3, hw = b.w / 2, y0 = b.y - b.h / 2, y1 = b.y + b.h / 2;
    // (left to right as seen from the street: whoever faces the front looks along -n, their right is (nz, -nx))
    const rx = b.nz, rz = -b.nx;
    const ax = b.x - rx * hw, az = b.z - rz * hw, bx = b.x + rx * hw, bz = b.z + rz * hw;
    pos.push(ax, y0, az, bx, y0, bz, bx, y1, bz, ax, y1, az);
    for (let q = 0; q < 4; q++) nor.push(b.nx, 0, b.nz);
    uv.push(u0, v0, u1, v0, u1, v1, u0, v1);
    idx.push(k, k + 1, k + 2, k, k + 2, k + 3);
    registrar({ id: `tienda:${b.o.bid}:${Math.round(b.x)},${Math.round(b.z)}`, tipo: 'fachada', texto: b.texto, poi: b.poi ? 'mapa:' + b.poi.i : null, poi_mapa: b.poi ? { tipo: b.poi.p.kind, x: +b.poi.p.x.toFixed(2), z: +b.poi.p.z.toFixed(2) } : null, generico: b.generico || !!(b.poi && !b.poi.p.name),
      motivo: b.generico ? 'sin comercio en el mapa a menos de 15 m' : null, bid: b.o.bid, x: b.x, y: b.y, z: b.z, nx: b.nx, nz: b.nz, caras: 1, w: b.w, h: b.h });
  });
  const tex = new THREE.CanvasTexture(c); tex.colorSpace = THREE.SRGBColorSpace; tex.anisotropy = 4;
  const g = new THREE.BufferGeometry();
  g.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
  g.setAttribute('normal', new THREE.Float32BufferAttribute(nor, 3));
  g.setAttribute('uv', new THREE.Float32BufferAttribute(uv, 2));
  g.setIndex(idx);
  const mat = new THREE.MeshStandardMaterial({ map: tex, roughness: 0.55, emissive: 0xffffff, emissiveMap: tex, emissiveIntensity: 0, polygonOffset: true, polygonOffsetFactor: -1, polygonOffsetUnits: -2 });
  const m = new THREE.Mesh(g, mat); m.receiveShadow = true; m.matrixAutoUpdate = false;
  world.root.add(m);
  (world.signMats || (world.signMats = [])).push([mat, 0.55]);
  return bands.length;
}
