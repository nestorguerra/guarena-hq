"""Mobiliario doméstico de dormitorios y habitaciones personales, en metros."""
from vivienda_base import *

def objetos():
    out=[]
    for id,nombre,w,rol in [('vb_cama_doble','Cama de matrimonio compacta',1.35,'cama_doble'),('vb_cama_individual','Cama individual',.85,'cama')]:
        p=[caja(w,.22,1.82,y=.2,tinte='madera'),caja(w-.03,.17,1.79,y=.395,c='#d2bca4',m='tela',tinte='tela'),caja(w,.65,.055,y=.325,z=-.883,tinte='madera'),caja(w-.04,.035,1.15,y=.497,z=.29,c='#997f95',m='tela',tinte='tela')]
        for x in [-w/2+.09,w/2-.09]:
            for z in [-.75,.75]:p.append(caja(.075,.15,.075,x=x,y=.075,z=z,tinte='madera'))
        for x in ([-w/4,w/4] if rol=='cama_doble' else [0]):p.append(caja(w/2-.12 if rol=='cama_doble' else w-.14,.1,.35,x=x,y=.53,z=-.58,c='#e4decf',m='tela'))
        out.append(objeto(id,nombre,w,.68,1.82,rol,52,partes=p))
    # Variante de cama para habitaciones amplias, sin agrandar la de los dormitorios estrechos.
    c=copy.deepcopy(out[0]);c['id']='vb_cama_amplia';c['nombre']='Cama de matrimonio amplia'
    for p in c['partes']:p['d'][0]*=1.6/1.35;p['p'][0]*=1.6/1.35
    out.append(c)
    out.append(objeto('vb_armario','Armario de dos puertas',.8,1.85,.4,'armario',55,partes=[caja(.8,1.85,.4,tinte='madera'),caja(.008,.18,.02,x=-.04,y=1,z=.215,c=METAL,m='metal'),caja(.008,.18,.02,x=.04,y=1,z=.215,c=METAL,m='metal')]))
    out.append(objeto('vb_alfombra','Alfombra de dormitorio',1.8,.012,1.3,None,3,partes=[caja(1.8,.012,1.3,c='#958273',m='tela',tinte='tela'),caja(1.65,.002,1.15,y=.013,c='#bba584',m='tela')],categoria='textil'))
    out.append(cajonera('vb_mesita','Mesita de noche',.32,.5,.28,'mesa',8))
    out.append(cajonera('vb_comoda','Cómoda con cajones'))
    out.append(mesa('vb_escritorio','Escritorio doméstico',.95,.45))
    out.append(mesa('vb_mesa_ninos','Mesa para deberes y juegos',.8,.42,.64))
    out.append(copiar('silla_comedor','vb_silla_ninos','Silla infantil','silla',.84))
    out.append(copiar('estanteria_libros','vb_estante_bajo','Estantería baja para cuentos y juguetes','libros',.65))
    out.append(objeto('vb_ordenador','Ordenador doméstico sin marca',.38,.31,.22,None,2,'plastico',partes=[caja(.38,.24,.025,y=.19,z=-.06,c='#57616c',m='plastico'),caja(.34,.2,.005,y=.19,z=-.044,c='#8aabc1',m='cristal'),caja(.04,.08,.04,y=.04,z=-.06,c='#81878e',m='metal'),caja(.32,.018,.13,y=.009,z=.04,c='#69747e',m='plastico')],soporte='superficie',categoria='informatica'))
    out.append(objeto('vb_caballete','Caballete con lienzo pintado',.72,1.65,.48,None,7,partes=[caja(.045,1.6,.045,x=-.26,y=.8,z=.13,r=[0,0,-8]),caja(.045,1.6,.045,x=.26,y=.8,z=.13,r=[0,0,8]),caja(.05,1.4,.05,y=.7,z=-.18),caja(.72,.045,.12,y=.72,z=.12),dict(f='plano',d=[.62,.54],p=[0,1.05,.19],c='#e8d4b4',m='tela',tex=dict(tipo='vivienda_lienzo_b'))]))
    out.append(objeto('vb_rifle','Rifle de caza guardado',.12,1.12,.08,None,3.5,'madera',partes=[caja(.09,.34,.045,y=.17,c='#825a3d',m='madera'),caja(.045,.4,.04,y=.52,c='#6b747c',m='metal'),cil(.012,.012,.45,y=.895,c='#697078',m='metal')],categoria='decoracion'))
    out.append(objeto('vb_armero','Soporte doméstico para armas',.55,1.25,.23,None,14,partes=[caja(.55,.1,.23),caja(.55,1.25,.04,z=-.095),caja(.55,.05,.17,y=.7),caja(.55,.05,.17,y=1.13)]))
    astas=[caja(.22,.3,.035,y=1.65,z=.0175)]
    for lado in [-1,1]:
        astas += [cil(.012,.024,.31,x=lado*.11,y=1.82,z=.09,c='#c6b797',m='hueso',r=[0,0,-lado*27]),cil(.008,.015,.23,x=lado*.19,y=2.03,z=.1,c='#c6b797',m='hueso',r=[0,0,-lado*9])]
        for x,y,ang in [(.13,1.91,-35),(.2,2.04,40),(.21,2.13,-40)]:
            astas.append(cil(.004,.011,.12,x=lado*x,y=y,z=.105,c='#c6b797',m='hueso',r=[0,0,lado*ang]))
    out.append(objeto('vb_cornamenta','Trofeo de caza en tabla',.55,.7,.18,None,3,'madera',partes=astas,soporte='pared',categoria='decoracion'))
    out.append(objeto('vb_altavoz','Altavoz doméstico',.25,.42,.23,None,5,'madera',partes=[caja(.25,.42,.23,c='#4b505a'),cil(.085,.085,.015,y=.15,z=.122,c='#89929a',m='metal',r=[90,0,0]),cil(.04,.04,.015,y=.33,z=.122,c='#89929a',m='metal',r=[90,0,0])],categoria='mueble'))
    for id,nombre,w,h,d,forma in [('vinilos','Discos de vinilo',.3,.035,.3,'cil'),('partituras','Partituras abiertas',.3,.015,.23,'caja'),('auriculares','Auriculares',.18,.07,.16,'cil'),('metronomo','Metrónomo',.075,.17,.085,'caja'),('paleta','Paleta con pinturas',.23,.025,.16,'cil'),('pinceles','Bote con pinceles',.07,.23,.07,'cil'),('carboncillos','Caja de carboncillos',.17,.025,.055,'caja'),('acuarelas','Estuche de acuarelas',.2,.025,.12,'caja'),('tubos_oleo','Tubos de óleo',.18,.035,.1,'caja'),('trapo','Trapo de pintura',.21,.02,.15,'caja'),('prismaticos','Prismáticos',.14,.07,.13,'caja'),('brujula','Brújula',.065,.025,.065,'cil'),('linterna','Linterna',.06,.16,.06,'cil'),('bolsa_caza','Bolsa de campo',.27,.2,.16,'caja')]:
        p=[cil(w/2,w/2,h,c='#777d86') if forma=='cil' else caja(w,h,d,c='#a1846b')]
        if id=='pinceles':p=[cil(.035,.035,.1,c='#9b7856',m='madera')]+[cil(.003,.003,.18,x=x,y=.17,c='#bd9a69',m='madera') for x in [-.02,0,.02]]
        if id=='paleta':p+=[cil(.025,.025,.005,x=x,y=.028,c=c,m='pintura') for x,c in [(-.06,'#b85f55'),(0,'#6e9a74'),(.06,'#6186a6')]]
        out.append(objeto('vb_'+id,nombre,w,h,d,None,.5,'madera',partes=p,soporte='superficie',categoria='decoracion'))
    for id,nombre,w,h,d,c in [('despertador','Despertador',.13,.11,.05,'#a19881'),('joyero','Joyero',.18,.07,.11,'#886249'),('hucha','Hucha',.11,.12,.09,'#d2959d'),('gafas','Gafas en su funda',.16,.03,.065,'#665e54'),('zapatillas','Zapatillas',.2,.055,.22,'#6f8995'),('ropa','Ropa doblada',.25,.1,.19,'#a6aca0'),('colcha','Colcha doblada',.32,.085,.25,'#9a7f9c'),('cuaderno','Cuaderno y lápiz',.19,.025,.24,'#bca886'),('cesto','Cesto pequeño',.22,.15,.18,'#a88e63'),('cargador','Cargador y cable',.07,.025,.08,'#555c62')]:
        o=objeto('vb_'+id,nombre,w,h,d,masa=.4,categoria='decoracion',partes=[caja(w,h,d,c=c,m='tela')]);o['soporte']='superficie';out.append(o)
    out.append(objeto('vb_plafon','Plafón doméstico',.38,.12,.38,None,2,'cristal',partes=[cil(.18,.18,.025,y=-.0125,c='#9c9fa4',m='metal'),cil(.17,.14,.09,y=-.07,c='#eee8db',m='cristal',luz=True)],soporte='techo',clase='FIXED',motivo_fijo='anclado en la realidad',categoria='lampara'))
    out.append(objeto('vb_lampara_trabajo','Lámpara lineal de trabajo',.8,.13,.18,None,2,'metal',partes=[caja(.8,.035,.18,y=-.0175,c='#9c9fa4',m='metal'),caja(.73,.07,.13,y=-.07,c='#eee8db',m='cristal',luz=True)],soporte='techo',clase='FIXED',motivo_fijo='anclado en la realidad',categoria='lampara'))
    osito=[dict(f='esfera',d=[.07],p=[0,.11,0],c='#b48d69',m='tela',s=[1,1.2,.85]),dict(f='esfera',d=[.055],p=[0,.21,0],c='#b48d69',m='tela')]
    for lado in [-1,1]:
        osito.extend([dict(f='esfera',d=[.023],p=[lado*.043,.25,0],c='#b48d69',m='tela'),dict(f='esfera',d=[.032],p=[lado*.055,.032,.025],c='#a47c58',m='tela'),dict(f='esfera',d=[.006],p=[lado*.018,.222,.048],c='#34363a',m='plastico')])
    osito.append(dict(f='esfera',d=[.013],p=[0,.203,.053],c='#6f5648',m='tela'))
    out.append(objeto('vb_osito','Osito de peluche',.18,.28,.14,None,.25,'tela',partes=osito,soporte='superficie',categoria='decoracion'))
    out.append(objeto('vb_bloques','Bloques de construcción de colores',.22,.13,.17,None,.35,'madera',partes=[caja(.07,.07,.07,x=-.07,y=.035,c='#ba645c'),caja(.07,.12,.07,y=.06,c='#799aaa'),caja(.07,.07,.07,x=.07,y=.035,c='#bda15f')],soporte='superficie',categoria='decoracion'))
    from composicion_domestica import mejorar_despacho
    mejorar_despacho(out)
    return out

if __name__=='__main__':guardar_catalogo('vivienda_b',objetos())
