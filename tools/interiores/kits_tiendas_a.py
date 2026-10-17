# The seven kits of the «tiendas_a» family (technical backlog, I-02): the «todo a cien» variety store, the hardware shop, the
# bookshop, the toyshop, the florist, the estanco (tobacco, lottery and press) and the jeweller-watchmaker / optician —
# written to data/kits/<kit>.json from here, so that a rule is written once and read well. The objects they name are in
# tools/interiores/catalogo_tiendas_a.py (and, by id, in the families hostelería, comercio and servicios); the moodboards
# (Wikimedia Commons: page, author and licence, never the picture) in tools/interiores/moodboard_tiendas_a.json.
#   python3 tools/interiores/catalogo_tiendas_a.py && python3 tools/interiores/kits_tiendas_a.py
import html, json, os, random
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
MOOD = json.load(open(os.path.join(ROOT, 'tools', 'interiores', 'moodboard_tiendas_a.json')))

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
def barajar(lista, semilla):
    """A fixed shuffle (the kit is the same every time it is written): products in an order that mixes the kinds."""
    L = list(lista); random.Random(semilla).shuffle(L); return L

def escribir(id, K):
    K['moodboard'] = [{'titulo': html.unescape(m['titulo']), 'url': m['url'], 'autor': html.unescape(m['autor']), 'licencia': m['licencia']} for m in MOOD[K.pop('_mood')]]
    json.dump(K, open(os.path.join(ROOT, 'data', 'kits', id + '.json'), 'w'), ensure_ascii=False, indent=1)
    print(id, len(K['objetos']), 'entradas')

# ================================================================== THE VARIETY STORE («todo a cien»)
BZ_HOGAR = ['bz_cubos', 'bz_cubos_azules', 'bz_barrenos', 'bz_barrenos_naranja', 'bz_fiambreras', 'bz_fiambreras_rojas', 'bz_vasos', 'bz_vasos_rosa', 'bz_platos', 'bz_tazas', 'bz_tazas_azules', 'bz_ollas', 'bz_cestos_ropa', 'bz_cestos_rosa',
            'bz_toallas', 'bz_trapos', 'bz_velas', 'bz_jarrones', 'bz_marcos', 'bz_flores_artificiales', 'bz_flores_lilas', 'bz_cestos_mimbre']
BZ_PAPEL = ['bz_cuadernos', 'bz_cuadernos_a4', 'bz_carpetas', 'bz_boligrafos', 'bz_pegamentos', 'bz_lapices_color', 'bz_acuarelas']
BZ_JUEGO = ['bz_puzles', 'bz_cochecitos', 'bz_munecas', 'bz_pompas', 'bz_pelotas_saltarinas']
BZ_TECNO = ['bz_cargadores', 'bz_auriculares', 'bz_fundas_movil', 'bz_pilas', 'bz_bombillas', 'bz_alargaderas']
BZ_TODO = BZ_HOGAR + BZ_PAPEL + BZ_JUEGO + BZ_TECNO

bazar = {
    'tipologia': 'tienda_especializada', 'nombre': 'Bazar («todo a cien»)',
    'nota': 'El bazar de pueblo de «todo a cien»: góndolas y estanterías repletas de menaje, juguetes, papelería, plásticos y accesorios de móvil, paneles de pared con relojes, espejos y cuadros, cestos de ofertas junto a la puerta, '
            'la caja con su mostrador pegada a la entrada y el almacén al fondo. La puerta en z = 0, el fondo en z = D; x de -W/2 a W/2.',
    '_mood': 'bazar',
    'superficie': {'ancho': [6.6, 8.1], 'fondo': [10.5, 13.2], 'alto': 3.0},
    'variables': {'xc': 'W/2-1.7', 'z0': '1.5', 'z1': '3.9', 'zb': 'D-2.1'},
    'paso_libre': 0.9, 'pared': '#f1e8cc', 'suelo': 'floor_tiles_06', 'suelo_color': '#cdc6b6',
    'puntos': {'dependiente': ['xc+0.8', '(z0+z1)/2'], 'mostrador': ['xc-0.75', '(z0+z1)/2']},
    'pedir': 'Pagar en caja',
    'zonas': [
        Z('entrada', ['-W/2', '0', 'W/2', '1.3']),
        Z('caja', ['xc-0.3', 'z0', 'xc+0.3', 'z1'], False),
        Z('trascaja', ['xc+0.33', 'z0', 'W/2', 'z1+0.2'], False),
        Z('frente_caja', ['xc-1.3', 'z0', 'xc-0.33', 'z1']),
        Z('puestos', ['-W/2+0.9', '1.3', 'xc-1.35', '4.9']),
        Z('sala', ['-W/2', '1.3', 'W/2', 'zb']),
        Z('isla', ['-W/2+0.42', '5.0', 'W/2-0.42', 'zb']),
        Z('almacen', ['-W/2', 'zb', 'W/2', 'D'], False),
    ],
    'tabiques': [{'de': ['-W/2', 'zb'], 'a': ['W/2', 'zb'], 'puerta': ['W-1.6', 1.0]}],
    'libres': [{'rect': ['xc-1.3', 'z0', 'xc-0.3', 'z1'], 'nota': 'el sitio para pagar en el mostrador: sin muebles delante'}, {'rect': ['xc+0.35', '(z0+z1)/2-0.45', 'xc+1.15', '(z0+z1)/2+0.45'], 'nota': 'donde está el dependiente'}],
    'objetos': [
        # ---- the counter, first: the kit's own design
        E('caja', 'modulos', 'mostrador_bazar', eje='z', linea=['xc', 'z0', 'z1'], mira='-x', obligatorio=True),
        sobre('caja', 'caja_registradora', ['mostrador_bazar'], cantidad=[1, 1], obligatorio=True),
        sobre('caja', 'datafono', ['mostrador_bazar'], cantidad=[1, 1], obligatorio=True),
        sobre('caja', 'pila_bolsas_plastico', ['mostrador_bazar'], cantidad=[1, 2], obligatorio=True),
        sobre('caja', 'expositor_pilas_mostrador', ['mostrador_bazar'], cantidad=[0, 1]),
        sobre('caja', 'expositor_llaveros', ['mostrador_bazar'], cantidad=[0, 1]),
        sobre('caja', 'bote_caramelos', ['mostrador_bazar'], cantidad=[0, 1]),
        sobre('caja', 'calculadora', ['mostrador_bazar'], cantidad=[0, 1]),
        E('trascaja', 'contra_pared', 'armario_trascaja', pared='E', cantidad=[1, 1], obligatorio=True),
        E('trascaja', 'pared', 'rotulo_bazar', pared='E', cantidad=[1, 1], obligatorio=True),
        sobre('trascaja', 'caja_bazar_grande', ['armario_trascaja'], cantidad=[0, 2]),
        E('trascaja', 'esquina', 'papelera', cantidad=[1, 1], obligatorio=True),
        E('trascaja', 'suelo_libre', 'silla_madera', cantidad=[0, 1]),
        # ---- the storeroom
        E('almacen', 'contra_pared', 'estanteria_metalica', pared='N', cantidad=[2, 2], obligatorio=True),
        sobre('almacen', ['caja_bazar_grande', 'caja_carton', 'bz_cubos', 'bz_toallas', 'bz_cestos_ropa'], ['estanteria_metalica'], relleno=[0.6, 0.9], todas=True, obligatorio=True),
        E('almacen', 'contra_pared', 'torre_cajas_bazar', pared='W', cantidad=[1, 2], obligatorio=True),
        E('almacen', 'contra_pared', 'caja_bazar_grande', pared='E', cantidad=[2, 4], obligatorio=True),
        E('almacen', 'esquina', 'taburete_escalon', cantidad=[0, 1]),
        E('almacen', 'esquina', 'fregona_cubo', cantidad=[0, 1]),
        E('almacen', 'esquina', 'escoba', cantidad=[0, 1]),
        E('almacen', 'techo', 'plafon_pequeno', cantidad=[1, 1], obligatorio=True),
        # ---- the door
        E('entrada', 'esquina', 'papelera', cantidad=[1, 1], obligatorio=True),
        E('entrada', 'pared', 'cartel_ofertas_bazar', pared=['W', 'E'], cantidad=[1, 1], obligatorio=True),
        E('entrada', 'suelo_libre', 'cesta_baratijas', cantidad=[1, 1], obligatorio=True),
        E('entrada', 'techo', 'regleta_fluorescente', cantidad=[1, 1], obligatorio=True),
        # ---- what is sold where it stands: stands by the door (buy points on each)
        E('puestos', 'suelo_libre', variantes=['expositor_cojines', 'paraguas_cubo', 'expositor_cactus'], cantidad=[3, 3], todas=True, obligatorio=True, vende=['cojines', 'paraguas', 'cactus']),
        E('puestos', 'suelo_libre', variantes=['cubo_peluches', 'expositor_cometas', 'red_balones'], cantidad=[3, 3], todas=True, obligatorio=True, vende=['peluche', 'cometa', 'balon']),
        E('puestos', 'suelo_libre', variantes=['expositor_lamparitas', 'expositor_gafas', 'expositor_cuadernos'], cantidad=[3, 3], todas=True, obligatorio=True, vende=['lamparita', 'gafas', 'cuaderno']),
        E('puestos', 'suelo_libre', 'expositor_posters', cantidad=[1, 1], obligatorio=True, vende='poster'),
        # ---- the west wall: low shelves with the pegboards above
        E('sala', 'pared', 'cartel_precio_bazar', pared='N', cantidad=[0, 1]),
        E('sala', 'pared', variantes=['panel_relojes', 'panel_espejos', 'panel_cuadros', 'panel_cargadores', 'panel_linternas', 'panel_cocina', 'panel_limpieza'], pared='W', cada=1.1, maximo=7, todas=True, obligatorio=True,
          vende=['reloj', 'espejo', 'cuadro', 'cargador', 'linterna']),
        E('sala', 'contra_pared', 'estanteria_bazar_baja', pared='W', llenar=True, obligatorio=True),
        E('sala', 'contra_pared', 'estanteria_bazar_pared', pared='E', llenar=True, obligatorio=True),
        E('sala', 'contra_pared', 'estanteria_bazar_pared', pared='N', llenar=True),
        E('sala', 'pared', 'reloj_pared', pared='N', cantidad=[0, 1]),
        # ---- the aisles: back-to-back gondolas
        E('isla', 'filas', 'gondola_bazar', eje='z', pasillo=0.95, margen=[0.9, 0.9], obligatorio=True),
        sobre('isla', barajar(BZ_TODO, 1), ['gondola_bazar'], relleno=[0.82, 0.97], todas=True, obligatorio=True),
        sobre('sala', barajar(BZ_TODO, 2), ['estanteria_bazar_baja'], relleno=[0.82, 0.97], todas=True, obligatorio=True),
        sobre('sala', barajar(BZ_TODO, 3), ['estanteria_bazar_pared'], relleno=[0.82, 0.97], todas=True, obligatorio=True),
        # ---- the lights (fluorescent tubes)
        E('sala', 'techo', 'regleta_fluorescente', por_m2=[0.09, 0.11], obligatorio=True),
        # ---- what the rules ask of a shop: an extinguisher, the exit light, the camera and the smoke detector
        E('sala', 'pared', 'extintor', pared=['W', 'E'], cantidad=[0, 1]),
        E('entrada', 'pared', 'senal_salida', pared=['E', 'W'], cantidad=[0, 1]),
        E('sala', 'techo', 'camara_seguridad', cantidad=[1, 1]),
        E('sala', 'techo', 'detector_humo', cantidad=[1, 1]),
    ],
    'iluminacion': {'fuentes': [4, 9], 'temperatura_k': [3800, 4500], 'dia': {'intensidad': 0.9}, 'noche': {'intensidad': 1.0}, 'minimo_lux_publico': 200},
    'ambiente': {'sonido': 'tienda', 'horario_defecto': 'Mo-Sa 09:30-14:00,17:00-21:00; Su 10:00-14:00',
                 'vida': ['cestos de ofertas junto a la puerta', 'peluches apilados', 'una caja de cartón a medio abrir', 'el cartel de «todo a un euro»'],
                 'cerrado': 'reja bajada, las luces del fondo encendidas'},
    'minimo_objetos_distintos': 40,
}

# ================================================================== THE HARDWARE SHOP (ferretería)
FE_PINT = ['fe_pintura_blanca', 'fe_pintura_roja', 'fe_pintura_azul', 'fe_pintura_verde', 'fe_pintura_amarilla', 'fe_pintura_gris', 'fe_barniz', 'fe_pintura_cubo', 'fe_brochas']
FE_TORN = ['fe_cajas_tornillos', 'fe_cajas_clavos_puntas', 'fe_tacos', 'fe_bisagras', 'fe_candados', 'fe_brocas', 'fe_niveles_metros']
FE_ELEC = ['fe_cable_bobinas', 'fe_enchufes', 'bz_bombillas', 'bz_alargaderas', 'bz_pilas']
FE_FONT = ['fe_grifos', 'fe_tuberias_pvc', 'fe_silicona', 'fe_cola', 'fe_cintas']
FE_JARD = ['fe_guantes_trabajo', 'fe_tijeras_poda', 'fe_regaderas', 'fe_abonos', 'fe_insecticidas']
FE_HERR = ['fe_maletines', 'fe_taladros_caja']
FE_TODO = FE_PINT + FE_TORN + FE_ELEC + FE_FONT + FE_JARD + FE_HERR

ferreteria = {
    'tipologia': 'tienda_especializada', 'nombre': 'Ferretería',
    'nota': 'La ferretería de pueblo: un mostrador largo de lado a lado con la regla de latón y la máquina de copiar llaves, detrás la pared de cajoncitos de tornillos y las estanterías de cajas, los paneles de herramientas colgadas y las estanterías bajas '
            'en las paredes de la sala, góndolas de pintura, fontanería y electricidad, la torre de botes, mangueras, escobas, escaleras, cemento y plantas en la entrada y el almacén al fondo. La puerta en z = 0, el fondo en z = D; x de -W/2 a W/2.',
    '_mood': 'ferreteria',
    'superficie': {'ancho': [6.0, 7.5], 'fondo': [12.3, 13.5], 'alto': 3.0},
    'variables': {'zm': 'D-5.6', 'zr': 'D-1.9'},
    'paso_libre': 0.9, 'pared': '#ebe4d2', 'suelo': 'rock_tile_floor', 'suelo_color': '#c4c0b4',
    'puntos': {'dependiente': ['0', 'zm+0.8'], 'mostrador': ['0', 'zm-0.75']},
    'pedir': 'Pedir en el mostrador',
    'zonas': [
        Z('entrada', ['-W/2', '0', 'W/2', '1.4']),
        Z('tienda', ['-W/2', '1.4', 'W/2', 'zm-0.9']),
        Z('isla', ['-W/2+0.42', '1.9', 'W/2-0.42', 'zm-0.9']),
        Z('mostrador', ['-W/2+1.5', 'zm-0.35', 'W/2', 'zm+0.35'], False),
        Z('trasmostrador', ['-W/2', 'zm+0.37', 'W/2', 'zr'], False),
        Z('almacen', ['-W/2', 'zr', 'W/2', 'D'], False),
    ],
    'tabiques': [{'de': ['-W/2', 'zr'], 'a': ['W/2', 'zr'], 'puerta': ['W-1.8', 1.0]}],
    'libres': [{'rect': ['-W/2', 'zm-0.9', 'W/2', 'zm-0.36'], 'nota': 'la cola delante del mostrador: sin muebles'},
               {'rect': ['-W/2', 'zm-1.7', '-W/2+1.6', 'zm+1.1'], 'nota': 'el paso del personal entre la sala y la trastienda'},
               {'rect': ['-0.45', 'zm+0.35', '0.45', 'zm+1.25'], 'nota': 'donde está el dependiente'}],
    'objetos': [
        # ---- the counter across the shop, first: the kit's own design (a gap at the west end for the staff)
        E('mostrador', 'modulos', 'mostrador_ferreteria', eje='x', linea=['zm', '-W/2+1.5', 'W/2'], mira='-z', obligatorio=True),
        sobre('mostrador', 'caja_registradora', ['mostrador_ferreteria'], cantidad=[1, 1], obligatorio=True),
        sobre('mostrador', 'datafono', ['mostrador_ferreteria'], cantidad=[1, 1], obligatorio=True),
        sobre('mostrador', 'maquina_llaves', ['mostrador_ferreteria'], cantidad=[1, 1], obligatorio=True),
        sobre('mostrador', 'expositor_linternas_mostrador', ['mostrador_ferreteria'], cantidad=[1, 1], obligatorio=True, vende='linterna'),
        sobre('mostrador', 'balanza_comercial', ['mostrador_ferreteria'], cantidad=[0, 1]),
        sobre('mostrador', 'bote_caramelos', ['mostrador_ferreteria'], cantidad=[0, 1]),
        sobre('mostrador', 'calculadora', ['mostrador_ferreteria'], cantidad=[0, 1]),
        sobre('mostrador', ['fe_cajas_tornillos', 'fe_tacos'], ['mostrador_ferreteria'], cantidad=[1, 2]),
        E('mostrador', 'techo', 'luminaria_campana', cantidad=[1, 1], obligatorio=True),
        # ---- behind the counter: the wall of drawers, the shelves of boxes, the keys, the sign
        E('trasmostrador', 'contra_pared', 'cajonera_tornillos', pared='N', cantidad=[2, 2], obligatorio=True),
        E('trasmostrador', 'contra_pared', 'estanteria_ferreteria_pared', pared='N', llenar=True, obligatorio=True),
        E('trasmostrador', 'pared', 'rotulo_ferreteria', pared='N', cantidad=[1, 1], obligatorio=True),
        E('trasmostrador', 'pared', 'tablero_llaves', pared='W', cantidad=[1, 1], obligatorio=True),
        E('trasmostrador', 'pared', 'cartel_llaves', pared='W', cantidad=[1, 1], obligatorio=True),
        E('trasmostrador', 'contra_pared', 'estanteria_ferreteria_pared', pared='E', llenar=True),
        E('trasmostrador', 'esquina', 'papelera', cantidad=[1, 1], obligatorio=True),
        E('trasmostrador', 'suelo_libre', 'silla_madera', cantidad=[0, 1]),
        E('trasmostrador', 'pared', variantes=['reloj_pared', 'calendario_pared'], pared='E', cantidad=[0, 2]),
        sobre('trasmostrador', barajar(FE_TORN + FE_ELEC + FE_FONT, 4), ['estanteria_ferreteria_pared'], relleno=[0.85, 0.97], todas=True, obligatorio=True),
        sobre('trasmostrador', ['caja_carton', 'fe_pintura_cubo', 'fe_abonos'], ['cajonera_tornillos'], cantidad=[0, 2]),
        E('trasmostrador', 'techo', 'regleta_fluorescente', cantidad=[1, 1], obligatorio=True),
        # ---- the storeroom
        E('almacen', 'contra_pared', 'estanteria_metalica', pared='N', cantidad=[2, 2], obligatorio=True),
        sobre('almacen', ['caja_carton', 'fe_pintura_blanca', 'fe_pintura_cubo', 'fe_cajas_tornillos', 'fe_abonos'], ['estanteria_metalica'], relleno=[0.6, 0.9], todas=True, obligatorio=True),
        E('almacen', 'contra_pared', variantes=['palet_sacos_cemento', 'cubos_albanil_pila'], pared='W', cantidad=[1, 2], todas=True, obligatorio=True),
        E('almacen', 'contra_pared', 'carretilla_obra', pared='E', cantidad=[1, 1], obligatorio=True),
        E('almacen', 'contra_pared', 'caja_carton', pared='E', cantidad=[0, 2]),
        E('almacen', 'esquina', 'escalera_tijera', cantidad=[0, 1]),
        E('almacen', 'esquina', 'fregona_cubo', cantidad=[0, 1]),
        E('almacen', 'esquina', 'escoba', cantidad=[0, 1]),
        E('almacen', 'techo', 'plafon_pequeno', cantidad=[1, 1], obligatorio=True),
        # ---- the door and the sales floor: stands first (what is sold where it stands), then the walls and the gondolas
        E('entrada', 'esquina', 'papelera', cantidad=[1, 1], obligatorio=True),
        E('entrada', 'suelo_libre', variantes=['ventilador_pie', 'paraguas_cubo'], cantidad=[2, 2], todas=True, obligatorio=True, vende=['ventilador', 'paraguas']),
        E('entrada', 'suelo_libre', variantes=['expositor_geranios', 'macetas_terracota'], cantidad=[2, 2], todas=True, obligatorio=True, vende=['geranios', 'planta']),
        E('entrada', 'suelo_libre', variantes=['carretilla_obra', 'palet_sacos_cemento', 'carrete_manguera', 'cubos_albanil_pila'], cantidad=[1, 2]),
        E('tienda', 'pared', variantes=['panel_herramientas', 'panel_navajas', 'panel_llaves_fijas', 'panel_alicates', 'panel_destornilladores', 'panel_martillos', 'panel_sierras'], pared='E', cada=1.1, maximo=7, todas=True, obligatorio=True, vende=['herramientas', 'navaja']),
        E('tienda', 'pared', variantes=['escalera_extensible_colgada'], pared='W', cantidad=[0, 1]),
        E('tienda', 'pared', 'cartel_pinturas', pared='W', cantidad=[1, 1], obligatorio=True),
        E('tienda', 'contra_pared', 'estanteria_ferreteria_baja', pared='E', llenar=True, obligatorio=True),
        E('tienda', 'contra_pared', 'estanteria_ferreteria_baja', pared='W', llenar=True, obligatorio=True),
        E('isla', 'filas', 'gondola_ferreteria', eje='x', pasillo=0.95, margen=[0.95, 0.95], obligatorio=True),
        E('tienda', 'suelo_libre', variantes=['torre_botes_pintura', 'expositor_herramientas_jardin', 'expositor_escobas', 'escalera_tijera'], cantidad=[2, 3], todas=True, obligatorio=True),
        sobre('isla', barajar(FE_TODO, 5), ['gondola_ferreteria'], relleno=[0.85, 0.97], todas=True, obligatorio=True),
        sobre('tienda', barajar(FE_PINT + FE_JARD + FE_HERR + FE_FONT, 6), ['estanteria_ferreteria_baja'], relleno=[0.85, 0.97], todas=True, obligatorio=True),
        E('tienda', 'techo', 'regleta_fluorescente', por_m2=[0.2, 0.25], obligatorio=True),
        # ---- what the rules ask of a shop: an extinguisher, the exit light, the camera and the smoke detector
        E('tienda', 'pared', 'extintor', pared=['W', 'E'], cantidad=[0, 1]),
        E('entrada', 'pared', 'senal_salida', pared=['E', 'W'], cantidad=[0, 1]),
        E('tienda', 'techo', 'camara_seguridad', cantidad=[1, 1]),
        E('tienda', 'techo', 'detector_humo', cantidad=[1, 1]),
    ],
    'iluminacion': {'fuentes': [4, 9], 'temperatura_k': [3900, 4500], 'dia': {'intensidad': 0.9}, 'noche': {'intensidad': 1.0}, 'minimo_lux_publico': 200},
    'ambiente': {'sonido': 'tienda', 'horario_defecto': 'Mo-Fr 09:00-14:00,16:30-20:00; Sa 09:00-14:00',
                 'vida': ['el tablero de llaves recién renovado', 'un saco de cemento junto a la puerta', 'la regla de latón del mostrador', 'una caja de tornillos abierta'],
                 'cerrado': 'reja bajada, la luz del mostrador encendida'},
    'minimo_objetos_distintos': 40,
}

# ================================================================== THE BOOKSHOP (librería-papelería)
LB_LIBROS = ['lb_libros_' + k for k in ('rojos', 'azules', 'verdes', 'ocres', 'negros', 'crema', 'morados', 'granates', 'mixtos_a', 'mixtos_b', 'infantiles', 'turquesas', 'grises', 'bolsillo', 'enciclopedia', 'atlas')] + ['lb_diccionarios']
LB_PAPEL = ['lb_cuadernos_espiral', 'lb_cuadernos_rojos', 'lb_carpetas_anillas', 'lb_estuches', 'lb_rotuladores', 'lb_papel_folios', 'lb_sobres', 'lb_agendas', 'lb_calculadoras', 'lb_gomas_tijeras', 'bz_pegamentos', 'bz_lapices_color', 'bz_acuarelas']
LB_CAFE = ['lb_comics_a', 'lb_comics_b', 'lb_comics_c', 'lb_comics_d']

libreria = {
    'tipologia': 'tienda_especializada', 'nombre': 'Librería-papelería',
    'nota': 'La librería-papelería de un pueblo de las Vegas Altas, con luz cálida: librerías de madera hasta el techo con libros de todos los colores, la mesa de novedades junto a la puerta, el expositor de prensa y el revistero, un sillón para hojear, '
            'cómics, láminas, juegos de mesa, la pared de la papelería y el material escolar, el mostrador de nogal con la caja y la trastienda con las cajas de libros. La puerta en z = 0, el fondo en z = D; x de -W/2 a W/2.',
    '_mood': 'libreria',
    'superficie': {'ancho': [6.3, 7.8], 'fondo': [10.5, 12.6], 'alto': 3.1},
    'variables': {'xc': 'W/2-1.8', 'z0': '1.5', 'z1': '3.3', 'zb': 'D-2.3'},
    'paso_libre': 0.9, 'pared': '#efe6d0', 'suelo': 'herringbone_parquet', 'suelo_color': '#b89868',
    'puntos': {'dependiente': ['xc+0.8', '(z0+z1)/2'], 'mostrador': ['xc-0.75', '(z0+z1)/2']},
    'pedir': 'Pagar en caja',
    'zonas': [
        Z('entrada', ['-W/2', '0', 'W/2', '1.4']),
        Z('caja', ['xc-0.3', 'z0', 'xc+0.3', 'z1'], False),
        Z('trascaja', ['xc+0.33', 'z0', 'W/2', 'z1+0.3'], False),
        Z('frente_caja', ['xc-1.3', 'z0', 'xc-0.33', 'z1']),
        Z('frente_w', ['-W/2', '1.4', '-W/2+1.0', '4.6'], False),
        Z('novedades', ['-W/2+1.2', '1.4', 'xc-1.4', '4.6']),
        Z('sala', ['-W/2', '1.4', 'W/2', 'zb']),
        Z('isla', ['-W/2+1.3', '5.0', 'W/2-1.3', 'zb']),
        Z('almacen', ['-W/2', 'zb', 'W/2', 'D'], False),
    ],
    'tabiques': [{'de': ['-W/2', 'zb'], 'a': ['W/2', 'zb'], 'puerta': ['W-1.6', 1.0]}],
    'libres': [{'rect': ['xc-1.3', 'z0', 'xc-0.3', 'z1'], 'nota': 'el sitio para pagar en el mostrador: sin muebles delante'}, {'rect': ['xc+0.35', '(z0+z1)/2-0.45', 'xc+1.25', '(z0+z1)/2+0.45'], 'nota': 'donde está el dependiente'}],
    'objetos': [
        # ---- the counter, first: the kit's own design
        E('caja', 'modulos', 'mostrador_libreria', eje='z', linea=['xc', 'z0', 'z1'], mira='-x', obligatorio=True),
        sobre('caja', 'caja_registradora', ['mostrador_libreria'], cantidad=[1, 1], obligatorio=True),
        sobre('caja', 'datafono', ['mostrador_libreria'], cantidad=[1, 1], obligatorio=True),
        sobre('caja', 'pila_bolsas_papel', ['mostrador_libreria'], cantidad=[1, 2], obligatorio=True),
        sobre('caja', 'lector_codigo', ['mostrador_libreria'], cantidad=[0, 1]),
        sobre('caja', 'lampara_lectura', ['mostrador_libreria'], cantidad=[0, 1]),
        sobre('caja', 'tarjetero', ['mostrador_libreria'], cantidad=[0, 1]),
        sobre('caja', ['lb_pila_novedad_b', 'lb_libros_cara_b'], ['mostrador_libreria'], cantidad=[0, 1]),
        E('trascaja', 'contra_pared', 'armario_trascaja', pared='E', cantidad=[1, 1], obligatorio=True),
        E('trascaja', 'pared', 'rotulo_libreria', pared='E', cantidad=[1, 1], obligatorio=True),
        E('trascaja', 'esquina', 'papelera', cantidad=[1, 1], obligatorio=True),
        sobre('trascaja', ['caja_libros', 'lb_pila_grandes'], ['armario_trascaja'], cantidad=[0, 2]),
        # ---- the storeroom
        E('almacen', 'contra_pared', 'estanteria_metalica', pared='N', cantidad=[2, 2], obligatorio=True),
        sobre('almacen', ['caja_libros', 'lb_libros_atlas', 'lb_libros_mixtos_a', 'lb_papel_folios', 'caja_carton'], ['estanteria_metalica'], relleno=[0.6, 0.9], todas=True, obligatorio=True),
        E('almacen', 'contra_pared', 'torre_cajas_libros', pared='W', cantidad=[1, 2], obligatorio=True),
        E('almacen', 'contra_pared', 'carro_libros', pared='E', cantidad=[1, 1], obligatorio=True),
        E('almacen', 'contra_pared', 'caja_libros', pared='W', cantidad=[0, 3]),
        E('almacen', 'esquina', 'escalera_libreria', cantidad=[0, 1]),
        E('almacen', 'esquina', 'fregona_cubo', cantidad=[0, 1]),
        E('almacen', 'esquina', 'escoba', cantidad=[0, 1]),
        E('almacen', 'techo', 'plafon_cristal_calido', cantidad=[1, 1], obligatorio=True),
        # ---- the door: the press, the magazines, a plant, the first light
        E('entrada', 'esquina', 'papelera', cantidad=[1, 1], obligatorio=True),
        E('entrada', 'contra_pared', 'expositor_prensa', pared='W', cantidad=[1, 1], obligatorio=True),
        E('entrada', 'esquina', 'revistero_giratorio', cantidad=[1, 1], obligatorio=True),
        E('entrada', 'esquina', 'planta_grande', cantidad=[0, 1]),
        E('entrada', 'techo', 'plafon_cristal_calido', cantidad=[1, 1], obligatorio=True),
        # ---- the west wall: low shelves with framed pictures above (the front), tall bookcases (the rest)
        E('frente_w', 'pared', variantes=['cuadro_libreria_a', 'cuadro_libreria_b', 'cuadro_libreria_c'], pared='W', cada=1.15, maximo=3, todas=True, obligatorio=True, vende='cuadro'),
        E('frente_w', 'contra_pared', 'estanteria_libros_baja', pared='W', llenar=True, obligatorio=True),
        E('sala', 'contra_pared', 'estanteria_libros_pared', pared='W', llenar=True, obligatorio=True),
        E('sala', 'contra_pared', 'estanteria_papeleria_pared', pared='E', llenar=True, obligatorio=True),
        E('sala', 'pared', 'cartel_libros_texto', pared='E', cantidad=[1, 1], obligatorio=True),
        E('sala', 'contra_pared', 'estanteria_libros_pared', pared='N', llenar=True, obligatorio=True),
        E('sala', 'pared', 'cartel_novedades', pared='N', cantidad=[1, 1], obligatorio=True),
        # ---- the new releases table (sold where it stands: «libro»), the armchair, the stands (what is sold: comics, prints, notebooks, parchís)
        E('novedades', 'conjunto', 'mesa_novedades', cantidad=[1, 2], obligatorio=True, vende='libro'),
        sobre('novedades', ['lb_pila_novedad_a', 'lb_libros_cara_a', 'lb_pila_novedad_b', 'lb_libros_cara_b', 'lb_pila_novedad_c', 'lb_pila_grandes', 'lb_libros_cara_c'], ['mesa_novedades'], por_soporte=[3, 4], todas=True, obligatorio=True),
        E('sala', 'suelo_libre', variantes=['expositor_comics', 'expositor_laminas', 'expositor_papeleria_giratorio', 'mesa_juegos_mesa'], cantidad=[4, 4], todas=True, obligatorio=True, vende=['comic', 'poster', 'cuaderno', 'parchis']),
        E('sala', 'suelo_libre', 'sillon_lectura', cantidad=[1, 2], obligatorio=True),
        E('sala', 'suelo_libre', 'mesa_auxiliar_lectura', cantidad=[1, 1]),
        E('sala', 'suelo_libre', variantes=['expositor_mochilas', 'escalera_libreria'], cantidad=[1, 2]),
        sobre('sala', 'lampara_lectura', ['mesa_auxiliar_lectura'], cantidad=[1, 1]),
        # ---- the island: browsing shelves back to back (only where the shop is deep enough)
        E('isla', 'filas', 'estanteria_libros_isla', eje='z', pasillo=1.1, margen=[0.9, 0.9]),
        # ---- the books and the stationery on their shelves
        sobre('sala', barajar(LB_LIBROS, 11), ['estanteria_libros_pared'], relleno=[0.9, 0.99], todas=True, obligatorio=True),
        sobre('frente_w', barajar(LB_LIBROS + LB_CAFE, 12), ['estanteria_libros_baja'], relleno=[0.88, 0.99], todas=True, obligatorio=True),
        sobre('isla', barajar(LB_LIBROS + LB_CAFE, 13), ['estanteria_libros_isla'], relleno=[0.88, 0.99], todas=True),
        sobre('sala', barajar(LB_PAPEL, 14), ['estanteria_papeleria_pared'], relleno=[0.85, 0.97], todas=True, obligatorio=True),
        # ---- the lights (warm pendants and opal ceiling lights)
        E('novedades', 'techo', 'lampara_colgante', cantidad=[1, 1], obligatorio=True),
        E('sala', 'techo', 'lampara_colgante', por_m2=[0.08, 0.1], obligatorio=True),
        # ---- what the rules ask of a shop: an extinguisher, the exit light, the camera and the smoke detector
        E('sala', 'pared', 'extintor', pared=['W', 'E'], cantidad=[0, 1]),
        E('entrada', 'pared', 'senal_salida', pared=['E', 'W'], cantidad=[0, 1]),
        E('sala', 'techo', 'camara_seguridad', cantidad=[1, 1]),
        E('sala', 'techo', 'detector_humo', cantidad=[1, 1]),
    ],
    'iluminacion': {'fuentes': [4, 9], 'temperatura_k': [2800, 3200], 'dia': {'intensidad': 0.8}, 'noche': {'intensidad': 1.0}, 'minimo_lux_publico': 150},
    'ambiente': {'sonido': 'tienda', 'horario_defecto': 'Mo-Fr 09:30-14:00,17:00-20:30; Sa 10:00-14:00',
                 'vida': ['un libro abierto sobre la mesa de novedades', 'la prensa del día recién puesta', 'el sillón junto a la ventana', 'cajas de libros de texto sin abrir'],
                 'cerrado': 'reja bajada, la lámpara del mostrador encendida'},
    'minimo_objetos_distintos': 40,
}

# ================================================================== THE TOYSHOP (juguetería)
JG_CAJAS = ['jg_munecas_rosa', 'jg_munecas_lila', 'jg_pistas_coches', 'jg_construccion_a', 'jg_construccion_b', 'jg_puzles_madera', 'jg_robots', 'jg_ciencia', 'jg_pizarras', 'jg_xilofonos', 'jg_juegos_mesa_a', 'jg_juegos_mesa_b', 'jg_juegos_mesa_c', 'bz_puzles', 'jg_cartas']
JG_FIGURAS = ['jg_peluche_osos', 'jg_peluche_conejos', 'jg_peluche_perros', 'jg_peluche_elefantes', 'jg_dinosaurios', 'jg_figuras_accion', 'jg_cubos_playa', 'jg_pistolas_agua', 'jg_tren_madera', 'jg_bloques_madera', 'jg_pinturas_dedos', 'bz_cochecitos', 'bz_pompas', 'bz_munecas', 'bz_pelotas_saltarinas']
JG_TODO = JG_CAJAS + JG_FIGURAS

jugueteria = {
    'tipologia': 'tienda_especializada', 'nombre': 'Juguetería',
    'nota': 'La juguetería de un pueblo de las Vegas Altas: el mostrador azul y amarillo con la caja a un lado de la puerta (el espejo del bazar: a la izquierda), muñecas, construcciones, puzles, peluches y juegos en estanterías y góndolas de colores, '
            'bicicletas y patinetes de exposición, el tren eléctrico en su mesa, la casa de muñecas, la piscina de bolas, el oso gigante, el buzón de los Reyes Magos y el almacén al fondo. La puerta en z = 0, el fondo en z = D; x de -W/2 a W/2.',
    '_mood': 'jugueteria',
    'superficie': {'ancho': [6.3, 8.1], 'fondo': [10.8, 12.9], 'alto': 3.0},
    'variables': {'xc': '-W/2+1.7', 'z0': '1.5', 'z1': '3.9', 'zb': 'D-2.2'},
    'paso_libre': 0.9, 'pared': '#f4ecd6', 'suelo': 'floor_tiles_06', 'suelo_color': '#d6d0c0',
    'puntos': {'dependiente': ['xc-0.8', '(z0+z1)/2'], 'mostrador': ['xc+0.75', '(z0+z1)/2']},
    'pedir': 'Pagar en caja',
    'zonas': [
        Z('entrada', ['-W/2', '0', 'W/2', '1.3']),
        Z('caja', ['xc-0.3', 'z0', 'xc+0.3', 'z1'], False),
        Z('trascaja', ['-W/2', 'z0', 'xc-0.33', 'z1+0.2'], False),
        Z('frente_caja', ['xc+0.33', 'z0', 'xc+1.3', 'z1']),
        Z('frente_e', ['W/2-1.0', '1.3', 'W/2', '4.9'], False),
        Z('puestos', ['xc+1.35', '1.3', 'W/2-0.9', '4.9']),
        Z('sala', ['-W/2', '1.3', 'W/2', 'zb']),
        Z('isla', ['-W/2+0.45', '5.0', 'W/2-0.45', 'zb']),
        Z('almacen', ['-W/2', 'zb', 'W/2', 'D'], False),
    ],
    'tabiques': [{'de': ['-W/2', 'zb'], 'a': ['W/2', 'zb'], 'puerta': ['W-1.6', 1.0]}],
    'libres': [{'rect': ['xc+0.3', 'z0', 'xc+1.3', 'z1'], 'nota': 'el sitio para pagar en el mostrador: sin muebles delante'}, {'rect': ['xc-1.15', '(z0+z1)/2-0.45', 'xc-0.35', '(z0+z1)/2+0.45'], 'nota': 'donde está el dependiente'}],
    'objetos': [
        # ---- the counter (on the west side), first: the kit's own design
        E('caja', 'modulos', 'mostrador_jugueteria', eje='z', linea=['xc', 'z0', 'z1'], mira='+x', obligatorio=True),
        sobre('caja', 'caja_registradora', ['mostrador_jugueteria'], cantidad=[1, 1], obligatorio=True),
        sobre('caja', 'datafono', ['mostrador_jugueteria'], cantidad=[1, 1], obligatorio=True),
        sobre('caja', 'pila_bolsas_plastico', ['mostrador_jugueteria'], cantidad=[1, 2], obligatorio=True),
        sobre('caja', 'bote_caramelos', ['mostrador_jugueteria'], cantidad=[0, 1]),
        sobre('caja', 'expositor_llaveros', ['mostrador_jugueteria'], cantidad=[0, 1]),
        sobre('caja', ['jg_cartas', 'bz_pompas', 'jg_pinturas_dedos'], ['mostrador_jugueteria'], cantidad=[0, 2]),
        E('trascaja', 'contra_pared', 'armario_trascaja', pared='W', cantidad=[1, 1], obligatorio=True),
        E('trascaja', 'pared', 'rotulo_jugueteria', pared='W', cantidad=[1, 1], obligatorio=True),
        E('trascaja', 'esquina', 'papelera', cantidad=[1, 1], obligatorio=True),
        # ---- the storeroom
        E('almacen', 'contra_pared', 'estanteria_metalica', pared='N', cantidad=[2, 2], obligatorio=True),
        sobre('almacen', ['caja_bazar_grande', 'caja_carton', 'jg_juegos_mesa_a', 'jg_juegos_mesa_c', 'jg_munecas_rosa'], ['estanteria_metalica'], relleno=[0.6, 0.9], todas=True, obligatorio=True),
        E('almacen', 'contra_pared', 'torre_cajas_bazar', pared='W', cantidad=[1, 2], obligatorio=True),
        E('almacen', 'contra_pared', variantes=['bici_infantil_azul', 'triciclo_rojo', 'patinete_juguete'], pared='E', cantidad=[2, 2], todas=True, obligatorio=True),
        E('almacen', 'contra_pared', 'caja_bazar_grande', pared='W', cantidad=[0, 3]),
        E('almacen', 'esquina', 'fregona_cubo', cantidad=[0, 1]),
        E('almacen', 'esquina', 'escoba', cantidad=[0, 1]),
        E('almacen', 'techo', 'plafon_pequeno', cantidad=[1, 1], obligatorio=True),
        # ---- the door
        E('entrada', 'esquina', 'papelera', cantidad=[1, 1], obligatorio=True),
        E('entrada', 'esquina', 'buzon_reyes_magos', cantidad=[1, 1], obligatorio=True),
        E('entrada', 'esquina', 'planta_grande', cantidad=[0, 1]),
        E('entrada', 'techo', 'lampara_panel_led', cantidad=[1, 1], obligatorio=True),
        # ---- the east wall: low shelves with the bunting and the campaign poster above; tall shelves for the rest of both walls
        E('frente_e', 'pared', 'cartel_juguetes', pared='E', cantidad=[1, 1], obligatorio=True),
        E('frente_e', 'pared', 'guirnalda_banderines', pared='E', cantidad=[1, 2], obligatorio=True),
        E('frente_e', 'contra_pared', 'estanteria_jugueteria_baja', pared='E', llenar=True, obligatorio=True),
        E('sala', 'contra_pared', 'estanteria_jugueteria_pared', pared='E', llenar=True, obligatorio=True),
        E('sala', 'contra_pared', 'estanteria_jugueteria_pared', pared='W', llenar=True, obligatorio=True),
        E('sala', 'contra_pared', 'estanteria_jugueteria_pared', pared='N', llenar=True),
        # ---- the play table: the electric train (the first thing a child sees)
        E('sala', 'conjunto', 'mesa_tren_juguete', cantidad=[1, 1], obligatorio=True),
        # ---- what is sold where it stands: the giant bear, the balls, the board games; kites, comics and posters
        E('puestos', 'suelo_libre', variantes=['bici_infantil_roja', 'bici_infantil_azul', 'patinete_juguete', 'triciclo_rojo'], cantidad=[1, 3], todas=True, obligatorio=True),
        E('puestos', 'suelo_libre', variantes=['oso_gigante_trono', 'red_balones'], cantidad=[2, 2], todas=True, obligatorio=True, vende=['peluche', 'balon']),
        E('sala', 'suelo_libre', 'mesa_juegos_mesa', cantidad=[1, 1], obligatorio=True, vende='parchis'),
        E('sala', 'suelo_libre', variantes=['expositor_cometas', 'expositor_comics', 'expositor_posters'], cantidad=[3, 3], todas=True, obligatorio=True, vende=['cometa', 'comic', 'poster']),
        E('sala', 'suelo_libre', variantes=['casa_munecas', 'cubo_pelotas_grande', 'percha_disfraces'], cantidad=[2, 3], todas=True, obligatorio=True),
        # ---- the aisles: back-to-back gondolas with blue ends
        E('isla', 'filas', 'gondola_jugueteria', eje='z', pasillo=1.2, margen=[1.0, 1.0]),
        sobre('isla', barajar(JG_TODO, 21), ['gondola_jugueteria'], relleno=[0.85, 0.98], todas=True),
        sobre('frente_e', barajar(JG_TODO, 22), ['estanteria_jugueteria_baja'], relleno=[0.85, 0.98], todas=True, obligatorio=True),
        sobre('sala', barajar(JG_TODO, 23), ['estanteria_jugueteria_pared'], relleno=[0.85, 0.98], todas=True, obligatorio=True),
        # ---- the lights
        E('sala', 'techo', 'lampara_panel_led', por_m2=[0.09, 0.11], obligatorio=True),
        # ---- what the rules ask of a shop: an extinguisher, the exit light, the camera and the smoke detector
        E('sala', 'pared', 'extintor', pared=['W', 'E'], cantidad=[0, 1]),
        E('entrada', 'pared', 'senal_salida', pared=['E', 'W'], cantidad=[0, 1]),
        E('sala', 'techo', 'camara_seguridad', cantidad=[1, 1]),
        E('sala', 'techo', 'detector_humo', cantidad=[1, 1]),
    ],
    'iluminacion': {'fuentes': [4, 9], 'temperatura_k': [3800, 4400], 'dia': {'intensidad': 0.9}, 'noche': {'intensidad': 1.0}, 'minimo_lux_publico': 200},
    'ambiente': {'sonido': 'tienda', 'horario_defecto': 'Mo-Sa 10:00-14:00,17:00-20:30',
                 'vida': ['el tren da vueltas sobre su mesa', 'una bici de exposición junto a la puerta', 'cartas a los Reyes Magos en el buzón', 'peluches por todas partes'],
                 'cerrado': 'reja bajada, el escaparate iluminado'},
    'minimo_objetos_distintos': 40,
}

# ================================================================== THE FLORIST (floristería)
FL_CUBOS = ['cubo_flores_' + k for k in ('rosas_rojas', 'rosas_rosas', 'rosas_blancas', 'claveles_rojos', 'claveles_blancos', 'girasoles', 'margaritas', 'lirios', 'tulipanes', 'gerberas', 'gladiolos', 'crisantemos', 'lavanda', 'eucalipto', 'paniculata', 'hortensias')]
FL_PLANTAS = ['fl_ficus', 'fl_orquidea_blanca', 'fl_orquidea_rosa', 'fl_helecho', 'fl_sansevieria', 'fl_begonia', 'fl_crasas', 'fl_flor_pascua', 'fl_lavanda', 'fl_cactus_columnar']

floristeria = {
    'tipologia': 'tienda_especializada', 'nombre': 'Floristería',
    'nota': 'La floristería de un pueblo de las Vegas Altas: cubos de zinc con flores cortadas de todos los colores en escalerillas y por el suelo, plantas en maceta sobre mesas y estantes, el mostrador encalado con tapa de zinc y su caja, '
            'la mesa de trabajo con los rollos de papel y las cintas, la pila de agua, la puerta de la cámara fría y un almacén con tierra y macetas. La puerta en z = 0, el fondo en z = D; x de -W/2 a W/2.',
    '_mood': 'floristeria',
    'superficie': {'ancho': [5.4, 6.9], 'fondo': [11.4, 12.9], 'alto': 3.0},
    'variables': {'zm': 'D-5.4', 'zb': 'D-2.4'},
    'paso_libre': 0.9, 'pared': '#eef2e6', 'suelo': 'rock_tile_floor', 'suelo_color': '#bfbbae',
    'puntos': {'dependiente': ['0.5', 'zm+0.8'], 'mostrador': ['0.5', 'zm-0.75']},
    'pedir': 'Pagar en el mostrador',
    'zonas': [
        Z('entrada', ['-W/2', '0', 'W/2', '1.3']),
        Z('sala', ['-W/2', '1.3', 'W/2', 'zm-0.9']),
        Z('mostrador', ['-W/2+1.5', 'zm-0.35', 'W/2', 'zm+0.35'], False),
        Z('taller', ['-W/2', 'zm+0.37', 'W/2', 'zb'], False),
        Z('fondo', ['-W/2', 'zb', 'W/2-2.2', 'D'], False),
        Z('almacen', ['W/2-2.2', 'zb', 'W/2', 'D'], False),
    ],
    'tabiques': [
        {'de': ['W/2-2.2', 'zb'], 'a': ['W/2-2.2', 'D']},
        {'de': ['W/2-2.2', 'zb'], 'a': ['W/2', 'zb'], 'puerta': ['0.2', 1.0]},
    ],
    'libres': [{'rect': ['-W/2', 'zm-0.9', 'W/2', 'zm-0.36'], 'nota': 'la cola delante del mostrador: sin muebles'},
               {'rect': ['-W/2', 'zm-1.7', '-W/2+1.6', 'zm+1.1'], 'nota': 'el paso del personal entre la sala y el taller'},
               {'rect': ['W/2-2.4', 'zb-1.3', 'W/2-0.7', 'zb'], 'nota': 'el paso hasta la puerta del almacén'},
               {'rect': ['0.05', 'zm+0.35', '0.95', 'zm+1.25'], 'nota': 'donde está la dependienta'}],
    'objetos': [
        # ---- the counter across the shop, first: the kit's own design
        E('mostrador', 'modulos', 'mostrador_floristeria', eje='x', linea=['zm', '-W/2+1.5', 'W/2'], mira='-z', obligatorio=True),
        sobre('mostrador', 'caja_registradora', ['mostrador_floristeria'], cantidad=[1, 1], obligatorio=True),
        sobre('mostrador', 'datafono', ['mostrador_floristeria'], cantidad=[1, 1], obligatorio=True),
        sobre('mostrador', 'portabobinas_cintas', ['mostrador_floristeria'], cantidad=[1, 1], obligatorio=True),
        sobre('mostrador', 'jarron_flores_mostrador', ['mostrador_floristeria'], cantidad=[1, 1], obligatorio=True),
        sobre('mostrador', ['ramo_envuelto_rosas', 'ramo_envuelto_primavera'], ['mostrador_floristeria'], cantidad=[1, 2], todas=True, obligatorio=True),
        sobre('mostrador', 'tarjetero_dedicatorias', ['mostrador_floristeria'], cantidad=[0, 1]),
        sobre('mostrador', ['rollo_papel_regalo', 'cesta_mimbre_flores'], ['mostrador_floristeria'], cantidad=[0, 1]),
        # ---- behind the counter: the work table, the sink, the paper, the cold room, the vases
        E('taller', 'conjunto', 'mesa_trabajo_floristeria', cantidad=[1, 1], obligatorio=True),
        sobre('taller', 'tijeras_floristeria', ['mesa_trabajo_floristeria'], cantidad=[1, 1], obligatorio=True),
        sobre('taller', ['ramo_envuelto_primavera', 'cesta_mimbre_flores', 'rollo_papel_regalo', 'portabobinas_cintas', 'tarjetero_dedicatorias'], ['mesa_trabajo_floristeria'], cantidad=[1, 3], todas=True),
        sobre('taller', 'cubo_flores_eucalipto', ['mesa_trabajo_floristeria'], cantidad=[0, 1]),
        E('taller', 'pared', 'rollos_papel_pared', pared=['W', 'E'], cantidad=[1, 1], obligatorio=True),
        E('taller', 'pared', 'rotulo_floristeria', pared='E', cantidad=[1, 1], obligatorio=True),
        E('taller', 'pared', 'estante_floristeria_pared', pared=['E', 'W'], cantidad=[1, 1], obligatorio=True),
        E('taller', 'contra_pared', 'fregadero_floristeria', pared='W', cantidad=[0, 1]),
        E('taller', 'esquina', variantes=['saco_tierra', 'regadera_zinc', 'macetero_grande_b'], cantidad=[1, 2], todas=True),
        E('taller', 'esquina', 'papelera', cantidad=[1, 1], obligatorio=True),
        sobre('taller', 'fl_jarrones', ['estante_floristeria_pared'], relleno=[0.8, 0.95], obligatorio=True),
        E('fondo', 'contra_pared', 'puerta_camara_frio', pared='N', cantidad=[1, 1], obligatorio=True),
        E('fondo', 'esquina', variantes=['cubo_flores_rosas_blancas', 'cubo_flores_gladiolos'], cantidad=[0, 2]),
        E('taller', 'techo', 'lampara_panel_led', cantidad=[2, 2], obligatorio=True),
        # ---- the storeroom (soil, pots, vases)
        E('almacen', 'contra_pared', 'estanteria_metalica', pared='N', cantidad=[1, 1], obligatorio=True),
        sobre('almacen', ['fl_macetas_apiladas', 'caja_carton', 'fl_jarrones'], ['estanteria_metalica'], relleno=[0.6, 0.9], todas=True, obligatorio=True),
        E('almacen', 'contra_pared', 'saco_tierra', pared='W', cantidad=[2, 3], obligatorio=True),
        E('almacen', 'contra_pared', variantes=['regadera_zinc', 'caja_carton'], pared='E', cantidad=[1, 2]),
        E('almacen', 'esquina', 'fregona_cubo', cantidad=[0, 1]),
        E('almacen', 'techo', 'plafon_pequeno', cantidad=[1, 1], obligatorio=True),
        # ---- the door
        E('entrada', 'esquina', 'papelera', cantidad=[1, 1], obligatorio=True),
        E('entrada', 'esquina', variantes=['macetero_grande_a', 'planta_alta'], cantidad=[1, 2], todas=True),
        E('entrada', 'suelo_libre', variantes=['cubo_flores_girasoles', 'cubo_flores_margaritas', 'cubo_flores_tulipanes'], cantidad=[1, 2]),
        E('entrada', 'techo', 'lampara_panel_led', cantidad=[1, 1], obligatorio=True),
        # ---- the sales floor: the plants table first (it asks for room round it), the stepped stands with their buckets (sold where they stand: flowers), then the plants (geraniums, cactus, indoor plants)
        E('sala', 'contra_pared', 'escalera_cubos_flores', pared='W', cantidad=[1, 3], obligatorio=True),
        E('sala', 'contra_pared', 'escalera_cubos_flores', pared='E', cantidad=[0, 3]),
        E('sala', 'conjunto', 'mesa_plantas_floristeria', cantidad=[1, 2], obligatorio=True),
        sobre('sala', barajar(FL_PLANTAS, 32), ['mesa_plantas_floristeria'], por_soporte=[3, 4], todas=True, obligatorio=True),
        sobre('sala', barajar(FL_CUBOS, 31), ['escalera_cubos_flores'], por_soporte=[3, 3], todas=True, obligatorio=True, vende='flores'),
        E('sala', 'suelo_libre', 'expositor_geranios', cantidad=[1, 1], obligatorio=True, vende='geranios'),
        E('sala', 'suelo_libre', 'expositor_cactus', cantidad=[1, 1], obligatorio=True, vende='cactus'),
        E('sala', 'suelo_libre', 'estante_plantas_interior', cantidad=[1, 1], obligatorio=True, vende='planta'),
        sobre('sala', barajar(FL_PLANTAS, 33), ['estante_plantas_interior'], por_soporte=[3, 4], todas=True),
        E('sala', 'suelo_libre', variantes=FL_CUBOS[::-1], cantidad=[3, 6], todas=True),
        E('sala', 'suelo_libre', variantes=['macetero_grande_a', 'macetero_grande_b', 'planta_alta', 'planta_grande'], cantidad=[1, 2]),
        E('sala', 'pared', 'pizarra_floristeria', pared='E', cantidad=[0, 1]),
        E('sala', 'pared', 'cartel_ramos', pared='W', cantidad=[0, 1]),
        E('sala', 'pared', variantes=['cuadro_botanico_a', 'cuadro_botanico_b', 'cuadro_botanico_c'], pared=['W', 'E'], cada=1.2, maximo=4, todas=True, obligatorio=True),
        E('sala', 'pared', 'estante_floristeria_pared', pared=['E', 'W'], cantidad=[0, 2]),
        sobre('sala', 'fl_jarrones', ['estante_floristeria_pared'], relleno=[0.8, 0.95]),
        E('sala', 'techo', 'planta_colgante', cantidad=[2, 3], obligatorio=True),
        E('sala', 'techo', 'lampara_panel_led', por_m2=[0.12, 0.16], obligatorio=True),
        # ---- what the rules ask of a shop: an extinguisher, the exit light, the camera and the smoke detector
        E('sala', 'pared', 'extintor', pared=['W', 'E'], cantidad=[0, 1]),
        E('entrada', 'pared', 'senal_salida', pared=['E', 'W'], cantidad=[0, 1]),
        E('sala', 'techo', 'camara_seguridad', cantidad=[1, 1]),
        E('sala', 'techo', 'detector_humo', cantidad=[1, 1]),
    ],
    'iluminacion': {'fuentes': [4, 9], 'temperatura_k': [3900, 4400], 'dia': {'intensidad': 0.9}, 'noche': {'intensidad': 1.0}, 'minimo_lux_publico': 200},
    'ambiente': {'sonido': 'tienda', 'horario_defecto': 'Mo-Sa 09:30-14:00,17:00-20:30; Su 10:00-13:30',
                 'vida': ['gotas de agua en el suelo junto a los cubos', 'un ramo a medio atar sobre la mesa', 'hojas cortadas en el suelo del taller', 'el olor a flor recién cortada'],
                 'cerrado': 'persiana bajada, los cubos dentro de la cámara'},
    'minimo_objetos_distintos': 40,
}

# ================================================================== THE ESTANCO (tobacco, lottery and press)
ES_PRENSA = ['es_pila_periodicos', 'es_pila_revistas']
ES_DULCES = ['bote_caramelos', 'expositor_mecheros']

estanco = {
    'tipologia': 'tienda_especializada', 'nombre': 'Estanco (tabaco, lotería y prensa)',
    'nota': 'El estanco de un pueblo de las Vegas Altas: un mostrador largo de madera con tapa de piedra, detrás los muebles de cajetillas genéricas (sin marca) y el terminal de lotería, en el mostrador la vitrina de décimos y sellos, mecheros y la caja, '
            'revisteros de pared, islas de prensa y el expositor de prensa junto a la puerta, golosinas y chocolate, postales, el cartel de recargas de móvil y la trastienda con los fardos de la prensa. La puerta en z = 0, el fondo en z = D; x de -W/2 a W/2.',
    '_mood': 'estanco',
    'superficie': {'ancho': [5.7, 6.9], 'fondo': [9.3, 10.8], 'alto': 3.0},
    'variables': {'xc': 'W/2-1.8', 'z0': '1.4', 'z1': '5.0', 'zb': 'D-1.9'},
    'paso_libre': 0.9, 'pared': '#efe8d6', 'suelo': 'floor_tiles_06', 'suelo_color': '#c0b49c',
    'puntos': {'dependiente': ['xc+0.8', '(z0+z1)/2'], 'mostrador': ['xc-0.75', '(z0+z1)/2']},
    'pedir': 'Pedir en el mostrador',
    'zonas': [
        Z('entrada', ['-W/2', '0', 'W/2', '1.3']),
        Z('caja', ['xc-0.3', 'z0', 'xc+0.3', 'z1'], False),
        Z('trascaja', ['xc+0.33', 'z0', 'W/2', 'z1+0.3'], False),
        Z('frente_caja', ['xc-1.3', 'z0', 'xc-0.33', 'z1']),
        Z('sala', ['-W/2', '1.3', 'W/2', 'zb']),
        Z('centro', ['-W/2+1.5', '1.9', 'xc-1.4', 'zb-0.3']),
        Z('almacen', ['-W/2', 'zb', 'W/2', 'D'], False),
    ],
    'tabiques': [{'de': ['-W/2', 'zb'], 'a': ['W/2', 'zb'], 'puerta': ['W-1.6', 1.0]}],
    'libres': [{'rect': ['xc-1.3', 'z0', 'xc-0.3', 'z1'], 'nota': 'el sitio para pedir en el mostrador: sin muebles delante'}, {'rect': ['xc+0.35', '(z0+z1)/2-0.45', 'xc+1.25', '(z0+z1)/2+0.45'], 'nota': 'donde está el dependiente'}],
    'objetos': [
        # ---- the counter, first: the kit's own design
        E('caja', 'modulos', 'mostrador_estanco', eje='z', linea=['xc', 'z0', 'z1'], mira='-x', obligatorio=True),
        sobre('caja', 'vitrina_loteria', ['mostrador_estanco'], cantidad=[1, 1], obligatorio=True),
        sobre('caja', 'caja_registradora', ['mostrador_estanco'], cantidad=[1, 1], obligatorio=True),
        sobre('caja', 'terminal_loteria', ['mostrador_estanco'], cantidad=[1, 1], obligatorio=True),
        sobre('caja', 'expositor_mecheros', ['mostrador_estanco'], cantidad=[1, 1], obligatorio=True),
        sobre('caja', 'expositor_sellos', ['mostrador_estanco'], cantidad=[1, 1], obligatorio=True),
        sobre('caja', 'datafono', ['mostrador_estanco'], cantidad=[1, 1], obligatorio=True),
        sobre('caja', 'balanza_postal', ['mostrador_estanco'], cantidad=[1, 1], obligatorio=True),
        sobre('caja', ['es_pila_periodicos', 'es_pila_revistas', 'bote_caramelos', 'expositor_llaveros', 'sello_tampon', 'expositor_pilas_mostrador'], ['mostrador_estanco'], cantidad=[0, 3], todas=True),
        # ---- behind it: the sign first (it hangs over what fills the wall), the cabinets of packs (generic), the clock
        E('trascaja', 'pared', 'rotulo_estanco', pared='E', cantidad=[1, 1], obligatorio=True),
        E('trascaja', 'contra_pared', variantes=['mueble_tabaco_a', 'mueble_tabaco_b', 'mueble_tabaco_c'], pared='E', llenar=True, todas=True, obligatorio=True),
        E('trascaja', 'esquina', 'papelera', cantidad=[1, 1], obligatorio=True),
        E('trascaja', 'suelo_libre', 'silla_madera', cantidad=[0, 1]),
        E('trascaja', 'pared', variantes=['reloj_pared', 'calendario_pared'], pared='N', cantidad=[0, 2]),
        # ---- the storeroom
        E('almacen', 'contra_pared', 'estanteria_metalica', pared='N', cantidad=[1, 2], obligatorio=True),
        sobre('almacen', ['caja_carton', 'es_pila_revistas', 'es_pila_periodicos', 'es_chocolatinas'], ['estanteria_metalica'], relleno=[0.6, 0.9], todas=True, obligatorio=True),
        E('almacen', 'contra_pared', 'fardos_prensa', pared='W', cantidad=[1, 2], obligatorio=True),
        E('almacen', 'contra_pared', 'torre_cajas_bazar', pared='E', cantidad=[0, 1]),
        E('almacen', 'esquina', 'fregona_cubo', cantidad=[0, 1]),
        E('almacen', 'esquina', 'escoba', cantidad=[0, 1]),
        E('almacen', 'techo', 'plafon_pequeno', cantidad=[1, 1], obligatorio=True),
        # ---- the door: the press stand, the magazine spinner, the cell-phone accessories, the age sign
        E('entrada', 'esquina', 'papelera', cantidad=[1, 1], obligatorio=True),
        E('entrada', 'pared', 'panel_cargadores', pared='E', cantidad=[1, 1], obligatorio=True, vende='cargador'),
        E('entrada', 'pared', 'cartel_menores', pared='W', cantidad=[1, 1], obligatorio=True),
        E('entrada', 'contra_pared', 'expositor_prensa', pared='W', cantidad=[1, 1], obligatorio=True),
        E('entrada', 'esquina', 'revistero_giratorio', cantidad=[1, 1], obligatorio=True),
        E('entrada', 'techo', 'regleta_led', cantidad=[1, 1], obligatorio=True),
        # ---- the signs over the racks (lottery on the back wall, top-ups and stamps on the west), then the racks and shelves they hang over
        E('sala', 'pared', 'cartel_loteria', pared='N', cantidad=[1, 1], obligatorio=True),
        E('sala', 'pared', variantes=['cartel_recargas', 'cartel_sellos'], pared='W', cantidad=[2, 2], todas=True, obligatorio=True),
        E('sala', 'contra_pared', variantes=['revistero_pared_a', 'revistero_pared_b'], pared='W', llenar=True, todas=True, obligatorio=True),
        E('sala', 'contra_pared', 'estanteria_estanco_pared', pared='N', llenar=True, obligatorio=True),
        # ---- what is sold where it stands: chocolate and sweets, notebooks; the press islands, the postcards
        E('sala', 'suelo_libre', 'expositor_golosinas', cantidad=[1, 1], obligatorio=True, vende='chocolate'),
        E('sala', 'suelo_libre', 'expositor_papeleria_giratorio', cantidad=[1, 1], obligatorio=True, vende='cuaderno'),
        E('centro', 'suelo_libre', 'isla_revistas', cantidad=[1, 2], obligatorio=True),
        E('sala', 'suelo_libre', variantes=['expositor_postales', 'expositor_cuadernos', 'revistero_giratorio'], cantidad=[1, 3], todas=True),
        E('sala', 'esquina', 'planta_grande', cantidad=[0, 1]),
        sobre('sala', barajar(['es_chocolatinas', 'es_chicles', 'es_caramelos_bolsas', 'es_pipas_bolsas', 'es_panuelos', 'es_cerillas_mecheros', 'es_tarjetas_regalo', 'bz_pilas', 'lb_cuadernos_espiral', 'lb_rotuladores', 'bz_pegamentos', 'lb_sobres'], 71), ['estanteria_estanco_pared'], relleno=[0.88, 0.98], todas=True, obligatorio=True),
        E('sala', 'techo', 'regleta_led', por_m2=[0.07, 0.09], obligatorio=True),
        # ---- what the rules ask of a shop: an extinguisher, the exit light, the camera and the smoke detector
        E('sala', 'pared', 'extintor', pared=['W', 'E'], cantidad=[0, 1]),
        E('entrada', 'pared', 'senal_salida', pared=['E', 'W'], cantidad=[0, 1]),
        E('sala', 'techo', 'camara_seguridad', cantidad=[1, 1]),
        E('sala', 'techo', 'detector_humo', cantidad=[1, 1]),
    ],
    'iluminacion': {'fuentes': [4, 9], 'temperatura_k': [3700, 4300], 'dia': {'intensidad': 0.9}, 'noche': {'intensidad': 1.0}, 'minimo_lux_publico': 180},
    'ambiente': {'sonido': 'tienda', 'horario_defecto': 'Mo-Fr 07:30-14:00,16:30-20:30; Sa 08:00-14:00,17:00-20:00',
                 'vida': ['la prensa del día recién colocada', 'décimos de lotería en la vitrina', 'un mechero olvidado sobre el mostrador', 'revistas del corazón en el revistero'],
                 'cerrado': 'reja bajada, el rótulo encendido'},
    'minimo_objetos_distintos': 40,
}

# ================================================================== THE JEWELLER-WATCHMAKER / OPTICIAN (joyería)
JY_BANDEJAS = ['jy_bandeja_anillos', 'jy_bandeja_relojes', 'jy_busto_collares', 'jy_expositor_pendientes', 'jy_estuches_joyas', 'jy_cojin_alianzas', 'expositor_gafas_mostrador']

joyeria = {
    'tipologia': 'tienda_especializada', 'nombre': 'Joyería-relojería y óptica',
    'nota': 'La joyería-relojería y óptica de un pueblo de las Vegas Altas, con luz cálida y alfombra: mostradores de cristal con anillos, relojes y collares, la vitrina de isla, vitrinas de pared con relojes y perfumes, la pared de monturas de gafas con su espejo y la mesita para probárselas, '
            'la consola con bandejas de terciopelo, detrás del mostrador el banco del relojero con su lámpara y su lupa, la caja fuerte y las vitrinas de joyas, y una trastienda con cajas. La puerta en z = 0, el fondo en z = D; x de -W/2 a W/2.',
    '_mood': 'joyeria',
    'superficie': {'ancho': [5.7, 6.9], 'fondo': [10.8, 12.3], 'alto': 3.0},
    'variables': {'zm': 'D-4.7', 'zb': 'D-1.9'},
    'paso_libre': 0.9, 'pared': '#f0e8da', 'suelo': 'rock_tile_floor', 'suelo_color': '#c6beb0',
    'puntos': {'dependiente': ['W/2-0.6', 'zm+0.8'], 'mostrador': ['W/2-0.6', 'zm-0.75']},
    'pedir': 'Pagar en el mostrador',
    'zonas': [
        Z('entrada', ['-W/2', '0', 'W/2', '1.3']),
        Z('sala', ['-W/2', '1.3', 'W/2', 'zm-0.9']),
        Z('mostrador', ['W/2-3.6', 'zm-0.35', 'W/2', 'zm+0.35'], False),
        Z('taller', ['-W/2', 'zm+0.37', 'W/2', 'zb'], False),
        Z('almacen', ['-W/2', 'zb', 'W/2', 'D'], False),
    ],
    'tabiques': [{'de': ['-W/2', 'zb'], 'a': ['W/2', 'zb'], 'puerta': ['W-1.6', 1.0]}],
    'libres': [{'rect': ['W/2-3.6', 'zm-0.9', 'W/2', 'zm-0.36'], 'nota': 'la cola delante del mostrador: sin muebles'},
               {'rect': ['-W/2', 'zm-0.9', 'W/2-3.6', 'zm+0.9'], 'nota': 'el paso del personal entre la sala y el taller'},
               {'rect': ['W/2-1.05', 'zm+0.35', 'W/2-0.15', 'zm+1.25'], 'nota': 'donde está el dependiente'}],
    'objetos': [
        # ---- the counter, first: glass cases for the watches, the rings and the necklaces, the cash desk at the east end
        E('mostrador', 'modulos', 'vitrina_mostrador_relojes', eje='x', linea=['zm', 'W/2-3.6', 'W/2-2.4'], mira='-z', obligatorio=True),
        E('mostrador', 'modulos', 'vitrina_mostrador_anillos', eje='x', linea=['zm', 'W/2-2.4', 'W/2-1.2'], mira='-z', obligatorio=True),
        E('mostrador', 'modulos', 'mostrador_caja_joyeria', eje='x', linea=['zm', 'W/2-1.2', 'W/2'], mira='-z', obligatorio=True),
        sobre('mostrador', 'caja_registradora', ['mostrador_caja_joyeria'], cantidad=[1, 1], obligatorio=True),
        sobre('mostrador', 'datafono', ['mostrador_caja_joyeria'], cantidad=[1, 1], obligatorio=True),
        sobre('mostrador', 'balanza_precision', ['mostrador_caja_joyeria'], cantidad=[1, 1], obligatorio=True),
        sobre('mostrador', ['jy_lupa_y_pinzas', 'jy_cojin_alianzas', 'jy_estuches_joyas', 'pila_bolsas_papel', 'tarjetero', 'bolsa_papel_grande'], ['mostrador_caja_joyeria'], cantidad=[2, 3], todas=True),
        E('mostrador', 'techo', 'foco_empotrable', cantidad=[2, 2], obligatorio=True),
        # ---- behind it: the wall of cases, the sign above, the safe, the watchmaker's bench
        E('taller', 'pared', 'rotulo_joyeria', pared='N', cantidad=[1, 1], obligatorio=True),
        E('taller', 'contra_pared', variantes=['vitrina_pared_joyas', 'vitrina_pared_relojes'], pared='N', llenar=True, todas=True, obligatorio=True),
        E('taller', 'contra_pared', 'banco_relojero', pared='W', cantidad=[1, 1], obligatorio=True),
        sobre('taller', ['jy_lupa_y_pinzas', 'lampara_escritorio'], ['banco_relojero'], cantidad=[1, 2], todas=True),
        E('taller', 'pared', 'cartel_arreglos', pared='W', cantidad=[1, 1], obligatorio=True),
        E('taller', 'esquina', 'taburete_relojero', cantidad=[1, 1], obligatorio=True),
        E('taller', 'contra_pared', 'caja_fuerte_pequena', pared='E', cantidad=[1, 1], obligatorio=True),
        E('taller', 'esquina', 'papelera', cantidad=[1, 1], obligatorio=True),
        E('taller', 'pared', variantes=['reloj_pared', 'calendario_pared'], pared='E', cantidad=[0, 1]),
        E('taller', 'techo', 'plafon_cristal_calido', cantidad=[1, 1], obligatorio=True),
        # ---- the storeroom
        E('almacen', 'contra_pared', 'estanteria_metalica', pared='N', cantidad=[1, 2], obligatorio=True),
        sobre('almacen', ['jy_estuches_joyas', 'caja_carton', 'jy_bandeja_relojes', 'jy_bandeja_anillos'], ['estanteria_metalica'], relleno=[0.6, 0.9], todas=True, obligatorio=True),
        E('almacen', 'contra_pared', 'caja_carton', pared='W', cantidad=[2, 3], obligatorio=True),
        E('almacen', 'contra_pared', 'torre_cajas_bazar', pared='E', cantidad=[0, 1]),
        E('almacen', 'esquina', 'fregona_cubo', cantidad=[0, 1]),
        E('almacen', 'techo', 'plafon_pequeno', cantidad=[1, 1], obligatorio=True),
        # ---- the door
        E('entrada', 'esquina', 'papelera', cantidad=[1, 1], obligatorio=True),
        E('entrada', 'contra_pared', 'reloj_pendulo_pie', pared='W', cantidad=[1, 1], obligatorio=True),
        E('entrada', 'esquina', 'planta_grande', cantidad=[1, 1]),
        E('entrada', 'techo', 'plafon_cristal_calido', cantidad=[1, 1], obligatorio=True),
        # ---- the east wall: cases of watches and perfumes (sold where they stand) and the console; the west: the glasses (sold where they stand)
        E('sala', 'contra_pared', variantes=['vitrina_pared_relojes', 'vitrina_perfumes'], pared='E', cantidad=[2, 2], todas=True, obligatorio=True, vende=['reloj', 'perfume']),
        E('sala', 'contra_pared', 'consola_joyeria', pared='E', cantidad=[0, 1]),
        sobre('sala', barajar(JY_BANDEJAS, 91), ['consola_joyeria'], cantidad=[0, 4], todas=True),
        E('sala', 'pared', variantes=['pared_gafas_a', 'pared_gafas_b'], pared='W', cantidad=[2, 2], todas=True, obligatorio=True, vende='gafas'),
        E('sala', 'pared', 'cartel_optica', pared='W', cantidad=[1, 1], obligatorio=True),
        E('sala', 'conjunto', 'mesa_optica', sillas={'variantes': ['silla_cliente_joyeria'], 'n': [2, 2]}, cantidad=[1, 1], obligatorio=True),
        sobre('sala', ['espejo_optica_mesa', 'expositor_gafas_mostrador'], ['mesa_optica'], cantidad=[1, 2], todas=True),
        E('sala', 'conjunto', 'vitrina_isla_joyas', cantidad=[1, 1], obligatorio=True),
        E('sala', 'conjunto', 'vitrina_isla_relojes', cantidad=[0, 1]),
        E('sala', 'conjunto', 'vitrina_mostrador_collares', cantidad=[0, 1]),
        E('sala', 'suelo_libre', 'maniqui_busto_joyas', cantidad=[1, 2], obligatorio=True),
        E('sala', 'suelo_libre', 'expositor_gafas', cantidad=[1, 1], obligatorio=True, vende='gafas'),
        E('sala', 'pared', variantes=['cuadro_joyeria_a', 'cuadro_joyeria_b'], pared=['W', 'E'], cantidad=[1, 2], todas=True, obligatorio=True),
        E('sala', 'pared', 'espejo_pared_grande', pared=['W', 'E'], cantidad=[0, 1]),
        E('sala', 'suelo_libre', variantes=['alfombra_burdeos', 'alfombra_verde'], cantidad=[1, 1], obligatorio=True),
        E('sala', 'esquina', 'planta_grande', cantidad=[0, 1]),
        E('sala', 'techo', 'plafon_cristal_calido', por_m2=[0.1, 0.13], obligatorio=True),
        # ---- what the rules ask of a shop: an extinguisher, the exit light, the camera and the smoke detector
        E('sala', 'pared', 'extintor', pared=['W', 'E'], cantidad=[0, 1]),
        E('entrada', 'pared', 'senal_salida', pared=['E', 'W'], cantidad=[0, 1]),
        E('sala', 'techo', 'camara_seguridad', cantidad=[1, 1]),
        E('sala', 'techo', 'detector_humo', cantidad=[1, 1]),
    ],
    'iluminacion': {'fuentes': [4, 9], 'temperatura_k': [2800, 3200], 'dia': {'intensidad': 0.8}, 'noche': {'intensidad': 1.0}, 'minimo_lux_publico': 150},
    'ambiente': {'sonido': 'tienda', 'horario_defecto': 'Mo-Fr 10:00-14:00,17:00-20:30; Sa 10:00-14:00',
                 'vida': ['un reloj abierto sobre el banco del relojero', 'una bandeja de anillos recién sacada', 'la lupa sobre el mostrador', 'las gafas de prueba junto al espejo'],
                 'cerrado': 'reja bajada, las vitrinas iluminadas'},
    'minimo_objetos_distintos': 40,
}

if __name__ == '__main__':
    escribir('bazar', bazar)
    escribir('ferreteria', ferreteria)
    escribir('libreria', libreria)
    escribir('jugueteria', jugueteria)
    escribir('floristeria', floristeria)
    escribir('estanco', estanco)
    escribir('joyeria', joyeria)
