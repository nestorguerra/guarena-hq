# The perfumery's objects (family «tiendas_b»): glass counters, lit wall shelving, display tables, the make-up table, the
# treatment cabin and, above all, the goods: perfumes in a score of bottles and the cosmetics, as facings. Ids start with «per_».
# No real brand: invented names («Azahar», «Brisa de Mayo»…), plain colours.
from tb_base import *

NEGRO, NEGRO_B = '#2e2e34', '#3a3a42'
CREMA, ORO = '#ece4d6', '#d2b46a'
LUZ_CAL = '#fff1d0'

# ---- glass counter: a low cabinet and a glass case on it (the top plate is a surface for testers and the till)
def vitrina(id, nombre, cuerpo, frente, tapa=NEGRO):
    P = [caja(1.2, 0.66, 0.56, y=0.33, z=0.0, c=cuerpo), caja(1.2, 0.07, 0.6, y=0.035, z=0.0, c=oscuro(cuerpo, 0.5)), caja(1.12, 0.5, 0.012, y=0.38, z=0.274, c=frente),
         caja(1.2, 0.04, 0.6, y=0.68, z=0.0, c=tapa), caja(1.2, 0.3, 0.012, y=0.85, z=0.28, c=GLASS, m='cristal'), caja(1.2, 0.3, 0.012, y=0.85, z=-0.28, c=GLASS, m='cristal'),
         caja(0.012, 0.3, 0.56, x=-0.594, y=0.85, c=GLASS, m='cristal'), caja(0.012, 0.3, 0.56, x=0.594, y=0.85, c=GLASS, m='cristal'),
         caja(1.2, 0.012, 0.6, y=1.006, c=GLASS, m='cristal'), caja(1.16, 0.012, 0.5, y=0.84, c=GLASS, m='cristal'), caja(1.1, 0.004, 0.42, y=0.874, c='#5a2a3a', m='tela')]
    # what is in the case: small boxes and bottles on the velvet
    for i, c in enumerate(['#b3547a', '#6a8aa8', '#c8a040', '#7aa07a', '#d8d0c0', '#8a5a9a']):
        P += [caja(0.07, 0.1, 0.05, x=-0.45 + i * 0.18, y=0.926, z=-0.08, c=c, m='cristal'), caja(0.04, 0.02, 0.03, x=-0.45 + i * 0.18, y=0.986, z=-0.08, c=ORO, m='metal')]
        P += [caja(0.09, 0.05, 0.07, x=-0.4 + i * 0.18, y=0.0 + 0.9, z=0.1, c=c, m='papel')] if i % 2 == 0 else []
    P += [caja(1.2, 0.018, 0.012, y=1.0, z=0.28, c=ORO, m='metal')]
    obj(id, nombre, 'mostrador', 'FIXED', 140, 'cristal', 'suelo', P, motivo_fijo='estructural', superficies=[sup(1.012, 0.04)], nota='mostrador de cristal: el cuerpo, la vitrina con terciopelo y una tapa para los probadores')
vitrina('per_mostrador_vitrina_crema', 'Mostrador vitrina (1,2 m), crema', CREMA, '#d8cdb8')
vitrina('per_mostrador_vitrina_negro', 'Mostrador vitrina (1,2 m), negro y oro', '#34343a', '#2a2a30')

# ---- lit wall shelving: glass shelves with a warm strip under each, a black back
def estanteria_luz(id, nombre, ancho=1.0, ys=(0.45, 0.8, 1.15, 1.5, 1.85, 2.2), c='#2e2e34', alto=2.45):
    d = 0.3
    P = [caja(0.025, alto, d, x=-ancho / 2 + 0.0125, z=d / 2, c=c), caja(0.025, alto, d, x=ancho / 2 - 0.0125, z=d / 2, c=c), caja(ancho - 0.05, alto, 0.015, z=0.0075, c=oscuro(c, 0.9)), caja(ancho - 0.05, 0.1, d - 0.03, y=0.05, z=d / 2, c=oscuro(c, 0.6))]
    P += [caja(ancho - 0.05, 0.016, d - 0.02, y=y - 0.008, z=d / 2, c=GLASS, m='cristal') for y in ys]
    P += [caja(ancho - 0.1, 0.008, 0.02, y=y - 0.02, z=0.06, c=LUZ_CAL, m='plastico', luz=True) for y in ys[1:]]
    P += [caja(ancho - 0.05, 0.1, 0.04, y=alto - 0.05, z=0.02, c=ORO, m='metal')]
    obj(id, nombre, 'estanteria', 'FIXED', 52, 'madera', 'suelo', P, motivo_fijo=FIJO, superficies=[sup(y, 0.02, fondo=d - 0.04) for y in ys], nota='baldas de cristal con una tira de luz cálida debajo')
estanteria_luz('per_estanteria_luz', 'Estantería de cristal con luz (1 m)')
estanteria_luz('per_estanteria_luz_baja', 'Estantería baja de cristal con luz (1 m)', ys=(0.45, 0.8, 1.15, 1.5), alto=1.7, c='#3a3a42')

# ---- display table (round, with a lower shelf) and a lit tower of tiers
def mesa_expositora(id, nombre, c, forma='redonda'):
    r = 0.45
    P = [cil(r, r, 0.04, y=0.8, c=c, seg=20), cil(0.05, 0.05, 0.76, y=0.38, c=oscuro(c, 0.8), seg=10), cil(0.3, 0.3, 0.03, y=0.015, c=oscuro(c, 0.7), seg=16), cil(0.3, 0.3, 0.03, y=0.4, c=CREMA, m='madera', seg=16)]
    obj(id, nombre, 'mesa', None, 24, 'madera', 'suelo', P, superficies=[sup(0.82, 0.07)], nota='mesa expositora redonda con balda baja')
mesa_expositora('per_mesa_expositora_negra', 'Mesa expositora redonda (negra)', '#34343a')
mesa_expositora('per_mesa_expositora_crema', 'Mesa expositora redonda (crema)', '#d8cdb8')
obj('per_torre_tester', 'Expositor escalonado de probadores', 'mueble', 'PUSH', 30, 'madera', 'suelo', [
    caja(0.7, 0.3, 0.3, y=0.15, z=0.3, c='#2e2e34'), caja(0.7, 0.55, 0.3, y=0.275, z=0.0, c='#3a3a42'), caja(0.7, 0.8, 0.3, y=0.4, z=-0.3, c='#2e2e34'),
    caja(0.7, 0.012, 0.3, y=0.306, z=0.3, c=ORO, m='metal'), caja(0.7, 0.012, 0.3, y=0.556, z=0.0, c=ORO, m='metal'), caja(0.7, 0.012, 0.3, y=0.806, z=-0.3, c=ORO, m='metal')],
    superficies=[sup(0.312, 0.03), sup(0.562, 0.03), sup(0.812, 0.03)], nota='tres escalones para los probadores')

# ---- the make-up table: a dressing table with a lit mirror (a frame of bulbs) and its stool
obj('per_tocador_maquillaje', 'Tocador de maquillaje con espejo de bombillas y taburete', 'mesa', 'PUSH', 42, 'madera', 'suelo', [
    caja(1.2, 0.05, 0.5, y=0.76, z=0.25, c='#e9e1d3')] + [caja(0.05, 0.74, 0.05, x=sx * 0.55, y=0.37, z=0.03 + sz * 0.22 + 0.22, c='#d8cdb8') for sx in (-1, 1) for sz in (-1, 1)] + [
    caja(1.0, 0.1, 0.46, y=0.69, z=0.25, c='#d8cdb8'), caja(0.9, 0.7, 0.02, y=1.2, z=0.02, c='#3a3a42'), caja(0.82, 0.62, 0.006, y=1.2, z=0.032, c=MIRROR, m='metal')]
    + [caja(0.03, 0.03, 0.03, x=x, y=1.55, z=0.035, c='#fff3d6', m='plastico', luz=True) for x in (-0.38, -0.19, 0, 0.19, 0.38)] + [caja(0.03, 0.03, 0.03, x=sx * 0.43, y=y, z=0.035, c='#fff3d6', m='plastico', luz=True) for sx in (-1, 1) for y in (0.95, 1.2, 1.45)]
    + [cil(0.19, 0.19, 0.08, y=0.52, z=0.78, c='#b3547a', m='tela', seg=14), cil(0.03, 0.03, 0.44, y=0.26, z=0.78, c=ORO, m='metal', seg=8), cil(0.18, 0.18, 0.025, y=0.0125, z=0.78, c=ORO, m='metal', seg=14)],
    superficies=[sup(0.785, 0.05, ancho=1.2)], modificadores=['SEAT'], asientos=[{'p': [0, 0.56, 0.78], 'h': 0.56, 'anim': 'taburete_alto'}], nota='tocador con bombillas alrededor del espejo, para probar el maquillaje; su taburete, un poco apartado')
obj('per_taburete_maquillaje', 'Taburete tapizado de maquillaje', 'taburete', 'PICKUP', 4.5, 'tela', 'suelo', [
    cil(0.19, 0.19, 0.08, y=0.52, c='#b3547a', m='tela', seg=14), cil(0.03, 0.03, 0.44, y=0.26, c=ORO, m='metal', seg=8), cil(0.18, 0.18, 0.025, y=0.0125, c=ORO, m='metal', seg=14)],
    modificadores=['SEAT'], asientos=[{'p': [0, 0.56, 0.0], 'h': 0.56, 'anim': 'taburete_alto'}])

# ---- the treatment cabin: couch, trolley, steamer, magnifier lamp, shelf with oils and towels
obj('per_camilla_estetica', 'Camilla de estética con toalla', 'tb_camilla', None, 46, 'tela', 'suelo', [
    caja(0.7, 0.1, 1.9, y=0.68, c='#f2eee6', m='tela'), caja(0.7, 0.14, 1.9, y=0.58, c='#e0ddd4', m='tela'), caja(0.5, 0.05, 0.3, y=0.74, z=0.9, c='#e8e4da', m='tela'),
    caja(0.46, 0.35, 0.05, y=0.9, z=-0.95, c='#e8e4da', m='tela', r=[20, 0, 0]),
    caja(0.6, 0.05, 1.7, y=0.025, c='#cfd3d6', m='metal'), cil(0.04, 0.04, 0.5, x=-0.2, y=0.3, z=0.7, c=STEEL, seg=8), cil(0.04, 0.04, 0.5, x=0.2, y=0.3, z=0.7, c=STEEL, seg=8),
    cil(0.04, 0.04, 0.5, x=-0.2, y=0.3, z=-0.7, c=STEEL, seg=8), cil(0.04, 0.04, 0.5, x=0.2, y=0.3, z=-0.7, c=STEEL, seg=8), caja(0.66, 0.04, 0.5, y=0.755, z=0.2, c='#9ab8c8', m='tela')],
    superficies=[sup(0.775, 0.1)], nota='camilla con una toalla azul doblada y el cabecero')
obj('per_carrito_estetica', 'Carrito de estética con productos', 'mueble', 'CARRY', 9, 'metal', 'suelo', [
    caja(0.04, 0.82, 0.04, x=sx * 0.2, y=0.46, z=sz * 0.13, c=STEEL, m='metal') for sx in (-1, 1) for sz in (-1, 1)] + [
    caja(0.46, 0.025, 0.34, y=y, c='#f2eee6', m='plastico') for y in (0.15, 0.47, 0.8)] + [cil(0.025, 0.025, 0.02, x=sx * 0.2, y=0.025, z=sz * 0.13, c='#2b2b2e', m='goma', r=[0, 0, 90], seg=8) for sx in (-1, 1) for sz in (-1, 1)],
    superficies=[sup(0.8125, 0.03), sup(0.4825, 0.03)])
obj('per_lampara_lupa', 'Lámpara de lupa con pie', 'lampara', 'CARRY', 7, 'metal', 'suelo', [
    cil(0.25, 0.25, 0.03, y=0.015, c='#cfd3d6', m='metal', seg=14), cil(0.025, 0.025, 1.3, y=0.68, c='#cfd3d6', m='metal', seg=8), caja(0.03, 0.03, 0.6, y=1.35, z=0.3, c='#cfd3d6', m='metal'),
    cil(0.16, 0.16, 0.05, y=1.33, z=0.6, c='#f2eee6', m='plastico', r=[90, 0, 0], seg=16), cil(0.14, 0.14, 0.01, y=1.33, z=0.63, c=GLASS, m='cristal', r=[90, 0, 0], seg=16)])
obj('per_vaporizador_facial', 'Vaporizador facial', 'pequeño_electrodomestico', 'CARRY', 9, 'metal', 'suelo', [
    cil(0.2, 0.2, 0.03, y=0.015, c='#cfd3d6', m='metal', seg=12), cil(0.03, 0.03, 1.1, y=0.58, c='#cfd3d6', m='metal', seg=8), cil(0.1, 0.12, 0.2, y=1.2, c='#f2eee6', m='plastico', seg=12), cil(0.05, 0.05, 0.12, y=1.04, z=0.1, c='#f2eee6', m='plastico', r=[90, 0, 0], seg=10)])
obj('per_taburete_estetica', 'Taburete de esteticista', 'taburete', 'PICKUP', 3.5, 'tela', 'suelo', [
    cil(0.19, 0.19, 0.08, y=0.5, c='#f2eee6', m='tela', seg=14), cil(0.03, 0.03, 0.42, y=0.25, c=STEEL, m='metal', seg=8), cil(0.2, 0.2, 0.025, y=0.0125, c=STEEL, m='metal', seg=14)],
    modificadores=['SEAT'], asientos=[{'p': [0, 0.54, 0.0], 'h': 0.54, 'anim': 'taburete_alto'}])
obj('per_estante_cabina', 'Estante de aceites y toallas', 'estanteria', 'FIXED', 12, 'madera', 'pared', [
    caja(0.9, 0.025, 0.25, y=1.3, z=0.125, c='#e9e1d3'), caja(0.9, 0.025, 0.25, y=1.7, z=0.125, c='#e9e1d3'), caja(0.9, 0.5, 0.012, y=1.5, z=0.006, c='#d8cdb8'),
    caja(0.3, 0.12, 0.2, x=-0.25, y=1.7125 + 0.06, z=0.125, c='#f2eee6', m='tela'), caja(0.3, 0.12, 0.2, x=-0.25, y=1.7125 + 0.18, z=0.125, c='#9ab8c8', m='tela')]
    + [cil(0.035, 0.035, 0.13, x=x, y=1.3125 + 0.065, z=0.125, c=c, m='cristal', seg=8) for x, c in ((0.0, '#c8a040'), (0.1, '#7aa07a'), (0.2, '#b3547a'), (0.3, '#8a5a9a'))], motivo_fijo=FIJO, superficies=[sup(1.3125, 0.03, fondo=0.23)])
obj('per_cortina_cabina', 'Cortina de la cabina', 'textil', 'FIXED', 2.5, 'tela', 'pared', [
    caja(1.0, 2.2, 0.03, y=1.15, z=0.015, c='#d8cdb8', m='tela'), caja(1.04, 0.03, 0.05, y=2.28, z=0.025, c=STEEL, m='metal')], motivo_fijo=FIJO)

# ---- the shop's own sign and posters
obj('per_rotulo', 'Rótulo interior de la perfumería', 'decoracion', 'PICKUP', 3, 'madera', 'pared', [
    caja(1.3, 0.34, 0.03, y=2.55, z=0.015, c='#1f1f24'), plano(1.24, 0.28, y=2.55, z=0.033, tex={'tipo': 'rotulo_tb', 'estilo': 'perfumeria', 'rotulo_local': True})])
obj('per_cartel_perfume', 'Cartel de una fragancia', 'cuadro', 'PICKUP', 1.2, 'papel', 'pared', [
    caja(0.5, 0.7, 0.025, y=1.75, z=0.0125, c='#2a2420'), plano(0.44, 0.64, y=1.75, z=0.027, tex={'tipo': 'cartel_tb', 'dibujo': 'perfume'})])
obj('per_cartel_belleza', 'Cartel de la sección de belleza', 'cuadro', 'PICKUP', 1.2, 'papel', 'pared', [
    caja(0.5, 0.7, 0.025, y=1.75, z=0.0125, c='#2a2420'), plano(0.44, 0.64, y=1.75, z=0.027, tex={'tipo': 'cartel_tb', 'dibujo': 'peinado_b', 'titulo': 'Belleza y cuidado'})])
obj('per_pizarra_tratamientos', 'Pizarra de tratamientos y precios', 'decoracion', 'PICKUP', 2.5, 'madera', 'pared', [
    caja(0.7, 0.9, 0.025, y=1.55, z=0.0125, c='#5a3a20'), plano(0.64, 0.84, y=1.55, z=0.0285, tex={'tipo': 'pizarra', 'lineas': ['Limpieza facial  38', 'Masaje relajante  45', 'Manicura  18', 'Pedicura  25', 'Depilación  12', 'Maquillaje  30']})])
obj('per_perfumes_escaparate', 'Pirámide de perfumes de regalo', 'tb_cosmetico', 'PICKUP', 2.4, 'cristal', 'superficie', [
    caja(0.5, 0.04, 0.3, y=0.02, c=ORO, m='metal')] + [p for k, (n, y) in enumerate(((4, 0.04), (3, 0.17), (2, 0.3))) for i in range(n) for p in (
    caja(0.09, 0.12, 0.07, x=(i - (n - 1) / 2) * 0.11, y=y + 0.06, z=0.0, c=['#b3547a', '#6a8aa8', '#c8a040', '#7aa07a'][(i + k) % 4], m='papel'),)], nota='cajas de regalo apiladas, para la caja')

# ---- bottles: the perfumes (a body of glass with its liquid, a cap) as facings
def f_cuadrado(c, tapon, w=0.055, h=0.11, d=0.035):
    def f(x, z): return [caja(w, h, d, x=x, y=h / 2, z=z, c=c, m='cristal'), caja(w - 0.012, h - 0.03, d - 0.012, x=x, y=h / 2 - 0.005, z=z, c=mezcla(c, '#c8a040', 0.4), m='comida'), caja(w * 0.5, 0.03, d * 0.7, x=x, y=h + 0.015, z=z, c=tapon, m='metal')]
    return f
def f_redondo(c, tapon, r=0.032, h=0.1):
    def f(x, z): return [cil(r, r, h, x=x, y=h / 2, z=z, c=c, m='cristal', seg=10), cil(r - 0.005, r - 0.005, h - 0.03, x=x, y=h / 2 - 0.005, z=z, c=mezcla(c, '#c8a040', 0.4), m='comida', seg=10), esf(r * 0.6, x, h + r * 0.45, z, c=tapon, m='metal')]
    return f
def f_alto(c, tapon, r=0.02, h=0.17):
    def f(x, z): return [cil(r, r, h, x=x, y=h / 2, z=z, c=c, m='cristal', seg=8), cil(r - 0.004, r - 0.004, h - 0.02, x=x, y=h / 2, z=z, c=mezcla(c, '#c8a040', 0.4), m='comida', seg=8), cil(r * 0.7, r * 0.7, 0.04, x=x, y=h + 0.02, z=z, c=tapon, m='metal', seg=8)]
    return f
def f_plano(c, tapon, w=0.07, h=0.09, d=0.02):
    def f(x, z): return [caja(w, h, d, x=x, y=h / 2, z=z, c=c, m='cristal'), caja(w - 0.01, h - 0.02, d - 0.006, x=x, y=h / 2, z=z, c=mezcla(c, '#c8a040', 0.4), m='comida'), caja(w * 0.4, 0.025, d, x=x, y=h + 0.0125, z=z, c=tapon, m='metal')]
    return f
def f_cono(c, tapon, r=0.036, h=0.12):
    def f(x, z): return [{**cono(r, h, x=x, y=h / 2, z=z, c=c, m='cristal', seg=10)}, esf(0.017, x, h + 0.01, z, c=tapon, m='metal')]
    return f
def f_esfera(c, tapon, r=0.04):
    def f(x, z): return [esf(r, x, r, z, c=c, m='cristal'), cil(0.012, 0.012, 0.03, x=x, y=2 * r + 0.012, z=z, c=tapon, m='metal', seg=8)]
    return f
PERFUMES = [
    ('azahar', 'Eau de parfum «Azahar»', f_cuadrado('#f4f0dc', ORO), 4, 0.065),
    ('jazmin', 'Eau de parfum «Jazmín»', f_redondo('#f2f4ee', '#e8e4d8'), 4, 0.075),
    ('rosa_mayo', 'Eau de parfum «Rosa de Mayo»', f_alto('#f4c8d8', '#c8a040'), 5, 0.055),
    ('lavanda', 'Colonia «Lavanda del Jerte»', f_plano('#c8b8e8', '#e8e4d8'), 4, 0.08),
    ('sandalo', 'Eau de parfum «Sándalo»', f_cuadrado('#d8b890', '#3a2a1a', 0.06, 0.12), 4, 0.07),
    ('ambar', 'Eau de parfum «Ámbar»', f_redondo('#e6b050', '#5a3a1a', 0.034, 0.11), 4, 0.078),
    ('citrus', 'Colonia fresca «Citrus»', f_cono('#e8e46a', '#e8e4d8'), 4, 0.08),
    ('brisa_marina', 'Eau de toilette «Brisa Marina»', f_plano('#a8d8e8', '#2c5aa0', 0.075, 0.1), 4, 0.085),
    ('vainilla', 'Eau de parfum «Vainilla»', f_esfera('#f2e0b0', '#c8a040'), 4, 0.09),
    ('noche_verano', 'Eau de parfum «Noche de Verano»', f_alto('#4a3a8a', '#c8a040', 0.022, 0.18), 5, 0.058),
    ('madera_noble', 'Eau de parfum «Madera Noble»', f_cuadrado('#8a5a32', '#c8a040', 0.062, 0.115, 0.04), 4, 0.072),
    ('almendro', 'Colonia «Almendro en flor»', f_redondo('#f6dede', '#c8a040', 0.03, 0.09), 5, 0.068),
    ('higuera', 'Eau de toilette «Higuera»', f_alto('#a8c88a', '#e8e4d8', 0.02, 0.16), 5, 0.055),
    ('romero', 'Colonia «Romero y tomillo»', f_cuadrado('#7aa07a', '#2b2b2e'), 4, 0.065),
    ('pino', 'Eau de toilette «Pino y cedro»', f_plano('#4a7a6a', '#c8a040', 0.07, 0.11), 4, 0.08),
    ('caramelo', 'Eau de parfum «Caramelo»', f_cono('#d89a4a', '#5a3a1a', 0.038, 0.13), 4, 0.085),
    ('violeta', 'Eau de parfum «Violeta»', f_esfera('#c8a0e0', '#e8e4d8', 0.036), 4, 0.085),
    ('cuero', 'Eau de toilette «Cuero y tabaco»', f_cuadrado('#4a3a30', '#c8a040', 0.065, 0.12), 4, 0.075),
    ('niños', 'Colonia infantil «Nube»', f_redondo('#bfe0f0', '#f4c8d8', 0.036, 0.1), 4, 0.08),
    ('oud', 'Eau de parfum «Oud»', f_alto('#2e2a3a', '#d2b46a', 0.026, 0.19), 4, 0.065),
]
for k, n_, unit, nx, dx in PERFUMES:
    regis('per_perfume_' + k.replace('ñ', 'n'), n_, 'tb_cosmetico', unit, nx, 2, dx, 0.07, 0.2, 0.27, '#d8cdb8', 0.14, mat='cristal', hf=0.55)

# ---- cosmetics
def u_pintalabios(c1, c2):
    def f(x, z): return [cil(0.011, 0.011, 0.05, x=x, y=0.025, z=z, c='#2e2e34', m='metal', seg=8), cil(0.009, 0.009, 0.025, x=x, y=0.062, z=z, c=c1, m='comida', seg=8)]
    return f
def u_esmalte(c, tapon='#2e2e34'):
    def f(x, z): return [cil(0.016, 0.016, 0.05, x=x, y=0.025, z=z, c=c, m='cristal', seg=8), cil(0.008, 0.008, 0.05, x=x, y=0.075, z=z, c=tapon, m='plastico', seg=6)]
    return f
COS = [
    ('pintalabios_rojos', 'Pintalabios rojos y coral', u_pintalabios('#c0302a', '#e07a5a'), 8, 0.032, 0.08, 'plastico'),
    ('pintalabios_nude', 'Pintalabios nude y rosa', u_pintalabios('#d8a090', '#e8a0b8'), 8, 0.032, 0.08, 'plastico'),
    ('esmaltes_rojos', 'Esmaltes de uñas rojos', u_esmalte('#c0302a'), 6, 0.04, 0.1, 'cristal'),
    ('esmaltes_pastel', 'Esmaltes de uñas pastel', u_esmalte('#e8b8d0', '#e8e4d8'), 6, 0.04, 0.1, 'cristal'),
    ('mascara_pestanas', 'Máscaras de pestañas', u_tubo(0.03, 0.14, '#2e2e34', '#d2b46a'), 6, 0.038, 0.14, 'plastico'),
    ('base_maquillaje', 'Bases de maquillaje', u_botella(0.022, 0.1, '#e8c8a8', '#f4f0e8', '#2e2e34', m='cristal'), 5, 0.055, 0.1, 'cristal'),
    ('polvos_compactos', 'Polvos compactos', lambda x, z: [cil(0.04, 0.04, 0.018, x=x, y=0.009, z=z, c='#2e2e34', m='plastico', seg=14), cil(0.034, 0.034, 0.004, x=x, y=0.02, z=z, c='#e0c0a0', m='comida', seg=14)], 4, 0.09, 0.03, 'plastico'),
    ('paleta_sombras', 'Paletas de sombras de ojos', lambda x, z: [caja(0.11, 0.015, 0.07, x=x, y=0.0075, z=z, c='#3a3a42', m='plastico')] + [caja(0.02, 0.004, 0.02, x=x - 0.04 + i * 0.027, y=0.017, z=z, c=['#c0586a', '#e0a050', '#7a8ab0', '#8a6a4a'][i], m='comida') for i in range(4)], 3, 0.12, 0.03, 'plastico'),
    ('brochas', 'Brochas de maquillaje en un vaso', lambda x, z: [cil(0.04, 0.04, 0.08, x=x, y=0.04, z=z, c='#e8e4d8', m='ceramica', seg=8)] + [p for dx, dz in ((-0.015, 0), (0.015, 0.01), (0, -0.015)) for p in (cil(0.005, 0.005, 0.1, x=x + dx, y=0.12, z=z + dz, c='#c8a040', m='madera', seg=5), cil(0.013, 0.009, 0.035, x=x + dx, y=0.18, z=z + dz, c='#2e2e34', m='tela', seg=6))], 3, 0.1, 0.2, 'plastico'),
    ('crema_facial', 'Cremas faciales en tarro', u_bote(0.035, 0.05, '#f4f0e8', '#d2b46a'), 5, 0.08, 0.05, 'cristal'),
    ('serum', 'Sérums con cuentagotas', u_botella(0.017, 0.1, '#e8d8b0', '#f4f0e8', '#2e2e34', m='cristal'), 6, 0.045, 0.1, 'cristal'),
    ('crema_manos', 'Cremas de manos', u_tubo(0.04, 0.12, '#f4d6e2', '#b3547a'), 6, 0.05, 0.12, 'plastico'),
    ('leche_corporal', 'Leches corporales', u_botella(0.032, 0.18, '#f0e8f4', '#8a5a9a', '#8a5a9a', m='plastico'), 4, 0.075, 0.18, 'plastico'),
    ('gel_ducha', 'Geles de ducha', u_botella(0.032, 0.2, '#bfe0f0', '#2c8ab0', '#2c8ab0', m='plastico'), 4, 0.075, 0.2, 'plastico'),
    ('jabones', 'Jabones artesanos', lambda x, z: [caja(0.07, 0.025, 0.05, x=x, y=0.0125 + k * 0.025, z=z, c=['#e8c8a8', '#c8d8a8', '#e0b8d0'][k % 3], m='comida') for k in range(3)], 4, 0.08, 0.075, 'comida'),
    ('sales_bano', 'Sales de baño', u_bote(0.04, 0.12, '#bfd8f0', '#d2b46a'), 4, 0.09, 0.12, 'cristal'),
    ('protector_solar', 'Protectores solares', u_botella(0.03, 0.16, '#f2c850', '#2c5aa0', '#2c5aa0', m='plastico'), 4, 0.07, 0.16, 'plastico'),
    ('desmaquillante', 'Desmaquillantes', u_botella(0.028, 0.15, '#bfe8e0', '#f4f0e8', '#3a8a7a', m='cristal'), 4, 0.065, 0.15, 'cristal'),
    ('agua_perfumada', 'Aguas perfumadas de ambiente', u_botella(0.03, 0.14, '#d8e8c8', '#f4f0e8', '#7aa07a', m='cristal'), 4, 0.07, 0.14, 'cristal'),
]
for k, n_, unit, nx, dx, h, mat in COS:
    regis('per_cosm_' + k, n_, 'tb_cosmetico', unit, nx, 2 if k == 'brochas' else 3, dx, 0.1 if k == 'brochas' else 0.075, h, 0.25, '#e0d4c0', 0.12, mat=mat, hf=0.7)
# small things for the counter
obj('per_cesto_regalo', 'Cesto de regalo con lazo', 'tb_cosmetico', 'PICKUP', 1.6, 'tela', 'superficie', [
    caja(0.32, 0.14, 0.22, y=0.07, c='#c8a878', m='madera'), caja(0.08, 0.1, 0.06, x=-0.08, y=0.19, c='#b3547a', m='cristal'), caja(0.07, 0.12, 0.05, x=0.04, y=0.2, c='#6a8aa8', m='cristal'), caja(0.1, 0.04, 0.2, y=0.16, c='#b3547a', m='tela', r=[0, 0, 0])])
obj('per_bolsas_regalo', 'Bolsas de regalo dobladas', 'papel', 'PICKUP', 0.5, 'papel', 'superficie', [
    caja(0.28, 0.12, 0.12, y=0.06, c='#2e2e34', m='papel'), caja(0.28, 0.012, 0.12, y=0.126, c=ORO, m='papel')])
obj('per_tarjetero_fidelidad', 'Expositor de tarjetas regalo', 'papel', 'PICKUP', 0.3, 'papel', 'superficie', [
    caja(0.12, 0.012, 0.08, y=0.006, c=ORO, m='metal'), caja(0.1, 0.1, 0.01, y=0.062, z=-0.01, c='#f2eee6', m='papel', r=[-10, 0, 0])])
obj('per_probador_papel', 'Tarro de tiras de papel para probar', 'tb_cosmetico', 'PICKUP', 0.3, 'cristal', 'superficie', [
    cil(0.04, 0.04, 0.08, y=0.04, c=GLASS, m='cristal', seg=10)] + [caja(0.012, 0.1, 0.004, x=-0.02 + i * 0.02, y=0.11, z=0.0, c='#f2eee6', m='papel', r=[0, 0, -10 + i * 10]) for i in range(3)])
