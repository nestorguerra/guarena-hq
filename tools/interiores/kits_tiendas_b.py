# The eight kits of the «tiendas_b» family (technical backlog, I-02): the furniture showroom, the household-appliance and
# electronics shop, the computer and phone shop, the bakery, the greengrocer, the perfumery, the hairdresser and the car
# workshop — written to data/kits/<kit>.json from here, so that a rule is written once and read well. The objects they
# name are in tools/interiores/catalogo_tiendas_b.py (tb_<tienda>.py); the moodboards (Wikimedia Commons: page, author and
# licence, never the picture) in tools/interiores/moodboard_tiendas_b.json.
#   python3 tools/interiores/catalogo_tiendas_b.py && python3 tools/interiores/kits_tiendas_b.py [kit …]
# Frame of a room: the street door at z = 0, the back wall at z = D; x from -W/2 to W/2 (the faces of the walls).
import json, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
MOOD = json.load(open(os.path.join(ROOT, 'tools', 'interiores', 'moodboard_tiendas_b.json')))

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
KITS = {}
def kit(f): KITS[f.__name__] = f; return f

# ================================================================== THE HAIRDRESSER
@kit
def peluqueria():
    M = '-W/2+1.1'
    return {
        'tipologia': 'tienda_especializada', 'nombre': 'Peluquería', '_mood': 'peluqueria',
        'nota': 'La peluquería de un pueblo de las Vegas Altas: la sala de espera y la recepción junto a la puerta, los puestos de peinado con su espejo y su sillón a lo largo de las dos paredes, '
                'los lavacabezas y los secadores al fondo y la trastienda de las toallas y los tintes tras un tabique. La puerta en z = 0, el fondo en z = D; x de -W/2 a W/2.',
        'superficie': {'ancho': [5.7, 7.2], 'fondo': [9.0, 11.4], 'alto': 3.0},
        'variables': {'xc': 'W/2-1.5', 'z0': '1.7', 'z1': '3.0', 'zs': '3.9', 'zl': 'D-2.8', 'xt': 'W/2-2.1', 'zt': 'D-2.5'},
        'paso_libre': 0.9, 'pared': '#f1e9e4', 'suelo': 'herringbone_parquet', 'suelo_color': '#cdbfae',
        'puntos': {'dependiente': ['xc+0.6', '(z0+z1)/2'], 'mostrador': ['xc-0.85', '(z0+z1)/2']},
        'pedir': 'Pedir cita o pagar en el mostrador',
        'zonas': [
            Z('entrada', ['-W/2', '0', 'W/2', '1.5']),
            Z('espera', ['-W/2', '1.5', '-W/2+2.0', '3.7']),
            Z('caja', ['xc-0.3', 'z0', 'xc+0.3', 'z1'], False),
            Z('frente_caja', ['xc-1.3', 'z0', 'xc-0.33', 'z1']),
            Z('tras_caja', ['xc+0.33', 'z0', 'W/2', 'z1+0.2'], False),
            Z('est_w', ['-W/2', 'zs', '-W/2+1.7', 'zl']),
            Z('est_e', ['W/2-1.7', 'zs', 'W/2', 'zl']),
            Z('centro', ['-W/2+1.8', '3.7', 'W/2-1.8', 'zl']),
            Z('lavado', ['-W/2', 'zl', 'xt', 'D']),
            Z('pasillo_fondo', ['xt', 'zl', 'W/2', 'zt']),
            Z('trastienda', ['xt', 'zt', 'W/2', 'D'], False),
            Z('luces', ['-W/2', '0', 'W/2', 'D'], False),
        ],
        'tabiques': [{'de': ['xt', 'zt'], 'a': ['xt', 'D']}, {'de': ['xt', 'zt'], 'a': ['W/2', 'zt'], 'puerta': [0.5, 1.0]}],
        'libres': [{'rect': ['xc-1.3', 'z0', 'xc-0.3', 'z1'], 'nota': 'el sitio para pagar o pedir cita: sin muebles delante'}],
        'objetos': [
            # ---- the counter first: the kit's own design
            E('caja', 'modulos', 'pel_mostrador_caja', eje='z', linea=['xc', 'z0', 'z1'], mira='-x', obligatorio=True),
            sobre('caja', 'pel_perfumes_vitrina', ['pel_mostrador_caja'], cantidad=[1, 1], obligatorio=True, vende='perfume'),
            sobre('caja', 'pel_tpv', ['pel_mostrador_caja'], cantidad=[1, 1], obligatorio=True),
            sobre('caja', 'pel_agenda', ['pel_mostrador_caja'], cantidad=[1, 1], obligatorio=True),
            sobre('caja', 'datafono', ['pel_mostrador_caja'], cantidad=[1, 1], obligatorio=True),
            sobre('caja', ['bote_propinas', 'tarjetero', 'bote_caramelos'], ['pel_mostrador_caja'], cantidad=[0, 1]),
            E('tras_caja', 'contra_pared', 'pel_expositor_pared', pared='E', cantidad=[1, 1], obligatorio=True),
            sobre('tras_caja', ['pel_prod_champu_nutritivo', 'pel_prod_champu_rizos', 'pel_prod_champu_caspa', 'pel_prod_mascarilla_capilar', 'pel_prod_serum_puntas', 'pel_prod_laca_fijacion',
                                'pel_prod_espuma_volumen', 'pel_prod_gel_fijador', 'pel_prod_cera_modeladora', 'pel_prod_tinte_caja_castano', 'pel_prod_tinte_caja_rubio', 'pel_prod_tinte_caja_rojo'],
                  ['pel_expositor_pared'], relleno=[0.8, 0.95], todas=True, obligatorio=True),
            E('tras_caja', 'pared', 'pel_rotulo', pared='E', cantidad=[1, 1], obligatorio=True),
            E('tras_caja', 'pared', 'pel_cartel_precios', pared='E', cantidad=[0, 1]),
            E('tras_caja', 'pared', 'reloj_pared', pared='E', cantidad=[0, 1]),
            E('tras_caja', 'esquina', 'papelera', cantidad=[0, 1]),
            # ---- the waiting corner
            E('espera', 'contra_pared', 'pel_sofa_espera', pared='W', cantidad=[1, 1], obligatorio=True),
            E('espera', 'suelo_libre', 'pel_mesa_revistas', cantidad=[1, 1], obligatorio=True),
            sobre('espera', ['revista', 'periodico', 'pel_botes_pinzas'], ['pel_mesa_revistas'], por_soporte=[1, 3], obligatorio=True),
            E('espera', 'pared', 'pel_revistero_pared', pared='W', cantidad=[1, 1], obligatorio=True),
            E('espera', 'pared', variantes=['pel_cartel_peinados_a', 'pel_cartel_peinados_b'], pared='W', cantidad=[1, 2], todas=True, obligatorio=True),
            E('espera', 'esquina', 'planta_grande', cantidad=[0, 1]),
            E('entrada', 'esquina', 'perchero', cantidad=[0, 1]),
            E('entrada', 'esquina', 'papelera', cantidad=[1, 1], obligatorio=True),
            E('entrada', 'esquina', 'paraguas_cubo', cantidad=[0, 1]),
            # ---- the styling stations: a console and mirror on the wall, its chair in front (the chairs on the walls' beat)
            E('est_w', 'contra_pared', variantes=['pel_estacion_blanca', 'pel_estacion_madera', 'pel_estacion_negra'], pared='W', llenar=True, todas=True, obligatorio=True),
            E('est_w', 'fila', 'pel_sillon_corte_negro', eje='z', linea=['-W/2+1.15', 'zs+0.48', 'zs+1.5'], cada=0.93, mira='-x', obligatorio=True),
            E('est_w', 'fila', 'pel_sillon_corte_rosa', eje='z', linea=['-W/2+1.15', 'zs+2.34', 'zl-0.3'], cada=0.93, mira='-x'),
            E('est_e', 'contra_pared', variantes=['pel_estacion_negra', 'pel_estacion_blanca', 'pel_estacion_madera'], pared='E', llenar=True, todas=True, obligatorio=True),
            E('est_e', 'fila', 'pel_sillon_corte_blanco', eje='z', linea=['W/2-1.15', 'zs+0.48', 'zs+1.5'], cada=0.93, mira='+x', obligatorio=True),
            E('est_e', 'fila', 'pel_sillon_corte_negro', eje='z', linea=['W/2-1.15', 'zs+2.34', 'zl-0.3'], cada=0.93, mira='+x'),
            sobre('est_w', ['pel_secador_mano', 'pel_plancha_pelo', 'pel_cepillo_redondo', 'pel_peine_cola', 'pel_tijeras_estuche', 'pel_maquinilla', 'pel_champu_rosa', 'pel_laca', 'pel_pulverizador', 'pel_botes_pinzas', 'pel_rulos_bandeja'],
                  ['pel_estacion_blanca', 'pel_estacion_madera', 'pel_estacion_negra'], por_soporte=[2, 3], obligatorio=True),
            sobre('est_e', ['pel_secador_mano', 'pel_plancha_pelo', 'pel_cepillo_redondo', 'pel_peine_cola', 'pel_tijeras_estuche', 'pel_maquinilla', 'pel_acondicionador', 'pel_laca', 'pel_pulverizador', 'pel_botes_pinzas', 'pel_champu_verde'],
                  ['pel_estacion_blanca', 'pel_estacion_madera', 'pel_estacion_negra'], por_soporte=[2, 3], obligatorio=True),
            # ---- the middle: trolleys and hood dryers
            E('centro', 'suelo_libre', variantes=['pel_carrito_blanco', 'pel_carrito_rosa'], cantidad=[1, 2], todas=True, obligatorio=True),
            sobre('centro', ['pel_bol_tinte', 'pel_tubo_tinte', 'pel_capa_corte', 'pel_toallas_dobladas', 'pel_peine_cola', 'pel_tijeras_estuche', 'pel_pulverizador'], ['pel_carrito_blanco', 'pel_carrito_rosa'], por_soporte=[2, 3], obligatorio=True),
            E('centro', 'suelo_libre', variantes=['pel_secador_casco_crema', 'pel_secador_casco_rosa'], cantidad=[1, 2], todas=True, obligatorio=True),
            # ---- the washing corner
            E('lavado', 'contra_pared', variantes=['pel_lavacabezas_negro', 'pel_lavacabezas_rosa'], pared='N', cantidad=[2, 2], todas=True, obligatorio=True),
            E('lavado', 'contra_pared', 'estanteria_metalica', pared='W', cantidad=[1, 1], obligatorio=True),
            sobre('lavado', ['pel_toallas_dobladas', 'pel_capa_corte', 'pel_bol_tinte', 'pel_botes_pinzas', 'pel_rulos_bandeja', 'pel_acondicionador', 'pel_champu_verde', 'pel_champu_rosa'], ['estanteria_metalica'], relleno=[0.6, 0.85], todas=True, obligatorio=True),
            E('lavado', 'esquina', 'pel_cesto_ropa', cantidad=[1, 1], obligatorio=True),
            E('lavado', 'esquina', variantes=['fregona_cubo', 'escoba'], cantidad=[0, 1]),
            E('pasillo_fondo', 'pared', 'pel_calentador_toallas', pared='E', cantidad=[0, 1]),
            E('pasillo_fondo', 'esquina', 'papelera', cantidad=[0, 1]),
            # ---- the back room
            E('trastienda', 'contra_pared', 'estanteria_metalica', pared='E', cantidad=[1, 1], obligatorio=True),
            sobre('trastienda', ['pel_caja_tinte', 'pel_bidon_oxidante', 'caja_carton', 'pel_toallas_dobladas'], ['estanteria_metalica'], relleno=[0.6, 0.85], todas=True, obligatorio=True),
            E('trastienda', 'suelo_libre', variantes=['pel_esterilizador', 'pel_bidon_oxidante'], cantidad=[1, 2], todas=True),
            E('trastienda', 'esquina', 'pel_cesto_ropa', cantidad=[0, 1]),
            E('trastienda', 'pared', 'lavabo', pared='N', cantidad=[0, 1]),
            # ---- the light
            E('luces', 'techo', 'lampara_panel_led', por_m2=[0.12, 0.15], obligatorio=True),
        ],
        'iluminacion': {'fuentes': [4, 9], 'temperatura_k': [3500, 4200], 'dia': {'intensidad': 0.85}, 'noche': {'intensidad': 1.0}, 'minimo_lux_publico': 150},
        'ambiente': {'sonido': 'tienda', 'horario_defecto': 'Tu-Fr 09:30-13:30,16:30-20:00; Sa 09:00-14:00',
                     'vida': ['pelo recién cortado en el suelo', 'una señora bajo el secador', 'las revistas de la sala de espera', 'toallas calientes'],
                     'cerrado': 'persiana bajada, los espejos apagados',
                     'clientela': {'maximo': 4, 'horas': [[9, 13, 0.5], [16, 20, 0.55]], 'frases': [
                         'Solo las puntas, que me las dejo largas.', 'A ver si me arreglas esto antes de la boda del sábado.', 'Qué calor hace hoy, ¿verdad?',
                         'Mi hija me tiene dicho que me tiña de caoba.', 'No me lo cortes mucho, que luego tarda en crecer.', '¿Has visto lo que ha subido la luz?']}},
        'minimo_objetos_distintos': 40,
    }

# ================================================================== THE PERFUMERY
PERFUMES = ['per_perfume_' + k for k in ('azahar', 'jazmin', 'rosa_mayo', 'lavanda', 'sandalo', 'ambar', 'citrus', 'brisa_marina', 'vainilla', 'noche_verano', 'madera_noble', 'almendro', 'higuera',
                                         'romero', 'pino', 'caramelo', 'violeta', 'cuero', 'ninos', 'oud')]
COSMETICOS = ['per_cosm_' + k for k in ('pintalabios_rojos', 'pintalabios_nude', 'esmaltes_rojos', 'esmaltes_pastel', 'mascara_pestanas', 'base_maquillaje', 'polvos_compactos', 'paleta_sombras', 'brochas',
                                         'crema_facial', 'serum', 'crema_manos', 'leche_corporal', 'gel_ducha', 'jabones', 'sales_bano', 'protector_solar', 'desmaquillante', 'agua_perfumada')]
@kit
def perfumeria():
    return {
        'tipologia': 'tienda_especializada', 'nombre': 'Perfumería y centro de belleza', '_mood': 'perfumeria',
        'nota': 'La perfumería de un pueblo de las Vegas Altas: el mostrador de vitrina con la caja a la derecha y, a su espalda, la pared de perfumes con luz cálida; a la izquierda, estantes de cosmética; en medio, mesas con probadores; '
                'al fondo, el tocador de maquillaje y la cabina de estética tras un tabique. Marcas inventadas. La puerta en z = 0, el fondo en z = D; x de -W/2 a W/2.',
        'superficie': {'ancho': [5.4, 6.9], 'fondo': [8.7, 10.5], 'alto': 3.0},
        'variables': {'xb': 'W/2-1.6', 'zb0': '1.8', 'zb1': '5.4', 'zc': 'D-3.3', 'xk': 'W/2-2.6'},
        'paso_libre': 0.9, 'pared': '#f3eee6', 'suelo': 'floor_tiles_06', 'suelo_color': '#d8d0c4',
        'puntos': {'dependiente': ['xb+0.8', '(zb0+zb1)/2'], 'mostrador': ['xb-0.9', '(zb0+zb1)/2']},
        'pedir': 'Pedir en el mostrador',
        'zonas': [
            Z('entrada', ['-W/2', '0', 'W/2', '1.5']),
            Z('pared_w', ['-W/2', '1.5', '-W/2+0.5', 'zc'], False),
            Z('sala', ['-W/2+0.5', '1.5', 'xb-1.3', 'zc']),
            Z('barra', ['xb-0.3', 'zb0', 'xb+0.3', 'zb1'], False),
            Z('frente_barra', ['xb-1.3', 'zb0', 'xb-0.33', 'zb1']),
            Z('trasbarra', ['xb+0.33', 'zb0', 'W/2', 'zb1'], False),
            Z('maquillaje', ['-W/2', 'zc', '-W/2+2.4', 'D']),
            Z('fondo', ['-W/2+2.4', 'zc', 'xk', 'D']),
            Z('cabina', ['xk', 'zc', 'W/2', 'D'], False),
            Z('luces', ['-W/2', '0', 'W/2', 'D'], False),
        ],
        'tabiques': [{'de': ['xk', 'zc'], 'a': ['xk', 'D'], 'puerta': [0.6, 1.0]}, {'de': ['xk', 'zc'], 'a': ['W/2', 'zc']}],
        'libres': [{'rect': ['xb-1.3', 'zb0', 'xb-0.3', 'zb1'], 'nota': 'el sitio para pedir en el mostrador: sin muebles delante'}],
        'objetos': [
            # ---- the counter first: the kit's own design
            E('barra', 'modulos', 'per_mostrador_vitrina_negro', eje='z', linea=['xb', 'zb0', 'zb1'], mira='-x', obligatorio=True),
            sobre('barra', 'per_perfumes_escaparate', ['per_mostrador_vitrina_negro'], cantidad=[1, 1], obligatorio=True, vende='perfume'),
            sobre('barra', 'pel_tpv', ['per_mostrador_vitrina_negro'], cantidad=[1, 1], obligatorio=True),
            sobre('barra', 'datafono', ['per_mostrador_vitrina_negro'], cantidad=[1, 1], obligatorio=True),
            sobre('barra', ['per_cesto_regalo', 'per_bolsas_regalo', 'per_tarjetero_fidelidad', 'per_probador_papel'], ['per_mostrador_vitrina_negro'], cantidad=[2, 3], obligatorio=True),
            sobre('barra', ['per_perfume_azahar', 'per_perfume_oud', 'per_perfume_rosa_mayo', 'per_perfume_vainilla'], ['per_mostrador_vitrina_negro'], cantidad=[1, 2], vende='perfume'),
            E('trasbarra', 'esquina', 'papelera', cantidad=[1, 1], obligatorio=True),
            E('trasbarra', 'contra_pared', 'per_estanteria_luz', pared='E', llenar=True, obligatorio=True),
            sobre('trasbarra', PERFUMES, ['per_estanteria_luz'], relleno=[0.8, 0.95], todas=True, obligatorio=True, vende='perfume'),
            E('trasbarra', 'suelo_libre', 'silla_cajera', cantidad=[0, 1]),
            E('trasbarra', 'techo', 'carril_focos', cantidad=[0, 1]),
            # ---- the west wall: lit shelving with the cosmetics (what does not fit on the counter's wall)
            E('pared_w', 'contra_pared', 'per_estanteria_luz', pared='W', llenar=True, obligatorio=True),
            sobre('pared_w', COSMETICOS + PERFUMES[8:], ['per_estanteria_luz'], relleno=[0.8, 0.95], todas=True, obligatorio=True),
            E('pared_w', 'pared', 'per_cartel_belleza', pared='W', cantidad=[0, 1]),
            # ---- the middle: tables with testers, a stepped tower
            E('sala', 'suelo_libre', variantes=['per_mesa_expositora_negra', 'per_mesa_expositora_crema'], cantidad=[1, 2], todas=True, obligatorio=True),
            sobre('sala', PERFUMES[:10] + ['per_probador_papel'], ['per_mesa_expositora_negra', 'per_mesa_expositora_crema'], por_soporte=[2, 4], obligatorio=True, vende='perfume'),
            E('sala', 'suelo_libre', 'per_torre_tester', cantidad=[1, 1], obligatorio=True),
            sobre('sala', COSMETICOS[:12], ['per_torre_tester'], relleno=[0.7, 0.95], todas=True),
            E('sala', 'esquina', 'planta_grande', cantidad=[0, 1]),
            E('entrada', 'esquina', 'papelera', cantidad=[1, 1], obligatorio=True),
            E('entrada', 'esquina', 'paraguas_cubo', cantidad=[0, 1]),
            E('entrada', 'esquina', 'planta_grande', cantidad=[0, 1]),
            # ---- the make-up table and the back
            E('maquillaje', 'contra_pared', 'per_tocador_maquillaje', pared='W', cantidad=[1, 1], obligatorio=True),
            sobre('maquillaje', COSMETICOS[:9] + ['per_probador_papel'], ['per_tocador_maquillaje'], por_soporte=[3, 5], obligatorio=True),
            E('maquillaje', 'pared', 'per_rotulo', pared='N', cantidad=[1, 1], obligatorio=True),
            E('maquillaje', 'pared', 'per_pizarra_tratamientos', pared='N', cantidad=[1, 1], obligatorio=True),
            E('fondo', 'pared', 'per_cartel_perfume', pared='N', cantidad=[0, 1]),
            E('fondo', 'esquina', 'planta_grande', cantidad=[0, 1]),
            E('fondo', 'esquina', 'per_taburete_maquillaje', cantidad=[0, 1]),
            # ---- the treatment cabin
            E('cabina', 'contra_pared', 'per_camilla_estetica', pared='E', cantidad=[1, 1], obligatorio=True),
            sobre('cabina', ['pel_toallas_dobladas', 'per_bolsas_regalo'], ['per_camilla_estetica'], cantidad=[0, 1]),
            E('cabina', 'suelo_libre', variantes=['per_carrito_estetica', 'per_lampara_lupa', 'per_vaporizador_facial'], cantidad=[3, 3], todas=True, obligatorio=True),
            sobre('cabina', ['per_cosm_crema_facial', 'per_cosm_serum', 'per_cosm_desmaquillante', 'per_cosm_crema_manos'], ['per_carrito_estetica'], por_soporte=[2, 3]),
            E('cabina', 'esquina', 'per_taburete_estetica', cantidad=[1, 1], obligatorio=True),
            E('cabina', 'pared', 'per_estante_cabina', pared='N', cantidad=[0, 1]),
            E('cabina', 'pared', 'pel_calentador_toallas', pared='N', cantidad=[0, 1]),
            E('cabina', 'esquina', 'planta_pequena', cantidad=[0, 1]),
            # ---- the light
            E('luces', 'techo', 'lampara_panel_led', por_m2=[0.12, 0.15], obligatorio=True),
        ],
        'iluminacion': {'fuentes': [4, 9], 'temperatura_k': [3500, 3900], 'dia': {'intensidad': 0.85}, 'noche': {'intensidad': 1.0}, 'minimo_lux_publico': 150},
        'ambiente': {'sonido': 'tienda', 'horario_defecto': 'Mo-Fr 10:00-13:45,17:00-20:30; Sa 10:00-14:00',
                     'vida': ['un probador con la tira de papel', 'bolsas de regalo junto a la caja', 'una clienta en el tocador', 'olor a jazmín'],
                     'cerrado': 'reja bajada, las vitrinas encendidas'},
        'minimo_objetos_distintos': 40,
    }

# ================================================================== THE CAR WORKSHOP
RECAMBIOS = ['tal_prod_' + k for k in ('filtro_aceite', 'filtro_aire', 'pastillas_freno', 'discos_freno', 'bujias', 'baterias', 'escobillas', 'aceite_5l', 'aceite_1l', 'anticongelante', 'bombillas',
                                        'correas', 'amortiguadores', 'limpiaparabrisas', 'ambientadores', 'cadenas_nieve', 'cables_arranque')]
UTILES = ['tal_llaves_juego', 'tal_martillo', 'tal_caja_herramientas', 'tal_lampara_inspeccion', 'tal_motor_arranque', 'tal_pistones', 'tal_trapos', 'tal_rollo_papel_taller']
@kit
def taller():
    return {
        'tipologia': 'tienda_especializada', 'nombre': 'Taller mecánico y recambios', '_mood': 'taller',
        'nota': 'El taller de coches de un pueblo de las Vegas Altas: el mostrador de recambios con sus estanterías de cajas junto a la puerta, el despacho y una salita con neumáticos de muestra, y al fondo la nave: un elevador de dos columnas con un coche, '
                'los bancos y las cajoneras de herramientas contra la pared, las estanterías de neumáticos, los bidones de aceite y, tras un tabique, el almacén. Luz fría, de nave. Sin marcas. La puerta en z = 0, el fondo en z = D; x de -W/2 a W/2.',
        'superficie': {'ancho': [8.1, 9.6], 'fondo': [12.0, 14.4], 'alto': 3.6},
        'variables': {'xm': 'W/2-1.5', 'z0': '1.8', 'z1': '4.3', 'zt': '4.8', 'zf': 'D-2.4', 'xo': '-W/2+3.0', 'xa': 'W/2-3.2'},
        'paso_libre': 0.9, 'pared': '#dcdedf', 'suelo': 'concrete_floor_damaged_01', 'suelo_color': '#8e9296',
        'puntos': {'dependiente': ['xm+0.8', '(z0+z1)/2'], 'mostrador': ['xm-0.9', '(z0+z1)/2']},
        'pedir': 'Pedir recambios o presupuesto en el mostrador',
        'zonas': [
            Z('entrada', ['-W/2', '0', 'W/2', '1.5']),
            Z('sala_cliente', ['-W/2', '1.5', 'xm-1.4', '4.6']),
            Z('barra', ['xm-0.3', 'z0', 'xm+0.3', 'z1'], False),
            Z('frente_barra', ['xm-1.4', 'z0', 'xm-0.33', 'z1']),
            Z('trasbarra', ['xm+0.33', '1.5', 'W/2', '6.0'], False),
            Z('taller', ['-W/2+0.8', 'zt', 'W/2-1.5', 'zf']),
            Z('pared_oeste', ['-W/2', 'zt', '-W/2+0.8', 'zf'], False),
            Z('pared_este', ['W/2-1.5', '6.2', 'W/2', 'zf'], False),
            Z('oficina', ['-W/2', 'zf', 'xo', 'D'], False),
            Z('fondo', ['xo', 'zf', 'xa', 'D']),
            Z('almacen', ['xa', 'zf', 'W/2', 'D'], False),
            Z('luces_frente', ['-W/2', '0', 'W/2', 'zt'], False),
            Z('luces_taller', ['-W/2', 'zt', 'W/2', 'D'], False),
        ],
        'tabiques': [
            {'de': ['-W/2', 'zf'], 'a': ['xo', 'zf'], 'puerta': [1.9, 1.0]}, {'de': ['xo', 'zf'], 'a': ['xo', 'D']},
            {'de': ['xa', 'zf'], 'a': ['xa', 'D']}, {'de': ['xa', 'zf'], 'a': ['W/2', 'zf'], 'puerta': [0.5, 1.0]},
        ],
        'libres': [{'rect': ['xm-1.4', 'z0', 'xm-0.3', 'z1'], 'nota': 'el sitio para pedir en el mostrador: sin muebles delante'}],
        'objetos': [
            # ---- the parts counter and its shelves
            E('barra', 'modulos', 'tal_mostrador_recambios', eje='z', linea=['xm', 'z0', 'z1'], mira='-x', obligatorio=True),
            sobre('barra', 'tal_exp_linternas', ['tal_mostrador_recambios'], cantidad=[1, 1], obligatorio=True, vende='linterna'),
            sobre('barra', 'tal_catalogo_recambios', ['tal_mostrador_recambios'], cantidad=[1, 1], obligatorio=True),
            sobre('barra', 'pel_tpv', ['tal_mostrador_recambios'], cantidad=[1, 1], obligatorio=True),
            sobre('barra', 'datafono', ['tal_mostrador_recambios'], cantidad=[1, 1], obligatorio=True),
            sobre('barra', ['bote_propinas', 'tarjetero', 'tal_prod_ambientadores', 'tal_prod_bombillas'], ['tal_mostrador_recambios'], cantidad=[1, 2]),
            E('trasbarra', 'contra_pared', 'tal_estanteria_recambios', pared='E', llenar=True, obligatorio=True),
            sobre('trasbarra', RECAMBIOS, ['tal_estanteria_recambios'], relleno=[0.8, 0.95], todas=True, obligatorio=True),
            E('trasbarra', 'pared', 'tal_rotulo', pared='E', cantidad=[1, 1], obligatorio=True),
            E('trasbarra', 'suelo_libre', 'taburete_alto', cantidad=[0, 1]),
            # ---- the west wall: benches and chests of tools
            E('pared_oeste', 'contra_pared', 'tal_banco_trabajo', pared='W', cantidad=[1, 1], obligatorio=True),
            E('pared_oeste', 'contra_pared', variantes=['tal_cajonera_roja', 'tal_cajonera_azul', 'tal_cajonera_gris'], pared='W', cantidad=[2, 3], todas=True, obligatorio=True),
            E('pared_oeste', 'contra_pared', 'tal_banco_trabajo_madera', pared='W', cantidad=[0, 1]),
            sobre('pared_oeste', UTILES, ['tal_banco_trabajo', 'tal_banco_trabajo_madera', 'tal_cajonera_roja', 'tal_cajonera_azul', 'tal_cajonera_gris'], por_soporte=[1, 3], obligatorio=True, vende='herramientas'),
            E('pared_oeste', 'pared', 'tal_panel_herramientas', pared='W', cantidad=[0, 2]),
            E('pared_oeste', 'pared', 'tal_senal_epi', pared='W', cantidad=[0, 1]),
            E('pared_oeste', 'pared', 'extintor_super', pared='W', cantidad=[0, 1]),
            # ---- the east wall: tyre racks, oil drums, compressor
            E('pared_este', 'contra_pared', 'tal_compresor', pared='E', cantidad=[1, 1], obligatorio=True),
            E('pared_este', 'contra_pared', 'tal_estanteria_neumaticos', pared='E', cantidad=[1, 2], obligatorio=True),
            E('pared_este', 'suelo_libre', variantes=['tal_bidon_aceite_azul', 'tal_bidon_aceite_negro', 'tal_bidon_aceite_usado'], cantidad=[2, 3], todas=True, obligatorio=True),
            E('pared_este', 'suelo_libre', variantes=['tal_garrafas_aceite_palet', 'tal_contenedor_residuos'], cantidad=[0, 2], todas=True),
            E('pared_este', 'pared', 'tal_senal_epi', pared='E', cantidad=[0, 1]),
            # ---- the waiting corner, with a few tyres to look at
            E('sala_cliente', 'contra_pared', 'banco_espera', pared='W', cantidad=[1, 1], obligatorio=True),
            E('sala_cliente', 'pared', variantes=['tal_cartel_tarifas', 'tal_cartel_neumaticos', 'tal_cartel_revision'], pared='W', cantidad=[1, 3], todas=True, obligatorio=True),
            E('sala_cliente', 'contra_pared', 'tal_estanteria_baja', pared='W', cantidad=[0, 1]),
            sobre('sala_cliente', ['tal_prod_neumatico_expuesto', 'tal_prod_filtro_aceite', 'tal_prod_aceite_1l', 'tal_prod_limpiaparabrisas'], ['tal_estanteria_baja'], relleno=[0.5, 0.8], todas=True),
            E('sala_cliente', 'suelo_libre', variantes=['tal_pila_neumaticos_a', 'tal_pila_neumaticos_b', 'tal_pila_neumaticos_c'], cantidad=[1, 2], todas=True, obligatorio=True),
            E('sala_cliente', 'suelo_libre', 'revistero', cantidad=[0, 1]),
            E('sala_cliente', 'esquina', 'planta_grande', cantidad=[0, 1]),
            E('entrada', 'esquina', 'papelera', cantidad=[1, 1], obligatorio=True),
            E('entrada', 'esquina', 'paraguas_cubo', cantidad=[0, 1]),
            # ---- the office
            E('oficina', 'contra_pared', 'puesto_oficina', pared='W', cantidad=[1, 1], obligatorio=True),
            E('oficina', 'contra_pared', 'archivador_metalico', pared='N', cantidad=[1, 2], obligatorio=True),
            E('oficina', 'contra_pared', 'estanteria_archivadores', pared='N', cantidad=[0, 1]),
            sobre('oficina', ['archivador_azul', 'archivador_rojo', 'archivador_verde', 'archivador_negro', 'archivador_amarillo', 'pila_carpetas'], ['estanteria_archivadores'], relleno=[0.5, 0.85], todas=True),
            sobre('oficina', ['monitor_pc_encendido', 'telefono_fijo', 'teclado', 'bloc_notas', 'calculadora'], ['puesto_oficina'], por_soporte=[2, 3]),
            E('oficina', 'pared', 'tablon_corcho', pared='E', cantidad=[1, 1], obligatorio=True),
            E('oficina', 'pared', 'calendario_pared', pared='E', cantidad=[0, 1]),
            E('oficina', 'suelo_libre', 'silla_visita', cantidad=[1, 1], obligatorio=True),
            E('oficina', 'esquina', 'planta_alta', cantidad=[0, 1]),
            # ---- the back of the bay
            E('fondo', 'pared', 'tal_lavabo_industrial', pared='N', cantidad=[1, 1], obligatorio=True),
            E('fondo', 'pared', variantes=['tal_cartel_revision', 'tal_cartel_neumaticos'], pared='N', cantidad=[0, 1]),
            E('fondo', 'esquina', 'tal_dispensador_papel', cantidad=[1, 1], obligatorio=True),
            E('fondo', 'contra_pared', 'tal_banco_trabajo_madera', pared='N', cantidad=[0, 1]),
            E('fondo', 'esquina', 'tal_contenedor_residuos', cantidad=[0, 1]),
            E('fondo', 'suelo_libre', variantes=['tal_bateria_cargador', 'tal_taburete_taller'], cantidad=[0, 2]),
            sobre('fondo', ['tal_trapos', 'tal_rollo_papel_taller', 'tal_llaves_juego'], ['tal_banco_trabajo_madera'], por_soporte=[1, 2]),
            # ---- the storeroom
            E('almacen', 'contra_pared', 'tal_estanteria_recambios', pared='N', cantidad=[1, 2], obligatorio=True),
            sobre('almacen', RECAMBIOS[5:] + ['caja_carton'], ['tal_estanteria_recambios'], relleno=[0.6, 0.9], todas=True, obligatorio=True),
            E('almacen', 'contra_pared', 'tal_estanteria_baja', pared='E', cantidad=[1, 1], obligatorio=True),
            sobre('almacen', ['caja_carton', 'tal_prod_neumatico_expuesto', 'tal_prod_filtro_aire', 'tal_prod_pastillas_freno'], ['tal_estanteria_baja'], relleno=[0.6, 0.9], todas=True),
            E('almacen', 'suelo_libre', variantes=['palet_madera', 'tal_garrafas_aceite_palet', 'pila_cajones_vacios'], cantidad=[1, 2], todas=True),
            E('almacen', 'esquina', 'fregona_cubo', cantidad=[0, 1]),
            E('almacen', 'esquina', 'escoba', cantidad=[0, 1]),
            # ---- the bay: a lift with a car, the machines
            E('taller', 'modulos', 'tal_elevador_azul', eje='x', linea=['zt+2.0', '-W/2+0.9', 'W/2-0.9'], mira='+z', obligatorio=True),
            E('taller', 'suelo_libre', variantes=['tal_desmontadora_neumaticos', 'tal_equilibradora'], cantidad=[1, 2], todas=True, obligatorio=True),
            E('taller', 'suelo_libre', variantes=['tal_gato_hidraulico', 'tal_caballetes', 'tal_carro_aceite', 'tal_carro_mecanico', 'tal_taburete_taller'], cantidad=[0, 4], todas=True),
            E('taller', 'suelo_libre', variantes=['tal_bidon_aceite_usado', 'tal_pila_neumaticos_a', 'tal_bateria_cargador'], cantidad=[0, 2]),
            E('taller', 'suelo_libre', 'tal_coche_capo_abierto', cantidad=[0, 1]),
            # ---- the light: LED high bays over the bay, panels over the front
            E('luces_frente', 'techo', 'regleta_led_techo', por_m2=[0.06, 0.08], obligatorio=True),
            E('luces_taller', 'techo', 'luminaria_campana', por_m2=[0.045, 0.06], obligatorio=True),
        ],
        'iluminacion': {'fuentes': [5, 9], 'temperatura_k': [4200, 4500], 'dia': {'intensidad': 0.9}, 'noche': {'intensidad': 1.0}, 'minimo_lux_publico': 200},
        'ambiente': {'sonido': 'taller', 'horario_defecto': 'Mo-Fr 08:30-13:30,15:30-19:30; Sa 09:00-13:00',
                     'vida': ['el coche elevado', 'una mancha de aceite en el suelo', 'la radio del taller', 'un neumático apoyado en la pared'],
                     'cerrado': 'persiana bajada, el elevador abajo'},
        'minimo_objetos_distintos': 40,
    }

# ================================================================== THE GREENGROCER
_FR = ['pera_conferencia', 'pera_limonera', 'ciruela_roja', 'ciruela_amarilla', 'cerezas', 'fresas', 'kiwi', 'pina', 'aguacate', 'higos', 'granadas', 'mandarinas', 'pomelos', 'uva_verde', 'uva_negra', 'nectarinas',
       'albaricoques', 'caquis', 'manzana_golden', 'manzana_fuji', 'platano_canario', 'mango', 'coco', 'membrillo', 'naranja_zumo', 'limon_verna']
_VE = ['calabacin', 'berenjena', 'pepino', 'judias_verdes', 'coliflor', 'brocoli', 'repollo', 'lombarda', 'esparragos', 'champinones', 'setas', 'remolacha', 'puerros', 'calabaza', 'boniato', 'espinacas', 'acelgas',
       'rabanitos', 'apio', 'alcachofas', 'mazorcas', 'guisantes', 'pimiento_verde', 'pimiento_amarillo', 'guindillas', 'perejil', 'ajos', 'cebolla_roja', 'cebolleta', 'patata_roja', 'patata_nueva', 'tomate_pera',
       'tomate_cherry', 'tomate_raf', 'lechuga_romana', 'lechuga_iceberg', 'endivias', 'canonigos', 'rucula', 'jengibre']
FRUTAS_F = ['fru_caja_' + k for k in _FR]
VERDURAS_F = ['fru_caja_' + k for k in _VE]
MELONES = ['prod_fruta_melones', 'fru_caja_melon_piel_sapo', 'fru_caja_melon_amarillo', 'fru_caja_sandia_mini']
COMERCIO_FRUTA = ['prod_fruta_melocotones', 'prod_fruta_naranjas', 'prod_fruta_manzanas_rojas', 'prod_fruta_manzanas_verdes', 'prod_fruta_limones', 'prod_fruta_tomates', 'prod_fruta_cebollas', 'prod_fruta_patatas',
                  'prod_fruta_lechugas', 'prod_fruta_pimientos', 'prod_fruta_zanahorias', 'prod_fruta_platanos', 'prod_fruta_uvas']
@kit
def fruteria():
    return {
        'tipologia': 'alimentacion', 'nombre': 'Frutería', '_mood': 'fruteria',
        'nota': 'La frutería de un pueblo de las Vegas Altas: cajones de fruta y verdura en escalones de madera a lo largo de las dos paredes, con toldillos y ristras de ajos y pimientos; en el centro, mesas con melones y cestas; '
                'el mostrador con la balanza y la caja a la derecha; sacos de patatas y cebollas junto a la puerta; al fondo las neveras de zumos y agua, y el almacén tras un tabique. La puerta en z = 0, el fondo en z = D; x de -W/2 a W/2.',
        'superficie': {'ancho': [6.9, 8.1], 'fondo': [9.3, 11.4], 'alto': 3.0},
        'variables': {'xc': 'W/2-2.0', 'z0': '1.5', 'z1': '3.9', 'zr': 'D-2.6', 'xs': '-W/2+3.4'},
        'paso_libre': 0.9, 'pared': '#f2eee0', 'suelo': 'floor_tiles_06', 'suelo_color': '#cfc6b4',
        'puntos': {'dependiente': ['xc+0.8', '(z0+z1)/2'], 'mostrador': ['xc-0.9', '(z0+z1)/2']},
        'pedir': 'Pesar y cobrar en el mostrador',
        'zonas': [
            Z('entrada', ['-W/2', '0', 'W/2', '1.3']),
            Z('barra', ['xc-0.3', 'z0', 'xc+0.3', 'z1'], False),
            Z('frente_barra', ['xc-1.3', 'z0', 'xc-0.33', 'z1']),
            Z('tras', ['xc+0.33', '1.3', 'W/2', '5.1'], False),
            Z('pared_w', ['-W/2', '1.3', '-W/2+1.0', 'zr'], False),
            Z('pared_e', ['W/2-1.0', '5.2', 'W/2', 'zr+0.8'], False),
            Z('centro', ['-W/2+1.0', '1.3', 'W/2-1.0', 'zr']),
            Z('fondo', ['xs', 'zr', 'W/2', 'D']),
            Z('almacen', ['-W/2', 'zr', 'xs', 'D'], False),
            Z('luces', ['-W/2', '0', 'W/2', 'D'], False),
        ],
        'tabiques': [{'de': ['xs', 'zr'], 'a': ['xs', 'D']}, {'de': ['-W/2', 'zr'], 'a': ['xs', 'zr'], 'puerta': [1.3, 1.0]}],
        'libres': [{'rect': ['xc-1.3', 'z0', 'xc-0.3', 'z1'], 'nota': 'el sitio para pesar y pagar en el mostrador: sin muebles delante'}],
        'objetos': [
            # ---- the counter first: the scale, the till, the bags
            E('barra', 'modulos', 'fru_mostrador', eje='z', linea=['xc', 'z0', 'z1'], mira='-x', obligatorio=True),
            sobre('barra', 'balanza_comercial', ['fru_mostrador'], cantidad=[1, 1], obligatorio=True),
            sobre('barra', 'pel_tpv', ['fru_mostrador'], cantidad=[1, 1], obligatorio=True),
            sobre('barra', 'fru_rollo_bolsas', ['fru_mostrador'], cantidad=[1, 1], obligatorio=True),
            sobre('barra', ['fru_cuenco_muestra', 'fru_cestillo_cambio', 'bote_propinas', 'datafono'], ['fru_mostrador'], cantidad=[2, 3], obligatorio=True),
            E('tras', 'esquina', 'papelera', cantidad=[1, 1], obligatorio=True),
            E('tras', 'contra_pared', 'estanteria_metalica', pared='E', cantidad=[1, 2], obligatorio=True),
            sobre('tras', ['caja_carton', 'fru_rollo_bolsas', 'fru_cestillo_cambio', 'fru_cuenco_muestra'], ['estanteria_metalica'], relleno=[0.5, 0.8], todas=True),
            E('tras', 'pared', 'fru_rotulo', pared='E', cantidad=[1, 1], obligatorio=True),
            E('entrada', 'pared', 'fru_pizarra_a', pared='W', cantidad=[1, 1], obligatorio=True),
            E('tras', 'suelo_libre', variantes=['taburete_alto', 'silla_cajera'], cantidad=[0, 1]),
            # ---- the stepped stands along both walls, with their crates
            E('pared_w', 'contra_pared', variantes=['fru_expositor_escalonado', 'fru_expositor_escalonado_verde'], pared='W', llenar=True, obligatorio=True),
            sobre('pared_w', FRUTAS_F + VERDURAS_F[:18], ['fru_expositor_escalonado', 'fru_expositor_escalonado_verde'], relleno=[1.0, 1.0], todas=True, obligatorio=True, vende='fruta'),
            E('pared_w', 'pared', variantes=['fru_toldo_verde', 'fru_toldo_rojo'], pared='W', cada=1.35, maximo=4),
            E('pared_w', 'pared', variantes=['fru_ristra_ajos', 'fru_ristra_pimientos', 'fru_estante_cestas'], pared='W', cantidad=[1, 2], todas=True, obligatorio=True),
            E('pared_e', 'contra_pared', variantes=['fru_expositor_escalonado_verde', 'fru_expositor_escalonado'], pared='E', llenar=True, obligatorio=True),
            sobre('pared_e', VERDURAS_F[18:] + FRUTAS_F[:10], ['fru_expositor_escalonado', 'fru_expositor_escalonado_verde'], relleno=[1.0, 1.0], todas=True, obligatorio=True),
            E('pared_e', 'pared', variantes=['fru_toldo_rojo', 'fru_toldo_verde'], pared='E', cada=1.35, maximo=3),
            E('pared_e', 'pared', variantes=['fru_ristra_pimientos', 'fru_ristra_ajos'], pared='E', cantidad=[0, 2], todas=True),
            # ---- the middle: tables with melons, fruit and baskets
            E('centro', 'suelo_libre', variantes=['fru_isla_central', 'mesa_fruteria'], cantidad=[2, 3], todas=True, obligatorio=True),
            sobre('centro', MELONES, ['fru_isla_central', 'mesa_fruteria'], por_soporte=[1, 2], obligatorio=True, vende='melon'),
            sobre('centro', COMERCIO_FRUTA, ['fru_isla_central', 'mesa_fruteria'], por_soporte=[1, 2], vende='fruta'),
            sobre('centro', FRUTAS_F[10:] + VERDURAS_F[:12], ['fru_isla_central', 'mesa_fruteria'], por_soporte=[1, 3]),
            E('centro', 'suelo_libre', variantes=['fru_cesta_naranjas', 'fru_cesta_manzanas', 'fru_cesta_limones', 'fru_sandias_pila'], cantidad=[2, 3], todas=True),
            # ---- the door: sacks, baskets, bananas
            E('entrada', 'suelo_libre', variantes=['fru_saco_patatas', 'fru_saco_cebollas', 'fru_saco_naranjas', 'fru_saco_zanahorias'], cantidad=[2, 3], todas=True, obligatorio=True),
            E('entrada', 'esquina', 'fru_colgador_platanos', cantidad=[1, 1], obligatorio=True),
            E('entrada', 'esquina', 'papelera', cantidad=[1, 1], obligatorio=True),
            E('entrada', 'contra_pared', 'pila_cestas', pared='S', cantidad=[1, 1], obligatorio=True),
            E('entrada', 'esquina', 'fru_pila_sacos', cantidad=[0, 1]),
            E('entrada', 'esquina', 'planta_grande', cantidad=[0, 1]),
            # ---- the back: fridges of juice and water, pallets
            E('fondo', 'contra_pared', 'nevera_bebidas_super', pared='N', cantidad=[1, 1], obligatorio=True),
            E('fondo', 'contra_pared', 'nevera_lacteos', pared='N', cantidad=[1, 1], obligatorio=True),
            sobre('fondo', ['prod_agua_fria', 'prod_naranja_fria', 'prod_zumo_frio', 'prod_cola_fria', 'prod_isotonica_fria', 'prod_cerveza_fria'], ['nevera_bebidas_super'], relleno=[0.8, 0.95], todas=True, obligatorio=True, vende=['zumo', 'agua']),
            sobre('fondo', ['prod_zumo_fresco', 'prod_yogur_natural', 'prod_yogur_fresa'], ['nevera_lacteos'], relleno=[0.8, 0.95], todas=True, obligatorio=True, vende='zumo'),
            E('fondo', 'pared', 'fru_pizarra_b', pared='E', cantidad=[1, 1], obligatorio=True),
            E('fondo', 'pared', 'fru_cartel_fruta', pared='E', cantidad=[0, 1]),
            E('fondo', 'suelo_libre', variantes=['fru_carro_cajas', 'palet_madera', 'pila_cajones_vacios'], cantidad=[1, 2], todas=True),
            E('fondo', 'pared', 'extintor_super', pared='E', cantidad=[0, 1]),
            # ---- the storeroom
            E('almacen', 'contra_pared', 'estanteria_metalica', pared='N', cantidad=[1, 2], obligatorio=True),
            sobre('almacen', ['caja_carton', 'fru_rollo_bolsas', 'prod_fruta_naranjas', 'prod_fruta_patatas'], ['estanteria_metalica'], relleno=[0.6, 0.85], todas=True, obligatorio=True),
            E('almacen', 'suelo_libre', variantes=['pila_cajones_vacios', 'fru_saco_patatas', 'fru_saco_cebollas', 'fru_carro_cajas'], cantidad=[2, 3], todas=True, obligatorio=True),
            E('almacen', 'esquina', 'fregona_cubo', cantidad=[0, 1]),
            E('almacen', 'esquina', 'escoba', cantidad=[0, 1]),
            # ---- the light
            E('luces', 'techo', 'lampara_panel_led', por_m2=[0.12, 0.15], obligatorio=True),
        ],
        'iluminacion': {'fuentes': [5, 9], 'temperatura_k': [3800, 4300], 'dia': {'intensidad': 0.9}, 'noche': {'intensidad': 1.0}, 'minimo_lux_publico': 200},
        'ambiente': {'sonido': 'tienda', 'horario_defecto': 'Mo-Sa 09:00-14:00,17:00-20:30',
                     'vida': ['cajones recién puestos', 'una clienta eligiendo melones', 'sacos junto a la puerta', 'el racimo de plátanos'],
                     'cerrado': 'persiana bajada, los cajones dentro'},
        'minimo_objetos_distintos': 80,
    }

# ================================================================== THE BAKERY
PANES_F = ['pan_pan_' + k for k in ('barra_pueblo', 'barra_integral', 'barra_candeal', 'barra_centeno', 'barra_semillas', 'baguette', 'hogaza_lena', 'hogaza_centeno', 'hogaza_integral', 'hogaza_pasas', 'rosca', 'mollete',
                                    'pistolas', 'chapata', 'pan_molde', 'pan_leche', 'picos', 'colines', 'reganas', 'pan_rallado', 'tortas_aceite')]
BOLLERIA_F = ['pan_bol_' + k for k in ('croissant', 'croissant_almendra', 'napolitana', 'napolitana_crema', 'palmera', 'palmera_choco', 'ensaimada', 'donut_rosa', 'donut_choco', 'donut_azucar', 'magdalena', 'muffin_choco',
                                       'cana_crema', 'eclair', 'milhojas', 'tartaletas', 'bocados_hojaldre', 'torrijas', 'pestinos', 'rosquillas')]
TARTAS_F = ['pan_tarta_' + k for k in ('queso', 'chocolate', 'manzana', 'santiago', 'fresas', 'tres_chocolates', 'limon', 'cumple')] + ['pan_brazo_gitano', 'pan_roscon_reyes', 'pan_flan_pastelero', 'pan_empanada']
DULCES_F = ['pan_dulce_' + k for k in ('perrunillas', 'magdalenas_bolsa', 'roscos_anis', 'roscos_vino', 'mantecados', 'polvorones', 'turron', 'dulce_leche', 'sequillos', 'bollas_aceite', 'floretas', 'cabello_angel',
                                       'bizcochos_borrachos', 'mazapan')]
@kit
def panaderia():
    return {
        'tipologia': 'alimentacion', 'nombre': 'Panadería y pastelería', '_mood': 'panaderia',
        'nota': 'La panadería-pastelería de un pueblo de las Vegas Altas: el mostrador de cristal con la bollería y las tartas, tras él las estanterías del pan y el mueble de la caja con la cortadora; a la izquierda, los dulces típicos '
                '(perrunillas, magdalenas, roscos), una mesa de panes y un rincón para tomar café; al fondo, tras un tabique, el obrador con el horno, la amasadora y la laminadora. Luz cálida. La puerta en z = 0, el fondo en z = D; x de -W/2 a W/2.',
        'superficie': {'ancho': [6.0, 7.5], 'fondo': [9.3, 11.4], 'alto': 3.1},
        'variables': {'xc': 'W/2-2.0', 'z0': '1.8', 'zo': 'D-3.2', 'z1': 'zo-0.6'},
        'paso_libre': 0.9, 'pared': '#f4ead6', 'suelo': 'floor_tiles_06', 'suelo_color': '#d6c6a8',
        'puntos': {'dependiente': ['xc+0.8', '(z0+z1)/2'], 'mostrador': ['xc-0.95', '(z0+z1)/2']},
        'pedir': 'Pedir en el mostrador',
        'zonas': [
            Z('entrada', ['-W/2', '0', 'W/2', '1.4']),
            Z('barra', ['xc-0.3', 'z0', 'xc+0.3', 'z1'], False),
            Z('frente_barra', ['xc-1.4', 'z0', 'xc-0.33', 'z1']),
            Z('tras', ['xc+0.33', '1.5', 'W/2', 'zo'], False),
            Z('sala', ['-W/2', '1.4', 'xc-1.4', 'zo']),
            Z('obrador', ['-W/2', 'zo', 'W/2', 'D'], False),
            Z('luces_sala', ['-W/2', '0', 'xc-0.3', 'zo'], False),
            Z('luces_barra', ['xc-0.3', '0', 'W/2', 'zo'], False),
            Z('luces_obrador', ['-W/2', 'zo', 'W/2', 'D'], False),
        ],
        'tabiques': [{'de': ['-W/2', 'zo'], 'a': ['W/2', 'zo'], 'puerta': ['W-1.5', 1.0]}],
        'libres': [{'rect': ['xc-1.4', 'z0', 'xc-0.3', 'z1'], 'nota': 'el sitio para pedir en el mostrador: sin muebles delante'}],
        'objetos': [
            # ---- the glass counter first (the kit's own design) and what is in it
            E('barra', 'modulos', 'pan_vitrina_modulo', eje='z', linea=['xc', 'z0', 'z1'], mira='-x', obligatorio=True),
            sobre('barra', 'pan_bocadillos', ['pan_vitrina_modulo'], cantidad=[1, 1], obligatorio=True, vende='bocadillo'),
            sobre('barra', TARTAS_F, ['pan_vitrina_modulo'], por_soporte=[1, 2], todas=True, obligatorio=True),
            sobre('barra', BOLLERIA_F, ['pan_vitrina_modulo'], por_soporte=[2, 3], todas=True),
            # ---- behind the counter: the till and the slicer, the shelves of bread
            E('tras', 'contra_pared', 'pan_mueble_trasero', pared='E', cantidad=[1, 1], obligatorio=True),
            sobre('tras', 'pan_cortadora_pan', ['pan_mueble_trasero'], cantidad=[1, 1], obligatorio=True),
            sobre('tras', 'pel_tpv', ['pan_mueble_trasero'], cantidad=[1, 1], obligatorio=True),
            sobre('tras', ['cafetera_industrial', 'molinillo', 'pan_cinta_envolver', 'pan_caja_tarta', 'datafono', 'bote_propinas', 'pila_bolsas_papel'], ['pan_mueble_trasero'], cantidad=[3, 4], obligatorio=True),
            E('tras', 'contra_pared', 'pan_estanteria_pan', pared='E', llenar=True, obligatorio=True),
            sobre('tras', PANES_F, ['pan_estanteria_pan'], relleno=[0.9, 1.0], todas=True, obligatorio=True),
            E('tras', 'pared', 'pan_rotulo', pared='E', cantidad=[1, 1], obligatorio=True),
            E('tras', 'esquina', 'papelera', cantidad=[0, 1]),
            # ---- the shop floor: bread on a table, the rack of traditional sweets, the coffee corner
            E('sala', 'contra_pared', 'pan_estante_dulces', pared='W', cantidad=[1, 2], obligatorio=True),
            sobre('sala', DULCES_F, ['pan_estante_dulces'], relleno=[0.85, 1.0], todas=True, obligatorio=True, vende=['perrunillas', 'magdalenas']),
            E('sala', 'pared', 'pan_estante_pared', pared='W', cantidad=[1, 1], obligatorio=True),
            sobre('sala', ['pan_dulce_chocolate_tableta', 'pan_dulce_bombones', 'prod_agua_15', 'prod_agua_gas', 'pan_cafe_paquete'], ['pan_estante_pared'], relleno=[0.8, 1.0], todas=True, obligatorio=True, vende=['chocolate', 'agua']),
            E('sala', 'pared', variantes=['pan_pizarra_precios', 'pan_cartel_pan', 'pan_cartel_tarta', 'pan_pala_horno_pared', 'pan_cesta_colgante'], pared='N', cantidad=[2, 4], todas=True, obligatorio=True),
            E('sala', 'pared', variantes=['pan_cartel_tarta', 'pan_cesta_colgante', 'pan_cartel_pan'], pared='W', cantidad=[0, 2], todas=True),
            E('tras', 'pared', variantes=['pan_pala_horno_pared', 'pan_cesta_colgante'], pared='N', cantidad=[0, 2], todas=True),
            E('sala', 'suelo_libre', 'pan_mesa_pan', cantidad=[1, 1], obligatorio=True),
            sobre('sala', PANES_F[6:] + ['pan_dulce_roscos_vino'], ['pan_mesa_pan'], por_soporte=[2, 3], obligatorio=True, vende='pan'),
            E('sala', 'conjunto', 'mesa_redonda', variantes=['mesa_redonda', 'mesa_cuadrada'], sillas={'variantes': ['silla_bistro', 'silla_madera'], 'n': [2, 3]}, cantidad=[0, 2]),
            sobre('sala', ['servilletero', 'azucarero'], ['mesa_redonda', 'mesa_cuadrada'], por_soporte=1),
            E('sala', 'vida', variantes=['taza_cafe', 'plato_cafe', 'plato_tostada', 'vaso_agua', 'periodico', 'servilleta_arrugada'], en=['mesa_redonda', 'mesa_cuadrada'], por_soporte=[1, 2]),
            E('sala', 'esquina', 'planta_grande', cantidad=[0, 1]),
            E('entrada', 'esquina', 'papelera', cantidad=[1, 1], obligatorio=True),
            E('entrada', 'esquina', 'paraguas_cubo', cantidad=[0, 1]),
            E('entrada', 'contra_pared', 'revistero', pared='S', cantidad=[0, 1]),
            # ---- the obrador behind the partition
            E('obrador', 'contra_pared', 'pan_horno_rotativo', pared='N', cantidad=[1, 1], obligatorio=True),
            E('obrador', 'contra_pared', 'pan_amasadora', pared='N', cantidad=[1, 1], obligatorio=True),
            E('obrador', 'contra_pared', 'pan_camara_fermentacion', pared='W', cantidad=[1, 1], obligatorio=True),
            E('obrador', 'contra_pared', 'fregadero_acero', pared='E', cantidad=[1, 1], obligatorio=True),
            E('obrador', 'contra_pared', 'pan_estante_moldes', pared='W', cantidad=[0, 1]),
            E('obrador', 'suelo_libre', 'pan_laminadora', cantidad=[1, 1], obligatorio=True),
            E('obrador', 'suelo_libre', variantes=['pan_mesa_obrador', 'mesa_acero'], cantidad=[1, 2], todas=True, obligatorio=True),
            sobre('obrador', ['pan_batidora', 'pan_horno_sobremesa', 'pan_cubeta_masa', 'tabla_cortar', 'balanza_precision'], ['pan_mesa_obrador', 'mesa_acero'], por_soporte=[1, 2], obligatorio=True),
            E('obrador', 'suelo_libre', variantes=['pan_carro_bandejas', 'pan_carro_bandejas_vacio'], cantidad=[1, 2], todas=True, obligatorio=True),
            E('obrador', 'suelo_libre', variantes=['pan_pila_harina', 'pan_saco_harina', 'pan_cubeta_masa'], cantidad=[1, 2], todas=True),
            E('obrador', 'pared', 'pan_pala_obrador', pared='W', cantidad=[0, 1]),
            E('obrador', 'esquina', variantes=['fregona_cubo', 'escoba', 'papelera'], cantidad=[0, 1]),
            # ---- the light: warm panels over the shop, pendants over the counter
            E('luces_sala', 'techo', 'lampara_panel_led', por_m2=[0.1, 0.13], obligatorio=True),
            E('luces_barra', 'techo', 'lampara_colgante', por_m=[0.35, 0.45], obligatorio=True),
            E('luces_obrador', 'techo', 'lampara_panel_led', cantidad=[2, 2], obligatorio=True),
        ],
        'iluminacion': {'fuentes': [5, 9], 'temperatura_k': [2900, 3200], 'dia': {'intensidad': 0.85}, 'noche': {'intensidad': 1.0}, 'minimo_lux_publico': 150},
        'ambiente': {'sonido': 'tienda', 'horario_defecto': 'Mo-Sa 07:00-14:00,17:00-20:30; Su 07:30-14:00',
                     'vida': ['pan recién hecho', 'una bandeja de perrunillas', 'un café con una magdalena', 'la cola del mostrador'],
                     'cerrado': 'persiana bajada, el horno aún caliente',
                     'clientela': {'maximo': 3, 'horas': [[7, 10, 0.45], [10, 14, 0.4], [17, 20, 0.35]], 'frases': [
                         'Ponme una barra y un par de molletes, que vienen los nietos.', 'Estas perrunillas huelen igual que las de mi abuela.', 'Un café con leche y una magdalena, por favor.',
                         'Hoy el pan sale calentito, ¿eh?', 'Guárdame un roscón para el sábado.', 'Qué buena pinta tienen las tartas de hoy.']}},
        'minimo_objetos_distintos': 80,
    }

# ================================================================== THE HOUSEHOLD-APPLIANCE AND ELECTRONICS SHOP
APARATOS_F = ['ele_ap_' + k for k in ('cafetera_goteo', 'cafetera_capsulas', 'tostadora', 'batidora_mano', 'robot_cocina', 'plancha_ropa', 'aspirador_escoba', 'hervidor', 'freidora_aire', 'exprimidor', 'picadora', 'olla_arroz',
                                       'secador_pelo', 'afeitadora', 'bascula_bano', 'batidora_vaso')]
FRIOS = ['ele_frigorifico_combi_blanco', 'ele_frigorifico_combi_inox', 'ele_frigorifico_combi_negro', 'ele_frigorifico_dos_puertas', 'ele_frigorifico_americano', 'ele_congelador_vertical', 'ele_frigorifico_bajo', 'ele_arcon_congelador']
LAVADO = ['ele_lavadora_blanca', 'ele_lavadora_inox', 'ele_secadora', 'ele_lavasecadora', 'ele_lavadora_carga_superior', 'ele_lavavajillas_blanco', 'ele_lavavajillas_inox']
@kit
def electro():
    return {
        'tipologia': 'tienda_especializada', 'nombre': 'Electrodomésticos e imagen y sonido', '_mood': 'electro',
        'nota': 'La tienda de electrodomésticos y electrónica de un pueblo de las Vegas Altas: el mostrador con la caja, los cargadores y los auriculares junto a la puerta; frigoríficos y lavadoras en hilera contra la pared izquierda, cocinas, lavavajillas y estanterías de pequeños aparatos a la derecha; '
                'en el centro islas de pequeño electrodoméstico, ventiladores, radios y lámparas; al fondo el muro de televisores sobre el tabique del almacén. Luz fría de tienda. La puerta en z = 0, el fondo en z = D; x de -W/2 a W/2.',
        'superficie': {'ancho': [6.6, 8.1], 'fondo': [9.9, 12.3], 'alto': 3.2},
        'variables': {'xc': 'W/2-1.7', 'z0': '1.6', 'z1': '4.1', 'zp': 'D-3.0'},
        'paso_libre': 0.9, 'pared': '#eeeeea', 'suelo': 'floor_tiles_06', 'suelo_color': '#c9c9c4',
        'puntos': {'dependiente': ['xc+0.8', '(z0+z1)/2'], 'mostrador': ['xc-0.95', '(z0+z1)/2']},
        'pedir': 'Pedir presupuesto o pagar en el mostrador',
        'zonas': [
            Z('entrada', ['-W/2', '0', 'W/2', '1.3']),
            Z('barra', ['xc-0.3', 'z0', 'xc+0.3', 'z1'], False),
            Z('frente_barra', ['xc-1.4', 'z0', 'xc-0.33', 'z1']),
            Z('tras', ['xc+0.33', '1.3', 'W/2', '4.4'], False),
            Z('pared_w', ['-W/2', '1.3', '-W/2+0.95', 'zp'], False),
            Z('pared_e', ['W/2-0.95', '4.9', 'W/2', 'zp'], False),
            Z('centro', ['-W/2+0.95', '1.3', 'W/2-0.95', 'zp-2.3']),
            Z('tv', ['-W/2+0.95', 'zp-2.3', 'W/2-0.95', 'zp']),
            Z('almacen', ['-W/2', 'zp', 'W/2', 'D'], False),
            Z('luces', ['-W/2', '0', 'W/2', 'zp'], False),
            Z('luces_almacen', ['-W/2', 'zp', 'W/2', 'D'], False),
        ],
        'tabiques': [{'de': ['-W/2', 'zp'], 'a': ['W/2', 'zp'], 'puerta': ['W-1.6', 1.0]}],
        'libres': [{'rect': ['xc-1.4', 'z0', 'xc-0.3', 'z1'], 'nota': 'el sitio para pedir en el mostrador: sin muebles delante'}],
        'objetos': [
            # ---- the counter first: till, chargers, headphones, torches
            E('barra', 'modulos', 'ele_mostrador', eje='z', linea=['xc', 'z0', 'z1'], mira='-x', obligatorio=True),
            sobre('barra', 'ele_cargadores_exp', ['ele_mostrador'], cantidad=[1, 1], obligatorio=True, vende='cargador'),
            sobre('barra', 'ele_auriculares_exp', ['ele_mostrador'], cantidad=[1, 1], obligatorio=True, vende='auriculares'),
            sobre('barra', 'ele_linternas_exp', ['ele_mostrador'], cantidad=[1, 1], obligatorio=True, vende='linterna'),
            sobre('barra', 'pel_tpv', ['ele_mostrador'], cantidad=[1, 1], obligatorio=True),
            sobre('barra', ['ele_catalogo', 'datafono', 'ele_radio_despertador', 'ele_altavoz_bluetooth', 'bote_propinas'], ['ele_mostrador'], cantidad=[2, 3], obligatorio=True),
            E('tras', 'contra_pared', 'ele_estanteria_baja', pared='E', cantidad=[1, 2], obligatorio=True),
            sobre('tras', ['ele_bombillas_exp', 'ele_flexo', 'ele_lamparita_mesa', 'ele_radio_portatil', 'ele_cargadores_exp', 'ele_linternas_exp'], ['ele_estanteria_baja'], relleno=[0.6, 0.9], todas=True),
            E('tras', 'pared', 'ele_rotulo', pared='E', cantidad=[1, 1], obligatorio=True),
            E('tras', 'esquina', 'papelera', cantidad=[1, 1], obligatorio=True),
            E('tras', 'suelo_libre', variantes=['silla_cajera', 'taburete_alto'], cantidad=[0, 1]),
            # ---- the west wall: fridges and freezers, then the washing machines
            E('pared_w', 'contra_pared', variantes=FRIOS, pared='W', cantidad=[3, 5], todas=True, obligatorio=True),
            sobre('pared_w', ['ele_catalogo', 'ele_lamparita_mesa'], ['ele_arcon_congelador', 'ele_frigorifico_bajo'], cantidad=[0, 1]),
            E('pared_w', 'contra_pared', variantes=LAVADO, pared='W', llenar=True, todas=True, obligatorio=True),
            sobre('pared_w', ['ele_catalogo', 'ele_flexo', 'ele_radio_despertador'], LAVADO[:5], cantidad=[0, 2]),
            # ---- the east wall: shelves of small appliances in their boxes, then cookers and dishwashers
            E('pared_e', 'contra_pared', 'ele_estanteria_pequenos', pared='E', cantidad=[1, 2], obligatorio=True),
            sobre('pared_e', APARATOS_F, ['ele_estanteria_pequenos'], relleno=[0.85, 1.0], todas=True, obligatorio=True),
            E('pared_e', 'contra_pared', variantes=['ele_cocina_vitro', 'ele_cocina_inox', 'ele_torre_horno', 'ele_lavavajillas_blanco', 'ele_lavavajillas_inox', 'ele_frigorifico_bajo'], pared='E', llenar=True, todas=True),
            E('pared_e', 'pared', 'ele_campana_pared', pared='E', cantidad=[0, 2]),
            # ---- the middle: islands of small appliances, fans, radios and lamps
            E('centro', 'suelo_libre', 'ele_isla_pequenos', cantidad=[2, 3], obligatorio=True),
            sobre('centro', APARATOS_F, ['ele_isla_pequenos'], por_soporte=[3, 4], todas=True, obligatorio=True),
            sobre('centro', ['ele_radio_clasica', 'ele_radio_portatil', 'ele_radio_despertador', 'ele_equipo_musica', 'ele_altavoz_bluetooth'], ['ele_isla_pequenos'], por_soporte=[0, 1], vende='radio'),
            sobre('centro', ['ele_ventilador_sobremesa', 'ele_lamparita_mesa', 'ele_flexo'], ['ele_isla_pequenos'], por_soporte=[1, 2], vende=['ventilador', 'lamparita']),
            E('centro', 'suelo_libre', variantes=['ele_ventilador_pie', 'ele_ventilador_torre', 'ele_aire_portatil'], cantidad=[2, 3], todas=True, obligatorio=True, vende='ventilador'),
            E('centro', 'suelo_libre', 'ele_lampara_pie_led', cantidad=[1, 2], obligatorio=True, vende='lampara'),
            E('centro', 'suelo_libre', variantes=['ele_arcon_congelador', 'ele_caja_nevera'], cantidad=[0, 1]),
            E('centro', 'esquina', 'planta_grande', cantidad=[0, 1]),
            E('entrada', 'esquina', 'papelera', cantidad=[1, 1], obligatorio=True),
            E('entrada', 'esquina', 'paraguas_cubo', cantidad=[0, 1]),
            E('entrada', 'contra_pared', 'ele_carretilla_electro', pared='W', cantidad=[0, 1]),
            E('entrada', 'pared', variantes=['ele_cartel_nevera', 'ele_cartel_lavadora', 'ele_cartel_tv'], pared='W', cantidad=[1, 2], todas=True),
            # ---- the television wall and the plinths
            E('tv', 'pared', 'ele_pared_pantallas', pared='N', cantidad=[0, 1]),
            E('tv', 'pared', variantes=['ele_tv_pared_65', 'ele_tv_pared_55', 'ele_tv_pared_50', 'ele_tv_pared_43', 'ele_tv_pared_32'], pared='N', cada=1.45, maximo=4, todas=True),
            E('tv', 'pared', 'ele_pantalla_ofertas', pared='N', cantidad=[0, 1]),
            E('tv', 'suelo_libre', 'ele_plinto_tv', cantidad=[1, 2], obligatorio=True),
            sobre('tv', ['ele_tv_peana_32', 'ele_tv_peana_43', 'ele_tv_peana_50'], ['ele_plinto_tv'], por_soporte=[1, 2], todas=True, obligatorio=True, vende='tele'),
            sobre('tv', ['ele_barra_sonido', 'ele_altavoz_torre', 'ele_equipo_musica'], ['ele_plinto_tv'], por_soporte=[0, 1]),
            E('tv', 'suelo_libre', variantes=['ele_altavoz_torre', 'ele_ventilador_torre'], cantidad=[0, 2]),
            # ---- the storeroom behind the partition
            E('almacen', 'contra_pared', 'estanteria_metalica', pared='N', cantidad=[1, 2], obligatorio=True),
            sobre('almacen', ['ele_ap_robot_cocina', 'ele_ap_freidora_aire', 'ele_ap_aspirador_escoba', 'caja_carton', 'ele_ap_cafetera_capsulas'], ['estanteria_metalica'], relleno=[0.6, 0.9], todas=True, obligatorio=True),
            E('almacen', 'suelo_libre', variantes=['ele_caja_lavadora', 'ele_caja_nevera', 'ele_caja_tv', 'ele_caja_cocina'], cantidad=[3, 4], todas=True, obligatorio=True),
            E('almacen', 'suelo_libre', variantes=['palet_madera', 'transpaleta', 'ele_carretilla_electro'], cantidad=[1, 2], todas=True),
            E('almacen', 'esquina', 'fregona_cubo', cantidad=[0, 1]),
            # ---- the light
            E('luces', 'techo', 'lampara_panel_led', por_m2=[0.1, 0.13], obligatorio=True),
            E('luces_almacen', 'techo', 'regleta_led', cantidad=[1, 2], obligatorio=True),
        ],
        'iluminacion': {'fuentes': [5, 9], 'temperatura_k': [3800, 4300], 'dia': {'intensidad': 0.9}, 'noche': {'intensidad': 1.0}, 'minimo_lux_publico': 200},
        'ambiente': {'sonido': 'tienda', 'horario_defecto': 'Mo-Fr 10:00-13:45,17:00-20:30; Sa 10:00-14:00',
                     'vida': ['la tele del escaparate encendida', 'una lavadora con la etiqueta de oferta', 'cajas apiladas junto al almacén', 'el catálogo del mes'],
                     'cerrado': 'persiana bajada, las pantallas apagadas'},
        'minimo_objetos_distintos': 40,
    }

# ================================================================== THE COMPUTER AND PHONE SHOP
ACC_F = ['inf_acc_' + k for k in ('auriculares_cable', 'cargador_pared', 'radio_bolsillo', 'linterna_led', 'lamparita_usb', 'auriculares_bt', 'cargador_coche', 'fundas_negras', 'fundas_color', 'protectores_pantalla',
                                  'cables_usb', 'bateria_externa', 'raton', 'alfombrilla', 'webcam', 'memoria_sd', 'soporte_movil')]
MOVILES = ['inf_movil_' + k for k in ('negro', 'azul', 'blanco', 'rojo', 'verde', 'plata')]
@kit
def informatica():
    return {
        'tipologia': 'tienda_especializada', 'nombre': 'Informática y telefonía', '_mood': 'informatica',
        'nota': 'La tienda de informática y móviles de un pueblo de las Vegas Altas: el mostrador con las tarjetas SIM y los teléfonos junto a la puerta, mesas con portátiles y móviles de prueba, un puesto de ordenador, '
                'estanterías y paneles de accesorios (fundas, cables, auriculares, cargadores) y, al fondo a la derecha, el taller de reparaciones tras un tabique. Marcas inventadas. La puerta en z = 0, el fondo en z = D; x de -W/2 a W/2.',
        'superficie': {'ancho': [5.7, 7.2], 'fondo': [8.7, 10.8], 'alto': 3.0},
        'variables': {'xc': 'W/2-1.6', 'z0': '1.6', 'z1': '4.1', 'zr': 'D-3.0', 'xr': 'W/2-2.7'},
        'paso_libre': 0.9, 'pared': '#eef0f2', 'suelo': 'floor_tiles_06', 'suelo_color': '#c6c8cc',
        'puntos': {'dependiente': ['xc+0.8', '(z0+z1)/2'], 'mostrador': ['xc-0.95', '(z0+z1)/2']},
        'pedir': 'Preguntar por un móvil o un arreglo en el mostrador',
        'zonas': [
            Z('entrada', ['-W/2', '0', 'W/2', '1.3']),
            Z('barra', ['xc-0.3', 'z0', 'xc+0.3', 'z1'], False),
            Z('frente_barra', ['xc-1.4', 'z0', 'xc-0.33', 'z1']),
            Z('tras', ['xc+0.33', '1.3', 'W/2', '4.4'], False),
            Z('pared_w', ['-W/2', '1.3', '-W/2+0.55', 'zr'], False),
            Z('sala', ['-W/2+0.55', '1.3', 'xc-1.4', 'zr']),
            Z('sala_e', ['xc-1.4', '4.4', 'W/2', 'zr']),
            Z('fondo', ['-W/2+0.55', 'zr', 'xr', 'D']),
            Z('reparacion', ['xr', 'zr', 'W/2', 'D'], False),
            Z('luces', ['-W/2', '0', 'W/2', 'D'], False),
        ],
        'tabiques': [{'de': ['xr', 'zr'], 'a': ['xr', 'D'], 'puerta': [0.5, 1.0]}, {'de': ['xr', 'zr'], 'a': ['W/2', 'zr']}],
        'libres': [{'rect': ['xc-1.4', 'z0', 'xc-0.3', 'z1'], 'nota': 'el sitio para preguntar en el mostrador: sin muebles delante'}],
        'objetos': [
            # ---- the counter first: till, SIM cards, a stand of phones
            E('barra', 'modulos', 'inf_mostrador', eje='z', linea=['xc', 'z0', 'z1'], mira='-x', obligatorio=True),
            sobre('barra', 'inf_expositor_moviles', ['inf_mostrador'], cantidad=[1, 1], obligatorio=True),
            sobre('barra', 'pel_tpv', ['inf_mostrador'], cantidad=[1, 1], obligatorio=True),
            sobre('barra', 'inf_exp_sim', ['inf_mostrador'], cantidad=[1, 1], obligatorio=True),
            sobre('barra', ['inf_pendrives_exp', 'datafono', 'inf_router', 'ele_catalogo', 'inf_disco_duro'], ['inf_mostrador'], cantidad=[2, 3], obligatorio=True),
            E('tras', 'contra_pared', 'inf_estanteria_accesorios', pared='E', cantidad=[1, 2], obligatorio=True),
            sobre('tras', ['inf_caja_pc', 'inf_router', 'inf_disco_duro', 'inf_pendrives_exp', 'inf_movil_negro', 'inf_movil_azul'], ['inf_estanteria_accesorios'], relleno=[0.5, 0.8], todas=True),
            E('tras', 'pared', 'inf_rotulo', pared='E', cantidad=[1, 1], obligatorio=True),
            E('tras', 'esquina', 'papelera', cantidad=[1, 1], obligatorio=True),
            E('tras', 'suelo_libre', 'silla_oficina', cantidad=[0, 1]),
            # ---- the west wall: shelves of accessories in their packs (the first five are the ones on sale)
            E('pared_w', 'contra_pared', 'inf_estanteria_accesorios', pared='W', llenar=True, obligatorio=True),
            sobre('pared_w', ACC_F, ['inf_estanteria_accesorios'], relleno=[0.9, 1.0], todas=True, obligatorio=True, vende=['auriculares', 'cargador', 'radio', 'linterna', 'lamparita']),
            # ---- the shop floor: laptops and phones to try, a PC, accessories on the wall
            E('sala', 'suelo_libre', 'inf_puesto_pc_exp', cantidad=[1, 1], obligatorio=True),
            sobre('sala', ['inf_teclado_raton', 'inf_router', 'inf_disco_duro'], ['inf_puesto_pc_exp'], por_soporte=[0, 1]),
            E('sala', 'suelo_libre', 'inf_mesa_exposicion', cantidad=[1, 2], obligatorio=True),
            sobre('sala', ['inf_portatil_13', 'inf_portatil_15', 'inf_portatil_17', 'inf_monitor_22', 'inf_todo_en_uno'], ['inf_mesa_exposicion'], por_soporte=[2, 3], todas=True, obligatorio=True),
            sobre('sala', ['inf_impresora', 'inf_teclado_raton', 'inf_router', 'inf_disco_duro', 'inf_monitor_24', 'inf_monitor_27'], ['inf_mesa_exposicion'], por_soporte=[1, 2]),
            E('sala', 'suelo_libre', 'inf_mesa_moviles', cantidad=[0, 1]),
            sobre('sala', MOVILES, ['inf_mesa_moviles'], por_soporte=[2, 4], todas=True),
            sobre('sala', ['inf_pendrives_exp', 'inf_exp_sim'], ['inf_mesa_moviles'], por_soporte=[0, 1]),
            E('sala', 'suelo_libre', variantes=['taburete_alto', 'silla_visita'], cantidad=[1, 2], todas=True),
            E('sala_e', 'pared', variantes=['inf_panel_fundas', 'inf_panel_cables', 'inf_panel_auriculares'], pared='E', cada=1.35, maximo=3, todas=True),
            E('sala_e', 'suelo_libre', variantes=['inf_torre_pc', 'inf_caja_portatil'], cantidad=[0, 2], todas=True),
            E('sala_e', 'esquina', 'planta_grande', cantidad=[0, 1]),
            E('entrada', 'esquina', 'papelera', cantidad=[1, 1], obligatorio=True),
            E('entrada', 'esquina', 'paraguas_cubo', cantidad=[0, 1]),
            E('entrada', 'pared', variantes=['inf_cartel_movil', 'inf_cartel_portatil', 'inf_pantalla_precios'], pared='W', cantidad=[1, 2], todas=True, obligatorio=True),
            # ---- the back wall
            E('fondo', 'pared', variantes=['inf_panel_cables', 'inf_panel_fundas', 'inf_panel_auriculares'], pared='N', cada=1.35, maximo=2, todas=True),
            E('fondo', 'pared', 'inf_pantalla_pared', pared='N', cantidad=[0, 1]),
            E('fondo', 'esquina', 'planta_grande', cantidad=[0, 1]),
            E('fondo', 'pared', 'extintor_super', pared='N', cantidad=[0, 1]),
            # ---- the repair shop behind the partition
            E('reparacion', 'contra_pared', 'inf_banco_reparacion', pared='N', cantidad=[1, 1], obligatorio=True),
            sobre('reparacion', ['inf_soldador', 'inf_destornilladores', 'inf_placa_madre', 'inf_movil_abierto', 'inf_portatil_13'], ['inf_banco_reparacion'], por_soporte=[2, 3], todas=True, obligatorio=True),
            E('reparacion', 'esquina', 'inf_taburete_reparacion', cantidad=[1, 1], obligatorio=True),
            E('reparacion', 'contra_pared', 'inf_estanteria_piezas', pared='E', cantidad=[1, 2], obligatorio=True),
            sobre('reparacion', ['inf_caja_pc', 'caja_carton', 'inf_router', 'inf_impresora', 'inf_disco_duro', 'inf_movil_negro'], ['inf_estanteria_piezas'], relleno=[0.6, 0.9], todas=True, obligatorio=True),
            E('reparacion', 'suelo_libre', variantes=['inf_cajonera_piezas', 'inf_caja_portatil', 'inf_torre_pc'], cantidad=[1, 2], todas=True),
            sobre('reparacion', ['inf_destornilladores', 'inf_placa_madre'], ['inf_cajonera_piezas'], cantidad=[0, 1]),
            E('reparacion', 'esquina', 'papelera', cantidad=[0, 1]),
            # ---- the light
            E('luces', 'techo', 'lampara_panel_led', por_m2=[0.11, 0.14], obligatorio=True),
        ],
        'iluminacion': {'fuentes': [5, 9], 'temperatura_k': [4000, 4500], 'dia': {'intensidad': 0.9}, 'noche': {'intensidad': 1.0}, 'minimo_lux_publico': 200},
        'ambiente': {'sonido': 'tienda', 'horario_defecto': 'Mo-Fr 10:00-14:00,17:00-20:30; Sa 10:00-14:00',
                     'vida': ['un portátil abierto para probar', 'el móvil de un cliente en reparación', 'los cables enrollados en el panel', 'la pantalla de ofertas'],
                     'cerrado': 'persiana bajada, las pantallas apagadas'},
        'minimo_objetos_distintos': 40,
    }

# ================================================================== THE FURNITURE AND DECORATION SHOWROOM
SOFAS3 = ['mue_sofa_3p_beige', 'mue_sofa_3p_gris', 'mue_sofa_3p_verde', 'mue_sofa_3p_azul']
SOFAS2 = ['mue_sofa_2p_mostaza', 'mue_sofa_2p_rosa', 'mue_sofa_2p_crema']
SILLONES = ['mue_sillon_orejero', 'mue_sillon_moderno', 'mue_sillon_relax']
PUFS = ['mue_puff_redondo_mostaza', 'mue_puff_redondo_gris', 'mue_puff_cuadrado_verde', 'mue_puff_cuadrado_rosa']
ALFOMBRAS = ['mue_alfombra_gris', 'mue_alfombra_roja', 'mue_alfombra_beige', 'mue_alfombra_azul', 'mue_alfombra_redonda', 'mue_alfombra_pasillo']
COJINES = ['mue_cojines_mostaza', 'mue_cojines_verde', 'mue_cojines_rojo', 'mue_cojines_azul']
CAMAS = ['mue_cama_150_madera', 'mue_cama_150_nogal', 'mue_cama_150_tapizada', 'mue_cama_135_blanca', 'mue_cama_90_juvenil']
MESILLAS = ['mue_mesilla_roble', 'mue_mesilla_blanca', 'mue_mesilla_nogal']
LAMPARAS_MESA = ['mue_lampara_mesa_azul', 'mue_lampara_mesa_blanca', 'mue_lampara_mesa_verde']
ADORNOS = ['mue_jarron_azul', 'mue_jarron_blanco', 'mue_jarron_verde', 'mue_libros_filas', 'mue_marcos_foto', 'mue_cuenco_decorativo']
ADORNOS_BAJOS = ['mue_jarron_azul', 'mue_jarron_verde', 'mue_libros_filas', 'mue_marcos_foto', 'mue_cuenco_decorativo']   # (no taller que el hueco entre dos baldas)
SILLAS = ['mue_silla_comedor_roble', 'mue_silla_comedor_tapizada', 'mue_silla_comedor_blanca', 'mue_silla_comedor_nogal']
CUADROS = ['mue_cuadro_a', 'mue_cuadro_b', 'mue_cuadro_c', 'mue_cuadro_d', 'mue_cuadro_e']
ESPEJOS = ['mue_espejo_redondo', 'mue_espejo_alto', 'mue_espejo_marco_nogal', 'mue_espejo_dorado']
@kit
def muebles():
    return {
        'tipologia': 'tienda_especializada', 'nombre': 'Muebles y decoración', '_mood': 'muebles',
        'nota': 'La tienda de muebles y decoración de un pueblo de las Vegas Altas: junto a la puerta, la mesa del vendedor con el catálogo; contra la pared izquierda los sofás con sus cojines, y delante butacas, pufs, mesas de centro, alfombras y lámparas; '
                'contra la derecha aparadores, librerías y vitrinas; en el centro los juegos de comedor; al fondo el dormitorio con las camas hechas y las mesillas, y el almacén de cajas tras un tabique. Luz cálida. La puerta en z = 0, el fondo en z = D; x de -W/2 a W/2.',
        'superficie': {'ancho': [7.2, 9.0], 'fondo': [11.4, 13.8], 'alto': 3.2},
        'variables': {'xc': 'W/2-1.8', 'z0': '1.8', 'z1': '3.4', 'zb': 'D-3.4', 'xk': 'W/2-2.6'},
        'paso_libre': 0.9, 'pared': '#f1e8d6', 'suelo': 'herringbone_parquet', 'suelo_color': '#cbb48c',
        'puntos': {'dependiente': ['xc+0.85', '(z0+z1)/2'], 'mostrador': ['xc-1.0', '(z0+z1)/2']},
        'pedir': 'Preguntar por un mueble o hacer un pedido',
        'zonas': [
            Z('entrada', ['-W/2', '0', 'W/2', '1.5']),
            Z('barra', ['xc-0.4', 'z0', 'xc+0.4', 'z1'], False),
            Z('frente_barra', ['xc-1.5', 'z0', 'xc-0.43', 'z1']),
            Z('tras', ['xc+0.43', '1.5', 'W/2', '4.0'], False),
            Z('pared_w', ['-W/2', '1.6', '-W/2+1.1', 'zb'], False),
            Z('salon', ['-W/2+1.1', '1.5', 'xc-1.5', '5.2']),
            Z('comedor', ['-W/2+1.1', '5.2', 'W/2-0.9', 'zb']),
            Z('pared_e', ['W/2-0.9', '4.4', 'W/2', 'zb+0.8'], False),
            Z('dormitorio', ['-W/2', 'zb', 'xk', 'D']),
            Z('almacen', ['xk', 'zb', 'W/2', 'D'], False),
            Z('luces_e', ['-W/2', '0', 'W/2', '3.0'], False),
            Z('luces_salon', ['-W/2', '3.0', 'W/2', '5.2'], False),
            Z('luces_comedor', ['-W/2', '5.2', 'W/2', 'zb'], False),
            Z('luces_dormitorio', ['-W/2', 'zb', 'xk', 'D'], False),
            Z('luces_almacen', ['xk', 'zb', 'W/2', 'D'], False),
        ],
        'tabiques': [{'de': ['xk', 'zb'], 'a': ['xk', 'D']}, {'de': ['xk', 'zb'], 'a': ['W/2', 'zb'], 'puerta': [0.4, 1.0]}],
        'libres': [{'rect': ['xc-1.5', 'z0', 'xc-0.4', 'z1'], 'nota': 'el sitio para atender al cliente en la mesa del vendedor: sin muebles delante'}],
        'objetos': [
            # ---- the salesperson's desk first (the kit's own design)
            E('barra', 'modulos', 'mue_mostrador_atencion', eje='z', linea=['xc', 'z0', 'z1'], mira='-x', obligatorio=True),
            sobre('barra', 'inf_portatil_15', ['mue_mostrador_atencion'], cantidad=[1, 1], obligatorio=True),
            sobre('barra', 'mue_catalogo_muebles', ['mue_mostrador_atencion'], cantidad=[1, 1], obligatorio=True),
            sobre('barra', ['datafono', 'bote_propinas', 'mue_marcos_foto', 'mue_jarron_blanco'], ['mue_mostrador_atencion'], cantidad=[1, 2]),
            E('tras', 'contra_pared', 'mue_libreria_blanca', pared='E', cantidad=[1, 1], obligatorio=True),
            sobre('tras', ADORNOS_BAJOS, ['mue_libreria_blanca'], relleno=[0.5, 0.8], todas=True),
            E('tras', 'pared', 'mue_rotulo', pared='E', cantidad=[1, 1], obligatorio=True),
            E('tras', 'suelo_libre', 'silla_oficina', cantidad=[1, 1], obligatorio=True),
            E('tras', 'esquina', 'papelera', cantidad=[1, 1], obligatorio=True),
            # ---- the west wall: sofas with their cushions, pictures and mirrors above
            E('pared_w', 'contra_pared', variantes=SOFAS3, pared='W', cantidad=[2, 2], todas=True, obligatorio=True, vende='sofa'),
            E('pared_w', 'contra_pared', variantes=SOFAS2, pared='W', cantidad=[0, 2], todas=True),
            sobre('pared_w', COJINES, SOFAS3 + SOFAS2, por_soporte=[1, 1], todas=True, obligatorio=True, vende='cojines'),
            E('pared_w', 'pared', variantes=CUADROS, pared='W', cantidad=[2, 3], todas=True, obligatorio=True, vende='cuadro'),
            E('pared_w', 'pared', variantes=ESPEJOS, pared='W', cantidad=[0, 2], todas=True, vende='espejo'),
            E('pared_w', 'pared', 'mue_reloj_pared_grande', pared='W', cantidad=[0, 1], vende='reloj'),
            E('pared_w', 'contra_pared', variantes=['mue_estanteria_cubos', 'mue_estanteria_cubos_blanca'], pared='W', cantidad=[0, 1]),
            sobre('pared_w', ADORNOS_BAJOS, ['mue_estanteria_cubos', 'mue_estanteria_cubos_blanca'], relleno=[0.5, 0.8], todas=True),
            # ---- the front of the showroom: armchairs, poufs, coffee tables, rugs and lamps
            E('salon', 'suelo_libre', variantes=['mue_mesa_centro_cuadrada', 'mue_mesa_centro_redonda', 'mue_mesa_centro_baja'], cantidad=[1, 2], todas=True, obligatorio=True),
            sobre('salon', ADORNOS, ['mue_mesa_centro_cuadrada', 'mue_mesa_centro_redonda', 'mue_mesa_centro_baja'], por_soporte=[1, 2], obligatorio=True),
            E('salon', 'suelo_libre', variantes=ALFOMBRAS[:5], cantidad=[2, 2], todas=True, obligatorio=True, vende='alfombra'),
            E('salon', 'suelo_libre', variantes=SILLONES, cantidad=[1, 3], todas=True, obligatorio=True, vende='sillon'),
            E('salon', 'suelo_libre', variantes=PUFS, cantidad=[1, 3], todas=True, obligatorio=True, vende='puff'),
            E('salon', 'suelo_libre', variantes=['mue_lampara_pie_laton', 'mue_lampara_pie_negra', 'mue_lampara_pie_madera'], cantidad=[1, 2], todas=True, obligatorio=True, vende='lampara'),
            E('salon', 'suelo_libre', 'mue_mesa_auxiliar', cantidad=[1, 2], vende='mesita'),
            sobre('salon', LAMPARAS_MESA + ['mue_marcos_foto'], ['mue_mesa_auxiliar'], por_soporte=1, vende='lamparita'),
            E('salon', 'esquina', 'planta_grande', cantidad=[0, 1]),
            E('entrada', 'esquina', 'planta_grande', cantidad=[0, 1]),
            E('entrada', 'esquina', 'papelera', cantidad=[1, 1], obligatorio=True),
            E('entrada', 'esquina', 'paraguas_cubo', cantidad=[0, 1]),
            E('entrada', 'pared', variantes=['mue_cartel_sofa', 'mue_cartel_cama'], pared='W', cantidad=[1, 2], todas=True),
            # ---- the east wall: bookcases, sideboards, a display cabinet, the TV unit
            E('pared_e', 'contra_pared', variantes=['mue_libreria_alta', 'mue_libreria_blanca'], pared='E', cantidad=[1, 2], todas=True, obligatorio=True, vende='estanteria'),
            E('pared_e', 'contra_pared', variantes=['mue_aparador_roble', 'mue_vitrina_salon', 'mue_aparador_blanco', 'mue_mueble_tv', 'mue_aparador_nogal', 'mue_comoda_cajones', 'mue_zapatero'], pared='E', llenar=True, todas=True, obligatorio=True),
            sobre('pared_e', ADORNOS_BAJOS, ['mue_libreria_alta', 'mue_libreria_blanca'], relleno=[0.5, 0.9], todas=True),
            sobre('pared_e', ADORNOS + LAMPARAS_MESA, ['mue_aparador_roble', 'mue_aparador_blanco', 'mue_aparador_nogal', 'mue_comoda_cajones', 'mue_zapatero'], por_soporte=[1, 2]),
            E('pared_e', 'pared', variantes=['mue_espejo_marco_nogal', 'mue_cuadro_c', 'mue_cuadro_a', 'mue_reloj_pared_grande'], pared='E', cada=1.4, maximo=2, todas=True),
            # ---- the dining sets, in the middle
            E('comedor', 'conjunto', variantes=['mue_mesa_comedor_roble', 'mue_mesa_comedor_blanca', 'mue_mesa_comedor_redonda'], sillas={'variantes': SILLAS, 'n': [4, 4]}, cantidad=[1, 2], obligatorio=True, vende='mesa'),
            sobre('comedor', ADORNOS, ['mue_mesa_comedor_roble', 'mue_mesa_comedor_blanca', 'mue_mesa_comedor_redonda'], por_soporte=[1, 2]),
            E('comedor', 'suelo_libre', variantes=ALFOMBRAS[2:], cantidad=[1, 2], todas=True),
            E('comedor', 'suelo_libre', 'mue_taburete_alto', cantidad=[0, 2]),
            E('comedor', 'esquina', 'planta_grande', cantidad=[0, 1]),
            # ---- the bedroom: beds made up, bedside tables with their lamps, wardrobes
            E('dormitorio', 'contra_pared', variantes=['mue_armario_3p', 'mue_armario_2p', 'mue_armario_4p_nogal'], pared='W', cantidad=[1, 1], obligatorio=True),
            E('dormitorio', 'contra_pared', variantes=CAMAS, pared='N', cantidad=[2, 2], todas=True, obligatorio=True),
            E('dormitorio', 'contra_pared', variantes=MESILLAS, pared='N', cantidad=[1, 3], todas=True, obligatorio=True),
            sobre('dormitorio', LAMPARAS_MESA, MESILLAS, por_soporte=[1, 1], todas=True, obligatorio=True, vende='lamparita'),
            E('dormitorio', 'pared', variantes=CUADROS, pared='N', cantidad=[1, 2], todas=True),
            E('dormitorio', 'contra_pared', variantes=['mue_comoda_blanca', 'mue_comoda_cajones'], pared='W', cantidad=[0, 1]),
            sobre('dormitorio', ADORNOS, ['mue_comoda_blanca', 'mue_comoda_cajones'], por_soporte=[1, 2]),
            E('dormitorio', 'pared', 'mue_espejo_alto', pared='W', cantidad=[0, 1]),
            E('dormitorio', 'suelo_libre', variantes=['mue_colchon_muestra', 'mue_alfombra_pasillo', 'mue_lampara_pie_negra'], cantidad=[0, 2], todas=True),
            E('dormitorio', 'esquina', 'planta_grande', cantidad=[0, 1]),
            # ---- the storeroom
            E('almacen', 'contra_pared', 'estanteria_metalica', pared='N', cantidad=[1, 1], obligatorio=True),
            sobre('almacen', ['caja_carton', 'mue_jarron_verde', 'mue_cojines_azul', 'mue_lampara_mesa_azul'], ['estanteria_metalica'], relleno=[0.6, 0.9], todas=True, obligatorio=True),
            E('almacen', 'suelo_libre', variantes=['mue_pila_cajas_plana', 'mue_caja_mueble_plana', 'mue_colchon_plastico', 'mue_carro_muebles'], cantidad=[1, 4], todas=True, obligatorio=True),
            E('almacen', 'suelo_libre', variantes=['palet_madera', 'transpaleta'], cantidad=[0, 1]),
            E('almacen', 'esquina', 'fregona_cubo', cantidad=[0, 1]),
            # ---- the light: a panel at the door, glass chandeliers in the lounge, cloth shades elsewhere
            E('luces_e', 'techo', 'lampara_panel_led', cantidad=[2, 2], obligatorio=True),
            E('luces_salon', 'techo', 'mue_lampara_techo_cristal', cantidad=[2, 2], obligatorio=True),
            E('luces_comedor', 'techo', 'mue_lampara_techo_pantalla', cantidad=[2, 2], obligatorio=True),
            E('luces_dormitorio', 'techo', 'mue_lampara_techo_pantalla', cantidad=[2, 2], obligatorio=True),
            E('luces_almacen', 'techo', 'regleta_led', cantidad=[1, 1], obligatorio=True),
        ],
        'iluminacion': {'fuentes': [5, 9], 'temperatura_k': [2900, 3200], 'dia': {'intensidad': 0.85}, 'noche': {'intensidad': 1.0}, 'minimo_lux_publico': 120},
        'ambiente': {'sonido': 'tienda', 'horario_defecto': 'Mo-Fr 10:00-13:45,17:00-20:30; Sa 10:00-14:00',
                     'vida': ['una pareja probando el sofá', 'la cama hecha con su colcha', 'un cliente midiendo el aparador', 'el catálogo abierto en la mesa'],
                     'cerrado': 'reja bajada, las lámparas del escaparate encendidas',
                     'clientela': {'maximo': 3, 'horas': [[10, 14, 0.3], [17, 20, 0.35]], 'frases': [
                         'Este sofá es más cómodo de lo que parece, ¿eh?', '¿Lo tenéis en otro color? Es para el salón de mi madre.', 'Mi marido quiere el aparador de roble y yo el blanco.',
                         'Fíjate qué buena cama; con el colchón se pone en nada.', 'Hay que medir bien el hueco antes de pedir nada.', '¿Cuánto tardan en servirlo? Que nos casamos en junio.']}},
        'minimo_objetos_distintos': 40,
    }

if __name__ == '__main__':
    for n in (sys.argv[1:] or list(KITS)):
        escribir(n, KITS[n]())
