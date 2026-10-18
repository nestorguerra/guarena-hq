# T17 · Revisión visual final R2 · regresión detectada

**RECHAZADA esta captura para integración o evaluación formal.** La ficha no representa la intervención limitada a pelusa anunciada: desaparecen los acabados serenos de suelo, paredes y techo del estudio. Es una regresión material clara respecto a final R1; no basta con observar que los puntos blancos se ven menos.

Ficha R2: `601184d0b4e53f4563b269ddd83d9d16eb55af0cdebe3ff7b44fda5c2201ef84`.
Ficha final R1: `7e5f2635ce48ddb7438ccf762952b1126fa926b39d5fe719ee62724e35c21503`.
JSON de R2/R1/greybox R2 idéntico: `a2606f95d3802b56e3a726c19611e5b0bc2779c94f48d5bd261e37120f82f6cd`. Las seis poses, objetivos y FOV coinciden. Se han cotejado los diez hashes de la procedencia; ésta registra 493 fuentes estables, seis guardas libres y alta/DPR1. Eso prueba identidad y trazabilidad de los archivos, no corrección visual.

He abierto la ficha y los seis raw de R2. En 3244 vuelve el jaspeado intenso del suelo, el muro verde moteado y el techo texturado anterior; desaparecen pared de uso verde lisa, paños claros y suelo calmado de R1. En 1594 reaparecen el suelo jaspeado y el azul de fondo anterior donde R1 tenía cal clara. En 1481 desaparece el acento marrón y reaparecen paredes moteadas verdes y jaspeado. Los modelos finales, láminas, cajoneros, biblioteca abierta y cortinas cortas permanecen visibles. El suelo vuelve a competir fuertemente con el puesto. No es un cambio explicado por cámara o encuadre.

El criterio de aceptación era conservar la apariencia de R1 y limpiar únicamente las motas de los paños de estudio, dejando muebles/puertas con su material artesanal. Ese criterio no se cumple. No se atribuye un defecto al diseño de los modelos ni se revoca el diagnóstico válido de pelusa R2 previo.

## Pista técnica comunicada; pendiente de confirmación

El parche privado usa `CLAY_LINT:0` en el material, mientras la expresión GLSL multiplica `cl.z * 0.7 * CLAY_LINT`. Un define numérico 0 puede emitirse como literal entero y causar incompatibilidad float×int en GLSL. La desaparición de los paños nuevos es compatible con un fallo de compilación de ese material. **Es hipótesis de código**, no causa demostrada por esta revisión; comprobar el registro de compilación WebGL y la conversión del define. Una solución posible es literal flotante `'0.0'` o conversión explícita `float(CLAY_LINT)`, a revisar por el responsable técnico. No se ha editado ninguna fuente.

Debe conservarse esta captura fallida como evidencia. Tras resolver la causa, recapturar el resultado real con los mismos encuadres y verificar que los paños lisos y su contraste vuelven, que la pelusa desaparece sólo en ellos y que los materiales ajenos conservan su apariencia. Recuento CPU y aprobación de código corresponden a la revisión técnica separada. No ejecutar evaluación formal sobre esta imagen fallida.

Sin GPU adicional, navegador, API, puntuación, cambios de producto ni afirmaciones de funcionamiento a partir de píxeles.
