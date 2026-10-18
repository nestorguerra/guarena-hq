# Cierre documental independiente T16 — 18 de octubre de 2026

**APROBADO para continuar con commit y CI; sin P1/P2 pendientes en esta auditoría.** La publicación debe seguir condicionada al CI y a la comprobación pública del SHA exacto. Este dictamen no ejecuta ni certifica esos pasos y no añade aprobación artística ni nota.

## Integridad y procedencia

- **160 archivos** del dossier coinciden con su manifest, sin ausentes ni extras. El primer sello157 omitía los tres manifests anidados por un filtro de nombre; raíz lo corrigió y conservó el sello157 privado. No era un cambio de producto ni una copia concurrente. Manifest final auditado: `68e9a0f21c971bdd9ae450e038ce2299c6527bd90efc6bb37050b80e12d3551a`.
- **413 entradas** de estado_candidato coinciden con las fuentes activas. Congelado auditado: `7b28c42f49f4bfdd837c300268b8c7b0241b9cbba0da1cc2cdbf92c7625fad8b`.
- La captura final precede sólo a dos cambios dentro de ese conjunto: callback artístico y transmisión de metadata de Annie. Los hashes antes/después coinciden exactamente con ambas anotaciones de reutilización. Fuente/modelos/capturador de las cocinas fotografiadas permanecen iguales; no se reescribe el recibo como imagen nueva.
- La ficha archivada, activa e imagen inmutable tienen el mismo SHA `d445639e300adceccfb7f0c9ed2c9e95064091633584c115b2e4db0ab815fc91`. Las seis poses/objetivos/FOV coinciden exactamente con baseT15 comparable, calidad alta/DPR1 y guardas candidate/beforeRender/afterRender libres. No se infiere igualdad de iluminación por estos datos.

## Coherencia de resultados

Los dos juicios archivados coinciden con recibos activos, respuestas conservadas, request-id y ficha. Cotejé también los cuerpos HTTP privados con SHA y JSON de las respuestas, sin red/cliente/credenciales. Niveles, probabilidades, expectativa, conversión score+1 y medias recalculados: **A3,276/B3,256**. No superan4/5; calidad_tanda16 y agregado lo declaran expresamente. La limitación de comparar esas notas con una ficha histórica de tres poses distintas está documentada: no se presenta como mejora causal exclusiva del código.

Leídos los nueve registros de salida0 y los recibos que los respaldan: **69/69 contratos**,40kits×5semillas,200casas/1166habitaciones,81cocinas literales, fuente/build/recursos/marcas/paquete. Recálculo de máximos de las200casas:70.192triángulos,60mallas,9luces,162,9ms de montaje; no FPS. Regeneración22derivados exacta. Fuente registra96recorridos distribuidos16+32+16vecinos+32Annie, sin escapes/túneles; fuente y paquete registran8entradas,Annie,3comercios y partida ficticia igual tras recarga, sin errores/consola.

El FAIL previo de Annie permanece en historico_annie_metadata_v1:68PASS y1FAIL de ese contrato. Los cierres técnicos y hashes finales distinguen R1, R2 y contrato75069a18, sin transferir aprobación geométrica entre versiones ni presentar callbacksCPU como69tests de navegador. La corrección de fecha del agregado a18oct no cambia fechas originales de recibos. Docs y agregado reflejan publicación pendiente y objetivo visual abierto.

## Límites

Auditoría sólo lectura/cálculo sobre recibos; no repetí GPU, navegador, tests del producto, build, CI ni API. No juzgué imágenes ni autoricé un envío/publicación por mi cuenta. Los instrumentos históricos privados no son un paquete autónomo de reproducción, limitación explícita del dossier. La evidencia conservada no convierte una evaluación visual en prueba funcional. La prueba pública y CI del futuro commit quedan pendientes de raíz.

Evidencia propia: `revision_cierre_cpu.py` y `revision_cierre_cpu.json`, con hashes y comprobaciones deterministas. No se modificaron fuentes, docs ni dossier.
