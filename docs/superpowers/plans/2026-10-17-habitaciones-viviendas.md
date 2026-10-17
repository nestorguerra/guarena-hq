# Habitaciones de las viviendas de Guareña HQ — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. Ejecución propuesta en esta conversación; revisión visual independiente al cerrar cada tanda, conforme a las reglas del proyecto. Este documento es una propuesta: todavía no autoriza la implementación ni la publicación.

**Goal:** Completar con kits las habitaciones de las 22 casas procedurales de vecinos, conservando sus planos, habitantes, estilos e interacciones, y demostrar la cobertura completa antes de cualquier publicación.

**Architecture:** Se conserva `buildVecino()` y el montador `amueblar()` existente. Se añaden catálogos y kits de vivienda en dos familias, aprovechando los módulos de texturas A/B ya conectados. Se refuerza el validador para distinguir una casa construida sin errores de una casa con todas sus habitaciones migradas.

**Tech Stack:** JavaScript ES modules, three.js 0.170.0 fijado en el empaquetador, JSON y generadores Python. Herramientas existentes de navegador para validación y capturas; sin dependencias nuevas previstas.

**Spec:** `docs/interiores.md` (especialmente «Las casas de los vecinos»), `CLAUDE.md`, `data/kits/kit.schema.json`, `data/interaction.schema.json` y `data/quality_budgets.json`. `docs/hiperrealismo.md` y su registro se han consultado: describen principalmente la iglesia; sus cambios históricos no amplían el alcance de estas habitaciones.

## Global Constraints

- Base exacta: `339cbe13508e9996d855d9ac8f6276e6b98042e9`, rama `epica-i-interiores`; coincide con `main` al revisar el 17-10-2026.
- Orden vigente del usuario: «No despliegues nada todavía». No hacer commit, push, merge, publicación, despliegue ni cambios en Render sin autorización explícita posterior.
- «Una sola zona, `estancia`, toda la habitación». Mantener planos, puertas, ventanas, escaleras, semillas y estilos existentes.
- «La altura de las casas es menor (2,75 m arriba): nada más alto de 2,4 m».
- Mantener la anchura configurada en vivienda: `paso_libre: 0.8`. Los locales usan por defecto 0,9 m; no confundir ambos valores ni aumentar las puertas de las casas durante esta migración. Documentar esta distinción en `docs/interiores.md`.
- Mantener los roles funcionales `cama`, `cama_doble`, `cocina`, `nevera`, `armario`, `comoda`, `mesa`, `silla`, `piano`, `guitarra` y `libros` allí donde correspondan; no basta con que el objeto se vea.
- «Ni un píxel de fotos en el juego». Para estos kits, geometría propia y dibujos de canvas; las fotos de Wikimedia Commons son referencias con autor y licencia. «Ninguna marca real» y «Ningún dato personal»; textos del jugador en español.
- «Las pruebas, siempre sin sonido»: navegador de pruebas con `--mute-audio`; nunca `--autoplay-policy`. Usar un perfil de pruebas aislado y verificar puertos antes de arrancarlo.
- No editar a mano `src/interiores_datos.js`: lo genera `tools/interiores/datos.py`. Los JSON generados deben corresponder a sus scripts fuente.
- Presupuestos actuales, marcados como propuesta en el proyecto: 350.000 triángulos, 60 mallas, 9 luces y 1.500 ms de entrada por interior. Medir la casa completa; no basta sumar los datos de un kit aislado.
- «El que construye nunca aprueba». La ficha de revisión existente requiere dos revisores: media de al menos 4/5 y ninguna dimensión por debajo de 3/5; después, visto bueno del usuario. Las comprobaciones automáticas no sustituyen esta revisión.

## Estado comprobado del punto de partida

| Evidencia | Resultado y límite |
|---|---|
| Árbol de GitHub y copia local | 25 kits reales. Solo existe `data/kits/vivienda_salon.json`; faltan los otros 15. |
| Catálogos y texturas de vivienda | `vivienda.json` contiene 58 objetos. No existen los catálogos/kits A/B; `src/texturas/vivienda_a.js` y `vivienda_b.js` están conectados pero vacíos. |
| Inventario guardado en el commit | 23 viviendas: 22 de vecinos y una casa especial de Annie. Las 22 procedurales tienen 132 habitaciones habitables: 22 salones por kit y 110 habitaciones con el sistema anterior. |
| Informe guardado `casas.json` | 200 casas, cero errores, pero solo 200 estancias comprobadas: todos son salones. No demuestra que las demás habitaciones estén migradas ni validadas. |
| Informe guardado del salón | 81 semillas, cero errores/avisos; corresponden a 13 combinaciones distintas de perfil y estilo, no a 81 tipos de hogar diferentes. |
| Revisión visual guardada | `data/interiors_review.json` tiene rúbrica pero ninguna revisión registrada. No atribuirle aprobación visual formal. |
| Validación estática nueva, 17-10-2026 | 1.668 objetos y 25 kits; cero errores/avisos. Regeneración en directorio temporal: el JS resultante coincide con el commit. |
| Empaquetado nuevo, 17-10-2026 | Generación local correcta, control de marcas sin errores, sintaxis del módulo empaquetado correcta y cero líneas `export` sueltas. Esto no es una prueba de arranque en navegador. |

No se ha recuperado ninguna entrega de los dos agentes fallidos. En esta revisión se ha inspeccionado el contenido publicado; no se ha accedido a sus posibles archivos sin subir en el M5.

### Alcance de Annie

`buildAnnieHouse()` en `src/interiors.js` usa otro constructor, con distribución e interacciones propias. No dispone del registro `h.estancias` del sistema de vecinos. No formaba parte de la integración preparada para los dos agentes.

Recomendación: cerrar primero las 22 casas de vecinos. Conservar Annie y registrarla como casa especial pendiente de una migración propia; no marcarla completa por instalar los 15 kits. Convertir Annie requeriría un encargo y plan aparte sobre `src/interiors.js`.

Si no cambia ningún otro interior, el inventario esperado tras este alcance será: 125 puertas, 122 interiores completos, 3 básicos (Annie, kebab y armería) y los mismos 3 locales sin puerta. Es una expectativa que debe releerse en el inventario final, no un resultado actual.

## Review Focus

1. Una excepción del kit vuelve silenciosamente al mobiliario anterior. Debe conservar el diagnóstico y fallar la aceptación si ese kit era exigible; una habitación omitida no puede dar un falso verde.
2. Las casas estrechas y las habitaciones de arriba tienen puertas laterales y ventanas. Deben conservar giro de puertas, paso de 0,8 m, límite de altura y acceso a las piezas funcionales.
3. Una cama, cocina o armario visualmente correcto puede carecer de rol o tener el punto de uso dentro de una pared. Deben seguir funcionando sueño, comida, ocultación y cajones; el botín no se duplica ni se pierde.
4. `dorm` y `dorm2` comparten kit; el `taller` de una artista debe usar pintura. Los ensayos deben cubrir estas distinciones y no fotografiar un taller agrícola como prueba de pintura.
5. Las casas completas agregan todas las habitaciones y luces. Medir triángulos, mallas, luces y entrada de la casa real; verificar también el paquete y la partida guardada de HQ.

## Mapa de archivos y entregables

| Responsabilidad | Archivos previstos |
|---|---|
| Cobertura, diagnóstico y selección de dormitorio | Modificar `src/houses.js`, `src/locales.js`, `data/kits/kit.schema.json`, `tools/interiores/validar.js` y `validar.py`. |
| Pruebas de comportamiento de vivienda | Crear `tools/interiores/casas_pruebas.js` y `casas_pruebas.py`, aprovechando el transporte de pruebas existente. |
| Familia A: cocina, baño, comedor, despensa, trastero, taller, costura | Crear `tools/interiores/catalogo_vivienda_a.py`, `kits_vivienda_a.py`, `moodboard_vivienda_a.json` y el catálogo generado `data/objetos/vivienda_a.json`. Completar `src/texturas/vivienda_a.js`. |
| Familia B: dormitorio, niños, joven, estudio, despacho, música, trofeos, pintura | Crear los mismos cuatro archivos con sufijo `_b`; completar `src/texturas/vivienda_b.js`. |
| Kits nuevos | Crear `data/kits/vivienda_<id>.json` para los 15 ids de las tandas siguientes. |
| Integración y evidencia | Regenerar `src/interiores_datos.js`, informes de `data/interiores/validacion/`, fichas, inventario y revisión; ajustar `tools/interiores/fotos_casa.py`, `inventario.js`, `docs/interiores.md` y `.github/workflows/validar.yml`. |

Se preservan los scripts del salón. Los nuevos generadores no deben importar scripts que escriben archivos al importarse ni regenerar el salón como efecto lateral. Reutilizar objetos existentes con ids estables cuando sean adecuados; los nuevos ids no pueden colisionar con otros catálogos.

## Task 1: Hacer visible qué habitaciones faltan y qué funcionalidades deben conservarse

**Files:** los cinco archivos de cobertura del mapa; crear `casas_pruebas.js` y `casas_pruebas.py`; documentar opciones en `docs/interiores.md`.

**Interfaces propuestas:**

- `kitDeEstancia(tipo, perfil)` exportado desde `src/houses.js`: devuelve el id `vivienda_*` esperado o `null` para pasillo/vestíbulo. Extraer el mapa actual sin cambiar su resultado: `dorm`/`dorm2` → dormitorio; `taller`/artista → pintura.
- `h.fallosKit`: lista de `{sala, tipo, kit, motivo}` cuando un kit presente falla. Conservar el retorno al mobiliario anterior durante la transición, pero no ocultar su causa al validador.
- `validarCasas(seeds, opts = {})`, conservando llamadas existentes; `opts.exigirKits` y `opts.exigirTodas`. Añadir por casa `cobertura: {habitables, porKit, faltantes}`. Excluir solo `pasillo` y `hall`.
- CLI nuevo: `--exigir-kits <ids,separados,por,comas>` para una tanda y `--exigir-todas` para el cierre; `--casas-pueblo` enumera las puertas reales en el juego y usa sus semillas, dejando Annie explícitamente fuera del constructor de vecinos.
- Añadir el filtro opcional `habitacion` en las entradas del esquema, en `filtroHogar()` y en el filtro de `buildVecino()`. Recibe los tipos reales `dorm`/`dorm2`; permite conservar cama doble principal y variantes secundarias con un único kit. El validador aislado debe suministrar también este contexto y cubrir ambos tipos.
- `probarCasas()` en `casas_pruebas.js` devuelve `{pruebas, errores}`; su lanzador Python termina con código 1 si hay errores. Los fixtures de fallo se restauran al terminar cada prueba.

- [ ] Añadir pruebas que fallen con el comportamiento actual: una casa sin todos sus kits no pasa con `exigirTodas`; una excepción forzada del montador queda identificada por sala y kit; la casa conserva su cobertura real aunque `errores` geométricos esté vacío.
- [ ] Fijar el mapa con aserciones: `kitDeEstancia('dorm','familia') === 'vivienda_dormitorio'`; lo mismo para `dorm2`; taller/artista es pintura y taller/agricultor es taller; hall/pasillo devuelven `null`.
- [ ] Implementar las interfaces anteriores y hacer que la validación distinga fallos, habitaciones sin kit y habitaciones aprobadas. Un error de kit presente nunca debe quedar oculto en un informe de aceptación.
- [ ] Añadir pruebas del filtro `habitacion`: la entrada exclusiva de `dorm` no se activa en `dorm2`, y viceversa; los kits sin el nuevo campo conservan el mismo montaje.
- [ ] Ejecutar los nuevos ensayos y la comprobación de 200 casas exigiendo solo `vivienda_salon`: deben pasar los salones y seguir apareciendo las habitaciones restantes como pendientes. Con `--exigir-todas`, la base debe fallar de forma explícita.
- [ ] Comparar los salones de referencia y sus hashes con la base: no cambiar su distribución para añadir estos controles. Preparar revisión local de esta tarea, sin commit.

## Task 2: Primera tanda — cocina, baño y dormitorio

**Files:** generadores A/B, sus catálogos y texturas; `vivienda_cocina.json`, `vivienda_bano.json`, `vivienda_dormitorio.json`; datos generados y pruebas funcionales.

**Interfaces:** consume selección, filtros y cobertura de Task 1. Produce tres kits utilizables por el montador actual, con una sola zona `estancia` y modelos de hasta 2,4 m.

| Kit | Obligatorios funcionales y prueba |
|---|---|
| `cocina` | Mueble de cocina con `rol: cocina`, nevera con `rol: nevera`, preparación y almacenaje. En una casa real, `pieces.kitchen` no queda vacío; existen acciones `eat` y `fridge`, con puntos de uso alcanzables. |
| `bano` | Inodoro, lavabo, ducha o bañera, espejo y objetos cotidianos adecuados al tamaño. Obligatorios presentes sin invadir puertas/ventanas; espejo con su rol si se ofrece esa interacción. |
| `dormitorio` | Cama, armario, mesita y almacenaje. `dorm` conserva cama doble; `dorm2` admite variante individual/doble. `pieces.bed` contiene camas utilizables y hay ocultación/cajones donde corresponda; los ahorros del colchón se generan una sola vez. |

- [ ] Añadir primero las aserciones de la tabla sobre casas representativas con planos de pasillo, lateral y dos plantas; verificar el fallo antes de añadir los kits.
- [ ] Crear los muebles y objetos que faltan, con masas, superficies y roles. Los catálogos existentes no tienen objetos con roles de cama, cocina, nevera o armario: no confundir los modelos de exposición de tiendas con los muebles funcionales de una vivienda.
- [ ] Completar cada moodboard con al menos 10 referencias reales de Commons y su autor/licencia verificados. No copiar las imágenes al juego.
- [ ] Generar los tres kits y los datos. Para cocina, baño y dormitorio, respetar el mínimo de 60 objetos distintos referenciados por el kit; ese mínimo mide variedad disponible, no 60 objetos colocados a la fuerza en una habitación pequeña.
- [ ] Validar cada kit en 81 semillas; para dormitorio cubrir ambos tipos y todas las combinaciones de perfil/estilo aplicables. Validar las 22 casas reales y 200 sintéticas exigiendo salón más esta tanda.
- [ ] Comprobar acceso a camas, cocina, nevera, armarios y cajones; conservar botín, alturas y puntos de uso en ambas plantas. Capturar habitaciones estrechas y de dos plantas.
- [ ] Obtener revisión visual independiente, anotar los resultados y corregir antes de pasar a la siguiente tanda. Guardar el avance local sin publicar.

## Task 3: Segunda tanda — comedor, niños, joven, estudio y despacho

**Files:** ampliar generadores y catálogos A/B, sus moodboards/texturas y cinco kits `vivienda_<id>.json`. Datos generados, fichas y pruebas correspondientes.

**Interfaces:** consume las camas, armarios y contexto de Task 2. El cuarto del estudiante se identifica por `dormJoven` y carga `vivienda_joven`; no crear un tercer nombre incompatible.

- [ ] Añadir pruebas que exijan mesa/asientos en comedor; cama y armario en `ninos`/`dormJoven`; escritorio, silla y libros en estudio/despacho. Las camas de niños y jóvenes deben registrarse en `pieces.bed` y ser alcanzables, también en la planta alta.
- [ ] Añadir los kits `comedor`, `ninos`, `joven`, `estudio` y `despacho`. Mantener las diferencias entre familia, estudiante y casa acomodada, sin marcas reales.
- [ ] Conservar las funciones existentes de lectura, cajones y caja fuerte; todo botín debe coincidir con el perfil y aparecer como máximo una vez por casa.
- [ ] Usar tipología `dormitorio` y mínimo de 60 referencias para `ninos`/`joven`; `otra_estancia` y mínimo de 30 para comedor/estudio/despacho. No bajar mínimos para silenciar el validador ni rellenar catálogos con duplicados nominales.
- [ ] Repetir 81 semillas por kit, 22 casas reales y 200 sintéticas con los kits entregados hasta esta tanda; comprobar cobertura y presupuesto de la casa agregada.
- [ ] Capturar y revisar variantes de perfil, tamaño y planta, con el mismo criterio de Task 2. Guardar revisión y avance local.

## Task 4: Tercera tanda — despensa, trastero, taller, costura, música, trofeos y pintura

**Files:** completar familias A/B y los siete kits restantes; ampliar pruebas y corregir `fotos_casa.py` para diferenciar taller y pintura por el kit resuelto.

**Interfaces:** consume `kitDeEstancia()` y el catálogo ya integrado. Produce la cobertura completa de las 16 clases, incluido el salón existente.

- [ ] Añadir pruebas de selección y contenido: artista/taller → `vivienda_pintura`; agricultor/taller → `vivienda_taller`; música mantiene instrumentos; trofeos respeta el botín de cazador; costura y almacenaje no obstruyen sus accesos.
- [ ] Crear los siete kits con tipología `otra_estancia`, al menos 30 referencias distintas y 10 referencias visuales acreditadas por kit. Reutilizar mobiliario y objetos coherentes entre las familias.
- [ ] Preservar piano, guitarra, lectura, herramientas y botín que ya ofrece el juego. No inventar acciones nuevas para objetos que solo son decorativos.
- [ ] Añadir una selección explícita de captura por kit o perfil: la ficha de pintura debe contener casas de artista; la de taller, casas con `vivienda_taller`. Corregir también la salida que comunica cuántas casas se han capturado.
- [ ] Validar los siete kits en 81 semillas cada uno; exigir todas las habitaciones en las 22 casas reales y en las 200 sintéticas. Cero retornos al sistema anterior en habitaciones de vecinos dentro de este alcance.
- [ ] Obtener revisión visual independiente y guardar las fichas y correcciones de esta tanda. Annie sigue identificada como caso especial.

## Task 5: Cierre de integración, evidencia y entrega privada

**Files:** validadores, `inventario.js`, `.github/workflows/validar.yml`, informes, fichas, `data/interiors_review.json` y `docs/interiores.md`; registro de trabajo pertinente, sin atribuir al usuario aprobaciones que no haya dado.

**Interfaces:** consume los 15 kits nuevos y las pruebas anteriores. Produce inventario veraz, resultados reproducibles y un paquete local listo para revisión.

- [ ] Ejecutar todos los generadores nuevos y `datos.py`. Resultado esperado: 40 kits en total; sin ids repetidos, referencias rotas ni errores. Explicar/corregir los avisos, sin ocultarlos. Una segunda generación debe producir los mismos archivos.
- [ ] Validar los 16 kits de vivienda con 81 semillas por kit. El informe debe listar la cobertura de perfiles/estilos y contexto; no llamarla «81 hogares distintos».
- [ ] Ejecutar `validar.py --casas 200 --exigir-todas` y `validar.py --casas-pueblo --exigir-todas` (opciones nuevas de Task 1). Esperado: todas las habitaciones habitables de vecinos por kit, ningún fallo de montaje, ningún obligatorio ausente ni obstrucción. Si el inventario permanece igual, 132/132 habitaciones en las 22 casas reales.
- [ ] Ampliar la medición por casa completa: triángulos, mallas, luces y tiempos de entrada. La comprobación actual de `validarCasas()` solo mide triángulos y descarta errores de luz; completar ese control sin sustituir la revisión visible de iluminación.
- [ ] Ejecutar las pruebas funcionales y de circulación: camas y sueño de habitantes; comida/nevera; ocultación/cajones; botín; puertas, escaleras y ambas plantas. Usar `tools/housetest.js` para la parte de colisiones que cubre; no presentarlo como prueba de todas las interacciones.
- [ ] Regenerar inventario desde el juego y comprobar las 125 puertas, la cobertura real y el estado de Annie. Eliminar la lista genérica de cuatro estancias que el inventario asigna ahora a toda vivienda: informar las habitaciones construidas o declarar su constructor especial.
- [ ] Añadir al workflow de validación existente los ensayos funcionales y cobertura estricta de viviendas: 30 casas en PR y 200 en la ejecución nocturna/manual. Mantener los validadores de tiendas y rótulos. No modificar ni ejecutar el workflow de publicación.
- [ ] Empaquetar con `python3 tools/build.py`; pasar `python3 tools/rotulos/rotulos.py validar dist/test.html`; comprobar sintaxis del módulo empaquetado y ausencia de exports sueltos. Después arrancar el paquete local en navegador, entrar/salir de casas de ambas plantas y comprobar ausencia de errores de consola.
- [ ] Revisar visualmente muestras de cada kit y las habitaciones más pequeñas. Registrar dos revisiones con la rúbrica existente, corrigiendo antes de declarar aprobado. Comprobar al menos una muestra de las dos estéticas del juego.
- [ ] Comprobar que una partida de HQ sigue cargando y que no se han cambiado claves de guardado ni datos de Evolución/fija. Entregar el paquete y las fichas como archivos privados para revisión del usuario.

## Criterio de aceptación y autorización siguiente

El trabajo solo podrá declararse completado para **las 22 casas de vecinos** cuando todas sus habitaciones estén por kit y pasen cobertura, geometría, funciones, rendimiento y revisión visual. Annie se mostrará como caso especial pendiente, no como casa migrada.

La siguiente decisión solicitada es aprobar o corregir este plan. Recomiendo implementar en esta conversación, por las tres tandas indicadas, con revisiones independientes antes de cerrar cada una. La publicación queda para una autorización posterior y separada, aunque todo lo anterior pase.

## Comprobación del propio plan

- Se cubren las siete estancias A y las ocho B anunciadas en el trabajo anterior: 15 kits nuevos, más el salón existente.
- Se conservan motor, plano, estilos, perfiles y semillas; la ampliación de esquema se limita al contexto de dormitorio que el sistema actual no puede distinguir.
- Las cinco condiciones de Review Focus tienen pruebas o comprobaciones concretas asignadas.
- Las opciones, metadatos y archivos nuevos están descritos como propuestas, no como herramientas ya implementadas.
- No se incluyen pasos de commit, push, despliegue ni cambios de infraestructura.
