# T18 · Revisión independiente acotada de correcciones R5

**Sin bloqueo nuevo detectado por lectura de estas tres correcciones. Respetan el alcance de código descrito, con un cambio de secuencia aleatoria que alcanza también decoración de hall y patio.** No se aprueba imagen, integración, CI ni publicación. No he ejecutado navegador, build, GPU, API ni pruebas; sólo he leído código/recibos y cotejado datos locales.

## Mezcla de paredes · houses.js:611–653

`mezclarParedes` copia la lista y ejecuta Fisher–Yates con índices válidos: n paredes consumen n−1 extracciones, ninguna para 0/1. No muta la entrada ni depende del número de comparaciones de sort. Los únicos reemplazos de sort respecto al HEAD leído son onWall y plant; las restantes líneas de ordenación permanecen iguales. El recuento actual en houses.js es 22 comparadores aleatorios restantes, más cinco ordenaciones ordinarias: no se ha hecho una limpieza global.

Causalidad observada: en `diagnostico_traza.json`, los valores del generador coinciden por índice, pero el primer sitio directo de consumo divergente está en444. En ese punto una ejecución sigue llamando al comparador de onWall y la otra ya pide una posición. Hay907 frente883 extracciones antes de patio. La diferencia de acciones registrada en3244 es la presencia/ausencia de `well` (Asomarse al pozo), no una recompensa de botín distinta. Esto respalda corregir el comparador aleatorio; no demuestra una razón interna concreta de V8, JIT o caché ni que el postpaso de lectura consuma azar.

Riesgo real de alcance: los dos helpers también participan en hall/patio y comparten el generador de la casa. El consumo fijo nuevo cambia la secuencia frente a T17/R4 y puede alterar decoración o elementos posteriores del patio. Los contratos A/B de lectura con el helper corregido no acreditan identidad de toda la casa respecto a T17. Conviene conservar ese límite en procedencia y no atribuir todas las diferencias de futuras fotos únicamente a la composición del salón. No propongo ampliar esta tanda a los otros comparadores.

## Alfombra · houses.js:1083–1093

La elevación se limita a `vivienda_salon`, objeto exacto `alfombra_salon`, sin soporte, reglas entre/suelo_libre y cota inicial prácticamente cero. Se fija y=.008 y se desplazan y0/y1 de su volumen antes de registrar estancias y antes de construir la geometría. El catálogo compartido no cambia; tampoco alfombras de otros kits, soportadas o ya elevadas. La operación es idempotente porque deja de cumplir la guarda y≈0.

El catálogo tiene caras superiores a.003 y.004; la nueva cota da.011 y.012 frente al acabado de suelo.0095: separación nominal de1,5 y2,5mm. El volumen registrado y la colocación construida siguen la misma traslación. La base de la alfombra queda a.008, parcialmente embebida en el acabado: no se debe describir como 8mm flotando sobre la cara final del suelo. El validador general permite hasta1cm respecto al origen y no comprueba por sí solo visibilidad frente a estas láminas. La cuenta geométrica es coherente; falta el contrato raycast real preparado por otro agente y la nueva evidencia visual. No los doy por aprobados.

## Contrato T20 · tools/interiores/casas_pruebas.js:1186–1195

La excepción admite sólo la clave exacta `acabado_domestico_salon_vertices`, exige vertexColors=true, blanco0xffffff, roughness=.92 y conjunto exacto de defines/valores deliberados. Las claves restantes fuera de estudio conservan la prohibición de CLAY_LINT. No es un startsWith amplio ni se ha retirado el control global; corrige un supuesto del contrato antiguo que excluía cualquier acabado posterior autorizado. El finally que restaura los interceptores se conserva.

Límite: las tres muestras de este contrato son artista/estudiante/músico; la rama familia del valor esperado no queda ejercitada ahí. La comprobación geométrica propia del salón y su prueba por perfiles son evidencia separada. Tampoco este chequeo de propiedades de material sustituye una compilación de shader o una captura real.

## Recibos y pendientes

`contratos.json` contiene77 pruebas PASS y errores[]. `kits5.log` contiene40 líneas de kits, cada una con cinco semillas y sin errores distintos de0. Son recibos del trabajo de raíz, no ejecuciones de este revisor. `R4_fallido_contratos.json` conserva los dos FAIL originales (prohibición LINT y acción well) y `R4_fallido_validacion_ejecuciones.json` conserva exit1. No se ha borrado ni reinterpretado ese fallo como PASS.

Esta revisión no utiliza como aprobado el barrido200 R5 que estaba en marcha ni las capturas/snapshot R5 pendientes. El siguiente cierre debe distinguir la mejora técnica de la revisión visual real del salón. No se propone retocar cámaras, semillas ni umbrales para obtener un resultado favorable.

## Hashes de lo leído

- `src/houses.js`: `60577120cc7bd6cae609d890734ffbca69b8debde685516bb7e1b057efbeea86`.
- `tools/interiores/casas_pruebas.js`: `fce0a540bcfdd3210631d8a5fd4985b481039382fd83c2517dac7e5eed8ca66e`.
- `src/acabados_vivienda.js`: `ae45aaf166bcd643ff1bf3429a479b0e302028701376aa16f69d137a7fdd5f8c`.
- `.cache/calidad/tanda18/causa_ordenacion.json`: `888c99434e73fffcec4b0be0c3859766bcfb10601a3fa6c863542edb0c7b9168`.
- `.cache/calidad/tanda18/diagnostico_traza.json`: `181eb16399a7e61ee193bc65ca9efdfb45d8ec144ada2e8bb072ab4dea5e78b9`.
- `.cache/calidad/tanda18/contratos.json`: `fe1440a0d4ccc31f465782bfd10c7fe6a17afc07580c57651b135a07189ed23d`.
- `.cache/calidad/tanda18/R4_fallido_contratos.json`: `4e721ca338fd0ba2d4b46ff00580591755a5d124c530b71d53d0cc65692aa339`.
