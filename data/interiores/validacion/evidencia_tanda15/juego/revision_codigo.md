# Revisión independiente B v3 — banco y huella de juego

**Sin P1/P2 pendientes en motor/modelos/receta corregidos.** Aceptación técnica acotada para integración local y capturas. Los contratos mantenidos del autor siguen pendientes de entrega/revisión en este punto; no es aprobación visual, de navegador, CI o publicación.

Motor: `a88e141f77e12dfae700ece9242ccfdd1fc7fe7c2fb0e1c8f6fa7845116e359e`.
Modelos/receta finales: `ac0b1d112a806f97cafc0ebec59de49c4903bc2fa72653059e0c9bbcfeadd5d9`.
No se revisan los acabados privados como propuesta B v3: el contraste pertenece a una tanda distinta.

## Hallazgo cerrado

P2 en `tools/interiores/kits_vivienda_b.py`, entrada de alfombra compacta: la primera versión usaba `area_max=12-1e-6`. `locales.js:522` ya excluye el límite superior (`W*D>=area_max`), por lo que el intervalo [11.999999,12) quedaba sin ninguna receta de alfombra activa. No era necesario añadir epsilon para evitar dos alfombras. Avisé a raíz y autor; la versión original `c8325802…` se conserva como histórica.

Reproducción independiente con `amueblar` real y kit mínimo: a 11.999999 y 11.9999995 m², versión original produce cero alfombras. Con `area_max=12`, se produce una compacta; a 12 y 12.000001 m², una grande. La corrección cierra el hueco sin solapamiento de filtros.

## Motor y geometría

El separador sustituye la holgura anterior .01; no se suma a ella. Sólo se aplica en la regla individual `contra_pared`, a la que delega `enfrente`. La guarda inicial rechaza reglas ajenas o entradas agrupadas. Los límites numéricos 0–.5 corresponden al schema; no se introduce una nueva semántica en los grupos.

Mi prueba dirigida comprueba .14 m exactos en N/S/E/W, con la envolvente rotada correctamente. Los cuatro controles sin propiedad coinciden por completo con el motor previo, incluido estado RNG. Tres semillas de la receta B v2 completa también mantienen el resultado serializable y la siguiente extracción aleatoria. La lectura del diff confirma que el resto de operaciones conserva su orden. El autor aporta además 81 semillas no optantes con igualdad de P; ese control concreto no compara directamente la siguiente extracción RNG.

Enfrente conserva la pared opuesta de la biblioteca. Si la bloqueamos, `si_no:false` omite el banco; un control con fallback habilitado sí puede encontrar otra pared. No se fuerza un banco en una posición ajena para cumplir cuota. Su reserva frontal .7×.55 sigue pasando por las guardas existentes de uso y espacio.

El banco mide .9×.4×.32 m, tiene ocho piezas, asiento a .4 m y rol `sillon`. Bases, costados, división y asiento contactan; las cajas apoyan en la base y quedan dentro de las dos cavidades. Mi comprobación de piezas no encuentra penetraciones internas ni componentes elevados sin apoyo. El autor incluye negativos de asiento elevado y caja atravesando la división. La alfombra compacta conserva las dos piezas y textura originales, con huella 1.2×.85 m; no se añaden superficies para acumular decoración.

La cortina real baja a .175 m y ondula ±.035 m respecto a su centro. Las reservas de ventana empiezan a .92 m y, por sí solas, no protegerían el banco bajo. El separador está justificado por esa diferencia geométrica. El ensayo del autor usa envolventes conservadoras de las cortinas y conserva un RED del prototipo sin separador; no se presenta como fallo de una versión publicada.

## Evidencia y alcance real

Propia: `revision_dirigida.cpu.mjs/json`, PASS sin GPU. Incluye las cuatro paredes, defaults, tres casos completos sin opt-in, relación opuesta/fallback, reglas rechazadas, frontera RED/GREEN y piezas del banco. No repetí los barridos del autor.

Leídos: `cpu_layout.json`, `cpu_detalles.json`, `cpu_full.json` y sus instrumentos. Layout: 31 estancias reales y 81 kits, cero errores; las seis piezas principales conservan sus posiciones en las 31 estancias reales. Hay alfombra en 112/112 casos; banco en 24/31 reales y 59/81 sintéticos. El banco sigue siendo opcional. La receta modifica el consumo incidental de RNG; no afirmo identidad de toda la decoración o poses de luminarias.

Constructor y agrupación reales: 31 casas, máximo **60 mallas, 63.264 triángulos y 8 luces**. Las 24 con banco tienen el asiento registrado en `pieces.seat` y frente libre con radio .34; el ciclo de ocultación/salida y uso completo pasan en las 31. Las otras estancias coinciden según el recibo. No se incrementa el número de luces en ese conjunto.

El ensayo completo compara B v2 y B v3 con **el mismo** acabado y caller contemporáneos de raíz, leídos una sola vez en memoria y cotejados al terminar: acabado `5c65b324b83ffed145793b01bb5635b85b31f6b71c232f32879f42f48adc71e9`, houses `20336003f922f667b29e2b7eb349fe720bd2d9dcb3aa6e5bdfe23043a3491706`. Estos archivos no se incluyen en el parche B v3. La prueba de layout usa su base B v2 sin ese contraste; los alcances están separados en los recibos.

## Declined to judge

- Apariencia, confort visual del asiento/animación de residentes, calidad de texturas y mejora de puntuación. Canvas es doble; no hay render de GPU en esta revisión.
- Presupuesto universal: 60 mallas es el máximo observado, no una garantía para todas las semillas posibles.
- Animación de sentarse en navegador. El recibo prueba registro del asiento y acceso físico; no ejecuta un residente sentado con raster real.
- Integración final con cambios concurrentes, compilación, CI, publicación y contratos mantenidos todavía no entregados.

No se modificaron producto, cámara, luces, archivos activos ni evidencias anteriores por este revisor.

## Adenda: cierre de los dos contratos mantenidos tanda 18

Revisado `contratos.patch`, SHA `0d67f92a95bcee0d841dca4adf5f2f9b000c7701474924da8651919d2f3bc45d`: **sin P1/P2**. Queda cerrada la revisión pendiente de contratos indicada arriba. El delta sólo añade dos callbacks tras el contrato de pintura; no lo sustituye ni altera los contratos previos. `git apply --check` sobre la activa con pintura ya incorporada pasa.

Cotejé el texto añadido byte a byte con `contratos.inc`, SHA `b650c9fa477f5257829c097f009e3037f099fefea4ee16f4a92042fd679e1333`, que ejecuta el recibo del autor `cpu_contratos.json` (`cf66b3f09ad2e3652de34cf0b4ec9aa6062e23a3c242dc6c9ad3fbf70fdedbd3`). Son los callbacks mantenidos exactos, no pruebas equivalentes reescritas. El primer caso visita nueve casas, incluidas las cinco que chocaban con cortinas en el prototipo sin separador. Exige banco en las tres canónicas, alfombra y contenido de biblioteca, registro de asiento, frente libre, relación con libros, ausencia de corte de cortinas, acceso funcional y coste <=60. La optionalidad en las otras casas es intencionada; no permite que desaparezcan todos los bancos para eludir las comprobaciones.

El segundo comprueba los apoyos y dos mutaciones físicas, la frontera del área, cuatro orientaciones con distancias ausente/0/.14, y rechazo fuera de las reglas admitidas. Sus mutaciones de partes se leen directamente en `partes`, sin quedar anuladas por el caché de `caja`; se restauran en `finally`, al igual que el kit temporal.

Prueba propia acotada `revision_contratos.cpu.mjs/json`: segundo callback completo PASS y catálogo/kit restaurados; mutante del límite superior antiguo produce RED en la frontera. Primer callback con exceso de mallas produce RED por presupuesto; sin banco canónico produce RED por admisión. Cada negativo del primer caso construye sólo la primera casa; no repetí su barrido de nueve. La evidencia conserva esos resultados como negativos esperados, no como éxitos del modelo mutado.

Precisión posterior sobre `detalles.cpu.mjs`: el autor añadió ahora la comparación explícita de la siguiente extracción `U` en las 81 semillas, además de P. Mi observación previa correspondía al texto anterior; el recibo JSON mantiene el mismo hash porque su resumen de checks no cambia.

Límites que permanecen: CPU con Canvas doble; el registro de asiento no demuestra una animación sentada correcta. La prueba de cortinas reconstruye su envolvente desde reservas y dimensiones actuales, no evalúa píxeles. Navegador, presupuesto de toda la población, calidad visual, pipeline y publicación siguen a cargo de la integración posterior. No hay dependencia de `.cache` introducida en los tests mantenidos.
