# R7 — protección de selección de asientos

Dos P2 del prototipo revisado, corregidos únicamente en el parche privado asientos.patch:

1. componerEstar inventariaba sólo roles sofa/sillon/silla y omitía el puff sin rol que houses registra cuando composiciónLectura lo admite. El segundo postpaso podía retirar ese acceso sin comprobarlo. Se pasa el índice exacto desde el caller; no se convierte cualquier puff del catálogo en asiento.
2. El filtro baseline<1.2 excluía asientos todavía seleccionables por Seats.near, cuyo corte real es estricto<1.25. Ahora se preserva la selección para baseline<1.25 y se exige candidato<1.25. No se afirma salida frontal segura a partir de una distancia radial.

El callback de locales conserva el try/finally con restauración íntegra de P y guardias, sin RNG. El helper mueve sólo mesa/alfombra y dependientes existentes; conserva IDs e índices, altura, referencias y K. Colisiones y reservas se comprueban por partes reales; contactos del mismo propietario quedan excluidos porque la transformación rígida conserva el estado previo. Rechazo o excepción no comprometen el candidato.

## Evidencia dirigida

La revisión inicial sobre modelos activosR6 reprodujo admisión3244 no vacía, rechazo total, excepción sin mutar P, inicio fuera y reserva total rechazados; amueblar conserva activas/guardias y12 U siguientes. Un primer ensayo de instrumento comparaba identidades K de distintos runtimes y falló; conservado en dirigida_error_fixture_v1.mjs y explicado en errata_fixture.txt, sin atribuirlo al producto.

politica.cpu.mjs prueba el helper literal con geometría/catálogo3244 y un doble explícito de mapa alcanzable para aislar la política: puff protegido→rechazo; restaurar omisión→aceptación indebida; asiento con distancia previa entre1.2/1.25→rechazo al perder alcance; restaurar filtro1.2→aceptación indebida; candidato aún dentro1.25→aceptación. Estos negativos no demuestran una ruta física rota en una vivienda real; demuestran ambos huecos de la condición con entradas de alcance controladas.

constructor.cpu.mjs ejecuta construcciones reales y amueblar con el parche:3244 admite,2786 conserva fallback íntegro. Interacciones/IDs/defs iguales, piezas fuera de movidos exactas, revisarUso0 y activas/guardias/12 U iguales. Canvas de trazas y assets placeholder; sin GPU. ModelosR8 no incluidos.

## Adaptación de pruebas mantenidas pendiente

T21 antiguo apaga composicion_lectura y con ello ambos programas: su comparación contra legacy debe usar unión explícita de movidosLectura y movidosEstar, sin permitir cambios fuera de ella. Mantener identidades, acciones y recompensas. El nuevo contrato separado de estar debe comparar lectura activa en ambos lados, con sólo estar apagado, y exigir admisión no vacía, núcleo fijo, dependientes rígidos y RNG; no cambiar K ni semillas para lograrlo. El caso2786 es fallback legítimo. No he cambiado esos contratos activos.

## Límites

No se aprueban modelos ni geometría nueva R8, costes globales, imágenes/nota, navegación universal ni publicación. Las salidas nominales inspeccionadas no constituyen fallo por sí solas: Player.standUp dispone de standPos y la ruta forward depende de su raycast exterior. El helper protege selección radial, no una salida certificada. Tampoco se transforma este cambio en una auditoría de dependencias malformadas heredadas. Gate integrado y evidencia visual nuevos siguen pendientes.
