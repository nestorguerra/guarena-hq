# Fallback HTTP v2 — diagnóstico y preparación

Estado: **PREPARADO; no ejecutado en navegador/GPU**. Producto, script v1 y resultados v1 intactos. Pruebas CPU: sintaxis Python, CLI --help y clasificador de errores con casos positivos/negativos. No se ha iniciado servidor ni realizado build.

## Evidencia v1, acotada

`ground-http-fallback-t12/report.json` terminó en `albedo_exact_flat_only_missing`. Había control normal, alta/manual, groundFx activo, iglesia, errores JS vacíos y glError=0. Esto no acredita las garantías restantes: el movimiento no llegó a comprobarse.

Además del albedo intencionadamente ausente (capa 0), quedó plano `withered_grass_d` (capa 5), con ERR_CONNECTION_RESET. En normales quedaron planas la capa 1 (`dirty_concrete_n`, ERR_SOCKET_NOT_CONNECTED) y la capa 2 (`dry_ground_01_n`, ERR_CONNECTION_RESET). La normal que se pretendía bloquear nunca alcanzó el servidor, por lo que v1 **no ensayó dos 404 HTTP**. También hubo seis ERR_CONNECTION_RESET de texturas del interior de iglesia. Nueve fallos de transporte y nueve mensajes de consola asociados: 18 eventos inesperados conservados por el clasificador v2 al releer v1.

La cola de aceptación por defecto de ThreadingHTTPServer (5), combinada con HTTP/1.0 y muchas conexiones simultáneas, es una causa plausible del fallo del servidor de prueba. El informe no contiene trazas de kernel/socket que permitan demostrar que ésa fue la causa única. El ensayo v2 debe confirmar o refutar la hipótesis; no se atribuye el fallo al juego ni se afirma corregido antes de ejecutarlo.

## Cambios privados

`ground_http_fallback_v2.py`, diff completo en `ground_http_fallback_v2.diff`:

- Servidor con `request_queue_size=128`, hilos daemon y HTTP/1.1. SimpleHTTPRequestHandler envía Content-Length para archivos y errores; el 204 de favicon añade Content-Length: 0. HTTP persistente permite reutilizar conexiones.
- Captura también excepciones del servidor. Cualquier excepción, reset o socket desconectado continúa siendo inesperado, incluso sobre las dos URLs bloqueadas.
- Mismas dos JPEG con 404 exacto y únicas; las otras diez deben responder 200 una vez en servidor y navegador. Iglesia 200. Capas ausentes exactas y otras diez no planas; ningún criterio geométrico/funcional se relaja.
- Conserva introducción normal, calidad alta/manual, movimiento real, contexto privado, errores JS/GL, captura y salida que rechaza sobrescritura. Nuevo candidato por defecto: `candidate-ground-t12/dist`; nueva salida: `ground-http-fallback-v2`.
- Clasifica errores también en finally, aunque falle antes una aserción. Escribe `report.json`, `http.jsonl` y `events.jsonl`, sin vaciar los eventos originales. Un error tardío del servidor impide estado de éxito.

## El 404 opcional de rótulos no se oculta

`src/rotulos.js:12–17` consulta `data/rotulos/reales.local.json`; el comentario y el control `r.ok` indican que la copia publicada conserva nombres públicos cuando ese fichero privado no existe. `.github/workflows/pages.yml` copia HTML y assets; no copia data. V1 recibió el 404 correspondiente.

V2 exige que ese archivo privado no exista en el paquete y registra **por separado** `optionalLocalErrors`. Debe observar exactamente una respuesta 404 real en servidor y CDP para esa ruta; no se sustituye por 200/JSON vacío, no se intercepta fetch, no se borra la consola. Sólo su 404 y mensaje network asociado con URL exacta pueden entrar en esa categoría. Un 403/500, reset, error JS o console.error sigue siendo inesperado. Las dos JPEG intencionadas siguen en `expectedGroundErrors`. Por tanto, el ensayo tiene dos fallos JPEG intencionados y un 404 público opcional explícito, no “cero errores de red”.

## Ejecución pendiente

Sólo por la raíz con la GPU libre y Chrome 9333 con --mute-audio:

```sh
python3 -B .cache/perf-beta/ground_http_fallback_v2.py --execute
```

El registro CPU y hashes están en `ground_http_fallback_v2_cpu.json`. La comparación v1 queda íntegra con SHA256 `e7852a7f143132e1ede13c4173c03ed971199fa358f7468dfad717ee451f1ca0`.

Límites conservados: no prueba peticiones pendientes indefinidamente (`loadImage` no tiene timeout propio), corrupción JPEG con 200, todas las combinaciones de ausencia, calidad visual ni mejora de carga del 25 %. La mayor cola no autoriza a ignorar un solo fallo imprevisto del próximo ensayo.
