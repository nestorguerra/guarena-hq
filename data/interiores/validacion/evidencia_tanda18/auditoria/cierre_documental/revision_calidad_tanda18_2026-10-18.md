# Tanda18: revisión independiente de salón

Mejora parcial revisada y validada, objetivo4/5 pendiente. A3.248/B3.366 sobre ficha c1db0f3df8ed77d1d4b175d00f3a7fd73231822401811311c68db10c2d5c799b, una llamada por lado. Los dictámenes de cada fase conservan su alcance y no anticipan los gates posteriores. El pase final integrado consta de79contratos,40kits×5,200casas/1166habitaciones,81salones,96rutas y nueve gatesPASS;417fuentes estables y22derivados idénticos mediante7generadores. Recibo vinculado al hash de fuentes: validacion/evidencia_tanda18/gates_finales/validacion_sello_final.json.

R6 no se publicó; R7 conserva tres FAIL de envolvente del puff y huecos de protección de asientos. R8 los corrige antes de validar. El delta posterior de metadatos/pruebas no cambia la escena de la ficha; invariancia CPU dirigida y diff conservados. La nueva pareja de lectura usa punto libre común distinto del complemento histórico; la cámara antigua fue vetada porque la mesa nueva la ocupaba. No se movieron muebles para la foto ni se rebajó la guarda.

Las notas de otros kits son sus últimas evaluaciones de imágenes, y no acreditan de nuevo esta versión tras cambios compartidos. Los4IDs de modelos cambian formas también donde se reutilizan fuera del salón; funcionalmente los cubren los gates globales. La paleta nueva se limita al sofá/puff del salón. No acredita4/5, FPS universales ni beta final. La publicación sigue pendiente de CI exacta y comprobación pública.

## Revisión del programa de lectura y sus guardas

# Revisión técnica privada R3 — postpaso de lectura

**Favorable para continuar el prototipo privado corregido; no es aprobación de integración final ni de calidad visual.** No se detecta otro P1/P2 geométrico o de atomicidad en el helper revisado. La ruta de laboratorio aún requiere transmitir perfil y declarar su contexto funcional antes de atribuirle cobertura R3.

Fuentes observadas: `postpaso_r3/composicion_lectura_salon.js` SHA `c28598fe5154a4405795977f973e00ae5778cc4a2618c7343eeea7e12f2016c3`; `locales.js` SHA `65448df1c41c24221f6915519d08be14cd336cafdd004e4767d8ec5ac9417e76`. El código permanece privado y se carga en memoria mediante el runtime de construcción. No se ha usado GPU, API, build ni modificado producto.

## Hallazgos y estado

**P2 cerrado — inicio físico ocupado aceptado por proximidad.** La versión R3c comprobaba una celda alcanzable a menos de .15 m del inicio. `mapaPaso` puede buscar otra semilla si el inicio está ocupado. Con la geometría real de 3244 y un inicio dirigido `(3.2903732327744373, .675)`, libre en la base, el helper admitía la esquina aunque la celda final tuviera `free=false` y `reach=false`. No se atribuye este inicio artificial a la entrada real de la vivienda. El helper corregido exige la celda literal dentro de bounds y `free && reach`, y rechaza ese mismo caso. RED conservado en `dirigida.json`; comparación literal RED→GREEN en `cierre_inicio.json`. El callback de aceptación es neutral en este test de la guarda, no se presenta como un build completo.

**Cobertura pendiente — laboratorio sin perfil.** `buildLocal` vigente transmite el filtro del hogar, pero no `hogar.perfil` a `ctx`. El helper exige `ctx.perfil`: pasar sólo `funciones:true` no lo activa. La adaptación privada de `houses` sí transmite el perfil. Raíz confirma que completará la transmisión del mismo hogar al laboratorio sin volver a ejecutar filtros. Hasta entonces un pase legacy de 81 semillas no acredita este postpaso. Exigir admisiones no vacías y metadata verificable en el recibo que lo pruebe.

## Comprobaciones independientes ejecutadas

`atomicidad_rng_giro.mjs/json` conserva tres controles acotados:

- `amueblar` real del salón 3244, semilla efectiva 424969 y contexto fijo: admisión no vacía, K conserva identidad, índices/obj/e/sop/sup/de idénticos, activas y guardias iguales, y **12 extracciones siguientes U exactamente iguales**. El filtro de este control usa las entradas activas del montaje base; no simula un nuevo consumo del pool doméstico.
- Callback `aceptar` literal extraído de la adaptación privada: `cierra` observa P temporal y lanza una excepción dirigida. El `finally` restaura P, sus referencias originales y guardias. El helper tampoco muta P si su callback lanza. No se ha convertido esa excepción en un PASS de montaje.
- Fixture dirigida de 9 × 9 m con los cuatro objetos reales y un libro dependiente: se rechazan las esquinas sin giro para forzar una admisión en pared E. Giro real de 90°, coordenadas locales del libro invariantes dentro de `1e-10`, `sop/sup` conservados y P original intacto. Es un control de transformación, no otra casa ni cobertura adicional de semillas.

Releído el recibo de raíz de 22 casas: dos admisiones, 3244 y 1594; veinte fallbacks, incluido 5045. No se mantiene la expectativa previa de tres admisiones. Las comprobaciones del autor conservan identidad, núcleo, otras estancias y tipos/labels/defs de acciones, con uso sin errores; no las presento como nuevas ejecuciones propias.

## Geometría e identidades

La clausura por índices y el cambio rígido de x/z/ry conservan alturas y relaciones de los soportes. Se recalculan volúmenes. Las colisiones contra otros propietarios y piezas inmóviles, límites/altura y reservas sí se comprueban. Excluir colisiones entre piezas del **mismo propietario** es admisible aquí porque todas reciben exactamente la misma transformación rígida: conserva contactos/penetraciones que ya existían, **no demuestra que la geometría inicial estuviera libre de ellos**. No extender la excepción a piezas de propietarios distintos.

La guarda de apoyo comprueba altura y centro del objeto en la superficie; no demuestra cobertura completa de una huella arbitraria. Para estos dependientes, el argumento principal es la conservación exacta de soporte y transformación relativa. No usarla como validador general de objetos reanclados a otro soporte.

K y entradas permanecen intactos; no se llama de nuevo a filtros ni r/U. El asiento añadido sólo se registra por el índice comprometido y `!o.rol`, evitando duplicar un sillón ya registrado por su rol. Este asiento de puff es una adición funcional autorizada, no mera conservación. Debe quedar comprobado en `pieces.seat` del constructor final. La instrumentación `__lecturaDebug` y detalle de intentos pertenece a este prototipo; no es parte necesaria del algoritmo de producto.

## Contratos mantenidos recomendados

1. **Admisión y conservación en constructor real.** 3244/1594 deben aplicar, conservar núcleo e inventario/acciones por identidad y añadir exactamente un asiento con pose válida. 4007/4685 deben conservar fallback íntegro y `phone/drawer`; un control no optante permanece idéntico. Verificar puntos de uso y la entrada con el collider real además del mapa .80. No exigir a 5045 aplicar si los límites físicos lo impiden.
2. **Transacción y transformación del helper.** Positivo de giro90° con dependiente, igualdad de siguiente U y salida al rechazar, negativo de inicio ocupado aquí reproducido, y excepción de aceptación con restauración de P/guardias. Incluir reserva o colisión real contra otro propietario para evitar un test que sólo valide el propio mapa de metadatos.

Los contratos deben usar el contexto real del gate y no atribuirle ejecución si el flag/perfil desactiva el pase. La selección de esquina y la visibilidad de galería quedan para revisión de imágenes; el resultado CPU no certifica composición visual ni coste final de render.

## Cierre de correcciones y alcance material

# Revisión independiente de correcciones R6 — T18

Dictamen: sin bloqueos de código identificados en el delta R5→R6. Apto para continuar los gates y la captura R6; no constituye aprobación visual, de publicación ni de los gates en curso. Revisión local por lectura y comparación determinista; no se ha ejecutado juego, GPU, build, API ni helpers de publicación. No se han modificado fuentes activas.

## Alcance comprobado

Comparados los dos archivos activos con `final_r5/`: el único cambio de producto es incluir `cazador` junto a `familia` en la excepción de material de `src/acabados_vivienda.js:27`. En pruebas cambian las expectativas correspondientes, se incorpora 4204 al caller T21 y se añade el contrato de alfombra. Los 416 archivos de `estado_candidato.json` coinciden con sus hashes al revisar. Los nueve archivos declarados por el manifiesto privado `alfombra_visible/manifest.json` también coinciden.

El acabado permanece limitado a salón y excluye Annie. Familia ya tenía este acabado; el nuevo efecto R6 afecta al salón cazador. Conserva blanco, colores por vértice, roughness .92 y los otros cuatro defines. No añade geometría, luces, consumo aleatorio ni cambios de disposición. T20 conserva la clave exacta de excepción, igualdad de claves/valores de defines y la prohibición de LINT para el resto de materiales no estudio; no se transforma en una autorización general.

## Evidencia y límites del material

El fallo R5 permanece en `r5_fallo_coste/casas_pueblo.json`: casa 4204, cazador/rústico, 42.976 triángulos, 61 mallas y 9 luces. El recibo dirigido `diagnostico_lote_cal.json` registra 61→60 mallas, 42.976 triángulos en ambas variantes y el mismo hash geométrico/color `bf2f4258bedd89253ba5f3860c290921bb4b86720dc52bc2dbcf487d0117c445`.

Leído también el instrumento: construye ambas casas con el constructor real, interviene únicamente el material de salón y restaura el prototipo en finally. La firma ordena triángulos mundiales y RGB, cuantizados a 1e-5. `sameInter` compara id/type/label/def/x/y/z. Esto respalda esa equivalencia acotada y la reducción dirigida de coste; no certifica todos los campos de interacción ni equivalencia completa de shader, píxeles o función. El valor LINT omitido toma el defecto 1.0 de plastilina: frente a R5 el cazador recupera la pelusa del acabado común. Su apariencia requiere captura real R6.

T21 añade 4204 al recorrido de material real y mantiene el assert explícito `mallas<=60` (casas_pruebas.js:1397), sin elevar ningún presupuesto. Conserva orientación/área del acento y RGB después de agrupar. La reducción de una muestra no sustituye el barrido de casas.

## Contrato de alfombra

El fragmento privado coincide literalmente con el añadido activo (SHA c2e4f92a9bc8c63cf8527af76d989d44b030803cddae7714c18adb1436a5450a). Usa casas reales 3244/1594 y control 2786 sin sofá/alfombra; raycasts sobre el grupo final con matrices mundiales actualizadas, incluidos los estados visible de sus ancestros. Exige suelo real a .0095, primer impacto superior y situado en la cara del textil, triángulos correspondientes a los rectángulos interior/borde y RGB resultante correcto. Comprueba coherencia p.v, clase/soporte/paso .80 y revisarUso; libera geometrías en finally.

Con p.y=.008, las caras superiores quedan a .012 y .011, por encima del acabado .0095. No depende sólo de la caja nominal. Los recibos CPU del autor registran PASS actual y dos negativos FAIL: retirar la subida entierra la alfombra; retirar color propio falla. He leído estos recibos, no los he reejecutado. El contrato no relaja la tolerancia del presupuesto ni modifica producción.

Límite: son dos puntos verticales por alfombra desde 4 cm, con distancias/colores fijados para estas muestras. No mide toda la superficie, oclusión desde una cámara, shader ni calidad visual. Es una prueba pertinente de la regresión suelo/textil, no una certificación de visibilidad artística completa.

## Helpers privados de publicación

`publicar_tras_ci.py` sólo cambia la carpeta T17→T18. Mantiene SHA explícito, HEAD/árbol congelado, árbol igual al merge de PR, CI de validar.yml con identidad/éxito y ambos jobs, árbol limpio, ascendencia y push sin force, más relectura de main. No se ha ejecutado ni consultado la red.

Se detectó una premisa incorrecta en la primera versión T18 del probe: contar `h.inter` de tipo asiento no comprueba el asiento doméstico. `houses.js:1117` registra el puff en `pieces.seat`, consumido directamente por `terrace.js:61`; el switch de interiors no prueba que houses cree esa interacción. El autor corrigió el helper antes de ejecutarlo. Releída la versión final: exige el índice de composición y objeto puff, exactamente un registro en origen+posición del puff con planta y orientación iguales. Es coherente con el asiento local x/z=0 del catálogo y el constructor actual. Registra expresamente que no ejecuta la acción de sentarse. Hallazgo cerrado por lectura, no por ejecución.

El probe conserva las ocho entradas, dos estudios, Annie, tres comercios, revisión exacta antes/después de recarga y fixture privada con comparación completa de partida. Añade ambos salones, altura de alfombra, registro del puff y veto a programas de shader no ejecutables. Este veto y consola no equivalen a revisión visual de píxeles. Los helpers siguen preparados y pendientes de SHA/CI/Pages reales T18.

## Criterio de integración y pendientes

Conservar R6 para terminar la validación, condicionada a los recibos de gates completos sobre este congelado y a capturas que permitan revisar el acabado cazador y la alfombra. Sin nueva objeción de código ni solicitud de ampliar alcance. No se ha evaluado visualmente R6 ni declarado CI, publicación, función de sentarse o resultado de los gates en curso. R5 fallido permanece como evidencia histórica.

## SHA-256 leídos

- `src/acabados_vivienda.js`: `3a5dedef261da21d0ba0cb91d27f62e6948569c959fcdd284cbeaf1065c5029f`.
- `tools/interiores/casas_pruebas.js`: `e1444ce0b33b99759493da3dac2e61204033c2837184d487b2582a10f14685c9`.
- `.cache/calidad/tanda18/estado_candidato.json`: `2a38907ab471fed425dfc206de30dd332c20094319e2e5ff8e7043a83ee16f05`.
- `.cache/calidad/tanda18/diagnostico_lote_cal.json`: `c66f62e49eebc2f2116948511cdc6eb528174cf0efe83a9e889a173a2ffca66d`.
- `.cache/calidad/tanda18/alfombra_visible/manifest.json`: `2e018d686036486e53fea8c2f6492fa51868262b7cbf27aaad5dd1ff76ba9f5a`.
- `.cache/calidad/tanda18/alfombra_visible/contrato.patch`: `92bfd5532f479e8f657baf5d3ded2984d4859cf684643d31744b2ed2dacec9f2`.
- `.cache/calidad/tanda18/publicar_tras_ci.py`: `4b0ebcc47196e45cdaad8e016cfa6c3dca403fe671c0204449413a3a3a161e58`.
- `.cache/calidad/tanda18/verificar_publico.py`: `ef83613cce96cc10482663e6c8df35cd491977605a1f631eb91f8b53b1a9a788`.

## Revisión independiente de integración R8

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

## Revisión visual final R8

# T18 · cierre visual final R8

**Aceptación visual acotada de R8 como mejora PARCIAL.** La composición mesa–sofá–alfombra y los modelos tapizados mejoran el estar respecto aR6; el resultado se conserva al volver a las seis poses exactas. No observo un defecto visible nuevo ni una falta de cobertura que impida este cierre. Integración/publicación siguen condicionadas a gates y revisión técnica de la escena final; no se atribuye4/5 ni se repite la evaluación formal.

## Evidencia final revisada

Se abrió `final_r8/capturas/casa_salon.jpg`, el original1594/uso, ambas vistas de familia4007 y la pareja completa `complementos_r8_comunes/antes.jpg`/`despues.jpg`, cotejando sus JSON. El JSON canónico R8 coincide **byte a byte conR6**: mismos seis puntos, objetivos, alturas yFOV. Sus guardas candidato/antes/después son libres, dentro del recinto, con profundidad/desplazamiento nulos y sin centro dentro de mobiliario. Familia4007 conserva sus guardas.

En3244 y1594, mesa y alfombra se leen asociadas al sofá y más próximas a su uso. Cojines, brazos blandos, base y apoyos dan una silueta doméstica reconocible; terracota/petróleo y textil natural evitan que los antiguos bloques amarillo/negro y la alfombra morada dominen. En1594 esta conclusión ya se apoya en cámaras estables, sin aprovechar los encuadres distintos deR7.2786 conserva camilla+sillas y su carácter compacto; continúa el recorte declarado de uso, compensado por conjunto.

Familia4007 muestra el nuevo asiento verde, mesa y alfombra como un conjunto claro; el mueble blanco y la pared quedan próximos en tono, pero sus contornos y apoyos siguen legibles. La puerta y borde de cámara limitan partes de biblioteca, sin nuevo defecto observado. No se ven bandas, triángulos, superficies negras o apoyos claramente separados nuevos.

## Complemento de lectura: procedencia distinta y honesta

La antigua pose complementaria deR6 fue vetada por la mesa acercada, con delta≈0,187m/profundidad≈0,154m. Su FAIL permanece en `captura_complementos_r8.log`; no se movió mobiliario para liberarla.

El nuevo par se encuentra en **`complementos_r8_comunes/`**, no en la carpeta fallida. Procede de selección entre posiciones libres del constructor realR6 y comprobación posterior enR8. Se cotejó la identidad exacta de ambos miembros: posición `[-5197.280761262942,1.6,-5196.324125616932]`, objetivo `[-5197.7413674141835,0.9499999850988388,-5198.985000007749]`, FOV68, clipped0, guardas libres antes/después y errors[]. Es otra pose respecto al complemento histórico, pero una comparación común válida entreR6/R8.

Desde ella se ven completos biblioteca, puff, mesita y lámpara, con el sofá al lado: el rincón mantiene relación y escala, y el puff blando/neutro se integra mejor. **No hacen falta más capturas para este dictamen acotado.**

## Límites y huellas

Sólo aspecto diurno estático y metadatos. Los PASS CPU22/5admisiones, propiedades funcionales, protección de asiento/puff y tolerancias de AABB fueron comunicados por raíz; no se convierten en comprobaciones propias por mirar las fotos. Las reservas artísticas ya documentadas quedan como mejoras posteriores; no se rehace aquí el diagnóstico ni se anticipa publicación. SinGPU, API, navegador, nuevas pruebas CPU o edición de fuentes/activos. Se conservan los informes anteriores.

Archivos bajo `.cache/calidad/tanda18/`:

- `final_r8/capturas/casa_salon.jpg`: `c1db0f3df8ed77d1d4b175d00f3a7fd73231822401811311c68db10c2d5c799b`.
- JSON canónico comúnR6/R8: `fb038c8a8371c566d1924d448ad0bbd27aa4ac3f7bf9868220e0cf6a514063d9`.
- `familia_r8/familia_0.jpg`: `18dd21c7114e2835c958487135eeef4be83c87cb8e2b33748e089e828458757d`.
- `familia_r8/familia_1.jpg`: `0ef464b63188395cbc7806792b1dc583f8c645192152f48530d6710e946cf1bf`.
- `complementos_r8_comunes/antes.jpg`: `d152d1ba4ef354f6354eaceb1adac3861e97ef84fde18550b1f5798d3d55770c`.
- `complementos_r8_comunes/despues.jpg`: `a37c34fad668293651db68cae288d80892ed052119ec5b573d74e9b7c8db74d0`.
- JSON de ambos complementos idéntico: `54d0e35c56ff915d63daca970bf889fea7c964ed8ede9f4c2011e8cf8e9c8ea0`.
