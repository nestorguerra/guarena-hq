// Dev-only: paints the drone's picture of Guareña the page shows while the game loads (src/intro.js), from exactly the
// camera the live flight starts at, in the look the game is running in: .snaps/intro.jpg in Plastilina (copy it to
// assets/intro.jpg), .snaps/intro_real.jpg in Realista (assets/intro_real.jpg). The town's own fair morning: the hour
// of the way in, the weather held neutral. With { cerca: 1.8 } the same view with the lens drawn in 1.8 times
// (…_cerca.jpg): the sharp picture the zoom goes on with while the town loads (index.html, guarenaZoom).
//   const I = await import('/tools/intro.js?' + Date.now()); await I.paint(); await I.paint({ cerca: 1.8 })
import * as THREE from 'three';
const G = () => window.game;
export async function paint({ W = 1920, H = 1080, q = 0.86, cerca = 0 } = {}) {
  const g = G(), I = await import('/src/intro.js'), M = await import('/src/materials.js'), S = await import('/src/style.js');
  const Wx = await import('/src/weather.js');
  const plan = I.introPlan(g);
  g.sky.hour = I.INTRO.hour;
  if (g.weather) { g.weather.hold = true; Object.assign(g.weather.now, Wx.NEUTRAL); }
  const fov = cerca ? THREE.MathUtils.radToDeg(2 * Math.atan(Math.tan(THREE.MathUtils.degToRad(I.INTRO.fov / 2)) / cerca)) : I.INTRO.fov;
  const cam = new THREE.PerspectiveCamera(fov, W / H, I.nearAt(plan.D0.y), 4200);
  cam.position.copy(plan.D0); cam.lookAt(plan.T); cam.updateMatrixWorld();
  // the protagonist where the flight will find her, so she is in the picture too
  if (g.player && g.player.char) { g.player.spawnAt(plan.P.x, plan.P.z, plan.heading); g.player.char.object.visible = true; }
  const night = g.sky.update(0, cam.position, true, cam);
  M.shared.uNight.value = night;
  await I.buildAround(g, plan.P); // (all of it built round her door, as the way in has it before flying)
  // (the town's detail streamed round her door, as the way in keeps it the whole way down: game.js, introFocus)
  for (let i = 0; i < 8; i++) { g.world._lodT = 0; g.world.update(0.016, night, plan.P); g.chars.updateLods(cam.position, true); await new Promise((r) => setTimeout(r, 30)); }
  const pr = g.renderer.getPixelRatio();
  g.renderer.setPixelRatio(1); g.renderer.setSize(W, H, false);
  if (g.composer) { if (g.composer.setPixelRatio) g.composer.setPixelRatio(1); g.composer.setSize(W, H); }
  if (g.updateBloom) g.updateBloom();
  for (let i = 0; i < 3; i++) g.renderView(cam);
  const c = g.renderer.domElement, o = document.createElement('canvas'); o.width = W; o.height = H;
  o.getContext('2d').drawImage(c, 0, 0, c.width, c.height, 0, 0, W, H);
  // (its mean colour: the page's ground behind the picture until it shows — index.html, #intro)
  const d = o.getContext('2d').getImageData(0, 0, W, H).data; let r = 0, gg = 0, b = 0, n = 0;
  for (let i = 0; i < d.length; i += 4 * 97) { r += d[i]; gg += d[i + 1]; b += d[i + 2]; n++; }
  const name = (S.STYLE.plastilina ? 'intro' : 'intro_real') + (cerca ? '_cerca' : '');
  await fetch('/__snap?name=' + name, { method: 'POST', body: o.toDataURL('image/jpeg', q) });
  g.renderer.setPixelRatio(pr); g.resize();
  const hex = '#' + [r, gg, b].map((v) => Math.round(v / n).toString(16).padStart(2, '0')).join('');
  return { name, P: plan.P.toArray().map((v) => +v.toFixed(1)), heading: +plan.heading.toFixed(3), D0: plan.D0.toArray().map((v) => +v.toFixed(2)), T: plan.T.toArray().map((v) => +v.toFixed(2)), mean: hex };
}
