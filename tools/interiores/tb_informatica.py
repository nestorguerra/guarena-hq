# The computer-and-phone shop's objects (family «tiendas_b»): the counter, laptops and PCs on display tables, phone stands,
# the slat-wall of accessories, the repair bench with its magnifier lamp, shelves of parts and accessories in their packs.
# Ids start with «inf_». No real brand: invented models, plain colours, painted screens.
from tb_base import *

PLATA, GRIS_I, NEGRO_I = '#c3c7ca', '#7a8086', '#2e2e34'
AZUL_I = '#1f6a9a'
PANT_LUZ = '#5a8ab8'

# ---- counter and fixtures
obj('inf_mostrador', 'Mostrador de cristal con accesorios (1,2 m)', 'mostrador', 'FIXED', 150, 'cristal', 'suelo', [
    caja(1.2, 0.7, 0.62, y=0.35, z=-0.02, c='#3a3e46'), caja(1.2, 0.04, 0.66, y=0.72, z=0.0, c='#e6e8ea'), caja(1.14, 0.3, 0.012, y=0.35, z=0.29, c=AZUL_I), caja(1.2, 0.08, 0.012, y=0.04, z=0.29, c=DARK),
    caja(1.14, 0.2, 0.01, y=0.86, z=0.3, c=GLASS, m='cristal'), caja(1.14, 0.18, 0.012, y=0.84, z=-0.28, c=GLASS, m='cristal'), caja(1.2, 0.012, 0.6, y=0.95, z=0.0, c=GLASS, m='cristal')],
    motivo_fijo='estructural', superficies=[sup(0.96, 0.04)], nota='un mostrador bajo con cubierta de cristal: la caja y las tarjetas SIM')
obj('inf_mesa_exposicion', 'Mesa de exposición (1,6 m)', 'mesa', 'PUSH', 40, 'madera', 'suelo', [
    caja(1.6, 0.05, 0.7, y=0.775, c='#e8e9ea')] + [caja(0.05, 0.75, 0.05, x=sx * 0.75, y=0.375, z=sz * 0.3, c='#5a626a', m='metal') for sx in (-1, 1) for sz in (-1, 1)] + [caja(1.5, 0.03, 0.6, y=0.25, c='#c9ccce')],
    superficies=[sup(0.8, 0.06), sup(0.265, 0.06)], nota='para los portátiles y los móviles de prueba')
obj('inf_mesa_moviles', 'Mesa expositora de teléfonos (1,2 m)', 'mesa', 'PUSH', 30, 'madera', 'suelo', [
    caja(1.2, 0.05, 0.6, y=0.875, c='#f2f2f0')] + [caja(0.05, 0.85, 0.05, x=sx * 0.55, y=0.425, z=sz * 0.25, c='#5a626a', m='metal') for sx in (-1, 1) for sz in (-1, 1)] + [caja(1.1, 0.03, 0.5, y=0.3, c='#d8dadc')],
    superficies=[sup(0.9, 0.06), sup(0.315, 0.06)])
obj('inf_puesto_pc_exp', 'Puesto de ordenador de muestra', 'mueble', None, 45, 'madera', 'suelo', [
    caja(1.3, 0.04, 0.7, y=0.75, z=0.35, c='#e8e9ea'), caja(0.05, 0.73, 0.65, x=-0.6, y=0.365, z=0.35, c='#8a9096', m='metal'), caja(0.05, 0.73, 0.65, x=0.6, y=0.365, z=0.35, c='#8a9096', m='metal'), caja(1.2, 0.3, 0.012, y=0.55, z=0.03, c='#8a9096', m='metal'),
    caja(0.55, 0.34, 0.025, y=1.17, z=0.2, c=NEGRO_I, m='plastico'), caja(0.5, 0.29, 0.004, y=1.17, z=0.214, c=PANT_LUZ, m='plastico', luz=True), caja(0.05, 0.14, 0.04, y=0.89, z=0.2, c=NEGRO_I, m='plastico'),
    caja(0.44, 0.012, 0.14, y=0.776, z=0.55, c='#d8dadc', m='plastico'), caja(0.2, 0.44, 0.45, x=0.45, y=1.0, z=0.4, c='#2a2e38', m='plastico'), caja(0.012, 0.3, 0.3, x=0.349, y=1.0, z=0.4, c='#7a9ab8', m='cristal')],
    superficies=[sup(0.77, 0.05)], nota='una mesa con monitor, teclado y torre, para probar')
estantes('inf_estanteria_accesorios', 'Estantería de accesorios (1 m)', 1.0, 0.36, [0.35, 0.7, 1.05, 1.4, 1.75], 1.95, c='#3a3e46', cp='#d8dadc', masa=45, nota='baldas de 33 cm para las cajas pequeñas')
estantes('inf_estanteria_piezas', 'Estantería de piezas y cajas (1 m)', 1.0, 0.45, [0.4, 0.8, 1.2, 1.6], 1.8, c='#8a9096', cp='#c3c7ca', masa=40)
obj('inf_banco_reparacion', 'Banco de reparaciones con lámpara de lupa', 'tb_banco_trabajo', 'PUSH', 70, 'metal', 'suelo', [
    caja(1.6, 0.05, 0.75, y=0.88, z=0.375, c='#d8dadc')] + [caja(0.05, 0.86, 0.05, x=sx * 0.75, y=0.43, z=0.06 + (sz + 1) * 0.3, c='#5a626a', m='metal') for sx in (-1, 1) for sz in (-1, 1)] + [
    caja(1.5, 0.03, 0.65, y=0.28, z=0.375, c='#8a9096', m='metal'), caja(0.9, 0.003, 0.5, x=-0.2, y=0.906, z=0.4, c='#3a8a5a', m='goma'), caja(1.6, 0.4, 0.02, y=1.35, z=0.01, c='#5a626a', m='metal'),
    cil(0.02, 0.02, 0.5, x=0.6, y=1.15, z=0.15, c=STEEL, m='metal', seg=8), caja(0.02, 0.02, 0.4, x=0.6, y=1.4, z=0.3, c=STEEL, m='metal'), cil(0.12, 0.12, 0.04, x=0.6, y=1.4, z=0.48, c='#f2efe6', m='plastico', r=[90, 0, 0], seg=16), cil(0.1, 0.1, 0.01, x=0.6, y=1.4, z=0.5, c=GLASS, m='cristal', r=[90, 0, 0], seg=16)],
    superficies=[sup(0.905, 0.05)], nota='con alfombrilla antiestática y la lupa con luz')
obj('inf_taburete_reparacion', 'Taburete giratorio de taller', 'taburete', 'PICKUP', 4.2, 'metal', 'suelo', [
    cil(0.19, 0.19, 0.06, y=0.6, c='#2e2e34', m='plastico', seg=12), cil(0.03, 0.03, 0.5, y=0.3, c=STEEL, m='metal', seg=8), cil(0.25, 0.25, 0.03, y=0.015, c='#5a626a', m='metal', seg=12)],
    modificadores=['SEAT'], asientos=[{'p': [0, 0.64, 0], 'h': 0.64, 'anim': 'taburete_alto'}])
obj('inf_cajonera_piezas', 'Cajonera de piezas con cajoncitos', 'mueble', 'CARRY', 14, 'plastico', 'suelo', [
    caja(0.36, 0.5, 0.3, y=0.25, c='#8a9096', m='plastico')] + [caja(0.15, 0.08, 0.012, x=(i % 2 - 0.5) * 0.17, y=0.07 + (i // 2) * 0.095, z=0.156, c=['#c0302a', '#2c5aa0', '#d8a020', '#3a8a5a', '#e8e4d8'][(i + i // 2) % 5], m='plastico') for i in range(10)],
    superficies=[sup(0.5, 0.03)], nota='cajones de plástico con tornillos y conectores')
obj('inf_rotulo', 'Rótulo interior de la tienda de informática', 'decoracion', 'PICKUP', 3, 'madera', 'pared', [
    caja(1.3, 0.34, 0.03, y=2.5, z=0.015, c='#14243a'), plano(1.24, 0.28, y=2.5, z=0.033, tex={'tipo': 'rotulo_tb', 'estilo': 'informatica', 'rotulo_local': True})])
for k, (n_, d1) in {'movil': ('Cartel de móviles libres', 'movil'), 'portatil': ('Cartel de portátiles', 'portatil')}.items():
    obj('inf_cartel_' + k, n_, 'cuadro', 'PICKUP', 1.2, 'papel', 'pared', [
        caja(0.5, 0.7, 0.025, y=1.7, z=0.0125, c='#2a2420'), plano(0.44, 0.64, y=1.7, z=0.027, tex={'tipo': 'cartel_tb', 'dibujo': d1})])
obj('inf_pantalla_precios', 'Pantalla de ofertas del mes', 'pantalla', 'FIXED', 8, 'plastico', 'pared', [
    caja(0.9, 0.52, 0.05, y=2.1, z=0.025, c='#2a2e38', m='plastico'), plano(0.84, 0.47, y=2.1, z=0.052, tex={'tipo': 'pantalla_tb', 'estilo': 'precios_inf'}, luz=True)], motivo_fijo=FIJO)
obj('inf_pantalla_pared', 'Monitor grande colgado con el escritorio', 'pantalla', 'FIXED', 10, 'plastico', 'pared', [
    caja(1.2, 0.7, 0.04, y=1.6, z=0.02, c='#2a2e38', m='plastico'), plano(1.16, 0.66, y=1.6, z=0.042, tex={'tipo': 'pantalla_tb', 'estilo': 'escritorio'}, luz=True)], motivo_fijo=FIJO)

# ---- laptops, monitors, towers, printers: boxy, with painted-glow screens (one colour of light: one mesh)
def portatil(id, nombre, ancho, c, masa=2.0):
    d = ancho * 0.68
    P = [caja(ancho, 0.02, d, y=0.01, z=0.0, c=c, m='metal'), caja(ancho * 0.84, 0.004, d * 0.4, y=0.022, z=d * 0.2, c='#2e2e34', m='plastico'), caja(ancho * 0.84, 0.003, d * 0.5, y=0.0235, z=-d * 0.2, c='#3a3e46', m='plastico'),
         caja(ancho * 0.3, 0.003, d * 0.25, y=0.0245, z=d * 0.34, c='#d8dadc', m='plastico'),
         caja(ancho, d * 0.78, 0.012, y=0.02 + d * 0.39 * 0.98, z=-d * 0.5 - d * 0.07, c=c, m='metal', r=[-14, 0, 0]), caja(ancho * 0.92, d * 0.68, 0.004, y=0.02 + d * 0.39 * 0.98, z=-d * 0.5 - d * 0.07 + 0.01, c=PANT_LUZ, m='plastico', luz=True, r=[-14, 0, 0])]
    obj(id, nombre, 'informatica', 'PICKUP', masa, 'metal', 'superficie', P)
portatil('inf_portatil_13', 'Portátil de 13 pulgadas (plata)', 0.31, PLATA, 1.3)
portatil('inf_portatil_15', 'Portátil de 15 pulgadas (gris)', 0.36, GRIS_I, 1.9)
portatil('inf_portatil_17', 'Portátil de 17 pulgadas (negro)', 0.4, NEGRO_I, 2.7)
def monitor(id, nombre, ancho, c='#2a2e38'):
    h = ancho * 0.56
    obj(id, nombre, 'informatica', 'PICKUP', round(ancho * 7.5, 1), 'plastico', 'superficie', [
        caja(ancho, h, 0.03, y=0.17 + h / 2, z=0.0, c=c, m='plastico'), caja(ancho - 0.03, h - 0.03, 0.004, y=0.17 + h / 2, z=0.017, c=PANT_LUZ, m='plastico', luz=True),
        caja(0.06, 0.15, 0.03, y=0.095, z=-0.03, c=c, m='plastico'), caja(0.28, 0.014, 0.2, y=0.007, z=0.0, c=c, m='plastico')])
monitor('inf_monitor_22', 'Monitor de 22 pulgadas', 0.5)
monitor('inf_monitor_24', 'Monitor de 24 pulgadas', 0.54)
monitor('inf_monitor_27', 'Monitor de 27 pulgadas', 0.62)
obj('inf_torre_pc', 'Torre de ordenador con ventana lateral', 'informatica', 'CARRY', 9, 'metal', 'suelo', [
    caja(0.2, 0.44, 0.45, y=0.22, z=0.0, c='#2a2e38', m='metal'), caja(0.012, 0.32, 0.34, x=0.103, y=0.23, z=0.0, c='#7a9ab8', m='cristal'), caja(0.012, 0.03, 0.2, x=0.103, y=0.15, z=0.0, c='#3a8a5a', m='plastico', luz=True),
    caja(0.14, 0.02, 0.012, x=0.0, y=0.4, z=0.231, c='#6a6e78', m='plastico'), cil(0.012, 0.012, 0.004, x=0.06, y=0.36, z=0.232, c='#7fe0ff', m='plastico', r=[90, 0, 0], seg=6, luz=True)])
obj('inf_todo_en_uno', 'Ordenador todo en uno', 'informatica', 'CARRY', 8, 'plastico', 'superficie', [
    caja(0.6, 0.38, 0.03, y=0.33, z=0.0, c='#e8e8ea', m='plastico'), caja(0.56, 0.33, 0.004, y=0.34, z=0.017, c=PANT_LUZ, m='plastico', luz=True), caja(0.08, 0.16, 0.03, y=0.08, z=-0.02, c='#d8dadc', m='plastico'), caja(0.26, 0.016, 0.2, y=0.008, z=0.0, c='#d8dadc', m='plastico')])
obj('inf_impresora', 'Impresora multifunción de tinta', 'informatica', 'CARRY', 6, 'plastico', 'superficie', [
    caja(0.45, 0.17, 0.35, y=0.085, c='#e8e8ea', m='plastico'), caja(0.4, 0.015, 0.3, y=0.178, c='#c3c7ca', m='plastico'), caja(0.3, 0.06, 0.003, y=0.12, z=0.176, c='#2e2e34', m='plastico'), caja(0.08, 0.03, 0.004, x=0.14, y=0.14, z=0.178, c='#7fe0ff', m='plastico', luz=True)])
obj('inf_router', 'Router con antenas', 'informatica', 'PICKUP', 0.8, 'plastico', 'superficie', [
    caja(0.22, 0.04, 0.16, y=0.02, c='#e8e8ea', m='plastico')] + [caja(0.012, 0.2, 0.012, x=sx * 0.09, y=0.14, z=-0.05, c='#2e2e34', m='plastico') for sx in (-1, 1)] + [caja(0.02, 0.006, 0.002, x=-0.08 + i * 0.03, y=0.025, z=0.081, c='#3adf6a', m='plastico', luz=True) for i in range(3)])
obj('inf_teclado_raton', 'Teclado y ratón inalámbricos', 'informatica', 'PICKUP', 0.9, 'plastico', 'superficie', [
    caja(0.42, 0.02, 0.14, y=0.01, c='#2e2e34', m='plastico'), caja(0.4, 0.004, 0.12, y=0.022, c='#4a4e58', m='plastico'), caja(0.06, 0.03, 0.1, x=0.3, y=0.015, z=0.0, c='#2e2e34', m='plastico')])
obj('inf_disco_duro', 'Discos duros externos', 'informatica', 'PICKUP', 0.6, 'plastico', 'superficie', [
    caja(0.08, 0.015, 0.12, x=-0.05, y=0.0075, c='#2e2e34', m='plastico'), caja(0.08, 0.015, 0.12, x=0.05, y=0.0075, c='#c0302a', m='plastico')])
obj('inf_pendrives_exp', 'Expositor de memorias USB y tarjetas', 'tb_accesorio', 'PICKUP', 0.6, 'plastico', 'superficie', [
    caja(0.26, 0.015, 0.14, y=0.0075, c='#2e2e34', m='plastico'), caja(0.26, 0.16, 0.012, y=0.095, z=-0.06, c='#1f6a9a', m='plastico')] + [caja(0.03, 0.06, 0.012, x=-0.1 + i * 0.05, y=0.12 - (i % 2) * 0.05, z=-0.05, c=['#c0302a', '#e8e4d8', '#2e2e34', '#d8a020', '#3a8a5a'][i], m='plastico') for i in range(5)])
obj('inf_exp_sim', 'Expositor de tarjetas SIM y recargas', 'papel', 'PICKUP', 0.3, 'papel', 'superficie', [
    caja(0.22, 0.012, 0.12, y=0.006, c='#2e2e34', m='plastico'), caja(0.22, 0.14, 0.01, y=0.08, z=-0.05, c='#2c8ab0', m='plastico', r=[-8, 0, 0])] + [caja(0.045, 0.06, 0.004, x=-0.07 + i * 0.07, y=0.09, z=-0.04, c=c, m='papel', r=[-8, 0, 0]) for i, c in enumerate(['#f2c230', '#e8e4d8', '#c0302a'])])

# ---- phones: slabs on little stands (the screens glow in one colour: one mesh)
def movil(id, nombre, c, w=0.072, h=0.152):
    obj(id, nombre, 'tb_telefono', 'PICKUP', 0.22, 'plastico', 'superficie', [
        caja(0.07, 0.012, 0.08, y=0.006, c='#e8e8ea', m='plastico'), caja(w, h, 0.008, y=0.012 + h / 2 * 0.95, z=-0.02, c=c, m='plastico', r=[-18, 0, 0]), caja(w - 0.008, h - 0.012, 0.003, y=0.012 + h / 2 * 0.95, z=-0.016, c=PANT_LUZ, m='plastico', luz=True, r=[-18, 0, 0])])
for k, (n_, c) in {'negro': ('Teléfono móvil negro', '#2a2a2e'), 'azul': ('Teléfono móvil azul', '#2c5aa0'), 'blanco': ('Teléfono móvil blanco', '#e8e8e8'), 'rojo': ('Teléfono móvil rojo', '#b3342a'), 'verde': ('Teléfono móvil verde', '#3a7a5a'), 'plata': ('Teléfono móvil plata', '#b9bec2')}.items():
    movil('inf_movil_' + k, n_, c)
obj('inf_expositor_moviles', 'Expositor escalonado de móviles', 'tb_accesorio', 'PICKUP', 2.9, 'plastico', 'superficie', [
    caja(0.9, 0.18, 0.5, y=0.09, c='#e8e8ea', m='plastico'), caja(0.9, 0.06, 0.012, y=0.21, z=0.2, c='#1f6a9a', m='plastico')] + [p for i in range(6) for j in range(2) for p in (
        caja(0.07, 0.15, 0.008, x=-0.35 + i * 0.14, y=0.18 + 0.075, z=-0.1 + j * 0.22, c=['#2a2a2e', '#2c5aa0', '#e8e8e8', '#b3342a', '#3a7a5a', '#b9bec2'][(i + j) % 6], m='plastico', r=[-14, 0, 0]),
        caja(0.062, 0.138, 0.003, x=-0.35 + i * 0.14, y=0.18 + 0.075, z=-0.1 + j * 0.22 + 0.006, c=PANT_LUZ, m='plastico', luz=True, r=[-14, 0, 0]))],
    nota='doce teléfonos de prueba atados con su cable')
def u_blister(c, c2, w=0.08, h=0.16):
    def f(x, z): return [caja(w, h, 0.02, x=x, y=h / 2, z=z, c=c, m='plastico'), caja(w * 0.8, h * 0.42, 0.022, x=x, y=h * 0.5, z=z, c=c2, m='plastico'), caja(w * 0.6, 0.012, 0.024, x=x, y=h * 0.9, z=z, c='#f2efe6', m='papel')]
    return f
ACCS = [
    ('fundas_negras', 'Fundas de móvil negras', u_blister('#2e2e34', '#4a4e58'), 6, 0.085, 0.16), ('fundas_color', 'Fundas de móvil de colores', u_blister('#3a8a9a', '#e8e4d8'), 6, 0.085, 0.16),
    ('protectores_pantalla', 'Protectores de pantalla', u_blister('#e8e8ea', '#9ab8c8', 0.07, 0.15), 6, 0.075, 0.15), ('cargador_pared', 'Cargadores de pared', u_blister('#e8e8ea', '#3a8a5a', 0.09, 0.14), 5, 0.095, 0.14),
    ('cargador_coche', 'Cargadores de coche', u_blister('#2e2e34', '#c0302a', 0.07, 0.14), 6, 0.075, 0.14), ('cables_usb', 'Cables USB enrollados', u_blister('#2c5aa0', '#e8e4d8', 0.08, 0.17), 6, 0.085, 0.17),
    ('auriculares_cable', 'Auriculares de cable', u_blister('#e8e8ea', '#2e2e34', 0.1, 0.18), 5, 0.105, 0.18), ('auriculares_bt', 'Auriculares bluetooth', u_blister('#2e2e34', '#2c8ab0', 0.1, 0.18), 5, 0.105, 0.18),
    ('bateria_externa', 'Baterías externas', u_blister('#e8e4d8', '#d8a020', 0.08, 0.16), 5, 0.085, 0.16), ('raton', 'Ratones con cable', u_blister('#2e2e34', '#d8dadc', 0.09, 0.14), 5, 0.095, 0.14),
    ('alfombrilla', 'Alfombrillas de ratón', u_blister('#3a3e46', '#c0302a', 0.1, 0.1), 4, 0.105, 0.1), ('webcam', 'Cámaras web', u_blister('#2e2e34', '#c3c7ca', 0.1, 0.12), 4, 0.105, 0.12),
    ('memoria_sd', 'Tarjetas de memoria', u_blister('#c0302a', '#e8e4d8', 0.05, 0.1), 8, 0.055, 0.1), ('soporte_movil', 'Soportes de móvil para el coche', u_blister('#e8e8ea', '#2e2e34', 0.08, 0.14), 6, 0.085, 0.14),
    ('radio_bolsillo', 'Radios de bolsillo', u_blister('#c0302a', '#e8e4d8', 0.09, 0.14), 5, 0.095, 0.14), ('linterna_led', 'Linternas LED recargables', u_blister('#d8a020', '#2e2e34', 0.07, 0.2), 6, 0.075, 0.2),
    ('lamparita_usb', 'Lamparitas USB flexibles', u_blister('#e8e8ea', '#3a8a5a', 0.08, 0.2), 5, 0.085, 0.2),
]
for k, n_, unit, nx, dx, h in ACCS:
    regis('inf_acc_' + k, n_, 'tb_accesorio', unit, nx, 2, dx, 0.03, h, 0.25, '#e0e0e0', 0.08, mat='plastico', hf=0.9)
# slat-walls of accessories, hung on the wall (blister packs painted on the panel)
def panel_acc(id, nombre, paleta):
    P = [caja(1.2, 1.9, 0.03, y=1.25, z=0.015, c='#3a3e46')] + [caja(1.18, 0.012, 0.012, y=0.35 + k * 0.1, z=0.036, c='#2e2e34', m='plastico') for k in range(16)]
    for r_ in range(5):
        for c_ in range(5):
            P.append(caja(0.15, 0.2, 0.02, x=-0.45 + c_ * 0.225, y=0.55 + r_ * 0.33, z=0.045, c=paleta[(r_ + c_) % len(paleta)], m='plastico'))
            P.append(caja(0.11, 0.07, 0.022, x=-0.45 + c_ * 0.225, y=0.6 + r_ * 0.33, z=0.046, c='#f2efe6', m='papel'))
    obj(id, nombre, 'tb_accesorio', 'FIXED', 3.0, 'plastico', 'pared', P, motivo_fijo=FIJO, nota='panel ranurado con blísteres')
panel_acc('inf_panel_fundas', 'Panel de fundas y protectores', ['#2e2e34', '#2c5aa0', '#c0302a', '#3a8a5a', '#e8c040'])
panel_acc('inf_panel_cables', 'Panel de cables y cargadores', ['#e8e8ea', '#2e2e34', '#1f6a9a', '#d8a020'])
panel_acc('inf_panel_auriculares', 'Panel de auriculares', ['#2e2e34', '#e8e8ea', '#c0302a', '#2c8ab0'])
# small things for benches
def util(id, nombre, masa, P): obj(id, nombre, 'informatica', 'PICKUP', masa, 'metal', 'superficie', P)
util('inf_soldador', 'Soldador con su soporte', 0.5, [caja(0.1, 0.03, 0.1, y=0.015, c='#5a626a', m='metal'), cil(0.012, 0.012, 0.2, x=0.02, y=0.07, z=0.0, c='#d8822a', m='plastico', r=[0, 0, 70], seg=6), caja(0.012, 0.012, 0.03, x=-0.08, y=0.105, z=0.0, c=STEEL, m='metal')])
util('inf_destornilladores', 'Juego de destornilladores de precisión', 0.3, [caja(0.2, 0.015, 0.1, y=0.0075, c='#2e2e34', m='plastico')] + [cil(0.007, 0.007, 0.09, x=-0.07 + i * 0.035, y=0.02, z=0.0, c=['#c0302a', '#2c5aa0', '#d8a020', '#3a8a5a', '#e8e4d8'][i], m='plastico', r=[90, 0, 0], seg=6) for i in range(5)])
util('inf_placa_madre', 'Placa base y piezas sobre la alfombrilla', 0.6, [caja(0.24, 0.012, 0.24, y=0.006, c='#2a6a4a', m='plastico'), caja(0.05, 0.02, 0.05, x=-0.04, y=0.022, z=-0.04, c='#c3c7ca', m='metal'), caja(0.04, 0.012, 0.12, x=0.07, y=0.018, z=0.0, c='#2a2e38', m='plastico')])
util('inf_movil_abierto', 'Móvil abierto en reparación', 0.3, [caja(0.075, 0.008, 0.155, y=0.004, c='#2a2a2e', m='plastico'), caja(0.05, 0.004, 0.08, x=0.0, y=0.01, z=0.0, c='#2a6a4a', m='plastico'), caja(0.016, 0.002, 0.016, x=0.0, y=0.013, z=0.0, c='#c3c7ca', m='metal')])
util('inf_caja_pc', 'Caja de ordenador sin abrir', 4.5, [caja(0.32, 0.4, 0.2, y=0.2, c='#c9a46e', m='papel'), caja(0.2, 0.1, 0.004, y=0.24, z=0.102, c='#f2efe6', m='papel')])
obj('inf_caja_portatil', 'Cajas de portátil apiladas', 'caja', 'PICKUP', 3.8, 'papel', 'suelo', [
    caja(0.4, 0.07, 0.3, y=0.035, c='#c9a46e', m='papel'), caja(0.4, 0.07, 0.3, y=0.105, c='#b8925c', m='papel'), caja(0.4, 0.07, 0.3, y=0.175, c='#c9a46e', m='papel'), caja(0.3, 0.02, 0.004, y=0.1, z=0.152, c='#f2efe6', m='papel')])
