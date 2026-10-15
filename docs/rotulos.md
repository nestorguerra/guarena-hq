# Los rótulos y sus nombres (épica R del backlog técnico)

Decisión del 15 de octubre de 2026: la copia publicada del juego (GitHub Pages) no muestra ninguna marca ni comercio
real. Las marcas salen **parodiadas** (nunca con su logotipo) y los comercios locales o los nombres de personas, con un
**genérico** de su clase. Los nombres reales solo aparecen en la copia local, la que se juega desde el repositorio con su
servidor de desarrollo.

## Cómo funciona

- `data/rotulos/marcas.json`: el registro. Cada entidad (marca, comercio local o persona) con sus nombres reales tal
  como se leen en las capturas o en OpenStreetMap, su categoría, su estado de autorización (ninguna está autorizada) y su
  nombre público. Además, el genérico de cada clase de comercio de OpenStreetMap y las clases públicas (instituciones,
  plazas, parques…), que conservan su nombre.
- `tools/rotulos/rotulos.py` genera `src/rotulos_datos.js` (solo los nombres públicos: es lo que va dentro del juego) y
  `data/rotulos/reales.local.json` (los reales; está en `.gitignore` y nunca se sube).
- `src/rotulos.js`: al arrancar, el juego intenta leer `data/rotulos/reales.local.json`. En la copia local existe y se
  ven los nombres reales; en la publicada no está y se ven los públicos. Cada rótulo que se dibuja queda apuntado en un
  inventario (`window.__rotulos`), con su texto, su entidad, su sitio y su orientación.
- `tools/fachadas/casas.py` escribe en `src/calles_casas.js` el nombre público y la entidad de cada rótulo leído en las
  capturas, nunca el real.
- `tools/build.py` sanea el mapa que empaqueta: los nombres de tiendas, bares, bancos, oficinas y fábricas de
  OpenStreetMap pasan al genérico de su clase. El juego no los muestra, pero la copia publicada tampoco los lleva.
- `python3 tools/rotulos/rotulos.py validar dist/test.html` comprueba la copia publicable: ninguna marca ni comercio
  real (R-07) y ningún texto de marcador (V-02). El flujo de GitHub Pages lo ejecuta antes de publicar y, si falla, no
  publica.
- Atribución: «© colaboradores de OpenStreetMap» con su enlace en los créditos y en la pantalla del mapa (R-11).

## Para añadir un rótulo con nombre real

Se añade su entidad a `data/rotulos/marcas.json` (id, tipo, nombres reales, nombre público) y se vuelve a ejecutar
`python3 tools/rotulos/rotulos.py`. Si un texto de la versión publicada coincide con un nombre real del registro, el
validador lo señala.

## El resto de la épica R (15 de octubre)

| Ítem | Qué hay | Estado |
| --- | --- | --- |
| R-01 Inventario | `tools/rotulos/inventario.py` carga el juego en el Chrome sin ventana y sin sonido y escribe `data/rotulos/signs_inventory.json`: 697 rótulos con UUID estable, edificio, posición en el juego y en latitud y longitud, tipo, caras, texto y estado. Dos pasadas dan el mismo fichero (mismo SHA-256). `--control` siembra 50 carteles y los encuentra los 50. | Cumple |
| R-02 Esquema | `data/rotulos/poi.schema.json`; `entidades.py` valida las 209 entidades (comercios de OpenStreetMap, los leídos en las capturas, instituciones y calles). | Cumple |
| R-03 OSM | Los comercios de la zona de juego (`data/bounds.geojson`) salen del extracto `data/guarena.osm` (`data/rotulos/osm_pois.json`, con nombre, marca, horario, id y fecha). `data/rotulos/overpass.ql` es la consulta para renovarlo (no se descarga sola). Cobertura en `data/rotulos/cobertura.json`: 89 comercios, 63 con rótulo, 26 huecos listados. | Cumple |
| R-04 Emparejamiento | `data/rotulos/sign_poi_map.json`: 612 rótulos con entidad (586 de confianza alta, 26 media) y 85 genéricos, todos con motivo. | Cumple |
| R-05 Verificación con capturas | `data/rotulos/verificacion_r05.json`. Las 292 capturas solo ven 13 de los 85 rótulos de la cola. Uno corregido (Modas Gallego, que OSM da con el nombre de una persona). | **Sin cerrar**: hace falta un revisor con Street View o fotos de campo |
| R-06 Rellenado | Los 172 rótulos de tienda tenían el panel en blanco: ahora llevan el nombre del comercio que el mapa sitúa allí (genérico en la copia publicada) o un genérico marcado. Ninguna placa vacía (`arreglos.py` las rechaza). 697 de 697 en estado `rellenado`. | Cumple |
| R-07 Parodia o genérico | Primera parte de este documento. | Cumple (falta la revisión legal) |
| R-08 Texto desde datos | Todos los rótulos se dibujan desde sus datos (lienzos generados, no texturas de fachada pintadas). | Cumple |
| R-09 Legibilidad | `tools/rotulos/legibilidad.py`: foto frontal a 10 m (o a la distancia libre si la calle es más estrecha o algo tapa), 1080p, de día y de noche, leída con el OCR de macOS (`tools/rotulos/ocr.swift`). **95,7 % de día y 95,8 % de noche** (objetivo 98 %). Los 30 que fallan son sobre todo rótulos de tienda tapados por árboles o toldos y calles de 2 m. Los rótulos se iluminan de noche. | **Sin cerrar** (≈96 %) |
| R-10 Placas en los cruces | 476 placas de calle: una por calle en cada cruce, en la pared y, si no la hay, en un poste. Rediseñadas como las de las capturas: azulejo blanco, borde azul, el tipo de vía pequeño y el nombre grande en una a tres líneas. Paradas de autobús y horarios: OSM no tiene ninguna parada en Guareña y solo 2 horarios. | Cumple para placas; paradas sin datos |
| R-11 Atribución | Créditos y pantalla del mapa. | Cumple |
| R-12 Resincronización | Consulta preparada; falta el trabajo trimestral en CI. | Pendiente |
| V-01 / V-02 | `.github/workflows/validar.yml` en cada pull request y cada noche: marcas, marcadores, esquema y emparejamiento. El OCR y el inventario necesitan macOS y el juego en un navegador: van en local. | En marcha |
