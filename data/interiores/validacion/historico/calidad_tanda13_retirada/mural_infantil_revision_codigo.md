# Revisión independiente · mural infantil sobre composición T13

**Sin hallazgos P1/P2 en el candidato revisado.** Aceptación estática para integración y comprobación runtime. No aprobación visual ni de publicación.

Parche: `.cache/calidad/mural_infantil.patch`, SHA-256 `b368ca63b33dac299a863dc633b11ebaebb07076fea5ad32208d6941987f8736`. Fuentes completas en `.cache/calidad/mural_infantil_candidato/`. Los ocho hashes de base y candidata coinciden con `manifest.json`, verificados independientemente al cerrar esta lectura. Recibo CPU del autor: `a1d640cc07987f33032f22ef2494af3a9303b2184db0ca57affd8650ca3b6226`.

## Geometría y conservación

En `src/acabados_vivienda.js:24–119`, el plan toma la cama colocada y trabaja en el marco del kit. Las reservas se descuentan por su intersección vertical con la banda 1,04–2,22 m, su proyección al muro y un margen lateral. El armario usa la envolvente `v`, que incluye las alturas reales calculadas por `caja` en `src/locales.js`; no se confunde su huella con una altura supuesta. Se descartan muebles apoyados o colgados; el bloqueo se refiere a muebles altos de suelo junto a esa pared. No se promete evitar cualquier oclusión desde cualquier cámara.

El algoritmo es determinista, no consume el RNG de amueblado ni modifica sus posiciones. Devuelve un único rectángulo continuo o una omisión completa; no rellena otra pared ajena a la cama. La conversión kit→casa usa `rm.cx` y `rm.z0+.075`, coherentes con `WALLF=.075`; `extraMesh` añade el origen exterior exactamente una vez. La planta se suma una vez en Y. El plano queda 3 mm dentro de la cara interior y utiliza UV completos de `THREE.PlaneGeometry`, evitando la escala por metros de `planeGeo`.

En `src/houses.js:1138`, sólo el acabado infantil pasa después del amueblado, como el baño. La semilla local del acabado conserva el suelo/zócalo/techo. Si el kit falla, se mantienen los acabados base sin inventar un mural huérfano. No se añaden collider, rol, interacción, luz ni cambios de guardado de partida.

La receta y su compilado sólo eliminan la entrada de galería: he comparado semánticamente `OBJETOS` y `KITS`; catálogo y demás kits son iguales. El pool infantil pasa de 62 a 61, por encima del mínimo 60. La retirada puede reducir en uno `it.seed` de los adornos posteriores cuando había galería; el autor lo documenta expresamente. Su recibo conserva posiciones/programa y estado RNG en 37 plantas y 81 semillas. No se confunde igualdad del programa de luminarias con una prueba completa de todo el render.

## Material, agrupado y coste

El mural usa tres texturas procedurales como máximo, nativas de 128×128, sRGB, material mate no emisor. Es una malla de dos triángulos. `extraMesh` y `finish` conservan `castShadow=false` y `receiveShadow=true`; la clave de `agruparCasa` distingue ambos flags.

Punto comprobado con especial cuidado: que exista `atlasCasa` **no** implica que el mural lo use. El agrupado deja intacto un bin de un único objeto. El recibo CPU dirigido ejercita precisamente esa rama: crea atlas, pero el mural conserva su CanvasTexture original128 y sus flags. La textura nativa evita que ese caso suba de resolución por accidente. Puede quedar un drawcall propio para el mural; no hay una medida del saldo total de drawcalls frente a las tres láminas retiradas ni una certificación del presupuesto de la casa completa.

## Contratos y evidencia

Leídos los dos contratos del mural y el instrumento CPU que ejecuta el callback negativo real. Cubren montaje tras agrupado, material no emisor, tamaño efectivo de textura, dos triángulos, altura real de planta, cuatro paredes, omisión por falta de cama/altura/reserva total y reserva parcial vertical. El negativo de armario es contiguo a la cama, no un obstáculo ficticio que la atraviesa. El control con reserva por encima de la banda evita un rechazo excesivo. Las mutaciones que suprimen cada guarda producen el resultado contrario y son detectadas.

El contrato T15 de composición se conserva byte por byte. Los tests de variación textil siguen activos; se sustituyen los de galería retirada por los del mural. La galería permanece disponible en catálogo, pero ya no forma parte de esta receta.

Verificaciones propias: `git apply --check`, ocho hashes base/candidata, sintaxis JS de los cuatro archivos afectados y comparación semántica del compilado. Lectura de las rutas reales de `HouseBuilder`, `agruparCasa`, colocación y empaquetado. No he repetido el muestreo CPU del autor ni sobrescrito sus recibos.

## Declined to judge / pendientes

- No ejecución de navegador, GPU, build ni montaje completo `buildVecino` de la candidata por este revisor.
- El CPU del autor usa planta/amueblado reales y montaje dirigido extraMesh/finish/atlas; compara y retira las geometrías base antes del finish dirigido. No equivale a agrupar la casa completa.
- No rasterizado ni puntuación de la pintura; legibilidad a 128 px, ausencia de apariencia de pantalla y oclusión visual requieren las fichas simétricas.
- No afirmación de mejora 4/5, FPS, presupuesto completo de mallas/triángulos/luces, cobertura de todas las semillas o autorización para publicar.
- La prueba runtime debe conservar las tres canónicas y el contrato de paso/uso T15; no reemplazar escenas desfavorables por otras donde el mural se vea mejor.
