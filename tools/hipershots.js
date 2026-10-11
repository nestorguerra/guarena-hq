// Dev-only: photos of the hyperreal church (docs/hiperrealismo.md) for the reviewer — from where the references were
// taken, from the plaza, from a drone round it, and straight down over the same window as the PNOA crop.
//   const H = await import('/tools/hipershots.js?' + Date.now()); await H.shoot('a')  → .snaps/hq_<view>_<tag>.jpg
// Eyes and targets in the church's own frame (poi.churchFrame: x along the nave to the apse, z across, + south; y up
// from the ground), except the views given in the world (w: true).
import * as THREE from 'three';
const G = () => window.game;
async function post(name, W, H) {
  const c = G().renderer.domElement, o = document.createElement('canvas');
  o.width = W; o.height = H; o.getContext('2d').drawImage(c, 0, 0, c.width, c.height, 0, 0, W, H);
  await fetch('/__snap?name=' + name, { method: 'POST', body: o.toDataURL('image/jpeg', 0.9) });
}
function size(w, h) { const g = G(); g.renderer.setSize(w, h, false); if (g.composer) { g.composer.setSize(w, h); if (g.bloom) g.bloom.setSize(w, h); } }
// the views: [name, eye, target, fov, hour, W, H, world?]
export const VIEWS = [
  // the Commons photo «Iglesia Parroquial de Santa María (Guareña, España)»: the west front and the north side from
  // the north-west, in the late afternoon. Its camera: the focal from the photo's EXIF (Canon EOS 600D, APS-C, 18 mm,
  // uncropped: 45° of vertical field), the rest fitted to fifteen points of the photo whose plan places are known (the
  // corners, the north wall's ends, the four north windows, the two oculi), the eye at 1,6 m: 33 m from the north-west
  // corner, heading 44,8° off the axis, tilted up 19,2°, rolled −2,8° (the lens's own −3 % barrel is undone on the marks)
  // (its sun: the EXIF says 18:31 on 3-12-2019, but the sun sets there about 18:00 that day and the photo has direct
  // sun: the camera's clock ran an hour fast — the sun stood ≈4° up, bearing ≈237°. The game dims its sun near the
  // horizon (full only from ≈9° up: sky.js), far more than the real one, which at 4° still left the photo's sunlit
  // front 3,4 times brighter than its shaded north wall: the shot takes the photo's bearing at 9°)
  ['noroeste', [-43.3, 1.6, -35.2], [-9.79, 18.04, -1.93], 45.0, 18.6, 1440, 960, false, -2.8, [237, 9]],
  // the plaza to the east (refcompare's «Iglesia» spot)
  ['plaza', [-104, 1.7, -62], [-163, 14, -57], 60, 13.0, 1600, 900, true],
  // a drone round it, 30 m up, 70 m out
  ['dron_no', [-60, 30, -45], [0, 10, 0], 50, 11.0, 1600, 900],
  ['dron_so', [-55, 30, 50], [0, 10, 0], 50, 11.0, 1600, 900],
  ['dron_se', [55, 30, 55], [0, 10, 0], 50, 16.0, 1600, 900],
  ['dron_ne', [60, 30, -50], [0, 10, 0], 50, 16.0, 1600, 900],
  // close up (from the detail phase on): the west front from its street (6 m wide: the houses across begin at x ≈ −33),
  // a north window, the top of the tower
  ['fachada', [-32.5, 1.7, 0.5], [-25.9, 9.5, 0.5], 74, 18.6, 1200, 1200],
  ['ventana', [-6.9, 16.6, -22.5], [-6.9, 16.6, -13.5], 40, 15.0, 1200, 1200],
  ['torre', [-40, 30, 22], [-22.7, 31.5, 9.9], 42, 18.6, 1000, 1200],
];
// straight down over the PNOA crop's window (pnoa_iglesia.jpg: x −205 → −120, z −90 → −25, north up, 0.075 m/px)
export const TOP = { x0: -205, x1: -120, z0: -90, z1: -25, px: 0.075, hour: 12.5 };

export async function shoot(tag = 'a', { only = null, top = true, clear = false } = {}) {
  const g = G(), f = g.world.landmarks.poi.churchFrame;
  // (clear: the photo's clear evening, whatever the real weather is now — the live reading off for the shots)
  if (clear && g.weather) { g.weather.on = false; Object.assign(g.weather.now, { cover: 0.12, over: 0, rain: 0, snow: 0, fog: 0, storm: 0 }); }
  for (const id of ['pause', 'menu', 'hud']) { const el = document.getElementById(id); if (el) el.style.display = 'none'; }
  const keepR = g.render, keepResize = g.resize; g.render = () => {}; g.resize = () => {};
  const toW = (p) => f.group.localToWorld(new THREE.Vector3(p[0], p[1], p[2]));
  const gy = f.group.position.y;
  const out = [];
  try {
    for (const [name, e, t, fov, hour, W, H, world, roll = 0, sun = null] of VIEWS) {
      if (only && !only.includes(name)) continue;
      size(W, H);
      const cam = new THREE.PerspectiveCamera(fov, W / H, 0.1, 2000);
      const eye = world ? new THREE.Vector3(e[0], gy + e[1], e[2]) : toW(e);
      const tgt = world ? new THREE.Vector3(t[0], gy + t[1], t[2]) : toW(t);
      cam.position.copy(eye); cam.lookAt(tgt); if (roll) cam.rotateZ(THREE.MathUtils.degToRad(roll)); cam.updateProjectionMatrix(); cam.updateMatrixWorld();
      // (the player stands 4 m behind the eye, out of the picture: the streets and facades stream in round them)
      const bx = eye.x - tgt.x, bz = eye.z - tgt.z, bl = Math.hypot(bx, bz) || 1;
      g.sky.hour = hour; g.player.spawnAt(eye.x + 4 * bx / bl, eye.z + 4 * bz / bl, Math.atan2(-bx, -bz));
      // (a view's own sun, [bearing, height] in degrees: north 0°, east 90°)
      if (sun) { const az = THREE.MathUtils.degToRad(sun[0]), al = THREE.MathUtils.degToRad(sun[1]); g.sky.sunAt = new THREE.Vector3(Math.sin(az) * Math.cos(al), Math.sin(al), -Math.cos(az) * Math.cos(al)); } else g.sky.sunAt = null;
      for (let i = 0; i < 6; i++) { g.state = 'play'; g.frame(1 / 30); }
      g.sky.update(0, cam.position, true);
      const keep = g.camera; g.camera = cam;
      try { g.renderView(cam); } finally { g.camera = keep; }
      await post(`hq_${name}_${tag}`, W, H);
      out.push(name);
    }
    if (top && (!only || only.includes('cenital'))) {
      const T = TOP, W = Math.round((T.x1 - T.x0) / T.px), H = Math.round((T.z1 - T.z0) / T.px);
      size(W, H);
      const cam = new THREE.OrthographicCamera(T.x0 - (T.x0 + T.x1) / 2, T.x1 - (T.x0 + T.x1) / 2, (T.z1 - T.z0) / 2, -(T.z1 - T.z0) / 2, 1, 1000);
      cam.position.set((T.x0 + T.x1) / 2, gy + 400, (T.z0 + T.z1) / 2); cam.up.set(0, 0, -1); cam.lookAt(cam.position.x, 0, cam.position.z);
      cam.updateProjectionMatrix(); cam.updateMatrixWorld();
      g.sky.hour = T.hour; g.player.spawnAt(cam.position.x, cam.position.z, 0);
      for (let i = 0; i < 6; i++) { g.state = 'play'; g.frame(1 / 30); }
      const keep = g.camera; g.camera = cam;
      try { g.renderView(cam); } finally { g.camera = keep; }
      await post(`hq_cenital_${tag}`, W, H);
      out.push('cenital');
    }
  } finally { g.render = keepR; g.resize = keepResize; g.resize(); g.sky.sunAt = null; }
  return out;
}
