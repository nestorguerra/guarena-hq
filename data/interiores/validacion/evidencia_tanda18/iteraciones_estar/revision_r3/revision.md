# Revisión técnica privada R3 — postpaso de lectura

**Favorable para continuar el prototipo privado corregido; no es aprobación de integración final ni de calidad visual.** No se detecta otro P1/P2 geométrico o de atomicidad en el helper revisado. La ruta de laboratorio aún requiere transmitir perfil y declarar su contexto funcional antes de atribuirle cobertura R3.

Fuentes observadas: `postpaso_r3/composicion_lectura_salon.js` SHA `c28598fe5154a4405795977f973e00ae5778cc4a2618c7343eeea7e12f2016c3`; `locales.js` SHA `65448df1c41c24221f6915519d08be14cd336cafdd004e4767d8ec5ac9417e76`. El código permanece privado y se carga en memoria mediante el runtime de construcción. No se ha usado GPU, API, build ni modificado producto.

## Hallazgos y estado

**P2 cerrado — inicio físico ocupado aceptado por proximidad.** La versión R3c comprobaba una celda alcanzable a menos de .15 m del inicio. `mapaPaso` puede buscar otra semilla si el inicio está ocupado. Con la geometría real de 3244 y un inicio dirigido `(3.2903732327744373, .675)`, libre en la base, el helper admitía la esquina aunque la celda final tuviera `free=false` y `reach=false`. No se atribuye este inicio artificial a la entrada real de la vivienda. El helper corregido exige la celda literal dentro de bounds y `free && reach`, y rechaza ese mismo caso. RED conservado en `dirigida.json`; comparación literal RED→GREEN en `cierre_inicio.json`. El callback de aceptación es neutral en este test de la guarda, no se presenta como un build completo.

**Cobertura pendiente — laboratorio sin perfil.** `buildLocal` vigente transmite el filtro del hogar, pero no `hogar.perfil` a `ctx`. El helper exige `ctx.perfil`: pasar sólo `funciones:true` no lo activa. La adaptación privada de `houses` sí transmite el perfil. Raíz confirma que completará la transmisión del mismo hogar al laboratorio sin volver a ejecutar filtros. Hasta entonces un pase legacy de 81 semillas no acredita este postpaso. Exigir admisiones no vacías y metadata verificable en el recibo que lo pruebe.

## Comprobaciones independientes ejecutadas

`atomicidad_rng_giro.mjs/json` conserva tres controles acotados:

- `amueblar` real del salón 3244, semilla efectiva 424969 y contexto fijo: admisión no vacía, K conserva identidad, índices/obj/e/sop/sup/de idénticos, activas y guardias iguales, y **12 extracciones siguientes U exactamente iguales**. El filtro de este control usa las entradas activas del montaje base; no simula un nuevo consumo del pool doméstico.
- Callback `aceptar` literal extraído de la adaptación privada: `cierra` observa P temporal y lanza una excepción dirigida. El `finally` restaura P, sus referencias originales y guardias. El helper tampoco muta P si su callback lanza. No se ha convertido esa excepción en un PASS de montaje.
- Fixture dirigida de 9 × 9 m con los cuatro objetos reales y un libro dependiente: se rechazan las esquinas sin giro para forzar una admisión en pared E. Giro real de 90°, coordenadas locales del libro invariantes dentro de `1e-10`, `sop/sup` conservados y P original intacto. Es un control de transformación, no otra casa ni cobertura adicional de semillas.

Releído el recibo de raíz de 22 casas: dos admisiones, 3244 y 1594; veinte fallbacks, incluido 5045. No se mantiene la expectativa previa de tres admisiones. Las comprobaciones del autor conservan identidad, núcleo, otras estancias y tipos/labels/defs de acciones, con uso sin errores; no las presento como nuevas ejecuciones propias.

## Geometría e identidades

La clausura por índices y el cambio rígido de x/z/ry conservan alturas y relaciones de los soportes. Se recalculan volúmenes. Las colisiones contra otros propietarios y piezas inmóviles, límites/altura y reservas sí se comprueban. Excluir colisiones entre piezas del **mismo propietario** es admisible aquí porque todas reciben exactamente la misma transformación rígida: conserva contactos/penetraciones que ya existían, **no demuestra que la geometría inicial estuviera libre de ellos**. No extender la excepción a piezas de propietarios distintos.

La guarda de apoyo comprueba altura y centro del objeto en la superficie; no demuestra cobertura completa de una huella arbitraria. Para estos dependientes, el argumento principal es la conservación exacta de soporte y transformación relativa. No usarla como validador general de objetos reanclados a otro soporte.

K y entradas permanecen intactos; no se llama de nuevo a filtros ni r/U. El asiento añadido sólo se registra por el índice comprometido y `!o.rol`, evitando duplicar un sillón ya registrado por su rol. Este asiento de puff es una adición funcional autorizada, no mera conservación. Debe quedar comprobado en `pieces.seat` del constructor final. La instrumentación `__lecturaDebug` y detalle de intentos pertenece a este prototipo; no es parte necesaria del algoritmo de producto.

## Contratos mantenidos recomendados

1. **Admisión y conservación en constructor real.** 3244/1594 deben aplicar, conservar núcleo e inventario/acciones por identidad y añadir exactamente un asiento con pose válida. 4007/4685 deben conservar fallback íntegro y `phone/drawer`; un control no optante permanece idéntico. Verificar puntos de uso y la entrada con el collider real además del mapa .80. No exigir a 5045 aplicar si los límites físicos lo impiden.
2. **Transacción y transformación del helper.** Positivo de giro90° con dependiente, igualdad de siguiente U y salida al rechazar, negativo de inicio ocupado aquí reproducido, y excepción de aceptación con restauración de P/guardias. Incluir reserva o colisión real contra otro propietario para evitar un test que sólo valide el propio mapa de metadatos.

Los contratos deben usar el contexto real del gate y no atribuirle ejecución si el flag/perfil desactiva el pase. La selección de esquina y la visibilidad de galería quedan para revisión de imágenes; el resultado CPU no certifica composición visual ni coste final de render.
