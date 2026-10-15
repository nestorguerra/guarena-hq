# The objects of a home in Guareña (technical backlog, I-02 and X-01/X-02): the furniture and the things of each room
# of the neighbours' houses — each a few primitives in metres, with its class of interaction, mass, material, what it
# stands on, and its part in the life of the house (rol: where people sit, sleep, eat or cook, the telly that is
# switched on, the wardrobe to hide in, the drawers to search…; src/houses.js reads it). The fabrics and the wood of a
# piece marked tinte take the colours of the house's style. The script is the model: it writes data/objetos/vivienda.json.
# Frame of an object: x across, y up from its foot, z out of its front (+z faces whoever uses it; its back at -z).
#   python3 tools/interiores/catalogo_vivienda.py
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

# (default colours: what a piece looks like out of a house; inside one, tinte takes the household's)
TELA, TELA2, MADERA, MADERA_C, BLANCO, NEGRO, METAL, CRISTAL, LATON = '#7a3a34', '#8a6a4a', '#6a4630', '#b8916a', '#efece4', '#2c2c2e', '#a8acb0', '#c8dce2', '#c8a860'
def patas(w, d, h, grosor=0.04, c=MADERA, m='madera', inset=0.05, **k):
    return [caja(grosor, h, grosor, x=sx * (w / 2 - inset), y=h / 2, z=sz * (d / 2 - inset), c=c, m=m, **k) for sx in (-1, 1) for sz in (-1, 1)]

# ---------------------------------------------------------------- sitting
def sofa(id, nombre, w, plazas, masa):
    partes = [caja(w, 0.12, 0.84, y=0.06, c=MADERA, tinte='madera'),
              caja(w, 0.3, 0.84, y=0.27, c=TELA, m='tela', tinte='tela'),
              caja(w - 0.36, 0.06, 0.62, y=0.45, z=0.08, c=TELA, m='tela', tinte='tela'),
              caja(w, 0.46, 0.2, y=0.65, z=-0.32, c=TELA, m='tela', tinte='tela'),
              caja(0.18, 0.26, 0.84, x=-w / 2 + 0.09, y=0.55, c=TELA, m='tela', tinte='tela'),
              caja(0.18, 0.26, 0.84, x=w / 2 - 0.09, y=0.55, c=TELA, m='tela', tinte='tela')]
    for i in range(plazas):
        x = -((w - 0.36) / 2) + (w - 0.36) * (i + 0.5) / plazas
        partes.append(caja((w - 0.36) / plazas - 0.04, 0.34, 0.12, x=x, y=0.66, z=-0.17, c=TELA2, m='tela', r=[-8, 0, 0]))
    asientos = [{'p': [-((w - 0.36) / 2) + (w - 0.36) * (i + 0.5) / plazas, 0.45, 0.12], 'h': 0.45, 'anim': 'sofa'} for i in range(plazas)]
    obj(id, nombre, 'sofa', 'PUSH', masa, 'tela', 'suelo', partes, rol='sofa', modificadores=['SEAT'], asientos=asientos,
        superficies=[{'y': 0.48, 'margen': 0.2}], nota='el sofá: la gente de la casa se sienta aquí a ver la tele')
sofa('sofa_tres_plazas', 'Sofá de tres plazas', 2.0, 3, 55)
sofa('sofa_dos_plazas', 'Sofá de dos plazas', 1.5, 2, 40)
obj('sillon_orejero', 'Sillón orejero', 'sillon', 'CARRY', 22, 'tela', 'suelo', [
    *patas(0.78, 0.78, 0.12, c=MADERA, tinte='madera'),
    caja(0.78, 0.3, 0.78, y=0.27, c=TELA, m='tela', tinte='tela'), caja(0.7, 0.75, 0.16, y=0.79, z=-0.3, c=TELA, m='tela', tinte='tela'),
    caja(0.14, 0.32, 0.7, x=-0.32, y=0.58, c=TELA, m='tela', tinte='tela'), caja(0.14, 0.32, 0.7, x=0.32, y=0.58, c=TELA, m='tela', tinte='tela'),
    caja(0.12, 0.3, 0.2, x=-0.3, y=1.0, z=-0.22, c=TELA, m='tela', tinte='tela'), caja(0.12, 0.3, 0.2, x=0.3, y=1.0, z=-0.22, c=TELA, m='tela', tinte='tela')],
    rol='sillon', modificadores=['SEAT'], asientos=[{'p': [0, 0.43, 0.08], 'h': 0.43, 'anim': 'sofa'}], nota='el de la abuela, junto a la ventana')
obj('sillon_moderno', 'Sillón tapizado', 'sillon', 'CARRY', 16, 'tela', 'suelo', [
    *patas(0.74, 0.74, 0.14, grosor=0.03, c=METAL, m='metal'),
    caja(0.74, 0.26, 0.74, y=0.27, c=TELA, m='tela', tinte='tela'), caja(0.74, 0.42, 0.14, y=0.61, z=-0.3, c=TELA, m='tela', tinte='tela'),
    caja(0.1, 0.2, 0.68, x=-0.32, y=0.5, c=TELA, m='tela', tinte='tela'), caja(0.1, 0.2, 0.68, x=0.32, y=0.5, c=TELA, m='tela', tinte='tela')],
    rol='sillon', modificadores=['SEAT'], asientos=[{'p': [0, 0.42, 0.06], 'h': 0.42, 'anim': 'sofa'}])
obj('silla_comedor', 'Silla de comedor', 'silla', 'CARRY', 5, 'madera', 'suelo', [
    *patas(0.44, 0.44, 0.44, grosor=0.035, c=MADERA, tinte='madera'),
    caja(0.44, 0.04, 0.44, y=0.46, c=MADERA, tinte='madera'), caja(0.4, 0.03, 0.4, y=0.495, c=TELA2, m='tela', tinte='tela'),
    caja(0.035, 0.5, 0.035, x=-0.2, y=0.73, z=-0.2, c=MADERA, tinte='madera'), caja(0.035, 0.5, 0.035, x=0.2, y=0.73, z=-0.2, c=MADERA, tinte='madera'),
    caja(0.42, 0.14, 0.025, y=0.88, z=-0.2, c=MADERA, tinte='madera')],
    rol='silla', modificadores=['SEAT'], asientos=[{'p': [0, 0.5, 0.02], 'h': 0.5, 'anim': 'silla'}])
obj('puff', 'Puf', 'sillon', 'CARRY', 8, 'tela', 'suelo', [cil(0.26, 0.26, 0.4, c=TELA, m='tela', tinte='tela', seg=14)], modificadores=['SEAT'], asientos=[{'p': [0, 0.4, 0], 'h': 0.4, 'anim': 'silla'}])

# ---------------------------------------------------------------- tables
obj('mesa_centro', 'Mesa de centro', 'mesa', 'CARRY', 14, 'madera', 'suelo', [
    *patas(1.0, 0.55, 0.4, c=MADERA, tinte='madera'), caja(1.0, 0.04, 0.55, y=0.42, c=MADERA, tinte='madera'), caja(0.9, 0.02, 0.45, y=0.12, c=MADERA, tinte='madera')],
    rol='mesa', superficies=[{'y': 0.44, 'margen': 0.04}])
obj('mesa_centro_cristal', 'Mesa de centro de cristal', 'mesa', 'CARRY', 18, 'cristal', 'suelo', [
    *patas(1.1, 0.6, 0.4, grosor=0.03, c=METAL, m='metal'), caja(1.1, 0.02, 0.6, y=0.41, c=CRISTAL, m='cristal')],
    rol='mesa', superficies=[{'y': 0.42, 'margen': 0.04}])
obj('mesa_camilla', 'Mesa camilla con faldas', 'mesa', 'CARRY', 16, 'tela', 'suelo', [
    cil(0.55, 0.62, 0.72, y=0.36, c=TELA, m='tela', tinte='tela', seg=20), cil(0.56, 0.56, 0.03, y=0.735, c=BLANCO, m='tela', seg=20)],
    rol='mesa', superficies=[{'y': 0.75, 'margen': 0.06}], nota='con el brasero debajo, como en las casas de antes')
obj('mesita_auxiliar', 'Mesita auxiliar', 'mesita', 'CARRY', 6, 'madera', 'suelo', [
    *patas(0.45, 0.45, 0.55, grosor=0.03, c=MADERA, tinte='madera'), caja(0.45, 0.03, 0.45, y=0.565, c=MADERA, tinte='madera')],
    superficies=[{'y': 0.58, 'margen': 0.03}])

# ---------------------------------------------------------------- the telly and the furniture round it
obj('mueble_tv', 'Mueble de la tele', 'mueble', 'PUSH', 35, 'madera', 'suelo', [
    caja(1.6, 0.48, 0.45, y=0.24, c=MADERA, tinte='madera'), caja(1.6, 0.02, 0.46, y=0.49, c=MADERA, tinte='madera'),
    caja(0.7, 0.3, 0.01, x=-0.4, y=0.24, z=0.226, c=MADERA_C, tinte='madera'), caja(0.7, 0.3, 0.01, x=0.4, y=0.24, z=0.226, c=MADERA_C, tinte='madera')],
    superficies=[{'y': 0.5, 'margen': 0.03}])
obj('mueble_tv_pequeno', 'Mesa de la tele', 'mueble', 'CARRY', 18, 'madera', 'suelo', [
    *patas(1.0, 0.5, 0.55, c=MADERA, tinte='madera'), caja(1.0, 0.03, 0.5, y=0.565, c=MADERA, tinte='madera'), caja(0.92, 0.02, 0.44, y=0.15, c=MADERA, tinte='madera')],
    superficies=[{'y': 0.58, 'margen': 0.03}])
obj('televisor_plano', 'Televisor de pantalla plana', 'televisor', 'CARRY', 12, 'plastico', 'superficie', [
    caja(0.32, 0.02, 0.2, y=0.01, c=NEGRO, m='plastico'), caja(0.06, 0.08, 0.04, y=0.06, c=NEGRO, m='plastico'),
    caja(1.24, 0.72, 0.05, y=0.46, c=NEGRO, m='plastico'), caja(1.18, 0.66, 0.006, y=0.46, z=0.028, c='#262a30', m='cristal', aparte=True)],
    rol='tv', modificadores=['USE'])
obj('televisor_tubo', 'Televisor de tubo', 'televisor', 'PUSH', 28, 'plastico', 'superficie', [
    caja(0.62, 0.5, 0.4, y=0.25, c='#3a3632', m='plastico'), caja(0.44, 0.34, 0.008, x=-0.05, y=0.27, z=0.202, c='#262a30', m='cristal', aparte=True),
    caja(0.09, 0.26, 0.01, x=0.23, y=0.27, z=0.202, c='#2e2c2a', m='plastico'), cil(0.004, 0.004, 0.35, x=-0.1, y=0.7, c=METAL, r=[0, 0, 30]), cil(0.004, 0.004, 0.35, x=0.1, y=0.7, c=METAL, r=[0, 0, -30])],
    rol='tv', modificadores=['USE'], nota='con su antena de cuernos')
obj('consola_videojuegos', 'Videoconsola', 'informatica', 'PICKUP', 3, 'plastico', 'superficie', [caja(0.3, 0.07, 0.24, c=NEGRO, m='plastico'), caja(0.14, 0.04, 0.09, x=0.28, y=0.02, c=NEGRO, m='plastico')])
obj('mando_tele', 'Mando de la tele', 'pequeño_electrodomestico', 'PICKUP', 0.6, 'plastico', 'superficie', [caja(0.05, 0.022, 0.17, c=NEGRO, m='plastico')], motivo_clase='un mando: PICKUP aunque su categoría pesa más')
obj('radio_antigua', 'Radio antigua', 'pequeño_electrodomestico', 'PICKUP', 3, 'madera', 'superficie', [caja(0.36, 0.22, 0.16, c='#6a4630'), caja(0.2, 0.12, 0.005, x=-0.06, y=0.12, z=0.081, c='#d8c8a0', m='tela'), cil(0.02, 0.02, 0.01, x=0.12, y=0.1, z=0.085, c=LATON, r=[90, 0, 0])])

# ---------------------------------------------------------------- storage and display
obj('aparador', 'Aparador', 'mueble', 'PUSH', 60, 'madera', 'suelo', [
    *patas(1.6, 0.45, 0.12, c=MADERA, tinte='madera'), caja(1.6, 0.7, 0.45, y=0.47, c=MADERA, tinte='madera'), caja(1.62, 0.03, 0.47, y=0.835, c=MADERA, tinte='madera'),
    *[caja(0.48, 0.18, 0.01, x=x, y=0.7, z=0.226, c=MADERA_C, tinte='madera') for x in (-0.52, 0, 0.52)],
    *[caja(0.48, 0.4, 0.01, x=x, y=0.36, z=0.226, c=MADERA_C, tinte='madera') for x in (-0.52, 0, 0.52)],
    *[cil(0.012, 0.012, 0.02, x=x, y=0.7, z=0.235, c=LATON, r=[90, 0, 0]) for x in (-0.52, 0, 0.52)]],
    rol='comoda', superficies=[{'y': 0.85, 'margen': 0.03}], nota='los cajones con los papeles, la plata y lo que haya')
obj('vitrina_salon', 'Vitrina con la vajilla buena', 'estanteria', 'PUSH', 70, 'madera', 'suelo', [
    caja(1.1, 0.8, 0.42, y=0.4, c=MADERA, tinte='madera'), caja(1.1, 1.1, 0.04, y=1.35, z=-0.19, c=MADERA, tinte='madera'),
    caja(0.04, 1.1, 0.42, x=-0.53, y=1.35, c=MADERA, tinte='madera'), caja(0.04, 1.1, 0.42, x=0.53, y=1.35, c=MADERA, tinte='madera'), caja(1.1, 0.06, 0.44, y=1.93, c=MADERA, tinte='madera'),
    caja(1.02, 0.02, 0.36, y=1.32, c=MADERA_C, tinte='madera'), caja(1.02, 1.04, 0.01, y=1.35, z=0.205, c=CRISTAL, m='cristal'),
    *[cil(0.1, 0.1, 0.012, x=x, y=yy, z=-0.12, c=BLANCO, m='ceramica', r=[80, 0, 0]) for x in (-0.3, 0, 0.3) for yy in (0.95, 1.45)],
    *[cil(0.03, 0.025, 0.1, x=x, y=1.38, z=0.06, c=CRISTAL, m='cristal') for x in (-0.36, -0.24, 0.24, 0.36)]],
    nota='los platos de la boda y las copas que no se usan nunca')
def estanteria(id, nombre, w, masa):
    ys = [0.04, 0.42, 0.8, 1.18, 1.56]
    partes = [caja(w, 1.9, 0.02, y=0.95, z=-0.15, c=MADERA, tinte='madera'), caja(0.03, 1.9, 0.32, x=-w / 2 + 0.015, y=0.95, c=MADERA, tinte='madera'), caja(0.03, 1.9, 0.32, x=w / 2 - 0.015, y=0.95, c=MADERA, tinte='madera'), caja(w, 0.03, 0.32, y=1.885, c=MADERA, tinte='madera')]
    partes += [caja(w - 0.06, 0.02, 0.3, y=y - 0.01, z=0.005, c=MADERA, tinte='madera') for y in ys]
    obj(id, nombre, 'estanteria', 'PUSH', masa, 'madera', 'suelo', partes, rol='libros', superficies=[{'y': y, 'fondo': 0.28} for y in ys])
estanteria('estanteria_libros', 'Estantería de libros', 0.9, 38)
estanteria('estanteria_libros_ancha', 'Librería', 1.4, 55)
COLS = ['#7a2a2a', '#2a3a5a', '#3a5a3a', '#c8a860', '#5a3a2a', '#e8e0c8', '#4a2a4a', '#2a2a2e', '#8a6a3a', '#3a6a7a']
for k in range(6):
    bk, x, partes = COLS[k:] + COLS[:k], -0.12, []
    for j in range(7):
        w, h = 0.025 + (j * 7 + k) % 3 * 0.008, 0.2 + ((j * 5 + k * 3) % 5) * 0.025
        partes.append(caja(w, h, 0.17 + (j % 2) * 0.03, x=x + w / 2, y=h / 2, c=bk[j % len(bk)], m='papel'))
        x += w + 0.003
    obj(f'hilera_libros_{"abcdef"[k]}', 'Libros en fila', 'decoracion', 'PICKUP', 2.5, 'papel', 'superficie', partes)
obj('libro_tumbado', 'Libros apilados', 'decoracion', 'PICKUP', 1.5, 'papel', 'superficie', [caja(0.24, 0.03, 0.17, y=0.015, c='#2a3a5a', m='papel'), caja(0.22, 0.03, 0.16, y=0.045, c='#7a2a2a', m='papel', r=[0, 8, 0]), caja(0.2, 0.025, 0.15, y=0.0725, c='#c8a860', m='papel', r=[0, -5, 0])])

# ---------------------------------------------------------------- light
obj('lampara_pie', 'Lámpara de pie', 'lampara', 'PICKUP', 4, 'metal', 'suelo', [
    cil(0.16, 0.18, 0.03, y=0.015, c=LATON, seg=16), cil(0.012, 0.012, 1.4, y=0.72, c=LATON), cono(0.22, 0.28, y=1.5, c='#efe4c8', m='tela', seg=16), esf(0.05, 0, 1.42, 0, c='#fff3d6', m='cristal', luz=True)])
obj('lampara_mesa', 'Lámpara de mesa', 'lampara', 'PICKUP', 1.8, 'ceramica', 'superficie', [
    cil(0.07, 0.09, 0.22, y=0.11, c='#c8b8a0', m='ceramica', seg=14), cil(0.006, 0.006, 0.1, y=0.27, c=LATON), cono(0.15, 0.18, y=0.39, c='#efe4c8', m='tela', seg=16), esf(0.035, 0, 0.33, 0, c='#fff3d6', m='cristal', luz=True)])
obj('lampara_techo_salon', 'Lámpara de techo', 'lampara', 'FIXED', 2.5, 'cristal', 'techo', [
    cil(0.004, 0.004, 0.45, y=-0.225, c=LATON), cil(0.06, 0.06, 0.04, y=-0.02, c=LATON), esf(0.2, 0, -0.62, 0, c='#f2ead8', m='cristal', s=[1, 0.6, 1]), esf(0.05, 0, -0.58, 0, c='#fff3d6', m='cristal', luz=True)],
    motivo_fijo='anclado en la realidad')
obj('lampara_arana', 'Lámpara de araña', 'lampara', 'FIXED', 6, 'cristal', 'techo', [
    cil(0.004, 0.004, 0.4, y=-0.2, c=LATON), cil(0.05, 0.08, 0.14, y=-0.47, c=LATON),
    *[cil(0.008, 0.008, 0.3, x=0.14 * dx, y=-0.55, z=0.14 * dz, c=LATON, r=[0, 0, 90]) for dx, dz in ((1, 0), (-1, 0))],
    *[esf(0.035, 0.28 * dx, -0.5, 0.28 * dz, c='#fff3d6', m='cristal', luz=True) for dx, dz in ((1, 0), (-1, 0), (0, 1), (0, -1))],
    *[cono(0.015, 0.08, x=0.22 * dx, y=-0.68, z=0.22 * dz, c=CRISTAL, m='cristal') for dx, dz in ((1, 0), (-1, 0), (0, 1), (0, -1))]],
    motivo_fijo='anclado en la realidad')

# ---------------------------------------------------------------- on the walls
obj('espejo_salon', 'Espejo con marco', 'espejo', 'CARRY', 7, 'cristal', 'pared', [caja(0.7, 0.95, 0.03, y=1.6, z=0.015, c=LATON, m='madera'), caja(0.6, 0.85, 0.006, y=1.6, z=0.033, c='#c8d2d6', m='metal')], rol='espejo')
obj('cuadro_virgen', 'Estampa de la Virgen', 'cuadro', 'PICKUP', 1.2, 'madera', 'pared', [caja(0.46, 0.56, 0.02, y=1.65, z=0.01, c=LATON), plano(0.42, 0.52, y=1.65, z=0.021, tex={'tipo': 'virgen'})])
obj('cuadro_oleo', 'Cuadro al óleo', 'cuadro', 'CARRY', 5, 'madera', 'pared', [caja(0.82, 0.62, 0.035, y=1.65, z=0.0175, c='#8a6a30'), plano(0.74, 0.54, y=1.65, z=0.036, tex={'tipo': 'paisaje'})], nota='el bueno: puede valer un dinero')
obj('poster_enmarcado', 'Póster enmarcado', 'cuadro', 'PICKUP', 1, 'papel', 'pared', [caja(0.52, 0.72, 0.015, y=1.6, z=0.0075, c=NEGRO, m='plastico'), plano(0.48, 0.68, y=1.6, z=0.016, tex={'tipo': 'cartel_fiesta'})])
obj('fotos_familia', 'Fotos de la familia', 'cuadro', 'PICKUP', 1, 'madera', 'pared', [
    *[caja(0.2, 0.26, 0.015, x=x, y=1.5 + dy, z=0.0075, c=LATON) for x, dy in ((-0.24, 0.06), (0, -0.04), (0.24, 0.08))],
    *[plano(0.17, 0.22, x=x, y=1.5 + dy, z=0.016, tex={'tipo': 'foto'}) for x, dy in ((-0.24, 0.06), (0, -0.04), (0.24, 0.08))]],
    nota='la boda, la comunión y el nieto en la mili')
obj('plato_pared', 'Platos de cerámica colgados', 'decoracion', 'PICKUP', 2, 'ceramica', 'pared', [
    *[cil(0.13, 0.13, 0.015, x=x, y=1.85, z=0.008, c=c, m='ceramica', r=[90, 0, 0], seg=20) for x, c in ((-0.3, '#2a5a8a'), (0, '#c8a040'), (0.3, '#3a7a5a'))]],
    nota='de Talavera, recuerdo de un viaje')

# ---------------------------------------------------------------- the hearth and the music
obj('chimenea', 'Chimenea de leña', 'obra', 'FIXED', 600, 'piedra', 'suelo', [
    caja(1.3, 0.12, 0.5, y=0.06, c='#9a9088', m='piedra'), caja(0.2, 1.0, 0.5, x=-0.55, y=0.5, c='#c8beb2', m='piedra'), caja(0.2, 1.0, 0.5, x=0.55, y=0.5, c='#c8beb2', m='piedra'),
    caja(1.4, 0.14, 0.56, y=1.07, c=MADERA, tinte='madera'), caja(0.9, 0.8, 0.06, y=0.52, z=-0.22, c='#3a3634', m='piedra'),
    caja(0.5, 0.06, 0.08, y=0.16, z=0.0, c='#5a3a20', r=[0, 20, 0]), caja(0.5, 0.06, 0.08, y=0.2, z=0.02, c='#4a3018', r=[0, -15, 0]), esf(0.12, 0, 0.2, 0, c='#e87a2a', m='comida', luz=True, s=[1.6, 0.5, 0.8])],
    rol='chimenea', motivo_fijo='estructural', superficies=[{'y': 1.14, 'margen': 0.04}], nota='la lumbre de las noches de invierno')
obj('piano_pared', 'Piano de pared', 'instrumento', 'PUSH_HEAVY', 210, 'madera', 'suelo', [
    caja(1.45, 1.2, 0.55, y=0.6, z=-0.05, c='#2c2622'), caja(1.45, 0.06, 0.62, y=0.72, z=0.01, c='#2c2622'), caja(1.3, 0.03, 0.15, y=0.735, z=0.2, c='#efece4', m='plastico'),
    *[caja(0.012, 0.018, 0.09, x=-0.6 + i * 0.05, y=0.755, z=0.18, c=NEGRO, m='plastico') for i in range(25) if i % 7 not in (2, 6)],
    caja(0.06, 0.66, 0.06, x=-0.65, y=0.33, z=0.22, c='#2c2622'), caja(0.06, 0.66, 0.06, x=0.65, y=0.33, z=0.22, c='#2c2622')],
    rol='piano', modificadores=['USE'], superficies=[{'y': 1.2, 'margen': 0.05}])
obj('banqueta_piano', 'Banqueta del piano', 'sillon', 'CARRY', 9, 'madera', 'suelo', [*patas(0.6, 0.34, 0.46, c='#2c2622'), caja(0.6, 0.06, 0.34, y=0.49, c='#2a2a2e', m='tela')],
    modificadores=['SEAT'], asientos=[{'p': [0, 0.52, 0], 'h': 0.52, 'anim': 'silla'}])
obj('guitarra_soporte', 'Guitarra en su soporte', 'instrumento', 'PICKUP', 3.5, 'madera', 'suelo', [
    caja(0.3, 0.02, 0.3, y=0.01, c=NEGRO, m='metal'), cil(0.008, 0.008, 0.5, y=0.25, z=-0.08, c=NEGRO, r=[-15, 0, 0]),
    esf(0.19, 0, 0.32, 0, c='#b8783a', m='madera', s=[1, 1.15, 0.28]), esf(0.15, 0, 0.6, 0, c='#b8783a', m='madera', s=[1, 1.05, 0.28]), caja(0.05, 0.52, 0.03, y=0.95, z=0.01, c='#3a2418'), caja(0.07, 0.14, 0.04, y=1.27, z=0.01, c='#3a2418')],
    rol='guitarra', modificadores=['USE'])

# ---------------------------------------------------------------- the small things of the room
obj('frutero', 'Frutero con fruta', 'alimento', 'PICKUP', 1.5, 'ceramica', 'superficie', [cil(0.15, 0.08, 0.07, c='#e8dcc4', m='ceramica', seg=16), esf(0.04, -0.05, 0.08, 0.02, c='#d8302a'), esf(0.04, 0.05, 0.08, -0.02, c='#e8a020'), esf(0.038, 0, 0.09, 0.05, c='#9ab83a'), esf(0.035, 0.02, 0.12, -0.04, c='#d8302a')])
obj('jarron_flores', 'Jarrón con flores', 'decoracion', 'PICKUP', 1.6, 'ceramica', 'superficie', [cil(0.06, 0.08, 0.24, c='#3a5a8a', m='ceramica', seg=14), *[esf(0.035, x, 0.32 + dy, z, c=c, m='tela') for x, z, dy, c in ((-0.04, 0, 0.02, '#d8263a'), (0.04, 0.02, 0.04, '#f2d230'), (0, -0.04, 0.0, '#e87aa4'), (0.02, 0.04, 0.07, '#f4f2ec'))], cil(0.004, 0.004, 0.12, y=0.28, c='#3a7a35', m='comida')])
obj('figura_porcelana', 'Figura de porcelana', 'decoracion', 'PICKUP', 0.6, 'ceramica', 'superficie', [cil(0.04, 0.05, 0.02, c=BLANCO, m='ceramica'), cono(0.05, 0.16, y=0.1, c='#d8e0ec', m='ceramica'), esf(0.025, 0, 0.2, 0, c=BLANCO, m='ceramica')], nota='la bailarina de la abuela')
obj('figura_toro', 'Figura de un toro', 'decoracion', 'PICKUP', 0.9, 'metal', 'superficie', [caja(0.16, 0.06, 0.06, y=0.07, c='#3a3230', m='metal'), caja(0.05, 0.05, 0.05, x=0.09, y=0.09, c='#3a3230', m='metal'), *[caja(0.012, 0.05, 0.012, x=sx * 0.06, y=0.025, z=sz * 0.02, c='#3a3230', m='metal') for sx in (-1, 1) for sz in (-1, 1)]])
obj('portarretratos', 'Portarretratos', 'decoracion', 'PICKUP', 0.4, 'madera', 'superficie', [caja(0.15, 0.2, 0.015, y=0.1, z=0.0, c=LATON, r=[-12, 0, 0]), plano(0.12, 0.16, y=0.1, z=0.012, tex={'tipo': 'foto'}, r=[-12, 0, 0])])
obj('cenicero', 'Cenicero de cristal', 'decoracion', 'PICKUP', 0.5, 'cristal', 'superficie', [cil(0.07, 0.06, 0.03, c=CRISTAL, m='cristal', seg=14)])
obj('tapete_ganchillo', 'Tapete de ganchillo', 'textil', 'PICKUP', 0.1, 'tela', 'superficie', [cil(0.2, 0.2, 0.003, c='#f4f0e4', m='tela', seg=20)], nota='hecho a mano, sobre la mesa y bajo el jarrón')
obj('reloj_sobremesa', 'Reloj de sobremesa', 'reloj', 'PICKUP', 1.2, 'madera', 'superficie', [caja(0.2, 0.26, 0.09, c='#6a4630'), cil(0.07, 0.07, 0.006, y=0.16, z=0.046, c='#f4efe0', m='ceramica', r=[90, 0, 0])])
obj('manta_doblada', 'Manta doblada', 'textil', 'PICKUP', 1.2, 'tela', 'superficie', [caja(0.42, 0.08, 0.32, c='#a8603a', m='tela', tinte='tela')])
obj('cojin_suelto', 'Cojín', 'textil', 'PICKUP', 0.5, 'tela', 'superficie', [caja(0.4, 0.14, 0.38, c=TELA2, m='tela', tinte='tela', r=[0, 12, 0])])
obj('telefono_casa', 'Teléfono de casa', 'pequeño_electrodomestico', 'PICKUP', 0.8, 'plastico', 'superficie', [caja(0.2, 0.07, 0.22, c='#e8e2d4', m='plastico'), caja(0.2, 0.05, 0.06, y=0.095, z=-0.04, c='#e8e2d4', m='plastico')], rol='telefono')
obj('velas', 'Velas', 'decoracion', 'PICKUP', 0.5, 'comida', 'superficie', [cil(0.025, 0.025, 0.2, x=-0.04, c='#f4ecd8', m='comida'), cil(0.025, 0.025, 0.14, x=0.04, c='#f4ecd8', m='comida'), cil(0.07, 0.07, 0.015, c=LATON, seg=14)])
obj('alfombra_salon', 'Alfombra', 'textil', 'PICKUP', 4, 'tela', 'suelo', [caja(2.0, 0.003, 1.4, y=0.0015, c='#7a2a2a', m='tela'), caja(1.8, 0.004, 1.2, y=0.002, c='#b8784a', m='tela', tinte='tela')],
    motivo_clase='enrollada se lleva en brazos, pero pesa poco')
obj('planta_maceta_salon', 'Costilla de Adán en maceta', 'planta', 'CARRY', 9, 'ceramica', 'suelo', [cil(0.2, 0.15, 0.34, c='#b5552e', m='ceramica', seg=14), *[esf(0.18, x, 0.62 + dy, z, c='#3f7a35', m='comida', s=[1.2, 0.6, 1]) for x, z, dy in ((-0.1, 0, 0.1), (0.12, 0.06, 0.0), (0, -0.1, 0.25), (0.05, 0.1, 0.35))]])

# ---------------------------------------------------------------- what can be taken (src/houses.js LOOT)
obj('cartera', 'Cartera', 'textil', 'PICKUP', 0.2, 'tela', 'superficie', [caja(0.11, 0.025, 0.09, c='#4a3020', m='tela')])
obj('movil', 'Teléfono móvil', 'informatica', 'PICKUP', 0.3, 'plastico', 'superficie', [caja(0.08, 0.012, 0.15, c=NEGRO, m='plastico'), caja(0.07, 0.001, 0.13, y=0.0125, c='#2a3a4a', m='cristal')])

json.dump({'version': 1, 'familia': 'vivienda', 'categorias': {'sillon': [4, 40], 'mesita': [2, 15], 'televisor': [4, 45], 'instrumento': [1, 320], 'obra': [100, 3000]},
           'objetos': OUT}, open(os.path.join(ROOT, 'data', 'objetos', 'vivienda.json'), 'w'), ensure_ascii=False, indent=1)
print('objetos de la vivienda:', len(OUT))
