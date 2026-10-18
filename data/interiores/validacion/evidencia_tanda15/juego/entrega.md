# Infantil Bv3: banco de lectura y huella de juego

Candidata terminada en CPU, pendiente de la revisión independiente del render. El autor sólo ha escrito la copia privada; raíz comunicó después su integración local y capturas. Sin GPU, publicación ni aprobación visual por el autor.

## Entrega

Tres deltas separados, sin compilados para copiar sobre raíz:

- `motor.patch`: `a88e141f77e12dfae700ece9242ccfdd1fc7fe7c2fb0e1c8f6fa7845116e359e`.
- `modelos.patch`: `ac0b1d112a806f97cafc0ebec59de49c4903bc2fa72653059e0c9bbcfeadd5d9`.
- `contratos.patch`, dos callbacks nuevos con `tanda>=18`: `0d67f92a95bcee0d841dca4adf5f2f9b000c7701474924da8651919d2f3bc45d`.

Base: Bv2 local congelada por hashes, HEAD `05d95051d1dfbd13a66b7f647a9783d985ca04b2` no describe por sí solo sus cambios locales. El delta de modelos sólo añade la alfombra compacta y banco propios, y cambia la receta infantil. Todos los modelos previos permanecen idénticos. No se incluyen houses, acabados, texturas ni cámaras.

## Función y geometría

Banco de 0,90×0,32 m, asiento a 0,40 m y dos cajas textiles de guardado bajo. Ocho piezas, rol `sillon` y asiento real de vida doméstica; sin superficies para añadir miniaturas. Se intenta frente a la pared de libros, centrado, sin filtro de área ni fallback a otra pared. Sólo permanece si cabe con su frente de 0,70×0,55 m y los usos existentes.

`separacion_pared=.14` sustituye la holgura habitual de .01 m. La cortina baja a .175 m y llega hasta .09 m hacia el interior: no basta la reserva de ventana desde .92 m. El opt-in se limita a contra_pared/enfrente individual; rechaza grupos u otras reglas. Default y RNG de no optantes conservados.

Alfombra compacta 1,20×0,85 m para área menor de12 m²; la grande 1,80×1,30 desde12 m². `area_max` es exclusivo en el motor real: frontera12 y ambos lados comprobados, una sola entrada activa. La textura de circuito ya existente es propia y se conserva. Primero se coloca la huella; el banco opcional no puede impedirla y forzar un reintento.

## Resultado CPU

- **31 casas/31 estancias reales +81 kits: cero errores.** Cama, mesita, mesa, silla, biblioteca y armario conservan exactamente sus poses en las31 reales. Las dos baldas siguen ocupadas.
- Alfombra libre de muebles en112/112; banco en24/31 reales y59/81 sintéticas. Entra en4007,5045 y1296, sin cambios de principales. La huella libre es1,02 m² en las dos estrechas y2,34 m² en1296.
- En las24 casas con banco, `pieces.seat` lo registra y su punto frontal admite cuerpo de radio.34. Accesos completos y ciclo hide/unhide exacto radio.34 pasan en31/31.
- Agrupación de mallas real: **máximo60 mallas,63.264 triángulos y8 luces**. Mallas, materiales y luces no aumentan en ninguna de31 casas. Los triángulos cambian entre−134 y+1.180 por banco/alfombra y decoración incidental del RNG; no se atribuye una medida de tiempo GPU.
- Separación de cortina: el prototipo sin separador produce RED en3072,4848,5144,6291 y8030; la receta final pasa en todas. La primera factibilidad, antes de priorizar alfombra, tenía6 conflictos. Son candidatos privados, nunca defectos atribuidos al juego publicado.
- Negativos de asiento flotante y caja interpenetrada detectados. Defaults+P+extracción U siguiente coinciden en81 semillas no optantes. El borde provisional erróneo12−1e−6 y los recibos previos se conservan en `historico/`.

El layout usa la Bv2 fijada sin acabados. **El coste completo compara Bv2+contraste contemporáneo de raíz frente a Bv3+el mismo contraste**: houses `20336003f922f667b29e2b7eb349fe720bd2d9dcb3aa6e5bdfe23043a3491706` y acabado `5c65b324b83ffed145793b01bb5635b85b31f6b71c232f32879f42f48adc71e9`. Ambos se leen una sola vez en memoria y se cotejan al terminar; no se copian ni editan. Los recibos `cpu_layout.json`, `cpu_full.json`, `cpu_detalles.json` y `cpu_contratos.json` contienen alcance y evidencia; `entrega.json` sella hashes.

## Límites

Tres kits sintéticos29/51/63 cambian de intento al exigir juego real; no se fuerza un orden por semilla. Decoración y luminarias opcionales pueden cambiar por consumo incidental del RNG. No se rediseña iluminación.

El banco se omite donde no cabe; no se cambia el amueblado para una cámara. Relación frontal y acceso geométricos no certifican lectura visual. El Canvas de CPU no rasteriza textura/atlas: la legibilidad de la alfombra y la composición completa requieren las capturas nuevas y otro revisor. No hay nota formal, comparación de FPS, CI ni publicación acreditadas por esta entrega.
