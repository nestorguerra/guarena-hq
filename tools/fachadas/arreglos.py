# What the audit of 2026-10-13 found missing or wrong along a street, as seen from one of its captures, and how it is
# put right: tools/fachadas/arreglos/<street>.json (written from the captures by looking, numbers and words only — see
# CORRECCIONES.md in the scratchpad), each item placed from its view's camera (fitted where Google's GPS was off:
# .cache/calles/camaras.json) along its axis, on the street beside it, in the game's metres → src/calles_arreglos.js
#   python3 tools/fachadas/arreglos.py
# Items (all distances in metres along the camera's axis — desde/hasta/en — on the side seen — lado 'izq' | 'der'):
#   {"tipo": "tapia", "vista", "lado", "desde", "hasta", "alto", "material": cal|enfoscado|piedra|ladrillo|seto|verja|malla|celosia, "color", "puerta"?: hex}
#       a wall (or hedge, railing on a low wall, wire fence, lattice) at the back of the pavement where no house stands
#   {"tipo": "arboles", "vista", "lado", "desde", "hasta", "especie": naranjo|platano|morera|olivo|palmera|pino|cipres|frutal|ciruelo|acacia, "cada", "escala"?}
#       trees in the pavement by the kerb, every so many metres
#   {"tipo": "arbol", "vista", "lado", "en", "fondo"?, "especie", "escala"?}   one tree, `fondo` m beyond the kerb (default 0.8)
#   {"tipo": "sin_arboles", "vista", "lado", "desde", "hasta", "fondo"?}   no tree from the kerb to `fondo` m back (default 25)
#   {"tipo": "suelo", "vista", "lado", "desde", "hasta", "fondo", "material": losa|baldosa|tierra|hierba|cesped|asfalto|adoquin|grava, "color"?}
#       the ground from the back of the pavement `fondo` m back (a lot's weeds, a paved forecourt, a garden)
#   {"tipo": "paso", "vista", "en"}   a zebra crossing across the street at that distance
#   {"tipo": "amarillo", "vista", "lado", "desde", "hasta"}   the kerb painted yellow
#   {"tipo": "farola", "vista", "lado", "en", "modelo": pared|columna|baculo|fernandino|globo|seta}
#   {"tipo": "senal", "vista", "lado", "en", "placas": [de arriba abajo, de PLACAS], "mira": camara|espalda|calle, "pared"?: true}
#       a traffic sign on its post by the kerb (or on a bracket on the wall): its face towards the camera, away from it,
#       or across the street
#   {"tipo": "sin_senales", "vista", "lado"?: izq|der|ambos, "desde", "hasta"}   no traffic sign put there by the game
#   {"tipo": "contenedores", "vista", "lado", "en", "tipos": [resto|envases|papel|organico|vidrio, …], "acera"?: true}
#       a set of rubbish containers in the parking lane against the kerb (or on the pavement), centred at `en`
#   {"tipo": "sin_contenedores", "vista", "lado"?: izq|der|ambos, "desde", "hasta"}   none put there by the game
#   {"tipo": "sin_farolas", "vista", "lado"?: izq|der|ambos, "desde", "hasta"}   no street lamp put there by the game
#   {"tipo": "sin_vado_amarillo", "vista", "lado"?: izq|der|ambos, "desde", "hasta"}   garage kerbs there left grey
#   {"tipo": "sin_relleno", "vista", "lado"?: izq|der|ambos, "desde", "hasta"}   no house made up by the game (infill.js)
#       in a gap of the fronts there: the captures show a lot, a yard or a wall
#   {"tipo": "banco", "vista", "lado", "en", "fondo"?, "mira"?: calle|pared}   a bench on the pavement, `fondo` m in from the kerb
#   {"tipo": "bolardos", "vista", "lado", "desde", "hasta", "cada"?}   bollards along the kerb, every `cada` m (1.6)
#   {"tipo": "aparcamiento", "vista", "lado", "desde", "hasta", "modo": cordon|bateria}   cars parked along the kerb
# Any item placed beside the street may instead give "lateral": m — its distance out from the camera's AXIS on its side,
#   straight, wherever the street is (a wall far back in a lot, a sign on an island, a hedge on a median the map lacks)
#   {"tipo": "acera", "vista", "lado", "desde", "hasta", "ancho", "calzada"?}   the pavement on that side that wide (m; 0:
#       none — the carriageway to the fronts, or to the earth of a lot); with calzada, its kerb that far from the street's axis
#   {"tipo": "silos", "vista", "lado", "en", "n", "radio", "alto", "color"?}   metal silos in a row behind the fronts
#   {"tipo": "deposito", "vista", "lado", "en", "alto", "material": ladrillo|hormigon, "color"?}   a water tower
#   {"tipo": "terraza", "vista", "lado", "en", "mesas", "sombrillas"?: hex, "toldo"?: hex, "acera"?: true}   a bar's tables
#       and chairs in the parking lane (or on the pavement), under sunshades or an awning
#   {"tipo": "cable", "vista", "en", "alto"?}   a wire across the street from front to front
#   {"tipo": "relleno", "vista", "lado"?, "desde", "hasta", "color", "plantas"}   the house the game makes up in a gap of
#       the fronts there (infill.js) painted so, with so many storeys
#   {"tipo": "casa", "vista", "lado", "desde", "hasta", "fondo"?, "plantas", "color", "alto"?}   a house the map lacks, on the
#       line of the fronts (or at `lateral` m), `fondo` m deep, wherever no building of the map stands
#   {"tipo": "sin_postes", "vista", "lado"?, "desde", "hasta"}   no wooden power pole of the map's there
#   {"tipo": "banderines", "vista", "en", "alto"?, "colores"?: [hex, …]}   a string of little flags across the street
#   {"tipo": "poste", "vista", "lado", "en", "modelo": madera|hormigon|celosia, "alto"?}   a power pole or a lattice pylon
#   {"tipo": "espejo", "vista", "lado", "en", "mira"?: camara|calle}   a convex traffic mirror on its post
#   {"tipo": "mastil", "vista", "lado", "en", "alto"?, "banderas": [hex, …], "pared"?: true}   a flagpole (on the wall: slanting)
#   {"tipo": "placa", "vista", "lado", "en", "texto", "fondo"?, "letra"?}   a street name plate on the wall
#   {"tipo": "sin_placas", "vista", "lado"?, "desde", "hasta"}   no street name plate put there by the game
#   {"tipo": "escalones", "vista", "lado", "desde", "hasta", "alto", "peldanos"?, "borde"?: hex}   steps (or a raised edge,
#       one step) up from the kerb onto a square, granite, the top one's face painted if `borde`
#   {"tipo": "plaza_azul", "vista", "lado", "en", "largo"?}   a disabled parking bay painted blue in the lane by the kerb
#   {"tipo": "tapa", "vista", "lado"?, "en", "forma": redonda|cuadrada|rejilla, "tam"?, "color"?, "sobre"?: calzada|acera}
#       a manhole cover, a drain grating, a service lid on the road (on its axis, or `lateral` m out) or on the pavement
#   {"tipo": "marca", "vista", "lado"?, "en", "largo", "ancho", "color"?, "sobre"?: calzada|acera}   a little painted mark
#   {"tipo": "banda", "vista", "en", "modelo": detencion|damero|alerta, "fondo"?}   a band painted across the carriageway
#   {"tipo": "semaforo", "vista", "lado", "en", "brazo"?: true}   traffic lights on a post (or on a mast arm over the road)
#   {"tipo": "bajante", "vista", "lado", "en", "alto", "color"?}   a downpipe on the wall there
#   {"tipo": "sierra", "vista", "col_desde", "col_hasta", "alto_px", "distancia"?: km}   hills on the horizon as the
#       capture shows them: from column to column, their crest so many pixels over the horizon
#   {"tipo": "sin_bancos" | "sin_valla_colegio" | "sin_terraza" | "sin_buzon" | "sin_tapias", "vista", "lado"?, "desde", "hasta", "fondo"?}
#   tapia and cable may also go from one point to another: "de": {"en", "lado", "lateral", "alto"?}, "a": {…}
#   {"tipo": "cartel", "vista", "lado", "en", "ancho", "alto", "color", "texto"?, "letra"?, "mira"?: camara|calle|espalda}
#       a billboard on two legs (its foot at the kerb, or `lateral` m out)
import json, math, os, re, glob, sys
REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
M = json.load(open(os.path.join(REPO, 'data', 'map.json')))
P = json.load(open(os.path.join(REPO, '.cache', 'calles', 'poses.json')))
try: C = json.load(open(os.path.join(REPO, '.cache', 'calles', 'camaras.json')))
except Exception: C = {}
HEX = lambda h: h if isinstance(h, str) and re.fullmatch(r'#[0-9a-fA-F]{6}', h) else None

B = [[v / 10 for v in b['p']] for b in M['buildings']]
G, CELL = {}, 20.0
for i, r in enumerate(B):
    xs, zs = r[0::2], r[1::2]
    for gx in range(int(math.floor(min(xs) / CELL)), int(math.floor(max(xs) / CELL)) + 1):
        for gz in range(int(math.floor(min(zs) / CELL)), int(math.floor(max(zs) / CELL)) + 1):
            G.setdefault((gx, gz), []).append(i)
def inside(x, z, r):
    n = len(r) // 2; c = False; j = n - 1
    for i in range(n):
        xi, zi, xj, zj = r[i * 2], r[i * 2 + 1], r[j * 2], r[j * 2 + 1]
        if (zi > z) != (zj > z) and x < (xj - xi) * (z - zi) / (zj - zi + 1e-12) + xi: c = not c
        j = i
    return c
def building_at(x, z):
    return any(inside(x, z, B[i]) for i in G.get((int(math.floor(x / CELL)), int(math.floor(z / CELL))), []))
E = []
for e in M['edges']:
    if e.get('n', -1) < 0 and not e.get('w'): continue
    p = [v / 10 for v in e['p']]
    E.append((list(zip(p[0::2], p[1::2])), e.get('w', 50) / 10, e.get('sw', 10) / 10, e.get('f', 0) / 10))  # (f: between the fronts, where measured)
def nearest(x, z):
    best = None
    for pts, w, sw, fw in E:
        for (ax, az), (bx, bz) in zip(pts, pts[1:]):
            dx, dz = bx - ax, bz - az; L2 = dx * dx + dz * dz or 1e-9
            t = max(0, min(1, ((x - ax) * dx + (z - az) * dz) / L2)); qx, qz = ax + dx * t, az + dz * t
            d = math.hypot(x - qx, z - qz)
            if best is None or d < best[0]: L = math.sqrt(L2); best = (d, qx, qz, dx / L, dz / L, w, sw, fw)
    return best
CAM_ITEM = {}  # (an item measured from an earlier camera of its view carries it: {"camara": {x, z, heading}} — so a
                # camera fitted again later does not move what was placed from the old one)
def cam(v):
    c = dict(P[v]); c.update(C.get(str(v), {}))
    if CAM_ITEM.get(v): c.update(CAM_ITEM[v])
    hd = math.radians(c['heading'])
    return c['x'], c['z'], math.sin(hd), -math.cos(hd), hd
LAT = [None]  # (an item with "lateral": metres out from the camera's axis on its side, wherever the street is — a wall
              # far back in a lot, a sign on an island, a hedge on a median the map has not: placed there, not on the street)
def along(v, side, t):
    """the street beside the view's axis at t m: its nearest point, its direction, the outward normal on that side, w, sw"""
    x, z, fx, fz, hd = cam(v)
    sx, sz = math.cos(hd) * (1 if side == 'der' else -1), math.sin(hd) * (1 if side == 'der' else -1)
    if LAT[0] is not None: return x + fx * t + sx * LAT[0], z + fz * t + sz * LAT[0], fx, fz, sx, sz, 0.0, 0.0, 0.0
    d, qx, qz, ux, uz, w, sw, fw = nearest(x + fx * t, z + fz * t)
    nx, nz = -uz, ux
    if nx * sx + nz * sz < 0: nx, nz = -nx, -nz
    return qx, qz, ux, uz, nx, nz, w, sw, fw
def line(v, side, t0, t1, off, step=1.0, skip_buildings=False):
    """points along the street at `off(w, sw)` m out on that side, from t0 to t1 every `step` m: [x, z, nx, nz]"""
    out, runs, t = [], [], t0
    while t <= t1 + 1e-6:
        qx, qz, ux, uz, nx, nz, w, sw, fw = along(v, side, t)
        o = off(w, sw, fw) if LAT[0] is None else 0.0; px, pz = qx + nx * o, qz + nz * o
        # (never inside a house: brought in towards the carriageway, a hand at a time, up to two metres)
        if not skip_buildings:
            for _ in range(10):
                if not building_at(px, pz): break
                o -= 0.2; px, pz = qx + nx * o, qz + nz * o
        if skip_buildings and (building_at(px, pz) or building_at(px + nx * 0.4, pz + nz * 0.4)):
            if len(out) > 1: runs.append(out)
            out = []
        else: out.append([round(px, 2), round(pz, 2), round(nx, 3), round(nz, 3)])
        t += step
    if len(out) > 1: runs.append(out)
    return runs
# (the street's own measures: where its fronts stand when measured — f, between them — or half the carriageway and a
# pavement out; the kerb no further out than a pavement's width in from the fronts)
house_line = lambda w, sw, fw=0: fw / 2 if fw > w * 0.5 else w / 2 + max(sw, 0.9) + 0.1
def kerb_line(w, sw, fw=0):
    h = house_line(w, sw, fw); k = min(w / 2, h - max(0.9, min(sw, 2.0)))
    return k + min(0.75, (h - k) * 0.45)   # (in the pavement, by the kerb: a tree pit, a lamp post)

out = {'TAPIAS': [], 'ARBOLES': [], 'SIN_ARBOLES': [], 'SUELOS': [], 'PASOS': [], 'AMARILLOS': [], 'FAROLAS': [],
       'ACERAS': [], 'SIN_RELLENO': [], 'SIN_FAROLAS': [], 'SIN_VADO_AMARILLO': [], 'SENALES': [], 'SIN_SENALES': [], 'CONTENEDORES': [], 'SIN_CONTENEDORES': [], 'BANCOS': [], 'BOLARDOS': [], 'APARCAMIENTOS': [],
       'SILOS': [], 'DEPOSITOS': [], 'TERRAZAS': [], 'CABLES': [], 'RELLENOS': [], 'CASAS_NUEVAS': [], 'SIN_POSTES': [],
       'BANDERINES': [], 'POSTES': [], 'ESPEJOS': [], 'MASTILES': [], 'PLACAS_CALLE': [], 'SIN_PLACAS': [], 'CARTELES': [], 'ESCALONES': [], 'PLAZAS_AZULES': [],
       'TAPAS': [], 'MARCAS': [], 'BANDAS': [], 'SEMAFOROS': [], 'BAJANTES': [], 'SIERRAS': [], 'SIN_BANCOS': [], 'SIN_VALLA_COLEGIO': [], 'SIN_TERRAZA': [], 'SIN_BUZON': [], 'SIN_TAPIAS': [], 'SIN_FLORES': []}
# the plates a sign can carry (their names in the game, signs.js)
PLACAS = {'stop': 'stop', 'ceda': 'ceda', 'direccion_prohibida': 'prohibido', 'velocidad_50': 'v50', 'velocidad_30': 'v30',
          'prohibido_estacionar': 'noAparcar', 'prohibido_parar': 'noParar', 'paso_peatones': 'paso', 'peligro_peatones': 'pelPaso',
          'ninos': 'ninos', 'resalto': 'resalto', 'parada_bus': 'bus', 'sentido_obligatorio': 'sentido', 'glorieta': 'glorieta',
          'aparcamiento': 'aparcamiento', 'peligro': 'peligro', 'entrada_poblacion': 'entrada', 'salida_poblacion': 'salida',
          'zona_residencial': 'zonaResidencial', 'prohibido_camiones': 'noCamiones'}
CONT = {'resto': 'v', 'envases': 'a', 'papel': 'z', 'organico': 'm', 'vidrio': 'i'}
kerb_at = lambda w, sw, fw=0: min(w / 2, house_line(w, sw, fw) - 0.9)
def cam_point(v, d):
    """{"en", "lado"?, "lateral"?} from the view's camera: so far ahead along its axis and so far out on that side"""
    x, z, fx, fz, hd = cam(v)
    sgn = 1 if d.get('lado', 'der') == 'der' else -1
    lat = float(d.get('lateral', 0)); t = float(d['en'])
    return x + fx * t + math.cos(hd) * sgn * lat, z + fz * t + math.sin(hd) * sgn * lat
def wall_at(qx, qz, nx, nz, w, sw, fw):
    """how far out from the street's axis the first wall of a building stands there (stepping out from the kerb), a hand
    in front of it — or the line of the fronts if there is none within 4 m past it"""
    o = kerb_at(w, sw, fw)
    while o < house_line(w, sw, fw) + 4:
        if building_at(qx + nx * o, qz + nz * o): return max(0.5, o - 0.05)
        o += 0.05
    return house_line(w, sw, fw) - 0.05
def band(v, sides, t0, t1, past=3.0):
    """the street's band on those sides from t0 to t1: from its axis to `past` m past the fronts (3), a ring each"""
    rings = []
    for sd in sides:
        a = line(v, sd, t0, t1, lambda w, sw, fw=0: 0.0, step=2.0)
        b = line(v, sd, t0, t1, lambda w, sw, fw=0: house_line(w, sw, fw) + past, step=2.0, skip_buildings=False)
        if a and b: rings.append([round(c, 2) for c in [c for p in a[0] for c in p[:2]] + [c for p in reversed(b[0]) for c in p[:2]]])
    return rings
bad = []
# (a file is {"calle": {the street's style touched up — estilos.py merges it}, "items": [...]}, or just the items;
# `--solo FILE` checks one file and writes nothing)
solo = sys.argv[sys.argv.index('--solo') + 1] if '--solo' in sys.argv else None
files = [solo] if solo else sorted(glob.glob(os.path.join(REPO, 'tools', 'fachadas', 'arreglos', '*.json')))
for f in files:
    street = os.path.basename(f)[:-5]
    data = json.load(open(f))
    cz = (data.get('calle') or {}).get('calzadas') if isinstance(data, dict) else None
    if cz is not None:
        try:
            for eid, c in cz.items():
                i = int(eid)
                if not (0 <= i < len(M['edges'])): raise ValueError('arista %s' % eid)
                if 'desplaza' in c and not -8 <= float(c['desplaza']) <= 8: raise ValueError('desplaza -8–8')
                if 'ancho' in c and not 2 <= float(c['ancho']) <= 20: raise ValueError('ancho 2–20')
                if 'acera' in c and not 0 <= float(c['acera']) <= 8: raise ValueError('acera 0–8')
                for q in c.get('puntos', []):
                    if not (isinstance(q, list) and len(q) == 2 and -8 <= float(q[1]) <= 8): raise ValueError('puntos [[s, desplaza -8–8], …]')
        except Exception as e: bad.append(f'{street}: calle.calzadas → {e}')
    for it in (data.get('items', []) if isinstance(data, dict) else data):
        try:
            k, v = it['tipo'], int(it['vista'])
            CAM_ITEM[v] = it.get('camara') if isinstance(it.get('camara'), dict) else None
            LAT[0] = float(it['lateral']) if it.get('lateral') is not None else None
            far = 200 if k in ('silos', 'deposito', 'casa') else 60  # (silos, water towers and houses seen far off the street)
            if LAT[0] is not None and not (0 <= LAT[0] <= far): raise ValueError('lateral %s (0–%d m)' % (LAT[0], far))
            side = it.get('lado', 'der')
            if k == 'tapia' and isinstance(it.get('de'), dict) and isinstance(it.get('a'), dict):
                # (a wall from one point to another, whichever way it runs: {"de": {"en", "lado", "lateral"}, "a": {…}})
                mat = it.get('material', 'cal')
                if mat not in ('cal', 'enfoscado', 'piedra', 'ladrillo', 'seto', 'verja', 'malla', 'celosia'): raise ValueError('material ' + mat)
                (x0, z0), (x1, z1) = cam_point(v, it['de']), cam_point(v, it['a'])
                L = math.hypot(x1 - x0, z1 - z0)
                if not 0.5 <= L <= 120: raise ValueError('de → a: 0,5–120 m')
                nx, nz = (z1 - z0) / L, -(x1 - x0) / L
                cx, cz = cam(v)[:2]
                if (cx - x0) * nx + (cz - z0) * nz > 0: nx, nz = -nx, -nz  # (its back away from the camera)
                n = max(1, round(L))
                pts = [[round(x0 + (x1 - x0) * k / n, 2), round(z0 + (z1 - z0) * k / n, 2), round(nx, 3), round(nz, 3)] for k in range(n + 1)]
                o = {'pts': pts, 'h': round(float(it.get('alto', 2.2)), 2), 'mat': mat, 'col': HEX(it.get('color')) or '#efede6', 'vista': v, 'calle': street}
                if HEX(it.get('puerta')): o['gate'] = HEX(it['puerta'])
                if HEX(it.get('murete')): o['murete'] = HEX(it['murete'])
                out['TAPIAS'].append(o)
            elif k == 'cable' and isinstance(it.get('de'), dict) and isinstance(it.get('a'), dict):
                (x0, z0), (x1, z1) = cam_point(v, it['de']), cam_point(v, it['a'])
                h0, h1 = float(it['de'].get('alto', 6)), float(it['a'].get('alto', 6))
                if not (2 <= h0 <= 40 and 2 <= h1 <= 40): raise ValueError('alto 2–40')
                out['CABLES'].append([round(x0, 2), round(z0, 2), round(x1, 2), round(z1, 2), round(h0, 2), round(h1, 2)])
            elif k == 'tapia':
                mat = it.get('material', 'cal')
                if mat not in ('cal', 'enfoscado', 'piedra', 'ladrillo', 'seto', 'verja', 'malla', 'celosia'): raise ValueError('material ' + mat)
                for r in line(v, side, float(it['desde']), float(it['hasta']), house_line, skip_buildings=True):
                    o = {'pts': r, 'h': round(float(it.get('alto', 2.2)), 2), 'mat': mat, 'col': HEX(it.get('color')) or '#efede6', 'vista': v, 'calle': street}
                    if HEX(it.get('puerta')): o['gate'] = HEX(it['puerta'])
                    if HEX(it.get('murete')): o['murete'] = HEX(it['murete'])
                    out['TAPIAS'].append(o)
            elif k == 'arboles':
                cada = max(2.0, float(it.get('cada', 7)))
                for r in line(v, side, float(it['desde']), float(it['hasta']), kerb_line, step=cada):
                    for p in r: out['ARBOLES'].append([p[0], p[1], it.get('especie', 'naranjo'), round(float(it.get('escala', 1)), 2)])
            elif k == 'arbol':
                qx, qz, ux, uz, nx, nz, w, sw, fw = along(v, side, float(it['en']))
                o = min(w / 2, house_line(w, sw, fw) - 0.9) + float(it.get('fondo', 0.8))
                if LAT[0] is not None: o = 0.0
                out['ARBOLES'].append([round(qx + nx * o, 2), round(qz + nz * o, 2), it.get('especie', 'naranjo'), round(float(it.get('escala', 1)), 2)])
            elif k == 'sin_arboles' and isinstance(it.get('de'), dict) and isinstance(it.get('a'), dict):
                # (a patch from one point to another, `ancho` m wide: a tree of a median the street's band does not reach)
                (x0, z0), (x1, z1) = cam_point(v, it['de']), cam_point(v, it['a'])
                L = math.hypot(x1 - x0, z1 - z0); hw = float(it.get('ancho', 4)) / 2
                if not (0.5 <= L <= 80 and 0.5 <= hw <= 20): raise ValueError('de → a: 0,5–80 m, ancho 1–40')
                nx, nz = (z1 - z0) / L, -(x1 - x0) / L
                out['SIN_ARBOLES'].append([round(c, 2) for c in (x0 + nx * hw, z0 + nz * hw, x1 + nx * hw, z1 + nz * hw, x1 - nx * hw, z1 - nz * hw, x0 - nx * hw, z0 - nz * hw)])
            elif k == 'sin_arboles':
                fondo = float(it.get('fondo', 25))
                ring = []
                a = line(v, side, float(it['desde']), float(it['hasta']), lambda w, sw, fw=0: w / 2 - 0.5, step=2.0)
                b = line(v, side, float(it['desde']), float(it['hasta']), lambda w, sw, fw=0: w / 2 + fondo, step=2.0)
                if a and b:
                    ring = [c for p in a[0] for c in p[:2]] + [c for p in reversed(b[0]) for c in p[:2]]
                    out['SIN_ARBOLES'].append([round(c, 2) for c in ring])
            elif k == 'suelo':
                mat = it.get('material', 'tierra')
                if mat not in ('losa', 'baldosa', 'tierra', 'hierba', 'cesped', 'asfalto', 'adoquin', 'grava'): raise ValueError('material ' + mat)
                fondo = float(it.get('fondo', 10))
                a = line(v, side, float(it['desde']), float(it['hasta']), house_line, step=2.0)
                b = line(v, side, float(it['desde']), float(it['hasta']), lambda w, sw, fw=0: house_line(w, sw, fw) + fondo, step=2.0)
                if a and b:
                    ring = [c for p in a[0] for c in p[:2]] + [c for p in reversed(b[0]) for c in p[:2]]
                    out['SUELOS'].append({'ring': [round(c, 2) for c in ring], 'mat': mat, 'col': HEX(it.get('color'))})
            elif k == 'paso':
                qx, qz, ux, uz, nx, nz, w, sw, fw = along(v, 'der', float(it['en']))
                out['PASOS'].append([round(qx, 2), round(qz, 2), round(ux, 3), round(uz, 3)])
            elif k == 'amarillo':
                for r in line(v, side, float(it['desde']), float(it['hasta']), lambda w, sw, fw=0: min(w / 2, house_line(w, sw, fw) - 0.9)):
                    out['AMARILLOS'].append([c for p in r for c in p[:2]])
            elif k == 'farola':
                qx, qz, ux, uz, nx, nz, w, sw, fw = along(v, side, float(it['en']))
                model = it.get('modelo', 'columna')
                if model not in ('pared', 'columna', 'baculo', 'fernandino', 'globo', 'seta', 'doble'): raise ValueError('modelo ' + str(model))
                o = house_line(w, sw, fw) - 0.05 if model in ('pared', 'fernandino') else kerb_line(w, sw, fw)
                if LAT[0] is not None: o = 0.0
                out['FAROLAS'].append([round(qx + nx * o, 2), round(qz + nz * o, 2), round(-nx, 3), round(-nz, 3), model])
            elif k == 'senal':
                qx, qz, ux, uz, nx, nz, w, sw, fw = along(v, side, float(it['en']))
                pl = [PLACAS.get(q) for q in it.get('placas', [])]
                if not pl or None in pl: raise ValueError('placas %s (valen: %s)' % (it.get('placas'), ', '.join(PLACAS)))
                fx, fz = cam(v)[2:4]
                if ux * fx + uz * fz < 0: ux, uz = -ux, -uz
                d = {'camara': (-ux, -uz), 'espalda': (ux, uz), 'calle': (-nx, -nz)}.get(it.get('mira', 'camara'))
                if d is None: raise ValueError('mira ' + str(it.get('mira')))
                wall = bool(it.get('pared'))
                o = house_line(w, sw, fw) - 0.05 if wall else kerb_line(w, sw, fw)
                if LAT[0] is not None: o = 0.0
                out['SENALES'].append([round(qx + nx * o, 2), round(qz + nz * o, 2), round(math.atan2(d[0], d[1]), 3), pl] + ([round(-nx, 3), round(-nz, 3)] if wall else [0, 0]))
            elif k in ('sin_senales', 'sin_contenedores', 'sin_relleno', 'sin_farolas', 'sin_vado_amarillo', 'sin_postes', 'sin_placas', 'sin_bancos', 'sin_valla_colegio', 'sin_terraza', 'sin_buzon', 'sin_tapias', 'sin_flores'):
                sides = ['izq', 'der'] if it.get('lado', 'ambos') == 'ambos' else [side]
                out[{'sin_senales': 'SIN_SENALES', 'sin_contenedores': 'SIN_CONTENEDORES', 'sin_relleno': 'SIN_RELLENO', 'sin_farolas': 'SIN_FAROLAS', 'sin_vado_amarillo': 'SIN_VADO_AMARILLO', 'sin_postes': 'SIN_POSTES', 'sin_placas': 'SIN_PLACAS', 'sin_bancos': 'SIN_BANCOS', 'sin_valla_colegio': 'SIN_VALLA_COLEGIO', 'sin_terraza': 'SIN_TERRAZA', 'sin_buzon': 'SIN_BUZON', 'sin_tapias': 'SIN_TAPIAS', 'sin_flores': 'SIN_FLORES'}[k]] += band(v, sides, float(it['desde']), float(it['hasta']), min(200.0, max(3.0, float(it.get('fondo', 3)))))  # (fondo: m past the fronts it reaches, for what stands far off)
            elif k == 'contenedores':
                qx, qz, ux, uz, nx, nz, w, sw, fw = along(v, side, float(it['en']))
                kinds = ''.join(CONT[t] for t in it.get('tipos', ['resto', 'envases', 'papel', 'organico']))
                if not kinds.replace('i', ''): raise ValueError('tipos: al menos un contenedor')
                o = kerb_at(w, sw, fw) + (0.9 if it.get('acera') else -0.82)
                if LAT[0] is not None: o = 0.0
                out['CONTENEDORES'].append([round(qx + nx * o, 2), round(qz + nz * o, 2), round(ux, 3), round(uz, 3), kinds])
            elif k == 'banco':
                qx, qz, ux, uz, nx, nz, w, sw, fw = along(v, side, float(it['en']))
                o = kerb_at(w, sw, fw) + float(it.get('fondo', 0.7))
                if LAT[0] is not None: o = 0.0
                d = (-nx, -nz) if it.get('mira', 'calle') == 'calle' else (nx, nz)
                out['BANCOS'].append([round(qx + nx * o, 2), round(qz + nz * o, 2), round(math.atan2(d[0], d[1]), 3)])
            elif k == 'bolardos':
                cada = max(0.8, float(it.get('cada', 1.6)))
                for r in line(v, side, float(it['desde']), float(it['hasta']), lambda w, sw, fw=0: kerb_at(w, sw, fw) + 0.3, step=cada):
                    out['BOLARDOS'] += [[p[0], p[1]] for p in r]
            elif k == 'acera':
                ancho = float(it['ancho'])
                if not 0 <= ancho <= 8: raise ValueError('ancho %s' % ancho)
                cz = it.get('calzada')  # (the kerb this far from the street's axis, m: the carriageway as wide as seen there)
                if cz is not None and not 1.2 <= float(cz) <= 12: raise ValueError('calzada 1.2–12')
                for r in line(v, side, float(it['desde']), float(it['hasta']), lambda w, sw, fw=0: kerb_at(w, sw, fw), step=1.0):
                    o = {'pts': [c for p in r for c in p[:2]], 'ancho': round(ancho, 2)}
                    if cz is not None: o['calzada'] = round(float(cz), 2)
                    out['ACERAS'].append(o)
            elif k == 'aparcamiento':
                modo = it.get('modo', 'cordon')
                if modo not in ('cordon', 'bateria'): raise ValueError('modo ' + modo)
                for r in line(v, side, float(it['desde']), float(it['hasta']), lambda w, sw, fw=0: kerb_at(w, sw, fw) - (1.05 if modo == 'cordon' else 2.4)):
                    out['APARCAMIENTOS'].append({'pts': [c for p in r for c in p[:2]], 'n': [r[0][2], r[0][3]], 'modo': modo})
            elif k == 'silos':
                qx, qz, ux, uz, nx, nz, w, sw, fw = along(v, side, float(it['en']))
                n, rad, h = int(it.get('n', 1)), float(it.get('radio', 2.5)), float(it.get('alto', 12))
                if not (1 <= n <= 6 and 0.4 <= rad <= 6 and 4 <= h <= 40): raise ValueError('n 1–6, radio 0,4–6, alto 4–40')
                o = house_line(w, sw, fw) + rad + 1.5 if LAT[0] is None else 0.0
                fx, fz = cam(v)[2:4]
                if ux * fx + uz * fz < 0: ux, uz = -ux, -uz
                for j in range(n):
                    a = (j - (n - 1) / 2) * rad * 2.15
                    out['SILOS'].append([round(qx + nx * o + ux * a, 2), round(qz + nz * o + uz * a, 2), round(rad, 2), round(h, 2), HEX(it.get('color')) or '#c9ccce'])
            elif k == 'deposito':
                qx, qz, ux, uz, nx, nz, w, sw, fw = along(v, side, float(it['en']))
                h = float(it.get('alto', 18)); mat = it.get('material', 'ladrillo')
                if not 8 <= h <= 40: raise ValueError('alto 8–40')
                if mat not in ('ladrillo', 'hormigon'): raise ValueError('material ' + mat)
                o = house_line(w, sw, fw) + 4 if LAT[0] is None else 0.0
                out['DEPOSITOS'].append([round(qx + nx * o, 2), round(qz + nz * o, 2), round(h, 2), mat, HEX(it.get('color')) or ('#b0624a' if mat == 'ladrillo' else '#cfccc4')])
            elif k == 'terraza':
                qx, qz, ux, uz, nx, nz, w, sw, fw = along(v, side, float(it['en']))
                m = int(it.get('mesas', 4))
                if not 1 <= m <= 12: raise ValueError('mesas 1–12')
                o = kerb_at(w, sw, fw) + (1.0 if it.get('acera') else -1.1)
                if LAT[0] is not None: o = 0.0
                out['TERRAZAS'].append([round(qx + nx * o, 2), round(qz + nz * o, 2), round(ux, 3), round(uz, 3), round(nx, 3), round(nz, 3), m, HEX(it.get('sombrillas')), HEX(it.get('toldo')), 1 if it.get('acera') else 0])
            elif k == 'cable' and it.get('desde') is None:
                qx, qz, ux, uz, nx, nz, w, sw, fw = along(v, 'der', float(it['en']))
                hl = house_line(w, sw, fw); h = float(it.get('alto', 5.5))
                if not 3 <= h <= 12: raise ValueError('alto 3–12')
                out['CABLES'].append([round(qx - nx * hl, 2), round(qz - nz * hl, 2), round(qx + nx * hl, 2), round(qz + nz * hl, 2), round(h, 2)])
            elif k == 'relleno':
                if not HEX(it.get('color')): raise ValueError('color #hex')
                pl = int(it.get('plantas', 2))
                if not 1 <= pl <= 4: raise ValueError('plantas 1–4')
                sides = ['izq', 'der'] if it.get('lado', 'ambos') == 'ambos' else [side]
                for ring in band(v, sides, float(it['desde']), float(it['hasta'])):
                    out['RELLENOS'].append({'ring': ring, 'wall': HEX(it['color']), 'floors': pl})
            elif k == 'casa':
                pl, fondo, colr = int(it.get('plantas', 2)), float(it.get('fondo', 10)), HEX(it.get('color'))
                if not (1 <= pl <= 8 and 3 <= fondo <= 40 and colr): raise ValueError('plantas 1–8, fondo 3–40, color #hex')
                alto = it.get('alto')
                if alto is not None and not 2.2 <= float(alto) <= 30: raise ValueError('alto 2.2–30')
                if isinstance(it.get('de'), dict) and isinstance(it.get('a'), dict):
                    # (a small building standing free, from one point to another of its front as seen — a transformer's hut
                    # on a square —, its depth away from the camera)
                    (x0, z0), (x1, z1) = cam_point(v, it['de']), cam_point(v, it['a'])
                    L = math.hypot(x1 - x0, z1 - z0)
                    if not 1.5 <= L <= 60: raise ValueError('de → a: 1,5–60 m')
                    nx, nz = (z1 - z0) / L, -(x1 - x0) / L
                    cx, cz = cam(v)[:2]
                    if (cx - x0) * nx + (cz - z0) * nz > 0: nx, nz = -nx, -nz
                    ring = [x0, z0, x1, z1, x1 + nx * fondo, z1 + nz * fondo, x0 + nx * fondo, z0 + nz * fondo]
                    n2 = 4; a2 = sum(ring[i * 2] * ring[((i + 1) % n2) * 2 + 1] - ring[((i + 1) % n2) * 2] * ring[i * 2 + 1] for i in range(n2))
                    if a2 < 0: ring = [c for i in reversed(range(n2)) for c in ring[i * 2:i * 2 + 2]]
                    o = {'ring': [round(c, 2) for c in ring], 'floors': pl, 'wall': colr}
                    if alto is not None: o['alto'] = round(float(alto), 2)
                    out['CASAS_NUEVAS'].append(o)
                    continue
                runs = line(v, side, float(it['desde']), float(it['hasta']), house_line, step=1.5, skip_buildings=True)
                if not runs: raise ValueError('ahí ya hay edificios del mapa en todo el tramo')
                for r in runs:
                    if len(r) < 2: continue
                    ring = [c for q in r for c in q[:2]] + [c for q in reversed(r) for c in (q[0] + q[2] * fondo, q[1] + q[3] * fondo)]
                    n2 = len(ring) // 2
                    a2 = sum(ring[i * 2] * ring[((i + 1) % n2) * 2 + 1] - ring[((i + 1) % n2) * 2] * ring[i * 2 + 1] for i in range(n2))
                    if a2 < 0: ring = [c for i in reversed(range(n2)) for c in ring[i * 2:i * 2 + 2]]  # (as the map's: counter-clockwise)
                    o = {'ring': [round(c, 2) for c in ring], 'floors': pl, 'wall': colr}
                    if alto is not None: o['alto'] = round(float(alto), 2)
                    out['CASAS_NUEVAS'].append(o)
            elif k in ('banderines', 'cable') and it.get('desde') is not None:
                # (along the street, desde → hasta, over its axis — or `lateral` m out on its side, or over the kerb with
                # `lado` alone — at its height, a hook every 12 m)
                h = float(it.get('alto', 6 if k == 'banderines' else 5.5))
                if not 3 <= h <= 14: raise ValueError('alto 3–14')
                off = (lambda w, sw, fw=0: kerb_at(w, sw, fw)) if it.get('lado') and LAT[0] is None else (lambda w, sw, fw=0: 0.0)
                for r in line(v, side, float(it['desde']), float(it['hasta']), off, step=12.0, skip_buildings=False):
                    for p0, p1 in zip(r, r[1:]):
                        if k == 'cable': out['CABLES'].append([p0[0], p0[1], p1[0], p1[1], round(h, 2)])
                        else:
                            cols = [HEX(c) for c in it.get('colores', ['#c8202a', '#f2c230'])]
                            if not cols or None in cols: raise ValueError('colores: lista de #hex')
                            out['BANDERINES'].append([p0[0], p0[1], p1[0], p1[1], round(h, 2), cols])
            elif k == 'banderines':
                qx, qz, ux, uz, nx, nz, w, sw, fw = along(v, 'der', float(it['en']))
                hl = house_line(w, sw, fw); h = float(it.get('alto', 6))
                if not 3 <= h <= 12: raise ValueError('alto 3–12')
                cols = [HEX(c) for c in it.get('colores', ['#c8202a', '#f2c230'])]
                if not cols or None in cols: raise ValueError('colores: lista de #hex')
                out['BANDERINES'].append([round(qx - nx * hl, 2), round(qz - nz * hl, 2), round(qx + nx * hl, 2), round(qz + nz * hl, 2), round(h, 2), cols])
            elif k in ('poste', 'espejo', 'mastil', 'cartel'):
                qx, qz, ux, uz, nx, nz, w, sw, fw = along(v, side, float(it['en']))
                wall = k == 'mastil' and bool(it.get('pared'))
                o = wall_at(qx, qz, nx, nz, w, sw, fw) if wall else kerb_line(w, sw, fw)
                if LAT[0] is not None: o = 0.0
                x, z = round(qx + nx * o, 2), round(qz + nz * o, 2)
                fx, fz = cam(v)[2:4]
                if ux * fx + uz * fz < 0: ux, uz = -ux, -uz
                face = {'camara': (-ux, -uz), 'espalda': (ux, uz), 'calle': (-nx, -nz)}.get(it.get('mira', 'camara'))
                if face is None: raise ValueError('mira ' + str(it.get('mira')))
                yaw = round(math.atan2(face[0], face[1]), 3)
                if k == 'poste':
                    mod = it.get('modelo', 'madera')
                    if mod not in ('madera', 'hormigon', 'celosia'): raise ValueError('modelo ' + str(mod))
                    h = float(it.get('alto', 22 if mod == 'celosia' else 8.5))
                    if not 4 <= h <= 40: raise ValueError('alto 4–40')
                    out['POSTES'].append([x, z, mod, round(h, 2)])
                elif k == 'espejo':
                    out['ESPEJOS'].append([x, z, yaw])
                elif k == 'mastil':
                    fl = [HEX(c) for c in it.get('banderas', ['#c8202a'])]
                    if not fl or None in fl: raise ValueError('banderas: lista de #hex')
                    out['MASTILES'].append([x, z, round(-nx, 3), round(-nz, 3), round(float(it.get('alto', 3.5 if wall else 8)), 2), fl, 1 if wall else 0])
                else:
                    cw, ch, colr = float(it['ancho']), float(it['alto']), HEX(it.get('color'))
                    if not (0.5 <= cw <= 15 and 0.4 <= ch <= 8 and colr): raise ValueError('ancho 0.5–15, alto 0.4–8, color #hex')
                    out['CARTELES'].append([x, z, yaw, round(cw, 2), round(ch, 2), round(float(it.get('suelo', 2.2)), 2), colr, str(it.get('texto') or '')[:40], HEX(it.get('letra')) or '#1e1e1e'])
            elif k == 'placa':
                qx, qz, ux, uz, nx, nz, w, sw, fw = along(v, side, float(it['en']))
                o = wall_at(qx, qz, nx, nz, w, sw, fw) + 0.01
                if LAT[0] is not None: o = 0.0
                # (no plate without words — backlog R-06: one whose words do not read in its capture takes its street's name)
                if not str(it.get('texto') or '').strip(): raise ValueError('placa sin texto: pon el nombre de su calle')
                out['PLACAS_CALLE'].append([round(qx + nx * o, 2), round(qz + nz * o, 2), round(-nx, 3), round(-nz, 3), str(it.get('texto'))[:40], HEX(it.get('fondo')) or '#f4f1ea', HEX(it.get('letra')) or '#1f3f7a'])
            elif k == 'escalones':
                h, n = float(it['alto']), int(it.get('peldanos', 1))
                if not (0.08 <= h <= 2 and 1 <= n <= 10): raise ValueError('alto 0.08–2, peldanos 1–10')
                for r in line(v, side, float(it['desde']), float(it['hasta']), lambda w, sw, fw=0: kerb_at(w, sw, fw) + 0.05, step=1.0):
                    out['ESCALONES'].append({'pts': [c for p in r for c in p], 'alto': round(h, 2), 'n': n, 'borde': HEX(it.get('borde'))})
            elif k == 'plaza_azul':
                qx, qz, ux, uz, nx, nz, w, sw, fw = along(v, side, float(it['en']))
                o = kerb_at(w, sw, fw) - 1.15
                if LAT[0] is not None: o = 0.0
                out['PLAZAS_AZULES'].append([round(qx + nx * o, 2), round(qz + nz * o, 2), round(ux, 3), round(uz, 3), round(float(it.get('largo', 5)), 2)])
            elif k in ('tapa', 'marca'):
                qx, qz, ux, uz, nx, nz, w, sw, fw = along(v, side, float(it['en']))
                on_pave = it.get('sobre', 'calzada') == 'acera'
                o = (kerb_at(w, sw, fw) + 0.8) if on_pave else (float(it.get('lateral')) if it.get('lateral') is not None else 0.0)
                if LAT[0] is not None: o = 0.0
                x, z = round(qx + nx * o, 2), round(qz + nz * o, 2)
                if k == 'tapa':
                    f = it.get('forma', 'redonda')
                    if f not in ('redonda', 'cuadrada', 'rejilla'): raise ValueError('forma ' + str(f))
                    t = float(it.get('tam', 0.6 if f != 'rejilla' else 0.5))
                    if not 0.2 <= t <= 2: raise ValueError('tam 0.2–2')
                    out['TAPAS'].append([x, z, round(ux, 3), round(uz, 3), f, round(t, 2), HEX(it.get('color')) or ('#3a3532' if f != 'cuadrada' else '#5d5853'), 1 if on_pave else 0])
                else:
                    L, W = float(it['largo']), float(it['ancho'])
                    if not (0.1 <= L <= 12 and 0.05 <= W <= 4): raise ValueError('largo 0.1–12, ancho 0.05–4')
                    out['MARCAS'].append([x, z, round(ux, 3), round(uz, 3), round(L, 2), round(W, 2), HEX(it.get('color')) or '#f2f2ee', 1 if on_pave else 0])
            elif k == 'banda':
                qx, qz, ux, uz, nx, nz, w, sw, fw = along(v, 'der', float(it['en']))
                mod = it.get('modelo', 'detencion')
                if mod not in ('detencion', 'damero', 'alerta'): raise ValueError('modelo ' + str(mod))
                out['BANDAS'].append([round(qx, 2), round(qz, 2), round(ux, 3), round(uz, 3), round(w, 2), mod, round(float(it.get('fondo', 0.4 if mod == 'detencion' else 1.2)), 2)])
            elif k == 'semaforo':
                qx, qz, ux, uz, nx, nz, w, sw, fw = along(v, side, float(it['en']))
                o = kerb_line(w, sw, fw) if LAT[0] is None else 0.0
                fx, fz = cam(v)[2:4]
                if ux * fx + uz * fz < 0: ux, uz = -ux, -uz
                out['SEMAFOROS'].append([round(qx + nx * o, 2), round(qz + nz * o, 2), round(-nx, 3), round(-nz, 3), round(math.atan2(-ux, -uz), 3), 1 if it.get('brazo') else 0])
            elif k == 'bajante':
                qx, qz, ux, uz, nx, nz, w, sw, fw = along(v, side, float(it['en']))
                o = wall_at(qx, qz, nx, nz, w, sw, fw) if LAT[0] is None else 0.0
                h = float(it.get('alto', 6))
                if not 2 <= h <= 30: raise ValueError('alto 2–30')
                out['BAJANTES'].append([round(qx + nx * (o - 0.07), 2), round(qz + nz * (o - 0.07), 2), round(h, 2), HEX(it.get('color')) or '#8e9092'])
            elif k == 'sierra':
                x, z, fx, fz, hd = cam(v)
                c0, c1, apx = float(it['col_desde']), float(it['col_hasta']), float(it['alto_px'])
                if not (0 <= c0 < c1 <= 1440 and 2 <= apx <= 150): raise ValueError('col_desde < col_hasta en 0–1440, alto_px 2–150')
                fov = math.radians(float(P[v].get('fov', 90))); F = (693 / 2) / math.tan(fov / 2)
                D = float(it.get('distancia', 8)) * 1000
                if not 1000 <= D <= 40000: raise ValueError('distancia 1–40 km')
                az = lambda col: hd + math.atan2(col + 0.5 - 720, F)
                out['SIERRAS'].append([round(x, 1), round(z, 1), round(az(c0), 4), round(az(c1), 4), round(D, 0), round(apx / F * D, 1), v])
            else: raise ValueError('tipo ' + k)
        except Exception as e:
            bad.append(f'{street}: {it} → {e}')
# (no wall ever closes a street: one measured far out from its camera that cuts across a street's axis — square to it,
# away from its ends, where a dead end's wall would stand — loses the stretch over that carriageway and its kerbs.
# Not a hedge: the medians' hedges run up to their crossings, where the map's wide junctions reach them)
def _cross(a, b, c, d):
    r = (b[0] - a[0]) * (d[1] - c[1]) - (b[1] - a[1]) * (d[0] - c[0])
    if abs(r) < 1e-9: return None
    t = ((c[0] - a[0]) * (d[1] - c[1]) - (c[1] - a[1]) * (d[0] - c[0])) / r
    u = ((c[0] - a[0]) * (b[1] - a[1]) - (c[1] - a[1]) * (b[0] - a[0])) / r
    return (t, u) if 0 <= t <= 1 and 0 <= u <= 1 else None
def _dist(p, pts):
    best = 1e9
    for (ax, az), (bx, bz) in zip(pts, pts[1:]):
        dx, dz = bx - ax, bz - az; L2 = dx * dx + dz * dz or 1e-9
        t = max(0, min(1, ((p[0] - ax) * dx + (p[1] - az) * dz) / L2))
        best = min(best, math.hypot(p[0] - ax - dx * t, p[1] - az - dz * t))
    return best
cut, keep = 0, []
for o in out['TAPIAS']:
    if o['mat'] == 'seto': keep.append(o); continue
    P = o['pts']; drop = set()
    xs, zs = [p[0] for p in P], [p[1] for p in P]
    for pts, w, sw, fw in E:
        if max(x for x, _ in pts) < min(xs) - 1 or min(x for x, _ in pts) > max(xs) + 1 or max(z for _, z in pts) < min(zs) - 1 or min(z for _, z in pts) > max(zs) + 1: continue
        seg = list(zip(pts, pts[1:])); tot = sum(math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in seg); s0 = 0.0; hit = False
        for a, b in seg:
            La = math.hypot(b[0] - a[0], b[1] - a[1])
            for p, q in zip(P, P[1:]):
                r = _cross(p, q, a, b)
                if not r: continue
                s = s0 + r[1] * La; Lw = math.hypot(q[0] - p[0], q[1] - p[1]) or 1e-9
                sin = abs((q[0] - p[0]) * (b[1] - a[1]) - (q[1] - p[1]) * (b[0] - a[0])) / (Lw * (La or 1e-9))
                if 3 < s < tot - 3 and sin > 0.5: hit = True
            s0 += La
        if hit:
            for i, p in enumerate(P):
                if _dist(p, pts) < w / 2 + max(sw, 0.9) * 0.5 + 0.3: drop.add(i)
    if not drop: keep.append(o); continue
    cut += 1; print('tapia que cerraba una calle, recortada:', o['calle'], 'vista', o['vista'], '%d/%d puntos' % (len(drop), len(P)))
    run = []
    for i, p in enumerate(P + [None]):
        if p is not None and i not in drop: run.append(p); continue
        if len(run) > 1: keep.append(dict(o, pts=run))
        run = []
out['TAPIAS'] = keep
js = ["// What the audit of 2026-10-13 found missing or wrong along the streets, put right from their captures — written by",
      "// tools/fachadas/arreglos.py from tools/fachadas/arreglos/*.json (numbers and words only). In the game's metres.",
      "// TAPIAS: walls, hedges, railings, fences (tapias.js) · ARBOLES: [x, z, species, scale] · SIN_ARBOLES: rings where no",
      "// tree grows · SUELOS: {ring, mat, col} · PASOS: [x, z, dx, dz] · AMARILLOS: polylines of kerb painted yellow ·",
      "// FAROLAS: [x, z, nx, nz (towards the street), model] · SENALES: [x, z, face yaw, plates, wall nx, nz (0, 0: a post)] ·",
      "// SIN_SENALES, SIN_CONTENEDORES: rings where the game puts none · CONTENEDORES: [x, z, ux, uz (along the row), kinds",
      "// v a z m i] · BANCOS: [x, z, yaw] · BOLARDOS: [x, z] · APARCAMIENTOS: {pts, n (out to the kerb), modo} ·",
      "// ACERAS: {pts (a side's kerb line), ancho (m of pavement; 0 none)} · SIN_RELLENO: rings where no house is made up ·",
      "// SILOS: [x, z, radius, height, colour] · DEPOSITOS: [x, z, height, material, colour] · TERRAZAS: [x, z, ux, uz, nx, nz",
      "// (out to the fronts), tables, sunshade colour|null, awning colour|null, on the pavement 1|0] · CABLES: [x0, z0, x1, z1,",
      "// height] · RELLENOS: {ring, wall, floors} · CASAS_NUEVAS: {ring, floors, wall, alto?} · SIN_POSTES, SIN_PLACAS: rings ·",
      "// BANDERINES: [x0, z0, x1, z1, height, colours] · POSTES: [x, z, model, height] · ESPEJOS: [x, z, yaw] · MASTILES: [x, z,",
      "// nx, nz (out from the wall), height, flags, on the wall 1|0] · PLACAS_CALLE: [x, z, nx, nz, text, ground, letters] ·",
      "// CARTELES: [x, z, yaw, width, height, its foot's clearance, colour, text, letters] · ESCALONES: {pts [x, z, nx, nz],",
      "// alto, n, borde} · PLAZAS_AZULES: [x, z, ux, uz, length] · TAPAS: [x, z, ux, uz, shape, size, colour, on the pavement]",
      "// · MARCAS: [x, z, ux, uz, length, width, colour, on the pavement] · BANDAS: [x, z, ux, uz, road width, model, depth] ·",
      "// SEMAFOROS: [x, z, nx, nz (to the road), facing yaw, on an arm] · BAJANTES: [x, z, height, colour] · SIERRAS: [camera x,",
      "// z, from azimuth, to azimuth, distance, crest height, view] · SIN_BANCOS, SIN_VALLA_COLEGIO, SIN_TERRAZA, SIN_BUZON: rings"]
for k, v in out.items():
    js.append(f'export const {k} = [')
    for o in v: js.append('  ' + json.dumps(o, ensure_ascii=False) + ',')
    js.append('];')
if not solo: open(os.path.join(REPO, 'src', 'calles_arreglos.js'), 'w').write('\n'.join(js) + '\n')
print({k: len(v) for k, v in out.items()})
for b in bad[:40]: print('ERROR', b)
print('errores', len(bad))
