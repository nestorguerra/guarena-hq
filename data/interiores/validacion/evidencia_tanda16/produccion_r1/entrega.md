# Cocina T16 — candidata privada literal

Frente guardar–preparar–cocinar a dos alturas, exclusivo de cocina. Base congelada **1884bfd** (T15/Bv3+contraste vigente); HEAD posterior e9022e4 sólo añade recibos. No se ha escrito producto activo, usado GPU/navegador, ejecutado build, commit, push ni API. `datos.py` se ejecutó completo en copia privada: validación y generación privada desde JSON actual, sin copiar compilados antiguos.

## Intervención

La continuidad baja ya existía y no se reivindica como nueva. Se añade una banda alta coherente de1,23/1,5382m sobre preparación+nevera, desde1,55hasta2,19m; alacena mayormente cerrada con un nicho diario, hasta2,19m; un único trabajo de pan sobre preparación. Frentes de cocina/preparación propios y contrastados, con geometría/superficies/roles exactos de sus originales. No cambia la paleta compartida, la luz, los acabados, los marcos, la mesa ni las cámaras.

Variantes: rústica con bastidores/madera y paneles claros; lisa con frentes pintados; vajillero con un tercio abierto. Se mantiene el catálogo y las recetas originales como fallback. En2786 la alacena conserva huella.65×.30; sus paneles claros reducen el riesgo de pantalla oscura. La banda se aproxima a la cota real de la nevera en lugar de dejar la ranura previa de7cm. Esto requiere imagen, no lo acredita CPU.

## Pase optativo y rollback

Activación: programa `composicion_cocina` y entrada diferida `fase: composicion_cocina`. Precondiciones: preparación/nevera/alacena/alto originales presentes, misma zona, frentes paralelos y contiguos, ancho de banda declarado coincidente. No hay claves de semilla/cámara ni búsqueda de una nueva planta.

Se prueba, en este orden: alacena amplia al extremo de nevera; compacta al extremo; compacta en huella original. Cada prueba incluye modelos finales, huecos/puertas, límites, frente de uso.8m, reservas y acceso mediante los validadores geométricos existentes. Sólo se compromete todo el conjunto. Si falla, P, activas, guardias y siguiente U permanecen iguales a la base; el pase no consume RNG.

Se sustituyen primera alacena/alto; se despejan dependientes decorativos de preparación, alacena principal y lavadora. La lista exacta de retirados e índices anteriores/remapeados está por caso en cpu.json. Los498 retirados incluyen36 muebles reemplazados y462 adornos sin función/botín actual. `sop/sup/de/e` quedan válidos. Un dependiente con rol, asiento, botín, interacción o venta —también los campos reales de entrada e.interaccion/e.vende— obliga a conservar íntegra la base.

El K efectivo por estancia modifica identidades y reservas, sin mutar KITS. `entradasEfectivas` y traza acompañan sólo el compromiso. revisar() conserva suelo de cuotas/obligatorios/activas desde receta global y hogar/área/fases, aunque falte metadata; modelos nuevos exigen metadata, actividad y reservas. La actividad diferida no se exige en fallback.

Justificación: `pared` sólo centra sobre una referencia. Adelantar un grupo ampliado cambia el RNG antes de mesa/sillas y no preserva los cuatro fallbacks. El pase tardío acotado reutiliza guardas existentes y evita extender la búsqueda general; no añade un solver de distribución.

## Evidencia final

- **22 casas reales** reconstruidas, no31.18 admiten composición;3627/2606/4007/4216 conservan exactamente P/RNG/guardias/coste base.
- Constructores, geometría, lotes y validadores literales finales:22/22 sin errores local/uso; máximo59mallas. Sin wrapper de amueblado ni cambio de dimensiones/reintentos para pasar.
- Canónicas2786/3244/1594:54/56/58mallas;39.980/51.354/59.590triángulos en R1. Materiales y luces sin aumento.
- Núcleo/mesa/sillas inmóviles; roles/superficies/volúmenes de12frentes copiados exactos. Otras estancias, luces, IDs/definiciones/poses de botín y tipos de acciones de cocina conservados. Salidas hide/unhide reales a radio.34 libres en las22casas.
-13compuestos: apoyos de vajilla/pan e interpenetraciones internas comprobados. El recibo RED del primer solape de2mm se conserva en geometria_interna_red.json; puertas corregidas sin ampliar volumen.
-39kits no optantes: resultado serializable completo y siguiente U idénticos.
- Tres contratos mantenidos `tanda>=19`, ejecutados literalmente en CPU, más umbral anterior adaptado: PASS. Negativos de cuota, activas, ausencia de ambos metadatos, reserva bloqueada/reducida, pan flotante, penetración y dependientes e.interaccion/e.vende reales. No sustituye la ejecución global del runner en navegador que hará raíz.

El capturador sólo normaliza los tres sufijos de preparación. Se conserva ranking/rejilla/FOV/objetivos/altura/guardas. Búsqueda CPU completa con geometría/colisionador reales: seis poses BASE idénticas entre688 y candidato; reconoce sólo las ocho preparaciones previstas, excluye mesa/isla. No es una captura GPU nueva. Fotos futuras pueden escoger otra pose por cambio real de geometría; no se afirmarán pares fijos sin comprobarlos.

## Parches y límites

`motor.patch`: locales, metadata mínima de houses/buildLocal, validador, esquema y validación de referencias. `modelos_receta.patch`: generadores propios/receta. `contratos.patch`:3contratos19 y selector del umbral. `capturador.patch`:un predicado. Los hashes finales y fuentes están en manifest.json. Los JSON/JS generados de candidata sólo son artefactos privados; raíz debe regenerar desde sus fuentes al integrar.

Este autor no aprueba su propia candidata. Revisión independiente de código y nueva comprobación visual/formal corresponden a otros agentes. La previa geométrica de cajas no se usa como prueba final. La previsualización R1 de raíz fue revisada por publicación; no acredita la R2 artística ni4/5. Se conservan R1 y sellos previos. No hay acreditación de FPS/GPU, imagen final o publicación.

### Cierre de procedencia posterior

`revision_final.md` del revisor cierra motor0e791510…/contratos4fe8f2a3… sin P1/P2. Raíz ha integrado esos patches y el modelo R2 aceptado en su árbol local, ha subido el runner a19 y ha regenerado desde fuentes; este autor no ejecutó esa integración. `integracion_observada.json` registra los hashes leídos después, aparte de `base.json` que sigue intacto. La aplicabilidad de patches se coteja ahora contra base/ privada, porque los activos ya contienen los cambios autorizados de raíz.
