# Los Backrooms bajo el teatro: Nivel 0, «The Lobby»

Estado: primera versión de prueba en la versión Evolución (9 de octubre de 2026). Lo pidió el usuario: un submundo
bajo tierra en Guareña, los Backrooms, «mundos de color crema, con salas infinitas una detrás de otra, con pasillos que
no llegan a ningún lado, los objetos repetidos y las estructuras distorsionadas algunas veces; geometrías raras,
liminales y difíciles de entender». Se entra como un *easter egg*: en el teatro, por una puerta. Para las pruebas, la
puerta se marca con un color distinto. Al menos diez salas, muy realistas, con muy buenas texturas, en Plastilina y en
Realista: el primer nivel, «The Lobby».

## Qué son

Una leyenda de internet. En 2019, un hilo de 4chan pedía «fotos inquietantes que parezcan raras» y alguien subió la
foto de una sala vacía:
- paredes amarillas;
- moqueta beige;
- falso techo con fluorescentes.

Debajo, otro escribió: «Si no tienes cuidado y te sales de la realidad por el sitio equivocado (*noclip*), acabarás en
los Backrooms: solo el olor a moqueta vieja y húmeda, la locura del amarillo uniforme, el ruido de fondo sin fin de
los fluorescentes al máximo zumbido, y unos 600 millones de millas cuadradas de salas vacías y segmentadas al azar».

En 2024 se supo de dónde era la foto: una tienda de muebles vacía de Oshkosh (Wisconsin), en obras en 2002. La wiki
que nació de la leyenda llama a esa primera planta **Level 0, «The Lobby»**: es el primer nivel, el que pidió el
usuario.

Lo que lo hace reconocible, sacado de la foto, la wiki y las películas (*The Backrooms* de Kane Parsons):
- papel pintado amarillo apagado, con un estampado de espigas en columnas, viejo y manchado;
- moqueta de bucle beige, húmeda, con cercos;
- falso techo de placas de fibra mineral de 60 cm en su perfilería blanca, con alguna placa manchada o que falta;
- fluorescentes empotrados de 60 × 120 cm, colocados «sin coherencia»: algunos fundidos y uno que parpadea;
- el zumbido constante de esos fluorescentes;
- tabiques sin sentido, salas sin ventanas ni muebles, pasillos que acaban contra una pared;
- la luz plana y amarillenta de una foto mal equilibrada.

## Cómo se entra

En la **Casa de la Cultura** (Teatro, Escuela Municipal de Teatro), por su puerta de la calle (*Entrar: Casa de la
Cultura*):
1. Cruza el patio de butacas y sube al escenario por las escaleras de los lados.
2. Al fondo, a la izquierda, hay una **puerta pintada de amarillo mostaza**. Bajo ella se cuela una raya de luz fría y,
   cerca, se oye el zumbido de unos fluorescentes que en el teatro no hay.
3. *Abrir la puerta amarilla*: un fundido largo, la estática y el golpe sordo de caerse de la realidad, y estás dentro.
   El cartel dice «Nivel 0 · «The Lobby» · los Backrooms».

Llegas mirando hacia dentro de la primera sala, con la puerta amarilla a la espalda. *Volver por la puerta amarilla*
te deja en el escenario, delante de la puerta. Desde el teatro se sale a la calle como siempre. Dentro se juega en
primera persona, como en las películas.

## El plano: salas que no se acaban

El nivel es un plano de **40 × 40 celdas de 1,2 m (48 m de lado)** que da la vuelta sobre sí mismo:
- Si sales por un lado, entras por el contrario: el juego te devuelve 48 m atrás sin que se note, porque allí están
  las mismas salas.
- Se dibuja nueve veces, en 3 × 3 alrededor del jugador. Se vea hacia donde se vea, hay salas.
- Una neblina amarillenta, el aire húmedo, tapa el borde a unos 50 m.
- Dos pasillos lo cruzan de lado a lado (J, de este a oeste; K, de norte a sur) y no se acaban nunca.
- Y, como en la leyenda, si andas mucho vuelves a pasar por las mismas salas.

24 espacios, cada uno con su letra en `src/backrooms.js`:

| | Qué tiene |
|---|---|
| **A** | Donde se llega, con la puerta amarilla. Desde ella se ve, por dos puertas seguidas, el salón de pilares. |
| **B** | Una sala en L que da al pasillo sin fin. |
| **C** | El salón de pilares: 27 × 14 m, tabiques sueltos. Uno de los pilares **no llega al suelo**: se queda a 30 cm. |
| **D** | Un pasillo de 17 m que acaba contra una pared. |
| **E** y **F** | **Las gemelas**: dos salas idénticas, la misma silla de oficina en el mismo sitio. Desde D se ven E, F y el salón de pilares, cuatro salas en fila. |
| **G** | **El pasillo que se estrecha**: dos paredes que se van cerrando de 2,4 m a 30 cm. |
| **H** | **El techo que baja**: cae de 2,74 a 2,18 m hacia el fondo; su puerta del sur queda a ras del techo. |
| **L** | **Una escalera que sube y se mete en el techo.** |
| **M** | **La sala oscura**: todos los tubos fundidos menos uno, que parpadea. |
| **N** | **El pasillo de los enchufes**: dos por cada 1,2 m de pared, una fila de enchufes que no acaba. |
| **O** | **Una puerta pequeña a media pared**, a 1,2 m del suelo. |
| **Q** | **El papel de lado**: el mismo papel, girado 90°. |
| **S** | Se ve **por una rendija** de 32 cm desde el pasillo T, pero no cabes. |
| **R**, **W** | Una **puerta que no se abre** («Ni siquiera gira el pomo. Al otro lado se oye el mismo zumbido.»). |
| T, U, V, Y, Z, I | Pasillos estrechos, salas con tabiques sueltos y más salas. |

Hay también **objetos repetidos**:
- la misma silla de oficina, siempre igual, en seis sitios;
- los mismos enchufes estadounidenses (los de la foto);
- las mismas manchas.

## La luz

Cada vértice de paredes, suelo y techo tiene su luz calculada al entrar (en 0,5 s; 0,8 s en Plastilina, que pinta más
texturas). Sale de los 236 fluorescentes del plano (217 encendidos, 16 fundidos y 3 que parpadean) y de los de sus ocho copias
vecinas:
- **directa**: cada tubo es un panel que alumbra hacia abajo. Se tienen en cuenta los cosenos y las sombras de los
  tabiques, que dejan pasar la luz por los huecos de las puertas por debajo del dintel. Cerca de un tubo se toman sus
  dos extremos, para que las sombras de las jambas salgan suaves;
- **rebotada**: más suave y por todas partes, por los mismos huecos. Es la única que llega al techo, más un brillo
  alrededor de cada tubo;
- **los rincones más oscuros**: el pie de las paredes, las esquinas y la línea del techo;
- **la suciedad de años**: polvo al pie de las paredes, amarilleo bajo el techo, manchas grandes y suaves, y la
  moqueta más oscura donde está mojada.

Dentro no hay sol ni cielo. La luz hemisférica del juego se pone blanca y a π, para que devuelva justo la luz
calculada: así, en Plastilina, las huellas y los relieves de la arcilla siguen viéndose. Los reflejos salen de una
sala amarilla pequeña, sin cielo azul. La luz del tubo que parpadea va aparte en cada vértice (`aFlk`) y se enciende y
apaga con él.

Calibrado contra las fotos. Colores medidos en pantalla en la primera sala, en Realista:

| | Medido | Objetivo |
|---|---|---|
| Paredes | (187, 173, 110) | ~(200, 182, 110) |
| Moqueta | (157, 136, 91) | ~(150, 128, 82) |
| Techo | (187, 183, 165) | parecido a las paredes o algo más oscuro |

## Las texturas

Todas se pintan en el propio juego (sin descargas, sin fotos de nadie), en 1024 px, y quedan guardadas para toda la
partida:
- **Papel pintado**: dos tiras de 53 cm con su junta. Lleva columnas de espigas cada 6,6 cm con un fino listado entre
  ellas, la fibra del papel en el sentido del rollo, algo de moteado y su relieve.
- **Moqueta**: bucles en hileras de 4,7 mm, en tres tonos de tostado y con relieve. Las manchas de humedad van por
  encima.
- **Techo**: cuatro clases de placa en una imagen:
  - nueva;
  - amarillenta;
  - con el cerco de una gotera;
  - vieja y rajada.

  Todas con las fisuras y los poros de la fibra mineral y el perfil blanco alrededor. Se giran al azar y una de cada
  cien falta: arriba se ve el hueco oscuro.
- **Difusor de los fluorescentes**: el prismático, con los dos tubos detrás.
- **Enchufes**: dos tomas estadounidenses con su tornillo.
- **Manchas en la pared**:
  - chorretones que bajan del techo;
  - un cerco de humedad;
  - roces al pie;
  - el papel despegándose por una junta.
- **Manchas en la moqueta**.

En **Plastilina**, todo se pinta como pedazos de arcilla:
- las espigas, hundidas en el papel;
- la moqueta, de migas de arcilla;
- la perfilería del techo, como un rollito.

Encima va la arcilla del juego, con sus huellas.

## El sonido

- **El zumbido**:
  - un zumbido de red a 120 Hz con sus armónicos (la red de la foto, la estadounidense);
  - el chisporroteo de las reactancias, más agudo;
  - un pitido fino;
  - el aire de un edificio vacío.

  Suena a unos −28 dB y más alto bajo un tubo: es un fondo, nunca tan fuerte como un coche. El tubo que parpadea
  chasca cada vez que vuelve a encenderse.
- **La música**: la de fondo («Liminal») se calla dentro. Aquí la música es el zumbido. Vuelve al salir.
- **Los pasos**: sobre la moqueta mojada suenan sordos, con un leve chapoteo.
- **La puerta del teatro**: en el escenario, cerca de ella, se oye el zumbido amortiguado.

## Medidas

En un Chrome sin ventana y sin sonido, a 1440 × 900 y 2× (estética Plastilina / Realista):
- **construir el nivel**: 0,8 s / 0,5 s (texturas, luz y geometría);
- **fotogramas**: de 57 a 60 fps en las vistas más anchas (el salón de pilares, el pasillo sin fin), y 60 fps en
  Realista. El procesador trabaja 3–4 ms por fotograma;
- **recorrido completo sin un error**: teatro → escenario → puerta amarilla → Backrooms → cruzar el borde del plano
  corriendo por el pasillo sin fin → chocar con una pared → volver por la puerta → salir a la calle.

## Para probar y seguir

- `tools/backroomslab.js`:
  - `plan()`: el plano desde arriba, con salas, tabiques por clase, tubos, pilares y puertas;
  - `enter()`: entrar directamente;
  - `shoot(tag, VIEWS)` y `CLOSE`: fotos desde puntos fijos.
- `tools/venueshots.js` tiene la vista `puerta` del teatro.
- **Ampliarlo**:
  - el plano está en `ROOMS` (rectángulos de celdas), `OPEN` (los huecos entre salas) y `STUBS` (tabiques sueltos);
  - las rarezas están en `PILLARS`, `SLANTS`, `SLOPE`, `STAIRS`, `DOORS` y `CHAIRS`;
  - los tubos que parpadean, en `FLICKER`;
  - la luz se calibra con `LIT`.
- **Cuando acaben las pruebas**: la puerta del teatro puede pasar del amarillo a su color normal (`venues.js`), para
  que sea un *easter egg* de verdad.
