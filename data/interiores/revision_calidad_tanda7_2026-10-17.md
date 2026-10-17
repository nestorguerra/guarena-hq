# Revisión independiente de la tanda 7

Compilación de los dictámenes originales, conservados en los archivos indicados. El autor de cada cambio no es quien aprueba su resultado. La aceptación de integración no equivale a la calidad formal 4/5.

## data/interiores/revision_codigo_tanda7_2026-10-17.md

# Revisión independiente de código — tanda 7

Fecha: 2026-10-17. Base HEAD: `6d34cc384fca3590a00e2cb3286c7e9da7382db8`.
Objeto: diff de trabajo y fuentes actuales; no un rango de commits. Revisor independiente de esta implementación. La propuesta de luz de tanda 8 queda fuera.

## Dictamen

**Aceptación estática del código de tanda 7: sin hallazgos P1/P2 nuevos que bloqueen su integración.** No equivale a aprobación visual, publicación ni cumplimiento de 4/5. Las correcciones de cámara que otro agente realiza después de esta lectura deberán revisarse por separado.

## Comprobaciones y evidencia

- `src/locales.js:165–191`: `buscar_refs` es optativo. Sin él se conserva la última referencia; con él se prueban referencias y lados, sin retirar las comprobaciones de contención, volumen libre ni accesibilidad. El salto de bucle termina ambas búsquedas al colocar una pieza. El fallback sigue condicionado por `si_no`; los acompañantes del trastero que lo desactivan no terminan dispersos por otra pared.
- `src/locales.js:296`: la regla `pared` emplea la misma función `cantidadPreferida` que otras reglas. La cantidad sigue dentro del rango declarado; permite intentar el armario alto opcional cuando se solicita `preferir`. Puede cambiar la secuencia de distribución de semillas respecto a la versión anterior; no introduce aleatoriedad externa.
- `data/kits/kit.schema.json`: extensión booleana compatible y opcional. Ejecutado el comprobador real de esquema sobre todos los JSON de kits: cero errores.
- Cocina: se priorizan el módulo alto y los frentes contiguos; no se retiran los muebles obligatorios. Baño: las dos entradas de inodoro tienen condiciones complementarias, `<10` y `>=10`; no están activas a la vez en el umbral. La regla `enfrente` mantiene su fallback a otra pared si la opuesta no admite el objeto. Trastero: las piezas mínimas admiten fallback y los acompañantes opcionales sólo se aceptan agrupados.
- Generador de catálogo ejecutado en memoria, sin escritura: sus 158 objetos coinciden exactamente con `data/objetos/vivienda_a.json`, con 158 identificadores únicos. Generador de kits ejecutado con escritura sustituida por captura en memoria: entradas de cocina, baño y trastero coinciden con los JSON actuales, incluida normalización de lámparas.
- Los siete objetos modificados se comprobaron con las funciones reales `alto` y `triangulos`: ninguno baja del suelo, todas las superficies declaradas tienen pieza de apoyo, y costes entre 288 y 1296 triángulos por objeto, por debajo de 5000. El mínimo vertical del armario alto es 1,3275 m, coherente con soporte de pared. La encimera conserva el plano útil en 0,89 m; vasos del armario apoyan sobre la balda en 1,3525 m.
- `src/acabados_vivienda.js`: cambios de colores del suelo; no modifica huecos, posiciones, colisiones ni materiales de interacción.
- `tools/interiores/casas_pruebas.js`: los dos contratos nuevos incluyen el caso de referencia bloqueada y una comprobación negativa con `buscar_refs=false`, además del intento de armario preferido en seis semillas. No se ha debilitado un criterio existente.
- `tools/interiores/fotos_casa.py`: el contexto privado y calidad alta manual/DPR1 evitan heredar la partida o adaptación de una sesión real. El registro incorpora calidad y DPR.

## Evidencia existente releída

`.cache/calidad/tanda7/contratos.json`: 32 contratos y cero errores. `.cache/calidad/tanda7/pasos.json` registra salida 0 de datos, contratos, 200 casas, laboratorio de semillas y capturas. Estas ejecuciones pertenecen a la cola del agente raíz; el revisor no abrió navegador ni las repitió. Las verificaciones propias fueron offline y en memoria.

## Pendientes y Declined to judge

- Cobertura visual de las cámaras de cocina y baño: raíz ha detectado muebles fuera de encuadre y WC cortado; otro agente está corrigiendo exclusivamente ese capturador. La versión de fotos identificada abajo no queda certificada como cobertura suficiente.
- No se puntúa 4/5, estética, contraste ni iluminación por este informe. Las imágenes anteriores no sustituyen las capturas finales y sus evaluaciones.
- No se evalúa ni aplica `tanda8_luz.patch`, ni se atribuyen mejoras de render a ese parche.
- No se certifican FPS, GPU, render final, despliegue ni compatibilidad del paquete a partir de pruebas estáticas. No se ejecutaron commit, push ni publicación.
- La revisión geométrica offline no demuestra ausencia universal de solapamientos visuales en todas las semillas. Los guardias y la evidencia de 200 casas/81 semillas acotan los casos probados.

## Identidad de los archivos leídos

- `src/locales.js`: `eebb063f0038059530840807e428e102b7c387ca2c72513612f115c9bd6b71f6`
- `src/acabados_vivienda.js`: `c439f596d8256cfae5e3a9fec0318ff4e28b456ca980ed84a51a161d9955ce6c`
- `data/kits/kit.schema.json`: `299e3c1cd00a7fcf5f3fd5c5e3b46f69137b287ca3b4a8a5519e7e5181640b1a`
- `tools/interiores/composicion_domestica.py`: `c7c168e029f9a278e4fea9b3792892de48c3b0385ac7b1f20ba8c75f35567f19`
- `tools/interiores/acabados_catalogo.py`: `e0963e92df7f659301ff4940176fee686e534952480d8eede6155c03069f302f`
- `tools/interiores/kits_vivienda_a.py`: `d398fee568d1b5f96cbbb1ef389dd8efcffb5da517521d82c6822914e76c25c5`
- `tools/interiores/casas_pruebas.js`: `29d54dfec522ac758ac1e6b6e8d5d6a1e49357b3ec5889929c22aa058ad6596e`
- `tools/interiores/fotos_casa.py`: `0a3119ae3181f1f43b61e31a5a8e0b18371496bad3db2a55f13814651eca6cb4`
- `data/kits/vivienda_cocina.json`: `241fbf6f65c265f76341a8e962cdffa1000fc697d9e0f7584710e3914491c973`
- `data/kits/vivienda_bano.json`: `e9ace969be39b2863bef2e8f45cb2de2a31c473fb6848cfb952cfd4167c3518c`
- `data/kits/vivienda_trastero.json`: `85a41b44b435386d992b582e8bfe9ae1b04de8420376be17544217e85a12aea9`
- `data/objetos/vivienda_a.json`: `d405cde128711ae427232e2e1c5e0a6d3f4d2129fb433ca7de3ba20c7d5fc7e2`
- `src/interiores_datos.js`: `4c54644e05ea023794992a618a8d1fe440b9f8d45fcf539c0a79a0129aec1ca9`


## data/interiores/revision_cocina_bano_tanda7_2026-10-17.md

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


## data/interiores/revision_trastero_tanda7_2026-10-17.md

# Revisión visual independiente — trastero, tanda 7

17 de octubre de 2026. Revisor independiente del autor del cambio. Inspección de las seis vistas de la ficha actual y comparación con la ficha anterior conservada. Sin ejecutar el juego, navegador, GPU, pruebas ni API de evaluación. No se asignan notas manuales ni se aprueba el objetivo formal 4/5.

## Conclusión

La agrupación mejora el orden del almacenaje y despeja la circulación. Se corrige la oclusión importante de la primera vista de 1594: ahora permite reconocer completa la bicicleta. No observo un bloqueo de evidencia que obligue a repetir estas capturas antes de cerrar la tanda. Persisten contraste suave, paredes altas muy vacías y una receta de pertenencias similar entre las tres muestras; son mejoras posteriores, no razones para añadir objetos por una métrica.

## Archivos examinados e integridad

Rutas relativas a `/Users/nestorguerra/Proyectos Vibe/Guarena HQ`.

| Evidencia | Ruta | SHA-256 |
|---|---|---|
| Ficha actual, modificada a las 19:56:59 | data/interiores/fichas/casa_trastero.jpg | f2d8a7dac8dacf1de9918a70b440f0873c016d8da722471b1848b3a399a4ce9b |
| Cámaras y muestras actuales | data/interiores/fichas/casa_trastero.json | f2ea8c41ed5565cadfe4f65000552e288f3858c2ddb1650bf2dc7b6464c65ddd |
| Ficha anterior conservada | data/interiores/validacion/imagenes/25b019a4b01bc4af938b905ada53add91e819912762daac641b7be82dbde9b75.jpg | 25b019a4b01bc4af938b905ada53add91e819912762daac641b7be82dbde9b75 |
| Cámaras anteriores | data/interiores/validacion/historico/calidad_tanda7_base/casa_trastero.json | 6d9a97640c6595c5be9f60653a29c486bc36f63f700a2fb5e462116cd2b8873a |

Los hashes se calcularon de nuevo al guardar este informe y coinciden con la evidencia inspeccionada. Las semillas son 1594, 3886 y 4589; perfil estudiante, estilo joven, plano dosPlantas, planta 1. La ficha actual declara calidad alta y DPR 1. Las dimensiones de sala coinciden con la base: 4,5 × 3,7; 5 × 3,5; y 5,3 × 3,6 m. Las cámaras mantienen FOV 68°, pero cambian cinco de las seis vistas. Solo la vista de conjunto de 3886 conserva sus coordenadas y objetivo anteriores. La comparación no aísla causalmente agrupación, materiales o luz.

## Cobertura de objetos y cámaras

| Semilla | Observación actual | ¿Recaptura imprescindible? |
|---|---|---|
| 1594 | La vista de uso muestra bicicleta completa y ventilador sin la estantería que antes tapaba la pertenencia. La general muestra las estanterías y cajas. Hay cajas cercanas cortadas en el borde derecho. | No. La pertenencia principal está cubierta y el recorte secundario es visible y declarado. |
| 3886 | La primera vista muestra bicicleta completa y su relación con puerta y almacenaje. La general corta la rueda delantera por el borde inferior/derecho. | No. La primera cubre completa la bicicleta; la segunda aporta contexto. |
| 4589 | Bicicleta y ventilador completos en las dos vistas. La general incorpora una estantería muy próxima al borde izquierdo y algunos enseres periféricos recortados. | No. El conjunto conserva suficiente contexto y no oculta la pertenencia principal. |

Los recortes no demuestran una colisión o un defecto geométrico. No se afirma que cada pieza periférica quede completa en ambas vistas. Las tres muestras muestran bicicleta: **la variante de escalera no tiene cobertura visual**.

## Qué mejora y qué sigue pendiente

- El almacenaje aparece más ordenado y hay menos pilas sueltas dominando el centro. La habitación deja un paso reconocible y la bicicleta gana protagonismo.
- La agrupación mejora la composición, pero no resuelve por completo el vacío. Los grandes paños superiores blancos siguen ocupando bastante imagen, especialmente en las vistas de uso.
- El ventilador tiene poco contraste contra el zócalo claro. Montantes, cajas y paredes conservan una separación tonal suave; no se observa una recuperación fuerte de contraste en toda la habitación.
- Las tres muestras comparten bicicleta, perfil y estética. Hay variación de distribución y acompañantes, pero no está demostrada una variedad amplia de pertenencias o estilos.
- No se observa una pieza principal claramente flotando ni una mancha nueva dominante de AO que impida interpretar la sala. Las imágenes estáticas no certifican estabilidad de sombras o parpadeo.

## Ajustes mínimos posteriores

1. Dar algo más de diferencia tonal al ventilador y a los montantes frente al zócalo, mediante los materiales existentes.
2. Valorar la iluminación preparada para reducir la uniformidad de paredes y techo conservando lectura de baldas y apoyos. Su resultado necesita capturas propias; este informe no lo aprueba de antemano.
3. Acercar visualmente bicicleta y almacenaje mediante distribución cuando la planta lo permita, conservando el paso. El objetivo sería relacionar los grupos existentes, no llenar el suelo ni añadir objetos para perseguir una nota.

Si se vuelve a capturar por otros cambios, conviene incluir la rueda completa en la general de 3886. Ese ajuste no es imprescindible para la cobertura actual porque la primera vista ya la documenta.

## Alcance

Revisión cualitativa de composición, contraste, vacío y cobertura de las tres muestras indicadas. No verifica transitabilidad, colisiones, todas las semillas, segunda estética, noche, rendimiento ni publicación. No sustituye las evaluaciones formales de Decision API. No se han modificado el juego, sus herramientas o las fichas.
