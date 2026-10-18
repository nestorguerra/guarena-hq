from pathlib import Path
import json,hashlib,shutil,subprocess
r=Path.cwd();o=r/'.cache/calidad/tanda18';v=r/'data/interiores/validacion';e=v/'evidencia_tanda18'
J=lambda p:json.loads(p.read_text());H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def W(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,ensure_ascii=False,indent=1)+'\n')
def cp(p,q):q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
assert not e.exists()
assert len(J(o/'validacion_ejecuciones.json'))==9 and all(x['exit_code']==0 for x in J(o/'validacion_ejecuciones.json'))
assert J(o/'regeneracion.json')['estado']=='PASS'
seal=J(o/'validacion_sello_final.json');assert seal['estado']=='PASS' and seal['freeze_sha256']==H(o/'estado_candidato.json') and seal['validacion_ejecuciones_sha256']==H(o/'validacion_ejecuciones.json')
frozen=J(o/'estado_candidato.json')['archivos'];assert all(H(r/p)==h for p,h in frozen.items())
ficha=o/'final_r8/capturas/casa_salon.jpg';sha=H(ficha)
for s in ['A','B']:
 d=J(o/f'formal_r8/data/interiores/validacion/visual_salon_{s}.json');assert d['estado']=='evaluado' and d['ficha_sha256']==sha
history=v/'historico/calidad_tanda18_r4';history.mkdir(exist_ok=False)
for f in ['data/interiores/fichas/casa_salon.jpg','data/interiores/fichas/casa_salon.json','data/interiores/validacion/visual_salon_A.json','data/interiores/validacion/visual_salon_B.json']:cp(r/f,history/Path(f).name)
for ext in ['jpg','json']:cp(o/f'final_r8/capturas/casa_salon.{ext}',r/f'data/interiores/fichas/casa_salon.{ext}')
cp(ficha,v/f'imagenes/{sha}.jpg')
for s in ['A','B']:cp(o/f'formal_r8/data/interiores/validacion/visual_salon_{s}.json',v/f'visual_salon_{s}.json')
e.mkdir()
def tree(src,tag):
 for p in sorted(src.rglob('*')):
  if p.is_file() and '__pycache__' not in p.parts:cp(p,e/tag/p.relative_to(src))
for folder,tag in [('base_T17/capturas','capturas/base_T17'),('final_r2/capturas','capturas/RECHAZADA_R2_por_coste'),('final_r4/capturas','capturas/final_R4'),('final_r6/capturas','capturas/final_R6'),('final_r7/capturas','capturas/final_R7'),('final_r8/capturas','capturas/final_R8'),('greybox_r4/capturas','capturas/greybox_R4'),('complementos_r4','capturas/complemento_R4'),('complementos_r6','capturas/complemento_R6'),('complementos_r8_comunes','capturas/complemento_R8_comun'),('familia_r8','capturas/familia_R8'),('familia_r4','capturas/familia_R4'),('cazador_r6','capturas/cazador_R6'),('r5_fallo_coste','historico/fallo_coste_R5'),('r6_validado_no_cerrado','historico/R6_validado_no_cerrado'),('ajuste_t20_alcance','correcciones/alcance_T20'),('mezcla_paredes','correcciones/mezcla'),('alfombra_visible','correcciones/alfombra')]:
 if (o/folder).exists():
  # These correction folders contain only small reports/patches; snapshots elsewhere excluded.
  if folder in ['ajuste_t20_alcance','mezcla_paredes','alfombra_visible']:
   for p in (o/folder).iterdir():
    if p.is_file() and p.suffix in ['.json','.md','.patch']:cp(p,e/tag/p.name)
  else:tree(o/folder,tag)
for p in o.iterdir():
 if p.is_file() and p.suffix in ['.json','.md'] and (p.name.startswith(('revision_','diagnostico_','causa_','errata_','R4_fallido','capturas_finales')) or p.name in ['estado_candidato.json','estado_candidato_R4_antes_correcciones.json','regeneracion.json','validacion_ejecuciones.json','CONTINUIDAD.md']):cp(p,e/'auditoria'/p.name)
for folder in ['medidas','postpaso_r3','revision_r3','estar_r7','estar_r8','estar_r7_revision/asientos_fix','contratos_r8','metadata_estar']:
 if (o/folder).exists():
  for f in (o/folder).iterdir():
   if f.is_file() and f.suffix in ['.json','.md','.patch','.log','.js','.mjs','.py']:cp(f,e/'iteraciones_estar'/folder.replace('/','_')/f.name)
for p in (o/'decisions').iterdir():
 if p.is_file():cp(p,e/'juicios'/p.name)
for s in ['A','B']:cp(v/f'visual_salon_{s}.json',e/f'juicios/visual_salon_{s}.json')
for name in ['validacion_inicio.json','validacion_sello_final.json','contratos.json','contratos.log','gates.log','regeneracion.json','validacion_ejecuciones.json','kits5.log','casas200.log','kits81.log','integracion_fuente.log','integracion_paquete.log','build.log','recursos.log','marcas.log']:cp(o/name,e/'gates_finales'/name)
for name in ['casas.json','casas_pueblo.json','vivienda_salon.json','integracion_juego.json','integracion_paquete.json']:cp(v/name,e/'gates_finales'/name)
for name in ['src/composicion_lectura_salon.js','src/composicion_estar_salon.js','tools/interiores/catalogo_vivienda.py','data/objetos/vivienda.json','src/acabados_vivienda.js','src/houses.js','tools/interiores/casas_pruebas.js','tools/interiores/fotos_casa.py','tools/interiores/kits_vivienda.py','data/kits/vivienda_salon.json']:
 cp(r/name,e/'fuentes_finales'/name)
# Maintained contracts, guards and reports are the reproducible product checks. Private snapshot scripts are not self-contained.
notes=J(o/'formal_r8/data/interiores/validacion/visual_salon_A.json')['media'],J(o/'formal_r8/data/interiores/validacion/visual_salon_B.json')['media']
count=len(J(o/'contratos.json')['pruebas'])
(e/'LEEME.md').write_text(f'''# T18: salón, lectura y estar

Programa optativo que compone biblioteca/asiento/apoyo/lámpara ya existentes y sus dependientes después de la receta original (2admisiones reales,20fallbacks). Segundo programa relaciona mesa/alfombra con el sofá existente (5admisiones,17fallbacks). Ambos conservan identidades, índices, botín, activas, guardias y azar del kit; no añaden muebles. Registro funcional del puff admitido, con selección accesible a<1.25m protegida en el segundo paso. Esta distancia radial no certifica salida frontal; Player.standUp dispone de standPos. Rechazo y excepción restauran P/guardias del caller.

Sofás con cojines/brazos redondeados y patas visibles, puff acolchado, alfombra de bandas propia. Catálogo mantiene propiedades funcionales de4modelos salvo nombre/nota/partes; modelos compartidos pueden cambiar otros cuartos, cubiertos por gates funcionales pero sin nueva formal visual allí. Paletas terracota/petróleo por estilo sólo para sofá/puff del salón. No se cambia toda la paleta de la casa. Cal/acento orientado por sofá y suelo doméstico. Cota de alfombra+8mm sólo en casas vecinales: caras .011/.012 sobre piso .0095; no Annie/buildLocal. Raycast cercano no certifica ausencia de cualquier oclusión de mobiliario desde la cámara.

Dos comparadores impuros sort(()=>r()-.5) de onWall/plant se sustituyen por Fisher–Yates local finito. Traza real confirmó diferente número de llamadas al comparador y desaparición del pozo; no se atribuye a caches/JIT. Cambia decoración hall/patio una vez respecto aT17/R4; quedan22 comparadores heredados. No se afirma invariancia de toda la casa histórica. R5 falló61mallas en4204; compartir parámetros domésticos para familia/cazador devuelve60 sin elevar límite.42976triángulos y hash geométrico/RGB invariantes allí no prueban shader idéntico: LINT efectivo cambia en cazador.

Las recetas declarativasR1/R2 perdían phone/drawer por azar alterado y se descartaron. R2de acabados(.94) falló61mallas en6sintéticas. PostpasoR3a/b sin admisiones yR3c con inicio ocupado quedaron rechazados. R7 movía puff por envolvente ampliada y omitía asiento de lectura/corte1.2vs1.25; conservados FAIL/negativos. R8 corrige huella y política: CPU22PASS, poses fuera de movidos exactas y envolventes documentadas aparte. La alfombra perdió motivo_clase en la primera preparación privada: comparación lo rechazó; se restauró antes del snapshot. No se cambian contratos para aparentar que el modelo antiguo y nuevo son idénticos. Las pruebas mantenidas separan invariancia del postpaso y cambios deliberados de geometría/color.

Ficha R8 {sha}: A{notes[0]}/B{notes[1]}, frente a base3.116/3.140. R4 3.38/3.25 yR6 3.148/3.142 conservadas, sin repetir llamada para mejorar nota. Un juicio por lado, mismo modelo/rúbrica y referencias invertidas; no humanos ni verificación funcional. Objetivo4/5 pendiente. Seis poses R8 exactasR6/baseT17; sólo5coinciden con el histórico anterior (2786/0 cambia). R7 usó otras2poses en1594 y no se evalúa formalmente. La antigua pose complementariaR6 ocupa ahora la mesa acercada: guardas vetan foto y se conservaFAIL. Nueva pareja3244 elige punto libre común y comprueba antes/después exactos, conservando las6canónicas.

{count}contratos,40kits×5,200casas/1166habitaciones,81salones,96recorridos y fuente/paquete/build/recursos/marcas PASS. El estado del freeze conserva el momento anterior a los gates; validacion_sello_final.json acredita el cierre posterior. Fuentes congeladas estables y derivados idénticos al regenerar; cifras exactas en gates_finales/regeneracion.json. Delta de instrumentación de metadatos y contratos respecto al snapshot visual se documenta sin cambiar escena. Los manifiestos privados no duplican todas sus entradas aquí; no es una auditoría autónoma. CI, Pages y comprobación pública se incorporarán después; no se presupone éxito posterior.
''')
import importlib.util
credential=Path('/Users/nestorguerra/.codex/automation-support/openai-decisions/decisions_alfred.py');spec=importlib.util.spec_from_file_location('alfred',credential);alfred=importlib.util.module_from_spec(spec);spec.loader.exec_module(alfred);secret=alfred.read_key().encode();assert not any(secret in p.read_bytes() for p in e.rglob('*') if p.is_file());secret=None
W(e/'manifest.json',{'fecha':'2026-10-18','archivos':{str(p.relative_to(e)):H(p) for p in sorted(e.rglob('*')) if p.is_file() and p!=e/'manifest.json'}})
print('Cierre preparado:',sha,notes,'dossier',len(J(e/'manifest.json')['archivos']))
