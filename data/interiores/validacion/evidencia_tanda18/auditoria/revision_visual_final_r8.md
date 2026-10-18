# T18 · cierre visual final R8

**Aceptación visual acotada de R8 como mejora PARCIAL.** La composición mesa–sofá–alfombra y los modelos tapizados mejoran el estar respecto aR6; el resultado se conserva al volver a las seis poses exactas. No observo un defecto visible nuevo ni una falta de cobertura que impida este cierre. Integración/publicación siguen condicionadas a gates y revisión técnica de la escena final; no se atribuye4/5 ni se repite la evaluación formal.

## Evidencia final revisada

Se abrió `final_r8/capturas/casa_salon.jpg`, el original1594/uso, ambas vistas de familia4007 y la pareja completa `complementos_r8_comunes/antes.jpg`/`despues.jpg`, cotejando sus JSON. El JSON canónico R8 coincide **byte a byte conR6**: mismos seis puntos, objetivos, alturas yFOV. Sus guardas candidato/antes/después son libres, dentro del recinto, con profundidad/desplazamiento nulos y sin centro dentro de mobiliario. Familia4007 conserva sus guardas.

En3244 y1594, mesa y alfombra se leen asociadas al sofá y más próximas a su uso. Cojines, brazos blandos, base y apoyos dan una silueta doméstica reconocible; terracota/petróleo y textil natural evitan que los antiguos bloques amarillo/negro y la alfombra morada dominen. En1594 esta conclusión ya se apoya en cámaras estables, sin aprovechar los encuadres distintos deR7.2786 conserva camilla+sillas y su carácter compacto; continúa el recorte declarado de uso, compensado por conjunto.

Familia4007 muestra el nuevo asiento verde, mesa y alfombra como un conjunto claro; el mueble blanco y la pared quedan próximos en tono, pero sus contornos y apoyos siguen legibles. La puerta y borde de cámara limitan partes de biblioteca, sin nuevo defecto observado. No se ven bandas, triángulos, superficies negras o apoyos claramente separados nuevos.

## Complemento de lectura: procedencia distinta y honesta

La antigua pose complementaria deR6 fue vetada por la mesa acercada, con delta≈0,187m/profundidad≈0,154m. Su FAIL permanece en `captura_complementos_r8.log`; no se movió mobiliario para liberarla.

El nuevo par se encuentra en **`complementos_r8_comunes/`**, no en la carpeta fallida. Procede de selección entre posiciones libres del constructor realR6 y comprobación posterior enR8. Se cotejó la identidad exacta de ambos miembros: posición `[-5197.280761262942,1.6,-5196.324125616932]`, objetivo `[-5197.7413674141835,0.9499999850988388,-5198.985000007749]`, FOV68, clipped0, guardas libres antes/después y errors[]. Es otra pose respecto al complemento histórico, pero una comparación común válida entreR6/R8.

Desde ella se ven completos biblioteca, puff, mesita y lámpara, con el sofá al lado: el rincón mantiene relación y escala, y el puff blando/neutro se integra mejor. **No hacen falta más capturas para este dictamen acotado.**

## Límites y huellas

Sólo aspecto diurno estático y metadatos. Los PASS CPU22/5admisiones, propiedades funcionales, protección de asiento/puff y tolerancias de AABB fueron comunicados por raíz; no se convierten en comprobaciones propias por mirar las fotos. Las reservas artísticas ya documentadas quedan como mejoras posteriores; no se rehace aquí el diagnóstico ni se anticipa publicación. SinGPU, API, navegador, nuevas pruebas CPU o edición de fuentes/activos. Se conservan los informes anteriores.

Archivos bajo `.cache/calidad/tanda18/`:

- `final_r8/capturas/casa_salon.jpg`: `c1db0f3df8ed77d1d4b175d00f3a7fd73231822401811311c68db10c2d5c799b`.
- JSON canónico comúnR6/R8: `fb038c8a8371c566d1924d448ad0bbd27aa4ac3f7bf9868220e0cf6a514063d9`.
- `familia_r8/familia_0.jpg`: `18dd21c7114e2835c958487135eeef4be83c87cb8e2b33748e089e828458757d`.
- `familia_r8/familia_1.jpg`: `0ef464b63188395cbc7806792b1dc583f8c645192152f48530d6710e946cf1bf`.
- `complementos_r8_comunes/antes.jpg`: `d152d1ba4ef354f6354eaceb1adac3861e97ef84fde18550b1f5798d3d55770c`.
- `complementos_r8_comunes/despues.jpg`: `a37c34fad668293651db68cae288d80892ed052119ec5b573d74e9b7c8db74d0`.
- JSON de ambos complementos idéntico: `54d0e35c56ff915d63daca970bf889fea7c964ed8ede9f4c2011e8cf8e9c8ea0`.
