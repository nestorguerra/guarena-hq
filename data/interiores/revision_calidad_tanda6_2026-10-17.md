# Tanda 6 — revisión visual independiente del trastero

17 de octubre de 2026. Reabiertos únicamente casa_trastero.jpg y su JSON finales, modificados a las 18:52:36. Semillas canónicas 1594, 3886 y 4589; estudiante/joven, planta 1. No se ha abierto el juego ni se ha interferido con el pipeline de integración.

| Archivo | SHA-256 |
|---|---|
| casa_trastero.jpg | 25b019a4b01bc4af938b905ada53add91e819912762daac641b7be82dbde9b75 |
| casa_trastero.json | 6d9a97640c6595c5be9f60653a29c486bc36f63f700a2fb5e462116cd2b8873a |

**Conclusión:** la bicicleta añade una pertenencia doméstica reconocible y da más identidad al trastero que la receta anterior de cajas, archivadores y textiles. Ventilador, recipiente/cesto y herramientas largas refuerzan esa lectura. Las tres muestras se pueden examinar combinando sus dos vistas, con una oclusión importante de la primera cámara en 1594. No se observa un defecto nuevo demostrado de geometría o una pieza claramente flotando.

## Cobertura concreta

| Semilla | Primera vista | Vista general | Resultado y límite |
|---|---|---|---|
| 1594 | La estantería próxima ocupa buena parte del primer plano y tapa parte de la bicicleta. | Se reconoce bicicleta entre estanterías, recipiente/cesto y almacenaje. | La pertenencia queda demostrada por la general; la primera no cumple del todo el propósito de mostrarla con claridad. |
| 3886 | Bicicleta completa, con cuadro, ruedas, sillín y manillar reconocibles. | Explica almacenaje, cajas, herramientas y ventilador junto a la pared. | Buen reparto entre pertenencia principal y contexto. La general mira a la otra zona; no necesita repetir la bicicleta completa. |
| 4589 | Bicicleta y ventilador legibles; recipiente/cesto próximo. | Muestra profundidad de la sala y almacenaje; la bicicleta queda parcialmente escondida por las cajas al fondo. | La primera compensa la oclusión de la general y permite revisar el objeto principal. |

**La escalera no tiene cobertura visual en esta ficha.** Las tres semillas muestran bicicleta. No se extrapola a la variante de escalera ni se afirma haber comprobado su escala, colocación o lectura.

## Mejora de identidad y composición

- Se diferencia mejor una casa que guarda pertenencias de un archivo de cajas. El cuadro y las ruedas de la bicicleta aportan una silueta nueva a la altura baja de la habitación.
- El ventilador tiene pie, aro y aspas reconocibles. Su carácter doméstico se entiende, aunque el tono claro lo acerca bastante a la pared.
- Las cajas agrupadas, estanterías, herramientas apoyadas y recipiente/cesto siguen teniendo escalas compatibles entre sí. No veo una acumulación aleatoria que impida leer la sala.
- Las baldas y cajas conservan diferencias de tono; etiquetas y archivadores se leen. El conjunto sigue siendo muy luminoso y de contraste contenido: no describo estas capturas como una habitación mucho más oscura.
- Las tres muestras comparten la misma bicicleta y una receta de almacenaje parecida. Hay cambios de distribución y acompañantes, pero la variedad de pertenencia principal no está demostrada.

## Defecto y acabados pendientes

**1594 conserva un defecto de encuadre concreto:** la primera vista, destinada a la pertenencia, queda dominada por una estantería a la derecha. Se ve la bicicleta, pero parte del cuadro/rueda queda detrás de los montantes y cajas. La penalización de oclusiones comunicada no se da por eficaz solo porque exista; esta imagen muestra su límite.

No es una ausencia de bicicleta ni una colisión confirmada. La vista general resuelve su identificación, por lo que no se convierte en una laguna total de evidencia. Si se retoca el encuadre en otra tanda, la prioridad sería dejar la bicicleta libre en esa primera vista.

Como acabados diferibles quedan el poco contraste del ventilador contra la pared y la escasa sombra de apoyo en algunas piezas claras. No reaparecen manchas negras/granuladas dominantes como las vistas en la cocina anterior. Los JPG no permiten revisar estabilidad de sombras en movimiento.

## Metadatos y alcance

El JSON documenta cámaras a y = 4,7 m, objetivos de uso a y = 3,95 m y objetivos generales a y = 4,5 m, con FOV 68°. Son coordenadas de planta alta. Corresponden al encuadre descrito; por sí solas no verifican altura relativa al suelo, transitabilidad ni la distancia libre al objeto. Tampoco acreditan el funcionamiento del cálculo de oclusiones.

La comparación cualitativa con la evidencia ya examinada del trastero anterior se limita a la incorporación de pertenencias y a su lectura actual; no es una comparación aislada de iluminación con cámaras idénticas.

No se observa un bloqueo visual total que impida reconocer el trastero en estas tres muestras. Se registra el límite de cámara 1594 y la falta de cobertura de escalera, sin atribuir puntuación ni aprobar el objetivo formal 4/5. No se han ejecutado API, pruebas, navegador, puertos ni modificaciones del juego o las fichas.
