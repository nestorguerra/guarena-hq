# Revisión independiente — biblioteca B, modelos/receta/contratos

**P2 abierto; no integrar esta versión hasta corregir la interpenetración interna indicada.** Motor ya revisado por separado sin P1/P2; no se reabre ni se aprueba globalmente la receta por ese dictamen. Parche combinado revisado `77199982fcfb82e6179f40f0de31b2c0783f3a27fa5d5250c594d57b59a52b9c`; contratos `a0e71e46bc445b22a128473f919582a10f768e7f9a8eeb36df2e3446fb4b33c3`.

## Hallazgo

**[P2] Separar la caja y la pila de cuadernos dentro de vb_hacer_biblioteca.** `tools/interiores/catalogo_vivienda_b.py:88–91` (copia candidata). La caja izquierda ocupa x=[−.2225,.0575], y=[0,.216]. Los cuadernos derechos inferiores ocupan x=[0,.26], y=[0,.025] y x=[.04,.22], y=[.025,.05]. Comparten profundidad, con intersecciones xyz de [.0575,.025,.21] y [.0175,.025,.18] m. Son volúmenes sólidos que se atraviesan, no una holgura numérica ni el contacto previsto entre apoyos. Se repetirá donde se elija esa pertenencia. Recibo determinista: `revision_overlap.json`, calculado de las cajas físicas sin giro del JSON generado.

El contrato de apoyos de `casas_pruebas.js:776–802` exige contacto bajo cada pieza, pero acepta cualquier pieza con base y=0 sin comprobar que otra la atraviese. Por eso la geometría defectuosa pasa tanto ese positivo como sus negativos de cuaderno flotante. Corrección mínima sugerida: separar/acotar los dos conjuntos conservando envolvente y soporte completo, y añadir comprobación entre pares internos con un negativo que reintroduzca esta penetración. No requiere cambiar receta, motor, luces ni cámara. Se ha informado a raíz y al autor; no he editado su modelo.

## Resto de la revisión

Los otros objetos del catálogo B permanecen idénticos estructuralmente; sólo se añaden los tres IDs propios. Biblioteca rol libros, soporte suelo y pertenencias decorativas de superficie sin rol nuevo preservan la integración de lectura/juego. Armario, mesa, silla, cama y mesita conservan sus modelos/roles. Baldas .48/.93 corresponden a la cara superior de los tableros .468/.918 de .024m; contenido de .24m cabe bajo el siguiente nivel. La caja inferior del mueble contacta la base a .04m. No he detectado otro bloqueo geométrico en esa lectura.

La receta vincula mesa y biblioteca, mantiene silla_frontal en raíz y reserva física .7×.6 del armario independiente. Cama/mesita se intentan primero. Sigue existiendo fallback individual de la misma receta y reintentos de casa; no se promete rollback T14 universal. El caso4034 cambia descanso por completar intento0 frente al intento1 de base, explícitamente documentado y autorizado por raíz. Los compilados privados no deben copiarse sobre activos; se regenera al integrar.

Los contratos separados usan tanda>=17 sin tocar workflow ni los contratos anteriores. Composición exige de/e del asiento y biblioteca, asiento inmediato, armario independiente, dos superficies con pertenencias referenciadas a sup0/1, bloques apoyados y funciones reales bed/table/seat/read/hide. La reserva frontal se mide con piezas reales, y en4007/5045 se añade sección física .8m además de revisarUso.

Ocultación: construye las seis casas, utiliza la interacción final y llama a métodos originales hideIn/unhide mediante instancia con game mínimo. Requiere posición interior del armario, estados/FOV/CSS, regreso EXACTO al punto inicial, resolución corporal .34m sin profundidad ni desplazamiento >1e-6 y sin contención en mueble de suelo de la planta. El negativo usa salida al centro sólido. Conserva/restaura CSS y libera geometrías en finally. Esto comprueba método y geometría; no el selector/prompt, la oclusión visual del residente ni el bucle completo del navegador. Esos límites coinciden con la entrega.

## Evidencia propia

`contratos.revision.cpu.mjs` reejecutó los tres callbacks exactos con salida separada `contratos_revision_cpu.json`: **3/3 PASS**, incluido buildVecino/colisionador real de las seis casas. La importación browser de Interiors se sustituye en CPU por los métodos extraídos de su fuente; DOM/classList y Canvas son dobles explícitos, sin raster ni GPU. El PASS no invalida el P2 de modelo que el oráculo aún no comprueba.

`git apply --check` de candidata y contratos pasa contra el árbol actual. Receta/modelos antiguos conservados por comparación JSON propia. No se han repetido barridos largos ni ejecutado GPU, build, CI, capturas o cambios de producto.

**Declined to judge:** lectura visual de la nueva distribución, cámaras libres, aprobado4/5, resultado de navegador de los contratos, ocultación gráfica, costes/FPS medidos, publicación y garantías para toda habitación fuera de la muestra. El cierre queda pendiente del P2 y del nuevo SHA, sin borrar este recibo inicial.


---

Cierre posterior: P2 cerrado en B v2. Dictamen y evidencia independiente en [revision_v2_adenda.md](revision_v2_adenda.md). Se conserva arriba el estado inicial.
