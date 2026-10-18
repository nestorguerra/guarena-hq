# Revisión visual de cocina y baño — tanda 7

17 de octubre de 2026. Revisor 2. Revisión cualitativa sin puntuación ni aprobación formal.

**Hallazgo del WC 3244 cerrado tras la corrección y la revisión de la ficha de 20:09:35.** Se conserva más abajo el episodio anterior, que sí bloqueaba publicar aquella distribución. Este cierre se limita al espacio frontal; no certifica calidad visual 4/5 ni aprobación del usuario.

## Alcance y autoría

Se inspeccionan las fichas locales y sus JSON de las semillas 2786, 3244 y 1594, en estética plastilina, calidad alta y DPR 1. Cocina definitiva: 20:04:54. Baño definitivo tras corregir el WC: 20:09:35; se conserva el contraste con la ficha previa de 20:03:34. Se contrastan con las fichas anteriores inspeccionadas durante esta tanda y con el volcado inicial `.cache/calidad/tanda7/posiciones.json`.

El revisor no ha construido los cambios de cocina o baño del juego. Sí ha corregido el helper `tools/interiores/fotos_casa.py`: segunda vista de cocina hacia preparación y nevera, frontalidad normalizada, y segunda vista de baño hacia el WC a altura objetivo de 0,8 m. Por tanto, esta es una revisión independiente del contenido de esos dos kits; la comprobación del helper propio no constituye revisión independiente de su implementación. La raíz ha ejecutado las capturas. Este revisor ha usado imágenes locales, lectura de fuentes y parseo estático, sin iniciar navegador ni pruebas GPU.

El trastero queda excluido: este revisor ha editado su generador. No se certifican en este informe rendimiento, integración, publicación ni el objetivo formal de 4/5.

## Mejoras observadas

- **Cocina 2786:** preparación, nevera y cocina se reconocen como frente doméstico. Frentes verdes y tableros claros se separan mejor que los anteriores muebles marrones; el alto con balda y vajilla aporta una segunda altura legible.
- **Cocinas 3244 y 1594:** las vistas secundarias definitivas muestran el frente de preparación y el frigorífico. En 3244 ya se ve la cara de la encimera; la primera recaptura mostraba el lateral de la nevera tapándola. Se retira la sospecha de ausencia: esos objetos existían en la pared opuesta al fuego, como confirma el volcado de posiciones.
- **Baño 2786:** la segunda vista incluye ahora asiento y cuerpo completos del WC, antes cortados por el borde inferior. El interior oscuro se distingue mejor del borde blanco.
- **Baños 3244 y 1594:** lavabo, espejo, bañera, sanitario y almacenaje se identifican entre las dos vistas. La lectura del suelo mejora respecto al fondo casi blanco anterior. No se observan muebles flotantes nuevos en estas imágenes.

## Reservas concretas

1. **Histórico, ahora corregido: espacio frontal insuficiente del WC en 3244.** En la ficha previa, WC, extremo de bañera, armario y cesto estaban concentrados en un extremo, mientras quedaba una superficie central amplia. El volcado inicial sitúa el WC con `ry=0`, en z local 0,3200, y la bañera perpendicular, en z 1,4325. Con las dimensiones del catálogo, el borde frontal del WC llegaba aproximadamente a z 0,6468 y el extremo de la bañera comenzaba en z 0,7300: unos **8,3 cm** entre ambos en esa dirección. Era un cálculo geométrico; no se ejecutó una prueba de uso. La raíz confirmó que el WC había pasado de x local −1,8196 en la base anterior a −2,5096 en aquella distribución, con la misma bañera, y bloqueó su publicación. Se conservan las posiciones iniciales y el contrato RED real en `.cache/calidad/tanda7/contratos-wc-red.json` y `contratos-wc-red.log`: 33 pruebas, tres fallos, incluido el caso 3244 por uso frontal ocupado. Este episodio no se reclasifica como una simple limitación de cámara.

2. **Grandes superficies vacías y poco contraste en salas grandes.** En cocinas 3244/1594 persisten zonas de trabajo separadas y paños grandes sin una relación visual fuerte con los muebles. En los baños grandes, los aparatos se concentran en extremos y el suelo y la pared dominan el conjunto. La nueva paleta ayuda, pero no resuelve por sí sola la distribución. El vacío se conserva visible; no se ha reducido el campo de visión para disimularlo. Conviene resolverlo mediante colocación de piezas existentes antes de añadir objetos o detalle.

3. **Cobertura de cámara limitada.** La secundaria de cocina documenta preparación y nevera; no es una panorámica completa de todas las paredes o de la mesa. En baño 2786 prioriza el WC y deja recortada parte alta de la ducha. La ducha de 3244 no queda documentada de forma suficiente entre ambos encuadres; sí existe en el volcado de posiciones. En 1594 la ducha y la bañera se reconocen en la secundaria, con limitaciones de encuadre. Estas limitaciones no deben traducirse en ausencia de objetos ni corregirse rellenando el cuarto.

## Corrección del espacio frontal y comprobación final

Se ha leído el diff de `src/interiores_geo.js`, `src/locales.js`, generador, esquema, validador y contrato. Las dos entradas WC declaran `espacio_frontal: [0.6, 0.65]`, interpretado como anchura y fondo. La reserva se orienta con el sanitario, comienza en su frente real y se comprueba dentro de la sala y contra las piezas de otros objetos.

- **Índice de entrada:** en `cierra`, `p.e ?? entrada` conserva la entrada original de objetos ya colocados y cubre candidatos WC todavía sin `e`, tanto en `enfrente/contra_pared` como en `junto_a`. `poner` fija el índice y los constructores de vecinos y Annie lo trasladan al validador. No se ha encontrado un defecto de índice en estas rutas actuales.
- **Paso:** el rectángulo de uso no se añade a geometría, collider ni `mapaPaso`. Las comprobaciones anteriores de paso y funciones siguen ejecutándose después de la reserva. Por tanto, la reserva no crea por sí misma un obstáculo virtual.
- **Validador y contrato:** el validador contrasta la reserva con las piezas reales. El contrato conserva el caso de las tres semillas e introduce una ducha delante del WC para exigir el diagnóstico `uso frontal:`. La detección no depende únicamente de las cajas `v` previamente guardadas.
- **Límite del mecanismo:** comprueba hueco físico libre; no añade un objetivo específico de alcanzabilidad hasta el rectángulo del WC. No se ha identificado en las tres imágenes actuales un caso que falle por ese límite. No se extiende este cierre a otras reservas hipotéticas o a todas las configuraciones posibles.

Resultados leídos en los archivos de la raíz, sin lanzar GPU desde esta revisión:

- `.cache/calidad/tanda7/contratos-wc-green.log`: **33 pruebas, cero fallos**.
- `.cache/calidad/tanda7/casas-wc.log`: **200 casas, 1166 estancias por kit, cero casas con errores**.
- `.cache/calidad/tanda7/bano-wc-corregido.log`: **81 semillas de baño, todas con cero errores**. El primer intento, conservado en `bano-wc.log`, falló al interpretar una lista vacía y no ejecutó validación; no se cuenta como resultado válido.
- `.cache/calidad/tanda7/fotos-bano-wc.log`: tres casas capturadas.

La ficha nueva y el JPG individual de 3244 muestran la bañera junto al lavabo, separada del WC. El suelo delante del sanitario queda despejado y ya no aparece el extremo de la bañera a pocos centímetros de la taza. Se mantienen el WC completo de 2786 y la lectura de los aparatos en 1594. No se detecta una nueva interpenetración visible. **La evidencia geométrica, la validación y la imagen son suficientes para cerrar el hallazgo concreto de los 8,3 cm.**

## Cierre

Quedan corregidos los problemas concretos de cobertura de preparación/frigorífico, el corte inferior del WC 2786 y el espacio frontal insuficiente del WC 3244. Este último deja de bloquear por el motivo descrito; no se afirma que todos los requisitos de publicación estén cerrados. Persisten las reservas de composición, contraste y cobertura parcial descritas, con superficies amplias vacías todavía visibles. No se certifica alcanzado el objetivo visual ni se atribuye aprobación al usuario.

No se solicitan más recapturas para buscar una nota favorable. La evaluación formal corresponde al procedimiento separado de la raíz y debe conservar sus resultados desfavorables.
