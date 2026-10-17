# The objects of the shops (technical backlog, I-02 and X-01/X-02): a clothes shop, a pharmacy and a supermarket — each one a
# few primitives (boxes, cylinders, spheres, cones and textured planes, in metres), its class of interaction, its mass, its
# material and what it stands on. The script is the model: it writes data/objetos/comercio.json.
# Frame of an object: x across, y up from its foot, z out of its front (+z faces whoever uses it; its back at -z).
# Products are FACINGS: a row of identical units at the front of a shelf, and a solid block of the same colour behind
# (the stock), so that a shelf looks full with few pieces. No real brand anywhere: invented names, plain colours.
#   python3 tools/interiores/catalogo_comercio.py
import json, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
OUT = []

def caja(w, h, d, x=0, y=None, z=0, c='#888888', m='madera', **k):
    return {'f': 'caja', 'd': [w, h, d], 'p': [x, h / 2 if y is None else y, z], 'c': c, 'm': m, **k}
def cil(rt, rb, h, x=0, y=None, z=0, c='#888888', m='metal', **k):
    return {'f': 'cil', 'd': [rt, rb, h], 'p': [x, h / 2 if y is None else y, z], 'c': c, 'm': m, **k}
def esf(r, x=0, y=0, z=0, c='#888888', m='comida', **k):
    return {'f': 'esfera', 'd': [r], 'p': [x, y, z], 'c': c, 'm': m, **k}
def cono(r, h, x=0, y=None, z=0, c='#888888', m='metal', **k):
    return {'f': 'cono', 'd': [r, h], 'p': [x, h / 2 if y is None else y, z], 'c': c, 'm': m, **k}
def plano(w, h, x=0, y=0, z=0, tex=None, c='#ffffff', m='papel', **k):
    return {'f': 'plano', 'd': [w, h], 'p': [x, y, z], 'c': c, 'm': m, **({'tex': tex} if tex else {}), **k}

def obj(id, nombre, categoria, clase, masa, material, soporte, partes, **k):
    OUT.append({'id': id, 'nombre': nombre, 'categoria': categoria, 'clase': clase, 'masa': masa, 'material': material, 'soporte': soporte, 'partes': partes, **k})

# the categories this family brings (their mass ranges, kg)
CATEGORIAS = {'comercio_maniqui': [3, 25], 'comercio_carro': [5, 30], 'comercio_bebida': [0.3, 12], 'comercio_hogar': [0.2, 12],
              'comercio_expositor': [2, 120], 'comercio_seguridad': [1, 20]}

TOPE = {'farmacia_producto': 1.5, 'alimento': 12, 'comercio_bebida': 12, 'comercio_hogar': 12}   # (the top of each category's mass range)
def clase_masa(m):
    return 'PICKUP' if m < 5 else 'CARRY' if m < 25 else 'PUSH' if m < 80 else 'PUSH_HEAVY' if m < 400 else 'FIXED'
def oscuro(c, f=0.85):
    r, g, b = (int(c[i:i + 2], 16) for i in (1, 3, 5))
    return '#%02x%02x%02x' % (min(255, int(r * f)), min(255, int(g * f)), min(255, int(b * f)))
def mezcla(a, b, t):
    ra, rb = [int(a[i:i + 2], 16) for i in (1, 3, 5)], [int(b[i:i + 2], 16) for i in (1, 3, 5)]
    return '#%02x%02x%02x' % tuple(int(x + (y - x) * t) for x, y in zip(ra, rb))
FIJO = 'anclado en la realidad'

STEEL, DARK, WOOD, WOOD_D, WOOD_L, WHITE, GLASS, CREAM = '#c3c7ca', '#2b2b2e', '#8a5a36', '#5e3b22', '#cfb48a', '#f4f2ec', '#bcd6dc', '#e9e2d2'
SKIN = '#e3d8ca'
MIRROR = '#c3d3da'

def estantes(id, nombre, w, d, ys, alto, c='#e6dfd0', cp='#f6f2ea', masa=55, cat='estanteria', soporte='suelo', nota=None):
    """A shelving unit: two side panels, a back, a plank at each height of ys (their tops are the surfaces), a kick plate."""
    P = [caja(0.02, alto, d, x=-w / 2 + 0.01, z=d / 2, c=c), caja(0.02, alto, d, x=w / 2 - 0.01, z=d / 2, c=c), caja(w - 0.04, alto, 0.012, z=0.006, c=c)]
    P += [caja(w - 0.04, 0.025, d, y=y - 0.0125, z=d / 2, c=cp) for y in ys]
    P.append(caja(w - 0.04, 0.1, d - 0.03, y=0.05, z=d / 2 + 0.0, c=oscuro(c, 0.55)))
    obj(id, nombre, cat, 'FIXED', masa, 'madera', soporte, P, motivo_fijo=FIJO, superficies=[{'y': y, 'fondo': round(d - 0.03, 3)} for y in ys], **({'nota': nota} if nota else {}))

def facing(unit, nx, nz, dx, dz, w, h, fondo, c, hf=0.92):
    """nx x nz units (unit(x, z) -> parts, its foot at y = 0) at the front, a solid block of the stock behind, to `fondo` deep."""
    P = []
    for iz in range(nz):
        for ix in range(nx):
            P += unit((ix - (nx - 1) / 2) * dx, iz * dz)
    zf = (nz - 1) * dz + dz / 2          # the front of the units (their centres run 0 .. (nz-1)*dz)
    zb = -dz / 2                         # their back
    extra = fondo - (nz * dz)
    if extra > 0.02:
        P.append(caja(nx * dx - 0.004, h * hf, extra, x=0, y=h * hf / 2, z=zb - extra / 2, c=oscuro(c, 0.9), m='comida'))
    return P

# ================================================================== LIGHTING (the shops' cool light)
obj('lampara_panel_led', 'Panel LED de techo (60 × 60)', 'lampara', 'FIXED', 3.5, 'metal', 'techo', [
    caja(0.62, 0.05, 0.62, y=-0.025, c='#f2f2ee', m='metal'), caja(0.56, 0.01, 0.56, y=-0.052, c='#fff8ea', m='cristal', luz=True)], motivo_fijo=FIJO)
obj('plafon_pequeno', 'Plafón redondo de techo', 'lampara', 'FIXED', 1.2, 'metal', 'techo', [
    cil(0.17, 0.17, 0.05, y=-0.025, c='#f2f2ee', m='metal', seg=16), cil(0.15, 0.15, 0.01, y=-0.055, c='#fff8ea', m='cristal', luz=True, seg=16)], motivo_fijo=FIJO)
obj('regleta_led', 'Regleta LED de techo (1,2 m)', 'lampara', 'FIXED', 2.2, 'metal', 'techo', [
    caja(1.2, 0.05, 0.12, y=-0.025, c='#eeeeea', m='metal'), caja(1.14, 0.01, 0.09, y=-0.052, c='#fffbee', m='cristal', luz=True)], motivo_fijo=FIJO)
obj('regleta_fluorescente', 'Pantalla fluorescente doble (1,5 m)', 'lampara', 'FIXED', 3.2, 'metal', 'techo', [
    caja(1.5, 0.06, 0.24, y=-0.03, c='#ecece8', m='metal'), caja(1.44, 0.012, 0.05, x=0, y=-0.062, z=-0.06, c='#fffbf0', m='cristal', luz=True), caja(1.44, 0.012, 0.05, y=-0.062, z=0.06, c='#fffbf0', m='cristal', luz=True)], motivo_fijo=FIJO)
obj('carril_focos', 'Carril de focos orientables', 'lampara', 'FIXED', 2.5, 'metal', 'techo', [
    caja(1.5, 0.03, 0.04, y=-0.015, c='#1f1f22', m='metal')] + [p for x in (-0.55, -0.18, 0.18, 0.55) for p in (cil(0.035, 0.045, 0.1, x=x, y=-0.08, z=0.02, c='#e9e9e6', m='metal', r=[20, 0, 0]), caja(0.02, 0.05, 0.02, x=x, y=-0.045, c='#1f1f22', m='metal'))],
    motivo_fijo=FIJO, nota='los focos, apagados: la luz del local la dan los paneles')
obj('aire_acondicionado_pared', 'Aire acondicionado de pared', 'pequeño_electrodomestico', 'FIXED', 12, 'plastico', 'pared', [
    caja(0.85, 0.28, 0.2, y=2.5, z=0.1, c='#f1f1ee', m='plastico'), caja(0.8, 0.03, 0.02, y=2.4, z=0.205, c='#cfd2d4', m='plastico'), caja(0.04, 0.02, 0.005, x=0.3, y=2.55, z=0.2, c='#4a8a5a', m='plastico', luz=True)], motivo_fijo=FIJO)

# ================================================================== THE CLOTHES SHOP (tienda_ropa)
obj('mostrador_tienda', 'Mostrador de tienda (1,1 m)', 'mostrador', 'FIXED', 160, 'madera', 'suelo', [
    caja(1.1, 0.9, 0.52, z=-0.04, c='#e6dfd0'), caja(1.1, 0.05, 0.64, y=0.925, z=0.0, c=WOOD_L), caja(1.0, 0.62, 0.01, y=0.48, z=0.226, c='#d4c8b0'),
    caja(1.1, 0.07, 0.01, y=0.035, z=0.226, c=DARK)], motivo_fijo='estructural', superficies=[{'y': 0.95, 'margen': 0.04}], nota='el mostrador con la caja, junto a la puerta')
obj('armario_trascaja', 'Armario de trastienda', 'mueble', 'FIXED', 70, 'madera', 'pared', [
    caja(0.9, 2.0, 0.45, z=0.225, c='#e4ddd0'), caja(0.01, 1.9, 0.005, y=1.0, z=0.452, c='#b8ad98'), cil(0.008, 0.008, 0.16, x=-0.06, y=1.0, z=0.47, c=STEEL, r=[0, 0, 0]), cil(0.008, 0.008, 0.16, x=0.06, y=1.0, z=0.47, c=STEEL)],
    motivo_fijo=FIJO, superficies=[{'y': 2.0, 'margen': 0.05}])
obj('pila_bolsas_papel', 'Pila de bolsas de papel', 'papel', 'PICKUP', 0.6, 'papel', 'superficie', [caja(0.3, 0.1, 0.1, c='#c9a46e', m='papel'), caja(0.3, 0.012, 0.1, y=0.106, c='#b58f58', m='papel')])
obj('bolsa_papel_grande', 'Bolsa de papel con asas', 'papel', 'PICKUP', 0.2, 'papel', 'superficie', [
    caja(0.26, 0.32, 0.1, c='#efe6d4', m='papel'), cil(0.005, 0.005, 0.1, x=-0.06, y=0.37, c='#8a7a5a', m='tela'), cil(0.005, 0.005, 0.1, x=0.06, y=0.37, c='#8a7a5a', m='tela'), cil(0.005, 0.005, 0.12, y=0.42, c='#8a7a5a', m='tela', r=[0, 0, 90])])
obj('cesta_calcetines', 'Cesta de calcetines', 'recipiente', 'PICKUP', 1.4, 'tela', 'superficie', [
    caja(0.34, 0.12, 0.24, c='#c8a878', m='madera')] + [caja(0.07, 0.03, 0.2, x=-0.12 + i * 0.08, y=0.135, c=c, m='tela') for i, c in enumerate(['#b3342a', '#243a63', '#3b6b4b', '#d1a038'])])
obj('expositor_joyas', 'Vitrina pequeña de bisutería', 'vitrina', 'CARRY', 8, 'cristal', 'superficie', [
    caja(0.42, 0.05, 0.3, c='#3a2e26'), caja(0.42, 0.14, 0.3, y=0.12, c=GLASS, m='cristal'), caja(0.36, 0.02, 0.24, y=0.06, c='#7a3a4a', m='tela'),
    esf(0.012, -0.1, 0.085, 0, c='#d8b040'), esf(0.012, 0.0, 0.085, 0.04, c='#c8c8d0'), esf(0.012, 0.1, 0.085, -0.03, c='#d8b040')])
obj('tarjetero', 'Tarjetero de mostrador', 'papel', 'PICKUP', 0.15, 'papel', 'superficie', [caja(0.1, 0.012, 0.07, c=STEEL, m='metal'), caja(0.09, 0.07, 0.04, y=0.045, c='#f0eee6', m='papel')])
obj('rollo_papel_regalo', 'Rollo de papel de regalo', 'papel', 'PICKUP', 0.6, 'papel', 'superficie', [
    cil(0.05, 0.05, 0.4, y=0.22, c='#b3342a', m='papel', r=[0, 0, 90]), caja(0.04, 0.06, 0.1, x=-0.22, y=0.03, c=DARK, m='metal'), caja(0.04, 0.06, 0.1, x=0.22, y=0.03, c=DARK, m='metal')])
obj('cartel_rebajas', 'Cartel de rebajas', 'cuadro', 'PICKUP', 0.6, 'papel', 'pared', [
    caja(0.5, 0.7, 0.012, y=1.6, z=0.006, c='#c0302a'), plano(0.46, 0.66, y=1.6, z=0.015, tex={'tipo': 'cartel_rebajas'})])
for k, (nom, sub, fondo, col) in {'a': ('Moda Dehesa', 'Señora · Caballero · Niños', '#2d3f35', '#f2e8c8'), 'b': ('Boutique Alba', 'Moda y complementos', '#4a2a3a', '#f4e4d8'),
                                  'c': ('Modas Candelaria', 'Confección desde 1978', '#23324a', '#f0e6c8')}.items():
    obj('rotulo_tienda_' + k, 'Rótulo interior «%s»' % nom, 'decoracion', 'PICKUP', 3, 'madera', 'pared', [
        caja(1.3, 0.34, 0.03, y=2.45, z=0.015, c='#2a2a2e'), plano(1.24, 0.28, y=2.45, z=0.033, tex={'tipo': 'rotulo', 'texto': nom, 'sub': sub, 'fondo': fondo, 'color': col, 'rotulo_local': True})])
for k in (1, 2):
    obj('cuadro_moda_' + 'ab'[k - 1], 'Lámina de moda enmarcada', 'cuadro', 'PICKUP', 1.5, 'madera', 'pared', [
        caja(0.5, 0.7, 0.03, y=1.75, z=0.015, c='#2a2420'), plano(0.44, 0.64, y=1.75, z=0.033, tex={'tipo': 'cartel_moda', 'estilo': k})])

# ---- shelving and what is folded on it
estantes('estanteria_ropa_pared', 'Estantería de pared para ropa doblada', 1.0, 0.4, [0.2, 0.56, 0.92, 1.28, 1.64, 2.0], 2.36, masa=55, nota='baldas de 36 cm: jerseys, vaqueros y camisetas doblados')
estantes('estanteria_ropa_baja', 'Estantería baja de ropa', 1.0, 0.4, [0.2, 0.55, 0.9], 1.0, masa=30)
estantes('expositor_zapatos', 'Expositor de zapatos', 1.0, 0.34, [0.3, 0.65, 1.0, 1.35, 1.7], 1.9, c='#d8d0c0', masa=40)
estantes('expositor_bolsos', 'Expositor de bolsos', 0.9, 0.32, [0.4, 0.85, 1.3], 1.6, c='#d8d0c0', cat='comercio_expositor', masa=30)

def pila(id, nombre, a, b, n, w, d, h1, mu):
    P = [caja(w - 0.006 * (i % 2), h1, d - 0.004 * (i % 2), y=h1 * (i + 0.5), c=(a if i % 3 else b), m='tela') for i in range(n)]
    obj(id, nombre, 'textil', 'PICKUP', round(n * mu, 2), 'tela', 'superficie', P)
for k, (n_, c1, c2) in {'rojo': ('rojo', '#b3342a', '#cc5a48'), 'azul_marino': ('azul marino', '#243a63', '#3d5a8a'), 'verde': ('verde', '#3b6b4b', '#5a8a68'),
                        'mostaza': ('mostaza', '#d1a038', '#e2bd62'), 'gris': ('gris', '#8a8f96', '#a8adb4'), 'crudo': ('crudo', '#e6dccb', '#f0e8da')}.items():
    pila('pila_jerseys_' + k, 'Pila de jerseys %s' % n_, c1, c2, 5, 0.32, 0.26, 0.055, 0.4)
for k, (n_, c1, c2) in {'claro': ('lavado claro', '#6b86a8', '#8aa2c0'), 'medio': ('lavado medio', '#3d5a80', '#4f6e96'), 'oscuro': ('azul oscuro', '#2b3f5c', '#3a506e')}.items():
    pila('pila_vaqueros_' + k, 'Pila de vaqueros %s' % n_, c1, c2, 5, 0.32, 0.26, 0.05, 0.55)
for k, (n_, c1, c2) in {'blanca': ('blancas', '#f2f0ea', '#e4e0d6'), 'negra': ('negras', '#34343a', '#4a4a50'), 'rosa': ('rosas', '#e0a4b0', '#eab8c2'), 'turquesa': ('turquesa', '#3a8f9a', '#5aa6b0')}.items():
    pila('pila_camisetas_' + k, 'Pila de camisetas %s' % n_, c1, c2, 7, 0.3, 0.24, 0.035, 0.22)
for k, (n_, c1, c2) in {'azul': ('azules', '#2c5aa0', '#4a74b4'), 'granate': ('granates', '#7a2a3a', '#98404f')}.items():
    pila('pila_polos_' + k, 'Pila de polos %s' % n_, c1, c2, 6, 0.3, 0.24, 0.04, 0.3)
for k, (n_, c1, c2) in {'beige': ('chinos beige', '#c8b48a', '#d6c6a0'), 'gris': ('pantalones de vestir grises', '#6b6f76', '#80848a')}.items():
    pila('pila_pantalones_' + k, 'Pila de %s' % n_, c1, c2, 4, 0.32, 0.26, 0.06, 0.5)
for k, (n_, c1, c2) in {'negra': ('negras', '#3c3c42', '#54545a'), 'burdeos': ('burdeos', '#6a2a3a', '#843c4c')}.items():
    pila('pila_sudaderas_' + k, 'Pila de sudaderas %s' % n_, c1, c2, 4, 0.32, 0.27, 0.07, 0.6)
obj('bufandas_dobladas', 'Bufandas dobladas', 'textil', 'PICKUP', 1.2, 'tela', 'superficie', [
    caja(0.3, 0.05, 0.22, c='#8a3a3a', m='tela'), caja(0.3, 0.05, 0.22, y=0.075, c='#3a5a7a', m='tela'), caja(0.3, 0.05, 0.22, y=0.125, c='#c8a048', m='tela')])
obj('gorros_lana', 'Gorros de lana', 'textil', 'PICKUP', 0.5, 'tela', 'superficie', [
    esf(0.09, -0.1, 0.08, 0, c='#6a2a3a', m='tela', s=[1, 0.85, 1]), esf(0.09, 0.1, 0.08, 0, c='#2a3a5a', m='tela', s=[1, 0.85, 1]), cil(0.02, 0.02, 0.03, x=-0.1, y=0.16, c='#e6dccb', m='tela', seg=8), cil(0.02, 0.02, 0.03, x=0.1, y=0.16, c='#e6dccb', m='tela', seg=8)])


# ---- tables for the middle of the shop
obj('mesa_exposicion', 'Mesa de exposición con balda', 'mesa', 'PUSH', 30, 'madera', 'suelo', [
    caja(1.2, 0.04, 0.8, y=0.83, c='#d8c4a0')] + [caja(0.05, 0.81, 0.05, x=sx * 0.55, y=0.405, z=sz * 0.35, c=WOOD_D) for sx in (-1, 1) for sz in (-1, 1)]
    + [caja(1.1, 0.03, 0.7, y=0.28, c='#cdb88e')], superficies=[{'y': 0.85, 'margen': 0.06}, {'y': 0.295, 'margen': 0.05}], nota='la mesa de los jerseys')
obj('mesa_escalonada', 'Expositor escalonado de tres alturas', 'mesa', 'PUSH', 40, 'madera', 'suelo', [
    caja(1.2, 0.3, 0.34, y=0.15, z=0.34, c='#d8c4a0'), caja(1.2, 0.55, 0.34, y=0.275, z=0.0, c='#cdb88e'), caja(1.2, 0.8, 0.34, y=0.4, z=-0.34, c='#d8c4a0')],
    superficies=[{'y': 0.3, 'margen': 0.02}, {'y': 0.55, 'margen': 0.02}, {'y': 0.8, 'margen': 0.02}], nota='tres escalones para jerseys y vaqueros')

# ---- hanging garments: slabs on a rail (sideways to it, as they hang in a shop)
def prendas(x0, x1, ybar, largo, cols, prof=0.4, paso=0.085, z=0.0):
    P, n = [], int((x1 - x0) / paso)
    for i in range(n):
        x, c = x0 + paso * (i + 0.5), cols[i % len(cols)]
        P.append(caja(0.045, largo, prof, x=x, y=ybar - 0.03 - largo / 2, z=z, c=c, m='tela'))
        P.append(caja(0.05, 0.05, prof * 0.6, x=x, y=ybar - 0.06, z=z, c=oscuro(c, 0.8), m='tela'))
    return P
ABRIGOS = ['#2a2a2e', '#6b5a48', '#8a8f96', '#243a63', '#7a2a3a', '#3b4a3a']
VESTIDOS = ['#b3342a', '#d1a038', '#3a8f9a', '#e0a4b0', '#5a4a8a', '#e6dccb', '#3b6b4b']
CAMISAS = ['#f2f0ea', '#6b86a8', '#e6dccb', '#2c5aa0', '#d8c8e0', '#aac4b8']
RAILES = {'abrigos': ('de abrigos', 0.95, ABRIGOS), 'camisas': ('de camisas', 0.7, CAMISAS), 'vestidos': ('de vestidos', 1.0, VESTIDOS)}
for k, (n_, largo, cols) in RAILES.items():
    P = [cil(0.012, 0.012, 1.2, y=1.5, c=STEEL, r=[0, 0, 90])]
    for sx in (-1, 1):
        P += [cil(0.012, 0.012, 1.55, x=sx * 0.57, y=0.775, c=STEEL), caja(0.04, 0.03, 0.5, x=sx * 0.57, y=0.015, c=STEEL, m='metal')]
    P += prendas(-0.52, 0.52, 1.5, largo, cols)
    obj('burra_suelo_' + k, 'Burra %s' % n_, 'mueble', 'CARRY', 16, 'metal', 'suelo', P, nota='perchero de tienda, con las prendas colgadas de lado')
    P = [cil(0.012, 0.012, 1.2, y=1.7, z=0.3, c=STEEL, r=[0, 0, 90]), caja(1.2, 0.03, 0.3, y=2.0, z=0.15, c=WOOD_L)]
    for sx in (-1, 1): P.append(caja(0.03, 0.03, 0.3, x=sx * 0.55, y=1.7, z=0.15, c=STEEL, m='metal'))
    P += prendas(-0.52, 0.52, 1.7, largo, cols, z=0.3)
    obj('burra_pared_' + k, 'Barra de pared %s' % n_, 'mueble', 'FIXED', 14, 'metal', 'pared', P, motivo_fijo=FIJO)

# ---- mannequins
def maniqui(id, nombre, tipo, c1, c2=None):
    c2 = c2 or c1
    P = [cil(0.17, 0.17, 0.014, c='#232326', seg=16), cil(0.012, 0.012, 0.62, y=0.324, c=STEEL, seg=8)]
    if tipo == 'vestido':
        P += [cil(0.1, 0.21, 0.6, y=0.85, c=c1, m='tela', seg=14), cil(0.035, 0.028, 0.5, x=-0.07, y=0.3, c=SKIN, m='plastico', seg=8), cil(0.035, 0.028, 0.5, x=0.07, y=0.3, c=SKIN, m='plastico', seg=8)]
        P += [cil(0.15, 0.12, 0.38, y=1.34, c=c1, m='tela', seg=14)]
        arm = SKIN
    else:
        P += [cil(0.075, 0.055, 0.86, x=-0.08, y=0.44, c=c2, m='tela', seg=8), cil(0.075, 0.055, 0.86, x=0.08, y=0.44, c=c2, m='tela', seg=8)]
        P += [cil(0.16, 0.13, 0.42, y=1.3, c=c1, m='tela', seg=14)]
        arm = c1
    P += [caja(0.4, 0.05, 0.17, y=1.5, c=c1 if tipo != 'vestido' else c1, m='tela'), cil(0.04, 0.045, 0.1, y=1.6, c=SKIN, m='plastico', seg=8), esf(0.095, 0, 1.72, 0, c=SKIN, m='plastico', s=[0.85, 1.15, 1.0]),
          cil(0.03, 0.026, 0.58, x=-0.225, y=1.2, c=arm, m='tela', r=[0, 0, 5], seg=8), cil(0.03, 0.026, 0.58, x=0.225, y=1.2, c=arm, m='tela', r=[0, 0, -5], seg=8)]
    obj(id, nombre, 'comercio_maniqui', 'CARRY', 9, 'plastico', 'suelo', P, nota='maniquí de escaparate')
maniqui('maniqui_vestido_rojo', 'Maniquí con vestido rojo', 'vestido', '#b3342a')
maniqui('maniqui_vestido_azul', 'Maniquí con vestido azul', 'vestido', '#2c5aa0')
maniqui('maniqui_vestido_mostaza', 'Maniquí con vestido mostaza', 'vestido', '#d1a038')
maniqui('maniqui_vaqueros', 'Maniquí con vaqueros y camiseta', 'pantalon', '#f2f0ea', '#3d5a80')
maniqui('maniqui_traje', 'Maniquí con traje gris', 'pantalon', '#6b6f76', '#6b6f76')
maniqui('maniqui_abrigo', 'Maniquí con abrigo', 'pantalon', '#6b5a48', '#2a2a2e')
obj('maniqui_almacen', 'Maniquí desnudo de almacén', 'comercio_maniqui', 'CARRY', 7, 'plastico', 'suelo', [
    cil(0.17, 0.17, 0.014, c='#232326', seg=16), cil(0.012, 0.012, 1.1, y=0.564, c=STEEL, seg=8), cil(0.14, 0.11, 0.5, y=1.19, c='#d8d2c6', m='plastico', seg=12), esf(0.09, 0, 1.6, 0, c='#d8d2c6', m='plastico', s=[0.85, 1.15, 1.0])])

# ---- mirrors, fitting rooms
obj('espejo_pie', 'Espejo de pie', 'espejo', 'CARRY', 12, 'cristal', 'suelo', [
    caja(0.55, 1.7, 0.03, y=0.87, c='#5a4630'), caja(0.49, 1.64, 0.006, y=0.87, z=0.018, c=MIRROR, m='metal'), caja(0.05, 0.03, 0.3, x=-0.2, y=0.015, c='#5a4630'), caja(0.05, 0.03, 0.3, x=0.2, y=0.015, c='#5a4630')])
obj('espejo_pared_grande', 'Espejo grande de pared', 'espejo', 'FIXED', 14, 'cristal', 'pared', [
    caja(0.9, 1.6, 0.03, y=1.1, z=0.015, c='#c8b48a'), caja(0.84, 1.54, 0.006, y=1.1, z=0.033, c=MIRROR, m='metal')], motivo_fijo=FIJO)
obj('espejo_probador', 'Espejo de probador', 'espejo', 'FIXED', 6, 'cristal', 'pared', [
    caja(0.5, 1.5, 0.03, y=1.1, z=0.015, c='#6a5a48'), caja(0.44, 1.44, 0.006, y=1.1, z=0.033, c=MIRROR, m='metal')], motivo_fijo=FIJO)
obj('gancho_probador', 'Tabla de ganchos', 'decoracion', 'PICKUP', 0.4, 'madera', 'pared', [
    caja(0.5, 0.06, 0.02, y=1.65, z=0.01, c=WOOD_D)] + [cil(0.008, 0.008, 0.05, x=x, y=1.66, z=0.04, c=STEEL, r=[90, 0, 0], seg=8) for x in (-0.15, 0, 0.15)])
obj('taburete_probador', 'Taburete tapizado', 'taburete', 'PICKUP', 3.5, 'madera', 'suelo', [
    cil(0.2, 0.2, 0.08, y=0.41, c='#7a4a5a', m='tela', seg=12)] + [caja(0.03, 0.37, 0.03, x=sx * 0.13, y=0.185, z=sz * 0.13, c=WOOD_D) for sx in (-1, 1) for sz in (-1, 1)],
    modificadores=['SEAT'], asientos=[{'p': [0, 0.45, 0], 'h': 0.45, 'anim': 'silla'}])
obj('banqueta_probador', 'Banqueta de probador', 'mueble', 'CARRY', 8, 'madera', 'suelo', [
    caja(0.9, 0.08, 0.34, y=0.41, c='#6a4a5a', m='tela')] + [caja(0.04, 0.37, 0.04, x=sx * 0.4, y=0.185, z=sz * 0.13, c=WOOD_D) for sx in (-1, 1) for sz in (-1, 1)],
    modificadores=['SEAT'], asientos=[{'p': [0, 0.45, 0], 'h': 0.45, 'anim': 'banco'}])
for lado, s in (('izq', -1), ('der', 1)):
    obj('cortina_probador_' + lado, 'Cortina de probador (recogida a la %s)' % ('izquierda' if s < 0 else 'derecha'), 'textil', 'FIXED', 3, 'tela', 'suelo', [
        cil(0.012, 0.012, 1.2, y=2.1, c=STEEL, r=[0, 0, 90], seg=8), cil(0.06, 0.07, 2.0, x=s * 0.53, y=1.0, c='#8a3a4a', m='tela', seg=8), cil(0.05, 0.06, 1.98, x=s * 0.46, y=0.99, z=0.03, c='#9a4a5a', m='tela', seg=8)],
        motivo_fijo=FIJO, nota='la cortina del probador, recogida a un lado: queda el paso de un cuerpo')

# ---- shoes and bags
def zapato(x, tipo, c):
    s, u = ('#2b2b2e', c)
    if tipo == 'formal':
        return [caja(0.085, 0.02, 0.29, x=x, y=0.01, c=s, m='goma'), caja(0.08, 0.06, 0.15, x=x, y=0.05, z=-0.06, c=u, m='goma'), caja(0.075, 0.04, 0.12, x=x, y=0.04, z=0.07, c=u, m='goma')]
    if tipo == 'bota':
        return [caja(0.09, 0.025, 0.29, x=x, y=0.0125, c=s, m='goma'), caja(0.085, 0.2, 0.15, x=x, y=0.125, z=-0.06, c=u, m='goma'), caja(0.08, 0.06, 0.13, x=x, y=0.055, z=0.07, c=u, m='goma')]
    if tipo == 'tacon':
        return [caja(0.07, 0.012, 0.25, x=x, y=0.07, z=0.0, c=s, m='goma'), caja(0.065, 0.05, 0.2, x=x, y=0.1, z=0.0, c=u, m='goma'), cil(0.012, 0.01, 0.07, x=x, y=0.035, z=-0.1, c=s, m='goma', seg=6)]
    return [caja(0.09, 0.03, 0.29, x=x, y=0.015, c='#f2f0ea', m='goma'), caja(0.085, 0.06, 0.2, x=x, y=0.06, z=-0.03, c=u, m='tela'), caja(0.08, 0.035, 0.1, x=x, y=0.048, z=0.09, c=u, m='tela')]
for k, (n_, tipo, c) in {'zapatos_hombre_negro': ('zapatos de hombre negros', 'formal', '#1f1f22'), 'zapatos_hombre_marron': ('zapatos de hombre marrones', 'formal', '#6b4426'), 'zapatos_mujer_rojo': ('zapatos de tacón rojos', 'tacon', '#b3342a'),
                         'zapatillas_blancas': ('zapatillas blancas', 'zapatilla', '#e8e6de'), 'zapatillas_azules': ('zapatillas azules', 'zapatilla', '#2c5aa0'),
                         'botas_marron': ('botas marrones', 'bota', '#6b4a30'), 'botas_negras': ('botas negras', 'bota', '#26262a')}.items():
    obj('par_' + k, 'Par de %s' % n_, 'ropa', 'PICKUP', 0.9, 'goma', 'superficie', zapato(-0.065, tipo, c) + zapato(0.065, tipo, c))
obj('pila_cajas_zapatos', 'Cajas de zapatos', 'caja', 'PICKUP', 1.6, 'papel', 'superficie', [caja(0.33, 0.12, 0.2, c='#d8c8a8', m='papel'), caja(0.33, 0.12, 0.2, y=0.18, c='#c9b48a', m='papel'), caja(0.31, 0.012, 0.18, y=0.126, c='#b3342a', m='papel')])
def bolso(x, c, asa):
    return [caja(0.32, 0.22, 0.1, c=c, m='tela'), caja(0.322, 0.07, 0.102, y=0.185, c=oscuro(c, 0.85), m='tela'), cil(0.006, 0.006, 0.12, x=-0.07, y=0.28, c=asa, m='tela', seg=6),
            cil(0.006, 0.006, 0.12, x=0.07, y=0.28, c=asa, m='tela', seg=6), cil(0.006, 0.006, 0.14, y=0.34, c=asa, m='tela', r=[0, 0, 90], seg=6)]
for k, (n_, c, a) in {'negro': ('negro', '#232326', '#c8a040'), 'marron': ('marrón', '#8a5a36', '#4a3020'), 'rojo': ('rojo', '#a8302a', '#e6dccb'), 'azul': ('azul', '#2c4a7a', '#c8c8c0')}.items():
    obj('bolso_' + k, 'Bolso %s' % n_, 'ropa', 'PICKUP', 0.8, 'tela', 'superficie', bolso(0, c, a))

# ---- stands on the floor
def espiral(R, ys, cols, alto_pack=0.16, ancho=0.1, n=8):
    import math
    P = []
    for j, y in enumerate(ys):
        for i in range(n):
            a = 2 * math.pi * i / n
            P.append(caja(ancho, alto_pack, 0.02, x=R * math.sin(a), y=y + alto_pack / 2, z=R * math.cos(a), c=cols[(i + j) % len(cols)], m='tela', r=[0, round(math.degrees(a), 1), 0]))
    return P
obj('expositor_calcetines', 'Expositor giratorio de calcetines', 'comercio_expositor', 'CARRY', 6, 'metal', 'suelo', [
    cil(0.22, 0.24, 0.03, y=0.015, c='#2b2b2e', seg=16), cil(0.02, 0.02, 1.5, y=0.78, c=STEEL, seg=8), cil(0.2, 0.2, 0.02, y=0.5, c=STEEL, seg=16), cil(0.2, 0.2, 0.02, y=0.95, c=STEEL, seg=16), cil(0.2, 0.2, 0.02, y=1.4, c=STEEL, seg=16)]
    + espiral(0.17, [0.51, 0.96, 1.41], ['#b3342a', '#243a63', '#3b6b4b', '#d1a038', '#f2f0ea', '#2a2a2e']))
obj('expositor_bufandas', 'Expositor de bufandas', 'comercio_expositor', 'CARRY', 5.5, 'metal', 'suelo', [
    cil(0.2, 0.22, 0.03, y=0.015, c='#2b2b2e', seg=16), cil(0.015, 0.015, 1.5, y=0.78, c=STEEL, seg=8), cil(0.008, 0.008, 0.6, y=1.45, c=STEEL, r=[0, 0, 90], seg=6),
    caja(0.06, 0.55, 0.03, x=-0.25, y=1.17, c='#8a3a3a', m='tela'), caja(0.06, 0.5, 0.03, x=-0.12, y=1.2, c='#3a5a7a', m='tela'), caja(0.06, 0.55, 0.03, x=0.12, y=1.17, c='#c8a048', m='tela'), caja(0.06, 0.5, 0.03, x=0.25, y=1.2, c='#3b6b4b', m='tela')])
obj('cesta_ofertas', 'Cesta de prendas en oferta', 'comercio_expositor', 'CARRY', 9, 'metal', 'suelo', [
    caja(0.7, 0.03, 0.45, y=0.465, c='#d6d9db', m='metal')] + [caja(0.04, 0.45, 0.04, x=sx * 0.32, y=0.225, z=sz * 0.19, c='#9aa0a4', m='metal') for sx in (-1, 1) for sz in (-1, 1)]
    + [caja(0.7, 0.2, 0.012, y=0.58, z=0.22, c='#d6d9db', m='cristal'), caja(0.7, 0.2, 0.012, y=0.58, z=-0.22, c='#d6d9db', m='cristal'), caja(0.012, 0.2, 0.45, x=-0.35, y=0.58, c='#d6d9db', m='cristal'), caja(0.012, 0.2, 0.45, x=0.35, y=0.58, c='#d6d9db', m='cristal'),
       caja(0.3, 0.12, 0.3, x=-0.17, y=0.54, c='#b3342a', m='tela'), caja(0.3, 0.14, 0.3, x=0.17, y=0.55, c='#3d5a80', m='tela'), caja(0.2, 0.1, 0.2, x=0.0, y=0.63, z=0.05, c='#d1a038', m='tela')])
obj('perchero_chaquetas', 'Perchero con chaquetas', 'perchero', 'CARRY', 7, 'madera', 'suelo', [
    cil(0.02, 0.02, 1.75, y=0.875, c=WOOD_D, m='madera', seg=8), cil(0.2, 0.22, 0.03, y=0.015, c=WOOD_D, m='madera', seg=14), cil(0.01, 0.01, 0.3, y=1.7, c=WOOD_D, m='madera', r=[0, 0, 70], seg=6), cil(0.01, 0.01, 0.3, y=1.7, c=WOOD_D, m='madera', r=[70, 0, 0], seg=6),
    caja(0.06, 0.6, 0.38, x=0.2, y=1.35, c='#243a63', m='tela'), caja(0.06, 0.6, 0.38, x=-0.2, y=1.35, c='#7a2a3a', m='tela'), caja(0.38, 0.6, 0.06, z=0.2, y=1.35, c='#6b5a48', m='tela')])
obj('antena_antihurto', 'Antena antihurto', 'mueble', 'CARRY', 7, 'plastico', 'suelo', [
    caja(0.45, 0.03, 0.2, y=0.015, c='#d9d9d6', m='plastico'), caja(0.4, 1.35, 0.04, y=0.705, c='#ecebe6', m='plastico'), caja(0.3, 0.03, 0.045, y=1.25, c='#8aa0a8', m='plastico')])

# ---- the stockroom
obj('caja_ropa_almacen', 'Caja de ropa de almacén', 'caja', 'PICKUP', 3, 'papel', 'superficie', [caja(0.5, 0.3, 0.35, c='#b88a58', m='papel'), caja(0.5, 0.01, 0.05, y=0.305, c='#d8c8a8', m='papel')])
obj('burra_almacen_fundas', 'Burra de almacén con fundas', 'mueble', 'CARRY', 15, 'metal', 'suelo', [
    cil(0.012, 0.012, 1.2, y=1.6, c=STEEL, r=[0, 0, 90])] + [p for sx in (-1, 1) for p in (cil(0.012, 0.012, 1.65, x=sx * 0.57, y=0.825, c=STEEL), caja(0.04, 0.03, 0.5, x=sx * 0.57, y=0.015, c=STEEL, m='metal'))]
    + [caja(0.05, 1.0, 0.4, x=-0.5 + i * 0.1, y=1.08, c='#e9eceb', m='cristal') for i in range(11)])
obj('vaporizador_ropa', 'Vaporizador de ropa', 'pequeño_electrodomestico', 'CARRY', 6, 'plastico', 'suelo', [
    cil(0.22, 0.24, 0.03, y=0.015, c='#2b2b2e', seg=12), cil(0.015, 0.015, 1.4, y=0.73, c=STEEL, seg=8), cil(0.09, 0.09, 0.28, y=0.3, c='#e9e9e6', m='plastico', seg=10), caja(0.14, 0.1, 0.1, y=1.38, c='#e9e9e6', m='plastico')])
obj('tabla_planchar', 'Tabla de planchar', 'mueble', 'CARRY', 5.5, 'metal', 'suelo', [
    caja(1.1, 0.03, 0.34, y=0.85, c='#6a86a8', m='tela'), caja(0.02, 0.84, 0.02, x=-0.3, y=0.42, z=0.0, c=STEEL, m='metal', r=[0, 0, 0]), caja(0.02, 0.84, 0.02, x=0.3, y=0.42, z=0.0, c=STEEL, m='metal'), caja(0.6, 0.02, 0.3, y=0.01, c=STEEL, m='metal')],
    superficies=[{'y': 0.865, 'margen': 0.03}])

# ---- the accessories the shop sells where they stand (the kit's `vende`: sunglasses, umbrellas, cologne)
obj('expositor_gafas', 'Expositor giratorio de gafas de sol', 'comercio_expositor', 'PICKUP', 4.5, 'metal', 'suelo', [
    cil(0.2, 0.22, 0.03, y=0.015, c='#2b2b2e', seg=14), cil(0.018, 0.018, 1.25, y=0.64, c=STEEL, seg=8), caja(0.36, 0.55, 0.36, y=1.4, c='#2b2b2e', m='plastico')]
    + [caja(0.11, 0.035, 0.012, x=x, y=y, z=0.186, c=c, m='plastico') for y, c in ((1.24, '#262626'), (1.4, '#6b4426'), (1.56, '#2c5aa0')) for x in (-0.08, 0.08)]
    + [caja(0.012, 0.035, 0.11, x=0.186, y=y, z=0.0, c='#262626', m='plastico') for y in (1.3, 1.5)], nota='gafas de sol, 22 €')
obj('paraguas_cubo', 'Cubo de paraguas', 'comercio_expositor', 'PICKUP', 4, 'metal', 'suelo', [
    cil(0.14, 0.12, 0.45, c='#3a3d42', m='metal', seg=14)] + [p for x, z, c in ((-0.05, 0.02, '#243a63'), (0.04, -0.04, '#7a2a3a'), (0.06, 0.05, '#2a2a2e'), (-0.06, -0.05, '#3b6b4b'))
                                                            for p in (cil(0.012, 0.012, 0.95, x=x, y=0.5, z=z, c=c, m='tela', seg=6), cil(0.012, 0.012, 0.08, x=x + 0.025, y=0.99, z=z, c='#5a3a20', m='madera', r=[0, 0, 90], seg=6))], nota='paraguas, 9 €')
estantes('perfumes_expositor', 'Expositor de colonias', 0.5, 0.25, [0.5, 0.85, 1.2], 1.4, c='#d8d0c0', cat='comercio_expositor', masa=7)
OUT[-1]['partes'] += [p for y in (0.5, 0.85, 1.2) for x, c in ((-0.12, '#c8a040'), (0.0, '#6a8aa8'), (0.12, '#b3547a')) for p in (caja(0.06, 0.1, 0.05, x=x, y=y + 0.05, z=0.12, c=c, m='cristal'), caja(0.03, 0.025, 0.03, x=x, y=y + 0.1125, z=0.12, c='#2b2b2e', m='plastico'))]
OUT[-1].pop('superficies'); OUT[-1]['nota'] = 'colonia, 20 €'

# ==== FARMACIA ====

# ---- product templates: a unit (x, z) -> parts, its foot at y = 0; and a FACING (a row of units, the stock as a block behind)
def regis(id, nombre, cat, unit, nx, nz, dx, dz, h, fondo, c, mu, mat='comida', hf=0.9, clase=None, nota=None):
    """A facing as an object: nx x nz units at the front, a block of stock behind to `fondo` deep; its mass counts the stock."""
    P = facing(unit, nx, nz, dx, dz, nx * dx, h, fondo, c, hf)
    masa = round(min(nx * (fondo / dz) * mu, 0.9 * TOPE.get(cat, 1e9)), 2)
    obj(id, nombre, cat, clase or clase_masa(masa), masa, mat, 'superficie', P, **({'nota': nota} if nota else {}))
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
def u_tubo(w, h, c, c2):
    def f(x, z):
        return [caja(w, h, w * 0.5, x=x, y=h / 2, z=z, c=c, m='plastico'), caja(w * 0.7, h * 0.12, w * 0.3, x=x, y=h * 0.94, z=z, c=c2, m='plastico')]
    return f

# ================================================================== THE PHARMACY (farmacia)
obj('mostrador_farmacia', 'Mostrador de farmacia (1,2 m)', 'mostrador', 'FIXED', 180, 'madera', 'suelo', [
    caja(1.2, 1.0, 0.56, z=-0.06, c='#e9eeee'), caja(1.2, 0.05, 0.7, y=1.025, z=0.0, c='#f4f6f6', m='piedra'), caja(1.18, 0.1, 0.01, y=0.62, z=0.226, c='#25b34a', m='plastico'),
    caja(1.2, 0.08, 0.012, y=0.04, z=0.226, c='#9aa0a4', m='metal')], motivo_fijo='estructural', superficies=[{'y': 1.05, 'margen': 0.04}], nota='el mostrador de atención, a lo ancho del local')
def cajones(id, nombre):
    P = [caja(0.02, 1.0, 0.5, x=-0.49, y=0.5, z=0.25, c='#e6ebec'), caja(0.02, 1.0, 0.5, x=0.49, y=0.5, z=0.25, c='#e6ebec'), caja(0.02, 1.4, 0.3, x=-0.49, y=1.7, z=0.15, c='#e6ebec'), caja(0.02, 1.4, 0.3, x=0.49, y=1.7, z=0.15, c='#e6ebec'),
         caja(0.98, 2.4, 0.012, y=1.2, z=0.006, c='#d8dfe0'), caja(0.96, 0.95, 0.48, y=0.475, z=0.26, c='#e6ebec'), caja(1.0, 0.04, 0.55, y=0.98, z=0.275, c='#f4f6f6', m='piedra')]
    for y in (0.17, 0.39, 0.61, 0.83):
        for sx in (-1, 1):
            P += [caja(0.46, 0.2, 0.012, x=sx * 0.235, y=y, z=0.506, c='#eef1f1'), caja(0.12, 0.015, 0.02, x=sx * 0.235, y=y + 0.05, z=0.52, c=STEEL, m='metal'), caja(0.1, 0.035, 0.004, x=sx * 0.235, y=y - 0.02, z=0.514, c='#25b34a', m='papel')]
    ys = [1.15, 1.45, 1.75, 2.05]
    P += [caja(0.96, 0.025, 0.3, y=y - 0.0125, z=0.15, c='#f4f6f6') for y in ys]
    obj(id, nombre, 'estanteria', 'FIXED', 90, 'madera', 'pared', P, motivo_fijo=FIJO, superficies=[{'y': y, 'fondo': 0.27} for y in ys], nota='cajones abajo y baldas con las cajas de medicamentos arriba')
cajones('estanteria_medicamentos', 'Módulo de cajones y baldas de medicamentos')
estantes('estanteria_parafarmacia_pared', 'Estantería de parafarmacia de pared', 1.0, 0.36, [0.25, 0.6, 0.95, 1.3, 1.65], 2.0, c='#eef2f0', masa=50)
estantes('gondola_parafarmacia', 'Góndola de parafarmacia', 1.0, 0.4, [0.2, 0.55, 0.9, 1.25], 1.5, c='#e6edea', masa=45, nota='por una cara: se pone de dos en dos, espalda con espalda')
obj('cruz_farmacia_pared', 'Cruz verde luminosa', 'decoracion', 'FIXED', 6, 'plastico', 'pared', [
    caja(0.46, 0.46, 0.06, y=2.7, z=0.03, c='#1a2a20', m='plastico'), plano(0.42, 0.42, y=2.7, z=0.063, tex={'tipo': 'cruz_farmacia'}, luz=True)], motivo_fijo=FIJO, nota='la cruz verde, también por dentro')
obj('pantalla_turno', 'Pantalla del turno (colgada)', 'pantalla', 'FIXED', 4, 'plastico', 'techo', [
    cil(0.004, 0.004, 0.5, x=-0.18, y=-0.25, c=STEEL, seg=6), cil(0.004, 0.004, 0.5, x=0.18, y=-0.25, c=STEEL, seg=6), caja(0.5, 0.2, 0.05, y=-0.6, c='#27272a', m='plastico'),
    plano(0.46, 0.17, y=-0.6, z=-0.0285, tex={'tipo': 'turno'}, r=[0, 180, 0])], motivo_fijo=FIJO, nota='el turno, de cara a quien espera')
obj('expendedor_turno', 'Expendedor de turno', 'comercio_expositor', 'CARRY', 6, 'plastico', 'suelo', [
    cil(0.2, 0.22, 0.03, y=0.015, c='#2b2b2e', seg=12), cil(0.025, 0.025, 1.0, y=0.53, c=STEEL, seg=8), caja(0.18, 0.28, 0.14, y=1.14, c='#25b34a', m='plastico'), caja(0.12, 0.05, 0.02, y=1.0, z=0.07, c='#f4f6f6', m='papel')], nota='para coger número')
obj('pantalla_promo', 'Pantalla de promociones de pared', 'pantalla', 'FIXED', 8, 'plastico', 'pared', [
    caja(0.86, 0.5, 0.05, y=2.0, z=0.025, c='#27272a', m='plastico'), plano(0.8, 0.45, y=2.0, z=0.054, tex={'tipo': 'pantalla_promo'}, luz=True)], motivo_fijo=FIJO)
obj('cartel_horario', 'Cartel del horario', 'cuadro', 'PICKUP', 0.6, 'papel', 'pared', [caja(0.34, 0.42, 0.01, y=1.55, z=0.005, c='#f4f1e8'), plano(0.32, 0.4, y=1.55, z=0.0125, tex={'tipo': 'horario'})])
obj('cartel_guardia', 'Cartel de farmacia de guardia', 'cuadro', 'PICKUP', 0.7, 'papel', 'pared', [caja(0.4, 0.56, 0.012, y=1.6, z=0.006, c='#e8f2ea'), plano(0.38, 0.54, y=1.6, z=0.0146, tex={'tipo': 'cartel_guardia'})])
obj('folletero_farmacia', 'Expositor de folletos', 'comercio_expositor', 'PICKUP', 3, 'metal', 'pared', [
    caja(0.5, 0.9, 0.03, y=1.4, z=0.015, c='#d8dedf', m='metal'), caja(0.5, 0.08, 0.04, y=1.81, z=0.02, c='#25b34a', m='plastico')]
    + [caja(0.14, 0.2, 0.05, x=x, y=y, z=0.055, c=c, m='papel') for y in (1.1, 1.42) for x, c in ((-0.16, '#e0a24a'), (0.0, '#5a9ad0'), (0.16, '#d86a8a'))] + [caja(0.5, 0.04, 0.07, y=1.0, z=0.05, c='#d8dedf', m='metal'), caja(0.5, 0.04, 0.07, y=1.32, z=0.05, c='#d8dedf', m='metal')])
# the units of the waiting room
def asientos_fila(n, paso, h=0.45): return [{'p': [(i - (n - 1) / 2) * paso, h, 0.0], 'h': h, 'anim': 'silla'} for i in range(n)]
obj('banco_espera', 'Banco de sala de espera (3 plazas)', 'banco', 'CARRY', 18, 'metal', 'suelo', [
    caja(1.5, 0.05, 0.45, y=0.44, c='#2f6a4a', m='plastico'), caja(1.5, 0.3, 0.04, y=0.72, z=-0.2, c='#2f6a4a', m='plastico')] + [caja(0.04, 0.42, 0.04, x=x, y=0.21, z=z, c='#9aa0a4', m='metal') for x in (-0.7, 0.7) for z in (-0.18, 0.18)],
    modificadores=['SEAT'], asientos=asientos_fila(3, 0.46))
obj('silla_espera', 'Silla de sala de espera', 'silla', 'CARRY', 5.5, 'plastico', 'suelo', [
    caja(0.45, 0.04, 0.42, y=0.45, c='#2f6a4a', m='plastico'), caja(0.45, 0.32, 0.03, y=0.67, z=-0.195, c='#2f6a4a', m='plastico')] + [caja(0.03, 0.43, 0.03, x=sx * 0.2, y=0.215, z=sz * 0.18, c='#9aa0a4', m='metal') for sx in (-1, 1) for sz in (-1, 1)],
    modificadores=['SEAT'], asientos=[{'p': [0, 0.48, 0.02], 'h': 0.48, 'anim': 'silla'}])
obj('bascula_farmacia', 'Báscula de columna con tallímetro', 'mueble', 'CARRY', 14, 'metal', 'suelo', [
    caja(0.4, 0.04, 0.5, y=0.02, c='#e6e9ea', m='plastico'), caja(0.34, 0.006, 0.4, y=0.043, z=0.02, c='#2b2b2e', m='goma'), caja(0.08, 1.25, 0.06, y=0.66, z=-0.2, c='#e6e9ea', m='plastico'),
    caja(0.28, 0.12, 0.1, y=1.34, z=-0.18, c='#d9dedf', m='plastico'), caja(0.2, 0.05, 0.005, y=1.34, z=-0.13, c='#b8d4b0', m='plastico', luz=True), caja(0.012, 0.9, 0.003, x=0.1, y=0.9, z=-0.168, c='#2b2b2e', m='plastico')], nota='pesa y mide')
obj('tensiometro_automatico', 'Tensiómetro automático', 'comercio_expositor', 'PUSH', 30, 'plastico', 'suelo', [
    caja(0.42, 1.0, 0.36, y=0.5, z=-0.02, c='#dfe5e6', m='plastico'), caja(0.3, 0.18, 0.02, y=0.95, z=0.17, c='#2b3a3a', m='plastico', r=[-20, 0, 0]),
    plano(0.14, 0.07, y=0.96, z=0.184, tex={'tipo': 'tensiometro'}, r=[-20, 0, 0], luz=True), cil(0.06, 0.06, 0.2, y=0.72, z=0.17, c='#9aa0a4', m='plastico', r=[90, 0, 0], seg=10), caja(0.42, 0.06, 0.38, y=1.03, z=-0.02, c='#25b34a', m='plastico')],
    modificadores=['USE'], nota='para tomarse la tensión sentado al lado')
obj('dispensador_gel_pie', 'Dispensador de gel de pie', 'limpieza', 'PICKUP', 3.5, 'metal', 'suelo', [
    caja(0.28, 0.03, 0.28, y=0.015, c='#2b2b2e', m='metal'), cil(0.025, 0.025, 0.9, y=0.48, c=STEEL, seg=8), caja(0.1, 0.18, 0.1, y=1.05, c='#e6e9ea', m='plastico')])
obj('contenedor_envases', 'Punto de recogida de envases de medicamentos', 'comercio_expositor', 'PUSH', 26, 'plastico', 'suelo', [
    caja(0.42, 0.8, 0.32, c='#f4f6f6', m='plastico'), caja(0.4, 0.2, 0.005, y=0.62, z=0.162, c='#25b34a', m='plastico'), caja(0.2, 0.03, 0.01, y=0.5, z=0.165, c='#1a2a20', m='plastico')])
obj('cesta_farmacia', 'Cestita de pequeños productos', 'recipiente', 'PICKUP', 1.5, 'plastico', 'superficie', [
    caja(0.3, 0.1, 0.2, c='#f4f6f6', m='plastico'), caja(0.05, 0.06, 0.04, x=-0.08, y=0.12, c='#e0a4b0', m='plastico'), caja(0.05, 0.06, 0.04, x=0.0, y=0.12, c='#5a9ad0', m='plastico'), caja(0.05, 0.06, 0.04, x=0.08, y=0.12, c='#25b34a', m='plastico')])
# what stands on the counter
obj('monitor_pc_mostrador', 'Ordenador del mostrador', 'informatica', 'PICKUP', 3.5, 'plastico', 'superficie', [
    cil(0.1, 0.1, 0.015, c='#2b2b2e', seg=12), caja(0.04, 0.14, 0.03, y=0.085, c='#2b2b2e', m='plastico'), caja(0.46, 0.28, 0.025, y=0.26, c='#1c1c1f', m='plastico'), caja(0.42, 0.24, 0.004, y=0.26, z=-0.0145, c='#4a7a9a', m='plastico', luz=True)], nota='de cara al dependiente')
obj('teclado_mostrador', 'Teclado', 'informatica', 'PICKUP', 0.6, 'plastico', 'superficie', [caja(0.42, 0.02, 0.14, c='#2b2b2e', m='plastico'), caja(0.38, 0.004, 0.1, y=0.021, c='#4a4a4e', m='plastico')])
obj('lector_codigo', 'Lector de códigos de barras', 'informatica', 'PICKUP', 0.5, 'plastico', 'superficie', [cil(0.05, 0.06, 0.03, c='#2b2b2e', seg=10), caja(0.04, 0.1, 0.05, y=0.08, c='#2b2b2e', m='plastico'), caja(0.05, 0.04, 0.09, y=0.13, z=0.02, c='#1c1c1f', m='plastico')])
obj('impresora_ticket', 'Impresora de tickets', 'informatica', 'PICKUP', 1.2, 'plastico', 'superficie', [caja(0.16, 0.12, 0.2, c='#2b2b2e', m='plastico'), caja(0.12, 0.01, 0.06, y=0.125, z=0.06, c='#f4f2ec', m='papel')])
obj('dosificador_gel_mostrador', 'Dosificador de gel hidroalcohólico', 'limpieza', 'PICKUP', 0.6, 'plastico', 'superficie', [cil(0.03, 0.03, 0.16, c='#e6e9ea', m='plastico', seg=8), cil(0.012, 0.012, 0.05, y=0.185, c='#9aa0a4', m='plastico', seg=6), caja(0.03, 0.01, 0.05, y=0.215, z=0.02, c='#9aa0a4', m='plastico')])
obj('mampara_metacrilato', 'Mampara de metacrilato', 'decoracion', 'PICKUP', 2.2, 'cristal', 'superficie', [caja(0.9, 0.6, 0.008, y=0.3, c='#dcebf0', m='cristal'), caja(0.05, 0.02, 0.1, x=-0.35, y=0.01, c='#9aa0a4', m='metal'), caja(0.05, 0.02, 0.1, x=0.35, y=0.01, c='#9aa0a4', m='metal')])
obj('bandeja_cambio', 'Bandeja de cambio', 'recipiente', 'PICKUP', 0.5, 'plastico', 'superficie', [caja(0.2, 0.02, 0.14, c='#2b2b2e', m='plastico'), caja(0.2, 0.03, 0.006, y=0.03, z=0.07, c='#2b2b2e', m='plastico')])
obj('bote_caramelos_farmacia', 'Bote de caramelos', 'recipiente', 'PICKUP', 0.9, 'cristal', 'superficie', [cil(0.06, 0.06, 0.16, c='#dcebf0', m='cristal', seg=12), cil(0.065, 0.065, 0.025, y=0.17, c='#25b34a', m='plastico', seg=12)] + [esf(0.015, x, 0.05, z, c=c, m='comida') for x, z, c in ((-0.02, 0.01, '#e8a040'), (0.02, -0.01, '#c0302a'), (0, 0.03, '#f2d84a'))])
obj('expositor_mostrador', 'Expositor de cacao de labios', 'decoracion', 'PICKUP', 1.0, 'plastico', 'superficie', [
    caja(0.2, 0.02, 0.14, c='#f4f6f6', m='plastico'), caja(0.2, 0.2, 0.01, y=0.12, z=-0.06, c='#f4f6f6', m='plastico')] + [cil(0.008, 0.008, 0.06, x=x, y=0.05, z=0.0, c=c, m='plastico', seg=6) for x, c in ((-0.07, '#c85a7a'), (-0.035, '#e8a040'), (0, '#5a9ad0'), (0.035, '#25b34a'), (0.07, '#d86a8a'))])
obj('bolsa_farmacia', 'Bolsa de la farmacia', 'papel', 'PICKUP', 0.15, 'papel', 'superficie', [caja(0.2, 0.26, 0.08, c='#f4f6f6', m='papel'), caja(0.2, 0.06, 0.082, y=0.1, c='#25b34a', m='papel'), cil(0.004, 0.004, 0.08, x=-0.05, y=0.3, c='#9aa0a4', m='tela', seg=6), cil(0.004, 0.004, 0.08, x=0.05, y=0.3, c='#9aa0a4', m='tela', seg=6)])
# the dispensary at the back
obj('mesa_rebotica', 'Mesa de trabajo de la rebotica', 'mesa', 'PUSH', 38, 'metal', 'suelo', [
    caja(1.4, 0.04, 0.7, y=0.88, c='#d9dedf', m='metal'), caja(0.05, 0.86, 0.05, x=-0.65, y=0.43, z=-0.3, c=STEEL, m='metal'), caja(0.05, 0.86, 0.05, x=0.65, y=0.43, z=-0.3, c=STEEL, m='metal'),
    caja(0.05, 0.86, 0.05, x=-0.65, y=0.43, z=0.3, c=STEEL, m='metal'), caja(0.05, 0.86, 0.05, x=0.65, y=0.43, z=0.3, c=STEEL, m='metal'), caja(1.3, 0.03, 0.6, y=0.25, c='#c3c7ca', m='metal')],
    superficies=[{'y': 0.9, 'margen': 0.05}, {'y': 0.265, 'margen': 0.05}])
obj('balanza_precision', 'Balanza de precisión', 'pequeño_electrodomestico', 'PICKUP', 2.5, 'metal', 'superficie', [caja(0.22, 0.05, 0.28, c='#e6e9ea', m='plastico'), cil(0.08, 0.08, 0.008, y=0.058, c=STEEL, m='metal', seg=12), caja(0.1, 0.03, 0.01, y=0.03, z=0.141, c='#b8d4b0', m='plastico', luz=True)])
obj('mortero', 'Mortero con su mano', 'vajilla', 'PICKUP', 1.2, 'piedra', 'superficie', [cil(0.07, 0.04, 0.07, c='#e6e2d8', m='ceramica', seg=12), cil(0.012, 0.016, 0.16, x=0.03, y=0.11, c='#d8d4c8', m='ceramica', r=[0, 0, 22], seg=8)])
obj('frasco_laboratorio', 'Frascos de laboratorio', 'recipiente', 'PICKUP', 1.0, 'cristal', 'superficie', [cil(0.04, 0.04, 0.14, x=-0.05, y=0.07, c='#c8a860', m='cristal', seg=10), cil(0.045, 0.045, 0.1, x=0.05, y=0.05, c='#dcebf0', m='cristal', seg=10), cil(0.042, 0.042, 0.02, x=-0.05, y=0.15, c='#2b2b2e', m='plastico', seg=10)])
obj('nevera_farmacia', 'Nevera de medicamentos', 'nevera', 'PUSH_HEAVY', 82, 'metal', 'suelo', [
    caja(0.62, 0.86, 0.62, c='#f4f6f6', m='metal'), caja(0.58, 0.72, 0.01, y=0.44, z=0.315, c='#bcd6dc', m='cristal'), caja(0.5, 0.05, 0.01, y=0.8, z=0.32, c='#3a7a5a', m='plastico', luz=True),
    caja(0.5, 0.02, 0.5, y=0.3, c='#d8dde0', m='metal'), caja(0.5, 0.02, 0.5, y=0.55, c='#d8dde0', m='metal')], modificadores=['USE'], superficies=[{'y': 0.86, 'margen': 0.05}])
obj('armario_rebotica', 'Armario metálico de la rebotica', 'mueble', 'FIXED', 70, 'metal', 'pared', [caja(0.9, 1.9, 0.45, z=0.225, c='#cfd6da', m='metal'), caja(0.01, 1.8, 0.005, y=0.95, z=0.452, c='#9aa0a6', m='metal'), caja(0.08, 0.02, 0.02, x=-0.06, y=1.0, z=0.46, c='#2b2b2e', m='plastico'), caja(0.08, 0.02, 0.02, x=0.06, y=1.0, z=0.46, c='#2b2b2e', m='plastico')], motivo_fijo=FIJO)
obj('cubeta_pedido', 'Cubeta de pedido del almacén', 'caja', 'PICKUP', 3.5, 'plastico', 'superficie', [caja(0.5, 0.28, 0.35, c='#3a7a5a', m='plastico'), caja(0.46, 0.02, 0.31, y=0.29, c='#2f6a4a', m='plastico'), caja(0.2, 0.1, 0.004, y=0.16, z=0.177, c='#f4f6f6', m='papel')])

# ---- medicines: boxes standing in rows, the stock behind (a facing is ~ 0.4 m wide)
MED = {  # id: (name, main, band, h, nx)
    'analgesico': ('Analgésico', '#f2f4f6', '#2c5aa0', 0.12, 5), 'antiinflamatorio': ('Antiinflamatorio', '#f4f2ec', '#e0782a', 0.11, 5), 'antibiotico': ('Antibiótico', '#f2f5f2', '#2f8a4a', 0.12, 5),
    'antihistaminico': ('Antihistamínico', '#f4f2f6', '#7a4a9a', 0.1, 6), 'antigripal': ('Antigripal', '#f2c840', '#c0302a', 0.12, 5), 'protector_estomago': ('Protector de estómago', '#f2f5f5', '#2a9a9a', 0.11, 5),
    'vitaminas': ('Vitaminas', '#e8902a', '#f2d060', 0.1, 5), 'pomada': ('Pomada', '#f4f4f0', '#c0302a', 0.14, 6), 'colirio': ('Colirio', '#e8f0f4', '#5a9ad0', 0.09, 7),
    'suero': ('Suero fisiológico', '#5a9ad0', '#f2f4f6', 0.1, 6), 'tiritas': ('Tiritas', '#f2c4cc', '#f4f4f0', 0.1, 6), 'gasas': ('Gasas', '#f4f4f0', '#3a9a5a', 0.1, 6),
    'mascarillas': ('Mascarillas', '#bcd8ec', '#f4f4f0', 0.13, 4), 'termometro': ('Termómetro digital', '#f4f4f0', '#2a8a8a', 0.15, 4), 'pastillas_garganta': ('Pastillas para la garganta', '#c8e0a8', '#2f8a4a', 0.07, 6),
    'melatonina': ('Melatonina', '#2a3a6a', '#f2d060', 0.09, 6), 'magnesio': ('Magnesio', '#f4f4f0', '#d86a8a', 0.12, 5), 'colageno': ('Colágeno', '#e8d8f0', '#7a4a9a', 0.12, 5),
}
for k, (n_, c1, c2, h, nx) in MED.items():
    regis('medicamento_' + k, n_ + ' (cajas)', 'farmacia_producto', u_caja(0.062, h, 0.034, c1, c2), nx, 2, 0.068, 0.038, h, 0.24, c1, 0.02, mat='papel')
def u_jarabe(x, z):
    return [cil(0.032, 0.032, 0.14, x=x - 0.03, y=0.07, z=z, c='#6b4426', m='plastico', seg=8), cil(0.014, 0.014, 0.03, x=x - 0.03, y=0.155, z=z, c='#f4f4f0', m='plastico', seg=8), caja(0.05, 0.1, 0.034, x=x + 0.035, y=0.05, z=z, c='#f4f4f0', m='papel')]
regis('jarabe_tos', 'Jarabe para la tos', 'farmacia_producto', u_jarabe, 3, 1, 0.1, 0.07, 0.17, 0.22, '#f4f4f0', 0.18, mat='plastico')
regis('bote_vitaminas', 'Botes de vitaminas', 'farmacia_producto', u_bote(0.036, 0.1, '#f4f4f0', '#e0782a'), 4, 2, 0.08, 0.08, 0.1, 0.22, '#f4f4f0', 0.12, mat='plastico')
regis('spray_nasal', 'Spray nasal', 'farmacia_producto', u_botella(0.017, 0.12, '#bcd8ec', '#2c5aa0', '#f4f4f0'), 6, 2, 0.04, 0.04, 0.12, 0.22, '#bcd8ec', 0.06, mat='plastico')
regis('gotas_orales', 'Frascos de gotas', 'farmacia_producto', u_botella(0.02, 0.1, '#a87a3a', '#f4f4f0', '#2b2b2e'), 6, 2, 0.045, 0.045, 0.1, 0.22, '#a87a3a', 0.07, mat='plastico')
# ---- parapharmacy: creams, baby products, sun protection, hygiene
def u_tarro(r, h, c, tapa): return u_bote(r, h, c, tapa)
PARA = [
    ('crema_facial', 'Cremas faciales', u_tarro(0.04, 0.06, '#f4eee6', '#d8b0a0'), 4, 2, 0.085, 0.085, 0.06, 0.3, '#f4eee6', 0.12),
    ('crema_manos', 'Cremas de manos', u_tubo(0.05, 0.13, '#f2c4cc', '#d86a8a'), 5, 2, 0.06, 0.04, 0.13, 0.28, '#f2c4cc', 0.1),
    ('protector_solar', 'Protector solar', u_botella(0.032, 0.17, '#f2a82a', '#f6e8b0', '#f4f4f0'), 4, 1, 0.075, 0.07, 0.17, 0.26, '#f2a82a', 0.28),
    ('protector_solar_spray', 'Protector solar en spray', u_botella(0.03, 0.2, '#e8d84a', '#f4f4f0', '#2c5aa0'), 4, 1, 0.07, 0.065, 0.2, 0.26, '#e8d84a', 0.25),
    ('leche_corporal', 'Leche corporal', u_botella(0.04, 0.2, '#f4f4f0', '#d8a8b8', '#d86a8a'), 3, 1, 0.09, 0.08, 0.2, 0.26, '#f4f4f0', 0.35),
    ('champu', 'Champú', u_botella(0.036, 0.2, '#6ab08a', '#f4f4f0', '#2f8a4a'), 4, 1, 0.08, 0.075, 0.2, 0.26, '#6ab08a', 0.35),
    ('gel_bano', 'Gel de baño', u_botella(0.038, 0.21, '#5a9ad0', '#f4f4f0', '#2c5aa0'), 4, 1, 0.082, 0.078, 0.21, 0.26, '#5a9ad0', 0.4),
    ('pasta_dientes', 'Pasta de dientes', u_caja(0.045, 0.18, 0.035, '#2c8ad0', '#f4f4f0'), 6, 2, 0.05, 0.04, 0.18, 0.24, '#2c8ad0', 0.15),
    ('panales', 'Paquetes de pañales', u_caja(0.26, 0.29, 0.14, '#7ac0e8', '#f4f4f0', banda=0.3, m='plastico'), 1, 2, 0.26, 0.15, 0.29, 0.31, '#7ac0e8', 1.6),
    ('toallitas_bebe', 'Toallitas de bebé', u_caja(0.15, 0.1, 0.09, '#8ad08a', '#f4f4f0', banda=0.3, m='plastico'), 2, 3, 0.16, 0.1, 0.1, 0.3, '#8ad08a', 0.4),
    ('leche_infantil', 'Leche infantil en polvo', u_bote(0.055, 0.15, '#f0e6c8', '#3a7aa8'), 3, 2, 0.12, 0.12, 0.15, 0.3, '#f0e6c8', 0.6),
    ('papilla', 'Tarritos de papilla', u_bote(0.035, 0.07, '#f2d880', '#7ac0e8'), 4, 3, 0.075, 0.075, 0.07, 0.3, '#f2d880', 0.2),
    ('biberon', 'Biberones', u_botella(0.03, 0.19, '#ecf0f2', '#bcd8ec', '#e8a0b8'), 4, 1, 0.07, 0.07, 0.19, 0.24, '#ecf0f2', 0.3),
    ('chupetes', 'Chupetes en blíster', u_caja(0.1, 0.16, 0.03, '#f4f4f0', '#e8a0b8', banda=0.5), 3, 2, 0.11, 0.04, 0.16, 0.24, '#f4f4f0', 0.1),
    ('desodorante', 'Desodorantes', u_botella(0.022, 0.16, '#e6eaec', '#5a9ad0', '#2b2b2e'), 5, 2, 0.052, 0.052, 0.16, 0.26, '#e6eaec', 0.15),
    ('colonia_bebe', 'Colonia de bebé', u_botella(0.035, 0.17, '#f4e8c8', '#f4f4f0', '#7ac0e8'), 4, 1, 0.08, 0.07, 0.17, 0.26, '#f4e8c8', 0.3),
    ('cepillos_dientes', 'Cepillos de dientes', u_caja(0.045, 0.2, 0.025, '#e0782a', '#f4f4f0', banda=0.4), 7, 2, 0.05, 0.03, 0.2, 0.24, '#e0782a', 0.05),
    ('contorno_ojos', 'Contornos de ojos', u_tubo(0.032, 0.11, '#e8d8f0', '#7a4a9a'), 6, 2, 0.04, 0.035, 0.11, 0.26, '#e8d8f0', 0.06),
    ('mascarilla_facial', 'Mascarillas faciales en sobre', u_caja(0.09, 0.14, 0.012, '#cfe8d0', '#2f8a4a', banda=0.3), 4, 3, 0.095, 0.02, 0.14, 0.24, '#cfe8d0', 0.03),
    ('agua_termal', 'Agua termal en spray', u_lata(0.03, 0.17, '#bcd8ec', '#f4f4f0'), 5, 1, 0.07, 0.07, 0.17, 0.26, '#bcd8ec', 0.22),
]
for k, n_, unit, nx, nz, dx, dz, h, fondo, c, mu in PARA:
    regis('para_' + k, n_, 'comercio_hogar', unit, nx, nz, dx, dz, h, fondo, c, mu, mat='plastico')

# ==== SUPERMERCADO ====

# ================================================================== THE SUPERMARKET (alimentacion): fixtures
estantes('gondola_super', 'Góndola de supermercado (1 m)', 1.0, 0.42, [0.2, 0.56, 0.92, 1.28], 1.65, c='#cdd5d9', cp='#f2f4f4', masa=60, nota='por una cara: se pone de dos en dos, espalda con espalda; baldas de 36 cm')
estantes('estanteria_super_pared', 'Estantería de pared de supermercado (1 m)', 1.0, 0.42, [0.2, 0.56, 0.92, 1.28, 1.64], 2.05, c='#cdd5d9', cp='#f2f4f4', masa=65)
estantes('expositor_dulces', 'Expositor de dulces junto a las cajas', 0.8, 0.36, [0.3, 0.6, 0.9, 1.2], 1.45, c='#e0782a', cp='#f6f2ea', cat='comercio_expositor', masa=25)
estantes('expositor_pan', 'Expositor de pan', 0.9, 0.5, [0.3, 0.7, 1.1, 1.5], 1.7, c='#a97a4a', cp='#c8a06a', cat='comercio_expositor', masa=35)
estantes('nevera_lacteos', 'Nevera mural de lácteos y fresco', 1.25, 0.7, [0.35, 0.7, 1.05, 1.4], 2.0, c='#dfe6ea', cp='#f2f6f8', cat='nevera', masa=130, nota='abierta por delante, con su luz')
OUT[-1]['partes'] += [caja(1.25, 0.2, 0.74, y=1.9, z=0.37, c='#2f7a3a', m='plastico'), caja(1.2, 0.02, 0.05, y=1.78, z=0.55, c='#ffffff', m='plastico', luz=True)]
estantes('nevera_bebidas_super', 'Nevera mural de bebidas con puertas de cristal', 1.25, 0.7, [0.3, 0.65, 1.0, 1.35], 1.95, c='#cfd8dc', cp='#f2f6f8', cat='nevera', masa=140, nota='dos puertas de cristal')
OUT[-1]['partes'] += [caja(1.25, 0.2, 0.74, y=1.85, z=0.37, c='#2c5aa0', m='plastico'), caja(1.2, 0.02, 0.05, y=1.73, z=0.55, c='#e8f4ff', m='plastico', luz=True),
                      caja(0.6, 1.62, 0.01, x=-0.31, y=0.95, z=0.715, c='#bcd6dc', m='cristal'), caja(0.6, 1.62, 0.01, x=0.31, y=0.95, z=0.715, c='#bcd6dc', m='cristal'),
                      cil(0.01, 0.01, 0.5, x=-0.02, y=1.0, z=0.73, c=STEEL, seg=6), cil(0.01, 0.01, 0.5, x=0.02, y=1.0, z=0.73, c=STEEL, seg=6)]
# freezer island: the chest, its goods in rows under a glass lid
def congelador():
    P = [caja(1.6, 0.85, 0.8, y=0.425, c='#e9eef0', m='metal'), caja(1.6, 0.04, 0.8, y=0.02, c='#2b2b2e', m='metal')]
    cols = ['#c0302a', '#2c5aa0', '#e8c030', '#3a8a3a', '#e0782a', '#f4f4f0', '#7a4a9a', '#2a9a9a']
    for i in range(8):
        for j in range(3):
            P.append(caja(0.18, 0.14, 0.22, x=-0.7 + i * 0.2, y=0.92, z=-0.26 + j * 0.26, c=cols[(i * 3 + j * 5) % len(cols)], m='papel'))
    P += [caja(1.5, 0.02, 0.74, y=1.02, c='#d8eaf0', m='cristal'), caja(1.6, 0.04, 0.03, y=0.87, z=0.385, c='#9aa0a4', m='metal'), caja(1.6, 0.04, 0.03, y=0.87, z=-0.385, c='#9aa0a4', m='metal')]
    obj('congelador_isla', 'Congelador de isla con tapa de cristal', 'comercio_expositor', 'FIXED', 110, 'metal', 'suelo', P, motivo_fijo=FIJO, nota='helados, pizzas, verduras y pescado congelados')
congelador()
obj('mesa_fruteria', 'Mesa de frutería', 'mesa', 'PUSH', 35, 'madera', 'suelo', [
    caja(1.2, 0.04, 0.8, y=0.78, c='#8a5a36')] + [caja(0.05, 0.76, 0.05, x=sx * 0.55, y=0.38, z=sz * 0.35, c=WOOD_D) for sx in (-1, 1) for sz in (-1, 1)] + [caja(1.1, 0.03, 0.7, y=0.25, c='#a07040')],
    superficies=[{'y': 0.8, 'margen': 0.04}, {'y': 0.265, 'margen': 0.04}], nota='con los cajones de fruta y verdura')
obj('caja_super_modulo', 'Caja de cobro con cinta (1,9 m)', 'mostrador', 'FIXED', 220, 'metal', 'suelo', [
    caja(1.9, 0.78, 0.8, y=0.39, c='#cfd5d8'), caja(1.15, 0.03, 0.5, x=-0.35, y=0.795, z=0.14, c='#2b2b2e', m='goma'), caja(1.15, 0.04, 0.02, x=-0.35, y=0.83, z=0.4, c=STEEL, m='metal'),
    caja(0.6, 0.12, 0.5, x=0.6, y=0.84, z=-0.05, c='#9aa0a4', m='metal'), caja(0.22, 0.004, 0.15, x=0.45, y=0.902, z=0.0, c='#1c3a4a', m='cristal', luz=True),
    cil(0.02, 0.02, 0.2, x=0.62, y=1.0, z=-0.22, c='#2b2b2e', seg=8), caja(0.34, 0.24, 0.03, x=0.62, y=1.18, z=-0.22, c='#27272a', m='plastico'), caja(0.3, 0.2, 0.004, x=0.62, y=1.18, z=-0.238, c='#4a7a9a', m='plastico', luz=True),
    caja(1.9, 0.5, 0.01, y=0.4, z=0.405, c='#2f7a3a', m='plastico'), caja(0.5, 0.05, 0.4, x=0.6, y=0.585, z=-0.36, c='#9aa0a4', m='metal')],
    motivo_fijo='estructural', superficies=[{'y': 0.81, 'margen': 0.04}], nota='la cinta hacia la izquierda; el cajero, al otro lado')
obj('silla_cajera', 'Silla de cajera', 'silla', 'CARRY', 8, 'metal', 'suelo', [
    cil(0.2, 0.2, 0.05, y=0.5, c='#2f3a3a', m='tela', seg=12), caja(0.4, 0.3, 0.04, y=0.78, z=-0.2, c='#2f3a3a', m='tela'), cil(0.025, 0.025, 0.4, y=0.25, c=STEEL, seg=8),
    caja(0.5, 0.03, 0.06, y=0.015, c='#2b2b2e', m='metal'), caja(0.06, 0.03, 0.5, y=0.015, c='#2b2b2e', m='metal')], modificadores=['SEAT'], asientos=[{'p': [0, 0.52, 0.0], 'h': 0.52, 'anim': 'silla'}])
obj('carrito_compra', 'Carro de la compra', 'comercio_carro', 'CARRY', 12, 'metal', 'suelo', [
    caja(0.5, 0.03, 0.9, y=0.15, c=STEEL, m='metal'), caja(0.5, 0.3, 0.9, y=0.38, c='#cfd6da', m='cristal'), cil(0.012, 0.012, 0.5, y=0.97, z=-0.48, c='#2f7a3a', r=[0, 0, 90], seg=8),
    caja(0.03, 0.55, 0.03, x=-0.24, y=0.7, z=-0.46, c='#2f7a3a', m='plastico'), caja(0.03, 0.55, 0.03, x=0.24, y=0.7, z=-0.46, c='#2f7a3a', m='plastico')]
    + [cil(0.04, 0.04, 0.03, x=sx * 0.22, y=0.04, z=sz * 0.38, c='#2b2b2e', m='goma', r=[0, 0, 90], seg=8) for sx in (-1, 1) for sz in (-1, 1)], nota='con su rejilla de cristal ligero: se ve lo que lleva')
obj('cesta_compra_roja', 'Cesta de la compra', 'recipiente', 'PICKUP', 1.2, 'plastico', 'suelo', [
    caja(0.42, 0.22, 0.28, c='#c0302a', m='plastico'), caja(0.38, 0.02, 0.24, y=0.225, c='#8a1c18', m='plastico'), cil(0.008, 0.008, 0.36, y=0.3, c=STEEL, r=[0, 0, 90], seg=6)])
obj('pila_cestas', 'Pila de cestas de la compra', 'recipiente', 'CARRY', 6, 'plastico', 'suelo', [
    caja(0.42, 0.5, 0.28, c='#c0302a', m='plastico')] + [caja(0.43, 0.012, 0.29, y=0.16 + i * 0.07, c='#e0584a', m='plastico') for i in range(5)])
obj('cesta_compra_llena', 'Cesta con la compra', 'recipiente', 'PICKUP', 3.5, 'plastico', 'superficie', [
    caja(0.42, 0.2, 0.28, c='#2f7a3a', m='plastico'), caja(0.1, 0.16, 0.08, x=-0.12, y=0.28, c='#e0782a', m='papel'), caja(0.12, 0.1, 0.1, x=0.06, y=0.25, c='#f4f0e0', m='papel'), cil(0.03, 0.03, 0.2, x=0.14, y=0.3, c='#5a7a2a', seg=8)])
obj('separador_cinta', 'Separador de compras', 'decoracion', 'PICKUP', 0.2, 'plastico', 'superficie', [caja(0.4, 0.04, 0.025, c='#2f7a3a', m='plastico')])
obj('cortadora_fiambre', 'Cortadora de fiambre', 'pequeño_electrodomestico', 'CARRY', 14, 'metal', 'superficie', [
    caja(0.45, 0.1, 0.34, c='#d8dde0', m='metal'), cil(0.14, 0.14, 0.02, x=-0.05, y=0.17, z=0.02, c=STEEL, m='metal', r=[0, 0, 80], seg=16), caja(0.12, 0.2, 0.2, x=0.13, y=0.2, z=0.0, c='#d8dde0', m='metal')], nota='para el jamón y el fiambre')
obj('balanza_comercial', 'Balanza comercial', 'pequeño_electrodomestico', 'PICKUP', 4.5, 'metal', 'superficie', [
    caja(0.32, 0.06, 0.34, c='#e6e9ea', m='metal'), caja(0.28, 0.01, 0.26, y=0.065, z=0.02, c=STEEL, m='metal'), caja(0.05, 0.2, 0.05, y=0.16, z=-0.14, c='#e6e9ea', m='metal'), caja(0.22, 0.09, 0.04, y=0.3, z=-0.14, c='#2b2b2e', m='plastico'), caja(0.18, 0.05, 0.004, y=0.3, z=-0.118, c='#b8d4b0', m='plastico', luz=True)])
obj('mesa_trabajo_charcuteria', 'Mesa de acero de la charcutería', 'mesa', 'PUSH', 40, 'metal', 'suelo', [
    caja(1.2, 0.04, 0.7, y=0.88, c='#d9dedf', m='metal')] + [caja(0.05, 0.86, 0.05, x=sx * 0.55, y=0.43, z=sz * 0.3, c=STEEL, m='metal') for sx in (-1, 1) for sz in (-1, 1)] + [caja(1.1, 0.03, 0.6, y=0.25, c='#c3c7ca', m='metal')],
    superficies=[{'y': 0.9, 'margen': 0.05}])
obj('mostrador_charcuteria_modulo', 'Mostrador de charcutería y quesos (1,2 m)', 'mostrador', 'FIXED', 210, 'cristal', 'suelo', [
    caja(1.2, 0.85, 0.7, y=0.425, c='#e9eef0', m='metal'), caja(1.2, 0.04, 0.45, y=0.87, z=-0.125, c='#d9dedf', m='metal'), caja(1.1, 0.02, 0.25, y=0.86, z=0.225, c=STEEL, m='metal'),
    caja(1.2, 0.3, 0.01, y=1.05, z=0.345, c='#d8eaf0', m='cristal'), caja(1.2, 0.01, 0.28, y=1.21, z=0.21, c='#d8eaf0', m='cristal'), caja(1.2, 0.02, 0.01, y=1.2, z=0.345, c='#9aa0a4', m='metal'),
    caja(0.3, 0.07, 0.18, x=-0.38, y=0.905, z=0.225, c='#8a3a2a', m='comida'), caja(0.26, 0.05, 0.16, x=-0.05, y=0.895, z=0.225, c='#e8c860', m='comida'), cil(0.07, 0.07, 0.05, x=0.3, y=0.895, z=0.225, c='#efe0a0', m='comida', seg=10),
    caja(0.2, 0.03, 0.12, x=0.48, y=0.885, z=0.18, c='#c8584a', m='comida'), cil(0.025, 0.025, 0.28, x=0.18, y=0.895, z=0.17, c='#7a2a1c', m='comida', r=[0, 0, 90], seg=8)],
    motivo_fijo='estructural', superficies=[{'y': 0.89, 'margen': 0.04}], nota='jamón, queso, embutidos y el torta del Casar a la vista')


# ---- the rest of the shop floor: pallets, promotions, signs, safety, the storeroom
def palet(id, nombre, cols, caja_dim=(0.58, 0.28, 0.38), capas=3, masa=100, wrap='#dcebf0'):
    w, h, d = caja_dim
    P = [caja(1.2, 0.14, 0.8, y=0.07, c='#b88a58', m='madera')]
    for k in range(capas):
        for i in range(2):
            for j in range(2):
                P.append(caja(w, h, d, x=(i - 0.5) * (w + 0.01), y=0.14 + h * (k + 0.5), z=(j - 0.5) * (d + 0.01) * 1.0, c=cols[(i + j + k) % len(cols)], m='plastico'))
    P.append(caja(1.2, 0.01, 0.8, y=0.14 + h * capas + 0.005, c=wrap, m='cristal'))
    obj(id, nombre, 'comercio_expositor', 'PUSH_HEAVY', masa, 'plastico', 'suelo', P, nota='palé de oferta junto a la entrada')
palet('palet_agua', 'Palé de agua mineral en packs', ['#9ecbe8', '#7ab4de', '#b8d8ee'], masa=118)
palet('palet_refrescos', 'Palé de refrescos', ['#c0302a', '#e0782a', '#e8c030'], masa=100)
palet('palet_leche', 'Palé de leche en packs', ['#f4f4f0', '#2c5aa0', '#7ac0e8'], masa=105)
palet('palet_aceite', 'Palé de garrafas de aceite', ['#5a7a2a', '#e8d890', '#7a9a3a'], caja_dim=(0.58, 0.3, 0.38), masa=110)
palet('palet_detergente', 'Palé de detergente', ['#2c8ad0', '#f4f4f0', '#2c5aa0'], capas=2, masa=90)
def torre_latas(id, nombre, c, c2):
    P = []
    for k, n in enumerate((4, 3, 2, 1)):
        for i in range(n):
            P += [cil(0.04, 0.04, 0.1, x=(i - (n - 1) / 2) * 0.085, y=0.05 + k * 0.1, c=c, m='metal', seg=8), cil(0.041, 0.041, 0.05, x=(i - (n - 1) / 2) * 0.085, y=0.05 + k * 0.1, c=c2, m='papel', seg=8)]
    P = [caja(0.5, 0.05, 0.3, y=0.025, c='#e0782a', m='madera')] + [{**q, 'p': [q['p'][0], q['p'][1] + 0.05, 0.0]} for q in P]
    obj(id, nombre, 'alimento', 'PICKUP', 4.2, 'metal', 'suelo', P, nota='torre de latas en oferta')
torre_latas('torre_latas_maiz', 'Torre de latas de maíz dulce en oferta', '#e8c030', '#3a8a3a')
torre_latas('torre_latas_tomate', 'Torre de latas de tomate en oferta', '#c0302a', '#f4f0e0')
for k, (nom, sub, fondo, col) in {'fruta': ('FRUTAS Y VERDURAS', 'del campo, de las Vegas', '#2f7a3a', '#ffffff'), 'charcuteria': ('CHARCUTERÍA Y QUESOS', 'jamón, queso y embutido', '#a8302a', '#ffffff'),
                                  'pan': ('PAN Y BOLLERÍA', 'recién hecho', '#a8702a', '#ffffff'), 'congelados': ('CONGELADOS', '', '#2c6ab0', '#ffffff'), 'lacteos': ('LÁCTEOS Y FRESCOS', 'leche, yogur y mantequilla', '#2a8a9a', '#ffffff'),
                                  'bebidas': ('BEBIDAS', 'agua, zumos y refrescos', '#2c5aa0', '#ffffff'), 'conservas': ('CONSERVAS, ARROZ Y PASTA', '', '#c0782a', '#ffffff'), 'limpieza': ('LIMPIEZA E HIGIENE', 'hogar y cuidado personal', '#6a3a8a', '#ffffff'),
                                  'dulces': ('GALLETAS Y DESAYUNO', '', '#d86a8a', '#ffffff')}.items():
    obj('cartel_seccion_' + k, 'Cartel colgado de «%s»' % nom.lower(), 'decoracion', 'FIXED', 3, 'plastico', 'techo', [
        cil(0.004, 0.004, 0.5, x=-0.55, y=-0.25, c=STEEL, seg=6), cil(0.004, 0.004, 0.5, x=0.55, y=-0.25, c=STEEL, seg=6), caja(1.4, 0.36, 0.02, y=-0.7, c='#2a2a2e', m='plastico'),
        plano(1.36, 0.32, y=-0.7, z=-0.0125, r=[0, 180, 0], tex={'tipo': 'seccion', 'texto': nom, 'sub': sub, 'fondo': fondo, 'color': col})], motivo_fijo=FIJO, nota='de cara a la entrada')
for n in (1, 2):
    obj('numero_caja_%d' % n, 'Indicador de la caja %d' % n, 'decoracion', 'FIXED', 2, 'plastico', 'techo', [
        cil(0.004, 0.004, 0.45, x=-0.1, y=-0.225, c=STEEL, seg=6), cil(0.004, 0.004, 0.45, x=0.1, y=-0.225, c=STEEL, seg=6), caja(0.3, 0.3, 0.03, y=-0.6, c='#27272a', m='plastico'),
        plano(0.27, 0.27, y=-0.6, z=-0.0185, r=[0, 180, 0], tex={'tipo': 'caja_numero', 'n': n})], motivo_fijo=FIJO)
for k, (t, sub) in {'2x1': ('2x1', 'en galletas'), '3x2': ('3x2', 'en limpieza')}.items():
    obj('cartel_oferta_' + k, 'Cartel de oferta %s' % t, 'cuadro', 'PICKUP', 0.5, 'papel', 'pared', [
        caja(0.5, 0.5, 0.012, y=1.75, z=0.006, c='#c0302a'), plano(0.46, 0.46, y=1.75, z=0.0146, tex={'tipo': 'cartel_oferta', 'texto': t, 'sub': sub})])
for k, (lineas) in {'fruteria': ['Melocotón  2,49', 'Naranjas  1,29', 'Manzanas  1,59', 'Tomate  1,99', 'Patatas  0,89', 'Melón  1,19'], 'charcuteria': ['Jamón  18,90', 'Queso curado  11,50', 'Chorizo  8,95', 'Torta  9,00', 'Salchichón  7,80']}.items():
    obj('pizarra_' + k, 'Pizarra de precios de la %s' % ('frutería' if k == 'fruteria' else 'charcutería'), 'decoracion', 'PICKUP', 3, 'madera', 'pared', [
        caja(0.9, 0.62, 0.025, y=1.7, z=0.0125, c='#5a3a20'), plano(0.84, 0.56, y=1.7, z=0.0285, tex={'tipo': 'pizarra', 'lineas': lineas})])
obj('extintor_super', 'Extintor', 'comercio_seguridad', 'FIXED', 6, 'metal', 'pared', [
    cil(0.07, 0.07, 0.4, y=0.9, z=0.08, c='#c0302a', m='metal', seg=10), cil(0.02, 0.03, 0.08, y=1.14, z=0.08, c='#2b2b2e', m='metal', seg=8), caja(0.12, 0.02, 0.04, y=0.88, z=0.01, c='#2b2b2e', m='metal')], motivo_fijo=FIJO)
obj('espejo_convexo', 'Espejo convexo de seguridad', 'espejo', 'FIXED', 3, 'cristal', 'pared', [
    cil(0.25, 0.25, 0.04, y=2.35, z=0.02, c=MIRROR, m='metal', r=[90, 0, 0], seg=18), cil(0.26, 0.26, 0.02, y=2.35, z=0.012, c='#c0302a', m='plastico', r=[90, 0, 0], seg=18)], motivo_fijo=FIJO)
obj('camara_cupula', 'Cámara de seguridad de cúpula', 'comercio_seguridad', 'FIXED', 1.2, 'plastico', 'techo', [
    cil(0.08, 0.08, 0.04, y=-0.02, c='#e6e9ea', m='plastico', seg=12), esf(0.07, 0, -0.07, 0, c='#1c1c1f', m='plastico')], motivo_fijo=FIJO)
obj('senal_salida_super', 'Señal luminosa de salida', 'decoracion', 'FIXED', 1.2, 'plastico', 'pared', [
    caja(0.4, 0.14, 0.04, y=2.6, z=0.02, c='#1f7a40', m='plastico'), caja(0.34, 0.08, 0.004, y=2.6, z=0.042, c='#d8f5de', m='plastico', luz=True)], motivo_fijo=FIJO)
obj('palet_madera', 'Palé de madera vacío', 'comercio_expositor', 'PUSH', 25, 'madera', 'suelo', [
    caja(1.2, 0.03, 0.8, y=0.135, c='#b88a58')] + [caja(0.12, 0.12, 0.8, x=x, y=0.06, c='#a07848') for x in (-0.54, 0, 0.54)] + [caja(1.2, 0.02, 0.1, y=0.01, z=z, c='#a07848') for z in (-0.35, 0, 0.35)])
obj('transpaleta', 'Transpaleta', 'comercio_expositor', 'PUSH', 62, 'metal', 'suelo', [
    caja(0.16, 0.08, 1.1, x=-0.25, y=0.04, z=0.1, c='#c0302a', m='metal'), caja(0.16, 0.08, 1.1, x=0.25, y=0.04, z=0.1, c='#c0302a', m='metal'), caja(0.66, 0.2, 0.15, y=0.2, z=-0.45, c='#c0302a', m='metal'),
    cil(0.015, 0.015, 1.0, y=0.65, z=-0.55, c='#2b2b2e', r=[-12, 0, 0], seg=8), cil(0.015, 0.015, 0.3, y=1.12, z=-0.6, c='#2b2b2e', r=[0, 0, 90], seg=8)])
obj('carretilla_mano', 'Carretilla de mano', 'comercio_expositor', 'CARRY', 9, 'metal', 'suelo', [
    caja(0.04, 1.1, 0.04, x=-0.2, y=0.55, z=-0.15, c='#c0302a', m='metal'), caja(0.04, 1.1, 0.04, x=0.2, y=0.55, z=-0.15, c='#c0302a', m='metal'), caja(0.4, 0.02, 0.22, y=0.02, z=-0.02, c='#9aa0a4', m='metal'),
    cil(0.1, 0.1, 0.04, x=-0.22, y=0.1, z=-0.2, c='#2b2b2e', m='goma', r=[0, 0, 90], seg=10), cil(0.1, 0.1, 0.04, x=0.22, y=0.1, z=-0.2, c='#2b2b2e', m='goma', r=[0, 0, 90], seg=10)])
obj('pila_cajones_vacios', 'Pila de cajones de fruta vacíos', 'caja', 'CARRY', 7, 'plastico', 'suelo', [caja(0.5, 0.16, 0.34, y=0.08 + i * 0.16, c='#3f7a45', m='plastico') for i in range(5)])


# ---- the goods: facings on the shelves (dry goods and drinks at 0.3 m of stock, fridges at 0.55), crates of fruit and vegetables
def u_lata_ap(r, h, n, c, c2):
    def f(x, z):
        P = []
        for k in range(n):
            P += [cil(r, r, h, x=x, y=h / 2 + k * h, z=z, c=c, m='metal', seg=8), cil(r + 0.001, r + 0.001, h * 0.6, x=x, y=h / 2 + k * h, z=z, c=c2, m='papel', seg=8)]
        return P
    return f
def u_pack(c, c2, r=0.028, h=0.06):
    def f(x, z):
        return [cil(r, r * 0.85, h, x=x + dx, y=h / 2, z=z + dz, c=c, m='plastico', seg=7) for dx in (-0.03, 0.03) for dz in (-0.03, 0.03)] + [caja(0.125, 0.012, 0.125, x=x, y=h + 0.004, z=z, c=c2, m='papel')]
    return f
def u_bolsa(w, h, d, c, c2):
    return u_caja(w, h, d, c, c2, banda=0.3, m='plastico')
SECO = [  # id, name, unit, nx, nz, dx, dz, h, fondo, colour, kg a unit
    ('atun', 'Latas de atún', u_lata_ap(0.038, 0.05, 2, '#2a5a9a', '#e8e0c0'), 4, 2, 0.08, 0.08, 0.1, 0.32, '#2a5a9a', 0.2),
    ('sardinillas', 'Latas de sardinillas', u_lata_ap(0.034, 0.035, 3, '#c0302a', '#e8d8b0'), 4, 2, 0.072, 0.072, 0.105, 0.3, '#c0302a', 0.12),
    ('mejillones', 'Latas de mejillones', u_lata_ap(0.034, 0.045, 2, '#e0782a', '#2a2a2e'), 4, 2, 0.072, 0.072, 0.09, 0.3, '#e0782a', 0.15),
    ('tomate_frito', 'Briks de tomate frito', u_caja(0.07, 0.15, 0.045, '#c0302a', '#f2e0b0'), 5, 2, 0.075, 0.05, 0.15, 0.3, '#c0302a', 0.4),
    ('maiz', 'Latas de maíz dulce', u_lata(0.037, 0.1, '#e8c030', '#3a8a3a'), 4, 2, 0.078, 0.078, 0.1, 0.31, '#e8c030', 0.3),
    ('judias_verdes', 'Latas de judías verdes', u_lata(0.037, 0.11, '#3a8a3a', '#f4f0e0'), 4, 2, 0.078, 0.078, 0.11, 0.31, '#3a8a3a', 0.35),
    ('garbanzos_bote', 'Botes de garbanzos cocidos', u_bote(0.04, 0.17, '#d8c8a0', '#3a8a3a'), 4, 2, 0.085, 0.085, 0.17, 0.32, '#d8c8a0', 0.7),
    ('pimientos_piquillo', 'Botes de pimientos del piquillo', u_bote(0.038, 0.12, '#c0302a', '#f2f0e0'), 4, 2, 0.08, 0.08, 0.12, 0.3, '#c0302a', 0.4),
    ('aceitunas', 'Botes de aceitunas', u_bote(0.036, 0.12, '#7a8a2a', '#c0302a'), 4, 2, 0.078, 0.078, 0.12, 0.3, '#7a8a2a', 0.35),
    ('pepinillos', 'Botes de pepinillos', u_bote(0.036, 0.13, '#8ab04a', '#f2f0e0'), 4, 2, 0.078, 0.078, 0.13, 0.3, '#8ab04a', 0.4),
    ('mermelada', 'Botes de mermelada de fresa', u_bote(0.036, 0.09, '#b02a5a', '#f4f0e0'), 4, 3, 0.078, 0.078, 0.09, 0.3, '#b02a5a', 0.4),
    ('miel', 'Botes de miel', u_bote(0.04, 0.1, '#e0a020', '#3a2a1a'), 4, 3, 0.085, 0.085, 0.1, 0.3, '#e0a020', 0.6),
    ('crema_cacao', 'Botes de crema de cacao', u_bote(0.042, 0.1, '#6b4426', '#f4f0e0'), 4, 3, 0.088, 0.088, 0.1, 0.3, '#6b4426', 0.5),
    ('melocoton_almibar', 'Latas de melocotón en almíbar', u_lata(0.05, 0.11, '#f2a030', '#f4f0e0'), 3, 2, 0.105, 0.105, 0.11, 0.32, '#f2a030', 0.5),
    ('aceite_oliva', 'Botellas de aceite de oliva virgen extra', u_botella(0.04, 0.28, '#5a7a2a', '#e8d890', '#c8a040'), 3, 1, 0.09, 0.09, 0.28, 0.3, '#5a7a2a', 0.95),
    ('aceite_girasol', 'Botellas de aceite de girasol', u_botella(0.045, 0.29, '#e8c030', '#f4f0e0', '#e8c030'), 3, 1, 0.1, 0.1, 0.29, 0.3, '#e8c030', 0.95),
    ('garrafa_aceite', 'Garrafas de aceite de 5 litros', u_caja(0.19, 0.3, 0.12, '#5a7a2a', '#e8d890', m='plastico'), 2, 2, 0.2, 0.14, 0.3, 0.32, '#5a7a2a', 4.6),
    ('vinagre', 'Botellas de vinagre', u_botella(0.032, 0.24, '#5a2a2a', '#f4f0e0', '#2a2a2a'), 4, 2, 0.07, 0.07, 0.24, 0.3, '#5a2a2a', 0.6),
    ('arroz', 'Paquetes de arroz', u_caja(0.1, 0.17, 0.06, '#f4f0e0', '#2c5aa0'), 4, 2, 0.105, 0.065, 0.17, 0.3, '#f4f0e0', 1.0),
    ('arroz_integral', 'Paquetes de arroz integral', u_caja(0.1, 0.17, 0.06, '#d8c8a0', '#3a8a3a'), 4, 2, 0.105, 0.065, 0.17, 0.3, '#d8c8a0', 1.0),
    ('espaguetis', 'Paquetes de espaguetis', u_caja(0.06, 0.26, 0.04, '#e8c040', '#c0302a'), 5, 2, 0.065, 0.045, 0.26, 0.3, '#e8c040', 0.5),
    ('macarrones', 'Paquetes de macarrones', u_caja(0.11, 0.2, 0.05, '#e8c040', '#2c8a4a'), 4, 2, 0.115, 0.055, 0.2, 0.3, '#e8c040', 0.5),
    ('lentejas', 'Paquetes de lentejas', u_caja(0.1, 0.18, 0.06, '#8a5a2a', '#f4f0e0'), 4, 2, 0.105, 0.065, 0.18, 0.3, '#8a5a2a', 0.5),
    ('garbanzos_seco', 'Paquetes de garbanzos', u_caja(0.1, 0.18, 0.06, '#d8b870', '#3a8a3a'), 4, 2, 0.105, 0.065, 0.18, 0.3, '#d8b870', 0.5),
    ('harina', 'Paquetes de harina', u_caja(0.1, 0.2, 0.07, '#f4f0e0', '#2c5aa0'), 4, 2, 0.105, 0.075, 0.2, 0.3, '#f4f0e0', 1.0),
    ('azucar', 'Paquetes de azúcar', u_caja(0.1, 0.18, 0.07, '#f4f4f0', '#c0302a'), 4, 2, 0.105, 0.075, 0.18, 0.3, '#f4f4f0', 1.0),
    ('sal', 'Botes de sal', u_bote(0.04, 0.14, '#2c5aa0', '#f4f4f0'), 4, 2, 0.085, 0.085, 0.14, 0.3, '#2c5aa0', 0.75),
    ('cafe_molido', 'Paquetes de café molido', u_caja(0.08, 0.14, 0.06, '#6b4426', '#e0a020'), 5, 2, 0.085, 0.065, 0.14, 0.3, '#6b4426', 0.25),
    ('infusiones', 'Cajas de infusiones', u_caja(0.07, 0.12, 0.06, '#4a8a4a', '#f2d060'), 5, 2, 0.075, 0.065, 0.12, 0.3, '#4a8a4a', 0.1),
    ('galletas_maria', 'Paquetes de galletas María', u_caja(0.1, 0.22, 0.06, '#e0b050', '#c0302a'), 4, 2, 0.105, 0.065, 0.22, 0.3, '#e0b050', 0.4),
    ('galletas_chocolate', 'Paquetes de galletas de chocolate', u_caja(0.1, 0.22, 0.06, '#6b3a1a', '#f2e0b0'), 4, 2, 0.105, 0.065, 0.22, 0.3, '#6b3a1a', 0.4),
    ('galletas_crackers', 'Paquetes de galletas saladas', u_caja(0.1, 0.22, 0.06, '#d8c8a8', '#2c5aa0'), 4, 2, 0.105, 0.065, 0.22, 0.3, '#d8c8a8', 0.3),
    ('cereales_a', 'Cajas de cereales de miel', u_caja(0.2, 0.3, 0.07, '#e0782a', '#f2d060'), 2, 2, 0.21, 0.075, 0.3, 0.3, '#e0782a', 0.4),
    ('cereales_b', 'Cajas de cereales de chocolate', u_caja(0.2, 0.3, 0.07, '#5a3a2a', '#e0a020'), 2, 2, 0.21, 0.075, 0.3, 0.3, '#5a3a2a', 0.4),
    ('cereales_c', 'Cajas de copos de maíz', u_caja(0.2, 0.3, 0.07, '#3a8a3a', '#f2d060'), 2, 2, 0.21, 0.075, 0.3, 0.3, '#3a8a3a', 0.4),
    ('pan_molde', 'Bolsas de pan de molde', u_bolsa(0.12, 0.2, 0.22, '#f2e0b0', '#c0302a'), 3, 1, 0.13, 0.23, 0.2, 0.3, '#f2e0b0', 0.55),
    ('snack_patatas', 'Bolsas de patatas fritas', u_bolsa(0.18, 0.26, 0.06, '#e0a020', '#c0302a'), 2, 2, 0.19, 0.065, 0.26, 0.3, '#e0a020', 0.15),
    ('snack_aperitivos', 'Bolsas de aperitivos', u_bolsa(0.18, 0.26, 0.06, '#c0302a', '#f2d060'), 2, 2, 0.19, 0.065, 0.26, 0.3, '#c0302a', 0.15),
]
for k, n_, unit, nx, nz, dx, dz, h, fondo, c, mu in SECO:
    regis('prod_' + k, n_, 'alimento', unit, nx, nz, dx, dz, h, fondo, c, mu)
SWEETS = [
    ('chocolate_tabletas', 'Tabletas de chocolate con almendras', u_caja(0.08, 0.17, 0.012, '#4a2a1a', '#d8b040'), 5, 6, 0.085, 0.016, 0.17, 0.3, '#4a2a1a', 0.1),
    ('magdalenas', 'Bolsas de magdalenas', u_bolsa(0.2, 0.12, 0.1, '#f2d880', '#c0302a'), 1, 3, 0.21, 0.11, 0.12, 0.32, '#f2d880', 0.4),
    ('perrunillas', 'Cajas de perrunillas', u_caja(0.16, 0.08, 0.1, '#e8d8a8', '#a06a30'), 2, 3, 0.17, 0.11, 0.08, 0.33, '#e8d8a8', 0.35),
    ('chicles', 'Cajitas de chicles', u_caja(0.05, 0.08, 0.025, '#3a9ad0', '#f4f4f0'), 6, 4, 0.055, 0.03, 0.08, 0.12, '#3a9ad0', 0.03),
    ('caramelos', 'Bolsas de caramelos', u_bolsa(0.12, 0.18, 0.05, '#e0584a', '#f2d060'), 3, 3, 0.13, 0.055, 0.18, 0.3, '#e0584a', 0.2),
]
for k, n_, unit, nx, nz, dx, dz, h, fondo, c, mu in SWEETS:
    regis('prod_' + k, n_, 'alimento', unit, nx, nz, dx, dz, h, fondo, c, mu)
BEBIDAS = [
    ('agua_15', 'Botellas de agua de litro y medio', u_botella(0.045, 0.3, '#d8ecf4', '#2c6ab0', '#2c6ab0'), 3, 1, 0.095, 0.1, 0.3, 0.3, '#d8ecf4', 1.6),
    ('agua_gas', 'Botellas de agua con gas', u_botella(0.03, 0.2, '#e4f0e8', '#3a8a3a', '#3a8a3a'), 5, 2, 0.065, 0.065, 0.2, 0.3, '#e4f0e8', 0.55),
    ('cola_15', 'Botellas de refresco de cola', u_botella(0.042, 0.29, '#3a1c14', '#c0302a', '#c0302a'), 3, 1, 0.09, 0.09, 0.29, 0.3, '#3a1c14', 1.6),
    ('naranja_15', 'Botellas de refresco de naranja', u_botella(0.042, 0.29, '#f08a20', '#2c5aa0', '#f08a20'), 3, 1, 0.09, 0.09, 0.29, 0.3, '#f08a20', 1.6),
    ('limon_15', 'Botellas de refresco de limón', u_botella(0.042, 0.29, '#d8e84a', '#3a8a3a', '#3a8a3a'), 3, 1, 0.09, 0.09, 0.29, 0.3, '#d8e84a', 1.6),
    ('cerveza_pack', 'Packs de seis latas de cerveza', u_caja(0.2, 0.12, 0.14, '#e8c040', '#c0302a', m='metal'), 2, 2, 0.21, 0.15, 0.12, 0.31, '#e8c040', 2.3),
    ('vino_tinto', 'Botellas de vino tinto', u_botella(0.037, 0.3, '#3a1a24', '#e8e0d0', '#c8a040'), 4, 1, 0.08, 0.08, 0.3, 0.3, '#3a1a24', 1.3),
    ('vino_blanco', 'Botellas de vino blanco', u_botella(0.037, 0.3, '#a8b860', '#e8e0d0', '#c8a040'), 4, 1, 0.08, 0.08, 0.3, 0.3, '#a8b860', 1.3),
    ('vino_rosado', 'Botellas de vino rosado', u_botella(0.037, 0.3, '#d8788a', '#e8e0d0', '#c8a040'), 4, 1, 0.08, 0.08, 0.3, 0.3, '#d8788a', 1.3),
    ('zumo_naranja', 'Briks de zumo de naranja', u_caja(0.07, 0.2, 0.07, '#f08a20', '#3a8a3a'), 4, 2, 0.075, 0.075, 0.2, 0.3, '#f08a20', 1.1),
    ('zumo_melocoton', 'Briks de zumo de melocotón', u_caja(0.07, 0.2, 0.07, '#f2b070', '#c0302a'), 4, 2, 0.075, 0.075, 0.2, 0.3, '#f2b070', 1.1),
    ('leche_entera', 'Briks de leche entera', u_caja(0.07, 0.2, 0.07, '#f4f4f0', '#2c5aa0'), 5, 2, 0.075, 0.075, 0.2, 0.3, '#f4f4f0', 1.1),
    ('leche_semi', 'Briks de leche semidesnatada', u_caja(0.07, 0.2, 0.07, '#f4f4f0', '#3a8a3a'), 5, 2, 0.075, 0.075, 0.2, 0.3, '#f4f4f0', 1.1),
    ('leche_desnatada', 'Briks de leche desnatada', u_caja(0.07, 0.2, 0.07, '#f4f4f0', '#e0a020'), 5, 2, 0.075, 0.075, 0.2, 0.3, '#f4f4f0', 1.1),
]
for k, n_, unit, nx, nz, dx, dz, h, fondo, c, mu in BEBIDAS:
    regis('prod_' + k, n_, 'comercio_bebida', unit, nx, nz, dx, dz, h, fondo, c, mu)
LIMPIEZA = [
    ('detergente_liquido', 'Garrafas de detergente líquido', u_caja(0.17, 0.27, 0.1, '#2c8ad0', '#f4f4f0', m='plastico'), 2, 2, 0.18, 0.11, 0.27, 0.3, '#2c8ad0', 3.2),
    ('detergente_polvo', 'Cajas de detergente en polvo', u_caja(0.22, 0.3, 0.12, '#2c5aa0', '#e0782a'), 2, 2, 0.23, 0.13, 0.3, 0.3, '#2c5aa0', 3.0),
    ('suavizante', 'Botellas de suavizante', u_botella(0.045, 0.28, '#e8a0c0', '#f4f4f0', '#d86a8a'), 3, 1, 0.1, 0.1, 0.28, 0.3, '#e8a0c0', 1.5),
    ('lavavajillas', 'Botellas de lavavajillas', u_botella(0.04, 0.25, '#e8d84a', '#3a8a3a', '#3a8a3a'), 4, 2, 0.085, 0.085, 0.25, 0.3, '#e8d84a', 0.8),
    ('lejia', 'Botellas de lejía', u_botella(0.05, 0.3, '#f4f4f0', '#2c5aa0', '#2c5aa0'), 3, 1, 0.11, 0.11, 0.3, 0.3, '#f4f4f0', 2.1),
    ('limpiacristales', 'Pulverizadores limpiacristales', u_botella(0.04, 0.27, '#7ac0e8', '#f4f4f0', '#c0302a'), 4, 1, 0.085, 0.085, 0.27, 0.3, '#7ac0e8', 0.8),
    ('fregasuelos', 'Botellas de fregasuelos', u_botella(0.045, 0.28, '#7ac07a', '#f4f4f0', '#2f8a4a'), 3, 1, 0.1, 0.1, 0.28, 0.3, '#7ac07a', 1.5),
    ('papel_higienico', 'Paquetes de doce rollos de papel higiénico', u_caja(0.34, 0.2, 0.2, '#f4f4f0', '#7ac0e8', m='plastico'), 1, 1, 0.34, 0.2, 0.2, 0.3, '#f4f4f0', 1.8),
    ('papel_cocina', 'Paquetes de papel de cocina', u_caja(0.28, 0.28, 0.12, '#f4f4f0', '#e0a020', m='plastico'), 1, 2, 0.28, 0.13, 0.28, 0.3, '#f4f4f0', 1.2),
    ('servilletas', 'Paquetes de servilletas', u_caja(0.15, 0.1, 0.15, '#f4f4f0', '#c0302a', m='plastico'), 2, 2, 0.16, 0.16, 0.1, 0.32, '#f4f4f0', 0.4),
    ('bolsas_basura', 'Rollos de bolsas de basura', u_caja(0.15, 0.1, 0.07, '#3a3a3e', '#7ac0e8', m='plastico'), 2, 3, 0.16, 0.075, 0.1, 0.3, '#3a3a3e', 0.35),
    ('gel_ducha', 'Botes de gel de ducha', u_botella(0.04, 0.25, '#5a9ad0', '#f4f4f0', '#2c5aa0'), 4, 1, 0.085, 0.085, 0.25, 0.3, '#5a9ad0', 0.85),
    ('champu_super', 'Botes de champú', u_botella(0.04, 0.25, '#6ab08a', '#f4f4f0', '#2f8a4a'), 4, 1, 0.085, 0.085, 0.25, 0.3, '#6ab08a', 0.85),
    ('dentifrico', 'Tubos de dentífrico', u_caja(0.045, 0.18, 0.035, '#2c8ad0', '#f4f4f0'), 6, 2, 0.05, 0.04, 0.18, 0.3, '#2c8ad0', 0.15),
    ('compresas', 'Paquetes de compresas', u_caja(0.12, 0.2, 0.07, '#e8a0c0', '#f4f4f0', m='plastico'), 3, 2, 0.13, 0.075, 0.2, 0.3, '#e8a0c0', 0.3),
    ('esponjas', 'Paquetes de estropajos', u_caja(0.1, 0.14, 0.05, '#f2d84a', '#3a8a3a', m='plastico'), 4, 3, 0.105, 0.055, 0.14, 0.3, '#f2d84a', 0.15),
]
for k, n_, unit, nx, nz, dx, dz, h, fondo, c, mu in LIMPIEZA:
    regis('prod_' + k, n_, 'comercio_hogar', unit, nx, nz, dx, dz, h, fondo, c, mu)
# the fridges (deeper shelves: 0.55 of stock)
FRESCO = [
    ('yogur_natural', 'Packs de yogur natural', u_pack('#f4f4f0', '#2c5aa0'), 3, 2, 0.13, 0.13, 0.07, 0.52, '#f4f4f0', 0.5, 'alimento'),
    ('yogur_fresa', 'Packs de yogur de fresa', u_pack('#e8a0b0', '#c0302a'), 3, 2, 0.13, 0.13, 0.07, 0.52, '#e8a0b0', 0.5, 'alimento'),
    ('yogur_limon', 'Packs de yogur de limón', u_pack('#f2e880', '#e0a020'), 3, 2, 0.13, 0.13, 0.07, 0.52, '#f2e880', 0.5, 'alimento'),
    ('mantequilla', 'Pastillas de mantequilla', u_caja(0.1, 0.04, 0.06, '#f2e080', '#e0a020'), 3, 4, 0.11, 0.065, 0.04, 0.52, '#f2e080', 0.25, 'alimento'),
    ('queso_lonchas', 'Paquetes de queso en lonchas', u_caja(0.12, 0.2, 0.02, '#f2c850', '#c0302a'), 4, 6, 0.13, 0.025, 0.2, 0.52, '#f2c850', 0.15, 'alimento'),
    ('huevos', 'Cartones de huevos', u_caja(0.3, 0.07, 0.1, '#d8c8a0', '#b8a070'), 1, 5, 0.31, 0.105, 0.07, 0.52, '#d8c8a0', 0.7, 'alimento'),
    ('nata', 'Briks de nata', u_caja(0.05, 0.1, 0.05, '#f4f4f0', '#c0302a'), 6, 4, 0.055, 0.055, 0.1, 0.52, '#f4f4f0', 0.2, 'alimento'),
    ('zumo_fresco', 'Botellas de zumo recién exprimido', u_botella(0.04, 0.25, '#f08a20', '#f4f4f0', '#3a8a3a'), 4, 2, 0.085, 0.085, 0.25, 0.52, '#f08a20', 0.5, 'comercio_bebida'),
    ('bandeja_carne', 'Bandejas de carne picada', u_caja(0.24, 0.03, 0.18, '#c04a4a', '#f4f4f0', m='plastico'), 1, 3, 0.25, 0.19, 0.03, 0.57, '#c04a4a', 0.5, 'alimento'),
    ('bandeja_pollo', 'Bandejas de pollo', u_caja(0.24, 0.04, 0.18, '#e8b870', '#f4f4f0', m='plastico'), 1, 3, 0.25, 0.19, 0.04, 0.57, '#e8b870', 0.6, 'alimento'),
    ('fiambre_loncheado', 'Paquetes de jamón cocido', u_caja(0.14, 0.02, 0.2, '#e8a0a0', '#f4f4f0', m='plastico'), 3, 2, 0.15, 0.21, 0.02, 0.5, '#e8a0a0', 0.15, 'alimento'),
    ('quesito_untable', 'Tarrinas de queso untable', u_bote(0.04, 0.06, '#f4f4f0', '#2a8a9a'), 4, 3, 0.085, 0.085, 0.06, 0.52, '#f4f4f0', 0.2, 'alimento'),
]
for k, n_, unit, nx, nz, dx, dz, h, fondo, c, mu, cat in FRESCO:
    regis('prod_' + k, n_, cat, unit, nx, nz, dx, dz, h, fondo, c, mu)
FRIAS = [
    ('agua_fria', 'Botellas de agua fresquita', u_botella(0.045, 0.3, '#d8ecf4', '#2c6ab0', '#2c6ab0'), 3, 2, 0.095, 0.095, 0.3, 0.55, '#d8ecf4', 1.6),
    ('naranja_fria', 'Botellas de refresco de naranja bien frío', u_botella(0.04, 0.28, '#f08a20', '#2c5aa0', '#f08a20'), 3, 2, 0.09, 0.09, 0.28, 0.55, '#f08a20', 1.5),
    ('zumo_frio', 'Botellas de zumo de melocotón', u_botella(0.04, 0.26, '#f2b070', '#f4f4f0', '#c0302a'), 3, 2, 0.09, 0.09, 0.26, 0.55, '#f2b070', 1.2),
    ('cola_fria', 'Latas de cola', u_lata(0.033, 0.12, '#3a1c14', '#c0302a'), 5, 3, 0.07, 0.07, 0.12, 0.5, '#3a1c14', 0.4),
    ('cerveza_fria', 'Latas de cerveza', u_lata(0.033, 0.12, '#e8c040', '#c0302a'), 5, 3, 0.07, 0.07, 0.12, 0.5, '#e8c040', 0.4),
    ('isotonica_fria', 'Botellas de bebida isotónica', u_botella(0.035, 0.24, '#2a9ad0', '#f4f4f0', '#2c5aa0'), 4, 2, 0.078, 0.078, 0.24, 0.55, '#2a9ad0', 0.9),
]
for k, n_, unit, nx, nz, dx, dz, h, fondo, c, mu in FRIAS:
    regis('prod_' + k, n_, 'comercio_bebida', unit, nx, nz, dx, dz, h, fondo, c, mu)
# the breads (lying along the rack's depth)
def u_barra(c):
    def f(x, z):
        return [cil(0.028, 0.028, 0.42, x=x, y=0.028, z=z, c=c, m='comida', r=[90, 0, 0], seg=7)]
    return f
def u_hogaza(c):
    def f(x, z):
        return [esf(0.1, x, 0.06, z, c=c, m='comida', s=[1, 0.6, 1])]
    return f
regis('prod_baguettes', 'Barras de pan', 'alimento', u_barra('#d8a050'), 7, 1, 0.07, 0.42, 0.06, 0.42, '#d8a050', 0.25, mat='comida')
regis('prod_hogazas', 'Hogazas de pan de pueblo', 'alimento', u_hogaza('#c88a40'), 3, 2, 0.21, 0.21, 0.12, 0.42, '#c88a40', 0.5, mat='comida')
regis('prod_bollos', 'Bolsas de bollos', 'alimento', u_bolsa(0.2, 0.14, 0.2, '#f2d880', '#a06a30'), 2, 2, 0.21, 0.21, 0.14, 0.42, '#f2d880', 0.4)
regis('prod_pan_molde_artesano', 'Panes de molde artesanos', 'alimento', u_caja(0.12, 0.12, 0.22, '#d8a050', '#a06a30', m='comida'), 3, 2, 0.13, 0.22, 0.12, 0.44, '#d8a050', 0.5, mat='comida')
# crates of fruit and vegetables: a green crate, the produce heaped on top
def cajon(id, nombre, col, r, n, forma='esfera', sy=1.0, masa=9.0, c2=None):
    P = [caja(0.5, 0.16, 0.34, y=0.08, c='#b88a58', m='madera'), caja(0.52, 0.02, 0.36, y=0.15, c='#9a7040', m='madera'), esf(1.0, 0, 0.16, 0, c=col, m='comida', s=[0.23, 0.07, 0.15])]
    pos = [(-0.15, -0.05), (-0.05, 0.06), (0.05, -0.06), (0.15, 0.05), (-0.1, 0.0), (0.1, 0.0)][:n]
    for i, (x, z) in enumerate(pos):
        c = col if not c2 or i % 2 else c2
        if forma == 'esfera': P.append(esf(r, x, 0.2 + r * sy * 0.6, z, c=c, m='comida', s=[1, sy, 1]))
        elif forma == 'barra': P.append(cil(r, r, 0.22, x=x, y=0.2 + r, z=z, c=c, m='comida', r=[0, 0, 90], seg=7))
        elif forma == 'cono': P.append({**cono(r, 0.16, x=x, y=0.2 + r, z=z, c=c, m='comida', seg=7), 'r': [0, 0, 90]})
        else: P.append(caja(r * 2, r * 2, r * 2, x=x, y=0.2 + r, z=z, c=c, m='comida'))
    obj(id, nombre, 'alimento', 'CARRY', masa, 'comida', 'superficie', P)
for k, (n_, col, r, n, forma, sy, c2) in {
        'melocotones': ('Cajón de melocotones', '#f0a060', 0.042, 5, 'esfera', 1.0, '#e87848'), 'melones': ('Cajón de melones', '#7aa050', 0.12, 2, 'esfera', 0.9, '#a8c070'),
        'naranjas': ('Cajón de naranjas', '#f08a20', 0.045, 6, 'esfera', 1.0, None), 'manzanas_rojas': ('Cajón de manzanas rojas', '#c0302a', 0.04, 6, 'esfera', 1.0, None),
        'manzanas_verdes': ('Cajón de manzanas verdes', '#9ab83a', 0.04, 6, 'esfera', 1.0, None), 'limones': ('Cajón de limones', '#f2e04a', 0.035, 6, 'esfera', 0.8, None),
        'tomates': ('Cajón de tomates', '#d8382a', 0.04, 6, 'esfera', 0.9, None), 'cebollas': ('Cajón de cebollas', '#d8a060', 0.045, 5, 'esfera', 0.9, None),
        'patatas': ('Cajón de patatas', '#a8825a', 0.05, 5, 'esfera', 0.7, '#8a6a46'), 'lechugas': ('Cajón de lechugas', '#7ac040', 0.09, 3, 'esfera', 0.9, '#5aa030'),
        'pimientos': ('Cajón de pimientos', '#c0302a', 0.035, 6, 'caja', 1.0, '#3a8a3a'), 'zanahorias': ('Cajón de zanahorias', '#e0782a', 0.025, 6, 'cono', 1.0, None),
        'platanos': ('Cajón de plátanos', '#f2d040', 0.022, 6, 'barra', 1.0, '#e8c030'), 'uvas': ('Cajón de uvas', '#8a4a9a', 0.022, 6, 'esfera', 1.0, '#a8c860')}.items():
    cajon('prod_fruta_' + k, n_, col, r, n, forma, sy, 9.0, c2)

if __name__ == '__main__':
    json.dump({'version': 1, 'familia': 'comercio', 'categorias': CATEGORIAS, 'objetos': OUT}, open(os.path.join(ROOT, 'data', 'objetos', 'comercio.json'), 'w'), ensure_ascii=False, indent=1)
    print('objetos de comercio:', len(OUT))
