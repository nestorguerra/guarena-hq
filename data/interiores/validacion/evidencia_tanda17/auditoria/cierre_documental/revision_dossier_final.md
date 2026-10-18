# Auditoría documental independiente — cierre T17

18 de octubre de 2026. **Favorable para continuar a commit y CI: sin hallazgos P1/P2 documentales.** No acredita CI remoto, Pages, prueba pública ni calidad 4/5. No se ejecutó GPU, navegador, API, build, generadores ni pruebas funcionales nuevas.

Sello revisado: `data/interiores/validacion/evidencia_tanda17/manifest.json`, SHA-256 `127241ea73700f0b86f413889645a9ade73a9a5279f67c4e1b63f4edef8a9e88`.

La reproducción privada `revision_dossier_cpu.py` produce **43 comprobaciones PASS** en `revision_dossier_cpu.json`:

- Inventario exacto de **294 archivos**, excluido sólo el propio manifiesto raíz: ningún archivo faltante, sobrante o con hash diferente. Los manifiestos anidados están incluidos y cotejados.
- Las **415 fuentes congeladas** conservan sus hashes activos. Copias del congelado y de los recibos de gates idénticas a sus originales. Cinco generadores, **22 derivados idénticos**, también cotejados contra los archivos actuales.
- Nueve gates con salida 0. **73 contratos**, **40 kits × 5 semillas**, **200 casas / 1166 habitaciones**, **81 semillas de estudio** y cero errores. Integración fuente y paquete con consola y errores vacíos y partida ficticia conservada. Los **96 recorridos** corresponden a fuente, en distribución **16 + 32 + 16 + 32**, sin túneles ni escapes; no se atribuyen de nuevo al paquete.
- Máximos del resumen coinciden con los 200 registros: **70.192 triángulos, 60 mallas, 9 luces y 154,8 ms**. Son máximos de esa muestra y ese montaje, no FPS ni límites universales.
- Ficha final del dossier y ficha activa iguales: `cfe597964fc9e1c5626c9886a1521b01780fc4b5f558526003287dc4c7b04fc2`. Los cuerpos HTTP de ambos juicios coinciden con sus hashes y longitudes; status 200, sin truncamiento. Identidad de petición/ficha y respuestas normalizadas coherentes con los recibos finales. Cinco criterios únicos por juicio, niveles 0–4/etiquetas 1–5, confianza y probabilidades válidas, suma y medias recalculadas: **A 3,222 / B 3,208**. Ambos dejan el umbral incumplido.
- El informe técnico copiado al dossier y al registro activo es idéntico al privado; su recibo de **36 PASS** permanece intacto. Ese informe refleja su momento anterior al sello; esta adenda documenta el cierre posterior sin reescribir aquella procedencia.

Leídos el LEEME del dossier, el resumen `calidad_tanda17.json`, el registro independiente y las nuevas secciones de `docs/calidad-viviendas-4-2026-10-17.md` y `docs/hiperrealismo-registro.md`. Separan correctamente la revisión técnica, los juicios visuales y la publicación pendiente. Declaran dos estudios del inventario y la muestra sintética 1481; no convierten 23 identidades ni los laboratorios en viviendas reales con estudio. También explican que cinco de las seis cámaras históricas no coinciden, por lo que la diferencia de nota no se atribuye íntegramente al producto.

El dossier conserva la candidata R2 rechazada y su fallo GLSL, el diagnóstico RED→GREEN, fases de modelos/captura y fallos instrumentales previos. La cadena de historia frente a la base Git ya fue cotejada en las 36 comprobaciones que este sello incorpora. No se han sustituido aquellos fallos por el resultado final. El LEEME aclara que los snapshots privados sólo se incluyen parcialmente: **no contiene ni promete 298 fuentes de construcción duplicadas ni una suite autónoma**.

## Límites — Declined to judge

Esta auditoría verifica integridad y coherencia documental, no añade una evaluación artística ni demuestra que el objetivo 4/5 se haya alcanzado. Las pruebas de GPU y gates son los recibos de raíz, no nuevas ejecuciones de este revisor. El siguiente estado debe acreditarse por separado con el commit, CI remoto y comprobación pública del SHA exacto.
