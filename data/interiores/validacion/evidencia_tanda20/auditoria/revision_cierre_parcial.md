# T20 · Revisión independiente de helpers de cierre parcial

Dictamen: sin P1/P2 confirmados que impidan preparar o publicar el estado parcial mediante estos helpers, sujeto a sus precondiciones. Revisión de lectura y parseo AST; no se ha ejecutado ninguno de los tres scripts ni se ha publicado nada desde esta revisión.

## Versión revisada

- `preparar_cierre_parcial.py`: `364d4aa712be4d921227ba078c1dcbab710b4e8ed0d3c96107171ecec0d45e5c`.
- `cerrar_publicacion.py`: `ab43036f571f38b6162518ddf590998bc0e4838c6026ff860b7f9c5863c61a82`.
- `publicar_tras_ci.py`: `62a4a41f35de0ee7a73ee6ea00532337ef6f49fd91881b7cbdd250b5e7440986`.

## Evidencia contrastada

- Los diez registros de `validacion_ejecuciones.json` tienen `exit_code: 0`. El contrato contiene 82 pruebas y `errores: []`. Casas declara 200/1166 y cero errores. Los recibos dormitorio/joven contienen `resultados` de longitud 81 y `errores: 0`.
- Las 417 entradas de `estado_candidato.json` coinciden con los bytes activos durante la revisión. Se verificaron 34 evaluaciones históricas y el SHA de cada ficha; el helper no las reescribe ni les atribuye una evaluación nueva de R1.
- Fuente y paquete tienen `errores: []`. Las claves usadas para tiempos, resultados y errores existen en los recibos reales. `joven_visual/REVISION.md` existe y la versión revisada lo exige antes de crear el dossier. El sondeo adicional de dormitorio empaquetado también se exige antes de mutar.
- Publicar exige HEAD exacto, árbol limpio, sello de fuentes, CI del SHA exacto y workflow validar, los dos trabajos obligatorios en verde, árbol del merge PR igual y avance de main por ancestro. Relee main tras el push. No se confunde un intento con publicación verificada.
- Cerrar publicación exige SHA servido antes/después, ausencia de errores/consola, persistencia explícita, recibos de seis dormitorios/joven, trofeos, Annie y comercios; coteja CI/Pages y main. La forma `dormitorios.rows` y su orden de semillas coincide con el emisor privado leído. Conserva el manifiesto previo y comprueba que sus archivos no cambian antes de sellar el ampliado.
- Los textos distinguen publicación parcial, ausencia de nueva nota formal, objetivo 4 pendiente y límites de la prueba pública. No presentan esta revisión como juicio artístico ni certificación de rendimiento.

## Observación menor de esquema

`preparar_cierre_parcial.py`, bucle que actualiza `s['kits']`: `d.get('avisos', 0)` lee una clave que los recibos no tienen. Los avisos están en `resultados[].avisos`. La expresión adecuada es `sum(len(f.get('avisos', [])) for f in d['resultados'])`. En los 16 recibos domésticos actuales la suma es cero en todos, por lo que no hay error en la cifra que documentaría este cierre. P3, sin bloqueo actual; no modifiqué el helper.

## Límites / Declined to judge

No se han ejecutado helpers, comandos de red, git con mutaciones, CI, Pages, navegador, GPU, API, pruebas del juego ni generación de arte. La futura publicación y su recibo no están certificados por este informe: los scripts deben completarse y sus resultados verificarse. No se reevalúa calidad artística, no se exige otra tanda ni puntuación, y no se garantiza idempotencia frente a una interrupción a mitad de escritura de estos cierres de uso único. La fotografía/revisión compartida joven se exige como precondición; aquí sólo se verifica su presencia, no se sustituye su revisión visual.

## Adenda final: correcciones instrumentales de raíz

Se relee el helper con suma de `resultados[].avisos`: P3 cerrado. Su precondición ahora exige `dormitorio_paquete_corregido.json` PASS y consola vacía; conserva ambos intentos JSON/log y copia ambos instrumentos. El FAIL previo no se cuenta como PASS ni se elimina. El nuevo sondeo aún debe ejecutarse y su corrección por receta/geometría queda bajo revisión independiente de publicación; este informe no certifica su comportamiento ni el futuro resultado. Ninguna corrección de producto ni nueva evaluación artística forma parte de esta adenda.

SHA releído de `preparar_cierre_parcial.py`: `981208af231cf839315ab0f41dbad5f686c60a856cc9dcd3e3e5c17611d1d6dc`. Los otros dos helpers mantienen los SHA consignados arriba. Dictamen instrumental sin bloqueos P1/P2, condicionado al PASS del sondeo corregido y a las precondiciones de publicación ya descritas.
