# T17 · Revisión visual final R3

**APROBADO visualmente para continuar la integración y la evaluación formal previstas, sujeto al cierre técnico separado.** Las seis vistas y la entrada adicional recuperan el acabado de R1; no detecto defectos visibles nuevos que exijan otra corrección antes de ese paso. No es autorización de publicación ni afirmación de 4/5.

## Evidencia verificada

- Ficha R3: `cfe597964fc9e1c5626c9886a1521b01780fc4b5f558526003287dc4c7b04fc2`.
- Ficha R1: `7e5f2635ce48ddb7438ccf762952b1126fa926b39d5fe719ee62724e35c21503`.
- JSON canónico R3 idéntico byte a byte a R1/R2: `a2606f95d3802b56e3a726c19611e5b0bc2779c94f48d5bd261e37120f82f6cd`. Seis poses, objetivos y FOV iguales; diez hashes de procedencia cotejados sin discrepancias.
- Procedencia canónica: 493 inputs estables, seis guardas libres, calidad alta/DPR1. El capturador revisado veta `__errs` antes/después de render y programas con `diagnostics.runnable===false`.
- Entrada final 1594: `455846e7514adb0c2f3620080055b447105597b6f4831fc282e2f20e6e0dc8db`. JSON `5bdeb491d3682db43833896ecfc07770dbc689bf63682647969c59a2b575a208`, exacto a R1. Sus tres hashes de procedencia coinciden; ésta registra 493 inputs estables y punto/objetivo/FOV/inicio/marco exactos al greybox R2.

He abierto la ficha R3, sus seis imágenes individuales y la entrada adicional. La entrada no sustituye las canónicas. No he ejecutado capturas, GPU, navegador o API.

## Resultado visible

**3244:** reaparecen el fondo verde liso del frente, los paños claros, techo claro y suelo sereno. Biblioteca abierta, bajo, lámina, ordenador y silla conservan su lectura. La cortina corta mantiene el remate de R1 por encima del puesto; no aparece una invasión nueva. En la vista opuesta persiste el gran paño vacío y sólo se ve una parte del apoyo secundario de lectura, límite de composición/evidencia ya documentado.

**1594:** vuelve la combinación azul del frente con cal clara y suelo calmado. El puesto se reconoce en la vista de uso y el guardado en la otra; la entrada fija mantiene pantalla, tablero y silla visibles pese a la biblioteca en primer plano. Los puntos claros sobre libros/biblioteca/puerta siguen perceptibles, coherentes con conservar el material artesanal de objetos. No se han limpiado globalmente todos los materiales.

**1481, sintética:** vuelven pared de acento marrón, cal y suelo liso. Desaparece la constelación de motas claras sobre el paño marrón que distraía en R1, mientras quedan pequeños puntos sobre el bajo. La partitura y el frente se leen sin pérdida visible de calidez ni de contraste. La cortina corta y los tres cuadros repetidos conservan el aspecto ya revisado; no constituyen una regresión nueva de R3.

El cambio visible ahora sí coincide con el alcance solicitado: limpiar superficies nuevas sin borrar la textura de muebles/puertas. No afirmo identidad píxel a píxel de todo lo ajeno ni aprobación funcional por fotografías.

## Cierre de la incidencia R2

He leído `diagnostico_shader_R2.json`: el RED recoge el error real de multiplicación entre `highp float` y `const int`; la conversión explícita `float(CLAY_LINT)` deja GREEN sin errores en ese diagnóstico. La hipótesis técnica de la revisión R2 queda confirmada por ese recibo. R3 muestra nuevamente las superficies que no se renderizaban.

`revision_visual_final_r2.md` permanece intacto, SHA `c28645731b245240b0591cafc5ed0f057ebe57ad934c750ebd1cf488080e3667`. La captura R2 continúa rechazada y no debe utilizarse para evaluación formal. Este dictamen corresponde exclusivamente a R3.

## Límites que se conservan

El frente adulto y la escala del puesto mejoran respecto al conjunto T16, pero frente a T16 sólo una de las seis poses coincide: no atribuir toda diferencia de imagen únicamente al producto. Permanecen áreas vacías amplias, repetición de mobiliario entre perfiles y la relación de valores cálidos en 1481. No se convierte esa mejora relativa en una nota formal.

No se ha revisado aquí el recosteo final ni se sustituyen los contratos, integración fuente/paquete, controles de otros kits o verificación pública. Esta aceptación visual permite continuar con esas comprobaciones y evaluar la imagen exacta una vez por juicio; no acredita su resultado por adelantado.
