"""Mobiliario doméstico funcional de cocina, baño y estancias de servicio. El script es el modelo."""
from vivienda_base import *

def objetos():
    out=[]
    p=[caja(1.18,.85,.5,c='#b58d63',tinte='madera'),caja(1.2,.04,.52,y=.87,c='#b9b4a8',m='piedra'),caja(.48,.012,.4,x=-.3,y=.896,c='#41454a',m='metal')]
    for x in [-.42,-.18]:
        for z in [-.11,.11]:p.append(cil(.075,.075,.018,x=x,y=.91,z=z,c='#8d9296'))
    p += [caja(.38,.014,.32,x=.28,y=.899,c=METAL,m='metal'),caja(.27,.012,.22,x=.28,y=.908,c='#7e9299',m='metal'),cil(.012,.012,.23,x=.28,y=1.015,z=-.18),caja(.025,.025,.15,x=.28,y=1.12,z=-.115,c=METAL,m='metal'),caja(.42,.38,.016,x=-.3,y=.43,z=.259,c='#59616a',m='cristal'),caja(.35,.025,.03,x=-.3,y=.66,z=.275,c=METAL,m='metal'),caja(.48,.72,.018,x=.3,y=.43,z=.259,tinte='madera'),caja(.15,.018,.03,x=.3,y=.76,z=.28,c=METAL,m='metal')]
    out.append(objeto('va_cocina','Cocina con fregadero y fogones',1.2,1.14,.52,'cocina',48,partes=p,superficies=[dict(y=.89,margen=.08,ancho=.15,fondo=.42)]))
    out.append(cajonera('va_encimera','Módulo de preparación de cocina',.65,.89,.5,'mesa',24))
    alacena=cajonera('va_alacena','Alacena de cocina',.65,1.65,.3,'armario',35)
    alacena['partes']=[caja(.65,1.65,.025,z=-.1375,tinte='madera'),caja(.025,1.65,.3,x=-.3125,tinte='madera'),caja(.025,1.65,.3,x=.3125,tinte='madera'),caja(.65,.025,.3,y=.0125,tinte='madera')]+[caja(.6,.025,.28,y=y,tinte='madera') for y in [.4,.8,1.2,1.65]]
    alacena['superficies']=[dict(y=y+.0125,margen=.025,fondo=.25) for y in [.4,.8,1.2,1.65]]
    out.append(objeto('va_nevera','Nevera doméstica',.52,1.55,.52,'nevera',55,'metal',partes=[caja(.52,1.55,.52,c=BLANCO,m='metal'),caja(.012,.5,.025,x=.21,y=1.05,z=.275,c=METAL,m='metal'),caja(.49,.015,.015,y=1.14,z=.264,c='#747779',m='metal')]))
    out.append(alacena)
    out.append(objeto('va_lavadora','Lavadora doméstica',.53,.84,.5,None,48,'metal',partes=[caja(.53,.84,.5,c=BLANCO,m='metal'),cil(.16,.16,.025,y=.42,z=.26,c='#66747b',m='cristal',r=[90,0,0])],superficies=[dict(y=.84,margen=.03)]))
    out.append(objeto('va_lavabo','Lavabo con mueble y grifo',.52,.95,.39,None,28,partes=[caja(.48,.72,.35,c='#a8b6af'),caja(.52,.06,.39,y=.75,c=BLANCO,m='ceramica'),caja(.31,.008,.24,y=.784,c='#79929d',m='ceramica'),cil(.012,.012,.17,y=.865,z=-.15),caja(.025,.025,.11,y=.94,z=-.11,c=METAL,m='metal'),caja(.2,.014,.025,y=.64,z=.19,c=METAL,m='metal')],superficies=[dict(y=.78,margen=.03)]))
    out.append(copiar('inodoro','va_inodoro','Inodoro doméstico'))
    out.append(objeto('va_ducha','Ducha con mampara lateral',.65,2.05,.65,None,38,'ceramica',partes=[caja(.65,.06,.65,c=BLANCO,m='ceramica'),cil(.025,.025,.005,y=.063,c='#76858d'),cil(.009,.009,1.8,y=1.05,z=-.3,c=METAL),cil(.08,.08,.018,y=1.96,z=-.24,c=METAL),caja(.2,.04,.05,y=1.04,z=-.28,c=METAL,m='metal'),caja(.012,1.82,.6,x=-.315,y=.97,c='#a0bdc6',m='cristal'),caja(.018,1.86,.025,x=-.315,y=.99,z=.3,c=METAL,m='metal')]))
    out.append(objeto('va_armario_bano','Armario estrecho del baño',.4,1.4,.25,None,14,superficies=[dict(y=1.4,margen=.03)]))
    out.append(objeto('va_espejo','Espejo del lavabo',.42,.55,.025,'espejo',3,material='cristal',categoria='decoracion',partes=[caja(.42,.55,.025,y=1.5,z=.0125,c='#879ba4',m='metal'),caja(.46,.025,.035,y=1.2,z=.0175,c=BLANCO,m='ceramica')],soporte='pared'))
    out.append(objeto('va_toallero','Toallero con toalla',.38,.42,.07,None,1,categoria='decoracion',partes=[caja(.38,.025,.05,y=1.15,z=.025,c=METAL,m='metal'),caja(.28,.38,.018,y=.98,z=.055,c='#729a9a',m='tela',tinte='tela')],soporte='pared'))
    out.append(copiar('portarrollos','va_papel','Papel higiénico en su soporte'))
    out.append(mesa('va_mesa_comedor','Mesa de comedor familiar',1.05,.7))
    out.append(copiar('estanteria_libros','va_estante','Estante de despensa y trastero',escala=.75))
    out[-1].pop('rol',None)
    out.append(objeto('va_alto_cocina','Armario alto sobre encimera',.56,.5,.25,None,12,partes=[caja(.56,.5,.25,y=1.65,z=.125,tinte='madera'),caja(.18,.015,.025,y=1.44,z=.26,c=METAL,m='metal')],soporte='pared'))
    out.append(objeto('va_banera','Bañera doméstica',1.45,.58,.67,None,65,'ceramica',partes=[caja(1.45,.5,.67,c=BLANCO,m='ceramica'),caja(1.28,.014,.49,y=.51,c='#88a3ae',m='ceramica'),caja(1.47,.045,.06,y=.53,z=-.31,c=BLANCO,m='ceramica'),caja(1.47,.045,.06,y=.53,z=.31,c=BLANCO,m='ceramica'),cil(.012,.012,.15,x=-.6,y=.56,z=-.23)],categoria='mueble'))
    out.append(objeto('va_cesto_ropa','Cesto de ropa sucia',.38,.56,.32,None,3,partes=[caja(.38,.56,.32,c='#b79d73',m='tela'),caja(.3,.06,.24,y=.57,c='#9caaa4',m='tela')],categoria='mueble'))
    banco=copiar('tal_banco_trabajo','va_banco','Banco de bricolaje doméstico',escala=.65);out.append(banco)
    costura=mesa('va_costura','Mesa con máquina de coser',.9,.45)
    costura['partes'] += [caja(.32,.025,.19,y=.775,c='#525b62',m='metal'),caja(.09,.23,.17,x=.12,y=.9,c='#565b60',m='metal'),caja(.31,.065,.16,y=1.015,c='#565b60',m='metal'),caja(.045,.13,.1,x=-.13,y=.94,c='#565b60',m='metal'),cil(.008,.008,.055,x=-.13,y=.845,c=METAL),cil(.055,.055,.025,x=.18,y=.94,c=METAL,r=[0,0,90])]
    out.append(costura)
    out.append(objeto('va_caja_almacen','Caja de almacenaje doméstico',.45,.33,.35,None,6,'papel',partes=[caja(.45,.33,.35,c='#ae895a',m='papel'),caja(.06,.335,.355,c='#c6b18e',m='papel'),caja(.18,.07,.002,y=.2,z=.177,c='#ded5bd',m='papel')],categoria='mueble'))
    out.append(objeto('va_cajas_apiladas','Cajas y baúl guardados',.6,1.05,.45,None,18,'papel',partes=[caja(.6,.36,.45,c='#967956',m='madera'),caja(.52,.31,.4,y=.515,c='#b99a71',m='papel'),caja(.43,.35,.36,y=.845,c='#af8d60',m='papel'),caja(.58,.03,.015,y=.2,z=.234,c='#8b9298',m='metal'),caja(.13,.06,.004,y=.82,z=.184,c='#d9ceb5',m='papel')]))
    out.append(objeto('va_tinaja','Tinaja de despensa con tapa',.45,.75,.45,None,22,'ceramica',partes=[cil(.17,.22,.62,y=.31,c='#a8774f',m='ceramica'),cil(.16,.17,.11,y=.675,c='#a8774f',m='ceramica'),cil(.18,.18,.025,y=.7425,c='#926c48',m='madera')]))
    out.append(copiar('estanteria_libros','va_estante_alto','Estantería alta doméstica'))
    out[-1].pop('rol',None)
    # Costura: siluetas distintas, no duplicados de catálogo para completar un mínimo.
    for i,(id,nombre,w,h,d) in enumerate([('tijeras','Tijeras de costura',.17,.018,.08),('cinta_metrica','Cinta métrica enrollada',.07,.03,.07),('alfiletero','Alfiletero',.08,.06,.08),('botones','Caja de botones',.14,.035,.1),('agujas','Estuche de agujas',.1,.012,.05),('patrones','Patrones de papel',.24,.012,.3),('dedal','Dedal',.018,.025,.018),('tela_lino','Lino doblado',.28,.06,.2),('tela_algodon','Algodón doblado',.25,.045,.18),('retales','Cesta de retales',.28,.18,.2),('bastidor','Bastidor de bordado',.2,.025,.2),('cierre','Cremalleras',.18,.015,.05),('caja_hilos','Caja de hilos',.2,.065,.16),('ovillo','Ovillo de lana',.1,.1,.1)]):
        p=[caja(w,h,d,c=['#7d9ca4','#b99374','#9884a4','#9caa86'][i%4],m='tela')]
        if id=='alfiletero':
            for x in [-.025,0,.025]:p.append(cil(.002,.002,.04,x=x,y=.075,c=METAL))
        if id=='tijeras':p=[caja(.15,.007,.018,y=.01,c=METAL,m='metal',r=[0,20,0]),caja(.15,.007,.018,y=.01,c=METAL,m='metal',r=[0,-20,0]),cil(.018,.018,.008,x=-.07,y=.01,z=.025,c='#6c7e8c')]
        out.append(objeto('va_'+id,nombre,w,h,d,None,.2,'tela',partes=p,categoria='decoracion',soporte='superficie'))
    for i,col in enumerate(['#b85f55','#678ca6','#ba9d5c','#697e64','#a68aa9','#d6c4a2']):
        out.append(objeto('va_hilo_'+str(i),'Carrete de hilo '+['rojo','azul','ocre','verde','violeta','beige'][i],.045,.075,.045,None,.06,'tela',partes=[cil(.025,.025,.008,y=.004,c='#c4a87e',m='madera'),cil(.018,.018,.065,y=.037,c=col,m='tela'),cil(.025,.025,.008,y=.073,c='#c4a87e',m='madera')],categoria='decoracion',soporte='superficie'))
    # Objetos pequeños: cada uno tiene una silueta y uso doméstico, sin envases de marca.
    for id,nombre,w,h,d,mat,col in [
      ('cepillero','Vaso con cepillos',.09,.16,.09,'ceramica','#779bad'),('dentifrico','Tubo de dentífrico',.045,.15,.035,'plastico','#cbdad2'),
      ('jabonera','Jabonera',.13,.025,.09,'ceramica','#ccb9aa'),('pastilla_jabon','Pastilla de jabón',.09,.025,.055,'comida','#dfc5ab'),
      ('peine','Peine',.16,.012,.035,'plastico','#5b4840'),('maquinilla','Maquinilla de afeitar',.045,.018,.14,'plastico','#596c78'),
      ('afeitado','Espuma de afeitar',.055,.18,.055,'metal','#85a698'),('esponja','Esponja de baño',.12,.07,.09,'tela','#d6b478'),
      ('algodon','Algodón en tarro',.09,.12,.09,'cristal','#d7dfdf'),('bastoncillos','Caja de bastoncillos',.1,.07,.08,'plastico','#b4c8d0'),
      ('toalla','Toalla doblada',.28,.07,.2,'tela','#7da1a3'),('toalla_manos','Toalla de manos',.2,.04,.15,'tela','#c9ad85'),
      ('secador','Secador',.2,.12,.1,'plastico','#6b6667'),('cortaunas','Cortaúñas',.02,.014,.065,'metal','#abb0b2'),
      ('panuelos','Caja de pañuelos',.2,.09,.11,'papel','#b7c0af'),('colonia','Colonia doméstica',.07,.15,.045,'cristal','#c8bd95'),
      ('desodorante','Desodorante',.055,.17,.055,'plastico','#a9bbc7'),('crema','Tarro de crema',.08,.055,.08,'plastico','#dfd2b2'),
      ('locion','Loción corporal',.07,.21,.045,'plastico','#c2cba6'),('sales','Tarro de sales',.08,.14,.08,'cristal','#d5c0be'),
      ('hilo_dental','Hilo dental',.05,.035,.025,'plastico','#dce2d5'),('cepillo_pelo','Cepillo del pelo',.06,.035,.18,'madera','#947457'),
      ('gorro','Gorro de ducha',.12,.025,.1,'tela','#b3c1b2'),('cosmeticos','Neceser cerrado',.21,.12,.09,'tela','#8c6977'),
      ('gel','Gel de ducha',.075,.22,.055,'plastico','#aabdc9'),('champu','Champú',.07,.2,.055,'plastico','#c4b68d')]:
        out.append(objeto('va_'+id,nombre,w,h,d,masa=.3,material=mat,partes=[caja(w,h,d,c=col,m=mat)],categoria='decoracion'))
        out[-1]['soporte']='superficie'
        if mat not in ['tela','metal'] and h>.05:
            out[-1]['partes'].append(dict(f='plano',d=[w*.78,h*.45],p=[0,h*.48,d/2+.002],c='#e7e0cf',m='papel',tex=dict(tipo='vivienda_etiqueta_a',titulo=nombre)))
    # Reservas a escala de una balda doméstica, con siluetas y etiquetas propias.
    for i,(nombre,col) in enumerate([('Arroz','#d6c8a0'),('Lentejas','#9e8055'),('Garbanzos','#cbb07c'),('Judías','#d8d0bc'),('Harina','#e1d7be'),('Pasta','#d6b976')]):
        p=[cil(.052,.052,.18,y=.09,c=col,m='comida'),cil(.056,.056,.018,y=.189,c='#7d8788',m='metal'),caja(.072,.055,.003,y=.095,z=.051,c='#e7dec7',m='papel'),caja(.055,.008,.004,y=.1,z=.054,c='#7c6550',m='papel')]
        out.append(objeto('va_reserva_'+str(i),nombre+' en tarro',.112,.2,.112,None,.7,'comida',partes=p,soporte='superficie',categoria='decoracion'))
    for i,col in enumerate(['#c47856','#81946c','#bea65c']):
        out.append(objeto('va_conserva_'+str(i),'Lata de conserva doméstica',.095,.12,.095,None,.4,'comida',partes=[cil(.045,.045,.11,c=col,m='comida'),cil(.047,.047,.008,y=.114,c='#abb0a8',m='metal'),caja(.06,.04,.003,y=.06,z=.044,c='#e5d6b5',m='papel')],soporte='superficie',categoria='decoracion'))
    return out

if __name__=='__main__':guardar_catalogo('vivienda_a',objetos())
