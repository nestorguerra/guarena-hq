# T19 · auditoría independiente de recibos de publicación

**Sin hallazgos P1/P2 ni bloqueo documental para incorporar el recibo.** La afirmación de publicación y comprobación del producto `c486ed205510c1b94ba013846d17a2a1ad55ed4c` es coherente con los recibos locales examinados. Esta auditoría no volvió a consultar GitHub/Pages ni ejecutó el probe o el cierre.

Reproducción local: `auditar_recibos_publicacion.py`. Resultado `revision_recibos_publicacion_cpu.json`: **40 comprobaciones PASS**. No escrituras en producto, docs o dossier; sólo estos artefactos privados. No GPU, navegador, API, build, commit, push ni despliegue.

## Integridad y procedencia

- HEAD observado: producto `c486ed205510c1b94ba013846d17a2a1ad55ed4c`.
- Manifiesto auditado: `566c2b69a4aeee6b8d54d8855a6866278c13510aff1b80ad457fcd6d135ae6fd`; **169 entradas exactas**, sin archivos sobrantes/ausentes y con todos los hashes coincidentes.
- `publicacion/manifest_pre_publicacion.json` conserva exactamente el manifiesto de HEAD y sus **159 archivos** permanecen intactos. Los diez archivos nuevos de publicación no reescriben esa evidencia.
- Las **417 fuentes congeladas** coinciden con el contenido activo y no tienen diff frente a HEAD. Los **22 derivados** del recibo de regeneración también coinciden. No se regeneró ninguno.
- El informe público, su original en `revision_publicacion/ejecuciones/` y la copia intermedia son idénticos: `49f9d5d4e92190fec333f8d60ae65b92cc08a0d5939526ac2e48d38b1fbc7630`. El acta enlaza ese hash.
- Las copias de los tres instrumentos en el dossier son idénticas a sus originales privados. Se leyeron sin importarlos ni ejecutarlos. El LEEME advierte que las copias son evidencia y sus rutas relativas no las convierten en ejecutables autónomos.

El árbol de trabajo observado contiene únicamente los recibos/documentación pendientes de registrar: manifiesto ampliado, dos append de docs, subcarpeta de publicación y dos JSON públicos. No hay cambios de fuentes de producto. La auditoría mantuvo ese estado.

## CI, Pages y comprobación pública

`ci_final.json` registra CI **39099689341**, SHA exacto, `completed/success`, ambos jobs `validate_signs` y `validate_interiors` y todos sus pasos correctos. El recibo del workflow identifica `.github/workflows/validar.yml`. No se confunden las 30 casas del paso de PR con las 200 del gate local.

`pages_final.json` registra Pages **39099907357**, mismo SHA, `completed/success`, build y deploy correctos; el recibo separado confirma `.github/workflows/pages.yml`. El árbol Git local del producto y el del merge de CI `4864736c5a02ee98afc633f739397195b4b868b2` coinciden exactamente: `f48456ac256d5e2333031de6ac51bdb5ff0e7565`.

La integración pública registra HTTP200 y SHA exacto antes y después de recargar, errores/consolas vacíos. Conserva ocho entradas genéricas y cuatro dirigidas a trofeos 2132/4204/1679/2162; 2132 aparece en ambos grupos: son **once semillas distintas**, no doce. El acta no afirma doce.

Los tres bancos tienen selección real, sentarse, levantarse, salida libre y posición restaurada. El destino observado es `standPos` en los tres. 2162 mantiene banco0. La lectura del instrumento confirma métodos reales del juego, comprobación de collider .34 y patrimonio; no se ocultan residentes. La reposición al acceso es explícita y no se presenta como recorrido desde la puerta ni juicio de animación. Rifle/prismáticos y read/drawer se comprueban por sus identidades/definiciones; no se recogieron públicamente.

Annie registra cinco kits, depósito/retirada y siesta; los tres comercios tienen acciones, sin realizar compras. Dinero321, banco700, decoración y los dos testigos de otros guardados coinciden tras reload en documento nuevo. La fixture sólo se inyecta una vez por sessionStorage dentro de contexto privado, destruido al terminar. El instrumento llama a `game.persist()` antes de recargar: acredita **persistencia explícita**, no una nueva prueba de autoguardado. El acta conserva ese alcance sin afirmar autoguardado.

Los máximos 172,7 ms de entradas genéricas, 91 ms de trofeos y 89,5 ms de Annie se recalcularon del recibo. Son tiempos observados en esta ejecución, no FPS ni rendimiento universal.

## Gates anteriores y arte

Se cotejaron los recibos previos: 82 contratos PASS, diez gates únicos exit0, 200 casas/1166 habitaciones con cero pendientes/errores y 81 laboratorios de trofeos sin errores. No se ejecutaron de nuevo ni se convierten en una comprobación pública adicional.

La ficha formal tiene hash `c8a411c871c821ad153645e46117ca99b7098a27bba8241c8f6e581fae7cf792`; coincide con la ficha activa y la copia por contenido de ambos recibos. Cinco dimensiones, probabilidades y medias son coherentes: **A3,306/B3,368**, ambas con `supera_umbral:false`. El acta mantiene objetivo4 pendiente y no acredita mejora25% ni FPS. No se emitió otra valoración artística.

Los append de las dos páginas de documentación conservan íntegra la historia anterior y añaden una única declaración final de publicación. Las frases previas de publicación pendiente pertenecen al cierre anterior; el LEEME específico de publicación y los append posteriores permiten distinguir la secuencia.

## Declined to judge

Estado remoto posterior al recibo; disponibilidad continua de Pages; recorrido del jugador desde puertas; calidad de animación; recogida/compra pública; autoguardado sin `persist`; FPS o 25% de carga; nota artística propia, 4/5 o aprobación estética global. No se vuelven a ejecutar herramientas de un solo uso. La incorporación posterior de este informe cambiará el manifiesto documental, no el SHA del producto que se auditó.
