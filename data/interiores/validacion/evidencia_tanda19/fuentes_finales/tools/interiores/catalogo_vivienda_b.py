"""Mobiliario doméstico de dormitorios y habitaciones personales, en metros."""
from vivienda_base import *

def modelos_estudio():
    """Frente adulto de trabajo/consulta: envolventes R2, materiales propios contenidos."""
    out=[];madera='#ae8962';canto='#8b674b';papel='#e5dcc8';azul='#637b86';oliva='#84907b'
    def b(w,h,d,**kw):return caja(w,h,d,redondeo=min(.006,min(w,h,d)/4),**kw)
    p=[b(1.30,.04,.60,y=.73,c=madera)]
    for x in [-.595,.595]:
        for z in [-.245,.245]:p.append(b(.045,.71,.045,x=x,y=.355,z=z,c=canto))
    for x in [-.595,.595]:p.append(b(.04,.47,.05,x=x,y=.985,z=-.265,c=canto))
    p.append(b(1.20,.38,.02,y=1.01,z=-.28,c='#b49672'))
    out.append(objeto('vb_puesto_estudio_amplio','Puesto adulto con respaldo de consulta',1.30,1.22,.60,'mesa',32,partes=p,superficies=[dict(y=.75,margen=.04,fondo=.24)]))
    # Biblioteca abierta: laterales finos, baldas reales y trasera ligera.
    p=[b(.95,1.64,.016,y=.85,z=-.162,c='#9b805f')]
    for x in [-.4875,.4875]:p.append(b(.025,1.70,.34,x=x,c=madera))
    for y in [.015,.400,.800,1.200,1.685]:p.append(b(1.,.03,.34,y=y,c=madera))
    # Consulta baja integrada: dos carpetas y un estuche cerrado, con apoyo real.
    p += [b(.57,.075,.27,x=-.16,y=.0675,z=.012,c='#9b8064',m='carton'),
          b(.50,.035,.25,x=-.16,y=.1225,z=.012,c=papel,m='papel')]
    for x,h,c in[(.22,.27,azul),(.31,.24,oliva),(.40,.29,'#a18b68')]:p.append(b(.06,h,.25,x=x,y=.03+h/2,z=.012,c=c,m='papel'))
    out.append(objeto('vb_biblioteca_estudio','Biblioteca abierta de consulta adulta',1.,1.70,.34,'libros',30,partes=p,superficies=[dict(y=y,margen=.035,fondo=.30)for y in [.415,.815,1.215]]))
    # Cajones entre el puesto y la biblioteca; cuerpo hueco, sin frentes superpuestos.
    p=[b(.90,.035,.35,y=.0175,c=canto),b(.90,.035,.35,y=.7625,c=madera)]
    for x in[-.435,.435]:p.append(b(.03,.71,.35,x=x,y=.39,c=madera))
    p.append(b(.84,.71,.018,y=.39,z=-.166,c=canto))
    for j in range(3):
        y=.15+j*.225
        p += [b(.84,.015,.32,y=.0425+j*.225,z=-.005,c=canto),
                  b(.3375,.20,.022,x=-.24375,y=y,z=.164,c='#bd9b73'),
                  b(.3375,.20,.022,x=.24375,y=y,z=.164,c='#bd9b73'),
                  b(.15,.18,.022,y=y-.01,z=.164,c='#bd9b73')]
    out.append(objeto('vb_guardado_estudio','Guardado bajo de cajones para el estudio',.90,.78,.35,'comoda',30,partes=p,superficies=[dict(y=.78,margen=.04)]))
    # Consulta por perfil: masas de libros/carpetas, no una fila comercial.
    for tema in ['estudiante','artista','musico']:
        if tema=='estudiante':
            p=[]
            for x,h,c in[(-.23,.25,azul),(-.17,.22,oliva),(-.11,.24,'#a18b68')]:p.append(b(.045,h,.21,x=x,y=h/2,z=-.01,c=c,m='papel'))
            p += [b(.28,.045,.25,x=.115,y=.0225,c='#bca17b',m='papel'),b(.25,.025,.21,x=.115,y=.0575,c=papel,m='papel')]
        elif tema=='artista':
            p=[b(.55,.035,.25,y=.0175,c=canto,m='carton'),b(.52,.022,.24,y=.046,c=papel,m='papel'),b(.46,.028,.23,x=-.015,y=.071,c='#a9b09a',m='carton')]
            for x,h in[(.14,.18),(.185,.25)]:p.append(b(.035,h,.18,x=x,y=.085+h/2,z=-.025,c=azul,m='papel'))
        else:
            p=[]
            for x,h,c in[(-.22,.25,canto),(-.14,.25,azul),(-.06,.23,oliva)]:
                p += [b(.06,h,.23,x=x,y=h/2,c=c,m='papel'),caja(.025,.09,.001,x=x,y=.14,z=.1155,c=papel,m='papel')]
            p += [b(.25,.025,.25,x=.14,y=.0125,c=papel,m='papel'),b(.23,.025,.22,x=.14,y=.0375,c='#9b8064',m='papel')]
        out.append(objeto('vb_consulta_estudio_'+tema,'Consulta adulta de '+tema,.55,.34,.25,None,1.8,'papel',partes=p,soporte='superficie',categoria='decoracion'))
        # Un único atlas propio: dos zonas de papel sobre el respaldo existente.
        p=[dict(f='caja',d=[1.10,.42,.001],p=[0,.21,-.0945],c='#b49672',m='papel',tex=dict(tipo='vivienda_consulta_estudio_b',tema=tema))]
        out.append(objeto('vb_panel_estudio_'+tema,'Notas de consulta de '+tema,1.10,.42,.001,None,.3,'papel',partes=p,soporte='superficie',categoria='cuadro'))
    p=[b(.45,.055,.27,y=.0275,c=canto,m='papel'),b(.38,.04,.23,y=.075,c=papel,m='papel'),b(.32,.025,.21,y=.1075,c=azul,m='papel')]
    out.append(objeto('vb_consulta_baja_estudio','Libros de consulta sobre el bajo',.45,.12,.27,'libros',5,'papel',partes=p,soporte='superficie',categoria='decoracion'))
    for old,id,nombre in [('silla_comedor','vb_silla_estudio','Silla de trabajo del estudio'),('sillon_orejero','vb_sillon_estudio','Sillón de lectura del estudio')]:
        o=copiar(old,id,nombre)
        for p in o['partes']:
            if p.get('tinte')=='tela':p['c']=azul if id=='vb_silla_estudio'else'#8b9380';p.pop('tinte')
            elif p.get('tinte')=='madera':p['c']=canto;p.pop('tinte')
        out.append(o)
    return out


def mejorar_trofeos(out):
    """Guardado de campo y consulta: superficies físicas y formas propias."""
    ids={o['id']:o for o in out};madera='#916e50';canto='#514332';verde='#596f60';lino='#b4b79d'
    def b(w,h,d,**kw):return caja(w,h,d,redondeo=min(.012,min(w,h,d)/4),**kw)
    ar=ids['vb_armero'];ar['nombre']='Armero de roble con vano y apoyo inferior'
    # El vano central queda libre desde la base hasta el remate; los travesaños
    # están detrás del rifle independiente. No hay un arma fundida en el soporte.
    ar['partes']=[b(.68,.12,.28,c=canto),b(.68,1.33,.025,y=.785,z=-.1275,c=madera),b(.68,.04,.28,y=1.47,c=canto)]
    for x in [-.3225,.3225]:ar['partes'].append(b(.035,1.31,.28,x=x,y=.785,c=madera))
    for y in [.68,1.10]:ar['partes'].append(b(.61,.04,.035,y=y,z=-.09,c=canto))
    ar['superficies']=[dict(y=.12,margen=.10)]
    p=[b(1.18,.05,.40,y=.085,c=canto),b(1.18,.045,.40,y=.8175,c=madera),b(1.11,.67,.022,y=.46,z=-.189,c=canto)]
    for x in [-.5725,.5725]:p.append(b(.035,.69,.40,x=x,y=.4625,c=madera))
    for x in [-.2875,.2875]:
        p += [b(.54,.30,.025,x=x,y=.625,z=.1875,c='#a17e58'),b(.54,.30,.025,x=x,y=.285,z=.1875,c='#a17e58')]
        for y in [.625,.285]:p.append(b(.12,.016,.026,x=x,y=y+.035,z=.213,c='#545d53',m='madera'))
    for x in [-.50,.50]:
        for z in [-.15,.15]:p.append(b(.055,.06,.055,x=x,y=.03,z=z,c=canto))
    out.append(objeto('vb_guardado_campo','Mueble bajo de equipo y consulta de campo',1.18,.84,.45,'comoda',35,partes=p,superficies=[dict(y=.84,margen=.04)]))
    # Ámbito real de equiparse: un asiento libre sobre banco zapatero abierto.
    # Botas y bolsa son parte del modelo propio; no sustituyen el botín suelto.
    p=[b(1.14,.045,.44,y=.4375,c=madera),b(1.10,.025,.40,y=.1125,c=canto),
       b(1.10,.29,.02,y=.275,z=-.205,c=canto)]
    for x in [-.535,.535]:
        for z in [-.165,.165]:p.append(b(.045,.415,.045,x=x,y=.2075,z=z,c=canto))
    p += [caja(.65,.045,.385,x=-.19,y=.4825,z=.008,c='#ad9060',m='tela',redondeo=.018),
          b(.025,.30,.38,x=.115,y=.275,c=madera)]
    # Par de botas con caña, interior oscuro del puño, puntera y suela; apoyadas en balda.
    for x in [.255,.425]:
        p += [caja(.125,.045,.24,x=x,y=.1475,z=.045,c='#3f4438',m='goma',redondeo=.015),
              caja(.115,.085,.22,x=x,y=.2025,z=.045,c='#6a7255',m='tela',redondeo=.025),
              caja(.105,.145,.105,x=x,y=.285,z=-.015,c='#667052',m='tela',redondeo=.02),
              caja(.075,.002,.075,x=x,y=.358,z=-.015,c='#30392e',m='tela',redondeo=.012)]
    # Bolsa sobre el extremo derecho; asa de dos montantes y travesaño unidos.
    p += [caja(.245,.19,.25,x=.405,y=.555,z=.005,c='#7c7255',m='tela',redondeo=.025),
          caja(.245,.045,.25,x=.405,y=.6325,z=.005,c='#927a56',m='tela',redondeo=.012)]
    for x in [.34,.47]:p.append(b(.018,.09,.025,x=x,y=.69,z=.005,c=canto))
    p.append(b(.148,.018,.025,x=.405,y=.726,z=.005,c=canto))
    out.append(objeto('vb_banco_equipo_campo','Banco zapatero para equiparse',1.14,.735,.44,'silla',20,
                      partes=p,modificadores=['SEAT'],asientos=[dict(p=[-.19,.505,.04],h=.505,anim='silla')],
                      nota='Un puesto libre para calzarse; botas en balda y bolsa integrada junto al asiento.'))
    # Dos cornamentas de escala doméstica: placa pequeña, astas con ramas y
    # curvatura escalonada. La geometría continúa a la altura de pared original.
    asta=[b(.21,.30,.025,y=1.665,z=.0125,c=canto)]
    for sign in [-1,1]:
        for x,y,h,a,rt,rb in [(.065,1.80,.16,-32,.015,.024),(.135,1.94,.18,-20,.010,.017),(.19,2.095,.17,-18,.004,.011)]:
            asta.append(cil(rt,rb,h,x=sign*x,y=y,z=.095,c='#dfd5b7',m='hueso',r=[0,0,sign*a],seg=9))
        for x,y,h,a in [(.09,1.85,.14,40),(.15,1.98,.13,38),(.192,2.075,.105,35)]:
            asta.append(cil(.003,.009,h,x=sign*x,y=y,z=.11,c='#dfd5b7',m='hueso',r=[0,0,sign*a],seg=8))
    asta.append(dict(f='esfera',d=[.06],p=[0,1.77,.065],s=[.78,1,.9],c='#dfd5b7',m='hueso'))
    ids['vb_cornamenta']['partes']=asta
    # Un orejero propio: la silla compartida de los otros cuartos no cambia.
    seat=copiar('sillon_orejero','vb_sillon_campo','Sillón de consulta de campo')
    seat['nota']='Tapizado mate, brazos curvos y patas de madera; asiento a 43 cm.'
    # Tapizado continuo sobre bastidor: radios visibles sin piezas esféricas
    # aisladas. Los montantes conservan la unión física del respaldo reclinado.
    def tap(w,h,d,**kw):return caja(w,h,d,redondeo=min(.065,min(w,h,d)/2),m='tela',c=verde,**kw)
    p=[b(.66,.13,.65,y=.335,z=.005,c=canto),
       tap(.59,.15,.56,y=.405,z=.035),
       tap(.62,.70,.16,y=.78,z=-.245,r=[-8,0,0])]
    for x in [-.18,.18]:p.append(b(.04,.59,.035,x=x,y=.685,z=-.30,c=canto))
    for sign in [-1,1]:
        p += [tap(.11,.25,.52,x=sign*.315,y=.42),
              tap(.14,.25,.64,x=sign*.315,y=.55,z=.01),
              tap(.12,.20,.16,x=sign*.29,y=.99,z=-.225)]
    for x in [-.27,.27]:
        for z in [-.27,.27]:p.append(b(.055,.27,.055,x=x,y=.135,z=z,c=canto))
    p.append(caja(.40,.24,.10,y=.66,z=-.135,c=lino,m='tela',redondeo=.04))
    # Manta de cuatro milímetros siguiendo el brazo y cayendo por el lateral.
    # Tiras unidas sobre dos cuartos de arco; no es un tablero horizontal grueso.
    import math
    def paño(a,b):
        dx,dy=b[0]-a[0],b[1]-a[1]
        return caja(math.hypot(dx,dy)+.001,.004,.28,x=(a[0]+b[0])/2,y=(a[1]+b[1])/2,z=.08,c='#b6a37f',m='tela',r=[0,0,math.degrees(math.atan2(dy,dx))])
    for cx,lo,hi in [(.305,math.pi,math.pi/2),(.325,math.pi/2,0)]:
        points=[(cx+.063*math.cos(lo+(hi-lo)*i/5),.615+.063*math.sin(lo+(hi-lo)*i/5))for i in range(6)]
        p.extend(paño(a,b)for a,b in zip(points,points[1:]))
    p += [paño((.305,.678),(.325,.678)),paño((.388,.615),(.388,.355))]
    seat['partes']=p;out.append(seat)
    out.append(mesa('vb_mesa_campo','Mesa auxiliar de consulta de campo',.48,.40,.55))
    p=[b(.66,1.30,.022,y=.67,z=-.139,c=canto)]
    for x in [-.338,.338]:p.append(b(.024,1.34,.30,x=x,c=madera))
    for y in [.03,.44,.88,1.328]:p.append(b(.70,.024,.30,y=y,c=madera))
    out.append(objeto('vb_biblioteca_campo','Biblioteca baja de consulta de campo',.70,1.34,.30,'libros',24,partes=p,superficies=[dict(y=y,margen=.03,fondo=.28) for y in [.452,.892]]))
    # Mesa central baja: una superficie de consulta delante del asiento,
    # con atlas propio abierto integrado y espacio libre para el libro recogible.
    p=[b(.90,.045,.55,y=.5975,c=madera)]
    for x in [-.395,.395]:
        for z in [-.22,.22]:p.append(b(.05,.575,.05,x=x,y=.2875,z=z,c=canto))
    p.append(b(.86,.04,.43,y=.18,c=canto))
    p.append(caja(.42,.006,.34,y=.623,c='#667c69',m='carton'))
    import math
    for sign in [-1,1]:
        angle=sign*math.radians(5);px=sign*.10
        p.append(caja(.196,.009,.32,x=px,y=.638,c='#e3dcc5',m='papel',r=[0,0,sign*5]))
        # Gráfico de campo propio en las páginas. Cada trazo sigue el giro del
        # papel y queda sobre su cara; no hay imágenes ni textos prestados.
        def pagina(lx,lz,w,d,col):
            sy=.0051
            return caja(w,.001,d,x=px+lx*math.cos(angle)-sy*math.sin(angle),y=.638+lx*math.sin(angle)+sy*math.cos(angle),z=lz,c=col,m='papel',r=[0,0,sign*5])
        if sign<0:
            p += [pagina(-.043,-.065,.062,.09,'#abb995'),pagina(.038,.045,.067,.11,'#c1ae86'),pagina(-.025,.045,.014,.14,'#829fa0')]
        else:
            p += [pagina(0,z,.12,.004,'#7c8a71')for z in [-.10,-.055,-.01,.035,.08]]
    out.append(objeto('vb_mesa_consulta_campo','Mesa baja de consulta con atlas abierto',.90,.65,.55,'mesa',18,partes=p,superficies=[dict(y=.62,margen=.04)]))
    # Esquema de campo propio: papel, parcelas, caminos y cauce. Son formas
    # originales, sin fotografías ni una ruta real presentada como cartografía.
    mapa=[caja(1.08,.76,.025,y=1.83,z=.0125,c=canto),caja(1.02,.70,.002,y=1.83,z=.026,c='#e2ddc8',m='papel')]
    for x,y,w,h,col in [(-.31,2.02,.27,.20,'#a7b69a'),(.13,2.04,.35,.16,'#b7b58d'),(-.29,1.67,.31,.15,'#c5b28e'),(.27,1.70,.25,.17,'#b5bf9b')]:
        mapa.append(caja(w,h,.001,x=x,y=y,z=.0275,c=col,m='papel'))
    def trazo(a,b,w,col):
        import math
        dx,dy=b[0]-a[0],b[1]-a[1]
        mapa.append(caja(math.hypot(dx,dy),w,.001,x=(a[0]+b[0])/2,y=(a[1]+b[1])/2,z=.029,c=col,m='papel',r=[0,0,math.degrees(math.atan2(dy,dx))]))
    for pa,pb in [((-.46,1.59),(-.17,1.78)),((-.17,1.78),(.17,1.92)),((.17,1.92),(.44,2.10)),((-.17,1.78),(-.34,2.12))]:trazo(pa,pb,.018,'#f6eed8')
    for pa,pb in [((-.08,2.14),(.015,1.95)),((.015,1.95),(.01,1.78)),((.01,1.78),(.18,1.51))]:trazo(pa,pb,.022,'#829fa0')
    for x,col in [(.27,'#a7b69a'),(.34,'#c5b28e'),(.41,'#829fa0')]:mapa.append(caja(.04,.025,.001,x=x,y=1.53,z=.029,c=col,m='papel'))
    out.append(objeto('vb_mapa_campo','Esquema de caminos de campo para consulta',1.08,.76,.03,None,1.5,'papel',partes=mapa,soporte='pared',categoria='cuadro'))
    # Prismáticos con dos cuerpos y oculares; bolsa con solapa, base y asa.
    ids['vb_prismaticos']['partes']=[b(.055,.05,.105,x=x,y=.035,c='#47594d',m='plastico')for x in [-.0375,.0375]]+[b(.03,.025,.045,y=.04,c='#66735b',m='plastico')]
    for x in [-.0375,.0375]:
        ids['vb_prismaticos']['partes'] += [cil(.023,.023,.015,x=x,y=.035,z=.06,c='#52696b',m='plastico',r=[90,0,0],seg=12),cil(.017,.017,.013,x=x,y=.035,z=-.061,c='#303f3c',m='plastico',r=[90,0,0],seg=12)]
    for p in ids['vb_prismaticos']['partes']:p['p'][1]-=.01
    ids['vb_bolsa_caza']['partes']=[b(.26,.145,.15,y=.0725,c='#8e7953',m='tela'),b(.27,.035,.16,y=.155,c='#a79168',m='tela'),b(.21,.07,.012,y=.125,z=.080,c='#a79168',m='tela'),b(.028,.04,.008,y=.12,z=.091,c='#5b6351',m='metal')]
    for x in [-.055,.055]:ids['vb_bolsa_caza']['partes'].append(b(.014,.03,.02,x=x,y=.18,c=canto))
    ids['vb_bolsa_caza']['partes'].append(b(.124,.014,.02,y=.202,c=canto))


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
    # Variantes infantiles: conservan roles y la cama original de 85 × 182 cm.
    # No se escalan ni recolorean los muebles compartidos de los otros dormitorios.
    cama=copy.deepcopy(next(o for o in out if o['id']=='vb_cama_individual'))
    cama['id']='vb_cama_ninos';cama['nombre']='Cama individual con cajones bajos'
    # El zócalo se retranquea; colchón, cabecero y huella total siguen iguales.
    cama['partes'][0]['d'][0]=.81
    for p in cama['partes']:
        if p.get('tinte')=='tela':p.pop('tinte');p['c']='#7c9b99'
    for lado in [-1,1]:
        for z in [-.44,.44]:
            cama['partes'] += [caja(.014,.15,.78,x=lado*.412,y=.23,z=z,c='#d4bd98'),caja(.012,.025,.12,x=lado*.419,y=.23,z=z,c='#697e77')]
    # Cobertor de cinco paños disjuntos dentro del volumen ya validado.
    # Las bandas toman la tela de la casa; ni huella ni altura cambian.
    cama['partes'][1]['c']='#d9d3c2'
    colcha=cama['partes'].pop(3);z=colcha['p'][2]-colcha['d'][2]/2
    for i,largo in enumerate([.46,.06,.23,.06,.34]):
        p=copy.deepcopy(colcha);p['d'][2]=largo;p['p'][2]=z+largo/2
        if i%2:p['c']='#d9cba6';p.pop('tinte',None)
        else:p['c']='#567c91';p['tinte']='tela'
        cama['partes'].insert(3+i,p);z+=largo
    out.append(cama)
    # Una sola galería de dibujos propios sobre el descanso, no una pared de pósters.
    laminas=[]
    for i,(x,y) in enumerate([(-.26,1.43),(0,1.48),(.26,1.43)]):
        laminas += [caja(.235,.315,.003,x=x,y=y,z=.0015,c='#d6cfba',m='papel'),
                    dict(f='plano',d=[.23,.31],p=[x,y,.0035],c='#e9dfc9',m='papel',tex=dict(tipo='vivienda_dibujo_ninos_b',lamina=i)),
                    caja(.055,.02,.001,x=x-.045,y=y+.153,z=.0045,c='#b6ad90',m='papel')]
    out.append(objeto('vb_dibujos_ninos','Dibujos infantiles guardados en la pared',.76,.37,.005,None,.3,'papel',partes=laminas,soporte='pared',categoria='cuadro'))
    # Mismo volumen y regla de la alfombra de dormitorio; sólo cambia su superficie.
    juego=copy.deepcopy(next(o for o in out if o['id']=='vb_alfombra'))
    juego['id']='vb_alfombra_juego';juego['nombre']='Alfombra de juego con circuito'
    juego['partes'][0].pop('tinte',None);juego['partes'][0]['c']='#647b78'
    juego['partes'][1]['tex']=dict(tipo='vivienda_juego_ninos_b')
    out.append(juego)
    # Una huella de juego proporcionada también a los dormitorios estrechos.
    # Misma textura propia y dos piezas de la alfombra grande; no hay juguetitos nuevos.
    compacta=copy.deepcopy(juego)
    compacta['id']='vb_alfombra_juego_compacta';compacta['nombre']='Alfombra compacta de juego con circuito'
    for pieza in compacta['partes']:
        pieza['d'][0]*=1.2/1.8;pieza['p'][0]*=1.2/1.8
        pieza['d'][2]*=.85/1.3;pieza['p'][2]*=.85/1.3
    out.append(compacta)
    # Banco infantil de lectura: asiento de 90 × 32 cm a 40 cm y guardado bajo real.
    # Cada tablero apoya en el inferior; el asiento puentea laterales y división.
    # Dos cajas textiles integradas, sin superficies para acumular adornos.
    p=[caja(.9,.035,.32,y=.0175,c='#c6b28d')]
    for x in [-.435,.435]:p.append(caja(.03,.30,.32,x=x,y=.185,c='#c6b28d'))
    p += [caja(.84,.30,.025,y=.185,z=-.1475,c='#8b7965'),
          caja(.025,.30,.295,y=.185,z=.0125,c='#c6b28d'),
          caja(.9,.065,.32,y=.3675,c='#567c91',m='tela')]
    for x in [-.21625,.21625]:p.append(caja(.33,.22,.25,x=x,y=.145,z=.0125,c='#a4b1a0',m='tela'))
    out.append(objeto('vb_banco_lectura_ninos','Banco de lectura con dos cajas de guardado',.9,.4,.32,'sillon',18,
                      partes=p,asientos=[dict(p=[0,0,.015],h=.4,anim='banco')]))
    # Armario bajo de ropa: cuerpo de 95 × 42 × 150 cm, no una cómoda.
    p=[caja(.95,1.5,.42,c='#cbb591')]
    for x in [-.2345,.2345]:
        p += [caja(.451,1.40,.014,x=x,y=.77,z=.217,c='#879e91'),caja(.018,.13,.025,x=x*.18,y=.83,z=.236,c='#d6d0bb',m='metal')]
    out.append(objeto('vb_armario_ninos','Armario infantil de ropa',.95,1.5,.45,'armario',48,partes=p))
    # Dos baldas accesibles, huecos para cuentos y cajas integradas bajo la superior.
    p=[caja(.88,.76,.022,z=-.139,c='#cbb591')]
    for x in [-.428,.428]:p.append(caja(.024,.76,.3,x=x,c='#cbb591'))
    for y in [.04,.38,.748]:p.append(caja(.88,.024,.3,y=y,c='#cbb591'))
    for x in [-.22,.22]:
        p += [caja(.34,.22,.24,x=x,y=.162,z=.012,c='#a4b1a0',m='tela'),caja(.09,.025,.008,x=x,y=.24,z=.136,c='#677e78')]
    out.append(objeto('vb_estante_ninos','Guardado bajo de cuentos y juegos',.88,.76,.3,'libros',20,partes=p,superficies=[dict(y=.76,margen=.025)]))
    # Biblioteca exclusiva: cuentos y juego junto al puesto, en dos niveles reales.
    # La caja inferior izquierda guarda piezas; el hueco inferior derecho queda libre.
    p=[caja(.92,1.34,.018,z=-.141,c='#8b7965')]
    for x in [-.448,.448]:p.append(caja(.024,1.34,.30,x=x,c='#c6b28d'))
    for y in [.028,.468,.918,1.328]:p.append(caja(.92,.024,.30,y=y,c='#c6b28d'))
    p += [caja(.024,.416,.30,y=.26,c='#c6b28d'),
          caja(.34,.27,.24,x=-.225,y=.175,z=.014,c='#718f96',m='tela'),
          caja(.09,.025,.008,x=-.225,y=.25,z=.138,c='#c2b79f',m='tela')]
    out.append(objeto('vb_biblioteca_ninos','Biblioteca infantil de cuentos y juegos',.92,1.34,.30,'libros',23,partes=p,
                      superficies=[dict(y=.48,margen=.035,fondo=.28),dict(y=.93,margen=.035,fondo=.28)]))
    # Dos pertenencias compuestas propias, misma envolvente; pocas masas legibles.
    # Cada una ocupa menos de 2/3 de la balda, sin dibujos de una falsa biblioteca.
    p=[caja(.26,.07,.21,x=.13,y=.035,c='#ae8967',m='carton')]
    for x,h,c in [(-.20,.24,'#567c91'),(-.14,.20,'#be9a65'),(-.08,.22,'#8b9a78')]:
        p.append(caja(.045,h,.17,x=x,y=h/2,z=-.012,c=c,m='papel'))
    p.append(caja(.23,.018,.18,x=.13,y=.079,c='#75938c',m='madera'))
    out.append(objeto('vb_cuentos_biblioteca','Cuentos y caja de construcciones',.48,.24,.21,None,1.8,'papel',partes=p,soporte='superficie',categoria='decoracion'))
    # La caja alcanza la base real del cuaderno: contacto a y=.216, sin aire.
    p=[caja(.28,.216,.21,x=-.0825,y=.108,c='#75938c',m='carton'),
       caja(.26,.024,.18,x=-.0825,y=.228,c='#be9a65',m='papel'),
       caja(.19,.025,.21,x=.165,y=.0125,c='#ae7868',m='papel'),
       caja(.18,.025,.18,x=.165,y=.0375,c='#c7b58c',m='papel'),
       caja(.08,.10,.08,x=.13,y=.10,c='#718f96',m='madera'),
       caja(.06,.045,.04,x=.13,y=.1725,c='#b99b70',m='madera')]
    out.append(objeto('vb_hacer_biblioteca','Cuadernos y caja de dibujo y manualidades',.48,.24,.21,None,1.8,'papel',partes=p,soporte='superficie',categoria='decoracion'))
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
    out.extend(modelos_estudio())
    mejorar_trofeos(out)
    return out

if __name__=='__main__':guardar_catalogo('vivienda_b',objetos())
