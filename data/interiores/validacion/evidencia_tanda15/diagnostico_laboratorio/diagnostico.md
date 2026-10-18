# Alfombra obligatoria: diagnóstico independiente del laboratorio

**No publicar todavía.** Reproduje los tres errores con `buildLocal` literal y `revisar` actuales, usando el contexto y perfil del gate. Ni un fallback local aislado ni copiar solamente los 12 reintentos de casas están demostrados como solución completa. Recomiendo combinar una búsqueda determinista optativa tras agotar `suelo_libre` con reintentos domésticos acotados ante mínimos incumplidos, conservando las dimensiones del primer intento y registrando la selección. No se ha implementado esa propuesta ni modificado un gate.

## Reproducción literal

| Seed | Dimensiones originales | Hash de colocación | Error reproducido |
|---|---|---|---|
| 29 | 5,9 × 2,1 × 2,75 m | d8ee0517 | falta alfombra grande obligatoria |
| 51 | 3,5 × 2,1 × 2,75 m | 83fa2dc0 | falta alfombra compacta obligatoria |
| 63 | 3,5 × 3,6 × 2,75 m | ce625c71 | falta alfombra grande obligatoria |

Hashes, dimensiones y lista de errores CPU coinciden exactamente con el informe real de navegador. `repro.cpu.mjs` usa constructor y geometría reales con Canvas doble; el adaptador sólo expone `glassMat`, que ya usa el `buildLocal` real. No sustituye la función de montaje ni el validador. Recibo: `repro_cpu.json`.

El recibo sintético previo de 81 kits ejecutaba una función `furnish` con hasta 12 llamadas a `amueblar`; el gate ejecuta una sola llamada desde `buildLocal`. Además, al no tener W/D fijados en esos contextos sintéticos, los reintentos podían volver a sortear dimensiones. Por ello, el verde de ese ensayo no equivale al gate de laboratorio ni demuestra éxito en la planta original. Sus recibos deben conservarse con ese alcance, sin presentarlos como ejecución literal de los 81 laboratorios.

## Separar falta de búsqueda de falta de espacio en la colocación elegida

`suelo_libre` (locales.js:354–364) prueba 200 posiciones aleatorias. Calcula centros con un margen fijo de .1 m usando la anchura/profundidad sin rotar, aunque después prueba orientación cercana a cuatro ejes. Si el hueco válido está fuera de ese dominio de muestreo, aumentar casualmente el número de tiros no basta.

Instrumenté sólo en memoria la finalización de esa regla. El sondeo recibe el estado exacto anterior a continuar con los demás adornos y llama a **las mismas funciones internas** `dentro`, `libre` y `cierra`; no inserta ninguna pieza. La malla de búsqueda de 2 cm y los ángulos son instrumento diagnóstico, no código de producto.

- Seed 63, intento original: existe posición aceptada para la alfombra grande original, x≈.73, z≈.91, ry=π/2. Por tanto, aquí el fallo inicial no implica falta absoluta de hueco.
- Seeds 29 y 51, intento original: no hallé posición en los cuatro ejes ni en el control adicional cada 5 grados. Esto es ausencia de hallazgo en un conjunto finito, **no una prueba matemática de imposibilidad**.

Recibos: `huecos_cpu.json` y `huecos_angulos_cpu.json`. No se mueve mobiliario ni se reduce una alfombra en esos sondeos.

## Reintentos con dimensiones honestamente fijadas

Conservé el intento inicial literal. En los siguientes usé `(seed + intento*104729) >>> 0`, W/D/H de ese primer resultado y el mismo contexto/perfil/reservas. No aumenté el límite de 12.

- 29 completa los mínimos en intento 1.
- 63 completa los mínimos en intento 2.
- **51 sigue sin compacta en los 12 intentos.**

Recibo: `reintentos_cpu.json`. Ese resultado impide recomendar únicamente el wrapper de reintento como arreglo del gate.

Un sondeo del intento 1 fijo de seed 51 (semilla efectiva 104780, W=3,5/D=2,1) sí encuentra compacta en x=1,060000024, z=.855000012, ry=0; pasa las tres guardas reales. Los intentos 6 y 11 dejan el mismo hueco. El máximo centro x de la búsqueda aleatoria original para esta alfombra es aproximadamente 1,05: la posición hallada está fuera de su dominio con margen .1. No se debilita ninguna guarda para comprobarla; la holgura al borde es aproximadamente .09 m. Recibo: `huecos_reintentos51_cpu.json`.

## Propuesta acotada y condiciones antes de integrar

1. Una opción explícita sólo para estas entradas `suelo_libre`. Después de los 200 intentos normales fallidos, recorrer candidatos deterministas válidos para la orientación de la huella. Conservar exactamente `dentro/libre/cierra`, tamaño, cuota y paso. No consumir RNG adicional al generar la lista. No sustituir una colocación que ya existe. Un conjunto acotado de ejes y candidatos requiere pruebas de los tres fallos, no la promesa de encontrar todo hueco imaginable.
2. Para el laboratorio doméstico, reintentar sólo si faltan mínimos. Conservar el primer resultado íntegro cuando ya es válido; fijar sus W/D/H, puerta/contexto/filtros en los intentos siguientes; mantener un límite explícito. No alterar comercios ni casas canónicas por una nueva política global inadvertida.
3. Conservar la semilla solicitada como identidad y exponer semilla efectiva, número de intento, dimensiones fijadas y agotamiento. Las posiciones, luces, metadatos y estado aleatorio usado para construir deben proceder de la selección real. Si todos los intentos fallan, el validador debe seguir viendo el mínimo ausente.
4. Antes de aceptar: `buildLocal` y `revisar` literales en 29/51/63, determinismo, negativo sin espacio que siga fallando, conservación del intento inicial válido y consumidores no optantes; después los gates mantenidos. Los puntos aceptados por el sondeo aún no son una validación del montaje completo con esta propuesta combinada.

No recomiendo cambiar semillas, ensanchar el laboratorio fallido, bajar cuota/tamaño/paso, modificar luz/timeout ni aprobar el gate por el éxito de otro intento con otra superficie. Tampoco recomiendo añadir un barrido global costoso sin opt-in. El cambio necesario es hacer explícita la política de búsqueda y selección, no ocultar el primer fallo.

## Límites

Sólo tres seeds reproducidas y diagnósticos acotados sobre ellas. No GPU, browser, build, CI, publicación ni edición activa. No se repitieron los barridos 31/81/200. Las posiciones de sondeo demuestran aceptación por las guardas del solver en ese instante; el producto combinado aún requiere implementación y validación completas. Los informes originales permanecen intactos.
