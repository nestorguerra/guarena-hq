# Calidad visual de viviendas: objetivo 4/5

Encargo del 17-10-2026: mejorar primero las habitaciones peor puntuadas y validar y desplegar cada tanda. Base recuperable: c0c4f5315d913d07332fc9e7b2439e36d0923d3b.

Se conserva la rúbrica doméstica de data/interiors_review.json: media de al menos 4 y ninguna dimensión por debajo de 3 en ambas evaluaciones A/B. Las peticiones usan el mismo modelo, referencias y semillas, sin repetir una llamada solo por una nota desfavorable. Las imágenes y los resultados quedan vinculados por hash. Cambiar las cámaras mejora la evidencia visible y se declara; no se atribuye toda diferencia de puntuación únicamente al mobiliario.

## Tanda 1: taller y baño

Base: taller 2,658/2,688 y baño 2,692/2,714. Cambios: banco a altura de trabajo con panel integrado y tornillo, estantería propia, almacenaje agrupado y fondo de menor contraste; en baño, zonas húmeda y de lavabo agrupadas, muebles con contraste, espejo, enseres reconocibles y revestimiento. Los paños respetan puertas y ventanas y no cambian colliders. Los materiales se comparten para respetar el límite de mallas. Se ha reproducido una pérdida de defines al clonar materiales en los lotes: el clon de three.js restablecía los valores estándar. Se conservan explícitamente los parámetros de acabado y se añade una regresión RED→GREEN. El ajuste compartido afecta también a las paredes limpias de las otras salas; sus notas anteriores siguen siendo línea base, no reevaluación de esta versión.

Las capturas conservan las tres semillas anteriores por kit, anotan posición, objetivo y campo de visión de cada cámara y buscan vistas complementarias de los muebles desde suelo libre. No se cambian los planos ni se eliminan ejemplos desfavorables.

Resultado de la tanda: taller A/B 2,842/2,942; baño A/B 2,904/2,754. Ninguno alcanza el objetivo. Pasan 22 contratos, 200 casas/1166 habitaciones, 81 distribuciones de cada kit y el paquete con Annie. Máximos sintéticos: 49172 triángulos, 59 mallas, nueve luces, 145,3 ms. Los artefactos de azulejo se resolvieron mediante piezas coplanares sin solapes; el revisor confirmó las seis vistas. Publicación verificada: commit 005c758, Actions 39045149975 en verde y página pública con ese commit. La integración pública comprueba entrada, caja, siesta, decoración, comercios y recarga sin errores. El primer verificador exigía document.readyState complete en diez segundos; para la web pública se espera al documento nuevo y al arranque real del juego, sin depender de fuentes u otros recursos remotos secundarios. Se conserva ese intento fallido.

Se conservan los intentos de evaluación anteriores en historico/. Algunas capturas intermedias se sobrescribieron antes de conservar su copia exacta; no se atribuye una imagen diferente a esos hashes. Las cuatro evaluaciones finales tienen imagen exacta conservada en imagenes/ y el instrumento guarda esa copia antes de cada petición futura.

## Orden de las siguientes tandas

Trastero y despacho; cocina y costura; después las demás salas en orden de nota. Las salas afectadas por cambios compartidos se vuelven a capturar y evaluar antes de declararlas sobre el umbral. Annie también debe alcanzar el objetivo. El progreso se actualizará con pruebas, notas y commit publicado por tanda.

## Tanda 2: volumen y uso de baño y taller

Se completan las dos salas iniciales con cantos redondeados opcionales, bañera hueca, inodoro con taza y cisterna y lavabo amplio según superficie. El taller incorpora bancos compactos o amplios con tres actividades posibles: casita, marco y motor de riego. Las tres semillas de evidencia muestran casita y motor; no demuestran por sí solas la tercera variante. Las ventanas del baño incorporan privacidad mate. El coste real de la geometría redondeada se contabiliza y un contrato comprueba sus dimensiones y sus 108 triángulos por caja.

Las cámaras documentan uso y conjunto a altura de jugador. Una primera ficha no mostraba el WC del baño 2786; se conserva su evaluación en historico/calidad_tanda2_cobertura_parcial. La cámara secundaria apunta ahora al conjunto sanitario, sin cambiar las semillas. El revisor independiente confirma que ya puede examinarlo. La mejora de cobertura también afecta a las notas: no se atribuye al mobiliario toda la variación.

Resultado final: taller A/B 3,154/3,218; baño A/B 3,036/2,854. Ninguno llega a 4. Pasan 23 contratos, 200 casas/1166 habitaciones y 81 distribuciones de cada kit, además de juego fuente, paquete y control de marcas. Máximos: 56190 triángulos, 59 mallas, nueve luces y 158,5 ms. Regeneración determinista sin diferencias. Publicación de prueba autorizada por tanda; el commit y la revisión pública se registran tras publicarse.

Tanda 2 publicada y verificada: commit 6a214fb, validación 39046360726 y Pages 39046553694 en verde. La integración pública relee ese commit, entra en casas y comercios y conserva caja, siesta y partida ficticia tras recargar, sin errores.

## Tanda 3: trastero y despacho

El trastero incorpora estanterías de tamaño doméstico con cajas, maletas, textiles y archivos integrados, útiles largos y almacenaje adaptado al área. El despacho incorpora mesas con cajonera y lámpara, silla tapizada y rincón de lectura. Suelos y revestimientos reducen los estampados dominantes. Los muebles por kit de todas las casas usan un relieve artesanal más contenido; este cambio compartido requiere reevaluar las otras fichas antes de atribuirles calidad de la versión actual.

Las mismas semillas muestran uso y conjunto, a altura de jugador. Resultado: trastero A/B 3,082/2,894; despacho 3,322/3,304. Continúan por debajo de 4. El revisor independiente considera suficiente la cobertura de estas muestras, sin defecto importante nuevo; señala contraste de blancos, repetición y ajuste visual del despacho 2665. Las imágenes no certifican colisiones ni acceso, que se comprueban por separado. Las pruebas y sus máximos exactos quedan en validacion/calidad_tanda3.json. Pendiente registrar publicación una vez servida.
