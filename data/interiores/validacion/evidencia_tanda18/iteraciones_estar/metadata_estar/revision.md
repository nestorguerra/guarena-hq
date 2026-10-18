# Propagación de metadatos de estar

Parche privado mínimo de dos líneas sobre final_r8 sellado: buildLocal añade `composicionEstar` a h.local sólo si el programa se admitió, y validar la copia al reporte. No altera el programa, geometría, materiales, colocación, RNG, controles ni umbrales; no informa admisión cuando el programa cae a fallback.

CPU dirigido ejecutado en `probar.cpu.mjs` y registrado en `cpu.json`:

- Semilla 34 del laboratorio literal: perfil rico; lectura admitida, estar no admitido. validar real da cero errores. Antes/después son exactamente iguales, incluida ausencia de estar en reporte.
- Semilla de constructor 3244, semilla local 424969: buildLocal con el marco/hogar original de esa sala admite estar (gap .55). h.local contiene los índices reales; la nueva línea literal del reporte conserva esa metadata no vacía. Este caso no es el laboratorio de dimensiones predeterminadas.
- En ambos casos se comparan exactamente posiciones, geometría/index/atributos —incluidos colores—, matrices, materiales/defines, luces del grupo y acciones. Los hashes visuales CPU coinciden; las piezas y el layout permanecen exactos. Se verifican los 494 hashes de R8 antes y después.

Esto acredita ausencia de cambio geométrico/material en los casos dirigidos y el alcance declarativo del diff. No certifica píxeles de Canvas/texturas ni raster GPU; no afirma 81 admisiones ni sustituye su barrido. La ficha R8 conserva su procedencia original: este delta posterior de reporte debe anotarse como tal, sin reetiquetar su captura como regenerada. Activos y R8 sellado intactos.
