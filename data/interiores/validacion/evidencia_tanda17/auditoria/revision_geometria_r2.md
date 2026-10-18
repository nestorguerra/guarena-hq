# T17 R2 · revisión independiente del orden del estudio

**APROBADO para la siguiente captura privada del greybox.** No se identifica bloqueo para observar las tres muestras y la entrada1594. No se aprueban integración, calidad visual, modelos finales ni publicación. Se conserva R1 como control congelado.

## Sello y cambio comprobados

Se verificaron los **47 hashes R2: cero discrepancias**. Se verificaron también los45 archivos del manifiesto R1: siguen exactos. La adenda visual que motivó la única variante conserva SHA `fe813f3402c909ee6ac11bb0be51883014355b581beca741b8a066bf2fb82848`.

Además de leer el informe del autor, se reconstruyó en memoria el cambio esperado sobre el JSON R1: intercambiar biblioteca/bajo y cambiar sólo sus referencias inmediatas produce **exactamente** el kit R2. La comparación de todos los archivos de ambas candidatas encuentra sólo los dos JSON de estudio y el JS privado regenerado. Catálogo, modelos, motor y demás fuentes permanecen iguales. No se ha aplicado el parche ni reejecutado la batería CPU.

El frente pasa de mesa→biblioteca→bajo a **mesa→bajo→biblioteca**, con silla ligada a mesa y ordenador separado sobre ella. Los frentes de uso, cantidades, perfiles, semillas solicitadas, dimensiones y piezas no cambian. No hay búsqueda nueva ni ajuste por cámara. El grupo existente cambia la pose del frente de3244: la mesa pasa de x1,0254 a x−0,0546. No debe describirse como un simple intercambio de muebles en poses fijas. En1594 y1481 la mesa conserva pose.

## Encaje y conservación según recibos leídos

Los tres marcos originales pasan en el primer intento, con semillas425071/208904/194118. La silla, bajo, biblioteca y ordenador mantienen vínculos coherentes. `huecos.cpu.mjs` contrasta piezas reales con todas las reservas originales; `huecos.json` registra **penetración máxima0** en puertas y ventanas de las tres muestras, incluido el hueco que podía comprometer3244. La planta comparativa confirma que el alto queda al extremo y el bajo entre alto y mesa.

El recibo `full.json` reconstruye22 identidades documentadas y1481 sintética:23 casas,20 controles sin estudio, cero errores. Marcos, luces, otras estancias y botín se conservan según sus aserciones. Sólo3244 y1594 son estudios reales del inventario. Costes de los tres greyboxes:56/58/58 mallas,48.206/58.358/43.216 triángulos y ocho luces; no son costes de modelos finales ni medida FPS.

El rectángulo de escritura sigue libre,0,60×0,30 m. El ordenador conserva definición T16, PICKUP y apoyo independiente; penetración cero frente al puesto. El desplazamiento negativo de4 cm detecta1,75 cm de penetración. Los negativos de recinto bloqueado, apoyo, uso frontal y silla se mantienen; sus fallos esperados no equivalen a aprobar un programa incompleto.

Annie12/13 mantiene, según el instrumento y recibo, cinco estancias, geometrías/poses/materiales representados en CPU, colliders y acciones/posiciones exactos respecto a T16. El opt-in sigue limitado a artista/estudiante/músico. No se acredita render de texturas o interacción animada mediante ese recibo CPU.

## Dictamen para la captura

La variante responde de forma material y acotada a la obstrucción observada en la entrada1594. Merece comprobar si la transición baja permite leer mejor tablero, pantalla y silla, sin añadir masas ni depender de abrir visualmente una biblioteca que aún es una caja. **La mejora sigue sin demostrarse:** el alto conserva tamaño y puede seguir dominando desde ciertos ángulos.

Raíz puede preparar el snapshot fresco T16 con el parche completo indicado y regenerar allí `tools/interiores/datos.py`. No aplicar después el parche incremental contra R1: son alternativas. No ejecutar generadores catálogo/kit sobre la sonda ni copiar el compilado global privado a producto. Esta revisión no ha hecho ninguna de esas operaciones.

La evidencia siguiente debe conservar canónicas completas y diagnóstico de1594 desde el mismo punto/FOV y criterio de mirar su mesa real. Documentar las poses automáticas que deban cambiar; no sustituir una canónica mala por el diagnóstico. Revisar también3244, cuyo frente se ha desplazado, y1481, que sigue siendo sintética. Ningún ajuste de cámara por conveniencia queda aprobado.

## Pendientes fuera de esta prueba

El fallback sólo acredita conservar receta individual/RNG cuando falla el grupo. Su ejemplo mantiene lámparas y carece de mínimos; **no es un caso positivo de programa individual completo**. Antes de producción se necesita comprobar un caso donde el grupo no quepa y la solución individual conserve funciones, paso0,80 y presupuesto, además de la cobertura prevista. No se impone aquí conservar las poses antiguas de T16. No se añade selector o solver a esta sonda.

Continúan pendientes perspectiva, biblioteca y contenidos finales, contraste/materiales, identidad adulta y posible combinación separada con el acabado R2 de raíz. Las plantas y los recibos CPU no resuelven esas preguntas ni conceden calidad4/5.

## Hashes de entrega

- `manifest.json`: `d5d6138512f7943655b7360a9aa308ecb03aaa4674968dbc4bb3725462998504`.
- `entrega.md`: `22f7816bfc3c1a110b7810f5feb2ca95f7099fece0d7434a9a0ef3efeb2c0ba5`.
- `greybox_r2_contra_t16.patch`: `ed0c405f0ca5d22e1960a70f04fbd05a42dde6432938d7927ef3489c7ae59c49`.
- `orden_r2_contra_r1.patch`: `67c8bde0c846da6386ce7943014f568ad19394cfeea0d6097ec17507093a82b9`.

Los hashes restantes y resultados deterministas constan en `revision_geometria_r2.json`. Sin GPU, API, build, producto, commit ni publicación. Sólo se han creado estos dos informes privados.
