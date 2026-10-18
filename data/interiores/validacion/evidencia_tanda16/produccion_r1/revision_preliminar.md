# T16 cocina — revisión preliminar de candidata no sellada

**No hay aprobación final. P2 demostrado en la confianza del validador; remitido al autor y raíz.** Lectura del pase final, esquema/generadores, consumidores y dos comprobaciones CPU dirigidas. Fuentes privadas todavía en evolución; sin GPU, build, API o cambios activos.

## P2 — ocultar una entrada obligatoria mediante `activas` evita el mínimo

`candidata/tools/interiores/validar.js`, bucle de recuento: la receta efectiva conserva cantidad/obligatorio frente a la global, pero `if (L.activas && !L.activas.includes(ei)) continue` permite omitir el mínimo por otro canal.

Ese `if` ya existía: es una debilidad heredada que afecta a la confianza del nuevo programa y su fase/receta efectiva. **No se describe como una regresión publicada en T15.** El cierre pedido se limita a composición de cocina T16; no exige refactorizar los filtros de tiendas.

Reproducción independiente sobre cocina 2786: retirar `va_nevera` (entrada 4), reindexando referencias restantes, produce el error obligatorio esperado. Retirar además el 4 de `L.activas` deja **errores=[]**. No se cambia ni la cuota global ni la efectiva. El control que baja explícitamente `cantidad/obligatorio` efectivos sí es rechazado. Evidencia: `revision_gate.cpu.mjs` y `revision_gate_cpu.json` (`P2_MASK_PASSES`).

Corrección requerida: conservar la receta global como suelo del contrato y verificar elegibilidad/fases/activas contra contexto real; limitar los metadatos efectivos a las identidades/referencias que cambian. Mantener los filtros legítimos. Este negativo representa un defecto del gate, no una nevera realmente desaparecida en las canónicas de la candidata.

La comprobación debe conservar hogar y área. La actividad de pan sólo es exigible si se comprometió el programa; el fallback exacto no debe adquirir ese mínimo diferido. El negativo de nevera corresponde a una entrada global elegible, no a una entrada excluida legítimamente por perfil, estilo o superficie.

## Botín y funciones frente a decoración

Lectura de `cpu.json` y catálogos: las 18 composiciones retiran 462 subobjetos clase PICKUP, 18 altos CARRY sin rol y 18 alacenas con rol armario que se sustituyen. Las tres canónicas retiran respectivamente 24/30/31 PICKUP decorativos. Sus entradas no tienen botín, venta o interacción; sus objetos no tienen rol ni valor de recompensa. La clase PICKUP por sí sola no crea un objeto recogible en esta ruta: `construir` fusiona geometría y `houses` crea botín mediante `e.botin`/pool y acciones mediante roles.

CPU independiente con `buildVecino` real, Three/agrupación y Canvas simulado, sólo 2786/3244/1594: todos los IDs y definiciones de botín son idénticos antes/después, también sus posiciones. Las listas de acciones de cocina coinciden exactamente: eat/fridge/hide en 2786 y 1594; eat/fridge/hide/hide en 3244. Evidencia `revision_funciones.cpu.mjs/json`, con hashes de las fuentes candidatas leídas. No se han ejecutado recogidas ni persistencia en navegador.

Por tanto, no se demuestra una pérdida funcional actual al reducir provisiones. El pase sí elimina dependientes recursivos sin distinguir funciones: se ha solicitado al autor un fallback atómico si un dependiente futuro lleva rol, botín, interacción o asiento, y un negativo significativo. La alacena sustituida debe conservar su acción de ocultación y destino utilizable; no basta contar muebles.

## Correspondencia y atomicidad observadas

La copia leída ya transmite `A.K.objetos` como `entradasEfectivas` desde ambos constructores y `revisar` las consume. Por tanto, la discrepancia inicial con KITS global está abordada, pendiente de cerrar el P2 anterior. KITS global no se reescribe: nuevoK se crea al comprometer el resultado.

El pase se ejecuta después de la base, no llama a r/U y transforma frentes conservando poses/superficies. Prueba columna amplia, compacta y huella actual; si no acepta ninguna, conserva base y restituye guardias. Construye clones y remapea sop/de mediante índices. Las nuevas piezas pasan límites, reservas, colisión por piezas, usos frontales y cierra. Debe cerrarse con recibos de los cuatro fallbacks exactos y negativos funcionales, no inferirse del comentario de atomicidad.

El flag de fase evita que la actividad consuma RNG durante la base; su activación posterior debe formar parte del contrato comprobado, no permitir ocultar mínimos. Los cambios previstos en el capturador para reconocer variantes aún requieren revisar su delta exacto; esta lectura no acredita ranking/FOV conservados.

## Pendientes / Declined to judge

Parche sellado y SHA final, resolución del P2, contratos 19/negativos, preservación final de fallbacks y no optantes, coste de modelos definitivos y delta del capturador. No se aprueban calidad visual, luz/píxeles, puntuación, todas las semillas, ejecución de acciones, publicación ni CI. No se repiten barridos globales.
