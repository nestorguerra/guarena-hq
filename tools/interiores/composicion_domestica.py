"""Conjuntos domésticos propios: almacenaje y trabajo con escala y uso legibles."""
from vivienda_base import *

def b(w,h,d,**kw):
    return caja(w,h,d,redondeo=min(.018,min(w,h,d)/3),**kw)

def mejorar_almacen(out):
    # Las baldas contienen pertenencias del hogar, no hileras de envases de tienda.
    for variante,col in enumerate(['#617a72','#6e7f8c','#8b755b']):
        p=[]
        for x in [-.57,.57]:
            for z in [-.2,.2]:p.append(b(.035,2.04,.035,x=x,z=z,c=col,m='metal'))
        for y in [.09,.56,1.03,1.5,2.02]:p.append(b(1.18,.035,.45,y=y,c='#a08b69'))
        for x,y,w,h,c in [(-.29,.3,.49,.38,'#a98b66'),(.3,.27,.45,.32,'#788e89'),(-.29,.78,.46,.4,'#be9d70'),(.3,1.25,.45,.4,'#b39167')]:
            p += [b(w,h,.36,x=x,y=y,z=.015,c=c,m='papel'),b(w+.02,.025,.37,x=x,y=y+h/2,c='#c3af89',m='papel'),caja(.15,.055,.004,x=x,y=y,z=.2,c='#e3dbc6',m='papel')]
        if variante==0:
            # Maleta guardada, asa, cierres y rollo de alfombra.
            p += [b(.46,.31,.29,x=.3,y=.735,c='#866654',m='tela'),b(.2,.025,.035,x=.3,y=.907,c='#62584a'),b(.035,.1,.018,x=.12,y=.74,z=.166,c='#b6ae8e',m='metal'),b(.035,.1,.018,x=.48,y=.74,z=.166,c='#b6ae8e',m='metal'),cil(.135,.135,.48,x=-.28,y=1.655,z=0,c='#9c9782',m='tela',r=[0,0,90])]
        elif variante==1:
            for i in range(7):p.append(b(.045,.26+(i%3)*.025,.23,x=.13+i*.05,y=.71+(i%3)*.0125,c=['#b28c65','#8d6b60','#657e85'][i%3],m='papel',r=[0,0,(-1)**i*3]))
            for i in range(3):p.append(b(.47,.065,.31,x=-.27,y=1.555+i*.07,c=['#aab09b','#899d9a','#bca387'][i],m='tela'))
        else:
            for i in range(4):p.append(b(.48,.08,.32,x=.29,y=.62+i*.085,c=['#9fa48b','#c5b28b','#879e9b','#b48f86'][i],m='tela'))
            p += [b(.45,.27,.28,x=-.28,y=1.655,c='#a08c69',m='tela'),b(.36,.045,.23,x=-.28,y=1.81,c='#d0c3a5',m='tela')]
        # Archivadores cerrados y una lámpara retirada, sobre balda superior interna.
        for i in range(4):p += [b(.075,.32,.25,x=.16+i*.085,y=1.68,c=['#657c79','#697b8b','#b19a77','#7f8c72'][i],m='papel'),caja(.037,.11,.004,x=.16+i*.085,y=1.68,z=.134,c='#d8d3c4',m='papel')]
        out.append(objeto('va_estante_trastero_'+str(variante),'Estantería de pertenencias domésticas '+str(variante+1),1.18,2.04,.45,None,48,'metal',partes=p,superficies=[dict(y=2.0375,margen=.06)]))
    # Un conjunto de útiles retirados: siluetas largas que ocupan otra pared.
    p=[b(.88,.07,.055,y=1.48,z=-.08,c='#957450')]
    for x in [-.3,0,.3]:p.append(cil(.017,.017,1.38,x=x,y=.71,c='#b49b70',m='madera',r=[0,0,x*10]))
    p += [b(.34,.09,.12,x=-.3,y=.045,c='#a4916b',m='tela'),b(.22,.3,.025,x=0,y=.18,c='#7a8881',m='metal'),b(.33,.035,.03,x=.3,y=.15,c='#87958a',m='metal')]
    for x in [.17,.23,.29,.35,.41]:p.append(b(.014,.13,.025,x=x,y=.08,c='#87958a',m='metal'))
    out.append(objeto('va_utiles_guardados','Escoba, pala y rastrillo guardados',.95,1.55,.18,None,8,partes=p))

def mejorar_despacho(out):
    # Mesa de trabajo completa: escala adulta, cajonera, bandejas y lámpara.
    for v,col in enumerate(['#8b6a49','#6f827d','#8b7461']):
        p=[b(1.42,.065,.64,y=.755,c='#b69b74'),b(.43,.67,.55,x=.44,y=.365,c=col),b(.065,.72,.54,x=-.63,y=.36,c=col)]
        for y in [.22,.43,.64]:
            p += [b(.39,.18,.018,x=.44,y=y,z=.285,c='#aa8b66'),b(.13,.012,.027,x=.44,y=y+.05,z=.307,c='#b6b5a6',m='metal')]
        p += [b(.42,.008,.28,x=-.18,y=.792,z=.12,c='#657c73',m='tela'),b(.12,.018,.12,x=-.57,y=.798,z=-.18,c='#6f7974',m='metal'),cil(.012,.012,.35,x=-.57,y=.98,z=-.18,c='#83958b',m='metal'),cil(.07,.11,.09,x=-.57,y=1.17,z=-.18,c='#c9ba93',m='metal'),b(.22,.025,.14,x=.45,y=.802,z=-.18,c='#b9ab91',m='papel')]
        # Zona libre central para ordenador y objetos del kit.
        out.append(objeto('vb_mesa_despacho_'+str(v),'Mesa de trabajo con cajonera y lámpara '+str(v+1),1.42,1.23,.64,'mesa',46,partes=p,superficies=[dict(y=.7875,margen=.02,ancho=.58,fondo=.37)]))
    p=[b(.54,.09,.5,y=.48,c='#5f7775',m='tela'),b(.49,.49,.055,y=.77,z=-.22,c='#6a8280',m='tela')]
    for x in [-.23,.23]:
        for z in [-.21,.21]:p.append(b(.04,.43,.04,x=x,y=.215,z=z,c='#6e6c5b'))
        p.append(b(.045,.035,.42,x=x,y=.65,c='#887c62'))
    out.append(objeto('vb_silla_despacho','Silla de despacho tapizada',.54,1.02,.5,'silla',9,partes=p))
    # Una segunda zona de lectura con mesa baja y libros, sin invadir el paso.
    p=[b(.52,.04,.46,y=.51,c='#b09972')]
    for x in [-.2,.2]:
        for z in [-.17,.17]:p.append(b(.035,.49,.035,x=x,y=.245,c='#806d54'))
    p += [b(.26,.025,.2,y=.542,c='#7d9693',m='papel'),b(.24,.025,.18,y=.568,c='#c9b88e',m='papel'),b(.22,.025,.17,y=.594,c='#9e7e6a',m='papel')]
    out.append(objeto('vb_mesa_lectura','Mesa auxiliar con libros',.52,.61,.46,None,6,partes=p))

def mejorar_cocina_costura(out):
    C={o['id']:o for o in out}
    for id in ['va_cocina','va_encimera','va_nevera','va_lavadora','va_alacena','va_alto_cocina']:
        for p in C[id]['partes']:
            if p['f']=='caja' and min(p['d'])>=.02:p['redondeo']=min(.014,min(p['d'])/3)
    # Campana, mandos y una olla sobre el fuego; todo conserva el plano de trabajo.
    C['va_cocina']['partes'] += [b(.5,.12,.38,x=-.3,y=1.78,z=-.045,c='#aab5ae',m='metal'),b(.22,.22,.2,x=-.3,y=1.95,z=-.13,c='#bdc5bc',m='metal'),cil(.12,.12,.16,x=-.3,y=1.0,z=.06,c='#698784',m='metal'),cil(.125,.125,.018,x=-.3,y=1.1,z=.06,c='#8d9f96',m='metal'),cil(.024,.024,.025,x=-.3,y=1.12,z=.06,c='#606f68',m='plastico')]
    for x in [-.46,-.34,-.22,-.1]:C['va_cocina']['partes'].append(cil(.018,.018,.018,x=x,y=.73,z=.276,c='#b8b8a9',m='metal',r=[90,0,0]))
    grande=copy.deepcopy(C['va_cocina']);grande['id']='va_cocina_amplia';grande['nombre']='Cocina amplia con fregadero, fogones y campana'
    for p in grande['partes']:
        if p['f'] in ['caja','plano']:p['d'][0]*=1.55
        p['p'][0]*=1.55
    grande['superficies']=[dict(y=.89,margen=.04,ancho=.24,fondo=.38)];out.append(grande)
    enc=copy.deepcopy(C['va_encimera']);enc['id']='va_encimera_amplia';enc['nombre']='Encimera amplia de preparación'
    for p in enc['partes']:p['d'][0]*=1.46;p['p'][0]*=1.46
    out.append(enc)
    p=[b(1.25,.055,.68,y=.85,c='#d5c6a9',m='piedra'),b(1.12,.71,.56,y=.42,c='#778f84')]
    for x in [-.36,0,.36]:p += [b(.33,.54,.018,x=x,y=.44,z=.29,c='#94a598'),b(.13,.013,.025,x=x,y=.65,z=.312,c='#c2bcaa',m='metal')]
    for x in [-.5,.5]:
        for z in [-.22,.22]:p.append(b(.06,.08,.06,x=x,y=.04,z=z,c='#776c54'))
    # Tabla y hogaza de pan: una actividad de cocina, sin una hilera de paquetes.
    p += [b(.35,.018,.23,x=-.32,y=.887,c='#a58155'),dict(f='esfera',d=[.09],p=[-.32,.963,0],c='#bc9764',m='comida',s=[1.9,.75,1])]
    out.append(objeto('va_isla_cocina','Isla de cocina con tabla y pan',1.25,1.06,.68,None,65,partes=p,superficies=[dict(y=.8775,margen=.05,ancho=.4,fondo=.42)]))
    # La costura reúne máquina, tela en curso y panel de carretes en el mismo puesto.
    p=[b(1.25,.05,.58,y=.735,c='#b69970')]
    for x in [-.54,.54]:
        for z in [-.22,.22]:p.append(b(.055,.71,.055,x=x,y=.355,z=z,c='#7f765d'))
    p += [b(.36,.028,.22,x=.27,y=.774,c='#566c68',m='metal'),b(.09,.25,.18,x=.4,y=.91,c='#67817c',m='metal'),b(.34,.07,.17,x=.27,y=1.035,c='#78938b',m='metal'),b(.045,.15,.11,x=.12,y=.94,c='#769087',m='metal'),cil(.005,.005,.06,x=.12,y=.85,c='#b4bbb0',m='metal'),cil(.06,.06,.027,x=.46,y=.94,c='#bdc2b5',m='metal',r=[0,0,90]),b(.96,.4,.025,y=1.44,z=-.27,c='#8d9d8e')]
    for x in [-.43,.43]:p.append(b(.025,.69,.025,x=x,y=1.095,z=-.27,c='#8d9d8e'))
    for i in range(7):
        x=-.4+i*.13
        p += [cil(.025,.025,.045,x=x,y=1.44,z=-.23,c=['#c4ad86','#8caaa0','#b3928b','#819ba8'][i%4],m='tela',r=[90,0,0]),cil(.03,.03,.008,x=x,y=1.44,z=-.2,c='#d0bc91',m='madera',r=[90,0,0])]
    for i in range(3):
        for j in range(3):p.append(b(.12,.012,.12,x=-.45+i*.123,y=.767,z=-.09+j*.123,c=['#97aaa1','#bdac90','#9caab1'][(i+j)%3],m='tela'))
    p += [b(.37,.3,.018,x=-.327,y=.61,z=.32,c='#a2b4a9',m='tela'),cil(.045,.045,.018,x=-.03,y=.77,z=.12,c='#d0bb83',m='tela')]
    C['va_costura']['partes']=p;C['va_costura']['superficies']=[dict(y=.76,margen=.035)]
    for id,nombre in [('bordado','Mesa con bordado en curso'),('patrones','Mesa con patrones de costura')]:
        o=copy.deepcopy(C['va_costura']);o['id']='va_costura_'+id;o['nombre']=nombre
        o['partes']=[q for q in o['partes'] if not(q.get('m')=='tela' and q['p'][1]<.8)]
        if id=='bordado':
            o['partes'] += [cil(.145,.145,.015,x=-.3,y=.772,c='#aa8757',m='madera'),cil(.126,.126,.012,x=-.3,y=.784,c='#d8ceaf',m='tela'),b(.29,.3,.018,x=-.3,y=.61,z=.32,c='#c5b4b2',m='tela')]
            for x,z in [(-.34,-.035),(-.3,0),(-.26,.035)]:o['partes'].append(b(.025,.003,.025,x=x,y=.792,z=z,c='#72978b',m='tela'))
        else:
            o['partes'] += [b(.35,.005,.26,x=-.32,y=.764,c='#e2dcc9',m='papel',r=[0,8,0]),b(.29,.005,.21,x=-.29,y=.771,z=.03,c='#ccc9b3',m='papel',r=[0,-12,0]),b(.34,.012,.035,x=-.32,y=.781,z=.15,c='#bdab78'),b(.14,.008,.012,x=-.3,y=.783,c='#756b55',m='madera',r=[0,25,0])]
        out.append(o)
    p=[b(1.04,.04,.4,y=.04,c='#a99470'),b(1.04,.04,.4,y=1.72,c='#a99470')]
    for x in [-.5,.5]:p.append(b(.04,1.72,.4,x=x,c='#9a8668'))
    for y in [.44,.87,1.3]:p.append(b(1.04,.03,.4,y=y,c='#b49e78'))
    for nivel,y in enumerate([.07,.47,.9,1.33]):
        for lado,x in enumerate([-.25,.25]):
            for i in range(3):p.append(b(.43,.075,.32,x=x,y=y+.0375+i*.078,c=['#91a49b','#c2af8b','#9ba9b1','#ba9991'][(nivel+lado+i)%4],m='tela'))
    out.append(objeto('va_mueble_telas','Estantería de telas y labores dobladas',1.04,1.74,.4,None,30,partes=p,superficies=[dict(y=1.74,margen=.04)]))

def unidades_domesticas(out):
    # Reutilizar la receta de UNA unidad, nunca la hilera ni el bloque de stock.
    from catalogo_comercio import SECO, SWEETS, BEBIDAS
    singular={'Paquetes de ':'Paquete de ','Bolsas de ':'Bolsa de ','Cajas de ':'Caja de ','Cajitas de ':'Cajita de ','Botes de ':'Bote de ','Botellas de ':'Botella de ','Tabletas de ':'Tableta de ','Packs de ':'Pack de ','Briks de ':'Brik de ','Garrafas de ':'Garrafa de '}
    for k,nombre,unit,nx,nz,dx,dz,h,fondo,c,mu in SECO+SWEETS+BEBIDAS:
        for plural,uno in singular.items():
            if nombre.startswith(plural):nombre=uno+nombre[len(plural):];break
        out.append(objeto('va_alimento_'+k,nombre,dx,h,dz,None,mu,'comida',partes=unit(0,0),soporte='superficie',categoria='alimento'))
