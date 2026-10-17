# Revisión independiente de código — tanda 5

Resultado final: **sin hallazgos abiertos de comportamiento en el estado releído**. Tres defectos comunicados durante la revisión fueron corregidos por raíz y se verificaron después. La actualización final de abajo sustituye la revisión inicial de costura y el primer perfil GTAO. Esta conclusión es de código y sondeos sin WebGL; no aprueba estética ni publicación.

Revisión de `git diff` y generadores actuales: cocina, costura, unidades domésticas, revestimientos, integración GTAO, contratos añadidos. Se consultaron CLAUDE.md, docs/interiores.md, los cinco puntos literales de Review Focus y los Ruling del ledger. El paquete de revisión conserva una base histórica; se revisó el árbol actual, no aquel rango de commits.

## Hallazgos corregidos durante la revisión

1. **P2 — intervalo sin cocina funcional**, `tools/interiores/kits_vivienda_a.py:11`. La primera lectura tenía `area_max=13.999` para cocina/encimera compactas y `area_min=14` para amplias. `src/locales.js:482` trata el máximo como exclusivo. Para W=4 y D=3.499875 (13.9995 m²), ninguna de esas entradas se activa. Un reintento con otra semilla no corrige un filtro dependiente solo del área; el control de obligatorias recorre precisamente las entradas activas. Raíz corrigió el máximo a 14. Se releyeron fuente y JSON generado: en 13.9989, 13.999 y 13.9995 se activan cocina/encimera compactas; en 14 se activan las amplias. La partición ya no tiene ese hueco.
2. **P3 — patas duplicadas en la isla**, `tools/interiores/composicion_domestica.py:75`. El bucle recorría z=±0.22 pero no pasaba z al constructor: cuatro piezas ocupaban solo dos posiciones en z=0. El efecto era geométrico: faltaban los apoyos previstos y había piezas coincidentes. Raíz añadió `z=z`. El catálogo regenerado coincide exactamente con `objetos()`; se verificaron cuatro posiciones distintas: (±0.5,0.04,±0.22).

## Comprobaciones independientes

- Importar `catalogo_comercio` y ejecutar `catalogo_vivienda_a.objetos()` con escrituras bloqueadas: cero escrituras y cero salida estándar. El diccionario comercial construido coincide exactamente con `data/objetos/comercio.json`. El cambio de guardia conserva la ejecución directa y evita el efecto lateral del import.
- Las **57 recetas domésticas** coinciden exactamente con `unit(0,0)`, conservan su masa y soporte de superficie; dimensiones positivas y finitas. No heredan las filas nx×nz ni la envolvente del stock comercial.
- `va_encimera` contiene únicamente primitivas `caja` en el catálogo actual. La ampliación 1.46 conserva alto/fondo y escala correctamente ancho/posición x. No hay actualmente cilindros o esferas deformados por tratar un radio como ancho. La ampliación de cocina/bancos sí distingue tipos.
- Estado inicial, sustituido por la actualización final: la costura usaba `conjunto`, una silla obligatoria en lado +z y las tres variantes de mesa. `src/locales.js:360–395` exige esa silla antes de añadir mesa y silla, aplica giro conjunto, comprueba geometría/paso y conserva `de` hacia la mesa. Ha desaparecido la ruta `junto_a` que podía recolocar la silla contra otra pared. El control de cantidad de `src/houses.js:1061` cuenta la mesa, no la silla. Es comprobación de lógica y JSON; no repetí los juegos completos de las semillas 2606/4216/3981.
- Estado inicial, perfil sustituido por la actualización final: **14 sondeos Node aprobados** sobre el helper real `prepararOclusionVivienda` y el cuerpo real de `Game.renderView`, con dobles de renderizador: vecino y Annie reciben radio .55, grosor .35, escala 1.25 y mezcla .75; se restauran valores originales no predeterminados. Exterior, otros edificios, cámara lejana, AO desactivado y componentes ausentes no cambian esos valores. Render directo y compositor restauran en éxito y excepción; la excepción original se propaga. Sin asignación de nuevos recursos GPU en el helper AO.
- Los cambios de revestimiento reutilizan la segmentación por huecos, añaden cocina/costura y conservan las ramas existentes de baño/despacho/taller/trastero. No identifiqué una modificación de interacciones, botín, claves de partida o recursos de otros edificios introducida por estas líneas.

## Declined to judge

- Calidad estética, claridad de los nuevos modelos, manchas visibles y adecuación perceptiva de GTAO: requieren imágenes y evaluación visual; no se puntúan aquí.
- El coste real del render, contadores GPU, compilación de shaders y liberación física de GPU: los sondeos emplean dobles y no WebGL.
- Certificación de 28/29 contratos, 200 casas, todas las semillas o paquete final: no se ejecutaron esos ensayos en esta revisión. Los resultados previos o aportados por raíz no sustituyen los ensayos posteriores al último ajuste.
- Persistencia de partidas reales y universalidad de interacciones: no se cargó ni modificó ninguna partida.
- Restauración de cámaras del compositor ante excepción: la línea que intercambia cámaras es anterior a esta tanda; no la presento como nueva regresión de GTAO.
- Continuidad visual al cruzar la distancia límite de 25 m: el helper tiene un corte deliberado y esta revisión no recorre cámara/GPU.
- Publicación, puntuaciones formales y aprobación final del usuario.

## Huellas del estado releído

- src/luz_vivienda.js: 4143db5ce1f4b632ec249889a5c8e3821b45c8f5edfaf085cd5b9449abff040a
- src/game.js: 097d47405a752881627970d68c9e1fc91be580d2ad7c152500b3752b4ad71c2f
- tools/interiores/composicion_domestica.py: 53c92e9d0be4e53a1e8db405a54d84b4c862fff38f146cbba2100d90f8b93908
- tools/interiores/kits_vivienda_a.py: e9c767f9245c791902a810a80c878a6ec34099b3e34a359868196707dfca5378
- tools/interiores/catalogo_comercio.py: d6c0fe5c4804d8b9319ddf1d8254cb8bfe1db530780344d64752c9743f41c513
- tools/interiores/casas_pruebas.js: d26542bde82f1adc2e550d308865c2c3ec34550cf962ba16a4dc13d4397e16af

No se modificó implementación ni se abrió navegador, servidor o puerto. Única escritura del revisor: este informe.


## Actualización final — puesto contra pared y perfil GTAO definitivo

**Sin hallazgos abiertos.** Revisión del cambio posterior en `src/locales.js`, esquema, generación de datos, kit de costura, validador y contratos. El estado final ya no emplea `conjunto` para costura; usa `contra_pared` con `silla_frontal`. El perfil AO final es radio **0.85**, grosor **0.6**, escala **1.4** y mezcla **0.85**.

### Tercer hallazgo, corregido

**P2 — falsos errores de exceso para todos los puestos válidos**, `src/locales.js:238` y `tools/interiores/validar.js:29`. Mesa y silla se insertan con el mismo índice de entrada, pero el recuento original contaba ambas y solo exceptuaba la regla `conjunto`. La nueva entrada `contra_pared` tiene cantidad [1,1]. Se reprodujo ejecutando el bloque real de recuento con una pareja correcta: `exceso: estancia/undefined — 2 colocados, el kit admite 1`. Esto rechazaba la aceptación de las habitaciones correctamente montadas.

Raíz corrigió el recuento para contar padres con `de===null` cuando se pide `silla_frontal`. Añadió la exigencia de exactamente una silla del tipo correcto vinculada a cada puesto y correspondencia entre número de auxiliares y padres. Se releyó y probó el bloque corregido: la validación no se ha debilitado para obtener un resultado favorable.

### Evidencia independiente posterior

- **24 sondeos Node** ejecutan el método real `contra_pared`, extraído de la fuente, con dobles de geometría: las cuatro paredes, orígenes asimétricos de mesa/silla, orientación opuesta, vínculo `de`, rechazo por silla fuera de zona, ocupada o solapada, rechazo de paso y camino sin `silla_frontal`. No se inserta ninguna mitad del puesto al rechazar la pareja; el guardia recibe ambas piezas antes de insertar.
- **10 sondeos Node** ejecutan el bloque real del validador: pareja correcta, silla ausente, duplicada, huérfana, tipo incorrecto, entrada incorrecta, ausencia de padre, padre extra, índices desplazados por otra entrada y entrada sin esta opción. Solo pasan las configuraciones correctas. No son ensayos del render ni sustituyen la geometría real de las 81 semillas.
- **14 sondeos Node** de AO repetidos con el perfil definitivo: restauración exacta, ámbitos excluidos, AO desactivado, componentes ausentes y render directo/compositor tanto normal como con excepción. Todos pasan.
- El checker real del esquema admite la referencia de silla como cadena y rechaza un número. La rama añadida en `datos.py` incluye esa referencia en el mismo control de existencia de catálogo que los objetos normales.
- Inventario de kits actual: solo `vivienda_costura.json`, entrada 0, activa `silla_frontal`. El nuevo camino es optativo. No hay cambios a la colocación del resto de entradas salvo la reorganización equivalente de sus guardias.
- Se revisaron el contrato de proximidad/frontalidad/mesa contra pared y el nuevo contrato positivo/negativo del asiento. No se ejecutó el juego completo del contrato 30 desde este revisor.

### Límites finales / Declined to judge

Se mantienen los límites de la primera revisión: imágenes, puntuación estética, rendimiento, GPU real, publicación y partidas reales. No certifico los resultados finales de 30 contratos/81 semillas/200 casas que ejecuta raíz. La ubicación de cámara y legibilidad visual del puesto requieren la revisión de capturas. Los sondeos de colocación prueban control de flujo y transformaciones con dobles, no la geometría completa del catálogo.

### Huellas que sustituyen las anteriores para los archivos cambiados

- src/locales.js: b85b9f61abe3b09401d3b6c9bd6042c67a6ce879d58d4b7d913055416ec0eb43
- src/luz_vivienda.js: babeedf2c322f1056332e7917de58f039717b7edfeb0df17ea7adf2b19a54e6b
- tools/interiores/validar.js: 34c73fead01e2ec4745ed6acb750f73be1b222fe04c19d30853abbfcd9be0666
- data/kits/kit.schema.json: f92a80c8357698eb06bb83528975a8edfc02052ebcca8829d8b3105353501a76
- tools/interiores/datos.py: 6f5b0637fed4948715afb8b17e786dd2979800ca1c208d1da475b68dc77a37a6
- tools/interiores/casas_pruebas.js: b9195351968438fe92c2c490819d07c4d33406a5d8abacef7ee2a23dffb2da48
- tools/interiores/kits_vivienda_a.py: 3f99875c9c174dac94c42649ac4216f2c09e130aa3d44ed78d1f28a81f8cfab5
