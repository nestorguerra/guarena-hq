# Revisión independiente — alfombra y laboratorio doméstico T15

**Dictamen acotado: sin hallazgos P1/P2 en el parche `36741ece79bdbbfb4d2d26855a53e233e9e62b3267929eb56a37682e4ffcec42`. Apto técnicamente para integración local y gates reales; no certifica todavía el barrido de navegador ni calidad visual.**

## Lectura y evidencia

- `src/locales.js` candidato, líneas 364–379: la búsqueda sólo interviene tras el bucle aleatorio original, en entradas de objeto fijo con `suelo_determinista === true` y `obligatorio === true`. Las dos únicas activaciones del kit son las alfombras obligatorias, separadas por el umbral de área existente. Se usan las dimensiones rotadas y `origen`, y se conservan las tres guardas reales `dentro`, `libre` y `cierra`. Rejilla de 5 cm, cuatro orientaciones cardinales, límites incluidos y máximo 16.000 candidatos por entrada; no consume RNG.
- Líneas 655–669: el primer montaje se conserva tal como era. Sólo si faltan mínimos se reintentan kits `vivienda_*`, hasta doce intentos totales. W/D/H y contexto provienen del original, y la puerta se comprueba sin recolocarla. Las variables, colocaciones, iluminación y semilla de construcción se toman del intento elegido. La identidad solicitada permanece en `local.seed`; `generacion` distingue semilla efectiva, índice de intento, marco y agotamiento.
- `validar.js` sólo conserva esa metadata. No convierte una generación agotada en válida ni reduce mínimos, luz, paso, presupuesto o determinismo. `git apply --check` pasa.
- Leído `tres.json` del autor: reproduce los hashes y errores originales de 29/51/63 y obtiene ausencia de errores con intentos 1/1/0, respectivamente. Es lectura de evidencia ajena, separada de la comprobación siguiente.

## CPU independiente dirigida

`revision_dirigida.cpu.mjs` y `revision_dirigida_cpu.json`: usan `amueblar`, `buildLocal` y `revisar` reales mediante el adaptador CPU, Three y geometría reales; Canvas sin rasterizado.

1. Semillas 1 y 51, mismo hogar y contexto: colocaciones y siguiente extracción de U idénticas frente a la base cuando el azar ya funciona o la búsqueda no encuentra hueco. La búsqueda fallida sólo añade diagnóstico y contadores de guardas.
2. `buildLocal` literal 51: validación sin errores, intento 1 y semilla efectiva 104780, W=3,5/D=2,1/H=2,75/puerta=-0,75. El contexto de entrada no se modifica.
3. Recinto sintético totalmente reservado: exactamente 12 intentos, último índice 11 y semilla correcta; `agotado:true`, faltantes en todos los intentos y errores obligatorios reales conservados por `revisar`. Ninguna búsqueda supera el límite de candidatos.

## Límites y Declined to judge

- La búsqueda finita no demuestra que todo hueco posible sea encontrado. El fracaso sigue siendo visible y debe continuar bloqueando los gates.
- `faltan` reproduce la política de mínimos del wrapper doméstico; no es un reemplazo del validador íntegro ni una selección por luminosidad, densidad, coste o ausencia de colisiones.
- No se han repetido barridos de 31/81/200 ni se ha ejecutado navegador, GPU, build o CI. Los nuevos contratos y recibos ampliados del autor quedan pendientes de adenda.
- No se juzgan imágenes, calidad estética, rendimiento global ni publicación. No se han cambiado fuentes activas ni evidencia anterior.

## Adenda — contratos y controles finales

**Sin nuevos P1/P2. Aceptación estática de `contratos.patch` SHA-256 `d307663d86d2ae8d178c872e777dd82fee8e9a115d35c902925cbb2c27702bef`.** Sólo añade dos callbacks bajo `opts.tanda>=18`; utiliza los imports reales ya presentes y no modifica contratos anteriores.

El primer callback ejecuta `buildLocal` y `revisar` para 29/51/63, fija las dimensiones históricas, comprueba identidad solicitada, secuencia de semillas efectivas, primer éxito, límite de búsqueda y determinismo completo de `local`. El control de éxito previo compara P y la siguiente U al desactivar temporalmente el opt-in, con restauración en `finally`. El segundo usa una reserva que cubre toda la habitación y exige el error obligatorio de alfombra, doce intentos y marco inalterado. Son comprobaciones del resultado y del fallo real, no sólo presencia de metadata. Una futura solución que ya funcione al primer intento podría necesitar actualizar la expectativa de traza del primer callback; eso no invalida la regresión actual.

He cotejado byte a byte las líneas añadidas del parche con `contratos.inc` (`216cbb504a0b530eae7fbd98dd5f690900daa44705d076d4fe2a8df47253a23d`) y con el hash registrado en `contratos.json` (`006d68c090cee1f98d9254790f3055fb69223fdebd29c1029e367d8ffcfaf705`). El autor ejecutó exactamente esos dos callbacks y ambos pasan CPU. `git apply --check` pasa. No he repetido esos callbacks ni los barridos.

Revisados `controles.cpu.mjs` y `controles.json` (`a355b1a3e82e3029a31209244b7ca802c320d68a52cae9e13604aba5f08e58c6`), comprobando además sus agregados con Python:

- 39 otros kits, sólo semilla 1: `local` completo idéntico antes/después y errores registrados vacíos.
- 81 laboratorios infantiles **literales**: marco comparado contra su propio original, cero errores finales; los 78 que ya pasaban conservan `local` completo. Aquí ya no se usa el antiguo wrapper sintético que cambiaba dimensiones.
- 31 casas: estancias, navegación, luces y hash de geometría/transformaciones idénticos; P y siguiente U iguales en el control de amueblado; todas con hasta 60 mallas. Esto no es una nueva prueba de interacción en navegador ni un hash de píxeles/materiales.
- Reserva total: FAIL obligatorio conservado y agotamiento explícito.

La primera ejecución del callback se detuvo al detectar la integración concurrente del motor por raíz. Su stderr permanece separado. El adaptador posterior usa los originales afectados conservados en `base.json`, comprueba sus SHA y lee el candidato privado; las otras dependencias siguen sujetas a SHA. Esta adaptación conserva la comparación de fuentes prevista, no transforma aquel intento detenido en PASS. Los recibos finales siguen siendo CPU con Canvas simulado; navegador, GPU, gates completos y publicación permanecen fuera de este dictamen.
