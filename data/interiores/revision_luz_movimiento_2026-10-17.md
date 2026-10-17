# Revisión independiente de movimiento y luz doméstica

17 de octubre de 2026. Revisor 2. Sin notas ni aprobación formal.

## Estado

**El salto inicial quedó reproducido y ya no aparece de forma notable en el mismo recorrido con el código corregido.** Se conserva evidencia de ambas versiones. También se cruzó la nueva bisectriz entre focos y no se observa un cambio brusco de brillo o una sombra que salte. Esta conclusión se limita a la muestra descrita; no constituye aprobación formal de la tanda.

## Evidencia inicial

Chrome 155.0.8059.80 existente, puerto 9333, headless y con `--mute-audio`. Servidor local 8920. Tab propio `FA8AA5A8CAA4B9BBEF8C776035B215F9` en contexto privado. Fixture ficticia; no se usa la partida real. Se esperó el contrato `LISTO` de `tools/interiores/integracion.py` antes de entrar.

Casa de vecino, semilla 2786, origen (-5200, -5200), planta 0. Paso entre pasillo y dormitorio L1. El umbral compartido es x=-5200.70325267618. Cámara a altura y=1.6, z=-5193.53469443867, mirando a -X, cuaternión [0, 0.7071067811865475, 0, 0.7071067811865476], FOV 65, imagen 960×540, `?estilo=real`, sombras activas. Hora congelada en 12.531402222222555, exposición 0.68. Se congelaron avance del juego y render automático dentro del Tab de ensayo; las dos imágenes se dibujaron con `game.renderView` y la misma orientación.

| Posición | x | Luz pasillo | Luz dormitorio | Foco con sombra |
|---|---:|---:|---:|---|
| Antes, pasillo | -5200.69325267618 | 10.578875349415465 | 0.6101030658940515 | Pasillo |
| Después, dormitorio | -5200.71325267618 | 0.8463100279532373 | 7.626288323675643 | Dormitorio |

Capturas: `data/interiores/validacion/imagenes/713eed5812a075cf2e2e257a2f51fbc81b2aec3240f3169bb038de82ce62f54c.jpg` y `data/interiores/validacion/imagenes/1d374802153e749d9a595386f1eb9761b6a3cbd08cad53c30e5d464d3093464e.jpg`. Registro completo: `data/interiores/validacion/luz_movimiento_inicial.json`, con SHA256 de ambas imágenes, muestras de todas las luces y coordenadas de las salas. Las capturas se inspeccionaron con `view_image`.

La imagen inicial es visiblemente más oscura. La media de gris de toda la imagen pasa de 50.17 a 83.51 (escala 0–255). Un parche estable [80,135,650,440] pasa de 60.40 a 102.18. Es una comprobación de píxeles renderizados, no una medida física ni una puntuación de calidad. El mínimo desplazamiento cambia ligeramente la proyección; la diferencia amplia de brillo no se explica por ese cambio de encuadre.

El código inicial escogía el foco por pertenencia estricta de la cámara a la sala y reducía los demás al 8 %. El cambio de sala alteraba de golpe las intensidades y el foco de sombra. `renderView` restauraba los valores tras cada vista; esa restauración no evitaba la discontinuidad entre posiciones.

## Límites

Prueba breve de una puerta de una casa y una estética. No cubre todas las semillas, apagones, plantas, ventanas exteriores ni todas las animaciones. El recorrido se muestreó con la cámara en posiciones controladas; no es una grabación continua del controlador de caminar. La conclusión se limita a la iluminación observada en esas posiciones.

## Repetición del candidato corregido

Se recargó exclusivamente el Tab propio, con caché ignorada, y se volvió a esperar `LISTO`. Se entró de nuevo en la casa 2786 con las mismas siete luces base, posición, orientación, FOV, resolución, hora, exposición y sombras. Se repitieron las coordenadas exactas del ensayo inicial con `game.renderView`.

| Par corregido | Luz pasillo, antes→después | Luz dormitorio, antes→después | Resultado visible |
|---|---:|---:|---|
| Umbral original a ±1 cm | 10.578875→10.578875 | 7.425068→7.450465 | Sin salto notable |
| Bisectriz a ±1 cm | 10.578875→10.578525 | 7.626037→7.626288 | Sin salto notable |

El nuevo foco más cercano cambia en x=-5200.986105473942, con y=1.6 y z=-5193.53469443867. Se capturó antes en x=-5200.976105473942 y después en x=-5200.996105473942. El foco con sombra cambia de pasillo a dormitorio; su `shadow.intensity` vale 0.000631129 y 0.000633027 a ambos lados. La sombra queda prácticamente desvanecida al cambiar de origen. El cambio observado entre las imágenes es el encuadre esperado al avanzar 2 cm.

Capturas inspeccionadas con `view_image`:

- `data/interiores/validacion/imagenes/84f3bab3b630e525edb510ab0c345848ab56b7047cb75960b845985f328f2df4.jpg`
- `data/interiores/validacion/imagenes/2459d2d8dd16413b3ec545f581a7919af8d6c11775483fad075b457fdc584294.jpg`
- `data/interiores/validacion/imagenes/67b66517017ad6ca0b97f87fcb04100f4ef48c3d79d0498c61611b241d59924a.jpg`
- `data/interiores/validacion/imagenes/1c05ece02004852cc426d0640a2253a20af675eedf634cdf371d7ac522b0c6cd.jpg`

La media de gris de la pareja del umbral pasa de 93.66 a 94.14; el mismo parche estable pasa de 113.92 a 114.35. En la bisectriz el parche pasa de 117.21 a 117.07. Las diferencias absolutas de píxeles incluyen desplazamiento de contornos y compresión JPEG; no se usan como puntuación. La gran variación de brillo del candidato inicial desaparece en la comparación visual.

Las cuatro preparaciones restauraron exactamente intensidad, `castShadow` y `shadow.intensity` a sus valores anteriores. La instrumentación de errores no registró errores JavaScript. El código corregido calcula intensidades por diferencia continua de distancias y desvanece la sombra cerca de la bisectriz; `renderView` mantiene la restauración en `finally`.

Registro completo: `data/interiores/validacion/luz_movimiento_corregido.json`. Copia de la fuente leída y su hash: `.cache/calidad_tanda4_fuente_corregida.json`, SHA256 `b433e6a03f6f208c2a3bd070c6c188269f1d386991af9ff2f51a418194f30d6f`.

## Cierre y alcance

Se cerró únicamente el Tab propio `FA8AA5A8CAA4B9BBEF8C776035B215F9` y se eliminó su contexto privado de ensayo. Se releyó el inventario y el Tab propio ya no existe. Hubo cambios simultáneos en otros identificadores entre inventarios, por lo que esta comparación no permite certificar la persistencia de todos los Tab ajenos. Las únicas órdenes de cierre de esta revisión apuntaron al identificador propio y al contexto privado creado por este mismo cliente; no se emitieron órdenes de control o cierre sobre identificadores ajenos. Registro: `.cache/calidad_tanda4_cierre_tab.json`.

No se ha modificado código ni datos del juego en esta revisión. Se han escrito solo el cliente temporal, capturas y metadatos de ensayo. No se han usado partidas reales ni se ha publicado. Quedan fuera de esta comprobación otras puertas, semillas, la casa de Annie, otras estéticas y los cambios de planta o de estado de suministro. El resultado cierra el defecto reproducido en esta muestra; no certifica esas combinaciones.
