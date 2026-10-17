# The household-appliance and electronics shop's objects (family «tiendas_b»): fridges and freezers, washing machines and
# dishwashers, cookers, TVs on the wall and on plinths, small appliances in their boxes, fans, radios, lamps, headphones and
# chargers, the counter and the storeroom's cartons. Ids start with «ele_». No real brand: invented names, plain colours.
from tb_base import *

BLANCO_E, INOX, NEGRO_E = '#eceae6', '#b9bec2', '#34343a'
PANT = '#2a2e38'

# ---- the counter and the fixtures
obj('ele_mostrador', 'Mostrador de electrodomésticos (1,2 m)', 'mostrador', 'FIXED', 140, 'madera', 'suelo', [
    caja(1.2, 0.95, 0.62, y=0.475, z=-0.02, c='#dcdfe2'), caja(1.22, 0.04, 0.68, y=0.97, z=0.0, c='#34383e'), caja(1.14, 0.55, 0.012, y=0.5, z=0.29, c='#1f4e8c'),
    caja(1.2, 0.08, 0.012, y=0.04, z=0.29, c=DARK), caja(0.5, 0.1, 0.012, y=0.84, z=0.29, c='#d6d9db')],
    motivo_fijo='estructural', superficies=[sup(0.99, 0.04)], nota='mostrador de azul y gris: la caja, el catálogo y los cargadores')
obj('ele_catalogo', 'Catálogo de ofertas', 'papel', 'PICKUP', 0.6, 'papel', 'superficie', [
    caja(0.22, 0.02, 0.3, y=0.01, c='#1f4e8c', m='papel'), caja(0.2, 0.004, 0.28, y=0.022, c='#f2efe6', m='papel')])
obj('ele_plinto_tv', 'Plinto bajo para pantallas (1,4 m)', 'mueble', 'PUSH', 38, 'madera', 'suelo', [
    caja(1.4, 0.4, 0.6, y=0.2, c='#2a2e38'), caja(1.42, 0.03, 0.62, y=0.415, c='#4a4e58')], superficies=[sup(0.43, 0.06)], nota='una peana baja donde se apoyan los televisores de sobremesa')
obj('ele_isla_pequenos', 'Isla de pequeños electrodomésticos (1,2 m)', 'mesa', 'PUSH', 42, 'madera', 'suelo', [
    caja(1.2, 0.05, 0.7, y=0.875, c='#e9eaec')] + [caja(0.05, 0.85, 0.05, x=sx * 0.55, y=0.425, z=sz * 0.3, c='#5a626a', m='metal') for sx in (-1, 1) for sz in (-1, 1)] + [caja(1.1, 0.03, 0.6, y=0.3, c='#d8dadc')],
    superficies=[sup(0.9, 0.05), sup(0.315, 0.05)])
estantes('ele_estanteria_pequenos', 'Estantería de pequeños electrodomésticos (1 m)', 1.0, 0.46, [0.35, 0.7, 1.05, 1.4, 1.75], 1.95, c='#dadde0', cp='#f2f4f4', masa=55, nota='baldas de 43 cm para las cajas')
estantes('ele_estanteria_baja', 'Estantería baja de accesorios (1 m)', 1.0, 0.4, [0.3, 0.6, 0.9, 1.2], 1.3, c='#dadde0', cp='#f2f4f4', masa=40)
obj('ele_rotulo', 'Rótulo interior de la tienda', 'decoracion', 'PICKUP', 3, 'madera', 'pared', [
    caja(1.3, 0.34, 0.03, y=2.6, z=0.015, c='#1f1f24'), plano(1.24, 0.28, y=2.6, z=0.033, tex={'tipo': 'rotulo_tb', 'estilo': 'electro', 'rotulo_local': True})])
for k, (n_, d1) in {'nevera': ('Cartel de frigoríficos', 'nevera'), 'lavadora': ('Cartel de lavadoras', 'lavadora'), 'tv': ('Cartel de televisores', 'tv')}.items():
    obj('ele_cartel_' + k, n_, 'cuadro', 'PICKUP', 1.2, 'papel', 'pared', [
        caja(0.5, 0.7, 0.025, y=1.7, z=0.0125, c='#2a2420'), plano(0.44, 0.64, y=1.7, z=0.027, tex={'tipo': 'cartel_tb', 'dibujo': d1})])
obj('ele_pantalla_ofertas', 'Pantalla de ofertas del mes', 'pantalla', 'FIXED', 8, 'plastico', 'pared', [
    caja(0.9, 0.52, 0.05, y=2.2, z=0.025, c=PANT, m='plastico'), plano(0.84, 0.47, y=2.2, z=0.052, tex={'tipo': 'pantalla_tb', 'estilo': 'precios'}, luz=True)], motivo_fijo=FIJO)

# ---- cold: fridges and freezers (a body, a door line, handles, feet)
def frigo(id, nombre, c, w=0.6, h=1.85, d=0.65, puertas=2, altura_sup=0.0, masa=70, cat='nevera'):
    P = [caja(w, h - 0.03, d, y=0.03 + (h - 0.03) / 2, z=d / 2 - 0.0, c=c, m='metal' if c in (INOX,) else 'plastico'), caja(w - 0.04, 0.03, d - 0.04, y=0.015, z=d / 2, c=oscuro(c, 0.5), m='plastico')]
    if puertas == 2:
        y1 = h * 0.62
        P += [caja(w - 0.02, 0.01, 0.01, y=y1, z=d + 0.002, c=oscuro(c, 0.55), m='metal'), caja(0.02, h * 0.28, 0.03, x=w / 2 - 0.07, y=y1 + h * 0.18, z=d + 0.025, c=STEEL, m='metal'), caja(0.02, h * 0.3, 0.03, x=w / 2 - 0.07, y=y1 - h * 0.22, z=d + 0.025, c=STEEL, m='metal')]
    elif puertas == 1:
        P += [caja(0.02, h * 0.4, 0.03, x=w / 2 - 0.07, y=h * 0.55, z=d + 0.025, c=STEEL, m='metal')]
    P += [caja(0.12, 0.05, 0.006, x=-0.12, y=h * 0.9, z=d + 0.004, c='#d8dde0', m='plastico')] if puertas == 2 else []
    obj(id, nombre, cat, None, masa, 'metal', 'suelo', P, nota='con su línea de puerta y sus tiradores')
frigo('ele_frigorifico_combi_blanco', 'Frigorífico combi blanco', BLANCO_E)
frigo('ele_frigorifico_combi_inox', 'Frigorífico combi inox', INOX, 0.6, 1.9, 0.68)
frigo('ele_frigorifico_combi_negro', 'Frigorífico combi negro', NEGRO_E, 0.6, 1.85, 0.66)
frigo('ele_frigorifico_dos_puertas', 'Frigorífico de dos puertas, 1,7 m', BLANCO_E, 0.7, 1.7, 0.68, masa=82)
frigo('ele_frigorifico_americano', 'Frigorífico americano de dos puertas', INOX, 0.9, 1.78, 0.72, puertas=1, masa=118)
frigo('ele_congelador_vertical', 'Congelador vertical', BLANCO_E, 0.6, 1.4, 0.62, puertas=1, masa=58)
frigo('ele_frigorifico_bajo', 'Frigorífico bajo encimera', BLANCO_E, 0.6, 0.85, 0.58, puertas=1, masa=42)
obj('ele_arcon_congelador', 'Arcón congelador', 'nevera', 'PUSH', 58, 'metal', 'suelo', [
    caja(1.0, 0.8, 0.62, y=0.4, z=0.31, c=BLANCO_E, m='plastico'), caja(1.02, 0.05, 0.64, y=0.825, z=0.31, c='#d8dde0', m='plastico'), caja(0.06, 0.04, 0.03, x=0.4, y=0.84, z=0.6, c='#8a9096', m='metal'), caja(0.1, 0.06, 0.004, x=-0.4, y=0.5, z=0.622, c='#7fe07f', m='plastico', luz=True)],
    superficies=[sup(0.85, 0.06)], nota='con la tapa llana: sirve de expositor')

# ---- washing: front loaders, dryers, dishwashers
def lavadora(id, nombre, c, tipo='frontal'):
    w, h, d = (0.6, 0.85, 0.6) if tipo != 'superior' else (0.4, 0.9, 0.6)
    P = [caja(w, h - 0.02, d, y=0.02 + (h - 0.02) / 2, z=d / 2, c=c, m='plastico'), caja(w - 0.04, 0.02, d - 0.04, y=0.01, z=d / 2, c=oscuro(c, 0.5), m='plastico')]
    if tipo == 'frontal':
        P += [cil(0.22, 0.22, 0.04, y=0.42, z=d + 0.01, c='#7a8a96', m='plastico', r=[90, 0, 0], seg=16), cil(0.18, 0.18, 0.045, y=0.42, z=d + 0.012, c=GLASS, m='cristal', r=[90, 0, 0], seg=16),
              caja(0.5, 0.08, 0.01, y=0.8, z=d + 0.004, c=oscuro(c, 0.85), m='plastico'), cil(0.03, 0.03, 0.02, x=0.18, y=0.8, z=d + 0.012, c=STEEL, m='metal', r=[90, 0, 0], seg=8), caja(0.12, 0.03, 0.004, x=-0.12, y=0.8, z=d + 0.01, c='#7fe0ff', m='plastico', luz=True)]
    elif tipo == 'superior':
        P += [caja(w - 0.04, 0.03, d - 0.04, y=h + 0.0, z=d / 2, c=oscuro(c, 0.9), m='plastico'), caja(0.3, 0.08, 0.01, y=h - 0.08, z=d + 0.004, c=oscuro(c, 0.85), m='plastico')]
    elif tipo == 'lavavajillas':
        P += [caja(w - 0.06, 0.12, 0.01, y=0.78, z=d + 0.004, c=oscuro(c, 0.8), m='plastico'), caja(0.4, 0.02, 0.03, y=0.7, z=d + 0.02, c=STEEL, m='metal'), caja(0.1, 0.03, 0.004, x=-0.16, y=0.8, z=d + 0.012, c='#7fe0ff', m='plastico', luz=True)]
    obj(id, nombre, 'electrodomestico', None, 72 if tipo == 'frontal' else 48 if tipo == 'superior' else 46, 'metal', 'suelo', P, **({'superficies': [sup(h, 0.06)]} if tipo in ('frontal', 'lavavajillas') else {}))
lavadora('ele_lavadora_blanca', 'Lavadora de carga frontal blanca', BLANCO_E)
lavadora('ele_lavadora_inox', 'Lavadora de carga frontal inox', INOX)
lavadora('ele_lavadora_carga_superior', 'Lavadora de carga superior', BLANCO_E, 'superior')
lavadora('ele_secadora', 'Secadora de condensación', '#e4e6e8')
lavadora('ele_lavasecadora', 'Lavasecadora', '#dfe3e6')
lavadora('ele_lavavajillas_blanco', 'Lavavajillas blanco', BLANCO_E, 'lavavajillas')
lavadora('ele_lavavajillas_inox', 'Lavavajillas inox', INOX, 'lavavajillas')

# ---- cooking
def cocina(id, nombre, c, gas=False):
    P = [caja(0.6, 0.83, 0.6, y=0.415, z=0.3, c=c, m='metal'), caja(0.6, 0.03, 0.6, y=0.845, z=0.3, c='#2e2e34', m='cristal' if not gas else 'metal'), caja(0.5, 0.35, 0.01, y=0.38, z=0.605, c='#3a3a3e', m='cristal'),
         cil(0.01, 0.01, 0.5, y=0.58, z=0.64, c=STEEL, m='metal', r=[0, 0, 90], seg=8), caja(0.56, 0.08, 0.01, y=0.74, z=0.605, c=oscuro(c, 0.8), m='metal')]
    P += [cil(0.015, 0.015, 0.03, x=x, y=0.745, z=0.61, c='#2b2b2e', m='plastico', r=[90, 0, 0], seg=8) for x in (-0.2, -0.07, 0.07, 0.2)]
    if gas: P += [cil(0.07 if i < 2 else 0.05, 0.07 if i < 2 else 0.05, 0.02, x=(i % 2 - 0.5) * 0.28, y=0.87, z=0.18 + (i // 2) * 0.28, c='#3a3a3e', m='metal', seg=12) for i in range(4)]
    else: P += [cil(0.09, 0.09, 0.004, x=(i % 2 - 0.5) * 0.28, y=0.862, z=0.18 + (i // 2) * 0.28, c='#d05a2a', m='plastico', seg=14, luz=False) for i in range(4)]
    obj(id, nombre, 'electrodomestico', None, 52, 'metal', 'suelo', P)
cocina('ele_cocina_vitro', 'Cocina de vitrocerámica', BLANCO_E)
cocina('ele_cocina_inox', 'Cocina de gas inox', INOX, gas=True)
obj('ele_torre_horno', 'Torre con horno y microondas', 'electrodomestico', 'PUSH', 70, 'metal', 'suelo', [
    caja(0.6, 1.9, 0.58, y=0.95, z=0.29, c='#34343a', m='plastico'), caja(0.5, 0.4, 0.01, y=0.7, z=0.585, c='#2a2a2e', m='cristal'), caja(0.5, 0.25, 0.01, y=1.2, z=0.585, c='#2a2a2e', m='cristal'), caja(0.55, 0.06, 0.012, y=0.95, z=0.588, c=oscuro(INOX, 0.9), m='metal'),
    cil(0.01, 0.01, 0.45, y=0.92, z=0.62, c=STEEL, m='metal', r=[0, 0, 90], seg=8), caja(0.12, 0.04, 0.004, x=0.2, y=1.55, z=0.586, c='#f0a040', m='plastico', luz=True), caja(0.4, 0.3, 0.01, y=0.3, z=0.585, c='#2a2a2e', m='plastico')], nota='horno y microondas en columna, con la luz del reloj')
obj('ele_campana_pared', 'Campana extractora de pared', 'electrodomestico', 'FIXED', 20, 'metal', 'pared', [
    caja(0.9, 0.12, 0.5, y=1.95, z=0.25, c=INOX, m='metal'), caja(0.3, 0.55, 0.28, y=2.34, z=0.14, c=INOX, m='metal'), caja(0.5, 0.01, 0.2, y=1.885, z=0.3, c='#fff3d6', m='plastico', luz=True)], motivo_fijo=FIJO)

# ---- TVs: wall-hung, on a plinth; the pictures are painted (landscape, pitch, news, film)
def tele(id, nombre, diag, estilo, pared=True, masa=None):
    w = round(diag * 2.54 * 0.872 / 100, 3); h = round(w * 9 / 16, 3)
    z0 = 0.0
    if pared:
        P = [caja(w, h, 0.04, y=1.55, z=0.02, c=PANT, m='plastico'), plano(w - 0.03, h - 0.03, y=1.55, z=0.042, tex={'tipo': 'pantalla_tb', 'estilo': estilo}, luz=True), caja(0.2, 0.1, 0.01, y=1.55, z=0.005, c='#2a2a2e', m='plastico')]
        obj(id, nombre, 'pantalla', 'FIXED', masa or round(diag * 0.28, 1), 'plastico', 'pared', P, motivo_fijo=FIJO)
    else:
        P = [caja(w, h, 0.04, y=0.12 + h / 2 + 0.03, z=0.0, c=PANT, m='plastico'), plano(w - 0.03, h - 0.03, y=0.15 + h / 2, z=0.022, tex={'tipo': 'pantalla_tb', 'estilo': estilo}, luz=True),
             caja(0.08, 0.1, 0.02, x=-w * 0.35, y=0.06 + 0.0, z=0.0, c='#2e2e32', m='plastico'), caja(0.08, 0.1, 0.02, x=w * 0.35, y=0.06 + 0.0, z=0.0, c='#2e2e32', m='plastico'), caja(0.1, 0.02, 0.2, x=-w * 0.35, y=0.01, z=0.0, c='#2e2e32', m='plastico'), caja(0.1, 0.02, 0.2, x=w * 0.35, y=0.01, z=0.0, c='#2e2e32', m='plastico')]
        obj(id, nombre, 'pantalla', None, masa or round(diag * 0.2, 1), 'plastico', 'superficie', P)
tele('ele_tv_pared_32', 'Televisor de 32 pulgadas colgado', 32, 'noticias')
tele('ele_tv_pared_43', 'Televisor de 43 pulgadas colgado', 43, 'paisaje')
tele('ele_tv_pared_50', 'Televisor de 50 pulgadas colgado', 50, 'futbol')
tele('ele_tv_pared_55', 'Televisor de 55 pulgadas colgado', 55, 'cine')
tele('ele_tv_pared_65', 'Televisor de 65 pulgadas colgado', 65, 'paisaje')
tele('ele_tv_peana_32', 'Televisor de 32 pulgadas con patas', 32, 'futbol', False)
tele('ele_tv_peana_43', 'Televisor de 43 pulgadas con patas', 43, 'cine', False)
tele('ele_tv_peana_50', 'Televisor de 50 pulgadas con patas', 50, 'noticias', False)
obj('ele_pared_pantallas', 'Pared de pantallas encendidas (seis)', 'pantalla', 'FIXED', 20, 'plastico', 'pared', [
    caja(3.7, 1.25, 0.03, y=1.65, z=0.015, c='#20242c')] + [p for i in range(3) for j in range(2) for p in (
        caja(1.1, 0.6, 0.03, x=(i - 1) * 1.2, y=1.35 + j * 0.65, z=0.045, c=PANT, m='plastico'), plano(1.07, 0.57, x=(i - 1) * 1.2, y=1.35 + j * 0.65, z=0.062, c=['#3a6ea5', '#3a8a5a', '#d8a84a', '#8a4a8a', '#c0584a', '#4a8aa8'][i * 2 + j], m='plastico', luz=True))], motivo_fijo=FIJO,
    nota='seis pantallas de colores: el muro de televisores')

# ---- audio, music, headphones, chargers, torches
def peq(id, nombre, masa, P, cat='tb_audio', **k): obj(id, nombre, cat, 'PICKUP', masa, 'plastico', 'superficie', P, **k)
peq('ele_barra_sonido', 'Barra de sonido', 2.6, [caja(0.9, 0.06, 0.1, y=0.03, c='#2e2e34', m='plastico'), caja(0.86, 0.02, 0.004, y=0.035, z=0.052, c='#4a4e58', m='metal'), caja(0.04, 0.012, 0.004, x=0.4, y=0.045, z=0.052, c='#7fe0ff', m='plastico', luz=True)])
peq('ele_altavoz_bluetooth', 'Altavoz bluetooth portátil', 0.9, [cil(0.05, 0.05, 0.16, y=0.05, c='#2c5aa0', m='plastico', r=[0, 0, 90], seg=10), caja(0.06, 0.012, 0.004, y=0.06, z=0.052, c='#e8e8e8', m='plastico')])
peq('ele_altavoz_torre', 'Altavoz de torre', 4.4, [caja(0.22, 0.9, 0.24, y=0.45, c='#3a3a42', m='madera'), cil(0.08, 0.08, 0.01, y=0.65, z=0.125, c='#2a2a2e', m='plastico', r=[90, 0, 0], seg=12), cil(0.05, 0.05, 0.01, y=0.3, z=0.125, c='#2a2a2e', m='plastico', r=[90, 0, 0], seg=12)])
peq('ele_radio_clasica', 'Radio clásica de sobremesa', 2.2, [caja(0.34, 0.2, 0.14, y=0.1, c='#8a5a32', m='madera'), caja(0.12, 0.08, 0.004, x=-0.08, y=0.11, z=0.072, c='#e8d890', m='plastico'), cil(0.025, 0.025, 0.02, x=0.1, y=0.11, z=0.082, c='#d8c070', m='metal', r=[90, 0, 0], seg=8), cil(0.05, 0.05, 0.004, x=0.1, y=0.1, z=0.072, c='#3a2a1a', m='plastico', r=[90, 0, 0], seg=8)])
peq('ele_radio_portatil', 'Radio portátil con asa', 1.1, [caja(0.24, 0.13, 0.07, y=0.065, c='#c0302a', m='plastico'), cil(0.01, 0.01, 0.25, y=0.14, c=STEEL, m='metal', r=[0, 0, 90], seg=6), caja(0.1, 0.04, 0.004, x=-0.04, y=0.08, z=0.036, c='#7fe07f', m='plastico', luz=True)])
peq('ele_radio_despertador', 'Radio despertador', 0.6, [caja(0.2, 0.1, 0.08, y=0.05, c='#2e2e34', m='plastico'), caja(0.1, 0.04, 0.004, y=0.06, z=0.042, c='#ff3b2a', m='plastico', luz=True)])
peq('ele_equipo_musica', 'Minicadena con dos altavoces', 4.8, [caja(0.3, 0.14, 0.26, y=0.07, c='#3a3a42', m='plastico'), caja(0.14, 0.04, 0.004, y=0.1, z=0.132, c='#7fe0ff', m='plastico', luz=True), caja(0.16, 0.26, 0.16, x=-0.28, y=0.13, c='#2e2e34', m='madera'), caja(0.16, 0.26, 0.16, x=0.28, y=0.13, c='#2e2e34', m='madera')], cat='tb_audio')
obj('ele_auriculares_exp', 'Expositor de auriculares', 'tb_accesorio', 'PICKUP', 2.4, 'plastico', 'superficie', [
    caja(0.4, 0.02, 0.24, y=0.01, c='#2e2e34', m='plastico'), caja(0.4, 0.34, 0.02, y=0.19, z=-0.1, c='#1f4e8c', m='plastico')] + [p for i, c in enumerate(['#2e2e34', '#c0302a', '#e8e4d8', '#2c5aa0']) for p in (
    caja(0.1, 0.03, 0.03, x=-0.15 + i * 0.1, y=0.3, z=-0.07, c=c, m='plastico'), caja(0.03, 0.1, 0.03, x=-0.19 + i * 0.1, y=0.23, z=-0.07, c=c, m='plastico'), caja(0.03, 0.1, 0.03, x=-0.11 + i * 0.1, y=0.23, z=-0.07, c=c, m='plastico'))], nota='a la venta junto a la caja')
obj('ele_cargadores_exp', 'Expositor de cargadores y cables', 'tb_accesorio', 'PICKUP', 1.4, 'plastico', 'superficie', [
    caja(0.36, 0.02, 0.2, y=0.01, c='#2e2e34', m='plastico'), caja(0.36, 0.26, 0.02, y=0.15, z=-0.09, c='#1f4e8c', m='plastico')] + [p for i, c in enumerate(['#efefef', '#2e2e34', '#d8a020', '#efefef', '#2e2e34']) for p in (
    caja(0.05, 0.06, 0.02, x=-0.14 + i * 0.07, y=0.18, z=-0.07, c=c, m='plastico'), caja(0.012, 0.1, 0.012, x=-0.14 + i * 0.07, y=0.1, z=-0.07, c=c, m='plastico'))], nota='cargadores de coche y de pared; a la venta junto a la caja')
obj('ele_linternas_exp', 'Expositor de linternas', 'tb_accesorio', 'PICKUP', 1.5, 'plastico', 'superficie', [
    caja(0.32, 0.02, 0.2, y=0.01, c='#2e2e34', m='plastico'), caja(0.32, 0.22, 0.02, y=0.13, z=-0.09, c='#c0302a', m='plastico')] + [p for i, c in enumerate(['#d8a020', '#2c5aa0', '#34343a', '#3a8a5a']) for p in (
    cil(0.018, 0.018, 0.16, x=-0.105 + i * 0.07, y=0.1, z=-0.01, c=c, m='plastico', seg=8), cil(0.026, 0.026, 0.035, x=-0.105 + i * 0.07, y=0.185, z=-0.01, c='#c3c7ca', m='metal', seg=8))], nota='linternas a la venta')

# ---- fans, lamps
obj('ele_ventilador_sobremesa', 'Ventilador de sobremesa', 'pequeño_electrodomestico', 'PICKUP', 1.8, 'plastico', 'superficie', [
    cil(0.1, 0.1, 0.03, y=0.015, c='#e8e4d8', m='plastico', seg=12), cil(0.02, 0.02, 0.2, y=0.13, c='#e8e4d8', m='plastico', seg=8), cil(0.14, 0.14, 0.05, y=0.3, z=0.04, c='#c3c7ca', m='metal', r=[90, 0, 0], seg=16), cil(0.12, 0.12, 0.01, y=0.3, z=0.07, c=GLASS, m='cristal', r=[90, 0, 0], seg=16)])
obj('ele_ventilador_pie', 'Ventilador de pie con rejilla', 'pequeño_electrodomestico', 'CARRY', 5.5, 'plastico', 'suelo', [
    cil(0.22, 0.22, 0.03, y=0.015, c='#34343a', m='plastico', seg=12), cil(0.025, 0.025, 1.1, y=0.57, c='#c3c7ca', m='metal', seg=8), cil(0.2, 0.2, 0.08, y=1.2, z=0.05, c='#e8e4d8', m='plastico', r=[90, 0, 0], seg=16), cil(0.19, 0.19, 0.02, y=1.2, z=0.1, c=GLASS, m='cristal', r=[90, 0, 0], seg=16)])
obj('ele_ventilador_torre', 'Ventilador de torre', 'pequeño_electrodomestico', 'CARRY', 5.2, 'plastico', 'suelo', [
    cil(0.12, 0.12, 0.03, y=0.015, c='#34343a', m='plastico', seg=12), cil(0.07, 0.07, 1.0, y=0.53, c='#2e2e34', m='plastico', seg=12), caja(0.1, 0.8, 0.02, y=0.6, z=0.068, c='#2a2a2e', m='plastico'), caja(0.06, 0.03, 0.004, y=0.96, z=0.075, c='#7fe0ff', m='plastico', luz=True)])
obj('ele_aire_portatil', 'Aire acondicionado portátil', 'electrodomestico', 'CARRY', 24, 'plastico', 'suelo', [
    caja(0.4, 0.75, 0.35, y=0.375, z=0.175, c=BLANCO_E, m='plastico'), caja(0.3, 0.04, 0.012, y=0.65, z=0.356, c='#2e2e34', m='plastico'), caja(0.12, 0.03, 0.004, x=0.08, y=0.52, z=0.357, c='#7fe0ff', m='plastico', luz=True)] + [cil(0.03, 0.03, 0.02, x=sx * 0.14, y=0.03, z=0.15, c=DARK, m='goma', r=[0, 0, 90], seg=8) for sx in (-1, 1)])
obj('ele_lampara_pie_led', 'Lámpara de pie LED', 'lampara', 'PICKUP', 4.5, 'metal', 'suelo', [
    cil(0.14, 0.14, 0.02, y=0.01, c='#2e2e34', m='metal', seg=12), cil(0.012, 0.012, 1.5, y=0.76, c='#c3c7ca', m='metal', seg=8), caja(0.28, 0.06, 0.28, y=1.55, c='#f2efe6', m='plastico'), caja(0.24, 0.008, 0.24, y=1.515, c='#fff3d6', m='plastico', luz=True)])
obj('ele_lamparita_mesa', 'Lamparita de mesilla con pantalla', 'lampara', 'PICKUP', 1.6, 'tela', 'superficie', [
    cil(0.07, 0.07, 0.02, y=0.01, c='#d8cdb8', m='ceramica', seg=10), cil(0.025, 0.025, 0.18, y=0.11, c='#d8cdb8', m='ceramica', seg=8), cil(0.1, 0.07, 0.16, y=0.26, c='#f2e6c8', m='tela', seg=12), esf(0.03, 0, 0.24, 0, c='#fff3d6', m='plastico', luz=True)])
obj('ele_flexo', 'Flexo de escritorio', 'lampara', 'PICKUP', 1.2, 'metal', 'superficie', [
    cil(0.07, 0.07, 0.02, y=0.01, c='#2e2e34', m='metal', seg=10), caja(0.015, 0.3, 0.015, x=0.0, y=0.17, z=-0.0, c='#c3c7ca', m='metal', r=[0, 0, 0]), caja(0.18, 0.015, 0.015, x=0.07, y=0.32, c='#c3c7ca', m='metal'), cil(0.04, 0.05, 0.07, x=0.15, y=0.3, c='#2e2e34', m='metal', seg=8), cil(0.035, 0.035, 0.004, x=0.15, y=0.262, c='#fff3d6', m='plastico', seg=8, luz=True)])
obj('ele_bombillas_exp', 'Expositor de bombillas y regletas', 'tb_accesorio', 'PICKUP', 1.2, 'plastico', 'superficie', [
    caja(0.34, 0.02, 0.2, y=0.01, c='#2e2e34', m='plastico'), caja(0.34, 0.24, 0.02, y=0.14, z=-0.09, c='#f2c230', m='plastico')] + [p for i in range(4) for p in (esf(0.03, -0.12 + i * 0.08, 0.2, -0.06, c='#fff3d6', m='cristal'), cil(0.018, 0.018, 0.03, x=-0.12 + i * 0.08, y=0.15, z=-0.06, c='#c3c7ca', m='metal', seg=8))])

# ---- small appliances in their boxes (facings: box in colour, a lighter panel, a little silhouette of the thing)
def u_caja_ap(c, w, h, d, forma, c2):
    def f(x, z):
        P = [caja(w, h, d, x=x, y=h / 2, z=z, c=c, m='papel'), caja(w * 0.8, h * 0.72, 0.004, x=x, y=h * 0.52, z=z + d / 2 + 0.002, c='#f2efe6', m='papel')]
        zz = z + d / 2 + 0.008
        if forma == 'cilindro': P.append(cil(w * 0.14, w * 0.14, h * 0.5, x=x, y=h * 0.5, z=zz, c=c2, m='plastico', seg=8))
        elif forma == 'caja': P.append(caja(w * 0.5, h * 0.36, 0.012, x=x, y=h * 0.5, z=zz, c=c2, m='plastico'))
        elif forma == 'plancha': P.append(caja(w * 0.55, h * 0.18, 0.012, x=x, y=h * 0.42, z=zz, c=c2, m='plastico'))
        elif forma == 'larga': P.append(caja(w * 0.14, h * 0.6, 0.012, x=x, y=h * 0.52, z=zz, c=c2, m='plastico'))
        elif forma == 'vaso': P.append(cil(w * 0.12, w * 0.09, h * 0.5, x=x, y=h * 0.5, z=zz, c=c2, m='cristal', seg=8))
        return P
    return f
APARATOS = [
    ('cafetera_goteo', 'Cafeteras de goteo', 'cilindro', '#2e2e34', '#c0302a', 0.24, 0.3, 0.2, 2, 2, 2.6), ('cafetera_capsulas', 'Cafeteras de cápsulas', 'caja', '#c0302a', '#2e2e34', 0.22, 0.3, 0.3, 2, 1, 3.8),
    ('tostadora', 'Tostadoras de pan', 'caja', '#e8e4d8', '#c3c7ca', 0.3, 0.22, 0.22, 2, 2, 1.6), ('batidora_mano', 'Batidoras de mano', 'larga', '#2c5aa0', '#e8e4d8', 0.14, 0.4, 0.14, 3, 2, 1.4),
    ('robot_cocina', 'Robots de cocina', 'cilindro', '#e8e4d8', '#c3c7ca', 0.4, 0.4, 0.4, 1, 1, 9.0), ('plancha_ropa', 'Planchas de vapor', 'plancha', '#2c5aa0', '#c3c7ca', 0.3, 0.16, 0.14, 3, 2, 1.8),
    ('aspirador_escoba', 'Aspiradores escoba sin cable', 'larga', '#c0302a', '#2e2e34', 0.2, 0.9, 0.16, 2, 1, 3.6), ('hervidor', 'Hervidores de agua', 'vaso', '#2e2e34', '#c3c7ca', 0.2, 0.26, 0.2, 3, 2, 1.5),
    ('freidora_aire', 'Freidoras de aire', 'caja', '#2e2e34', '#c0302a', 0.34, 0.36, 0.34, 1, 1, 6.5), ('exprimidor', 'Exprimidores eléctricos', 'cilindro', '#f2a030', '#e8e4d8', 0.22, 0.28, 0.2, 2, 2, 2.2),
    ('picadora', 'Picadoras de cocina', 'vaso', '#3a8a5a', '#c3c7ca', 0.18, 0.24, 0.18, 3, 2, 1.8), ('olla_arroz', 'Ollas de arroz', 'cilindro', '#e8e4d8', '#d8dde0', 0.26, 0.26, 0.26, 2, 1, 3.4),
    ('secador_pelo', 'Secadores de pelo', 'larga', '#e0b4c0', '#2e2e34', 0.12, 0.3, 0.1, 4, 2, 0.7), ('afeitadora', 'Afeitadoras eléctricas', 'larga', '#34343a', '#c3c7ca', 0.1, 0.2, 0.08, 4, 2, 0.4),
    ('bascula_bano', 'Básculas de baño', 'plancha', '#e8e4d8', '#7fa0c8', 0.34, 0.06, 0.34, 2, 1, 2.4), ('batidora_vaso', 'Batidoras de vaso', 'vaso', '#c0302a', '#c3c7ca', 0.2, 0.4, 0.2, 2, 2, 3.5),
]
for k, n_, forma, c, c2, w, h, d, nx, nz, mu in APARATOS:
    nz = min(nz, int(0.42 / (d + 0.01)))
    regis('ele_ap_' + k, n_, 'pequeño_electrodomestico', u_caja_ap(c, w, h, d, forma, c2), nx, nz, w + 0.01, d + 0.01, h, 0.42, c, mu, mat='papel', hf=0.95)
for k, (n_, c, w, h, d, mu) in {'lavadora': ('Caja de lavadora', '#c9a46e', 0.65, 0.9, 0.62, 74), 'nevera': ('Caja de frigorífico', '#c9a46e', 0.65, 1.9, 0.7, 70), 'tv': ('Caja de televisor', '#c9a46e', 1.25, 0.8, 0.2, 14), 'cocina': ('Caja de cocina', '#c9a46e', 0.64, 0.9, 0.64, 50)}.items():
    obj('ele_caja_' + k, n_ + ' (embalaje)', 'caja', None, min(mu, 25) if k != 'tv' else 14, 'papel', 'suelo', [
        caja(w, h, d, y=h / 2, c=c, m='papel'), caja(w * 0.6, h * 0.25, 0.004, y=h * 0.6, z=d / 2 + 0.002, c='#f2efe6', m='papel'), caja(w * 0.45, h * 0.06, 0.005, y=h * 0.6, z=d / 2 + 0.004, c='#1f4e8c', m='papel'), caja(w + 0.01, 0.02, d + 0.01, y=h - 0.01, c='#b8925c', m='papel')],
        )
obj('ele_carretilla_electro', 'Carretilla de mano para electrodomésticos', 'tb_producto_hogar', 'CARRY', 14, 'metal', 'suelo', [
    caja(0.04, 1.2, 0.04, x=-0.22, y=0.6, z=-0.15, c='#1f4e8c', m='metal'), caja(0.04, 1.2, 0.04, x=0.22, y=0.6, z=-0.15, c='#1f4e8c', m='metal'), caja(0.5, 0.02, 0.25, y=0.03, z=0.0, c='#9aa0a4', m='metal'), caja(0.46, 0.04, 0.04, y=0.9, z=-0.15, c='#1f4e8c', m='metal'),
    cil(0.1, 0.1, 0.04, x=-0.25, y=0.1, z=-0.2, c=DARK, m='goma', r=[0, 0, 90], seg=12), cil(0.1, 0.1, 0.04, x=0.25, y=0.1, z=-0.2, c=DARK, m='goma', r=[0, 0, 90], seg=12)])
