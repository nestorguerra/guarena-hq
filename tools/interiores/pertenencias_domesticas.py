"""Pertenencias propias del hogar: siluetas abiertas, sin imágenes ni recursos externos."""
import math
from vivienda_base import *

def barra(a,b,r=.014,c='#879b94',m='metal',seg=6):
    # Estas barras se modelan en XY; los manillares perpendiculares son cilindros aparte.
    dx,dy=b[0]-a[0],b[1]-a[1]
    return cil(r,r,math.hypot(dx,dy),x=(a[0]+b[0])/2,y=(a[1]+b[1])/2,z=(a[2]+b[2])/2,c=c,m=m,seg=seg,r=[0,0,-math.degrees(math.atan2(dx,dy))])

def aro_xy(x,y,z,R,t,c,segmentos=20):
    p=[]
    for i in range(segmentos):
        a=i*2*math.pi/segmentos;b=(i+1)*2*math.pi/segmentos
        p.append(barra((x+R*math.cos(a),y+R*math.sin(a),z),(x+R*math.cos(b),y+R*math.sin(b),z),t,c))
    return p

def pertenencias(out):
    # Bicicleta de paseo guardada: ruedas huecas, radios, cuadro, sillín y manillar.
    p=[]
    for x in [-.45,.45]:
        p+=aro_xy(x,.325,0,.3,.024,'#4c554d')
        p+=aro_xy(x,.325,.002,.275,.008,'#b5bbb1')
        for i in range(8):
            a=i*math.pi/4;p.append(barra((x,.325,.005),(x+.268*math.cos(a),.325+.268*math.sin(a),.005),.003,'#a1aaa4'))
        p.append(cil(.03,.03,.09,x=x,y=.325,c='#a6afa8',r=[90,0,0],seg=8))
    for a,b in [((-.45,.325),(-.2,.68)),((-.2,.68),(.18,.68)),((.18,.68),(-.06,.34)),((-.06,.34),(-.45,.325)),((-.2,.68),(-.06,.34)),((.18,.68),(.45,.325)),((.18,.68),(.26,.94)),((-.2,.68),(-.22,.84))]:
        p.append(barra((*a,0),(*b,0),.019,'#648c86'))
    p+=aro_xy(-.06,.34,.04,.085,.009,'#9eaaa2',16)
    p += [cil(.012,.012,.24,x=-.06,y=.34,c='#a2aca6',r=[90,0,0],seg=8),barra((-.06,.34,.115),(.02,.34,.115),.009,'#a2aca6'),barra((-.06,.34,-.115),(-.14,.34,-.115),.009,'#a2aca6')]
    p += [caja(.24,.055,.14,x=-.22,y=.865,c='#6e6858',m='tela',redondeo=.022),cil(.012,.012,.46,x=.26,y=.94,c='#a2aca6',r=[90,0,0],seg=8),caja(.16,.025,.07,x=.02,y=.34,z=.12,c='#696e62',m='goma',redondeo=.008),caja(.16,.025,.07,x=-.14,y=.34,z=-.12,c='#696e62',m='goma',redondeo=.008),barra((-.06,.34,-.08),(.12,.005,-.08),.009,'#78887c')]
    for z in [-.19,.19]:p.append(cil(.02,.02,.09,x=.26,y=.94,z=z,c='#656d61',m='goma',r=[90,0,0],seg=8))
    out.append(objeto('va_bicicleta_guardada','Bicicleta de paseo guardada',1.56,1,.5,None,14,'metal',partes=p))
    # Escalera plegada, cubo y rodillo de una reforma, con apoyos separados.
    p=[]
    for x in [-.26,.26]:
        p += [caja(.045,1.65,.055,x=x,y=.825,z=-.06,c='#9ca9a2',m='metal',redondeo=.009),caja(.07,.06,.08,x=x,y=.03,z=-.06,c='#66766b',m='goma',redondeo=.012)]
    for y in [.22,.49,.76,1.03,1.3,1.57]:p.append(caja(.49,.04,.08,y=y,z=-.045,c='#b4bcb1',m='metal',redondeo=.008))
    p += [cil(.14,.11,.27,x=.45,y=.135,z=.035,c='#a5b6a4',m='plastico'),cil(.142,.142,.018,x=.45,y=.278,z=.035,c='#c5c9b5',m='plastico'),barra((.44,.28,.04),(.6,.77,.04),.012,'#9b8460','madera'),cil(.045,.045,.23,x=.6,y=.79,z=.04,c='#d4cbb1',m='tela',r=[0,0,90],seg=12)]
    out.append(objeto('va_escalera_guardada','Escalera plegada y útiles de pintar guardados',1.03,1.68,.35,None,12,'metal',partes=p))
    # Ventilador retirado: aro abierto y aspas legibles, sobre su pedestal.
    p=[cil(.16,.19,.035,y=.0175,c='#7a8e83',m='metal'),cil(.018,.018,.68,y=.37,c='#9aa99e',seg=8),cil(.055,.055,.12,y=.74,c='#839b91',r=[90,0,0],seg=10)]
    p+=aro_xy(0,.74,.065,.22,.012,'#9baea0')
    for i in range(8):
        a=i*math.pi/4;p.append(barra((0,.74,.07),(.21*math.cos(a),.74+.21*math.sin(a),.07),.004,'#b0bdb0'))
    for i in range(3):
        a=i*2*math.pi/3;p.append(caja(.085,.16,.018,x=.09*math.sin(a),y=.74+.09*math.cos(a),z=.03,c='#b6c8ba',m='plastico',r=[0,0,-math.degrees(a)],redondeo=.025))
    p.append(cil(.04,.04,.018,y=.74,z=.09,c='#8d9f91',r=[90,0,0],seg=10))
    out.append(objeto('va_ventilador_guardado','Ventilador guardado fuera de temporada',.47,.98,.39,None,6,'metal',partes=p))
    # Cesto de temporada, sombrero, manta y paraguas, otra silueta distinta de caja.
    p=[cil(.23,.18,.37,y=.185,c='#ae9670',m='madera',seg=16),cil(.24,.24,.035,y=.385,c='#c3ac82',m='madera',seg=16),caja(.34,.075,.28,x=.01,y=.43,z=.02,c='#8fa59c',m='tela',redondeo=.025),cil(.16,.16,.025,x=.03,y=.48,z=.01,c='#c8b88d',m='tela',seg=16),cil(.085,.11,.105,x=.03,y=.545,z=.01,c='#b8a377',m='tela',seg=16),cil(.018,.018,1.04,x=.3,y=.52,z=-.04,c='#8b7656',m='madera',r=[0,0,-8],seg=8),cil(.045,.018,.7,x=.31,y=.64,z=-.04,c='#667f79',m='tela',r=[0,0,-8],seg=10)]
    out.append(objeto('va_cesto_temporada','Cesto con manta, sombrero y paraguas guardados',.65,1.1,.5,None,8,'tela',partes=p))
