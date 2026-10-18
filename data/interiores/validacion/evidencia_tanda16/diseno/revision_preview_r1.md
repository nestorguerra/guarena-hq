# Cocina T16 — revisión visual independiente del preview R1

**Conservaría la propuesta visual para continuar hacia la integración, condicionada a la revisión técnica y al cierre de la candidata final.** El cambio mejora el conjunto de guardado–preparación–cocción en las tres muestras; no es sólo una tanda de detalles. No identifico en estas imágenes una regresión visual importante que obligue a rehacer el programa antes de continuar. Esto no aprueba técnicamente la candidata ni el despliegue y no acredita una nota 4/5.

Revisadas la ficha base T15, la ficha preview y las seis imágenes individuales nuevas. La comparación utiliza `.cache/calidad/cocina_t16/captura_base_T15/`, no las cámaras históricas previas.

## Resultado frente a los criterios

| Pareja | Ganancia / límite |
| --- | --- |
| 2786 / uso | La alacena sustituye la exposición multicolor por guardado cerrado y un hueco con jarra/taza reconocibles. Gana mucha presencia vertical, pero los paneles crema con madera oscura evitan la pantalla marrón temida. Fuego, olla, fregadero y preparación continúan reconocibles. La tabla con pan se lee mejor como actividad que la hilera anterior de botellas. La parte alta de la alacena queda recortada: no se certifica su remate por esta vista. |
| 2786 / conjunto | La banda enlaza visualmente preparación y nevera, con una escala más coherente que el alto anterior aislado. Encimera y lavadora quedan despejadas. El lateral de alacena sigue entrando por la izquierda, sin una nueva ocultación importante del núcleo en esta toma. El carácter rústico persiste en madera y marcos, aunque la cocina se vuelve apreciablemente más clara. |
| 3244 / uso | Los frentes verdosos se separan mejor de encimera, pared y suelo. Fogones, mandos, horno y fregadero mantienen lectura. Se sigue recortando casi toda la zona de preparación y el alto: esta imagen no demuestra la recomposición completa. |
| 3244 / conjunto | Es clara la nueva relación alacena–nevera–banda alta y el plano de preparación libre. Las grandes masas ahora forman un frente doméstico en lugar de una estantería con provisiones junto a un alto aislado. El hueco abierto justo sobre la nevera queda poco explicado: su contenido bajo apenas destaca y puede parecer una interrupción residual de la banda. |
| 1594 / uso | El cambio de valor/color distingue los muebles del fondo claro y mantiene el núcleo funcional reconocible. La actividad de preparación sólo asoma por el borde: no atribuirle mejora de lectura desde esta toma. |
| 1594 / conjunto | La alacena visible al extremo y la banda alta dan continuidad y densidad útil al frente sin una nueva isla ni más objetos. El verde azulado separa bien encimera, horno y puertas; se conserva una cocina clara. El conjunto ya comunica guardado y preparación. Mesa y sillas siguen parcialmente recortadas. |

## Puntos críticos resueltos visualmente y reservas

- **Alacena 2786:** el riesgo de pantalla oscura no se materializa de forma importante en estas dos vistas. El nuevo volumen es dominante en uso, pero sus paneles claros y el hueco diario permiten leerlo como mueble. No se infiere de esto visibilidad universal al recorrer la cocina ni funcionamiento de guardado/ocultación.
- **Unión banda/nevera:** no se observa una ranura negra fuerte ni una interpenetración inequívoca en las tres vistas de conjunto. La diferencia de profundidad se entiende razonablemente como muebles altos sobre un electrodoméstico más profundo. La cercanía visual es grande; las imágenes no certifican la holgura de 7 cm ni barridos de puertas. Los remates y juntas deben conservarse en la versión final, sin aumentar volúmenes por mera continuidad gráfica.
- **Actividad pan:** tabla y pieza ovalada se reconocen por contexto como preparación de comida y dejan espacio libre. Es una mejora real frente a las provisiones dispersas. La hogaza lisa es genérica y se repite en las tres casas; no basta para distinguir hábitos domésticos. Es un pendiente de acabado, no una razón para recuperar más botes. Si se mejora, conviene trabajar la forma/lectura de la actividad existente sin aumentar la cantidad de objetos.
- **Hueco alto 3244:** el hueco encima de la nevera aporta variedad de frente, pero su contenido resulta poco legible y queda muy alto respecto a la preparación. Revisaría su función visual en un acabado posterior; no presentaría ese hueco como un puesto cotidiano accesible verificado. La alacena baja sí ofrece vajilla reconocible. No es una colisión demostrada ni un bloqueo visual del conjunto.

## Qué queda fuera de la aceptación parcial

Las dos grandes aún comparten una receta muy parecida y abundan paños altos claros. La candidata reduce el aspecto de exposición de productos sin convertir todo el frente en cajas indiferenciadas, pero no resuelve toda la variedad doméstica. La mesa no se ha evaluado completamente; su recorte no justifica moverla. En 3244 se aprecia además cambio de color del asiento visible (rojizo en base, amarillo en preview): se registra como diferencia real, sin atribuirle cambio de geometría ni asumir su causa. La comparación no aísla únicamente volumen de muebles; incluye material, contenido y otros cambios visibles.

No observo roturas evidentes de textura, piezas flotantes claras ni pérdida importante de lectura de cocina/fregadero en las seis capturas. La ausencia de estos defectos en píxeles no prueba reservas, acciones, dependencias, botín, RNG, fallbacks ni presupuesto. Esos aspectos corresponden a la revisión técnica y a la candidata final; no se aprueban por estos fotogramas.

## Procedencia y comprobaciones realizadas

- Base T15 ficha SHA256: `eedf6d1f6cfa8240025cfba64c273c01716a30f776d77eafea4c07fbc6f9633c`.
- Preview ficha SHA256: `eede2f4b7b174e1ff26696f7a60522542f99ce5683fd44bacf7c221325eef51c`.
- Preview JSON SHA256: `10aeeb984b5f8c7de009f74237e02c8ab5a70283e4f858e365089daabbbe031f`.
- `preview_r1/procedencia_final.json` SHA256: `b2da2b5c945ca1fae62abf4d89f53976af3b2731c6c86437bef55b27a86ee2b0`.
- Todos los archivos de captura del preview cotejados con su manifest: hashes coincidentes. Comparación directa de posición, objetivo y FOV con la base: **6/6 idénticas**. Los metadatos registran **6/6 guardas finales libres**.
- La procedencia registra 116 fuentes candidatas estables y capturador privado SHA `6b45ac1f4ef9c824877fe277f838d57815f0fd34b4293dafe7d77950f054e996`. Se lee ese recibo; esta revisión no repite una auditoría de todas las fuentes.
- Se conserva la explicación del primer assert: comparó erróneamente las dos salidas previstas con la ficha histórica copiada. El control corregido excluyó esas salidas y comprobó las demás fuentes. No se describe ese episodio como fallo del producto.

Este snapshot es previo a las últimas correcciones del control de metadatos; no certifica su estado final. Misma pose no significa iluminación dinámica idéntica en píxeles. Sin GPU, navegador, build, API, puntuación ni modificaciones de producto por este revisor. Dictamen y reservas trasladados al autor `revision_visual_uno`.
