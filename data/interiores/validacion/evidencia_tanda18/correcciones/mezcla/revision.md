# T18 — mezcla finita de las dos rutas de paredes

Propuesta técnica favorable para ensayo e integración local revisada por raíz. No es cierre del gate navegador ni aprobación de reutilización de imágenes R4. Dos parches separados: producto.patch (únicamente houses.js) y contrato.patch (un callback acumulativo tanda21).

## Cambio

Un helper local copia la lista de paredes y ejecuta Fisher–Yates descendente con el RNG local de la vivienda. Sólo onWall y plant sustituyen sus sort con comparador aleatorio. Para cuatro paredes siempre son tres extracciones; listas vacías o unitarias no consumen ninguna. El rango de mulberry32 es [0,1), por lo que cada índice cae entre 0 e i y cada pared aparece una vez. No muta el argumento original. No cambia Room.fit, reservas, cuotas, kits, función de RNG ni las demás ordenaciones legacy.

La traza de navegador aportada por raíz conserva el FAIL y acota la primera divergencia de sitio a las comparaciones de onWall. Un comparador aleatorio no cumple el contrato de ordenación; su número de llamadas no debe gobernar decisiones de juego posteriores. La reparación elimina esa dependencia en las dos rutas acotadas, sin afirmar que el resto legacy ya sea independiente de sort.

## Evidencia privada CPU

Callback mantenido ejecutado literalmente con constructor real3244, Three/HouseBuilder/locales/acabados reales y houses candidata: PASS, admisión de lectura y pertenencias no vacías, revisarUso sin errores. Una guardia temporal de Array.prototype.sort rechaza ordenar las cuatro paredes con un comparador; todos los demás sorts delegan al original. Se restaura en finally antes de disponer geometrías. Es una guardia estructural deliberada de estas rutas de la fixture, no un inspector universal de pureza de comparadores.

Dos mutantes independientes vuelven a la llamada anterior sólo en onWall o sólo en plant: ambos dan RED por la guardia y restauran sort. Así se demuestra que la fixture atraviesa ambas rutas. Ocho pruebas puras del helper literal cubren listas de0/1/2/4paredes con valores RNG0 y casi1: permutación válida, copia separada, entrada intacta y consumo0/0/1/3.

Par adicional3244 con configuración de lectura retirada/restaurada: acciones y recompensas por id/type/label/def/r/crack idénticas, admisión real y revisarUso0. No se presenta como reproducción de toda la suite calentada del navegador. Sintaxis y git apply --check de ambos parches PASS.

## Riesgos y límites

La secuencia de rhouse cambia una vez respecto a T17/R4. Pueden cambiar decoración del hall y patio, pozo/árbol y posiciones de sobrantes; onWall puede alojar el cuadro recogible, así que tampoco se presume invariancia de todas las poses de botín. Las definiciones de LOOT y recetas no se editan. Los callers legacy de estos dos helpers también recibirán la nueva mezcla; sus otras ordenaciones quedan intactas. No se debe prometer que toda casa o captura se conserva sólo porque el postpaso no consume U.

Antes de reutilizar juicios R4, comparar escenas canónicas y las invariantes declaradas con las nuevas fuentes; si hay diferencias visuales relevantes, recapturar. Repetir los gates que raíz determine sobre el congelado final. No aumentar límites ni suprimir la aserción que detectó well. CPU usa Canvas de trazas y texturas placeholder: no prueba GPU ni estado del navegador tras la suite. No se han alterado fuentes activas, snapshots, evidencia original, CI o publicación.
