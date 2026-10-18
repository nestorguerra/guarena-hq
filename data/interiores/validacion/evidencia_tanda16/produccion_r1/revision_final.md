# Revisión independiente T16 — cierre técnico R1

**Sin P1/P2 pendientes en el motor `0e79151039e3eff3eff7cf718c100545197e311ec7cc461508ce0dd85644301a` y contratos `4fe8f2a3465906708b8dc05f936e7b45a8d2b1c3d3c08c85aea20e85e35a37f5`.** Admisión técnica acotada para integración y validación runtime posterior. No constituye aprobación visual ni publicación.

## Procedencia

Reconstruí en memoria los cuatro patches desde `base/` y cotejé byte a byte cada fuente resultante con `candidata/`: 5 archivos de motor, 3 de modelos/receta, 1 de contratos y 1 de capturador. `revision_parches.json` y `revision_final_manifest.json` fijan hashes de patches, fuentes y recibos leídos. El manifest del autor aún mostraba el sello anterior de motor/contratos al leerlo; este cierre identifica los bytes actuales, no ese manifest pendiente de actualizar.

## Hallazgos subsanados

- **P2, confianza del mínimo de cocina:** el antiguo condicional heredado `if(L.activas)` permitía ocultar una nevera ausente quitando su entrada de activas. No se atribuye como regresión publicada T15. La incorporación de receta efectiva exigía cerrarlo para este programa. `tools/interiores/validar.js:25` parte ahora de `base.composicion_cocina`, mantiene cuotas/obligatoriedad globales y filtros de hogar/área; difiere únicamente la fase de composición cuando esta no se compromete. Mi prueba de 2786 elimina nevera/reindexa referencias y omite activas: falla incluso suprimiendo ambos metadatos. Rebajar cantidad y obligatorio también falla. Los cuatro fallbacks reales conservan la receta base y no exigen pan diferido. Recibo: `revision_cierre_gate_cpu.json`.
- **P2, dependiente con acción:** la guarda inicial comprobaba campos del objeto, pero omitía las rutas reales de entrada `e.interaccion`/`e.vende`. Mi caso no vacío de entrada18/semilla365022 producía 3 lecturas o compras en base y 0 tras componer. `src/locales.js:677` cubre ambas rutas. En los bytes finales comprobé **3→3**, composición cancelada en ambos casos; permanece el RED anterior en `revision_final_funcional_cpu.json`. Recibo GREEN: `revision_cierre_funciones_cpu.json`.

## Comprobación independiente

- Cuatro fallbacks 3627/2606/4007/4216: 33/30/40/41 colocados; P, activas, guardias, avisos, debe, W/D/H/puerta y siguiente extracción U iguales frente a base. Dos no optantes dirigidos (bar e infantil) conservan resultado serializable íntegro y U. No se reescribe KITS. Recibo `revision_cierre_fallback_cpu.json`.
- Reejecuté los callbacks literales finales: **3 nuevos T19 + 1 umbral existente**, todos PASS. Conservan negativos de cuota, reserva, omisión de metadata, apoyo/penetración y dependiente funcional no vacío. **No son los 66 contratos previos.** Recibo `revision_cierre_contratos_cpu.json`.
- Tres constructores reales CPU 2786/3244/1594: IDs/defs y poses de botín idénticos; tipos e identificadores de acciones de cocina conservados. El retiro de 462 PICKUP de decoración en las 18 composiciones del recibo del autor no equivale a 462 acciones: esas entradas/modelos no tenían botín/interacción/venta/valor; los PICKUP se agrupan como geometría. La sustitución de la alacena conserva el rol de guardado. No ejecuté acciones/persistencia en navegador.
- Pase final optativo: candidatos clonados, P restaurado tras ensayo, K/activas comprometidos sólo tras guardas; no llamadas aleatorias nuevas. Reservas de huecos y frentes, límite de estancia/altura, partes reales y cierre de uso preceden al compromiso. Índices sop/de se remapean; actividad usa sup0 de preparación. No mueve núcleo, mesa ni sillas.
- **Sólo modelos R1:** mis 13 compuestos no penetran >1e-6 y tienen apoyo completo de contenidos; las 12 variantes de núcleo conservan geometría/superficies/roles. El recibo de autor de 22 construcciones completas CPU registra 18 composiciones/4 fallbacks y costes dentro de60 mallas. Canvas/texturas son dobles sin raster; Three/merge y geometría son reales. Estas pruebas no se transfieren a R2 artística.
- Capturador `df5e101a…`: sólo normaliza los tres sufijos de familia para reconocer preparación. La búsqueda completa CPU del autor conserva seis poses sobre la misma geometría BASE. Esto no demuestra igualdad de cámaras entre geometrías distintas ni valora imágenes nuevas.

## Declined to judge

Calidad estética, nota formal, pan/cuchillo/vajilla R2, píxeles, renderer/GPU, sombras/apagones runtime, rendimiento real, acciones y persistencia en navegador, publicación, y cobertura universal fuera de semillas/negativos descritos. Tampoco se interpreta el recibo CPU como ejecución de los 66 contratos anteriores. El navegador completo y pipeline quedan a cargo de raíz tras integrar.
