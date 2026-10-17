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
