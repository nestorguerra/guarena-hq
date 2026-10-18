# Propuesta de CI y revisión de cargas pendientes — suelo fotográfico

**Preparado, no aplicado.** El parche privado `carga_suelo_ci.patch` añade exactamente dos pasos (cuatro líneas) a los workflows. No toca el juego, el empaquetador, el contrato ni sus límites de tiempo. No he ejecutado build, contrato de paquete, navegador o GPU.

## Integración mínima

- `.github/workflows/validar.yml:39`: ejecutar `python3 tools/perf/tests/carga_assets.py` después del build normal y antes de validar marcas. Usa Python 3.12 ya instalado en ese job.
- `.github/workflows/pages.yml:42`: el mismo contrato después del paso que construye y prepara `_site`, antes de configurar/subir el artefacto. Si falla, el job `build` falla y `deploy`, que declara `needs: build`, no publica. No hay `continue-on-error` ni `if: always()` en el contrato.

El contrato examina `dist/assets`, `dist/test.html`, `dist/guarena-hq.html` y `multijugador/guarena.html`. La copia a `_site` sigue siendo la existente; ningún paso modifica sus recursos entre copia y comprobación. El contrato no valida directamente el artefacto remoto publicado.

**Dependencia de integración:** aplicar junto al candidato `carga_suelo.patch`, que incorpora el nuevo archivo `tools/perf/tests/carga_assets.py`. Aún no existe en las fuentes activas al revisar. Aplicar sólo el parche CI haría fallar ambos workflows por archivo ausente. La variante normal actual de ambos workflows coincide con el modo por defecto del contrato; no añadir `--split` a estos builds normales.

## Qué prueba y qué no prueba el contrato

Compara exactamente los doce JPEG de suelo y la iglesia con los binarios de origen; presencia externa y presencia/ausencia embebida según las tres variantes; codificación base85. No vuelve a construir: `runpy.run_path` carga las funciones de `tools/build.py` sin entrar en su guard `__main__`.

No comprueba respuestas HTTP, decodificación de JPEG, arranque, solicitudes pendientes ni rendimiento. Los contratos normales favorables en `candidate-ground` son resultados previos comunicados por raíz; no los he repetido.

## Error terminado frente a petición pendiente

| Estado real | Código y consecuencia |
|---|---|
| Imagen externa cargada | `src/assets.js:21–28`: `onload` resuelve la promesa con Image. |
| Fallo de red/decodificación que emite `onerror` | `src/assets.js:26`: resuelve `null`, no rechaza. Una vez resueltas las demás imágenes, `loadTextureArray` rellena esa capa con gris o normal plana (`:104–123`). Un fallo terminado por sí solo no bloquea; otra petición pendiente sí puede hacerlo. |
| Solicitud que sigue sin `onload` ni `onerror` | No hay temporizador, cancelación ni límite aplicativo en `loadImage`. Su promesa permanece pendiente. El límite que pueda imponer el navegador no está definido ni garantizado por el juego. |
| Alguna de las seis promesas de una matriz queda pendiente | `Promise.all` en `src/assets.js:104` no entrega la matriz. No llega al bucle de capas planas, porque éste empieza después del await. |
| Matriz de suelo pendiente en Realista | `src/world.js:220–223` espera albedos y, si `q.shadows>0`, normales. Bloquea ese tramo de `World.build`, `Game.init` (`src/game.js:128`) y `boot` (`src/main.js:108–119`), antes de retirar loading/iniciar la introducción completa. |

En Realista con sombras se solicitan doce JPEG; sin sombras, seis albedos. Plastilina omite ambas matrices. Portable y multijugador conservan copias embebidas y por tanto evitan estas doce dependencias de red en el camino normal; un error de decodificación embebida puede entrar en el fallback de red (`src/assets.js:80–92`).

**No confundir alguna capa válida con todas cargadas:** `loadTextureArray` devuelve `any: ok.some(Boolean)` y `groundFx.on/normals` usan ese valor (`assets.js:132`, `world.js:224`). Por tanto ambos flags pueden ser verdaderos con varias capas fallidas. El comprobador HTTP leído, `ground_compatibility_v2.py:23–31`, añade la igualdad de los doce nombres, estado 200 y bytes; eso sí cubre cargas terminadas de cada fichero en una ejecución satisfactoria. Las entradas completadas de Resource Timing no certifican por sí solas que no haya solicitudes todavía pendientes. Un caso detenido antes de LISTO no puede evaluarse sólo a partir del estado final.

No añado timeout ni propongo una cifra arbitraria dentro de este cambio CI. Si se exige arranque acotado ante una petición eternamente pendiente, hace falta un cambio separado de política: alcance limitado a esas matrices, plazo explícitamente acordado, fallback por capa y control de respuestas tardías. La prueba decisiva sería retener deliberadamente una de las doce solicitudes (sin completarla con error) y observar el comportamiento autorizado; no se ha ejecutado aquí. Un 404 no reproduce ese caso.

## Evidencia de rendimiento y alcance

Leídos `cold-ground/setup.json` y `summary.json`: tres rondas, 12 Mbps, estilo **Plastilina**, semilla 388, introducción normal sin adelantar, sin adaptación. Medianas de tiempo hasta control: 48.744,9 → 36.236,4 ms; reducción 25,661146 %. Es evidencia del ensayo aislado citado por raíz. No mide las esperas externas del arranque Realista ni acredita que cualquier equipo/red mejore ese porcentaje. El contrato añadido no compara rendimiento ni declara ese objetivo alcanzado en CI.

## Verificación de esta propuesta

- YAML analizado con `yaml.BaseLoader`: ambos documentos válidos; contrato después del build; en Pages, antes de upload y `deploy` dependiente de build.
- AST del contrato candidato válido, sin ejecutarlo.
- `git apply --check .cache/perf-beta/carga_suelo_ci.patch`: PASS, sin aplicar.
- Recibo: `carga_suelo_ci_comprobacion.json`.

SHA-256 parche CI: `c5f58d88a7283971b97384cb25a29733c882bac0e72399a78b3b8a698319305f`.
SHA-256 candidato de carga revisado: `51de064c0f0693ce23bb36b7b9778dfcd789ca5a4b4e52f4c186edbfe9cb51dd`.

Fuera de juicio: aprobación visual, publicación, disponibilidad de HTTP, tratamiento de peticiones eternamente pendientes y generalización del 25 %. Este informe sólo propone la puerta CI y describe el comportamiento observable del código leído.
