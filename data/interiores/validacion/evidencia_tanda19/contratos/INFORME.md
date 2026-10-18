# T19 R8 · revisión independiente y contratos T22

**Sin P1/P2 pendiente en el alcance dirigido. Preparado para validación integrada; este informe no certifica navegador, calidad artística ni publicación.** Revisión del banco nuevo, su receta, consumidores de asiento y catálogo R8 congelado. Las fuentes activas y los snapshots no se han escrito por este revisor. Raíz comunicó después la integración reversible y el inicio de los gates; sus resultados todavía no forman parte de este dictamen.

- Parche mantenido, sólo `tools/interiores/casas_pruebas.js`: `16d68d671913eb7d9b8aa40907ab9a92d525cb6733231d4e5c69c191e812fd7f`.
- Fragmento literal: `1be00296af3ea9bfd37779661d7b09b77177f6273a354719e1a082558f595929`.
- R8 `preparado.json`: `34dc720c76b6965951a8b66f16bacc95d27429ba4f34630025d5785c32b1512a`; 494 archivos cotejados antes y después de cada ejecución literal.
- R7 y sus negativos permanecen en `../contratos_t22_r7/`; R5/R6 y el falso fallo de margen anterior se conservan sin sobrescritura.

## Resultado ejecutado

`cpu_positivo_prototipo_r8.json`: **3/3 callbacks literales PASS**, construyendo las cuatro casas reales 2132, 4204, 1679 y 2162. Usa HouseBuilder, geometría y agrupación Three r170, amueblar y validadores reales del snapshot; Canvas y carga de texturas son dobles. No WebGL. Se comprueba restauración del prototype y de los conjuntos de identificadores temporales de OBJETOS/KITS.

Se mantienen íntegros los controles R7 de rifle independiente/recompensa/apoyo y penetración con padre, prismáticos/recompensa, dos trofeos con referencias y unión física placa–astas, orejero/montantes, consulta amplia/compacta/atlas, pool adulto mínimo 30 efectivo, biblioteca/read, cómoda/drawer y caller real del acabado. Se mantiene también el callback API autónomo de `separacion_frontal`, con default/RNG/reservas y entradas inválidas.

El catálogo R7→R8 agrega únicamente `vb_banco_equipo_campo`; las diferencias de los objetos ya existentes se limitan a colores de partes. Se compararon todos los campos al eliminar sólo `c` recursivamente: ninguna diferencia restante. No se atribuye a R8 invariancia de colores ni de colocación global: añadir el miembro optativo puede cambiar la distribución y consumo posterior del kit.

## Banco y uso real registrado

Banco de 1,14 × 0,44 m, CARRY/masa 20, rol silla y un puesto a la izquierda. Se comprueba en cada constructor su relación `de` con el bajo, alineación y separación lateral de 4 cm; conserva grupo, `si_no:false`, carácter optativo y mínimo de área. Las tres primeras casas lo admiten; 2162 (11,767969 m²) lo omite.

El punto del asiento cae dentro del cojín, a su altura real 0,505 m, y tiene exactamente un registro `pieces.seat` con `chair:true` y orientación correcta. La reserva .70 × .65 se coteja contra piezas ajenas y espacios libres. No se supone que esa reserva central sea equivalente a la del asiento lateral.

Se prueba además un punto frontal literal sobre el eje del asiento, a 0,40 m del borde del banco. Es libre y conectado en el mapa real de paso de ancho 0,80 en 2132/4204/1679; está a 0,58 m del asiento, dentro de la selección real `<1,25`. Inyectar una obstrucción física en ese punto lo invalida. Este control prueba selección accesible; no ejecuta sentarse/levantarse ni certifica el destino de `standUp`. El mapa conserva la política existente de elegir inicio libre cercano; no se presenta como prueba adicional del origen literal de entrada.

## Apoyos y negativos

Dos suelas apoyan sobre la balda a 0,125 m; la bolsa sobre tablero a 0,46 m. El oráculo construye triángulos de la balda/tablero y lanza cinco rayos verticales sobre la huella plana interior de cada pieza redondeada: cuatro esquinas interiores y centro. Exige contacto vertical 1e-6. No exige que las esquinas exteriores del redondeo sean planas.

Los negativos internos elevan botas o bolsa 2 cm, y desplazan las suelas fuera de la balda; todos deben rechazarse. La lectura de geometría confirma continuidad nominal de cuerpo/caña y asa de bolsa; estos contactos estructurales no se declaran sin penetraciones: hay uniones deliberadas. El puño de las botas es una superficie oscura, no una cavidad modelada.

El tercer callback es una fixture parcial explícita: guardado obligatorio en pared y banco optativo con la entrada real. En 4 × 4 m admite ambos; en 2,25 × 6 m (área suficiente, pared insuficiente) conserva sólo guardado; por debajo de 13 m² omite banco. Aumentar únicamente su reserva frontal a 5 m también debe omitirlo y conservar guardado. No se cambian reglas de producción ni se presenta la fixture como laboratorio completo.

Negativos externos sobre el mismo fragmento final:

- `banco_botas_flotantes`: primer callback FAIL por apoyo físico; API y fixture PASS.
- `banco_sin_asiento`: primer callback FAIL por asiento propio ausente; restantes PASS.
- `banco_sin_reserva`: primer callback FAIL por reserva frontal reducida; restantes PASS.

Cada ejecución terminó correctamente al observar el FAIL esperado, restauró temporales y mantuvo los 494 hashes. Sintaxis y `git apply --check` pasaron antes de que raíz integrase el parche. El contrato R8 agrega controles; no elimina negativos ni rebaja aserciones R7.

## Límites / Declined to judge

No se ejecutaron GPU, navegador, API, build, gates 81/200 ni interacción/persistencia del jugador. Las acciones se comprueban como registros y recompensas del constructor. No se certifica coste global: 58/60/57/55 mallas procede del recibo CPU de raíz `medidas/prototipo_r8_final.json`; el gate integrado es independiente. No se puntúan imágenes, encuadre, densidad, mérito artístico ni objetivo 4/5. No se certifican CI, publicación o despliegue.

Reproducción: `node .cache/calidad/tanda19/contratos_t22_r8/probar.cpu.mjs positivo .cache/calidad/tanda19/prototipo_r8`; sustituya `positivo` por los tres modos negativos anteriores. Los scripts sólo escriben recibos privados. No reejecutarlos durante un gate que exija aislamiento de carga sin coordinación con raíz.
