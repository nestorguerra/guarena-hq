# The four kits of the «servicios» family (technical backlog, I-02): a small-town bank branch, an office (insurance, gestoría…),
# a gym and a «casa de comidas» — written to data/kits/banco.json, oficina.json, gimnasio.json and restaurante.json from here,
# so that a rule is written once and read well. The objects they name are in tools/interiores/catalogo_servicios.py (and
# the hostelería catalogue, for the bottles, the chairs and the sanitaryware); the moodboards (Wikimedia Commons: page, author
# and licence, never the picture) in tools/interiores/moodboard_servicios.json.
#   python3 tools/interiores/catalogo_servicios.py && python3 tools/interiores/kits_servicios.py
import json, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
MOOD = json.load(open(os.path.join(ROOT, 'tools', 'interiores', 'moodboard_servicios.json')))

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
def vida(zona, variantes, en, **k): return E(zona, 'vida', variantes=variantes, en=en, **k)

def escribir(id, K):
    K['moodboard'] = [{'titulo': m['titulo'], 'url': m['url'], 'autor': m['autor'], 'licencia': m['licencia']} for m in MOOD[K.pop('_mood')]]
    json.dump(K, open(os.path.join(ROOT, 'data', 'kits', id + '.json'), 'w'), ensure_ascii=False, indent=1)
    print(id, len(K['objetos']), 'entradas')

# what lies on a desk, for the bank and the office
ESCRIT = ['puesto_gerencia', 'puesto_oficina', 'escritorio_oficina', 'escritorio_gerente']
SOBRE_ESCRIT = ['bloc_notas', 'taza_cafe', 'portalapices', 'calculadora', 'lampara_escritorio', 'bandeja_documentos', 'pila_carpetas', 'tarjetero_visitas', 'cuaderno_citas', 'grapadora', 'sello_tampon', 'portatil', 'bote_caramelos', 'planta_pequena']

# ================================================================== THE BANK
def banco():
    K = {
        'tipologia': 'sucursal_bancaria', 'nombre': 'Sucursal bancaria', '_mood': 'banco',
        'nota': 'La sucursal de un banco en un pueblo de las Vegas Altas (aquí, el «Banco del Valle», inventado): el cajero y el actualizador de libretas en el vestíbulo, pegados a la pared de la calle; la máquina de turnos y su pantalla; '
                'una sala con las mesas de dos o tres gestores (cada una con su sillón detrás y una silla de visita delante), la fila de sillas de espera y los folletos; al fondo, el mostrador de cajas con mampara de cristal, la puerta del personal '
                'a un lado, y detrás el puesto de los cajeros, el archivo y la puerta redonda de la cámara acorazada. La puerta de la calle en z = 0, el fondo en z = D; x de -W/2 a W/2.',
        'superficie': {'ancho': [7.5, 8.7], 'fondo': [11.1, 12.6], 'alto': 3.2},
        # (the counter: five windows of 1.2 m from the west wall; the staff's door in the stub of wall beyond them)
        'variables': {'zm': 'D-3.4', 'xs': '-W/2+6.0', 'zh': 'D-4.0'},
        'paso_libre': 0.9, 'pared': '#ecebe4', 'suelo': 'rock_tile_floor', 'suelo_color': '#c9c4b8',
        'puntos': {'dependiente': ['-W/2+1.2', 'zm+0.85'], 'mostrador': ['-W/2+1.2', 'zm-0.95']},
        'pedir': 'Consultar el saldo en ventanilla',
        'zonas': [
            Z('cajeros', ['-W/2', '0', '-0.95', '1.5']),
            Z('entrada', ['-0.95', '0', 'W/2', '1.5']),
            Z('gestores', ['-W/2', '2.2', 'W/2-2.1', 'zh']),
            Z('espera', ['W/2-2.0', '1.5', 'W/2', 'zh']),
            Z('ventanillas', ['-W/2', 'zm-0.55', 'xs', 'zm+0.55'], False),
            Z('personal', ['-W/2', 'zm+0.6', 'W/2', 'D'], False),
        ],
        'tabiques': [{'de': ['xs', 'zm'], 'a': ['W/2', 'zm'], 'puerta': [0.25, 1.0]}],
        'objetos': [
            # ---- the counter: its five windows, what lies on the customers' ledge, the staff's chairs
            E('ventanillas', 'modulos', 'ventanilla_modulo', eje='x', linea=['zm', '-W/2', 'xs'], mira='-z', obligatorio=True),
            sobre('ventanillas', 'boligrafo_cadena', ['ventanilla_modulo'], por_soporte=1, obligatorio=True),
            sobre('ventanillas', 'bote_caramelos', ['ventanilla_modulo'], cantidad=[1, 2]),
            sobre('ventanillas', 'folletos_pila', ['ventanilla_modulo'], cantidad=[1, 3]),
            sobre('ventanillas', 'datafono', ['ventanilla_modulo'], cantidad=[1, 2]),
            E('personal', 'fila', 'silla_oficina', eje='x', linea=['zm+0.92', '-W/2+0.6', 'xs-0.6'], cada=1.2, mira='-z'),
            # ---- the vestibule: the cash machines on the street wall, the queue ticket machine
            E('cajeros', 'contra_pared', 'cajero_automatico', pared='S', cantidad=[2, 2], obligatorio=True),
            E('cajeros', 'contra_pared', 'actualizador_libretas', pared='S', cantidad=[1, 1], obligatorio=True),
            E('cajeros', 'esquina', 'papelera', cantidad=[1, 1]),
            E('cajeros', 'techo', 'panel_led', cantidad=[1, 1], obligatorio=True),
            E('entrada', 'contra_pared', 'dispensador_turnos', pared='E', cantidad=[1, 1], obligatorio=True),
            E('entrada', 'contra_pared', 'dispensador_gel', pared='E', cantidad=[1, 1]),
            E('entrada', 'pared', 'cartel_horario_banco', pared='E', cantidad=[1, 1], obligatorio=True),
            E('entrada', 'pared', 'extintor', pared='E', cantidad=[1, 1], obligatorio=True),
            E('entrada', 'esquina', 'planta_grande', cantidad=[0, 1]),
            E('entrada', 'techo', 'panel_led', cantidad=[1, 1], obligatorio=True),
            E('entrada', 'techo', 'camara_seguridad', cantidad=[1, 1], obligatorio=True),
            # ---- the managers' desks (a client's chair in front, their armchair behind) and what lies on them
            E('gestores', 'conjunto', variantes=['puesto_gerencia', 'puesto_oficina'], sillas={'variantes': ['silla_visita'], 'n': [1, 1], 'lados': ['-z']}, cantidad=[2, 3], giro=[0, 180], obligatorio=True),
            E('gestores', 'conjunto', variantes=['escritorio_gerente', 'escritorio_oficina'], sillas={'variantes': ['silla_oficina'], 'n': [2, 2], 'lados': ['+z', '-z']}, cantidad=[0, 1], giro=[0, 180]),
            sobre('gestores', ['monitor_pc', 'monitor_pc_encendido'], ESCRIT, por_soporte=1, obligatorio=True),
            sobre('gestores', 'teclado', ESCRIT, por_soporte=1, obligatorio=True),
            sobre('gestores', 'raton_pc', ESCRIT, fraccion=[0.7, 1.0]),
            sobre('gestores', 'telefono_fijo', ESCRIT, fraccion=[0.6, 1.0]),
            vida('gestores', SOBRE_ESCRIT, ESCRIT, por_soporte=[2, 4], obligatorio=True),
            E('gestores', 'contra_pared', 'expositor_folletos', pared='W', cantidad=[1, 1], obligatorio=True),
            E('gestores', 'contra_pared', 'archivador_metalico', pared='W', cantidad=[0, 1]),
            E('gestores', 'pared', variantes=['cartel_hipotecas', 'cartel_ahorro'], pared='W', cantidad=[2, 2], todas=True, obligatorio=True),
            E('gestores', 'pared', 'expositor_folletos_pared', pared='W', cantidad=[0, 1]),
            E('gestores', 'pared', 'diploma_enmarcado', pared='W', cantidad=[0, 1]),
            E('gestores', 'esquina', 'planta_alta', cantidad=[0, 1]),
            E('gestores', 'esquina', 'papelera', cantidad=[0, 1]),
            E('gestores', 'techo', 'panel_led', por_m2=[0.11, 0.14], obligatorio=True),
            E('gestores', 'techo', 'detector_humo', cantidad=[1, 1]),
            # ---- the waiting area: chairs along the east wall, the turn display, a low table
            E('espera', 'contra_pared', 'silla_espera_fila', pared='E', cantidad=[2, 2], obligatorio=True),
            E('espera', 'pared', 'pantalla_turnos', pared='E', cantidad=[1, 1], obligatorio=True),
            E('espera', 'suelo_libre', 'mesa_baja', cantidad=[1, 1]),
            vida('espera', ['revista', 'periodico', 'bote_caramelos'], ['mesa_baja'], por_soporte=[1, 2]),
            E('espera', 'suelo_libre', 'sillon_espera', cantidad=[0, 1]),
            E('espera', 'esquina', 'planta_alta', cantidad=[0, 1]),
            E('espera', 'esquina', 'dispensador_agua', cantidad=[0, 1]),
            E('espera', 'techo', 'panel_led', por_m2=[0.1, 0.14], obligatorio=True),
            E('espera', 'techo', 'foco_empotrable', cantidad=[1, 1]),
            # ---- behind the counter: the strong-room door, the safe, the archive, the chairs' corner
            E('personal', 'pared', 'rotulo_banco', pared='N', cantidad=[1, 1], obligatorio=True),
            E('personal', 'pared', 'puerta_camara', pared='N', cantidad=[1, 1], obligatorio=True),
            E('personal', 'contra_pared', 'caja_fuerte', pared='N', cantidad=[1, 1], obligatorio=True),
            E('personal', 'contra_pared', 'archivador_metalico', pared='N', cantidad=[1, 2], obligatorio=True),
            E('personal', 'contra_pared', 'estanteria_archivadores', pared='W', cantidad=[1, 1], obligatorio=True),
            sobre('personal', ['archivador_azul', 'archivador_rojo', 'archivador_verde', 'archivador_negro', 'archivador_amarillo'], ['estanteria_archivadores'], relleno=[0.7, 0.9], todas=True, obligatorio=True),
            sobre('personal', ['caja_archivo', 'planta_pequena', 'bandeja_documentos'], ['archivador_metalico'], cantidad=[1, 3]),
            E('personal', 'contra_pared', 'fotocopiadora', pared='E', cantidad=[1, 1], obligatorio=True),
            sobre('personal', 'impresora_sobremesa', ['archivador_metalico'], cantidad=[0, 1]),
            E('personal', 'esquina', 'trituradora_papel', cantidad=[0, 1]),
            E('personal', 'esquina', 'papelera_reciclaje', cantidad=[0, 1]),
            E('personal', 'esquina', 'dispensador_agua', cantidad=[0, 1]),
            E('personal', 'pared', 'reloj_pared', pared='W', cantidad=[1, 1], obligatorio=True),
            E('personal', 'pared', 'aire_acondicionado', pared='W', cantidad=[1, 1]),
            E('personal', 'pared', 'senal_salida', pared='N', cantidad=[1, 1]),
            E('personal', 'techo', 'panel_led', cantidad=[2, 3], obligatorio=True),
            E('personal', 'techo', 'camara_seguridad', cantidad=[1, 1]),
        ],
        'iluminacion': {'fuentes': [6, 9], 'temperatura_k': [4000, 5000], 'dia': {'intensidad': 0.85}, 'noche': {'intensidad': 1.0}, 'minimo_lux_publico': 150},
        'ambiente': {
            'sonido': 'banco', 'horario_defecto': 'Mo-Fr 08:30-14:00; Th 16:30-18:30',
            'vida': ['la cola del turno', 'la libreta por actualizar', 'folletos de hipotecas', 'el cajero con su pantalla encendida'],
            'cerrado': 'persiana bajada y el cajero encendido en el vestíbulo',
            'clientela': {'maximo': 4, 'horas': [[8.5, 10, 0.3], [10, 12, 0.45], [12, 14, 0.3], [16.5, 18.5, 0.25]],
                          'frases': ['Llevo media hora con el turno en la mano.', 'Dicen que van a cerrar la oficina de la plaza.', 'Vengo a actualizar la libreta, como cada mes.', '¿Tú sabes cómo va eso de la banca por internet?', 'Mi nieto me dice que ya nadie viene al banco.']},
        },
        'minimo_objetos_distintos': 40,
    }
    escribir('banco', K)

# ================================================================== THE OFFICE (an insurance agency, a gestoría…)
def oficina():
    K = {
        'tipologia': 'oficina', 'nombre': 'Oficina (seguros, gestoría)', '_mood': 'oficina',
        'nota': 'La oficina de una aseguradora o gestoría de pueblo: sillas de espera bajo la ventana, el mostrador de recepción a la derecha con su archivador, detrás los escritorios con ordenador y una silla de visita delante, '
                'el archivo con estanterías de archivadores y la fotocopiadora contra la pared del fondo izquierdo, la sala de reuniones con su mesa al fondo derecho, el dispensador de agua, plantas, diplomas y el cartel de la compañía. '
                'La puerta de la calle en z = 0, el fondo en z = D.',
        'superficie': {'ancho': [6.9, 8.1], 'fondo': [11.7, 12.9], 'alto': 2.9},
        'variables': {'zr': '3.0', 'xr': 'W/2-3.6', 'zrm': 'D-3.4', 'xm': 'W/2-3.0'},
        'paso_libre': 0.9, 'pared': '#efece4', 'suelo': 'long_white_tiles', 'suelo_color': '#d4cfc4',
        'puntos': {'dependiente': ['W/2-1.8', 'zr+0.9']},
        'zonas': [
            Z('espera', ['-W/2', '0', '-0.95', '1.6']),
            Z('entrada', ['-0.95', '0', 'W/2', '1.6']),
            Z('sala', ['-W/2', '1.6', 'W/2', 'zr-0.55']),
            Z('mostrador', ['xr', 'zr-0.55', 'W/2', 'zr+0.55'], False),
            Z('tras_mostrador', ['xr', 'zr+0.6', 'W/2', 'zr+1.5'], False),
            Z('despachos', ['-W/2+1.7', '5.5', 'W/2', 'zrm-0.1']),
            Z('despachos2', ['-W/2+1.7', 'zrm', 'xm', 'D']),
            Z('archivo', ['-W/2', '4.1', '-W/2+1.1', 'D'], False),
            Z('reunion', ['xm', 'zrm', 'W/2', 'D']),
        ],
        'tabiques': [
            {'de': ['xm', 'zrm'], 'a': ['xm', 'D']},
            {'de': ['xm', 'zrm'], 'a': ['W/2', 'zrm'], 'puerta': [0.5, 1.0]},
        ],
        'objetos': [
            # ---- the reception counter and the clerk's side
            E('mostrador', 'modulos', 'mostrador_recepcion_modulo', eje='x', linea=['zr', 'xr', 'W/2'], mira='-z', obligatorio=True),
            sobre('mostrador', ['bote_caramelos', 'tarjetero_visitas', 'folletos_pila', 'bloc_notas'], ['mostrador_recepcion_modulo'], cantidad=[2, 4], obligatorio=True),
            sobre('mostrador', 'datafono', ['mostrador_recepcion_modulo'], cantidad=[0, 1]),
            E('tras_mostrador', 'contra_pared', 'archivador_metalico', pared='E', cantidad=[1, 1], obligatorio=True),
            sobre('tras_mostrador', ['impresora_sobremesa', 'caja_archivo', 'planta_pequena'], ['archivador_metalico'], cantidad=[1, 2], obligatorio=True),
            E('tras_mostrador', 'fila', 'silla_oficina', eje='x', linea=['zr+0.95', 'xr+0.6', 'W/2-0.6'], cada=1.2, mira='-z'),
            E('tras_mostrador', 'esquina', 'papelera_reciclaje', cantidad=[0, 1]),
            E('tras_mostrador', 'techo', 'panel_led', cantidad=[1, 1], obligatorio=True),
            # ---- the waiting corner under the window and the entrance
            E('espera', 'contra_pared', 'silla_espera_fila', pared='S', cantidad=[1, 1], obligatorio=True),
            E('espera', 'suelo_libre', 'mesa_baja', cantidad=[0, 1]),
            vida('espera', ['revista', 'periodico', 'bote_caramelos'], ['mesa_baja'], por_soporte=[1, 2]),
            E('espera', 'esquina', 'planta_alta', cantidad=[0, 1]),
            E('espera', 'esquina', 'perchero', cantidad=[0, 1]),
            E('espera', 'esquina', 'paraguero', cantidad=[0, 1]),
            E('espera', 'techo', 'foco_empotrable', cantidad=[1, 1], obligatorio=True),
            E('entrada', 'contra_pared', 'dispensador_agua', pared='E', cantidad=[1, 1], obligatorio=True),
            E('entrada', 'pared', 'cartel_horario_oficina', pared='E', cantidad=[1, 1], obligatorio=True),
            E('entrada', 'pared', 'extintor', pared='E', cantidad=[1, 1], obligatorio=True),
            E('entrada', 'esquina', 'papelera', cantidad=[0, 1]),
            E('entrada', 'techo', 'panel_led', cantidad=[1, 1], obligatorio=True),
            E('entrada', 'techo', 'detector_humo', cantidad=[1, 1]),
            E('sala', 'pared', 'cartel_aseguradora', pared='W', cantidad=[1, 1], obligatorio=True),
            E('sala', 'pared', 'reloj_pared', pared='W', cantidad=[0, 1]),
            E('sala', 'pared', variantes=['tablon_corcho', 'diploma_enmarcado'], pared='W', cantidad=[0, 1]),
            E('sala', 'esquina', 'sillon_espera', cantidad=[0, 1]),
            E('sala', 'techo', 'regleta_led_techo', cantidad=[1, 2], obligatorio=True),
            E('sala', 'techo', 'camara_seguridad', cantidad=[0, 1]),
            # ---- the desks: a clerk's chair behind, a visitor's in front, a screen, a keyboard, papers
            E('despachos', 'conjunto', variantes=['puesto_oficina', 'puesto_gerencia'], sillas={'variantes': ['silla_visita'], 'n': [1, 1], 'lados': ['-z']}, cantidad=[1, 2], giro=[0, 180], obligatorio=True),
            E('despachos2', 'conjunto', 'puesto_oficina', sillas={'variantes': ['silla_visita'], 'n': [1, 1], 'lados': ['-z']}, cantidad=[1, 1], giro=[0, 180], obligatorio=True),
            E('despachos', 'conjunto', variantes=['escritorio_oficina', 'escritorio_gerente'], sillas={'variantes': ['silla_oficina'], 'n': [2, 2], 'lados': ['+z', '-z']}, cantidad=[0, 1], giro=[0, 180]),
            sobre('despachos', ['monitor_pc', 'monitor_pc_encendido'], ESCRIT, por_soporte=1, obligatorio=True),
            sobre('despachos', 'teclado', ESCRIT, por_soporte=1, obligatorio=True),
            sobre('despachos', 'raton_pc', ESCRIT, fraccion=[0.7, 1.0]),
            sobre('despachos', 'telefono_fijo', ESCRIT, por_soporte=1),
            vida('despachos', SOBRE_ESCRIT, ESCRIT, por_soporte=[2, 4]),
            sobre('despachos2', ['monitor_pc_encendido', 'teclado', 'telefono_fijo', 'raton_pc'], ESCRIT, por_soporte=4),
            E('despachos', 'techo', 'panel_led', por_m2=[0.12, 0.16], obligatorio=True),
            E('despachos2', 'pared', variantes=['diploma_enmarcado', 'tablon_corcho'], pared='N', cantidad=[1, 2], todas=True, obligatorio=True),
            E('despachos2', 'pared', 'aire_acondicionado', pared='N', cantidad=[0, 1]),
            E('despachos2', 'pared', 'calendario_pared', pared='N', cantidad=[0, 1]),
            E('despachos2', 'esquina', 'planta_alta', cantidad=[0, 1]),
            E('despachos2', 'techo', 'panel_led', cantidad=[1, 1], obligatorio=True),
            # ---- the archive along the west wall
            E('archivo', 'contra_pared', 'estanteria_archivadores', pared='W', cantidad=[2, 2], obligatorio=True),
            sobre('archivo', ['archivador_azul', 'archivador_rojo', 'archivador_verde', 'archivador_negro', 'archivador_amarillo'], ['estanteria_archivadores'], relleno=[0.7, 0.92], todas=True, obligatorio=True),
            E('archivo', 'contra_pared', 'fotocopiadora', pared='W', cantidad=[1, 1], obligatorio=True),
            E('archivo', 'contra_pared', 'archivador_metalico', pared='W', cantidad=[1, 2], obligatorio=True),
            E('archivo', 'contra_pared', 'armario_oficina', pared='W', cantidad=[0, 1]),
            sobre('archivo', ['caja_archivo', 'impresora_sobremesa', 'pila_carpetas'], ['archivador_metalico'], cantidad=[1, 3]),
            E('archivo', 'contra_pared', 'trituradora_papel', pared='W', cantidad=[0, 1]),
            E('archivo', 'techo', 'regleta_led_techo', cantidad=[1, 1], obligatorio=True),
            # ---- the meeting room
            E('reunion', 'conjunto', 'mesa_reunion', sillas={'variantes': ['silla_oficina', 'silla_visita'], 'n': [4, 4]}, cantidad=[1, 1], giro=[90], obligatorio=True),
            sobre('reunion', ['portatil', 'bloc_notas', 'taza_cafe', 'pila_carpetas', 'bote_caramelos'], ['mesa_reunion'], cantidad=[3, 5], obligatorio=True),
            E('reunion', 'pared', 'pizarra_blanca', pared='E', cantidad=[1, 1], obligatorio=True),
            E('reunion', 'pared', 'cartel_aseguradora', pared='N', cantidad=[0, 1]),
            E('reunion', 'pared', 'senal_salida', pared='N', cantidad=[1, 1]),
            E('reunion', 'esquina', 'planta_alta', cantidad=[0, 1]),
            E('reunion', 'techo', 'panel_led', cantidad=[1, 2], obligatorio=True),
        ],
        'iluminacion': {'fuentes': [6, 9], 'temperatura_k': [4000, 5000], 'dia': {'intensidad': 0.85}, 'noche': {'intensidad': 1.0}, 'minimo_lux_publico': 150},
        'ambiente': {
            'sonido': 'oficina', 'horario_defecto': 'Mo-Fr 09:00-14:00,16:30-19:00',
            'vida': ['la fotocopiadora', 'carpetas por archivar', 'el teléfono sonando', 'el dispensador de agua'],
            'cerrado': 'persiana bajada y la luz del fondo encendida',
            'clientela': {'maximo': 3, 'horas': [[9, 11, 0.4], [11, 14, 0.5], [16.5, 19, 0.4]],
                          'frases': ['Vengo por lo de la declaración de la renta.', 'Me han dicho que traiga el recibo del seguro.', '¿Esto es para el coche o para la casa?', 'Siempre hay que traer una fotocopia más.']},
        },
        'minimo_objetos_distintos': 40,
    }
    escribir('oficina', K)

# ================================================================== THE GYM
TRAIN = {'type': 'train', 'label': 'Entrenar una hora'}
MANCUERNAS = ['mancuerna_%dkg' % n for n in (2, 4, 6, 8, 10, 12, 14, 16, 20, 24, 28, 32, 36, 40)]
PESAS_RUSAS = ['pesa_rusa_%dkg' % n for n in (4, 8, 12, 16, 20, 24)]
BALONES = ['balon_medicinal_%dkg' % n for n in (3, 5, 8)]
DISCOS = ['disco_1_25kg', 'disco_2_5kg', 'disco_5kg', 'disco_10kg', 'disco_15kg', 'disco_20kg']
def gimnasio():
    K = {
        'tipologia': 'gimnasio', 'nombre': 'Gimnasio', '_mood': 'gimnasio',
        'nota': 'El gimnasio de un pueblo de las Vegas Altas en una nave de techo alto: la recepción y la nevera de bebidas junto a la puerta; las cintas, elípticas y bicicletas en fila contra la pared de la izquierda, de cara a las teles; las máquinas de pesas '
                'contra la de la derecha; en el centro el suelo para esterillas, pelotas y el saco de boxeo colgado del techo; al fondo el peso libre (soportes de mancuernas, de pesas rusas, rack de sentadilla, bancos, discos) bajo un gran espejo; y el vestuario, '
                'con taquillas, duchas y un banco, tras un tabique. La puerta de la calle en z = 0, el fondo en z = D; x de -W/2 a W/2.',
        'superficie': {'ancho': [8.7, 10.2], 'fondo': [12.3, 14.7], 'alto': 3.4},
        'variables': {'zv': 'D-3.8', 'xv': '-W/2+3.8', 'zc': 'D-4.2'},
        'paso_libre': 0.9, 'pared': '#e6e9eb', 'suelo': 'concrete_floor_damaged_01', 'suelo_color': '#b4b8bb',
        'puntos': {'dependiente': ['W/2-0.55', '3.3'], 'mostrador': ['W/2-2.7', '3.3']},
        'pedir': 'Recepción: cuota, bebidas y entrenar',
        'zonas': [
            Z('entrada', ['-W/2', '0', 'W/2-2.3', '2.0']),
            Z('entrada_e', ['W/2-2.3', '0', 'W/2', '2.0']),
            Z('recepcion', ['W/2-2.2', '2.1', 'W/2-1.0', '4.5'], False),
            Z('tras_recepcion', ['W/2-1.0', '2.1', 'W/2', '4.5'], False),
            Z('cardio', ['-W/2', '2.1', '-W/2+2.2', 'zc']),
            Z('boxeo', ['-W/2+0.5', '0.3', '-W/2+2.4', '2.0']),
            Z('centro', ['-W/2+2.3', '2.1', 'W/2-2.5', 'zc']),
            Z('maquinas', ['W/2-2.4', '4.9', 'W/2', 'zc']),
            Z('pesolibre', ['-W/2+3.9', 'D-4.0', 'W/2', 'D']),
            Z('vestuario', ['-W/2', 'zv', 'xv', 'D']),
        ],
        'tabiques': [
            {'de': ['-W/2', 'zv'], 'a': ['xv', 'zv'], 'puerta': [2.5, 1.0]},
            {'de': ['xv', 'zv'], 'a': ['xv', 'D']},
        ],
        'objetos': [
            # ---- the boxing bag in the front corner, by the window, laid out first (it hangs where nothing else may stand)
            E('boxeo', 'techo', 'saco_boxeo', cantidad=[1, 1], obligatorio=True),
            E('boxeo', 'suelo_libre', 'guantes_boxeo', cantidad=[0, 1]),
            E('boxeo', 'suelo_libre', 'colchoneta', cantidad=[0, 1]),
            # ---- the reception (two modules along the east wall) and the drinks fridge by the door
            E('recepcion', 'modulos', 'mostrador_gimnasio_modulo', eje='z', linea=['W/2-1.6', '2.1', '4.5'], mira='-x', obligatorio=True),
            sobre('recepcion', ['toalla_doblada', 'bidon_agua', 'bote_caramelos', 'bote_proteina_choco', 'bote_proteina_vainilla', 'bote_proteina_fresa', 'datafono'], ['mostrador_gimnasio_modulo'], cantidad=[3, 5], obligatorio=True),
            E('tras_recepcion', 'suelo_libre', 'silla_oficina', cantidad=[1, 1]),
            E('tras_recepcion', 'pared', 'cartel_clases', pared='E', cantidad=[1, 1], obligatorio=True),
            E('tras_recepcion', 'pared', 'cartel_tarifas', pared='E', cantidad=[1, 1], obligatorio=True),
            E('tras_recepcion', 'pared', 'reloj_pared', pared='E', cantidad=[0, 1]),
            E('tras_recepcion', 'techo', 'luminaria_campana', cantidad=[1, 1], obligatorio=True),
            E('entrada_e', 'contra_pared', 'nevera_bebidas', pared='E', cantidad=[1, 1], obligatorio=True, vende=['agua', 'isotonica']),
            E('entrada_e', 'contra_pared', 'estante_suplementos', pared='E', cantidad=[0, 1]),
            sobre('entrada_e', ['bote_proteina_choco', 'bote_proteina_vainilla', 'bote_proteina_fresa'], ['estante_suplementos'], relleno=[0.6, 0.9], todas=True),
            E('entrada_e', 'esquina', 'planta_grande', cantidad=[0, 1]),
            E('entrada', 'pared', 'fuente_agua', pared='W', cantidad=[1, 1], obligatorio=True),
            E('entrada', 'pared', 'cartel_normas_gimnasio', pared='W', cantidad=[1, 1], obligatorio=True),
            E('entrada', 'pared', 'espejo_gimnasio_alto', pared='W', cantidad=[0, 1]),
            E('entrada', 'pared', 'perchero_pared', pared='W', cantidad=[0, 1]),
            E('entrada', 'esquina', 'bascula_gimnasio', cantidad=[0, 1]),
            E('entrada', 'esquina', 'papelera', cantidad=[0, 1]),
            E('entrada', 'techo', 'luminaria_campana', cantidad=[1, 1], obligatorio=True),
            E('entrada', 'techo', 'camara_seguridad', cantidad=[1, 1]),
            # ---- cardio along the west wall, facing it (and the screens)
            E('cardio', 'contra_pared', 'cinta_correr', pared='W', cantidad=[3, 3], obligatorio=True, interaccion=TRAIN),
            E('cardio', 'contra_pared', 'eliptica', pared='W', cantidad=[1, 1], obligatorio=True, interaccion=TRAIN),
            E('cardio', 'contra_pared', 'bici_estatica', pared='W', cantidad=[1, 1], obligatorio=True, interaccion=TRAIN),
            E('cardio', 'contra_pared', 'bici_ciclo_indoor', pared='W', cantidad=[1, 1], obligatorio=True, interaccion=TRAIN),
            E('cardio', 'contra_pared', variantes=['cinta_correr', 'bici_ciclo_indoor', 'eliptica', 'bici_estatica'], pared='W', cantidad=[0, 2], interaccion=TRAIN),
            E('cardio', 'pared', 'tv_gimnasio', pared='W', cantidad=[1, 2], obligatorio=True),
            E('cardio', 'pared', 'altavoz_pared', pared='W', cantidad=[0, 2]),
            E('cardio', 'techo', 'luminaria_campana', cantidad=[1, 2], obligatorio=True),
            # ---- strength machines along the east wall
            E('maquinas', 'contra_pared', 'multiestacion', pared='E', cantidad=[1, 1], obligatorio=True, interaccion=TRAIN),
            E('maquinas', 'contra_pared', 'prensa_piernas', pared='E', cantidad=[1, 1], obligatorio=True, interaccion=TRAIN),
            E('maquinas', 'contra_pared', 'polea_alta', pared='E', cantidad=[0, 1], interaccion=TRAIN),
            E('maquinas', 'contra_pared', 'pec_deck', pared='E', cantidad=[0, 1], interaccion=TRAIN),
            E('maquinas', 'contra_pared', 'remo_maquina', pared='E', cantidad=[0, 1], interaccion=TRAIN),
            E('maquinas', 'techo', 'luminaria_campana', cantidad=[1, 2], obligatorio=True),
            # ---- the middle: the frame for pull-ups, mats and small gear
            E('centro', 'suelo_libre', 'estructura_dominadas', cantidad=[1, 1], obligatorio=True, interaccion=TRAIN),
            E('centro', 'suelo_libre', 'colchoneta', cantidad=[2, 4], obligatorio=True),
            E('centro', 'suelo_libre', variantes=['pera_boxeo', 'pelota_pilates', 'media_pelota_equilibrio', 'esterilla_yoga', 'step_aerobic', 'rodillo_espuma', 'comba', 'gomas_elasticas', 'bolsa_deporte', 'guantes_boxeo', 'bidon_agua', 'bascula_gimnasio'], cantidad=[11, 12], todas=True, obligatorio=True),
            E('centro', 'techo', 'luminaria_campana', por_m2=[0.05, 0.07], obligatorio=True),
            # ---- free weights at the back, under a big mirror
            E('pesolibre', 'contra_pared', 'soporte_mancuernas', pared='N', cantidad=[1, 1], obligatorio=True),
            E('pesolibre', 'contra_pared', 'soporte_kettlebells', pared='N', cantidad=[1, 1], obligatorio=True),
            E('pesolibre', 'contra_pared', 'soporte_balones', pared='N', cantidad=[0, 1]),
            E('pesolibre', 'contra_pared', 'soporte_mancuernas', pared='N', cantidad=[0, 1]),
            sobre('pesolibre', MANCUERNAS, ['soporte_mancuernas'], relleno=[0.96, 1.0], todas=True, obligatorio=True),
            sobre('pesolibre', PESAS_RUSAS, ['soporte_kettlebells'], relleno=[0.9, 1.0], todas=True, obligatorio=True),
            sobre('pesolibre', BALONES, ['soporte_balones'], relleno=[0.7, 0.95], todas=True),
            E('pesolibre', 'pared', 'espejo_gimnasio_grande', pared='N', cantidad=[1, 2], obligatorio=True),
            E('pesolibre', 'pared', variantes=['cartel_sentadilla', 'cartel_press'], pared='N', cantidad=[0, 2], todas=True),
            E('pesolibre', 'suelo_libre', 'rack_sentadilla', cantidad=[1, 1], obligatorio=True, interaccion=TRAIN),
            E('pesolibre', 'suelo_libre', variantes=['banco_plano', 'banco_inclinado', 'banco_regulable', 'banco_abdominales'], cantidad=[3, 4], todas=True, obligatorio=True),
            E('pesolibre', 'suelo_libre', 'arbol_discos', cantidad=[0, 1]),
            E('pesolibre', 'suelo_libre', variantes=['barra_olimpica', 'barra_z'], cantidad=[1, 2], todas=True),
            E('pesolibre', 'suelo_libre', variantes=DISCOS, cantidad=[5, 6], todas=True, obligatorio=True),
            E('pesolibre', 'esquina', 'ventilador_pie', cantidad=[0, 1]),
            E('pesolibre', 'techo', 'luminaria_campana', cantidad=[2, 2], obligatorio=True),
            # ---- the changing room
            E('vestuario', 'contra_pared', variantes=['taquilla_metalica', 'taquilla_doble', 'taquilla_media'], pared='W', llenar=True, obligatorio=True),
            sobre('vestuario', ['toalla_doblada', 'bolsa_deporte'], ['taquilla_doble', 'taquilla_metalica'], cantidad=[0, 2]),
            E('vestuario', 'contra_pared', 'ducha_cabina', pared='N', cantidad=[2, 2], obligatorio=True),
            E('vestuario', 'suelo_libre', 'banco_vestuario', cantidad=[1, 2], obligatorio=True),
            sobre('vestuario', ['toalla_doblada', 'bolsa_deporte', 'bidon_agua'], ['banco_vestuario'], cantidad=[1, 3]),
            E('vestuario', 'pared', 'lavabo', pared='E', cantidad=[1, 1], obligatorio=True),
            E('vestuario', 'pared', 'espejo_aseo', pared='E', cantidad=[1, 1], obligatorio=True, sobre_de='lavabo'),
            E('vestuario', 'pared', 'dispensador_jabon', pared='E', cantidad=[1, 1]),
            E('vestuario', 'pared', 'secador_pelo_pared', pared='E', cantidad=[1, 1]),
            E('vestuario', 'pared', 'dispensador_toallas', pared='E', cantidad=[0, 1]),
            E('vestuario', 'pared', 'ducha_abierta', pared='N', cantidad=[0, 1]),
            E('vestuario', 'esquina', 'papelera', cantidad=[0, 1]),
            E('vestuario', 'techo', 'panel_led', cantidad=[2, 2], obligatorio=True),
        ],
        'iluminacion': {'fuentes': [6, 9], 'temperatura_k': [4000, 5000], 'dia': {'intensidad': 0.85}, 'noche': {'intensidad': 1.0}, 'minimo_lux_publico': 150},
        'ambiente': {
            'sonido': 'gimnasio', 'horario_defecto': 'Mo-Su 07:00-22:30',
            'vida': ['las cintas en marcha', 'una toalla sobre el banco', 'discos sin recoger', 'la tele con el fútbol'],
            'cerrado': 'la reja bajada y las luces del fondo encendidas',
        },
        'minimo_objetos_distintos': 80,
    }
    escribir('gimnasio', K)

# ================================================================== THE «CASA DE COMIDAS»
MESAS_R = ['mesa_mantel_blanca', 'mesa_mantel_cuadros', 'mesa_cuadrada_mantel', 'mesa_redonda_mantel']
SILLAS_R = ['silla_anea', 'silla_comedor_tapizada', 'silla_madera']
BOTELLAS_BAR = ['botella_whisky', 'botella_ron', 'botella_ginebra', 'botella_anis', 'botella_brandy', 'botella_vino_tinto', 'botella_vino_blanco', 'botella_vermut', 'botella_licor_hierbas', 'botella_pacharan',
                'botella_agua_mineral', 'botella_refresco_cola', 'botella_refresco_naranja', 'botella_cerveza', 'botella_mosto']
def restaurante():
    mesas = lambda zona: [
        sobre(zona, ['cubiertos_servicio', 'plato_llano', 'copa_vino', 'vaso_agua', 'servilleta_doblada'], MESAS_R, por_soporte=[4, 6], obligatorio=True),
        sobre(zona, 'cesta_pan', MESAS_R, fraccion=[0.6, 0.9]),
        sobre(zona, ['botella_vino_tinto', 'botella_vino_blanco', 'botella_agua_mineral', 'jarra_agua'], MESAS_R, fraccion=[0.6, 0.9], obligatorio=True),
        sobre(zona, ['salero_pimentero', 'aceitera_vinagrera', 'florero_mesa'], MESAS_R, por_soporte=[1, 2], obligatorio=True),
        vida(zona, ['plato_hondo', 'plato_postre', 'plato_tortilla', 'plato_jamon', 'cuenco_aceitunas', 'periodico', 'carta_menu'], MESAS_R, fraccion=[0.3, 0.6], por_soporte=[1, 2]),
    ]
    K = {
        'tipologia': 'restaurante', 'nombre': 'Casa de comidas', '_mood': 'restaurante',
        'nota': 'La casa de comidas de un pueblo de las Vegas Altas, con su menú del día: una barra pequeña a la entrada (taburetes, caja, vitrina de tapas, el jamón colgado y los botelleros detrás), el comedor con las mesas puestas '
                '(mantel, platos, cubiertos, copas, cesta de pan, botella de vino, servilletas) y sillas de anea, la pizarra del menú, los cuadros y la cabeza de ciervo, el aseo, y la cocina tras un tabique con su fogón, campana, mesas de acero, fregadero y neveras. '
                'La puerta de la calle en z = 0, el fondo en z = D; x de -W/2 a W/2.',
        'superficie': {'ancho': [8.4, 9.6], 'fondo': [12.0, 13.8], 'alto': 3.3},
        'variables': {'xc': 'W/2-1.95', 'z0': '1.7', 'z1': '5.3', 'zk': 'D-3.6', 'za': 'D-6.0', 'xa': '-W/2+2.1'},
        'paso_libre': 0.9, 'pared': '#efe3c8', 'suelo': 'floor_tiles_06', 'suelo_color': '#cdb592',
        'puntos': {'dependiente': ['xc+0.75', '(z0+z1)/2'], 'mostrador': ['xc-0.95', '(z0+z1)/2']},
        'pedir': 'Pedir en la barra',
        'zonas': [
            Z('entrada', ['-W/2', '0', 'xc-0.4', '1.2']),
            Z('barra', ['xc-0.3', 'z0', 'xc+0.3', 'z1'], False),
            Z('frente_barra', ['xc-1.3', 'z0', 'xc-0.33', 'z1']),
            Z('trasbarra', ['xc+0.33', 'z0', 'W/2', 'z1+0.2'], False),
            Z('comedor', ['-W/2', '1.2', 'xc-1.35', 'za-0.1']),
            Z('comedor2', ['-W/2+2.2', 'za-0.1', 'W/2', 'zk-0.1']),
            Z('aseo', ['-W/2', 'za', 'xa', 'zk']),
            Z('cocina', ['-W/2', 'zk', 'W/2', 'D'], False),
        ],
        'tabiques': [
            {'de': ['-W/2', 'zk'], 'a': ['W/2', 'zk'], 'puerta': ['W-2.4', 1.0]},
            {'de': ['xa', 'za'], 'a': ['xa', 'zk']},
            {'de': ['-W/2', 'za'], 'a': ['xa', 'za'], 'puerta': [0.55, 1.0]},
        ],
        'libres': [{'rect': ['xc-1.3', '(z0+z1)/2-0.55', 'xc-0.3', '(z0+z1)/2+0.55'], 'nota': 'el sitio para pedir en la barra, junto a la caja: sin taburetes'}],
        'objetos': [
            # ---- the little bar at the entrance
            E('barra', 'modulos', 'barra_modulo', eje='z', linea=['xc', 'z0', 'z1'], mira='-x', obligatorio=True, vende=['bocadillo', 'agua']),
            sobre('barra', 'caja_registradora', ['barra_modulo'], cantidad=[1, 1], obligatorio=True),
            sobre('barra', 'vitrina_tapas', ['barra_modulo'], cantidad=[0, 1]),
            sobre('barra', 'tirador_cerveza', ['barra_modulo'], cantidad=[1, 1], obligatorio=True),
            sobre('barra', 'servilletero', ['barra_modulo'], por_m=[0.3, 0.5], obligatorio=True),
            sobre('barra', 'palillero', ['barra_modulo'], cantidad=[1, 2]),
            sobre('barra', 'datafono', ['barra_modulo'], cantidad=[1, 1]),
            sobre('barra', 'bote_propinas', ['barra_modulo'], cantidad=[0, 1]),
            sobre('barra', 'jamonero', ['barra_modulo'], cantidad=[0, 1]),
            vida('barra', ['plato_tortilla', 'cuenco_aceitunas', 'plato_jamon', 'vaso_cana', 'copa_vino', 'taza_cafe', 'servilleta_arrugada'], ['barra_modulo'], fraccion=[0.5, 0.8], por_soporte=[1, 3]),
            E('frente_barra', 'fila', 'taburete_alto', eje='z', linea=['xc-0.68', 'z0+0.3', 'z1-0.3'], cada=0.6, mira='+x', obligatorio=True),
            E('trasbarra', 'contra_pared', 'nevera_bebidas', pared='E', cantidad=[1, 1], obligatorio=True),
            E('trasbarra', 'contra_pared', 'mueble_trasbarra', pared='E', llenar=True, obligatorio=True),
            E('trasbarra', 'pared', 'botellero_pared', pared='E', cada=1.25, obligatorio=True),
            sobre('trasbarra', 'cafetera_industrial', ['mueble_trasbarra'], cantidad=[1, 1], obligatorio=True),
            sobre('trasbarra', ['tostadora', 'exprimidor', 'microondas'], ['mueble_trasbarra'], cantidad=[0, 2]),
            sobre('trasbarra', BOTELLAS_BAR, ['botellero_pared'], relleno=[0.7, 0.9], todas=True, obligatorio=True),
            E('barra', 'techo', 'lampara_colgante', por_m=[0.3, 0.4], obligatorio=True),
            E('barra', 'techo', 'jamon_colgado', por_m=[0.3, 0.5], obligatorio=True),
            # ---- the entrance
            E('entrada', 'contra_pared', 'caballete_menu', pared='W', cantidad=[1, 1], obligatorio=True),
            E('entrada', 'esquina', 'perchero', cantidad=[0, 1]),
            E('entrada', 'esquina', 'planta_grande', cantidad=[0, 1]),
            E('entrada', 'esquina', 'paraguero', cantidad=[0, 1]),
            E('entrada', 'techo', 'lampara_colgante', cantidad=[1, 1], obligatorio=True),
            # ---- the dining room: tables laid, chairs of rush and upholstery, the board of the menu
            E('comedor', 'conjunto', variantes=MESAS_R, sillas={'variantes': SILLAS_R, 'n': [2, 4]}, por_m2=[0.1, 0.15], obligatorio=True),
            *mesas('comedor'),
            E('comedor', 'contra_pared', 'aparador_comedor', pared='W', cantidad=[0, 1]),
            sobre('comedor', ['plato_llano', 'copa_vino', 'botella_vino_tinto', 'florero_mesa', 'cesta_pan'], ['aparador_comedor'], cantidad=[0, 4]),
            E('comedor', 'pared', 'rotulo_restaurante', pared='W', cantidad=[1, 1], obligatorio=True),
            E('comedor', 'pared', 'pizarra_menu_pared', pared='W', cantidad=[1, 1], obligatorio=True),
            E('comedor', 'pared', variantes=['cuadro_paisaje', 'cuadro_foto_antigua', 'cartel_toros'], pared='W', cantidad=[2, 3], todas=True, obligatorio=True),
            E('comedor', 'pared', 'cabeza_ciervo', pared='W', cantidad=[0, 1]),
            E('comedor', 'pared', 'lampara_aplique', pared='W', cantidad=[1, 2]),
            E('comedor', 'pared', 'reloj_pared', pared='W', cantidad=[0, 1]),
            E('comedor', 'esquina', 'planta_grande', cantidad=[0, 1]),
            E('comedor', 'techo', 'lampara_colgante', por_m2=[0.07, 0.1], obligatorio=True),
            E('comedor2', 'conjunto', variantes=MESAS_R, sillas={'variantes': SILLAS_R, 'n': [2, 4]}, por_m2=[0.1, 0.16], obligatorio=True),
            *mesas('comedor2'),
            E('comedor2', 'techo', 'lampara_colgante', cantidad=[2, 2], obligatorio=True),
            # ---- the toilets
            E('aseo', 'contra_pared', 'inodoro', pared='N', cantidad=[1, 1], obligatorio=True),
            E('aseo', 'esquina', 'escobilla', cantidad=[0, 1]),
            E('aseo', 'pared', 'lavabo', pared='W', cantidad=[1, 1], obligatorio=True),
            E('aseo', 'pared', 'espejo_aseo', pared='W', cantidad=[1, 1], obligatorio=True, sobre_de='lavabo'),
            E('aseo', 'pared', 'dispensador_jabon', pared='W', cantidad=[1, 1], obligatorio=True),
            E('aseo', 'pared', 'secamanos', pared='E', cantidad=[1, 1], obligatorio=True),
            E('aseo', 'pared', 'portarrollos', pared='N', cantidad=[1, 1], obligatorio=True),
            E('aseo', 'esquina', 'papelera', cantidad=[0, 1]),
            E('aseo', 'techo', 'lampara_colgante', cantidad=[1, 1], obligatorio=True),
            # ---- the kitchen
            E('cocina', 'contra_pared', 'cocina_fuegos', pared='N', cantidad=[1, 1], obligatorio=True),
            E('cocina', 'pared', 'campana_extractora', pared='N', cantidad=[1, 1], obligatorio=True, sobre_de='cocina_fuegos'),
            sobre('cocina', ['olla_grande', 'cazuela_barro', 'sarten_grande', 'cacerola'], ['cocina_fuegos'], cantidad=[1, 4], obligatorio=True),
            E('cocina', 'contra_pared', 'fregadero_acero', pared='W', cantidad=[1, 1], obligatorio=True),
            E('cocina', 'contra_pared', 'nevera_industrial', pared='E', cantidad=[1, 1], obligatorio=True),
            E('cocina', 'contra_pared', 'arcon_congelador', pared='E', cantidad=[0, 1]),
            E('cocina', 'contra_pared', 'lavavajillas', pared='W', cantidad=[0, 1]),
            E('cocina', 'contra_pared', 'mesa_acero', pared='W', cantidad=[0, 1]),
            E('cocina', 'suelo_libre', 'mesa_acero', cantidad=[1, 1], obligatorio=True),
            sobre('cocina', ['freidora', 'plancha_cocina', 'tabla_cortar', 'garrafa_aceite', 'olla_grande', 'cazuela_barro'], ['mesa_acero'], cantidad=[2, 4], obligatorio=True),
            sobre('cocina', ['tabla_cortar', 'caja_verduras', 'garrafa_aceite'], ['arcon_congelador'], cantidad=[0, 2]),
            E('cocina', 'pared', 'estante_ollas', pared='W', cantidad=[0, 1]),
            E('cocina', 'contra_pared', 'estanteria_metalica', pared='N', cantidad=[0, 1]),
            sobre('cocina', ['caja_carton', 'caja_vasos', 'garrafa_aceite', 'saco_cafe'], ['estanteria_metalica'], relleno=[0.6, 0.9], todas=True),
            E('cocina', 'suelo_libre', variantes=['caja_verduras', 'saco_patatas', 'carro_servicio'], cantidad=[2, 3], todas=True),
            E('cocina', 'esquina', 'cubo_basura_pedal', cantidad=[0, 1]),
            E('cocina', 'esquina', 'fregona_cubo', cantidad=[0, 1]),
            E('cocina', 'esquina', 'escoba', cantidad=[0, 1]),
            E('cocina', 'techo', 'lampara_colgante', cantidad=[1, 1], obligatorio=True),
        ],
        'iluminacion': {'fuentes': [6, 9], 'temperatura_k': [2700, 3200], 'dia': {'intensidad': 0.8}, 'noche': {'intensidad': 1.0}, 'minimo_lux_publico': 80},
        'ambiente': {
            'sonido': 'restaurante', 'horario_defecto': 'Mo-Su 13:00-16:30,20:30-23:30',
            'vida': ['el menú del día en la pizarra', 'cestas de pan en las mesas', 'copas a medias', 'la cocina al fondo con las ollas al fuego'],
            'cerrado': 'persiana bajada y sillas sobre las mesas',
            'clientela': {'maximo': 12, 'horas': [[13, 16.5, 0.7], [20.5, 23.5, 0.55], [9, 12, 0.12]],
                          'frases': ['Hoy de primero hay migas, ¡y están de rechupete!', 'Ponme un tinto de verano bien fresquito.', '¿Queda postre casero?', 'El cordero es de aquí, de las Vegas.', 'Esto sí que es comer como en casa.', 'Otra de pan, que se acaba.']},
        },
        'minimo_objetos_distintos': 60,
    }
    escribir('restaurante', K)

if __name__ == '__main__':
    import sys
    quiere = sys.argv[1:] or ['banco', 'oficina', 'gimnasio', 'restaurante']
    for k in quiere:
        if k in globals() and callable(globals()[k]): globals()[k]()
