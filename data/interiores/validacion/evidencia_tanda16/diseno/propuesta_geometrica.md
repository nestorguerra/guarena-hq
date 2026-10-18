# Cocina T16 — propuesta geométrica privada

**Es viable recomponer guardado–preparación–cocción sin mover mesa, sillas ni núcleo funcional en las tres canónicas.** Se propone una alacena mayormente cerrada con un hueco diario, alto continuo sobre preparación/nevera y una actividad clara en preparación. Sólo hay volúmenes conservadores CPU: no modelos finales, receta activa, solver, acabados ni GPU.

## Medidas y programa

La ficha redondea la envolvente que incluye muros. El constructor amuebla el recinto útil, descontando .15 m en cada dimensión:

| Casa | Ficha | Útil CPU | Propuesta que cabe |
|---|---|---|---|
|2786|3,6×2,9 m|3,413×2,703 m;9,23 m²|Mantener huella lateral de alacena .65×.30; no cabe extender al extremo sin cortar lavadora/límite. Alto de1,23 m sobre preparar+nevera.|
|3244|5,6×4,2 m|5,469×4,029 m;22,03 m²|Alacena .90×.35 al extremo de nevera; alto de1,538 m sobre preparar+nevera.|
|1594|4,5×4,3 m|4,361×4,180 m;18,23 m²|Alacena compacta .65×.30 al extremo de nevera; .90 m sale del recinto. Alto de1,538 m.|

Alacena hasta2,26 m; sólo un hueco de uso diario, resto cerrado. Banda alta de .30 m de fondo/.64 de alto, desde1,62 hasta2,26 m: deja .07 m sobre la nevera y termina antes de invadir campana/fuego. Una actividad de .35×.23 m sobre encimera a .89 m (tabla/pan como intención, no un modelo final). Se conservan madera/bastidores rústicos y puertas lisas o hueco de vajilla según variante; no se añade otra fila de altos ni más provisiones expuestas.

La alacena actual busca junto a cocina/preparación, pero esa lista excluye la nevera. Eso explica su dispersión lateral en1594 pese al hueco disponible al final del frente. La sonda prueba un extremo ancho, después compacto, después la huella actual; si falla todo, conserva exactamente la base. No usa semillas/cámaras para decidir ni busca otra distribución de mesa.

## Cobertura CPU real

El inventario disponible contiene **22 semillas públicas, no31**. Se reutilizan sólo sus identidades y se reconstruye todo desde las fuentes actuales Bv3+contraste selladas por hashes, sin notas ni resultados numéricos históricos. No se copia `src/interiores_datos.js`; el catálogo se lee de JSON en memoria.

En22 cocinas:18 admiten la propuesta (7 extremo ancho,5 extremo compacto,6 huella actual);4 conservan la base exacta (3627, 2606, 4007, 4216). Se prueban colisiones de volúmenes contra piezas reales, huecos, límites, reserva frontal y mapa de paso .80 m. El primer oráculo de mesa por un punto frontal genérico producía falsos rechazos; se conserva ese recibo como histórico y se sustituye por mesa/sillas inmóviles más el validador real de uso con sus puestos.

Montaje completo con constructor/agrupación reales, Canvas sin rasterizar: **22/22 sin errores de uso/local, máximo59 mallas**. Mallas canónicas54/56/58, sin aumento de materiales ni luces. Mesa, sillas, cocina/fregadero/fuego/campana, preparación, nevera y lavadora conservan sus poses. Los cuatro fallbacks también conservan métricas geométricas exactas. Este coste corresponde a cajas conservadoras; los modelos finales deben repetir la comprobación ≤60 y no añadir materiales exclusivos.

## Entrega y límites

- `geometria_r1/esquema.svg`: plantas propias antes/propuesta, a escala por casa.
- `dimensiones.json`, `factibilidad.json`, `volumen_full.json`: medidas, cada rechazo y resultado.
- `propuesta.mjs`: sonda privada sobre la planta ya amueblada; **no es una receta de producción ni un solver propuesto para integrar**.
- `base.json` y `manifest.json`: procedencia y hashes.

Fuentes raíz selladas: locales `6a86a62488f1d3162387c32414bd7c244b321f0d85658507ecf9cddbbf10dad3`, houses `20336003f922f667b29e2b7eb349fe720bd2d9dcb3aa6e5bdfe23043a3491706`, acabados `5c65b324b83ffed145793b01bb5635b85b31f6b71c232f32879f42f48adc71e9`; cocinaJSON `8231d11513e52e3a29a29e55eaf23f3a85652fb52a0ac6b8a6017b2ad854bb2e`. Todos se cotejan antes/después de CPU. Base Bv3+contraste real, no HEAD05 histórico.

Las cajas opacas incluyen conservadoramente la futura cavidad del armario; no demuestran puertas, apoyo de vajilla ni legibilidad de tabla/pan. El hueco diario todavía es diseño, no geometría final. No hay prueba de píxeles, luz, coste GPU o calidad formal. Las cámaras actuales recortan alto/comedor; este estudio no las mueve ni certifica cobertura. La eventual implementación debe aprovechar la cadena existente hasta4 miembros y conservar fallback; el anclaje de la banda sobre dos referencias requiere especificación mínima posterior, no queda resuelto por esta sonda.

Se cierra esta fase como propuesta geométrica acotada y se pausa para priorizar la corrección del laboratorio infantil T15, por instrucción de raíz.
