# Revisión visual independiente — luz doméstica, tanda 8

17 de octubre de 2026. Inspección posterior de las 16 PNG originales de la comparación entre la base congelada de tanda 7 y el primer candidato de tanda 8. El revisor preparó el instrumento, pero no implementó el render ni el cambio de iluminación. No se asignan notas manuales ni se atribuye el objetivo formal de calidad.

**Estado vigente:** aceptada la corrección final del apagón dentro de la muestra inspeccionada. El cierre al final sustituye la reserva de oscurecimiento del candidato inicial. Permanecen el plafón lavado y la cobertura parcial de cocina nocturna.

## Resultado del candidato inicial

**Aceptación visual parcial:** la atenuación ambiental aporta una mejora moderada de contraste de día, conserva la lectura con luces encendidas y no muestra una fuga de luz al exterior tras entrar y salir. **El apagón inicial queda demasiado oscuro y requiere corrección antes de extenderle el perfil.** El plafón conserva un techo muy lavado; el cambio no resuelve ese defecto anterior.

Las 16 PNG originales se conservan. La exclusión de h.powered === false comunicada por el constructor se comprobará en una captura dirigida separada; no se da por resuelta por el cambio de código ni por sus contratos.

## Evidencia e integridad

Directorio exacto de todas las imágenes examinadas:

`/Users/nestorguerra/Proyectos Vibe/Guarena HQ/.cache/calidad/tanda8/capturas/`

El recibo report.json tiene SHA-256 `56f943eb1ae0b6105c101b10ab2ad72bcd3b900242b6307448997ff55bcb6490`. Registra captura de 18:13:27–18:14:26 UTC, ocho pares y errores vacíos. Se comprobaron de nuevo los hashes de las 16 PNG contra el recibo y sus dimensiones reales, 1920 × 1080. El manifiesto identifica únicamente src/game.js y src/luz_vivienda.js como diferencias de fuentes entre base y candidato inicial.

| Par; archivos before_ y after_ con este sufijo | SHA-256 before | SHA-256 after inicial |
|---|---|---|
| exterior_before_enter_day.png | 8d61e1459d01261868b21d857ef2e8fe32bc1a3b5357c7cf865a75871852bef0 | 1b065255502969fc3de4f4784a6e4e8d9b186a563367ac752c3ca9503d120c6b |
| trastero_day.png | eb1f1fe2f7a67775e51366d44a431b29e07293757d6e857f8f708ea23878aa57 | 64d6efff3ab64e00dcc13001a670161a60b882d039cbc682e7d3d8ad804e9848 |
| trastero_night.png | c88846d97774d4f542c52fb72a2db146bd4f4b2978dade941ea29db75ebdd4c7 | 9a89cefa0843eee5656f2aadfe86f7435754d593c7b8cf535953d2b58c6e0f78 |
| trastero_lamp_night.png | 723c0ba20b747fc23f8e354e81b5f6ae72b18c71e7e66d02de7dc20171f7f290 | 6cc55f37382ffb02836116e9561c8ce0ec88c6d6b72e0cabc04b4b70bc122bb3 |
| trastero_blackout_night.png | c9d99b3998b612f20bc58984664f587c27fdff348f609ea5e6972379c9fb23d4 | 5e36c31106abe258534af2320008becea24dc0601e7ab1f26bf44b4c5e2d5807 |
| exterior_after_exit_day.png | 630d90bbcf7eb0f4a92fa5605826a9a242a53320f94394054c5b1d827f9c2123 | 1c255d2c7a82ac669c54734e5fc4a74a46eaf3d049d5834d4d691295dc766396 |
| cocina_day.png | b23cae65cb07773b9d3de265d14f3d2122c9f4e5ad2486889179365b3bc18e4e | 4d4de40b3b1169f8a8ead7f588a3e8adb89936b899d7b845a66b6d9cc6f06139 |
| cocina_night.png | ed397959344d3633964ef767d3b22d1ae6a9144c3e452a324d8bafa867b07f14 | 2f4f1124f1b0c5ab031bb00cbca40d0e57ac5e167ecf1332b4db975de7cf4bcc |

## Comparabilidad y restauración

Las muestras usan trastero 3886 y cocina 2786 con las cámaras de uso congeladas de la base, calidad alta, DPR 1,5, MSAA de escena 4 y exposición 0,9. Dentro de cada par coinciden cámara completa, hora, clima, material de ventana, estado doméstico y configuración restante registrada. La noche está a las 23:00 y night = 1. Cada captura acredita una actualización de PMREM forzada con contador 1 y envTimer = 3; la reutilización del render target no se interpreta como falta de refresco.

HouseLife permanece adjunta y sincronizada con dt = 0. Las entradas diurna y nocturna se reconstruyen a su hora correspondiente. El recibo mantiene estado y posición de residentes comparables entre lados, sin eliminarlos para la fotografía.

En el candidato inicial, el render doméstico diurno usa IBL 0,33 y rebote 0,2375 frente a 0,6 y 0,95; el nocturno usa IBL 0,2475 frente a 0,45 y rebote 0 en ambos. Los valores originales se restituyen exactamente tras cada render, según los registros antes/durante/después. Las llamadas de exterior de WindowView del trastero conservan los valores ambientales originales. En cocina no se registra un pase exterior visible en estos encuadres.

La puerta de calle es la existente de semilla 2786. El interior de revisión 3886 se asocia explícitamente a esa puerta mediante la fixture; no se presenta como una puerta real de semilla 3886. Las imágenes exteriores utilizan la misma cámara antes de entrar y después de ejecutar la salida del juego. Se conservan IBL 0,6 y rebote 0,95; el aspecto de fachada, acera y coche próximo no muestra oscurecimiento nuevo o dominante tras volver a la calle. Esto comprueba el estado final de esa entrada/salida, no una transición temporal continua.

## Observaciones visuales

| Par | Observación |
|---|---|
| Exterior antes de entrar | Aspecto y lectura prácticamente iguales entre base y candidato. Sin alteración importante de iluminación. |
| Trastero de día | El cuadro de la bicicleta y las caras de las cajas ganan algo de separación. Se conserva el color y los radios. La pared alta sigue bastante uniforme: la mejora es moderada. |
| Trastero de noche encendida | Ligero oscurecimiento controlado de medios tonos. Bicicleta, cajas, borde del suelo y puerta siguen legibles; no aparece una región nueva que se funda en negro. |
| Plafón de noche | El techo continúa casi blanco en una extensión muy grande y el contorno del emisor es débil. La atenuación de IBL cambia poco ese lavado. No es una regresión nueva importante, pero tampoco una solución del defecto anterior. |
| Apagón de noche | El candidato inicial pierde señal en cuadro, radios, pedales y cajas. El suelo ya era casi negro en la base; la reducción adicional resta margen de lectura. Se considera una regresión de visibilidad que debe corregirse en ese estado. |
| Exterior después de salir | Sin fuga observable del perfil doméstico al volver a la calle. Los valores ambientales se restauran y la imagen mantiene su luz. |
| Cocina de día | Mejora ligera del volumen de armarios y diferencias entre encimera, frentes y pared. Conserva lectura de olla, fregadero y tiradores sin nuevas manchas negras dominantes. |
| Cocina de noche | Un residente ocupa gran parte del primer plano en ambos lados y tapa fogones, olla y parte de la encimera. La zona visible conserva detalle, pero no permite certificar el conjunto nocturno de la cocina. Es una limitación de evidencia simétrica, no una regresión del render demostrada. |

## Ajustes y límites

La corrección mínima para el apagón es conservar su ambiente anterior cuando la vivienda no tiene corriente, manteniendo el cambio diurno y nocturno con luces encendidas. La nueva condición necesita su captura final dirigida antes de retirar esa reserva.

No recomiendo seguir reduciendo globalmente IBL para perseguir el techo lavado: el beneficio observado allí es escaso y el apagón pierde visibilidad. Si se aborda ese acabado después, conviene separar emisor/bloom nocturno en otra comparación pequeña, sin oscurecer el conjunto a ciegas.

Para completar la lectura de cocina nocturna bastaría una pareja adicional con un pequeño desplazamiento de cámara que conserve el residente y deje visible la encimera. Esta ficha no prueba ausencia de defectos detrás de él.

Revisión estática de dos interiores, una fachada, una estética y una calidad. No certifica movimiento, transición perceptiva al cruzar puertas, todas las habitaciones/semillas, segunda estética, rendimiento o HUD HTML. La inspección de estas 16 imágenes se hizo solo mediante archivos locales, sin generar nuevas capturas ni abrir el juego. La comprobación posterior del guard de apagón se documentará de forma separada y no reemplazará los originales.

## Cierre de apagón corregido — paquete final

Se ha inspeccionado el PNG final `/Users/nestorguerra/Proyectos Vibe/Guarena HQ/.cache/calidad/tanda8/apagon-final/after_final_trastero_blackout_night.png`, SHA-256 `1b013cd7d16cc974a0b5a285c948d29d46d3b59b7a4b44bc6a4f631314214ad3`. **Aceptada la corrección del oscurecimiento adicional:** bicicleta, radios y cajas recuperan la visibilidad de la base; el suelo continúa oscuro como antes. No observo una regresión nueva en este estado final.

La comprobación dirigida se ejecutó una sola vez, con autorización y GPU exclusiva, contra dist/test.html, SHA-256 `9dde78039bac2bfef9556f6a3ee704984f7c32b44bab4c06679f2cea38ce2c6a`. Su report.json tiene SHA-256 `df9062e4d347d5457fb0f7c6d59633927f89314ce404ff626358a7e0f2855d80`: misma cámara, estado doméstico/HouseLife y hora 23 frente al antes conservado, PMREM con una actualización, ambiente 0,45 y rebote 0 antes/durante/después del render, invariantes idénticos y errores vacíos. El contexto privado quedó eliminado y la GPU liberada. Los originales no se reemplazaron.

Este cierre retira únicamente la reserva del apagón. Conserva las observaciones de los ocho pares iniciales, sin volver a capturar el resto del paquete. El plafón sigue lavado y el residente limita la lectura de cocina nocturna. No se amplía a estabilidad temporal, otros interiores o calidad formal.
