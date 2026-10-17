# The kits of the rooms of a home (technical backlog, epic I: vivienda por estancia): each room of a neighbour's house
# (src/houses.js) is furnished from the kit of its kind, the size of the room, from the door one comes in by, round its
# doors and windows, and for its household: an entry with `perfil` or `estilo` only in the houses of those neighbours or
# those styles («!x» leaves them out), one with `botin` only where the household has that thing to take (and what it
# lays down is the loot). Standalone (the validator) every entry is laid out. Writes data/kits/vivienda_<estancia>.json.
#   python3 tools/interiores/kits_vivienda.py
import json, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
MOOD = json.load(open(os.path.join(os.path.dirname(__file__), 'moodboard_vivienda.json')))
VIEJOS = ['abuela', 'matrimonio']
NO_VIEJOS = ['!abuela', '!matrimonio']
MODERNOS = ['moderno', 'lujo', 'joven']

def E(zona, regla, obj=None, **k):
    e = {'zona': zona, 'regla': regla}
    if isinstance(obj, list): e['variantes'] = obj
    elif obj: e['obj'] = obj
    e.update(k)
    return e

def kit(id, tipologia, nombre, nota, superficie, objetos, minimo, extra=None):
    K = {'tipologia': tipologia, 'nombre': nombre, 'nota': nota, 'superficie': superficie, 'variables': {}, 'paso_libre': 0.8,
         'zonas': [{'id': 'estancia', 'publica': True, 'rect': ['-W/2', '0', 'W/2', 'D']}], 'tabiques': [], 'objetos': objetos,
         'iluminacion': {'fuentes': [1, 3], 'temperatura_k': [2700, 3000], 'minimo_lux_publico': 60},
         'ambiente': {'sonido': 'casa', 'vida': ['las cosas de la familia a la vista'], 'horario_defecto': 'Mo-Su 00:00-24:00'},
         'minimo_objetos_distintos': minimo, 'moodboard': MOOD[id]}
    K.update(extra or {})
    json.dump(K, open(os.path.join(ROOT, 'data', 'kits', 'vivienda_' + id + '.json'), 'w'), ensure_ascii=False, indent=1)
    return K

# ---------------------------------------------------------------- the sitting room (salón)
# The telly against a wall; across from it the sofa (the young and the families) or, in the old couples' and widows' houses,
# the mesa camilla with its chairs and the wing chair; the bookcase, the sideboard with the good things on it, the china
# cabinet of the old houses, the fireplace of the rustic ones, the hunter's trophies, the musician's piano; pictures on
# the walls (the Virgin in the old houses, posters in the young ones) and the life on the tables.
SOFAS = ['sofa_tres_plazas', 'sofa_dos_plazas']
TELE = ['mueble_tv', 'mueble_tv_pequeno']
MESAS = ['mesa_centro', 'mesa_centro_cristal', 'mesa_camilla']
VIDA_MESA = ['frutero', 'jarron_flores', 'revista', 'periodico', 'mando_tele', 'cenicero', 'libro_tumbado', 'velas']
ADORNOS = ['figura_porcelana', 'portarretratos', 'jarron_flores', 'reloj_sobremesa', 'velas', 'figura_toro', 'lampara_mesa']
salon = [
    # the telly and what stands across from it
    E('estancia', 'contra_pared', 'mueble_tv_pequeno', pared='*', cantidad=[1, 1], perfil=VIEJOS),
    E('estancia', 'contra_pared', 'mueble_tv', pared='*', cantidad=[1, 1], perfil=NO_VIEJOS, obligatorio=True),
    E('estancia', 'sobre', 'televisor_tubo', en=TELE, cantidad=[1, 1], perfil=VIEJOS),
    E('estancia', 'sobre', 'televisor_plano', en=TELE, cantidad=[1, 1], perfil=NO_VIEJOS, obligatorio=True),
    E('estancia', 'enfrente', SOFAS, de=TELE, cantidad=[1, 1], perfil=NO_VIEJOS, obligatorio=True),
    E('estancia', 'entre', 'alfombra_salon', a=SOFAS, b=TELE, perfil=NO_VIEJOS),
    E('estancia', 'entre', 'mesa_centro_cristal', a=SOFAS, b=TELE, estilo=MODERNOS, perfil=NO_VIEJOS),
    E('estancia', 'entre', 'mesa_centro', a=SOFAS, b=TELE, estilo=['!moderno', '!lujo', '!joven'], perfil=NO_VIEJOS),
    E('estancia', 'conjunto', 'mesa_camilla', sillas={'variantes': ['silla_comedor'], 'n': [2, 3]}, cantidad=[1, 1], perfil=VIEJOS),
    E('estancia', 'contra_pared', 'sillon_orejero', pared='*', cantidad=[1, 1], perfil=VIEJOS + ['cazador', 'agricultor']),
    E('estancia', 'contra_pared', ['estanteria_libros', 'estanteria_libros_ancha'], pared='*', cantidad=[1, 1], obligatorio=True),
    E('estancia', 'contra_pared', 'sillon_moderno', pared='*', cantidad=[0, 1], perfil=['!abuela', '!matrimonio', '!cazador', '!agricultor']),
    # the hearth, the music
    E('estancia', 'contra_pared', 'chimenea', pared='*', cantidad=[0, 1], estilo=['rustico']),
    E('estancia', 'contra_pared', 'piano_pared', pared='*', cantidad=[1, 1], perfil=['musico']),
    E('estancia', 'esquina', 'guitarra_soporte', cantidad=[0, 1], botin='guitarra'),
    # storage and display
    E('estancia', 'sobre', ['hilera_libros_a', 'hilera_libros_b', 'hilera_libros_c', 'hilera_libros_d', 'hilera_libros_e', 'hilera_libros_f'], en=['estanteria_libros', 'estanteria_libros_ancha'], relleno=[0.55, 0.95], obligatorio=True),
    E('estancia', 'sobre', ['libro_tumbado', 'portarretratos', 'figura_porcelana'], en=['estanteria_libros', 'estanteria_libros_ancha'], cantidad=[1, 3]),
    E('estancia', 'contra_pared', 'aparador', pared='*', cantidad=[0, 1]),
    E('estancia', 'contra_pared', 'vitrina_salon', pared='*', cantidad=[0, 1], perfil=VIEJOS + ['rico']),
    E('estancia', 'contra_pared', 'mesita_auxiliar', pared='*', cantidad=[0, 1]),
    E('estancia', 'esquina', ['planta_maceta_salon', 'planta_grande'], cantidad=[0, 1]),
    E('estancia', 'esquina', 'lampara_pie', cantidad=[0, 1], perfil=NO_VIEJOS),
    E('estancia', 'suelo_libre', 'puff', cantidad=[0, 1], estilo=['joven', 'alegre', 'bohemio']),
    # on the walls
    E('estancia', 'pared', 'cuadro_oleo', pared='*', cantidad=[0, 1], botin='cuadro'),
    E('estancia', 'pared', 'cuadro_virgen', pared='*', cantidad=[1, 1], perfil=VIEJOS),
    E('estancia', 'pared', 'poster_enmarcado', pared='*', cantidad=[1, 2], estilo=['joven']),
    E('estancia', 'pared', 'cabeza_ciervo', pared='*', cantidad=[1, 2], perfil=['cazador']),
    E('estancia', 'pared', ['fotos_familia', 'cuadro_paisaje', 'cuadro_foto_antigua', 'plato_pared'], pared='*', cantidad=[2, 3], todas=True, obligatorio=True),
    E('estancia', 'pared', 'reloj_pared', pared='*', cantidad=[0, 1]),
    E('estancia', 'pared', 'espejo_salon', pared='*', cantidad=[0, 1]),
    # the life on the tables and the shelves
    E('estancia', 'sobre', 'tapete_ganchillo', en=MESAS + ['aparador'], cantidad=[1, 1], perfil=VIEJOS),
    E('estancia', 'sobre', 'cartera', en=MESAS + ['aparador', 'mesita_auxiliar', 'mueble_tv', 'mueble_tv_pequeno'], cantidad=[0, 1], botin='cartera'),
    E('estancia', 'sobre', 'movil', en=MESAS + ['aparador', 'mesita_auxiliar', 'mueble_tv', 'mueble_tv_pequeno'], cantidad=[0, 1], botin='movil'),
    E('estancia', 'sobre', 'consola_videojuegos', en=TELE + MESAS + ['mesita_auxiliar', 'aparador'], cantidad=[0, 1], botin='consola'),
    E('estancia', 'sobre', 'radio_antigua', en=TELE + ['aparador', 'mesita_auxiliar'], cantidad=[0, 1], perfil=VIEJOS),
    E('estancia', 'vida', VIDA_MESA, en=MESAS + ['aparador', 'mesita_auxiliar'], por_soporte=[2, 4], obligatorio=True),
    E('estancia', 'vida', ADORNOS, en=['aparador', 'chimenea', 'piano_pared', 'mesita_auxiliar'], por_soporte=[2, 4]),
    E('estancia', 'sobre', 'telefono_casa', en=['mesita_auxiliar', 'aparador'], cantidad=[0, 1]),
    E('estancia', 'vida', ['manta_doblada', 'cojin_suelto'], en=SOFAS, por_soporte=[1, 2], fraccion=[0.5, 0.9]),
    # the ceiling
    E('estancia', 'techo', 'lampara_arana', por_m2=[0.06, 0.09], estilo=['lujo', 'antiguo']),
    E('estancia', 'techo', 'lampara_techo_salon', por_m2=[0.06, 0.09], estilo=['!lujo', '!antiguo'], obligatorio=True),
]
kit('salon', 'salon', 'Salón de una casa del pueblo',
    'El salón de las casas de Guareña: la tele y, enfrente, el sofá o la mesa camilla con sus sillas; la estantería de libros, el aparador con las cosas buenas, la vitrina de la vajilla en las casas de los mayores, la lumbre en las rústicas; fotos de la familia, la Virgen o los pósteres según quién viva, y la vida encima de las mesas.',
    {'ancho': [3.3, 7.8], 'fondo': [3.4, 4.8], 'alto': 2.75}, salon, 60)
print('kits de la vivienda: salón')
