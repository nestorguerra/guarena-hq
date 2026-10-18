# Contratos privados T21 para R8

Preparados para revisión e integración por raíz. No se han modificado activos, el snapshot R8, workflow, límites ni producto. Base del parche: `base.js`, copia del runner activo R6. Gate acumulativo 21 intacto. El parche añade un caso y conserva los demás salvo los dos ajustes explícitos descritos abajo.

- Constructor: el conjunto de índices movidos es la unión de `composicionLectura.movidos` y `composicionEstar.movidos`. Conserva identidades, referencias, acciones/recompensas, otras salas, phone/drawer, asientos existentes, funciones y presupuesto; compara literalmente las poses fuera de esa unión. El caso sin ninguno de los programas conserva el fallback íntegro.
- Estar aislado: `amueblar` legacy → helper real de lectura → helper real de estar, con callback `revisar` real. Exige admisión y movimiento efectivo en 3244/1594 y fallback en 2786. Compara el resultado con `amueblar` integrado, preserva identidades y apoyos relativos, protege selección de asientos con mapa físico y alcance estricto 1,25 m, incluido el puff registrado por lectura. Comprueba reserva total, inicio exterior, rechazo funcional y excepción sin mutación del P recibido. K se restaura y las geometrías se liberan en finally.
- Alfombra: sólo cambian expectativas explícitas de color al diseño R8, centro `#c8bda5` y borde `#687565`. Se mantienen raycasts sobre triángulos reales después de agrupar, muestras transformadas por origen/rotación, altura .012/.011, forma y visibilidad sobre suelo. 2786 conserva ausencia legítima de sofá/alfombra.

## Evidencia ejecutada

`cpu.json`: dos callbacks nuevos/adaptados literales PASS sobre final_r8 sellado; configuración restaurada. `alfombra_cpu.json`: callback literal PASS; quitar subida de cota falla por alfombra oculta y borrar color falla por pérdida de color propio. `negativo_sin_movimiento.json` y `negativo_ignora_rechazo.json`: FAIL esperado por prueba vacía y rechazo ignorado respectivamente, con configuración restaurada. No se cambió el callback para aceptar estos mutantes.

El primer ensayo privado tenía un error del harness (no exportaba `componerLectura`); se conserva en `cpu_error_harness_v1.json`. No se considera fallo del producto ni ejecución válida del segundo callback.

## Límites

CPU con Three r170, geometrías y constructores reales; Canvas de trazas y texturas placeholder. No equivale a navegador, raster, FPS ni gate final de mallas. Las aserciones de coste del callback se mantienen para el navegador; no se certifica presupuesto final con dobles CPU.

Las 12 extracciones U, activas y guardias comparan los dos programas juntos apagados/encendidos. No se atribuyen a aislamiento exclusivo de estar. El rechazo/excepción del helper demuestra P de entrada intacto; no demuestra por sí solo restauración del cierre privado `cierra`. Las pruebas dirigidas anteriores de ese cierre y los negativos de política de puff/rango se conservan en `estar_r7_revision/asientos_fix`; no se presentan como nuevos casos mantenidos. No se demuestra salida `standUp` con la distancia radial de selección.

No se ejecutaron aquí los restantes callbacks, 81 laboratorios, 200 casas, GPU ni API. No constituye aprobación visual ni publicación. Los hashes de lo entregado están en manifest.json.
