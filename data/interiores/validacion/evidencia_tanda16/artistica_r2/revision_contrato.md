# Revisión independiente del contrato artístico T19

**Sin P1/P2 pendientes** en delta `75069a188a6360942c5034e70a4ce9c1d838d21c35697a77c56c6d043dcede2a`, aplicado conceptualmente tras contrato técnico `4fe8f2a3465906708b8dc05f936e7b45a8d2b1c3d3c08c85aea20e85e35a37f5`. El nuevo combinado es distinto: `b36de117d1ce0162cb7c800f06cb2cf6a26093603c20968d53677cd4b9f987e6`.

Reconstruí el delta desde fuente privada técnica y cotejé bytes exactos con candidata. Sólo cambia el tercer callback T19. Ahora audita todas las partes del pan, incluida hoja metálica y mango, y usa extensión horizontal de la pieza rotada. Los soportes de estos modelos son ejes alineados; la fórmula es válida para ellos, sin pretender un auditor genérico de soportes girados.

La versión fd5547 tenía negativo condicionado a encontrar hoja. Mi CPU demostró que quitarla daba PASS y se avisó. Autor preservó esa versión y sustituyó la condición por una exigencia explícita. Nuevo CPU ejecuta el callback exacto extraído de casas_pruebas: positivo PASS; mutante del antiguo filtro por material FAIL por cuchillo flotante; quitar hoja FAIL por ausencia. Los tres casos cotejan además que el callback restaura íntegro el catálogo tras sus mutaciones internas. No se omiten pruebas heredadas de pan flotante ni taza penetrante.

Recibo propio `revision_contrato_cpu.json`; recibo anterior `revision_contrato_cpu_fd5547.json` conservado. Runtime/partes/collider son los del entorno CPU privado leído; no GPU, navegador, API, activos, build ni CI. Esto revisa un callback y sus negativos, no afirma que se haya ejecutado el harness completo ni aprueba aspecto visual.
