# The objects of a bar, a café and a restaurant (technical backlog, I-02 and X-01/X-02): each one a few primitives —
# boxes, cylinders, spheres, cones and textured planes, in metres —, its class of interaction, its mass, its material
# and what it stands on. The script is the model: it writes data/objetos/hosteleria.json.
# Frame of an object: x across, y up from its foot, z out of its front (+z faces whoever uses it; its back at -z).
#   python3 tools/interiores/catalogo_hosteleria.py
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

STEEL, DARK, WOOD, WOOD_D, MARBLE, WHITE, GLASS = '#c3c7ca', '#2b2b2e', '#8a5a36', '#5e3b22', '#e9e4dc', '#f4f2ec', '#bcd6dc'

# ---------------------------------------------------------------- the counter and what stands on it
obj('barra_modulo', 'Módulo de barra (1,2 m)', 'barra', 'FIXED', 450, 'madera', 'suelo', [
    caja(1.2, 1.02, 0.56, z=0, c=WOOD_D), caja(1.2, 0.05, 0.66, y=1.045, z=0.03, c=MARBLE, m='piedra'),
    caja(1.2, 0.1, 0.06, y=0.05, z=0.29, c=DARK, m='metal'), cil(0.025, 0.025, 1.2, y=0.22, z=0.36, c='#b8a46a', r=[0, 0, 90])],
    motivo_fijo='estructural', superficies=[{'y': 1.07, 'margen': 0.04}], nota='la barra de obra, con su reposapiés de latón')
obj('barra_esquina', 'Cabeza de barra', 'barra', 'FIXED', 300, 'madera', 'suelo', [
    caja(0.6, 1.02, 0.56, c=WOOD_D), caja(0.66, 0.05, 0.66, y=1.045, z=0.03, c=MARBLE, m='piedra')], motivo_fijo='estructural', superficies=[{'y': 1.07, 'margen': 0.04}])
obj('cafetera_industrial', 'Cafetera industrial de dos grupos', 'maquina_hosteleria', 'FIXED', 62, 'metal', 'superficie', [
    caja(0.72, 0.42, 0.42, y=0.21, z=-0.04, c=STEEL, m='metal'), caja(0.72, 0.04, 0.42, y=0.44, z=-0.04, c='#9aa0a4', m='metal'),
    caja(0.6, 0.08, 0.05, y=0.32, z=0.195, c=DARK, m='metal'),
    cil(0.035, 0.035, 0.06, x=-0.16, y=0.25, z=0.215, c=DARK), cil(0.035, 0.035, 0.06, x=0.16, y=0.25, z=0.215, c=DARK),
    caja(0.6, 0.025, 0.12, y=0.0125, z=0.22, c=DARK, m='metal'),
    cil(0.006, 0.006, 0.16, x=0.3, y=0.3, z=0.21, c=STEEL, r=[30, 0, 0])],
    modificadores=['USE'], motivo_fijo='anclado en la realidad', nota='conectada al agua y al desagüe')
obj('molinillo', 'Molinillo de café', 'pequeño_electrodomestico', 'CARRY', 9, 'metal', 'superficie', [
    caja(0.2, 0.34, 0.3, c=DARK, m='metal'), cono(0.09, 0.22, y=0.45, c='#3a2a20', m='plastico'), cil(0.1, 0.1, 0.02, y=0.57, c=DARK)])
obj('caja_registradora', 'Caja registradora', 'pequeño_electrodomestico', 'CARRY', 6, 'plastico', 'superficie', [
    caja(0.36, 0.12, 0.38, c='#33363a', m='plastico'), caja(0.3, 0.12, 0.04, y=0.2, z=-0.08, c='#1f2225', m='plastico', r=[-15, 0, 0]),
    caja(0.24, 0.07, 0.01, y=0.2, z=-0.055, c='#3b6d8a', m='plastico', luz=True)], modificadores=['USE'])
obj('vitrina_bolleria', 'Vitrina de bollería', 'vitrina', 'CARRY', 18, 'cristal', 'superficie', [
    caja(0.8, 0.04, 0.42, c=STEEL, m='metal'), caja(0.8, 0.36, 0.42, y=0.22, c=GLASS, m='cristal'),
    esf(0.045, -0.25, 0.08, 0.05, c='#c98a3c'), esf(0.045, -0.12, 0.08, -0.06, c='#d39a48'), caja(0.12, 0.05, 0.08, x=0.05, y=0.07, c='#a8642c', m='comida'),
    esf(0.05, 0.22, 0.09, 0.04, c='#e0b46a'), caja(0.16, 0.04, 0.1, x=0.1, y=0.22, c='#d8a050', m='comida'), esf(0.04, -0.2, 0.23, 0, c='#b97a34')])
obj('servilletero', 'Servilletero', 'papel', 'PICKUP', 0.25, 'metal', 'superficie', [
    caja(0.13, 0.015, 0.08, c=STEEL, m='metal'), caja(0.12, 0.09, 0.06, y=0.06, c=WHITE, m='papel'), caja(0.13, 0.1, 0.005, y=0.06, z=0.035, c=STEEL, m='metal')])
obj('azucarero', 'Azucarero dosificador', 'vajilla', 'PICKUP', 0.3, 'cristal', 'superficie', [cil(0.035, 0.04, 0.1, c=GLASS, m='cristal'), cil(0.03, 0.035, 0.03, y=0.115, c=STEEL)])
obj('palillero', 'Palillero', 'vajilla', 'PICKUP', 0.1, 'madera', 'superficie', [cil(0.025, 0.025, 0.07, c='#c8a878', m='madera')])
obj('datafono', 'Datáfono', 'informatica', 'PICKUP', 0.35, 'plastico', 'superficie', [caja(0.08, 0.03, 0.17, c='#26292c', m='plastico'), caja(0.06, 0.003, 0.05, y=0.0315, z=-0.045, c='#4a7a9a', m='plastico', luz=True), caja(0.06, 0.002, 0.07, y=0.031, z=0.035, c='#3a3d40', m='plastico')])
obj('bote_propinas', 'Bote de propinas', 'vajilla', 'PICKUP', 0.4, 'cristal', 'superficie', [cil(0.05, 0.05, 0.12, c=GLASS, m='cristal'), cil(0.04, 0.04, 0.02, y=0.02, c='#c8a040', m='metal')])
obj('tirador_cerveza', 'Grifo de cerveza', 'maquina_hosteleria', 'FIXED', 9, 'metal', 'superficie', [
    caja(0.32, 0.03, 0.18, c=STEEL, m='metal'), cil(0.05, 0.05, 0.42, y=0.24, c=STEEL), caja(0.26, 0.08, 0.08, y=0.42, z=0.02, c=STEEL, m='metal'),
    cil(0.012, 0.012, 0.18, x=-0.07, y=0.55, z=0.06, c='#262626', m='plastico'), cil(0.012, 0.012, 0.18, x=0.07, y=0.55, z=0.06, c='#262626', m='plastico')],
    modificadores=['USE'], motivo_fijo='anclado en la realidad')
obj('bandeja', 'Bandeja', 'vajilla', 'PICKUP', 0.4, 'metal', 'superficie', [cil(0.17, 0.17, 0.015, c='#9aa0a4', m='metal', seg=24)])
obj('taburete_alto', 'Taburete alto de barra', 'taburete', 'CARRY', 6, 'metal', 'suelo', [
    cil(0.19, 0.19, 0.06, y=0.75, c='#5a3a24', m='madera', seg=18), cil(0.022, 0.022, 0.72, y=0.36, c=DARK),
    cil(0.2, 0.22, 0.02, y=0.01, c=DARK), cil(0.13, 0.13, 0.015, y=0.3, c=DARK, seg=16)],
    modificadores=['SEAT'], asientos=[{'p': [0, 0.78, 0], 'h': 0.78, 'anim': 'taburete_alto'}])

# ---------------------------------------------------------------- behind the counter
obj('mueble_trasbarra', 'Mueble bajo de trasbarra (1,2 m)', 'mueble', 'FIXED', 140, 'madera', 'suelo', [
    caja(1.2, 0.86, 0.6, c='#6a4a32'), caja(1.2, 0.04, 0.63, y=0.88, z=0.015, c='#d8d2c8', m='piedra'),
    caja(0.56, 0.7, 0.01, x=-0.3, y=0.43, z=0.305, c='#5a3e2a'), caja(0.56, 0.7, 0.01, x=0.3, y=0.43, z=0.305, c='#5a3e2a')],
    motivo_fijo='estructural', superficies=[{'y': 0.9, 'margen': 0.03}])
obj('botellero_pared', 'Botellero de pared (3 baldas)', 'estanteria', 'FIXED', 22, 'madera', 'pared', [
    caja(1.2, 0.02, 0.24, y=1.5, z=0.12, c=WOOD), caja(1.2, 0.02, 0.24, y=1.85, z=0.12, c=WOOD), caja(1.2, 0.02, 0.24, y=2.2, z=0.12, c=WOOD),
    caja(1.2, 0.95, 0.02, y=1.86, z=0.01, c='#b7a58c', m='madera'), caja(1.2, 0.4, 0.005, y=1.7, z=0.015, c='#d8dde0', m='cristal')],
    motivo_fijo='anclado en la realidad', superficies=[{'y': 1.51, 'fondo': 0.22}, {'y': 1.86, 'fondo': 0.22}, {'y': 2.21, 'fondo': 0.22}])
BOT = [('whisky', 'Botella de whisky', '#8a4a18', '#2a1a10', 0.05, 0.3, 'caja'), ('ron', 'Botella de ron', '#6a3a1c', '#262626', 0.042, 0.3, 'cil'),
       ('ginebra', 'Botella de ginebra', '#9fc4c8', '#2a4a6a', 0.04, 0.3, 'cil'), ('anis', 'Botella de anís', '#e8eef0', '#c82a2a', 0.045, 0.28, 'caja'),
       ('brandy', 'Botella de brandy', '#7a3a14', '#c8a040', 0.045, 0.27, 'cil'), ('vino_tinto', 'Botella de vino tinto', '#3a1a24', '#e8e0d0', 0.038, 0.3, 'cil'),
       ('vino_blanco', 'Botella de vino blanco', '#a8b860', '#e8e0d0', 0.038, 0.3, 'cil'), ('vermut', 'Botella de vermut', '#5a1a14', '#e8c060', 0.042, 0.28, 'cil'),
       ('licor_hierbas', 'Botella de licor de hierbas', '#3a5a2a', '#f0e6c8', 0.04, 0.26, 'cil'), ('pacharan', 'Botella de pacharán', '#6a1a3a', '#f0e6c8', 0.04, 0.27, 'cil'),
       ('agua_mineral', 'Botella de agua', '#cfe6f0', '#2a6ab0', 0.035, 0.24, 'cil'), ('refresco_cola', 'Botella de refresco de cola', '#2a1410', '#c82020', 0.032, 0.22, 'cil'),
       ('refresco_naranja', 'Botella de refresco de naranja', '#f08a20', '#1a4aa0', 0.032, 0.22, 'cil'), ('cerveza', 'Botellín de cerveza', '#5a3a10', '#e8c040', 0.03, 0.2, 'cil'),
       ('mosto', 'Botella de mosto', '#c89a4a', '#3a6a2a', 0.034, 0.24, 'cil')]
for k, n, cuerpo, etiqueta, r, h, forma in BOT:
    partes = ([caja(r * 2, h * 0.7, r * 1.6, c=cuerpo, m='cristal'), caja(r * 2 + 0.002, h * 0.25, r * 1.6 + 0.002, y=h * 0.32, c=etiqueta, m='papel')] if forma == 'caja' else
              [cil(r, r, h * 0.7, c=cuerpo, m='cristal'), cil(r + 0.001, r + 0.001, h * 0.25, y=h * 0.32, c=etiqueta, m='papel')])
    partes += [cono(r, h * 0.12, y=h * 0.76, c=cuerpo, m='cristal'), cil(r * 0.36, r * 0.36, h * 0.18, y=h * 0.91, c=cuerpo, m='cristal'), cil(r * 0.4, r * 0.4, h * 0.04, y=h * 0.99, c='#c8a040' if k != 'agua_mineral' else '#2a6ab0')]
    obj('botella_' + k, n, 'botella', 'PICKUP', round(0.4 + h * 3, 2), 'cristal', 'superficie', partes)
obj('estante_vajilla', 'Estante de tazas y vasos', 'estanteria', 'FIXED', 14, 'madera', 'pared', [
    caja(1.0, 0.02, 0.3, y=1.15, z=0.15, c=WOOD), caja(1.0, 0.02, 0.3, y=1.42, z=0.15, c=WOOD), caja(0.02, 0.3, 0.3, x=-0.49, y=1.29, z=0.15, c=WOOD), caja(0.02, 0.3, 0.3, x=0.49, y=1.29, z=0.15, c=WOOD)],
    motivo_fijo='anclado en la realidad', superficies=[{'y': 1.16, 'fondo': 0.28}, {'y': 1.43, 'fondo': 0.28}])
obj('taza_cafe', 'Taza de café', 'vajilla', 'PICKUP', 0.18, 'ceramica', 'superficie', [cil(0.038, 0.03, 0.065, c=WHITE, m='ceramica'), cil(0.02, 0.02, 0.008, x=0.045, y=0.035, c=WHITE, m='ceramica', r=[90, 0, 0])])
obj('taza_desayuno', 'Taza de desayuno', 'vajilla', 'PICKUP', 0.3, 'ceramica', 'superficie', [cil(0.048, 0.04, 0.085, c='#f0ece2', m='ceramica'), cil(0.025, 0.025, 0.01, x=0.056, y=0.045, c='#f0ece2', m='ceramica', r=[90, 0, 0])])
obj('plato_cafe', 'Platillo', 'vajilla', 'PICKUP', 0.12, 'ceramica', 'superficie', [cil(0.07, 0.06, 0.012, c=WHITE, m='ceramica', seg=20)])
obj('plato_llano', 'Plato llano', 'vajilla', 'PICKUP', 0.5, 'ceramica', 'superficie', [cil(0.13, 0.11, 0.02, c=WHITE, m='ceramica', seg=24)])
obj('vaso_cana', 'Vaso de caña', 'vajilla', 'PICKUP', 0.2, 'cristal', 'superficie', [cil(0.035, 0.03, 0.12, c=GLASS, m='cristal')])
obj('vaso_tubo', 'Vaso de tubo', 'vajilla', 'PICKUP', 0.25, 'cristal', 'superficie', [cil(0.03, 0.03, 0.15, c=GLASS, m='cristal')])
obj('copa_vino', 'Copa de vino', 'vajilla', 'PICKUP', 0.15, 'cristal', 'superficie', [cil(0.035, 0.025, 0.08, y=0.13, c=GLASS, m='cristal'), cil(0.004, 0.004, 0.09, y=0.045, c=GLASS, m='cristal'), cil(0.03, 0.03, 0.004, y=0.002, c=GLASS, m='cristal')])
obj('lavavajillas', 'Lavavajillas de barra', 'electrodomestico', 'FIXED', 48, 'metal', 'suelo', [caja(0.6, 0.82, 0.6, c=STEEL, m='metal'), caja(0.5, 0.05, 0.02, y=0.7, z=0.3, c=DARK, m='plastico')],
    modificadores=['USE'], motivo_fijo='anclado en la realidad')
obj('nevera_bebidas', 'Nevera de bebidas con puerta de cristal', 'nevera', 'PUSH_HEAVY', 92, 'metal', 'suelo', [
    caja(0.62, 1.86, 0.62, c='#2a2e33', m='metal'), caja(0.54, 1.5, 0.01, y=1.0, z=0.31, c='#9cc8d8', m='cristal'), caja(0.5, 0.18, 0.012, y=1.72, z=0.315, c='#c82020', m='plastico', luz=True),
    caja(0.5, 0.02, 0.5, y=0.55, z=0.0, c='#d8dde0', m='metal'), caja(0.5, 0.02, 0.5, y=0.95, c='#d8dde0', m='metal'), caja(0.5, 0.02, 0.5, y=1.35, c='#d8dde0', m='metal'),
    cil(0.03, 0.03, 0.2, x=-0.15, y=0.66, z=0.15, c='#c82020', m='cristal'), cil(0.03, 0.03, 0.2, x=0, y=0.66, z=0.15, c='#f08a20', m='cristal'), cil(0.03, 0.03, 0.2, x=0.15, y=0.66, z=0.15, c='#2a6ab0', m='cristal'),
    cil(0.03, 0.03, 0.2, x=-0.15, y=1.06, z=0.15, c='#5a3a10', m='cristal'), cil(0.03, 0.03, 0.2, x=0.15, y=1.06, z=0.15, c='#5a3a10', m='cristal')],
    modificadores=['USE'])
obj('pizarra_precios', 'Pizarra de precios', 'decoracion', 'PICKUP', 3, 'madera', 'pared', [caja(0.9, 0.62, 0.025, y=1.95, z=0.0125, c='#5a3a20'), plano(0.84, 0.56, y=1.95, z=0.027, tex={'tipo': 'pizarra', 'lineas': ['Café solo  1,20', 'Café con leche  1,40', 'Tostada  1,80', 'Caña  1,50', 'Tinto  1,50', 'Churros  2,00']})])
obj('exprimidor', 'Exprimidor de zumos', 'pequeño_electrodomestico', 'CARRY', 7, 'metal', 'superficie', [caja(0.26, 0.2, 0.3, c=STEEL, m='metal'), cil(0.1, 0.1, 0.25, y=0.32, c='#d0e8d8', m='plastico'), esf(0.04, 0.05, 0.47, 0, c='#f08a20')])
obj('tostadora', 'Tostadora de barra', 'pequeño_electrodomestico', 'CARRY', 8, 'metal', 'superficie', [caja(0.46, 0.24, 0.34, c=STEEL, m='metal'), caja(0.4, 0.04, 0.02, y=0.12, z=0.17, c='#262626', m='metal')])
obj('microondas', 'Microondas', 'pequeño_electrodomestico', 'CARRY', 13, 'metal', 'superficie', [caja(0.5, 0.3, 0.38, c='#e8e8e4', m='metal'), caja(0.32, 0.22, 0.005, x=-0.06, y=0.15, z=0.19, c='#1a1c1e', m='cristal'), caja(0.1, 0.22, 0.005, x=0.19, y=0.15, z=0.19, c='#c8ccd0', m='plastico')])
obj('jamonero', 'Jamonero con jamón', 'alimento', 'CARRY', 9, 'madera', 'superficie', [caja(0.2, 0.04, 0.5, c=WOOD), caja(0.04, 0.16, 0.04, y=0.12, z=-0.2, c=STEEL, m='metal'),
    {'f': 'esfera', 'd': [0.09], 'p': [0, 0.14, 0.04], 'c': '#7a2a1c', 'm': 'comida', 's': [1, 0.8, 2.2]}, cil(0.02, 0.025, 0.12, y=0.2, z=-0.2, c='#c89a6a', m='comida', r=[60, 0, 0])])
obj('televisor_pared', 'Televisor de pared', 'pantalla', 'FIXED', 11, 'plastico', 'pared', [caja(1.0, 0.6, 0.05, y=2.3, z=0.06, c='#242424', m='plastico'), plano(0.94, 0.54, y=2.3, z=0.088, tex={'tipo': 'pantalla'}, m='plastico', luz=True), caja(0.2, 0.2, 0.04, y=2.3, z=0.02, c='#2a2a2a', m='metal')],
    motivo_fijo='anclado en la realidad')
obj('reloj_pared', 'Reloj de pared', 'reloj', 'PICKUP', 0.8, 'plastico', 'pared', [cil(0.17, 0.17, 0.04, y=2.35, z=0.02, c='#f6f2e6', m='plastico', r=[90, 0, 0], tex={'tipo': 'reloj'})])
obj('calendario_pared', 'Calendario de la cooperativa', 'papel', 'PICKUP', 0.2, 'papel', 'pared', [plano(0.32, 0.46, y=1.6, z=0.005, tex={'tipo': 'calendario'})])
obj('expositor_patatas', 'Expositor de patatas fritas', 'decoracion', 'CARRY', 6, 'metal', 'suelo', [caja(0.4, 1.5, 0.35, c='#c8ccd0', m='metal'),
    caja(0.34, 0.3, 0.06, y=0.4, z=0.12, c='#e8c040', m='plastico'), caja(0.34, 0.3, 0.06, y=0.8, z=0.12, c='#c82a2a', m='plastico'), caja(0.34, 0.3, 0.06, y=1.2, z=0.12, c='#2a6ab0', m='plastico')])

# ---------------------------------------------------------------- the room
obj('mesa_cuadrada', 'Mesa cuadrada de bar', 'mesa', 'PUSH', 27, 'metal', 'suelo', [caja(0.7, 0.03, 0.7, y=0.745, c='#e6e0d4', m='piedra'), cil(0.03, 0.03, 0.71, y=0.375, c=DARK), caja(0.5, 0.02, 0.06, y=0.01, c=DARK, m='metal'), caja(0.06, 0.02, 0.5, y=0.01, c=DARK, m='metal')],
    motivo_clase='encimera de mármol sobre pie de fundición', superficies=[{'y': 0.76, 'margen': 0.05}])
obj('mesa_redonda', 'Mesa redonda de mármol', 'mesa', 'PUSH', 29, 'piedra', 'suelo', [cil(0.36, 0.36, 0.03, y=0.745, c='#ece6dc', m='piedra', seg=24), cil(0.03, 0.03, 0.71, y=0.375, c=DARK), cil(0.22, 0.24, 0.03, y=0.015, c=DARK)],
    superficies=[{'y': 0.76, 'margen': 0.08}])
obj('mesa_comedor', 'Mesa de comedor (4)', 'mesa', 'PUSH', 34, 'madera', 'suelo', [caja(1.2, 0.04, 0.8, y=0.74, c=WOOD), caja(0.06, 0.72, 0.06, x=-0.54, y=0.36, z=-0.34, c=WOOD_D), caja(0.06, 0.72, 0.06, x=0.54, y=0.36, z=-0.34, c=WOOD_D),
    caja(0.06, 0.72, 0.06, x=-0.54, y=0.36, z=0.34, c=WOOD_D), caja(0.06, 0.72, 0.06, x=0.54, y=0.36, z=0.34, c=WOOD_D)], superficies=[{'y': 0.76, 'margen': 0.06}])
obj('silla_bistro', 'Silla de bar', 'silla', 'CARRY', 5.5, 'metal', 'suelo', [caja(0.42, 0.04, 0.42, y=0.46, c='#6a4a30'), cil(0.012, 0.012, 0.45, x=-0.18, y=0.225, z=-0.18, c=DARK), cil(0.012, 0.012, 0.45, x=0.18, y=0.225, z=-0.18, c=DARK),
    cil(0.012, 0.012, 0.45, x=-0.18, y=0.225, z=0.18, c=DARK), cil(0.012, 0.012, 0.45, x=0.18, y=0.225, z=0.18, c=DARK), caja(0.4, 0.4, 0.03, y=0.7, z=-0.2, c='#6a4a30', r=[-8, 0, 0])],
    modificadores=['SEAT'], asientos=[{'p': [0, 0.48, 0.02], 'h': 0.48, 'anim': 'silla'}])
obj('silla_madera', 'Silla de madera', 'silla', 'CARRY', 5, 'madera', 'suelo', [caja(0.44, 0.04, 0.44, y=0.46, c=WOOD), caja(0.04, 0.44, 0.04, x=-0.19, y=0.22, z=-0.19, c=WOOD_D), caja(0.04, 0.44, 0.04, x=0.19, y=0.22, z=-0.19, c=WOOD_D),
    caja(0.04, 0.44, 0.04, x=-0.19, y=0.22, z=0.19, c=WOOD_D), caja(0.04, 0.44, 0.04, x=0.19, y=0.22, z=0.19, c=WOOD_D), caja(0.04, 0.5, 0.04, x=-0.19, y=0.73, z=-0.2, c=WOOD_D), caja(0.04, 0.5, 0.04, x=0.19, y=0.73, z=-0.2, c=WOOD_D),
    caja(0.42, 0.14, 0.03, y=0.86, z=-0.2, c=WOOD)], modificadores=['SEAT'], asientos=[{'p': [0, 0.48, 0.02], 'h': 0.48, 'anim': 'silla'}])
obj('revistero', 'Revistero', 'mueble', 'CARRY', 5.5, 'metal', 'suelo', [caja(0.4, 0.02, 0.3, y=0.01, c=DARK, m='metal'), caja(0.4, 0.7, 0.02, y=0.36, z=-0.1, c=DARK, m='metal'), caja(0.38, 0.3, 0.06, y=0.5, z=-0.05, c='#e8e2d4', m='papel')], superficies=[{'y': 0.02, 'margen': 0.02}])
obj('periodico', 'Periódico', 'papel', 'PICKUP', 0.25, 'papel', 'superficie', [caja(0.3, 0.012, 0.4, c='#ece8dc', m='papel', tex={'tipo': 'periodico'})])
obj('revista', 'Revista', 'papel', 'PICKUP', 0.2, 'papel', 'superficie', [caja(0.21, 0.008, 0.28, c='#c84a3a', m='papel')])
obj('planta_grande', 'Planta en maceta grande', 'planta', 'CARRY', 18, 'ceramica', 'suelo', [cil(0.22, 0.17, 0.42, c='#b5694a', m='ceramica'), esf(0.32, 0, 0.82, 0, c='#4a7a3a', m='madera', s=[1, 1.3, 1]), esf(0.2, 0.15, 1.1, 0.1, c='#558a40', m='madera')])
obj('planta_pequena', 'Maceta pequeña', 'planta', 'PICKUP', 1.2, 'ceramica', 'superficie', [cil(0.07, 0.055, 0.12, c='#c87a54', m='ceramica'), esf(0.09, 0, 0.18, 0, c='#4f8a3c', m='madera')])
obj('cuadro_paisaje', 'Cuadro de un paisaje de las Vegas', 'cuadro', 'PICKUP', 2, 'madera', 'pared', [caja(0.7, 0.5, 0.03, y=1.7, z=0.015, c='#6a4a2a'), plano(0.62, 0.42, y=1.7, z=0.031, tex={'tipo': 'paisaje'}, m='papel')])
obj('cuadro_foto_antigua', 'Foto antigua del pueblo', 'cuadro', 'PICKUP', 1.2, 'madera', 'pared', [caja(0.5, 0.38, 0.025, y=1.75, z=0.0125, c='#2a2420'), plano(0.44, 0.32, y=1.75, z=0.026, tex={'tipo': 'foto'}, m='papel')])
obj('cartel_toros', 'Cartel de toros enmarcado', 'cuadro', 'PICKUP', 1.5, 'papel', 'pared', [caja(0.5, 0.75, 0.02, y=1.75, z=0.01, c='#3a2a1a'), plano(0.46, 0.7, y=1.75, z=0.021, tex={'tipo': 'cartel_fiesta'}, m='papel')])
obj('lampara_colgante', 'Lámpara colgante', 'lampara', 'FIXED', 1.6, 'metal', 'techo', [cil(0.004, 0.004, 0.7, y=-0.35, c='#262626'), cono(0.2, 0.18, y=-0.79, c='#2f3a34', m='metal'), esf(0.05, 0, -0.86, 0, c='#fff3d6', m='cristal', luz=True)],
    motivo_fijo='anclado en la realidad')
obj('papelera', 'Papelera', 'papelera', 'PICKUP', 1.5, 'metal', 'suelo', [cil(0.13, 0.11, 0.38, c='#7a8086', m='metal')])
obj('perchero', 'Perchero de pie', 'perchero', 'CARRY', 6, 'madera', 'suelo', [cil(0.02, 0.02, 1.75, y=0.875, c=WOOD_D, m='madera'), cil(0.2, 0.22, 0.03, y=0.015, c=WOOD_D, m='madera'), cil(0.01, 0.01, 0.3, y=1.7, c=WOOD_D, m='madera', r=[0, 0, 70]), cil(0.01, 0.01, 0.3, y=1.7, c=WOOD_D, m='madera', r=[70, 0, 0])])
obj('tragaperras', 'Máquina tragaperras', 'maquina_expendedora', 'PUSH_HEAVY', 88, 'metal', 'suelo', [caja(0.6, 1.7, 0.5, c='#2a1a3a', m='metal'), plano(0.5, 0.5, y=1.25, z=0.252, tex={'tipo': 'tragaperras'}, m='plastico', luz=True), caja(0.5, 0.06, 0.15, y=0.85, z=0.3, c='#c8a040', m='metal')],
    modificadores=['USE'])
obj('maquina_tabaco', 'Máquina de tabaco', 'maquina_expendedora', 'PUSH_HEAVY', 120, 'metal', 'suelo', [caja(0.7, 1.75, 0.45, c='#3a3e44', m='metal'), caja(0.6, 0.9, 0.01, y=1.15, z=0.23, c='#c8ccd0', m='plastico', luz=True), caja(0.2, 0.1, 0.05, y=0.55, z=0.24, c='#262626', m='metal')],
    modificadores=['USE'])
obj('carta_menu', 'Carta', 'papel', 'PICKUP', 0.15, 'papel', 'superficie', [caja(0.16, 0.01, 0.24, c='#6a2a1c', m='papel')])
obj('atril_menu', 'Pizarra de menú del día', 'decoracion', 'CARRY', 6, 'madera', 'suelo', [caja(0.6, 0.85, 0.02, y=0.425, z=0.09, c='#2a2a26', r=[-12, 0, 0], tex={'tipo': 'menu_dia'}), caja(0.6, 0.85, 0.02, y=0.425, z=-0.09, c='#2a2a26', r=[12, 0, 0]), caja(0.66, 0.04, 0.05, y=0.84, c=WOOD)])
obj('cucharilla', 'Cucharilla', 'cubiertos', 'PICKUP', 0.02, 'metal', 'superficie', [caja(0.012, 0.004, 0.11, c=STEEL, m='metal')])
obj('plato_churros', 'Ración de churros', 'alimento', 'PICKUP', 0.5, 'comida', 'superficie', [cil(0.1, 0.09, 0.015, c=WHITE, m='ceramica'), cil(0.012, 0.012, 0.14, x=-0.03, y=0.025, c='#d8a050', m='comida', r=[90, 20, 0]), cil(0.012, 0.012, 0.14, x=0.02, y=0.025, c='#d09848', m='comida', r=[90, -15, 0])])
obj('plato_tostada', 'Tostada con tomate', 'alimento', 'PICKUP', 0.55, 'comida', 'superficie', [cil(0.1, 0.09, 0.015, c=WHITE, m='ceramica'), caja(0.14, 0.02, 0.08, y=0.025, c='#c8904a', m='comida'), caja(0.12, 0.006, 0.06, y=0.038, c='#c8402a', m='comida')])
obj('vaso_agua', 'Vaso de agua', 'vajilla', 'PICKUP', 0.25, 'cristal', 'superficie', [cil(0.033, 0.028, 0.1, c=GLASS, m='cristal')])
obj('servilleta_arrugada', 'Servilleta arrugada', 'papel', 'PICKUP', 0.01, 'papel', 'superficie', [esf(0.025, 0, 0.02, 0, c=WHITE, m='papel', s=[1.2, 0.7, 1])])

# ---------------------------------------------------------------- the toilets
obj('lavabo', 'Lavabo', 'sanitario', 'FIXED', 18, 'ceramica', 'pared', [caja(0.5, 0.16, 0.42, y=0.8, z=0.21, c=WHITE, m='ceramica'), cil(0.08, 0.06, 0.62, y=0.36, z=0.18, c=WHITE, m='ceramica'), cil(0.012, 0.012, 0.16, y=0.95, z=0.06, c=STEEL, r=[30, 0, 0])],
    modificadores=['USE'], motivo_fijo='anclado en la realidad')
obj('inodoro', 'Inodoro', 'sanitario', 'FIXED', 30, 'ceramica', 'suelo', [cil(0.17, 0.13, 0.4, z=0.08, c=WHITE, m='ceramica'), caja(0.4, 0.38, 0.17, y=0.6, z=-0.22, c=WHITE, m='ceramica'), cil(0.18, 0.18, 0.03, y=0.415, z=0.08, c='#f8f6f0', m='plastico')],
    modificadores=['USE', 'SEAT'], motivo_fijo='anclado en la realidad', asientos=[{'p': [0, 0.42, 0.08], 'h': 0.42, 'anim': 'silla'}])
obj('dispensador_jabon', 'Dispensador de jabón', 'limpieza', 'FIXED', 0.6, 'plastico', 'pared', [caja(0.1, 0.2, 0.09, y=1.15, z=0.045, c='#e8ecef', m='plastico')], motivo_fijo='anclado en la realidad')
obj('secamanos', 'Secamanos', 'pequeño_electrodomestico', 'FIXED', 4, 'metal', 'pared', [caja(0.28, 0.24, 0.16, y=1.3, z=0.08, c='#e6e8ea', m='metal')], modificadores=['USE'], motivo_fijo='anclado en la realidad')
obj('espejo_aseo', 'Espejo del aseo', 'espejo', 'FIXED', 5, 'cristal', 'pared', [caja(0.5, 0.7, 0.012, y=1.55, z=0.006, c='#c8d6dc', m='cristal')], motivo_fijo='anclado en la realidad')
obj('portarrollos', 'Portarrollos', 'limpieza', 'FIXED', 0.4, 'metal', 'pared', [cil(0.05, 0.05, 0.1, y=0.65, z=0.06, c=WHITE, m='papel', r=[0, 0, 90])], motivo_fijo='anclado en la realidad')
obj('escobilla', 'Escobilla del váter', 'limpieza', 'PICKUP', 0.3, 'plastico', 'suelo', [cil(0.05, 0.05, 0.12, c='#e8e8e8', m='plastico'), cil(0.008, 0.008, 0.3, y=0.25, c='#e8e8e8', m='plastico')])

# ---------------------------------------------------------------- the storeroom
obj('caja_bebidas', 'Caja de botellines', 'caja', 'CARRY', 12, 'plastico', 'suelo', [caja(0.4, 0.28, 0.3, c='#c82a2a', m='plastico'), cil(0.03, 0.03, 0.04, x=-0.1, y=0.3, c='#5a3a10', m='cristal'), cil(0.03, 0.03, 0.04, x=0.1, y=0.3, c='#5a3a10', m='cristal')], superficies=[{'y': 0.28, 'margen': 0.02}])
obj('barril_cerveza', 'Barril de cerveza', 'barril', 'PUSH', 60, 'metal', 'suelo', [cil(0.2, 0.2, 0.55, c=STEEL, seg=18), cil(0.21, 0.21, 0.03, y=0.06, c='#9aa0a4'), cil(0.21, 0.21, 0.03, y=0.5, c='#9aa0a4'), cil(0.04, 0.04, 0.05, y=0.575, c=DARK)])
obj('estanteria_metalica', 'Estantería metálica de almacén', 'estanteria', 'PUSH', 32, 'metal', 'suelo', [
    caja(0.04, 1.8, 0.04, x=-0.48, y=0.9, z=-0.18, c='#8a9096', m='metal'), caja(0.04, 1.8, 0.04, x=0.48, y=0.9, z=-0.18, c='#8a9096', m='metal'),
    caja(0.04, 1.8, 0.04, x=-0.48, y=0.9, z=0.18, c='#8a9096', m='metal'), caja(0.04, 1.8, 0.04, x=0.48, y=0.9, z=0.18, c='#8a9096', m='metal'),
    caja(1.0, 0.02, 0.4, y=0.15, c='#9aa0a6', m='metal'), caja(1.0, 0.02, 0.4, y=0.7, c='#9aa0a6', m='metal'), caja(1.0, 0.02, 0.4, y=1.25, c='#9aa0a6', m='metal'), caja(1.0, 0.02, 0.4, y=1.78, c='#9aa0a6', m='metal')],
    superficies=[{'y': 0.16, 'fondo': 0.38}, {'y': 0.71, 'fondo': 0.38}, {'y': 1.26, 'fondo': 0.38}])
obj('fregona_cubo', 'Fregona y cubo', 'limpieza', 'PICKUP', 2.5, 'plastico', 'suelo', [cil(0.15, 0.13, 0.26, c='#2a6ab0', m='plastico'), cil(0.01, 0.01, 1.3, x=0.05, y=0.65, c='#c8c8c8', m='metal', r=[0, 0, 8])])
obj('escoba', 'Escoba', 'limpieza', 'PICKUP', 0.7, 'plastico', 'suelo', [cil(0.012, 0.012, 1.25, y=0.7, c='#3a6a2a', m='plastico', r=[0, 0, 6]), caja(0.28, 0.08, 0.06, y=0.04, c='#e8c040', m='plastico')])
obj('caja_carton', 'Caja de cartón', 'caja', 'PICKUP', 2.5, 'papel', 'superficie', [caja(0.36, 0.26, 0.3, c='#b88a58', m='papel')])
obj('saco_cafe', 'Saco de café', 'alimento', 'CARRY', 6, 'tela', 'superficie', [caja(0.3, 0.36, 0.18, c='#a07a4a', m='tela')])
obj('caja_vasos', 'Caja de vasos', 'caja', 'CARRY', 7, 'papel', 'superficie', [caja(0.4, 0.22, 0.3, c='#d8c8a8', m='papel')])

# ---------------------------------------------------------------- what a village bar has that a café does not
obj('diana', 'Diana de dardos', 'decoracion', 'PICKUP', 2.5, 'tela', 'pared', [
    caja(0.6, 0.6, 0.02, y=1.73, z=0.01, c='#3a2416'), cil(0.225, 0.225, 0.035, y=1.73, z=0.0375, c='#242424', m='tela', r=[90, 0, 0], seg=24),
    plano(0.45, 0.45, y=1.73, z=0.0555, tex={'tipo': 'diana'}, m='tela')], nota='a 1,73 m del suelo, como manda el reglamento')
FUT = [caja(1.4, 0.04, 0.75, y=0.74, c='#2a3a6a', m='madera'), plano(1.3, 0.66, y=0.762, tex={'tipo': 'futbolin'}, m='plastico', r=[-90, 0, 0]),
       caja(1.4, 0.18, 0.03, y=0.81, z=0.36, c='#2a3a6a'), caja(1.4, 0.18, 0.03, y=0.81, z=-0.36, c='#2a3a6a'),
       caja(0.03, 0.18, 0.75, x=0.685, y=0.81, c='#2a3a6a'), caja(0.03, 0.18, 0.75, x=-0.685, y=0.81, c='#2a3a6a')]
FUT += [caja(0.07, 0.72, 0.07, x=sx * 0.62, y=0.36, z=sz * 0.3, c='#262626', m='metal') for sx in (-1, 1) for sz in (-1, 1)]
for i, (n, col) in enumerate([(1, '#c8202a'), (2, '#c8202a'), (3, '#2a5ac8'), (5, '#c8202a'), (5, '#2a5ac8'), (3, '#c8202a'), (2, '#2a5ac8'), (1, '#2a5ac8')]):
    x = -0.6 + i * (1.2 / 7)
    FUT.append(cil(0.008, 0.008, 1.12, x=x, y=0.86, c=STEEL, r=[90, 0, 0]))
    FUT.append(cil(0.018, 0.018, 0.1, x=x, y=0.86, z=(0.53 if i % 2 else -0.53), c='#262626', m='goma', r=[90, 0, 0]))
    for j in range(n):
        FUT.append(caja(0.025, 0.09, 0.03, x=x, y=0.835, z=(j - (n - 1) / 2) * (0.6 / max(n, 2)), c=col, m='plastico'))
obj('futbolin', 'Futbolín', 'mueble', 'PUSH', 70, 'madera', 'suelo', FUT, modificadores=['USE'], nota='el de toda la vida, rojos contra azules')
obj('cabeza_ciervo', 'Cabeza de ciervo disecada', 'decoracion', 'CARRY', 9, 'tela', 'pared', [
    caja(0.3, 0.4, 0.03, y=2.05, z=0.015, c='#5a3a20'), cil(0.07, 0.09, 0.2, y=2.0, z=0.12, c='#7a5634', m='tela', r=[70, 0, 0]),
    caja(0.13, 0.15, 0.26, y=2.08, z=0.26, c='#7a5634', m='tela', r=[-20, 0, 0]), caja(0.07, 0.07, 0.1, y=2.03, z=0.42, c='#3a2a1a', m='tela'),
    cil(0.012, 0.016, 0.42, x=-0.1, y=2.36, z=0.24, c='#d8c8a8', m='madera', r=[0, 0, 28]), cil(0.012, 0.016, 0.42, x=0.1, y=2.36, z=0.24, c='#d8c8a8', m='madera', r=[0, 0, -28]),
    cil(0.008, 0.01, 0.16, x=-0.2, y=2.43, z=0.28, c='#d8c8a8', m='madera', r=[0, 0, 70]), cil(0.008, 0.01, 0.16, x=0.2, y=2.43, z=0.28, c='#d8c8a8', m='madera', r=[0, 0, -70])],
    nota='trofeo de montería, de las que cuelgan en los bares de Extremadura')
obj('ventilador_techo', 'Ventilador de techo con luz', 'lampara', 'FIXED', 6, 'metal', 'techo', [
    cil(0.015, 0.015, 0.3, y=-0.15, c='#d8c8a0', m='metal'), cil(0.1, 0.1, 0.12, y=-0.36, c='#d8c8a0', m='metal'),
    caja(1.2, 0.012, 0.13, y=-0.4, c=WOOD, m='madera'), caja(0.13, 0.012, 1.2, y=-0.4, c=WOOD, m='madera'),
    esf(0.07, 0, -0.49, 0, c='#fff3d6', m='cristal', luz=True)], motivo_fijo='anclado en la realidad')
obj('vitrina_tapas', 'Vitrina refrigerada de tapas', 'vitrina', 'CARRY', 22, 'cristal', 'superficie', [
    caja(1.0, 0.08, 0.4, y=0.04, c=STEEL, m='metal'), caja(1.0, 0.22, 0.36, y=0.19, c=GLASS, m='cristal'),
    caja(0.26, 0.03, 0.22, x=-0.33, y=0.095, c='#e8c860', m='comida'), caja(0.26, 0.03, 0.22, x=0, y=0.095, c='#efe6c8', m='comida'), caja(0.26, 0.03, 0.22, x=0.33, y=0.095, c='#9a5a2a', m='comida')],
    modificadores=['USE'], nota='tortilla, ensaladilla y croquetas')
obj('mesa_barril', 'Mesa de barril', 'mueble', 'PUSH', 38, 'madera', 'suelo', [
    cil(0.3, 0.28, 0.95, y=0.475, c='#7a4a26', m='madera', seg=18), cil(0.302, 0.302, 0.04, y=0.25, c='#3a3a3a', m='metal', seg=18), cil(0.302, 0.302, 0.04, y=0.75, c='#3a3a3a', m='metal', seg=18),
    cil(0.36, 0.36, 0.04, y=0.97, c='#5e3b22', m='madera', seg=20)], superficies=[{'y': 0.99, 'margen': 0.03}], nota='un tonel de vino como mesa alta')
obj('plato_tortilla', 'Tapa de tortilla', 'alimento', 'PICKUP', 0.35, 'ceramica', 'superficie', [cil(0.075, 0.065, 0.012, c=WHITE, m='ceramica', seg=18), caja(0.07, 0.035, 0.06, y=0.03, c='#e8c860', m='comida', r=[0, 20, 0])])
obj('cuenco_aceitunas', 'Cuenco de aceitunas', 'alimento', 'PICKUP', 0.3, 'ceramica', 'superficie', [cil(0.055, 0.035, 0.04, c='#c87a3a', m='ceramica', seg=16)] + [esf(0.012, x, 0.04, z, c='#6a7a2a') for x, z in ((-0.02, 0), (0.015, 0.01), (0, -0.02), (0.02, -0.015), (-0.01, 0.02))])
obj('plato_jamon', 'Plato de jamón', 'alimento', 'PICKUP', 0.4, 'ceramica', 'superficie', [cil(0.1, 0.09, 0.014, c=WHITE, m='ceramica', seg=20)] + [caja(0.07, 0.004, 0.04, x=x, y=0.016, z=z, c='#a8343a', m='comida', r=[0, a, 0]) for x, z, a in ((-0.03, 0, 10), (0.03, 0.01, -25), (0, -0.035, 50))])
obj('jarra_cerveza', 'Jarra de cerveza', 'vajilla', 'PICKUP', 0.6, 'cristal', 'superficie', [cil(0.045, 0.042, 0.15, c='#e8a62a', m='cristal'), cil(0.044, 0.044, 0.025, y=0.162, c='#fbf6ea', m='comida'), caja(0.015, 0.09, 0.03, x=0.055, y=0.08, c=GLASS, m='cristal')])
obj('cubo_botellines', 'Cubo de botellines con hielo', 'recipiente', 'CARRY', 6, 'metal', 'superficie', [cil(0.12, 0.1, 0.2, c=STEEL, m='metal', seg=18)] + [cil(0.012, 0.012, 0.09, x=x, y=0.24, z=z, c='#5a3a10', m='cristal') for x, z in ((-0.04, 0.03), (0.04, 0.02), (0, -0.05), (0.05, -0.04))])
obj('jamon_colgado', 'Jamón colgado', 'alimento', 'CARRY', 7.5, 'comida', 'techo', [
    cil(0.004, 0.004, 0.35, y=-0.175, c='#d8c8a8', m='tela'), cil(0.025, 0.02, 0.12, y=-0.41, c='#d8c8a8', m='comida'),
    cono(0.1, 0.42, y=-0.68, c='#7a3a24', m='comida'), esf(0.11, 0, -0.9, 0, c='#8a4a2c', m='comida', s=[1, 0.6, 0.8])], nota='curándose colgado del techo, sobre la barra')
obj('pizarra_tapas', 'Pizarra de tapas', 'decoracion', 'PICKUP', 3, 'madera', 'pared', [caja(0.7, 0.9, 0.025, y=1.9, z=0.0125, c='#5a3a20'), plano(0.64, 0.84, y=1.9, z=0.027, tex={'tipo': 'pizarra', 'lineas': ['TAPAS', 'Tortilla  2,00', 'Ensaladilla  2,00', 'Croquetas  2,50', 'Migas  3,00', 'Pringá  2,50', 'Pinchito  2,00']})])
obj('papel_suelo', 'Servilletas tiradas al suelo', 'papel', 'PICKUP', 0.02, 'papel', 'suelo', [esf(0.02, x, 0.012, z, c='#f4f2ec', m='papel', s=[1.3, 0.5, 1]) for x, z in ((-0.06, 0.02), (0.05, -0.03), (0.0, 0.05))], nota='las servilletas al suelo, como en todo bar que se precie')

json.dump({'version': 1, 'familia': 'hostelería', 'objetos': OUT}, open(os.path.join(ROOT, 'data', 'objetos', 'hosteleria.json'), 'w'), ensure_ascii=False, indent=1)
print('objetos de hostelería:', len(OUT))
