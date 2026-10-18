# Shared pieces of the «tiendas_b» family's catalogue (furniture, appliances, computers, bakery, greengrocer, perfumery,
# hairdresser and car workshop): the primitives (the same as catalogo_comercio.py's), the registry of objects with its
# own checks (mass inside the category's range, the class the mass gives, surfaces at the top of a part, nothing under the
# foot), and a few builders (legs, shelving, facings). Imported by catalogo_tiendas_b.py and its tb_<tienda>.py sections.
# Frame of an object: x across, y up from its foot, z out of its front (+z faces whoever uses it; its back at -z).
import json, math, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
OUT = []
IDS = set()
ERRS = []
def fallo(m): ERRS.append(m)

def caja(w, h, d, x=0, y=None, z=0, c='#888888', m='madera', **k):
    return {'f': 'caja', 'd': [round(w, 4), round(h, 4), round(d, 4)], 'p': [round(x, 4), round(h / 2 if y is None else y, 4), round(z, 4)], 'c': c, 'm': m, **k}
def _lados(r, k, por_defecto):
    # (a polygon's box is narrower than its circle unless a vertex lies on each axis: sides in multiples of 4 for what is big)
    sg = k.get('seg') or por_defecto
    if r >= 0.1 and sg % 4: k['seg'] = int(round(sg / 4.0)) * 4 or 4
    return k
def cil(rt, rb, h, x=0, y=None, z=0, c='#888888', m='metal', **k):
    k = _lados(max(rt, rb), k, 12)
    return {'f': 'cil', 'd': [round(rt, 4), round(rb, 4), round(h, 4)], 'p': [round(x, 4), round(h / 2 if y is None else y, 4), round(z, 4)], 'c': c, 'm': m, **k}
def esf(r, x=0, y=0, z=0, c='#888888', m='comida', **k):
    return {'f': 'esfera', 'd': [round(r, 4)], 'p': [round(x, 4), round(y, 4), round(z, 4)], 'c': c, 'm': m, **k}
def cono(r, h, x=0, y=None, z=0, c='#888888', m='metal', **k):
    k = _lados(r, k, 16)
    return {'f': 'cono', 'd': [round(r, 4), round(h, 4)], 'p': [round(x, 4), round(h / 2 if y is None else y, 4), round(z, 4)], 'c': c, 'm': m, **k}
def plano(w, h, x=0, y=0, z=0, tex=None, c='#ffffff', m='papel', **k):
    return {'f': 'plano', 'd': [round(w, 4), round(h, 4)], 'p': [round(x, 4), round(y, 4), round(z, 4)], 'c': c, 'm': m, **({'tex': tex} if tex else {}), **k}

STEEL, DARK, WOOD, WOOD_D, WOOD_L, WHITE, GLASS, CREAM = '#c3c7ca', '#2b2b2e', '#8a5a36', '#5e3b22', '#cfb48a', '#f2f0ea', '#bcd6dc', '#e9e2d2'
SKIN, MIRROR = '#e3d8ca', '#c3d3da'
FIJO = 'anclado en la realidad'

# the categories this family brings (their mass ranges, kg); the rest are the project's own
CATEGORIAS = {
    'tb_mueble_grande': [40, 300], 'tb_colchon_cama': [20, 160], 'tb_audio': [0.3, 12], 'tb_telefono': [0.1, 1.2], 'tb_accesorio': [0.01, 3],
    'tb_obrador': [20, 700], 'tb_saco': [5, 50], 'tb_cosmetico': [0.02, 3], 'tb_camilla': [20, 160], 'tb_peluqueria': [0.04, 120],
    'tb_herramienta': [0.1, 60], 'tb_cajonera': [30, 260], 'tb_neumatico': [6, 25], 'tb_bidon': [10, 230], 'tb_banco_trabajo': [40, 260],
    'tb_vehiculo': [400, 2500], 'tb_elevador': [300, 1800], 'tb_bolleria': [0.02, 6], 'tb_maquina_taller': [20, 400], 'tb_pila_producto': [10, 140], 'tb_pila_neumaticos': [20, 90], 'tb_producto_hogar': [0.1, 30],
}
RANGOS = None
def _rangos():
    global RANGOS
    if RANGOS is None:
        RANGOS = dict(json.load(open(os.path.join(ROOT, 'data', 'mass_ranges.json')))['categorias'])
        RANGOS.update(CATEGORIAS)
        import glob
        for f in glob.glob(os.path.join(ROOT, 'data', 'objetos', '*.json')):
            if f.endswith('tiendas_b.json'): continue
            for c, rg in json.load(open(f)).get('categorias', {}).items(): RANGOS.setdefault(c, rg)
    return RANGOS
def clase_masa(m):
    return 'PICKUP' if m < 5 else 'CARRY' if m < 25 else 'PUSH' if m < 80 else 'PUSH_HEAVY' if m < 400 else 'FIXED'
def oscuro(c, f=0.85):
    r, g, b = (int(c[i:i + 2], 16) for i in (1, 3, 5))
    return '#%02x%02x%02x' % tuple(max(0x2a, min(255, int(v * f))) for v in (r, g, b))
def mezcla(a, b, t):
    ra, rb = [int(a[i:i + 2], 16) for i in (1, 3, 5)], [int(b[i:i + 2], 16) for i in (1, 3, 5)]
    return '#%02x%02x%02x' % tuple(int(x + (y - x) * t) for x, y in zip(ra, rb))
def claro(c, t=0.3): return mezcla(c, '#f2f0ea', t)

def _alto(p):
    d, sc = p['d'], p.get('s', [1, 1, 1])
    f = p['f']
    hw, hh, hd = ((d[0] / 2, d[1] / 2, d[2] / 2) if f == 'caja' else (max(d[0], d[1]), d[2] / 2, max(d[0], d[1])) if f == 'cil' else
                  (d[0], d[0], d[0]) if f == 'esfera' else (d[0], d[1] / 2, d[0]) if f == 'cono' else (d[0] / 2, d[1] / 2, 0.002))
    hw, hh, hd = hw * sc[0], hh * sc[1], hd * sc[2]
    r = p.get('r') or [0, 0, 0]
    if r[0] or r[2]:
        rx, rz = math.radians(r[0]), math.radians(r[2])
        hh = abs(hh * math.cos(rx) * math.cos(rz)) + abs(hd * math.sin(rx)) + abs(hw * math.sin(rz))
    return hh, p['p'][1]
def tris(p):
    f, seg = p['f'], p.get('seg')
    return {'caja': 12, 'cil': 4 * (seg or 12), 'esfera': 2 * 12 * 8, 'cono': 2 * (seg or 14), 'plano': 2}[f]

def obj(id, nombre, categoria, clase, masa, material, soporte, partes, **k):
    """Registers an object. clase None: the one its mass gives (FIXED must be given, with its reason)."""
    if id in IDS: raise SystemExit('id repetido: ' + id)
    IDS.add(id)
    R = _rangos()
    lo, hi = R[categoria]
    if clase is None: clase = clase_masa(masa)
    if not (lo <= masa <= hi) and 'motivo_clase' not in k: fallo(f'{id}: masa {masa} fuera de {categoria} {lo}–{hi}')
    if clase == 'FIXED' and 'motivo_fijo' not in k: k['motivo_fijo'] = FIJO
    if clase != 'FIXED' and clase != clase_masa(masa) and 'motivo_clase' not in k: fallo(f'{id}: clase {clase} con {masa} kg')
    ext = [_alto(p) for p in partes]
    for s in k.get('superficies', []):
        if not any(abs(c + h - s['y']) <= 0.005 for h, c in ext): fallo(f'{id}: superficie y={s["y"]} sin pieza a esa altura')
    if soporte != 'techo' and min(c - h for h, c in ext) < -0.002: fallo(f'{id}: por debajo de su pie ({min(c - h for h, c in ext):.3f})')
    if soporte in ('suelo', 'superficie') and min(c - h for h, c in ext) > 0.0099: fallo(f'{id}: flota {min(c - h for h, c in ext) * 100:.1f} cm sobre su apoyo')
    for p in partes:   # (a polygon's box is narrower than its circle unless a vertex lies on the axis: sides in multiples of 4 for what is big)
        if p['f'] in ('cil', 'cono'):
            r_ = max(p['d'][0], p['d'][1]) if p['f'] == 'cil' else p['d'][0]
            sg = p.get('seg') or (12 if p['f'] == 'cil' else 14)
            if r_ >= 0.1 and sg % 4: fallo(f'{id}: cilindro de radio {r_} con {sg} lados (múltiplo de 4)'); break
    n = sum(tris(p) for p in partes)
    if n > 5000: fallo(f'{id}: {n} triángulos')
    OUT.append({'id': id, 'nombre': nombre, 'categoria': categoria, 'clase': clase, 'masa': masa, 'material': material, 'soporte': soporte, 'partes': partes, **k})

def sup(y, margen=0.04, fondo=None, **k):
    d = {'y': round(y, 4), 'margen': margen}
    if fondo is not None: d['fondo'] = round(fondo, 3)
    d.update(k)
    return d

def patas(w, d, h, c=WOOD_D, inset=0.04, grosor=0.04, y0=0, forma='caja'):
    """Four legs of a table or a piece of furniture: w x d footprint, h tall."""
    P = []
    for sx in (-1, 1):
        for sz in (-1, 1):
            x, z = sx * (w / 2 - inset), sz * (d / 2 - inset)
            P.append(caja(grosor, h, grosor, x=x, y=y0 + h / 2, z=z, c=c) if forma == 'caja' else cil(grosor / 2, grosor / 2 * 0.7, h, x=x, y=y0 + h / 2, z=z, c=c, m='madera', seg=8))
    return P

def estantes(id, nombre, w, d, ys, alto, c='#e6dfd0', cp='#f6f2ea', masa=55, cat='estanteria', soporte='suelo', nota=None, zocalo=True, fondo_panel=True):
    """A shelving unit: two side panels, a back, a plank at each height of ys (their tops are the surfaces), a kick plate."""
    P = [caja(0.02, alto, d, x=-w / 2 + 0.01, z=d / 2, c=c), caja(0.02, alto, d, x=w / 2 - 0.01, z=d / 2, c=c)]
    if fondo_panel: P.append(caja(w - 0.04, alto, 0.012, z=0.006, c=c))
    P += [caja(w - 0.04, 0.025, d, y=y - 0.0125, z=d / 2, c=cp) for y in ys]
    if zocalo: P.append(caja(w - 0.04, 0.1, d - 0.03, y=0.05, z=d / 2, c=oscuro(c, 0.55)))
    obj(id, nombre, cat, 'FIXED', masa, 'madera', soporte, P, motivo_fijo=FIJO, superficies=[sup(y, 0.02, fondo=d - 0.03) for y in ys], **({'nota': nota} if nota else {}))

# ---- products as FACINGS (a row of identical units at the front of a shelf, and a block of the same colour behind: the stock)
def facing(unit, nx, nz, dx, dz, w, h, fondo, c, hf=0.92):
    P = []
    for iz in range(nz):
        for ix in range(nx):
            P += unit((ix - (nx - 1) / 2) * dx, iz * dz)
    zb = -dz / 2
    extra = fondo - (nz * dz)
    if extra > 0.02:
        P.append(caja(nx * dx - 0.004, h * hf, extra, x=0, y=h * hf / 2, z=zb - extra / 2, c=oscuro(c, 0.9), m='comida'))
    return P
def regis(id, nombre, cat, unit, nx, nz, dx, dz, h, fondo, c, mu, mat='comida', hf=0.9, clase=None, nota=None, **k):
    P = facing(unit, nx, nz, dx, dz, nx * dx, h, fondo, c, hf)
    lo, hi = _rangos()[cat]
    masa = round(max(lo, min(nx * (fondo / dz) * mu, 0.9 * hi)), 2)
    obj(id, nombre, cat, clase, masa, mat, 'superficie', P, **({'nota': nota} if nota else {}), **k)
def u_caja(w, h, d, c, c2=None, banda=0.35, m='papel'):
    def f(x, z):
        P = [caja(w, h, d, x=x, y=h / 2, z=z, c=c, m=m)]
        if c2: P.append(caja(w + 0.002, h * banda, d + 0.002, x=x, y=h * 0.62, z=z, c=c2, m=m))
        return P
    return f
def u_lata(r, h, c, c2=None, seg=8):
    def f(x, z):
        P = [cil(r, r, h, x=x, y=h / 2, z=z, c=c, m='metal', seg=seg)]
        if c2: P.append(cil(r + 0.001, r + 0.001, h * 0.55, x=x, y=h * 0.5, z=z, c=c2, m='papel', seg=seg))
        return P
    return f
def u_bote(r, h, c, tapa, seg=8, m='plastico'):
    def f(x, z):
        return [cil(r, r, h * 0.8, x=x, y=h * 0.4, z=z, c=c, m=m, seg=seg), cil(r * 1.03, r * 1.03, h * 0.2, x=x, y=h * 0.9, z=z, c=tapa, m='plastico', seg=seg)]
    return f
def u_botella(r, h, c, etq, tapon, seg=8, m='cristal'):
    def f(x, z):
        return [cil(r, r, h * 0.66, x=x, y=h * 0.33, z=z, c=c, m=m, seg=seg), cil(r + 0.001, r + 0.001, h * 0.3, x=x, y=h * 0.33, z=z, c=etq, m='papel', seg=seg),
                cil(r * 0.42, r * 0.42, h * 0.34, x=x, y=h * 0.83, z=z, c=tapon, m='plastico', seg=seg)]
    return f
def u_tubo(w, h, c, c2):
    def f(x, z):
        return [caja(w, h, w * 0.5, x=x, y=h / 2, z=z, c=c, m='plastico'), caja(w * 0.7, h * 0.12, w * 0.3, x=x, y=h * 0.94, z=z, c=c2, m='plastico')]
    return f

def guardar(familia='tiendas_b'):
    if ERRS:
        print('\n'.join(ERRS)); raise SystemExit(f'{len(ERRS)} errores')
    json.dump({'version': 1, 'familia': familia, 'categorias': CATEGORIAS, 'objetos': OUT}, open(os.path.join(ROOT, 'data', 'objetos', familia + '.json'), 'w'), ensure_ascii=False, indent=1)
    print('objetos de %s: %d' % (familia, len(OUT)))
