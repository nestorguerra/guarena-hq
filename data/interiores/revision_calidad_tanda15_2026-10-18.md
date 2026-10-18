# Tanda15 infantil — recopilación de revisiones independientes

18 de octubre de2026. Dictamen visual: mejora parcial conservable frente al producto T14. A3,488/B3,208, antes3,328/3,040; objetivo4/5 pendiente. Esta recopilación enlaza revisiones realizadas por agentes distintos de los autores; no añade una aprobación formal ni sustituye al visto bueno del usuario. La publicación por tandas está autorizada en el encargo.

## Composición y acabados

Biblioteca con dos baldas ocupadas y vinculada al escritorio/silla; armario independiente en esquina. Los módulos se admiten juntos con referencias correctas y fallback conservado. Se corrigió una penetración entre cuadernos y caja antes de integrar Bv2. Revisiones en evidencia_tanda15/biblioteca/.

El fondo de la cama reutiliza un tono más profundo; las otras paredes altas toman la cal cálida del techo. Respeta puertas/ventanas y no añade familias materiales. El primer caller aplicaba acabado antes de amueblar: corregido y protegido por prueba de paños emitidos. Se comprueban cuatro orientaciones, ambas plantas y seis casas efectivas. Revisiones en contraste/.

La zona baja de lectura y juego incorpora banco propio de90×32cm, asiento a40cm y dos cajas de guardado. Alfombra compacta1,20×0,85m en áreas menores de12m²; grande1,80×1,30 desde12m². La frontera real de area_max es exclusiva; se retiró el límite provisional12−1e−6 que dejaba un intervalo vacío. El banco queda frente a libros sólo si conserva uso, cortinas y pasos; separacion_pared=.14 sustituye la holgura habitual.01. No se fuerza en las siete casas donde no cabe. Las31construcciones por semilla conservan muebles principales;24tienen banco y todas alfombra. Coste acotado de esas31:60mallas/63.264triángulos/8luces, materiales y luces sin aumento. Revisiones/recibos en juego/.

La revisión visual Bv3 acepta mejora parcial sin regresión importante pendiente. Banco azul y alfombra equilibran mejor el ocre y dan uso al vacío. Persisten paño alto dominante, programa parecido en las dos estrechas y estudio poco claro en4007. Los objetos pequeños también cambian por RNG; no se atribuye la mejora sólo al banco. La comparación con pintura previa conserva5/6cámaras; con T14cambian6/6. No hay una prueba causal de iluminación idéntica en píxeles. Banco y alfombra aparecen recortados según vista; no se afirma cobertura de cada esquina de todos los muebles. Ver revision_visual_Bv3.md y capturas/.

## Validación, fallos y correcciones

Las guardas del capturador rechazan cuerpos dentro de mobiliario, centros de círculos, resolución cancelada con profundidad, límites de estancia y cambios de pose en render. Tres casas y seis vistas finales físicamente libres; algoritmo688sin nuevos ajustes de ranking/FOV para favorecer esta tanda. Evidencia en guardas_fotos/.

T17 falló primero porque su rectángulo exigía todo el fondo de1,2904m hasta pared. El hueco real banco–silla es.8304m en4007/5045 y hay corredor continuo para radio.4; lectura/ocultación conectadas con radio.34. Se mantiene el mínimo.8 y se exige una sección.8×.8 contigua a la silla. El banco clonado adelantado hasta dejar.79debe fallar. El negativo adaptativo evita un falso fallo si una mejora futura aumenta el hueco. Se preserva el FAIL original y el diagnóstico, sin mover producto para hacerlo pasar. Ver paso/, historico_paso_v1/ y revision_raiz_paso.md.

El primer PASS81 CPU no acreditaba los81laboratorios literales: su wrapper cambiaba dimensiones al reintentar. La errata y recibos originales se conservan. El navegador detectó29/51/63sin alfombra; su FAIL se conserva en historico_laboratorio_v2/. Reproducción independiente exacta de hashes y dimensiones. La búsqueda aleatoria tenía un margen.1 que dejaba fuera un hueco admitido por las guardas en51. Un opt-in de las dos alfombras añade búsqueda cardinal finita tras agotar200tiros, límite16.000 y sin relajar dentro/libre/cierra. buildLocal doméstico reintenta mínimos con W/D/H/contexto originales y puerta comprobada, hasta12, y expone semilla efectiva/intento/agotamiento. La reserva total sigue fallando tras12; no se reduce tamaño ni cuota. Ver diagnostico_laboratorio/, fix_laboratorio/ y ERRATA_CPU_81.md.

Los controles finales usan buildLocal literal:81completos con marco fijo;78antesválidos exactamente iguales.31construcciones completas por semilla conservan estancias/nav/atributosgeométricos/transformaciones/luces y P/U;39otroskits sólosemilla1sin cambios. Eso justifica reutilizar la ficha8a902376… sin nueva llamada de puntuación. Se conserva su procedencia original y se documenta la inferencia de invariancia; no se presenta una nueva comparación de píxeles. Ver reutilizacion_capturas.json.

## Gates finales

66contratos del navegador, todos los kits en cinco semillas,200casas/1166habitaciones y81montajes infantiles pasan. El juego fuente pasa96recorridos sin escapes/atravesamientos, ocho vecinos, Annie y partida; recursos y marcas pasan.22derivados se regeneran idénticos. Máximos de200casas:70.192triángulos,60mallas,9luces y166ms de montaje enM1; no es una medida deFPS ni garantía universal.

La integración del paquete final también pasa: ocho casas, Annie, acciones de tres comercios, partida ficticia y recarga, sin errores. Los nueve gates del candidato congelado terminan con exit_code 0 y sin cambios de sus fuentes. CI y lectura pública del SHA exacto quedan para después del commit.
