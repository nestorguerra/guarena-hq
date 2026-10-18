from pathlib import Path
p=Path('.cache/calidad/tanda18/postpaso_r3');base=Path('.cache/calidad/tanda18/medidas/runtime.cpu.mjs').read_text()
base=base.replace("from '../../tanda11", "from '../../tanda11").replace("const read=(p,after=false)=>fs.readFileSync(p,'utf8');", "const overrides=new Map(); const read=(p,after=false)=>after&&overrides.has(p)?overrides.get(p):fs.readFileSync(p,'utf8');")
base=base.replace("const locales=make(","const composition=make(fs.readFileSync('.cache/calidad/tanda18/postpaso_r3/composicion_lectura_salon.js','utf8'),{...data,...objetos,...geo},'componerLectura');\n const locales=make(")
base=base.replace("{THREE,...data,...HK,...objetos,...geo,...util,MURO:HK.T}","{THREE,...data,...HK,...objetos,...geo,...util,...composition,MURO:HK.T}")
base=base.replace('export{runtime,','export{overrides,runtime,')
(p/'runtime.cpu.mjs').write_text(base)
locales=Path('src/locales.js').read_text();marker='  return { K, tipologia, seed, W, D, H, ev, U, puertaX, inicio, ancho, avisos, zonas, tabiques, libres, P, guardias, debe, activas,'
hook='''  let composicionLectura;
  const lectura=componerLectura({P,K,ctx,planta,H,libres,inicio,aceptar:candidatos=>{
    const original=P.slice(),g=guardias;
    try{P.splice(0,P.length,...candidatos);return !cierra([]);}
    finally{P.splice(0,P.length,...original);guardias=g;}
  }});
  if(lectura){P.splice(0,P.length,...lectura.P);composicionLectura=lectura.metadata;}

'''
assert marker in locales
locales=locales.replace(marker,hook+marker+' ...(composicionLectura?{composicionLectura}:{}),')
(p/'locales.js').write_text(locales)
houses=Path('src/houses.js').read_text().replace('filtro,funciones:true','filtro,funciones:true,perfil:prof.id')
houses=houses.replace('estancias.push({ ...(A.composicionCocina?', 'estancias.push({ ...(A.composicionLectura?{composicionLectura:A.composicionLectura}:{}),...(A.composicionCocina?')
houses=houses.replace('      switch (o.rol) {','      if(A.composicionLectura?.asiento===i&&!o.rol)for(const st of asientos)pieces.seat.push(st);\n      switch (o.rol) {',1)
(p/'houses.js').write_text(houses)
