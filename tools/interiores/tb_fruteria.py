# The greengrocer's objects (family «tiendas_b»): the counter, stepped stands and islands of crates, hanging bananas and garlic,
# sacks of potatoes and onions, baskets, the stock room — and, above all, the produce: crates of fruit and vegetables of
# fifty kinds (shapes made of a few spheres, cylinders and cones, in their colours). Ids start with «fru_».
from tb_base import *

VERDE_F = '#2f7a3a'
CAJA_M, CAJA_M2 = '#b88a58', '#9a7040'

# ---- the counter: wood with a green front and a steel plate for the scale
obj('fru_mostrador', 'Mostrador de frutería (1,2 m)', 'mostrador', 'FIXED', 130, 'madera', 'suelo', [
    caja(1.2, 0.9, 0.58, y=0.45, z=-0.02, c='#e8e0cc'), caja(1.22, 0.05, 0.66, y=0.925, z=0.0, c='#b88a58'), caja(1.14, 0.55, 0.012, y=0.5, z=0.27, c=VERDE_F),
    caja(1.2, 0.08, 0.012, y=0.04, z=0.27, c=DARK), caja(0.5, 0.1, 0.012, y=0.82, z=0.27, c='#d8d2c0')],
    motivo_fijo='estructural', superficies=[sup(0.95, 0.04)], nota='mostrador de madera con el frente verde: la balanza, la caja y las bolsas')
obj('fru_rollo_bolsas', 'Soporte de bolsas de papel y rollo', 'papel', 'PICKUP', 0.8, 'papel', 'superficie', [
    caja(0.2, 0.02, 0.14, y=0.01, c='#8a9096', m='metal'), caja(0.02, 0.26, 0.02, x=-0.08, y=0.15, c='#8a9096', m='metal'), caja(0.02, 0.26, 0.02, x=0.08, y=0.15, c='#8a9096', m='metal'),
    cil(0.05, 0.05, 0.14, y=0.27, c='#c9a46e', m='papel', r=[0, 0, 90], seg=8)])
obj('fru_cuenco_muestra', 'Cuenco de fruta de muestra', 'alimento', 'PICKUP', 1.4, 'comida', 'superficie', [
    cil(0.12, 0.08, 0.07, y=0.035, c='#c8a878', m='madera', seg=12), esf(0.04, -0.05, 0.1, 0.02, c='#c0302a'), esf(0.04, 0.05, 0.1, -0.02, c='#f08a20'), esf(0.035, 0.0, 0.14, 0.0, c='#9ab83a')])
obj('fru_cestillo_cambio', 'Cestillo de mimbre para el cambio', 'recipiente', 'PICKUP', 0.5, 'madera', 'superficie', [
    cil(0.08, 0.06, 0.04, y=0.02, c='#c8a878', m='madera', seg=8), cil(0.06, 0.06, 0.006, y=0.043, c='#d8d0c0', m='tela', seg=8)])

# ---- stands for crates: stepped (three steps of 32 cm), a low island, a table with an awning
def expositor_escalonado(id, nombre, ancho, c, c2):
    tiers = [(0.45, 0.64), (0.7, 0.32), (0.95, 0.0)]
    P = []
    for top, z0 in tiers:
        P += [caja(ancho, top - 0.1, 0.32, y=0.1 + (top - 0.1) / 2, z=z0 + 0.16, c=c), caja(ancho + 0.02, 0.03, 0.34, y=top - 0.015, z=z0 + 0.16, c=c2)]
    P += [caja(ancho, 0.1, 0.96, y=0.05, z=0.48, c=oscuro(c, 0.6))]
    obj(id, nombre, 'mueble', 'FIXED', 70, 'madera', 'suelo', P, motivo_fijo=FIJO, superficies=[sup(0.45, 0.02), sup(0.7, 0.02), sup(0.95, 0.02)], nota='tres escalones de 32 cm para cajones de fruta y verdura')
expositor_escalonado('fru_expositor_escalonado', 'Expositor escalonado de madera (1,4 m)', 1.4, '#7a5a38', '#a88a60')
expositor_escalonado('fru_expositor_escalonado_verde', 'Expositor escalonado verde (1,4 m)', 1.4, '#3a6a3a', '#a88a60')
obj('fru_isla_central', 'Isla de exposición a dos alturas', 'mesa', 'PUSH', 45, 'madera', 'suelo', [
    caja(1.2, 0.05, 0.8, y=0.775, z=0.0, c='#a88a60')] + [caja(0.05, 0.75, 0.05, x=sx * 0.55, y=0.375, z=sz * 0.35, c='#5a3a20') for sx in (-1, 1) for sz in (-1, 1)] + [caja(1.1, 0.03, 0.7, y=0.28, z=0.0, c='#8a6a40')],
    superficies=[sup(0.8, 0.04), sup(0.295, 0.04)], nota='mesa de madera con balda baja')
def toldo(id, nombre, c1, c2):
    P = []
    for k in range(6):
        P.append(caja(0.215, 0.02, 0.62, x=-0.54 + k * 0.216, y=2.25, z=0.34, c=c1 if k % 2 else c2, m='tela', r=[22, 0, 0]))
    P += [caja(1.3, 0.04, 0.03, y=2.26 + 0.12 * 0 - 0.0, z=0.02, c='#5a3a20'), caja(1.3, 0.14, 0.012, y=2.14, z=0.64, c=c1, m='tela')]
    obj(id, nombre, 'textil', 'FIXED', 3.5, 'tela', 'pared', P, motivo_fijo=FIJO, nota='toldillo de rayas sobre los cajones')
toldo('fru_toldo_verde', 'Toldillo a rayas verdes y blancas', '#f2efe6', '#3a8a4a')
toldo('fru_toldo_rojo', 'Toldillo a rayas rojas y blancas', '#f2efe6', '#c0302a')

# ---- hanging things: a banana stand, garlic strings, a basket shelf
obj('fru_colgador_platanos', 'Colgador de plátanos con un racimo', 'tb_producto_hogar', 'CARRY', 9, 'comida', 'suelo', [
    cil(0.22, 0.22, 0.03, y=0.015, c='#5a3a20', m='madera', seg=12), cil(0.025, 0.025, 1.7, y=0.86, c='#5a3a20', m='madera', seg=8), caja(0.5, 0.025, 0.025, y=1.72, c='#5a3a20', m='madera'),
    cil(0.012, 0.012, 0.1, x=0.15, y=1.66, c='#8a9096', m='metal', seg=6)] + [cil(0.02, 0.015, 0.2, x=0.15 + (k - 2) * 0.03, y=1.5 - 0.02 * abs(k - 2), z=(k % 2) * 0.03, c='#f2d040' if k % 2 else '#e8c030', m='comida', r=[0, 0, (k - 2) * 7], seg=6) for k in range(5)] + [
    cil(0.02, 0.015, 0.2, x=0.15 + (k - 1.5) * 0.03, y=1.28, z=0.05 - (k % 2) * 0.03, c='#f2d040', m='comida', r=[0, 0, (k - 1.5) * 8], seg=6) for k in range(4)] + [
    cil(0.012, 0.012, 0.1, x=-0.15, y=1.66, c='#8a9096', m='metal', seg=6), caja(0.03, 0.04, 0.03, x=0.15, y=1.74, c='#4a7a2a', m='comida')],
    nota='el racimo de plátanos, colgado de un gancho; el otro gancho, libre')
obj('fru_ristra_ajos', 'Ristras de ajos colgadas', 'tb_producto_hogar', 'PICKUP', 2.4, 'comida', 'pared', [
    cil(0.012, 0.012, 0.4, y=1.8, z=0.04, c='#5a3a20', m='madera', seg=6)] + [esf(0.04, 0.0, 1.65 - k * 0.07, 0.04 + (k % 2) * 0.01, c='#efe8dc') for k in range(5)] + [esf(0.04, 0.12, 1.7 - k * 0.07, 0.04 - (k % 2) * 0.01, c='#e8dccb') for k in range(4)] + [
    cil(0.01, 0.01, 0.4, x=0.06, y=1.8, z=0.04, c='#5a3a20', m='madera', r=[0, 0, 90], seg=6)], nota='ristras de ajos y de pimientos secos para el escaparate')
obj('fru_ristra_pimientos', 'Ristras de pimientos secos colgadas', 'tb_producto_hogar', 'PICKUP', 2.8, 'comida', 'pared', [
    cil(0.012, 0.012, 0.5, y=1.9, z=0.04, c='#5a3a20', m='madera', r=[0, 0, 90], seg=6)] + [p for x in (-0.15, 0.0, 0.15) for k in range(4) for p in (cil(0.03, 0.02, 0.1, x=x, y=1.78 - k * 0.1, z=0.04, c='#9a1f1a', m='comida', seg=6),)], nota='ristras de pimientos secos')
obj('fru_estante_cestas', 'Estante de pared con cestas de mimbre', 'estanteria', 'FIXED', 12, 'madera', 'pared', [
    caja(1.2, 0.03, 0.3, y=1.2, z=0.15, c='#7a5a38'), caja(1.2, 0.03, 0.3, y=1.7, z=0.15, c='#7a5a38'), caja(1.2, 0.55, 0.012, y=1.45, z=0.006, c='#a88a60')] + [
    p for y in (1.215, 1.715) for x in (-0.4, 0.0, 0.4) for p in (cil(0.13, 0.1, 0.12, x=x, y=y + 0.06, z=0.15, c='#c8a878', m='madera', seg=12), esf(0.05, x - 0.03, y + 0.13, 0.15, c=['#f08a20', '#c0302a', '#9ab83a'][int(x * 5 + 2) % 3]))],
    motivo_fijo=FIJO, superficies=[])

# ---- sacks and baskets on the floor
def saco(id, nombre, c, c2, etq, masa=20):
    P = [caja(0.38, 0.5, 0.22, y=0.25, c=c, m='tela'), esf(1.0, 0, 0.5, 0, c=c, m='tela', s=[0.19, 0.09, 0.11]), caja(0.3, 0.2, 0.012, y=0.3, z=0.116, c=etq, m='papel'), caja(0.12, 0.08, 0.012, y=0.3, z=0.123, c=c2, m='papel'),
         caja(0.4, 0.02, 0.24, y=0.01, c=oscuro(c, 0.8), m='tela')]
    obj(id, nombre, 'tb_saco', None, masa, 'tela', 'suelo', P)
saco('fru_saco_patatas', 'Saco de patatas', '#b08a5a', '#8a5a2a', '#efe6d4')
saco('fru_saco_cebollas', 'Saco de cebollas', '#c8a060', '#c0302a', '#efe6d4')
saco('fru_saco_naranjas', 'Saco de naranjas de zumo', '#e0a040', '#f08a20', '#efe6d4')
saco('fru_saco_zanahorias', 'Saco de zanahorias', '#c89a60', '#e0782a', '#efe6d4')
obj('fru_pila_sacos', 'Pila de sacos de patatas y cebollas', 'tb_pila_producto', None, 70, 'tela', 'suelo', [
    p for k in range(2) for j in range(2) for p in (caja(0.38, 0.4, 0.5, x=(k - 0.5) * 0.4, y=0.2 + 0.0, z=(j - 0.5) * 0.52, c=['#b08a5a', '#c8a060'][(k + j) % 2], m='tela'), esf(1.0, (k - 0.5) * 0.4, 0.4, (j - 0.5) * 0.52, c=['#b08a5a', '#c8a060'][(k + j) % 2], m='tela', s=[0.19, 0.06, 0.25]))] + [
    caja(0.38, 0.4, 0.5, x=0.0, y=0.62, z=0.0, c='#b08a5a', m='tela'), caja(0.3, 0.12, 0.012, x=0.0, y=0.62, z=0.256, c='#efe6d4', m='papel')], nota='sacos apilados junto a la puerta')
def cesta_mimbre(id, nombre, col, r, forma='esfera'):
    P = [cil(0.27, 0.22, 0.28, y=0.14, c='#c8a878', m='madera', seg=12), cil(0.28, 0.28, 0.02, y=0.29, c='#a88a60', m='madera', seg=12), cil(0.012, 0.012, 0.56, y=0.35, c='#a88a60', m='madera', r=[0, 0, 90], seg=6)]
    P += [esf(r, (i % 3 - 1) * r * 1.9, 0.29 + r * 0.8 + (i // 3) * r * 1.5, ((i // 3) % 2 - 0.5) * r * 1.8, c=col[i % len(col)], m='comida') for i in range(7)]
    obj(id, nombre, 'alimento', 'CARRY', 9, 'madera', 'suelo', P)
cesta_mimbre('fru_cesta_naranjas', 'Cesta de mimbre con naranjas', ['#f08a20', '#e87a18'], 0.065)
cesta_mimbre('fru_cesta_manzanas', 'Cesta de mimbre con manzanas', ['#c0302a', '#9ab83a', '#d8c040'], 0.062)
cesta_mimbre('fru_cesta_limones', 'Cesta de mimbre con limones', ['#f2e04a'], 0.055)
obj('fru_sandias_pila', 'Montón de sandías', 'tb_pila_producto', None, 55, 'comida', 'suelo', [
    caja(0.9, 0.12, 0.9, y=0.06, c='#a88a60', m='madera')] + [esf(0.19, (i % 2 - 0.5) * 0.4, 0.12 + 0.17, (i // 2 - 0.5) * 0.4, c=['#3a7a3a', '#2f6a30'][i % 2], m='comida', s=[1, 0.9, 1.1]) for i in range(4)] + [esf(0.18, 0.0, 0.12 + 0.17 + 0.28, 0.0, c='#4a8a4a', m='comida', s=[1, 0.9, 1.1])],
    nota='sandías a pie de calle')

# ---- the produce: crates 0.36 x 0.28 with a mound of fruit
def cajon(id, nombre, col, forma, n=6, r=0.04, col2=None, sy=1.0):
    P = [caja(0.36, 0.13, 0.28, y=0.065, c=CAJA_M, m='madera'), caja(0.375, 0.02, 0.295, y=0.14, c=CAJA_M2, m='madera'), esf(1.0, 0, 0.145, 0, c=col, m='comida', s=[0.17, 0.05, 0.125])]
    pos = [(-0.095, -0.05), (0.0, 0.065), (0.095, -0.05), (0.0, -0.07), (-0.1, 0.07), (0.1, 0.07), (-0.045, 0.0), (0.05, 0.005)][:n]
    for i, (x, z) in enumerate(pos):
        c = col2 if col2 and i % 2 else col
        if forma == 'esfera': P.append(esf(r, x, 0.15 + r * sy * 0.6, z, c=c, m='comida', s=[1, sy, 1]))
        elif forma == 'pera': P += [esf(r, x, 0.15 + r * 0.9, z, c=c, m='comida', s=[1, 1.05, 1]), esf(r * 0.62, x, 0.15 + r * 2.0, z, c=c, m='comida')]
        elif forma == 'barra': P.append(cil(r, r * 0.9, 0.17, x=x * 0.2, y=0.15 + r + (i % 3) * r * 1.9, z=z * 1.3, c=c, m='comida', r=[0, 0, 90], seg=6))
        elif forma == 'cono': P.append({**cono(r, 0.16, x=x * 0.3, y=0.15 + r + (i % 3) * r * 1.8, z=z * 1.4, c=c, m='comida', seg=6), 'r': [0, 0, 90]})
        elif forma == 'caja': P.append(caja(r * 1.6, r * 1.8, r * 1.6, x=x, y=0.15 + r * 0.9, z=z, c=c, m='comida'))
        elif forma == 'hoja': P.append(esf(r, x, 0.15 + r * 0.6, z, c=c, m='comida', s=[1.0, 0.7, 1.0]))
        elif forma == 'haz': P.append(cil(r, r, 0.2, x=x * 0.2, y=0.15 + r + (i % 3) * r * 2, z=z * 1.2, c=c, m='comida', r=[0, 0, 90], seg=5))
        elif forma == 'pina': P += [cil(r, r, r * 2.4, x=x * 1.2, y=0.15 + r * 1.2, z=z, c=c, m='comida', seg=6), cono(r * 0.7, r * 1.2, x=x * 1.2, y=0.15 + r * 2.4 + r * 0.6, z=z, c='#4a7a2a', m='comida', seg=6)]
    obj(id, nombre, 'alimento', 'CARRY', 8.5, 'comida', 'superficie', P)
FRUTAS = [
    ('pera_conferencia', 'Cajón de peras conferencia', '#b8b04a', 'pera', 5, 0.034, None), ('pera_limonera', 'Cajón de peras limoneras', '#e0d060', 'pera', 5, 0.034, None),
    ('ciruela_roja', 'Cajón de ciruelas rojas', '#8a2a4a', 'esfera', 8, 0.026, '#a03a5a'), ('ciruela_amarilla', 'Cajón de ciruelas amarillas', '#e8c84a', 'esfera', 8, 0.026, '#d8b030'),
    ('cerezas', 'Cajón de cerezas del Jerte', '#8a1a2a', 'esfera', 8, 0.022, '#a82a3a'), ('fresas', 'Cajón de fresas', '#d02a3a', 'cono', 8, 0.024, '#e0443a'),
    ('kiwi', 'Cajón de kiwis', '#8a7a3a', 'esfera', 6, 0.032, '#9a8a4a'), ('pina', 'Cajón de piñas', '#e0b83a', 'pina', 3, 0.05, '#d8a830'),
    ('aguacate', 'Cajón de aguacates', '#3a4a2a', 'pera', 5, 0.034, '#4a5a30'), ('higos', 'Cajón de higos', '#5a2a5a', 'pera', 6, 0.028, '#6a3a6a'),
    ('granadas', 'Cajón de granadas', '#b3342a', 'esfera', 5, 0.04, '#a02a22'), ('mandarinas', 'Cajón de mandarinas', '#f08a20', 'esfera', 8, 0.032, '#f29a30'),
    ('pomelos', 'Cajón de pomelos', '#f0c050', 'esfera', 4, 0.052, '#e8a060'), ('uva_verde', 'Cajón de uva blanca', '#b8d06a', 'esfera', 8, 0.02, '#a8c05a'),
    ('uva_negra', 'Cajón de uva negra', '#3a1a4a', 'esfera', 8, 0.02, '#4a2a5a'), ('nectarinas', 'Cajón de nectarinas', '#e8643a', 'esfera', 6, 0.036, '#f08a3a'),
    ('albaricoques', 'Cajón de albaricoques', '#f0a040', 'esfera', 8, 0.028, '#e8903a'), ('caquis', 'Cajón de caquis', '#e87a2a', 'esfera', 6, 0.04, '#e0661e'),
    ('manzana_golden', 'Cajón de manzanas golden', '#d8c040', 'esfera', 6, 0.038, '#c8b030'), ('manzana_fuji', 'Cajón de manzanas fuji', '#c8584a', 'esfera', 6, 0.038, '#d8786a'),
    ('platano_canario', 'Cajón de plátanos de Canarias', '#e8c030', 'barra', 6, 0.024, '#f0d040'), ('mango', 'Cajón de mangos', '#e07a3a', 'pera', 4, 0.045, '#c8a03a'),
    ('coco', 'Cajón de cocos', '#6a4a2a', 'esfera', 4, 0.048, '#5a3a20'), ('membrillo', 'Cajón de membrillos', '#d8c04a', 'pera', 5, 0.038, '#c8b040'),
    ('naranja_zumo', 'Cajón de naranjas de zumo', '#f08a20', 'esfera', 8, 0.034, '#e87818'), ('limon_verna', 'Cajón de limones verna', '#f2e04a', 'esfera', 8, 0.03, '#e8d03a', 0.85),
    ('melon_piel_sapo', 'Cajón de melones piel de sapo', '#8aa05a', 'esfera', 3, 0.075, '#7a9050', 0.85), ('melon_amarillo', 'Cajón de melones amarillos', '#e8d060', 'esfera', 3, 0.075, '#d8c050', 0.85),
    ('sandia_mini', 'Cajón de sandías mini', '#3a7a3a', 'esfera', 3, 0.08, '#2f6a30', 0.9),
]
VERDURAS = [
    ('calabacin', 'Cajón de calabacines', '#4a7a2a', 'barra', 6, 0.03, '#3a6a22'), ('berenjena', 'Cajón de berenjenas', '#3a1a4a', 'barra', 6, 0.036, '#4a2a5a'),
    ('pepino', 'Cajón de pepinos', '#3a8a3a', 'barra', 6, 0.026, '#2f7a30'), ('judias_verdes', 'Cajón de judías verdes', '#5a9a3a', 'haz', 8, 0.012, '#4a8a30'),
    ('coliflor', 'Cajón de coliflores', '#eee8d8', 'esfera', 3, 0.085, '#e0dac8', 0.9), ('brocoli', 'Cajón de brócoli', '#3a6a2a', 'hoja', 5, 0.065, '#4a7a30'),
    ('repollo', 'Cajón de repollos', '#7aa04a', 'esfera', 3, 0.09, '#6a9040', 0.9), ('lombarda', 'Cajón de lombardas', '#7a2a6a', 'esfera', 3, 0.09, '#6a1a5a', 0.9),
    ('esparragos', 'Cajón de espárragos trigueros', '#5a7a2a', 'haz', 8, 0.012, '#4a6a22'), ('champinones', 'Cajón de champiñones', '#e8dfd0', 'hoja', 8, 0.034, '#d8cfc0'),
    ('setas', 'Cajón de setas de cardo', '#b8a88a', 'hoja', 6, 0.04, '#a89878'), ('remolacha', 'Cajón de remolachas', '#6a1a3a', 'esfera', 6, 0.04, '#7a2a4a'),
    ('puerros', 'Cajón de puerros', '#e8efdc', 'haz', 8, 0.018, '#6a9a3a'), ('calabaza', 'Cajón de calabazas', '#e08a2a', 'esfera', 3, 0.08, '#d87a1e', 0.75),
    ('boniato', 'Cajón de boniatos', '#a8603a', 'barra', 6, 0.034, '#98502a'), ('espinacas', 'Cajón de espinacas', '#2f6a2a', 'hoja', 6, 0.06, '#3a7a30'),
    ('acelgas', 'Cajón de acelgas', '#3f7a35', 'hoja', 6, 0.06, '#e8efdc'), ('rabanitos', 'Cajón de rabanitos', '#c8203a', 'esfera', 8, 0.024, '#d8304a'),
    ('apio', 'Cajón de apio', '#a8c870', 'haz', 6, 0.024, '#98b860'), ('alcachofas', 'Cajón de alcachofas', '#7a8a4a', 'pera', 6, 0.036, '#6a7a3a'),
    ('mazorcas', 'Cajón de mazorcas de maíz', '#e8c040', 'barra', 6, 0.03, '#d8b030'), ('guisantes', 'Cajón de guisantes en vaina', '#6aa04a', 'haz', 8, 0.014, '#5a9040'),
    ('pimiento_verde', 'Cajón de pimientos verdes', '#3a8a3a', 'caja', 6, 0.036, '#2f7a30'), ('pimiento_amarillo', 'Cajón de pimientos amarillos', '#e8c030', 'caja', 6, 0.036, '#f0d040'),
    ('guindillas', 'Cajón de guindillas', '#c0302a', 'haz', 8, 0.01, '#3a8a3a'), ('perejil', 'Manojos de perejil', '#2f7a2a', 'hoja', 6, 0.05, '#3a8a30'),
    ('ajos', 'Cajón de cabezas de ajo', '#efe8dc', 'esfera', 8, 0.034, '#e0d8c8'), ('cebolla_roja', 'Cajón de cebollas rojas', '#8a2a4a', 'esfera', 6, 0.042, '#9a3a5a'),
    ('cebolleta', 'Cajón de cebolletas', '#e8efdc', 'haz', 8, 0.016, '#6a9a3a'), ('patata_roja', 'Cajón de patatas rojas', '#a83a3a', 'esfera', 6, 0.042, '#983030', 0.75),
    ('patata_nueva', 'Cajón de patatas nuevas', '#d8b878', 'esfera', 6, 0.04, '#c8a868', 0.75), ('tomate_pera', 'Cajón de tomates pera', '#d8382a', 'pera', 6, 0.03, '#c8281a'),
    ('tomate_cherry', 'Cajón de tomates cherry', '#e0382a', 'esfera', 8, 0.022, '#d02a1a'), ('tomate_raf', 'Cajón de tomates raf', '#b8452a', 'esfera', 4, 0.055, '#a8351a', 0.8),
    ('lechuga_romana', 'Cajón de lechugas romanas', '#6aa040', 'hoja', 5, 0.062, '#7ab050'), ('lechuga_iceberg', 'Cajón de lechugas iceberg', '#a8d070', 'esfera', 4, 0.06, '#98c060', 0.9),
    ('endivias', 'Cajón de endivias', '#f0efc8', 'pera', 8, 0.026, '#e8e8b8'), ('canonigos', 'Bandejas de canónigos', '#3a7a30', 'hoja', 6, 0.05, '#4a8a3a'),
    ('rucula', 'Bandejas de rúcula', '#2f7a2a', 'hoja', 6, 0.05, '#3a8a30'), ('jengibre', 'Cajón de jengibre', '#c8a070', 'barra', 6, 0.03, '#b89060'),
]
for t in FRUTAS + VERDURAS:
    k, n_, col, forma, n, r, col2 = t[:7]
    cajon('fru_caja_' + k, n_, col, forma, n, r, col2, t[7] if len(t) > 7 else 1.0)

# ---- price boards, sign, poster
for k, (lin, titulo) in {'a': (['Melocotón  2,49', 'Cerezas  5,90', 'Sandía  0,69', 'Melón  1,19', 'Higos  4,50', 'Uvas  2,95'], 'frutas'), 'b': (['Tomate  1,99', 'Patatas  0,89', 'Cebolla  1,10', 'Pimientos  2,45', 'Judías  3,20', 'Calabacín  1,60'], 'verduras')}.items():
    obj('fru_pizarra_' + k, 'Pizarra de precios de %s' % titulo, 'decoracion', 'PICKUP', 3, 'madera', 'pared', [
        caja(0.9, 0.62, 0.03, y=1.65, z=0.015, c='#5a3a20'), plano(0.84, 0.56, y=1.65, z=0.033, tex={'tipo': 'pizarra', 'lineas': lin})])
obj('fru_rotulo', 'Rótulo interior de la frutería', 'decoracion', 'PICKUP', 3, 'madera', 'pared', [
    caja(1.3, 0.34, 0.03, y=2.55, z=0.015, c='#2a2a2e'), plano(1.24, 0.28, y=2.55, z=0.033, tex={'tipo': 'rotulo_tb', 'estilo': 'fruteria', 'rotulo_local': True})])
obj('fru_cartel_fruta', 'Cartel de fruta de temporada', 'cuadro', 'PICKUP', 1.2, 'papel', 'pared', [
    caja(0.5, 0.7, 0.025, y=1.7, z=0.0125, c='#2a2420'), plano(0.44, 0.64, y=1.7, z=0.027, tex={'tipo': 'cartel_tb', 'dibujo': 'fruta'})])
obj('fru_carro_cajas', 'Carro con cajones apilados', 'tb_pila_producto', None, 48, 'madera', 'suelo', [
    caja(0.6, 0.05, 0.9, y=0.15, c='#5a626a', m='metal'), caja(0.05, 1.1, 0.05, x=-0.28, y=0.65, z=-0.4, c='#5a626a', m='metal'), caja(0.05, 1.1, 0.05, x=0.28, y=0.65, z=-0.4, c='#5a626a', m='metal'),
    caja(0.58, 0.05, 0.05, y=1.2, z=-0.4, c='#5a626a', m='metal')] + [cil(0.07, 0.07, 0.04, x=sx * 0.27, y=0.07, z=sz * 0.38, c=DARK, m='goma', r=[0, 0, 90], seg=8) for sx in (-1, 1) for sz in (-1, 1)] + [
    caja(0.42, 0.14, 0.5, y=0.24 + k * 0.145, z=0.1, c=CAJA_M, m='madera') for k in range(5)], nota='para llevar los cajones al almacén')
