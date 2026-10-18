# T20 R1 · integración y probe público preparados

**Sin bloqueo de integración identificado en el delta revisado.** La orden actual es detener iteraciones y mostrar el estado parcial. No se exige nueva puntuación ni4/5 para este dictamen. Los gates y la publicación corresponden a raíz y sus recibos; este informe no los anticipa.

Se cotejaron las ocho fuentes activas enumeradas en integracion_r1.json contra prototipo_r1: igualdad exacta. Las417 entradas de estado_candidato permanecen idénticas. El diff activo tiene ocho archivos y no añade un solver ni cambia constructor de Annie.

En catálogo sólo cambian vb_cama_doble, vb_cama_individual y vb_cama_amplia; no se añaden IDs. Los campos fuera de partes/nota (rol, clase y demás metadatos funcionales) son exactos a HEAD. Las variantes infantiles se fabrican antes de la modificación final y no están entre los IDs cambiados. La cama individual también es compartida por joven: su receta no cambia, su modelo sí. Por eso el probe añade la puerta real1594, cuyo kit vivienda_joven está presente en el inventario del pueblo; no fabrica una habitación de laboratorio.

Receta dormitorio conserva camas/armario/cómoda y reorganiza el programa opcional de lectura: orejero, mesa auxiliar, libro, biblioteca y alfombra relacionada. Los umbrales16/22/26 y fallbacks siguen explícitos. El recibo CPU resultado_r1 contiene22construcciones sin pérdidas/errores/uso en sus dormitorios. La revisión CPU dirigida registra mismas envolventes de las tres camas y comprobaciones de apoyos y accesos; son evidencias leídas, no ejecuciones propias. Cambiar entradas de receta puede alterar índices de adornos/semillas posteriores: no se afirma identidad decorativa global.

El acabado de dorm/dorm2 pasa después del kit, orienta el paño por la cama y evita el zócalo antiguo duplicado. La paleta textil nueva sólo se aplica a roles cama en vivienda_dormitorio; no se atribuye esa paleta a vivienda_joven. No se cambian métodos de hide, cama, navegación ni límites de mallas/luces en este delta. La ausencia de errores en estas lecturas no sustituye los barridos200/81dorm/81joven ni el paquete que ejecuta raíz.

## Instrumento público nuevo, aún sin ejecutar

revision_publicacion/verificar_publico.py mantiene roots parents[4], SHA obligatorio y páginas HQ; conserva literalmente los bloques T19 de ocho vecinos/estudios/salones/trofeos/Annie/comercios/persistencia. trofeos_publico.js es copia exacta T19. Añade dormitorios_publico.js antes de Annie, con errores parciales conservados y error global si falla.

El nuevo bloque abre2786/3244/1689/2132/5157 por puertas reales y revisa todas sus estancias vivienda_dormitorio, incluyendo dorm2; abre además1594 real para cama individual joven. Exige registro pieces.bed ligado al índice real, prueba HouseLife.lieOnBed y wake con residente real y salida física libre. En cada armario llama hideIn/unhide reales, comprueba flags/posición y salida con collider. Reposición privada declarada; restaura jugador/cámara y sale de la casa en finally. No fuerza flags de ocultación ni crea jóvenes sintéticos.

En3244 exige silla de lectura, mesa vinculada, biblioteca, libros con soporte nominal correspondiente al catálogo (mesa.555; baldas.04/.42/.8/1.18/1.56), registro único del asiento y acción read. Renderiza y veta shaders no ejecutables. **Límites deliberados:** no raycast de las superficies de libros, no simulación de caminar entre plantas, no inspección visible desde dentro del armario, no activación de leer/sentarse en el bloque dormitorio. La cama se usa por el residente mediante métodos reales; no se inventa una acción del jugador para dormir en cama ajena. La siesta del jugador sigue probándose en Annie mediante el bloque heredado. Persistencia, dinero, caja, decoración y claves Evolución/fija se comparan al final por el wrapper.

Comprobado sólo AST de Python y node --check del JS. Preparado para lectura de raíz y ejecución posterior con SHA publicado; no se ha abierto navegador, GPU ni API, ni se ha hecho build/commit/push/despliegue o edición de producto.

## Huellas

- `.cache/calidad/tanda20/integracion_r1.json`: `13ec3bf055aaefe84366c3a6d434d6a2c5b92e58e438354a38d1755ce55e700f`.
- `.cache/calidad/tanda20/estado_candidato.json`: `fb6194fa3e727b734f69260990ee11523721312fad03a9798637379bccb45052`.
- `.cache/calidad/tanda20/revision_publicacion/verificar_publico.py`: `4aa59e73e110628f080efb9e4d9768fb836c0b15820df655417d0812b72705d1`.
- `.cache/calidad/tanda20/revision_publicacion/dormitorios_publico.js`: `125ecbcd458490f7aa26ec57d89a0b1315937f8a7694b9b57d3e8f623053ba1e`.
- `.cache/calidad/tanda20/revision_publicacion/trofeos_publico.js`: `7225e61b1c30ebf9bac46267a0a78f5047499dfae372bf6d0bb6545232a14dd9`.
