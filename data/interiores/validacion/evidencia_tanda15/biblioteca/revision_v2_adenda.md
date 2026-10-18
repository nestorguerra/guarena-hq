# Adenda B v2 — P2 cerrado

**Sin P1/P2 pendientes en el alcance estático revisado.** Combinado `cae307dfc79c6de166c9b729a117acaacb7c77052f638420dd150102bd608504`; contrato `918fe8a4761d3dbae715bda780dad1290a958dea5773c0609eda9b6be0c12539`. Esta adenda sustituye el estado abierto de revision_codigo.md, conservado como evidencia. Aceptación acotada para integración y validación posterior; no aprobación visual ni ejecución en navegador.

Delta: sólo tres valores del JSON de vb_hacer_biblioteca (ancho inferior .26→.19; centros x de dos cuadernos .13→.165), con sus líneas del generador. Los bordes izquierdos .070/.075 quedan separados del extremo .0575 de la caja. El cuaderno superior apoya entero sobre el inferior; recipiente y pieza superior conservan apoyo completo. Caja izquierda/cuaderno asociado, envolvente, materiales y número de piezas permanecen. Motor, receta y los otros dos callbacks mantenidos no cambian.

Evidencia propia revision_solape_v2.cpu.mjs/json: caja real idéntica en los nueve campos; partes/penetra detectan exactamente dos pares en B v1 (.025/.0175m), cero en B v2. El nuevo callback mantenido exacto pasa con v2 y falla con v1 conservada por subpiezas interpenetradas. Sus cuatro negativos pasan y los datos se restauran exactamente. El negativo nuevo reintroduce el solape original y exige que el viejo control sólo de apoyo siga pasando. No se ha usado navegador, GPU, build, CI ni editado producto.

## Discrepancia del diagnóstico de 1296

Se leyeron el recibo normal conservado, traza con operandos, script de traza y control sin JIT. Comparación profunda normal/control: sólo cambian dos hojas que duplican el mismo campo de 1296 (rows y canonical); ground/poses permanecen idénticos. El script de traza añade observación, sin cambiar geometría ni constantes. Eso no demuestra por sí solo una causa de JIT.

Se recalcularon **224 campos por recibo** con Python independiente desde las poses/volúmenes guardados: normal tiene una discrepancia; v1 y control sin JIT tienen cero. Para 1296, bedNorth=1.8305000162124634 y wardSouth=2.594894859119875; su diferencia es 0.7643948429074114. El −1.8205000162124634 guardado en la ejecución normal no corresponde a esos operandos. Recibo propio revision_metrica_python.json.

Hay una inconsistencia real del diagnóstico normal, con causa no establecida. **No se usa ese escalar para acreditar separación, mejora visual ni corrección del producto.** No hay evidencia en estos recibos de movimiento de muebles o cambio de fixture. El delta sellado afecta dos cuadernos internos y conserva envolvente, motor y receta. La comprobación geométrica del arreglo es independiente de ese campo. Acceso/reserva/ocultación usan otras mediciones; no se sustituye su criterio por el escalar. El recibo anómalo se conserva, y el final se identifica como ejecución sin JIT. No se certifica el evaluador normal completo ni se afirma un fallo de V8 sin reproducción causal.

Permanecen los límites anteriores: importación/ejecución real de contratos en navegador, calidad visual, cámaras libres y salida bajo el bucle completo requieren validación posterior. No se ha repetido aquí el barrido 31+81 ni las seis casas completas: se revisaron sus recibos; la ejecución propia se acotó al modelo/callback alterado y al recálculo diagnóstico independiente.
