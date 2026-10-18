# The car workshop's objects (family «tiendas_b»): the parts counter and its shelves of boxed parts, the bay with a two-post
# lift and a car, the tool chests and benches, tyre racks, oil drums, compressor, tyre machines, the little office.
# Ids start with «tal_». No real brand: invented names, plain colours; the cars are plain boxes on wheels, with no marque.
from tb_base import *

AZUL_T, ROJO_T, GRIS_T = '#2c5aa0', '#b3342a', '#8a9096'
NEUM = '#2b2b2e'

# ---- the parts counter: grey laminate, steel top, a glass front lip
obj('tal_mostrador_recambios', 'Mostrador de recambios (1,2 m)', 'mostrador', 'FIXED', 150, 'metal', 'suelo', [
    caja(1.2, 0.98, 0.64, y=0.49, z=-0.02, c='#9aa0a6'), caja(1.22, 0.04, 0.7, y=1.0, z=0.0, c='#d0d4d6', m='metal'), caja(1.14, 0.55, 0.012, y=0.52, z=0.3, c=AZUL_T),
    caja(1.2, 0.08, 0.012, y=0.04, z=0.3, c=DARK), caja(0.4, 0.1, 0.012, y=0.86, z=0.3, c='#d6d9db')],
    motivo_fijo='estructural', superficies=[sup(1.02, 0.04)], nota='mostrador de recambios, con la caja y el catálogo')
obj('tal_catalogo_recambios', 'Catálogo de recambios abierto', 'papel', 'PICKUP', 1.2, 'papel', 'superficie', [
    caja(0.46, 0.04, 0.32, y=0.02, c='#2c5aa0', m='papel'), caja(0.21, 0.02, 0.29, x=-0.115, y=0.05, c='#f2efe6', m='papel'), caja(0.21, 0.02, 0.29, x=0.115, y=0.05, c='#f2efe6', m='papel')])
obj('tal_exp_linternas', 'Expositor de linternas', 'tb_herramienta', 'PICKUP', 1.8, 'plastico', 'superficie', [
    caja(0.3, 0.02, 0.2, y=0.01, c='#2e2e34', m='plastico'), caja(0.3, 0.22, 0.02, y=0.13, z=-0.09, c='#2c5aa0', m='plastico')] + [
    p for i, c in enumerate(['#d8a020', '#b3342a', '#34343a', '#2c5aa0']) for p in (cil(0.018, 0.018, 0.17, x=-0.105 + i * 0.07, y=0.115, z=0.0, c=c, m='plastico', seg=8), cil(0.026, 0.026, 0.035, x=-0.105 + i * 0.07, y=0.2, z=0.0, c='#c3c7ca', m='metal', seg=8))],
    nota='linternas a la venta junto a la caja')

# ---- heavy-duty shelving for boxed parts: four posts, steel decking at each level
def estanteria_pesada(id, nombre, w, d, ys, alto, post=AZUL_T, viga='#d8822a'):
    P = [caja(0.05, alto, 0.05, x=sx * (w / 2 - 0.025), y=alto / 2, z=sz * (d / 2 - 0.025) + d / 2, c=post, m='metal') for sx in (-1, 1) for sz in (-1, 1)]
    P += [caja(w, 0.03, d, y=y - 0.015, z=d / 2, c='#c3c7ca', m='metal') for y in ys]
    P += [caja(w, 0.06, 0.04, y=y - 0.06, z=d - 0.02, c=viga, m='metal') for y in ys[1:]] + [caja(w, 0.06, 0.04, y=ys[0] - 0.06, z=0.02, c=viga, m='metal')]
    obj(id, nombre, 'estanteria', 'FIXED', 85, 'metal', 'suelo', P, motivo_fijo=FIJO, superficies=[sup(y, 0.03, fondo=d - 0.04) for y in ys], nota='estantería metálica de carga: postes azules y vigas naranjas')
estanteria_pesada('tal_estanteria_recambios', 'Estantería de recambios (1,2 m)', 1.2, 0.5, [0.35, 0.7, 1.05, 1.4, 1.75, 2.1], 2.2)
estanteria_pesada('tal_estanteria_baja', 'Estantería baja de almacén (1,2 m)', 1.2, 0.5, [0.4, 0.8, 1.2], 1.4, post=GRIS_T)

# ---- tool chests (the red roller cabinets of every workshop), benches and pegboards
def cajonera(id, nombre, c, ancho=0.75):
    P = [caja(ancho, 0.8, 0.46, y=0.4, z=0.0, c=c), caja(ancho + 0.02, 0.04, 0.5, y=0.82, c=oscuro(c, 0.8), m='metal'), caja(ancho * 0.97, 0.22, 0.42, y=0.95, z=-0.01, c=c), caja(ancho * 0.97, 0.02, 0.44, y=1.07, z=-0.01, c=oscuro(c, 0.8), m='metal')]
    for k, y in enumerate((0.15, 0.35, 0.55, 0.73)):
        P += [caja(ancho * 0.92, 0.17 if k < 3 else 0.14, 0.012, y=y, z=0.232, c=oscuro(c, 0.9)), caja(ancho * 0.6, 0.014, 0.02, y=y + 0.05, z=0.245, c=STEEL, m='metal')]
    P += [caja(ancho * 0.9, 0.12, 0.012, y=0.95, z=0.2, c=oscuro(c, 0.85)), caja(0.12, 0.02, 0.02, y=0.98, z=0.21, c=STEEL, m='metal')]
    P += [cil(0.05, 0.05, 0.04, x=sx * (ancho / 2 - 0.06), y=0.05, z=sz * 0.14, c=DARK, m='goma', r=[0, 0, 90], seg=8) for sx in (-1, 1) for sz in (-1, 1)]
    obj(id, nombre, 'tb_cajonera', None, 90, 'metal', 'suelo', P, superficies=[sup(1.08, 0.04)], nota='cajonera de herramientas con cajón superior; ruedas y asas')
cajonera('tal_cajonera_roja', 'Cajonera de herramientas roja', ROJO_T)
cajonera('tal_cajonera_azul', 'Cajonera de herramientas azul', '#2c5aa0')
cajonera('tal_cajonera_gris', 'Cajonera de herramientas gris', '#7a8086')
def utensilios(x0, y0, ancho, alto):
    """tools hung on a pegboard: spanners, hammers, pliers, a saw — flat boxes in plain colours (the pegboard's local frame: z in front of it)"""
    P = []
    cols = [STEEL, ROJO_T, '#d8a020', '#2c5aa0', '#3a8a5a']
    for i in range(6):
        xx = x0 + 0.12 + i * (ancho - 0.24) / 5
        P += [caja(0.03, 0.26 + (i % 3) * 0.06, 0.014, x=xx, y=y0 + alto * 0.7, z=0.04, c=STEEL if i % 2 else cols[i % 5], m='metal'), caja(0.06, 0.05, 0.016, x=xx, y=y0 + alto * 0.7 + 0.15 + (i % 3) * 0.03, z=0.04, c=STEEL, m='metal')]
    for i in range(3):
        P += [caja(0.04, 0.14, 0.02, x=x0 + 0.2 + i * 0.3, y=y0 + alto * 0.3, z=0.045, c=cols[(i + 1) % 5], m='plastico'), caja(0.1, 0.04, 0.02, x=x0 + 0.2 + i * 0.3, y=y0 + alto * 0.3 + 0.09, z=0.045, c=STEEL, m='metal')]
    P += [caja(0.3, 0.1, 0.014, x=x0 + ancho - 0.25, y=y0 + alto * 0.3, z=0.04, c='#d8a020', m='plastico')]
    return P
def panel_pared(ancho=1.2, alto=0.9, y0=1.25):
    return [caja(ancho, alto, 0.02, y=y0 + alto / 2, z=0.01, c='#5a626a')] + utensilios(-ancho / 2, y0, ancho, alto)
obj('tal_panel_herramientas', 'Panel de herramientas colgadas', 'tb_herramienta', 'FIXED', 12, 'metal', 'pared', [
    caja(1.2, 0.9, 0.02, y=1.65, z=0.01, c='#5a626a')] + utensilios(-0.6, 1.2, 1.2, 0.9), motivo_fijo=FIJO)
def banco_trabajo(id, nombre, c_top='#b8935a'):
    P = [caja(1.8, 0.05, 0.7, y=0.9, z=0.35, c=c_top), caja(1.76, 0.06, 0.66, y=0.85, z=0.35, c='#5a626a', m='metal')] + [caja(0.06, 0.82, 0.06, x=sx * 0.84, y=0.41, z=0.06 + (sz + 1) * 0.29, c='#5a626a', m='metal') for sx in (-1, 1) for sz in (-1, 1)]
    P += [caja(1.7, 0.03, 0.6, y=0.2, z=0.35, c='#8a9096', m='metal')]
    P += [caja(0.14, 0.1, 0.12, x=0.75, y=0.975, z=0.5, c='#c0392b', m='metal'), caja(0.06, 0.06, 0.1, x=0.75, y=1.06, z=0.58, c='#2b2b2e', m='metal'), caja(0.02, 0.08, 0.1, x=0.75, y=1.02, z=0.66, c=STEEL, m='metal')]  # the vice
    P += panel_pared(1.7, 0.9, 1.08)
    obj(id, nombre, 'tb_banco_trabajo', None, 95, 'metal', 'suelo', P, superficies=[sup(0.925, 0.05)], nota='banco de trabajo con tornillo de banco y panel de herramientas')
banco_trabajo('tal_banco_trabajo', 'Banco de trabajo con tornillo y panel')
banco_trabajo('tal_banco_trabajo_madera', 'Banco de trabajo de madera con panel', c_top='#a8825a')

# ---- the lift and the cars: plain boxes on wheels
def coche(y0, c1, abierto=False, cola='#b3342a'):
    P = [caja(3.9, 0.46, 1.62, y=y0 + 0.57, c=c1, m='metal'), caja(3.5, 0.1, 1.3, y=y0 + 0.28, c='#3a3a42', m='metal'),
         caja(1.15, 0.08, 1.58, x=1.4, y=y0 + 0.84, c=c1, m='metal') if not abierto else caja(1.15, 0.06, 1.58, x=1.5, y=y0 + 1.25, c=c1, m='metal', r=[0, 0, 62]),
         caja(0.8, 0.08, 1.58, x=-1.5, y=y0 + 0.84, c=c1, m='metal'),
         caja(1.7, 0.48, 1.56, x=-0.1, y=y0 + 1.1, c=c1, m='metal'), caja(1.5, 0.05, 1.58, x=-0.1, y=y0 + 1.36, c=oscuro(c1, 0.9), m='metal'),
         caja(1.45, 0.34, 0.02, x=-0.1, y=y0 + 1.1, z=0.79, c='#7a9aa8', m='cristal'), caja(1.45, 0.34, 0.02, x=-0.1, y=y0 + 1.1, z=-0.79, c='#7a9aa8', m='cristal'),
         caja(0.02, 0.4, 1.4, x=0.82, y=y0 + 1.1, c='#7a9aa8', m='cristal', r=[0, 0, 26]), caja(0.02, 0.36, 1.4, x=-1.0, y=y0 + 1.1, c='#7a9aa8', m='cristal', r=[0, 0, -24]),
         caja(0.1, 0.18, 1.64, x=2.0, y=y0 + 0.42, c='#3a3a42', m='plastico'), caja(0.1, 0.18, 1.64, x=-2.0, y=y0 + 0.42, c='#3a3a42', m='plastico'),
         caja(0.04, 0.1, 0.3, x=1.96, y=y0 + 0.66, z=-0.55, c='#e8e4d0', m='plastico'), caja(0.04, 0.1, 0.3, x=1.96, y=y0 + 0.66, z=0.55, c='#e8e4d0', m='plastico'),
         caja(0.04, 0.1, 0.3, x=-1.96, y=y0 + 0.66, z=-0.55, c=cola, m='plastico'), caja(0.04, 0.1, 0.3, x=-1.96, y=y0 + 0.66, z=0.55, c=cola, m='plastico'),
         caja(0.04, 0.1, 0.4, x=1.96, y=y0 + 0.42, z=0, c='#e8e4d8', m='plastico')]
    for sx in (-1, 1):
        for sz in (-1, 1):
            P += [cil(0.31, 0.31, 0.22, x=sx * 1.25, y=y0 + 0.31, z=sz * 0.78, c=NEUM, m='goma', r=[90, 0, 0], seg=14), cil(0.18, 0.18, 0.225, x=sx * 1.25, y=y0 + 0.31, z=sz * 0.78, c='#a8adb2', m='metal', r=[90, 0, 0], seg=10)]
    return P
obj('tal_coche_capo_abierto', 'Coche con el capó abierto', 'tb_vehiculo', 'FIXED', 1150, 'metal', 'suelo', coche(0, '#7a8a9a', abierto=True), motivo_fijo='diseño', nota='un turismo sin marca, a la espera de reparación')
def elevador(c1):
    P = coche(1.05, c1)
    for sz in (-1, 1):
        P += [caja(0.28, 2.9, 0.22, x=0, y=1.45, z=sz * 1.2, c='#d8822a', m='metal'), caja(0.9, 0.03, 0.8, x=0, y=0.015, z=sz * 1.2, c='#5a626a', m='metal'), caja(0.3, 0.3, 0.26, x=0, y=1.0, z=sz * 1.2, c='#8a9096', m='metal'),
              caja(1.3, 0.08, 0.1, x=-0.75, y=0.98, z=sz * 0.92, c='#8a9096', m='metal'), caja(1.3, 0.08, 0.1, x=0.75, y=0.98, z=sz * 0.92, c='#8a9096', m='metal'),
              cil(0.07, 0.07, 0.06, x=-1.15, y=1.04, z=sz * 0.82, c='#2b2b2e', m='goma', seg=8), cil(0.07, 0.07, 0.06, x=1.15, y=1.04, z=sz * 0.82, c='#2b2b2e', m='goma', seg=8)]
    P += [caja(0.12, 0.12, 2.4, x=0, y=2.88, z=0.0, c='#8a9096', m='metal'), caja(0.5, 0.35, 0.18, x=0.0, y=1.5, z=-1.42, c='#c3c7ca', m='metal'), caja(0.12, 0.08, 0.02, x=0.1, y=1.55, z=-1.52, c='#3a8a5a', m='plastico', luz=True)]
    obj('tal_elevador_' + {'#2c5aa0': 'azul', '#b3342a': 'rojo', '#c3c7ca': 'plata'}[c1], 'Elevador de dos columnas con un turismo elevado', 'tb_elevador', 'FIXED', 1450, 'metal', 'suelo', P, motivo_fijo=FIJO, nota='el coche, un metro por encima del suelo; las columnas, de lado a lado')
for c1 in ('#2c5aa0', '#b3342a', '#c3c7ca'): elevador(c1)

# ---- small machines and equipment of the bay
obj('tal_gato_hidraulico', 'Gato hidráulico de carretilla', 'tb_herramienta', 'CARRY', 22, 'metal', 'suelo', [
    caja(0.3, 0.14, 0.7, y=0.09, z=0.0, c=ROJO_T, m='metal'), caja(0.2, 0.12, 0.2, y=0.16, z=0.0, c='#d8a020', m='metal'), cil(0.04, 0.04, 0.35, y=0.3, z=-0.28, c='#2b2b2e', m='metal', r=[-30, 0, 0], seg=8), cil(0.03, 0.03, 0.3, y=0.12, z=-0.42, c=STEEL, m='metal', r=[90, 0, 0], seg=8),
    cil(0.05, 0.05, 0.04, x=-0.15, y=0.05, z=0.3, c=DARK, m='goma', r=[0, 0, 90], seg=8), cil(0.05, 0.05, 0.04, x=0.15, y=0.05, z=0.3, c=DARK, m='goma', r=[0, 0, 90], seg=8)])
obj('tal_caballetes', 'Pareja de caballetes de seguridad', 'tb_herramienta', 'CARRY', 11, 'metal', 'suelo', [
    p for sx in (-0.2, 0.2) for p in (caja(0.2, 0.04, 0.2, x=sx, y=0.02, c='#3a8a5a', m='metal'), cil(0.04, 0.04, 0.3, x=sx, y=0.19, c='#3a8a5a', m='metal', seg=8), cil(0.07, 0.07, 0.03, x=sx, y=0.355, c='#3a8a5a', m='metal', seg=8))])
obj('tal_carro_aceite', 'Carro recogedor de aceite usado', 'tb_herramienta', 'CARRY', 16, 'metal', 'suelo', [
    cil(0.17, 0.17, 0.6, y=0.38, c='#d8a020', m='metal', seg=12), cil(0.22, 0.22, 0.04, y=0.82, c='#a8adb2', m='metal', seg=14), cil(0.06, 0.06, 0.3, y=0.97, c='#a8adb2', m='metal', seg=8), caja(0.3, 0.03, 0.4, y=0.07, c=DARK, m='metal')] + [
    cil(0.04, 0.04, 0.03, x=sx * 0.14, y=0.04, z=sz * 0.15, c=DARK, m='goma', r=[0, 0, 90], seg=8) for sx in (-1, 1) for sz in (-1, 1)])
obj('tal_compresor', 'Compresor de aire con ruedas', 'tb_maquina_taller', 'PUSH', 55, 'metal', 'suelo', [
    cil(0.2, 0.2, 0.8, y=0.5, c=AZUL_T, m='metal', r=[0, 0, 90], seg=14), caja(0.3, 0.3, 0.3, x=0.1, y=0.85, c='#5a626a', m='metal'), cil(0.07, 0.07, 0.04, x=0.1, y=1.02, z=0.1, c='#c0392b', m='plastico', seg=8),
    cil(0.06, 0.06, 0.04, x=0.3, y=0.52, z=0.21, c='#d8d8d0', m='metal', r=[90, 0, 0], seg=10), caja(0.04, 0.6, 0.04, x=-0.35, y=0.3, z=-0.18, c='#5a626a', m='metal'), caja(0.04, 0.6, 0.04, x=-0.35, y=0.3, z=0.18, c='#5a626a', m='metal'),
    cil(0.14, 0.14, 0.05, x=0.0, y=0.14, z=0.3, c=DARK, m='goma', r=[0, 0, 90], seg=10), cil(0.14, 0.14, 0.05, x=0.0, y=0.14, z=-0.3, c=DARK, m='goma', r=[0, 0, 90], seg=10), caja(0.5, 0.04, 0.5, x=-0.1, y=0.27, c='#5a626a', m='metal')])
obj('tal_equilibradora', 'Equilibradora de ruedas', 'tb_maquina_taller', 'PUSH', 70, 'metal', 'suelo', [
    caja(0.8, 0.8, 0.6, y=0.4, z=0.0, c='#d0d4d6', m='metal'), caja(0.5, 0.12, 0.4, y=0.86, z=0.05, c='#5a626a', m='metal'), cil(0.3, 0.3, 0.2, y=1.0, z=0.45, c=NEUM, m='goma', r=[90, 0, 0], seg=14), cil(0.17, 0.17, 0.21, y=1.0, z=0.45, c='#a8adb2', m='metal', r=[90, 0, 0], seg=10),
    caja(0.62, 0.62, 0.04, y=1.1, z=0.7, c='#c3c7ca', m='cristal'), caja(0.22, 0.12, 0.03, x=0.28, y=0.8, z=0.31, c='#2b2b2e', m='plastico'), caja(0.16, 0.08, 0.004, x=0.28, y=0.8, z=0.327, c='#7fe0ff', m='plastico', luz=True)])
obj('tal_desmontadora_neumaticos', 'Desmontadora de neumáticos', 'tb_maquina_taller', 'PUSH', 78, 'metal', 'suelo', [
    caja(0.8, 0.2, 0.8, y=0.1, c='#5a626a', m='metal'), cil(0.38, 0.38, 0.05, y=0.225, c='#d8822a', m='metal', seg=16), cil(0.05, 0.05, 0.05, y=0.275, c='#c3c7ca', m='metal', seg=8),
    caja(0.18, 1.4, 0.18, x=0.5, y=0.7, z=-0.2, c='#5a626a', m='metal'), caja(0.7, 0.08, 0.1, x=0.15, y=1.35, z=-0.2, c='#5a626a', m='metal'), caja(0.08, 0.3, 0.08, x=-0.2, y=1.2, z=-0.2, c='#c0392b', m='metal'), cil(0.025, 0.025, 0.5, x=0.55, y=0.4, z=0.15, c='#2b2b2e', m='goma', r=[90, 0, 0], seg=6)])
obj('tal_carro_mecanico', 'Carro de mecánico para tumbarse', 'tb_herramienta', 'PICKUP', 4.2, 'plastico', 'suelo', [
    caja(0.45, 0.04, 1.0, y=0.065, c='#c0392b', m='plastico'), caja(0.45, 0.08, 0.2, y=0.1, z=-0.4, c='#a8301f', m='plastico')] + [cil(0.03, 0.03, 0.02, x=sx * 0.18, y=0.03, z=sz * 0.4, c=DARK, m='goma', r=[0, 0, 90], seg=6) for sx in (-1, 1) for sz in (-1, 1)])
obj('tal_taburete_taller', 'Taburete bajo de taller', 'taburete', 'PICKUP', 3.2, 'metal', 'suelo', [
    cil(0.17, 0.17, 0.05, y=0.42, c='#2b2b2e', m='plastico', seg=12)] + [cil(0.015, 0.015, 0.42, x=sx * 0.12, y=0.21, z=sz * 0.12, c=STEEL, m='metal', seg=6) for sx in (-1, 1) for sz in (-1, 1)] + [cil(0.15, 0.15, 0.02, y=0.15, c=STEEL, m='metal', seg=10)],
    modificadores=['SEAT'], asientos=[{'p': [0, 0.45, 0], 'h': 0.45, 'anim': 'taburete_alto'}])

# ---- tyres: a stack, a rack with standing tyres, the drums of oil
def neumatico_pie(x, y, z, r=0.31, ancho=0.2, eje='z'):
    rot = [90, 0, 0] if eje == 'z' else [0, 0, 90]
    return [cil(r * 0.96, r * 0.96, ancho, x=x, y=y, z=z, c='#34343a', m='goma', r=rot, seg=16), cil(r, r, ancho * 0.62, x=x, y=y, z=z, c=NEUM, m='goma', r=rot, seg=16), cil(r * 0.58, r * 0.58, ancho + 0.005, x=x, y=y, z=z, c='#a8adb2', m='metal', r=rot, seg=12)]
def pila_neum(id, nombre, r, ancho, n, rim):
    P = []
    for k in range(n):
        P += [cil(r * 0.96, r * 0.96, ancho, y=ancho / 2 + k * ancho, c='#34343a', m='goma', seg=16), cil(r, r, ancho * 0.62, y=ancho / 2 + k * ancho, c=NEUM, m='goma', seg=16)]
    P += [cil(r * 0.6, r * 0.6, 0.004, y=n * ancho, c=rim, m='metal', seg=12)]
    obj(id, nombre, 'tb_pila_neumaticos', None, round(n * 9.5, 1), 'goma', 'suelo', P)
pila_neum('tal_pila_neumaticos_a', 'Pila de neumáticos de turismo', 0.31, 0.2, 4, '#a8adb2')
pila_neum('tal_pila_neumaticos_b', 'Pila de neumáticos de furgoneta', 0.34, 0.24, 3, '#c3c7ca')
pila_neum('tal_pila_neumaticos_c', 'Pila de neumáticos pequeños', 0.27, 0.17, 5, '#8a9096')
def estanteria_neum(id, nombre, c):
    P = [caja(0.06, 1.8, 0.06, x=sx * 0.57, y=0.9, z=sz * 0.3 + 0.35, c=c, m='metal') for sx in (-1, 1) for sz in (-1, 1)]
    P += [caja(1.2, 0.04, 0.7, y=y, z=0.35, c='#8a9096', m='metal') for y in (0.02, 0.62, 1.22)]
    for y in (0.02, 0.62, 1.22):
        P += [p for k in range(4) for p in neumatico_pie(-0.43 + k * 0.29, y + 0.02 + 0.31, 0.35, ancho=0.2 if k % 2 else 0.24)]
    obj(id, nombre, 'estanteria', 'FIXED', 110, 'metal', 'suelo', P, motivo_fijo=FIJO, nota='tres baldas con neumáticos de pie')
estanteria_neum('tal_estanteria_neumaticos', 'Estantería de neumáticos', '#d8822a')
def bidon(id, nombre, c, masa=190, c2='#f2efe6'):
    obj(id, nombre, 'tb_bidon', None, masa, 'metal', 'suelo', [
        cil(0.29, 0.29, 0.88, y=0.44, c=c, m='metal', seg=14), cil(0.3, 0.3, 0.03, y=0.86, c=oscuro(c, 0.9), m='metal', seg=14), cil(0.3, 0.3, 0.03, y=0.02, c=oscuro(c, 0.9), m='metal', seg=14), cil(0.3, 0.3, 0.015, y=0.45, c=oscuro(c, 0.9), m='metal', seg=14),
        caja(0.3, 0.2, 0.01, y=0.5, z=0.29, c=c2, m='papel'), cil(0.03, 0.03, 0.05, x=0.12, y=0.9, z=0.1, c='#2b2b2e', m='plastico', seg=8)])
bidon('tal_bidon_aceite_azul', 'Bidón de aceite de motor (200 l, azul)', '#2c5aa0')
bidon('tal_bidon_aceite_negro', 'Bidón de aceite de cambio (200 l, negro)', '#3a3a42', 175)
bidon('tal_bidon_aceite_usado', 'Bidón de aceite usado (200 l, verde)', '#3a7a4a', 110)
obj('tal_garrafas_aceite_palet', 'Palé de garrafas de aceite de 5 litros', 'tb_bidon', 'PUSH_HEAVY', 110, 'plastico', 'suelo', [
    caja(1.2, 0.14, 0.8, y=0.07, c='#b88a58', m='madera')] + [caja(0.28, 0.3, 0.2, x=(i - 1.5) * 0.3, y=0.14 + 0.15 + k * 0.3, z=(j - 0.5) * 0.3, c=['#d8a020', '#2c5aa0', '#3a8a5a'][(i + j + k) % 3], m='plastico') for i in range(4) for j in range(2) for k in range(3)])

# ---- little things for benches, chests and shelves
def util(id, nombre, masa, P, cat='tb_herramienta', **k): obj(id, nombre, cat, 'PICKUP', masa, 'metal', 'superficie', P, **k)
util('tal_llaves_juego', 'Juego de llaves fijas', 0.9, [caja(0.3, 0.015, 0.14, y=0.0075, c='#2b2b2e', m='plastico')] + [caja(0.28, 0.01, 0.014, y=0.02, z=-0.05 + i * 0.025, c=STEEL, m='metal') for i in range(5)])
util('tal_martillo', 'Martillo de peña', 0.8, [caja(0.03, 0.03, 0.3, y=0.015, c='#8a5a36', m='madera'), caja(0.14, 0.04, 0.05, x=0, y=0.05, z=-0.13, c=STEEL, m='metal')])
util('tal_caja_herramientas', 'Caja de herramientas abierta', 3.8, [caja(0.45, 0.18, 0.22, y=0.09, c=ROJO_T, m='plastico'), caja(0.4, 0.015, 0.18, y=0.19, c='#d6d9db', m='plastico')] + [caja(0.03, 0.14, 0.014, x=-0.15 + i * 0.075, y=0.22, z=0.0, c=[STEEL, '#d8a020', STEEL, '#2c5aa0', STEEL][i], m='metal') for i in range(5)] + [caja(0.4, 0.02, 0.02, y=0.3, c='#2b2b2e', m='metal')])
util('tal_lampara_inspeccion', 'Lámpara de inspección portátil', 0.9, [cil(0.05, 0.05, 0.22, y=0.05, c='#d8a020', m='plastico', r=[0, 0, 90], seg=8), cil(0.045, 0.045, 0.004, x=0.112, y=0.05, c='#fff3d6', m='plastico', r=[0, 0, 90], seg=8, luz=True)])
util('tal_motor_arranque', 'Motor de arranque desmontado', 4.5, [cil(0.05, 0.05, 0.18, y=0.05, c='#8a9096', m='metal', r=[0, 0, 90], seg=10), cil(0.04, 0.05, 0.1, x=0.12, y=0.05, c='#5a626a', m='metal', r=[0, 0, 90], seg=10), cil(0.045, 0.045, 0.14, x=-0.15, y=0.045, c='#3a3a42', m='metal', r=[0, 0, 90], seg=10)])
util('tal_pistones', 'Juego de pistones sobre un trapo', 1.2, [caja(0.3, 0.012, 0.18, y=0.006, c='#c9b46a', m='tela')] + [cil(0.035, 0.035, 0.06, x=-0.1 + i * 0.07, y=0.042, z=0.0, c='#a8adb2', m='metal', seg=8) for i in range(4)])
util('tal_trapos', 'Montón de trapos', 0.4, [caja(0.26, 0.06, 0.2, y=0.03, c='#c8b898', m='tela'), caja(0.2, 0.05, 0.16, x=0.02, y=0.085, c='#8a9aaa', m='tela')])
util('tal_rollo_papel_taller', 'Rollo de papel azul de taller', 0.6, [cil(0.09, 0.09, 0.2, y=0.1, c='#2c8ab0', m='papel', seg=12), cil(0.03, 0.03, 0.2, y=0.1, c='#c9a46e', m='papel', seg=8)])
# ---- a few more furniture pieces
obj('tal_lavabo_industrial', 'Lavabo industrial con jabón de talleres', 'sanitario', 'FIXED', 28, 'metal', 'pared', [
    caja(0.7, 0.2, 0.5, y=0.82, z=0.25, c='#c3c7ca', m='metal'), caja(0.64, 0.06, 0.44, y=0.9, z=0.25, c='#9aa0a4', m='metal'), cil(0.02, 0.02, 0.2, y=1.02, z=0.08, c=STEEL, m='metal', seg=8), caja(0.1, 0.18, 0.08, x=0.3, y=1.12, z=0.04, c='#d8a020', m='plastico'),
    caja(0.04, 0.8, 0.04, x=-0.3, y=0.4, z=0.46, c='#8a9096', m='metal'), caja(0.04, 0.8, 0.04, x=0.3, y=0.4, z=0.46, c='#8a9096', m='metal')], motivo_fijo=FIJO)
obj('tal_dispensador_papel', 'Dispensador de papel azul de pie', 'tb_herramienta', 'CARRY', 7, 'metal', 'suelo', [
    cil(0.2, 0.2, 0.03, y=0.015, c='#5a626a', m='metal', seg=12), cil(0.025, 0.025, 0.9, y=0.47, c='#8a9096', m='metal', seg=8), cil(0.1, 0.1, 0.22, y=1.0, c='#2c8ab0', m='papel', r=[0, 0, 90], seg=12), caja(0.26, 0.03, 0.03, y=1.14, c='#8a9096', m='metal')])
obj('tal_contenedor_residuos', 'Contenedor de residuos peligrosos', 'tb_bidon', 'PUSH', 40, 'metal', 'suelo', [
    caja(0.7, 0.8, 0.5, y=0.4, c='#d8a020', m='metal'), caja(0.72, 0.04, 0.52, y=0.82, c=oscuro('#d8a020', 0.85), m='metal'), plano(0.3, 0.3, y=0.5, z=0.252, c='#2b2b2e', m='papel')], nota='con su pictograma de residuo peligroso')
obj('tal_bateria_cargador', 'Cargador de baterías con ruedas', 'tb_herramienta', 'CARRY', 14, 'metal', 'suelo', [
    caja(0.32, 0.5, 0.3, y=0.5, c=AZUL_T, m='metal'), caja(0.04, 0.5, 0.04, x=-0.1, y=0.25, z=-0.1, c='#5a626a', m='metal'), caja(0.04, 0.5, 0.04, x=0.1, y=0.25, z=-0.1, c='#5a626a', m='metal'), caja(0.36, 0.03, 0.3, y=0.25, c='#5a626a', m='metal'),
    caja(0.2, 0.12, 0.004, y=0.62, z=0.152, c='#f2efe6', m='plastico'), cil(0.01, 0.01, 0.3, x=0.15, y=0.5, z=0.16, c='#c0392b', m='plastico', seg=6)] + [cil(0.04, 0.04, 0.03, x=sx * 0.14, y=0.04, z=0.1, c=DARK, m='goma', r=[0, 0, 90], seg=6) for sx in (-1, 1)])

# ---- the shop's own sign, posters and the price board
obj('tal_rotulo', 'Rótulo interior del taller', 'decoracion', 'PICKUP', 3, 'madera', 'pared', [
    caja(1.3, 0.34, 0.03, y=2.55, z=0.015, c='#2a2a2e'), plano(1.24, 0.28, y=2.55, z=0.033, tex={'tipo': 'rotulo_tb', 'estilo': 'taller', 'rotulo_local': True})])
for k, (n_, d1, t) in {'neumaticos': ('Cartel de neumáticos', 'neumatico', None), 'revision': ('Cartel de la revisión pre-ITV', 'coche', None)}.items():
    obj('tal_cartel_' + k, n_, 'cuadro', 'PICKUP', 1.2, 'papel', 'pared', [
        caja(0.5, 0.7, 0.025, y=1.7, z=0.0125, c='#2a2420'), plano(0.44, 0.64, y=1.7, z=0.027, tex={'tipo': 'cartel_tb', 'dibujo': d1})])
obj('tal_cartel_tarifas', 'Tarifas del taller', 'decoracion', 'PICKUP', 2, 'madera', 'pared', [
    caja(0.8, 0.8, 0.025, y=1.6, z=0.0125, c='#34383c'), plano(0.74, 0.74, y=1.6, z=0.0285, tex={'tipo': 'pizarra', 'lineas': ['Cambio de aceite  49', 'Frenos delanteros  89', 'Revisión pre-ITV  39', 'Alineado  35', 'Neumáticos  desde 55', 'Aire acondicionado  60']})])
obj('tal_senal_epi', 'Señal de uso obligatorio de protección', 'decoracion', 'PICKUP', 0.4, 'plastico', 'pared', [
    caja(0.3, 0.3, 0.01, y=1.8, z=0.005, c='#1f5aa0', m='plastico'), cil(0.1, 0.1, 0.004, y=1.8, z=0.012, c='#f2efe6', m='plastico', r=[90, 0, 0], seg=14), caja(0.12, 0.05, 0.004, y=1.82, z=0.014, c='#2b2b2e', m='plastico')])

# ---- parts: facings of boxed car parts (invented labels, plain boxes)
def u_disco(r, c):
    def f(x, z): return [cil(r, r, 0.03, x=x, y=0.015 + k * 0.034, z=z, c=c, m='metal', seg=12) for k in range(3)]
    return f
def u_amort(c):
    def f(x, z): return [cil(0.032, 0.032, 0.42, x=x, y=0.032, z=z, c=c, m='metal', r=[0, 0, 90], seg=8)]
    return f
def u_arbol(c):
    def f(x, z): return [cono(0.03, 0.09, x=x, y=0.045, z=z, c=c, m='plastico', seg=6), caja(0.07, 0.01, 0.04, x=x, y=0.005, z=z, c='#f2efe6', m='papel')]
    return f
PIEZAS = [
    ('filtro_aceite', 'Filtros de aceite', u_lata(0.04, 0.1, '#2c5aa0', '#f2efe6'), 6, 3, 0.085, 0.085, 0.1, 0.45, '#2c5aa0', 0.5, 'metal'),
    ('filtro_aire', 'Filtros de aire en caja', u_caja(0.2, 0.06, 0.16, '#d8a020', '#2b2b2e'), 2, 2, 0.21, 0.17, 0.06, 0.45, '#d8a020', 0.4, 'papel'),
    ('pastillas_freno', 'Pastillas de freno', u_caja(0.15, 0.06, 0.1, '#c0392b', '#f2efe6'), 3, 4, 0.16, 0.11, 0.06, 0.45, '#c0392b', 0.5, 'papel'),
    ('discos_freno', 'Discos de freno', u_disco(0.15, '#a8adb2'), 2, 1, 0.32, 0.32, 0.1, 0.34, '#a8adb2', 4.5, 'metal'),
    ('bujias', 'Cajitas de bujías', u_caja(0.1, 0.1, 0.05, '#3a8a5a', '#f2efe6'), 4, 4, 0.105, 0.055, 0.1, 0.45, '#3a8a5a', 0.25, 'papel'),
    ('baterias', 'Baterías de arranque', u_caja(0.24, 0.19, 0.17, '#2b2b2e', '#c0392b'), 1, 2, 0.25, 0.18, 0.19, 0.4, '#2b2b2e', 13, 'plastico'),
    ('escobillas', 'Escobillas limpiaparabrisas', u_caja(0.5, 0.025, 0.07, '#2b2b2e', '#2c8ab0'), 1, 6, 0.51, 0.075, 0.05, 0.45, '#2b2b2e', 0.35, 'papel'),
    ('aceite_5l', 'Garrafas de aceite de motor (5 l)', u_caja(0.2, 0.28, 0.13, '#d8a020', '#2b2b2e', m='plastico'), 3, 3, 0.21, 0.14, 0.28, 0.45, '#d8a020', 4.6, 'plastico'),
    ('aceite_1l', 'Botes de aceite de motor (1 l)', u_botella(0.036, 0.2, '#2c5aa0', '#f2efe6', '#2b2b2e', m='plastico'), 5, 3, 0.08, 0.08, 0.2, 0.45, '#2c5aa0', 0.95, 'plastico'),
    ('anticongelante', 'Botellas de anticongelante', u_botella(0.04, 0.26, '#d86a8a', '#f2efe6', '#d86a8a', m='plastico'), 4, 3, 0.09, 0.09, 0.26, 0.45, '#d86a8a', 1.1, 'plastico'),
    ('bombillas', 'Cajitas de bombillas de coche', u_caja(0.08, 0.1, 0.04, '#f2c230', '#2b2b2e'), 5, 4, 0.085, 0.045, 0.1, 0.45, '#f2c230', 0.1, 'papel'),
    ('correas', 'Correas de distribución', u_disco(0.08, '#2b2b2e'), 3, 2, 0.2, 0.2, 0.1, 0.4, '#2b2b2e', 0.6, 'goma'),
    ('amortiguadores', 'Amortiguadores', u_amort('#d8a020'), 1, 6, 0.44, 0.075, 0.07, 0.45, '#d8a020', 3.2, 'metal'),
    ('limpiaparabrisas', 'Líquido limpiaparabrisas', u_botella(0.04, 0.26, '#7ac0e8', '#f2efe6', '#2c5aa0', m='plastico'), 4, 3, 0.09, 0.09, 0.26, 0.45, '#7ac0e8', 1.1, 'plastico'),
    ('ambientadores', 'Ambientadores de coche', u_arbol('#3a8a5a'), 8, 4, 0.07, 0.07, 0.09, 0.3, '#3a8a5a', 0.03, 'plastico'),
    ('cadenas_nieve', 'Cajas de cadenas de nieve', u_caja(0.3, 0.12, 0.25, '#e0782a', '#2b2b2e'), 1, 2, 0.31, 0.26, 0.12, 0.5, '#e0782a', 3.5, 'papel'),
    ('cables_arranque', 'Cables de arranque', u_caja(0.28, 0.08, 0.16, '#c0392b', '#2b2b2e'), 1, 3, 0.29, 0.17, 0.08, 0.5, '#c0392b', 1.2, 'papel'),
]
for k, n_, unit, nx, nz, dx, dz, h, fondo, c, mu, mat in PIEZAS:
    regis('tal_prod_' + k, n_, 'tb_herramienta', unit, nx, nz, dx, dz, h, fondo, c, mu, mat='metal' if mat == 'metal' else 'plastico')
obj('tal_prod_neumatico_expuesto', 'Neumático nuevo en exposición', 'tb_neumatico', 'CARRY', 9.5, 'goma', 'superficie', neumatico_pie(0, 0.31, 0.0, ancho=0.2))
