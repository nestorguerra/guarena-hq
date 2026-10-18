# The objects of the «tiendas_a» family (technical backlog, I-02 and X-01/X-02): seven small-town Spanish shops — the
# «todo a cien» variety store, the hardware shop, the bookshop, the toyshop, the florist, the «estanco» (tobacco, lottery
# and press) and the jeweller-watchmaker / optician. Each object is a few primitives (boxes, cylinders, spheres, cones
# and textured planes, in metres), its class of interaction, its mass, its material and what it stands on. The script is
# the model: it writes data/objetos/tiendas_a.json. Frame of an object: x across, y up from its foot, z out of its front
# (+z faces whoever uses it; its back at -z). Products are FACINGS: a row of identical units at the front of a shelf and a
# solid block of the same colour behind (the stock), so that a shelf looks full with few pieces; books are rows of spines.
# No real brand anywhere: invented names, plain colours. Objects that already exist in the families hostelería, comercio
# and servicios are reused by id from the kits (kits_tiendas_a.py), never redefined here.
#   python3 tools/interiores/catalogo_tiendas_a.py
import json, math, os, random
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
OUT = []

def caja(w, h, d, x=0, y=None, z=0, c='#888888', m='madera', **k):
    return {'f': 'caja', 'd': [w, h, d], 'p': [x, h / 2 if y is None else y, z], 'c': c, 'm': m, **k}
def _seg(k, defecto=None):
    """Sides of a round part, always a multiple of 4: then its true extent is its radius on every side (the validator measures
    a cylinder as the square round it; with 5, 7, 10 sides the polygon is narrower and neighbours can look 1 cm too close)."""
    s = k.pop('seg', None) or defecto
    if s: k['seg'] = 4 * math.ceil(s / 4)
    return k
def cil(rt, rb, h, x=0, y=None, z=0, c='#888888', m='metal', **k):
    return {'f': 'cil', 'd': [rt, rb, h], 'p': [x, h / 2 if y is None else y, z], 'c': c, 'm': m, **_seg(k)}
def esf(r, x=0, y=0, z=0, c='#888888', m='comida', **k):
    return {'f': 'esfera', 'd': [r], 'p': [x, y, z], 'c': c, 'm': m, **k}
def cono(radio, h, x=0, y=None, z=0, c='#888888', m='metal', **k):
    return {'f': 'cono', 'd': [radio, h], 'p': [x, h / 2 if y is None else y, z], 'c': c, 'm': m, **_seg(k, 8)}
def plano(w, h, x=0, y=0, z=0, tex=None, c='#ffffff', m='papel', **k):
    return {'f': 'plano', 'd': [w, h], 'p': [x, y, z], 'c': c, 'm': m, **({'tex': tex} if tex else {}), **k}

def clase_masa(m):
    return 'PICKUP' if m < 5 else 'CARRY' if m < 25 else 'PUSH' if m < 80 else 'PUSH_HEAVY' if m < 400 else 'FIXED'
FIJO = 'anclado en la realidad'
def obj(id, nombre, categoria, masa, material, soporte, partes, fijo=None, clase=None, **k):
    """An object: its class comes from its mass (X-01) unless it is anchored (`fijo`: the reason it is FIXED)."""
    assert all(o['id'] != id for o in OUT), 'id repetido ' + id
    if fijo: clase, k['motivo_fijo'] = 'FIXED', fijo
    OUT.append({'id': id, 'nombre': nombre, 'categoria': categoria, 'clase': clase or clase_masa(masa), 'masa': masa, 'material': material, 'soporte': soporte, 'partes': partes, **k})

# the categories this family brings (their mass ranges, kg)
CATEGORIAS = {'ta_producto': [0.01, 15], 'ta_juguete': [0.05, 25], 'ta_herramienta': [0.05, 30], 'ta_libro': [0.1, 12], 'ta_papeleria': [0.01, 12],
              'ta_flor': [0.05, 20], 'ta_joya': [0.005, 5], 'ta_expositor': [1, 150]}

def oscuro(c, f=0.85):
    r, g, b = (int(c[i:i + 2], 16) for i in (1, 3, 5))
    return '#%02x%02x%02x' % (min(255, int(r * f)), min(255, int(g * f)), min(255, int(b * f)))
def mezcla(a, b, t):
    ra, rb = [int(a[i:i + 2], 16) for i in (1, 3, 5)], [int(b[i:i + 2], 16) for i in (1, 3, 5)]
    return '#%02x%02x%02x' % tuple(int(x + (y - x) * t) for x, y in zip(ra, rb))
def r2(v): return round(v, 3)

STEEL, DARK, WOOD, WOOD_D, WOOD_L, WHITE, GLASS, CREAM = '#c3c7ca', '#2f2f32', '#8a5a36', '#5e3b22', '#cfb48a', '#eeeae0', '#bcd6dc', '#e9e2d2'
PLASTIC = {'rojo': '#d23a2c', 'azul': '#2f64b4', 'amarillo': '#f0c030', 'verde': '#3f9a4a', 'naranja': '#ee8a2a', 'rosa': '#e76a9a', 'turquesa': '#2aa6a6', 'morado': '#7a4aa0'}
BRIGHT = list(PLASTIC.values())

# ---------------------------------------------------------------- shelving
def estantes(id, nombre, w, d, ys, alto, c='#e6dfd0', cp='#f2eee4', masa=55, cat='estanteria', soporte='suelo', borde=None, zocalo=0.1, nota=None, tapa=False):
    """A shelving unit: two side panels, a back, a plank at each height of ys (their tops are the surfaces), a kick plate, and
    optionally a coloured price rail along the front of each plank."""
    P = [caja(0.02, alto, d, x=-w / 2 + 0.01, z=d / 2, c=c), caja(0.02, alto, d, x=w / 2 - 0.01, z=d / 2, c=c), caja(w - 0.04, alto, 0.012, z=0.006, c=c)]
    P += [caja(w - 0.04, 0.025, d, y=y - 0.0125, z=d / 2, c=cp) for y in ys]
    if zocalo: P.append(caja(w - 0.04, zocalo, d - 0.03, y=zocalo / 2, z=d / 2, c=oscuro(c, 0.55)))
    if borde: P += [caja(w - 0.04, 0.035, 0.012, y=y + 0.005, z=d - 0.006, c=borde) for y in ys]
    if tapa: P.append(caja(w, 0.025, d, y=alto + 0.0125, z=d / 2, c=cp))
    obj(id, nombre, cat, masa, 'madera', soporte, P, fijo=FIJO, superficies=[{'y': y, 'fondo': r2(d - 0.03)} for y in ys], **({'nota': nota} if nota else {}))

def facing(unit, nx, nz, dx, dz, h, fondo, c, hf=0.92):
    """nx x nz units (unit(x, z) -> parts, its foot at y = 0) at the front, a solid block of the stock behind, to `fondo` deep."""
    P = []
    for iz in range(nz):
        for ix in range(nx):
            P += unit((ix - (nx - 1) / 2) * dx, iz * dz)
    zb = -dz / 2
    extra = fondo - (nz * dz)
    if extra > 0.02:
        P.append(caja(nx * dx - 0.004, h * hf, extra, x=0, y=h * hf / 2, z=zb - extra / 2, c=oscuro(c, 0.9), m='comida'))
    return P

def regis(id, nombre, unit, nx, nz, dx, dz, h, fondo, c, mu, cat='ta_producto', mat='plastico', hf=0.9, nota=None, clase=None):
    """A facing as an object: nx x nz units at the front, a block of stock behind to `fondo` deep; its mass counts the stock."""
    P = facing(unit, nx, nz, dx, dz, h, fondo, c, hf)
    masa = round(min(nx * (fondo / dz) * mu, 14), 2)
    obj(id, nombre, cat, masa, mat, 'superficie', P, clase=clase, **({'nota': nota} if nota else {}))

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
def u_bote(r, h, c, tapa, seg=8):
    def f(x, z):
        return [cil(r, r, h * 0.8, x=x, y=h * 0.4, z=z, c=c, m='plastico', seg=seg), cil(r * 1.03, r * 1.03, h * 0.2, x=x, y=h * 0.9, z=z, c=tapa, m='plastico', seg=seg)]
    return f
def u_botella(r, h, c, etq, tapon, seg=8):
    def f(x, z):
        return [cil(r, r, h * 0.66, x=x, y=h * 0.33, z=z, c=c, m='plastico', seg=seg), cil(r + 0.001, r + 0.001, h * 0.3, x=x, y=h * 0.33, z=z, c=etq, m='papel', seg=seg),
                cil(r * 0.42, r * 0.42, h * 0.34, x=x, y=h * 0.83, z=z, c=tapon, m='plastico', seg=seg)]
    return f
def u_blister(w, h, c, c2, d=0.025):
    """A card with a bubble: a hanging pack."""
    def f(x, z):
        return [caja(w, h, 0.004, x=x, y=h / 2, z=z, c=c, m='papel'), caja(w * 0.7, h * 0.5, d, x=x, y=h * 0.42, z=z + d / 2, c=c2, m='plastico')]
    return f

# ---------------------------------------------------------------- LIGHTING: the shops' own fittings
obj('plafon_cristal_calido', 'Plafón de techo de cristal opal (luz cálida)', 'lampara', 1.4, 'cristal', 'techo', [
    cil(0.2, 0.2, 0.03, y=-0.015, c='#d8d2c4', m='metal', seg=14), cil(0.17, 0.2, 0.1, y=-0.08, c='#f0e8d4', m='cristal', luz=True, seg=14)], fijo=FIJO)

def pila(id, nombre, cols, w, d, h1, n, mu, cat='ta_papeleria', mat='papel', m='papel', nota=None):
    """A stack of n slabs (notebooks, towels, folded things), colours taken in turn."""
    P = [caja(w - 0.006 * (i % 2), h1, d - 0.004 * (i % 2), y=h1 * (i + 0.5), c=cols[i % len(cols)], m=m) for i in range(n)]
    obj(id, nombre, cat, round(n * mu, 2), mat, 'superficie', P, **({'nota': nota} if nota else {}))

def panel(id, nombre, w, h, y0, items, c='#d9cfb6', masa=7, cat='ta_expositor', nota=None, **k):
    """A board screwed to the wall (a peg board) with things hung on it: items = parts in the object's frame (the board's face at z = 0.02)."""
    P = [caja(w, h, 0.02, y=y0 + h / 2, z=0.01, c=c)] + items
    obj(id, nombre, cat, masa, 'madera', 'pared', P, fijo=FIJO, **({'nota': nota} if nota else {}), **k)

# ================================================================== THE VARIETY STORE («todo a cien»)
CHAPA = '#e9e6dc'
obj('mostrador_bazar', 'Mostrador del bazar (1,2 m)', 'mostrador', 150, 'madera', 'suelo', [
    caja(1.2, 0.88, 0.5, z=-0.04, c='#e8e2d2'), caja(1.2, 0.05, 0.62, y=0.925, z=0.0, c='#b88a58'), caja(1.1, 0.5, 0.01, y=0.5, z=0.216, c='#d6cbb0'),
    caja(1.2, 0.07, 0.01, y=0.035, z=0.216, c='#3c3c40'), caja(1.1, 0.04, 0.12, y=0.27, z=0.27, c='#c0392b')], fijo='estructural', superficies=[{'y': 0.95, 'margen': 0.04}],
    nota='el mostrador con la caja, junto a la puerta, con la repisa de las cosas de última hora')
estantes('gondola_bazar', 'Góndola del bazar', 1.0, 0.42, [0.2, 0.52, 0.84, 1.16, 1.48], 1.7, c='#dcb64a', cp='#eceef0', masa=48, borde='#c0392b',
         nota='por una cara: se pone de dos en dos, espalda con espalda; el rail amarillo de los precios')
estantes('estanteria_bazar_pared', 'Estantería de pared del bazar', 1.0, 0.38, [0.18, 0.5, 0.82, 1.14, 1.46, 1.78], 2.1, c='#e4ddc9', cp='#f0ebdd', masa=60, borde='#f0c030')
estantes('estanteria_bazar_baja', 'Estantería baja del bazar (bajo los paneles)', 1.0, 0.4, [0.2, 0.5, 0.8, 1.1], 1.1, c='#e4ddc9', cp='#f0ebdd', masa=32, borde='#f0c030')

# ---- what is hung on pegboards: things in packs and on hooks (a board is 1.0 m wide, from 1.35 to 2.2 m)
def utensilio(x, y, c1, c2, largo=0.24, ancho=0.07):
    return [caja(0.018, largo, 0.012, x=x, y=y - largo / 2, z=0.03, c=c1, m='plastico'), caja(ancho, ancho * 1.3, 0.01, x=x, y=y - largo - ancho * 0.6, z=0.03, c=c2, m='plastico')]
def cepillo(x, y, c1, c2):
    return [caja(0.02, 0.42, 0.012, x=x, y=y - 0.21, z=0.03, c=c1, m='madera'), caja(0.11, 0.05, 0.03, x=x, y=y - 0.45, z=0.04, c=c2, m='plastico')]
def paquete(x, y, w, h, c, c2):
    return [caja(w, h, 0.006, x=x, y=y, z=0.026, c=c, m='papel'), caja(w * 0.72, h * 0.5, 0.025, x=x, y=y - h * 0.08, z=0.04, c=c2, m='plastico')]
rr = random.Random(11)
panel('panel_cocina', 'Panel de cocina con utensilios colgados', 1.0, 0.85, 1.35,
      [p for fila, yy in enumerate((2.14, 1.78)) for i in range(7) for p in utensilio(-0.42 + i * 0.14, yy, BRIGHT[(i + fila * 3) % 8], oscuro(BRIGHT[(i * 2 + fila) % 8], 0.9), largo=0.2 + 0.03 * (i % 3))])
panel('panel_limpieza', 'Panel de limpieza con cepillos y recogedores', 1.0, 0.85, 1.35,
      [p for i in range(8) for p in cepillo(-0.44 + i * 0.125, 2.2, ('#8a5a36', '#cfb48a')[i % 2], BRIGHT[(i * 3) % 8])])
panel('panel_cargadores', 'Panel de cargadores y accesorios de móvil', 1.0, 0.85, 1.35,
      [p for fila, yy in enumerate((2.1, 1.8, 1.5)) for i in range(5) for p in paquete(-0.4 + i * 0.2, yy, 0.15, 0.24, ('#2f64b4', '#d23a2c', '#2aa6a6', '#f0c030', '#7a4aa0')[(i + fila) % 5], ('#2f2f32', '#e8e8e4', '#2f2f32', '#9aa0a4', '#2f2f32')[(i * 2 + fila) % 5])],
      nota='cargadores, cables y auriculares en blísteres', )
def linterna(x, y):
    return [caja(0.06, 0.16, 0.006, x=x, y=y, z=0.026, c='#f0c030', m='papel'), cil(0.016, 0.02, 0.15, x=x, y=y, z=0.045, c='#2f64b4', m='plastico', seg=6), cil(0.028, 0.02, 0.04, x=x, y=y + 0.09, z=0.045, c='#d23a2c', m='plastico', seg=6)]
def linterna_grande(x, y):
    return [caja(0.14, 0.34, 0.006, x=x, y=y, z=0.026, c='#d23a2c', m='papel'), cil(0.03, 0.035, 0.3, x=x, y=y, z=0.05, c='#2f2f32', m='plastico', seg=8), cil(0.05, 0.035, 0.07, x=x, y=y + 0.17, z=0.05, c='#9aa0a4', m='plastico', seg=8)]
panel('panel_linternas', 'Panel de linternas y pilas', 1.0, 0.85, 1.35,
      [p for i in range(5) for p in linterna_grande(-0.4 + i * 0.2, 2.0)] + [p for i in range(10) for p in linterna(-0.45 + i * 0.1, 1.62)])
def reloj(x, y, r, c, cara='#efe9d6'):
    return [cil(r, r, 0.035, x=x, y=y, z=0.04, c=c, m='plastico', seg=14, r=[90, 0, 0]), cil(r * 0.84, r * 0.84, 0.01, x=x, y=y, z=0.06, c=cara, m='plastico', seg=14, r=[90, 0, 0]),
            caja(0.008, r * 0.62, 0.004, x=x, y=y + r * 0.28, z=0.068, c='#2f2f32', m='plastico'), caja(r * 0.5, 0.008, 0.004, x=x + r * 0.22, y=y, z=0.068, c='#2f2f32', m='plastico')]
panel('panel_relojes', 'Panel de relojes de pared', 1.0, 0.85, 1.35,
      [p for i, (x, y, r, c) in enumerate(((-0.3, 1.95, 0.15, '#8a5a36'), (0.0, 2.0, 0.13, '#d23a2c'), (0.3, 1.95, 0.15, '#2f2f32'), (-0.34, 1.6, 0.11, '#f0c030'), (-0.12, 1.6, 0.11, '#2aa6a6'),
                                           (0.1, 1.58, 0.12, '#cfb48a'), (0.34, 1.6, 0.11, '#e76a9a'))) for p in reloj(x, y, r, c)])
def espejo_marco(x, y, w, h, c):
    return [caja(w, h, 0.025, x=x, y=y, z=0.032, c=c, m='madera'), caja(w - 0.04, h - 0.04, 0.006, x=x, y=y, z=0.047, c='#c3d3da', m='metal')]
panel('panel_espejos', 'Panel de espejos', 1.0, 0.85, 1.35,
      espejo_marco(-0.28, 1.95, 0.26, 0.36, '#8a5a36') + espejo_marco(0.0, 1.9, 0.3, 0.46, '#d6c8a8') + espejo_marco(0.3, 1.95, 0.26, 0.36, '#2f2f32') + espejo_marco(-0.3, 1.55, 0.2, 0.2, '#d23a2c')
      + espejo_marco(-0.05, 1.55, 0.2, 0.2, '#f0c030') + espejo_marco(0.22, 1.55, 0.2, 0.2, '#2aa6a6') + espejo_marco(0.42, 1.55, 0.12, 0.2, '#8a5a36'))
def lamina(x, y, w, h, marco, cielo, suelo, motivo):
    return [caja(w, h, 0.025, x=x, y=y, z=0.032, c=marco, m='madera'), caja(w - 0.04, (h - 0.04) * 0.55, 0.006, x=x, y=y + (h - 0.04) * 0.225, z=0.047, c=cielo, m='papel'),
            caja(w - 0.04, (h - 0.04) * 0.45, 0.006, x=x, y=y - (h - 0.04) * 0.275, z=0.047, c=suelo, m='papel'), caja((w - 0.04) * 0.3, (h - 0.04) * 0.25, 0.008, x=x - w * 0.1, y=y - h * 0.02, z=0.05, c=motivo, m='papel')]
panel('panel_cuadros', 'Panel de cuadros y láminas', 1.0, 0.85, 1.35,
      lamina(-0.27, 1.95, 0.4, 0.3, '#2f2f32', '#8ec0d8', '#6a9a4a', '#d23a2c') + lamina(0.2, 1.95, 0.5, 0.3, '#8a5a36', '#e8c880', '#a8683a', '#2f64b4') + lamina(-0.33, 1.52, 0.26, 0.36, '#d6c8a8', '#c8d8e0', '#4a7a9a', '#f0c030')
      + lamina(-0.02, 1.52, 0.26, 0.36, '#2f2f32', '#e8b8c0', '#8a6a9a', '#eeeae0') + lamina(0.3, 1.52, 0.3, 0.36, '#cfb48a', '#a8d0a0', '#5a8a3a', '#d23a2c'))

# ---- the stands on the floor
def alambre(w, h, d, y0, c='#b8bcc0'):
    """A wire basket's cage (thin metal bars: corner posts and two rails round), from y0 up h — the contents show through."""
    P = [caja(0.012, h, 0.012, x=sx * w / 2, y=y0 + h / 2, z=sz * d / 2, c=c, m='metal') for sx in (-1, 1) for sz in (-1, 1)]
    for yy in (y0 + h - 0.006, y0 + h * 0.5):
        P += [caja(w, 0.012, 0.012, y=yy, z=sz * d / 2, c=c, m='metal') for sz in (-1, 1)] + [caja(0.012, 0.012, d, x=sx * w / 2, y=yy, c=c, m='metal') for sx in (-1, 1)]
    return P
def patas(w, d, h, c='#7a7e82', g=0.03):
    return [caja(g, h, g, x=sx * (w / 2 - g / 2), y=h / 2, z=sz * (d / 2 - g / 2), c=c, m='metal') for sx in (-1, 1) for sz in (-1, 1)]
obj('expositor_cojines', 'Cesto de cojines', 'ta_expositor', 12, 'metal', 'suelo', patas(0.8, 0.55, 0.3) + [caja(0.8, 0.03, 0.55, y=0.3, c='#7a7e82', m='metal')] + alambre(0.8, 0.35, 0.55, 0.3) + [
    caja(0.42, 0.12, 0.42, x=-0.15, y=0.43, z=0.02, c='#d23a2c', m='tela'), caja(0.4, 0.12, 0.4, x=0.18, y=0.43, z=-0.02, c='#2f64b4', m='tela'), caja(0.4, 0.12, 0.4, x=-0.1, y=0.55, z=0.0, c='#f0c030', m='tela', r=[0, 20, 0]),
    caja(0.38, 0.12, 0.38, x=0.2, y=0.55, z=0.03, c='#3f9a4a', m='tela', r=[0, -15, 0]), caja(0.4, 0.12, 0.4, x=0.02, y=0.67, z=-0.03, c='#e76a9a', m='tela', r=[0, 35, 0]), caja(0.36, 0.1, 0.36, x=-0.22, y=0.66, z=0.05, c='#eeeae0', m='tela', r=[0, 5, 0])],
    nota='cojines estampados, 6 €')
def maceta(x, y, z, alto=0.1, c='#b8683a', verde='#4f8a3a', forma='cil'):
    P = [cil(0.04, 0.03, 0.06, x=x, y=y + 0.03, z=z, c=c, m='ceramica', seg=8)]
    if forma == 'cil': P.append(cil(0.025, 0.028, alto, x=x, y=y + 0.06 + alto / 2, z=z, c=verde, m='comida', seg=6))
    elif forma == 'bola': P += [cil(0.035, 0.035, alto * 0.7, x=x, y=y + 0.06 + alto * 0.35, z=z, c=verde, m='comida', seg=6)]
    else: P += [cono(0.035, alto, x=x, y=y + 0.06 + alto / 2, z=z, c=verde, m='comida', seg=6)]
    P.append(caja(0.012, 0.012, 0.012, x=x, y=y + 0.066 + alto, z=z, c='#e76a9a', m='comida'))
    return P
P_ = [caja(0.56, 0.03, 0.38, y=0.3, c='#8a5a36'), caja(0.56, 0.03, 0.38, y=0.62, c='#8a5a36'), caja(0.56, 0.03, 0.38, y=0.94, c='#8a5a36')] + patas(0.56, 0.38, 0.94, c='#6a4a2c')
for lv, y in enumerate((0.315, 0.635, 0.955)):
    for i in range(4):
        P_ += maceta(-0.21 + i * 0.14, y, 0.0, alto=(0.1, 0.14, 0.09, 0.12)[(i + lv) % 4], c=('#b8683a', '#a85a30')[i % 2], verde=('#4f8a3a', '#6a9a4a', '#3f7a4a')[(i + lv) % 3], forma=('cil', 'bola', 'cono')[(i + lv) % 3])
obj('expositor_cactus', 'Estantería de cactus en maceta', 'ta_expositor', 14, 'madera', 'suelo', P_, nota='cactus, 3 €')
def peluche(x, y, z, c, tipo=0):
    P = [cil(0.075, 0.085, 0.14, x=x, y=y + 0.07, z=z, c=c, m='tela', seg=8), cil(0.06, 0.06, 0.09, x=x, y=y + 0.19, z=z, c=mezcla(c, '#eeeae0', 0.15), m='tela', seg=8),
         cil(0.025, 0.025, 0.02, x=x - 0.05, y=y + 0.25, z=z, c=c, m='tela', seg=6), cil(0.025, 0.025, 0.02, x=x + 0.05, y=y + 0.25, z=z, c=c, m='tela', seg=6),
         caja(0.03, 0.1, 0.04, x=x - 0.1, y=y + 0.09, z=z + 0.02, c=c, m='tela'), caja(0.03, 0.1, 0.04, x=x + 0.1, y=y + 0.09, z=z + 0.02, c=c, m='tela')]
    return P
pel = [(-0.28, 0.12, -0.2, '#c8884a'), (-0.1, 0.1, -0.22, '#e76a9a'), (0.1, 0.12, -0.2, '#f0c030'), (0.28, 0.1, -0.15, '#7aa0d8'), (-0.25, 0.14, 0.1, '#eeeae0'), (0.0, 0.12, 0.05, '#3f9a4a'), (0.25, 0.14, 0.12, '#b0603a'),
       (-0.12, 0.3, -0.1, '#e76a9a'), (0.12, 0.3, -0.05, '#c8884a'), (0.0, 0.42, -0.1, '#7a4aa0')]
obj('cubo_peluches', 'Cubo de peluches', 'ta_expositor', 9, 'tela', 'suelo', patas(0.9, 0.7, 0.15) + [caja(0.9, 0.03, 0.7, y=0.15, c='#7a7e82', m='metal')] + alambre(0.9, 0.55, 0.7, 0.15, '#d23a2c')
    + [p for (x, y, z, c) in pel for p in peluche(x, 0.16 + y * 0.9 - 0.12, z, c)], nota='peluches, 8 €')
def cometa(x, y, z, c1, c2, ry=0, rz=0, s=0.32):
    return [caja(s, s * 1.25, 0.006, x=x, y=y, z=z, c=c1, m='tela', r=[0, ry, 45 + rz]), caja(s * 0.45, s * 0.7, 0.008, x=x, y=y, z=z + 0.002, c=c2, m='tela', r=[0, ry, 45 + rz])]
obj('expositor_cometas', 'Cubo de cometas', 'ta_expositor', 6, 'tela', 'suelo', patas(0.5, 0.4, 0.5) + [caja(0.5, 0.03, 0.4, y=0.5, c='#7a7e82', m='metal')] + [cil(0.025, 0.025, 1.05, x=x, y=0.52 + 0.525, z=z, c='#3f9a4a', m='plastico', seg=6) for x, z in ((-0.15, 0.0), (0.0, 0.05), (0.15, 0.0))]
    + cometa(-0.16, 1.3, 0.2, '#d23a2c', '#f0c030', rz=0) + cometa(0.14, 1.4, 0.2, '#2f64b4', '#eeeae0', rz=0) + cometa(0.0, 0.98, 0.22, '#3f9a4a', '#f0c030', rz=0) + cometa(-0.2, 0.8, 0.22, '#e76a9a', '#eeeae0', rz=0, s=0.26)
    + cometa(0.2, 0.84, 0.22, '#ee8a2a', '#2f64b4', rz=0, s=0.26), nota='cometas, 5 €')
bolas = [(-0.2, 0.1, '#d23a2c'), (0.0, 0.1, '#2f64b4'), (0.2, 0.1, '#f0c030'), (-0.1, 0.28, '#3f9a4a'), (0.1, 0.28, '#ee8a2a'), (0.0, 0.46, '#eeeae0')]
obj('red_balones', 'Jaula de balones', 'ta_expositor', 8, 'metal', 'suelo', patas(0.8, 0.6, 0.15) + [caja(0.8, 0.03, 0.6, y=0.15, c='#7a7e82', m='metal')] + alambre(0.8, 0.7, 0.6, 0.15) + [
    esf(0.115, -0.22 + 0.22 * i, 0.285, 0.0, c=c, m='goma') for i, c in enumerate(('#d23a2c', '#2f64b4', '#f0c030'))] + [esf(0.115, -0.11 + 0.22 * i, 0.285 + 0.2, 0.0, c=c, m='goma') for i, c in enumerate(('#3f9a4a', '#ee8a2a'))]
    + [esf(0.115, 0.0, 0.285 + 0.4, 0.0, c='#eeeae0', m='goma')], nota='balones, 7 €')
def lamparita(x, y, z, c, h=0.2):
    return [cil(0.05, 0.06, 0.02, x=x, y=y + 0.01, z=z, c=c, m='ceramica', seg=10), cil(0.012, 0.012, h, x=x, y=y + 0.02 + h / 2, z=z, c=c, m='ceramica', seg=6), cil(0.06, 0.1, 0.14, x=x, y=y + h + 0.08, z=z, c='#efe3c6', m='tela', seg=10)]
obj('expositor_lamparitas', 'Estante de lamparitas de mesa', 'ta_expositor', 14, 'madera', 'suelo',
    [caja(0.6, 0.03, 0.34, y=0.3, c='#d6cbb0'), caja(0.6, 0.03, 0.34, y=0.8, c='#d6cbb0')] + patas(0.6, 0.34, 0.8, c='#9a7040') + [caja(0.6, 0.03, 0.34, y=1.3, c='#d6cbb0')] + [caja(0.03, 1.3, 0.03, x=sx * 0.285, y=0.65, z=-0.15, c='#9a7040') for sx in (-1, 1)]
    + [p for lv, y in enumerate((0.315, 0.815)) for i in range(3) for p in lamparita(-0.2 + i * 0.2, y, 0.0, ('#2f64b4', '#d23a2c', '#3f9a4a', '#f0c030', '#e76a9a', '#2aa6a6')[(i + lv * 3) % 6], h=0.18 + 0.03 * (i % 2))], nota='lamparitas, 12 €')
obj('expositor_posters', 'Cubo de láminas enrolladas', 'ta_expositor', 5, 'papel', 'suelo', [cil(0.2, 0.2, 0.45, c='#3a3d42', m='plastico', seg=12)] + [
    p for i, (x, z) in enumerate(((-0.08, -0.05), (0.06, -0.08), (0.1, 0.06), (-0.06, 0.08), (0.0, 0.0), (-0.12, 0.0), (0.12, -0.0), (0.0, -0.13)))
    for p in (cil(0.032, 0.032, 0.9, x=x, y=0.5 + 0.1 * (i % 3), z=z, c=('#e8d8b0', '#d6c8a8', '#c8d8e0', '#e8b8c0')[i % 4], m='papel', seg=6, r=[0, 0, 3 * (i % 3 - 1)]), cil(0.034, 0.034, 0.03, x=x, y=0.93 + 0.1 * (i % 3), z=z, c=BRIGHT[i % 8], m='plastico', seg=6))],
    nota='láminas y pósters, 4 €')
obj('expositor_cuadernos', 'Torre de cuadernos y material escolar', 'ta_expositor', 12, 'metal', 'suelo', [
    caja(0.5, 0.03, 0.4, y=0.015, c='#2f2f32', m='metal'), cil(0.025, 0.025, 1.5, y=0.76, c='#7a7e82', m='metal', seg=8)] + [
    p for lv in range(4) for p in [caja(0.46, 0.02, 0.2, y=0.35 + lv * 0.33, z=0.08, c='#f0c030', m='plastico', r=[-12, 0, 0])]
    + [caja(0.13, 0.02, 0.17, x=-0.15 + 0.15 * i, y=0.4 + lv * 0.33, z=0.09, c=BRIGHT[(lv * 3 + i) % 8], m='papel', r=[-12, 0, 0]) for i in range(3)]], nota='cuadernos, 2 €')
obj('cesta_baratijas', 'Cesta de baratijas', 'ta_expositor', 7, 'metal', 'suelo', patas(0.7, 0.45, 0.4) + [caja(0.7, 0.03, 0.45, y=0.4, c='#d6d9db', m='metal')] + alambre(0.7, 0.18, 0.45, 0.4, '#d6d9db') + [
    caja(0.12, 0.08, 0.12, x=-0.25 + 0.17 * i, y=0.47, z=-0.1, c=BRIGHT[i % 8], m='plastico', r=[0, 12 * i, 0]) for i in range(4)] + [
    caja(0.14, 0.05, 0.1, x=-0.2 + 0.2 * i, y=0.46, z=0.1, c=BRIGHT[(i + 4) % 8], m='plastico', r=[0, -10 * i, 0]) for i in range(3)])
obj('expositor_pilas_mostrador', 'Expositor de pilas de mostrador', 'ta_expositor', 1.2, 'plastico', 'superficie', [
    caja(0.24, 0.02, 0.14, c='#2f2f32', m='plastico'), caja(0.24, 0.2, 0.01, y=0.12, z=-0.065, c='#d23a2c', m='plastico')] + [
    p for i in range(4) for p in (caja(0.05, 0.12, 0.004, x=-0.09 + i * 0.06, y=0.1, z=-0.055, c=('#2f64b4', '#f0c030')[i % 2], m='papel'), caja(0.035, 0.05, 0.02, x=-0.09 + i * 0.06, y=0.08, z=-0.042, c='#2f2f32', m='plastico'))])
obj('expositor_llaveros', 'Expositor giratorio de llaveros', 'ta_expositor', 1.6, 'metal', 'superficie', [cil(0.08, 0.09, 0.02, c='#2f2f32', m='metal', seg=10), cil(0.01, 0.01, 0.32, y=0.18, c='#9aa0a4', m='metal', seg=6)] + [
    caja(0.03, 0.06, 0.01, x=0.06 * math.sin(a), y=0.12 + 0.08 * (i % 3), z=0.06 * math.cos(a), c=BRIGHT[i % 8], m='plastico', r=[0, math.degrees(a), 0]) for i, a in enumerate(2 * math.pi * k / 9 for k in range(9))])
obj('pila_bolsas_plastico', 'Pila de bolsas de plástico', 'ta_papeleria', 0.3, 'plastico', 'superficie', [caja(0.28, 0.05, 0.2, c='#eeeae0', m='plastico'), caja(0.28, 0.01, 0.2, y=0.056, c='#d23a2c', m='plastico')])
obj('cartel_precio_bazar', 'Cartel de precios (cartulina amarilla)', 'cuadro', 0.3, 'papel', 'pared', [caja(0.4, 0.28, 0.006, y=1.7, z=0.003, c='#f0d030', m='papel'), plano(0.38, 0.26, y=1.7, z=0.0075, tex={'tipo': 'ta_cartel_euro'})])
obj('rotulo_bazar', 'Rótulo interior del bazar', 'decoracion', 3, 'madera', 'pared', [caja(1.6, 0.4, 0.03, y=2.5, z=0.015, c='#6a2a22'), plano(1.54, 0.34, y=2.5, z=0.033, tex={'tipo': 'ta_rotulo_bazar', 'rotulo_local': True})])
obj('cartel_ofertas_bazar', 'Cartel de ofertas', 'cuadro', 0.4, 'papel', 'pared', [caja(0.5, 0.7, 0.012, y=1.65, z=0.006, c='#d23a2c', m='papel'), plano(0.46, 0.66, y=1.65, z=0.0135, tex={'tipo': 'ta_cartel_ofertas'})])

# ---- what the bazar sells (facings and stacks)
def u_cubo(c, r=0.1, h=0.22):
    def f(x, z):
        return [cil(r * 1.05, r * 0.8, h, x=x, y=h / 2, z=z, c=c, m='plastico', seg=10), cil(r * 1.12, r * 1.12, 0.012, x=x, y=h - 0.006, z=z, c=oscuro(c, 0.88), m='plastico', seg=10)]
    return f
def u_barreno(c, r=0.2, h=0.11):
    def f(x, z):
        return [cil(r, r * 0.78, h, x=x, y=h / 2, z=z, c=c, m='plastico', seg=12), cil(r * 0.9, r * 0.72, 0.01, x=x, y=h - 0.012, z=z, c=oscuro(c, 0.8), m='plastico', seg=12)]
    return f
def u_apilado(w, d, n, h1, cols, tapa=None, m='plastico'):
    def f(x, z):
        return [caja(w, h1, d, x=x, y=h1 * (i + 0.5), z=z, c=cols[i % len(cols)], m=m) for i in range(n)] + ([caja(w + 0.004, 0.012, d + 0.004, x=x, y=h1 * n + 0.006, z=z, c=tapa, m=m)] if tapa else [])
    return f
def u_taza(c, asa=None):
    def f(x, z):
        return [cil(0.04, 0.036, 0.09, x=x, y=0.045, z=z, c=c, m='ceramica', seg=8), caja(0.012, 0.06, 0.03, x=x + 0.05, y=0.05, z=z, c=asa or c, m='ceramica')]
    return f
def u_vaso(c):
    def f(x, z): return [cil(0.034, 0.028, 0.1, x=x, y=0.05, z=z, c=c, m='plastico', seg=7)]
    return f
def u_plato(c, borde):
    def f(x, z): return [cil(0.11, 0.11, 0.09, x=x, y=0.045, z=z, c=c, m='ceramica', seg=12), cil(0.112, 0.112, 0.012, x=x, y=0.084, z=z, c=borde, m='ceramica', seg=12)]
    return f
def u_olla(c):
    def f(x, z):
        return [cil(0.1, 0.1, 0.13, x=x, y=0.065, z=z, c=c, m='metal', seg=10), cil(0.105, 0.105, 0.012, x=x, y=0.136, z=z, c='#9aa0a4', m='metal', seg=10), cil(0.015, 0.015, 0.02, x=x, y=0.155, z=z, c='#2f2f32', m='plastico', seg=6),
                caja(0.06, 0.02, 0.025, x=x - 0.14, y=0.1, z=z, c='#2f2f32', m='plastico'), caja(0.06, 0.02, 0.025, x=x + 0.14, y=0.1, z=z, c='#2f2f32', m='plastico')]
    return f
def u_cesto(c, w=0.42, h=0.27, d=0.3):
    def f(x, z): return [caja(w, h, d, x=x, y=h / 2, z=z, c=c, m='plastico'), caja(w - 0.06, 0.012, d - 0.06, x=x, y=h - 0.006, z=z, c=oscuro(c, 0.7), m='plastico'), caja(0.12, 0.03, 0.01, x=x - w / 2 + 0.1, y=h - 0.06, z=z + d / 2, c=oscuro(c, 0.8), m='plastico'), caja(0.12, 0.03, 0.01, x=x + w / 2 - 0.1, y=h - 0.06, z=z + d / 2, c=oscuro(c, 0.8), m='plastico')]
    return f
regis('bz_cubos', 'Cubos de plástico', u_cubo('#d23a2c'), 2, 1, 0.24, 0.24, 0.22, 0.3, '#d23a2c', 0.7)
regis('bz_cubos_azules', 'Cubos de fregar azules', u_cubo('#2f64b4', r=0.11, h=0.26), 2, 1, 0.26, 0.26, 0.26, 0.3, '#2f64b4', 0.8)
regis('bz_barrenos', 'Barreños de colores', u_barreno('#3f9a4a'), 1, 2, 0.42, 0.42, 0.13, 0.4, '#3f9a4a', 0.5)
regis('bz_barrenos_naranja', 'Barreños anaranjados', u_barreno('#ee8a2a', r=0.17, h=0.1), 2, 1, 0.36, 0.36, 0.1, 0.36, '#ee8a2a', 0.4)
regis('bz_fiambreras', 'Fiambreras con tapa de colores', u_apilado(0.17, 0.12, 3, 0.07, ['#e8e6dc'], tapa='#2f64b4'), 3, 2, 0.19, 0.14, 0.22, 0.3, '#e8e6dc', 0.25)
regis('bz_fiambreras_rojas', 'Fiambreras rojas', u_apilado(0.2, 0.14, 2, 0.08, ['#e8e6dc'], tapa='#d23a2c'), 2, 2, 0.22, 0.16, 0.18, 0.32, '#e8e6dc', 0.3)
regis('bz_vasos', 'Vasos de plástico', u_vaso('#2aa6a6'), 6, 2, 0.07, 0.07, 0.1, 0.3, '#2aa6a6', 0.06)
regis('bz_vasos_rosa', 'Vasos de colores', u_vaso('#e76a9a'), 5, 3, 0.07, 0.07, 0.1, 0.34, '#e76a9a', 0.06)
regis('bz_platos', 'Platos blancos', u_plato('#eeeae0', '#2f64b4'), 2, 1, 0.24, 0.24, 0.12, 0.3, '#eeeae0', 1.2, mat='ceramica')
regis('bz_tazas', 'Tazas de desayuno', u_taza('#d23a2c', '#d23a2c'), 4, 2, 0.1, 0.1, 0.09, 0.3, '#d23a2c', 0.3, mat='ceramica')
regis('bz_tazas_azules', 'Tazas azules', u_taza('#2f64b4'), 3, 2, 0.1, 0.1, 0.09, 0.3, '#2f64b4', 0.3, mat='ceramica')
regis('bz_ollas', 'Ollas con tapa', u_olla('#aab0b4'), 2, 1, 0.3, 0.3, 0.16, 0.32, '#aab0b4', 1.8, mat='metal')
regis('bz_cestos_ropa', 'Cestos de la ropa', u_cesto('#3f9a4a'), 1, 1, 0.44, 0.32, 0.27, 0.34, '#3f9a4a', 1.2)
regis('bz_cestos_rosa', 'Cestos de la ropa rosas', u_cesto('#e76a9a', w=0.38, h=0.24, d=0.28), 1, 1, 0.38, 0.3, 0.24, 0.32, '#e76a9a', 1.0)
pila('bz_toallas', 'Toallas dobladas', ['#2f64b4', '#d23a2c', '#eeeae0', '#3f9a4a'], 0.34, 0.24, 0.05, 5, 0.35, cat='ta_producto', mat='tela', m='tela')
pila('bz_trapos', 'Bayetas y paños', ['#f0c030', '#3f9a4a', '#2aa6a6'], 0.28, 0.2, 0.03, 6, 0.08, cat='ta_producto', mat='tela', m='tela')
def u_velon(c, tapa):
    def f(x, z): return [cil(0.04, 0.04, 0.09, x=x, y=0.045, z=z, c=c, m='cristal', seg=8), cil(0.041, 0.041, 0.012, x=x, y=0.096, z=z, c=tapa, m='metal', seg=8)]
    return f
regis('bz_velas', 'Velas en vaso', u_velon('#c8884a', '#d6b25a'), 4, 2, 0.09, 0.09, 0.1, 0.28, '#c8884a', 0.25)
regis('bz_jarrones', 'Jarrones de cristal de colores', lambda x, z: [cil(0.06, 0.05, 0.1, x=x, y=0.05, z=z, c='#7ab0c8', m='cristal', seg=10), cil(0.04, 0.06, 0.08, x=x, y=0.14, z=z, c='#7ab0c8', m='cristal', seg=10), cil(0.04, 0.04, 0.05, x=x, y=0.205, z=z, c='#7ab0c8', m='cristal', seg=10)],
      3, 1, 0.14, 0.14, 0.23, 0.2, '#7ab0c8', 0.5, mat='cristal')
regis('bz_marcos', 'Marcos de fotos', lambda x, z: [caja(0.15, 0.2, 0.012, x=x, y=0.1, z=z, c=('#8a5a36', '#2f2f32', '#cfb48a', '#d23a2c')[int(abs(x * 100)) % 4], m='madera', r=[-8, 0, 0]), caja(0.11, 0.16, 0.014, x=x, y=0.1, z=z + 0.003, c='#c8d8e0', m='papel', r=[-8, 0, 0])],
      5, 1, 0.16, 0.05, 0.2, 0.06, '#8a5a36', 0.18, mat='madera')
def u_flores(c1, c2):
    def f(x, z):
        P = [cil(0.045, 0.035, 0.07, x=x, y=0.035, z=z, c=c2, m='plastico', seg=7)]
        for i, (dx, dz, h) in enumerate(((0, 0, 0.2), (-0.03, 0.01, 0.17), (0.03, -0.01, 0.18), (0.0, 0.03, 0.15), (-0.015, -0.03, 0.19))):
            P += [cil(0.003, 0.003, h, x=x + dx, y=0.07 + h / 2, z=z + dz, c='#3f7a3a', m='comida', seg=4), caja(0.035, 0.025, 0.035, x=x + dx, y=0.07 + h, z=z + dz, c=c1 if i % 2 else mezcla(c1, '#eeeae0', 0.3), m='comida', r=[0, 30 * i, 0])]
        return P
    return f
regis('bz_flores_artificiales', 'Ramos de flores artificiales', u_flores('#d23a2c', '#eeeae0'), 3, 1, 0.12, 0.12, 0.27, 0.2, '#3f7a3a', 0.15, hf=0.5)
regis('bz_flores_lilas', 'Ramos artificiales lilas', u_flores('#a070c8', '#d6c8a8'), 3, 1, 0.12, 0.12, 0.27, 0.2, '#3f7a3a', 0.15, hf=0.5)
pila('bz_cuadernos', 'Cuadernos de espiral', ['#2f64b4', '#d23a2c', '#3f9a4a', '#f0c030', '#e76a9a'], 0.21, 0.15, 0.012, 7, 0.1)
pila('bz_cuadernos_a4', 'Cuadernos A4 de tapa dura', ['#7a4aa0', '#2aa6a6', '#ee8a2a', '#2f64b4'], 0.3, 0.22, 0.016, 6, 0.28)
regis('bz_carpetas', 'Carpetas de colores', lambda x, z: [caja(0.034, 0.27, 0.22, x=x, y=0.135, z=z, c=BRIGHT[int(abs(x * 100)) % 8], m='plastico')], 7, 1, 0.036, 0.22, 0.27, 0.22, '#2f64b4', 0.2)
regis('bz_boligrafos', 'Paquetes de bolígrafos', u_blister(0.07, 0.19, '#2f64b4', '#d23a2c'), 4, 1, 0.08, 0.04, 0.19, 0.06, '#2f64b4', 0.05, hf=0.2)
regis('bz_pegamentos', 'Barras de pegamento', lambda x, z: [cil(0.014, 0.014, 0.09, x=x, y=0.045, z=z, c='#3f9a4a', m='plastico', seg=6), cil(0.015, 0.015, 0.025, x=x, y=0.102, z=z, c='#eeeae0', m='plastico', seg=6)], 8, 2, 0.034, 0.034, 0.11, 0.1, '#3f9a4a', 0.03)
regis('bz_lapices_color', 'Cajas de lápices de colores', u_caja(0.19, 0.012, 0.09, '#f0c030', '#d23a2c', banda=0.9), 3, 5, 0.2, 0.1, 0.07, 0.3, '#f0c030', 0.08, cat='ta_papeleria', mat='papel', hf=0.9)
regis('bz_acuarelas', 'Cajas de acuarelas', u_caja(0.2, 0.025, 0.12, '#eeeae0', '#2aa6a6', banda=0.5), 2, 3, 0.21, 0.13, 0.075, 0.3, '#eeeae0', 0.2, cat='ta_papeleria', mat='papel', hf=0.9)
regis('bz_puzles', 'Puzles en caja', u_caja(0.3, 0.05, 0.22, '#2f64b4', '#f0c030', banda=0.5), 1, 5, 0.3, 0.06, 0.22, 0.26, '#2f64b4', 0.5, cat='ta_juguete', mat='papel', hf=0.95)
def u_cochecito(c):
    def f(x, z): return [caja(0.07, 0.025, 0.14, x=x, y=0.02, z=z, c=c, m='plastico'), caja(0.065, 0.025, 0.07, x=x, y=0.045, z=z - 0.01, c=mezcla(c, '#eeeae0', 0.4), m='plastico')] + [cil(0.014, 0.014, 0.01, x=x + sx * 0.037, y=0.014, z=z + sz * 0.045, c='#2f2f32', m='goma', seg=6, r=[0, 0, 90]) for sx in (-1, 1) for sz in (-1, 1)]
    return f
regis('bz_cochecitos', 'Coches de juguete', u_cochecito('#d23a2c'), 4, 2, 0.085, 0.16, 0.06, 0.3, '#d23a2c', 0.08, cat='ta_juguete')
regis('bz_munecas', 'Muñecas en caja', lambda x, z: [caja(0.13, 0.3, 0.06, x=x, y=0.15, z=z, c='#e76a9a', m='papel'), caja(0.1, 0.2, 0.008, x=x, y=0.17, z=z + 0.031, c='#f2d8c8', m='plastico'), caja(0.07, 0.06, 0.01, x=x, y=0.25, z=z + 0.036, c='#c8884a', m='plastico')], 3, 1, 0.15, 0.07, 0.3, 0.07, '#e76a9a', 0.35, cat='ta_juguete', hf=0.5)
regis('bz_pompas', 'Botes de pompas de jabón', u_botella(0.025, 0.14, '#7ab0e8', '#f0c030', '#e76a9a'), 6, 2, 0.06, 0.06, 0.14, 0.2, '#7ab0e8', 0.1)
regis('bz_pelotas_saltarinas', 'Redes de pelotas saltarinas', lambda x, z: [caja(0.18, 0.2, 0.1, x=x, y=0.1, z=z, c='#cfd6d8', m='plastico')] + [esf(0.03, x + dx, 0.05 + dy, z, c=c, m='goma') for dx, dy, c in ((-0.04, 0.0, '#d23a2c'), (0.04, 0.0, '#2f64b4'), (0.0, 0.07, '#f0c030'))], 3, 1, 0.19, 0.11, 0.2, 0.12, '#cfd6d8', 0.15, cat='ta_juguete', hf=0.3)
regis('bz_cargadores', 'Cargadores de móvil en blíster', u_blister(0.1, 0.2, '#2aa6a6', '#eeeae0'), 4, 1, 0.11, 0.05, 0.2, 0.08, '#2aa6a6', 0.06, hf=0.2)
regis('bz_auriculares', 'Auriculares con cable', u_caja(0.12, 0.17, 0.04, '#2f2f32', '#d23a2c', banda=0.4), 4, 2, 0.13, 0.05, 0.17, 0.12, '#2f2f32', 0.12)
regis('bz_fundas_movil', 'Fundas de móvil', lambda x, z: [caja(0.08, 0.16, 0.004, x=x, y=0.085, z=z, c=BRIGHT[int(abs(x * 100)) % 8], m='plastico', r=[-6, 0, 0])], 8, 1, 0.09, 0.03, 0.17, 0.05, '#2f64b4', 0.05, hf=0.4)
regis('bz_pilas', 'Pilas en blíster', u_blister(0.07, 0.18, '#f0c030', '#2f2f32'), 5, 1, 0.08, 0.04, 0.18, 0.06, '#f0c030', 0.05, hf=0.2)
regis('bz_bombillas', 'Cajas de bombillas', u_caja(0.07, 0.12, 0.07, '#eeeae0', '#f0c030', banda=0.4), 5, 2, 0.075, 0.075, 0.12, 0.2, '#eeeae0', 0.08)
regis('bz_alargaderas', 'Alargaderas con enchufes', lambda x, z: [caja(0.36, 0.045, 0.06, x=x, y=0.0225, z=z, c='#eeeae0', m='plastico'), cil(0.07, 0.07, 0.04, x=x, y=0.065, z=z + 0.05, c='#2f2f32', m='goma', seg=8)], 1, 3, 0.36, 0.14, 0.09, 0.24, '#eeeae0', 0.3)
regis('bz_cestos_mimbre', 'Cestos de mimbre', lambda x, z: [cil(0.12, 0.1, 0.12, x=x, y=0.06, z=z, c='#c8a468', m='madera', seg=10), cil(0.125, 0.125, 0.012, x=x, y=0.126, z=z, c='#b08a4a', m='madera', seg=10)], 2, 1, 0.26, 0.26, 0.14, 0.28, '#c8a468', 0.2, mat='madera')
# the stock room
obj('caja_bazar_grande', 'Caja grande de cartón con cinta', 'caja', 6, 'papel', 'superficie', [caja(0.55, 0.38, 0.38, c='#b88a58', m='papel'), caja(0.56, 0.01, 0.06, y=0.385, c='#e0d4b8', m='papel'), caja(0.2, 0.12, 0.004, x=0.1, y=0.2, z=0.192, c='#eeeae0', m='papel')])
obj('torre_cajas_bazar', 'Pila de cajas de cartón de almacén', 'caja', 22, 'papel', 'suelo', [
    caja(0.6, 0.4, 0.4, y=0.2, c='#b88a58', m='papel'), caja(0.55, 0.38, 0.4, x=0.03, y=0.59, c='#a87c4c', m='papel', r=[0, 4, 0]), caja(0.5, 0.35, 0.38, x=-0.02, y=0.955, c='#b88a58', m='papel', r=[0, -3, 0]),
    caja(0.2, 0.1, 0.004, x=0.1, y=0.22, z=0.202, c='#eeeae0', m='papel')], superficies=[{'y': 1.13, 'margen': 0.04}])
obj('taburete_escalon', 'Escalón de plástico', 'mueble', 3, 'plastico', 'suelo', [caja(0.4, 0.03, 0.3, y=0.22, c='#3f9a4a', m='plastico'), caja(0.36, 0.03, 0.18, y=0.1, c='#3f9a4a', m='plastico'), caja(0.03, 0.22, 0.3, x=-0.185, y=0.11, c='#2f7a3a', m='plastico'), caja(0.03, 0.22, 0.3, x=0.185, y=0.11, c='#2f7a3a', m='plastico')])

# ================================================================== THE HARDWARE SHOP (ferretería)
GRIS_AC, VERDE_FE, ROJO_FE = '#8a949c', '#6f8a6a', '#c0392b'
obj('mostrador_ferreteria', 'Mostrador de ferretería (1,2 m)', 'mostrador', 200, 'madera', 'suelo', [
    caja(1.2, 0.92, 0.52, z=-0.03, c='#7d8c78'), caja(1.2, 0.06, 0.7, y=0.97, z=0.0, c='#9a6b3c'), caja(1.2, 0.008, 0.02, y=1.004, z=0.3, c='#c8a040', m='metal'),
    caja(1.1, 0.55, 0.01, y=0.52, z=0.236, c='#6c7a68'), caja(0.4, 0.15, 0.012, x=-0.32, y=0.72, z=0.244, c='#9a6b3c'), caja(0.4, 0.15, 0.012, x=0.32, y=0.72, z=0.244, c='#9a6b3c'),
    caja(0.12, 0.02, 0.02, x=-0.32, y=0.72, z=0.256, c='#c8a040', m='metal'), caja(0.12, 0.02, 0.02, x=0.32, y=0.72, z=0.256, c='#c8a040', m='metal'), caja(1.2, 0.07, 0.01, y=0.035, z=0.236, c='#3c3c40')],
    fijo='estructural', superficies=[{'y': 1.0, 'margen': 0.04}], nota='el mostrador largo de madera con la regla de latón en el borde')
# the wall of little drawers behind the counter: screws, nails, washers
P_ = [caja(1.0, 2.1, 0.33, z=0.165, c='#a88255')]
for fila in range(12):
    for col in range(5):
        c = ('#c9a46e', '#b88a58')[(fila + col) % 2]
        P_ += [caja(0.186, 0.15, 0.012, x=-0.4 + col * 0.2, y=0.14 + fila * 0.17, z=0.336, c=c), caja(0.07, 0.024, 0.004, x=-0.4 + col * 0.2, y=0.17 + fila * 0.17, z=0.344, c='#efe8d4', m='papel')]
obj('cajonera_tornillos', 'Cajonera de tornillos, clavos y arandelas', 'mueble', 95, 'madera', 'pared', P_, fijo=FIJO, superficies=[{'y': 2.1, 'margen': 0.04}], nota='sesenta cajoncitos con su etiqueta')
estantes('estanteria_ferreteria_pared', 'Estantería metálica de pared de ferretería', 1.0, 0.4, [0.25, 0.6, 0.95, 1.3, 1.65, 2.0], 2.3, c='#a2aab0', cp='#c0c6ca', masa=58, borde='#c0392b')
estantes('estanteria_ferreteria_baja', 'Estantería baja de ferretería (bajo los paneles)', 1.0, 0.4, [0.22, 0.55, 0.88, 1.1], 1.1, c='#a2aab0', cp='#c0c6ca', masa=34, borde='#c0392b')
estantes('gondola_ferreteria', 'Góndola de ferretería', 1.0, 0.45, [0.22, 0.58, 0.94, 1.3], 1.55, c='#9aa4aa', cp='#bcc2c6', masa=48, borde='#c0392b', nota='por una cara; de dos en dos, espalda con espalda')

# ---- tools hung on pegboards
def herr_llave(x, y, L, c='#aab0b4'):
    return [caja(0.02, L, 0.006, x=x, y=y - L / 2, z=0.03, c=c, m='metal'), caja(0.045, 0.05, 0.006, x=x, y=y + 0.01, z=0.03, c=c, m='metal'), caja(0.04, 0.045, 0.006, x=x, y=y - L - 0.005, z=0.03, c=c, m='metal')]
def herr_alicate(x, y, c):
    return [caja(0.022, 0.15, 0.012, x=x - 0.012, y=y - 0.09, z=0.032, c=c, m='plastico', r=[0, 0, 6]), caja(0.022, 0.15, 0.012, x=x + 0.012, y=y - 0.09, z=0.032, c=c, m='plastico', r=[0, 0, -6]),
            caja(0.045, 0.085, 0.01, x=x, y=y + 0.01, z=0.032, c='#aab0b4', m='metal')]
def herr_destornillador(x, y, c, L=0.14):
    return [cil(0.014, 0.014, 0.1, x=x, y=y - 0.05, z=0.032, c=c, m='plastico', seg=6), caja(0.006, L, 0.006, x=x, y=y - 0.1 - L / 2, z=0.032, c='#aab0b4', m='metal')]
def herr_martillo(x, y, madera='#8a5a36'):
    return [caja(0.02, 0.3, 0.014, x=x, y=y - 0.17, z=0.032, c=madera), caja(0.11, 0.04, 0.03, x=x, y=y + 0.0, z=0.038, c='#8f969c', m='metal')]
def herr_sierra(x, y, c):
    return [caja(0.07, 0.38, 0.004, x=x, y=y - 0.25, z=0.03, c='#b8bec2', m='metal'), caja(0.04, 0.11, 0.022, x=x, y=y - 0.015, z=0.036, c=c, m='plastico')]
def herr_navaja(x, y, c):
    return [caja(0.07, 0.15, 0.004, x=x, y=y, z=0.026, c='#d8d2c0', m='papel'), caja(0.022, 0.12, 0.014, x=x, y=y, z=0.036, c=c, m='plastico'), caja(0.012, 0.04, 0.006, x=x, y=y + 0.07, z=0.04, c='#b8bec2', m='metal')]
panel('panel_llaves_fijas', 'Panel de llaves fijas y de carraca', 1.0, 0.9, 1.35, [p for i in range(12) for p in herr_llave(-0.44 + i * 0.08, 2.2, 0.19 + 0.02 * (i % 6) if i < 6 else 0.37 - 0.02 * (i - 6))],
      c='#d6cdb4', nota='una llave de cada medida, por orden')
panel('panel_alicates', 'Panel de alicates y tenazas', 1.0, 0.9, 1.35, [p for fila, yy in enumerate((2.18, 1.82)) for i in range(7) for p in herr_alicate(-0.42 + i * 0.14, yy, ('#d23a2c', '#f0c030', '#2f64b4')[(i + fila) % 3])], c='#d6cdb4')
panel('panel_destornilladores', 'Panel de destornilladores', 1.0, 0.9, 1.35, [p for fila, yy in enumerate((2.2, 1.85)) for i in range(11) for p in herr_destornillador(-0.46 + i * 0.092, yy, ('#d23a2c', '#f0c030', '#2f64b4', '#3f9a4a')[(i + fila) % 4], 0.11 + 0.012 * (i % 4))], c='#d6cdb4')
panel('panel_martillos', 'Panel de martillos y mazas', 1.0, 0.9, 1.35, [p for i in range(7) for p in herr_martillo(-0.42 + i * 0.14, 2.2, ('#8a5a36', '#c8a468', '#6a4a2c')[i % 3])] + [
    p for i in range(4) for p in (caja(0.025, 0.32, 0.02, x=-0.33 + i * 0.22, y=1.64, z=0.034, c='#d23a2c', m='plastico'), caja(0.1, 0.06, 0.05, x=-0.33 + i * 0.22, y=1.82, z=0.04, c='#7d8388', m='metal'))], c='#d6cdb4')
panel('panel_sierras', 'Panel de serruchos y sierras', 1.0, 0.9, 1.35, [p for i in range(7) for p in herr_sierra(-0.42 + i * 0.14, 2.2, ('#d23a2c', '#2f64b4', '#f0c030')[i % 3])], c='#d6cdb4')
panel('panel_navajas', 'Panel de navajas y cuchillos multiusos', 1.0, 0.7, 1.45, [p for fila, yy in enumerate((2.0, 1.76)) for i in range(7) for p in herr_navaja(-0.42 + i * 0.14, yy, ('#2f2f32', '#d23a2c', '#2f64b4', '#3f9a4a')[(i + fila) % 4])], c='#d6cdb4', nota='navajas, 12 €')
panel('panel_herramientas', 'Panel de herramientas manuales surtidas', 1.0, 0.9, 1.35, [
    p for i in range(5) for p in herr_llave(-0.42 + i * 0.07, 2.2, 0.24 + 0.02 * i)] + [p for i in range(3) for p in herr_alicate(-0.05 + i * 0.13, 2.18, ('#d23a2c', '#f0c030', '#2f64b4')[i])] + [
    p for i in range(4) for p in herr_destornillador(-0.4 + i * 0.1, 1.75, ('#d23a2c', '#f0c030', '#2f64b4', '#3f9a4a')[i])] + [p for i in range(3) for p in herr_martillo(0.08 + i * 0.14, 1.78)], c='#d6cdb4', nota='herramientas, 15 €')
# the key-cutting board (blanks) and the machine
P_ = []
for fila in range(7):
    for col in range(8):
        P_.append(caja(0.03, 0.06, 0.004, x=-0.24 + col * 0.068, y=1.55 + fila * 0.1, z=0.026, c=('#c8a040', '#aab0b4', '#d8d4cc')[(fila + col) % 3], m='metal'))
        P_.append(caja(0.02, 0.025, 0.004, x=-0.24 + col * 0.068, y=1.6 + fila * 0.1, z=0.026, c='#2f2f32', m='plastico'))
panel('tablero_llaves', 'Tablero de llaves en blanco', 0.62, 0.76, 1.5, P_, c='#3a3d42', masa=4, nota='las llaves en blanco para copiar')
obj('maquina_llaves', 'Máquina de duplicar llaves', 'ta_herramienta', 14, 'metal', 'superficie', [
    caja(0.5, 0.2, 0.34, c='#5a7a6a', m='metal'), caja(0.28, 0.16, 0.2, x=-0.08, y=0.28, z=-0.04, c='#5a7a6a', m='metal'), caja(0.07, 0.07, 0.07, x=0.12, y=0.215, z=0.1, c='#8f969c', m='metal'), caja(0.07, 0.07, 0.07, x=-0.1, y=0.215, z=0.1, c='#8f969c', m='metal'),
    cil(0.04, 0.04, 0.012, x=0.12, y=0.255, z=0.1, c='#c3c7ca', m='metal', seg=10), cil(0.04, 0.04, 0.012, x=-0.1, y=0.255, z=0.1, c='#c3c7ca', m='metal', seg=10), caja(0.04, 0.03, 0.04, x=0.2, y=0.215, z=-0.1, c='#d23a2c', m='plastico')], modificadores=['USE'], nota='para copiar llaves al momento')
obj('expositor_linternas_mostrador', 'Expositor de linternas de mostrador', 'ta_expositor', 3, 'plastico', 'superficie', [
    caja(0.4, 0.02, 0.18, c='#2f2f32', m='plastico'), caja(0.4, 0.22, 0.01, y=0.13, z=-0.085, c='#d23a2c', m='plastico')] + [
    p for i, c in enumerate(('#2f64b4', '#f0c030', '#2f2f32', '#3f9a4a')) for p in (cil(0.022, 0.026, 0.2, x=-0.15 + i * 0.1, y=0.12, z=-0.03, c=c, m='plastico', seg=7, r=[-8, 0, 0]), cil(0.034, 0.026, 0.045, x=-0.15 + i * 0.1, y=0.23, z=-0.04, c='#aab0b4', m='metal', seg=7, r=[-8, 0, 0]))], nota='linternas, 9 €')
# ladders
def escalera_tijera():
    P = []
    for sx in (-1, 1):
        P += [caja(0.04, 1.52, 0.022, x=sx * 0.22, y=0.7474, z=0.18, c='#b8bec2', m='metal', r=[-11.3, 0, 0]), caja(0.04, 1.52, 0.022, x=sx * 0.22, y=0.7474, z=-0.18, c='#b8bec2', m='metal', r=[11.3, 0, 0])]
    for y in (0.3, 0.6, 0.9, 1.2):
        zf = 0.18 - (y - 0.75) * 0.2
        P += [caja(0.44, 0.03, 0.1, y=y, z=zf, c='#9aa2a8', m='metal')]
    P += [caja(0.48, 0.03, 0.34, y=1.5, z=0.0, c='#d23a2c', m='plastico'), caja(0.4, 0.02, 0.02, y=0.5, z=-0.2, c='#9aa2a8', m='metal')]
    return P
obj('escalera_tijera', 'Escalera de tijera de aluminio', 'mueble', 7, 'metal', 'suelo', escalera_tijera(), nota='cuatro peldaños')
obj('escalera_extensible_colgada', 'Escalera extensible colgada en la pared', 'mueble', 8, 'metal', 'pared', [
    caja(2.4, 0.04, 0.03, y=2.34, z=0.06, c='#b8bec2', m='metal'), caja(2.4, 0.04, 0.03, y=2.06, z=0.06, c='#b8bec2', m='metal')] + [caja(0.025, 0.3, 0.025, x=-1.1 + i * 0.28, y=2.2, z=0.06, c='#9aa2a8', m='metal') for i in range(9)] + [
    caja(0.04, 0.4, 0.05, x=sx * 0.9, y=2.2, z=0.03, c='#5a5e62', m='metal') for sx in (-1, 1)], fijo=FIJO)
# stands on the floor
def tin(x, y, z, c, r=0.085, h=0.19):
    return [cil(r, r, h, x=x, y=y + h / 2, z=z, c='#e8e4d8', m='metal', seg=8), cil(r + 0.002, r + 0.002, h * 0.34, x=x, y=y + h * 0.5, z=z, c=c, m='papel', seg=8), cil(r + 0.006, r + 0.006, 0.012, x=x, y=y + h - 0.006, z=z, c='#aab0b4', m='metal', seg=8)]
P_ = [caja(0.7, 0.04, 0.5, y=0.02, c='#8a5a36')]
for (x, z, k) in [(sx * 0.18, sz * 0.1, 0) for sx in (-1, 0, 1) for sz in (-1, 1)]:
    P_ += tin(x, 0.04, z, ('#d23a2c', '#2f64b4', '#3f9a4a', '#f0c030', '#eeeae0', '#ee8a2a')[(int(x * 10) + int(z * 10) + 5) % 6])
for x in (-0.09, 0.09):
    for z in (-0.1, 0.1): P_ += tin(x, 0.23, z, ('#2f64b4', '#d23a2c', '#3f9a4a', '#f0c030')[(int(x * 10) + int(z * 10) + 4) % 4])
for z in (-0.1, 0.1): P_ += tin(0.0, 0.42, z, '#eeeae0')
obj('torre_botes_pintura', 'Torre de botes de pintura sobre un palé', 'ta_expositor', 24, 'metal', 'suelo', P_, nota='doce botes de colores')
obj('expositor_herramientas_jardin', 'Rastrillero de herramientas de jardín', 'ta_herramienta', 14, 'metal', 'suelo', [
    caja(0.9, 0.03, 0.3, y=0.015, c='#5a5e62', m='metal'), caja(0.9, 0.04, 0.03, y=1.25, z=-0.1, c='#5a5e62', m='metal'), caja(0.03, 1.28, 0.03, x=-0.44, y=0.64, z=-0.1, c='#5a5e62', m='metal'), caja(0.03, 1.28, 0.03, x=0.44, y=0.64, z=-0.1, c='#5a5e62', m='metal')] + [
    p for i in range(6) for p in (cil(0.015, 0.015, 1.45, x=-0.36 + i * 0.144, y=0.745, z=-0.04, c='#c8a468', m='madera', seg=5),
                                  (caja(0.34, 0.04, 0.012, x=-0.36 + i * 0.144, y=0.08, z=0.0, c='#8f969c', m='metal') if i % 3 == 0 else caja(0.2, 0.28, 0.012, x=-0.36 + i * 0.144, y=0.2, z=0.0, c='#8f969c', m='metal') if i % 3 == 1 else caja(0.15, 0.12, 0.012, x=-0.36 + i * 0.144, y=0.12, z=0.0, c='#8f969c', m='metal')))],
    nota='rastrillos, palas y azadas')
obj('expositor_escobas', 'Expositor de escobas y fregonas', 'ta_herramienta', 8, 'plastico', 'suelo', [
    caja(0.8, 0.03, 0.3, y=0.015, c='#5a5e62', m='metal'), caja(0.8, 0.04, 0.03, y=1.15, z=-0.1, c='#5a5e62', m='metal'), caja(0.03, 1.18, 0.03, x=-0.39, y=0.59, z=-0.1, c='#5a5e62', m='metal'), caja(0.03, 1.18, 0.03, x=0.39, y=0.59, z=-0.1, c='#5a5e62', m='metal')] + [
    p for i in range(6) for p in (cil(0.012, 0.012, 1.3, x=-0.32 + i * 0.128, y=0.68, z=-0.04, c=('#c8a468', '#d23a2c', '#2f64b4')[i % 3], m='plastico', seg=5),
                                  (caja(0.28, 0.05, 0.07, x=-0.32 + i * 0.128, y=0.04, z=0.0, c=BRIGHT[i], m='plastico') if i % 2 == 0 else cil(0.07, 0.07, 0.1, x=-0.32 + i * 0.128, y=0.08, z=0.0, c='#e8e4d8', m='tela', seg=8)))], nota='escobas, recogedores y fregonas')
obj('carrete_manguera', 'Carrete de manguera de jardín', 'ta_herramienta', 9, 'plastico', 'suelo', [
    caja(0.5, 0.03, 0.36, y=0.015, c='#2f2f32', m='plastico'), cil(0.27, 0.27, 0.02, x=-0.15, y=0.33, c='#2f7a3a', m='plastico', seg=14, r=[0, 0, 90]), cil(0.27, 0.27, 0.02, x=0.15, y=0.33, c='#2f7a3a', m='plastico', seg=14, r=[0, 0, 90]),
    cil(0.22, 0.22, 0.26, y=0.33, c='#3f9a4a', m='plastico', seg=14, r=[0, 0, 90]), caja(0.03, 0.5, 0.03, x=-0.15, y=0.25, z=-0.12, c='#2f2f32', m='plastico'), caja(0.03, 0.5, 0.03, x=0.15, y=0.25, z=-0.12, c='#2f2f32', m='plastico'),
    caja(0.34, 0.03, 0.03, y=0.55, z=-0.12, c='#2f2f32', m='plastico')], nota='30 metros')
obj('carretilla_obra', 'Carretilla de obra', 'ta_herramienta', 14, 'metal', 'suelo', [
    caja(0.6, 0.1, 0.74, y=0.38, z=0.0, c='#d23a2c', m='metal'), caja(0.62, 0.2, 0.02, y=0.5, z=0.37, c='#d23a2c', m='metal', r=[-14, 0, 0]), caja(0.62, 0.2, 0.02, y=0.5, z=-0.37, c='#d23a2c', m='metal', r=[14, 0, 0]),
    caja(0.02, 0.2, 0.74, x=-0.31, y=0.5, c='#d23a2c', m='metal', r=[0, 0, 12]), caja(0.02, 0.2, 0.74, x=0.31, y=0.5, c='#d23a2c', m='metal', r=[0, 0, -12]),
    caja(0.03, 0.03, 0.7, x=-0.2, y=0.38, z=-0.62, c='#7a7e82', m='metal', r=[-6, 0, 0]), caja(0.03, 0.03, 0.7, x=0.2, y=0.38, z=-0.62, c='#7a7e82', m='metal', r=[-6, 0, 0]),
    cil(0.2, 0.2, 0.05, x=0.0, y=0.2, z=0.5, c='#2f2f32', m='goma', seg=12, r=[0, 0, 90]), cil(0.14, 0.14, 0.052, x=0.0, y=0.2, z=0.5, c='#aab0b4', m='metal', seg=12, r=[0, 0, 90]),
    caja(0.03, 0.18, 0.03, x=-0.23, y=0.12, z=-0.42, c='#7a7e82', m='metal'), caja(0.03, 0.18, 0.03, x=0.23, y=0.12, z=-0.42, c='#7a7e82', m='metal')], nota='carretilla de albañil')
obj('cubos_albanil_pila', 'Cubos de albañil apilados', 'recipiente', 3.6, 'goma', 'suelo', [
    cil(0.17, 0.12, 0.26, y=0.13, c='#2f2f32', m='goma', seg=10), cil(0.17, 0.12, 0.26, y=0.25, c='#3a3a3e', m='goma', seg=10, x=0.01), cil(0.17, 0.12, 0.26, y=0.37, c='#2f2f32', m='goma', seg=10)])
P_ = [caja(1.2, 0.12, 0.8, y=0.06, c='#b08a58')]
for capa in range(3):
    for i in range(2):
        for j in range(2):
            P_ += [caja(0.5, 0.12, 0.34, x=-0.28 + i * 0.56, y=0.18 + capa * 0.125, z=-0.2 + j * 0.4, c='#b8b4a8', m='papel', r=[0, 3 * ((i + j + capa) % 3 - 1), 0]), caja(0.18, 0.121, 0.34, x=-0.28 + i * 0.56, y=0.18 + capa * 0.125, z=-0.2 + j * 0.4, c='#6f8a6a', m='papel')]
obj('palet_sacos_cemento', 'Palé de sacos de cemento', 'ta_expositor', 140, 'papel', 'suelo', P_, nota='doce sacos de 25 kg')
def planta_geranio(x, y, z, flor):
    return [cil(0.055, 0.04, 0.09, x=x, y=y + 0.045, z=z, c='#b8683a', m='ceramica', seg=8), cil(0.07, 0.05, 0.07, x=x, y=y + 0.125, z=z, c='#4f8a3a', m='comida', seg=7)] + [
        caja(0.035, 0.03, 0.035, x=x + dx, y=y + 0.18 + dy, z=z + dz, c=flor, m='comida', r=[0, 25 * k, 0]) for k, (dx, dy, dz) in enumerate(((0.0, 0.03, 0.0), (-0.035, 0.0, 0.02), (0.035, 0.005, -0.02), (0.0, 0.0, 0.04)))]
P_ = [caja(0.7, 0.03, 0.34, y=0.3, c='#c8a468'), caja(0.7, 0.03, 0.34, y=0.62, c='#c8a468'), caja(0.7, 0.03, 0.34, y=0.94, c='#c8a468')] + patas(0.7, 0.34, 0.94, c='#8a5a36')
for lv, yy in enumerate((0.315, 0.635, 0.955)):
    for i in range(4): P_ += planta_geranio(-0.26 + i * 0.173, yy, 0.0, ('#d23a2c', '#e76a9a', '#eeeae0', '#d8402a')[(i + lv) % 4])
obj('expositor_geranios', 'Escalera de geranios en maceta', 'ta_expositor', 18, 'madera', 'suelo', P_, nota='geranios, 4 €')
def maceta_grande(x, z, h, c='#b8683a', hoja='#4f8a3a', flor=None):
    P = [cil(0.15, 0.1, h, x=x, y=h / 2, z=z, c=c, m='ceramica', seg=10), cil(0.16, 0.16, 0.03, x=x, y=h - 0.015, z=z, c=oscuro(c, 0.9), m='ceramica', seg=10)]
    P += [cil(0.03, 0.03, 0.35, x=x, y=h + 0.17, z=z, c='#5a7a3a', m='comida', seg=5), cil(0.16, 0.05, 0.25, x=x, y=h + 0.3, z=z, c=hoja, m='comida', seg=7)]
    if flor: P += [caja(0.05, 0.04, 0.05, x=x + dx, y=h + 0.43 + dy, z=z + dz, c=flor, m='comida') for dx, dy, dz in ((0, 0, 0), (0.07, -0.04, 0.03), (-0.06, -0.05, -0.03))]
    return P
obj('macetas_terracota', 'Macetas grandes de terracota con plantas', 'ta_expositor', 22, 'ceramica', 'suelo', [caja(1.0, 0.1, 0.5, y=0.05, c='#b08a58')] + maceta_grande(-0.28, 0.0, 0.3, hoja='#3f7a3a', flor='#e76a9a') + maceta_grande(0.05, 0.05, 0.26, c='#a85a30', hoja='#5a9a3a') + maceta_grande(0.32, -0.02, 0.32, hoja='#2f6a3a', flor='#f0c030'), nota='plantas de interior y exterior, 14 €')
obj('rotulo_ferreteria', 'Rótulo interior de la ferretería', 'decoracion', 3, 'madera', 'pared', [caja(1.6, 0.4, 0.03, y=2.5, z=0.015, c='#2f3a2c'), plano(1.54, 0.34, y=2.5, z=0.033, tex={'tipo': 'ta_rotulo_ferreteria', 'rotulo_local': True})])
obj('cartel_llaves', 'Cartel de copia de llaves', 'cuadro', 0.5, 'papel', 'pared', [caja(0.6, 0.3, 0.012, y=2.3, z=0.006, c='#f0c030', m='papel'), plano(0.56, 0.26, y=2.3, z=0.0135, tex={'tipo': 'ta_cartel_llaves'})])
obj('cartel_pinturas', 'Cartel de pinturas y barnices', 'cuadro', 0.6, 'papel', 'pared', [caja(0.6, 0.4, 0.012, y=1.75, z=0.006, c='#eeeae0', m='papel'), plano(0.56, 0.36, y=1.75, z=0.0135, tex={'tipo': 'ta_cartel_pinturas'})])

# ---- what the hardware shop sells (facings)
def u_tin(c, r=0.085, h=0.19, tapa='#aab0b4'):
    def f(x, z):
        return [cil(r, r, h, x=x, y=h / 2, z=z, c='#e8e4d8', m='metal', seg=8), cil(r + 0.002, r + 0.002, h * 0.34, x=x, y=h * 0.5, z=z, c=c, m='papel', seg=8), cil(r + 0.006, r + 0.006, 0.012, x=x, y=h - 0.006, z=z, c=tapa, m='metal', seg=8)]
    return f
for k, (n_, c) in {'blanca': ('blanca', '#eeeae0'), 'roja': ('roja', '#d23a2c'), 'azul': ('azul', '#2f64b4'), 'verde': ('verde', '#3f9a4a'), 'amarilla': ('amarilla', '#f0c030'), 'gris': ('gris', '#8a949c')}.items():
    regis('fe_pintura_' + k, 'Botes de pintura %s' % n_, u_tin(c), 3, 2, 0.19, 0.19, 0.19, 0.38, c, 1.5, mat='metal')
regis('fe_barniz', 'Botes de barniz para madera', u_tin('#8a5a36', r=0.06, h=0.14), 4, 2, 0.13, 0.13, 0.14, 0.26, '#8a5a36', 0.9, mat='metal')
regis('fe_pintura_cubo', 'Cubos grandes de pintura plástica', lambda x, z: [cil(0.14, 0.13, 0.27, x=x, y=0.135, z=z, c='#eeeae0', m='plastico', seg=10), cil(0.145, 0.145, 0.02, x=x, y=0.27, z=z, c='#2f64b4', m='plastico', seg=10), caja(0.2, 0.03, 0.01, x=x, y=0.27, z=z + 0.14, c='#aab0b4', m='metal')],
      2, 1, 0.3, 0.3, 0.28, 0.3, '#eeeae0', 5.0, mat='plastico', clase=None)
regis('fe_cajas_tornillos', 'Cajitas de tornillos', u_caja(0.1, 0.06, 0.07, '#c9a46e', '#d23a2c', banda=0.4), 4, 2, 0.105, 0.075, 0.06, 0.28, '#c9a46e', 0.25, mat='papel')
regis('fe_cajas_clavos_puntas', 'Cajas de puntas y clavos', u_caja(0.09, 0.05, 0.12, '#eeeae0', '#2f64b4', banda=0.5), 4, 2, 0.095, 0.125, 0.05, 0.28, '#eeeae0', 0.4, mat='papel')
regis('fe_tacos', 'Tacos y tornillos en blíster', u_blister(0.08, 0.17, '#f0c030', '#eeeae0'), 5, 1, 0.09, 0.04, 0.17, 0.07, '#f0c030', 0.06, hf=0.2)
regis('fe_bisagras', 'Bisagras y escuadras en caja', u_caja(0.11, 0.05, 0.09, '#2f64b4', '#eeeae0', banda=0.4), 3, 2, 0.115, 0.095, 0.05, 0.28, '#2f64b4', 0.35, mat='papel')
regis('fe_candados', 'Candados en blíster', lambda x, z: [caja(0.08, 0.14, 0.004, x=x, y=0.07, z=z, c='#2f2f32', m='papel'), caja(0.05, 0.05, 0.03, x=x, y=0.06, z=z + 0.016, c='#c8a040', m='metal'), cil(0.018, 0.018, 0.045, x=x, y=0.1, z=z + 0.016, c='#aab0b4', m='metal', seg=6)], 5, 1, 0.09, 0.04, 0.14, 0.07, '#2f2f32', 0.2, mat='metal', hf=0.2)
regis('fe_silicona', 'Cartuchos de silicona', lambda x, z: [cil(0.021, 0.021, 0.2, x=x, y=0.1, z=z, c='#eeeae0', m='plastico', seg=7), cil(0.0, 0.021, 0.05, x=x, y=0.225, z=z, c='#c8a040', m='plastico', seg=7), cil(0.022, 0.022, 0.03, x=x, y=0.06, z=z, c='#d23a2c', m='papel', seg=7)],
      7, 2, 0.05, 0.05, 0.25, 0.14, '#eeeae0', 0.3, hf=0.7)
regis('fe_cola', 'Botes de cola blanca', u_botella(0.03, 0.17, '#eeeae0', '#f0c030', '#d23a2c'), 5, 2, 0.07, 0.07, 0.17, 0.2, '#eeeae0', 0.4)
regis('fe_cintas', 'Rollos de cinta aislante y de carrocero', lambda x, z: [cil(0.04, 0.04, 0.05, x=x, y=0.025, z=z, c=BRIGHT[int(abs(x * 100)) % 8], m='plastico', seg=9), cil(0.025, 0.025, 0.052, x=x, y=0.026, z=z, c='#d8d2c0', m='papel', seg=9)], 6, 3, 0.085, 0.085, 0.05, 0.28, '#d23a2c', 0.08)
regis('fe_cable_bobinas', 'Bobinas de cable eléctrico', lambda x, z: [cil(0.075, 0.075, 0.012, x=x, y=0.075, z=z - 0.025, c='#7a5a36', m='madera', seg=10, r=[90, 0, 0]), cil(0.075, 0.075, 0.012, x=x, y=0.075, z=z + 0.025, c='#7a5a36', m='madera', seg=10, r=[90, 0, 0]),
                                                                  cil(0.06, 0.06, 0.04, x=x, y=0.075, z=z, c=('#d23a2c', '#2f2f32', '#2f64b4', '#c8884a')[int(abs(x * 100)) % 4], m='plastico', seg=10, r=[90, 0, 0])], 4, 1, 0.16, 0.07, 0.15, 0.1, '#2f64b4', 0.5, hf=0.4)
regis('fe_enchufes', 'Cajas de enchufes e interruptores', u_caja(0.08, 0.09, 0.05, '#eeeae0', '#f0c030', banda=0.3), 5, 2, 0.085, 0.055, 0.09, 0.22, '#eeeae0', 0.15)
regis('fe_grifos', 'Grifos de cocina en caja', u_caja(0.15, 0.2, 0.08, '#2f64b4', '#c3c7ca', banda=0.4), 3, 1, 0.16, 0.09, 0.2, 0.18, '#2f64b4', 0.8, mat='papel', hf=0.7)
regis('fe_tuberias_pvc', 'Codos y manguitos de PVC', lambda x, z: [cil(0.03, 0.03, 0.09, x=x, y=0.045, z=z, c='#8a949c', m='plastico', seg=7, r=[0, 0, 90]), cil(0.03, 0.03, 0.09, x=x + 0.045, y=0.09, z=z, c='#8a949c', m='plastico', seg=7), cil(0.034, 0.034, 0.02, x=x, y=0.045, z=z, c='#c8c8c0', m='plastico', seg=7, r=[0, 0, 90])],
      5, 2, 0.12, 0.08, 0.12, 0.22, '#8a949c', 0.2)
regis('fe_guantes_trabajo', 'Guantes de trabajo', lambda x, z: [caja(0.09, 0.2, 0.025, x=x, y=0.1, z=z, c=('#f0c030', '#2f64b4', '#ee8a2a', '#3f9a4a')[int(abs(x * 100)) % 4], m='tela', r=[-4, 0, 0]), caja(0.07, 0.08, 0.028, x=x, y=0.045, z=z, c='#eeeae0', m='tela')], 6, 1, 0.1, 0.03, 0.2, 0.06, '#f0c030', 0.12, hf=0.3)
regis('fe_tijeras_poda', 'Tijeras de podar', lambda x, z: [caja(0.07, 0.22, 0.004, x=x, y=0.11, z=z, c='#2f2f32', m='papel'), caja(0.03, 0.12, 0.02, x=x - 0.012, y=0.07, z=z + 0.012, c='#d23a2c', m='plastico'), caja(0.03, 0.12, 0.02, x=x + 0.012, y=0.07, z=z + 0.012, c='#d23a2c', m='plastico'), caja(0.02, 0.09, 0.008, x=x, y=0.17, z=z + 0.012, c='#aab0b4', m='metal')], 5, 1, 0.09, 0.04, 0.22, 0.08, '#2f2f32', 0.25, hf=0.2)
regis('fe_regaderas', 'Regaderas de plástico', lambda x, z: [cil(0.09, 0.09, 0.19, x=x, y=0.095, z=z, c='#3f9a4a', m='plastico', seg=10), cil(0.012, 0.014, 0.26, x=x + 0.13, y=0.15, z=z, c='#3f9a4a', m='plastico', seg=6, r=[0, 0, 45]), cil(0.03, 0.03, 0.03, x=x + 0.22, y=0.26, z=z, c='#2f7a3a', m='plastico', seg=6, r=[0, 0, 45]), caja(0.02, 0.2, 0.03, x=x - 0.1, y=0.15, z=z, c='#3f9a4a', m='plastico')],
      2, 1, 0.34, 0.2, 0.28, 0.25, '#3f9a4a', 0.5, hf=0.4)
regis('fe_abonos', 'Sacos de abono', lambda x, z: [caja(0.2, 0.28, 0.09, x=x, y=0.14, z=z, c='#c8b48a', m='papel'), caja(0.2, 0.08, 0.092, x=x, y=0.22, z=z, c='#3f9a4a', m='papel')], 3, 1, 0.21, 0.1, 0.28, 0.2, '#c8b48a', 1.5, hf=0.9)
regis('fe_insecticidas', 'Sprays insecticidas y herbicidas', u_botella(0.032, 0.26, '#eeeae0', '#d23a2c', '#d23a2c'), 5, 2, 0.07, 0.07, 0.26, 0.2, '#eeeae0', 0.5)
regis('fe_maletines', 'Maletines de herramientas', lambda x, z: [caja(0.4, 0.17, 0.17, x=x, y=0.085, z=z, c='#d23a2c', m='plastico'), caja(0.4, 0.012, 0.17, x=x, y=0.176, z=z, c='#2f2f32', m='plastico'), caja(0.2, 0.025, 0.025, x=x, y=0.2, z=z, c='#2f2f32', m='plastico')], 2, 1, 0.42, 0.18, 0.21, 0.2, '#d23a2c', 3.0, hf=0.8)
regis('fe_taladros_caja', 'Taladros en su maletín', lambda x, z: [caja(0.36, 0.11, 0.28, x=x, y=0.055, z=z, c='#2f64b4', m='plastico'), caja(0.36, 0.012, 0.28, x=x, y=0.116, z=z, c='#2f2f32', m='plastico'), caja(0.12, 0.012, 0.06, x=x, y=0.125, z=z + 0.05, c='#eeeae0', m='papel')], 2, 1, 0.38, 0.3, 0.13, 0.3, '#2f64b4', 3.5, hf=0.8)
regis('fe_brocas', 'Estuches de brocas', lambda x, z: [caja(0.2, 0.025, 0.12, x=x, y=0.0125, z=z, c='#2f2f32', m='plastico')] + [cil(0.005, 0.005, 0.1, x=x - 0.07 + 0.02 * i, y=0.032, z=z, c='#c8a040', m='metal', seg=4, r=[90, 0, 0]) for i in range(8)], 2, 3, 0.21, 0.13, 0.04, 0.3, '#2f2f32', 0.3)
regis('fe_niveles_metros', 'Niveles y metros plegables', lambda x, z: [caja(0.26, 0.04, 0.025, x=x, y=0.02, z=z, c='#f0c030', m='plastico'), caja(0.2, 0.012, 0.02, x=x, y=0.046, z=z, c='#2f2f32', m='plastico'), caja(0.06, 0.06, 0.04, x=x + 0.14, y=0.03, z=z, c='#d23a2c', m='plastico')], 2, 4, 0.34, 0.06, 0.06, 0.28, '#f0c030', 0.3)
regis('fe_brochas', 'Brochas y rodillos', lambda x, z: [caja(0.05, 0.2, 0.012, x=x, y=0.14, z=z, c=('#c8a468', '#d23a2c')[int(abs(x * 100)) % 2], m='madera'), caja(0.07, 0.07, 0.025, x=x, y=0.035, z=z, c='#f0e8c8', m='tela')] + [caja(0.012, 0.012, 0.12, x=x + 0.07, y=0.125, z=z, c='#aab0b4', m='metal'), cil(0.03, 0.03, 0.12, x=x + 0.07, y=0.065, z=z, c='#eeeae0', m='tela', seg=7, r=[0, 0, 90])],
      4, 2, 0.15, 0.06, 0.24, 0.2, '#c8a468', 0.25, hf=0.4)

# ================================================================== THE BOOKSHOP (librería-papelería)
MADERA_L, MADERA_L2 = '#8a5a36', '#a06c40'
obj('mostrador_libreria', 'Mostrador de la librería (0,9 m)', 'mostrador', 140, 'madera', 'suelo', [
    caja(0.9, 0.88, 0.5, z=-0.04, c='#5a3a22'), caja(0.9, 0.05, 0.62, y=0.925, z=0.0, c='#7a4a28'), caja(0.8, 0.5, 0.01, y=0.5, z=0.216, c='#6a4528'), caja(0.9, 0.025, 0.025, y=0.2, z=0.25, c='#c8a040', m='metal'),
    caja(0.9, 0.07, 0.01, y=0.035, z=0.216, c='#2f2f32')], fijo='estructural', superficies=[{'y': 0.95, 'margen': 0.04}], nota='el mostrador de nogal con el pasamanos de latón')
estantes('estanteria_libros_pared', 'Librería de pared de madera (siete baldas)', 1.0, 0.32, [0.18, 0.5, 0.82, 1.14, 1.46, 1.78, 2.1], 2.2, c=MADERA_L, cp=MADERA_L2, masa=70, zocalo=0.12, tapa=True,
         nota='baldas de 31 cm: caben los libros de todos los tamaños')
estantes('estanteria_libros_baja', 'Librería baja de madera', 1.0, 0.32, [0.2, 0.5, 0.8, 1.1], 1.1, c=MADERA_L, cp=MADERA_L2, masa=40, zocalo=0.1)
estantes('estanteria_libros_isla', 'Módulo de librería de isla (por una cara)', 1.0, 0.32, [0.22, 0.55, 0.88, 1.21], 1.34, c=MADERA_L, cp=MADERA_L2, masa=44, zocalo=0.1, tapa=True, nota='de dos en dos, espalda con espalda')
estantes('estanteria_papeleria_pared', 'Estantería de papelería de pared', 1.0, 0.36, [0.2, 0.52, 0.84, 1.16, 1.48, 1.8], 2.0, c='#d8d4c8', cp='#eeeae0', masa=48, borde='#2f64b4')

# ---- the books: rows of spines in a palette (the shelf's 'products'), random heights, widths and the odd lean
PAL = {'rojos': ['#a8322a', '#c0453a', '#8a2a26', '#d8806a', '#e8d8b8'], 'azules': ['#27406e', '#3a5a8a', '#1f3258', '#6a8ab0', '#e8e0cc'], 'verdes': ['#2f5a3a', '#4a7a4e', '#1f3e2a', '#8aa878', '#e8e0cc'],
       'ocres': ['#c8a040', '#a8803a', '#e0c070', '#8a6a30', '#3a2a1a'], 'negros': ['#2f2f34', '#3a3a40', '#4a4a52', '#6a6a72', '#b8b0a0'], 'crema': ['#e8dcc0', '#efe6cf', '#d8c8a0', '#c8b890', '#a89870'],
       'morados': ['#5a3a7a', '#7a5a9a', '#3e2a58', '#b8a0c8', '#e8e0cc'], 'granates': ['#6a2230', '#8a3040', '#4a1a26', '#b86a78', '#e0d4b8'], 'mixtos_a': ['#a8322a', '#27406e', '#c8a040', '#2f5a3a', '#e8dcc0'],
       'mixtos_b': ['#5a3a7a', '#d8806a', '#3a5a8a', '#4a7a4e', '#2f2f34'], 'vivos': ['#d23a2c', '#2f64b4', '#f0c030', '#3f9a4a', '#e76a9a', '#ee8a2a', '#2aa6a6'], 'turquesas': ['#2a8a8a', '#4aa6a0', '#1f6a6a', '#8ac8c0', '#e8e0cc'],
       'grises': ['#8a8f96', '#a8adb4', '#6a6f76', '#c8ccd0', '#e8e8e4']}
def fila_libros(id, nombre, pal, n, hmin, hmax, wmin, wmax, prof=0.21, seed=1, inclinado=True, banda=0.45, tope=0.36):
    r = random.Random(seed)
    ws = [r.uniform(wmin, wmax) for _ in range(n)]
    while sum(ws) > tope - 0.01: ws.pop()
    x, P = -sum(ws) / 2, []
    for i, w in enumerate(ws):
        h, c = r.uniform(hmin, hmax), pal[r.randrange(len(pal))]
        P.append(caja(w * 0.97, h, prof, x=x + w / 2, y=h / 2, z=0.0, c=c, m='papel'))
        if r.random() < banda: P.append(caja(w * 0.97 + 0.002, 0.025, prof + 0.002, x=x + w / 2, y=h * r.uniform(0.62, 0.86), z=0.0, c=r.choice(('#e0c070', '#e8e0cc', '#2f2f34')), m='papel'))
        x += w
    if inclinado:   # (the last one leans on its neighbour)
        h, c = r.uniform(hmin, hmax), pal[r.randrange(len(pal))]
        wl = ws[-1] * 0.97
        P.append(caja(wl, h, prof, x=x + 0.03, y=h / 2 * math.cos(math.radians(9)) + wl / 2 * math.sin(math.radians(9)) + 0.0004, z=0.0, c=c, m='papel', r=[0, 0, -9]))
    obj(id, nombre, 'ta_libro', round(len(ws) * 0.4 + 0.4, 2), 'papel', 'superficie', P)
for k, (nom, pal_, n, hmin, hmax, wmin, wmax, sd) in {
        'rojos': ('rojos', 'rojos', 11, 0.2, 0.27, 0.024, 0.04, 1), 'azules': ('azules', 'azules', 11, 0.2, 0.27, 0.024, 0.04, 2), 'verdes': ('verdes', 'verdes', 11, 0.2, 0.27, 0.024, 0.04, 3),
        'ocres': ('ocres', 'ocres', 10, 0.21, 0.28, 0.026, 0.042, 4), 'negros': ('negros (novela negra)', 'negros', 12, 0.19, 0.24, 0.02, 0.034, 5), 'crema': ('de tapa crema', 'crema', 11, 0.2, 0.26, 0.022, 0.04, 6),
        'morados': ('morados', 'morados', 11, 0.2, 0.27, 0.024, 0.04, 7), 'granates': ('granates', 'granates', 10, 0.2, 0.27, 0.026, 0.042, 8), 'mixtos_a': ('de colores variados', 'mixtos_a', 12, 0.19, 0.28, 0.02, 0.036, 9),
        'mixtos_b': ('de colores mezclados', 'mixtos_b', 12, 0.19, 0.28, 0.02, 0.036, 10), 'infantiles': ('infantiles de colores vivos', 'vivos', 8, 0.2, 0.26, 0.012, 0.022, 11),
        'turquesas': ('turquesas', 'turquesas', 11, 0.2, 0.27, 0.024, 0.04, 12), 'grises': ('de tapa gris', 'grises', 11, 0.2, 0.26, 0.022, 0.038, 13),
        'bolsillo': ('de bolsillo', 'mixtos_a', 14, 0.15, 0.19, 0.014, 0.022, 14), 'enciclopedia': ('enciclopedia', 'granates', 7, 0.26, 0.28, 0.04, 0.05, 15), 'atlas': ('atlas y obras grandes', 'azules', 6, 0.26, 0.28, 0.045, 0.055, 16)}.items():
    fila_libros('lb_libros_' + k, 'Libros %s' % nom, PAL[pal_], n, hmin, hmax, wmin, wmax, seed=sd, prof=0.24 if k in ('atlas', 'enciclopedia') else 0.2)
def pila_libros(id, nombre, cols, n, w, d, seed):
    r = random.Random(seed)
    P, y = [], 0.0
    for i in range(n):
        h = r.uniform(0.025, 0.04); ww, dd = w * r.uniform(0.9, 1.0), d * r.uniform(0.92, 1.0)
        P.append(caja(ww, h, dd, x=r.uniform(-0.012, 0.012), y=y + h / 2, z=r.uniform(-0.01, 0.01), c=cols[i % len(cols)], m='papel', r=[0, r.uniform(-6, 6), 0]))
        P.append(caja(ww * 0.97, h * 0.6, dd * 0.97 + 0.004, x=0, y=y + h / 2, z=0.0, c='#efe8d4', m='papel'))   # (the pages)
        y += h
    obj(id, nombre, 'ta_libro', round(n * 0.5, 2), 'papel', 'superficie', P)
pila_libros('lb_pila_novedad_a', 'Pila de novedades (tapas rojas y crema)', ['#a8322a', '#e8dcc0', '#c0453a', '#2f5a3a'], 5, 0.16, 0.23, 21)
pila_libros('lb_pila_novedad_b', 'Pila de novedades (tapas azules)', ['#27406e', '#d8806a', '#3a5a8a', '#e0c070'], 6, 0.15, 0.22, 22)
pila_libros('lb_pila_novedad_c', 'Pila de novedades (tapas variadas)', ['#5a3a7a', '#e0c070', '#2a8a8a', '#e8d8b8'], 5, 0.16, 0.24, 23)
pila_libros('lb_pila_grandes', 'Pila de libros grandes ilustrados', ['#2f2f34', '#c8a040', '#a8322a'], 4, 0.25, 0.32, 24)
def libros_de_cara(id, nombre, cols, n=4, seed=31):
    r = random.Random(seed)
    P = [caja(0.1 + n * 0.14, 0.02, 0.1, y=0.01, z=0.02, c='#7a4a28'), caja(0.1 + n * 0.14, 0.05, 0.012, y=0.045, z=0.065, c='#7a4a28')]
    for i in range(n):
        c = cols[i % len(cols)]
        P += [caja(0.125, 0.19, 0.016, x=-0.07 * (n - 1) + i * 0.14, y=0.115, z=0.04, c=c, m='papel', r=[-14, 0, 0]), caja(0.09, 0.05, 0.004, x=-0.07 * (n - 1) + i * 0.14, y=0.15, z=0.049, c='#efe8d4', m='papel', r=[-14, 0, 0]),
              caja(0.11, 0.07, 0.004, x=-0.07 * (n - 1) + i * 0.14, y=0.08, z=0.052, c=mezcla(c, '#ffffff', 0.35), m='papel', r=[-14, 0, 0])]
    obj(id, nombre, 'ta_libro', 1.2, 'papel', 'superficie', P)
libros_de_cara('lb_libros_cara_a', 'Libros de cara sobre un atril', ['#d23a2c', '#2f64b4', '#f0c030', '#3f9a4a'])
libros_de_cara('lb_libros_cara_b', 'Libros de cara (ensayo y novela)', ['#27406e', '#a8322a', '#e8dcc0', '#5a3a7a'], seed=32)
libros_de_cara('lb_libros_cara_c', 'Libros de cara (infantil)', ['#e76a9a', '#2aa6a6', '#ee8a2a', '#7a4aa0'], n=3, seed=33)
# comics (thin, tall, loud)
def u_comic(c, c2):
    def f(x, z): return [caja(0.17, 0.26, 0.004, x=x, y=0.13, z=z, c=c, m='papel', r=[-8, 0, 0]), caja(0.15, 0.08, 0.005, x=x, y=0.2, z=z + 0.003, c=c2, m='papel', r=[-8, 0, 0])]
    return f
regis('lb_comics_a', 'Cómics de aventuras', u_comic('#d23a2c', '#f0c030'), 5, 2, 0.19, 0.012, 0.27, 0.12, '#d23a2c', 0.1, cat='ta_libro', mat='papel', hf=0.9)
regis('lb_comics_b', 'Cómics de humor', u_comic('#2f64b4', '#e76a9a'), 5, 2, 0.19, 0.012, 0.27, 0.12, '#2f64b4', 0.1, cat='ta_libro', mat='papel', hf=0.9)
regis('lb_comics_c', 'Cómics de superhéroes', u_comic('#7a4aa0', '#ee8a2a'), 5, 2, 0.19, 0.012, 0.27, 0.12, '#7a4aa0', 0.1, cat='ta_libro', mat='papel', hf=0.9)
regis('lb_comics_d', 'Tebeos de la infancia', u_comic('#3f9a4a', '#f0c030'), 5, 2, 0.19, 0.012, 0.27, 0.12, '#3f9a4a', 0.1, cat='ta_libro', mat='papel', hf=0.9)
# stationery and school things (the back and east walls)
regis('lb_cuadernos_espiral', 'Cuadernos de espiral', u_caja(0.17, 0.24, 0.012, '#2f64b4', '#f6f2e8', banda=0.5), 5, 3, 0.18, 0.014, 0.24, 0.12, '#2f64b4', 0.1, cat='ta_papeleria', mat='papel', hf=0.9)
regis('lb_cuadernos_rojos', 'Cuadernos de tapa dura', u_caja(0.17, 0.24, 0.012, '#c0392b', '#f6f2e8', banda=0.5), 5, 3, 0.18, 0.014, 0.24, 0.12, '#c0392b', 0.1, cat='ta_papeleria', mat='papel', hf=0.9)
regis('lb_carpetas_anillas', 'Carpetas de anillas', u_caja(0.05, 0.28, 0.26, '#3f9a4a', '#eeeae0', banda=0.25, m='plastico'), 5, 1, 0.055, 0.26, 0.28, 0.3, '#3f9a4a', 0.5, cat='ta_papeleria', mat='plastico', hf=0.95)
regis('lb_estuches', 'Estuches escolares', lambda x, z: [caja(0.2, 0.06, 0.07, x=x, y=0.03, z=z, c=BRIGHT[int(abs(x * 100)) % 8], m='tela'), caja(0.2, 0.012, 0.02, x=x, y=0.066, z=z, c='#eeeae0', m='metal')], 3, 2, 0.21, 0.08, 0.07, 0.24, '#2f64b4', 0.15, cat='ta_papeleria', mat='tela')
regis('lb_rotuladores', 'Cajas de rotuladores', u_caja(0.22, 0.03, 0.12, '#eeeae0', '#d23a2c', banda=0.9), 2, 3, 0.23, 0.13, 0.03, 0.3, '#eeeae0', 0.2, cat='ta_papeleria', mat='papel', hf=0.9)
regis('lb_papel_folios', 'Paquetes de folios', u_caja(0.22, 0.05, 0.3, '#eeeae0', '#2f64b4', banda=0.5), 1, 5, 0.23, 0.05, 0.3, 0.3, '#eeeae0', 1.8, cat='ta_papeleria', mat='papel', hf=0.95)
regis('lb_sobres', 'Paquetes de sobres', u_caja(0.12, 0.02, 0.23, '#e8dcc0', '#c8a040', banda=0.9), 2, 6, 0.13, 0.025, 0.23, 0.28, '#e8dcc0', 0.1, cat='ta_papeleria', mat='papel', hf=0.95)
regis('lb_agendas', 'Agendas y diarios', u_caja(0.15, 0.21, 0.025, '#5a3a7a', '#e0c070', banda=0.15), 4, 3, 0.16, 0.028, 0.21, 0.26, '#5a3a7a', 0.3, cat='ta_papeleria', mat='papel', hf=0.9)
regis('lb_diccionarios', 'Diccionarios y gramáticas', lambda x, z: [caja(0.07, 0.27, 0.19, x=x, y=0.135, z=z, c=('#27406e', '#a8322a', '#2f5a3a')[int(abs(x * 100)) % 3], m='papel'), caja(0.072, 0.03, 0.192, x=x, y=0.22, z=z, c='#e0c070', m='papel')], 4, 1, 0.075, 0.2, 0.27, 0.22, '#27406e', 0.9, cat='ta_libro', mat='papel')
regis('lb_calculadoras', 'Calculadoras científicas', lambda x, z: [caja(0.08, 0.16, 0.02, x=x, y=0.08, z=z, c='#2f2f34', m='plastico', r=[-6, 0, 0]), caja(0.06, 0.03, 0.004, x=x, y=0.14, z=z + 0.012, c='#9ab0a0', m='plastico', r=[-6, 0, 0])], 5, 1, 0.09, 0.03, 0.17, 0.08, '#2f2f34', 0.12, cat='ta_papeleria', mat='plastico', hf=0.3)
regis('lb_gomas_tijeras', 'Blísteres de gomas, tijeras y reglas', u_blister(0.1, 0.2, '#eeeae0', '#e76a9a'), 5, 1, 0.11, 0.04, 0.2, 0.07, '#eeeae0', 0.08, cat='ta_papeleria', mat='plastico', hf=0.2)
def mochila(c, c2):
    def f(x, z):
        return [caja(0.3, 0.4, 0.15, x=x, y=0.2, z=z, c=c, m='tela'), caja(0.22, 0.2, 0.06, x=x, y=0.15, z=z + 0.1, c=c2, m='tela'), caja(0.04, 0.3, 0.02, x=x - 0.1, y=0.2, z=z - 0.08, c=oscuro(c, 0.7), m='tela'), caja(0.04, 0.3, 0.02, x=x + 0.1, y=0.2, z=z - 0.08, c=oscuro(c, 0.7), m='tela'), caja(0.1, 0.03, 0.02, x=x, y=0.41, z=z, c=oscuro(c, 0.7), m='tela')]
    return f
# a backpack is higher than a shelf's clearance: they go on a rack of their own (below)
# ---- the furniture of the shop
def mesa_novedades():
    P = [caja(1.2, 0.04, 0.8, y=0.83, c='#6a4528')] + [caja(0.05, 0.81, 0.05, x=sx * 0.55, y=0.405, z=sz * 0.35, c='#4a2e18') for sx in (-1, 1) for sz in (-1, 1)] + [caja(1.1, 0.03, 0.7, y=0.28, c='#7a5232'), caja(1.2, 0.05, 0.02, y=0.775, z=0.39, c='#4a2e18'), caja(1.2, 0.05, 0.02, y=0.775, z=-0.39, c='#4a2e18')]
    obj('mesa_novedades', 'Mesa de novedades con balda', 'mesa', 34, 'madera', 'suelo', P, superficies=[{'y': 0.85, 'margen': 0.06}, {'y': 0.295, 'margen': 0.05}], nota='la mesa de las novedades junto a la puerta')
mesa_novedades()
P_ = [caja(0.8, 0.03, 0.34, y=0.015, c='#4a2e18'), caja(0.8, 1.5, 0.03, y=0.78, z=-0.15, c='#6a4528'), caja(0.8, 0.14, 0.03, y=1.56, z=-0.15, c='#2f5a3a')]
for lv, y in enumerate((0.3, 0.72, 1.14)):
    P_ += [caja(0.78, 0.015, 0.22, y=y, z=-0.02, c='#7a5232', r=[-14, 0, 0])]
    for i in range(4):
        P_ += [caja(0.17, 0.3, 0.004, x=-0.29 + i * 0.19, y=y + 0.16, z=0.0 + 0.012 * (i % 2), c=('#e8e0cc', '#efe6cf', '#d8d0b8')[(i + lv) % 3], m='papel', r=[-14, 0, 0]), caja(0.15, 0.03, 0.005, x=-0.29 + i * 0.19, y=y + 0.28, z=0.0 + 0.012 * (i % 2) + 0.003, c='#2f2f34', m='papel', r=[-14, 0, 0]),
               caja(0.12, 0.012, 0.005, x=-0.29 + i * 0.19, y=y + 0.2, z=0.004 + 0.012 * (i % 2), c='#2f2f34', m='papel', r=[-14, 0, 0])]
obj('expositor_prensa', 'Expositor de prensa diaria', 'ta_expositor', 14, 'madera', 'suelo', P_, nota='periódicos del día')
P_ = [cil(0.2, 0.22, 0.03, y=0.015, c='#2f2f32', m='metal', seg=12), cil(0.03, 0.03, 1.5, y=0.76, c='#9aa0a4', m='metal', seg=8), cil(0.22, 0.22, 0.02, y=1.5, c='#2f2f32', m='metal', seg=12)]
for lv, y in enumerate((0.35, 0.78, 1.18)):
    for i in range(8):
        a = 2 * math.pi * i / 8
        P_ += [caja(0.2, 0.28, 0.004, x=0.15 * math.sin(a), y=y + 0.16, z=0.15 * math.cos(a), c=BRIGHT[(i + lv * 3) % 8], m='papel', r=[0, math.degrees(a), 0]), caja(0.17, 0.05, 0.005, x=0.153 * math.sin(a), y=y + 0.26, z=0.153 * math.cos(a), c='#eeeae0', m='papel', r=[0, math.degrees(a), 0])]
obj('revistero_giratorio', 'Revistero giratorio', 'ta_expositor', 11, 'metal', 'suelo', P_, nota='revistas del mes')
P_ = [caja(0.7, 0.03, 0.34, y=0.015, c='#4a2e18'), caja(0.7, 1.3, 0.03, y=0.68, z=-0.15, c='#6a4528'), caja(0.7, 0.12, 0.03, y=1.36, z=-0.15, c='#d23a2c')]
for lv, y in enumerate((0.28, 0.66, 1.02)):
    P_ += [caja(0.68, 0.015, 0.22, y=y, z=-0.02, c='#7a5232', r=[-14, 0, 0])]
    for i in range(4):
        P_ += [caja(0.15, 0.24, 0.004, x=-0.26 + i * 0.17, y=y + 0.13, z=0.0, c=BRIGHT[(i * 3 + lv) % 8], m='papel', r=[-14, 0, 0]), caja(0.12, 0.07, 0.005, x=-0.26 + i * 0.17, y=y + 0.2, z=0.004, c=BRIGHT[(i + lv * 2 + 4) % 8], m='papel', r=[-14, 0, 0])]
obj('expositor_comics', 'Expositor de cómics y tebeos', 'ta_expositor', 14, 'madera', 'suelo', P_, nota='cómics, 8 €')
P_ = [caja(0.8, 0.03, 0.36, y=0.015, c='#4a2e18'), caja(0.03, 0.9, 0.34, x=-0.39, y=0.45, c='#6a4528'), caja(0.03, 0.9, 0.34, x=0.39, y=0.45, c='#6a4528'), caja(0.74, 0.5, 0.012, y=0.28, z=-0.17, c='#6a4528')]
for i, (x, c1, c2, h, rz) in enumerate(((-0.28, '#8ec0d8', '#6a9a4a', 0.7, 4), (-0.1, '#e8c880', '#a8683a', 0.66, -3), (0.08, '#c8d8e0', '#4a7a9a', 0.7, 2), (0.26, '#e8b8c0', '#8a6a9a', 0.64, -4))):
    P_ += [caja(0.46, h, 0.012, x=x, y=0.04 + h / 2, z=-0.05 + 0.04 * (i % 2), c='#2f2f34', m='madera', r=[-6, 0, rz]), caja(0.42, h * 0.55, 0.014, x=x, y=0.04 + h * 0.72, z=-0.047 + 0.04 * (i % 2), c=c1, m='papel', r=[-6, 0, rz]), caja(0.42, h * 0.4, 0.014, x=x, y=0.04 + h * 0.27, z=-0.047 + 0.04 * (i % 2), c=c2, m='papel', r=[-6, 0, rz])]
obj('expositor_laminas', 'Cajón de láminas y pósters', 'ta_expositor', 10, 'madera', 'suelo', P_, nota='láminas, 7 €')
for k, (n_, marco, c1, c2, c3) in {'a': ('paisaje de dehesa', '#8a5a36', '#8ec0d8', '#b8a060', '#6a9a4a'), 'b': ('grabado de un libro antiguo', '#2f2f34', '#e8dcc0', '#c8b890', '#8a6a40'), 'c': ('lámina de una biblioteca', '#cfb48a', '#c8d8e0', '#4a7a9a', '#a8322a')}.items():
    obj('cuadro_libreria_' + k, 'Cuadro enmarcado: %s' % n_, 'cuadro', 2, 'madera', 'pared', [caja(0.5, 0.65, 0.03, y=1.7, z=0.015, c=marco), caja(0.42, 0.57, 0.006, y=1.7, z=0.033, c=c1, m='papel'), caja(0.42, 0.26, 0.007, y=1.55, z=0.034, c=c2, m='papel'), caja(0.2, 0.16, 0.008, x=-0.08, y=1.7, z=0.035, c=c3, m='papel')])
P_ = [caja(0.7, 0.22, 0.65, y=0.31, c='#3a5a48', m='tela'), caja(0.7, 0.55, 0.16, y=0.62, z=-0.25, c='#3a5a48', m='tela', r=[-10, 0, 0]), caja(0.14, 0.3, 0.66, x=-0.36, y=0.46, c='#335040', m='tela'), caja(0.14, 0.3, 0.66, x=0.36, y=0.46, c='#335040', m='tela'),
      caja(0.6, 0.1, 0.55, y=0.46, z=0.03, c='#4a7058', m='tela')] + [caja(0.05, 0.2, 0.05, x=sx * 0.3, y=0.1, z=sz * 0.27, c='#4a2e18') for sx in (-1, 1) for sz in (-1, 1)]
obj('sillon_lectura', 'Sillón de lectura', 'mueble', 24, 'tela', 'suelo', P_, modificadores=['SEAT'], asientos=[{'p': [0, 0.5, 0.02], 'h': 0.5, 'anim': 'sofa'}], nota='un sillón para hojear tranquilo')
obj('mesa_auxiliar_lectura', 'Mesita redonda de lectura', 'mesa', 9, 'madera', 'suelo', [cil(0.23, 0.23, 0.03, y=0.54, c='#6a4528', seg=14), cil(0.025, 0.025, 0.5, y=0.27, c='#4a2e18', seg=8), cil(0.18, 0.18, 0.025, y=0.0125, c='#4a2e18', seg=12)], superficies=[{'y': 0.555, 'margen': 0.02}])
obj('lampara_lectura', 'Lámpara de lectura con pantalla verde', 'lampara', 1.2, 'metal', 'superficie', [cil(0.06, 0.07, 0.02, y=0.01, c='#c8a040', m='metal', seg=10), cil(0.012, 0.012, 0.3, y=0.17, c='#c8a040', m='metal', seg=6), cil(0.07, 0.11, 0.12, y=0.38, c='#f0e8d4', m='cristal', luz=True, seg=10), cil(0.075, 0.115, 0.012, y=0.31, c='#2f5a3a', m='plastico', seg=10)])
obj('carro_libros', 'Carro de libros', 'mueble', 12, 'metal', 'suelo', [
    caja(0.9, 0.03, 0.45, y=0.2, c='#9aa0a4', m='metal'), caja(0.9, 0.03, 0.45, y=0.5, c='#9aa0a4', m='metal'), caja(0.03, 0.9, 0.03, x=-0.43, y=0.45, z=-0.2, c='#7a7e82', m='metal'), caja(0.03, 0.9, 0.03, x=0.43, y=0.45, z=-0.2, c='#7a7e82', m='metal'), caja(0.9, 0.03, 0.03, y=0.9, z=-0.2, c='#7a7e82', m='metal'),
    caja(0.03, 0.4, 0.03, x=-0.43, y=0.7, z=0.21, c='#7a7e82', m='metal'), caja(0.03, 0.4, 0.03, x=0.43, y=0.7, z=0.21, c='#7a7e82', m='metal')] + [cil(0.05, 0.05, 0.03, x=sx * 0.4, y=0.05, z=sz * 0.18, c='#2f2f32', m='goma', seg=8, r=[0, 0, 90]) for sx in (-1, 1) for sz in (-1, 1)] + [
    caja(0.07, 0.24, 0.2, x=-0.3 + i * 0.075, y=0.335 + 0.0, z=0.0, c=PAL['mixtos_a'][i % 5], m='papel') for i in range(9)] + [caja(0.07, 0.25, 0.2, x=-0.3 + i * 0.075, y=0.64, z=0.0, c=PAL['azules'][i % 5], m='papel') for i in range(9)], nota='libros por colocar')
obj('escalera_libreria', 'Escalerilla de biblioteca de madera', 'mueble', 7, 'madera', 'suelo', [
    caja(0.46, 0.03, 0.2, y=0.33, z=0.17, c='#a06c40'), caja(0.46, 0.03, 0.2, y=0.64, z=0.0, c='#a06c40'), caja(0.46, 0.03, 0.22, y=0.95, z=-0.17, c='#a06c40')] + [
    p for sx in (-1, 1) for p in (caja(0.03, 0.315, 0.2, x=sx * 0.215, y=0.1575, z=0.17, c='#8a5a36'), caja(0.03, 0.625, 0.2, x=sx * 0.215, y=0.3125, z=0.0, c='#8a5a36'), caja(0.03, 0.935, 0.22, x=sx * 0.215, y=0.4675, z=-0.17, c='#8a5a36'))], nota='para alcanzar los de arriba')
P_ = [caja(0.9, 0.03, 0.4, y=0.015, c='#2f2f34', m='plastico'), caja(0.04, 1.5, 0.04, x=-0.43, y=0.75, z=-0.15, c='#7a7e82', m='metal'), caja(0.04, 1.5, 0.04, x=0.43, y=0.75, z=-0.15, c='#7a7e82', m='metal'), caja(0.9, 0.04, 0.04, y=0.55, z=-0.15, c='#7a7e82', m='metal'), caja(0.9, 0.04, 0.04, y=1.2, z=-0.15, c='#7a7e82', m='metal')]
for i, (c, c2) in enumerate((('#d23a2c', '#f0c030'), ('#2f64b4', '#e76a9a'), ('#3f9a4a', '#eeeae0'), ('#7a4aa0', '#ee8a2a'))):
    ox, oy = -0.22 + (i % 2) * 0.44, (0.57 if i < 2 else 1.22)
    P_ += [p for p in mochila(c, c2)(ox, 0.0) for p in [dict(p, p=[p['p'][0], p['p'][1] + oy, p['p'][2]])]]
obj('expositor_mochilas', 'Perchero de mochilas escolares', 'ta_expositor', 8, 'tela', 'suelo', P_, nota='mochilas, 24 €')
def tray(y, r, cols, sd):
    P = [cil(r, r, 0.015, y=y, c='#d8d4c8', m='plastico', seg=10)]
    for i in range(8):
        a = 2 * math.pi * i / 8
        P += [caja(0.12, 0.17, 0.012, x=(r - 0.05) * math.sin(a), y=y + 0.095, z=(r - 0.05) * math.cos(a), c=cols[i % len(cols)], m='papel', r=[0, math.degrees(a), 0])]
    return P
P_ = [cil(0.2, 0.22, 0.03, y=0.015, c='#2f2f32', m='metal', seg=12), cil(0.025, 0.025, 1.4, y=0.7, c='#9aa0a4', m='metal', seg=8)] + tray(0.4, 0.3, ('#2f64b4', '#d23a2c', '#3f9a4a', '#f0c030'), 1) + tray(0.85, 0.28, ('#7a4aa0', '#ee8a2a', '#2aa6a6', '#e76a9a'), 2) + tray(1.3, 0.24, ('#d23a2c', '#f0c030', '#2f64b4', '#3f9a4a'), 3)
obj('expositor_papeleria_giratorio', 'Torre giratoria de cuadernos y bolígrafos', 'ta_expositor', 10, 'metal', 'suelo', P_, nota='cuadernos, 2 €')
P_ = [caja(1.0, 0.04, 0.7, y=0.73, c='#8a5a36')] + [caja(0.05, 0.71, 0.05, x=sx * 0.45, y=0.355, z=sz * 0.3, c='#6a4528') for sx in (-1, 1) for sz in (-1, 1)]
def caja_juego(x, z, ry, c, c2, w=0.32, d=0.32, h=0.055):
    return [caja(w, h, d, x=x, y=0.75 + h / 2, z=z, c=c, m='papel', r=[0, ry, 0]), caja(w * 0.9, 0.006, d * 0.9, x=x, y=0.75 + h + 0.003, z=z, c=c2, m='papel', r=[0, ry, 0])]
P_ += caja_juego(-0.22, 0.0, 6, '#c0392b', '#f0e0b8') + caja_juego(-0.18, 0.2, -10, '#2f64b4', '#e8dcc0', 0.28, 0.2, 0.05)
P_ += [caja(0.3, 0.05, 0.3, x=0.2, y=0.775, z=-0.02, c='#d6b66e', m='papel'), caja(0.28, 0.012, 0.28, x=0.2, y=0.806, z=-0.02, c='#f0e0b8', m='papel')] + [
    caja(0.11, 0.008, 0.11, x=0.2 + (i % 2) * 0.125 - 0.0625, y=0.816, z=-0.02 + (i // 2) * 0.125 - 0.0625, c=c, m='papel') for i, c in enumerate(('#d23a2c', '#2f64b4', '#f0c030', '#3f9a4a'))]   # (parchís: the four corners)
obj('mesa_juegos_mesa', 'Mesa de juegos de mesa (parchís, damas, oca)', 'mesa', 30, 'madera', 'suelo', P_, superficies=[{'y': 0.75, 'margen': 0.05}], nota='parchís, 9 €')
obj('rotulo_libreria', 'Rótulo interior de la librería', 'decoracion', 3, 'madera', 'pared', [caja(1.5, 0.4, 0.03, y=2.55, z=0.015, c='#3a2616'), plano(1.44, 0.34, y=2.55, z=0.033, tex={'tipo': 'ta_rotulo_libreria', 'rotulo_local': True})])
obj('cartel_novedades', 'Cartel de novedades', 'cuadro', 0.8, 'madera', 'pared', [caja(0.9, 0.3, 0.02, y=2.55, z=0.01, c='#2f5a3a'), plano(0.86, 0.26, y=2.55, z=0.021, tex={'tipo': 'ta_cartel_novedades'})])
obj('cartel_libros_texto', 'Cartel de libros de texto y material escolar', 'cuadro', 0.8, 'madera', 'pared', [caja(0.9, 0.3, 0.02, y=2.55, z=0.01, c='#27406e'), plano(0.86, 0.26, y=2.55, z=0.021, tex={'tipo': 'ta_cartel_texto'})])
obj('caja_libros', 'Caja de cartón de libros', 'caja', 14, 'papel', 'superficie', [caja(0.45, 0.28, 0.32, c='#b88a58', m='papel'), caja(0.46, 0.01, 0.05, y=0.285, c='#e0d4b8', m='papel'), caja(0.16, 0.1, 0.004, x=0.1, y=0.16, z=0.162, c='#eeeae0', m='papel')])
obj('torre_cajas_libros', 'Pila de cajas de libros', 'caja', 24, 'papel', 'suelo', [caja(0.5, 0.3, 0.36, y=0.15, c='#b88a58', m='papel'), caja(0.5, 0.3, 0.36, x=0.02, y=0.45, c='#a87c4c', m='papel', r=[0, 5, 0]), caja(0.46, 0.28, 0.34, x=-0.01, y=0.74, c='#b88a58', m='papel', r=[0, -4, 0])], superficies=[{'y': 0.88, 'margen': 0.04}])

# ================================================================== THE TOYSHOP (juguetería)
obj('mostrador_jugueteria', 'Mostrador de la juguetería (1,2 m)', 'mostrador', 150, 'madera', 'suelo', [
    caja(1.2, 0.88, 0.5, z=-0.04, c='#2f64b4'), caja(1.2, 0.05, 0.62, y=0.925, z=0.0, c='#f0c030'), caja(1.1, 0.5, 0.01, y=0.5, z=0.216, c='#4a82d0'), caja(1.2, 0.07, 0.01, y=0.035, z=0.216, c='#2f2f32')] + [
    caja(0.12, 0.12, 0.012, x=-0.4 + i * 0.27, y=0.52, z=0.226, c=BRIGHT[(i * 2) % 8]) for i in range(4)], fijo='estructural', superficies=[{'y': 0.95, 'margen': 0.04}], nota='el mostrador azul con la tapa amarilla')
estantes('gondola_jugueteria', 'Góndola de la juguetería', 1.0, 0.45, [0.2, 0.52, 0.84, 1.16, 1.48], 1.7, c='#4a82d0', cp='#f2eee4', masa=48, borde='#f0c030', nota='por una cara; de dos en dos, espalda con espalda; los costados azules')
estantes('estanteria_jugueteria_pared', 'Estantería de pared de la juguetería', 1.0, 0.4, [0.18, 0.5, 0.82, 1.14, 1.46, 1.78], 2.1, c='#f0ece0', cp='#fbf8ee', masa=60, borde='#e76a9a')
estantes('estanteria_jugueteria_baja', 'Estantería baja de la juguetería', 1.0, 0.4, [0.2, 0.5, 0.8, 1.1], 1.1, c='#f0ece0', cp='#fbf8ee', masa=32, borde='#e76a9a')

def u_caja_v(w, h, d, c, cv, m='papel'):
    """A toy box with a window on its face (the toy inside) and a band on top."""
    def f(x, z):
        return [caja(w, h, d, x=x, y=h / 2, z=z, c=c, m=m), caja(w * 0.7, h * 0.55, 0.006, x=x, y=h * 0.5, z=z + d / 2 + 0.002, c=cv, m='plastico'), caja(w * 0.9, h * 0.12, 0.008, x=x, y=h * 0.9, z=z + d / 2 + 0.002, c='#f0c030', m='papel')]
    return f
regis('jg_munecas_rosa', 'Muñecas en caja (rosa)', u_caja_v(0.13, 0.28, 0.06, '#e76a9a', '#f2d8c8'), 3, 2, 0.14, 0.07, 0.28, 0.3, '#e76a9a', 0.4, cat='ta_juguete', hf=0.9)
regis('jg_munecas_lila', 'Muñecas en caja (lila)', u_caja_v(0.13, 0.28, 0.06, '#a070c8', '#f2d8c8'), 3, 2, 0.14, 0.07, 0.28, 0.3, '#a070c8', 0.4, cat='ta_juguete', hf=0.9)
regis('jg_pistas_coches', 'Circuitos de coches', u_apilado(0.34, 0.24, 3, 0.08, ['#d23a2c', '#f0c030', '#2f64b4'], m='papel'), 1, 1, 0.34, 0.24, 0.25, 0.32, '#d23a2c', 3.0, cat='ta_juguete', mat='papel', hf=0.95)
regis('jg_construccion_a', 'Cajas de construcción (rojas)', u_caja_v(0.26, 0.2, 0.08, '#d23a2c', '#f0c030'), 2, 2, 0.27, 0.09, 0.2, 0.3, '#d23a2c', 1.2, cat='ta_juguete', hf=0.9)
regis('jg_construccion_b', 'Cajas de construcción (amarillas)', u_caja_v(0.26, 0.2, 0.08, '#f0c030', '#2f64b4'), 2, 2, 0.27, 0.09, 0.2, 0.3, '#f0c030', 1.2, cat='ta_juguete', hf=0.9)
regis('jg_puzles_madera', 'Puzles de madera', u_apilado(0.28, 0.2, 4, 0.035, ['#f0c030', '#3f9a4a', '#2f64b4', '#e76a9a'], m='madera'), 1, 1, 0.28, 0.2, 0.14, 0.26, '#f0c030', 1.6, cat='ta_juguete', mat='madera', hf=0.95)
regis('jg_robots', 'Robots en caja', u_caja_v(0.17, 0.27, 0.1, '#7ab0e8', '#b8bec2'), 3, 2, 0.18, 0.11, 0.27, 0.3, '#7ab0e8', 0.7, cat='ta_juguete', hf=0.9)
regis('jg_ciencia', 'Juegos de ciencia', u_caja_v(0.22, 0.27, 0.08, '#3f9a4a', '#eeeae0'), 2, 2, 0.23, 0.09, 0.27, 0.3, '#3f9a4a', 0.8, cat='ta_juguete', hf=0.9)
regis('jg_pizarras', 'Pizarras mágicas', u_apilado(0.3, 0.24, 4, 0.03, ['#d23a2c', '#2f64b4', '#f0c030'], m='plastico'), 1, 1, 0.3, 0.24, 0.12, 0.26, '#d23a2c', 1.0, cat='ta_juguete', mat='plastico', hf=0.95)
regis('jg_xilofonos', 'Xilófonos de colores', lambda x, z: [caja(0.3, 0.03, 0.12, x=x, y=0.015, z=z, c='#8a5a36', m='madera')] + [caja(0.032, 0.012, 0.1 - 0.004 * i, x=x - 0.126 + 0.036 * i, y=0.036, z=z, c=BRIGHT[i % 8], m='plastico') for i in range(8)], 1, 3, 0.31, 0.13, 0.05, 0.3, '#8a5a36', 0.7, cat='ta_juguete')
def u_peluche(c, tipo):
    def f(x, z):
        P = [cil(0.06, 0.07, 0.11, x=x, y=0.055, z=z, c=c, m='tela', seg=8), cil(0.05, 0.05, 0.08, x=x, y=0.15, z=z, c=mezcla(c, '#eeeae0', 0.2), m='tela', seg=8), caja(0.025, 0.07, 0.03, x=x - 0.075, y=0.08, z=z + 0.01, c=c, m='tela'), caja(0.025, 0.07, 0.03, x=x + 0.075, y=0.08, z=z + 0.01, c=c, m='tela')]
        if tipo == 'oso': P += [cil(0.02, 0.02, 0.02, x=x - 0.04, y=0.2, z=z, c=c, m='tela', seg=6), cil(0.02, 0.02, 0.02, x=x + 0.04, y=0.2, z=z, c=c, m='tela', seg=6), caja(0.04, 0.03, 0.02, x=x, y=0.14, z=z + 0.05, c='#e8d8b8', m='tela')]
        elif tipo == 'conejo': P += [caja(0.02, 0.1, 0.012, x=x - 0.025, y=0.255, z=z, c=c, m='tela'), caja(0.02, 0.1, 0.012, x=x + 0.025, y=0.255, z=z, c=c, m='tela')]
        elif tipo == 'perro': P += [caja(0.025, 0.06, 0.012, x=x - 0.055, y=0.17, z=z, c=oscuro(c, 0.7), m='tela'), caja(0.025, 0.06, 0.012, x=x + 0.055, y=0.17, z=z, c=oscuro(c, 0.7), m='tela'), caja(0.03, 0.025, 0.03, x=x, y=0.145, z=z + 0.05, c='#2f2f34', m='tela')]
        else: P += [caja(0.07, 0.09, 0.012, x=x - 0.07, y=0.17, z=z, c=c, m='tela'), caja(0.07, 0.09, 0.012, x=x + 0.07, y=0.17, z=z, c=c, m='tela'), caja(0.025, 0.07, 0.03, x=x, y=0.13, z=z + 0.05, c=c, m='tela')]
        return P
    return f
for k, (n_, c, tipo) in {'osos': ('Osos de peluche', '#c8884a', 'oso'), 'conejos': ('Conejos de peluche', '#e8b8c8', 'conejo'), 'perros': ('Perritos de peluche', '#e8dcc0', 'perro'), 'elefantes': ('Elefantes de peluche', '#8ab0d8', 'elefante')}.items():
    regis('jg_peluche_' + k, n_, u_peluche(c, tipo), 3, 2, 0.17, 0.12, 0.26, 0.3, c, 0.35, cat='ta_juguete', mat='tela')
regis('jg_dinosaurios', 'Dinosaurios de goma', lambda x, z: [caja(0.14, 0.07, 0.05, x=x, y=0.06, z=z, c='#5aa040', m='goma'), caja(0.05, 0.06, 0.045, x=x + 0.08, y=0.1, z=z, c='#5aa040', m='goma'), cono(0.025, 0.1, x=x - 0.1, y=0.05, z=z, c='#5aa040', m='goma', seg=5, r=[0, 0, 90]),
                                                          caja(0.02, 0.05, 0.03, x=x - 0.03, y=0.025, z=z, c='#4a8a38', m='goma'), caja(0.02, 0.05, 0.03, x=x + 0.04, y=0.025, z=z, c='#4a8a38', m='goma')], 2, 4, 0.22, 0.07, 0.13, 0.3, '#5aa040', 0.2, cat='ta_juguete', mat='goma')
regis('jg_figuras_accion', 'Figuras de acción en blíster', lambda x, z: [caja(0.12, 0.24, 0.004, x=x, y=0.12, z=z, c='#2f2f34', m='papel'), caja(0.07, 0.17, 0.03, x=x, y=0.12, z=z + 0.017, c='#d8dce0', m='plastico'), caja(0.05, 0.07, 0.025, x=x, y=0.19, z=z + 0.017, c='#d23a2c', m='plastico')], 4, 1, 0.13, 0.04, 0.24, 0.08, '#2f2f34', 0.12, cat='ta_juguete', hf=0.2)
regis('jg_cubos_playa', 'Cubos y palas de playa', lambda x, z: [cil(0.07, 0.055, 0.12, x=x, y=0.06, z=z, c=BRIGHT[int(abs(x * 100)) % 8], m='plastico', seg=8), caja(0.045, 0.16, 0.012, x=x + 0.09, y=0.0845, z=z, c=BRIGHT[(int(abs(x * 100)) + 3) % 8], m='plastico', r=[0, 0, 12])], 3, 2, 0.17, 0.15, 0.17, 0.3, '#2f64b4', 0.25, cat='ta_juguete')
regis('jg_pistolas_agua', 'Pistolas de agua', lambda x, z: [caja(0.18, 0.08, 0.04, x=x, y=0.1, z=z, c=BRIGHT[int(abs(x * 100)) % 8], m='plastico'), caja(0.04, 0.1, 0.04, x=x - 0.05, y=0.05, z=z, c=BRIGHT[(int(abs(x * 100)) + 2) % 8], m='plastico'), cil(0.03, 0.03, 0.08, x=x + 0.02, y=0.18, z=z, c='#8ec0d8', m='cristal', seg=6)], 4, 2, 0.2, 0.06, 0.2, 0.3, '#2aa6a6', 0.15, cat='ta_juguete')
regis('jg_tren_madera', 'Trenes de madera', lambda x, z: [caja(0.09, 0.05, 0.05, x=x - 0.1, y=0.04, z=z, c='#d23a2c', m='madera'), caja(0.09, 0.05, 0.05, x=x, y=0.04, z=z, c='#f0c030', m='madera'), caja(0.09, 0.05, 0.05, x=x + 0.1, y=0.04, z=z, c='#3f9a4a', m='madera')] + [
    cil(0.016, 0.016, 0.052, x=x + dx, y=0.016, z=z, c='#2f2f34', m='madera', seg=6, r=[90, 0, 0]) for dx in (-0.13, -0.07, 0.07, 0.13)], 1, 4, 0.33, 0.07, 0.08, 0.3, '#d23a2c', 0.4, cat='ta_juguete', mat='madera')
regis('jg_bloques_madera', 'Botes de bloques de madera', lambda x, z: [cil(0.09, 0.09, 0.2, x=x, y=0.1, z=z, c='#f0c030', m='plastico', seg=10), cil(0.095, 0.095, 0.02, x=x, y=0.21, z=z, c='#d23a2c', m='plastico', seg=10), caja(0.1, 0.05, 0.005, x=x, y=0.1, z=z + 0.092, c='#eeeae0', m='papel')], 3, 2, 0.19, 0.19, 0.22, 0.3, '#f0c030', 0.9, cat='ta_juguete')
for k, (n_, c, c2) in {'a': ('rojo', '#c0392b', '#f0e0b8'), 'b': ('azul', '#2f64b4', '#e8dcc0'), 'c': ('verde', '#3f9a4a', '#f0e0b8')}.items():
    regis('jg_juegos_mesa_' + k, 'Juegos de mesa en caja (%s)' % n_, u_apilado(0.3, 0.3, 4, 0.055, [c, mezcla(c, '#ffffff', 0.25), oscuro(c, 0.85)], tapa=c2, m='papel'), 1, 1, 0.3, 0.3, 0.24, 0.32, c, 2.2, cat='ta_juguete', mat='papel', hf=0.95)
regis('jg_cartas', 'Barajas y juegos de cartas', u_caja(0.07, 0.1, 0.025, '#d23a2c', '#f0c030', banda=0.4), 5, 3, 0.08, 0.03, 0.1, 0.3, '#d23a2c', 0.1, cat='ta_juguete')
regis('jg_pinturas_dedos', 'Pinturas de dedos y plastilina', lambda x, z: [caja(0.16, 0.04, 0.07, x=x, y=0.02, z=z, c='#eeeae0', m='papel')] + [cil(0.03, 0.03, 0.05, x=x - 0.05 + 0.034 * i, y=0.065, z=z, c=BRIGHT[(i + int(abs(x * 100))) % 8], m='plastico', seg=6) for i in range(4)], 3, 3, 0.17, 0.09, 0.07, 0.3, '#eeeae0', 0.15, cat='ta_juguete')
def bici_infantil(id, nombre, c, c2):
    P = []
    for wx in (-0.34, 0.34):
        P += [cil(0.15, 0.15, 0.04, x=wx, y=0.15, z=0.0, c='#2f2f34', m='goma', seg=14, r=[90, 0, 0]), cil(0.115, 0.115, 0.043, x=wx, y=0.15, z=0.0, c='#c8ccd0', m='metal', seg=14, r=[90, 0, 0]), cil(0.02, 0.02, 0.06, x=wx, y=0.15, z=0.0, c='#7a7e82', m='metal', seg=6, r=[90, 0, 0])]
    P += [caja(0.46, 0.028, 0.028, x=-0.03, y=0.36, c=c, m='metal'), caja(0.38, 0.028, 0.028, x=-0.02, y=0.22, c=c, m='metal', r=[0, 0, 24]), caja(0.028, 0.34, 0.028, x=-0.22, y=0.3, c=c, m='metal', r=[0, 0, -8]),
          caja(0.028, 0.34, 0.028, x=0.29, y=0.31, c=c, m='metal', r=[0, 0, 14]), caja(0.14, 0.04, 0.08, x=-0.25, y=0.5, c='#2f2f34', m='plastico'), caja(0.03, 0.03, 0.4, x=0.33, y=0.5, c='#c8ccd0', m='metal'),
          caja(0.03, 0.03, 0.09, x=0.33, y=0.5, z=0.22, c=c2, m='goma'), caja(0.03, 0.03, 0.09, x=0.33, y=0.5, z=-0.22, c=c2, m='goma'), caja(0.12, 0.012, 0.05, x=-0.01, y=0.1, z=0.05, c='#2f2f34', m='goma')]
    P += [cil(0.045, 0.045, 0.02, x=-0.34, y=0.045, z=0.1, c='#d8d2c0', m='plastico', seg=8, r=[90, 0, 0]), cil(0.045, 0.045, 0.02, x=-0.34, y=0.045, z=-0.1, c='#d8d2c0', m='plastico', seg=8, r=[90, 0, 0])]
    obj(id, nombre, 'ta_juguete', 8, 'metal', 'suelo', P, nota='bicicleta infantil con ruedines')
bici_infantil('bici_infantil_roja', 'Bicicleta infantil roja', '#d23a2c', '#f0c030')
bici_infantil('bici_infantil_azul', 'Bicicleta infantil azul', '#2f64b4', '#f0c030')
obj('patinete_juguete', 'Patinete infantil', 'ta_juguete', 3.5, 'metal', 'suelo', [
    caja(0.55, 0.03, 0.12, x=0.0, y=0.1, c='#2aa6a6', m='metal'), caja(0.028, 0.82, 0.028, x=0.26, y=0.52, c='#c8ccd0', m='metal'), caja(0.03, 0.03, 0.4, x=0.26, y=0.93, c='#c8ccd0', m='metal'), caja(0.03, 0.03, 0.08, x=0.26, y=0.93, z=0.2, c='#f0c030', m='goma'), caja(0.03, 0.03, 0.08, x=0.26, y=0.93, z=-0.2, c='#f0c030', m='goma')] + [
    cil(0.05, 0.05, 0.03, x=wx, y=0.05, z=0.0, c='#2f2f34', m='goma', seg=10, r=[90, 0, 0]) for wx in (-0.25, 0.28)])
obj('triciclo_rojo', 'Triciclo rojo', 'ta_juguete', 5.5, 'metal', 'suelo', [
    cil(0.14, 0.14, 0.035, x=0.28, y=0.14, c='#2f2f34', m='goma', seg=12, r=[90, 0, 0]), cil(0.1, 0.1, 0.037, x=0.28, y=0.14, c='#c8ccd0', m='metal', seg=12, r=[90, 0, 0])] + [
    cil(0.07, 0.07, 0.03, x=-0.28, y=0.07, z=sz * 0.17, c='#2f2f34', m='goma', seg=10, r=[90, 0, 0]) for sz in (-1, 1)] + [
    caja(0.5, 0.05, 0.05, x=0.0, y=0.26, c='#d23a2c', m='metal', r=[0, 0, -8]), caja(0.15, 0.04, 0.1, x=-0.2, y=0.42, c='#2f2f34', m='plastico'), caja(0.03, 0.2, 0.03, x=-0.2, y=0.3, c='#d23a2c', m='metal'), caja(0.03, 0.03, 0.32, x=0.3, y=0.45, c='#c8ccd0', m='metal'),
    caja(0.03, 0.3, 0.03, x=0.3, y=0.3, c='#d23a2c', m='metal'), caja(0.03, 0.03, 0.4, x=-0.28, y=0.15, c='#7a7e82', m='metal')])
# a train table: the oval track, the engines, a tunnel
ov = []
for i in range(24):
    a = 2 * math.pi * i / 24
    ov.append(caja(0.12, 0.012, 0.03, x=0.42 * math.cos(a), y=0.778, z=0.26 * math.sin(a), c='#5a3a22' if i % 2 else '#7a5232', m='madera', r=[0, -math.degrees(a) - 90 + 180 * 0, 0]))
obj('mesa_tren_juguete', 'Mesa con un tren eléctrico de juguete', 'mesa', 34, 'madera', 'suelo', [
    caja(1.2, 0.04, 0.8, y=0.76, c='#3f8a3a'), caja(1.24, 0.06, 0.84, y=0.74, c='#8a5a36')] + [caja(0.05, 0.71, 0.05, x=sx * 0.55, y=0.355, z=sz * 0.35, c='#6a4528') for sx in (-1, 1) for sz in (-1, 1)] + ov + [
    caja(0.1, 0.05, 0.05, x=0.42, y=0.81, z=0.0, c='#d23a2c', m='plastico', r=[0, 90, 0]), caja(0.08, 0.04, 0.05, x=0.42 * math.cos(0.4), y=0.805, z=0.26 * math.sin(0.4), c='#f0c030', m='plastico', r=[0, 60, 0]), caja(0.08, 0.04, 0.05, x=0.42 * math.cos(0.75), y=0.805, z=0.26 * math.sin(0.75), c='#2f64b4', m='plastico', r=[0, 40, 0]),
    caja(0.25, 0.1, 0.18, x=-0.3, y=0.83, z=-0.12, c='#a89878', m='plastico'), cil(0.07, 0.07, 0.015, x=-0.3, y=0.89, z=-0.12, c='#2f2f34', m='plastico', seg=8, r=[90, 0, 0]),
    caja(0.04, 0.08, 0.04, x=-0.1, y=0.82, z=-0.3, c='#3f9a4a', m='plastico'), caja(0.04, 0.08, 0.04, x=0.1, y=0.82, z=0.33, c='#e76a9a', m='plastico')], nota='el tren da vueltas para quien lo mira')
def casa_munecas():
    P = [caja(0.8, 0.5, 0.4, y=0.25, z=-0.0, c='#f2d8b8'), caja(0.84, 0.03, 0.44, y=0.515, c='#e76a9a')]
    for sx in (-1, 1): P.append(caja(0.46, 0.04, 0.46, x=sx * 0.17, y=0.64, z=0.0, c='#c0392b', r=[0, 0, -sx * 40]))
    P += [caja(0.8, 0.02, 0.42, y=0.0 + 0.01, c='#8a5a36')]
    # (the front: a door, windows with shutters, a chimney, a little garden)
    P += [caja(0.14, 0.26, 0.01, x=0.0, y=0.15, z=0.205, c='#8a5a36'), cil(0.012, 0.012, 0.012, x=0.04, y=0.15, z=0.212, c='#f0c030', m='metal', seg=6, r=[90, 0, 0])]
    for sx in (-1, 1):
        for sy in (0.2, 0.42):
            if sy == 0.42 and sx == 1: continue
            P += [caja(0.16, 0.14, 0.01, x=sx * 0.26, y=sy + 0.06, z=0.205, c='#bcd6dc', m='cristal'), caja(0.05, 0.14, 0.014, x=sx * 0.26 - 0.1, y=sy + 0.06, z=0.205, c='#3f9a4a'), caja(0.05, 0.14, 0.014, x=sx * 0.26 + 0.1, y=sy + 0.06, z=0.205, c='#3f9a4a')]
    P += [caja(0.12, 0.2, 0.12, x=0.22, y=0.82, z=-0.05, c='#a8483a'), caja(0.84, 0.04, 0.2, y=0.02, z=0.3, c='#5aa040')]
    obj('casa_munecas', 'Casa de muñecas de tres plantas', 'ta_juguete', 14, 'madera', 'suelo', P, nota='casa de muñecas, 45 €')
casa_munecas()
P_ = [caja(0.9, 0.04, 0.9, y=0.02, c='#8a5a36')] + [caja(0.9, 0.5, 0.04, y=0.29, z=sz * 0.43, c='#2f64b4') for sz in (-1, 1)] + [caja(0.04, 0.5, 0.82, x=sx * 0.43, y=0.29, c='#d23a2c') for sx in (-1, 1)]
rb = random.Random(5)
for i in range(16):
    x, z = rb.uniform(-0.32, 0.32), rb.uniform(-0.32, 0.32)
    P_.append(esf(0.07, x, 0.11 + (0.0 if i < 12 else 0.1), z, c=BRIGHT[i % 8], m='goma'))
obj('cubo_pelotas_grande', 'Piscina de bolas de colores', 'ta_juguete', 18, 'goma', 'suelo', P_, nota='una piscina de bolas')
OSO, OSO_C = '#a8683a', '#c8884a'
P_ = [caja(0.5, 0.3, 0.5, y=0.15, c='#f0c030'), caja(0.46, 0.03, 0.46, y=0.315, c='#d23a2c'),                        # (the stool and its cushion: top at 0.33)
      cil(0.2, 0.23, 0.42, y=0.54, c=OSO, m='tela', seg=10), cil(0.14, 0.14, 0.05, y=0.62, z=0.14, c=OSO_C, m='tela', seg=8, r=[-90, 0, 0]),   # (body, belly)
      cil(0.16, 0.17, 0.24, y=0.87, c=OSO, m='tela', seg=10), caja(0.12, 0.09, 0.08, y=0.82, z=0.15, c='#e8d8b8', m='tela'), caja(0.04, 0.03, 0.03, y=0.85, z=0.2, c='#2f2f34', m='plastico'),
      caja(0.03, 0.03, 0.02, x=-0.06, y=0.91, z=0.155, c='#2f2f34', m='plastico'), caja(0.03, 0.03, 0.02, x=0.06, y=0.91, z=0.155, c='#2f2f34', m='plastico'),
      cil(0.055, 0.055, 0.05, x=-0.12, y=1.01, c=OSO, m='tela', seg=6), cil(0.055, 0.055, 0.05, x=0.12, y=1.01, c=OSO, m='tela', seg=6)]
P_ += [cil(0.06, 0.07, 0.3, x=sx * 0.26, y=0.55, z=0.0, c=OSO, m='tela', seg=7, r=[0, 0, sx * 20]) for sx in (-1, 1)] + [cil(0.075, 0.08, 0.3, x=sx * 0.12, y=0.4, z=0.28, c=OSO, m='tela', seg=7, r=[-78, 0, 0]) for sx in (-1, 1)]
P_ += [caja(0.18, 0.05, 0.05, y=0.72, z=0.1, c='#d23a2c', m='tela'), caja(0.06, 0.08, 0.05, x=-0.08, y=0.73, z=0.1, c='#d23a2c', m='tela'), caja(0.06, 0.08, 0.05, x=0.08, y=0.73, z=0.1, c='#d23a2c', m='tela')]
obj('oso_gigante_trono', 'Oso de peluche gigante', 'ta_juguete', 6.5, 'tela', 'suelo', P_, nota='el oso de peluche de la entrada, 39 €')
def disfraz(x, c, largo, tipo):
    P = [caja(0.16, largo, 0.045, x=x, y=1.45 - 0.04 - largo / 2, z=0.0, c=c, m='tela')]
    if tipo == 'capa': P += [caja(0.13, 0.12, 0.048, x=x, y=1.45 - 0.1, z=0.0, c='#f0c030', m='tela')]
    if tipo == 'princesa': P += [caja(0.14, largo * 0.4, 0.048, x=x, y=1.45 - 0.04 - largo * 0.8, z=0.0, c=mezcla(c, '#ffffff', 0.4), m='tela')]
    return P + [caja(0.04, 0.05, 0.04, x=x, y=1.43, z=0.0, c='#8a8f96', m='metal')]
P_ = [caja(1.2, 0.03, 0.5, y=0.015, c='#2f2f34', m='plastico'), caja(0.03, 1.5, 0.03, x=-0.58, y=0.75, c='#9aa0a4', m='metal'), caja(0.03, 1.5, 0.03, x=0.58, y=0.75, c='#9aa0a4', m='metal'), cil(0.012, 0.012, 1.2, y=1.5, c='#9aa0a4', m='metal', seg=6, r=[0, 0, 90])]
for i, (c, l, t) in enumerate((('#d23a2c', 0.9, 'capa'), ('#2f64b4', 0.85, 'capa'), ('#e76a9a', 0.95, 'princesa'), ('#7a4aa0', 0.9, 'princesa'), ('#3f9a4a', 0.8, 'capa'), ('#f0c030', 0.9, 'princesa'))):
    P_ += disfraz(-0.47 + i * 0.19, c, l, t)
obj('percha_disfraces', 'Percha de disfraces infantiles', 'perchero', 9, 'tela', 'suelo', P_, nota='capas y vestidos de princesa')
obj('buzon_reyes_magos', 'Buzón de cartas a los Reyes Magos', 'ta_expositor', 18, 'metal', 'suelo', [
    caja(0.4, 0.8, 0.3, y=0.4, c='#c0392b', m='metal'), caja(0.42, 0.04, 0.32, y=0.82, c='#f0c030', m='metal'), caja(0.2, 0.012, 0.02, y=0.62, z=0.155, c='#2f2f34', m='plastico'),
    caja(0.3, 0.08, 0.06, y=0.9, c='#f0c030', m='metal'), cono(0.04, 0.07, x=-0.12, y=0.975, c='#f0c030', m='metal', seg=5), cono(0.04, 0.07, x=0.0, y=0.985, c='#f0c030', m='metal', seg=5), cono(0.04, 0.07, x=0.12, y=0.975, c='#f0c030', m='metal', seg=5),
    plano(0.3, 0.2, y=0.4, z=0.152, tex={'tipo': 'ta_cartel_reyes'})], nota='cartas a los Reyes Magos')
obj('guirnalda_banderines', 'Guirnalda de banderines', 'decoracion', 0.3, 'tela', 'pared', [caja(2.0, 0.008, 0.008, y=2.6, z=0.04, c='#eeeae0', m='tela')] + [
    caja(0.12, 0.16, 0.004, x=-0.9 + i * 0.15, y=2.52, z=0.04, c=BRIGHT[i % 8], m='tela', r=[0, 0, 45]) for i in range(13)])
obj('rotulo_jugueteria', 'Rótulo interior de la juguetería', 'decoracion', 3, 'madera', 'pared', [caja(1.6, 0.4, 0.03, y=2.5, z=0.015, c='#2f64b4'), plano(1.54, 0.34, y=2.5, z=0.033, tex={'tipo': 'ta_rotulo_jugueteria', 'rotulo_local': True})])
obj('cartel_juguetes', 'Cartel de la campaña de juguetes', 'cuadro', 0.5, 'papel', 'pared', [caja(0.6, 0.8, 0.012, y=1.7, z=0.006, c='#e76a9a', m='papel'), plano(0.56, 0.76, y=1.7, z=0.0135, tex={'tipo': 'ta_cartel_juguetes'})])

# ================================================================== THE FLORIST (floristería)
ZINC, MADERA_B = '#b8bcc0', '#d8d0bc'
obj('mostrador_floristeria', 'Mostrador de la floristería (1,2 m)', 'mostrador', 130, 'madera', 'suelo', [
    caja(1.2, 0.88, 0.5, z=-0.04, c='#d8d2c0'), caja(1.2, 0.04, 0.64, y=0.92, z=0.0, c=ZINC, m='metal'), caja(1.1, 0.5, 0.01, y=0.5, z=0.216, c='#c8c2ae'), caja(1.2, 0.07, 0.01, y=0.035, z=0.216, c='#6f8a6a'),
    caja(1.2, 0.03, 0.4, y=0.3, z=0.28, c='#a89878')], fijo='estructural', superficies=[{'y': 0.94, 'margen': 0.04}], nota='el mostrador encalado con tapa de zinc')
obj('mesa_trabajo_floristeria', 'Mesa de trabajo de floristería con tapa de zinc', 'mesa', 38, 'madera', 'suelo', [
    caja(1.6, 0.04, 0.8, y=0.88, c=ZINC, m='metal'), caja(1.6, 0.06, 0.8, y=0.84, c='#a89878')] + [caja(0.06, 0.82, 0.06, x=sx * 0.74, y=0.41, z=sz * 0.34, c='#8a7a5a') for sx in (-1, 1) for sz in (-1, 1)] + [caja(1.5, 0.03, 0.7, y=0.28, c='#a89878')],
    superficies=[{'y': 0.9, 'margen': 0.05}, {'y': 0.295, 'margen': 0.05}], nota='donde se hacen los ramos')
obj('mesa_plantas_floristeria', 'Mesa de plantas con balda baja', 'mesa', 30, 'madera', 'suelo', [
    caja(1.2, 0.04, 0.8, y=0.83, c='#d8d0bc')] + [caja(0.05, 0.81, 0.05, x=sx * 0.55, y=0.405, z=sz * 0.35, c='#8a7a5a') for sx in (-1, 1) for sz in (-1, 1)] + [caja(1.1, 0.03, 0.7, y=0.28, c='#c8bea4')],
    superficies=[{'y': 0.85, 'margen': 0.06}, {'y': 0.295, 'margen': 0.05}])
P_ = []
for lv in range(2):   # a stepped stand for buckets of cut flowers: two steps (0.42 m deep each), 1.2 m wide
    P_ += [caja(1.2, 0.03, 0.42, y=0.3 + lv * 0.3 - 0.015, z=0.21 - lv * 0.42, c='#d8d0bc')] + [caja(0.04, 0.3 + lv * 0.3 - 0.03, 0.42, x=sx * 0.58, y=(0.3 + lv * 0.3 - 0.03) / 2, z=0.21 - lv * 0.42, c='#a89878') for sx in (-1, 1)]
P_ += [caja(1.2, 0.6, 0.012, y=0.3, z=-0.43, c='#c8bea4')]
obj('escalera_cubos_flores', 'Escalera de madera para cubos de flores', 'ta_expositor', 34, 'madera', 'suelo', P_, superficies=[{'y': 0.3, 'margen': 0.02}, {'y': 0.6, 'margen': 0.02}], nota='flores cortadas, a 2 € la flor')
P_ = [caja(1.1, 0.03, 0.4, y=0.3, c='#d8d0bc'), caja(1.1, 0.03, 0.4, y=0.7, c='#d8d0bc'), caja(1.1, 0.03, 0.4, y=1.1, c='#d8d0bc')] + [caja(0.04, 1.4, 0.4, x=sx * 0.53, y=0.7, c='#a89878') for sx in (-1, 1)] + [caja(1.1, 0.4, 0.015, y=0.2, z=-0.19, c='#c8bea4')]
obj('estante_plantas_interior', 'Estantería de plantas de interior', 'ta_expositor', 28, 'madera', 'suelo', P_, superficies=[{'y': 0.315, 'margen': 0.03}, {'y': 0.715, 'margen': 0.03}, {'y': 1.115, 'margen': 0.03}], nota='plantas de interior, 9 €')
obj('estante_floristeria_pared', 'Estante de pared para jarrones', 'estanteria', 12, 'madera', 'pared', [
    caja(0.98, 0.03, 0.3, y=1.185, z=0.15, c='#d8d0bc'), caja(0.98, 0.03, 0.3, y=1.585, z=0.15, c='#d8d0bc'), caja(0.03, 0.43, 0.3, x=-0.48, y=1.4, z=0.15, c='#a89878'), caja(0.03, 0.43, 0.3, x=0.48, y=1.4, z=0.15, c='#a89878'),
    caja(0.98, 0.43, 0.012, y=1.4, z=0.006, c='#c8bea4')], fijo=FIJO, superficies=[{'y': 1.2, 'fondo': 0.27}, {'y': 1.6, 'fondo': 0.27}])
obj('puerta_camara_frio', 'Puerta de la cámara frigorífica', 'ta_expositor', 90, 'metal', 'pared', [
    caja(1.0, 2.1, 0.1, y=1.05, z=0.05, c='#dfe3e4', m='metal'), caja(0.9, 2.0, 0.012, y=1.05, z=0.106, c='#cfd4d6', m='metal'), caja(0.05, 0.3, 0.05, x=0.38, y=1.0, z=0.13, c='#9aa0a4', m='metal'), caja(0.04, 0.25, 0.012, x=0.34, y=1.0, z=0.128, c='#2f2f32', m='plastico'),
    caja(0.24, 0.3, 0.014, y=1.55, z=0.108, c='#bcd6dc', m='cristal'), caja(0.1, 0.04, 0.012, x=0.0, y=1.8, z=0.108, c='#2f2f32', m='plastico'), caja(0.07, 0.02, 0.004, x=0.0, y=1.8, z=0.116, c='#6fd09a', m='plastico', luz=True)], fijo=FIJO, nota='la cámara donde duran las flores: 4 °C')
obj('fregadero_floristeria', 'Fregadero con grifo alto', 'mueble', 25, 'metal', 'pared', [
    caja(0.8, 0.12, 0.5, y=0.82, z=0.25, c='#c3c7ca', m='metal'), caja(0.7, 0.1, 0.4, y=0.7, z=0.25, c='#9aa0a4', m='metal'), caja(0.76, 0.76, 0.46, y=0.38, z=0.25, c='#d8d2c0'), cil(0.015, 0.015, 0.3, x=0.0, y=1.0, z=0.05, c='#c3c7ca', m='metal', seg=6), caja(0.025, 0.025, 0.2, x=0.0, y=1.15, z=0.15, c='#c3c7ca', m='metal')], fijo=FIJO)
obj('rollos_papel_pared', 'Soporte de pared con rollos de papel de envolver', 'ta_expositor', 6, 'papel', 'pared', [
    caja(1.1, 0.03, 0.06, y=1.58, z=0.03, c='#7a7e82', m='metal'), caja(1.1, 0.03, 0.06, y=1.18, z=0.03, c='#7a7e82', m='metal')] + [
    p for i, c in enumerate(('#c8a468', '#e8d8b0', '#6f8a6a', '#e76a9a', '#eeeae0', '#a070c8')) for p in (cil(0.045, 0.045, 0.34, x=-0.45 + i * 0.18, y=1.38, z=0.1, c=c, m='papel', seg=8), cil(0.015, 0.015, 0.4, x=-0.45 + i * 0.18, y=1.38, z=0.1, c='#a89878', m='madera', seg=5))], fijo=FIJO, nota='kraft, crepé y papel de colores')
obj('portabobinas_cintas', 'Soporte de bobinas de cinta y rafia', 'ta_expositor', 1.6, 'madera', 'superficie', [
    caja(0.34, 0.025, 0.14, c='#a89878'), caja(0.025, 0.2, 0.025, x=-0.15, y=0.12, c='#a89878'), caja(0.025, 0.2, 0.025, x=0.15, y=0.12, c='#a89878'), cil(0.008, 0.008, 0.32, y=0.2, c='#9aa0a4', m='metal', seg=5, r=[0, 0, 90])] + [
    cil(0.05, 0.05, 0.035, x=-0.12 + i * 0.06, y=0.2, c=c, m='tela', seg=9, r=[0, 0, 90]) for i, c in enumerate(('#d23a2c', '#eeeae0', '#6f8a6a', '#e76a9a', '#c8a468'))])
obj('tarjetero_dedicatorias', 'Tarjetero de dedicatorias', 'ta_papeleria', 0.4, 'papel', 'superficie', [caja(0.2, 0.01, 0.08, c='#a89878', m='madera'), caja(0.2, 0.1, 0.01, y=0.06, z=-0.035, c='#a89878', m='madera')] + [caja(0.045, 0.07, 0.004, x=-0.07 + i * 0.07, y=0.05, z=0.0, c=c, m='papel', r=[-12, 0, 0]) for i, c in enumerate(('#e76a9a', '#eeeae0', '#f0c030'))])
obj('tijeras_floristeria', 'Tijeras y cizalla de florista', 'ta_herramienta', 0.4, 'metal', 'superficie', [caja(0.2, 0.012, 0.03, y=0.006, c='#b8bec2', m='metal', r=[0, 12, 0]), caja(0.1, 0.02, 0.025, x=-0.08, y=0.012, z=0.0, c='#d23a2c', m='plastico', r=[0, 12, 0]), caja(0.18, 0.012, 0.03, x=0.0, y=0.02, z=0.04, c='#b8bec2', m='metal', r=[0, -20, 0])])
obj('jarron_flores_mostrador', 'Jarrón de cristal con flores', 'recipiente', 1.6, 'cristal', 'superficie', [
    cil(0.07, 0.05, 0.22, y=0.11, c='#cfe6e8', m='cristal', seg=10), cil(0.065, 0.065, 0.1, y=0.12, c='#7ab0c8', m='cristal', seg=10)] + [
    p for i, (dx, dz, h, c) in enumerate(((0, 0, 0.32, '#e76a9a'), (-0.03, 0.02, 0.28, '#eeeae0'), (0.03, -0.02, 0.3, '#d23a2c'), (0.01, 0.035, 0.26, '#f0c030'))) for p in (cil(0.004, 0.004, h, x=dx, y=0.2 + h / 2, z=dz, c='#3f7a3a', m='comida', seg=4), cil(0.03, 0.02, 0.04, x=dx, y=0.2 + h, z=dz, c=c, m='comida', seg=6))])
def ramo_papel(id, nombre, papel, flores, sd):
    P = [cil(0.14, 0.03, 0.42, y=0.21, c=papel, m='papel', seg=8), cil(0.15, 0.115, 0.1, y=0.37, c=mezcla(papel, '#ffffff', 0.3), m='papel', seg=8), caja(0.1, 0.04, 0.02, y=0.12, z=0.1, c='#d23a2c', m='tela')]
    for i, c in enumerate(flores):
        a = 2 * math.pi * i / len(flores)
        P += [cil(0.004, 0.004, 0.2, x=0.06 * math.sin(a), y=0.52, z=0.06 * math.cos(a), c='#3f7a3a', m='comida', seg=4), cil(0.034, 0.024, 0.05, x=0.075 * math.sin(a), y=0.64, z=0.075 * math.cos(a), c=c, m='comida', seg=8)]
    obj(id, nombre, 'ta_flor', 1.5, 'papel', 'superficie', P)
ramo_papel('ramo_envuelto_rosas', 'Ramo de rosas envuelto en papel kraft', '#c8a468', ['#d23a2c', '#d23a2c', '#e76a9a', '#d23a2c', '#eeeae0', '#d23a2c'], 1)
ramo_papel('ramo_envuelto_primavera', 'Ramo de primavera envuelto en papel crepé', '#e8d8b0', ['#f0c030', '#a070c8', '#eeeae0', '#ee8a2a', '#e76a9a', '#f0c030'], 2)
# the buckets of cut flowers
def vec_giro(dx, dy, dz):
    L = math.sqrt(dx * dx + dy * dy + dz * dz)
    return [round(math.degrees(math.atan2(dz, dy)), 1), 0, round(math.degrees(-math.asin(dx / L)), 1)], L
def cubo_flores(id, nombre, cab, n=17, hmin=0.36, hmax=0.52, rad=0.13, sd=1, cubo='#b8bcc0', hoja=True):
    r = random.Random(sd)
    P = [cil(0.17, 0.13, 0.3, y=0.15, c=cubo, m='metal', seg=10), cil(0.176, 0.176, 0.012, y=0.294, c=oscuro(cubo, 0.85), m='metal', seg=10)]
    for i in range(n):
        a, d = r.uniform(0, 2 * math.pi), rad * math.sqrt(r.random())
        x, z = d * math.sin(a), d * math.cos(a)
        h = r.uniform(hmin, hmax) * (1 - 0.3 * d / rad)
        bx, bz = x * 0.3, z * 0.3
        rot, L = vec_giro(x - bx, h, z - bz)
        P.append(cil(0.004, 0.004, L, x=(x + bx) / 2, y=0.3 + h / 2, z=(z + bz) / 2, c='#3f7a3a', m='comida', seg=4, r=rot))
        P += cab(x, 0.3 + h, z, r)
    obj(id, nombre, 'ta_flor', 11, 'metal', 'superficie', P, clase='CARRY', nota='cubo de zinc con agua')
def c_rosa(col):
    return lambda x, y, z, r: [cil(0.034, 0.04, 0.065, x=x, y=y + 0.022, z=z, c=col, m='comida', seg=7), cil(0.02, 0.034, 0.03, x=x, y=y + 0.065, z=z, c=oscuro(col, 0.85), m='comida', seg=7), cil(0.03, 0.01, 0.015, x=x, y=y - 0.012, z=z, c='#3f7a3a', m='comida', seg=6)]
def c_clavel(col):
    return lambda x, y, z, r: [cil(0.036, 0.016, 0.045, x=x, y=y + 0.015, z=z, c=col, m='comida', seg=7)]
def c_disco(col, centro, rad=0.055):
    return lambda x, y, z, r: [cil(rad, rad, 0.012, x=x, y=y + 0.008, z=z, c=col, m='comida', seg=9, r=[r.uniform(-25, 25), 0, r.uniform(-25, 25)]), cil(rad * 0.45, rad * 0.45, 0.018, x=x, y=y + 0.012, z=z, c=centro, m='comida', seg=7)]
def c_lirio(col):
    return lambda x, y, z, r: [cil(0.045, 0.008, 0.1, x=x, y=y + 0.03, z=z, c=col, m='comida', seg=6), cil(0.012, 0.012, 0.06, x=x, y=y + 0.07, z=z, c='#ee8a2a', m='comida', seg=4)]
def c_tulipan(col):
    return lambda x, y, z, r: [cil(0.022, 0.034, 0.06, x=x, y=y + 0.02, z=z, c=col, m='comida', seg=6), cono(0.02, 0.03, x=x, y=y + 0.065, z=z, c=col, m='comida', seg=6)]
def c_gladiolo(col):
    return lambda x, y, z, r: [caja(0.045, 0.035, 0.045, x=x, y=y - 0.1 + 0.055 * j, z=z, c=col, m='comida', r=[0, 40 * j, 0]) for j in range(5)]
def c_bola(col, rad=0.04):
    return lambda x, y, z, r: [cil(rad, rad, rad * 1.1, x=x, y=y + rad * 0.4, z=z, c=col, m='comida', seg=7)]
def c_espiga(col):
    return lambda x, y, z, r: [cil(0.006, 0.012, 0.14, x=x, y=y + 0.03, z=z, c=col, m='comida', seg=5)]
def c_hojas(col):
    return lambda x, y, z, r: [caja(0.07, 0.1, 0.004, x=x, y=y + 0.03, z=z, c=col, m='comida', r=[0, r.uniform(0, 180), 0]), caja(0.05, 0.08, 0.004, x=x, y=y - 0.04, z=z, c=oscuro(col, 0.92), m='comida', r=[0, r.uniform(0, 180), 0])]
def c_nube(col):
    return lambda x, y, z, r: [caja(0.03, 0.03, 0.03, x=x + dx, y=y + 0.01 + dy, z=z + dz, c=col, m='comida', r=[0, 30 * k, 0]) for k, (dx, dy, dz) in enumerate(((0, 0, 0), (0.03, 0.01, 0.01), (-0.03, 0.0, 0.02), (0.0, 0.025, -0.02)))]
for k, (n_, cab, sd, ex) in {
        'rosas_rojas': ('Rosas rojas', c_rosa('#c0302a'), 1, {}), 'rosas_rosas': ('Rosas rosas', c_rosa('#e76a9a'), 2, {}), 'rosas_blancas': ('Rosas blancas', c_rosa('#eeeae0'), 3, {}),
        'claveles_rojos': ('Claveles rojos', c_clavel('#d23a2c'), 4, {}), 'claveles_blancos': ('Claveles blancos y rosas', c_clavel('#f2d8e0'), 5, {}), 'girasoles': ('Girasoles', c_disco('#f0c030', '#5a3a22', 0.065), 6, {'n': 10, 'hmin': 0.4, 'hmax': 0.55}),
        'margaritas': ('Margaritas', c_disco('#eeeae0', '#f0c030', 0.04), 7, {'n': 22, 'hmin': 0.32, 'hmax': 0.45}), 'lirios': ('Lirios blancos', c_lirio('#f2eee0'), 8, {'n': 12}), 'tulipanes': ('Tulipanes', c_tulipan('#e8603a'), 9, {}),
        'gerberas': ('Gerberas naranjas', c_disco('#ee8a2a', '#3a2a1a', 0.055), 10, {}), 'gladiolos': ('Gladiolos rosas', c_gladiolo('#e86a9a'), 11, {'n': 10, 'hmin': 0.5, 'hmax': 0.7}), 'crisantemos': ('Crisantemos amarillos', c_bola('#f0c030', 0.04), 12, {'n': 16}),
        'lavanda': ('Lavanda', c_espiga('#8a5ab0'), 13, {'n': 24, 'hmin': 0.34, 'hmax': 0.48, 'rad': 0.1}), 'eucalipto': ('Eucalipto', c_hojas('#7a9a88'), 14, {'n': 10, 'hmin': 0.4, 'hmax': 0.6}), 'paniculata': ('Paniculata', c_nube('#f6f2ea'), 15, {'n': 12}),
        'hortensias': ('Hortensias azules', c_bola('#6a8ad0', 0.065), 16, {'n': 6, 'hmin': 0.34, 'hmax': 0.46})}.items():
    cubo_flores('cubo_flores_' + k, 'Cubo de %s' % n_.lower(), cab, sd=sd, **ex)
# potted plants (on tables and stands: not on shelves)
def maceta_f(x, z, r0=0.075, h=0.12, c='#b8683a'):
    return [cil(r0, r0 * 0.72, h, x=x, y=h / 2, z=z, c=c, m='ceramica', seg=9), cil(r0 * 1.05, r0 * 1.05, 0.015, x=x, y=h - 0.0075, z=z, c=oscuro(c, 0.92), m='ceramica', seg=9)]
def planta_maceta(id, nombre, partes_fn, masa=2.5):
    obj(id, nombre, 'ta_flor', masa, 'ceramica', 'superficie', partes_fn(), nota='planta de interior')
planta_maceta('fl_ficus', 'Ficus benjamina en maceta', lambda: maceta_f(0, 0, 0.1, 0.16) + [cil(0.012, 0.014, 0.22, y=0.27, c='#6a4a2c', m='madera', seg=5), cil(0.15, 0.1, 0.1, y=0.42, c='#3f7a3a', m='comida', seg=8), cil(0.12, 0.15, 0.1, y=0.52, c='#4a8a3a', m='comida', seg=8), cil(0.05, 0.12, 0.08, y=0.61, c='#3f7a3a', m='comida', seg=8)], 4)
planta_maceta('fl_orquidea_blanca', 'Orquídea blanca', lambda: maceta_f(0, 0, 0.055, 0.1, '#eeeae0') + [cil(0.004, 0.004, 0.4, x=0.0, y=0.3, c='#4a7a3a', m='comida', seg=4, r=[0, 0, 8])] + [caja(0.07, 0.07, 0.008, x=0.03 + 0.012 * i, y=0.18 + 0.065 * i, z=0.0, c='#f6f2ea', m='comida', r=[0, 40 * i, 0]) for i in range(5)] + [caja(0.16, 0.012, 0.04, x=-0.06, y=0.14, z=0.04, c='#3f7a3a', m='comida', r=[0, 0, 20]), caja(0.16, 0.012, 0.04, x=0.06, y=0.14, z=-0.04, c='#3f7a3a', m='comida', r=[0, 0, -20])])
planta_maceta('fl_orquidea_rosa', 'Orquídea rosa', lambda: maceta_f(0, 0, 0.055, 0.1, '#7a4aa0') + [cil(0.004, 0.004, 0.42, x=0.0, y=0.31, c='#4a7a3a', m='comida', seg=4, r=[0, 0, -8])] + [caja(0.07, 0.07, 0.008, x=-0.03 - 0.012 * i, y=0.2 + 0.065 * i, z=0.0, c='#e0589a', m='comida', r=[0, 40 * i, 0]) for i in range(5)] + [caja(0.16, 0.012, 0.04, x=-0.06, y=0.14, z=0.04, c='#3f7a3a', m='comida', r=[0, 0, 20]), caja(0.16, 0.012, 0.04, x=0.06, y=0.14, z=-0.04, c='#3f7a3a', m='comida', r=[0, 0, -20])])
def helecho():
    P = maceta_f(0, 0, 0.09, 0.14, '#a85a30')
    for i in range(8):
        k, sg = i % 4, 1 if i < 4 else -1
        col = ('#4a8a3a', '#5a9a44', '#3f7a3a', '#4f9040')[k]
        if k % 2 == 0: P.append(caja(0.04, 0.26, 0.004, x=0.06 * sg * (1 if k == 0 else 0.6), y=0.28, z=0.03 * (k - 1), c=col, m='comida', r=[0, 0, -sg * 32]))
        else: P.append(caja(0.04, 0.26, 0.004, x=0.03 * (k - 2), y=0.28, z=0.06 * sg, c=col, m='comida', r=[sg * 32, 0, 0]))
    return P
planta_maceta('fl_helecho', 'Helecho en maceta', helecho, 3)
def sansevieria():
    P = maceta_f(0, 0, 0.09, 0.16, '#eeeae0')
    for i, (dx, dz, h, rz) in enumerate(((0, 0, 0.5, 0), (-0.04, 0.02, 0.42, 6), (0.04, -0.02, 0.45, -6), (0.0, 0.05, 0.36, -3), (-0.05, -0.04, 0.33, 8), (0.05, 0.04, 0.38, -8))):
        rr = [0, 0, rz] if i % 2 == 0 else [0, 90, 0]
        P.append(caja(0.05, h, 0.012, x=dx, y=0.16 + h / 2, z=dz, c=('#3f6a3a', '#4a7a3a')[i % 2], m='comida', r=rr))
        P.append(caja(0.012, h * 0.98, 0.014, x=dx, y=0.16 + h / 2, z=dz, c='#c8c060', m='comida', r=rr))
    return P
planta_maceta('fl_sansevieria', 'Sansevieria (lengua de suegra)', sansevieria, 3.5)
def begonia():
    P = maceta_f(0, 0, 0.08, 0.12, '#b8683a') + [cil(0.12, 0.08, 0.1, y=0.18, c='#4a8a3a', m='comida', seg=8)]
    P += [cil(0.025, 0.02, 0.03, x=0.08 * math.sin(a), y=0.24 + 0.02 * (i % 2), z=0.08 * math.cos(a), c=('#d23a2c', '#e76a9a')[i % 2], m='comida', seg=6) for i, a in enumerate(2 * math.pi * k / 7 for k in range(7))] + [cil(0.03, 0.025, 0.03, y=0.27, c='#d23a2c', m='comida', seg=6)]
    return P
planta_maceta('fl_begonia', 'Begonia en flor', begonia, 2)
def crasas():
    P = [caja(0.3, 0.03, 0.2, y=0.015, c='#8a6a40')] + [caja(0.3, 0.05, 0.012, y=0.055, z=0.1, c='#8a6a40'), caja(0.3, 0.05, 0.012, y=0.055, z=-0.1, c='#8a6a40')]
    for i in range(6):
        x, z = -0.1 + 0.1 * (i % 3), -0.05 + 0.1 * (i // 3)
        P += [cil(0.04, 0.03, 0.05, x=x, y=0.055, z=z, c='#b8683a', m='ceramica', seg=7), cil(0.045, 0.02, 0.035, x=x, y=0.098, z=z, c=('#5a8a6a', '#7aa88a', '#4a7a5a')[i % 3], m='comida', seg=8), cil(0.025, 0.015, 0.025, x=x, y=0.12, z=z, c=('#8ac0a0', '#a8c8a0', '#6a9a7a')[i % 3], m='comida', seg=8)]
    return P
planta_maceta('fl_crasas', 'Bandeja de plantas crasas', crasas, 3)
def poinsettia():
    P = maceta_f(0, 0, 0.08, 0.12, '#d23a2c') + [cil(0.1, 0.06, 0.1, y=0.18, c='#3f7a3a', m='comida', seg=8)]
    for i in range(8):
        a = 2 * math.pi * i / 8
        P.append(caja(0.07, 0.01, 0.12, x=0.08 * math.sin(a), y=0.25, z=0.08 * math.cos(a), c='#c0302a', m='comida', r=[0, math.degrees(a), 0]))
    P.append(cil(0.025, 0.02, 0.02, y=0.26, c='#f0c030', m='comida', seg=6))
    return P
planta_maceta('fl_flor_pascua', 'Flor de Pascua', poinsettia, 2)
def lavanda_maceta():
    P = maceta_f(0, 0, 0.09, 0.13, '#c8a468') + [cil(0.1, 0.08, 0.09, y=0.17, c='#6a8a6a', m='comida', seg=8)]
    for i in range(14):
        a, d = i * 2.4, 0.07 * math.sqrt((i + 1) / 14)
        P.append(cil(0.008, 0.012, 0.14, x=d * math.sin(a), y=0.28, z=d * math.cos(a), c='#8a5ab0', m='comida', seg=5))
    return P
planta_maceta('fl_lavanda', 'Lavanda en maceta', lavanda_maceta, 2.5)
planta_maceta('fl_cactus_columnar', 'Cactus columnar', lambda: maceta_f(0, 0, 0.08, 0.12, '#b8683a') + [cil(0.04, 0.045, 0.34, y=0.29, c='#3f7a4a', m='comida', seg=8), cil(0.03, 0.03, 0.14, x=0.07, y=0.32, c='#3f7a4a', m='comida', seg=7), cil(0.03, 0.04, 0.05, x=0.05, y=0.24, c='#3f7a4a', m='comida', seg=7, r=[0, 0, -70]), caja(0.02, 0.02, 0.02, y=0.47, c='#e76a9a', m='comida')], 3)
# big planters on the floor and the stock
def macetero(id, nombre, c, h, r0, hoja, flor=None):
    obj(id, nombre, 'ta_flor', 16, 'ceramica', 'suelo', [cil(r0, r0 * 0.72, h, y=h / 2, c=c, m='ceramica', seg=12), cil(r0 * 1.04, r0 * 1.04, 0.025, y=h - 0.0125, c=oscuro(c, 0.9), m='ceramica', seg=12), cil(r0 * 0.92, r0 * 0.92, 0.02, y=h - 0.04, c='#4a3a2a', m='comida', seg=10)] + [
        p for i in range(9) for p in (cil(0.01, 0.014, 0.4 + 0.1 * (i % 3), x=0.5 * r0 * math.sin(i * 0.7), y=h + 0.2, z=0.5 * r0 * math.cos(i * 0.7), c='#5a7a3a', m='comida', seg=4, r=[10 * math.cos(i), 0, 10 * math.sin(i)]),
                                      caja(0.2, 0.012, 0.1, x=0.7 * r0 * math.sin(i * 0.7), y=h + 0.45 + 0.05 * (i % 3), z=0.7 * r0 * math.cos(i * 0.7), c=hoja, m='comida', r=[0, math.degrees(i * 0.7), 0]))])
macetero('macetero_grande_a', 'Macetero grande con una palmera', '#c8bea4', 0.4, 0.22, '#3f7a3a')
macetero('macetero_grande_b', 'Macetero alto con un arbusto', '#a85a30', 0.5, 0.2, '#4a8a3a')
regis('fl_jarrones', 'Jarrones de cerámica', lambda x, z: [cil(0.07, 0.05, 0.12, x=x, y=0.06, z=z, c=('#eeeae0', '#6f8a6a', '#c8a468', '#7ab0c8')[int(abs(x * 100)) % 4], m='ceramica', seg=10), cil(0.045, 0.07, 0.1, x=x, y=0.17, z=z, c=('#eeeae0', '#6f8a6a', '#c8a468', '#7ab0c8')[int(abs(x * 100)) % 4], m='ceramica', seg=10)], 4, 1, 0.16, 0.16, 0.22, 0.24, '#eeeae0', 0.8, cat='ta_flor', mat='ceramica', hf=0.3)
regis('fl_macetas_apiladas', 'Macetas de barro apiladas', lambda x, z: [cil(0.07, 0.05, 0.1, x=x, y=0.05, z=z, c='#b8683a', m='ceramica', seg=9), cil(0.07, 0.05, 0.1, x=x, y=0.12, z=z, c='#a85a30', m='ceramica', seg=9), cil(0.07, 0.05, 0.1, x=x, y=0.19, z=z, c='#b8683a', m='ceramica', seg=9)], 3, 2, 0.16, 0.16, 0.26, 0.3, '#b8683a', 0.5, cat='ta_flor', mat='ceramica')
obj('saco_tierra', 'Saco de tierra para macetas', 'ta_producto', 14, 'papel', 'suelo', [caja(0.4, 0.14, 0.6, y=0.07, c='#4a3a2a', m='papel'), caja(0.38, 0.06, 0.3, y=0.17, z=-0.1, c='#3f3a2a', m='papel'), caja(0.28, 0.003, 0.34, y=0.145, z=0.1, c='#3f9a4a', m='papel')], nota='sustrato universal 20 L')
obj('regadera_zinc', 'Regadera de zinc', 'recipiente', 1.2, 'metal', 'suelo', [cil(0.1, 0.11, 0.24, y=0.12, c='#aab0b4', m='metal', seg=10), cil(0.014, 0.018, 0.34, x=0.18, y=0.24, c='#aab0b4', m='metal', seg=6, r=[0, 0, 50]), cil(0.04, 0.04, 0.03, x=0.31, y=0.4, c='#aab0b4', m='metal', seg=7, r=[0, 0, 50]), caja(0.025, 0.2, 0.04, x=-0.11, y=0.26, c='#aab0b4', m='metal')])
obj('cesta_mimbre_flores', 'Cesta de mimbre con flores', 'ta_flor', 3, 'madera', 'superficie', [cil(0.15, 0.12, 0.14, y=0.07, c='#c8a468', m='madera', seg=10), cil(0.155, 0.155, 0.015, y=0.145, c='#b08a4a', m='madera', seg=10)] + [cil(0.003, 0.003, 0.5, x=0.2, y=0.28, z=0.0, c='#c8a468', m='madera', seg=4, r=[0, 0, 75]), cil(0.003, 0.003, 0.5, x=-0.2, y=0.28, z=0.0, c='#c8a468', m='madera', seg=4, r=[0, 0, -75])] + [
    cil(0.03, 0.02, 0.04, x=-0.07 + 0.045 * i, y=0.19 + 0.01 * (i % 2), z=0.02 * (i % 3 - 1), c=c, m='comida', seg=6) for i, c in enumerate(('#e76a9a', '#f0c030', '#eeeae0', '#a070c8', '#d23a2c', '#ee8a2a'))])
obj('rotulo_floristeria', 'Rótulo interior de la floristería', 'decoracion', 3, 'madera', 'pared', [caja(1.5, 0.4, 0.03, y=2.5, z=0.015, c='#3f5a3a'), plano(1.44, 0.34, y=2.5, z=0.033, tex={'tipo': 'ta_rotulo_floristeria', 'rotulo_local': True})])
obj('pizarra_floristeria', 'Pizarra de precios de la floristería', 'decoracion', 2.5, 'madera', 'pared', [caja(0.6, 0.8, 0.03, y=1.65, z=0.015, c='#8a6a40'), plano(0.54, 0.74, y=1.65, z=0.033, tex={'tipo': 'ta_pizarra_flores'})])
obj('cartel_ramos', 'Cartel de ramos, centros y coronas', 'cuadro', 0.5, 'papel', 'pared', [caja(0.5, 0.35, 0.012, y=1.9, z=0.006, c='#eeeae0', m='papel'), plano(0.46, 0.31, y=1.9, z=0.0135, tex={'tipo': 'ta_cartel_ramos'})])

# ================================================================== THE ESTANCO (tobacco, lottery and press)
obj('mostrador_estanco', 'Mostrador del estanco (1,2 m)', 'mostrador', 170, 'madera', 'suelo', [
    caja(1.2, 0.9, 0.52, z=-0.04, c='#6a3a2a'), caja(1.2, 0.04, 0.66, y=0.92, z=0.0, c='#d8d2c0', m='piedra'), caja(1.1, 0.55, 0.01, y=0.5, z=0.226, c='#7a4a36'), caja(1.2, 0.07, 0.01, y=0.035, z=0.226, c='#2f2f32'),
    caja(1.1, 0.03, 0.012, y=0.78, z=0.232, c='#c8a040', m='metal')], fijo='estructural', superficies=[{'y': 0.94, 'margen': 0.04}], nota='el mostrador de madera con tapa de piedra')
def mueble_tabaco(id, nombre, pal, madera='#7a4a36'):
    """A wall unit behind the counter: drawers below, and above five shelves of GENERIC packs (plain colours, no brand)."""
    P = [caja(1.0, 0.9, 0.42, y=0.45, z=0.21, c=madera), caja(1.04, 0.03, 0.46, y=0.915, z=0.23, c=oscuro(madera, 0.85)), caja(1.0, 1.42, 0.02, y=1.65, z=0.01, c=oscuro(madera, 0.8)), caja(0.02, 1.4, 0.27, x=-0.49, y=1.64, z=0.135, c=madera), caja(0.02, 1.4, 0.27, x=0.49, y=1.64, z=0.135, c=madera)]
    for i in range(2): P += [caja(0.46, 0.38, 0.012, x=-0.245 + i * 0.49, y=0.45, z=0.426, c=oscuro(madera, 1.12)), caja(0.1, 0.02, 0.016, x=-0.245 + i * 0.49, y=0.6, z=0.44, c='#c8a040', m='metal')]
    for j, y in enumerate((1.1, 1.36, 1.62, 1.88, 2.14)):
        P += [caja(0.96, 0.02, 0.26, y=y - 0.01, z=0.13, c=madera), caja(0.94, 0.082, 0.1, y=y + 0.041, z=0.06, c=pal[j % len(pal)], m='papel')]
        for i in range(14):
            c = pal[(i + j) % len(pal)]
            P += [caja(0.056, 0.084, 0.024, x=-0.435 + i * 0.067, y=y + 0.042, z=0.17, c=c, m='papel'), caja(0.058, 0.024, 0.026, x=-0.435 + i * 0.067, y=y + 0.074, z=0.17, c=mezcla(c, '#ffffff', 0.55), m='papel')]
    P += [caja(1.0, 0.03, 0.3, y=2.315, z=0.15, c=madera)]
    obj(id, nombre, 'mueble', 120, 'madera', 'suelo', P, fijo=FIJO, superficies=[{'y': 2.33, 'margen': 0.04}], nota='cajetillas genéricas, sin marca')
mueble_tabaco('mueble_tabaco_a', 'Mueble de cajetillas (rojos y blancos)', ['#c0392b', '#eeeae0', '#c0392b', '#2f64b4', '#eeeae0'])
mueble_tabaco('mueble_tabaco_b', 'Mueble de cajetillas (azules y dorados)', ['#2f64b4', '#e0b030', '#eeeae0', '#2f64b4', '#3f9a4a'])
mueble_tabaco('mueble_tabaco_c', 'Mueble de cajetillas (verdes y grises)', ['#3f9a4a', '#8a949c', '#eeeae0', '#3f9a4a', '#c0392b'])
def decimos(x0, y, z, n, c, w=0.04):
    return [caja(w, 0.1, 0.003, x=x0 + 0.045 * i, y=y, z=z, c=(c, mezcla(c, '#ffffff', 0.4), '#e0b030')[i % 3], m='papel', r=[-14, 0, 0]) for i in range(n)]
obj('vitrina_loteria', 'Vitrina de lotería y sellos para el mostrador', 'vitrina', 12, 'cristal', 'superficie', [
    caja(0.7, 0.04, 0.36, y=0.02, c='#5a3a26'), caja(0.7, 0.16, 0.36, y=0.12, c='#bcd6dc', m='cristal'), caja(0.64, 0.01, 0.3, y=0.045, c='#2f5a3a', m='tela')] + decimos(-0.25, 0.1, 0.05, 6, '#3f9a4a') + decimos(-0.25, 0.1, -0.06, 6, '#d23a2c') + [
    caja(0.07, 0.005, 0.05, x=0.17 + 0.075 * (i % 2), y=0.052, z=0.07 - 0.07 * (i // 2), c=c, m='papel') for i, c in enumerate(('#2f64b4', '#f0c030', '#d23a2c', '#3f9a4a'))], nota='décimos y sellos')
obj('terminal_loteria', 'Terminal de lotería con su impresora', 'informatica', 3.5, 'plastico', 'superficie', [
    caja(0.3, 0.05, 0.26, c='#d8dadc', m='plastico'), caja(0.24, 0.18, 0.025, y=0.14, z=-0.06, c='#2f2f32', m='plastico', r=[-12, 0, 0]), caja(0.21, 0.14, 0.004, y=0.145, z=-0.045, c='#4a7a9a', m='plastico', r=[-12, 0, 0], luz=True),
    caja(0.14, 0.02, 0.1, x=-0.05, y=0.06, z=0.06, c='#2f2f32', m='plastico'), caja(0.08, 0.1, 0.07, x=0.09, y=0.1, z=0.08, c='#d8dadc', m='plastico'), caja(0.05, 0.004, 0.05, x=0.09, y=0.152, z=0.08, c='#eeeae0', m='papel')], nota='terminal de juegos del Estado, sin logotipo')
obj('expositor_sellos', 'Expositor de sellos y sobres', 'ta_expositor', 1.2, 'papel', 'superficie', [
    caja(0.3, 0.015, 0.16, c='#5a3a26'), caja(0.3, 0.26, 0.012, y=0.145, z=-0.06, c='#e8dcc0', m='papel', r=[-10, 0, 0])] + [
    caja(0.05, 0.065, 0.004, x=-0.105 + 0.07 * (i % 4), y=0.07 + 0.075 * (i // 4), z=-0.053 + 0.0 * (i // 4), c=BRIGHT[i % 8], m='papel', r=[-10, 0, 0]) for i in range(12)], nota='sellos y sobres')
P_ = [caja(0.32, 0.03, 0.16, y=0.015, c='#2f2f32', m='plastico'), caja(0.32, 0.16, 0.012, y=0.1, z=-0.07, c='#d23a2c', m='plastico')]
for j in range(3):
    for i in range(7):
        c = BRIGHT[(i * 3 + j) % 8]
        P_ += [caja(0.022, 0.07, 0.012, x=-0.135 + i * 0.045, y=0.065 + j * 0.0 + 0.0, z=-0.04 + j * 0.035, c=c, m='plastico'), caja(0.024, 0.014, 0.014, x=-0.135 + i * 0.045, y=0.107, z=-0.04 + j * 0.035, c='#b8bec2', m='metal')]
obj('expositor_mecheros', 'Expositor de mecheros', 'ta_expositor', 1.4, 'plastico', 'superficie', P_, nota='mecheros, 1,50 €')
def revistero_pared(id, nombre, pal, sd):
    r = random.Random(sd)
    P = [caja(1.0, 0.04, 0.3, y=0.02, c='#5a3a26'), caja(1.0, 1.96, 0.02, y=1.0, z=0.01, c='#7a5a3c'), caja(0.03, 1.96, 0.3, x=-0.485, y=1.0, z=0.15, c='#5a3a26'), caja(0.03, 1.96, 0.3, x=0.485, y=1.0, z=0.15, c='#5a3a26')]
    for j, y in enumerate((0.3, 0.7, 1.1, 1.5, 1.88)):
        P += [caja(0.94, 0.015, 0.2, y=y, z=0.1, c='#6a4a30', r=[-14, 0, 0]), caja(0.94, 0.04, 0.012, y=y + 0.0, z=0.18, c='#6a4a30')]
        for i in range(5):
            c = pal[r.randrange(len(pal))]
            P += [caja(0.17, 0.26, 0.004, x=-0.37 + i * 0.185, y=y + 0.15, z=0.08 + 0.012 * (i % 2), c=c, m='papel', r=[-14, 0, 0]), caja(0.15, 0.06, 0.005, x=-0.37 + i * 0.185, y=y + 0.24, z=0.086 + 0.012 * (i % 2), c='#eeeae0', m='papel', r=[-14, 0, 0])]
    obj(id, nombre, 'ta_expositor', 22, 'madera', 'suelo', P, nota='revistas y fascículos')
revistero_pared('revistero_pared_a', 'Revistero de pared (revistas del corazón y del motor)', ['#d23a2c', '#2f64b4', '#f0c030', '#e76a9a', '#3f9a4a', '#ee8a2a'], 41)
revistero_pared('revistero_pared_b', 'Revistero de pared (revistas de ciencia y cocina)', ['#2aa6a6', '#7a4aa0', '#e8d8b0', '#3f9a4a', '#ee8a2a', '#2f64b4'], 42)
P_ = [caja(0.8, 0.03, 0.4, y=0.015, c='#5a3a26'), caja(0.8, 1.3, 0.02, y=0.68, z=-0.19, c='#7a5a3c'), caja(0.03, 1.3, 0.4, x=-0.385, y=0.68, c='#5a3a26'), caja(0.03, 1.3, 0.4, x=0.385, y=0.68, c='#5a3a26')]
for j, y in enumerate((0.3, 0.62, 0.94, 1.26)):
    P_ += [caja(0.76, 0.02, 0.36, y=y, z=0.0, c='#6a4a30')]
    if j == 3:
        P_ += [p for i in range(5) for p in (cil(0.055, 0.055, 0.16, x=-0.28 + i * 0.14, y=y + 0.09, z=0.0, c='#cfe6e8', m='cristal', seg=8), cil(0.058, 0.058, 0.02, x=-0.28 + i * 0.14, y=y + 0.18, z=0.0, c='#d23a2c', m='plastico', seg=8))] + [
            caja(0.022, 0.022, 0.022, x=-0.31 + i * 0.14 + 0.03 * (k % 3 - 1), y=y + 0.06 + 0.04 * (k // 3), z=0.02 * (k % 2), c=BRIGHT[(i + k) % 8], m='comida') for i in range(5) for k in range(5)]
    elif j == 0:
        P_ += [caja(0.16, 0.014, 0.08, x=-0.3 + 0.15 * (i % 5), y=y + 0.017 + 0.016 * (i // 5), z=-0.05 + 0.1 * ((i // 5) % 2), c=('#6a3a22', '#d23a2c', '#2f64b4', '#eeeae0', '#f0c030')[i % 5], m='papel') for i in range(10)] + [caja(0.16, 0.014, 0.08, x=-0.3 + 0.15 * (i % 5), y=y + 0.017, z=0.1, c=('#6a3a22', '#d23a2c', '#2f64b4', '#eeeae0', '#f0c030')[(i + 2) % 5], m='papel') for i in range(5)]
    else:
        P_ += [caja(0.12, 0.2, 0.05, x=-0.3 + 0.15 * i, y=y + 0.11, z=0.0, c=BRIGHT[(i + j) % 8], m='plastico') for i in range(5)]
obj('expositor_golosinas', 'Expositor de chocolate, chicles y golosinas', 'ta_expositor', 18, 'comida', 'suelo', P_, nota='chocolate, 2 €')
def pila_prensa(id, nombre, cols, n, sd):
    r = random.Random(sd)
    P = []
    for i in range(n):
        P += [caja(0.3, 0.008, 0.4, y=0.004 + i * 0.008, z=0.0, c=cols[i % len(cols)], m='papel', r=[0, r.uniform(-4, 4), 0])]
    P += [caja(0.22, 0.003, 0.05, y=0.008 * n + 0.0015, z=-0.12, c='#2f2f34', m='papel'), caja(0.2, 0.003, 0.14, y=0.008 * n + 0.0015, z=0.05, c='#b8b4a8', m='papel')]
    obj(id, nombre, 'ta_papeleria', round(n * 0.12, 2), 'papel', 'superficie', P)
pila_prensa('es_pila_periodicos', 'Pila de periódicos del día', ['#e8e4d4', '#d8d4c4', '#efe8d4'], 8, 51)
pila_prensa('es_pila_revistas', 'Pila de revistas semanales', ['#e76a9a', '#2f64b4', '#f0c030', '#3f9a4a'], 6, 52)
obj('fardos_prensa', 'Fardos de prensa atados con cinta', 'ta_producto', 14, 'papel', 'suelo', [
    caja(0.7, 0.3, 0.45, y=0.15, c='#e0dccb', m='papel'), caja(0.68, 0.3, 0.44, x=0.02, y=0.45, z=0.0, c='#d6d2c0', m='papel', r=[0, 4, 0]), caja(0.7, 0.012, 0.47, y=0.15, x=0.18, c='#d6a050', m='papel'), caja(0.012, 0.3, 0.47, y=0.15, x=-0.1, z=0.0, c='#d6a050', m='papel'),
    caja(0.68, 0.012, 0.45, x=0.02, y=0.45, z=0.0, c='#d6a050', m='papel', r=[0, 4, 0])], nota='el reparto de la prensa de esta mañana')

def isla_revistas(id, nombre, pal, sd):
    r = random.Random(sd)
    P = [caja(1.0, 0.04, 0.72, y=0.02, c='#5a3a26'), caja(1.0, 1.4, 0.03, y=0.74, z=0.0, c='#7a5a3c'), caja(0.03, 1.4, 0.7, x=-0.485, y=0.74, c='#5a3a26'), caja(0.03, 1.4, 0.7, x=0.485, y=0.74, c='#5a3a26'), caja(1.0, 0.04, 0.72, y=1.46, c='#5a3a26')]
    for lado in (-1, 1):
        for j, y in enumerate((0.25, 0.56, 0.87, 1.18)):
            P += [caja(0.94, 0.015, 0.3, y=y, z=lado * 0.17, c='#6a4a30', r=[-lado * 14, 0, 0]), caja(0.94, 0.04, 0.012, y=y, z=lado * 0.33, c='#6a4a30')]
            for i in range(5):
                c = pal[r.randrange(len(pal))]
                P += [caja(0.17, 0.25, 0.004, x=-0.37 + i * 0.185, y=y + 0.15, z=lado * (0.12 + 0.012 * (i % 2)), c=c, m='papel', r=[-lado * 14, 0, 0]), caja(0.15, 0.05, 0.005, x=-0.37 + i * 0.185, y=y + 0.23, z=lado * (0.126 + 0.012 * (i % 2)), c='#eeeae0', m='papel', r=[-lado * 14, 0, 0])]
    obj(id, nombre, 'ta_expositor', 44, 'madera', 'suelo', P, nota='prensa y revistas por las dos caras')
isla_revistas('isla_revistas', 'Isla de prensa y revistas (dos caras)', ['#d23a2c', '#2f64b4', '#f0c030', '#e76a9a', '#3f9a4a', '#ee8a2a', '#7a4aa0', '#2aa6a6'], 61)
def expositor_postales():
    P = [cil(0.18, 0.2, 0.03, y=0.015, c='#2f2f32', m='metal', seg=12), cil(0.025, 0.025, 1.5, y=0.76, c='#9aa0a4', m='metal', seg=8), cil(0.2, 0.2, 0.02, y=1.5, c='#2f2f32', m='metal', seg=12)]
    for k in range(4):
        a = math.pi / 2 * k
        for j in range(5):
            for i in range(2):
                P += [caja(0.11, 0.075, 0.004, x=0.14 * math.sin(a) + 0.06 * (i - 0.5) * math.cos(a), y=0.32 + j * 0.21, z=0.14 * math.cos(a) - 0.06 * (i - 0.5) * math.sin(a), c=('#8ec0d8', '#e8c880', '#a8d0a0', '#e8b8c0')[(k + j + i) % 4], m='papel', r=[0, math.degrees(a), 0]),
                      caja(0.11, 0.03, 0.005, x=0.141 * math.sin(a) + 0.06 * (i - 0.5) * math.cos(a), y=0.305 + j * 0.21, z=0.141 * math.cos(a) - 0.06 * (i - 0.5) * math.sin(a), c=('#6a9a4a', '#a8683a', '#4a7a9a')[(k + j + i) % 3], m='papel', r=[0, math.degrees(a), 0])]
    obj('expositor_postales', 'Expositor giratorio de postales', 'ta_expositor', 9, 'metal', 'suelo', P, nota='postales del pueblo')
expositor_postales()
obj('balanza_postal', 'Báscula de franqueo', 'pequeño_electrodomestico', 1.4, 'plastico', 'superficie', [
    caja(0.2, 0.04, 0.14, c='#d8dadc', m='plastico'), caja(0.16, 0.008, 0.12, y=0.044, z=0.0, c='#b8bec2', m='metal'), caja(0.1, 0.05, 0.03, y=0.06, z=-0.06, c='#2f2f32', m='plastico'), caja(0.07, 0.02, 0.004, y=0.065, z=-0.044, c='#9ab0a0', m='plastico')])
estantes('estanteria_estanco_pared', 'Estantería de golosinas y papelería del estanco', 1.0, 0.3, [0.2, 0.5, 0.8, 1.1, 1.4, 1.7], 2.0, c='#7a4a36', cp='#9a6a4a', masa=44, zocalo=0.1)
regis('es_chocolatinas', 'Tabletas de chocolate', u_apilado(0.16, 0.07, 5, 0.012, ['#6a3a22', '#d23a2c', '#2f64b4', '#e8d8b0'], m='papel'), 2, 3, 0.17, 0.08, 0.06, 0.26, '#6a3a22', 0.1, mat='comida')
regis('es_chicles', 'Paquetes de chicles', u_caja(0.06, 0.1, 0.02, '#3f9a4a', '#eeeae0', banda=0.4), 5, 3, 0.065, 0.025, 0.1, 0.24, '#3f9a4a', 0.04, mat='papel')
regis('es_caramelos_bolsas', 'Bolsas de caramelos', lambda x, z: [caja(0.1, 0.18, 0.04, x=x, y=0.09, z=z, c=BRIGHT[int(abs(x * 100)) % 8], m='plastico'), caja(0.1, 0.03, 0.045, x=x, y=0.17, z=z, c='#eeeae0', m='plastico')], 4, 2, 0.11, 0.045, 0.18, 0.25, '#e76a9a', 0.2, mat='plastico')
regis('es_pipas_bolsas', 'Bolsas de pipas y frutos secos', lambda x, z: [caja(0.12, 0.2, 0.045, x=x, y=0.1, z=z, c=('#f0c030', '#3f9a4a', '#c8884a')[int(abs(x * 100)) % 3], m='plastico'), caja(0.12, 0.025, 0.05, x=x, y=0.19, z=z, c='#eeeae0', m='plastico')], 3, 2, 0.13, 0.05, 0.2, 0.26, '#f0c030', 0.15, mat='plastico')
regis('es_panuelos', 'Paquetes de pañuelos', u_caja(0.06, 0.1, 0.025, '#eeeae0', '#2f64b4', banda=0.4), 5, 2, 0.065, 0.03, 0.1, 0.22, '#eeeae0', 0.05, mat='papel')
regis('es_cerillas_mecheros', 'Cajas de cerillas y mecheros de repuesto', u_caja(0.05, 0.07, 0.02, '#d23a2c', '#f0c030', banda=0.5), 6, 3, 0.055, 0.025, 0.07, 0.25, '#d23a2c', 0.03, mat='papel')
regis('es_tarjetas_regalo', 'Tarjetas de regalo y de recarga', u_blister(0.07, 0.12, '#2f64b4', '#f0c030'), 5, 1, 0.08, 0.02, 0.12, 0.08, '#2f64b4', 0.05, hf=0.2)

obj('rotulo_estanco', 'Rótulo interior del estanco', 'decoracion', 3, 'madera', 'pared', [caja(1.5, 0.4, 0.03, y=2.55, z=0.015, c='#3a1f1a'), plano(1.44, 0.34, y=2.55, z=0.033, tex={'tipo': 'ta_rotulo_estanco', 'rotulo_local': True})])
obj('cartel_recargas', 'Cartel de recargas de móvil', 'cuadro', 0.6, 'papel', 'pared', [caja(0.6, 0.4, 0.012, y=2.2, z=0.006, c='#2f2f34', m='papel'), plano(0.56, 0.36, y=2.2, z=0.0135, tex={'tipo': 'ta_cartel_recargas'})])
obj('cartel_loteria', 'Cartel de lotería y apuestas', 'cuadro', 0.8, 'papel', 'pared', [caja(0.9, 0.35, 0.012, y=2.3, z=0.006, c='#2f5a3a', m='papel'), plano(0.86, 0.31, y=2.3, z=0.0135, tex={'tipo': 'ta_cartel_loteria'})])
obj('cartel_sellos', 'Cartel de sellos y franqueo', 'cuadro', 0.5, 'papel', 'pared', [caja(0.5, 0.3, 0.012, y=2.2, z=0.006, c='#27406e', m='papel'), plano(0.46, 0.26, y=2.2, z=0.0135, tex={'tipo': 'ta_cartel_sellos'})])
obj('cartel_menores', 'Cartel de prohibición de venta a menores', 'cuadro', 0.4, 'papel', 'pared', [caja(0.3, 0.2, 0.01, y=1.9, z=0.005, c='#eeeae0', m='papel'), plano(0.28, 0.18, y=1.9, z=0.0105, tex={'tipo': 'ta_cartel_menores'})])

# ================================================================== THE JEWELLER-WATCHMAKER / OPTICIAN (joyería)
ORO, PLATA, TERCIOPELO, AZUL_T = '#d4a83a', '#c8ccd0', '#6a1f2a', '#1f2a4a'
NOGAL, NOGAL_L = '#5a3e2e', '#6a4a38'
GEMAS = ['#f0f4f8', '#c0302a', '#2f64b4', '#3f9a4a', '#a070c8']
def anillo(x, y, z, gema, oro=ORO):
    """A ring standing on the velvet: the band as a thin disc, the stone a little cone on top (a ring is two centimetres)."""
    return [cil(0.011, 0.011, 0.004, x=x, y=y + 0.011, z=z, c=oro, m='metal', seg=8, r=[0, 0, 90]), cono(0.006, 0.01, x=x, y=y + 0.026, z=z, c=gema, m='cristal', seg=4)]
def reloj_plano(x, y, z, correa, esfera, oro=ORO):
    """A wrist watch lying flat: the strap along z, the case and the face on it."""
    return [caja(0.016, 0.004, 0.11, x=x, y=y + 0.002, z=z, c=correa, m='tela'), cil(0.026, 0.026, 0.008, x=x, y=y + 0.008, z=z, c=oro, m='metal', seg=8), cil(0.021, 0.021, 0.004, x=x, y=y + 0.0125, z=z, c=esfera, m='plastico', seg=8)]
def reloj_de_pie(x, y, z, correa, esfera, oro=ORO):
    """A wrist watch standing up on a shelf: the face towards the front, the strap curving behind."""
    return [caja(0.016, 0.05, 0.004, x=x, y=y + 0.035, z=z - 0.012, c=correa, m='tela'), caja(0.016, 0.05, 0.004, x=x, y=y + 0.035 + 0.045, z=z - 0.012, c=correa, m='tela'),
            cil(0.025, 0.025, 0.01, x=x, y=y + 0.055, z=z, c=oro, m='metal', seg=8, r=[90, 0, 0]), cil(0.02, 0.02, 0.005, x=x, y=y + 0.055, z=z + 0.006, c=esfera, m='plastico', seg=8, r=[90, 0, 0])]
def base_mostrador(P, h=0.72):
    return [caja(1.2, h, 0.58, y=h / 2, c=NOGAL), caja(1.1, h - 0.2, 0.01, y=h / 2, z=0.296, c=NOGAL_L), caja(1.2, 0.07, 0.01, y=0.035, z=0.296, c='#2f2f34')] + P
def vitrina_mostrador(id, nombre, contenido, nota):
    P = [caja(1.18, 0.26, 0.56, y=0.85, c='#cfe0e4', m='cristal'), caja(1.2, 0.02, 0.02, y=0.99, z=0.29, c=ORO, m='metal'), caja(1.2, 0.02, 0.02, y=0.99, z=-0.29, c=ORO, m='metal'), caja(0.02, 0.02, 0.6, x=-0.59, y=0.99, c=ORO, m='metal'), caja(0.02, 0.02, 0.6, x=0.59, y=0.99, c=ORO, m='metal'), caja(1.12, 0.02, 0.5, y=0.73, c=TERCIOPELO, m='tela')] + contenido
    obj(id, nombre, 'mostrador', 160, 'cristal', 'suelo', base_mostrador(P), fijo='estructural', nota=nota)
cont = []
for fila, z in enumerate((-0.17, 0.0, 0.17)):
    for i in range(9): cont += anillo(-0.5 + 0.125 * i, 0.74, z, GEMAS[(i + fila) % 5], oro=(ORO, PLATA)[(i + fila) % 3 == 0])
vitrina_mostrador('vitrina_mostrador_anillos', 'Vitrina de mostrador con anillos y alianzas', cont, 'anillos desde 40 €')
cont = []
for fila, z in enumerate((-0.12, 0.12)):
    for i in range(8): cont += reloj_plano(-0.49 + 0.14 * i, 0.74, z, ('#2f2f34', '#7a4a2a', '#c8ccd0', '#1f2a4a')[(i + fila) % 4], ('#f0eee6', '#1f2a4a', '#2f2f34', '#e8e0cc')[(i * 3 + fila) % 4], oro=(ORO, PLATA)[(i + fila) % 2])
vitrina_mostrador('vitrina_mostrador_relojes', 'Vitrina de mostrador con relojes de pulsera', cont, 'relojes desde 60 €')
cont = []
for i in range(5):
    x = -0.46 + 0.23 * i
    cont += [caja(0.12, 0.1, 0.08, x=x, y=0.79, z=-0.05, c=AZUL_T if i % 2 else '#3a1a22', m='tela'), cil(0.045, 0.055, 0.06, x=x, y=0.85, z=-0.05, c=AZUL_T if i % 2 else '#3a1a22', m='tela', seg=8),
             caja(0.006, 0.14, 0.004, x=x - 0.035, y=0.83, z=-0.01, c=ORO, m='metal', r=[0, 0, 20]), caja(0.006, 0.14, 0.004, x=x + 0.035, y=0.83, z=-0.01, c=ORO, m='metal', r=[0, 0, -20]), cono(0.012, 0.025, x=x, y=0.76, z=-0.0, c=GEMAS[i % 5], m='cristal', seg=4)]
    cont += [caja(0.012, 0.045, 0.004, x=x - 0.07 + 0.14 * k, y=0.76, z=0.18, c=ORO, m='metal') for k in range(2)] + [cono(0.007, 0.012, x=x - 0.07 + 0.14 * k, y=0.78, z=0.18, c=GEMAS[(i + k + 2) % 5], m='cristal', seg=4) for k in range(2)]
vitrina_mostrador('vitrina_mostrador_collares', 'Vitrina de mostrador con collares y pendientes', cont, 'collares y pendientes')
obj('mostrador_caja_joyeria', 'Mostrador de caja de la joyería (1,2 m)', 'mostrador', 150, 'madera', 'suelo', [
    caja(1.2, 0.92, 0.52, z=-0.03, c=NOGAL), caja(1.2, 0.06, 0.66, y=0.97, z=0.0, c='#5a4030'), caja(1.1, 0.55, 0.01, y=0.5, z=0.236, c=NOGAL_L), caja(1.2, 0.07, 0.01, y=0.035, z=0.236, c='#2f2f34'), caja(1.2, 0.012, 0.02, y=0.3, z=0.26, c=ORO, m='metal'),
    caja(0.4, 0.15, 0.012, x=-0.3, y=0.7, z=0.244, c='#5a4030'), caja(0.4, 0.15, 0.012, x=0.3, y=0.7, z=0.244, c='#5a4030')], fijo='estructural', superficies=[{'y': 1.0, 'margen': 0.04}], nota='el mostrador de caja, con la báscula de precisión')
obj('vitrina_isla_joyas', 'Vitrina de isla con joyas y relojes', 'vitrina', 70, 'cristal', 'suelo', [
    caja(1.0, 0.6, 0.55, y=0.3, c=NOGAL), caja(1.0, 0.04, 0.6, y=0.62, c='#2f2f34'), caja(0.96, 0.34, 0.52, y=0.81, c='#cfe0e4', m='cristal'), caja(1.0, 0.02, 0.02, y=0.99, z=0.28, c=ORO, m='metal'), caja(1.0, 0.02, 0.02, y=0.99, z=-0.28, c=ORO, m='metal'), caja(0.02, 0.02, 0.58, x=-0.49, y=0.99, c=ORO, m='metal'), caja(0.02, 0.02, 0.58, x=0.49, y=0.99, c=ORO, m='metal'), caja(0.9, 0.02, 0.46, y=0.65, c=AZUL_T, m='tela')] + [
    p for i in range(4) for p in reloj_plano(-0.36 + 0.24 * i, 0.66, -0.1, ('#2f2f34', '#7a4a2a', '#c8ccd0', '#1f2a4a')[i], ('#f0eee6', '#1f2a4a', '#2f2f34', '#e8e0cc')[i])] + [
    p for i in range(6) for p in anillo(-0.38 + 0.15 * i, 0.66, 0.13, GEMAS[i % 5])], fijo='estructural', nota='todo bajo llave')
def vitrina_pared(id, nombre, filas_fn, nota, vitrinas=4):
    P = [caja(1.0, 0.85, 0.34, y=0.425, c=NOGAL, z=0.17), caja(1.04, 0.03, 0.38, y=0.865, z=0.19, c=NOGAL_L), caja(1.0, 1.25, 0.02, y=1.5, z=0.01, c='#26262a'), caja(0.02, 1.25, 0.3, x=-0.49, y=1.5, z=0.15, c=NOGAL), caja(0.02, 1.25, 0.3, x=0.49, y=1.5, z=0.15, c=NOGAL),
         caja(1.0, 0.03, 0.34, y=2.135, z=0.17, c=NOGAL), caja(0.96, 1.2, 0.008, y=1.5, z=0.325, c='#cfe0e4', m='cristal'), caja(0.9, 0.03, 0.01, y=2.08, z=0.3, c='#f0e8d4', m='cristal', luz=True)]
    for j, y in enumerate((1.05, 1.35, 1.65, 1.95)[:vitrinas]):
        P += [caja(0.96, 0.015, 0.28, y=y - 0.0075, z=0.15, c='#2c2c30'), caja(0.94, 0.005, 0.26, y=y + 0.0025, z=0.15, c=TERCIOPELO if j % 2 else AZUL_T, m='tela')] + filas_fn(y + 0.005, j)
    obj(id, nombre, 'vitrina', 110, 'cristal', 'suelo', P, fijo=FIJO, nota=nota)
def fila_relojes(y, j):
    P = []
    for i in range(6): P += reloj_de_pie(-0.4 + 0.16 * i, y, 0.15, ('#2f2f34', '#7a4a2a', '#c8ccd0', '#1f2a4a', '#3a2a24', '#6a1f2a')[(i + j) % 6], ('#f0eee6', '#1f2a4a', '#2f2f34', '#e8e0cc')[(i * 3 + j) % 4], oro=(ORO, PLATA)[(i + j) % 2])
    return P
vitrina_pared('vitrina_pared_relojes', 'Vitrina de pared con relojes', fila_relojes, 'relojes, 80 €')
def fila_collares(y, j):
    P = []
    for i in range(4):
        x = -0.36 + 0.24 * i
        P += [caja(0.09, 0.12, 0.06, x=x, y=y + 0.06, z=0.15, c=('#3a1a22', '#e8dcc0')[(i + j) % 2], m='tela'), cil(0.035, 0.045, 0.05, x=x, y=y + 0.145, z=0.15, c=('#3a1a22', '#e8dcc0')[(i + j) % 2], m='tela', seg=8),
              caja(0.006, 0.12, 0.004, x=x - 0.03, y=y + 0.12, z=0.19, c=ORO, m='metal', r=[0, 0, 24]), caja(0.006, 0.12, 0.004, x=x + 0.03, y=y + 0.12, z=0.19, c=ORO, m='metal', r=[0, 0, -24]), cono(0.012, 0.025, x=x, y=y + 0.07, z=0.19, c=GEMAS[(i + j) % 5], m='cristal', seg=4)]
    return P
vitrina_pared('vitrina_pared_joyas', 'Vitrina de pared con collares y pendientes', fila_collares, 'joyas de oro y plata')
def fila_perfumes(y, j):
    P = []
    for i in range(6):
        c = ('#e8c880', '#7ab0c8', '#e0a4b8', '#a8d0a0', '#d8c0e8', '#eeeae0')[(i + j) % 6]
        P += [caja(0.05, 0.1 + 0.02 * (i % 3), 0.04, x=-0.4 + 0.16 * i, y=y + 0.05 + 0.01 * (i % 3), z=0.15, c=c, m='cristal'), cil(0.012, 0.012, 0.03, x=-0.4 + 0.16 * i, y=y + 0.115 + 0.02 * (i % 3), z=0.15, c=ORO, m='metal', seg=8)]
    return P
vitrina_pared('vitrina_perfumes', 'Vitrina de perfumes', fila_perfumes, 'perfumes, 35 €')
def pared_gafas(id, nombre, sd, marcos):
    r = random.Random(sd)
    P = [caja(1.0, 1.1, 0.02, y=1.7, z=0.01, c='#8a7a66'), caja(1.04, 0.03, 0.04, y=2.26, z=0.02, c=NOGAL), caja(1.04, 0.03, 0.04, y=1.14, z=0.02, c=NOGAL)]
    for fila, y in enumerate((2.05, 1.75, 1.45)):
        P += [caja(0.96, 0.012, 0.045, y=y - 0.07, z=0.04, c=NOGAL)]
        for i in range(5):
            x = -0.38 + 0.19 * i
            mc = r.choice(marcos)
            tinte = r.choice(('#bcd6dc', '#bcd6dc', '#6a5a4a', '#2f2f34', '#8aa8c8'))
            P += [caja(0.07, 0.048, 0.004, x=x - 0.042, y=y, z=0.05, c=tinte, m='cristal'), caja(0.07, 0.048, 0.004, x=x + 0.042, y=y, z=0.05, c=tinte, m='cristal'),
                  caja(0.078, 0.008, 0.008, x=x - 0.042, y=y + 0.026, z=0.05, c=mc, m='plastico'), caja(0.078, 0.008, 0.008, x=x + 0.042, y=y + 0.026, z=0.05, c=mc, m='plastico'), caja(0.078, 0.008, 0.008, x=x - 0.042, y=y - 0.026, z=0.05, c=mc, m='plastico'), caja(0.078, 0.008, 0.008, x=x + 0.042, y=y - 0.026, z=0.05, c=mc, m='plastico'),
                  caja(0.008, 0.05, 0.008, x=x - 0.081, y=y, z=0.05, c=mc, m='plastico'), caja(0.008, 0.05, 0.008, x=x + 0.081, y=y, z=0.05, c=mc, m='plastico'), caja(0.008, 0.05, 0.008, x=x, y=y, z=0.05, c=mc, m='plastico'), caja(0.02, 0.008, 0.008, x=x, y=y + 0.012, z=0.05, c=mc, m='plastico'),
                  caja(0.006, 0.006, 0.04, x=x - 0.088, y=y + 0.02, z=0.03, c=mc, m='plastico'), caja(0.006, 0.006, 0.04, x=x + 0.088, y=y + 0.02, z=0.03, c=mc, m='plastico')]
    obj(id, nombre, 'ta_expositor', 8, 'madera', 'pared', P, fijo=FIJO, nota='gafas graduadas desde 90 €')
pared_gafas('pared_gafas_a', 'Pared de monturas (negras y carey)', 81, ['#2f2f34', '#6a4a2a', '#3a2a24', '#8a6a3a'])
pared_gafas('pared_gafas_b', 'Pared de monturas (colores y metal)', 82, ['#c0302a', '#2f64b4', '#c8ccd0', '#d4a83a', '#3f9a4a', '#2f2f34'])
obj('espejo_optica_mesa', 'Espejo de mesa para probarse las gafas', 'espejo', 2, 'cristal', 'superficie', [caja(0.34, 0.4, 0.02, y=0.2, z=-0.04, c='#5a4030', r=[-8, 0, 0]), caja(0.3, 0.36, 0.006, y=0.2, z=-0.026, c='#c3d3da', m='metal', r=[-8, 0, 0]), caja(0.3, 0.02, 0.1, y=0.01, z=-0.02, c='#5a4030')])
obj('mesa_optica', 'Mesita de la óptica con espejo y lámpara', 'mesa', 18, 'madera', 'suelo', [caja(0.9, 0.04, 0.5, y=0.73, c='#5a4030')] + [caja(0.04, 0.71, 0.04, x=sx * 0.41, y=0.355, z=sz * 0.21, c=NOGAL) for sx in (-1, 1) for sz in (-1, 1)] + [caja(0.84, 0.1, 0.012, y=0.66, z=0.245, c=NOGAL_L)], superficies=[{'y': 0.75, 'margen': 0.05}])
obj('silla_cliente_joyeria', 'Silla tapizada para el cliente', 'silla', 5.5, 'madera', 'suelo', [
    caja(0.46, 0.06, 0.44, y=0.45, c='#6a1f2a', m='tela'), caja(0.46, 0.34, 0.04, y=0.7, z=-0.2, c='#6a1f2a', m='tela')] + [caja(0.035, 0.43, 0.035, x=sx * 0.2, y=0.215, z=sz * 0.18, c=NOGAL) for sx in (-1, 1) for sz in (-1, 1)] + [caja(0.035, 0.5, 0.035, x=sx * 0.2, y=0.7, z=-0.2, c=NOGAL) for sx in (-1, 1)],
    modificadores=['SEAT'], asientos=[{'p': [0, 0.48, 0.02], 'h': 0.48, 'anim': 'silla'}])
# the watchmaker's bench
obj('banco_relojero', 'Banco de trabajo del relojero', 'mesa', 40, 'madera', 'suelo', [
    caja(1.1, 0.06, 0.6, y=0.84, c='#8a5a36'), caja(1.0, 0.004, 0.5, y=0.872, c='#2f5a3a', m='tela'), caja(0.5, 0.6, 0.55, x=-0.28, y=0.51, z=0.0, c=NOGAL), caja(0.04, 0.78, 0.04, x=0.5, y=0.39, z=-0.26, c=NOGAL), caja(0.04, 0.78, 0.04, x=0.5, y=0.39, z=0.26, c=NOGAL),
    caja(0.22, 0.12, 0.012, x=-0.28, y=0.62, z=0.28, c=NOGAL_L), caja(0.22, 0.12, 0.012, x=-0.28, y=0.42, z=0.28, c=NOGAL_L),
    # (the lamp on its arm, the glass dome with a movement under it, the loupe, the tray of little parts)
    cil(0.07, 0.08, 0.02, x=0.4, y=0.88, z=-0.2, c='#2f2f34', m='metal', seg=8), cil(0.008, 0.008, 0.4, x=0.4, y=1.08, z=-0.2, c='#2f2f34', m='metal', seg=6), caja(0.3, 0.008, 0.008, x=0.26, y=1.28, z=-0.2, c='#2f2f34', m='metal'),
    cil(0.05, 0.08, 0.06, x=0.12, y=1.26, z=-0.2, c='#f0e8d4', m='plastico', luz=True, seg=8),
    cil(0.05, 0.05, 0.07, x=-0.05, y=0.905, z=0.05, c='#cfe0e4', m='cristal', seg=12), cil(0.018, 0.018, 0.012, x=-0.05, y=0.88, z=0.05, c=ORO, m='metal', seg=8), cil(0.03, 0.03, 0.02, x=0.2, y=0.9, z=0.15, c='#2f2f34', m='plastico', seg=8), cil(0.03, 0.03, 0.01, x=0.2, y=0.915, z=0.15, c='#cfe0e4', m='cristal', seg=8),
    caja(0.16, 0.012, 0.1, x=0.3, y=0.88, z=0.12, c='#d8dadc', m='plastico'), caja(0.012, 0.012, 0.1, x=0.37, y=0.9, z=0.12, c='#d8dadc', m='plastico'), caja(0.14, 0.02, 0.012, x=-0.2, y=0.882, z=0.2, c=PLATA, m='metal'), caja(0.12, 0.02, 0.012, x=-0.2, y=0.882, z=0.22, c=ORO, m='metal')],
    superficies=[{'y': 0.874, 'margen': 0.05}], nota='el relojero trabaja aquí, con su lámpara y su lupa')
obj('taburete_relojero', 'Taburete del relojero', 'taburete', 4.5, 'madera', 'suelo', [cil(0.2, 0.2, 0.04, y=0.62, c='#6a1f2a', m='tela', seg=12), cil(0.02, 0.02, 0.58, y=0.3, c=NOGAL, m='madera', seg=8), cil(0.18, 0.2, 0.025, y=0.0125, c=NOGAL, m='madera', seg=12)] + [caja(0.18, 0.025, 0.025, x=0, y=0.24, z=0, c=NOGAL, r=[0, 60 * k, 0]) for k in range(3)],
    modificadores=['SEAT'], asientos=[{'p': [0, 0.64, 0], 'h': 0.64, 'anim': 'taburete_alto'}])
obj('caja_fuerte_pequena', 'Caja fuerte pequeña de acero', 'caja_fuerte', 220, 'metal', 'suelo', [
    caja(0.5, 0.6, 0.48, y=0.3, c='#5a6a62', m='metal'), caja(0.42, 0.52, 0.02, y=0.3, z=0.25, c='#6f8078', m='metal'), cil(0.05, 0.05, 0.02, x=-0.02, y=0.36, z=0.27, c='#2f2f34', m='metal', seg=12, r=[90, 0, 0]), cil(0.03, 0.03, 0.01, x=-0.02, y=0.36, z=0.285, c=PLATA, m='metal', seg=12, r=[90, 0, 0]),
    caja(0.12, 0.03, 0.03, x=0.13, y=0.3, z=0.28, c=PLATA, m='metal'), caja(0.1, 0.05, 0.01, x=-0.02, y=0.5, z=0.262, c='#2f2f34', m='plastico')], fijo=FIJO, nota='lo que no se enseña')
def alfombra(id, nombre, c1, c2, w=2.4, d=1.6):
    obj(id, nombre, 'textil', 5.5, 'tela', 'suelo', [plano(w, d, y=0.0085, c=c2, m='tela', r=[-90, 0, 0]), plano(w - 0.12, d - 0.12, y=0.0095, c=c1, m='tela', r=[-90, 0, 0]), plano(w - 0.5, d - 0.5, y=0.0105, c=oscuro(c1, 0.82), m='tela', r=[-90, 0, 0])], nota='una alfombra que amortigua los pasos')
alfombra('alfombra_burdeos', 'Alfombra burdeos con cenefa dorada', '#7a2a36', '#b8984a')
alfombra('alfombra_verde', 'Alfombra verde con cenefa crema', '#3a6a48', '#cfc09a')
# small things for trays, tops and counters
obj('jy_bandeja_anillos', 'Bandeja de terciopelo con anillos', 'ta_joya', 0.5, 'tela', 'superficie', [caja(0.26, 0.015, 0.18, c='#2f2f34', m='plastico'), caja(0.24, 0.008, 0.16, y=0.0115, c=TERCIOPELO, m='tela')] + [p for fila in range(2) for i in range(5) for p in anillo(-0.1 + 0.05 * i, 0.015, -0.04 + 0.08 * fila, GEMAS[(i + fila) % 5], oro=(ORO, PLATA)[(i + fila) % 3 == 0])])
obj('jy_bandeja_relojes', 'Bandeja de terciopelo con relojes', 'ta_joya', 0.9, 'tela', 'superficie', [caja(0.4, 0.015, 0.22, c='#2f2f34', m='plastico'), caja(0.38, 0.008, 0.2, y=0.0115, c=AZUL_T, m='tela')] + [p for i in range(5) for p in reloj_plano(-0.15 + 0.075 * i, 0.015, 0.0, ('#2f2f34', '#7a4a2a', '#c8ccd0', '#6a1f2a', '#1f2a4a')[i], ('#f0eee6', '#1f2a4a', '#2f2f34', '#e8e0cc', '#f0eee6')[i], oro=(ORO, PLATA)[i % 2])])
obj('jy_busto_collares', 'Busto de terciopelo con un collar', 'ta_joya', 0.8, 'tela', 'superficie', [cil(0.06, 0.07, 0.03, c='#2f2f34', m='plastico', seg=8), caja(0.1, 0.14, 0.07, y=0.1, c='#d8c8a8', m='tela'), cil(0.04, 0.05, 0.06, y=0.2, c='#d8c8a8', m='tela', seg=8), caja(0.005, 0.12, 0.004, x=-0.04, y=0.14, z=0.045, c=ORO, m='metal', r=[0, 0, 22]), caja(0.005, 0.12, 0.004, x=0.04, y=0.14, z=0.045, c=ORO, m='metal', r=[0, 0, -22]), cono(0.014, 0.03, y=0.07, z=0.045, c='#2f64b4', m='cristal', seg=4)])
obj('jy_cojin_alianzas', 'Cojín con alianzas y estuche', 'ta_joya', 0.4, 'tela', 'superficie', [caja(0.12, 0.03, 0.1, c='#e8dcc0', m='tela'), cil(0.016, 0.016, 0.006, x=-0.025, y=0.035, c=ORO, m='metal', seg=8, r=[0, 0, 90]), cil(0.014, 0.014, 0.006, x=0.025, y=0.035, c=PLATA, m='metal', seg=8, r=[0, 0, 90]), caja(0.1, 0.05, 0.08, x=0.16, y=0.025, z=0.0, c=AZUL_T, m='tela'), caja(0.1, 0.012, 0.08, x=0.16, y=0.056, z=-0.03, c='#16203a', m='tela', r=[-50, 0, 0])])
obj('jy_estuches_joyas', 'Estuches de joyería apilados', 'caja', 0.8, 'tela', 'superficie', [caja(0.12, 0.05, 0.12, c=AZUL_T, m='tela'), caja(0.12, 0.004, 0.12, y=0.027, c=ORO, m='metal'), caja(0.1, 0.05, 0.1, x=0.02, y=0.077, c=TERCIOPELO, m='tela', r=[0, 12, 0]), caja(0.1, 0.004, 0.1, x=0.02, y=0.104, c=ORO, m='metal', r=[0, 12, 0]), caja(0.09, 0.04, 0.09, x=-0.14, y=0.02, c='#e8dcc0', m='tela')])
obj('jy_lupa_y_pinzas', 'Lupa de joyero y pinzas', 'ta_joya', 0.2, 'metal', 'superficie', [cil(0.025, 0.025, 0.004, y=0.015, c='#cfe0e4', m='cristal', seg=12), caja(0.012, 0.012, 0.07, y=0.012, z=0.06, c='#2f2f34', m='plastico'), caja(0.004, 0.004, 0.11, x=0.07, y=0.002, z=0.0, c=PLATA, m='metal'), caja(0.004, 0.004, 0.11, x=0.075, y=0.002, z=0.0, c=PLATA, m='metal')])
obj('jy_expositor_pendientes', 'Expositor de pendientes con tarjetas', 'ta_joya', 0.6, 'plastico', 'superficie', [caja(0.34, 0.012, 0.1, c='#2f2f34', m='plastico'), caja(0.34, 0.2, 0.008, y=0.11, z=-0.04, c='#e8dcc0', m='papel', r=[-10, 0, 0])] + [p for fila in range(2) for i in range(5) for p in (cil(0.008, 0.008, 0.004, x=-0.13 + 0.065 * i, y=0.07 + 0.08 * fila, z=-0.025, c=(ORO, PLATA)[(i + fila) % 2], m='metal', seg=8, r=[90, 0, 0]), cono(0.005, 0.014, x=-0.13 + 0.065 * i, y=0.05 + 0.08 * fila, z=-0.022, c=GEMAS[(i + fila) % 5], m='cristal', seg=4))])
obj('expositor_gafas_mostrador', 'Expositor giratorio de gafas de sol de mostrador', 'ta_expositor', 1.8, 'plastico', 'superficie', [cil(0.08, 0.09, 0.015, y=0.0075, c='#2f2f34', m='metal', seg=12), cil(0.012, 0.012, 0.3, y=0.165, c=PLATA, m='metal', seg=8)] + [
    p for k in range(4) for p in (caja(0.06, 0.03, 0.004, x=0.07 * math.sin(math.pi / 2 * k), y=0.2 + 0.07 * (k % 2), z=0.07 * math.cos(math.pi / 2 * k), c=('#2f2f34', '#6a4a2a', '#c0302a', '#2f64b4')[k], m='plastico', r=[0, math.degrees(math.pi / 2 * k), 0]),
                                 caja(0.052, 0.024, 0.003, x=0.0705 * math.sin(math.pi / 2 * k), y=0.2 + 0.07 * (k % 2), z=0.0705 * math.cos(math.pi / 2 * k), c='#3a3a40', m='cristal', r=[0, math.degrees(math.pi / 2 * k), 0]))])
obj('consola_joyeria', 'Consola de madera con tapa de mármol', 'mueble', 28, 'madera', 'suelo', [
    caja(1.0, 0.04, 0.42, y=0.86, c='#d8d2c0', m='piedra')] + [caja(0.05, 0.84, 0.05, x=sx * 0.45, y=0.42, z=sz * 0.17, c=NOGAL) for sx in (-1, 1) for sz in (-1, 1)] + [caja(0.9, 0.12, 0.4, y=0.78, c=NOGAL_L), caja(0.9, 0.03, 0.36, y=0.2, c=NOGAL)],
    superficies=[{'y': 0.88, 'margen': 0.04}], nota='donde se exponen las bandejas y los bustos')
obj('rotulo_joyeria', 'Rótulo interior de la joyería', 'decoracion', 3, 'madera', 'pared', [caja(1.5, 0.4, 0.03, y=2.55, z=0.015, c='#2a2220'), plano(1.44, 0.34, y=2.55, z=0.033, tex={'tipo': 'ta_rotulo_joyeria', 'rotulo_local': True})])
obj('cartel_optica', 'Cartel de la óptica', 'cuadro', 0.6, 'papel', 'pared', [caja(0.6, 0.4, 0.012, y=2.62, z=0.006, c='#1f2a4a', m='papel'), plano(0.56, 0.36, y=2.62, z=0.0135, tex={'tipo': 'ta_cartel_optica'})])
obj('cartel_arreglos', 'Cartel de arreglos y grabados', 'cuadro', 0.5, 'papel', 'pared', [caja(0.4, 0.28, 0.012, y=2.2, z=0.006, c='#2f2f34', m='papel'), plano(0.36, 0.24, y=2.2, z=0.0135, tex={'tipo': 'ta_cartel_arreglos'})])

# ---- florist's wall decoration and the hanging pots
for k, (n_, hoja, flor) in {'a': ('helechos', '#4a8a3a', None), 'b': ('una rosa', '#3f7a3a', '#c0302a'), 'c': ('hojas de ginkgo', '#c8a030', None)}.items():
    P = [caja(0.45, 0.6, 0.03, y=1.7, z=0.015, c='#cfb48a'), caja(0.39, 0.54, 0.006, y=1.7, z=0.033, c='#f0e8d4', m='papel')]
    for i in range(7):
        P.append(caja(0.05, 0.2 - 0.012 * i, 0.004, x=-0.1 + 0.035 * i, y=1.62 + 0.03 * (3 - abs(i - 3)), z=0.038, c=hoja, m='papel', r=[0, 0, 18 - 6 * i]))
    P.append(caja(0.004, 0.3, 0.004, y=1.62, z=0.037, c='#5a7a3a', m='papel'))
    if flor: P += [cil(0.05, 0.035, 0.05, y=1.82, z=0.04, c=flor, m='papel', seg=8, r=[90, 0, 0])]
    obj('cuadro_botanico_' + k, 'Lámina botánica enmarcada (%s)' % n_, 'cuadro', 1.2, 'madera', 'pared', P)
obj('planta_colgante', 'Cesta colgante con una planta', 'planta', 3, 'madera', 'techo', [
    cil(0.004, 0.004, 0.5, y=-0.25, c='#7a7e82', m='metal', seg=4), cil(0.13, 0.1, 0.1, y=-0.55, c='#c8a468', m='madera', seg=8), cil(0.15, 0.13, 0.06, y=-0.47, c='#4a8a3a', m='comida', seg=8)] + [
    p for i in range(8) for p in (caja(0.02, 0.3 + 0.05 * (i % 3), 0.004, x=0.11 * math.sin(i * 0.785), y=-0.7 - 0.025 * (i % 3), z=0.11 * math.cos(i * 0.785), c=('#4a8a3a', '#3f7a3a')[i % 2], m='comida', r=[0, math.degrees(i * 0.785), 0]),
                                  caja(0.03, 0.03, 0.004, x=0.11 * math.sin(i * 0.785), y=-0.88 - 0.05 * (i % 3), z=0.11 * math.cos(i * 0.785), c=('#d23a2c', '#e76a9a')[i % 2], m='comida', r=[0, math.degrees(i * 0.785), 0]))], nota='una planta colgante, 12 €')

# ---- more for the jeweller's
def reloj_pendulo():
    P = [caja(0.4, 1.7, 0.22, y=0.85, z=0.0, c='#6a4a30'), caja(0.46, 0.06, 0.26, y=1.73, c='#5a3e2e'), caja(0.46, 0.08, 0.26, y=0.04, c='#5a3e2e'), caja(0.3, 0.55, 0.012, y=0.62, z=0.116, c='#bcd6dc', m='cristal'),
         caja(0.3, 0.012, 0.012, y=0.9, z=0.116, c=ORO, m='metal'), cil(0.14, 0.14, 0.02, y=1.38, z=0.113, c='#efe8d4', m='plastico', seg=16, r=[90, 0, 0]), cil(0.15, 0.15, 0.008, y=1.38, z=0.108, c=ORO, m='metal', seg=16, r=[90, 0, 0]),
         caja(0.01, 0.1, 0.006, y=1.43, z=0.126, c='#2f2f34', m='plastico'), caja(0.08, 0.01, 0.006, x=0.03, y=1.38, z=0.126, c='#2f2f34', m='plastico'),
         caja(0.01, 0.4, 0.006, y=0.55, z=0.0, c=ORO, m='metal'), cil(0.07, 0.07, 0.012, y=0.37, z=0.0, c=ORO, m='metal', seg=12, r=[90, 0, 0])]
    obj('reloj_pendulo_pie', 'Reloj de pie de péndulo', 'mueble', 38, 'madera', 'suelo', P, nota='suena a las horas')
reloj_pendulo()
obj('maniqui_busto_joyas', 'Busto de terciopelo con collares sobre pie', 'ta_expositor', 6, 'tela', 'suelo', [
    cil(0.15, 0.17, 0.03, y=0.015, c='#2f2f34', m='metal', seg=12), cil(0.02, 0.02, 0.9, y=0.48, c=ORO, m='metal', seg=8), caja(0.26, 0.3, 0.14, y=1.18, c='#d8c8a8', m='tela'), cil(0.06, 0.08, 0.1, y=1.38, c='#d8c8a8', m='tela', seg=8)] + [
    p for k, (rr, c) in enumerate(((0.1, ORO), (0.14, PLATA), (0.18, ORO))) for p in (caja(0.01, 0.1 + 0.05 * k, 0.006, x=-rr * 0.7, y=1.3 - 0.03 * k, z=0.08, c=c, m='metal', r=[0, 0, 24 + 8 * k]), caja(0.01, 0.1 + 0.05 * k, 0.006, x=rr * 0.7, y=1.3 - 0.03 * k, z=0.08, c=c, m='metal', r=[0, 0, -24 - 8 * k]), cono(0.014, 0.03, y=1.17 - 0.06 * k, z=0.082, c=GEMAS[k + 1], m='cristal', seg=4))], nota='collares, 120 €')
cont = []
for fila in range(2):
    for i in range(4): cont += reloj_plano(-0.36 + 0.24 * i, 0.66, -0.13 + 0.26 * fila, ('#2f2f34', '#7a4a2a', '#c8ccd0', '#1f2a4a')[(i + fila) % 4], ('#f0eee6', '#1f2a4a', '#2f2f34', '#e8e0cc')[(i + 2 * fila) % 4], oro=(ORO, PLATA)[(i + fila) % 2])
obj('vitrina_isla_relojes', 'Vitrina de isla con relojes de pulsera', 'vitrina', 70, 'cristal', 'suelo', [
    caja(1.0, 0.6, 0.55, y=0.3, c=NOGAL), caja(1.0, 0.04, 0.6, y=0.62, c='#2f2f34'), caja(0.96, 0.34, 0.52, y=0.81, c='#cfe0e4', m='cristal'), caja(1.0, 0.02, 0.02, y=0.99, z=0.28, c=ORO, m='metal'), caja(1.0, 0.02, 0.02, y=0.99, z=-0.28, c=ORO, m='metal'),
    caja(0.02, 0.02, 0.58, x=-0.49, y=0.99, c=ORO, m='metal'), caja(0.02, 0.02, 0.58, x=0.49, y=0.99, c=ORO, m='metal'), caja(0.9, 0.02, 0.46, y=0.65, c=TERCIOPELO, m='tela')] + cont, fijo='estructural', nota='relojes de pulsera')
for k, (n_, motivo) in {'a': ('un diamante', 'gema'), 'b': ('un reloj antiguo', 'reloj')}.items():
    P = [caja(0.5, 0.65, 0.03, y=1.7, z=0.015, c=NOGAL), caja(0.42, 0.57, 0.006, y=1.7, z=0.033, c='#2a2220', m='papel')]
    if motivo == 'gema':
        P += [caja(0.2, 0.2, 0.006, y=1.7, z=0.04, c='#e8f0f4', m='cristal', r=[0, 0, 45]), caja(0.1, 0.1, 0.007, y=1.7, z=0.044, c='#b8d0e0', m='cristal', r=[0, 0, 45]), caja(0.3, 0.012, 0.006, y=1.52, z=0.04, c=ORO, m='metal')]
    else:
        P += [cil(0.13, 0.13, 0.01, y=1.72, z=0.04, c=ORO, m='metal', seg=16, r=[90, 0, 0]), cil(0.11, 0.11, 0.012, y=1.72, z=0.042, c='#efe8d4', m='plastico', seg=16, r=[90, 0, 0]), caja(0.01, 0.09, 0.006, y=1.76, z=0.05, c='#2f2f34', m='plastico'), caja(0.07, 0.01, 0.006, x=0.025, y=1.72, z=0.05, c='#2f2f34', m='plastico')]
    obj('cuadro_joyeria_' + k, 'Cuadro de %s' % n_, 'cuadro', 2, 'madera', 'pared', P)

# ==== FIN ====
json.dump({'version': 1, 'familia': 'tiendas_a', 'categorias': CATEGORIAS, 'objetos': OUT}, open(os.path.join(ROOT, 'data', 'objetos', 'tiendas_a.json'), 'w'), ensure_ascii=False, indent=1)
print('objetos de tiendas_a:', len(OUT))
