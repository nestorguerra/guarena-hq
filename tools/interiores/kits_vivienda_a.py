"""Kits domésticos A: esenciales y estancias de servicio, con referencias verificadas."""
from vivienda_base import *

def generar():
    C=catalogo();mood=json.load(open(os.path.join(ROOT,'tools','interiores','moodboard_vivienda_a.json')))
    comida=[k for k,o in C.items() if k.startswith('prod_') and o['soporte']=='superficie' and not any(x in k for x in ['deter','suaviz','lejia','limpia','fregas','higienico','gel','champu','dentif','compresa','basura'])]
    vajilla=['bandeja','azucarero','taza_cafe','taza_desayuno','plato_cafe','plato_llano','vaso_agua','cucharilla','frutero','servilletero']
    higiene_ids=['va_cepillero', 'va_dentifrico', 'va_jabonera', 'va_pastilla_jabon', 'va_peine', 'va_maquinilla', 'va_afeitado', 'va_esponja', 'va_algodon', 'va_bastoncillos', 'va_toalla', 'va_toalla_manos', 'va_secador', 'va_cortaunas', 'va_panuelos', 'va_colonia', 'va_desodorante', 'va_crema', 'va_locion', 'va_sales', 'va_hilo_dental', 'va_cepillo_pelo', 'va_gorro', 'va_cosmeticos', 'va_gel', 'va_champu']
    higiene=[k for k,o in C.items() if (k in higiene_ids or k.startswith(('per_cosm_','per_perfume_'))) and o['soporte']=='superficie']+['prod_papel_higienico','prod_gel_ducha','prod_champu_super','prod_dentifrico','prod_compresas','prod_esponjas']
    cocina=[pared('va_cocina'),junto('va_encimera',['va_cocina','va_encimera'],True),junto('va_nevera',['va_cocina','va_encimera'],True),pared('va_alacena'),pared('va_lavadora',False),E('pared','va_alto_cocina',pared='*',sobre_de='va_encimera',cantidad=[0,1]),junto('va_encimera',['va_cocina','va_encimera'],area_min=12),pared('va_alacena',False,area_min=16),E('conjunto','mesa_camilla',cantidad=[0,1],preferir=True,area_min=13,estilo=['antiguo','rustico'],sillas=dict(variantes=['silla_comedor'],n=[2,3])),E('conjunto','va_mesa_comedor',cantidad=[0,1],preferir=True,area_min=13,estilo=['!antiguo','!rustico'],sillas=dict(variantes=['silla_comedor'],n=[2,3]))]+adornos(comida+vajilla,['va_encimera','va_alacena','va_lavadora'])
    kit('cocina','Cocina de una casa del pueblo','cocina',cocina,mood['cocina'],fondo=(2.4,4.8))
    bano=[pared('va_lavabo'),E('pared','va_espejo',pared='*',sobre_de='va_lavabo',cantidad=[1,1],obligatorio=True),pared('va_ducha'),junto('va_inodoro','va_ducha',True),junto('va_toallero','va_lavabo',True),E('pared','va_papel',pared='*',sobre_de='va_inodoro',cantidad=[0,1]),junto('va_armario_bano','va_lavabo'),pared('va_banera',False,area_min=10),pared('va_cesto_ropa',False),junto('va_alfombrilla_bano','va_lavabo',lados=['frente'],si_no=False),E('sobre',['va_cepillero','va_jabonera','va_jabonera'],en=['va_lavabo'],por_soporte=[1,1])]+adornos(higiene,['va_armario_bano'])
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
    taller=[pared('va_banco'),junto('va_estante_taller','va_banco',True),pared('va_cajas_apiladas',False),pared('va_estante_taller',False,area_min=12),E('sobre',sueltos,en=['va_banco'],por_soporte=[1,2])]+adornos(herramientas,['va_estante_taller'])
    kit('taller','Taller doméstico de bricolaje','otra_estancia',taller,mood['taller'],fondo=(2.5,5))
    almacen= herramientas+['caja_carton','caja_archivo','vb_cesto','vb_ropa','vb_colcha']
    trastero=[pared('va_estante_alto'),pared('va_cajas_apiladas'),pared('va_cajas_apiladas',False),pared('va_estante_alto',False),pared('va_cajas_apiladas',False,area_min=12),pared('va_estante',False),pared('va_caja_almacen',False,area_min=12),pared('va_cajas_apiladas',False,area_min=18),E('suelo_libre','va_cajas_apiladas',cantidad=[1,1],obligatorio=True,area_min=14)]+adornos(almacen,['va_estante','va_estante_alto'])
    trastero[-2]['por_soporte']=[10,16]
    kit('trastero','Trastero de la vivienda','otra_estancia',trastero,mood['trastero'],fondo=(2.5,5))
    telas=[k for k,o in C.items() if o['soporte']=='superficie' and k.startswith(('va_hilo','va_tela','pila_camiseta','pila_pantalon','pila_jersey'))]+['va_tijeras','va_cinta_metrica','va_alfiletero','va_botones','va_agujas','va_patrones','va_dedal','va_retales','va_bastidor','va_cierre','va_caja_hilos','va_ovillo','vb_colcha','vb_ropa','vb_cesto','lampara_mesa']
    costura=[pared('va_costura'),junto('silla_comedor','va_costura',True,lados=['frente'],mira_ref=True),pared('va_estante'),pared('vb_armario',False),pared('sillon_orejero',False,area_min=14),E('pared',['cuadro_paisaje','fotos_familia'],pared='*',cantidad=[1,2])]+adornos(telas,['va_estante','va_costura'])
    kit('costura','Cuarto de costura y labores','otra_estancia',costura,mood['costura'],fondo=(2.3,5))

if __name__=='__main__':generar()
