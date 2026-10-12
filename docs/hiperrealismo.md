# Hiperrealismo: la zona de la iglesia de Santa María

Documento de diseño y única fuente de verdad para el modelo hiperrealista. Si algo no está aquí, se pregunta o se añade
antes de construirlo. Las reglas de trabajo están en `CLAUDE.md`; el registro de comentarios y arreglos, en
`docs/hiperrealismo-registro.md`.

## Qué se pide

El usuario, el 11 de octubre de 2026, en Guareña HQ: «quiero hacerlo hiperrealista, aunque solo sea una parte del juego,
por ejemplo la zona de la iglesia y las partes cercanas, para ir probando cómo queda». Lo pidió con el método de una guía
para hacer juegos con Opus y Blender:
- preparar todo antes de escribir código: un resumen grande, las reglas y los documentos de diseño;
- repartir el trabajo entre agentes, con un revisor que solo mira y aprueba;
- modelar en Blender y empezar por un *greybox*;
- avanzar capa por capa con sus comentarios, apuntando cada arreglo.

Eligió hacerlo en el navegador (three.js, como el resto del juego) con Blender para modelar, sin Unity.

## El objetivo

Que la iglesia de Santa María y lo que la rodea parezcan una fotografía en la estética **Realista**:
- la piedra dorada de mampostería con su sillería;
- la escala enorme de la fábrica del siglo XVI, la luz rasante del atardecer sobre ella;
- las cigüeñas en la torre.

Se juzga siempre frente a las referencias, desde los mismos puntos de vista. La Plastilina se queda como está (allí la
iglesia es de arcilla, a propósito).

## Las referencias (solo para mirar: ni un píxel entra en el juego)

| Qué | De dónde | Licencia | Para qué |
|---|---|---|---|
| Foto del exterior desde el noroeste, al atardecer | Wikimedia Commons, «Iglesia Parroquial de Santa María (Guareña, España).jpg», de El tiu Cancho | CC BY-SA 4.0 | fachada de los pies, costado norte, campanario, portada, óculo, piedra |
| Planta | Catastro (`data/map.json`, edificio 2919) | datos abiertos | la huella exacta |
| (Descartada) | Wikimedia Commons, «Guareña_iglesia.jpg» | — | es un interior (la capilla mayor con el retablo): no sirve para el exterior |
| Vista cenital | PNOA, IGN (`.cache/pnoa`, solo medir) | CC BY 4.0 | cubierta, contrafuertes, cabecera, torre |
| Medidas e historia | «La iglesia de Santa María de Guareña en la arquitectura extremeña del siglo XVI» (Coloquios Históricos de Extremadura); Wikipedia; BOE 1-7-1988 (declaración BIC) | citas | dimensiones, tramos, materiales, fechas |

Lo que dicen las fuentes:
- **Planta:** nave única de unos 50 × 16 m, con cuatro tramos, capillas entre los contrafuertes y capilla mayor
  semicircular; 54 × 27 m por fuera y unos 25 m de alto.
- **Fábrica:** muros de mampostería con sillería en esquinas y contrafuertes; un ventanal por tramo; un óculo sobre la
  portada de los pies; tres puertas de medio punto.
- **Historia:**
  - obras desde 1557, con Sancho de Cabrera y luego Rodrigo Gil de Hontañón;
  - la torre se terminó en 1700;
  - la portada de los pies es de 1793 y la del Mediodía, la más rica, del siglo XVII;
  - en 1900 se hundió el cuarto tramo de bóveda, rehecho hasta 1917.

Lo que enseña la foto:
- **Piedra:** mampostería dorada, con piedras oscuras sobre un mortero ocre y mechinales, y sillares grandes en las
  esquinas.
- **Contrafuertes:** planos, de sillería, con remates de teja a dos aguas.
- **Ventanas:** altas y estrechas, de medio punto, con un relieve bajo el alféizar.
- **Gárgolas:** de cañón, bajo la cornisa, que es lisa y oculta la cubierta.
- **Fachada de los pies:**
  - el óculo, con cuatro anillos moldurados y celosía;
  - la portada, con columnas sobre pedestales, entablamento y frontón con escudo y tres pináculos;
  - una fila de canecillos a media altura;
  - un zócalo más oscuro.
- **Campanario:** sale de la fachada en la esquina suroeste. Es un cuerpo de sillería con dos arcos por cara entre
  pilastras y bolas en las esquinas. Encima, otro cuerpo con arcos y un remate piramidal con bola, cruz y veleta.
  Tiene nidos de cigüeña.
- **Torreón:** uno pequeño en la esquina noroeste.

## La iglesia: medidas (el marco del juego)

Coordenadas locales del marco que el juego calcula sobre la planta del Catastro (`data/hq/iglesia_marco.json`, sacado
del juego con `poi.churchFrame`):
- la x va a lo largo del eje, hacia el este (la cabecera);
- la z va a través, con +z hacia el sur;
- la y es la altura sobre el suelo, en metros.

El marco está sobre el eje de la nave. Su centro en el mundo es (−163,43; −58,09) y está girado 16,5°. El centro del
rectángulo del Catastro queda 2,2 m al sur, porque la sacristía lo tuerce.

De dónde sale cada medida:
- **La planta**, del Catastro.
- **El ritmo de los contrafuertes**, de la ortofoto del PNOA.
- **Las alturas y las posiciones a lo largo de los muros**, de la foto de Commons, con su cámara reconstruida (ver
  «La vista de referencia»).

| Pieza | Medidas |
|---|---|
| Eje de la nave | z = 0, a medio camino entre el muro norte (−13,54) y el sur (+13,54) |
| Bloque principal | x −26,7 → 26,7 (de los pies al ábside), z −13,54 → +13,54 (27 m). Los muros largos van de x −20,68 (el retranqueo noroeste) a 16,66 (el arranque del ábside); el sur se desvía 1,6° del eje, como lo dibuja el Catastro. La esquina suroeste del Catastro (su punto 0) viene torcida 8,8°. La foto no decide: pone esa cara en x ≈ −25,6 ± 0,4, entre el Catastro (−25,2) y una cara recta (−26,34). Se toma la cara recta porque la torre es cuadrada y así el campanario no vuela |
| Cornisa | de sillería, moldurada, con su borde de arriba a 22,05 m y 0,45 m de vuelo. Así su arista cae donde la línea de la foto, con la que el greybox coincidía a 22,5 en el plano del muro: vista desde abajo, una arista más cercana se ve más baja. La cubierta no se ve desde la calle |
| Cubierta | a dos aguas, a 20°, sobre los 18 m de la nave (z ±9), con cumbrera a ≈25,3 m; a cuatro aguas al oeste desde x −20,5; en abanico sobre el ábside (centro en x 15,5); las capillas de alrededor, planas a la altura de la cornisa |
| Tramos | cuatro en los muros largos, de unos 9,6, 8,8, 8,5 y 8,8 m, entre x −20,68 y 14,9; de ahí al ábside, una banda de sillería. La foto (con su cámara rehecha) y la ortofoto coinciden |
| Contrafuertes | bandas planas de sillería en x −11,1, −2,35, 6,1 y 14,9 (esta sigue hasta el ábside), a los dos lados: 2 m de ancho y 0,25 m de vuelo; la cornisa pasa recta por encima |
| Cabezas de los muros entre capillas | en las mismas x, desde 0,7 m detrás de la fachada hasta el alero de la nave (\|z\| = 9). Son muros de ≈1,2 m de grueso (la foto da 1,1–1,3 m y la ortofoto 1,2–1,5), hasta 23,6 m, con remate de teja a dos aguas: los «remates» de la foto y los «⌐» de la ortofoto |
| Ventanales | uno por tramo y lado, en su centro (x −16,3, −6,9, 1,6 y 10,5); de medio punto, con parteluz de piedra, dos arquillos y un óculo calado arriba. La luz mide 1,4 × 3,8 m, con el alféizar a 14,6 m y la clave a 18,4 m; el primero (el del coro, seguramente) va ≈0,5 m más alto: alféizar a 15,1. Alrededor, el recercado de sillería (hasta ≈19 m) y, bajo el alféizar, una cartela tallada (desde ≈13,7 m). En el sur, el último da sobre el tejado de la sacristía |
| Gárgolas | de cañón, ocho por lado, cada 4,8 m desde x −19,1, con el caño a ≈19,5 m (unos 2 m bajo el borde de la cornisa): las dos más cercanas de la foto caen en −19,1 y −14,3 |
| Zócalo | 1,0 m de sillería oscura alrededor |
| Fachada de los pies | tres planos: la torre en x −26,34, el centro en −25,9 y el bloque noroeste en −26,6. En la cara oeste de la torre, una fila de canecillos a ≈8,6 m (z 6,3 → 11,8) y una saetera (z 9,9, a 10,4 m), medidos en la foto |
| Óculo grande | sobre la portada: centro a 10 m, radio 2,3 m, z 0,5. Cuatro anillos moldurados, un anillo de bolas dentro y una celosía de barrotes verticales finos (la foto) |
| Óculo pequeño | bajo la cornisa: centro a 19,7 m, radio 1,0 m, z −0,2 |
| Portada de los pies | la de `churchdoors.js` (su puerta se abre y lleva dentro), en el eje y reducida al 85 %. La foto, con su cámara rehecha, pone su umbral en el eje (z ≈ −0,3) y el vértice del frontón a ≈7,0 m, con el pináculo rozando el óculo. Reducida, la del juego llega a 7,0 m. El hueco de su puerta en el modelo va a esa medida |
| Torre (esquina suroeste) | planta x −26,34 → −19,0, z +6,16 → +13,54 (7,4 m); el cuerpo bajo, enrasado con la fachada hasta la cornisa |
| Campanario | sobre el eje de la torre (centro x −22,6, z 9,6), de 5,7 m de lado, retirado ≈1 m de la fachada; 22,5 → 31,2 m, con cornisa hasta 31,45 y bolas en las esquinas; dos arcos de 1,4 × 3,0 m por cara, en lo alto, entre pilastras |
| Cuerpo alto | de 2,4 m de lado, 31,45 → 35,5 m, con cornisa hasta 35,75; un arco de 0,8 × 1,6 m por cara; bolas en las esquinas |
| Remate | un pedestal esbelto de 1,2 m de lado (35,75 → 37,4 m), una pirámide de 1,0 m de base hasta 39,4 m, bola, y la cruz con veleta hasta 41,5 m. La punta sale de la foto, con la cámara rehecha, y lleva ±1 m de error: los «40 m» de antes no tenían fuente. Nidos de cigüeña en las cornisas |
| Torreón noroeste | junto a la esquina, retirado 0,6 m: x −26,13 → −24,13, z −10,45 → −8,45 (2 m de lado). Su cuerpo y su cornisa llegan a 23,75 m; encima, en cada cara, un frontón de medio punto peraltado de 1,5 m de ancho y, en cada esquina, un pináculo (pedestal, obelisco y bola), hasta 26,2 m (la foto) |
| Bloque noroeste (la escalera) | vestido de sillería en una banda de 2 m junto a la esquina de la fachada, en el escalón del retranqueo y en el final del muro norte. Cuatro saeteras en su cara oeste (z −9,6; a 12,5, 14,9, 17,2 y 19,4 m) y cuatro ventanitas de 0,6 × 0,9 en su cara norte: (x −23,5; 18,6 m), (−24,5; 15,2), (−23,1; 12,2), (−22,5; 5,6). Todo medido con la cámara de la foto |
| Retranqueo noroeste | no es un cuerpo bajo. La cara norte del bloque de los pies está 2,3 m más adentro (z −11,15) entre x −26,7 y −20,7; en la foto, es el escalón al final del muro norte |
| Cabecera | poligonal, centrada en (15,5; 0), de unos 10,3 m de radio, de x 16,7 a 26,7, con contrafuertes en las esquinas (los dientes del Catastro); hasta la cornisa. La sacristía tapa su lado sur en el Catastro, así que se dibuja como el norte, en espejo |
| Sacristía (sureste) | x 9,6 → 25,2; rodea el lado sur del ábside desde z +7,5 hasta +17,9; 9 m de alto |
| Portadas laterales | la del Mediodía (sur) y la del Evangelio (norte), en el tercer tramo, las de `churchdoors.js`. La foto confirma que la del Evangelio está en el tercer tramo |

Las puertas siguen siendo las del juego: se abren al acercarse y llevan al interior (`church.js`).

### La vista de referencia

La foto de Commons se hizo desde la calle, al noroeste, con una Canon EOS 600D a 18 mm (APS-C, sin recortar, según su
EXIF): 45° de campo vertical. Con esa focal fija, la cámara se ajustó a quince puntos de la foto cuya planta se conoce:
- las esquinas;
- los dos extremos del muro norte;
- la clave y el alféizar de los cuatro ventanales norte (sus alturas, como incógnitas);
- los dos óculos.

La lente tiene un barril de ≈−3 %; la cámara del juego no, así que las marcas de la foto se dibujan ya corregidas.

| Dato | Valor |
|---|---|
| Posición | local (−43,3; 1,6; −35,2); en el mundo, (−214,9; −79,6) |
| Distancia a la esquina noroeste | 29 m |
| Rumbo | 44,8° respecto del eje |
| Inclinación | 19,2° hacia arriba |
| Giro | −2,8° |
| Campo vertical | 45° (3:2) |
| Error | ≈14 px de 1920 de media |

Así está en `tools/hipershots.js` (`'noroeste'`). Las marcas de la foto (posiciones, ni un píxel) se dibujan encima con
`tools/hipermarcas.py`.

Cada marca se comprueba sobre la foto ampliada antes de usarla. La del pie de la esquina noroeste estaba ≈100 px
desviada: los coches tapan ese pie. Corregida, la cámara la pone donde está, en (1304, 1200).

Comprobaciones:
- **Ventanales:** con el ojo a 1,6 m, el ajuste deja los ventanales en x −16,5, −6,8, 1,8 y 10,8, aunque se les dejó la
  x libre: son los del modelo.
- **Ojo bajo el suelo:** si se deja libre, se va por debajo del suelo y los ventanales se descolocan. Por eso se fija.
- **Torre:** las esquinas del campanario dan una planta de 5,7 m y la cornisa a ≈31,5 m; el cuerpo alto, 2,4 m.

### La ortofoto engaña en lo alto

El PNOA no es una ortofoto verdadera: lo alto se desplaza respecto de su planta. A la altura de la cornisa, la iglesia
aparece unos 8 m corrida, (−5,7; +5,6) en el marco, que en el mundo es hacia el suroeste; la torre, el doble.

Cómo se midió:
- **La componente z (+5,6):** es lo que va del borde de la cornisa norte en la ortofoto al muro norte del Catastro.
- **La componente x (−5,7):**
  1. con ella, los rasgos de los muros entre capillas («⌐») caen, a los dos lados, en −11,1, −2,4, 6,0 y 14,6;
  2. ahí los ponen también la foto (con su cámara) y los ventanales centrados en sus tramos;
  3. el primer cálculo (−4,5) los dejaba ≈1,2 m al oeste.

La planta se mide en el suelo (el Catastro). De la ortofoto solo valen las distancias entre cosas de la misma altura,
como el ritmo de los contrafuertes.

## Materiales

Las texturas las hace `tools/blender/texturas.py` con las de Poly Haven (CC0, a 2K) de `.cache/polyhaven`. Las deja en
`.cache/hq/tex` y el modelo las lleva dentro (`assets/hq/iglesia.glb`), en JPEG, que es la única copia que se publica.
Las UV van en metros sobre el tamaño de cada una.

| Material | Textura | Tamaño real | Dónde |
|---|---|---|---|
| Mampostería | propia, como la enseña la foto y la midió el revisor. La masa son piedras doradas u ocres de 20–70 cm, casi del tono del mortero, cada una con su trozo de una piedra real («Large Sandstone Blocks 01») y las juntas apenas más oscuras. Sueltas, piedras oscuras angulosas de 10–45 cm: un 13 % del muro (la foto da un 11–13 % en el muro en sombra y un 3–5 % en la fachada al sol). Las oscuras son de un pardo grisáceo, no negras: en la foto valen ≈0,55 del brillo del mortero. Por encima, el grano de «Yellow Stone Wall». Sin costuras | 6 m | paños de muro |
| Mampostería de la fachada de los pies | la misma, con solo un 3,5 % de piedra oscura (la foto da un 3–5 % en la fachada al sol) | 6 m | la fachada oeste |
| Sillería | «Large Sandstone Blocks 01», pasada del gris al dorado de la foto. Se le quitan las manchas anchas que cruzaban las juntas: queda un dorado parejo con su grano | 3 m | esquinas, contrafuertes, cornisas, recercados, torre, remates |
| Zócalo | la sillería, oscurecida (×0,62) | 3 m | el zócalo |
| Teja árabe | «Clay Roof Tiles 02», envejecida: más parda y apagada, como las de la ortofoto | 2,5 m | cubiertas y remates |
| Madera de las puertas | «Rough Pine Door» | — | (las puertas siguen siendo las del juego) |
| Losas de granito | «Granite Tile» | — | (fase 5: el atrio) |
| Adoquín | «Cobblestone Floor 08» | — | (fase 5: las calles) |

En el juego, la piedra lleva además una mancha suave en coordenadas del mundo (`src/hiper.js`): más oscura o más cálida
aquí y allá. Así no hay dos trozos de muro iguales aunque la textura se repita cada 6 m. Mezclar una segunda lectura
girada de la textura dejaba piedras fantasma, y se descartó.

Crédito: texturas de Poly Haven (polyhaven.com), CC0.

## Cómo se construye

- **Texturas:** `tools/blender/texturas.py` (Blender sin ventana, con numpy) → `.cache/hq/tex`.
- **Modelo:** `tools/blender/iglesia.py`, en Blender 5.2 sin ventana.
  - Lee el marco (`data/hq/iglesia_marco.json`) y los parámetros de la tabla, que van en el propio script, en un bloque
    `SPEC` que copia la tabla.
  - `--greybox` saca solo los volúmenes, en gris (fase 1).
  - Sin él, hace las fases 2–4:
    - **Piezas y huecos:** cada pieza en su material, y los huecos cortados de verdad con booleanas (ventanales, óculos,
      la saetera, el bolsillo de cada puerta con su vestíbulo).
    - **Sombra de la piedra:** la oclusión ambiental de la piedra, cocida en Cycles sobre un segundo juego de UV, que el
      juego usa como `aoMap`.
    - **Mallas:** una malla por material.
  - Escribe `assets/hq/iglesia.glb` y, al lado, `iglesia.json`, con lo que el juego tiene que saber: los contrafuertes,
    para sus colisiones, las campanas, los nidos y el tamaño de la portada de los pies.
- **Juego:** `src/hiper.js`, solo en la estética Realista.
  - Carga el modelo en el marco de la iglesia y esconde los volúmenes del modelo antiguo; deja las portadas con sus
    puertas.
  - Reduce la portada de los pies al tamaño de la foto, con sus colisiones.
  - Da colisión a los contrafuertes y cuelga las campanas de su corona para que volteen.
  - Pone a la piedra la mancha a gran escala.
- **Luz:** el sol y el cielo del juego; la oclusión ambiental cocida.
- **Fotos para el revisor:** `tools/hipershots.js`, en la página del juego con `?estilo=real` y una partida empezada; con
  `clear`, el cielo despejado de la foto, sea cual sea el tiempo real. Saca a `.snaps/hq_<vista>_<etiqueta>.jpg`:
  - la vista de la foto de referencia (`noroeste`);
  - la plaza;
  - cuatro vistas de dron;
  - tres primeros planos: la fachada de los pies desde su calle, un ventanal norte y lo alto de la torre;
  - la cenital, sobre la misma ventana que el recorte del PNOA (x −205 → −120, z −90 → −25, norte arriba, 0,075 m/px).

  Después, `tools/hipermarcas.py` dibuja encima de la vista `noroeste` las marcas de la foto.

## Fases (cada una la aprueba el revisor antes de la siguiente; el usuario, al final)

1. **Greybox:** los volúmenes y las alturas de la tabla en gris, en el juego. Se aprueba si se parecen a la foto vista
   desde su mismo punto (el noroeste) y encajan con la ortofoto desde arriba. *Aprobado con arreglos menores el
   2026-10-11, a la segunda; los arreglos, hechos.*
2. **Detalle:**
   - cornisas, contrafuertes con sus remates, ventanales, gárgolas y zócalo;
   - el óculo con sus anillos, los canecillos y la torre completa;
   - el torreón, la cabecera y la sacristía.
3. **Materiales:**
   - la piedra a su escala real, la sillería distinta de la mampostería y la teja;
   - el color comparado con la foto (la piedra dorada, no gris ni naranja).
4. **Luz:** de día, al atardecer y de noche (los focos), con oclusión ambiental y sombras nítidas; sin brillos de
   plástico.
   - **El sol de la foto.** Venía a ≈4° de altura y rumbo ≈237° (el reloj de la cámara iba una hora adelantado). El
     juego atenúa el sol cerca del horizonte, y a 4° le da la mitad de fuerza. Por eso la vista de la foto se saca con
     ese rumbo a 9°, donde el juego ya da el sol entero.
   - **El contraste.** En la foto, la fachada al sol es ≈3,4 veces más clara que el muro en sombra. En el juego es
     menor, porque el cielo y la luz de rebote aclaran las sombras en todo el pueblo. Eso es la luz de todo el juego y
     su cambio lo decide el usuario.

   Las fases 2, 3 y 4 se revisan juntas. El detalle no se puede juzgar frente a la foto sin su piedra y su luz:
   un muro gris liso no dice si un recercado sobra o falta. Los focos de noche quedan para después.
   **4b. Lo que se trae de Unity (2026-10-11).** *Aprobado el 2026-10-11, a la segunda; publicado en HQ.* La comparación con Unity HDRP (proyecto aparte, `unity-iglesia`;
   ver el registro) mostró qué hace mejor un motor de gama alta con el mismo modelo. Al juego se trae lo que se puede
   llevar sin tocar la luz de todo el pueblo, que el usuario quiere como está:
   - **El vidrio refleja el cielo.** En el juego era un agujero negro; ahora toma el mapa del cielo entero, con la
     rugosidad de un vidrio (0,06).
   - **La oclusión, con la luz que rebota.** El mapa de oclusión aprobado se queda tal cual, y se le suma la luz que
     rebota entre las piedras y en la calle (Cycles, difuso indirecto bajo un cielo blanco, 256 muestras):
     oclusión + (1 − oclusión) · rebote. Los muros abiertos apenas cambian. Los derrames, las cartelas y los rincones
     quedan en sombra, pero no negros.
     - *Primer intento, descartado:* hornear la luz entera de un cielo blanco y escalarla a la mediana del mapa anterior.
       La calle de debajo cuenta como cielo que el muro no ve, y el juego ya pone ese suelo oscuro en su luz ambiente. Los
       muros abiertos habrían bajado de ≈0,95 a ≈0,63, y toda la cara en sombra se habría oscurecido.
   - **La cartela es piedra.** El panel rehundido bajo cada ventanal se cortaba con el material de los huecos y salía
     una ranura negra alrededor del óculo.

   Se aprueba si, en las mismas vistas:
   - el vidrio enseña el cielo;
   - los rincones y derrames no salen negros;
   - los muros abiertos no cambian (±5 % en los parches de la foto);
   - el juego sigue a más de 50 fps.

   Lo que Unity hace mejor y no se trae, porque es la luz de todo el pueblo:
   - el cielo más azul y oscuro;
   - el sol bajo a pleno;
   - la penumbra de las sombras.

5. **Alrededores:** el atrio y las calles de alrededor, el suelo, los bordillos, las casas de enfrente y los faroles.

   **5a. La capa de desgaste de la iglesia (2026-10-11).** Lo pidió el usuario: aún no la ve hiperrealista, y quiere
   desgaste, suciedad e irregularidades en los muros. Se toma de la foto de Commons, que lo enseña así:
   - **Churretes.** En el muro norte hay una mancha larga, oscura y verdosa, que baja de la cornisa junto a la banda de
     sillería del extremo oeste. Bajo las gárgolas, regueros oscuros de un par de metros.
   - **Desconchones.** La fachada de los pies tiene manchas claras donde el revoco o la piedra han saltado, y piedras de
     colores muy distintos.
   - **Mechinales.** Filas de agujeros cuadrados pequeños en la fachada de los pies y en la torre: los de los andamios.
   - **El pie.** El zócalo y el arranque de los muros son más grises y sucios.

   Cómo se hace:
   - **Una capa en el sombreado** de la piedra de la iglesia (`src/hiper.js`), calculada con la propia forma del
     edificio en su marco. Sin texturas nuevas ni descargas.
     - Churretes bajo cada gárgola, bajo los extremos de los alféizares y desde la cornisa, a trechos al azar y de largo
       distinto. El grande del muro norte va en su sitio.
     - Humedad y suciedad en el metro y medio de abajo, más en el lado norte.
     - Desconchones claros en la mampostería, más en la fachada de los pies.
     - Liquen en las caras que miran arriba (cornisas, alféizares, remates) y en la teja.
     - Ondulaciones suaves del muro, de medio metro a dos, para que no sea un plano.
     - Los sitios de gárgolas y ventanales salen del modelo (`iglesia.json`), no se repiten a mano.
   - **Los mechinales,** como agujeros de verdad en el modelo (`tools/blender/iglesia.py`).

   Se aprueba si, frente a la foto y en las vistas de siempre:
   - los churretes, el pie sucio, los desconchones y los mechinales se reconocen donde la foto los tiene;
   - nada parece pintado encima: siguen la forma del edificio y no se repiten a la vista;
   - la piedra al sol y en sombra no cambia de media (±5 % en los parches de la foto);
   - el juego sigue a más de 50 fps.

   **5b. El suelo de alrededor (después de 5a).** Junto a la iglesia no hay una plaza enlosada:
   - al norte, el «Estacionamiento de la Iglesia», un aparcamiento de asfalto lleno de coches, como en la foto;
   - un pequeño parque;
   - calles estrechas de asfalto (Santa María, Pozo Pajares, la Cuesta, de 16 m), con aceras estrechas y el bordillo
     al pie de la iglesia.

   Se hace en Blender con texturas propias:
   - asfalto con su árido, parches, grietas, manchas de aceite y rayas de aparcamiento gastadas;
   - aceras con baldosas sueltas o hundidas;
   - bordillos de granito desconchados;
   - alcorques, tapas y sumideros;
   - el suelo un poco ondulado;
   - y, en las juntas, polvo y malas hierbas.

6. **El interior en alta definición** (2026-10-11): ver «El interior», más abajo. Se hace antes que los arreglos de
   la 5a y que la 5b, que quedan en pausa.

## El interior (fase 6)

### Qué se pide

El usuario, el 11 de octubre de 2026: «Haz la iglesia por dentro de muy alta definición, todo, esculturas, santos,
cuadros, bancos, decoraciones, velas, flores... todo con el máximo detalle y realismo como si fuera el GTA V, usa
Unreal para hacerlo posible.»

Unreal no puede ir dentro del juego, que es una página web. Por eso el usuario eligió:
- **En el juego web:** se hace con lo que hace un motor así:
  - la luz que rebota, horneada en Blender (Cycles);
  - escaneos de materiales reales;
  - modelos detallados;

  pero dentro del juego del navegador y solo en la estética Realista.
- **Escaneos reales:**
  - texturas y modelos libres (Poly Haven, ambientCG, Smithsonian Open Access);
  - Megascans de Fab solo con la cuenta de Epic del usuario, y si su licencia deja usarlos fuera de Unreal: desde
    2025 la mayoría son de pago;
  - imaginería española escaneada con licencia libre, con su crédito.

  Cada descarga se pide antes, con su nombre, su origen y su tamaño.
- **Cuadros reales de dominio público:** Zurbarán, Murillo, Morales…, en reproducciones de obras en dominio público,
  con su crédito. Es la única excepción a «ni un píxel de una foto», y la decidió el usuario.
- **El suelo:** losas de granito gris. Lo dice el usuario, que conoce la iglesia.

### Lo que se sabe del interior

**De los textos**, los que cita `src/church.js`: Diputación de Badajoz; J. García Murga, *Coloquios Históricos de
Extremadura*, 1977 y 2001; la audioguía de la parroquia.
- **La nave:** una sola, de ≈50 × 16 m, «quizá la mayor de toda la región». Tiene cuatro tramos con bóvedas de
  terceletes sobre altas columnas jónicas estriadas.
- **Las capillas:** entre los contrafuertes, tras arcos apuntados. Las puertas laterales están en el tercer tramo.
- **El coro:** alto, a los pies, sobre un sotocoro de «afiligranadas crucerías», y lo alumbra el óculo grande.
- **La cabecera:** semicircular, bajo una media naranja de casetones.
- **El retablo mayor:** de madera dorada, de Diego López Cabrera (1945–49); el antiguo ardió en 1936.
- **La sacristía:** del lado de la Epístola.
- **La pintura mural:** Santo Domingo y Santa Catalina, tras el altar colateral derecho.

**De la foto de Commons «Guareña iglesia.jpg»** (CC BY-SA 3.0, de 300 × 400; solo para mirar): enseña el presbiterio
y la cabecera.
- Todo es de un blanco grisáceo frío: granito y encalado.
- El tramo de delante de la cabecera tiene una bóveda estrellada de nervios.
- La media naranja tiene unas cinco filas de casetones, que menguan hacia arriba.
- El arco triunfal es ancho, con el intradós de casetones.
- En los bordes se ven columnas estriadas.
- El retablo es dorado:
  - tres cuerpos y un ático, en cinco calles;
  - cuadros en los paneles de los lados y el sagrario en el centro.
- Hay dos faroles de hierro en la pared, uno a cada lado, y ventanas a los lados de la cabecera, que salen blancas.
- Al pie, una alfombra roja y un comulgatorio.

### Las medidas: las de `src/church.js`

La planta del juego no cambia. De ella dependen:
- las puertas y sus cancelas;
- las colisiones;
- los sitios donde se aparece;
- la misa (`ChurchLife`);
- la puerta de la sacristía, que lleva a los Backrooms.

El modelo nuevo se hace con esas mismas medidas:
- **ejes:** la x hacia el altar (el este), la z hacia el sur (la Epístola) y la y hacia arriba, sobre
  `INTERIOR_ORIGIN`;
- **unidades:** metros.

| Pieza | Medidas |
|---|---|
| Nave | de los pies (x −26,5) al arco triunfal (x 18,5); 16 m entre columnas (z ±8) |
| Tramos | cuatro de 9,5 m, desde el frente del coro (x −19,5); pilares de 2,4 m de ancho y 3,1 m de fondo (las capillas) |
| Columnas | jónicas, estriadas, adosadas a cada pilar en z ±8,05, sobre pedestales de 1,5 m; fuste de radio 0,62–0,67; los capiteles bajo el arranque de las bóvedas (12,4 m) |
| Arcos fajones | de medio punto, de columna a columna, de radio 7,75 |
| Bóvedas | de terceletes; la clave a ≈20,9 m; claves doradas. La del presbiterio, estrellada (la foto): combados en rombo por los extremos de los terceletes y en cuadrado por las diagonales, con 13 claves |
| Capillas | de 7,1 × 3,1 m y 10,2 m de alto, tras arcos apuntados (arranque 6,6, flecha 3,3) |
| Ventanales | uno por tramo y lado, en el centro, en el luneto de la bóveda (que sube 7 m sobre el arranque). La luz, de 1,4 × 3,8 m entre 14,6 y 18,4 m, como en la foto de fuera; por dentro, el derrame la abre a 2,1 m, de 13,4 a 18,6 m. `church.js` los tenía a 10,9–15,2, cruzando la imposta. Dos en la cabecera, de 0,88 m, de 8,6 a 11,6 m, a los lados, junto a las columnas del arco (la foto no enseña ventanas junto al retablo: su luz llega por los bordes) |
| Óculo | en el muro de los pies, con el centro a 10 m como en la foto de fuera (`church.js` lo tenía a 12,55); 3,2 m de luz, con su derrame y tres anillos moldurados |
| Cabecera | semicírculo de radio 8 centrado en x 18,5, con sus muros de sillería de granito claro (la foto); media naranja desde 12,4 m, con 12 × 5 casetones de cal, sus fondos algo más grises |
| Presbiterio | cinco gradas desde x 13,6 (0,9 m en total); de ahí, el suelo a 0,9 |
| Coro y sotocoro | de x −26,5 a −19,5; el suelo del coro a 6,2 m; la bóveda del sotocoro, de 4,5 a 5,75 m |
| Puertas | la de los pies (2,6 m de luz, arranque 3,7), la del Mediodía (2,3; 3,3) y la del Evangelio (2,2; 3,2), estas dos en el tercer tramo; la de la escalera de la torre, en el coro; la de la sacristía, en la cabecera |

### Cómo se hace

- **El modelo:** `tools/blender/interior.py`, en Blender sin ventana, con las medidas de la tabla. Sale a
  `assets/hq/interior/`, en tres partes:
  - la geometría (`interior.glb`);
  - las texturas, en archivos aparte;
  - los mapas de luz.

  Así, cambiar la geometría no obliga a volver a subir las texturas.
- **Las texturas:** las hace `tools/blender/texturas_interior.py`, desde los escaneos de `.cache`. Las del juego van
  optimizadas.

  | Material | De dónde | Tamaño real | Dónde va |
  |---|---|---|---|
  | Granito | «Granite002A» de ambientCG, gris claro y neutro, mate y labrado: el escaneo es de una encimera pulida, así que su moteado va a la mitad de contraste, algo suavizado y casi sin color. Los sillares y dovelas, con sus juntas | grano ≈0,7 m; sillar ≈60 × 40 cm | columnas, pedestales, arcos, nervios, impostas, zócalo, gradas, óculo, muros de la cabecera |
  | Encalado | «Plaster003» de ambientCG, blanqueado a cal: blanco neutro, algo frío (la foto), con las pasadas de la llana | ≈1,6 m | muros, plementos de las bóvedas, capillas, casetones |
  | Losas del suelo | propias: losas de granito a hiladas, de largo variable, cada una con su trozo de granito; desgaste y arañazos de «Large Floor Tiles 02» (Poly Haven) | losas de 0,6–1,2 × 0,5–0,7 m | la nave, las capillas, el coro |
  | Dorado | metal dorado con su rugosidad, sin textura | — | claves |
  | Vidrio | propio: vidriera emplomada de vidrio claro, algo verdoso y desigual | — | ventanales y óculo |

- **La luz** (como hacen Unreal y Unity: lo que no se mueve, horneado):
  - **El sol directo:** en tiempo real. Es el sol del juego, con sus sombras: las manchas de sol se mueven con la
    hora y siguen los haces de polvo.
  - **El cielo:** horneado. Es la luz que entra por ventanales y óculo, con sus rebotes, bajo un cielo blanco. En el
    juego se escala con el color y la fuerza del cielo de cada hora.
  - **El rebote del sol:** horneado a cinco horas. El juego tiene un recorrido fijo del sol (finales de septiembre):
    9:30, 12:00, 14:30, 17:00 y 19:30. En cada momento se mezclan las dos más cercanas.
  - **La noche:** las arañas, las velas, la lámpara del Santísimo y los focos del retablo, horneados (su luz y sus
    rebotes). Se encienden cuando el juego enciende las luces.
  - **En lo horneado no actúan** ni la luz ambiente del juego ni sus luces puntuales, que ya están en el mapa. (Se
    quitan del trozo de three ya expandido: en `onBeforeCompile` el shader aún tiene sus `#include`, y buscar dentro
    de ellos no encuentra nada.)
  - **El color de las lámparas:** ≈3000 K, el de las arañas de `church.js`, el mismo en los mapas y en las sondas.
  - **Lo que se mueve** (las personas, el jugador) toma la luz de una sonda: una foto en cubo del propio interior al
    entrar. Esa misma foto da los reflejos del oro, el vidrio y el suelo.
  - **La exposición:** dentro, como una cámara que se adapta a la penumbra. También al color: deshace en parte el de
    la luz que domina (cielo, sol y lámparas, por su parte), un 70 % de día y un 21 % de noche, como un balance de
    blancos. La cal se ve blanca bajo el sol, y de noche las lámparas siguen cálidas.
- **La carga:** el interior no va dentro de la página, que ya pesa 27 MB. Se descarga aparte, en segundo plano una
  vez cargado el pueblo, o al entrar. Mientras llega, se ve el interior de ahora.
- **El juego:** en la estética Realista se esconden las mallas de la arquitectura de `church.js` y se pone el modelo.
  Puertas, cancelas, bancos, altares, imágenes, velas y personas siguen siendo las de siempre hasta sus subfases.
  - La arquitectura de `church.js` usa claves de material propias (`granA`, `stepA`, `goldA`, `goldPlainA`), aparte de
    las de los muebles. Así se puede esconder ella sola (`h.archMats`).
  - Los haces de polvo entran por los ventanales del modelo (`interior.json`, «ventanas»).
- **Las herramientas:**
  - `tools/blender/interior.py` hace el modelo y hornea la luz:
    - `--greybox` saca solo los volúmenes;
    - `--sin-luz` lo hace sin hornear;
    - `--muebles` toma los muebles del juego;
    - `--lm` y `--lm-sol` fijan el tamaño de los mapas;
    - `--muestras` y `--muestras-sol`, las muestras de Cycles.
  - `tools/blender/texturas_interior.py` hace las texturas.
  - `tools/hipermuebles.py` saca del juego los muebles de `church.js` (bancos, retablos, altares, púlpito, órgano,
    cancelas), para que den su sombra en el horneado; no se exportan con el modelo.
- **Lo que nadie ve desde dentro** (las caras de fuera de los muros, sus remates, lo que queda en la piedra o encima de
  las bóvedas) se quita del modelo, para que el mapa de luz tenga más resolución. Se sabe por rayos desde unos 7.300
  puntos del aire de la iglesia. Esas caras siguen dando sombra en el horneado y salen aparte como «sombra», una malla
  que solo proyecta la del sol: sin ella, los muros eran láminas para el mapa de sombras y el sol se colaba por los
  rincones.
- **Los mapas de luz:**
  - cielo y lámparas, de 3072 px; rebote del sol, de 2048 px; unos 4,3 cm por píxel en todas partes, también en
    bóvedas y arcos;
  - el rebote del sol, con 4 veces las muestras del resto: su luz sale de unas pocas manchas de sol pequeñas y muy
    brillantes, que un camino encuentra pocas veces;
  - cada pieza curva (molduras, nervios, arcos, torneados, plementos, media naranja) en una sola isla del atlas, con la
    costura en su cara escondida (dentro de la piedra o encima de la bóveda). Márgenes de 4 px y relleno de 8;
  - el quitarruido (OIDN) guiado por las normales de cada píxel del atlas, que hornean una vez por tamaño;
  - WebP sin pérdida (calidad 100) en sRGB, con su escala en `interior.json`: sin los bloques del JPEG;
  - la escala no pasa de 24 veces la mediana del interior. Lo que supera eso (los derrames a pleno cielo) sale blanco
    en pantalla de todos modos, y así los 8 bits se quedan para la penumbra.
- **Las piezas talladas, en el mapa de luz:**
  - **Los fustes estriados** se hornean como cilindros lisos, con su desenvolvimiento propio. La sombra de cada estría
    la pone el sombreado del juego: un mapa de 4 cm por píxel no puede dibujar estrías de 17 cm.
  - **La media naranja y el intradós del arco triunfal** tienen su proyección de una pieza (la media naranja, de área
    igual), y su textura sigue el mismo desenvolvimiento, en metros. Sus marcos son de cal; sus fondos, de una cal más
    gris (los centros oscuros de la foto). La sombra de los fondos la da el horneado, sin oclusión por vértice.
- **Lo que no se hornea** (los muebles, las puertas, los cuadros de `church.js`) toma la luz de las sondas:
  - una rejilla cada 1,5 m por el aire de la iglesia, con la luz que llega por cada uno de sus seis lados («ambient
    cube», como en los motores);
  - se hornean con los mapas y se mezclan igual;
  - esas piezas dejan de recibir la luz ambiente del juego y sus luces puntuales.
- **Sin rendijas:**
  - los plementos se meten 18 cm en los muros y bajo los arcos;
  - la media naranja tiene un borde que entra en el muro y en el arco triunfal;
  - alrededor de la cabecera, entre la coronación de su muro y el tejado, una carcasa estanca solo para la sombra.
- **La luz del cielo, dentro:** neutra y algo fría, con la fuerza del cielo del juego.
- **Los reflejos** (el oro, el suelo): una foto en cubo del interior desde el centro de la nave. En cada superficie se
  escalan con su luz, la horneada o la de las sondas, frente a la del sitio de la foto: el oro de una capilla en
  penumbra no brilla como el de la nave.
- **Los haces de sol:** volúmenes de luz de borde suave (cada píxel sigue el rayo a través del haz), y no cajas de
  caras duras.
- **La carga:** `tools/build.py` deja `assets/hq/interior/` fuera de la página y al lado, en `dist/assets`; la
  publicación de GitHub Pages la copia junto a la página.

### Subfases (cada una la aprueba el revisor; el usuario, al final)

- **6a. La arquitectura y su luz:**
  - suelos y gradas;
  - muros, pilares y capillas;
  - columnas, arcos y bóvedas con sus nervios y claves;
  - cabecera y media naranja;
  - coro y sotocoro;
  - ventanales, óculo y huecos de las puertas;
  - zócalo e impostas;
  - todo con la luz horneada.
- **6b. Los muebles:**
  - bancos;
  - altar mayor y altares de las capillas;
  - el retablo mayor y los colaterales;
  - púlpito, coro y órgano, confesionarios, pila bautismal y rejas.
- **6c. Las imágenes y la vida:**
  - santos y esculturas;
  - cuadros de dominio público con sus marcos;
  - velas, flores, manteles y paños;
  - arañas y faroles.

### Se aprueba (6a) si

- **Las proporciones:** encaja con las colisiones de `church.js` (no se atraviesa nada y nada flota). El presbiterio,
  visto desde el punto de la foto, se parece a ella: la bóveda estrellada, la media naranja, el arco y las columnas.
- **La luz:**
  - entra por ventanales y óculo y rebota;
  - los rincones quedan en penumbra pero no negros;
  - el horneado no tiene ruido, manchas ni costuras;
  - las manchas de sol se mueven con la hora;
  - de noche alumbran las arañas.
- **Los materiales:** a su escala (un sillar de granito, ≈60 × 40 cm), sin repeticiones a la vista y sin brillo de
  plástico.
- **El rendimiento:** dentro, más de 50 fps en el Chrome sin ventana de siempre, y sin errores.
- **El peso:** la 6a no pasa de 30 MB de descarga.

### La 6b: los muebles

**Qué hay que hacer.** Son los muebles que monta hoy `church.js`, con sus medidas y su sitio: las colisiones, los
puntos de uso y la misa no cambian.
- **Bancos:**
  - dos bloques de roble, a cada lado del pasillo central, de 1,25 a 7 m del eje, a 0,98 m uno de otro;
  - respaldo de cuarterones con su repisa de misales y reclinatorio acolchado de terciopelo;
  - testeros recortados en voluta, con un cuarterón tallado en el del pasillo.
- **El presbiterio:**
  - el altar de mármol (mesa sobre pie y frontal) con sus manteles de lino;
  - el ambón, las sillas de madera tapizadas y la credencia;
  - el comulgatorio al pie del presbiterio (la foto lo enseña): una baranda baja.
- **El retablo mayor** (Diego López Cabrera, 1945–49, madera dorada). La composición y las medidas son las de
  `src/retablo.js`, sacadas de fotos del retablo:
  - tres planos: el central, plano; las calles de fuera, giradas con la curva del ábside;
  - cinco calles sobre un banco, tres cuerpos y un ático;
  - columnas con el tercio bajo tallado, fuste estriado y capitel corintio; entablamentos quebrados sobre ellas;
    cornisa con dentellones;
  - el sagrario y el expositor, la hornacina de la Virgen con su venera y su resplandor, el Calvario, el Espíritu
    Santo en su gloria, frontón partido y cruz;
  - las cajas de los 12 apóstoles y de los 4 doctores (los cuadros van en la 6c).
- **Los colaterales:** los retablos de las cinco capillas, de un cuerpo y tres calles con ático, con las medidas de
  `church.js`:
  - mesa de altar y columnas salomónicas;
  - hornacina central para su imagen y dos cajas para sus cuadros (las dos, en la 6c).
- **El púlpito:** copa de granito sobre columna, escalera de hierro con pasamanos y tornavoz de madera con su remate
  dorado.
- **Los confesionarios** (dos, en el tramo de las puertas): de madera, con celosía, cortina de terciopelo y remate.
- **La pila bautismal** (copa gallonada de granito, tapa de madera) y la reja de hierro forjado de su capilla.
- **El órgano del coro:** caja de madera con tres castillos de tubos y decoración dorada, **apartado del óculo**.
- **Lo pequeño:**
  - pilas de agua bendita, cepillo y placa;
  - los marcos de las 14 estaciones del Vía Crucis.

  Los candeleros de hierro con sus velas encendibles siguen siendo los de `church.js`.

**Materiales.** Los CC0 de Poly Haven se descargaron el 12-10 a `.cache/polyhaven/muebles_6b`:

| Material | Para qué |
|---|---|
| madera oscura «Dark Wood» | bancos, púlpito, confesionarios, órgano, sillas |
| terciopelo «Velour Velvet», teñido de granate | reclinatorios, cortinas, tapicería |
| «Quatrefoil Jacquard Fabric», en rojo | alfombra del pasillo, paños |
| lino «Rough Linen» | manteles |
| «Marble 01» | altar, comulgatorio |

- **El dorado, propio:** pan de oro, con el bol rojo asomando en lo hondo de la talla. Es más brillante en lo
  saliente, como el oro bruñido junto al mate de un retablo.
- **La talla:** en geometría donde se ve de perfil; lo menudo, en mapa de normales.
- **El granito y el hierro:** los de la 6a.

**Cómo se hace:**
- **El script:** `tools/blender/muebles.py`, en Blender sin ventana. Cada mueble es una función con sus medidas, y
  todo sale a `assets/hq/interior/muebles.glb`.
- **Entran en el horneado.** Los muebles quietos (bancos, retablos, altares, púlpito, confesionarios, órgano) llevan
  su mapa de luz, como la arquitectura, en el mismo atlas o en uno propio. Dejan de tomar la luz de las sondas: así un
  banco tiene su sombra suave debajo y el retablo su penumbra en lo hondo. Las sondas quedan para lo que se mueve.
- **Los repetidos** (unos 30 bancos, las 14 estaciones) son una sola malla con varias copias. Cada copia lleva su
  trozo del atlas de luz, con una escala y un desplazamiento propios, como en Unity.
- **Los dorados y la plata** reciben en tiempo real la luz de las arañas y los focos: un metal no tiene luz difusa
  que contar dos veces, y así sus brillos chispean. En lo demás, esas luces ya van horneadas.
- **El órgano** se aparta del óculo: su centro pasa a −5,3 m, con 5 m de ancho.
- **`church.js` sigue mandando en lo que se toca:** las colisiones, sentarse, encender velas, el agua bendita y los
  carteles; también la gente rezando y la misa. Se esconden sus mallas de muebles, como en la 6a las de la
  arquitectura. Lo pequeño que se mueve o se enciende (las velas del jugador) sigue siendo suyo.

**Peso y rendimiento:**
- muebles, texturas y horneado nuevo suman como mucho 25 MB más; la 6a y la 6b juntas, 50 MB como mucho, aparte de
  la página;
- dentro, más de 50 fps.

**Se aprueba (6b) si:**
- todo encaja en su sitio y con las colisiones: nada flota ni se atraviesa;
- de cerca, cada mueble se lee como el objeto real, sin repeticiones a la vista:
  - veta y desgaste en la madera, más en los bordes y donde se apoyan las manos;
  - terciopelo con su brillo;
  - talla con profundidad;
  - dorado con su bol;
- los muebles están dentro de la luz: sombras suaves debajo y detrás, penumbra en lo hondo de la talla, nada que
  parezca flotar sobre el suelo;
- el peso y el rendimiento caben en lo dicho.

### La 6c: santos, cuadros y vida (plan)

- **Los cuadros:** reproducciones fieles de pinturas en dominio público, de Wikimedia Commons, con su crédito.
  - **Para el retablo mayor:** un apostolado completo de la pintura española (los 12 apóstoles; por ejemplo, el de El
    Greco o el de Ribera) y los 4 Doctores de la Iglesia.
  - **En las capillas:** santos de Zurbarán, Murillo y Morales, según la advocación de cada una.
  - **Las descargas:** se propone la lista, cada archivo con su tamaño, y se descarga con permiso del usuario. El
    12-10 aprobó 25 (en el registro), solo las marcadas como dominio público.
  - **El encaje:** cada lienzo llena su hueco, recortado por los bordes como un lienzo hecho a medida. Si la
    proporción no cabe (la Crucifixión de El Greco, alta y estrecha), el marco se hace a la del cuadro.
  - **En el juego,** cada cuadro va con su marco y su barniz, un reflejo suave.
- **Las imágenes:** la Virgen del retablo, el Cristo, la Dolorosa, San José, el Sagrado Corazón, la Inmaculada y el
  Calvario.
  - Son talla policromada, como la imaginería española: carnaciones mates, ropas estofadas (oro con dibujos rayados
    sobre el color) y ojos de cristal.
  - **Se tallan en Blender** (lo eligió el usuario el 12-10): cuerpos de MakeHuman (la vía de los personajes del
    juego) en su postura, ropajes con sus pliegues, y la policromía de la imaginería
    (`tools/blender/imagenes.py`).
  - **Todas con cuello** (lo pidió el usuario el 12-10: «la cabeza está metida en los hombros»):
    - la cabeza, sobre el cuello del cuerpo: los rasgos de mujer se toman desde la base del cráneo y se desvanecen
      por el cuello, sin la altura de la mujer entera, que la hundía 15 cm en los hombros;
    - la túnica, con escote en la raíz del cuello (el «tights» de MakeHuman sube hasta el cráneo como una
      capucha), con el borde ceñido a la piel;
    - el velo, ajustado a la cabeza y abierto bajo la barbilla; el manto, sobre los hombros;
    - lo que lleven en brazos o en el pecho (el Niño, el corazón, el puñal) no tapa la cara ni el cuello.
  - **Las comprobaciones:** de frente y de tres cuartos en Blender, y en el juego, desde el suelo y de cerca
    (`shootImages` de `tools/churchshots.js`).
- **La vida:**
  - velas de cera con su llama y su goteo;
  - flores (nardos, gladiolos, rosas) en jarras de cristal y de metal;
  - manteles de encaje y paños de altar;
  - las arañas, y los dos faroles de hierro que la foto enseña en la pared de la cabecera.

### Créditos

- Texturas CC0:
  - de ambientCG (ambientcg.com): «Granite002A» y «Plaster003»;
  - de Poly Haven (polyhaven.com): «Large Floor Tiles 02»; para los muebles (6b), «Dark Wood», «Velour Velvet»,
    «Quatrefoil Jacquard Fabric», «Rough Linen» y «Marble 01».
- Foto de referencia, solo para mirar: «Guareña iglesia.jpg», Wikimedia Commons, CC BY-SA 3.0.

## Lo que mira el revisor

- Proporciones y alturas frente a la foto y la tabla. La torre debe sobresalir lo que sobresale; la fachada no puede
  quedar ni chata ni estirada.
- Que no haya huecos, caras invertidas ni piezas flotando, y que nada se meta en el suelo o en las calles.
- La escala de las texturas: un sillar mide en torno a 60 × 40 cm. Los mampuestos dorados, de 20 a 70 cm, y los oscuros, de 10 a 45 cm.
- El color y la luz frente a la foto. Las capturas se comparan en las mismas condiciones: el tiempo propio del juego,
  no el de Guareña en directo (cambia entre tandas), y el «bloom» de la hora de la captura (`game.updateBloom()`).
- Que el juego siga a más de 50 fps en la zona y que no aparezcan errores.
