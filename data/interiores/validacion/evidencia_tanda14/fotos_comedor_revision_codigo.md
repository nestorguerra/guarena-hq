# Revisión del capturador de comedor

Revisión estática del diff de `tools/interiores/fotos_casa.py`, SHA256 `134d613de0f59ca50f7ff6b67ffae326f28a5d596bbd02441b5cbb0428abc0b3`. Sin modificar producto/instrumento activo ni ejecutar navegador/GPU.

**El criterio es uniforme y no selecciona semillas por resultado visual. Dos rutas de falso verde deben cerrarse antes de interpretar la cobertura como garantía.**

- **P2 — recorte aceptado sin aviso**, líneas 82 y 95–100: las esquinas fuera de frustum/margen sólo restan 100 a la puntuación. Si todas las cámaras válidas recortan la mesa/sillas, `mejor` sigue finito y se guarda una ficha normal. El JSON permite detectar el recorte a posteriori, pero no falla ni avisa; el contador tampoco se imprime en la ficha. Reproducción CPU del criterio: dos candidatos con 3/2 esquinas recortadas dan ganador finito con 2 recortes. Para garantizar la primera vista completa, exigir cero recortes en comedor/k0 o declarar explícitamente captura incompleta en salida y bloquear su aceptación. No cambiar FOV ni eliminar muebles para lograrlo.
- **P2 — cobertura de una pose anterior a la captura**, líneas 59–81 y 98–101: se mide la puerta y después se ejecutan tres `g.frame(1/30)`. `src/game.js:693` llama a `interiors.update`; `src/interiors.js:913–920` puede girar puertas hacia su target. Desactivar HouseLife no desactiva ese movimiento. La captura y el JSON pueden discrepar. Ensayo CPU con cámara/raycast reales de Three r170 y hoja de dimensiones reales: pose 1,20→1,42 rad cambia de 4/35 (11,43%, aceptada) a 5/35 (14,29%, rechazada), con cámara/objetivo constantes. No es una reproducción en las tres casas canónicas. Corrección mínima: recalcular cobertura en la cámara final después de los frames y `updateMatrixWorld`, justo antes de render/captura, registrar ese valor y fallar si supera el límite. Esto conserva el estado real de la puerta.

## Correcto y límites de interpretación

El encuadre transforma las ocho esquinas AABB del catálogo con posición/rotación reales y origen de estancia; incluye sillas vinculadas por `de`. El FOV/aspecto de cámara de prueba coincide con la final. El filtro nuevo sólo se aplica al comedor; la lógica efectiva de cocina/baño/otras tipologías no cambia. Semillas, calidad, DPR, actor/estado y flujo previo se conservan; no se introduce ocultación de puertas ni apertura artificial.

La fracción es **35 rayos muestreados**, no un porcentaje exacto de píxeles tapados. El umbral permite 4 rayos y rechaza 5; sólo estudia hojas a 1,25 m y una malla interior NDC, no todos los oclusores ni los bordes de pantalla. Es razonable como rechazo de primer plano, pero no certifica visibilidad completa del conjunto. En la segunda vista no hay objetivos: `esquinas_recortadas:0` significa conjunto vacío, no toda la habitación dentro del encuadre; conviene añadir número de esquinas/objetivos evaluados o usar null en ese caso.

Las cámaras nuevas no son idénticas a las fichas históricas: para comparación causal antes/después, reutilizar cámara declarada o recapturar ambos con el mismo instrumento. Puede usarse esta ficha como nueva evidencia descriptiva sin atribuir toda mejora al producto.

Evidencia propia: `fotos_comedor_revision_cpu.mjs/json`; AST Python correcto. Declined to judge: capturas nuevas aún no vistas, calidad estética/nota formal, oclusión real de las tres casas, mejora de producto, GPU y publicación. No se afirma que los dos defectos se hayan materializado en la última ficha.


## Adenda de subsanación: cobertura final estricta

Releído `tools/interiores/fotos_casa.py` SHA256 `46f06530176d1a5bacdc765ecc81c8aae511f6cdee2a61f97ce0000ab18dfd72`. **Los dos P2 anteriores quedan cerrados estáticamente.** Tras los tres frames, se aplica la cámara final, se actualizan las matrices de la casa, se recalculan los 35 rayos y las esquinas proyectadas, y se lanza error antes de render/captura si la fracción supera 0,12 o existe un recorte. No hay await entre esa validación y render/toDataURL. El registro almacena los resultados finales; k1 declara cero esquinas evaluadas y recortes null, corrigiendo la ambigüedad.

Cambio de protocolo explícito: comedor pasa de FOV68 a75 y objetivos verticales de1,05/1,40 a0,75/1,05m; ojos siguen1,60m. Este cambio afecta sólo al comedor. Semillas, calidad y DPR no cambian. No cabe usar las fichas históricas68 como comparación de cámara idéntica; la nueva ficha es evidencia con protocolo distinto. La justificación declarada es cubrir mesa y sillas sin quitar elementos; valorar su lectura visual corresponde a la captura posterior. No se certifica aquí equivalencia del FOV con todas las modalidades de cámara del juego.

No se detecta un nuevo bloqueo estático. La primera vista valida todas las esquinas de los objetivos existentes; si faltara la mesa por un fallo de producto, la lista quedaría vacía. Esa ausencia la cubren los contratos de producto, no esta guarda geométrica; sería útil exigir mesa/objetivos no vacíos antes de llamar completa a esa vista. La fracción sigue siendo muestreo de hojas cercanas, no visibilidad integral de muebles.

Verificación propia: parseo AST Python y sintaxis del JavaScript interpolado sin ejecución de juego. La prueba runtime estricta que falló2606 y la corrida cobertura3 son evidencia de raíz, no una prueba ejecutada por este revisor. GPU/capturas nuevas siguen fuera de esta revisión.


## Adenda: centro vertical de conjunto y rejilla ampliada

Releído capturador SHA256 `6df65f3e1b9c384d44a28568b51bde2d9fb0a2a722464af92dda10324574d937`. Sin nuevo bloqueo estático: el objetivo vertical de k0 comedor es el centro entre las cotas extremas reales de mesa/sillas; ojos1,6m, FOV75, margen0,94 y validación final permanecen. La rejilla más densa sólo afecta al comedor y conserva resolución de colisión y separación. Ausencia de mesa ahora falla expresamente. No hay excepción por semilla ni ocultación de mobiliario. El objetivo y cámara final se registran, manteniendo trazabilidad del nuevo protocolo. No se atribuye a producto una mejora causada por este encuadre.
