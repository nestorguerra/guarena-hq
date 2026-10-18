# T17 · revisión estática de helpers de publicación

**Pendiente una corrección acotada en el publicador; el probe público no presenta pérdida de garantías respecto a T16 en el delta leído.** No se ejecutaron helpers, red, GPU, git push ni prueba de navegador. No existe autorización de publicación en este dictamen; SHA y CI finales siguen pendientes.

## P2 · `--ci` no identifica la validación obligatoria

`publicar_tras_ci.py:8–10` acepta cualquier ejecución que tenga el SHA esperado, estado completado, conclusión exitosa y todos sus jobs verdes. Al dejar de utilizar un run fijo revisado previamente, no exige que sea el workflow de `.github/workflows/validar.yml` ni que estén presentes y hayan pasado `validate_signs` y `validate_interiors`.

Una ejecución exitosa de otro workflow con el mismo SHA puede satisfacer esos controles. El cotejo del árbol PR/producto asegura coincidencia de contenido, pero no demuestra qué validaciones ejecutó ese run. En el repositorio existen dos workflows distintos: el de Pages tiene build/deploy y no reemplaza la batería de interiores del de validación.

Corrección mínima recomendada: conservar `--ci` explícito y validar la identidad de `validar.yml` (o identidad inequívoca de ese workflow) y presencia/éxito de ambos jobs obligatorios. No basta `all(...)` sobre los jobs devueltos, porque no exige nombres ni cantidad mínima. No hace falta otro framework. Después de esa corrección, esta observación puede cerrarse por lectura estática antes de introducir el run final.

## Controles conservados en el publicador

El resto es idéntico a T16 salvo la carpeta: HEAD exacto, árbol local limpio, hashes del estado candidato, coincidencia de árbol de producto con merge PR2, comprobación de ancestro de main, push de SHA exacto a main sin force, y relectura remota de main antes de registrar éxito. Se conserva el alcance específico al PR2 y `nestorguerra/guarena-hq`; no es un publicador genérico ni debe invocarse desde otro checkout. Esta lectura no verifica estado vivo de ninguna rama o ejecución CI.

## Probe público T17

Los cambios se limitan a paths/textos T17 y comprobación del estudio dentro de las mismas ocho entradas de vecinos. Exige los tres IDs acordados, exactamente un `vb_ordenador`, ejecuta frame/render y registra el programa. Después exige que los estudios confirmados correspondan exactamente a1594/3244. Si el inventario cambia y esas semillas salen de las primeras ocho visitas, falla explícitamente; no produce un PASS sin cubrirlas.

Se conservan SHA público obligatorio y validado al cargar y recargar, respuesta HTTP, contexto privado, fixture ficticia, ocho vecinos, Annie con caja/siesta/decoración, tres comercios sin ejecutar compras, errores de consola, recarga real y comparación de los valores de partida incluidos en la prueba. La evidencia anterior no se sobrescribe: el nombre existente del informe provoca error. La limpieza del contexto permanece en finally. Son garantías heredadas del instrumento, no una certificación nueva por esta lectura.

La nueva comprobación confirma presencia del programa y ausencia de excepción al renderizar; no demuestra apariencia, funcionamiento del PICKUP del monitor, acceso al guardado ni todas las rutas del fallback. No sustituye las pruebas técnicas y capturas previas de la tanda. No se afirma aquí que la prueba pública haya sido ejecutada.

## Hashes revisados

- T17 publicar_tras_ci.py: `3b5ed7c18821282658008d5069f7794bb3c82a80fc5654e6cfb745aa65005caa`.
- T17 verificar_publico.py: `449597a902362ab267fd5f0106d23a0739f1b42760b4e5d7755b39563af7cccb`.
- T16 publicar_tras_ci.py: `5f10e2c418967224fbc552558d36b8947fcabbe74eabb662e2aa6c2d32beeee9`.
- T16 verificar_publico.py: `3a0b1a61143767674c863676acf388cdf9102b4cdb302dfa4a3f0eb16e1106bf`.

## Adenda · P2 cerrado por lectura de la corrección

**Hallazgo cerrado. Los helpers quedan preparados y pendientes del SHA/CI finales y de su ejecución autorizada.** La versión corregida de `publicar_tras_ci.py` solicita la ejecución al repositorio explícito `nestorguerra/guarena-hq` y exige id igual a `--ci`, path exacto `.github/workflows/validar.yml`, SHA esperado, estado completado y conclusión exitosa. Además exige que existan `validate_signs` y `validate_interiors` y que todos los jobs hayan terminado con éxito. Se conserva esa respuesta como `workflow_verificado` en el recibo. El resto de los controles revisados permanece.

La corrección elimina la aceptación de otro workflow verde como sustituto del validador. No se han ejecutado el publicador, el probe, consultas API ni push en esta revisión. La comprobación del formato API con el run T16 `39085048712` fue comunicada por raíz; no se presenta como ejecución del revisor. La actualización futura del contrato CI de tanda19 a20 aún no se da aquí por aplicada o verificada.

Hashes finales releídos:
- `publicar_tras_ci.py`: `40a396e6696d86b973f7a81e17e935a46cd0e56a1f67269fc3de080c17f59805`.
- `verificar_publico.py`: `449597a902362ab267fd5f0106d23a0739f1b42760b4e5d7755b39563af7cccb`.

Se conserva el informe inicial como historia del hallazgo. No se ha revisado la copia mutable de modelos ni se aprueba publicación o calidad visual.
