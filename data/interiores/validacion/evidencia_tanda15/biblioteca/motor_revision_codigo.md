# Revisión independiente — motor de grupo con silla frontal

**Sin hallazgos P1/P2. Aceptación estática acotada al motor**, no de la receta infantil ni de su resultado visual. Parche motor.patch SHA256 `6d6a15276668beaa0e01d2dd22fc6bd5ce31bd5eab22e104b9acf4039a0fda8e`; src/locales.js candidato SHA256 `c24286ee0e4ed23bf79f76b7e5f887001a7a254206aaaaf2f2488f664852cae0`. Base declarada62e1c73; src/locales.js activo sigue idéntico a esa base. No se ha aplicado ni modificado producto, ni usado GPU, build o CI.

## Lectura del cambio

- src/locales.js:530 conserva las restricciones del grupo y sólo admite silla_frontal en la raíz si su objeto tiene soporte suelo. Una silla en un acompañante rechaza la vía de grupo y usa las reglas individuales previas. Las referencias de cada miembro aún deben contener el objeto inmediatamente anterior. Filtros de hogar/área y continuidad de entradas se evalúan antes del grupo.
- :559–572 calcula la misma pose frontal que contra_pared: origen geométrico real, holgura .06 y giro pi respecto de la mesa. Comprueba zona, reservas y objetos existentes con libre, y colisión por piezas con TODOS los miembros nuevos antes de poner ninguno. La silla tiene e de raíz antes de pasar por cierra.
- :581–584 incluye el asiento también frente a reserva_lateral y en cierra(prueba). No se evita el guard de paso/zonas/usos frontales. No se altera el mínimo de paso del kit ni la tolerancia de interpenetración de .005.
- :586–596 compromete la raíz y su asiento consecutivos. El asiento.de apunta al índice real de raíz. El siguiente miembro también referencia la raíz, no la silla; los posteriores apuntan a su miembro previo. previo se actualiza con puesto, no con asiento. Se restauran entrada y cursor de pared sólo tras aceptar todo el frente.
- Un intento fallido no modifica P, cursores ni el RNG principal. Puede aumentar guardias, como los intentos de grupo anteriores; ese contador no es igualdad de decoración. Después del fallo se ejecuta la misma receta por reglas individuales, con su opcionalidad. **No hay garantía universal de frente completo ni vuelta a la receta T12**.

Sin nueva gramática obligatoria: silla_frontal ya es string aceptado en kit.schema.json:240 y sus referencias se validan en datos.py:93. El significado sigue siendo asiento asociado al mueble contra pared. El motor verifica soporte suelo para el grupo. El validador de asientos existente cuenta padres sin de y exige un auxiliar con de al padre; la inserción propuesta mantiene esa representación y el resto de entradas conserva su e. No hace falta elevar mínimos ni excluir auxiliares nuevos.

## Evidencia CPU

Reejecutado el instrumento del autor con salida separada: grupo.revision.cpu.mjs / grupo_revision_cpu.json. Dos geometrías prueban orden físico inicial/inverso; 162 fallbacks fallidos comparan P/activas/debe/avisos exactos, incluyendo entradas posteriores de decoración y luz; **120 casos no optantes** comparan la salida serializable íntegra (81 infantiles +39 otros kits). Caso dirigido1555 del autor también pasa. No son40 otros kits en ese recibo. No se han reejecutado sus ensayos completos de casa/200casas ni sus capturas.

Instrumento propio motor_revision_dirigida.cpu.mjs / motor_revision_dirigida_cpu.json: **11 casos PASS** usando amueblar, caja, geometría de partes y mapa de paso reales. Cadena de tres miembros más asiento en N/S/E/W: orden lógico, e/de exactos, silla frontal orientada a mesa, ausencia de penetración por piezas y repetición determinista. Otros siete casos comprueban equivalencia con fallback previo al filtrar la raíz o un miembro por área, pedir silla en no raíz, bifurcar de, intercalar una entrada activa, hacer la zona demasiado corta para la silla o reservar todo su frente en la pared permitida.

Las cuatro paredes se ensayan con libres=[] explícito y comienzo central; el negativo de reserva se limita a N y usa su reserva real. Así no se confunde un fallback válido a otra pared con un fallo del motor. Estos son fixtures sintéticos de motor con modelos reales, no las seis casas completas ni un ensayo de cámara/salida real.

Sintaxis de locales.js y git apply --check PASS. SHA de motor y candidata conservados al terminar. El parche no cambia consumidores que no combinan grupo_pared y silla_frontal; la reejecución demuestra los consumidores muestreados, no todos los contextos posibles.

## Alcance pendiente / Declined to judge

La aprobación de receta B, sus mínimos en toda la muestra de casas, costes totales, texturas/modelos, apoyo de pertenencias, efectos decorativos/luminarias del RNG tras un grupo exitoso y calidad visual no están incluidos. Éxito de grupo puede variar el consumo incidental de la receta frente a las reglas individuales; la igualdad prometida aquí corresponde al fallo y a consumidores no optantes. No se certifican hideIn/unhide ni sus puntos de salida exactos con este recibo de motor: requieren los contratos reales de la entrega de receta, conservando collider, contención y profundidad. Tampoco se certifica runtime navegador/paquete ni publicación.
