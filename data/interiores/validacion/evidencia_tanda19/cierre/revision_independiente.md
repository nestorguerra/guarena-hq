# T19: revisiones independientes

# T19 · revisión visual R8, frente y consulta

**R8 añade un uso real y permite pasar a la evaluación formal, sin acabado imprescindible pendiente en las vistas inspeccionadas.** El banco no actúa como otra caja para llenar: asiento libre, bolsa al extremo y botas bajo la balda explican equiparse y guardar material de campo. No asigno nota, no doy por alcanzado 4/5 ni apruebo integrar o publicar.

## Avance observado

Se abrieron ambas fichas de `comparativa_r8_completa/{antes,despues}` y los originales candidatos `casa_trofeos_2132_0.jpg` y `casa_trofeos_1679_0.jpg`. El nuevo frente une armero, cajones y banco a tres alturas. Se distingue mejor una secuencia de guardar equipo, equiparse y consultar después. La huella de uso crece con una función pertinente, sin llenar la circulación de enseres pequeños.

La mesa de consulta y el orejero mantienen una relación clara. El atlas se reconoce; la manta y el cuerpo tapizado ya no presentan el defecto de R6. Las maderas medias/oscuras separan patas, baldas y tablero del suelo claro. La mejora procede de programa, masa baja y contraste local; no sólo del protocolo nuevo de cámara ni de orientar el frente de otra forma.

## Cobertura y reservas concretas

Asiento y mesa de consulta se ven completos en las tres vistas k1. Frente, cornamentas y banco entran en k0; **encuadrar sus AABB no equivale a ver todas las superficies sin oclusión**. En 2132, la biblioteca próxima tapa el extremo derecho del banco y parte de la bolsa. Aun así se leen el asiento libre y las botas; en 4204/1679 el banco queda claro. En 1679, la biblioteca se superpone al borde izquierdo del armero, conservando el arma y la función legibles. Son límites localizados de evidencia, no prueba de colisión ni razón para mover muebles o pedir otra foto.

Persisten simplificación en arma/pertenencias y paños tranquilos. El vocabulario de las tres muestras sigue siendo similar, pues comparten cazador/rústico/pasillo. No veo ahora un vacío dominante que obligue a añadir otro ámbito antes de evaluar: el banco corrige precisamente la carencia funcional material señalada en R7. No recomiendo otra estructura, alfombra o galería para perseguir densidad.

Se releyeron JSON y procedencia: seis poses, objetivos, ojo1,60/FOV68 exactos en ambos miembros; doce vistas con guardas libres y dentro del recinto, desplazamiento/profundidad nulos y sin centros dentro de mobiliario. Alta/DPR1, 494 fuentes estables por miembro según procedencia. k1 declara 16 esquinas sin recortes y rayos suficientes; k0 usa AABB durante selección y la revisión humana anterior acota sus oclusiones.

El protocolo frente/consulta es nuevo. BASE hereda exactamente esas poses, pero conserva sus objetos originales y no posee las nuevas raíces. Que algunos objetos históricos queden fuera de estas vistas no demuestra ausencia o peor función. La pareja compara las escenas desde posiciones iguales; no sustituye la cobertura histórica de BASE ni permite atribuir a arte la mejora del encuadre.

## Alcance e identidad

Cobertura visual limitada a 2132, 4204 y 1679, estética plastilina diurna. La compacta2162 sin banco no aparece aquí; su conservación es evidencia CPU separada. Leído recibo `medidas/prototipo_r8_final.json`: 58/60/57/55 mallas en cuatro casos; no se ejecutaron ni se transfieren estos resultados como verificación de interacción, coste GPU, 81/200 casos o publicación.

- Candidata JPG: `c8a411c871c821ad153645e46117ca99b7098a27bba8241c8f6e581fae7cf792`.
- Candidata JSON: `7ae8326e1801854f68520fe4164b89a24c53c47e17c7b6c3de4707d48e37a076`.
- Base JPG: `dffd1546b732a7aea20ab70b7e2e9219973ace72d8d6a6f02c2bb7ad669bd779`.
- Base JSON: `e6d2dc0533a183cc9a20d2fd1b80bc0f5581dccf6df40e9d63f113b461ef5849`.

Sólo lectura de imágenes/metadatos locales y creación de este informe privado. Sin GPU, navegador, API, nuevas pruebas de producto ni cambios activos. Se conservan dictámenes y fichas anteriores.

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

# T19 R8: revisión de integración e instrumentos privados

**Sin bloqueo nuevo en la integración del producto revisada.** El defecto de alcance del capturador se corrigió antes de aplicar. Dictamen condicionado a terminar los diez gates, regeneración, cierre documental y CI/publicación reales. No se han ejecutado aquí GPU, juego, build, gates, API ni acciones externas; sólo lectura, hashes, cálculo sobre JSON y comprobación sintáctica de instrumentos propios.

## Identidad y delta

Los494 hashes del snapshot prototipo_r8 y los417 del congelado activo coinciden. Las10 fuentes de arte/datos/generadores copiadas son idénticas al snapshot sellado34dc720c76b6965951a8b66f16bacc95d27429ba4f34630025d5785c32b1512a. Las13 copias de antes_integracion coinciden con HEAD previo. Entre archivos compartidos con el snapshot difieren el runner de contratos y el capturador. El snapshot no contiene .github/workflows/validar.yml; el workflow activo cambia 21→22 respecto a HEAD y sí está incluido en el congelado de417 archivos. El registro integrar_r8 documenta contrato16d68d671913eb7d9b8aa40907ab9a92d525cb6733231d4e5c69c191e812fd7f y fotos2b8d0305e6584178fa9a5f40684ccc610bb3fa4203e76a614276f9c1541a6b6b.

Acabado extiende la rama doméstica de salón a trofeos, mantiene la exclusión Annie y orienta acento por el armero. Houses aplica ese acabado después del kit. No se modifican el constructor singular ni luces globales. Locales añade únicamente separacion_frontal optativa en junto_a individual con frente explícito y sin grupo_pared, finita entre.06 y1; default.06 conservado. La receta de consulta pide.32, sin cambiar el resto del solver. El modelo del banco se registra como silla mediante el flujo doméstico existente.

Cuatro modelos previos compartidos cambian: vb_armero, vb_cornamenta, vb_prismaticos y vb_bolsa_caza. El catálogo añade también las nuevas piezas específicas de guardado/consulta/biblioteca/mapa/banco; no describir T19 como sólo cuatro IDs modificados sin mencionar los nuevos. Las tres amplias2132/4204/1679 reciben banco;2162 no lo recibe por área<13, aunque su área≈11.77 sí activa mesa de consulta amplia (umbral11). Cálculo sobre los cuatro recibos confirma gap≈.32. No confundir «compacta del pueblo» con el caso de laboratorio inferior a11m².

## Contratos y validación

T22 añade pruebas de frente, pertenencias apoyadas, conexiones físicas, asiento/soporte/reserva del banco, guardado conservado al omitirlo, umbrales11/13 y API de separación frontal. No se observa relajación de presupuesto: continúa60mallas/9luces. Los callbacks CPU del autor registran tres PASS y negativos efectivos sin asiento, sin reserva y con botas flotantes, restaurando configuración. Son recibos leídos, no ejecuciones propias. El recibo activo ya contiene82 contratos PASS/errores[]; al revisar, la lista secuencial sólo había confirmado el primer gate. No se da por terminada la cola.

## P2 de capturador cerrado

La primera propuesta mantenida introducía altura media para cualquier lista objetivos y veto de recortes global. Eso afectaba a cocina/baño/comedor fuera del encargo. Se informó y raíz lo corrigió privadamente: ahora ambas condiciones nuevas requieren tipo==='trofeos', y la expresión anterior de altura sigue literal en la rama alternativa. Releído parche2b8d... y recibo alcance_no_trofeos.json; capturador activo coincide con la candidata corregida. El veto final trofeos cubre proyección del frente; para frente su lista de visibilidad es vacía y no acredita ausencia de oclusión. Consulta añade rayos limitados. Las fotos privadasR8 no se reetiquetan como capturadas por esta herramienta mantenida sin whitelist; son otra procedencia documentada. No hay recaptura ni nuevo juicio en este pase.

## Helpers

integrar_r8.py exige árbol limpio, hashes previos/snapshot, apply-check, respaldo13, copias acotadas y freeze; el recibo actual confirma ese resultado. Es reversible mediante copias, no una transacción automática ante fallo intermedio. No lo he ejecutado.

verificar_banco.py emplea selector real→sit→standUp y collider.34 antes/después. Las guardas finitas añadidas evitan que NaN/Inf pasen la comparación. Su alcance es mecánico dirigido: elimina residentes, reposiciona al acceso y no acredita recorrido desde puerta, dinámica con residentes ni evaluación visual completa. No es un probe de paquete: importa objetos desde /src. Esto es válido para el gate fuente declarado, pero no debe sustituir prueba del código empaquetado/publicado.

El probe público nuevo está separado en revision_publicacion/verificar_publico.py y trofeos_publico.js. Conserva ocho casas, estudios/salones anteriores, Annie/caja/siesta/decoración, tres comercios y recarga privada; añade cuatro puertas reales de trofeos. Usa sólo objetos reales del paquete, sin imports /src. Mantiene residentes, exige banco único/registro exacto en tres amplias y ausencia en2162, gap.32, vínculos de frente y premios conservados. Selecciona por Seats.near, llama Seats.sit/standUp, comprueba modo/pose/registro, salida prevista por el método real, collider y límites del recinto, controles/patrimonio y reposición de fixture restaurados. No asigna flags de sentado ni cambia catálogo/colliders para pasar. La reposición es explícita; no afirma haber caminado desde la puerta ni evaluar la animación por píxeles. No se ejecutó aún.

## Estado visual y publicación

Se acepta como evidencia ajena la revisión artística parcial R8; no se repuntúa. A3.306/B3.368 no constituye4/5 ni mejora25% de carga. La revisión de integración no anticipa CI/Pages ni sustituye el gate pendiente del banco real. El cierre/publicador nuevo se prepara aparte y raíz debe leerlo antes de ejecutarlo con el SHA/CI efectivos.

## Huellas

- `estado_candidato.json`: `56d72d622301b55094f5af4a575cf71ddeb6ff6820ad7581754b2054fc5d622e`.
- `integracion_r8.json`: `f29a4fb92f7452cfeb1906624f76fbefe4a6eb369ad879f8eaef8bbeafa97abe`.
- `integrar_r8.py`: `2eff75b850a7bfb265e1a9b2d648988cc1e50720076499c7b81571bffcd72858`.
- `verificar_banco.py`: `962435e5e6c6a1628723312e5f907e4eafbc3a115fe8918118e75ca2fb746972`.
- `fotos_mantenidas/fotos.patch`: `2b8d0305e6584178fa9a5f40684ccc610bb3fa4203e76a614276f9c1541a6b6b`.
- `contratos_t22_r8/contratos.patch`: `16d68d671913eb7d9b8aa40907ab9a92d525cb6733231d4e5c69c191e812fd7f`.
- `contratos.json`: `80c6991213a565c128f29a7334c8662b8e2524be0f71399862794f6d61f511c8`.
- `prototipo_r8/preparado.json`: `34dc720c76b6965951a8b66f16bacc95d27429ba4f34630025d5785c32b1512a`.

Errata documental: corregida la afirmación de presencia del workflow en el snapshot. El hash anterior del informe era5e262380822623ba06abf7fa27765da94b7a7ae10b6bfb7c109f9236a7cda67e; no cambia el resto del dictamen.
