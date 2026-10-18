# T20 · diagnóstico privado de dormitorio (dorm / dorm2)

**Recomendación:** componer descanso–guardado y una zona de lectura únicamente en salas amplias, con cama y fondo de mayor contraste. El problema visible combina uso poco articulado, exceso de superficies estampadas y modelos demasiado semejantes en color. Añadir más miniaturas o aumentar luz no resolvería esas causas. Propuesta pendiente de implementación, revisión y escenas reales; no supone calidad aprobada ni predice alcanzar el objetivo.

## Evidencia y procedencia

Inspeccionadas directamente con view_image las doce vistas locales: `casa_dorm.jpg` (2786 matrimonio/rústico, 3244 artista/bohemio, 1689 agricultor/rústico; dos vistas por casa) y `casa_dorm2.jpg` (1689 agricultor, 2132 cazador y 5157 matrimonio; dos vistas). JSON leídos completos.

La ficha dorm se escribió el 17-10 a las 20:51 y coincide por SHA con los juicios A/B `visual_dormitorio_*.json`, fechados a las 18:53 UTC. Sus dimensiones débiles son densidad y lectura funcional. Los juicios contienen valores agregados, no explicaciones de causas: las observaciones siguientes proceden de esta inspección, no se atribuyen al modelo evaluador. No se ha emitido puntuación nueva.

La ficha dorm2 es anterior (17-10, 16:16); su JSON no conserva cámaras/FOV/calidad/DPR. No está incluida en esos juicios formales. Las imágenes siguen disponibles, pero **no certifican el render T18 actual**: después hubo cambios compartidos de luz/material y sillón. Dorm sí registra FOV 68 y altura 1,6 m; no se sustituirá por una cámara más favorable para aparentar mejora.

Fuentes: rúbrica doméstica `data/interiors_review.json`; reglas `CLAUDE.md`, `docs/interiores.md` y plan de habitaciones; dirección artesanal `docs/plastilina.md` §2; kit B, catálogo B, acabados, locales y houses actuales. La dirección pide formas blandas, colores de cal/ocre/teja/verde y luz doméstica suave, manteniendo controles y lectura. No pide fotografía ni superficies blancas uniformes.

## Tres causas concretas

1. **En la sala amplia falta una composición de usos, no una lista de muebles.** En ambas vistas de 3244 (7,9×5,6m) cama, mesitas, armario claro, cómoda, sillón verde y estantería se concentran junto a la ventana. La alfombra pequeña queda separada en una extensa superficie residual. La estantería aparece vacía. El código explica parte de ello: escritorio/silla/librería son opcionales independientes desde 22 m²; sillón desde 16 m²; alfombra `suelo_libre` desde 26 m², sin relación con cama o lectura. El pool de objetos personales sólo usa mesita/cómoda/escritorio: **no llena la librería**, cuyo modelo sólo contiene carcasa y baldas. No se demuestra que escritorio y silla falten: podrían estar fuera de ambos planos. Se demuestra que estas vistas no articulan una segunda función creíble.

2. **El descanso pierde jerarquía por color y silueta.** En 2786 y 1689 dorm, y 1689/2132 dorm2, el gran plano de la colcha se lee casi del mismo marrón que bastidor, armario y cajonera. Almohadas claras identifican la cama, pero el bloque inferior y la tapa rígida dominan sobre su lectura textil. El código usa cajas rectas para base/colchón/cobertor y `tinte:tela` para colchón y colcha; la paleta doméstica puede aproximarse demasiado a la madera. Es un diagnóstico de lectura material, no un defecto de descanso demostrado. Las huellas de plastilina se conservan; no hace falta sustituirlas por tejido fotográfico.

3. **Pared/suelo compiten con el mobiliario y la decoración se escoge sin una relación doméstica clara.** El dorm2 de 5157 combina círculos azules grandes en todo el zócalo y baldosa geométrica de alto contraste. Los demás compactos repiten baldosa naranja con juntas muy blancas y paredes jaspeadas beige. En 2786 se repiten imagen devocional y cartel de feria; en 2132 aparece una portada genérica. Son objetos presentes, no recortes de cámara. La selección mural actual es `[1,3]` piezas de un pool mixto, sin `sobre_de`; la variedad por perfil no garantiza un paño de descanso distinto y coherente. Dormitorios aún no tienen rama propia en `revestirEstancia`.

## Programa funcional y propuesta acotada

**Base común:** conservar número/tipo de camas vigente, mesita relacionada, armario para hide y cómoda con cajones si la receta la admite; sueño de residentes, salida de cama y ahorros bajo colchón cuando correspondan. Dorm principal mantiene doble 1,35 m y amplia 1,60 m en sus rangos actuales; dorm2 conserva selección individual/doble. No se decide ocupación por las tres fichas ni se cambia una cama doble por individual para ganar suelo.

**Compacto:** mantener cama–mesita; relacionar armario y cómoda en un mismo paño mediante reglas existentes y reserva frontal, sólo donde cabe sin invadir puertas/ventanas ni desplazar la cama para la foto. Un único conjunto mural a escala doméstica, vinculado a cama o cómoda, sustituye la lotería de carteles repetidos. Nada de sumar otro escritorio/sillón para llenar la sala. Mantener la ruta anterior si no cabe la relación completa, sin perder cajones o hide por decorar.

**Amplio:** separar dos conjuntos reconocibles: descanso y guardado/lectura. Relacionar el sillón con librería y una superficie pequeña existente, con espacio corporal para sentarse y consultar. Poner algunos volúmenes de libros legibles sobre sus baldas reales, no hileras de perfumes o seis objetos en cada mesita. Anclar la alfombra a ese uso o a los pies de cama con una posición legal; no dejarla como isla aleatoria. Un puesto de escritorio ya aceptado debe conservar silla y uso; no se elimina a ciegas ni se duplica automáticamente el estudio de la casa. No convertir esta propuesta en un nuevo solver: usar `grupo_pared`, `junto_a`, `enfrente`, apoyos y reservas existentes, rechazando la receta incompleta.

**Contraste/modelo en el mismo alcance:** suelo de junta discreta o tabla ancha según estilo; cal crema en paños secundarios y un paño de descanso ligado al giro real de cama. Recortar huecos con `panosPared`. Colcha oliva/azul petróleo/teja moderada separada de madera cálida y una banda de sábana crema; más claro no equivale a todo blanco. Si se reedita la cama, ablandar colchón/cobertor y distinguir bastidor con su misma huella, altura, patas y anclas, mediante variantes exclusivas del dormitorio o override material acotado. No modificar a ciegas `vb_cama_individual` o `sillon_orejero`, compartidos con otros kits; no añadir geometría de pliegues pequeños como intervención principal. Conservar objetos existentes y agrupar materiales; presupuesto real de casa pendiente de recostear, sin prometer coste cero.

Archivos previstos: `tools/interiores/kits_vivienda_b.py` (sólo receta dormitorio), `tools/interiores/catalogo_vivienda_b.py` si hay variantes adultas propias, y `src/acabados_vivienda.js` para dorm/dorm2 exclusivamente; `src/houses.js` sólo si hace falta un override textil por estancia, sin tocar motor de luz. Derivados únicamente tras revisión. Annie queda fuera de lectura funcional, propuesta y cambios.

## Límites y cobertura necesaria

- Las puertas próximas a cámara ocultan parte de 1689/5157 dorm2. No se interpreta fuera de plano como ausente ni se diagnostica una colisión desde una foto. Falta volcado actual de posiciones para saber dónde quedan escritorio/silla, puntos de uso y reservas.
- Estas seis identidades no cubren todos los perfiles/estilos, una cama individual de dorm2, habitación mínima del laboratorio ni noche/apagón. Sólo 3244 representa planta alta/gran tamaño. No se ha abierto Realista en esta inspección. No hay escenas nuevas ni ensayo funcional.
- Antes de decidir integrar: recapturar mismas semillas y, cuando sean seguras, poses actuales; si una cámara histórica ocupa un objeto, documentar desigualdad en vez de mover muebles. Mostrar frente del guardado, cama y circulación; una complementaria de lectura sólo si las vistas actuales no la cubren, sin ocultar el suelo residual.
- Mantener paso 0,8 m, giro de puertas y reservas 3D, altura máxima, mínimos del kit, IDs/valores/acciones del botín, RNG y fallback completo. Comprobar destino final real de hide contra collider y radio corporal, no inferirlo sólo del frente nominal ni de una celda próxima; houses ajusta los puntos de uso al final. Probar salida/despertar, sueño, cajones, consulta, recogida y persistencia según afectación.
- La luz actual se conserva en la propuesta. Se aprecia techo iluminado y un conjunto bastante uniforme; no se ve una oscuridad general que justifique añadir focos. Distribución nocturna y relación exacta luz–mueble necesitan escenas reales después de componer, sin cambiar umbrales ni usar el índice de cobertura como lux medidos.

No se han editado activos, generado producto, llamado API/juicio semántico, usado GPU/navegador ni aprobado la propuesta.

## Huellas de la evidencia leída

HEAD leído: `28ae178589eed26c178d053349ad568f4990023b`.

- `data/interiores/fichas/casa_dorm.jpg`: `923f1f48b3875a996f81921ea9bea7ae74fd4cc4cf0a43235c8960a28dd5cbea`.
- `data/interiores/fichas/casa_dorm.json`: `059133170742056a0bed72e7610e78849f1609de3db60702a94f032aa1433ea7`.
- `data/interiores/fichas/casa_dorm2.jpg`: `413b7c26d050b45cb4439efe4d8a069e391e4644011ef973514af14b007065da`.
- `data/interiores/fichas/casa_dorm2.json`: `58347f80ce24dd65e6101f861b38bad99decbe746afeeedbc5d0b0dabde15141`.
