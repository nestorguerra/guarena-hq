# Protocolo de capturas del comedor

Estado: instrumento corregido y comprobado en las tres casas. La ficha final del servicio r2 está capturada; sus guardas y diferencias se documentan al final.

La revisión detectó una puerta en primer plano y sillas recortadas. Se conserva la primera ficha candidata, sin puntuación, en `pre_servicio`. El primer muestreo de puertas no comprobaba la pose final. Se corrigieron los dos P2 con una guarda después de actualizar fotogramas y matrices, justo antes de renderizar. El intento `cobertura2` falló por una esquina recortada en 2606; no se cuenta como validación.

El intento `cobertura3` usa FOV 75°, el campo inicial del juego, ojo a 1,60 m y objetivos a 0,75/1,05 m. Las tres vistas de uso incluyen mesa y sillas completas: se comprobaron 24 o 40 esquinas, con cero recortes. El muestreo cercano de hojas dio 0/35 en las seis vistas. Es un muestreo, no una medida de todos los píxeles. La segunda vista declara cero esquinas evaluadas y recortes `null`; no certifica todos los objetos de la habitación.

Las cámaras difieren de la base anterior de 68°. No se atribuye a producto una diferencia causada por este protocolo. Las capturas corregidas anteriores al servicio se conservan en `pre_servicio_cobertura3`. Semillas, calidad alta fija, DPR 1 y estilo Plastilina se mantienen. La ficha del servicio terminado se registra a continuación como evidencia nueva.


Captura final del servicio r2: JPG 48b820c112a5fa4ac73adca16125f1343e3a80ae07f9a1461a056249f3b0bfc1. En uso apunta al centro Y de la envolvente real de mesa y sillas (≈0,49 m), no a un punto fijo anterior. Cero esquinas recortadas en las tres vistas de uso (40 / 24 / 40 evaluadas). Conjunto no evalúa esquinas (null). Muestreo de hojas: 2786/conjunto, 3/35 = 8,571%; otras cinco vistas, 0/35; límite 12%. No es certificación píxel a píxel ni cámara equivalente a la base FOV 68.
