# Revisión independiente de código — tanda 6, trastero

Resultado final: **sin hallazgos abiertos en el estado releído**. Los tres detalles geométricos P3 de unión/apoyo detectados fueron corregidos por raíz y verificados después. No se modifica implementación ni se abre juego, navegador o servidor. Esta revisión no aprueba estética ni publicación.

Alcance: nuevo `tools/interiores/pertenencias_domesticas.py`, llamada de `catalogo_vivienda_a.py`, cambio de trastero en `kits_vivienda_a.py`, catálogo y kit generados. Contrastados con primitivas y agrupación de `src/objetos.js`, geometría de `src/interiores_geo.js` y esquema/contadores de `tools/interiores/datos.py`.

## Tercer hallazgo, corregido al cierre

**P3 — pata de cabra desconectada y sin llegar al suelo**, `tools/interiores/pertenencias_domesticas.py:30`. La barra entre (-0.02,0.36,-0.08) y (0.12,0.04,-0.08), radio .009, no toca el cuadro situado en z=0 ni el eje/bielas añadidos. Su cota inferior, incluso usando la envolvente conservadora, es y=0.0363926 m: queda al menos 3.6 cm por encima del suelo. El efecto es una pieza suspendida, no una pérdida de interacción o una avería del motor. Raíz lo corrigió: ahora une (-.06,.34,-.08), dentro del eje, con (.12,.005,-.08). La envolvente conservadora llega a y=.00074016 m (0.74 mm sobre suelo), sin penetrar el suelo. La receta completa vuelve a coincidir con el catálogo. No cambia el número de primitivas ni sus 3468 triángulos.

## Hallazgos corregidos durante esta revisión

- **P3 — cabeza del ventilador sin unión al pedestal**, línea 41 actual. Antes el poste acababa en y=.67 y el motor comenzaba en y=.685: hueco de 15 mm. Ahora el poste mide .68 y está centrado en .37; termina en .71 y entra 25 mm en el motor. Fuente y catálogo regenerado coinciden.
- **P3 — pedales de bicicleta sin eje/bielas**, líneas 29–30 actuales. Antes sus caras próximas estaban en z=±.085, separadas del cuadro/plato por al menos 36 mm delante y 66 mm detrás. Se añadieron eje transversal de .24 m y dos bielas en z=±.115, conectadas a los pedales y al eje. Se releyeron las tres piezas nuevas y se actualizó su coste; la bicicleta pasa de 3388 a 3468 triángulos.

## Verificaciones independientes

- Importación y generación en memoria con escrituras bloqueadas: cero escrituras y cero salida estándar. Dos llamadas independientes producen estructuras idénticas; `objetos()` coincide exactamente con `data/objetos/vivienda_a.json`.
- Los cuatro IDs son únicos; no hay primitivas exactamente duplicadas dentro de los nuevos objetos. Dimensiones estrictamente positivas y finitas, posiciones y giros finitos. Los cuatro objetos y el kit pasan el checker real de esquema.
- Las llamadas actuales a `barra` tienen igual z en sus extremos, conforme a su contrato XY. La fórmula de giro reconstruye sus extremos con error máximo observado de 1.15e-16 m. Los aros de 16 y 20 segmentos cierran con tolerancia 1e-12 m. No hay inversión de signo que convierta las barras en diagonales opuestas.
- Escalera: pies en y=0, peldaños unidos a ambos largueros. Cubo: base en y=0 y tapa unida. Mango/rodillo con unión geométrica. Se consideran pertenencias agrupadas distintas, no una única pieza física que deba unir cubo y escalera.
- Ventilador: pedestal en y=0, poste unido a base y motor tras la corrección. Aro/aspas y radios comparten orientación XY; quedan pequeñas separaciones de detalle por debajo de 1 cm que no se elevan aquí a un defecto funcional.
- Cesto: cuerpo en y=0; borde, manta, ala y copa del sombrero tienen apoyos coincidentes o solapados. El paraguas inclinado apoya cerca del suelo y es una pertenencia independiente, no requiere unirse a la cesta.
- Bicicleta: ruedas abiertas y radios sin duplicados exactos; sillín y manillar enlazados al cuadro. Cota mínima de los neumáticos aproximadamente 4.5 mm sobre suelo para los cilindros poligonales de seis segmentos, dentro de la tolerancia de 1 cm. Eje y pedales nuevos enlazados. La pata de cabra también queda corregida al cierre, como se documenta arriba.
- Kit: bicicleta/escalera son variantes de **una** entrada obligatoria [1,1]; no se fuerzan ambas simultáneamente. Estantería y cesto obligatorios, ventilador opcional. `trastero[-2]` sigue señalando la regla `sobre` con 2–4 adornos por soporte. No se han introducido lámparas, texturas, superficies de apoyo falsas, roles ni referencias inexistentes en los nuevos objetos.

## Coste geométrico

Recuento calculado de las primitivas actuales y contrastado con las recetas del motor: cilindros cerrados 4×segmentos; cajas biseladas 108 triángulos. Son triángulos geométricos por objeto, no draw calls ni tiempo GPU.

| Objeto | Primitivas | Triángulos | Envolvente aproximada ancho × alto × fondo (m) |
| --- | ---: | ---: | --- |
| Bicicleta | 132 | 3468 | 1.541 × 0.960 × 0.470 |
| Escalera y útiles | 14 | 1248 | 1.010 × 1.650 × 0.284 |
| Ventilador | 35 | 1156 | 0.461 × 0.970 × 0.380 |
| Cesto de temporada | 7 | 436 | 0.641 × 1.037 × 0.480 |

Todos quedan por debajo de 5000 triángulos por objeto. La combinación máxima de nuevas pertenencias del kit es bicicleta + ventilador + cesto: **5060 triángulos**; la alternativa con escalera suma **2840**. No es el coste total del trastero ni de la casa. Las envolventes usan vértices poligonales de cilindro y límites conservadores para cajas biseladas; no son medidas nominales declaradas a `objeto`, pues el motor obtiene su volumen de las primitivas. La agrupación existente combina metal/mate; el número de primitivas no equivale al número final de mallas.

## Declined to judge

- Calidad estética, reconocimiento de las siluetas, composición y sombras visibles de la ficha: requieren inspección visual, que corresponde al otro revisor.
- FPS, draw calls finales, buffers reales GPU y coste de una casa completa: no se ejecutó WebGL.
- Aprobación de 81 semillas, 200 casas o publicación: son ensayos de raíz, no ejecutados por este revisor; deben corresponder al último catálogo.
- Estabilidad física real de las pertenencias: el juego utiliza colisiones geométricas, no una simulación de equilibrio estático detallada.
- Persistencia de partidas reales e interacciones de todas las casas: no se cargó ninguna partida. No hay cambios de motor/guardado en el diff de esta tanda.

## Último ajuste de color

Se releyó el diff de `composicion_domestica.py`: únicamente cambian colores de estructura, baldas y cajas dentro de `mejorar_almacen`. No cambian dimensiones, posiciones, cantidad, materiales, superficies ni reglas. No se afirma que el contraste visual esté aprobado: eso requiere la ficha final.

## Huellas finales del estado revisado

- tools/interiores/pertenencias_domesticas.py: 7cb0274ca26ffab539537c5710a63d37e6a108b7ce9f8e6551328eaf5e3442a2
- tools/interiores/composicion_domestica.py: 973c3b2ae5ab3fd9518e2f3a7a93e08d0240089c24661f884895ee2b41699ccd
- tools/interiores/catalogo_vivienda_a.py: c5b9bd49298a3078d8125ac49f413519c1d7a92493c580a3f4beba68a9ae1cac
- tools/interiores/kits_vivienda_a.py: 7903c21bc99c55c3ce9c0d25b63488ec97abd0b2e325cec291f2122b484d3cef

Única escritura del revisor: este informe.
