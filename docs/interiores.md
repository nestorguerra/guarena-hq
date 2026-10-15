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
