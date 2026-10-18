# Evidencia de la tanda 15

Mejora infantil parcial: biblioteca vinculada al estudio, fondo de cama contrastado y zona baja de lectura/juego. Notas A 3,488 y B 3,208; objetivo 4/5 pendiente. Las revisiones independientes describen mejoras y límites; no sustituyen el visto bueno del usuario.

`capturas/` conserva cuatro estados con procedencia original. `reutilizacion_capturas.json` justifica por invariancia de 31 construcciones reutilizar la ficha final tras la reparación lógica del laboratorio: no representa una nueva comparación de píxeles ni una nueva evaluación de API. Los juicios y sus imágenes exactas están en la carpeta de validación y su archivo de imágenes.

`ERRATA_CPU_81.md`, los dos históricos FAIL y el diagnóstico conservan los fallos del instrumento y del producto. El arreglo del laboratorio mantiene marcos, puertas, mínimos y guardas: búsqueda finita sólo en las dos alfombras y reintentos domésticos acotados con semilla efectiva expuesta. `fix_laboratorio/` documenta código y revisión independiente.

`gates_finales/` contiene nueve ejecuciones terminadas con éxito, 66 contratos y 412 entradas de fuente congeladas verificadas antes y después. Cubre 200 casas/1166 habitaciones, 81 laboratorios infantiles, todos los kits en cinco semillas, 96 recorridos de colisión, juego fuente/paquete, recursos y marcas. Las pruebas usan partidas ficticias y Chrome sin sonido. Los tiempos son de montaje local M1, no FPS ni garantía de otros equipos.

CI y publicación se acreditan por separado en `publicacion_tanda15.json` cuando existan; este dossier no las presupone. El manifiesto cubre los archivos presentes, excepto el propio manifiesto.

Precisión de alcance: 31 construcciones por semilla no acreditan 31 casas del inventario público; 1296 es una fixture sintética conocida.
