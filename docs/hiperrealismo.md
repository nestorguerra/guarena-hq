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

## Lo que mira el revisor

- Proporciones y alturas frente a la foto y la tabla. La torre debe sobresalir lo que sobresale; la fachada no puede
  quedar ni chata ni estirada.
- Que no haya huecos, caras invertidas ni piezas flotando, y que nada se meta en el suelo o en las calles.
- La escala de las texturas: un sillar mide en torno a 60 × 40 cm. Los mampuestos dorados, de 20 a 70 cm, y los oscuros, de 10 a 45 cm.
- El color y la luz frente a la foto.
- Que el juego siga a más de 50 fps en la zona y que no aparezcan errores.
