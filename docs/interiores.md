# Interiores de alta densidad (épica I del backlog técnico)

Cada local del pueblo (bar, cafetería, tienda, banco, farmacia, gimnasio…) se amuebla desde un **kit**: un JSON que
dice el tamaño del local, sus zonas, sus tabiques y, zona por zona, qué objetos del **catálogo** van allí, cuántos y con
qué regla. El juego lo monta con la semilla del local (`src/locales.js`, `buildLocal(kit, semilla)`): la misma semilla da
siempre el mismo local, y otra semilla da otro distinto. Un validador comprueba cada kit con varias semillas.

La referencia es la **cafetería** (`data/kits/cafeteria.json`) y su hermano el **bar** (`data/kits/bar.json`), con el
catálogo de hostelería (`tools/interiores/catalogo_hosteleria.py`). Para empezar un kit nuevo, léelos enteros.

## Ficheros

| Qué | Dónde |
|---|---|
| Catálogo de una familia (el script es el modelo) | `tools/interiores/catalogo_<familia>.py` → `data/objetos/<familia>.json` |
| Esquema de un objeto | `data/interaction.schema.json` |
| Rangos de masa por clase y categoría | `data/mass_ranges.json` (una familia puede traer los suyos en `"categorias"`) |
| Kit | `data/kits/<kit>.json` (el nombre del fichero es el id del kit; varios kits pueden ser de la misma tipología) |
| Esquema de un kit | `data/kits/kit.schema.json` |
| Texturas pintadas de una familia | `src/texturas/<familia>.js` (`tipo → { w, h, draw(ctx, w, h, tex, seed) }`) |
| Datos para el juego (no se editan) | `src/interiores_datos.js`, que escribe `tools/interiores/datos.py` |
| Montaje | `src/locales.js`; geometría compartida con el validador: `src/interiores_geo.js` |
| Validador | `tools/interiores/validar.py` (+ `validar.js`) → `data/interiores/validacion/<kit>.json` |
| Fotos de prueba | `tools/interiores/lab.js` → `.snaps/int_<kit>_<semilla>_<etiqueta>_<k>.jpg` |
| Inventario de interiores (I-01) | `tools/interiores/inventario.py` → `data/interiors_inventory.json` |

## Un objeto

Un objeto es un puñado de primitivas en metros, en su propio marco: **x** a lo ancho, **y** hacia arriba desde su pie
(y = 0 es el suelo o la superficie donde se apoya), **z** hacia su frente (+z mira a quien lo usa; la espalda en −z).
Primitivas: `caja(an, al, fondo)`, `cil(radio_arriba, radio_abajo, alto)`, `esf(radio)`, `cono(radio, alto)`,
`plano(an, al, tex=…)` (un dibujo: cuadro, pantalla, pizarra, etiqueta). Cada pieza lleva color (`c`) y material (`m`).
Una pieza con `luz=True` brilla (lámparas, pantallas); una lámpara de techo (soporte `techo`) con una pieza de luz
recibe una luz puntual en el juego.

- **Escala real** en centímetros: una taza mide 6,5 cm, una barra 1,07 m de alto, una puerta 2,1 m.
- **Nada por debajo del pie** (salvo lo que cuelga del techo: sus piezas van en y negativa desde el techo).
- **Superficies** (`superficies=[{'y': …, 'margen': …}]`): donde se ponen cosas encima, a la altura de lo alto de una
  pieza (el validador lo comprueba). Una balda de estantería lleva `fondo` (se llena en fila desde un extremo).
- **Clase de interacción por masa** (X-01): PICKUP < 5 kg, CARRY 5–25, PUSH 25–80, PUSH_HEAVY 80–400, FIXED > 400 o
  anclado, con `motivo_fijo` (anclado en la realidad, estructural, rendimiento, diseño). Una excepción a la masa, con
  `motivo_clase`. Modificadores: `SEAT` (con `asientos`), `USE`.
- La **masa** dentro del rango de su categoría (`data/mass_ranges.json`).
- **Calidad (I-07)**: id en minúsculas con `_`; como mucho 5.000 triángulos por objeto (más pediría niveles de detalle);
  colores con albedo físico: ni negro puro ni blanco puro en la pintura (`datos.py` avisa por debajo de `#262626` y por
  encima de `#f6f6f6`, salvo cristal, metal, piezas de luz y dibujos).

## Un kit

```json
{ "tipologia": "bar", "nombre": "…", "superficie": { "ancho": [6.6, 9.0], "fondo": [9.6, 13.5], "alto": 3.2 },
  "variables": { "xc": "W/2-1.95" }, "zonas": [ { "id": "sala", "publica": true, "rect": ["-W/2", "1.1", "xc-1.35", "D-3.7"] } ],
  "tabiques": [ { "de": ["-W/2+2.1", "D-2.4"], "a": ["-W/2+2.1", "D"], "puerta": [0.55, 1.0] } ],
  "libres": [ { "rect": [ … ], "nota": "el sitio para pedir" } ],
  "objetos": [ { "zona": "sala", "obj": "mesa_cuadrada", "regla": "conjunto", … } ], … }
```

Marco del local: la puerta de la calle en z = 0 (centrada, o en `puerta`), el fondo en z = D, x de −W/2 a W/2: las caras
de las paredes. Las expresiones usan W, D, H y las `variables`. Una zona que llega a un tabique termina en su cara
(el montaje lo ajusta solo). Las puertas de los tabiques, de **1 m** (pasa un cuerpo de 0,9 m).

Los objetos se colocan **en el orden del kit**: lo que tiene que estar sí o sí, primero; lo que cuelga de una pared
llena, antes que lo que la llena.

### Reglas

| Regla | Qué hace | Parámetros |
|---|---|---|
| `modulos` | Módulos de punta a punta en una línea (la barra, un mostrador): diseño del kit, no se mueven | `linea: [fijo, desde, hasta]`, `eje`, `mira` |
| `filas` | Filas de muebles de punta a punta, espalda con espalda, con pasillos (góndolas, islas) | `eje` (`z`/`x`), `pasillo` (1,2), `doble`, `margen` |
| `fila` | Una fila de cosas sueltas cada tantos metros (taburetes) | `linea`, `eje`, `cada`, `mira` |
| `contra_pared` | De pie contra una pared de la zona, una tras otra | `pared` (N/S/E/W), `cantidad` o `llenar` |
| `pared` | Colgado de una pared: al azar, en fila `cada` m, o encima de otro (`sobre_de`) | `pared`, `cantidad`/`cada` |
| `esquina` | En las esquinas de la zona que dan a pared | `cantidad` |
| `suelo_libre` | En el suelo, donde quepa | `cantidad` |
| `conjunto` | Una mesa con sus sillas alrededor (o por los lados que diga el kit, o ninguna), con pasillo | `variantes`, `sillas: { variantes, n, lados }`, `por_m2`/`cantidad`, `giro` |
| `sobre` | Encima de las superficies de otros (`en`) | `cantidad`, `por_m`, `por_soporte`, `relleno` (estanterías), `fraccion` |
| `vida` | Como `sobre`, lo que deja la gente (tazas a medias, el periódico) | igual |
| `techo` | Colgado del techo en rejilla | `cantidad`, `por_m`, `por_m2` |

Detalles útiles: `pared` admite una lista (`["N", "W"]`: si la primera está llena, la siguiente) y, en fila (`cada`),
`maximo`; `esquina`, sin esquina libre, se pone contra cualquier pared de la zona; `techo` admite `variantes`; `sobre` con
`relleno` sigue donde lo dejó otra entrada en la misma balda y prueba otra variante si una no cabe. Lo largo, antes que lo
pequeño: en una barra o un mostrador, la vitrina primero. Una pieza con dibujo marcado `rotulo_local` (un rótulo, la
pantalla del cajero) muestra el nombre del local donde está (`tex.titulo` en su textura).

`obligatorio: true` hace que el validador exija al menos uno. `variantes` + `todas: true` pone cada variante una vez
antes de repetir. `vende: "<id>"` (o una lista de ids de `src/items.js`) pone un punto de compra delante de las primeras
piezas de esa entrada, como en las tiendas hechas a mano: «Comprar … (precio)». `interaccion: { "type": "train",
"label": "Entrenar una hora" }` pone delante de ellas una acción del juego (en el gimnasio, entrenar).

### La gente (I-08)

`ambiente.clientela = { "maximo": 8, "horas": [[8, 11, 0.2], [20, 24, 0.55], …], "frases": ["…"] }`: en los asientos
(objetos `SEAT` con `asientos`) de las zonas públicas se sienta gente del pueblo, en la proporción de cada hora y nunca más
del máximo; algunos charlan y dicen de vez en cuando una de las frases. El dependiente o el camarero sale en
`puntos.dependiente`; `puntos.mostrador` es donde se pide (abre la lista del mostrador: lo que se vende y, en hostelería,
la carta).

### Lo que el montaje garantiza (y el validador comprueba, I-04)

- Todos los obligatorios y las densidades del kit.
- Nada flotando más de 1 cm; nada metido en otra cosa más de 1 cm.
- **Paso libre de 0,9 m** desde la puerta de la calle a cada zona pública: el montaje no pone nada que corte el paso.
- Luces: número y temperatura de color del kit; ninguna zona pública a oscuras.
- Presupuesto de rendimiento (`data/quality_budgets.json`): triángulos, mallas, luces.
- La misma semilla, el mismo local (hash); otra semilla, al menos un 30 % distinto.
- Al menos 40 objetos distintos (tiendas, farmacia, banco, oficina), 60 (hostelería, vivienda) u 80 (gimnasio,
  alimentación), y un moodboard de 10 fotos reales de Wikimedia Commons con autor y licencia.

## Las casas de los vecinos (vivienda por estancia)

Las casas (`src/houses.js`) conservan su plano —de pasillo, estrecha con pasillo lateral o de dos plantas—, su estilo
(antiguo, rústico, moderno, alegre, joven, lujo, bohemio) y su vecino (abuela, matrimonio, familia, estudiante, cazador,
músico, rico, agricultor, artista). Cada habitación, salvo pasillos y vestíbulos, se amuebla con el kit de su clase,
`data/kits/vivienda_<estancia>.json` (salon, comedor, cocina, bano, dormitorio, ninos, joven, estudio, despacho, musica,
trofeos, pintura, taller, costura, despensa, trastero), con el tamaño de la habitación, desde la puerta por la que se
entra, dejando libre el giro de sus puertas y sin nada alto ni colgado delante de sus ventanas. Una clase sin kit todavía
se amuebla como antes, a mano. Referencia: `vivienda_salon` (`tools/interiores/kits_vivienda.py`,
`tools/interiores/catalogo_vivienda.py`).

- **Una sola zona**, `estancia`, toda la habitación: el kit no sabe dónde caen la puerta ni las ventanas. Por eso las
  reglas de pared admiten `pared: "*"` (cualquiera de las cuatro) y hay dos reglas de relación: `enfrente` (contra la
  pared de enfrente de la de `de`: el sofá frente a la tele; si no cabe, contra otra) y `entre` (entre `a` y `b`, mirando
  como `b`: la mesa de centro, la alfombra; si no cabe, donde quepa).
- **Para quién**: `perfil: [...]` y `estilo: [...]` (o `["!abuela", ...]` para excluir) ponen una entrada solo en esas
  casas. `botin: "<id>"` (de `LOOT` en `src/houses.js`: joyero, colchon, cartera, reloj, consola, portatil, hucha, movil,
  guitarra, altavoz, vinilos, rifle, jamon, prismaticos, cajaFuerte, cuadro, lata, garrafa) solo se pone si el vecino tiene
  esa cosa, y la primera pieza que pone es el botín (su propia malla, que desaparece al cogerlo). Si no cabe, el botín
  vuelve al montón y la casa lo deja en una mesa. Las entradas con botín, `cantidad: [0, 1]`.
- **El papel de cada mueble** (`rol` en el objeto) es lo que usa la vida de la casa: `sofa`, `sillon` y `silla` (sus
  `asientos` son sitios donde se sienta la gente), `mesa`, `cama` y `cama_doble` (donde duermen; bajo el colchón de una
  doble, los ahorros), `tv` (con una pieza `aparte: true`, la pantalla que se enciende), `cocina` («picar algo», donde
  cocinan), `nevera`, `armario` (esconderse), `comoda` (registrar los cajones), `espejo`, `piano`, `guitarra`, `libros`,
  `telefono`, `chimenea`. Una habitación con camas, un dormitorio sin `cama` deja a la familia sin dormir.
- **El estilo de la casa**: una pieza con `tinte: "tela"` toma una de las telas del estilo; con `tinte: "madera"`, su
  madera.
- La altura de las casas es menor (2,75 m arriba): nada más alto de 2,4 m.

Comprobación: `validar.py vivienda_<estancia> --semillas 1,…,81` prueba 81 semillas. El informe identifica el perfil,
estilo y contexto de dormitorio de cada semilla; no son 81 hogares distintos. `validar.py --casas 200 --exigir-todas`
construye 200 casas y exige kit en cada habitación habitable. Una habitación que vuelve al constructor anterior o
falla al montar nunca puede dar un informe de aceptación verde. `--casas-pueblo --exigir-todas` usa las 22 puertas
reales de vecinos. Annie conserva constructor propio: cinco estancias por kit y un dormitorio personalizado, con validación específica en las pruebas de contrato e integración.
Para verlas: `python3 tools/interiores/fotos_casa.py <tipo> 3` (tipos de `src/houses.js`: salon, cocina, bano, dorm,
dorm2, ninos, dormJoven, comedor, estudio, despacho, musica, trofeos, taller, costura, despensa, trastero).

Las viviendas conservan `paso_libre: 0.8`; el acceso predeterminado de un comercio es de 0,9 m. No se agrandan las
puertas para que quepan muebles. La regla `junto_a` relaciona módulos y acompañantes; `sobre_de` cuelga el espejo en
la pared del lavabo. `habitacion` distingue `dorm` y `dorm2`; `area_min`/`area_max` reservan variantes amplias para
salas que las admiten. `preferir` intenta la cantidad máxima sin convertir una pieza opcional en obligatoria.

El montador doméstico conserva acceso a los muebles funcionales y puede probar hasta doce distribuciones
deterministas si una puerta impide colocar un obligatorio. La semilla definitiva queda en el informe. Los puntos de
uso y de despertar se sitúan en suelo alcanzable; el botín sin superficie accesible puede quedar junto a ella en el
suelo, sin duplicarse. Las correcciones de acceso pueden cambiar distribuciones anteriores, pero la misma entrada
vuelve a producir la misma casa.

Se miden triángulos, mallas visibles, luces y tiempo de construcción de la casa entera. `integracion.py` mide además
la entrada real, arranque y recarga de partida, con datos ficticios en un contexto privado del navegador de ensayos.
No escribe partidas de usuarios. La iluminación de la vivienda conserva el color de su estilo y registra la
intensidad y alcance reales; el índice de cobertura pondera esa intensidad respecto a la lámpara de laboratorio.
Ese índice no es una medición fotométrica de lux y no sustituye la revisión visual.

`src/casa_lotes.js` agrupa geometría estática y dibujos de canvas de las viviendas para respetar el presupuesto de
mallas. Cada puerta mantiene su pivote; botín, ventanas y pantallas de televisión conservan sus mallas mutables.
El atlas y los materiales del lote se liberan al salir de la casa. Annie usa también los lotes estáticos; se conservan sus puertas, TV y luminarias controlables. Los locales conservan sus constructores.

Ensayos de integración:

```bash
python3 tools/interiores/casas_pruebas.py --tanda 5
python3 tools/interiores/validar.py --casas 200 --exigir-todas
python3 tools/interiores/integracion.py --colisiones
python3 tools/build.py
python3 tools/interiores/integracion.py --paquete
python3 tools/interiores/fotos_casa.py taller 3 --kit vivienda_pintura --perfil artista
python3 tools/interiores/fotos_casa.py dorm 2 --estilo real
```

Las fichas identifican semilla, perfil, dimensiones y planta. Se puede pasar una lista de tipos separada por comas.
Las puntuaciones formales se registran con una rúbrica doméstica en `data/interiors_review.json`, conservando las respuestas y los hashes de las fichas. La orden del usuario del 17-10 autoriza publicar esta versión de prueba; no convierte las puntuaciones inferiores al umbral en una aprobación de calidad. Un resultado técnico verde solo acredita el alcance de sus ensayos.

## Cómo se trabaja

```bash
python3 tools/interiores/catalogo_<familia>.py   # el catálogo
python3 tools/interiores/datos.py                # comprueba objetos y kits y escribe src/interiores_datos.js
python3 tools/interiores/validar.py <kit> --semillas 1,2,3,4,5,6,7,8,9,10
```

El validador y las fotos corren en el Chrome sin ventana (**siempre sin sonido**, `--mute-audio`, puerto 9333) sobre el
servidor de desarrollo (`python3 tools/devserver.py 8920`). Para mirar el resultado:
`await (await import('/tools/interiores/lab.js')).fotos('<kit>', 3, 'a')` desde la página del juego.

## Reglas del proyecto que aplican

- **Ni un píxel de fotos en el juego.** Todo lo que se ve son primitivas y dibujos de canvas. Las fotos del moodboard son
  solo referencia: se guarda su página, autor y licencia, nunca la imagen. Nada de Google ni Street View.
- **Ninguna marca real** en lo que se publica (rótulos, envases, pantallas): nombres inventados o genéricos.
- **Ningún dato personal** de personas reales.
- Todo lo que lee el jugador, en español.
- Nada se publica (commit, Pages, artefactos) sin que el usuario lo pida.

## Casa de Annie y acabados (17-10-2026)

`src/casa_annie.js` adapta cinco kits al plano singular de Annie: salón, cocina, dos baños y estudio. El dormitorio mantiene cama, gato, tocador, guirnaldas y caja fuerte, con acabados añadidos. Arquitectura, patio, dos plantas, puertas y claves de guardado se conservan. Las pruebas recorren las dos plantas por sus colliders y ejercitan caja fuerte, siesta y decoración guardada en una partida ficticia privada.

Se corrige la conversión sRGB duplicada del catálogo y la caché de texturas dibujadas incluye su semilla. Las lámparas de trabajo y plafones distinguen funciones; el piano muestra el teclado, las cornamentas tienen ramas y la camilla tiene pliegues. La despensa usa reservas a escala de las baldas. Cocina y cuarto joven reservan zonas de mesa y TV; en cuartos amplios el sofá queda frente a la pantalla. Los baños solo seleccionan artículos de higiene.

Las capturas esperan a terminar el vuelo de introducción y buscan cámaras libres; una ficha de taller excluye el estudio de pintura. El empaquetador incluye `guarena-revision` para verificar qué commit se está sirviendo en Pages.
