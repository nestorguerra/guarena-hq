# Viviendas y Annie: revisión del 17-10-2026

Estado: revisión técnica y visual realizada; objetivo formal de calidad no superado. El usuario ha solicitado expresamente commit, push y publicación de esta versión de prueba. La publicación se verifica por separado en GitHub Actions y en la página servida. Esta nota sustituye el estado anterior que dejaba Annie aplazada y prohibía publicar.

## Resultado del cambio

Las 22 casas de vecinos tienen 132 habitaciones habitables por kit. Se añaden 15 kits al salón existente. Annie conserva su plano singular, escalera, patio, dormitorio personalizado, gato, tocador, caja fuerte y las claves de guardado; salón, cocina, ambos baños y estudio usan cinco kits. El inventario distingue cinco habitaciones por kit y una personalizada, sin atribuir seis kits a Annie.

Se corrigen el color demasiado oscuro del catálogo, la caché de cuadros que repetía dibujos, los carteles y lienzos, las lámparas según uso, el teclado del piano, las cornamentas y la falda de la camilla. Las cocinas grandes incluyen mesa; el cuarto joven tiene TV apoyada y sofá enfrente; despensa y trastero tienen más dotación proporcional. Los baños restringen sus enseres a higiene. Los lotes estáticos conservan las piezas móviles y las lámparas controlables.

## Código y función

Dos revisiones de código en momentos distintos detectaron el rechazo de cuadros legítimos en hall/pasillo, la lectura de profile ausente en Annie y la bandera de lámpara de los lotes. Se corrigieron y se verificaron. Los contratos finales son 20 y pasan todos, incluyendo acceso a las funciones de Annie por sus colliders en ambas plantas, mesa/TV/sofá, conversión de color y variación de cuadros.

Los ensayos estrictos cubren 200 casas sintéticas con 1166 habitaciones y las 22 casas reales con 132 habitaciones. Cada uno de los 16 kits de vivienda pasa 81 distribuciones: 1296 ensayos, sin errores ni avisos. No se elevan presupuestos: máximos sintéticos de 41886 triángulos, 59 mallas, nueve luces y 143,5 ms de montaje en el equipo y condiciones registrados. Los 21 archivos derivados se regeneran idénticos.

La integración del juego comprueba entrada en ocho casas, tres planos y ambas plantas, además de Annie. Una partida ficticia privada comprueba dinero, caja fuerte, decoración de planta alta, depósito/retirada, siesta y recarga; conserva los testigos de las otras dos versiones del juego. Se registran 64 recorridos acotados de vecinos y 32 de Annie, sin túneles ni escapes. El informe del paquete comprueba también bar, cafetería y farmacia después del cambio global de color.

Las métricas y errores concretos se conservan en [resumen técnico](validacion/resumen_viviendas.json), [integración fuente](validacion/integracion_juego.json) e [integración del paquete](validacion/integracion_paquete.json). Un ensayo fallido durante la preparación comercial omitía shopRef en su puerta ficticia; se corrigió el instrumento para usar el mismo contrato que la entrada real.

## Imagen y evaluación formal

Dos revisores independientes inspeccionan 19 JPG y sus JSON: 18 fichas de vecinos, incluida una variante de dormitorio con la segunda estética, y Annie. Sus informes conservan los hallazgos iniciales y el cierre posterior. Pintura 3244 ya muestra el lienzo sobre caballete; joven 1851 ya muestra sofá y TV enfrentados. No queda un defecto importante observable pendiente en esas muestras.

- [Revisor 1](revision_visual_revisor1_2026-10-17.md).
- [Revisor 2](revision_visual_revisor2_2026-10-17.md).
- [Galería](fichas/viviendas.html).

Decision API de OpenAI añade dos peticiones independientes por ficha para los 16 kits y Annie: 34 evaluaciones finales. Cada petición usa capturas, referencias acreditadas y cinco dimensiones domésticas. Las medias van de 2,658 a 3,246; ninguna supera el objetivo de media ≥ 4 y ninguna dimensión < 3. Las peticiones A/B usan el mismo modelo y no equivalen a diversidad de modelos. Se conservan respuestas, rúbrica, request id y hashes, además de las rondas anteriores. No se repite una puntuación por ser desfavorable.

[Resumen formal](validacion/resumen_revision_visual.json). Las notas son evaluaciones, no verificaciones de funcionamiento. La publicación autorizada no se presenta como aprobación de calidad artística ni como visto bueno del usuario sobre las imágenes.

## Menores y límites que se conservan

- Algunas habitaciones grandes mantienen suelo muy libre y mobiliario perimetral. Se puede mejorar composición, contraste de muebles claros, patrones antiguos, variedad de cornamentas y separación tonal de textiles. Los pliegues finos de la camilla no quedan suficientemente expuestos en las fichas para darlos por evaluados visualmente.
- Algunas puertas y objetos próximos a cámara tapan parte de una vista; las alternativas permiten identificar el uso. La segunda estética solo está muestreada en dos dormitorios; no se extiende esa cobertura a todas las salas.
- El índice geométrico de iluminación pondera intensidad respecto a 5,5; no mide lux. La revisión visible sigue siendo necesaria. El patio usa cielo y luminaria sin otra luz puntual.
- El montaje puede probar semillas derivadas deterministas cuando una composición bloquea el uso. La misma entrada conserva su resultado, aunque alguna distribución cambie respecto al despliegue anterior. Annie admite hasta 24 intentos por habitación.
- El botín sin superficie accesible puede colocarse junto a ella en suelo alcanzable, marcado como reubicado. Conserva identidad y cantidad, pero puede cambiar de posición.
- El rendimiento se mide sin otras escenas de ensayo compitiendo; no garantiza toda carga ni todo hardware. Un ensayo anterior con contención se conserva como fallo, sin subir el presupuesto.
- La persistencia usa un fixture reducido y ficticio, sin tocar partidas reales. No cubre toda partida antigua ni toda decoración posible. Las colisiones son 16 recorridos por planta a 60/20 fps de 0,35 s; no constituyen un barrido exhaustivo.
- Publicar esta versión de prueba deja pendiente alcanzar el objetivo artístico formal. El paquete depende también de recursos opcionales en assets; no se presenta como HTML totalmente autónomo.

## Publicación y recuperación

Destino: GitHub Pages de nestorguerra/guarena-hq, rama main. No se modifica 388 Pueblos en Render. El paquete incorpora guarena-revision; Actions y la página pública permiten verificar el commit servido. La base recuperable anterior es 339cbe13508e9996d855d9ac8f6276e6b98042e9.
