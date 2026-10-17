# The objects of the «servicios» family (technical backlog, I-02 and X-01/X-02): a small-town bank branch, an office
# (insurance, gestoría…), a gym and a «casa de comidas». Each one a few primitives — boxes, cylinders, spheres, cones and
# textured planes, in metres —, its class of interaction, its mass, its material and what it stands on. The script is
# the model: it writes data/objetos/servicios.json. What the family shares with hostelería (chairs, bottles, sanitaryware…)
# is not repeated: the kits name those objects by their id.
# Frame of an object: x across, y up from its foot, z out of its front (+z faces whoever uses it; its back at -z). A
# machine of the gym has its console at -z and is stepped onto from +z, so standing against a wall it faces the wall.
# Hung from the ceiling (soporte «techo») the parts run down from y = 0; on a wall (soporte «pared») the back is at z = 0.
#   python3 tools/interiores/catalogo_servicios.py
import json, math, os
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

CATEGORIAS = {  # (mass ranges, kg, of the categories this family brings)
    'equipo_gimnasio': [0.1, 200], 'terminal_cliente': [5, 150], 'seguridad_local': [0.1, 20], 'menaje_cocina': [0.1, 30],
}

def obj(id, nombre, categoria, masa, material, soporte, partes, fijo=None, clase=None, **k):
    # the class follows the mass (PICKUP < 5 kg, CARRY < 25, PUSH < 80, PUSH_HEAVY < 400, FIXED beyond), unless `fijo` (the
    # reason it is bolted down) makes it FIXED, or `clase` says otherwise (and then the note says why: motivo_clase)
    cl = clase or ('FIXED' if fijo else 'PICKUP' if masa < 5 else 'CARRY' if masa < 25 else 'PUSH' if masa < 80 else 'PUSH_HEAVY' if masa < 400 else 'FIXED')
    if cl == 'FIXED' and not fijo: fijo = 'estructural'
    o = {'id': id, 'nombre': nombre, 'categoria': categoria, 'clase': cl, 'masa': masa, 'material': material, 'soporte': soporte, 'partes': partes, **k}
    if fijo and cl == 'FIXED': o['motivo_fijo'] = fijo
    OUT.append(o)

def lado(partes, dz=0.0, dx=0.0):
    # the same parts turned half a turn about y (what stands behind a desk looks at it) and moved dx, dz
    out = []
    for p in partes:
        q = dict(p, p=[-p['p'][0] + dx, p['p'][1], -p['p'][2] + dz])
        r = p.get('r')
        if r: q['r'] = [-r[0], r[1], -r[2]]
        out.append(q)
    return out

STEEL, GREY, GREYD, DARK, BLACK, WHITE = '#c3c7ca', '#8e949a', '#5b6066', '#2b2b2e', '#1d1f22', '#f1efe9'
BEECH, WOOD, WOOD_D, GLASS, BLUE = '#d6c19a', '#8a5a36', '#5e3b22', '#bcd6dc', '#2f4a6b'
TEAL, GOLD, RED, GREEN = '#0f5c6e', '#d9a441', '#b5342c', '#3d7a4a'
STONE = '#dcd6c8'

# ================================================================ furniture of an office (shared by the bank and the office)
SILLA_G = [  # swivel chair: five-star base on casters, gas lift, upholstered seat and back, arms (its front at +z)
    *[caja(0.32, 0.03, 0.05, x=0.16 * math.sin(math.radians(72 * k + 18)), y=0.065, z=0.16 * math.cos(math.radians(72 * k + 18)), c=DARK, m='plastico', r=[0, 72 * k + 18 - 90, 0]) for k in range(5)],
    *[cil(0.022, 0.022, 0.05, x=0.31 * math.sin(math.radians(72 * k + 18)), y=0.025, z=0.31 * math.cos(math.radians(72 * k + 18)), c=BLACK, m='goma', seg=8) for k in range(5)],
    cil(0.03, 0.03, 0.33, y=0.255, c=GREY, seg=8),
    caja(0.48, 0.07, 0.46, y=0.47, c=BLUE, m='tela'), caja(0.44, 0.46, 0.06, y=0.82, z=-0.21, c=BLUE, m='tela', r=[-8, 0, 0]),
    caja(0.04, 0.03, 0.26, x=-0.26, y=0.68, z=0.0, c=DARK, m='plastico'), caja(0.04, 0.03, 0.26, x=0.26, y=0.68, z=0.0, c=DARK, m='plastico'),
    caja(0.03, 0.18, 0.03, x=-0.26, y=0.59, z=0.06, c=DARK, m='plastico'), caja(0.03, 0.18, 0.03, x=0.26, y=0.59, z=0.06, c=DARK, m='plastico')]
obj('silla_oficina', 'Silla giratoria de oficina', 'silla', 8.5, 'tela', 'suelo', SILLA_G, modificadores=['SEAT'], asientos=[{'p': [0, 0.505, 0.0], 'h': 0.505, 'anim': 'silla'}])
obj('silla_visita', 'Silla de visita', 'silla', 5.5, 'metal', 'suelo', [
    *[cil(0.012, 0.012, 0.45, x=sx * 0.19, y=0.225, z=sz * 0.18, c=STEEL, seg=8) for sx in (-1, 1) for sz in (-1, 1)],
    caja(0.44, 0.05, 0.42, y=0.47, c=BLUE, m='tela'), caja(0.42, 0.34, 0.04, y=0.78, z=-0.2, c=BLUE, m='tela', r=[-6, 0, 0]),
    cil(0.012, 0.012, 0.34, x=-0.2, y=0.67, z=-0.19, c=STEEL, seg=8), cil(0.012, 0.012, 0.34, x=0.2, y=0.67, z=-0.19, c=STEEL, seg=8),
    cil(0.01, 0.01, 0.38, x=-0.21, y=0.65, z=0.0, c=STEEL, seg=8, r=[90, 0, 0]), cil(0.01, 0.01, 0.38, x=0.21, y=0.65, z=0.0, c=STEEL, seg=8, r=[90, 0, 0])],
    modificadores=['SEAT'], asientos=[{'p': [0, 0.495, 0.02], 'h': 0.495, 'anim': 'silla'}])
obj('silla_espera_fila', 'Fila de tres sillas de espera', 'banco', 19, 'metal', 'suelo', [
    caja(1.5, 0.04, 0.05, y=0.29, z=-0.05, c=GREYD, m='metal'),
    *[caja(0.05, 0.43, 0.05, x=sx * 0.68, y=0.215, z=sz * 0.2, c=GREYD, m='metal') for sx in (-1, 1) for sz in (-1, 1)],
    *[caja(0.46, 0.05, 0.44, x=k * 0.5, y=0.45, c='#3a5a78', m='plastico') for k in (-1, 0, 1)],
    *[caja(0.46, 0.3, 0.04, x=k * 0.5, y=0.72, z=-0.2, c='#3a5a78', m='plastico', r=[-6, 0, 0]) for k in (-1, 0, 1)]],
    modificadores=['SEAT'], asientos=[{'p': [k * 0.5, 0.475, 0.02], 'h': 0.475, 'anim': 'banco'} for k in (-1, 0, 1)])
obj('sillon_espera', 'Sillón de sala de espera', 'sofa', 27, 'tela', 'suelo', [
    caja(0.72, 0.3, 0.7, y=0.15, c='#7a4a3a', m='tela'), caja(0.5, 0.12, 0.5, y=0.36, z=0.04, c='#8a5a48', m='tela'),
    caja(0.72, 0.42, 0.16, y=0.6, z=-0.27, c='#7a4a3a', m='tela', r=[-8, 0, 0]),
    caja(0.12, 0.2, 0.62, x=-0.3, y=0.4, z=0.02, c='#6a3e30', m='tela'), caja(0.12, 0.2, 0.62, x=0.3, y=0.4, z=0.02, c='#6a3e30', m='tela')],
    modificadores=['SEAT'], asientos=[{'p': [0, 0.42, 0.04], 'h': 0.42, 'anim': 'sofa'}])

DESK_BODY = lambda w, c: [  # a plain desk of w × 0.7 (user at +z, modesty panel at -z, drawers on the right)
    caja(w, 0.03, 0.7, y=0.735, c=c), caja(0.03, 0.72, 0.66, x=-(w / 2 - 0.035), y=0.36, c=GREY, m='metal'),
    caja(0.42, 0.72, 0.62, x=w / 2 - 0.21, y=0.36, c='#c9ccce'),
    *[caja(0.36, 0.17, 0.012, x=w / 2 - 0.21, y=yy, z=0.316, c=GREYD, m='plastico') for yy in (0.6, 0.4, 0.2)],
    *[caja(0.1, 0.015, 0.015, x=w / 2 - 0.21, y=yy + 0.04, z=0.328, c=STEEL, m='metal') for yy in (0.6, 0.4, 0.2)],
    caja(w - 0.5, 0.42, 0.02, x=-0.2, y=0.5, z=-0.3, c=c)]
obj('escritorio_oficina', 'Escritorio de oficina', 'mesa', 36, 'madera', 'suelo', DESK_BODY(1.4, BEECH), superficies=[{'y': 0.75, 'margen': 0.05}])
obj('escritorio_gerente', 'Escritorio de gerente', 'mesa', 44, 'madera', 'suelo', [
    caja(1.6, 0.04, 0.8, y=0.73, c='#8a5a36'), caja(0.45, 0.71, 0.7, x=-0.575, y=0.355, c='#6a4228'), caja(0.45, 0.71, 0.7, x=0.575, y=0.355, c='#6a4228'),
    caja(0.7, 0.45, 0.02, y=0.48, z=-0.33, c='#6a4228'),
    *[caja(0.38, 0.19, 0.012, x=sx * 0.575, y=yy, z=0.356, c='#7a4e30') for sx in (-1, 1) for yy in (0.58, 0.36, 0.14)],
    *[caja(0.12, 0.015, 0.015, x=sx * 0.575, y=yy + 0.05, z=0.368, c=GOLD, m='metal') for sx in (-1, 1) for yy in (0.58, 0.36, 0.14)]],
    superficies=[{'y': 0.75, 'margen': 0.06}])
obj('puesto_oficina', 'Escritorio con su silla giratoria', 'mueble', 52, 'madera', 'suelo',
    DESK_BODY(1.4, BEECH) + lado([dict(p, p=[p['p'][0], p['p'][1], p['p'][2] - 0.52]) for p in SILLA_G]), superficies=[{'y': 0.75, 'margen': 0.05}],
    nota='el escritorio con su silla detrás, para la gente que trabaja en él')
obj('puesto_gerencia', 'Escritorio de gerente con su sillón', 'mueble', 62, 'madera', 'suelo', [
    caja(1.6, 0.04, 0.8, y=0.73, c='#8a5a36'), caja(0.45, 0.71, 0.7, x=-0.575, y=0.355, c='#6a4228'), caja(0.45, 0.71, 0.7, x=0.575, y=0.355, c='#6a4228'),
    caja(0.7, 0.45, 0.02, y=0.48, z=-0.33, c='#6a4228'),
    *[caja(0.38, 0.19, 0.012, x=sx * 0.575, y=yy, z=0.356, c='#7a4e30') for sx in (-1, 1) for yy in (0.58, 0.36, 0.14)],
    # (the manager's armchair behind it: leather, high back, on a star base)
    *[caja(0.34, 0.03, 0.05, x=0.17 * math.sin(math.radians(72 * k)), y=0.065, z=0.55 + 0.17 * math.cos(math.radians(72 * k)), c=DARK, m='plastico', r=[0, 72 * k - 90, 0]) for k in range(5)],
    *[cil(0.022, 0.022, 0.05, x=0.33 * math.sin(math.radians(72 * k)), y=0.025, z=0.55 + 0.33 * math.cos(math.radians(72 * k)), c=BLACK, m='goma', seg=8) for k in range(5)],
    cil(0.03, 0.03, 0.34, y=0.26, z=0.55, c=GREY, seg=8), caja(0.54, 0.09, 0.52, y=0.48, z=0.55, c='#3a2418', m='tela'),
    caja(0.52, 0.7, 0.09, y=0.92, z=0.78, c='#3a2418', m='tela', r=[8, 0, 0]),
    caja(0.07, 0.04, 0.34, x=-0.3, y=0.7, z=0.55, c='#2a1810', m='tela'), caja(0.07, 0.04, 0.34, x=0.3, y=0.7, z=0.55, c='#2a1810', m='tela')],
    superficies=[{'y': 0.75, 'margen': 0.06}], nota='el escritorio del director con su sillón de piel detrás')
obj('mesa_reunion', 'Mesa de reuniones', 'mesa', 44, 'madera', 'suelo', [
    caja(2.2, 0.04, 1.0, y=0.73, c=BEECH), caja(0.05, 0.71, 0.8, x=-0.95, y=0.355, c=GREY, m='metal'), caja(0.05, 0.71, 0.8, x=0.95, y=0.355, c=GREY, m='metal'),
    caja(1.85, 0.3, 0.02, y=0.5, z=-0.35, c=GREY, m='metal')], superficies=[{'y': 0.75, 'margen': 0.07}])
obj('mesa_baja', 'Mesa baja de sala de espera', 'mesa', 13, 'madera', 'suelo', [
    caja(0.9, 0.04, 0.5, y=0.4, c=BEECH), *[caja(0.04, 0.38, 0.04, x=sx * 0.4, y=0.19, z=sz * 0.2, c=GREY, m='metal') for sx in (-1, 1) for sz in (-1, 1)]],
    superficies=[{'y': 0.42, 'margen': 0.05}])
obj('mostrador_recepcion_modulo', 'Módulo de mostrador de recepción (1,2 m)', 'mostrador', 450, 'madera', 'suelo', [
    caja(1.2, 1.04, 0.1, y=0.52, z=0.3, c='#a8845a'), caja(1.2, 0.04, 0.4, y=1.06, z=0.17, c=BEECH),
    caja(1.2, 0.03, 0.55, y=0.735, z=-0.25, c=BEECH), caja(1.2, 0.5, 0.02, y=0.5, z=-0.52, c='#a8845a'),
    caja(0.03, 0.72, 0.5, x=-0.585, y=0.36, z=-0.27, c=GREY, m='metal'), caja(0.03, 0.72, 0.5, x=0.585, y=0.36, z=-0.27, c=GREY, m='metal'),
    caja(1.2, 0.5, 0.35, y=0.8, z=0.08, c='#a8845a'),
    # (the clerk's screen, keyboard and telephone, facing -z)
    caja(0.04, 0.14, 0.03, x=-0.25, y=0.84, z=-0.28, c=DARK, m='plastico'), caja(0.46, 0.28, 0.03, x=-0.25, y=1.0, z=-0.28, c=DARK, m='plastico'),
    caja(0.42, 0.24, 0.006, x=-0.25, y=1.0, z=-0.3, c='#1c2630', m='plastico'), caja(0.42, 0.015, 0.15, x=-0.25, y=0.7625, z=-0.42, c=DARK, m='plastico'),
    caja(0.18, 0.06, 0.2, x=0.3, y=0.78, z=-0.32, c=GREYD, m='plastico')],
    superficies=[{'y': 1.08, 'margen': 0.05}], fijo='estructural', nota='mostrador de recepción: el voladizo de cara al público (1,08 m) es lo único que se amuebla; detrás, la mesa de quien atiende')

# ---------------------------------------------------------------- storage and machines of an office
obj('archivador_metalico', 'Archivador metálico de cuatro cajones', 'mueble', 38, 'metal', 'suelo', [
    caja(0.47, 1.32, 0.62, c='#9aa1a8', m='metal'),
    *[caja(0.43, 0.29, 0.012, y=0.19 + 0.32 * k, z=0.316, c='#b3b8bc', m='metal') for k in range(4)],
    *[caja(0.16, 0.025, 0.02, y=0.3 + 0.32 * k, z=0.335, c=GREYD, m='metal') for k in range(4)],
    *[caja(0.07, 0.04, 0.003, y=0.26 + 0.32 * k, z=0.323, c=WHITE, m='papel') for k in range(4)]],
    superficies=[{'y': 1.32, 'margen': 0.04}])
obj('armario_oficina', 'Armario de oficina con puertas', 'mueble', 70, 'madera', 'suelo', [
    caja(0.9, 1.9, 0.42, c='#cfc6b4'), caja(0.43, 1.84, 0.012, x=-0.22, y=0.96, z=0.216, c='#bfb5a0'), caja(0.43, 1.84, 0.012, x=0.22, y=0.96, z=0.216, c='#bfb5a0'),
    caja(0.02, 0.18, 0.02, x=-0.03, y=0.95, z=0.232, c=GREYD, m='metal'), caja(0.02, 0.18, 0.02, x=0.03, y=0.95, z=0.232, c=GREYD, m='metal')],
    superficies=[{'y': 1.9, 'margen': 0.04}])
SHELF = [0.035, 0.45, 0.85, 1.25, 1.65]
obj('estanteria_archivadores', 'Estantería de archivadores', 'estanteria', 60, 'madera', 'suelo', [
    caja(0.03, 2.0, 0.35, x=-0.435, c='#c9bba0'), caja(0.03, 2.0, 0.35, x=0.435, c='#c9bba0'), caja(0.84, 1.96, 0.01, y=1.0, z=-0.17, c='#b8aa90'),
    *[caja(0.84, 0.03, 0.34, y=y, c='#c9bba0') for y in SHELF], caja(0.84, 0.03, 0.34, y=1.985, c='#c9bba0')],
    superficies=[{'y': y + 0.015, 'fondo': 0.32} for y in SHELF[1:]])
for k, n, c in (('azul', 'azul', '#2a56a0'), ('rojo', 'rojo', '#b8302a'), ('verde', 'verde', '#2e7a46'), ('negro', 'negro', '#26282b'), ('amarillo', 'amarillo', '#d8a82a')):
    obj('archivador_' + k, f'Archivador de anillas {n}', 'oficina', 0.7, 'papel', 'superficie', [
        caja(0.08, 0.31, 0.28, c=c, m='plastico'), caja(0.05, 0.12, 0.004, y=0.2, z=0.142, c=WHITE, m='papel'), caja(0.045, 0.015, 0.004, y=0.1, z=0.142, c=STEEL, m='metal')])
obj('caja_archivo', 'Caja de archivo', 'caja', 2, 'papel', 'superficie', [caja(0.38, 0.26, 0.3, c='#c5a77a', m='papel'), caja(0.39, 0.03, 0.31, y=0.275, c='#b8996a', m='papel'), caja(0.12, 0.06, 0.004, y=0.14, z=0.152, c=WHITE, m='papel')])
obj('fotocopiadora', 'Fotocopiadora multifunción', 'electrodomestico', 85, 'plastico', 'suelo', [
    caja(0.66, 0.78, 0.62, c='#d9dcde', m='plastico'), caja(0.66, 0.05, 0.6, y=0.805, c='#c4c8ca', m='plastico'), caja(0.5, 0.012, 0.4, y=0.835, z=0.0, c=GLASS, m='cristal'),
    caja(0.3, 0.06, 0.2, x=0.14, y=0.86, z=0.2, c=DARK, m='plastico', r=[-18, 0, 0]),
    caja(0.54, 0.1, 0.5, y=0.2, z=0.12, c='#bfc3c6', m='plastico'), caja(0.54, 0.1, 0.5, y=0.45, z=0.12, c='#bfc3c6', m='plastico'),
    caja(0.12, 0.05, 0.01, x=-0.2, y=0.65, z=0.312, c=GREYD, m='plastico')], modificadores=['USE'], nota='con su bandeja de papel y la pantalla táctil')
obj('impresora_sobremesa', 'Impresora de oficina', 'informatica', 7, 'plastico', 'superficie', [
    caja(0.36, 0.2, 0.32, c='#d4d7d9', m='plastico'), caja(0.3, 0.012, 0.12, y=0.206, z=-0.05, c=WHITE, m='papel'),
    caja(0.3, 0.012, 0.16, y=0.03, z=0.21, c=WHITE, m='papel'), caja(0.12, 0.03, 0.01, x=0.1, y=0.14, z=0.161, c=GREYD, m='plastico')], modificadores=['USE'])
obj('trituradora_papel', 'Trituradora de papel', 'oficina', 9, 'plastico', 'suelo', [
    caja(0.36, 0.5, 0.25, c=BLACK, m='plastico'), caja(0.38, 0.06, 0.27, y=0.53, c=DARK, m='plastico'), caja(0.28, 0.012, 0.02, y=0.565, c=GREYD, m='metal')], modificadores=['USE'])
obj('dispensador_agua', 'Dispensador de agua', 'electrodomestico', 16, 'plastico', 'suelo', [
    caja(0.32, 0.92, 0.32, c='#e2e6e8', m='plastico'), cil(0.14, 0.14, 0.38, y=1.14, c='#8fc4de', m='cristal'), cil(0.04, 0.04, 0.03, y=1.34, c='#8fc4de', m='cristal'),
    caja(0.07, 0.03, 0.04, x=-0.06, y=0.72, z=0.175, c='#3a7ac0', m='plastico'), caja(0.07, 0.03, 0.04, x=0.06, y=0.72, z=0.175, c=RED, m='plastico'),
    caja(0.24, 0.02, 0.1, y=0.62, z=0.14, c=GREYD, m='metal')], modificadores=['USE'])
obj('papelera_reciclaje', 'Papelera de reciclaje de papel', 'papelera', 2.5, 'plastico', 'suelo', [cil(0.15, 0.13, 0.5, c='#2a5aa8', m='plastico'), cil(0.155, 0.155, 0.03, y=0.515, c='#1c3f78', m='plastico'), caja(0.14, 0.02, 0.01, y=0.5, z=0.15, c=BLACK, m='plastico')])
obj('paraguero', 'Paragüero', 'mueble', 3.2, 'metal', 'suelo', [
    cil(0.13, 0.12, 0.5, c='#3a3e44', m='metal'), cil(0.012, 0.012, 0.35, x=-0.03, y=0.6, z=0.02, c='#1a2a4a', m='plastico', r=[0, 0, 8]), cil(0.012, 0.012, 0.35, x=0.04, y=0.6, z=-0.03, c='#7a1f24', m='plastico', r=[0, 0, -10])])
obj('planta_alta', 'Ficus en maceta', 'planta', 11, 'ceramica', 'suelo', [
    cil(0.17, 0.13, 0.3, c='#3a3e44', m='ceramica'), cil(0.018, 0.022, 0.8, y=0.7, c='#6a4a2a', m='madera'),
    esf(0.3, 0, 1.25, 0, c='#3f7a3a', m='madera', s=[1, 1.1, 1]), esf(0.2, 0.18, 1.0, 0.06, c='#4c8a42', m='madera'), esf(0.18, -0.16, 1.5, -0.04, c='#4c8a42', m='madera')])
obj('extintor', 'Extintor de polvo', 'seguridad_local', 6, 'metal', 'pared', [
    cil(0.07, 0.07, 0.42, y=0.95, z=0.09, c=RED), cil(0.025, 0.025, 0.07, y=1.19, z=0.09, c=DARK), caja(0.14, 0.04, 0.03, y=0.9, z=0.015, c=GREYD, m='metal'),
    caja(0.04, 0.05, 0.06, x=0.05, y=1.21, z=0.1, c=DARK, m='plastico'), caja(0.05, 0.08, 0.003, y=1.0, z=0.162, c=WHITE, m='papel')], nota='junto a la puerta, a un metro del suelo')
obj('senal_salida', 'Señal de salida de emergencia', 'seguridad_local', 1.2, 'plastico', 'pared', [
    caja(0.4, 0.15, 0.04, y=2.3, z=0.02, c=GREEN, m='plastico'), caja(0.34, 0.09, 0.005, y=2.3, z=0.0425, c=WHITE, m='plastico', luz=True)], fijo='anclado en la realidad')
obj('aire_acondicionado', 'Aire acondicionado de pared', 'electrodomestico', 15, 'plastico', 'pared', [
    caja(0.95, 0.3, 0.22, y=2.35, z=0.11, c=WHITE, m='plastico'), caja(0.9, 0.04, 0.02, y=2.23, z=0.215, c='#d4d8da', m='plastico'), caja(0.05, 0.02, 0.005, x=0.38, y=2.4, z=0.222, c=GREEN, m='plastico')],
    fijo='anclado en la realidad')
obj('tablon_corcho', 'Tablón de corcho', 'decoracion', 2, 'madera', 'pared', [
    caja(0.9, 0.6, 0.025, y=1.65, z=0.0125, c=WOOD), caja(0.84, 0.54, 0.01, y=1.65, z=0.03, c='#b88c57'),
    *[caja(0.13, 0.17, 0.003, x=-0.3 + 0.2 * (k % 4), y=1.78 - 0.24 * (k // 4), z=0.037, c=cc, m='papel') for k, cc in enumerate(['#f1efe9', '#f2d56a', '#9ac4e0', '#f1efe9', '#e8a0a0', '#f1efe9', '#a8d8a0', '#f2d56a'])]])
obj('diploma_enmarcado', 'Diploma enmarcado', 'cuadro', 0.8, 'madera', 'pared', [caja(0.44, 0.34, 0.025, y=1.7, z=0.0125, c='#3a2a1c'), plano(0.38, 0.28, y=1.7, z=0.026, tex={'tipo': 'diploma'})])
obj('pizarra_blanca', 'Pizarra blanca de la sala de reuniones', 'decoracion', 5, 'plastico', 'pared', [
    caja(1.3, 0.95, 0.025, y=1.5, z=0.0125, c='#a8aeb2', m='metal'), caja(1.24, 0.89, 0.006, y=1.5, z=0.028, c='#f6f6f2', m='plastico'), caja(1.0, 0.02, 0.05, y=1.01, z=0.045, c='#a8aeb2', m='metal'),
    caja(0.12, 0.02, 0.012, x=-0.2, y=1.035, z=0.07, c='#2a56a0', m='plastico'), caja(0.12, 0.02, 0.012, x=0.0, y=1.035, z=0.07, c=RED, m='plastico')], fijo='anclado en la realidad')
obj('cartel_aseguradora', 'Cartel de seguros', 'cuadro', 1.3, 'papel', 'pared', [caja(0.52, 0.72, 0.02, y=1.65, z=0.01, c='#1a3a5a'), plano(0.48, 0.68, y=1.65, z=0.021, tex={'tipo': 'cartel_seguros'})])

# ---------------------------------------------------------------- what stands on a desk
obj('monitor_pc', 'Monitor de ordenador', 'informatica', 4.2, 'plastico', 'superficie', [
    caja(0.22, 0.015, 0.16, c=DARK, m='plastico'), caja(0.05, 0.13, 0.03, y=0.08, z=-0.02, c=DARK, m='plastico'),
    caja(0.5, 0.3, 0.03, y=0.3, z=-0.02, c=DARK, m='plastico'), caja(0.46, 0.26, 0.004, y=0.3, z=-0.0, c='#18222e', m='plastico')])
obj('monitor_pc_encendido', 'Monitor de ordenador encendido', 'informatica', 4.2, 'plastico', 'superficie', [
    caja(0.22, 0.015, 0.16, c=DARK, m='plastico'), caja(0.05, 0.13, 0.03, y=0.08, z=-0.02, c=DARK, m='plastico'),
    caja(0.5, 0.3, 0.03, y=0.3, z=-0.02, c=DARK, m='plastico'), caja(0.46, 0.26, 0.004, y=0.3, z=0.0, c='#cfe0ee', m='plastico', luz=True)])
obj('portatil', 'Portátil abierto', 'informatica', 1.8, 'plastico', 'superficie', [
    caja(0.33, 0.02, 0.23, c='#9aa0a6', m='metal'), caja(0.31, 0.2, 0.012, y=0.115, z=-0.11, c='#9aa0a6', m='metal', r=[-12, 0, 0]),
    caja(0.28, 0.17, 0.003, y=0.115, z=-0.102, c='#161c24', m='plastico', r=[-12, 0, 0]), caja(0.28, 0.003, 0.08, y=0.0215, z=0.02, c=GREYD, m='plastico')])
obj('teclado', 'Teclado', 'informatica', 0.7, 'plastico', 'superficie', [caja(0.44, 0.02, 0.15, c='#d4d7d9', m='plastico'), caja(0.4, 0.004, 0.11, y=0.021, c='#3a3e44', m='plastico')])
obj('raton_pc', 'Ratón', 'oficina', 0.1, 'plastico', 'superficie', [caja(0.06, 0.03, 0.1, c='#2b2b2e', m='plastico')])
obj('telefono_fijo', 'Teléfono de mesa', 'informatica', 0.9, 'plastico', 'superficie', [
    caja(0.2, 0.05, 0.2, c='#2b2b2e', m='plastico'), caja(0.05, 0.04, 0.2, x=-0.07, y=0.07, c='#2b2b2e', m='plastico'), caja(0.1, 0.012, 0.1, x=0.04, y=0.056, z=0.03, c='#4a4e54', m='plastico')])
obj('bandeja_documentos', 'Bandeja de documentos', 'oficina', 1, 'plastico', 'superficie', [
    *[caja(0.3, 0.012, 0.24, y=0.006 + 0.07 * k, c='#3a3e44', m='plastico') for k in range(3)], *[caja(0.012, 0.2, 0.24, x=sx * 0.144, y=0.1, c='#3a3e44', m='plastico') for sx in (-1, 1)],
    caja(0.26, 0.012, 0.2, y=0.025, c=WHITE, m='papel'), caja(0.26, 0.02, 0.2, y=0.105, c='#f2e8c8', m='papel')])
obj('pila_carpetas', 'Pila de carpetas', 'oficina', 1.4, 'papel', 'superficie', [
    caja(0.24, 0.025, 0.32, c='#2a56a0', m='papel'), caja(0.24, 0.025, 0.32, y=0.038, c='#d8a82a', m='papel'), caja(0.24, 0.025, 0.32, y=0.063, c='#b8302a', m='papel'), caja(0.24, 0.025, 0.32, y=0.088, c='#2e7a46', m='papel')])
obj('lampara_escritorio', 'Lámpara de escritorio', 'lampara', 1.1, 'metal', 'superficie', [
    cil(0.07, 0.07, 0.02, c=DARK, m='metal'), cil(0.008, 0.008, 0.3, y=0.17, z=-0.01, c=DARK, m='metal', r=[10, 0, 0]),
    cil(0.008, 0.008, 0.26, x=0.0, y=0.4, z=0.05, c=DARK, m='metal', r=[70, 0, 0]), dict(cono(0.06, 0.1, y=0.46, z=0.17, c='#2a6a4a', m='metal'), r=[100, 0, 0])])
obj('grapadora', 'Grapadora', 'oficina', 0.3, 'metal', 'superficie', [caja(0.05, 0.03, 0.16, c='#b8302a', m='plastico'), caja(0.045, 0.012, 0.15, y=0.036, c=DARK, m='metal')])
obj('portalapices', 'Vaso portalápices', 'oficina', 0.3, 'metal', 'superficie', [cil(0.04, 0.04, 0.1, c='#3a3e44', m='metal', seg=10), cil(0.004, 0.004, 0.08, x=-0.015, y=0.12, c='#2a56a0', m='plastico', r=[0, 0, 8]), cil(0.004, 0.004, 0.08, x=0.012, y=0.12, c='#b8302a', m='plastico', r=[0, 0, -10])])
obj('calculadora', 'Calculadora de mesa', 'oficina', 0.2, 'plastico', 'superficie', [caja(0.13, 0.02, 0.19, c='#d4d7d9', m='plastico'), caja(0.1, 0.004, 0.04, y=0.021, z=-0.06, c='#9ab49a', m='plastico'), caja(0.1, 0.004, 0.09, y=0.021, z=0.04, c='#4a4e54', m='plastico')])
obj('bloc_notas', 'Bloc de notas', 'papel', 0.25, 'papel', 'superficie', [caja(0.15, 0.015, 0.21, c='#f2e8a8', m='papel'), caja(0.15, 0.004, 0.02, y=0.0155, z=-0.095, c=STEEL, m='metal')])
obj('sello_tampon', 'Sello y tampón', 'oficina', 0.2, 'plastico', 'superficie', [caja(0.09, 0.02, 0.06, c='#2a56a0', m='plastico'), cil(0.018, 0.018, 0.06, x=0.04, y=0.05, z=0.0, c=WOOD_D, m='madera', seg=8)])
obj('tarjetero_visitas', 'Tarjetero de visitas', 'oficina', 0.2, 'plastico', 'superficie', [caja(0.1, 0.03, 0.06, c=STEEL, m='metal'), caja(0.09, 0.05, 0.012, y=0.04, z=-0.02, c=WHITE, m='papel', r=[-12, 0, 0])])
obj('cuaderno_citas', 'Agenda de citas', 'papel', 0.4, 'papel', 'superficie', [caja(0.21, 0.025, 0.29, c='#7a1f24', m='papel'), caja(0.2, 0.01, 0.28, y=0.016, c='#f2ede0', m='papel')])

# ---------------------------------------------------------------- ceiling fittings (each with a light part gets a point light in the game)
obj('panel_led', 'Panel LED de techo (60 × 60)', 'lampara', 3, 'metal', 'techo', [
    caja(0.62, 0.02, 0.62, y=-0.01, c='#e6e8ea', m='metal'), caja(0.57, 0.008, 0.57, y=-0.024, c=WHITE, m='plastico', luz=True)], fijo='anclado en la realidad')
obj('regleta_led_techo', 'Regleta LED (1,2 m)', 'lampara', 2.2, 'metal', 'techo', [
    caja(1.2, 0.05, 0.12, y=-0.025, c='#e6e8ea', m='metal'), caja(1.14, 0.008, 0.08, y=-0.054, c=WHITE, m='plastico', luz=True)], fijo='anclado en la realidad')
obj('foco_empotrable', 'Foco LED empotrado', 'lampara', 0.6, 'metal', 'techo', [
    cil(0.075, 0.075, 0.02, y=-0.01, c='#e6e8ea', m='metal'), cil(0.05, 0.05, 0.006, y=-0.023, c=WHITE, m='plastico', luz=True)], fijo='anclado en la realidad')
obj('luminaria_campana', 'Campana industrial de LED', 'lampara', 4.5, 'metal', 'techo', [
    cil(0.006, 0.006, 0.55, y=-0.275, c=DARK), cil(0.04, 0.04, 0.05, y=-0.025, c=DARK), cono(0.3, 0.22, y=-0.66, c='#d8dcde', m='metal'),
    cil(0.14, 0.14, 0.02, y=-0.78, c=WHITE, m='plastico', luz=True)], fijo='anclado en la realidad', nota='para techos altos: la nave de un gimnasio')
obj('camara_seguridad', 'Cámara de vigilancia en cúpula', 'seguridad_local', 0.8, 'plastico', 'techo', [
    cil(0.075, 0.075, 0.025, y=-0.0125, c=WHITE, m='plastico'), esf(0.06, 0, -0.048, 0, c='#2a2a2e', m='plastico', s=[1, 0.8, 1]), cil(0.012, 0.012, 0.01, y=-0.085, c='#4a8ac0', m='cristal')], fijo='anclado en la realidad')
obj('detector_humo', 'Detector de humos', 'seguridad_local', 0.2, 'plastico', 'techo', [cil(0.055, 0.055, 0.03, y=-0.015, c=WHITE, m='plastico'), cil(0.012, 0.012, 0.008, y=-0.032, c=RED, m='plastico')], fijo='anclado en la realidad')

# ================================================================ the bank
obj('cajero_automatico', 'Cajero automático', 'cajero', 520, 'metal', 'suelo', [
    caja(0.56, 0.95, 0.52, c='#6a7078', m='metal'), caja(0.56, 0.75, 0.4, y=1.325, z=-0.06, c='#6a7078', m='metal'),
    caja(0.5, 0.1, 0.012, y=1.63, z=0.146, c=WHITE, m='plastico', luz=True), caja(0.4, 0.32, 0.03, y=1.3, z=0.155, c=BLACK, m='plastico'),
    plano(0.34, 0.26, y=1.3, z=0.171, tex={'tipo': 'cajero_pantalla', 'rotulo_local': True}, m='plastico', luz=True),
    caja(0.5, 0.05, 0.2, y=1.0, z=0.22, c=DARK, m='plastico', r=[-12, 0, 0]), caja(0.14, 0.012, 0.14, x=0.1, y=1.035, z=0.215, c='#7a8086', m='metal', r=[-12, 0, 0]),
    caja(0.1, 0.03, 0.02, x=-0.14, y=1.1, z=0.15, c=BLACK, m='plastico'), caja(0.3, 0.07, 0.03, y=0.78, z=0.265, c=BLACK, m='plastico'),
    caja(0.14, 0.01, 0.04, x=-0.16, y=0.62, z=0.265, c='#7a8086', m='metal')],
    fijo='anclado en la realidad', modificadores=['USE'], nota='el cajero de la entrada: con su pantalla, su teclado y la ranura de los billetes')
obj('actualizador_libretas', 'Actualizador de libretas', 'maquina_expendedora', 140, 'metal', 'suelo', [
    caja(0.46, 0.95, 0.38, c='#6a7078', m='metal'), caja(0.46, 0.3, 0.3, y=1.1, z=-0.04, c='#6a7078', m='metal'),
    caja(0.28, 0.14, 0.01, y=1.16, z=0.112, c='#18222e', m='plastico'), caja(0.3, 0.03, 0.02, y=0.98, z=0.195, c=BLACK, m='plastico'),
    caja(0.12, 0.04, 0.12, x=0.14, y=1.0, z=0.16, c=DARK, m='plastico'), caja(0.24, 0.008, 0.004, y=1.0, z=0.208, c=GOLD, m='metal')],
    modificadores=['USE'], nota='donde se pone la libreta para que se actualice')
obj('ventanilla_modulo', 'Módulo de ventanilla con mampara (1,2 m)', 'mostrador', 450, 'madera', 'suelo', [
    caja(1.2, 1.04, 0.1, y=0.52, z=0.41, c='#1d6e7c'), caja(1.2, 1.04, 0.02, y=0.52, z=0.01, c='#6a6e72'), caja(0.02, 1.04, 0.46, x=-0.59, y=0.52, z=0.24, c='#17606d'), caja(0.02, 1.04, 0.46, x=0.59, y=0.52, z=0.24, c='#17606d'),
    caja(1.2, 0.04, 0.46, y=1.06, z=0.24, c=STONE, m='piedra'),
    caja(1.2, 0.86, 0.012, y=1.51, z=0.03, c='#c8dde4', m='cristal'), caja(1.2, 0.03, 0.04, y=1.955, z=0.03, c=STEEL), caja(0.3, 0.07, 0.03, y=1.115, z=0.03, c=STEEL), caja(0.12, 0.1, 0.016, y=1.35, z=0.03, c=STEEL),
    caja(1.2, 0.03, 0.55, y=0.735, z=-0.29, c='#cfcabb'), caja(0.03, 0.72, 0.5, x=-0.585, y=0.36, z=-0.3, c=GREY), caja(0.03, 0.72, 0.5, x=0.585, y=0.36, z=-0.3, c=GREY), caja(1.2, 0.5, 0.02, y=0.5, z=-0.55, c='#a8a89c'),
    caja(0.04, 0.14, 0.03, x=-0.25, y=0.83, z=-0.3, c=DARK, m='plastico'), caja(0.46, 0.28, 0.03, x=-0.25, y=1.0, z=-0.3, c=DARK, m='plastico'),
    caja(0.42, 0.24, 0.006, x=-0.25, y=1.0, z=-0.318, c='#18222e', m='plastico'), caja(0.42, 0.015, 0.15, x=-0.25, y=0.7625, z=-0.42, c=DARK, m='plastico'),
    caja(0.26, 0.15, 0.3, x=0.3, y=0.825, z=-0.3, c='#d8dbde', m='plastico'), caja(0.14, 0.04, 0.1, x=0.3, y=0.92, z=-0.37, c=DARK, m='plastico')],
    superficies=[{'y': 1.08, 'margen': 0.05}], fijo='estructural', nota='la ventanilla de caja: voladizo de piedra y mampara de cristal; detrás, el puesto del cajero')
obj('dispensador_turnos', 'Máquina de turnos', 'terminal_cliente', 28, 'plastico', 'suelo', [
    caja(0.3, 1.0, 0.28, c=TEAL, m='plastico'), caja(0.36, 0.3, 0.22, y=1.15, z=0.02, c='#e8ecee', m='plastico'), caja(0.24, 0.18, 0.01, y=1.2, z=0.132, c='#18222e', m='plastico', r=[-10, 0, 0]),
    caja(0.12, 0.03, 0.05, y=1.03, z=0.15, c=DARK, m='plastico'), *[caja(0.05, 0.03, 0.01, x=-0.07 + 0.07 * k, y=1.1, z=0.133, c=cc, m='plastico') for k, cc in enumerate(['#d8a82a', '#2e7a46', '#b8302a'])]],
    modificadores=['USE'], nota='saca el papel con el número de turno')
obj('pantalla_turnos', 'Pantalla de turnos', 'pantalla', 6, 'plastico', 'pared', [
    caja(0.92, 0.3, 0.05, y=2.3, z=0.025, c=BLACK, m='plastico'), plano(0.86, 0.24, y=2.3, z=0.0525, tex={'tipo': 'turnos_pantalla'}, m='plastico', luz=True)], fijo='anclado en la realidad')
obj('expositor_folletos', 'Expositor de folletos de pie', 'mueble', 12, 'metal', 'suelo', [
    caja(0.5, 0.05, 0.3, c=GREYD, m='metal'), caja(0.48, 1.5, 0.03, y=0.8, z=-0.12, c='#e8ecee', m='metal'),
    *[caja(0.46, 0.03, 0.13, y=0.32 + 0.3 * k, z=-0.04, c=STEEL, m='metal') for k in range(4)],
    *[caja(0.4, 0.22, 0.012, y=0.44 + 0.3 * k, z=-0.075, c=cc, m='papel') for k, cc in enumerate(['#2a56a0', '#d8a82a', '#2e7a46', '#b8302a'])],
    caja(0.5, 0.12, 0.04, y=1.6, z=-0.12, c=TEAL, m='plastico')])
obj('expositor_folletos_pared', 'Portafolletos de pared', 'decoracion', 1.6, 'plastico', 'pared', [
    caja(0.34, 0.62, 0.02, y=1.4, z=0.01, c='#e8ecee', m='plastico'), *[caja(0.32, 0.03, 0.08, y=1.2 + 0.19 * k, z=0.05, c=STEEL, m='plastico') for k in range(3)],
    *[caja(0.28, 0.15, 0.006, y=1.285 + 0.19 * k, z=0.03, c=cc, m='papel') for k, cc in enumerate(['#d8a82a', '#2a56a0', '#2e7a46'])]])
obj('folletos_pila', 'Montón de folletos', 'papel', 0.25, 'papel', 'superficie', [caja(0.15, 0.025, 0.21, c='#f2ede0', m='papel'), caja(0.15, 0.006, 0.21, y=0.0155, c='#2a56a0', m='papel'), caja(0.15, 0.025, 0.21, y=0.04, c='#f2ede0', m='papel')])
obj('puerta_camara', 'Puerta de la cámara acorazada', 'caja_fuerte', 1500, 'metal', 'pared', [
    caja(1.7, 2.3, 0.14, y=1.15, z=0.07, c='#4a4f56', m='metal'), cil(0.66, 0.66, 0.14, y=1.15, z=0.17, c='#9aa0a6', m='metal', r=[90, 0, 0], seg=20),
    cil(0.5, 0.5, 0.05, y=1.15, z=0.255, c='#6a7078', m='metal', r=[90, 0, 0], seg=20), cil(0.2, 0.2, 0.05, y=1.15, z=0.3, c='#3a3e44', m='metal', r=[90, 0, 0], seg=16),
    caja(0.7, 0.045, 0.04, y=1.15, z=0.33, c=STEEL, m='metal'), caja(0.045, 0.7, 0.04, y=1.15, z=0.33, c=STEEL, m='metal'),
    cil(0.05, 0.05, 0.07, y=1.15, z=0.32, c=GOLD, m='metal', r=[90, 0, 0], seg=10),
    caja(0.08, 0.3, 0.1, x=-0.76, y=0.6, z=0.17, c='#3a3e44', m='metal'), caja(0.08, 0.3, 0.1, x=-0.76, y=1.7, z=0.17, c='#3a3e44', m='metal'),
    caja(0.26, 0.1, 0.02, x=0.6, y=0.3, z=0.15, c=BLACK, m='plastico'), caja(0.2, 0.06, 0.003, x=0.6, y=0.3, z=0.161, c='#9ab49a', m='plastico')],
    fijo='anclado en la realidad', nota='la puerta redonda de la cámara acorazada, con su rueda y el reloj de cierre')
obj('caja_fuerte', 'Caja fuerte', 'caja_fuerte', 380, 'metal', 'suelo', [
    caja(0.7, 1.0, 0.6, c='#3a4a3e', m='metal'), caja(0.62, 0.9, 0.04, y=0.5, z=0.32, c='#4a5a4e', m='metal'), cil(0.07, 0.07, 0.04, y=0.55, z=0.36, c=STEEL, m='metal', r=[90, 0, 0], seg=16),
    caja(0.18, 0.025, 0.03, x=0.14, y=0.55, z=0.375, c=STEEL, m='metal'), caja(0.1, 0.04, 0.01, x=-0.2, y=0.72, z=0.345, c=BLACK, m='plastico')],
    fijo='anclado en la realidad', modificadores=['USE'])
obj('rotulo_banco', 'Rótulo del banco', 'decoracion', 9.5, 'metal', 'pared', [
    caja(2.4, 0.5, 0.06, y=2.4, z=0.03, c=TEAL, m='plastico'), plano(2.3, 0.42, y=2.4, z=0.0615, tex={'tipo': 'rotulo_banco', 'rotulo_local': True}, m='plastico')], fijo='anclado en la realidad')
obj('cartel_hipotecas', 'Cartel de hipotecas', 'cuadro', 1.2, 'papel', 'pared', [caja(0.62, 0.92, 0.02, y=1.55, z=0.01, c=TEAL), plano(0.56, 0.86, y=1.55, z=0.021, tex={'tipo': 'cartel_banco', 'lema': 'hipoteca'})])
obj('cartel_ahorro', 'Cartel de planes de ahorro', 'cuadro', 1.2, 'papel', 'pared', [caja(0.62, 0.92, 0.02, y=1.55, z=0.01, c='#7a5a1c'), plano(0.56, 0.86, y=1.55, z=0.021, tex={'tipo': 'cartel_banco', 'lema': 'ahorro'})])
obj('cartel_horario_banco', 'Horario de atención al público', 'cuadro', 0.6, 'papel', 'pared', [caja(0.34, 0.46, 0.015, y=1.55, z=0.0075, c='#2a2a2e'), plano(0.3, 0.42, y=1.55, z=0.016, tex={'tipo': 'cartel_horario', 'titulo': 'ATENCIÓN AL PÚBLICO', 'lineas': ['Lunes a viernes', '8:30 a 14:00', 'Jueves también', '16:30 a 18:30', 'Sábados y domingos', 'cerrado']})])
obj('cartel_horario_oficina', 'Horario de la oficina', 'cuadro', 0.6, 'papel', 'pared', [caja(0.34, 0.48, 0.015, y=1.55, z=0.0075, c='#2a2a2e'), plano(0.3, 0.42, y=1.55, z=0.016, tex={'tipo': 'cartel_horario', 'titulo': 'HORARIO', 'lineas': ['Lunes a viernes', '9:00 a 14:00', 'Tardes (salvo viernes)', '16:30 a 19:00', 'Sin cita previa', 'hasta las 13:30']})])
obj('dispensador_gel', 'Dispensador de gel hidroalcohólico', 'mueble', 6, 'metal', 'suelo', [
    cil(0.15, 0.17, 0.03, c=GREYD), cil(0.025, 0.025, 0.95, y=0.5, c=STEEL), caja(0.14, 0.2, 0.1, y=1.1, z=0.03, c='#e8ecee', m='plastico'), caja(0.04, 0.02, 0.07, y=1.0, z=0.1, c=DARK, m='plastico')], modificadores=['USE'])
obj('boligrafo_cadena', 'Bolígrafo con cadenita', 'oficina', 0.08, 'plastico', 'superficie', [
    cil(0.03, 0.035, 0.025, c=STEEL, seg=10), cil(0.006, 0.006, 0.15, x=0.0, y=0.1, z=0.0, c='#2a56a0', m='plastico', r=[0, 0, 18]), cil(0.003, 0.003, 0.1, x=0.06, y=0.012, z=0.0, c=STEEL, r=[0, 0, 90])])
obj('bote_caramelos', 'Bote de caramelos', 'recipiente', 0.4, 'cristal', 'superficie', [
    cil(0.05, 0.05, 0.13, c=GLASS, m='cristal'), cil(0.045, 0.045, 0.02, y=0.145, c=RED, m='plastico'),
    esf(0.014, -0.02, 0.04, 0.01, c='#d8a82a'), esf(0.014, 0.02, 0.06, -0.01, c=RED), esf(0.014, 0.0, 0.09, 0.02, c=GREEN), esf(0.014, 0.025, 0.03, 0.02, c='#2a56a0')])

# ================================================================ the gym
G_RUB, G_ORA = '#25262a', '#d8641c'
def torre(x, z, h=1.8, c='#8a9096'):
    # the weight stack of a machine: four posts, the stack of plates and a cap
    return [*[caja(0.05, h, 0.05, x=x + sx * 0.2, y=h / 2, z=z + sz * 0.2, c=DARK) for sx in (-1, 1) for sz in (-1, 1)],
            caja(0.32, h * 0.55, 0.32, x=x, y=0.1 + h * 0.275, z=z, c=c), caja(0.46, 0.05, 0.46, x=x, y=h + 0.025, z=z, c=DARK)]
def pantallita(x, y, z, rx=-25, w=0.3, h=0.1):
    return [caja(w + 0.06, h + 0.12, 0.08, x=x, y=y, z=z, c=DARK, m='plastico', r=[rx, 0, 0]), caja(w, h, 0.01, x=x, y=y + 0.01, z=z + 0.047, c=WHITE, m='plastico', r=[rx, 0, 0], luz=True)]

obj('cinta_correr', 'Cinta de correr', 'maquina_gimnasio', 110, 'metal', 'suelo', [
    caja(0.62, 0.04, 0.12, y=0.02, z=-0.72, c=DARK, m='goma'), caja(0.62, 0.04, 0.12, y=0.02, z=0.86, c=DARK, m='goma'),
    caja(0.7, 0.16, 1.5, y=0.12, z=0.07, c=GREYD), caja(0.5, 0.02, 1.42, y=0.21, z=0.07, c=BLACK, m='goma'),
    caja(0.1, 0.05, 1.46, x=-0.3, y=0.225, z=0.07, c=GREY), caja(0.1, 0.05, 1.46, x=0.3, y=0.225, z=0.07, c=GREY),
    caja(0.66, 0.28, 0.3, y=0.32, z=-0.55, c=GREYD), caja(0.05, 0.95, 0.05, x=-0.3, y=0.835, z=-0.6, c=DARK), caja(0.05, 0.95, 0.05, x=0.3, y=0.835, z=-0.6, c=DARK),
    *pantallita(0, 1.27, -0.62, -25, 0.3, 0.1),
    cil(0.018, 0.018, 0.55, x=-0.3, y=1.0, z=-0.32, c=BLACK, m='goma', r=[90, 0, 0]), cil(0.018, 0.018, 0.55, x=0.3, y=1.0, z=-0.32, c=BLACK, m='goma', r=[90, 0, 0])],
    modificadores=['USE'], nota='de espaldas a quien la usa se ve la consola: se sube por detrás (+z) y se corre de cara a la pared')
obj('bici_estatica', 'Bicicleta estática', 'equipo_gimnasio', 38, 'metal', 'suelo', [
    caja(0.55, 0.04, 0.1, y=0.02, z=-0.38, c=DARK, m='goma'), caja(0.5, 0.04, 0.1, y=0.02, z=0.38, c=DARK, m='goma'), caja(0.08, 0.08, 0.82, y=0.1, c=GREYD),
    cil(0.17, 0.17, 0.12, y=0.34, z=-0.05, c=GREYD, r=[0, 0, 90]), caja(0.03, 0.03, 0.17, x=0.08, y=0.34, z=-0.05, c=STEEL), caja(0.03, 0.03, 0.17, x=-0.08, y=0.34, z=-0.05, c=STEEL),
    caja(0.1, 0.03, 0.1, x=0.2, y=0.24, z=-0.05, c=BLACK, m='goma'), caja(0.1, 0.03, 0.1, x=-0.2, y=0.44, z=-0.05, c=BLACK, m='goma'),
    caja(0.05, 0.66, 0.05, y=0.47, z=0.3, c=STEEL), caja(0.24, 0.07, 0.28, y=0.835, z=0.32, c=BLACK, m='plastico'),
    caja(0.05, 0.9, 0.05, y=0.59, z=-0.36, c=GREYD), caja(0.46, 0.03, 0.04, y=1.05, z=-0.36, c=BLACK, m='goma'), *pantallita(0, 1.17, -0.38, -20, 0.14, 0.07)],
    modificadores=['USE', 'SEAT'], asientos=[{'p': [0, 0.87, 0.32], 'h': 0.87, 'anim': 'taburete_alto'}], nota='se sienta uno detrás (+z), de cara a la consola')
obj('bici_ciclo_indoor', 'Bicicleta de ciclo indoor', 'equipo_gimnasio', 52, 'metal', 'suelo', [
    caja(0.6, 0.04, 0.1, y=0.02, z=-0.42, c=DARK, m='goma'), caja(0.6, 0.04, 0.1, y=0.02, z=0.42, c=DARK, m='goma'), caja(0.08, 0.08, 0.9, y=0.1, c=RED),
    cil(0.24, 0.24, 0.06, y=0.38, z=-0.3, c=RED, r=[0, 0, 90]), caja(0.04, 0.5, 0.04, y=0.35, z=-0.05, c=RED), caja(0.1, 0.03, 0.1, x=0.2, y=0.2, z=-0.0, c=BLACK, m='goma'),
    caja(0.1, 0.03, 0.1, x=-0.2, y=0.5, z=-0.0, c=BLACK, m='goma'),
    caja(0.05, 0.7, 0.05, y=0.49, z=0.28, c=STEEL), caja(0.22, 0.07, 0.26, y=0.87, z=0.3, c=BLACK, m='plastico'),
    caja(0.05, 0.88, 0.05, y=0.58, z=-0.4, c=RED), caja(0.44, 0.03, 0.04, y=1.04, z=-0.42, c=BLACK, m='goma'), caja(0.03, 0.03, 0.2, x=-0.2, y=1.04, z=-0.32, c=BLACK, m='goma'),
    caja(0.03, 0.03, 0.2, x=0.2, y=1.04, z=-0.32, c=BLACK, m='goma'), caja(0.1, 0.05, 0.04, y=1.12, z=-0.43, c=DARK, m='plastico')],
    modificadores=['USE', 'SEAT'], asientos=[{'p': [0, 0.905, 0.3], 'h': 0.905, 'anim': 'taburete_alto'}])
obj('eliptica', 'Bicicleta elíptica', 'maquina_gimnasio', 88, 'metal', 'suelo', [
    caja(0.62, 0.04, 0.12, y=0.02, z=-0.7, c=DARK, m='goma'), caja(0.62, 0.04, 0.12, y=0.02, z=0.7, c=DARK, m='goma'), caja(0.5, 0.08, 1.4, y=0.08, c=GREYD),
    cil(0.22, 0.22, 0.5, y=0.34, z=-0.5, c=GREYD, r=[0, 0, 90]), caja(0.14, 0.04, 0.34, x=-0.2, y=0.17, z=0.3, c=BLACK, m='goma'), caja(0.14, 0.04, 0.34, x=0.2, y=0.17, z=0.3, c=BLACK, m='goma'),
    caja(0.05, 0.3, 0.05, x=-0.26, y=0.4, z=0.05, c=STEEL, r=[-12, 0, 0]), caja(0.05, 0.3, 0.05, x=0.26, y=0.4, z=0.05, c=STEEL, r=[-12, 0, 0]),
    caja(0.05, 1.3, 0.05, x=-0.28, y=0.85, z=-0.5, c=GREYD), caja(0.05, 1.3, 0.05, x=0.28, y=0.85, z=-0.5, c=GREYD),
    cil(0.018, 0.018, 0.5, x=-0.28, y=1.05, z=-0.28, c=BLACK, m='goma', r=[90, 0, 0]), cil(0.018, 0.018, 0.5, x=0.28, y=1.05, z=-0.28, c=BLACK, m='goma', r=[90, 0, 0]),
    *pantallita(0, 1.42, -0.54, -20, 0.26, 0.1)], modificadores=['USE'])
obj('remo_maquina', 'Máquina de remo', 'equipo_gimnasio', 26, 'metal', 'suelo', [
    caja(0.5, 0.04, 0.1, y=0.02, z=-0.8, c=DARK, m='goma'), caja(0.5, 0.04, 0.1, y=0.02, z=0.85, c=DARK, m='goma'),
    caja(0.06, 0.2, 0.06, x=0, y=0.14, z=-0.8, c=GREYD), caja(0.06, 0.2, 0.06, y=0.14, z=0.82, c=GREYD), caja(0.08, 0.06, 1.8, y=0.27, z=0.0, c=GREYD),
    cil(0.22, 0.22, 0.1, y=0.4, z=-0.75, c=GREYD, r=[0, 0, 90]), caja(0.3, 0.04, 0.3, y=0.34, z=0.35, c=BLACK, m='plastico'),
    caja(0.14, 0.18, 0.03, x=-0.12, y=0.42, z=-0.55, c=BLACK, m='plastico', r=[-30, 0, 0]), caja(0.14, 0.18, 0.03, x=0.12, y=0.42, z=-0.55, c=BLACK, m='plastico', r=[-30, 0, 0]),
    *pantallita(0, 0.62, -0.78, -30, 0.14, 0.06)], modificadores=['USE'])
obj('multiestacion', 'Multiestación de musculación', 'maquina_gimnasio', 260, 'metal', 'suelo', [
    caja(1.3, 0.05, 1.2, y=0.025, c=DARK), *torre(0, -0.45, 2.0), caja(0.06, 0.06, 0.9, y=2.0, z=-0.0, c=DARK),
    cil(0.015, 0.015, 0.9, y=1.85, z=0.3, c=STEEL, r=[0, 0, 90]), caja(0.4, 0.1, 0.4, y=0.45, z=0.3, c=BLACK, m='tela'), caja(0.4, 0.5, 0.1, y=0.8, z=0.55, c=BLACK, m='tela', r=[8, 0, 0]),
    caja(0.06, 1.5, 0.06, x=0.55, y=0.8, z=0.1, c=DARK), caja(0.5, 0.1, 0.4, x=0.55, y=0.48, z=0.4, c=BLACK, m='tela'),
    caja(0.7, 0.04, 0.04, x=0.3, y=1.5, z=0.1, c=STEEL), cil(0.05, 0.05, 0.03, x=0.6, y=1.0, z=-0.1, c=GREYD, r=[0, 0, 90])],
    modificadores=['USE', 'SEAT'], asientos=[{'p': [0, 0.5, 0.3], 'h': 0.5, 'anim': 'banco'}], nota='cuatro puestos con una pila de pesas')
obj('prensa_piernas', 'Prensa de piernas', 'maquina_gimnasio', 180, 'metal', 'suelo', [
    caja(0.9, 0.05, 2.0, y=0.025, c=DARK), caja(0.06, 0.1, 1.4, x=-0.4, y=0.55, z=0.2, c=DARK, r=[-30, 0, 0]), caja(0.06, 0.1, 1.4, x=0.4, y=0.55, z=0.2, c=DARK, r=[-30, 0, 0]),
    caja(0.5, 0.1, 0.5, y=0.3, z=0.55, c=BLACK, m='tela'), caja(0.5, 0.5, 0.1, y=0.62, z=0.85, c=BLACK, m='tela', r=[40, 0, 0]),
    caja(0.7, 0.06, 0.7, y=0.75, z=-0.45, c=GREYD, r=[-40, 0, 0]), *[caja(0.1, 0.1, 0.5, x=sx * 0.3, y=0.9, z=-0.3, c=DARK) for sx in (-1, 1)],
    cil(0.1, 0.1, 0.06, x=-0.4, y=0.95, z=-0.6, c=DARK, r=[0, 0, 90]), cil(0.1, 0.1, 0.06, x=0.4, y=0.95, z=-0.6, c=DARK, r=[0, 0, 90])],
    modificadores=['USE', 'SEAT'], asientos=[{'p': [0, 0.35, 0.55], 'h': 0.35, 'anim': 'banco'}])
obj('polea_alta', 'Polea alta y remo', 'maquina_gimnasio', 150, 'metal', 'suelo', [
    caja(0.8, 0.05, 1.5, y=0.025, z=0.15, c=DARK), *torre(0, -0.45, 2.1), caja(0.06, 0.06, 0.9, y=2.1, z=-0.1, c=DARK), caja(0.06, 0.06, 0.06, y=2.0, z=0.3, c=DARK),
    caja(0.9, 0.03, 0.03, y=1.95, z=0.3, c=STEEL), caja(0.4, 0.1, 0.4, y=0.45, z=0.35, c=BLACK, m='tela'), caja(0.3, 0.1, 0.25, y=0.95, z=0.3, c=BLACK, m='tela'),
    caja(0.04, 0.5, 0.04, x=-0.15, y=0.7, z=0.3, c=DARK), caja(0.04, 0.5, 0.04, x=0.15, y=0.7, z=0.3, c=DARK)],
    modificadores=['USE', 'SEAT'], asientos=[{'p': [0, 0.5, 0.35], 'h': 0.5, 'anim': 'banco'}])
obj('pec_deck', 'Máquina de aperturas (pec deck)', 'maquina_gimnasio', 130, 'metal', 'suelo', [
    caja(0.9, 0.05, 1.3, y=0.025, z=0.1, c=DARK), *torre(0, -0.5, 1.6), caja(0.5, 0.1, 0.4, y=0.45, z=0.35, c=BLACK, m='tela'), caja(0.5, 0.8, 0.1, y=1.0, z=0.12, c=BLACK, m='tela', r=[8, 0, 0]),
    caja(0.07, 0.8, 0.07, x=-0.4, y=1.0, z=0.3, c=DARK), caja(0.07, 0.8, 0.07, x=0.4, y=1.0, z=0.3, c=DARK),
    caja(0.12, 0.5, 0.1, x=-0.4, y=1.1, z=0.55, c=BLACK, m='tela'), caja(0.12, 0.5, 0.1, x=0.4, y=1.1, z=0.55, c=BLACK, m='tela')],
    modificadores=['USE', 'SEAT'], asientos=[{'p': [0, 0.5, 0.35], 'h': 0.5, 'anim': 'banco'}])
obj('rack_sentadilla', 'Rack de sentadilla con barra', 'maquina_gimnasio', 95, 'metal', 'suelo', [
    *[caja(0.06, 2.2, 0.06, x=sx * 0.55, y=1.1, z=sz * 0.45, c=G_ORA if sz < 0 else DARK) for sx in (-1, 1) for sz in (-1, 1)],
    caja(1.16, 0.06, 0.06, y=2.2, z=-0.45, c=DARK), caja(0.06, 0.06, 0.96, x=-0.55, y=2.2, c=DARK), caja(0.06, 0.06, 0.96, x=0.55, y=2.2, c=DARK),
    caja(0.06, 0.06, 0.96, x=-0.55, y=0.5, c=DARK), caja(0.06, 0.06, 0.96, x=0.55, y=0.5, c=DARK),
    caja(0.14, 0.04, 0.08, x=-0.55, y=1.4, z=-0.45, c=STEEL), caja(0.14, 0.04, 0.08, x=0.55, y=1.4, z=-0.45, c=STEEL),
    cil(0.014, 0.014, 2.2, y=1.46, z=-0.45, c=STEEL, r=[0, 0, 90], seg=8), cil(0.11, 0.11, 0.05, x=-0.8, y=1.46, z=-0.45, c=G_RUB, m='goma', r=[0, 0, 90], seg=14), cil(0.11, 0.11, 0.05, x=0.8, y=1.46, z=-0.45, c=G_RUB, m='goma', r=[0, 0, 90], seg=14),
    cil(0.16, 0.16, 0.04, x=-0.86, y=1.46, z=-0.45, c='#2a56a0', m='goma', r=[0, 0, 90], seg=14), cil(0.16, 0.16, 0.04, x=0.86, y=1.46, z=-0.45, c='#2a56a0', m='goma', r=[0, 0, 90], seg=14),
    caja(0.9, 0.03, 0.9, y=0.015, z=0.0, c='#2a2c30', m='goma')], modificadores=['USE'], nota='con la barra cargada, lista para sentadillas')
obj('estructura_dominadas', 'Estructura de dominadas', 'maquina_gimnasio', 62, 'metal', 'suelo', [
    *[caja(0.07, 2.3, 0.07, x=sx * 0.55, y=1.15, z=-0.0, c=DARK) for sx in (-1, 1)], *[caja(0.07, 0.04, 0.8, x=sx * 0.55, y=0.02, z=0.0, c=DARK) for sx in (-1, 1)],
    cil(0.017, 0.017, 1.1, y=2.2, c=STEEL, r=[0, 0, 90]), cil(0.015, 0.015, 0.6, x=0.3, y=1.8, z=0.0, c=STEEL, r=[0, 0, 90]), cil(0.015, 0.015, 0.6, x=-0.3, y=1.4, z=0.0, c=STEEL, r=[0, 0, 90])],
    modificadores=['USE'])
obj('banco_plano', 'Banco plano de press', 'banco', 22, 'metal', 'suelo', [
    caja(0.3, 0.07, 1.2, y=0.435, c=BLACK, m='tela'), caja(0.07, 0.4, 0.5, y=0.2, z=0.0, c=GREYD), caja(0.5, 0.04, 0.07, y=0.02, z=-0.45, c=DARK), caja(0.5, 0.04, 0.07, y=0.02, z=0.45, c=DARK),
    caja(0.07, 0.4, 0.07, x=-0.15, y=0.2, z=-0.45, c=GREYD), caja(0.07, 0.4, 0.07, x=0.15, y=0.2, z=-0.45, c=GREYD)],
    modificadores=['SEAT'], asientos=[{'p': [0, 0.47, 0.2], 'h': 0.47, 'anim': 'banco'}])
obj('banco_inclinado', 'Banco inclinado', 'banco', 24, 'metal', 'suelo', [
    caja(0.3, 0.07, 0.7, y=0.7, z=-0.2, c=BLACK, m='tela', r=[-40, 0, 0]), caja(0.3, 0.07, 0.4, y=0.44, z=0.35, c=BLACK, m='tela'),
    caja(0.07, 0.6, 0.07, y=0.3, z=-0.3, c=GREYD), caja(0.07, 0.4, 0.07, y=0.2, z=0.35, c=GREYD), caja(0.5, 0.04, 0.07, y=0.02, z=-0.45, c=DARK), caja(0.5, 0.04, 0.07, y=0.02, z=0.45, c=DARK)],
    modificadores=['SEAT'], asientos=[{'p': [0, 0.475, 0.35], 'h': 0.475, 'anim': 'banco'}])
obj('banco_regulable', 'Banco regulable con respaldo', 'banco', 26, 'metal', 'suelo', [
    caja(0.3, 0.07, 0.8, y=0.62, z=-0.25, c='#3a3e44', m='tela', r=[-20, 0, 0]), caja(0.3, 0.07, 0.42, y=0.46, z=0.3, c='#3a3e44', m='tela'),
    caja(0.07, 0.5, 0.07, y=0.25, z=-0.3, c=G_ORA), caja(0.07, 0.42, 0.07, y=0.21, z=0.3, c=G_ORA), caja(0.5, 0.04, 0.07, y=0.02, z=-0.45, c=DARK), caja(0.5, 0.04, 0.07, y=0.02, z=0.45, c=DARK)],
    modificadores=['SEAT'], asientos=[{'p': [0, 0.495, 0.3], 'h': 0.495, 'anim': 'banco'}])
obj('banco_abdominales', 'Banco de abdominales', 'banco', 17, 'metal', 'suelo', [
    caja(0.32, 0.07, 1.1, y=0.48, z=0.0, c=BLACK, m='tela', r=[-14, 0, 0]), caja(0.06, 0.5, 0.06, y=0.3, z=-0.45, c=GREYD), caja(0.06, 0.3, 0.06, y=0.2, z=0.4, c=GREYD),
    caja(0.5, 0.04, 0.07, y=0.02, z=-0.45, c=DARK), caja(0.5, 0.04, 0.07, y=0.02, z=0.45, c=DARK), cil(0.04, 0.04, 0.25, x=-0.12, y=0.33, z=0.55, c=BLACK, m='goma', r=[0, 0, 90]), cil(0.04, 0.04, 0.25, x=0.12, y=0.33, z=0.55, c=BLACK, m='goma', r=[0, 0, 90])],
    modificadores=['SEAT'], asientos=[{'p': [0, 0.5, 0.0], 'h': 0.5, 'anim': 'banco'}])

# ---------------------------------------------------------------- racks: what stands on them is placed by the kit
def estante_rack(id, nombre, largo, tops, fondo, masa, c='#3a3e44', extra=None, cat='estanteria'):
    alto = tops[-1] + 0.04
    partes = [*[caja(0.05, alto, fondo + 0.04, x=sx * (largo / 2 + 0.025), c=DARK) for sx in (-1, 1)], *[caja(largo, 0.03, fondo + 0.04, y=t - 0.015, c=c) for t in tops]]
    obj(id, nombre, cat, masa, 'metal', 'suelo', partes, superficies=[{'y': t, 'fondo': fondo} for t in tops], **(extra or {}))
estante_rack('soporte_mancuernas', 'Soporte de mancuernas de dos pisos', 2.4, [0.45, 0.85], 0.36, 78)
estante_rack('soporte_kettlebells', 'Soporte de pesas rusas', 1.6, [0.28, 0.62], 0.36, 48)
estante_rack('soporte_balones', 'Soporte de balones medicinales', 1.2, [0.25, 0.55], 0.36, 30)
obj('arbol_discos', 'Árbol de discos', 'equipo_gimnasio', 62, 'metal', 'suelo', [
    caja(0.7, 0.04, 0.45, y=0.02, c=DARK), *[cil(0.025, 0.025, 1.1, x=sx * 0.17, y=0.58, c=STEEL, seg=8) for sx in (-1, 1)],
    *[cil(0.2 - 0.01 * k, 0.2 - 0.01 * k, 0.04, x=-0.17, y=0.07 + 0.045 * k, c=['#2a56a0', G_RUB, '#d8a82a', G_RUB, '#2e7a46', G_RUB][k % 6], m='goma', seg=14) for k in range(6)],
    *[cil(0.17 - 0.008 * k, 0.17 - 0.008 * k, 0.04, x=0.17, y=0.07 + 0.045 * k, c=[G_RUB, '#b8302a', G_RUB, '#d8a82a', G_RUB][k % 5], m='goma', seg=14) for k in range(5)]],
    nota='con los discos de pesas puestos en dos columnas')
obj('estante_suplementos', 'Expositor de suplementos', 'estanteria', 36, 'metal', 'suelo', [
    caja(0.04, 1.7, 0.36, x=-0.46, c='#3a3e44'), caja(0.04, 1.7, 0.36, x=0.46, c='#3a3e44'), caja(0.9, 1.66, 0.01, y=0.85, z=-0.175, c=G_ORA),
    *[caja(0.88, 0.03, 0.34, y=t - 0.015, c='#d8dcde') for t in (0.05, 0.45, 0.85, 1.25)], caja(0.96, 0.1, 0.04, y=1.7, z=0.0, c=G_ORA, m='plastico')],
    superficies=[{'y': t, 'fondo': 0.3} for t in (0.45, 0.85, 1.25)])

def disco(n, r, t, c):
    obj(f'disco_{str(n).replace(".", "_")}kg', f'Disco de {n} kg'.replace('.', ','), 'pesas', n, 'metal', 'suelo', [cil(r, r, t, c=c, m='goma', seg=16), cil(0.027, 0.027, t + 0.004, c=STEEL, seg=8)])
for n, r, t, c in ((1.25, 0.11, 0.02, '#c8ccd0'), (2.5, 0.14, 0.024, '#2e7a46'), (5, 0.17, 0.03, '#ece8dc'), (10, 0.2, 0.04, '#2e7a46'), (15, 0.22, 0.045, '#d8a82a'), (20, 0.225, 0.05, '#2a56a0')):
    disco(n, r, t, c)
def mancuerna(n):
    r, hl, mango = 0.04 + (n - 2) * 0.0016, 0.045 + n * 0.0014, 0.14
    col = '#d8641c' if n < 10 else '#c8ccd0' if n < 20 else '#d8a82a'
    obj(f'mancuerna_{n}kg', f'Mancuerna de {n} kg', 'pesas', n, 'metal', 'superficie', [
        cil(0.015, 0.015, mango + 0.02, y=r, c=STEEL, r=[0, 0, 90], seg=8),
        *[cil(r, r, hl, x=sx * (mango / 2 + hl / 2), y=r, c=G_RUB, m='goma', r=[0, 0, 90], seg=12) for sx in (-1, 1)],
        *[cil(r * 0.98, r * 0.98, 0.012, x=sx * (mango / 2 + 0.006), y=r, c=col, m='goma', r=[0, 0, 90], seg=12) for sx in (-1, 1)]])
for n in (2, 4, 6, 8, 10, 12, 14, 16, 20, 24, 28, 32, 36, 40): mancuerna(n)
def kettlebell(n, r, c):
    obj(f'pesa_rusa_{n}kg', f'Pesa rusa de {n} kg', 'pesas', n, 'metal', 'superficie', [
        esf(r, 0, r, 0, c=c, m='goma'), cil(r * 0.5, r * 0.6, 0.025, y=0.0125, c=c, m='goma', seg=10),
        caja(0.018, 0.075, 0.03, x=-r * 0.62, y=2 * r + 0.012, c=c, m='goma'), caja(0.018, 0.075, 0.03, x=r * 0.62, y=2 * r + 0.012, c=c, m='goma'), caja(r * 1.4, 0.022, 0.03, y=2 * r + 0.058, c=c, m='goma')])
for n, r, c in ((4, 0.055, '#e08aa8'), (8, 0.07, '#e8c42a'), (12, 0.08, '#2a56a0'), (16, 0.09, '#2e7a46'), (20, 0.095, '#7a3a9a'), (24, 0.1, '#b8302a')): kettlebell(n, r, c)
def balon(n, r, c):
    obj(f'balon_medicinal_{n}kg', f'Balón medicinal de {n} kg', 'pesas', n, 'goma', 'superficie', [esf(r, 0, r, 0, c=c, m='goma'), cil(r, r, 0.012, y=r, c=G_RUB, m='goma', seg=14)])
for n, r, c in ((3, 0.1, '#b8302a'), (5, 0.115, '#2a56a0'), (8, 0.13, '#2e7a46')): balon(n, r, c)
obj('barra_olimpica', 'Barra olímpica', 'pesas', 20, 'metal', 'suelo', [
    cil(0.014, 0.014, 2.2, y=0.025, c=STEEL, r=[0, 0, 90], seg=8), *[cil(0.025, 0.025, 0.4, x=sx * 0.9, y=0.025, c=STEEL, r=[0, 0, 90], seg=10) for sx in (-1, 1)]])
obj('barra_z', 'Barra Z de curl', 'pesas', 8, 'metal', 'suelo', [
    cil(0.014, 0.014, 1.2, y=0.025, c=STEEL, r=[0, 0, 90], seg=8), *[cil(0.025, 0.025, 0.2, x=sx * 0.5, y=0.025, c=STEEL, r=[0, 0, 90], seg=10) for sx in (-1, 1)]])

# ---------------------------------------------------------------- floor work, boxing and small gear
obj('colchoneta', 'Colchoneta de gimnasia', 'textil', 1.4, 'goma', 'suelo', [caja(0.6, 0.025, 1.8, c='#2a56a0', m='goma'), caja(0.6, 0.004, 0.02, y=0.027, z=0.5, c=WHITE, m='goma')])
obj('esterilla_yoga', 'Esterilla de yoga enrollada', 'textil', 1.1, 'goma', 'suelo', [cil(0.065, 0.065, 0.6, y=0.065, c='#7a3a9a', m='goma', r=[0, 0, 90]), caja(0.04, 0.02, 0.14, x=0.1, y=0.03, c=G_RUB, m='goma')])
obj('rodillo_espuma', 'Rodillo de espuma', 'equipo_gimnasio', 0.6, 'goma', 'suelo', [cil(0.075, 0.075, 0.33, y=0.075, c='#2e7a46', m='goma', r=[0, 0, 90])])
obj('pelota_pilates', 'Pelota de pilates', 'equipo_gimnasio', 1.2, 'goma', 'suelo', [esf(0.32, 0, 0.32, 0, c='#2a8a9a', m='goma')])
obj('media_pelota_equilibrio', 'Media pelota de equilibrio', 'equipo_gimnasio', 4.2, 'goma', 'suelo', [cil(0.3, 0.3, 0.03, y=0.015, c=G_RUB, m='goma', seg=16), cil(0.27, 0.3, 0.07, y=0.065, c='#2a56a0', m='goma', seg=16), cil(0.18, 0.27, 0.06, y=0.13, c='#2a56a0', m='goma', seg=16)])
obj('step_aerobic', 'Step de aeróbic', 'equipo_gimnasio', 3.8, 'plastico', 'suelo', [caja(0.9, 0.04, 0.35, y=0.14, c='#3a3e44', m='plastico'), caja(0.12, 0.12, 0.33, x=-0.38, y=0.06, c=G_ORA, m='plastico'), caja(0.12, 0.12, 0.33, x=0.38, y=0.06, c=G_ORA, m='plastico')])
obj('comba', 'Comba de saltar', 'equipo_gimnasio', 0.25, 'goma', 'suelo', [cil(0.09, 0.09, 0.02, c=RED, m='goma', seg=14), cil(0.025, 0.025, 0.12, x=-0.12, y=0.06, c=BLACK, m='goma', r=[0, 0, 90], seg=8)])
obj('gomas_elasticas', 'Gomas elásticas', 'equipo_gimnasio', 0.3, 'goma', 'suelo', [cil(0.07, 0.07, 0.03, c='#d8641c', m='goma', seg=12), cil(0.065, 0.065, 0.03, y=0.03, c='#2e7a46', m='goma', seg=12), cil(0.06, 0.06, 0.03, y=0.06, c='#2a56a0', m='goma', seg=12)])
obj('guantes_boxeo', 'Guantes de boxeo', 'equipo_gimnasio', 0.9, 'tela', 'suelo', [esf(0.075, -0.07, 0.06, 0, c=RED, m='tela', s=[1, 0.8, 1.35]), esf(0.075, 0.07, 0.06, 0.02, c=RED, m='tela', s=[1, 0.8, 1.35]), caja(0.06, 0.05, 0.07, x=-0.07, y=0.04, z=-0.1, c=G_RUB, m='tela'), caja(0.06, 0.05, 0.07, x=0.07, y=0.04, z=-0.08, c=G_RUB, m='tela')])
obj('saco_boxeo', 'Saco de boxeo colgado', 'equipo_gimnasio', 38, 'tela', 'techo', [
    cil(0.007, 0.007, 1.75, y=-0.875, c=STEEL), cil(0.04, 0.04, 0.04, y=-0.04, c=DARK), caja(0.05, 0.06, 0.05, y=-1.78, c=STEEL, m='metal'),
    cil(0.17, 0.17, 1.2, y=-2.35, c='#b8302a', m='goma'), cil(0.171, 0.171, 0.08, y=-1.95, c=G_RUB, m='goma'), cil(0.171, 0.171, 0.08, y=-2.75, c=G_RUB, m='goma')],
    fijo='anclado en la realidad', nota='para un techo de 3,4 m: el saco queda a unos 45 cm del suelo')
obj('pera_boxeo', 'Pera de velocidad', 'equipo_gimnasio', 2.5, 'tela', 'suelo', [
    caja(0.4, 0.04, 0.4, y=0.02, c=G_RUB, m='goma'), cil(0.02, 0.02, 1.1, y=0.6, c=STEEL), caja(0.5, 0.03, 0.4, y=1.2, c=WOOD_D),
    esf(0.07, 0, 0.9, 0.08, c=RED, m='goma', s=[1, 1.3, 1])])
obj('toalla_doblada', 'Toalla doblada', 'textil', 0.4, 'tela', 'superficie', [caja(0.34, 0.05, 0.22, c='#f1efe9', m='tela'), caja(0.34, 0.012, 0.05, y=0.031, z=0.06, c='#2a56a0', m='tela')])
obj('bolsa_deporte', 'Bolsa de deporte', 'equipo_gimnasio', 3.5, 'tela', 'suelo', [caja(0.55, 0.26, 0.26, c='#2a2c30', m='tela'), caja(0.5, 0.02, 0.24, y=0.27, c=G_ORA, m='tela'), caja(0.3, 0.14, 0.01, y=0.14, z=0.135, c=G_ORA, m='tela')])
obj('bidon_agua', 'Bidón de agua deportivo', 'equipo_gimnasio', 0.7, 'plastico', 'superficie', [cil(0.035, 0.032, 0.2, c='#8fc4de', m='cristal', seg=10), cil(0.025, 0.025, 0.04, y=0.22, c=G_ORA, m='plastico', seg=10)])
obj('bascula_gimnasio', 'Báscula', 'equipo_gimnasio', 3.2, 'cristal', 'suelo', [caja(0.32, 0.03, 0.32, c='#cfd6da', m='cristal'), caja(0.12, 0.004, 0.05, y=0.032, z=-0.1, c='#2a3a2a', m='plastico')])
for k, n, c in (('choco', 'chocolate', '#5a3a24'), ('vainilla', 'vainilla', '#e8d9a8'), ('fresa', 'fresa', '#d86a8a')):
    obj(f'bote_proteina_{k}', f'Bote de proteínas de {n}', 'alimento', 1.2, 'plastico', 'superficie', [cil(0.065, 0.065, 0.2, c=c, m='plastico', seg=12), cil(0.068, 0.068, 0.03, y=0.215, c=G_RUB, m='plastico', seg=12), cil(0.066, 0.066, 0.1, y=0.1, c=WHITE, m='papel', seg=12)])
obj('mostrador_gimnasio_modulo', 'Módulo de mostrador de recepción (1,2 m)', 'mostrador', 420, 'madera', 'suelo', [
    caja(1.2, 1.04, 0.1, y=0.52, z=0.3, c=G_ORA), caja(1.2, 0.04, 0.42, y=1.06, z=0.19, c='#d9d3c6'), caja(1.2, 1.04, 0.02, y=0.52, z=0.0, c='#3a3e44'),
    caja(1.2, 0.03, 0.5, y=0.735, z=-0.27, c='#d9d3c6'), caja(0.03, 0.72, 0.5, x=-0.585, y=0.36, z=-0.27, c='#3a3e44'), caja(0.03, 0.72, 0.5, x=0.585, y=0.36, z=-0.27, c='#3a3e44'),
    caja(1.2, 0.5, 0.02, y=0.5, z=-0.52, c='#3a3e44'),
    caja(0.04, 0.14, 0.03, x=-0.25, y=0.84, z=-0.28, c=DARK, m='plastico'), caja(0.46, 0.28, 0.03, x=-0.25, y=1.0, z=-0.28, c=DARK, m='plastico'),
    caja(0.42, 0.24, 0.006, x=-0.25, y=1.0, z=-0.298, c='#18222e', m='plastico'), caja(0.42, 0.015, 0.15, x=-0.25, y=0.7625, z=-0.4, c=DARK, m='plastico')],
    superficies=[{'y': 1.08, 'margen': 0.05}], fijo='estructural', nota='la recepción del gimnasio: lo de cara al público es el voladizo de 1,08 m')
# lockers, showers, mirrors and the rest of the changing room
def taquilla(id, nombre, ancho, alto, masa, c, puertas):
    partes = [caja(ancho, alto, 0.45, c=c, m='metal')]
    for k in range(puertas):
        x = -ancho / 2 + ancho / puertas * (k + 0.5)
        partes += [caja(ancho / puertas - 0.02, alto - 0.06, 0.012, x=x, y=alto / 2, z=0.231, c=c, m='metal'), caja(0.04, 0.012, 0.012, x=x, y=alto * 0.7, z=0.24, c=WHITE, m='plastico'), caja(0.03, 0.06, 0.012, x=x, y=alto * 0.55, z=0.24, c=STEEL, m='metal')]
    obj(id, nombre, 'mueble', masa, 'metal', 'suelo', partes, superficies=[{'y': alto, 'margen': 0.03}])
taquilla('taquilla_metalica', 'Taquilla metálica', 0.3, 1.8, 22, '#5a7a9a', 1)
taquilla('taquilla_doble', 'Taquilla doble', 0.6, 1.8, 40, '#8e949a', 2)
taquilla('taquilla_media', 'Taquilla baja', 0.6, 0.9, 26, G_ORA, 2)
obj('banco_vestuario', 'Banco de vestuario', 'banco', 21, 'madera', 'suelo', [
    *[caja(0.17, 0.04, 0.36, x=-0.57 + 0.38 * k, y=0.43, c='#c8a878') for k in range(4)], caja(0.05, 0.41, 0.34, x=-0.65, y=0.205, c=GREYD, m='metal'), caja(0.05, 0.41, 0.34, x=0.65, y=0.205, c=GREYD, m='metal'),
    caja(1.3, 0.03, 0.04, y=0.2, z=0.0, c=GREYD, m='metal')],
    modificadores=['SEAT'], asientos=[{'p': [k * 0.45, 0.45, 0.0], 'h': 0.45, 'anim': 'banco'} for k in (-1, 0, 1)], superficies=[{'y': 0.45, 'margen': 0.03}])
obj('ducha_cabina', 'Cabina de ducha', 'sanitario', 45, 'ceramica', 'suelo', [
    caja(0.9, 0.08, 0.9, y=0.04, c=WHITE, m='ceramica'), caja(0.03, 2.0, 0.9, x=-0.435, y=1.0, c='#cfd8dc', m='ceramica'), caja(0.03, 2.0, 0.9, x=0.435, y=1.0, c='#cfd8dc', m='ceramica'),
    caja(0.84, 1.7, 0.01, y=1.0, z=0.44, c='#a8d0e0', m='cristal'), cil(0.01, 0.01, 0.9, x=0.28, y=1.5, z=-0.42, c=STEEL), cil(0.08, 0.08, 0.02, x=0.28, y=2.0, z=-0.3, c=STEEL, r=[30, 0, 0], seg=12),
    caja(0.12, 0.12, 0.05, x=0.28, y=1.1, z=-0.43, c=STEEL, m='metal'), cil(0.04, 0.04, 0.008, y=0.084, z=0.0, c=STEEL)],
    fijo='anclado en la realidad', modificadores=['USE'], nota='cabina con plato, mampara de cristal y mezclador')
obj('ducha_abierta', 'Ducha de pared', 'limpieza', 3.5, 'metal', 'pared', [
    cil(0.012, 0.012, 1.2, y=1.4, z=0.04, c=STEEL), cil(0.09, 0.09, 0.02, y=2.0, z=0.18, c=STEEL, r=[70, 0, 0], seg=12), cil(0.01, 0.01, 0.18, y=1.98, z=0.1, c=STEEL, r=[90, 0, 0]),
    caja(0.14, 0.14, 0.06, y=1.1, z=0.03, c=STEEL, m='metal'), caja(0.04, 0.03, 0.06, x=-0.04, y=1.1, z=0.08, c=RED, m='plastico'), caja(0.04, 0.03, 0.06, x=0.04, y=1.1, z=0.08, c='#2a56a0', m='plastico')],
    fijo='anclado en la realidad', modificadores=['USE'])
obj('secador_pelo_pared', 'Secador de pelo de pared', 'limpieza', 1.5, 'plastico', 'pared', [
    caja(0.2, 0.16, 0.1, y=1.5, z=0.05, c=WHITE, m='plastico'), cil(0.04, 0.05, 0.14, y=1.42, z=0.15, c=WHITE, m='plastico', r=[90, 0, 0], seg=10), caja(0.06, 0.1, 0.05, y=1.32, z=0.12, c=WHITE, m='plastico')],
    fijo='anclado en la realidad', modificadores=['USE'])
obj('espejo_gimnasio_grande', 'Espejo grande de pared', 'espejo', 14.5, 'cristal', 'pared', [caja(2.0, 1.3, 0.02, y=1.65, z=0.01, c='#b5c6cf', m='cristal'), caja(2.04, 0.03, 0.03, y=1.0, z=0.015, c=STEEL, m='metal'), caja(2.04, 0.03, 0.03, y=2.3, z=0.015, c=STEEL, m='metal')], fijo='anclado en la realidad')
obj('espejo_gimnasio_alto', 'Espejo alto', 'espejo', 9, 'cristal', 'pared', [caja(0.9, 1.7, 0.02, y=1.25, z=0.01, c='#b5c6cf', m='cristal'), caja(0.94, 0.03, 0.03, y=0.4, z=0.015, c=STEEL, m='metal'), caja(0.94, 0.03, 0.03, y=2.1, z=0.015, c=STEEL, m='metal')], fijo='anclado en la realidad')
obj('fuente_agua', 'Fuente de agua', 'electrodomestico', 18, 'metal', 'pared', [
    caja(0.4, 0.14, 0.38, y=0.95, z=0.19, c=STEEL, m='metal'), caja(0.32, 0.02, 0.3, y=1.03, z=0.2, c='#9aa0a6', m='metal'), cil(0.012, 0.012, 0.12, y=1.1, z=0.08, c=STEEL), caja(0.34, 0.8, 0.1, y=0.4, z=0.05, c='#e2e6e8', m='metal')],
    fijo='anclado en la realidad', modificadores=['USE'])
obj('ventilador_pie', 'Ventilador industrial de pie', 'electrodomestico', 15.5, 'metal', 'suelo', [
    cil(0.22, 0.25, 0.04, c=DARK, seg=14), cil(0.03, 0.03, 1.15, y=0.62, c=GREYD, seg=8), cil(0.26, 0.26, 0.1, y=1.3, z=0.05, c=DARK, r=[90, 0, 0], seg=16), cil(0.24, 0.24, 0.02, y=1.3, z=0.115, c='#c8ccd0', m='metal', r=[90, 0, 0], seg=16)])
obj('tv_gimnasio', 'Televisor de pared', 'pantalla', 12, 'plastico', 'pared', [caja(1.1, 0.65, 0.05, y=2.3, z=0.075, c=BLACK, m='plastico'), caja(1.04, 0.59, 0.004, y=2.3, z=0.1, c='#1a2028', m='plastico'), caja(0.2, 0.2, 0.05, y=2.3, z=0.025, c=GREYD, m='metal')], fijo='anclado en la realidad')
obj('altavoz_pared', 'Altavoz de pared', 'informatica', 3.2, 'plastico', 'pared', [caja(0.22, 0.34, 0.18, y=2.55, z=0.09, c=BLACK, m='plastico'), cil(0.07, 0.07, 0.02, y=2.47, z=0.185, c='#3a3e44', m='plastico', r=[90, 0, 0], seg=12), cil(0.035, 0.035, 0.02, y=2.63, z=0.185, c='#3a3e44', m='plastico', r=[90, 0, 0], seg=10)], fijo='anclado en la realidad')
obj('dispensador_toallas', 'Dispensador de toallas', 'limpieza', 3, 'plastico', 'pared', [caja(0.3, 0.35, 0.15, y=1.3, z=0.075, c=WHITE, m='plastico'), caja(0.24, 0.16, 0.012, y=1.12, z=0.156, c='#cfd6da', m='plastico'), caja(0.2, 0.3, 0.012, y=0.9, z=0.07, c='#2a56a0', m='tela')], fijo='anclado en la realidad', modificadores=['USE'])
obj('perchero_pared', 'Barra de colgar con perchas', 'decoracion', 1.5, 'madera', 'pared', [caja(0.9, 0.06, 0.03, y=1.7, z=0.015, c=WOOD), *[cil(0.008, 0.008, 0.07, x=-0.36 + 0.18 * k, y=1.71, z=0.065, c=STEEL, r=[90, 0, 0], seg=6) for k in range(5)]])
# posters (painted pictures: src/texturas/servicios.js)
obj('cartel_tarifas', 'Cartel de tarifas', 'cuadro', 1.0, 'papel', 'pared', [caja(0.62, 0.9, 0.02, y=1.6, z=0.01, c=G_ORA), plano(0.56, 0.84, y=1.6, z=0.021, tex={'tipo': 'cartel_tarifas'})])
obj('cartel_clases', 'Horario de clases dirigidas', 'cuadro', 1.0, 'papel', 'pared', [caja(0.8, 0.6, 0.02, y=1.7, z=0.01, c=G_RUB), plano(0.76, 0.56, y=1.7, z=0.021, tex={'tipo': 'cartel_clases'})])
obj('cartel_sentadilla', 'Cartel de la sentadilla', 'cuadro', 1.0, 'papel', 'pared', [caja(0.52, 0.72, 0.02, y=1.7, z=0.01, c=G_RUB), plano(0.48, 0.68, y=1.7, z=0.021, tex={'tipo': 'cartel_ejercicio', 'ejercicio': 'sentadilla'})])
obj('cartel_press', 'Cartel del press de banca', 'cuadro', 1.0, 'papel', 'pared', [caja(0.52, 0.72, 0.02, y=1.7, z=0.01, c=G_RUB), plano(0.48, 0.68, y=1.7, z=0.021, tex={'tipo': 'cartel_ejercicio', 'ejercicio': 'press'})])
obj('cartel_normas_gimnasio', 'Normas del gimnasio', 'cuadro', 0.6, 'papel', 'pared', [caja(0.42, 0.58, 0.015, y=1.6, z=0.0075, c='#2a2a2e'), plano(0.38, 0.54, y=1.6, z=0.016, tex={'tipo': 'cartel_normas'})])

# ================================================================ the «casa de comidas»
CLOTH = '#f4f0e6'
def mesa_mantel(id, nombre, w, d, masa, c, cuadros=False, redonda=False):
    if redonda:
        partes = [cil(w / 2, w / 2, 0.016, y=0.758, c=c, m='tela', seg=24), cil(w / 2 + 0.005, w / 2 + 0.005, 0.24, y=0.65, c=c, m='tela', seg=24), cil(0.04, 0.04, 0.53, y=0.265, c=WOOD_D, m='madera'), cil(0.25, 0.27, 0.03, y=0.015, c=WOOD_D, m='madera', seg=16)]
    else:
        partes = [caja(w, 0.016, d, y=0.758, c=c, m='tela'), caja(w, 0.24, 0.012, y=0.65, z=d / 2 - 0.006, c=c, m='tela'), caja(w, 0.24, 0.012, y=0.65, z=-d / 2 + 0.006, c=c, m='tela'),
                  caja(0.012, 0.24, d, x=w / 2 - 0.006, y=0.65, c=c, m='tela'), caja(0.012, 0.24, d, x=-w / 2 + 0.006, y=0.65, c=c, m='tela'),
                  *[caja(0.06, 0.53, 0.06, x=sx * (w / 2 - 0.1), y=0.265, z=sz * (d / 2 - 0.1), c=WOOD_D) for sx in (-1, 1) for sz in (-1, 1)]]
        if cuadros:
            partes += [caja(w, 0.002, 0.06, y=0.767, z=zz, c='#b5342c', m='tela') for zz in (-0.3, -0.15, 0, 0.15, 0.3) if abs(zz) < d / 2 - 0.05]
            partes += [caja(0.06, 0.002, d, x=xx, y=0.767, c='#b5342c', m='tela') for xx in (-0.5, -0.25, 0, 0.25, 0.5) if abs(xx) < w / 2 - 0.05]
    obj(id, nombre, 'mesa', masa, 'madera', 'suelo', partes, superficies=[{'y': 0.766, 'margen': 0.06 if not redonda else 0.03}])
mesa_mantel('mesa_mantel_blanca', 'Mesa de comedor con mantel blanco', 1.2, 0.8, 34, CLOTH)
mesa_mantel('mesa_mantel_cuadros', 'Mesa de comedor con mantel de cuadros', 1.2, 0.8, 34, '#f0e4cc', cuadros=True)
mesa_mantel('mesa_cuadrada_mantel', 'Mesa cuadrada con mantel', 0.8, 0.8, 26, '#e8dcc0')
mesa_mantel('mesa_redonda_mantel', 'Mesa redonda con mantel', 1.1, 1.1, 30, CLOTH, redonda=True)
obj('silla_anea', 'Silla de anea', 'silla', 4.8, 'madera', 'suelo', [
    caja(0.42, 0.04, 0.4, y=0.45, c='#c8aa5a', m='tela'), caja(0.04, 0.98, 0.04, x=-0.18, y=0.49, z=-0.19, c=WOOD_D), caja(0.04, 0.98, 0.04, x=0.18, y=0.49, z=-0.19, c=WOOD_D),
    caja(0.04, 0.43, 0.04, x=-0.18, y=0.215, z=0.18, c=WOOD_D), caja(0.04, 0.43, 0.04, x=0.18, y=0.215, z=0.18, c=WOOD_D),
    caja(0.32, 0.06, 0.02, y=0.92, z=-0.19, c=WOOD), caja(0.32, 0.05, 0.02, y=0.76, z=-0.19, c=WOOD), caja(0.32, 0.03, 0.03, y=0.2, z=0.18, c=WOOD_D), caja(0.32, 0.03, 0.03, y=0.2, z=-0.19, c=WOOD_D)],
    modificadores=['SEAT'], asientos=[{'p': [0, 0.47, 0.02], 'h': 0.47, 'anim': 'silla'}], nota='la de toda la vida: de madera con el asiento de anea')
obj('silla_comedor_tapizada', 'Silla de comedor tapizada', 'silla', 6.5, 'madera', 'suelo', [
    caja(0.44, 0.07, 0.44, y=0.47, c='#7a2a30', m='tela'), caja(0.04, 0.95, 0.04, x=-0.19, y=0.475, z=-0.2, c=WOOD_D), caja(0.04, 0.95, 0.04, x=0.19, y=0.475, z=-0.2, c=WOOD_D),
    caja(0.04, 0.43, 0.04, x=-0.19, y=0.215, z=0.19, c=WOOD_D), caja(0.04, 0.43, 0.04, x=0.19, y=0.215, z=0.19, c=WOOD_D), caja(0.4, 0.34, 0.05, y=0.78, z=-0.2, c='#7a2a30', m='tela')],
    modificadores=['SEAT'], asientos=[{'p': [0, 0.505, 0.02], 'h': 0.505, 'anim': 'silla'}])
obj('aparador_comedor', 'Aparador del comedor', 'mueble', 70, 'madera', 'suelo', [
    caja(1.4, 0.82, 0.45, c='#6a4228'), caja(1.44, 0.04, 0.48, y=0.84, z=0.015, c='#7a5234'), *[caja(0.44, 0.7, 0.012, x=-0.46 + 0.46 * k, y=0.42, z=0.231, c='#5a3820') for k in range(3)],
    *[caja(0.02, 0.1, 0.02, x=-0.3 + 0.46 * k, y=0.5, z=0.245, c=GOLD, m='metal') for k in range(3)]], superficies=[{'y': 0.86, 'margen': 0.05}])
obj('cubiertos_servicio', 'Cubiertos puestos', 'cubiertos', 0.15, 'metal', 'superficie', [
    caja(0.012, 0.003, 0.19, x=-0.05, y=0.0015, c=STEEL, m='metal'), caja(0.012, 0.003, 0.2, x=0.05, y=0.0015, c=STEEL, m='metal'), caja(0.02, 0.003, 0.17, x=0.08, y=0.0015, c=STEEL, m='metal')])
obj('servilleta_doblada', 'Servilleta doblada', 'papel', 0.02, 'papel', 'superficie', [caja(0.15, 0.01, 0.15, c='#f4f0e6', m='tela')])
obj('plato_hondo', 'Plato hondo con caldo', 'vajilla', 0.45, 'ceramica', 'superficie', [cil(0.1, 0.065, 0.04, c=WHITE, m='ceramica', seg=20), cil(0.085, 0.085, 0.004, y=0.034, c='#d8a850', m='comida', seg=16)])
obj('plato_postre', 'Plato de flan', 'vajilla', 0.3, 'ceramica', 'superficie', [cil(0.085, 0.075, 0.012, c=WHITE, m='ceramica', seg=18), cil(0.04, 0.045, 0.04, y=0.032, c='#e0a844', m='comida', seg=12), cil(0.04, 0.04, 0.004, y=0.054, c='#7a3a14', m='comida', seg=12)])
obj('cesta_pan', 'Cesta de pan', 'alimento', 0.6, 'tela', 'superficie', [
    cil(0.13, 0.1, 0.07, c='#b88a58', m='tela', seg=12), esf(0.06, -0.04, 0.075, 0.01, c='#c8924a', m='comida', s=[1.5, 0.7, 0.9]), esf(0.055, 0.045, 0.073, -0.02, c='#d3a05a', m='comida', s=[1.4, 0.7, 0.9]), cil(0.12, 0.12, 0.01, y=0.04, c='#f4f0e6', m='tela', seg=12)])
obj('jarra_agua', 'Jarra de agua', 'vajilla', 0.9, 'cristal', 'superficie', [cil(0.05, 0.045, 0.18, c='#bcd6dc', m='cristal', seg=12), caja(0.015, 0.1, 0.03, x=0.065, y=0.09, c='#bcd6dc', m='cristal'), cil(0.045, 0.045, 0.012, y=0.185, c='#d8dcd0', m='cristal', seg=12)])
obj('salero_pimentero', 'Salero y pimentero', 'vajilla', 0.2, 'cristal', 'superficie', [cil(0.018, 0.022, 0.07, x=-0.03, c='#e8eef0', m='cristal', seg=8), cil(0.018, 0.022, 0.07, x=0.03, c='#4a3a30', m='cristal', seg=8), cil(0.014, 0.018, 0.015, x=-0.03, y=0.077, c=STEEL, seg=8), cil(0.014, 0.018, 0.015, x=0.03, y=0.077, c=STEEL, seg=8)])
obj('aceitera_vinagrera', 'Aceitera y vinagrera', 'vajilla', 0.5, 'cristal', 'superficie', [
    caja(0.18, 0.01, 0.09, c=STEEL, m='metal'), cil(0.025, 0.03, 0.13, x=-0.045, y=0.075, c='#8a9a3a', m='cristal', seg=10), cil(0.025, 0.03, 0.13, x=0.045, y=0.075, c='#7a2a24', m='cristal', seg=10),
    cil(0.008, 0.008, 0.04, x=-0.045, y=0.16, c=STEEL, seg=6), cil(0.008, 0.008, 0.04, x=0.045, y=0.16, c=STEEL, seg=6)])
obj('florero_mesa', 'Florero con flores', 'decoracion', 0.8, 'cristal', 'superficie', [
    cil(0.035, 0.03, 0.14, c=GLASS, m='cristal', seg=10), cil(0.004, 0.004, 0.12, x=-0.012, y=0.2, c='#4a7a3a', m='madera', seg=5), cil(0.004, 0.004, 0.14, x=0.014, y=0.21, c='#4a7a3a', m='madera', seg=5),
    esf(0.026, -0.016, 0.27, 0, c='#e8c42a'), esf(0.026, 0.02, 0.29, 0.01, c='#d8506a'), esf(0.022, 0.0, 0.3, -0.02, c=WHITE)])
obj('pizarra_menu_pared', 'Pizarra del menú del día', 'decoracion', 4, 'madera', 'pared', [
    caja(0.84, 1.04, 0.03, y=1.65, z=0.015, c=WOOD_D), plano(0.78, 0.98, y=1.65, z=0.031, tex={'tipo': 'pizarra_menu'})])
obj('rotulo_restaurante', 'Rótulo de la casa de comidas', 'decoracion', 6, 'madera', 'pared', [
    caja(1.7, 0.42, 0.05, y=2.4, z=0.025, c='#3a2418'), plano(1.62, 0.34, y=2.4, z=0.0515, tex={'tipo': 'rotulo_restaurante', 'rotulo_local': True})], fijo='anclado en la realidad')
obj('caballete_menu', 'Caballete con el menú del día', 'decoracion', 4.5, 'madera', 'suelo', [
    caja(0.6, 0.9, 0.025, y=0.449, z=0.08, c='#3a2418', r=[-10, 0, 0]), caja(0.6, 0.9, 0.025, y=0.449, z=-0.08, c='#3a2418', r=[10, 0, 0]),
    plano(0.54, 0.84, y=0.449, z=0.0935, tex={'tipo': 'pizarra_menu'}, r=[-10, 0, 0]), caja(0.04, 0.04, 0.04, y=0.9, c='#3a2418')],
    nota='el menú del día en la acera, junto a la puerta')
obj('lampara_aplique', 'Aplique de pared', 'lampara', 1.2, 'metal', 'pared', [
    caja(0.1, 0.16, 0.03, y=1.95, z=0.015, c='#3a2418', m='madera'), caja(0.03, 0.03, 0.12, y=1.95, z=0.09, c=GOLD, m='metal'), cil(0.07, 0.04, 0.12, y=2.05, z=0.16, c='#f2e2b0', m='cristal', seg=10), esf(0.025, 0, 2.0, 0.16, c='#fff3d6', m='cristal', luz=True)],
    fijo='anclado en la realidad')
# the kitchen
obj('cocina_fuegos', 'Cocina de seis fuegos con horno', 'electrodomestico', 110, 'metal', 'suelo', [
    caja(0.9, 0.85, 0.8, c=STEEL), caja(0.9, 0.02, 0.8, y=0.86, c='#a8aeb2'), caja(0.9, 0.22, 0.05, y=0.99, z=-0.375, c=STEEL),
    *[cil(0.085, 0.085, 0.02, x=-0.28 + 0.28 * (k % 3), y=0.88, z=-0.17 + 0.34 * (k // 3), c=DARK, seg=10) for k in range(6)],
    caja(0.78, 0.5, 0.02, y=0.38, z=0.41, c=DARK), caja(0.7, 0.025, 0.04, y=0.66, z=0.44, c=STEEL), *[cil(0.018, 0.018, 0.03, x=-0.3 + 0.12 * k, y=0.77, z=0.41, c=BLACK, m='plastico', r=[90, 0, 0], seg=8) for k in range(6)]],
    fijo='anclado en la realidad', superficies=[{'y': 0.87, 'margen': 0.08}], modificadores=['USE'], nota='con gas de la calle y su horno')
obj('campana_extractora', 'Campana extractora', 'electrodomestico', 25, 'metal', 'pared', [
    caja(0.9, 0.14, 0.62, y=2.0, z=0.31, c=STEEL), caja(0.34, 0.9, 0.34, y=2.69, z=0.17, c=STEEL), caja(0.84, 0.04, 0.5, y=1.93, z=0.31, c='#8a9096', m='metal')], fijo='anclado en la realidad')
obj('mesa_acero', 'Mesa de trabajo de acero', 'mueble', 40, 'metal', 'suelo', [
    caja(1.5, 0.04, 0.7, y=0.88, c=STEEL), *[caja(0.05, 0.86, 0.05, x=sx * 0.7, y=0.43, z=sz * 0.3, c='#a8aeb2') for sx in (-1, 1) for sz in (-1, 1)], caja(1.4, 0.02, 0.6, y=0.2, c='#a8aeb2')],
    superficies=[{'y': 0.9, 'margen': 0.05}])
obj('fregadero_acero', 'Fregadero de acero de dos senos', 'sanitario', 45, 'metal', 'suelo', [
    caja(1.4, 0.04, 0.65, y=0.88, c=STEEL), caja(0.55, 0.03, 0.45, x=-0.3, y=0.84, c='#8a9096'), caja(0.55, 0.03, 0.45, x=0.3, y=0.84, c='#8a9096'),
    *[caja(0.05, 0.86, 0.05, x=sx * 0.65, y=0.43, z=sz * 0.28, c='#a8aeb2') for sx in (-1, 1) for sz in (-1, 1)], cil(0.015, 0.015, 0.3, y=1.05, z=-0.25, c=STEEL), cil(0.012, 0.012, 0.2, y=1.2, z=-0.15, c=STEEL, r=[90, 0, 0]), caja(1.4, 0.12, 0.03, y=0.96, z=-0.31, c=STEEL)],
    fijo='anclado en la realidad', modificadores=['USE'])
obj('nevera_industrial', 'Nevera industrial de acero', 'nevera', 150, 'metal', 'suelo', [
    caja(0.75, 2.0, 0.8, c=STEEL), caja(0.7, 0.9, 0.02, y=1.4, z=0.41, c='#a8aeb2'), caja(0.7, 0.9, 0.02, y=0.5, z=0.41, c='#a8aeb2'), caja(0.03, 0.4, 0.03, x=0.3, y=1.4, z=0.43, c=DARK, m='plastico'), caja(0.03, 0.4, 0.03, x=0.3, y=0.5, z=0.43, c=DARK, m='plastico')],
    modificadores=['USE'])
obj('arcon_congelador', 'Arcón congelador', 'nevera', 60, 'metal', 'suelo', [caja(1.0, 0.85, 0.65, c=WHITE, m='metal'), caja(1.04, 0.03, 0.69, y=0.865, c='#d8dcde', m='metal'), caja(0.2, 0.04, 0.03, y=0.9, z=0.3, c=DARK, m='plastico')],
    superficies=[{'y': 0.88, 'margen': 0.05}], modificadores=['USE'])
obj('freidora', 'Freidora de dos cubas', 'maquina_hosteleria', 18, 'metal', 'superficie', [
    caja(0.4, 0.3, 0.5, c=STEEL), caja(0.18, 0.02, 0.2, x=-0.09, y=0.31, z=0.0, c=DARK), caja(0.18, 0.02, 0.2, x=0.09, y=0.31, z=0.0, c=DARK), caja(0.03, 0.03, 0.18, x=-0.09, y=0.33, z=0.3, c=BLACK, m='plastico'), caja(0.03, 0.03, 0.18, x=0.09, y=0.33, z=0.3, c=BLACK, m='plastico')], modificadores=['USE'])
obj('plancha_cocina', 'Plancha de cocina', 'maquina_hosteleria', 30, 'metal', 'superficie', [caja(0.6, 0.15, 0.5, c=STEEL), caja(0.58, 0.012, 0.46, y=0.156, c='#3a3e44'), caja(0.5, 0.03, 0.03, y=0.07, z=0.26, c=DARK, m='plastico')], modificadores=['USE'])
obj('olla_grande', 'Olla grande', 'menaje_cocina', 3, 'metal', 'superficie', [cil(0.17, 0.17, 0.25, c=STEEL, seg=12), cil(0.175, 0.175, 0.02, y=0.26, c='#a8aeb2', seg=12), caja(0.07, 0.03, 0.02, x=-0.2, y=0.18, c=DARK, m='plastico'), caja(0.07, 0.03, 0.02, x=0.2, y=0.18, c=DARK, m='plastico'), cil(0.015, 0.015, 0.03, y=0.285, c=DARK, m='plastico', seg=6)])
obj('cazuela_barro', 'Cazuela de barro', 'menaje_cocina', 2.2, 'ceramica', 'superficie', [cil(0.15, 0.12, 0.09, c='#b5693a', m='ceramica', seg=12), caja(0.06, 0.03, 0.02, x=-0.17, y=0.07, c='#b5693a', m='ceramica'), caja(0.06, 0.03, 0.02, x=0.17, y=0.07, c='#b5693a', m='ceramica'), cil(0.13, 0.13, 0.005, y=0.092, c='#7a3a14', m='comida', seg=12)])
obj('sarten_grande', 'Sartén grande', 'menaje_cocina', 1.4, 'metal', 'superficie', [cil(0.14, 0.12, 0.045, c=DARK, seg=14), caja(0.22, 0.02, 0.03, x=0.24, y=0.035, c=DARK, m='plastico')])
obj('cacerola', 'Cacerola con mango', 'menaje_cocina', 1.1, 'metal', 'superficie', [cil(0.09, 0.09, 0.1, c=STEEL, seg=12), caja(0.16, 0.02, 0.03, x=0.17, y=0.08, c=DARK, m='plastico')])
obj('tabla_cortar', 'Tabla de cortar', 'menaje_cocina', 0.9, 'madera', 'superficie', [caja(0.4, 0.02, 0.28, c='#c8a878'), caja(0.14, 0.012, 0.02, x=-0.1, y=0.026, z=0.04, c=STEEL, m='metal'), caja(0.1, 0.006, 0.1, x=0.08, y=0.023, z=-0.04, c='#c8402a', m='comida')])
obj('estante_ollas', 'Estante de la cocina con ollas colgadas', 'estanteria', 14, 'metal', 'pared', [
    caja(1.2, 0.03, 0.25, y=1.5, z=0.125, c=STEEL), caja(1.2, 0.04, 0.02, y=1.62, z=0.01, c='#a8aeb2'),
    *[cil(0.008, 0.008, 0.07, x=-0.45 + 0.3 * k, y=1.57, z=0.04, c=STEEL, r=[90, 0, 0], seg=6) for k in range(4)],
    *[cil(0.09 + 0.01 * (k % 2), 0.09 + 0.01 * (k % 2), 0.1, x=-0.45 + 0.3 * k, y=1.45, z=0.12, c=STEEL if k % 2 else '#b5693a', seg=10) for k in range(4)]],
    superficies=[{'y': 1.515, 'fondo': 0.22}], fijo='anclado en la realidad')
obj('carro_servicio', 'Carro de servicio', 'mueble', 12, 'metal', 'suelo', [
    caja(0.8, 0.03, 0.45, y=0.84, c=STEEL), caja(0.8, 0.03, 0.45, y=0.4, c=STEEL), *[caja(0.03, 0.86, 0.03, x=sx * 0.38, y=0.43, z=sz * 0.2, c='#a8aeb2') for sx in (-1, 1) for sz in (-1, 1)], caja(0.03, 0.2, 0.46, x=0.4, y=0.94, c='#a8aeb2')],
    superficies=[{'y': 0.855, 'margen': 0.04}, {'y': 0.415, 'margen': 0.04}])
obj('cubo_basura_pedal', 'Cubo de basura de pedal', 'papelera', 3.2, 'metal', 'suelo', [cil(0.17, 0.15, 0.55, c='#8a9096', seg=12), cil(0.175, 0.175, 0.03, y=0.565, c='#3a3e44', seg=12), caja(0.1, 0.02, 0.1, y=0.02, z=0.18, c=DARK, m='plastico')])
obj('caja_verduras', 'Caja de verduras', 'caja', 5.5, 'madera', 'superficie', [
    caja(0.5, 0.22, 0.35, c='#c8a878'), esf(0.07, -0.12, 0.25, 0.0, c='#c8402a'), esf(0.07, 0.0, 0.25, 0.06, c='#d8641c'), esf(0.075, 0.12, 0.25, -0.03, c='#7aa83a'), esf(0.06, -0.05, 0.26, -0.08, c='#d8c42a'), esf(0.065, 0.1, 0.25, 0.1, c='#a8402a')])
obj('saco_patatas', 'Saco de patatas', 'alimento', 10, 'tela', 'suelo', [caja(0.35, 0.5, 0.2, c='#b8996a', m='tela'), esf(0.12, 0, 0.5, 0, c='#b8996a', m='tela', s=[1.1, 0.35, 0.8])])
obj('garrafa_aceite', 'Garrafa de aceite de cinco litros', 'alimento', 4.8, 'plastico', 'superficie', [caja(0.17, 0.27, 0.12, c='#d8c42a', m='plastico'), cil(0.03, 0.03, 0.05, y=0.295, c='#3a7a2a', m='plastico', seg=8), caja(0.12, 0.12, 0.003, y=0.14, z=0.062, c=WHITE, m='papel')])

os.makedirs(os.path.join(ROOT, 'data', 'objetos'), exist_ok=True)
json.dump({'version': 1, 'familia': 'servicios', 'categorias': CATEGORIAS, 'objetos': OUT}, open(os.path.join(ROOT, 'data', 'objetos', 'servicios.json'), 'w'), ensure_ascii=False, indent=1)
print('objetos de servicios:', len(OUT))
