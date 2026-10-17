# Cierre independiente r2

**Sin P1/P2 pendientes en r2. Los hallazgos r1 quedan subsanados; aceptación de código condicionada a integración/runtime y revisión de ficha.** Parche `3add25a47e41efade3e37542d91a0a5c5d97eb3d328847f879587e802f60bebc`.

- Repetición independiente del mismo caso bajo ventana: ahora el joyero se desplaza de z≈0,3965 a≈0,6380m sobre el apoyo y ninguna pieza invade la reserva. Recibo `comedor_t14_servicio_revision_reserva_r2.json`; r1 permanece conservado.
- Repetición independiente de cinco casas sin comedor1000–1004: todas las cotas de botín vuelven a coincidir con la base. Recibo `comedor_t14_servicio_revision_scope_r2.json`. La ruta legacy conserva yy+.02 y las mismas tiradas.
- `apoyoBotin.probar` incluye e.libres; la nueva comprobación de reservas en sobre se limita a funciones y a centrado o botin+preferir. No cambia los cinco sobre+botin antiguos de salón/trofeos/música. Los dos nuevos contratos negativos comprueban soporte bajo presente y ausencia del objeto que atraviesa ventana, incluido el servicio con jarra.
- Verificados manifiesto, diez hashes de candidato y base congelada, y scope semántico del compilado: siete objetos nuevos, cero existentes modificados/eliminados, sólo kit vivienda_comedor cambiado. `comedor_t14_servicio_revision_r2_verificacion.json`. Apply --check había pasado antes de la integración concurrente de raíz; el último readback muestra las diez activas idénticas al candidato. Este revisor no aplicó ni editó producto.
- Recibo actualizado del autor CPU200 r2:200casas,66comedores,0errores,máximo60mallas. Seis contratos CPU y negativos/mutante leídos; no presentados como ejecución propia. Coste real WebGL, recogida/recompensa/persistencia después del parche y paquete corresponden a raíz. No se repite ni se certifica aquí ese runtime.

Se conserva el diseño nuevo (servicio2/4, un foco vinculado, botín separado y fallback accesible) y los límites documentados: el RNG y las distribuciones del comedor cambian; ninguna muestra acredita todas las semillas. Un límite de60mallas en CPU deja margen nulo en algunas casas. La primera revisión de imagen debe preceder a una nueva puntuación formal. No se aprueba estética, despliegue ni partida del usuario.

---

# Revisión independiente del servicio de comedor T14

## Primera revisión (r1, histórico pendiente de corrección)

Parche `53dcd0ce1c5dd7129b499f91c15b42a4b23ce094ffe573489c32a0a627c350d9`. Sin aplicar ni GPU. **Un P2 geométrico y una ampliación incidental de alcance; autor acepta corregirlos. No cerrar aceptación con este hash.**

### P2: un apoyo de botín puede invadir una reserva alta

`src/houses.js:1196–1199` del candidato: `apoyoBotin.probar` contrasta piezas del objeto con muebles y otro botín, pero omite `e.libres`. El fallback de suelo sí comprueba esas reservas. Un mueble bajo la ventana puede ser válido y su pertenencia superar el alféizar/penetrar el hueco reservado.

Reproducción independiente CPU con la función candidata exacta, `partes`, `penetra`, `superficie`, `mapaPaso` y `caja` reales: superficie a0,87m debajo de reserva de ventana y0=0,92m; acepta joyero y sus piezas penetran1–1,8cm en la reserva. Caso sintético válido de apoyo bajo, no encontrado en las tres canónicas. Evidencia: `comedor_t14_servicio_revision_reserva.mjs/json`. Añadir reservas al rechazo de superficies y buscar otro punto/soporte o suelo; si ninguno sirve, fallar con diagnóstico.

### Alcance: cambian alturas en casas sin comedor

`src/houses.js:1238`: `yy-b.y0` sustituye `yy+.02` también cuando no se llama a apoyoBotin. Prueba propia con constructor completo CPU sobre1000–1004 sin comedor: cambia la altura de cartera, móvil, jamón, lata, portátil, hucha y consola entre7,5mm y2cm. Puede corregir un hundimiento anterior, pero amplía la intervención a otro mobiliario y no permite afirmar conservación visual fuera del comedor. Evidencia `comedor_t14_servicio_revision_scope.mjs/json`. Autor propone conservar la ruta legacy fuera del objetivo.

## Lectura del resto del candidato

Las nuevas opciones de conjunto centrado, sobre centrado/preferir y techo sobre_de no están utilizadas actualmente en esos modos por otros kits. La ordenación de candidatos sólo corre con centrado. El centro exacto conserva las mismas guardas antes del commit del conjunto; la lámpara sin referencia se omite, no queda colgada huérfana. El catálogo anterior y sus roles no deben cambiar: se añade servicio compuesto2/4, vajilla guardada y tres modelos de pertenencias. El servicio se apoya a altura de tablero y usa colisiones por piezas reales para evitar el falso AABB con patas de silla; esto no autoriza invadir reservas.

La nueva posición del foco se deriva de la luminaria y su emisor, conserva una luz física, intensidad/base y funciones de encendido/apagón existentes. La geometría de botín integrada por kit se construye en mundo y se añade sin segunda transformación; fallback se construye en origen y se transforma una vez mediante lootItem/B.extraMesh. Los IDs/defs siguen en LOOT, se conserva takeLoot/restitución a pool y la malla permanece separada para recogida. Los cuatro contratos cubren tres casas y ausencia de aparador/alacena, pero no descubrían la reserva alta omitida.

Advertencia para la subsanación: hay `sobre+botin` previos en salón (cartera/móvil/consola), trofeos y música. Una nueva guarda genérica e.botin ampliaría esos casos; acotar al nuevo modo preferir o verificar/declarar ese cambio. Esto ya se comunicó al autor.

Evidencia del autor leída: CPU200 coste/validación local,0errores,máximo60mallas; canónicas y cuatro contratos verdes con constructor/merge reales, Canvas sin raster. No repetida como prueba propia ni equivalente a GPU. Manifest inicialmente heredado de a188: se espera manifiesto definitivo de la nueva corrección.

**Declined to judge:** estética/ficha/nota formal, continuidad perceptiva de materiales, FPS/GPU, partida real del usuario, publicación y cobertura universal de semillas. El acceso y recompensa persistida que raíz ejecutó antes del parche son baseline; no validan aún este candidato.


## Adenda: selector omite botín ya recogido

Releído `src/interiors.js:1158`, SHA256 `ceb6c3bcad9db507fe633a22c3f69d0ccfadae11607bf46681b943d91f85c0af`. Sin hallazgos en el cambio de una línea. Se omiten únicamente entradas type=loot con taken verdadero antes de elegir best, evitando que una interacción terminal más cercana oculte otra disponible. No muta objeto, recompensa, estado guardado ni malla. El control defensivo en takeLoot y el caso loot siguen intactos.

Se conservan el retorno prioritario de horror mientras está escondido, el filtro de planta, el descarte de asientos ocupados/taken y todas las otras ramas. En horror activo fuera de escondite se delega el mejor objeto aún disponible. No se elimina un objeto no-loot que tenga propiedad taken.

Prueba CPU propia del cuerpo real de option con dobles de estado/acciones: siete comprobaciones pasan (lata tras joyero tomado, acción y agotamiento, no-loot taken, planta, asiento ocupado, horror escondido y delegado). Instrumento y recibo: `selector_botin_revision_cpu.mjs/json`. Esto no sustituye la repetición runtime/persistencia de raíz. El RED de `.cache/calidad/tanda14/loot_despues_r2.log` confirma el prompt ausente antes del arreglo; no se ha ejecutado GPU por este revisor.
