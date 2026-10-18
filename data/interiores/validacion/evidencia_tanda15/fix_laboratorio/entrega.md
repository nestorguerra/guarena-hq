# T15 — corrección acotada del laboratorio infantil

**CPU GREEN con constructor y validador literales; gates de raíz pendientes.** El autor sólo ha escrito la candidata privada. Raíz comunicó integración local del motor y regeneración desde fuentes activas. No se usó GPU, build, CI ni publicación.

## Deltas

- `motor.patch`: `36741ece79bdbbfb4d2d26855a53e233e9e62b3267929eb56a37682e4ffcec42`.
- `contratos.patch`, dos callbacks con gate **18**: `d307663d86d2ae8d178c872e777dd82fee8e9a115d35c902925cbb2c27702bef`.

El motor tiene revisión independiente sin P1/P2; la adenda de contratos se coordina con código_final. No incluye modelos, acabados, casas, cámaras, workflows ni compilados.

## Cambio

Opt-in `suelo_determinista:true` sólo en las dos alfombras infantiles obligatorias. Conserva los200 tiros previos y cualquier colocación exitosa. Sólo si faltan piezas, prueba cuatro ejes y una rejilla de5 cm con límites reales de huella, margen .01 y máximo16.000 candidatos. Reutiliza `dentro/libre/cierra`; no toma RNG adicional. Es una búsqueda finita, no una prueba de que todo hueco posible sea hallado.

`buildLocal` reintenta sólo vivienda_* ante mínimos ausentes: máximo12 intentos incluyendo el original, seed base+i×104729. Fija W/D/H originales y conserva contexto, filtro, reservas y puerta; si la puerta cambiase, falla explícitamente. Toda la construcción y la luz usan el intento seleccionado. Mantiene la semilla solicitada como identidad y añade traza con semilla efectiva/intento/marco/agotamiento sólo cuando interviene búsqueda o reintento. `validar` persiste esa traza. El wrapper no sustituye la validación completa: densidad, luz, colisión y demás errores siguen siendo gates.

## Evidencia

- RED inicial reproducido exactamente:29 `d8ee0517`,51 `83fa2dc0`,63 `ce625c71`.
- GREEN literal:29 pasa en intento1,51 en intento1 (468 candidatos deterministas),63 en intento0 (1.683 candidatos). W/D/H y puerta idénticos a los originales; montaje repetido determinista.
- **81 laboratorios infantiles GREEN**. Los78 anteriormente válidos conservan h.local completo, posiciones, luces y hash.
- **31 casas completas idénticas** en estancias, navegación, geometría, luces y extracción U posterior. Ningún cambio de layout por adelantar un intento.
- **39 otros kits**, semilla1: metadata completa idéntica. No se atribuye una cobertura39×81 a ese control.
- Negativo con toda la zona reservada: agota exactamente12, conserva3,5×2,1×2,75 m y puerta−.75, mantiene el error de alfombra y demás cuotas incumplidas.
- Dos callbacks permanentes exactos ejecutados en CPU: PASS. `git apply --check` del contrato: PASS.

Recibos: `tres.json`, `controles.json`, `contratos.json`; hashes en `entrega.json`. Los datos fuente activos corresponden a locales `6a86a62488f1d3162387c32414bd7c244b321f0d85658507ecf9cddbbf10dad3`, kit `e04c07747886e8b397591a75b8be28cd0f527eff5812fe522a90f7a63fe8ad66` y catálogoB `42d80ffe515d45e7f3dde04b602601ac008b3e184ca9150f5f0bf83b4b8f769e`. Se usan JSON en memoria, no un compilado antiguo.

Al integrar raíz durante la preparación del contrato, la guarda de procedencia detuvo el primer ensayo: se conserva en `historico_guardia_post_integracion.stderr`. La ejecución posterior usa los originales afectados ya sellados en base.json más el delta privado; las dependencias intactas siguen cotejadas por SHA. No se contó el intento detenido como PASS.

La errata del anterior helper sintético permanece en la entrega Bv3. Estos recibos nuevos corrigen la equivalencia de prueba; no borran el alcance erróneo anterior ni acreditan navegador, rendimiento o publicación.
