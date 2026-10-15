// A sample sheet of the catalogue (family «tiendas_a»): objects stood in rows on a floor against a wall, labelled, shot from
// the front with the camera fitted to them — to see each object's shape and scale at close range — and views of a built
// shop from a few free spots. From the test tools, in the game's page (tools/interiores/muestrario_tiendas_a.py):
//   const M = await import('/tools/interiores/muestrario_tiendas_a.js'); await M.hoja(['id', …], 'tag')  → .snaps/ta_hoja_tag.jpg
import * as THREE from 'three';
import { construir, caja } from '/src/objetos.js';
import { OBJETOS } from '/src/interiores_datos.js';
import { buildLocal } from '/src/locales.js';
import { partes, mapaPaso } from '/src/interiores_geo.js';
const O = { x: -8300, z: -8300 };
function preparar(w, h) {
  const g = window.game, r = g.renderer, cam = g.camera;
  const body = g.player.char && g.player.char.object; if (body) body.visible = false;
  r.setSize(w, h, false); if (g.composer) { g.composer.setSize(w, h); if (g.bloom) g.bloom.setSize(w, h); }
  cam.aspect = w / h; cam.fov = 40; cam.updateProjectionMatrix();
  return { g, r, cam };
}
function etiqueta(texto, alto) {
  const c = document.createElement('canvas'); c.width = 512; c.height = 64;
  const x = c.getContext('2d'); x.fillStyle = 'rgba(255,255,255,0.85)'; x.fillRect(0, 0, 512, 64); x.fillStyle = '#111'; x.font = 'bold 30px Arial'; x.textAlign = 'center'; x.textBaseline = 'middle';
  x.fillText(texto, 256, 34, 500);
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace;
  const s = new THREE.Mesh(new THREE.PlaneGeometry(alto * 6, alto), new THREE.MeshBasicMaterial({ map: t, transparent: true }));
  return s;
}
async function foto(r, name) { await fetch('/__snap?name=' + name, { method: 'POST', body: r.domElement.toDataURL('image/jpeg', 0.9) }); return name; }
export async function hoja(ids, tag, { w = 1280, h = 720, hora = 12, fila = 6, yaw = 0, etiquetas = true, techo = 2.7 } = {}) {
  const { g, r, cam } = preparar(w, h);
  if (window.__muestra) { g.scene.remove(window.__muestra); window.__muestra.traverse((o) => { if (o.isMesh) o.geometry.dispose(); }); }
  const grp = new THREE.Group(); window.__muestra = grp; g.scene.add(grp);
  g.sky.hour = hora;
  // rows of up to `fila` objects, each row 1 object deeper than the last in z (they do not overlap on screen: laid out in a grid)
  const filas = []; for (let i = 0; i < ids.length; i += fila) filas.push(ids.slice(i, i + fila));
  let zr = 0, maxW = 0, maxH = 0.5;
  const rows = [];
  for (const row of filas) {
    let x = 0, prof = 0; const sep = 0.08 + Math.max(...row.map((id) => caja(id).w)) * 0.15;
    const items = [];
    for (const id of row) { const b = caja(id), o = OBJETOS[id]; const ancho = Math.max(b.w, 0.12); items.push({ id, b, o, x: x + ancho / 2 }); x += ancho + sep; prof = Math.max(prof, b.d); maxH = Math.max(maxH, o.soporte === 'techo' ? techo : b.y1); }
    rows.push({ items, w: x - sep, z: zr, prof });
    maxW = Math.max(maxW, x - sep); zr += prof + 0.6;
  }
  const fit = [];
  for (const rw of rows) for (const it of rw.items) {
    const o = it.o, b = it.b;
    const cx = O.x + it.x - rw.w / 2 - (b.x0 + b.x1) / 2, cz = O.z + rw.z - (b.z0 + b.z1) / 2 * 0 + (it.b.z0 < 0 ? -it.b.z0 : 0), y = o.soporte === 'techo' ? techo : 0;
    const items = [{ obj: it.id, x: cx, y, z: cz, ry: yaw, seed: 3, titulo: 'Casa Prueba' }];
    grp.add(construir(items));
    if (etiquetas) { const lab = etiqueta(it.id, Math.max(0.012, Math.min(maxW, 4) * 0.03)); lab.position.set(O.x + it.x - rw.w / 2, 0.03, O.z + rw.z + b.d + 0.1 + (b.z0 < 0 ? -b.z0 : 0)); lab.rotation.x = -0.6; grp.add(lab); }
  }
  // the floor and the wall behind the first row
  const wall = new THREE.Mesh(new THREE.PlaneGeometry(maxW + 4, maxH + 1.5), new THREE.MeshStandardMaterial({ color: 0xd8d4c8, roughness: 0.95 }));
  wall.position.set(O.x, (maxH + 1.5) / 2 - 0.2, O.z - 0.12); grp.add(wall);
  const floor = new THREE.Mesh(new THREE.PlaneGeometry(maxW + 4, zr + 4), new THREE.MeshStandardMaterial({ color: 0xb8a68a, roughness: 0.9 }));
  floor.rotation.x = -Math.PI / 2; floor.position.set(O.x, -0.002, O.z + zr / 2); grp.add(floor);
  // the camera: fitted to the sheet
  const tan = Math.tan((cam.fov * Math.PI) / 360), asp = w / h;
  const alto = maxH + 0.08, dist = Math.max(maxW / 2 / (tan * asp), alto / 2 / tan) * 1.08 + zr * 0.5 + 0.1;
  const tilt = zr > 1 ? 0.55 : 0.1; // (several rows: from above)
  cam.position.set(O.x, alto / 2 + dist * Math.sin(tilt) * 0.7, O.z + zr * 0.3 + dist); cam.lookAt(O.x, alto / 2, O.z + zr * 0.3); cam.updateMatrixWorld(true);
  g.sky.update(0, cam.position); g.render(); g.render();
  return await foto(r, 'ta_hoja_' + tag);
}
// a built shop seen from free spots: views = [{ p: [x, z], t: [x, z] }] in the room's frame (eyes 1.6 m, looking at 1.2)
export async function sala(kit, seed, tag, vistas, { w = 1280, h = 720, hora = 12, fov = 72 } = {}) {
  const { g, r, cam } = preparar(w, h);
  if (window.__labLocal) { g.scene.remove(window.__labLocal.group); window.__labLocal.group.traverse((o) => { if (o.isMesh) o.geometry.dispose(); }); window.__labLocal = null; }
  if (window.__muestra) { g.scene.remove(window.__muestra); window.__muestra = null; }
  const o = { x: -8600, z: -8600 };
  const hh = buildLocal(kit, seed, o, 'Casa Prueba'); g.scene.add(hh.group); window.__labLocal = hh; g.sky.hour = hora;
  const L = hh.local, { W, D, H } = L;
  if (!vistas) {
    const piezas = L.colocados.filter((c) => c.regla !== 'techo').flatMap((c) => partes(c));
    const m = mapaPaso({ W, D, zonas: L.zonas, tabiques: L.tabiques }, piezas, 0.1, 0.9, L.puertaX || 0);
    const libres = [];
    for (let k = 0; k < m.nz; k++) for (let i = 0; i < m.nx; i++) if (m.reach[k * m.nx + i]) libres.push([-W / 2 + (i + 0.5) * m.S, (k + 0.5) * m.S]);
    const cerca = (x, z) => libres.reduce((b, c) => (Math.hypot(c[0] - x, c[1] - z) < Math.hypot(b[0] - x, b[1] - z) ? c : b), libres[0]);
    const zf = Math.min(D - 0.5, Math.max(...Object.values(L.zonas).filter((q) => q.publica).map((q) => q.z1)));
    const defs = [[-0.3, 0.9, 0.25, 0.62], [0.3, 0.9, -0.25, 0.62], [-0.3, 0.35, 0.3, 0.8], [0.3, 0.35, -0.3, 0.8], [0, 0.97, 0, 0.0], [-0.3, 0.7, 0.3, 0.05], [0.3, 0.7, -0.3, 0.05], [0.1, 0.12, -0.2, 0.9]];
    vistas = defs.map(([px, pz, tx, tz]) => ({ p: cerca(px * W, 0.5 + pz * (zf - 0.5)), t: [tx * W, tz * zf] }));
  }
  cam.fov = fov; cam.updateProjectionMatrix();
  const out = [];
  for (const [k, v] of vistas.entries()) {
    cam.position.set(o.x + v.p[0], v.y || 1.6, o.z + v.p[1]); cam.lookAt(o.x + v.t[0], v.ty || 1.15, o.z + v.t[1]); cam.updateMatrixWorld(true);
    g.sky.update(0, cam.position); g.render(); g.render();
    out.push(await foto(r, `ta_sala_${kit}_${seed}_${tag}_${k}`));
  }
  return { fotos: out, W, D, n: L.colocados.length, hash: L.hash };
}
// the plan of a built shop seen from above, drawn on a canvas: zones, partitions, what stands on the floor (by kind), what hangs,
// and the cells a 0.9 m body reaches from the door (green) — for finding what shuts a zone off. → a data URL
export async function plano(kit, seed, px = 70) {
  const o = { x: -8000, z: -8000 };
  const hh = buildLocal(kit, seed, o, 'Plano'), L = hh.local, { W, D } = L;
  const piezas = L.colocados.flatMap((c) => c.regla === 'techo' ? [] : partes(c));
  const m = mapaPaso({ W, D, zonas: L.zonas, tabiques: L.tabiques }, piezas, 0.05, 0.9, L.puertaX || 0);
  const c = document.createElement('canvas'); c.width = Math.round(W * px) + 20; c.height = Math.round(D * px) + 20; const x = c.getContext('2d');
  x.fillStyle = '#fff'; x.fillRect(0, 0, c.width, c.height); x.translate(10 + (W / 2) * px, 10);
  const S = m.S; x.fillStyle = 'rgba(80,200,120,0.35)';
  for (let k = 0; k < m.nz; k++) for (let i = 0; i < m.nx; i++) if (m.reach[k * m.nx + i]) x.fillRect((-W / 2 + i * S) * px, k * S * px, S * px, S * px);
  x.strokeStyle = '#88a'; x.lineWidth = 1; x.font = '11px Arial'; x.fillStyle = '#88a';
  for (const Z of Object.values(L.zonas)) { x.strokeRect(Z.x0 * px, Z.z0 * px, (Z.x1 - Z.x0) * px, (Z.z1 - Z.z0) * px); x.fillText(Z.id, Z.x0 * px + 3, Z.z0 * px + 12); }
  for (const c0 of L.colocados) {
    const v = c0.v; x.save(); x.translate(v.cx * px, v.cz * px); x.rotate(-v.a);
    const sob = c0.sop != null, col = c0.regla === 'techo' ? 'rgba(255,200,0,0.4)' : sob ? 'rgba(220,80,80,0.7)' : c0.regla === 'pared' ? 'rgba(40,40,200,0.5)' : 'rgba(30,30,30,0.55)';
    x.fillStyle = col; x.fillRect(-v.hw * px, -v.hd * px, v.hw * 2 * px, v.hd * 2 * px); x.restore();
  }
  x.strokeStyle = '#000'; x.lineWidth = 3;
  for (const t of L.tabiques) { x.beginPath(); x.moveTo(t.ax * px, t.az * px); x.lineTo(t.bx * px, t.bz * px); x.stroke(); }
  x.strokeRect(-W / 2 * px, 0, W * px, D * px);
  return c.toDataURL('image/png');
}
