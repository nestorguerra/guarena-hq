# The hairdresser's objects (family «tiendas_b»): reception counter, styling chairs and mirror stations, backwash units,
# hood dryers, trolleys, tools and bottles, the waiting corner and the back room. Ids start with «pel_».
from tb_base import *

ROSA, ROSA_D, NEGRO = '#d9a0b0', '#b9707f', '#2e2e32'
CUERO = '#34343a'

# ---- the counter: a small reception desk, white lacquer with a dark top and a rose front
obj('pel_mostrador_caja', 'Mostrador de recepción (1,2 m)', 'mostrador', 'FIXED', 120, 'madera', 'suelo', [
    caja(1.2, 0.9, 0.5, y=0.45, z=-0.02, c='#ece6dc'), caja(1.22, 0.04, 0.56, y=0.92, z=0.0, c='#3a3a40'), caja(1.14, 0.5, 0.012, y=0.5, z=0.236, c=ROSA),
    caja(1.2, 0.07, 0.012, y=0.035, z=0.236, c=DARK), caja(0.6, 0.1, 0.012, y=0.82, z=0.236, c='#d6cebf')],
    motivo_fijo='estructural', superficies=[sup(0.94, 0.04)], nota='el mostrador de recepción: la caja, las agendas y las colonias')
obj('pel_tpv', 'Terminal de cobro con pantalla táctil', 'informatica', 'PICKUP', 1.6, 'plastico', 'superficie', [
    caja(0.28, 0.03, 0.22, y=0.015, c='#d6d9db', m='metal'), caja(0.05, 0.14, 0.04, y=0.1, z=-0.06, c='#2e2e32', m='plastico'), caja(0.26, 0.17, 0.025, y=0.2, z=-0.06, c='#2e2e32', m='plastico', r=[-8, 0, 0]),
    caja(0.23, 0.13, 0.004, y=0.2, z=-0.046, c='#7aa0c8', m='plastico', luz=True, r=[-8, 0, 0])])
obj('pel_agenda', 'Agenda de citas abierta', 'papel', 'PICKUP', 0.5, 'papel', 'superficie', [
    caja(0.22, 0.02, 0.16, y=0.01, c='#7a3a4a', m='papel'), caja(0.1, 0.012, 0.15, x=-0.055, y=0.026, c='#f2efe6', m='papel'), caja(0.1, 0.012, 0.15, x=0.055, y=0.026, c='#f2efe6', m='papel')])

# ---- styling chair: black upholstery, chrome base and footrest; the person sits at its origin
def sillon_corte(id, nombre, tapiz, cromo=STEEL):
    P = [cil(0.31, 0.31, 0.03, y=0.015, c=oscuro(cromo, 0.8), m='metal', seg=16), cil(0.07, 0.09, 0.4, y=0.23, c=cromo, m='metal', seg=10),
         caja(0.52, 0.09, 0.5, y=0.5, z=0.0, c=tapiz, m='tela'), caja(0.5, 0.62, 0.1, y=0.88, z=-0.22, c=tapiz, m='tela'), caja(0.3, 0.16, 0.09, y=1.27, z=-0.22, c=tapiz, m='tela'),
         caja(0.04, 0.08, 0.04, y=1.2, z=-0.23, c=cromo, m='metal'),
         caja(0.07, 0.06, 0.44, x=-0.3, y=0.68, z=0.0, c=cromo, m='metal'), caja(0.07, 0.06, 0.44, x=0.3, y=0.68, z=0.0, c=cromo, m='metal'),
         caja(0.04, 0.2, 0.04, x=-0.3, y=0.58, z=-0.18, c=cromo, m='metal'), caja(0.04, 0.2, 0.04, x=0.3, y=0.58, z=-0.18, c=cromo, m='metal'),
         caja(0.36, 0.03, 0.2, y=0.2, z=0.5, c=cromo, m='metal', r=[-14, 0, 0]), cil(0.012, 0.012, 0.28, y=0.33, z=0.32, c=cromo, m='metal', r=[-48, 0, 0], seg=8)]
    obj(id, nombre, 'tb_peluqueria', None, 34, 'metal', 'suelo', P, modificadores=['SEAT'], asientos=[{'p': [0, 0.55, 0.0], 'h': 0.55, 'anim': 'silla'}])
sillon_corte('pel_sillon_corte_negro', 'Sillón de corte negro con reposapiés', CUERO)
sillon_corte('pel_sillon_corte_rosa', 'Sillón de corte rosa con reposapiés', '#c98b9c')
sillon_corte('pel_sillon_corte_blanco', 'Sillón de corte blanco con reposapiés', '#e4dfd6')

# ---- station: a console under a wall mirror, with its lit strip
def estacion(id, nombre, c1, c2, anch=0.9):
    P = [caja(anch, 0.8, 0.42, y=0.4, z=0.21, c=c1), caja(anch + 0.02, 0.04, 0.45, y=0.82, z=0.225, c=c2),
         caja(anch - 0.1, 0.17, 0.01, x=0, y=0.62, z=0.425, c=oscuro(c1, 0.92)), caja(anch - 0.1, 0.17, 0.01, y=0.4, z=0.425, c=oscuro(c1, 0.92)), caja(anch - 0.1, 0.17, 0.01, y=0.18, z=0.425, c=oscuro(c1, 0.92)),
         caja(0.12, 0.012, 0.016, y=0.65, z=0.435, c=STEEL, m='metal'), caja(0.12, 0.012, 0.016, y=0.43, z=0.435, c=STEEL, m='metal'), caja(0.12, 0.012, 0.016, y=0.21, z=0.435, c=STEEL, m='metal'),
         caja(anch - 0.04, 1.05, 0.03, y=1.5, z=0.015, c='#6a5a4a'), caja(anch - 0.1, 0.99, 0.006, y=1.5, z=0.033, c=MIRROR, m='metal'),
         caja(anch - 0.2, 0.025, 0.04, y=2.04, z=0.05, c='#fff3d6', m='plastico', luz=True)]
    obj(id, nombre, 'tb_peluqueria', None, 48, 'madera', 'suelo', P, superficies=[sup(0.84, 0.05)], nota='tocador con espejo y tira de luz')
estacion('pel_estacion_blanca', 'Puesto de peinado blanco con espejo', '#ece6dc', '#d8d2c6')
estacion('pel_estacion_madera', 'Puesto de peinado de madera con espejo', '#a8825a', '#8a6a46')
estacion('pel_estacion_negra', 'Puesto de peinado negro con espejo', '#3a3a40', '#4a4a50')

# ---- backwash unit: the basin against the wall, the chair reclined towards it
def lavacabezas(id, nombre, tapiz, ceramica='#f1efe9'):
    P = [caja(0.6, 0.78, 0.5, y=0.39, z=0.26, c='#e4dfd6'), caja(0.64, 0.08, 0.54, y=0.82, z=0.27, c=ceramica, m='ceramica'), caja(0.4, 0.02, 0.32, y=0.87, z=0.25, c='#bfc6c8', m='ceramica'),
         caja(0.2, 0.05, 0.1, y=0.86, z=0.5, c='#d3d8d9', m='ceramica'), cil(0.015, 0.015, 0.22, y=0.99, z=0.04, c=STEEL, seg=8), cil(0.012, 0.012, 0.16, y=1.1, z=0.13, c=STEEL, r=[90, 0, 0], seg=8),
         cil(0.01, 0.01, 0.4, x=0.2, y=1.0, z=0.12, c='#2b2b2e', m='goma', r=[0, 0, 40], seg=6),
         cil(0.2, 0.22, 0.03, y=0.015, z=1.0, c=STEEL, m='metal', seg=14), cil(0.06, 0.08, 0.38, y=0.22, z=1.0, c=STEEL, m='metal', seg=10),
         caja(0.52, 0.1, 0.5, y=0.5, z=1.0, c=tapiz, m='tela'), caja(0.5, 0.62, 0.1, y=0.82, z=0.7, c=tapiz, m='tela', r=[-34, 0, 0]), caja(0.44, 0.07, 0.42, y=0.34, z=1.45, c=tapiz, m='tela', r=[22, 0, 0]),
         caja(0.05, 0.05, 0.4, x=-0.3, y=0.66, z=1.0, c=STEEL, m='metal'), caja(0.05, 0.05, 0.4, x=0.3, y=0.66, z=1.0, c=STEEL, m='metal')]
    obj(id, nombre, 'tb_peluqueria', None, 78, 'ceramica', 'suelo', P, nota='lavacabezas con sillón reclinable: la nuca sobre la pila')
lavacabezas('pel_lavacabezas_negro', 'Lavacabezas con sillón negro', CUERO)
lavacabezas('pel_lavacabezas_rosa', 'Lavacabezas con sillón rosa', '#c98b9c')

# ---- hood dryer on its stand, with the chair under it
def secador_casco(id, nombre, c):
    P = [cil(0.27, 0.27, 0.03, y=0.015, z=-0.22, c=STEEL, m='metal', seg=14), cil(0.035, 0.035, 1.55, y=0.8, z=-0.22, c=STEEL, m='metal', seg=8),
         caja(0.05, 0.05, 0.42, y=1.57, z=-0.0, c=STEEL, m='metal'), cil(0.03, 0.03, 0.14, y=1.5, z=0.17, c=STEEL, m='metal', seg=8),
         esf(0.24, 0, 1.3, 0.17, c=c, m='plastico', s=[1.0, 1.0, 1.0]), cil(0.15, 0.2, 0.05, y=1.12, z=0.2, c=oscuro(c, 0.9), m='plastico', seg=12),
         caja(0.1, 0.05, 0.03, x=0.18, y=1.5, z=-0.2, c='#2b2b2e', m='plastico'),
         cil(0.2, 0.2, 0.03, y=0.015, z=0.28, c=STEEL, m='metal', seg=12), cil(0.05, 0.06, 0.28, y=0.17, z=0.28, c=STEEL, m='metal', seg=8), caja(0.46, 0.08, 0.44, y=0.46, z=0.28, c=CUERO, m='tela'),
         caja(0.46, 0.5, 0.08, y=0.78, z=0.08, c=CUERO, m='tela')]
    obj(id, nombre, 'tb_peluqueria', None, 24, 'metal', 'suelo', P, modificadores=['SEAT'], asientos=[{'p': [0, 0.5, 0.28], 'h': 0.5, 'anim': 'silla'}])
secador_casco('pel_secador_casco_crema', 'Secador de casco con sillón (crema)', '#e4d8c4')
secador_casco('pel_secador_casco_rosa', 'Secador de casco con sillón (rosa)', '#e0b4c0')

# ---- trolley of tools: three trays, a handle, castors
def carrito(id, nombre, c):
    P = [caja(0.04, 0.82, 0.04, x=sx * 0.2, y=0.46, z=sz * 0.13, c=STEEL, m='metal') for sx in (-1, 1) for sz in (-1, 1)]
    P += [caja(0.46, 0.025, 0.34, y=0.15, c=c, m='plastico'), caja(0.46, 0.025, 0.34, y=0.47, c=c, m='plastico'), caja(0.46, 0.025, 0.34, y=0.8, c=c, m='plastico'), caja(0.46, 0.03, 0.03, y=0.83, z=0.17, c=c, m='plastico'), caja(0.46, 0.03, 0.03, y=0.83, z=-0.17, c=c, m='plastico')]
    P += [cil(0.025, 0.025, 0.02, x=sx * 0.2, y=0.025, z=sz * 0.13, c='#2b2b2e', m='goma', r=[0, 0, 90], seg=8) for sx in (-1, 1) for sz in (-1, 1)]
    obj(id, nombre, 'tb_peluqueria', None, 7, 'metal', 'suelo', P, superficies=[sup(0.8125, 0.03), sup(0.4825, 0.03)], nota='carrito de las tinturas y las herramientas')
carrito('pel_carrito_blanco', 'Carrito de peluquería blanco', '#eceae4')
carrito('pel_carrito_rosa', 'Carrito de peluquería rosa', ROSA)

# ---- the waiting corner
obj('pel_sofa_espera', 'Sofá de espera de dos plazas', 'sofa', None, 38, 'tela', 'suelo', [
    caja(1.5, 0.28, 0.72, y=0.2, z=0.0, c='#b9707f', m='tela'), caja(1.5, 0.42, 0.18, y=0.62, z=-0.27, c='#b9707f', m='tela'), caja(0.14, 0.34, 0.72, x=-0.68, y=0.45, c='#a8626f', m='tela'), caja(0.14, 0.34, 0.72, x=0.68, y=0.45, c='#a8626f', m='tela'),
    caja(0.6, 0.12, 0.5, x=-0.3, y=0.4, z=0.04, c='#c98b9c', m='tela'), caja(0.6, 0.12, 0.5, x=0.3, y=0.4, z=0.04, c='#c98b9c', m='tela')] + [caja(0.05, 0.08, 0.05, x=sx * 0.7, y=0.04, z=sz * 0.3, c=WOOD_D) for sx in (-1, 1) for sz in (-1, 1)],
    modificadores=['SEAT'], asientos=[{'p': [-0.3, 0.46, 0.05], 'h': 0.46, 'anim': 'sofa'}, {'p': [0.3, 0.46, 0.05], 'h': 0.46, 'anim': 'sofa'}])
obj('pel_mesa_revistas', 'Mesa baja con revistas', 'mesa', None, 12, 'madera', 'suelo', [
    caja(0.8, 0.04, 0.5, y=0.42, c='#8a6a46')] + [caja(0.04, 0.4, 0.04, x=sx * 0.35, y=0.2, z=sz * 0.2, c=WOOD_D) for sx in (-1, 1) for sz in (-1, 1)] + [caja(0.76, 0.02, 0.46, y=0.14, c='#6a4a30')],
    superficies=[sup(0.44, 0.05), sup(0.15, 0.05)])
obj('pel_revistero_pared', 'Revistero de pared', 'decoracion', 'PICKUP', 2.4, 'metal', 'pared', [
    caja(0.4, 0.5, 0.02, y=1.2, z=0.01, c='#d6d9db', m='metal'), caja(0.4, 0.02, 0.1, y=0.97, z=0.05, c='#d6d9db', m='metal'), caja(0.4, 0.02, 0.1, y=1.2, z=0.05, c='#d6d9db', m='metal'), caja(0.4, 0.02, 0.1, y=1.43, z=0.05, c='#d6d9db', m='metal')]
    + [caja(0.18, 0.2, 0.008, x=x, y=y, z=0.05, c=c, m='papel', r=[-12, 0, 0]) for y in (1.1, 1.33) for x, c in ((-0.1, '#d98a9a'), (0.1, '#7aa0c8'))])

# ---- bottles, tools, towels (small things for the stations, trolleys and the counter)
def frasco_bomba(id, nombre, c, c2, h=0.2, r=0.035):
    obj(id, nombre, 'tb_cosmetico', 'PICKUP', 0.5, 'plastico', 'superficie', [
        cil(r, r, h * 0.78, y=h * 0.39, c=c, m='plastico', seg=8), cil(r + 0.001, r + 0.001, h * 0.34, y=h * 0.4, c=c2, m='papel', seg=8), cil(0.008, 0.008, h * 0.14, y=h * 0.85, c=c2, m='plastico', seg=6),
        caja(0.05, 0.015, 0.02, y=h * 0.94, z=0.012, c=c2, m='plastico')])
frasco_bomba('pel_champu_rosa', 'Champú (bote con bomba, rosa)', '#e8a8b8', '#f4f0e8')
frasco_bomba('pel_champu_verde', 'Champú (bote con bomba, verde)', '#9cc8a0', '#f4f0e8')
frasco_bomba('pel_acondicionador', 'Acondicionador (bote con bomba, malva)', '#b8a0d0', '#f4f0e8', h=0.22)
obj('pel_laca', 'Laca para el cabello (spray)', 'tb_cosmetico', 'PICKUP', 0.35, 'metal', 'superficie', [
    cil(0.032, 0.032, 0.18, y=0.09, c='#c9ced1', m='metal', seg=8), cil(0.033, 0.033, 0.08, y=0.09, c='#d9a0b0', m='papel', seg=8), cil(0.028, 0.032, 0.03, y=0.195, c='#c9ced1', m='metal', seg=8), cil(0.03, 0.03, 0.05, y=0.235, c='#2b2b2e', m='plastico', seg=8)])
obj('pel_pulverizador', 'Pulverizador de agua', 'tb_cosmetico', 'PICKUP', 0.4, 'plastico', 'superficie', [
    cil(0.04, 0.045, 0.16, y=0.08, c='#cfe3ea', m='cristal', seg=8), caja(0.04, 0.05, 0.08, y=0.2, z=0.01, c='#e0b4c0', m='plastico'), cil(0.012, 0.012, 0.07, y=0.185, z=0.07, c='#e0b4c0', m='plastico', r=[90, 0, 0], seg=6)])
obj('pel_bol_tinte', 'Bol de tinte con brocha', 'tb_peluqueria', 'PICKUP', 0.4, 'plastico', 'superficie', [
    cil(0.08, 0.05, 0.05, y=0.025, c='#e8e6e0', m='plastico', seg=12), cil(0.07, 0.07, 0.008, y=0.052, c='#6a2a3a', m='comida', seg=12), cil(0.008, 0.008, 0.2, x=0.04, y=0.085, c='#2b2b2e', m='plastico', r=[0, 0, -55], seg=6)])
obj('pel_tubo_tinte', 'Tubos de tinte', 'tb_cosmetico', 'PICKUP', 0.2, 'plastico', 'superficie', [
    p for z, c in ((-0.05, '#c0392b'), (0.0, '#6a3a22'), (0.05, '#d8b560')) for p in (caja(0.16, 0.022, 0.04, z=z, c=c, m='plastico'), caja(0.02, 0.026, 0.03, x=0.09, z=z, c='#2b2b2e', m='plastico'))])
obj('pel_secador_mano', 'Secador de mano', 'pequeño_electrodomestico', 'PICKUP', 0.6, 'plastico', 'superficie', [
    caja(0.045, 0.13, 0.045, x=-0.03, y=0.065, c='#2e2e32', m='plastico'), cil(0.045, 0.05, 0.2, y=0.17, c='#2e2e32', m='plastico', r=[0, 0, 90], seg=10), cil(0.047, 0.047, 0.01, x=0.105, y=0.17, c=STEEL, m='metal', r=[0, 0, 90], seg=10)])
obj('pel_plancha_pelo', 'Plancha del pelo', 'pequeño_electrodomestico', 'PICKUP', 0.5, 'plastico', 'superficie', [
    caja(0.03, 0.02, 0.26, y=0.012, c='#e0b4c0', m='plastico'), caja(0.03, 0.02, 0.26, y=0.035, c='#e0b4c0', m='plastico'), caja(0.03, 0.045, 0.1, y=0.03, z=-0.18, c='#2e2e32', m='plastico')])
obj('pel_cepillo_redondo', 'Cepillo redondo', 'tb_peluqueria', 'PICKUP', 0.12, 'plastico', 'superficie', [
    cil(0.025, 0.025, 0.08, y=0.025, z=0.1, c='#6a4a30', m='madera', r=[90, 0, 0], seg=8), cil(0.012, 0.012, 0.14, y=0.025, z=-0.04, c='#2e2e32', m='plastico', r=[90, 0, 0], seg=6)])
obj('pel_peine_cola', 'Peine de cola', 'tb_peluqueria', 'PICKUP', 0.04, 'plastico', 'superficie', [caja(0.03, 0.008, 0.22, y=0.004, c='#2e2e32', m='plastico'), caja(0.03, 0.008, 0.1, y=0.004, z=-0.16, c='#d9a0b0', m='plastico')])
obj('pel_tijeras_estuche', 'Estuche de tijeras y navaja', 'tb_peluqueria', 'PICKUP', 0.3, 'tela', 'superficie', [
    caja(0.24, 0.025, 0.12, y=0.0125, c='#34343a', m='tela'), caja(0.22, 0.004, 0.012, y=0.03, z=0.02, c=STEEL, m='metal', r=[0, 12, 0]), caja(0.22, 0.004, 0.012, y=0.03, z=-0.02, c=STEEL, m='metal', r=[0, -10, 0])])
obj('pel_maquinilla', 'Maquinilla de cortar el pelo', 'tb_peluqueria', 'PICKUP', 0.45, 'plastico', 'superficie', [
    caja(0.05, 0.16, 0.04, y=0.08, c='#34343a', m='plastico'), caja(0.045, 0.03, 0.03, y=0.17, z=0.02, c=STEEL, m='metal')])
obj('pel_rulos_bandeja', 'Bandeja de rulos', 'tb_peluqueria', 'PICKUP', 0.6, 'plastico', 'superficie', [
    caja(0.3, 0.02, 0.2, y=0.01, c='#eceae4', m='plastico')] + [cil(0.025, 0.025, 0.07, x=-0.1 + i * 0.065, y=0.055, z=-0.04 + (i % 2) * 0.08, c=c, m='plastico', r=[0, 0, 90], seg=8) for i, c in enumerate(['#d98a9a', '#7aa0c8', '#e6c26a', '#9cc8a0'])])
obj('pel_toallas_dobladas', 'Toallas dobladas', 'textil', 'PICKUP', 0.9, 'tela', 'superficie', [
    caja(0.34, 0.06, 0.24, y=0.03, c='#e9e4da', m='tela'), caja(0.34, 0.06, 0.24, y=0.09, c='#d9a0b0', m='tela'), caja(0.34, 0.06, 0.24, y=0.15, c='#e9e4da', m='tela')])
obj('pel_capa_corte', 'Capa de corte doblada', 'textil', 'PICKUP', 0.4, 'tela', 'superficie', [caja(0.3, 0.05, 0.26, y=0.025, c='#34343a', m='tela'), caja(0.28, 0.02, 0.24, y=0.06, c='#4a4a52', m='tela')])
obj('pel_botes_pinzas', 'Bote de pinzas y horquillas', 'tb_peluqueria', 'PICKUP', 0.2, 'plastico', 'superficie', [
    cil(0.04, 0.04, 0.09, y=0.045, c='#cfe3ea', m='cristal', seg=10), caja(0.07, 0.04, 0.02, y=0.1, z=0.0, c='#34343a', m='plastico', r=[0, 0, 20]), caja(0.07, 0.03, 0.02, y=0.1, z=0.015, c='#d9a0b0', m='plastico', r=[0, 0, -25])])
obj('pel_perfumes_vitrina', 'Colonias en un soporte de cristal', 'tb_cosmetico', 'PICKUP', 1.2, 'cristal', 'superficie', [
    caja(0.42, 0.02, 0.2, y=0.01, c='#e9e4da'), caja(0.4, 0.02, 0.18, y=0.12, c=GLASS, m='cristal')] + [
    p for i, c in enumerate(['#c8a040', '#6a8aa8', '#b3547a', '#7aa07a', '#d8d0c0']) for p in (
        caja(0.06, 0.1, 0.045, x=-0.16 + i * 0.08, y=0.07, z=0.0, c=c, m='cristal'), caja(0.03, 0.025, 0.03, x=-0.16 + i * 0.08, y=0.132, z=0.0, c='#2b2b2e', m='plastico'))],
    nota='colonias a la venta junto a la caja')

# ---- retail shelf of hair products (facings) and a perfume stand
estantes('pel_expositor_pared', 'Expositor de productos capilares (pared)', 0.9, 0.3, [0.4, 0.78, 1.16, 1.54, 1.92], 2.1, c='#e9e4da', cp='#f6f2ea', masa=40)
PEL = [
    ('champu_nutritivo', 'Champús nutritivos', 'bote', '#e8a8b8', 4, 0.075, 0.2),
    ('champu_rizos', 'Champús de rizos', 'bote', '#b8a0d0', 4, 0.075, 0.2),
    ('champu_caspa', 'Champús anticaspa', 'bote', '#7fb8d0', 4, 0.075, 0.2),
    ('mascarilla_capilar', 'Mascarillas capilares', 'tarro', '#d8c8e0', 4, 0.09, 0.1),
    ('serum_puntas', 'Sérum para las puntas', 'frasco', '#d8b560', 6, 0.05, 0.14),
    ('laca_fijacion', 'Lacas de fijación', 'spray', '#c9ced1', 5, 0.06, 0.22),
    ('espuma_volumen', 'Espumas de volumen', 'spray', '#9cc8a0', 5, 0.06, 0.2),
    ('gel_fijador', 'Geles fijadores', 'tubo', '#4a7aa8', 6, 0.055, 0.16),
    ('cera_modeladora', 'Ceras modeladoras', 'tarro', '#e6c26a', 5, 0.08, 0.06),
    ('tinte_caja_castano', 'Cajas de tinte castaño', 'caja', '#6a3a22', 6, 0.065, 0.14),
    ('tinte_caja_rubio', 'Cajas de tinte rubio', 'caja', '#e0c070', 6, 0.065, 0.14),
    ('tinte_caja_rojo', 'Cajas de tinte caoba', 'caja', '#9a2a3a', 6, 0.065, 0.14),
]
for k, n_, forma, c, nx, dx, h in PEL:
    if forma == 'bote': unit = u_botella(0.032, h, c, '#f4f0e8', c, m='plastico')
    elif forma == 'tarro': unit = u_bote(dx * 0.42, h, c, '#f4f0e8')
    elif forma == 'frasco': unit = u_botella(0.02, h, '#d8b560', '#f4f0e8', '#2b2b2e', m='cristal')
    elif forma == 'spray': unit = u_lata(0.028, h, c, '#d9a0b0')
    elif forma == 'tubo': unit = u_tubo(dx * 0.9, h, c, '#f4f0e8')
    else: unit = u_caja(dx * 0.92, h, 0.05, c, '#f4f0e8')
    regis('pel_prod_' + k, n_, 'tb_cosmetico', unit, nx, 3, dx, 0.08, h, 0.26, c, 0.1, mat='plastico')

# ---- the back room
obj('pel_calentador_toallas', 'Calentador de toallas', 'pequeño_electrodomestico', 'FIXED', 12, 'metal', 'pared', [
    caja(0.5, 0.6, 0.18, y=1.2, z=0.09, c='#e8e8e4', m='metal'), caja(0.46, 0.5, 0.02, y=1.2, z=0.19, c='#d8d8d4', m='metal'), caja(0.03, 0.02, 0.005, x=0.18, y=1.46, z=0.18, c='#d9a060', m='plastico', luz=True)], motivo_fijo=FIJO)
obj('pel_esterilizador', 'Esterilizador de herramientas', 'pequeño_electrodomestico', 'PICKUP', 2.6, 'plastico', 'superficie', [
    caja(0.32, 0.14, 0.2, y=0.07, c='#eceae4', m='plastico'), caja(0.28, 0.02, 0.16, y=0.15, c='#7aa0c8', m='cristal'), caja(0.03, 0.015, 0.005, x=0.12, y=0.09, z=0.1, c='#5a9a6a', m='plastico', luz=True)])
obj('pel_cesto_ropa', 'Cesto de toallas sucias', 'recipiente', 'PICKUP', 1.8, 'plastico', 'suelo', [
    cil(0.2, 0.17, 0.5, y=0.25, c='#c8b898', m='plastico', seg=12), cil(0.205, 0.205, 0.03, y=0.51, c='#a89878', m='plastico', seg=12)])
obj('pel_caja_tinte', 'Caja de tintes (reposición)', 'caja', 'PICKUP', 3.5, 'papel', 'superficie', [
    caja(0.4, 0.26, 0.3, y=0.13, c='#c9a46e', m='papel'), plano(0.3, 0.12, y=0.14, z=0.152, c='#d9a0b0', m='papel')])
obj('pel_bidon_oxidante', 'Bidón de oxidante', 'recipiente', 'CARRY', 6, 'plastico', 'suelo', [
    caja(0.24, 0.32, 0.18, y=0.16, c='#e9e4da', m='plastico'), cil(0.03, 0.03, 0.04, x=0.06, y=0.34, c='#d9a0b0', m='plastico', seg=8), caja(0.18, 0.1, 0.004, y=0.16, z=0.092, c='#d9a0b0', m='papel')])

# ---- wall decoration
for k, (n_, d1) in {'a': ('Cartel de peinados «Melena»', 'peinado_a'), 'b': ('Cartel de peinados «Recogido»', 'peinado_b')}.items():
    obj('pel_cartel_peinados_' + k, n_, 'cuadro', 'PICKUP', 1.1, 'papel', 'pared', [
        caja(0.5, 0.7, 0.025, y=1.7, z=0.0125, c='#2a2420'), plano(0.44, 0.64, y=1.7, z=0.027, tex={'tipo': 'cartel_tb', 'dibujo': d1})])
obj('pel_rotulo', 'Rótulo interior de la peluquería', 'decoracion', 'PICKUP', 3, 'madera', 'pared', [
    caja(1.3, 0.34, 0.03, y=2.45, z=0.015, c='#2a2a2e'), plano(1.24, 0.28, y=2.45, z=0.033, tex={'tipo': 'rotulo_tb', 'estilo': 'peluqueria', 'rotulo_local': True})])
obj('pel_cartel_precios', 'Tarifas de la peluquería', 'decoracion', 'PICKUP', 2, 'madera', 'pared', [
    caja(0.7, 0.9, 0.025, y=1.55, z=0.0125, c='#5a3a20'), plano(0.64, 0.84, y=1.55, z=0.0285, tex={'tipo': 'pizarra', 'lineas': ['Corte señora  18', 'Corte caballero  11', 'Lavar y marcar  14', 'Tinte  32', 'Mechas  48', 'Peinado  25']})])
obj('pel_perchero_pared', 'Percheros de pared', 'decoracion', 'FIXED', 3, 'madera', 'pared', [
    caja(0.9, 0.08, 0.02, y=1.7, z=0.01, c=WOOD_D)] + [cil(0.01, 0.01, 0.06, x=x, y=1.7, z=0.05, c=STEEL, r=[90, 0, 0], seg=6) for x in (-0.3, 0, 0.3)] , motivo_fijo=FIJO)
