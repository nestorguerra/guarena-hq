# Revisión independiente de la tanda 10

Alcance: composición y acabados de cocina, baño y trastero. La luz cenital ensayada se rechaza y queda fuera del código publicado.

# Revisión independiente de código — tanda 10

Dictamen: **sin hallazgos P1/P2 identificados** en el diff activo de composición de baño, cocina y trastero. Aceptación estática de este alcance; no certifica calidad visual, rendimiento ni publicación. La luz cenital candidata y sus contratos `tanda >= 13` quedan excluidos.

## Alcance y comprobaciones

- `src/locales.js:509–568`: los acompañantes opcionales sólo entran en grupos si son preferidos `[0,1]`; la raíz sigue obligatoria y cada miembro debe referir al inmediato anterior. La prueba no modifica colocaciones, cursores ni el RNG compartido hasta que todas las piezas y accesos pasan. Si falla, continúan las reglas individuales, con sus mínimos y `si_no` originales.
- `src/locales.js:542–557`: la reserva lateral calcula el mismo origen, orientación y ajuste a pared que `junto_a` (líneas 177–197), también para las cuatro orientaciones y cajas no centradas. Comprueba zonas, huecos, muebles del grupo y paso antes del commit. No añade una pieza falsa a la salida ni modifica el recuento. En el baño actual, el toallero se coloca inmediatamente después del grupo: no hay una entrada intermedia que pueda consumir su hueco.
- `tools/interiores/kits_vivienda_a.py`: las dos agrupaciones del baño son independientes; la pequeña superficie conserva su alternativa. Los opcionales no se vuelven obligatorios en la validación general. El espacio frontal del WC se mantiene. En trastero, la pertenencia requerida busca adyacencia y conserva otra pared como fallback; la segunda estantería puede referenciar la pertenencia o la primera estantería.
- `src/houses.js:1138–1140` y `src/acabados_vivienda.js:41–55`: sólo el baño aplaza el acabado hasta conocer el lavabo colocado. Su orientación local identifica la pared correcta; el acabado no altera piezas, aberturas, reservas ni RNG de mobiliario. Sin estancia/lavabo amplio se conserva el acabado anterior, incluido el llamante de Annie.
- Cocina: filtros de estilos excluyentes y rangos de superficie complementarios. El alto requiere su encimera del ancho correspondiente (`sobre_de`, `si_no:false`), sin colocación huérfana. Nuevos cuerpos, estantes y vajilla mantienen apoyos y dimensiones compatibles; materiales se generan por el mismo mecanismo de tintado. No se introducen luces ni comportamiento de interacción.
- Schema: `reserva_lateral` es opt-in, cerrada a `obj`/`lado` y sin cambios a kits que no la usan. La referencia concreta `va_toallero` existe y es de pared. Limitación de robustez para futuras autorías: `datos.py` no valida la existencia de esta nueva referencia; un ID erróneo rechazaría el grupo y activaría el fallback. No afecta a los datos actuales ni constituye aquí un bloqueo.

## Evidencia y límites

Leídos los contratos actuales: fallback/RNG de grupo opcional, control negativo sin reserva lateral, baños reales, altos por siete estilos y dos tamaños, hueco de ventana/alto huérfano, adyacencia y fallback del trastero. No he repetido ensayos ni regenerado datos.

El artefacto de esta tanda `.cache/calidad/tanda10/contratos.json` contiene 45 pruebas, estados ['PASS'], errores []. El manifiesto `.cache/calidad/tanda10/regeneracion.json` registra 21 archivos y cambios []; he cotejado sus hashes contra los archivos actuales: todos coinciden. Esto verifica correspondencia de evidencia, no una nueva ejecución independiente.

La prueba específica de reserva lateral cubre N; su equivalencia en las otras orientaciones se ha revisado en las fórmulas, sin ampliar ejecuciones. La reserva es una precondición del grupo, no una garantía persistente para futuros kits con entradas intermedias. No se exige invariancia de distribución respecto a la tanda anterior: cambia el orden de colocación del trastero deliberadamente; sí se conserva reproducibilidad por semilla.

**Declined to judge:** nota estética 4/5; sombras/estrías de la propuesta cenital rechazada; calidad de las fichas/cámaras; cobertura exhaustiva de todas las plantas y semillas; FPS; despliegue y estado público. Ningún navegador/GPU ni modificación de fuentes durante esta revisión.

## Identidad de la revisión

HEAD de comparación: `6186c7ba99ca0a8dafa2690a4aaa5873822329d1`. Revisión del árbol de trabajo, no de un rango vacío de commits. SHA-256 de las fuentes/datos leídos:

```json
{
  "src/locales.js": "9ed8c8ae0a22886f2124ff405efeb1bc5888ae09344abfc62b5fc8625159ad3c",
  "src/houses.js": "a668db5692eab1f6ec780eeca0721bfee14c6778527eef62fae4974821ae52de",
  "src/acabados_vivienda.js": "75a252da1bed44b62c0ac3139e67f021e70ebb121d027bac51472a168ff41a1f",
  "tools/interiores/kits_vivienda_a.py": "f786ef2e7fdff65632bcba5d145ef9450a7178dfa09dd26b2ee279917ca237ce",
  "tools/interiores/composicion_domestica.py": "8d74bdbda14dc3b4ee6729e4985ec0e03673656d524a2a23b5c068b0a4d3656f",
  "tools/interiores/casas_pruebas.js": "3390b58f1a80fb3bbc5fc118fd3921be7bc15849400e17bb0ec833f208e72d97",
  "data/kits/kit.schema.json": "d3614c6580654c8bd30f4e882e6084f9502aec71d71d6e09d453d2bf28f24612",
  "data/kits/vivienda_bano.json": "5aba80f9775608db25c74d2ee2095061c5e638961366ecda3b70242bb94b6362",
  "data/kits/vivienda_cocina.json": "8231d11513e52e3a29a29e55eaf23f3a85652fb52a0ac6b8a6017b2ad854bb2e",
  "data/kits/vivienda_trastero.json": "970f68da349d8d640d2809495102770bb7445b77addd322834c3d5f58196206b",
  "data/objetos/vivienda_a.json": "50269ab7a132920728b2c470057755abba7be6dc6bf11a8e56b895307174667c",
  "src/interiores_datos.js": "0c07a1cd0f786a72932e5422e89552675cd7a72ec0d5495749ef6afa1f7bf710"
}
```

---

# Tanda 10 — cierre visual independiente

17 de octubre de 2026. Reabierta la ficha final de baño de las 20:45:32 y su JSON. Cocina y trastero conservan exactamente los hashes de la revisión parcial; mantienen sus observaciones y límites. No se ha aplicado luz cenital en estas fichas. Inspección mediante archivos, sin GPU, juego, nuevas pruebas ni notas formales; revisor distinto de los autores de los cambios.

**Aprobación cualitativa acotada de la tanda, con cobertura parcial declarada.** No se observa un defecto nuevo demostrado de geometría o distribución que bloquee este cierre. No equivale a resolver los vacíos de planta, acreditar todos los accesos o alcanzar el objetivo formal de calidad.

## Evidencia final

Directorio `/Users/nestorguerra/Proyectos Vibe/Guarena HQ/data/interiores/fichas/`.

| Archivo | SHA-256 |
|---|---|
| casa_bano.jpg | 466d6c857698e54714834d731efb1ac227957d877b14363a5c5adbb3ef653b38 |
| casa_bano.json | fbcc51c3e4db9e3031df89f43c084deafcee14df4667762df32fe1b8d14bfddd |
| casa_cocina.jpg | 9fa9b7494291de50566f7ff4af2685e8c3b1357f281f16924bfae487f7204020 |
| casa_cocina.json | 2d84be58594101a5a8dd95d0df7785743029787f789be521f9a3df4911f70351 |
| casa_trastero.jpg | c17a6c0f53787eb39300614fd236d97177d9f97d6ef3a5559aeddf0cd8a637a7 |
| casa_trastero.json | 3c29571bd234afa25da4b7890728f4f44fee5bc2d7dfa3916a4e26da9659e61f |

## Baño final

- **2786:** conserva el aseo compacto reconocible. Las vistas muestran lavabo/espejo/toalla y el otro conjunto de ducha/WC/almacenaje. No aparece un nuevo elemento claramente suspendido o una pieza principal tapada por el armario.
- **3244:** lavabo, espejo, toalla y armario se leen ahora como un frente. La ducha está relacionada con ese grupo y la bañera se reconoce en primer plano; el WC queda visible al fondo de la general. El paño principal y los secundarios claros ordenan mejor el color. Persiste un vacío grande y alargado entre grupos, coherente con los aproximadamente 15,7 m² documentados. No se presenta como una habitación proporcionada por haber agrupado los sanitarios.
- **1594:** la unión lavabo/espejo/armario es clara y la toalla queda visible a su lado. La general permite entender la relación con zona de baño y WC. La separación cromática del frente de aseo aporta jerarquía, aunque la superficie libre continúa siendo amplia.

**Límite de captura:** la bañera de 3244 queda parcial en las dos imágenes, con un recorte importante en la general; no se afirma inspección completa de toda su silueta. Las piezas cercanas al borde en la general de 1594 también tienen recortes. No se infiere un problema de acceso o colisión por esos recortes. La visibilidad de la toalla no verifica por sí sola su reserva lateral ni la ruta de uso; esos aspectos corresponden a posiciones y contratos, no a la fotografía.

## Cocina y trastero: alcance conservado

Se mantiene la revisión `.cache/calidad/tanda10_revision_visual_parcial.md`: altos de cocina mejor proporcionados y distintos, madera coherente y leve pérdida de contraste en frentes claros sin borrar funciones. La esquina de almacenaje del trastero mejora la composición.

La bicicleta de trastero 3886 no queda completa entre sus dos vistas. El volcado de posiciones no muestra solapamiento con la estantería contigua ni ocupación de la banda frontal diagnóstica; no hay bloqueo físico demostrado. Tampoco existe un contrato/interacción específica de uso o extracción de bicicleta que se pueda dar por validado. Las tres muestras siguen siendo estudiante/joven; no representan otros perfiles o la escalera.

El cierre se limita a estas capturas diurnas en Plastilina, alta y DPR 1. No certifica noche/apagón, movimiento, todas las semillas, segunda estética o rendimiento. No se han repetido las comprobaciones del constructor. Las carencias estructurales de tamaño/programa y los límites de evidencia permanecen documentados, sin exigir otra tanda de pruebas por un defecto que no se ha demostrado aquí.

---

# Tanda 10 — revisión visual parcial independiente

17 de octubre de 2026. Examinadas las fichas nuevas de cocina y trastero, sus JSON y el volcado de posiciones disponible. El baño sigue en corrección y no se evalúa aquí. Revisión mediante imágenes/archivos locales, sin juego, GPU, nuevas pruebas o notas formales. El revisor no es autor de los cambios de modelos/colocación.

**Resultado:** aprobación cualitativa acotada de cocina y de la mejora de esquina del trastero. No identifico un bloqueo físico demostrado en 3886; sí una limitación de cobertura que impide describir su bicicleta como completamente visible. No se atribuye el objetivo formal de calidad.

## Archivos inspeccionados

Rutas bajo `/Users/nestorguerra/Proyectos Vibe/Guarena HQ`.

| Archivo | SHA-256 |
|---|---|
| data/interiores/fichas/casa_cocina.jpg, 20:34:34 | 9fa9b7494291de50566f7ff4af2685e8c3b1357f281f16924bfae487f7204020 |
| data/interiores/fichas/casa_cocina.json | 2d84be58594101a5a8dd95d0df7785743029787f789be521f9a3df4911f70351 |
| data/interiores/fichas/casa_trastero.jpg, 20:34:47 | c17a6c0f53787eb39300614fd236d97177d9f97d6ef3a5559aeddf0cd8a637a7 |
| data/interiores/fichas/casa_trastero.json | 3c29571bd234afa25da4b7890728f4f44fee5bc2d7dfa3916a4e26da9659e61f |
| .cache/calidad/tanda10_trastero_posiciones.json | 7b1f02f8c1f7b9f05509dfb0a1f4e9d998dfa573e2910ddb0d8f32e143bd94e9 |

La comparación anterior corresponde a las fichas de tanda 9 ya examinadas: cocina 287501f5259e37f60ea756e67fac90721be53df740990341d6a544ce7fa1d53f y trastero 79cd1821f201fd3ad53c01dedb80062566d11ace095a79544cf2eca031fbdd14. Cocina conserva las cámaras; trastero cambia vistas, por lo que no se aísla el efecto de composición de su cobertura.

## Cocina

- Los altos tienen ahora anchura más acorde con la preparación amplia. El rústico muestra puertas con bastidor, el bohemio combina hueco abierto y puerta, y el joven usa un frente liso. La diferencia de almacenamiento se ve en las generales sin añadir desorden al suelo.
- La madera oscura relaciona mejor los muebles rústicos con la alacena. En artista/joven, el frente claro pierde parte del contraste anterior entre carcasa y puerta verde, pero encimera, tiradores, juntas y fogones siguen separando las funciones. No se observa una pérdida importante de lectura que bloquee esta versión.
- Se mantiene el frente bajo legible. Las dos vistas cubren fogones, fregadero, preparación y nevera, con los mismos recortes secundarios de la general compacta y sillas en el borde inferior de las grandes. No veo un objeto principal claramente flotando ni un hueco nuevo importante entre módulos.
- Persisten paños altos bastante extensos. El alto mejora proporción y variedad; no resuelve el tamaño de las cocinas grandes por sí solo.

## Trastero

La esquina con estanterías y bicicleta se entiende como un conjunto de guardado más continuo. Las masas altas ayudan a enmarcar la pertenencia baja y el centro se lee mejor como paso. En 1594 y 4589 la combinación de vistas permite reconocer bicicleta, almacenaje y relación con puerta/ventana. El espacio libre sigue siendo generoso; la nueva composición no cambia las dimensiones de la sala.

### 3886: cobertura limitada, sin bloqueo físico demostrado

En la primera vista, una estantería muy próxima oculta parte de la bicicleta. La segunda explica el almacenaje, pero no recupera completa la bici. **No se afirma cobertura visual completa de ese objeto entre ambas imágenes.**

El volcado exacto permite separar esa oclusión de una colisión. En coordenadas locales de la estancia:

- Huella de bicicleta: X de −2,37356 a −0,83250; Z de 0,01 a 0,48 m.
- Estantería contigua: X de −0,79250 a 0,38750; Z de 0,01 a 0,46 m. Hay unos 0,04 m de separación lateral; no se solapan sus huellas.
- Una banda diagnóstica de 0,80 m delante de la bicicleta, con su anchura completa y Z de 0,48 a 1,28 m, no intersecta las huellas de estanterías, cajas o cesto registradas. Es una comprobación aritmética del volcado, no una nueva ejecución del validador o del juego.

La estantería está al lado del objeto en la planta y delante de la cámara en la imagen. No hay evidencia aquí de que bloquee físicamente la bicicleta o su frente. **El sistema no declara una reserva específica ni una interacción de uso/extracción de bicicleta**; por tanto, tampoco se da esa usabilidad por verificada. No confundir ausencia de solapamiento con un contrato funcional que no existe.

No se solicita una nueva captura en esta revisión parcial. Si posteriormente se exige mostrar íntegra la bicicleta de 3886, hará falta un ángulo adicional o corregido que documente el objeto sin ocultar el resto de la planta; sería una mejora de evidencia, no una mejora automática del juego o de su nota.

## Cobertura y límite global

Las tres muestras de trastero siguen siendo estudiante/joven y muestran bicicleta. No prueban variedad de otros perfiles, escalera o estilos. Posteriormente puede auditarse el inventario real y añadir la primera semilla determinista de cada otro perfil con trastero que efectivamente exista, conservando estas tres. Eso ampliaría evidencia; no se presentaría como una mejora del contenido ni se sustituirían casos desfavorables.

Este cierre no evalúa el baño nuevo, noche, apagón, movimiento, todas las semillas, accesos no contratados o rendimiento. La causa de dimensiones/programa se documenta aparte en `.cache/calidad/diagnostico_composicion_global.md`. No hay un hallazgo visible o geométrico demostrado en esta inspección que obligue a ampliar pruebas de la tanda parcial.
