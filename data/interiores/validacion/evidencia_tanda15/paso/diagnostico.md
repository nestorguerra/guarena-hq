# Paso infantil B v3: diagnóstico y delta privado T17

**En 4007 y 5045 no se demuestra un bloqueo del paso.** Existe un corredor continuo de 0,8 m desde la entrada hasta el frente de la silla. El FAIL T17 conserva correctamente su comprobación original, pero ésta exige vacío todo el fondo de 1,2904 m hasta la pared, no sólo una sección de paso de 0,8 m. El nuevo banco ocupa el extremo sobrante. No se mueve ni se elimina el banco para obtener este resultado.

El informe de navegador fallido y las 412 fuentes congeladas se conservan por raíz. Este diagnóstico no los transforma en PASS. Las revisiones CPU anteriores de los nuevos callbacks y `revisarUso` no habían ejecutado T17 contra B v3 y no sustituían ese gate completo.

## Medición independiente

Dos constructores reales, Three r170, colliders reales y geometría de mobiliario; Canvas doble sin GPU. Fuentes efectivamente usadas cotejadas con `estado_candidato.json` en `fuentes.json`. La base privada de houses sin contraste no se ejecuta: el runtime lee el caller/acabado activos congelados. Los demás módulos relevantes usados desde la copia privada coinciden con sus fuentes congeladas.

Ambas casas dan:

- Frente de silla: z = 1,290400015 m.
- Frente del banco: z = 0,459999993 m.
- Hueco conservador entre ambos: **0,830400022 m**.
- Centros admisibles para radio 0,34: z ∈ [0,799999993; 0,950400015].
- Centros admisibles para radio 0,40: z ∈ [0,859999993; 0,890400015].

El rectángulo original cubre z = [0; 1,2904] y sólo intersecta el banco. El cuadrado de .8×.8 inmediatamente ante la silla cubre aproximadamente z = [.4904; 1.2904]; está libre de todas las piezas comprobadas por el guard anterior. Se conserva también `d >= .8`.

`diagnostico.cpu.mjs` calcula rutas en una rejilla de 2 cm, pero **no infiere continuidad sólo de muestras**: comprueba la distancia mínima de cada segmento de ruta completo a los segmentos reales Float32 del collider, círculos y OBB conservadoras del mobiliario. Rechaza puntos interiores de OBB. Además ejecuta `resolveCircle` real en cada nodo y comprueba profundidad y desplazamiento cero.

| Casa | Radio de paso | Distancia continua mínima | Collider: profundidad/desplazamiento |
|---|---:|---:|---:|
| 4007 | .34 | .340121566 m | 0 / 0 |
| 4007 | .40 | .400100514 m | 0 / 0 |
| 5045 | .34 | .340000007 m | 0 / 0 |
| 5045 | .40 | .400000007 m | 0 / 0 |

La conexión recta adicional desde fuera del umbral hasta `e.inicio` admite radio .40: distancia mínima .449844460 m y .449800701 m respectivamente; profundidad/desplazamiento cero en la comprobación del collider. No se desplaza la entrada. Los destinos reales de lectura y ocultación están conectados desde `e.inicio` con radio .34; rutas y coordenadas completas quedan en `report.json`. No se afirma radio .40 en esos dos destinos exactos de interacción, sólo en el corredor y umbral.

## Delta privado solicitado

`paso_t17.patch` modifica sólo el bloque de sección estrecha de T17 en `tools/interiores/casas_pruebas.js`. Conserva el umbral .8, el resto de geometría del contrato, `revisarUso`, la ocultación/salida y los contratos de pintura/B v3. Sustituye el rectángulo hasta la pared por el cuadrado .8×.8 ante la silla. No cambia producto, poses ni colliders.

Añade una comprobación del hueco geométrico del banco y un negativo: una **copia local** del banco se adelanta 4 cm hacia la silla. Queda un hueco de **0,790400022 m** y penetra en el cuadrado de paso. Debe dar FAIL. El objeto colocado original no se modifica; las piezas del clon se calculan desde su posición real, no desde una envolvente `v` obsoleta.

`contrato.cpu.mjs` ejecuta el bloque exacto extraído del candidato en las dos casas: T17 original RED esperado; bloque candidato PASS; banco adelantado RED esperado. Comprueba conservación íntegra de los datos de colocación después de cada ejecución. `contrato_cpu.json` conserva los recibos. Sintaxis y `git apply --check`: PASS. No se ha aplicado el parche.

## Límites y decisión

El delta está justificado para estas dos pruebas dirigidas sin reducir el requisito de anchura de .8 m. No demuestra cobertura universal de todas las habitaciones o semillas. El recorrido CPU no representa una sesión de movimiento de jugador ni colisiones con hojas animadas; no hay GPU ni juicio visual. El contrato completo y el navegador deben ejecutarse después de integrar el delta. No he cambiado los gates activos ni el FAIL histórico.
