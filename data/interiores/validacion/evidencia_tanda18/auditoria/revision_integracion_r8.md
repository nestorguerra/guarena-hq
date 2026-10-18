# Revisión independiente de integración R8 — T18

Dictamen: **sin bloqueos nuevos identificados en la integración examinada**. El producto activo coincide con el R8 sellado salvo los deltas instrumentales declarados. Puede continuar el cierre técnico condicionado a los gates completos; este informe no aprueba publicación ni sustituye la revisión artística. Sólo lectura de fuentes/recibos y comprobaciones deterministas de hashes/diffs. Sin GPU, navegador, API, build, regeneración propia ni modificación de fuentes activas.

## Identidad de la candidata

Verificados los 494 hashes de `final_r8/preparado.json` y los 417 de `estado_candidato.json`: cero discrepancias. Los manifiestos de `metadata_estar` y `contratos_r8` coinciden íntegramente con sus archivos. Las fuentes artísticas, generador de catálogo, objetos JSON y compilado activos coinciden con R8.

Las diferencias compartidas activo/snapshot son exactamente cuatro archivos: `src/locales.js` y `tools/interiores/validar.js` por las dos líneas de metadata; `tools/interiores/casas_pruebas.js` por el parche de contratos; `tools/interiores/fotos_casa.py` por el puerto 8935→8920. Este último es una diferencia instrumental real, no una modificación de poses/guardas. El runner activo coincide byte a byte con `contratos_r8/candidata.js`.

## Producto y alcance

El nuevo `src/composicion_estar_salon.js` se ejecuta después de lectura. Conserva el opt-in de receta/perfil/área y las funciones domésticas; no añade entradas ni usa RNG. Busca mesa y alfombra existentes de la zona del sofá, arrastra sus dependientes con transformación rígida y mantiene el núcleo. Rechaza dependencias cruzadas/ciclos/referencias inválidas; comprueba límites, partes físicas, reservas, apoyos y celda inicial alcanzable antes de aceptar. El callback de `locales.js:741–745` restaura P y guardias mediante finally, también en excepción. El resultado se instala sólo al admitirlo; el fallback conserva el estado previo al pase de estar, que puede incluir lectura. No significa retorno a T17 o a antes de lectura.

Las dos correcciones de selección ya revisadas están presentes: índice exacto del puff procedente de lectura y alcance estricto <1.25, coherente con Seats.near. La mesa/alfombra no arrastran sofá o asientos protegidos. Esta condición conserva selección radial alcanzable; no certifica por sí sola la animación de sentarse ni standUp. No se han reabierto ni ejecutado esas pruebas.

El constructor propaga composicionEstar y limita la paleta nueva a sofá/puff de vivienda_salon. El cambio de **modelos de catálogo es compartido**, no exclusivo del salón: comparación JSON contra HEAD identifica únicamente sofá de dos plazas, sofá de tres plazas, puff y alfombra_salon; cambian partes y nombre/nota, sin nuevos IDs y sin cambios de clase, modificadores, roles, asientos ni superficies. Las patas, cojines y redondeos de esos modelos alcanzan cualquier instancia que los use. Por ello la cobertura de otras salas/Annie/comercios y presupuesto completo sigue siendo pertinente; la igualdad de propiedades no demuestra igualdad de toda geometría o coste.

El generador `catalogo_vivienda.py` contiene esos cambios y coincide con el snapshot, al igual que el JSON y compilado. El script preparado de regeneración R8 incluye ahora dicho generador además de los demás y exige hashes previos/congelados exactos después. No lo ejecuté. El recibo de regeneración que aún existía al revisar correspondía a R6 (sin catalogo_vivienda.py); no se usa como evidencia de regeneración R8.

## Metadata y contratos

Las dos líneas de metadata únicamente copian composicionEstar si existe, primero a h.local y después al reporte. No alteran filtro, geometría, cierra, RNG, presupuesto ni aceptación del validador. El CPU dirigido del autor compara el laboratorio 34 sin admisión de estar y el marco real de 3244/localSeed424969 con admisión. Registra poses, geometría/atributos, materiales, luces y acciones iguales salvo metadata. Es evidencia dirigida CPU, no raster ni un barrido de 81 admisiones.

La adaptación del contrato anterior utiliza unión explícita de movidos de lectura/estar; conserva identidades, soporte/dependencias, acciones/recompensas, otras salas, phone/drawer, asiento nuevo y preexistentes, usos y presupuesto. Exige poses literales fuera de esa unión y fallback completo cuando no existe ninguno. No oculta un fallo bajando requisitos. El caso aislado exige movimiento efectivo, compara helper e integración, conserva núcleo/dependientes, activas/guardias y 12 extracciones U; incluye reserva total, inicio exterior, rechazo y excepción sin mutar P. Los negativos guardados detectan ausencia de movimiento y rechazo ignorado. El primer error del harness sigue preservado.

Las expectativas de alfombra cambian sólo al color diseñado R8: centro #c8bda5 y borde #687565. Se mantienen altura, triángulos raycast, forma y color sobre suelo después de agrupar, control sin alfombra y negativos de hundimiento/pérdida de color. Los callbacks privados son literales; no se han quitado aserciones de coste para aprobarlos. La prueba CPU no equivale a renderer ni a coste de navegador.

El presupuesto `data/quality_budgets.json` coincide con HEAD: **60 mallas, 9 luces, 350000 triángulos y 1500 ms**. T21 mantiene el límite explícito de 60 del caller y el presupuesto general. Workflow sigue ejecutando tanda 21. No he encontrado relajación de tests/umbrales en el delta.

## Evidencia disponible y límites de cierre

- Recibo activo `contratos.json`: 79 casos PASS, errores []. `validacion_ejecuciones.json`, al leerlo, contenía sólo contratos y kits5, ambos exit0. No se da por terminado el pipeline de nueve pasos.
- CPU de modelos: 22 muestras, cinco admisiones de estar (3244,1594,4007,5045,4685). El contrato mantiene lectura en 3244/1594. Esto no equivale a «cinco en todo el barrido200» ni a una cuota obligatoria de admisión. Los conteos de mallas CPU con placeholders —incluido 61 de 2786 en ese recibo— no certifican coste final; lo decide el gate real pendiente.
- Revisión artística ajena `revision_visual_final_r8.md`: aceptación parcial, no nueva valoración propia. Formal A/B leído: 3.248/3.366, ambas sobre c1db0f3df8ed77d1d4b175d00f3a7fd73231822401811311c68db10c2d5c799b y sin superar umbral. No 4/5, no nuevas consultas ni repetición de juicio.
- La ficha activa todavía tiene SHA67b799b21ce503b2af4e290700a34c2fc0f64aad62df973ce93b995b0121eb3c; no es la ficha R8. Es un pendiente conocido del cierre, no una discordancia oculta. Instalar ficha/JSON y recibos R8 coherentes antes de afirmar expediente completo.

Pendientes concretos: terminar gates de casas/81 semillas/integración fuente y paquete/build/recursos/marcas, regeneración R8 idéntica, comprobar estabilidad del congelado al final y preparar expediente con ficha R8 correcta. CI/commit/push/Pages/verificación pública T18 siguen sin acreditar aquí. No he ejecutado esas acciones ni aceptado visualmente funciones por fotografías.

## SHA-256 comprobados

- `estado_candidato.json`: `f56e7fef99302b69994357a92db02a09f2493575485cf50706899b0e6bf25181`.
- `final_r8/preparado.json`: `efe9f0cba1e9f48aa598210d73bc620b04f4feb88ea3a42f093b62764e51101f`.
- `integracion_r8.json`: `85b61b36466548ff0e3c503e8f6140ffc2030dff6c8f018e1ee4d3ffa16d60ba`.
- `metadata_estar/metadata.patch`: `717cfaabdee2d7edd9776b1fab496c53fb642bedf0b8836bcd0ad2211ec93aa7`.
- `metadata_estar/cpu.json`: `355da79094f59123b457aa355a65a5bf71290712cb35d1d51a6b49ec9e4e8128`.
- `contratos_r8/contratos.patch`: `6f480045538da84e763293213ae1e68e0af3981afa6ca60f128af4a47b83d252`.
- `contratos_r8/cpu.json`: `888ddc8aef3a35b214bafce919283e78456526708dd4cd854ff682f8c8979c06`.
- `contratos.json`: `ce8f0839e9dedb50ee7018114a0c710b0002166b6a0b97786cac36c71cb14401`.
- `revision_visual_final_r8.md`: `beaee1a6364061376f541899b6e5fc86c48178ab1bb46e79688743e39a04da6f`.
- `src/composicion_estar_salon.js`: `c79e36a7b09bbf63b96b8c8a8286d5dff3d6dbfad484eccf42a06ba5f1a25306`.
- `src/locales.js`: `9702bc80ff51c4f8a4926ef6c9ce04459b03abeea4d399c662c5acc99f557cfd`.
- `src/houses.js`: `3a1557b5050a227cbaaa00e4ce6d613dce23d8e66ca9e2a1732394c6ffd810f3`.
- `tools/interiores/catalogo_vivienda.py`: `1339d00ac2f48031202a22507d47ad3292bbffb2d04508cc64d91d22d5057d8c`.
- `tools/interiores/casas_pruebas.js`: `678f408bb34c87d05625e638a75fede7df8f7fe341e387f5a64338848e177a65`.
- `tools/interiores/validar.js`: `8e15029ba61a03dd1f3987814c2beb6bb98d34b87dfcef4549d40f436001cf3f`.
