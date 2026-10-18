# T17 · Estudio final R1 · candidata privada

**Preparada para revisión independiente y captura; no aprobada visualmente ni integrada.** Un solo parche contra los bytes T16 sellados, con modelos/receta/textura propios, cortinas cortas y **acabado R2 de raíz incluido**. No aplicar de nuevo `acabados_r2/acabados.patch`: sus cambios de `houses.js` ya forman parte del combinado.

Parche: `estudio_final_combinado_contra_T16.patch`, SHA256 `222f89128d77a6ff61a28d2d226c192765877cdd1cb0116625a2b94601bb0dd9`. Son cinco fuentes: catálogo B, kits B, textura B, houses y acabados. `fuentes_finales.json` lista hashes base/final. Motor `locales.js`, validador, capturador, luces, marcos y umbrales permanecen sin cambios. El catálogo/kit/JS compilado se regeneran; no se copian sobre producción.

## Procedencia y alcance

`base/` conserva los bytes T16 aprobados de R2, no reconstruye un HEAD antiguo. `base.json` conserva su historia original (HEAD observado e902 con fuentes T16 actuales por hash); no se reescribe como si procediera del commit posterior. Annie mantiene `7364d553829e4a86b470d266ef9849cf3498e3cec584404e6d5e5dbd0fd8ff09`. R1 y R2 greybox siguen selladas e intactas. `procedencia.json` identifica el acabado de raíz SHA35515f62 y los dos manifiestos anteriores.

La cohorte es **22 identidades documentadas del pueblo**, de las cuales sólo **3244 y1594 tienen estudio**, más **1481 sintética**. No son31 estudios reales ni81 montajes. El alcance CPU actual no sustituye los gates de producción posteriores ni las futuras capturas de los modelos finales.

## Programa y modelos finales

Se conserva la distribución R2 mesa→bajo→biblioteca, envolventes y poses de los tres muebles, silla y ordenador en las tres canónicas. Puesto `vb_puesto_estudio_amplio` de1,30×0,60m y altura1,22m, bajo `vb_guardado_estudio` de0,90×0,35×0,78m y biblioteca `vb_biblioteca_estudio` de1×0,34×1,70m. No hay motor nuevo, cambio de cámara ni búsqueda por semilla.

La biblioteca tiene laterales/trasera delgados, huecos y baldas reales, guardado adulto integrado abajo y dos grupos de consulta obligatorios sobre baldas. El bajo presenta tres cajones con hueco central de agarre y tapas apoyadas. El escritorio tiene tablero, patas, montantes y respaldo físico; una lámina de cartón delgada arranca apoyada en el tablero a0,75m y toca el respaldo, sin volumen fantasma. Se conservan **0,60×0,30m frontales libres** incluyendo todas las piezas apoyadas. El ordenador T16 continúa único e independiente, misma definición `PICKUP`, con su apoyo real; no se integra en la mesa.

Cada perfil tiene consulta y lámina propias: carpetas/bocetos del artista, libros/apuntes del estudiante y carpetas/partituras originales del músico. Son masas y dibujos distintos, no sólo tintes. La silla y orejero exclusivos del estudio copian geometría, roles y asientos compartidos y usan textiles calmados; los originales no se modifican. Se conserva una lectura secundaria con sillón, mesita y libro cuando cabe, sin forzarla en1594. El único conjunto de lectura sobre el bajo sustituye el bloque morado del greybox; la galería opcional queda en0–1 porque el respaldo ya explica la actividad.

El pool adulto tiene54 IDs declarados por perfil. Una prueba conservadora acredita **33 utilizables** por perfil (26 variantes existentes que caben sin girar en una balda real de930×290mm/370mm de altura y7 piezas principales efectivas); no se cuentan para ese suelo las variantes grandes que el motor debe omitir. `datos.py` completo pasa sin bajar mínimo30. Los nuevos IDs no entran en kits no optantes.

## Tela: RED preservado y solución autorizada

El greybox R2 intersectaba tela real en3244:13 triángulos con tablero,4 con pata,3 con montante y4 con respaldo, incluso con inset de1mm. Se conservan `tela_r2.json` y `tela_contacto_local.json`; no se ha recortado el mueble para esconder ese defecto.

`windowIn` recibe dueño opcional conocido en todas sus llamadas (L/R/RR y superiores). Sólo estudio de artista/estudiante/músico usa paños cortos: top2,225m, borde inferior1,28m, altura0,945m, centro1,7525m. `curtainGeo` global no cambia. Conserva dos paños,34 vértices por paño, ancho, posición lateral/profundidad, pliegues, tejido/color, hueco, vidrio, persiana, alféizar, luces y RNG de ventanas. En la cohorte cambian únicamente los dos paños de3244 y los dos de1481;1594 carece de ventana. Los demás paños son exactos. **Cero intersecciones de triángulos reales con las piezas finales** verificadas de estudio. El hueco nominal de6cm sobre el puesto no equivale a aceptación visual del remate corto: debe verse en3244/1481.

## Evidencia CPU literal

| Caso | T16 mallas/triángulos | Final combinado mallas/triángulos | Luces |
|---|---:|---:|---:|
|3244 artista|56 /51210|56 /53988|8|
|1594 estudiante|58 /59590|58 /63274|8|
|1481 músico sintética|58 /45034|58 /48516|8|

`full.json`:22 identidades+1481, marcos, luces y botín exactos; acciones de estudio conservadas;20 casas sin estudio y sus estancias exactas. Coste observado máximo59 mallas/63274 triángulos/9 luces en la cohorte, dentro de60/350000/9. Es comparación **T16 contra final+acabadoR2+cortinas**, no coste aislado de catálogo ni FPS.

`annie.json`: semillas12/13, cinco estancias, construcción completa (geometría/poses/materiales), colisionadores, acciones y posiciones exactamente T16;60mallas,9luces. La receta efectiva no optante se conserva, no sólo un recuento de acciones.

`geometria.json`: apoyos completos e interpenetración nula de pertenencias compuestas; etiquetas de carpeta en contacto lateral real; estructuras conectadas físicamente al suelo. Se enumeran las uniones de tableros/laterales/traseras del mueble (ensambles de8–25mm), sin presentarlas como cero penetración de estructura. Lámina sobre mesa y respaldo, PC real y escritura libre. Negativos de carpeta elevada36mm y pila desplazada dentro de libros fallan. `negativos.json`: recinto reservado agota12, libro flotante4cm, reserva frontal invadida y silla retirada siguen rechazados. Se conserva el RED inicial de masa0,2kg de láminas en `gen_datos_red_masa_panel.log`; masa final real0,3kg pasa el rango de cuadro.

`fallback_final.json`: **semilla4 fija, estudiante/joven,3,2×2,8×2,75m, puerta−0,75**, intento0 completo con los modelos finales. Único delta declarativo aprobado: biblioteca `si_no:true`; tras rechazar el grupo, recuperación existente `contra_pared` en otra pared, sin vínculo `de` ficticio.14mallas/5774triángulos,1luz,0errores. Entrada y centro de uso de biblioteca libres y alcanzables con cuerpo0,80m. Layout individual y siguientes dos extracciones RNG iguales al mismo kit sin grupos; no rollback a receta T16. El recinto reservado agota12 y mantiene marco. **El laboratorio no reserva su ventana y ésta puede quedar parcialmente tapada en proyección**: ese PASS no acredita imagen/ventana ni se traslada a casas sin sus reservas.

La decoración y opcionales de estudio cambian respecto aR2 por las entradas/materiales nuevos: no se atribuye invariancia de todo su RNG/poses. Sí se acredita núcleo canónico igual, otras estancias/luces exactas y los controles descritos. `planta_comparacion.png/svg` muestra masas/paso, sin raster de materiales. `regeneracion.json` conserva20 derivados/registros de validación:19 salidas idénticas en dos generaciones completas y reporte `datos.json` cotejado además entre ejecuciones2/3; los tres stdout de `datos.py` coinciden. Sin errores.

## Reproducción e integración posterior

Desde una copia de la raíz con los bytes T16 de `fuentes_finales.json`, comprobar/aplicar **sólo** el parche combinado y regenerar:

```sh
git apply --check /RUTA/estudio_final_combinado_contra_T16.patch
git apply /RUTA/estudio_final_combinado_contra_T16.patch
python3 tools/interiores/catalogo_vivienda_a.py
python3 tools/interiores/catalogo_vivienda_b.py
python3 tools/interiores/kits_vivienda_a.py
python3 tools/interiores/kits_vivienda_b.py
python3 tools/interiores/datos.py
```

No aplicar además el acabado R2 ni copiar compilados de esta carpeta. Los hashes esperados de cada derivado están en `regeneracion.json`. La comprobación `git apply --check` contra raíz T16 pasó sin escribir activos. Contratos mantenidos de raíz/coder están preparados aparte para tanda20; no se copian ni se atribuye su ejecución aquí.

## Pendiente de revisión independiente

Código: cotejar uniones estructurales, superficie/PC/lámina, caller de cortinas y no optantes, composición efectiva y fallback final. Visual: lectura de la biblioteca abierta y consulta según perfil, panel detrás del monitor, volumen alto todavía dominante, remate corto sobre alféizar y jerarquía de lectura en3244. No hay raster de texturas ni GPU; sólo se ejecutó canvas stub para construcción CPU. No se mide rendimiento de juego vivo, ni se afirma4/5, aprobación formal o publicación. Los81/200 y combinación browser se ejecutarán posteriormente por raíz sobre la candidata revisada.
