# Calidad y rendimiento para la beta pública

Encargo de Néstor: continuar hacia4/5 visual, mejorar al menos25%fluidez y carga, detectar capacidades al arrancar y adaptar calidad silenciosamente. Se mantiene publicación por tandas validadas. Objetivo completo pendiente.

## Plan y evidencia exigida

1. Conservar base3e93087815607c7286959d0913df367dd87f039d y medir antes/después alternados con el mismo Chrome/M1, ventana, ruta, estética, calidad y semillas. Separar optimización a igual calidad de adaptación. Carga: primera visita con caché vacía hasta primer control, además de tiempo de motor y bytes. Fluidez: tiempo de fotograma, p95/p99 y tirones en calle, conducción y viviendas. No presentar una sola muestra ni el tamaño de HTML como25%de tiempo conseguido.
2. Evitar cargar recursos que no se usan. Examinar antialias de pasadas de pantalla y recorridos redundantes. Mantener detalle y funciones; comparar imágenes.
3. Elegir perfil inicial con señales disponibles de Chrome: memoria aproximada, núcleos lógicos expuestos, capacidad WebGL y resolución. No afirmar RAM exacta, modeloCPU ni GPU si están ocultos. Datos locales, sin telemetría ni permisos adicionales. Ajustar después con tiempos reales, histéresis, gracia tras entradas y pausa al ocultar pestaña; conservar selección manual.
4. Validar decisiones con trazas lentas/rápidas/reanudación y navegador real. Probar baja/media/alta, origen y paquete, colisiones/interacciones y recarga de partida ficticia. Revisión independiente antes de publicar.
5. Continuar composición/contraste/variedad hasta que las16estancias y Annie alcancen media4/5 en ambas evaluaciones y ningún criterio<3. La beta pública no se considera lista por superar pruebas automáticas: faltan esa calidad y recorridos de juego en máquinas representativas.

## Punto de partida observado

M1,16GB, Chrome con ANGLE Metal AppleM1;1440×900,devicePixelRatio2,calidadalta,DPRinterno1,5. Primera muestra exploratoria:12,9fps andando,13,5girando,13,8conduciendo; sin errores. No es la comparación final. Construcción de atlas de fachadas y suelo suma aproximadamente4s; motor listo11,8s. Existe adaptación de DPR, pero el dt recortado a0,1s impedía actuar a10fps o menos.

Fuentes: Navigator.deviceMemory y hardwareConcurrency, WEBGL_debug_renderer_info en MDN; Three.jsr170 fijado por el proyecto. El navegador puede redondear, limitar u omitir señales. No se promete fluidez universal en cualquier máquina sin WebGL2 o con recursos agotados.

## Tanda6 publicada: comprobación posterior

GitHub Pages sirve3e93087815607c7286959d0913df367dd87f039d. CI39051716881 y publicación39051966185 terminaron correctamente. El juego público se abrió en contexto privado: ocho casas, Annie (caja fuerte, siesta y decoración), tres comercios y recarga completa de partida321€/700€ sin errores. Las partidas de Evolución y fija conservan sus testigos. Evidencia local: `.cache/calidad/tanda6/integracion_publica.json`.

## Candidata de rendimiento: estado de pruebas

Primera comparación exploratoria, tres rondas alternadas: medianas13,6→16,6fps andando (+22,1%),14,3→18,3 al girar (+28,0%),14,3→17,8 conduciendo (+24,5%). p95/p99 mejoran en las tres rutas. No alcanza25%en todas ni30fps. Esta ronda no sirve para probar carga real: adelantaba la introducción; además clima y semilla de arranque no estaban fijados. Se conserva, sin convertirla en certificación. El nuevo instrumento espera la introducción normal, registra navegación, fija semilla388/clima del juego y repite desde caché vacía.

El controlador permite explorar nitidez por encima del valor inicial conservador, dentro del mismo presupuesto de píxeles. Prueba cada subida durante4s y revierte si pierde fluidez; ocultar/redimensionar cancela la prueba y restaura el estado validado. Los recursos del perfil (sombras, población y materiales) se eligen al arrancar: no se promete reconstruirlos de media a alta durante una partida.18 contratos deterministas en verde, incluida lentitud sostenida alrededor de 1 fps. Las pruebas posteriores de navegador real se detallan abajo.


## Comparación de juego vivo a igual ajuste

Tres rondas alternadas, semilla388 y tiempo local fijo, clima en vivo desactivado, calidad alta y DPR1,5; la introducción termina normalmente. Medianas: andando13,3→17,3fps (+29,6%), girando14,1→18,6 (+31,7%) y conduciendo13,9→18,0 (+29,2%). p95/p99 mejoran en los tres recorridos. Las tres mejoras observadas superan25% de FPS; no llega a30fps en este M1 a ese ajuste. El revisor detecta que las rutas de duración fija recorren distancias distintas:80–83 frente a101–102m andando y137–193 frente a235–290m conduciendo. Por ello no se atribuye todo el incremento al coste de render a escena idéntica. El giro permanece en el mismo punto; se añade una comparación de imágenes/escenas controladas antes de dar por cerrado el umbral. La reducción del tiempo por fotograma es22,6–24,1%, otra magnitud distinta. Evidencia: `.cache/perf-beta/fixed-direct/summary.json`. Carga local28,94→27,17s:6,1%; la carga con red limitada se evalúa por separado.


## Carga fría del paquete

Tres rondas alternadas sin caché, red emulada12Mbps/40ms, misma introducción completa. Mediana50,445→39,208s, reducción22,28%; rangos49,961–51,393 y39,013–41,315s. No se alcanza25%. El HTML de Pages se reduce31,9→19,3MB al descargar la iglesia detallada sólo cuando el modo realista la necesita. Las copias portátiles y multijugador conservan la iglesia integrada. La prueba local usa respuestas sin la compresión que pueda aplicar Pages; no certifica esos tiempos en Internet ni en otra máquina. Evidencia: `.cache/perf-beta/cold-direct/summary.json`.

El primer ensayo de adaptación del paquete falló por una dependencia del instrumento: el ayudante de recorridos importaba `three` sin el mapa de importaciones que sólo contiene la página de desarrollo. Se conserva el fallo en `.cache/perf-beta/adaptacion/report.json`. El instrumento reutiliza ahora ese mapa en su contexto privado antes de importar el ayudante. No cambia el paquete publicado para hacer pasar la prueba.


## Adaptación, compatibilidad e integración verificadas

El tercer ensayo completo del paquete termina sin errores. Al recorrer el pueblo durante 90 s obtiene 30,0 fps medios; el giro posterior de 20 s obtiene 42,7 fps. La adaptación baja el DPR de 1,179 a 0,707 y reduce efectos hasta el nivel 2. Estas cifras incluyen menor resolución y efectos: no equivalen a optimización a calidad constante ni garantizan 60 fps. El cambio a una ventana 4K respeta el presupuesto de 1,8 millones de píxeles. Al volver de suspensión, renderer y controlador coinciden; la selección manual alta y los 321 € ficticios sobreviven a una recarga. Las señales omitidas eligen media y las señales emuladas de 2 núcleos/2 GiB eligen baja sin errores. Son pruebas de selección, no rendimiento de esas máquinas. Evidencia: `.cache/perf-beta/adaptacion-v3/report.json`.

Se conservan los ensayos incompletos: el primero carecía de mapa de importaciones en el instrumento; el segundo agotó el tiempo de recarga al quedar la pestaña de Chrome sin ventana en estado oculto después de una congelación artificial. El instrumento mantiene ahora emulación de foco en su propia sesión y comprueba visibilidad al reanudar. No se modifica el juego para ocultar esos fallos.

Las tres variantes empaquetadas conservan su contrato: Pages pesa 19.318.068 bytes y descarga la iglesia detallada bajo demanda; los HTML portátil y multijugador (31,9 MB) la incluyen. El modo realista cargó el modelo de 10.084.432 bytes con HTTP 200 y sin errores. Ocho casas, caja fuerte/siesta/decoración de Annie, tres tiendas y recarga 321 €/700 € pasan en el paquete; los testigos de las partidas Evolución y fija se mantienen. Evidencias: `.cache/perf-beta/packaged-compatibility.json` e `integracion_candidata.json`.

La comparación visual de nueve vistas antes/después fija DPR 1,5, cámara, hora y clima, e incluye noche, lámpara y tres poses cercanas. Las rutas de render directo, copia sin gradación, depuración AO y destino fuera de pantalla funcionan sin errores WebGL. Las poses estáticas no certifican ausencia de parpadeo en movimiento continuo. La revisión independiente acepta ausencia de regresión importante relativa en los nueve pares. La noche es sólo comparación simétrica: el instrumento no refrescaba el mapa de ambiente ni el vidrio de ventana después de cambiar la hora. No certifica la iluminación nocturna real. El ensayo corregido posterior se documenta a continuación; esta limitación del conjunto original se conserva.

Los resúmenes, trazas, hashes de fuente/paquete y comprobación funcional se conservan en `data/rendimiento/beta_parcial_2026-10-17.json`. Revisión estática independiente sin P1/P2 abiertos; publicación parcial admitida con los límites anteriores.


El ensayo adicional de render estático completó tres rondas, pero su control de igualdad rechazó las tres escenas: cambian la pose residual de una malla y la geometría de los 5.200 puntos del cielo entre sesiones/versiones. Todo lo demás del manifiesto coincide y cada medición permanece estable internamente; eso no convierte el par en una escena idéntica. No se publica un porcentaje causal a partir de este ensayo. Los datos completos se conservan en `.cache/perf-beta/replay-estricto/`; el objetivo de causalidad queda abierto.


## Noche corregida: cierre relativo de tres pares

El conjunto `visual-night-real-v2` registra una actualización forzada del entorno por estado, intensidad ambiental 0,6 de día y 0,45 de noche, y emisión de ventana 0,85 → 0,1. Los seis archivos coinciden con sus hashes; los tres pares conservan cámara, DPR 1,5, luces y clima comparables, sin errores registrados. La revisión visual independiente acepta ausencia de una regresión importante atribuible al postprocesado. Esta muestra corrige la reserva de ambiente y ventana diurnos retenidos en el ensayo anterior.

El techo sigue lavado al mirar la lámpara en ambos pipelines. La iluminación nocturna no queda plenamente resuelta. Son tres pares estáticos de un interior: no certifican exterior nocturno, movimiento continuo, calidad 4/5 ni la tanda 7. Evidencia: `.cache/perf-beta/visual-night-real-v2/report.json`; dictamen: `.cache/revision-visual-post.md`.

## Publicación parcial de rendimiento verificada

El commit `6d34cc384fca3590a00e2cb3286c7e9da7382db8` está publicado y verificado funcionalmente en [Guareña HQ](https://nestorguerra.github.io/guarena-hq/?estilo=plastilina&v=6d34cc3). Se releyeron los workflows: [validación 39055528734](https://github.com/nestorguerra/guarena-hq/actions/runs/39055528734), en `epica-i-interiores`, y [Pages 39055742146](https://github.com/nestorguerra/guarena-hq/actions/runs/39055742146), en `main`, ambos completos y correctos para ese SHA exacto.

El informe público devuelve la misma revisión servida y cero errores registrados. Prueba ocho viviendas, Annie con cinco kits y dormitorio personalizado, caja fuerte, siesta y decoración; también bar, cafetería y farmacia. La recarga conserva 321 € de dinero, 700 € de banco, decoración y los testigos de las partidas Evolución y fija. Evidencia: `.cache/perf-beta/integracion_publica.json`, incorporada al registro JSON de rendimiento.

Esta prueba pública acredita integración, no una nueva medición de velocidad: el instrumento adelanta la introducción y no ejecutó colisiones exhaustivas. La carga medida sigue en 22,28 %, por debajo del 25 %; el replay sigue rechazado como comparación causal. El objetivo visual 4/5 y la beta completa permanecen pendientes.


## Segunda tanda de carga: suelo fotográfico separado

Candidato sobre T12 (`f667142e230a7f52d746f4b69901b1fdfe429bf2`): Pages descarga las doce imágenes de suelo sólo si el modo Realista las pide. Plastilina no las usa. Las copias portátil y multijugador mantienen esos recursos integrados; las tres variantes conservan los bytes originales. No cambia el JavaScript del juego. El contrato de recursos se incorpora a CI y Pages.

En el M1, tres rondas alternadas con caché vacía, red emulada de 12 Mbps/40 ms, introducción completa y calidad alta manual (DPR 1,5) dan **49,859 → 36,9215 s**, reducción de mediana **25,948 %**. Rangos 49,5194–51,4922 s y 36,3212–39,1716 s. Es el resultado acumulado contra la base original `3e93087815607c7286959d0913df367dd87f039d`, no el efecto causal aislado de este último cambio. El servidor local no aplica compresión de Pages; no se garantizan estos tiempos en Internet u otros equipos. Las seis ejecuciones originales, configuración e identidades se guardan en `data/rendimiento/carga_suelo_2026-10-17/mediciones`.

Compatibilidad en el candidato actual: introducción y control en ambos estilos; Plastilina hace cero peticiones de suelo y Realista recibe las doce JPEG y la iglesia con HTTP 200, tamaño exacto y sin errores JS/WebGL. Las capturas fueron inspeccionadas directamente; no constituyen una evaluación artística ni equivalencia de pose entre estilos.

La prueba de ausencia por HTTP devuelve 404 para un albedo y una normal: sólo sus capas son planas, las otras diez responden 200 y conservan detalle, la iglesia carga y el jugador se mueve con entrada real. Cero errores inesperados JS, WebGL o transporte. El 404 opcional de rótulos privados se conserva y se registra aparte, como corresponde al paquete público. No se han probado peticiones pendientes indefinidamente ni todas las combinaciones de recursos ausentes.

La primera versión del servidor de ensayo falló con nueve errores de transporte y queda archivada íntegra; no se cuenta como validación. La segunda amplía la cola y usa HTTP persistente, manteniendo los controles estrictos. El éxito de la segunda no demuestra por sí solo la causa única de los fallos anteriores. Los scripts de `data/rendimiento/carga_suelo_2026-10-17` son copias de auditoría de instrumentos privados, con sus rutas originales; las pruebas mantenidas del repositorio están en `tools/perf/tests`.

El paquete integrado y su publicación se verifican por separado. Esta tanda no resuelve el replay causal de fluidez ni el objetivo visual 4/5.

El build integrado coincide byte a byte con los tres HTML y todos los recursos externos del candidato medido. Pasan los contratos de bytes normal y split, marcas, y la integración del paquete (ocho vecinos, Annie, tres comercios, recarga de partida). Los contratos split se ejecutan sobre la copia física aislada anterior de la misma modificación de build; no prueban comportamiento jugable split. Evidencias y SHA-256 en la carpeta de esta tanda.
