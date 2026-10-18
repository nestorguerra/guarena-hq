# Revisión independiente del contrato de composición T15

Dictamen: **sin hallazgos P1/P2** en el parche privado revisado. Adecuado para integrarlo y ejecutar el harness real; no acredita por sí solo calidad visual ni presupuesto runtime.

Parche revisado: `infantil_composicion_contrato.patch`, SHA-256 `9ec7e4167b64d8ede0ee7e3f2ca47584ca71f545eba5db5eca68fafe12267b6e`. Recibo CPU del autor leído: SHA-256 `efbfe736b58bdcbe6df728a61d9bac5c83f4fc505a5612ce9e413675546f1215`. He verificado independientemente estos hashes y `git apply --check`; he leído el callback y su instrumento CPU. No he vuelto a ejecutar la CPU ni modificado su evidencia.

El caso usa `H.buildVecino`, las envolventes resultantes y los puntos finales de uso. Exige descanso agrupado, reserva frontal física del armario, llegada próxima a la entrada y accesos no vacíos a ocultación/despertar con cuerpo de 0,8 m. En 4007/5045 la distancia física estricta de 0,8−1e−6 impide que una celda favorable de la rejilla oculte una estrechez real. No depende de la galería, el mural o la presencia del estante opcional. El bloque `finally` mantiene la limpieza habitual del harness y el caso no modifica recetas compartidas.

La prueba privada conserva un límite claro: constructor, geometría de colocación, collider y corrección de usos son reales; canvas, mallas de catálogo, acabados y agrupado son dobles. Sus siete negativos ejercitan los asserts del mismo callback y el positivo sin estante evita convertir una pieza opcional en obligatoria. La receta T12 congelada constituye un negativo real, no una comparación accidental contra la activa T13.

Límites / Declined to judge: no ejecución del harness completo en navegador; no render, sombras, atlas, drawcalls o presupuesto GPU; no nota estética; no certificación de todas las semillas ni de las adaptaciones del mural pendientes. La tolerancia horizontal de 2 mm en las parejas y 5 mm en reservas es explícita y no se utiliza para rebajar el paso mínimo de 0,8 m.
