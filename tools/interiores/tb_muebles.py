# The furniture-and-decoration showroom's objects (family «tiendas_b»): sofas and armchairs, dining sets, sideboards and
# bookcases, beds with their bedding, wardrobes, rugs, lamps, mirrors, pictures, cushions and ornaments, the salesperson's
# desk and the storeroom's packs. Ids start with «mue_». Plain colours, no brands; the pictures are painted, never photographs.
from tb_base import *

ROBLE, ROBLE_D, NOGAL, BLANCO_M, GRIS_M = '#b8925c', '#8a6a40', '#6a4a30', '#efece6', '#8a9096'

# ---- sofas and armchairs: legs, a base, seat cushions (the surface where cushions go), a back, arms
def sofa(id, nombre, c, c2, ancho=2.1, plazas=3, pata=NOGAL, brazos=0.15, masa=None):
    d = 0.9
    nseat = plazas
    sw = (ancho - 2 * brazos - 0.02) / nseat
    P = [caja(0.06, 0.1, 0.06, x=sx * (ancho / 2 - 0.08), y=0.05, z=sz * 0.36, c=pata) for sx in (-1, 1) for sz in (-1, 1)]
    P += [caja(ancho, 0.2, d, y=0.2, z=0.0, c=oscuro(c, 0.9), m='tela'), caja(ancho, 0.5, 0.22, y=0.55, z=-0.34, c=c, m='tela'),
          caja(brazos, 0.32, d, x=-(ancho / 2 - brazos / 2), y=0.44, z=0.0, c=c, m='tela'), caja(brazos, 0.32, d, x=(ancho / 2 - brazos / 2), y=0.44, z=0.0, c=c, m='tela')]
    P += [caja(sw - 0.01, 0.15, 0.62, x=(i - (nseat - 1) / 2) * sw, y=0.375, z=0.1, c=c2 if i % 2 == 0 else c, m='tela') for i in range(nseat)]
    P += [caja(sw - 0.04, 0.38, 0.16, x=(i - (nseat - 1) / 2) * sw, y=0.62, z=-0.2, c=c2 if i % 2 == 0 else c, m='tela', r=[-12, 0, 0]) for i in range(nseat)]
    obj(id, nombre, 'sofa', None, masa or round(18 + ancho * 22), 'tela', 'suelo', P, superficies=[sup(0.45, 0.04)], modificadores=['SEAT'],
        asientos=[{'p': [(i - (nseat - 1) / 2) * sw, 0.45, 0.1], 'h': 0.45, 'anim': 'sofa'} for i in range(nseat)], nota='patas de madera, asientos con cojín y respaldo')
sofa('mue_sofa_3p_beige', 'Sofá de tres plazas beige', '#c9b894', '#d8cab0')
sofa('mue_sofa_3p_gris', 'Sofá de tres plazas gris', '#7a8088', '#8a9098')
sofa('mue_sofa_3p_verde', 'Sofá de tres plazas verde', '#5a7a5a', '#6a8a6a', pata=ROBLE_D)
sofa('mue_sofa_3p_azul', 'Sofá de tres plazas azul petróleo', '#3a5a6a', '#4a6a7a')
sofa('mue_sofa_2p_mostaza', 'Sofá de dos plazas mostaza', '#c8a040', '#d8b050', ancho=1.6, plazas=2)
sofa('mue_sofa_2p_rosa', 'Sofá de dos plazas rosa empolvado', '#c8a0a0', '#d8b0b0', ancho=1.6, plazas=2, pata=ROBLE)
sofa('mue_sofa_2p_crema', 'Sofá de dos plazas crema', '#e0d8c4', '#ece4d2', ancho=1.6, plazas=2)
def sillon(id, nombre, c, c2, tipo='clasico'):
    P = [caja(0.05, 0.14, 0.05, x=sx * 0.34, y=0.07, z=sz * 0.34, c=NOGAL) for sx in (-1, 1) for sz in (-1, 1)]
    P += [caja(0.8, 0.16, 0.8, y=0.22, c=oscuro(c, 0.9), m='tela'), caja(0.7, 0.14, 0.58, y=0.37, z=0.07, c=c2, m='tela'), caja(0.8, 0.55, 0.2, y=0.62, z=-0.3, c=c, m='tela'),
          caja(0.14, 0.3, 0.8, x=-0.33, y=0.44, c=c, m='tela'), caja(0.14, 0.3, 0.8, x=0.33, y=0.44, c=c, m='tela')]
    if tipo == 'orejero': P += [caja(0.1, 0.42, 0.3, x=sx * 0.35, y=0.83, z=-0.25, c=c, m='tela') for sx in (-1, 1)]
    if tipo == 'relax': P += [caja(0.7, 0.1, 0.42, y=0.17, z=0.58, c=c, m='tela', r=[-10, 0, 0])]
    obj(id, nombre, 'sofa', None, 27, 'tela', 'suelo', P, modificadores=['SEAT'], asientos=[{'p': [0, 0.45, 0.07], 'h': 0.45, 'anim': 'sofa'}])
sillon('mue_sillon_orejero', 'Sillón orejero de tela', '#8a5a4a', '#9a6a5a', 'orejero')
sillon('mue_sillon_moderno', 'Sillón moderno gris', '#7a8088', '#8a9098')
sillon('mue_sillon_relax', 'Sillón relax con reposapiés', '#5a4a3a', '#6a5a4a', 'relax')
def puff(id, nombre, c, r=0.26, h=0.42, forma='cil'):
    P = [cil(r, r * 0.95, h, y=h / 2, c=c, m='tela', seg=12), cil(r * 0.92, r * 0.92, 0.03, y=h + 0.0, c=oscuro(c, 0.92), m='tela', seg=12)] if forma == 'cil' else [caja(r * 1.9, h, r * 1.9, y=h / 2, c=c, m='tela'), caja(r * 1.7, 0.03, r * 1.7, y=h + 0.0, c=oscuro(c, 0.92), m='tela')]
    obj(id, nombre, 'silla', 'PICKUP', 4.5, 'tela', 'suelo', P, modificadores=['SEAT'], asientos=[{'p': [0, h + 0.015, 0], 'h': h, 'anim': 'banco'}])
puff('mue_puff_redondo_mostaza', 'Puf redondo mostaza', '#c8a040')
puff('mue_puff_redondo_gris', 'Puf redondo gris', '#8a9098')
puff('mue_puff_cuadrado_verde', 'Puf cuadrado verde', '#5a7a5a', 0.24, 0.4, 'caja')
puff('mue_puff_cuadrado_rosa', 'Puf cuadrado rosa', '#c8a0a0', 0.24, 0.4, 'caja')

# ---- tables and chairs
def mesa(id, nombre, w, d, h, c, tipo='caja', cat='mesa', masa=22, pata=None):
    pata = pata or oscuro(c, 0.8)
    if tipo == 'redonda':
        P = [cil(w / 2, w / 2, 0.04, y=h - 0.02, c=c, m='madera', seg=20), cil(0.07, 0.09, h - 0.04, y=(h - 0.04) / 2, c=pata, m='madera', seg=12), cil(0.3, 0.3, 0.03, y=0.015, c=pata, m='madera', seg=16)]
    else:
        P = [caja(w, 0.04, d, y=h - 0.02, c=c, m='madera')] + [caja(0.06, h - 0.04, 0.06, x=sx * (w / 2 - 0.07), y=(h - 0.04) / 2, z=sz * (d / 2 - 0.07), c=pata, m='madera') for sx in (-1, 1) for sz in (-1, 1)]
        P += [caja(w - 0.2, 0.08, 0.02, y=h - 0.08, z=d / 2 - 0.07, c=pata, m='madera'), caja(w - 0.2, 0.08, 0.02, y=h - 0.08, z=-(d / 2 - 0.07), c=pata, m='madera')]
    obj(id, nombre, cat, None, masa, 'madera', 'suelo', P, superficies=[sup(h, 0.06)])
mesa('mue_mesa_comedor_roble', 'Mesa de comedor de roble (1,6 m)', 1.6, 0.9, 0.76, ROBLE, masa=38)
mesa('mue_mesa_comedor_blanca', 'Mesa de comedor lacada en blanco (1,4 m)', 1.4, 0.8, 0.76, BLANCO_M, masa=32, pata='#8a9096')
mesa('mue_mesa_comedor_redonda', 'Mesa de comedor redonda de nogal', 1.1, 1.1, 0.76, NOGAL, 'redonda', masa=30)
mesa('mue_mesa_centro_cuadrada', 'Mesa de centro cuadrada de roble', 0.9, 0.9, 0.4, ROBLE, masa=14)
mesa('mue_mesa_centro_redonda', 'Mesa de centro redonda de mármol', 0.8, 0.8, 0.4, '#e8e6e0', 'redonda', masa=18, pata='#c8a040')
mesa('mue_mesa_centro_baja', 'Mesa de centro baja con balda', 1.1, 0.6, 0.4, NOGAL, masa=15)
mesa('mue_mesa_auxiliar', 'Mesa auxiliar de metal y madera', 0.45, 0.45, 0.55, ROBLE, masa=8, pata='#2e2e34')
mesa('mue_mesa_escritorio', 'Escritorio de pino con cajonera', 1.3, 0.6, 0.75, '#d8c298', masa=26)
def silla(id, nombre, c, c_asiento, pata=NOGAL, tipo='recta'):
    P = [caja(0.04, 0.45, 0.04, x=sx * 0.19, y=0.225, z=sz * 0.19, c=pata, m='madera') for sx in (-1, 1) for sz in (-1, 1)]
    P += [caja(0.44, 0.04, 0.44, y=0.47, c=c_asiento, m='tela'), caja(0.04, 0.5, 0.04, x=-0.19, y=0.72, z=-0.19, c=pata, m='madera'), caja(0.04, 0.5, 0.04, x=0.19, y=0.72, z=-0.19, c=pata, m='madera')]
    if tipo == 'recta': P += [caja(0.42, 0.14, 0.03, y=0.9, z=-0.19, c=c, m='madera'), caja(0.42, 0.1, 0.03, y=0.74, z=-0.19, c=c, m='madera')]
    elif tipo == 'tapizada': P += [caja(0.42, 0.36, 0.05, y=0.82, z=-0.19, c=c_asiento, m='tela', r=[-6, 0, 0])]
    else: P += [caja(0.44, 0.05, 0.03, y=0.95, z=-0.19, c=c, m='madera'), caja(0.03, 0.2, 0.02, x=-0.1, y=0.82, z=-0.19, c=c, m='madera'), caja(0.03, 0.2, 0.02, x=0.1, y=0.82, z=-0.19, c=c, m='madera'), caja(0.03, 0.2, 0.02, x=0.0, y=0.82, z=-0.19, c=c, m='madera')]
    obj(id, nombre, 'silla', None, 5.5, 'madera', 'suelo', P, modificadores=['SEAT'], asientos=[{'p': [0, 0.49, 0.0], 'h': 0.49, 'anim': 'silla'}])
silla('mue_silla_comedor_roble', 'Silla de comedor de roble', ROBLE, '#c9b894')
silla('mue_silla_comedor_tapizada', 'Silla de comedor tapizada', '#8a6a40', '#7a8a7a', tipo='tapizada')
silla('mue_silla_comedor_blanca', 'Silla de comedor blanca con barrotes', BLANCO_M, '#ece4d2', pata='#8a9096', tipo='barrotes')
silla('mue_silla_comedor_nogal', 'Silla de comedor de nogal', NOGAL, '#8a5a4a')
obj('mue_taburete_alto', 'Taburete alto de madera', 'taburete', 'PICKUP', 3.4, 'madera', 'suelo', [
    cil(0.17, 0.17, 0.04, y=0.62, c=ROBLE, m='madera', seg=12)] + [cil(0.016, 0.016, 0.62, x=sx * 0.12, y=0.31, z=sz * 0.12, c=ROBLE_D, m='madera', seg=6) for sx in (-1, 1) for sz in (-1, 1)] + [cil(0.15, 0.15, 0.02, y=0.2, c=ROBLE_D, m='madera', seg=10)],
    modificadores=['SEAT'], asientos=[{'p': [0, 0.64, 0], 'h': 0.64, 'anim': 'taburete_alto'}])

# ---- storage: sideboards, chests, bookcases, display cabinet, wardrobes, TV unit, bedside tables
def mueble_caja(id, nombre, w, h, d, c, c2, puertas=2, cajones=0, pata=0.1, masa=55, cat='mueble', soporte='suelo', tirador=STEEL):
    P = [caja(w, h - pata, d, y=pata + (h - pata) / 2, z=d / 2, c=c, m='madera'), caja(w + 0.03, 0.03, d + 0.03, y=h - 0.015, z=d / 2, c=c2, m='madera')]
    P += [caja(0.04, pata, 0.04, x=sx * (w / 2 - 0.05), y=pata / 2, z=sz * (d / 2 - 0.05) + d / 2, c=oscuro(c, 0.7), m='madera') for sx in (-1, 1) for sz in (-1, 1)] if pata > 0.03 else []
    zf = d + 0.006
    if puertas:
        pw = w / puertas
        for i in range(puertas):
            P += [caja(pw - 0.03, (h - pata) * (0.6 if cajones else 0.88), 0.012, x=(i - (puertas - 1) / 2) * pw, y=pata + (h - pata) * (0.3 if cajones else 0.45), z=zf, c=oscuro(c, 0.93), m='madera'), caja(0.012, 0.12, 0.02, x=(i - (puertas - 1) / 2) * pw + pw * 0.38 * (-1 if i % 2 else 1), y=pata + (h - pata) * (0.34 if cajones else 0.5), z=zf + 0.014, c=tirador, m='metal')]
    for k in range(cajones):
        P += [caja(w - 0.06, (h - pata) / cajones - 0.04, 0.012, y=pata + (h - pata) * (k + 0.5) / cajones, z=zf, c=oscuro(c, 0.93), m='madera'), caja(0.14, 0.014, 0.02, y=pata + (h - pata) * (k + 0.5) / cajones + 0.03, z=zf + 0.014, c=tirador, m='metal')]
    obj(id, nombre, cat, None, masa, 'madera', soporte, P, superficies=[sup(h, 0.05)] if h < 1.3 else [])
mueble_caja('mue_aparador_roble', 'Aparador de roble (1,6 m)', 1.6, 0.85, 0.45, ROBLE, '#c9a870', puertas=3, masa=78)
mueble_caja('mue_aparador_blanco', 'Aparador blanco lacado (1,4 m)', 1.4, 0.8, 0.42, BLANCO_M, '#e0ddd6', puertas=2, masa=60, tirador='#c8a040')
mueble_caja('mue_aparador_nogal', 'Aparador de nogal con cajones (1,2 m)', 1.2, 0.8, 0.42, NOGAL, '#7a5a40', puertas=2, cajones=0, masa=55)
mueble_caja('mue_comoda_cajones', 'Cómoda de cuatro cajones', 0.9, 0.9, 0.45, '#d8c298', '#c8b288', puertas=0, cajones=4, masa=50)
mueble_caja('mue_comoda_blanca', 'Cómoda blanca de seis cajones', 1.2, 0.85, 0.45, BLANCO_M, '#e0ddd6', puertas=0, cajones=3, masa=62, tirador='#c8a040')
mueble_caja('mue_mesilla_roble', 'Mesilla de noche de roble', 0.45, 0.55, 0.4, ROBLE, '#c9a870', puertas=0, cajones=2, pata=0.12, masa=12, cat='mueble')
mueble_caja('mue_mesilla_blanca', 'Mesilla de noche blanca', 0.45, 0.55, 0.4, BLANCO_M, '#e0ddd6', puertas=0, cajones=2, pata=0.12, masa=11, cat='mueble', tirador='#c8a040')
mueble_caja('mue_mesilla_nogal', 'Mesilla de noche de nogal', 0.5, 0.55, 0.4, NOGAL, '#7a5a40', puertas=1, cajones=0, pata=0.12, masa=12, cat='mueble')
mueble_caja('mue_zapatero', 'Zapatero de dos puertas', 0.8, 1.1, 0.3, '#d8c298', '#c8b288', puertas=2, masa=24, cat='mueble')
mueble_caja('mue_armario_2p', 'Armario ropero de dos puertas', 1.0, 2.05, 0.55, '#d8c8a8', '#c8b898', puertas=2, pata=0.06, masa=96, cat='tb_mueble_grande')
mueble_caja('mue_armario_3p', 'Armario ropero de tres puertas', 1.5, 2.1, 0.58, BLANCO_M, '#e0ddd6', puertas=3, pata=0.06, masa=140, cat='tb_mueble_grande', tirador='#8a9096')
mueble_caja('mue_armario_4p_nogal', 'Armario de cuatro puertas de nogal', 1.9, 2.15, 0.6, NOGAL, '#7a5a40', puertas=4, pata=0.06, masa=180, cat='tb_mueble_grande')
estantes('mue_libreria_alta', 'Librería alta de roble (0,9 m)', 0.9, 0.35, [0.38, 0.76, 1.14, 1.52, 1.9], 2.0, c=ROBLE, cp='#c9a870', masa=48, nota='cinco baldas para libros y adornos')
estantes('mue_libreria_blanca', 'Librería blanca de cuatro baldas (0,8 m)', 0.8, 0.32, [0.4, 0.8, 1.2, 1.6], 1.7, c=BLANCO_M, cp='#f2efe8', masa=34)
def cubos(id, nombre, c, n=3):
    P = [caja(0.02, n * 0.38, 0.34, x=(i - n / 2) * 0.38, y=n * 0.19, z=0.17, c=c, m='madera') for i in range(n + 1)] + [caja(n * 0.38, 0.02, 0.34, y=(k) * 0.38 + 0.01, z=0.17, c=c, m='madera') for k in range(n + 1)] + [caja(n * 0.38, n * 0.38, 0.01, y=n * 0.19, z=0.005, c=oscuro(c, 0.9), m='madera')]
    obj(id, nombre, 'estanteria', None, 36, 'madera', 'suelo', P, superficies=[sup(0.02 + k * 0.38, 0.04, fondo=0.32) for k in range(0, n + 1)])
cubos('mue_estanteria_cubos', 'Estantería de cubos de madera (3 × 3)', '#d8c298')
cubos('mue_estanteria_cubos_blanca', 'Estantería de cubos blanca (2 × 2)', BLANCO_M, 2)
obj('mue_vitrina_salon', 'Vitrina de salón con puertas de cristal', 'tb_mueble_grande', None, 70, 'madera', 'suelo', [
    caja(0.9, 1.85, 0.38, y=0.925, z=0.19, c=NOGAL, m='madera'), caja(0.84, 1.1, 0.01, y=1.25, z=0.386, c=GLASS, m='cristal'), caja(0.84, 0.55, 0.012, y=0.37, z=0.386, c='#5a3a28', m='madera'), caja(0.82, 0.01, 0.34, y=1.0, z=0.19, c=GLASS, m='cristal'), caja(0.82, 0.01, 0.34, y=1.4, z=0.19, c=GLASS, m='cristal'),
    caja(0.012, 0.2, 0.02, x=0.38, y=1.0, z=0.4, c='#c8a040', m='metal')] + [cil(0.07, 0.05, 0.04, x=-0.2 + i * 0.2, y=1.43, z=0.18, c=['#e8e4d8', '#6a8aa8', '#e8e4d8'][i], m='ceramica', seg=10) for i in range(3)] + [cil(0.05, 0.05, 0.12, x=-0.2 + i * 0.2, y=1.07, z=0.18, c=['#c0302a', '#e8c040', '#3a8a5a'][i], m='cristal', seg=8) for i in range(3)], nota='con platos y copas dentro')
obj('mue_mueble_tv', 'Mueble de televisión con televisor', 'mueble', None, 46, 'madera', 'suelo', [
    caja(1.8, 0.5, 0.45, y=0.3, z=0.225, c=NOGAL, m='madera')] + [caja(0.04, 0.05, 0.04, x=sx * 0.85, y=0.025, z=sz * 0.18 + 0.225, c='#2e2e34', m='metal') for sx in (-1, 1) for sz in (-1, 1)] + [
    caja(0.55, 0.4, 0.012, x=-0.45, y=0.3, z=0.452, c='#5a3a28', m='madera'), caja(0.55, 0.4, 0.012, x=0.45, y=0.3, z=0.452, c='#5a3a28', m='madera'), caja(0.7, 0.44, 0.03, y=0.82, z=0.2, c='#2a2e38', m='plastico'), caja(0.66, 0.4, 0.004, y=0.82, z=0.217, c='#4a6a8a', m='plastico', luz=True),
    caja(0.15, 0.04, 0.12, y=0.57, z=0.2, c='#2a2e38', m='plastico')], superficies=[sup(0.55, 0.05)], nota='con una tele apagada en su peana')
obj('mue_consola_entrada', 'Consola de entrada con espejo', 'mueble', None, 28, 'madera', 'suelo', [
    caja(1.0, 0.04, 0.3, y=0.78, z=0.15, c=ROBLE)] + [caja(0.04, 0.76, 0.04, x=sx * 0.45, y=0.38, z=0.04 + sz * 0.13 + 0.13, c=ROBLE_D) for sx in (-1, 1) for sz in (-1, 1)] + [caja(0.9, 0.9, 0.03, y=1.35, z=0.015, c='#8a6a40'), caja(0.82, 0.82, 0.006, y=1.35, z=0.033, c=MIRROR, m='metal')],
    superficies=[sup(0.8, 0.04)], nota='consola con un espejo de pared sobre ella')
# ---- beds with their bedding
def cama(id, nombre, ancho, c_cab, c_ropa, c_almo, tipo='madera'):
    L = 1.95
    P = [caja(ancho + 0.1, 0.22, L + 0.08, y=0.19, z=L / 2, c=c_cab, m='madera' if tipo != 'tapizada' else 'tela')]
    P += [caja(0.06, 0.08, 0.06, x=sx * (ancho / 2 + 0.01), y=0.04, z=sz * (L / 2 - 0.05) + L / 2, c=oscuro(c_cab, 0.7), m='madera') for sx in (-1, 1) for sz in (-1, 1)]
    P += [caja(ancho + 0.1, 1.1 if tipo == 'tapizada' else 1.0, 0.09, y=0.55 if tipo != 'tapizada' else 0.6, z=0.045, c=c_cab, m='madera' if tipo != 'tapizada' else 'tela')]
    if tipo == 'tapizada': P += [caja(ancho * 0.3, 0.9, 0.012, x=(i - 1) * ancho * 0.32, y=0.6, z=0.096, c=oscuro(c_cab, 0.92), m='tela') for i in range(3)]
    P += [caja(ancho + 0.1, 0.36, 0.06, y=0.28, z=L + 0.05, c=c_cab, m='madera'), caja(ancho, 0.2, L - 0.1, y=0.4, z=L / 2 + 0.02, c='#f2efe8', m='tela'), caja(ancho + 0.02, 0.07, L * 0.62, y=0.535, z=L * 0.7, c=c_ropa, m='tela'),
          caja(ancho + 0.04, 0.03, 0.16, y=0.57, z=L * 0.42, c=oscuro(c_ropa, 0.85), m='tela')]
    npil = 2 if ancho > 1.2 else 1
    P += [caja(0.55 if ancho > 1.2 else 0.5, 0.12, 0.32, x=(i - (npil - 1) / 2) * (ancho / npil), y=0.56, z=0.28, c=c_almo, m='tela', r=[-10, 0, 0]) for i in range(npil)]
    obj(id, nombre, 'tb_colchon_cama', None, 62 if ancho > 1.2 else 38, 'madera', 'suelo', P, nota='cabecero contra la pared, colchón, colcha y almohadas')
cama('mue_cama_150_madera', 'Cama de matrimonio de madera (150)', 1.5, ROBLE, '#6a8aa8', '#f2efe8')
cama('mue_cama_150_nogal', 'Cama de matrimonio de nogal (150)', 1.5, NOGAL, '#c0a070', '#efe8d8')
cama('mue_cama_150_tapizada', 'Cama tapizada con cabecero capitoné (150)', 1.5, '#8a8f98', '#d8d0c0', '#e8e2d6', 'tapizada')
cama('mue_cama_135_blanca', 'Cama de 135 lacada en blanco', 1.35, BLANCO_M, '#c8a0a0', '#f2efe8')
cama('mue_cama_90_juvenil', 'Cama individual juvenil (90)', 0.9, '#d8c298', '#3a6a8a', '#f2efe8')
obj('mue_colchon_muestra', 'Colchón de muestra sobre una base', 'tb_colchon_cama', None, 24, 'tela', 'suelo', [
    caja(1.5, 0.2, 1.95, y=0.1, z=0.975, c='#8a6a40', m='madera'), caja(1.46, 0.22, 1.9, y=0.31, z=0.975, c='#efece4', m='tela'), caja(1.48, 0.012, 1.92, y=0.426, z=0.975, c='#c8d4e0', m='tela'), caja(0.4, 0.1, 0.004, y=0.35, z=1.93, c='#2c5aa0', m='papel')], nota='con su etiqueta de firmeza')
# ---- rugs: a 4 mm slab just above the floor (the floor plane lies at 5 mm; the layout lets what stands on it overlap it)
def alfombra(id, nombre, w, d, c, c2, tipo='rect'):
    # (all of it inside 4.8 mm, from 9.7 mm up: the floor plane lies at 5 mm, and what stands on a rug may overlap it by less than the layout's 5 mm)
    if tipo == 'redonda': P = [cil(w / 2, w / 2, 0.004, y=0.0117, c=c, m='tela', seg=24), cil(w / 2 * 0.8, w / 2 * 0.8, 0.0045, y=0.012, c=c2, m='tela', seg=24), cil(w / 2 * 0.45, w / 2 * 0.45, 0.0046, y=0.0122, c=c, m='tela', seg=24)]
    else:
        P = [caja(w, 0.004, d, y=0.0117, c=c, m='tela'), caja(w * 0.9, 0.0045, d * 0.88, y=0.012, c=c2, m='tela')]
        P += [caja(w * 0.82, 0.0046, 0.04, y=0.0122, z=(k - 2) * d * 0.17, c=c, m='tela') for k in range(5)]
    obj(id, nombre, 'textil', 'PICKUP', 4.8, 'tela', 'suelo', P)
alfombra('mue_alfombra_gris', 'Alfombra rectangular gris (2 × 1,4 m)', 2.0, 1.4, '#8a9098', '#a8aeb4')
alfombra('mue_alfombra_roja', 'Alfombra rectangular granate (2,4 × 1,7 m)', 2.4, 1.7, '#8a3a3a', '#b86a5a')
alfombra('mue_alfombra_beige', 'Alfombra rectangular beige (2,4 × 1,7 m)', 2.4, 1.7, '#cdbf9e', '#e0d4b8')
alfombra('mue_alfombra_azul', 'Alfombra rectangular azul (2 × 1,4 m)', 2.0, 1.4, '#3a5a7a', '#6a8aa8')
alfombra('mue_alfombra_redonda', 'Alfombra redonda de yute (1,6 m)', 1.6, 1.6, '#c8b078', '#b09a62', 'redonda')
alfombra('mue_alfombra_pasillo', 'Alfombra de pasillo verde (0,8 × 2,2 m)', 0.8, 2.2, '#5a7a5a', '#8aa88a')
# ---- lamps, mirrors, pictures, clocks (painted)
def lampara_pie(id, nombre, c, pantalla):
    obj(id, nombre, 'lampara', 'PICKUP', 3.8, 'metal', 'suelo', [
        cil(0.16, 0.16, 0.025, y=0.0125, c=c, m='metal', seg=16), cil(0.012, 0.012, 1.4, y=0.7, c=c, m='metal', seg=8), cil(0.2, 0.15, 0.3, y=1.55, c=pantalla, m='tela', seg=16), cil(0.1, 0.1, 0.01, y=1.42, c='#fff1d0', m='plastico', seg=12, luz=True)])
lampara_pie('mue_lampara_pie_laton', 'Lámpara de pie de latón con pantalla crema', '#c8a040', '#f2e6c8')
lampara_pie('mue_lampara_pie_negra', 'Lámpara de pie negra con pantalla blanca', '#2e2e34', '#efece4')
lampara_pie('mue_lampara_pie_madera', 'Lámpara de pie de madera', '#8a6a40', '#e8dcc0')
def lampara_mesa(id, nombre, c, pantalla):
    obj(id, nombre, 'lampara', 'PICKUP', 1.8, 'ceramica', 'superficie', [
        cil(0.08, 0.08, 0.025, y=0.0125, c=c, m='ceramica', seg=12), cil(0.045, 0.06, 0.2, y=0.125, c=c, m='ceramica', seg=12), cil(0.13, 0.1, 0.18, y=0.31, c=pantalla, m='tela', seg=16), esf(0.03, 0, 0.27, 0, c='#fff1d0', m='plastico', luz=True)])
lampara_mesa('mue_lampara_mesa_azul', 'Lamparita de mesilla de cerámica azul', '#5a7a9a', '#f2e6c8')
lampara_mesa('mue_lampara_mesa_blanca', 'Lamparita de mesilla blanca', '#efece4', '#e8d8b0')
lampara_mesa('mue_lampara_mesa_verde', 'Lamparita de mesilla verde', '#5a8a6a', '#f2efe4')
obj('mue_lampara_techo_cristal', 'Lámpara de techo de cristal y latón', 'lampara', 'FIXED', 6, 'metal', 'techo', [
    cil(0.006, 0.006, 0.55, y=-0.275, c='#c8a040', m='metal', seg=6), cil(0.04, 0.04, 0.03, y=-0.015, c='#c8a040', m='metal', seg=8)] + [cil(0.012, 0.012, 0.28, x=math.cos(a) * 0.3, y=-0.66, z=math.sin(a) * 0.3, c='#c8a040', m='metal', seg=6) for a in (0, 1.26, 2.51, 3.77, 5.03)] + [
    esf(0.07, math.cos(a) * 0.3, -0.86, math.sin(a) * 0.3, c='#fff1d0', m='cristal', luz=True) for a in (0, 1.26, 2.51, 3.77, 5.03)] + [cil(0.3, 0.3, 0.012, y=-0.55, c='#c8a040', m='metal', seg=16)], motivo_fijo=FIJO, nota='cinco brazos con tulipas')
obj('mue_lampara_techo_pantalla', 'Lámpara de techo de pantalla de tela', 'lampara', 'FIXED', 3.5, 'tela', 'techo', [
    cil(0.006, 0.006, 0.5, y=-0.25, c='#2e2e34', m='metal', seg=6), cil(0.25, 0.25, 0.2, y=-0.6, c='#efe6d0', m='tela', seg=16), cil(0.18, 0.18, 0.01, y=-0.7, c='#fff1d0', m='plastico', seg=12, luz=True)], motivo_fijo=FIJO)
def espejo(id, nombre, w, h, y, marco, redondo=False, vende=None):
    if redondo:
        P = [cil(w / 2, w / 2, 0.04, y=y, z=0.02, c=marco, m='madera', r=[90, 0, 0], seg=24), cil(w / 2 - 0.04, w / 2 - 0.04, 0.006, y=y, z=0.043, c=MIRROR, m='metal', r=[90, 0, 0], seg=24)]
    else:
        P = [caja(w, h, 0.04, y=y, z=0.02, c=marco, m='madera'), caja(w - 0.08, h - 0.08, 0.006, y=y, z=0.043, c=MIRROR, m='metal')]
    obj(id, nombre, 'espejo', 'FIXED', 8, 'cristal', 'pared', P, motivo_fijo=FIJO)
espejo('mue_espejo_redondo', 'Espejo redondo con marco de roble (0,8 m)', 0.8, 0.8, 1.6, ROBLE, True)
espejo('mue_espejo_alto', 'Espejo alto de cuerpo entero (0,6 × 1,6 m)', 0.6, 1.6, 1.0, '#c8a040')
espejo('mue_espejo_marco_nogal', 'Espejo rectangular con marco de nogal', 0.8, 1.0, 1.55, NOGAL)
espejo('mue_espejo_dorado', 'Espejo de pared con marco dorado', 0.7, 0.9, 1.6, '#c8a850')
for k, (n_, est, n) in {'a': ('Cuadro abstracto (ocres)', 'abstracto', 1), 'b': ('Cuadro abstracto (verdes)', 'abstracto', 2), 'c': ('Cuadro de una marina', 'marina', 1), 'd': ('Cuadro de un bodegón', 'bodegon', 1), 'e': ('Cuadro de flores', 'flores', 1)}.items():
    obj('mue_cuadro_' + k, n_, 'cuadro', 'PICKUP', 2.0, 'madera', 'pared', [
        caja(0.7, 0.54, 0.035, y=1.7, z=0.0175, c='#2a2420'), plano(0.62, 0.46, y=1.7, z=0.037, tex={'tipo': 'cuadro_tb', 'estilo': est, 'n': n})])
obj('mue_reloj_pared_grande', 'Reloj de pared grande de madera', 'reloj', 'PICKUP', 1.4, 'madera', 'pared', [
    cil(0.28, 0.28, 0.05, y=1.9, z=0.025, c=ROBLE_D, m='madera', r=[90, 0, 0], seg=24), cil(0.25, 0.25, 0.01, y=1.9, z=0.05, c='#f6f2e6', m='papel', r=[90, 0, 0], seg=24), caja(0.012, 0.2, 0.008, y=1.97, z=0.058, c='#2e2e34', m='metal'), caja(0.12, 0.012, 0.008, x=0.05, y=1.9, z=0.06, c='#2e2e34', m='metal')])
# ---- cushions, throws and ornaments (PICKUP, on sofas, tables, shelves)
def cojin(id, nombre, c1, c2):
    obj(id, nombre, 'textil', 'PICKUP', 1.0, 'tela', 'superficie', [
        caja(0.34, 0.1, 0.34, y=0.05, z=0.0, c=c1, m='tela'), caja(0.28, 0.1, 0.28, y=0.15, z=0.0, c=c2, m='tela', r=[0, 22, 0])])
cojin('mue_cojines_mostaza', 'Cojines de mostaza y gris', '#c8a040', '#8a9098')
cojin('mue_cojines_verde', 'Cojines verde y crema', '#5a7a5a', '#e0d8c4')
cojin('mue_cojines_rojo', 'Cojines granate y beige', '#8a3a3a', '#cdbf9e')
cojin('mue_cojines_azul', 'Cojines azules', '#3a5a7a', '#8aa8c0')
obj('mue_manta_doblada', 'Manta de lana doblada', 'textil', 'PICKUP', 1.2, 'tela', 'superficie', [
    caja(0.5, 0.05, 0.36, y=0.025, c='#b09068', m='tela'), caja(0.5, 0.05, 0.36, y=0.075, c='#8a3a3a', m='tela'), caja(0.5, 0.02, 0.05, y=0.1, z=0.1, c='#e0d8c4', m='tela')])
def jarron(id, nombre, c, h=0.3, r=0.07, flores=None):
    P = [cil(r * 0.7, r, h, y=h / 2, c=c, m='ceramica', seg=10), cil(r * 0.5, r * 0.6, 0.04, y=h + 0.0, c=c, m='ceramica', seg=10)]
    if flores: P += [cil(0.006, 0.006, 0.3, x=(i - 1) * 0.03, y=h + 0.15, z=(i % 2 - 0.5) * 0.03, c='#4a7a2a', m='comida', seg=5) for i in range(3)] + [esf(0.03, (i - 1) * 0.04, h + 0.32, (i % 2 - 0.5) * 0.04, c=flores, m='comida') for i in range(3)]
    obj(id, nombre, 'decoracion', 'PICKUP', 1.2, 'ceramica', 'superficie', P)
jarron('mue_jarron_azul', 'Jarrón de cerámica azul', '#4a6a8a', 0.3)
jarron('mue_jarron_blanco', 'Jarrón blanco con flores', '#efece4', 0.26, 0.07, '#d8a0a8')
jarron('mue_jarron_verde', 'Jarrón verde alto', '#5a8a6a', 0.32, 0.055)
obj('mue_libros_filas', 'Libros en fila con un sujetalibros', 'decoracion', 'PICKUP', 3.2, 'papel', 'superficie', [
    caja(0.03, 0.2 + (i % 3) * 0.03, 0.2, x=-0.18 + i * 0.035, y=0.1 + (i % 3) * 0.015, z=0.0, c=['#8a3a3a', '#3a5a7a', '#c9b894', '#5a7a5a', '#6a4a30', '#a07a3a', '#2e2e34', '#8a9098'][i], m='papel') for i in range(8)] + [caja(0.02, 0.18, 0.12, x=0.13, y=0.09, c='#2e2e34', m='metal')])
obj('mue_marcos_foto', 'Marcos de fotos sobre la mesa', 'cuadro', 'PICKUP', 0.6, 'madera', 'superficie', [
    caja(0.15, 0.2, 0.02, x=-0.1, y=0.1, z=0.0, c=ROBLE_D, m='madera', r=[-8, 0, 0]), caja(0.12, 0.17, 0.004, x=-0.1, y=0.1, z=0.012, c='#9ab8c8', m='papel', r=[-8, 0, 0]), caja(0.18, 0.14, 0.02, x=0.1, y=0.07, z=0.02, c='#c8a040', m='metal', r=[-8, 0, 0]), caja(0.15, 0.11, 0.004, x=0.1, y=0.07, z=0.032, c='#c8b898', m='papel', r=[-8, 0, 0])])
obj('mue_cuenco_decorativo', 'Cuenco decorativo con piñas', 'decoracion', 'PICKUP', 0.9, 'ceramica', 'superficie', [
    cil(0.14, 0.08, 0.08, y=0.04, c='#8a6a40', m='ceramica', seg=12)] + [esf(0.035, (i % 3 - 1) * 0.05, 0.1, (i // 3 - 0.5) * 0.06, c='#6a4a30', m='comida') for i in range(5)])
# ---- the salesperson's desk and the storeroom's packs
obj('mue_mostrador_atencion', 'Mesa de atención del vendedor (1,5 m)', 'mostrador', 'FIXED', 120, 'madera', 'suelo', [
    caja(1.5, 0.72, 0.66, y=0.36, z=-0.02, c='#d8c8a8'), caja(1.52, 0.04, 0.7, y=0.74, z=0.0, c=NOGAL), caja(1.44, 0.5, 0.012, y=0.38, z=0.31, c='#8a6a40'), caja(1.5, 0.07, 0.012, y=0.04, z=0.31, c=DARK)],
    motivo_fijo='estructural', superficies=[sup(0.76, 0.05)], nota='una mesa de nogal para atender al cliente y enseñar muestras')
obj('mue_catalogo_muebles', 'Catálogo de muebles y muestrario de telas', 'decoracion', 'PICKUP', 1.6, 'papel', 'superficie', [
    caja(0.34, 0.05, 0.26, y=0.025, c='#6a4a30', m='papel'), caja(0.3, 0.02, 0.22, y=0.06, c='#f2efe6', m='papel')] + [caja(0.04, 0.02, 0.1, x=-0.08 + i * 0.05, y=0.08, z=0.0, c=['#c0302a', '#2c5aa0', '#d8a020', '#3a8a5a'][i], m='tela') for i in range(4)])
obj('mue_rotulo', 'Rótulo interior de la tienda de muebles', 'decoracion', 'PICKUP', 3, 'madera', 'pared', [
    caja(1.3, 0.34, 0.03, y=2.6, z=0.015, c='#2a1c10'), plano(1.24, 0.28, y=2.6, z=0.033, tex={'tipo': 'rotulo_tb', 'estilo': 'muebles', 'rotulo_local': True})])
for k, (n_, d1) in {'sofa': ('Cartel de sofás a medida', 'sofa'), 'cama': ('Cartel de descanso', 'cama')}.items():
    obj('mue_cartel_' + k, n_, 'cuadro', 'PICKUP', 1.2, 'papel', 'pared', [
        caja(0.5, 0.7, 0.025, y=1.7, z=0.0125, c='#2a2420'), plano(0.44, 0.64, y=1.7, z=0.027, tex={'tipo': 'cartel_tb', 'dibujo': d1})])
obj('mue_caja_mueble_plana', 'Caja plana de mueble sin montar', 'caja', 'CARRY', 24, 'papel', 'suelo', [
    caja(1.4, 0.2, 0.45, y=0.1, c='#c9a46e', m='papel'), caja(0.8, 0.002, 0.2, y=0.201, z=0.0, c='#f2efe6', m='papel'), caja(1.42, 0.015, 0.03, y=0.1, z=0.0, c='#8a6a40', m='papel')], nota='el mueble en piezas, con su etiqueta')
obj('mue_pila_cajas_plana', 'Pila de cajas planas', 'caja', 'PUSH', 25, 'papel', 'suelo', [
    caja(1.2, 0.18, 0.4, y=0.09 + k * 0.185, c=['#c9a46e', '#b8925c'][k % 2], m='papel') for k in range(5)] + [caja(0.6, 0.12, 0.004, y=0.5, z=0.202, c='#f2efe6', m='papel')], motivo_clase='una pila de cajas planas: el conjunto pesa más que una caja')
obj('mue_colchon_plastico', 'Colchón envuelto en plástico, apoyado', 'tb_colchon_cama', 'PUSH', 30, 'tela', 'suelo', [
    caja(1.3, 1.9, 0.22, y=0.95, z=0.0, c='#e8ecef', m='cristal'), caja(0.4, 0.6, 0.005, y=1.1, z=0.113, c='#2c5aa0', m='papel')], nota='un colchón en su funda de plástico, de canto')
obj('mue_carro_muebles', 'Carro plataforma para muebles', 'tb_producto_hogar', 'CARRY', 18, 'metal', 'suelo', [
    caja(0.7, 0.04, 1.2, y=0.14, c='#5a626a', m='metal'), caja(0.7, 0.12, 0.04, y=0.2, z=-0.58, c='#5a626a', m='metal')] + [cil(0.06, 0.06, 0.04, x=sx * 0.3, y=0.06, z=sz * 0.5, c=DARK, m='goma', r=[0, 0, 90], seg=8) for sx in (-1, 1) for sz in (-1, 1)] + [caja(0.04, 1.0, 0.04, x=0.0, y=0.66, z=-0.58, c='#5a626a', m='metal'), caja(0.5, 0.04, 0.04, y=1.16, z=-0.58, c='#5a626a', m='metal')])
