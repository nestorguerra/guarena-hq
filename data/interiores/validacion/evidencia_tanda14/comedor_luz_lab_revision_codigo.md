# Revisión independiente de luz del laboratorio comedor

**Sin hallazgos P1/P2. Aceptación estática para la validación real.** Parche SHA256 `5b503b2c494b6c5f177f400ad7b2b97eedd1c83c6a3f20f270c7381a7acc4b9f`. Revisión de sus cuatro archivos, contrato, fórmula, PointLight y calibración existente. No GPU, build ni cambios de producto por este revisor. Al comprobar los hashes finales, activa ya coincidía con los cuatro candidatos; esa aplicación concurrente no la ha realizado este revisor.

## Evidencia

- `src/housekit.js:83`: helper sin RNG devuelve exactamente `min(11,4+area*.32)` y `max(6,sqrt(area)*2.6)`. Comprobación propia de nueve áreas, incluidos0 y21.875 donde satura intensidad, PASS. No hay ciclo nuevo: locales/houses ya importaban housekit.
- `src/houses.js:344`: sólo extrae las dos expresiones; conserva B.light, coordenadas, color y resultado retornado. B.light sigue creando PointLight con decay1.6 y userData.base=intensidad. No modifica apagón, elección de sombras, luz cenital ni restauración.
- `src/locales.js:674–681`: rama exacta para vivienda_comedor. La altura ahora usa el y real de la luminaria más su emisor, en lugar de H más emisor menos.15. El modelo de esta receta tiene un único emisor centrado; su giro no introduce otro desplazamiento. Intensidad/alcance se calculan con el área real. Los otros kits mantienen expresiones, metadata y orden de llamadas anteriores.
- Metadata doméstica se extrae del PointLight creado, incluidos origen, y, intensidad y alcance; modoLuz casa usa la calibración ya existente en validar.js. El parche no cambia validador, umbral, presupuestos ni planos. No transforma un FAIL en PASS cambiando sólo el dato declarado: también modifica el foco físico del laboratorio.
- Contrato nuevo opts.tanda>=16: constructor real, tres semillas y origen alternativo; exige una sola fuente, posición del emisor, base/intensidad/distancia, metadata fiel, temperatura y revisar sin errores. finally dispone geometría. Los contratos previos quedan intactos. Comparar la fórmula contra el mismo helper protege integración, aunque no sustituye la comprobación independiente de equivalencia realizada arriba.
- Recibos del autor leídos:29/81 fallos previos sólo luz →0/81, colocaciones/hash/coste idénticos81; luces/metadata/coste idénticos de tres casas;12 laboratorios ajenos idénticos. Ejecución CPU con Three r170 y merge reales, Canvas sin raster. No he repetido ese barrido ni lo presento como ejecución propia/GPU.

## Hashes cotejados

- housekit: `f3da737e3c7d97ff8bf99948051b435602945251b4670a404c3e012ddc6dccdd`.
- houses: `a234706e81332076072aa362be06f387704b50a91577ab8843e10a4457fd15ea`.
- locales: `6b94e0edd33b35854110995bf4766c786f66e7d065ef9610fbc0e48b73be63c0`.
- casas_pruebas: `765a32cffee8f12b264a2ac7c723b73dda6f3c252e908246535285f9e382d4ea`.

## Declined to judge

Calidad visual, exposición percibida y sombras; FPS/GPU; ejecución real de fuente/paquete/CI; identidad cromática entre laboratorio y todos los estilos de casa; cobertura de toda semilla o cualquier futura luminaria con varios emisores/desplazamientos; publicación. El validador de iluminancia es una aproximación preexistente, no una medición física ni un juicio visual. El ensayo runtime final sigue siendo necesario.
