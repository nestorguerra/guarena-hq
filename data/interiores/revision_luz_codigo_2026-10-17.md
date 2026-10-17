# Revisión independiente de código — tanda 4

Fecha: 2026-10-17. Alcance: `src/luz_vivienda.js`, integración en `Game.renderView()` y contrato añadido en `tools/interiores/casas_pruebas.js`.

## Veredicto

**Sin hallazgos nuevos de código que requieran corrección dentro del alcance revisado.** No se asigna puntuación estética ni aprobación de despliegue. La revisión es de lectura del código; el único archivo escrito por este revisor es este informe.

## Evidencia comprobada

- `src/luz_vivienda.js:6`: solo entra en viviendas `vecino` y `annie`. Los locales, iglesia, edificios singulares y la casa `apagon` quedan fuera.
- `src/luz_vivienda.js:11-12`: no selecciona luces apagadas ni el fuego como principal. Si todas las luces domésticas están apagadas, no altera las intensidades.
- `src/luz_vivienda.js:19-30`: conserva y restaura exactamente intensidad y `castShadow` de todas las luces; no atenúa el fuego. Los parámetros del mapa de sombras son configuración persistente de esas luces, no valores animados.
- `src/game.js:808-815`: la restauración de las lámparas queda en `finally`, también si el render directo o el compositor lanza una excepción.
- `src/luz_vivienda.js:7-9` y `src/interiors.js:859`: el listener se registra una vez por vivienda; la salida elimina el grupo del padre y provoca la liberación de `shadow.map` y `shadow.mapPass` de sus luces.
- `src/windowview.js`: la vista de la calle utiliza `renderer.render()` directamente, antes del ajuste temporal doméstico. No atraviesa `Game.renderView()` con las lámparas atenuadas. La guarda de distancia también deja intacta una cámara exterior lejana que sí llame al método.
- El nuevo contrato comprueba una luz con sombras, atenuación de relleno, restauración y apagón. No acredita por sí solo liberación GPU, otros edificios ni la ruta de excepción.

## Sondeos ejecutados sin navegador ni puertos

Node de la distribución local de Codex, importando el módulo real `src/luz_vivienda.js` y extrayendo el método real `renderView()` de `src/game.js`. Dobles mínimos de luces, cámaras, grupo y renderizadores; no se sustituyó la lógica del módulo. Siete grupos de comprobaciones, cero errores:

1. Restauración exacta de intensidad y `castShadow`; fuego conservado.
2. `sombras=false` no activa sombras; repetir la preparación registra un solo listener.
3. Invocar el evento de eliminación llama una vez a `dispose()` para `map` y `mapPass` de cada luz.
4. Un apagón completo conserva todas las intensidades a cero.
5. Un interior `local` no cambia luces ni registra listener.
6. Una vista lejana de `annie` no altera sus lámparas.
7. Inyectar una excepción en el render directo y en el compositor restaura las lámparas y propaga el error original.

## Declined to judge

- Calidad estética, fidelidad de la iluminación, sombras visibles y transición entre habitaciones: corresponden al otro revisor.
- Liberación efectiva de memoria de GPU: se verificó la ruta y la llamada a `dispose()`, no contadores WebGL ni memoria física.
- Coste de 4–6 ms, FPS o estabilidad temporal: dato aportado por raíz, no repetido aquí.
- Los 24 contratos completos, paquete, marcas y despliegue: no se ejecutaron ni se certifican en esta revisión.
- Restauración de cámaras del compositor cuando este falla: la línea que intercambia/restaura esas cámaras ya existía antes de este cambio. No la presento como regresión introducida por esta tanda.
- Cámaras arbitrarias bajo padres transformados: los usos revisados trabajan con las posiciones mundiales que espera el helper; no se certifica ese contrato para nuevas cámaras ajenas a esas rutas.


## Segunda revisión — mezcla continua y desvanecimiento de sombras

**Sin nuevos hallazgos bloqueantes.** Esta revisión sustituye las conclusiones sobre el algoritmo de selección brusca de la versión anterior. Se ha releído el helper y el contrato 25, sin navegador ni puertos.

El peso `.08 + .92 * exp(-((d-d0)/2.25)^2)` es continuo al cambiar la luz más cercana: `d0` es el mínimo de distancias continuas. La diferencia entre las dos menores distancias también es continua. Cuando cambia el origen de la sombra, esa diferencia llega a cero y la intensidad de la sombra llega a cero mediante `smoothstep`. Esto cubre también un empate triple; no depende de que las intensidades base de los focos sean iguales.

La restauración incluye ahora `shadow.intensity` de **todas** las luces. Se comprobó con un valor inicial no predeterminado de 0,37 para evitar un falso positivo por restaurar siempre 1. `shadow.dispose()` sustituye la liberación manual de los mapas; se verificó que la ruta del evento lo invoca en todas las luces.

Sondeos Node sobre el módulo real y el método real `Game.renderView()`, con dobles de luces y renderizador: cero errores.

- Cruce de la bisectriz con cámaras a ±1 mm, focos de intensidad 10 y 7: diferencia máxima de intensidad `0.0000036345663`; intensidad máxima de sombra `0.000007022962`. En el empate exacto, sombra cero.
- Barrido entre x=-3 y x=3 con pasos de 1 mm: diferencia máxima entre muestras `0.00328279`; sin salto al cambiar el foco principal.
- Empate entre tres focos de intensidades distintas: sombra inferior a `1e-8` a ambos lados y restauración exacta.
- Restauración exacta de intensidad, `castShadow` y `shadow.intensity`, también al lanzar una excepción el render directo o el compositor.
- `sombras=false`, fuego sin atenuación, apagón completo y llamada a `shadow.dispose()` al retirar el grupo.

Límites: continuidad acreditada con el mismo conjunto de focos encendidos y dentro del radio doméstico de 25 m. La guarda exterior sigue siendo un corte deliberado; no se afirma continuidad global al atravesarla. No se repiten ni se certifican GPU, FPS, shader de Three.js, calidad estética, contratos completos ni despliegue. La compatibilidad de `shadow.intensity`/`shadow.dispose()` con r170 procede de la comprobación oficial comunicada por raíz; estos sondeos verifican su uso y restauración, no reimplementan Three.js.

El contrato 25 cubre la regresión numérica de la bisectriz. La restauración específica de `shadow.intensity` todavía queda cubierta por estos sondeos independientes y no por una aserción explícita del contrato persistente; añadirla sería una mejora de cobertura, no un defecto observado en producción.

SHA-256 del helper revisado: `b433e6a03f6f208c2a3bd070c6c188269f1d386991af9ff2f51a418194f30d6f`.
