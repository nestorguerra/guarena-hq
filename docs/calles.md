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

## Pendiente

- Las calles de las zonas Norte (21), Sur (11) y Oeste (4), con las mismas instrucciones (`AMPLIACION.md`: perfil y
  casas en un solo paso, en grupos de 4–5 calles).
- Lo que el estilo de una calle aún no sabe dibujar: soportales bajo los bloques (Gerardo Diego), naves con cubierta
  de chapa roja, setos altos de arizónica, vallas de barrotes entre pilares, la cal desconchada de las casas de labor,
  las medianas de las calles que el mapa tiene como una sola calzada (Don Benito, Alberquilla), anchos de calle que el
  mapa da mal (Camino del Gamero: 10–11 m reales, 5,5 en el juego) y los nombres que el mapa da cambiados (la rama sur
  de la Cuesta se llama Bronca; el tramo de la vista 17, Nueva).
- En Realista el asfalto medido ya toma su color; la textura fotográfica de los demás sigue oscura.
