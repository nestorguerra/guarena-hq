# T17 · Revisión del helper de cierre de publicación

Revisión estática de `cerrar_publicacion.py`, SHA `8cf85aa963bd4e6122f7bc921343e9c46e8f910a19511436a9f8fc032bac6cf9`. No se ha ejecutado el helper, red, publicador, probe, commit o despliegue. Los recibos finales y `commit_producto.txt` todavía no existen al revisar; la ejecución continúa pendiente.

## Hallazgo relevante · P2 · identidad de Pages no comprobada

En la línea 6 se exige `pages['conclusion']=='success'` y `pages['headSha']==expected`, pero no la identidad de workflow ni la finalización de sus jobs. Un JSON de una ejecución satisfactoria de `validar.yml` con el mismo SHA satisface esas condiciones y su `databaseId` termina atribuido a Pages en el acta/documentos. El HTTP200 y el SHA público antes/después son comprobaciones independientes útiles, pero no demuestran que el identificador citado sea el run de despliegue.

Corrección mínima: exigir un recibo verificable del ID, repositorio, path `.github/workflows/pages.yml`, head SHA, status completed y conclusion success, con `build` y `deploy` presentes y satisfactorios; conservarlo en la evidencia durable. Puede obtenerse en la etapa de preparación/consulta ya existente; este informe no pide ejecutar ahora red ni desplegar.

En línea 8 se copia sólo `ci['ci']` y un subconjunto de `ci` para el árbol. Se pierde `workflow_verificado`, la comprobación explícita de identidad del CI añadida al publicador tras la revisión anterior. Preservar ese campo o el `main_actualizado.json` completo evita que la evidencia durable omita esa garantía. El publicador ya hace la comprobación; no se pide reimplementarlo.

## Resto del alcance

No he detectado otra contradicción relevante entre el SHA esperado, las fuentes congeladas, el SHA público antes/después, el main leído en remoto o la preservación de los archivos del manifiesto anterior. El cierre comprueba los hashes históricos antes y después y conserva una copia del manifiesto previo. El texto visual mantiene expresamente el objetivo4/5 pendiente. El script escribe archivos/documentos, por lo que debe ejecutarse una sola vez con todos los recibos definitivos preparados; esta revisión no equivale a ejecución ni éxito de publicación.

## Adenda · P2 cerrado por lectura de la corrección

Helper corregido SHA `8cf85aa963bd4e6122f7bc921343e9c46e8f910a19511436a9f8fc032bac6cf9`. **P2 cerrado; sin bloqueos detectados para ejecutar el cierre cuando estén los recibos reales.**

Las líneas8–9 consultan el run identificado por `pages.databaseId` en el repositorio exacto y exigen ID, path `.github/workflows/pages.yml`, SHA esperado, completed/success; además requieren jobs build/deploy y éxito de todos los registrados. El ejemplo anterior de un recibo de validar.yml ya se rechaza por path. Las líneas10–11 revalidan la identidad CI preservada y sus dos jobs obligatorios. La línea19 archiva tanto `pages_workflow_verificado.json` como `main_actualizado_completo.json`, conservando `workflow_verificado`; ambos entran en el nuevo manifiesto.

El resto del cierre conserva las comprobaciones previas. `pages_final.json` debe contener databaseId/headSha/status/conclusion/url/jobs como se ha indicado. Esta adenda acredita únicamente lectura del código nuevo: no se ha ejecutado consulta, cierre, commit ni despliegue, y no se afirma que los recibos pendientes hayan pasado.

Nota de trazabilidad: el hash consignado en el encabezado inicial se calculó después de comunicar el hallazgo, cuando el archivo ya contenía la corrección; por eso coincide con el SHA final. El hallazgo histórico se basó en la lectura anterior sin las guardas nuevas, no en los bytes del SHA final. No se atribuye ese P2 al archivo corregido ni se inventa un hash de la versión anterior.
