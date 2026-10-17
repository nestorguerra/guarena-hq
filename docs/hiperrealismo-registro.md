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

## 2026-10-11 · el usuario: la iglesia también en Unity

- Vuelve a pegar la guía y pregunta qué hay que hacer ahora con Blender y Unity. Decide:
  - **Unity, aparte y solo con la iglesia:** un proyecto Unity 6 (HDRP) con la zona de la iglesia, para comparar la
    calidad visual. No sustituye al juego, que sigue en el navegador.
  - **Blender y Unity, con scripts sin ventana:** Blender con Python, como hasta ahora; Unity con C# en modo batch,
    sin conector MCP.
  - **El proyecto, solo en local:** una carpeta junto a HQ (`unity-iglesia`), fuera de git, mientras sea una prueba.
  - **Descargas:** sí a Unity Hub, al editor Unity 6.3 LTS y a los paquetes de HDRP.
- Instala él Rosetta 2 y activa su licencia Personal de Unity (lo que necesita su cuenta o su contraseña).

## 2026-10-11 · Unity: instalación y preparación (el que construye)

- **Instalado:** Unity Hub 3.22.2 y el editor 6000.3.26f1 (Apple silicon, 9,2 GB), que trae HDRP 17.3.0. La plantilla
  HDRP de Unity (com.unity.template.hdrp-blank 17.1.1, 61 MB, comprobada su suma) da la escena de partida: sol, cielo
  físico con niebla y los ajustes «High Fidelity».
- **Por qué hace falta Rosetta:** el horneado de luz de Unity (`LightBaker`, `JobProcess`) solo existe para Intel. Sin
  Rosetta, la iglesia solo tendría luz en tiempo real.
- **Las portadas:** en el juego son las antiguas, procedurales, y no están en el GLB de Blender. Se exportan del propio
  juego (Realista, la oeste a 0,85 y entonada como en `src/hiper.js`) a un GLB en el marco de la iglesia. Sin ellas,
  las puertas serían agujeros negros.
- **La escena es un script** (`Assets/Editor/IglesiaUnity.cs`): `Montar` pone la iglesia, las portadas y el suelo
  (adoquín de Poly Haven, CC0) sobre la escena de la plantilla, con su sol y un volumen propio (exposición medida,
  ACES, sombras a 4096 con las de contacto, oclusión e iluminación global en pantalla). `Fotos` saca las vistas de
  `tools/hipershots.js` dibujando cada una muchas veces (para que el antialiasing temporal y la luz se asienten), al
  doble de tamaño, y luego la reduce.
- **Los ejes:** glTFast pasa de glTF (diestro) a Unity (zurdo) invirtiendo la x: un punto (x, y, z) del marco es
  (−x, y, z) en Unity. El giro de la cámara conserva su signo. Se comprueba con las marcas de la foto
  (`tools/hipermarcas.py`).
- **El sol de la foto:** en Unity, la vista «noroeste» lleva el sol real de la foto, a ≈4° y rumbo 237°. El juego no
  puede ponerlo tan bajo y usa 9° (la vista «noroeste9» es esa, para compararlas). La prueba de la luz: en la foto, la
  fachada al sol está 3,4 veces más clara que el muro norte en sombra.

## 2026-10-11 · Unity: la escena, la luz y el ajuste a la foto (el que construye)

- **La primera foto de Unity** salió bien de geometría: las marcas de la foto caen en sus ventanales, óculos, gárgolas
  y torre, como en el juego. El espejo de los ejes y el signo del giro están bien.
- **La luz salió mal:**

  | | sol | sombra | razón | cielo |
  |---|---|---|---|---|
  | Unity | 125 | 14 | 8,9 | 47 |
  | foto | 194 | 59 | 3,3 | 122 |

  Además, el lado al sol salía rojo naranja (190, 110, 32).
- **Lo que no era:**
  - El ambiente «estático» de la plantilla: cambiarlo a dinámico no cambió nada.
  - La iluminación global en pantalla (SSGI), ni la niebla.
  - Que HDRP lee la luz del cielo de la GPU un fotograma después: se probó a dibujar una pasada por actualización
    del editor, como un juego. Se queda así, pero no era esto.
- **Lo que era:** medido en lineal (exposición fija, sin curva), la física de HDRP está bien: sol/sombra ≈ 14, donde la
  foto, estimada, da ≈ 12. Lo que fallaba era el «revelado»: la exposición automática dejaba el sol en 125, y la curva
  ACES hunde mucho los oscuros (por eso la sombra casi negra y el cielo de «fachada» casi negro).
- **El ajuste**, como el de una cámara y solo en la vista de la foto: +1,6 EV sobre el fotómetro y una curva de tono
  propia, con un pie corto y suave y un hombro largo. Queda en los parches de la foto:

  | | sol | sombra | razón | cielo |
  |---|---|---|---|---|
  | foto | 194 | 59 | 3,29 | 122 |
  | Unity (4°) | 193 | 64 | 3,02 | 120 |

- **Probado y descartado:**
  - Más saturación, para el azul más intenso de la foto: quema la fachada al sol (el azul baja a 0).
  - Más aerosoles en el cielo: aclaran el cielo, pero el sol a 4° se apaga demasiado.
- **Lo que queda distinto:**
  - La sombra de la foto es más cálida (84, 53, 26 frente a 74, 63, 40): allí le llega luz rebotada del pueblo al sol,
    que en Unity no hay.
  - El cielo de la foto es más azul y saturado: es el estilo de color de la cámara, o un polarizador.
- **Una puerta encendida:** la puerta norte brillaba en la sombra. El juego le da una luz para la noche, a fuerza 0 de
  día, y el importador de Unity no respeta esa fuerza 0. La exportación de las portadas apaga esas luces.
- **El servidor de HQ** (8920) lo paró la aplicación a mitad de trabajo, y las fotos del juego fallaban con «no carga».
  Se arrancó de nuevo. Además, hipercheck cierra ya su pestaña aunque falle (una pestaña colgada hacía fallar la
  siguiente).

## 2026-10-11 · revisión de la escena de Unity (el revisor): APROBADO CON ARREGLOS

- **Para qué sirve ya:** sirve para comparar geometría, materiales, oclusión y bordes. Para comparar la luz con la foto le
  falta el pueblo alrededor, y la exposición no puede estar ajustada a la propia foto.
- **1. Ejes y cámara:** bien. Las marcas caen en Unity igual que en el juego, a 3–5 px como mucho.
  - Con el espejo en x mal hecho, la torre saldría a la izquierda. Con el signo del giro cambiado, las marcas del borde
    se moverían unos 50 px.
  - **Corrección a una revisión anterior:** la marca del pie de la esquina noroeste cae en lo alto del zócalo, ≈1 m sobre
    el suelo, en el greybox, en el juego y en Unity por igual. Queda para la fase 5 (cámara o terreno de la calle).
- **2. Luz:**
  - El ajuste vale como revelado, pero no como prueba: cinco parámetros de curva más la exposición, ajustados a tres
    parches, los clavan sea cual sea la luz.
  - Lo propuesto: la exposición fija del EXIF de la foto (1/640 s, f/4,5, ISO 200: EV100 ≈ 12,7) y una curva elegida
    sin mirar la foto.
  - La medida buena es la de sol/sombra en lineal, ≈14 en Unity frente a ≈12 en la foto. Esa sí está bien.
  - En otras vistas el ajuste no aguanta: «fachada» saca un cielo casi negro, ≈5 pasos bajo la piedra (un cielo
    despejado a 90° del sol queda 2–3 pasos por debajo), y «ventana» sale lavada.
  - La sombra de Unity tiene un tono gris frío (74, 63, 40); la de la foto es parda (84, 52, 26). Las piedras oscuras
    en sombra salen gris azuladas; en la foto son pardo rojizas (≈44, 18, 4).
  - Faltan las sombras de las casas sobre los 5–6 m de abajo de la fachada de los pies.
  - Las caras oeste de las bandas del muro norte tienen filos naranjas encendidos, y deberían estar en sombra (el rayo
    hacia el sol choca con el muro a ≈0,9 m).
  - El cielo sale gris pizarra (102, 124, 148) frente al azul de la foto (66, 135, 199), y crema abajo a la izquierda
    frente al (161, 210, 244) de la foto.
- **3. Calidad:**
  - **Gana Unity:** piedra al sol, oclusión y relieve (derrame, cartela, vuelo de la cornisa, anillos del óculo) y el
    vidrio, que refleja el cielo. En «torre», la cara en sombra queda almohadillada.
  - **Gana el juego:** el tono de la sombra y las sombras de las casas.
  - **Bordes:** comparación injusta, porque Unity va al doble de tamaño y con 64 pasadas.
  - **Materiales:** falta en Unity la mancha de color del juego (`hiper.js`), y la textura se repite cada 6 m.
- **4. Arreglos, por orden:**
  1. El pueblo alrededor en volúmenes simples: las casas del Catastro con su altura, encaladas y con tejado pardo, en
     60–80 m.
  2. El cielo: menos aerosoles, ozono, y la niebla sin el crema del horizonte.
  3. La exposición fija (EXIF en «noroeste», fija por hora en las demás) y una curva de cámara congelada.
  4. La fuga de las bandas.
  5. Comparación justa: la misma mancha en Unity y el mismo supermuestreo en los dos motores.

## 2026-10-11 · los arreglos de Unity (el que construye)

1. **El pueblo.** No se rehízo desde el Catastro: es la geometría del propio juego (casas, calles, bordillos), exportada
   a 80 m de la iglesia (`entorno_glb.py`). Así coinciden alturas y tejados. Va en tres materiales lisos, porque las
   casas del juego toman su aspecto de sus propios sombreadores:
   - paredes encaladas (0,78);
   - tejados pardos (0,45, 0,25, 0,17);
   - suelo gris (0,33).
   Quedan fuera los árboles, los coches, las farolas y la gente. Ahora la sombra de las casas cae sobre la parte baja de
   la fachada de los pies y sobre la portada, como en la foto y en el juego.
2. **El cielo.** Queda sin tocar: el modelo de HDRP por defecto ya trae ozono y aerosoles mínimos. Más aerosoles
   apagaban el sol a 4°, y la saturación quemaba la piedra.
3. **Exposición y curva, sin mirar la foto.**
   - EV100 fija: 12,7 en «noroeste», la del EXIF (1/640 s, f/4,5, ISO 200). En las demás vistas, según la altura del
     sol: de 12,7 a 4° hasta 15 («sunny 16») a 40° o más, en línea recta.
   - La curva es la neutra de HDRP, tal cual.
   - Ahora la medida es una medida. En «noroeste», Unity da sol 143, sombra 36 y cielo 86; la foto, 194, 59 y 122: Unity
     sale ≈0,7–1 paso más oscuro.
4. **La fuga de las bandas.** No era el sesgo de la sombra: con la luz directa del sol apagada, las líneas naranjas
   seguían ahí. Era la luz del cielo de poniente, que en tiempo real llega sin tapar a esas caras.
   - El arreglo es luz horneada por vista: lightmaps del cielo y del rebote del sol, el pueblo incluido, sobre el
     segundo UV del modelo, a 5 texeles/m. Son ≈20 s por vista, con el horneador de Unity bajo Rosetta.
   - La luz directa sigue en tiempo real.
   - La SSGI queda apagada.
   - La AO de Blender queda a 0 (si no, oscurecería las esquinas dos veces).
   - Las portadas toman la luz de sondas puestas delante.
5. **Comparación justa.** Las fotos del juego («_justa») van al doble de tamaño y reducidas, como las de Unity, y sin
   la mancha de `hiper.js` (`tools/hipershots.js`: opciones `pr` y `sinmancha`).

## 2026-10-11 · segunda revisión de Unity (el revisor): APROBADO CON ARREGLOS

- **Para qué sirve:** la escena de Unity ya es base de comparación. La cámara está bien y la exposición ya no está
  ajustada a la foto, así que la medida dice algo.
- **Los cinco arreglos:**
  1. Pueblo: en parte. La sombra de las casas ya cae en la fachada, pero el muro norte no se calienta: sigue
     (43, 34, 23) frente a (84, 53, 26).
  2. Cielo: no. Sigue gris pizarra y crema junto al horizonte; queda probarlo sin niebla.
  3. Exposición y curva: sí.
  4. Fuga: en parte. Las líneas naranjas se fueron, pero el horneado ha traído manchas de color: una roja y otra amarillo
     verdosa en «ventana», y cartelas rojizas en «noroeste». El segundo UV es el atlas de la oclusión, compartido y con
     márgenes de 0,003: a 5 téxeles/m sangra. Y 512 muestras dejan ruido.
  5. Comparación justa: sí, para fotos fijas.
- **La medida:**
  - El reparto sol/cielo es el de la foto: 2,95 frente a 2,77 en lineal.
  - El paso de menos se explica por dos mitades:
    - medio paso de convención: el EV100 de HDRP pone la saturación donde la cámara pone el gris del 18 %;
    - y la incertidumbre de la altura del sol (en la foto el frontón de la portada está al sol; en Unity a 4°, no) o de
      la altura de las casas.
  - El contraste de más está en la sombra: es luz cálida que no llega.
- **Motor contra motor:**
  - **Unity hace mejor:** el brillo del cielo (el del juego es tan claro como el muro, y eso un cielo despejado no lo
    da), el sol a 4°, las sombras con su penumbra, la oclusión de huecos, cartelas y óculo, y el vidrio que refleja.
  - **El juego hace mejor:** el tono de la sombra; no tiene manchas; y va todo en tiempo real, con el sol moviéndose.
  - **Injusto a favor de Unity:** hornea la luz para cada vista, y las 64 pasadas de TAA con la cámara quieta.
- **Arreglos pendientes de Unity:**
  1. la sombra cálida (comprobar que el pueblo rebota en el horneado);
  2. el cielo sin niebla;
  3. un horneado limpio (segundo UV propio, márgenes, más muestras y eliminación de ruido);
  4. la altura del sol de la foto, en la fase 5;
  5. −0,5 EV de convención si se comparan brillos;
  6. menores: SSAO a 0,5 m y el relieve de la sillería de la torre.

## 2026-10-11 · el usuario: lo de Unity, al juego

- Quiere ver el resultado en el juego. Elige pasar al juego del navegador lo que Unity hace mejor y se puede llevar, y
  publicarlo en GitHub Pages (HQ). Unity sigue siendo solo la comparación.
- Lo que no se toca es la luz de todo el pueblo (su decisión anterior). Las mejoras van en la iglesia.

## 2026-10-11 · fase 4b en el juego, primera vuelta (el que construye)

- **Vidrio:** toma el mapa del cielo de la escena como su envMap propio, a intensidad 1, con rugosidad 0,06
  (`src/hiper.js`, `glass`). Pasa de negro (15, 15, 13) a (31, 32, 27).
- **Oclusión con rebote** (`bake_ao`):
  - **Primer intento, descartado:** hornear la luz entera de un cielo blanco y escalarla a la mediana. Los muros abiertos
    bajaban de ≈0,95 a ≈0,63, porque la calle contaba como cielo tapado y el juego ya la pone en su luz ambiente.
  - **El bueno:** el AO aprobado tal cual, más el difuso indirecto bajo cielo blanco, con una calle de albedo 0,25:
    `ao + (1 − ao)·rebote`. La mediana pasa de 0,59 a 0,63; los muros abiertos no cambian (sol 153 → 154, sombra 52).
- **Cartela:** cortada con sillería en vez de «hueco».
- **Rendimiento:** 59,9 fps junto a la iglesia.

## 2026-10-11 · revisión de la fase 4b (el revisor): NO APROBADO, todavía

- **Lo que está bien:** nada empeora. El vidrio ya refleja, en la cantidad de un vidrio de verdad (un 4 % de frente), y los
  muros abiertos no cambian.
- **Lo que falla: derrames y cartela siguen negros.**
  - **Los derrames:** sus caras no son de piedra. Los cortadores de ventanales, recercados y arcos del campanario dejan
    el material «hueco», de albedo 0,01, y ninguna oclusión puede aclararlo.
  - **La cartela:** el fondo de su rebaje coincide con el plano del muro, y dos caras en el mismo sitio se hornean sin
    luz.
  - **El mapa nuevo:** no se nota en ninguna vista. Sube poco: la mediana, de 0,59 a 0,63.
- **Arreglos pedidos:**
  1. derrames de piedra; el negro, solo en los huecos de verdad (puertas y saeteras);
  2. la cartela, a 1–2 cm del muro;
  3. capturas que lo enseñen: un primer plano de la cartela y el vidrio visto desde la calle.
- **Opcional:** un mapa del cielo propio para el vidrio, sin la banda de fachadas (a 16 m de altura no es creíble), y
  rugosidad 0,15–0,25 para las vidrieras emplomadas.

## 2026-10-11 · fase 4b, segunda vuelta (el que construye)

1. **Derrames de piedra.** Dejan caras de sillería todos estos cortadores: ventanales, recercados, tracerías, óculos y
   su anillo, ventanitas del bloque noroeste, arcos y cámara del campanario y del cuerpo alto. El «hueco» queda solo
   en las bolsas de las puertas y en las saeteras. En el GLB, «hueco» pasa de 2150 a 221 triángulos.
   - **Escala de la textura:** las UV de cada cara van ahora a la escala de su propio material (`reuv`). Un derrame
     cortado en la mampostería iba a 6 m y ahora va a los 3 m de la sillería.
2. **Cartela:** el fondo, a 0,02 m delante del muro.
3. **Capturas nuevas** en `tools/hipershots.js`: «cartela», el primer plano, y «vidrio», desde la calle bajo el ventanal.
- **El resultado se ve** en el campanario (jambas, intradoses y la cámara, ahora de piedra en sombra), en los derrames
  de los ventanales y en la cartela. Los muros abiertos siguen igual, y el juego, a 59,9 fps.

## 2026-10-11 · segunda revisión de la fase 4b (el revisor): APROBADO

- **Los cuatro criterios se cumplen:**
  - **El vidrio refleja el cielo.** Visto desde la calle, a 49–55°, sale azul marino oscuro, como los ventanales del
    muro norte en la foto. De frente y a su altura, refleja el horizonte.
  - **Derrames, cartela, campanario y cuerpo alto:** de piedra con su sombra. El negro queda solo en saeteras y puertas.
  - **Muros abiertos:** sin cambio. La mampostería sigue a 6 m.
  - **Rendimiento:** a 59,9 fps.
- **Nada ha empeorado.**
- **Para la próxima vuelta** (ya estaban antes; no bloquean):
  1. Los cañones de las gárgolas salen negros en sombra, seguramente con oclusión 0 en el atlas.
  2. Los lados de 3 cm del rebaje de la cartela salen como una línea negra de 1–2 px: son más estrechos que un téxel.
  3. Las juntas de la sillería cruzan el marco y el óvalo de la cartela.
  4. Opcional: el mapa del cielo propio para el vidrio, sin la banda de fachadas.

## 2026-10-11 · el usuario: desgaste, el interior y los Backrooms en la iglesia

- «Sigo sin verlo hiperrealista.» Pide una capa nueva en la plaza y en la iglesia, con desgaste, suciedad e
  irregularidades al azar en el suelo y en las paredes.
- Pide también que el interior mejore muchísimo, «como en Unreal o Unity». Elige «Luz de motor, en el juego»: la luz de
  un motor de gama alta, pero dentro del juego del navegador.
- Y que los Backrooms no estén en el teatro, sino en la iglesia, «en una de las puertas al lado del altar».
- Acepta descargar cinco texturas de Poly Haven (CC0) para el suelo de la fase 5b: asphalt_04, asphalt_02,
  checkered_pavement_tiles, brown_mud_dry y concrete_floor_01.

## 2026-10-11 · los Backrooms, a la puerta de la sacristía (el que construye)

- La puerta de la sacristía, junto al altar mayor (lado de la Epístola), lleva ahora a los Backrooms. Tiene una raya de
  luz fría por debajo y el zumbido de los tubos.
- Al volver, se sale delante de esa misma puerta, en el presbiterio y de espaldas a ella.
- El teatro pierde su puerta amarilla.
- Probado sin sonido en el Chrome sin ventana: el aviso «Abrir la puerta de la sacristía», la entrada, la salida y la
  vuelta a la iglesia, sin errores.

## 2026-10-11 · fase 5a, primera vuelta (el que construye)

- **La capa de desgaste** está en el sombreado de la piedra (`src/hiper.js`) y se calcula en el marco de la iglesia:
  - churretes desde la cornisa, bajo las ocho gárgolas de cada lado, desde los extremos de los alféizares y el largo del
    muro norte;
  - el pie sucio y húmedo;
  - desconchones claros en la mampostería;
  - liquen en lo que mira arriba;
  - una ondulación de pocos centímetros.

  Dónde van las gárgolas y los ventanales sale de `iglesia.json` («desgaste»).
- **Los mechinales:** 96 agujeros de 16 cm en filas cada 1,45 m, en la fachada de los pies y la torre, cortados en el
  modelo.
- **Los parches de la foto no cambian:** al sol, 154 → 153; en sombra, 52 → 51.
- **Rendimiento:** 59 fps (p95: 16,8 ms).

## 2026-10-11 · revisión de la fase 5a (el revisor): NO APROBADO

- **El veredicto:** lo pedido está y casi todo en su sitio, pero la mitad del desgaste parece pintado encima. Antes de
  afinarlo hay que rehacer la mampostería, que es lo que más separa la iglesia de la foto.
- **Criterio a criterio:**
  - **El churrete largo del norte:** está en su sitio, pero sale como una línea fina, ondulada y casi negra, de 15–25 cm
    (parece una grieta o un cable). En la foto es una banda recta y difusa, gris verdosa y de poco contraste: unos
    0,3 m de ancho bajo la gárgola y 0,7 m abajo.
  - **Bajo las gárgolas:** de largo están bien.
  - **Desde la cornisa:** la foto no tiene ninguno. En el juego salen como barrotes verticales regulares.
  - **El pie:** vale. En la foto es más gris, no más oscuro, con manchas blanquecinas de cal.
  - **Desconchones: no.** Son manchones gris blanquecino de 1–2 m con borde nítido, por encima de las piedras. En la
    foto lo claro va piedra a piedra (piedras crema y grises, mortero de cal), a 10–30 cm.
  - **Mechinales:** de lejos se leen como en la foto. De cerca son cuadrados de negro puro, perfectos e iguales. En la
    foto son pardo oscuro, irregulares, de 10–16 cm, y algunos están medio rellenos.
  - **La ondulación:** no se ve en ninguna vista.
  - **Parches y rendimiento:** se cumplen.
- **Lo que más pesa:**
  1. **La mampostería:**
     - la masa dorada es un mosaico de polígonos con juntas finas, y en la foto el mortero está enrasado, del mismo
       tono, sin juntas a la vista;
     - las piedras oscuras son esquirlas de aristas rectas, gris pizarra, con halo y repartidas por igual. En la foto
       son cantos redondeados, pardo rojizo oscuro (≈44, 18, 4 en sombra), de 8–30 cm, sin halo y en racimos;
     - y todo es plano.
  2. **La luz del pueblo:** 153 frente a 194 de la foto. La decide el usuario.
  3. **El desgaste de ahora:** los manchones, los barrotes y los negros.
  4. **La geometría, demasiado perfecta.** Falta además el pararrayos de cobre de la esquina noroeste.
  5. **La portada oeste antigua**, pixelada.
  6. **Los alrededores** (fase 5b).
- **Arreglos pedidos:**
  1. Rehacer la mampostería en `texturas.py` y medir la piedra oscura: ≈13 % en el norte y ≈4 % en los pies.
  2. Quitar los manchones: piedras sueltas más claras y cal blanquecina solo abajo, en el norte, hasta unos 3 m.
  3. Los churretes:
     - el largo, recto, de 0,3 a 0,8 m, gris verdoso, oscureciendo un 25–35 % (ahora, un 64 %);
     - los de cornisa, fuera, o uno o dos cortos por muro;
     - los de gárgola, más suaves.
  4. Los mechinales, con caras de piedra; de 12–20 cm, irregulares, algunos medio rellenos.
  5. El pie, más gris que oscuro.
  6. Capturas, parches y fps nuevos.
- **Siguen ahí:** los cañones de las gárgolas negros en sombra y las líneas de 1 px de la cartela.

## 2026-10-11 · el usuario: el interior en alta definición

- Pide: «Haz la iglesia por dentro de muy alta definición, todo, esculturas, santos, cuadros, bancos, decoraciones,
  velas, flores... todo con el máximo detalle y realismo como si fuera el GTA V, usa Unreal para hacerlo posible.»
- Se le explica que Unreal no puede ir dentro del juego del navegador. Elige:
  - **En el juego web:** Blender con escaneos y luz horneada, dentro del juego;
  - **Escaneos reales:** texturas y modelos libres (Poly Haven, ambientCG, Smithsonian), Megascans de Fab con su
    cuenta de Epic si hacen falta, e imaginería española escaneada con licencia libre, con su crédito. Cada descarga se
    le pide antes;
  - **Cuadros reales de dominio público:** Zurbarán, Murillo, Morales…, con su crédito.
- Los arreglos de la fase 5a y el suelo de la 5b quedan en pausa: se hace antes el interior (fase 6, en
  `docs/hiperrealismo.md`).

## 2026-10-12 · el usuario: las descargas y el suelo

- Aprueba bajar tres texturas CC0 (48 MB, en `.cache`):
  - de ambientCG, «Granite002A» y «Plaster003»;
  - de Poly Haven, «Large Floor Tiles 02».

  Sumas MD5 y zip comprobados.
- El suelo de Santa María es de **losas de granito gris** (lo dice el usuario).

## 2026-10-12 · fase 6a, primera vuelta (el que construye)

- **El modelo** (`tools/blender/interior.py`) se hace con las medidas de `church.js`:
  - los muros macizos con sus huecos cortados: puertas, ventanales abocinados y óculo;
  - pilares y capillas, con su bóveda apuntada y su arco apuntado moldurado;
  - las columnas jónicas enteras: pedestal moldurado, basa ática, fuste con éntasis y 24 estrías, equino con ovas, dos
    volutas en espiral, ábaco e imposta;
  - los arcos fajones moldurados;
  - bóvedas de terceletes con nervios de perfil de bocel y claves talladas y doradas; en el tramo del presbiterio, la
    estrella de la foto;
  - el arco triunfal, con el intradós de casetones;
  - la media naranja, con 60 casetones de dos escalones y su roseta;
  - el coro sobre el sotocoro estrellado, con la balaustrada torneada;
  - el zócalo de sillería y los marcos de las dos puertas pequeñas.
- **Dos medidas cambian** respecto a `church.js`, y lo que se pisa no cambia:
  - los ventanales de la nave suben a los lunetos (la luz entre 14,6 y 18,4 m, como en la foto de fuera); antes
    cruzaban la imposta;
  - el óculo baja a 10 m, como en la foto.
- **El greybox,** comparado con el interior de antes desde las vistas de `tools/churchshots.js`: encaja con los
  bancos, el retablo y las puertas.
- **Las texturas** (`tools/blender/texturas_interior.py`):
  - el encalado, de «Plaster003», blanqueado a cal;
  - el granito gris claro, mate y labrado, de «Granite002A»;
  - las losas del suelo a hiladas, cada una con su trozo de granito y el desgaste de «Large Floor Tiles 02»;
  - una vidriera emplomada.
- **La luz,** horneada en Cycles con la GPU y el quitarruido OIDN:
  - el cielo, por los ventanales, con portales de luz en ellos;
  - el rebote del sol a cinco horas;
  - las lámparas.
- **El juego** (`src/hiperinterior.js`):
  - carga el modelo aparte, solo en Realista;
  - esconde la arquitectura de `church.js`;
  - mezcla los mapas según la hora, el cielo y las lámparas, y adapta la exposición como una cámara;
  - el sol directo va en tiempo real;
  - lo horneado no recibe la luz ambiente ni las puntuales;
  - las juntas de tambores, dovelas y sillares se dibujan en el sombreado;
  - los reflejos salen de una foto en cubo del propio interior.
- **Problemas encontrados y arreglados:**
  1. **El atlas de luz se aprovechaba en un 6 %:** casi 12.000 islas, y sus márgenes se lo comían. Se quitaron 54.000
     caras que nadie ve (por rayos desde 7.300 puntos del aire de la iglesia), el margen quedó en 2,5 px y la
     resolución es mayor abajo que en las bóvedas. Ahora se aprovecha un 50 %.
  2. **Al apartar las caras ocultas con operadores,** la selección que venía de antes se llevaba también las visibles:
     el suelo desaparecía entero. Ahora se hace con bmesh.
  3. **Todo salía negro:** el `interior.json` de un horneado anterior, con el formato viejo, daba NaN.
  4. **Manchas en bóvedas y casetones:** la escala de cada mapa la ponía la luz de los derrames, cien veces la de la
     nave, y los 8 bits no alcanzaban para la penumbra. Ahora la escala no pasa de 24 veces la mediana.
  5. **Una raya de sol en los rincones de las capillas:** sin sus caras exteriores, los muros eran láminas para el mapa
     de sombras. Las caras ocultas van ahora al juego como «sombra», una malla que solo da la sombra del sol.
  6. **Columnas rayadas:** a 12 cm por píxel, el mapa no puede dibujar estrías de 17 cm. El horneado final va a
     3072 px, unos 4 cm.
- **Rendimiento dentro:** 57,7 fps (con el interior antiguo, 59,9); p95 de 16,8 ms.

## 2026-10-12 · fase 6a, segunda vuelta (el que construye)

Con el horneado final (3072 px, 1024 muestras) la iglesia salía mucho más limpia, pero quedaban tres problemas:
1. **Las columnas, rayadas.** Las estrías (de 17 cm) salían en franjas irregulares porque el mapa las muestreaba mal.
   - El fuste se hornea ahora como un cilindro liso: con su propio desenvolvimiento y las normales del cilindro.
   - La sombra de cada estría la pone el sombreado del juego, desde la UV del fuste.
   - Queda regular y nítida.
2. **Los casetones, manchados.** La media naranja y el arco triunfal se partían en islas diminutas.
   - Cada uno tiene ahora su proyección, de una pieza: la media naranja, de área igual (sinusoidal); el intradós del
     arco, desenrollado.
   - Sus fondos se oscurecen con una oclusión por vértice, según la profundidad de cada escalón: el material
     «casetón», con su COLOR_0.
3. **Los muebles sin la luz horneada.** El retablo de una capilla brillaba igual que en la nave.
   - Se hornean además 5.296 sondas de luz, una rejilla cada 1,5 m por el aire de la iglesia. Cada sonda es un cubito
     cuyas seis caras guardan la luz que les llega de su lado (un «ambient cube»).
   - Van en `luz/sondas.bin`, de 1 MB.
   - En el juego, los muebles, las puertas y los cuadros de `church.js` toman de ellas su luz ambiente, mezclada a cada
     hora como los mapas. Dejan de recibir las luces puntuales, que ya están en las sondas.
- **El horneado final:**
  - mapas de 3072 px (cielo y lámparas) y de 2048 px (sol);
  - 1024 muestras;
  - los muebles del juego dan su sombra;
  - unos 11 minutos con la GPU.

  Lo que se descarga aparte pesa 20 MB: el modelo, 5,3; las texturas, 8,0; la luz y las sondas, 6,7.
- **Retoques:**
  - de noche, la vista no se adapta del todo: el nivel baja al 62 %, con las bóvedas en penumbra y la luz de las arañas;
  - el oro, el latón y la plata de los muebles reflejan la foto en cubo del propio interior, y no el entorno pintado de
    `church.js`, que los hacía brillar en la penumbra de las capillas.
- **Rendimiento:**
  - el Chrome sin ventana va a 30 Hz desde la madrugada (también con el interior antiguo), así que los fps de ahora no
    sirven para comparar;
  - midiendo el coste de cada fotograma esperando a la GPU, el interior nuevo y el antiguo cuestan lo mismo: 2,5 y
    2,6 ms de mediana;
  - la mezcla de las sondas se rehacía 15 veces por segundo (5,5 ms cada una). Ahora va a lo sumo una vez por segundo,
    solo si la luz cambia, y repartida en seis fotogramas de 1 ms.

## 2026-10-12 · revisión de la fase 6a (el revisor): NO APROBADO

- **El veredicto:** la arquitectura está completa y en su sitio. La luz entra, rebota, se mueve con la hora, y la noche
  funciona. Pero dos criterios no se cumplen:
  - el horneado de día tiene costuras, manchas y fugas de sol;
  - la media naranja no se parece a la foto: sale casi negra.
- **Criterio a criterio:**
  - **Proporciones frente a `church.js`:** sí. El órgano tapa ahora media vista del óculo, que ha bajado a 10 m (para la 6b).
  - **Parecido con la foto:** las formas, sí. El tono y los materiales, no:

    | Medida | Juego | Foto |
    |---|---|---|
    | Media naranja (brillo mediano) | 34–42 | 134 |
    | Muros del ábside | 101–114 | 169 |
    | Media naranja ÷ muro | 0,33 | 0,79 |
    | Color de los muros | sepia (127, 111, 92) | gris neutro frío (169, 169, 172) |

    - En la foto, los muros del ábside son de sillería de granito, no de cal.
    - No enseña ventanas junto al retablo: la luz llega por los bordes, junto a las columnas.
    - La estrella del presbiterio es una red de nervios curvos en rombos, con 8–12 claves; en el modelo, un anillo.
  - **La luz:**
    - entra y rebota, los rincones quedan en penumbra sin ser negros, las manchas de sol se mueven con la hora y de
      noche alumbran las arañas: sí;
    - **sin ruido, manchas ni costuras: no.** Salen:
      - escalones y dientes de sierra en los plementos;
      - rectángulos y manchas nubladas en las enjutas;
      - bloques pixelados en la moldura del arco triunfal y en la imposta;
      - **fugas de sol:** líneas de puntos blancos en un meridiano y en el pie de la media naranja, y en el borde alto
        del arco triunfal, por rendijas de la malla «sombra»;
      - motitas color cielo donde los nervios y el arco se juntan con los plementos.
    - La noche apenas es más oscura que el día.
  - **Materiales:**
    - los sillares van dibujados de 0,90 × 0,45 m, y la tabla pide ≈0,60 × 0,40;
    - el granito, de cerca, parece una encimera.
  - **Rendimiento:** sin verificar con la versión final; hay que medir a 60 Hz.
  - **Peso:** sí, 20 MB.
  - **Sondas de los muebles:** encajan a medias. El oro refleja el cubo tomado en el centro de la nave y brilla en los
    rincones oscuros.
- **Lo que más pesa, por orden:**
  1. los muebles y las lámparas de `church.js` (6b y 6c);
  2. el horneado: costuras, dientes de sierra, manchas y fugas;
  3. el tono: sepia y apagado, con la media naranja casi negra;
  4. todo demasiado limpio y perfecto: sin humedad, hollín, desgaste ni grietas; aristas vivas;
  5. los materiales: granito de encimera, cal sin variación, losas demasiado iguales;
  6. los haces de polvo, planos de bordes duros;
  7. las vidrieras, una rejilla demasiado regular.
- **Arreglos pedidos:**
  1. **Un horneado limpio:**
     - mapas sin compresión por bloques (sin pérdida, o KTX2);
     - en bóvedas y arcos, al menos la densidad de los muros;
     - costuras escondidas bajo nervios y aristas, con 4–8 px de margen;
     - más muestras, o el quitarruido con sus pases de albedo y normales.
  2. **Cerrar las fugas:**
     - una «sombra» estanca y plementos metidos bajo los nervios;
     - buscar fugas con el sol a cada hora.
  3. **La media naranja como en la foto:**
     - casetones de cal o de piedra clara;
     - la oclusión por vértice solo para lo que el mapa no ve;
     - meta: ≈0,8 del muro del ábside.
  4. **El ábside:** de sillería de granito claro, y revisar sus ventanas con la foto.
  5. **La luz del cielo,** neutra o algo fría.
  6. **Reflejos según la luz de cada sitio:** una sonda por capilla, o el especular atenuado con la sonda.
  7. **Haces de polvo:** menos y de bordes suaves.
  8. **Menores:**
     - sillares de 0,60 × 0,40;
     - granito más claro y menos moteado;
     - la estrella en rombos;
     - una noche más oscura;
     - el órgano fuera del óculo (6b);
     - fps medidos a 60 Hz.

## 2026-10-12 · fase 6a, tercera vuelta (el que construye)

Los arreglos del revisor, por su orden:
1. **Un horneado limpio:**
   - **Una isla por pieza:** cada pieza curva lleva su propio desenvolvimiento, de una sola isla, con la costura en su
     cara escondida:
     - los barridos (molduras, nervios, arcos, archivoltas), por su perfil y su largo;
     - los torneados, alrededor de su eje;
     - las superficies (plementos, sotocoro, capillas, media naranja), por la longitud de sus filas y columnas.

     Las islas bajan de casi 12.000 a unas 7.000, casi todas de los detalles pequeños.
   - **Densidad pareja:** la misma en todo, también en bóvedas y arcos: ≈4,3 cm por píxel. Márgenes de 4 px y relleno
     de 8.
   - **Quitarruido guiado** por las normales del atlas, horneadas aparte.
   - **WebP sin pérdida** (calidad 100, comprobado: error 0) en vez de JPEG.
   - **Más muestras:** 2048.
2. **Las fugas:**
   - una carcasa estanca alrededor de la cabecera, de la coronación del muro al tejado (por ahí entraba el sol sobre la
     media naranja);
   - los plementos entran 18 cm en los muros y bajo los arcos;
   - la media naranja, con un borde que se mete en el muro y en el arco triunfal.
3. **La media naranja:**
   - los casetones son de cal, y sus fondos de una cal algo más gris, como los centros oscuros de la foto;
   - sin la oclusión por vértice, que oscurecía dos veces.
4. **El ábside:** de sillería de granito claro, con sus hiladas siguiendo la curva. Sus dos ventanas pasan a los lados,
   junto a las columnas del arco.
5. **El color:**
   - la luz del cielo, neutra y algo fría (0,95; 0,98; 1);
   - la cal, neutra (0,76; 0,77; 0,78);
   - el granito, gris claro y neutro (0,56), con el moteado a la mitad.
6. **Los reflejos:**
   - lo horneado se había quedado sin ellos: el parche quitaba el trozo de three que los pone. Ahora los recupera;
   - se escalan con la luz de cada superficie (la horneada, o la de las sondas en los muebles), frente a la del sitio
     de la foto en cubo. Así el oro de un rincón oscuro no brilla;
   - la luz difusa del mapa de reflejos ya no se suma a la horneada ni a la de las sondas.
7. **Los haces de sol:** ahora son volúmenes. Cada píxel sigue su rayo a través del haz en seis pasos, con un perfil
   suave hasta el borde, la entrada y la caída, y el polvo moviéndose.
8. **Menores:**
   - sillares dibujados de 0,60 × 0,40 m;
   - la estrella del presbiterio, con sus combados en rombo y 13 claves;
   - la noche, al 45 %.

## 2026-10-12 · fase 6a, tercera vuelta: lo que salió al comprobarla (el que construye)

- **Rendimiento:** dentro, a 60 fps de día y de noche, con el interior nuevo y con el antiguo (bucle real del juego,
  Chrome sin ventana a 60 Hz). Cada fotograma, esperando a la GPU: 2,3–2,9 ms el nuevo frente a 5,7 ms el antiguo,
  de noche. Al entrar hay un parón de ≈1,5 s (montar la iglesia de `church.js`), igual con los dos interiores. Los
  41,9 y 50,6 fps medidos antes de noche eran de una pestaña recién abierta, no del interior.
- **«No carga» en las pruebas:** el servidor de desarrollo cortaba conexiones (`net::ERR_CONNECTION_RESET`) cuando el
  navegador pedía todos los módulos a la vez: la cola de espera de Python es de 5. `tools/devserver.py` la sube a 128.
- **Las lámparas alumbraban dos veces.** El parche que apaga en tiempo real los puntos y focos de `church.js` sobre lo
  horneado (su luz ya está en el horneado) no hacía nada: se aplicaba antes de que three expanda sus `#include`, y el
  texto que buscaba no estaba aún. Las arañas (14 cada una, también de día) y los focos del retablo (60) se sumaban,
  cálidos, a la luz horneada: de ahí el tono sepia que vio el revisor. Ahora se cambia el trozo de three ya expandido,
  en la arquitectura y en los muebles de las sondas.
  - **Consecuencias:** sin esa luz de más todo quedó neutro pero más apagado. La exposición del «ojo» sube de 0,62 a
    1,15, y la luz ambiente de la gente baja de noche como la horneada.
  - **El color de las lámparas,** uno solo para mapas y sondas: ≈3000 K, el de las arañas de `church.js`. Antes, el de
    los mapas iba aparte, más frío, y a las sondas no llegaba.
  - **El ojo también se adapta al color:** deshace en parte el color de la luz que domina (cielo, sol y lámparas, por
    su parte en la mediana), un 70 % de día y un 21 % de noche, como un balance de blancos. Así la cal se ve blanca
    bajo el sol de la mañana, y de noche las lámparas siguen cálidas. El tono cálido que quedaba de día venía del sol
    rebotado, no de las lámparas.
- **Las medidas no eran repetibles,** por dos cosas que ya están corregidas:
  - **El tiempo en directo:** el juego lee las nubes reales de Guareña, que cambian entre tandas. Ahora las pruebas
    usan el tiempo propio del juego (el de claude.ai, parcialmente nuboso).
  - **El «bloom» de las capturas:** `tools/churchshots.js` apaga `render()` mientras fotografía, y el bloom se quedaba
    con el de la hora a la que arrancó el juego. A veces era el de noche, que deja un velo sobre la cal. El bloom pasa
    a `game.updateBloom()`, y las capturas lo ponen para su hora.
- **La media naranja,** medida así (11 h, las mismas regiones, sin ventanas ni retablo):
  - cúpula 73 (73, 73, 73);
  - muros del ábside 100 (101, 100, 96) y 76 (77, 76, 73);
  - cociente 0,83 (foto: 0,79).

  El fondo de los casetones vuelve a 0xa9abb0.
- **La noche:** plementos de la nave a 66 de noche frente a 137 de día, cálidos (73, 65, 56).
- **Quedan dos cosas, que van a un horneado nuevo:**
  - **Manchas** del tamaño de una mano en columnas y rincones, que desaparecen al quitar el término del sol: son ruido
    del sol rebotado. Esa luz sale de pocas manchas de sol, pequeñas y muy brillantes, y un camino las encuentra
    pocas veces. El sol se hornea con 4 veces las muestras (8192; `--muestras-sol`).
  - **Vetas** en los marcos de los casetones (cúpula y arco triunfal). Su textura iba proyectada cara a cara, y el eje
    cambiaba de una cara pequeña a la siguiente. Ahora siguen el mismo desenvolvimiento que su luz, en metros.

## 2026-10-12 · el usuario: santos, cuadros y muebles

- A la pregunta «¿Qué echas en falta?» (tras decir «falta algo»), el usuario contestó **«Santos, cuadros y muebles»**:
  lo que pidió al principio y aún son los de `church.js`. El documento tiene ya el plan de la 6b (muebles) y de la 6c
  (santos, cuadros y vida).
- **Aprobó la descarga** de las cinco texturas CC0 de Poly Haven para los muebles: «Dark Wood», «Velour Velvet»,
  «Quatrefoil Jacquard Fabric», «Rough Linen» y «Marble 01». Son 2K en JPG (color, normales y rugosidad/AO), 15
  archivos y 41 MB, en `.cache/polyhaven/muebles_6b`.
- **El horneado de la 6a** queda en luz difusa pura. Las manchas que no se iban con más muestras no eran ruido, sino
  cáusticas: las manchas de sol del suelo, que tenía brillo especular en el horneado, se reflejaban en columnas, arcos
  y casetones. Los motores hornean solo lo difuso y dejan el brillo a los reflejos del juego, y así se hace ya: sin
  capa especular, ni cáusticas ni rebotes especulares en Cycles.

## 2026-10-12 · fase 6b, primera vuelta: los muebles en Blender (el que construye)

- **El método:** `tools/blender/muebles.py` hace cada mueble con las medidas y el sitio de `church.js`. `interior.py
  --muebles-hd [grupos]` lo mete en el modelo: se hornea con la arquitectura y sale en `interior.glb`. Su
  `interior.json` lista los grupos que trae (`muebles`). En el juego, `church.js` da a los muebles de cada grupo
  claves de material propias (`h.furn`), y `hiperinterior.js` esconde los del grupo que el modelo trae: sus
  colisiones, asientos, velas y la misa siguen siendo los de siempre.
- **Los grupos hechos:**
  - **bancos:** 48 bancos de roble teñido, con testeros en voluta (el del pasillo con su cuarterón tallado),
    respaldo de cuarterones inclinado 7°, pasamanos, repisa de misales con ménsulas, travesaño, pata central y
    reclinatorio de terciopelo granate;
  - **retablo mayor:** la composición de `retablo.js` en tres planos, con molduras de verdad:
    - columnas de tercio bajo tallado, fuste estriado y capitel de hojas con volutas;
    - cornisas con arquitrabe, friso tallado y dentellones, quebradas sobre las columnas;
    - marcos de medio punto con cartela y querubines, y las hornacinas del expositor (terciopelo) y de la Virgen
      (azul estrellado), con venera;
    - el sagrario y el expositor de plata, el resplandor;
    - el ático con la paloma en su gloria, las volutas, el frontón partido, el globo y la cruz;
    - copetes, remates y pináculos.

    Los cuadros y la Virgen siguen siendo los de `church.js` (6c);
  - **órgano:** caja de cuarterones, consola de dos teclados con su banqueta, tres castillos de tubos en V con su
    boca, cresterías talladas, cornisas y remates. Va al norte del de `church.js` (centro a −5,3 m), fuera del
    óculo, como pidió el revisor;
  - **colaterales:** los cinco retablos de capilla, con:
    - altar de piedra con tableros y mantel de lino;
    - banco, cuatro columnas salomónicas (fuste en cinco vueltas, con su parra en lo hondo);
    - hornacina con venera, los marcos de sus dos cuadros con querubines;
    - ático con marco y volutas, copete y remate;
  - **presbiterio:** altar de mármol con tableros moldurados y mantel de lino, ambón de madera de atril inclinado y
    las tres sillas (la presidencial con brazos y copete);
  - **púlpito:** copa de granito moldurada sobre su columna, tornavoz con corona tallada y remate, respaldo, y
    escalera de hierro con zancas, balaustres y pasamanos;
  - **confesionarios:** caja con zócalo y cornisa, media puerta con celosía y cortina, reclinatorios con rejilla,
    copete y remate;
  - **bautismo:** pila gallonada sobre balaustre, tapa de madera con cruz; el marco del cuadro; la reja con barrotes
    de lanza, travesaños y volutas;
  - **menores:** las tres pilas de agua bendita en venera, el cepillo con flejes de hierro sobre su poste, y los
    marcos y cruces de las 14 estaciones.
- **Materiales nuevos** (`texturas_interior.py`):
  - madera de nogal medio, de «Dark Wood»;
  - terciopelo granate, de «Velour Velvet»;
  - lino blanco, de «Rough Linen»;
  - propios: pan de oro bruñido (pliegos de 8 cm y bol rojo donde se gastó), talla dorada (más gastada, con el fondo
    picado), plata, azul estrellado, blanco, mármol blanco de vetas grises y hierro.
- **El quitarruido, por islas.** La guía de islas se hornea en la CPU: en la GPU, Cycles se caía compilando para Metal.
  Una prueba rápida con mapas de 1024 y 512 px dejó todo a cero; no era un fallo: con 13.500 islas, los márgenes de
  4 px no caben en mapas tan pequeños. Las pruebas, a tamaño real y con pocas muestras.
- **Peso:** con todos los grupos, el modelo pasa de 4,8 a 11,6 MB (unas 3.000 piezas, 406.000 caras); la talla
  dorada es lo que más pesa.

## 2026-10-12 · el usuario: los cuadros y los santos

- **Aprobó descargar 25 cuadros** de dominio público de Wikimedia Commons («Sí, los 25»): JPG de 1024 px de ancho,
  12,2 MB, en `.cache/commons/cuadros_6c`, con su ficha en `.cache/commons/cuadros_6c_fuentes.json`.
  - Se descartaron las fotos con licencia CC BY-SA del fotógrafo y se eligieron versiones marcadas como dominio
    público.
  - **Retablo mayor:** el Apostolado de El Greco (Museo del Greco, Toledo), los 12 apóstoles; la Crucifixión con la
    Virgen y San Juan, de El Greco y taller; los cuatro Doctores de Zurbarán (San Jerónimo, San Ambrosio, San
    Gregorio; San Agustín, atribuido).
  - **Capillas:** el Bautismo de Cristo de Murillo (catedral de Sevilla); el Milagro del pozo (San Isidro) de
    Alonso Cano; Santa Ana y la Virgen y San Roque, de Murillo; y de Zurbarán Santa Isabel de Portugal, San
    Francisco en meditación, San Antonio de Padua con el Niño y Santa Lucía.
- **Los santos, tallados en Blender** («Talladas en Blender»): figuras propias de imaginería, con cuerpos de
  MakeHuman, ropajes y policromía, sin descargas.

## 2026-10-12 · el usuario: las imágenes sin cuello

- **Lo que dijo:** «Parece que las imágenes las esculturas no tienen cuello parece que la cabeza está metida en los
  hombros por favor, asegúrate que todas las esculturas tengan cuello».
- **Por qué pasaba (dos causas):**
  - **Las tres Vírgenes.** Sus rasgos de mujer salen de los objetivos de MakeHuman de una mujer entera (el archivo de
    cabezas del juego, `assets/mh/head.bin.gz`), más baja que el hombre cuyo cuerpo llevan debajo. Sobre ese cuerpo
    bajaban la cabeza y el cuello entre 13 y 15 cm, dentro de los hombros.
    - Arreglo: de esos objetivos se toma solo la forma de la cara. Se miden desde la base del cráneo, enteros en la
      cabeza y desvaneciéndose por el cuello, de la barbilla a su raíz. El cuello del cuerpo sostiene la cabeza donde
      iba.
  - **Todas.** La túnica salía de la malla «tights» de MakeHuman, un mono entero que sube por el cuello y la nuca
    hasta el cráneo, como una capucha.
    - Arreglo: un escote redondo en la raíz del cuello, bajo delante (en el hueco del esternón), donde el cuello se
      junta con los hombros a los lados y en la séptima vértebra detrás.
    - El borde va suavizado a lo largo del corte, y la tela se ciñe allí al cuello, como un dobladillo.
- **Lo que se ajustó a la vez:**
  - **El velo:** medido sobre la cabeza (la coronilla, y los lados hasta la barbilla) y abierto bajo la barbilla, para
    que se vea el cuello.
  - **El pelo:**
    - las Vírgenes llevan pelo con raya en medio bajo el velo; antes asomaban calvas;
    - el pelo y las barbas de los hombres crecen de la piel, sin el borde de casco, y van en mechones tallados.
  - **El Cristo:** el cuello 2,5 cm más largo y la cabeza algo menos caída.
  - **El Niño de San José:** más abajo y a un lado, para que no tape la cara ni el cuello del santo.
  - **El corazón del Sagrado Corazón:** encima del pecho (estaba dentro de la túnica), con su corona de espinas, sus
    llamas y su cruz.
  - **El puñal de la Dolorosa:** la hoja clavada y el puño de plata fuera.
  - **Los ojos de vidrio:** en el juego llevan ya su iris y su pupila (textura propia, «ojo»).
  - **Las imágenes antiguas:** las piezas de metal (aureolas, coronas, puñal, vara) tienen claves propias y se
    esconden enteras cuando entran las nuevas. Antes quedaban el puñal viejo, cruzando a la Dolorosa, y una segunda
    aureola sobre San José.
- **Comprobado:** en Blender, de frente y de tres cuartos, y en el juego, desde el suelo y de cerca. Las seis tienen
  cuello.
  - Capturas: `.snaps/im_<imagen>_pie_cuello2.jpg` y `.snaps/im_<imagen>_cerca_cuello2.jpg`.
  - El antes y el ahora: `.snaps/cuello_antes_ahora.jpg`.
- **Queda (6c):**
  - la Dolorosa y el Sagrado Corazón se ven muy oscuros en sus capillas (el luto, en una capilla en penumbra: hará
    falta la luz de sus velas o un foco);
  - la policromía (estofado y encarnaciones), la corona de espinas del Cristo y la cara del Niño, que es de adulto.


## 2026-10-17 · Viviendas, acabados y casa de Annie

- El usuario pidió reforzar validación y completar las habitaciones por tandas; después autorizó terminar revisión visual, corregir acabados, actualizar Annie, hacer commits/push y desplegar.
- Se incorporan 15 kits nuevos y se preservan funciones y perfiles de las 22 casas de vecinos. Annie conserva su plano singular y dormitorio, con cinco habitaciones comunes por kit.
- Se corrigen materiales demasiado oscuros por una segunda conversión sRGB, caché de dibujos sin semilla, mobiliario de cocinas grandes y cuarto joven, reservas de despensa, luminarias, piano, cornamentas y telas. El kit doméstico conserva paso de 0,8 m y los límites originales de rendimiento.
- La revisión independiente detectó un error del inventario de Annie y pérdida de control de sus lámparas al agrupar; se corrigieron. Las capturas esperan el fin del vuelo inicial y distinguen taller de pintura.
- Las evaluaciones de Decision API se conservan, incluidas las rondas desfavorables. No equivalen a verificación funcional ni aprobación del usuario. La publicación solicitada es una versión de prueba; no se afirma superado el objetivo formal de 4/5.
- Evidencia reproducible: `tools/interiores/casas_pruebas.py --tanda 5`, `validar.py --casas 200 --exigir-todas`, `integracion.py --colisiones` y `integracion.py --paquete`; informes en `data/interiores/validacion/` y fichas en `data/interiores/fichas/`.
- Se conservan las claves de guardado HQ, Evolución y fija. Las pruebas de partida, caja fuerte, siesta y decoración usan datos ficticios en contexto privado; no se modifican partidas reales del usuario.

## 2026-10-17 · calidad visual por tandas hasta 4/5

El usuario solicita mejorar primero las habitaciones peor puntuadas, composición y contraste, validar y desplegar cada tanda. Tanda 1: taller y baño. Se mantienen rúbrica, umbral y semillas; las capturas registran sus cámaras. Se añaden superficies serenas, revestimientos con huecos recortados, banco a escala doméstica, almacenaje de herramientas y detalle/contraste de lavabo, espejo y armario. La evaluación debe conservar resultados desfavorables y solo declarará 4/5 cuando ambos evaluadores lo alcancen.
