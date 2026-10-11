// Dev-only: the Backrooms (src/backrooms.js) from outside. The page's look is the page's (?estilo=real / plastilina).
//   const B = await import('/tools/backroomslab.js?' + Date.now());
//   await B.plan()              → .snaps/br_plan.jpg (the plan from above: rooms, walls by kind, lamps, pillars, doors)
//   await B.enter()             → straight into the level (as through the theatre's yellow door); its build time
//   await B.shoot('a', B.VIEWS) → .snaps/br_<view>_<tag>.jpg (views in the plan's metres: eye, target, fov)
import * as THREE from 'three';
import { BACKROOMS_PLAN as BP } from '/src/backrooms.js';
const G = () => window.game;
async function post(name, c) { await fetch('/__snap?name=' + name, { method: 'POST', body: c.toDataURL('image/jpeg', 0.88) }); }

export const VIEWS = [
  ['llegada', [4.75, 1.6, 6.6], [14, 1.45, 6.4], 72],
  ['gemelas', [4.0, 1.6, 13.8], [30, 1.45, 13.8], 72],
  ['pilares', [21.5, 1.7, 3.6], [42, 1.2, 13], 74],
  ['infinito', [5, 1.6, 1.2], [40, 1.5, 1.2], 70],
  ['estrecho', [26.4, 1.6, 17.6], [26.4, 1.35, 32], 72],
  ['techobajo', [30.5, 1.6, 17.4], [25, 1.2, 24.6], 74],
  ['escalera', [6.6, 1.6, 20.4], [14.2, 2.1, 27.2], 72],
  ['oscura', [16.6, 1.6, 20.2], [22.6, 1.2, 26.6], 74],
  ['enchufes', [22.6, 1.6, 30.6], [3.6, 0.5, 32.2], 70],
  ['puertaalta', [27.6, 1.6, 30.4], [38.4, 1.9, 33.0], 72],
  ['tumbado', [4.6, 1.6, 33.8], [12.4, 1.5, 38.6], 74],
  ['tabiques', [14.6, 1.7, 33.8], [23.6, 1.3, 46], 74],
];

// close up: the paper and a row of sockets, the ceiling, the carpet, the chair, the slit, the floating pillar, the door
export const CLOSE = [
  ['enchufes2', [8.0, 0.9, 31.0], [8.6, 0.35, 32.4], 50],
  ['techo', [7.0, 1.6, 4.6], [8.2, 2.74, 6.8], 64],
  ['moqueta', [6.0, 1.25, 5.6], [6.6, 0, 7.2], 55],
  ['silla', [6.0, 1.35, 13.8], [7.5, 0.45, 11.8], 60],
  ['rendija', [17.4, 1.6, 18.6], [22, 1.45, 18.6], 62],
  ['pilarflota', [44.6, 0.9, 13.2], [42, 0.3, 10.8], 62],
  ['salida', [7.6, 1.6, 6.6], [3.6, 1.15, 6.6], 62],
  ['alta', [34.8, 1.6, 31.6], [38.4, 1.95, 33.0], 60],
];

export function plan(S = 960) {
  const c = document.createElement('canvas'); c.width = c.height = S;
  const x = c.getContext('2d'), k = S / BP.P, C = BP.C, N = BP.N;
  x.fillStyle = '#1a1a1a'; x.fillRect(0, 0, S, S);
  const hue = (id) => { const h = ((id * 47) % 360); return `hsl(${h},35%,${id ? 62 : 12}%)`; };
  for (let z = 0; z < N; z++) for (let i = 0; i < N; i++) { const id = BP.ID[z * N + i]; x.fillStyle = id ? hue(id) : '#202020'; x.fillRect(i * C * k, z * C * k, C * k + 0.5, C * k + 0.5); }
  x.font = 'bold 14px sans-serif'; x.fillStyle = 'rgba(0,0,0,0.75)';
  for (const [r, x0, z0, x1, z1] of BP.ROOMS) x.fillText(r, ((x0 + x1 + 1) / 2) * C * k - 5, ((z0 + z1 + 1) / 2) * C * k + 5);
  const col = ['', '#000', '#e04040', '', '#4060e0', '#e0a020'];
  for (const [E, o] of [[BP.VE, 'v'], [BP.HE, 'h']]) for (let z = 0; z < N; z++) for (let i = 0; i < N; i++) {
    const ty = E[z * N + i]; if (!ty || ty === 3) continue;
    x.strokeStyle = col[ty]; x.lineWidth = ty === 1 ? 2.5 : 2;
    x.beginPath();
    if (o === 'v') { x.moveTo(i * C * k, z * C * k); x.lineTo(i * C * k, (z + 1) * C * k); } else { x.moveTo(i * C * k, z * C * k); x.lineTo((i + 1) * C * k, z * C * k); }
    x.stroke();
  }
  for (const l of BP.LAMPS) { x.fillStyle = l.st === 0 ? '#fff6c0' : l.st === 2 ? '#ff60ff' : '#555'; const w = l.ax === 'x' ? 1.2 : 0.6, d = l.ax === 'x' ? 0.6 : 1.2; x.fillRect(l.u0 * k, l.v0 * k, w * k, d * k); }
  x.fillStyle = '#222'; for (const [cx, cz, fl] of BP.PILLARS) { x.fillStyle = fl ? '#a04' : '#222'; x.fillRect((cx * C - 0.3) * k, (cz * C - 0.3) * k, 0.6 * k, 0.6 * k); }
  x.strokeStyle = '#000'; x.lineWidth = 2; for (const [a, b, c2, d] of BP.SLANTS) { x.beginPath(); x.moveTo(a * k, b * k); x.lineTo(c2 * k, d * k); x.stroke(); }
  x.fillStyle = 'rgba(80,60,40,0.8)'; x.fillRect(BP.STAIRS.x0 * k, BP.STAIRS.z0 * k, (BP.STAIRS.x1 - BP.STAIRS.x0) * k, (BP.STAIRS.z1 - BP.STAIRS.z0) * k);
  for (const [dx, dz, , kind] of BP.DOORS) { x.fillStyle = kind === 'exit' ? '#ffd000' : kind === 'high' ? '#00d0ff' : '#ffffff'; x.beginPath(); x.arc(dx * k, dz * k, 6, 0, 6.283); x.fill(); }
  for (const [cx, cz] of BP.CHAIRS) { x.fillStyle = '#40ff60'; x.beginPath(); x.arc(cx * k, cz * k, 4, 0, 6.283); x.fill(); }
  return post('br_plan', c).then(() => 'br_plan');
}

export async function enter() {
  const g = G(), I = g.interiors;
  if (g.interior && g.interior.backrooms) return { ms: g.interior.bakeMs };
  if (g.interior) I.leave();
  const t0 = performance.now();
  await I.enter({ venue: 'backrooms', name: 'Nivel 0', sub: '«The Lobby» · los Backrooms', seed: 1 }, { silent: true, mode: 'visit' });
  return { ms: Math.round(performance.now() - t0), bake: g.interior.bakeMs };
}

export async function shoot(tag = '', views = VIEWS, { W = 960, H = 600 } = {}) {
  const g = G();
  if (!(g.interior && g.interior.backrooms)) await enter();
  const h = g.interior, O = h.origin;
  const keepR = g.render; g.render = () => {};
  g.renderer.setSize(W, H, false);
  const cam = new THREE.PerspectiveCamera(70, W / H, 0.05, 400);
  const out = [];
  try {
    for (let i = 0; i < 3; i++) { g.state = 'play'; g.frame(1 / 30); }
    for (const [name, e, t, fov] of views) {
      cam.fov = fov; cam.aspect = W / H; cam.position.set(O.x + e[0], e[1], O.z + e[2]); cam.lookAt(O.x + t[0], t[1], O.z + t[2]); cam.updateProjectionMatrix(); cam.updateMatrixWorld();
      g.sky.update(0, cam.position, true); g.interiors.dimSky();
      const keep = g.camera; g.camera = cam;
      try { g.renderView(cam); } finally { g.camera = keep; }
      const c = g.renderer.domElement, o = document.createElement('canvas'); o.width = c.width; o.height = c.height; o.getContext('2d').drawImage(c, 0, 0);
      await post(`br_${name}_${tag}`, o);
      out.push(`br_${name}_${tag}`);
    }
  } finally { g.render = keepR; g.resize(); }
  return out;
}
