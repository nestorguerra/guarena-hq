# Contraste infantil Bv2 — revisión visual estática

**Recomendación: conservar como candidata para combinar y revisar con juego Bv3; no cerrar el acabado ni aprobar publicación.** La pintura mejora la separación de los elementos claros y conserva una paleta doméstica cálida. La ganancia es desigual: 1296 resulta más articulada; en 4007 el gran paño ocre compite con la cama y hace más visible la falta de uso del área libre.

Revisadas las dos fichas y las doce imágenes individuales de 4007, 5045 y 1296 (uso/conjunto). Antes: `.cache/calidad/tanda15_fotos_canonicas/after`; después: `.cache/calidad/ninos_contraste_Bv2/fotos`. Bv3 no está en estas imágenes.

## Observaciones por pareja

- **4007/uso:** almohada, cabecero claro, mesilla y pequeñas láminas destacan mejor contra el fondo. La colcha amarilla sigue siendo legible por valor y por sus bandas claras, pero comparte familia cromática con la pared: no se consigue una separación cromática fuerte. El paño ocre completo domina gran parte del encuadre; la cama no gana protagonismo en la misma medida.
- **4007/conjunto:** el contraste organiza los planos, pero la gran pared ocre vacía adquiere más peso y acentúa la sensación de corredor. Puerta y armario se reconocen; siguen sin explicarse las actividades infantiles. No añadiría más saturación ni oscurecería de nuevo toda esa superficie.
- **5045/uso:** la madera clara, el cabecero y las láminas se separan mejor del azul. La colcha azul oscura conserva lectura frente al fondo medio y los textiles blancos. Se mantiene calidez gracias a madera y zonas altas claras, aunque el paño azul vacío sigue compitiendo con el conjunto pequeño del fondo.
- **5045/conjunto:** el lateral azul aporta profundidad y evita tanto blanco continuo. No resuelve la composición: puerta, armario y vacío siguen siendo casi todo el contenido. No observo pérdida de identificación de esos volúmenes.
- **1296/uso:** el fondo verde mejora el recorte de la cortina, la almohada y las láminas del cabecero. Cama, mesa y biblioteca mantienen su lectura y relación. El beneficio es local; persiste el suelo libre sin señal de juego.
- **1296/conjunto:** es la mejora más clara. Ventana y cortinas dejan de confundirse tanto con la pared; se distingue mejor el plano de la ventana respecto al lateral del armario. Verde, madera y blanco cálido conservan un ambiente doméstico sin un oscurecimiento visual excesivo. El área bajo/junto a la ventana sigue sin programa legible.

No aprecio nuevas ocultaciones de muebles ni una pérdida relevante de legibilidad de colchas o libros en estas vistas. Esto es una observación visual, no una validación funcional. La pintura tampoco añade densidad funcional ni variedad de actividad; no sustituye la intervención de juego. La prioridad sigue siendo relacionar esa área con biblioteca/lectura/juego a escala de uso, sin llenar el paso ni añadir miniaturas. En la combinación Bv3 comprobaría primero que dicha zona equilibra el paño ocre de 4007; si no, revisaría la extensión del acento antes de intensificar el color.

## Trazabilidad y límites

Hashes de todas las imágenes cotejados con ambas procedencias: coinciden. Los JSON de captura son idénticos byte a byte; se mantienen las seis poses y constan seis guardas libres. Ambos manifiestos contienen 134 fuentes; el delta registrado está limitado a `src/acabados_vivienda.js` y `src/houses.js`. No se confunde esta pareja con el anterior T14→Bv2, que sí cambiaba las cámaras.

- Ficha antes SHA256: `af3dfede018e1632607008b62f2f324ca4c0392ff55309847031bae19214023b`.
- Ficha después SHA256: `919b7b69f60cf99734c0f2fb66264af1443e60e2ccae949852073117823f079d`.
- JSON común SHA256: `17a06deaa3a8052cbdc4122f85d000ca502b94b770910f8060e4fca7da55ffed`.
- Capturador declarado común: `6881d0b2f2d528552a0480ccc43188c8a4071ea73364418df387f077ebb69cae`.
- Parche declarado: `cc5b2445555c1814d5cda804dca2d5ce53e7c9e338e85179e8c53add23d5a98e`.

La procedencia informa igualdad de luces construidas en CPU, pero no fija todos los parámetros dinámicos de captura. No afirmo iluminación causalmente idéntica en los píxeles ni atribuyo cada cambio de luminosidad sólo a la pintura. No se han ejecutado GPU, juego, API ni pruebas de función; no se han modificado fuentes de producto. Sin puntuación formal ni afirmación de alcanzar 4/5.
