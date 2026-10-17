"""Kits domésticos B: dormitorio y habitaciones personales, sin escribir al importar."""
from vivienda_base import *

def personales(C):
    return list(dict.fromkeys([k for k,o in C.items() if o['soporte']=='superficie' and (k.startswith(('hilera_libros_','pila_camiseta','pila_pantalon','pila_jersey','mue_cojin','mue_manta','per_perfume_')) or k in ['vb_despertador','vb_joyero','vb_hucha','vb_gafas','vb_zapatillas','vb_ropa','vb_colcha','vb_cuaderno','vb_cesto','vb_cargador'])]+['lampara_mesa','libro_tumbado','portarretratos','reloj_sobremesa','jarron_flores','figura_porcelana','telefono_casa','manta_doblada','cojin_suelto','cartera','movil','revista','periodico','velas']))

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
        if id=='ninos':p += [E('sobre','vb_osito',en=['vb_mesita'],cantidad=[1,1],obligatorio=True),E('sobre','vb_bloques',en=[mesa_id,'vb_estante_bajo'],cantidad=[1,1],obligatorio=True)]
        if id=='joven':p += [pared('guitarra_soporte',False),E('sobre','vb_ordenador',en=[mesa_id],cantidad=[1,1])]
        if id=='joven':p += [pared('estanteria_libros',False,area_min=16),pared('mueble_tv',False,area_min=22),E('sobre','televisor_plano',en=['mueble_tv'],cantidad=[1,1],area_min=22),E('enfrente','sofa_dos_plazas',de='televisor_plano',cantidad=[0,1],preferir=True,si_no=False,area_min=22,area_max=30),E('enfrente','sofa_dos_plazas',de='televisor_plano',cantidad=[1,1],obligatorio=True,si_no=False,area_min=30),E('entre','mesa_centro',a='televisor_plano',b='sofa_dos_plazas',cantidad=[0,1],area_min=22),pared('vb_comoda',False,area_min=18),E('suelo_libre','vb_alfombra',cantidad=[0,1],area_min=18)]
        if id=='joven':soportes+=['estanteria_libros','mesa_centro','vb_comoda']
        p+=adornos(juguetes+libros+['vb_hucha','vb_despertador','vb_cuaderno','vb_cesto','vb_ropa','vb_colcha','lampara_mesa','libro_tumbado','cojin_suelto'] if id=='ninos' else papeles+personales(C),soportes)
        kit(id,nombre,'dormitorio',p,mood[id],fondo=(2.1,5.2))
    for id,nombre in [('estudio','Estudio para leer y trabajar'),('despacho','Despacho doméstico')]:
        p=[pared('vb_escritorio'),junto('silla_comedor','vb_escritorio',True,lados=['frente'],mira_ref=True),pared('estanteria_libros'),pared('vb_comoda',False),pared('sillon_orejero',False,area_min=11),pared('estanteria_libros',False,area_min=16),E('pared',['cuadro_paisaje','fotos_familia','poster_enmarcado'],pared='*',cantidad=[1,3]),E('sobre','vb_ordenador',en=['vb_escritorio'],cantidad=[1,1])]
        if id=='despacho':p += [pared('caja_fuerte_pequena',botin='cajaFuerte')]
        p+=adornos(papeles,['vb_escritorio','vb_comoda','estanteria_libros'])
        kit(id,nombre,'otra_estancia',p,mood[id],fondo=(2.1,5))
    musica=[pared('piano_pared'),junto('banqueta_piano','piano_pared',lados=['frente'],mira_ref=True),pared('guitarra_soporte'),pared('guitarra_soporte',False,botin='guitarra'),pared('vb_altavoz'),pared('vb_altavoz',False,botin='altavoz'),pared('estanteria_libros',False),pared('vb_escritorio',False),E('sobre','vb_vinilos',en=['vb_escritorio'],cantidad=[0,1],botin='vinilos'),E('pared',['poster_enmarcado','cuadro_paisaje'],pared='*',cantidad=[1,3])]+adornos(papeles+['vb_vinilos','vb_partituras','vb_auriculares','vb_metronomo'],['vb_escritorio','estanteria_libros'])
    kit('musica','Cuarto de música','otra_estancia',musica,mood['musica'],fondo=(2.1,5))
    trofeos=[pared('vb_armero'),pared('vb_rifle',botin='rifle'),E('pared','vb_cornamenta',pared='*',cantidad=[2,4],obligatorio=True),pared('sillon_orejero'),pared('estanteria_libros',False),pared('vb_comoda',False),E('sobre','vb_prismaticos',en=['vb_comoda','estanteria_libros'],cantidad=[0,1],botin='prismaticos')]+adornos(libros+['vb_brujula','vb_linterna','vb_bolsa_caza','vb_prismaticos','libro_tumbado','reloj_sobremesa'],['vb_comoda','estanteria_libros'])
    kit('trofeos','Cuarto de trofeos del cazador','otra_estancia',trofeos,mood['trofeos'],fondo=(2.1,5))
    arte=['vb_paleta','vb_pinceles','vb_carboncillos','vb_acuarelas','vb_tubos_oleo','vb_trapo']+[k for k,o in C.items() if k.startswith('fe_pintura') and o['soporte']=='superficie']+libros+['lb_rotuladores','lb_papel_folios']
    pintura=[pared('vb_caballete'),pared('vb_escritorio'),junto('silla_comedor','vb_escritorio',True,lados=['frente'],mira_ref=True),pared('estanteria_libros',False),pared('vb_caballete',False,area_min=12),E('pared','cuadro_paisaje',pared='*',cantidad=[0,1],botin='cuadro'),E('pared',['cuadro_paisaje','poster_enmarcado'],pared='*',cantidad=[1,3])]+adornos(arte,['vb_escritorio','estanteria_libros'])
    kit('pintura','Estudio de pintura','otra_estancia',pintura,mood['pintura'],fondo=(2.1,5))

if __name__=='__main__':generar()
