"""Kits domésticos B: dormitorio y habitaciones personales, sin escribir al importar."""
from vivienda_base import *

def personales(C):
    return list(dict.fromkeys([k for k,o in C.items() if o['soporte']=='superficie' and (k.startswith(('hilera_libros_','pila_camiseta','pila_pantalon','pila_jersey','mue_cojin','mue_manta','per_perfume_')) or k in ['vb_despertador','vb_joyero','vb_hucha','vb_gafas','vb_zapatillas','vb_ropa','vb_colcha','vb_cuaderno','vb_cesto','vb_cargador'])]+['lampara_mesa','libro_tumbado','portarretratos','reloj_sobremesa','jarron_flores','figura_porcelana','telefono_casa','manta_doblada','cojin_suelto','cartera','movil','revista','periodico','velas']))

def infantiles(C):
    """Cuentos, juego, deberes y pertenencias domésticas; sólo piezas bajas reales."""
    from datos import alto
    familias={
        'lectura':['hilera_libros_a','hilera_libros_b','hilera_libros_c','hilera_libros_e','hilera_libros_f','lb_libros_infantiles','lb_libros_bolsillo','lb_libros_atlas','lb_diccionarios','lb_libros_cara_c','libro_tumbado'],
        'juego':['jg_puzles_madera','jg_pizarras','jg_dinosaurios','jg_figuras_accion','jg_tren_madera','jg_cartas','jg_pinturas_dedos','bz_cochecitos','vb_bloques'],
        'deberes_manualidades':['bloc_notas','portalapices','grapadora','va_tela_algodon','va_botones','va_cinta_metrica','va_ovillo','lb_estuches','lb_calculadoras','lb_gomas_tijeras','bz_cuadernos','bz_cuadernos_a4','vb_cuaderno','vb_acuarelas','vb_paleta','vb_pinceles'],
        'personales':['va_panuelos','va_cepillo_pelo','cesta_calcetines','vb_hucha','vb_despertador','vb_cesto','vb_ropa','vb_colcha','vb_joyero','vb_gafas','portarretratos','manta_doblada','vb_brujula','vb_prismaticos','vb_linterna','vb_auriculares'],
    }
    ids=list(dict.fromkeys(i for grupo in familias.values() for i in grupo))
    def altura(i):return max(c+h for h,c in map(alto,C[i]['partes']))
    bajos=[i for i in ids if C[i]['soporte']=='superficie' and altura(i)<=.280001]
    # En el tablero de deberes, ninguna pieza supera 16 cm. Lo más alto sólo
    # aparece en mesita o estante; no se añaden referencias ajenas para sumar IDs.
    return bajos,[i for i in bajos if altura(i)<=.160001]

def programa_estudio(p,C):
    """Receta base para contextos no optantes; frente adulto R2 en tres perfiles."""
    base=copy.deepcopy(p);perfiles=['artista','estudiante','musico']
    for e in base:e['perfil']=['!'+x for x in perfiles]
    mesa='vb_puesto_estudio_amplio';bajo='vb_guardado_estudio';bib='vb_biblioteca_estudio'
    nuevo=[E('contra_pared',mesa,pared=['N','S','E','W'],centrado=True,cantidad=[1,1],obligatorio=True,preferir=True,silla_frontal='vb_silla_estudio',grupo_pared='trabajo_consulta'),
           junto(bajo,[mesa],True,buscar_refs=True,si_no=False,grupo_pared='trabajo_consulta',espacio_frontal=[.70,.8]),
           junto(bib,[bajo],True,buscar_refs=True,si_no=True,grupo_pared='trabajo_consulta',espacio_frontal=[.75,.8]),
           E('sobre','vb_ordenador',en=[mesa],cantidad=[1,1],obligatorio=True,centrado=True)]
    for tema in perfiles:nuevo.append(E('sobre','vb_panel_estudio_'+tema,en=[mesa],cantidad=[1,1],obligatorio=True,centrado=True,perfil=[tema]))
    nuevo += [E('enfrente','vb_sillon_estudio',de=[mesa],cantidad=[0,1],preferir=True,area_min=11,si_no=False,espacio_frontal=[.70,.8]),
              junto('mesa_auxiliar_lectura',['vb_sillon_estudio'],si_no=False,area_min=11),E('sobre','libro_tumbado',en=['mesa_auxiliar_lectura'],cantidad=[0,1],preferir=True,centrado=True,area_min=11),
              E('sobre','vb_consulta_baja_estudio',en=[bajo],cantidad=[1,1],obligatorio=True,centrado=True,area_min=16)]
    for tema in perfiles:nuevo.append(E('sobre','vb_consulta_estudio_'+tema,en=[bib],cantidad=[2,2],obligatorio=True,centrado=True,perfil=[tema]))
    # Pool adulto existente: sólo sobre biblioteca, nunca sus hileras en el bajo.
    libros=[i for i,o in C.items()if i.startswith('lb_') and o['soporte']=='superficie' and i not in ['lb_libros_infantiles','lb_libros_morados','lb_agendas']]
    nuevo += [E('sobre',libros,en=[bib],cantidad=[0,1],preferir=True,centrado=True),
              E('sobre',['bloc_notas','vb_cuaderno','vb_partituras','grapadora','libro_tumbado'],en=[bajo],por_soporte=[0,1],area_max=16),
              E('pared',['cuadro_paisaje','fotos_familia','poster_enmarcado'],pared='*',cantidad=[0,1],preferir=True),copy.deepcopy(p[-1])]
    for e in nuevo:
        if 'perfil' not in e:e['perfil']=perfiles.copy()
    return base+nuevo

def generar():
    C=catalogo();mood=json.load(open(os.path.join(ROOT,'tools','interiores','moodboard_vivienda_b.json')))
    dormitorio=[pared('vb_cama_doble',habitacion=['dorm'],area_max=18,centrado=True),pared('vb_cama_amplia',habitacion=['dorm'],area_min=18,centrado=True),pared(['vb_cama_individual','vb_cama_doble'],habitacion=['dorm2']),junto('vb_mesita',['vb_cama_doble','vb_cama_individual','vb_cama_amplia'],True),pared('vb_armario'),pared('vb_comoda',False),junto('vb_mesita',['vb_cama_doble','vb_cama_individual','vb_cama_amplia'],area_min=16),pared('sillon_orejero',False,area_min=16),pared('vb_escritorio',False,area_min=22),junto('silla_comedor','vb_escritorio',lados=['frente'],mira_ref=True,area_min=22),pared('estanteria_libros',False,area_min=22),E('suelo_libre','vb_alfombra',cantidad=[0,1],area_min=16,area_max=26),E('suelo_libre','vb_alfombra',cantidad=[1,1],area_min=26,obligatorio=True),E('pared',['fotos_familia','cuadro_paisaje','cuadro_foto_antigua','cuadro_virgen','poster_enmarcado'],pared='*',cantidad=[1,3])]+adornos(personales(C),['vb_mesita','vb_comoda','vb_escritorio'])
    kit('dormitorio','Dormitorio de una casa del pueblo','dormitorio',dormitorio,mood['dormitorio'])
    libros=[k for k,o in C.items() if k.startswith('lb_') and o['soporte']=='superficie']
    juguetes=[k for k,o in C.items() if k.startswith('jg_') and o['soporte']=='superficie']
    papeles=libros+['libro_tumbado','portarretratos','reloj_sobremesa','lampara_mesa','vb_cuaderno','vb_despertador','vb_ordenador','movil','cartera']
    for id,hab,nombre,mesa_id in [('ninos','ninos','Cuarto de los niños','vb_mesa_ninos'),('joven','dormJoven','Dormitorio del estudiante','vb_escritorio')]:
        silla='vb_silla_ninos' if id=='ninos' else 'silla_comedor'
        soportes=['vb_mesita',mesa_id,'vb_estante_bajo']
        p=[pared('vb_cama_individual'),junto('vb_mesita','vb_cama_individual',True),pared(mesa_id),junto(silla,mesa_id,True,lados=['frente'],mira_ref=True),pared('vb_armario'),pared('vb_estante_bajo',False),pared('vb_cama_individual',False,area_min=20,habitacion=['ninos']),E('pared',['poster_enmarcado','fotos_familia','cuadro_paisaje'],pared='*',cantidad=[1,3])]
        if id=='ninos':
            # Un puesto se admite sólo con su silla frontal: no hay silla dispersa.
            # Descanso conservado; estudio completo con silla, biblioteca vinculada
            # al puesto, probados juntos; armario independiente en esquina libre.
            # Reglas generales: no se leen semillas, perfiles ni cámaras.
            p=[pared('vb_cama_ninos'),junto('vb_mesita','vb_cama_ninos',True),
               E('contra_pared',mesa_id,pared=['N','S','E','W'],cantidad=[1,1],obligatorio=True,preferir=True,silla_frontal=silla,grupo_pared='estudio_infantil'),
               junto('vb_biblioteca_ninos',mesa_id,True,buscar_refs=True,si_no=False,grupo_pared='estudio_infantil'),
               E('esquina','vb_armario_ninos',cantidad=[1,1],obligatorio=True,preferir=True,espacio_frontal=[.7,.6]),
               pared('vb_cama_ninos',False,area_min=20,habitacion=['ninos']),
               # Lectura frente a los libros: sólo si cabe con el cuerpo y su uso.
               # Separar la trasera deja intactas las cortinas hasta el suelo.
               E('suelo_libre','vb_alfombra_juego',cantidad=[1,1],obligatorio=True,suelo_determinista=True,area_min=12),
               E('suelo_libre','vb_alfombra_juego_compacta',cantidad=[1,1],obligatorio=True,suelo_determinista=True,area_max=12),
               E('enfrente','vb_banco_lectura_ninos',de='vb_biblioteca_ninos',cantidad=[0,1],preferir=True,centrado=True,si_no=False,separacion_pared=.14,espacio_frontal=[.7,.55]),
               E('pared','vb_dibujos_ninos',pared='*',sobre_de='vb_cama_ninos',cantidad=[0,1],preferir=True,si_no=False)]
            soportes=['vb_mesita',mesa_id,'vb_biblioteca_ninos']
        if id=='ninos':p += [E('sobre','vb_osito',en=['vb_mesita'],cantidad=[1,1],obligatorio=True),E('sobre','vb_bloques',en=['vb_biblioteca_ninos'],cantidad=[1,1],obligatorio=True)]
        if id=='joven':p += [pared('guitarra_soporte',False),E('sobre','vb_ordenador',en=[mesa_id],cantidad=[1,1])]
        if id=='joven':p += [pared('estanteria_libros',False,area_min=16),pared('mueble_tv',False,area_min=22),E('sobre','televisor_plano',en=['mueble_tv'],cantidad=[1,1],area_min=22),E('enfrente','sofa_dos_plazas',de='televisor_plano',cantidad=[0,1],preferir=True,si_no=False,area_min=22,area_max=30),E('enfrente','sofa_dos_plazas',de='televisor_plano',cantidad=[1,1],obligatorio=True,si_no=False,area_min=30),E('entre','mesa_centro',a='televisor_plano',b='sofa_dos_plazas',cantidad=[0,1],area_min=22),pared('vb_comoda',False,area_min=18),E('suelo_libre','vb_alfombra',cantidad=[0,1],area_min=18)]
        if id=='joven':soportes+=['estanteria_libros','mesa_centro','vb_comoda']
        p+=adornos(juguetes+libros+['vb_hucha','vb_despertador','vb_cuaderno','vb_cesto','vb_ropa','vb_colcha','lampara_mesa','libro_tumbado','cojin_suelto'] if id=='ninos' else papeles+personales(C),soportes)
        if id=='ninos':
            # La mesa queda para juego y deberes: piezas pequeñas, sin hileras altas de libros.
            bajos,tablero=infantiles(C)
            p[-2:-1]=[E('sobre',tablero,en=[mesa_id],por_soporte=[1,2]),
                       E('sobre',bajos,en=['vb_mesita'],por_soporte=[1,2]),
                       E('sobre',['vb_cuentos_biblioteca','vb_hacer_biblioteca'],en=['vb_biblioteca_ninos'],por_soporte=[1,1])]
        kit(id,nombre,'dormitorio',p,mood[id],fondo=(2.1,5.2))
    for id,nombre in [('estudio','Estudio para leer y trabajar'),('despacho','Despacho doméstico')]:
        p=[pared('vb_escritorio'),junto('silla_comedor','vb_escritorio',True,lados=['frente'],mira_ref=True),pared('estanteria_libros'),pared('vb_comoda',False),pared('sillon_orejero',False,area_min=11),pared('estanteria_libros',False,area_min=16),E('pared',['cuadro_paisaje','fotos_familia','poster_enmarcado'],pared='*',cantidad=[1,3]),E('sobre','vb_ordenador',en=['vb_escritorio'],cantidad=[1,1])]
        if id=='despacho':p += [pared('caja_fuerte_pequena',botin='cajaFuerte')]
        if id=='despacho':
            mesas=['vb_mesa_despacho_0','vb_mesa_despacho_1','vb_mesa_despacho_2']
            p[0]=pared(mesas);p[1]=junto('vb_silla_despacho',mesas,True,lados=['frente'],mira_ref=True)
            p[-2]=E('sobre','vb_ordenador',en=mesas,cantidad=[1,1])
            p += [junto('vb_mesa_lectura','sillon_orejero',lados=['derecha','izquierda']),E('suelo_libre','vb_alfombra',cantidad=[0,1],preferir=True,area_min=13)]
        p+=adornos([x for x in papeles if x!='vb_ordenador'] if id=='despacho' else papeles,(mesas if id=='despacho' else ['vb_escritorio'])+['vb_comoda','estanteria_libros'])
        if id=='estudio':p=programa_estudio(p,C)
        kit(id,nombre,'otra_estancia',p,mood[id],fondo=(2.1,5))
    musica=[pared('piano_pared'),junto('banqueta_piano','piano_pared',lados=['frente'],mira_ref=True),pared('guitarra_soporte'),pared('guitarra_soporte',False,botin='guitarra'),pared('vb_altavoz'),pared('vb_altavoz',False,botin='altavoz'),pared('estanteria_libros',False),pared('vb_escritorio',False),E('sobre','vb_vinilos',en=['vb_escritorio'],cantidad=[0,1],botin='vinilos'),E('pared',['poster_enmarcado','cuadro_paisaje'],pared='*',cantidad=[1,3])]+adornos(papeles+['vb_vinilos','vb_partituras','vb_auriculares','vb_metronomo'],['vb_escritorio','estanteria_libros'])
    kit('musica','Cuarto de música','otra_estancia',musica,mood['musica'],fondo=(2.1,5))
    trofeos=[pared('vb_armero'),pared('vb_rifle',botin='rifle'),E('pared','vb_cornamenta',pared='*',cantidad=[2,4],obligatorio=True),pared('sillon_orejero'),pared('estanteria_libros',False),pared('vb_comoda',False),E('sobre','vb_prismaticos',en=['vb_comoda','estanteria_libros'],cantidad=[0,1],botin='prismaticos')]+adornos(libros+['vb_brujula','vb_linterna','vb_bolsa_caza','vb_prismaticos','libro_tumbado','reloj_sobremesa'],['vb_comoda','estanteria_libros'])
    kit('trofeos','Cuarto de trofeos del cazador','otra_estancia',trofeos,mood['trofeos'],fondo=(2.1,5))
    arte=['vb_paleta','vb_pinceles','vb_carboncillos','vb_acuarelas','vb_tubos_oleo','vb_trapo']+[k for k,o in C.items() if k.startswith('fe_pintura') and o['soporte']=='superficie']+libros+['lb_rotuladores','lb_papel_folios']
    pintura=[pared('vb_caballete'),pared('vb_escritorio'),junto('silla_comedor','vb_escritorio',True,lados=['frente'],mira_ref=True),pared('estanteria_libros',False),pared('vb_caballete',False,area_min=12),E('pared','cuadro_paisaje',pared='*',cantidad=[0,1],botin='cuadro'),E('pared',['cuadro_paisaje','poster_enmarcado'],pared='*',cantidad=[1,3])]+adornos(arte,['vb_escritorio','estanteria_libros'])
    kit('pintura','Estudio de pintura','otra_estancia',pintura,mood['pintura'],fondo=(2.1,5))

if __name__=='__main__':generar()
