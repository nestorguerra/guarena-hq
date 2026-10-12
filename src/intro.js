// The way into the game, without menus: while the town is still being built, a drone's view of Guareña painted from
// exactly this camera (assets/intro.jpg in Plastilina, assets/intro_real.jpg in Realista; tools/intro.js paints them)
// drifts slowly closer; when the town is ready the live view takes over from the same point and flies on down to Annie,
// at her door in calle Malfeitos, and ends in the camera behind her: you are playing.
// 388 Pueblos (pueblos388.onrender.com) flies its own camera down to this same view first and fades into it: the
// camera, the field of view and the hour are the ones its page knows (web/js/jugar.js there), so they stay as they are.
import * as THREE from 'three';
import { polySample, polyNearest } from './util.js';
import { PLAYER_PRESETS } from './characters.js';

export const INTRO = { fov: 48, aspect: 16 / 9, zoomMax: 1.34, zoomTime: 26, flight: 9, hour: 10.6 };
// the drone's camera and where it looks (game metres): the view 388 Pueblos flies its own camera down to (its
// web/js/jugar.js, DRONE and TARGET) — pinned here, so that nothing changed in the town (the tower's landmark, say)
// moves the picture away from the page's last frame
export const VIEW = { D0: [239.21775900469402, 150, -289.8913002799052], T: [80.96342613091716, 0, -157.29580214110777] };

// who comes in: Annie — unless another character was chosen in the game itself (X · Cambiar personaje: save.pick);
// an older save's character (the old title menu's) does not count
export const ANNIE = PLAYER_PRESETS.find((p) => p.id === 'annie');
export function protagonist(save) {
  const c = save && save.custom;
  return c && save.pick && (c.id || 'custom') === save.pick ? c : ANNIE;
}

// where the protagonist starts, and the drone's first camera: the same every time — Annie's door, whoever comes in
export function introPlan(g) {
  const lm = g.world.landmarks.poi, map = g.map;
  const C = lm.churchTower || lm.plaza || { x: 0, z: 0 };
  const home = ANNIE && ANNIE.start;
  if (home) {
    // Annie's door: she starts facing up her street; the drone's picture looks over the roofs from beyond her house
    // towards the tower of Santa María, and the flight comes round and down to her
    const P = new THREE.Vector3(home.x, 0, home.z), heading = Number.isFinite(home.heading) ? home.heading : 0;
    const dir = new THREE.Vector3(Math.sin(heading), 0, Math.cos(heading)), side = new THREE.Vector3(-dir.z, 0, dir.x);
    const vc = new THREE.Vector3(C.x - P.x, 0, C.z - P.z).normalize(), sc = new THREE.Vector3(-vc.z, 0, vc.x);
    // (the drone: high beyond her house and a little to one side, looking over the roofs towards the tower — as
    // pinned in VIEW, which is this, measured once)
    const T = new THREE.Vector3(...VIEW.T), D0 = new THREE.Vector3(...VIEW.D0);
    return { P, dir, side, heading, T, D0, church: C, vc, sc };
  }
  const tmp = {};
  let best = null;
  for (const e of map.edges) {
    if (!e.walk || e.blocked || e.dirt || e.len < 20) continue;
    for (let s = 4; s < e.len - 4; s += 2.5) {
      polySample(e.pts, e.cum, s, tmp);
      const dx = C.x - tmp.x, dz = C.z - tmp.z, d = Math.hypot(dx, dz);
      if (d < 50 || d > 110) continue;
      const ux = dx / d, uz = dz / d, al = Math.abs(ux * tmp.dx + uz * tmp.dz); // (the street runs towards the church)
      if (al < 0.92) continue;
      if (map.buildingAt(tmp.x, tmp.z) || map.buildingAt(tmp.x - ux * 4, tmp.z - uz * 4)) continue;
      let clear = 0; // (nothing in the way until the church itself)
      for (let t = 0.1; t < 0.8; t += 0.05) if (!map.buildingAt(tmp.x + dx * t, tmp.z + dz * t)) clear++;
      const score = al * 2 + clear * 0.2 - Math.abs(d - 75) * 0.01;
      if (!best || score > best.score) best = { score, x: tmp.x, z: tmp.z, ux, uz };
    }
  }
  if (!best) best = { x: C.x + 30, z: C.z + 60, ux: -0.45, uz: -0.9 };
  const P = new THREE.Vector3(best.x, 0, best.z), dir = new THREE.Vector3(best.ux, 0, best.uz).normalize();
  const side = new THREE.Vector3(-dir.z, 0, dir.x);
  const heading = Math.atan2(dir.x, dir.z);
  const T = P.clone().addScaledVector(dir, 34);
  const D0 = P.clone().addScaledVector(dir, -165).addScaledVector(side, 55).add(new THREE.Vector3(0, 150, 0));
  return { P, dir, side, heading, T, D0, church: C };
}

// the town round her door built through at once — its façades, their windows and doors, the weeds in its yards: they
// stream in a few at a time round the camera while playing (facades.js); behind the picture they can all be built
// before the flight, which then meets nothing being put up on the way down (and tools/intro.js paints them so)
export async function buildAround(g, P, maxMs = 6000) {
  const fd = g.world && g.world.facades, t0 = performance.now();
  if (!fd || !fd.list) return;
  while (performance.now() - t0 < maxMs) {
    fd.update(P.x, P.z, 40);
    if (!fd.list.some((ch) => !ch.built && ch.d < fd.near + 60)) return;
    await new Promise((r) => setTimeout(r, 0));
  }
}

// the near plane for a camera this high (the drone's picture is painted with it too: tools/intro.js)
export function nearAt(h, near0 = 0.25) { return Math.max(near0, Math.min(6, h * 0.04)); }

// the camera that matches the picture zoomed in s times (the same view ray, s times closer to its target)
export function droneAt(plan, s, out = new THREE.Vector3()) {
  return out.copy(plan.D0).sub(plan.T).multiplyScalar(1 / s).add(plan.T);
}
// the picture's vertical field of view as the screen shows it (object-fit: cover crops one way or the other)
export function coverFov(aspect) {
  const t = Math.tan(THREE.MathUtils.degToRad(INTRO.fov / 2));
  return aspect > INTRO.aspect ? THREE.MathUtils.radToDeg(2 * Math.atan(t * INTRO.aspect / aspect)) : INTRO.fov;
}

const ease = (t) => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2);
// (a centripetal Catmull–Rom between p1 and p2: through its points, without loops or overshoots)
function catmull(p0, p1, p2, p3, u, out) {
  const d = (a, b) => Math.max(1e-3, Math.sqrt(a.distanceTo(b)));
  const t1 = d(p0, p1), t2 = t1 + d(p1, p2), t3 = t2 + d(p2, p3), t = t1 + (t2 - t1) * u;
  const L = (a, b, ta, tb) => a.clone().multiplyScalar((tb - t) / (tb - ta)).addScaledVector(b, (t - ta) / (tb - ta));
  const A1 = L(p0, p1, 0, t1), A2 = L(p1, p2, t1, t2), A3 = L(p2, p3, t2, t3);
  const B1 = L(A1, A2, 0, t2), B2 = L(A2, A3, t1, t3);
  return out.copy(L(B1, B2, t1, t2));
}
// the flight: from the drone (where the picture was when the town was ready) down to the game's own camera behind her.
// It goes through two points over the middle of her street — high above its roofs well behind her, then down between
// its houses just under the eaves — so that it comes down the street's own canyon and brushes no roof or balcony; its
// speed eased along the length of the way (slow off, slow in)
export class IntroFlight {
  constructor(plan, from, fromFov, to, toLook, toFov, map = null) {
    this.plan = plan; this.t = 0;
    const tmp = {};
    const centre = (back, h) => {
      const b = to.clone().addScaledVector(plan.dir, -back);
      const q = map && map.nearestEdge(b.x, b.z, 30, (e) => {
        polySample(e.pts, e.cum, polyNearest(e.pts, e.cum, b.x, b.z).s, tmp);
        return Math.abs(tmp.dx * plan.dir.x + tmp.dz * plan.dir.z) > 0.8; // (her own street, not a crossing)
      });
      if (q) { b.x = q.x; b.z = q.z; }
      b.y = h;
      return b;
    };
    const W = [from.clone(), centre(46, 34), centre(17, 7.5), to.clone()];
    const P = [W[0].clone().multiplyScalar(2).sub(W[1]), ...W, W[3].clone().multiplyScalar(2).sub(W[2])];
    this.pts = []; this.cum = [0];
    const v = new THREE.Vector3();
    for (let i = 1; i < P.length - 2; i++) for (let k = 0; k < 60; k++) this.pts.push(catmull(P[i - 1], P[i], P[i + 1], P[i + 2], k / 60, v).clone());
    this.pts.push(to.clone());
    for (let i = 1; i < this.pts.length; i++) this.cum.push(this.cum[i - 1] + this.pts[i].distanceTo(this.pts[i - 1]));
    this.l0 = plan.T.clone(); this.l1 = toLook.clone();
    this.f0 = fromFov; this.f1 = toFov;
    this._p = new THREE.Vector3(); this._l = new THREE.Vector3();
  }
  get done() { return this.t >= 1; }
  at(s, out) {
    const c = this.cum, n = c.length - 1;
    if (s >= c[n]) return out.copy(this.pts[n]);
    let lo = 0, hi = n;
    while (hi - lo > 1) { const m = (lo + hi) >> 1; if (c[m] <= s) lo = m; else hi = m; }
    return out.copy(this.pts[lo]).lerp(this.pts[hi], (s - c[lo]) / Math.max(1e-6, c[hi] - c[lo]));
  }
  update(dt, cam) {
    if (this.near0 === undefined) this.near0 = cam.near;
    this.t = Math.min(1, this.t + dt / INTRO.flight);
    const k = ease(this.t);
    const p = this.at(k * this.cum[this.cum.length - 1], this._p);
    // (high up, the near plane drawn out with the height: the depth buffer then tells the town's coplanar layers apart
    // — yard and pavement, the roofs' courses — which otherwise flicker through each other from a drone's distance)
    cam.near = this.t >= 1 ? this.near0 : nearAt(p.y, this.near0);
    const lk = ease(Math.min(1, this.t * 1.15));
    const l = this._l.copy(this.l0).lerp(this.l1, lk);
    cam.position.copy(p);
    cam.lookAt(l);
    cam.fov = this.f0 + (this.f1 - this.f0) * k;
    cam.updateProjectionMatrix();
  }
}
