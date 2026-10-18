# Previsualización R2 — sólo snapshot privado

Cambios autorizados: orden mesa→bajo→biblioteca y `de` inmediatos. Catálogo, modelos, dimensiones, superficies, motor, acabados, cámaras y umbrales iguales a R1. No usar esta propuesta como parche de producción de generadores.

Dos bases posibles:

- Snapshot T16 sin greybox: `greybox_r2_contra_t16.patch` (dos JSON: objetos + kit principal).
- Preview que ya tiene la R1 sellada: `orden_r2_contra_r1.patch` (sólo kit principal).

Aplicar uno de ellos únicamente en la copia privada y regenerar allí con `python3 tools/interiores/datos.py`. No ejecutar generadores catálogo/kit después: sobrescribirían estos JSON de sonda. No copiar compilados sobre la raíz. El JSON alternativo `vivienda_estudio_grey_amplio` es para la CPU privada y no se incluye en los parches.

La captura/API no se ejecuta desde esta entrega. Raíz comparará las canónicas y la entrada1594. Los recibos CPU no aprueban la apariencia ni cubren todavía el caso positivo del fallback individual completo.
