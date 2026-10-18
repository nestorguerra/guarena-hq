# T17 · criterio de diseño para la tela del estudio

**Recomiendo ensayar paños laterales cortos de estudio y conservar íntegro el puesto.** Es una solución doméstica coherente para una ventana junto a una mesa de trabajo. No recomiendo recortar tablero, pata, montante y respaldo para esquivar una cortina larga que atraviesa las cuatro piezas. Se acepta la dirección de diseño, no una implementación ni un resultado visual producido.

Se leyeron `estudio_final_r1/tela_r2.json` y `tela_contacto_local.json`, además de `curtainGeo` y `windowIn` en `src/houses.js`. El recibo RED informa13 triángulos de contacto con tablero,4 con pata,3 con montante y4 con panel, aun con retracción interior1mm. Son recuentos de triángulos, no una medida de profundidad o volumen; no cabe inferir de ellos cuánto habría que recortar legítimamente. Sí descartan tratarlo como un único roce menor. La reserva de ventana no cubre la tela real.

La propuesta de conservar borde superior2,225 m y elevar el inferior a1,28 m da **0,945 m de tela**, centro1,7525 m y separación vertical nominal de6 cm respecto al máximo1,22 m del puesto. Son cotas locales respecto a la planta; debe sumarse la altura de piso al colocarlas. Mantener ancho0,38 m, posición lateral/profundidad, color, material y pliegues actuales conserva el carácter textil doméstico sin añadir masas, luces ni adornos. `curtainGeo` no consume RNG: el alcance propuesto es viable sin introducir consumo aleatorio, pero debe comprobarse en el parche.

**Estilo:** esta solución puede funcionar en el estudio joven o bohemio y evita que la tela caiga sobre un área de escritura. Si sólo cambia la longitud, denominarla «cortina corta» o «paño corto»; no afirmar un recogido que no se representa físicamente. El remate quedará por encima del alféizar de0,95 m y de la zona baja del vidrio. La futura captura debe comprobar que se perciba intencional y no como dos tiras truncadas para esquivar el respaldo. El modelo previo ya son paños laterales abiertos: no se elimina con ello una cobertura total de la ventana que antes existiera.

Una cortina realmente recogida hacia el lateral podría conservar su largo y aspecto, pero requeriría otra forma de tela y nueva comprobación de su volumen. No la elegiría antes de probar la variante corta mínima. Recortar estructuralmente el puesto sólo sería defendible por un diseño propio útil —por ejemplo, una forma de tablero razonada— y medidas de contacto completas, no por sucesivas muescas en varias piezas. La evidencia actual no justifica ese camino.

**Alcance recomendado:** parámetro opcional de tela en `windowIn`, predeterminado idéntico a T16; activación sólo cuando la habitación de la ventana sea estudio y el perfil optante sea artista/estudiante/músico. Los llamadores de las ventanas superiores conocen `up0.type`/`up2.type`; el cambio no necesita inferir por semilla, cámara o proximidad casual al escritorio. Preservar número de paños/mallas, top, hueco, vidrio, alféizar, persiana, vista exterior, luces, RNG y toda ventana no optante. Annie usa constructor propio y debe seguir excluida, con comprobación de conservación; no basta deducirlo de la intención.

**Antes de cerrar:** comprobar cero intersecciones con triángulos reales de tela y todas las piezas del puesto, incluida su definición final; conservar el RED anterior; verificar muestras con y sin estudio/ventana y no optantes, presupuesto y RNG. Luego revisar el remate visible en3244 y1481 sin mover cámaras para ocultarlo. La dirección es adecuada para una propuesta privada, no certifica aún que1,28 sea la solución visual final ni autoriza integración/publicación.

Hashes de evidencia leída:
- `tela_r2.json`: `edbd83a03a636dfdd619ad83903ad5f99c54c8c9915ab544d0f9f9dc740264bb`.
- `tela_contacto_local.json`: `f47d832084c3be73f0aba0d00493abac64ca72e7693d695967dfefdfcdb9efe8`.

Sin GPU, API, edición de activos, implementación ni barridos; sólo lectura y este informe privado.
