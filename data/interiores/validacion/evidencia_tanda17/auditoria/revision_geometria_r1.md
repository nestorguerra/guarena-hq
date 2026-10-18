# T17 · revisión de geometría y composición del estudio

Estado: revisión preliminar; pendiente del sello final del autor. Alcance: lectura de plantas y recibos CPU, y revisión estática de la base T16. Sin GPU, navegador, API, compilación, pruebas ejecutadas por este revisor ni cambios en producto. No es aprobación de modelos finales, integración, función en juego o calidad 4/5.

## Diseño frente a la base

La propuesta aborda el problema principal: el puesto deja de ser una mesa pequeña aislada detrás del sillón o junto a la puerta. Mesa, biblioteca y bajo forman un frente relacionado; la silla pertenece al puesto. No es una tanda de microdecoración. Los tres cuerpos suman 3,20 m de ancho nominal, más las separaciones de colocación.

- **3244, artista, real:** el frente se reúne al norte, con el bajo bajo la ventana y la biblioteca fuera del hueco. La lectura queda al suroeste con apoyo junto al sillón. El centro continúa amplio: la planta indica 8,77 m² alcanzables frente a 9,50 m² antes. Esa medida representa centros navegables, no superficie vacía ni densidad visual. No exigiría otro volumen antes de ver la perspectiva: el nuevo frente y los dos usos justifican comprobar la hipótesis. Si sigue pareciendo un perímetro de muebles alrededor de un vacío, habrá que relacionar espacialmente lectura y consulta, no añadir miniaturas.
- **1594, estudiante, real:** la propuesta utiliza la mesa amplia de 1,30 × 0,60 m, también aquí; no la compacta. La envolvente de la silla termina aproximadamente a 1,04 m de la pared opuesta. Los recibos sitúan silla y frente completos dentro del recinto de 4,36 × 2,15 m y conservan acceso de 0,80 m. Baja el área de centros alcanzables de 3,57 a 2,64 m². Esto no demuestra comodidad en primera persona: la prueba debe comprobar que se sigue entendiendo el tablero y que la biblioteca no reproduce la oclusión de la base.
- **1481, músico, canónica sintética:** trabajo y consulta pasan al oeste; lectura y apoyo quedan al este, fuera de la reserva de entrada. Es una hipótesis más coherente que la mesa aislada junto a la puerta de la base. La ventana norte permanece libre. Debe identificarse como fixture sintética, no como tercer estudio existente en el pueblo.

## Evidencia revisada y alcance

`fit.json` prueba ambos tamaños en los tres marcos originales: cadena completa, silla vinculada, sin errores geométricos. `full.json` reconstruye 22 identidades del inventario y 1481 sintética: sólo dos viviendas del pueblo contienen estudio. Registra marcos, luces, otras estancias, botín y tipos de acciones conservados; los tres estudios pasan el validador. Comprueba una superficie de escritura libre de 0,60 × 0,30 m. Los recibos son del autor; este revisor no ha ejecutado esos programas.

Los negativos cubren reserva total del recinto, libro flotante 4 cm, bloqueo de uso de biblioteca y puesto sin silla, con fallos esperados. El recibo de fallback preserva el resultado individual y la secuencia aleatoria de la **receta nueva** cuando falla su grupo; no demuestra volver a toda la receta anterior T16. Esa diferencia debe conservarse al describir una futura implementación.

Annie se comprueba en CPU con semillas 12 y 13: marco, acciones y los otros cuatro kits iguales según el recibo. Alcanza 60 mallas y 9 luces. No hay margen para sumar mallas o luces en modelos finales sin resolverlo; tampoco hay una comparación visible nueva de Annie aquí.

## Criterios concretos para la siguiente prueba

1. El tablero, la silla y el frente de consulta han de leerse como un puesto adulto utilizable. Evitar el aspecto de dormitorio infantil o despacho de oficina mediante programa y construcción final; la planta por sí sola no resuelve identidad.
2. En 3244, el sillón debe actuar como lectura secundaria, sin volver a tapar ni dominar el puesto. Evaluar si ambos grupos articulan la estancia desde el recorrido real, no llenar el centro por su área en planta.
3. En 1594, comprobar lectura del tablero y acceso aparente al asiento sin que el lateral alto de la biblioteca se convierta otra vez en pantalla. El ajuste físico CPU es necesario pero insuficiente para esta comprobación visual.
4. En 1481, comprobar que el frente oeste y la lectura este se perciben relacionados y que el acceso conserva una lectura clara; la evidencia no generaliza una tercera casa real.
5. La prueba gris permite juzgar masas, distancias y jerarquía, no variedad final, contraste de materiales ni acabado. El suelo jaspeado visible en la base sigue siendo un competidor relevante; cambiarlo no debe ocultar un fallo de composición. No alterar luces o cámaras para favorecer el resultado sin registrar la comparación.
6. El ordenador está incorporado geométricamente a la mesa de la propuesta gris. No tomar conservación de tipos de interacción como demostración de identidad, recogida o función independiente del ordenador. El modelo final deberá explicitar y verificar su comportamiento. Tampoco inferir colisiones, persistencia o acciones visibles a partir de la futura foto.

## Dictamen pendiente

La lectura preliminar no identifica un ajuste material imprescindible antes de probar estas masas en una copia aislada. La autorización de esa siguiente prueba queda pendiente de recibir y comprobar el sello final del autor; no autoriza integrar esta receta ni publicar.

## Adenda · entrega sin sello y alternativa de consulta posterior

La revisión precedente corresponde al ensayo con ordenador incorporado geométricamente al puesto. No llegó a sellarse: al comprobar el manifiesto `0d64b62c92be496dc8570d8ac914bad490c073e097138b7265b94a3091793086` había 7 discrepancias entre sus 42 entradas y los archivos, durante una modificación comunicada al autor. No constituye fallo de producto ni evidencia de fuentes finales congeladas.

Raíz comunica que al recuperar el ordenador como objeto separado, los intentos de 3244/1481 fallan por la reserva de ventana. Por tanto, las plantas y cifras anteriores quedan como evidencia histórica del ensayo integrado, no como recibos de una entrega válida con el ordenador separado. **No se aprueba todavía la captura del candidato.**

La alternativa de diseño propuesta por raíz es razonable para volver a comprobar CPU: un panel físico posterior de consulta/notas integrado en el puesto, con altura total aproximada de 1,20–1,25 m, dentro de la huella de la mesa. Puede aportar identidad adulta real —consulta de láminas, agenda de estudio o partituras— y evitar que el programa se sitúe bajo la ventana por su volumen físico. No debe ser una reserva invisible ni un tabique arbitrario para engañar la colocación.

Condiciones previas a cerrar ese diseño: conservar el rectángulo frontal utilizable de 0,60 × 0,30 m; mantener apoyo real y comportamiento independiente del ordenador; dejar suficiente panel visible por encima o al lado de la pantalla para que sirva de consulta; no estrechar el puesto, crear un borde que invada silla/circulación ni convertir el respaldo en otro mueble alto dominante. La anchura del panel debe venir de su uso, no copiar el tamaño del hueco que se intenta evitar. Se conservan los límites de lectura en 1594 y de vacío central en 3244. La alternativa aún no tiene aprobación geométrica ni visual por este revisor.

## Adenda final · sello estable y dictamen de siguiente prueba

**APROBADO para una captura privada del greybox en juego de las tres muestras 3244, 1594 y 1481.** No identifico un bloqueo concreto para esa prueba acotada. Esta conclusión sustituye únicamente el estado pendiente de las adendas anteriores; se conserva su historia. No aprueba integración, modelos finales, publicación, función en navegador ni calidad 4/5.

Se comprobó el manifiesto final contra los bytes de sus **45 archivos: 45 coinciden, cero discrepancias**. También coinciden los SHA de propuesta y parche comunicados por raíz. Se leyeron nuevamente los recibos finales y los instrumentos `crear_greybox.py`, `full.cpu.mjs` y `annie.cpu.mjs`; no se ejecutaron sus pruebas ni GPU durante esta revisión. El parche afecta exclusivamente a los dos JSON privados de catálogo B y kit estudio. La regeneración indicada es `tools/interiores/datos.py` dentro de la copia, sin copiar el compilado global privado ni ejecutar los generadores de catálogo/kit encima del parche.

| Artefacto final | SHA-256 |
|---|---|
| manifest.json | `63461d72a6baaa29da7968773a23c6dcb8b12eea96cc71b26938c0d615533f07` |
| propuesta_geometrica.md | `9a89aa8ff34db60e6328baa604439c508c473f700c8d30dfb6f90044354787da` |
| greybox.patch | `c4c924ba0ad1638c4d1d87140ea2c8a875a1f8e156b75b698ea838c4156619ee` |
| fit.json | `f01c4081eac316a0b8966e25749b49808afe8a6dd09db53b997f3c7942554cdd` |
| full.json | `fff7f2f2a60423e02a163227310dccbf44ed9ca4e6027720f4acb75a4328c352` |
| annie.json | `d993ba7d3683e6945ea4c47a19c88a70b1340fd01de96da6cc23dd2b8a74fc8b` |
| negativos.json | `464d0b79009323aa4bf721bb869d0bcd40a0544e6c7737416c2b95729f351fda` |
| fallback.json | `4b2f3984f1c566c109011095befa63faeda340aa062312cc789dde2e236942c1` |
| planta_comparacion.png | `12364befa0c97e0cb2ce97334070b154e3e78cb6e62fd4606e9814d07824717e` |
| base visual T16 casa_estudio.jpg | `d70efcfa6f89273d53a7cb6ed4c6f3a24fe1659bb56227e8b2a60c7adeca838e` |

### Qué resuelve esta versión

El puesto mantiene 1,30 × 0,60 m y añade un respaldo **físico** de consulta, con panel de 1,20 × 0,38 × 0,02 m y montantes que alcanzan 1,22 m. El panel está unido al tablero y su volumen participa en la colocación: no es una reserva invisible. Su altura intermedia y superficie útil ofrecen una identidad de estudio adulto más convincente que una mesa con monitor incorporado. La pantalla ocupa sólo parte de su anchura; la futura imagen debe confirmar la legibilidad de sus laterales y banda superior. El contenido del panel todavía no existe.

`vb_ordenador` conserva definición T16 y clase PICKUP, separado y apoyado en la mesa. El recibo final registra penetración cero con puesto/panel en las tres muestras; el negativo de desplazarlo 4 cm hacia atrás detecta 1,75 cm de penetración. El instrumento examina las piezas físicas, además del validador general que excluye pares hijo/soporte. Registra también el rectángulo libre de escritura de 0,60 × 0,30 m. Esto cierra la objeción geométrica del ensayo integrado para esta captura; no equivale a probar recogida/manipulación visible en navegador.

Las tres muestras amplias entran en el primer intento con semillas originales, sin cambiar W/D/H. **La compacta ya no forma parte de la candidata final**: las afirmaciones iniciales sobre seis combinaciones correspondían a otra sonda y no se transfieren a esta entrega. Se mantienen los dos estudios reales y 1481 sintética. La cadena final sigue ocupando el frente descrito en la planta; su anchura completa es 3,28 m incluidas juntas.

El opt-in por artista/estudiante/músico deja fuera a Annie. Su nuevo recibo comprueba igualdad de cinco estancias, receta efectiva, geometrías/poses/materiales representados en CPU, colliders y acciones/posiciones frente a T16 en semillas 12/13. Esto sustituye el anterior ensayo donde cambiaba su estudio. Canvas sin raster no acredita píxeles de texturas ni comportamiento animado; tampoco hace falta una nueva apariencia de Annie para juzgar la composición de estas tres muestras.

### Condiciones y límites que permanecen

- **3244:** mantener el ensayo sin añadir otro volumen al centro. El frente y el ámbito de lectura ya justifican probar una mejora de organización. La captura decidirá si el centro se percibe articulado o si permanece el vacío dominante de T16; no inferir densidad visual del área navegable.
- **1594:** evaluar desde el recorrido real el tablero, el asiento y el lateral alto junto a la mesa. La mesa amplia cabe según CPU, pero sólo la perspectiva dirá si se percibe como puesto cómodo o si la biblioteca vuelve a ocultarlo.
- **1481:** evaluar relación trabajo–lectura y acceso. Conservar identificación de fixture sintética y no presentarla como tercera casa real.
- Capturar esta alternativa única con procedencia y guardas físicas. Si alguna pose base ya no es válida, documentar el cambio; no forzar una cámara dentro del mobiliario ni atribuir causalidad exacta a imágenes con poses diferentes. Una combinación con acabado R2/caller de raíz sería otra variante y debe identificarse como tal.
- Los volúmenes grises no permiten aprobar contraste, densidad de baldas, variedad por perfil o identidad gráfica del panel. Suelo jaspeado, jerarquía del sillón y semejanza con despacho/niños siguen siendo preguntas visibles, no problemas declarados resueltos por CPU.
- **Producción sigue pendiente:** el fallback de un perfil optante cuando no cabe el frente continúa siendo el individual de la receta nueva; no retorna íntegramente a T16. Los negativos lo dejan fallar honestamente. Debe cerrarse antes de una integración general, pero no impide observar estas tres muestras que sí tienen programa completo. No hay selector amplio→compacto aprobado.
- El presupuesto leído corresponde al greybox (56/58/58 mallas y ocho luces en las tres muestras). No acredita coste de baldas o contenidos finales, FPS, persistencia o interacción real. Annie queda igual, con su presupuesto existente; no se le concede margen adicional.

No se han modificado fuentes activas, ejecutado captura ni realizado llamadas de evaluación formal. La siguiente acción admitida por este dictamen es exclusivamente observar el greybox aislado; el resultado visual puede exigir cambiar el diseño.
