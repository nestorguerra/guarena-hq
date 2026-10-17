// The interiors' lab (technical backlog, epic I): a kit built at its own spot far from the town, photographed from fixed
// cameras (I-04's four shots), and its layout handed to the validator. From the test tools, in the game's page:
//   const L = await import('/tools/interiores/lab.js'); await L.fotos('cafeteria', 7, 'tag')  → .snaps/int_cafeteria_7_tag_k.jpg
import { buildLocal } from '/src/locales.js';
import { partes, mapaPaso } from '/src/interiores_geo.js';
const ORIGIN = { x: -8600, z: -8600 };
// (the room on show is kept on the page, not in this module: the tools import it afresh for each kit, and the last one
// must go before the next is put at the same spot)
export function montar(tip, seed) {
  const g = window.game;
  const cur = window.__labLocal;
  if (cur) { g.scene.remove(cur.group); cur.group.traverse((o) => { if (o.isMesh) o.geometry.dispose(); }); window.__labLocal = null; }
  const h = buildLocal(tip, seed, ORIGIN, 'Prueba');
  g.scene.add(h.group);
  window.__labLocal = h;
  return h;
}
// the four fixed cameras: from the door, from the back, along the counter, over the room — each one stood where a body
// can stand (src/interiores_geo.js), never inside a piece of furniture or a partition
export function camaras(h) {
  const L = h.local, { W, D, H } = L, o = ORIGIN;
  const piezas = L.colocados.filter((c) => c.regla !== 'techo').flatMap((c) => partes(c));
  const m = mapaPaso({ W, D, zonas: L.zonas, tabiques: L.tabiques }, piezas, 0.1, 0.5, L.puertaX || 0);
  const libres = [];
  const publicas = Object.values(L.zonas).filter((z) => z.publica);
  for (let k = 0; k < m.nz; k++) for (let i = 0; i < m.nx; i++) {
    const x = -W / 2 + (i + 0.5) * m.S, z = (k + 0.5) * m.S;
    if (m.reach[k * m.nx + i] && publicas.some((Z) => x > Z.x0 && x < Z.x1 && z > Z.z0 && z < Z.z1)) libres.push([x, z]); // (where a customer stands)
  }
  const cerca = (x, z) => libres.reduce((b, c) => (Math.hypot(c[0] - x, c[1] - z) < Math.hypot(b[0] - x, b[1] - z) ? c : b), libres[0] || [x, z]);
  const fondo = libres.reduce((b, c) => (c[1] - Math.abs(c[0]) * 0.3 > b[1] - Math.abs(b[0]) * 0.3 ? c : b), libres[0] || [0, D - 2]);
  const Z = L.zonas.barra || L.zonas.mostrador;
  const c2 = Z ? cerca(Z.x0 - 1.1, Z.z0 - 0.5) : cerca(W / 2 - 0.8, 1.0);
  return [
    { p: [o.x + 0.3, 1.65, o.z + 0.6], t: [o.x, 1.2, o.z + D * 0.7] },
    { p: [o.x + fondo[0], 1.65, o.z + fondo[1]], t: [o.x, 1.2, o.z + D * 0.2] },
    Z ? { p: [o.x + c2[0], 1.6, o.z + c2[1]], t: [o.x + Z.x0 + 0.5, 1.1, o.z + Z.z1] } : { p: [o.x + c2[0], 1.7, o.z + c2[1]], t: [o.x - W / 4, 1.1, o.z + D - 3] },
    { p: [o.x - W / 2 + 0.4, H - 0.25, o.z + 0.4], t: [o.x + W / 3, 0.2, o.z + D * 0.6] },
  ];
}
export async function fotos(tip, seed, tag = 'a', w = 1280, hgt = 720) {
  const g = window.game, r = g.renderer, cam = g.camera;
  const h = montar(tip, seed);
  const body = g.player.char && g.player.char.object; if (body) body.visible = false;
  r.setSize(w, hgt, false); if (g.composer) { g.composer.setSize(w, hgt); if (g.bloom) g.bloom.setSize(w, hgt); }
  cam.aspect = w / hgt; cam.fov = 70; cam.updateProjectionMatrix();
  const out = [];
  for (const [k, c] of camaras(h).entries()) {
    cam.position.set(...c.p); cam.lookAt(...c.t); cam.updateMatrixWorld(true);
    g.sky.update(0, cam.position); g.render(); g.render();
    const name = `int_${tip}_${seed}_${tag}_${k}`;
    await fetch('/__snap?name=' + name, { method: 'POST', body: r.domElement.toDataURL('image/jpeg', 0.88) });
    out.push(name);
  }
  return { fotos: out, hash: h.local.hash, n: h.local.colocados.length, W: h.local.W, D: h.local.D, luces: h.local.luces.length };
}
