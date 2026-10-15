# The entities the signs name (technical backlog, R-02 … R-04), from data the repository already has:
#   R-03  the businesses of OpenStreetMap inside the playable area (data/bounds.geojson) out of the extract the map was
#         built from (data/guarena.osm, the OSM API's; the Overpass query that renews it: data/rotulos/overpass.ql, run
#         by hand with --descargar — R-12), with their name, brand, opening hours, id and the extract's date
#   R-02  data/rotulos/pois.json, every entity — OpenStreetMap's, the ones read in the captures (data/rotulos/marcas.json,
#         levantamiento_propio), the public institutions and the streets — checked against data/rotulos/poi.schema.json
#   R-04  data/rotulos/sign_poi_map.json: each sign of the inventory (data/rotulos/signs_inventory.json, inventario.py)
#         with its entity and a confidence (alta, media, baja), or marked generic with its reason; and
#         data/rotulos/cobertura.json: the businesses with no sign and the signs with no business
#   python3 tools/rotulos/entidades.py           → writes them; exit 1 if the schema or R-04's 100 % fails
import json, math, os, re, sys, unicodedata
import xml.etree.ElementTree as ET
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
D = os.path.join(ROOT, 'data', 'rotulos')
LAT0, LON0, R = 38.8596, -6.1025, 6378137.0
KX, KZ = math.cos(math.radians(LAT0)) * R * math.pi / 180.0, R * math.pi / 180.0
B_LAT0, B_LAT1, B_LON0, B_LON1 = 38.8465, 38.8695, -6.1195, -6.0745  # (the playable area: tools/build_map.py)
proj = lambda lat, lon: ((lon - LON0) * KX, -(lat - LAT0) * KZ)
REG = json.load(open(os.path.join(D, 'marcas.json'), encoding='utf-8'))
GEN = REG['genericos_por_tipo']

# R-03's tags: shop=*, these amenities, fitness centres, offices, crafts
AMENITY = {'restaurant', 'bar', 'cafe', 'fast_food', 'bank', 'pharmacy', 'pub'}
def wanted(t):
    if 'shop' in t: return 'shop:' + t['shop']
    if t.get('amenity') in AMENITY: return 'amenity:' + t['amenity']
    if t.get('leisure') == 'fitness_centre': return 'leisure:fitness_centre'
    if 'office' in t: return 'office:' + t['office']
    if 'craft' in t: return 'craft:' + t['craft']
    return None
CATEG = [(r'^shop:(supermarket|convenience|greengrocer|bakery|butcher|confectionery|pastry|deli|frozen_food|beverages)$', 'alimentación'),
         (r'^amenity:(restaurant|fast_food)$', 'restaurante'), (r'^amenity:(bar|pub)$', 'bar'), (r'^amenity:cafe$', 'cafetería'),
         (r'^amenity:bank$', 'banco'), (r'^amenity:pharmacy$', 'farmacia'), (r'^leisure:fitness_centre$', 'gimnasio'),
         (r'^office:', 'oficina'), (r'^(shop|craft):', 'tienda')]
categoria = lambda k: next((c for p, c in CATEG if re.search(p, k)), 'otro')
norm = lambda s: re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFD', (s or '').lower()).encode('ascii', 'ignore').decode())

def osm():
    tree = ET.parse(os.path.join(ROOT, 'data', 'guarena.osm')).getroot()
    nodes = {n.get('id'): (float(n.get('lat')), float(n.get('lon'))) for n in tree.iter('node')}
    fecha = max(e.get('timestamp', '')[:10] for e in tree if e.tag in ('node', 'way'))
    out, ways = [], {}
    for e in tree:
        if e.tag not in ('node', 'way'): continue
        t = {g.get('k'): g.get('v') for g in e.iter('tag')}
        if e.tag == 'node': lat, lon = nodes[e.get('id')]
        else:
            pts = [nodes[nd.get('ref')] for nd in e.iter('nd') if nd.get('ref') in nodes]
            if not pts: continue
            lat, lon = sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts)
            if t.get('highway') and t.get('name'): ways.setdefault(t['name'], []).append(e.get('id'))
        k = wanted(t)
        if not k or not (B_LAT0 <= lat <= B_LAT1 and B_LON0 <= lon <= B_LON1): continue
        x, z = proj(lat, lon)
        out.append({'id': f'osm:{e.tag}/{e.get("id")}', 'tipo_osm': k, 'name': t.get('name', ''), 'brand': t.get('brand'), 'opening_hours': t.get('opening_hours'),
                    'lat': round(lat, 7), 'lon': round(lon, 7), 'x': round(x, 2), 'z': round(z, 2)})
    return sorted(out, key=lambda p: p['id']), ways, fecha

# the schema's checker: the part of JSON Schema the schema uses (type, required, enum, pattern, properties, items, format)
def check(v, s, path='$'):
    errs = []
    t = s.get('type')
    if t:
        ok = {'object': isinstance(v, dict), 'array': isinstance(v, list), 'string': isinstance(v, str), 'null': v is None,
              'number': isinstance(v, (int, float)) and not isinstance(v, bool), 'boolean': isinstance(v, bool)}
        if not any(ok[x] for x in ([t] if isinstance(t, str) else t)): return [f'{path}: tipo {t}']
    if 'enum' in s and v not in s['enum']: errs.append(f'{path}: «{v}» fuera de {s["enum"]}')
    if isinstance(v, str) and 'pattern' in s and not re.search(s['pattern'], v): errs.append(f'{path}: «{v}» no cumple {s["pattern"]}')
    if isinstance(v, str) and s.get('minLength') and len(v) < s['minLength']: errs.append(f'{path}: vacío')
    if isinstance(v, dict):
        for r in s.get('required', []):
            if r not in v: errs.append(f'{path}: falta «{r}»')
        for k, sub in s.get('properties', {}).items():
            if k in v: errs += check(v[k], sub, f'{path}.{k}')
        if s.get('additionalProperties') is False:
            for k in v:
                if k not in s.get('properties', {}): errs.append(f'{path}: campo desconocido «{k}»')
    if isinstance(v, list) and 'items' in s:
        for i, x in enumerate(v): errs += check(x, s['items'], f'{path}[{i}]')
    return errs

def main():
    pois_osm, ways, fecha = osm()
    json.dump({'extracto': 'data/guarena.osm (API de OpenStreetMap)', 'ultima_edicion': fecha, 'consulta_renovacion': 'data/rotulos/overpass.ql',
               'atribucion': '© colaboradores de OpenStreetMap (ODbL)', 'pois': pois_osm}, open(os.path.join(D, 'osm_pois.json'), 'w'), ensure_ascii=False, indent=1, sort_keys=True)
    marcas = {e['id']: e for e in REG['entidades']}
    ents = []
    # (the businesses of OpenStreetMap: a brand of the registry by its own rules, any other its kind's generic in a public copy)
    reg_by_name = {norm(r): e for e in REG['entidades'] for r in e['real']}
    for p in pois_osm:
        e = reg_by_name.get(norm(p['name'])) or (reg_by_name.get(norm(p['brand'])) if p['brand'] else None)
        marca = e is not None and e['tipo'] == 'marca' or bool(p['brand'])
        ents.append({'poi_id': p['id'], 'nombre_visible': p['name'] or GEN.get(p['tipo_osm'], 'Comercio'), 'categoria': categoria(p['tipo_osm']), 'fuente': p['id'],
                     'fecha_verificacion': fecha, 'verificador': 'OpenStreetMap (sin revisar)', 'modo_rotulacion': 'parodia' if marca else 'genérico',
                     'nombre_parodia': (e['publico'] if e else None) if marca else None, 'nombre_publico': e['publico'] if e else GEN.get(p['tipo_osm'], 'Comercio'),
                     'atribucion': '© colaboradores de OpenStreetMap (ODbL)', 'evidencias': [], 'tipo_osm': p['tipo_osm'], 'horario': p['opening_hours'], 'lat': p['lat'], 'lon': p['lon']})
    # (the ones read in the captures — levantamiento_propio — with their capture as evidence)
    V = {}
    for e in REG['entidades']:
        ents.append({'poi_id': 'lev:' + e['id'], 'nombre_visible': e['real'][0], 'categoria': {'alimentación': 'alimentación', 'banco': 'banco', 'oficina': 'oficina', 'tienda': 'tienda', 'bar': 'bar'}.get(e['categoria'], 'otro'),
                     'fuente': 'levantamiento_propio', 'fecha_verificacion': '2026-10-15', 'verificador': 'auditoría de calles (capturas)', 'modo_rotulacion': e['modo'] if e['modo'] in ('parodia', 'genérico', 'real') else 'genérico',
                     'nombre_parodia': e['publico'] if e['modo'] == 'parodia' else None, 'nombre_publico': e['publico'], 'atribucion': None,
                     'evidencias': [f'captura vista {e["vista"]} (~/Desktop/Guareña, solo referencia)'] if e.get('vista') else []})
    # (the public institutions and the streets: their own names, real in every copy)
    inst = {'ayuntamiento': 'Ayuntamiento de Guareña', 'tarteso': 'Centro de Interpretación Tarteso', 'piscina': 'Piscina Municipal', 'teatro': 'Casa de la Cultura',
            'mercado': 'Mercado de Abastos', 'pabellon': 'Pabellón Municipal La Encina'}
    inv = json.load(open(os.path.join(D, 'signs_inventory.json'), encoding='utf-8'))['rotulos']
    for s in inv:
        if (s.get('poi') or '').startswith('inst:'):
            k = s['poi'][5:]
            if k not in inst: inst[k] = s['texto'].title()
    for k, n in sorted(inst.items()):
        ents.append({'poi_id': 'inst:' + k, 'nombre_visible': n, 'categoria': 'institución', 'fuente': 'levantamiento_propio', 'fecha_verificacion': '2026-10-15',
                     'verificador': 'datos del juego', 'modo_rotulacion': 'real', 'nombre_parodia': None, 'nombre_publico': n, 'atribucion': None, 'evidencias': []})
    for name in sorted(ways):
        ents.append({'poi_id': 'via:' + name, 'nombre_visible': name, 'categoria': 'otro', 'fuente': 'osm:way/' + sorted(ways[name], key=int)[0], 'fecha_verificacion': fecha,
                     'verificador': 'OpenStreetMap (sin revisar)', 'modo_rotulacion': 'real', 'nombre_parodia': None, 'nombre_publico': name,
                     'atribucion': '© colaboradores de OpenStreetMap (ODbL)', 'evidencias': []})
    schema = json.load(open(os.path.join(D, 'poi.schema.json'), encoding='utf-8'))
    errs = []
    for i, e in enumerate(ents): errs += check(e, schema, f'pois[{i}]')
    json.dump({'version': 1, 'pois': ents}, open(os.path.join(D, 'pois.json'), 'w'), ensure_ascii=False, indent=1, sort_keys=True)
    # ---- R-04: each sign and its entity
    M = json.load(open(os.path.join(ROOT, 'data', 'map.json'), encoding='utf-8'))
    mp = M['pois']
    def osm_of_map(pm):  # (a business of the game's map → the OpenStreetMap element it came from: same kind, within 3 m)
        if not pm: return None
        best = min((q for q in pois_osm if q['tipo_osm'] == pm['tipo']), key=lambda q: math.hypot(q['x'] - pm['x'], q['z'] - pm['z']), default=None)
        return best if best and math.hypot(best['x'] - pm['x'], best['z'] - pm['z']) < 3 else None
    rows = []
    for s in inv:
        x, z, poi, conf, motivo = s['mundo']['x'], s['mundo']['z'], None, None, None
        if s['subtipo'] == 'placa_calle':
            poi, conf = 'via:' + s['calle'], 'alta' if s['calle'] in ways else 'media'
        elif (s.get('poi') or '').startswith('inst:'): poi, conf = s['poi'], 'alta'
        elif (s.get('poi') or '').startswith('mapa:'):
            q = osm_of_map(s.get('poi_mapa'))
            if q:
                d = math.hypot(q['x'] - x, q['z'] - z)
                poi, conf = q['id'], 'alta' if d < 8 else 'media' if d < 15 else 'baja'
            else: poi, conf = None, None
        elif s.get('poi') in marcas:
            poi, conf = 'lev:' + s['poi'], 'alta'
        else:
            # (a sign read in the captures with no entity — a trade's own word, an institution's board, a street plate on a
            # wall —: the nearest OpenStreetMap business of a kind its words name, or a street, or generic)
            t = norm(s['texto'])
            if s['subtipo'] == 'placa' and any(norm(w) == t or norm(w).endswith(t) for w in ways):
                poi, conf = 'via:' + next(w for w in ways if norm(w) == t or norm(w).endswith(t)), 'alta'
            else:
                near = sorted(((math.hypot(q['x'] - x, q['z'] - z), q) for q in pois_osm), key=lambda dq: dq[0])
                hit = next((q for d, q in near if d < 15 and (t and (t in norm(q['name']) or norm(GEN.get(q['tipo_osm'], '')) in t))), None)
                if hit: poi, conf = hit['id'], 'media'
        if not poi:
            motivo = s.get('motivo_generico') or ('número de portal' if re.fullmatch(r'\d+[A-Z]?', s['texto']) else 'señal informativa sin entidad (vado, cruz de farmacia, cartel de obra o de venta)' if s['subtipo'] in ('cartel', 'placa') else 'texto descriptivo de su oficio, sin entidad identificada')
        rows.append({'sign_id': s['sign_id'], 'clave': s['clave'], 'texto': s['texto'], 'poi_id': poi, 'confianza': conf, 'generico': poi is None or s.get('generico', False), 'motivo': motivo})
    json.dump({'version': 1, 'total': len(rows), 'rotulos': rows}, open(os.path.join(D, 'sign_poi_map.json'), 'w'), ensure_ascii=False, indent=1, sort_keys=True)
    sin = [r for r in rows if not r['poi_id'] and not (r['generico'] and r['motivo'])]
    if sin: errs.append(f'R-04: {len(sin)} rótulos sin entidad ni motivo de genérico')
    # ---- R-03's coverage: the businesses inside the area and the signs that name them
    named = {r['poi_id'] for r in rows if r['poi_id']}
    huecos = [{'poi_id': p['id'], 'nombre': p['name'], 'tipo': p['tipo_osm']} for p in pois_osm if p['id'] not in named]
    cob = {'pois_en_el_area': len(pois_osm), 'con_rotulo': len(pois_osm) - len(huecos), 'huecos': huecos,
           'rotulos': len(rows), 'rotulos_con_entidad': sum(1 for r in rows if r['poi_id']), 'rotulos_genericos': sum(1 for r in rows if not r['poi_id']),
           'confianza': {c: sum(1 for r in rows if r['confianza'] == c) for c in ('alta', 'media', 'baja')}}
    json.dump(cob, open(os.path.join(D, 'cobertura.json'), 'w'), ensure_ascii=False, indent=1, sort_keys=True)
    print(json.dumps({k: v for k, v in cob.items() if k != 'huecos'} | {'huecos': len(huecos), 'entidades': len(ents), 'errores': errs[:20]}, ensure_ascii=False))
    return not errs

if __name__ == '__main__':
    if '--descargar' in sys.argv:
        sys.exit('La renovación del extracto (R-12) se hace a mano: ver data/rotulos/overpass.ql y docs/rotulos.md')
    sys.exit(0 if main() else 1)
