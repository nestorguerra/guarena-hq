# Tanda 16 cocina — recopilación de revisiones independientes

18 de octubre de 2026. Mejora parcial conservable; juicios A **3,276** y B **3,256**, frente a 3,050/3,048. El objetivo 4/5 sigue pendiente. Esta recopilación enlaza revisiones de agentes distintos de los autores; no añade una puntuación ni sustituye el visto bueno del usuario. El encargo autoriza publicar cada tanda validada.

## Composición

Se conserva la continuidad baja de cocinar–preparar–nevera que ya existía. El nuevo programa añade guardado a dos alturas: banda alta sobre preparación y nevera, columna mayormente cerrada con nicho diario y actividad de cortar pan. Los frentes propios ofrecen bastidor rústico, puertas lisas y vajillero parcial; no se modifica la paleta compartida ni la luz. La mesa, las sillas y el núcleo conservan sus poses. Se observa un cambio de color del asiento de 3244, sin atribuir aquí una causa ni toda la mejora a un mueble concreto.

El pase optativo se ejecuta al terminar el amueblado y no consume RNG. Prueba columna amplia, compacta y huella original, con huecos, reservas, usos y paso existentes; compromete todo o conserva la base. No busca otra planta ni mueve muebles para la foto. En las 22 cocinas del inventario reconstruido, 18 admiten composición y cuatro conservan fallback exacto. El dominio no se amplía a todas las semillas. Los adornos retirados no tenían acciones, venta ni botín; la revisión independiente comprobó las rutas reales de consumidor, no sólo su clase PICKUP. Las variantes de núcleo conservan volúmenes, superficies, roles y masa.

R2 sólo cambia tres compuestos: hogaza con cortes y cuchillo apoyado, y dos anchos de banda vajillero con una cazuela. Apoyos, límites e interpenetraciones se revisaron con geometría real; 54/56/58 mallas en las tres canónicas, materiales y luces sin aumento respecto al candidato R1. Esto no es una medida de FPS. Informes: produccion_r1/revision_final.md y artistica_r2/revision.md.

## Hallazgos y controles

La revisión técnica encontró dos problemas antes de integrar: confiar en activas/metadatos propios para mínimos, y omitir e.interaccion/e.vende en el rollback de dependientes. El suelo de exigencia parte ahora de KITS global para este programa, preservando filtros, cuotas y reservas; el fallback no exige la actividad diferida. Omitir la nevera y sus metadatos falla. Los dependientes con lectura o compra conservan 3→3 acciones al cancelar la composición. Los RED originales se conservan. La debilidad previa de activas no se presenta como una regresión publicada T15.

El contrato artístico final exige la hoja antes de probar su negativo: el filtro anterior y una hoja ausente fallan. Los callbacks CPU dirigidos no equivalen a los 69 del navegador. Los cuatro fallbacks no vacíos y los controles no optantes conservaron P, marco, guardias y siguiente U en el alcance documentado; no se muta KITS.

El primer navegador completo registró 68/69 PASS: el constructor propio de Annie omitía los metadatos de composición. Se conserva ese FAIL y su congelado. La corrección añade una sola transmisión de campos; dos semillas CPU pasan RED→GREEN con geometría, colliders, acciones registradas, puertas, luces y escalera idénticos. La repetición real del navegador pasa los 69 contratos, incluido Annie. Los controles CPU no se presentan como ejecución de caja o siesta; la integración fuente las comprueba aparte. Ver annie_metadata/ e historico_annie_metadata_v1/.

## Evidencia visual y juicios

Base actual T15 y final R2 conservan las seis poses, objetivos y FOV, con seis cámaras físicamente libres, calidad alta manual y DPR1. El capturador sólo reconoce las variantes nuevas de preparación; mantiene algoritmo, altura y guardas. La captura final conserva su procedencia original. Después sólo cambiaron un callback de prueba y la transmisión de metadatos de Annie; se documentan por separado y no se presentan como un render nuevo ni como igualdad de iluminación en píxeles.

La ficha canónica histórica asociada a 3,050/3,048 tenía tres poses de conjunto diferentes. Por ello la diferencia formal no constituye una estimación causal exclusiva del código. Se conservan su ficha y juicios. La comparación visual independiente sobre las seis poses comunes sí respalda la mejora de composición y contraste.

La revisión visual final acepta R2 sin corrección obligatoria ni regresión importante identificada. Pan y cuchillo explican preparación; el vajillero deja de parecer un hueco residual. Límites: pan rectangular y repetido, tapa/pomo de cazuela poco legibles en la ficha, programa parecido entre las dos cocinas grandes y mesa/servicio recortados. No acredita cada acceso por píxeles ni promete 4/5. Ver revision_visual_final.md.

Los dos juicios se llaman una sola vez sobre la misma ficha d445639e300adceccfb7f0c9ed2c9e95064091633584c115b2e4db0ab815fc91. Misma petición, modelo, referencias y rúbrica; distribución, niveles, confianza y score validados. El instrumento conserva cuerpo HTTP/request-id antes de parsear para recuperar un resultado sin repetir llamada; su delta se revisó offline. Una evaluación no verifica acciones ni autoriza publicar. Las otras fichas conservan evidencia histórica, sin recertificar esta versión compartida.

## Gates finales

Pasan 69 contratos, los 40 kits en cinco semillas, 200 casas/1166 habitaciones, 81 laboratorios literales de cocina y la integración fuente con 96 recorridos, ocho vecinos, Annie, comercios y persistencia. Máximos sintéticos: 70.192 triángulos, 60 mallas, nueve luces y 162,9 ms de montaje en este M1; no son FPS ni garantía de otro equipo. Cinco generadores reproducen 22 derivados idénticos. Recursos y marcas pasan.

La integración del paquete final también pasa: ocho casas, Annie, acciones de tres comercios y recarga sin errores. Los nueve gates del congelado de 413 fuentes terminan con salida cero. CI y lectura pública del SHA exacto quedan para después del commit.
