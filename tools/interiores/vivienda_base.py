"""Primitivas y escritura de los kits domésticos. Importar este módulo no escribe archivos."""
import copy, json, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
MADERA, TELA, BLANCO, METAL = '#926b45', '#7a5b63', '#e9e5dc', '#9c9fa4'

def caja(w,h,d,x=0,y=None,z=0,c=MADERA,m='madera',**kw):
    return dict(f='caja',d=[w,h,d],p=[x,h/2 if y is None else y,z],c=c,m=m,**kw)
def cil(rt,rb,h,x=0,y=None,z=0,c=METAL,m='metal',**kw):
    return dict(f='cil',d=[rt,rb,h],p=[x,h/2 if y is None else y,z],c=c,m=m,**kw)
def objeto(id,nombre,w,h,d,rol=None,masa=30,material='madera',partes=None,superficies=None,categoria='mueble',**kw):
    clase='PICKUP' if masa<5 else 'CARRY' if masa<25 else 'PUSH' if masa<80 else 'PUSH_HEAVY'
    out=dict(id=id,nombre=nombre,categoria=categoria,clase=clase,masa=masa,material=material,soporte='suelo',partes=partes or [caja(w,h,d,m=material)])
    out.update(kw)
    if rol:out['rol']=rol
    if superficies is not None:out['superficies']=superficies
    return out
def guardar_catalogo(familia,objetos):
    with open(os.path.join(ROOT,'data','objetos',familia+'.json'),'w') as f:
        json.dump(dict(version=1,familia=familia,objetos=objetos),f,ensure_ascii=False,indent=1)
    print(familia,len(objetos),'objetos')
def catalogo():
    import glob
    return {o['id']:o for f in sorted(glob.glob(os.path.join(ROOT,'data','objetos','*.json'))) for o in json.load(open(f))['objetos']}
def copiar(id,nuevo,nombre=None,rol=None,escala=1):
    o=copy.deepcopy(catalogo()[id]);o['id']=nuevo
    if nombre:o['nombre']=nombre
    if rol:o['rol']=rol
    if escala!=1:
        for p in o['partes']:p['d']=[v*escala for v in p['d']];p['p']=[v*escala for v in p['p']]
        for sup in o.get('superficies',[]):
            for k in ['y','fondo','margen']:
                if k in sup:sup[k]*=escala
    return o
def E(regla,obj=None,**kw):
    return dict(zona='estancia',regla=regla,**({'variantes':obj} if isinstance(obj,list) else {'obj':obj} if obj else {}),**kw)
def pared(obj,obligatorio=True,**kw):return E('contra_pared',obj,pared='*',cantidad=[1 if obligatorio else 0,1],obligatorio=obligatorio,preferir=True,**kw)
def junto(obj,de,obligatorio=False,**kw):return E('junto_a',obj,de=de,cantidad=[1 if obligatorio else 0,1],obligatorio=obligatorio,preferir=True,**kw)
def cajonera(id,nombre,w=.72,h=.74,d=.34,rol='comoda',masa=28):
    p=[caja(w,h,d,tinte='madera')]
    for i in range(3):
        y=(i+.5)*h/3;p += [caja(w-.035,h/3-.025,.016,y=y,z=d/2+.008,c='#b18c64',tinte='madera'),caja(.14,.018,.025,y=y,z=d/2+.024,c=METAL,m='metal')]
    return objeto(id,nombre,w,h,d,rol,masa,partes=p,superficies=[dict(y=h,margen=.025)])
def mesa(id,nombre,w=1.05,d=.5,h=.75,rol='mesa'):
    p=[caja(w,.045,d,y=h-.0225,tinte='madera')]
    for x in [-w/2+.045,w/2-.045]:
        for z in [-d/2+.045,d/2-.045]:p.append(caja(.055,h-.045,.055,x=x,y=(h-.045)/2,z=z,tinte='madera'))
    return objeto(id,nombre,w,h,d,rol,18,partes=p,superficies=[dict(y=h,margen=.04)])
def kit(id,nombre,tipologia,entradas,mood,fondo=(1.9,4.8),ancho=(3.2,7.8)):
    for e in entradas:
        if e.get('regla')=='techo' and id in ['bano','despensa','trastero','taller','costura','cocina','estudio','despacho']:
            e['obj']='vb_lampara_trabajo' if id in ['taller','costura','cocina','estudio'] else 'vb_plafon'
    k=dict(tipologia=tipologia,nombre=nombre,superficie=dict(ancho=list(ancho),fondo=list(fondo),alto=2.75),variables={},puerta=-.75,paso_libre=.8,
           zonas=[dict(id='estancia',publica=True,rect=['-W/2','0','W/2','D'])],tabiques=[],objetos=entradas,
           iluminacion=dict(fuentes=[1,3],temperatura_k=[2700,3000],minimo_lux_publico=60),ambiente=dict(sonido='casa',vida=['objetos cotidianos del hogar']),
           minimo_objetos_distintos=60 if tipologia in ['cocina','bano','dormitorio'] else 30,moodboard=mood)
    with open(os.path.join(ROOT,'data','kits','vivienda_'+id+'.json'),'w') as f:json.dump(k,f,ensure_ascii=False,indent=1)
    return k
def adornos(pool,soportes,lampara='lampara_techo_salon'):
    return [E('sobre',list(dict.fromkeys(pool)),en=soportes,por_soporte=[3,6]),E('techo',lampara,por_m=[.4,.42],obligatorio=True)]
