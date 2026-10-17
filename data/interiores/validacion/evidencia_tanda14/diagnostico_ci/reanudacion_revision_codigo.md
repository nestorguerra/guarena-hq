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


---

# Adenda — reanudación explícita para el contrato mecánico

**Sin P1/P2; aceptación estática.** Python SHA256 `121da2a38f0ca43c64e1d8e055d1a737b412577006eb2bfd27d35af839a0fcec`; workflow SHA256 `bbefd8d5db03f2a9ef9452fad43ac3e951e0d5184c6005d01bda9ca6a9e5f050`. Revisión sin navegador/GPU y sin cambios de producto.

`--sin-intro` es optativo. Sólo CI lo activa, junto a calidad baja, y el informe/stdout declaran que la cinemática se omite. Sin el flag se mantiene la introducción con LISTO y sus límites anteriores. No se cambian el contrato JS de recogida, sus premios, la comparación persistida ni los tiempos de espera.

La inyección de `window.claude.hot.data.resume=true` usa la entrada ya existente de `src/main.js:79,101,119,992–997`: boot omite introPicture, construye el juego y llama startGame. No modifica el bucle ni simula play. Está registrada antes de navegar mediante Page.addScriptToEvaluateOnNewDocument. La asignación de resume está fuera del condicional de sessionStorage: se ejecuta también después de Page.reload, mientras la fixture de partida sólo se inicializa una vez. El contexto privado sigue aislado y no se escribe en partidas del usuario.

Las guardas posteriores a LISTO comprueban IntroTimes, flying y cinematic en ambos documentos. Una introducción que se hubiese ejecutado y terminado tampoco pasa, porque IntroTimes permanece. Los fallos conservan diagnóstico, estado FAIL y retorno1. El perfil manual también se comprueba en ambas cargas.

**Evidencia propia CPU:** `botin_sin_intro_ci_revision_cpu.py` y `botin_sin_intro_ci_revision_cpu/report.json`: 14 casos PASS ejecutando main/diagnosticar reales con PrivateTab/CDP dobles. Incluyen valor por defecto, perfiles incorrectos, errores de arranque/recogida/recarga/diagnóstico/cierre y los dos rechazos de cinemática. Se verifica el script efectivamente instalado y que resume aparece sólo con el flag. Ejecutado además ese JS real en dos documentos Node VM con almacenamiento doble: primer arranque instala money321/bagvacía; tras simular money450/joyero, la segunda inyección mantiene ambos y vuelve a instalar resume. AST Python correcto. Estos dobles comprueban control e inyección, no comportamiento gráfico ni CDP real.

El nuevo diagnóstico de CI comunicado por raíz identifica SwiftShader en ese runner. La reanudación permite aislar el contrato de botín; **no corrige ni valida el vuelo lento/detenido, ni acredita una mejora de rendimiento**. La cinemática requiere su evidencia separada. El éxito fuente/paquete M1 y el del runner son comprobaciones distintas y no se dan aquí por realizados.

**Declined to judge:** causa última del avance de vuelo, comportamiento de SwiftShader, rendimiento, cinemática en CI, calidad visual, ejecución real fuente/paquete/CI y publicación.
