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
