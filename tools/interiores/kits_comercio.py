# The three kits of the «comercio» family (technical backlog, I-02): the clothes shop, the pharmacy and the supermarket —
# written to data/kits/ropa.json, farmacia.json and supermercado.json from here, so that a rule is written once and read
# well. The objects they name are in tools/interiores/catalogo_comercio.py; the moodboards (Wikimedia Commons: page,
# author and licence, never the picture) in tools/interiores/moodboard_comercio.json.
#   python3 tools/interiores/catalogo_comercio.py && python3 tools/interiores/kits_comercio.py
import json, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
MOOD = json.load(open(os.path.join(ROOT, 'tools', 'interiores', 'moodboard_comercio.json')))

def E(zona, regla, obj=None, **k):
    d = {'zona': zona, 'regla': regla}
    if obj: d['obj'] = obj
    d.update(k)
    return d
def Z(id, rect, publica=True): return {'id': id, 'publica': publica, 'rect': rect}
def sobre(zona, variantes, en, **k):
    """On the surfaces of `en`: one object or the list of variants."""
    if isinstance(variantes, str): return E(zona, 'sobre', variantes, en=en, **k)
    return E(zona, 'sobre', variantes=variantes, en=en, **k)

def escribir(id, K):
    K['moodboard'] = [{'titulo': m['titulo'], 'url': m['url'], 'autor': m['autor'], 'licencia': m['licencia']} for m in MOOD[K.pop('_mood')]]
    json.dump(K, open(os.path.join(ROOT, 'data', 'kits', id + '.json'), 'w'), ensure_ascii=False, indent=1)
    print(id, len(K['objetos']), 'entradas')

# ================================================================== THE CLOTHES SHOP
PILAS = (['pila_jerseys_' + k for k in ('rojo', 'azul_marino', 'verde', 'mostaza', 'gris', 'crudo')] + ['pila_vaqueros_' + k for k in ('claro', 'medio', 'oscuro')]
         + ['pila_camisetas_' + k for k in ('blanca', 'negra', 'rosa', 'turquesa')] + ['pila_polos_azul', 'pila_polos_granate', 'pila_pantalones_beige', 'pila_pantalones_gris',
                                                                                          'pila_sudaderas_negra', 'pila_sudaderas_burdeos', 'bufandas_dobladas', 'gorros_lana'])
ZAPATOS = ['par_zapatos_hombre_negro', 'par_zapatos_hombre_marron', 'par_zapatos_mujer_rojo', 'par_zapatillas_blancas', 'par_zapatillas_azules', 'par_botas_marron', 'par_botas_negras', 'pila_cajas_zapatos']
BOLSOS = ['bolso_negro', 'bolso_marron', 'bolso_rojo', 'bolso_azul']
MANIQUIES = ['maniqui_vestido_rojo', 'maniqui_vestido_azul', 'maniqui_vestido_mostaza', 'maniqui_vaqueros', 'maniqui_traje', 'maniqui_abrigo']

ropa = {
    'tipologia': 'tienda_ropa', 'nombre': 'Tienda de ropa',
    'nota': 'La tienda de ropa de un pueblo de las Vegas Altas: un escaparate con maniquíes, el mostrador con la caja junto a la puerta, estanterías de pared con ropa doblada, barras con prendas colgadas, mesas de jerseys y vaqueros, '
            'zapatos y bolsos, espejos, dos probadores con cortina al fondo y un almacén pequeño. La puerta en z = 0, el fondo en z = D; x de -W/2 a W/2.',
    '_mood': 'ropa',
    'superficie': {'ancho': [6.3, 8.1], 'fondo': [8.7, 11.7], 'alto': 3.0},
    'variables': {'xc': 'W/2-1.9', 'z0': '1.7', 'z1': '4.0', 'zb': 'D-1.7'},
    'paso_libre': 0.9, 'pared': '#f1ece2', 'suelo': 'herringbone_parquet', 'suelo_color': '#d8c8ac',
    'puntos': {'dependiente': ['xc+0.8', '(z0+z1)/2'], 'mostrador': ['xc-0.75', '(z0+z1)/2']},
    'pedir': 'Pagar en caja',
    'zonas': [
        Z('entrada', ['-W/2', '0', 'W/2', '1.5']),
        Z('caja', ['xc-0.3', 'z0', 'xc+0.3', 'z1'], False),
        Z('trascaja', ['xc+0.33', 'z0', 'W/2', 'z1+0.2'], False),
        Z('frente_caja', ['xc-1.3', 'z0', 'xc-0.33', 'z1']),
        Z('sala', ['-W/2', '1.5', 'W/2', 'zb']),
        Z('probador_a', ['-W/2', 'zb', '-W/2+1.4', 'D'], False),
        Z('probador_b', ['-W/2+1.4', 'zb', '-W/2+2.8', 'D'], False),
        Z('fondo', ['-W/2+2.8', 'zb', 'W/2-2.4', 'D'], False),
        Z('almacen', ['W/2-2.4', 'zb', 'W/2', 'D'], False),
    ],
    'tabiques': [
        {'de': ['-W/2+1.4', 'zb'], 'a': ['-W/2+1.4', 'D']},
        {'de': ['-W/2+2.8', 'zb'], 'a': ['-W/2+2.8', 'D']},
        {'de': ['W/2', 'zb'], 'a': ['W/2-2.4', 'zb'], 'puerta': [0.5, 1.0]},
        {'de': ['W/2-2.4', 'zb'], 'a': ['W/2-2.4', 'D']},
    ],
    'libres': [{'rect': ['xc-1.3', 'z0', 'xc-0.3', 'z1'], 'nota': 'el sitio para pagar en el mostrador: sin muebles delante'}],
    'objetos': [
        # ---- the counter, first: the kit's own design
        E('caja', 'modulos', 'mostrador_tienda', eje='z', linea=['xc', 'z0', 'z1'], mira='-x', obligatorio=True),
        sobre('caja', 'caja_registradora', ['mostrador_tienda'], cantidad=[1, 1], obligatorio=True),
        sobre('caja', 'datafono', ['mostrador_tienda'], cantidad=[1, 1], obligatorio=True),
        sobre('caja', 'tarjetero', ['mostrador_tienda'], cantidad=[1, 1]),
        sobre('caja', 'pila_bolsas_papel', ['mostrador_tienda'], cantidad=[1, 2], obligatorio=True),
        sobre('caja', 'bolsa_papel_grande', ['mostrador_tienda'], cantidad=[0, 1]),
        sobre('caja', 'cesta_calcetines', ['mostrador_tienda'], cantidad=[0, 1]),
        sobre('caja', 'expositor_joyas', ['mostrador_tienda'], cantidad=[0, 1]),
        sobre('caja', 'rollo_papel_regalo', ['mostrador_tienda'], cantidad=[0, 1]),
        E('trascaja', 'contra_pared', 'armario_trascaja', pared='E', cantidad=[1, 1], obligatorio=True),
        sobre('trascaja', 'pila_bolsas_papel', ['armario_trascaja'], cantidad=[0, 1]),
        E('trascaja', 'pared', 'rotulo_tienda_a', variantes=['rotulo_tienda_a', 'rotulo_tienda_b', 'rotulo_tienda_c'], pared='E', cantidad=[1, 1], obligatorio=True),
        E('caja', 'techo', 'plafon_pequeno', cantidad=[1, 1], obligatorio=True),
        # ---- the fitting rooms (before the floor fills up: their curtains must leave the way in)
        E('probador_a', 'contra_pared', variantes=['cortina_probador_izq', 'cortina_probador_der'], pared='S', cantidad=[1, 1], obligatorio=True),
        E('probador_b', 'contra_pared', variantes=['cortina_probador_der', 'cortina_probador_izq'], pared='S', cantidad=[1, 1], obligatorio=True),
        E('probador_a', 'pared', 'espejo_probador', pared='N', cantidad=[1, 1], obligatorio=True),
        E('probador_b', 'pared', 'espejo_probador', pared='N', cantidad=[1, 1], obligatorio=True),
        E('probador_a', 'pared', 'gancho_probador', pared='W', cantidad=[1, 1], obligatorio=True),
        E('probador_b', 'pared', 'gancho_probador', pared='E', cantidad=[1, 1], obligatorio=True),
        E('probador_a', 'esquina', variantes=['taburete_probador', 'banqueta_probador'], cantidad=[0, 1]),
        E('probador_b', 'esquina', 'taburete_probador', cantidad=[0, 1]),
        E('probador_a', 'techo', 'plafon_pequeno', cantidad=[1, 1], obligatorio=True),
        E('probador_b', 'techo', 'plafon_pequeno', cantidad=[1, 1], obligatorio=True),
        # ---- the stockroom
        E('almacen', 'contra_pared', 'estanteria_metalica', pared='N', cantidad=[1, 2], obligatorio=True),
        sobre('almacen', ['caja_ropa_almacen', 'caja_carton'], ['estanteria_metalica'], relleno=[0.6, 0.9], todas=True, obligatorio=True),
        E('almacen', 'contra_pared', 'burra_almacen_fundas', pared='E', cantidad=[0, 1]),
        E('almacen', 'esquina', variantes=['vaporizador_ropa', 'maniqui_almacen', 'tabla_planchar'], cantidad=[1, 2], todas=True),
        E('almacen', 'esquina', 'fregona_cubo', cantidad=[0, 1]),
        E('almacen', 'esquina', 'escoba', cantidad=[0, 1]),
        E('almacen', 'suelo_libre', 'caja_ropa_almacen', cantidad=[0, 2]),
        E('almacen', 'techo', 'plafon_pequeno', cantidad=[1, 1], obligatorio=True),
        E('fondo', 'pared', 'reloj_pared', pared='N', cantidad=[0, 1]),
        E('fondo', 'pared', 'espejo_pared_grande', pared='N', cantidad=[0, 1]),
        # ---- the window and the door
        E('entrada', 'esquina', 'papelera', cantidad=[1, 1], obligatorio=True),
        E('entrada', 'contra_pared', variantes=MANIQUIES, pared='S', cantidad=[2, 3], todas=True, obligatorio=True),
        E('entrada', 'esquina', 'antena_antihurto', cantidad=[0, 2]),
        E('entrada', 'esquina', 'planta_grande', cantidad=[0, 1]),
        E('entrada', 'esquina', 'perchero', cantidad=[0, 1]),
        E('entrada', 'techo', 'lampara_panel_led', cantidad=[1, 1], obligatorio=True),
        # ---- the west wall: shelving with folded clothes, the bags, a low shelf
        # (the single pieces first: in a short shop the tall shelving fills what is left)
        E('sala', 'contra_pared', 'expositor_bolsos', pared='W', cantidad=[1, 1], obligatorio=True),
        E('sala', 'contra_pared', 'estanteria_ropa_baja', pared='W', cantidad=[1, 1], obligatorio=True),
        E('sala', 'contra_pared', 'estanteria_ropa_pared', pared='W', cantidad=[1, 3], obligatorio=True),
        sobre('sala', PILAS, ['estanteria_ropa_pared'], relleno=[0.8, 0.95], todas=True, obligatorio=True),
        sobre('sala', PILAS, ['estanteria_ropa_baja'], relleno=[0.7, 0.95], obligatorio=True),
        sobre('sala', BOLSOS, ['expositor_bolsos'], relleno=[0.7, 0.9], todas=True, obligatorio=True),
        # ---- the east wall: shoes, the big mirror, rails of hanging garments
        E('sala', 'contra_pared', 'expositor_zapatos', pared='E', cantidad=[1, 1], obligatorio=True),
        sobre('sala', ZAPATOS, ['expositor_zapatos'], relleno=[0.75, 0.95], todas=True, obligatorio=True),
        E('sala', 'pared', 'espejo_pared_grande', pared='E', cantidad=[1, 1], obligatorio=True),
        E('sala', 'pared', variantes=['burra_pared_abrigos', 'burra_pared_camisas', 'burra_pared_vestidos'], pared='E', cada=1.35, todas=True),
        E('sala', 'pared', 'aire_acondicionado_pared', pared='E', cantidad=[0, 1]),
        E('sala', 'pared', variantes=['cuadro_moda_a', 'cuadro_moda_b'], pared='W', cantidad=[0, 2], todas=True),
        E('sala', 'pared', 'cartel_rebajas', pared='E', cantidad=[0, 1]),
        # ---- the floor: central tables, racks, mannequins, mirrors, what is sold where it stands
        E('sala', 'conjunto', 'mesa_exposicion', variantes=['mesa_exposicion', 'mesa_escalonada'], cantidad=[2, 3], obligatorio=True),
        sobre('sala', PILAS, ['mesa_exposicion', 'mesa_escalonada'], por_soporte=[2, 3], obligatorio=True),
        E('sala', 'suelo_libre', variantes=['burra_suelo_abrigos', 'burra_suelo_camisas', 'burra_suelo_vestidos'], cantidad=[2, 3], todas=True, obligatorio=True),
        E('sala', 'suelo_libre', variantes=MANIQUIES[::-1], cantidad=[1, 2], todas=True),
        E('sala', 'suelo_libre', 'espejo_pie', cantidad=[1, 1], obligatorio=True),
        E('sala', 'suelo_libre', 'cesta_ofertas', cantidad=[1, 1]),
        E('sala', 'suelo_libre', variantes=['expositor_calcetines', 'expositor_bufandas', 'perchero_chaquetas'], cantidad=[1, 2], todas=True),
        E('sala', 'suelo_libre', variantes=['expositor_gafas', 'paraguas_cubo', 'perfumes_expositor'], cantidad=[3, 3], todas=True, obligatorio=True, vende=['gafas', 'paraguas', 'perfume']),
        E('sala', 'techo', 'lampara_panel_led', por_m2=[0.08, 0.1], obligatorio=True),
        E('sala', 'techo', 'carril_focos', cantidad=[1, 2]),
    ],
    'iluminacion': {'fuentes': [4, 9], 'temperatura_k': [3500, 4300], 'dia': {'intensidad': 0.9}, 'noche': {'intensidad': 1.0}, 'minimo_lux_publico': 150},
    'ambiente': {'sonido': 'tienda', 'horario_defecto': 'Mo-Fr 10:00-14:00,17:00-20:30; Sa 10:00-14:00',
                 'vida': ['percha con una prenda probada', 'bolsas de papel junto a la caja', 'maniquíes recién vestidos', 'cartel de rebajas'],
                 'cerrado': 'reja bajada, la luz del escaparate encendida'},
    'minimo_objetos_distintos': 40,
}

# ================================================================== THE PHARMACY
MEDS = ['medicamento_' + k for k in ('analgesico', 'antiinflamatorio', 'antibiotico', 'antihistaminico', 'antigripal', 'protector_estomago', 'vitaminas', 'pomada', 'colirio', 'suero', 'tiritas', 'gasas',
                                      'mascarillas', 'termometro', 'pastillas_garganta', 'melatonina', 'magnesio', 'colageno')] + ['jarabe_tos', 'bote_vitaminas', 'spray_nasal', 'gotas_orales']
PARA = ['para_' + k for k in ('crema_facial', 'crema_manos', 'protector_solar', 'protector_solar_spray', 'leche_corporal', 'champu', 'gel_bano', 'pasta_dientes', 'panales', 'toallitas_bebe', 'leche_infantil',
                              'papilla', 'biberon', 'chupetes', 'desodorante', 'colonia_bebe', 'cepillos_dientes', 'contorno_ojos', 'mascarilla_facial', 'agua_termal')]

farmacia = {
    'tipologia': 'farmacia', 'nombre': 'Farmacia',
    'nota': 'La farmacia de un pueblo de las Vegas Altas: un mostrador largo de lado a lado con los dependientes detrás, la pared del fondo con cajones y baldas llenas de cajas de medicamentos, góndolas de parafarmacia, sala de espera con la báscula '
            'y el tensiómetro, la pantalla del turno, la cruz verde por dentro, el expositor de folletos y la rebotica al fondo con su nevera. La puerta en z = 0, el fondo en z = D; x de -W/2 a W/2.',
    '_mood': 'farmacia',
    'superficie': {'ancho': [5.4, 7.2], 'fondo': [8.4, 11.4], 'alto': 3.0},
    'variables': {'zm': 'D-3.9', 'zr': 'D-2.2'},
    'paso_libre': 0.9, 'pared': '#f3f5f2', 'suelo': 'long_white_tiles', 'suelo_color': '#dfe3de',
    'puntos': {'dependiente': ['0', 'zm+0.8'], 'mostrador': ['0', 'zm-0.75']},
    'pedir': 'Pedir en el mostrador',
    'zonas': [
        Z('entrada', ['-W/2', '0', 'W/2', '1.3']),
        Z('sala', ['-W/2', '0.3', 'W/2', 'zm-0.9']),
        Z('isla', ['-W/2+0.9', '1.3', 'W/2-0.9', 'zm-0.9']),
        Z('espera', ['-W/2', 'zm-0.9', 'W/2', 'zm-0.37']),
        Z('mostrador', ['-W/2+1.1', 'zm-0.35', 'W/2', 'zm+0.35'], False),
        Z('trasmostrador', ['-W/2+2.4', 'zm+0.37', 'W/2', 'D'], False),
        Z('rebotica', ['-W/2', 'zr', '-W/2+2.4', 'D'], False),
    ],
    'tabiques': [
        {'de': ['-W/2', 'zr'], 'a': ['-W/2+2.4', 'zr']},
        {'de': ['-W/2+2.4', 'zr'], 'a': ['-W/2+2.4', 'D'], 'puerta': [0.2, 1.0]},
    ],
    'libres': [{'rect': ['-W/2', 'zm-0.9', 'W/2', 'zm-0.36'], 'nota': 'la cola delante del mostrador: sin muebles'}],
    'objetos': [
        # ---- the counter across the room, first: the kit's own design
        E('mostrador', 'modulos', 'mostrador_farmacia', eje='x', linea=['zm', '-W/2+1.1', 'W/2'], mira='-z', obligatorio=True),
        sobre('mostrador', 'monitor_pc_mostrador', ['mostrador_farmacia'], cantidad=[1, 2], obligatorio=True),
        sobre('mostrador', 'teclado_mostrador', ['mostrador_farmacia'], cantidad=[1, 2], obligatorio=True),
        sobre('mostrador', 'datafono', ['mostrador_farmacia'], cantidad=[1, 2], obligatorio=True),
        sobre('mostrador', 'lector_codigo', ['mostrador_farmacia'], cantidad=[1, 1], obligatorio=True),
        sobre('mostrador', 'impresora_ticket', ['mostrador_farmacia'], cantidad=[1, 1], obligatorio=True),
        sobre('mostrador', 'dosificador_gel_mostrador', ['mostrador_farmacia'], cantidad=[1, 1], obligatorio=True),
        sobre('mostrador', 'mampara_metacrilato', ['mostrador_farmacia'], cantidad=[1, 2], obligatorio=True),
        sobre('mostrador', 'bandeja_cambio', ['mostrador_farmacia'], cantidad=[0, 1]),
        sobre('mostrador', 'bote_caramelos_farmacia', ['mostrador_farmacia'], cantidad=[0, 1]),
        sobre('mostrador', 'expositor_mostrador', ['mostrador_farmacia'], cantidad=[0, 1]),
        sobre('mostrador', 'cesta_farmacia', ['mostrador_farmacia'], cantidad=[0, 1]),
        E('mostrador', 'techo', 'pantalla_turno', cantidad=[1, 1], obligatorio=True),
        E('mostrador', 'techo', 'regleta_led', cantidad=[1, 2], obligatorio=True),
        # ---- behind the counter: the wall of drawers and shelves, the cross, the cupboard
        E('trasmostrador', 'esquina', 'papelera', cantidad=[1, 1], obligatorio=True),
        E('trasmostrador', 'contra_pared', 'estanteria_medicamentos', pared='N', llenar=True, obligatorio=True),
        E('trasmostrador', 'pared', 'cruz_farmacia_pared', pared='N', cantidad=[1, 1], obligatorio=True),
        E('trasmostrador', 'contra_pared', 'estanteria_medicamentos', pared='E', cantidad=[0, 1]),
        E('trasmostrador', 'contra_pared', 'armario_rebotica', pared='E', cantidad=[0, 1]),
        sobre('trasmostrador', MEDS, ['estanteria_medicamentos'], relleno=[0.8, 0.95], todas=True, obligatorio=True),
        E('trasmostrador', 'pared', 'reloj_pared', pared='N', cantidad=[0, 1]),
        E('trasmostrador', 'suelo_libre', 'silla_madera', cantidad=[0, 1]),
        E('trasmostrador', 'techo', 'lampara_panel_led', por_m2=[0.06, 0.08], obligatorio=True),
        # ---- the dispensary: shelves of deliveries, the work table, the medicine fridge
        E('rebotica', 'contra_pared', 'estanteria_metalica', pared='N', cantidad=[1, 1], obligatorio=True),
        sobre('rebotica', ['cubeta_pedido', 'caja_carton'], ['estanteria_metalica'], relleno=[0.6, 0.9], todas=True, obligatorio=True),
        E('rebotica', 'contra_pared', 'mesa_rebotica', pared='W', cantidad=[1, 1], obligatorio=True),
        sobre('rebotica', 'balanza_precision', ['mesa_rebotica'], cantidad=[1, 1], obligatorio=True),
        sobre('rebotica', 'mortero', ['mesa_rebotica'], cantidad=[1, 1], obligatorio=True),
        sobre('rebotica', 'frasco_laboratorio', ['mesa_rebotica'], cantidad=[1, 2], obligatorio=True),
        sobre('rebotica', 'cubeta_pedido', ['mesa_rebotica'], cantidad=[0, 1]),
        E('rebotica', 'contra_pared', 'nevera_farmacia', pared='N', cantidad=[1, 1], obligatorio=True),
        E('rebotica', 'pared', 'lavabo', pared='W', cantidad=[0, 1]),
        E('rebotica', 'esquina', 'silla_madera', cantidad=[0, 1]),
        E('rebotica', 'techo', 'plafon_pequeno', cantidad=[1, 1], obligatorio=True),
        # ---- the door, the islands, the waiting corner and the parapharmacy wall (the obligatory first)
        E('entrada', 'esquina', 'bascula_farmacia', cantidad=[1, 1], obligatorio=True),
        E('entrada', 'contra_pared', 'contenedor_envases', pared='W', cantidad=[1, 1], obligatorio=True),
        E('entrada', 'esquina', 'papelera', cantidad=[1, 1], obligatorio=True),
        E('entrada', 'esquina', 'dispensador_gel_pie', cantidad=[1, 1], obligatorio=True),
        E('entrada', 'esquina', 'planta_grande', cantidad=[0, 1]),
        E('entrada', 'pared', 'cartel_horario', pared='E', cantidad=[1, 1], obligatorio=True),
        E('entrada', 'pared', 'cartel_guardia', pared='E', cantidad=[0, 1]),
        E('entrada', 'techo', 'lampara_panel_led', cantidad=[1, 1], obligatorio=True),
        E('isla', 'filas', 'gondola_parafarmacia', eje='z', pasillo=0.95, margen=[0.7, 0.4], obligatorio=True),
        E('sala', 'contra_pared', 'banco_espera', pared='W', cantidad=[1, 1], obligatorio=True),
        E('sala', 'contra_pared', 'tensiometro_automatico', pared='W', cantidad=[1, 1], obligatorio=True),
        E('sala', 'contra_pared', 'silla_espera', pared='W', cantidad=[0, 2]),
        E('sala', 'contra_pared', 'estanteria_parafarmacia_pared', pared='E', llenar=True, obligatorio=True),
        E('sala', 'pared', 'folletero_farmacia', pared='W', cantidad=[1, 1], obligatorio=True),
        E('sala', 'pared', 'pantalla_promo', pared='W', cantidad=[1, 1], obligatorio=True),
        E('sala', 'suelo_libre', 'expendedor_turno', cantidad=[1, 1], obligatorio=True),
        sobre('isla', PARA[::-1], ['gondola_parafarmacia'], relleno=[0.8, 0.95], todas=True, obligatorio=True),
        sobre('sala', PARA, ['estanteria_parafarmacia_pared'], relleno=[0.8, 0.95], todas=True, obligatorio=True),
        E('sala', 'techo', 'lampara_panel_led', por_m2=[0.08, 0.1], obligatorio=True),
    ],
    'iluminacion': {'fuentes': [4, 9], 'temperatura_k': [3900, 4500], 'dia': {'intensidad': 0.9}, 'noche': {'intensidad': 1.0}, 'minimo_lux_publico': 200},
    'ambiente': {'sonido': 'tienda', 'horario_defecto': 'Mo-Fr 09:30-14:00,17:00-20:30; Sa 09:30-14:00',
                 'vida': ['el turno parpadea sobre el mostrador', 'alguien se toma la tensión', 'bolsa de la farmacia sobre el mostrador', 'cola ante el mostrador'],
                 'cerrado': 'persiana bajada, la cruz verde encendida',
                 'clientela': {'maximo': 3, 'horas': [[9, 14, 0.55], [17, 20.5, 0.5]],
                               'frases': ['¿Cuánto se tarda, hijo?', 'Hoy hay cola, como siempre.', 'A ver si tienen el jarabe del niño.', 'Dicen que este año viene fuerte la gripe.',
                                          'Yo solo vengo a tomarme la tensión.', 'La receta electrónica va muy bien, sí.', 'Con este calor no hay quien pare.', 'Me han dicho que esto es lo mejor para la tos.']}},
    'minimo_objetos_distintos': 40,
}

# ================================================================== THE SUPERMARKET
SECO_L = ['prod_' + k for k in ('atun', 'sardinillas', 'mejillones', 'tomate_frito', 'maiz', 'judias_verdes', 'garbanzos_bote', 'pimientos_piquillo', 'aceitunas', 'pepinillos', 'mermelada', 'miel', 'crema_cacao',
                                  'melocoton_almibar', 'aceite_oliva', 'aceite_girasol', 'garrafa_aceite', 'vinagre', 'arroz', 'arroz_integral', 'espaguetis', 'macarrones', 'lentejas', 'garbanzos_seco', 'harina',
                                  'azucar', 'sal', 'cafe_molido', 'infusiones', 'galletas_maria', 'galletas_chocolate', 'galletas_crackers', 'cereales_a', 'cereales_b', 'cereales_c', 'pan_molde', 'snack_patatas', 'snack_aperitivos')]
BEBI_L = ['prod_' + k for k in ('agua_15', 'agua_gas', 'cola_15', 'naranja_15', 'limon_15', 'cerveza_pack', 'vino_tinto', 'vino_blanco', 'vino_rosado', 'zumo_naranja', 'zumo_melocoton', 'leche_entera', 'leche_semi', 'leche_desnatada')]
LIMP_L = ['prod_' + k for k in ('detergente_liquido', 'detergente_polvo', 'suavizante', 'lavavajillas', 'lejia', 'limpiacristales', 'fregasuelos', 'papel_higienico', 'papel_cocina', 'servilletas', 'bolsas_basura',
                                  'gel_ducha', 'champu_super', 'dentifrico', 'compresas', 'esponjas')]
FRESCO_L = ['prod_' + k for k in ('yogur_natural', 'yogur_fresa', 'yogur_limon', 'mantequilla', 'queso_lonchas', 'huevos', 'nata', 'zumo_fresco', 'bandeja_carne', 'bandeja_pollo', 'fiambre_loncheado', 'quesito_untable')]
FRIAS_L = ['prod_' + k for k in ('agua_fria', 'naranja_fria', 'zumo_frio', 'cola_fria', 'cerveza_fria', 'isotonica_fria')]
SWEETS_L = ['prod_' + k for k in ('chocolate_tabletas', 'magdalenas', 'perrunillas', 'chicles', 'caramelos')]
FRUTA_L = ['prod_fruta_' + k for k in ('melocotones', 'melones', 'naranjas', 'manzanas_rojas', 'manzanas_verdes', 'limones', 'tomates', 'cebollas', 'patatas', 'lechugas', 'pimientos', 'zanahorias', 'platanos', 'uvas')]
PAN_L = ['prod_baguettes', 'prod_hogazas', 'prod_bollos', 'prod_pan_molde_artesano']

supermercado = {
    'tipologia': 'alimentacion', 'nombre': 'Supermercado',
    'nota': 'El supermercado de pueblo: la frutería y el pan en la entrada, las cajas con su cinta a la derecha, pasillos de góndolas con conservas, arroz, pasta, aceite, galletas, bebidas y limpieza, neveras murales de lácteos y bebidas, '
            'congeladores de isla, el mostrador de charcutería y quesos y el almacén al fondo. Marcas inventadas o sin marca. La puerta en z = 0, el fondo en z = D; x de -W/2 a W/2.',
    '_mood': 'supermercado',
    'superficie': {'ancho': [9.0, 11.4], 'fondo': [15.0, 18.0], 'alto': 3.2},
    'variables': {'xk': 'W/2-1.6', 'xq': 'W/2-3.6', 'nT': 'Math.floor((D-10.8)/2.04+1e-6)', 'nA': 'Math.ceil(nT/2)', 'zA1': '5.9+1.2+nA*2.04+0.02', 'zf': 'D-3.7', 'za': 'D-2.9'},
    'paso_libre': 0.9, 'pared': '#f0eee6', 'suelo': 'floor_tiles_06', 'suelo_color': '#c9c6bd',
    'puntos': {'dependiente': ['xk+0.8', '3.8'], 'mostrador': ['xk-0.9', '3.8']},
    'pedir': 'Pagar en caja',
    'zonas': [
        Z('entrada', ['-W/2', '0', 'xq', '2.2']),
        Z('fruteria', ['-W/2', '2.2', 'xq', '5.9']),
        Z('caja', ['xk-0.5', '1.8', 'xk+0.5', '5.7'], False),
        Z('trascaja', ['xk+0.52', '1.8', 'W/2', '5.7'], False),
        Z('frente_caja', ['xq', '1.8', 'xk-0.52', '5.9']),
        Z('gond_a', ['-W/2+0.45', '5.9', 'W/2-0.45', 'zA1']),
        Z('gond_b', ['-W/2+0.45', 'zA1-1.2', 'W/2-0.45', 'zf']),
        Z('pared_oeste', ['-W/2', '5.9', '-W/2+0.5', 'D-4.1'], False),
        Z('pared_este', ['W/2-0.5', '5.9', 'W/2', 'D-4.8'], False),
        Z('neveras', ['-W/2+3.1', 'zf', 'W/2-3.1', 'D']),
        Z('deli', ['W/2-1.9', 'D-4.0', 'W/2', 'D'], False),
        Z('deli_frente', ['W/2-3.0', 'D-4.0', 'W/2-1.9', 'D-0.3']),
        Z('almacen', ['-W/2', 'za', '-W/2+3.0', 'D'], False),
        Z('caja_1', ['xk-0.5', '1.8', 'xk+0.5', '3.75'], False),
        Z('caja_2', ['xk-0.5', '3.75', 'xk+0.5', '5.7'], False),
        Z('s_fruta', ['-W/2+2.2', '3.1', '-W/2+3.8', '3.7'], False),
        Z('s_pan', ['-W/2+0.2', '4.2', '-W/2+1.8', '4.8'], False),
        Z('s_conservas', ['-W/4-0.8', '6.4', '-W/4+0.8', '7.0'], False),
        Z('s_dulces', ['W/4-0.8', '6.4', 'W/4+0.8', '7.0'], False),
        Z('s_bebidas', ['-W/4-0.8', 'zA1+0.7', '-W/4+0.8', 'zA1+1.3'], False),
        Z('s_limpieza', ['W/4-0.8', 'zA1+0.7', 'W/4+0.8', 'zA1+1.3'], False),
        Z('s_lacteos', ['-1.8', 'D-3.6', '-0.2', 'D-3.0'], False),
        Z('s_congelados', ['0.2', 'D-3.6', '1.8', 'D-3.0'], False),
        Z('s_charcuteria', ['W/2-3.0', 'D-4.4', 'W/2-1.4', 'D-3.8'], False),
        Z('luces_frente', ['-W/2', '0', 'W/2', '5.9'], False),
        Z('luces_campo', ['-W/2+0.45', '5.9', 'W/2-0.45', 'zf'], False),
    ],
    'tabiques': [
        {'de': ['-W/2', 'za'], 'a': ['-W/2+3.0', 'za'], 'puerta': [1.0, 1.0]},
        {'de': ['-W/2+3.0', 'za'], 'a': ['-W/2+3.0', 'D']},
    ],
    'objetos': [
        # ---- the checkouts, first: the kit's own design (belt, till, scanner), the cashiers behind
        E('caja', 'modulos', 'caja_super_modulo', eje='z', linea=['xk', '1.8', '5.7'], mira='-x', obligatorio=True),
        sobre('caja', 'cesta_compra_llena', ['caja_super_modulo'], cantidad=[0, 2]),
        sobre('caja', 'separador_cinta', ['caja_super_modulo'], cantidad=[1, 2], obligatorio=True),
        E('trascaja', 'suelo_libre', 'silla_cajera', cantidad=[1, 2], obligatorio=True),
        E('trascaja', 'esquina', 'papelera', cantidad=[1, 1], obligatorio=True),
        E('trascaja', 'pared', 'cartel_oferta_2x1', variantes=['cartel_oferta_2x1', 'cartel_oferta_3x2'], pared='E', cantidad=[1, 1], obligatorio=True),
        E('caja_1', 'techo', 'numero_caja_1', cantidad=[1, 1], obligatorio=True),
        E('caja_2', 'techo', 'numero_caja_2', cantidad=[1, 1], obligatorio=True),
        # ---- the storeroom
        E('almacen', 'contra_pared', 'estanteria_metalica', pared='N', cantidad=[1, 2], obligatorio=True),
        sobre('almacen', ['caja_carton', 'prod_garrafa_aceite', 'prod_detergente_polvo', 'prod_leche_entera', 'prod_arroz'], ['estanteria_metalica'], relleno=[0.6, 0.9], todas=True, obligatorio=True),
        E('almacen', 'suelo_libre', variantes=['palet_madera', 'transpaleta', 'palet_agua'], cantidad=[1, 2], obligatorio=True),
        E('almacen', 'esquina', variantes=['pila_cajones_vacios', 'carretilla_mano'], cantidad=[1, 2], todas=True),
        E('almacen', 'esquina', 'fregona_cubo', cantidad=[0, 1]),
        E('almacen', 'esquina', 'escoba', cantidad=[0, 1]),
        E('almacen', 'suelo_libre', 'caja_carton', cantidad=[1, 3], obligatorio=True),
        # ---- the deli counter (the first modules sell: Torta del Casar, migas, a sandwich), its signs and hams
        E('deli', 'modulos', 'mostrador_charcuteria_modulo', eje='z', linea=['W/2-1.5', 'D-4.0', 'D-0.3'], mira='-x', obligatorio=True, vende=['torta', 'migas', 'bocadillo']),
        sobre('deli', 'balanza_comercial', ['mostrador_charcuteria_modulo'], cantidad=[1, 1], obligatorio=True),
        sobre('deli', 'cortadora_fiambre', ['mostrador_charcuteria_modulo'], cantidad=[1, 1], obligatorio=True),
        E('deli', 'pared', 'pizarra_charcuteria', pared='E', cantidad=[1, 1], obligatorio=True),
        E('deli', 'techo', 'jamon_colgado', cantidad=[2, 3], obligatorio=True),
        E('s_charcuteria', 'techo', 'cartel_seccion_charcuteria', cantidad=[1, 1], obligatorio=True),
        # ---- the wall fridges and the freezers at the back
        E('neveras', 'contra_pared', variantes=['nevera_lacteos', 'nevera_bebidas_super'], pared='N', llenar=True, todas=True, obligatorio=True),
        sobre('neveras', FRESCO_L, ['nevera_lacteos'], relleno=[0.8, 0.95], todas=True, obligatorio=True),
        sobre('neveras', FRIAS_L, ['nevera_bebidas_super'], relleno=[0.8, 0.95], todas=True, obligatorio=True, vende=['agua', 'refresco', 'zumo']),
        E('neveras', 'suelo_libre', 'congelador_isla', cantidad=[1, 2], obligatorio=True),
        E('s_lacteos', 'techo', 'cartel_seccion_lacteos', cantidad=[1, 1], obligatorio=True),
        E('s_congelados', 'techo', 'cartel_seccion_congelados', cantidad=[1, 1], obligatorio=True),
        E('neveras', 'techo', 'regleta_fluorescente', cantidad=[1, 1], obligatorio=True),
        E('neveras', 'pared', 'extintor_super', pared='N', cantidad=[0, 1]),
        # ---- the entrance: baskets, trolleys, promotions, what is sold by the door
        E('entrada', 'esquina', 'papelera', cantidad=[1, 1], obligatorio=True),
        E('entrada', 'contra_pared', 'pila_cestas', pared='S', cantidad=[1, 1], obligatorio=True),
        E('entrada', 'contra_pared', 'carrito_compra', pared='S', cantidad=[2, 4], obligatorio=True),
        E('entrada', 'suelo_libre', 'torre_latas_maiz', cantidad=[1, 1], obligatorio=True, vende='maiz'),
        E('entrada', 'suelo_libre', variantes=['palet_agua', 'palet_refrescos', 'palet_leche', 'palet_aceite', 'palet_detergente'], cantidad=[1, 2], obligatorio=True),
        E('entrada', 'suelo_libre', 'torre_latas_tomate', cantidad=[0, 1]),
        E('entrada', 'pared', 'senal_salida_super', pared='W', cantidad=[1, 1], obligatorio=True),
        E('entrada', 'pared', 'extintor_super', pared='W', cantidad=[0, 1]),
        E('entrada', 'techo', 'camara_cupula', cantidad=[1, 1], obligatorio=True),
        # ---- the greengrocer's and the bread, by the entrance (west)
        E('fruteria', 'contra_pared', 'expositor_pan', pared='W', cantidad=[1, 1], obligatorio=True),
        sobre('fruteria', PAN_L, ['expositor_pan'], relleno=[0.8, 0.95], todas=True, obligatorio=True, vende='pan'),
        E('fruteria', 'contra_pared', 'mesa_fruteria', pared='W', cantidad=[1, 2], obligatorio=True),
        E('fruteria', 'conjunto', 'mesa_fruteria', cantidad=[1, 2], obligatorio=True),
        sobre('fruteria', FRUTA_L, ['mesa_fruteria'], por_soporte=[3, 4], todas=True, obligatorio=True, vende=['fruta', 'melon']),
        E('fruteria', 'pared', 'pizarra_fruteria', pared='W', cantidad=[1, 1]),
        E('fruteria', 'esquina', 'planta_grande', cantidad=[0, 1]),
        E('s_fruta', 'techo', 'cartel_seccion_fruta', cantidad=[1, 1], obligatorio=True),
        E('s_pan', 'techo', 'cartel_seccion_pan', cantidad=[1, 1], obligatorio=True),
        # ---- by the checkouts: sweets
        E('frente_caja', 'suelo_libre', 'expositor_dulces', cantidad=[1, 1], obligatorio=True),
        sobre('frente_caja', SWEETS_L, ['expositor_dulces'], relleno=[0.8, 0.95], todas=True, obligatorio=True, vende=['chocolate', 'magdalenas', 'perrunillas']),
        # ---- the aisles: two bands of gondolas (dry goods, then drinks and cleaning), wall shelving
        E('gond_a', 'filas', 'gondola_super', eje='x', pasillo=1.2, margen=[1.0, 1.0], obligatorio=True),
        E('gond_b', 'filas', 'gondola_super', eje='x', pasillo=1.2, margen=[1.0, 1.0], obligatorio=True),
        E('pared_oeste', 'contra_pared', 'estanteria_super_pared', pared='W', llenar=True, obligatorio=True),
        E('pared_este', 'contra_pared', 'estanteria_super_pared', pared='E', llenar=True, obligatorio=True),
        sobre('gond_a', SECO_L, ['gondola_super'], relleno=[0.8, 0.95], todas=True, obligatorio=True),
        sobre('gond_b', BEBI_L + LIMP_L, ['gondola_super'], relleno=[0.8, 0.95], todas=True, obligatorio=True),
        sobre('pared_oeste', SECO_L[::-1] + SWEETS_L, ['estanteria_super_pared'], relleno=[0.8, 0.95], todas=True, obligatorio=True),
        sobre('pared_este', LIMP_L[::-1] + BEBI_L[::-1], ['estanteria_super_pared'], relleno=[0.8, 0.95], todas=True, obligatorio=True),
        E('pared_oeste', 'pared', 'espejo_convexo', pared='W', cantidad=[0, 1]),
        E('pared_oeste', 'pared', 'reloj_pared', pared='W', cantidad=[0, 1]),
        E('s_conservas', 'techo', 'cartel_seccion_conservas', cantidad=[1, 1], obligatorio=True),
        E('s_dulces', 'techo', 'cartel_seccion_dulces', cantidad=[1, 1], obligatorio=True),
        E('s_bebidas', 'techo', 'cartel_seccion_bebidas', cantidad=[1, 1], obligatorio=True),
        E('s_limpieza', 'techo', 'cartel_seccion_limpieza', cantidad=[1, 1], obligatorio=True),
        # ---- the lights of the shop (fluorescent strips): the front, the aisles, the back
        E('luces_frente', 'techo', 'regleta_fluorescente', cantidad=[2, 2], obligatorio=True),
        E('luces_campo', 'techo', 'regleta_fluorescente', cantidad=[6, 6], obligatorio=True),
    ],
    'iluminacion': {'fuentes': [6, 9], 'temperatura_k': [3800, 4500], 'dia': {'intensidad': 0.9}, 'noche': {'intensidad': 1.0}, 'minimo_lux_publico': 200},
    'ambiente': {'sonido': 'tienda', 'horario_defecto': 'Mo-Sa 09:00-14:30,17:00-21:00',
                 'vida': ['cestas junto a la puerta', 'cajas de fruta recién puestas', 'oferta de latas', 'la cola de la caja'],
                 'cerrado': 'persiana bajada, las neveras encendidas'},
    'minimo_objetos_distintos': 80,
}

if __name__ == '__main__':
    escribir('ropa', ropa)
    escribir('farmacia', farmacia)
    escribir('supermercado', supermercado)
