# Revisión de calidad de la tanda visual 12

Contratos ejecutados con nivel 14; es una numeración distinta del número de tanda visual.

# Revisión independiente — identidad infantil, tanda visual 12 (contratos 14)

**Sin P1/P2 identificados en el prototipo revisado. Preparado para prueba aislada; no es aprobación visual ni de publicación.** No se ha aplicado el candidato ni los contratos, no se han tocado fuentes activas y no se ha usado GPU/navegador. T11 permanece separado.

Parche revisado: `identidad_infantil.patch`, SHA-256 `cccc6f0032a127f9faa0b453efc58d0641a76edc9773093777a8d0939f17cbda`.

## Comprobaciones independientes

**Caché y dibujos.** `src/objetos.js:73` ya usa `tipo + JSON.stringify(tex) + seed%17`. Incluye `tex.lamina`, por lo que 0, 1 y 2 no colisionan. Ejecuté ese código real con `THREE.CanvasTexture` y un contexto Canvas que registra trazos, usando el catálogo y las funciones de dibujo candidatas. Resultado: tres objetos de textura distintos y tres trazas diferentes. Semilla 18 reutiliza exactamente las texturas de semilla 1. La mutación privada que elimina `JSON.stringify(tex)` de la clave falla con 1 textura distinta en vez de 3. Esto verifica la caché; no sustituye la comparación de píxeles o la lectura visual en juego.

**Apoyo de galería.** `tools/interiores/catalogo_vivienda_b.py:45–51` candidato y regla `pared` de `src/locales.js:282–320`: la galería completa queda entre y=1,2725 y 1,643 m; la cama termina en y≈0,65 m. Su ancho real es ≈0,755 m, menor que los ≈0,85 m de cama. Las tres láminas y cintas forman un único objeto; no se sortea cada dibujo independientemente. En N/S/E/W, comprobación con `amueblar` real: orientación y centro de cama coinciden y la cara trasera está a 3 mm de pared. Una reserva en ese volumen suprime la galería y conserva la cama; si falta la cama, no aparece galería huérfana ni fallback a otra pared.

**AABB y colcha.** `catalogo_vivienda_b.py:35–43`: cinco cajas contiguas, sin superposición volumétrica, longitudes .46+.06+.23+.06+.34=1,15 m; conservan inicio/final y espesor del cobertor. La envolvente completa de cama y la de alfombra coinciden con la base en las seis cotas (tolerancia 1e-7). El cabecero, colchón y cajones no se ensanchan. El cambio añade cuatro cajas, sin modificar paso o collider. Tres paños recuperan `tinte:'tela'`; dos bandas crema no llevan tinte. `src/objetos.js:178` selecciona la tela de la paleta por semilla de objeto; `src/houses.js:1080` suministra esa paleta/semilla al montador. No se prometen colores de píxel bajo iluminación.

**Alfombra.** `catalogo_vivienda_b.py:52–57` conserva las dos cajas y sus dimensiones; la textura se dibuja en la superficie existente, no crea otra lámina coplanar. `src/texturas/vivienda_b.js:40–50` candidato ofrece tres paletas por la semilla reducida; el paso por la caché real produce tres trazas distintas para semillas 1/2/3. La regla sigue siendo opcional desde 12 m²; `preferir:true` no obliga a aparecer porque `suelo_libre` conserva su sorteo preexistente. No debe anunciarse alfombra presente en cada cuarto grande.

**Compatibilidad e invariancias.** Los cambios están limitados a catálogo B, kit infantil B, familia de texturas B y sus dos JSON. No cambia `src/objetos.js`, el solver ni el acabado infantil activo. Los cinco hashes de entrada del manifiesto siguen coincidiendo con la activa. Leídos el informe y las pruebas del autor: sus 81 muestras y 37 cuartos de plantas no son pruebas de navegador de este revisor. 4007/5045 tienen acceso inventariado; 1296 sigue siendo semilla sintética de ficha. No se llama a las tres «casas reales publicadas».

Recibos independientes: `identidad_infantil_revision_cpu.mjs/json` y `identidad_infantil_revision_mutacion.json`. Se usaron geometrías Three reales y cajas conservadoras para redondeos; no se construyó la escena completa ni se rasterizó con Canvas de navegador.

## Dos contratos propuestos

Parche privado `identidad_infantil_contratos.patch`, SHA-256 `d569d56735fffbbdf2d4421cf2a9117c07438bab5bb3e034a7dbf77e2f4eedac`. Sólo añade dos casos a `tools/interiores/casas_pruebas.js`, con guard **`opts.tanda>=14`**; no toca CI ni mezcla la ejecución tanda13.

1. Montaje real mediante `construir`: tres mapas y tres imágenes Canvas distintas; reutilización de caché al repetir semilla equivalente; tres paletas de alfombra; variación de colores de vértices de cama con paleta doméstica; envolventes de cama/alfombra frente a los modelos de referencia conservados. Cubre el hueco del autocontrol del autor, que llama a `draw` directamente y no pasaba por la caché/montador.
2. Colocación de galería en cuatro paredes: altura sobre cama, centro, orientación, apoyo y reproducibilidad; controles negativos de reserva y ausencia de cama. No depende de las cámaras de una ficha.

Los contratos usan sólo importaciones de producción, ninguna ruta `.cache`. Su limpieza libera geometría y materiales propios de láminas, conservando las texturas/materiales compartidos de caché. Parseo Node y `git apply --check` pasan. **No ejecutados en navegador**; el primer caso exige Canvas 2D real y el montador completo. Las comprobaciones CPU descritas cubren las propiedades centrales pero no se presentan como ejecución íntegra de esos contratos.

## Declined to judge

- Reconocimiento de casa/barco/cohete a distancia de jugador, lectura del circuito, composición y nota 4/5.
- Calidad de iluminación, sombras, contraste final, impresión de tela/plastilina o escalado de capturas.
- FPS, memoria GPU y coste real de las texturas/mallas nuevas. Igual AABB no implica igual coste de render.
- Conservación integral de partida, interacción de ocultación e inventario tras integración: el candidato no toca esos mecanismos, pero no se ha ejecutado ese flujo.
- Resultado de una integración futura sobre T11: se deberá regenerar desde las fuentes activas; no copiar el derivado global de la carpeta privada.

## Adenda — integración activa después de T11

Releído el diff sobre HEAD `b7ea0fe663ee33cde3f7ececc619fde27696f855` (T11). **Sin P1/P2 nuevos en esta integración estática.** Los cinco archivos del prototipo coinciden byte a byte con el manifiesto candidato; los dos contratos están aplicados exactamente (`git apply --reverse --check` PASS). CI pasa de tanda13 a tanda14.

La única adición al acabado es `src/acabados_vivienda.js:26`: `#a0b3ad/#b6a68e/#98aeb8` → `#718d82/#aa895b/#6e879b`. Comprobado por sustitución exacta sobre HEAD: no cambia ninguna otra línea del archivo. Se conservan altura .92 m, recortes de huecos, geometría, suelo/techo, RNG, parámetros de material y luz. Sólo cambia el color base de esos paños infantiles; no se afirma su resultado bajo la iluminación final.

El derivado `src/interiores_datos.js` sólo cambia `vb_cama_ninos`, añade `vb_dibujos_ninos`/`vb_alfombra_juego` y actualiza `vivienda_ninos`. Catálogo B y receta compilados coinciden con sus JSON (sin `moodboard` en el compilado, como antes). No aparecen cambios semánticos en otros objetos o kits.

No se han ejecutado aquí contratos de navegador, regeneración, build ni GPU. Captura `ninos3` en curso por raíz: pendiente de lectura y juicio visual independiente. La publicación de T11 comunicada por raíz no se extrapola a esta tanda nueva.

Hashes del estado leído (recibo adicional `identidad_infantil_adenda_integrada.json`):

- `src/acabados_vivienda.js`: `6e6efdf14d66d057e5f767b39328112137ff7e3ae0b7eddc14c856edd69189a2`
- `src/texturas/vivienda_b.js`: `508048d8b58ab97b9464c717994c7f518f45432d080bf7f6a4a418b6171f61b2`
- `tools/interiores/catalogo_vivienda_b.py`: `e43c9071910bf6da1703e102e79b92a6dcc9f8f9fa0c6c4faf3a46822a5a7bb8`
- `tools/interiores/kits_vivienda_b.py`: `1fa535f7d85cea38060b3432094fe9b7bd127d4fc68182bf28a007be331233a2`
- `data/objetos/vivienda_b.json`: `5f2c99b894a5c0eb0d138876fdca71db722e34bbcfb9c7a06b36863715355920`
- `data/kits/vivienda_ninos.json`: `3e4f61d619663308522ba896c762b560eb2bf49379ebb9d798bac428f3561668`
- `src/interiores_datos.js`: `4fbdfd8660b979643a793eb5dea4aa059962aba67fc508ff5ddcd59e6e80e79c`
- `tools/interiores/casas_pruebas.js`: `be978562e981b643f552e50802ce0150300ad15c35285d4cb986d74a44c6cd91`
- `.github/workflows/validar.yml`: `829b500c2b7aed2bb3a2d8cd99273692931186096689acff2ce920d83ab4577d`


---

# Tanda 12 · revisión visual infantil

**Dictamen: avance visible, sin regresión visual bloqueante observada.** No certifica el objetivo de calidad ni emite puntuación formal.

Inspección directa de las seis vistas de `data/interiores/fichas/casa_ninos.jpg` (17/10/2026, 21:30:11), frente a la base T11 de `data/interiores/validacion/historico/calidad_tanda12_base/casa_ninos.jpg` (21:08:31). Ambos JSON son idénticos: semillas 4007/5045/1296, mismas posiciones de cámara/objetivos, FOV 68, calidad alta y DPR 1. Esto permite comparar los mismos encuadres, sin demostrar igualdad de toda la escena dinámica.

- SHA-256 T12: `88c915094c98fe2652e82a3fdd94d1a8f0eba339d6b4a6c9c5a19dfe5f982d6c`.
- SHA-256 base T11: `dfc023de67961c9d1225ce47dd8f2e0a8c5f682c72e037a87ab1e2ac321ea63d`.
- SHA-256 JSON común: `3f2c71681463faa1005bab99037173fb4d08c1ffbf83da5b0d8322921b4702e8`.

## Avance y límites por muestra

- **4007:** colcha mostaza y zócalo ocre más profundo dan una masa de color reconocible y separan mejor el descanso de los muebles claros. Los dibujos añaden identidad, pero se leen como un acento pequeño en una pared muy grande. Continúa la sensación de superficies claras lavadas, especialmente mesa y guardado bajo.
- **5045:** colcha azul y zócalo más oscuro mejoran claramente la separación cama/pared. El armario conserva su dominio visual y tapa parte importante del descanso desde el primer encuadre; esto ya ocurría en T11. La galería queda casi oculta en ese ángulo y el segundo no documenta la cabecera. La retirada de cuadros genéricos mejora la pertinencia infantil, pero reduce la superficie decorada; la nueva galería no equilibra por sí sola el gran paño blanco.
- **1296:** el circuito sustituye con ventaja al antiguo borde azul: ahora la alfombra se reconoce como superficie de juego. Zócalo verde y colcha azul aportan contraste a escala de habitación. La galería se identifica sobre la cama, aunque ocupa poco paño. La mesa/estante siguen siendo claros y la gran zona alta de pared mantiene un aspecto escaso.

No aparecen en estos encuadres nuevos solapes evidentes, desaparición de muebles principales ni artefactos gráficos bloqueantes. La menor ocupación visual de pared en 5045 es una limitación real del intercambio de cuadros, no una regresión funcional demostrada. Se conserva la estética artesanal y no veo que el patrón de alfombra introduzca el ruido que tenía el suelo antiguo.

## Siguiente limitación principal

**La jerarquía de la estancia sigue dominada por el armario y los grandes paños claros, más que por descanso y juego.** Antes de añadir más miniaturas, conviene revisar la relación espacial del armario con la cama en las salas estrechas, manteniendo sus reservas y paso, y dar al paño de descanso una composición de mayor escala. No aconsejo otra ronda de oscurecimiento general ni más luces para compensarlo: T12 ya demuestra que el contraste puede avanzar sin resolver esa estructura.

Alcance: revisión estática de tres casas y seis encuadres. No se ha usado GPU, navegador ni modificado producto. No verifica circulación, reservas geométricas, otras semillas, rendimiento o lectura de texturas de cerca. Este revisor propuso los tonos del zócalo; no es autor del prototipo de dibujos/textiles/alfombra, y el dictamen se basa en los píxeles actuales. No atribuye aprobación al usuario.


---

Revisión visual independiente y acotada de T12 frente a su base; sólo las dos fichas, sin juego/GPU ni puntuación.
T12 SHA256: 88c915094c98fe2652e82a3fdd94d1a8f0eba339d6b4a6c9c5a19dfe5f982d6c.
Base SHA256: dfc023de67961c9d1225ce47dd8f2e0a8c5f682c72e037a87ab1e2ac321ea63d.
Los zócalos azul y verde más oscuros separan mejor paredes y muebles claros; en estas vistas no ocultan sus contornos ni sobrecargan el cuarto.
Las colchas azules de 5045 y 1296 se distinguen mejor de almohadas, cama y suelo; las bandas claras conservan legibilidad.
En 4007, colcha amarilla y zócalo ocre se aproximan más que en la base: pequeña pérdida de diferenciación cromática entre ambos, sin pérdida visible de la silueta de cama gracias al marco blanco y las bandas.
La alfombra de 1296 gana una función visual reconocible de juego; borde y circuito se leen, con contraste suficiente respecto al suelo y sin competir de forma excesiva con mesa/cama.
Conclusión limitada: no observo una regresión visible que bloquee esta paleta; vigilar sólo la proximidad amarillo/ocre de 4007. No atribuyo a la paleta los cambios simultáneos de objetos o cuadros, ni evalúo otras cámaras/modos.


## Verificaciones de raíz

La captura final y sus dos evaluaciones corresponden al candidato integrado, incluidos los tres colores de zócalo. Las puntuaciones son 3,328/3,040 y el objetivo no está alcanzado. Pasan los 51 contratos, incluida rasterización real de las tres láminas y prueba de la caché; la ficha usa las mismas cámaras que T11. Las cifras de la validación final se registran en calidad_tanda12.json. Las pruebas de ocultación detalladas de T11 conservan valor como evidencia previa de las mismas envolventes; no se presentan como nuevas ejecuciones T12.


## Publicación verificada

Commit `f667142e230a7f52d746f4b69901b1fdfe429bf2`. CI 39063117668 y Pages 39063319918 completados con éxito para esa revisión. La prueba pública confirmó la revisión antes y después de recargar, ocho viviendas, Annie (caja, siesta y decoración), acciones disponibles en tres comercios y persistencia de partida. Cero errores de consola o de integración. Las acciones de comercio se comprobaron disponibles; no se realizaron compras. Evidencia: `validacion/publicacion_tanda12.json`.
