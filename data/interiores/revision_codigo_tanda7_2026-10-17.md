# Revisión independiente de código — tanda 7

Fecha: 2026-10-17. Base HEAD: `6d34cc384fca3590a00e2cb3286c7e9da7382db8`.
Objeto: diff de trabajo y fuentes actuales; no un rango de commits. Revisor independiente de esta implementación. La propuesta de luz de tanda 8 queda fuera.

## Dictamen

**Aceptación estática del código de tanda 7: sin hallazgos P1/P2 nuevos que bloqueen su integración.** No equivale a aprobación visual, publicación ni cumplimiento de 4/5. Las correcciones de cámara que otro agente realiza después de esta lectura deberán revisarse por separado.

## Comprobaciones y evidencia

- `src/locales.js:165–191`: `buscar_refs` es optativo. Sin él se conserva la última referencia; con él se prueban referencias y lados, sin retirar las comprobaciones de contención, volumen libre ni accesibilidad. El salto de bucle termina ambas búsquedas al colocar una pieza. El fallback sigue condicionado por `si_no`; los acompañantes del trastero que lo desactivan no terminan dispersos por otra pared.
- `src/locales.js:296`: la regla `pared` emplea la misma función `cantidadPreferida` que otras reglas. La cantidad sigue dentro del rango declarado; permite intentar el armario alto opcional cuando se solicita `preferir`. Puede cambiar la secuencia de distribución de semillas respecto a la versión anterior; no introduce aleatoriedad externa.
- `data/kits/kit.schema.json`: extensión booleana compatible y opcional. Ejecutado el comprobador real de esquema sobre todos los JSON de kits: cero errores.
- Cocina: se priorizan el módulo alto y los frentes contiguos; no se retiran los muebles obligatorios. Baño: las dos entradas de inodoro tienen condiciones complementarias, `<10` y `>=10`; no están activas a la vez en el umbral. La regla `enfrente` mantiene su fallback a otra pared si la opuesta no admite el objeto. Trastero: las piezas mínimas admiten fallback y los acompañantes opcionales sólo se aceptan agrupados.
- Generador de catálogo ejecutado en memoria, sin escritura: sus 158 objetos coinciden exactamente con `data/objetos/vivienda_a.json`, con 158 identificadores únicos. Generador de kits ejecutado con escritura sustituida por captura en memoria: entradas de cocina, baño y trastero coinciden con los JSON actuales, incluida normalización de lámparas.
- Los siete objetos modificados se comprobaron con las funciones reales `alto` y `triangulos`: ninguno baja del suelo, todas las superficies declaradas tienen pieza de apoyo, y costes entre 288 y 1296 triángulos por objeto, por debajo de 5000. El mínimo vertical del armario alto es 1,3275 m, coherente con soporte de pared. La encimera conserva el plano útil en 0,89 m; vasos del armario apoyan sobre la balda en 1,3525 m.
- `src/acabados_vivienda.js`: cambios de colores del suelo; no modifica huecos, posiciones, colisiones ni materiales de interacción.
- `tools/interiores/casas_pruebas.js`: los dos contratos nuevos incluyen el caso de referencia bloqueada y una comprobación negativa con `buscar_refs=false`, además del intento de armario preferido en seis semillas. No se ha debilitado un criterio existente.
- `tools/interiores/fotos_casa.py`: el contexto privado y calidad alta manual/DPR1 evitan heredar la partida o adaptación de una sesión real. El registro incorpora calidad y DPR.

## Evidencia existente releída

`.cache/calidad/tanda7/contratos.json`: 32 contratos y cero errores. `.cache/calidad/tanda7/pasos.json` registra salida 0 de datos, contratos, 200 casas, laboratorio de semillas y capturas. Estas ejecuciones pertenecen a la cola del agente raíz; el revisor no abrió navegador ni las repitió. Las verificaciones propias fueron offline y en memoria.

## Pendientes y Declined to judge

- Cobertura visual de las cámaras de cocina y baño: raíz ha detectado muebles fuera de encuadre y WC cortado; otro agente está corrigiendo exclusivamente ese capturador. La versión de fotos identificada abajo no queda certificada como cobertura suficiente.
- No se puntúa 4/5, estética, contraste ni iluminación por este informe. Las imágenes anteriores no sustituyen las capturas finales y sus evaluaciones.
- No se evalúa ni aplica `tanda8_luz.patch`, ni se atribuyen mejoras de render a ese parche.
- No se certifican FPS, GPU, render final, despliegue ni compatibilidad del paquete a partir de pruebas estáticas. No se ejecutaron commit, push ni publicación.
- La revisión geométrica offline no demuestra ausencia universal de solapamientos visuales en todas las semillas. Los guardias y la evidencia de 200 casas/81 semillas acotan los casos probados.

## Identidad de los archivos leídos

- `src/locales.js`: `eebb063f0038059530840807e428e102b7c387ca2c72513612f115c9bd6b71f6`
- `src/acabados_vivienda.js`: `c439f596d8256cfae5e3a9fec0318ff4e28b456ca980ed84a51a161d9955ce6c`
- `data/kits/kit.schema.json`: `299e3c1cd00a7fcf5f3fd5c5e3b46f69137b287ca3b4a8a5519e7e5181640b1a`
- `tools/interiores/composicion_domestica.py`: `c7c168e029f9a278e4fea9b3792892de48c3b0385ac7b1f20ba8c75f35567f19`
- `tools/interiores/acabados_catalogo.py`: `e0963e92df7f659301ff4940176fee686e534952480d8eede6155c03069f302f`
- `tools/interiores/kits_vivienda_a.py`: `d398fee568d1b5f96cbbb1ef389dd8efcffb5da517521d82c6822914e76c25c5`
- `tools/interiores/casas_pruebas.js`: `29d54dfec522ac758ac1e6b6e8d5d6a1e49357b3ec5889929c22aa058ad6596e`
- `tools/interiores/fotos_casa.py`: `0a3119ae3181f1f43b61e31a5a8e0b18371496bad3db2a55f13814651eca6cb4`
- `data/kits/vivienda_cocina.json`: `241fbf6f65c265f76341a8e962cdffa1000fc697d9e0f7584710e3914491c973`
- `data/kits/vivienda_bano.json`: `e9ace969be39b2863bef2e8f45cb2de2a31c473fb6848cfb952cfd4167c3518c`
- `data/kits/vivienda_trastero.json`: `85a41b44b435386d992b582e8bfe9ae1b04de8420376be17544217e85a12aea9`
- `data/objetos/vivienda_a.json`: `d405cde128711ae427232e2e1c5e0a6d3f4d2129fb433ca7de3ba20c7d5fc7e2`
- `src/interiores_datos.js`: `4c54644e05ea023794992a618a8d1fe440b9f8d45fcf539c0a79a0129aec1ca9`
