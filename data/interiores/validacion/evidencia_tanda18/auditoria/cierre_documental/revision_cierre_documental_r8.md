# Cierre documental R8 — T18

**Favorable acotado para cerrar el expediente previo al commit. Sin bloqueos documentales nuevos.** Esta revisión comprueba archivos y recibos locales ya producidos por raíz; no ejecuta gates, GPU, navegador, red, API, publicador ni helper de cierre. No acredita CI, Pages o publicación T18, todavía pendientes. No modifica fuentes ni dossier.

## Manifiestos y correspondencia

- Manifiesto del dossier: 336 entradas verificadas, sin hashes erróneos ni archivos sin inventariar (excepto el propio manifiesto). `manifest_pre_cierre.json` conserva las 330 entradas originales con los mismos hashes; las seis adiciones son documentos/instrumentos de cierre.
- Congelado activo: 417/417 hashes coinciden. El sello final PASS vincula exactamente el hash del congelado f56e7fef99302b69994357a92db02a09f2493575485cf50706899b0e6bf25181 y el recibo de nueve ejecuciones b18f1f6df786e909f837c42b227b08e3756722860834bc0ccdf2e7266c22a5cf.
- Los nueve pasos registran exit0. Contratos:79, errores[]. Regeneración:7 generadores,22 derivados idénticos,417 fuentes estables; comprobados también sus hashes actuales. Queda resuelto el pendiente de regeneración de mi informe anterior, que leyó todavía el recibo R6.
- Los cinco JSON de casas/laboratorio/integraciones del dossier coinciden con los activos; las copias de calidad_tanda18.json y revisión consolidada coinciden con sus originales. Los informes históricos mantienen su contexto temporal: sus pendientes anteriores no se reescriben como si ya estuvieran cerrados entonces.

## Cifras y estados

Las cifras declaradas corresponden a los recibos:200 casas sintéticas/1166 habitaciones,22 casas del pueblo/132 habitaciones,81 salones sin errores, ocho entradas fuente y paquete, consola vacía y partida inicial igual a la recargada. Los recorridos fuente suman16+32+16 y32 de Annie=96, sin escapes/túneles. La integración empaquetada conserva el alcance de sus acciones; no se atribuyen96 recorridos adicionales al paquete.

Máximos sintéticos calculados del JSON:73424 triángulos,60 mallas,9 luces,689ms. Pueblo:65456,60,9,481.7ms. Son montaje local, no FPS ni mejora del25%. El laboratorio registra7 admisiones de estar y1 de lectura, algo distinto de las5/2 del CPU de22 casas: la documentación circunscribe correctamente estas últimas a esas muestras, sin imponerlas al laboratorio.

La ficha activa es ahora R8 c1db0f3df8ed77d1d4b175d00f3a7fd73231822401811311c68db10c2d5c799b y el JSON fb038c8a8371c566d1924d448ad0bbd27aa4ac3f7bf9868220e0cf6a514063d9. Ambos juicios de salón apuntan a esa imagen, A3.248/B3.366, sin superar umbral. Las34 medias consolidadas coinciden con sus34 recibos; cada hash de imagen encuentra un archivo correspondiente. Esto comprueba trazabilidad, no reevalúa las imágenes ni recertifica otras habitaciones tras modelos compartidos.

Leídos los apartados T18 de ambos documentos, calidad_tanda18.json, LEEME y cabecera de la revisión consolidada. Conservan mejora parcial/4pendiente, cambios globales de los cuatro modelos frente a paleta sólo salón, cambio LINT efectivo, límites radiales del asiento, diferencias históricas de cámara/RNG, FAIL previos y dependencia de snapshots privados. No presentan el dossier como reproducción autónoma ni anticipan CI/Pages. El historial R6/R7 y los dictámenes anteriores siguen reconocibles.

## Instrumentos privados de publicación

Publicador: misma versión revisada de T17 salvo ruta T18. Mantiene SHA requerido, workflow validar.yml e identidad/éxito, ambos jobs obligatorios, árbol limpio/congelado, igualdad de árbol con PR y ascendencia antes del push sin force; relee main. No se ha ejecutado.

Probe final: exige composiciones de lectura/estar en1594/3244, la alfombra correcta y su cota .008, mesa orientada al sofá, centro común mesa/alfombra, separación proyectada contra las semiprofundidades y asiento exacto del puff en pieces.seat. La fórmula de gap es coherente con rot(x,z,a) del motor; aplicada por cálculo a los recibos existentes produce .55 en ambas muestras. Se registra sólo presencia del asiento, no sentarse.

Se señaló una omisión de cobertura: la primera versión comprobaba centro de alfombra, pero no su orientación respecto a mesa. Raíz añadió `Math.cos(rug.ry-mesa.ry)<.999999`; releída la guarda en el archivo final. Hallazgo cerrado por lectura, sin ensayo público. No era un bug de producto: las posiciones recibidas ya tenían las tres orientaciones iguales. Permanecen veto de shader, consola, revisión exacta antes/después y partida privada. Las aserciones geométricas del probe no sustituyen un juicio visual.

Helper cerrar_publicacion.py: leído el delta contra T17. Actualiza rutas, juicios de salón y dos programas públicos; exige1594/3244, gap .55 y un registro de asiento, conservando fuentes, manifiesto anterior, identidad CI/Pages, jobs build/deploy y validate_signs/validate_interiors, revisión exacta servida, recarga y relectura de main. Archiva los recibos antes de ampliar el manifiesto y distingue acciones disponibles de compras/sentarse. Es preparación condicional: ningún éxito externo se acredita por esta lectura. No se ha ejecutado.

## Cierre y límites

Puede incorporarse este informe al dossier con un hash nuevo y reconstruir su manifiesto sin modificar los330 originales. El producto permanece en el congelado revisado. La publicación sigue condicionada a los recibos reales del commit/CI/Pages y probe exacto, cuya verificación será posterior. No se exige otro barrido ni otra evaluación artística para este cierre documental.

## Huellas de este pase

- `data/interiores/validacion/evidencia_tanda18/manifest.json`: `4117e9667b34e00d6f7cd7520735aa9cfb8f7c436db014e2b56dca7bcfc72352`.
- `data/interiores/validacion/evidencia_tanda18/auditoria/cierre_documental/manifest_pre_cierre.json`: `92244bb60a80e4562c65a2b4f98d25aa2c8a1300be05f20a98a8da61b4058979`.
- `.cache/calidad/tanda18/validacion_sello_final.json`: `0eab18da771cb6e89e0ac7b6f96e0bddb323f4ec2755f4cde204baf900e7474b`.
- `.cache/calidad/tanda18/validacion_ejecuciones.json`: `b18f1f6df786e909f837c42b227b08e3756722860834bc0ccdf2e7266c22a5cf`.
- `.cache/calidad/tanda18/regeneracion.json`: `4f1a6580427520f3e52ad110e778fa57a4bc718096c4aca0f0f5597035ca443d`.
- `data/interiores/validacion/resumen_revision_visual.json`: `e87b063f92b7b1af377c518ca1fc869d1f09c50f11f6e94bacbcbb1caebaf193`.
- `data/interiores/validacion/calidad_tanda18.json`: `b62c5ec60a74c4964656d4ae9cf54e9be65675368db78dce19ccfa4ea6ea49da`.
- `data/interiores/revision_calidad_tanda18_2026-10-18.md`: `fbceabb583e09ba605b6eb5ce37add185e1b05c56916ba085605af0b986c9efa`.
- `docs/calidad-viviendas-4-2026-10-17.md`: `c72871654aaa63fdfd3b028a56fafb4cd7abc5ca6f019592240912a00be02565`.
- `docs/hiperrealismo-registro.md`: `ae5c159c71593d2b6200da8c03413e779a2d11f50e21ea71c366f1c6d516949d`.
- `.cache/calidad/tanda18/publicar_tras_ci.py`: `4b0ebcc47196e45cdaad8e016cfa6c3dca403fe671c0204449413a3a3a161e58`.
- `.cache/calidad/tanda18/verificar_publico.py`: `dd2253e6a5a5ad5a1a6c398a364f5b23655c3540b1fa3a2e449132b56d075724`.
- `.cache/calidad/tanda18/cerrar_publicacion.py`: `54d49d9cb506a23dc7c49289c9c4413fb98205bedd22d8094c02d967f9c36c59`.
