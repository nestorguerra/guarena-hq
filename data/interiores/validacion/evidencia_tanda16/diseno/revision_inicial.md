# Cocina T16 — diagnóstico visual inicial

**Recomendación: recomponer el frente como un conjunto de guardar–preparar–cocinar, con almacenaje mayoritariamente cerrado y una superficie de preparación legible.** No empezaría por añadir objetos ni por otro aumento aislado del armario alto. Propuesta privada; ninguna implementación, captura, build o publicación autorizada por este informe. Sin puntuación ni promesa de alcanzar una nota.

## Evidencia

Revisada la ficha vigente de seis vistas y su JSON: 2786 (matrimonio/rústico, 3,6 × 2,9 m), 3244 (artista/bohemio, 5,6 × 4,2 m) y 1594 (estudiante/joven, 4,5 × 4,3 m), alta/DPR1. La dirección de arte pide formas blandas, material mate con huella limpia, paleta doméstica y lectura funcional conservada; no realismo fotográfico ni suciedad añadida. Se leyó el listado de referencias del moodboard, no las fotografías externas.

La receta ya agrupa cocina, preparación y nevera mediante `frente_trabajo`. Ya existen altos clásico/liso/abierto, de 0,62 o 0,94 m según programa, y muebles bajos amplios desde 14 m². Por tanto, no atribuyo la debilidad actual a que falte agrupación o sólo haya un alto compacto. Mesa desde 13 m² e isla desde 22 m² son opcionales: su entrada en la receta no demuestra que estén colocadas.

## Tres defectos que más limitan lectura y densidad

1. **Jerarquía de almacenaje desequilibrada.** En 2786, la alacena abierta y la encimera concentran muchos paquetes y botellas de colores primarios; el primer plano se parece a exposición de productos. En 3244, alacena y nevera forman una torre estrecha junto a preparación; en 1594 no se reconoce una alacena en estas vistas. El inventario está visualmente presente en unas zonas, pero no constituye un conjunto de guardado doméstico claro. La solución no es igualar el número de botes entre casas.
2. **El frente alto no compone con el volumen de la habitación.** En las dos grandes, alto y campana parecen piezas separadas en un gran paño claro; el resto del muro y techo ocupan mucho más que el programa. El alto abierto de 3244 aporta algo de variedad, pero el frente bajo y la silueta general son casi los mismos que en 1594. En 2786 el color de madera y los bastidores sí ayudan: la mejora debe conservar esa identidad, no reemplazarla por una cocina neutra única.
3. **Preparar/comer se entiende peor que cocinar.** Olla, fogones y fregadero son inequívocos; la superficie auxiliar suele comunicar paquetes apoyados más que una tarea. Las vistas grandes dejan ver respaldos recortados en el borde inferior, pero no permiten evaluar mesa, puestos ni relación con el frente. La sensación de cocina poco habitada procede en parte de esa cobertura, y en parte de una encimera sin actividad clara. No se puede concluir que la mesa falte ni moverla para favorecer la foto.

## Una intervención coherente, a escala de programa

Proponer un **frente doméstico de preparación y guardado a dos alturas**, escalado por espacio realmente disponible: conservar cocina/fregadero/campana y acceso a nevera; relacionar una zona baja de preparación con un alto de vajilla y un extremo de almacenaje cerrado o mixto. Integrar la alacena como parte de ese extremo, sustituyendo su exposición abundante por puertas y un único hueco de uso diario. No añadir otra fila de muebles sobre la existente.

En la compacta 2786, el programa debe caber dentro de las huellas actuales: reorganizar visualmente la alacena y liberar una parte de la encimera, manteniendo madera oscura y bastidores. En 3244/1594, comprobar si un tramo coherente de guardado alto puede acompañar la preparación y conectar visualmente con la nevera sin invadir campana, puertas o ventanas. No extender armarios sobre el fuego por completar una banda ni exigir un tramo que no cabe; el fallback conservaría el programa actual.

El conjunto debe dejar **una superficie de trabajo continua reconocible**, con una sola actividad —por ejemplo preparar pan— y el resto de provisiones guardadas. Esa actividad puede reutilizar el lenguaje ya presente en la isla de tabla y pan; no exige añadir una isla ni repetir utensilios pequeños. Mantener la lectura rústica de 2786, vajillero parcialmente abierto en 3244 y puertas lisas en 1594 da variación de uso y frente, además de color. Un contraste moderado entre frente/encimera y fondo ayuda a separar estos volúmenes; pintar toda la pared más fuerte no organiza el almacenaje.

La hipótesis común es reducir ruido en la compacta y aumentar volumen útil relacionado en las grandes. Necesita comprobarse; no garantiza mejora en las tres. Antes de implementar habría que medir el tramo libre, conservar roles y acciones, reservas de preparación y paso de 0,80 m, acceso de nevera y guardado, huecos y coste. No se propone ampliar el solver ni alterar semillas, cámaras o límites.

## Límites y siguiente decisión

Las vistas de uso de 3244/1594 recortan el alto y la preparación lateral; las de conjunto recortan casi todo el posible comedor. El JSON actual no incluye las guardas de cámara posteriores de T15. No demuestra una colisión, pero tampoco permite afirmar cobertura funcional completa. No se ha reconstruido ninguna casa ni ejecutado el juego. T15 afecta a niños; esta revisión no abre una tanda de implementación de cocina.

Si se acepta explorar el programa, el primer entregable debería ser una propuesta geométrica aislada con las tres huellas y el frente completo, antes de modelar más objetos. La mesa queda como cuestión de evidencia pendiente, no como blanco de una recolocación para la foto.

## Fuentes y hashes SHA256

- `data/interiores/fichas/casa_cocina.jpg`: `9fa9b7494291de50566f7ff4af2685e8c3b1357f281f16924bfae487f7204020`.
- `data/interiores/fichas/casa_cocina.json`: `2d84be58594101a5a8dd95d0df7785743029787f789be521f9a3df4911f70351`.
- `docs/plastilina.md`: `3e90dce114bc9bdcc031f44a9078df01f1c98cfe305c51b145b1d03178b11b04`.
- `docs/interiores.md`: `09801b3599526a978b702609c224d8fd47f2257d2c8696c474e15e3dbde5476a`.
- `docs/calidad-viviendas-4-2026-10-17.md`: `b0333ce82327945bc02044a66bd5c2e24eaf2171e1bb16e43ce68afeee6e569b`.
- `tools/interiores/kits_vivienda_a.py`: `ee47f465ab79dae2fe3854cd24afae17dc4275b3a07d5ce508ee885c8127cb93`.
- `tools/interiores/catalogo_vivienda_a.py`: `cfed6ea37b35fc1aeef355b42a31219279b2da2f27254dec428c93b00c236690`.
- `tools/interiores/composicion_domestica.py`: `8d74bdbda14dc3b4ee6729e4985ec0e03673656d524a2a23b5c068b0a4d3656f`.
- `src/acabados_vivienda.js`: `5c65b324b83ffed145793b01bb5635b85b31f6b71c232f32879f42f48adc71e9`.
- `tools/interiores/moodboard_vivienda_a.json`: `0b45a7a504d71993893a0c94e76211b0db733a1ab2e75869c970905528a454f1`.
