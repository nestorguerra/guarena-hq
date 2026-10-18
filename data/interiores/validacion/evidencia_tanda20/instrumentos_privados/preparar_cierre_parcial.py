from pathlib import Path
import json,hashlib,shutil,subprocess,datetime
r=Path.cwd();o=r/'.cache/calidad/tanda20';v=r/'data/interiores/validacion';e=v/'evidencia_tanda20'
J=lambda f:json.loads(f.read_text());H=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
def W(f,d):f.parent.mkdir(parents=True,exist_ok=True);f.write_text(json.dumps(d,ensure_ascii=False,indent=1)+'\n')
def cp(f,q):q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(f,q)
def tree(f,q):
 for t in sorted(f.rglob('*')):
  if t.is_file() and '__pycache__' not in t.parts:cp(t,q/t.relative_to(f))
assert not e.exists()
assert J(o/'dormitorio_paquete_corregido.json')['resultado']['estado']=='PASS' and not J(o/'dormitorio_paquete_corregido.json')['consola']
assert (o/'joven_visual/REVISION.md').exists()
assert J(o/'regeneracion.json')['estado']=='PASS'
assert J(o/'validacion_sello_final.json')['estado']=='PASS'
gates=J(o/'validacion_ejecuciones.json');assert len(gates)==10 and all(t['exit_code']==0 for t in gates)
assert all(H(r/f)==h for f,h in J(o/'estado_candidato.json')['archivos'].items())
assert all((o/f).exists() for f in ['revision_visual_r1.md','revision_r1/INFORME.md','revision_publicacion/revision_integracion_r1.md'])
contracts=J(o/'contratos.json');houses=J(v/'casas.json');packed=J(v/'integracion_paquete.json');source=J(v/'integracion_juego.json')
assert not contracts['errores'] and not houses['errores'] and not packed['errores'] and not source['errores']
assert houses['casas']==200
for kit in ['vivienda_dormitorio','vivienda_joven']:
 d=J(v/(kit+'.json'));assert len(d['resultados'])==81 and not d['errores']
# Mantener las 34 evaluaciones y sus imágenes históricas sin sustituirlas por R1 no puntuada.
for f in v.glob('visual_*_[AB].json'):
 d=J(f)
 if d.get('estado')=='evaluado':assert H(r/d['ficha'])==d['ficha_sha256'],str(f)
e.mkdir()
for sub,name in [('base_T19/capturas','capturas/base_T19'),('prototipo_r1/capturas','capturas/R1'),('revision_r1','revision_tecnica'),('revision_publicacion/inicial_fallido','instrumentacion/inicial_fallido')]:tree(o/sub,e/name)
for name in ['revision_cierre_parcial.md','diagnostico_dormitorio.md','revision_visual_r1.md','integracion_r1.json','estado_candidato.json','regeneracion.json','validacion_inicio.json','validacion_sello_final.json','validacion_ejecuciones.json']:cp(o/name,e/'auditoria'/name)
cp(o/'revision_publicacion/revision_integracion_r1.md',e/'auditoria/revision_integracion_r1.md')
for name in ['resultado_r1.json','camaras_comunes_r1.json','probar_r1.mjs','runtime.cpu.mjs']:cp(o/'medidas'/name,e/'medidas'/name)
for name in ['dormitorio_paquete.json','dormitorio_paquete.log','dormitorio_paquete_corregido.json','dormitorio_paquete_corregido.log','contratos.json','contratos.log','kits5.log','casas200.log','kits81.log','joven81.log','integracion_fuente.log','build.log','recursos.log','marcas.log','integracion_paquete.log']:cp(o/name,e/'gates'/name)
for name in ['casas.json','casas_pueblo.json','vivienda_dormitorio.json','vivienda_joven.json','integracion_juego.json','integracion_paquete.json']:cp(v/name,e/'gates'/name)
for name in ['preparar_cierre_parcial.py','validar_candidato.py','regenerar_comprobar.py','capturador_comun_r1.py','probar_dormitorio_paquete.py','probar_dormitorio_paquete_corregido.py']:cp(o/name,e/'instrumentos_privados'/name)
for f in J(o/'integracion_r1.json')['cambiados']:cp(r/f,e/'fuentes_finales'/f)
# Cobertura del modelo individual compartido; fotos nuevas sin atribuir nueva nota formal.
young=o/'joven_visual'
assert young.exists();tree(young,e/'capturas/joven_compartido')
maxima={k:max(c[k] for c in houses['resultados']) for k in ['triangulos','mallas','luces','montaje_ms']}
rep={'fecha':'2026-10-18','tanda':20,'estado':'avance_parcial_publicacion_solicitada','objetivo':4,'objetivo_4_alcanzado':False,'nueva_puntuacion_formal':False,'base':J(o/'integracion_r1.json')['base_git'],'contratos':len(contracts['pruebas']),'casas':houses['casas'],'habitaciones':houses['habitables'],'maximos':maxima,'kits':{'dormitorio':{'semillas_laboratorio':81,'errores':0,'nota':'R1 sin nueva puntuación; evaluación anterior histórica'},'joven':{'semillas_laboratorio':81,'errores':0,'nota':'Sólo cama individual compartida; resto de programa y paleta sin editar'}},'integracion':{'fuente_errores':0,'paquete_errores':0},'revision_independiente':'data/interiores/revision_calidad_tanda20_2026-10-18.md','pendiente':'Usuario detiene las mejoras y solicita probar lo actual. 4/5 pendiente; centro de sala amplia, ribete morado/alfombra y paños/carteles. CI/Pages y prueba pública todavía pendientes en este commit.'}
W(v/'calidad_tanda20.json',rep)
review='\n\n'.join((o/f).read_text().rstrip() for f in ['revision_visual_r1.md','revision_r1/INFORME.md','revision_publicacion/revision_integracion_r1.md'])
(r/rep['revision_independiente']).write_text('# T20 R1: revisión independiente de la publicación parcial\n\n'+review+'\n')
summary=J(v/'resumen_revision_visual.json');summary.update(objetivo_4='Pausado por el usuario tras T20 parcial: dormitorio y cama individual compartida sin nueva puntuación formal. Las 34 evaluaciones e imágenes conservadas son históricas y no acreditan esta versión.',estado='objetivo_no_alcanzado_mejoras_pausadas_por_usuario');W(v/'resumen_revision_visual.json',summary)
s=J(v/'resumen_viviendas.json');s.update(contratos={'pruebas':len(contracts['pruebas']),'errores':0},maximos_sinteticas=maxima,regeneracion=J(o/'regeneracion.json'),revision_visual=summary);s['calidad_tanda20']=rep
# Los recibos canónicos se regeneran con cinco semillas salvo los dos kits afectados (81).
for item in s['kits']:
 d=J(v/(item['kit']+'.json'));item['semillas']=len(d['resultados']);item['errores']=d['errores'];item['avisos']=sum(len(t.get('avisos',[])) for t in d['resultados'])
s['paquete'].update(maximo_entrada_ms=max(c['entrada_ms'] for c in packed['entradas']),annie_entrada_ms=packed['annie']['entrada_ms']);W(v/'resumen_viviendas.json',s)
text='''\n\n## 2026-10-18 · Tanda20 parcial: dormitorio y pausa solicitada\n\nEl usuario pide detener las iteraciones y publicar todas las mejoras actuales para verlas. Se integra R1: colchones crema, colchas con contraste por estilo, bordes suaves y vuelta de sábana apoyada; suelo y paños calmos orientados por la cama. En amplios se relacionan orejero, superficie y biblioteca con libros apoyados; alfombra vinculada cuando cabe y recuperación existente. Se conservan las reglas de cama, guardado y acciones. Las entradas añadidas consumen azar y pueden cambiar escritorio/decoración posterior; no se promete distribución idéntica.\n\nSólo cambian tres camas adultas del catálogo B; la individual se comparte con cuarto joven y se revalida expresamente. Los otros76objetos B, incluidos clones infantiles, no cambian. Annie mantiene constructor propio. Las revisiones técnica y visual independientes aceptan la publicación parcial, sin defectos bloqueantes confirmados en su alcance. Quedan centro libre, ribete morado de alfombra y paños/carteles; no se abre otra iteración. Las12vistas R1 incluyen10poses idénticas a BASE y2cambiadas de3244, declaradas; no se puntúan para atribuir mejora numérica.\n\nNo hay nuevas llamadas Decision API. Las34evaluaciones e imágenes previas se conservan literalmente como históricas: ni dormitorio ni joven acreditan4/5 en esta versión. Pasan82contratos,40kits×5,200casas/1166habitaciones,81dormitorios,81joven y los diez gates;7generadores reproducen22derivados idénticos. Fuente/paquete, recursos y marcas sin errores. Los tiempos de montaje no sonFPS ni acreditan25% o beta terminada. Dossier: data/interiores/validacion/evidencia_tanda20/manifest.json. Publicación pendiente de CI exacta,Pages y prueba pública en este punto. Tras publicar, se pausa el trabajo por orden del usuario.\n'''
for f in ['docs/calidad-viviendas-4-2026-10-17.md','docs/hiperrealismo-registro.md']:
 q=r/f;t=q.read_text();assert '## 2026-10-18 · Tanda20 parcial:' not in t;q.write_text(t.rstrip()+text)
(e/'LEEME.md').write_text('''# T20 R1 · Publicación parcial solicitada\n\nSe detienen mejoras y se prepara lo actual para ver en Pages. Sin nueva nota formal ni atribución4/5. Las fichas canónicas evaluadas se conservan; capturas nuevas aquí, con diferencias de pose documentadas por revisión. Tres camas adultas cambian; sólo individual se comparte con joven. Annie/infantil sin edición. No se amplían límites, ni luz, cámara mantenida, dependencias o solver.\n\nLas pruebas dirigidas CPU son reales en geometría/collider pero usan Canvas/texturas de prueba y no miden raster o FPS. Instrumentos privados conservados como evidencia, con dependencias de snapshots/rutas locales; no son un entorno autocontenido. El primer probe adicional falló por una premisa del instrumento: junto_a genérico no persiste de. Se conserva el intento fallido y se cambia sólo la comprobación a receta/poses/gap/alineación, con negativos de perturbación; el producto no cambia. La segunda ejecución del paquete debe pasar antes de este cierre. Las herramientas mantenidas y CI son la ruta de reproducción de producto. No contiene credenciales. Recuperación mediante commit de producto anterior c486ed205510c1b94ba013846d17a2a1ad55ed4c. CI/Pages y prueba pública se añadirán al publicar.\n''')
W(e/'manifest.json',{'fecha':'2026-10-18','archivos':{str(f.relative_to(e)):H(f) for f in sorted(e.rglob('*')) if f.is_file() and f!=e/'manifest.json'}})
print(json.dumps({'evidencias':len(J(e/'manifest.json')['archivos']),'contratos':rep['contratos'],'casas':rep['casas'],'habitaciones':rep['habitaciones'],'maximos':maxima,'estado':'preparado_sin_publicar'},indent=1))
