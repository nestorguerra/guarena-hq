// The names on the signs (technical backlog, epic R). A sign that names a brand or a business says it through its
// entity (data/rotulos/marcas.json): the published game shows the public name — a brand's parody, a local business's
// generic (src/rotulos_datos.js) —; a local copy of the game, the one that has data/rotulos/reales.local.json beside it
// (never committed, never published), the real one. And every sign the game draws is put on the inventory (R-01).
import * as THREE from 'three';
import { ROTULOS } from './rotulos_datos.js';

let REALES = null;
export const ROT = { modo: 'parodia', inventario: [] };
if (typeof window !== 'undefined') window.__rotulos = ROT; // (for the test tools: tools/rotulos)

// (at boot, before the town is built: a published copy has no such file — or cannot fetch it — and keeps the parodies)
export async function cargarReales() {
  try {
    const r = await fetch('data/rotulos/reales.local.json', { cache: 'no-store' });
    if (r.ok) { REALES = await r.json(); ROT.modo = 'real'; }
  } catch (e) { /* (the published copy) */ }
}

// what a sign of that entity reads (r) or how it is called (n); a text with no entity, as it is
export function rotulo(id, campo = 'r') {
  const e = (ROT.modo === 'real' && REALES && REALES[id]) || ROTULOS[id];
  return e ? e[campo] : '';
}

// (a local copy: the entity whose real names include a business's name in the map — an OpenStreetMap name a capture
// corrected, R-05 —; a published copy has no real names and finds none)
const _nom = (t) => (t || '').normalize('NFD').replace(/[^A-Za-z0-9]/g, '').toUpperCase();
export function entidadPorNombre(name) {
  if (!REALES || !name) return null;
  for (const [id, e] of Object.entries(REALES)) if ((e.alias || []).some((a) => _nom(a) === _nom(name))) return id;
  return null;
}

// every sign put up: { id (stable), tipo, texto, poi?, x, z, bid? } — tools/rotulos read it (inventory, checks)
export function registrar(s) { ROT.inventario.push(s); return s; }

// a sign that is a mesh of its own (a plaque, a name board over a gate): its words on it, and when the inventory is
// taken (recoger) its place and the way it faces — the plane's +z — from where it ended up in the town
export function marcar(mesh, info) { mesh.userData.rotulo = info; return mesh; }
const _p = new THREE.Vector3(), _q = new THREE.Quaternion(), _n = new THREE.Vector3();
export function recoger(scene) {
  const have = new Set(ROT.inventario.map((s) => s.id));
  scene.updateMatrixWorld(true);
  scene.traverse((o) => {
    const r = o.userData && o.userData.rotulo;
    if (!r) return;
    o.getWorldPosition(_p); o.getWorldQuaternion(_q); _n.set(0, 0, 1).applyQuaternion(_q);
    let id = r.id, k = 2;
    while (have.has(id)) id = r.id + '#' + k++;
    have.add(id);
    const g = o.geometry && o.geometry.parameters;
    registrar({ id, tipo: r.tipo, texto: r.texto, poi: r.poi || null, x: _p.x, y: _p.y, z: _p.z, nx: _n.x, nz: _n.z, caras: r.caras || 1, w: g ? g.width : null, h: g ? g.height : null });
  });
  return ROT.inventario;
}
ROT.recoger = recoger; ROT.Raycaster = THREE.Raycaster; // (the test tools take the inventory, and a ray to look along, through window.__rotulos)
