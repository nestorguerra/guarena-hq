// Level 0 of the Backrooms, «The Lobby»: the easter egg behind the sacristy door of Santa María, beside the high altar
// (church.js, Interiors.noclip; until 2026-10-11 it was a yellow door on the stage of the theatre of the Casa de la
// Cultura). The internet's legend — a photograph taken in 2002 in an empty
// shop in Oshkosh (Wisconsin), posted in a 4chan thread in 2019 («If you're not careful and you noclip out of reality
// in the wrong areas, you'll end up in the Backrooms…»), and the wiki that grew out of it: an endless maze of empty
// rooms — mono-yellow wallpaper with a chevron print, old damp beige carpet, a drop ceiling of mineral-fibre tiles with
// fluorescent troffers that hum and buzz without end, partitions that make no sense, corridors that lead nowhere.
// Here (the whole design: docs/backrooms.md):
//  - a plan of 40 × 40 cells of 1.2 m (48 m a side) that wraps round on itself: walk out at one side and you come in at
//    the other, and it is drawn 3 × 3 times round you — the level has no end, and you keep meeting the same rooms, as
//    you would there. Two corridors cross it from side to side: they go on for ever
//  - 24 spaces, among them a hall of pillars (one of which does not reach the floor), two rooms the same down to the
//    chair, a corridor that narrows to nothing, a ceiling that comes down, a slit you can see through and not pass, a
//    flight of stairs into the ceiling, a door halfway up a wall, a dark room with one tube that will not die, a
//    corridor of sockets, a room whose wallpaper lies on its side
//  - the light of its 236 troffers, worked out when you arrive for every corner of the walls, floor and ceiling (in the
//    vertices' colours): the pools of light, the partitions' shadows, the darker corners and skirting. The sky's
//    hemisphere light is set to give exactly that back, so the clay of the Plastilina look still shows its prints
//  - textures painted here (canvas): the wallpaper, the carpet, the ceiling tiles, the lenses, the sockets, the stains;
//    in the Plastilina look as pieces of clay
//  - the hum of the lights (audio.js BackroomsHum), louder under a lamp; one tube that flickers and ticks
import * as THREE from 'three';
import { mergeGeometries } from 'three/addons/utils/BufferGeometryUtils.js';
import { INTERIOR_ORIGIN } from './housekit.js';
import { StaticCollider } from './collision.js';
import { STYLE } from './style.js';
import { clayRepaint, PLASTILINA } from './plastilina.js';
import { clamp, smoothstep, hash2 } from './util.js';

export const BR = { C: 1.2, N: 40, H: 2.74, T: 0.12, HD: 2.1 };
const { C, N, H, T, HD } = BR;
const P = C * N;     // 48 m: the plan repeats every 48 m both ways
const HALF = T / 2;
const WP = 1.06;     // the wallpaper's tile (two strips of 53 cm)
const mod = (a) => ((a % N) + N) % N;

// ---------------------------------------------------------------- the plan (cells of 1.2 m; x east, z south)
// Rooms as rectangles of cells [id, x0, z0, x1, z1] (inclusive), painted in order; the cells left out are solid
const ROOMS = [
  ['J', 0, 0, 39, 1],                          // the corridor with no end (east–west, round the plan's edge)
  ['K', 0, 2, 1, 39],                          // and its brother (north–south)
  ['A', 3, 3, 9, 8],                           // where you come in, by the sacristy's door
  ['B', 11, 2, 16, 2], ['B', 10, 3, 16, 8],
  ['C', 17, 2, 39, 13],                        // the hall of pillars
  ['D', 3, 9, 4, 22],                          // a corridor that ends at a wall
  ['E', 5, 9, 10, 14], ['F', 11, 9, 16, 14],   // the twins
  ['T', 5, 15, 16, 15],                        // the narrow passage
  ['S', 17, 14, 20, 15],
  ['G', 21, 14, 22, 26],                       // the corridor that narrows to nothing
  ['H', 24, 14, 31, 20],                       // the ceiling that comes down
  ['I', 32, 14, 39, 27],
  ['L', 5, 16, 12, 23],                        // the stairs into the ceiling
  ['M', 13, 16, 19, 22],                       // the dark room
  ['U', 23, 21, 31, 22],
  ['N', 3, 24, 20, 26],                        // the sockets
  ['O', 23, 23, 31, 29],                       // the door up the wall
  ['Q', 3, 27, 10, 33],                        // the wallpaper on its side
  ['R', 3, 34, 10, 39],
  ['V', 11, 27, 20, 39],                       // partitions
  ['Y', 21, 27, 22, 39],
  ['Z', 23, 30, 31, 39],
  ['W', 32, 28, 39, 39],
];
// The openings (every other edge between two rooms, or a room and the solid, is a partition): [side, x, z, kind] — the
// east ('e') or south ('s') edge of cell (x, z), round the plan's edge too; kind 1 a doorway (the wall goes on over it
// from 2.1 m), 2 open from floor to ceiling, 3 a narrow door (0.9 m), 4 a slit you see through and cannot pass (32 cm)
const OPEN = [
  ['s', 0, 1, 2], ['s', 1, 1, 2], ['s', 0, 39, 2], ['s', 1, 39, 2],                     // J–K (and round the edge)
  ['s', 12, 1, 2], ['s', 13, 1, 2],                                                    // J–B
  ['s', 20, 1, 1], ['s', 27, 1, 2], ['s', 28, 1, 2], ['s', 35, 1, 1],                  // J–C
  ['e', 9, 4, 3], ['e', 9, 6, 1], ['s', 3, 8, 2], ['s', 4, 8, 2],                      // A–B, A–D
  ['e', 16, 5, 1], ['s', 14, 8, 1],                                                    // B–C, B–F
  ['e', 39, 5, 2], ['e', 39, 6, 2], ['e', 39, 10, 1],                                  // C–K (round the edge)
  ['e', 16, 11, 1], ['s', 18, 13, 1], ['s', 21, 13, 2], ['s', 22, 13, 2], ['s', 27, 13, 1], ['s', 35, 13, 2], ['s', 36, 13, 2],
  ['e', 4, 11, 1], ['e', 10, 11, 1],                                                   // D–E–F, in line with F–C: four rooms in a row
  ['e', 4, 15, 1], ['e', 4, 20, 1],                                                    // D–T, D–L
  ['s', 15, 14, 1], ['s', 8, 15, 1], ['s', 14, 15, 1], ['s', 18, 15, 1],              // F–T, T–L, T–M, S–M
  ['e', 16, 15, 4],                                                                    // T–S: the slit
  ['e', 12, 19, 1], ['s', 9, 23, 1],                                                   // L–M, L–N
  ['s', 26, 20, 1], ['e', 31, 17, 1], ['e', 31, 22, 1], ['s', 29, 22, 2], ['s', 30, 22, 2], // H–U, H–I, U–I, U–O
  ['e', 39, 18, 1], ['e', 39, 24, 2], ['e', 31, 25, 1], ['s', 35, 27, 1],             // I–K, O–I, I–W
  ['s', 6, 26, 1], ['s', 15, 26, 2], ['s', 16, 26, 2],                                 // N–Q, N–V
  ['e', 10, 30, 1], ['s', 6, 33, 1], ['s', 7, 39, 1],                                  // Q–V, Q–R, R–J
  ['e', 20, 33, 1], ['s', 13, 39, 2], ['s', 14, 39, 2], ['s', 21, 39, 2], ['s', 22, 39, 2], // V–Y, V–J, Y–J
  ['e', 22, 28, 1], ['e', 22, 35, 3], ['s', 26, 29, 1], ['e', 31, 28, 1],             // Y–O, Y–Z, O–Z, O–W
  ['e', 31, 34, 1], ['s', 28, 39, 1], ['e', 39, 31, 1], ['e', 39, 36, 2], ['s', 34, 39, 1], // Z–W, Z–J, W–K, W–J
];
// partitions standing free in a room, on the grid's lines: [x0, z0, x1, z1] (cells; x0 = x1 or z0 = z1)
const STUBS = [[24, 5, 24, 9], [30, 10, 34, 10], [33, 18, 37, 18], [36, 21, 36, 25], [14, 28, 14, 32], [16, 31, 20, 31], [17, 34, 17, 38], [11, 35, 14, 35], [33, 32, 37, 32], [27, 31, 27, 35], [7, 35, 7, 38]];
// square pillars (60 cm) on grid points [x, z, floating]: one of them stops 30 cm short of the floor
const PILLARS = [[20, 5], [27, 5], [31, 5], [35, 5], [20, 9], [27, 9], [31, 9], [35, 9, true], [34, 23], [37, 15]];
const PIL = 0.3;
// the corridor that narrows (G): two walls closing in from 2.4 m to 30 cm (metres)
const SLANTS = [[25.2, 19.2, 26.25, 32.4], [27.6, 19.2, 26.55, 32.4]];
// the ceiling that comes down: room H, from 2.74 m at its north side to 2.18 m at its south
const SLOPE = { z0: 14 * C, z1: 21 * C, lo: 2.18 };
// a flight of stairs that goes up into the ceiling (room L): x from–to, z from–to (metres), rising east
const STAIRS = { x0: 8.4, x1: 14.4, z0: 26.4, z1: 27.6, n: 16 };
// doors (metres): the yellow one you came in by (A), a small one high up a wall (O), two that do not open (R, W)
// [x, z, facing (rad, 0 = +z), kind, sill, height, width]
const DOORS = [
  [3.6, 6.6, Math.PI / 2, 'exit', 0, 2.04, 0.9],
  [38.4, 33.0, -Math.PI / 2, 'high', 1.2, 1.5, 0.75],
  [3.6, 43.8, Math.PI / 2, 'shut', 0, 2.04, 0.9],
  [46.2, 33.6, 0, 'shut', 0, 2.04, 0.9],
];
// the same office chair, always the same, here and there (metres, facing)
const CHAIRS = [[7.5, 11.8, Math.PI], [14.7, 11.8, Math.PI], [4.3, 30.6, -Math.PI / 2], [28.8, 47.0, 0], [14.0, 44.4, -Math.PI / 2], [41.5, 16.6, Math.PI * 0.75]];
// tubes that flicker (cells): in the dark room, in the hall, in the partitions
const FLICKER = new Set(['16,20', '26,6', '18,31']);

// ---------------------------------------------------------------- the plan, worked out
const ID = new Uint8Array(N * N);   // the room of each cell (its letter's code; 0 solid)
const VE = new Uint8Array(N * N);   // the line x·C between cells x−1 and x, row z: [z·N + x]
const HE = new Uint8Array(N * N);   // the line z·C between rows z−1 and z, column x: [z·N + x]
// what each kind of edge is made of: spans [from, to along it (m), bottom, top]
// 0 nothing · 1 a partition · 2 a doorway (the wall over it) · 3 open · 4 a narrow door · 5 a slit
const SPANS = [[], [[0, C, 0, H]], [[0, C, HD, H]], [], [[0, 0.15, 0, H], [1.05, C, 0, H], [0.15, 1.05, HD, H]], [[0, 0.44, 0, H], [0.76, C, 0, H]]];
(function plan() {
  for (const [r, x0, z0, x1, z1] of ROOMS) for (let z = z0; z <= z1; z++) for (let x = x0; x <= x1; x++) ID[z * N + x] = r.charCodeAt(0);
  for (let z = 0; z < N; z++) for (let x = 0; x < N; x++) {
    const b = ID[z * N + x], a = ID[z * N + mod(x - 1)], c = ID[mod(z - 1) * N + x];
    if (a !== b) VE[z * N + x] = 1;
    if (c !== b) HE[z * N + x] = 1;
  }
  for (const [sd, x, z, k] of OPEN) { if (sd === 'e') VE[z * N + mod(x + 1)] = k + 1; else HE[mod(z + 1) * N + x] = k + 1; }
  for (const [x0, z0, x1, z1] of STUBS) {
    if (x0 === x1) for (let z = z0; z < z1; z++) VE[mod(z) * N + mod(x0)] = 1;
    else for (let x = x0; x < x1; x++) HE[mod(z0) * N + mod(x)] = 1;
  }
})();
const cellId = (x, z) => ID[mod(z) * N + mod(x)];
const roomAt = (u, v) => String.fromCharCode(cellId(Math.floor(u / C), Math.floor(v / C)) || 35);
// the ceiling's height (m): over a point, and along a cell of a given room at v (exact on its edges: the tiles of the
// slope meet without a crack)
const slopeY = (v) => { const q = ((v % P) + P) % P; return H - (H - SLOPE.lo) * clamp((q - SLOPE.z0) / (SLOPE.z1 - SLOPE.z0), 0, 1); };
const ceilOf = (room, v) => (room === 'H' ? slopeY(v) : H);
function ceilAt(u, v) { return ceilOf(roomAt(u, v), v); }
function blocks(ty, s, y) {
  for (const sp of SPANS[ty]) if (s >= sp[0] - 1e-4 && s <= sp[1] + 1e-4 && y >= sp[2] - 1e-4 && y <= sp[3] + 1e-4) return true;
  return false;
}

// ---------------------------------------------------------------- the lamps
// a troffer of 0.6 × 1.2 m in the ceiling's grid, along x or z; st 0 lit, 1 dead, 2 flickering. Rooms: one every second
// cell across and third down (an office's grid, «inconsistently placed»: a few missing, moved or dead); corridors:
// down their middle
const LAMPS = [];
const CORR = { J: ['x', 0], U: ['x', 21], T: ['x', 15], K: ['z', 0], D: ['z', 3], Y: ['z', 21], G: ['z', 21] };
(function lamps() {
  const box = new Map();
  for (const [r, x0, z0] of ROOMS) if (!box.has(r)) box.set(r, [x0, z0]);
  for (let z = 0; z < N; z++) for (let x = 0; x < N; x++) {
    const r = String.fromCharCode(ID[z * N + x] || 35);
    if (r === '#') continue;
    const co = CORR[r], hs = hash2(x * 7 + 3, z * 13 + 5);
    let ax, ok;
    if (co) {
      ax = co[0];
      ok = ax === 'x' ? z === co[1] && x % 3 === 1 : x === co[1] && (r === 'G' ? z % 2 === 0 && z <= 20 : z % 3 === 1);
    } else {
      const [bx, bz] = box.get(r);
      ax = 'z'; ok = (x - bx) % 2 === 1 && (z - bz) % 3 === 1;
    }
    if (!ok) continue;
    const key = x + ',' + z, flick = FLICKER.has(key), keep = r === 'A'; // (where you arrive, every tube works)
    if (!flick && !keep && hs < 0.05) continue; // (missing)
    let st = flick ? 2 : r === 'M' ? 1 : !keep && hs < 0.09 ? 1 : 0;
    // its place in the ceiling's grid of 60 cm tiles: [u0, v0] its corner, along ax
    let u0, v0;
    if (ax === 'x') { u0 = x * C; v0 = r === 'J' || r === 'U' ? z * C + 0.6 : z * C; }
    else { u0 = r === 'G' ? x * C + 0.6 : x * C + (co ? 0.6 : 0); v0 = z * C; }
    if (!co && hs > 0.93) u0 += 0.6; // (one here and there a tile across)
    const cx = ax === 'x' ? u0 + 0.6 : u0 + 0.3, cz = ax === 'x' ? v0 + 0.3 : v0 + 0.6;
    LAMPS.push({ u0, v0, ax, st, x: cx, z: cz, y: ceilAt(cx, cz) - 0.02 });
  }
})();
// every lamp's light: its copies in the 3 × 3 plans round (the level repeats), binned by 2.4 m for the lookups
const LR = 7.5, LR2 = LR * LR, BIN = 2.4, BO = LR + 1, NB = Math.ceil((P + 2 * BO) / BIN);
let lampBins = null;
function lampIndex() {
  if (lampBins) return lampBins;
  lampBins = Array.from({ length: NB * NB }, () => []);
  for (const l of LAMPS) {
    if (l.st === 1) continue;
    const ex = l.ax === 'x' ? 0.3 : 0, ez = l.ax === 'z' ? 0.3 : 0;
    for (let i = -1; i <= 1; i++) for (let j = -1; j <= 1; j++) {
      const x = l.x + i * P, z = l.z + j * P;
      if (x < -BO || x > P + BO || z < -BO || z > P + BO) continue;
      lampBins[Math.floor((z + BO) / BIN) * NB + Math.floor((x + BO) / BIN)].push({ x, y: l.y, z, ex, ez, st: l.st });
    }
  }
  return lampBins;
}

// ---------------------------------------------------------------- what stands in the light's way
// the extra blockers besides the partitions: the pillars (boxes) and the narrowing walls (segments, floor to ceiling)
const BLOCK = [];
for (const [x, z, fl] of PILLARS) BLOCK.push({ box: [x * C - PIL, fl ? 0.3 : 0, z * C - PIL, x * C + PIL, H, z * C + PIL] });
for (const s of SLANTS) BLOCK.push({ seg: s });
// is the straight line from a to b clear of every partition (over the doorways, under the walls' tops), pillar and slant?
function clearRay(ax, ay, az, bx, by, bz) {
  const dx = bx - ax, dy = by - ay, dz = bz - az;
  if (Math.abs(dx) > 1e-9) {
    const k0 = Math.floor(ax / C), k1 = Math.floor(bx / C);
    if (dx > 0) { for (let k = k0 + 1; k <= k1; k++) if (lineHit(VE, k, (k * C - ax) / dx, az, dz, ay, dy)) return false; }
    else for (let k = k0; k > k1; k--) if (lineHit(VE, k, (k * C - ax) / dx, az, dz, ay, dy)) return false;
  }
  if (Math.abs(dz) > 1e-9) {
    const k0 = Math.floor(az / C), k1 = Math.floor(bz / C);
    if (dz > 0) { for (let k = k0 + 1; k <= k1; k++) if (lineHitH(k, (k * C - az) / dz, ax, dx, ay, dy)) return false; }
    else for (let k = k0; k > k1; k--) if (lineHitH(k, (k * C - az) / dz, ax, dx, ay, dy)) return false;
  }
  for (const b of BLOCK) {
    if (b.box) {
      const [x0, y0, z0, x1, y1, z1] = b.box;
      if (Math.max(ax, bx) < x0 || Math.min(ax, bx) > x1 || Math.max(az, bz) < z0 || Math.min(az, bz) > z1) continue;
      let t0 = 1e-4, t1 = 1 - 1e-4;
      for (const [o, d, lo, hi] of [[ax, dx, x0, x1], [ay, dy, y0, y1], [az, dz, z0, z1]]) {
        if (Math.abs(d) < 1e-9) { if (o < lo || o > hi) { t0 = 2; break; } continue; }
        let ta = (lo - o) / d, tb = (hi - o) / d; if (ta > tb) [ta, tb] = [tb, ta];
        t0 = Math.max(t0, ta); t1 = Math.min(t1, tb); if (t0 > t1) break;
      }
      if (t0 <= t1) return false;
    } else {
      const [x0, z0, x1, z1] = b.seg, ex = x1 - x0, ez = z1 - z0, den = dx * ez - dz * ex;
      if (Math.abs(den) < 1e-9) continue;
      const t = ((x0 - ax) * ez - (z0 - az) * ex) / den, s = ((x0 - ax) * dz - (z0 - az) * dx) / den;
      if (t > 1e-4 && t < 1 - 1e-4 && s >= 0 && s <= 1) return false;
    }
  }
  return true;
}
function lineHit(E, k, t, az, dz, ay, dy) {
  if (t <= 1e-6 || t >= 1 - 1e-6) return false;
  const z = az + t * dz, row = Math.floor(z / C), ty = E[mod(row) * N + mod(k)];
  return ty !== 0 && blocks(ty, z - row * C, ay + t * dy);
}
function lineHitH(k, t, ax, dx, ay, dy) {
  if (t <= 1e-6 || t >= 1 - 1e-6) return false;
  const x = ax + t * dx, col = Math.floor(x / C), ty = HE[mod(k) * N + mod(col)];
  return ty !== 0 && blocks(ty, x - col * C, ay + t * dy);
}
// how far (m) from (x, z) the nearest wall face is that runs north–south, and the nearest that runs east–west, at
// height y — for the darker skirting and corners
function wallDist(x, z, y) {
  let ex = 9, ez = 9;
  const cx = Math.floor(x / C), cz = Math.floor(z / C);
  for (let k = cx - 1; k <= cx + 2; k++) { const ty = VE[mod(cz) * N + mod(k)]; if (ty && blocks(ty, z - cz * C, y)) ex = Math.min(ex, Math.max(0, Math.abs(x - k * C) - HALF)); }
  for (let k = cz - 1; k <= cz + 2; k++) { const ty = HE[mod(k) * N + mod(cx)]; if (ty && blocks(ty, x - cx * C, y)) ez = Math.min(ez, Math.max(0, Math.abs(z - k * C) - HALF)); }
  for (const b of BLOCK) {
    if (!b.box) continue;
    const [x0, y0, z0, x1, , z1] = b.box;
    if (y < y0) continue;
    if (z > z0 && z < z1) ex = Math.min(ex, Math.max(0, x < x0 ? x0 - x : x - x1));
    if (x > x0 && x < x1) ez = Math.min(ez, Math.max(0, z < z0 ? z0 - z : z - z1));
  }
  return [ex, ez];
}

// ---------------------------------------------------------------- the light, worked out once
// irradiance from the troffers (Lambertian panels facing down): direct (with the cosines, the partitions' shadows) and
// a softer bounce (all round, through the same openings) for what faces away — the ceiling above all; a little ambient
// (calibrated against the photographs: walls ~(200, 182, 110) on the screen, the carpet ~(150, 128, 82), the ceiling a
// little darker than the walls; the hemisphere light gives L × the albedo back: its intensity is π)
const LIT = { kd: 4.4, ki: 0.18, kc: 0.6, amb: 0.06, col: [1.0, 0.99, 0.94], hg: 0.6 };
// the hemisphere light gives back hemiK(n) of its sky colour to a surface facing n: the colours are divided by it
const hemiK = (ny) => LIT.hg + (1 - LIT.hg) * (0.5 + 0.5 * ny);
function lightAt(px, py, pz, nx, ny, nz) {
  const bins = lampIndex();
  let dir = 0, ind = 0, fd = 0, fi = 0;
  const bx0 = Math.max(0, Math.floor((px - LR + BO) / BIN)), bx1 = Math.min(NB - 1, Math.floor((px + LR + BO) / BIN));
  const bz0 = Math.max(0, Math.floor((pz - LR + BO) / BIN)), bz1 = Math.min(NB - 1, Math.floor((pz + LR + BO) / BIN));
  for (let bz = bz0; bz <= bz1; bz++) for (let bx = bx0; bx <= bx1; bx++) for (const l of bins[bz * NB + bx]) {
    const hx = l.x - px, hz = l.z - pz, h2 = hx * hx + hz * hz;
    if (h2 > LR2) continue;
    // near a lamp its two ends (soft shadows at a doorway's edge); further off its middle
    const pts = h2 < 12 ? [[l.x - l.ex, l.z - l.ez, 0.5], [l.x + l.ex, l.z + l.ez, 0.5]] : [[l.x, l.z, 1]];
    for (const [sx, sz, w] of pts) {
      const dx = sx - px, dy = l.y - py, dz = sz - pz, d2 = dx * dx + dy * dy + dz * dz;
      if (!clearRay(px, py, pz, sx, l.y - 0.02, sz)) continue;
      const i = w / (d2 + 2.4);
      let e = 0;
      if (dy > 0.02) { const d = Math.sqrt(d2), cr = (nx * dx + ny * dy + nz * dz) / d; if (cr > 0) e = (w * (dy / d) * cr) / Math.max(d2, 0.25); }
      if (l.st === 2) { fd += e; fi += i; } else { dir += e; ind += i; }
    }
  }
  return [dir, ind, fd, fi];
}

// the glow on the tiles round a tube (its lens and frame light them a little): [lit tubes', the flickering one's]
function nearLamp(px, pz) {
  const bins = lampIndex(), bx = Math.floor((px + BO) / BIN), bz = Math.floor((pz + BO) / BIN);
  let g = 0, f = 0;
  for (let j = bz - 1; j <= bz + 1; j++) for (let i = bx - 1; i <= bx + 1; i++) {
    if (i < 0 || j < 0 || i >= NB || j >= NB) continue;
    for (const l of bins[j * NB + i]) {
      const hx = Math.max(0, Math.abs(px - l.x) - (l.ex ? 0.6 : 0.3)), hz = Math.max(0, Math.abs(pz - l.z) - (l.ez ? 0.6 : 0.3));
      const v = Math.exp(-(hx * hx + hz * hz) / 0.3);
      if (l.st === 2) f += v; else g += v;
    }
  }
  return [g, f];
}

// value noise that wraps every `per` steps (the textures tile; the plan's stains repeat with the plan)
function hashI(x, y, s) { let h = (Math.imul(x, 374761393) + Math.imul(y, 668265263) + Math.imul(s, 1442695041)) | 0; h = Math.imul(h ^ (h >>> 13), 1274126177); return ((h ^ (h >>> 16)) >>> 0) / 4294967296; }
function pnoise(x, y, px, py, s = 0) {
  const xi = Math.floor(x), yi = Math.floor(y), fx = x - xi, fy = y - yi, u = fx * fx * (3 - 2 * fx), v = fy * fy * (3 - 2 * fy);
  const x0 = ((xi % px) + px) % px, x1 = (x0 + 1) % px, y0 = ((yi % py) + py) % py, y1 = (y0 + 1) % py;
  const a = hashI(x0, y0, s), b = hashI(x1, y0, s), c = hashI(x0, y1, s), d = hashI(x1, y1, s);
  return a + (b - a) * u + (c - a) * v + (a - b - c + d) * u * v;
}
// the same over the plan: `f` steps across its 48 m
const wnoise = (x, z, f, s) => pnoise((x / P) * f, (z / P) * f, f, f, s);

// the colour a vertex takes: its light (and the flickering tube's, apart), its corner's shade, the dirt of years
const NOBASE = [0, 0, 0, 0, 0, 0];
function shade(kind, x, y, z, nx, ny, nz) {
  // (a hair off the surface, into the room: never exactly on a line of the grid)
  const qx = x + nx * 0.03, qy = y + ny * 0.03, qz = z + nz * 0.03;
  const [dir, ind, fd, fi] = lightAt(qx, qy, qz, nx, ny, nz);
  // the ceiling sees only what the room sends back up (and the glow round each tube); the rest, the tubes themselves
  const ki = kind === 'ceil' ? LIT.kc : LIT.ki;
  let l = LIT.amb + LIT.kd * dir + ki * ind, f = LIT.kd * fd + ki * fi;
  if (kind === 'ceil') { const g0 = nearLamp(qx, qz); l += 0.35 * g0[0]; f += 0.35 * g0[1]; }
  let ao = 1, r = 1, g = 1, b = 1;
  if (kind === 'floor' || kind === 'ceil') {
    const [ex, ez] = wallDist(qx, qz, kind === 'floor' ? 0.05 : ceilAt(qx, qz) - 0.05), k = kind === 'floor' ? 0.42 : 0.3;
    ao = (1 - k * Math.exp(-ex / 0.24)) * (1 - k * Math.exp(-ez / 0.24));
    if (kind === 'floor') {
      // the carpet: damp where the stains spread (darker, a little browner), greyer along the walls
      const wet = smoothstep(0.58, 0.76, wnoise(x, z, 12, 7)) * 0.2 + smoothstep(0.64, 0.82, wnoise(x, z, 30, 9)) * 0.1;
      const m = 1 + 0.07 * (wnoise(x, z, 20, 3) - 0.5);
      r = m * (1 - wet); g = m * (1 - wet * 1.06); b = m * (1 - wet * 1.25);
      const edge = Math.exp(-Math.min(ex, ez) / 0.4) * 0.08; r -= edge; g -= edge; b -= edge * 0.9;
    } else { const m = 1 + 0.06 * (wnoise(x, z, 24, 5) - 0.5); r = g = m; b = m * 0.99; }
  } else if (kind === 'wall') {
    const [ex, ez] = wallDist(qx, qz, y);
    const side = Math.abs(nx) > 0.5 ? ez : ex; // (the corner: a wall across this one)
    const hc = ceilAt(qx, qz);
    ao = (1 - 0.34 * Math.exp(-y / 0.16)) * (1 - 0.26 * Math.exp(-Math.max(0, hc - y) / 0.14)) * (1 - 0.3 * Math.exp(-side / 0.22));
    // dirt kicked up at the foot, smoke and age under the ceiling, the years in big soft patches
    const big = wnoise(x + y * 0.31, z - y * 0.27, 16, 11), low = Math.exp(-y / 0.32) * 0.09;
    const top = Math.exp(-Math.max(0, hc - y) / 0.5) * 0.1, m = 1 + 0.08 * (big - 0.5);
    r = m * (1 - low) * (1 - top * 0.25); g = m * (1 - low * 1.04) * (1 - top * 0.45); b = m * (1 - low * 1.1) * (1 - top * 1.1);
  } else ao = 1;
  const hk = hemiK(ny), c = LIT.col;
  return [l * c[0] * r * ao / hk, l * c[1] * g * ao / hk, l * c[2] * b * ao / hk, f * c[0] * r * ao / hk, f * c[1] * g * ao / hk, f * c[2] * b * ao / hk];
}
// the light at a point for a small thing (a socket, a chair): one colour for all of it, lit from above
function shadePoint(x, y, z) { return shade('prop', x, y, z, 0, 1, 0); }

// ---------------------------------------------------------------- textures (painted here; cached for the session)
const TEX = new Map();
function canvas(w, h) { const c = document.createElement('canvas'); c.width = w; c.height = h; return c; }
function texOf(key, c, srgb = true, repeat = true) {
  const t = new THREE.CanvasTexture(c);
  if (srgb) t.colorSpace = THREE.SRGBColorSpace;
  if (repeat) t.wrapS = t.wrapT = THREE.RepeatWrapping;
  t.anisotropy = 8;
  TEX.set(key, t);
  return t;
}
// fill a canvas pixel by pixel: fn(x, y, out) writes r, g, b (0–255) and optionally a
function paint(w, h, fn) {
  const c = canvas(w, h), x = c.getContext('2d', { willReadFrequently: true }), im = x.createImageData(w, h), d = im.data, o = [0, 0, 0, 255];
  for (let py = 0; py < h; py++) for (let px = 0; px < w; px++) {
    o[3] = 255; fn(px, py, o);
    const i = (py * w + px) * 4;
    d[i] = o[0]; d[i + 1] = o[1]; d[i + 2] = o[2]; d[i + 3] = o[3];
  }
  x.putImageData(im, 0, 0);
  return c;
}
function clayify(c, opts) {
  const x = c.getContext('2d', { willReadFrequently: true }), im = x.getImageData(0, 0, c.width, c.height);
  clayRepaint(im.data, c.width, 1, opts);
  x.putImageData(im, 0, 0);
  return c;
}
// the wallpaper: two strips of 53 cm (1024 px = 1.06 m), a print of chevrons in columns of 6.6 cm, a pinstripe between,
// the paper's fibres running down the roll and a little mottled, the seam between the strips; and its relief (bump)
function wallpaperTex(clay) {
  const k = 'wall' + clay;
  if (TEX.has(k)) return [TEX.get(k), TEX.get(k + 'b')];
  const S = 1024, COL = 64, PER = 34, base = clay ? [226, 205, 128] : [220, 200, 124], ink = clay ? [0.88, 0.855, 0.77] : [0.9, 0.88, 0.8];
  const arm = clay ? 2.6 : 1.7;
  const mark = (px, py) => {
    const cx = Math.floor(px / COL) * COL + COL / 2, adx = Math.abs(px + 0.5 - cx);
    const ty = (((py + 0.5 + adx * 0.9) % PER) + PER) % PER, d = Math.abs(ty - PER / 2);
    const chev = smoothstep(arm + 0.9, arm - 0.4, d) * smoothstep(19.5, 17, adx);
    const sm = Math.min(px % COL, COL - (px % COL)), stripe = smoothstep(1.4, 0.3, sm);
    const seam = Math.min(px % 512, 512 - (px % 512));
    return [chev, stripe, seam];
  };
  const col = paint(S, S, (px, py, o) => {
    const [chev, stripe, seam] = mark(px, py);
    const fib = pnoise(px / 2, py / 8, 512, 128, 3), mot = pnoise(px / 32, py / 32, 32, 32, 4), big = pnoise(px / 128, py / 128, 8, 8, 5);
    let m = 1 + 0.032 * (fib - 0.5) * (clay ? 0.4 : 1) + 0.03 * (mot - 0.5) + 0.022 * (big - 0.5);
    if (px >= 512) m *= 0.988; // (the second strip from another roll)
    m *= 1 + 0.05 * stripe;
    if (!clay) { if (seam < 0.8) m *= 0.78; else if (seam < 3) m *= 1.045; }
    o[0] = base[0] * m * (1 - chev + chev * ink[0]); o[1] = base[1] * m * (1 - chev + chev * ink[1]); o[2] = base[2] * m * (1 - chev + chev * ink[2]);
  });
  const bump = paint(S, S, (px, py, o) => {
    const [chev, stripe, seam] = mark(px, py), fib = pnoise(px / 2, py / 8, 512, 128, 3);
    const v = 128 + (clay ? -46 : 34) * chev + 12 * stripe + (clay ? 4 : 16) * (fib - 0.5) - (!clay && seam < 1.2 ? 50 : 0);
    o[0] = o[1] = o[2] = v;
  });
  if (clay) clayify(col, { blur: 2, levels: 6, posterize: 0.3, saturation: 1.06 });
  return [texOf(k, col), texOf(k + 'b', bump, false)];
}
// the carpet: a loop pile in rows (4.7 mm), heathered with three tones of tan, a little mottled (1024 px = 1.2 m)
function carpetTex(clay) {
  const k = 'carpet' + clay;
  if (TEX.has(k)) return [TEX.get(k), TEX.get(k + 'b')];
  const S = 1024, T1 = [168, 148, 108], T2 = [144, 125, 89], T3 = [114, 98, 69];
  const loop = (px, py) => {
    const row = Math.floor(py / 4), fy = (py % 4 + 0.5) / 4, off = hashI(row, 0, 21) * 2.56;
    const xx = (px + off) / 2.56, ci = Math.floor(xx), fx = xx - ci, sh = Math.sin(Math.PI * fx) * Math.sqrt(Math.sin(Math.PI * fy));
    return [hashI(((ci % 400) + 400) % 400, row, 22), sh];
  };
  const col = paint(S, S, (px, py, o) => {
    const [t, sh] = loop(px, py), tone = t < 0.46 ? T1 : t < 0.86 ? T2 : T3;
    const m = (clay ? 0.94 + 0.06 * sh : 0.8 + 0.2 * sh) * (1 + 0.05 * (pnoise(px / 16, py / 16, 64, 64, 23) - 0.5) + 0.04 * (pnoise(px / 128, py / 128, 8, 8, 24) - 0.5));
    const c0 = clay ? [154, 136, 96] : tone;
    o[0] = c0[0] * m; o[1] = c0[1] * m; o[2] = c0[2] * m;
  });
  const bump = paint(S, S, (px, py, o) => { const [, sh] = loop(px, py); o[0] = o[1] = o[2] = 100 + 110 * sh; });
  if (clay) clayify(col, { blur: 3, levels: 5, posterize: 0.35, saturation: 1.05 });
  return [texOf(k, col), texOf(k + 'b', bump, false)];
}
// the ceiling's tiles: four kinds in one picture (2 × 2, each 512 px = 60 cm): new, yellowed, with a water stain, old
// and cracked — mineral fibre full of fissures and pinholes, the white T-bar of the grid round each
function ceilingTex(clay) {
  const k = 'ceil' + clay;
  if (TEX.has(k)) return [TEX.get(k), TEX.get(k + 'b')];
  const S = 1024, c = canvas(S, S), x = c.getContext('2d'), b = canvas(S, S), y = b.getContext('2d');
  const R = (s) => { let t = s; return () => { t = (t * 16807) % 2147483647; return t / 2147483647; }; };
  for (let q = 0; q < 4; q++) {
    const ox = (q % 2) * 512, oy = Math.floor(q / 2) * 512, r = R(1000 + q * 77);
    // the body
    const body = paint(512, 512, (px, py, o) => {
      const m = 1 + 0.035 * (pnoise(px / 24, py / 24, 21, 21, 30 + q) - 0.5) + 0.025 * (pnoise(px / 5, py / 5, 102, 102, 40 + q) - 0.5);
      const yel = q === 1 ? 0.06 * (px + py) / 1024 : q === 3 ? 0.04 : 0;
      o[0] = 223 * m * (1 - yel * 0.3); o[1] = 218 * m * (1 - yel * 0.6); o[2] = 198 * m * (1 - yel * 1.6);
    });
    x.drawImage(body, ox, oy);
    y.fillStyle = '#808080'; y.fillRect(ox, oy, 512, 512);
    // the fissures and pinholes of mineral fibre
    for (const [ctx, ink] of [[x, 'rgba(120,112,92,'], [y, 'rgba(20,20,20,']]) {
      const rr = R(2000 + q * 31);
      ctx.save(); ctx.beginPath(); ctx.rect(ox + 12, oy + 12, 488, 488); ctx.clip();
      for (let i = 0; i < 210; i++) {
        let px = ox + 12 + rr() * 488, py = oy + 12 + rr() * 488, a = rr() * 6.28;
        ctx.strokeStyle = ink + (0.22 + rr() * 0.25) + ')'; ctx.lineWidth = 1.2 + rr() * 1.6; ctx.beginPath(); ctx.moveTo(px, py);
        const n = 3 + Math.floor(rr() * 5);
        for (let j = 0; j < n; j++) { a += (rr() - 0.5) * 1.4; px += Math.cos(a) * (3 + rr() * 5); py += Math.sin(a) * (3 + rr() * 5); ctx.lineTo(px, py); }
        ctx.stroke();
      }
      for (let i = 0; i < 1700; i++) { ctx.fillStyle = ink + (0.3 + rr() * 0.4) + ')'; ctx.beginPath(); ctx.arc(ox + 12 + rr() * 488, oy + 12 + rr() * 488, 0.6 + rr() * 1.1, 0, 6.283); ctx.fill(); }
      ctx.restore();
    }
    // a water stain: the brown tide line of a leak that dried, the paler ring inside
    if (q === 2) {
      const cx = ox + 230 + r() * 60, cy = oy + 250 + r() * 60, R0 = 120 + r() * 50;
      for (let ring = 0; ring < 3; ring++) {
        const rad = R0 * (1 - ring * 0.22);
        x.beginPath();
        for (let a = 0; a <= 6.3; a += 0.12) { const rr2 = rad * (0.82 + 0.3 * pnoise(a * 2, ring * 3, 13, 13, 50)); a === 0 ? x.moveTo(cx + Math.cos(a) * rr2, cy + Math.sin(a) * rr2) : x.lineTo(cx + Math.cos(a) * rr2, cy + Math.sin(a) * rr2); }
        x.closePath();
        x.fillStyle = `rgba(168,138,80,${0.1 + ring * 0.05})`; x.fill();
        x.strokeStyle = `rgba(130,96,44,${0.45 - ring * 0.1})`; x.lineWidth = 3 - ring * 0.6; x.stroke();
      }
    }
    // an old tile: a crack across it, a sag (darker to one side)
    if (q === 3) {
      const g = x.createLinearGradient(ox, oy, ox + 512, oy + 512); g.addColorStop(0, 'rgba(0,0,0,0)'); g.addColorStop(1, 'rgba(60,50,30,0.12)'); x.fillStyle = g; x.fillRect(ox + 12, oy + 12, 488, 488);
      for (const [ctx, st] of [[x, 'rgba(70,62,48,0.7)'], [y, 'rgba(0,0,0,0.9)']]) { ctx.strokeStyle = st; ctx.lineWidth = 2; ctx.beginPath(); let px = ox + 40, py = oy + 140; ctx.moveTo(px, py); const rr = R(77); for (let j = 0; j < 14; j++) { px += 26 + rr() * 8; py += (rr() - 0.4) * 30; ctx.lineTo(px, py); } ctx.stroke(); }
    }
    // the grid's T-bar round it: white enamel, a thin shadow line where the tile sits on its flange
    const bw = clay ? 13 : 10; // (in clay a roll a little wider: the smoothing would lose a thin one)
    for (const [ctx, bar, line, sh] of [[x, '#ecE9de', 'rgba(90,86,74,0.9)', clay ? 'rgba(60,55,40,0.6)' : 'rgba(60,55,40,0.35)'], [y, '#b8b8b8', '#202020', 'rgba(0,0,0,0.5)']]) {
      ctx.fillStyle = bar; ctx.fillRect(ox, oy, 512, bw); ctx.fillRect(ox, oy + 512 - bw, 512, bw); ctx.fillRect(ox, oy, bw, 512); ctx.fillRect(ox + 512 - bw, oy, bw, 512);
      ctx.fillStyle = line; ctx.fillRect(ox, oy, 512, clay ? 2 : 1); ctx.fillRect(ox, oy, clay ? 2 : 1, 512); ctx.fillRect(ox, oy + 511, 512, 1); ctx.fillRect(ox + 511, oy, 1, 512);
      ctx.strokeStyle = sh; ctx.lineWidth = clay ? 4 : 2.5; ctx.strokeRect(ox + bw + 1.5, oy + bw + 1.5, 509 - 2 * bw, 509 - 2 * bw);
    }
  }
  if (clay) { clayify(c, { blur: 3, levels: 5, posterize: 0.4, saturation: 1.04 }); clayify(b, { blur: 4, levels: 8, posterize: 0, saturation: 1 }); }
  return [texOf(k, c), texOf(k + 'b', b, false)];
}
// a troffer's lens: a prismatic acrylic sheet (a fine diamond pattern), the two tubes behind it brighter, its edges darker
function lensTex() {
  if (TEX.has('lens')) return TEX.get('lens');
  const c = paint(256, 512, (px, py, o) => {
    const tri = (v) => Math.abs((((v % 2) + 2) % 2) - 1);
    const pr = 0.9 + 0.1 * tri((px + py) / 5) * tri((px - py) / 5);
    const tubes = Math.exp(-(((px - 85) / 24) ** 2)) + Math.exp(-(((px - 171) / 24) ** 2));
    const edge = smoothstep(0, 16, Math.min(px, 255 - px, py, 511 - py));
    const v = Math.min(255, 228 * pr * (0.72 + 0.28 * edge) * (0.86 + 0.2 * tubes));
    o[0] = v; o[1] = v * 0.99; o[2] = v * 0.92;
  });
  return texOf('lens', c, true, false);
}
// a wall socket (US duplex, as the photographs'): its ivory plate, two outlets, the screw
function socketTex() {
  if (TEX.has('socket')) return TEX.get('socket');
  const c = canvas(128, 192), x = c.getContext('2d');
  const g = x.createLinearGradient(0, 0, 128, 192); g.addColorStop(0, '#f2ecd8'); g.addColorStop(1, '#ddd4bb'); x.fillStyle = g; x.fillRect(0, 0, 128, 192);
  x.strokeStyle = 'rgba(80,70,50,0.35)'; x.lineWidth = 4; x.strokeRect(2, 2, 124, 188);
  for (const cy of [52, 140]) {
    x.fillStyle = '#e6dec6'; x.beginPath(); x.ellipse(64, cy, 34, 30, 0, 0, 6.283); x.fill();
    x.strokeStyle = 'rgba(70,60,40,0.4)'; x.lineWidth = 2; x.stroke();
    x.fillStyle = '#2a2420'; x.fillRect(46, cy - 16, 7, 20); x.fillRect(75, cy - 16, 7, 22);
    x.beginPath(); x.arc(64, cy + 16, 6, Math.PI, 0); x.lineTo(70, cy + 22); x.lineTo(58, cy + 22); x.fill();
  }
  x.fillStyle = '#b8b2a0'; x.beginPath(); x.arc(64, 96, 6, 0, 6.283); x.fill(); x.strokeStyle = '#5a5448'; x.lineWidth = 1.5; x.beginPath(); x.moveTo(59, 96); x.lineTo(69, 96); x.stroke();
  return texOf('socket', c, true, false);
}
// stains for the walls (four, side by side: streaks run down from the ceiling, a damp bloom with its tide line, scuffs
// at the foot, the paper peeling at a seam) and for the carpet (a wet patch, a ring), on transparent canvas
function stainTex(clay) {
  const k = 'stain' + clay;
  if (TEX.has(k)) return TEX.get(k);
  const c = canvas(1024, 512), x = c.getContext('2d');
  const R = (s) => { let t = s; return () => { t = (t * 16807) % 2147483647; return t / 2147483647; }; };
  // 0: streaks from the top
  { const r = R(11); for (let i = 0; i < 9; i++) { const sx = 30 + r() * 196, w = 6 + r() * 22, len = 160 + r() * 330; const g = x.createLinearGradient(0, 0, 0, len); g.addColorStop(0, 'rgba(120,92,46,0.42)'); g.addColorStop(0.7, 'rgba(120,92,46,0.18)'); g.addColorStop(1, 'rgba(120,92,46,0)'); x.fillStyle = g; x.beginPath(); x.moveTo(sx, 0); for (let yy = 0; yy <= len; yy += 12) x.lineTo(sx + Math.sin(yy * 0.05 + i) * 3, yy); for (let yy = len; yy >= 0; yy -= 12) x.lineTo(sx + w + Math.sin(yy * 0.06 + i * 2) * 3, yy); x.fill(); } }
  // 1: a damp bloom
  { const cx = 384, cy = 230; for (let ring = 0; ring < 4; ring++) { x.beginPath(); for (let a = 0; a <= 6.3; a += 0.1) { const rr = (100 - ring * 18) * (0.8 + 0.35 * pnoise(a * 2.2, ring, 14, 9, 60)); const px = cx + Math.cos(a) * rr * 1.1, py = cy + Math.sin(a) * rr * 1.5; a === 0 ? x.moveTo(px, py) : x.lineTo(px, py); } x.closePath(); x.fillStyle = `rgba(138,110,58,${0.07 + ring * 0.035})`; x.fill(); x.strokeStyle = `rgba(112,84,38,${0.32 - ring * 0.06})`; x.lineWidth = 2.5; x.stroke(); } }
  // 2: scuffs at the foot
  { const r = R(33); for (let i = 0; i < 26; i++) { const px = 520 + r() * 220, py = 420 + r() * 80, w = 12 + r() * 50; x.fillStyle = `rgba(70,62,52,${0.06 + r() * 0.12})`; x.beginPath(); x.ellipse(px, py, w, 3 + r() * 6, (r() - 0.5) * 0.3, 0, 6.283); x.fill(); } }
  // 3: paper peeling at a seam: the paper's pale back where it curls off, its shadow, the bare plaster under it
  { const sh = x.createLinearGradient(900, 0, 916, 0); sh.addColorStop(0, 'rgba(60,46,20,0.3)'); sh.addColorStop(1, 'rgba(60,46,20,0)');
    x.fillStyle = sh; x.beginPath(); x.moveTo(900, 0); x.lineTo(918, 0); x.bezierCurveTo(916, 120, 908, 220, 901, 300); x.closePath(); x.fill();
    x.fillStyle = 'rgba(248,240,210,0.6)'; x.beginPath(); x.moveTo(897, 0); x.lineTo(901, 0); x.bezierCurveTo(901, 110, 900, 200, 899, 270); x.bezierCurveTo(898, 200, 897, 100, 897, 0); x.fill();
    x.fillStyle = 'rgba(240,230,196,0.85)'; x.beginPath(); x.moveTo(898, 0); x.lineTo(924, 0); x.quadraticCurveTo(918, 22, 899, 30); x.closePath(); x.fill();
    x.fillStyle = 'rgba(70,54,24,0.35)'; x.beginPath(); x.moveTo(899, 30); x.quadraticCurveTo(918, 22, 924, 0); x.lineTo(930, 0); x.quadraticCurveTo(922, 30, 899, 36); x.closePath(); x.fill(); }
  if (clay) clayify(c, { blur: 4, levels: 6, posterize: 0.3, saturation: 1.0 });
  return texOf(k, c, true, false);
}
function floorStainTex(clay) {
  const k = 'fstain' + clay;
  if (TEX.has(k)) return TEX.get(k);
  const c = canvas(512, 256), x = c.getContext('2d');
  for (const [cx, rad, a] of [[128, 110, 0.4], [384, 96, 0.28]]) {
    for (let ring = 0; ring < 5; ring++) {
      x.beginPath();
      for (let t = 0; t <= 6.3; t += 0.08) { const rr = rad * (1 - ring * 0.17) * (0.78 + 0.32 * pnoise(t * 2.4, ring * 2 + cx, 16, 13, 70)); const px = cx + Math.cos(t) * rr, py = 128 + Math.sin(t) * rr; t === 0 ? x.moveTo(px, py) : x.lineTo(px, py); }
      x.closePath(); x.fillStyle = `rgba(52,42,24,${a * 0.7 * (0.18 + ring * 0.08)})`; x.fill();
    }
  }
  if (clay) clayify(c, { blur: 4, levels: 6, posterize: 0.3, saturation: 1.0 });
  return texOf(k, c, true, false);
}

// ---------------------------------------------------------------- the materials
// the flickering tube's light, shared: the vertices keep it apart (aFlk) and the shader adds it × this
const FLICK = { value: 1 };
function baked(m, clayDefs) {
  m.vertexColors = true;
  if (STYLE.plastilina && clayDefs) m.defines = { ...(m.defines || {}), ...clayDefs };
  m.onBeforeCompile = (sh) => {
    sh.uniforms.uBRFlick = FLICK;
    sh.vertexShader = 'attribute vec3 aFlk;\nuniform float uBRFlick;\n' + sh.vertexShader.replace('#include <color_vertex>', '#include <color_vertex>\n\tvColor.rgb += aFlk * uBRFlick;');
  };
  m.customProgramCacheKey = () => 'backrooms1';
  return m;
}
const CLAY_WALL = { CLAY_RELIEF: '1.2', CLAY_TONE: '1.3', CLAY_SET: '0', CLAY_TILE: '2.4', CLAY_AMP: '0.03', CLAY_CAV: '0.1' };
const CLAY_CARPET = { CLAY_RELIEF: '1.5', CLAY_TONE: '1.3', CLAY_SET: '1', CLAY_TILE: '1.6', CLAY_AMP: '0.012', CLAY_CAV: '0.16' };
const CLAY_CEIL = { CLAY_RELIEF: '1.0', CLAY_TONE: '1.1', CLAY_SET: '0', CLAY_TILE: '1.8', CLAY_AMP: '0.02', CLAY_CAV: '0.1' };
let MATS = null;
function materials() {
  if (MATS && MATS.clay === STYLE.plastilina) return MATS;
  const clay = STYLE.plastilina;
  const [wp, wpb] = wallpaperTex(clay), [cp, cpb] = carpetTex(clay), [ce, ceb] = ceilingTex(clay);
  const M = (o, defs) => baked(new THREE.MeshStandardMaterial({ roughness: 0.85, metalness: 0, ...o }), defs);
  MATS = {
    clay,
    wall: M({ map: wp, bumpMap: wpb, bumpScale: clay ? 0.6 : 1.1, roughness: 0.78 }, CLAY_WALL),
    carpet: M({ map: cp, bumpMap: cpb, bumpScale: clay ? 0.5 : 1.6, roughness: 1 }, CLAY_CARPET),
    ceil: M({ map: ce, bumpMap: ceb, bumpScale: clay ? 0.5 : 1.0, roughness: 0.95 }, CLAY_CEIL),
    plenum: M({ color: 0x3a3630, roughness: 1 }),
    frame: M({ color: 0xf0ede4, roughness: 0.45, metalness: clay ? 0 : 0.3 }),
    skirting: M({ color: clay ? 0x86704c : 0x6e5c40, roughness: 0.6 }),
    socket: M({ map: socketTex(), roughness: 0.5 }),
    stairs: M({ map: cp, bumpMap: cpb, bumpScale: 1.2, roughness: 1 }, CLAY_CARPET),
    fabric: M({ color: clay ? 0x4a4e58 : 0x3c3f46, roughness: 0.95 }),
    plastic: M({ color: 0x1c1c1e, roughness: 0.45, metalness: clay ? 0 : 0.1 }),
    stain: M({ map: stainTex(clay), transparent: true, depthWrite: false, roughness: 0.9, polygonOffset: true, polygonOffsetFactor: -2, polygonOffsetUnits: -2 }),
    fstain: M({ map: floorStainTex(clay), transparent: true, depthWrite: false, roughness: 1, polygonOffset: true, polygonOffsetFactor: -2, polygonOffsetUnits: -2 }),
    lens: new THREE.MeshStandardMaterial({ color: 0x000000, emissive: 0xfff6e2, emissiveMap: lensTex(), emissiveIntensity: 2.4, roughness: 0.3 }),
    lensF: new THREE.MeshStandardMaterial({ color: 0x000000, emissive: 0xfff6e2, emissiveMap: lensTex(), emissiveIntensity: 2.4, roughness: 0.3 }),
    lensOff: M({ color: 0xe6e4da, map: lensTex(), roughness: 0.4 }),
  };
  return MATS;
}

// ---------------------------------------------------------------- building geometry, lit as it is built
class Geo {
  constructor() { this.p = []; this.n = []; this.t = []; this.c = []; this.f = []; this.i = []; }
  get count() { return this.p.length / 3; }
  vert(x, y, z, nx, ny, nz, u, v, col) { this.p.push(x, y, z); this.n.push(nx, ny, nz); this.t.push(u, v); this.c.push(col[0], col[1], col[2]); this.f.push(col[3], col[4], col[5]); return this.count - 1; }
  geometry() {
    if (!this.i.length) return null;
    const g = new THREE.BufferGeometry();
    g.setAttribute('position', new THREE.Float32BufferAttribute(this.p, 3));
    g.setAttribute('normal', new THREE.Float32BufferAttribute(this.n, 3));
    g.setAttribute('uv', new THREE.Float32BufferAttribute(this.t, 2));
    g.setAttribute('color', new THREE.Float32BufferAttribute(this.c, 3));
    g.setAttribute('aFlk', new THREE.Float32BufferAttribute(this.f, 3));
    g.setIndex(this.i);
    g.computeBoundingSphere();
    return g;
  }
}
// a flat piece of surface: corner o, edge vectors a and b, cut at the fractions ta (along a) and tb (along b); it faces
// nrm; uvf(x, y, z) its texture coordinates; kind the way its light is worked out ('floor', 'ceil', 'wall'); memo, for
// the floor and the ceiling, the light already worked out at a point (shared by the tiles round it); sp, where to work
// a vertex's light out instead of at the vertex (a point on a grid line is on both sides of the wall standing on it)
function sheet(G, o, a, b, ta, tb, nrm, uvf, kind, memo = null, col = null, sp = null) {
  const base = G.count, nb = tb.length;
  for (const fa of ta) for (const fb of tb) {
    const x = o[0] + a[0] * fa + b[0] * fb, y = o[1] + a[1] * fa + b[1] * fb, z = o[2] + a[2] * fa + b[2] * fb;
    let c = col;
    if (!c) {
      const q = sp ? sp(x, y, z) : null, sx = q ? q[0] : x, sy = q ? q[1] : y, sz = q ? q[2] : z;
      if (memo) { const key = Math.round(x * 50) * 1e7 + Math.round(z * 50) * 10 + (kind === 'floor' ? 1 : 2); c = memo.get(key); if (!c) { c = shade(kind, sx, sy, sz, nrm[0], nrm[1], nrm[2]); memo.set(key, c); } }
      else c = shade(kind, sx, sy, sz, nrm[0], nrm[1], nrm[2]);
    }
    const [u, v] = uvf(x, y, z);
    G.vert(x, y, z, nrm[0], nrm[1], nrm[2], u, v, c);
  }
  // (counter-clockwise seen from the side it faces)
  const cx = a[1] * b[2] - a[2] * b[1], cy = a[2] * b[0] - a[0] * b[2], cz = a[0] * b[1] - a[1] * b[0];
  const flip = cx * nrm[0] + cy * nrm[1] + cz * nrm[2] < 0;
  for (let i = 0; i < ta.length - 1; i++) for (let j = 0; j < nb - 1; j++) {
    const v00 = base + i * nb + j, v10 = v00 + nb, v11 = v10 + 1, v01 = v00 + 1;
    if (flip) G.i.push(v00, v11, v10, v00, v01, v11); else G.i.push(v00, v10, v11, v00, v11, v01);
  }
}
const steps = (n) => Array.from({ length: n + 1 }, (_, i) => i / n);
// the heights a wall's face is cut at: finer at the foot and under the ceiling, where the light changes fastest
const ROWS = [0, 0.1, 0.32, 0.75, 1.3, 1.9, 2.3, 2.55, 2.74];
function rowsBetween(y0, y1) { const r = [y0]; for (const y of ROWS) if (y > y0 + 0.02 && y < y1 - 0.02) r.push(y); r.push(y1); return r.map((y) => (y - y0) / (y1 - y0)); }

// ---------------------------------------------------------------- the pieces
function buildFloorAndCeiling(G) {
  const memoF = new Map(), memoC = new Map(), covered = new Set(), plenums = [];
  for (const l of LAMPS) {
    const i = Math.round(l.u0 / 0.6), j = Math.round(l.v0 / 0.6);
    covered.add(i + ',' + j); covered.add(l.ax === 'x' ? i + 1 + ',' + j : i + ',' + (j + 1));
  }
  for (let z = 0; z < N; z++) for (let x = 0; x < N; x++) {
    const r = ID[z * N + x];
    if (!r) continue;
    const x0 = x * C, z0 = z * C, room = String.fromCharCode(r), cx = x0 + C / 2, cz = z0 + C / 2;
    // (a vertex on the cell's edge takes its light on this cell's side of the wall standing there — but not across an
    // opening: the floor goes on through a doorway, the ceiling through an opening, without a seam in the light)
    const edgeTy = (px, pz) => [Math.abs(px - x0) < 1e-6 ? VE[z * N + x] : Math.abs(px - x0 - C) < 1e-6 ? VE[z * N + mod(x + 1)] : 0, Math.abs(pz - z0) < 1e-6 ? HE[z * N + x] : Math.abs(pz - z0 - C) < 1e-6 ? HE[mod(z + 1) * N + x] : 0];
    const inwardOf = (through) => (px, py, pz) => { const [tx, tz] = edgeTy(px, pz); return [px + (through(tx) ? 0 : Math.sign(cx - px) * 0.05), py, pz + (through(tz) ? 0 : Math.sign(cz - pz) * 0.05)]; };
    const inward = inwardOf((t) => t !== 1 && t !== 5), inwardC = inwardOf((t) => t === 0 || t === 3);
    // the carpet: one sheet a cell, its light every 60 cm (worked out once per point and room)
    const mf = memoF.get(r) || (memoF.set(r, new Map()), memoF.get(r));
    sheet(G.carpet, [x0, 0, z0], [C, 0, 0], [0, 0, C], steps(2), steps(2), [0, 1, 0], (px, py, pz) => [px / 1.2, -pz / 1.2], 'floor', mf, null, inward);
    // the ceiling: tile by tile (each its kind in the picture of four); where a lamp sits, none; now and then one missing
    const mc = memoC.get(r) || (memoC.set(r, new Map()), memoC.get(r));
    for (let a = 0; a < 2; a++) for (let b = 0; b < 2; b++) {
      const i = x * 2 + a, j = z * 2 + b, u0 = i * 0.6, v0 = j * 0.6;
      if (covered.has(i + ',' + j)) continue;
      const hh = hashI(i, j, 91);
      if (hh < 0.011 && room !== 'M' && !CORR[room]) { plenums.push([u0, v0]); continue; }
      const kind = hh < 0.07 ? 2 : hh < 0.13 ? 3 : hashI(i, j, 92) < 0.4 ? 1 : 0, ku = (kind % 2) * 0.5, kv = kind < 2 ? 0.5 : 0;
      const rot = hashI(i, j, 93) < 0.5;
      const y00 = ceilOf(room, v0), y01 = ceilOf(room, v0 + 0.6);
      sheet(G.ceil, [u0, y00, v0], [0.6, 0, 0], [0, y01 - y00, 0.6], [0, 1], [0, 1], [0, -1, 0], (px, py, pz) => {
        let s = (px - u0) / 0.6, t = (pz - v0) / 0.6; if (rot) [s, t] = [1 - s, 1 - t];
        return [ku + s * 0.5, kv + (1 - t) * 0.5];
      }, 'ceil', mc, null, inwardC);
    }
  }
  // a missing tile: the dark plenum above it (its sides catch a little of the room's light)
  for (const [u0, v0] of plenums) {
    const hc = ceilAt(u0 + 0.3, v0 + 0.3), d = 0.5, lo = shade('ceil', u0 + 0.3, hc, v0 + 0.3, 0, -1, 0), dim = (k) => lo.map((v) => v * k);
    const top = dim(0.05), mid = dim(0.35);
    sheet(G.plenum, [u0, hc + d, v0], [0.6, 0, 0], [0, 0, 0.6], [0, 1], [0, 1], [0, -1, 0], () => [0, 0], 'prop', null, top);
    for (const [o, a, n] of [[[u0, hc, v0], [0.6, 0, 0], [0, 0, 1]], [[u0, hc, v0 + 0.6], [0.6, 0, 0], [0, 0, -1]], [[u0, hc, v0], [0, 0, 0.6], [1, 0, 0]], [[u0 + 0.6, hc, v0], [0, 0, 0.6], [-1, 0, 0]]]) {
      const b0 = G.plenum.count;
      sheet(G.plenum, o, a, [0, d, 0], [0, 1], [0, 1], n, () => [0, 0], 'prop', null, mid);
      for (let k = 0; k < 4; k++) if (k % 2 === 1) { const ci = (b0 + k) * 3; G.plenum.c[ci] = top[0]; G.plenum.c[ci + 1] = top[1]; G.plenum.c[ci + 2] = top[2]; } // (darker up inside)
    }
  }
}
// the partitions: every edge with a wall on it, both its faces (where there is a room), the ends you can see (a
// doorway's jambs, a free partition's end) and the undersides of the wall over a doorway; the skirting along their feet
function buildWalls(G, decals) {
  // the edge on line k (x = k·C for 'v', z = k·C for 'h'), i-th along it
  const edge = (o, k, i) => (o === 'v' ? VE[mod(i) * N + mod(k)] : HE[mod(k) * N + mod(i)]);
  const near = (a, b) => Math.abs(a - b) < 1e-4;
  for (const o of ['v', 'h']) for (let k = 0; k < N; k++) for (let i = 0; i < N; i++) {
    const ty = edge(o, k, i);
    if (!ty || ty === 3) continue;
    // the cells either side: 'v' — west and east of the line; 'h' — north and south
    const sideA = o === 'v' ? cellId(k - 1, i) : cellId(i, k - 1), sideB = o === 'v' ? cellId(k, i) : cellId(i, k);
    const line = k * C, along0 = i * C;
    // a point on the wall: s along it (m), w across (m, + towards side B), y up
    const at = (s, w, y) => (o === 'v' ? [line + w, y, along0 + s] : [along0 + s, y, line + w]);
    const vec = (ds, dw, dy) => (o === 'v' ? [dw, dy, ds] : [ds, dy, dw]);
    const nrm = (w) => (o === 'v' ? [w, 0, 0] : [0, 0, w]);
    const spans = SPANS[ty];
    for (const span of spans) {
      const [s0, s1, y0, y1] = span;
      // at each end, what carries on: along the line (cl) and across it at a corner (cp), as height ranges. Where a wall
      // across covers it all, the faces run on to its far side (or an outside corner would be left open); where nothing
      // covers, the end shows (a doorway's jamb, a free partition's end)
      const ends = [s0, s1].map((s, e) => {
        const cl = [], cp = [];
        for (const sp of spans) if (sp !== span && (e === 0 ? near(sp[1], s) : near(sp[0], s))) cl.push([sp[2], sp[3]]);
        const atV = near(s, 0) || near(s, C);
        if (atV) {
          const j = i + (e === 0 ? -1 : 1), v = i + (e === 0 ? 0 : 1), po = o === 'v' ? 'h' : 'v';
          for (const sp of SPANS[edge(o, k, j)]) if (e === 0 ? near(sp[1], C) : near(sp[0], 0)) cl.push([sp[2], sp[3]]);
          for (const sp of SPANS[edge(po, v, k - 1)]) if (near(sp[1], C)) cp.push([sp[2], sp[3]]);
          for (const sp of SPANS[edge(po, v, k)]) if (near(sp[0], 0)) cp.push([sp[2], sp[3]]);
        }
        const full = (cov) => cov.length > 0 && subtract([y0, y1], cov).length === 0;
        return { ext: atV && full(cp) && !full(cl) ? HALF : 0, cap: full(cl) ? [] : subtract([y0, y1], cl.concat(cp)) };
      });
      const fa = s0 - ends[0].ext, fb = s1 + ends[1].ext;
      // (a vertex's light: at its own place along the wall, never past the span's ends)
      const own = (x, y, z) => { const s = clamp((o === 'v' ? z : x) - along0, s0 + 0.02, s1 - 0.02); return o === 'v' ? [x, y, along0 + s] : [along0 + s, y, z]; };
      // the faces
      for (const sd of [-1, 1]) {
        const room = sd < 0 ? sideA : sideB;
        if (!room) continue;
        const rot = String.fromCharCode(room) === 'Q';
        const uvf = (px, py, pz) => { const al = o === 'v' ? pz : px; return rot ? [py / WP, al / WP] : [al / WP, py / WP]; };
        sheet(G.wall, at(fa, sd * HALF, y0), vec(fb - fa, 0, 0), vec(0, 0, y1 - y0), steps(Math.max(1, Math.round((fb - fa) / 0.6))), rowsBetween(y0, y1), nrm(sd), uvf, 'wall', null, null, own);
        if (y0 === 0) skirting(G, at, vec, nrm, fa - (ends[0].ext ? 0.012 : 0), fb + (ends[1].ext ? 0.012 : 0), sd, own);
        if (y0 === 0 && s1 - s0 > 1.1) dress(G, decals, o, k, i, at, vec, nrm, sd, room);
      }
      // the underside of the wall over a doorway
      if (y0 > 0) sheet(G.wall, at(s0, -HALF, y0), vec(s1 - s0, 0, 0), vec(0, T, 0), steps(2), [0, 1], [0, -1, 0], (px, py, pz) => [(o === 'v' ? pz : px) / WP, (o === 'v' ? px : pz) / WP], 'wall', null, null, own);
      // the ends that show
      for (const [e, s, dir] of [[0, s0, -1], [1, s1, 1]]) for (const [a, b] of ends[e].cap) {
        sheet(G.wall, at(s, -HALF, a), vec(0, T, 0), vec(0, 0, b - a), [0, 1], rowsBetween(a, b), vec(dir, 0, 0), (px, py, pz) => [(o === 'v' ? px : pz) / WP, py / WP], 'wall');
      }
    }
  }
}
function subtract([a, b], cover) {
  let out = [[a, b]];
  for (const [c, d] of cover) out = out.flatMap(([p, q]) => (d <= p || c >= q ? [[p, q]] : [[p, Math.max(p, c)], [Math.min(q, d), q]].filter(([u, v]) => v - u > 0.01)));
  return out;
}
// the skirting: a 9 cm vinyl strip at the foot of a face, standing 1.2 cm proud of it
function skirting(G, at, vec, nrm, s0, s1, sd, own) {
  const w = sd * (HALF + 0.012), n = nrm(sd);
  sheet(G.skirting, at(s0, w, 0), vec(s1 - s0, 0, 0), vec(0, 0, 0.09), steps(Math.max(1, Math.round((s1 - s0) / 0.6))), [0, 1], n, () => [0, 0], 'wall', null, null, own);
  sheet(G.skirting, at(s0, sd * HALF, 0.09), vec(s1 - s0, 0, 0), vec(0, sd * 0.012, 0), [0, 1], [0, 1], [0, 1, 0], () => [0, 0], 'wall', null, null, own);
}
// what a stretch of wall gets beside its paper: a socket now and then (and a whole row of them along the corridor of
// sockets), a stain. (k, i: its line and place along it)
function dress(G, decals, o, k, i, at, vec, nrm, sd, room) {
  const r = String.fromCharCode(room), h = hashI(k * 3 + (o === 'v' ? 1 : 2), i * 5 + sd, 101);
  const row = r === 'N' && o === 'h' && k === 27 && sd < 0;
  const plates = row ? [0.3, 0.9] : h < 0.13 ? [0.6] : [];
  for (const s of plates) socket(G, at(s, sd * (HALF + 0.004), 0.32), nrm(sd), o);
  const hs = hashI(k * 7 + (o === 'v' ? 3 : 4), i * 11 + sd, 102);
  if (hs < 0.09) decals.push({ o, k, i, at, vec, nrm: nrm(sd), sd, kind: Math.floor(hashI(k, i, 103 + sd) * 4) });
}
function socket(G, p, n, o) {
  const c = shadePoint(p[0] + n[0] * 0.2, 0.35, p[2] + n[2] * 0.2), W = 0.07, Hh = 0.115;
  // (its face, a hair proud of the wall; along the wall: x for a wall running east–west)
  const ax = o === 'v' ? [0, 0, -n[0]] : [n[2], 0, 0];
  sheet(G.socket, [p[0] - ax[0] * W / 2, p[1] - Hh / 2, p[2] - ax[2] * W / 2], [ax[0] * W, 0, ax[2] * W], [0, Hh, 0], [0, 1], [0, 1], n, (px, py, pz) => [((px - p[0]) * ax[0] + (pz - p[2]) * ax[2]) / W + 0.5, (py - p[1]) / Hh + 0.5], 'prop', null, c);
}
function buildDecals(G, decals) {
  for (const d of decals) {
    const { at, vec, nrm, sd, kind } = d;
    const s0 = 0.1 + hashI(d.k, d.i * 2 + d.sd, 110) * 0.3, len = kind === 2 ? 0.9 : 0.7;
    const y0 = kind === 0 ? 1.2 : kind === 1 ? 1.25 : kind === 2 ? 0.02 : 0.9, y1 = kind === 0 ? H - 0.01 : kind === 1 ? 2.35 : kind === 2 ? 0.55 : 2.45;
    const ku = kind * 0.25;
    const o0 = at(s0, sd * (HALF + 0.002), y0);
    sheet(G.stain, o0, vec(len, 0, 0), vec(0, 0, y1 - y0), steps(2), rowsBetween(y0, y1), nrm, (px, py, pz) => {
      const s = ((px - o0[0]) * (d.o === 'v' ? 0 : 1) + (pz - o0[2]) * (d.o === 'v' ? 1 : 0)) / len, t = (py - y0) / (y1 - y0);
      return [ku + s * 0.25, t];
    }, 'wall');
  }
  // the wet patches on the carpet
  for (let z = 0; z < N; z++) for (let x = 0; x < N; x++) {
    if (!ID[z * N + x] || hashI(x, z, 120) > 0.035) continue;
    const k = hashI(x, z, 121) < 0.6 ? 0 : 1, s = 0.9 + hashI(x, z, 122) * 0.8, u0 = x * C + 0.6 - s / 2, v0 = z * C + 0.6 - s / 2;
    sheet(G.fstain, [u0, 0.004, v0], [s, 0, 0], [0, 0, s], steps(2), steps(2), [0, 1, 0], (px, py, pz) => [k * 0.5 + ((px - u0) / s) * 0.5, 1 - (pz - v0) / s], 'floor');
  }
}
// the troffers: the lens (lit, dead or flickering) a little above the ceiling's plane, the enamelled frame round it
function buildLamps(G) {
  const F = 0.025, R = 0.014; // (the frame's width; how far up the lens sits in its housing)
  for (const l of LAMPS) {
    const w = l.ax === 'x' ? 1.2 : 0.6, d = l.ax === 'x' ? 0.6 : 1.2, u0 = l.u0, v0 = l.v0, room = roomAt(l.x, l.z);
    const y = (v) => ceilOf(room, v) - 0.002; // (the ceiling's plane there: sloping in room H)
    const lens = l.st === 0 ? G.lens : l.st === 2 ? G.lensF : G.lensOff;
    const ya = y(v0 + F), yb = y(v0 + d - F);
    sheet(lens, [u0 + F, ya + R, v0 + F], [w - 2 * F, 0, 0], [0, yb - ya, d - 2 * F], [0, 1], [0, 1], [0, -1, 0], (px, py, pz) => {
      const s = (px - u0 - F) / (w - 2 * F), t = (pz - v0 - F) / (d - 2 * F);
      return l.ax === 'x' ? [t, s] : [s, 1 - t];
    }, 'prop', null, l.st === 1 ? shade('ceil', l.x, y(l.z), l.z, 0, -1, 0) : NOBASE);
    const c = shade('ceil', l.x, y(l.z), l.z, 0, -1, 0).map((v) => v * 1.25);
    // the enamelled frame round the lens, at the ceiling's plane
    for (const [o, a, b] of [[[u0, y(v0), v0], [w, 0, 0], [0, y(v0 + F) - y(v0), F]], [[u0, y(v0 + d - F), v0 + d - F], [w, 0, 0], [0, y(v0 + d) - y(v0 + d - F), F]], [[u0, y(v0), v0], [F, 0, 0], [0, y(v0 + d) - y(v0), d]], [[u0 + w - F, y(v0), v0], [F, 0, 0], [0, y(v0 + d) - y(v0), d]]]) {
      sheet(G.frame, o, a, b, [0, 1], [0, 1], [0, -1, 0], () => [0, 0], 'prop', null, c);
    }
    // and the housing's four sides, from the frame up to the lens (no gap to see through)
    for (const [o, a, n] of [[[u0 + F, ya, v0 + F], [0, yb - ya, d - 2 * F], [1, 0, 0]], [[u0 + w - F, ya, v0 + F], [0, yb - ya, d - 2 * F], [-1, 0, 0]], [[u0 + F, ya, v0 + F], [w - 2 * F, 0, 0], [0, 0, 1]], [[u0 + F, yb, v0 + d - F], [w - 2 * F, 0, 0], [0, 0, -1]]]) {
      sheet(G.frame, o, a, [0, R + 0.001, 0], [0, 1], [0, 1], n, () => [0, 0], 'prop', null, c);
    }
  }
}
// pillars (one floating), the narrowing walls, the stairs into the ceiling
function buildOdd(G) {
  for (const [cx, cz, fl] of PILLARS) {
    const x = cx * C, z = cz * C, y0 = fl ? 0.3 : 0;
    for (const [o, a, n] of [[[x - PIL, y0, z + PIL], [2 * PIL, 0, 0], [0, 0, 1]], [[x + PIL, y0, z - PIL], [-2 * PIL, 0, 0], [0, 0, -1]], [[x + PIL, y0, z + PIL], [0, 0, -2 * PIL], [1, 0, 0]], [[x - PIL, y0, z - PIL], [0, 0, 2 * PIL], [-1, 0, 0]]]) {
      sheet(G.wall, o, a, [0, H - y0, 0], steps(1), rowsBetween(y0, H), n, (px, py, pz) => [(px + pz) / WP, py / WP], 'wall');
      if (!fl) sheet(G.skirting, [o[0] + n[0] * 0.012, 0, o[2] + n[2] * 0.012], a, [0, 0.09, 0], [0, 1], [0, 1], n, () => [0, 0], 'wall');
    }
    if (fl) sheet(G.wall, [x - PIL, y0, z - PIL], [2 * PIL, 0, 0], [0, 0, 2 * PIL], [0, 1], [0, 1], [0, -1, 0], (px, py, pz) => [px / WP, pz / WP], 'wall');
  }
  for (const [x0, z0, x1, z1] of SLANTS) {
    const L = Math.hypot(x1 - x0, z1 - z0), nx = (z1 - z0) / L, nz = -(x1 - x0) / L, s = x0 < 26.4 ? 1 : -1; // (facing into the corridor)
    const n = [nx * s, 0, nz * s];
    sheet(G.wall, [x0 + n[0] * 0.02, 0, z0 + n[2] * 0.02], [x1 - x0, 0, z1 - z0], [0, H, 0], steps(Math.round(L / 0.6)), rowsBetween(0, H), n, (px, py, pz) => [Math.hypot(px - x0, pz - z0) / WP, py / WP], 'wall');
    sheet(G.skirting, [x0 + n[0] * 0.032, 0, z0 + n[2] * 0.032], [x1 - x0, 0, z1 - z0], [0, 0.09, 0], steps(Math.round(L / 0.6)), [0, 1], n, () => [0, 0], 'wall');
  }
  const S = STAIRS, tread = (S.x1 - S.x0) / S.n, rise = H / S.n;
  for (let i = 0; i < S.n; i++) {
    const xa = S.x0 + i * tread, top = rise * (i + 1);
    sheet(G.stairs, [xa, top, S.z0], [tread, 0, 0], [0, 0, S.z1 - S.z0], [0, 1], [0, 1], [0, 1, 0], (px, py, pz) => [px / 1.2, pz / 1.2], 'floor');
    sheet(G.stairs, [xa, top - rise, S.z0], [0, rise, 0], [0, 0, S.z1 - S.z0], [0, 1], [0, 1], [-1, 0, 0], (px, py, pz) => [pz / 1.2, py / 1.2], 'wall');
  }
  for (const [z, n] of [[S.z0, -1], [S.z1, 1]]) {
    // the sides of the flight: a wall in the shape of the stairs
    const b0 = G.wall.count;
    for (let i = 0; i <= S.n; i++) {
      const xa = S.x0 + i * tread, y = Math.min(H, rise * i);
      for (const yy of [0, y]) G.wall.vert(xa, yy, z, 0, 0, n, xa / WP, yy / WP, shade('wall', xa, Math.max(0.05, yy * 0.5), z, 0, 0, n));
    }
    for (let i = 0; i < S.n; i++) { const a = b0 + i * 2; if (n > 0) G.wall.i.push(a, a + 2, a + 3, a, a + 3, a + 1); else G.wall.i.push(a, a + 3, a + 2, a, a + 1, a + 3); }
  }
}
// the office chair, the same everywhere: a padded seat and back on a gas lift, five legs on castors
let CHAIR = null;
function chairGeo() {
  if (CHAIR) return CHAIR;
  const fab = [], pla = [];
  const B = (w, h, d, x, y, z, rx = 0) => { const g = new THREE.BoxGeometry(w, h, d, 2, 1, 2); if (rx) g.rotateX(rx); g.translate(x, y, z); return g; };
  // a cushion: a box with its top swelling and its edges rounded off (seat and back)
  const cushion = (w, h, d, x, y, z, rx = 0) => {
    const g = new THREE.BoxGeometry(w, h, d, 6, 2, 6), p = g.attributes.position;
    for (let i = 0; i < p.count; i++) {
      const u = p.getX(i) / (w / 2), v = p.getZ(i) / (d / 2), top = p.getY(i) > 0;
      const r = Math.max(Math.abs(u), Math.abs(v)), sw = (1 - Math.min(1, u * u)) * (1 - Math.min(1, v * v));
      if (top) p.setY(i, p.getY(i) + 0.022 * sw);
      if (r > 0.99) { p.setX(i, p.getX(i) * 0.97); p.setZ(i, p.getZ(i) * 0.97); p.setY(i, p.getY(i) * (top ? 0.75 : 0.9)); }
    }
    g.computeVertexNormals(); if (rx) g.rotateX(rx); g.translate(x, y, z); return g;
  };
  fab.push(cushion(0.48, 0.08, 0.46, 0, 0.47, 0.02), cushion(0.44, 0.06, 0.5, 0, 0.84, -0.22, Math.PI / 2 - 0.12));
  pla.push(B(0.06, 0.34, 0.035, 0, 0.62, -0.26, -0.08), new THREE.CylinderGeometry(0.025, 0.03, 0.3, 10).translate(0, 0.28, 0), new THREE.CylinderGeometry(0.06, 0.07, 0.05, 12).translate(0, 0.42, 0));
  for (const sx of [-1, 1]) pla.push(B(0.03, 0.2, 0.03, sx * 0.22, 0.6, 0.04), B(0.05, 0.025, 0.26, sx * 0.22, 0.71, 0.02)); // (the arms)
  for (let i = 0; i < 5; i++) {
    const a = (i / 5) * Math.PI * 2, leg = B(0.04, 0.03, 0.3, 0, 0.1, 0.15);
    leg.rotateY(a); pla.push(leg);
    const w = new THREE.CylinderGeometry(0.03, 0.03, 0.03, 10); w.rotateZ(Math.PI / 2); w.translate(Math.sin(a) * 0.29, 0.03, Math.cos(a) * 0.29); pla.push(w);
  }
  const clean = (gs) => mergeGeometries(gs.map((g) => { const q = g.index ? g.toNonIndexed() : g; for (const k of Object.keys(q.attributes)) if (!['position', 'normal', 'uv'].includes(k)) q.deleteAttribute(k); return q; }));
  CHAIR = { fab: clean(fab), pla: clean(pla) };
  return CHAIR;
}
function buildChairs(G) {
  const ch = chairGeo();
  for (const [x, z, a] of CHAIRS) {
    const c = shadePoint(x, 0.6, z);
    for (const [key, src] of [['fabric', ch.fab], ['plastic', ch.pla]]) {
      const g = src.clone(); g.rotateY(a); g.translate(x, 0, z);
      const p = g.attributes.position, n = g.attributes.normal, t = g.attributes.uv, D = G[key], b = D.count;
      for (let i = 0; i < p.count; i++) D.vert(p.getX(i), p.getY(i), p.getZ(i), n.getX(i), n.getY(i), n.getZ(i), t.getX(i), t.getY(i), c.map((v, k) => (k < 3 ? v * (0.75 + 0.25 * n.getY(i)) : 0)));
      for (let i = 0; i < p.count; i++) D.i.push(b + i);
    }
  }
}
// a door: its frame, its leaf with two raised panels, its knob. Built for the Backrooms (shut, its colour times the
// light where it stands). Faces +z, sill at y 0
export function doorMesh(o = {}) {
  const w = o.w || 0.9, h = o.h || 2.04, g = new THREE.Group();
  const paint = o.paint || new THREE.MeshStandardMaterial({ color: o.color || 0xd4a72c, roughness: 0.55 });
  const frame = o.frameMat || new THREE.MeshStandardMaterial({ color: o.frame || 0x3a2a1a, roughness: 0.6 });
  const knob = o.knobMat || new THREE.MeshStandardMaterial({ color: 0xc8a050, roughness: 0.3, metalness: STYLE.plastilina ? 0 : 0.8 });
  const B = (m, bw, bh, bd, x, y, z) => { const mm = new THREE.Mesh(new THREE.BoxGeometry(bw, bh, bd), m); mm.position.set(x, y, z); g.add(mm); return mm; };
  B(paint, w, h, 0.04, 0, h / 2, 0);
  for (const [py, ph] of [[0.55, 0.7], [1.45, 0.75]]) for (const sz of [-1, 1]) B(paint, w * 0.66, ph * (h / 2.04), 0.012, 0, py * (h / 2.04), sz * 0.026);
  B(frame, 0.07, h + 0.07, 0.1, -w / 2 - 0.035, (h + 0.07) / 2, 0); B(frame, 0.07, h + 0.07, 0.1, w / 2 + 0.035, (h + 0.07) / 2, 0); B(frame, w + 0.14, 0.07, 0.1, 0, h + 0.035, 0);
  for (const sz of [-1, 1]) { const k = new THREE.Mesh(new THREE.SphereGeometry(0.03, 12, 9), knob); k.position.set(w / 2 - 0.09, 1.0 * (h / 2.04), sz * 0.05); g.add(k); }
  g.traverse((m) => { if (m.isMesh) { m.castShadow = true; m.receiveShadow = true; } });
  return g;
}

// a group's meshes merged into one per material (a door: three draws instead of ten — it is drawn nine times)
function mergeByMaterial(group) {
  group.updateMatrixWorld(true);
  const by = new Map();
  group.traverse((m) => {
    if (!m.isMesh) return;
    const g = (m.geometry.index ? m.geometry.toNonIndexed() : m.geometry.clone()).applyMatrix4(m.matrixWorld);
    for (const k of Object.keys(g.attributes)) if (!['position', 'normal', 'uv'].includes(k)) g.deleteAttribute(k);
    if (!by.has(m.material)) by.set(m.material, []);
    by.get(m.material).push(g);
  });
  const out = new THREE.Group();
  for (const [mat, gs] of by) out.add(new THREE.Mesh(mergeGeometries(gs), mat));
  return out;
}

// ---------------------------------------------------------------- the environment (reflections): a yellow room
let ENV = null;
function envMap(pmrem) {
  if (ENV || !pmrem) return ENV;
  const sc = new THREE.Scene(), M = (c, e = 0) => new THREE.MeshBasicMaterial({ color: new THREE.Color(c).multiplyScalar(1 + e), side: THREE.BackSide });
  const room = new THREE.Mesh(new THREE.BoxGeometry(10, 2.8, 10), [M(0x8a7a44), M(0x8a7a44), M(0xb8b4a0), M(0x6a5a3a), M(0x8a7a44), M(0x8a7a44)]);
  sc.add(room);
  for (let i = -1; i <= 1; i++) for (let j = -1; j <= 1; j++) { const l = new THREE.Mesh(new THREE.PlaneGeometry(0.6, 1.2), new THREE.MeshBasicMaterial({ color: new THREE.Color(0xfff6e2).multiplyScalar(4) })); l.rotation.x = Math.PI / 2; l.position.set(i * 3, 1.38, j * 3); sc.add(l); }
  ENV = pmrem.fromScene(sc, 0, 0.1, 50).texture;
  return ENV;
}

// ---------------------------------------------------------------- the level
// what the Interiors expect of a building (housekit.js HouseBuilder.finish), and its own hooks: tick (the endless
// plan, the flickering tube, the hum), look (the light inside), unlook
export function buildBackrooms(origin = INTERIOR_ORIGIN) {
  const t0 = performance.now();
  const ox = origin.x, oz = origin.z, mats = materials();
  const keys = ['wall', 'carpet', 'ceil', 'plenum', 'frame', 'skirting', 'socket', 'stairs', 'fabric', 'plastic', 'stain', 'fstain', 'lens', 'lensF', 'lensOff'];
  const G = Object.fromEntries(keys.map((k) => [k, new Geo()]));
  const decals = [];
  buildFloorAndCeiling(G);
  buildWalls(G, decals);
  buildDecals(G, decals);
  buildLamps(G);
  buildOdd(G);
  buildChairs(G);
  const group = new THREE.Group();
  const geos = [];
  for (const k of keys) {
    const geo = G[k].geometry();
    if (!geo) continue;
    geos.push(geo);
    // the plan and its eight neighbours: it repeats round you
    for (let i = -1; i <= 1; i++) for (let j = -1; j <= 1; j++) {
      const m = new THREE.Mesh(geo, mats[k]);
      m.position.set(ox + i * P, 0, oz + j * P);
      m.receiveShadow = false; m.castShadow = false;
      if (k === 'stain' || k === 'fstain') m.renderOrder = 1;
      group.add(m);
    }
  }
  // the doors (the sacristy's, dark wood, back to the church; a small one up a wall; two that do not open), the colour of each
  // times the light where it stands
  const inter = [];
  for (const [x, z, a, kind, sill, hh, w] of DOORS) {
    // (its light as the wall's there, facing the way it faces; the hemisphere light gives its share back itself)
    const lit = shade('wall', x + Math.sin(a) * 0.1, sill + hh * 0.5, z + Math.cos(a) * 0.1, Math.sin(a), 0, Math.cos(a)), k = ((lit[0] + lit[1] + lit[2]) / 3) * hemiK(0);
    const tint = (c) => new THREE.Color(c).multiplyScalar(k);
    const d = mergeByMaterial(doorMesh({ w, h: hh, paint: new THREE.MeshStandardMaterial({ color: tint(kind === 'exit' ? 0x5a3c24 : 0xc9b98a), roughness: 0.55 }), frameMat: new THREE.MeshStandardMaterial({ color: tint(kind === 'exit' ? 0x2e2016 : 0xb8a678), roughness: 0.6 }), knobMat: new THREE.MeshStandardMaterial({ color: tint(0xc8a050), roughness: 0.3, metalness: STYLE.plastilina ? 0 : 0.7 }) }));
    for (let i = -1; i <= 1; i++) for (let j = -1; j <= 1; j++) {
      const c = i === 0 && j === 0 ? d : d.clone();
      c.position.set(ox + x + i * P + Math.sin(a) * (HALF + 0.02), sill, oz + z + j * P + Math.cos(a) * (HALF + 0.02)); c.rotation.y = a;
      group.add(c);
    }
    const ix = ox + x + Math.sin(a) * 0.7, iz = oz + z + Math.cos(a) * 0.7;
    if (kind === 'exit') inter.push({ type: 'backrooms_out', x: ix, z: iz, r: 1.2, label: 'Volver por la puerta de madera <small>(a la sacristía de Santa María)</small>' });
    else if (kind === 'shut') inter.push({ type: 'info', x: ix, z: iz, r: 1.1, label: 'Abrir la puerta', text: 'No se abre. Ni siquiera gira el pomo. Al otro lado se oye el mismo zumbido.' });
  }
  inter.push({ type: 'info', x: ox + 16.5 * C + 0.4, z: oz + 15.5 * C, r: 1.0, label: 'Mirar por la rendija', text: 'Por la rendija se ve otra sala igual, con la misma luz. No cabes.' });
  // the walls to walk into: every partition that reaches the floor (a doorway's sides, a slit's), the pillars, the
  // narrowing walls, the stairs, the chairs — in the plan and round it
  const segs = [];
  const seg = (ax, az, bx, bz) => segs.push([ax, az, bx, bz]);
  for (const o of ['v', 'h']) for (let z = 0; z < N; z++) for (let x = 0; x < N; x++) {
    const ty = (o === 'v' ? VE : HE)[z * N + x];
    for (const [s0, s1, y0] of SPANS[ty] || []) {
      if (y0 > 0.5) continue;
      if (o === 'v') seg(x * C, z * C + s0, x * C, z * C + s1); else seg(x * C + s0, z * C, x * C + s1, z * C);
    }
  }
  for (const [cx, cz] of PILLARS) { const x = cx * C, z = cz * C; seg(x - PIL, z - PIL, x + PIL, z - PIL); seg(x + PIL, z - PIL, x + PIL, z + PIL); seg(x + PIL, z + PIL, x - PIL, z + PIL); seg(x - PIL, z + PIL, x - PIL, z - PIL); }
  for (const s of SLANTS) seg(...s);
  { const S = STAIRS; seg(S.x0, S.z0, S.x1, S.z0); seg(S.x1, S.z0, S.x1, S.z1); seg(S.x1, S.z1, S.x0, S.z1); seg(S.x0, S.z1, S.x0, S.z0); }
  for (const [x, z] of CHAIRS) { const r = 0.28; seg(x - r, z - r, x + r, z - r); seg(x + r, z - r, x + r, z + r); seg(x + r, z + r, x - r, z + r); seg(x - r, z + r, x - r, z - r); }
  const collider = new StaticCollider(ox - P - 4, oz - P - 4, ox + 2 * P + 4, oz + 2 * P + 4, 2);
  for (let i = -1; i <= 1; i++) for (let j = -1; j <= 1; j++) for (const [ax, az, bx, bz] of segs) collider.addSegment(ox + ax + i * P, oz + az + j * P, ox + bx + i * P, oz + bz + j * P, H);
  collider.build();

  // ---- the house
  const exit = DOORS[0];
  const h = {
    group, collider, lights: [], inter, doors: [], views: [], spots: {}, backrooms: true, thirdPerson: false, origin: { x: ox, z: oz },
    spots0: null, ceilY: (x, z) => ceilAt(x - ox, z - oz), daylight: { sun: 0, hemi: 1 }, bakeMs: 0,
    step: 'footstep_carpet',
    bloom: STYLE.plastilina ? { strength: 0.32, threshold: 0.92, radius: 0.55 } : { strength: 0.42, threshold: 0.9, radius: 0.5 },
    flick: { t: 0, burst: 0, next: 4, on: 1 }, humT: 0,
  };
  h.spots.entrada = { x: ox + exit[0] + 1.15, z: oz + exit[1], h: Math.PI / 2 };
  h.bounds = { x0: ox - P, x1: ox + 2 * P, z0: oz - P, z1: oz + 2 * P };
  h.look = (g) => look(g, h);
  h.unlook = (g) => unlook(g, h);
  h.tick = (dt, g) => tick(dt, g, h);
  h.dispose = () => { for (const geo of geos) geo.dispose(); };
  h.bakeMs = Math.round(performance.now() - t0);
  return h;
}

// the light inside: no sun nor sky, the hemisphere light as the baked colours expect it (white from above, a darker
// version from below), the yellow room in the reflections, a little haze of damp air far off (and over the plan's edge)
const SKY_THINGS = ['dome', 'phys', 'cotton', 'stars', 'moon'];
function look(g, h) {
  const s = g.sky, clay = STYLE.plastilina;
  s.sun.intensity = 0;
  if (s.bounce) s.bounce.intensity = 0;
  s.hemi.color.setRGB(1, 1, 1); s.hemi.groundColor.setRGB(LIT.hg, LIT.hg, LIT.hg);
  s.hemi.intensity = Math.PI; // (it gives L × the albedo back)
  const env = envMap(s.pmrem);
  if (env) { g.scene.environment = env; g.scene.environmentIntensity = clay ? 0.1 : 0.14; }
  const f = s.fog; f.near = 10; f.far = 50; f.color.setRGB(0.66, 0.6, 0.4);
  // (past the last copy of the plan there is nothing: the same haze, not the black of an empty frame)
  if (h.bg === undefined) h.bg = g.scene.background;
  g.scene.background = f.color;
  g.renderer.toneMappingExposure = 1.0;
  // the sky and what is in it are not down here
  if (!h.skyVis) h.skyVis = SKY_THINGS.map((k) => [k, !!(s[k] && s[k].visible)]);
  for (const k of SKY_THINGS) if (s[k]) s[k].visible = false;
  // (claymation: the film's warm grade would turn the yellow to mustard)
  if (g.grade) { const U = g.grade.uniforms; U.uSat.value = 1.0; U.uWarm.value = 0.012; }
}
function unlook(g, h) {
  const s = g.sky;
  if (s.envRT) g.scene.environment = s.envRT.texture;
  if (h.skyVis) for (const [k, v] of h.skyVis) if (s[k]) s[k].visible = v;
  h.skyVis = null;
  if (h.bg !== undefined) { g.scene.background = h.bg; h.bg = undefined; }
  if (g.grade) g.grade.uniforms.uWarm.value = PLASTILINA.grade.warm;
  FLICK.value = 1;
  if (g.audio.backrooms) g.audio.backrooms(0);
}

// per frame: the endless plan (out at one side, in at the other: the player, and whatever the camera keeps of where
// they were, moved back by the plan's size — the same rooms are there), the tube that flickers, the hum
function tick(dt, g, h) {
  const p = g.player, o = h.origin;
  let sx = 0, sz = 0;
  if (p.pos.x - o.x < 0) sx = P; else if (p.pos.x - o.x >= P) sx = -P;
  if (p.pos.z - o.z < 0) sz = P; else if (p.pos.z - o.z >= P) sz = -P;
  if (sx || sz) {
    p.pos.x += sx; p.pos.z += sz;
    const ch = p.char;
    if (ch) {
      ch.object.position.x += sx; ch.object.position.z += sz;
      if (ch.locks) for (const k of ['L', 'R']) if (ch.locks[k] && ch.locks[k].pos) { ch.locks[k].pos.x += sx; ch.locks[k].pos.z += sz; }
    }
    const cam = g.cam;
    if (cam.tgtS) { cam.tgtS.x.x += sx; cam.tgtS.z.x += sz; }
    if (cam.pos) { cam.pos.x += sx; cam.pos.z += sz; }
    if (cam.target) { cam.target.x += sx; cam.target.z += sz; }
    g.camera.position.x += sx; g.camera.position.z += sz;
  }
  // the tube that is going: on, then now and then a fit of blinks
  const F = h.flick;
  F.t += dt;
  if (F.burst > 0) {
    F.burst -= dt; F.sw = (F.sw || 0) - dt;
    if (F.sw <= 0) { F.on = F.on > 0.5 ? 0.04 + Math.random() * 0.1 : 1; F.sw = 0.03 + Math.random() * (F.on > 0.5 ? 0.12 : 0.07); if (F.on > 0.5 && g.audio.backroomsTick) g.audio.backroomsTick(); }
    if (F.burst <= 0) F.on = Math.random() < 0.18 ? 0.06 : 1; // (sometimes it stays out a while)
  } else if (F.t > F.next) { F.t = 0; F.next = 3 + Math.random() * 7; F.burst = 0.25 + Math.random() * 1.1; }
  FLICK.value = F.on;
  const M = MATS;
  if (M) M.lensF.emissiveIntensity = 2.4 * F.on;
  // the hum: the whole ceiling's, louder under a tube
  h.humT -= dt;
  if (h.humT <= 0 && g.audio.backrooms) {
    h.humT = 0.15;
    const x = p.pos.x - o.x, z = p.pos.z - o.z;
    let near = 9;
    for (const l of LAMPS) {
      if (l.st === 1) continue;
      const dx = Math.abs(l.x - x) % P, dz = Math.abs(l.z - z) % P, d = Math.hypot(Math.min(dx, P - dx), Math.min(dz, P - dz));
      if (d < near) near = d;
    }
    g.audio.backrooms(0.55 + 0.45 * Math.exp(-(near * near) / 5), F.on);
  }
}

// for the tools: the plan as it was worked out
export const BACKROOMS_PLAN = { ID, VE, HE, LAMPS, ROOMS, PILLARS, SLANTS, STAIRS, DOORS, CHAIRS, P, C, N };
