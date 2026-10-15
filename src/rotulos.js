// The names on the signs (technical backlog, epic R). A sign that names a brand or a business says it through its
// entity (data/rotulos/marcas.json): the published game shows the public name — a brand's parody, a local business's
// generic (src/rotulos_datos.js) —; a local copy of the game, the one that has data/rotulos/reales.local.json beside it
// (never committed, never published), the real one. And every sign the game draws is put on the inventory (R-01).
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

// every sign put up: { id (stable), tipo, texto, poi?, x, z, bid? } — tools/rotulos read it (inventory, checks)
export function registrar(s) { ROT.inventario.push(s); return s; }
