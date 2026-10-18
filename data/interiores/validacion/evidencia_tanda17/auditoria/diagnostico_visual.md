# Tanda 17 — diagnóstico privado de estudio y trofeos

**Recomiendo abordar primero estudio.** Su actividad principal queda subordinada a bibliotecas, sillón y suelo en las tres muestras, y la receta permite intervenir en esa relación de forma acotada. Trofeos conserva una identidad temática reconocible, aunque su mobiliario está disperso y el armero se lee mal. La prioridad procede de los defectos visibles y de la oportunidad de recomponer el uso, no de ordenar las medias históricas por unas décimas.

No se ha ejecutado evaluación formal nueva. Las cifras recibidas (trofeos A/B 3,034/3,222; estudio 3,086/3,066) son históricas, no una recertificación de estas fuentes. Se conserva la rúbrica doméstica de `data/interiors_review.json`: densidad sin vacíos/amontonamientos, coherencia doméstica, luz legible, variedad creíble y lectura de usos/paso; ninguna dimensión se redefine. Annie queda fuera: casa singular y evidencia histórica que necesitaría refrescarse antes de priorizarla por una cifra antigua.

## Evidencia leída

Dos fichas, doce vistas en total y sus JSON: estudio 3244/artista (5,6×3,5 m), 1594/estudiante (4,5×2,3 m), 1481/músico (4,3×3,6 m); trofeos 2132, 4204 y 1679, todos cazador/rústico, 4,4 m de ancho y 3,5–3,9 m de fondo. Son dimensiones redondeadas de ficha, no huellas útiles medidas. Todas registran alta/DPR1; sus JSON no contienen las guardas físicas recientes. No se certifica que las cámaras sean libres ni se compara causalmente con otra captura.

Se leyeron recetas activas, modelos fuente y entradas de catálogo, además de la selección de acabados. Ninguna casa se ha reconstruido ni medido en ejecución. Los catálogos confirman roles y formas, no que cada opcional haya aparecido en las imágenes.

## Estudio: tres problemas materiales

1. **El puesto no gobierna la estancia.** En 3244, un sillón amarillo muy dominante se sitúa visualmente delante del escritorio y deja el ordenador y la silla como elementos secundarios. En 1594/uso la cara lateral de la biblioteca tapa buena parte del puesto; conjunto permite verlo mejor. En 1481 el escritorio pequeño aparece aislado cerca de la puerta, mientras cómoda y estantería forman otro conjunto. Son problemas visibles de relación y cobertura, no colisiones demostradas.
2. **Mucho inventario, poca superficie de trabajo explicada.** La mesa real mide 0,95×0,45 m, altura 0,75; la receta pone un ordenador obligatorio y permite además adornos de `papeles`, que también incluye `vb_ordenador`, sobre mesa/cómoda/estantería (3–6 por soporte). Esa selección explica que puedan aparecer pantallas y grupos de libros en lugares ajenos al puesto. En 1594 se aprecia otra pantalla en la estantería. No afirmo una duplicación de botín: el problema aquí es lectura doméstica y jerarquía.
3. **La habitación parece una colección de muebles pegados a paredes.** La receta coloca biblioteca, cómoda y sillón de forma independiente del escritorio; una segunda biblioteca se habilita desde 16 m². En 3244 hay un centro enorme de suelo jaspeado y poco uso reconocible; 1481 repite biblioteca/cómoda/paño vacío. El suelo de alto contraste compite con muebles de madera clara. `acabados_vivienda.js` distingue despacho, pero no da a estudio el tratamiento específico de ese despacho; no debe suponerse que ambos ya comparten el mismo acabado.

## Primera propuesta: un puesto de trabajo con biblioteca vinculada y lectura secundaria

El cambio debe ser **de composición funcional**, con una zona principal de trabajo/consulta y una secundaria de lectura sólo cuando quepa. No añadir una tercera estantería ni convertir el estudio en despacho corporativo.

Esquema conceptual, no planta medida:

`guardado de consulta — mesa de trabajo — apoyo bajo`  
`                         silla / reserva frontal`  
`paso continuo hacia puerta y ventana — lectura secundaria opcional`

- Mantener mesa y silla como pareja obligatoria con acceso frontal. Estudiar una variante exclusiva de estudio de unos 1,20–1,35×0,55–0,60 m, a 0,75 m de alto, para las amplias; en 1594 conservar la de 0,95×0,45 si el aumento no admite todas las reservas. Estas medidas son propuesta, no fit comprobado. Pantalla/teclado en una franja posterior y una superficie frontal/lateral libre para leer o escribir; no cubrirla con libros verticales.
- Relacionar una biblioteca con el puesto por extremo y frente de uso, evitando que se coloque como pantalla delante del escritorio. Puede conservarse la biblioteca de 0,90 m de ancho si cabe; antes de sumar otra alta, estudiar sustituir la cómoda opcional por guardado bajo útil (aprox. 0,80–1,00 m de ancho y 0,30–0,35 de fondo). No agrandar ni recolocar muebles compartidos globalmente.
- Separar el sillón del frente del escritorio y vincularlo a lectura con apoyo bajo, sólo cuando exista un segundo ámbito alcanzable. En la estrecha 1594 no forzar un rincón de lectura por densidad; el programa de estudio completo tiene prioridad. Mantener roles/asientos y acceso, sin reducir reservas para hacer caber la composición.
- Diferenciar programas por perfil dentro de esa misma lógica: **estudiante**, ordenador y zona de apuntes; **artista**, consulta gráfica/bocetos sobre superficie libre, sin repetir el caballete del taller; **músico**, escritura/consulta de partituras junto al ordenador, sin introducir otro piano. La diferencia debe verse en organización de superficie y guardado, no sólo en el color del sillón o tres miniaturas distintas.
- Reducir el contraste del suelo sólo como apoyo al conjunto y en un cambio separado revisable. Un suelo más calmo no corrige el escritorio oculto. Conservar presupuesto de luces; no añadir iluminación para compensar una mala jerarquía de modelos.

### Condiciones geométricas y criterios de aceptación

Primero preparar plantas privadas con geometría útil real de las tres casas, puertas/ventanas y reservas; la envolvente de ficha no basta. Probar el conjunto completo antes de comprometer piezas y conservar fallback completo si no cabe, semillas, índices/dependencias, RNG y funciones. La solución debe usar las relaciones existentes si bastan, sin abrir otro solver general.

La futura evidencia debería mostrar el tablero y la silla como un puesto reconocible, biblioteca accesible relacionada sin taparlo, y un paso continuo de 0,80 m probado técnicamente. Debe quedar superficie útil frente a pantalla/material, no una mesa mayor con la misma saturación. En 3244 la lectura secundaria no debe volver a ocultar trabajo; en 1594 no se acepta mejora de cámara que deje intacta una disposición que tapa el puesto desde el acceso; en 1481 biblioteca y trabajo deben pertenecer al mismo ámbito sin invadir puerta/ventana. Para la función se necesitan contratos reales, no píxeles.

La selección decorativa debe distinguir pantalla funcional del grupo de enseres, sin eliminar inventario/roles ajenos ni bajar el mínimo de catálogo: ambos kits son `otra_estancia`, cuyo mínimo doméstico actual es 30 tipos. No inflar listas con objetos que no puedan apoyarse. Los modelos exclusivos deben conservar superficies, acciones/asientos y coste; el paso de cámara por sí solo no prueba uso de la silla.

## Trofeos: diagnóstico y propuesta posterior

La pared de cornamentas identifica el cuarto, pero las tres casas repiten casi la misma combinación de orejero, librería muy llena, cómoda y trofeos. En 2132 el armero queda visualmente detrás del sillón; en 1679 aparece como un pequeño estante vacío. En 4204 el gran paño de trofeos está separado de biblioteca/sillón. Suelo rojo de juntas claras y paredes estampadas dominan el espacio libre. Añadir más cornamentas o cajas aumentaría la repetición.

La receta confirma la causa probable: armero y rifle se colocan por reglas de pared independientes; el rifle es botín condicional, por lo que un soporte vacío no demuestra un fallo. Sillón, librería y cómoda también se colocan por separado. El armero fuente es un soporte estrecho de 0,55×0,23 m y 1,25 m de alto, sin una envolvente que lo haga inequívoco como armario. Las cornamentas comparten modelo y se piden 2–4; no existe una composición de exposición sobre un soporte común.

Propuesta posterior: **un frente de colección y equipo más un rincón de lectura**, no una armería comercial. Vincular cómoda/guardado bajo con 2–3 trofeos dispuestos sobre ese frente y conservar armero contiguo como volumen legible; disponer el sillón frente o junto a ese conjunto con apoyo de consulta, lejos del acceso al armero. Estudiar un aparador específico de aproximadamente 1,10–1,30×0,35–0,40 m, alto 0,75–0,90 m, en sustitución de cómoda y parte del inventario expuesto, no como mueble adicional obligatorio. El lateral de equipo puede reutilizar la huella del armero con un modelo doméstico más claro. Son dimensiones a ensayar, no soluciones verificadas.

Rifle y prismáticos deben conservar identidad de botín, desaparición y persistencia: nunca rellenar visualmente el soporte con duplicados para ocultar que el botín falta o fue recogido. Una ausencia legítima debe seguir resultando coherente. Mantener el asiento utilizable, el acceso al guardado y puertas libres. Variación posible por composición —colección centrada sobre aparador o frente lateral con lectura— condicionada al recinto, no más armas ni trofeos de mayor escala por semilla.

Criterios: leer conjuntamente colección/equipo/descanso; armero identificable con y sin botín; al menos un ámbito útil en el vacío actual sin ocupar circulación; trofeos a escala y relacionados con muebles bajos; no perder claridad por madera oscura o cortinas. Si las cámaras actuales no muestran armero y trofeos juntos, registrar la cobertura faltante; no mover muebles sólo para la foto.

## Alcance, orden y límites

1. Estudio: propuesta geométrica privada sobre las tres casas; núcleo de trabajo/consulta primero. Todavía no iniciar implementación.
2. Trofeos: conservar este diagnóstico para después; su cambio depende especialmente de funciones y botín, además de composición.
3. Annie: ninguna decisión de diseño en esta tanda sin evidencia singular actualizada.

No se han puntuado imágenes ni llamado a API; no se han ejecutado GPU, navegador o build, ni editado activos o publicado. El presente documento no da por implementada ninguna propuesta ni promete alcanzar el umbral. Las fichas antiguas no incorporan las guardas nuevas: antes de comparar una futura candidata habrá que preservar una base actual con cobertura/poses documentadas. La apariencia cambiante por cámara se separará del efecto de producto, manteniendo la rúbrica intacta.

## Fuentes y SHA256

- `data/interiores/fichas/casa_estudio.jpg`: `8e6b5e276ce0980af26a091f8388f48fb2e3fe20a3460d4980c992a6f0d61e9b`.
- `data/interiores/fichas/casa_estudio.json`: `a24ff13c45cc59b943ad012c952c6e351208612b252e5e555f88470411c55071`.
- `data/interiores/fichas/casa_trofeos.jpg`: `8987ee2a6b9d2ba0e697ae7aed2fb55ac1c6c65e2a8c9d54a6fcdfd7a734a14d`.
- `data/interiores/fichas/casa_trofeos.json`: `d4ed0d20f416b23c8b05f3a49aff46ef2534947bf6df3ba2cab1deb2b488f880`.
- `data/interiors_review.json`: `a6b789ace3ff0d48c9ca7961d1603e12c174a5002c6c831bb1565442c6d26141`.
- `tools/interiores/kits_vivienda_b.py`: `486141fa1c52bb22a71c92c5a08a81047562e6bad04495d8a85d4a5a1517a551`.
- `tools/interiores/catalogo_vivienda_b.py`: `59410aeb5fe499213ab19ff528acc131aae08aa3e582d0cd76f88a6ea93e9f70`.
- `tools/interiores/catalogo_vivienda.py`: `364598f631afe2178e5b70a84a7687a428bd886ab236efbdbee9ac580a7c99ab`.
- `tools/interiores/vivienda_base.py`: `e0f129803d087aa3d9aafa96c77e0c4b27b2682afc819063335d5bff4185d4b8`.
- `data/kits/vivienda_estudio.json`: `758fc3ae8bc7e1491f86d98538f079e25542fa98dc5863970da624003b56a049`.
- `data/kits/vivienda_trofeos.json`: `e6e18eefd473c35326ece26cb0dd5f69927fa8d4c7bca34c6aef4e8b0580e9a3`.
- `src/acabados_vivienda.js`: `5c65b324b83ffed145793b01bb5635b85b31f6b71c232f32879f42f48adc71e9`.

## Apéndice — base actual T16 de estudio y criterios para el greybox

Revisada la nueva ficha privada `.cache/calidad/tanda17/captura_base_T16/casa_estudio.jpg`. **Confirma el diseño propuesto; no cambia la prioridad ni justifica abrir otra línea de intervención.** Se conserva íntegro el diagnóstico anterior (hash previo `606bfc17f7ac2cb90d822920368f6e3594127e47a23745b894215ffed6e36647`). La mejora de evidencia es que ahora las seis vistas tienen guardas físicas libres: los problemas de lectura observados persisten en cámaras libres, y no se pueden descartar como simples cámaras dentro de muebles.

No obstante, cámara libre no demuestra uso, recorrido ni que todos los muebles queden visibles. Se comprobó que las seis posiciones, objetivos y FOV coinciden con la ficha histórica; no se atribuye ninguna mejora a esta recaptura ni se afirma iluminación idéntica en píxeles.

### Criterios concretos contra el resultado actual

- **3244/artista:** el puesto debe adquirir suficiente superficie y presencia para ser la función principal, sin que el sillón amarillo quede como pantalla delante del ordenador/silla. La segunda biblioteca y el centro vacío no se resuelven aumentando libros: plantear consulta/bocetos y lectura como dos ámbitos relacionados y alcanzables, con el sillón subordinado. La propuesta debe explicar qué sustituye o reagrupa, no sólo qué añade.
- **1594/estudiante:** conservar un estudio completo en el recinto estrecho. No aceptar una gran mesa que sólo cabe quitando reserva frontal o paso. La biblioteca debe servir al puesto, con frente accesible y sin su lateral dominante tapando la zona de trabajo como en la vista de uso actual. La mejora deberá existir en la planta y en los accesos, no sólo al escoger otro ángulo. No forzar sillón secundario ni convertirlo en un cuarto infantil sin cama.
- **1481/músico:** vincular la superficie de consulta/escritura con los libros y partituras, manteniendo la puerta y ventana útiles. El escritorio pequeño junto a la entrada y el conjunto biblioteca/cómoda separado no deben seguir pareciendo muebles sin relación. No replicar la sala de música mediante otro instrumento ni ocultar el puesto tras almacenaje.
- **Escala y superficie útil:** la mesa actual parece pequeña frente a los muebles altos y queda poblada de enseres. La candidata tiene que demostrar una zona despejada para leer/escribir además del ordenador, sin agrandar todo el mobiliario ni usar la cantidad de objetos como criterio de densidad. Revisar contenidos y soportes para que pantallas y grandes grupos de libros no compitan con la tarea.
- **Suelo y contraste:** el jaspeado marrón de alta frecuencia domina las tres casas, especialmente el centro de 3244. Un suelo más calmo puede ayudar, pero debe acompañar una composición ya resuelta; separar ese cambio en la evidencia para no confundirlo con la solución del puesto. No uniformar paredes y muebles en el mismo tono ni recurrir a luces nuevas para compensar falta de separación.
- **Identidad de estudio:** lectura, consulta y trabajo personal deben gobernar el conjunto. No copiar la mesa de despacho con accesorios integrados y estética de oficina, ni repetir banco/alfombra/biblioteca de niños con otra paleta. Los perfiles deben diferenciar la organización del trabajo y guardado (bocetos, apuntes, partituras), conservando una escala adulta y doméstica. No implica fabricar tres familias completas de muebles ni tres listas de adornos.

El futuro greybox debería entregar para cada semilla huellas útiles reales, entrada/huecos, frente de silla y recorrido hacia biblioteca, con comparación antes/propuesta. Si sólo cambia color, se amplía una mesa sin resolver su relación o se agregan objetos, no cumple el objetivo de composición. Si no cabe el conjunto completo, conservar el fallback definido; la integridad de acciones, RNG, índices y dependencias corresponde a revisión técnica independiente. Este apéndice no aprueba ninguna propuesta aún no recibida ni inicia implementación.

### Trazabilidad de la base nueva

Ficha SHA256 `d70efcfa6f89273d53a7cb6ed4c6f3a24fe1659bb56227e8b2a60c7adeca838e`; JSON `e3550493ebe8d5730bf39d0d8106d5ba703951f8dc8b8461f07e1306f11c29e9`; procedencia `e699b9529fb0625fc1e8dc3b89c222efd9cae676ff1edcb0d4c2a154977f4e7e`. Todos los hashes de archivos declarados coinciden. Verificados alta/DPR1, seis poses iguales a la histórica y seis guardas finales libres. La procedencia registra 415 fuentes estables; no se ha repetido esa auditoría de fuentes. Sin GPU, navegador, API, build, puntuación ni cambios activos.
