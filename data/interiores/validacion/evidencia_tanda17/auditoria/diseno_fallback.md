# T17 — decisión técnica de diseño del fallback

**Recomiendo conservar el motor y aceptar la receta nueva colocada individualmente cuando complete el programa y pase las mismas guardas. No exigir ahora un retorno íntegro a T16.** Fallar el intento de grupo no equivale a fallar el estudio; el encargo pide función, paso y calidad, no conservar las poses antiguas ni una única alineación. Esto es una decisión de diseño condicionada, **no aprobación del producto T17**, cuyos gates81literal/200 aún están pendientes.

Revisados45hashes del sello R1, receta, grupo_pared, fallbacks y negativos; sin ejecución de barridos ni intervención en el orden R2 del autor.

## Por qué basta, si se valida

`src/locales.js:535–646` intenta el grupo antes de comprometerlo y, al fallar, ejecuta las reglas individuales de las mismas entradas. La raíz nueva mantiene mesa+silla_frontal; biblioteca y bajo siguen siendo obligatorios y ligados por de, con si_no:false y sus reservas .75×.80/.70×.80. Ordenador y consulta aplicable mantienen mínimos. No hay motivo para sustituir un estudio completo y accesible por T16 por el mero hecho de no haberse colocado en el primer intento conjunto.

Se deben evaluar relaciones de uso, además de cuotas: silla ante mesa; biblioteca y bajo accesibles y ligados al trabajo; lectura/cajones/puestos conservados; paso doméstico.8, entrada y acciones reales alcanzables; apoyos/huecos y presupuesto≤60 sin excepciones por semilla. Un amueblado individual que rompe la intención funcional no queda aprobado sólo porque tenga los objetos.

## Lo que R1 acredita y lo que no

`fallback.json` **no es un positivo de estudio individual válido**: conserva exactamente2lámparas y registra6entradas ausentes (10,11,12,13,18,20). Es útil para demostrar que un grupo rechazado conserva el resultado y las siguientes extracciones U de la receta individual, y que no transforma un recinto bloqueado en PASS. No demuestra conservación de un estudio completo ni retorno a T16.

La segregación de perfiles conserva la receta T16 elegible para familia/Annie; es distinta de la recuperación por falta de espacio para un optante. Su conservación de funciones está ensayada aparte. No llamar a ambas cosas «fallback completo».

## Cierre mínimo recomendado

Terminar la prueba de ordenR2 sin ampliar solver. Antes de producción, exigir los gates finales81laboratorios literales con marco original y200casas, más el contrato dirigido de silla/funciones/reservas. Si se permite la ruta individual como resultado positivo, conservar al menos un caso no vacío que realmente rechace el grupo y complete la receta individual, y un negativo que pierda una pieza obligatoria y siga fallando. Mantener semilla solicitada/efectiva, W/D/H/puertas/huecos, reintentos y fallos visibles; nunca arreglar el recibo cambiando dimensiones o perfil ni tomar los datos producidos como autoridad para rebajar cuotas globales.

No implementar una segunda receta por anticipación. Si los gates muestran un no-fit real del programa nuevo en un marco legítimo, revisar primero orden o variante de tamaño con las mismas funciones/reservas. Sólo si eso no ofrece una solución proporcionada se justifica diseñar selección declarativa de receta completa, antes del montaje, con ambas alternativas explícitas en KITS, RNG reiniciado desde la semilla acordada y ninguna mutación global ni mezcla parcial. Esa ampliación requeriría encargo y revisión propios; hoy añade estados, validación y riesgo sin fallo positivo demostrado que la haga necesaria.

La propuesta R1 debe ajustar su frase de «fallback completo antes de producción» a este criterio si raíz lo adopta. No se elimina ningún requisito de función ni se declara válida la ruta individual actual sin evidencia. No se afirma garantía universal por81/200, ni se juzga imagen, materiales finales, GPU, acciones ejecutadas o publicación.
