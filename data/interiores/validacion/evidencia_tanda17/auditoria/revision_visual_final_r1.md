# T17 · Revisión visual final R1

**Conservar la candidata: mejora coherente de composición y lectura respecto a R2 y al estudio T16.** No veo una corrección obligatoria de distribución o modelos antes de continuar la validación. Sí debe aclararse el origen de las motas blancas visibles antes de presentar el acabado como cerrado. No se aprueba publicación ni se asigna puntuación.

## Evidencia y comparabilidad

He abierto la ficha final y sus seis imágenes individuales, la ficha R2, la base T16 y la entrada fija 1594 final/R2. Los diez hashes declarados por la procedencia de las canónicas coinciden. La procedencia registra 493 inputs estables, seis guardas libres, calidad alta y DPR1.

Final: `7e5f2635ce48ddb7438ccf762952b1126fa926b39d5fe719ee62724e35c21503`.
R2: `037ea9f862ee10933d6769828fc0b7a567c2b739a6ffcf636138276fa0f24163`.
Base T16: `d70efcfa6f89273d53a7cb6ed4c6f3a24fe1659bb56227e8b2a60c7adeca838e`.

Los JSON de final y R2 son idénticos byte a byte: `a2606f95d3802b56e3a726c19611e5b0bc2779c94f48d5bd261e37120f82f6cd`. Por tanto las seis poses, objetivos y FOV coinciden. Frente a T16 sólo coincide 1481/vista1; las cinco restantes no permiten atribución causal estricta por imagen. El conjunto final cambia modelos, pertenencias, acabados y cortinas, no una sola variable. Las mismas luces declaradas no implican iluminación idéntica en píxeles.

Entrada final 1594: `87e3d3211e4742f9c9827b3941318d397d567a3ec39ea55497c1f482ed2e92df`. El JSON conserva punto físico, objetivo, FOV75, alta/DPR1 y las dos guardas libres de R2; su única diferencia es el ID del escritorio final. La procedencia de entrada ya está sellada (`c329ce453216a7da10500109136ab2f5021bf3ffbe2419e239c19e3ac69bc2d2`): registra 493 inputs estables y se han cotejado sus tres hashes de imagen/JSON/capturador sin discrepancias. El punto, objetivo, FOV, inicio y marco coinciden con R2. Esta entrada adicional no sustituye las seis canónicas.

## Resultado visible por habitación

**3244, artista.** La vista0 reúne biblioteca, bajo y puesto en un frente adulto comprensible. El monitor se distingue de las dos hojas de consulta y el tablero conserva una zona frontal despejada. Las baldas abiertas y el cajonero aportan volumen reconocible; el fondo verde separa la madera y la silla. El suelo calmado deja de competir con la actividad como ocurría en T16/R2. La cortina acaba por encima del respaldo sin una invasión visible del puesto. En vista1 siguen dominando un paño blanco y suelo vacíos: sólo aparece un fragmento de la mesa auxiliar de lectura; no se puede juzgar el conjunto completo del sillón desde esa toma ni inferir su eliminación. Este vacío continúa limitando la densidad percibida.

**1594, estudiante.** En vista0 se leen puesto, silla y transición baja sin que una masa alta corte el centro de trabajo. Vista1 explica almacenamiento y consulta, aunque recorta el escritorio por el encuadre. Desde la entrada fija, la biblioteca ocupa bastante primer plano, pero sus huecos, libros y carpetas sustituyen la envolvente ciega de R2. Se ven pantalla, lámina, tablero y silla; no hace falta volver a cambiar el orden de muebles ni ajustar la cámara para resolver esa lectura. El azul cálido/frío de pared y asiento diferencia el puesto de la madera, con un resultado doméstico sobrio. La pared opuesta blanca sigue muy vacía; no es un motivo para añadir miniaturas dispersas.

**1481, músico; fixture sintética.** La partitura del respaldo se reconoce y la cadena biblioteca–bajo–puesto se entiende en ambas vistas. El marrón separa mejor las hojas claras y el conjunto del muro que el jaspeado anterior, aunque madera, bajo y pared mantienen valores próximos. Tres cuadros idénticos en el paño blanco repiten una señal decorativa sin reforzar mucho la actividad musical. La cortina corta se lee como dos paños completos, sin cortes visibles ni fragmentos sueltos; su borde queda claramente por encima del alféizar y resulta más corto que una solución convencional. Es un remate a vigilar, pero no un defecto que exija recortar muebles o rediseñar la ventana según estas capturas.

## Incidencia visible: puntos blancos

Las dos vistas de 1481 muestran motas claras muy contrastadas sobre el paño marrón; algunas también se ven sobre el bajo. Hay puntos similares en el lateral de biblioteca de 3244/vista1, puerta/biblioteca/bajo de 1594/vista1 y la biblioteca de la entrada fija. Son perceptibles y rompen la limpieza de superficies lisas. No los atribuyo a z-fighting, textura ni pared desplazada sin diagnóstico: su presencia delante de materiales distintos hace plausible un efecto de partículas superpuesto, pero es sólo una hipótesis. No he tocado ni limpiado imágenes.

Si se confirma un efecto ambiental preexistente, documentar que el mayor contraste lo hace visible; eso no exige alterar arbitrariamente la paleta ni ocultarlo para una evaluación. Si procede de superficies nuevas o es un artefacto de render, corregir su causa antes del cierre. La composición puede conservarse en ambos casos.

## Lo que todavía limita el acabado

El programa funciona visualmente como un frente de estudio, pero las tres habitaciones comparten casi el mismo cajonero, silla y ritmo de baldas; las diferencias de perfil descansan bastante en hojas de consulta y algunos libros. En las grandes, los paños blancos y el centro amplio siguen pesando más que el programa secundario de lectura. Hay zonas de sombra granular en encuentros de muebles y paredes y cierta uniformidad cálida entre madera/suelo; las imágenes no permiten diagnosticar si es material, luz o render. Son límites observados, no una puntuación ni una promesa de alcanzar 4/5.

La mejora principal ya es material y amplia: escala del puesto, relación entre trabajo/guardado/consulta, biblioteca abierta y eliminación del suelo dominante. Recomiendo mantenerla y resolver primero el origen de las motas, sin iniciar otra tanda de adornos pequeños o cambios de cámara. Los callbacks T20 comunicados por raíz son evidencia técnica separada; no demuestran estética, uso vivo ni navegación por los píxeles aquí revisados.

Revisión estática de archivos existentes: sin GPU, navegador, API, edición de producto o evaluación formal.

## Adenda · causa de las motas resuelta

La pareja válida `diagnostico_motas_r2` elimina las motas al retirar únicamente la mezcla de pelusa del shader. La hipótesis de partículas superpuestas queda sustituida por pelusa procedimental de plastilina, sin evidencia de z-fighting. Véase `revision_diagnostico_motas_r2.md`: se recomienda preparar un define optativo sólo para acabados de estudio, con materiales propios y control de coste. El diagnóstico retiró lint también de muebles; el arreglo acotado conservará su textura y aún necesita código/captura propios. Se mantiene la recomendación de conservar composición/modelos, sin aprobar una corrección todavía no revisada.
