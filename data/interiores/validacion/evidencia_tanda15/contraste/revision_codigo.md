# Revisión independiente del contraste infantil B v2

Dictamen: **sin P1/P2 pendientes en cc5b244**. Aceptación técnica acotada para captura y comparación visual. No acredita mejora visual ni autoriza publicación.

Parche revisado: `cc5b2445555c1814d5cda804dca2d5ce53e7c9e338e85179e8c53add23d5a98e`.
Acabado: `5c65b324b83ffed145793b01bb5635b85b31f6b71c232f32879f42f48adc71e9`.
Caller houses candidato: `20336003f922f667b29e2b7eb349fe720bd2d9dcb3aa6e5bdfe23043a3491706`.

## Hallazgo cerrado

**P2, versión inicial, houses.js:1141–1143 / acabados_vivienda.js:47–49.** El acabado infantil se ejecutaba antes de amueblar y sin `estancia`; por tanto nunca encontraba la cama y todos los paños altos quedaban claros. Los contadores y la igualdad de poses no detectaban esa ausencia del resultado solicitado. La versión inicial y sus recibos quedan en `historico_v1`.

La corrección demora solamente el acabado infantil hasta después de `amueblarEstancia`, como ya ocurría con baño. Pasa la estancia recién añadida cuando el montaje devuelve éxito; si falla, pasa null y conserva el fallback claro. Los demás llamadores mantienen su orden y condiciones.

Lo comprobé con los constructores reales: 4007, 5045, 1296, 3405, 1555 y 4034 reciben una cama y emiten paños superiores profundos en **una única pared**, coherente con su orientación. 3405 selecciona norte; las otras cinco, sur. El hallazgo queda cerrado por resultado geométrico observado, no solamente por lectura del condicional.

## Evidencia independiente

`revision_dirigida.cpu.mjs` ejecutado sin GPU, salida `revision_dirigida.cpu.json`: PASS. Ocho casos sintéticos cubren las cuatro orientaciones en plantas 0 y 1. Cada pared contiene puerta y ventana; todos los rectángulos emitidos quedan fuera de los huecos y dentro de la altura de planta. Cada caso mantiene seis claves de materiales y una sola orientación superior profunda. Los seis constructores reales confirman el caller efectivo y el color asignado antes de agrupar.

El plano se coloca con el mismo inset y las mismas rotaciones interiores que el revestimiento inferior. La cota de planta es 3,1 m y las alturas usadas son 2,95/2,75 m. Puertas se recortan hasta 2,1 m; el recorte de ventana .92–2.08 engloba las ventanas ordinarias .95–2.05 y la posterior alta 1.1–1.9. La abertura especial del balcón frontal pertenece a A0: en el perfil familiar A0 consume `dorm` primero, por lo que no es una habitación infantil afectada por este cambio. No se ha generalizado aquí un nuevo contrato arquitectónico para otros perfiles.

El material profundo reutiliza la clave de la franja inferior; las demás paredes altas reutilizan la del techo. La función no consume azar adicional para los paños altos. La agrupación real ya utiliza esas claves, sin una familia material adicional por pared.

## Comparación del instrumento de raíz

Leí el instrumento completo y comprobé que los datos compilados y el motor de colocación de ANTES y DESPUÉS son iguales: ambos son B v2. ANTES usa `houses_base.js` y el acabado base; DESPUÉS usa el caller corregido y el acabado candidato. No compara biblioteca antigua frente a biblioteca nueva. En el momento de mi prueba, `houses_base.js` coincidía también con el archivo activo; esa precondición deja de cumplirse después de la aplicación local anunciada por raíz. Los snapshots privados permanecen como base reproducible.

El recibo de raíz `cpu_full.json`, SHA `ea18f96f3743a09a54ae7737aacfde92c2c09d61fd5d8f87e9020021d16dfad9`, compara las seis casas: mismas estancias, luces y número de mallas; conserva las comprobaciones de uso y salida de ocultación. Mallas: 57, 58, 60, 56, 59 y 60; luces: 8, 8, 8, 7, 8 y 8. Se añaden 12 triángulos en las dos primeras casas y 16 en las otras cuatro. No se repitió el barrido de 203 casas.

SHA de mi instrumento: `c750fbd2b28f63fd23bf60bf2061894126e61f0d2611d3b5d18483e750e14794`.
SHA de mi recibo: `5114ea353039eadbd76ef4c2d4169e2162de99647fb65c20e1843b40db0061b6`.

## Declined to judge

- Calidad visual, contraste percibido, sombras de los nuevos paños, fidelidad del raster y puntuación formal. Canvas es un doble y no se usó GPU.
- Presupuesto universal de todas las semillas; sólo los seis casos medidos sostienen el resultado de coste de esta revisión.
- Nueva zona de juego B v3, combinaciones futuras, acabados de otras tipologías, despliegue y validación integral.

No modifiqué fuentes activas ni ejecuté build, CI, navegador o publicación. La aplicación posterior anunciada por raíz no forma parte de las acciones de este revisor.
