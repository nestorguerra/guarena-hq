# T19 R8 · auditoría documental previa al commit

**Favorable en el alcance revisado; sin bloqueo documental P1/P2 identificado.** El expediente demuestra preparación y validación local. No acredita todavía commit, CI, Pages ni comprobación del SHA público. Sólo he leído archivos/recibos, calculado hashes y ejecutado git diff --check; no he repetido juego, GPU, build, API o gates.

## Integridad y preservación

El manifiesto original contiene150 entradas: todas existen y sus SHA256 coinciden; no hay archivos adicionales sin declarar, aparte del propio manifiesto. El congelado de417 fuentes sigue íntegro. El sello final PASS enlaza exactamente el hash del congelado y el de las diez ejecuciones, todas exit0. Los22 derivados actuales coinciden con el recibo de regeneración de los siete generadores. Las copias de cierre y del informe consolidado coinciden con sus archivos activos.

Ficha activa JPG c8a411c871c821ad153645e46117ca99b7098a27bba8241c8f6e581fae7cf792 y JSON7ae8326e1801854f68520fe4164b89a24c53c47e17c7b6c3de4707d48e37a076 son exactos a R8. A/B vinculan esa imagen y registran3.306/3.368; data/interiors_review.json sólo actualiza esas dos evaluaciones, mantiene aprobado:false y no altera rúbrica. Los cuatro archivos de historico/calidad_tanda19_base (JPG,JSON,A,B) coinciden byte a byte con HEAD previo. Los límites de comparación por nuevo protocolo y las cuatro piezas compartidas están declarados; no se recertifican visualmente otros cuartos.

## Alcance real de recibos

Leídos82 contratos PASS;200casas sintéticas/1166habitaciones con cero errores/pendientes;22casas del pueblo/132habitaciones sin errores;81semillas de trofeos y el gate40kits×5. vivienda_salon.json actual contiene cinco semillas, como corresponde al gate general: no demuestra un nuevo barrido81salones. El recibo81 anterior sigue íntegro en evidencia_tanda18/gates_finales/vivienda_salon.json y coincide con su manifiesto histórico.

Integración fuente y paquete conserva ocho entradas, Annie cinco kits más dormitorio personalizado, acciones de tres comercios y fixture/recarga321/700 con testigos Evolución/fija; errores y consola vacíos. El barrido fuente contiene96 recorridos, no se extrapola al paquete ni a todos los muebles. Máximos sintéticos73424triángulos/60mallas/9luces/677ms se presentan como coste de construcción, noFPS.

El gate banco_jugador es una prueba mecánica sobre fuente, con residentes eliminados y reposición a acceso validado. La integración general de paquete no contiene por sí misma esa prueba de asiento. **Suplemento leído después:** banco_paquete.json registra cuatro PASS usando el trofeos_publico.js exacto sobre dist/test.html local, con residentes conservados y consola vacía.2132/4204/1679 pasan selector real, sit, standUp, collider y restauración; las tres salidas toman la rama standPos.2162 mantiene banco0 y mesa amplia (área11.767969, no rama<11). Este suplemento cierra la cobertura mecánica dirigida en paquete local; no prueba Pages/SHA público ni recorrido desde puerta, calidad de animación o la rama de salida frontal.

## Claims y helpers

Los apéndices documentales dicen mejora parcial y publicación pendiente. No afirman4/5,25% ni beta completa. R5/R6/R7 y la errata histórica del workflow se conservan; los informes anteriores con gates pendientes se leen como estados históricos, superados por los recibos finales de esta auditoría.

Publicar_tras_ci mantiene SHA explícito, workflow validar.yml, dos jobs obligatorios exitosos, árbol probado igual al producto, árbol limpio y avance main sin force. Probe privado conserva HQ, vecinos/Annie/comercios/recarga y añade cuatro trofeos/tres bancos mediante métodos reales. El cierre privado conserva identidad workflow CI/Pages, jobs obligatorios, SHA y árboles, veto de sobrescritura y manifiesto previo; copiará ambos instrumentos y declarará su ruta de ejecución. No se han ejecutado aquí. El cierre fue preparado por este mismo revisor: esta lectura es autocontrol de ese helper, no una segunda autoría independiente; raíz lo revisará antes de ejecutarlo.

Raíz incorporará esta auditoría y el suplemento después del manifiesto original150, preservando sus hashes. La integridad de esa ampliación futura debe comprobarse al añadirla; no se da por realizada en este informe.

## Huellas leídas
- `data/interiores/validacion/evidencia_tanda19/manifest.json`: `87d0fcc6a9e4c158277b086965d2df989550f282aa3c0abf7431dbb6c3c0b4d4`.
- `.cache/calidad/tanda19/estado_candidato.json`: `56d72d622301b55094f5af4a575cf71ddeb6ff6820ad7581754b2054fc5d622e`.
- `.cache/calidad/tanda19/validacion_sello_final.json`: `0f110548a88c20a3da432b57df6ac821fad2c89336c80f2bb93c77290f4a355b`.
- `.cache/calidad/tanda19/validacion_ejecuciones.json`: `d1731c766748577a4a737305a1823bbc772c5b782c6ecae3bea38bc9a6ecae10`.
- `.cache/calidad/tanda19/regeneracion.json`: `81ef79dff71ffe6814273d95a0069626160112fbfed8ac7468089a08856bfa1a`.
- `.cache/calidad/tanda19/banco_jugador.json`: `9a3043f41c499b499db1b1af2fa95ee0e55a979e8cbab00692d43aee967867a8`.
- `.cache/calidad/tanda19/banco_paquete.json`: `d24de1d44377e9e13027c1ba35b761fb7dee244ebb381ed83b12e9c132a18255`.
- `.cache/calidad/tanda19/probar_banco_paquete.py`: `0c0048cb757279797e62ddc3e46c2ba4f5d6d022759c302a19054d4fa186f48d`.
- `.cache/calidad/tanda19/publicar_tras_ci.py`: `6cca3dbc27d1192bef2aa634d62653029ed9c38bfd377f2b98fe80f3c1b09a7d`.
- `.cache/calidad/tanda19/revision_publicacion/verificar_publico.py`: `dd4b72a35d37951a8d7a6703e7a5cbf725e99c888c89bf73328c8f160854a7ec`.
- `.cache/calidad/tanda19/revision_publicacion/trofeos_publico.js`: `7225e61b1c30ebf9bac46267a0a78f5047499dfae372bf6d0bb6545232a14dd9`.
- `.cache/calidad/tanda19/revision_publicacion/cerrar_publicacion.py`: `35948242c2c1e28ce6ac285b61d5704d003e4480b99cde413c3966c02fe98dfb`.
