# T17 — propuesta geométrica privada de estudio sobre T16

**Un frente de trabajo con consulta física en altura, una biblioteca y guardado bajo; lectura secundaria cuando quepa.** La alternativa final conserva el ordenador independiente y cabe en las tres muestras con los marcos originales. Es un greybox para revisión, no una candidata de producción ni una aprobación visual.

## Alternativa final, única

La cadena existente `grupo_pared` prueba **mesa → biblioteca → bajo y silla frontal** antes de colocar sus piezas. No se ha modificado el motor. El frente mide 3,28 m: mesa de 1,30×0,60 m y tablero a 0,75 m; biblioteca de 1,00×0,34×1,70 m; bajo de 0,90×0,35×0,78 m; dos juntas de 0,04 m.

El puesto incorpora un **respaldo real de consulta a 1,22 m**, unido al tablero mediante dos montantes. El panel mide 1,20×0,38×0,02 m. Tiene una función visible propuesta —notas, bocetos o partituras— y dimensiones domésticas iguales para todos los casos. No es un volumen fantasma ni una anchura adaptada a ventanas. El grupo comprueba así la altura física del puesto antes de comprometerlo.

`vb_ordenador` sigue como objeto separado, con la definición T16 exacta, clase PICKUP y apoyo sobre una banda posterior real del tablero. No se integra su geometría en la mesa. No penetra el panel ni los montantes. Delante queda una superficie continua libre de **0,60×0,30 m**, suficiente para A3 apaisado. El monitor ocupa 0,38 m de los 1,20 m de ancho del panel: quedan dos laterales de unos0,41 m y una banda superior visibles. El contenido del panel aún no está modelado.

Sólo hay una biblioteca alta. En3244 la segunda acción `read` se conserva con consulta baja sobre el aparador, en lugar de otra biblioteca. El bajo pasa a ser parte obligatoria del programa y sustituye su dispersión opcional anterior. Biblioteca y bajo conservan frentes libres de0,75×0,80 y0,70×0,80 m. No se admiten adornos aleatorios sobre el puesto y se retira el ordenador del pool decorativo.

El sillón queda subordinado: se intenta en la pared opuesta al trabajo, desde11 m² como en la base y sin buscar otra pared si no cabe. Mesita de lectura existente y libro apoyado sólo se intentan junto a él. En3244 mira hacia la ventana norte, fuera del frente de trabajo. En1481 forma un segundo ámbito en la pared opuesta; en1594 se omite. **La planta organiza dos usos, pero la jerarquía y el vacío central de3244 siguen pendientes de perspectiva real.** No se añaden adornos para llenar ese suelo.

| Semilla | Procedencia y perfil | Marco útil W×D×H (m) | Frente final | Lectura | Mallas T16/gris |
|---|---|---|---|---|---|
| 3244 | Pueblo, artista | 5,4693×3,3143×2,75 | N; intento0, seed425071 | S, sillón+mesita+libro | 56/56 |
| 1594 | Pueblo, estudiante | 4,3609×2,1500×2,75 | N; intento0, seed208904 | Omitida | 58/58 |
| 1481 | Sintética, músico | 4,1611×3,4125×2,75 | W; intento0, seed194118 | E, sillón+mesita+libro | 58/58 |

La mesa ofrece un82% más de tablero que la actual de0,95×0,45 m. Ese porcentaje describe geometría, no calidad. El ID del greybox es `t17_mesa_amplio`; el nombre previsto para producción es `vb_puesto_estudio_amplio`, pendiente del modelo final. La compacta queda sólo en el histórico: no forma parte de esta alternativa final.

## Identidad del programa

- Estudiante: apuntes en la superficie frontal y material de consulta a mano; panel con notas de trabajo y guardado de carpetas. Escala adulta, no cuarto infantil con otra paleta.
- Artista: bocetos A3 y consulta gráfica; panel de referencia propio y carpetas planas en el bajo, sin añadir caballete ni repetir la sala de pintura.
- Músico: lectura/escritura de partituras, consulta en el panel y orden de carpetas/partituras en la biblioteca; sin otro instrumento.

La diferencia final debe cambiar organización y masas de trabajo/guardado dentro de esta envolvente, no limitarse a tres miniaturas o colores. Los contenidos y baldas finales aún no existen; las cajas de biblioteca y bajo son conservadoras. La planta señala la superficie útil, no una textura ya creada.

## Opt-in y conservación de Annie

El programa nuevo es declarativo y exclusivo de **artista/estudiante/musico**, los tres perfiles que tienen estudio en `PROFILES`. La receta T16 completa queda primero y se mantiene para los demás contextos mediante los filtros existentes. No hay condición por semilla, cámara o nombre de Annie, ni cambio de solver. Los otros kits y sus pools no cambian; ningún ID nuevo entra en ellos.

La aplicación indiscriminada anterior produjo un **RED en Annie por uso frontal del bajo**. Se conserva en `hist_sonda8_respaldo_sin_optin/` y `annie_respaldo_sin_optin_RED.json`; no se transfiere el PASS de la primera sonda integrada a esta versión. El acabado de raíz también queda fuera del alcance singular.

La versión final reconstruye Annie12/13 con la fuente corregida7364d55 y comprueba **cinco estancias/receta efectiva, acciones y posiciones, geometrías/poses/materiales y colliders exactamente iguales a T16**. Ambas conservan60 mallas/9 luces. No se acredita apariencia de texturas mediante Canvas sin raster, ni animación de manipulación del ordenador en navegador.

## Evidencia CPU literal

`base.json` conserva el sello de las fuentes activas verificadas T16, no un checkout del viejo HEAD. Al iniciar, HEAD aún era e9022e4; al cerrar se cotejan otra vez los archivos críticos activos contra sus bytes. La publicación posterior288e24e de raíz no reescribe esta procedencia. Se ejecutaron cinco generadores actuales en copia: sus JSON base coinciden con T16, sin copiar compilados antiguos.

El inventario de pueblo tiene **22 identidades y sólo dos estudios:3244/1594**. Se reconstruyeron las22 con el constructor literal y se añadió1481 como canónica sintética. No se afirma una cohorte de31 estudios reales. Las otras20 casas son controles sin estudio.

- `full.json`:23 casas completas; validadores reales de estancia y uso sin errores; paso0,80 m, apoyos e interpenetraciones. Marcos/rooms y otras estancias exactos; botín, definiciones/poses y acciones del estudio conservados; luces físicas exactas. Máximo59 mallas en la cohorte.
- `fit.json`:tres combinaciones finales, primer intento en todas; W/D/H, inicio y huecos fijos. No hay wrapper que redimensione al reintentar.
- `annie.json`:T16 exacta en los términos anteriores, y otros kits/pools sin IDs nuevos.
- `negativos.json`:recinto completo reservado agota12 intentos del `buildLocal` literal con marco/puerta fijos y errores reales de mínimos; elevar el libro4 cm produce error de apoyo; bloquear el frente de biblioteca produce error de uso; retirar la silla produce error de vínculo.
- `full.json` añade un negativo geométrico no vacío: desplazar el ordenador4 cm hacia atrás lo introduce1,75 cm en el panel; el oráculo lo rechaza. En las tres muestras finales la penetración real ordenador/puesto es0. Este control importa porque el validador general excluye del test de colisión las parejas hijo/soporte.
- `datos_greybox.log`:validación de datos completa y compilado privado desde los JSON actuales, sin errores.

El mapa de cuerpo0,80 m pasa de9,50 a8,77 m² alcanzables en3244; de3,57 a2,64 en1594; y de6,36 a5,94 en1481. Es suelo disponible al cuerpo, no una puntuación ni ocupación visual. En1594 aumenta la superficie de trabajo y sigue pasando la circulación; su proporción debe verse en el juego.

Se usan THREE r170, constructor, agrupación, geometrías/collider y validadores reales; Canvas no rasteriza. **Los recuentos corresponden al greybox, no garantizan el coste de baldas/contenidos finales.** Annie ya tiene60 mallas. No hay medida GPU, FPS ni aprobación de materiales.

## Fallback y fallos conservados

El motor actual conserva sus reglas individuales y RNG si falla el grupo. `fallback.json` compara ese fallo con la misma receta nueva sin grupo: P no vacío y tres extracciones U siguientes son idénticos. El recinto totalmente bloqueado sigue fallando.

**No se implementa todavía un retorno geométrico completo a T16 para un perfil optante cuyo frente no quepa.** El fallback por contexto no optante sí conserva T16, como demuestra Annie; no debe confundirse con un selector amplio→compacto. Antes de producción se deberá cerrar la conservación completa ante no-fit, sin ampliar el solver ni inferir fit sólo por área. Esta entrega permite probar masas de las tres muestras; no da cobertura universal ni autoriza integrar una receta definitiva.

Los históricos conservan grupo de dos que dejaba al bajo fuera, ordenador integrado, banda posterior de20 cm insuficiente para el ordenador asimétrico, ordenador separado que agotaba12 intentos bajo ventana y una plataforma lateral funcional que sí cabía. La alternativa final única es el respaldo de consulta acordado; no se seguirán sondeando posiciones pequeñas. La vieja anotación `lowLinked=false` de sonda2 usaba incorrectamente `de` para `junto_a` individual: esa regla no escribe ese índice. El primer instrumento negativo también corrigió un nombre de metadata, sin modificar el producto.

## Entrega y límites siguientes

`planta_comparacion.png/svg` y `propuesta_geometrica.md` son los artefactos de revisión. `greybox.patch` sólo añade los objetos grises y receta JSON a una copia T16; no es parche de producción de generadores. `LEEME.md` explica cómo regenerar los datos únicamente en la copia privada. `manifest.json` sella los archivos finales.

No se han tocado fuentes activas, luces, cámaras, marcos, puertas/ventanas, acabados ni exclusión de zócalo. El acabado R2/caller diferido de raíz no se incluye en los costes o plantas y requerirá comprobación combinada. La base visual sigue siendo `../captura_base_T16/casa_estudio.jpg`, SHA d70efcfa6f89273d53a7cb6ed4c6f3a24fe1659bb56227e8b2a60c7adeca838e; no hay captura nueva de juego.

Se solicita revisión independiente de esta propuesta estable antes de verla en una copia privada. Pendientes: perspectiva/jerarquía de3244, lectura del puesto1594, identidad de panel y contenidos, modelos finales/presupuesto y fallback completo de no-fit. Sin GPU, navegador, API, build, puntuación, commit ni publicación.
