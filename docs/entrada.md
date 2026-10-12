# La entrada al juego: sin menús, desde 388 Pueblos

Lo pidió el usuario el 12 de octubre de 2026: «que no tengas un menú de inicio, sino que cargues directamente entrando
en el personaje de Annie, en la puerta de su casa», en Plastilina, con un zoom «muy smooth» que empiece en la web de
388 Pueblos (https://pueblos388.onrender.com/): se elige Extremadura, Guareña, *Jugar en Guareña*, y la cámara baja
despacio hasta el pueblo, se queda un rato quieta mientras el juego carga «sin que el jugador se dé cuenta», y sigue
bajando hasta Annie. Los ajustes, con X; en ellos, *Volver a la página web*. El formulario de la lista de espera ya no
corta la entrada (sigue en la portada de la web).

## Cómo se entra

1. **La foto del dron.** `index.html` pone al instante, a toda pantalla, `assets/intro.jpg` (Plastilina) o
   `assets/intro_real.jpg` (Realista): Guareña pintada por el propio juego desde un dron, a 150 m, mirando por
   encima de los tejados hacia la torre de Santa María. Se va acercando con una transición CSS (26 s, hasta 1,34×),
   que sigue suave aunque la página esté ocupada construyendo el pueblo.
2. **Detrás, el juego.** `main.js` arranca la partida con Annie en su puerta (`src/intro.js`: `protagonist`, que es
   Annie salvo que se haya cambiado de personaje desde los ajustes) y construye entera su calle y alrededores
   (`buildAround`), para que nada aparezca durante la bajada.
3. **El relevo.** La cámara del juego se pone exactamente como se ve la foto en ese instante: en el dron, con el
   objetivo cerrado s veces (la foto crece desde su centro; acercar la cámara movería los tejados cercanos contra los
   lejanos y las dos imágenes no casarían en el fundido). La foto se funde con la vista en vivo.
4. **El vuelo** (`IntroFlight`, 9 s): por dos puntos sobre el centro de su calle, primero alto por encima de los
   tejados y luego entre las casas por debajo de los aleros, hasta la cámara de juego detrás de Annie. Mientras
   tanto el pueblo vive (coches, vecinos, el viento), el detalle se mantiene alrededor de su puerta (`introFocus`),
   el tiempo es el de la foto (mañana despejada: el real llega después, poco a poco) y el plano cercano de la cámara
   crece con la altura, para que las capas del suelo no parpadeen vistas desde lejos.
5. **Al aterrizar** aparece el HUD con un fundido y la ayuda de bienvenida (con X para los ajustes).

## Desde 388 Pueblos

La web (repositorio `nestorguerra/388-pueblos`, `web/js/jugar.js`) carga el juego en un iframe
(`?estilo=plastilina&desde=388`) y los dos se hablan con mensajes:

| Mensaje | De → a | Qué quiere decir |
|---|---|---|
| `guarena:ready` | juego → web | la foto está puesta y quieta |
| `guarena:go {t}` | web → juego | la web ya se ha fundido con la foto: que empiece a acercarse (desde `t`) y que se construya el pueblo |
| `guarena:shown` | web → juego | ya se ve el juego: el vuelo puede empezar cuando esté listo |
| `guarena:picture`, `guarena:live`, `guarena:play` | juego → web | la foto se acerca; empieza el vuelo; se está jugando |
| `guarena:salir` | juego → web | *Volver a la página web*: la web cierra el juego y recupera su cámara |

El orden importa: mientras la cámara de la web baja (4,2 s), el juego solo descarga y **no construye nada**. Ese
trabajo pesado congela la cámara de la web, porque en muchos navegadores los dos comparten proceso: en las pruebas se
paraba 15 s y luego saltaba. En la segunda mitad de la bajada la maqueta de la web se calienta con un filtro CSS hacia
los colores de la foto (color medio 193, 133, 88 frente a 194, 126, 88), y el fundido junta dos imágenes que ya se
parecen.

Fuera de la web (abriendo el juego directamente) todo es igual, sin esperas.

## Volver a pintar las fotos

Si cambia el pueblo alrededor de la calle Malfeitos, o el aspecto, se pintan otra vez desde el juego (servidor local,
`?estilo=plastilina` o `?estilo=real`):

```js
const I = await import('/tools/intro.js?' + Date.now()); await I.paint()
```

Guarda `.snaps/intro.jpg` o `.snaps/intro_real.jpg`; se copian a `assets/` (JPEG progresivo, calidad 82). El encuadre
del dron está fijado en `src/intro.js` (`VIEW`): es el mismo que conoce la web (`DRONE` y `TARGET` en su `jugar.js`).
Si se cambia, hay que cambiarlo en los dos sitios.

## Pruebas

En Chrome sin ventana y sin sonido, con el juego en el 8920 y la web en el 8388:
- el juego solo: `http://localhost:8920/index.html?estilo=plastilina`;
- desde la web: `http://localhost:8388/guarena.html?juego=http://localhost:8920/index.html` (el parámetro `juego`
  solo se acepta en localhost).
