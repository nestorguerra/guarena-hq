# Revisión visual T13 — composición y mural infantil

**Conclusión:** el mural mejora de forma visible la identidad infantil y el foco sobre la cama. No veo una regresión visual bloqueante causada por el mural en estas seis vistas, pero esto no cierra la calidad global ni autoriza la publicación del intento revisado: queda pendiente la corrección del coste y comprobar su resultado visible. Revisión cualitativa, sin puntuación propia ni Decision API.

## Evidencia y comparabilidad

Se han inspeccionado las tres fichas completas: base T12, composición intermedia sin mural y captura con mural; semillas 4007, 5045 y 1296, dos vistas por semilla. Revisión de archivos existentes, sin ejecutar juego, navegador, build ni GPU y sin modificar producto.

Los JSON actual e intermedio son idénticos byte a byte y semánticamente: mismas semillas, salas, calidad alta, DPR 1, posiciones, objetivos y FOV. Esto confirma las seis cámaras comunes para comparar con/sin mural. No garantiza por sí solo igualdad de todos los materiales renderizados.

De T12 a la composición cambian cinco de los seis registros de vista; sólo 4007/conjunto conserva exactamente la cámara. Por tanto, no atribuyo al mural ni cuantifico como mejora de diseño toda la apertura aparente de T13 frente a T12. En 5045, especialmente, la diferencia de punto de vista favorece ver el eje cama–mesa y cambia mucho la presencia aparente del armario.

## Observación por caso

- **4007:** el mural se distingue inmediatamente donde los adhesivos anteriores resultaban muy pequeños y pálidos. Su masa de verdes y azules añade contraste al conjunto amarillo. La cama y el puesto mantienen su lectura. El dibujo queda parcialmente fuera del encuadre en ambas vistas; es un límite de estas cámaras, no evidencia de un recorte de la geometría. El gran paño blanco izquierdo permanece vacío y muy luminoso.
- **5045:** el mural da continuidad al azul de la cama y al zócalo. Añade un foco reconocible sin ocultar mobiliario. La composición cama–mesa se entiende mejor que en T12, pero esa mejora pertenece principalmente a la tanda de composición y a sus cámaras, no a la incorporación del mural. El armario sigue siendo un volumen alto importante; la pared superior continúa dominando la vista de conjunto.
- **1296:** en uso se ve el mural completo, claramente ligado a la cama y compatible con la alfombra y el guardado. Es el ejemplo más claro de mejora local del paño sobre el cabecero. En conjunto la cámara mira al lado opuesto: permanece una gran extensión blanca sin resolver. La alfombra sigue siendo un elemento muy prominente en el suelo, sin que estas imágenes demuestren una nueva regresión atribuible al mural.

## Diferencias y defectos persistentes

El mismo paisaje se repite en las tres semillas; mejora la identificación infantil, pero aporta poca variedad entre ellas. No hay indicios visibles de que el mural tape puerta, ventana o una función del mobiliario en los encuadres disponibles. Esto no verifica colisiones, interacción ni recorrido real.

Hay una diferencia adicional entre las dos fichas con cámaras idénticas: en la vista de uso de 1296, las grandes superficies azules del mueble en primer plano pasan a gris. La silla con asiento gris ya aparece en la intermedia; no confundir ambas piezas. La raíz comunica la explicación del autor: retirar la galería reduce en uno el índice `it.seed` de los adornos posteriores cuando existía; conserva programa, posición y RNG del mobiliario, pero puede cambiar tintes/texturas de adornos. Esta explicación se recoge como información del autor, no como una auditoría de código realizada aquí. La diferencia visual existe e impide atribuir todo el cambio exclusivamente al mural. La igualdad de JSON registra cámaras y no texturas; no hay base para hablar de metadatos o imágenes falseados. La comparación del efecto del mural sobre la pared sigue siendo legible.

Persisten el predominio de paredes superiores claras, cierta pérdida de relieve por luminosidad y la proximidad visual cama–puesto en las habitaciones estrechas. El mural no arregla por sí solo toda la composición. No se deduce un objetivo 4/5 ni una aceptación global de las casas a partir de esta revisión.

## Estado y siguiente comprobación

Este informe queda vinculado al intento de imagen con SHA-256 `41f2327d8a07e17d0e1a87e85df9d9fc0e44eef06033c188f6fe143f624cde0f`. La raíz ha comunicado un incumplimiento de coste de 61 mallas en tres semillas y una corrección en preparación, manteniendo el límite. Ese fallo funcional no se considera resuelto por esta inspección visual. Si la corrección cambia materiales o geometría, hay que cotejar sus nuevas capturas antes de trasladar esta valoración al resultado final. No he ejecutado ni certificado los contratos o el barrido de 200 casas en esta revisión.

## Huellas de los archivos revisados

- `data/interiores/fichas/casa_ninos.jpg`: `41f2327d8a07e17d0e1a87e85df9d9fc0e44eef06033c188f6fe143f624cde0f`
- `data/interiores/fichas/casa_ninos.json`: `38cc79116a91c38efc3d328d6b51067b2870a14128128d3f3e213cfff4d68057`
- `.cache/calidad/tanda13_composicion_intermedia/casa_ninos.jpg`: `6ef62fa8941a2376bef5a8deb805cbddd0e8fadc91caf56628e24d24e8ee258d`
- `.cache/calidad/tanda13_composicion_intermedia/casa_ninos.json`: `38cc79116a91c38efc3d328d6b51067b2870a14128128d3f3e213cfff4d68057`
- `data/interiores/validacion/historico/calidad_tanda13_base/casa_ninos.jpg`: `88c915094c98fe2652e82a3fdd94d1a8f0eba339d6b4a6c9c5a19dfe5f982d6c`
- `data/interiores/validacion/historico/calidad_tanda13_base/casa_ninos.json`: `3f2c71681463faa1005bab99037173fb4d08c1ffbf83da5b0d8322921b4702e8`


## Adenda — ficha final T13 tras compartir material

**Aceptación visual acotada:** acepto la preservación del aspecto del mural y de las seis vistas tras la corrección de material. He vuelto a abrir y comparar la ficha final con la copia conservada en `.cache/calidad/tanda13/intento_mural1/`. No observo una regresión visible que bloquee esta corrección. Esta aceptación sustituye únicamente el pendiente de cotejo visual del arreglo de coste; no constituye autorización de publicación, certificación funcional ni cumplimiento de 4/5.

En 4007 se conservan mural, colcha amarilla, asiento azul y contraste del zócalo; en 5045 se mantienen el mural, la cama azul, el puesto y el armario; en 1296 se mantienen el paisaje, el suelo/alfombra y las superficies grises ya presentes en el primer intento con mural. No aprecio pérdida nueva de legibilidad, cambios de composición ni nuevas franjas de sombra al comparar ambas fichas a su tamaño disponible. Siguen vigentes los defectos persistentes descritos arriba: paredes blancas dominantes, dibujo repetido y recorte del mural por los encuadres estrechos.

Los JSON final y primer intento son idénticos byte a byte y semánticamente (tres semillas, seis vistas). Las imágenes no son idénticas byte a byte. Como contraste determinista, ambas miden 1280×1158; la diferencia absoluta media por canal RGB es 0,576 / 0,534 / 0,641 niveles sobre 255. La media por vista es 0,607 / 0,398 / 0,618 / 0,389 / 1,028 / 0,461 niveles, en orden de lectura. Hay diferencias locales de hasta 43 niveles; por tanto no afirmo igualdad exacta ni atribuyo la diferencia a compresión sin comprobarla. La aceptación procede de inspección visual, no de un umbral de píxeles.

Huellas de esta adenda:

- Ficha final `data/interiores/fichas/casa_ninos.jpg`: `3c80b75c0047139c1458abadf3383a3dc18df7695ecc1ac648bc2af821989d15`.
- Primer intento conservado `.cache/calidad/tanda13/intento_mural1/casa_ninos.jpg`: `41f2327d8a07e17d0e1a87e85df9d9fc0e44eef06033c188f6fe143f624cde0f`.
- Ambos `casa_ninos.json`: `38cc79116a91c38efc3d328d6b51067b2870a14128128d3f3e213cfff4d68057`.

La raíz comunica 54 contratos y barridos de 200 casas y 81 semillas PASS. No los he reejecutado ni auditado aquí. En el momento de este encargo, la integración continúa y la nueva evaluación formal A/B está solicitada; no doy ambas por terminadas. Se conserva la revisión anterior como historial del primer intento. Sin GPU, navegador ni cambios en producto.
