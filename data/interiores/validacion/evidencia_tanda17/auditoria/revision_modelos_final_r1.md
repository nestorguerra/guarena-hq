# T17 · Revisión independiente de modelos finales R1

**APROBADO para preparar y capturar la copia privada final. Sin bloqueos P1/P2 detectados para ese siguiente paso.** No es aprobación visual, integración, publicación ni GREEN de los contratos T20.

## Sello y comprobaciones propias

- Manifiesto `5bb39f7bc90b1a8091a9cb302669777719e99e6ae2de19e44c0ee1fee7be9c5a`: 298 entradas cotejadas, cero discrepancias.
- Parche combinado `222f89128d77a6ff61a28d2d226c192765877cdd1cb0116625a2b94601bb0dd9`: cinco fuentes. Reproduje sus hunks enteramente en memoria sobre `base/`; las cinco salidas coinciden byte a byte con `candidata/`. No se aplicó a disco ni a producto.
- Las cinco fuentes activas siguen siendo exactamente los bytes base T16. El delta privado es el declarado: cinco fuentes y cuatro derivados; dos de esos derivados no estaban incluidos en `base/`. No se incorporan cambios del motor `locales.js` ni del validador.
- El acabado R2 de raíz está incluido: **aplicar sólo el combinado**, nunca sumar `acabados_r2/acabados.patch`. Regenerar en copia privada; no copiar derivados globales de la candidata.
- Comparé directamente los recibos R2/final: mesa, bajo, biblioteca, silla y PC conservan x/y/z/ry en 3244,1594,1481. El informe geométrico comprueba además envolventes. No se exige invariancia de adornos, entradas opcionales o su RNG, que cambian de forma declarada.

## Lectura de código y de la evidencia sellada

La receta mantiene el orden mesa→bajo→biblioteca y la silla frontal vinculada. El ordenador conserva su definición T16 y clase PICKUP, separado del mueble. Las piezas nuevas conservan roles domésticos; silla y orejero propios copian geometría y asientos de los compartidos. El programa original queda filtrado para no optantes, sin introducir los nuevos IDs en otros kits.

La biblioteca final tiene huecos reales, baldas, laterales y trasera delgados; el bajo y el escritorio tienen estructura apoyada. `geometria.cpu.mjs` distingue ensambles estructurales de las penetraciones entre pertenencias. Sus negativos detectan carpeta elevada y pila solapada. La prueba de escritura incluye todos los objetos apoyados de las tres canónicas, incluida la lámina: 0,60×0,30 m libres. La lámina arranca en el tablero y toca el respaldo; el PC tiene apoyo y el desplazamiento negativo de 4 cm choca. Esto es evidencia geométrica CPU, no una prueba de interacción viva.

El pool declara 54 IDs por perfil y acredita conservadoramente 33 utilizables, sin contar variantes que no caben en la balda. `datos.py` y su regeneración están documentados; no se ha reducido el mínimo. Los tres perfiles tienen grupos de consulta y dibujos propios, cuya legibilidad real sigue pendiente.

`windowIn` recibe la habitación propietaria y acorta sólo la tela de estudio de artista/estudiante/músico. Mantiene el top 2,225 m y sube el borde a 1,28 m, sin alterar `curtainGeo` global, hueco, vidrio, alféizar ni extracciones RNG. El instrumento captura triángulos reales antes de que `HouseBuilder.add` transforme la geometría y los compara con las OBB de piezas finales. Conserva el RED previo. En los 23 casos sólo cambian dos paños de 3244 y dos de 1481; 1594 carece legítimamente de ventana. No hay contactos detectados en las piezas comprobadas; el inset de 1 mm excluye contactos superficiales y piezas de espesor total ≤2 mm. No equivale a demostrar ausencia absoluta de todo contacto microscópico.

`full.cpu.mjs` construye 22 identidades del pueblo y 1481 sintética: sólo 3244/1594 son estudios reales y hay 20 controles sin estudio. Los recibos no tienen errores; marcos, programa de luces, botín y datos de otras estancias coinciden. Máximo de la cohorte: 59 mallas, 63.274 triángulos y 9 luces. No son 23 estudios, un barrido 200/81 ni una medida de FPS. La igualdad de los 20 controles se refiere a las comparaciones instrumentadas, no a una comparación rasterizada de cada material.

Annie 12/13 mantiene cinco estancias, geometría/poses/materiales de construcción, colliders, acciones y posiciones exactos según comparación profunda del instrumento; 60 mallas y 9 luces. La fuente singular no cambia. La comparación de materiales usa metadatos y canvas simulado, no píxeles de textura.

El fallback fijo 4 completa el programa en 3,2×2,8×2,75 m. `si_no:true` de biblioteca permite el fallback individual existente, sin vínculo `de` ficticio ni retorno a T16. El instrumento compara layout y dos extracciones RNG posteriores con el mismo kit sin grupos. Entrada y centro de uso de biblioteca son libres y alcanzables con cuerpo de 0,80 m; el recinto reservado falla tras 12 intentos sin cambiar dimensiones. **La ventana del laboratorio no está reservada y puede quedar parcialmente tapada**: este recibo no aprueba esa imagen ni garantiza ventanas para otros contextos. Las casas reales usan sus reservas y tienen validación propia.

## Condiciones y límites del siguiente paso

Procede una captura privada del combinado sobre la copia T16 fresca, con regeneración y comprobación de fuentes antes/después. Los contratos T20 preparados deben ejecutarse en ese snapshot; su GREEN final sigue pendiente. Esta revisión ha leído instrumentos/recibos y hecho cotejos deterministas de archivos y JSON; no ha vuelto a ejecutar constructores, generadores, navegador, GPU ni API.

En la imagen habrá que comprobar: biblioteca abierta y lectura del puesto en 1594 desde entrada y canónicas; lámina legible detrás del monitor sin saturarlo; remate corto de cortinas en 3244/1481; apoyo secundario de lectura y equilibrio entre muebles/suelo/pared. No resolver una obstrucción moviendo sólo la cámara. Deben documentarse poses que cambien y cualquier diferencia de exposición, sin atribuir todos los píxeles al catálogo.

Quedan fuera del dictamen la calidad estética final, uso real de acciones, navegación viva, evaluación formal, gates 200/81, integración fuente/paquete, rendimiento y publicación. No se afirma 4/5.
