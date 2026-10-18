# T20 R1: revisión independiente de la publicación parcial

# Dormitorio R1 · revisión visual independiente breve

**Aceptable visualmente para la publicación parcial solicitada, con pendientes. No observo en estas muestras un defecto visual bloqueante nuevo.** No se certifica calidad objetivo, funcionamiento ni cobertura completa; no se emite puntuación. No se propone otra tanda ni se condiciona este dictamen a mejoras cosméticas.

Inspeccionadas directamente las dos fichas R1 locales y ambas BASE T19 frescas: doce vistas por versión, dorm 2786/3244/1689 y dorm2 1689/2132/5157. JSON de cámaras contrastados. Identificación recibida: sello R1 de 667 inputs, `74497e2d…af1`; no se ha recalculado ese sello en esta revisión visual. BASE declara commit `c486ed205510c1b94ba013846d17a2a1ad55ed4c`.

- **Cama y compactas:** la sábana clara y colcha verde/azulada distinguen tela y madera; bordes de colchón/almohadas más blandos. Se conservan a la vista cabecero, mesitas y guardado. La eliminación de estampados dominantes, especialmente 5157 dorm2, permite reconocer mejor la cama y el suelo. No veo cama suspendida, desaparición de pieza principal, penetración evidente ni pantalla negra en estas imágenes. Pies y contactos fuera de plano no quedan certificados.
- **3244:** ahora se reconocen cama/mesitas, armario y cómoda, escritorio con silla al fondo, y un rincón separado de sillón–mesita con libro–librería con libros. La lectura doméstica es más clara que el grupo apiñado y librería vacía de BASE. La sala conserva un gran centro libre y mucho paño blanco; es un pendiente de composición, no evidencia de función ausente. Las dos poses cambiaron (FOV 68 y objetivos conservados); no se atribuye toda la mejor cobertura exclusivamente a los modelos.
- **Alfombra 3244:** se ve plana sobre el suelo, sin flotación ni intersección manifiesta. El ribete morado y su posición central siguen pareciendo una isla gráfica poco vinculada al descanso/lectura. La segunda vista la recorta parcialmente. Son limitaciones reales visibles, sin justificar otro retoque antes de la publicación parcial pedida.
- **Pendientes diferibles:** persisten carteles genéricos/repetidos, superficies bastante claras y repetición de la combinación textil. El acabado conserva la simplificación artesanal; esta revisión no exige realismo fotográfico.

**Límites:** diez poses coinciden exactamente con BASE y dos de 3244 difieren. No se han probado circulación, despertar, hide, cajones, botín o persistencia; no se infieren de los píxeles. Las muestras muestran camas dobles: el cambio compartido de cama individual en joven necesita cobertura separada y aquí queda sin verificar. Los clones infantiles y Annie se declaran intactos en el encargo, pero estas fichas no lo acreditan; no se inspecciona ni modifica Annie. Tampoco se cubren Realista, noche o apagón. No hay nuevos renders/GPU, navegador, API, evaluación formal ni edición de producto.

## Huellas de las imágenes inspeccionadas

- `.cache/calidad/tanda20/base_T19/capturas/casa_dorm.jpg`: `dbef107f8f3160025d580ade61a982b1cc762e01cc013e2274108ffee9a6d914`.
- `.cache/calidad/tanda20/base_T19/capturas/casa_dorm2.jpg`: `26524189d101432c5c40a3a3ea02c52bcf2d53877248f1f12b2ea3168dcc6f13`.
- `.cache/calidad/tanda20/prototipo_r1/data/interiores/fichas/casa_dorm.jpg`: `2e78411f4d778c155d38aa6a314f63a80633f7bd4765b629ec2829c63dc62fbe`.
- `.cache/calidad/tanda20/prototipo_r1/data/interiores/fichas/casa_dorm2.jpg`: `f7fe11189a26d0097040498f3848cacba9ca93f829b3d652f4cff8c9f3056b82`.

# T20 R1 · revisión técnica independiente dirigida

**Sin P1/P2 confirmado en el alcance revisado; no bloqueo técnico para integrar esta candidata y ejecutar los gates finales.** No propone otra iteración. El usuario ha pedido detener mejoras y desplegar lo actual; la integración/publicación corresponde a raíz y esta revisión no sustituye sus gates.

Candidata examinada: `prototipo_r1/preparado.json`, SHA `74497e2dffde62ef6ce4975dcd01b218486c918110a8b691305977e0e6afbaf1`, **667 entradas cotejadas**. Los seis archivos de entrada de la prueba dirigida coinciden con el sello final. Producto activo y snapshot no se han escrito. Sólo se generaron estos instrumentos/recibos privados, sin GPU, navegador, API, build ni gates amplios.

## Camas, apoyos y alcance compartido

El catálogo B cambia exactamente `vb_cama_doble`, `vb_cama_individual` y `vb_cama_amplia`. Clase PUSH, masa, roles y demás metadatos funcionales permanecen idénticos; sólo cambian partes y nota. Las envolventes de los tres modelos mantienen sus seis extremos dentro de 1e−6 m. Los demás objetos B son estructuralmente idénticos, incluida la cama infantil: sus copias se crean antes de aplicar la transformación adulta.

La nueva vuelta de sábana apoya sobre la colcha real: nueve rayos por modelo contra geometría Three r170, 27 en total, muestran contacto con diferencia aproximada −2,2e−8 m. No se deduce apoyo sólo del AABB. Colchón y colcha conservan continuidad central y las uniones estructurales previas; no se presenta el modelo textil como un conjunto sin solapes. El colchón crema deja de recibir tinte; sólo el dormitorio aplica la nueva paleta de colcha por estilo. La geometría compartida de **cama individual** cambia también `vivienda_joven`. No hay referencias de doble/amplia en ese kit. Sus notas visuales previas no acreditan el modelo nuevo.

Annie conserva dormitorio propio y no consume el kit de dormitorio ni estos tres modelos. La rama de acabado excluye explícitamente perfil Annie. Es alcance comprobado por fuentes; no se ejecutó su casa en esta revisión.

## Colocación e interacciones

Las entradas de cama/mesitas/armario/cómoda preceden al programa nuevo y mantienen sus reglas. La receta introduce orejero enfrente, superficie/libro y biblioteca vinculados, con recuperaciones existentes; no introduce solver. La biblioteca puede recuperar contra pared si no cabe junto al asiento. No se promete composición agrupada universal ni igualdad de RNG: las entradas añadidas modifican consumo posterior y pueden desplazar escritorio/decoración legítimamente.

Se revisó el recibo de raíz `medidas/resultado_r1.json` y el código que lo genera: 22 construcciones del pueblo/28 dormitorios, cero errores de validar/revisarUso, camas de los mismos IDs/cantidades y ninguna pérdida por **tipo y multiplicidad** de acción en la sala. Ese comparador comprueba inclusión de los tipos anteriores; no prueba identidad, precio o ejecución de cada acción. Máximos declarados allí: 60 mallas y 65.948 triángulos. No se ha repetido ese barrido ni se transforma en validación universal.

La prueba independiente construye 3244, 2720 y 4685 con HouseBuilder, geometrías, agrupación y collider reales, Canvas/texturas de prueba. En las tres:

- El destino final de salida de cama está conectado en mapa de ancho .80, y el collider real con radio .34 devuelve delta/depth0.
- El destino final de la acción hide devuelve delta/depth0. Es el punto ajustado de houses que consume unhide, no el frente nominal del armario.
- Cada orejero y silla de escritorio tiene un único asiento registrado y al menos un punto alcanzable libre, donde es el asiento más próximo y su distancia es menor de1,25 m. Distancias encontradas: aproximadamente .63–.71 m.

En3244/4685 el frente de la silla de escritorio está ocupado por la mesa, como corresponde a una silla que la mira. La comprobación inicial de frente dio `map80:false` y se conserva en el recibo. El acceso lateral/trasero conectado existe y el collider lo confirma; no se corrigió una pose ni se declaró libre ese frente. La selección accesible no equivale a ejecutar sit/standUp ni a probar la animación.

Se revisaron las poses de los nuevos objetos sobre mesa auxiliar/biblioteca en el recibo de las22casas: ninguna penetración con su propio soporte supera .005m usando partes reales. Es relevante porque el motor excluye al padre de colisiones generales. Los controles de reservas, interior y paso del motor siguen vigentes; no se redujeron mínimos ni dimensiones.

## Acabado y caller

La lectura del diff confirma que dorm/dorm2 se revisten después de amueblar, pasando la estancia real, y su zócalo anterior se excluye. El acento elige la pared del cabecero mediante el giro de la cama y mantiene el recorte de huecos existente. Reutiliza la misma familia de material de salón/trofeos y los defines dependen del perfil de la casa, no de una selección tardía por habitación. No se cambian luz, cámara, arquitectura ni colisiones.

La alfombra `vb_alfombra` tiene tapas a .012/.014 m: ambas quedan por encima del acabado nuevo .0095 m. No reproduce el enterramiento de la antigua alfombra de salón. Esto se comprobó en cotas de fuente; no se hizo prueba de píxeles.

## Evidencia y límites

`dirigida.cpu.mjs`, `resultado.json` y `cierre.json` contienen la reproducción, entradas hash y resultados. El primer intento del instrumento asumió `h.levels` obligatorio; falló al llegar a una casa de planta única. Se conserva en `error_instrumento_levels.log`; se corrigió únicamente el acceso opcional y se repitió la prueba. No era un fallo de producto ni se contó como PASS.

**Declined to judge:** calidad visual/nota4, captura o shader WebGL, noche/Realista, acciones ejecutadas y persistencia, recorrido completo del jugador, autoguardado, rendimiento/FPS, 81laboratorios/200casas, CI/Pages/despliegue. La rama `entre` de alfombra obligatoria depende de que exista el sillón y usa el fallback existente cuando falla la colocación; su cobertura global queda a los gates, no al éxito de estas tres casas. No se han alterado umbrales ni añadido excepciones para obtener verde.

Los contratos T23 no se han preparado: no se amplía la tarea tras la orden de cerrar mejoras. Este informe acredita la revisión dirigida del sello indicado, sin presentar pruebas pendientes como terminadas.

# T20 R1 · integración y probe público preparados

**Sin bloqueo de integración identificado en el delta revisado.** La orden actual es detener iteraciones y mostrar el estado parcial. No se exige nueva puntuación ni4/5 para este dictamen. Los gates y la publicación corresponden a raíz y sus recibos; este informe no los anticipa.

Se cotejaron las ocho fuentes activas enumeradas en integracion_r1.json contra prototipo_r1: igualdad exacta. Las417 entradas de estado_candidato permanecen idénticas. El diff activo tiene ocho archivos y no añade un solver ni cambia constructor de Annie.

En catálogo sólo cambian vb_cama_doble, vb_cama_individual y vb_cama_amplia; no se añaden IDs. Los campos fuera de partes/nota (rol, clase y demás metadatos funcionales) son exactos a HEAD. Las variantes infantiles se fabrican antes de la modificación final y no están entre los IDs cambiados. La cama individual también es compartida por joven: su receta no cambia, su modelo sí. Por eso el probe añade la puerta real1594, cuyo kit vivienda_joven está presente en el inventario del pueblo; no fabrica una habitación de laboratorio.

Receta dormitorio conserva camas/armario/cómoda y reorganiza el programa opcional de lectura: orejero, mesa auxiliar, libro, biblioteca y alfombra relacionada. Los umbrales16/22/26 y fallbacks siguen explícitos. El recibo CPU resultado_r1 contiene22construcciones sin pérdidas/errores/uso en sus dormitorios. La revisión CPU dirigida registra mismas envolventes de las tres camas y comprobaciones de apoyos y accesos; son evidencias leídas, no ejecuciones propias. Cambiar entradas de receta puede alterar índices de adornos/semillas posteriores: no se afirma identidad decorativa global.

El acabado de dorm/dorm2 pasa después del kit, orienta el paño por la cama y evita el zócalo antiguo duplicado. La paleta textil nueva sólo se aplica a roles cama en vivienda_dormitorio; no se atribuye esa paleta a vivienda_joven. No se cambian métodos de hide, cama, navegación ni límites de mallas/luces en este delta. La ausencia de errores en estas lecturas no sustituye los barridos200/81dorm/81joven ni el paquete que ejecuta raíz.

## Instrumento público nuevo, aún sin ejecutar

revision_publicacion/verificar_publico.py mantiene roots parents[4], SHA obligatorio y páginas HQ; conserva literalmente los bloques T19 de ocho vecinos/estudios/salones/trofeos/Annie/comercios/persistencia. trofeos_publico.js es copia exacta T19. Añade dormitorios_publico.js antes de Annie, con errores parciales conservados y error global si falla.

El nuevo bloque abre2786/3244/1689/2132/5157 por puertas reales y revisa todas sus estancias vivienda_dormitorio, incluyendo dorm2; abre además1594 real para cama individual joven. Exige registro pieces.bed ligado al índice real, prueba HouseLife.lieOnBed y wake con residente real y salida física libre. En cada armario llama hideIn/unhide reales, comprueba flags/posición y salida con collider. Reposición privada declarada; restaura jugador/cámara y sale de la casa en finally. No fuerza flags de ocultación ni crea jóvenes sintéticos.

En3244 exige silla de lectura, mesa vinculada, biblioteca, libros con soporte nominal correspondiente al catálogo (mesa.555; baldas.04/.42/.8/1.18/1.56), registro único del asiento y acción read. Renderiza y veta shaders no ejecutables. **Límites deliberados:** no raycast de las superficies de libros, no simulación de caminar entre plantas, no inspección visible desde dentro del armario, no activación de leer/sentarse en el bloque dormitorio. La cama se usa por el residente mediante métodos reales; no se inventa una acción del jugador para dormir en cama ajena. La siesta del jugador sigue probándose en Annie mediante el bloque heredado. Persistencia, dinero, caja, decoración y claves Evolución/fija se comparan al final por el wrapper.

Comprobado sólo AST de Python y node --check del JS. Preparado para lectura de raíz y ejecución posterior con SHA publicado; no se ha abierto navegador, GPU ni API, ni se ha hecho build/commit/push/despliegue o edición de producto.

## Huellas

- `.cache/calidad/tanda20/integracion_r1.json`: `13ec3bf055aaefe84366c3a6d434d6a2c5b92e58e438354a38d1755ce55e700f`.
- `.cache/calidad/tanda20/estado_candidato.json`: `fb6194fa3e727b734f69260990ee11523721312fad03a9798637379bccb45052`.
- `.cache/calidad/tanda20/revision_publicacion/verificar_publico.py`: `4aa59e73e110628f080efb9e4d9768fb836c0b15820df655417d0812b72705d1`.
- `.cache/calidad/tanda20/revision_publicacion/dormitorios_publico.js`: `125ecbcd458490f7aa26ec57d89a0b1315937f8a7694b9b57d3e8f623053ba1e`.
- `.cache/calidad/tanda20/revision_publicacion/trofeos_publico.js`: `7225e61b1c30ebf9bac46267a0a78f5047499dfae372bf6d0bb6545232a14dd9`.

## Corrección instrumental posterior a prueba local

La primera ejecución local falló en3244 por una premisa incorrecta del instrumento: exigía table.de===chair.i. src/locales.js, regla junto_a, llama poner sin asignar de; ese campo sólo existe en otros flujos. La escena sí conservaba la relación física. El resultado fallido y los instrumentos originales se preservan en inicial_fallido/. No fue una pérdida funcional del producto ni justifica añadir metadatos a sus fuentes.

La versión corregida exige entradas de receta7/8/12, reglas y zona correctas, volumen finito, orientación común, separación lateral exacta.04m y bordes posteriores alineados mediante longitudinal=hdHijo−hdSillón, tanto para mesa como para biblioteca. Ambos deben flanquear al sillón. Se conserva el resto de apoyos/asiento/acciones. El cálculo sobre el recibo CPU3244 admite ambas relaciones y rechaza perturbaciones independientes de posición lateral, longitudinal, orientación e índice de receta. No se ha ejecutado la nueva versión en navegador; queda pendiente repetir únicamente la comprobación local/pública que raíz considere.

JS corregido: `9fc3bef184e59ca2a5d9d251d612f5134a5cde4cfbfd9770f840c405262e2889`. Wrapper sin cambios: `4aa59e73e110628f080efb9e4d9768fb836c0b15820df655417d0812b72705d1`.
