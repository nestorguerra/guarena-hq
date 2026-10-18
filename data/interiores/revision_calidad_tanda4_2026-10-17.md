# Tanda 4 — comparación independiente de iluminación

17 de octubre de 2026. Se han reabierto las fichas actuales de baño (17:56:56) y trastero (17:57:09), sus JSON y los snapshots anteriores indicados por los recibos A/B de `data/interiores/validacion/historico/calidad_antes_luz/`.

**Conclusión:** el cambio aporta profundidad y apoyo de los objetos, especialmente en trastero. Las zonas de uso siguen legibles. El coste visible es una sombra más dura, con bordes algo escalonados en algunas proyecciones próximas. No observo una regresión importante de representación ni la reaparición de los artefactos del alicatado en estas imágenes; conviene conservar la cautela sobre la estabilidad de las sombras en movimiento.

## Evidencia comparada

- Baño: snapshot `799fbc5319507e588606d31b0e9881222ea479d6765b8cecce75ab4a1b222d29.jpg`.
- Trastero: snapshot `3997bfe37ca7910520ad7ae0e1077bc8b011c3d2b94eba15d6ce45410d77df8d.jpg`.
- Ambos existen y su SHA-256 coincide con el campo `ficha_sha256` del recibo. A y B señalan el mismo snapshot por kit; no se han tratado como dos imágenes anteriores distintas.
- Los objetos y encuadres coinciden visualmente entre antes y después. Los JSON actuales mantienen las tres semillas por kit y sus vistas de uso/conjunto. Esta comparación permite observar el efecto sobre las mismas superficies, sin confundirlo con una nueva distribución.

## Baño

### Ganancia visible

- 2786: gabinete, toalla y armario de toallas proyectan sombras reconocibles. Las baldas del armario tienen más profundidad y el lavabo queda mejor separado de la pared.
- 3244: se refuerza el apoyo del gabinete y la lectura del interior de la bañera, la cisterna y la ducha. Las caras claras siguen siendo legibles; no aparece una zona de uso negra.
- 1594: el mueble del lavabo tiene más volumen y la columna de ducha proyecta una silueta visible sobre la pared. Los sanitarios se separan algo mejor del pavimento.

### Dureza y límites

Las sombras del frasco sobre el armario, la columna de ducha y otros elementos pequeños son más recortadas que antes. No impiden identificar las piezas, pero hacen la iluminación algo menos suave.

En la vista de lavabo 2786 aparece además una franja de sombra bastante recta en la pared de la habitación contigua, visible por el hueco de entrada. Es una diferencia real respecto al snapshot; con una imagen fija no puedo decidir si corresponde a una proyección coherente del vano o a un límite de la luz. No se presenta como fallo confirmado.

No reaparecen los antiguos triángulos/franjas del alicatado ni la banda rayada detrás del lavabo. Las nuevas líneas de sombra de elementos identificables no se confunden con aquellos artefactos de superficie.

## Trastero

### Ganancia visible

- 1594: las sombras entre cajas, bajo baldas y sobre la pared separan mejor cada nivel. La estructura de la estantería ya no se funde tanto con el fondo claro.
- 3886: la pila del centro tiene mejor lectura de caras y apoyo; las cajas de la estantería ganan profundidad. Las etiquetas claras se conservan legibles.
- 4589: la pila contra la pared y el almacenaje próximo a cámara tienen más volumen. Se mantiene la lectura de las dos zonas de almacenaje y del suelo libre entre ellas.

### Regresión de suavidad

En 1594, sobre todo en la pared derecha de la vista de conjunto, las proyecciones de la estantería son grandes, duras y algo escalonadas. En 4589, la sombra de la pila también tiene un borde muy definido. Son siluetas atribuibles a los objetos visibles, no una prueba de geometría rota, pero llaman más la atención que en la versión anterior.

No veo desaparición importante de objetos en oscuridad ni pérdida de la función doméstica. La variante nueva comunica mejor profundidad; la anterior era más uniforme y suave.

## Cierre y alcance

Las seis muestras conservan cobertura de uso y conjunto. La ganancia más clara es el apoyo y separación del almacenaje; en baño es más contenida. La dureza de las sombras debe considerarse un acabado pendiente si el objetivo es una luz de diorama artesanal suave.

Este pase solo compara JPG fijos. No verifica el porcentaje de relleno, el tamaño del mapa de sombras ni la selección de una luz principal comunicados por el constructor; tampoco permite comprobar parpadeo, desplazamientos bruscos o estabilidad al mover la cámara. Una toma en movimiento resolvería ese límite cuando corresponda, sin sustituir este resultado estático.

Sin navegador, puertos, pruebas ni cambios de código. Sin puntuación manual, sin aprobación formal y sin afirmar que se haya alcanzado 4/5.

## Cierre de suavidad — candidato continuo de 18:10–18:11

Se han reabierto baño (18:10:40), trastero (18:11:03) y sus JSON actuales. La comparación se ha hecho contra los snapshots exactos de los recibos de calidad_luz_discreta: baño db649c186ece76bd1e84e4c5efa0ec13dbc8660d6e52184f63bb978efd1e8bfa.jpg y trastero 0927405151b5b2a8f2d910f958e9b3949b506cd1dd4334f773f01b9159232a25.jpg. Ambos hashes coinciden con sus recibos.

**El candidato actual suaviza el resultado sin perder la lectura del volumen. No observo una regresión importante nueva en estas imágenes.**

- En trastero 1594, las proyecciones de la estantería sobre la pared derecha son más claras y menos recortadas. Se atenúa el aspecto de silueta escalonada señalado antes. Las sombras bajo baldas y entre cajas siguen aportando profundidad.
- En trastero 4589, la sombra de la pila sobre el zócalo es menos dura. En 3886 se mantiene el apoyo de la pila y la lectura de las cajas, con un contraste algo menos contundente. Esa pequeña pérdida de oscuridad no oculta los objetos ni sus etiquetas.
- En baño 2786 ya no destaca la franja horizontal de sombra de la pared contigua como en el candidato discreto. El gabinete y el armario mantienen volumen.
- En baños 3244 y 1594, las siluetas de las piezas pequeñas y la ducha continúan visibles, pero son menos dominantes. Se conserva el interior legible de la bañera y la separación de los sanitarios. El alicatado sigue sin las antiguas franjas y triángulos de superficie.

Persisten algunas líneas de sombra reconocibles y relativamente definidas, sobre todo en la ducha; el cambio no convierte toda proyección en una sombra difusa. En comparación, el equilibrio actual resulta más próximo a la suavidad del diorama que el candidato discreto, manteniendo parte de su ganancia de profundidad.

**Límite esencial:** JPG y JSON no permiten verificar la mezcla continua, el desvanecimiento de sombra ni la ausencia de salto al cruzar una puerta. Tampoco acreditan radio o intensidad del mapa de sombras. Este cierre solo confirma la suavidad y legibilidad estáticas observadas; la corrección del problema temporal requiere su evidencia de movimiento correspondiente.

Se mantienen las demás carencias documentadas. Sin notas numéricas ni aprobación formal del objetivo 4/5. No se han usado navegador ni pruebas, ni se ha modificado código.
