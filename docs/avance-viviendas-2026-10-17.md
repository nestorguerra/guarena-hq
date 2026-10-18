# Guareña HQ: viviendas y acabados del 17-10-2026

Versión de prueba cuya publicación ha solicitado el usuario. La inspección visual y las puntuaciones se conservan con sus límites; publicar no equivale a superar el objetivo de calidad de la rúbrica.

## Cambios

- 15 kits nuevos más el salón existente: las 132 habitaciones habitables de las 22 casas de vecinos se amueblan por kit.
- Annie mantiene su plano singular, dormitorio personalizado, gato, tocador, caja fuerte, patio y dos plantas. Salón, cocina, ambos baños y estudio usan cinco kits.
- Color del catálogo corregido, dibujos distintos por semilla, lámparas según función, teclado del piano visible, cornamentas ramificadas y pliegues en la camilla.
- Cocinas grandes con mesa; cuarto joven amplio con TV apoyada y sofá de frente; despensas con reservas a escala de las baldas; juguetes reconocibles en niños. Se restringen los enseres del baño a higiene.
- Lotes de geometría estática mantienen puertas, pantallas, botín y lámparas controlables. No se elevan los límites de rendimiento.
- Capturas con cámara libre y vuelo inicial terminado. Taller y pintura tienen fichas separadas.

## Comprobación

Los contratos comprueban montaje, roles, acceso a interacciones, cobertura de kits, color, caché, composición y las funciones propias de Annie. El muestreo estricto cubre 200 casas sintéticas y las 22 reales. Cada kit de vivienda tiene un laboratorio de 81 semillas con contextos registrados; no son 81 hogares diferentes.

La integración usa una partida ficticia en contexto privado. Comprueba 321 euros, 700 euros en caja fuerte, una decoración guardada en planta alta, depósito/retirada, siesta, entrada/salida y recarga. Los testigos de Evolución y fija deben permanecer intactos. No se prueba una partida real del usuario ni toda combinación posible de decoración antigua.

Las métricas finales y los resultados están en `data/interiores/validacion/`. Los recorridos de colisión son muestreos acotados, no barridos exhaustivos. La revisión de código detectó y permitió corregir el inventario de Annie y la bandera de sus lámparas agrupadas.

## Revisión visual

Dos revisores independientes inspeccionan las fichas y registran problemas concretos. Decision API de OpenAI añade puntuaciones en cinco dimensiones con referencias del moodboard. Los resultados inferiores a 4 de media o a 3 en una dimensión permanecen como no aprobados. No se cambian los umbrales ni se sustituyen notas desfavorables por declaraciones de aprobación.

[Galería](../data/interiores/fichas/viviendas.html) · [Informe](../data/interiores/revision_viviendas_2026-10-17.md)

## Publicación y recuperación

Destino comprobado: GitHub Pages de `nestorguerra/guarena-hq`, rama `main`. Esta orden no modifica el servicio diferente de 388 Pueblos en Render. El paquete incorpora el commit en `guarena-revision`; Actions y la página pública permiten releer la versión servida. La base anterior permanece en Git: `339cbe13508e9996d855d9ac8f6276e6b98042e9`.
