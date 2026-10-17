# Revisión de calidad de la tanda 11

Revisión de código y visual separada de las verificaciones de raíz. Ninguna aprobación implica alcanzar 4/5.

# Revisión independiente de código infantil — tanda 11

**Dictamen final del estado identificado abajo: sin P1/P2 pendientes.** Se encontró un P2 geométrico en los cajones de la cama; raíz lo corrigió durante la revisión y la geometría corregida se ha comprobado de nuevo de forma independiente. Esto no aprueba calidad visual ni publicación.

## P2 encontrado y subsanado

`tools/interiores/catalogo_vivienda_b.py:26–34`, `vb_cama_ninos`:

- Estado inicial: cuerpo de ancho .85, frentes x=±.418 con espesor .014. Cara externa ±.425 exactamente coplanar con el cuerpo. Tiradores con el mismo x y espesor .012: cara externa ±.424, enterrada 1 mm. La cota y el fondo de esas piezas estaban dentro del cuerpo macizo. Efecto: detalle de cajón con conflicto de profundidad y tirador oculto por la geometría, en todas las semillas.
- Corrección releída en generador y JSON activo: cuerpo inferior .81 (cara ±.405); frentes de .014 en ±.412, desde .405 hasta .419; tiradores de .012 en ±.419, desde .413 hasta .425. Conectados y con salida visible de 6 mm respecto al frente. Cabecero .85 y colchón .82 intactos; huella total .85 y longitud anteriores conservadas.
- Verificación CPU independiente: cuatro frentes/tiradores cotejados numéricamente y aserciones de contacto/saliente/huella PASS. Sin GPU. No se ha revisado una captura posterior; la ficha inicial anterior a la corrección no prueba este estado final.

## Revisión funcional y de colocación

- `kits_vivienda_b.py:34–45`: el cambio infantil está separado del joven. Mesa con `silla_frontal` usa la admisión atómica existente: geometría y reserva de asiento se comprueban antes de comprometer el puesto, mantiene índices `e` y enlace `de`. No aparece una segunda silla independiente. No se alteran reglas del motor ni la anchura de paso de .8 m.
- Armario con reserva frontal [.7,.6], rol `armario`, dimensiones de cuerpo .95 × .42 × 1.50 y tiradores añadidos fuera del frente. Conserva la creación de interacción `hide` por rol; no se reduce a un objeto decorativo sin función. Cama conserva `cama`; mesa/asiento y estante conservan roles. La cama adicional mantiene su condición de área/habitación.
- Estante: cajas inferiores apoyadas en y=.052, cara superior de balda inferior; superficie usable superior y=.76 coincide con el techo de la balda. No he identificado piezas flotantes ni dimensiones negativas. El acompañamiento junto a mesa sigue opcional y conserva su fallback a pared, sin debilitar reservas.
- Catálogo B: comparación independiente contra HEAD de cada objeto preexistente, **todos idénticos**. Sólo se añaden cama, armario y estante infantiles; no se escala el mobiliario compartido de otros dormitorios.
- `acabados_vivienda.js:22–27`: plano exclusivo de `rm.type==='ninos'`, recortado .15 m a las dimensiones del cuarto y 9 mm sobre su planta. Retorno temprano evita aplicar el acabado a otros tipos. No modifica colisiones, huecos de pared, mobiliario o luces. Es una lámina nueva sobre el suelo, no la sustitución de su geometría; no he observado un fallo funcional estático por ello.

## Pool aplicado

Parche `.cache/calidad/ninos_pool.patch` ya presente en fuente activa al leerla. `infantiles(C)` se ejecutó sólo en memoria (sin generar ni escribir datos): **52 IDs en pool bajo y 36 en tablero**, idénticos a las dos listas del kit JSON activo. `alto` considera escala y rotación de piezas; límites .280001 y .160001 sobre cota superior real. Las referencias existen y son de superficie.

El reemplazo `p[-2:-1]` conserva la entrada de techo de `adornos` y sustituye sólo su entrada de superficie por mesa y mesita/estante. Osito y bloques obligatorios se ejecutan antes. Se reduce decoración opcional a 1–2 piezas por soporte, sin alterar mínimos de los objetos funcionales.

Leído `ninos_pool_encaje.json`: todos los 52 IDs caben al menos en un soporte autorizado; los 36 de mesa caben en ella. Ocho IDs del pool general sólo caben en mesa: están también en su pool específico; que no entren en mesita/estante es un rechazo normal de colocación opcional, no colocación forzada. Esto no prueba que cada ID vaya a aparecer en una muestra pequeña de semillas. El inventario cuenta 63 objetos distintos declarados, no 63 objetos colocados por habitación.

## Contratos y evidencia

Leídos los dos contratos nuevos con guard `opts.ninos || opts.tanda>=13`: constructores `buildVecino` para 4007/5045/1296 (4007 y 5045 tienen puerta real en inventario; 1296 es una semilla sintética de ficha), relación mesa/silla, usos, interacción del armario, obligaciones, dimensiones/roles y controles negativos de reservas frontal y total. CI pasa de tanda12 a tanda13 y no incluye los contratos descartados de luz.

Las 47 pruebas navegador anteriores al pool son resultado comunicado por raíz, **no ejecutado de nuevo por este revisor** y no se extrapolan automáticamente al estado final con pool/cajones. Leídos los informes CPU y de datos privados del pool; además se han hecho las comprobaciones independientes acotadas de geometría, listas generadas e invariancia de modelos descritas arriba. No se ha ejecutado regeneración ni navegador/GPU. Quedan a la validación final de raíz los contratos/semillas sobre esta última combinación y la nueva captura.

Limitación de cobertura de tests: los dos nuevos contratos no comprueban el límite de altura de todo el pool ni el saliente de los tiradores. Las comprobaciones independientes anteriores sí cubren los datos actuales, pero no sustituyen una regresión persistente si se desea proteger esas propiedades frente a cambios futuros.

**Declined to judge:** nota estética infantil y objetivo 4/5; despensa y otras habitaciones fuera de este encargo; luz cenital r2, residentes y diagnóstico previo; fluidez/GPU, save/load completo y publicación. Ninguna fuente activa editada por este revisor.

## Estado exacto

SHA-256 de los archivos revisados tras la corrección de cajones:

```json
{
  "tools/interiores/catalogo_vivienda_b.py": "338354e0e78d95ddfd07a8e7cb4ab393760e70f499ce7caa2d27945c4aa035e5",
  "tools/interiores/kits_vivienda_b.py": "fca78dabd232caff6344bb7aa5c94aad56a62659e60d96e99de44181b64c018d",
  "src/acabados_vivienda.js": "d22444633e67bb4b64f8b70a674a41b3ca21d936c29846f342f9fe1c19d2054b",
  "tools/interiores/casas_pruebas.js": "398b4a40abcf03f111dbb79cbf5fb64880b4529ce3f0c30efbb68787f0da6cef",
  ".github/workflows/validar.yml": "acf4fd692e8646aa07616611b15da767f770d6e91e899010f7f53a9c26f4efeb",
  "data/kits/vivienda_ninos.json": "d54a9c620581e2390ba425c1f93eefe7803c928f843b0dad594ede9d78e7165a",
  "data/objetos/vivienda_b.json": "8d1ff06d66356400e3ce7c2f220c988882858def00e84437d5eef20155d3038a",
  "src/interiores_datos.js": "e05c2085ca459437c024a9056ca501690e9e13060ae2c2a18065171f4e88b1e3",
  ".cache/calidad/ninos_pool.patch": "a0772d920bae605bfb55f1b01301577880bfcfb39344d6872b5a0a5611d0d552"
}
```

## Adenda: acabado infantil ampliado y alfombra (estado posterior)

Releídos el acabado y el kit activos después de la primera revisión. **Sin nuevos P1/P2 identificados.** Esta adenda sustituye el alcance anterior de “sólo plano de suelo” y añade la alfombra; no atribuye resultados a pruebas navegador pendientes.

- `acabados_vivienda.js:22–44`: los paños terminan en .92 m. `panosPared` resta cada puerta desde 0 a 2.1 m, por lo que no deja pintura atravesando su paso. Las ventanas arrancan en .92 m: el paño inferior toca el borde del alféizar pero no invade la abertura. Orientación e inset siguen el mismo convenio de los acabados existentes. No añade arquitectura ni collider.
- Verificación CPU adicional con el cuerpo real de `revestirEstancia` y registros de geometría/material: **8 casos PASS**, cuatro orientaciones y dos plantas; no hay intersección de los paños con la abertura de puerta, todas las tablas tienen dimensión positiva y quedan dentro del borde previsto, la ventana en el límite .92 no se tapa y colores de la misma semilla se repiten. Artefactos `ninos_acabados_revision_cpu.mjs/json`. No renderiza ni prueba profundidad de píxeles.
- Cotas leídas: suelo arquitectónico y+.005; base nueva y+.009; tablas y+.0095. Hay separación geométrica de 4 mm respecto al suelo original y de .5 mm respecto a la base, no coplanaridad exacta. Las tablas dejan juntas de 3 mm. La alfombra existente tiene base superior .012 y paño superior .014, de modo que quedan respectivamente 2.5/4.5 mm por encima de las tablas; se oculta parte del canto inferior bajo el revestimiento, sin hacer desaparecer su cara superior. No afirmo ausencia de artefactos de profundidad/sombra sin la captura posterior.
- Techo nuevo y+altura−.008, orientado hacia abajo; separa 8 mm de la cara arquitectónica y mantiene las cotas de planta. No toca la posición de luces. Los límites horizontal y vertical del cuarto siguen siendo los existentes.
- La alfombra se inserta después de cama/mesita/armario/puesto/estante y antes de cuadros/adornos: no altera la colocación ya comprometida de los muebles funcionales. Área `<12` la excluye antes de consumir RNG. Área `>=12` usa `suelo_libre`, con dentro/libre/cierra existentes y omisión si no cabe; no fuerza una pieza contra reservas.
- **Efecto RNG explícito:** `suelo_libre` usa `N(cantidad)`, no `cantidadPreferida`; por tanto `preferir:true` no obliga a probar una alfombra y `[0,1]` conserva posibilidad de cero. Cuando la entrada es activa consume RNG incluso si sale cero, y si busca posición consume más. Pueden cambiar cuadros/adornos posteriores y su distribución; no se puede afirmar identidad de esos objetos frente al kit previo. La misma semilla con el mismo kit sigue siendo reproducible. No cambia el motor ni el comportamiento de otros kits. El RNG del acabado es local e independiente del utilizado por `amueblar`; esto no es una garantía sobre el RNG global de UUID/animación de personajes.

Las pruebas de navegador y la captura que raíz estaba ejecutando durante esta adenda no se han usado como evidencia de éxito. Queda pendiente su resultado sobre el conjunto final.

SHA-256 del estado ampliado revisado (sustituye estos archivos en la identidad anterior):

```json
{
  "src/acabados_vivienda.js": "7d843e85720f208b1d429a99e891d8e45614fcfcc670452faceb3657dfadcaa3",
  "tools/interiores/kits_vivienda_b.py": "7ee7fa4335e20acf7faec013bd8e82b1c4444bd4f8e296ee32f26acdc1dc4237",
  "data/kits/vivienda_ninos.json": "26755404e77d73b5a334684c0d22c5abe40fc46773d8ff57a1d333ca2eecd51b",
  "src/interiores_datos.js": "00b81ba61535a682081cef9991dbd2e8ef5917877d8b194bf188400e194d2b44",
  "tools/interiores/catalogo_vivienda_b.py": "338354e0e78d95ddfd07a8e7cb4ab393760e70f499ce7caa2d27945c4aa035e5",
  "data/objetos/vivienda_b.json": "8d1ff06d66356400e3ce7c2f220c988882858def00e84437d5eef20155d3038a"
}
```

Precisión de alcance: la lectura de los contratos no certifica ocultación real en las tres semillas. La raíz comunicó comprobación de ocultación v1 en 4007/5045; 1296 sigue pendiente de una puerta temporal declarada y del control de conservación de inventario/partida. No se reclasifica como validada.


---

# Revisión independiente de despensa — tanda 11

**Dictamen del estado identificado al cierre: sin P1/P2 pendientes en la fuente activa revisada.** El parche original `9da82232ee1776649bdf9b64d0db37694203268d4cc372c5c9500b005b41cf31` sí contenía un P2 geométrico; raíz lo ha subsanado en generador, JSON y receta compilada. El parche original permanece como evidencia y no debe reaplicarse sin esa corrección. No se aprueba aquí calidad visual ni publicación.

## P2 encontrado y subsanado: vinagre atraviesa la tapa superior

Ubicación: `tools/interiores/kits_vivienda_a.py:73–78`, pool sobre `va_estante`; propagado a la entrada 10 de `data/kits/vivienda_despensa.json`.

La botella `va_alimento_vinagre` mide 24 cm. La última superficie está en y=1,17 y la cara inferior de la tapa en y=1,4025. El hueco real es **23,25 cm**, aunque el comentario dice 25 cm. La botella llega a y=1,41 y atraviesa 7,5 mm de madera. Reproducido con `amueblar` y geometría reales, semilla 53, W=5, D=4, H=2,75, funciones activas. Evidencia inmutable: `despensa_vinagre_repro.mjs/json`, y primera comprobación exhaustiva `despensa_revision_independiente_cpu.json` en esta carpeta.

El informe del autor no lo detectó: su comprobación admite penetraciones de hasta 1 cm. No es una diferencia estética; el tapón queda dentro de una pieza sólida. La raíz excluyó el vinagre sólo del estante bajo. Sigue disponible sobre el aparador y en almacenaje alto. Releídos generador, JSON y entrada compilada: la corrección coincide. El contrato propuesto admite sólo 0,1 mm de error numérico; vuelve a fallar exactamente por este caso al reintroducir el ID en memoria y pasa con la receta corregida.

La raíz corrigió también el comentario a «al menos 23 cm útiles». La holgura mínima calculada es 23,25 cm; el contrato protege la propiedad a partir de la geometría.

## Comportamiento revisado

- **Mínimos y fallback:** estante y aparador obligatorios; el tercer módulo preferido no elimina la búsqueda individual si falla el grupo. Probado con pared inicial de 2 m en una sala de 14 m²: el aparador pasa a otra pared y permanecen las cajas. Una reserva total del volumen de uso no fuerza muebles dentro de ella. Las luminarias siguen su mecanismo de techo preexistente, fuera del control negativo de muebles.
- **Umbral de cajas:** áreas 13,999 / 14 / 14,001 m² tienen exactamente una entrada activa. A partir de 14 es obligatoria y aparece; debajo mantiene condición opcional. No se solapan intervalos `area_max` y `area_min`. Semilla repetida produce P idéntico en estos casos.
- **Perfiles negativos:** agricultor y cazador activan sólo la provisión de aceite/conservas; matrimonio, familia, estudiante, artista y anciana sólo desayuno. Se comprobó exclusión y presencia del contenido esperado; no se confía únicamente en el número de entradas.
- **Alturas:** revisión exhaustiva de cada ID que cabe en planta sobre cada superficie real de cada soporte del pool. La receta corregida no penetra baldas/tapas en esas posiciones. Además, las colocaciones CPU de las tres plantas canónicas 2786/1689/2132 no presentan interpenetración con su soporte con tolerancia de 0,1 mm. Estos últimos datos proceden de funciones de planta/mobiliario, no del constructor completo de escena ni de GPU.
- **Acabados e integración infantil:** `src/acabados_vivienda.js:45–110` añade despensa a la rama existente. El bloque infantil con retorno temprano permanece igual al candidato revisado. El archivo completo coincide con la copia del prototipo; la receta A no modifica el kit infantil B. `houses.js:562` sólo excluye despensa del zócalo previo, para no superponerlo al acabado nuevo. Conserva los recortes de puertas/ventanas de `panosPared`; suelo a +9/+9,5 mm y techo local siguen las cotas del mecanismo existente. No se introducen cambios de arquitectura, luces, reglas del solver ni cámara.
- **RNG:** la receta nueva cambia legítimamente el mobiliario sorteado de despensa. No se promete igualdad de resultados con la receta anterior. La repetición con la misma semilla es determinista; el material usa un generador local independiente. No se ha certificado invariancia del RNG global usado por residentes asíncronos.

## Contratos preparados y entregados

`despensa_contratos.patch`, dos casos con `opts.tanda>=13`, sólo modifica `tools/interiores/casas_pruebas.js`:

1. Pool completo contra las piezas reales de cada soporte y superficie, incluida tapa superior. Usa `partes`, `penetra`, `superficie` y `caja` de producción. No duplica una lista manual de exclusiones ni un límite nominal de 25 cm.
2. `buildVecino` en las tres semillas canónicas, muebles obligatorios, acceso, apoyos y no penetración soporte/hijo; filtros de perfil excluyentes; umbral de 14 m²; fallback a otra pared, determinismo y reserva negativa.

Parseo Node y `git apply --check`: PASS antes de la entrega. Durante el cierre, raíz aplicó exactamente el parche; `git apply --reverse --check` confirma su presencia actual. Este revisor no modificó fuentes activas. Ejecución CPU de todo el primer caso y de los subcasos del segundo que no construyen la escena: PASS; recibo `despensa_contratos_cpu.json`. Mutación sólo en memoria reintroduciendo vinagre: FAIL intencionado en superficie 4; recibo `despensa_contratos_mutacion_cpu.json`. No se ejecutaron los tres `buildVecino` de este parche en navegador; queda pendiente esa parte. El harness CPU declara expresamente su omisión. No usa importaciones de `.cache` en los contratos entregados.

El informe del autor y sus 81/203 muestras se han leído; no se han repetido ni convertido en verificación propia de navegador. La receta compilada coincide con la JSON (el compilador omite `moodboard`, por diseño).

## Declined to judge

- Calidad estética, lectura de alimentos, puntuación 4/5 o autorización de publicación.
- Coste GPU, FPS, sombras, iluminación y resultados de capturas posteriores.
- Integración completa de navegación/partida/ocultación: sólo lectura de mecanismos y contratos; pruebas finales a cargo de raíz.
- Cobertura universal de todas las semillas. El contrato exhaustivo cubre pools y soportes en posición central válida; las tres escenas comprueban colocaciones reales concretas, no toda posible combinación.
- Ocultación parcial de ventana por provisiones del aparador: riesgo visual declarado por el autor, no defecto de acceso demostrado aquí.
- Los cambios de luz cenital rechazados/pendientes, fuera de esta tanda.

Se corrigió también la precisión del informe infantil: 4007 y 5045 tienen puerta real; 1296 es semilla sintética de ficha. Construir las tres por `buildVecino` no demuestra tres accesos existentes en inventario ni tres ocultaciones ya verificadas.

## Identidad final leída

- `tools/interiores/kits_vivienda_a.py`: `cb18ebdc6c548f39efe6190ce95506662d0c846077097a55f63dfa7590c6c0a6`
- `data/kits/vivienda_despensa.json`: `28195beeb86ac9b6f9a8f4244e821c97bd47b64db05dfe67adbd8244505e8880`
- `src/acabados_vivienda.js`: `5cc8a52d29ee342052012a85abd24a14d2be5e9ac5a1feab604310fbaf752517`
- `src/houses.js`: `8199cd82a0e89feb3e19e002cd9fd17a63d7f26f9fe95a7adff34cc8dcacc162`
- `src/interiores_datos.js`: `f534acd0fc0f9ec7a3ac01b0c8c244e2d8b2b323396506c0211645f5afb1f765`
- `tools/interiores/casas_pruebas.js`: `a0e7b5b490a34de5ba528756e675a8997300bde32bb17abcdefcb1cae6dbb0bb`
- `.cache/calidad/despensa_contratos.patch`: `fc1da2112ca2e6b94ee33a5b87f98af556431278138288961461ab1717cff278`

## Estado comunicado por raíz después del cierre estático

Raíz comunica tanda13 completa **49/49 en navegador** tras aplicar estos dos contratos y regeneración idéntica. No repetida por este revisor. Las 200 casas, 81 semillas por kit, integración, build y paquete seguían en curso; no se dan por terminadas en este informe.

Manifiesto de congelación disponible: `.cache/calidad/tanda11/estado_candidato.json`, SHA-256 `bdc738a0b6c868739d9ca4ffbdc4e156296d206c9c1585c9ae973dd88f654a96`.


---

# Tanda 11 · revisión visual independiente de infantil

Dictamen: **no observo una regresión visual bloqueante en la segunda ficha infantil**. Mejoran la relación cama–guardado–mesa, la lectura del suelo y el contraste del conjunto. Puede cerrarse como mejora parcial; el objetivo de calidad sigue pendiente. No emito puntuación propia ni aprobación formal.

## Evidencia y alcance

Ficha actual `data/interiores/fichas/casa_ninos.jpg` y JSON, escrita el 17/10/2026 a las 21:08:31. Comparada visualmente con la primera candidata `.cache/calidad/tanda11_ninos_inicial.jpg` (21:05:31) y la base `data/interiores/validacion/historico/calidad_tanda11_base/casa_ninos.jpg` (20:50:50), ya inspeccionadas en la revisión previa. Reabierta la actual para este cierre. Semillas 4007, 5045 y 1296; dos vistas por casa, calidad alta, DPR 1 y FOV 68.

SHA-256 actual: `dfc023de67961c9d1225ce47dd8f2e0a8c5f682c72e037a87ab1e2ac321ea63d`.
SHA-256 primera candidata: `5668dc9dd8509faff56200b1ac7a20fbd88de8bf25434b053448bca65eb75615`.
SHA-256 base: `a35faa3a2de019f419b4ab98c90564b9288829f517bf65fb6859bad8b033a4da`.

## Observado

- **4007, 4,8 × 2,3 m:** cama con cajones, mesa/silla y guardado bajo ofrecen funciones reconocibles. El zócalo cálido separa mejor suelo y pared. El armario alto sigue dominando el extremo y el espacio conserva poco contraste entre madera clara, pared y suelo. No conviene añadir otro mueble al estrecho paso visible.
- **5045, 4,9 × 2,3 m:** el zócalo azulado y el suelo discreto ordenan mejor el conjunto que la primera versión. Hay guardado accesible y puesto de trabajo reconocible; el armario grande y las superficies claras siguen pesando más que la identidad infantil. Los cuadros de paisaje/familia conservan una lectura genérica. Los encuadres se complementan; no interpreto el mueble recortado en uno como ausente.
- **1296, 4,5 × 3,3 m:** la alfombra delimita una zona libre y mejora la orientación de la sala. Su centro casi del mismo color que el suelo y su simple borde azul producen poca masa visual. Los bloques permanecen alineados sobre la mesa mientras la zona de juego queda vacía. El cartel «Música en la plaza» y las grandes paredes claras apenas distinguen la estancia de un dormitorio genérico.

El techo crema, el zócalo y el pavimento más tranquilo son mejoras visibles. Persisten una iluminación muy lavada sobre superficies pálidas y poca identidad infantil en las paredes. La lectura de cajones y tiradores es compatible con la corrección anunciada, pero las imágenes de ficha no verifican por sí solas AABB, holguras ni usabilidad.

## Siguientes tres mejoras visibles

1. Sustituir los cuadros/carteles genéricos por una composición infantil clara sobre cama o mesa, respetando el estilo artesanal y los huecos de pared.
2. En 1296, dar más masa de color a la alfombra y relacionarla con una actividad de juego usando los bloques existentes, conservando las reservas de paso.
3. Reforzar el contraste de cama y guardado frente a las paredes pálidas mediante su paleta actual. No sumar mobiliario ni luces como sustituto de esa composición.

No se ha abierto el juego ni realizado más ensayos. No certifico otras semillas, circulación con movimiento, rendimiento ni el objetivo formal. Las puntuaciones de raíz quedan separadas de este dictamen. No atribuyo aprobación al usuario.


---

# Tanda 11 · revisión visual independiente de despensa

Dictamen: **no observo una regresión visual bloqueante en las seis vistas actuales**. La nueva composición mejora la lectura doméstica y conserva el estilo de diorama artesanal. Es una mejora parcial; esta revisión no certifica el objetivo de calidad ni sustituye la evaluación formal.

## Evidencia y alcance

Inspección directa de `data/interiores/fichas/casa_despensa.jpg` (17/10/2026, 21:17:39) y su JSON, frente a `data/interiores/validacion/historico/calidad_tanda11_base/casa_despensa.jpg` (20:50:57) y su JSON. Semillas 2786, 1689 y 2132; dos vistas por casa, calidad alta, DPR 1, FOV 68 y altura de cámara 1,6 m.

SHA-256 actual: `bbd53162ebcf8cb0a437ef0c87786c453415a734f0b2877a48ee573dcd2a6316`.
SHA-256 base: `003d39beaa29053eef57ddd898e33dac3e1572abf5cc405ec73ea045c77ecbfa`.

Las cámaras han cambiado entre versiones. Se comparan la composición general y las zonas identificables; no es un A/B visual estricto de iluminación, ni permite atribuir a una retirada lo que sólo queda fuera de plano. No se ha abierto el juego, ejecutado GPU ni modificado producto.

## Observado

- **2786:** aparador, estante estrecho y dos altos forman un frente reconocible de almacenamiento y apoyo. Los envases de colores rompen la antigua repetición de paquetes idénticos. El conjunto oscuro destaca bien sobre la pared. A cambio, varias baldas tienen grandes huecos y la vista secundaria muestra una superficie muy extensa de pared/suelo sin jerarquía; el frente sigue pareciendo escaso para el tamaño de la sala. El recorte lateral del estante alto en esa segunda vista no demuestra ausencia: la primera lo muestra completo.
- **1689:** el aparador bajo la ventana, flanqueado por estantes, ofrece la relación de uso más clara. Las cajas quedan agrupadas en el extremo visible. Mejora la unidad frente a las piezas separadas de la base. La segunda cámara corta parte del estante derecho, compensada por la primera. Se conserva una gran pared lateral vacía, pero no observo en las imágenes una invasión nueva evidente del acceso.
- **2132:** aparador y estante componen un frente continuo, con un paso visible ante la puerta. Los tarros grandes ocupan buena parte de algunos huecos y dominan frente a los envases pequeños; la variedad se lee irregular y varias baldas quedan casi vacías. El gran paño opuesto tampoco participa en la composición. No identifico por estos píxeles una nueva colisión funcional.

Los acabados lisos, el zócalo y el suelo más discreto reducen el ruido de la base y permiten leer mejor las siluetas. El mobiliario de madera conserva contraste suficiente. La habitación pierde parte del contraste cálido del antiguo suelo de teja; pared y pavimento claros se acercan entre sí y dejan más expuesta la baja densidad. Eso es un límite de composición, no una prueba de peor iluminación.

La exclusión del vinagre del estante bajo fue comunicada por raíz. No identifico etiquetas legibles suficientes para verificar semánticamente ese ingrediente sólo en la ficha.

## Pendiente para otra tanda

1. Componer el frente existente como conjunto más intencionado: concentrar las reservas en grupos de tamaños compatibles y equilibrar los huecos de las baldas, sin regresar a filas idénticas ni sumar muebles al paso.
2. Dar jerarquía al paño del almacenamiento mediante los acabados actuales y ajustar la relación de color entre pared baja y suelo. La mejora debe verse a escala de habitación.
3. Moderar el predominio de los tarros grandes de 2132 para que el tamaño del producto y la capacidad de la balda resulten coherentes.

Este dictamen se limita a las tres muestras y sus encuadres. No verifica circulación con movimiento, reservas geométricas, otras semillas ni rendimiento. Las pruebas funcionales y puntuaciones formales quedan en el registro de raíz. No atribuye aprobación al usuario.


## Cierre de verificación por raíz

El candidato final pasa 49 contratos en navegador, 200 casas, 81 semillas por kit, integración fuente con 96 recorridos de colisión y paquete. Se regeneran 21 archivos sin cambios. La ocultación y salida de los armarios se comprueba en dos puertas reales y una muestra sintética, con recarga y conservación de inventario/partida. Las nueve capturas se inspeccionan; véase validacion/tanda11_armarios.json. Las pendientes de ejecución indicadas por los revisores describen el instante de su revisión; estos resultados posteriores están en los informes de validación. No se certifica 4/5 ni rendimiento general.
