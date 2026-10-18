# T17 · revisión visual del greybox en perspectiva

**Dictamen: conservar la hipótesis de composición, pero no cerrar todavía el detalle de la biblioteca.** 3244 muestra una mejora clara de escala del puesto y separación entre trabajo y lectura. En1594 persiste una obstrucción visual importante en las dos cámaras automáticas; hace falta el diagnóstico fijo desde entrada propuesto por raíz antes de decidir que debe cambiarse el orden de las piezas. No aprobaría esa obstrucción cambiando la cámara de la ficha. Esta revisión no aprueba acabado, integración o publicación, ni otorga puntuación.

## Procedencia revisada

Se han visto la ficha y sus seis imágenes individuales, junto a la base T16. Los diez hashes recogidos en `preview_greybox/capturas/procedencia.json` coinciden con sus archivos. Se ha cotejado el JSON de cámaras con el de la base: sólo coinciden **3244/conjunto y1481/conjunto**; cambian las otras cuatro poses. Las seis vistas registran guardas libres antes y después del render. La procedencia informa de490 entradas estables, alta manual y DPR1; esta revisión no ha vuelto a capturar ni ha verificado el proceso GPU. No hay acabados R2 ni modelos finales.

- Ficha greybox: `bb2e46af8b6bd003f841ff28a9e8901d0d228c1f2b66485e12d62adc80ec220a`.
- JSON greybox: `e7ce13d6ddc87e8a24a47dc6a407302ab7fe215e615d97d3a776fe26fc0f45d2`.
- Procedencia: `c39354d1ff675193f919021d5fa878715ab04eed5e7c329a5e86da2c4202d9d9`.
- Ficha base T16: `d70efcfa6f89273d53a7cb6ed4c6f3a24fe1659bb56227e8b2a60c7adeca838e`.

## Lo que muestran las seis vistas

**3244/uso:** la mesa ofrece un tablero reconocible delante del ordenador, con silla propia y respaldo de consulta. El puesto ya no queda reducido a una mesa pequeña detrás del sillón. Biblioteca y bajo forman un frente relacionado con la ventana. La caja alta domina aún el centro del frente por su masa ciega; su condición gris explica parte importante de ello. No puede darse por resuelta la jerarquía final sólo por el ajuste geométrico.

**3244/conjunto — misma pose que la base:** ahora se distinguen un ámbito de trabajo próximo y un rincón de lectura separado con apoyo. El sillón deja de ocultar la mesa. El paño derecho y el centro continúan extensos; no concluyo que haya que rellenarlos con otro mueble. Conviene observar esta disposición con la biblioteca real antes de añadir otro volumen. El sillón pasa visiblemente de amarillo a morado, por lo que su menor predominio no se atribuye exclusivamente a la colocación: también cambian color y distancia respecto al ojo. No he verificado aquí la causa de ese cambio de tinte.

**1594/uso:** se ve el ordenador, una parte sustancial del tablero y la silla, mejor definidos que en la antigua vista de uso. Sin embargo, la biblioteca ocupa gran parte del primer plano y corta la relación visual con el bajo. Es un obstáculo importante para leer el conjunto, aunque no borra por completo el puesto.

**1594/conjunto:** predominan la biblioteca, la puerta y el paño azul; la mesa queda casi fuera de imagen. Esta cámara mira hacia la puerta desde dentro, no representa mirar al puesto desde el acceso. La toma no permite deducir que un jugador que entra vea lo mismo. Tampoco debe descartarse como una foto incómoda: evidencia que el frente tiene una masa alta dominante en parte del recorrido.

En ambas vistas de1594, llamar al problema únicamente «lateral de biblioteca» sería impreciso: se ve una porción amplia de su **frente macizo provisional**, además del canto. Una biblioteca abierta cambiará esa superficie frontal. No garantiza eliminar el contorno alto ni la ocultación desde el lado; sólo cambiar el material o dibujar libros encima no basta para afirmar una solución.

**1481/uso:** el puesto queda relacionado con la biblioteca y el bajo en un mismo frente, frente a la mesa aislada junto a la puerta de T16. La lectura del tablero es posible, pero el volumen alto conserva el protagonismo y el suelo jaspeado ocupa gran parte de la imagen. Cambia la cámara, por lo que no es una comparación causal pura.

**1481/conjunto — misma pose que la base:** se ve la relación bajo–alto–mesa y la ventana libre, aunque el puesto queda en el borde derecho. La biblioteca gris elimina temporalmente la información de baldas/libros que daba domesticidad a la base. Eso limita la comparación de variedad y densidad final; no es razón para aprobar la caja como acabado ni para declarar que el programa final tendrá menos contenido. 1481 sigue siendo fixture sintética.

## Decisión antes de detallar

**No ordenaría aún un cambio de disposición sólo por estas cámaras, pero mantendría pendiente la biblioteca y su relación con el puesto.** El siguiente dato útil es una vista de1594 desde el acceso real, con ojo/posición registrados y guardas libres, mirando al puesto. Debe conservarse como diagnóstico adicional, sin sustituir las seis canónicas ni mejorar su encuadre retrospectivamente. No hace falta una búsqueda de ángulos favorables.

Si desde la entrada la masa alta también tapa ordenador, tablero o silla, habría motivo para ajustar la relación de piezas **antes del detalle**. La primera alternativa a estudiar sería una transición baja entre puesto y biblioteca, desplazando el alto hacia el extremo del frente, sin estrechar el paso ni forzar el hueco de ventana. No es una solución aprobada: requiere nueva comprobación del grupo completo y no debe imponerse por semilla o cámara.

Si desde la entrada se lee el puesto con claridad, conservaría la disposición para modelar una biblioteca realmente abierta y con masa lateral controlada. Después habría que volver a comprobar las vistas canónicas y el recorrido: la apertura del frente no autoriza ignorar un lateral que siga actuando como pantalla. La cuestión es la relación funcional y espacial, no lograr una fotografía bonita.

En3244 mantendría de momento el frente y la lectura secundaria; en1481, el frente relacionado. El suelo jaspeado sigue compitiendo con el mobiliario, pero el acabado R2 pendiente debe evaluarse por separado y no utilizarse para tapar un fallo de disposición. Respaldo, paneles de consulta, libros y guardado final aún deben aportar identidad adulta; estos bloques no demuestran variedad ni una calidad4/5.

## Límites

No se infieren colisiones, capacidad de recogida, navegación, persistencia o acciones a partir de píxeles. Los recibos CPU previos no aprueban la apariencia. No se ha ejecutado GPU, navegador, API, build ni modificado producto. La autorización anterior para capturar el greybox se ha consumado por raíz y no implicaba aceptar el resultado; esta revisión deja pendiente el diagnóstico de1594 antes de cerrar su diseño.

## Adenda · diagnóstico desde la entrada de1594

**Decisión: procede UNA prueba privada del orden mesa → bajo → biblioteca antes de detallar los muebles.** Mismas dimensiones y motor existente, sin añadir masas, alterar cámaras ni forzar una colocación inválida. Es aprobación de contrastar una hipótesis de composición, no de integrar esa disposición ni de ejecutar GPU por parte de este revisor.

Las dos imágenes parten del mismo punto físico exacto `[-5199.469532269612, 4.7, -5194.0573493495585]`, mismo inicio real, FOV75, alta/DPR1 y marco. Se han cotejado esos campos y las guardas libres antes/después. **La orientación no es idéntica:** cada mirada sigue su escritorio real, con objetivos distintos registrados. Son diagnósticos del acceso, no sustitutos de las cámaras canónicas ni un A/B de orientación fija.

La silla y el tablero del greybox se reconocen mejor que en T16, pero el alto sigue interpuesto y oculta parte de pantalla/puesto desde la entrada. Esta evidencia descarta explicar toda la dificultad como una mala selección de las cámaras automáticas. No demuestra que cualquier biblioteca abierta vaya a producir la misma oclusión; sí impide darla por resuelta de antemano sólo con baldas y libros. La apertura del frente aliviaría masa ciega, mientras su contorno/costado seguirían presentes.

La transición baja propuesta permitiría ensayar continuidad visual entre superficie de trabajo y guardado, desplazando el volumen alto al extremo. **No se presume que funcione:** debe pasar el grupo completo y sus reservas en las tres muestras, especialmente la ventana de3244, sin cambios de semilla, dimensiones, pasos o ramas por cámara. Si no cabe, conservar el fallo y la variante previa; no abrir otra serie de pequeños desplazamientos para salvar esta prueba. Si pasa CPU, comparar con el mismo punto/FOV y criterio de mirada desde entrada y con las canónicas completas, documentando cualquier pose automática que deba cambiar por seguridad.

Hashes del diagnóstico leído:
- `base_T16.jpg`: `6b4cb400c6fa329a3ebccc53f85ddd72dd685ecfe728455d8c05ddd321823830`.
- `greybox.jpg`: `161bea3fefde38e2fb865947e0a2038adfb58f5e41678a031156c53c0643a222`.
- `base_T16.json`: `972f0ebfb416675c057cd85d8a17ce0eca768a032ac74b651386d388c4d1742b`.
- `greybox.json`: `c30e951a5502b3a7a02b867dfa6bb9368266c82bd479468232952af9376a16ef`.

El dato de490 entradas estables procede de raíz; esta adenda sólo ha leído imágenes/JSON y comprobado sus campos y hashes. Sin API, GPU, cambios de producto o puntuación formal.
