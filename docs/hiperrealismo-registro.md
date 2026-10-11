# Registro del hiperrealismo: comentarios, revisiones y arreglos

Cada entrada lleva fecha, quién habla (el usuario, el revisor o el que construye), qué se vio y qué se hizo, con su
motivo. Se lee antes de empezar cada paso y se escribe al acabarlo. Lo que se aprende aquí vale para la próxima pieza.

## 2026-10-11 · arranque

- **Usuario:** pide la zona de la iglesia hiperrealista para probar cómo queda, con el método de la guía de
  Opus + Blender: diseño primero, agentes, revisor que aprueba, greybox y capas, y cada arreglo apuntado. Elige el
  navegador con Blender, no Unity.
- **Preparación:**
  - Blender 5.2.2 LTS instalado, comprobando su SHA-256 oficial y la firma notarizada de la Blender Foundation;
  - 30 texturas CC0 de Poly Haven a 2K (64 MB) en `.cache/polyhaven`, con permiso del usuario.
- **Referencias reunidas:**
  - la foto de Commons desde el noroeste;
  - la planta del Catastro y la ortofoto del PNOA (solo para medir);
  - los estudios de los Coloquios Históricos, Wikipedia y el BOE.
- **Aprendido de las referencias** (el modelo antiguo estaba mal en esto):
  - la nave mide 22,5 m hasta la cornisa y la torre pasa de 37 a 40 m;
  - el eje de la nave está 2,4 m al norte del centro del rectángulo del Catastro, porque la sacristía tuerce el
    rectángulo;
  - los costados son muros lisos con contrafuertes planos, sin capillas que sobresalgan;
  - el campanario sale de la fachada de los pies en la esquina suroeste;
  - la cubierta no se ve desde la calle.

## 2026-10-11 · greybox (el que construye)

- **Hecho:**
  - `tools/blender/iglesia.py --greybox` da 32 piezas y 825 triángulos (69 KB);
  - `src/hiper.js` lo carga en el marco de la iglesia, en Realista; los 86 volúmenes antiguos se esconden y quedan las
    tres portadas;
  - la puerta de los pies sigue llevando dentro;
  - sin errores.
- **Primer intento y lo que falló:**
  - La vista «noroeste» estaba puesta a ojo y daba contra la pared de una casa. Una vista de referencia se calcula, no se
    adivina.
  - Se reconstruyó la cámara de la foto con sus puntos de fuga y seis puntos del Catastro. Ahora el juego enseña la
    misma esquina, los mismos tramos y la misma casa de balcones al borde derecho que la foto.
- **Medido, y corregido en la tabla del diseño:**
  - **Contrafuertes:** el greybox tenía cuatro tramos iguales de 10,7 m. La ortofoto da un ritmo de 8,4 m a los dos
    lados y la foto lo sitúa en x −11,4, −3,0 y 5,4. Los tramos quedan de 9,3, 8,4, 8,4 y 11,3 m: el último, junto al
    ábside, es más largo.
  - **Óculos:** el grande va a 10 m (no a 14) y hay otro pequeño bajo la cornisa, a 19,5 m.
  - **Torre:** el campanario sube hasta 32 m (no 30,5) y el cuerpo alto, hasta 36 m.
  - **El noroeste:** no hay un cuerpo bajo. Es un retranqueo de 2,3 m de la cara norte, y el torreón está sobre la
    esquina.
  - **Cubierta y ábside:** la cubierta va solo sobre la nave (18 m, a 20°, cumbrera a 25,8 m), con las capillas
    planas alrededor. El lado sur del ábside, tapado por la sacristía en el Catastro, se dibuja en espejo del norte.
- **Aprendido** (vale para la próxima pieza):
  - **El PNOA no es una ortofoto verdadera.** A la altura de la cornisa, la iglesia aparece 7 m corrida hacia el
    suroeste, y la torre, el doble. De la ortofoto solo valen las distancias entre cosas de la misma altura; la planta
    se mide en el Catastro.
  - **Las alturas de una sola foto dependen de la que se fije.** Con la cornisa en 22,5 m, el resto cuadra con un error
    de 10 a 25 px de 1920. Lo lejano se desvía más.
- **Queda para el revisor:**
  - en la foto, el extremo este del muro norte aparece unos 60 px más bajo que en el juego;
  - la portada real está 2–3 m al sur del óculo y es más baja. Es la portada antigua del juego: se cambia en la fase 2.

## 2026-10-11 · revisión del greybox (el revisor): NO APROBADO

Midió la foto de Commons a 1920 px, pasada a las capturas de 1440 × 960. Las alturas las tomó por razón doble en la
vertical de cada rasgo, con el suelo y la cornisa de 22,5 m como referencias, para no depender de la cámara.

**Bloquea:**
1. **El cuerpo bajo de la torre.** Sigue el punto 0 del Catastro, una cara oeste torcida 8,8°. Así, el campanario queda
   volado hasta 0,93 m sobre el vacío. La foto da la razón a la tabla: la cara es recta, en x −26,34. Por ejemplo, el
   ancho de la fachada a media altura es ≈363 px en la foto, ≈357 con el rectángulo y ≈329 con el Catastro.
2. **La torre por encima de la cornisa es demasiado maciza.**
   - El cuerpo alto mide ≈2,3–2,6 m de lado, no 3,8, y le falta su arco por cara.
   - El remate es un pedestal esbelto con pirámide, de ≈3 m en total, con bola, cruz y veleta.
   - El campanario mide ≈5,5 m de lado, está retirado ≈1,5 m de la fachada y tiene la cornisa a ≈31,4 m.
   - Sus arcos miden ≈3 m de alto, no 5.
   - La altura hasta la cruz está bien.
3. **Los ventanales.** El alféizar va a ≈14,5 m (no 13,5) y el hueco mide ≈3,8 m hasta la clave, a 18,3 m. Los 13,5 y
   4,2 m de la tabla incluían el relieve y el recercado.
4. **La vista de referencia no cuadra tanto como decía el registro.**
   - El EXIF de la foto dice Canon EOS 600D (APS-C) a 18 mm, sin recortar: 45° de campo vertical, no 43°.
   - El error crece hacia el extremo este de la cornisa norte: 65 px de 1440.
   - Pide rehacer la cámara con esa focal y una distorsión radial, con más puntos de ajuste.

**No bloquea:**

5. **Contrafuertes.** El ritmo de 8,4 m está bien, pero la ortofoto corregida y la foto los ponen ≈0,7 m más al oeste:
   −12,3, −3,6 y 4,8. Hay un cuarto rasgo en x ≈13,4–14 y una banda de sillería de ≈3 m en el extremo noreste. Además,
   el vuelo de 1 m es dudoso: la cornisa pasa recta por encima. Los remates de teja están ≈1 m detrás de la cornisa:
   son las cabezas de los muros entre capillas (los «⌐» de la ortofoto).
6. **Torreón.** Mide ≈2 m de lado, está retirado 0,5–1 m de la esquina y lleva remate curvo con pináculos.
7. **Portada de los pies.** El frontón de la portada antigua se mete en el óculo grande, que ahora está a 10 m.
8. **Cubierta al oeste.** No se puede decidir con estas referencias.
9. **Menudencias:**
   - los óculos quedan 2–14 cm por delante de la fachada;
   - el torreón sobresale 0,12 m de la cara oeste;
   - el muro sur se desvía 1,67°, no 1°.
10. **La otra foto de Commons** («Guareña_iglesia.jpg») es un interior.

**Bien:**
- la planta, la esquina noroeste con su retranqueo y los dos óculos (10,1 y ≈20 m);
- los ventanales en horizontal (a menos de 7 px);
- la altura total de la torre;
- la cubierta oculta;
- la geometría limpia.

**Lo que aprendo para la próxima pieza:**
- **La focal se lee del EXIF.** Antes de calcular la cámara de una foto, se mira su EXIF: la focal deja de ser una
  incógnita.
- **Medir alturas por razón doble.** Las alturas se miden en la vertical de cada rasgo, contra el suelo y una altura
  conocida, por razón doble. Así no dependen del error de la cámara.

## 2026-10-11 · arreglos del greybox (el que construye)

- **Cámara de la foto, rehecha.** Focal del EXIF (45°), barril −0,03 y quince puntos: las claves y los alféizares de
  los cuatro ventanales, medidos de nuevo, con su altura como incógnita. Con el ojo a 1,6 m, los ventanales salen donde
  están en el modelo. Error ≈14 px de 1920.
- **Torre.**
  - La cara oeste del cuerpo bajo, recta (x −26,34).
  - Campanario: 5,7 m de lado, centrado en (−22,6; 9,6), cornisa a 31,45.
  - Cuerpo alto: 2,4 m de lado, con su arco.
  - Pedestal y pirámide esbeltos.
  - Medido ajustando a las esquinas de la foto: rms 2,9 px.
- **Ventanales.** Alféizar a 14,6 m, luz de 3,8 m.
- **Contrafuertes.** Bandas planas de 2 m en x −11,1, −2,35, 6,1 y 14,9, con las cabezas de los muros entre capillas un
  metro detrás de la cornisa.
  - Con la cámara nueva, los remates de la foto y una banda plana medida entre los ventanales 2 y 3 caen ahí.
  - Así los cuatro ventanales quedan centrados en sus tramos.
- **Torreón y óculos.** Torreón de 2 m, retirado 0,6 m; óculos sobre la fachada central.

## 2026-10-11 · segunda revisión del greybox (el revisor): APROBADO CON ARREGLOS MENORES

- **Coincidencias con la foto** (en px de 1440):
  - esquinas del campanario a 4–14 px y del cuerpo alto a 3–8;
  - ventanales 2–4 a 1–4 px;
  - remates a 2–8 px y óculos a 6–9 px;
  - la esquina noroeste, de arriba abajo, a ≈3 px;
  - la casa de balcones, en su sitio.
- **Ortofoto.** Con una corrección de −5,7 m en x, los cuatro rasgos de cada lado caen en −11,1, −2,4, 6,0 y 14,6, como
  el modelo.
- **El revisor se corrige.** En la primera revisión se fió de la marca «esquina NO (suelo)», que estaba mal puesta:
  - el error de 18–23 px en ese pie no existía;
  - el argumento del ancho de la fachada a favor de la cara recta de la torre no vale.

  La foto pone esa cara en x ≈ −25,6 ± 0,4: no decide entre el Catastro (−25,2) y el rectángulo (−26,34). Se mantiene
  el rectángulo, porque la torre es cuadrada y nada vuela, pero no porque lo diga la foto.
- **Arreglos menores, hechos en el paso siguiente:**
  1. Dos marcas mal puestas:
     - «esquina NO (suelo)» está en ≈(1304, 1200), no en (1203, 1195);
     - «fachada O, extremo S» está en ≈(1683, 800).
     La primera entraba en el ajuste de la cámara.
  2. Las cabezas del lado sur se metían en la cubierta: deben acabar en |z| = 9.
  3. Los primeros planos «fachada» (con la cámara dentro de la casa de enfrente) y «ventana» (cortado) no servían.
  4. El documento: el desplazamiento de la ortofoto (−5,7 en x), los fps y la puerta con esta versión.
  5. Menores:
     - el ventanal 1 está ≈0,35–0,55 m más alto en la foto;
     - la foto pone la punta de la cruz a ≈41,5 m;
     - los extremos del retranqueo noroeste caen a 15–21 px (fase 2);
     - las cabezas parecen más gruesas, de 1,1–1,5 m (fase 2);
     - la portada antigua sigue metida en el óculo (fase 2).
- **Lo que aprendo:**
  - **Una marca mal puesta engaña a todos.** Una sola marca de la foto mal puesta engañó al ajuste de la cámara y al
    revisor. Cada marca se comprueba sobre la foto ampliada antes de usarla, y las de los pies de las esquinas, con
    especial cuidado: los coches las tapan.
  - **Si la foto no decide, se dice.** Donde la foto no decide, se escribe así y se decide por otra razón, también
    escrita (aquí, que la torre es cuadrada).

## 2026-10-11 · arreglos menores, y detalle, materiales y luz (el que construye)

**Arreglos menores del greybox**
- **Marcas.** Las dos marcas corregidas, comprobadas sobre la foto ampliada: el pie de la esquina noroeste en
  (1304, 1200) y el borde suroeste a media altura en ≈1680.
- **Cámara.** Se queda como estaba: ya pone ese pie donde está.
  - Un reajuste con la marca buena cambia el giro y empeora otros puntos dentro del error.
  - Con el ojo libre, la cámara se iría 2 m bajo el suelo, y la foto no enseña ningún muro de contención.
- **Cabezas del sur.** Acaban en |z| = 9 y son de 1,2 m.
- **Ventanal 1.** Sube a 15,1.
- **Cruz.** A 41,5 m, como da la foto (±1 m). Los 40 m no tenían fuente.
- **Primeros planos.** La fachada se ve desde su calle (6 m de ancho; el mapa dice dónde empiezan las casas) y el
  ventanal, entero.
- **Comprobado con esta versión:** 60 fps, la puerta de los pies lleva dentro, las campanas voltean y los contrafuertes
  paran al jugador.

**Me corrijo: la portada no está desplazada.**
- Con la cámara rehecha, el umbral de la portada sale en el eje (z ≈ −0,3), bajo el óculo (z 0,15).
- Lo de «2–3 m más al sur» salía de tomar el umbral y el vértice del frontón en la misma columna de la foto: con la
  cámara inclinada, la vertical de la portada no es una columna de píxeles.
- El frontón llega a ≈7,0 m y la portada del juego llegaba a 8,25. Se reduce al 85 %, con sus colisiones y el bolsillo
  de su puerta en el modelo, y ya no se mete en el óculo.

**Detalle, materiales y luz, en `tools/blender/iglesia.py` sin `--greybox`:**
- **Huecos:** las booleanas cortan los ventanales, los óculos, la saetera y el bolsillo de cada puerta con el cuarto de
  su vestíbulo. Así se ven dentro el derrame, las hojas y el vestíbulo de `churchdoors.js`, que antes quedaban tapados
  por el muro macizo.
- **Ventanales:** recercado, alféizar, relieve, vidrio y barras.
- **Óculos:** el grande con cuatro anillos y rueda de 16 radios con lóbulos; el pequeño con dos anillos.
- **Muros:** cornisa moldurada y zócalo recorridos sobre la planta; sillares alternos en las esquinas.
- **Contrafuertes:** bandas con su zócalo, y las cabezas con albardilla y remate de teja.
- **Detalles de la fachada:** gárgolas de cañón y los canecillos y la saetera de la torre, medidos en la foto.
- **Torre:** campanario y cuerpo alto huecos, con arcos de verdad, pilastras, imposta, cornisa y bolas, y tres
  campanas; pedestal, pirámide, bola, cruz y veleta; dos nidos.
- **Torreón, cubierta y sacristía:** torreón con caperuza y bolas; cubierta con cumbrera; sacristía con su zócalo y su
  cornisa.
- **Materiales:** de `tools/blender/texturas.py`.
  - La mampostería es propia, con la cara de una piedra real en cada piedra y las juntas hundidas.
  - La primera, con piedras pequeñas y planas, parecía confeti. La foto, con su cámara, da piedras de 30–70 cm.
- **Luz:** la oclusión ambiental, cocida en Cycles (≈10 s).
- **En cifras:** 10 mallas (una por material), 9.725 caras, 6,5 MB con las texturas dentro, 60 fps.
- **Lo que aprendo:**
  - **La vertical en una foto inclinada no es una columna de píxeles.** Para situar algo en una foto, se toma un solo
    punto y se proyecta con la cámara, no dos puntos de la misma columna.

## 2026-10-11 · revisión de las fases 2, 3 y 4 (el revisor): NO APROBADO

Midió la foto a 1920 px, con estadísticas de luminosidad leídas en el navegador, y las capturas a 1440 px con la cámara
del documento. Le parecen bien la estructura (huecos de verdad, cornisa, zócalo, esquinales, bandas, cabezas) y la
torre, «muy parecida a la foto». Mis arreglos menores están hechos.

**Bloquea:**
1. **La mampostería no es la de la foto.**
   - En la foto, el grueso del muro son piedras doradas de 20–70 cm, de un tono casi igual al del mortero.
   - Las oscuras, de 10–45 cm, son pocas: 11–13 % en el muro en sombra y 3–5 % en la fachada al sol.
   - La mía tiene un 40–50 % de piedra oscura y un mortero caqui: se lee como un camuflaje oscuro, no dorado.
2. **La repetición se nota.** Los mismos grupos de piedras aparecen a los dos lados de un ventanal, a 4 m. La mancha de
   color no cambia la forma.
3. **La cornisa queda alta y tapa los remates.**
   - Su borde, que vuela 0,52 m, queda ≈0,5 m por encima de la línea de la foto, con la que el greybox coincidía.
   - Los remates de las cabezas no asoman desde el punto de la foto; en ella asoman claramente.
4. **El relleno del óculo grande es inventado.** La foto enseña, dentro de las molduras, un anillo de bolas y una reja
   de barrotes verticales finos («celosía»), no una rueda gótica.
5. **El remate del torreón** no es una caperuza con bolas: son frontones curvos de piedra en cada cara y pináculos en
   las esquinas, como dice la tabla.

**No bloquea:**

6. **Gárgolas.** Hay unas 8 en el muro norte, también en los contrafuertes.
7. **Faltan detalles:**
   - cuatro ventanitas en la cara norte del bloque de los pies;
   - tres saeteras junto a la esquina noroeste;
   - el escalón del retranqueo y el final del muro norte, de sillería entera;
   - la banda de sillería de la esquina noroeste, de ≈2 m.
8. **Ventanales.** Bajo el alféizar, una cartela tallada. En la luz, un parteluz de piedra con dos arquillos y tracería,
   no barras.
9. **Sillería.** Los borrones del escaneo cruzan las juntas. La foto enseña un dorado parejo, que varía de un sillar a
   otro.
10. **Luz.**
    - En la foto, la fachada al sol es ≈3,4 veces más clara que el muro en sombra.
    - El EXIF dice las 18:31 del 3-12-2019, pero ese día el sol se pone hacia las 18:00 y en la foto hay sol directo: el
      reloj de la cámara iba adelantado ≈1 h. El sol estaba a ≈4° de altura, con rumbo ≈237°.
    - Hay que comparar con el sol ahí, y después de arreglar la piedra.
    - Bien: la oclusión, las sombras nítidas y sin brillos de plástico.
11. **Portada antigua.** El frontón es de dos losas; en la foto es triangular cerrado, con escudo y tres pináculos.
    Queda fuera del modelo.
12. **Documento.** Unificar los tamaños de piedra: las oscuras miden 10–45 cm y las doradas, 20–70 cm.
13. **Menores:**
    - la teja, demasiado naranja;
    - la cabecera, sin esquinales (no hay foto);
    - una banda oscura en la torre, que es la sombra del cuerpo alto.

## 2026-10-11 · arreglos de las fases 2–4 (el que construye)

**Bloqueantes**
1. **Mampostería, rehecha como la foto.**
   - La masa son piedras doradas de 20–70 cm, casi del tono del mortero: un ocre más saturado, no caqui. Cada piedra
     lleva su trozo de piedra real y las juntas son finas, apenas más oscuras.
   - Las piedras oscuras son celdas angulosas de un diagrama más fino, de 10–45 cm, sueltas: un 13,1 % del muro, medido.
   - Antes las hice con lóbulos y parecían estrellas: una piedra de verdad es un polígono.
2. **Repetición.** La textura pasa de 4 a 6 m (3072 px) y la mancha del mundo sigue encima.
3. **Cornisa y remates.**
   - La cornisa baja a 22,05 m y vuela 0,45: su arista cae donde la línea de la foto.
   - Las cabezas empiezan a 0,7 m de la fachada y sus remates de teja asoman sobre la cornisa desde el punto de la foto,
     junto a las marcas «remate».
4. **Óculo grande.** Lleva cuatro anillos, un anillo de 30 bolas dentro y una celosía de barrotes verticales finos,
   como en la foto, en lugar de la rueda inventada.
5. **Torreón.** Su cuerpo y su cornisa llegan a 23,75; encima, un frontón curvo con moldura en cada cara y un pináculo
   con bola en cada esquina, hasta ≈24,9.

**No bloqueantes, hechos**
- **Gárgolas** también en los contrafuertes: 7 por lado.
- **Bloque noroeste**, medido con la cámara: sus cuatro saeteras (la foto enseña cuatro, en una columna) y sus cuatro
  ventanitas. Va vestido de sillería en una banda de 2 m en la esquina de la fachada, en el escalón del retranqueo y en
  el final del muro norte.
- **Ventanales.** Parteluz de piedra, dos arquillos y un óculo calado bajo el arco; cartela tallada, con marco y óvalo,
  bajo el alféizar.
- **Sillería** sin las manchas anchas del escaneo; **teja** más parda.
- **El sol de la foto.**
  - Para la vista de la foto: rumbo 237°, pero a 9°, porque el juego atenúa el sol por debajo de 9°.
  - El contraste sol/sombra del juego sigue siendo menor que el de la foto: es la luz de todo el pueblo, que aclara las
    sombras con el cielo y un rebote. Queda apuntado para que lo decida el usuario.
- **Comprobado:** 60 fps, sin errores, la puerta lleva dentro, las campanas voltean y los contrafuertes paran al jugador.

## 2026-10-11 · segunda revisión de las fases 2–4 (el revisor): APROBADO CON ARREGLOS MENORES

- **Coincidencias con la foto:**
  - la vista de la foto ya se parece de verdad: la piedra dorada con piedras oscuras sueltas, sin repetición visible;
  - la arista de la cornisa, en la línea de la foto;
  - los tres remates, junto a sus marcas;
  - el óculo con sus bolas y su reja;
  - las ventanitas y las saeteras del bloque noroeste, en su sitio.
- **Luz.** Aceptable dentro de la luz del juego:
  - oclusión, sombras nítidas, sin brillos;
  - el sol a 9° es un buen apaño;
  - el contraste sol/sombra queda como decisión del usuario.
- **Arreglos menores, para hacer antes de enseñarlo:**
  1. **Torreón:** su coronación se queda ≈1,3 m corta. La foto pone el vértice del frontón y la punta de los
     pináculos a ≈26,2 m, así que los frontones van peraltados, de ≈1,5 m, y los pináculos de ≈1,9 m.
  2. **Fachada de los pies:** demasiada piedra oscura. La foto da un 3–5 % al sol: una variante con ≈4 %.
  3. **Piedras oscuras:** casi negras. En la foto, en sombra, valen ≈0,55 del mortero, no ≈0,3.
  4. **Gárgolas:** altas y negras. En la foto cuelgan ≈2 m bajo el borde de la cornisa, a ≈19,5–20 m.
  5. **Documento:** pequeñas incoherencias (las cabezas a 0,7 m, la textura de 6 m, la cumbrera a ≈25,3 m, 7 gárgolas
     por lado).
- **Pendiente, fuera del modelo:** la portada antigua, con su frontón de dos losas.

## 2026-10-11 · el usuario

- Pregunta qué necesito y qué decisiones quedan para jugarlo y probarlo. Decide:
  - **Publicar:** sí, en GitHub Pages (Guareña HQ), después de los retoques del revisor.
  - **La luz:** dejarla como está. No se endurece el contraste sol/sombra en todo el juego, porque cambiaría los
    atardeceres de todo el pueblo.
  - **Después de probarlo:** los alrededores (fase 5).

## 2026-10-11 · los retoques, antes de publicar (el que construye)

1. **Torreón.** Con la cámara, el vértice del frontón y la punta del pináculo de la foto están a 26,2 m. Los frontones
   son ahora de medio punto peraltados, de 1,5 m de ancho, y los pináculos llevan pedestal, obelisco y bola, hasta
   26,2 m. En la vista de la foto llegan a sus marcas.
2. **Fachada de los pies.** Lleva su propia variante de la mampostería: la misma masa dorada, con un 3,5 % de piedra
   oscura (las oscuras son una parte de las del resto).
3. **Piedras oscuras.** Pardo grisáceas (0,085–0,19 en lineal), no negras.
4. **Gárgolas.** No van sobre ventanales y contrafuertes, como puse. En la foto van cada ≈4,8 m: las dos más cercanas,
   en x −19,1 y −14,3. Ahora son ocho por lado, a ≈19,5 m, y caen en sus marcas («gárgola 1» y «gárgola 2»). Las de
   antes salían negras porque estaban metidas bajo la cornisa, en su sombra y en su oclusión.
5. **Documento** al día.

**Además, dos fallos míos, encontrados por el camino:**
- **Escala de la mampostería.** La textura se hizo para 6 m, pero el modelo aún la ponía a 4 m: las piedras salían a
  dos tercios de su tamaño. Ahora va a 6 m.
- **Fachada de los pies en negro.** Al darle su material, la pinté entera de negro. Las booleanas ya habían añadido el
  material «hueco» como segunda ranura del muro, y yo asigné «la ranura 1» a ciegas. Se arregla con el índice del
  material recién añadido.

**Lo que aprendo:**
- **Las ranuras de material se buscan por su nombre.** Las booleanas añaden materiales a una malla: un número fijo no
  vale.
- **La escala de una textura tiene una sola fuente.** Cuando cambia el tamaño real de una textura, se cambia en el sitio
  que la genera y en el que la aplica a la vez. Mejor aún: que el modelo lo lea de un único sitio.
