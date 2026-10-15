# Las calles del casco antiguo, como son

Petición del usuario (12 de octubre de 2026): «he incluido en la carpeta de Guareña que está en el escritorio imágenes
de las calles de Guareña capturadas… ve calle por calle analizando estas fotografías y utiliza las mismas texturas,
objetos y elementos arquitectónicos que veas en las fotografías, en los edificios y fachadas que correspondan, dándole el
realismo necesario para que realmente sean exactamente iguales las calles que tenemos modeladas nosotros con las
reales». Y en el mismo mensaje: «que el estilo plastilina quede muy realista».

## Las capturas

`~/Desktop/Guareña`: capturas de Google Maps (Street View y vista 3D), una carpeta por calle o plaza, con
`indice_capturas.json` y una `GUIA_Y_FUENTES.txt` en cada carpeta (enlace, fecha y encuadre de cada imagen). Al
principio eran 127 capturas de 22 calles y 4 plazas; la carpeta ha seguido creciendo con más calles.

**Son de Google: solo referencia.** Sus condiciones no permiten copiar sus píxeles, y la regla del proyecto tampoco
(«en el juego no entra ni un píxel de ninguna foto»). Todo lo que pasa al juego son números y palabras: colores
medidos, alturas, tipos de zócalo, de reja, de puerta… y la textura de cada cosa se hace aquí, como siempre. Las hojas
de comparación con las capturas se guardan fuera del repositorio. (Como en la calle Malfeitos: `docs/malfeitos.md`.)

## El método

1. **Las cámaras** (`tools/fachadas/capturas.py` → `.cache/calles/poses.json`, fuera del repositorio): de cada enlace de
   Street View, la posición, el rumbo, la inclinación y el campo de visión, en metros del juego. Las capturas tienen 90°
   de campo vertical, también las de enlace `api=1`, cuyo `fov` no es lo que muestran (medido con la forma redonda de
   las tapas de registro). Cada vista conserva su número aunque la carpeta crezca (por carpeta y fichero; las nuevas,
   detrás). El GPS de Google deja muchas cámaras a varios metros (dentro de una casa, pegadas a una fachada, en la
   calle de al lado; las `api=1` dan el punto pedido, no el de la panorámica): los agentes que identifican las casas las
   recolocan cuadrando esquinas y medianeras con el mapa, y `tools/fachadas/camaras.py` las junta en
   `.cache/calles/camaras.json`, que `tools/callelab.js` aplica.
2. **El juego desde la misma cámara** (`tools/callelab.js`: `CL.shot(id)`, `CL.some(ids)`, `CL.folder(calle)`): para
   poner cada captura junto a lo que hoy se ve en el juego.
3. **Qué edificio es cada fachada** (`tools/fachadas/lados.py` → `.cache/calles/lados.json`): a cada lado del eje de
   cada vista, los edificios del Catastro en orden, metro a metro.
4. **Los perfiles de cada calle**: mirando todas sus capturas y midiendo colores en zonas al sol y a la sombra, una
   descripción de lo que domina en la calle (pinturas, zócalos, recercados, rejas, balcones, puertas, persianas,
   remates, faroles, suelo) y de cada fachada que se ve bien. Los hicieron varios agentes en paralelo, con un esquema
   común.
5. **El estilo de cada calle** (`tools/fachadas/estilos.py` → `src/calles_estilos.js`): de los perfiles, con reglas que
   pasan sus palabras a los parámetros del generador de fachadas. Los retoques a mano van en `MANUAL`, dentro de la
   misma herramienta, para que no se pierdan al regenerar.
6. **Casa por casa** (`tools/fachadas/casas.py` → `src/calles_casas.js`): cada fachada descrita en los perfiles, con el
   número de su edificio (leído en la captura con los números escritos encima) y lo que se ve de ella. Solo pasan las
   identificadas con confianza alta o media.

## En el juego

- `src/calles.js`: a qué calle o plaza da cada edificio (por los metros de fachada que dan a ella; las dos plazas de
  Santa María, que no tienen calle propia en el mapa, por su lado respecto a la iglesia), y el estilo de cada casa: el
  de su calle, sorteado con su semilla, y encima lo visto de ella si está en `calles_casas.js`.
- `buildings.js`: el tipo de casa, la pintura exacta medida y un **zócalo propio** por casa (color, altura y tipo:
  pintado, granito en placas, piedra, azulejo, cemento o ninguno), dibujado por el sombreador de los edificios
  (`aZoc`); el **pretil** ante el tejado en las casas que lo tienen (desde la calle, el pretil blanco y su albardilla, no
  la fila de tejas).
- `facades.js`: rejas (cuántas, color, de panza), recercados (pintados o de granito), carpintería, persianas, puertas,
  balcones, cocheras y macetas como en su calle; las **tapias** vistas en las capturas, ciegas y con su portón.
- `ground.js`: el suelo de cada calle, en su color medido: asfalto (viejo, gris claro y cálido casi siempre: `roadCol`),
  adoquín en hileras, losas en plataforma única sin bordillos, o adoquín en plataforma; por tramos donde la calle cambia
  (`tramos`: la Estacada, adoquín solo hasta Malfeitos; Pajares, Túnel, Cañadilla), sin líneas de carril (las calles
  reales no tienen ninguna marca). Y su acera, del bordillo a las fachadas (`acera`: su color y su baldosa), dibujada en
  el material del suelo, por tramos y por lado si cambia: en Malfeitos, la hidráulica blanca y roja en damero al norte,
  roja con cadeneta de rombos blancos junto a Correos, blanca con dos hileras rojas junto al bordillo en el lado este
  del tramo sur y gris en el oeste.
- Los espacios abiertos junto a las calles (plazas, delante de la iglesia, cruces anchos) pavimentados; la tierra de
  los solares, solo dentro de las manzanas (a más de 12–18 m de una calle). Sin el empedrado que la plastilina ponía en
  todas las calles alrededor de Santa María (eran de asfalto).
- `buildings.js`: el ladrillo visto y la piedra, en su color medido (rojo en el casco, ocre y crema en los bloques de
  los años 70–90); una casa vista pintada no hereda el ladrillo que le tocara en el sorteo de su calle. Las **hileras
  de adosados** que el mapa tiene como un solo edificio largo (`adosados`: en los barrios nuevos, promociones enteras de
  casas de 6–6,5 m registradas juntas), cada casa con su pintura y su zócalo de los de su calle.
- `mapdata.js`: **cada volumen con la planta en la que está.** El Catastro da las construcciones de un edificio al
  edificio entero, y el mapa las enlazaba a su primera planta: un edificio de varias plantas separadas (una hilera de
  adosados, los bloques de una promoción) se dibujaba entero con el estilo de la primera, y lo visto de las otras en
  las capturas no llegaba a su casa. Era una cuarta parte de los volúmenes (2.147 de 8.570); las casas medidas de
  Malfeitos no cambian.
- `vegetation.js`: los árboles de alineación, solo donde las capturas los muestran, de su especie y su edad
  (`arboles`: los naranjos jóvenes en alcorques de la calle Grande; los plátanos del tramo de la Estacada junto a Don
  Benito); en las demás calles analizadas, ninguno; y en sus plazas, solo los que se ven (la de Abastos es un espacio
  abierto, no una arboleda). Los jardines vistos, con su suelo y sus especies (`parque`: el de la plaza García Lorca, de
  albero sin césped, con árboles grandes de copa ancha y un cedro, sin palmeras).
- `world.js`: las farolas, faroles en la fachada o de columna en la acera según las capturas (`lamps.kind`: en los
  barrios nuevos del Este, de columna).
- `buildings.js`, además: las plantas que se ven (`floors` en las casas: el Catastro a veces cuenta una de más o de
  menos) y el color visto de las naves (de bloque crema o blanco, no de chapa gris).
- `townplus.js`: las medianas con sus árboles donde las capturas las muestran (`mediana`) — solo donde el mapa tiene
  dos calzadas de verdad; Don Benito, Alberquilla y Castillejos son en el mapa una sola calzada ancha y no la tienen.
- `ground.js`: las rayas de la calzada (línea central, aparcamiento) solo donde las capturas las muestran (`lineas`).
- `world.js`: los faroles de forja en ménsula, a la distancia que se ven en cada calle y a la altura de la primera
  planta; ninguna farola de báculo en estas calles.
- `streetlife.js`: las macetas, las pocas que hay.

## La plastilina, realista

Los colores de la plastilina se habían ajustado a las primeras imágenes de referencia del usuario (retocadas), y todo
tiraba a melocotón y naranja: la cal salía salmón. Desde el 12 de octubre:

- Paredes: el sombreador de la plastilina ya no tiñe (`CLAY_WALL` en `plastilina.js`, neutro).
- Luz de día: sol algo cálido y sombra con luz de cielo (`sky.js`, `CLAY`); gradación neutra (`PLASTILINA.grade`).
- Paletas de la cal, los colores, los zócalos y los recercados, las de las capturas (`buildings.js`, `textures.js`,
  `facades.js`).
- Calzada gris (no rosada), aceras de baldosa gris (no arena ni rosa), bordillos finos (no bloques de 42 cm).
- Sin las exageraciones de las primeras imágenes: rejas en casi todas las ventanas, recercados de arenisca en casi
  todas las puertas, macetas en casi todos los alféizares; ni los cantos rodados oscuros en plazas y espacios abiertos
  (ahora losas claras de granito, baldosa y, en los solares, tierra), ni las losas de arenisca del albero.
- Paredes más lisas, como el enlucido de las capturas (`CLAY_RELIEF` 1,0).
- La iglesia: mampostería de granito gris pardo y sillares grises, con su mortero de cal gris (`clayStones`), no cantos
  ocres y naranjas en un lecho crema.

## Lo que quedaba del centro (13 de octubre)

- **El atrio de Santa María** (`src/atrio.js`): la plataforma enlosada de granito al sur de la iglesia, del muro sur a la
  acera de la Cuesta y de la calle de Santa María a la escalinata del lado este; su muro de contención color arena con
  albardilla de granito, la verja de forja con aspas entre pilares de granito, la cruz de granito sobre su pedestal de
  tres gradas, las farolas de fundición de dos brazos y sus dos pinos. Medido en el sistema de la iglesia (`churchFrame`)
  con la ortofoto del PNOA y las calles del mapa.
- **Plaza Vieja**: su parque como es (`parque`: césped seco, naranjos, un olivo, palmitos jóvenes y un árbol grande) y
  la ermita del lado este (edificio 1260: muros ciegos encalados, una planta alta; `landmarks.js` `ermitaPlazaVieja`: su
  portada barroca de granito mirando al parque y la espadaña con campana y cruz junto a la esquina de Fuentes).
- **El bulevar de Castillejos** (`bulevar`): la mediana peatonal de adoquín de hormigón claro con bordillo, árboles
  jóvenes y bancos, por el eje de la calzada ancha sin nombre que el mapa tiene a su lado (`ground.js`, `townplus.js`).
- **Las tapias** (`src/tapias.js`): los huecos de 2,5 a 30 m entre dos casas de las calles del centro, cerrados con su
  tapia encalada, zócalo gris y portón; y las siete tapias largas que las capturas enseñan donde el mapa no tiene nada
  (`tools/fachadas/tapias.py` → `src/calles_tapias.js`: la de piedra de la Cuesta, la de ladrillo de Hornillos, el muro
  alto ocre de Fuentes, las de Pozo Dulce y Pozo Pajares…).
- **El Ayuntamiento** como en su foto: siete ejes (tres arcos del soportal y cuatro vanos adintelados de granito), el
  balcón corrido en los tres centrales, recuadros ciegos con farol sobre los arcos laterales, un balcón en cada extremo,
  la cornisa con una bola sobre cada eje y el ático del reloj con volutas, frontón partido, pináculo y flameros (sin la
  espadaña con campana, que no tiene); sin naranjos delante, donde están las terrazas.
- **El ramal sur de Eugenio Frutos** (sin nombre en el mapa: `calles.js` `NOMBRES`), de asfalto casi blanco con
  aceras; las esquinas de baldosa roja de la Estacada con Malfeitos y de la Cuesta frente a Cuatro Esquinas.
- Las arboledas que el juego ponía en todas las plazas, solo donde las capturas las muestran (la Plaza de España sí).
- **El soportal del Ayuntamiento**, transitable: la planta baja retranqueada 4,2 m tras los tres arcos (galería con su
  techo y vigas, faroles), las puertas al fondo y la puerta principal, la del interior (`landmarks.js` `ayuntamiento`).
  Trampa: un frutal «de corral» que antes quedaba oculto dentro del macizo salía en la galería — las plantaciones de los
  patios miran también `claims` (`vegetation.js`).

## Lo que el estilo aún no sabía dibujar (13 de octubre)

- **Soportales bajo los bloques** (`calles_casas.js` `soportal: { fondo }`; `buildings.js` `markArcade`,
  `arcadeShell`, `arcadeCollider`): en los frentes a la calle de los bloques de 1983 de Gerardo Diego (457) y Miguel
  Hernández (458) la planta baja se mete 2,6 / 2,4 m tras pilares cuadrados de 42 cm, uno por crujía (3,2 m), bajo el
  techo del primer piso; pilares y pared del fondo con la pintura del zócalo visto (terracota, ocre); solo donde la pieza
  tiene fondo (las franjas de balcones conservan su muro). Se entra entre pilares, se pasea a lo largo y las puertas
  quedan al fondo. Trampa: la «red de seguridad» del jugador (`player.js`: si pasa un segundo dentro de un edificio lo
  saca a la calle) lo expulsaba del soportal; el índice de «dentro de un edificio» usa ahora la planta con los
  soportales recortados (`p.walkRing`, `mapdata.js` `useDrawnParts`, rehecho tras el bucle de las piezas).
- **Cubiertas de chapa roja** (`cubierta: { col, calle?, una?, alto? }`): capa de chapa del tejado de nave teñida del
  color visto, un tercio más oscura que el color leído en una fachada (en una vertiente abierta al cielo salía rosa).
  La nave de Gerardo Diego (294): fachada ciega (`ciega`) de 4 m y tejado a dos aguas con la cumbrera paralela a la
  calle a media profundidad, la vertiente de la calle a 24° para que se vea por encima del muro, como en su captura
  (`buildings.js` `streetRoof`, para cualquier planta: cada vertiente es la mitad del contorno a su lado de la
  cumbrera). Las de la carretera de Manchita (141), Alberquilla (97), Palacios (1914) y la caseta del aparcamiento de
  Santa María (2783), granates o rojizas a dos aguas.
- **Setos altos de arizónica**: en la lista de las tapias largas (`tapias.py`, material `seto`): Antonio Machado al sur
  (2,5 m) y alrededor del jardín del bloque 502 de El Chiriveje (2,2 m); `tapias.js` los planta con las piezas de seto
  recortado (`trees.js` `seto`) de punta a punta, de su altura y su verde oliva, y los cierra como un muro.
- **La cal desconchada** (`desconchada`: en cada casa vista `[nivel 1–3, 'ocre'|'gris'|'blanco']`, o una parte de las
  casas de la calle — Atrás, Hornillos, Fuentes, Bronca): en el sombreado de las fachadas (`materials.js`), manchas de
  bordes rotos donde la cal se ha caído, sobre todo al pie del muro, que enseñan el enfoscado ocre y la tierra, el
  mortero gris o el enlucido blanco bajo una mano de color. Va en las centenas del atributo del zócalo (`aZoc.w`).
- **Las medianas** (`tools/fachadas/medianas.py` → `src/calles_medianas.js`): la de Don Benito, medida por las copas de
  sus árboles en la ortofoto (ajuste de segundo grado, 0,37 m de error medio): el mapa dibujaba sus dos calzadas de
  sentido único encima de la mediana, 14–17 m de ancho cada una, y el tráfico circulaba por la fila de árboles. Ahora
  `mapdata.js` lleva cada calzada a su lado (`CALZADAS`: 6 m, acera solo del lado de las casas, coches aparcados ahí,
  `fleet.js` `parkOnly`), sus extremos en sus cruces; la mediana (`bulevar` en piezas, con asfalto debajo de cruce a
  cruce): 2,2 m de adoquín gris claro y los últimos 30 m del este de baldosa roja, plátanos de sombra y ciruelos de hoja
  roja alternos, farolas de báculo galvanizado de 9 m con un brazo hacia cada calzada cada 30 m; sin farolas en las
  aceras. La de Alberquilla: el mapa sí tiene sus dos calzadas; la búsqueda de la mediana (`townplus.js` `avenida`)
  buscaba siempre la otra calzada de la Avenida de la Constitución — corregido; seto bajo y moreras jóvenes.
- **La caseta del aparcamiento de Santa María** (edificio 2783, vista 7): el Catastro le da una planta en L de ~30 m con
  una pieza de dos plantas tendida sobre la calle Pozo Pajares, y el juego levantaba ahí una nave alta. Medida en tres
  vuelos del PNOA: un rectángulo de 13 × 8,6 m de una planta (3,2 m) con su tejado a dos aguas de chapa rojo óxido a lo
  largo (`calles.js` `PLANTAS`: `mapdata.js` le cambia la planta y deja «gone» sus otras piezas, que no se dibujan, no
  se sueldan ni tapan grietas — `world.js` `skipPart`, `solidez.js`).

## La auditoría y sus correcciones (13 y 14 de octubre)

`docs/auditoria-calles.md`: 292 vistas de las capturas comparadas con el juego desde la misma cámara, 2818
discrepancias (341 graves, 1599 medias, 878 leves) y 45 vistas con la cámara mal situada. Se corrigieron calle a calle
con agentes que solo escriben datos (perfil, casas, arreglos) y repasos sucesivos cada vez que el juego aprendía a leer
algo nuevo; los monumentos y lo que faltaba, en código.

- **Las cámaras** (`.cache/calles/camaras.json`, `tools/fachadas/camaras.py`): las 45 de la auditoría y otras que los
  correctores vieron desviadas, recolocadas por resección (medianeras y esquinas del mapa en sus columnas de la
  captura, 3–5 puntos, error de 0,4 a 10 px). Antes de reajustar una vista se «sellan» sus arreglos con la cámara vieja
  (`camara` en cada item) para que no se muevan.
- **Arreglos** (`tools/fachadas/arreglos/<calle>.json` → `src/calles_arreglos.js`, cabecera de `arreglos.py`): tapias,
  árboles, suelos, pasos, bordillos amarillos, farolas (pared, columna, báculo, fernandino, globo, seta), señales con sus
  placas, contenedores, bancos, bolardos, aparcamiento en cordón o batería, el ancho de la acera y la distancia del
  bordillo al eje (`acera`, `calzada`), y para quitar lo que el juego ponía de más: `sin_senales`,
  `sin_contenedores`, `sin_farolas`, `sin_relleno`, `sin_vado_amarillo`, `sin_postes`. Lo que faltaba en el pueblo:
  `casa` (una casa que el mapa no tiene), `relleno` (la casa inventada de un hueco, pintada y con sus plantas),
  `silos`, `deposito` (de agua), `terraza` (mesas con sombrillas o toldo), `cable` (de fachada a fachada). Todos admiten
  `lateral`: a tantos metros del eje de la cámara, lejos de la calle (una mediana, el fondo de un solar). En el
  `calle` de cada fichero: `firme` (asfalto liso o gastado), `aristas` (tramos sin nombre que son de esa calle),
  `bordillo` (su color), `cables` (tendido por todas sus fachadas) y `tramos` con su propio pavimento.
- **Casas** (`calles_casas.js`): además de lo de antes, `fachada`/`fachadas` por calle (`frente`), `teja`, `alto`,
  `placas`, `soportal` con `arcos` de medio punto, `bajantes`, `muros` (el color de un frente a otra calle),
  `pinturas` (varias casas de colores en un solo edificio del Catastro, de izquierda a derecha con sus metros),
  `aires`, `antenas`, `parabolica`, `cables`, `rotulo` (letrero sobre la planta baja o en banderola, con su texto),
  `buzones` y `cerramiento.fondo` (la verja de un jardincillo que el mapa no deja). `src/detalles.js` dibuja los
  cables, rótulos, antenas, buzones, silos, depósitos, cables cruzados y terrazas.
- **Lo que faltaba del mapa y del pueblo, por fin (14–15 de octubre)**: el frente de un edificio movido hacia la calle o
  hacia atrás donde el Catastro lo pone mal (`mover_frente`, `mapdata.js`), el eje, el ancho y las aceras de un tramo de
  calle sin tocar sus cruces (`calzadas`), el bordillo a una distancia del eje (`acera.calzada`), firme, pavimento,
  rayas y color de senda por tramo (`tramos`); casas que el mapa no tiene (`casa`) y las inventadas pintadas o quitadas
  (`relleno`, `sin_relleno`); en las casas `muros` y `pinturas` (colores por frente y por casa de un mismo edificio),
  `toldo`, `cierro`, `celosia`, `mural`, `pergola`, `chimeneas`, `reja_hex`, `barandilla` (balaustres, forja),
  `arcos_puertas`, `arcos_ventanas`, `cochera`, `rotulo` (con `pos`, en banderola, también en naves), `antenas`,
  `parabolica`, `aires`, `cables`, `buzones`, `ropa`, `atrezo` (sin objetos ni bicicleta a la puerta) y
  `cerramiento.fondo`; y los arreglos de piezas: silos, depósitos, terrazas, cables y banderines (a lo ancho o a lo
  largo), postes y torres de celosía, espejos, mástiles, placas de calle, carteles, escalones con borde pintado, plazas
  azules, tapas y rejillas, marcas y bandas en la calzada, semáforos, bajantes, sierras en el horizonte; y para quitar lo
  que el juego ponía de más: señales, contenedores, farolas, postes y su tendido, placas, bancos, la valla de un colegio,
  la terraza de un bar, el buzón de Correos. Todo en `src/detalles.js`, `facades.js`, `buildings.js`, `ground.js`,
  `streetlife.js`, `world.js` y `schools.js`, leído de `calles_casas.js` y `calles_arreglos.js`.
- **Más fallos de fondo**: la Avenida de la Constitución recibía su mediana dos veces (dos juegos de árboles y farolas);
  sus farolas son ya grises de un brazo curvo (`mediana.farolas` `baculo1`), como las de la Plaza de España, grises de
  fundición sobre un banco redondo de piedra.
- **Monumentos** (`landmarks.js`, `atrio.js`, `churchdoors.js`): la iglesia con su muro norte en un solo plano hasta la
  cornisa y la torre de 41,5 m con chapitel de piedra; el atrio con su contorno medido, muretes de 1–1,6 m, verja de
  aspas y una encina; el Ayuntamiento abierto al este por la galería, con su lateral de revoco, el arco de 3,1 m, sus
  impostas, ventanas y jambas de granito.
- **Fallos que salieron al comparar**: las naves no tomaban nunca el color visto (su chapa no estaba marcada como
  pintable en `textures.js`); la plastilina abría una rendija de arriba abajo en las esquinas poco cerradas (cada arco
  de esquina en 6 trozos de menos de 5 cm, que las paredes descartaban: `roundRing` los hace ahora de 7 cm como mínimo).

## La revisión final (15 de octubre)

Antes de publicar, cada vista se miró una vez más (captura arriba, juego abajo, desde la misma cámara) buscando solo lo
que cualquiera vería al jugar: cámaras mal puestas, piezas rotas, cosas inventadas o grandes ausencias. Lo que salió:
- **Muros que cerraban calles**: una tapia medida a 40 m de su cámara (vista 212) cruzaba la calle Severo Ochoa. Ahora
  `arreglos.py` recorta toda tapia que cruce el eje de una calle a lo ancho, lejos de sus extremos (donde sí cierra un
  fondo de saco): se recortaron 5 (los setos no: los de las medianas llegan hasta sus cruces). Y un seto medido desde
  una cámara que el juego tiene en otro sitio ya no deja un muro invisible donde cae sobre una calzada (sus piezas no se
  plantan en el asfalto, pero su choque sí quedaba: en la carretera de Don Benito, la calle Almendralejo, la de Oliva).
- **Fachadas leídas que se perdían**: una fachada leída con huecos de menos de 1,4 m en su muro se descartaba entera
  (42 casas). Ahora se juntan los huecos vecinos (una puerta antes que una ventana, una ventana antes que un paño ciego):
  se aplican 430 de las 487 leídas, antes 397. Una casa vista sin tienda en su planta baja (sin `T`) ya no recibe un
  escaparate porque el mapa tenga un comercio en ella (la chapa ondulada de la calle Túnel, vista 92). Las naves admiten
  huecos de hasta 8 m: sus pocos portones a lo largo de todo el muro.
- **La mediana de El Rollo** (vistas 154–156): el mapa tiene sus dos calzadas de un sentido una encima de otra, como
  tenía las de la calle Don Benito; `medianas.py` las separa ahora también a 3,8 m de su eje y tiende su bulevar de
  arbolitos (moreras y ciruelos de hoja morada) y farolas de dos brazos, cortado en cada cruce, sobre la hilera de copas
  que se ve en el PNOA.
- **Las sierras lejanas** salían rayadas de negro y, vistas desde otra calle, como un bloque: la oclusión de contacto
  (AO) se calculaba también a 3,8 km, donde la profundidad ya no tiene precisión (ahora se apaga entre 400 y 900 m), y su
  cresta acababa en seco (ahora baja hasta la llanura). La de la vista 269 se quitó: 76 px de cresta a 3,8 km, un monte
  de 12° que ninguna otra captura tiene.
- **Piezas sueltas**: dos señales en mitad de un paso de cebra (vistas 9 y 29), un farol y una bajante colocados en el
  aire (`lateral` sobre el eje de la cámara, vistas 17 y 69), una celosía gigante (vista 33), la «barandilla» de una
  azotea hecha celosía flotante (vista 168), dos palmeras de más (vista 241), un parpadeo de dos calzadas superpuestas
  (vista 288: la arista 720 toma el estilo de su carretera).
- **Montajes con carteles**: algunos agentes imitaron con carteles un frontón (vista 243), un zócalo (vista 35) o el
  remate de una tapia (vista 63); desde otra cámara flotaban o dejaban postes como tuberías. Se quitaron, y un cartel
  pegado a una pared ya no lleva postes: cuelga de ella.
- **Calzadas que parpadeaban**: dos calzadas del mismo tipo superpuestas (una carretera y el ramal sin nombre que el mapa
  tiende sobre ella) se pisaban en escalera blanca; ahora la del color de su calle queda un pelo por encima, y los
  ramales y la EX-105 toman el firme de la carretera a la que se unen (vistas 286–288).
- **Casas que el Catastro da por naves**: `nave: false` en su ficha las dibuja como casas (vista 43: una casa
  reformada salía de chapa ondulada).
- **Lo que faltaba**: los muros de las vistas 213 y 273, la caseta del transformador de la vista 133 (`casa` admite
  ahora `de`/`a`, de punto a punto, para un edificio exento), el silo de cereal de la calle Almendralejo (vista 276: la
  franja oeste de su parcela, partida y subida a 26 m, medida por su sombra en el PNOA y el ángulo de su cima). El muro
  curvo de sillería de la Rotonda del Arroyo (vista 238), la isleta ajardinada de la calle Julia Mayoral (vista 130).
- **Lo que queda**: en la vista 114 la cámara del juego va por la calzada principal de la carretera de Don Benito y la
  captura por la vía de servicio paralela, que el mapa no tiene: su seto no puede ponerse; el soportal del
  Ayuntamiento en la calle Túnel (vista 93) se dejó como está (la captura es de 2009).

## Pendiente

- Las calles de las zonas Norte (21), Sur (11) y Oeste (4), con las mismas instrucciones (`AMPLIACION.md`: perfil y
  casas en un solo paso, en grupos de 4–5 calles).
- Lo que el estilo de una calle aún no sabe dibujar: vallas de barrotes entre pilares, anchos de calle que el mapa da
  mal (Camino del Gamero: 10–11 m reales, 5,5 en el juego) y los nombres que el mapa da cambiados (la rama sur de la
  Cuesta se llama Bronca; el tramo de la vista 17, Nueva).
- En Realista el asfalto medido ya toma su color; la textura fotográfica de los demás sigue oscura.
