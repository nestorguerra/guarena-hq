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
