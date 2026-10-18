# Revisión instrumental · capturador consulta R7

**Aceptación instrumental acotada, sin P1/P2 demostrado en la pareja producida.** No constituye nota artística ni autorización de publicación. Fuente revisada: `capturador_consulta_r7.py`, SHA `2f2570cfd76ce7a4406e615811e448e59e0fb1e4c2cc5fafb2525e53e50e8dd2`.

## Comprobación independiente sin GPU

`preflight.py/json` reconstruye las sustituciones del JS de ambas ramas sin importar el cliente de navegador ni invocar main; comprueba sintaxis Node de ambos resultados. También relee la pareja ya creada por raíz:17 archivos coinciden con los hashes de procedencia, tres semillas idénticas, seis poses exactamente iguales en x/y/z/objetivo/FOV, alta y DPR1 en ambos lados, doce vistas con clearance antes/después libre. No se ejecutó JavaScript de escena, navegador ni API.

Los494 inputs actuales de BASE y los494 de R7 coinciden con sus respectivos sellos. Las imágenes/JSON de salida no forman parte de esos494 inputs. El capturador no los modifica; escribe en .snaps y fichas de las copias privadas. El script no incorpora por sí mismo una verificación de hashes al principio/final: la estabilidad histórica declarada durante la captura corresponde al wrapper/recibo de raíz. La lectura actual independiente acredita coincidencia actual, no observación retroactiva del proceso.

## Ámbitos y geometría

K0 conserva la búsqueda general heredada y se etiqueta frente_general. No tiene objetivos específicos armero/bajo ni una guarda de sus esquinas: el nombre no debe interpretarse como certificación de cobertura completa del frente. Esto queda sujeto a lectura visual.

K1 candidata exige exactamente las dos raíces de consulta existentes (sillón y mesa),16 esquinas proyectadas sin recortes en margen.94 y cámara en el hemisferio frontal del asiento. Construye ghosts exclusivamente para raycast a partir de las mismas partes/posiciones; no se añaden a la escena. El material doméstico cambia sombreado, no esa geometría. Los cinco rayos buscan primero un triángulo de la raíz y luego obstáculos reales hasta5mm antes: evita contar su propia cara como oclusor. Exige al menos3 impactos medidos y60% libres por raíz, antes de seleccionar y tras actualizar matrices para la pose final. Las geometrías ghost se liberan antes de render.

Las tres vistas K1 registran16 esquinas/0 recortes; fracciones de visibilidad .8/1 en2132 y1/1 en4204/1679. Cinco rayos no demuestran visibilidad de cada píxel del objeto: el instrumento lo limita expresamente y requiere revisión humana. No se transforma esa muestra en una certificación de legibilidad artística.

Las poses se filtran contra puntos CPU libres en ambas construcciones, y navegador vuelve a exigir collider sobre copia, depth/delta≤1e-6, límites de sala, ausencia de contención OBB y centro de círculo. Repite clearance antes/después de render y comprueba pose inmutable, errores de consola, shader runnable y HTTP de guardado.

## BASE y simetría

La rama BASE desactiva consulta antes de ejecutar JS: no exige IDs nuevos, no construye ghosts ni inserta mobiliario. Reutiliza pose/objetivo/FOV de la metadata candidata; valida altura/fov y clearance de la pose aplicada. No atribuye cobertura de raíces candidatas a BASE, y sus JSON no incluyen cobertura_consulta. Las seis poses guardadas son exactamente iguales por comparación independiente.

La búsqueda residual de BASE previa al override puede fallar de manera conservadora si no encuentra candidato; no cambia la pose canónica para conseguir PASS. En la pareja observada terminó correctamente. La nueva selección favorece la documentación de consulta en ambos lados por igual; no es equivalente al protocolo histórico ni permite adjudicar la mejora de encuadre al producto.

## Límites restantes

No se han puntuado JPG ni validado comparabilidad completa de iluminación/residentes mediante trazas; el cambio examinado conserva el protocolo heredado de fotografías. Tampoco se acredita ejecución propia de GPU, conservación histórica antes/durante más allá del recibo de raíz, ni un gate global. Para un uso aislado futuro, el wrapper debe seguir sellando inputs, comunes, metadata y salidas; no basta ejecutar este archivo y afirmar que él verifica494 fuentes.
