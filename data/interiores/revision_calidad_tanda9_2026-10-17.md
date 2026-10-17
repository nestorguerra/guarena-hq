# Revisión independiente de tanda 9

Los informes siguientes conservan los hallazgos originales y su cierre. Los contratos que estaban pendientes durante la revisión estática se ejecutaron después: 40 pruebas, cero errores. La revisión visual final es acotada y no declara 4/5.

# Revisión independiente del candidato tanda 10

Estado: **requiere una corrección P2 antes de aceptar la nueva regla**. No aplicado, sin GPU, sin aprobación visual ni de publicación.

Artefacto revisado: `.cache/calidad/tanda10_cocina.patch`, SHA-256 `ae13df47c0057ca86fdbd5ef4be5de84d7f0cdbb4342d8850c9a60f86c73f695`.

## Hallazgo

**P2 — Un grupo puede aceptar y registrar una relación `junto_a` que no cumple.** Localización: `src/locales.js` candidato, línea 512 (admisión de referencias anteriores), líneas 526–541 (sólo orden original/inverso y asignación de `de`). La guarda admite A contra pared, B de A y C de A. La búsqueda coloca A–B–C o C–B–A: C queda separado de A por B, pero asigna `C.de = índice(A)` y evita la regla individual, incluso con `si_no:false`.

Reproducción offline con el `amueblar` real, geometría pura real, tres cajas de suelo 1 × 1 × 0,5 m, zona de 5 × 4 m, pared N, seed 37, entradas obligatorias unitarias y `funciones:true`: antes A.x=−1,97, B.x=−0,93, C omitido porque no cabe junto a A; candidato añade C.x=0,11 y `de:0`. Separación entre bordes de A y C: **1,08 m**, frente a los 0,04 m de la regla. No hay WebGL ni simulación del algoritmo de colocación en esta reproducción; sólo se inyectan los tres modelos sintéticos y sus cotas exactas.

El kit de cocina propuesto admite nevera de [cocina, encimera] y por ello **no activa este defecto en sus tres entradas actuales**. Sí lo permite el contrato general de 2–4 módulos que se incorpora al motor. Corrección mínima: exigir que cada miembro tenga como referencia admisible al miembro inmediatamente anterior de la cadena; o validar la adyacencia real con alguna referencia admitida en cada orden antes de comprometerlo. Si no se satisface, conservar el fallback individual. Añadir contrato negativo A/B/C de A y verificar que no se declara éxito con la referencia lejana.

## Comprobaciones y límites

- `git apply --check` pasa contra el árbol actual, sin aplicar el parche.
- Atomicidad ordinaria: no se llama a `poner`, ni se cambian P/cursores hasta aceptar todas las piezas y `cierra(nuevos)`. El índice de entrada se conserva por pieza. Las guardias se incrementan por intentos fallidos, como instrumentación esperable.
- La búsqueda usa PRNG propio. Comparación offline antes/candidato en zona imposible 2,1 × 2,1 m, semillas 1–12: **0 diferencias** en P y en el siguiente `U([0,1])`.
- Se mantienen `dentro`, obstáculos/colisiones entre miembros, acceso y reserva de espacio frontal. Agrupación opt-in, consecutiva en entradas activas y acotada a 2–4 módulos; los otros kits conservan sus reglas. El filtro pasa a evaluarse de antemano: no se ha encontrado una regresión concreta en el filtro actual de viviendas, pero debe mantenerse puro respecto a la colocación.
- El éxito del grupo cambia deliberadamente la secuencia compartida posterior respecto a la distribución antigua, porque omite las reglas individuales: no debe venderse como conservación de RNG en éxitos. La promesa de fallback fallido sí está sustentada por la prueba citada.
- Los contratos añadidos cubren el hueco aislado, fallback/RNG y las tres cocinas objetivo; falta el caso de referencia no adyacente. No he ejecutado los contratos GPU ni evaluado coste total de búsqueda en casas reales.

**Declined to judge:** estética o 4/5; eficacia visual de las tres cocinas; publicación/despliegue; rendimiento GPU; efectos de los candidatos separados 8/9; aprobación de la tanda 7. La viabilidad sintáctica y de aplicación no acredita calidad visual ni cobertura de todas las semillas.


## Subsanación del autor del candidato — P2 de referencia no adyacente

Esta sección conserva íntegra la revisión independiente anterior y documenta una nueva versión. No sustituye el visto bueno del revisor ni aprueba lo visual.

**Candidato actualizado, no aplicado.** SHA-256: `61761fb95972b01018f3363c7d4385afc499fe58e494dc47cd246e1c99984f9c`.

La admisión de grupos ahora exige que cada `junto_a` incluya como referencia el `obj` de la entrada inmediatamente anterior. Se mantiene el alcance de 2–4 módulos obligatorios, unitarios y consecutivos. El caso A contra pared, B de A, C de A devuelve `false` antes de buscar posiciones o consumir RNG. Las reglas individuales reciben las mismas entradas, incluido `si_no:false`. C de [A,B], como la nevera de la cocina, sigue admitido.

Al comprometer una cadena válida, el `de` de cada puesto apunta exactamente al puesto anterior. Ya no se busca cualquier referencia anterior admisible. En el orden normal y en el invertido los puestos consecutivos permanecen adyacentes, con separación de 0,04 m. No se reordena el grafo ni se amplía la regla para ramificaciones.

Cambios preparados: `src/locales.js`, descripción del esquema y nuevo contrato en `tools/interiores/casas_pruebas.js`; el parche mantiene también generador y derivados de cocina ya propuestos. Ninguna fuente activa se ha editado.

### Regresión offline ejecutada

Instrumento: `.cache/calidad/tanda10_regresion_offline.mjs`.
Resultado: `.cache/calidad/tanda10_regresion_offline.json`.

Se ejecutan el `amueblar` candidato y las funciones reales de `interiores_geo.js`/`util.js`, reconstruidos en memoria. Sólo se inyectan tres cuboides sintéticos y sus cotas exactas; no se carga WebGL, no se construyen casas ni se simula el algoritmo de colocación.

- Rama A/B de A/C de A, `si_no:false`, semillas 1, 37, 81: P idéntico al candidato sin grupo y al código activo sin grupo; activas y siguiente U idénticos. Se colocan A y B; C conserva la omisión del fallback.
- Cadena C de [A,B], paredes N/S/E/W: tres piezas, cada `de` apunta a su predecesor admisible y a 0,04 m entre bordes.
- Grupo imposible en 2,1 × 2,1 m, semillas 1–12: P y siguiente U idénticos con y sin grupo.
- Control de mutación: se restaura sólo la guarda permisiva anterior en memoria. Vuelve a aceptar A/B/C donde la corrección mantiene A/B. La regresión detecta ese fallo. Este control no se presenta como ejecución del antiguo artefacto completo.

### Contrato de navegador incorporado, pendiente de ejecución

Nuevo caso `grupo ramificado respeta referencia inmediata y si_no sin alterar fallback`: objetos reales cocina/encimera/nevera, semillas 1/37/81, compara P, activas y siguiente U con el mismo kit sin grupo. Después cambia la nevera a `de:[cocina,encimera]` y exige tres piezas, índices originales y adyacencia de referencias. Permanecen los contratos previos del hueco aislado, fallback compacto y las tres viviendas objetivo. No se afirma que estos contratos de navegador hayan pasado.

### Verificación y límites

- Sintaxis de los archivos JavaScript candidatos: PASS mediante Node `--check`; Python del generador: parseo PASS.
- `git apply --check`: PASS, sin aplicar.
- Hashes de las seis fuentes activas frente al manifiesto base: 6/6 coincidentes después de preparar y ejecutar la regresión. Los cambios permanecen sólo en artefactos `.cache`.
- La garantía de conservación de RNG cubre rechazo/fallo, no el éxito deliberado del grupo.
- Sigue pendiente revisión independiente de la corrección, contratos en navegador, cocinas reales, cobertura de semillas, presupuesto y validación visual. No es aprobación de publicación ni 4/5.

## Cierre independiente de la corrección

**P2 cerrado en la revisión estática y la reproducción offline.** Artefacto releído: SHA-256 `61761fb95972b01018f3363c7d4385afc499fe58e494dc47cd246e1c99984f9c`. El estado inicial de este documento conserva la evidencia del defecto anterior; ya no describe el candidato corregido.

La admisión exige que `de` incluya al miembro inmediatamente anterior de la cadena. Al colocar, `puesto.de` señala precisamente a ese miembro, también cuando el orden espacial se invierte. La rama A/B de A/C de A se rechaza antes de consumir el PRNG propio o modificar colocaciones, y continúa por las reglas existentes.

He leído y ejecutado personalmente `.cache/calidad/tanda10_regresion_offline.mjs` (Node, sin navegador): PASS en rama con semillas 1/37/81, P/activas/RNG iguales al fallback y P igual al motor previo; cadena válida en N/S/E/W con distancia y referencia reales; grupo imposible en 12 semillas con P/RNG conservados. El control por mutación devuelve tres piezas con la guarda antigua y dos con la corregida: la regresión discrimina el defecto original. `git apply --check`: PASS sin aplicar.

No queda un bloqueo concreto de código identificado en el alcance revisado. **Aceptación estática del candidato corregido**, condicionada a integración y ensayos reales ya previstos; no acredita imágenes, 4/5, tiempo de búsqueda en todas las casas ni publicación. Siguen vigentes los límites y «Declined to judge» anteriores. Los derivados compartidos de tandas 9/10 deben regenerarse después de integrar ambas, no superponerse descartando una de ellas.


---

# Revisión independiente — tanda 9, trastero

**Resultado actualizado: los tres hallazgos Minor quedan cerrados en revisión estática del candidato final `df033940ff64eb081437521a5c6322d7a4508f64ad5f0338fbcbbd75e7b91a0f`. No se identifica bloqueo de código en este alcance. Contratos de navegador y aceptación visual pendientes; no es aprobación de publicación.**

La revisión inicial y sus hallazgos se conservan como historial. El cierre individual figura al final.

Parche revisado: `.cache/calidad/tanda9_trastero.patch`, SHA-256 `31dee499b0a2f912ca619ad4dd75d95aedacf6502de89a21d4611b3077b6ce24`. Propuesta: `.cache/calidad/tanda9_trastero_propuesta.md`. Las líneas de hallazgos corresponden al archivo candidato reconstruido en memoria, no al archivo aún sin aplicar.

## Hallazgos

### Minor — El portaequipajes no conecta sus tirantes con el eje

`tools/interiores/pertenencias_domesticas.py:37–38`.

Los cuatro tirantes terminan en `(-.45,.325,±.10)`. El eje trasero existente es el cilindro centrado en `(-.45,.325,0)`, con longitud `.09` orientada en Z: llega a `z=±.045`. El radio de los tirantes es `.009`, de modo que queda una separación de al menos `.046 m` entre sus volúmenes y el eje. No hay otra unión de esta estructura nueva al cuadro: la bolsa está apoyada en la tabla, pero tabla y tirantes quedan suspendidos respecto de la bicicleta. La declaración «tirantes al eje» no se cumple geométricamente.

Corrección mínima: añadir una extensión transversal del eje/conexión hasta ambos tirantes o colocarlos en Z dentro del alcance del eje existente. Mantener la huella y comprobar la unión, además de la base de la bolsa.

### Minor — La bolsa invade el extremo posterior del sillín

`tools/interiores/pertenencias_domesticas.py:39`, frente al sillín existente de la línea 30.

La bolsa ocupa X `[-.62,-.32]`, Y `[.6925,.9525]`, Z `[-.12,.12]`. El sillín ocupa X `[-.34,-.10]`, Y `[.8375,.8925]`, Z `[-.07,.07]`. Existe una penetración lateral de `.02 m`, con alturas y profundidades coincidentes; el redondeo de las esquinas no elimina la zona central de contacto. El contrato comprueba la base de la bolsa, pero no esta intersección interna. El colocador tampoco la detecta: comprueba objetos entre sí, no las piezas dentro de un objeto.

Corrección mínima: retrasar ligeramente o estrechar la bolsa, ajustando sus correas y manteniendo toda su base dentro del tablero; comprobar un margen respecto del sillín. No requiere ampliar la huella de la bicicleta.

### Minor — El contrato de variedad puede pasar aunque la variante añadida nunca se coloque

`tools/interiores/casas_pruebas.js:338`.

`ids.size>=2` permite aprobar sólo con bicicleta original y escalera. Esas dos siluetas ya existían antes del cambio. Por tanto, una regresión que impida colocar `va_bicicleta_carga` en todas las muestras seguiría verde. La prueba de dimensiones consulta el catálogo, pero tampoco demuestra colocación.

Corrección mínima: exigir que el conjunto observado contenga explícitamente los tres IDs en el conjunto de semillas de prueba, o añadir un caso sintético que fuerce cada variante en una estancia amplia. Para los nuevos accesorios, añadir también referencia existente con una reserva de ventana/obstáculo y comprobar que se omiten sin recolocarse; el contrato actual sólo cubre ausencia y colocación positiva en pared N.

## Integración comprobada

- `git apply --check .cache/calidad/tanda9_trastero.patch`: PASS contra el árbol actual durante esta revisión. No aplica el parche.
- Reconstrucción de los candidatos enteramente en memoria, verificando cada contexto y línea eliminada. Los siete objetos producidos por la función candidata `pertenencias()` coinciden exactamente con sus entradas en el JSON candidato.
- La única modificación de `src/locales.js` es la guarda `sobre_de && !ref && si_no===false`. Las entradas sin esa condición conservan su comportamiento. Con referencia presente se mantiene la pared y el centro de la referencia; si no cabe, la regla existente termina y no busca otra pared.
- Los accesorios siguen sujetos a `dentro` y `libre`, incluyendo reservas de puertas y ventanas. Sus alturas mínimas superan 1,2 m; la regla omite `cierra` para esos volúmenes igual que antes, coherente con el límite de altura del mapa de paso. No reducen `paso_libre` ni añaden huella a nivel de tránsito.
- El cambio de paleta está limitado por `rm.type==='trastero'`. No introduce llamadas aleatorias nuevas: la selección usa semilla y estilo directamente. Las demás clases de habitación conservan su expresión de paleta.
- La nueva variante sustituye una pertenencia en la misma entrada. Los acompañantes junto a `guardados` admiten los tres IDs. No aparecen referencias de juego a los IDs antiguos que excluyan explícitamente la bicicleta de carga. La captura de ficha sí tiene una lista de foco con los dos IDs antiguos; cae a su foco alternativo para la variante nueva, como advierte la propuesta.
- La modificación de reserva de uso frontal del inodoro se conserva: el parche no altera `cierra`, `espacioFrontal` ni esa prueba. La guarda de tanda 9 y la agrupación de tanda 10 están en secciones distintas de `locales.js`; los derivados compilados deben regenerarse tras combinar ambas tandas, no resolverse descartando un lado.

## Impacto y condiciones de aceptación

La distribución por semillas cambia al ampliar dos variantes a tres; esto es comportamiento esperado, no una garantía de equivalencia con viviendas ya capturadas. La reproducibilidad debe verificarse sobre la versión final. No se cambian las semillas canónicas ni se deben seleccionar otras para ocultar los resultados.

Después de las correcciones: ejecutar los contratos nuevos, validación de kits/objetos, cobertura de 81 semillas, 200 casas e integración acordadas. Registrar presencia de los tres tipos y omisiones de accesorios. Recalcular presupuestos de casa completa: el coste por objeto de la propuesta no demuestra el coste agregado ni el número de mallas tras montaje.

## Declined to judge

No se han ejecutado juego, navegador, GPU, build ni los contratos de navegador. No se han aprobado color, contraste, luz, densidad percibida, puntuación 4/5 ni mejora visual. No se ha validado rendimiento o presupuesto agregado. No se han modificado fuentes, datos, cámaras, semillas ni el parche; sólo se escribe este informe. Los resultados offline declarados por el autor que no se enumeran como comprobados arriba siguen siendo evidencia del autor.


## Cierre independiente de las correcciones

Artefacto final revisado: `.cache/calidad/tanda9_trastero.patch`, SHA-256 `df033940ff64eb081437521a5c6322d7a4508f64ad5f0338fbcbbd75e7b91a0f`. El SHA `0873a88754c84a68f912dd6da1ff2840e4bf5e03600d270d1ce5041e31ce8477` comunicado inicialmente era intermedio; no es el artefacto de este cierre.

1. **Portaequipajes sin conexión al eje — CERRADO.** El nuevo cilindro transversal, centrado en `(-.45,.325,0)`, tiene longitud `.22` y llega a Z ±.11. Se solapa con el eje original y alcanza los cuatro tirantes a Z ±.10. Cálculo independiente de sus extremos inferiores: error en XY inferior a `8e-17 m` respecto del centro del eje; los cuatro están dentro de la longitud y radio del cilindro. El contrato añadido reconstruye esos extremos y exige la unión. La corrección no aumenta la huella dominada por ruedas/manillar.

2. **Bolsa dentro del sillín — CERRADO.** La bolsa pasa a X centro −.50: ocupa `[-.65,-.35]`. El sillín empieza en −.34, dejando `.010 m` libre. Las correas se desplazan con ella. Su anchura queda dentro del tablero `[-.66,-.28]`; su base Y `.6925` coincide con la cara superior del tablero. Se añade aserto de margen bolsa/sillín. Comprobado sobre los datos generados por la función candidata.

3. **Contrato permite omitir la variante nueva — CERRADO EN EL CÓDIGO DEL CONTRATO.** El aserto ahora exige cada uno de los tres IDs, incluida `va_bicicleta_carga`, en el conjunto de 24 semillas. Ya no puede aprobar con sólo dos variantes. Además, la prueba de referencia válida repite la colocación reservando el volumen del accesorio y exige conservar la bicicleta y omitir el accesorio; detecta tanto invasión como recolocación en otra pared. La ejecución de estos casos sigue pendiente: cerrar la carencia de asertos no demuestra que las 24 semillas pasen.

Comprobación adicional: reconstrucción en memoria del parche; los siete objetos producidos por `pertenencias()` coinciden exactamente tanto con `data/objetos/vivienda_a.json` candidato como con `OBJETOS` de `src/interiores_datos.js` candidato. `git apply --check`: PASS sobre el árbol actual, sin aplicar.

**Declined to judge:** cobertura de colocación ejecutada, integración de casas, presupuesto total, apariencia, contraste o puntuación visual. No se han ejecutado navegador/GPU/build, ni se han modificado fuentes, datos o el parche. Sólo este informe se actualiza. No quedan abiertos los tres hallazgos concretos, pero siguen las condiciones de ejecución y revisión visual ya indicadas.


---

# Revisión visual independiente — tanda 9, cocina y trastero

17 de octubre de 2026. El log `.cache/calidad/tanda9/fichas.log` confirma tres casas capturadas para cada kit. Se examinaron los dos JPG actuales, sus JSON y los dos snapshots de tanda 8 conservados. Revisión solo mediante archivos locales; sin ejecutar juego, GPU, pruebas o API. No se asignan notas ni se atribuye el objetivo formal de calidad.

**Aprobación acotada de las muestras visibles.** No observo un bloqueo nuevo de frente, apoyos, puerta o silueta que exija otra captura o corrección para esta tanda. Las mejoras de composición no resuelven por completo la proporción de vacío del trastero.

## Evidencia

Rutas relativas a `/Users/nestorguerra/Proyectos Vibe/Guarena HQ`.

| Archivo | SHA-256 |
|---|---|
| data/interiores/fichas/casa_cocina.jpg, 20:25:02 | 287501f5259e37f60ea756e67fac90721be53df740990341d6a544ce7fa1d53f |
| data/interiores/fichas/casa_cocina.json | 2d84be58594101a5a8dd95d0df7785743029787f789be521f9a3df4911f70351 |
| data/interiores/fichas/casa_trastero.jpg, 20:25:16 | 79cd1821f201fd3ad53c01dedb80062566d11ace095a79544cf2eca031fbdd14 |
| data/interiores/fichas/casa_trastero.json | f2ea8c41ed5565cadfe4f65000552e288f3858c2ddb1650bf2dc7b6464c65ddd |

Snapshots anteriores examinados, con hash de archivo verificado frente al recibo de `historico/calidad_tanda9_base`:

- `data/interiores/validacion/imagenes/1f34c47d762fb39dcbf33d7a03580a259dfb321cc154b0580a711bb9758f636a.jpg`, cocina de tanda 8.
- `data/interiores/validacion/imagenes/0855865979ae16feef71c8f0aeeaa785ad6f6cd7d25a0f6c658324fb1305c5c7.jpg`, trastero de tanda 8.

## Cocina

Las semillas 2786, 3244 y 1594 reúnen ahora cajonera, zona de preparación, cocción/fregadero y nevera en un frente más fácil de entender. En las grandes, la general explica la relación entre esos módulos que antes quedaban repartidos fuera del mismo encuadre. Las juntas entre módulos siguen visibles, pero no observo una separación importante que rompa el frente o una pieza principal claramente suspendida. Olla y alimentos parecen apoyados en sus superficies; los alimentos conservan escala y contexto domésticos.

Las dos vistas cubren las piezas principales. En 2786, la general tiene un costado de armario muy próximo y recorta parte del fogón, que la primera vista muestra. En las grandes, las sillas entran por el borde inferior; son un límite de encuadre, sin ocultar el frente completo entre ambas vistas. No aparece una puerta claramente bloqueada en estas capturas.

El contraste entre frentes verdes, estructura y encimera ayuda a separar volúmenes. Persisten pared alta uniforme, la sencillez de la grifería/fregadero y una receta de mobiliario bastante compartida. Son acabados posteriores. Las seis cámaras de cocina cambian respecto al histórico: la comparación no aísla el efecto de muebles y cámaras.

## Trastero

Las semillas 1594, 3886 y 4589 conservan exactamente las cámaras anteriores. El ventilador se separa mejor de la pared. Bomba y aro colgados sobre la bicicleta añaden una silueta funcional de guardado/mantenimiento. Las variantes naranja con bulto trasero y la bicicleta azul aportan diferencias visibles; no se afirma cobertura de escalera.

La bicicleta queda completa en al menos una vista de cada muestra. La general de 3886 sigue cortando la rueda delantera, compensada por la primera. Los estantes cercanos recortan cajas periféricas en algunas generales. No veo un objeto principal claramente flotando; esto no verifica colisiones o cada anclaje oculto.

**Carencia estructural pendiente:** el almacenaje alto sigue concentrado en una franja o esquina, mientras la pared de bicicleta conserva mucho paño superior y el centro ocupa bastante imagen sin relacionar los grupos. La nueva decoración mejora identidad, pero no cambia mucho esa proporción.

La intervención posterior más útil sería formar una esquina de almacenaje con dos alturas y relacionarla con la bicicleta: reordenar primero las estanterías y pilas existentes, conservar un paso claro y comprobar que se leen como un conjunto doméstico. Si hiciera falta un volumen bajo, tendría una función concreta de guardado. Añadir más objetos pequeños colgados o llenar el centro no resolvería por sí solo el reparto de masas.

## Alcance del cierre

Aprobación cualitativa limitada a estas seis muestras, dos vistas por muestra, estética Plastilina, calidad alta y DPR 1. No prueba noche, apagón, movimiento, transitabilidad, todas las semillas, otras estéticas o rendimiento. Los contratos y evaluaciones formales comunicados por el constructor no sustituyen esta inspección y no se han repetido. No hay un hallazgo visible que justifique ampliar pruebas en esta tanda; el vacío del trastero queda como mejora posterior explícita.
