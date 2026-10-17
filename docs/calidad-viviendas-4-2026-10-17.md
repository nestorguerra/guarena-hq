# Calidad visual de viviendas: objetivo 4/5

Encargo del 17-10-2026: mejorar primero las habitaciones peor puntuadas y validar y desplegar cada tanda. Base recuperable: c0c4f5315d913d07332fc9e7b2439e36d0923d3b.

Se conserva la rúbrica doméstica de data/interiors_review.json: media de al menos 4 y ninguna dimensión por debajo de 3 en ambas evaluaciones A/B. Las peticiones usan el mismo modelo, referencias y semillas, sin repetir una llamada solo por una nota desfavorable. Las imágenes y los resultados quedan vinculados por hash. Cambiar las cámaras mejora la evidencia visible y se declara; no se atribuye toda diferencia de puntuación únicamente al mobiliario.

## Tanda 1: taller y baño

Base: taller 2,658/2,688 y baño 2,692/2,714. Cambios: banco a altura de trabajo con panel integrado y tornillo, estantería propia, almacenaje agrupado y fondo de menor contraste; en baño, zonas húmeda y de lavabo agrupadas, muebles con contraste, espejo, enseres reconocibles y revestimiento. Los paños respetan puertas y ventanas y no cambian colliders. Los materiales se comparten para respetar el límite de mallas. Se ha reproducido una pérdida de defines al clonar materiales en los lotes: el clon de three.js restablecía los valores estándar. Se conservan explícitamente los parámetros de acabado y se añade una regresión RED→GREEN. El ajuste compartido afecta también a las paredes limpias de las otras salas; sus notas anteriores siguen siendo línea base, no reevaluación de esta versión.

Las capturas conservan las tres semillas anteriores por kit, anotan posición, objetivo y campo de visión de cada cámara y buscan vistas complementarias de los muebles desde suelo libre. No se cambian los planos ni se eliminan ejemplos desfavorables.

Resultado de la tanda: taller A/B 2,842/2,942; baño A/B 2,904/2,754. Ninguno alcanza el objetivo. Pasan 22 contratos, 200 casas/1166 habitaciones, 81 distribuciones de cada kit y el paquete con Annie. Máximos sintéticos: 49172 triángulos, 59 mallas, nueve luces, 145,3 ms. Los artefactos de azulejo se resolvieron mediante piezas coplanares sin solapes; el revisor confirmó las seis vistas. Pendiente verificar la publicación de esta tanda.

Se conservan los intentos de evaluación anteriores en historico/. Algunas capturas intermedias se sobrescribieron antes de conservar su copia exacta; no se atribuye una imagen diferente a esos hashes. Las cuatro evaluaciones finales tienen imagen exacta conservada en imagenes/ y el instrumento guarda esa copia antes de cada petición futura.

## Orden de las siguientes tandas

Trastero y despacho; cocina y costura; después las demás salas en orden de nota. Las salas afectadas por cambios compartidos se vuelven a capturar y evaluar antes de declararlas sobre el umbral. Annie también debe alcanzar el objetivo. El progreso se actualizará con pruebas, notas y commit publicado por tanda.
