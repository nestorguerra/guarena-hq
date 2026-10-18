# Adenda — perfil bajo para el contrato mecánico en CI

**Sin P1/P2; aceptación estática.** Python SHA256 `67410f5ae4af4c1d0079a415449d365c7db78409a5f6e655ccee36047a7e8bda`; workflow `8d0761880febae2a8cc6fc1016496fb6ec1a7fa912ffcff8744413eb44c20bd5`.

`--calidad alta|baja` conserva alta como valor por defecto. Sólo el paso de botín de CI selecciona baja. La fixture permanece manual, dynResfalse y misma partida ficticia; no se cambian el contrato JS, criterios de premio/persistencia, LISTO ni sus tiempos. El perfil y modo manual se verifican después del arranque y después de recargar. No se modifica producto ni el perfil de las capturas visuales.

Reejecución propia CPU de main/diagnosticar con PrivateTab/CDP dobles: **11 casos PASS**. Incluye alta por defecto, baja explícita, rechazo de calidad distinta y modo automático en ambos documentos, además de los seis casos de excepción/cierre. Se coteja que el script de nueva página instala calidad solicitada/manual/dynResfalse/money321/bagvacía. Evidencia: `botin_calidad_ci_revision_cpu.py` y `botin_calidad_ci_revision_cpu/report.json`.

RENDER ejecutado aparte con dobles de contexto: registra calidad/manual/DPR/canvas y string de renderer cuando existe WEBGL_debug_renderer_info; devuelve null cuando no existe y tolera game aún ausente para diagnóstico. No se ha creado contexto WebGL. cinematic se reduce correctamente a bool, evitando serializar la ruta entera. El resultado de renderer es dato del navegador, no identificación garantizada del hardware físico.

El diagnóstico CI comunicado (intro activa, vuelo y progreso ~.06095; carga oculta y sin errores) sólo localiza la fase: no llegó a recoger. **No demuestra renderer software ni confirma que bajar calidad resuelva el fallo.** Hace falta la nueva ejecución real; resultados M1 y CI se interpretan por separado. No se ha extendido ningún timeout ni se ha ocultado el FAIL. El límite previo de timeout de protocolo frente a socket permanece.

**Declined to judge:** causa de la introducción detenida, suficiencia de baja en el runner, eficacia visual, regresión de GPU, nueva ejecución CI/fuente/paquete y publicación.

---

# Revisión independiente del diagnóstico de botín en CI

**Sin P1/P2 pendientes. Aceptación estática del diagnóstico corregido**, SHA256 `2320e4775243e18b0642a6b9c469af1d945b7b8784f8ec0f2d1a79e3a10b4996`. No se ha abierto navegador/GPU ni modificado producto. No se atribuye una causa al fallo CI original.

## Evidencia propia

Ejecutado `main` y `diagnosticar` reales con dobles explícitos de PrivateTab/CDP, sin esperas ni navegador. Instrumento `botin_diagnostico_ci_revision_cpu.py`; recibos por caso y resumen en `botin_diagnostico_ci_revision_cpu/report.json`. **Seis casos PASS**: éxito normal; fallo al arrancar; fallo al recoger; fallo al arrancar tras recarga; fallo adicional al tomar diagnóstico; fallo de cierre después de éxito funcional. AST Python correcto.

ExitStack registra primero la salida del contexto y después el callback. Su orden LIFO toma el diagnóstico con la pestaña aún viva y después cierra PrivateTab. El callback no suprime excepciones. Una excepción al diagnosticar queda separada en diagnostico_error; la causa original se conserva en errores/stdout y el proceso devuelve1. Cuando todo pasa no se consulta diagnóstico y se devuelve0.

Durante la revisión se señaló un falso PASS preexistente: un error al cerrar el contexto después del éxito funcional añadía errores sin cambiar estado. Raíz añadió estado=FAIL en except; el sexto caso demuestra ahora retorno1. No se ha debilitado ningún criterio de recompensa, recarga, fixture o espera.

El diff sólo añade diagnóstico/etapas/stdout y corrige el estado en la ruta de excepción. Los puntos de acción y comparación de recompensa permanecen. El nuevo JSON de fallo se escribe en el informe habitual y su causa se imprime en CI; no depende de recuperar /tmp después del runner.

## Límites reales

`tab.ev(..., timeout=5)` configura el límite de evaluación JavaScript de CDP. **No es un plazo de pared de cinco segundos del transporte**: Tab usa un socket de hasta1800s. Si Chrome deja de responder al protocolo, el diagnóstico puede tardar hasta ese límite heredado; no se ha cambiado aquí ni se ha certificado fallo de transporte real. Un error en PrivateTab.__enter__ no tiene pestaña adquirida ni callback y se informa por la ruta general. Un error exclusivamente de cierre tras éxito se marca FAIL, pero no puede obtener retrospectivamente el diagnóstico vivo.

El recibo añade observabilidad para la próxima ejecución; no demuestra por sí mismo que LISTO, importaciones, recursos o recompensas expliquen los207s observados. **Declined to judge:** causa raíz de CI, corrección funcional de ese fallo, runtime fuente/paquete, publicación y ejecución GPU de cámaras infantiles.
