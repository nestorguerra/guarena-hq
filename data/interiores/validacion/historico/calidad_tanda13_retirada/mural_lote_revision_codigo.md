# Revisión independiente · coste del mural

**Aceptación estática condicionada; sin hallazgos P1/P2.** Parche SHA-256 `d6a8c11bd0a739b4cd6fe201b41e43e5a195cce2131f5beb8dc0a90b4153bc39`. Raíz lo ha aplicado durante el cierre: los tres archivos activos coinciden exactamente con los hashes candidatos del manifest. Raíz confirmará coste y render en navegador. El intento anterior de 61 mallas permanece como evidencia fallida.

Ámbito: `src/objetos.js:146`, `src/acabados_vivienda.js:117` y contratos de `tools/interiores/casas_pruebas.js`. No cambia presupuesto, agrupador, geometría de muebles, posiciones, RNG, luces o flags de sombra.

La fábrica materialDibujoDomestico reproduce los parámetros del material existente para canvas domésticos no emisivos y sin recorte. He comparado sus parámetros serializados con Three r170 CPU: iguales, con la misma textura de entrada. Recibo mural_lote_revision_material.json. La imagen sintética no se rasterizó ni serializó; no se afirma igualdad visual por esta prueba. Las ramas de emisión, recorte y comercio conservan su construcción previa.

El mural adopta esa familia y coincide con su clave de agrupado: mapa atlas, roughness .7, defines domésticos y emissiveIntensity0, además de los demás parámetros. Conserva castShadow=false/receiveShadow=true. La reducción se consigue compartiendo un lote, sin ocultar el plano, quitar muebles ni eliminar su recepción de luz. La importación desde objetos no introduce un ciclo.

Existe un cambio visual real del mural: roughness .94→.7 y sus defines pasan a los de los dibujos domésticos. No equivale a conservar exactamente su respuesta previa a la luz. Requiere recaptura; no modifica su geometría ni el dibujo nativo de 128 px.

El contrato adaptado localiza las dos caras dentro del rectángulo mundial del mural, aunque estén en un lote mayor. Exige dimensiones, altura de planta, dos caras, mismo lote, flags de sombra, ausencia de emisión y span UV de 128 píxeles efectivos por eje. El nuevo contrato de coste construye 4034/6291/8030 y lee el presupuesto real; no aumenta el límite. Conserva composición T15 y las reservas negativas del mural.

He leído el recibo CPU completo del autor y su instrumento: buildVecino, RoundedBoxGeometry, mergeGeometries y agrupador reales r170, Canvas sin raster y texturas externas representadas mediante sus identidades/wrapping. Reproduce 61→60 mallas en las tres semillas; triángulos 40126/45072/44196 y ocho luces por casa permanecen iguales. Estancias idénticas. Es evidencia geométrica útil, distinta de un benchmark o validación visual. No la he repetido ni reescrito. El autor puede añadir evidencia geométrica sin alterar el parche.

Comprobaciones propias: diff completo, hashes de los tres candidatos y su integración activa, sintaxis JS de los tres archivos, git apply --check antes de la integración y equivalencia CPU de parámetros del material anterior. Sin edición activa ni GPU por este revisor.

Declined to judge: presupuesto final de 200 casas en navegador, tiempo GPU/drawcalls observados, píxeles del atlas, calidad estética y publicación. Quedan para raíz ensayo completo y fichas simétricas. No se sustituyen semillas problemáticas ni se presenta 60 como margen holgado: las tres casas quedan exactamente en el límite.
