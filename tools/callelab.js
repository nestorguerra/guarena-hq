// Calles lab: the user's Google Maps captures of the old town (~/Desktop/Guareña, 2026-10-12: 95 street-level views of
// 26 streets and squares) as camera poses (tools/fachadas/capturas.py → .cache/calles/poses.json), and the game
// photographed from each of them at the captures' size, to compare façade by façade. The captures are only a reference
// for modelling by hand: nothing of them goes into the game.
//   const CL = await import('/tools/callelab.js?' + Date.now());
//   await CL.shot(3)                       // view 3 → .snaps/calle_003.jpg
//   await CL.some([0, 1, 2], { tag: 'b' })  // several (the town built once)
//   await CL.folder('Calle Grande')         // every view of one street
import { setup } from '/tools/playtest.js';

let POSES = null;
export async function poses() {
  if (POSES) return POSES;
  const P = await (await fetch('/.cache/calles/poses.json?' + Date.now())).json();
  // (the cameras put back where they stood, where Google's GPS had them metres off: tools/fachadas/camaras.py)
  let fit = {};
  try { const r = await fetch('/.cache/calles/camaras.json?' + Date.now()); if (r.ok) fit = await r.json(); } catch (e) { /* none yet */ }
  for (const v of P) { const f = fit[v.id]; if (f) Object.assign(v, { x: f.x, z: f.z, heading: f.heading, eye: f.eye, fitted: f.moved }, f.fov ? { fov: f.fov } : {}); }
  return (POSES = P);
}
const yieldNow = () => new Promise((r) => { const ch = new MessageChannel(); ch.port1.onmessage = () => r(); ch.port2.postMessage(0); });
const step = (n) => { const G = window.game; for (let i = 0; i < n; i++) { if (G.state !== 'play') { G.state = 'play'; const p = document.getElementById('pause'); if (p) p.hidden = true; } G.frame(1 / 30); } };

// the camera where the Street View one stood (its eye 2.5 m up, the car's, unless its fitting found otherwise)
export function pose(v, o = {}) {
  const G = window.game, c = G.camera;
  const x = v.x + (o.dx || 0), z = v.z + (o.dz || 0);
  const h = ((v.heading + (o.dh || 0)) * Math.PI) / 180, up = ((v.pitch + (o.dp || 0)) * Math.PI) / 180;
  c.fov = v.fov + (o.dfov || 0);
  c.position.set(x, o.eye ?? v.eye ?? 2.5, z);
  c.lookAt(x + Math.sin(h) * Math.cos(up), c.position.y + Math.sin(up), z - Math.cos(h) * Math.cos(up)); // (compass heading → x east, z south)
  c.updateProjectionMatrix(); c.updateMatrixWorld(true);
}
export async function shot(id, o = {}) {
  const G = window.game, r = G.renderer, w = o.w || 1440, h = o.h || 693, v = (await poses())[id];
  await setup();
  if (G.player.vehicle) G.player.exitVehicle(true);
  G.player.spawnAt(v.x, v.z, 0);
  G.sky.hour = o.hour ?? 12.5;
  if (G.weather && o.clear !== false) { const W = G.weather; clearTimeout(W.timer); W.on = false; W.data = null; Object.assign(W.now, { cover: 0.15, over: 0, rain: 0, snow: 0, fog: 0, storm: 0, fogFar: 3000 }); }
  step(o.warm ?? 45);
  r.setSize(w, h, false);
  if (G.composer) { G.composer.setSize(w, h); if (G.bloom) G.bloom.setSize(w, h); }
  G.camera.aspect = w / h;
  const body = G.player.char && G.player.char.object;
  if (body) body.visible = false;
  for (let k = 0; k < 4; k++) { step(1); pose(v, o); G.sky.update(0, G.camera.position); G.render(); }
  const c = r.domElement, out = document.createElement('canvas');
  out.width = w; out.height = h; out.getContext('2d').drawImage(c, 0, 0, c.width, c.height, 0, 0, w, h);
  if (body) body.visible = true;
  await fetch('/__snap?name=' + (o.name || 'calle_' + String(id).padStart(3, '0') + (o.tag ? '_' + o.tag : '')), { method: 'POST', body: out.toDataURL('image/jpeg', 0.88) });
  return { id, folder: v.folder, file: v.file };
}
export async function some(list, o = {}) {
  const done = [];
  for (const id of list) { done.push(await shot(id, o)); await yieldNow(); }
  window.game.resize();
  return done;
}
export async function folder(name, o = {}) {
  const P = await poses();
  return some(P.filter((v) => v.folder === name).map((v) => v.id), o);
}
