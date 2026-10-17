# Calidad visual de viviendas: objetivo 4/5

Encargo del 17-10-2026: mejorar primero las habitaciones peor puntuadas y validar y desplegar cada tanda. Base recuperable: c0c4f5315d913d07332fc9e7b2439e36d0923d3b.

Se conserva la rúbrica doméstica de data/interiors_review.json: media de al menos 4 y ninguna dimensión por debajo de 3 en ambas evaluaciones A/B. Las peticiones usan el mismo modelo, referencias y semillas, sin repetir una llamada solo por una nota desfavorable. Las imágenes y los resultados quedan vinculados por hash. Cambiar las cámaras mejora la evidencia visible y se declara; no se atribuye toda diferencia de puntuación únicamente al mobiliario.

## Tanda 1: taller y baño

Base: taller 2,658/2,688 y baño 2,692/2,714. Cambios: banco a altura de trabajo con panel integrado y tornillo, estantería propia, almacenaje agrupado y fondo de menor contraste; en baño, zonas húmeda y de lavabo agrupadas, muebles con contraste, espejo, enseres reconocibles y revestimiento. Los paños respetan puertas y ventanas y no cambian colliders. Los materiales se comparten para respetar el límite de mallas. Se ha reproducido una pérdida de defines al clonar materiales en los lotes: el clon de three.js restablecía los valores estándar. Se conservan explícitamente los parámetros de acabado y se añade una regresión RED→GREEN. El ajuste compartido afecta también a las paredes limpias de las otras salas; sus notas anteriores siguen siendo línea base, no reevaluación de esta versión.

Las capturas conservan las tres semillas anteriores por kit, anotan posición, objetivo y campo de visión de cada cámara y buscan vistas complementarias de los muebles desde suelo libre. No se cambian los planos ni se eliminan ejemplos desfavorables.

Resultado de la tanda: taller A/B 2,842/2,942; baño A/B 2,904/2,754. Ninguno alcanza el objetivo. Pasan 22 contratos, 200 casas/1166 habitaciones, 81 distribuciones de cada kit y el paquete con Annie. Máximos sintéticos: 49172 triángulos, 59 mallas, nueve luces, 145,3 ms. Los artefactos de azulejo se resolvieron mediante piezas coplanares sin solapes; el revisor confirmó las seis vistas. Publicación verificada: commit 005c758, Actions 39045149975 en verde y página pública con ese commit. La integración pública comprueba entrada, caja, siesta, decoración, comercios y recarga sin errores. El primer verificador exigía document.readyState complete en diez segundos; para la web pública se espera al documento nuevo y al arranque real del juego, sin depender de fuentes u otros recursos remotos secundarios. Se conserva ese intento fallido.

Se conservan los intentos de evaluación anteriores en historico/. Algunas capturas intermedias se sobrescribieron antes de conservar su copia exacta; no se atribuye una imagen diferente a esos hashes. Las cuatro evaluaciones finales tienen imagen exacta conservada en imagenes/ y el instrumento guarda esa copia antes de cada petición futura.

## Orden de las siguientes tandas

Trastero y despacho; cocina y costura; después las demás salas en orden de nota. Las salas afectadas por cambios compartidos se vuelven a capturar y evaluar antes de declararlas sobre el umbral. Annie también debe alcanzar el objetivo. El progreso se actualizará con pruebas, notas y commit publicado por tanda.

## Tanda 2: volumen y uso de baño y taller

Se completan las dos salas iniciales con cantos redondeados opcionales, bañera hueca, inodoro con taza y cisterna y lavabo amplio según superficie. El taller incorpora bancos compactos o amplios con tres actividades posibles: casita, marco y motor de riego. Las tres semillas de evidencia muestran casita y motor; no demuestran por sí solas la tercera variante. Las ventanas del baño incorporan privacidad mate. El coste real de la geometría redondeada se contabiliza y un contrato comprueba sus dimensiones y sus 108 triángulos por caja.

Las cámaras documentan uso y conjunto a altura de jugador. Una primera ficha no mostraba el WC del baño 2786; se conserva su evaluación en historico/calidad_tanda2_cobertura_parcial. La cámara secundaria apunta ahora al conjunto sanitario, sin cambiar las semillas. El revisor independiente confirma que ya puede examinarlo. La mejora de cobertura también afecta a las notas: no se atribuye al mobiliario toda la variación.

Resultado final: taller A/B 3,154/3,218; baño A/B 3,036/2,854. Ninguno llega a 4. Pasan 23 contratos, 200 casas/1166 habitaciones y 81 distribuciones de cada kit, además de juego fuente, paquete y control de marcas. Máximos: 56190 triángulos, 59 mallas, nueve luces y 158,5 ms. Regeneración determinista sin diferencias. Publicación de prueba autorizada por tanda; el commit y la revisión pública se registran tras publicarse.

Tanda 2 publicada y verificada: commit 6a214fb, validación 39046360726 y Pages 39046553694 en verde. La integración pública relee ese commit, entra en casas y comercios y conserva caja, siesta y partida ficticia tras recargar, sin errores.

## Tanda 3: trastero y despacho

El trastero incorpora estanterías de tamaño doméstico con cajas, maletas, textiles y archivos integrados, útiles largos y almacenaje adaptado al área. El despacho incorpora mesas con cajonera y lámpara, silla tapizada y rincón de lectura. Suelos y revestimientos reducen los estampados dominantes. Los muebles por kit de todas las casas usan un relieve artesanal más contenido; este cambio compartido requiere reevaluar las otras fichas antes de atribuirles calidad de la versión actual.

Las mismas semillas muestran uso y conjunto, a altura de jugador. Resultado: trastero A/B 3,082/2,894; despacho 3,322/3,304. Continúan por debajo de 4. El revisor independiente considera suficiente la cobertura de estas muestras, sin defecto importante nuevo; señala contraste de blancos, repetición y ajuste visual del despacho 2665. Las imágenes no certifican colisiones ni acceso, que se comprueban por separado. Las pruebas y sus máximos exactos quedan en validacion/calidad_tanda3.json. Pendiente registrar publicación una vez servida.

Tanda 3 publicada y verificada: commit 059f665, validación 39047130127 y Pages 39047293781 en verde. La integración pública sirve ese commit y termina sin errores, incluidas acciones de Annie y recarga de la partida ficticia.

## Tanda 4: luz y oclusión domésticas

Las luces puntuales de las casas no proyectaban sombras y contribuían a iluminar muebles a través de sus tabiques. El render doméstico limita ese relleno por diferencia continua de distancias y utiliza una luz principal con sombra por vista. La sombra se desvanece al cambiar de foco. Los valores originales se restauran al terminar, incluidos apagones, fuego e intensidad de sombra; los mapas se liberan al quitar la casa. Se excluyen comercios y otros edificios.

El primer candidato seleccionaba la sala de forma discreta y el revisor reprodujo un salto visible con un movimiento de 2 cm. El contrato mínimo también falló con un cruce de 2 mm. Se corrigió antes de publicar. La prueba ahora pasa: 25 contratos, cero errores. El revisor repitió exactamente el umbral de la casa 2786 y la bisectriz entre focos, sin salto notable. Esta muestra no certifica todas las puertas y semillas. Los dos candidatos y sus capturas se conservan por separado.

La revisión estática final observa sombras más suaves, volumen conservado y ausencia de regresión importante visible. Notas finales A/B: baño 3,034/2,974; trastero 2,814/2,894. No se alcanza 4 y no hay una mejora uniforme de las puntuaciones. Las evaluaciones anteriores se conservan en historico/calidad_antes_luz y calidad_luz_discreta.

Ensayo acotado en el M1, calidad alta, 960×540, tres baños, doce imágenes medidas por muestra tras cuatro de calentamiento: base 4,8/13,1/13,4 ms; luz final 7,3/14,8/15,1 ms, máximo observado 19,1 ms. Es coste de render sincronizado; no una medida general de FPS ni de todos los equipos. El ensayo inicial discreto se conserva aparte. Los conteos de memoria de la base repiten el estado final de su serie, por lo que no prueban estabilidad temporal ni ausencia de fugas GPU.

Pasan juego fuente, paquete y control de marcas. Datos y modelos son idénticos por hash a la tanda 3: su barrido de 200 casas sigue siendo evidencia geométrica; no se presenta como una nueva ejecución de este render. La integración de esta tanda sí vuelve a probar las 22 casas reales, entradas, Annie, comercios y partida ficticia. API de sombras comprobada contra [la fuente de three.js r170](https://github.com/mrdoob/three.js/blob/r170/src/lights/LightShadow.js). Publicación pendiente de commit, Actions y comprobación pública.


Tanda 4 publicada y verificada: commit 189929e, validación 39048780754 y Pages 39048994637 en verde. La integración pública relee ese commit, conserva la partida ficticia 321/700 tras recarga y termina sin errores.

## Tanda 5: cocina y costura

Los módulos de cocina tienen campana, olla, mandos y dimensiones adaptadas a la sala. La isla conserva cuatro apoyos distintos. Costura incorpora labores de patchwork, bordado o patrones, textiles y panel de carretes. El puesto contra pared se acepta junto con su silla frontal; si falta espacio se prueba otra posición. La validación cuenta el puesto una vez y exige su asiento vinculado. Se conserva el fallo real de asiento alejado en 2606 y el falso exceso del primer contador, corregidos con contratos positivos y negativos.

Se detectó que los alimentos domésticos reutilizaban facings de ocho unidades y bloques de stock comercial. Cocina, comedor y despensa usan ahora 57 recetas unitarias existentes, con su masa individual. Importar el generador comercial no escribe archivos; ejecutar su catálogo produce exactamente los mismos bytes. Se corrigen intervalos de superficie sin cobertura junto a 14/10/10,5 m², sin modificar mínimos.

La oclusión ambiental exterior de 2 m ennegrecía el suelo bajo las sillas. Comparar la misma vista con el efecto desactivado y acotado confirmó su contribución. Las viviendas usan radio 0,85 m, grosor 0,6 m y escala 1,4, mezcla 0,85; los valores anteriores se restauran después de cada vista y los demás edificios conservan su perfil. El primer candidato de radio 0,55 era demasiado plano y se ajustó antes de la ficha final. El revisor confirma las manchas eliminadas y las tres sillas visibles; persiste contraste suave y variedad limitada.

Las cámaras mantienen semillas y altura 1,6 m. La general mira a 1,4 m, antes 1,05 m; costura admite una vista lateral frontal más cercana al eje para no exigir situarse donde está la silla. Estos cambios de evidencia se declaran y no equivalen a mejorar geometría. Todas las evaluaciones finales e intermedias de esta tanda conservan su imagen exacta por hash.

Notas finales A/B: cocina 2,988/3,016 y costura 3,422/3,610. No llegan a 4. Pasan 30 contratos, 200 casas/1166 habitaciones,81 semillas de cocina/costura/despensa/comedor/taller, integración fuente/paquete y marcas, más regeneración de 21 archivos sin diferencias. Los máximos y recibos están en validacion/calidad_tanda5.json. Las otras 15 fichas siguen siendo evidencia de sus versiones anteriores; no certifican este render compartido. Publicación pendiente de commit, Actions y prueba pública.


La tanda5 se publicó como 6d4c9b54ab031e46b416505b5ec7507dedb71c1a. CI39050839250 y Pages39050995955 completadas; la prueba pública relee ese commit, conserva la partida ficticia321/700 tras recarga y acaba sin errores.

## Tanda6: pertenencias del trastero

Bicicleta, escalera con útiles, ventilador y cesto de temporada, modelados con primitivas existentes; estanterías y cajas con mayor contraste. La revisión independiente detectó uniones pendientes en pedestal, pedales y pata de cabra: corregidas y releídas. Tres semillas canónicas1594/3886/4589 seleccionan bicicleta; no se afirma cobertura visual de escalera. El objetivo de cámara cambia al elemento principal, a0,85m, con distancia2,1m y FOV68; altura de observación1,6m. Se penalizan obstáculos opacos delante del foco. La primera vista1594 sigue parcialmente obstruida, con cobertura complementaria en la general.

Notas A/B2,966/2,858: objetivo4/5 pendiente. La ficha también incorpora los ajustes compartidos de render de tanda5; no todo cambio de nota se atribuye a las pertenencias. Se conservan los recibos anteriores e imágenes exactas. Pasan30contratos,200casas/1166habitaciones,81semillas del trastero, integración fuente y paquete, marcas y regeneración de21archivos sin diferencias. Revisión visual independiente sin aprobación formal4.

Tanda 6 publicada y verificada: commit `3e93087815607c7286959d0913df367dd87f039d`, CI 39051716881 y Pages 39051966185. La integración pública conserva la partida de prueba y termina sin errores. La publicación posterior de rendimiento `6d34cc3` conserva esa composición; su evidencia y límites están en `docs/beta-rendimiento-2026-10-17.md`.

## Tanda 7: agrupación y contraste de cocina, baño y trastero

Se permite buscar distintos extremos de un frente modular antes de recurrir a otra pared. La cocina incorpora encimera a 0,89 m, frentes verdes, balda y armario alto preferido, y puertas diferenciadas de nevera. El baño separa sus zonas cuando hay espacio; el trastero agrupa estantes y cajas y evita dispersar los acompañantes opcionales. Los suelos de las tres habitaciones usan tonos medios. Los mínimos, pasos y límites de geometría se mantienen.

Las capturas siguen las mismas semillas y altura de observación de 1,6 m; fijan calidad alta manual y DPR 1. Se corrige la cobertura: la segunda vista de cocina muestra preparación y nevera de frente, y la del baño apunta a 0,8 m para no cortar el WC. No se atribuyen las diferencias de nota sólo al mobiliario; también cambian cámaras y el render compartido. Se conservan los resultados e imágenes anteriores. La evidencia del trastero continúa limitada a tres estudiantes con bicicleta; no prueba la variante de escalera.

Notas finales A/B: cocina **2,934/2,942**, baño **2,986/2,972**, trastero **2,868/2,934**. No hay una mejora uniforme de puntuaciones y ninguno alcanza 4. Persisten vacíos, composición dispersa de cocinas grandes, contraste suave y poca variedad. La siguiente corrección de cocina debe planificar el frente de trabajo completo antes de aceptar cada mueble; añadir detalles aislados ha resultado insuficiente.

Pasan 33 contratos, 200 casas/1166 habitaciones y 81 semillas de cada kit. Integración fuente con 96 recorridos de colisión sin escapes ni atravesamientos, paquete, partida ficticia, marcas y regeneración de 21 archivos sin diferencias. Máximos sintéticos: 70.556 triángulos, 59 mallas, nueve luces y 171 ms de montaje. No son una certificación universal de rendimiento. La publicación de esta tanda queda pendiente de su commit, Actions y comprobación pública.

La revisión final detectó sólo 8,3 cm delante del WC de la casa 3244, aunque no había interpenetraciones. Se añade una reserva física de 0,60 × 0,65 m delante del inodoro; no crea un obstáculo para el jugador. El algoritmo prueba otra posición de los muebles y el validador comprueba el hueco por separado. El nuevo contrato falla antes de la corrección y pasa después, incluido un bloqueo deliberado. Se conservan las dos evaluaciones del candidato estrecho (3,010/3,014) y sus imágenes en el histórico. La reserva no certifica accesibilidad normativa ni el acceso universal a ese rectángulo; el paso y las interacciones existentes se comprueban aparte.


Tanda 7 publicada y verificada: `44e3de33d69b5cf2a4822bc7abe8ed146fdc7fa8`, CI 39057155420 y Pages 39057301779 en verde. El juego público sirve ese commit, permite entrar en ocho casas, conserva la caja fuerte, siesta y decoración de Annie, y mantiene 321 € / 700 € tras recargar; tres comercios con compra y cero errores. Recibo: `data/interiores/validacion/publicacion_tanda7.json`.

## Tanda 8: contraste de luz doméstica

Se reduce el relleno ambiental durante el dibujo de casas en Plastilina y se restauran sus valores al salir de cada vista. La escena de calle por la ventana, comercios y Realista conservan sus valores. La comparación de ocho pares mantiene cámara, habitación, hora, clima y calidad alta manual. La mejora diurna es moderada; no resuelve las paredes vacías ni la distribución. El primer candidato oscurecía demasiado los apagones: se conserva su evidencia y se excluyen las casas sin electricidad del ajuste final.

Notas A/B actuales: cocina **3,040/3,042**, baño **3,152/3,018**, trastero **2,938/2,700**. No hay mejora uniforme y ningún kit llega a 4. El procedimiento y las semillas se mantienen; los cambios de estas seis notas no certifican las otras 14 fichas ni eliminan la variabilidad del juicio. Los resultados e imágenes anteriores se conservan. La revisión de noche en cocina queda limitada por un residente que tapa parte de la encimera en ambos candidatos.

Nueve contratos de luz y restauración pasan. La geometría es idéntica a tanda 7: sus 33 contratos, 200 casas y 81 semillas por kit se conservan como evidencia previa, sin presentarlos como nuevas ejecuciones. La integración completa del primer paquete de tanda 8 pasa; el paquete final corrige únicamente el guard de apagón y se comprueba por separado. Publicación pendiente de ese caso dirigido, revisión independiente, commit, Actions y prueba pública.


El caso dirigido de apagón se ha ejecutado sobre el paquete final: cámara, estado, PMREM, HouseLife e intensidades coinciden con la base anterior; cero errores y contexto privado cerrado. El ambiente permanece en 0,45 durante y después del render. No se vuelve a puntuar la misma ficha diurna, cuyo render no cambia al añadir el guard.

Tanda 8 publicada y verificada: `313cf52da64c844941b5723326ad73716e2c00dc`, CI 39057951048 y Pages 39058116327 en verde. El juego público sirve ese commit. Ocho casas, Annie (caja fuerte, siesta, decoración), tres comercios y recarga con 321 € / 700 € pasan sin errores; las claves Evolución y fija conservan sus testigos. Recibo: `data/interiores/validacion/publicacion_tanda8.json`.

## Tanda 9: frente de cocina y pertenencias del trastero

La cocina busca y acepta conjuntamente los tres módulos del frente de trabajo, con prueba de orden espacial inverso y sin consumir el azar compartido si falla. La revisión estática detectó referencias ramificadas incorrectas: se exige referencia al miembro inmediato y se conserva el fallo anterior como regresión. Las tres cocinas canónicas reúnen cocción, preparación y nevera. El trastero añade bicicleta con carga, útiles de mantenimiento y contraste de ventilador y pared; se corrigen eje del portaequipajes, margen del sillín y cobertura de la variante nueva antes de integrar.

Notas A/B: cocina **3,176/3,094** y trastero **3,252/3,048**. Mejoran respecto a tanda 8, pero no alcanzan 4/5. La revisión independiente acepta las muestras con límites: quedan paños altos vacíos, altos de cocina pequeños y almacenaje del trastero poco relacionado con la bici. Las cámaras del trastero coinciden con la tanda anterior; las de cocina cambian por la nueva colocación, conservando algoritmo, semillas, altura y campos de visión. No se atribuye toda la diferencia de nota al código. Las otras 15 fichas conservan sus evaluaciones anteriores y no acreditan esta versión compartida.

Pasan 40 contratos, 200 casas / 1166 habitaciones, 81 semillas de cada kit afectado, integración fuente con colisiones, paquete y marcas. Máximos sintéticos: 70.578 triángulos, 59 mallas, nueve luces y 168,1 ms de montaje. Los siete generadores reproducen 21 archivos idénticos. La revisión estática y visual se conserva en `data/interiores/revision_calidad_tanda9_2026-10-17.md`. Pendiente de commit, Actions y prueba pública de esta tanda.

Tanda 9 publicada y verificada: `6186c7ba99ca0a8dafa2690a4aaa5873822329d1`, CI 39058481610 y Pages 39058656031 en verde. La integración pública relee ese commit, entra en ocho casas, conserva las funciones y decoración de Annie, compra en tres comercios y mantiene 321 € / 700 € tras recargar; cero errores. Recibo: `data/interiores/validacion/publicacion_tanda9.json`.

## Tanda 10: relaciones entre muebles y proporción de los altos

Los baños amplios componen dos grupos: aseo con armario y zona húmeda con ducha/bañera. La búsqueda del frente reserva también el hueco lateral real de la toalla antes de comprometer el lavabo. El primer candidato perdía la bañera de 3244 y dejaba la toalla alejada: se rechazó, se conservaron sus fallos y se corrigió sin relajar los contratos. El color superior destaca sólo la pared del lavabo amplio; las restantes son claras. El baño compacto conserva su programa.

Los altos de cocina tienen anchura acorde con la preparación y diseños clásico, liso o mixto según el estilo. Los frentes bajos usan la madera del estilo. El trastero coloca la pertenencia junto al primer estante antes de prolongar el almacenaje; mantiene su fallback y mínimos. No se cambian dimensiones de las habitaciones en esta tanda.

Notas A/B: cocina **3,050/3,048**, baño **3,210/3,132** y trastero **3,302/3,076**. Baño y trastero suben ligeramente; cocina no mejora la nota anterior y sus frentes claros pierden algo de contraste. No se alcanza 4/5. Se conservan recibos e imágenes anteriores. La revisión independiente acepta la mejora acotada y declara cobertura parcial de la bañera 3244 y bicicleta 3886. Las otras 14 fichas mantienen evidencia histórica; no acreditan el render actual.

Un ensayo aislado de luz cenital comparó 14 parejas sobre la misma base T9, con geometría, estado y cámaras iguales. Contenía el techo lavado, pero introducía estrías en espejos y muebles. Se rechaza: este código sigue usando la luz puntual anterior. El primer ensayo abortó por una precondición incorrecta del instrumento sobre clearGlass de Annie; se conservó y corrigió sólo el instrumento antes de la comparación completa. Ninguno de esos ensayos acredita la calidad 4 ni forma parte del despliegue.

Pasan 45 contratos, 200 casas / 1166 habitaciones y 81 semillas de cada kit afectado. Máximos sintéticos: 70.192 triángulos, 59 mallas, nueve luces y 166,7 ms de montaje. Siete generadores reproducen 21 archivos idénticos. Integración fuente con colisiones, paquete, partida ficticia y marcas comprobados; evidencia de ejecución en validacion/calidad_tanda10.json y revisión independiente en data/interiores/revision_calidad_tanda10_2026-10-17.md. Publicación pendiente de commit, Actions y comprobación pública.

Tanda 10 publicada y verificada: `48f77feceef519c3ede275a00db0e6630aa50b07`, CI 39059812292 y Pages 39060045909 en verde. La versión pública sirve ese commit y pasa ocho casas, funciones y decoración de Annie, tres comercios y recarga de la partida ficticia con 321 € / 700 €; cero errores. Recibo: `data/interiores/validacion/publicacion_tanda10.json`.

## Relectura tras tanda 10

Se actualizan trece fichas y sus 26 evaluaciones con el mismo procedimiento, calidad alta manual y DPR 1. Las tres estancias de tanda 10 no se repiten; Annie mantiene evidencia histórica. Hay así dieciséis kits con capturas actuales, ninguno aprobado por ambos revisores. Niños queda en 2,978/2,900, despensa en 3,058/3,092, y costura en 3,480/3,602. Las diferencias pequeñas de nota no fijan un orden preciso; se priorizan niños y despensa por sus defectos visibles de escala y composición. Esta actualización amplía la evidencia, no acredita una nueva mejora del código. Se preservan fichas/recibos anteriores en historico/antes_relectura_tanda10; detalle en validacion/relectura_tanda10.json.


## Tanda 11: cuarto infantil y despensa

El cuarto infantil usa cama con cajones, armario y estante de escala propia. Conserva cama utilizable, ocultación y puesto de deberes con silla vinculada. El suelo de tabla ancha, el color inferior y la alfombra opcional reducen el ruido del acabado anterior. Las pertenencias son cuentos, juegos y objetos de estudio de altura adecuada; se mantienen los muebles compartidos de otros dormitorios.

La despensa agrupa estante, aparador y módulo alto. Alterna envases domésticos con huecos entre grupos y conserva los mínimos y el fallback cuando el frente no cabe. Sus paredes y suelo separan mejor los muebles. La revisión independiente detectó una botella de vinagre que penetraba 7,5 mm en la tapa: se excluyó del estante bajo y un contrato exhaustivo protege el hueco real de todas las baldas. También se corrigieron los cajones infantiles coplanares y sus tiradores enterrados.

Notas A/B: niños **3,130/2,944** (antes 2,978/2,900); despensa **3,278/3,348** (antes 3,058/3,092). Ninguno alcanza 4/5. En despensa, iluminación/contraste supera 4 en ambos juicios; densidad, variedad y lectura funcional siguen pendientes. Los nuevos muebles cambian las vistas automáticas; no se trata de una comparación de cámaras idénticas. Se preservan imágenes y evaluaciones anteriores en historico/calidad_tanda11_base. Las otras fichas conservan su evidencia anterior, sin recertificar el render compartido.

Pasan 49 contratos, 200 casas / 1166 habitaciones, 81 semillas de cada kit y 96 recorridos de colisión. Máximos sintéticos: 70.388 triángulos, 60 mallas, nueve luces y 148,8 ms de montaje. Los generadores afectados y el compilador reproducen 21 archivos idénticos. Integración fuente y empaquetada, marcas y persistencia de partida ficticia pasan. Ocultación comprobada en 4007/5045 y en la muestra sintética 1296 con puerta temporal, sin añadirla al inventario; se conserva el primer fallo del instrumento por buscarla como puerta real. Capturas y alcance en validacion/tanda11_armarios.json.

La revisión visual independiente no identifica regresión bloqueante; quedan espacios demasiado vacíos y poca identidad infantil. Siguiente tanda: dibujos infantiles propios, textiles y alfombra de juego, conservando mobiliario funcional y reservas. La luz cenital experimental y la optimización de carga de suelo permanecen fuera de este despliegue. Publicación pendiente de commit, CI y comprobación pública del SHA exacto.
