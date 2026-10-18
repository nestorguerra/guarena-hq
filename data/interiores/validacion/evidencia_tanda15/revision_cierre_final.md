# T15 — comprobación independiente de cierre

**Sin hallazgos P1/P2 de coherencia o procedencia.** El estado final examinado respalda el cierre técnico local de la tanda. No certifica CI, publicación, mejora universal ni acabado 4/5.

- Las **412 entradas** de `estado_candidato.json` coinciden por SHA-256 con los archivos activos. Comprobado de nuevo al terminar. El runner valida el mismo congelado antes y después de sus nueve comandos.
- Los **nueve gates** registran salida cero y sus logs contienen los resultados correspondientes: 66 contratos sin errores; todos los kits en cinco semillas; 200 casas, 1166 habitaciones y cobertura completa; 81 laboratorios infantiles literales; integración fuente; build; recursos; marcas e integración del paquete. Leídos además los JSON: cero errores en los 200 resultados y en los 81 infantiles. Los 96 recorridos fuente suman 16+32+16 en vecinos y 32 en Annie, según el informe JSON íntegro (el log omite el detalle de vecinos), sin escapes ni atravesamientos; fuente y paquete contienen ocho entradas vecinales y errores vacíos. No se atribuye al paquete el barrido de colisiones exclusivo de fuente.
- Las copias de gates finales coinciden con los recibos del runner donde corresponde. El manifiesto del dossier cubre **135 archivos**, todos con hash correcto. Regeneración declarada y preservada: 22 derivados idénticos. Los máximos de montaje son mediciones locales, no FPS ni garantía en otro hardware.

## Procedencia visual

La ficha activa, la ficha archivada Bv3 y la imagen inmutable ligada a ambos juicios A/B tienen el mismo SHA-256: `8a902376baea6e83f2457ae80ecd4cb4cdd6a82faeab26f1476ea741004a782e`. Su JSON activo coincide con el archivado. Se comprobaron los siete hashes de imagen de cada uno de los cuatro estados preservados, además del capturador conservado.

La procedencia Bv3 mantiene los hashes originales de `locales.js`, datos y kit anteriores al arreglo de laboratorio. `reutilizacion_capturas.json` distingue expresamente esa captura del estado actual y enlaza el recibo de invariancia `a355b1a3…`, cuyo contenido y hash se verificaron. No se ha sustituido retroactivamente la procedencia original por la fuente nueva. Las notas 3,488 y 3,208 siguen asociadas a la ficha exacta; mi revisión técnica no añade puntuación ni actúa como una evaluación artística.

La inferencia de reutilización está acotada a las construcciones conservadas y no se presenta como nueva igualdad de píxeles, sombras o todas las semillas. Las limitaciones de cámaras —5/6 iguales frente a pintura anterior, ninguna frente a T14— y los recortes constan en el agregado y en la revisión visual original.

## FAIL e historial

Se cotejaron **los 5 archivos de `historico_paso_v1` y los 10 de `historico_laboratorio_v2`** contra sus originales privados: copias exactas. El primer JSON conserva el FAIL de T17 en 4007. El segundo conserva los errores obligatorios de alfombra en 29/51/63 y sus 81 resultados originales. `ERRATA_CPU_81.md` explica que el primer wrapper CPU no equivalía a laboratorios literales con marco fijo y separa la corrección posterior. No se reclasifica ninguno de esos FAIL como PASS.

El agregado final ya reemplaza la marca transitoria de paquete pendiente por su resultado real y mantiene CI/publicación como posteriores. Una precisión terminológica sin impacto técnico: las 31 casas del control son construcciones por semilla; ese número no acredita que todas existan en el inventario público (1296 es una fixture sintética conocida).

## Alcance

Relectura estática, hashes, agregados deterministas y recibos existentes. Sin repetir barridos, GPU, navegador, build ni CI; sin editar producto ni crear commit. `revision_cierre_final_cpu.json` conserva los hashes del congelado, agregado y manifiesto examinados, los nueve resultados y los máximos leídos. No se reabren aquí las revisiones técnicas ya cerradas ni se emite aprobación visual o de publicación.
