"""Kits domésticos A: esenciales y estancias de servicio, con referencias verificadas."""
from vivienda_base import *

def generar():
    C=catalogo();mood=json.load(open(os.path.join(ROOT,'tools','interiores','moodboard_vivienda_a.json')))
    comida=[k for k,o in C.items() if k.startswith('va_alimento_') and o['soporte']=='superficie']
    vajilla=['bandeja','azucarero','taza_cafe','taza_desayuno','plato_cafe','plato_llano','vaso_agua','cucharilla','frutero','servilletero']
    higiene_ids=['va_cepillero', 'va_dentifrico', 'va_jabonera', 'va_pastilla_jabon', 'va_peine', 'va_maquinilla', 'va_afeitado', 'va_esponja', 'va_algodon', 'va_bastoncillos', 'va_toalla', 'va_toalla_manos', 'va_secador', 'va_cortaunas', 'va_panuelos', 'va_colonia', 'va_desodorante', 'va_crema', 'va_locion', 'va_sales', 'va_hilo_dental', 'va_cepillo_pelo', 'va_gorro', 'va_cosmeticos', 'va_gel', 'va_champu']
    higiene=[k for k,o in C.items() if (k in higiene_ids or k.startswith(('per_cosm_','per_perfume_'))) and o['soporte']=='superficie']+['prod_papel_higienico','prod_gel_ducha','prod_champu_super','prod_dentifrico','prod_compresas','prod_esponjas']
    frentes=['va_cocina','va_cocina_amplia','va_encimera','va_encimera_amplia']
    cocina=[pared('va_cocina',area_max=14),pared('va_cocina_amplia',area_min=14),junto('va_encimera',frentes,True,area_max=14),junto('va_encimera_amplia',frentes,True,area_min=14),junto('va_nevera',frentes,True),pared('va_alacena'),pared('va_lavadora',False),E('pared','va_alto_cocina',pared='*',sobre_de='va_encimera',cantidad=[0,1],preferir=True,area_max=14),E('pared','va_alto_cocina',pared='*',sobre_de='va_encimera_amplia',cantidad=[0,1],preferir=True,area_min=14),junto('va_encimera_amplia',frentes,area_min=18),pared('va_alacena',False,area_min=20),E('conjunto','mesa_camilla',cantidad=[0,1],preferir=True,area_min=13,estilo=['antiguo','rustico'],sillas=dict(variantes=['silla_comedor'],n=[2,3])),E('conjunto','va_mesa_comedor',cantidad=[0,1],preferir=True,area_min=13,estilo=['!antiguo','!rustico'],sillas=dict(variantes=['silla_comedor'],n=[2,3])),E('suelo_libre','va_isla_cocina',cantidad=[0,1],preferir=True,area_min=22)]+adornos(comida+vajilla,['va_encimera','va_encimera_amplia','va_alacena','va_lavadora','va_isla_cocina'])
    kit('cocina','Cocina de una casa del pueblo','cocina',cocina,mood['cocina'],fondo=(2.4,4.8))
    bano=[pared('va_lavabo',area_max=10),pared('va_lavabo_amplio',area_min=10),E('pared','va_espejo',pared='*',sobre_de='va_lavabo',cantidad=[1,1],obligatorio=True,area_max=10),E('pared','va_espejo_amplio',pared='*',sobre_de='va_lavabo_amplio',cantidad=[1,1],obligatorio=True,area_min=10),pared('va_ducha'),junto('va_inodoro','va_ducha',True),junto('va_toallero',['va_lavabo','va_lavabo_amplio'],True),E('pared','va_papel',pared='*',sobre_de='va_inodoro',cantidad=[0,1]),junto('va_armario_bano',['va_lavabo','va_lavabo_amplio']),pared('va_banera',False,area_min=10),pared('va_cesto_ropa',False),junto('va_alfombrilla_bano',['va_lavabo','va_lavabo_amplio'],lados=['frente'],si_no=False),E('sobre',['va_cepillero','va_jabonera','va_jabonera'],en=['va_lavabo','va_lavabo_amplio'],por_soporte=[1,1])]+adornos(higiene,['va_armario_bano'])
    kit('bano','Baño doméstico','bano',bano,mood['bano'],fondo=(1.9,3.6))
    comedor=[E('conjunto','va_mesa_comedor',cantidad=[1,1],obligatorio=True,giro=[0,90],sillas=dict(variantes=['silla_comedor'],n=[2,4])),pared('aparador',False),pared('va_alacena',False),E('pared',['cuadro_paisaje','fotos_familia','cuadro_virgen'],pared='*',cantidad=[1,3]),E('sobre',vajilla,en=['va_mesa_comedor'],por_soporte=[2,4])]+adornos(vajilla+comida,['aparador','va_alacena'])
    kit('comedor','Comedor familiar','otra_estancia',comedor,mood['comedor'],fondo=(2.5,5))
    reservas=[k for k in C if k.startswith(('va_reserva_','va_conserva_'))]
    despensa=[pared('va_estante'),pared('va_estante',False),pared('va_alacena',False),pared('va_estante_alto',False,area_min=8),pared('va_estante_alto',False,area_min=12),pared('va_tinaja',False),pared('va_cajas_apiladas',False,area_min=9),E('suelo_libre','va_cajas_apiladas',cantidad=[1,1],obligatorio=True,area_min=14)]+adornos(reservas+comida,['va_estante','va_alacena','va_estante_alto'])
    despensa[-2]['variantes']=reservas
    despensa[-2]['por_soporte']=[12,20]
    despensa.insert(-1,E('sobre',comida,en=['va_estante','va_alacena','va_estante_alto'],por_soporte=[0,2]))
    kit('despensa','Despensa doméstica','otra_estancia',despensa,mood['despensa'])
    herramientas=[k for k,o in C.items() if k.startswith('fe_') and o['soporte']=='superficie' and 'insectic' not in k]+['tal_llaves_juego','tal_martillo','tal_caja_herramientas','tal_trapos','tal_rollo_papel_taller']
    sueltos=['tal_llaves_juego','tal_martillo','tal_caja_herramientas','tal_trapos','tal_rollo_papel_taller','fe_niveles_metros','fe_tijeras_poda','fe_guantes_trabajo']
    bancos=['va_banco','va_banco_carpinteria','va_banco_mecanica']
    todos_bancos=bancos+[id+'_amplio' for id in bancos]
    taller=[pared(bancos,area_max=10.5),pared([id+'_amplio' for id in bancos],area_min=10.5),junto('va_estante_taller',todos_bancos,True),pared('va_cajas_apiladas',False),pared('va_estante_taller',False,area_min=12),E('sobre',sueltos,en=todos_bancos,por_soporte=[1,2])]+adornos(herramientas,['va_estante_taller'])
    kit('taller','Taller doméstico de bricolaje','otra_estancia',taller,mood['taller'],fondo=(2.5,5))
    almacen= herramientas+['caja_carton','caja_archivo','vb_cesto','vb_ropa','vb_colcha']
    estantes=['va_estante_trastero_0','va_estante_trastero_1','va_estante_trastero_2']
    trastero=[pared(estantes),junto('va_cajas_apiladas',estantes,True),pared(estantes,area_min=10),pared(estantes,False,area_min=18),pared('va_utiles_guardados',False),pared('va_cajas_apiladas',False,area_min=16),pared('va_caja_almacen',False,area_min=12),E('suelo_libre','va_cajas_apiladas',cantidad=[1,1],obligatorio=True,area_min=14)]+adornos(almacen,estantes)
    trastero[-2]['por_soporte']=[2,4]
    kit('trastero','Trastero de la vivienda','otra_estancia',trastero,mood['trastero'],fondo=(2.5,5))
    telas=[k for k,o in C.items() if o['soporte']=='superficie' and k.startswith(('va_hilo','va_tela','pila_camiseta','pila_pantalon','pila_jersey'))]+['va_tijeras','va_cinta_metrica','va_alfiletero','va_botones','va_agujas','va_patrones','va_dedal','va_retales','va_bastidor','va_cierre','va_caja_hilos','va_ovillo','vb_colcha','vb_ropa','vb_cesto','lampara_mesa']
    labores=['va_costura','va_costura_bordado','va_costura_patrones']
    costura=[pared(labores,silla_frontal='silla_comedor'),junto('va_mueble_telas',labores,True),pared('vb_armario',False),pared('sillon_orejero',False,area_min=14),E('pared',['cuadro_paisaje','fotos_familia'],pared='*',cantidad=[1,2])]+adornos(telas,['va_mueble_telas'])
    kit('costura','Cuarto de costura y labores','otra_estancia',costura,mood['costura'],fondo=(2.3,5))

if __name__=='__main__':generar()
