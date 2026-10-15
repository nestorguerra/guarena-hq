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
