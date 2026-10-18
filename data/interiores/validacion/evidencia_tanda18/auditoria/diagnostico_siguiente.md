# Siguiente tanda · diagnóstico de precedencia · 18-10-2026

**Recomiendo SALÓN: organizar estancia principal y lectura/guardado como dos ámbitos relacionados.** Es la intervención con mayor alcance visible entre estos candidatos: en3244 y1594 el conjunto sofá–TV funciona, pero queda una gran extensión sin programa y el mobiliario secundario aparece disperso. No propongo llenar el centro ni añadir más objetos sobre mesas. T17estudio sigue en cierre/CI según el encargo; este análisis no confirma publicación ni vuelve a puntuar ningún kit.

## Evidencia y precedencia

Se abrieron los cuatro JPG y JSON actuales de `data/interiores/fichas/`, recetas y generadores de salón/trofeos/dormitorio, `src/casa_annie.js`, `docs/interiores.md`, el resumen y las ocho evaluaciones guardadas A/B. Sus hashes corresponden exactamente a estos JPG. Son evaluaciones del17octubre: salón/trofeos/dormitorio de18:53UTC y Annie de14:20UTC. Acreditan esos píxeles, **no el render actual tras cambios compartidos**. No se han hecho llamadas nuevas.

|Orden|Candidato y muestras conocidas|Limitación visible y de receta|
|---|---|---|
|1|**Salón**,2786 matrimonio/rústico16,2m²;3244 artista/bohemio34,8m²;1594 estudiante/joven27,2m². Notas históricas3,116/3,140.|3244 y1594 tienen sofá, mesa yTV, pero la gran pared opuesta/lateral y el otro extremo quedan desocupados o con un puff/planta aislados. La receta relaciona sólo TV→sofá→mesa/alfombra; biblioteca, sillón, aparador y mesita se colocan contra paredes de forma independiente. Hay densidad sobre encimeras, pero poca composición del espacio completo. Suelo jaspeado y flores de colores primarios atraen más que los usos secundarios.2786 ya tiene una camilla reconocible: debe ser control compacto, no recibir por fuerza el programa de una sala de35m².|
|2|**Trofeos**,2132/4204/1679, cazador/rústico,15,4/17,2/15,8m².3,034/3,222.|Cornamentas idénticas repartidas, armero casi vacío y biblioteca genérica dominan; sillón y cómoda no forman un uso común. La receta coloca armero y rifle como dos piezas independientes y usa el mismo pool amplio de librería para las pertenencias. Siguiente intervención propia: frente de guardado de equipo ligado a armero/rifle y bajo de consulta, cornamentas relacionadas con él y sillón+apoyo. No otra biblioteca más llena ni más astas sueltas.|
|3|**Dormitorio**,2786/3244/1689.3,086/3,210.|Las dos pequeñas ya explican dormir+ropa. El problema fuerte es3244: habitación44,2m² con cama, armario, cómoda y sillón apretados en un extremo, biblioteca vacía y una alfombra pequeña aislada en medio. La receta sólo exige cama/una mesita/armario; el ámbito de vestir y la lectura siguen opcionales y dispersos. Haría después dos zonas reales descanso+vestir/lectura; aumentar únicamente la alfombra o la cama no resolvería la distribución.|
|4|**Annie**,una vivienda singular, ficha de8espacios;2,990/2,998.|Cocina y estudio visibles tienen frentes pequeños y paños altos vacíos; dormitorio amplio con cama en un extremo; baños muy blancos y objetos al fondo. Afecta a varios programas, no a una pieza. Cocina/estudio de esta captura son anteriores a las candidatas actuales: no trasladarles el veredicto de T16/T17 ni atribuir su ausencia a un fallo de captura. Propongo revisión propia por estancia después de actualizar evidencia; puede recibir el salón compartido sólo si conserva funciones y presupuesto. El primer plano de una puerta en salón y los recortes de otras vistas limitan la evidencia, no prueban colisión o inaccesibilidad.|

Las diferencias pequeñas de notas no precisan este orden: la precedencia combina problema observado, alcance y posibilidad de resolverlo en una tanda coherente. Annie no queda excluida por autorización; su intervención integral es más amplia y su evidencia más antigua.

## Una intervención acotada de salón

**Programa: estar–conversar/TV, más consulta–lectura cuando el plano lo admite.** Mantener la identidad camilla+sillas/orejero de mayores; en los otros perfiles, conservar TV y asientos reales. Relacionar:

- **Sofá, mesa de centro y una huella textil útil**, con distancias domésticas y frente de TV libre. La alfombra debe pertenecer al estar y poder colocarse geométricamente; no decorar un hueco lejano porque el centro rechazó su huella.
- **Biblioteca, asiento secundario y apoyo de lectura** como un segundo ámbito junto a luz natural cuando exista y sus reservas lo permitan. En las salas grandes debe dar uso al extremo actualmente desnudo; en la pequeña puede faltar el asiento adicional si no cabe. No colocar el alto entre sofá yTV ni frente a entrada/ventana.
- **Guardado/exposición baja relacionado con la estancia**, sustituyendo acumulación de piezas dispersas. No una pared entera de cajas: volumen bajo/alto escalonado que explique libros, TV y pertenencias de la familia y deje superficies de uso reconocibles. Aprovechar primero los muebles existentes y las reglas de relación; si el motor actual no consigue el programa completo, documentarlo antes de extenderlo.

Como apoyo del mismo programa, acabado exclusivo de salón con suelo mate de lectura más tranquila y contraste local sofá–suelo–mueble; mantener rústico/bohemio/joven distintos. Dar a cada apoyo una actividad clara (leer, mando/TV o camilla) y reducir la repetición cromática de jarrones de flor. Esto sustituye selección redundante: no aumenta adornos ni baja mínimos. No tocar luz global, rúbrica, dimensiones o cámaras para favorecer el resultado.

## Referencias y límites

Se leyó la nota de diseño del kit y los metadatos existentes de `moodboard_vivienda.json`, `moodboard_vivienda_b.json` y las referencias formales. Salón mezcla mesa camilla y casas museo con vivienda contemporánea; orienta las dos familias de programa, no una única decoración. Trofeos usa principalmente castillos/pabellones de caza: no justifica copiar escala palaciega a una habitación doméstica. Dormitorio mezcla apartamentos y dormitorios históricos. No se abrieron fotos remotas ni se han revalidado sus metadatos: la observación visual anterior procede de los JPG del juego, no de una supuesta inspección nueva de fotos de referencia. Ninguna foto se propone como textura.

**Siguiente paso propuesto, sin ejecutar:** greybox privado en los mismos marcos2786/3244/1594 y cohorte real documentada; preservar botín, acciones de TV/lectura/teléfono/chimenea/piano y asientos según perfil, paso0,80m, apoyos, puertas, tela real, mínimos y60mallas. Negativos de asiento/uso bloqueado y programa que no cabe; fallback íntegro sin alterar medidas. Annie12/13 como controles funcionales si el kit compartido cambia, sin inventar que esa sea la semilla de la ficha antigua. Después, capturas de conjunto/uso con método conservado y revisión independiente: no se promete4/5 a partir del diseño.

## Huella de imágenes leídas

- `data/interiores/fichas/casa_salon.jpg`: `f17dbf8c03bed386bdd01689719af4e106b2ea7678dd43aedc9b95ef12c620ad`.
- `data/interiores/fichas/casa_trofeos.jpg`: `8987ee2a6b9d2ba0e697ae7aed2fb55ac1c6c65e2a8c9d54a6fcdfd7a734a14d`.
- `data/interiores/fichas/casa_dorm.jpg`: `923f1f48b3875a996f81921ea9bea7ae74fd4cc4cf0a43235c8960a28dd5cbea`.
- `data/interiores/fichas/casa_annie.jpg`: `18393c661df58d8c03134b560c9bee88715abf32b6cbe402eedbdb06ce30ea04`.

Sólo lectura del juego e informe privado. Sin implementación, GPU, API, pruebas nuevas, puntuación propia ni comprobación de publicación.

## Apéndice · nueva base T17 del salón

**La captura nueva confirma SALÓN primero y mantiene el programa propuesto.** Se abrió `.cache/calidad/tanda18/base_T17/capturas/casa_salon.jpg`, SHA256 `1e5ec49b0658d7f520d043da91c72237483a4e033f171548f2439e97587285f4`, y se leyeron su JSON/procedencia. La procedencia declara base local `765c1590078779d4b5d318ed98f838a4f678f751`,492 inputs estables y veto de errores/shaders. El cotejo de metadatos confirma seis guardas libres antes/después del render y cinco poses históricas idénticas; sólo cambia2786/uso. Estas guardas acreditan la cámara, no los accesos funcionales de toda la sala.

- **2786:** la nueva vista0 acerca la camilla al primer plano; camilla+sillas, orejero, biblioteca y mueble bajo ya explican una estancia compacta. La vista1 permite reconocerlo sin ese recorte. Mantenerlo como control; no imponerle otro ámbito ni interpretar el nuevo recorte de mesa como regresión del producto.
- **3244:** persisten el estar reconocible junto a sofá/TV y un extremo con puff/planta/apoyo aislados, separado por mucha superficie vacía. Los pequeños adornos sobre el aparador no explican ese segundo ámbito. Prioridad real: biblioteca–asiento–apoyo de lectura o guardado de consulta como conjunto, sin convertir toda la pared en una masa alta ni llenar el centro.
- **1594:** el sofá, TV y mesa forman un uso claro, pero biblioteca/apoyo, puff y planta siguen desligados. Continúa el gran paño blanco y suelo jaspeado dominante. Relacionar consulta/lectura con el estar aportaría más que cambiar de nuevo los objetos de la mesa.

Las vistas no muestran todas las piezas desde todos los lados: no declaro ausente una biblioteca oculta fuera de campo ni infiero colisiones. La propuesta es corregir relaciones y jerarquía en el plano completo, con acabado local como apoyo; no encuadrar mejor el vacío. Esta base actual sustituye a la histórica **para la futura comparación de salón**, sin sobrescribir la historia ni trasladar sus notas A/B a T17. No se asigna nota nueva y no se acredita publicación: Pages/prueba pública seguían pendientes según el aviso de raíz, sin consulta de estado por este revisor.
