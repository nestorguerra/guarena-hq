# T17 · Diagnóstico de motas R2 y alcance de la corrección

**Causa confirmada en esta pareja: la mezcla de pelusa del shader de plastilina produce las motas visibles. Recomiendo preparar la corrección optativa limitada a los acabados nuevos del estudio.** No es una aprobación de implementación todavía ni de publicación.

He abierto ambas imágenes y leído `diagnostico_motas_r2.py`, resultado y procedencia. Los tres hashes del recibo coinciden; registra 493 fuentes estables, cero errores, alta/DPR1, cámara canónica 1481/vista0 y guardas libres. El instrumento hace ambos renders y obtiene sus imágenes de forma síncrona antes de los envíos; comprueba posición, orientación y FOV sin cambios. Sólo sustituye una aparición de `cl.z * 0.7` por `0.0` y fuerza recompilación con un define diagnóstico sin uso semántico. No usa la primera prueba `diagnostico_motas`, fallida por la guarda y conservada como fallo instrumental.

Original: `d7e7a1ce122b51314b6b2014bcf58d37ded7aa7f6ed11069c2868e7265397f88`.
Sin lint: `385cdc882e6ed7a6796f695b24cfff35e5d034f7102afe02843302276ced65eb`.
Resultado: `8a876294c8ed42db13fe848cea0a6c4fb16fb6babbddb779ab45512b8ffdb29d`.

En la segunda imagen desaparecen los puntos claros de la pared marrón y del frente del bajo. Se conservan la lectura del puesto y biblioteca, el relieve general y las sombras visibles. La concordancia entre la intervención concreta, el código de `src/plastilina.js:348` y el efecto observado sustenta la causalidad; no hay evidencia aquí de z-fighting ni motivo para desplazar paredes. Mi hipótesis previa de partículas superpuestas queda sustituida por este diagnóstico de pelusa procedimental del material.

## Alcance recomendado

- Añadir `CLAY_LINT` con valor GLSL por defecto `1.0`, multiplicando únicamente el factor de mezcla de pelusa. Así se conserva por defecto el comportamiento matemático previo; no cambiar CLAY_TONE, relieve, geometría, luces ni cámaras.
- Establecer `CLAY_LINT:0` sólo en el helper de materiales de los acabados nuevos del estudio. Usar claves propias `estudio_…`: el actual `acabado_domestico_…` comparte cal con otras salas y podría reutilizar un material con defines incorrectos según el orden de construcción.
- Mantener muebles, puertas, otros kits y Annie en el valor por defecto. La intervención diagnóstica recompiló 52 materiales y retiró lint globalmente en ese contexto; **la corrección acotada conservará las motas de muebles/puertas y no reproducirá exactamente la segunda foto**. Eso es compatible con preservar su acabado artesanal, pero debe mostrarse el resultado real acotado.
- `src/casa_lotes.js:36` incluye defines en la clave de agrupación. Separar el material de estudio puede añadir un lote respecto a la cal compartida. Comprobar el coste final y controles/Annie sin elevar límites; no inferir mallas iguales porque no cambie la geometría.

La preparación es pequeña y coherente. Antes de cerrar: lectura del parche real, valores por defecto y exclusión efectiva de otros materiales; coste CPU del combinado; compilación/render del caso acotado con los mismos encuadres. No se pide un nuevo motor ni un cambio global de estilo. No afirmo todavía equivalencia rasterizada del valor por defecto ni ausencia de regresiones en todos los materiales.

Revisión de imágenes y fuentes existentes; sin GPU, navegador, API, ejecución de diagnóstico ni cambios de producto.
