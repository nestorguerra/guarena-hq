# Cocina T16 — acabado artístico R2, privado

Delta exclusivamente sobre el generador de R1. Cambian **va_preparar_pan**, **va_banda_vajillero** y **va_banda_vajillero_amplio**. Motor, receta, acabados, luces y cámaras permanecen byte a byte iguales a la candidata técnica R1 final.

La hogaza incorpora volumen redondeado con tres cortes de corteza sobre su cara plana. Cuchillo y mango reposan íntegros en la tabla, sin invadir el pan ni ampliar huella/altura máxima0,109m. El hueco alto vajillero sustituye pilas pequeñas por una cazuela doméstica de0,244m con tapa y pomo, apoyada en balda. Se mantienen variantes y13compuestos.

CPU sólo sobre las piezas afectadas y los tres montajes canónicos reales: apoyos completos (incluidas hoja/mango), incisiones dentro de cara plana del bisel, cero penetraciones internas>1e−6; mismas envolventes dentro de1e−6, poses/referencias/roles/receta y luces. Presupuesto54/56/58mallas, sin aumento de materiales/luces. Validadores local y uso sin errores. `datos.py` completo PASS en copia privada. No se repite el barrido22 porque sólo cambia arte dentro de la misma envolvente; su cobertura técnica se documenta separada en R1.

`artistica.patch` aplica sobre el generador R1, no sobre la fuente base que aún no contiene ese fichero. `manifest.json` identifica ambos. El modelo/JSON/compilado privados se generaron desde la fuente actual; no se copian a producto. La revisión geométrica independiente previa corresponde sólo a R1: se ha pedido una revisión nueva de estos tres modelos. Sin GPU ni aprobación visual/formal ni publicación por este autor.

La revisión independiente está cerrada en `revision.md`, sobre artistica.patch cbcef6a4…, sin P1/P2 y con repetición separada de geometría/coste. No es aprobación visual. Se añade `artistica_contratos.patch`75069a18…: delta sólo del tercer callback19, con soporte de hoja/mango, giro de surcos y negativo no vacío que exige hoja presente y detecta+2cm. Callback literal PASS; la revisión de este delta de contrato se entrega separada de la revisión de modelos. `contratos_r2.patch`b36de117… es la versión combinada contra base; no aplicar las dos versiones a la vez.

Cierre del contrato artístico: `revision_contrato.md` acepta75069a18… sin P1/P2. El revisor ejecutó positivo, mutante del filtro antiguo y ausencia de hoja: PASS/FAIL/FAIL respectivos, con restauración íntegra del catálogo. No es ejecución del harness completo ni aprobación visual. No quedan cambios previstos de este autor en motor, modelos, receta o contratos.
