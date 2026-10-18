# Revisión técnica independiente T17 — estudio adulto

Fecha: 18 de octubre de 2026. Base revisada: `4640cfa891989d9e5d7430609f6c0689e033b997`. Estado: **cierre técnico local favorable, sin hallazgos P1/P2 pendientes en el alcance revisado**. No certifica CI, publicación ni objetivo visual 4/5. El dossier público aún debe recibir su sello documental final.

## Identidad del producto revisado

Cotejo independiente de lectura y CPU de procedencia: **36 comprobaciones PASS**, en `.cache/calidad/tanda17/revision_integracion_cpu.json`; reproducción en `revision_integracion_cpu.py`. No ejecuté de nuevo navegador, GPU, build, generadores ni API en este cierre.

- Las **415 entradas** de `estado_candidato.json` coinciden con los archivos activos después de los gates y la regeneración.
- Las siete fuentes de `integracion_R3.json` coinciden con sus hashes anteriores en la base Git y con sus hashes integrados. Coinciden con el preview R3, excepto la sustitución explícita del puerto privado 8926 por el puerto activo 8920 en el capturador.
- Catálogo B, receta B, texturas B y `houses.js` conservan exactamente los bytes de la candidata final R1 sellada. R3 cambia el acabado de estudio, la expresión de shader y las guardas de captura; no introduce otro motor de colocación.
- Los cuatro derivados integrados de catálogo/kit/datos coinciden con el preview R3. El recibo final de regeneración acredita cinco generadores y **22 derivados idénticos**; comprobé sus 22 hashes actuales. Este cotejo no se presenta como una segunda ejecución de los generadores.
- El parche de validación `de5836e82adacf2e689d68d5675b16689ae4737caa5e1bf979e152453a955920`, aplicado a la base en una carpeta temporal privada, reproduce exactamente `casas_pruebas.js` y el workflow activos. Se conservan los contratos anteriores; se añade `mapaPaso`, cuatro callbacks y CI tanda 20. Los tres callbacks del fragmento de estudio R2 y el callback de tela coinciden literalmente con los integrados.

## Criterio técnico y fallos cerrados

El programa optativo de estudio conserva mesa, silla, ordenador independiente y guardado relacionados; la recuperación individual utiliza el motor existente, sin prometer una vuelta íntegra a la receta T16. El caso dirigido de marco 3,2 × 2,8 m y semilla 4 conserva el fallo inicial con `si_no:false` y la recuperación posterior de biblioteca en otra pared. El contrato mantenido exige mínimos, apoyos y acceso conectado con ancho 0,80 m. No presume que la ventana del laboratorio quede libre en proyección donde aquel contexto no reservaba el hueco.

El caller real aplica el acabado después de amueblar y entrega la estancia. El contrato observa planos construidos, orientación respecto a la mesa, área de acento, tres orientaciones claras distintas, techo y material con `CLAY_LINT:0`. Annie conserva su acabado singular.

La cortina corta se limita al estudio de perfiles optantes. El contrato usa triángulos reales capturados antes de mutar la geometría y OBB de piezas con retranqueo de 1 mm; no sustituye esa prueba por la reserva de ventana. La ausencia de ventana en el estudio de 1594 es legítima y no se inventan paños. El negativo alargando la tela reproduce la colisión de 3244. Las muestras de estudio son **3244 y 1594 del inventario, más 1481 sintética**, aunque un título del contrato use la expresión «tres marcos reales» para las construcciones.

R2 de limpieza de paños falló realmente por multiplicar float por la macro entera 0 en GLSL. Se conserva el error. R3 convierte `float(CLAY_LINT)` y mantiene el valor por defecto 1.0; el probe WebGL real de raíz conserva RED→GREEN. Claves de material propias impiden compartir la supresión de pelusa con otras salas. El capturador rechaza errores antes/después del render y programas no ejecutables antes de guardar. La construcción CPU anterior **no se cuenta como compilación de shader**. No se añadió otra prueba de GPU durante los gates.

La separación de material añade un lote en las tres muestras: el recosteo CPU previo pasó de 56/58/58 a 57/59/59, máximo 59 en 23 identidades (22 del inventario y la sintética). No es una medida de FPS ni una garantía universal de costes. El gate final de 200 casas no registró errores de presupuesto.

## Evidencia final releída

Los nueve registros de `validacion_ejecuciones.json` tienen `exit_code:0`; se cotejaron sus salidas y recibos:

| Gate | Resultado observado |
|---|---|
| Contratos del navegador | 73 PASS, 0 fallos; incluye los cuatro nuevos |
| Kits generales | 40 kits × 5 semillas, sin errores |
| Casas completas | 200 construcciones, cobertura 1166/1166, 0 errores |
| Laboratorio estudio | 81 semillas literales, 0 errores |
| Integración fuente | 0 errores y consola vacía; 96 recorridos: **16 + 32 + 16 + 32**; sin túneles ni escapes |
| Build | salida 0 y paquete generado |
| Recursos | 12 JPEG de suelo + iglesia, tres variantes HTML, bytes exactos |
| Marcas | 63 textos, 0 errores |
| Integración paquete | 0 errores y consola vacía, conservación de partida según recibo |

Los 96 recorridos corresponden al recibo de integración **fuente**; no se atribuye esa batería adicional al paquete. Estos son resultados ejecutados por raíz y releídos por esta revisión, no nuevas ejecuciones propias. Los controles CPU anteriores de construcción/acciones registradas tampoco se presentan como acciones de juego ejecutadas en navegador.

## Ficha, evaluación y procedencia

La ficha activa, la del preview R3 y el archivo por contenido coinciden en SHA-256 `cfe597964fc9e1c5626c9886a1521b01780fc4b5f558526003287dc4c7b04fc2`. Las cuatro piezas históricas de ficha/metadata/juicios A y B coinciden byte a byte con la base Git anterior. No se sustituyeron los resultados viejos por los nuevos.

Cotejadas probabilidades, escala y medias de los recibos: **A 3,222 / B 3,208**, frente a 3,086 / 3,066. Ambos declaran `supera_umbral:false`. Son dos juicios del mismo modelo sobre la misma ficha con referencias invertidas; esta revisión técnica no añade una nota ni acredita calidad 4/5. Las seis poses nuevas se comparan con la cadena greybox/final preservada; no se afirma que toda la ficha histórica T16 use esas mismas cámaras.

## Declined to judge — límites explícitos

No se juzga aquí la suficiencia artística para 4/5, el rendimiento/FPS, todas las semillas posibles, la compilación en cada GPU o navegador, CI remoto, despliegue ni funcionamiento público posterior. Tampoco se convierte el dossier todavía sin sello final en una entrega documental ya auditada. No quedan P1/P2 técnicos detectados en el diff integrado revisado; la meta visual permanece abierta.
