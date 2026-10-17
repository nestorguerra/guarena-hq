# Comedor T14 — revisión visual del servicio r2

**Conclusión:** mejora cualitativa clara de lectura funcional frente a la primera candidata. Las tres mesas ya se leen como preparadas para comer; la vajilla almacenada y los objetos del aparador se distinguen mejor. No veo una regresión visual bloqueante en estas seis vistas que impida continuar a evaluación formal. Esto no es aprobación de publicación ni afirmación de que alcance 4/5.

Revisión independiente del diseño del servicio: lectura de la ficha JPG y de sus metadatos; sin ejecutar GPU, navegador ni producto, sin puntuación propia y sin nueva llamada de evaluación.

## Inspección de las seis vistas

| Casa | Vista de uso | Vista de conjunto |
|---|---|---|
| 2786, matrimonio/rústico | Se reconocen cuatro sillas y cuatro servicios con plato, cubiertos y vaso; jarra/pan aportan un centro de uso. La mesa destaca por su vajilla clara y ya no por los bloques negros ambiguos. El aparador sigue muy despejado, pero fotografía, envases y vajilla permiten leer uso doméstico. | El conjunto mesa–aparador–estantería se entiende. En las baldas derechas se reconocen platos y tazas, con huecos libres. No aparece la pareja de cuadros idénticos contiguos de la primera candidata. Una hoja roja ocupa el extremo izquierdo del encuadre, sin reproducir la gran ocultación central de 5157 anterior. |
| 5157, matrimonio/antiguo | Dos sillas, dos platos y utensilios orientados hacia cada plaza: el servicio responde al tamaño de mesa. El guardado se ve algo más usado; la botella, tarro y recipiente tienen siluetas diferentes. La estantería estrecha queda muy lateral y su contenido sigue siendo poco legible desde aquí. | El problema anterior de la puerta que tapaba el conjunto queda resuelto en esta nueva captura. Se ven mesa, dos plazas y aparador. Paisaje y cuadro de figura azul son distintos. Permanecen grandes paños vacíos, sobre todo en la pared del fondo. |
| 2606, abuela/antiguo | Cuatro servicios coherentes con las cuatro sillas. Vajilla, vaso/jarra, pan y cubiertos dan una función reconocible al centro. Se distinguen tazas en la estantería y fotografía/utensilios en el aparador. No veo el cubo negro dominante de la primera candidata. | La mesa sigue siendo el foco y se entiende su relación con el guardado. Un solo cuadro pequeño deja gran parte de la pared superior vacía. El encuadre ya no muestra el techo suficiente para resolver el hallazgo anterior de los dos plafones; no lo doy por corregido por ausencia en imagen. |

## Defectos persistentes que pueden limitar el resultado

- **Paredes y densidad:** los planos superiores claros conservan mucho peso, especialmente en 5157 y 2606. Añadir servicios resolvió la mesa; todavía no convierte todo el recinto en un comedor vivido.
- **Variedad entre casas:** se repiten aparador largo, estantería muy estrecha, mismo tono de madera y servicio blanco muy parecido. Cambian plazas, algunos objetos y cuadros; la diferenciación doméstica por perfil sigue siendo limitada. No exigiría más objetos aleatorios para corregirlo, sino otro uso reconocible del guardado o una distribución distinta cuando la geometría lo permita.
- **Guardado:** ahora contiene vajilla reconocible, pero grandes huecos y aparadores muy despejados aún dominan. La estantería de 5157 tiene poca presencia útil en ambas vistas. La función mejora; la densidad percibida no queda automáticamente resuelta.
- **Materialidad y uso:** platos y cubiertos destacan bien, aunque son muy planos/blancos y repetidos; varias plazas parecen el mismo servicio dispuesto de forma rígida. Es un límite del acabado estilizado, no una prueba de error de geometría. No se propone añadir suciedad o dispersar piezas para simular vida.
- **Botín:** la ambigüedad visual de los bloques negros deja de dominar. Algunas piezas del aparador se leen como fotografía, envase o botella; desde estas capturas no se puede certificar su ID, capacidad de recogida ni interacción. «Reconocible» visualmente no equivale a «botín comprobado».

No asigno una nota ni predigo el resultado de A/B. Estos son motivos concretos para que una mejora de lectura funcional no implique necesariamente cumplir el objetivo global.

## Cámaras y alcance de las guardas

La nueva ficha usa FOV 75 y ojo a 1,60 m en las seis vistas. En uso apunta a y≈0,49 m, centro declarado de la envolvente mesa/sillas; en conjunto a y=1,05 m. Esto explica que la cámara mire hacia abajo y muestre mejor tablero y sillas, con mayor presencia del suelo. No es la misma evidencia que las cámaras FOV 68 de la primera ficha: la mejora de encuadre no se atribuye íntegramente al servicio.

El JSON registra 0 esquinas recortadas en las tres vistas de uso: 40, 24 y 40 esquinas evaluadas. Las de conjunto registran 0 esquinas evaluadas y `esquinas_recortadas: null`; no es válido describirlas como otras tres pruebas de cero recortes.

En el muestreo de hojas cercanas, cinco vistas registran 0/35. **2786/conjunto registra 3/35 = 0,085714**, por debajo del límite 0,12. No es un fallo de la guarda; tampoco son cero rayos en toda la ficha. El muestreo acotado no garantiza que cada píxel o cada objeto esté libre de ocultación.

Las diferencias de cámara son declaradas. Las seis vistas actuales son útiles para valorar esta candidata; no constituyen una comparación causal con cámaras idénticas respecto a la primera candidata o la base histórica. El gran obstáculo anterior de 5157/conjunto sí deja de aparecer en la nueva captura.

## Estado técnico y entrega

La raíz comunica 57 contratos y 200 casas PASS; queda pendiente el barrido de 81 semillas por la incidencia de luz genérica 0,029 frente a 0,03. No he reejecutado ni resuelto ese diagnóstico. La aceptación visual para pasar a evaluación formal no elimina ese pendiente ni permite publicar. No certifico circulación real, coste, guardado, botín o estabilidad temporal mediante estas imágenes.

Huellas del material revisado:

- `data/interiores/fichas/casa_comedor.jpg`: `48b820c112a5fa4ac73adca16125f1343e3a80ae07f9a1461a056249f3b0bfc1`.
- `data/interiores/fichas/casa_comedor.json`: `9c59d60f702ecd87b84eb9f46984a97bd00ef9fd0eaf5606dc3eaa011f9774ba`.
- Primera candidata revisada anteriormente: JPG `4f8d9187c9cf785570ab88549a3c0d7a8fff69aebb16a1d018e0c411935bdfe6`; su informe se conserva en `.cache/calidad/comedor_tanda14_revision_preformal.md`.

## Adenda de cierre técnico local T14 — recibos finales

Esta adenda conserva la revisión visual anterior y actualiza sus pendientes técnicos con los recibos finales, sin volver a puntuar ni ejecutar juego/GPU. **Los controles locales revisados están completos y verdes; publicación, CI y comprobación pública siguen pendientes. El objetivo visual de 4/5 no está cumplido.**

- Contratos: 58/58 PASS, `errores: []`. Barrido de casas: 200 casas, 1.166 salas habitables, cero pendientes y errores; barrido del comedor: 81 semillas, cero errores. Se comprobaron también los campos de errores anidados. Los máximos registrados en casas son 70.192 triángulos, 60 mallas, 9 luces y 208,5 ms de montaje. Ese tiempo de construcción no es una medición de FPS.
- Luz del laboratorio: la revisión de código acepta el parche `5b503b2c494b6c5f177f400ad7b2b97eedd1c83c6a3f20f270c7381a7acc4b9f`. El recibo CPU registra 29 fallos de iluminación anteriores frente a cero posteriores, geometría/distribución y determinismo iguales en 81 semillas, tres casas numéricamente iguales y doce laboratorios ajenos sin cambios. Se usa el programa físico doméstico del comedor; no se rebaja el umbral ni se amplía presupuesto. Esto cierra el pendiente 0,029/0,03 de la sección anterior dentro del alcance de esos recibos; no prueba rendimiento ni iluminación de todos los escenarios temporales.
- Integración final: las siete etapas —200 casas, 81 semillas, integración fuente, build, recursos, marcas e integración de paquete— registran salida 0. Fuente y paquete registran ocho entradas de vecinos, Annie con cinco kits y dormitorio personalizado, tres comercios y recarga, con errores y consola vacíos. Fuente añade 96 recorridos de colisión (64 en vecinos y 32 en Annie), sin túneles ni escapes. El recibo de paquete no contiene ese barrido de 96 recorridos: no se le atribuye. Ambas recargas conservan la partida de prueba, decoración y testigos de Evolución/fija.
- Botín v3: los dos recibos finales registran PASS y salida 0. En fuente, recoger el joyero mantiene 321 y añade una pieza a la mochila; la lata eleva el dinero a 555. Tras recarga persisten 555 y el joyero con valor 208. En paquete, el mismo flujo mantiene inicialmente 321, añade el joyero y la lata eleva a 629; recarga conserva 629 y el joyero de valor 201. Las dos mallas recogidas quedan ocultas y los testigos de Evolución/fija se conservan en ambas ejecuciones. Los premios variables entre ejecuciones no se confunden con una discrepancia de persistencia. La raíz confirma que v3 no introduce guardado artificial; se revisaron resultados, no se volvió a ejecutar ni auditar íntegramente el instrumento. La fixture retira residentes, como declara el propio recibo: no certifica testigos/NPC durante el robo. Se conserva v2 como antecedente, sin reemplazar sus resultados.
- Congelación y derivados: se recalcularon los SHA-256 de los 40 archivos de `estado_candidato.json` y los 21 de `regeneracion.json`; todos coinciden con sus registros. El recibo de regeneración declara PASS con los tres generadores. Esta lectura no ejecutó de nuevo los generadores.

La ficha sigue siendo `48b820c112a5fa4ac73adca16125f1343e3a80ae07f9a1461a056249f3b0bfc1`; su JSON sigue siendo `9c59d60f702ecd87b84eb9f46984a97bd00ef9fd0eaf5606dc3eaa011f9774ba`. Las evaluaciones formales guardadas, ambas vinculadas a esa imagen, son A **3,552** y B **3,410**, con `supera_umbral: false`. Son resultados existentes, no una nueva puntuación de esta revisión. Confirman una mejora relativa y mantienen abiertos variedad, composición de paredes y lectura doméstica. Permanecen los límites de cámara ya descritos: sólo uso certifica esquinas completas y 2786/conjunto tiene 3/35 rayos sobre hoja, no cero. La propuesta futura de composición se conserva separada en `.cache/calidad/comedor_siguiente_propuesta.md`.

**Dictamen acotado:** no queda un pendiente técnico local demostrado por estos recibos que impida avanzar al proceso de publicación autorizado. No equivale a publicación aprobada o realizada, a CI verde ni a alcanzar el objetivo artístico. La aceptación visual relativa de r2 y sus defectos persistentes se mantienen.

Huellas SHA-256 de los recibos releídos para esta adenda:

- `.cache/calidad/tanda14/contratos.json`: `65d073e40e90247d17836f636ec99c7909f3abf870c684235d14d86a6bcea939`.
- `data/interiores/validacion/casas.json`: `23c9fc12f343e221147896ce9d1382811e21b4df7c63d015a707aaeb18a5ba38`.
- `data/interiores/validacion/vivienda_comedor.json`: `f7ec81fd028dc0419edd70e98679447cbe6260a030ace1226a9578c694ea8233`.
- `.cache/calidad/comedor_luz_lab_revision_codigo.md`: `3ca5961a23b5d663624e565ea8f086898e6317760c13de146d9a98261d620689`.
- `.cache/calidad/comedor_luz_lab_candidato/cpu_green.json`: `fd36e59ae8b9824eea3fdaf8861fb38e0f89cfcf1c0f6140af70018df98a1e6e`.
- `.cache/calidad/tanda14/validacion_ejecuciones.json`: `929b5fde5cd770aab9332592e9bae7fda6e78a699951ed4256c3f9f5b546f920`.
- `data/interiores/validacion/integracion_juego.json`: `52435def3372cf2b6dda96d1d5d0e834bfdfb57b40d21f17f4cdec12a08e31be`.
- `data/interiores/validacion/integracion_paquete.json`: `e60132adc24a293a35fb8c8cb916088c5a57aa394814da7f7047e4a830083735`.
- `.cache/calidad/tanda14/botin_fuente_v3.json`: `659437d673fc54420238041a7bfc1adb413dbb146c43dddb1dc1916b05f98841`.
- `.cache/calidad/tanda14/botin_paquete_v3.json`: `9baa168966c05ab2ab7846ca9c45d84d0e097a3e7ee0baf47466761ba96e12e3`.
- `.cache/calidad/tanda14/botin_ejecuciones.json`: `888731cf6f2c74991fe8fd72e55d4e8ddc44dd12185f95d6b11c0667c142a67f`.
- `.cache/calidad/tanda14/estado_candidato.json`: `51219587c9c2c30432dd4929daee39c3cb9fde1cfa0053a15ff273e4d6f3faa6`.
- `.cache/calidad/tanda14/regeneracion.json`: `494de69cb56510556c18f311a7694b611ced11bbfc78010420cd33a56adc7357`.
- `data/interiores/validacion/visual_comedor_A.json`: `491db751aa4b050a678b75fceb679df33c6cbd4ad03f1a0b60d1ce0fd9f72849`.
- `data/interiores/validacion/visual_comedor_B.json`: `28740d64f6fc53308226cc5ef9bc57a291bd3fd3a110d8cc3fc9bd86f5493686`.
