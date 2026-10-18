# Guardas físicas del capturador — propuesta privada T15

**Preparado, no aplicado.** Sólo propone cambiar `tools/interiores/fotos_casa.py`. Base activa congelada `2fc0167ae2f4b1104b6071c8864053cda33aa7b5`; SHA base `6df65f3e1b9c384d44a28568b51bde2d9fb0a2a722464af92dda10324574d937`. No se han ejecutado capturas, navegador, GPU, build ni cambios de producto. Los pares fijos biblioteca y sus evidencias se conservan.

Parche `fotos_guardas.patch`, SHA256 `6777e0908038f728812337ba069fe371808962234ce63e8c7d2b80eb0cbe7a44`. Candidata completa `fotos_casa.py`, SHA256 `6881d0b2f2d528552a0480ccc43188c8a4071ea73364418df387f077ebb69cae`. `base_fotos_casa.py` es copia física de la base. El archivo completo es para revisar/aplicar en su ruta original: no ejecutar directamente desde esta carpeta, pues ROOT se calcula respecto a esa ruta.

## Cambio concreto

Cada candidato se evalúa sobre un clon x/z. La posición original no recibe la resolución del collider. Sólo es válido con desplazamiento y profundidad finitos <=1e-6 m, radio .34 m y dentro de los límites reales de la estancia (origen/W/D), descontado ese radio. Se rechaza además el centro dentro de una OBB de mueble de suelo de la misma planta y el centro degenerado de círculo vivo que resolveCircle omite. El filtro de muebles sigue houses.js: sin soporte, pared, techo, PICKUP ni altura <.3. La clase se lee del catálogo real, como houses.js, sin depender de que cada colocado incluya p.clase.

Tras los tres frames normales se impone la pose seleccionada original. Se vuelve a comprobar justo antes de render y al terminar, antes de publicar JPEG en /__snap. Si el render mueve posición/orientación/FOV, falla. No se reubica la cámara para salvar la captura. JSON de cada vista añade clearance.candidate/beforeRender/afterRender con límites, radio/tolerancia, delta/profundidad, contenciones, círculos y declaración de comprobación sobre copia. Un fallo final incluye el clearance en la excepción; no genera una nueva imagen para esa vista.

Objetivos, altura humana, FOV, semillas, rejilla, puertas/cobertura y fórmula de selección visual permanecen literalmente iguales. La nueva guarda cambia cuáles candidatos son físicamente admisibles. Si no hay candidato válido, el capturador falla: no se amplía el espacio de búsqueda ni se sustituye una semilla. Ninguna regla especial para 5045 u otra casa.

## Evidencia CPU propia

`guardas.cpu.mjs` extrae las funciones y controles finales exactos de la candidata. Usa StaticCollider real, caja real con datos activos, Three r170 y RoundedBoxGeometry existentes. No rasteriza ni crea WebGL. `cpu.json`: **15 casos de clearance, cuatro mutantes y cuatro casos de render simulado pasan**.

- Dos segmentos enfrentados producen delta=0 y depth=.279999994: el criterio anterior aceptaba, el nuevo rechaza por profundidad. Es reproducción sintética del mecanismo de cancelación, no reejecución GPU de la pose histórica 5045 (.28546875).
- Penetración de 2cm: antes se aceptaba y desplazaba la pose; ahora se rechaza sin modificarla.
- Centro profundo de cama real girada: delta=depth=0, rechazado por OBB. Centro de prop circular vivo: delta=depth=0, rechazado por centro degenerado.
- Frente libre, límite utilizable, planta distinta, objetos apoyados/de pared/techo/PICKUP/bajos y círculo desactivado conservan aceptación. OBB con origen trasladado y planta alta se detecta.
- Quitar por separado profundidad, OBB, centro circular o bounds vuelve a aceptar su negativo dirigido.
- Controles exactos antes/después del render: ruta libre pasa; ocupación previa impide llamar render; ocupación posterior falla; desplazar la cámara a otro punto libre también falla por cambio de pose. Render es un doble CPU explícito.

AST Python, sintaxis JS y `git apply --check` pasan. El main Python permanece exacto. Manifest registra hashes y expresiones preservadas. Activa comprobada idéntica a la base después de las pruebas.

Repetición CPU desde raíz:

```sh
/Users/nestorguerra/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node .cache/calidad/fotos_guardas_t15/guardas.cpu.mjs
```

## Riesgos y límites

La búsqueda actual puede quedarse sin pose aceptable o escoger otra distinta; eso debe conservarse como FAIL o como protocolo de captura nuevo, sin atribuirlo al producto ni comparar imágenes como cámaras idénticas. Las OBB son la huella física usada por el juego, no una prueba de malla hueca a altura ocular. La tolerancia 1e-6 puede hacer visibles contactos antes ignorados. No se promete que todas las semillas tengan dos poses libres con la rejilla existente.

El capturador anterior puede haber escrito imágenes previas de otras vistas antes de un fallo; este parche no convierte el conjunto de escrituras en una transacción ni borra evidencias viejas. La captura canónica requiere revisión independiente, aplicación autorizada y ensayo runtime posterior. No se ha aprobado calidad visual, persistencia/iluminación de residentes, resultado GPU ni despliegue. Las comprobaciones de identidad/fuentes/PMREM de los pares fijos siguen siendo responsabilidad de su instrumento separado.
