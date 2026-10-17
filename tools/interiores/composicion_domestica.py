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
