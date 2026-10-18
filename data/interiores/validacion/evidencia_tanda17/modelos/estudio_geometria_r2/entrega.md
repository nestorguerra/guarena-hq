# T17 — greybox R2: mesa, bajo y biblioteca

**R2 está preparada para revisión/captura privada, sin integración.** La única variante cambia el orden del frente a **mesa → bajo → biblioteca**. El grupo completo entra en el primer intento en las tres muestras y respeta los huecos originales. La mejora de visibilidad desde la entrada todavía no está demostrada: falta la comparación en juego de raíz.

## Motivo y delta exacto

Se leyó la revisión `../revision_visual_greybox.md`, SHA `fe813f3402c909ee6ac11bb0be51883014355b581beca741b8a066bf2fb82848`, y se vieron la ficha R1 y los dos diagnósticos de entrada 1594. El punto físico/FOV75/alta/DPR1 del diagnóstico son iguales; cada orientación sigue su mesa real y no constituye una mirada fija idéntica. La obstrucción parcial observada por el revisor justifica ensayar una transición baja entre el puesto y el volumen alto.

No cambia ninguna dimensión, pieza, superficie, material, reserva, mínimo, perfil, luz, cámara, semilla solicitada ni motor. El JSON intercambia las dos entradas de bajo/biblioteca y actualiza sus `de` inmediatos. El motor existente genera los índices `e/de/sop/sup` del nuevo orden:

`mesa (P0) + silla (P1→P0); bajo (P2→P0); biblioteca (P3→P2); ordenador separado (P4, sop0/sup0)`.

El catálogo/modelos R2 es byte a byte idéntico a R1. Lo mismo ocurre con todas las fuentes del motor/constructor/validación/acabados. `integridad_r1_r2.json` sólo encuentra dos JSON de estudio distintos y el JS privado regenerado. Uno de esos JSON es un duplicado exclusivo de las sondas CPU; el parche de previsualización incluye sólo el kit principal y los objetos grises necesarios sobre T16.

R1 queda intacta, incluido su manifest `63461d72a6baaa29da7968773a23c6dcb8b12eea96cc71b26938c0d615533f07`. No se reutilizan sus recibos como prueba de R2: se han vuelto a ejecutar con el JSON literal final.

## Tres muestras, marcos fijos

| Semilla / perfil | Marco útil W×D×H (m) | Seed efectiva / intento | Relación R2 | Mallas / triángulos / luces |
|---|---|---|---|---|
| 3244 / artista | 5,4693×3,3143×2,75 | 425071 / 0 | N; mesa x−0,0546, bajo1,0854, biblioteca2,0754 | 56 / 48.206 / 8 |
| 1594 / estudiante | 4,3609×2,1500×2,75 | 208904 / 0 | N; mesa x−1,0005, bajo0,1395, biblioteca1,1295 | 58 / 58.358 / 8 |
| 1481 / músico | 4,1611×3,4125×2,75 | 194118 / 0 | W; mesa z0,68, bajo1,82, biblioteca2,81 | 58 / 43.216 / 8 |

Las dos primeras son las dos casas con estudio del inventario documentado de 22 identidades. 1481 sigue siendo una canónica sintética, no otra casa real de ese inventario. No se atribuye cobertura a 31 estudios.

En 3244 cambia la posición del frente al resolver la misma cadena con el orden nuevo; no se ha fijado ni buscado una posición por semilla. En 1594 y 1481 el puesto conserva su pose R1 y los dos guardados intercambian su relación. Todas las búsquedas son las ya existentes en el motor, sin otra rejilla, heurística ni ensayo de posiciones añadido.

`huecos.json` comprueba piezas reales de todos los objetos frente a las reservas originales de puertas/ventanas, con límite0,005 m: **penetración máxima 0 en las tres casas**, incluida ventana de 3244. No se redimensiona la estancia, el ordenador ni la biblioteca, ni se rebajan las reservas para conseguirlo.

## CPU completada

- `fit.json`: tres programas finales completos en intento0; vínculo raíz–bajo–biblioteca y silla frontal correcto; validadores geométricos sin errores.
- `full.json`: constructor, agrupación y validadores literales de 22 identidades de pueblo + 1481. Tres estudios sin errores de estancia/uso; veinte controles sin estudio conservados. Marcos/rooms, otras estancias, botín con definiciones/poses y acciones del estudio conservados frente a T16; luces físicas exactas. Máximo de la cohorte59 mallas, inferior a60.
- El puesto sigue ofreciendo 0,60×0,30 m libres de escritura. `vb_ordenador` conserva su definición/clase PICKUP y apoyo independiente. Penetración con el soporte 0; el negativo que lo desplaza 4 cm hacia el respaldo detecta 1,75 cm de penetración.
- `annie.json`: semillas 12/13, cinco estancias y construcción T16 exactas en geometría/poses/materiales/colliders/acciones y posiciones, 60 mallas/9 luces. Las reglas activas T16 se conservan tras resolver el filtro de alcance; el JSON global sí incluye esos filtros declarativos y el programa optante para artista/estudiante/musico. Los otros kits/pools no incluyen IDs nuevos.
- `negativos.json`: recinto totalmente reservado sigue fallando tras 12 intentos literales con marco/puerta fijos; libro elevado 4 cm falla apoyo; objeto en frente de biblioteca falla uso; silla retirada falla vínculo. No se han convertido esos FAIL en PASS.
- `datos_greybox.log`: validación/regeneración privada de datos completa, sin errores. No se copia ningún compilado a la raíz.

Se usan THREE r170 real, constructor/agrupación/collider y validadores actuales con Canvas sin raster. Esto no mide GPU ni apariencia final. Mismos modelos grises y entradas de contenido que R1; no hay modelos finales o acabado R2 combinado.

## Fallback: límite conservado, fuera de esta sonda

`fallback.json` sólo comprueba que fallar el grupo conserva la receta individual y las siguientes extracciones RNG. Su caso tiene lámparas y mínimos ausentes: **no es un positivo de programa individual válido**.

La revisión posterior de producción exigirá un caso no vacío donde no quepa el grupo pero sí el programa individual completo con paso 0,80 y presupuesto, además de 81 montajes literales / 200 casas. No se exige conservar poses T16 si la nueva colocación individual es funcional. No se añade selector, solver ni retorno a poses legacy en esta sonda, y no se han hecho esos barridos adicionales ahora.

## Artefactos y siguiente comprobación

- `planta_r1_r2.png/svg`: planta R1 sellada frente a R2. El tablero señalado en azul conserva la misma superficie útil; la anotación no representa una función nueva de R2.
- `planta_comparacion.png/svg`: T16 frente a R2.
- `greybox_r2_contra_t16.patch`: objetos R1 sin cambios + receta R2, para una copia privada T16.
- `orden_r2_contra_r1.patch`: sólo el cambio de orden/de en el JSON principal, para el preview R1 ya montado.
- `manifest.json`: nuevo sello; `procedencia_r2.json` mantiene la cadena T16→R1→R2 y el dictamen que autoriza la variante.

Los dos parches son alternativas de base, no deben aplicarse uno tras otro. Tras aplicar uno en la copia privada, regenerar allí `tools/interiores/datos.py`; no ejecutar generadores catálogo/kit ni copiar el JS compilado privado a otra versión.

Falta que raíz capture las canónicas con el mismo método y el diagnóstico de entrada 1594 con la misma posición/FOV y criterio de mirada a la mesa. Se documentarán las poses automáticas que cambien por seguridad. No se presupone que la oclusión haya desaparecido ni se cambiaron cámaras para mostrar un resultado favorable.

Sin fuentes activas, GPU, navegador, API, build, puntuación, commit o publicación. El acabado privado de raíz y el fallback de producción siguen fuera de este sello.
