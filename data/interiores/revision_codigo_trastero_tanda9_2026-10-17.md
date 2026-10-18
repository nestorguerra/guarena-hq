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
