# Revisión independiente del comedor sobre T12

**Dictamen: sin hallazgos P1/P2 en el parche revisado. Aceptación estática condicionada para integración y ensayo; no aprobación visual ni de publicación.**

Base comprobada: `e218dc535eeb45ef1e79b0d974098edfd5e8b37e`. Parche privado `.cache/calidad/comedor_t12.patch`, SHA-256 `a188081c71f3c52c67f7edc12061cbebd59c38b6b2f323ca3bea155addeb860b`. Se revisan cinco fuentes y cuatro salidas generadas. No se aplica el parche, no se modifica producto y no se ejecuta navegador/GPU/build.

## Comprobaciones independientes

- Comparación directa de las nueve bases con `git show e218dc5:<archivo>` y de los nueve candidatos con sus hashes de manifiesto; `git apply --check` correcto. Se verifican también los hashes de los recibos CPU. Evidencia propia: `comedor_t12_revision_verificacion.json`.
- Comparación semántica de todo `src/interiores_datos.js`: sólo se añade `OBJETOS.va_mesa_familiar` y cambia `KITS.vivienda_comedor`. Ningún objeto previo ni otro kit cambia. Galería infantil T12 intacta. No se incorpora mural, composición T13, fábrica de material ni contrato T15. Los contratos previos son literalmente idénticos al quitar los dos nuevos.
- `tools/interiores/kits_vivienda_a.py:54–69` y `src/locales.js:387–423,506`: área inferior a 12 y área desde 12 forman una partición sin hueco. El conjunto de cuatro lados exige las cuatro sillas antes de comprometer mesa/asientos; mantiene `libre`, límites, separación geométrica y `cierra`. Los asientos conservan `de` al índice de la mesa. No hay fallback oculto a dos asientos en el conjunto grande ni cambios del solver.
- `tools/interiores/catalogo_vivienda_a.py:27–29`: mesa nueva exclusiva, 1,35 × 0,80 m, altura 0,75 m, rol mesa y superficie coincidente con el tablero. Sus cuatro patas apoyan en suelo y llegan al tablero. La mesa compartida de cocina, 1,05 × 0,70 m, queda exacta. El pool nuevo usa identificadores existentes; comida con geometría real (pan, fruta, tortilla o caldo), sin paquetes de tienda. Pool de 34 objetos frente al mínimo 30, acreditado en el recibo de datos.
- `src/acabados_vivienda.js:22–42` y `src/houses.js:562`: acabado sólo del comedor y exclusión coherente del zócalo antiguo. Los paños se recortan antes de dividirse a 1,02 m, sin superposición entre mitades; suelo a +0,009 m y techo a altura−0,008 m, coherentes con los otros acabados existentes. Material no emisor, roughness 0,94, sin texturas nuevas. No cambia reservas/colliders ni consume RNG.
- Ensayo propio de los paños con puertas/ventanas solapadas, ventana lateral, dos plantas/alturas y tres estilos: seis casos correctos, sin ocupar huecos ni exceder cotas. Dobles de geometría/material; acredita las coordenadas emitidas, no rasterización. Instrumento/recibo: `comedor_t12_revision_panos.mjs/json`.
- Los dos nuevos contratos `tools/interiores/casas_pruebas.js:653–688` comprueban tres constructores reales, mesa/sillas asociadas, servicio apoyado y uso; frontera 11,999/12/12,001; rechazo de conjunto incompleto y reserva total sin vajilla huérfana. Guard `opts.tanda>=16`; una integración que sólo ejecute la tanda anterior no los ejecutará.

## Evidencia del autor leída, no repetida como prueba propia

`comedor_t12_candidato/cpu.json`: 53 salas y 81 semillas, cero errores. `cpu_full.json`: constructor, geometría, merge y colisiones reales en 2786/5157/2606; cero errores de uso completo y otras estancias con metadata idéntica. Costes: 54→55, 57→58 y 58→59 mallas; luces 7/8/8 sin cambio en esas tres. `cpu200_cost.json`: 200 casas, 66 comedores, cero errores de coste/validación local, máximo 60 mallas. Estos recibos son de CPU, con Canvas sin rasterización y texturas externas sin píxeles; no acreditan navegador ni GPU.

## Límites y riesgos que permanecen

1. El margen de coste llega al límite de 60 mallas. No hay presupuesto elevado ni retirada encubierta de muebles. El coste real de navegador y la integración/paquete siguen pendientes.
2. Cambia el estado final del RNG y el mobiliario del comedor en 53/53 salas comparadas; cambian posición/cantidad de lámparas en 6 (1015, 1054, 1105, 1118, 1148, 1165). No se declara preservación de esas tiradas. La regla/familia de luz se mantiene. Conviene incluir una de esas seis en la comprobación posterior.
3. Cuatro sillas no equivalen a cuatro puestos servidos: hay comida y bebida compartidas, sin relación de vajilla por asiento. Es una limitación deliberada de la propuesta; raíz debe decidir tras ficha si el tablero queda insuficientemente servido, antes de puntuar.
4. Una sala de área ≥12 con forma/reservas incompatibles puede rechazar toda la mesa grande; el parche no añade sustitución automática por mesa pequeña. Es coherente con la capacidad exigida y conserva el fallo de mínimos. Las muestras no prueban todas las plantas/semillas posibles.
5. Los contratos no prueban por sí solos toda la navegación de las 200 casas ni persistencia de una partida. El motor de usos/botín no cambia; no se infiere de ello cobertura universal.

**Declined to judge:** estética o nota 4/5, legibilidad del servicio y suelo en captura, sombras/contraste efectivo, rendimiento GPU/FPS, navegación global de 200 casas, partida real del usuario, despliegue y aprobación del usuario. El comedor antiguo sobre T13 (`5bf4…`) queda histórico; sus resultados no sustituyen los recibos de esta base.
