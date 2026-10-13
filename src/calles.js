// The town's streets as they really are: a style for each street and square, written from the user's Google Maps
// captures of them (2026-10-12/13, ~/Desktop/Guareña: the centre's 26 and the eastern quarter's 23 so far, of the 85
// folders there; tools/fachadas/capturas.py and tools/callelab.js put the game's camera where each was taken). The captures
// are only a reference: every colour and measure here was read from them by eye and by sampling, nothing of them goes
// into the game. A house on one of these streets takes its look from its street's style instead of the town's generic
// ones (buildings.js, facades.js, streetlife.js, world.js); the houses measured one by one (fachadas.js: Malfeitos)
// keep their own.
import { polyNearest, pointInRing, ringArea, mulberry32 } from './util.js';
import { STYLES as STYLES0 } from './calles_estilos.js';
import { CASAS } from './calles_casas.js';
export const STYLES = STYLES0; // (re-exported so: tools/build.py knows only `export const|function|class`)

// ---------------------------------------------------------------- which street a building looks onto
// Each building's street: the named street (or square) its fronts look onto, by the metres of front that do — walls
// probed a step and a few metres out, the nearest named street whose carriageway and pavement reach there. The two
// squares round Santa María have no street of their own in the map: what faces the church's open ground is the Plaza
// de Santa María to the north and west and the Plaza de los Castillejos — the atrium — to the south and east (as the
// captures' guide places them, after the BOE of 1 July 1988)
const CHURCH_SQUARES = { r: 46, nw: 'Plaza de Santa María', se: 'Plaza de los Castillejos' };
export function streetsOf(map, church = null) {
  if (map._calles) return map._calles;
  const squares = map.areas.filter((a) => a.name && /^Plaza /.test(a.name) && STYLES[a.name]).map((a) => {
    let x0 = Infinity, z0 = Infinity, x1 = -Infinity, z1 = -Infinity;
    for (let i = 0; i < a.ring.length; i += 2) { x0 = Math.min(x0, a.ring[i]); x1 = Math.max(x1, a.ring[i]); z0 = Math.min(z0, a.ring[i + 1]); z1 = Math.max(z1, a.ring[i + 1]); }
    return { name: a.name, ring: a.ring, bb: [x0 - 1, z0 - 1, x1 + 1, z1 + 1] };
  });
  const out = new Array(map.buildings.length).fill(null);
  for (const b of map.buildings) {
    const r = b.ring, n = r.length / 2, ccw = ringArea(r) > 0, tally = new Map();
    for (let i = 0; i < n; i++) {
      const ax = r[i * 2], az = r[i * 2 + 1], bx = r[((i + 1) % n) * 2], bz = r[((i + 1) % n) * 2 + 1];
      const L = Math.hypot(bx - ax, bz - az);
      if (L < 1.5) continue;
      // (outwards: for a ring turning anticlockwise in x-z the inside is to the left — (−dz, dx) — so out is (dz, −dx))
      let nx = (bz - az) / L, nz = -(bx - ax) / L;
      if (!ccw) { nx = -nx; nz = -nz; }
      const mx = (ax + bx) / 2, mz = (az + bz) / 2;
      let got = null;
      for (const off of [1.2, 3.5, 6.5]) {
        const px = mx + nx * off, pz = mz + nz * off;
        if (off > 2 && map.buildingAt(px, pz)) break; // (a yard wall, the house behind: not a front)
        let best = null, bd = Infinity;
        for (const id of map.edgesNear(px, pz, 6)) {
          const e = map.edges[id];
          if (!e.name || e.dirt) continue;
          const d = polyNearest(e.pts, e.cum, px, pz).d;
          if (d < e.w / 2 + Math.max(1.2, e.sw || 0) + 1.6 && d < bd) { bd = d; best = e.name; }
        }
        if (best) { got = best; break; }
        for (const sq of squares) if (px > sq.bb[0] && px < sq.bb[2] && pz > sq.bb[1] && pz < sq.bb[3] && pointInRing(px, pz, sq.ring)) { got = sq.name; break; }
        if (got) break;
        if (church) {
          const dx = px - church.x, dz = pz - church.z;
          if (dx * dx + dz * dz < CHURCH_SQUARES.r * CHURCH_SQUARES.r) {
            const bearing = (Math.atan2(dx, -dz) * 180 / Math.PI + 360) % 360; // (0 north, 90 east)
            got = bearing >= 45 && bearing < 225 ? CHURCH_SQUARES.se : CHURCH_SQUARES.nw;
            break;
          }
        }
      }
      if (got) tally.set(got, (tally.get(got) || 0) + L);
    }
    let best = null, bl = 0;
    for (const [k, v] of tally) if (v > bl) { bl = v; best = k; }
    out[b.id] = best;
  }
  return (map._calles = out);
}

// ---------------------------------------------------------------- the styles
// A street's style (calles_estilos.js; all optional; shares are of the street's houses):
//  walls: [[hex, share, kind?], …]         the paint, as it looks in daylight (kind 'ladrillo' or 'piedra': a front of
//                                          bare brick or stone, not paint)
//  kinds: { trad_ocre: 0.5, renovada: 0.3, … } which of the town's façade kinds its houses are built on (textures.js)
//  plinth: [{ kind: 'pintado'|'granito'|'piedra'|'azulejo'|'cemento'|'ninguno'|null, col, h, share }, …]
//  surround: { share, col, kind? }         window and door surrounds (recercados) painted round the openings ('piedra':
//                                          the door's of granite)
//  reja: { share, col, buche }             ground-floor window grilles: how many, their colour, the bellied share
//  balc: share                             upper windows that are balconies
//  garage: share                           ground bays that are garage doors
//  shutters, frames, door, wood            colours (hex) of the roller shutters, the frames, the doors, the carpentry
//  pots: share                             doorsteps and sills with pots (the real streets have far fewer than the game)
//  pretil: share                           houses whose front ends in a parapet before the tiled roof (no tile eaves)
//  lamps: { every }                        wall lanterns, metres apart
//  cables: true                            telephone and power lines along the fronts

// a building's own resolved style on its street, picked once with its seed (the same every load)
const _hexes = new Map();
function weighted(list, r) {
  let t = 0;
  for (const it of list) t += it.share ?? it[1] ?? 1;
  let x = r * t;
  for (const it of list) { x -= it.share ?? it[1] ?? 1; if (x <= 0) return it; }
  return list[list.length - 1];
}
export function houseStyle(street, bid) {
  const S = street && STYLES[street];
  if (!S) return CASAS[bid] ? ownStyle(street, bid, {}) : null;
  const key = street + '|' + bid;
  if (_hexes.has(key)) return _hexes.get(key);
  const rnd = mulberry32(((bid + 1) * 2246822519) >>> 0);
  const w = S.walls ? weighted(S.walls, rnd()) : null;
  const kinds = S.kinds ? Object.entries(S.kinds).map(([k, v]) => [k, v]) : null;
  const pl = S.plinth ? weighted(S.plinth, rnd()) : null;
  const kind = kinds ? weighted(kinds, rnd())[0] : null;
  const out = {
    street,
    wall: w ? w[0] : null,
    kind: w && (w[2] === 'ladrillo' || w[2] === 'piedra') ? w[2] : kind,
    plinth: pl && pl.kind ? { kind: pl.kind, col: pl.col, h: pl.h } : pl ? 'none' : null,
    surround: S.surround && rnd() < S.surround.share ? S.surround.col : null,
    surroundKind: S.surround && S.surround.kind ? S.surround.kind : null,
    reja: S.reja ? rnd() < S.reja.share : null, rejaCol: S.reja ? S.reja.col : null, buche: S.reja ? rnd() < (S.reja.buche || 0) : null,
    balc: S.balc ?? null, garage: S.garage ?? null, pots: S.pots ?? null,
    pretil: S.pretil != null ? rnd() < S.pretil : false,
    shutters: S.shutters || null, frames: S.frames || null, door: S.door || null, wood: S.wood || null,
  };
  _hexes.set(key, CASAS[bid] ? ownStyle(street, bid, out) : out);
  return _hexes.get(key);
}
// a garden seen in the captures (a square's: calles_estilos.js parque — where it is, its ground, its trees): the one
// whose circle holds (x, z), or null
export function parkOf(x, z) {
  for (const k in STYLES) { const p = STYLES[k].parque; if (p && Math.hypot(x - p.x, z - p.z) < p.r) return p; }
  return null;
}
// the names the map leaves out: a stretch of street with none, which its captures show to be part of a named one
// (mapdata.js gives it the name: its style, its signs) — by its index in data/map.json
export const NOMBRES = { 365: 'Calle Eugenio Frutos' }; // (its south branch, towards Herreros: view 60)
// the paint seen on a building in the captures, whatever it is (a shed's too: buildings.js)
export function seenWall(bid) { return (CASAS[bid] && CASAS[bid].wall) || null; }
// and its storeys, as many as are seen (the Catastro's count is now and then one too many or too few)
export function seenFloors(bid) { return (CASAS[bid] && CASAS[bid].floors) || 0; }
// a house seen in the captures (calles_casas.js): what was seen of it over its street's draw
function ownStyle(street, bid, base) {
  const h = CASAS[bid], o = { ...base, street, own: true };
  if (h.wall) o.wall = h.wall;
  if (h.special === 'ladrillo' || h.special === 'piedra') o.kind = h.special;
  else if (h.special === 'tapia') { o.tapia = true; o.kind = 'trad_ocre'; }
  else if (h.special === 'capilla') { o.capilla = true; o.kind = 'trad_ocre'; }
  else if (h.special === 'chapado') o.kind = 'renovada';
  else if (h.wall && (o.kind === 'ladrillo' || o.kind === 'piedra')) o.kind = 'renovada'; // (painted, as seen — not the bare brick or stone its street's draw gave it)
  if (h.plinth) o.plinth = h.plinth.kind === 'ninguno' ? 'none' : { kind: h.plinth.kind, col: h.plinth.col, h: h.plinth.h };
  if (h.surround) { o.surround = h.surround.kind === 'ninguno' ? null : h.surround.col || '#f6f3ec'; o.surroundKind = h.surround.kind === 'piedra' ? 'piedra' : null; }
  if (h.reja != null) o.reja = h.reja;
  if (h.buche != null) o.buche = h.buche;
  if (h.balc != null) o.balc = h.balc ? Math.max(base.balc || 0, 0.65) : 0;
  if (h.door) o.door = h.door;
  if (h.shutters) o.shutters = h.shutters;
  if (h.frames) o.frames = h.frames;
  if (h.pretil != null) o.pretil = h.pretil;
  return o;
}
