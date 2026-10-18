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
