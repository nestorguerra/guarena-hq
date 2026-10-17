# Revisión independiente del candidato de carga de suelo

**Sin regresión concreta identificada de rutas, selección o empaquetado. Puede continuar el ensayo aislado.** No se acredita todavía la mejora del 25 %, el funcionamiento HTTP ni una integración/publicación. No he aplicado el parche, construido paquetes ni usado navegador/GPU.

Parche revisado completo: `carga_suelo.patch`, SHA-256 `51de064c0f0693ce23bb36b7b9778dfcd789ca5a4b4e52f4c186edbfe9cb51dd`. También leídos el autocontrol del autor, sus instrumentos y las fuentes/callers de assets, mundo, materiales, arranque, empaquetador, servidor multijugador y workflows.

## Evidencia independiente

- La selección es exactamente los doce JPEG de `GROUND_DETAIL`, más la iglesia que ya tenía tratamiento externo en Pages. Las trece rutas existen; `startswith` no atrapa otros archivos del árbol actual. Se reprodujo la selección y el ensamblaje del candidato en memoria; `git apply --check` pasó sin aplicar.
- En el build normal, Pages excluye esos recursos del JSON embebido y los copia a `dist/assets`. El workflow copia el HTML como `_site/index.html` y todo `dist/assets` como `_site/assets`. `new URL('assets/',document.baseURI)` resuelve las rutas de raíz y subruta conservando el repositorio. No se cambia el cargador ni sus claves.
- Portable y MP reinsertan los trece recursos en `assetdata` manteniendo `__enc:'b85'`. El servidor MP de producción no ofrece el árbol general de assets: esas copias embebidas siguen siendo necesarias y están presentes en la lógica propuesta. En `--split` no se ejecuta la reinserción y se mantiene el comportamiento externo anterior; split no adquiere autosuficiencia de archivo único.
- Ejecuté el **bloque real de ensamblaje candidato con los trece archivos binarios reales**, sin `main`, empaquetado de módulos ni escritura de dist. Después el decodificador real de `src/assets.js` recuperó **12.337.780 bytes con los trece SHA-256 exactos y cero fetch**. El bloque original de Pages y una entrada ajena de control quedaron intactos. Esto supera el alcance de los payloads sintéticos del autocontrol, pero sigue sin ser un build ni decodificación de JPEG/GLB.
- Reejecuté los instrumentos CPU inspeccionados del autor guardando resultados independientes: resolución de URL, prioridad embebida, peticiones externas, fallback de imágenes ausentes, normales planas y selección por modo pasan. Son dobles CPU de Image/canvas/red, sin solicitudes reales.
- `world.js` omite ambas matrices de suelo fotográfico en Plastilina. Realista espera seis albedos y, con sombras, seis normales antes de continuar. No hay otro consumidor de los seis nombres localizado en `src`. Se conservan selección de estilo previa a construir, partida e introducción.

Evidencia propia: `carga_suelo_revision_cpu.json`, `carga_suelo_revision_loader.json`, `carga_suelo_revision_integridad.py` y `carga_suelo_revision_integridad.json`, en esta carpeta.

## Observaciones y aceptación pendiente

**Observación menor — CI:** el contrato nuevo `tools/perf/tests/carga_assets.py` no se añade a los workflows. Incorporar su ejecución tras el build normal protege bytes y presencia embebida/externa de las tres variantes. El contrato preparado compara los archivos reales y sus codificaciones; no es una prueba del 25 %. Probar split por separado sobre un paquete split aislado.

Realista adquiere doce dependencias externas en Pages. Un error terminado tiene fallback; una petición pendiente no tiene timeout explícito en `loadImage`, por lo que puede retrasar el arranque. El caso parcial de texturas ausentes usa capas planas, no una recuperación procedural por capa. Son límites reales de esa nueva ruta de carga, ya reconocidos por el autor; falta verificarlos por HTTP y con imágenes reales antes de cerrar funcionamiento.

Los doce JPEG suman 2.253.348 bytes binarios. La retirada de unos 2,8 MB de texto base85 sin comprimir no equivale a esa reducción de transferencia ni de tiempo. Hace falta el A/B frío alternado con introducción completa y misma versión/calidad/red/caché. No se da por alcanzado el objetivo del 25 %.

Raíz comunica por separado un build físico y contrato de bytes favorables, más una prueba HTTP en curso. No son ejecuciones de este revisor y no se incorporan como resultados ya verificados por mí. El dictamen aquí es técnico y acotado: continuar las pruebas, conservar el candidato previo de comparación y decidir integración después de sus resultados.
