# T17/T20 · revisión independiente del cuarto contrato de tela

**APROBADO de forma acotada el contrato de tela y su incorporación al parche de pruebas/CI para ejecutar contra el candidato sellado. Sin bloqueos estáticos detectados.** No es GREEN del candidato, aprobación de modelos, integración de producto ni publicación. Esta revisión se concentra en el cuarto contrato; los otros tres conservan la revisión previa de `codigo_final` y no se presentan aquí como una segunda validación ejecutada.

## Controles leídos

- **Ventana legítima:** toma la estancia real, su marco en `h.rooms` y los huecos físicos `h.views`, que `HouseBuilder.view` sitúa en coordenadas mundiales. La cota inferior descarta las puertas convencionales; el centro del hueco se asigna al marco de habitación. No deduce una ventana porque encuentre tela ni usa una reserva abstracta como prueba de existencia. En1594 sin ventana exige también ausencia de tela y sólo entonces continúa; antes ya comprobó mesa única, ordenador único y su apoyo. El guard está dirigido a estas tres muestras, no es un clasificador universal de cualquier hueco arquitectónico.
- **Geometría real:** intercepta `HouseBuilder.add` y clona antes de que éste transforme la geometría recibida. Aplica a la copia la misma rotación Y y traslación del builder. Las cajas globales de las telas se usan únicamente para seleccionar las de la estancia; la colisión utiliza sus triángulos indexados o no indexados y `Box3.intersectsTriangle` contra cada pieza del puesto, ordenador y paneles de estudio.
- **Transformación correcta:** la inversa `x*cos−z*sin`, `x*sin+z*cos`, tras quitar origen de estancia y centro de pieza, coincide con la convención de `rot`/`partes` en `interiores_geo.js`. Y se expresa en la misma cota local que `b.y0/y1`. Para piezas con inclinación X/Z, el contrato conserva la aproximación OBB envolvente de `partes`; no afirma intersección contra el triángulo real de cada mueble.
- **Tolerancia y longitud:** retrae1mm cada cara de la caja para no contar mero contacto. Las cajas que quedan vacías se omiten; no es una garantía para espesores≤2mm. Comprueba además paños cortos con top2,225/bajo1,28 y altura0,945, usando tolerancia1e−5. Estas cotas forman parte del diseño propuesto; un cambio de diseño legítimo exigiría revisar el contrato explícitamente.
- **Negativo dirigido:** sólo3244 alarga copias de los triángulos cortos a2,05m conservando top y X/Z. Exige recuperar una intersección. No modifica muebles ni geometría viva. Las cotas min/max copiadas no se recalculan, pero el oráculo negativo sólo consume `tri`, por lo que no invalida la prueba.
- **Limpieza:** el `finally` interior libera la casa si llegó a construirse y, mediante un segundo `finally`, libera los clones aun si falla esa limpieza. El `finally` exterior restaura `prototype.add`. El primer FAIL no deja instalado el interceptor. No hay llamadas asíncronas dentro de este interceptor; los casos del harness se esperan secuencialmente.

## Evidencia exacta y límites

El fragmento actual está incluido **literalmente** en `validacion_t20.patch`. Los seis hashes del manifiesto específico `manifest_tela_r2.json` coinciden con sus archivos. El manifiesto anterior `manifest_tela_y_cierre.json` es anterior a la corrección de ventana; no se usa como sello vigente.

`contratos_estudio_RED_T16_v2.json` conserva tres FAIL esperados por falta del programa nuevo en T16. No es resultado del cuarto contrato. `tela_RED_R2.json` registra el callback actual contra el greybox R2: falla en3244 por intersecciones en partes0/3/6/7; registra27clones/27disposes y prototype restaurado. Como se detiene allí, **no acredita ejecución del resto del callback en1594/1481 ni del negativo de tela alargada**.

`tela_ventanas_cpu.json` sí ejecuta por separado la región exacta de clasificación en las tres muestras:3244 y1481 tienen una ventana/dos paños;1594 cero/cero. Los negativos eliminan paños donde hay ventana e introducen tela en el estudio interior, y se rechazan. Eso valida el guard; no sustituye el GREEN de tela corta frente al modelo final. Estos recibos se han leído y cotejado por hash; este revisor no ha reejecutado CPU o navegador.

## Pruebas y CI

El parche añade los cuatro contratos detrás de `tanda>=20`, importa `mapaPaso` para el tercer contrato y cambia únicamente `--tanda 19` a `--tanda 20` en el paso existente del workflow. No elimina otros controles o pasos CI. Es adecuado preparar esa incorporación para que CI ejecute el nuevo contrato, condicionado a ejecutar primero la batería contra el candidato final sellado y conservar los recibos. No se ha aplicado el parche ni ejecutado CI.

Pendiente: GREEN completo del cuarto contrato en las tres muestras, negativo largo de3244 efectivamente ejecutado, resto de contratos y revisiones del candidato final. La prueba dirigida no acredita por sí sola todas las ventanas optantes, conservación global de no optantes/Annie ni apariencia de las cortinas; esas garantías corresponden a la revisión y cobertura del producto.

## Hashes revisados

- `validacion_t20.patch`: `9a9cb6a41861fd9fee50a503765788c3004fa900d25863016fff6999ab403d83`.
- `contratos_tela.fragment.js`: `a25a4816c5c02f335e53c6c5ac7831f4bca39bf106c53163a183a39e6d97f2a4`.
- `manifest_tela_r2.json`: `4dc31dfa0999331615c4108fc0658ddb0ce82ba0b847b9c56ce3eaead694ee5e`.
- `tela_RED_R2.json`: `b3e2ffb1b9433445080fbfed75099f9ddf6cc24ce822193ce0e7be2b0c340203`.
- `tela_ventanas_cpu.json`: `238cf511f1a0fe239b527116234e8bfd88cef3bb62e9c300dca1804aa2a16a9f`.
- `contratos_estudio_RED_T16_v2.json`: `6306043e77fa9c8ea3df813f86ea9af1b7215c8de11cce4b95e942b7b24a35cc`.

Sólo lectura y este informe privado. Sin GPU, API, fuentes activas, modelos mutables, publicación ni afirmación de GREEN final.
