"""Kits domésticos A: esenciales y estancias de servicio, con referencias verificadas."""
from vivienda_base import *

def generar():
    C=catalogo();mood=json.load(open(os.path.join(ROOT,'tools','interiores','moodboard_vivienda_a.json')))
    comida=[k for k,o in C.items() if k.startswith('va_alimento_') and o['soporte']=='superficie']
    vajilla=['bandeja','azucarero','taza_cafe','taza_desayuno','plato_cafe','plato_llano','vaso_agua','cucharilla','frutero','servilletero']
    higiene_ids=['va_cepillero', 'va_dentifrico', 'va_jabonera', 'va_pastilla_jabon', 'va_peine', 'va_maquinilla', 'va_afeitado', 'va_esponja', 'va_algodon', 'va_bastoncillos', 'va_toalla', 'va_toalla_manos', 'va_secador', 'va_cortaunas', 'va_panuelos', 'va_colonia', 'va_desodorante', 'va_crema', 'va_locion', 'va_sales', 'va_hilo_dental', 'va_cepillo_pelo', 'va_gorro', 'va_cosmeticos', 'va_gel', 'va_champu']
    higiene=[k for k,o in C.items() if (k in higiene_ids or k.startswith(('per_cosm_','per_perfume_'))) and o['soporte']=='superficie']+['prod_papel_higienico','prod_gel_ducha','prod_champu_super','prod_dentifrico','prod_compresas','prod_esponjas']
    frentes=['va_cocina','va_cocina_amplia','va_encimera','va_encimera_amplia']
    # Un frente de trabajo continuo; la puerta puede obligar a usar otra pared.
    cocina=[
        pared('va_cocina',area_max=14,grupo_pared='frente_trabajo'),pared('va_cocina_amplia',area_min=14,grupo_pared='frente_trabajo'),
        junto('va_encimera',frentes,True,area_max=14,buscar_refs=True,grupo_pared='frente_trabajo'),
        junto('va_encimera_amplia',frentes,True,area_min=14,buscar_refs=True,grupo_pared='frente_trabajo'),
        junto('va_nevera',frentes,True,buscar_refs=True,grupo_pared='frente_trabajo'),
        *[E('pared','va_alto_cocina'+sufijo+('_amplio' if amplio else ''),pared='*',sobre_de='va_encimera'+('_amplia' if amplio else ''),cantidad=[0,1],preferir=True,si_no=False,estilo=estilos,**({'area_min':14} if amplio else {'area_max':14}))
          for sufijo,estilos in [('', ['antiguo','rustico']),('_liso',['moderno','joven','lujo']),('_abierto',['!antiguo','!rustico','!moderno','!joven','!lujo'])]
          for amplio in [False,True]],
        junto('va_lavadora',frentes,buscar_refs=True),junto('va_alacena',frentes,True,buscar_refs=True),
        junto('va_encimera_amplia',frentes,area_min=18,buscar_refs=True),
        pared('va_alacena',False,area_min=20),
        E('conjunto','mesa_camilla',cantidad=[0,1],preferir=True,area_min=13,estilo=['antiguo','rustico'],sillas=dict(variantes=['silla_comedor'],n=[2,3])),
        E('conjunto','va_mesa_comedor',cantidad=[0,1],preferir=True,area_min=13,estilo=['!antiguo','!rustico'],sillas=dict(variantes=['silla_comedor'],n=[2,3])),
        E('suelo_libre','va_isla_cocina',cantidad=[0,1],preferir=True,area_min=22),
    ]+adornos(comida+vajilla,['va_encimera','va_encimera_amplia','va_alacena','va_lavadora','va_isla_cocina'])
    kit('cocina','Cocina de una casa del pueblo','cocina',cocina,mood['cocina'],fondo=(2.4,4.8))
    # En salas grandes, reservar el frente de aseo antes de comprometer el lavabo.
    # Armario opcional: si no cabe el conjunto, el fallback conserva su omisión.
    bano=[
        pared('va_lavabo',area_max=10),
        pared('va_lavabo_amplio',area_min=10,grupo_pared='aseo_diario',reserva_lateral=dict(obj='va_toallero',lado='izquierda')),
        junto('va_armario_bano','va_lavabo_amplio',area_min=10,grupo_pared='aseo_diario',si_no=False),
        junto('va_toallero','va_lavabo_amplio',True,area_min=10,lados=['izquierda'],si_no=False),
        E('pared','va_espejo',pared='*',sobre_de='va_lavabo',cantidad=[1,1],obligatorio=True,area_max=10),
        E('pared','va_espejo_amplio',pared='*',sobre_de='va_lavabo_amplio',cantidad=[1,1],obligatorio=True,area_min=10),
        E('enfrente','va_inodoro',de=['va_lavabo','va_lavabo_amplio'],cantidad=[1,1],obligatorio=True,area_min=10),
        pared('va_ducha',area_max=10),
        junto('va_inodoro','va_ducha',True,area_max=10),
        junto('va_toallero',['va_lavabo','va_lavabo_amplio'],True,area_max=10),
        E('pared','va_papel',pared='*',sobre_de='va_inodoro',cantidad=[0,1]),
        junto('va_armario_bano',['va_lavabo','va_lavabo_amplio'],area_max=10),
        # Conjunto húmedo independiente del aseo: reservar ducha + bañera completas.
        # La ducha sigue obligatoria y la bañera opcional al recurrir al fallback.
        pared('va_ducha',area_min=10,grupo_pared='zona_humeda'),
        junto('va_banera','va_ducha',area_min=10,grupo_pared='zona_humeda',si_no=False),
        pared('va_cesto_ropa',False),
        junto('va_alfombrilla_bano',['va_lavabo','va_lavabo_amplio'],lados=['frente'],si_no=False),
        E('sobre',['va_cepillero','va_jabonera','va_jabonera'],en=['va_lavabo','va_lavabo_amplio'],por_soporte=[1,1]),
    ]+adornos(higiene,['va_armario_bano'])
    for e in bano:
        if e.get('obj')=='va_inodoro':e['espacio_frontal']=[.6,.65]
    kit('bano','Baño doméstico','bano',bano,mood['bano'],fondo=(1.9,3.6))
    mesas_comedor=['va_mesa_comedor','va_mesa_familiar']
    servicio_comedor=['bandeja','azucarero','taza_cafe','taza_desayuno','plato_cafe','plato_llano','vaso_agua','copa_vino','cucharilla','servilletero','cubiertos_servicio','servilleta_doblada','jarra_agua','salero_pimentero','aceitera_vinagrera','botella_vino_tinto','botella_vino_blanco','bote_caramelos','florero_mesa','portarretratos','reloj_sobremesa']
    comedor=[
        E('conjunto','va_mesa_comedor',cantidad=[1,1],obligatorio=True,giro=[0,90],centrado=True,area_max=12,sillas=dict(variantes=['silla_comedor'],n=2,lados=['+z','-z'])),
        E('conjunto','va_mesa_familiar',cantidad=[1,1],obligatorio=True,giro=[0,90],centrado=True,area_min=12,sillas=dict(variantes=['silla_comedor'],n=4,lados=['+z','-z','+x','-x'])),
        pared('aparador',False),pared('va_alacena',False),
        E('pared','cuadro_paisaje',pared='*',cantidad=[1,1],obligatorio=True),
        E('pared','fotos_familia',pared='*',cantidad=[0,1]),
        E('pared','cuadro_virgen',pared='*',cantidad=[0,1]),
        E('sobre','va_servicio_comedor_2',en=['va_mesa_comedor'],cantidad=[1,1],obligatorio=True,centrado=True,area_max=12),
        E('sobre','va_servicio_comedor_4',en=['va_mesa_familiar'],cantidad=[1,1],obligatorio=True,centrado=True,area_min=12),
        # Un único objeto/acción de cada pertenencia, antes de llenar baldas opcionales.
        *[E('sobre',obj,en=['aparador','va_alacena'],cantidad=[0,1],preferir=True,botin=botin)
          for obj,botin in [('va_joyero_guardado','joyero'),('va_lata_guardada','lata'),('va_reloj_guardado','reloj')]],
        E('sobre',['va_vajilla_guardada_platos','va_vajilla_guardada_tazas'],en=['va_alacena'],por_soporte=[1,1]),
        E('sobre',servicio_comedor,en=['aparador'],por_soporte=[2,3]),
        E('techo','lampara_techo_salon',cantidad=[1,1],obligatorio=True,sobre_de='va_mesa_comedor',area_max=12),
        E('techo','lampara_techo_salon',cantidad=[1,1],obligatorio=True,sobre_de='va_mesa_familiar',area_min=12),
    ]
    kit('comedor','Comedor familiar','otra_estancia',comedor,mood['comedor'],fondo=(2.5,5))
    reservas=[k for k in C if k.startswith(('va_reserva_','va_conserva_'))]
    # Frente doméstico de guardado: módulo bajo entre dos alturas, antes de ampliar.
    # Si no cabe, los obligatorios conservan su búsqueda individual de pared.
    guardado=['va_estante','aparador','va_estante_alto','va_alacena']
    despensa=[
        pared('va_estante',grupo_pared='guardado_despensa'),
        junto('aparador','va_estante',True,buscar_refs=True,grupo_pared='guardado_despensa'),
        junto('va_estante_alto','aparador',area_min=8,buscar_refs=True,si_no=False,grupo_pared='guardado_despensa'),
        junto('va_alacena',guardado,area_min=12,buscar_refs=True,si_no=False),
        junto('va_estante_alto',guardado,area_min=18,buscar_refs=True,si_no=False),
        junto('va_tinaja',guardado,buscar_refs=True,si_no=False,estilo=['antiguo','rustico']),
        junto('va_cajas_apiladas',guardado,area_min=9,area_max=14,buscar_refs=True,si_no=False),
        junto('va_cajas_apiladas',guardado,True,area_min=14,buscar_refs=True),
        # En la superficie baja: formatos grandes y provisiones de uso cotidiano.
        E('sobre',['va_alimento_garrafa_aceite','va_alimento_vinagre','va_alimento_miel','va_alimento_pimientos_piquillo'],en=['aparador'],por_soporte=[2,3],perfil=['agricultor','cazador']),
        E('sobre',['va_alimento_pan_molde','va_alimento_galletas_maria','va_alimento_cafe_molido','va_alimento_mermelada','va_alimento_leche_semi'],en=['aparador'],por_soporte=[2,3],perfil=['!agricultor','!cazador']),
        # La balda pequeña deja al menos 23 cm útiles; las botellas van al mueble alto.
        E('sobre',reservas+[k for k in comida if k not in [
            'va_alimento_aceite_oliva','va_alimento_aceite_girasol','va_alimento_garrafa_aceite','va_alimento_vinagre',
            'va_alimento_espaguetis','va_alimento_cereales_a','va_alimento_cereales_b','va_alimento_cereales_c',
            'va_alimento_snack_patatas','va_alimento_snack_aperitivos','va_alimento_agua_15','va_alimento_cola_15',
            'va_alimento_naranja_15','va_alimento_limon_15','va_alimento_vino_tinto','va_alimento_vino_blanco','va_alimento_vino_rosado',
        ]],en=['va_estante'],por_soporte=[2,4]),
    ]+adornos(reservas+comida,['va_alacena','va_estante_alto'])
    # Unidades de varios formatos, con huecos entre grupos; nunca facings de tienda.
    despensa[-2]['por_soporte']=[2,4]
    kit('despensa','Despensa doméstica','otra_estancia',despensa,mood['despensa'])
    herramientas=[k for k,o in C.items() if k.startswith('fe_') and o['soporte']=='superficie' and 'insectic' not in k]+['tal_llaves_juego','tal_martillo','tal_caja_herramientas','tal_trapos','tal_rollo_papel_taller']
    sueltos=['tal_llaves_juego','tal_martillo','tal_caja_herramientas','tal_trapos','tal_rollo_papel_taller','fe_niveles_metros','fe_tijeras_poda','fe_guantes_trabajo']
    bancos=['va_banco','va_banco_carpinteria','va_banco_mecanica']
    todos_bancos=bancos+[id+'_amplio' for id in bancos]
    taller=[pared(bancos,area_max=10.5),pared([id+'_amplio' for id in bancos],area_min=10.5),junto('va_estante_taller',todos_bancos,True),pared('va_cajas_apiladas',False),pared('va_estante_taller',False,area_min=12),E('sobre',sueltos,en=todos_bancos,por_soporte=[1,2])]+adornos(herramientas,['va_estante_taller'])
    kit('taller','Taller doméstico de bricolaje','otra_estancia',taller,mood['taller'],fondo=(2.5,5))
    almacen= herramientas+['caja_carton','caja_archivo','vb_cesto','vb_ropa','vb_colcha']
    estantes=['va_estante_trastero_0','va_estante_trastero_1','va_estante_trastero_2']
    guardados=['va_bicicleta_guardada','va_bicicleta_carga','va_escalera_guardada']
    almacenaje=estantes+['va_cajas_apiladas']
    # La pareja alta/baja arranca en un extremo libre de pared: primero el
    # estante y su bicicleta/escalera, antes de consumir el frente con otro estante.
    # Los obligatorios mantienen el fallback de junto_a si esa relación no cabe.
    trastero=[
        pared(estantes),junto(guardados,estantes,True,buscar_refs=True),
        junto(estantes,guardados+estantes,True,area_min=10,buscar_refs=True),
        junto('va_cajas_apiladas',estantes,True,area_min=14,buscar_refs=True),
        E('pared','va_soporte_ciclismo',pared='*',sobre_de='va_bicicleta_guardada',cantidad=[0,1],preferir=True,si_no=False),
        E('pared','va_soporte_ciclismo',pared='*',sobre_de='va_bicicleta_carga',cantidad=[0,1],preferir=True,si_no=False),
        E('pared','va_soporte_pintura',pared='*',sobre_de='va_escalera_guardada',cantidad=[0,1],preferir=True,si_no=False),
        junto('va_cesto_temporada',estantes,True,buscar_refs=True),
        junto(estantes,estantes,area_min=18,buscar_refs=True,si_no=False),
        junto('va_cajas_apiladas',almacenaje,area_min=16,buscar_refs=True,si_no=False),
        junto('va_caja_almacen',almacenaje,area_min=12,buscar_refs=True,si_no=False),
        junto('va_ventilador_guardado',guardados,buscar_refs=True,si_no=False),
        junto('va_utiles_guardados',guardados,buscar_refs=True,si_no=False),
    ]+adornos(almacen,estantes)
    trastero[-2]['por_soporte']=[2,4]
    kit('trastero','Trastero de la vivienda','otra_estancia',trastero,mood['trastero'],fondo=(2.5,5))
    telas=[k for k,o in C.items() if o['soporte']=='superficie' and k.startswith(('va_hilo','va_tela','pila_camiseta','pila_pantalon','pila_jersey'))]+['va_tijeras','va_cinta_metrica','va_alfiletero','va_botones','va_agujas','va_patrones','va_dedal','va_retales','va_bastidor','va_cierre','va_caja_hilos','va_ovillo','vb_colcha','vb_ropa','vb_cesto','lampara_mesa']
    labores=['va_costura','va_costura_bordado','va_costura_patrones']
    costura=[pared(labores,silla_frontal='silla_comedor'),junto('va_mueble_telas',labores,True),pared('vb_armario',False),pared('sillon_orejero',False,area_min=14),E('pared',['cuadro_paisaje','fotos_familia'],pared='*',cantidad=[1,2])]+adornos(telas,['va_mueble_telas'])
    kit('costura','Cuarto de costura y labores','otra_estancia',costura,mood['costura'],fondo=(2.3,5))

if __name__=='__main__':generar()
