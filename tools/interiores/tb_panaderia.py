# The bakery-confectionery's objects (family «tiendas_b»): the glass counter, the bread shelves, the back counter with its
# slicer, tables with baskets, the Extremaduran sweets' rack, the obrador (oven, kneader, sheeter, trolleys) — and the goods:
# some twenty breads, twenty pastries, a dozen cakes, a dozen traditional sweets. Ids start with «pan_». Plain colours, no brands.
from tb_base import *

MIGA, DORADO, TOSTADO, CHOCO = '#e8d4a8', '#d89a48', '#b8742e', '#4a2a1a'
MADERA_P = '#a8825a'

# ---- the glass counter module (1.2 m): a cabinet, a glass case with two shelves, a wooden top for the till
def vitrina_modulo(id, nombre, cuerpo, frente):
    P = [caja(1.2, 0.5, 0.66, y=0.25, z=-0.02, c=cuerpo), caja(1.2, 0.07, 0.7, y=0.035, z=-0.02, c=oscuro(cuerpo, 0.5)), caja(1.12, 0.38, 0.012, y=0.27, z=0.31, c=frente),
         caja(1.16, 0.012, 0.62, y=0.506, z=0.0, c='#f4efe4'), caja(1.12, 0.012, 0.5, y=0.82, z=0.0, c=GLASS, m='cristal'),
         caja(1.2, 0.02, 0.7, y=1.13, z=-0.02, c=MADERA_P), caja(1.2, 0.58, 0.012, y=0.82, z=0.33, c=GLASS, m='cristal', r=[-8, 0, 0]), caja(1.2, 0.5, 0.012, y=0.8, z=-0.35, c=GLASS, m='cristal'),
         caja(0.012, 0.58, 0.64, x=-0.594, y=0.8, z=-0.01, c=GLASS, m='cristal'), caja(0.012, 0.58, 0.64, x=0.594, y=0.8, z=-0.01, c=GLASS, m='cristal'),
         caja(1.2, 0.02, 0.02, y=0.53, z=0.34, c=STEEL, m='metal')]
    obj(id, nombre, 'mostrador', 'FIXED', 170, 'cristal', 'suelo', P, motivo_fijo='estructural', superficies=[sup(0.512, 0.08), sup(0.826, 0.08)], nota='mostrador de cristal: dos baldas dentro, con la tapa de madera cerrada')
vitrina_modulo('pan_vitrina_modulo', 'Mostrador vitrina de pastelería (1,2 m)', '#e9dfcb', '#7a4a2a')
vitrina_modulo('pan_vitrina_modulo_verde', 'Mostrador vitrina de pastelería, verde (1,2 m)', '#dfe8d8', '#3a6a4a')

# ---- shelving: wooden, with deep shelves for loaves; the back counter; table with baskets; the rack of traditional sweets
estantes('pan_estanteria_pan', 'Estantería de madera para el pan (1,2 m)', 1.2, 0.46, [0.45, 0.85, 1.25, 1.65, 2.05], 2.2, c='#a8825a', cp='#c8a06a', masa=60, nota='baldas de 43 cm para barras y hogazas')
estantes('pan_estante_dulces', 'Expositor de dulces típicos (0,9 m)', 0.9, 0.34, [0.4, 0.78, 1.16, 1.54], 1.75, c='#8a5a36', cp='#c8a06a', masa=36)
estantes('pan_estante_pared', 'Estante de pared para galletas y cajas', 1.0, 0.36, [1.1, 1.5, 1.9], 2.0, c='#8a5a36', cp='#c8a06a', masa=25, soporte='pared', nota='colgado de la pared, sobre el mueble trasero', zocalo=False)
obj('pan_mueble_trasero', 'Mueble trasero con la caja y la cortadora (1,2 m)', 'mostrador', 'FIXED', 120, 'madera', 'suelo', [
    caja(1.2, 0.9, 0.6, y=0.45, z=0.0, c='#e9dfcb'), caja(1.22, 0.05, 0.64, y=0.925, z=0.0, c='#d2d6d8', m='metal'), caja(1.14, 0.5, 0.012, y=0.5, z=0.306, c='#7a4a2a'), caja(1.2, 0.08, 0.012, y=0.04, z=0.306, c=DARK)],
    motivo_fijo='estructural', superficies=[sup(0.95, 0.04)], nota='tras el mostrador: la cortadora de pan, la cafetera y la caja')
obj('pan_mesa_pan', 'Mesa expositora de pan con cestos (1,2 m)', 'mesa', 'PUSH', 38, 'madera', 'suelo', [
    caja(1.2, 0.05, 0.8, y=0.775, c=MADERA_P)] + [caja(0.05, 0.75, 0.05, x=sx * 0.55, y=0.375, z=sz * 0.35, c='#5a3a20') for sx in (-1, 1) for sz in (-1, 1)] + [caja(1.1, 0.03, 0.7, y=0.25, c='#8a6a40')],
    superficies=[sup(0.8, 0.05), sup(0.265, 0.05)])
obj('pan_cortadora_pan', 'Cortadora de pan eléctrica', 'pequeño_electrodomestico', 'CARRY', 16, 'metal', 'superficie', [
    caja(0.46, 0.1, 0.48, y=0.05, c='#c3c7ca', m='metal'), caja(0.4, 0.55, 0.26, y=0.375, z=-0.09, c='#d8dde0', m='metal'), caja(0.34, 0.3, 0.012, y=0.4, z=0.05, c=GLASS, m='cristal'),
    caja(0.28, 0.04, 0.02, y=0.28, z=0.06, c=STEEL, m='metal'), caja(0.14, 0.05, 0.05, x=0.14, y=0.62, z=-0.09, c='#c0392b', m='plastico'), caja(0.3, 0.02, 0.18, x=0.0, y=0.11, z=0.15, c='#9aa0a4', m='metal')],
    nota='para cortar las barras y las hogazas en el momento')
obj('pan_rotulo', 'Rótulo interior de la panadería', 'decoracion', 'PICKUP', 3, 'madera', 'pared', [
    caja(1.3, 0.34, 0.03, y=2.55, z=0.015, c='#3a2a1c'), plano(1.24, 0.28, y=2.55, z=0.033, tex={'tipo': 'rotulo_tb', 'estilo': 'panaderia', 'rotulo_local': True})])
obj('pan_pizarra_precios', 'Pizarra de precios del pan y los dulces', 'decoracion', 'PICKUP', 3, 'madera', 'pared', [
    caja(0.9, 0.62, 0.03, y=1.75, z=0.015, c='#5a3a20'), plano(0.84, 0.56, y=1.75, z=0.033, tex={'tipo': 'pizarra', 'lineas': ['Barra de pan  0,75', 'Hogaza  1,90', 'Mollete  0,35', 'Perrunillas  4,80', 'Magdalenas  2,60', 'Tarta queso  14,00']})])
obj('pan_cartel_pan', 'Cartel del pan de leña', 'cuadro', 'PICKUP', 1.2, 'papel', 'pared', [
    caja(0.5, 0.7, 0.025, y=1.7, z=0.0125, c='#2a2420'), plano(0.44, 0.64, y=1.7, z=0.027, tex={'tipo': 'cartel_tb', 'dibujo': 'pan'})])
obj('pan_cartel_tarta', 'Cartel de tartas por encargo', 'cuadro', 'PICKUP', 1.2, 'papel', 'pared', [
    caja(0.5, 0.7, 0.025, y=1.7, z=0.0125, c='#2a2420'), plano(0.44, 0.64, y=1.7, z=0.027, tex={'tipo': 'cartel_tb', 'dibujo': 'tarta'})])
obj('pan_pala_horno_pared', 'Pala de horno de madera colgada', 'decoracion', 'PICKUP', 2, 'madera', 'pared', [
    caja(0.32, 0.02, 0.4, y=1.9, z=0.04, c='#c8a06a', m='madera', r=[90, 0, 0]), caja(0.04, 1.0, 0.02, y=1.35, z=0.04, c='#a8825a', m='madera')], nota='la pala con la que se mete el pan al horno de leña')
obj('pan_cesta_colgante', 'Cestas de mimbre colgadas de la pared', 'decoracion', 'PICKUP', 2.4, 'madera', 'pared', [
    cil(0.15, 0.1, 0.1, x=-0.25, y=1.9, z=0.15, c='#c8a878', m='madera', seg=12), cil(0.15, 0.1, 0.1, x=0.25, y=1.7, z=0.15, c='#c8a878', m='madera', seg=12), caja(0.7, 0.02, 0.02, y=1.98, z=0.02, c='#5a3a20')])
obj('pan_caja_tarta', 'Cajas de pastelería apiladas', 'papel', 'PICKUP', 1.2, 'papel', 'superficie', [
    caja(0.3, 0.1, 0.3, y=0.05, c='#f2e8d4', m='papel'), caja(0.3, 0.1, 0.3, y=0.15, c='#e8c0c8', m='papel'), caja(0.3, 0.02, 0.3, y=0.21, c='#7a4a2a', m='papel'), caja(0.31, 0.012, 0.03, y=0.19, z=0.0, c='#c0302a', m='tela')])
obj('pan_cinta_envolver', 'Rollo de papel de envolver y cinta', 'papel', 'PICKUP', 0.5, 'papel', 'superficie', [
    cil(0.05, 0.05, 0.3, y=0.05, c='#f2e8d4', m='papel', r=[0, 0, 90], seg=8), caja(0.04, 0.1, 0.1, x=-0.18, y=0.05, c=STEEL, m='metal'), caja(0.04, 0.1, 0.1, x=0.18, y=0.05, c=STEEL, m='metal')])

# ---- bread (facings of 40 cm along the shelf): shapes made of cylinders and flattened spheres
def u_barra(c, r=0.03, l=0.4, raya='#f0d9a0'):
    def f(x, z): return [cil(r, r, l, x=x, y=r, z=z, c=c, m='comida', r=[90, 0, 0], seg=8), caja(r * 1.2, 0.006, l * 0.7, x=x, y=r * 1.85, z=z, c=raya, m='comida')]
    return f
def u_hogaza(c, r=0.12, h=0.55):
    def f(x, z): return [esf(r, x, r * h, z, c=c, m='comida', s=[1, h, 1]), esf(r * 0.5, x, r * h * 1.55, z, c=claro(c, 0.2), m='comida', s=[1, 0.35, 1])]
    return f
def u_rosca(c, r=0.09):
    def f(x, z): return [cil(r, r, 0.05, x=x, y=0.025, z=z, c=c, m='comida', seg=12), cil(r * 0.35, r * 0.35, 0.052, x=x, y=0.026, z=z, c=oscuro(c, 0.55), m='comida', seg=8)]
    return f
def u_ovalo(c, rx=0.07, rz=0.055, h=0.5):
    def f(x, z): return [esf(1.0, x, rx * h, z, c=c, m='comida', s=[rx, rx * h, rz])]
    return f
def u_caja_pan(c, w, h, d, c2=None):
    def f(x, z): return [caja(w, h, d, x=x, y=h / 2, z=z, c=c, m='comida')] + ([caja(w * 0.96, h * 0.25, d * 0.96, x=x, y=h * 0.95, z=z, c=c2, m='comida')] if c2 else [])
    return f
def u_bolsa_pan(c, c2, w=0.1, h=0.2, d=0.06):
    def f(x, z): return [caja(w, h, d, x=x, y=h / 2, z=z, c=c, m='papel'), caja(w * 0.9, h * 0.22, d + 0.002, x=x, y=h * 0.7, z=z, c=c2, m='papel'), caja(w * 0.8, 0.02, d * 0.5, x=x, y=h + 0.01, z=z, c=c, m='papel')]
    return f
PANES = [
    ('barra_pueblo', 'Barras de pan de pueblo', u_barra('#d89a48'), 7, 1, 0.062, 0.4, 0.07, '#d89a48', 0.25),
    ('barra_integral', 'Barras de pan integral', u_barra('#9a6a3a', raya='#c8a070'), 7, 1, 0.062, 0.4, 0.07, '#9a6a3a', 0.25),
    ('barra_candeal', 'Barras de pan candeal', u_barra('#e6c078', raya='#f4e0b0'), 7, 1, 0.062, 0.4, 0.07, '#e6c078', 0.25),
    ('barra_centeno', 'Barras de pan de centeno', u_barra('#7a5a40', raya='#a8825a'), 7, 1, 0.062, 0.4, 0.07, '#7a5a40', 0.25),
    ('barra_semillas', 'Barras de pan de semillas', u_barra('#c89048', raya='#efe2c0'), 7, 1, 0.062, 0.4, 0.07, '#c89048', 0.25),
    ('baguette', 'Baguettes largas', u_barra('#e0a858', r=0.027), 8, 1, 0.056, 0.42, 0.06, '#e0a858', 0.22),
    ('hogaza_lena', 'Hogazas de pan de leña', u_hogaza('#c88a40'), 3, 2, 0.26, 0.21, 0.13, '#c88a40', 0.9),
    ('hogaza_centeno', 'Hogazas de centeno', u_hogaza('#8a6a4a', 0.12, 0.5), 3, 2, 0.26, 0.21, 0.12, '#8a6a4a', 0.9),
    ('hogaza_integral', 'Hogazas integrales', u_hogaza('#a8784a', 0.11, 0.55), 3, 2, 0.24, 0.2, 0.12, '#a8784a', 0.8),
    ('hogaza_pasas', 'Hogazas de nueces y pasas', u_hogaza('#9a6a40', 0.11, 0.55), 3, 2, 0.24, 0.2, 0.12, '#9a6a40', 0.8),
    ('rosca', 'Roscas de pan', u_rosca('#d8a050'), 4, 2, 0.19, 0.2, 0.05, '#d8a050', 0.45),
    ('mollete', 'Molletes', u_ovalo('#e8c078', 0.075, 0.06, 0.45), 5, 3, 0.16, 0.13, 0.04, '#e8c078', 0.12),
    ('pistolas', 'Pistolas y panecillos', u_ovalo('#e0a858', 0.085, 0.045, 0.55), 5, 4, 0.18, 0.1, 0.05, '#e0a858', 0.1),
    ('chapata', 'Chapatas', u_caja_pan('#e8c078', 0.2, 0.05, 0.1), 3, 3, 0.21, 0.11, 0.05, '#e8c078', 0.2),
    ('pan_molde', 'Panes de molde', u_caja_pan('#e8c890', 0.12, 0.12, 0.25, '#c8883a'), 3, 1, 0.13, 0.26, 0.13, '#e8c890', 0.5),
    ('pan_leche', 'Panes de leche', u_ovalo('#f0d8a0', 0.07, 0.05, 0.5), 6, 3, 0.15, 0.11, 0.04, '#f0d8a0', 0.08),
    ('picos', 'Bolsas de picos', u_bolsa_pan('#e8d4a8', '#d89a48'), 4, 2, 0.11, 0.07, 0.2, '#e8d4a8', 0.25),
    ('colines', 'Bolsas de colines', u_bolsa_pan('#f2e8d0', '#7a4a2a', 0.08, 0.28, 0.05), 5, 2, 0.09, 0.06, 0.28, '#f2e8d0', 0.15),
    ('reganas', 'Bolsas de regañás', u_bolsa_pan('#efe2c0', '#3a6a4a'), 4, 2, 0.11, 0.07, 0.2, '#efe2c0', 0.2),
    ('pan_rallado', 'Bolsas de pan rallado', u_bolsa_pan('#e6c890', '#2c5aa0', 0.12, 0.18, 0.05), 4, 2, 0.13, 0.06, 0.18, '#e6c890', 0.3),
    ('tortas_aceite', 'Tortas de aceite en su papel', u_caja_pan('#e8d8b0', 0.18, 0.04, 0.18, '#d8c090'), 3, 2, 0.19, 0.19, 0.06, '#e8d8b0', 0.4),
]
for k, n_, unit, nx, nz, dx, dz, h, c, mu in PANES:
    regis('pan_pan_' + k, n_, 'alimento', unit, nx, nz, dx, dz, h, 0.42, c, mu, mat='comida')

# ---- pastries: a tray with six or eight of one kind; whole cakes on a plate
def bandeja(unit, n, cols=4, dx=0.085, dz=0.085, c='#f4efe4'):
    def f(x, z):
        P = [caja(0.32, 0.012, 0.24, x=x, y=0.006, z=z, c=c, m='metal')]
        for i in range(n): P += unit(x + (i % cols - (cols - 1) / 2) * dx, z + (i // cols - 0.5) * dz)
        return P
    return f
def o_croissant(c='#d89a48'):
    def f(x, z): return [esf(1.0, x, 0.024, z, c=c, m='comida', s=[0.052, 0.024, 0.028])]
    return f
def o_napolitana(c='#e0a858', choco=CHOCO):
    def f(x, z): return [caja(0.085, 0.032, 0.05, x=x, y=0.028, z=z, c=c, m='comida'), caja(0.08, 0.004, 0.012, x=x, y=0.046, z=z - 0.012, c=choco, m='comida'), caja(0.08, 0.004, 0.012, x=x, y=0.046, z=z + 0.012, c=choco, m='comida')]
    return f
def o_palmera(c='#d8964a'):
    def f(x, z): return [esf(1.0, x - 0.02, 0.022, z, c=c, m='comida', s=[0.03, 0.022, 0.034]), esf(1.0, x + 0.02, 0.022, z, c=claro(c, 0.15), m='comida', s=[0.03, 0.022, 0.034])]
    return f
def o_donut(c, glaseado):
    def f(x, z): return [cil(0.04, 0.04, 0.03, x=x, y=0.015, z=z, c=c, m='comida', seg=10), cil(0.04, 0.04, 0.006, x=x, y=0.033, z=z, c=glaseado, m='comida', seg=10), cil(0.012, 0.012, 0.042, x=x, y=0.021, z=z, c='#f4efe4', m='metal', seg=6)]
    return f
def o_cupcake(c, top):
    def f(x, z): return [cil(0.034, 0.024, 0.04, x=x, y=0.02, z=z, c=c, m='papel', seg=8), esf(0.036, x, 0.052, z, c=top, m='comida', s=[1, 0.8, 1])]
    return f
def o_barra_dulce(c, glaseado, l=0.12, r=0.018):
    def f(x, z): return [cil(r, r, l, x=x, y=r, z=z, c=c, m='comida', r=[0, 0, 90], seg=8), cil(r * 1.05, r * 1.05, l * 0.5, x=x, y=r, z=z, c=glaseado, m='comida', r=[0, 0, 90], seg=8)]
    return f
def o_cuadrado(c, c2, h=0.03, w=0.07):
    def f(x, z): return [caja(w, h, w, x=x, y=h / 2, z=z, c=c, m='comida'), caja(w * 0.9, 0.008, w * 0.9, x=x, y=h + 0.004, z=z, c=c2, m='comida')]
    return f
def o_tartaleta(c, fruta):
    def f(x, z): return [cil(0.038, 0.03, 0.022, x=x, y=0.011, z=z, c=c, m='comida', seg=10), esf(0.015, x - 0.012, 0.032, z, c=fruta, m='comida'), esf(0.015, x + 0.012, 0.032, z + 0.01, c=fruta, m='comida')]
    return f
def o_bola(c, r=0.022):
    def f(x, z): return [esf(r, x, r * 0.9, z, c=c, m='comida', s=[1, 0.9, 1])]
    return f
u_bola = o_bola
def o_ensaimada(c='#efd9a0'):
    def f(x, z): return [cil(0.04, 0.04, 0.03, x=x, y=0.015, z=z, c=c, m='comida', seg=10), cil(0.03, 0.03, 0.016, x=x, y=0.036, z=z, c='#f6f0e0', m='comida', seg=10), cil(0.012, 0.012, 0.012, x=x, y=0.048, z=z, c=c, m='comida', seg=8)]
    return f
BOLLERIA = [
    ('croissant', 'Croissants de mantequilla', o_croissant(), 8, 4, 0.085, 0.085, 0.052), ('croissant_almendra', 'Croissants de almendra', o_croissant('#c8863a'), 8, 4, 0.085, 0.085, 0.052),
    ('napolitana', 'Napolitanas de chocolate', o_napolitana(), 6, 3, 0.1, 0.07, 0.04), ('napolitana_crema', 'Napolitanas de crema', o_napolitana('#e8c078', '#f2e07a'), 6, 3, 0.1, 0.07, 0.04),
    ('palmera', 'Palmeras de hojaldre', o_palmera(), 8, 4, 0.08, 0.08, 0.045), ('palmera_choco', 'Palmeras bañadas en chocolate', o_palmera('#6a3a22'), 8, 4, 0.08, 0.08, 0.045),
    ('ensaimada', 'Ensaimadas', o_ensaimada(), 6, 3, 0.1, 0.1, 0.05), ('donut_rosa', 'Donuts de fresa', o_donut('#e0b070', '#e8a0b8'), 8, 4, 0.085, 0.085, 0.034),
    ('donut_choco', 'Donuts de chocolate', o_donut('#e0b070', '#5a3022'), 8, 4, 0.085, 0.085, 0.034), ('donut_azucar', 'Donuts de azúcar', o_donut('#e0b070', '#f6f0e0'), 8, 4, 0.085, 0.085, 0.034),
    ('magdalena', 'Magdalenas grandes', o_cupcake('#c89048', '#e8c078'), 8, 4, 0.085, 0.085, 0.07), ('muffin_choco', 'Muffins de chocolate', o_cupcake('#e8e0d0', '#5a3022'), 8, 4, 0.085, 0.085, 0.07),
    ('cana_crema', 'Cañas de crema', o_barra_dulce('#d8a050', '#f2e8c0'), 6, 3, 0.07, 0.07, 0.036), ('eclair', 'Petisús y éclairs', o_barra_dulce('#d8a050', '#5a3022', 0.1, 0.02), 6, 3, 0.07, 0.07, 0.04),
    ('milhojas', 'Milhojas de crema', o_cuadrado('#e0b868', '#f6f0e0', 0.05, 0.07), 6, 3, 0.09, 0.09, 0.054), ('tartaletas', 'Tartaletas de fruta', o_tartaleta('#d8a858', '#c0302a'), 8, 4, 0.085, 0.085, 0.045),
    ('bocados_hojaldre', 'Bocados de hojaldre con cabello de ángel', o_cuadrado('#d89a48', '#e8c050', 0.035, 0.065), 8, 4, 0.08, 0.08, 0.04), ('torrijas', 'Torrijas con canela', o_cuadrado('#c88a40', '#a8602a', 0.035, 0.075), 6, 3, 0.1, 0.09, 0.04),
    ('pestinos', 'Pestiños con miel', o_bola('#d89a48', 0.026), 8, 4, 0.075, 0.075, 0.03), ('rosquillas', 'Rosquillas fritas con azúcar', o_donut('#d8a050', '#f2efe6'), 8, 4, 0.085, 0.085, 0.034),
]
for k, n_, unit, nb, cols, dx, dz, h in BOLLERIA:
    regis('pan_bol_' + k, n_, 'tb_bolleria', bandeja(unit, nb, cols, dx, dz), 1, 1, 0.34, 0.26, h, 0.26, '#f4efe4', 0.8, mat='comida', hf=0.01)
def tarta(id, nombre, base, crema, deco, r=0.11, h=0.09):
    P = [cil(0.15, 0.15, 0.012, y=0.006, c='#f4efe4', m='ceramica', seg=16), cil(r, r, h, y=0.012 + h / 2, c=base, m='comida', seg=16), cil(r + 0.002, r + 0.002, 0.018, y=0.012 + h * 0.5, c=crema, m='comida', seg=16), cil(r * 0.98, r * 0.98, 0.012, y=0.012 + h + 0.006, c=crema, m='comida', seg=16)]
    top = 0.012 + h + 0.012
    for dx_, dz_, rr, c in deco: P.append(esf(rr, dx_ * r, top + rr * 0.6, dz_ * r, c=c, m='comida'))
    obj(id, nombre, 'tb_bolleria', 'PICKUP', 1.6, 'comida', 'superficie', P)
tarta('pan_tarta_queso', 'Tarta de queso con mermelada', '#e8d4a0', '#f2e6c0', [(0.0, 0.0, 0.03, '#a8203a'), (-0.5, 0.2, 0.02, '#a8203a'), (0.5, -0.3, 0.02, '#a8203a'), (0.2, 0.6, 0.02, '#a8203a')])
tarta('pan_tarta_chocolate', 'Tarta de chocolate', '#4a2a1a', '#5a3322', [(0.0, 0.0, 0.025, '#d8b070'), (0.55, 0.0, 0.02, '#d8b070'), (-0.55, 0.0, 0.02, '#d8b070'), (0.0, 0.55, 0.02, '#d8b070'), (0.0, -0.55, 0.02, '#d8b070')])
tarta('pan_tarta_manzana', 'Tarta de manzana', '#d8a050', '#c88a3a', [(0.0, 0.0, 0.03, '#e8c070'), (0.4, 0.4, 0.025, '#e8c070'), (-0.4, 0.4, 0.025, '#e8c070'), (-0.4, -0.4, 0.025, '#e8c070'), (0.4, -0.4, 0.025, '#e8c070')])
tarta('pan_tarta_santiago', 'Tarta de Santiago', '#e0b868', '#f2e6c8', [(0.0, 0.0, 0.03, '#f6f2e8')], h=0.06)
tarta('pan_tarta_fresas', 'Tarta de fresas con nata', '#f2e0c0', '#f6f0e4', [(0.0, 0.0, 0.026, '#c0302a'), (0.55, 0.0, 0.026, '#c0302a'), (-0.55, 0.0, 0.026, '#c0302a'), (0.0, 0.55, 0.026, '#c0302a'), (0.0, -0.55, 0.026, '#c0302a'), (0.39, 0.39, 0.026, '#c0302a'), (-0.39, -0.39, 0.026, '#c0302a')])
tarta('pan_tarta_tres_chocolates', 'Tarta de tres chocolates', '#6a4a30', '#f2e0c0', [(0.0, 0.0, 0.02, '#4a2a1a'), (0.5, 0.3, 0.02, '#4a2a1a'), (-0.5, -0.3, 0.02, '#4a2a1a')], h=0.1)
tarta('pan_tarta_limon', 'Tarta de limón con merengue', '#f2e07a', '#f6f0e0', [(0.0, 0.0, 0.035, '#f6f0e0'), (0.5, 0.3, 0.03, '#f6f0e0'), (-0.5, 0.3, 0.03, '#f6f0e0'), (0.0, -0.6, 0.03, '#f6f0e0')])
tarta('pan_tarta_cumple', 'Tarta de cumpleaños con velas', '#f2c0cc', '#f6f0e4', [(0.0, 0.0, 0.012, '#f2d060'), (0.4, 0.2, 0.012, '#5aa0e0'), (-0.4, 0.2, 0.012, '#c0302a'), (0.0, -0.5, 0.012, '#7ac07a')])
obj('pan_brazo_gitano', 'Brazo de gitano', 'tb_bolleria', 'PICKUP', 1.2, 'comida', 'superficie', [
    caja(0.34, 0.012, 0.16, y=0.006, c='#f4efe4', m='metal'), cil(0.06, 0.06, 0.28, y=0.072, c='#e0b868', m='comida', r=[0, 0, 90], seg=12), cil(0.045, 0.045, 0.285, y=0.07, c='#f6f0e0', m='comida', r=[0, 0, 90], seg=12)])
obj('pan_roscon_reyes', 'Roscón de Reyes con fruta escarchada', 'tb_bolleria', 'PICKUP', 1.4, 'comida', 'superficie', [
    cil(0.15, 0.15, 0.012, y=0.006, c='#f4efe4', m='ceramica', seg=16), cil(0.13, 0.13, 0.06, y=0.042, c='#d8a050', m='comida', seg=16), cil(0.04, 0.04, 0.062, y=0.043, c='#f4efe4', m='ceramica', seg=8)] + [
    esf(0.018, 0.1 * (1 if i % 2 else 0.7) * (1 if i < 3 else -1) * 0.8, 0.083, 0.1 * ((i * 2 - 3) % 3 - 1) * 0.9, c=['#c0302a', '#3a8a3a', '#e8c040', '#e87a2a'][i % 4], m='comida') for i in range(6)])
obj('pan_flan_pastelero', 'Flanes de huevo', 'tb_bolleria', 'PICKUP', 1.2, 'comida', 'superficie', [
    caja(0.32, 0.012, 0.22, y=0.006, c='#f4efe4', m='metal')] + [p for i in range(6) for p in (cil(0.04, 0.032, 0.05, x=-0.1 + (i % 3) * 0.1, y=0.037, z=-0.05 + (i // 3) * 0.1, c='#f2d070', m='comida', seg=8), esf(0.04, -0.1 + (i % 3) * 0.1, 0.062, -0.05 + (i // 3) * 0.1, c='#a8602a', m='comida', s=[1, 0.35, 1]))])
for k, (n_, base, creama) in {'pan_empanada': ('Empanada de pisto y atún', '#d8a050', '#c88a3a')}.items():
    obj(k, n_, 'tb_bolleria', 'PICKUP', 1.8, 'comida', 'superficie', [
        caja(0.4, 0.012, 0.3, y=0.006, c='#f4efe4', m='metal'), caja(0.36, 0.05, 0.26, y=0.037, c=base, m='comida'), caja(0.34, 0.01, 0.24, y=0.067, c=creama, m='comida')] + [caja(0.3, 0.012, 0.012, y=0.075, z=-0.08 + i * 0.08, c='#f0d9a0', m='comida') for i in range(3)])

# ---- the traditional sweets: bags, tins and boxes on the rack (facings)
def u_lata_dulce(c, c2, r=0.05, h=0.1):
    def f(x, z): return [cil(r, r, h, x=x, y=h / 2, z=z, c=c, m='metal', seg=10), cil(r + 0.001, r + 0.001, h * 0.45, x=x, y=h * 0.5, z=z, c=c2, m='papel', seg=10), cil(r * 1.04, r * 1.04, 0.012, x=x, y=h + 0.006, z=z, c=oscuro(c, 0.9), m='metal', seg=10)]
    return f
DULCES = [
    ('perrunillas', 'Perrunillas (caja de galletas de manteca)', u_caja_pan('#e8d8a8', 0.14, 0.07, 0.1, '#a06a30'), 4, 3, 0.15, 0.11, 0.07, '#e8d8a8', 0.3),
    ('magdalenas_bolsa', 'Magdalenas de casa en bolsa', u_bolsa_pan('#f2d880', '#c0302a', 0.16, 0.12, 0.08), 3, 3, 0.17, 0.09, 0.12, '#f2d880', 0.35),
    ('roscos_anis', 'Roscos de anís', u_lata_dulce('#d8a050', '#f2efe6', 0.055, 0.1), 4, 3, 0.115, 0.115, 0.1, '#d8a050', 0.4),
    ('roscos_vino', 'Roscos de vino', u_lata_dulce('#b8743a', '#e8c070', 0.055, 0.1), 4, 3, 0.115, 0.115, 0.1, '#b8743a', 0.4),
    ('mantecados', 'Mantecados de Navidad', u_caja_pan('#f2e8d0', 0.16, 0.06, 0.12, '#c0302a'), 3, 3, 0.17, 0.13, 0.06, '#f2e8d0', 0.4),
    ('polvorones', 'Polvorones en su papel', u_bola('#f2e6d0', 0.03), 6, 4, 0.07, 0.07, 0.06, '#f2e6d0', 0.08),
    ('turron', 'Turrones de Navidad', u_caja_pan('#e8c890', 0.2, 0.025, 0.09, '#7a4a2a'), 3, 3, 0.21, 0.1, 0.04, '#e8c890', 0.25),
    ('dulce_leche', 'Tarros de dulce de leche', u_bote(0.04, 0.09, '#e8c078', '#f4efe4', m='cristal'), 4, 3, 0.09, 0.09, 0.09, '#e8c078', 0.3),
    ('sequillos', 'Sequillos', u_bolsa_pan('#efe2c0', '#d8a050', 0.14, 0.14, 0.07), 3, 3, 0.15, 0.08, 0.14, '#efe2c0', 0.3),
    ('bollas_aceite', 'Bollas de aceite', u_ovalo('#d8a858', 0.07, 0.07, 0.4), 4, 3, 0.16, 0.15, 0.04, '#d8a858', 0.15),
    ('floretas', 'Floretas de carnaval', u_bola('#e8b868', 0.03), 5, 4, 0.08, 0.075, 0.06, '#e8b868', 0.12),
    ('cabello_angel', 'Botes de cabello de ángel', u_bote(0.04, 0.1, '#e8b840', '#f4efe4', m='cristal'), 4, 3, 0.09, 0.09, 0.1, '#e8b840', 0.3),
    ('bizcochos_borrachos', 'Bizcochos borrachos', u_caja_pan('#d8a050', 0.1, 0.05, 0.1, '#f2efe6'), 4, 3, 0.11, 0.11, 0.05, '#d8a050', 0.15),
    ('mazapan', 'Mazapanes', u_bola('#d8b070', 0.032), 5, 4, 0.085, 0.075, 0.06, '#d8b070', 0.1),
    ('chocolate_tableta', 'Tabletas de chocolate a la taza', u_caja_pan('#4a2a1a', 0.09, 0.16, 0.015, '#d8b040'), 5, 6, 0.1, 0.02, 0.16, '#4a2a1a', 0.18),
    ('bombones', 'Cajas de bombones', u_caja_pan('#6a3a22', 0.2, 0.04, 0.15, '#d8b040'), 2, 3, 0.21, 0.16, 0.04, '#6a3a22', 0.3),
]
for k, n_, unit, nx, nz, dx, dz, h, c, mu in DULCES:
    regis('pan_dulce_' + k, n_, 'alimento', unit, nx, nz, dx, dz, h, 0.32, c, mu, mat='comida')
# sandwiches, water, coffee
regis('pan_bocadillos', 'Bocadillos envueltos en papel', 'alimento', lambda x, z: [caja(0.2, 0.06, 0.08, x=x, y=0.03, z=z, c='#efe6d0', m='papel'), caja(0.2, 0.012, 0.081, x=x, y=0.054, z=z, c='#c0302a', m='papel')], 1, 3, 0.21, 0.09, 0.06, 0.28, '#efe6d0', 0.3, mat='papel')
regis('pan_cafe_paquete', 'Paquetes de café en grano', 'alimento', u_caja_pan('#6b4426', 0.08, 0.14, 0.06, '#e0a020'), 5, 4, 0.085, 0.065, 0.14, 0.3, '#6b4426', 0.25, mat='papel')

# ---- the obrador (workshop behind the shop)
obj('pan_horno_rotativo', 'Horno rotativo de panadería', 'tb_obrador', 'FIXED', 450, 'metal', 'suelo', [
    caja(1.05, 2.0, 1.0, y=1.0, z=0.0, c='#c3c7ca', m='metal'), caja(0.6, 1.1, 0.02, y=1.1, z=0.51, c='#3a3a3e', m='cristal'), caja(0.6, 1.1, 0.012, y=1.1, z=0.504, c='#f0a040', m='plastico', luz=True), caja(0.05, 0.9, 0.04, x=0.38, y=1.1, z=0.53, c=STEEL, m='metal'),
    caja(0.28, 0.5, 0.02, x=-0.36, y=1.5, z=0.51, c='#2e2e32', m='plastico'), caja(0.2, 0.2, 0.004, x=-0.36, y=1.6, z=0.522, c='#7fe07f', m='plastico', luz=True), caja(1.05, 0.12, 0.05, y=0.06, z=0.5, c='#5a626a', m='metal'), cil(0.1, 0.1, 0.5, x=0.3, y=2.2, z=-0.2, c='#a8adb2', m='metal', seg=12)],
    motivo_fijo=FIJO, nota='con su puerta de cristal, su luz y su chimenea')
obj('pan_horno_sobremesa', 'Horno de sobremesa para pastelería', 'tb_obrador', 'CARRY', 24, 'metal', 'superficie', [
    caja(0.6, 0.45, 0.5, y=0.225, c='#c3c7ca', m='metal'), caja(0.4, 0.32, 0.01, x=-0.05, y=0.23, z=0.255, c='#3a3a3e', m='cristal'), caja(0.12, 0.3, 0.02, x=0.22, y=0.23, z=0.26, c='#2e2e32', m='plastico'), caja(0.4, 0.32, 0.004, x=-0.05, y=0.23, z=0.252, c='#f0a040', m='plastico', luz=True)],
    motivo_clase='24 kg: un horno pequeño, que se lleva entre dos')
obj('pan_amasadora', 'Amasadora de espiral', 'tb_obrador', 'PUSH_HEAVY', 160, 'metal', 'suelo', [
    caja(0.6, 0.85, 0.7, y=0.425, z=0.0, c='#d8dde0', m='metal'), cil(0.3, 0.26, 0.4, y=1.05, z=0.1, c='#c3c7ca', m='metal', seg=16), cil(0.31, 0.31, 0.03, y=1.26, z=0.1, c='#a8adb2', m='metal', seg=16),
    caja(0.12, 0.3, 0.1, y=1.16, z=-0.25, c='#d8dde0', m='metal'), caja(0.2, 0.12, 0.04, x=0.2, y=0.6, z=0.36, c='#2e2e32', m='plastico')], motivo_fijo=FIJO)
obj('pan_laminadora', 'Laminadora de masa', 'tb_obrador', 'PUSH_HEAVY', 190, 'metal', 'suelo', [
    caja(2.2, 0.08, 0.7, y=0.9, z=0.0, c='#d2d6d8', m='metal')] + [caja(0.1, 0.86, 0.1, x=sx * 1.0, y=0.43, z=sz * 0.25, c='#8a9096', m='metal') for sx in (-1, 1) for sz in (-1, 1)] + [
    caja(0.5, 0.3, 0.5, x=0.0, y=1.09, z=-0.05, c='#d8dde0', m='metal'), cil(0.07, 0.07, 0.62, y=1.29, z=-0.05, c='#a8adb2', m='metal', r=[90, 0, 0], seg=12)], motivo_fijo=FIJO)
obj('pan_mesa_obrador', 'Mesa de trabajo de acero con balda', 'mesa', 'PUSH', 42, 'metal', 'suelo', [
    caja(1.5, 0.04, 0.8, y=0.88, c='#d9dedf', m='metal')] + [caja(0.05, 0.86, 0.05, x=sx * 0.7, y=0.43, z=sz * 0.35, c=STEEL, m='metal') for sx in (-1, 1) for sz in (-1, 1)] + [caja(1.4, 0.03, 0.7, y=0.25, c='#c3c7ca', m='metal')],
    superficies=[sup(0.9, 0.05), sup(0.265, 0.05)])
def carro_bandejas(id, nombre, llenas):
    P = [caja(0.04, 1.75, 0.04, x=sx * 0.3, y=0.875, z=sz * 0.36, c='#a8adb2', m='metal') for sx in (-1, 1) for sz in (-1, 1)]
    P += [caja(0.6, 0.012, 0.72, y=0.2 + k * 0.17, c='#8a9096', m='metal') for k in range(9)]
    P += [cil(0.05, 0.05, 0.04, x=sx * 0.3, y=0.05, z=sz * 0.36, c=DARK, m='goma', r=[0, 0, 90], seg=8) for sx in (-1, 1) for sz in (-1, 1)]
    for k in llenas: P += [esf(1.0, -0.12 + i * 0.12, 0.2 + k * 0.17 + 0.026, z, c=['#d89a48', '#c88a3a', '#e8c078'][(i + k) % 3], m='comida', s=[0.07, 0.03, 0.06]) for i in range(4) for z in (-0.2, 0.2)]
    obj(id, nombre, 'tb_obrador', 'PUSH', 38, 'metal', 'suelo', P, nota='carro de bandejas con el pan recién salido del horno')
carro_bandejas('pan_carro_bandejas', 'Carro de bandejas con pan', (1, 3, 5))
carro_bandejas('pan_carro_bandejas_vacio', 'Carro de bandejas vacío', ())
obj('pan_camara_fermentacion', 'Cámara de fermentación', 'tb_obrador', 'PUSH_HEAVY', 130, 'metal', 'suelo', [
    caja(0.8, 2.0, 0.8, y=1.0, c='#e6e9ea', m='metal'), caja(0.7, 1.7, 0.01, y=1.0, z=0.405, c='#9ab8c8', m='cristal'), caja(0.12, 0.2, 0.02, x=0.3, y=1.9, z=0.41, c='#2e2e32', m='plastico'), caja(0.08, 0.04, 0.004, x=0.3, y=1.92, z=0.421, c='#f0a040', m='plastico', luz=True)], motivo_fijo=FIJO)
obj('pan_batidora', 'Batidora planetaria', 'tb_obrador', 'CARRY', 22, 'metal', 'superficie', [
    caja(0.4, 0.12, 0.4, y=0.06, c='#d8dde0', m='metal'), caja(0.12, 0.45, 0.12, y=0.34, z=-0.14, c='#d8dde0', m='metal'), caja(0.12, 0.12, 0.3, y=0.52, z=0.0, c='#d8dde0', m='metal'), cil(0.16, 0.12, 0.24, y=0.24, z=0.1, c='#c3c7ca', m='metal', seg=16)],
    motivo_clase='22 kg: una batidora de sobremesa, a mano')
obj('pan_saco_harina', 'Saco de harina de 25 kg', 'tb_saco', 'PUSH', 25, 'tela', 'suelo', [
    caja(0.4, 0.5, 0.2, y=0.25, c='#efe8d8', m='tela'), esf(1.0, 0, 0.5, 0, c='#efe8d8', m='tela', s=[0.2, 0.08, 0.1]), caja(0.3, 0.2, 0.012, y=0.3, z=0.106, c='#2c5aa0', m='papel'), caja(0.4, 0.02, 0.22, y=0.01, c='#d8d0c0', m='tela')])
obj('pan_pila_harina', 'Pila de sacos de harina', 'tb_pila_producto', 'PUSH', 75, 'tela', 'suelo', [
    p for k in range(3) for p in (caja(0.8, 0.2, 0.5, y=0.1 + k * 0.205, c='#efe8d8' if k % 2 else '#e6dfcf', m='tela'), caja(0.5, 0.1, 0.012, y=0.1 + k * 0.205, z=0.256, c='#2c5aa0', m='papel'))] + [caja(0.9, 0.04, 0.6, y=0.02, c='#b88a58', m='madera')],
    nota='sacos de harina sobre un palé')
obj('pan_estante_moldes', 'Estante de moldes y bandejas', 'estanteria', 'PUSH', 40, 'metal', 'suelo', [
    caja(0.05, 1.8, 0.05, x=sx * 0.57, y=0.9, z=sz * 0.28 + 0.3, c='#a8adb2', m='metal') for sx in (-1, 1) for sz in (-1, 1)] + [caja(1.2, 0.03, 0.6, y=y, z=0.3, c='#c3c7ca', m='metal') for y in (0.4, 0.8, 1.2, 1.6)] + [
    caja(0.5, 0.06, 0.4, x=-0.3, y=0.43, z=0.3, c='#8a9096', m='metal'), caja(0.5, 0.06, 0.4, x=0.3, y=0.43, z=0.3, c='#8a9096', m='metal'), caja(0.4, 0.1, 0.5, x=-0.3, y=0.85, z=0.3, c='#7a7e84', m='metal'), caja(0.4, 0.1, 0.5, x=0.3, y=0.85, z=0.3, c='#7a7e84', m='metal')],
    superficies=[sup(1.215, 0.04, fondo=0.55), sup(1.615, 0.04, fondo=0.55)])
obj('pan_cubeta_masa', 'Cubeta de masa con trapo', 'recipiente', 'PICKUP', 4.5, 'plastico', 'suelo', [
    cil(0.22, 0.18, 0.3, y=0.15, c='#e6e9ea', m='plastico', seg=16), cil(0.2, 0.2, 0.02, y=0.31, c='#e8d4a8', m='comida', seg=16), caja(0.3, 0.01, 0.3, y=0.325, c='#f2efe6', m='tela')])
obj('pan_pala_obrador', 'Palas y rasquetas', 'decoracion', 'PICKUP', 2.4, 'madera', 'pared', [
    caja(0.04, 0.9, 0.02, x=-0.2, y=1.5, z=0.02, c='#a8825a', m='madera'), caja(0.04, 0.9, 0.02, x=0.0, y=1.5, z=0.02, c='#8a6a40', m='madera'), caja(0.16, 0.28, 0.01, x=-0.2, y=1.1, z=0.025, c='#c8a06a', m='madera'), caja(0.14, 0.08, 0.01, x=0.0, y=1.15, z=0.025, c=STEEL, m='metal')])
