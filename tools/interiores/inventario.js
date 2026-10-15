// The inventory of the interiors (technical backlog, I-01), taken in the game's page once the town is up: every door you
// can go in by — the shops and bars (src/shops.js), the houses, the church and the town's own buildings
// (src/interiors.js) — with the interior it leads to, built once here to see that it exists and how big it is; and every
// business of the map (its OpenStreetMap kind) with or without a door yet. tools/interiores/inventario.py writes it.
//   const I = await import('/tools/interiores/inventario.js'); await I.inventario()
import { buildShop, SHOP_TYPES } from '/src/shops.js';
import { buildHouse, buildAnnieHouse } from '/src/interiors.js';
import { buildVecino } from '/src/houses.js';
import { buildChurch } from '/src/church.js';
import { buildVenue } from '/src/venues.js';
import { KITS } from '/src/interiores_datos.js';

const ORIGIN = { x: -9800, z: -9800 };
// what a business of the map is, by its OpenStreetMap kind
const COMERCIO = /^(shop:|amenity:(bar|cafe|bank|pharmacy|restaurant|fast_food|pub|post_office|driving_school|dentist|clinic|library|casino)$|office:|craft:)/;
export function tipologiaDe(kind) {
  if (/^amenity:(bar|pub|casino)$/.test(kind)) return 'bar';
  if (kind === 'amenity:cafe') return 'cafeteria';
  if (/^amenity:(restaurant|fast_food)$/.test(kind)) return 'restaurante';
  if (/^shop:(supermarket|convenience|greengrocer|bakery|confectionery|butcher|deli|frozen_food)$/.test(kind)) return 'alimentacion';
  if (/^shop:(clothes|shoes|boutique|fashion)$/.test(kind)) return 'tienda_ropa';
  if (kind === 'amenity:pharmacy') return 'farmacia';
  if (kind === 'amenity:bank') return 'sucursal_bancaria';
  if (/^(office:|amenity:(post_office|driving_school|dentist|clinic|library)$)/.test(kind)) return 'oficina';
  if (kind === 'leisure:fitness_centre') return 'gimnasio';
  return 'tienda_especializada';
}
// the game's shop types → typology
const TIPO_TIENDA = { bar: 'bar', cafeteria: 'cafeteria', super: 'alimentacion', fruteria: 'alimentacion', panaderia: 'alimentacion', kebab: 'restaurante', gimnasio: 'gimnasio' };
// the town's own buildings: one of a kind, made by hand (no kit): their typology is «singular»
const SINGULAR = { ayto: 'Ayuntamiento', teatro: 'Teatro', mercado: 'Mercado de Abastos', pabellon: 'Pabellón', corbacho: 'Casa-palacio de los Corbacho', sangregorio: 'Ermita de San Gregorio' };

const area = (h) => (h && h.bounds ? +((h.bounds.x1 - h.bounds.x0) * (h.bounds.z1 - h.bounds.z0)).toFixed(1) : null);
const tirar = (h) => { if (h && h.group) h.group.traverse((o) => { if (o.isMesh) { o.geometry.dispose(); } }); };
function construye(fn) {
  try { const h = fn(); const a = area(h); const extra = h && h.local ? { semilla_kit: h.local.seed, kit: h.local.kit } : {}; tirar(h); return { ok: !!h, superficie_m2: a, ...extra }; } catch (e) { return { ok: false, error: String(e && e.message || e).slice(0, 200) }; }
}

export async function inventario() {
  const g = window.game, map = g.map, out = [], errores = [];
  const edificio = (x, z) => { const b = map.buildingAt(x, z); return b ? b.id ?? map.buildings.indexOf(b) : null; };
  // ---- the shops and bars
  const conPuerta = new Set();
  for (const s of g.shops.list) {
    const T = SHOP_TYPES[s.type], poi = s.poi != null && s.poi >= 0 ? s.poi : null;
    if (poi != null) conPuerta.add(poi);
    const tip = TIPO_TIENDA[s.type] || 'tienda_especializada', kit = T.kit && KITS[T.kit] ? T.kit : null;
    const b = construye(() => buildShop(s.type, s.seed, ORIGIN, s.title));
    const id = `tienda:${s.type}:${s.seed}`;
    if (!b.ok) errores.push(`${id}: la puerta lleva a un interior que no se construye (${b.error})`);
    out.push({ interior_id: id, puerta: { x: +s.x.toFixed(2), z: +s.z.toFixed(2) }, building_id: edificio(s.fx ?? s.x, s.fz ?? s.z), poi_id: poi, osm: poi != null ? map.pois[poi].kind : null,
      tipologia: tip, nombre: s.title, superficie_m2: b.superficie_m2, accesible: true, estado: !b.ok ? 'vacio' : kit ? 'completo' : 'basico', kit, constructor: kit ? 'locales.js (kit)' : 'shops.js (a mano)' });
  }
  // ---- the doors of the houses, the church and the town's buildings
  for (const d of g.interiors.doors) {
    let id, tip, b, nombre = d.name, extra = {};
    if (d.church) { id = `iglesia:${d.church}`; tip = 'singular'; b = construye(() => buildChurch(d.seed, ORIGIN)); }
    else if (d.venue) { id = `edificio:${d.venue}`; tip = 'singular'; nombre = SINGULAR[d.venue] || d.name; b = construye(() => buildVenue(d.venue, d.seed, ORIGIN)); }
    else if (d.owner === 'annie') { id = 'vivienda:annie'; tip = 'vivienda'; b = construye(() => buildAnnieHouse(d.seed, ORIGIN)); }
    else if (d.seed >= 1000) { id = `vivienda:${d.seed}`; tip = 'vivienda'; b = construye(() => buildVecino(d.seed, ORIGIN)); }
    else { id = `vivienda:${d.seed}`; tip = 'vivienda'; b = construye(() => buildHouse('casa', d.seed, ORIGIN)); }
    if (tip === 'vivienda') extra.estancias = ['salon', 'cocina', 'dormitorio', 'bano'];
    if (!b.ok) errores.push(`${id}: la puerta lleva a un interior que no se construye (${b.error})`);
    out.push({ interior_id: id, puerta: { x: +d.x.toFixed(2), z: +d.z.toFixed(2) }, building_id: edificio(d.fx ?? d.x, d.fz ?? d.z), poi_id: null, osm: null,
      tipologia: tip, nombre, superficie_m2: b.superficie_m2, accesible: true, estado: b.ok ? (tip === 'singular' ? 'completo' : 'basico') : 'vacio', kit: null, constructor: tip === 'singular' ? 'a mano (pieza única)' : 'interiors.js / houses.js (a mano)', ...extra });
  }
  // ---- the businesses of the map with no door yet
  map.pois.forEach((p, i) => {
    if (!COMERCIO.test(p.kind) || conPuerta.has(i) || !map.inTown(p.x, p.z)) return;
    out.push({ interior_id: `local:${i}`, puerta: null, building_id: edificio(p.x, p.z), poi_id: i, osm: p.kind, tipologia: tipologiaDe(p.kind), nombre: null, superficie_m2: null, accesible: false, estado: 'vacio', kit: null, constructor: null });
  });
  // ---- the checks (I-01): every door on the list, none to an interior that does not exist, none accessible without typology
  const ids = new Set();
  for (const r of out) { if (ids.has(r.interior_id)) errores.push(`${r.interior_id}: repetido`); ids.add(r.interior_id); if (r.accesible && !r.tipologia) errores.push(`${r.interior_id}: accesible sin tipología`); }
  const puertas = g.shops.list.length + g.interiors.doors.length, enLista = out.filter((r) => r.puerta).length;
  if (puertas !== enLista) errores.push(`puertas: ${puertas} en el juego, ${enLista} en el inventario`);
  return { puertas, interiores: out.length, errores, interiors: out };
}
