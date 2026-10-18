# Greybox T17 — copia privada exclusivamente

La base es T16 actual sellada en `base.json`, con Annie7364d55. Fuentes críticas sin cambios, receta/objetos nuevos sólo en `candidata/data/`. Los modelos son envolventes grises y un respaldo físico de consulta; los contenidos finales no están modelados.

Para una previsualización autorizada por raíz, aplicar `greybox.patch` **sólo en el snapshot privado** y ejecutar allí `python3 tools/interiores/datos.py`. No ejecutar los generadores catálogo/kit A/B después del parche: esta primera propuesta modifica sus JSON derivados, no sus generadores. No copiar `candidata/src/interiores_datos.js` sobre la raíz ni sobre otra versión. El kit alternativo `vivienda_estudio_grey_amplio` es sólo un duplicado para las sondas CPU y no se incluye en el parche.

No contiene el acabado R2 de raíz. La eventual combinación se montará y medirá por separado. Cámaras y capturador originales permanecen intactos. Esta entrega no autoriza ejecutar GPU ni integrar producto; falta revisión independiente de la propuesta y cierre de fallback geométrico para producción.

Reproducir CPU desde la raíz del repositorio con el Node r170 declarado en los imports: `fit.cpu.mjs`, `full.cpu.mjs`, `annie.cpu.mjs`, `negativos.cpu.mjs` y `fallback.cpu.mjs`; todos leen la base congelada y la receta final. `hist_sonda*/` y recibos RED se conservan como evidencia previa, no son el estado final. Los instrumentos RED históricos no deben ejecutarse contra datos finales esperando reproducir otro snapshot.
