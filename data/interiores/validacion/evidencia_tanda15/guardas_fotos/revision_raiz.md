# Revisión independiente de guardas físicas de cámara

Sin P1/P2 estáticos identificados. Candidata SHA6881d0b2f2d528552a0480ccc43188c8a4071ea73364418df387f077ebb69cae; parche6777e0908038f728812337ba069fe371808962234ce63e8c7d2b80eb0cbe7a44. Se revisa el diff completo y se ejecuta de nuevo el instrumento CPU:15 casos físicos, cuatro mutantes y cuatro controles de render simulado PASS. Usa Collider y caja reales; no hay WebGL ni capturas nuevas.

La comprobación opera sobre copia, conserva la pose elegida y evalúa delta y profundidad, contención OBB de la misma planta y centros circulares degenerados. El criterio anterior sólo comprobaba desplazamiento neto y admitía cancelación. Se conserva literalmente selección visual, semillas, FOV y objetivos. Se registra el estado anterior y posterior al render y se rechaza cualquier cambio de pose. La clase PICKUP procede del catálogo correcto.

La exclusión de poses puede dejar la rejilla sin solución: debe mantenerse el FAIL. Es un protocolo nuevo; no vuelve válidas las cámaras históricas ni permite atribuir diferencias de nota sólo al producto. No prueba visibilidad, iluminación, arte, GPU o transacción de la ficha entera. Aplicación y captura runtime pendientes. La candidata no está en el producto activo ni entra en la publicación T14 congelada.
