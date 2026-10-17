"""Detalle doméstico de baño y bricolaje. Geometría propia, sin fotografías."""
from vivienda_base import *

def mejorar_bano_taller(out):
    C={o['id']:o for o in out}
    # La porcelana tiene cuerpo, asiento y cisterna; no se lee como un cubo tapado.
    C['va_inodoro']['partes']=[
        cil(.125,.14,.3,z=.055,c='#e3e1d8',m='ceramica'),
        cil(.18,.12,.14,y=.35,z=.08,c='#e9e7dc',m='ceramica',s=[1,1,1.28]),
        cil(.185,.185,.025,y=.431,z=.09,c='#f0eee4',m='plastico',s=[1,1,1.28]),
        cil(.125,.125,.006,y=.447,z=.105,c='#657e7d',m='ceramica',s=[1,1,1.3]),
        caja(.38,.37,.17,y=.6,z=-.22,c='#e5e4da',m='ceramica',redondeo=.025),
        caja(.39,.027,.18,y=.798,z=-.22,c='#edebe0',m='ceramica',redondeo=.01),
        cil(.018,.018,.006,y=.816,z=-.22,c='#a3aaa4',m='metal'),
    ]
    # Bañera hueca, con fondo hundido y borde de porcelana a escala.
    C['va_banera']['partes']=[
        caja(1.38,.1,.61,y=.05,c='#c9d2ce',m='ceramica',redondeo=.035),
        caja(1.4,.42,.075,y=.31,z=-.29,c='#e8e6da',m='ceramica',redondeo=.025),
        caja(1.4,.42,.075,y=.31,z=.29,c='#e8e6da',m='ceramica',redondeo=.025),
        caja(.085,.42,.54,x=-.66,y=.31,c='#e8e6da',m='ceramica',redondeo=.025),
        caja(.085,.42,.54,x=.66,y=.31,c='#e8e6da',m='ceramica',redondeo=.025),
        cil(.012,.012,.19,x=-.59,y=.55,z=-.23,c='#a2aca7'),
        caja(.025,.025,.14,x=-.59,y=.64,z=-.17,c='#a2aca7',m='metal'),
    ]
    # Lavabo grande: la escala del mueble responde a una sala de más de 12 m².
    p=[caja(.9,.67,.42,y=.435,c='#557e78',m='madera',redondeo=.025),
       caja(.94,.05,.46,y=.795,c='#d5c6a6',m='piedra',redondeo=.015),
       caja(.45,.012,.29,y=.829,c='#9aaba4',m='ceramica',redondeo=.005)]
    for x in [-.43,.43]:
        p.append(caja(.065,.1,.34,x=x,y=.05,c='#6f5e48',m='madera',redondeo=.01))
    for x in [-.22,.22]:
        p += [caja(.41,.53,.02,x=x,y=.44,z=.221,c='#71958b',m='madera',redondeo=.008),
              caja(.13,.014,.028,x=x,y=.66,z=.244,c='#b9b09b',m='metal',redondeo=.005)]
    for z in [-.155,.155]:p.append(caja(.48,.035,.03,y=.843,z=z,c='#e9e5d8',m='ceramica',redondeo=.01))
    for x in [-.225,.225]:p.append(caja(.03,.035,.3,x=x,y=.843,c='#e9e5d8',m='ceramica',redondeo=.01))
    p += [cil(.013,.013,.18,y=.94,z=-.19,c='#a4b0a9'),caja(.025,.025,.12,y=1.025,z=-.145,c='#a4b0a9',m='metal')]
    out.append(objeto('va_lavabo_amplio','Lavabo amplio con mueble y porcelana',.94,1.04,.46,None,42,partes=p,superficies=[dict(y=.82,margen=.04)]))
    out.append(objeto('va_espejo_amplio','Espejo amplio con marco y luz',.91,.67,.045,'espejo',5,'metal',partes=[
        caja(.91,.67,.03,y=1.5,z=.015,c='#4d6e67',m='madera',redondeo=.014),
        caja(.85,.6,.008,y=1.5,z=.036,c='#9db4b5',m='metal'),
        caja(.7,.025,.045,y=1.855,z=.025,c='#eee8db',m='cristal',luz=True)],soporte='pared',categoria='decoracion'))
    # El armario tiene baldas abiertas y toallas, no una silueta de ropero.
    p=[caja(.4,1.4,.025,z=-.112,c='#718b80',m='madera')]
    for x in [-.185,.185]:p.append(caja(.03,1.4,.25,x=x,c='#a78b64',m='madera',redondeo=.008))
    for y in [.04,.5,.92,1.4]:p.append(caja(.4,.03,.25,y=y,c='#b3976d',m='madera',redondeo=.008))
    for y,col in [(.55,'#c0c6ac'),(.62,'#8ba39a'),(.97,'#c8b897')]:p.append(caja(.3,.055,.2,y=y,z=.005,c=col,m='tela',redondeo=.02))
    C['va_armario_bano']['partes']=p
    C['va_armario_bano']['superficies']=[dict(y=1.415,margen=.03)]
    for id in ['va_lavabo','va_armario_bano','va_cesto_ropa']:
        for p in C[id]['partes']:
            if p['f']=='caja' and min(p['d'])>=.025:p['redondeo']=min(.018,min(p['d'])/3)

    # Tres actividades del taller, con piezas en reparación apoyadas en el tablero.
    base=C['va_banco']
    marco=copy.deepcopy(base);marco['id']='va_banco_carpinteria';marco['nombre']='Banco de carpintería con marco en reparación'
    motor=copy.deepcopy(base);motor['id']='va_banco_mecanica';motor['nombre']='Banco con motor de riego en reparación'
    for o,color in [(marco,'#8a9b88'),(motor,'#637f8b')]:
        for p in o['partes']:
            if p['f']=='caja' and p['d'][1]>.7 and p['d'][2]<.04:p['c']=color
    for x in [-.42,-.08]:marco['partes'].append(caja(.045,.04,.28,x=x,y=.927,z=.01,c='#ac7848',m='madera',redondeo=.009))
    for z in [-.11,.13]:marco['partes'].append(caja(.38,.04,.04,x=-.25,y=.927,z=z,c='#b58956',m='madera',redondeo=.009))
    marco['partes'] += [caja(.24,.025,.035,x=-.25,y=.96,z=.01,c='#828c86',m='metal'),caja(.045,.11,.045,x=-.32,y=.99,z=.01,c='#a86b40',m='madera')]
    motor['partes'] += [caja(.32,.035,.25,x=-.28,y=.927,z=.01,c='#586f72',m='metal'),
        cil(.1,.1,.2,x=-.28,y=1.045,z=.01,c='#9aa7a1',m='metal',r=[90,0,0]),
        cil(.025,.025,.32,x=-.28,y=1.045,z=.01,c='#aeb4ac',m='metal',r=[90,0,0]),
        caja(.09,.055,.11,x=-.28,y=1.17,z=.01,c='#5f777b',m='metal',redondeo=.012)]
    base['partes'] += [caja(.22,.18,.18,x=-.25,y=.995,z=.04,c='#b38954',m='madera',redondeo=.009),
        cil(.033,.033,.003,x=-.25,y=1.025,z=.132,c='#4e5547',m='madera',r=[90,0,0]),
        caja(.15,.02,.22,x=-.305,y=1.115,z=.04,c='#96734e',m='madera',r=[0,0,32],redondeo=.006),
        caja(.15,.02,.22,x=-.195,y=1.115,z=.04,c='#96734e',m='madera',r=[0,0,-32],redondeo=.006)]
    for o in [base,marco,motor]:
        for p in o['partes']:
            if p['f']=='caja' and min(p['d'])>=.03:p['redondeo']=min(.012,min(p['d'])/3)
    out += [marco,motor]
    for o in [base,marco,motor]:
        amplio=copy.deepcopy(o);amplio['id']=o['id']+'_amplio';amplio['nombre']=o['nombre']+' de mayor longitud'
        for p in amplio['partes']:
            if p['f'] in ['caja','plano']:p['d'][0]*=1.32
            p['p'][0]*=1.32
        for sup in amplio.get('superficies',[]):
            if 'ancho' in sup:sup['ancho']*=1.32
        out.append(amplio)
