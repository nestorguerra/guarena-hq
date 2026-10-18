# Revisión privada del instrumento de juicio

Sin P1/P2 pendientes para `decision_visual.py` SHA `f74cdba771d371ddc2ae8366ff58149a6434a554afb86ab652984d8e0a1ad705`. Comparado con cliente original: petición, rúbrica, instrucciones, referencias, modelo y endpoint intactos. No se leyó helper/credencial ni se ejecutó red/API.

La primera versión guardaba tras json.loads; observado y corregido por raíz. La versión final escribe bytes HTTP200, request-id y SHA antes del parseo, con límite1MiB+sentinela explícito. Nombres incluyen requestdigest y se bloquea repetir una petición conservada sin recibo. Un recibo evaluado igual mantiene salida idempotente; otro recibo requiere preservar evidencia antes de nueva llamada.

Ejecuté offline únicamente fragmentos AST de validación y lectura HTTP con dobles: válido aceptado; duplicado, confianza fuera de rango, falta de nivel, etiqueta distinta, suma y score incoherentes rechazados. HTTP200 de JSON incompleto produce FAIL pero conserva cuerpo y request-id antes de parsear. Recibo `revision_decision_cpu/report.json`. No se importó el módulo ni su cliente seguro.

Las tolerancias .01 para suma y .015 para esperanza permanecen explícitas; no cambian la nota recibida ni la media. Límite menor: isinstance acepta bool como subtipo numérico de Python; no reproduje respuesta real con booleanos y no lo considero bloqueo de esta llamada bajo esquema servido. Si se endurece después, usar type exacto sin cambiar ponderación.

Declined to judge: resultado futuro del servicio, semántica/nota de imágenes, disponibilidad de credenciales, red, publicación y replay34 del autor (no ejecutado en esta revisión).
