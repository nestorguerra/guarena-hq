# T18 · revisión visual independiente R4 + acabado final R2

**Mejora parcial integrable; no veo defecto visual bloqueante de publicación de prueba en lo mostrado.** La agrupación aporta un uso legible en1594 y el acabado mejora las tres muestras. No equivale a lograr4/5 ni a validar funciones/coste con imágenes. En3244 sigue faltando una vista frontal de la biblioteca para cerrar visualmente el rincón nuevo. Es una laguna de evidencia, no una colisión observada ni motivo para mover muebles por la cámara.

## Comparación y cobertura

Se abrieron las fichas de base T17, greybox R4 y finalR2, más originales R4 de3244/uso+conjunto y1594/uso+conjunto, y finales de3244/uso,1594/conjunto y2786/conjunto. Los JSON completos de las tres fichas son **idénticos**: seis poses/objetivos/FOV conservados. Se cotejaron las guardas del final en candidato/antes/después: cámara libre, dentro del recinto, profundidad y desplazamiento nulos, sin centro dentro de mobiliario. Procedencias: base492inputs, R4/final493, seis guardas, captura alta/DPR1 y veto de errores/shaders. Esto no certifica toda la circulación ni uso.

- **1594:** biblioteca, puff, mesita y lámpara se leen juntos y a escala doméstica. En conjunto se ven las cuatro piezas completas junto al sofá; el nuevo asiento de lectura deja de aparecer aislado en el otro extremo. La TV queda parcial en uso y fuera del conjunto, como limitación heredada; no se altera ese núcleo en esta propuesta. El acabado azul distingue el estar de paredes claras, y el suelo permite leer las patas y huellas.
- **3244:** en uso se ven puff–mesita–lámpara reunidos al fondo y se comprende mejor un segundo ámbito. Pero la biblioteca sólo aparece prácticamente de canto junto al borde de la ventana; conjunto mira hacia sofá/TV y excluye el rincón. Por tanto, estas vistas **no demuestran toda la relación biblioteca–asiento**. El estar principal se mantiene reconocible y la nueva pared verde lo ancla. La gran superficie central sigue abierta; no es por sí sola un fallo, pero el pequeño puff sigue teniendo poco peso funcional frente a una sala de35m².
- **2786:** conserva la composición compacta de camilla+sillas, orejero y biblioteca. El suelo cerámico tranquilo y la cal reducen el ruido y conservan madera/textil rústicos. Uso corta la camilla por proximidad; conjunto muestra su tablero y las sillas. No ocultar el recorte ni tratarlo como una regresión de amueblado. No requiere imponer el rincón de las grandes.

El gris R4 es una intervención del capturador: no se juzga su falta de contraste como acabado de producto. El finalR2 sí permite valorar el cambio local de pared/suelo: mejora clara frente al jaspeado y motivo mural repetido, sin franjas, triángulos, manchas negras o pérdida importante de contorno nuevos observables. No se ha capturado noche ni movimiento.

## Qué sigue faltando hacia el objetivo

1. **Jerarquía real del rincón grande:** el puff de40cm y la mesita son proporcionados, pero parecen un apoyo ocasional más que un ámbito de lectura asentado. Una futura variante con asiento cómodo reconocible y respaldo, cuando quepa con su uso, aportaría más que agregar libros/cuadros. Antes de decidirla, ver de frente3244: no deducir un fallo del mobiliario que la cámara no muestra.
2. **Calidad y variedad de las masas principales:** sofá/aparador y cilindro del puff siguen siendo volúmenes bastante elementales. Los colores muy saturados de sofá/puff y los mismos jarrones de flores primarias dominan sobre las actividades. Falta articulación del textil y del asiento y una selección doméstica menos repetida; eso exige detalle útil de modelos/paleta local, no más miniaturas ni nueva iluminación. El acabado recién capturado es un apoyo, no sustituye esta carencia.

## Captura complementaria mínima

Conservar las seis canónicas. Añadir **una vista humana del rincón3244**: puede reutilizar la posición ya libre de su conjunto, `(-5198.41614929311,1.6,-5197.806838598195)`, girando la mirada al grupo biblioteca–puff–mesita, con objetivo de altura doméstica y FOV68. Es una posición físicamente libre acreditada por el JSON; el nuevo ángulo aún no se ha capturado ni se garantiza que incluya todos los bordes. Si no cubre el grupo completo, seleccionar otra pose con guardas físicas estrictas y registrar su procedencia. Capturar también la base desde la misma pose/objetivo para distinguir el cambio; no reemplazar vistas desfavorables ni mover mobiliario para liberarla.1594 ya muestra el grupo entero: no exige otra vista para esta intervención.

## Alcance técnico y dictamen

Se leyó el recibo existente `postpaso_r3/resultados.json`; el módulo de composición coincide byte a byte con el de R4. Registra dos aplicaciones3244/1594 y20fallbacks; uso sin errores. No se reejecutó CPU. La lista de acciones de3244 conserva tipos/recuentos, pero reproyecta el espejo unos7cm; no describir todas las posiciones de acciones como exactas.1594 mantiene su lista exacta. La aprobación técnica de rollback, asientos registrados, admisiones,81montajes y presupuesto pertenece a sus recibos/revisores, no a esta inspección de JPG.

**Aceptación visual acotada del finalR2 como mejora parcial**, condicionada al cierre técnico habitual. La cobertura incompleta3244 impide afirmar que el programa entero nuevo fue revisado visualmente, pero no aporta un bloqueo observado para integrar/publicar la mejora de prueba con ese límite explícito. No declaro objetivo formal alcanzado ni autorizo una acción externa; raíz conserva el cierre/publicación del encargo.

Hashes de fichas utilizadas:

- Base `.cache/calidad/tanda18/base_T17/capturas/casa_salon.jpg`: `1e5ec49b0658d7f520d043da91c72237483a4e033f171548f2439e97587285f4`.
- R4 `.cache/calidad/tanda18/greybox_r4/capturas/casa_salon.jpg`: `df99760bb37d4ab8bce7efc012a314464d3ff451a3c1df962e2a949a3be07df7`.
- Final `.cache/calidad/tanda18/final_r2/capturas/casa_salon.jpg`: `e68fca946010e38f22706349eb3afe481f3be86bc9878417d8d61ba4950ed8e4`.
- JSON común: `fb038c8a8371c566d1924d448ad0bbd27aa4ac3f7bf9868220e0cf6a514063d9`.

Sin GPU, navegador, API, puntuaciones propias ni edición de fuentes/activos.
