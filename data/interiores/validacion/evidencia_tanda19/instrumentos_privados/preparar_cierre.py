from pathlib import Path
import json,hashlib,shutil,subprocess,importlib.util
r=Path.cwd();o=r/'.cache/calidad/tanda19';v=r/'data/interiores/validacion';e=v/'evidencia_tanda19'
J=lambda p:json.loads(p.read_text());H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def cp(a,b):b.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(a,b)
def W(p,d):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,ensure_ascii=False,indent=1)+'\n')
assert not e.exists()
parts=[o/'revision_visual_r8_completa.md',o/'contratos_t22_r8/INFORME.md',o/'revision_publicacion/revision_integracion_r8.md']
assert all(f.exists() for f in parts),parts
g=J(o/'validacion_ejecuciones.json');assert len(g)==10 and all(x['exit_code']==0 for x in g)
seal=J(o/'validacion_sello_final.json');assert seal['estado']=='PASS' and seal['freeze_sha256']==H(o/'estado_candidato.json') and seal['validacion_ejecuciones_sha256']==H(o/'validacion_ejecuciones.json')
assert J(o/'regeneracion.json')['estado']=='PASS'
assert all(H(r/f)==h for f,h in J(o/'estado_candidato.json')['archivos'].items())
assert J(o/'banco_jugador.json')['estado']=='PASS'
ficha=o/'comparativa_r8_completa/despues/casa_trofeos.jpg';sha=H(ficha)
for s in ['A','B']:
    d=J(o/f'formal_r8/data/interiores/validacion/visual_trofeos_{s}.json');assert d['estado']=='evaluado' and d['ficha_sha256']==sha
history=v/'historico/calidad_tanda19_base';history.mkdir(exist_ok=False)
for f in ['data/interiores/fichas/casa_trofeos.jpg','data/interiores/fichas/casa_trofeos.json','data/interiores/validacion/visual_trofeos_A.json','data/interiores/validacion/visual_trofeos_B.json']:cp(r/f,history/Path(f).name)
for ext in ['jpg','json']:cp(o/f'comparativa_r8_completa/despues/casa_trofeos.{ext}',r/f'data/interiores/fichas/casa_trofeos.{ext}')
cp(ficha,v/f'imagenes/{sha}.jpg')
for s in ['A','B']:cp(o/f'formal_r8/data/interiores/validacion/visual_trofeos_{s}.json',v/f'visual_trofeos_{s}.json')
e.mkdir()
def tree(src,dst,extensions=None):
    for f in sorted(src.rglob('*')):
        if f.is_file() and '__pycache__' not in f.parts and (extensions is None or f.suffix in extensions):cp(f,e/dst/f.relative_to(src))
for src,dst in [('comparativa_r8_completa','capturas/R8_pareja'),('comparativa_r7_consulta','capturas/R7_consulta_no_evaluada'),('prototipo_r6/capturas','capturas/R6_rechazada'),('contratos_t22_r8','contratos'),('fotos_mantenidas','instrumentacion/fotos'),('revision_capturador_consulta','instrumentacion/revision_R7')]:tree(o/src,dst)
for n in ['casa_trofeos.jpg','casa_trofeos.json']:cp(o/'prototipo_r5/capturas'/n,e/'capturas/R5_evaluada'/n)
for n in ['prototipo_r7_final.json','prototipo_r8_final.json','camaras_comunes_r8.json']:cp(o/'medidas'/n,e/'medidas'/n)
for f in (o/'decisions').iterdir():
    if f.is_file():cp(f,e/'juicios/raw'/f.name)
for version in ['r5','r8']:
    for s in ['A','B']:cp(o/f'formal_{version}/data/interiores/validacion/visual_trofeos_{s}.json',e/f'juicios/{version}/visual_trofeos_{s}.json')
for name in ['validacion_inicio.json','validacion_sello_final.json','contratos.json','contratos.log','gates.log','regeneracion.json','validacion_ejecuciones.json','kits5.log','casas200.log','kits81.log','integracion_fuente.log','banco_jugador.log','banco_jugador.json','build.log','recursos.log','marcas.log','integracion_paquete.log']:cp(o/name,e/'gates'/name)
for name in ['casas.json','casas_pueblo.json','vivienda_trofeos.json','integracion_juego.json','integracion_paquete.json']:cp(v/name,e/'gates'/name)
for name in ['revision_visual_final_r5.md','revision_artistica_r7.md','revision_visual_r7_consulta.md','revision_visual_r8_completa.md','resultado_formal_r5.json','resultado_formal_r8.json','estado_candidato.json','integracion_r8.json']:cp(o/name,e/'auditoria'/name)
integration=J(o/'integracion_r8.json')
for f in integration['fuentes_snapshot']+integration['deltas_instrumentales']:cp(r/f,e/'fuentes_finales'/f)
for name in ['verificar_banco.py','validar_candidato.py','regenerar_comprobar.py','decision_visual_privada.py','preparar_cierre.py']:cp(o/name,e/'instrumentos_privados'/name)
notes={s:J(v/f'visual_trofeos_{s}.json')['media'] for s in ['A','B']}
contracts=len(J(o/'contratos.json')['pruebas']);houses=J(v/'casas.json')
(e/'LEEME.md').write_text(f'''# T19: guardar equipo, equiparse y consultar

Frente de armero y guardado bajo, con dos cornamentas referidas a sus módulos. Rifle independiente apoyado en base a0,12m, vano libre y botín/recompensa conservados. Biblioteca de consulta adulta; mapa/atlas propios de geometría original, sin fotografías. Orejero tapizado y mesa de consulta central con holgura32cm en áreas≥11m²; debajo de11 conserva mesita lateral y libro suelto. Esa rama compacta es distinta de la casa2162, que mide11,768m² y sí recibe la mesa central.

Banco zapatero optativo desde13m², unido al frente y con un asiento real libre: botas en balda, bolsa integrada al extremo. No son nuevos objetos recogibles y no sustituyen las pertenencias sueltas. En2132/4204/1679 se admite;2162 conserva su programa sin banco. Reserva frontal y punto real del asiento comprobados con paso80cm. Botas/bolsa apoyadas por geometría real, con negativos de flotación/ausencia/reserva. La prueba de jugador ejecuta selector, sentarse y levantarse desde un acceso libre; no acredita un recorrido humano completo desde la puerta ni animación en todos los equipos.

Siete modelos nuevos y cuatro modelos compartidos cambiados: armero, cornamenta, prismáticos y bolsa. Estos últimos también aparecen en otros cuartos; los gates funcionales los cubren, sus notas visuales anteriores no acreditan esta versión. Pared verde orientada por el armero, suelo/cal más serenos y maderas de mayor contraste. Acabado comparte parámetros y materiales domésticos para respetar el coste. La nueva separación_frontal es optativa .06–1m; default.06, laterales y azar comprobados. No se cambia el límite de mallas.

R8 A{notes['A']}/B{notes['B']}: ninguna dimensión menor de3, **objetivo4 pendiente**. R5 A3,282/B3,112 conservadas; R6 se rechazó por sillón antropomórfico y manta rígida. R7 corrigió el modelo pero mantuvo vacío dominante; se decidió ampliar el programa antes de llamar API. No hubo evaluaciones R6/R7. Una llamada A/B por ficha evaluada, rúbrica/modelo/referencias históricas preservados y respuesta HTTP guardada antes de analizar. Las dos referencias formales no representan las diez entradas completas del moodboard.

Evidencia R8: {sha}. Nuevo protocolo común frente completo/consulta completa a ojo1,60m/FOV68/altaDPR1. BASE conserva exactamente esas seis poses y objetivos, sin añadir las raíces nuevas. No equivale a la cámara histórica ni permite atribuir toda diferencia de puntuación sólo al juego. Guardas12 libres,494inputs estables por snapshot. En2132 la biblioteca oculta el extremo derecho del banco y parte de bolsa; asiento/botas visibles, límite aceptado por lectura independiente. La vista general veta AABB recortadas al seleccionar; consulta añade rayos geométricos escasos y revisión final. Cinco rayos no prueban visibilidad de cada píxel. La herramienta mantenida elimina la lista privada de puntos comunes y añade un veto final al frente, sólo para trofeos. La primera conversión tenía dos condiciones demasiado amplias para otros cuartos: revisión detectó y corrigió antes de integrar, sin cambiar arte ni repetir API.

{contracts}contratos,40kits×5,{houses['casas']}casas/{houses['habitables']}habitaciones,81trofeos,fuente/colisiones, banco real,paquete,build,recursos ymarcas PASS; diez gates. Regeneración determinista con derivados idénticos. Recibos exactos en gates/. No se convierten tiempos de montaje enFPS ni se certifica25% o beta profesional. Fuentes finales coinciden con snapshot salvo pruebas/capturador/CI. CI, Pages y prueba pública se incorporarán tras el commit; no se presupone éxito posterior.

Los instrumentos privados conservan su ubicación original en comentarios/manifiestos y pueden depender de snapshots que no se duplican aquí. No es un entorno autónomo completo. Los contratos y herramientas mantenidas del repositorio son la ruta reproducible de producto. No se copian credenciales.
''')
review='\n\n'.join(f.read_text().rstrip() for f in parts)
(r/'.cache/calidad_tanda19_revision.md').write_text('# T19: revisiones independientes\n\n'+review+'\n')
subprocess.run(['python3',str(o/'cerrar_tanda.py'),'19','trofeos'],check=True)
for f in ['calidad_tanda19.json','resumen_revision_visual.json']:cp(v/f,e/'cierre'/f)
cp(r/'data/interiores/revision_calidad_tanda19_2026-10-18.md',e/'cierre/revision_independiente.md')
append=f'''\n\n## Tanda19: equipo de campo y consulta\n\nLa sala de trofeos organiza guardado, consulta y un banco zapatero optativo para equiparse. El banco se admite en tres casas amplias del pueblo;2162 conserva la consulta sin banco. Los apoyos del rifle, botas y bolsa se comprueban geométricamente; selector, sentarse y levantarse del banco se ejecutan en navegador. Las maderas medias/oscuras y la pared orientada al armero separan mejor los muebles del fondo. El libro abierto y mapa son formas originales, sin fotografías.\n\nNotas A/B **{notes['A']}/{notes['B']}**: objetivo4 pendiente, con todas las dimensiones≥3. R5 3,282/3,112 conservada; R6 rechazado visualmente, R7 no evaluado antes de ampliar el programa. El protocolo nuevo muestra frente y consulta completos en las mismas poses BASE/candidata, altura1,60/FOV68. No equivale al histórico ni atribuye toda diferencia de nota al mobiliario. La biblioteca oculta parte del extremo del banco2132; límite documentado.\n\nPasan {contracts}contratos,40kits×5,{houses['casas']}casas/{houses['habitables']}habitaciones,81distribuciones de trofeos y los diez gates de integración/build/paquete/recursos/marcas/banco. Generadores reproducen derivados idénticos sin elevar límites. Cuatro modelos compartidos también cambian otros cuartos, cuyas notas siguen históricas. Los tiempos de montaje no sonFPS ni prueba universal de25%. Dossier: `data/interiores/validacion/evidencia_tanda19/manifest.json`. Publicación pendiente de commit,CI,Pages y comprobación pública.\n'''
for f in ['docs/calidad-viviendas-4-2026-10-17.md','docs/hiperrealismo-registro.md']:
    q=r/f;s=q.read_text();assert '## Tanda19: equipo de campo y consulta' not in s;q.write_text(s.rstrip()+append)
credential=Path('/Users/nestorguerra/.codex/automation-support/openai-decisions/decisions_alfred.py');spec=importlib.util.spec_from_file_location('alfred',credential);alfred=importlib.util.module_from_spec(spec);spec.loader.exec_module(alfred);secret=alfred.read_key().encode()
assert not any(secret in f.read_bytes() for f in e.rglob('*') if f.is_file());secret=None
W(e/'manifest.json',{'fecha':'2026-10-18','archivos':{str(f.relative_to(e)):H(f) for f in sorted(e.rglob('*')) if f.is_file() and f!=e/'manifest.json'}})
assert all(H(r/f)==h for f,h in J(o/'estado_candidato.json')['archivos'].items())
print('T19 preparada con',len(J(e/'manifest.json')['archivos']),'evidencias; no publicada')
