from pathlib import Path
p=Path('.cache/calidad/tanda18/estar_r7');r=Path.cwd()
s=(r/'tools/interiores/catalogo_vivienda.py').read_text();lo=s.index('def sofa(');hi=s.index("sofa('sofa_tres_plazas'",lo)
sofa='''def sofa(id, nombre, w, plazas, masa):
    # Misma huella, altura y plazas: patas, bastidor, cojines y brazos blandos.
    partes = [*patas(w-.04,.78,.12,grosor=.055,c=MADERA,tinte='madera',inset=.055),
              caja(w-.06,.08,.78,y=.16,c=MADERA,tinte='madera',redondeo=.018),
              caja(w,.20,.84,y=.30,c=TELA,m='tela',tinte='tela',redondeo=.04),
              caja(w,.46,.20,y=.65,z=-.32,c=TELA,m='tela',tinte='tela',redondeo=.045),
              caja(.18,.27,.84,x=-w/2+.09,y=.545,c=TELA,m='tela',tinte='tela',redondeo=.055),
              caja(.18,.27,.84,x=w/2-.09,y=.545,c=TELA,m='tela',tinte='tela',redondeo=.055)]
    ancho = (w-.36)/plazas
    for i in range(plazas):
        x = -(w-.36)/2 + ancho*(i+.5)
        partes += [caja(ancho-.018,.12,.62,x=x,y=.42,z=.08,c=TELA,m='tela',tinte='tela',redondeo=.045),
                   caja(ancho-.025,.34,.14,x=x,y=.66,z=-.17,c=TELA,m='tela',tinte='tela',redondeo=.04,r=[-8,0,0])]
    for lado in [-1,1]:
        partes.append(caja(.29,.30,.13,x=lado*(w/2-.34),y=.62,z=.12,c='#c6b79b',m='tela',redondeo=.055,r=[-9,0,lado*8]))
    asientos = [{'p': [-((w-.36)/2)+(w-.36)*(i+.5)/plazas,.45,.12], 'h':.45,'anim':'sofa'} for i in range(plazas)]
    obj(id,nombre,'sofa','PUSH',masa,'tela','suelo',partes,rol='sofa',modificadores=['SEAT'],asientos=asientos,
        superficies=[{'y':.48,'margen':.2}],nota='sofá tapizado con cojines separados, brazos blandos y patas de madera')
'''
s=s[:lo]+sofa+s[hi:]
lo=s.index("obj('puff',");hi=s.index('\n',lo)
s=s[:lo]+"""obj('puff', 'Puf tapizado', 'sillon', 'CARRY', 8, 'tela', 'suelo', [
    cil(.235,.235,.025,y=.0125,c='#6d6252',m='tela',seg=20),
    cil(.26,.25,.295,y=.1725,c=TELA,m='tela',tinte='tela',seg=20),
    esf(.26,y=.30,c=TELA,m='tela',tinte='tela',s=[1, .3846153846, 1]),
    cil(.259,.259,.008,y=.307,c='#a6977d',m='tela',seg=20)],
    modificadores=['SEAT'], asientos=[{'p':[0,.4,0],'h':.4,'anim':'silla'}])"""+s[hi:]
lo=s.index("obj('alfombra_salon',");hi=s.index("obj('planta_maceta_salon'",lo)
s=s[:lo]+"""# Tejido geométrico propio: cenefa, campo sereno y bandas amplias, sin fotografía.
alfombra = [caja(2,.003,1.4,y=.0015,c='#687565',m='tela'),caja(1.8,.004,1.2,y=.002,c='#c8bda5',m='tela')]
for x in [-.68,-.34,0,.34,.68]:
    alfombra.append(caja(.055,.0004,1.12,x=x,y=.0038,c='#aaa58e',m='tela'))
for z in [-.46,.46]:
    alfombra.append(caja(1.72,.0004,.055,y=.0038,z=z,c='#8b7760',m='tela'))
obj('alfombra_salon','Alfombra tejida','textil','PICKUP',4,'tela','suelo',alfombra,
    nota='tejido propio de tonos naturales; cenefa y bandas agrupadas en el material mate')
"""+s[hi:]
(p/'catalogo_vivienda.py').write_text(s)
h=(p/'houses.js').read_text();a="const it = { obj: p.obj, x: B.ox + hx, y, z: B.oz + hz, ry: p.ry, seed: prof.seed + rooms.indexOf(rm) * 97 + i, paleta };";assert h.count(a)==1
b="""const tejidosSalon={joven:'#526c78',bohemio:'#a27054',alegre:'#6b8271',moderno:'#767d79',lujo:'#61747a',rustico:'#826b54',antiguo:'#80755d'};
      const paletaPieza=kid==='vivienda_salon'&&(o.rol==='sofa'||p.obj==='puff')?{...paleta,tela:[p.obj==='puff'?'#a99a7e':tejidosSalon[prof.style]||'#767d79']}:paleta;
      const it = { obj: p.obj, x: B.ox + hx, y, z: B.oz + hz, ry: p.ry, seed: prof.seed + rooms.indexOf(rm) * 97 + i, paleta:paletaPieza };"""
h=h.replace(a,b);(p/'houses.js').write_text(h)
print('Modelos privados escritos; fuentes activas intactas')
