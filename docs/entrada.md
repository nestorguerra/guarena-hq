# La entrada al juego: sin menús, desde 388 Pueblos

Lo pidió el usuario el 12 de octubre de 2026: «que no tengas un menú de inicio, sino que cargues directamente entrando
en el personaje de Annie, en la puerta de su casa», en Plastilina, con un zoom «muy smooth» que empiece en la web de
388 Pueblos (https://pueblos388.onrender.com/): se elige Extremadura, Guareña, *Jugar en Guareña*, y la cámara baja
despacio hasta el pueblo, se queda un rato quieta mientras el juego carga «sin que el jugador se dé cuenta», y sigue
bajando hasta Annie. Los ajustes, con X; en ellos, *Volver a la página web*. El formulario de la lista de espera ya no
corta la entrada (sigue en la portada de la web).

Después, el mismo día: «mientras está cargando se queda estático en una imagen de Guareña… que estuviera haciendo un
zoom, aunque fuera lento, cada vez más cercano hacia la posición donde va a arrancar el juego», sincronizado con lo que
tarda en cargar. Ahora el zoom no se para nunca: de la cámara de la web a la foto, durante toda la carga, y de la foto
a la cámara del juego.

## Cómo se entra

1. **La foto del dron.** `index.html` pone al instante, a toda pantalla, `assets/intro.jpg` (Plastilina) o
   `assets/intro_real.jpg` (Realista): Guareña pintada por el propio juego desde un dron, a 150 m, mirando por
   encima de los tejados hacia la torre de Santa María. Se va acercando mientras carga el pueblo (ver *El zoom de
   la carga*); a mitad de camino la releva, fundida, `assets/intro_cerca.jpg` (o `intro_real_cerca.jpg`): la misma
   vista con el objetivo cerrado 1,8 veces, pintada nítida, para que el zoom no se emborrone.
2. **Detrás, el juego.** `main.js` arranca la partida con Annie en su puerta (`src/intro.js`: `protagonist`, que es
   Annie salvo que se haya cambiado de personaje desde los ajustes) y construye entera su calle y alrededores
   (`buildAround`), para que nada aparezca durante la bajada.
3. **El relevo.** La cámara del juego se pone exactamente como se ve la foto en ese instante: en el dron, con el
   objetivo cerrado s veces (la foto crece desde su centro; acercar la cámara movería los tejados cercanos contra los
   lejanos y las dos imágenes no casarían en el fundido). Antes, detrás de la foto, unos fotogramas de calentamiento
   (el tráfico y los vecinos echan a andar, los shaders se compilan) y el sonido se despierta: lo que cuesta, que no
   caiga en los primeros fotogramas del vuelo. La foto se funde con la vista en vivo **sin dejar de acercarse**, a la
   velocidad que llevaba (`guarenaZoom.handover`), y el objetivo de la cámara en vivo hace exactamente el mismo zoom
   mientras dura el fundido (1,1 s); luego ese zoom se apaga a la vez que el vuelo arranca (`ZOOM` en
   `src/intro.js`).
4. **El vuelo** (`IntroFlight`, 9 s): por dos puntos sobre el centro de su calle, primero alto por encima de los
   tejados y luego entre las casas por debajo de los aleros, hasta la cámara de juego detrás de Annie. Mientras
   tanto el pueblo vive (coches, vecinos, el viento), el detalle se mantiene alrededor de su puerta (`introFocus`),
   el tiempo es el de la foto (mañana despejada: el real llega después, poco a poco) y el plano cercano de la cámara
   crece con la altura, para que las capas del suelo no parpadeen vistas desde lejos.
5. **Al aterrizar** aparece el HUD con un fundido y la ayuda de bienvenida (con X para los ajustes).

## El zoom de la carga

`index.html` (`guarenaZoom`) acerca la foto desde 1 hasta `MAX` = 2,6 (la calle de Annie de cerca) y procura llegar
justo cuando acabe la carga:

- **Cuánto tardará.** Al principio, lo que tardó la última vez en este aparato (`localStorage`:
  `guarena_hq_carga_388` dentro de 388 Pueblos, `guarena_hq_carga` fuera; si no hay, 12 s y 18 s). Según avanza, la
  carga dice por dónde va (`main.js`: `guarenaZoom.to`) y se corrige: `CURVE` dice qué parte del tiempo ha pasado
  cuando la carga dice que va por tal punto (medido: las calles y las casas se llevan casi todo el tiempo, los últimos
  pasos son rápidos).
- **La velocidad, sin tirones.** Cada corrección cambia la velocidad poco a poco (1,5 s); en los dos últimos segundos
  previstos ya no se corrige: mejor quedarse algo corto o pasarse de `MAX` que frenar para clavarlo, porque frenar se
  lee como pararse. Si la carga se alarga, el zoom sigue, cada vez más despacio, sin pararse nunca (hasta `CAP` = 3,6).
- **Una sola animación.** Las dos fotos van en una caja (`#introZoom`) que acerca una única animación (Web Animations,
  logarítmica de 1 a `CAP`) que corre en el hilo de la pantalla, haga lo que haga la página. Las correcciones solo
  cambian su velocidad, y dónde va el zoom se lleva con el reloj (`M`), poniendo a juego el inicio de la animación.
  Así se aprendió, midiéndolo fotograma a fotograma:
  - una transición CSS relanzada cada poco se acababa en mitad de los pasos largos de la construcción (hasta 2 s sin
    que la página pueda hacer nada) y la foto se quedaba quieta y luego daba un salto atrás;
  - el reloj de animaciones de la página no avanza durante un paso largo, y justo después sigue atrasado uno o dos
    fotogramas (también dentro de `requestAnimationFrame`): leer de él dónde va la animación, o cambiarle la velocidad
    con `updatePlaybackRate` en ese momento, la hacía saltar atrás un poco.

Medido en Chrome (Mac), entrando desde la web: la foto se acerca sin pausas a ≈0,075 por segundo (logarítmico) de
principio a fin de la carga, y el relevo a la cámara en vivo no cambia la velocidad.

## Desde 388 Pueblos

La web (repositorio `nestorguerra/388-pueblos`, `web/js/jugar.js`) carga el juego en un iframe
(`?estilo=plastilina&desde=388`) y los dos se hablan con mensajes:

| Mensaje | De → a | Qué quiere decir |
|---|---|---|
| `guarena:ready {rate}` | juego → web | la foto está puesta; `rate`: la velocidad con que arrancará su zoom (logarítmica, por segundo) |
| `guarena:zoom {s, r, t, hold}` | web → juego | empieza el fundido: la cámara de la web va por el zoom `s` y crece e^`r` veces por segundo (en el instante `t` de su reloj); la foto se pone ahí y sigue igual durante `hold` s |
| `guarena:go {t}` | web → juego | la web ya se ha fundido con la foto: que se construya el pueblo |
| `guarena:shown` | web → juego | ya se ve el juego: el vuelo puede empezar cuando esté listo |
| `guarena:picture`, `guarena:live`, `guarena:play` | juego → web | la foto se acerca; empieza el vuelo; se está jugando |
| `guarena:salir` | juego → web | *Volver a la página web*: la web cierra el juego y recupera su cámara |

El orden importa: mientras la cámara de la web baja (4,2 s), el juego solo descarga y **no construye nada**. Ese
trabajo pesado congela la cámara de la web, porque en muchos navegadores los dos comparten proceso: en las pruebas se
paraba 15 s y luego saltaba. En la segunda mitad de la bajada la maqueta de la web se calienta con un filtro CSS hacia
los colores de la foto (color medio 193, 133, 88 frente a 194, 126, 88), y el fundido junta dos imágenes que ya se
parecen.

La cámara de la web tampoco se para en el dron: mientras frena al llegar, su objetivo empieza a cerrarse, y llega ya
con el zoom a la velocidad que el juego anunció en `ready`. Al empezar el fundido le dice a la foto dónde va (`zoom`):
las dos hacen el mismo zoom mientras se funden, y después la foto sigue con el de la carga. Por eso hay que publicar
**primero el juego y después la web**: una web nueva con un juego viejo haría el fundido con la foto quieta.

Fuera de la web (abriendo el juego directamente) todo es igual, sin esperas.

## Volver a pintar las fotos

Si cambia el pueblo alrededor de la calle Malfeitos, o el aspecto, se pintan otra vez desde el juego (servidor local,
`?estilo=plastilina` o `?estilo=real`):

```js
const I = await import('/tools/intro.js?' + Date.now()); await I.paint()
```

Guarda `.snaps/intro.jpg` o `.snaps/intro_real.jpg`; se copian a `assets/` (JPEG progresivo, calidad 82). La foto
cercana, con `await I.paint({ cerca: 1.8 })` (`…_cerca.jpg`). Las cuatro van fuera del HTML empaquetado
(`tools/build.py`, `LAZY`). El encuadre
del dron está fijado en `src/intro.js` (`VIEW`): es el mismo que conoce la web (`DRONE` y `TARGET` en su `jugar.js`).
Si se cambia, hay que cambiarlo en los dos sitios.

## Pruebas

En Chrome sin ventana y sin sonido, con el juego en el 8920 y la web en el 8388:
- el juego solo: `http://localhost:8920/index.html?estilo=plastilina`;
- desde la web: `http://localhost:8388/guarena.html?jugar&juego=http://localhost:8920/index.html` (el parámetro
  `juego` solo se acepta en localhost).

Para ver si el zoom se para, lo que vale es grabarlo como lo pinta la pantalla (`Page.startScreencast` del protocolo
de DevTools, con la hora de cada fotograma de su `metadata.timestamp`) y medir, entre fotogramas, la escala que pone
uno encima del otro: así salen las pausas, los saltos atrás y los cambios de velocidad. La pestaña de la app, sin
foco, da un fotograma cada 2 s: ahí no se puede juzgar.
