# Auditoría de las calles: capturas de Google Maps frente al juego

Fecha: 13 de octubre de 2026. 292 vistas de 85 carpetas de capturas (~/Desktop/Guareña). Para cada vista, el juego fotografiado desde la misma cámara (posición, rumbo y campo de visión de la captura, con las cámaras recolocadas donde el GPS de Google se desviaba: .cache/calles/camaras.json), en su estado actual sin publicar, con el aspecto Plastilina a las 12:30 y el cielo despejado.

Método: ocho revisores, cada uno con un grupo de calles, compararon cada captura con su imagen del juego y anotaron solo lo que se ve distinto en las dos, con el sitio de la imagen donde se ve (columnas en píxeles de 0 a 1440). Sin causas ni arreglos. Las hojas de comparación (captura arriba, juego abajo) están fuera del repositorio, en el scratchpad de la sesión (auditoria/a_NNN.jpg), porque las capturas son de Google.

## Resumen

- Discrepancias: **2818** — alta 341, media 1599, baja 878.
- Vistas con alguna discrepancia: 292 de 292.
- Vistas con la cámara del juego mal situada (45): #22, #64, #94, #99, #100, #104, #105, #107, #108, #111, #119, #133, #136, #137, #141, #143, #146, #147, #148, #149, #153, #155, #156, #222, #226, #236, #237, #238, #242, #244, #245, #246, #248, #249, #259, #264, #267, #268, #273, #276, #283, #285, #286, #287, #289.

| Categoría | Alta | Media | Baja | Total |
|---|---:|---:|---:|---:|
| Cámara | 45 | 0 | 0 | 45 |
| Geometría | 123 | 91 | 2 | 216 |
| Color de fachada | 91 | 133 | 8 | 232 |
| Huecos | 2 | 502 | 46 | 550 |
| Detalles de fachada | 0 | 139 | 109 | 248 |
| Zócalo | 0 | 88 | 29 | 117 |
| Cubierta | 0 | 163 | 32 | 195 |
| Calzada | 2 | 55 | 70 | 127 |
| Marcas viales | 0 | 75 | 36 | 111 |
| Acera y bordillo | 7 | 77 | 63 | 147 |
| Vegetación | 29 | 116 | 100 | 245 |
| Mobiliario | 1 | 91 | 239 | 331 |
| Muros y vallas | 26 | 45 | 14 | 85 |
| Vehículos | 0 | 4 | 17 | 21 |
| Otros | 15 | 20 | 113 | 148 |

### Por calle

| Calle | Vistas | Alta | Media | Baja | Total |
|---|---:|---:|---:|---:|---:|
| Plaza de España | 5 | 3 | 36 | 19 | 58 |
| Plaza de Santa María | 3 | 2 | 25 | 8 | 35 |
| Plaza de los Castillejos | 4 | 1 | 27 | 9 | 37 |
| Plaza Vieja | 4 | 0 | 26 | 14 | 40 |
| Calle Atrás | 3 | 2 | 21 | 9 | 32 |
| Calle Bronca | 3 | 1 | 21 | 4 | 26 |
| Calle Castillejos | 4 | 2 | 13 | 11 | 26 |
| Calle Cañadilla | 3 | 0 | 21 | 15 | 36 |
| Calle Cuatro Esquinas | 3 | 2 | 13 | 9 | 24 |
| Calle de Don Juan Durán | 2 | 0 | 13 | 0 | 13 |
| Calle de la Cuesta | 4 | 2 | 33 | 9 | 44 |
| Calle de Santa María | 2 | 3 | 23 | 11 | 37 |
| Calle Derecha | 3 | 3 | 25 | 14 | 42 |
| Calle Doctor Lozano | 2 | 2 | 9 | 11 | 22 |
| Calle Don Manuel Dorado | 5 | 5 | 35 | 26 | 66 |
| Calle Estacada | 6 | 5 | 29 | 25 | 59 |
| Calle Eugenio Frutos | 5 | 3 | 22 | 19 | 44 |
| Calle Fuentes | 4 | 2 | 15 | 11 | 28 |
| Calle Grande | 3 | 3 | 17 | 11 | 31 |
| Calle Herreros | 5 | 3 | 30 | 29 | 62 |
| Calle Hornillos | 4 | 2 | 26 | 21 | 49 |
| Calle Malfeitos | 4 | 4 | 27 | 13 | 44 |
| Calle Pajares | 4 | 1 | 31 | 14 | 46 |
| Calle Pozo Dulce | 4 | 3 | 22 | 9 | 34 |
| Calle Pozo Pajares | 3 | 4 | 15 | 8 | 27 |
| Calle Túnel | 3 | 2 | 8 | 7 | 17 |
| Avenida de San Ginés | 4 | 8 | 20 | 15 | 43 |
| Calle San Ginés | 4 | 4 | 5 | 1 | 10 |
| Calle Extremadura | 3 | 2 | 18 | 5 | 25 |
| Calle Carolina Coronado | 3 | 5 | 11 | 9 | 25 |
| Calle Rosalía de Castro | 3 | 3 | 8 | 2 | 13 |
| Calle María Zambrano | 3 | 2 | 8 | 4 | 14 |
| Calle Dulce Chacón | 3 | 5 | 20 | 10 | 35 |
| Carretera de Don Benito | 3 | 8 | 25 | 7 | 40 |
| Calle Antonia López González | 3 | 6 | 32 | 12 | 50 |
| Calle Alcornoque | 3 | 11 | 20 | 13 | 44 |
| Calle Gabriel y Galán | 3 | 6 | 24 | 11 | 41 |
| Calle Julia Mayoral Márquez | 3 | 7 | 28 | 11 | 46 |
| Calle Teresa de Calcuta | 3 | 11 | 10 | 5 | 26 |
| Calle Medellín | 3 | 3 | 6 | 7 | 16 |
| Calle Nueva | 3 | 2 | 14 | 10 | 26 |
| Calle El Palomar | 3 | 5 | 15 | 7 | 27 |
| Travesía del Palomar | 3 | 4 | 6 | 3 | 13 |
| Travesía Nueva | 3 | 2 | 6 | 3 | 11 |
| Travesía El Royo | 3 | 6 | 13 | 6 | 25 |
| Calle El Rollo | 3 | 5 | 8 | 7 | 20 |
| Calle Nuestra Señora de Guadalupe | 3 | 6 | 19 | 17 | 42 |
| Calle Alberquilla | 5 | 1 | 33 | 17 | 51 |
| Calle Salsipuedes | 3 | 0 | 20 | 13 | 33 |
| Calle de San Gregorio | 3 | 0 | 19 | 19 | 38 |
| Calle Don Benito | 3 | 3 | 16 | 10 | 29 |
| Calle Luis Cernuda | 3 | 2 | 19 | 12 | 33 |
| Calle Rafael Alberti | 3 | 2 | 16 | 11 | 29 |
| Calle de Luis Chamizo | 3 | 0 | 18 | 16 | 34 |
| Calle Olivo | 3 | 0 | 13 | 17 | 30 |
| Calle Antonio Machado | 3 | 0 | 14 | 8 | 22 |
| Calle El Chiriveje | 3 | 2 | 19 | 11 | 32 |
| Calle Gerardo Diego | 4 | 8 | 35 | 21 | 64 |
| Calle José de Echagaray | 3 | 7 | 17 | 8 | 32 |
| Calle Juan Ramón Jiménez | 4 | 12 | 23 | 6 | 41 |
| Calle Miguel Hernández | 3 | 6 | 20 | 7 | 33 |
| Calle Palacios | 3 | 9 | 14 | 6 | 29 |
| Calle Severo Ochoa | 3 | 4 | 17 | 7 | 28 |
| Calle Vicente Aleixandre | 3 | 6 | 11 | 4 | 21 |
| Camino del Gamero | 3 | 6 | 13 | 3 | 22 |
| Carretera de Guareña a Manchita | 3 | 1 | 22 | 4 | 27 |
| Dámaso Fernández del Pozo | 3 | 1 | 12 | 3 | 16 |
| Plaza de Abastos | 5 | 4 | 28 | 14 | 46 |
| Plaza Federico García Lorca | 3 | 1 | 24 | 20 | 45 |
| Plaza Ramón y Cajal | 3 | 5 | 28 | 11 | 44 |
| Avenida de la Constitución | 6 | 8 | 21 | 14 | 43 |
| Calle de Don Diego López | 3 | 4 | 17 | 14 | 35 |
| Calle de Hernán Cortés | 4 | 4 | 5 | 2 | 11 |
| Calle del Arroyo | 4 | 5 | 7 | 7 | 19 |
| Calle el Pilar | 3 | 3 | 23 | 9 | 35 |
| Calle Encina | 3 | 2 | 17 | 13 | 32 |
| Calle Espronceda | 3 | 3 | 13 | 6 | 22 |
| Calle Lumbreras | 4 | 3 | 20 | 11 | 34 |
| Calle San Roque | 3 | 4 | 18 | 6 | 28 |
| Traseras de la Calle el Pilar | 3 | 8 | 13 | 6 | 27 |
| Travesía Luis Chamizo | 4 | 6 | 27 | 13 | 46 |
| Calle Almendralejo | 4 | 16 | 15 | 11 | 42 |
| Calle Puerta del Sol | 3 | 9 | 19 | 2 | 30 |
| Carretera de Don Benito a Portugal por Almendralejo | 6 | 7 | 14 | 6 | 27 |
| Carretera de Guareña a Oliva de Mérida | 4 | 8 | 20 | 9 | 37 |

## Cambiado en el juego después de las fotos de la auditoría

Las entradas siguen en el listado tal como se vieron; el cambio va anotado en cada una («Después»).

- n.º 1903 (vista #192, bloque de pisos cercano, lado izquierdo): corregido: el bloque tiene ya sus cuatro plantas.
- n.º 1904 (vista #192, segundo bloque de pisos del lado izquierdo (plano medio)): corregido: cuatro plantas.
- n.º 1908 (vista #192, planta baja del bloque cercano de la izquierda): cambiado: bajo el soportal ya no hay cocheras y su fondo queda en sombra; sigue cerrado al fondo (en la captura se ve el patio a través).
- n.º 2054 (vista #204, planta baja del bloque de la derecha): cambiado: el fondo del soportal (2,4 m) queda en sombra y sin cocheras.
- n.º 2063 (vista #205, bloques de pisos de la izquierda (nº de plantas)): corregido: cuatro plantas.
- n.º 2064 (vista #205, planta baja de los bloques de la izquierda): cambiado: el fondo del soportal queda en sombra y sin cocheras.

## Listado

### Plaza de España

**Vista #0** — 03_Fachada_del_Ayuntamiento_abril_2026.jpg (abril de 2026) · hoja a_000.jpg

1. [media] Huecos — huecos de la planta primera del Ayuntamiento
   - Captura: Los huecos de la planta primera (x≈355–385, 515–548, 603–645, 713–750) son rectángulos oscuros metidos en su marco de piedra, sin contraventanas a los lados.
   - Juego: Cada hueco de la planta primera lleva contraventanas de madera marrón abiertas a ambos lados (x≈380–425, 497–580, 640–665, 750–780, 935–960).
2. [media] Mobiliario — farola de fundición del primer plano derecho
   - Captura: Farola alta de fundición negra con farol en lo alto y un brazo con otro farol, sobre pedestal de piedra, en primer plano a la derecha delante de la fachada (x≈1000–1130, desde y≈140 hasta el suelo).
   - Juego: No hay farola en esa zona (x≈1000–1130): se ve el extremo derecho de la fachada, el cielo y el suelo despejado.
3. [media] Muros y vallas — barandilla de hierro del primer plano derecho
   - Captura: Barandilla baja de barrotes negros en el primer plano derecho, a ambos lados del pedestal de la farola (x≈985–1180, y≈600–680).
   - Juego: Suelo despejado de adoquín en abanico en la misma zona (x≈980–1180), sin barandilla.
4. [baja] Mobiliario — terraza de bar delante del Ayuntamiento
   - Captura: Terraza con sombrillas grandes grises y mesas y sillas blancas a la izquierda, delante de los arcos (x≈258–540, y≈400–693).
   - Juego: Explanada vacía en esa zona, sin terraza ni sombrillas.
5. [baja] Mobiliario — mástiles de bandera del Ayuntamiento
   - Captura: Cuatro banderas en mástiles inclinados sobre el balcón central (x≈475–760, y≈215–360).
   - Juego: Una sola bandera de España (x≈510–565, y≈5–35).
6. [baja] Otros — reposteros colgados de los balcones del Ayuntamiento
   - Captura: Tres reposteros rojos con escudo colgados del balcón central (x≈490–535, 580–630, 690–745; y≈350–430) y un pendón rojo largo colgado de la farola (x≈960–1045, y≈240–445).
   - Juego: Sin reposteros ni pendón.
**Vista #1** — 04_Plaza_lados_sur_y_oeste_abril_2009.jpg (abril de 2009) · hoja a_001.jpg

7. [media] Geometría — muro blanco del primer plano izquierdo
   - Captura: El muro blanco desconchado del primer plano ocupa solo x≈0–180; detrás asoma un edificio blanco de tres plantas con balcones de hierro y rótulo de tienda (x≈180–305).
   - Juego: El muro blanco del primer plano es mucho más ancho (x≈0–322) y tapa por completo la zona del edificio blanco con balcones.
8. [media] Huecos — planta primera de la fachada principal del edificio de ladrillo
   - Captura: Tres balcones con barandilla de hierro negro en la planta primera (x≈312–355, 370–420, 435–490; y≈280–312).
   - Juego: Un solo balcón (x≈440–495, y≈288–330); los otros dos huecos son ventanas sin balcón (x≈322–350 y x≈385–415).
9. [media] Huecos — planta segunda de la fachada principal del edificio de ladrillo
   - Captura: Tres ventanas pequeñas casi cuadradas con recercado blanco, sin balcón (x≈330–352, 385–412, 452–480; y≈160–200).
   - Juego: Ventanas altas con persiana marrón y dos balcones con barandilla (x≈322–352, y≈200–240; x≈440–495, y≈183–230).
10. [media] Huecos — planta baja de la fachada principal del edificio de ladrillo
   - Captura: Puerta de madera con recercado de piedra en el centro de la planta baja (x≈383–415, y≈345–420), entre dos ventanas con reja.
   - Juego: Ventana con reja en el lugar de la puerta (x≈385–415, y≈345–395); la planta baja frontal no tiene puerta.
11. [media] Cubierta — remate del edificio de ladrillo rojo
   - Captura: Azotea con pretil de balaustres blancos entre machones de ladrillo rematados en blanco, sobre cornisa blanca (x≈305–660, y≈80–160).
   - Juego: Tejado inclinado de color rojo ladrillo sin balaustrada ni machones (x≈322–665, y≈88–130).
12. [media] Acera y bordillo — borde elevado de la plaza
   - Captura: La plaza queda más alta que la calzada, con un murete/escalón de granito que la recorre de x≈830 a x≈1440 (y≈470–600).
   - Juego: La plaza está a ras de la calzada adoquinada (x≈700–1440, y≈440–560), sin escalón ni murete.
13. [media] Vegetación — árbol junto a la esquina del edificio rojo
   - Captura: No hay árbol delante de la esquina del edificio rojo: calle lateral con un banco (x≈607–680, y≈360–430).
   - Juego: Árbol redondo pequeño delante de la esquina del edificio rojo (x≈607–680, y≈360–430).
14. [media] Vegetación — árboles del fondo de la plaza
   - Captura: En el fondo de la plaza (x≈930–1035, y≈335–375) solo hay farolas, bancos y la fuente; no hay árboles.
   - Juego: Dos árboles redondos pequeños en el fondo de la plaza (x≈932–980 y x≈990–1035, y≈335–370).
15. [media] Mobiliario — farola principal de la plaza
   - Captura: Farola alta gris de fundición con cuatro faroles sobre un banco circular de piedra (x≈1090–1230, y≈185–520).
   - Juego: Poste negro con dos faroles blancos (x≈1035–1120, y≈255–440), sin banco circular.
16. [baja] Detalles de fachada — toldo del edificio del fondo derecho
   - Captura: Toldo largo marrón rojizo de un café en la planta baja del edificio del fondo derecho (x≈1220–1440, y≈335–360).
   - Juego: Sin toldo en esa fachada.
17. [baja] Acera y bordillo — bordillo pintado de amarillo
   - Captura: Bordillo pintado de amarillo que bordea la plaza en curva desde la esquina del edificio rojo hasta abajo a la derecha (x≈450–1010, y≈470–693).
   - Juego: Sin bordillo amarillo; el adoquín pasa a las losas de la plaza sin marca.
18. [baja] Vegetación — jardineras redondas con flores
   - Captura: No hay jardineras con flores: losas de la plaza y, a la derecha, una terraza de café.
   - Juego: Dos jardineras redondas con flores rojas (x≈988–1055, y≈380–400; x≈1300–1385, y≈382–395).
19. [baja] Mobiliario — contenedores de basura
   - Captura: Tres contenedores verdes en fila en el borde de la plaza (x≈665–840, y≈435–545).
   - Juego: No hay contenedores en esa zona.
20. [baja] Mobiliario — señal de tráfico en la plaza
   - Captura: No hay ninguna señal en esa zona de la plaza.
   - Juego: Señal de disco rojo sobre poste fino en medio de la plaza (x≈1058–1075, y≈325–490).
**Vista #2** — 05_Ayuntamiento_y_lado_oeste_marzo_2009.jpg (marzo de 2009) · hoja a_002.jpg

21. [alta] Color de fachada — edificio del fondo de la plaza (derecha)
   - Captura: Fachada blanca de dos plantas al fondo de la plaza (x≈725–830, y≈245–380).
   - Juego: Fachada amarillo ocre (x≈725–820, y≈300–375).
22. [alta] Huecos — gran arco del lateral del Ayuntamiento
   - Captura: Arco de medio punto grande en la planta baja, el más cercano a la cámara (x≈1100–1290, y≈250–450), con una ventana oscura al fondo.
   - Juego: Paño de sillería continuo sin ningún arco en esa zona (x≈1060–1440); los únicos arcos quedan lejos (x≈910–1000).
23. [media] Geometría — escalinata de la plaza
   - Captura: Escalones de granito a la izquierda (x≈0–300, y≈470–560).
   - Juego: Suelo llano de losas, sin escalones.
24. [media] Geometría — torre al fondo de la calle
   - Captura: Cielo en esa zona; no se ve ninguna torre (x≈865–895, y≈255–305).
   - Juego: Torre de ladrillo con chapitel al fondo (x≈865–895, y≈258–305).
25. [media] Cubierta — edificios del fondo de la plaza
   - Captura: Edificios blancos del fondo rematados en cornisa recta con pretil, sin teja visible (x≈655–830, y≈245–260).
   - Juego: Tejados de teja naranja en los edificios del fondo (x≈640–730, y≈260–270; x≈725–820, y≈298–305).
26. [media] Acera y bordillo — borde de la plaza con la calle Grande
   - Captura: La plaza queda elevada sobre la calle con un murete de granito (x≈595–860, y≈455–530).
   - Juego: La plaza baja hasta la calle con un bordillo blanco bajo en diagonal (x≈180–700, y≈480–693).
27. [media] Vegetación — magnolio del primer plano
   - Captura: Un único árbol grande de hoja ancha (magnolio) cuya copa ocupa x≈0–680 desde el borde superior hasta y≈450, con el tronco en x≈370–400.
   - Juego: Dos árboles redondos pequeños separados (x≈0–240 con tronco en x≈60; x≈260–510 con tronco en x≈400) más otro en la esquina inferior izquierda (x≈0–80, y≈465–620); las copas no pasan de y≈285.
28. [media] Mobiliario — farola central de la plaza
   - Captura: Farola alta gris de fundición de varios brazos sobre un banco circular de piedra (x≈705–775, y≈240–445).
   - Juego: En x≈705–775 no hay farola; la más cercana es un poste negro con dos faroles blancos en x≈570–630 (y≈270–425), sin banco circular.
29. [baja] Detalles de fachada — farol de pared y recuadro de la planta alta del lateral
   - Captura: Farol de brazo en la pared (x≈1195–1245, y≈75–160) dentro de un recuadro moldurado (x≈1150–1260, y≈95–190).
   - Juego: Paño de sillería liso, sin farol ni recuadro.
30. [baja] Detalles de fachada — toldo del café del fondo izquierdo
   - Captura: Toldo marrón rojizo de un café al fondo (x≈530–640, y≈340–375).
   - Juego: Sin toldo en esa zona.
31. [baja] Acera y bordillo — bordillo amarillo junto al Ayuntamiento
   - Captura: Bordillo pintado de amarillo desde x≈690,y≈575 hasta x≈1440,y≈500.
   - Juego: Sin bordillo pintado.
32. [baja] Vegetación — seto en jardinera
   - Captura: Seto bajo recortado dentro de una jardinera de piedra (x≈295–595, y≈455–515).
   - Juego: No hay seto; suelo de losas.
33. [baja] Mobiliario — contenedores de basura
   - Captura: Contenedores verdes en primer plano (x≈250–690, y≈490–693).
   - Juego: No hay contenedores.
34. [baja] Mobiliario — bancos de la plaza
   - Captura: Bancos de madera y hierro en la plaza (x≈95–195, y≈410–440; x≈435–495, y≈410–450; x≈558–648, y≈418–455).
   - Juego: No hay bancos en esa zona.
35. [baja] Mobiliario — señal de tráfico en la plaza
   - Captura: Plaza despejada, sin señal.
   - Juego: Señal circular sobre poste en medio de la plaza (x≈738–760, y≈330–455).
**Vista #3** — 06_Lateral_Ayuntamiento_y_calle_Tunel_marzo_2009.jpg (marzo de 2009) · hoja a_003.jpg

36. [alta] Huecos — arco del lateral del Ayuntamiento
   - Captura: Arco de medio punto grande en planta baja (x≈190–360, y≈250–470) con ventana al fondo.
   - Juego: Muro de sillería continuo sin arco (x≈130–528); solo una puerta estrecha en x≈60–110.
37. [media] Geometría — altura de la casa de la derecha
   - Captura: Planta baja muy alta (puertas hasta y≈210–245); la planta alta solo asoma en el borde superior con balcones (y≈0–55) y no se ve tejado.
   - Juego: Casa de dos plantas más baja, con la planta alta completa (balcones en y≈130–300) y alero de teja visible arriba.
38. [media] Color de fachada — acabado del lateral del Ayuntamiento
   - Captura: Paramento liso blanco grisáceo con juntas apenas marcadas (x≈0–520).
   - Juego: Sillería beige almohadillada con juntas muy marcadas (x≈0–528).
39. [media] Huecos — ventanas estrechas junto a la esquina del Ayuntamiento
   - Captura: Dos ventanas estrechas cerca de la esquina, la baja con reja (x≈480–500, y≈175–240 y y≈305–390).
   - Juego: Muro liso sin huecos en x≈480–528.
40. [media] Huecos — puerta acristalada de la casa de la esquina
   - Captura: Puerta acristalada de madera marrón de suelo a y≈245 (x≈640–745, y≈245–480).
   - Juego: Ventana con persiana blanca y macetas (x≈588–680, y≈350–470).
41. [media] Huecos — portón de madera de la casa de la derecha
   - Captura: Gran portón de madera de dos hojas, viejo, de y≈210 al suelo (x≈945–1140, y≈210–610).
   - Juego: Ventana con persiana blanca y recercado blanco (x≈1110–1285, y≈350–510) y balcón encima.
42. [media] Detalles de fachada — molduras de yeso y ménsulas sobre las puertas
   - Captura: Molduras ornamentales de yeso y ménsulas sobre las dos puertas (x≈550–825, y≈60–230; x≈935–1180, y≈30–210) y pilastras.
   - Juego: Fachada lisa con balcones de barandilla, sin molduras ni ménsulas.
43. [media] Zócalo — zócalo de la casa de la derecha
   - Captura: Fachada blanca hasta el suelo, solo con la base algo manchada de gris (x≈520–830, y≈470–575).
   - Juego: Zócalo beige-marrón continuo hasta y≈450–510 (x≈528–1440).
44. [media] Cubierta — alero de la casa de la derecha
   - Captura: No se ve tejado: la fachada sigue por encima del borde superior.
   - Juego: Alero de teja naranja visible arriba (x≈500–960, y≈0–110).
45. [media] Acera y bordillo — acera junto al Ayuntamiento
   - Captura: Acera estrecha a lo largo del Ayuntamiento con bordillo pintado de amarillo (x≈0–520, y≈420–600).
   - Juego: El muro arranca directamente del adoquinado, sin acera ni bordillo amarillo (x≈0–528, y≈420–480).
46. [baja] Detalles de fachada — farol de pared del lateral del Ayuntamiento
   - Captura: Farol de brazo en la pared (x≈295–330, y≈100–150).
   - Juego: Sin farol en esa zona.
47. [baja] Detalles de fachada — toldo a rayas
   - Captura: No hay toldo.
   - Juego: Toldo a rayas rojas y blancas sobre la ventana central de la planta alta (x≈797–947, y≈62–110).
48. [baja] Mobiliario — brazo de farol en la fachada derecha
   - Captura: Pilastra blanca sin farol (x≈1370–1440, y≈140–190).
   - Juego: Brazo de farol negro en la fachada (x≈1370–1440, y≈140–190).
**Vista #4** — 07_Acceso_calle_Grande_marzo_2009.jpg (marzo de 2009) · hoja a_004.jpg

49. [media] Geometría — altura de las casas de la izquierda (primer tramo)
   - Captura: Casas altas: la planta baja llega a y≈170 y encima hay balcones que salen por arriba (x≈410–600, y≈20–190); no se ve tejado.
   - Juego: Casa de dos plantas con alero de teja naranja visible (x≈330–580, y≈0–160).
50. [media] Huecos — portón de la primera casa de la izquierda
   - Captura: Gran portón de madera de dos hojas con marco moldurado (x≈0–240, y≈170–560).
   - Juego: Ventana con persiana blanca (x≈195–360, y≈350–525) y paño liso; balcón encima (x≈170–405, y≈130–300).
51. [media] Huecos — puerta acristalada de la segunda casa de la izquierda
   - Captura: Puerta acristalada de madera marrón alta (x≈460–530, y≈255–460).
   - Juego: Hueco pequeño con recercado blanco y más bajo (x≈475–535, y≈350–425).
52. [media] Huecos — ventana con contraventanas de la izquierda
   - Captura: No hay ventana con contraventanas en esa zona (x≈450–555, y≈135–265): hay molduras de yeso.
   - Juego: Ventana con contraventanas de madera marrón abiertas (x≈450–555, y≈135–265).
53. [media] Huecos — puerta del número 2 del edificio de ladrillo
   - Captura: Puerta de madera con recercado de piedra y número 2 encima (x≈1150–1265, y≈310–545).
   - Juego: Ventana con reja en esa posición (x≈1165–1245, y≈350–475); no hay puerta.
54. [media] Huecos — planta primera del edificio de ladrillo (lado calle Grande)
   - Captura: Tres balcones con barandilla de hierro abombada (x≈1060–1120, y≈220–280; x≈1135–1260, y≈150–260; x≈1320–1440, y≈40–190).
   - Juego: Dos ventanas sin balcón (x≈1075–1110, y≈185–275; x≈1170–1245, y≈95–245) y un solo balcón (x≈1300–1440, y≈110–290).
55. [media] Detalles de fachada — molduras sobre la puerta acristalada de la izquierda
   - Captura: Molduras y ménsulas de yeso ornamentales sobre la puerta acristalada (x≈410–600, y≈90–280).
   - Juego: Pared lisa con un farol de brazo y una ventana con contraventanas marrones (x≈405–555, y≈135–265).
56. [media] Zócalo — zócalo del edificio de ladrillo
   - Captura: Zócalo de piedra clara color crema (x≈1055–1440, y≈450–620).
   - Juego: Zócalo gris oscuro (x≈1060–1440, y≈430–650).
57. [media] Vegetación — arbolillos de la acera izquierda
   - Captura: Arbolillos en alcorque a lo largo de la acera izquierda (x≈620–730 con tronco en x≈675–682, y≈250–525; x≈765–840, y≈300–410).
   - Juego: Ningún árbol en la acera izquierda (x≈620–840).
58. [baja] Detalles de fachada — farol de pared de la izquierda
   - Captura: Sin farol en la fachada en esa zona.
   - Juego: Farol de brazo negro en la fachada (x≈405–460, y≈210–265).

### Plaza de Santa María

**Vista #5** — 03_Desde_el_lado_norte_hacia_la_iglesia.jpg (mayo de 2024) · hoja a_005.jpg

59. [alta] Geometría — volumen del muro norte de la iglesia
   - Captura: Muro norte en un solo plano desde el suelo hasta por encima del borde superior (x≈530–1440, y≈0–390); la cornisa de la esquina izquierda queda en y≈20 (x≈530).
   - Juego: La iglesia sale escalonada: un cuerpo bajo adelantado a todo lo largo (x≈548–1440, hasta y≈250) y el muro alto retranqueado encima; la esquina superior izquierda del muro alto queda en y≈160 (x≈580), mucho más baja.
60. [media] Color de fachada — fábrica del muro norte
   - Captura: Mampostería irregular de piedras de tamaños variados, tono general rosado-pardo (media ≈ RGB 184,162,140).
   - Juego: Hiladas regulares de piezas pequeñas alargadas beige, naranja y gris, tono más apagado (≈ RGB 153,141,122).
61. [media] Huecos — ventanas altas del muro norte
   - Captura: Tres ventanas de medio punto muy altas con recercado moldurado y adorno debajo: x≈585–620 (y≈55–140), x≈715–745 (y≈5–85), x≈900–935 (y≈0–40).
   - Juego: Cuatro ventanas de medio punto sin recercado y más bajas: x≈675–695 (y≈170–240), x≈803–828 (y≈140–220), x≈982–1018 (y≈95–195), x≈1250–1305 (y≈30–160).
62. [media] Huecos — planta alta del edificio blanco de la izquierda
   - Captura: Ventanas con persiana enrollable blanca, sin contraventanas (x≈60–125, 165–215, 295–355; y≈215–310).
   - Juego: Ventanas con contraventanas de madera marrón abiertas (x≈110–250, 278–345, 360–405; y≈200–295).
63. [media] Huecos — planta baja del edificio blanco de la izquierda
   - Captura: Ventana con reja en x≈297–325 (y≈335–410), junto a un gran hueco enrejado de tres paños (x≈170–280).
   - Juego: Puerta blanca en x≈297–325 (y≈350–415) y una ventana enrejada más pequeña en x≈155–228.
64. [media] Detalles de fachada — portada del lado norte
   - Captura: Portada clásica de piedra: arco de medio punto entre pilastras, entablamento y hornacina con remate encima (x≈680–775, y≈215–370).
   - Juego: Puerta de madera de medio punto con recercado sencillo (x≈778–830, y≈305–395) y un ventanuco arqueado encima (x≈790–808, y≈258–290); sin pilastras, entablamento ni hornacina, y unos 70 px más a la derecha.
65. [media] Detalles de fachada — pilastras de sillería del muro norte
   - Captura: Pilastras/contrafuertes de sillería de granito que bajan de arriba abajo (x≈640–700, 780–830, 1020–1080).
   - Juego: Contrafuertes solo en el cuerpo alto retranqueado (x≈600–640, 720–760, 880–920, 1100–1185); el cuerpo bajo es liso.
66. [media] Cubierta — edificio blanco de la izquierda
   - Captura: Edificio blanco de dos plantas rematado en azotea, sin teja visible (x≈0–370, y≈190–240).
   - Juego: Casa blanca con alero de teja naranja (x≈0–410, y≈125–275).
67. [media] Calzada — suelo de la plaza
   - Captura: Toda la plaza es asfalto gris claro uniforme hasta la fila de coches (x≈0–1440, y≈370–693).
   - Juego: Mitad izquierda de tierra/arena beige (x≈0–700, y≈380–693) con un borde curvo marcado contra asfalto gris oscuro a la derecha (x≈520–720); losas blancas en el primer plano inferior (x≈330–700, y≈610–693).
68. [baja] Vehículos — aparcamiento en batería junto a la iglesia
   - Captura: Fila continua de coches aparcados en batería contra el muro de la iglesia (x≈540–1440, y≈365–465).
   - Juego: Ningún coche; la franja junto a la iglesia está vacía.
**Vista #6** — 04_Lado_norte_hacia_el_oeste.jpg (mayo de 2024) · hoja a_006.jpg

69. [media] Color de fachada — fábrica del muro de la iglesia (primer plano)
   - Captura: Mampostería irregular de lajas planas oscuras recibidas con mucho mortero claro (x≈0–660, y≈0–360).
   - Juego: Hiladas regulares de piezas redondeadas grandes beige, naranja y gris con llagas blancas anchas (x≈0–850).
70. [media] Huecos — fachada del edificio del aparcamiento público
   - Captura: Paño blanco ciego, sin ventanas ni cochera (x≈940–1270, y≈225–400).
   - Juego: Ventanas con marco marrón y balconcillos (x≈1005–1050, 1115–1160, 1250–1300; y≈265–330) y una cochera marrón (x≈985–1070, y≈345–388).
71. [media] Huecos — puerta metálica del edificio de la derecha
   - Captura: Gran puerta metálica gris de lamas (x≈1340–1440, y≈240–500).
   - Juego: Paño blanco liso sin puerta (x≈1370–1440).
72. [media] Detalles de fachada — esquina de sillería de la iglesia
   - Captura: Contrafuerte/esquina de sillares de granito (x≈660–770, y≈0–380).
   - Juego: No hay sillería: el muro de piezas llega hasta su borde (x≈850).
73. [media] Zócalo — zarpa en la base del muro de la iglesia
   - Captura: Zarpa/banco inclinado de piedras oscuras con albardilla de granito al pie del muro (x≈0–775, y≈360–693).
   - Juego: El muro baja recto hasta una acera de baldosas, sin zarpa.
74. [media] Cubierta — edificio del aparcamiento público
   - Captura: Edificio blanco rematado en plano con pretil escalonado (x≈940–1270, y≈170–225).
   - Juego: Casa blanca con tejado de teja naranja (x≈930–1440, y≈175–260).
75. [media] Acera y bordillo — pie del muro de la iglesia
   - Captura: La zarpa llega directamente al asfalto; no hay acera (x≈640–780, y≈380–693).
   - Juego: Acera de baldosas grises con bordillo blanco y línea amarilla al pie del muro (x≈620–890, y≈470–693).
76. [media] Muros y vallas — entrada del aparcamiento público
   - Captura: A la derecha se abre la entrada asfaltada del aparcamiento, sin cierre (x≈990–1230, y≈395–500).
   - Juego: Tapia blanca lisa que cierra esa zona (x≈1090–1370, y≈310–520).
77. [baja] Detalles de fachada — pilar de ladrillo del edificio de la derecha
   - Captura: Pilar de ladrillo visto en la esquina (x≈1225–1270, y≈270–510).
   - Juego: Sin pilar de ladrillo; tapia blanca.
78. [baja] Calzada — trampilla metálica en la calzada
   - Captura: Gran trampilla/rejilla metálica en la calzada, junto al bordillo derecho (x≈975–1180, y≈540–693).
   - Juego: Calzada lisa sin trampilla.
79. [baja] Mobiliario — cartel de aparcamiento público
   - Captura: Cartel azul «P PARKING PÚBLICO» en la fachada (x≈975–1045, y≈258–290).
   - Juego: Sin cartel.
**Vista #7** — 05_Salida_del_lado_oeste.jpg (mayo de 2024) · hoja a_007.jpg

80. [alta] Color de fachada — bloque de pisos detrás de la caseta
   - Captura: Bloque de pisos blanco/gris claro de cuatro plantas (x≈480–620, y≈250–370) y edificio blanco detrás de la caseta.
   - Juego: Bloque de ladrillo naranja (x≈555–725, y≈245–330).
81. [media] Geometría — posición y tamaño de la caseta
   - Captura: La caseta ocupa x≈525–810.
   - Juego: La caseta ocupa x≈358–738: más ancha y desplazada a la izquierda.
82. [media] Geometría — casa blanca de la derecha
   - Captura: Casa blanca de dos plantas con alero de teja visible, a cierta distancia (x≈1040–1440, y≈110–440).
   - Juego: La casa está mucho más cerca: ocupa x≈950–1440 y sube por encima del borde superior, sin alero visible.
83. [media] Color de fachada — paredes de la caseta
   - Captura: Paredes color crema (x≈525–810, y≈330–430).
   - Juego: Paredes blancas con zócalo gris (x≈358–738, y≈330–450).
84. [media] Huecos — puerta de la caseta
   - Captura: Puerta gris pequeña (x≈545–570, y≈350–400) y una caja de contadores (x≈600–620, y≈365–395).
   - Juego: Gran puerta azul (x≈488–558, y≈343–440).
85. [media] Huecos — planta baja de la casa de la derecha
   - Captura: Puerta de entrada en x≈1355–1440 (y≈355–440) y ventana con reja (x≈1105–1165).
   - Juego: Cochera con persiana marrón (x≈1285–1440, y≈365–565) y dos ventanas con reja (x≈963–995, x≈1050–1112).
86. [media] Cubierta — tejado de la caseta
   - Captura: Tejado de teja rojiza a dos aguas bien visible (x≈525–810, y≈285–330).
   - Juego: Cubierta casi plana blanca con borde rojo oscuro (x≈358–738, y≈290–330).
87. [media] Calzada — suelo de la explanada
   - Captura: Explanada de asfalto gris con plazas de aparcamiento (x≈0–1440, y≈380–693).
   - Juego: Explanada de losas de piedra clara (x≈0–780, y≈390–693).
88. [media] Acera y bordillo — límite entre la explanada y la calle
   - Captura: Asfalto continuo entre el aparcamiento y la calle, sin bordillo ni aceras.
   - Juego: Bordillo blanco que separa la explanada de la calle (x≈745–860, y≈390–693) y aceras con bordillo blanco a ambos lados de la calle.
89. [media] Vegetación — árboles detrás de la caseta
   - Captura: No hay árboles: cielo y bloques de pisos (x≈145–560, y≈205–390).
   - Juego: Dos árboles grandes de copa ancha (x≈145–560, y≈205–390).
90. [baja] Marcas viales — líneas de aparcamiento
   - Captura: Líneas blancas de plazas y un cebreado (x≈735–770, y≈450–515; x≈1150–1440, y≈470–530).
   - Juego: Sin marcas.
91. [baja] Mobiliario — poste del tendido
   - Captura: Poste del tendido con cables (x≈770–780, y≈215–440).
   - Juego: No hay poste.
92. [baja] Mobiliario — señales de tráfico de la calle
   - Captura: Dos señales circulares rojas en un poste junto a la casa de la derecha (x≈1030–1045, y≈340–375).
   - Juego: Sin señales.
93. [baja] Vehículos — aparcamiento en batería
   - Captura: Aparcamiento en batería lleno, unos quince coches (x≈0–960, y≈370–560).
   - Juego: Solo tres coches al fondo izquierdo (x≈235–360, y≈355–400).

### Plaza de los Castillejos

**Vista #8** — 03_Atrio_y_fachada_sur_de_la_iglesia.jpg (mayo de 2024) · hoja a_008.jpg

94. [alta] Geometría — muro y forma del atrio
   - Captura: Muro de contención alto y largo del atrio, paralelo a la calle, desde x≈520 hasta el borde derecho; su base baja de y≈400 (fondo) a y≈600 (primer plano) y lleva verja encima (y≈300–385).
   - Juego: El atrio es una plataforma baja con una esquina saliente justo delante de la cámara (x≈760–830, y≈430–693) y lados que van a x≈340 y x≈1000; a la derecha (x≈960–1440, y≈390–590) hay una explanada de losas en lugar del muro.
95. [media] Color de fachada — fábrica de la iglesia
   - Captura: Mampostería irregular ocre-rosada con sillares en esquinas, contrafuertes y recercados (x≈590–1250).
   - Juego: Hiladas regulares de piezas alargadas beige y grises (x≈555–1200).
96. [media] Detalles de fachada — portada sur
   - Captura: Portada barroca de piedra con columnas, frontón y hornacina, y puerta roja (x≈725–795, y≈205–345).
   - Juego: Portada de piedra gris sencilla, sin puerta roja (x≈695–745, y≈290–370).
97. [media] Cubierta — remate de la torre
   - Captura: Chapitel de piedra gris con veleta (x≈615–635, y≈40–75) sobre el cuerpo de campanas con pináculos.
   - Juego: Tejadillo piramidal de teja roja con cruz (x≈565–640, y≈95–130).
98. [media] Cubierta — casas de la izquierda
   - Captura: Casas de dos plantas rematadas en cornisa recta, sin teja visible (x≈0–310, y≈185–275).
   - Juego: Alero de teja naranja corrido (x≈0–290, y≈230–310).
99. [media] Vegetación — pinos delante de la torre
   - Captura: Solo un árbol pequeño tras el muro (x≈575–620, y≈290–335); no hay árboles altos delante de la torre.
   - Juego: Dos pinos altos de copa en parasol delante de la torre (x≈355–600, y≈160–380; troncos en x≈485–515).
100. [media] Mobiliario — crucero de piedra
   - Captura: Cruz de piedra sobre columna en el extremo oeste del atrio (x≈550–580, y≈250–335).
   - Juego: No hay crucero; solo un poste fino y una maceta en x≈715–760 (y≈365–425).
101. [baja] Marcas viales — paso de peatones del primer plano
   - Captura: Franjas blancas de paso de peatones en el primer plano derecho (x≈880–1100, y≈560–693).
   - Juego: Sin marcas en el suelo.
102. [baja] Mobiliario — farola del atrio
   - Captura: Farola de dos brazos dentro del atrio junto a la portada (x≈645–685, y≈230–335).
   - Juego: Las farolas están más a la izquierda (x≈437–445 y x≈480–500, y≈290–385); en x≈645–685 no hay farola.
103. [baja] Mobiliario — señal de dirección prohibida
   - Captura: Sin señal en esa zona (casas al fondo de la calle).
   - Juego: Señal de disco rojo sobre poste al fondo izquierdo (x≈318–325, y≈340–400).
**Vista #9** — 04_Acceso_hacia_Cuatro_Esquinas.jpg (mayo de 2024) · hoja a_009.jpg

104. [media] Color de fachada — parte alta de las casas de la izquierda
   - Captura: Fachada crema-amarillenta desconchada en la parte alta de la primera casa y en la segunda (x≈300–600, y≈0–300).
   - Juego: Fachadas blancas.
105. [media] Huecos — planta alta de la casa amarilla
   - Captura: Cuatro balcones (x≈865–935, 1003–1082, 1100–1200, 1258–1370); el tramo izquierdo de la fachada (x≈725–860) es ciego.
   - Juego: Cinco balcones; el primero ya en x≈762–836, en el tramo que en la captura es ciego.
106. [media] Huecos — planta baja de la casa amarilla
   - Captura: Secuencia puerta (x≈865–930) – ventana enrejada (x≈1003–1075) – ventana enrejada (x≈1105–1180) – puerta (x≈1262–1345); tramo izquierdo ciego.
   - Juego: Secuencia ventana enrejada (x≈768–826) – ventana enrejada (x≈900–963) – puerta (x≈1043–1115) – ventana enrejada (x≈1205–1283) – puerta de lamas (x≈1378–1440).
107. [media] Huecos — casa blanca de la izquierda, planta baja
   - Captura: Paño blanco con bajante y una pilastra, sin puerta (x≈395–470, y≈300–550).
   - Juego: Puerta con la parte baja marrón (x≈405–465, y≈350–500).
108. [media] Cubierta — alero de la casa amarilla
   - Captura: Alero de teja árabe rojiza corrido sobre una cornisa blanca (x≈725–1440, y≈155–210).
   - Juego: Remate recto sin teja (x≈722–1440, y≈125–170).
109. [media] Calzada — suelo delante de la casa amarilla
   - Captura: Asfalto hasta la acera estrecha de la casa amarilla (x≈760–1440, y≈440–693).
   - Juego: Explanada de losas claras delante de la casa amarilla (x≈730–1440, y≈440–610).
110. [media] Marcas viales — paso de peatones
   - Captura: Paso de peatones de franjas blancas en primer plano con una pintada en el asfalto (x≈430–960, y≈480–693).
   - Juego: Sin paso de peatones ni marcas.
111. [baja] Acera y bordillo — pavimento de la esquina izquierda
   - Captura: Acera de la esquina con baldosa rojiza (x≈350–565, y≈520–610).
   - Juego: Sin acera rojiza: asfalto beige.
112. [baja] Mobiliario — farol de pared
   - Captura: Farol en la esquina izquierda de la casa amarilla (x≈705–720, y≈280–310).
   - Juego: Farol en mitad de la fachada amarilla, junto a un balcón (x≈1040–1065, y≈270–300); en la esquina no hay.
**Vista #10** — 05_Lado_este_y_entorno_del_abside.jpg (mayo de 2024) · hoja a_010.jpg

113. [media] Color de fachada — fábrica de la cabecera
   - Captura: Mampostería irregular ocre-rosada con piedras oscuras (x≈610–1440).
   - Juego: Hiladas regulares de piezas alargadas beige y grises.
114. [media] Huecos — ventanuco de la capilla
   - Captura: Ventanuco rectangular con recercado de piedra (x≈810–850, y≈95–175).
   - Juego: Muro ciego sin ventana.
115. [media] Detalles de fachada — esquinas de sillería de la cabecera
   - Captura: Esquinas y contrafuerte de sillares de granito (x≈625–710 y x≈975–1110) que enmarcan la mampostería.
   - Juego: Muro uniforme de piezas alargadas, sin sillería en las esquinas.
116. [media] Zócalo — moldura y zócalo de la capilla
   - Captura: Imposta moldurada de granito en y≈315–330 y zócalo de piedra debajo (x≈610–1110, y≈315–420).
   - Juego: Muro uniforme hasta el suelo, sin imposta ni zócalo.
117. [media] Zócalo — zarpa inclinada del muro de la derecha
   - Captura: Gran zarpa inclinada de piedra al pie del muro de la derecha (x≈1110–1440, y≈285–360) sobre un muro de mampostería (y≈355–480).
   - Juego: Muro recto hasta el suelo, sin zarpa.
118. [media] Cubierta — alero de la capilla de la cabecera
   - Captura: Alero de teja sobre el cuerpo bajo de la cabecera (x≈610–960, y≈0–75).
   - Juego: Remate recto sin teja (x≈615–1020, y≈45–60).
119. [media] Cubierta — casa amarilla del fondo
   - Captura: Casa amarilla de dos plantas con tejado de teja a la vista y chimenea (x≈120–480, y≈262–320).
   - Juego: Edificio amarillo de dos plantas con remate plano sin teja (x≈65–470, y≈260–280).
120. [media] Calzada — suelo delante de la cabecera
   - Captura: Asfalto con coches aparcados (x≈0–1440, y≈420–693) y solo una franja estrecha clara al pie del muro (x≈1030–1440, y≈455–500).
   - Juego: Explanada ancha de losas claras (x≈200–1440, y≈410–693) separada por un bordillo del asfalto de la izquierda.
121. [baja] Mobiliario — señales junto al atrio
   - Captura: Señal triangular sobre poste (x≈255–270, y≈350–400) y placa azul (x≈315–325, y≈368–385).
   - Juego: Sin señales en esa zona.
122. [baja] Vehículos — aparcamiento en batería
   - Captura: Cinco coches aparcados en batería delante de la cabecera (x≈0–1090, y≈410–630).
   - Juego: Ningún coche.
**Vista #11** — 06_Acceso_desde_la_Cuesta.jpg (mayo de 2024) · hoja a_011.jpg

123. [media] Geometría — casa amarilla de la derecha
   - Captura: Fachada en un solo plano que se aleja hacia el fondo (x≈840–1440); la parte cercana (x≈1100–1440) es un paño amarillo ciego.
   - Juego: La fachada quiebra hacia la cámara en x≈1040–1100 y la parte cercana (x≈1060–1440) queda casi de frente con un ventanal con persiana (x≈1185–1355, y≈115–240) y una ventana enrejada grande (x≈1185–1355, y≈350–470).
124. [media] Huecos — puerta de la casa amarilla
   - Captura: Puerta de madera oscura con recercado blanco (x≈975–1030, y≈345–470).
   - Juego: Puerta de barrotes metálicos con recercado blanco (x≈965–1010, y≈350–470).
125. [media] Cubierta — alero de la casa amarilla
   - Captura: Alero de teja con borde blanco a lo largo de toda la fachada (x≈840–1150, y≈0–280).
   - Juego: Remate recto sin teja (x≈835–1440, y≈0–265).
126. [media] Acera y bordillo — acera de la casa amarilla
   - Captura: Acera estrecha de baldosa gris a lo largo de la casa amarilla (x≈930–1170, y≈470–693).
   - Juego: Acera ancha de losas claras delante de la casa amarilla (x≈760–1440, y≈390–580).
127. [media] Mobiliario — farola del atrio
   - Captura: Farola de fundición gris con dos faroles (x≈360–420, y≈225–335).
   - Juego: Farola moderna negra de báculo con dos brazos (x≈310–420, y≈245–395).
128. [media] Muros y vallas — verja del atrio de la iglesia
   - Captura: Verja de hierro con aspas en X sobre el murete del atrio (x≈90–600, y≈330–380).
   - Juego: Verja de barrotes verticales entre pilares (x≈0–630, y≈380–580).
129. [baja] Marcas viales — paso de peatones del fondo
   - Captura: Paso de peatones al fondo de la calle (x≈600–750, y≈383–397).
   - Juego: Sin paso de peatones.
130. [baja] Mobiliario — señal del primer plano izquierdo
   - Captura: No hay señal en el primer plano (muro del atrio y furgoneta aparcada).
   - Juego: Señal circular grande sobre poste en primer plano (x≈65–225, y≈295–390; poste hasta abajo en x≈148–165).

### Plaza Vieja

**Vista #12** — 02_Desde_el_acceso_de_Hornillos.jpg (mayo de 2024) · hoja a_012.jpg

131. [media] Geometría — casa vieja de la izquierda
   - Captura: Casa blanca alta con el alero en y≈240–280 y el faldón de teja subiendo hasta y≈150 (x≈0–240).
   - Juego: Casa de una planta más baja, con el alero en y≈315–335 (x≈0–245).
132. [media] Geometría — casa del fondo derecho
   - Captura: Casa blanca de dos plantas con tejado de teja (x≈1010–1195, y≈250–375).
   - Juego: Edificio de tres plantas, más alto, con remate plano (x≈1080–1200, y≈200–380).
133. [media] Color de fachada — casa del fondo derecho
   - Captura: Fachada blanca (x≈1010–1195).
   - Juego: Fachada beige grisácea (x≈1080–1200).
134. [media] Huecos — edificio de dos plantas del lado izquierdo de la plaza
   - Captura: Planta alta con cuatro balcones de barandilla (x≈290–320, 345–375, 400–425, 445–470; y≈255–300); planta baja con ventanas y una puerta oscura (x≈345–375).
   - Juego: Planta alta con ventanas de contraventanas verdes sin balcón (x≈262–330, y≈295–325); planta baja con dos puertas de cochera blancas (x≈258–335 y x≈348–410, y≈340–385).
135. [media] Cubierta — edificio de dos plantas del lado izquierdo de la plaza
   - Captura: Edificio blanco-crema rematado en cornisa recta, sin teja visible (x≈245–495, y≈220–250).
   - Juego: Tejado de teja naranja (x≈245–480, y≈280–300).
136. [media] Acera y bordillo — acera de la izquierda
   - Captura: Asfalto hasta las casas en el primer plano izquierdo (x≈0–460, y≈560–693), sin acera ancha.
   - Juego: Acera ancha de losas claras con bordillo (x≈0–460, y≈385–693).
137. [media] Vegetación — arbolado del jardín central
   - Captura: Copas densas y altas de árboles (x≈625–815, y≈305–380) y palmeras bajas de abanico (x≈770–815, y≈340–380) en un jardín compacto.
   - Juego: Césped grande con tres árboles redondos pequeños separados (x≈668–715, 750–810, 890–940) y palmeras de tronco alto y fino (x≈675–690, 720–735, 815–845).
138. [baja] Mobiliario — contenedores junto al jardín
   - Captura: Contenedores azul y amarillo junto al jardín (x≈625–675, y≈365–395).
   - Juego: Sin contenedores.
139. [baja] Otros — obra de la derecha
   - Captura: Obra en curso a la derecha: vallas metálicas, hormigonera y materiales (x≈905–1440, y≈365–693), torre de celosía (x≈1075–1130, y≈0–440) y edificio de ladrillo visto sin terminar, con huecos sin carpintería (x≈1265–1440, y≈0–480).
   - Juego: Sin obra: acera despejada y edificio de ladrillo terminado con ventanas, persianas y rejas (x≈1270–1440).
140. [baja] Otros — chimenea de ladrillo del fondo
   - Captura: Chimenea alta de ladrillo de antigua fábrica al fondo (x≈795–805, y≈270–300).
   - Juego: No hay chimenea.
**Vista #13** — 03_Desde_el_acceso_de_Derecha.jpg (mayo de 2024) · hoja a_013.jpg

141. [media] Huecos — casa blanca de la derecha, planta alta
   - Captura: Balcones con barandilla en la planta alta (x≈1235–1320, y≈320–345).
   - Juego: Ventanas con contraventanas marrones sin balcón (x≈1225–1325, y≈280–315).
142. [media] Cubierta — casa blanca de la derecha
   - Captura: Remate en pretil con chimenea, sin teja a la vista (x≈1215–1340, y≈262–285).
   - Juego: Tejado de teja naranja (x≈1210–1440, y≈235–300).
143. [media] Acera y bordillo — acera de la izquierda
   - Captura: Acera estrecha junto a las casas (x≈150–330, y≈480–600).
   - Juego: Acera muy ancha de losas claras (x≈0–540, y≈390–693).
144. [media] Acera y bordillo — borde del jardín de la plaza
   - Captura: El jardín acaba en un bordillo bajo y lo rodea el asfalto (x≈460–1440, y≈380–693).
   - Juego: Explanada ancha de losas blancas con bordillo que rodea el césped y forma una punta hacia la cámara (x≈530–1100, y≈375–545).
145. [media] Vegetación — arbolado del jardín central
   - Captura: Copas densas y altas de naranjos y olivos (x≈630–945, y≈295–440).
   - Juego: Árboles redondos pequeños separados (x≈577–820, y≈340–400) y palmeras de tronco alto y fino (x≈640–655, 705–725, 880–905).
146. [baja] Vegetación — plantas en la acera izquierda
   - Captura: Acera sin plantas.
   - Juego: Arbusto cónico y maceta con planta en la acera (x≈95–195, y≈470–575).
147. [baja] Mobiliario — señal de dirección prohibida
   - Captura: Sin señal en esa zona (furgoneta y jardín).
   - Juego: Señal de disco rojo sobre poste junto al jardín (x≈818–830, y≈335–435).
148. [baja] Otros — edificio de ladrillo en obra
   - Captura: Edificio de ladrillo visto sin terminar, con andamio y grúa (x≈905–1110, y≈210–395), sin tejado.
   - Juego: Edificio de ladrillo terminado con ventanas blancas y tejado de teja naranja (x≈905–1080, y≈285–375).
**Vista #14** — 04_Desde_Fuentes_y_Pozo_Dulce.jpg (mayo de 2024) · hoja a_014.jpg

149. [media] Geometría — iglesia al fondo
   - Captura: Tras las casas del fondo asoma el cuerpo pardo de la iglesia junto a la torre (x≈950–1035, y≈270–305).
   - Juego: Solo asoma la torre (x≈932–950); en x≈950–1035, y≈270–305 hay cielo sobre casas blancas con teja.
150. [media] Huecos — primera casa de la izquierda
   - Captura: Jamba de granito (x≈0–90, y≈320–560) y ventana con reja (x≈125–175, y≈375–470).
   - Juego: Gran puerta de cochera de madera (x≈105–260, y≈335–590).
151. [media] Zócalo — casa blanca de la derecha
   - Captura: Zócalo gris de aproximadamente un metro a lo largo de la fachada (x≈1100–1440, y≈410–520).
   - Juego: Fachada blanca hasta el suelo, sin zócalo.
152. [media] Acera y bordillo — acera de la izquierda
   - Captura: Acera estrecha junto a las casas; los coches aparcan en el asfalto y a la derecha del coche blanco (x≈690–810, y≈450–693) ya es calzada.
   - Juego: Acera ancha de losas claras que llega hasta x≈810 en el primer plano (x≈0–810, y≈375–693).
153. [media] Vegetación — arbolado del jardín central
   - Captura: Copas densas de árboles y un olivo (x≈700–910, y≈310–400).
   - Juego: Árboles redondos pequeños (x≈655–690, 755–820, 830–865) y palmeras altas de tronco fino (x≈720–735, 750–762, 822–835).
154. [baja] Acera y bordillo — bordillo en la calzada (primer plano derecho)
   - Captura: Asfalto con una tapa de registro (x≈1135–1220, y≈545–575); ningún bordillo en la calzada.
   - Juego: Tramo de bordillo blanco tendido en la calzada (x≈1155–1335, y≈615–693).
155. [baja] Mobiliario — farol de pared de la izquierda
   - Captura: Farol de pared (x≈360–395, y≈255–290).
   - Juego: Sin farol.
156. [baja] Mobiliario — farol de pared de la derecha
   - Captura: Farol de pared en la esquina de la casa de la derecha (x≈1075–1130, y≈225–275).
   - Juego: Sin farol.
157. [baja] Mobiliario — contenedores junto al jardín
   - Captura: Contenedores amarillos, negro y marrón (x≈685–785, y≈370–405).
   - Juego: Sin contenedores.
**Vista #15** — 05_Lateral_oeste_del_parque.jpg (mayo de 2024) · hoja a_015.jpg

158. [media] Geometría — volumen de la ermita
   - Captura: Fachada blanca larga y recta, paralela a la plaza, con tejado de teja (x≈1040–1440, y≈205–420).
   - Juego: Bloque blanco alto que sobresale hacia la cámara con tejado a cuatro aguas (x≈1095–1270, y≈240–415) y un lateral que se aleja (x≈1270–1330).
159. [media] Geometría — espadaña de la ermita
   - Captura: Espadaña blanca con cruz en x≈1225–1300 (y≈165–210).
   - Juego: Torrecilla blanca con cruz en x≈1075–1130 (y≈215–280), unos 150 px más a la izquierda.
160. [media] Detalles de fachada — portada de la ermita
   - Captura: Portada barroca de piedra con frontón curvo y hornacina sobre el arco de la puerta (x≈975–1045, y≈235–385).
   - Juego: Recercado de piedra sencillo con puerta de medio punto y un ventanuco encima (x≈1005–1060, y≈295–385), sin frontón ni hornacina.
161. [media] Zócalo — zócalo de la ermita
   - Captura: Zócalo gris corrido (x≈1040–1440, y≈375–420).
   - Juego: Fachada blanca hasta el suelo, sin zócalo.
162. [media] Acera y bordillo — borde del jardín
   - Captura: El césped está rodeado por un bordillo estrecho de baldosa (x≈400–1030, y≈410–575) y fuera hay asfalto.
   - Juego: Explanada muy ancha de losas blancas alrededor del césped (x≈0–1070, y≈380–693).
163. [media] Vegetación — árbol grande del primer plano izquierdo
   - Captura: En x≈240–470 no hay árbol: asfalto y casas al fondo.
   - Juego: Naranjo grande y redondo (x≈240–470, y≈325–485).
164. [media] Vegetación — palmera del jardín
   - Captura: Una palmera baja de abanico (x≈570–680, y≈350–450).
   - Juego: Dos palmeras de tronco alto y fino que suben hasta y≈245 (troncos en x≈685 y x≈738).
165. [media] Vegetación — árbol grande del centro del jardín
   - Captura: Un árbol de copa densa y grande (x≈620–830, y≈270–410) y un olivo a su derecha (x≈750–900, y≈335–430).
   - Juego: Árboles redondos pequeños separados (x≈600–680, 680–750, 795–875; y≈315–415).
166. [media] Vegetación — palmera sobre la ermita
   - Captura: Cielo sobre la ermita.
   - Juego: Palmera grande detrás de la ermita (x≈1120–1200, y≈160–240).
167. [baja] Mobiliario — contenedores amarillos
   - Captura: Dos contenedores amarillos grandes (x≈1030–1240, y≈410–545).
   - Juego: Sin contenedores.
168. [baja] Mobiliario — banco del jardín
   - Captura: Banco cerca, en el borde derecho del césped (x≈850–965, y≈425–485).
   - Juego: Banco más lejos y pequeño (x≈765–810, y≈388–410).
169. [baja] Mobiliario — farol de la ermita
   - Captura: Farol de pared en la fachada (x≈1190–1215, y≈250–290).
   - Juego: Sin farol.
170. [baja] Otros — obra de la izquierda
   - Captura: Valla de obra con pancartas y andamio (x≈0–175, y≈210–465).
   - Juego: Sin obra.

### Calle Atrás

**Vista #16** — 02_Entrada_oeste_hacia_el_centro.jpg (mayo de 2024) · hoja a_016.jpg

171. [media] Huecos — portón del número 102
   - Captura: Portón de madera rojo oscuro de dos hojas con aldabas (x≈220–430, y≈370–693).
   - Juego: Puerta doble rosa con dos ventanillos de cristal (x≈0–310, y≈370–693), más a la izquierda.
172. [media] Huecos — planta alta del número 102
   - Captura: Ventana con persiana enrollable marrón, sin balcón (x≈330–430, y≈60–250).
   - Juego: Balcón con barandilla de barrotes y macetas con flores (x≈0–405, y≈0–260).
173. [media] Huecos — planta baja de la segunda casa de la izquierda
   - Captura: Paño blanco en x≈495–530 y ventana con reja en x≈545–585 (y≈360–460).
   - Juego: Puerta marrón rosada en x≈495–530 (y≈360–500) y ventana pequeña en x≈590–605.
174. [media] Huecos — cochera de la casa de la derecha
   - Captura: Puerta de cochera blanca (x≈1025–1105, y≈280–430).
   - Juego: Puerta con cortina de tiras de colores (x≈970–1045, y≈350–530).
175. [media] Huecos — balcón de balaustres de la casa de la derecha
   - Captura: Balcón con balaustrada blanca (x≈950–1070, y≈160–245).
   - Juego: Ventana con persiana y macetas en el alféizar, sin balcón (x≈975–1040, y≈85–240).
176. [media] Huecos — balcón de la casa más cercana a la derecha
   - Captura: Balcón con barandilla de hierro labrada a todo lo ancho (x≈1165–1440, y≈80–300).
   - Juego: Ventana con contraventana/persiana marrón, sin balcón (x≈1180–1310, y≈0–145).
177. [media] Huecos — planta baja de la casa más cercana a la derecha
   - Captura: Ventana grande con reja de hierro (x≈1240–1440, y≈340–520).
   - Juego: Puerta rosa en el borde derecho (x≈1350–1440, y≈380–693) y paño liso.
178. [media] Cubierta — remate de las casas de la izquierda
   - Captura: Pretiles y cornisas rectas, sin teja ni hastiales (x≈430–720, y≈0–260); una chimenea en x≈615–635.
   - Juego: Hastial triangular con teja naranja de cara a la calle (x≈465–645, y≈30–210).
179. [media] Acera y bordillo — acera izquierda
   - Captura: Acera ancha de baldosa gris (de la fachada en x≈330 al bordillo en x≈610 en el borde inferior).
   - Juego: Acera estrecha (de la fachada en x≈310 al bordillo en x≈420 en el borde inferior).
180. [baja] Detalles de fachada — número 102
   - Captura: Placa con el número 102 sobre el portón (x≈380–410, y≈335–355).
   - Juego: Sin número.
181. [baja] Acera y bordillo — bordillo derecho
   - Captura: Bordillo pintado de amarillo en la acera derecha (x≈820–945, y≈360–435).
   - Juego: Bordillo blanco sin pintar.
**Vista #17** — 03_Extremo_junto_a_Medellin.jpg (mayo de 2024) · hoja a_017.jpg

182. [alta] Color de fachada — casa blanca moderna de la izquierda
   - Captura: Fachada blanca (x≈595–785, y≈20–500).
   - Juego: Fachada rojo anaranjado de ladrillo (x≈590–895, y≈0–670).
183. [alta] Color de fachada — edificio del fondo de la calle
   - Captura: Casas blancas al fondo (x≈1045–1145, y≈285–385).
   - Juego: Edificio de ladrillo naranja (x≈1090–1255, y≈260–370).
184. [media] Huecos — planta baja de la casa moderna
   - Captura: Porche retranqueado con cancela y barandilla de hierro oscuro (x≈635–770, y≈290–460).
   - Juego: Dos puertas grises de barrotes en fachada (x≈695–760, y≈365–625; x≈835–857, y≈360–475).
185. [media] Huecos — planta alta de la casa moderna
   - Captura: Un balcón corrido con barandilla de barras horizontales oscuras (x≈635–770, y≈190–265).
   - Juego: Dos balcones con barandilla de barrotes verticales (x≈670–830, y≈75–295; x≈830–895, y≈215–315).
186. [media] Huecos — portón del edificio de la izquierda
   - Captura: Gran portón corredero de chapa marrón oscuro (x≈140–545, y≈265–650).
   - Juego: Persiana de madera más baja en x≈0–285 (y≈400–550) y paño liso en x≈285–590.
187. [media] Cubierta — edificio de la izquierda
   - Captura: Muro alto que sale por el borde superior, sin alero visible (x≈0–530).
   - Juego: Alero de teja muy grande y bajo cruzando la parte alta (x≈0–650, y≈20–265).
188. [media] Marcas viales — líneas de la calzada
   - Captura: Calzada sin líneas pintadas.
   - Juego: Línea blanca central continua (x≈1040–1230, y≈400–693) y línea de borde a la derecha (x≈1275–1440, y≈420–470).
189. [baja] Detalles de fachada — toldo a rayas
   - Captura: Sin toldo.
   - Juego: Toldo a rayas rojas y blancas en lo alto (x≈745–850, y≈0–75).
190. [baja] Acera y bordillo — acera izquierda
   - Captura: Acera de pavimento gris oscuro (x≈200–650, y≈490–693).
   - Juego: Acera de baldosa clara con bordillo blanco (x≈720–990, y≈370–693).
191. [baja] Vegetación — macetas en la acera izquierda
   - Captura: Acera sin macetas.
   - Juego: Macetas con flores y un cactus junto a las puertas (x≈640–835, y≈490–693).
192. [baja] Mobiliario — señal de vado en el portón
   - Captura: Placa de prohibido aparcar en el portón (x≈375–415, y≈345–390).
   - Juego: Sin señal.
193. [baja] Mobiliario — farol de pared grande
   - Captura: Farol de brazo grande en la esquina de la casa moderna (x≈560–605, y≈110–225).
   - Juego: Sin farol.
194. [baja] Mobiliario — farola del fondo izquierdo
   - Captura: Sin farola en esa zona.
   - Juego: Farola de báculo en la acera izquierda al fondo (x≈965–1010, y≈280–395).
**Vista #18** — 04_Tramo_occidental_hacia_la_Cuesta.jpg (mayo de 2024) · hoja a_018.jpg

195. [media] Geometría — tramo cercano de la derecha
   - Captura: La misma fachada continúa hasta el borde derecho con el alero en y≈0–80 (x≈1210–1440).
   - Juego: Casa baja aparte con alero de teja en y≈250–305 delante de una nave más alta (x≈1210–1440).
196. [media] Huecos — portón del edificio de la derecha
   - Captura: Un portón de chapa gris oscuro casi negro con placa de vado (x≈915–1050, y≈290–475).
   - Juego: Dos puertas azul verdoso (x≈818–845, y≈345–415; x≈988–1120, y≈340–525).
197. [media] Huecos — ventanas del edificio de la derecha
   - Captura: Ventanucos pequeños (x≈850–875, y≈275–305) y una ventana alta apaisada con reja oscura (x≈1110–1295, y≈140–250).
   - Juego: Bandas de ventanas apaisadas de nave (x≈870–1150, y≈80–245; x≈865–935, y≈335–357).
198. [media] Huecos — puerta vieja de la primera casa de la izquierda
   - Captura: Puerta de madera vieja y grande con un tablón cruzado (x≈55–255, y≈270–570).
   - Juego: Paño liso en x≈55–255; la puerta del juego es una puerta doble clara más lejos (x≈405–465, y≈365–565).
199. [media] Cubierta — edificio largo de la derecha
   - Captura: Alero de teja a lo largo de toda la fachada (x≈710–1440, de y≈310 a y≈0).
   - Juego: Nave blanca con remate plano sin teja (x≈705–1210).
200. [media] Acera y bordillo — acera izquierda elevada
   - Captura: Acera izquierda muy elevada sobre la calzada con bordillo alto pintado de amarillo (x≈380–650, y≈380–693).
   - Juego: Acera a altura normal con bordillo bajo blanco.
201. [media] Muros y vallas — barandilla de la acera izquierda
   - Captura: Barandilla metálica a lo largo de la acera izquierda (x≈60–600, y≈385–693).
   - Juego: Sin barandilla.
202. [baja] Vegetación — planta junto a la puerta
   - Captura: Planta crecida junto a la puerta (x≈225–280, y≈450–550).
   - Juego: Sin planta.

### Calle Bronca

**Vista #19** — 02_Recorrido_hacia_la_Cuesta_mayo_2024.jpg (mayo de 2024) · hoja a_019.jpg

203. [media] Huecos — planta alta de la casa rosa (n.º 27)
   - Captura: Ventana con persiana enrollable blanca, sin balcón (x≈990–1130, y≈0–170).
   - Juego: Balcón con barandilla de hierro y macetas con flores (x≈905–1225, y≈0–275).
204. [media] Huecos — puerta de la casa rosa (n.º 27)
   - Captura: Puerta vieja de madera marrón, rehundida, con rampa gris delante (x≈990–1145, y≈330–680).
   - Juego: Puerta doble de madera clara con dos ventanillos, a ras de fachada y sin rampa (x≈1000–1155, y≈375–693).
205. [media] Huecos — portón en arco de la izquierda
   - Captura: Portón de madera oscura bajo un arco rebajado en la tapia blanca (x≈220–335, y≈275–590).
   - Juego: Tapia lisa en esa zona; la única puerta es una cochera de madera más al fondo (x≈455–490, y≈340–505).
206. [media] Huecos — puerta enrejada de la casa crema de la derecha
   - Captura: Puerta con cancela de barrotes (x≈840–870, y≈320–500) junto a una ventana enrejada (x≈755–785, y≈320–420).
   - Juego: En x≈840–870 hay paño y zócalo, sin puerta; la ventana enrejada está en x≈785–840 (y≈350–490) y hay una puerta blanca en x≈730–745.
207. [media] Cubierta — edificio tras la tapia de la izquierda
   - Captura: Bloque blanco de remate plano tras la tapia (x≈365–520, y≈195–290).
   - Juego: Casa con tejado de teja naranja y chimenea tras la tapia (x≈180–525, y≈160–290).
**Vista #20** — 03_Recorrido_hacia_el_norte_mayo_2024.jpg (mayo de 2024) · hoja a_020.jpg

208. [alta] Geometría — edificio de la derecha
   - Captura: Tapia/casa baja de una planta, blanca, con alero de teja desde x≈620 (y≈250) hasta el borde derecho (y≈80).
   - Juego: Casa de dos plantas que sube por encima del borde superior en todo el tramo x≈685–1440.
209. [media] Color de fachada — paramento de la derecha
   - Captura: Tapia encalada blanca con un desconchón que deja ver el ladrillo rojo (x≈795–930, y≈515–693).
   - Juego: Fachada crema/beige uniforme.
210. [media] Color de fachada — casa de la izquierda (primer plano)
   - Captura: Fachada color crema/ocre claro (x≈0–280).
   - Juego: Fachada gris blanquecina (x≈0–290).
211. [media] Huecos — portón de la derecha
   - Captura: Gran cancela de hierro oscuro de dos hojas (x≈695–795, y≈315–600).
   - Juego: Puerta estrecha (x≈718–745, y≈365–550) y ventana enrejada (x≈805–915, y≈360–670).
212. [media] Huecos — balcones de la derecha
   - Captura: Sin balcones (edificio de una planta).
   - Juego: Dos balcones con barandilla en la planta alta (x≈660–745, y≈150–300; x≈740–950, y≈0–275).
213. [media] Huecos — planta alta de la casa crema de la izquierda
   - Captura: Balcón con barandilla (x≈185–285, y≈215–310).
   - Juego: Ventana con contraventanas de madera marrón, sin balcón (x≈140–285, y≈0–225).
214. [media] Huecos — puertas verdes de las casas blancas de la izquierda
   - Captura: Puerta/portón verde (x≈355–390, y≈365–495) y otra verde más al fondo (x≈455–470).
   - Juego: Ventana enrejada (x≈330–365, y≈350–440) y puerta clara (x≈395–410); nada verde.
215. [media] Zócalo — zócalo de la derecha
   - Captura: Sin zócalo: el encalado llega al suelo.
   - Juego: Zócalo de azulejo marrón (x≈690–980, y≈460–693).
216. [media] Cubierta — alero de la derecha
   - Captura: Alero corrido de teja con remate de chapa marrón a lo largo de la tapia (x≈905–1440, y≈90–250).
   - Juego: La fachada sigue hacia arriba; solo hay un trozo suelto de alero de teja naranja festoneado (x≈1150–1440, y≈0–180).
217. [media] Acera y bordillo — acera derecha
   - Captura: Acera de baldosa gris a lo largo de la tapia (x≈580–830, y≈450–693).
   - Juego: No hay acera a la derecha: la fachada arranca de la calzada.
218. [baja] Vegetación — macetas de la acera izquierda
   - Captura: Acera sin macetas.
   - Juego: Macetas con plantas y arbusto cónico (x≈280–380, y≈420–540) y flores rosas en la esquina inferior izquierda (x≈0–90, y≈640–693).
219. [baja] Vegetación — palmera al fondo
   - Captura: No se ve ninguna palmera al fondo.
   - Juego: Palmera al fondo de la calle (x≈565–580, y≈283–305).
**Vista #21** — 04_Tramo_medio_hacia_el_sur_mayo_2024.jpg (mayo de 2024) · hoja a_021.jpg

220. [media] Huecos — ventanal de la casa de la izquierda
   - Captura: Ventanal con carpintería de madera y reja de hierro forjado (x≈85–325, y≈270–565).
   - Juego: Paño beige liso con un recuadro más claro (x≈0–135, y≈325–693), sin ventana.
221. [media] Huecos — puerta de la casa de la izquierda
   - Captura: Puerta rehundida con aplacado de piedra y buzón (x≈420–500, y≈280–500).
   - Juego: Ventana con reja en esa zona (x≈500–555, y≈355–545); no hay puerta.
222. [media] Huecos — reja de la casa cercana de la derecha
   - Captura: Ventana con reja de rombos (x≈1200–1440, y≈340–650).
   - Juego: Ventana con reja de barrotes verticales (x≈1110–1440, y≈355–680).
223. [media] Huecos — planta alta de la casa cercana de la derecha
   - Captura: Paño blanco liso con cables (x≈1000–1440, y≈0–330) y una ventana pequeña (x≈925–955, y≈170–245).
   - Juego: Ventana grande con reja de barrotes (x≈1125–1440, y≈0–180) y aparato de aire acondicionado (x≈1020–1125, y≈35–135).
224. [media] Huecos — planta baja de la segunda casa de la derecha
   - Captura: Ventana con reja (x≈895–940, y≈350–470).
   - Juego: Puerta con celosía gris (x≈908–955, y≈360–490).
225. [media] Detalles de fachada — recercado pétreo de la casa de la izquierda
   - Captura: Gran recercado de aplacado granítico moteado gris alrededor del ventanal (x≈0–325, y≈210–600).
   - Juego: Sin recercado.
226. [media] Zócalo — zócalo de la casa de la izquierda
   - Captura: Zócalo de aplacado de piedra/ladrillo en tonos ocres (x≈225–560, y≈380–693).
   - Juego: Fachada beige lisa hasta el suelo.
227. [baja] Mobiliario — farol de pared de la izquierda
   - Captura: Farol de brazo en la fachada izquierda (x≈555–595, y≈170–220).
   - Juego: Sin farol en la izquierda (el juego pone uno a la derecha, x≈825–850, y≈283–300).
228. [baja] Mobiliario — señal de prohibido aparcar
   - Captura: Sin señal.
   - Juego: Señal de prohibido aparcar sobre poste en la acera derecha (x≈815–845, y≈330–475).

### Calle Castillejos

**Vista #22** — 02_Tramo_norte_hacia_la_iglesia.jpg (mayo de 2024) · hoja a_022.jpg

229. [alta] Cámara — encuadre de la vista
   - Captura: Calle Castillejos vista desde la calzada: local con escaparate y portal a la izquierda (x≈0–600), la calle hacia la iglesia al fondo (x≈600–800) y la mediana con arbolillos y un banco a la derecha (x≈680–1440).
   - Juego: La copa de un árbol pegada a la cámara tapa casi todo el encuadre (x≈150–1440, y≈0–693); solo se ve a la izquierda un edificio con toldo a rayas y un trozo de calzada (x≈0–280).
**Vista #23** — 03_Desde_la_iglesia_hacia_el_norte.jpg (mayo de 2024) · hoja a_023.jpg

230. [media] Huecos — puerta de la casa amarilla
   - Captura: Puerta con recercado de piedra (x≈1035–1095, y≈330–440).
   - Juego: Ventana con reja en esa posición (x≈1043–1108, y≈350–435).
231. [media] Cubierta — edificios blancos del fondo izquierdo
   - Captura: Edificio blanco de remate plano (x≈0–240, y≈250–275).
   - Juego: Casas blancas de una planta con tejado de teja naranja (x≈0–430, y≈255–340).
232. [media] Marcas viales — paso de peatones y línea de detención
   - Captura: Paso de peatones (x≈640–890, y≈420–445) y línea de detención (x≈805–905, y≈455–460).
   - Juego: Sin paso de peatones.
233. [media] Vegetación — zona ajardinada de la izquierda
   - Captura: Jardín con setos bajos continuos (x≈100–640, y≈330–380) y árboles frondosos grandes (x≈240–430 y x≈520–660, y≈220–360) detrás de los coches.
   - Juego: Explanada de arena amarilla sin setos, con árboles redondos sueltos (x≈80–200, x≈415–600, x≈610–690; y≈255–420).
234. [baja] Detalles de fachada — balcones del bloque alto del fondo
   - Captura: Frentes de balcón pintados de rojo oscuro en el bloque blanco (x≈800–840, y≈190–340).
   - Juego: Balcones blancos/grises (x≈760–925, y≈180–360).
235. [baja] Mobiliario — contenedores azules
   - Captura: Contenedores azules (x≈455–580, y≈385–445).
   - Juego: Sin contenedores.
236. [baja] Mobiliario — farol de la casa amarilla
   - Captura: Farol de brazo grande entre los balcones (x≈1110–1190, y≈150–230).
   - Juego: Farol pequeño junto al balcón, más a la izquierda y más bajo (x≈1020–1035, y≈275–295).
237. [baja] Vehículos — aparcamiento en batería de la izquierda
   - Captura: Fila de coches aparcados en batería (x≈0–460, y≈355–460).
   - Juego: Ningún coche; solo una carretilla y una persona.
**Vista #24** — 04_Acceso_desde_la_Cuesta.jpg (mayo de 2024) · hoja a_024.jpg

238. [media] Huecos — planta baja de la casa de la derecha
   - Captura: Paño blanco a la derecha del ventanal (x≈1230–1440, y≈280–450).
   - Juego: Gran puerta doble de madera con recercado crema (x≈1245–1440, y≈355–650).
239. [media] Detalles de fachada — recercados ocres de la casa de la derecha
   - Captura: Recercados pintados de ocre alrededor del balcón alto (x≈1065–1225, y≈20–260) y de la ventana baja (x≈1080–1230, y≈305–480), y franja ocre en la cornisa (x≈935–1180, y≈0–200).
   - Juego: Huecos sin recercado ocre salvo una ventana enrejada con marco amarillo (x≈1010–1085, y≈350–455).
240. [media] Cubierta — edificios blancos del fondo izquierdo
   - Captura: Edificios blancos de remate plano (x≈0–370, y≈260–300).
   - Juego: Casas blancas con tejado de teja naranja (x≈0–440, y≈265–340).
241. [media] Cubierta — remate de la casa de la derecha
   - Captura: Cornisa pintada de ocre, sin teja visible (x≈935–1180, y≈0–200).
   - Juego: Alero de teja naranja (x≈870–1200, y≈0–245).
242. [media] Vegetación — zona ajardinada de la izquierda
   - Captura: Árboles frondosos y setos tras el aparcamiento (x≈235–660, y≈265–360).
   - Juego: Explanada de arena con árboles redondos sueltos (x≈80–660, y≈285–395), sin setos.
243. [baja] Marcas viales — plaza de aparcamiento reservada
   - Captura: Plaza de aparcamiento pintada de azul con líneas blancas en primer plano (x≈0–450, y≈540–693).
   - Juego: Asfalto sin pintar.
244. [baja] Marcas viales — paso de peatones del fondo
   - Captura: Paso de peatones al fondo (x≈655–780, y≈380–390).
   - Juego: Sin paso de peatones.
245. [baja] Mobiliario — contenedores azules
   - Captura: Contenedores azules al fondo (x≈585–635, y≈362–390).
   - Juego: Sin contenedores.
246. [baja] Vehículos — aparcamiento en batería de la izquierda
   - Captura: Aparcamiento en batería lleno (x≈0–640, y≈345–600).
   - Juego: Sin coches.
**Vista #25** — 05_Tramo_central_hacia_el_norte.jpg (mayo de 2024) · hoja a_025.jpg

247. [alta] Geometría — mediana de la calle
   - Captura: Andén ancho de baldosas con arbolillos y bancos, a la izquierda de la cámara (bordes en x≈180 y x≈500 en el borde inferior, hasta x≈730 al fondo); la calzada de la derecha es de un solo carril (x≈500–1030 abajo).
   - Juego: Franja estrecha de adoquín justo delante de la cámara (x≈450–850 abajo, x≈670–780 al fondo), con calzadas a ambos lados; la de la derecha, ancha y con dos líneas (x≈850–1440).
248. [media] Huecos — local de la derecha
   - Captura: Gran escaparate acristalado del local (x≈1040–1440, y≈180–480).
   - Juego: Fachada residencial con balcones y una puerta doble de madera (x≈1245–1330, y≈355–485).
249. [media] Detalles de fachada — rótulos de la derecha
   - Captura: Rótulo azul y blanco «Centro de Formación Vial» (x≈985–1440, y≈60–250) y rótulo «Consultorex» (x≈1015–1230, y≈0–140).
   - Juego: Sin rótulos; un toldo a rayas verdes y blancas (x≈1185–1340, y≈155–230).
250. [media] Marcas viales — líneas de la calzada
   - Captura: Calzada derecha sin líneas; a la izquierda solo las líneas de las plazas de aparcamiento (x≈330–480, y≈470–490).
   - Juego: Líneas blancas continuas de borde a ambos lados de la mediana (x≈0–610, y≈390–590; x≈820–1240, y≈390–693) y otra línea en la calzada derecha.
251. [media] Vegetación — árbol de la mediana
   - Captura: Arbolillos jóvenes de tronco fino y copa pequeña (x≈640–720, y≈265–400).
   - Juego: Un árbol de copa redonda y densa (x≈610–810, y≈280–470).
252. [baja] Mobiliario — banco de la mediana
   - Captura: Banco en la mediana (x≈595–650, y≈405–455).
   - Juego: Sin banco en la mediana.
253. [baja] Mobiliario — farol de pared de la derecha
   - Captura: Farol de brazo en la fachada (x≈930–1005, y≈115–195).
   - Juego: Sin farol.
254. [baja] Vehículos — aparcamiento en batería de la izquierda
   - Captura: Coches aparcados en batería junto a las casas de la izquierda (x≈0–560, y≈340–440).
   - Juego: Sin coches.

### Calle Cañadilla

**Vista #26** — 02_Ramal_oeste_desde_Atras.jpg (mayo de 2024) · hoja a_026.jpg

255. [media] Geometría — altura de la casa larga de la izquierda
   - Captura: Casa más alta: la cornisa va de y≈130 a y≈300 a lo largo de la fachada (x≈340–585).
   - Juego: Casa más baja: el alero queda en y≈260–340 (x≈310–630) y por encima asoma otro edificio rosado (x≈390–595, y≈230–320).
256. [media] Geometría — edificio del fondo de la calle
   - Captura: Medianera alta gris-beige ciega cerrando el fondo (x≈695–760, y≈265–365).
   - Juego: Casa blanca de dos plantas con ventanas (x≈695–760, y≈295–375).
257. [media] Color de fachada — casa con balcones de la derecha (fondo)
   - Captura: Casa de color salmón/rosado (x≈785–830, y≈205–310).
   - Juego: Casa de ladrillo rojo anaranjado (x≈795–850, y≈185–410).
258. [media] Huecos — planta baja de la primera casa de la izquierda
   - Captura: Puerta metálica gris azulada con buzón verde al lado (x≈125–280, y≈355–580).
   - Juego: Ventana grande con marco blanco (x≈20–225, y≈365–600).
259. [media] Huecos — cochera de la casa cercana de la derecha
   - Captura: Gran portón de cochera de madera marrón (x≈1150–1440, y≈210–640).
   - Juego: Paño liso sin cochera (x≈1200–1440).
260. [media] Huecos — puerta de la casa cercana de la derecha
   - Captura: Puerta de madera marrón oscuro (x≈1030–1070, y≈295–510).
   - Juego: Ventana grande con marco blanco (x≈1050–1200, y≈350–540).
261. [media] Zócalo — zócalo de la casa larga de la izquierda
   - Captura: Zócalo gris de cemento (x≈340–590, y≈400–520).
   - Juego: Zócalo beige claro (x≈330–630, y≈440–550).
262. [media] Cubierta — remate de la casa larga de la izquierda
   - Captura: Cornisa moldurada recta, sin teja visible (x≈340–585).
   - Juego: Alero de teja naranja festoneado (x≈310–630, y≈260–340).
263. [baja] Detalles de fachada — paño pintado sobre la puerta de la izquierda
   - Captura: Paño pintado de color terracota sobre la puerta (x≈125–280, y≈200–350).
   - Juego: Fachada beige sin paño de color.
264. [baja] Acera y bordillo — pavimento de las aceras
   - Captura: Aceras de baldosa gris con parches de baldosa roja (x≈480–560, y≈450–470; x≈810–870, y≈420–445).
   - Juego: Aceras de baldosa clara uniforme.
265. [baja] Vegetación — macetas de las aceras
   - Captura: Aceras sin macetas.
   - Juego: Macetas con flores en ambas aceras (x≈505–565, y≈405–455; x≈805–835, y≈395–425).
266. [baja] Mobiliario — farol de pared de la izquierda
   - Captura: Farol de brazo grande en la esquina (x≈320–400, y≈65–175).
   - Juego: Sin farol; en su lugar asoma un toldo naranja (x≈300–410, y≈0–60).
267. [baja] Mobiliario — farola de la acera derecha
   - Captura: Sin farola en la acera derecha.
   - Juego: Farola de báculo moderna en la acera derecha (x≈795–920, y≈90–545).
**Vista #27** — 03_Acceso_norte_hacia_el_sur.jpg (mayo de 2024) · hoja a_027.jpg

268. [media] Huecos — ventana de la primera casa de la izquierda
   - Captura: Ventanal con reja blanca de forja ornamental y recercado de piedra gris (x≈200–370, y≈275–600).
   - Juego: Persiana de cochera blanca (x≈0–130, y≈310–693) y ventana con reja de barrotes rectos (x≈335–440, y≈350–525).
269. [media] Huecos — planta alta de la primera casa de la izquierda
   - Captura: Balcón con barandilla (x≈300–420, y≈0–160).
   - Juego: Ventana con reja de barrotes (x≈335–440, y≈15–230).
270. [media] Huecos — planta baja de la casa rosa (tramo lejano)
   - Captura: Escaparate con recercado moldurado en arco (x≈885–950, y≈310–450) y ventana pequeña (x≈825–855).
   - Juego: Puerta de madera (x≈878–942, y≈350–500) y ventana (x≈815–835).
271. [media] Huecos — planta alta de la casa rosa
   - Captura: Ventanas pequeñas con recercado moldurado, sin balcón (x≈820–860, y≈200–250; x≈905–995, y≈60–175).
   - Juego: Balcón con barandilla (x≈848–948, y≈210–310).
272. [media] Huecos — tramo cercano de la casa rosa
   - Captura: Paño rosa sin huecos con cables, contador (x≈1095–1150, y≈405–465) y bajante (x≈1335–1385).
   - Juego: Ventanal con persiana blanca (x≈1125–1440, y≈350–660) y otro ventanal arriba (x≈1125–1440, y≈0–145).
273. [media] Zócalo — zócalo de la casa rosa
   - Captura: Zócalo de piedra gris (x≈810–1440, y≈400–680).
   - Juego: Zócalo marrón-beige (x≈940–1440, y≈470–693).
274. [baja] Detalles de fachada — placas de nombre de calle
   - Captura: No se ven placas en esas posiciones.
   - Juego: Placas «CALLE CAÑADILLA» en ambas fachadas (x≈145–275, y≈275–315; x≈1005–1085, y≈300–320).
275. [baja] Vegetación — plantas de la acera izquierda
   - Captura: Acera sin plantas.
   - Juego: Matas con flores y una maceta (x≈350–500, y≈510–590; x≈580–605, y≈405–425).
276. [baja] Vegetación — árbol al fondo de la calle
   - Captura: Sin árbol al fondo (casas blancas).
   - Juego: Árbol redondo al fondo (x≈700–745, y≈310–345).
277. [baja] Mobiliario — señal del primer plano izquierdo
   - Captura: Señal circular sobre poste en primer plano (x≈120–280, y≈210–600).
   - Juego: Sin señal.
278. [baja] Mobiliario — farol de pared de la izquierda
   - Captura: Farol más al fondo (x≈550–600, y≈175–230).
   - Juego: Farol en la primera casa, en primer plano (x≈260–380, y≈120–220).
**Vista #28** — 04_Acceso_sur_hacia_el_norte.jpg (mayo de 2024) · hoja a_028.jpg

279. [media] Geometría — posición del edificio de la farmacia
   - Captura: Fachada de la farmacia cercana, junto a la acera (x≈715–1440, y≈0–500), con los balcones en la parte alta del encuadre.
   - Juego: Edificio más lejano y más pequeño (x≈700–1440, y≈120–465) con una explanada amplia de losas delante (x≈630–1440, y≈365–693).
280. [media] Huecos — casa de la izquierda
   - Captura: Medianera blanca ciega, sin huecos (x≈0–485, y≈0–620).
   - Juego: Ventanas (x≈275–340, y≈100–240; x≈410–440, y≈355–420) y una puerta (x≈270–335, y≈360–530).
281. [media] Huecos — planta alta de la farmacia
   - Captura: Balcones con barandilla de forja y puertas de madera (x≈795–875, y≈130–240; x≈1000–1115, y≈105–225; x≈1285–1440, y≈65–205).
   - Juego: Ventanas pequeñas con persiana y macetas, sin balcones salientes (x≈735–1440, y≈205–320).
282. [media] Huecos — planta baja de la farmacia
   - Captura: Entrada de la farmacia con cancelas de hierro abiertas (x≈970–1150, y≈320–490) entre ventanas enrejadas (x≈800–865; x≈1295–1420).
   - Juego: Puerta de cochera (x≈968–1095, y≈340–405), ventanas enrejadas y una puerta (x≈740–785).
283. [media] Detalles de fachada — letrero y cruz de la farmacia
   - Captura: Letras «FARMACIA» en la fachada (x≈880–1285, y≈255–305) y cruz verde luminosa en la esquina (x≈670–735, y≈85–160).
   - Juego: Sin letrero ni cruz.
284. [media] Cubierta — casa de la izquierda
   - Captura: Borde recto del muro, sin teja (x≈390–485, y≈0–175).
   - Juego: Alero de teja naranja (x≈240–475, y≈0–205).
285. [media] Marcas viales — paso de peatones
   - Captura: Paso de peatones de franjas blancas en primer plano (x≈450–740, y≈520–693).
   - Juego: Sin paso de peatones.
286. [baja] Marcas viales — plaza de aparcamiento reservada
   - Captura: Plaza pintada de azul delante de la farmacia (x≈950–1440, y≈530–693).
   - Juego: Losas claras sin pintar.
287. [baja] Acera y bordillo — pavimento de las aceras de la esquina
   - Captura: Franjas de baldosa roja en las aceras (x≈200–470, y≈540–693; x≈690–850, y≈455–693).
   - Juego: Losas claras uniformes.
288. [baja] Vegetación — plantas en la puerta de la izquierda
   - Captura: Sin plantas.
   - Juego: Cactus y macetas con flores junto a la puerta (x≈180–285, y≈515–625).
289. [baja] Mobiliario — señal de aparcamiento reservado
   - Captura: Señal azul de minusválidos sobre poste (x≈918–968, y≈320–530).
   - Juego: Sin señal.
290. [baja] Mobiliario — farol de la esquina de la farmacia
   - Captura: Farol de pared en la esquina (x≈690–715, y≈255–285).
   - Juego: Sin farol.

### Calle Cuatro Esquinas

**Vista #29** — 02_Acceso_desde_la_iglesia.jpg (mayo de 2024) · hoja a_029.jpg

291. [media] Color de fachada — parte alta de la casa de la izquierda
   - Captura: Planta alta de la casa de la izquierda pintada de ocre claro con desconchones (x≈350–490, y≈0–250).
   - Juego: Fachada blanca en toda su altura.
292. [media] Huecos — planta baja de la casa amarilla
   - Captura: Secuencia puerta (x≈905–970) – ventana enrejada (x≈1060–1140) – ventana enrejada (x≈1180–1270) – puerta (x≈1385–1440), y≈340–440.
   - Juego: Secuencia ventana enrejada (x≈810–878) – ventana enrejada (x≈968–1048) – puerta (x≈1155–1258) – ventana enrejada (x≈1390–1440), y≈345–475.
293. [media] Cubierta — alero de la casa amarilla
   - Captura: Alero de teja árabe corrido con cornisa blanca (x≈755–1440, y≈130–210).
   - Juego: Remate recto sin teja (x≈760–1440, y≈75–150).
294. [media] Marcas viales — paso de peatones
   - Captura: Paso de peatones de franjas blancas en primer plano, con una pintada en el asfalto (x≈470–1010, y≈470–693).
   - Juego: Sin paso de peatones ni marcas.
295. [baja] Acera y bordillo — acera roja de la esquina izquierda
   - Captura: Tramo de acera de baldosa roja en la esquina (x≈400–600, y≈510–590).
   - Juego: Sin baldosa roja: suelo claro continuo.
296. [baja] Mobiliario — bolardos del cruce
   - Captura: Bolardos bajos en el cruce (x≈705–715, y≈455–475).
   - Juego: Sin bolardos.
297. [baja] Mobiliario — farol de la esquina de la casa amarilla
   - Captura: Farol en la esquina izquierda de la casa amarilla (x≈740–750, y≈280–305).
   - Juego: Sin farol en la esquina; el juego pone uno en mitad de la fachada, junto a un balcón (x≈1140–1190, y≈255–290).
**Vista #30** — 03_Cruce_con_Manuel_Dorado_y_Matasanos.jpg (mayo de 2024) · hoja a_030.jpg

298. [alta] Geometría — edificio de la esquina derecha
   - Captura: Fachada de la casa de la derecha casi de frente a la cámara y cercana (x≈740–1440), con la esquina en x≈740; tras ella no se ve ninguna calle.
   - Juego: La casa de la derecha es una fachada larga que se aleja a lo largo de la calle del fondo (x≈620–1090), con la esquina en x≈1090; a su derecha se abre otra calle con un edificio de sillería al fondo (x≈1285–1440, y≈185–375).
299. [media] Huecos — cochera de la casa blanca de la izquierda (fondo)
   - Captura: Persiana de cochera de madera marrón (x≈370–450, y≈315–390).
   - Juego: Puerta de cochera blanca (x≈380–450, y≈335–480).
300. [media] Huecos — ventana de la casa de la izquierda (primer plano)
   - Captura: Ventanal grande con reja de forja y contraventana de madera detrás (x≈20–260, y≈170–530).
   - Juego: Ventanas pequeñas con persiana marrón y jardinera (x≈260–330, y≈90–230 y y≈360–480) y solo un trozo de reja en el borde (x≈0–50).
301. [media] Zócalo — zócalo de la casa de la derecha
   - Captura: Zócalo de sillarejo de piedra arenisca (x≈745–1000, y≈490–693).
   - Juego: Zócalo liso pintado de ocre anaranjado (x≈690–1285, y≈420–690).
302. [media] Calzada — suelo de la calle del fondo
   - Captura: Pavimento claro de losas/hormigón en toda la calle, sin bordillos (x≈370–740, y≈400–693).
   - Juego: Calzada de asfalto gris oscuro con grieta y aceras con bordillo blanco (x≈230–760, y≈370–693).
303. [baja] Mobiliario — señal de dirección prohibida
   - Captura: Sin señal.
   - Juego: Señal de dirección prohibida grande en primer plano (x≈1075–1200, y≈250–693).
304. [baja] Mobiliario — bolardos del cruce
   - Captura: Bolardos bajos en el cruce (x≈425–465, y≈430–470; x≈655–675, y≈420–460).
   - Juego: Sin bolardos.
**Vista #31** — 04_Referencia_del_Ayuntamiento_desde_Grande.jpg (marzo de 2009) · hoja a_031.jpg

305. [alta] Color de fachada — edificio del fondo de la plaza
   - Captura: Edificio blanco al fondo (x≈590–640, y≈285–365).
   - Juego: Edificio amarillo ocre (x≈575–640, y≈310–365).
306. [media] Color de fachada — fachada del Ayuntamiento hacia la calle Grande
   - Captura: Fachada blanca con arcos (x≈690–780, y≈215–400).
   - Juego: Sillería beige almohadillada (x≈680–830, y≈180–380).
307. [media] Cubierta — remate del edificio blanco de la derecha
   - Captura: Cornisa moldurada blanca, sin teja (x≈780–1000, y≈0–130).
   - Juego: Alero de teja naranja (x≈785–1120, y≈0–255).
308. [media] Marcas viales — paso de peatones
   - Captura: Paso de peatones en la calle Grande (x≈505–650, y≈450–500).
   - Juego: Sin paso de peatones.
309. [media] Vegetación — naranjo de la acera derecha
   - Captura: Naranjo grande en la acera derecha, con la copa de x≈890 a x≈1300 y del borde superior a y≈620.
   - Juego: No hay árbol en la acera derecha (x≈890–1300).
310. [media] Vegetación — árboles de la plaza
   - Captura: Árboles altos de tronco limpio y copa ancha en la plaza (x≈400–600, y≈210–440; x≈325–400, y≈250–370).
   - Juego: Dos arbustos redondos bajos (x≈305–370, y≈310–400; x≈370–510, y≈320–445).
311. [baja] Detalles de fachada — cruz de farmacia en la fachada derecha
   - Captura: Cruz verde luminosa de farmacia en la fachada (x≈1265–1440, y≈115–265).
   - Juego: Sin cruz; ventana con contraventanas marrones (x≈1270–1410, y≈0–155).
312. [baja] Vegetación — seto de la plaza
   - Captura: Seto bajo (x≈390–545, y≈395–420).
   - Juego: Sin seto.
313. [baja] Mobiliario — contenedores verdes
   - Captura: Contenedores verdes junto a la plaza (x≈535–600, y≈390–450).
   - Juego: Sin contenedores.
314. [baja] Mobiliario — farol de la casa de ladrillo
   - Captura: Farol de brazo en la esquina de la casa de ladrillo de la izquierda (x≈325–395, y≈145–210).
   - Juego: Sin farol.

### Calle de Don Juan Durán

**Vista #32** — 02_Desde_Plaza_la_Parada_hacia_Malfeitos.jpg (mayo de 2024) · hoja a_032.jpg

315. [media] Color de fachada — casa rosa de la izquierda
   - Captura: Rosa salmón intenso (≈ RGB 224,173,154) (x≈0–530).
   - Juego: Rosa melocotón pálido (≈ RGB 226,197,180) (x≈0–520).
316. [media] Color de fachada — casa vieja del borde derecho
   - Captura: Fachada ocre/parda desconchada (x≈1240–1440, y≈0–693).
   - Juego: Fachada blanca grisácea (x≈1240–1440).
317. [media] Huecos — ventanal de la casa rosa (primer plano)
   - Captura: Ventanal con gran reja de forja ornamental (x≈0–290, y≈200–620).
   - Juego: Ventana con persiana enrollable blanca y macetas con flores, sin reja (x≈0–165, y≈300–560).
318. [media] Huecos — segundo hueco de la planta baja de la casa rosa
   - Captura: Ventana alta con reja (x≈440–505, y≈255–455).
   - Juego: Puerta de madera (x≈425–475, y≈330–490).
319. [media] Huecos — balcón de la casa rosa
   - Captura: Balcón con barandilla de hierro negro sobre ménsula moldurada (x≈425–530, y≈55–200).
   - Juego: Balcón con barandilla blanca (x≈410–525, y≈170–290).
320. [media] Huecos — puerta de la casa blanca de la derecha
   - Captura: Puerta de madera con arco de medio punto (x≈880–920, y≈300–450).
   - Juego: Puerta de madera de dintel recto (x≈865–905, y≈335–440).
321. [media] Zócalo — zócalo de la casa rosa
   - Captura: Parte baja blanca/crema clara (≈ RGB 235,209,192) (x≈280–530, y≈450–550).
   - Juego: Zócalo beige grisáceo más oscuro (≈ RGB 187,176,161) (x≈0–520, y≈450–693).
**Vista #33** — 03_Desde_Malfeitos_hacia_Plaza_la_Parada.jpg (mayo de 2024) · hoja a_033.jpg

322. [media] Color de fachada — casa de la izquierda (primer plano)
   - Captura: Amarillo pálido (x≈0–520).
   - Juego: Beige arena grisáceo (x≈0–565).
323. [media] Huecos — planta baja de la casa de la izquierda
   - Captura: Ventanal con reja de forja y recercado blanco (x≈60–300, y≈300–565).
   - Juego: Puerta doble de cochera de madera con ventanillos (x≈0–235, y≈320–580).
324. [media] Huecos — puerta de la casa blanca de la derecha
   - Captura: Puerta de madera con recercado (x≈1020–1070, y≈305–465).
   - Juego: Cochera con persiana de madera y parte baja negra (x≈975–1060, y≈320–495).
325. [media] Huecos — balcón de la casa blanca de la derecha
   - Captura: Balcón con barandilla y un estandarte colgado (x≈980–1075, y≈155–255).
   - Juego: Ventana con contraventanas marrones, sin balcón (x≈950–1105, y≈35–240).
326. [media] Huecos — planta alta del extremo derecho
   - Captura: Balcón con barandilla de forja (x≈1265–1440, y≈0–130).
   - Juego: Ventana con contraventana marrón, sin balcón (x≈1225–1395, y≈0–100).
327. [media] Detalles de fachada — relieve de la fachada de la izquierda
   - Captura: Fachada con relieve decorativo de hexágonos (x≈0–520, y≈220–470).
   - Juego: Fachada lisa.

### Calle de la Cuesta

**Vista #34** — 02_Acceso_oeste_hacia_la_iglesia.jpg (mayo de 2024) · hoja a_034.jpg

328. [media] Geometría — volumen del edificio azul oscuro
   - Captura: Borde izquierdo vertical en x≈325–330; a su izquierda la pared es blanca.
   - Juego: El edificio azul oscuro se extiende hacia la izquierda por encima de la casa blanca con un hastial (x≈55–390, y≈0–300).
329. [media] Geometría — edificio del fondo de la calle
   - Captura: Casas blancas bajas con tejado (x≈780–880, y≈305–340).
   - Juego: Bloque blanco de tres plantas con remate plano (x≈815–895, y≈300–370).
330. [media] Huecos — cochera de la casa blanca de la izquierda
   - Captura: Gran portón de cochera marrón (x≈0–295, y≈265–600).
   - Juego: Ventana con persiana enrollable blanca (x≈0–215, y≈365–580).
331. [media] Huecos — planta alta del edificio azul oscuro
   - Captura: Ventanales anchos apaisados con carpintería blanca (x≈390–525, y≈100–270; x≈550–605, y≈200–290).
   - Juego: Ventanas pequeñas verticales con marco verde claro y persiana (x≈425–505, y≈120–260; x≈560–595, y≈210–285; x≈620–640, y≈250–300).
332. [media] Huecos — planta baja del edificio azul oscuro
   - Captura: Dos puertas de cochera blancas (x≈395–515, y≈300–455) y una puerta acristalada (x≈555–590, y≈315–390).
   - Juego: Ventana (x≈425–505, y≈345–465), puerta (x≈560–595, y≈350–455) y ventanuco (x≈620–640, y≈345–400); sin cocheras.
333. [media] Detalles de fachada — pilastras y bandas verde lima
   - Captura: Pilastras verde lima en planta baja (x≈510–525 y x≈590–610, y≈300–440) y tabla verde bajo el alero.
   - Juego: Sin elementos verde lima; solo marcos de ventana verde claro.
334. [media] Cubierta — casa blanca de la izquierda
   - Captura: Bajo el panel de Street View se ve pared blanca, sin alero (x≈0–330, y≈215–265).
   - Juego: Alero de teja naranja festoneado cruzando esa zona (x≈0–390, y≈165–300).
335. [media] Cubierta — tejado del edificio azul oscuro
   - Captura: Alero de teja rojiza con tabla verde lima (x≈330–625, y≈30–225).
   - Juego: Tejado a dos aguas gris pizarra oscuro (x≈55–685, y≈0–240).
336. [media] Vegetación — arboleda tras la tapia
   - Captura: Hilera continua de árboles tras la tapia (x≈880–1440, y≈290–340).
   - Juego: Dos palmeras (x≈1160–1225, y≈260–330) y un árbol redondo (x≈950–1010, y≈320–345).
337. [media] Muros y vallas — tapia de la derecha
   - Captura: Tapia de tierra/mampostería ocre de textura irregular con albardilla (x≈780–1440, y≈335–693).
   - Juego: Muro de ladrillo naranja en hiladas regulares (x≈855–1440, y≈335–693).
338. [baja] Mobiliario — placa de vado
   - Captura: Placa de vado en el portón (x≈155–205, y≈345–390).
   - Juego: Sin placa.
339. [baja] Mobiliario — farol del edificio azul oscuro
   - Captura: Sin farol en la fachada.
   - Juego: Farol de brazo en la fachada (x≈425–480, y≈220–270).
**Vista #35** — 03_Extremo_este_hacia_el_oeste.jpg (mayo de 2024) · hoja a_035.jpg

340. [media] Huecos — ventana enrejada de la casa de la izquierda
   - Captura: Paño liso con desconchones, sin ventana (x≈365–495, y≈350–495).
   - Juego: Ventana con reja (x≈365–495, y≈350–495).
341. [media] Zócalo — zócalo de la casa de la izquierda
   - Captura: Zócalo gris de cemento (x≈170–700, y≈430–600).
   - Juego: Zócalo beige de sillares (x≈0–700, y≈470–693).
342. [media] Cubierta — casas del fondo de la calle
   - Captura: Casas del fondo con remate plano (x≈770–1025, y≈270–295).
   - Juego: Tejados de teja naranja (x≈735–1030, y≈285–300).
343. [media] Vegetación — árbol junto a la iglesia
   - Captura: Arbusto pequeño junto al pedestal (x≈1050–1140, y≈230–310).
   - Juego: Árbol grande de tronco anaranjado cuya copa llega al borde superior (x≈895–1340, y≈0–395).
344. [media] Vegetación — tronco del primer plano derecho
   - Captura: Sin árbol: verja y muro (x≈1355–1440, y≈310–500).
   - Juego: Tronco grueso de árbol (x≈1355–1440, y≈310–500).
345. [media] Mobiliario — pedestal de piedra junto a la iglesia
   - Captura: Pedestal alto de piedra con columna junto a la iglesia (x≈1100–1225, y≈115–345).
   - Juego: Sin pedestal.
346. [media] Mobiliario — farola junto a la iglesia
   - Captura: Farola de fundición gris con dos faroles (x≈1165–1340, y≈115–335).
   - Juego: Farola moderna negra de báculo con dos brazos (x≈1200–1440, y≈180–520).
347. [media] Muros y vallas — verja del atrio
   - Captura: Verja de hierro con aspas en X a lo largo de todo el murete (x≈790–1440, y≈330–400).
   - Juego: Verja de barrotes verticales en el tramo cercano (x≈995–1440, y≈385–570); aspas solo al fondo (x≈830–970).
348. [baja] Mobiliario — señal de dirección prohibida
   - Captura: Señal de dirección prohibida en la fachada izquierda (x≈0–175, y≈265–370).
   - Juego: Sin señal.
349. [baja] Mobiliario — farol en el balcón de la izquierda
   - Captura: Sin farol.
   - Juego: Farol colgado en el balcón (x≈430–460, y≈210–260).
350. [baja] Mobiliario — contenedor verde
   - Captura: Contenedor verde junto al atrio (x≈785–805, y≈360–385).
   - Juego: Sin contenedor.
**Vista #36** — 04_Ramal_sur_y_union_con_la_calle_principal.jpg (mayo de 2024) · hoja a_036.jpg

351. [alta] Geometría — casa de la izquierda en primer plano
   - Captura: Fachada que se aleja desde el borde izquierdo (x≈0–620), con el balcón en x≈375–495 (y≈80–215) y la ventana enrejada en x≈395–480.
   - Juego: Volumen pegado a la cámara: un balcón enorme (x≈0–550, y≈0–215), una barandilla (x≈0–390, y≈370–693) y una pared (x≈0–515) ocupan toda la izquierda.
352. [alta] Color de fachada — casa de la izquierda en primer plano
   - Captura: Fachada crema clara (x≈0–620).
   - Juego: Fachada rojo anaranjado (x≈0–515).
353. [media] Huecos — puerta de la casa de la derecha
   - Captura: Puerta de madera con recercado de ladrillo (x≈925–1040, y≈225–460).
   - Juego: Puerta con cortina de tiras verdes y recercado blanco (x≈920–975, y≈345–465).
354. [media] Huecos — planta alta de la casa de la derecha
   - Captura: Ventana con reja y marco gris, sin balcón (x≈945–1005, y≈75–235).
   - Juego: Balcón con barandilla y macetas (x≈900–975, y≈255–315).
355. [media] Huecos — ventana del borde derecho
   - Captura: Ventana con reja oscura (x≈1310–1440, y≈335–630).
   - Juego: Paño liso (x≈1310–1440, y≈335–630).
356. [media] Zócalo — parte baja de la casa de la izquierda
   - Captura: Parte baja blanca (x≈260–620, y≈400–600).
   - Juego: Zócalo de azulejo beige (x≈530–700, y≈420–693).
357. [media] Zócalo — zócalo de la casa de la derecha
   - Captura: Aplacado de ladrillo/piedra marrón (x≈820–1440, y≈370–693).
   - Juego: Banda lisa beige-marrón (x≈975–1440, y≈420–693).
358. [baja] Mobiliario — señal de estacionamiento prohibido de la izquierda
   - Captura: Señal con placa de fechas sobre poste (x≈170–315, y≈265–693).
   - Juego: Sin señal.
359. [baja] Mobiliario — señal de estacionamiento prohibido de la derecha
   - Captura: Señal con placa de fechas sobre poste (x≈1060–1150, y≈240–355).
   - Juego: Sin señal.
360. [baja] Mobiliario — farol de la izquierda
   - Captura: Sin farol en x≈625–695.
   - Juego: Farol de brazo (x≈625–695, y≈180–245).
**Vista #37** — 05_Tramo_central_y_cruce_con_Bronca.jpg (mayo de 2024) · hoja a_037.jpg

361. [media] Huecos — ventanal de la casa de la izquierda
   - Captura: Ventanal con reja de forja ornamental (x≈0–215, y≈230–510).
   - Juego: Ventana con marco blanco, sin reja (x≈0–160, y≈410–693).
362. [media] Huecos — puerta del n.º 18
   - Captura: Puerta doble blanca (x≈440–515, y≈265–470).
   - Juego: Ventana con reja (x≈515–610, y≈355–550) y balcón encima (x≈495–640, y≈110–300); no hay puerta.
363. [media] Huecos — puerta de la segunda casa de la izquierda
   - Captura: Puerta de madera marrón (x≈560–585, y≈275–405).
   - Juego: Puerta verde (x≈645–675, y≈345–470).
364. [media] Huecos — puerta de forja de la derecha
   - Captura: Puerta de hierro forjado con recercado de piedra (x≈1050–1170, y≈310–500).
   - Juego: Ventana con persiana enrollable (x≈1095–1190, y≈345–445).
365. [media] Huecos — planta alta de la casa de la derecha
   - Captura: Ventana con persiana y recercado (x≈1200–1360, y≈30–200), sin balcón.
   - Juego: Balcón con barandilla (x≈1340–1440, y≈165–290) y ventana con persiana (x≈1095–1190, y≈160–275).
366. [media] Detalles de fachada — recercados de piedra de la casa de la izquierda
   - Captura: Aplacado de piedra gris alrededor del ventanal (x≈0–250, y≈210–520) y de la puerta (x≈425–535, y≈250–480).
   - Juego: Recercado blanco liso (x≈0–300, y≈330–693).
367. [media] Zócalo — zócalo de la casa de la izquierda
   - Captura: Zócalo de aplacado de piedra gris (x≈0–430, y≈470–693).
   - Juego: Fachada blanca hasta abajo en x≈0–300 y zócalo beige liso desde x≈300.
368. [media] Zócalo — zócalo de las casas de la derecha
   - Captura: Aplacado de piedra marrón grisácea (x≈905–1440, y≈380–600).
   - Juego: Banda lisa beige-marrón (x≈870–1410, y≈370–560).
369. [media] Acera y bordillo — acera izquierda elevada
   - Captura: Acera izquierda elevada sobre la calzada con bordillo alto (x≈420–735, y≈340–600).
   - Juego: Acera a altura normal con bordillo bajo blanco.
370. [media] Muros y vallas — barandilla de la acera izquierda
   - Captura: Barandilla de tubo metálico a lo largo de la acera izquierda (x≈200–735, y≈340–693).
   - Juego: Sin barandilla.
371. [baja] Detalles de fachada — recercados rosados de la derecha
   - Captura: Recercados rosa salmón en las ventanas (x≈1200–1360, y≈30–200; x≈995–1035, y≈170–260; x≈935–960, y≈220–310).
   - Juego: Recercados blancos.

### Calle de Santa María

**Vista #38** — 02_Acceso_sur_y_fachada_de_la_iglesia.jpg (mayo de 2024) · hoja a_038.jpg

372. [alta] Color de fachada — casas del fondo a la izquierda
   - Captura: Fachadas blancas encaladas, x≈640–700, y≈250–390 (fondo, izquierda).
   - Juego: Fachadas color ladrillo/naranja, x≈655–700, y≈250–385.
373. [alta] Vegetación — árbol grande del atrio (derecha)
   - Captura: Árbol grande de copa verde oscura y densa delante del muro de la iglesia, x≈870–1440, y≈50–450, con el tronco inclinado en x≈1190–1240 (medio, derecha).
   - Juego: No hay ningún árbol: en esa zona se ve el muro de la iglesia entero hasta el suelo (x≈830–1440).
374. [alta] Muros y vallas — cerramiento del atrio de la iglesia (lado derecho de la calle)
   - Captura: Murete de granito a lo largo de todo el borde derecho de la calzada, coronado por una verja de hierro de aspas color óxido y con pilares de granito (x≈865–895 y x≈1040–1145); el atrio queda más alto que la calle. Recorre x≈800–1440, y≈370–693 (primer plano y medio, derecha).
   - Juego: No hay murete ni verja junto a la calzada: solo un bordillo blanco redondeado en diagonal (x≈880–1250, y≈490–693) y el suelo del atrio al nivel de la acera; únicamente un tramo corto de barandilla negra sobre un murete, retranqueado, en el borde derecho (x≈1360–1440, y≈405–560).
375. [media] Geometría — edificio que cierra la calle al fondo
   - Captura: Edificio de 3 plantas, blanco, con balcones, x≈705–775, y≈298–350 (fondo, centro).
   - Juego: Edificio bajo amarillo, x≈700–760, y≈300–360.
376. [media] Huecos — ventanas pequeñas del muro de la iglesia
   - Captura: Dos ventanitas: una cuadrada con reja en x≈888–912, y≈180–205 y otra pequeña de medio punto en x≈865–885, y≈268–302.
   - Juego: Muro ciego, sin ningún hueco, en x≈775–1440.
377. [media] Huecos — ventana grande con reja de la primera casa de la izquierda
   - Captura: Ventana grande con reja de forja negra abombada (barrotes con nudos) dentro de un recercado rehundido color crema, x≈130–400, y≈230–690 (primer plano, izquierda).
   - Juego: Pared lisa blanca sin ningún hueco en esa zona (x≈40–430); solo un panel claro estrecho en el borde, x≈0–40, y≈360–693.
378. [media] Huecos — puerta y reja de la segunda casa de la izquierda
   - Captura: Puerta de madera marrón de dos hojas con recercado crema de arco rebajado, x≈540–590, y≈290–465, y ventana alta con reja negra, x≈608–630, y≈320–425.
   - Juego: En ese tramo (x≈540–640) solo pared blanca con ventanitas de marco blanco (x≈592–612, y≈205–275 y y≈352–410) y un bajante; ni puerta de madera ni reja.
379. [media] Huecos — balcón de la izquierda
   - Captura: Un solo balcón, en la segunda casa, con barandilla de forja negra abombada, x≈535–610, y≈165–270; la primera casa no tiene balcón.
   - Juego: El balcón está más cerca, sobre la primera casa (x≈430–572, y≈160–305), con barandilla recta sobre una losa blanca gruesa y una ventana con persiana blanca encima (x≈455–520, y≈70–180).
380. [media] Detalles de fachada — aparejo del muro de la iglesia (derecha)
   - Captura: Mampostería irregular: piedras de tamaños y formas distintas con mucho mortero, tonos ocre y gris, con sillares en la esquina (x≈775–800); x≈775–1440, y≈0–400.
   - Juego: Hiladas regulares de bloques rectangulares redondeados casi iguales, alineados como ladrillos grandes, en beige, gris, marrón y naranja; x≈775–1440, y≈0–500.
381. [media] Detalles de fachada — imposta horizontal del muro de la iglesia
   - Captura: Moldura de piedra horizontal saliente que cruza el muro, x≈775–1010, y≈95–120.
   - Juego: El muro no tiene ninguna moldura horizontal; las hiladas siguen sin interrupción (x≈775–1440, y≈0–500).
382. [media] Cubierta — alero de las casas de la izquierda
   - Captura: El remate de las fachadas de la izquierda se ve como una cornisa blanca lisa, sin tejas visibles (x≈520–700, y≈0–300).
   - Juego: Hilera de tejas rojo-anaranjadas muy visible a lo largo de todo el alero izquierdo, x≈470–700, y≈0–300.
383. [media] Acera y bordillo — suelo del atrio (derecha)
   - Captura: Enlosado de lanchas de piedra irregulares gris-ocre, x≈900–1440, y≈400–693.
   - Juego: Baldosas cuadradas regulares gris claro, x≈880–1440, y≈490–693.
384. [media] Acera y bordillo — acera izquierda
   - Captura: Acera gris clara de aproximadamente 1 m con bordillo a lo largo de las casas de la izquierda, x≈330–700, y≈365–693.
   - Juego: No hay acera a la izquierda: el asfalto llega directamente al zócalo de las casas (x≈350–700, y≈365–693).
385. [baja] Detalles de fachada — bajante entre la primera y la segunda casa de la izquierda
   - Captura: Sin bajante visible en el encuentro de las dos casas (x≈540).
   - Juego: Bajante blanco vertical, x≈565–580, y≈130–490.
386. [baja] Vegetación — árboles al final de la calle
   - Captura: No se ven árboles al fondo de la calle (x≈700–775).
   - Juego: Árboles de copa redonda verde delante del edificio del fondo, x≈720–775, y≈300–345.
387. [baja] Mobiliario — banco de piedra del atrio
   - Captura: Banco de piedra en el atrio, x≈1035–1090, y≈405–425 (medio, derecha).
   - Juego: No hay banco en el atrio.
388. [baja] Mobiliario — farol de pared junto al balcón
   - Captura: Farol de forja colgado de la fachada izquierda, x≈612–640, y≈178–230.
   - Juego: No hay farol en las fachadas de la izquierda.
389. [baja] Otros — cables aéreos
   - Captura: Cables negros grapados a lo largo de las fachadas de la izquierda (y≈130–260) y uno que cruza la calle en x≈670–780, y≈210–235.
   - Juego: Sin cables.
**Vista #39** — 03_Desde_el_extremo_norte_hacia_la_Cuesta.jpg (mayo de 2024) · hoja a_039.jpg

390. [media] Color de fachada — casa del primer plano derecho
   - Captura: Fachada crema/amarillo muy pálido, x≈955–1440, y≈0–450.
   - Juego: Fachada ocre-mostaza saturada, x≈935–1440, y≈0–540.
391. [media] Color de fachada — segunda casa de la derecha
   - Captura: Fachada crema rosada pálida, x≈830–955, y≈240–380.
   - Juego: Fachada salmón/naranja más saturada, x≈820–935, y≈235–415.
392. [media] Huecos — ventana sobre la portada lateral de la iglesia
   - Captura: Ventana alta y estrecha de medio punto con moldura, sobre la portada, x≈700–722, y≈85–165.
   - Juego: Rosetón circular calado en x≈680–720, y≈60–165.
393. [media] Huecos — planta baja de la casa del primer plano derecho
   - Captura: Puerta de madera marrón con recercado gris en x≈1065–1135, y≈335–395 y ventana grande con reja negra en x≈1280–1415, y≈340–440.
   - Juego: Posiciones cambiadas: ventana con reja negra en x≈1050–1125, y≈350–440 y puerta de madera con marco blanco en x≈1270–1440, y≈340–580.
394. [media] Huecos — balcones de la planta alta (derecha)
   - Captura: Tres balcones con barandilla negra: x≈975–1025, x≈1050–1135 y x≈1240–1440 (y≈150–310).
   - Juego: Dos balcones: x≈935–995 (y≈280–320) y x≈1230–1440 (y≈150–300); donde está el central de la captura hay un farol (x≈1135–1195).
395. [media] Detalles de fachada — aparejo de los muros de la iglesia (izquierda)
   - Captura: Mampostería irregular rosada-ocre con mucho mortero en los paños y sillares grandes de granito bien escuadrados en las esquinas (esquina del contrafuerte en x≈420–500); x≈0–760, y≈0–520.
   - Juego: Todos los paños y esquinas con el mismo aparejo de hiladas regulares de bloques redondeados beige-gris-marrón-naranja, sin sillares de esquina distintos; x≈0–760, y≈0–560.
396. [media] Detalles de fachada — portada lateral de la iglesia
   - Captura: Portada de piedra del mismo tono rosado-ocre que el muro, con pilastras y frontón, x≈695–745, y≈195–400.
   - Juego: Portada de aspecto rugoso gris oscuro, distinta del muro, x≈670–730, y≈180–410.
397. [media] Detalles de fachada — recercados de la casa del primer plano derecho
   - Captura: Recercados anchos gris piedra alrededor de cada ventana, balcón y puerta (x≈990–1440) y cornisa gris corrida arriba.
   - Juego: Huecos sin recercado; solo la puerta lleva un marco blanco moteado (x≈1270–1440, y≈340–580).
398. [media] Zócalo — basamento de la iglesia
   - Captura: Zócalo de piedra más oscura y saliente, con una repisa corrida en y≈400–420 de x≈200 a x≈700, y un bloque bajo saliente a la izquierda (x≈80–210, y≈310–480).
   - Juego: Los muros bajan rectos hasta el enlosado, sin zócalo ni repisa (x≈0–720, y≈380–560).
399. [media] Cubierta — alero de la casa del primer plano derecho
   - Captura: Remate con cornisa gris moldurada, sin tejas visibles (x≈955–1440, y≈0–200).
   - Juego: Alero de tejas naranjas visible en todo el borde superior (x≈940–1360, y≈0–235).
400. [media] Cubierta — remate de la segunda casa de la derecha
   - Captura: Pretil ondulado (mixtilíneo) sobre la fachada, x≈830–955, y≈240–285.
   - Juego: Remate recto con alero de tejas, x≈820–935, y≈235–300.
401. [media] Marcas viales — línea blanca del aparcamiento (derecha)
   - Captura: Línea blanca continua que separa la banda de aparcamiento de la derecha, de x≈840, y≈425 a x≈1200, y≈693.
   - Juego: Calzada sin ninguna línea pintada.
402. [media] Acera y bordillo — suelo junto a la iglesia (izquierda)
   - Captura: Enlosado de lanchas de piedra irregulares gris-beige delante de la iglesia (x≈0–560, y≈470–693) y acera de losas junto al muro (x≈300–720, y≈380–693).
   - Juego: Baldosas cuadradas regulares gris claro en toda la zona (x≈0–720, y≈380–693).
403. [baja] Huecos — huecos pequeños del muro de la iglesia
   - Captura: Dos huecos rectangulares pequeños en el muro: x≈545–575, y≈240–280 y x≈620–635, y≈175–225.
   - Juego: Muro ciego en esa zona (x≈540–660).
404. [baja] Huecos — persianas de la planta alta (derecha)
   - Captura: Persianas enrollables color ocre/tostado (x≈1075–1125, y≈180–240; x≈1275–1415, y≈60–190).
   - Juego: Persianas blancas (x≈960–990, y≈235–280; x≈1335–1440, y≈50–180).
405. [baja] Calzada — parches y grietas del asfalto
   - Captura: Asfalto uniforme, sin líneas de sellado ni parches marcados (x≈700–1200, y≈380–693).
   - Juego: Dos líneas negras largas de sellado de grietas a lo largo de la calle (x≈760–1000, y≈380–693) y un parche rectangular (x≈770–1000, y≈580–693).
406. [baja] Acera y bordillo — bordillo izquierdo
   - Captura: Bordillo bajo de granito gris que dibuja una curva, x≈560–730, y≈380–693.
   - Juego: Bordillo blanco, redondeado y más alto, casi recto, x≈690–760, y≈380–693.
407. [baja] Vegetación — macetas del balcón (derecha)
   - Captura: Balcón sin macetas (x≈1240–1440, y≈150–280).
   - Juego: Macetas con flores rosas en la barandilla, x≈1230–1390, y≈175–225.
408. [baja] Mobiliario — farol de pared (derecha)
   - Captura: Farol clásico de forja en la esquina de la segunda casa, x≈925–945, y≈255–285.
   - Juego: Farol negro moderno en la casa del primer plano, x≈1135–1195, y≈230–280; ninguno en x≈925–945.

### Calle Derecha

**Vista #40** — 02_Desde_la_iglesia_hacia_el_sur.jpg (mayo de 2024) · hoja a_040.jpg

409. [alta] Geometría — volumen del primer plano izquierdo
   - Captura: La izquierda la ocupa una pared blanca encalada con zócalo marrón que se aleja en perspectiva desde el borde de la imagen (x≈0–580, y≈0–693).
   - Juego: Una fachada ocre-mostaza puesta de frente tapa todo el primer plano izquierdo de arriba abajo (x≈0–335, y≈0–693), con una ventana de reja gris (x≈0–110, y≈355–693); la pared blanca con zócalo marrón solo aparece detrás, a partir de x≈335 y más lejos.
410. [media] Huecos — huecos de la casa blanca de la izquierda
   - Captura: Pared ciega en casi toda su longitud; solo una puerta estrecha oscura al final, x≈540–560, y≈375–475.
   - Juego: Cochera de dos hojas gris-marrón con ventanitas y un letrero azul, x≈450–505, y≈360–520.
411. [media] Huecos — planta alta de la casa del primer plano derecho
   - Captura: Un balcón pequeño de forja negra abombada sobre la puerta, x≈815–930, y≈30–215; el resto de la planta alta (x≈930–1440) es pared lisa.
   - Juego: Ventanas con persianas de librillo marrones en x≈820–915, y≈20–250 y un balcón muy grande de barandilla gris sobre losa blanca en x≈960–1440, y≈0–250.
412. [media] Huecos — puerta de la casa del primer plano derecho
   - Captura: Puerta de madera oscura tallada de dos hojas con recercado blanco ancho, x≈840–945, y≈220–560.
   - Juego: Puerta metálica clara de lamas verticales con marco blanco, más estrecha, x≈830–885, y≈350–580.
413. [media] Zócalo — zócalo de la casa del primer plano derecho
   - Captura: Zócalo de granito gris moteado en toda la base, x≈760–1440, y≈420–693.
   - Juego: Sin zócalo: el revoco beige de la fachada baja hasta la acera (x≈885–1050, y≈480–693).
414. [media] Cubierta — remate de la casa blanca de la izquierda
   - Captura: Azotea: la pared blanca termina en un pretil liso coronado por una barandilla negra de hierro, x≈180–430, y≈60–200; sin tejas.
   - Juego: Alero de tejas rojo-anaranjadas sobre la casa blanca, x≈300–605, y≈255–330, sin barandilla.
415. [media] Cubierta — alero de las casas de la derecha
   - Captura: Remate con cornisa blanca, sin tejas visibles (x≈760–1100, y≈0–280).
   - Juego: Alero de tejas rojas visible a lo largo del borde superior, x≈720–880, y≈0–270.
416. [media] Otros — losa gris volada sobre la izquierda
   - Captura: En x≈335–465, y≈125–185 solo se ve la pared blanca y la barandilla de la azotea.
   - Juego: Una losa gris plana sobresale en el aire, x≈335–465, y≈125–185, sin barandilla ni apoyo visible.
417. [baja] Huecos — reja de la ventana grande derecha
   - Captura: Reja de forja negra, x≈1130–1440, y≈160–693.
   - Juego: Reja gris clara, x≈1050–1440, y≈355–693.
418. [baja] Calzada — color del asfalto
   - Captura: Asfalto muy claro de tono arena/beige, x≈430–840, y≈385–693.
   - Juego: Asfalto gris claro neutro con una grieta oscura larga en el centro (x≈650–690, y≈365–470).
419. [baja] Acera y bordillo — acera derecha
   - Captura: Acera de baldosa cuadrada gris media con bordillo gris, x≈715–960, y≈390–693.
   - Juego: Acera de losas blancas muy claras con bordillo blanco redondeado, x≈700–960, y≈365–693.
420. [baja] Vegetación — flores del balcón derecho
   - Captura: Sin plantas en la fachada derecha.
   - Juego: Macetas con flores rosas colgando junto al balcón, x≈950–1020, y≈0–75.
421. [baja] Otros — horizonte al fondo de la calle
   - Captura: Al fondo se ven el caserío bajando y la silueta de unas sierras en el horizonte, x≈650–720, y≈320–360.
   - Juego: Al fondo solo casas rosadas y cielo, sin sierras, x≈645–700, y≈305–360.
**Vista #41** — 03_Tramo_medio_hacia_la_iglesia.jpg (mayo de 2024) · hoja a_041.jpg

422. [alta] Color de fachada — casas de la derecha en segundo plano
   - Captura: Fachadas blancas encaladas, x≈780–860, y≈200–420.
   - Juego: Fachadas salmón/rosadas con zócalo tostado, x≈775–825, y≈200–420.
423. [media] Geometría — límite entre la casa rosa y la casa blanca (izquierda)
   - Captura: La casa rosa llega hasta x≈480, donde empieza la casa blanca.
   - Juego: La casa rosa termina en x≈310 (bajante en x≈325–345); la casa blanca empieza mucho antes y su balcón y su puerta quedan más cerca.
424. [media] Geometría — torre de la iglesia al fondo
   - Captura: Torre de piedra ocre que asoma al final de la calle, más alta (remate en y≈255), sin tejado de tejas, x≈695–740, y≈255–330.
   - Juego: Torre más baja (arriba en y≈290) rematada con tejas rojas, x≈690–735, y≈290–355.
425. [media] Huecos — ventana de la casa rosa del primer plano izquierdo
   - Captura: Ventana con reja negra de dibujo geométrico (rectángulos) y persiana blanca, dentro de un recercado gris piedra, x≈0–290, y≈300–600.
   - Juego: Pared rosa lisa sin ventana; solo un panel blanco vertical en x≈0–75, y≈355–693.
426. [media] Huecos — puerta de la casa blanca de la izquierda
   - Captura: Puerta estrecha marrón, rehundida, x≈548–562, y≈300–395, con dos escalones que salen a la acera (x≈540–620, y≈395–420).
   - Juego: Puerta de madera de dos hojas con marco blanco, mucho mayor, al nivel de la acera, x≈395–485, y≈350–550; sin escalones.
427. [media] Huecos — planta alta de la casa del primer plano derecho
   - Captura: Pared blanca lisa, sin huecos, en x≈870–1440, y≈0–340.
   - Juego: Ventana grande con persiana blanca y marco blanco (x≈990–1145, y≈0–185) y ventanas con persiana oscura (x≈870–895, y≈160–255).
428. [media] Zócalo — zócalo de la casa rosa del primer plano izquierdo
   - Captura: Zócalo de granito gris moteado, x≈220–480, y≈470–693.
   - Juego: Base beige-tostada, sin zócalo gris, x≈75–310, y≈580–693.
429. [media] Zócalo — zócalo de la casa blanca de la izquierda
   - Captura: Zócalo gris muy oscuro, casi negro, x≈480–690, y≈360–520.
   - Juego: Zócalo tostado/marrón claro, x≈485–600, y≈400–520.
430. [media] Cubierta — remate de la casa blanca de la izquierda
   - Captura: Cornisa blanca volada sobre la planta baja (x≈480–570, y≈160–240) y remate blanco arriba, sin tejas visibles.
   - Juego: Alero de tejas rojo-anaranjadas, x≈420–600, y≈0–195.
431. [baja] Huecos — ventana enrejada de la casa del primer plano derecho
   - Captura: Reja negra rehundida, más pequeña, sin macetas, x≈945–1060, y≈345–505.
   - Juego: Reja gris más grande con macetas de flores en el alféizar, x≈975–1155, y≈355–625.
432. [baja] Mobiliario — señal de tráfico a la derecha
   - Captura: Sin señal visible en ese punto; solo un farol de pared en x≈773–783, y≈255–275.
   - Juego: Señal redonda roja sobre poste, x≈760–772, y≈340–352.
433. [baja] Otros — bicicleta y hierbas del primer plano izquierdo
   - Captura: Acera izquierda despejada (x≈160–410, y≈520–693).
   - Juego: Bicicleta blanca apoyada en la fachada (x≈160–410, y≈520–693) y matas de hierba al pie (x≈150–260, y≈620–693).
434. [baja] Otros — cables y cajas de contadores
   - Captura: Cajas de contadores en la casa rosa (x≈425–480, y≈220–270) y cables por las fachadas y cruzando la calle (x≈480–900, y≈0–200).
   - Juego: Sin cables ni cajas.
**Vista #42** — 04_Extremo_sur_cruce_con_Hornillos_y_Plaza_Vieja.jpg (mayo de 2024) · hoja a_042.jpg

435. [alta] Geometría — casa de la esquina izquierda
   - Captura: Una sola fachada de planta alta, con el alero a y≈170–190 en x≈0–580; encima solo cielo.
   - Juego: Fila de casas más bajas (alero a y≈265–330, x≈0–655) con otros volúmenes blancos más altos detrás (x≈0–225, y≈185–265 y x≈390–680, y≈220–330).
436. [media] Geometría — torre de la iglesia al fondo
   - Captura: La torre de Santa María asoma al final de la calle, x≈688–705, y≈245–290, con el cuerpo de la iglesia en x≈690–755, y≈280–300.
   - Juego: No se ve ninguna torre: al fondo solo cielo y casas bajas (x≈690–760).
437. [media] Geometría — casa del fondo a la derecha (x≈770–815)
   - Captura: Casa de dos plantas con la parte alta de ladrillo rojo, remate en y≈255, x≈775–815, y≈255–400.
   - Juego: Edificio salmón de 3–4 plantas, mucho más alto (remate en y≈120), x≈770–880, y≈120–400.
438. [media] Huecos — huecos de la casa de la esquina izquierda
   - Captura: Puerta con reja verde (x≈322–405, y≈375–505), ventanuco oscuro bajo el alero (x≈345–380, y≈220–270) y ventana enrejada en el borde (x≈0–40, y≈375–495); sin cochera.
   - Juego: Ventana con reja gris y macetas (x≈200–300, y≈350–460), cochera blanca enrollable (x≈385–555, y≈335–505), puerta azul (x≈600–628, y≈340–480) y ventana con contraventanas (x≈0–65, y≈360–450).
439. [media] Huecos — puerta de la casa nº 27 (primer plano derecho)
   - Captura: Gran puerta de madera oscura tallada con sobrepuerta de forja calada, x≈1130–1440, y≈200–693.
   - Juego: Persiana de cochera blanca enrollable, x≈1160–1440, y≈310–693.
440. [media] Huecos — planta alta de las casas del primer plano derecho
   - Captura: Balcones con barandilla negra (x≈905–1020, y≈60–175) y balcón con balaustrada blanca (x≈1065–1180, y≈0–80); sin contraventanas.
   - Juego: Ventanas con contraventanas verdes de lamas (x≈905–1060, y≈45–255 y x≈1185–1365, y≈0–130) y un farol (x≈920–980, y≈215–265).
441. [media] Huecos — planta baja de la segunda casa de la derecha
   - Captura: Ventana alta y estrecha con reja negra y recercado blanco, x≈930–990, y≈300–520.
   - Juego: Persiana de cochera blanca enrollable, x≈905–1075, y≈325–600.
442. [media] Detalles de fachada — estado de la fachada de la casa de la esquina izquierda
   - Captura: Encalado viejo y desconchado, con calvas que dejan ver ladrillo/adobe en la base, x≈280–600, y≈400–500, y parches de revoco.
   - Juego: Fachada blanca limpia con zócalo tostado regular (x≈75–385, y≈455–515).
443. [media] Detalles de fachada — recercado de granito de la casa nº 27
   - Captura: Recercado ancho de granito gris alrededor de la puerta, con el número 27, x≈1060–1440, y≈200–693.
   - Juego: Solo un marco blanco fino alrededor de la cochera.
444. [media] Cubierta — tejas de la casa de la esquina izquierda
   - Captura: Teja vieja de color rojo pardo oscuro, x≈0–660, y≈170–260.
   - Juego: Teja naranja viva, x≈0–655, y≈185–330.
445. [media] Calzada — suelo del cruce delante de la casa de la izquierda
   - Captura: Asfalto ocre-gris gastado y con parches de la calle transversal, con una acera estrecha elevada junto a la casa (x≈340–620, y≈500–550).
   - Juego: Explanada peatonal de baldosas claras sin calzada ni acera diferenciada, x≈0–650, y≈500–693.
446. [baja] Calzada — asfalto de la calle Derecha
   - Captura: Asfalto beige claro gastado, con parches y una tapa de registro (x≈615–655, y≈530–555).
   - Juego: Asfalto gris medio uniforme con una grieta oscura larga por el centro (x≈730–800, y≈380–693).
447. [baja] Marcas viales — líneas amarillas en los bordillos
   - Captura: Bordillos sin pintar (blanco/gris) en el primer plano.
   - Juego: Tramos de línea amarilla en los bordillos, x≈425–500, y≈630–693 y x≈950–1000, y≈635–693.
448. [baja] Vegetación — hierbas delante de la casa de la izquierda
   - Captura: Sin matas en ese punto (x≈455–555, y≈470–525).
   - Juego: Matas de hierba seca y verde, x≈455–555, y≈470–525.
449. [baja] Mobiliario — farol de la casa de la izquierda
   - Captura: Farol colgado de un brazo de forja con volutas, alto, x≈150–240, y≈210–255.
   - Juego: Farol en un brazo recto, bajo y en el borde, x≈0–105, y≈335–385.
450. [baja] Otros — caja eléctrica y cables de la casa de la izquierda
   - Captura: Caja eléctrica (x≈535–560, y≈235–275) y cables por la fachada y en el aire (x≈0–670).
   - Juego: Sin caja ni cables.

### Calle Doctor Lozano

**Vista #43** — 02_Desde_Manuel_Dorado_hacia_la_plaza.jpg (mayo de 2024) · hoja a_043.jpg

451. [alta] Geometría — anchura de la calle / posición de la fachada derecha
   - Captura: La base de las fachadas de la derecha (zócalo rojo) baja muy inclinada y llega al borde inferior en x≈960; el suelo visible abajo va de x≈520 a x≈960.
   - Juego: La base de la fachada derecha baja mucho más tendida y llega al borde inferior en x≈1380; el suelo abajo va de x≈680 a x≈1380: la fachada derecha queda bastante más lejos y la calle se ve más ancha.
452. [alta] Color de fachada — casa del primer plano izquierdo
   - Captura: Fachada blanca con recercados anchos gris claro alrededor de los huecos, x≈0–665, y≈0–693.
   - Juego: Gran paño azul verdoso (turquesa oscuro) que ocupa la mitad inferior de la fachada, x≈20–605, y≈220–693, con el resto blanco.
453. [media] Huecos — huecos de la casa del primer plano izquierdo
   - Captura: Ventana grande con reja de pletinas horizontales gris oscuro (x≈300–500, y≈270–680), portal rehundido con recercado gris (x≈570–625, y≈250–520), ventana alta con recercado gris (x≈600–635, y≈40–210) y otra enrejada (x≈628–650, y≈315–440).
   - Juego: Pared sin ningún hueco en x≈0–655; solo un bajante en x≈655–670.
454. [media] Huecos — balcón de la casa del primer plano derecho
   - Captura: Balcón arriba del todo a la derecha, x≈1080–1440, y≈0–140, con barandilla negra y losa moldurada pintada de rojo por debajo.
   - Juego: Balcón más bajo y más a la izquierda, x≈1010–1340, y≈45–295, con losa blanca lisa.
455. [media] Detalles de fachada — franjas rojas de la casa del primer plano derecho
   - Captura: Fachada crema con pilastra pintada de rojo teja (x≈940–970, de arriba abajo), franja roja horizontal (y≈150–250) y recercado rojo ancho de la ventana (x≈1155–1440, y≈280–693).
   - Juego: Fachada crema sin pilastra ni franja roja; la ventana tiene un marco rosa pálido (x≈1075–1290, y≈350–605); solo el zócalo es rojo.
456. [media] Cubierta — alero de las casas de la derecha
   - Captura: Remate con cornisa lisa, sin tejas visibles (x≈780–945, y≈0–150).
   - Juego: Alero de tejas rojas a lo largo del borde superior, x≈800–955, y≈105–300.
457. [baja] Huecos — ventana de planta baja de la casa del primer plano derecho
   - Captura: Reja de balaustres torneados negros delante de una persiana de madera marrón, x≈1155–1440, y≈280–693.
   - Juego: Reja de barrotes rectos gris oscuro, x≈1075–1290, y≈350–605.
458. [baja] Detalles de fachada — bajantes
   - Captura: No hay bajantes en las fachadas visibles (x≈640–680 y x≈860–945).
   - Juego: Bajantes blancos verticales en x≈655–670 (izquierda) y en x≈865–875 y x≈925–940 (derecha).
459. [baja] Calzada — imbornales del pavimento
   - Captura: Rejillas de desagüe en el centro de la calle, x≈720–745, y≈455–465; x≈795–810, y≈525–545; x≈900–925, y≈605–615.
   - Juego: Pavimento de losas sin rejillas.
460. [baja] Vegetación — macetas del balcón derecho
   - Captura: Balcón sin macetas.
   - Juego: Macetas con flores rosas colgadas de la barandilla, x≈1010–1230, y≈60–200.
461. [baja] Muros y vallas — verja blanca al fondo
   - Captura: Al fondo, delante del edificio que cierra la calle (x≈725–770, y≈275–355), no hay ninguna verja.
   - Juego: Verja/barandilla blanca atravesada al fondo de la calle, x≈745–800, y≈340–370.
462. [baja] Otros — cables y contadores de la derecha
   - Captura: Cajas de contadores y madeja de cables en la fachada derecha, x≈920–975, y≈90–290.
   - Juego: Sin cables ni cajas.
**Vista #44** — 03_Desde_la_plaza_hacia_Manuel_Dorado.jpg (mayo de 2024) · hoja a_044.jpg

463. [media] Huecos — ventana de planta baja de la casa del primer plano izquierdo
   - Captura: Ventana grande con reja de forja negra con nudos y persiana blanca, dentro de un recercado ancho de piedra gris clara, x≈350–570, y≈320–693.
   - Juego: Ventana más pequeña con reja de barrotes rectos y marco blanco fino, sin recercado de piedra, x≈305–480, y≈350–570.
464. [media] Huecos — planta baja de la casa del primer plano derecho
   - Captura: Puerta de madera clara de dos hojas con recercado blanco (x≈940–985, y≈310–520) y ventana grande con reja verde de balaustres abombada (x≈1100–1310, y≈300–660).
   - Juego: Caja eléctrica blanca donde estaba la puerta (x≈950–990, y≈495–570) y una puerta de lamas verticales beige con marco blanco grueso donde estaba la ventana (x≈995–1230, y≈355–693).
465. [media] Huecos — planta alta de la casa del primer plano derecho
   - Captura: Una sola ventana pequeña de marco marrón con recercado blanco, x≈935–975, y≈125–205.
   - Juego: Ventanas anchas con contraventanas de madera marrón (x≈960–1160, y≈0–170) y otra ventana estrecha (x≈880–910, y≈110–235).
466. [media] Zócalo — zócalo de la casa del primer plano derecho
   - Captura: Zócalo gris claro en la base, x≈870–1110, y≈440–600.
   - Juego: Sin zócalo: la pared blanca baja hasta el suelo (x≈860–1000, y≈450–650).
467. [media] Cubierta — alero de la casa del primer plano derecho
   - Captura: Cornisa blanca sin tejas visibles, x≈865–1030, y≈0–190.
   - Juego: Alero de tejas rojas, x≈850–925, y≈0–145.
468. [baja] Detalles de fachada — losa del balcón de la casa del primer plano izquierdo
   - Captura: Balcón sobre una base moldurada gruesa pintada de ocre/melocotón, x≈320–610, y≈0–245.
   - Juego: Balcón sobre una losa blanca lisa, x≈275–525, y≈85–300.
469. [baja] Detalles de fachada — carteles de «se vende»
   - Captura: Dos carteles de venta colgados de las barandillas de la izquierda, x≈400–485, y≈0–70 y x≈680–720, y≈215–250.
   - Juego: Sin carteles.
470. [baja] Detalles de fachada — placa con el nombre de la calle
   - Captura: No hay placa en la fachada derecha.
   - Juego: Placa blanca con borde azul «CALLE DOCTOR LOZANO», x≈1100–1290, y≈225–295.
471. [baja] Calzada — imbornal del pavimento
   - Captura: Rejilla de desagüe en el centro de la calle, x≈780–825, y≈533–548.
   - Juego: Pavimento de losas sin rejilla.
472. [baja] Mobiliario — farol de pared
   - Captura: Farol clásico en la fachada derecha, x≈828–862, y≈210–260; ninguno en la izquierda.
   - Juego: Farol negro en la fachada izquierda, metido en el balcón (x≈395–475, y≈160–230); ninguno en la derecha.

### Calle Don Manuel Dorado

**Vista #45** — 02_Desde_Cuatro_Esquinas_hacia_el_sur.jpg (mayo de 2024) · hoja a_045.jpg

473. [alta] Geometría — edificio del primer plano derecho
   - Captura: Edificio grande de aspecto público: cuerpo bajo revestido con llagueado horizontal beige y cuerpo alto blanco más alto con óculos redondos (x≈960–985, y≈0–45 y x≈925–940, y≈95–130); sale del encuadre por arriba, x≈915–1440.
   - Juego: Casa de dos plantas de revoco beige liso cuyo remate queda dentro del encuadre (y≈0–130), x≈970–1440.
474. [media] Huecos — ventana grande de la casa del primer plano izquierdo
   - Captura: Ventana grande con reja negra de diseño moderno (barras curvas y rectángulos) y persiana blanca, x≈180–490, y≈190–520.
   - Juego: Pared lisa sin ventana en x≈0–445; solo un bajante.
475. [media] Huecos — puerta de la casa del primer plano izquierdo
   - Captura: Puerta de cochera metálica gris oscura de lamas verticales, metida en un hueco rehundido, x≈620–670, y≈350–520.
   - Juego: Puerta de madera marrón de dos hojas con ventanitas, x≈555–615, y≈360–555.
476. [media] Huecos — huecos del edificio de la derecha
   - Captura: Entrada rehundida con puerta gris oscura bajo la marquesina (x≈975–1000, y≈360–490) y óculos redondos en la parte alta; sin balcones.
   - Juego: Balcón de barandilla oscura sobre losa blanca (x≈1040–1260, y≈95–300), ventana con persiana blanca (x≈1120–1210, y≈0–130) y puerta blanca de barrotes con marco blanco grueso (x≈1100–1240, y≈350–670).
477. [media] Detalles de fachada — revestimiento y marquesina del edificio de la derecha
   - Captura: Paramento con bandas horizontales marcadas (llagueado) en x≈990–1440, y≈170–693 y marquesina curva metálica oscura sobre la entrada, x≈920–1120, y≈310–360.
   - Juego: Revoco liso sin bandas y sin marquesina.
478. [media] Cubierta — alero de la casa del primer plano izquierdo
   - Captura: Remate liso sin tejas visibles, con cables a lo largo (x≈380–690, y≈0–240).
   - Juego: Alero de tejas rojas, x≈580–770, y≈0–300.
479. [media] Mobiliario — señal de prohibido estacionar
   - Captura: No hay señal en ese punto.
   - Juego: Señal grande de prohibido estacionar (círculo azul con aspa roja) en primer plano, x≈1265–1440, y≈260–390.
480. [baja] Huecos — contraventanas verdes a la izquierda
   - Captura: Las ventanas de la segunda casa (x≈690–720, y≈260–310) tienen reja y no contraventanas.
   - Juego: Ventana con contraventanas verdes, x≈670–715, y≈190–285.
481. [baja] Detalles de fachada — bajante de la casa del primer plano izquierdo
   - Captura: Sin bajante en la fachada (x≈380–690).
   - Juego: Bajante blanco grueso de arriba abajo, x≈445–470, y≈0–693.
482. [baja] Calzada — manchas y grietas del asfalto
   - Captura: Asfalto claro y limpio, x≈600–1000, y≈380–693.
   - Juego: Grieta oscura larga por el centro (x≈820–890, y≈420–693) y una mancha oscura (x≈790–915, y≈485–525).
483. [baja] Marcas viales — bordillo pintado de amarillo
   - Captura: Bordillo izquierdo blanco/gris sin pintar.
   - Juego: Tramo de bordillo amarillo, x≈590–635, y≈635–693.
484. [baja] Otros — cables de la fachada izquierda
   - Captura: Cables negros a lo largo de la parte alta de la fachada izquierda, x≈380–690, y≈0–240.
   - Juego: Sin cables.
**Vista #46** — 03_Desde_Fuentes_hacia_el_Ayuntamiento.jpg (mayo de 2024) · hoja a_046.jpg

485. [alta] Geometría — construcción de la izquierda
   - Captura: Muro/edificio alto y ciego, blanco arriba y crema abajo, de al menos dos plantas (su borde superior va de y≈0–60 en x≈0–330 a y≈240 en x≈600).
   - Juego: Casa baja de una planta con el alero de tejas en y≈75–335 (x≈0–580): mucho más baja.
486. [media] Huecos — puerta de rayas de la izquierda
   - Captura: Muro ciego, sin puertas, en x≈0–560.
   - Juego: Puerta de tiras verticales de colores (rojo, amarillo, verde, blanco), x≈285–420, y≈370–665, y un letrero azul (x≈220–255, y≈405–435).
487. [media] Huecos — planta baja de la casa del primer plano derecho
   - Captura: Ventana con reja de balaustres negros torneados y persiana blanca, con recercado blanco ancho, x≈1085–1440, y≈280–693.
   - Juego: Puerta de tiras verticales amarillas, blancas y marrones con marco blanco grueso, x≈970–1410, y≈355–693, y una caja eléctrica blanca (x≈915–965, y≈505–590).
488. [media] Huecos — huecos de la segunda casa de la derecha
   - Captura: Balcón con barandilla negra en la planta alta (x≈775–845, y≈135–265), puerta de madera oscura con recercado blanco en la baja (x≈780–850, y≈310–540) y ventana con reja (x≈730–745, y≈345–440).
   - Juego: Ventanas con persianas de librillo marrones (x≈775–860, y≈70–255) y contraventanas verdes (x≈730–765, y≈200–280) arriba; ventana con reja (x≈785–835, y≈350–480) donde estaba la puerta y puerta (x≈735–755, y≈350–445) donde estaba la reja.
489. [media] Cubierta — cubierta metálica sobre el muro de la izquierda
   - Captura: Pérgola/tejadillo de chapa con estructura metálica oscura asomando sobre el muro, x≈330–575, y≈40–210.
   - Juego: No existe; en su lugar alero de tejas naranjas con manchas blancas, x≈0–580, y≈75–335.
490. [media] Cubierta — alero de la segunda casa de la derecha
   - Captura: Tejas encaladas (blancas) en el alero, x≈700–860, y≈0–230.
   - Juego: Tejas rojo-anaranjadas, x≈690–855, y≈0–275.
491. [media] Acera y bordillo — acera izquierda
   - Captura: Casi sin acera: solo una franja estrecha con bordillo/rigola de granito gris oscuro junto al muro, x≈380–610, y≈380–693.
   - Juego: Acera blanca de más de 1 m con bordillo blanco redondeado, x≈290–590, y≈370–693.
492. [baja] Calzada — marcas del asfalto
   - Captura: Asfalto claro uniforme, x≈430–850, y≈380–693.
   - Juego: Grieta oscura larga, mancha oscura (x≈620–670, y≈480–500) y contorno de un parche rectangular (x≈540–830, y≈555–693).
493. [baja] Vegetación — flores al pie de la fachada derecha
   - Captura: Sin plantas al pie de la fachada.
   - Juego: Mata de flores amarillas, x≈900–960, y≈580–690.
494. [baja] Mobiliario — farol a la izquierda
   - Captura: Sin farol en el muro de la izquierda.
   - Juego: Farol de pared, x≈555–580, y≈340–360.
495. [baja] Otros — cables de la fachada derecha
   - Captura: Cables a lo largo de la parte alta de la fachada derecha, x≈840–1440, y≈0–170.
   - Juego: Sin cables.
**Vista #47** — 04_Cruce_con_Eugenio_Frutos.jpg (mayo de 2024) · hoja a_047.jpg

496. [alta] Color de fachada — casa del borde derecho
   - Captura: Fachada salmón/rosada desconchada, x≈1230–1440, y≈0–693.
   - Juego: Fachada blanca (continuación de la casa blanca con la ventana grande), x≈1270–1440.
497. [media] Geometría — altura de la casa del primer plano izquierdo
   - Captura: La fachada sigue por encima del borde superior de la imagen en su esquina (x≈550–570), sin alero visible.
   - Juego: El alero de tejas baja de y≈0 (x≈480) a y≈230 (x≈580): la casa es más baja.
498. [media] Color de fachada — casa del primer plano izquierdo
   - Captura: Fachada crema muy clara, casi blanca, x≈0–570.
   - Juego: Fachada beige-tostada grisácea, más oscura, x≈0–570.
499. [media] Huecos — planta baja de la casa del primer plano izquierdo
   - Captura: Ventana con persiana de madera marrón y reja negra con nudos dentro de un recercado rojo ancho, x≈80–370, y≈225–600.
   - Juego: Sin esa ventana: cochera blanca enrollable en el borde (x≈0–145, y≈290–693) y puerta de barrotes gris oscuro con marco rosa (x≈370–470, y≈350–535).
500. [media] Huecos — huecos de la casa del primer plano derecho
   - Captura: Gran portón de madera marrón de dos hojas (x≈870–1045, y≈340–630) y ventanuco oscuro encima (x≈895–925, y≈250–320).
   - Juego: Puerta estrecha marrón con ventanuco de barrotes (x≈860–905, y≈360–540) y ventana grande acristalada con marco de madera (x≈1060–1270, y≈370–660).
501. [media] Detalles de fachada — franjas y recercados rojos de la casa del primer plano izquierdo
   - Captura: Franja horizontal roja teja que cruza la fachada (y≈180–310) y recercados rojos anchos en ventanas.
   - Juego: Sin franja roja; los huecos tienen marcos rosa pálido finos.
502. [media] Detalles de fachada — pilastras ocres de la segunda casa de la derecha
   - Captura: Casa blanca con pilastras y recercados amarillo ocre en todos los huecos, x≈700–790, y≈250–450.
   - Juego: Casa blanca sin pilastras ni recercados ocres, x≈690–830.
503. [media] Cubierta — alero de la casa del primer plano derecho
   - Captura: Tejas viejas encaladas, gris claro, en un alero que sube de (x≈820, y≈250) a (x≈1230, y≈20).
   - Juego: Tejas naranja vivo en un alero más bajo, de (x≈800, y≈320) a (x≈1440, y≈110), con una chimenea encima (x≈1260–1355, y≈55–120).
504. [media] Mobiliario — espejo de tráfico
   - Captura: Espejo convexo sobre poste gris en primer plano, x≈1130–1335, y≈185–693.
   - Juego: No hay espejo ni poste.
505. [baja] Detalles de fachada — bajante negro de la izquierda
   - Captura: Bajante negro vertical de arriba abajo, x≈60–85.
   - Juego: Sin bajante en esa posición.
506. [baja] Mobiliario — señal de aparcamiento
   - Captura: Señal azul de «P», x≈710–725, y≈350–365.
   - Juego: Sin señal.
507. [baja] Otros — bicicleta y caja junto a la fachada izquierda
   - Captura: Acera despejada junto a la fachada.
   - Juego: Bicicleta verde apoyada (x≈280–440, y≈535–693) y caja blanca (x≈320–380, y≈505–580).
508. [baja] Otros — cables de la fachada derecha
   - Captura: Cables a lo largo de la fachada derecha, x≈820–1440, y≈250–350.
   - Juego: Sin cables.
509. [baja] Otros — chimenea de ladrillo al fondo
   - Captura: Chimenea alta de fábrica asomando al fondo, x≈675–685, y≈285–345.
   - Juego: Sin chimenea; al fondo solo tejados (x≈640–690).
**Vista #48** — 05_Continuacion_norte_por_Matasanos.jpg (mayo de 2024) · hoja a_048.jpg

510. [alta] Geometría — bloque alto al fondo
   - Captura: Al fondo, casas blancas de dos plantas con una puerta verde, x≈800–890, y≈235–355.
   - Juego: Bloque moderno blanco de 4–5 plantas, x≈805–910, y≈240–360.
511. [alta] Color de fachada — segunda casa de la izquierda
   - Captura: Fachada rosa/salmón, x≈720–800, y≈0–420.
   - Juego: Fachada blanca, x≈720–810, y≈40–500.
512. [media] Geometría — plantas de la segunda casa de la izquierda
   - Captura: Tres plantas, con balcones de balaustrada blanca a y≈100–160 y y≈220–290.
   - Juego: Dos plantas con alero de tejas (x≈715–810, y≈40–270) y cochera blanca (x≈730–760, y≈335–500).
513. [media] Color de fachada — casa del primer plano derecho
   - Captura: Fachada crema muy clara, casi blanca, x≈870–1440.
   - Juego: Fachada beige-tostada, x≈920–1440.
514. [media] Huecos — escaparate de la casa del primer plano izquierdo
   - Captura: Escaparate grande con marco negro (tela estampada detrás), x≈65–570, y≈230–693.
   - Juego: Pared lisa; solo una ventana más pequeña con persiana blanca en x≈565–675, y≈365–610.
515. [media] Huecos — planta alta de la casa del primer plano izquierdo
   - Captura: Balcón con barandilla negra, x≈650–720, y≈140–205.
   - Juego: Ventana con persiana blanca sin balcón, x≈565–675, y≈0–190.
516. [media] Huecos — planta baja de la casa del primer plano derecho
   - Captura: Ventana alta con reja negra y recercado ocre (x≈1015–1080, y≈330–530) y puerta pequeña (x≈940–955, y≈340–430); pared lisa en x≈1100–1440.
   - Juego: Puerta de madera de dos hojas con marco blanco en x≈1100–1215, y≈350–590 y ventanas con reja en x≈950–1020, y≈350–425.
517. [media] Detalles de fachada — molduras ocres de la casa del primer plano derecho
   - Captura: Pilastras, cornisa y recercados pintados de ocre amarillo alrededor de huecos y esquinas.
   - Juego: Sin pilastras ni recercados ocres (solo el zócalo ocre).
518. [media] Zócalo — chapado de la planta baja de la casa del primer plano izquierdo
   - Captura: Planta baja chapada de placas de granito gris moteado, x≈0–720.
   - Juego: Revoco blanco liso hasta el suelo, sin chapado.
519. [media] Calzada — color del asfalto
   - Captura: Asfalto muy claro, beige-gris, x≈650–1150, y≈360–693.
   - Juego: Asfalto gris oscuro con una grieta negra larga y una tapa rectangular (x≈830–890, y≈400–420).
520. [media] Mobiliario — alumbrado de la derecha
   - Captura: Farol de forja grande sobre brazo de volutas en la fachada, x≈1045–1205, y≈0–110.
   - Juego: Ningún farol de pared; en su lugar una farola moderna de báculo negro en la acera, x≈930–1035, y≈170–490.
521. [baja] Detalles de fachada — toldo de la derecha
   - Captura: Sin toldo.
   - Juego: Toldo de rayas rojas y blancas, x≈1030–1200, y≈45–180.
522. [baja] Marcas viales — marcas blancas en la calzada
   - Captura: Pequeños rectángulos blancos pintados en la calzada, x≈800–835, y≈488–502 y x≈862–938, y≈495–515.
   - Juego: Sin marcas.
523. [baja] Vegetación — árboles al fondo
   - Captura: Sin árboles al fondo de la calle.
   - Juego: Árboles de copa verde redonda, x≈835–910, y≈320–360.
524. [baja] Vegetación — flores de los balcones de la derecha
   - Captura: Balcones de forja sin flores.
   - Juego: Macetas con flores rosas en los balcones (x≈1040–1160, y≈180–245 y x≈1370–1440, y≈30–110).
525. [baja] Otros — cables
   - Captura: Cables por la fachada izquierda (x≈200–720, y≈150–300) y cruzando la calle (y≈200–220).
   - Juego: Sin cables.
**Vista #49** — 06_Ramal_oeste_desde_Plaza_Vieja.jpg (mayo de 2024) · hoja a_049.jpg

526. [media] Color de fachada — edificio del fondo
   - Captura: Edificio blanco con tejado de tejas cerrando la calle, x≈715–780, y≈300–360.
   - Juego: Parte alta amarilla/ocre, x≈730–770, y≈315–340 (resto blanco).
527. [media] Huecos — planta baja de la casa de la izquierda
   - Captura: Pared blanca ciega en x≈200–640 (planta baja sin huecos).
   - Juego: Cochera con persiana verde y recercado de piedra gris, x≈400–605, y≈340–693, y un letrero azul (x≈330–390, y≈450–510).
528. [media] Huecos — casa del borde derecho (x≈1300–1440)
   - Captura: Fachada blanca ciega con un azulejo/placa cerámica, x≈1380–1440, y≈95–165.
   - Juego: Ventana con persiana blanca arriba (x≈1300–1440, y≈0–170) y ventana con reja gris abajo (x≈1275–1440, y≈355–580).
529. [media] Huecos — segunda casa de la derecha (x≈900–1300)
   - Captura: Planta alta con un balcón negro y puerta de persiana marrón (x≈930–1010, y≈130–250); planta baja con ventana de reja negra (x≈950–1000, y≈305–495) y el resto ciego.
   - Juego: Planta alta con contraventanas verdes (x≈945–1005, y≈210–290), balcón con flores (x≈1010–1130, y≈220–315) y ventana con persiana (x≈1055–1110, y≈150–230); planta baja con ventana de persiana blanca (x≈1050–1110, y≈355–455).
530. [media] Cubierta — remate de las casas de ambos lados
   - Captura: Cornisas blancas sin tejas visibles (izquierda x≈580–700, y≈0–200; derecha x≈840–1300, y≈0–300).
   - Juego: Aleros de tejas rojas a ambos lados (izquierda x≈640–730, y≈0–295; derecha x≈820–1210, y≈0–290).
531. [media] Mobiliario — poste con señal y cartel municipal
   - Captura: Poste en la acera izquierda con una señal triangular (vista de espaldas) y un cartel blanco municipal con círculo rojo, x≈330–445, y≈210–693.
   - Juego: No hay poste ni señales.
532. [baja] Huecos — balcón de la casa de la izquierda
   - Captura: Balcón con balaustres blancos torneados, x≈430–580, y≈0–160.
   - Juego: Balcón de barrotes grises rectos sobre losa blanca, x≈400–655, y≈0–285.
533. [baja] Detalles de fachada — placa con el nombre de la calle
   - Captura: Placa negra con letras blancas en la fachada DERECHA, x≈1150–1240, y≈170–235.
   - Juego: Placa blanca con borde azul en la fachada IZQUIERDA, x≈410–525, y≈240–300; ninguna en la derecha.
534. [baja] Calzada — línea discontinua oscura en el asfalto
   - Captura: Asfalto sin líneas.
   - Juego: Hilera de trazos oscuros que cruza la calzada, x≈790–1030, y≈505–515.
535. [baja] Acera y bordillo — tapas de registro de la acera izquierda
   - Captura: Dos tapas redondas marrones en la acera, x≈505–560, y≈585–645.
   - Juego: Acera sin tapas.
536. [baja] Acera y bordillo — acera derecha
   - Captura: Baldosa gris con bordillo gris oscuro, x≈840–1150, y≈380–693.
   - Juego: Losas blancas con bordillo blanco redondeado, x≈820–1440, y≈370–693.
537. [baja] Mobiliario — farol de la izquierda
   - Captura: Farol de pared, x≈670–700, y≈210–260.
   - Juego: Sin farol en esa zona.
538. [baja] Otros — elemento verde arriba a la izquierda
   - Captura: En x≈595–680, y≈0–50 solo fachada blanca y cielo.
   - Juego: Pieza verde (toldo o cartel) asomando, x≈595–680, y≈0–50.

### Calle Estacada

**Vista #50** — 02_Desde_Plaza_la_Parada_hacia_el_este.jpg (mayo de 2024) · hoja a_050.jpg

539. [media] Huecos — casa blanca de la izquierda
   - Captura: Dos ventanas grandes con reja negra en planta baja (x≈450–505, y≈205–410 y x≈530–560, y≈255–390), dos balcones de forja en la alta (x≈435–535, y≈20–190 y x≈530–580, y≈135–235) y rejillas de ventilación blancas (x≈470–495, y≈450–505).
   - Juego: Puerta de tiras verticales amarillas y blancas con marco marrón en planta baja (x≈405–500, y≈325–550) y ventana con persiana blanca sin balcón arriba (x≈410–495, y≈0–190); un solo balcón más allá (x≈560–612, y≈230–305).
540. [media] Huecos — cochera de la casa del primer plano derecho
   - Captura: Puerta de cochera seccional marrón imitación madera, x≈1150–1440, y≈285–693.
   - Juego: Persiana de cochera blanca enrollable, x≈1185–1440, y≈270–660.
541. [media] Huecos — cierro acristalado de la segunda casa de la derecha
   - Captura: Cierro (mirador acristalado con forja negra) en la planta alta, x≈795–880, y≈135–290.
   - Juego: Balcón abierto con barandilla (x≈845–905, y≈250–300) y un toldito de rayas azules (x≈840–870, y≈210–235); sin cierro.
542. [media] Detalles de fachada — esquina de sillares del primer plano izquierdo
   - Captura: Pilastra/esquina de grandes sillares de granito gris-beige, de arriba abajo, x≈60–245, y≈0–693.
   - Juego: Pared de revoco crema lisa en x≈0–245, sin sillares.
543. [media] Cubierta — remate de las casas de ambos lados
   - Captura: Cornisas molduradas sin tejas visibles (derecha x≈800–1060, y≈0–200; izquierda x≈480–600, y≈0–200).
   - Juego: Aleros de tejas rojas (derecha x≈800–1080, y≈0–245; izquierda x≈600–700, y≈230–330).
544. [baja] Zócalo — zócalo de la segunda casa de la derecha
   - Captura: Zócalo rosado algo más oscuro que la fachada, x≈850–1060, y≈400–560.
   - Juego: Zócalo marrón-terracota, x≈900–1145, y≈410–530.
545. [baja] Calzada — adoquinado
   - Captura: Adoquín de granito gris-beige pequeño e irregular, x≈480–1000, y≈380–693.
   - Juego: Adoquín rectangular regular gris claro colocado a soga, x≈420–1300, y≈350–693.
546. [baja] Mobiliario — placa de vado en la cochera
   - Captura: Placa de prohibido aparcar pegada en la cochera, x≈1215–1275, y≈335–390.
   - Juego: Sin placa.
547. [baja] Otros — cables de la fachada derecha
   - Captura: Cables a lo largo de la fachada derecha, x≈1050–1440, y≈215–285.
   - Juego: Sin cables; en su lugar un bajante (x≈1145–1165, y≈0–550).
**Vista #51** — 03_Cruce_con_Malfeitos_hacia_el_este.jpg (mayo de 2024) · hoja a_051.jpg

548. [alta] Geometría — casa de la esquina derecha
   - Captura: Casa de una planta muy alta: alero de tejas de y≈45 (esquina, x≈760) a y≈200 (x≈1420); fachada de y≈520 a y≈45–200.
   - Juego: Casa mucho más baja: alero a y≈255–300 y base a y≈500–525, x≈730–1440.
549. [media] Color de fachada — casa de la esquina derecha
   - Captura: Encalado blanco con la base sucia y grietas en el revoco, x≈760–1440, y≈90–520.
   - Juego: Revoco gris medio (cemento) uniforme, x≈730–1440, y≈270–520.
550. [media] Color de fachada — casa ocre de la izquierda (x≈520–590)
   - Captura: Fachada amarillo ocre, tres plantas con balcones, x≈520–590, y≈220–380.
   - Juego: Fachadas beige claro/blancas en esa zona, x≈520–600, y≈270–380.
551. [media] Huecos — huecos de la casa de la esquina derecha
   - Captura: Fachada casi ciega: solo dos ventanucos altos y estrechos oscuros, x≈1300–1330 y x≈1375–1390, y≈355–470.
   - Juego: Dos puertas de madera de dos hojas (x≈875–945, y≈330–500 y x≈1220–1260, y≈335–475), ventana grande con reja (x≈1065–1140, y≈320–440), dos ventanas con reja (x≈1340–1440) y una cochera blanca (x≈750–775).
552. [media] Cubierta — remate de las casas de la izquierda
   - Captura: Pretiles y cornisas, uno con balaustrada decorativa (x≈320–520, y≈60–200); sin tejas visibles.
   - Juego: Aleros de tejas rojas en toda la fila (x≈140–700, y≈110–330) y placas solares sobre el tejado (x≈465–550, y≈220–260).
553. [media] Marcas viales — paso de peatones
   - Captura: Paso de cebra de franjas blancas cruzando la calle, x≈150–690, y≈440–510.
   - Juego: Sin paso de peatones.
554. [media] Acera y bordillo — acera derecha de la calle Estacada
   - Captura: Acera estrecha de baldosa rojiza, x≈695–760, y≈370–530.
   - Juego: Acera ancha de baldosa blanca con ajedrezado rojo, x≈600–780, y≈380–693.
555. [baja] Huecos — ventanas en arco de la casa crema de la izquierda
   - Captura: Ventanas altas de medio punto en la planta alta, x≈395–465, y≈170–235.
   - Juego: Ventanas rectangulares; ningún arco.
556. [baja] Detalles de fachada — toldo de la izquierda
   - Captura: Sin toldos en las fachadas de la izquierda.
   - Juego: Toldo de rayas gris y blanco, x≈230–340, y≈180–230.
557. [baja] Cubierta — antenas sobre la casa de la esquina
   - Captura: Sin antenas visibles sobre el tejado.
   - Juego: Dos antenas de televisión, x≈880–935, y≈200–225 y x≈1000–1035, y≈195–235.
558. [baja] Calzada — asfalto del cruce
   - Captura: Asfalto gris medio, con una rejilla de desagüe (x≈680–735, y≈595–635).
   - Juego: Asfalto beige claro, sin rejilla y con el contorno de un parche rectangular (x≈880–1230, y≈605–693).
559. [baja] Acera y bordillo — acera izquierda
   - Captura: Acera de baldosa rojiza/rosada, x≈0–450, y≈430–520.
   - Juego: Acera estrecha gris clara con bordillo blanco, x≈0–640, y≈370–510.
560. [baja] Vegetación — macetas en la acera izquierda
   - Captura: Acera izquierda sin macetas.
   - Juego: Macetas con flores rojas en la acera, x≈190–240, y≈420–450 y x≈325–360, y≈405–425.
561. [baja] Mobiliario — farol de la casa de la esquina
   - Captura: Farol de forja en la fachada, x≈1365–1440, y≈200–275.
   - Juego: Sin farol.
562. [baja] Otros — cable y tubo de la esquina
   - Captura: Cable/poste que sube por la esquina hasta arriba y tubo eléctrico, x≈765–830, y≈0–300.
   - Juego: Sin cables.
**Vista #52** — 04_Tramo_medio_del_sector_este.jpg (mayo de 2024) · hoja a_052.jpg

563. [media] Geometría — altura de la casa del primer plano izquierdo
   - Captura: Casa de una planta con el alero de tejas viejas visible arriba (x≈0–510, y≈60–190) y solo un ventanuco bajo él.
   - Juego: La fachada sube hasta el borde superior de la imagen (x≈0–515), con una planta alta de contraventanas verdes (x≈245–515, y≈0–185).
564. [media] Color de fachada — casa del primer plano derecho
   - Captura: Fachada crema/amarillo pálido con recercados blancos, x≈900–1440.
   - Juego: Fachada gris-beige (topo), x≈820–1440.
565. [media] Huecos — planta baja de la casa del primer plano izquierdo
   - Captura: Gran portón de madera oscura con recercado blanco (x≈0–285, y≈365–693) y placa azul con el número 777 (x≈165–222, y≈318–348).
   - Juego: Sin portón ni placa; ventana con reja blanca y macetas (x≈350–490, y≈300–520).
566. [media] Huecos — huecos de la casa del primer plano derecho
   - Captura: Planta alta con dos balcones de forja (x≈1015–1170, y≈150–270 y x≈920–990, y≈230–290); planta baja con puerta de madera oscura de dos hojas con el número 98 (x≈1035–1160, y≈295–500).
   - Juego: Planta alta con ventana de persiana blanca sin balcón (x≈1040–1150, y≈45–220); planta baja con ventana enrejada (x≈1040–1150, y≈315–450) donde estaba la puerta.
567. [media] Cubierta — remate de las casas de la derecha
   - Captura: Cornisa gris, sin tejas visibles, x≈900–1440, y≈0–210.
   - Juego: Alero de tejas rojas, x≈810–1120, y≈0–270.
568. [baja] Huecos — reja de la segunda casa de la izquierda
   - Captura: Reja negra, x≈420–475, y≈390–500.
   - Juego: Reja blanca, x≈350–490, y≈300–520.
569. [baja] Otros — cables y cajas eléctricas
   - Captura: Cables por la fachada izquierda (y≈240–320) y cruzando la calle (x≈540–900, y≈110–240), y cajas en x≈325–360, y≈245–290 y x≈490–540, y≈220–275.
   - Juego: Sin cables ni cajas.
570. [baja] Otros — objeto naranja en la acera izquierda
   - Captura: Acera sin objetos junto a la puerta (x≈605–620).
   - Juego: Bombona/objeto naranja junto a la puerta, x≈605–620, y≈415–445.
**Vista #53** — 05_Extremo_este_hacia_el_centro.jpg (mayo de 2024) · hoja a_053.jpg

571. [alta] Vegetación — hilera de árboles
   - Captura: No hay ni un árbol en la calle.
   - Juego: Hilera de árboles grandes de copa verde y tronco moteado a lo largo de la acera izquierda, desde el primer plano (copa x≈0–620, y≈0–550; tronco x≈255–335) hasta el fondo (x≈500–720), y otro en la derecha (x≈720–800, y≈235–370).
572. [media] Huecos — planta baja de la casa naranja del primer plano izquierdo
   - Captura: Ventana con persiana de madera y reja dentro de un recercado de piedra gris (x≈50–245, y≈320–470) y puerta de madera con recercado de granito y número 134 (x≈310–395, y≈320–440).
   - Juego: Gran portón de cochera de madera de dos hojas con ventanitas, x≈5–240, y≈325–555; sin la ventana ni la puerta 134.
573. [media] Huecos — planta baja de la casa del primer plano derecho
   - Captura: Pared blanca con una ventana de reja negra (x≈995–1045, y≈355–435); sin cochera.
   - Juego: Persiana de cochera blanca enrollable, x≈995–1235, y≈280–610.
574. [media] Detalles de fachada — toldo y rótulo del borde derecho
   - Captura: Pared blanca lisa con farol y cables en x≈1175–1440, y≈0–470; sin comercio.
   - Juego: Toldo de rayas beige y blancas (x≈1175–1440, y≈260–390) y un rótulo lila (x≈1305–1440, y≈160–270), como un escaparate.
575. [media] Cubierta — remate de las casas de la derecha
   - Captura: Cornisas blancas, sin tejas visibles (x≈850–1100, y≈0–200).
   - Juego: Alero de tejas rojas, x≈790–1020, y≈0–265.
576. [media] Marcas viales — líneas amarillas en los bordillos
   - Captura: Bordillos grises sin pintar a ambos lados.
   - Juego: Línea amarilla continua junto a ambos bordillos, x≈250–480, y≈495–670 y x≈905–1020, y≈505–580.
577. [baja] Mobiliario — farol del primer plano derecho
   - Captura: Farol de forja grande sobre brazo de volutas, x≈1100–1215, y≈0–110.
   - Juego: Sin farol en ese punto.
578. [baja] Otros — aire acondicionado y cables de la derecha
   - Captura: Aparato de aire acondicionado (x≈930–975, y≈150–200), caja blanca (x≈1225–1265, y≈210–250) y cables por la fachada (x≈1215–1360, y≈100–250).
   - Juego: Sin aparatos ni cables.
**Vista #54** — 06_Acceso_este_junto_a_Plaza_de_Don_Benito.jpg (mayo de 2024) · hoja a_054.jpg

579. [alta] Vegetación — árbol grande del primer plano derecho
   - Captura: Plátano de sombra grande en la isleta de la mediana: tronco claro moteado (x≈1075–1245, y≈380–693) y copa verde que ocupa x≈920–1440, y≈0–400.
   - Juego: No hay árbol grande; en la mediana un arbolito de copa granate/morada (x≈835–1075, y≈325–500) y otro verde más lejos (x≈700–860, y≈200–400).
580. [media] Huecos — casa del borde izquierdo
   - Captura: Planta baja de pared blanca ciega con zócalo gris (x≈0–300, y≈290–580).
   - Juego: Ventana con persiana blanca y alféizar blanco, x≈40–195, y≈320–495.
581. [media] Huecos — tapia/casa baja de la izquierda
   - Captura: Pared blanca larga con dos celosías de ventilación (x≈310–330, y≈240–290 y x≈455–480, y≈280–315) y una puerta de cochera metálica gris (x≈400–460, y≈345–455).
   - Juego: Cochera blanca enrollable (x≈320–425, y≈310–490), puerta (x≈462–487, y≈335–410) y ventana (x≈515–533, y≈335–385); sin celosías.
582. [media] Detalles de fachada — chapado de piedra de las casas de la derecha
   - Captura: Casa moderna con fachada chapada de pizarra/piedra multicolor, x≈945–1010, y≈225–410.
   - Juego: Casas blancas lisas, sin chapado de piedra (x≈930–1130, y≈190–370).
583. [media] Acera y bordillo — mediana central
   - Captura: Isleta estrecha de adoquín de granito gris con bordillo (x≈900–1070, y≈555–693) y una mediana estrecha al fondo (x≈700–760, y≈330–410).
   - Juego: Mediana ancha de adoquín claro en espiga con bordillo blanco, que en primer plano va de x≈1060 a x≈1440 (y≈380–693).
584. [media] Muros y vallas — valla metálica de la derecha
   - Captura: Valla/cancela de chapa gris ondulada, x≈1030–1440, y≈330–430.
   - Juego: Sin valla: fachadas blancas con una cochera blanca (x≈1140–1305, y≈320–410).
585. [baja] Marcas viales — bordillo amarillo a la izquierda
   - Captura: Bordillo gris sin pintar.
   - Juego: Tramo de bordillo amarillo, x≈440–490, y≈455–480.
586. [baja] Mobiliario — farola de la mediana
   - Captura: Farola de doble brazo pequeña, lejos, x≈710–750, y≈235–410.
   - Juego: Farola de doble brazo mucho más cerca y grande, x≈735–910, y≈40–430.
587. [baja] Mobiliario — objeto verde y rojo en primer plano izquierdo
   - Captura: Acera de baldosa oscura vacía en x≈0–230, y≈615–693.
   - Juego: Objeto verde con una pieza roja (como un contenedor), x≈0–230, y≈615–693.
588. [baja] Otros — silla en la acera izquierda
   - Captura: Acera vacía.
   - Juego: Silla de madera junto a la puerta, x≈455–485, y≈395–440.
589. [baja] Otros — bombona naranja a la derecha
   - Captura: Sin objetos junto a las fachadas de la derecha.
   - Juego: Bombona naranja, x≈1375–1410, y≈415–450.
**Vista #55** — 07_Curva_en_el_sector_este.jpg (mayo de 2024) · hoja a_055.jpg

590. [alta] Color de fachada — casa de ladrillo de la izquierda
   - Captura: Casa de ladrillo rojo visto, x≈215–275, y≈310–420.
   - Juego: Casa blanca en esa posición, x≈175–260, y≈300–395.
591. [alta] Vegetación — hilera de árboles de la izquierda
   - Captura: No hay árboles en la calle.
   - Juego: Hilera de árboles grandes de copa verde a lo largo de la acera izquierda, x≈0–390, y≈0–430 (troncos en x≈145–190, x≈240–270 y x≈300–320).
592. [media] Huecos — planta baja de la casa del primer plano derecho
   - Captura: Puerta oscura con reja (x≈660–695, y≈350–515) y ventana grande con reja de barras curvas (x≈795–1040, y≈345–600), ambas con recercado de plaqueta marrón tipo piedra.
   - Juego: Puerta de madera de dos hojas con recercado de piedra blanca moteada (x≈675–815, y≈285–580) y pared lisa donde estaba la ventana (x≈815–1440).
593. [media] Huecos — planta alta de la casa del primer plano derecho
   - Captura: Ventana de marco marrón oscuro con barandilla sencilla, x≈830–965, y≈45–255, y balconcito en x≈655–690, y≈210–300.
   - Juego: Balcón de barandilla negra más a la izquierda (x≈635–820, y≈0–255) y ventana con contraventanas verdes (x≈580–635, y≈95–215).
594. [media] Zócalo — zócalo de la casa del primer plano derecho
   - Captura: Plaqueta marrón-anaranjada de aspecto piedra rústica, x≈700–1100, y≈470–693.
   - Juego: Azulejo cuadrado beige-marrón en cuadrícula regular, x≈645–1440, y≈435–693.
595. [baja] Calzada — línea discontinua en el asfalto
   - Captura: Asfalto sin líneas, con una tapa redonda (x≈240–320, y≈600–645) y una rejilla (x≈615–660, y≈620–665).
   - Juego: Línea discontinua oscura que cruza la calzada (x≈200–490, y≈410–440); sin tapa ni rejilla.
596. [baja] Otros — ropa tendida y bombona
   - Captura: Balcón sin ropa y acera sin objetos.
   - Juego: Ropa blanca y rosa tendida en el balcón (x≈665–765, y≈0–150) y bombona naranja junto a la puerta (x≈775–830, y≈575–693).
597. [baja] Otros — cables de la fachada derecha
   - Captura: Cables a lo largo de la fachada (y≈140–330) y cruzando arriba (x≈380–640, y≈0–170).
   - Juego: Sin cables.

### Calle Eugenio Frutos

**Vista #56** — 02_Desde_el_oeste_hacia_Pajares.jpg (mayo de 2024) · hoja a_056.jpg

598. [media] Color de fachada — casa del primer plano derecho
   - Captura: Amarillo pálido/crema, x≈930–1440.
   - Juego: Ocre-mostaza más saturado, x≈910–1440.
599. [media] Huecos — planta baja del edificio de la izquierda
   - Captura: Portón de madera oscura con recercado de piedra clara (x≈0–270, y≈270–693), ventana con reja (x≈415–515, y≈320–485) y puerta color teja (x≈555–590, y≈330–480).
   - Juego: Pared lisa en x≈0–300; puerta de barrotes grises con recercado de piedra blanca moteada (x≈305–465, y≈340–590) y una ventana (x≈540–570, y≈355–430) donde estaba la puerta teja.
600. [media] Huecos — planta alta de la casa del primer plano derecho
   - Captura: Balcón corrido con barandilla negra en diagonal, x≈930–1260, y≈0–220, y un plato cerámico decorativo (x≈995–1020, y≈35–60).
   - Juego: Ventanas con contraventanas verdes y persiana blanca, sin balcón, x≈940–1200, y≈0–190.
601. [media] Detalles de fachada — revestimiento del edificio de la izquierda
   - Captura: Fachada chapada de placas de piedra gris-beige con juntas horizontales marcadas, tres plantas, x≈270–660, y≈0–480.
   - Juego: Revoco beige liso sin placas, x≈0–630.
602. [media] Cubierta — remate de las casas de la derecha
   - Captura: Cornisa blanca sin tejas visibles, x≈780–930, y≈0–270.
   - Juego: Alero de tejas rojas, x≈750–920, y≈0–280.
603. [baja] Detalles de fachada — bajante de la derecha
   - Captura: Sin bajante entre las dos casas de la derecha (x≈920–930).
   - Juego: Bajante blanco de arriba abajo, x≈900–920, y≈20–560.
604. [baja] Calzada — color del enlosado
   - Captura: Losas de granito gris medio, más oscuras en el centro, x≈390–1000, y≈350–693.
   - Juego: Losas gris muy claro casi blancas, x≈300–1000, y≈350–693.
605. [baja] Vegetación — macetas de la acera izquierda
   - Captura: Sin macetas junto a la fachada izquierda.
   - Juego: Macetas con flores rosas y rojas al pie de la fachada, x≈195–360, y≈565–693; x≈470–530, y≈460–535; x≈560–590, y≈435–470.
**Vista #57** — 03_Desde_el_este_hacia_Manuel_Dorado.jpg (mayo de 2024) · hoja a_057.jpg

606. [alta] Color de fachada — muro de ladrillo detrás del muro de la derecha
   - Captura: Pared de ladrillo rojo visto asomando detrás del muro blanco, x≈905–1220, y≈95–260.
   - Juego: Edificio blanco con contraventanas verdes en esa zona, x≈1030–1440, y≈105–240.
607. [media] Huecos — puerta de la segunda casa de la izquierda
   - Captura: Puerta de madera marrón oscura, x≈575–625, y≈360–535.
   - Juego: Ventana con reja en esa posición (x≈560–615, y≈350–450); la puerta queda más lejos (x≈648–665).
608. [media] Huecos — puerta en el muro de la derecha
   - Captura: Muro encalado ciego en x≈920–1440, y≈260–693.
   - Juego: Puerta de madera de dos hojas con ventanitas, x≈1015–1140, y≈370–670.
609. [media] Cubierta — remate de las casas de la izquierda
   - Captura: Cornisa/pretil blanco sin tejas visibles, x≈350–720, y≈0–260.
   - Juego: Alero de tejas rojas, x≈450–690, y≈0–235.
610. [media] Cubierta — remate del muro de la derecha
   - Captura: Muro encalado rematado con albardilla blanca, sin tejas (x≈870–1440, y≈20–280).
   - Juego: Alero grande de tejas naranjas festoneadas, x≈840–1440, y≈110–330.
611. [baja] Huecos — ventana de la primera casa de la izquierda
   - Captura: Ventana con persiana de madera y reja abombada blanca y negra, x≈155–405, y≈420–693.
   - Juego: Ventana con persiana beige y marco blanco, sin reja, x≈235–420, y≈360–580.
612. [baja] Calzada — color del enlosado
   - Captura: Losas de granito gris medio, x≈450–1000, y≈370–693.
   - Juego: Losas gris muy claro, x≈300–1050, y≈370–693.
613. [baja] Mobiliario — farol de la derecha
   - Captura: Farol de pared pequeño y lejano, x≈875–925, y≈190–260.
   - Juego: Farol grande y cercano, x≈975–1100, y≈320–415.
614. [baja] Muros y vallas — valla de madera de la derecha
   - Captura: Sin valla junto al muro.
   - Juego: Valla/cancela baja de madera marrón, x≈1105–1215, y≈615–693.
615. [baja] Otros — cable de la fachada izquierda
   - Captura: Cable que baja por la fachada, x≈90–130, y≈200–470.
   - Juego: Sin cable.
**Vista #58** — 04_Acceso_al_ramal_hacia_Grande.jpg (mayo de 2024) · hoja a_058.jpg

616. [alta] Color de fachada — edificio rosado al fondo izquierdo
   - Captura: Edificio salmón/rosado con tejado de tejas, x≈330–410, y≈265–375.
   - Juego: Edificios blancos en esa posición, x≈320–400, y≈250–380.
617. [media] Huecos — balcones del edificio de la esquina
   - Captura: Balcones solo en la primera planta (x≈410–550, y≈250–310 y x≈650–705, y≈260–305); la segunda planta tiene ventanas con persiana marrón sin balcón (x≈655–690, y≈135–180).
   - Juego: Balcones en la primera y en la segunda planta (x≈455–555, y≈105–200 y y≈260–320; x≈625–705, y≈110–180 y y≈260–315).
618. [media] Detalles de fachada — molduras del edificio de la esquina (centro)
   - Captura: Edificio blanco de tres plantas con pilastras de esquina y cornisas color crema, x≈400–750, y≈50–460.
   - Juego: Edificio blanco liso, sin pilastras ni cornisas crema, x≈400–810.
619. [media] Zócalo — zócalo de la casa del primer plano derecho
   - Captura: Zócalo de granito rosado-gris moteado, x≈750–1110, y≈475–693.
   - Juego: Zócalo beige/tostado, x≈810–1440, y≈520–693.
620. [media] Muros y vallas — valla metálica de la izquierda
   - Captura: Valla de barrotes verde oscuro/negra sobre murete, x≈70–190, y≈340–440.
   - Juego: Fachada blanca con ventanas en esa zona (x≈0–200), sin valla.
621. [baja] Huecos — balcón de la casa del primer plano derecho
   - Captura: Barandilla de forja negra con volutas decorativas sobre base moldurada crema, x≈1060–1440, y≈0–135.
   - Juego: Barandilla de barrotes grises rectos sobre losa blanca, más baja, x≈900–1395, y≈0–270.
622. [baja] Huecos — ventana baja de la casa del primer plano derecho
   - Captura: Reja de balaustres negros torneados con persiana de madera clara y recercado blanco ancho, x≈1065–1440, y≈310–693.
   - Juego: Reja de barrotes grises rectos con marco blanco, más pequeña, x≈935–1245, y≈350–665.
623. [baja] Calzada — enlosado y registros
   - Captura: Losas de granito gris con tapas de registro (x≈430–500, y≈550–590; x≈525–565, y≈480–495), rejillas (x≈375–415, y≈550–580; x≈600–665, y≈470–495) y placas metálicas (x≈700–800, y≈560–645).
   - Juego: Losas gris muy claro sin tapas, rejillas ni placas.
624. [baja] Otros — ropa tendida y cables
   - Captura: Muchos cables cruzando la escena (x≈300–1060, y≈0–300) y sin ropa tendida.
   - Juego: Sin cables; ropa rosa y verde tendida en un balcón (x≈650–700, y≈115–160) y macetas.
**Vista #59** — 05_Acceso_al_ramal_desde_Grande.jpg (marzo de 2009) · hoja a_059.jpg

625. [alta] Vegetación — árbol grande de la plaza (derecha)
   - Captura: Árbol grande de hoja perenne verde oscuro (tipo magnolio) que ocupa x≈940–1440, y≈0–500.
   - Juego: Ningún árbol grande; tres naranjos redondos más pequeños con frutos naranjas (x≈820–955, y≈325–480; x≈925–1095, y≈300–430; x≈1090–1440, y≈280–500).
626. [media] Color de fachada — edificio de la calle Grande a la izquierda
   - Captura: Edificios blancos con balcones, x≈180–390, y≈150–400.
   - Juego: Un edificio de cuatro plantas con las plantas altas rosa pálido, x≈280–330, y≈160–360.
627. [media] Huecos — planta baja del edificio de ladrillo nº 2
   - Captura: Puerta de madera tallada con recercado de granito (x≈465–520, y≈320–475) y ventanas con reja verde y recercado blanco (x≈408–440, y≈340–455; x≈560–625, y≈335–505).
   - Juego: Tres ventanas con reja oscura en la cara izquierda (x≈475–650, y≈345–420) y la puerta en la otra cara (x≈710–730, y≈345–445); sin la puerta tallada.
628. [media] Huecos — balcones del edificio de ladrillo nº 2
   - Captura: Primera planta con cuatro balcones de forja negra (x≈395–445, x≈455–520, x≈545–630, x≈725–760; y≈200–300); la segunda planta solo con ventanas pequeñas, sin balcones.
   - Juego: Un balcón en la primera planta de la cara izquierda (x≈585–655, y≈265–320) y otro en la segunda (x≈585–655, y≈120–195).
629. [media] Vegetación — jardinera elevada y seto de la plaza
   - Captura: Jardinera elevada con escalones y un seto, x≈1000–1400, y≈380–560.
   - Juego: Plaza plana enlosada, sin jardinera ni seto.
630. [baja] Zócalo — zócalo del edificio de ladrillo nº 2
   - Captura: Zócalo de sillería color crema, x≈390–700, y≈440–535.
   - Juego: Zócalo gris, x≈465–785, y≈400–460.
631. [baja] Calzada — adoquinado de la calle Grande
   - Captura: Adoquín de granito gris irregular, x≈0–700, y≈360–693.
   - Juego: Adoquín rectangular regular gris en hiladas onduladas, x≈0–1440, y≈360–693.
632. [baja] Mobiliario — farol de la esquina
   - Captura: Farol de pared en la esquina del edificio, x≈690–725, y≈115–215.
   - Juego: Sin farol en la esquina.
633. [baja] Mobiliario — bancos de la plaza
   - Captura: Bancos de forja y madera, x≈810–835, y≈420–470 y x≈1170–1250, y≈510–610.
   - Juego: Sin bancos en la plaza (solo una figura sentada junto al edificio, x≈740–775, y≈380–430).
**Vista #60** — 06_Ramal_sur_hacia_Herreros.jpg (mayo de 2024) · hoja a_060.jpg

634. [media] Geometría — posición de la casa del primer plano derecho
   - Captura: La fachada se aleja a lo largo de la calle: su base va de (x≈1440, y≈693) a (x≈850, y≈470).
   - Juego: La fachada está de frente y retranqueada: su base corre horizontal a y≈560 (x≈940–1440) con una explanada de losas delante (y≈560–693).
635. [media] Huecos — planta baja de la casa rosa de la izquierda
   - Captura: Ventana grande con reja negra de barrotes y recercado de piedra crema (x≈270–505, y≈335–650) y portal rehundido chapado de granito gris (x≈555–610, y≈320–530).
   - Juego: Puerta de tiras verticales amarillas y marrones con recercado de piedra blanca moteada (x≈300–500, y≈340–693) y ventana con reja (x≈570–608, y≈350–455) donde estaba el portal.
636. [media] Huecos — planta alta de la casa rosa de la izquierda
   - Captura: Sin balcón: ventana con persiana blanca arriba a la izquierda (x≈350–470, y≈0–110).
   - Juego: Balcón de barandilla gris sobre losa rosa, x≈290–545, y≈35–290.
637. [media] Huecos — huecos de la casa del primer plano derecho
   - Captura: Aparato de aire acondicionado (x≈1115–1300, y≈145–260), ventanas con reja negra arriba y abajo (x≈885–920) y el resto de la fachada ciego.
   - Juego: Ventana con persiana y balconcillo con macetas (x≈1080–1225, y≈90–280), ventana con persianas marrones (x≈885–910, y≈150–250), puerta (x≈890–915, y≈360–495) y cochera gris (x≈1025–1285, y≈340–480).
638. [media] Detalles de fachada — imposta crema de la casa rosa
   - Captura: Banda crema con dados/ménsulas a lo largo de la fachada, x≈300–650, y≈140–300.
   - Juego: Sin banda ni ménsulas.
639. [baja] Detalles de fachada — desconchones de la casa rosa
   - Captura: Calvas blancas de pintura desconchada, x≈0–270, y≈420–560.
   - Juego: Pintura rosa uniforme.
640. [baja] Acera y bordillo — acera derecha
   - Captura: Baldosa gris oscura, x≈770–1050, y≈380–693.
   - Juego: Losas gris claro con bordillo blanco redondeado, x≈760–1000, y≈380–693.
641. [baja] Otros — caja blanca y cables de la izquierda
   - Captura: Cables por la parte alta de la fachada (x≈300–660, y≈60–300); acera libre.
   - Juego: Sin cables; una caja blanca baja junto a la fachada, x≈185–305, y≈580–693.

### Calle Fuentes

**Vista #61** — 02_Desde_Plaza_Vieja_hacia_el_este.jpg (mayo de 2024) · hoja a_061.jpg

642. [alta] Geometría — volumen de la casa larga de la izquierda
   - Captura: Una sola fachada blanca larga y alta, con el alero bajando de (x≈380, y≈0) a (x≈720, y≈300) y una chimenea (x≈598–635, y≈150–210).
   - Juego: Casa baja en primer plano con el alero a y≈155–320 (x≈0–570) y, detrás, un bloque blanco de cubierta plana más alto (x≈330–680, y≈195–470).
643. [media] Huecos — huecos de la izquierda
   - Captura: Pared ciega en x≈0–650; un único portón de madera oscura en un hueco gris, x≈655–695, y≈330–425.
   - Juego: Puerta de madera clara con cristal (x≈0–185, y≈375–693), ventana con persiana blanca (x≈450–515, y≈355–460) y dos puertas azules (x≈630–675, y≈340–425).
644. [media] Huecos — planta alta de la casa del primer plano derecho
   - Captura: Pared lisa con una ventanita con barandilla negra (x≈1015–1050, y≈195–265).
   - Juego: Balcón grande de barandilla negra sobre losa blanca (x≈1040–1235, y≈155–305) con ventana de persiana blanca encima (x≈1110–1190, y≈55–180).
645. [media] Cubierta — tejas de ambos lados
   - Captura: Tejas viejas grisáceas con el borde encalado (izquierda x≈380–720, y≈0–300; derecha x≈930–1440, y≈0–240).
   - Juego: Tejas naranja vivo festoneadas (izquierda x≈0–570, y≈155–320; derecha x≈850–1150, y≈0–275).
646. [baja] Cubierta — chimenea de la izquierda
   - Captura: Chimenea blanca sobre el tejado, x≈598–635, y≈150–210.
   - Juego: Sin chimenea.
647. [baja] Otros — bombona naranja a la derecha
   - Captura: Sin objetos junto a la puerta de la derecha.
   - Juego: Bombona naranja junto a la puerta, x≈993–1018, y≈455–497.
**Vista #62** — 03_Extremo_este_hacia_Plaza_Vieja.jpg (mayo de 2024) · hoja a_062.jpg

648. [media] Huecos — huecos de la casa del primer plano izquierdo
   - Captura: Planta alta con ventana de persiana de librillo beige y recercado blanco, sin balcón (x≈405–500, y≈45–240); planta baja con portón de madera marrón de dos hojas (x≈320–500, y≈320–640) y puerta blanca en el borde (x≈0–80).
   - Juego: Balcón de balaustres blancos con macetas (x≈360–545, y≈115–300); puerta de barrotes grises con marco blanco (x≈380–500, y≈350–590); pared lisa en x≈0–190.
649. [media] Huecos — planta baja de la segunda casa de la izquierda
   - Captura: Persiana de cochera gris oscura, x≈585–635, y≈340–455.
   - Juego: Puerta verde (x≈575–610, y≈355–455), cubo azul delante (x≈570–595, y≈450–490) y toldillos verdes arriba (x≈640–680, y≈110–165).
650. [media] Huecos — planta baja de la casa del primer plano derecho
   - Captura: Ventana con reja de forja negra de remate ornamental y recercado blanco (x≈1090–1300, y≈290–680) y puerta gris azulada con escalones (x≈990–1010, y≈335–470).
   - Juego: Puerta blanca con ventanita y marco blanco (x≈1205–1440, y≈355–693); pared lisa en x≈990–1200.
651. [media] Zócalo — zócalo de la segunda casa de la derecha
   - Captura: Zócalo de azulejo rojo-marrón oscuro, x≈820–940, y≈380–480.
   - Juego: Base beige/tostada, x≈860–1000, y≈400–500.
652. [media] Acera y bordillo — acera izquierda
   - Captura: Baldosa blanca con rombos rojos en ajedrezado, x≈300–690, y≈380–693, y un tramo de bordillo pintado de amarillo (x≈590–635, y≈478–502).
   - Juego: Losas gris claro con bordillo blanco redondeado, sin dibujo rojo ni amarillo, x≈400–730, y≈380–693.
653. [media] Acera y bordillo — acera derecha
   - Captura: Baldosa blanca con rombos rojos en ajedrezado, x≈800–1150, y≈385–693.
   - Juego: Losas gris claro con bordillo blanco redondeado, x≈780–1180, y≈370–693.
654. [baja] Huecos — balcón de la casa del primer plano derecho
   - Captura: Barandilla de forja negra con remate inferior de volutas sobre base moldurada blanca, x≈1040–1360, y≈0–220.
   - Juego: Barandilla de barrotes rectos oscuros con macetas, x≈1115–1440, y≈0–280.
655. [baja] Detalles de fachada — bajantes de la casa del primer plano izquierdo
   - Captura: Sin bajantes en la fachada.
   - Juego: Dos bajantes blancos paralelos de arriba abajo, x≈195–245 y x≈265–300.
656. [baja] Calzada — parche en el asfalto
   - Captura: Asfalto beige limpio, x≈520–1000, y≈380–693.
   - Juego: Grieta oscura por el centro y contorno de un parche rectangular, x≈600–1010, y≈555–693.
657. [baja] Vegetación — macetas de la izquierda
   - Captura: Sin macetas.
   - Juego: Macetas con flores rojas y rosas en la acera y el balcón (x≈300–430, y≈580–693; x≈520–570, y≈480–540; x≈430–550, y≈115–210).
658. [baja] Mobiliario — farol de la derecha
   - Captura: Farol de pared, x≈820–835, y≈255–290.
   - Juego: Sin farol en esa casa.
659. [baja] Otros — cable que cruza la calle
   - Captura: Cable que cruza la calle de lado a lado arriba, x≈540–950, y≈45–70.
   - Juego: Sin cables.
**Vista #63** — 04_Ramal_sur_hacia_la_calle_principal.jpg (mayo de 2024) · hoja a_063.jpg

660. [media] Huecos — huecos del muro de la izquierda
   - Captura: Ventanuco con reja en lo alto (x≈580–610, y≈205–265) y una puerta en arco al fondo (x≈665–680, y≈340–425).
   - Juego: Muro completamente ciego.
661. [media] Huecos — huecos de la casa de la derecha
   - Captura: Pared encalada larga con solo dos ventanucos altos con reja (x≈895–930, y≈190–255 y x≈820–830, y≈270–300); sin puertas en el tramo visible.
   - Juego: Puerta de madera clara con cristal (x≈1195–1440, y≈385–693), ventana con persiana blanca y jardinera (x≈890–935, y≈355–470) y puertas marrones más allá (x≈830–850).
662. [media] Detalles de fachada — estado del muro de la izquierda
   - Captura: Revoco ocre muy envejecido, con chorreones de óxido, desconchones y la mitad baja oscura (marrón-gris), x≈0–700, y≈0–693.
   - Juego: Paño liso de color arena uniforme, sin manchas ni desconchones, x≈0–690.
663. [media] Cubierta — tejas de la casa de la derecha
   - Captura: Tejas viejas encaladas/grisáceas en el alero, x≈820–1060, y≈0–280.
   - Juego: Tejas naranja vivo festoneadas, x≈780–1440, y≈30–335, y placas solares en un tejado del fondo (x≈815–910, y≈260–275).
664. [media] Calzada — color del asfalto
   - Captura: Asfalto beige claro, x≈430–940, y≈360–693.
   - Juego: Asfalto gris oscuro con trazos, x≈520–980, y≈360–693.
665. [media] Acera y bordillo — acera derecha
   - Captura: Acera de baldosa gris con bordillo blanco a lo largo de la pared derecha, x≈790–1080, y≈360–693.
   - Juego: Sin acera a la derecha: el asfalto llega hasta la fachada (x≈780–960).
666. [baja] Vegetación — hierba sobre el muro de la izquierda
   - Captura: Matas de hierba seca sobre la coronación del muro, x≈400–640, y≈0–220.
   - Juego: Coronación limpia, sin hierba.
667. [baja] Vegetación — macetas al pie de la casa de la derecha
   - Captura: Sin macetas.
   - Juego: Macetas con geranios rojos al pie de la fachada, x≈945–1090, y≈600–693 y x≈830–860, y≈430–480.
668. [baja] Otros — cables de la pared derecha
   - Captura: Cables negros a lo largo de la pared derecha, x≈820–1440, y≈100–330, y por la izquierda (x≈0–640, y≈60–280).
   - Juego: Sin cables.
**Vista #64** — 05_Cruce_del_ramal_sur.jpg (mayo de 2024) · hoja a_064.jpg

669. [alta] Cámara — posición de la cámara
   - Captura: Cámara dentro del callejón estrecho: las dos paredes (blanca con zócalo gris verdoso a la izquierda, x≈0–740; ocre con zócalo naranja a la derecha, x≈790–1440) arrancan en los bordes de la imagen y fugan muy deprisa hacia el centro (x≈750, y≈340), con un farol grande en primer plano (x≈590–660, y≈65–195).
   - Juego: Cámara fuera del callejón, en un cruce abierto: delante hay una explanada enlosada (x≈0–1440, y≈500–693) y las dos casas se ven casi de frente (x≈0–680 y x≈780–1350), con la boca del callejón entre ellas (x≈600–780).

### Calle Grande

**Vista #65** — 02_Desde_Plaza_de_Espana_hacia_el_este.jpg (marzo de 2009) · hoja a_065.jpg

670. [alta] Vegetación — naranjos de la acera izquierda
   - Captura: Hilera de naranjos pequeños en la acera izquierda (tronco en x≈600, copa x≈550–660, y≈270–450, y otro en x≈625–660, y≈310–390).
   - Juego: Acera izquierda sin ningún árbol.
671. [media] Huecos — planta baja del edificio de la derecha
   - Captura: Puertas estrechas entre pilastras de mármol y una ventana con reja negra (x≈870–945, y≈350–440), con el rótulo de un café-bar (x≈810–885, y≈300–330).
   - Juego: Escaparates acristalados corridos bajo una franja verde, x≈720–1085, y≈300–520; sin reja ni rótulo.
672. [media] Huecos — planta alta de la casa de ladrillo (borde derecho)
   - Captura: Balcón de forja negra con base moldurada blanca, x≈1170–1440, y≈0–200.
   - Juego: Ventana con persiana marrón y marco blanco, sin balcón, x≈1190–1440, y≈0–190.
673. [media] Detalles de fachada — rótulo de la planta baja del primer plano izquierdo
   - Captura: Gran rótulo blanco con letras azules («…JA DE EXTREMADURA») sobre la planta baja, x≈0–500, y≈210–330.
   - Juego: Franja morada lisa sin letras, x≈0–570, y≈275–340.
674. [media] Detalles de fachada — chapado de mármol del edificio de la derecha
   - Captura: Fachada chapada de placas de mármol gris claro veteado, con recercados de piedra gris, x≈780–1090, y≈50–500.
   - Juego: Revoco blanco liso, x≈720–1085, y≈0–520.
675. [media] Zócalo — chapado de la planta baja del primer plano izquierdo
   - Captura: Planta baja chapada de granito gris moteado con puertas de cristal oscuras, x≈100–500, y≈290–600.
   - Juego: Fila de cierres metálicos grises/blancos de comercio sin chapado de piedra, x≈0–620, y≈330–640.
676. [baja] Huecos — contraventanas verdes de la izquierda
   - Captura: Fachadas blancas de la izquierda sin contraventanas verdes (x≈300–640, y≈0–300).
   - Juego: Contraventanas verdes en x≈315–430, y≈135–270 y x≈515–545, y≈160–215.
677. [baja] Detalles de fachada — toldo del primer plano izquierdo
   - Captura: Sin toldos en la fachada izquierda.
   - Juego: Toldo de rayas grises y blancas, x≈0–370, y≈340–445.
678. [baja] Marcas viales — línea amarilla del bordillo izquierdo
   - Captura: Línea amarilla continua junto al bordillo izquierdo, x≈420–640, y≈440–620.
   - Juego: Bordillo blanco sin línea amarilla.
679. [baja] Mobiliario — señal de prohibido estacionar de la derecha
   - Captura: Señal redonda azul y roja sobre poste, x≈1010–1075, y≈340–525.
   - Juego: Sin esa señal; solo un bolardo rojo y blanco (x≈800–815, y≈380–410) y un disco amarillo (x≈770–790, y≈340–355).
**Vista #66** — 03_Tramo_oriental_hacia_Plaza_de_Espana.jpg (marzo de 2009) · hoja a_066.jpg

680. [alta] Geometría — bloque rosa detrás de la primera casa de la izquierda
   - Captura: Sobre la primera casa blanca solo hay cielo; la casa rosa empieza en x≈515 (y≈110–420).
   - Juego: Un volumen rosa alto asoma por detrás y por encima de la casa blanca, x≈310–520, y≈85–230, unido a la hilera rosa que sigue hasta x≈640.
681. [alta] Vegetación — naranjos de la acera derecha
   - Captura: Hilera de naranjos pequeños en la acera derecha: x≈1005–1200, y≈235–540 (tronco en x≈1075) y otros más lejos en x≈780–840, y≈310–390 y x≈700–740, y≈325–360.
   - Juego: Acera derecha sin ningún árbol.
682. [media] Geometría — altura de la primera casa blanca de la izquierda
   - Captura: Cornisa alta con remates, a y≈0–110 en x≈380–510 (pináculo en x≈490–515, y≈75–120).
   - Juego: Alero de tejas más bajo, que baja de y≈0 (x≈150) a y≈230 (x≈515).
683. [media] Geometría — casa del borde derecho
   - Captura: Casa blanca clásica con balcón de forja de remate inferior (x≈1215–1440, y≈40–195) y ventana con reja (x≈1415–1440, y≈290–420).
   - Juego: Edificio moderno: toldo de rayas verdes y blancas (x≈1120–1440, y≈0–160), antepecho gris corrido (x≈1140–1440, y≈150–290) y planta baja beige con una puerta gris grande (x≈1160–1440, y≈300–475).
684. [media] Huecos — portada de la casa del primer plano izquierdo
   - Captura: Gran puerta acristalada con forja negra bajo un tejaroz gris moldurado, x≈0–230, y≈305–560.
   - Juego: Ventana con reja (x≈0–145, y≈340–380) tapada en parte por un árbol; sin portada ni tejaroz.
685. [media] Huecos — planta baja de la casa blanca de la derecha
   - Captura: Ventana con reja negra, x≈980–1045, y≈300–435.
   - Juego: Puerta de madera con marco blanco, x≈1015–1085, y≈345–460.
686. [media] Vegetación — árbol del primer plano izquierdo
   - Captura: Acera izquierda sin árbol (x≈0–240).
   - Juego: Árbol de copa verde redonda, x≈0–240, y≈370–660.
687. [baja] Huecos — balcón bajo la puerta verde (izquierda)
   - Captura: Balcón de forja negra bajo una puerta balconera verde, x≈335–445, y≈140–300.
   - Juego: Ventana con persiana enrollable verde y sin balcón, x≈330–390, y≈165–260.
688. [baja] Mobiliario — farol de la derecha
   - Captura: Farol de pared, x≈930–965, y≈230–280.
   - Juego: Sin farol en esa fachada.
**Vista #67** — 04_Referencia_del_cruce_de_Pajares_y_Don_Diego_Lopez.jpg (mayo de 2024) · hoja a_067.jpg

689. [media] Geometría — altura del edificio de la esquina (derecha)
   - Captura: Planta baja muy alta (ventana de x≈820–910 entre y≈250 y y≈470) y balcones de la planta primera arriba del todo (y≈40–185); el edificio sigue por encima del borde superior, sin tejado visible.
   - Juego: Dos plantas más bajas: ventanas de planta baja a y≈350–465, balcones a y≈210–305 y alero de tejas visible a y≈50–160 (x≈665–1440).
690. [media] Huecos — planta baja del edificio de la esquina
   - Captura: Una ventana alta con reja (x≈820–910, y≈250–470) y dos huecos cegados pintados de blanco (x≈1065–1145, y≈250–460; x≈1250–1315, y≈260–445); sin puertas en ese tramo.
   - Juego: Dos ventanas con reja (x≈770–865 y x≈970–1050, y≈350–465), una puerta de madera (x≈1130–1190, y≈350–475), una cochera blanca (x≈1240–1325, y≈335–475) y otra puerta (x≈1370–1410).
691. [media] Huecos — planta baja de la acera izquierda (comercios)
   - Captura: Escaparates abiertos de una tienda de modas con rótulo azul y blanco, x≈90–400, y≈315–420.
   - Juego: Cierres metálicos grises bajados, x≈100–385, y≈330–440, sin rótulo.
692. [media] Detalles de fachada — pilastras y recercados blancos del edificio de la esquina
   - Captura: Esquina y pilastras pintadas de blanco (x≈655–760, x≈960–1000, x≈1190–1240) y recercados blancos anchos en todos los huecos, sobre fondo ocre.
   - Juego: Fachada beige continua sin pilastras; solo marcos blancos finos en los huecos.
693. [media] Calzada — suelo del primer plano
   - Captura: Plataforma única de losas claras sin bordillo: el enlosado llega llano hasta la base del edificio (x≈650–1440, y≈470–693).
   - Juego: Calzada de asfalto gris-beige en primer plano (x≈0–1440, y≈500–693) y acera elevada con bordillo blanco redondeado que dobla la esquina (x≈515–790, y≈485–580).
694. [media] Calzada — calle de la izquierda
   - Captura: Asfalto gris donde aparcan los coches, x≈0–650, y≈380–600.
   - Juego: Adoquinado gris, x≈0–560, y≈400–693.
695. [media] Vegetación — jardineras redondas
   - Captura: Jardineras grandes redondas de hormigón con palmitos y plantas, x≈95–200, y≈415–475 y x≈230–420, y≈480–680.
   - Juego: Sin jardineras; en su lugar un arbolito redondo (x≈565–655, y≈370–455) y una mata (x≈375–430, y≈355–395).
696. [baja] Zócalo — zócalo del edificio de la esquina
   - Captura: Zócalo amarillo ocre intenso, x≈655–1440, y≈480–575.
   - Juego: Banda baja beige-tostada apagada, x≈680–1440, y≈465–525.
697. [baja] Mobiliario — señal de zona residencial y placa de la calle
   - Captura: Señal azul de zona residencial sobre poste (x≈975–1035, y≈300–525) y placa «CALLE PAJARES» en la esquina (x≈705–750, y≈275–295).
   - Juego: Sin señal ni placa.
698. [baja] Mobiliario — poste y bolardo junto a la esquina
   - Captura: Poste de señal (x≈455–480, y≈330–580) y bolardo (x≈505–520, y≈480–540).
   - Juego: Sin poste ni bolardo.
699. [baja] Otros — toldo y ropa tendida del edificio de la esquina
   - Captura: Sin toldo ni ropa.
   - Juego: Toldillo de rayas rojas y blancas (x≈980–1105, y≈150–180) y ropa amarilla y lila tendida (x≈1030–1090, y≈225–280).
700. [baja] Otros — banderines y cables
   - Captura: Guirnaldas de banderines verdes y blancos cruzando la calle (x≈300–650, y≈60–300) y cables por la fachada del edificio de la esquina (y≈120–200).
   - Juego: Sin banderines ni cables.

### Calle Herreros

**Vista #68** — 02_Acceso_oeste_hacia_el_este.jpg (mayo de 2024) · hoja a_068.jpg

701. [media] Huecos — planta alta de la casa del primer plano izquierdo
   - Captura: Balcón de forja negra con volutas sobre base moldurada, x≈235–490, y≈0–225.
   - Juego: Ventana con reja negra sin balcón, x≈360–470, y≈55–245.
702. [media] Huecos — planta baja de la casa del primer plano izquierdo
   - Captura: Ventana baja y ancha con reja de balaustres negros y alféizar rojizo, dentro de un recercado blanco ancho rehundido, x≈210–455, y≈235–425.
   - Juego: Puerta de madera clara de dos hojas con ventanitas, x≈355–465, y≈350–530.
703. [media] Huecos — puerta de la casa del primer plano derecho
   - Captura: Puerta de madera marrón dentro de un portal rehundido con recercado crema moldurado, x≈880–985, y≈265–600.
   - Juego: Puerta con cortina de tiras verdes y blancas en marco blanco, x≈865–965, y≈355–670.
704. [media] Huecos — balcón de la casa del primer plano derecho
   - Captura: Sobre la puerta solo hay una imposta crema moldurada (x≈880–985, y≈150–260) y una ventana arriba (x≈940–1030, y≈0–90); el único balcón es pequeño y está más lejos (x≈810–865, y≈140–245).
   - Juego: Balcón grande de barandilla negra sobre losa, x≈810–985, y≈40–290.
705. [media] Detalles de fachada — pilastras y molduras de la casa del primer plano derecho
   - Captura: Pilastra ocre (x≈1160–1210) e impostas molduradas crema en la fachada.
   - Juego: Fachada beige lisa sin pilastras ni molduras.
706. [baja] Calzada — parches del asfalto
   - Captura: Asfalto liso sin parches, x≈430–950, y≈360–693.
   - Juego: Contornos de parches rectangulares (x≈540–715, y≈475–555; x≈630–710, y≈410–435) y una grieta larga.
707. [baja] Acera y bordillo — acera derecha
   - Captura: Baldosa gris oscura con bordillo, x≈750–980, y≈370–693.
   - Juego: Losas claras con bordillo blanco redondeado, x≈740–880, y≈370–693.
708. [baja] Vegetación — macetas de la acera izquierda
   - Captura: Sin macetas.
   - Juego: Maceta con flores rosas, x≈320–405, y≈520–600.
709. [baja] Mobiliario — farol de la fachada izquierda
   - Captura: Sin farol en ese punto (x≈530–570).
   - Juego: Farol de pared, x≈530–570, y≈260–295.
710. [baja] Otros — silla en la acera izquierda
   - Captura: Acera izquierda vacía.
   - Juego: Silla blanca junto a la fachada, x≈475–525, y≈445–505.
711. [baja] Otros — cables de la fachada derecha
   - Captura: Madeja de cables por la fachada derecha, x≈850–1440, y≈145–310.
   - Juego: Sin cables.
**Vista #69** — 03_Extremo_este_hacia_el_oeste.jpg (mayo de 2024) · hoja a_069.jpg

712. [media] Huecos — cochera del edificio de la esquina izquierda
   - Captura: Cochera con puerta metálica gris oscura de lamas y recercado rojizo, x≈175–355, y≈285–470.
   - Juego: Puerta azul estrecha, x≈250–318, y≈340–500; sin cochera.
713. [media] Huecos — ventanas del edificio de la esquina izquierda
   - Captura: Solo dos ventanas con reja: una pequeña (x≈65–125, y≈275–335) y una alargada (x≈455–615, y≈225–325); el resto del muro ciego.
   - Juego: Dos filas de ventanas corridas tipo nave, sin rejas, a lo largo de todo el edificio (x≈0–680, y≈55–155 y y≈325–370).
714. [media] Huecos — muro del primer plano derecho
   - Captura: Pared blanca alta y ciega, solo con un cable, x≈1060–1440, y≈0–693.
   - Juego: Casa con ventana de persiana blanca (x≈1250–1380, y≈365–540), ventana alta (x≈1250–1380, y≈0–185) y puerta verde (x≈1100–1135, y≈355–505).
715. [media] Huecos — balcón de la segunda casa de la derecha
   - Captura: Solo un farol de pared (x≈950–990, y≈220–275) y una ventanita (x≈1000–1020, y≈325–370); sin balcón.
   - Juego: Balcón con barandilla verde-gris y farol, x≈1040–1150, y≈215–300.
716. [media] Zócalo — zócalo del edificio de la esquina izquierda
   - Captura: Muro blanco hasta el suelo, sin zócalo (x≈0–830).
   - Juego: Zócalo gris-beige alto, x≈0–825, y≈410–560.
717. [media] Zócalo — zócalo de la segunda casa de la derecha
   - Captura: Zócalo gris, x≈960–1065, y≈380–480.
   - Juego: Fachadas blancas hasta el suelo, sin zócalo (x≈950–1100).
718. [media] Cubierta — remate del primer plano derecho
   - Captura: Remate plano encalado, sin tejas (x≈1060–1440, y≈0–140).
   - Juego: Alero de tejas rojas, x≈1040–1210, y≈0–160.
719. [media] Cubierta — casas del fondo derecho
   - Captura: Casas blancas de remate plano con una franja rojiza en la cornisa, sin tejas visibles, x≈860–920, y≈215–385.
   - Juego: Casas con tejados de tejas rojas, x≈860–1060, y≈235–330.
720. [baja] Vegetación — flores al pie del edificio de la esquina
   - Captura: Sin plantas al pie del muro.
   - Juego: Mata de flores amarillas, x≈65–105, y≈430–475.
721. [baja] Mobiliario — farol del edificio de la esquina
   - Captura: Farol de forja grande en la fachada, x≈400–500, y≈0–175.
   - Juego: Sin farol.
722. [baja] Mobiliario — señal de sentido obligatorio
   - Captura: Señal redonda de sentido obligatorio sobre poste junto a la cochera, x≈345–390, y≈340–470.
   - Juego: Sin señal.
723. [baja] Otros — caja eléctrica y cable de la esquina
   - Captura: Caja eléctrica y cable bajando por la esquina, x≈735–760, y≈0–300.
   - Juego: Sin caja ni cable.
**Vista #70** — 04_Ramal_sur_desde_Fuentes.jpg (mayo de 2024) · hoja a_070.jpg

724. [alta] Geometría — rendija en el edificio de la esquina
   - Captura: Muro de la esquina continuo, blanco con zócalo ocre, x≈585–1150, y≈0–640.
   - Juego: Una rendija vertical oscura parte el edificio de arriba abajo en x≈705–730 y deja ver por detrás ladrillo, tejas y otra fachada.
725. [media] Huecos — planta baja de la casa salmón de la derecha
   - Captura: Cochera con puerta blanca y placa de vado, x≈1230–1440, y≈240–630.
   - Juego: Ventana con persiana blanca, x≈1300–1440, y≈350–620.
726. [media] Huecos — planta alta de la casa salmón de la derecha
   - Captura: Balcón de forja con base moldurada, x≈1290–1440, y≈0–180.
   - Juego: Ventana con marco blanco sin balcón, x≈1310–1440, y≈0–95.
727. [media] Huecos — balcón y puerta de la primera casa de la izquierda
   - Captura: Balcón de forja (x≈0–95, y≈210–285) y puerta (x≈30–70, y≈335–480).
   - Juego: Pared lisa con una placa pequeña (x≈10–45, y≈320–330); sin balcón ni puerta.
728. [media] Detalles de fachada — recercados ocres de las casas de la izquierda
   - Captura: Recercados ocre/crema alrededor de las ventanas (x≈115–210, y≈325–445; x≈480–505, y≈240–400) y de la puerta (x≈30–70).
   - Juego: Ventanas con marco blanco fino, sin recercados ocres.
729. [media] Cubierta — remate de las casas de la izquierda
   - Captura: Cornisa blanca sin tejas visibles, x≈0–585, y≈60–280.
   - Juego: Alero de tejas rojas, x≈0–590, y≈70–280.
730. [baja] Huecos — ventana con reja del edificio de la esquina
   - Captura: Ventana con reja más pequeña y más cerca de la esquina, x≈730–850, y≈340–490.
   - Juego: Ventana con reja mucho mayor y más a la derecha, x≈840–1030, y≈360–605.
731. [baja] Detalles de fachada — pilastras de la casa salmón de la derecha
   - Captura: Pilastras y recercados en tono salmón más oscuro, x≈1155–1230.
   - Juego: Fachada lisa sin pilastras.
732. [baja] Detalles de fachada — placa con el nombre de la calle
   - Captura: Sin placa en la esquina.
   - Juego: Placa «CALLE FUENTES», x≈1135–1255, y≈280–305.
733. [baja] Zócalo — zócalo de la primera casa de la izquierda
   - Captura: Zócalo de piedra gris, x≈55–280, y≈450–510.
   - Juego: Zócalo beige, x≈0–590, y≈455–515.
734. [baja] Calzada — color del asfalto de la calle izquierda
   - Captura: Asfalto beige claro, x≈0–585, y≈380–693.
   - Juego: Asfalto gris más oscuro, x≈0–590, y≈390–693.
735. [baja] Mobiliario — farol de la esquina
   - Captura: Farol de forja arriba a la derecha del edificio de la esquina, x≈1110–1160, y≈0–70.
   - Juego: Sin farol.
736. [baja] Mobiliario — señal de prohibido el paso
   - Captura: Señal pequeña y lejana, en la entrada de la calle junto a la esquina, x≈540–585, y≈305–355.
   - Juego: Señal grande en primer plano, sobre la acera delante de la cámara, x≈400–490, y≈300–693.
737. [baja] Otros — cables del edificio de la esquina
   - Captura: Cables por la fachada y cruzando la calle, x≈300–1150, y≈0–230.
   - Juego: Sin cables.
**Vista #71** — 05_Union_del_ramal_sur_con_el_tramo_principal.jpg (mayo de 2024) · hoja a_071.jpg

738. [alta] Geometría — posición de la fachada derecha / anchura de la calle
   - Captura: La fachada derecha está pegada a una acera estrecha: su base va de (x≈790, y≈440) a (x≈1000, y≈693).
   - Juego: La fachada derecha está retranqueada tras un enlosado ancho (x≈700–1440, y≈380–693): su base va de (x≈870, y≈420) a (x≈1440, y≈600).
739. [media] Huecos — puerta de la casa del primer plano izquierdo
   - Captura: Puerta de madera marrón oscura tallada en cuarterones, rehundida, x≈0–280, y≈390–693.
   - Juego: Puerta de madera clara de dos hojas con ventanitas y marco beige rosado, x≈40–395, y≈355–693.
740. [media] Huecos — planta alta de la casa del primer plano izquierdo
   - Captura: Pared blanca sin huecos por encima del alero, x≈0–380, y≈0–200.
   - Juego: Dos huecos con contraventanas/puertas (x≈30–120, y≈85–175 y x≈305–390, y≈105–260) con macetas.
741. [media] Huecos — planta baja de la casa de la derecha
   - Captura: Puerta de aluminio gris de dos hojas con escalones (x≈880–1000, y≈320–640), ventana con reja (x≈810–840, y≈345–440) y ventana grande con reja negra (x≈1230–1440, y≈335–693).
   - Juego: Puerta con cortina de tiras de colores (x≈970–1045, y≈345–485), ventana con reja (x≈880–915, y≈350–410) y cochera de madera clara (x≈1205–1440, y≈345–600).
742. [media] Detalles de fachada — recercados de granito de la casa de la derecha
   - Captura: Recercados anchos de granito gris en las ventanas y en la puerta (x≈880–1000, y≈80–640; x≈1230–1440, y≈335–693).
   - Juego: Ventanas sin recercado; solo marcos de piedra blanca moteada en dos puertas (x≈965–1050 y x≈1205–1440).
743. [media] Cubierta — alero bajo de la casa del primer plano izquierdo
   - Captura: Tejas encaladas (blancas), x≈0–420, y≈190–330.
   - Juego: Tejas naranja vivo festoneadas, x≈0–500, y≈140–310.
744. [baja] Huecos — planta alta de la segunda casa de la izquierda
   - Captura: Ventana con barandilla negra (x≈485–535, y≈160–270) y aparato de aire acondicionado (x≈550–585, y≈240–280).
   - Juego: Ventanas con contraventanas verdes (x≈510–545, y≈160–255 y x≈570–600, y≈215–285); sin aire acondicionado.
745. [baja] Huecos — contraventanas marrones de la casa de la derecha
   - Captura: Ventanas de la planta alta sin contraventanas (x≈810–1000, y≈80–270).
   - Juego: Contraventanas de madera marrón (x≈870–1065, y≈170–290; x≈1145–1245, y≈95–235), aire acondicionado (x≈1120–1225, y≈105–180) y ventana con persiana (x≈1255–1440, y≈30–190).
746. [baja] Vegetación — macetas de la derecha
   - Captura: Sin macetas.
   - Juego: Macetas con flores rojas y rosas al pie de la fachada, x≈920–970, y≈420–460 y x≈1130–1245, y≈485–560.
747. [baja] Mobiliario — farol de la derecha
   - Captura: Sin farol en la fachada derecha.
   - Juego: Farol negro, x≈1295–1365, y≈300–375.
748. [baja] Otros — cables
   - Captura: Cables por ambas fachadas (izquierda x≈0–620, y≈210–300; derecha x≈790–1440, y≈160–320) y uno cruzando la calle.
   - Juego: Sin cables.
**Vista #72** — 06_Ramal_sur_hacia_Fuentes.jpg (mayo de 2024) · hoja a_072.jpg

749. [alta] Color de fachada — casa del primer plano derecho
   - Captura: Fachada blanca encalada, x≈850–1440, y≈0–693.
   - Juego: Fachada rojo anaranjado (ladrillo), x≈850–1440, y≈0–693.
750. [media] Color de fachada — edificio del fondo
   - Captura: Edificio de ladrillo/salmón con ventanas, cerrando la calle, x≈645–720, y≈295–375.
   - Juego: Edificio beige claro, x≈660–715, y≈305–365.
751. [media] Huecos — portón metálico del primer plano derecho
   - Captura: Gran portón de chapa gris oscura de dos hojas, x≈975–1440, y≈295–693.
   - Juego: Sin portón: ventana grande con marco blanco (x≈1225–1440, y≈350–693) y puerta blanca con reja (x≈880–965, y≈350–600).
752. [media] Huecos — balcón del primer plano derecho
   - Captura: Pared blanca lisa en x≈840–980, y≈150–320.
   - Juego: Balcón con balaustrada blanca, x≈840–980, y≈155–310.
753. [media] Huecos — planta alta de la casa de la izquierda
   - Captura: Ventana pequeña con barandilla y macetas de flores rosas colgando, x≈365–470, y≈65–215.
   - Juego: Balcón grande de barandilla negra sobre losa blanca, x≈105–490, y≈0–290.
754. [media] Huecos — ventana de planta baja de la casa de la izquierda
   - Captura: Ventana alta y estrecha con reja de balaustres negros, sin recercado, x≈365–470, y≈355–625.
   - Juego: Ventana ancha con reja de barrotes rectos dentro de un recercado blanco, x≈175–425, y≈350–693.
755. [media] Detalles de fachada — pilastra gris de la casa de la izquierda
   - Captura: Pilastra/franja vertical gris de arriba abajo, x≈155–230.
   - Juego: Sin pilastra; pared blanca continua.
756. [media] Cubierta — remate de las casas de la izquierda
   - Captura: Cornisa blanca sin tejas visibles, x≈410–640, y≈0–280.
   - Juego: Alero de tejas rojas, x≈480–660, y≈0–275.
757. [baja] Detalles de fachada — toldo de la derecha
   - Captura: Sin toldo.
   - Juego: Toldo de rayas azules y blancas, x≈825–960, y≈30–165.
758. [baja] Zócalo — zócalo de la casa del primer plano derecho
   - Captura: Pared blanca hasta la acera, sin zócalo marcado (x≈850–975, y≈400–520).
   - Juego: Zócalo blanco-turquesa, x≈965–1180, y≈545–693.
759. [baja] Zócalo — zócalo de la casa de la izquierda
   - Captura: Zócalo salmón/rosado, x≈230–640, y≈430–693.
   - Juego: Zócalo beige-tostado, x≈420–640, y≈470–693.
760. [baja] Mobiliario — farol de la derecha
   - Captura: Farol de pared, x≈730–765, y≈220–275.
   - Juego: Sin farol en esa zona.
761. [baja] Mobiliario — banco de la acera izquierda
   - Captura: Acera izquierda sin banco.
   - Juego: Banco blanco junto a la fachada, x≈475–580, y≈480–600.
762. [baja] Otros — cables de la derecha
   - Captura: Cables a lo largo de la fachada derecha, x≈720–1440, y≈170–330.
   - Juego: Sin cables.

### Calle Hornillos

**Vista #73** — 02_Desde_la_Cuesta_hacia_Plaza_Vieja.jpg (mayo de 2024) · hoja a_073.jpg

763. [media] Geometría — altura del edificio del portón azul (derecha)
   - Captura: El edificio termina en un pretil encalado a y≈180–290 (x≈850–1440), con cielo por encima.
   - Juego: El muro sube hasta el borde superior de la imagen en casi todo su ancho (x≈840–1440, y≈0–693): mucho más alto.
764. [media] Color de fachada — casa del fondo izquierdo (x≈600–660)
   - Captura: Casas blancas, x≈600–645, y≈260–400.
   - Juego: Casa ocre/amarilla, x≈610–660, y≈245–390.
765. [media] Huecos — casa baja del primer plano izquierdo
   - Captura: Pared blanca con una ventana con reja (x≈390–450, y≈255–365) y una puerta estrecha más allá (x≈555–575, y≈340–465).
   - Juego: Gran persiana de cochera blanca enrollable que ocupa casi toda la pared, x≈0–575, y≈220–693, y una puerta de madera marrón (x≈595–625, y≈335–590).
766. [media] Cubierta — remate de la casa del primer plano izquierdo
   - Captura: Remate liso encalado que sube en diagonal, sin tejas visibles, x≈330–520, y≈90–300.
   - Juego: Alero de tejas naranjas festoneadas, x≈90–640, y≈0–320.
767. [media] Calzada — color de la calzada
   - Captura: Asfalto gris oscuro, x≈540–870, y≈380–693.
   - Juego: Pavimento beige muy claro, casi blanco, x≈580–950, y≈365–693.
768. [media] Muros y vallas — tapia de ladrillo del fondo derecho
   - Captura: Tapia de ladrillo rojo con un árbol verde asomando, x≈720–845, y≈310–365.
   - Juego: Volúmenes blancos de cubierta plana con una puerta marrón, x≈700–840, y≈285–390; sin ladrillo ni árbol.
769. [baja] Huecos — portón azul de la derecha
   - Captura: Portón de chapa ondulada azul que ocupa casi toda la altura, x≈990–1440, y≈190–693.
   - Juego: Panel azul verdoso liso más bajo, x≈1080–1440, y≈320–693.
770. [baja] Huecos — ventanas del muro derecho
   - Captura: Muro blanco sin ventanas en x≈845–990 (solo una cajita en x≈920–940, y≈290–315).
   - Juego: Ventanas horizontales tipo nave, x≈850–960, y≈320–370.
771. [baja] Detalles de fachada — bajantes de la casa del primer plano izquierdo
   - Captura: Dos bajantes grises verticales, x≈160–240, y≈200–693.
   - Juego: Sin bajantes en esa zona.
772. [baja] Cubierta — cubierta de chapa y antena del fondo izquierdo
   - Captura: Tejadillo de chapa oscura sobre estructura (x≈470–640, y≈240–300) y una antena (x≈470–500, y≈160–220).
   - Juego: Tejados de tejas naranjas, sin chapa ni antena (x≈590–660, y≈245–330).
773. [baja] Cubierta — chimenea de la derecha
   - Captura: Chimenea blanca sobre el pretil, x≈870–915, y≈180–255.
   - Juego: Sin chimenea.
774. [baja] Marcas viales — línea amarilla del bordillo derecho
   - Captura: Bordillo derecho sin pintar.
   - Juego: Línea amarilla junto al bordillo derecho, x≈800–895, y≈470–590.
775. [baja] Acera y bordillo — acera derecha
   - Captura: Baldosa gris oscura, x≈760–1060, y≈390–693.
   - Juego: Losas claras con bordillo blanco redondeado, x≈800–1060, y≈400–693.
**Vista #74** — 03_Desde_el_tramo_sur_hacia_la_Cuesta.jpg (mayo de 2024) · hoja a_074.jpg

776. [alta] Geometría — lado derecho de la calle
   - Captura: Fachada blanca continua con zócalo ocre pegada a una acera estrecha (su base va de x≈1040, y≈395 a x≈1440, y≈560) y asfalto delante.
   - Juego: Explanada enlosada ancha (x≈880–1440, y≈370–693) con un volumen beige de dos plantas puesto de frente (x≈1000–1190, y≈150–470) y la casa blanca retranqueada detrás.
777. [media] Huecos — puertas de la casa de la izquierda
   - Captura: Puerta gris oscura con recercado (x≈615–700, y≈330–475) y puerta con reja (x≈715–770, y≈330–460).
   - Juego: Sin puertas: una ventana con reja en x≈570–655, y≈350–460 y pared lisa en x≈655–700.
778. [media] Huecos — balcón y puerta de la casa del primer plano derecho
   - Captura: Pared blanca sin balcón; solo un hueco de puerta oscuro en el borde, x≈1385–1440, y≈270–520.
   - Juego: Balcón de barandilla negra (x≈1175–1440, y≈110–300) y puerta con cortina de tiras de colores (x≈1290–1395, y≈370–615).
779. [media] Detalles de fachada — recercados de la casa de la izquierda
   - Captura: Recercados y pilastras de piedra clara en todos los huecos de la parte derecha de la casa (x≈600–780, y≈140–480).
   - Juego: Huecos sin recercados ni pilastras.
780. [media] Zócalo — zócalo de la casa de la izquierda
   - Captura: Zócalo de granito gris, x≈0–770, y≈455–560.
   - Juego: Zócalo de bloques beige-tostados, x≈0–700, y≈450–650.
781. [media] Cubierta — azotea con balaustrada de la casa de la izquierda
   - Captura: La parte izquierda de la casa es más baja y termina en una azotea con balaustrada blanca, x≈0–380, y≈140–250.
   - Juego: Fachada continua hasta el borde superior de la imagen (x≈0–340), sin balaustrada; alero de tejas en x≈340–715.
782. [media] Cubierta — tejas de la casa de la izquierda
   - Captura: Borde de tejas encaladas (blancas), x≈380–780, y≈30–180.
   - Juego: Alero de tejas naranjas, x≈340–715, y≈0–145.
783. [media] Cubierta — cubierta de la casa del primer plano derecho
   - Captura: Cubierta de chapa ondulada roja, x≈1240–1440, y≈30–195.
   - Juego: Alero de tejas naranjas, x≈1140–1250, y≈0–95.
784. [media] Calzada — color de la calzada
   - Captura: Asfalto gris oscuro con grietas, x≈250–1300, y≈360–693.
   - Juego: Pavimento beige muy claro, x≈0–950, y≈370–693.
785. [media] Acera y bordillo — acera izquierda
   - Captura: Acera de baldosa gris oscura a lo largo de la casa, x≈200–880, y≈385–600.
   - Juego: Sin acera: el pavimento llega hasta el zócalo (x≈0–700, y≈450–693).
786. [baja] Huecos — ventana grande de la casa de la izquierda
   - Captura: Reja de balaustres negros con nudos, dentro de un recercado blanco ancho, x≈180–400, y≈345–550.
   - Juego: Reja de barrotes rectos grises sin recercado, x≈260–420, y≈350–510.
787. [baja] Huecos — planta alta de la casa de la izquierda
   - Captura: Ventana con persiana blanca (x≈615–700, y≈145–260) y ventana alta y estrecha de cuarterones (x≈715–770, y≈180–320).
   - Juego: Una sola ventana con marco blanco, x≈575–645, y≈145–245.
788. [baja] Zócalo — zócalo de las casas de la derecha
   - Captura: Zócalo amarillo ocre a lo largo de la fachada, x≈1040–1440, y≈380–560.
   - Juego: Fachadas blancas/beige sin zócalo ocre.
789. [baja] Mobiliario — farol de la derecha
   - Captura: Farol de pared, x≈1005–1040, y≈235–270.
   - Juego: Sin farol.
790. [baja] Otros — bombona naranja y flores
   - Captura: Sin objetos ni plantas en primer plano.
   - Juego: Bombona naranja (x≈1380–1440, y≈595–693) y mata de flores amarillas (x≈425–465, y≈510–560).
**Vista #75** — 04_Acceso_oeste_desde_Avenida_de_la_Constitucion.jpg (mayo de 2024) · hoja a_075.jpg

791. [alta] Geometría — depósito de agua tras la tapia
   - Captura: Depósito de agua elevado, cilíndrico, sobre torre de fábrica, x≈335–435, y≈160–350.
   - Juego: No existe; en esa zona hay cielo y un ciprés.
792. [media] Color de fachada — torre del fondo izquierdo
   - Captura: Torre de ladrillo rojo con remate, x≈275–320, y≈205–250.
   - Juego: Torre blanca con cupulín rojo, x≈285–345, y≈255–335.
793. [media] Color de fachada — construcción tras la tapia
   - Captura: Muros viejos de adobe/mampostería pardos, medio en ruina, con cubierta de chapa, x≈430–590, y≈270–410.
   - Juego: Casa blanca con tejado de tejas naranjas, x≈370–630, y≈310–415.
794. [media] Huecos — portón azul del edificio de la derecha
   - Captura: Gran portón metálico azul con rejilla de ventilación arriba, x≈855–975, y≈220–470, con placa de vado.
   - Juego: Solo una puerta azul pequeña, x≈855–880, y≈350–440.
795. [media] Huecos — ventanas del edificio de la derecha
   - Captura: Muro blanco ciego, sin ventanas, x≈975–1440, y≈0–693.
   - Juego: Ventanas con contraventanas de madera marrón (x≈905–1000, y≈145–270; x≈1055–1440, y≈0–220) y ventanas con persiana blanca (x≈930–975, y≈355–440; x≈1110–1290, y≈360–540).
796. [media] Cubierta — remate del edificio de la derecha
   - Captura: Pretil blanco liso con una línea rojiza fina, sin tejas, x≈810–1000, y≈0–220.
   - Juego: Alero de tejas naranjas, x≈805–1100, y≈0–250.
797. [media] Vegetación — ciprés tras la tapia
   - Captura: Sin ciprés.
   - Juego: Ciprés grande, x≈160–290, y≈85–365.
798. [media] Vegetación — hojas de palmera arriba a la izquierda
   - Captura: Solo cielo en x≈0–190, y≈0–220.
   - Juego: Hojas de palmera colgando, x≈0–190, y≈0–220.
799. [baja] Detalles de fachada — manchas del edificio de la derecha
   - Captura: Encalado blanco limpio.
   - Juego: Manchas grises de humedad por toda la fachada, x≈880–1440, y≈220–693.
800. [baja] Calzada — parche central del asfalto
   - Captura: Franja oscura de bacheo a lo largo del centro de la calzada, x≈640–780, y≈400–693.
   - Juego: Pavimento claro uniforme con una grieta y una tapa (x≈635–670, y≈460–475).
801. [baja] Acera y bordillo — acera derecha
   - Captura: Acera ancha de baldosa gris oscura, x≈800–1300, y≈380–693.
   - Juego: Losas claras con bordillo blanco redondeado, x≈780–1200, y≈370–693.
**Vista #76** — 05_Giro_junto_a_Plaza_Vieja.jpg (mayo de 2024) · hoja a_076.jpg

802. [media] Huecos — planta baja de la casa de la izquierda
   - Captura: Ventana grande con reja verde y marco verde, x≈290–445, y≈285–410.
   - Juego: Pared lisa en x≈290–420 y una puerta de madera gris de dos hojas en x≈420–485, y≈355–480.
803. [media] Huecos — tramo cercano de la casa de la derecha
   - Captura: Muro ciego en x≈1050–1440 (planta alta y baja).
   - Juego: Ventana grande arriba (x≈1210–1325, y≈70–220) y ventana grande con reja abajo (x≈1185–1330, y≈355–505).
804. [media] Cubierta — remate de la casa de la izquierda
   - Captura: Borde de cubierta sin tejas visibles, x≈200–730, y≈60–320.
   - Juego: Alero de tejas naranjas, x≈210–645, y≈0–255.
805. [media] Cubierta — remate de la casa de la derecha
   - Captura: Cornisa gris/blanca sin tejas visibles, x≈870–1440, y≈0–280.
   - Juego: Alero de tejas naranjas, x≈870–1290, y≈0–275.
806. [baja] Huecos — contraventanas de la casa de la derecha
   - Captura: Ventana de la planta alta con marco blanco y sin contraventanas, x≈1000–1035, y≈195–270.
   - Juego: Ventana con contraventanas de madera marrón, x≈1015–1100, y≈175–275.
807. [baja] Zócalo — zócalo de la casa de la derecha
   - Captura: Zócalo de piedra gris, x≈870–1440, y≈380–520.
   - Juego: Zócalo de bloques beige-tostados, x≈940–1440, y≈400–630.
808. [baja] Calzada — parche del asfalto
   - Captura: Asfalto con grietas, sin parche rectangular.
   - Juego: Contorno de un parche rectangular grande, x≈800–1175, y≈460–660.
809. [baja] Acera y bordillo — acera izquierda
   - Captura: Baldosa gris oscura, x≈60–420, y≈450–600.
   - Juego: Losas claras con bordillo blanco redondeado, x≈0–560, y≈450–693.
810. [baja] Mobiliario — farol de la izquierda
   - Captura: Farol de pared lejano, x≈640–660, y≈255–290.
   - Juego: Farol más cercano, x≈275–335, y≈205–260; ninguno en x≈640–660.
811. [baja] Otros — cables de la fachada izquierda
   - Captura: Cables a lo largo de la fachada izquierda, x≈0–640, y≈170–300.
   - Juego: Sin cables.

### Calle Malfeitos

**Vista #77** — 02_Desde_Nueva_hacia_Estacada.jpg (mayo de 2024) · hoja a_077.jpg

812. [media] Geometría — edificio alto del fondo, lado derecho
   - Captura: Bloque de unas cuatro plantas con balcones acristalados y, detrás, un torreón gris con una chimenea metálica que sube hasta y≈30 (x≈755–905, y≈30–380).
   - Juego: Edificio de tres plantas, blanco con una franja marrón arriba, cuyo remate queda en y≈170 (x≈765–875); no hay torreón ni chimenea.
813. [media] Color de fachada — casa del primer plano derecho
   - Captura: Fachada blanca (en sombra) con una banda horizontal y una pilastra ocres en el borde (x≈1180–1440, y≈0–480).
   - Juego: Fachada amarillo pálido que empieza en x≈1160 y ocupa todo el borde derecho (x≈1160–1440, y≈0–550).
814. [media] Huecos — casa del primer plano izquierdo: puerta principal
   - Captura: Gran puerta de madera marrón oscuro de dos hojas, con clavos, enmarcada en jambas de piedra gris, en primer plano a la izquierda (x≈300–440, y≈330–630).
   - Juego: En ese sitio hay una persiana metálica gris enrollable (x≈312–460, y≈300–505) y, más adelante, una puerta marrón estrecha de una hoja (x≈510–540); no hay portón de madera ni jambas de piedra.
815. [media] Huecos — casa del primer plano izquierdo: ventana del borde izquierdo
   - Captura: Ventana con reja de barrotes blancos y persiana marrón en el borde izquierdo (x≈0–130, y≈320–570).
   - Juego: Franja lisa de color claro sin ningún hueco en el borde izquierdo (x≈0–70); no hay ventana.
816. [media] Huecos — segunda casa a la izquierda: balcón de la planta alta
   - Captura: Balcón cerrado con un cañizo o celosía de madera marrón (x≈510–585, y≈190–290).
   - Juego: Balcón abierto con barandilla de barrotes negros (x≈565–620, y≈220–290).
817. [media] Huecos — casa del primer plano derecho: planta alta
   - Captura: Ventana con persiana y recercado ocre, sin balcón (x≈1060–1185, y≈40–200); a su derecha, pared blanca lisa hasta la pilastra ocre (x≈1185–1370, y≈0–260).
   - Juego: Balcón de forja negra que ocupa lo alto del borde derecho (x≈1200–1440, y≈0–150).
818. [media] Huecos — casa del primer plano derecho: planta baja junto al borde
   - Captura: Pared blanca lisa por encima del coche aparcado (x≈1185–1370, y≈260–470); la única ventana con reja de la planta baja está más a la izquierda (x≈1055–1170, y≈345–475).
   - Juego: Una ventana grande con reja negra junto al borde derecho (x≈1270–1440, y≈275–610), además de la ventana con reja de x≈1005–1085.
819. [baja] Huecos — tercera casa a la izquierda: balcón
   - Captura: Balcón con cierre de lamas marrones (x≈605–635, y≈265–310).
   - Juego: Balcón abierto con barandilla negra (x≈625–655, y≈265–305).
820. [baja] Calzada — asfalto de la calzada
   - Captura: Asfalto gris uniforme, sin grietas marcadas (x≈480–880, y≈400–693).
   - Juego: Una grieta sellada oscura recorre la calzada en diagonal desde x≈720, y≈360 hasta x≈1030, y≈693.
821. [baja] Mobiliario — farol de pared en la casa blanca de la derecha
   - Captura: No hay farol en esa fachada (x≈960–1060, y≈170–260): solo la barandilla del balcón y la banda ocre.
   - Juego: Farol negro de brazo junto al balcón (x≈975–1010, y≈180–215).
**Vista #78** — 03_Cruce_con_Don_Juan_Duran.jpg (octubre de 2021) · hoja a_078.jpg

822. [alta] Geometría — edificio de la esquina izquierda (Malfeitos con Don Juan Durán)
   - Captura: Sobre la planta del balcón de balaustres, la esquina remata en un alero curvo de teja (x≈330–660, y≈50–180); la esquina del edificio es redondeada.
   - Juego: A esa altura la fachada sigue con otra planta y otro balcón (x≈385–530, y≈0–115) y la pared continúa por encima del borde superior; la esquina es en ángulo recto (x≈570–690) y no hay alero curvo.
823. [media] Color de fachada — edificio de la esquina izquierda: planta alta
   - Captura: Planta alta de color crema-ocre (x≈330–640, y≈90–200).
   - Juego: Plantas altas de color blanco grisáceo (x≈150–630, y≈0–315).
824. [media] Color de fachada — edificio del borde derecho
   - Captura: Fachada beis/ocre claro (x≈1340–1440, y≈0–600).
   - Juego: Fachada blanco grisáceo (x≈1250–1440, y≈0–600).
825. [media] Huecos — edificio de la esquina izquierda: planta baja
   - Captura: En la planta baja roja: una puerta de madera (x≈258–295, y≈320–400), una puerta de cristal con marco blanco (x≈360–405, y≈320–410) y una ventana con barrotes blancos (x≈460–527, y≈310–380).
   - Juego: Una puerta de cochera seccional blanca (x≈165–350, y≈335–500) y una puerta con cortina de tiras verdes y blancas (x≈425–525, y≈350–495).
826. [media] Huecos — edificio de la esquina izquierda: balcón de la planta alta
   - Captura: Balcón corrido con balaustres blancos que recorre la fachada y dobla la esquina (x≈295–655, y≈195–270).
   - Juego: Balcón corto con barandilla negra, macetas y un farol (x≈148–312, y≈225–300).
827. [media] Huecos — casa del extremo izquierdo (al otro lado de Don Juan Durán)
   - Captura: Balcón con balaustrada blanca en la planta alta (x≈0–165, y≈195–255) y la puerta de madera en x≈110–170 (y≈305–410).
   - Juego: Ventana con contraventanas de madera abiertas y sin balcón (x≈0–115, y≈150–250); la puerta de madera está en x≈0–70 (y≈350–500).
828. [media] Zócalo — edificio de la esquina izquierda
   - Captura: Zócalo de granito gris bajo la planta baja roja (x≈400–600, y≈395–455).
   - Juego: El rojo baja hasta la acera sin zócalo (x≈145–690, y≈315–500).
829. [media] Calzada — asfalto del cruce y de la calle
   - Captura: Asfalto gris oscuro, muy agrietado y con parches (x≈450–1100, y≈470–693).
   - Juego: Asfalto gris claro uniforme con una sola grieta sellada (x≈630–1250, y≈360–693).
830. [media] Acera y bordillo — acera derecha
   - Captura: Acera de baldosa roja/rosada en casi todo su ancho, con damero rojo y blanco junto al bordillo (x≈900–1250, y≈470–640).
   - Juego: Tira de damero rojo y blanco junto al bordillo (x≈760–1150, y≈365–560) y losas gris claro junto a la fachada (x≈1100–1440, y≈540–693); sin baldosa roja.
831. [media] Mobiliario — señal de tráfico de la derecha
   - Captura: Señal redonda azul de sentido obligatorio (flecha blanca hacia la derecha) sobre un poste (x≈1175–1275, y≈315–385; el poste baja hasta y≈610).
   - Juego: Señal roja de dirección prohibida pegada a la fachada (x≈1030–1075, y≈318–360); no hay señal azul ni poste.
832. [baja] Detalles de fachada — edificio de la esquina izquierda: rótulos
   - Captura: Rótulo blanco «CENTRO DE FISIOTERAPIA OSTEOPATÍA» sobre la planta baja (x≈260–470, y≈283–305) y una placa redonda en la esquina (x≈598–632, y≈285–320).
   - Juego: Ningún rótulo en la fachada.
833. [baja] Detalles de fachada — toldos del edificio de la derecha
   - Captura: Toldos lisos de color verde oscuro (x≈1010–1110, y≈0–90 y x≈840–870, y≈205–235).
   - Juego: Toldos a rayas verdes y blancas (x≈1115–1240, y≈0–75 y x≈945–1020, y≈130–185).
834. [baja] Detalles de fachada — aparato de aire acondicionado de la fachada derecha
   - Captura: Aparato de aire acondicionado blanco en la fachada (x≈1145–1195, y≈185–235).
   - Juego: No hay ningún aparato en esa fachada (x≈1100–1250, y≈150–260).
835. [baja] Acera y bordillo — bordillo de la acera derecha
   - Captura: Bordillo pintado de amarillo (x≈1060–1200, y≈600–680).
   - Juego: Bordillo blanco sin pintar (x≈1100–1250, y≈550–620).
836. [baja] Acera y bordillo — bordillo de la esquina izquierda
   - Captura: Bordillo pintado de amarillo rodeando la esquina (x≈470–660, y≈430–495).
   - Juego: Bordillo blanco sin pintar en la esquina (x≈490–690, y≈360–590).
837. [baja] Mobiliario — buzón amarillo de la acera derecha
   - Captura: No hay buzón en la acera derecha (x≈820–880, y≈370–430).
   - Juego: Buzón de correos amarillo (x≈840–858, y≈385–420).
**Vista #79** — 04_Desde_el_Mercado_hacia_el_norte.jpg (mayo de 2024) · hoja a_079.jpg

838. [alta] Geometría — lado derecho de la calle
   - Captura: Una tapia encalada alta y larga, sin ventanas, cuyo remate va de y≈0 en el borde derecho a y≈240 en x≈760 (x≈750–1440, y≈0–600).
   - Juego: Casas bajas de una planta con aleros de teja naranja (x≈760–1440, y≈160–330) y cielo por encima.
839. [alta] Color de fachada — planta baja del edificio de la izquierda (comercios)
   - Captura: Paños de color salmón/melocotón separados por pilastras azules (x≈280–660, y≈235–510).
   - Juego: Pared enlucida blanco grisácea (x≈0–560, y≈150–690).
840. [media] Huecos — lado derecho de la calle: huecos
   - Captura: Una sola puerta de tablones de madera marrón bajo un guardapolvo de mortero (x≈905–1020, y≈325–560).
   - Juego: Ventana con reja negra (x≈945–1020, y≈350–470), puerta de madera (x≈865–895, y≈350–450), persiana de cochera (x≈815–845, y≈340–425) y un portón de madera clara en primer plano (x≈1260–1440, y≈375–693).
841. [media] Huecos — planta baja del edificio de la izquierda
   - Captura: Escaparates y puertas de cristal con perfilería negra (x≈55–275, y≈215–610 y x≈440–550, y≈280–520) y más escaparates al fondo (x≈560–660).
   - Juego: Ventana de vivienda con persiana marrón (x≈455–515, y≈365–520) y, más adelante, persianas metálicas grises (x≈575–690, y≈340–500).
842. [media] Zócalo — planta baja del edificio de la izquierda
   - Captura: Zócalo de placas de piedra/mármol crema bajo los paños salmón (x≈330–440, y≈490–600).
   - Juego: Sin zócalo: la pared blanca llega a la acera (x≈300–560, y≈500–690).
843. [media] Acera y bordillo — acera izquierda
   - Captura: Acera de baldosa con dibujo de rombos rojo oscuro y blancos (x≈280–670, y≈370–693).
   - Juego: Acera de losas gris claro sin dibujo rojo (x≈450–700, y≈370–693).
844. [baja] Detalles de fachada — rótulo de la tienda de pinturas
   - Captura: Rótulo «Pinturas CARMONA» en la fachada izquierda (x≈445–665, y≈205–330).
   - Juego: Sin rótulo; solo una banda amarilla y un toldo azul más al fondo (x≈575–700, y≈310–360).
845. [baja] Zócalo — parte baja de la tapia de la derecha
   - Captura: Franja inferior gris azulada y manchada en la base de la tapia (x≈1000–1440, y≈470–690).
   - Juego: Pared lisa gris clara sin zócalo (x≈1020–1260, y≈450–650).
**Vista #80** — 05_Cruce_con_Estacada.jpg (mayo de 2024) · hoja a_080.jpg

846. [alta] Geometría — lado izquierdo de la calle
   - Captura: Tapia encalada alta, sin huecos, rematada con teja (x≈0–670, y≈0–600).
   - Juego: Casas de una planta con tejado de teja naranja y otro tejado detrás (x≈0–690, y≈90–590); se ve cielo por encima de los tejados.
847. [media] Geometría — casa amarilla del primer plano derecho: altura
   - Captura: La fachada sigue por encima del borde superior de la imagen (x≈1190–1440, y≈0) y su balcón está en y≈115–240.
   - Juego: La casa termina en un alero de teja naranja en y≈100–185, con cielo encima (x≈1000–1440); su balcón está en y≈235–305.
848. [media] Huecos — lado izquierdo de la calle: huecos
   - Captura: Ningún hueco en el tramo cercano de la tapia (x≈0–600, y≈200–600).
   - Juego: Ventanas con reja (x≈45–110 y x≈578–605), una puerta de cochera blanca (x≈165–330, y≈330–580) y una puerta de madera (x≈470–520, y≈355–510).
849. [media] Huecos — edificio de la esquina derecha: planta baja
   - Captura: Puerta de madera marrón de dos hojas con marco de granito (x≈1030–1135, y≈320–470); el comercio ocupa solo la parte de la esquina (x≈735–905).
   - Juego: Dos grandes escaparates acristalados con muestrario de colores ocupan toda la planta baja (x≈840–1130, y≈340–465); no hay puerta de madera.
850. [media] Huecos — casa amarilla del primer plano derecho: planta baja
   - Captura: Ventana con reja negra en un recercado de piedra (x≈1310–1440, y≈285–420).
   - Juego: Planta baja sin ventana: pared crema lisa (x≈1135–1440, y≈310–430).
851. [media] Detalles de fachada — edificio de la esquina derecha: recercados
   - Captura: Ventanas con recercados anchos gris oscuro y una losa gris saliente sobre el balcón (x≈815–1145, y≈40–300).
   - Juego: Ventanas sin recercado gris en una fachada blanca lisa (x≈870–1090, y≈90–320).
852. [media] Zócalo — edificio de la esquina derecha
   - Captura: Zócalo de granito gris (x≈990–1190, y≈410–470).
   - Juego: Sin zócalo: los escaparates llegan al suelo (x≈840–1130, y≈400–465).
853. [media] Calzada — cruce con Estacada, primer plano derecho
   - Captura: Tras la acera de la esquina (x≈790–1440, y≈455–520) hay un bordillo y la calzada asfaltada de la calle transversal (x≈850–1440, y≈520–693).
   - Juego: Toda esa zona es una explanada de losas claras sin calzada ni bordillo (x≈830–1440, y≈440–693).
854. [baja] Detalles de fachada — edificio de la esquina derecha: toldo y rótulo
   - Captura: Rótulo «Pinturas CARMONA» sobre el comercio (x≈800–905, y≈315–350) y ningún toldo.
   - Juego: Toldo a rayas azules y blancas (x≈838–1015, y≈340–375) y una banda amarilla (x≈835–1135, y≈320–335); sin rótulo.
855. [baja] Mobiliario — farol de pared al fondo de la tapia
   - Captura: Farol de brazo en lo alto de la tapia (x≈638–660, y≈283–310).
   - Juego: No hay farol en ese punto (x≈620–680, y≈270–330).

### Calle Pajares

**Vista #81** — 02_Desde_Tunel_hacia_el_este.jpg (octubre de 2021) · hoja a_081.jpg

856. [media] Huecos — casa del primer plano izquierdo: planta baja
   - Captura: Ventana grande con reja de hierro negra y persiana verde detrás, bajo un dintel moldurado ocre (x≈210–425, y≈240–600); a su izquierda, pared blanca lisa (x≈0–210).
   - Juego: Una puerta de cochera blanca enrollable (x≈330–510, y≈280–575) y, en el borde izquierdo, una puerta marrón con un marco blanco ancho (x≈0–155, y≈255–693); no hay ventana con reja.
857. [media] Huecos — casa del primer plano izquierdo: planta alta
   - Captura: Balcón con barandilla de forja negra curvada (x≈280–440, y≈30–165).
   - Juego: Ventana sin balcón con persiana verde (x≈405–475, y≈40–195).
858. [media] Huecos — edificio del primer plano derecho: planta baja
   - Captura: Gran portón de cochera con paneles blancos opacos en un marco gris (x≈1170–1430, y≈210–680).
   - Juego: Ventana con persiana en un marco blanco (x≈1020–1120, y≈310–465) y pared lisa; no hay portón.
859. [media] Detalles de fachada — escudo de la fachada izquierda
   - Captura: Escudo heráldico en relieve en la planta alta (x≈490–535, y≈75–140).
   - Juego: No hay escudo: pared lisa (x≈480–560, y≈60–160).
860. [media] Calzada — pavimento de la calzada
   - Captura: Adoquín de granito gris parduzco, de piezas casi cuadradas en hileras curvas irregulares (x≈350–1000, y≈360–693).
   - Juego: Adoquín rectangular gris claro muy regular, colocado a soga en hileras rectas (x≈330–1150, y≈365–693).
861. [media] Acera y bordillo — acera derecha
   - Captura: Acera de baldosa gris oscura con textura de tacos (x≈830–1100, y≈380–693).
   - Juego: Acera de losas gris claro lisas (x≈800–1440, y≈370–693).
862. [baja] Detalles de fachada — cornisa de la casa de la izquierda
   - Captura: Cornisa pintada de amarillo ocre bajo el alero de teja a lo largo de la fachada (x≈480–660, y≈0–230).
   - Juego: Alero de teja naranja sin banda ocre; la pared llega blanca hasta las tejas (x≈450–640, y≈0–220).
863. [baja] Detalles de fachada — edificio del primer plano derecho: friso moldurado
   - Captura: Franja de molduras en relieve con motivos colgantes sobre la planta baja (x≈1100–1440, y≈150–280).
   - Juego: Pared lisa sin molduras (x≈1140–1440, y≈150–300).
864. [baja] Mobiliario — señal de dirección prohibida de la acera izquierda
   - Captura: Señal redonda roja de dirección prohibida sobre un poste, en primer plano (x≈355–440, y≈278–360; el poste baja hasta y≈640).
   - Juego: No hay señal ni poste (en x≈330–510 está la puerta de cochera).
**Vista #82** — 03_Tramo_este_hacia_Tunel.jpg (octubre de 2021) · hoja a_082.jpg

865. [media] Color de fachada — casa del primer plano derecho
   - Captura: Fachada color melocotón/salmón claro (x≈830–1440, y≈0–420).
   - Juego: Fachada crema amarillenta más pálida (x≈830–1250, y≈0–610).
866. [media] Color de fachada — borde derecho de la imagen
   - Captura: La fachada melocotón sigue hasta el borde derecho (x≈1250–1440).
   - Juego: Una pared enlucida blanca ocupa todo el borde derecho (x≈1250–1440, y≈0–693).
867. [media] Huecos — casa del primer plano izquierdo: planta baja
   - Captura: Ventana grande con reja de hierro negra y persiana verde (x≈45–285, y≈335–570) en pared blanca.
   - Juego: Gran escaparate o cierre acristalado con marco blanco y una marquesina plana encima (x≈0–310, y≈170–693).
868. [media] Huecos — segunda casa a la izquierda: balcón
   - Captura: Pared blanca con una ventanita (x≈568–585, y≈200–245) y sin balcón (x≈525–610, y≈245–300).
   - Juego: Balcón con barandilla negra y un farol (x≈528–605, y≈245–300).
869. [media] Huecos — casa del primer plano derecho: planta alta
   - Captura: Ventanita de marco marrón metida en un hueco con guardapolvo, sin balcón (x≈950–1005, y≈110–210).
   - Juego: Balcón con barandilla negra y ventana con persiana (x≈895–1085, y≈65–270).
870. [media] Huecos — casa del primer plano derecho: planta baja
   - Captura: Ventana con reja negra ornamentada (x≈950–1025, y≈350–540).
   - Juego: Puerta con barrotes verticales gris azulados (x≈960–1055, y≈325–565).
871. [media] Detalles de fachada — edificio de varias plantas del fondo izquierdo
   - Captura: Pilastras y frentes de balcón de ladrillo visto rojizo sobre fachada blanca (x≈620–680, y≈105–390).
   - Juego: El edificio de esa posición es todo blanco, sin ladrillo visto (x≈470–670, y≈45–330).
872. [media] Zócalo — casa del primer plano derecho
   - Captura: Zócalo alto de baldosas beis/tostadas (x≈830–1440, y≈420–660).
   - Juego: Sin zócalo diferenciado: la pared crema baja hasta el escalón (x≈1060–1250, y≈470–690).
873. [media] Calzada — pavimento de la calzada
   - Captura: Adoquín de granito gris parduzco de piezas casi cuadradas (x≈480–980, y≈370–693).
   - Juego: Adoquín rectangular gris claro, regular, colocado a soga (x≈190–1050, y≈360–693).
874. [media] Mobiliario — contenedores de basura
   - Captura: Dos contenedores amarillos y dos verdes grandes junto a la acera izquierda (x≈240–600, y≈420–693).
   - Juego: No hay contenedores: acera y calzada vacías (x≈200–600, y≈420–693).
875. [baja] Detalles de fachada — segunda casa a la izquierda: toldo
   - Captura: Sin toldo (x≈530–600, y≈180–235).
   - Juego: Toldo amarillo sobre el balcón (x≈535–590, y≈185–230).
876. [baja] Acera y bordillo — bordillo derecho
   - Captura: Bordillo pintado de amarillo en toda su longitud (x≈740–985, y≈370–680).
   - Juego: Bordillo blanco sin pintar (x≈740–1050, y≈370–693).
877. [baja] Acera y bordillo — bordillo izquierdo
   - Captura: Bordillo pintado de amarillo (x≈595–660, y≈395–455).
   - Juego: Bordillo blanco sin pintar (x≈420–690, y≈380–560).
**Vista #83** — 04_Tramo_sur_hacia_el_Mercado.jpg (mayo de 2024) · hoja a_083.jpg

878. [media] Geometría — edificio del frente (centro-izquierda)
   - Captura: Edificio de dos plantas visto de frente, con la fachada plana hasta su esquina en x≈810 y el remate saliendo por el borde superior (x≈330–810, y≈0–440).
   - Juego: El edificio de esa posición es más bajo en la imagen (remate en y≈190–230, cielo encima) y hace esquina en x≈635, con una fachada lateral que gira hacia la derecha (x≈635–755).
879. [media] Huecos — edificio del frente: balcones y puerta
   - Captura: Balcones con barandilla de hierro negra en la primera planta (x≈440–725, y≈185–245) y puerta de madera en el centro de la planta baja (x≈470–505, y≈290–410).
   - Juego: Ventanas con contraventanas verdes y sin balcones (x≈345–630, y≈220–295); en la planta baja solo ventanas con reja (x≈275–610, y≈345–415), sin puerta.
880. [media] Huecos — edificio de la derecha: planta baja
   - Captura: Planta baja chapada de piedra gris con un solo escaparate con cartel (x≈1130–1195, y≈345–435) y una puerta oscura (x≈1355–1440).
   - Juego: Escaparates de cristal continuos en toda la planta baja (x≈990–1440, y≈370–620).
881. [media] Detalles de fachada — edificio del frente: pilastras y recercados
   - Captura: Pilastras blancas y recercados moldurados blancos sobre paños crema (x≈330–810, y≈0–400).
   - Juego: Fachada crema lisa, sin pilastras ni molduras (x≈255–635, y≈210–445).
882. [media] Detalles de fachada — edificio de la derecha: rótulo
   - Captura: Banda roja con letras blancas (rótulo de banco) sobre la planta baja (x≈1065–1440, y≈255–325).
   - Juego: Banda verde (x≈985–1440, y≈285–330).
883. [media] Zócalo — edificio del frente
   - Captura: Zócalo amarillo ocre (x≈340–810, y≈395–440).
   - Juego: Sin zócalo: la fachada crema llega al suelo (x≈255–635, y≈400–445).
884. [media] Cubierta — edificio del frente: remate
   - Captura: Cornisa moldurada blanca y pretil alto, sin teja a la vista (x≈330–810, y≈0–95).
   - Juego: Alero de teja naranja (x≈240–755, y≈180–320).
885. [media] Calzada — pavimento del primer plano y del cruce
   - Captura: Losas de granito gris claro con triángulos rojizos incrustados, sin asfalto (x≈300–1440, y≈450–693).
   - Juego: Asfalto con una grieta (x≈360–1230, y≈400–693), más un abanico de adoquines (x≈0–470, y≈420–600) y adoquín rectangular gris (x≈0–690, y≈550–693).
886. [media] Marcas viales — paso de peatones
   - Captura: Paso de peatones de bandas blancas que cruza la calle (x≈890–1090, y≈430–480).
   - Juego: No hay paso de peatones (x≈760–1000, y≈400–480).
887. [baja] Detalles de fachada — edificio de la derecha: toldos
   - Captura: Sin toldos.
   - Juego: Toldos a rayas naranjas y blancas (x≈945–1440, y≈340–430).
888. [baja] Detalles de fachada — edificio de la izquierda: toldo
   - Captura: Toldo negro sobre un local (x≈150–290, y≈320–365).
   - Juego: En esa zona, persianas metálicas sin toldo (x≈60–255, y≈335–420); solo hay un toldo rojo y blanco en x≈0–60.
889. [baja] Vegetación — arbusto al pie del edificio del frente
   - Captura: No hay ningún arbusto ante la fachada (x≈430–545, y≈370–460).
   - Juego: Arbusto verde redondo junto a la fachada (x≈430–545, y≈370–460).
890. [baja] Vegetación — jardinera de la esquina
   - Captura: Jardinera redonda blanca con una planta de hojas largas en la esquina (x≈775–875, y≈430–530).
   - Juego: No hay jardinera (x≈760–880, y≈400–530).
891. [baja] Mobiliario — farol de pared del edificio del frente
   - Captura: Farol de brazo en la fachada (x≈395–430, y≈205–255).
   - Juego: No hay farol en la fachada.
892. [baja] Mobiliario — señal de aparcamiento (P)
   - Captura: Señal azul de aparcamiento «P» sobre un poste (x≈770–810, y≈315–370; poste hasta y≈440).
   - Juego: No hay señal.
893. [baja] Mobiliario — bolardos
   - Captura: Bolardos negros (x≈465–475, y≈420–450 y x≈740–750, y≈430–470).
   - Juego: Sin bolardos.
**Vista #84** — 05_Tramo_sur_hacia_Don_Diego_Lopez.jpg (mayo de 2024) · hoja a_084.jpg

894. [alta] Mobiliario — barrera que cruza la calle delante de la cámara
   - Captura: La calle está despejada delante de la cámara: calzada de losas, coches aparcados a la izquierda y la tapia a la derecha (x≈350–1440, y≈280–450).
   - Juego: Una barra negra gruesa cruza toda la imagen (x≈345–1440, y≈292–345) desde un poste negro (x≈428–492, y≈330–445), con una lámina blanca debajo (x≈360–1440, y≈350–370).
895. [media] Color de fachada — lado derecho de la calle
   - Captura: Tapia o fachada encalada blanca (x≈830–1440, y≈0–600).
   - Juego: Fachada beis (x≈805–1440, y≈0–693).
896. [media] Huecos — lado derecho de la calle: huecos
   - Captura: Muro ciego salvo una puerta de madera con arco de medio punto (x≈880–915, y≈310–445).
   - Juego: Ventanas con contraventanas verdes (x≈980–1230, y≈0–190), un balcón con barandilla negra (x≈870–935, y≈210–290) y una ventana con reja negra (x≈1000–1135, y≈300–520).
897. [media] Huecos — casa del primer plano izquierdo
   - Captura: Portón de madera de dos hojas con recercado ocre (x≈150–300, y≈320–500), ventana con reja (x≈375–405, y≈340–430) y dos balcones de forja negra (x≈183–290, y≈225–290 y x≈370–418, y≈270–310).
   - Juego: Puerta de cochera blanca enrollable (x≈35–240, y≈310–475), ventanas sin balcón (x≈100–200, y≈145–250 y x≈300–345, y≈220–280) y una ventana con reja (x≈300–350, y≈335–390).
898. [media] Detalles de fachada — casa del primer plano izquierdo: recercados
   - Captura: Recercados, impostas y cornisa pintados de ocre sobre fachada crema (x≈0–445, y≈130–520).
   - Juego: Fachada beis lisa con recercados claros finos (x≈0–370, y≈60–480).
899. [media] Zócalo — lado derecho de la calle: zócalo
   - Captura: Zócalo pintado de amarillo ocre a lo largo de la base (x≈830–1440, y≈380–693).
   - Juego: Sin zócalo amarillo: la fachada beis llega al suelo (x≈1000–1440, y≈450–693).
900. [media] Otros — bastidor con ruedas en mitad de la calle
   - Captura: Calzada libre en el centro (x≈690–950, y≈420–640).
   - Juego: Un bastidor sin carrocería con cuatro ruedas y una rueda de repuesto encima, en mitad de la calzada (x≈715–940, y≈430–630).
901. [baja] Mobiliario — postes blancos
   - Captura: Sin postes en la calzada ni junto a la tapia.
   - Juego: Postes blancos rectangulares (x≈380–455, y≈470–693; x≈637–652, y≈395–600; x≈1155–1190, y≈400–650).

### Calle Pozo Dulce

**Vista #85** — 02_Desde_Plaza_Vieja_hacia_el_sur.jpg (mayo de 2024) · hoja a_085.jpg

902. [media] Geometría — casa de la derecha: altura
   - Captura: Casa alta: el alero queda en y≈30–90 y hay mucha pared por encima de la ventana (x≈930–1440, y≈80–365).
   - Juego: Casa más baja: el alero queda en y≈200–280 y apenas hay pared sobre las ventanas (x≈800–1440, y≈260–360).
903. [media] Huecos — casa del primer plano izquierdo: planta baja
   - Captura: Ventana con reja de hierro negra en una pared lisa (x≈390–485, y≈350–505); no hay puerta grande en primer plano.
   - Juego: Portón de madera clara de dos hojas con cristales, en un marco blanco (x≈210–500, y≈355–693), y una ventanita azul a su izquierda (x≈105–190, y≈440–495).
904. [media] Huecos — casa de la derecha: ventana principal
   - Captura: Ventana con barrotes blancos y persiana verde, con un guardapolvo moldurado encima (x≈1110–1260, y≈365–550).
   - Juego: Ventana con reja de barrotes negros, sin guardapolvo (x≈1280–1440, y≈360–605).
905. [media] Huecos — casa de la derecha: tramo hacia el fondo
   - Captura: Pared blanca lisa sin huecos (x≈790–930, y≈200–600).
   - Juego: Una ventana con reja negra (x≈885–935, y≈350–490) y una puerta de cochera blanca (x≈830–865, y≈335–470).
906. [media] Cubierta — casa de la derecha: tejado
   - Captura: Alero de teja vieja de color gris parduzco (x≈780–1440, y≈0–280).
   - Juego: Tejado de teja naranja vivo con alero festoneado (x≈800–1440, y≈190–330).
907. [baja] Detalles de fachada — placa con el nombre de la calle
   - Captura: Placa de calle en la esquina de la casa derecha (x≈890–918, y≈230–270).
   - Juego: No hay placa.
908. [baja] Acera y bordillo — bordillo derecho
   - Captura: Bordillo sin pintar (x≈750–900, y≈370–600).
   - Juego: Línea amarilla pintada junto al bordillo derecho (x≈790–840, y≈430–530).
909. [baja] Vegetación — matas de flores amarillas
   - Captura: Sin plantas junto a la casa de la derecha (x≈1040–1220, y≈600–693).
   - Juego: Matas con flores amarillas en primer plano a la derecha (x≈1040–1220, y≈600–693).
910. [baja] Mobiliario — farol de pared de la fachada izquierda
   - Captura: Farol de brazo en la fachada izquierda (x≈605–650, y≈180–250).
   - Juego: No hay farol en esa fachada (x≈580–680, y≈150–280).
911. [baja] Mobiliario — señal de dirección prohibida de la fachada derecha
   - Captura: Señal roja de dirección prohibida fijada en la fachada (x≈988–1072, y≈260–340).
   - Juego: No hay señal (x≈950–1100, y≈250–350).
**Vista #86** — 03_Tramo_sur_hacia_Plaza_Vieja.jpg (mayo de 2024) · hoja a_086.jpg

912. [alta] Calzada — explanada delante de la cámara
   - Captura: Toda la explanada es asfalto gris gastado, con grietas y parches, continuo hasta las casas (x≈0–1440, y≈410–693).
   - Juego: Una plaza peatonal de losas blancas y grises (x≈0–1000, y≈420–693), separada por un bordillo de la calle asfaltada de la derecha.
913. [media] Huecos — casas bajas de la izquierda: huecos
   - Captura: Ventanucos altos con contraventanas de madera marrón (x≈80–140, y≈240–285 y x≈270–300, y≈270–300), una ventana con reja y una puerta en recercados marrones (x≈30–160, y≈325–470 y x≈255–315, y≈345–390).
   - Juego: Solo dos ventanas con reja en la planta baja (x≈0–75, y≈355–445 y x≈218–275, y≈350–415); sin ventanucos altos ni puerta.
914. [media] Huecos — casa del centro con galería
   - Captura: Casa de dos plantas con pilares de mampostería y una galería abierta en la planta alta (x≈330–500, y≈215–420), puerta con arco (x≈350–385, y≈335–390).
   - Juego: Casa blanca lisa de dos plantas con ventanas con reja y macetas (x≈315–490, y≈215–410); sin galería ni pilares de piedra.
915. [media] Huecos — casa blanca del fondo con cochera
   - Captura: Gran puerta de cochera metálica marrón (x≈615–705, y≈325–415) en una fachada encalada.
   - Juego: Casa blanca con dos ventanas con reja y jardineras (x≈530–585 y x≈660–710, y≈350–400); sin cochera.
916. [media] Huecos — casa del primer plano derecho
   - Captura: Pared lisa sin balcón ni ventana en la zona media y baja (x≈1080–1440, y≈190–480); solo una ventana arriba (x≈1150–1250, y≈0–100).
   - Juego: Balcón con barandilla negra (x≈1070–1260, y≈195–310) y ventana con reja negra en la planta baja (x≈1110–1235, y≈350–485).
917. [media] Huecos — segunda casa a la derecha: planta baja
   - Captura: Puerta de cochera blanca seccional (x≈925–1010, y≈310–450).
   - Juego: Ventana con reja negra (x≈955–1005, y≈350–425) y una puerta (x≈885–910, y≈350–420); sin cochera.
918. [media] Cubierta — casas bajas de la izquierda: tejado
   - Captura: Tejados de teja a un agua sobre las casas bajas (x≈0–340, y≈150–270).
   - Juego: Muro beis de remate plano, sin tejado visible (x≈0–315, y≈250–300).
919. [media] Cubierta — casa blanca del fondo: tejado
   - Captura: Solo se ve un remate fino de teja casi plano (x≈500–745, y≈262–278).
   - Juego: Tejado a cuatro aguas de teja naranja bien visible (x≈475–770, y≈280–330).
920. [media] Acera y bordillo — acera de la derecha
   - Captura: Acera con bordillo a lo largo de las casas de la derecha (x≈830–1440, y≈380–640).
   - Juego: Sin acera: el asfalto llega hasta el zócalo de las casas (x≈760–1440, y≈370–693).
**Vista #87** — 04_Tramo_al_sur_de_Avenida_de_la_Constitucion.jpg (mayo de 2024) · hoja a_087.jpg

921. [alta] Otros — explanada de la derecha
   - Captura: Solar de tierra con hierba y malas hierbas, rodeado por un bordillo curvo (x≈720–1440, y≈440–693).
   - Juego: Explanada pavimentada de losas blancas con bordillo (x≈760–1440, y≈400–693).
922. [media] Geometría — edificio rojo de la izquierda: longitud
   - Captura: La esquina del edificio rojo queda muy cerca, en x≈385 (y≈0–440); a su derecha ya se abre el cruce con la avenida.
   - Juego: La fachada roja sigue en perspectiva hasta x≈600 (y≈0–470), con la acera delante, antes de llegar al cruce.
923. [media] Geometría — chimenea de ladrillo del fondo
   - Captura: Chimenea alta de ladrillo destacando sobre los tejados (x≈975–990, y≈215–290).
   - Juego: No hay chimenea; en esa zona solo cielo y casas bajas (x≈950–1010, y≈200–330).
924. [media] Cubierta — remate del edificio rojo de la izquierda
   - Captura: Cornisa blanca moldurada que remata la fachada roja (x≈230–390, y≈0–120).
   - Juego: Alero de teja naranja (x≈470–600, y≈0–190).
925. [media] Vegetación — árbol podado del solar
   - Captura: Árbol desmochado con tronco alto en el solar (x≈950–1050, y≈240–495).
   - Juego: No hay árbol en esa zona (x≈900–1100, y≈240–500).
926. [media] Mobiliario — farolas de la avenida
   - Captura: Farolas altas de un solo brazo curvo (x≈535–570, y≈195–390 y x≈1000–1020, y≈215–300).
   - Juego: Farolas negras de doble brazo con lámparas planas (x≈1010–1160, y≈255–400).
927. [baja] Geometría — campanario del fondo
   - Captura: Campanario de una iglesia asomando al fondo (x≈660–672, y≈290–320).
   - Juego: No hay campanario; casas bajas (x≈655–735, y≈315–355).
928. [baja] Vegetación — palmera del fondo derecho
   - Captura: Árboles de hoja ancha al fondo derecho, sin palmeras (x≈1100–1250, y≈285–400).
   - Juego: Una palmera (x≈1190–1250, y≈310–360).
929. [baja] Mobiliario — señal de STOP de la esquina
   - Captura: Señal de STOP sobre un poste en la esquina (x≈730–760, y≈335–450).
   - Juego: No hay señal de STOP (x≈700–800, y≈330–450).
**Vista #88** — 05_Giro_del_extremo_sur.jpg (mayo de 2024) · hoja a_088.jpg

930. [alta] Geometría — nave y tapia de la izquierda
   - Captura: Esquina alta de una nave, blanca con una franja azul vertical, que sube por encima del borde superior (x≈150–400, y≈0–660), y una tapia alta que sigue hasta x≈620 (remate en y≈240–300).
   - Juego: Un muro blanco exento y bajo (remate en y≈275–330) desde x≈70 hasta x≈660, con una nave gris más baja detrás (x≈0–630, y≈255–375); no hay esquina alta de nave ni franja azul.
931. [media] Cubierta — bloque blanco de la derecha: remate
   - Captura: Cubierta plana con antepechos de balaustres blancos (x≈1105–1440, y≈195–290).
   - Juego: Alero de teja naranja (x≈1105–1440, y≈270–305).
932. [media] Vegetación — árboles de la mediana
   - Captura: Mediana con bordillo y árboles podados de tronco alto (x≈835–1000, y≈265–500).
   - Juego: Una banda de acera plana sin árboles en ese tramo (x≈750–1100, y≈370–693); solo unos arbustos redondos bajos más al fondo (x≈975–1025, y≈340–360).
933. [media] Mobiliario — contenedores de la acera izquierda
   - Captura: Contenedor verde grande, contenedores azules y uno marrón junto a la acera izquierda (x≈545–665, y≈400–600).
   - Juego: No hay contenedores (x≈540–680, y≈380–600).
934. [media] Mobiliario — farola de la avenida
   - Captura: Farola alta de un solo brazo (x≈1100–1165, y≈215–390).
   - Juego: Farola negra de doble brazo con lámparas planas (x≈1055–1200, y≈215–405).
935. [baja] Mobiliario — contenedores de reciclaje del fondo
   - Captura: Dos contenedores de reciclaje tipo iglú, verde y blanco (x≈755–810, y≈360–405).
   - Juego: No hay contenedores en ese punto.

### Calle Pozo Pajares

**Vista #89** — 02_Tramo_oeste_hacia_Atras.jpg (mayo de 2024) · hoja a_089.jpg

936. [alta] Geometría — edificación detrás de la tapia izquierda
   - Captura: Casas y cobertizos bajos con tejados de teja y de fibrocemento ondulado, a poca altura sobre la tapia (x≈170–640, y≈260–335).
   - Juego: Una gran nave industrial gris claro con puertas azules y ventanas corridas, mucho más alta (x≈0–690, y≈250–385).
937. [alta] Otros — parcela de la derecha
   - Captura: Solar con hierba y matorral verde alto (x≈830–1440, y≈355–560).
   - Juego: Explanada pavimentada de losas blancas con unas pocas matas sueltas (x≈830–1440, y≈365–693).
938. [media] Geometría — posición de la tapia izquierda y su acera
   - Captura: La base de la tapia va de x≈0, y≈560 a x≈640, y≈375, con una acera ancha delante (x≈0–690, y≈375–600) y la calzada a continuación.
   - Juego: La tapia está mucho más cerca del eje de la calle: su base va de x≈380, y≈693 a x≈750, y≈375 y ocupa todo el primer plano izquierdo, con solo una acera estrecha delante (x≈380–770).
939. [media] Vegetación — árboles de la derecha
   - Captura: Varias palmeras detrás de la valla (x≈840–1440, y≈310–375).
   - Juego: Un gran árbol de copa redonda de hoja ancha en la explanada (x≈1115–1415, y≈240–410) y solo una palmera lejana (x≈950–975, y≈275–355).
940. [media] Muros y vallas — valla del solar de la derecha
   - Captura: Valla de malla metálica oxidada con postes, a lo largo de toda la acera derecha (x≈830–1440, y≈355–500).
   - Juego: No hay valla: la explanada queda abierta a la acera (x≈830–1440, y≈365–500).
941. [media] Muros y vallas — tapia de la izquierda
   - Captura: Tapia vieja de mampostería de piedra irregular, encalada en gris blanquecino con manchas (x≈0–640, y≈315–560).
   - Juego: Muro de ladrillos regulares redondeados de color tostado y marrón (x≈0–755, y≈350–693).
**Vista #90** — 03_Desde_la_union_oeste_hacia_San_Gines.jpg (mayo de 2024) · hoja a_090.jpg

942. [alta] Geometría — edificio de la esquina izquierda
   - Captura: Construcción vieja de una planta, encalada, con alero de teja (remate en y≈200–330) y una chimenea de ladrillo (x≈340–405, y≈165–220).
   - Juego: Nave industrial gris claro de gran altura que sale por el borde superior (x≈0–720, y≈0–620).
943. [alta] Geometría — hilera de casas de ladrillo del lado derecho
   - Captura: La tapia encalada sigue sin casas hasta el fondo (x≈770–930, y≈300–480).
   - Juego: Hilera de casas bajas con fachada de ladrillo rojo y tejado de teja naranja (x≈815–930, y≈265–400).
944. [media] Geometría — tapia de la derecha: altura
   - Captura: Tapia alta con albardilla de teja: su remate baja desde y≈130 en el borde derecho hasta y≈330 en x≈770.
   - Juego: Muro más bajo: su remate va de y≈230 en el borde derecho a y≈320 en x≈930.
945. [media] Huecos — edificio de la esquina izquierda: huecos
   - Captura: Muro ciego encalado con una sola puerta metálica verde bajo un tejadillo (x≈80–190, y≈310–445).
   - Juego: Dos filas de ventanas corridas y puertas azules (x≈20–40, x≈530–600 y x≈665–680, y≈340–545).
946. [media] Huecos — tapia de la derecha: puerta
   - Captura: Tapia sin puertas (x≈770–1440, y≈300–570).
   - Juego: Puerta enrollable marrón (x≈985–1055, y≈340–445).
947. [media] Acera y bordillo — acera de la izquierda
   - Captura: Acera de baldosa color ladrillo (x≈80–560, y≈440–550).
   - Juego: Acera de losas gris claro (x≈0–720, y≈420–693).
948. [media] Mobiliario — poste de farola en la esquina izquierda
   - Captura: En la esquina no hay poste; solo la arista del edificio y una bajante (x≈300–420, y≈0–500).
   - Juego: Poste negro alto de farola en primer plano (x≈325–375, y≈0–665).
949. [baja] Color de fachada — tapia de la derecha: enlucido
   - Captura: Encalado desconchado con grandes manchas ocres y de ladrillo a la vista (x≈1030–1440, y≈180–560).
   - Juego: Enlucido gris claro uniforme, sin desconchones (x≈930–1440, y≈300–575).
950. [baja] Detalles de fachada — bajante de la tapia derecha
   - Captura: Bajante vertical gris en la tapia (x≈995–1020, y≈190–540).
   - Juego: Sin bajante.
951. [baja] Mobiliario — farol de pared al fondo de la tapia izquierda
   - Captura: Farol de brazo en lo alto de la tapia izquierda, al fondo (x≈620–640, y≈280–320).
   - Juego: En ese punto está la fachada de la nave, sin farol (x≈600–700, y≈260–340).
952. [baja] Mobiliario — farol de la tapia derecha
   - Captura: No hay farol en la tapia derecha.
   - Juego: Farol negro de brazo en el muro (x≈1205–1275, y≈335–380).
**Vista #91** — 04_Desde_San_Gines_hacia_el_oeste.jpg (mayo de 2024) · hoja a_091.jpg

953. [media] Huecos — construcción de la izquierda: hueco principal
   - Captura: Gran portón de cochera de tablas de madera marrón en diagonal, en un recercado blanco (x≈270–445, y≈310–520).
   - Juego: Dos ventanas con persiana blanca en recercados blancos (x≈30–255, y≈350–580 y x≈540–610, y≈350–475); sin portón.
954. [media] Huecos — casa de la esquina derecha: planta alta
   - Captura: Voladizo curvo continuo que dobla la esquina, con barandilla negra (x≈920–1440, y≈140–240).
   - Juego: Balcones sueltos con barandilla negra (x≈955–1345, y≈220–330) y una ventana con persiana.
955. [media] Zócalo — construcción de la izquierda
   - Captura: Encalado hasta el suelo, sin zócalo (x≈60–520, y≈430–530).
   - Juego: Zócalo gris alto de borde ondulado (x≈0–640, y≈470–693).
956. [media] Cubierta — construcción de la izquierda: tejado
   - Captura: Solo una albardilla fina de teja sobre el muro encalado (x≈80–525, y≈225–260).
   - Juego: Tejado de teja naranja muy visible con alero festoneado (x≈0–655, y≈165–325).
957. [media] Cubierta — casa de la esquina derecha: remate
   - Captura: Terraza plana con barandilla negra corrida como remate, sin alero de teja (x≈930–1440, y≈90–140).
   - Juego: Alero de teja naranja a lo largo de todo el edificio (x≈910–1440, y≈20–275).
958. [media] Vegetación — buganvilla de la casa de la esquina derecha
   - Captura: Buganvilla de flores rosas sobre la barandilla de la planta alta (x≈930–1440, y≈0–230).
   - Juego: Sin plantas trepadoras (x≈910–1440, y≈0–330).
959. [baja] Detalles de fachada — hornacina con imagen religiosa
   - Captura: Hornacina o azulejo con una imagen religiosa en la planta alta (x≈1310–1375, y≈105–195).
   - Juego: No hay hornacina; ventana con persiana (x≈1215–1315, y≈145–235).
960. [baja] Calzada — franja del primer plano
   - Captura: Franja de adoquín de granito en primer plano (x≈150–1440, y≈620–693).
   - Juego: Asfalto hasta el borde inferior (x≈520–1440, y≈600–693).
961. [baja] Vegetación — palmera tras la casa de la izquierda
   - Captura: Solo cielo sobre la construcción de la izquierda (x≈540–610, y≈100–290).
   - Juego: Una palmera alta (x≈540–610, y≈105–290).
962. [baja] Mobiliario — señal de prohibido aparcar del portón
   - Captura: Placa de prohibido aparcar junto al portón (x≈408–426, y≈328–352).
   - Juego: Sin placa.

### Calle Túnel

**Vista #92** — 02_Desde_Estacada_hacia_el_Ayuntamiento.jpg (octubre de 2021) · hoja a_092.jpg

963. [alta] Color de fachada — edificio de la derecha: planta baja
   - Captura: Muro desconchado con el ladrillo rojizo a la vista y restos de enlucido ocre (x≈930–1440, y≈190–693).
   - Juego: Superficies blancas y grises lisas (x≈780–1440, y≈0–693).
964. [media] Geometría — edificio ocre de la izquierda: altura
   - Captura: La fachada ocre sube por encima del borde superior en todo su ancho (x≈0–640, y≈0); no se ve tejado y el cielo solo empieza a la derecha de x≈640.
   - Juego: El edificio es más bajo: su alero de teja naranja se ve contra el cielo (x≈440–665, y≈0–200) y hay cielo encima de x≈560.
965. [media] Huecos — edificio ocre de la izquierda: huecos
   - Captura: Muro casi ciego: una sola ventana alta con reja negra en la planta baja (x≈435–535, y≈255–535) y ninguna ventana encima.
   - Juego: Dos ventanas con persiana marrón en la planta alta (x≈330–465, y≈0–220 y x≈540–580, y≈170–275) y dos ventanas con reja en la baja (x≈330–468, y≈350–545 y x≈545–582, y≈350–440).
966. [media] Huecos — edificio de la derecha: huecos de la planta baja
   - Captura: Una hilera de huecos pequeños en celosía de ladrillo (x≈940–1440, y≈310–360) y pared sin acristalar debajo.
   - Juego: Gran cerramiento acristalado con montantes blancos y una franja naranja vertical (x≈780–1440, y≈320–693).
967. [media] Detalles de fachada — edificio de la derecha: panel horizontal
   - Captura: No hay ningún panel ni marquesina; arriba, fachada blanca con ventanas (x≈760–900, y≈0–350) y muro de ladrillo (x≈930–1440).
   - Juego: Gran panel blanco acanalado horizontal a lo largo de la fachada (x≈760–1440, y≈0–335).
968. [baja] Detalles de fachada — edificio ocre de la izquierda: recuadro moldurado
   - Captura: Gran recuadro rehundido con moldura alrededor de la ventana (x≈380–550, y≈125–590).
   - Juego: Pared ocre lisa sin recuadro.
969. [baja] Calzada — canaleta central del pavimento
   - Captura: Franja central de piezas más oscuras a lo largo de la calle (x≈705–735, y≈380–693).
   - Juego: Losas grises uniformes sin franja central (x≈600–760, y≈380–693).
970. [baja] Vegetación — macetas al pie de la fachada izquierda
   - Captura: Sin macetas en la acera (x≈350–520, y≈480–640).
   - Juego: Dos macetas con flores rojas y rosas (x≈370–500, y≈490–620).
971. [baja] Muros y vallas — vallas de obra de la derecha
   - Captura: Vallas metálicas de obra a lo largo del lado derecho (x≈740–1100, y≈380–693).
   - Juego: Sin vallas.
**Vista #93** — 03_Desde_Plaza_de_Espana_hacia_el_norte.jpg (marzo de 2009) · hoja a_093.jpg

972. [media] Huecos — edificio de la izquierda: huecos
   - Captura: Ventana alta con reja negra (x≈490–555, y≈255–510) y otra ventana arriba (x≈655–670, y≈145–200).
   - Juego: Muro ciego sin ningún hueco (x≈0–750, y≈0–693).
973. [media] Huecos — casa de la derecha: planta baja
   - Captura: Puerta alta de madera con cuarterones de cristal (x≈1110–1155, y≈290–500) dentro de un recercado blanco moldurado (x≈1080–1175, y≈235–510).
   - Juego: Ventana con persiana blanca enrollable (x≈1125–1245, y≈350–525).
974. [media] Detalles de fachada — edificio de la izquierda: acabado y cornisa
   - Captura: Fachada blanca almohadillada en grandes sillares lisos de juntas finas, con cornisa de ménsulas arriba (x≈600–750, y≈0–250).
   - Juego: Paramento de ladrillos o bloques crema redondeados con juntas hundidas, sin cornisa (x≈0–750, y≈0–693).
975. [media] Calzada — pavimento de la calzada
   - Captura: Adoquín de granito gris oscuro de piezas casi cuadradas (x≈550–1300, y≈370–693).
   - Juego: Adoquín rectangular gris claro colocado a soga (x≈200–1250, y≈375–693).
976. [baja] Detalles de fachada — toldo de la casa de la derecha
   - Captura: Sin toldo (x≈960–1050, y≈160–240).
   - Juego: Toldo a rayas rojas y blancas (x≈970–1045, y≈170–230).
977. [baja] Detalles de fachada — casa blanca del fondo
   - Captura: Pilastras y cornisas pintadas de amarillo ocre y puertas verdes (x≈750–965, y≈225–380).
   - Juego: Casa blanca lisa sin molduras ocres (x≈770–935, y≈270–385).
978. [baja] Acera y bordillo — bordillo derecho
   - Captura: Bordillo pintado de amarillo (x≈1000–1100, y≈500–600).
   - Juego: Bordillo blanco (x≈1000–1200, y≈450–650).
**Vista #94** — 04_Cruce_con_Pajares.jpg (octubre de 2021) · hoja a_094.jpg

979. [alta] Cámara — posición de la cámara del juego
   - Captura: La cámara está ya dentro de la boca de la calle Pajares: sus fachadas arrancan en los bordes de la imagen y fugan hacia el centro (ventana con reja y señal de dirección prohibida a la izquierda, x≈210–440; portón de cochera a la derecha, x≈1170–1430).
   - Juego: La cámara está más atrás, en el cruce: a ambos lados se ven de frente las fachadas de las casas de las esquinas, con balcones y ventanas (x≈0–560 y x≈1080–1440), y la calle Pajares solo aparece en el centro (x≈560–1080).

### Avenida de San Ginés

**Vista #95** — 02_Entrada_occidental_junto_al_parque.jpg (mayo de 2024) · hoja a_095.jpg

980. [alta] Geometría — gran edificio de la izquierda
   - Captura: Gran edificio institucional de dos plantas, crema/ocre con remates rojizos, toldos azules y una arquería en la planta baja (x≈0–545, y≈205–345).
   - Juego: Una nave blanca de una planta con tejado de teja naranja (x≈0–245, y≈210–415) y un edificio blanco de dos plantas con tejado de teja (x≈245–575, y≈275–380); sin arquería.
981. [media] Color de fachada — gran edificio de la izquierda: color
   - Captura: Fachada crema/ocre con franjas y arcos rojizos (x≈0–545, y≈205–345).
   - Juego: Fachadas blancas (x≈0–575, y≈240–415).
982. [media] Cubierta — construcción blanca de la derecha: remate
   - Captura: Tapia alta encalada de remate plano y sin teja (x≈760–1440, y≈185–200).
   - Juego: Casa de una planta con tejado de teja naranja a la vista (x≈750–1440, y≈265–330), más baja.
983. [media] Marcas viales — líneas de la avenida
   - Captura: Asfalto sin marcas viales visibles (x≈300–700, y≈350–600).
   - Juego: Línea central discontinua y línea de borde blancas (x≈355–690, y≈365–450).
984. [media] Acera y bordillo — frente de la construcción de la derecha
   - Captura: Acera estrecha junto a la tapia (x≈700–810, y≈380–470) y calzada asfaltada delante, donde aparca el camión (x≈700–1440, y≈470–693).
   - Juego: Plataforma ancha de losas blancas con bordillo (x≈700–1440, y≈370–610).
985. [media] Muros y vallas — verja del edificio de la izquierda
   - Captura: Verja metálica verde sobre un murete bajo, delante del edificio (x≈160–530, y≈330–350).
   - Juego: Sin verja ni murete (x≈160–530, y≈370–420).
986. [baja] Vegetación — árboles del fondo de la avenida
   - Captura: Árboles de hoja ancha y pinos al fondo, sin palmeras (x≈540–700, y≈275–345).
   - Juego: Palmeras (x≈455–475, y≈290–305 y x≈600–640, y≈290–345) entre árboles redondos.
987. [baja] Mobiliario — farol de la tapia derecha
   - Captura: Farol de brazo en lo alto de la tapia blanca (x≈1255–1330, y≈200–275).
   - Juego: En esa zona solo hay tejado y cielo, sin farol (x≈1230–1350, y≈190–300).
**Vista #96** — 03_Tramo_central_hacia_Medellin.jpg (mayo de 2024) · hoja a_096.jpg

988. [alta] Color de fachada — bloque de viviendas de la derecha
   - Captura: Fachada enlucida crema/beis (x≈900–1260, y≈0–420).
   - Juego: Fachada de ladrillo rojo visto (x≈900–1255, y≈20–465).
989. [alta] Color de fachada — edificio del borde derecho
   - Captura: Fachada granate/rojo oscuro (x≈1255–1440, y≈0–440).
   - Juego: Fachada blanca (x≈1255–1440, y≈0–510).
990. [alta] Vegetación — suelo del parque de la izquierda
   - Captura: Suelo de tierra y grava clara con parterres de rosales y arbustos (x≈0–760, y≈360–600).
   - Juego: Césped verde continuo (x≈0–770, y≈370–693).
991. [media] Geometría — bloque de viviendas de la derecha: plantas
   - Captura: Cuatro plantas (baja y tres altas) (x≈900–1260, y≈0–420).
   - Juego: Tres plantas (x≈900–1255, y≈20–465).
992. [media] Huecos — bloque de viviendas de la derecha: balcones
   - Captura: Balcones corridos con barandilla en cada planta y aparatos de aire acondicionado (x≈920–1220, y≈30–300).
   - Juego: Ventanas sueltas de marco blanco y un solo balcón pequeño (x≈1095–1195, y≈270–325).
993. [media] Marcas viales — líneas de la avenida
   - Captura: Asfalto sin marcas viales (x≈380–1100, y≈350–693).
   - Juego: Línea central y línea de borde blancas (x≈760–850, y≈380–450 y x≈880–1440, y≈370–610).
994. [media] Vegetación — árboles del parque
   - Captura: Palmeras (x≈590–700, y≈235–340), un árbol de hoja morada (x≈330–420, y≈290–370) y árboles y arbustos variados.
   - Juego: Árboles de copa redonda y árboles altos de tronco fino, sin palmeras (x≈50–800, y≈0–415).
995. [baja] Detalles de fachada — toldo del edificio del borde derecho
   - Captura: Toldo a rayas verdes y blancas (x≈1340–1440, y≈125–205).
   - Juego: Toldo a rayas amarillas y blancas (x≈1265–1440, y≈120–205).
996. [baja] Mobiliario — farol de pared del borde derecho
   - Captura: Farol de brazo en la fachada (x≈1240–1300, y≈195–255).
   - Juego: Sin farol (x≈1230–1310, y≈180–270).
997. [baja] Mobiliario — farola junto al parque
   - Captura: En primer plano no hay farola (x≈600–770, y≈0–470): árboles y cielo.
   - Juego: Farola alta de brazo en el borde del parque (x≈605–770, y≈0–470).
998. [baja] Vehículos — coche bajo la cámara
   - Captura: Calzada libre delante de la cámara (x≈420–1120, y≈445–693).
   - Juego: El techo de un coche negro ocupa el primer plano central (x≈420–1120, y≈445–693).
**Vista #97** — 04_Extremo_oriental_hacia_el_parque.jpg (mayo de 2024) · hoja a_097.jpg

999. [alta] Color de fachada — casa de la izquierda
   - Captura: Fachada enlucida color rosa salmón con recercados blancos (x≈20–600, y≈0–510).
   - Juego: Fachada de ladrillo rojo visto (x≈0–575, y≈65–525).
1000. [alta] Color de fachada — edificio de la derecha
   - Captura: Fachada de ladrillo rojo visto (x≈835–1440, y≈0–693).
   - Juego: Fachada enlucida blanca (x≈805–1440, y≈0–693).
1001. [media] Color de fachada — edificios del fondo
   - Captura: Edificios y tapias blancos al fondo (x≈600–790, y≈285–415).
   - Juego: Casas de ladrillo rojo con tejado de teja (x≈575–780, y≈270–365).
1002. [media] Huecos — casa de la izquierda: planta baja
   - Captura: Gran puerta de cochera marrón (x≈393–535, y≈345–465) y ventana con contraventana/reja marrón (x≈240–340, y≈355–470).
   - Juego: Puerta con barrotes grises (x≈345–400, y≈355–445) y ventanas con persiana blanca (x≈85–210, y≈355–450 y x≈470–500, y≈350–395); sin cochera.
1003. [media] Cubierta — casa de la izquierda: remate
   - Captura: Cornisa blanca con pretil por encima, sin teja (x≈320–600, y≈0–210; la parte izquierda queda bajo el panel de Street View).
   - Juego: Alero de teja naranja a lo largo de la fachada (x≈0–575, y≈65–265).
1004. [media] Marcas viales — línea de borde de la calzada
   - Captura: Sin línea de borde a lo largo de la calzada (x≈150–800, y≈400–693).
   - Juego: Línea blanca continua de borde (x≈130–800, y≈380–693).
1005. [baja] Mobiliario — farola de la acera izquierda
   - Captura: Farola de farol negro tradicional sobre poste (x≈200–265, y≈240–515).
   - Juego: Sin farola en esa acera (x≈180–280, y≈240–520).
1006. [baja] Mobiliario — señal de paso de peatones
   - Captura: Señal de paso de peatones en la fachada derecha (x≈990–1025, y≈355–395).
   - Juego: Sin señal (x≈980–1070, y≈340–400).
1007. [baja] Muros y vallas — vallas de obra ante el edificio de la derecha
   - Captura: Vallas metálicas de obra, sacos y escombros a lo largo de la fachada de ladrillo (x≈790–1060, y≈380–693).
   - Juego: Sin vallas ni material de obra (la acera junto a la fachada blanca está despejada, x≈760–800, y≈380–450).
1008. [baja] Vehículos — furgoneta delante de la cámara
   - Captura: Calzada libre y vallas de obra en ese sitio (x≈780–1060, y≈400–693).
   - Juego: Una furgoneta blanca aparcada justo delante de la cámara tapa el primer plano derecho (x≈780–1230, y≈385–693).
**Vista #98** — 06_Giro_hacia_Medellin.jpg (mayo de 2024) · hoja a_098.jpg

1009. [alta] Color de fachada — edificio del primer plano izquierdo
   - Captura: Fachada de ladrillo rojo visto, en obras (x≈0–505, y≈0–693).
   - Juego: Fachada enlucida blanca con zócalo ocre (x≈0–500, y≈0–693).
1010. [alta] Color de fachada — casa de dos plantas a la izquierda
   - Captura: Fachada amarillo crema/ocre claro (x≈505–770, y≈0–470).
   - Juego: Fachada de ladrillo rojo visto (x≈500–775, y≈20–540).
1011. [media] Color de fachada — casa de la derecha
   - Captura: Fachada gris lila claro con recercados blancos (x≈1015–1305, y≈120–420).
   - Juego: Fachada blanca (x≈1015–1430, y≈185–450).
1012. [media] Huecos — edificio del primer plano izquierdo: planta alta
   - Captura: Balcón con barandilla gris (visible en x≈140–420, y≈165–280, bajo el panel de Street View).
   - Juego: Ventana con persiana y contraventanas marrones, sin balcón (x≈10–465, y≈0–210).
1013. [media] Huecos — casa de dos plantas a la izquierda: huecos
   - Captura: Dos balcones con balaustres blancos (x≈595–690, y≈160–255 y x≈705–770, y≈225–290) y una puerta con reja negra (x≈660–690, y≈320–420).
   - Juego: Un balcón pequeño con barandilla negra (x≈670–730, y≈260–325) y ventanas con persiana blanca (x≈565–615, y≈145–250 y y≈355–455); sin puerta visible.
1014. [media] Huecos — casa de la derecha: balcones
   - Captura: Ventanas con recercado blanco y sin balcones (x≈1050–1240, y≈220–375).
   - Juego: Dos balcones con barandilla negra (x≈1055–1095, y≈305–330 y x≈1200–1300, y≈280–325).
1015. [media] Cubierta — casa de dos plantas a la izquierda: remate
   - Captura: Cornisa blanca de remate plano, sin teja (x≈505–770, y≈0–200).
   - Juego: Alero de teja naranja (x≈480–775, y≈15–240).
1016. [media] Cubierta — casa de la derecha: remate
   - Captura: Pretil plano sin teja (x≈1015–1305, y≈120–210).
   - Juego: Tejado de teja naranja con alero (x≈1015–1430, y≈185–285).
1017. [media] Marcas viales — líneas de la calzada
   - Captura: Asfalto sin marcas viales (x≈700–1100, y≈380–693).
   - Juego: Línea central discontinua blanca (x≈720–850, y≈500–693) y líneas en el cruce del fondo (x≈805–850, y≈370–390).
1018. [baja] Detalles de fachada — toldo de la casa de dos plantas
   - Captura: Toldo de lona marrón sobre la ventana alta (x≈590–665, y≈80–130).
   - Juego: Sin toldo.
1019. [baja] Detalles de fachada — celosía de la tapia del borde derecho
   - Captura: Celosía de ladrillo en la tapia blanca (x≈1330–1410, y≈290–325).
   - Juego: En su lugar, una construcción con puerta verde y alero de teja (x≈1325–1440, y≈295–455).
1020. [baja] Vegetación — macetas
   - Captura: Sin macetas en las fachadas ni en la acera.
   - Juego: Macetas con flores en la ventana del primer plano (x≈170–410, y≈490–550), en la acera (x≈595–625, y≈475–510) y ante la casa de la derecha (x≈1305–1375, y≈420–455).
1021. [baja] Mobiliario — farola de la acera izquierda
   - Captura: Farola de farol negro sobre poste (x≈727–745, y≈280–370).
   - Juego: Sin farola en ese punto (x≈720–760, y≈270–380).
1022. [baja] Mobiliario — farola de la acera derecha
   - Captura: Farola de farol negro sobre poste delante de la casa de la derecha (x≈1180–1210, y≈275–370).
   - Juego: Sin farola (x≈1170–1220, y≈270–380).

### Calle San Ginés

**Vista #99** — 03_Tramo_norte_hacia_el_parque.jpg (mayo de 2024) · hoja a_099.jpg

1023. [alta] Cámara — cámara del juego bajo un tejado
   - Captura: Calle estrecha entre muros encalados: tapia lisa con remate de teja a la izquierda (x≈0–725, y≈120–693) y casas blancas con una ventana a la derecha (x≈850–1440); la calle fuga al fondo en el centro (x≈725–850).
   - Juego: La cámara está metida bajo un tejado: arriba se ve la cara inferior de las tejas (x≈0–1440, y≈0–280) y, delante, paredes muy cercanas (un escaparate con franjas de colores en x≈560–1270, y≈250–693, y una ventana con reja y macetas en x≈0–275, y≈370–650); no se ve la calle.
**Vista #100** — 04_Enlace_sur_con_Pozo_Pajares.jpg (mayo de 2024) · hoja a_100.jpg

1024. [alta] Cámara — cámara del juego dentro de la construcción de la izquierda
   - Captura: Cámara en medio de una calle estrecha empedrada: tapia crema con una ventana de reja a la izquierda (x≈0–645, y≈160–693) y casa crema con zócalo rosa a la derecha (x≈800–1440); la calle fuga hacia el centro (x≈645–800).
   - Juego: La cámara está dentro de la construcción de la izquierda: en la mitad izquierda se ve la cara inferior de un tejado de teja (x≈0–590, y≈0–330), un pasillo con una puerta marrón (x≈285–380, y≈350–465) y una arista de muro pegada a la cámara (x≈590–720, y≈0–693); la calle solo aparece a la derecha (x≈720–1440).
**Vista #118** — 05_Cruce_con_la_avenida_hacia_el_sur.jpg (mayo de 2024) · hoja a_118.jpg

1195. [alta] Geometría — lado izquierdo del cruce
   - Captura: Una tapia encalada larga y alta, ciega y de remate plano (x≈0–730, y≈100–520), con un farol en su extremo (x≈640–665, y≈270–305).
   - Juego: Un edificio blanco de tres plantas con tejado de teja y balcones (x≈100–565, y≈135–400) y una casa de una planta con tejado de teja naranja, ventanas con reja, faroles y zócalo de piedra (x≈280–800, y≈285–450).
1196. [media] Huecos — edificio de la derecha
   - Captura: Fila de viviendas de dos plantas con balcones de barandilla negra (x≈1075–1410, y≈305–335) y ventanas con reja en la planta baja (x≈1065–1130 y x≈1300–1400, y≈355–420).
   - Juego: Edificio con grandes escaparates y franjas de colores (x≈940–1440, y≈240–400) y un panel marrón (x≈1115–1165, y≈280–325); sin balcones ni rejas.
1197. [media] Cubierta — edificio de la derecha: tejado
   - Captura: Tejado de poca pendiente de teja oscura con una chimenea (x≈960–1440, y≈195–250; chimenea x≈1100–1110).
   - Juego: Cubierta plana con tramos cortos de alero de teja naranja (x≈955–1440, y≈240–285).
1198. [media] Marcas viales — líneas de la calzada
   - Captura: Asfalto sin marcas viales (x≈200–1440, y≈380–693).
   - Juego: Línea blanca a la izquierda (x≈0–250, y≈480–585) y línea central al fondo (x≈825–905, y≈365–395).
1199. [media] Acera y bordillo — frente de la tapia izquierda
   - Captura: Calzada asfaltada hasta casi el pie de la tapia, con una acera estrecha (x≈0–230, y≈480–560) y camiones aparcados.
   - Juego: Una explanada ancha de losas blancas con bordillo delante de las casas (x≈0–800, y≈390–560).
1200. [media] Vegetación — árboles del lado derecho
   - Captura: Solo un arbolito estrecho junto a la fachada (x≈1185–1210, y≈355–400).
   - Juego: Dos árboles grandes de copa redonda (x≈965–1050, y≈330–400 y x≈1115–1400, y≈310–465).
1201. [baja] Mobiliario — señal de dirección prohibida
   - Captura: No hay señal en ese punto (x≈1040–1090, y≈330–450).
   - Juego: Señal de dirección prohibida sobre un poste (x≈1055–1075, y≈335–450).
**Vista #119** — 02_Tramo_norte_hacia_Medellin.jpg (mayo de 2024) · hoja a_119.jpg

1202. [alta] Cámara — cámara del juego bajo un tejado
   - Captura: Cruce abierto: a la izquierda la esquina de una casa encalada con alero de teja (x≈0–570, y≈200–693); a la derecha, al otro lado, casas bajas blancas con zócalo y recercados granates, contenedores (x≈685–750) y una farola de fundición (x≈1080–1125, y≈255–510).
   - Juego: La cámara está bajo un tejado: la cara inferior de las tejas ocupa toda la mitad superior (x≈0–1440, y≈0–330) y alrededor hay paredes cercanas con ventanas y puertas negras (x≈0–1300, y≈300–600) sobre un suelo de losas; no se ven el cielo ni el cruce.

### Calle Extremadura

**Vista #101** — 04_Desde_el_extremo_opuesto.jpg (Fecha de toma no indicada) · hoja a_101.jpg

1025. [alta] Color de fachada — casa del primer plano izquierdo
   - Captura: Vivienda moderna blanca con muros de cerramiento grises y puertas gris oscuro (x≈0–470, y≈60–520).
   - Juego: Casa de ladrillo rojo visto (x≈0–210, y≈20–555).
1026. [media] Geometría — viviendas de la izquierda
   - Captura: Viviendas de dos plantas retranqueadas, con porche de teja delante (x≈0–480, y≈60–330).
   - Juego: Casas de una planta con tejado de teja naranja alineadas con la acera (x≈210–600, y≈190–440).
1027. [media] Huecos — casa del primer plano derecho
   - Captura: Pared alta lisa sin ventanas (x≈1020–1440, y≈0–420).
   - Juego: Cuatro ventanas cerradas con contraventanas y dos balconcillos (x≈1120–1410, y≈100–475).
1028. [media] Detalles de fachada — hilera de casas de la derecha: recercados
   - Captura: Ventanas y puertas con recercados de color rosa salmón sobre fachada blanca (x≈740–1020, y≈130–440).
   - Juego: Huecos con marcos blancos, sin recercados de color (x≈800–900, y≈170–420).
1029. [media] Marcas viales — líneas de la calzada
   - Captura: Asfalto sin marcas viales (x≈200–1000, y≈350–693).
   - Juego: Línea central blanca (x≈715–810, y≈365–693) y línea de borde (x≈20–660, y≈375–693).
1030. [media] Muros y vallas — cerramientos de las viviendas de la izquierda
   - Captura: Muretes grises con puertas metálicas gris oscuro y una cancela negra delante de las casas (x≈0–520, y≈300–520).
   - Juego: Sin cerramientos: las fachadas dan directamente a la acera (x≈210–600, y≈330–440).
1031. [media] Muros y vallas — murete del primer plano derecho
   - Captura: Murete chapado de mampostería con una verja metálica blanca encima (x≈1015–1440, y≈415–693).
   - Juego: Explanada de losas abierta, sin murete ni verja (x≈930–1440, y≈500–693).
1032. [baja] Vegetación — maceta del primer plano izquierdo
   - Captura: Sin plantas junto al muro gris (x≈60–140, y≈430–500).
   - Juego: Maceta con un arbusto recortado en cono (x≈65–130, y≈440–540).
1033. [baja] Mobiliario — farola de la acera derecha
   - Captura: Sin farola en esa acera (x≈800–920, y≈150–500).
   - Juego: Farola moderna de brazo (x≈810–910, y≈155–500).
**Vista #123** — 02_Desde_un_extremo_hacia_el_otro.jpg (mayo de 2024) · hoja a_123.jpg

1247. [alta] Geometría — lado izquierdo tras la primera casa
   - Captura: Una tapia blanca baja con una puerta metálica gris (x≈390–620, y≈270–520) y, detrás, una casa blanca de dos plantas con tejado de teja (x≈360–665, y≈200–330).
   - Juego: Un bloque blanco de tres plantas con balcones de barandilla blanca a la línea de la calle (x≈230–545, y≈0–520).
1248. [media] Color de fachada — casa del primer plano izquierdo
   - Captura: Fachada chapada de piedra beis/ocre con persiana gris (x≈0–270, y≈0–600).
   - Juego: Pared enlucida blanco grisácea (x≈0–230, y≈0–515).
1249. [media] Huecos — edificio grande de la derecha: planta alta
   - Captura: Ventana en arco sin balcón (x≈1030–1150, y≈30–190).
   - Juego: Balcón corrido con barandilla blanca (x≈1070–1440, y≈30–295).
1250. [media] Huecos — edificio grande de la derecha: planta baja
   - Captura: Pared blanca con zócalo beis, sin puertas, por detrás de la furgoneta (x≈1240–1440, y≈300–600).
   - Juego: Gran portón de madera de dos hojas con cristales (x≈1160–1410, y≈365–693) y un farol de pared (x≈975–1035, y≈315–365).
1251. [media] Detalles de fachada — edificio grande de la derecha: ladrillo
   - Captura: Franjas de ladrillo visto bajo la cornisa (x≈920–1440, y≈125–290), ventana en arco con rosca de ladrillo (x≈1030–1150, y≈30–190) y puerta enmarcada en ladrillo (x≈920–970, y≈325–395).
   - Juego: Fachada enlucida sin ningún ladrillo visto (x≈760–1440, y≈0–600).
1252. [media] Marcas viales — líneas de la calzada
   - Captura: Asfalto sin marcas viales (x≈330–830, y≈350–693).
   - Juego: Línea central blanca (x≈730–910, y≈370–693) y línea de borde (x≈120–680, y≈375–693).
1253. [media] Muros y vallas — cerramiento de la casa del primer plano izquierdo
   - Captura: Murete chapado de piedra con lamas metálicas gris oscuro encima y un pilar blanco con el número 1 (x≈110–415, y≈360–600).
   - Juego: Sin cerramiento: fachada de un bloque alineada con la acera (x≈230–545, y≈0–520).
1254. [baja] Vegetación — árbol tras el cerramiento izquierdo
   - Captura: Árbol o arbusto grande asomando sobre la valla (x≈215–400, y≈260–365).
   - Juego: No hay árbol (fachada del bloque en esa zona).
1255. [baja] Mobiliario — farola de la acera izquierda
   - Captura: Farola alta de báculo con luminaria redonda (x≈440–515, y≈90–555).
   - Juego: No hay farola (x≈430–530, y≈80–560).
**Vista #124** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_124.jpg

1256. [media] Geometría — vivienda de la izquierda
   - Captura: Vivienda retranqueada tras el cerramiento, con marquesina gris oscuro (x≈0–440, y≈200–300) y tejado de teja (x≈320–445, y≈150–245).
   - Juego: Casa de una planta con tejado de teja naranja (x≈0–300, y≈110–510) y un bloque blanco de dos plantas con balcones (x≈180–515, y≈150–445), ambos a la línea de la calle.
1257. [media] Color de fachada — casa crema con cochera del lado derecho
   - Captura: Fachada crema con puerta de cochera marrón y tejado a dos aguas (x≈820–970, y≈225–395).
   - Juego: Casas de ladrillo rojo visto con tejado naranja (x≈760–850, y≈290–395).
1258. [media] Huecos — casa del primer plano derecho
   - Captura: Balcón de forja negra (x≈1035–1195, y≈175–290), ventana con reja negra ornamentada (x≈1055–1170, y≈335–465) y un gran porche cerrado con reja negra (x≈1240–1440, y≈245–550).
   - Juego: Grandes ventanales grises (x≈1070–1440, y≈0–240) y puertas grises lisas (x≈1115–1310, y≈355–693 y x≈955–990, y≈350–500); sin rejas ni balcón.
1259. [media] Zócalo — casa del primer plano derecho
   - Captura: Zócalo chapado de piedra (x≈1060–1240, y≈440–510).
   - Juego: Sin zócalo de piedra (x≈840–1440, y≈420–600).
1260. [media] Marcas viales — líneas de la calzada
   - Captura: Asfalto sin marcas viales (x≈450–1000, y≈350–693).
   - Juego: Línea central blanca (x≈720–770, y≈365–693) y línea de borde (x≈0–690, y≈370–693).
1261. [media] Muros y vallas — cerramiento de la vivienda de la izquierda
   - Captura: Puertas y valla de lamas metálicas gris oscuro sobre un murete y pilares chapados de piedra (x≈30–600, y≈345–693).
   - Juego: Sin cerramiento: fachadas blancas a la línea de la acera (x≈0–515, y≈150–510).
1262. [baja] Vegetación — árbol tras el cerramiento izquierdo
   - Captura: Árbol frondoso detrás de la valla (x≈470–640, y≈255–340).
   - Juego: No hay árbol (x≈450–650, y≈240–350).

### Calle Carolina Coronado

**Vista #102** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_102.jpg

1034. [alta] Geometría — edificación tras el solar derecho
   - Captura: Una tapia blanca alta (x≈900–1270, y≈265–430) y, detrás, un edificio de dos plantas con terraza y aparatos de aire (x≈830–1165, y≈200–270).
   - Juego: Un grupo de casas blancas de dos plantas con cuerpos escalonados, tejadillos de teja y tres puertas de madera (x≈820–1350, y≈120–445).
1035. [alta] Otros — parcela del primer plano derecho
   - Captura: Solar de tierra con hierba seca, cerrado con malla metálica sobre postes de madera (x≈900–1440, y≈370–693).
   - Juego: Explanada pavimentada de losas blancas (x≈930–1440, y≈410–693).
1036. [media] Huecos — hilera de viviendas de la izquierda: primer plano
   - Captura: Ventana con reja negra en un recercado ocre (x≈280–415, y≈340–470) y, más adelante, puertas blancas de cochera bajo arcos (x≈455–610, y≈330–470).
   - Juego: Una persiana de cochera gris (x≈0–100, y≈335–640), una puerta gris de vidrio (x≈265–355, y≈350–520) y otra persiana gris (x≈415–500, y≈340–470).
1037. [media] Detalles de fachada — hilera de viviendas de la izquierda: molduras
   - Captura: Recercados y bandas horizontales de color ocre/amarillo y arcos ocres sobre las cocheras (x≈0–700, y≈100–470).
   - Juego: Fachada gris clara sin molduras de color (x≈0–700, y≈0–560).
1038. [media] Marcas viales — líneas de la calzada
   - Captura: Asfalto sin marcas viales (x≈260–1000, y≈380–693).
   - Juego: Dos líneas blancas continuas a lo largo de la calzada (x≈365–700 y x≈760–1030, y≈370–693).
1039. [baja] Detalles de fachada — rótulos del comercio de la derecha
   - Captura: Rótulos de peluquería en la tapia y en la fachada (x≈860–950, y≈310–345).
   - Juego: Sin rótulos (x≈830–950, y≈300–360).
1040. [baja] Acera y bordillo — bordillo izquierdo
   - Captura: Bordillo sin pintar (x≈420–600, y≈410–520).
   - Juego: Bordillo pintado de amarillo (x≈100–560, y≈440–693).
1041. [baja] Mobiliario — banco de la acera izquierda
   - Captura: Sin banco en la acera izquierda (x≈190–300, y≈470–590).
   - Juego: Banco blanco (x≈195–290, y≈480–580).
1042. [baja] Mobiliario — farola de la acera izquierda
   - Captura: Poste de farola gris en la acera izquierda (x≈220–245, y≈180–590).
   - Juego: Sin farola en esa acera (x≈200–260, y≈170–590).
**Vista #128** — 02_Desde_un_extremo_hacia_el_otro.jpg (mayo de 2024) · hoja a_128.jpg

1304. [alta] Geometría — fondo de la explanada izquierda
   - Captura: Una vivienda adosada blanca de dos plantas con tejado de teja y chimenea, de costado (x≈100–600, y≈90–440).
   - Juego: Un bloque blanco de tres plantas con balcones y tejado de teja (x≈330–640, y≈140–420) y, a su izquierda, casas de ladrillo rojo de dos plantas (x≈0–330, y≈160–415).
1305. [media] Color de fachada — casas del fondo derecho
   - Captura: Hilera de casas blancas (x≈740–940, y≈150–420).
   - Juego: Casas de ladrillo rojo visto en el tramo medio (x≈760–880, y≈230–380).
1306. [media] Huecos — casa del primer plano derecho: planta baja
   - Captura: Gran puerta de madera marrón con clavos (x≈1150–1245, y≈360–565), una ventana con reja negra (x≈970–1020, y≈335–460) y una puerta de cochera marrón (x≈890–930, y≈340–430).
   - Juego: Dos puertas grises lisas (x≈1070–1120, y≈350–460 y x≈1240–1360, y≈350–535) y una ventana con persiana (x≈975–1025, y≈345–415).
1307. [media] Huecos — casa del primer plano derecho: planta alta
   - Captura: Balcón con barandilla negra (x≈940–1030, y≈230–320) y ventanas con recercado (x≈1110–1255, y≈50–190).
   - Juego: Ventanal acristalado con un antepecho gris (x≈1010–1160, y≈170–325) y un panel marrón (x≈975–1025, y≈225–305); sin balcón de barandilla negra.
1308. [media] Zócalo — vivienda de la izquierda
   - Captura: Zócalo alto de plaqueta marrón rojiza (x≈0–600, y≈395–445).
   - Juego: Sin ese zócalo: el bloque blanco solo tiene una franja gris baja (x≈335–630, y≈395–420).
1309. [baja] Cubierta — casas de la derecha: tejadillos
   - Captura: Solo un tejadillo de teja pequeño (x≈880–935, y≈285–310).
   - Juego: Tejadillos de teja naranja largos sobre las plantas bajas (x≈910–970, y≈315–335 y x≈1150–1440, y≈90–320).
1310. [baja] Marcas viales — líneas de la calzada
   - Captura: Asfalto sin marcas viales (x≈600–900, y≈380–693).
   - Juego: Líneas blancas al fondo de la calzada (x≈720–840, y≈365–410).
1311. [baja] Vegetación — macetas de la acera derecha
   - Captura: Sin macetas en la acera derecha.
   - Juego: Macetas con flores ante las fachadas (x≈1120–1210, y≈440–500 y x≈945–970, y≈400–415).
**Vista #129** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_129.jpg

1312. [alta] Color de fachada — hilera de viviendas de la izquierda
   - Captura: Casas blancas encaladas (x≈0–690, y≈0–600).
   - Juego: Volúmenes de ladrillo rojo visto (x≈50–710, y≈0–600).
1313. [alta] Color de fachada — casa del primer plano derecho
   - Captura: Fachada crema clara con recercados y bandas marrón oscuro (x≈950–1440, y≈0–600).
   - Juego: Fachada de ladrillo rojo visto (x≈1005–1440, y≈0–445).
1314. [media] Huecos — viviendas de la izquierda: planta baja
   - Captura: Puerta de madera clara con el número 14 (x≈180–285, y≈330–565) y puertas de cochera de chapa marrón (x≈370–485, y≈340–500 y x≈595–615, y≈340–400).
   - Juego: Una puerta acristalada gris (x≈0–250, y≈360–693), una ventana con persiana blanca (x≈470–530, y≈355–495) y puertas estrechas blancas (x≈580–600, y≈350–460); sin cocheras marrones.
1315. [media] Huecos — casa del primer plano derecho: planta baja
   - Captura: Puerta de madera marrón de dos hojas bajo un dintel marrón (x≈1190–1305, y≈330–580) y una ventana con reja negra (x≈1000–1065, y≈335–460).
   - Juego: Puerta gris con barrotes (x≈1155–1220, y≈355–450) y persiana de cochera blanca (x≈1030–1065, y≈350–400).
1316. [media] Cubierta — tejadillo del primer plano izquierdo
   - Captura: Solo un tejadillo pequeño de teja más al fondo (x≈410–510, y≈260–305).
   - Juego: Alero de teja naranja muy grande en primer plano (x≈0–450, y≈110–295).
1317. [media] Marcas viales — líneas de la calzada
   - Captura: Asfalto sin marcas viales (x≈500–950, y≈360–693).
   - Juego: Línea blanca central continua (x≈735–815, y≈365–693) y línea de borde (x≈800–1300, y≈370–600).
1318. [baja] Detalles de fachada — colgadura del balcón de la derecha
   - Captura: Colgadura azul con una imagen de la Virgen colgada del balcón (x≈980–1040, y≈225–325).
   - Juego: Sin colgadura (x≈1000–1080, y≈270–330).
1319. [baja] Vegetación — macetas de la acera izquierda
   - Captura: Sin macetas en la acera izquierda (x≈330–600, y≈470–693).
   - Juego: Macetas con un cactus y flores en la acera (x≈335–475, y≈540–693).

### Calle Rosalía de Castro

**Vista #103** — 02_Desde_un_extremo_hacia_el_otro.jpg (mayo de 2024) · hoja a_103.jpg

1043. [alta] Color de fachada — segunda casa de la izquierda
   - Captura: Fachada blanca encalada (x≈380–620, y≈0–420).
   - Juego: Fachada de ladrillo rojo visto de dos plantas (x≈135–590, y≈0–470).
1044. [media] Huecos — casa del primer plano izquierdo: planta baja
   - Captura: Ventana con reja de forja negra y persiana marrón (x≈190–315, y≈325–520).
   - Juego: Portón de madera clara de dos hojas con cristales (x≈280–375, y≈365–585).
1045. [media] Huecos — casa del primer plano izquierdo: planta alta
   - Captura: Balcón con barandilla de forja negra (x≈170–370, y≈195–290) y ventana con persiana (x≈390–440, y≈160–245).
   - Juego: Sin balcón en la casa del primer plano: un tejadillo de teja naranja (x≈55–445, y≈215–315) y pared lisa encima.
1046. [media] Huecos — casas de la izquierda: cocheras
   - Captura: Puertas de cochera de chapa marrón (x≈395–430, y≈335–430 y x≈475–530, y≈335–415).
   - Juego: Puerta blanca con barrotes (x≈480–515, y≈355–465) y ventanas; sin cocheras marrones.
1047. [media] Huecos — casa del primer plano derecho: planta baja
   - Captura: Ventana con reja blanca (x≈1040–1145, y≈340–445), puerta blanca (x≈955–985, y≈345–460) y puerta de cochera blanca bajo un arco (x≈880–925, y≈345–440).
   - Juego: Ventanal acristalado oscuro (x≈1205–1440, y≈340–465), ventana con reja negra (x≈1030–1100, y≈350–440) y puerta de madera (x≈950–975, y≈355–440).
1048. [media] Detalles de fachada — hilera de viviendas de la derecha: recercados
   - Captura: Recercados, cornisa e impostas de color salmón/melocotón sobre fachada crema (x≈860–1440, y≈0–660).
   - Juego: Fachada gris clara uniforme sin recercados de color (x≈820–1440, y≈90–500).
1049. [media] Zócalo — casas de la izquierda
   - Captura: Zócalo de pizarra o piedra gris y ocre (x≈0–190, y≈480–560) y paños de pizarra en la fachada (x≈490–545, y≈195–325).
   - Juego: Zócalo gris liso (x≈0–440, y≈500–693); sin piedra.
1050. [media] Zócalo — casas de la derecha
   - Captura: Zócalo alto de color salmón en las plantas bajas (x≈920–1360, y≈440–620).
   - Juego: Zócalo de mampostería gris oscura (x≈880–1160, y≈385–500).
1051. [media] Marcas viales — líneas de la calzada
   - Captura: Asfalto sin marcas viales (x≈560–950, y≈360–693).
   - Juego: Dos líneas blancas continuas (x≈570–700 y x≈760–1180, y≈365–693).
1052. [baja] Mobiliario — señal del primer plano izquierdo
   - Captura: Señal redonda (de espaldas) sobre un poste en la acera (x≈85–220, y≈335–580).
   - Juego: Sin señal (x≈80–230, y≈330–590).
1053. [baja] Otros — escoba apoyada en la acera izquierda
   - Captura: Nada en ese punto de la acera (x≈180–250, y≈600–680).
   - Juego: Una escoba amarilla en la acera (x≈185–250, y≈600–675).
**Vista #104** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_104.jpg

1054. [alta] Cámara — cámara del juego bajo un porche de la acera izquierda
   - Captura: Cámara en el centro de la calle: hileras de viviendas blancas con balcones a la izquierda (x≈0–690) y casas crema con recercados ocres y cocheras blancas a la derecha (x≈740–1440); la calle fuga al centro (x≈690–740).
   - Juego: La cámara está bajo un porche en la acera izquierda: la cara inferior de un tejado de teja ocupa arriba a la izquierda (x≈0–740, y≈0–240), un pilar blanco cercano parte la imagen (x≈650–840, y≈0–693) y a la izquierda se ve un espacio cerrado con suelo de losas y puertas negras (x≈0–720, y≈240–693); la calle solo aparece a la derecha (x≈830–1440).
**Vista #105** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_105.jpg

1055. [alta] Cámara — cámara del juego pegada a las casas de la derecha
   - Captura: Cámara en el centro de la calle: casas crema con recercados ocres a la izquierda (x≈0–700) y casas blancas con recercados granates a la derecha (x≈740–1440); la calle fuga al centro (x≈700–740).
   - Juego: La cámara está pegada a la fachada de la derecha o dentro de ella: un voladizo blanco cercano tapa la parte superior (x≈300–830, y≈0–260), una pared ocupa el centro (x≈720–950, y≈0–693) y a la derecha se ve un recinto bajo tejado con suelo de losas (x≈950–1440, y≈0–693); la calle solo aparece a la izquierda (x≈0–720).

### Calle María Zambrano

**Vista #106** — 02_Desde_un_extremo_hacia_el_otro.jpg (mayo de 2024) · hoja a_106.jpg

1056. [media] Geometría — distancia de la fachada izquierda a la cámara
   - Captura: La cámara está en mitad de la calzada: la base de la fachada izquierda queda en y≈470 a la altura de x≈440 y el bordillo derecho llega al borde inferior en x≈960.
   - Juego: La fachada izquierda está mucho más cerca: su base llega al borde inferior en x≈450, el bordillo izquierdo pasa por x≈560 abajo y el derecho por x≈1330.
1057. [media] Color de fachada — casa del borde izquierdo
   - Captura: Fachada crema con impostas y molduras ocres (x≈0–240, y≈0–520).
   - Juego: Fachada gris clara uniforme (x≈0–400, y≈0–693).
1058. [media] Huecos — hilera de viviendas de la izquierda: planta baja
   - Captura: Ventana con reja blanca (x≈375–435, y≈335–410), puerta blanca (x≈480–510, y≈320–440) y puertas de cochera blancas (x≈525–565 y x≈575–600, y≈340–420).
   - Juego: Una persiana enrollable grande (x≈0–330, y≈320–693) y ventanales con marco gris (x≈495–580, y≈335–545); sin cocheras blancas.
1059. [media] Detalles de fachada — hilera de viviendas de la izquierda: molduras
   - Captura: Impostas blancas gruesas y recercados blancos marcados alrededor de las ventanas (x≈0–700, y≈100–330).
   - Juego: Fachadas lisas sin impostas ni recercados en relieve (x≈0–720, y≈0–600).
1060. [media] Cubierta — remate de las viviendas de la izquierda
   - Captura: Remate con cornisa y pretil blancos, sin teja a la vista (x≈300–700, y≈0–330).
   - Juego: Alero de teja naranja a lo largo de toda la hilera (x≈540–720, y≈0–330).
1061. [media] Acera y bordillo — acera del lado del campo
   - Captura: Acera estrecha de hormigón con bordillo, de ancho constante, pegada al campo (x≈745–1000, y≈365–693).
   - Juego: Explanada ancha de losas blancas entre el bordillo y el campo (x≈815–1440, y≈365–693).
1062. [media] Muros y vallas — valla del campo
   - Captura: Valla de malla metálica sobre postes a lo largo de la acera derecha (x≈750–1290, y≈350–693; postes en x≈900 y x≈1230).
   - Juego: Sin valla (x≈820–1440, y≈350–693).
1063. [media] Otros — campo del lado derecho
   - Captura: Campo arado de tierra marrón rojiza (x≈740–1440, y≈345–693).
   - Juego: Llanura lisa de color amarillo arena (x≈830–1440, y≈350–480).
1064. [baja] Vegetación — hierbas al pie de la valla
   - Captura: Franja de hierbas verdes entre la acera y el campo (x≈930–1200, y≈500–693).
   - Juego: Sin hierbas: losas hasta el campo.
1065. [baja] Vegetación — árboles al final de la calle
   - Captura: Ningún árbol junto al final de la calle (x≈800–930, y≈320–390).
   - Juego: Dos árboles de copa redonda al final de la calle, junto al campo (x≈820–915, y≈330–380).
1066. [baja] Mobiliario — farol de pared de la fachada izquierda
   - Captura: Sin farol en esa zona de la fachada (x≈540–620, y≈300–370).
   - Juego: Farol negro de brazo (x≈560–615, y≈315–365).
1067. [baja] Otros — bombona en la acera izquierda
   - Captura: Nada en ese punto de la acera (x≈600–640, y≈440–500).
   - Juego: Una bombona naranja (x≈612–630, y≈455–495).
**Vista #107** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_107.jpg

1068. [alta] Cámara — cámara del juego pegada a la fachada izquierda
   - Captura: Cámara en mitad de la calzada: la hilera de viviendas de la izquierda se ve en perspectiva con su acera (base de la fachada en y≈470 a x≈440), la calle fuga en x≈700–740 y a la derecha está el campo arado tras una valla.
   - Juego: La cámara está sobre la acera izquierda, pegada a la fachada: la cara inferior de un balcón ocupa arriba a la izquierda (x≈0–700, y≈0–260), una persiana a un par de metros ocupa abajo a la izquierda (x≈0–520, y≈280–693) y el bordillo izquierdo pasa por el centro de la imagen (x≈700–730, y≈360–693).
**Vista #108** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_108.jpg

1069. [alta] Cámara — cámara del juego dentro de una construcción de ladrillo
   - Captura: Cámara en mitad de la calle: campo arado con valla a la izquierda (x≈0–720), calzada al centro y hilera de viviendas blancas con recercados y cocheras blancas a la derecha (x≈750–1440).
   - Juego: La cámara está metida en una construcción de ladrillo rojo: un muro de ladrillo con dos paneles grises ocupa el centro (x≈600–1080, y≈0–570), a la derecha se ve un recinto bajo un tejado de teja con suelo de losas (x≈1080–1440) y un murete cercano en primer plano (x≈600–840, y≈570–693); la calle y el campo solo aparecen a la izquierda (x≈0–600).

### Calle Dulce Chacón

**Vista #109** — 02_Desde_un_extremo_hacia_el_otro.jpg (mayo de 2024) · hoja a_109.jpg

1070. [alta] Geometría — edificio blanco del lado izquierdo (primer plano)
   - Captura: Fachada blanca retranqueada: entre ella y la calzada hay una acera y una fila de coches aparcados; ocupa x≈0–610 y la calzada se ve en el centro inferior (x≈330–1000).
   - Juego: Un muro blanco pegado a la cámara ocupa x≈135–735 de arriba abajo; entre el muro y la calzada solo queda una acera estrecha (x≈690–850) y no hay banda de aparcamiento.
1071. [alta] Color de fachada — hilera de adosados del lado derecho (casas cercanas)
   - Captura: Enfoscado salmón-rosado en planta baja y crema con recercados salmón en la alta (x≈760–1440).
   - Juego: Ladrillo visto rojo anaranjado con remates blancos (x≈890–1440); solo el tramo del fondo (x≈760–890) es blanco.
1072. [media] Geometría — borde izquierdo de la imagen (x≈0–135)
   - Captura: Sigue la misma fachada blanca del edificio izquierdo, con una ventana alta (x≈0–25, y≈270–570).
   - Juego: El muro termina en x≈135 y detrás se ve un espacio abierto pavimentado en gris claro (y≈400–693) y otra edificación gris con cierre metálico (y≈330–395), tejado de teja roja y una chimenea blanca (x≈70–130, y≈255–312).
1073. [media] Huecos — huecos del edificio blanco izquierdo
   - Captura: Ventanas grandes con carpintería gris (x≈255–330, y≈295–495; x≈0–25), puerta de dos hojas color crema (x≈428–475, y≈333–435) y rejillas de ventilación (x≈500–540, y≈210–255).
   - Juego: Muro ciego sin ventanas; solo un cierre metálico gris de lamas (x≈612–700, y≈290–693).
1074. [media] Huecos — planta baja de la casa más cercana a la derecha
   - Captura: Cochera ancha de lamas verticales blancas (x≈1165–1440, y≈345–650) junto a una puerta blanca (x≈1028–1072, y≈340–505).
   - Juego: En la casa más cercana no hay cochera: puerta gris con rejilla (x≈1083–1120, y≈352–432) y ventana blanca de dos hojas (x≈1215–1290, y≈355–430); la única cochera blanca está más al fondo (x≈993–1045).
1075. [media] Huecos — ventanas de planta baja de la hilera derecha
   - Captura: Ventanas con reja de hierro (x≈930–970, y≈340–410; x≈872–885).
   - Juego: Ventanas de planta baja sin reja (x≈1215–1290, y≈355–430; x≈955–975).
1076. [media] Huecos — ventanas de planta alta de la hilera derecha
   - Captura: Carpintería blanca con persiana blanca (x≈1025–1075, y≈95–200; x≈935–970, y≈175–245).
   - Juego: Ventanas con persiana marrón-ocre (x≈1218–1287, y≈188–245; x≈1082–1120, y≈235–290; x≈1007–1028, y≈262–295).
1077. [media] Detalles de fachada — recercados y arcos de la hilera derecha
   - Captura: Recercados salmón en relieve alrededor de ventanas y puertas; las puertas están bajo un arco de medio punto (x≈1015–1075, y≈305–345; x≈835–860).
   - Juego: Huecos sin recercado ni arco; solo vierteaguas blancos.
1078. [media] Cubierta — remate del edificio blanco izquierdo
   - Captura: Remate recto y plano, sin alero ni teja (borde superior en x≈395–610, y≈40–230).
   - Juego: Alero de teja roja sobre el muro (x≈490–735, y≈0–330).
1079. [media] Cubierta — remate de la hilera derecha
   - Captura: Remate con cornisa/moldura salmón y sin teja visible (borde superior de x≈760,y≈300 a x≈1000,y≈0).
   - Juego: Alero de teja roja con banda blanca a lo largo de toda la hilera (x≈890–1440, y≈80–270).
1080. [media] Marcas viales — calzada
   - Captura: Calzada sin marcas viales (x≈330–1000, y≈380–693).
   - Juego: Línea blanca continua por el centro (de x≈830,y≈430 a x≈1100,y≈660) y línea blanca de borde a la derecha (x≈850–1440, y≈380–600).
1081. [media] Mobiliario — farola de la acera izquierda
   - Captura: Farola de columna con globo blanco arriba (x≈560–582, y≈265–405).
   - Juego: Farola de báculo oscuro con brazo y luminaria (x≈735–765, y≈290–390).
1082. [baja] Detalles de fachada — panel de azulejos de la casa cercana derecha
   - Captura: Panel de azulejos pintados con una figura religiosa en la planta alta (x≈1225–1440, y≈0–200).
   - Juego: No hay panel de azulejos en la fachada.
1083. [baja] Detalles de fachada — bajantes de la casa cercana derecha
   - Captura: No se ven bajantes en la fachada cercana (x≈1000–1440).
   - Juego: Dos bajantes blancas verticales de arriba abajo (x≈1355–1400, y≈115–500).
1084. [baja] Calzada — firme de la calzada
   - Captura: Asfalto gastado de tono pardo-beige y polvoriento (x≈330–1000, y≈380–693).
   - Juego: Asfalto gris oscuro uniforme (x≈760–1440, y≈380–693).
1085. [baja] Vegetación — macetas en la acera derecha
   - Captura: Acera derecha despejada, sin macetas (x≈800–1150, y≈380–693).
   - Juego: Macetas con plantas al pie de las fachadas (x≈1030–1060 y x≈1120–1145, y≈400–440).
1086. [baja] Vehículos — aparcamiento en cordón
   - Captura: Fila continua de coches aparcados en el lado izquierdo (x≈270–760) y otro en el derecho (x≈750–805).
   - Juego: Un único coche azul aparcado (x≈757–838, y≈365–432).
**Vista #110** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_110.jpg

1087. [alta] Geometría — edificio de ladrillo del lado izquierdo
   - Captura: Un único volumen largo de ladrillo alineado con la acera, con remate recto continuo (x≈0–665), sin retranqueos; delante solo una acera estrecha y coches aparcados.
   - Juego: Casa de dos plantas de ladrillo con un entrante en L: la fachada cercana (x≈0–565) está retranqueada y un muro perpendicular (x≈565–725) la une con la fachada siguiente, dejando delante una explanada de baldosa blanca (x≈150–760, y≈480–693).
1088. [alta] Color de fachada — hilera de adosados del lado derecho
   - Captura: Enfoscado salmón-rosado en planta baja y crema rosado con recercados salmón en la alta (x≈840–1440).
   - Juego: Enfoscado gris claro/blanco uniforme (x≈780–1440).
1089. [media] Huecos — huecos del edificio de ladrillo izquierdo
   - Captura: Sin ventanas convencionales: pequeños huecos rectangulares dispersos en la parte alta (x≈465–640, y≈135–300) y un gran paño acristalado tras una celosía metálica (x≈462–622, y≈315–445).
   - Juego: Ventanas convencionales con persiana blanca y vierteaguas blanco en dos plantas (x≈0–165, y≈0–145 y y≈365–600; x≈437–520, y≈355–470; x≈600–650, y≈358–440) y un balcón con barandilla (x≈595–655, y≈175–305).
1090. [media] Huecos — ventanas de planta baja de la hilera derecha
   - Captura: Ventanas pequeñas con reja de hierro (x≈1010–1085, y≈340–435; x≈905–935, y≈340–395).
   - Juego: Ventanas anchas sin reja con persiana gris (x≈1135–1260, y≈340–455; x≈1035–1095, y≈345–420).
1091. [media] Huecos — ventanas de planta alta de la hilera derecha
   - Captura: Ventanas medianas con persiana blanca dentro de recercado salmón (x≈1170–1340, y≈25–195; x≈1005–1095, y≈110–245).
   - Juego: Ventanales anchos con persiana gris (x≈1135–1260, y≈165–295; x≈1350–1440, y≈100–270; x≈1035–1095, y≈225–310).
1092. [media] Huecos — puerta de la casa cercana derecha (nº 15)
   - Captura: Puerta blanca de cuarterones con el número 15 (x≈1210–1320, y≈350–580).
   - Juego: Puerta gris lisa (x≈1405–1440, y≈350–520).
1093. [media] Detalles de fachada — recercados, arcos e imposta de la hilera derecha
   - Captura: Recercados salmón en relieve en todas las ventanas, arcos de medio punto sobre las puertas (x≈1185–1325, y≈305–350; x≈850–875, y≈335–355) e imposta salmón entre plantas (x≈840–1440, y≈215–300).
   - Juego: Huecos sin recercado, sin arcos y sin imposta.
1094. [media] Zócalo — pie del edificio de ladrillo izquierdo
   - Captura: El ladrillo baja hasta la acera sin zócalo diferenciado (x≈230–660, y≈395–560).
   - Juego: Zócalo continuo gris oscuro-pardo (x≈0–725, y≈450–693).
1095. [media] Cubierta — remate del edificio de ladrillo izquierdo
   - Captura: Remate recto y plano, sin alero ni teja (borde superior de x≈410,y≈0 a x≈665,y≈270).
   - Juego: Alero de teja roja con cornisa blanca (x≈340–735, y≈0–150).
1096. [media] Cubierta — remate de la hilera derecha
   - Captura: Remate con cornisa salmón, sin teja visible (borde superior de x≈840,y≈215 a x≈1100,y≈0).
   - Juego: Alero de teja roja continuo (de x≈780,y≈320 a x≈1440,y≈50).
1097. [media] Marcas viales — calzada
   - Captura: Calzada sin marcas viales (x≈380–1200).
   - Juego: Línea blanca continua (de x≈775,y≈375 a x≈870,y≈465) y línea blanca de borde a la derecha (de x≈800,y≈370 a x≈1440,y≈640).
1098. [media] Mobiliario — farola de la acera derecha
   - Captura: Farola de columna con globo en la acera derecha (x≈893–918, y≈252–405).
   - Juego: No hay farola de globo; solo un poste blanco delgado junto a la fachada (x≈1105–1120, y≈195–450).
1099. [baja] Detalles de fachada — buzones de la casa cercana derecha
   - Captura: Buzones blancos adosados a la fachada (x≈1350–1440, y≈445–545).
   - Juego: No hay buzones.
1100. [baja] Calzada — firme de la calzada
   - Captura: Asfalto gastado pardo-beige (x≈380–1200, y≈370–693).
   - Juego: Asfalto gris uniforme (x≈745–1440, y≈360–693).
1101. [baja] Vegetación — macetas en la acera izquierda
   - Captura: Acera izquierda sin macetas (tramo visible x≈600–660, y≈390–420).
   - Juego: Macetas con flores rojas y plantas en la acera izquierda (x≈728–752, y≈420–490).
1102. [baja] Mobiliario — farol de pared en la hilera derecha
   - Captura: No hay faroles de pared en la hilera derecha.
   - Juego: Farol de pared negro (x≈990–1015, y≈335–355).
1103. [baja] Vehículos — aparcamiento en cordón
   - Captura: Coches aparcados en cordón a ambos lados (izquierda x≈370–720; derecha x≈760–1125).
   - Juego: Ningún coche aparcado a la vista salvo una furgoneta azul oscuro en primer plano (x≈775–1340, y≈465–693).
**Vista #111** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_111.jpg

1104. [alta] Cámara — encuadre completo
   - Captura: Calle abierta con cielo: a la izquierda la hilera de adosados salmón y crema de dos plantas con cocheras (x≈0–570), a la derecha el gran muro de ladrillo con huecos pequeños y celosía (x≈650–1440) y la calzada con coches aparcados en el centro.
   - Juego: Un pasillo cerrado: paredes de ladrillo con ventanas a ambos lados (x≈0–460 y x≈720–1440), un techo de ladrillo/teja que tapa todo el cielo (y≈0–300) y suelo de baldosa blanca (y≈370–693) hasta una pared al fondo (x≈455–720, y≈265–390); no se ve cielo ni calzada.

### Carretera de Don Benito

**Vista #112** — 03_Tramo_oriental_hacia_el_casco_urbano.jpg (mayo de 2024) · hoja a_112.jpg

1105. [alta] Geometría — trazado de la carretera
   - Captura: Una sola calzada de dos carriles con línea discontinua central (x≈545–720), bordeada a la izquierda por un seto bajo y a la derecha por una cuneta de hierba seca (x≈760–1440).
   - Juego: Avenida de doble calzada: a la izquierda de la cámara hay un andén central de baldosa blanca (x≈0–690, y≈420–693) y, más allá, otra calzada asfaltada (x≈0–660, y≈360–600).
1106. [alta] Vegetación — palmeras del andén central
   - Captura: No hay andén ni palmeras junto a la calzada; solo una palmera detrás del seto izquierdo (x≈440–560, y≈320–400).
   - Juego: Hilera de palmeras grandes en el andén central (x≈480–760, y≈0–490; x≈640–740; x≈800–870; x≈870–1010).
1107. [media] Geometría — edificios del fondo izquierdo
   - Captura: Nave baja rosada-gris con cubierta inclinada (x≈150–410, y≈330–395) y casas blancas de dos plantas (x≈520–630, y≈300–370).
   - Juego: Hilera de casas de ladrillo rojo de dos plantas con tejado de teja (x≈0–390, y≈285–370).
1108. [media] Acera y bordillo — margen derecho
   - Captura: Sin acera: cuneta y talud de hierba seca junto a la línea de borde (x≈760–1440, y≈360–693).
   - Juego: Acera ancha de baldosa blanca con bordillo (x≈900–1440, y≈370–580).
1109. [media] Vegetación — palmera de la acera derecha
   - Captura: En el margen derecho no hay árboles: hierba seca y campo (x≈760–1440).
   - Juego: Palmera grande en primer plano a la derecha (x≈1030–1440, y≈0–510).
1110. [media] Vegetación — seto del borde izquierdo
   - Captura: Seto verde bajo y continuo a lo largo del borde izquierdo de la calzada (x≈0–700, y≈360–600).
   - Juego: No hay seto: bordillo blanco y andén de baldosa (x≈0–690, y≈420–693).
1111. [media] Vegetación — árbol grande de la izquierda
   - Captura: Árbol frondoso de hoja ancha y altura media (x≈0–175, y≈230–410); por encima, cielo despejado.
   - Juego: Árbol de copa en racimos muy alto que cubre la parte superior izquierda (x≈0–520, y≈0–390).
1112. [media] Mobiliario — farolas del margen izquierdo
   - Captura: Farola alta de báculo gris en primer plano izquierdo (x≈80–105, y≈0–510) y otras altas a lo largo del margen (x≈610–635, y≈250–370; x≈668–680, y≈295–355).
   - Juego: No hay farola en primer plano izquierdo; solo farolas oscuras más bajas en el andén (x≈595–605, y≈300–420).
1113. [media] Muros y vallas — cerramiento del lado izquierdo
   - Captura: Muro bajo amarillo con valla metálica de una pista deportiva de cemento (x≈0–560, y≈330–500).
   - Juego: Valla roja de barrotes (x≈0–520, y≈360–440) delante de un césped verde (x≈0–350, y≈380–440).
1114. [media] Otros — solar del lado derecho
   - Captura: Campo arado de tierra rojiza-parda (x≈840–1440, y≈365–500).
   - Juego: Explanada de arena amarillo-ocre (x≈940–1440, y≈370–440) con un arbolito redondo (x≈1085–1145, y≈370–415).
**Vista #113** — 02_Entrada_occidental_desde_la_rotonda.jpg (mayo de 2024) · hoja a_113.jpg

1115. [alta] Color de fachada — edificio cercano de la izquierda
   - Captura: Edificio blanco con alero de teja (x≈60–270, y≈210–400).
   - Juego: Casa de ladrillo rojo (x≈0–215, y≈175–450).
1116. [alta] Vegetación — seto del borde derecho
   - Captura: Seto bajo recortado y continuo a lo largo del borde derecho de la calzada (x≈780–1440, y≈375–693).
   - Juego: No hay seto junto a la calzada: bordillo y acera ancha de baldosa blanca (x≈740–1440, y≈385–693); solo hay setos redondeados más lejos, al borde de un césped (x≈905–1440, y≈370–480).
1117. [media] Huecos — edificio cercano de la izquierda
   - Captura: Una ventana con arco de medio punto y reja en la planta baja (x≈118–178, y≈315–400); sin balcones.
   - Juego: Dos plantas: balcón de forja con puerta acristalada arriba (x≈10–165, y≈225–325) y ventana con persiana blanca abajo (x≈30–130, y≈350–410).
1118. [media] Marcas viales — eje de la calzada
   - Captura: Doble línea continua central (x≈420–665, y≈400–693) y líneas de borde continuas.
   - Juego: Una línea continua (de x≈60,y≈693 a x≈580,y≈420), una discontinua (x≈535–610, y≈440–515) y otra continua (x≈630–700, y≈420–693); no hay doble línea central.
1119. [media] Acera y bordillo — espacio tras el seto derecho
   - Captura: Tras el seto, un parque de tierra/arena clara (x≈880–1440, y≈380–500).
   - Juego: Acera o plaza de baldosa blanca pegada a la calzada (x≈740–1440, y≈385–693).
1120. [media] Vegetación — seto del borde izquierdo
   - Captura: Seto bajo recortado a lo largo del borde izquierdo de la calzada (x≈0–505, y≈385–570).
   - Juego: No hay seto: bordillo con franja de grava blanca (x≈0–600, y≈360–610).
1121. [media] Vegetación — árboles del parque de la derecha
   - Captura: Árboles frondosos de copa densa (x≈950–1440, y≈0–430).
   - Juego: Árboles de copa en racimos tipo pino (x≈970–1440, y≈0–380).
1122. [media] Vegetación — palmera en primer plano derecho
   - Captura: No hay palmera cerca; las palmeras están lejos, al fondo de la carretera (x≈620–760, y≈245–350).
   - Juego: Palmera grande en la acera derecha (x≈720–1020, y≈95–435).
1123. [media] Mobiliario — farolas
   - Captura: Farolas altas de columna gris con dos luminarias en T a ambos lados (x≈415–475, y≈148–400; x≈818–870, y≈150–410).
   - Juego: Farola negra de un solo brazo y una luminaria a la izquierda (x≈105–240, y≈135–515) y farolas negras bajas al fondo (x≈615–635, y≈305–375); ninguna en x≈818–870.
1124. [media] Otros — suelo del parque de la derecha
   - Captura: Suelo de arena/tierra clara (x≈880–1440, y≈380–500).
   - Juego: Césped verde intenso (x≈905–1440, y≈370–490).
1125. [baja] Mobiliario — señal de peligro
   - Captura: Señal triangular de peligro (niños) sobre poste en el seto derecho (x≈820–862, y≈318–410).
   - Juego: No hay señal.
1126. [baja] Muros y vallas — pilar y murete del parque
   - Captura: Pilar de ladrillo (x≈1050–1078, y≈338–438) y murete bajo anaranjado (x≈860–1040, y≈375–395).
   - Juego: No hay pilar ni murete.
1127. [baja] Vehículos — aparcamiento de la vía lateral izquierda
   - Captura: Coches aparcados a lo largo de la vía de servicio izquierda (x≈60–520, y≈350–470).
   - Juego: No hay coches aparcados; solo un bulto azul (x≈235–295, y≈350–380).
**Vista #114** — 04_Cruce_con_Medellin_y_Alcornoque.jpg (mayo de 2024) · hoja a_114.jpg

1128. [alta] Geometría — trazado de la calzada
   - Captura: La cámara está en una calzada estrecha de un carril (x≈420–1000 abajo), separada de la carretera principal por una mediana con seto (x≈0–565, y≈420–693).
   - Juego: Calzada ancha de varios carriles sin mediana (x≈0–1150), asfalto continuo hasta la acera izquierda.
1129. [alta] Geometría — edificio cercano de la derecha
   - Captura: Edificio de tres plantas: ventanas en planta baja (y≈345–460), primera (y≈175–260) y segunda (y≈10–150) en x≈940–1230.
   - Juego: Casa de dos plantas: ventana baja (x≈925–970, y≈350–435), ventana alta (x≈925–970, y≈185–270) y alero de teja encima (x≈900–1030, y≈80–190).
1130. [alta] Color de fachada — edificio cercano de la derecha
   - Captura: Enfoscado salmón-anaranjado claro con recercados y zócalo salmón oscuro (x≈930–1440).
   - Juego: Ladrillo visto rojo (x≈900–1440).
1131. [alta] Vegetación — seto de la mediana izquierda
   - Captura: Seto verde recortado que ocupa el primer plano izquierdo (x≈0–565, y≈420–693) y continúa al fondo (x≈600–705, y≈365–430).
   - Juego: No hay seto; asfalto (x≈0–700, y≈420–693).
1132. [media] Color de fachada — edificio de la esquina izquierda
   - Captura: Fachada crema-amarillenta (x≈0–280, y≈0–410).
   - Juego: Fachada gris-blanca de bloque moderno (x≈0–390, y≈40–410).
1133. [media] Color de fachada — edificio intermedio de la derecha
   - Captura: Fachada salmón con toldos verdes y balcones de forja (x≈800–940, y≈150–400).
   - Juego: Fachada crema de tres plantas con balcones negros (x≈775–900, y≈45–430).
1134. [media] Huecos — edificio de la esquina izquierda
   - Captura: Miradores acristalados blancos en las plantas altas (x≈0–160, y≈200–300) y ventanas sueltas (x≈180–250, y≈255–290).
   - Juego: Balcones corridos grises en cada planta (x≈0–310, y≈120–330) y un toldo de rayas (x≈0–125, y≈250–275).
1135. [media] Huecos — portón del edificio cercano derecho
   - Captura: Portón de madera oscura con celosía de listones (x≈1190–1440, y≈345–600).
   - Juego: Puerta de cochera gris clara con barrotes verticales (x≈1130–1390, y≈365–693).
1136. [media] Detalles de fachada — toldos del edificio cercano derecho
   - Captura: Toldos verdes sobre las ventanas de todas las plantas (x≈940–1230, y≈10–150; x≈935–1000, y≈175–230; x≈940–1115, y≈345–400).
   - Juego: Ningún toldo verde; un toldo de rayas azules y blancas arriba (x≈1100–1260, y≈0–125).
1137. [media] Zócalo — zócalo del edificio cercano derecho
   - Captura: Zócalo alto salmón oscuro (x≈930–1440, y≈420–540).
   - Juego: Zócalo bajo gris oscuro (x≈900–1060, y≈430–520).
1138. [media] Marcas viales — paso de peatones en primer plano
   - Captura: Paso de peatones cebreado cruzando la calzada de la cámara (x≈590–930, y≈435–520), línea de detención (x≈835–985, y≈530–545) y paso ancho en la carretera de la izquierda (x≈0–440, y≈410–460).
   - Juego: No hay paso de peatones cerca: líneas de carril continuas (x≈400–640, x≈780–920, y≈460–693); solo un paso lejano a la izquierda (x≈420–635, y≈398–415).
1139. [media] Vegetación — palmera de la izquierda
   - Captura: No hay palmera en primer plano izquierdo; un árbol pequeño de hoja ancha (x≈285–350, y≈295–400).
   - Juego: Palmera grande en la acera izquierda (x≈40–410, y≈150–420).
1140. [media] Mobiliario — semáforo
   - Captura: Semáforo sobre báculo curvo en la mediana (x≈330–470, y≈75–430) y otro al fondo izquierdo (x≈275–380, y≈285–400).
   - Juego: No hay semáforos.
1141. [baja] Detalles de fachada — banderas
   - Captura: Mástiles con banderas en la fachada (x≈830–870, y≈160–260).
   - Juego: No hay banderas.
1142. [baja] Acera y bordillo — acera derecha
   - Captura: Acera de baldosa rojiza junto al edificio cercano (x≈1000–1440, y≈530–693) y de hormigón claro más allá.
   - Juego: Acera gris clara con bordillo blanco (x≈820–1300, y≈380–693).
1143. [baja] Otros — escalera con barandillas
   - Captura: Escalera con barandillas metálicas en la mediana (x≈530–645, y≈390–475).
   - Juego: No hay escalera ni barandillas.
1144. [baja] Otros — bombona junto a la fachada
   - Captura: No hay objetos junto a la fachada en ese punto.
   - Juego: Bombona naranja en la acera (x≈1058–1098, y≈505–570).

### Calle Antonia López González

**Vista #115** — 02_Desde_un_extremo_hacia_el_otro.jpg (mayo de 2024) · hoja a_115.jpg

1145. [alta] Geometría — fachada cercana del lado izquierdo
   - Captura: La fachada izquierda queda a varios metros, tras la acera y un coche aparcado; se ven de frente la puerta nº 4 y las ventanas (x≈0–480).
   - Juego: Un muro pegado a la cámara ocupa x≈0–545 de arriba abajo (ventana y vuelo de balcón vistos casi de canto).
1146. [alta] Color de fachada — casa cercana izquierda (nº 4)
   - Captura: Enfoscado blanco con bandas y paños ocre-crema (x≈0–330).
   - Juego: Ladrillo visto rojo (x≈0–490).
1147. [alta] Color de fachada — edificio cercano de la derecha
   - Captura: Enfoscado ocre-amarillo (x≈920–1440).
   - Juego: Enfoscado gris claro (x≈990–1440).
1148. [alta] Color de fachada — edificio del fondo de la calle
   - Captura: Al fondo, edificios blancos y crema con bandas ocres de dos plantas (x≈730–930, y≈225–390).
   - Juego: Al fondo, casas de ladrillo rojo de dos plantas con cochera blanca (x≈800–1010, y≈270–395).
1149. [media] Huecos — casa cercana izquierda (nº 4)
   - Captura: Puerta blanca de aluminio con ventanillos bajo arco (x≈130–260, y≈290–560) y buzón (x≈0–75, y≈440–500).
   - Juego: Ventana grande con marco blanco y barrotes (x≈0–275, y≈420–693) y vuelo de balcón blanco encima (x≈0–545, y≈0–200).
1150. [media] Huecos — ventanas de planta baja de la izquierda
   - Captura: Ventanas con reja de hierro (x≈345–435, y≈325–425; x≈510–535, y≈335–385).
   - Juego: Ventanas con persiana blanca y sin reja (x≈560–605, y≈350–500; x≈637–650, y≈355–440).
1151. [media] Huecos — planta baja del edificio cercano derecho
   - Captura: Grandes escaparates acristalados bajo arcos de medio punto blancos (x≈975–1085, y≈315–510; x≈1170–1440, y≈295–600).
   - Juego: Ventanas con reja de barrotes (x≈1040–1095, y≈350–415; x≈1210–1350, y≈350–465).
1152. [media] Huecos — planta alta del edificio cercano derecho
   - Captura: Puertas-ventana con balcón de forja (x≈980–1060, y≈170–260; x≈1235–1440, y≈0–150) en recercado blanco.
   - Juego: Ventanas sin balcón (x≈1050–1095, y≈220–285; x≈1225–1340, y≈135–250).
1153. [media] Detalles de fachada — recercados de las casas siguientes de la izquierda
   - Captura: Recercados y bandas ocres (x≈280–480) y rosa-salmón (x≈480–600) alrededor de ventanas y puertas.
   - Juego: Fachadas gris-blancas sin recercados de color (x≈490–700).
1154. [media] Zócalo — edificio cercano de la derecha
   - Captura: Sin zócalo diferenciado: el paño ocre baja hasta la acera (x≈920–1440, y≈500–620).
   - Juego: Zócalo de mampostería gris oscura (x≈1015–1440, y≈400–550).
1155. [media] Cubierta — remate de la hilera izquierda
   - Captura: Cornisa moldurada blanca y ocre sin teja visible (x≈0–700, y≈0–330).
   - Juego: Alero de teja roja (x≈620–700, y≈0–300).
1156. [media] Cubierta — remate del edificio cercano derecho
   - Captura: Cornisa blanca sin teja visible (x≈920–1050, y≈0–130).
   - Juego: Alero de teja roja (x≈990–1440, y≈20–230).
1157. [media] Marcas viales — calzada
   - Captura: Calzada sin marcas viales.
   - Juego: Dos líneas blancas continuas longitudinales (x≈800–980 y x≈990–1440, y≈480–693).
1158. [media] Mobiliario — farola de la acera izquierda
   - Captura: Farola de columna con globo (x≈525–550, y≈250–430).
   - Juego: No hay farola en la acera izquierda.
1159. [baja] Detalles de fachada — imposta del edificio cercano derecho
   - Captura: Imposta blanca moldurada entre plantas (x≈920–1440, y≈170–300).
   - Juego: Fachada lisa sin imposta.
1160. [baja] Calzada — firme de la calzada
   - Captura: Asfalto pardo-beige polvoriento (x≈420–900, y≈380–693).
   - Juego: Asfalto gris uniforme (x≈700–1440, y≈385–693).
1161. [baja] Vegetación — macetas en la acera izquierda
   - Captura: Acera izquierda sin macetas (tramo visible x≈480–660, y≈380–440).
   - Juego: Macetas con flores en la acera (x≈625–665, y≈470–540) y matas floridas en primer plano (x≈530–670, y≈570–693).
1162. [baja] Mobiliario — señal de la acera izquierda
   - Captura: Señal circular vista por detrás sobre poste (x≈483–498, y≈348–395).
   - Juego: No hay señal.
**Vista #116** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_116.jpg

1163. [alta] Color de fachada — casa del borde derecho
   - Captura: Enfoscado blanco con paños beige-grisáceos (x≈1200–1440).
   - Juego: Ladrillo visto rojo (x≈1310–1440, y≈30–545).
1164. [media] Color de fachada — casa cercana izquierda (nº 18)
   - Captura: Blanca con cornisa, recercados y paños salmón-terracota (cornisa x≈0–510, y≈200–310; planta baja x≈0–390, y≈290–560).
   - Juego: Enfoscado blanco-crema uniforme, sin color (x≈0–700).
1165. [media] Huecos — planta baja de la casa cercana izquierda (nº 18)
   - Captura: Puerta blanca con vidriera oval nº 18 (x≈240–335, y≈310–555), cochera blanca de lamas (x≈390–500, y≈330–520) y buzones (x≈350–380, y≈345–440).
   - Juego: Una ventana con persiana blanca (x≈430–520, y≈350–555) y un paño crema (x≈0–75, y≈360–693); ni puerta ni cochera.
1166. [media] Huecos — ventanas de planta alta de la hilera derecha
   - Captura: Persiana blanca dentro de recercado beige, sin contraventanas (x≈1095–1185, y≈50–195; x≈945–1000, y≈170–235).
   - Juego: Contraventanas de madera marrón a ambos lados (x≈1115–1270, y≈160–275; x≈1010–1085, y≈225–295).
1167. [media] Huecos — planta baja de la hilera derecha
   - Captura: Cocheras blancas de lamas (x≈930–1030, y≈345–480; x≈870–920, y≈345–410) y puerta blanca de cuarterones nº 13 (x≈1100–1175, y≈340–525).
   - Juego: Puerta de madera marrón (x≈1030–1062, y≈352–435) y ventanas con reja (x≈1140–1225, y≈350–440; x≈952–978, y≈350–395); ninguna cochera.
1168. [media] Detalles de fachada — arcos de la hilera izquierda
   - Captura: Arcos de medio punto sobre la puerta y la cochera (x≈240–335, y≈305–345; x≈390–500, y≈320–345).
   - Juego: Huecos rectos sin arcos.
1169. [media] Detalles de fachada — arcos de la hilera derecha
   - Captura: Arcos de medio punto sobre la puerta nº 13 y las cocheras (x≈1090–1180, y≈300–340; x≈930–1030, y≈320–345).
   - Juego: Huecos rectos sin arcos.
1170. [media] Detalles de fachada — balcones de la hilera derecha
   - Captura: Balcones de forja en la planta alta (x≈910–1020, y≈220–300; x≈855–915, y≈265–310).
   - Juego: Planta alta sin balcones en ese tramo (x≈900–1270); solo uno lejano (x≈820–870, y≈318–335).
1171. [media] Zócalo — hilera derecha
   - Captura: Sin zócalo diferenciado: el paño beige de la planta baja llega a la acera.
   - Juego: Zócalo ocre-pardo continuo (x≈900–1310, y≈380–500).
1172. [media] Cubierta — remate de la hilera izquierda
   - Captura: Cornisa moldurada salmón y blanca, sin teja visible (x≈0–690, y≈0–330).
   - Juego: Alero de teja roja (x≈520–700, y≈0–300).
1173. [media] Cubierta — remate de la hilera derecha
   - Captura: Remate blanco con cornisa, sin teja visible (de x≈740,y≈320 a x≈1050,y≈0).
   - Juego: Alero de teja roja (de x≈760,y≈330 a x≈1440,y≈30).
1174. [media] Marcas viales — calzada
   - Captura: Calzada sin marcas viales.
   - Juego: Línea blanca continua (x≈735–840, y≈420–693) y línea de borde a la derecha (de x≈760,y≈360 a x≈1440,y≈680).
1175. [media] Mobiliario — farola de la acera izquierda
   - Captura: Farola de columna con globo (x≈632–645, y≈300–395).
   - Juego: No hay farola en la acera izquierda.
1176. [baja] Detalles de fachada — bajantes de la hilera derecha
   - Captura: No se ven bajantes en la fachada derecha.
   - Juego: Dos bajantes blancas de arriba abajo (x≈1280–1330, y≈95–515).
1177. [baja] Calzada — firme de la calzada
   - Captura: Asfalto pardo-beige (x≈480–1100, y≈360–693).
   - Juego: Asfalto gris uniforme (x≈560–1440, y≈360–693).
1178. [baja] Vegetación — macetas en la acera izquierda
   - Captura: Acera izquierda sin macetas (tramo visible x≈240–400, y≈510–560).
   - Juego: Dos macetas con arbustos cónicos (x≈465–555, y≈465–655) y otras macetas más adelante (x≈580–600, y≈425–440; x≈660–670, y≈380–400).
**Vista #117** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_117.jpg

1179. [alta] Color de fachada — hilera de adosados del lado izquierdo
   - Captura: Enfoscado blanco con recercados y paños beige-grisáceos (x≈0–700).
   - Juego: Ladrillo visto rojo (x≈0–600).
1180. [media] Huecos — planta baja de la casa cercana izquierda (nº 23)
   - Captura: Puerta blanca de cuarterones nº 23 (x≈160–290, y≈320–520) y cochera blanca de lamas (x≈355–475, y≈330–480); más cocheras blancas al fondo (x≈497–545).
   - Juego: Puerta gris acristalada (x≈0–75, y≈360–530) y ventanas con persiana blanca (x≈250–315, y≈355–430; x≈390–425); ninguna cochera en la hilera izquierda.
1181. [media] Huecos — planta alta de la hilera derecha
   - Captura: Ventanas sueltas con carpintería blanca y persiana (x≈1195–1300, y≈40–250), sin balcones.
   - Juego: Grandes ventanales con balcones corridos de vidrio y metal (x≈850–1055, y≈30–320) y una persiana enrollable blanca muy ancha (x≈1155–1440, y≈0–190).
1182. [media] Huecos — planta baja de la hilera derecha (nº 28)
   - Captura: Ventana con lamas horizontales (x≈985–1090, y≈350–405), puerta blanca (x≈1290–1335, y≈365–560) y cocheras blancas al fondo (x≈835–880, y≈350–410).
   - Juego: Puerta gris (x≈925–985, y≈355–530), persiana (x≈835–875, y≈340–420) y un gran cierre enrollable blanco (x≈1155–1440, y≈330–693).
1183. [media] Detalles de fachada — arcos de la hilera izquierda
   - Captura: Arcos de medio punto sobre puertas y cocheras (x≈160–290, y≈305–355; x≈355–475, y≈325–355; x≈497–545, y≈330–350).
   - Juego: Huecos rectos sin arcos.
1184. [media] Zócalo — hilera izquierda
   - Captura: Sin zócalo oscuro: los paños blancos y beige llegan a la acera.
   - Juego: Zócalo gris oscuro continuo (x≈0–600, y≈380–520).
1185. [media] Zócalo — hilera derecha
   - Captura: Zócalo alto de granito gris claro moteado (x≈880–1440, y≈400–550).
   - Juego: Zócalo gris oscuro estrecho (x≈860–1150, y≈440–610).
1186. [media] Cubierta — remate de la hilera izquierda
   - Captura: Cornisa blanca moldurada sin teja visible (de x≈0,y≈40 a x≈690,y≈330).
   - Juego: Alero de teja roja con banda blanca (de x≈0,y≈30 a x≈600,y≈295).
1187. [media] Cubierta — remate de la hilera derecha
   - Captura: Remate blanco con cornisa, sin teja visible (de x≈760,y≈300 a x≈1100,y≈0).
   - Juego: Alero de teja roja (de x≈720,y≈330 a x≈1000,y≈0).
1188. [media] Marcas viales — calzada
   - Captura: Calzada sin marcas viales.
   - Juego: Línea blanca continua (de x≈60,y≈693 a x≈660,y≈370) y línea de borde a la derecha (x≈695–735, y≈400–693).
1189. [media] Mobiliario — farola de la acera izquierda
   - Captura: Farola de columna con globo (x≈628–640, y≈300–380).
   - Juego: No hay farola de globo en la acera izquierda.
1190. [baja] Detalles de fachada — cajas de contadores de la hilera derecha
   - Captura: Caja de registro eléctrico y rejilla en la fachada (x≈1095–1145, y≈420–500).
   - Juego: No hay cajas de registro.
1191. [baja] Calzada — firme de la calzada
   - Captura: Asfalto pardo-beige (x≈480–1100, y≈360–693).
   - Juego: Asfalto gris uniforme (x≈0–950, y≈360–693).
1192. [baja] Vegetación — macetas en la acera izquierda
   - Captura: Acera izquierda sin macetas (tramo visible x≈460–600, y≈400–480).
   - Juego: Macetas con flores al pie de las fachadas (x≈450–475, y≈400–420; x≈520–535, y≈385–400) y en los balcones (x≈30–150, y≈205–235).
1193. [baja] Vegetación — arbusto en primer plano derecho
   - Captura: No hay plantas en la acera derecha (x≈1000–1440, y≈550–693).
   - Juego: Arbusto cónico verde en maceta y flores al pie de la fachada (x≈1215–1340, y≈580–693; x≈1065–1105, y≈615–650).
1194. [baja] Vehículos — lado de aparcamiento
   - Captura: Coches aparcados en el lado izquierdo (x≈600–700, y≈360–435, y uno en primer plano x≈0–505).
   - Juego: Furgonetas aparcadas en el lado derecho (x≈710–860, y≈365–550) y ninguna en el izquierdo.

### Calle Alcornoque

**Vista #120** — 02_Desde_un_extremo_hacia_el_otro.jpg (mayo de 2024) · hoja a_120.jpg

1203. [alta] Geometría — edificio de la derecha (posición)
   - Captura: El edificio de la derecha queda a varios metros, tras la acera; su fachada se ve de frente con dos puertas (x≈820–1440, y≈80–480).
   - Juego: Un muro pegado a la cámara, visto casi de canto, ocupa x≈820–1440 de arriba abajo.
1204. [alta] Color de fachada — edificio de la derecha
   - Captura: Fachada rojo almagre/terracota (x≈820–1440, y≈80–480) con zócalo crema.
   - Juego: Fachada blanca-beige (x≈820–1440).
1205. [alta] Color de fachada — local de la izquierda (mural)
   - Captura: Fachada verde menta con un gran mural pintado (x≈0–480, y≈0–520) y después fachada blanca con grafiti «Pitufos» (x≈480–660).
   - Juego: Casas blancas con zócalo gris (x≈0–520, y≈300–510).
1206. [media] Huecos — edificio de la derecha
   - Captura: Dos puertas con recercado claro bajo una marquesina (x≈893–935, y≈345–400; x≈985–1015, y≈345–415) y paños ciegos.
   - Juego: Un gran escaparate acristalado con marco metálico (x≈870–1440, y≈330–693).
1207. [media] Huecos — local de la izquierda
   - Captura: Escaparates anchos con marco blanco (x≈185–460, y≈320–520; x≈520–580, y≈335–385).
   - Juego: Cochera blanca (x≈0–130, y≈335–510), puerta de madera con reja (x≈235–305, y≈355–450), ventana con reja (x≈395–440, y≈345–400) y persiana (x≈465–515, y≈340–400).
1208. [media] Detalles de fachada — remate de la fachada de la derecha
   - Captura: Marquesina oscura sobre las puertas (x≈870–1025, y≈305–325) y alero de teja parda (x≈1000–1440, y≈80–260).
   - Juego: Chapa ondulada clara corrida a lo largo de la fachada (x≈840–1440, y≈0–330).
1209. [media] Detalles de fachada — mural y grafiti de la izquierda
   - Captura: Mural de un árbol y personajes de dibujos sobre la fachada verde (x≈0–480) y grafiti (x≈520–600, y≈250–330).
   - Juego: Fachadas lisas sin pinturas.
1210. [media] Zócalo — edificios de la izquierda
   - Captura: Sin zócalo de piedra: la fachada verde/blanca llega al suelo.
   - Juego: Zócalo de mampostería gris (x≈120–470, y≈400–490).
1211. [media] Cubierta — cubiertas de la izquierda
   - Captura: Alero corrido de teja parda paralelo a la calle (x≈200–660, y≈60–300).
   - Juego: Tejados de teja naranja a dos aguas con hastiales blancos hacia la calle (x≈0–300, y≈195–310; x≈540–650, y≈290–340).
1212. [media] Marcas viales — calzada
   - Captura: Calzada sin marcas viales.
   - Juego: Dos líneas blancas longitudinales (de x≈0,y≈610 a x≈690,y≈385; de x≈390,y≈693 a x≈690,y≈395).
1213. [baja] Detalles de fachada — toldo del fondo derecho
   - Captura: No hay toldos en la acera derecha.
   - Juego: Toldo de rayas rojas y blancas en un edificio beige (x≈700–810, y≈340–385).
1214. [baja] Calzada — firme de la calzada
   - Captura: Asfalto pardo-beige (x≈600–1100, y≈350–693).
   - Juego: Asfalto gris (x≈0–690, y≈385–693).
1215. [baja] Mobiliario — farol de pared de la derecha
   - Captura: No hay farol en la fachada de la derecha.
   - Juego: Farol negro de pared con brazo (x≈780–1010, y≈310–480).
**Vista #121** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_121.jpg

1216. [alta] Geometría — edificio cercano de la izquierda
   - Captura: Tapia o nave alta de ladrillo encalado sin huecos (x≈0–560, y≈0–490).
   - Juego: Casa baja de una planta con el tejado a la vista (x≈0–510, y≈210–490).
1217. [alta] Geometría — casa de la derecha
   - Captura: Casa blanca-crema de dos plantas retranqueada detrás del muro (x≈1170–1440, y≈0–380).
   - Juego: Casa blanca de dos plantas alineada con la acera en primer plano (x≈940–1440, y≈0–693), con balcón (x≈930–1000, y≈230–320), puerta de madera con barrotes (x≈1280–1440, y≈375–660) y cochera blanca (x≈955–1010, y≈330–490).
1218. [alta] Color de fachada — edificio cercano de la izquierda
   - Captura: Ladrillo pintado de blanco (x≈0–560).
   - Juego: Fachada rojo-anaranjada (x≈0–510, y≈300–490).
1219. [alta] Color de fachada — casa verde de la izquierda
   - Captura: Casa pintada de verde oliva (x≈560–640, y≈225–490) con ventana enrejada (x≈592–620, y≈365–420).
   - Juego: Casas blancas con zócalo gris (x≈505–680, y≈290–430).
1220. [alta] Muros y vallas — cerramiento de la parcela derecha
   - Captura: Muro bajo con pilares y celosía marrón de cañizo/madera (x≈935–1375, y≈330–560).
   - Juego: No hay muro: la fachada de una casa llega hasta la acera (x≈860–1440).
1221. [media] Geometría — volumen blanco del centro-derecha
   - Captura: En x≈860–950 se ve el muro bajo y, al fondo, el edificio verde del centro médico.
   - Juego: Un volumen blanco alto con zócalo de piedra (x≈860–950, y≈130–460).
1222. [media] Huecos — edificio cercano de la izquierda
   - Captura: Muro ciego, sin huecos.
   - Juego: Cierre enrollable blanco (x≈170–305, y≈355–455), puerta enrollable (x≈433–475, y≈350–418) y farol de pared (x≈425–460, y≈338–370).
1223. [media] Cubierta — edificio cercano de la izquierda
   - Captura: Remate recto con cornisa, sin teja visible (x≈0–560, y≈0–235).
   - Juego: Faldón de teja naranja visible (x≈0–630, y≈210–335).
1224. [media] Marcas viales — calzada
   - Captura: Calzada sin marcas viales.
   - Juego: Línea blanca continua (x≈350–675, y≈400–693) y línea blanca ondulada (x≈750–850, y≈400–693).
1225. [media] Otros — edificios del fondo
   - Captura: Edificio verde con el rótulo «Centro Médico Guadámez» (x≈885–1105, y≈278–375), nave gris (x≈1100–1210, y≈245–345) y nave blanca (x≈805–890, y≈290–380).
   - Juego: No están; al fondo solo una casa blanca con tejado de teja (x≈800–865, y≈318–375).
1226. [baja] Calzada — firme de la calzada
   - Captura: Asfalto pardo-beige (x≈500–1200, y≈360–693).
   - Juego: Asfalto gris (x≈330–1050, y≈385–693).
1227. [baja] Acera y bordillo — bordillo izquierdo
   - Captura: Bordillo pintado de amarillo (x≈480–720, y≈360–693).
   - Juego: Bordillo blanco-gris (x≈490–650, y≈385–470).
1228. [baja] Acera y bordillo — bordillo derecho
   - Captura: Bordillo pintado de amarillo (x≈880–1360, y≈415–640).
   - Juego: Bordillo blanco (x≈830–1100, y≈390–693).
1229. [baja] Vegetación — árbol al fondo de la calle
   - Captura: Al fondo no hay árbol: farola y nave blanca (x≈760–840, y≈290–380).
   - Juego: Árbol redondo de copa verde (x≈760–840, y≈275–375).
1230. [baja] Vegetación — plantas en la acera derecha
   - Captura: Acera derecha sin plantas (x≈880–1440, y≈420–693).
   - Juego: Maceta con plantas (x≈1170–1290, y≈560–690) y matas al pie de la fachada (x≈930–1000, y≈460–510).
**Vista #122** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_122.jpg

1231. [alta] Color de fachada — edificio de tres plantas de la derecha
   - Captura: Ladrillo anaranjado con balcones (x≈1025–1095, y≈150–390).
   - Juego: Bloque blanco de tres-cuatro plantas con balcones (x≈1030–1440, y≈80–330).
1232. [alta] Acera y bordillo — margen izquierdo de la calzada
   - Captura: No hay acera: el asfalto linda directamente con la maleza (x≈560–700, y≈400–693).
   - Juego: Acera ancha de baldosa blanca con bordillo (x≈100–700, y≈360–693).
1233. [alta] Vegetación — solar de la izquierda
   - Captura: Solar con hierba seca alta y matorral verde (x≈0–690, y≈340–693).
   - Juego: Explanada lisa de arena amarilla sin vegetación (x≈0–660, y≈355–693).
1234. [media] Huecos — casa de la bifurcación
   - Captura: Puerta de cochera gris (x≈810–865, y≈350–390) y señal de dirección prohibida al lado (x≈868–882, y≈340–352).
   - Juego: Ventana con reja (x≈815–845, y≈350–375); sin cochera ni señal.
1235. [media] Huecos — nave de una planta de la derecha
   - Captura: Gran portón metálico azul (x≈1125–1205, y≈290–440) en un muro de ladrillo pintado de blanco.
   - Juego: Ventanas con marco verde (x≈1215–1250, y≈355–425; x≈1100–1115, y≈350–390) y una puerta (x≈1140–1165, y≈350–420).
1236. [media] Cubierta — casa de la bifurcación
   - Captura: Casa blanca de cubierta plana con chimenea pequeña (x≈780–940, y≈295–390).
   - Juego: Casa blanca con tejado de teja naranja (x≈775–915, y≈280–385).
1237. [media] Cubierta — nave de una planta de la derecha
   - Captura: Cubierta gris (x≈1150–1440, y≈215–265).
   - Juego: Alero de teja naranja (x≈1080–1440, y≈205–330).
1238. [media] Marcas viales — bifurcación
   - Captura: Sin líneas longitudinales en la calzada.
   - Juego: Líneas blancas que separan los dos ramales (de x≈825,y≈460 a x≈940,y≈360; de x≈880,y≈420 a x≈1090,y≈495).
1239. [media] Mobiliario — farolas del centro
   - Captura: No se ven farolas en el margen izquierdo ni en la bifurcación.
   - Juego: Dos farolas negras de báculo (x≈680–725, y≈265–410; x≈878–918, y≈275–400).
1240. [media] Muros y vallas — tapia de bloques de la derecha
   - Captura: Tapia de bloques grises sin enfoscar (x≈1275–1440, y≈350–520).
   - Juego: No hay tapia: fachada blanca con zócalo oscuro.
1241. [media] Otros — fondo izquierdo
   - Captura: Vallas, maquinaria agrícola y naves bajas (x≈0–720, y≈310–390).
   - Juego: Hilera de casas blancas y de ladrillo con tejados rojos (x≈0–700, y≈310–360) y una palmera (x≈315–345, y≈318–350).
1242. [baja] Calzada — firme de la calzada
   - Captura: Asfalto pardo-beige gastado (x≈480–1300, y≈360–693).
   - Juego: Asfalto gris (x≈630–1440, y≈360–693).
1243. [baja] Mobiliario — espejo de tráfico
   - Captura: Espejo convexo de tráfico sobre poste (x≈480–525, y≈305–425).
   - Juego: No hay espejo; solo un poste fino (x≈660–668, y≈330–455).
1244. [baja] Mobiliario — contenedor
   - Captura: Contenedor de basura verde junto a la calzada (x≈613–652, y≈395–450).
   - Juego: No hay contenedor.
1245. [baja] Mobiliario — farol de pared de la derecha
   - Captura: Farol de pared sobre la nave (x≈1105–1150, y≈245–285).
   - Juego: No hay farol.
1246. [baja] Vehículos — aparcamiento del lado derecho
   - Captura: Fila de coches aparcados en el lado derecho (x≈995–1230, y≈360–515).
   - Juego: Ningún coche aparcado.

### Calle Gabriel y Galán

**Vista #125** — 02_Desde_un_extremo_hacia_el_otro.jpg (mayo de 2024) · hoja a_125.jpg

1263. [alta] Color de fachada — plantas altas del bloque de pisos de la izquierda
   - Captura: Ladrillo cara vista amarillo-beige (x≈260–545, y≈0–290).
   - Juego: Enfoscado blanco (x≈0–630, y≈0–330).
1264. [alta] Color de fachada — planta baja del bloque de pisos de la izquierda
   - Captura: Enfoscado rosa-salmón rojizo (x≈0–450, y≈220–520).
   - Juego: Banda azul (x≈0–630, y≈215–330) sobre escaparates grises (x≈0–630, y≈340–693).
1265. [media] Huecos — planta baja del bloque de la izquierda
   - Captura: Cierre de reja plegable metálica (x≈205–365, y≈315–515) y ventanas con reja (x≈375–440, y≈285–370; x≈0–175, y≈320–400).
   - Juego: Escaparates acristalados continuos con cierres enrollables (x≈0–630, y≈340–693).
1266. [media] Huecos — plantas altas del bloque de la izquierda
   - Captura: Balcones corridos con barandilla y aparatos de aire acondicionado en fachada (x≈0–110, y≈215–300; x≈415–460, y≈280–330).
   - Juego: Ventanas con macetas (x≈195–360, y≈0–185) y balcones blancos (x≈475–630, y≈0–160); sin aparatos de aire.
1267. [media] Huecos — casas bajas de la derecha
   - Captura: Cochera blanca de lamas (x≈1100–1440, y≈365–640), puerta en hueco oscuro (x≈1035–1060, y≈350–440) y ventana con reja (x≈880–925, y≈350–400).
   - Juego: Puerta doble de madera marrón (x≈1055–1135, y≈350–445), ventana con reja (x≈908–940, y≈350–390) y ventana (x≈1335–1390, y≈355–440); sin cochera.
1268. [media] Detalles de fachada — toldos del bloque de la izquierda
   - Captura: Toldos de rayas rojas y blancas en los balcones de las plantas altas (x≈200–540, y≈0–220); ninguno en la planta baja.
   - Juego: Toldo corrido de rayas verdes y blancas en la planta baja (x≈0–530, y≈340–485); ninguno arriba.
1269. [media] Zócalo — bloque de la izquierda
   - Captura: Zócalo negro/gris oscuro (x≈0–440, y≈450–560).
   - Juego: Sin zócalo: los escaparates llegan al suelo.
1270. [media] Zócalo — casas bajas de la derecha
   - Captura: Zócalo verde oscuro (x≈860–1100, y≈390–440).
   - Juego: Zócalo ocre-pardo (x≈870–1440, y≈380–490).
1271. [media] Cubierta — casas bajas de la derecha
   - Captura: Remate plano con cornisa blanca, sin teja visible (x≈860–1440, y≈110–300).
   - Juego: Tejados de teja naranja a la vista con chimeneas de ladrillo (x≈870–1440, y≈245–335).
1272. [media] Marcas viales — calzada
   - Captura: Calzada sin marcas viales.
   - Juego: Línea blanca central continua (x≈660–700, y≈360–693) y línea de borde derecha (de x≈760,y≈370 a x≈1440,y≈660).
1273. [baja] Detalles de fachada — rótulo del bar
   - Captura: Rótulo redondo «TABÚ» sobre la entrada (x≈270–335, y≈255–310).
   - Juego: No hay rótulo.
1274. [baja] Calzada — firme de la calzada
   - Captura: Asfalto pardo-beige (x≈250–1100, y≈350–693).
   - Juego: Asfalto gris (x≈420–1440, y≈355–693).
1275. [baja] Mobiliario — contenedor y cajas de la acera derecha
   - Captura: Acera derecha sin contenedores (x≈1200–1440, y≈600–693).
   - Juego: Contenedor iglú verde (x≈1130–1350, y≈440–560) y cajas de cartón (x≈1245–1440, y≈450–640).
**Vista #126** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_126.jpg

1276. [alta] Color de fachada — casas cercanas de la izquierda
   - Captura: Ladrillo cara vista amarillo-beige (x≈0–400, y≈0–540).
   - Juego: Enfoscado blanco (x≈0–410, y≈0–510).
1277. [alta] Color de fachada — volumen del centro-derecha
   - Captura: Casas de una planta crema-amarillentas y blancas (x≈780–870, y≈290–390).
   - Juego: Volumen de ladrillo rojo con puerta gris (x≈785–960, y≈275–470).
1278. [media] Huecos — casa cercana de la izquierda
   - Captura: Ventana ancha con reja de barrotes en planta baja (x≈205–365, y≈335–455).
   - Juego: Puerta doble de madera de cochera (x≈0–150, y≈360–555) y ventanas con persiana blanca (x≈315–370, y≈350–420; x≈0–150, y≈80–230).
1279. [media] Detalles de fachada — toldos de la izquierda
   - Captura: Toldos marrones/beige sobre las ventanas altas (x≈220–375, y≈170–245; x≈410–510, y≈200–280).
   - Juego: Sin toldos.
1280. [media] Zócalo — casas de la izquierda
   - Captura: Sin zócalo diferenciado: el ladrillo llega a la acera.
   - Juego: Zócalo gris (x≈150–410, y≈420–510).
1281. [media] Zócalo — casas bajas de la derecha
   - Captura: Zócalo alto de plaqueta marrón-ocre (x≈870–1170, y≈380–560).
   - Juego: Zócalo de mampostería gris oscura (x≈960–1440, y≈420–693).
1282. [media] Cubierta — casas cercanas de la izquierda
   - Captura: Remate de ladrillo sin teja visible (x≈0–400, y≈0–140).
   - Juego: Alero de teja roja (x≈0–400, y≈0–190).
1283. [media] Cubierta — casas bajas de la derecha
   - Captura: Remate plano con cornisa blanca, sin teja visible (x≈870–1440, y≈110–300).
   - Juego: Alero de teja naranja (x≈955–1440, y≈210–320).
1284. [media] Marcas viales — calzada
   - Captura: Calzada sin marcas viales.
   - Juego: Línea blanca central (de x≈60,y≈693 a x≈650,y≈370) y línea de borde derecha (x≈705–915, y≈370–693).
1285. [media] Muros y vallas — verja de la casa nº 10
   - Captura: Verja de hierro baja delante de la puerta (x≈1165–1440, y≈455–620).
   - Juego: Solo una reja vertical en el borde (x≈1385–1440, y≈360–625).
1286. [baja] Calzada — firme de la calzada
   - Captura: Asfalto pardo-beige (x≈200–1150, y≈350–693).
   - Juego: Asfalto gris (x≈0–1100, y≈360–693).
1287. [baja] Vegetación — buganvilla de la izquierda
   - Captura: Buganvilla florida colgando de la casa cercana (x≈0–180, y≈150–290).
   - Juego: No hay; solo macetas pequeñas en un alféizar (x≈0–140, y≈190–230).
1288. [baja] Vegetación — planta de la casa nº 10
   - Captura: Planta grande (ficus) en maceta tras la verja (x≈1170–1310, y≈320–570).
   - Juego: No hay planta.
1289. [baja] Mobiliario — banco y silla en la acera izquierda
   - Captura: Acera izquierda sin bancos (x≈150–450, y≈420–560).
   - Juego: Banco blanco (x≈180–260, y≈450–515) y silla blanca (x≈470–495, y≈392–418).
**Vista #127** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_127.jpg

1290. [alta] Geometría — casa de la izquierda (posición)
   - Captura: La fachada izquierda se ve de frente a varios metros, tras una furgoneta aparcada (x≈0–560, y≈150–520).
   - Juego: Muro pegado a la cámara, visto de canto (x≈0–690, y≈0–693).
1291. [alta] Color de fachada — casas bajas de la derecha
   - Captura: Enfoscado crema-beige (x≈870–1440, y≈160–470).
   - Juego: Ladrillo visto rojo (x≈985–1375, y≈300–470).
1292. [media] Color de fachada — edificio de varias plantas del fondo derecho
   - Captura: Planta baja de ladrillo y plantas altas blancas/crema (x≈780–1110, y≈190–380).
   - Juego: Todo de ladrillo rojo (x≈815–1075, y≈205–390).
1293. [media] Huecos — casa de la izquierda
   - Captura: Ventana ancha con reja de hierro (x≈285–415, y≈360–450) y cochera blanca (x≈470–520, y≈350–435).
   - Juego: Puerta de madera con ventanillo (x≈0–285, y≈410–693) y una ventana estrecha (x≈620–645, y≈350–400).
1294. [media] Huecos — casas bajas de la derecha
   - Captura: Ventana ancha con barrotes blancos (x≈1018–1135, y≈335–405) y entrada retranqueada (x≈920–970, y≈350–400).
   - Juego: Ventanas con persiana blanca (x≈1020–1070, y≈350–395; x≈1225–1310, y≈350–420).
1295. [media] Zócalo — casas bajas de la derecha
   - Captura: Zócalo de granito gris claro (x≈965–1100, y≈395–470).
   - Juego: Zócalo gris oscuro-pardo (x≈985–1375, y≈395–470).
1296. [media] Cubierta — casa de la izquierda
   - Captura: Remate plano con pretil blanco, sin teja (x≈0–560, y≈150–300).
   - Juego: Alero de teja roja-naranja (x≈0–690, y≈0–330).
1297. [media] Cubierta — edificio de varias plantas del fondo derecho
   - Captura: Tejado de teja con buhardillas (x≈850–1100, y≈190–240).
   - Juego: Remate plano sin teja ni buhardillas (x≈930–1035, y≈205–280).
1298. [media] Marcas viales — calzada
   - Captura: Calzada sin marcas viales.
   - Juego: Línea blanca central (x≈765–1080, y≈410–693) y línea de borde derecha (de x≈770,y≈365 a x≈1440,y≈560).
1299. [media] Vegetación — árboles sobre las casas de la derecha
   - Captura: Sobre las casas de la derecha solo hay cielo (x≈1100–1440, y≈160–300).
   - Juego: Árbol grande de copa en racimos y una palmera (x≈1095–1360, y≈195–310).
1300. [baja] Calzada — firme de la calzada
   - Captura: Asfalto pardo-beige (x≈420–1100, y≈350–693).
   - Juego: Asfalto gris (x≈715–1440, y≈360–693).
1301. [baja] Vegetación — macetas en la acera izquierda
   - Captura: Acera izquierda sin macetas (tramo visible x≈490–620, y≈400–480).
   - Juego: Macetas con arbustos cónicos y flores (x≈620–660, y≈395–495).
1302. [baja] Mobiliario — farol de la casa de la izquierda
   - Captura: Farol fernandino con brazo de forja en la fachada (x≈418–478, y≈195–300).
   - Juego: No hay farol en la fachada izquierda.
1303. [baja] Vehículos — aparcamiento a ambos lados
   - Captura: Calle con coches y furgonetas aparcados a ambos lados (izquierda x≈0–680; derecha x≈730–1440).
   - Juego: Ningún coche aparcado cerca; solo una furgoneta verde en el carril (x≈715–765, y≈365–415) y coches lejanos a la izquierda.

### Calle Julia Mayoral Márquez

**Vista #130** — 02_Desde_un_extremo_hacia_el_otro.jpg (mayo de 2024) · hoja a_130.jpg

1320. [alta] Geometría — trazado: calzada y jardín de la derecha
   - Captura: Calzada estrecha de un carril (x≈240–780 abajo) y, a su derecha, un gran espacio ajardinado con setos y arbustos (x≈690–1440, y≈330–693).
   - Juego: Calzada ancha de varios carriles que ocupa casi todo el ancho (x≈0–1440, y≈390–693) y una plaza pavimentada a la derecha (x≈990–1440, y≈375–480); no hay jardín.
1321. [alta] Color de fachada — bloque del fondo derecho
   - Captura: Casas blancas de dos plantas con tejado de teja (x≈830–1260, y≈265–365).
   - Juego: Bloque de ladrillo rojo de tres plantas (x≈890–1105, y≈235–385).
1322. [alta] Vegetación — setos, arbustos y olivo del jardín de la derecha
   - Captura: Setos, arbustos redondeados y un olivo (x≈840–1180, y≈300–693).
   - Juego: No hay vegetación en ese espacio; solo dos árboles redondos lejanos (x≈750–805 y x≈930–995, y≈330–380).
1323. [media] Geometría — edificios del fondo derecho
   - Captura: Casas de dos plantas (x≈830–1260, y≈265–365).
   - Juego: Bloques blancos de tres plantas (x≈1140–1415, y≈235–385).
1324. [media] Color de fachada — edificio de la izquierda
   - Captura: Enfoscado crema-amarillo (x≈0–605).
   - Juego: Enfoscado blanco (x≈0–575).
1325. [media] Huecos — planta baja del edificio de la izquierda
   - Captura: Escaparates acristalados (x≈0–265, y≈270–530) y huecos en arco cerrados con paneles blancos (x≈340–440, y≈305–455; x≈468–520, y≈320–420).
   - Juego: Puerta de cochera beige con barrotes (x≈0–165, y≈365–590) y ventanas con reja (x≈350–415, y≈350–435; x≈478–508, y≈350–405).
1326. [media] Huecos — planta alta del edificio de la izquierda
   - Captura: Balcones con barandilla (x≈360–430, y≈130–270; x≈478–512, y≈205–285) y aparatos de aire acondicionado (x≈320–370, y≈210–240; x≈460–490, y≈250–275).
   - Juego: Ventanas sin balcón en esas posiciones (x≈350–410, y≈185–270; x≈475–505, y≈240–290); balcón solo en x≈0–245.
1327. [media] Detalles de fachada — arcos de la planta baja izquierda
   - Captura: Arcos de medio punto en la planta baja (x≈340–600, y≈305–360).
   - Juego: Huecos rectos sin arcos.
1328. [media] Zócalo — edificio de la izquierda
   - Captura: Sin zócalo de piedra (paño crema hasta la acera).
   - Juego: Zócalo de mampostería gris (x≈210–570, y≈385–520).
1329. [media] Cubierta — edificio de la izquierda
   - Captura: Cornisa moldurada sin teja visible (x≈200–605, y≈0–260).
   - Juego: Alero de teja roja (x≈100–575, y≈0–265).
1330. [media] Marcas viales — calzada
   - Captura: Calzada sin líneas longitudinales; un paso de peatones lejano y estrecho (x≈640–720, y≈375–385).
   - Juego: Varias líneas longitudinales (x≈245–605; x≈760–875; x≈780–935; x≈1090–1195) y un paso de peatones ancho (x≈585–1000, y≈388–400).
1331. [media] Mobiliario — farola en primer plano derecho
   - Captura: No hay farola en primer plano a la derecha.
   - Juego: Farola negra alta en primer plano (x≈1355–1440, y≈15–615).
1332. [media] Otros — rueda de molino y placa del jardín
   - Captura: Rueda de molino de piedra (x≈828–945, y≈392–465) y una placa informativa (x≈962–1090, y≈465–525).
   - Juego: No hay.
1333. [baja] Mobiliario — señal de obligación
   - Captura: Señal azul redonda con flecha sobre poste en el jardín (x≈1200–1290, y≈345–510).
   - Juego: No está; hay una señal azul de paso de peatones en otro punto (x≈1050–1067, y≈340–405).
1334. [baja] Otros — cartel de venta de solares
   - Captura: Cartel grande «venta de solares residenciales» (x≈1260–1440, y≈240–380).
   - Juego: No hay cartel.
1335. [baja] Otros — bicicleta en la acera izquierda
   - Captura: No hay bicicleta.
   - Juego: Bicicleta azul apoyada en la fachada (x≈220–365, y≈435–530).
**Vista #131** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_131.jpg

1336. [alta] Geometría — banda de aparcamiento y franja ajardinada de la derecha
   - Captura: A la derecha de la calzada, aparcamiento en batería (x≈760–1230, y≈360–540) y una franja de césped con árboles jóvenes antes de la otra calzada (x≈780–1440, y≈255–560).
   - Juego: Mediana con bordillos blancos y árboles (x≈820–1205, y≈285–495); no hay banda de aparcamiento en batería.
1337. [alta] Color de fachada — bloque del centro-derecha
   - Captura: Casas blancas (x≈870–950, y≈290–370).
   - Juego: Bloque de ladrillo rojo (x≈885–945, y≈245–335).
1338. [media] Geometría — casas de la derecha
   - Captura: Casas de dos plantas (x≈870–1440, y≈120–425).
   - Juego: Bloque blanco con dos plantas de ventanas sobre una planta baja (x≈1045–1440, y≈90–450).
1339. [media] Color de fachada — casas siguientes de la izquierda
   - Captura: Crema-melocotón con bandas salmón (x≈520–720, y≈0–420).
   - Juego: Gris-blanco uniforme (x≈450–705).
1340. [media] Huecos — planta baja de la casa cercana izquierda (nº 12)
   - Captura: Puerta de cochera blanca con adornos dorados y el nº 12 (x≈0–250, y≈230–600) y ventana con reja y macetas (x≈370–480, y≈310–450).
   - Juego: Ventanal con persiana enrollable gris (x≈0–85, y≈335–590), puerta gris (x≈280–365, y≈355–530) y ventana sin reja (x≈440–505, y≈340–440).
1341. [media] Huecos — planta alta de la casa cercana izquierda
   - Captura: Ventana con toldo y flores colgantes, sin balcón (x≈375–535, y≈0–215).
   - Juego: Balcón corrido de vidrio y metal (x≈195–455, y≈180–320).
1342. [media] Detalles de fachada — arco y molduras de la casa cercana izquierda
   - Captura: Arco moldurado sobre la cochera (x≈0–250, y≈230–330) y cornisa e impostas molduradas (x≈0–530, y≈200–300).
   - Juego: Fachada lisa sin arco ni molduras.
1343. [media] Cubierta — casas de la derecha
   - Captura: Tejados de teja a dos aguas (x≈870–1440, y≈120–300).
   - Juego: Bloques de cubierta plana (x≈1045–1430, y≈90–330).
1344. [media] Marcas viales — líneas de la calzada
   - Captura: Líneas blancas transversales de aparcamiento en batería (x≈800–1230, y≈380–540); sin líneas longitudinales.
   - Juego: Líneas longitudinales continuas (x≈360–700; x≈760–1060, y≈360–693) y líneas a la derecha (x≈1170–1420, y≈575–585).
1345. [media] Vegetación — árboles de la franja derecha
   - Captura: Árboles jóvenes de tronco fino y copa estrecha (x≈935–1015, y≈255–415; x≈770–860, y≈310–375) y arbustos bajos sobre césped (x≈1020–1095, y≈395–455).
   - Juego: Árboles de copa redonda muy densa (x≈820–1205, y≈285–495).
1346. [media] Mobiliario — farola de la franja derecha
   - Captura: Farola de globo (x≈1160–1215, y≈220–490).
   - Juego: No hay farola de globo; farolas oscuras lejanas (x≈760–800, y≈310–340).
1347. [baja] Detalles de fachada — toldo de la casa cercana izquierda
   - Captura: Toldo liso beige (x≈375–535, y≈0–165).
   - Juego: Toldo de rayas rojas y blancas (x≈250–460, y≈50–190).
1348. [baja] Detalles de fachada — bandera en un balcón de la derecha
   - Captura: Bandera roja colgada de un balcón (x≈1225–1275, y≈290–325).
   - Juego: No hay bandera.
1349. [baja] Calzada — firme de la calzada
   - Captura: Asfalto pardo-beige (x≈450–1300, y≈360–693).
   - Juego: Asfalto gris (x≈100–1440, y≈360–693).
1350. [baja] Acera y bordillo — bordillo izquierdo
   - Captura: Bordillo pintado de amarillo (x≈420–720, y≈360–693).
   - Juego: Bordillo blanco (x≈60–700, y≈360–693).
**Vista #132** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_132.jpg

1351. [alta] Color de fachada — casa cercana de la derecha
   - Captura: Fachada blanca con aplacado de piedra gris-marrón (x≈880–1440).
   - Juego: Ladrillo visto rojo (x≈1025–1440).
1352. [alta] Color de fachada — bloque del fondo izquierdo
   - Captura: Casas blancas (x≈440–530, y≈280–380).
   - Juego: Bloque de ladrillo rojo (x≈440–525, y≈225–380).
1353. [media] Geometría — casas del fondo izquierdo
   - Captura: Casas blancas de dos plantas con tejado de teja (x≈0–660, y≈200–440).
   - Juego: Bloques blancos de tres plantas con balcones (x≈0–440, y≈45–380).
1354. [media] Huecos — planta baja de la casa cercana derecha
   - Captura: Cochera blanca de lamas muy ancha (x≈1070–1440, y≈340–680).
   - Juego: Puerta gris con barrotes (x≈1100–1220, y≈365–610) y una caja blanca (x≈1040–1075, y≈445–490).
1355. [media] Huecos — balcón de la casa cercana derecha
   - Captura: Balcón corrido de forja negra (x≈1020–1440, y≈0–240).
   - Juego: Balcón blanco de barrotes blancos con ropa tendida (x≈1030–1270, y≈130–305).
1356. [media] Huecos — casas siguientes de la derecha
   - Captura: Cocheras blancas de lamas (x≈915–1010, y≈345–520), ventanas con reja (x≈835–860, y≈345–390) y balcones de forja (x≈885–1000, y≈185–290).
   - Juego: Balcones corridos de vidrio (x≈830–1000, y≈230–330), persianas enrollables (x≈935–1005, y≈340–470) y puertas grises (x≈880–905, y≈350–420).
1357. [media] Detalles de fachada — aplacado y arco de las casas de la derecha
   - Captura: Pilastras y recercados de aplacado de piedra (x≈905–930, y≈330–465; x≈1010–1030, y≈325–545; x≈925–990, y≈95–260) y arco moldurado sobre la cochera (x≈1045–1440, y≈270–345).
   - Juego: Sin aplacado ni arco.
1358. [media] Cubierta — hilera de la derecha
   - Captura: Cornisa blanca sin teja visible (de x≈760,y≈330 a x≈1100,y≈0).
   - Juego: Alero de teja roja (de x≈745,y≈330 a x≈1120,y≈0).
1359. [media] Marcas viales — líneas de la calzada
   - Captura: Líneas transversales de aparcamiento en batería (x≈150–490, y≈460–545); la calzada no tiene líneas longitudinales.
   - Juego: Línea central continua (x≈740–930, y≈360–693) y línea izquierda (x≈235–700, y≈360–693).
1360. [media] Vegetación — árboles de la franja izquierda
   - Captura: Árboles jóvenes de tronco fino y copa estrecha sobre césped (x≈225–390, y≈210–460; x≈560–610, y≈300–360).
   - Juego: Hilera de árboles de copa redonda muy densa (x≈0–710, y≈285–500).
1361. [media] Mobiliario — farola de la franja izquierda
   - Captura: Farola de globo (x≈500–520, y≈290–380).
   - Juego: No hay farola de globo; farolas oscuras al fondo (x≈600–635, y≈280–330).
1362. [baja] Calzada — firme de la calzada
   - Captura: Asfalto pardo-beige (x≈480–960, y≈360–693).
   - Juego: Asfalto gris (x≈200–1100, y≈360–693).
1363. [baja] Acera y bordillo — bordillo derecho
   - Captura: Bordillo pintado de amarillo (x≈750–900, y≈370–560).
   - Juego: Bordillo blanco (x≈760–1300, y≈360–693).
1364. [baja] Vegetación — macetas en la acera derecha
   - Captura: Acera derecha sin macetas (x≈780–1000, y≈380–600).
   - Juego: Macetas con flores (x≈855–915, y≈405–455).
1365. [baja] Vehículos — aparcamiento del lado izquierdo
   - Captura: Aparcamiento en batería marcado con líneas blancas (x≈150–490, y≈460–545) con coches en batería (x≈390–625).
   - Juego: Coches aparcados en cordón (x≈0–700, y≈360–600).

### Calle Teresa de Calcuta

**Vista #133** — 02_Acceso_desde_la_carretera.jpg (mayo de 2024) · hoja a_133.jpg

1366. [alta] Cámara — encuadre completo
   - Captura: Calle abierta con cielo: caseta blanca de transformación con puertas metálicas grises (x≈740–1080, y≈335–480), árboles frondosos detrás (x≈770–1440, y≈120–380), una señal de prohibición en la esquina (x≈605–650, y≈325–545), tapia blanca y naves a la izquierda (x≈0–560, y≈300–430) y paso de peatones abajo a la derecha (x≈770–1300, y≈520–693).
   - Juego: La cámara está dentro de la copa de un árbol: ramas y troncos ocupan x≈0–720 de arriba abajo y una masa de hojas verdes tapa el cielo (x≈0–1440, y≈0–480); solo se ven abajo un trozo de calzada (x≈250–600, y≈400–600) y un suelo de arena con un banco (x≈650–1440, y≈390–693).
**Vista #134** — 03_Giro_del_ensanche.jpg (mayo de 2024) · hoja a_134.jpg

1367. [alta] Geometría — adosados de la izquierda
   - Captura: Dos plantas, con terrazas en la planta alta (x≈150–610, y≈230–420).
   - Juego: Casas de una sola planta (x≈0–620, y≈270–410).
1368. [alta] Color de fachada — adosados de la izquierda
   - Captura: Enfoscado salmón-rosado con bandas blancas (x≈20–650, y≈230–420).
   - Juego: Ladrillo visto rojo (x≈0–620, y≈270–410).
1369. [alta] Color de fachada — adosados de la derecha
   - Captura: Enfoscado salmón-rosado (x≈780–1440, y≈170–450).
   - Juego: Enfoscado blanco-gris (x≈815–1440, y≈185–440).
1370. [alta] Vegetación — árboles de alineación
   - Captura: No hay árboles en las aceras de la calle (solo un árbol tras la tapia derecha, x≈1160–1370, y≈255–350).
   - Juego: Hileras de árboles de copa redonda en ambas aceras (x≈385–725, y≈155–410; x≈735–1440, y≈255–455).
1371. [alta] Muros y vallas — cerramientos de la izquierda
   - Captura: Murete con pilares y vallas metálicas oscuras delante de cada casa (x≈20–640, y≈340–420) y cancelas (x≈110–150, x≈165–205, x≈350–410).
   - Juego: No hay muretes ni vallas: las fachadas dan a la acera.
1372. [alta] Muros y vallas — cerramientos de la derecha
   - Captura: Murete con pilares, vallas metálicas y una cancela granate (x≈840–1440, y≈350–450; cancela x≈975–1095).
   - Juego: No hay muretes ni cancelas.
1373. [media] Huecos — planta alta de los adosados de la derecha
   - Captura: Terrazas voladas en la planta alta (x≈890–1170, y≈275–320) y ventanas con persiana (x≈930–965, x≈1020–1060, y≈250–280).
   - Juego: Sin terrazas: fachada lisa con alero de teja intermedio (x≈875–1440, y≈310–330).
1374. [media] Marcas viales — cruce
   - Captura: Paso de peatones cebreado (x≈545–800, y≈405–430) y triángulo de ceda el paso pintado (x≈575–600, y≈430–440).
   - Juego: Sin paso de peatones; solo una línea central lejana (x≈720–745, y≈360–415) y una línea a la derecha (x≈1210–1440, y≈505–520).
1375. [media] Mobiliario — farola de la esquina izquierda
   - Captura: Farola de globo (x≈5–35, y≈265–410).
   - Juego: No hay farola.
1376. [baja] Calzada — firme del cruce
   - Captura: Asfalto pardo-beige (x≈0–1440, y≈420–693).
   - Juego: Asfalto gris (x≈0–1440, y≈410–693).
1377. [baja] Mobiliario — señales de paso de peatones
   - Captura: Dos señales azules de paso de peatones (x≈472–488, y≈320–340; x≈815–840, y≈345–370).
   - Juego: No hay señales.
**Vista #138** — 04_Conexion_occidental_con_Alcornoque.jpg (Fecha de toma no indicada) · hoja a_138.jpg

1394. [alta] Geometría — edificio de la izquierda
   - Captura: Gran nave con fachada lisa y rótulo «Centro Médico Guadámez» (x≈0–455, y≈185–420).
   - Juego: Casas de una planta con tejado de teja naranja (x≈0–620, y≈270–440).
1395. [alta] Color de fachada — edificio de la izquierda
   - Captura: Verde claro (x≈0–455, y≈185–420).
   - Juego: Blanco (x≈0–620, y≈330–440).
1396. [alta] Vegetación — árboles de la acera izquierda
   - Captura: No hay árboles: cielo y la nave verde.
   - Juego: Hilera de árboles de copa redonda (x≈0–670, y≈105–400).
1397. [alta] Muros y vallas — cerramiento de la casa de la esquina
   - Captura: Murete crema con pilares y celosías marrones que rodea la parcela (x≈555–1180, y≈330–490).
   - Juego: No hay murete: la casa da directamente a la acera (x≈660–1085, y≈130–465).
1398. [media] Color de fachada — casa de la esquina
   - Captura: Enfoscado crema (x≈710–1115, y≈90–360).
   - Juego: Enfoscado blanco-gris (x≈660–1085, y≈130–465).
1399. [media] Huecos — planta alta de la casa de la esquina
   - Captura: Una ventana con persiana, sin balcón (x≈760–805, y≈205–250).
   - Juego: Dos balcones con barandilla blanca (x≈730–835, y≈265–320; x≈955–1045, y≈270–320).
1400. [media] Marcas viales — calzada
   - Captura: Calzada sin marcas viales.
   - Juego: Líneas blancas longitudinales (x≈320–660, y≈380–600) y una línea quebrada (x≈530–1440, y≈460–550).
1401. [media] Mobiliario — contenedores
   - Captura: Contenedores verde, azul y amarillo junto a la valla (x≈378–515, y≈365–410).
   - Juego: No hay contenedores.
1402. [media] Mobiliario — farola de la derecha
   - Captura: Farola de globo (x≈1370–1425, y≈195–445).
   - Juego: No hay farola de globo; solo un farol de pared (x≈1390–1435, y≈340–365).
1403. [media] Muros y vallas — valla de la nave de la izquierda
   - Captura: Valla metálica sobre murete bajo (x≈65–455, y≈350–440).
   - Juego: No hay valla.
1404. [media] Muros y vallas — cerramientos de los adosados de la derecha
   - Captura: Muretes con pilares, celosías y cancelas delante de los adosados (x≈1180–1440, y≈350–440).
   - Juego: No hay muretes: fachadas blancas con puertas grises a la acera (x≈1065–1440, y≈225–420).
1405. [baja] Detalles de fachada — rótulo del centro médico
   - Captura: Rótulo con texto, teléfonos y pictogramas (x≈175–420, y≈230–370).
   - Juego: No hay rótulo.
1406. [baja] Calzada — firme de la calzada
   - Captura: Asfalto pardo-beige con parches (x≈0–1440, y≈380–693).
   - Juego: Asfalto gris (x≈0–1440, y≈380–693).
1407. [baja] Mobiliario — señal de la esquina
   - Captura: Señal de prohibición sobre poste (x≈500–530, y≈340–475).
   - Juego: No hay señal.

### Calle Medellín

**Vista #135** — 02_Desde_un_extremo_hacia_el_otro.jpg (mayo de 2024) · hoja a_135.jpg

1378. [alta] Color de fachada — casa de ladrillo de la derecha
   - Captura: Casa de ladrillo visto rojo con balcón y aire acondicionado (x≈835–915, y≈40–420).
   - Juego: En esa posición, fachadas blancas (x≈800–960, y≈150–430).
1379. [media] Color de fachada — casa nº 10 (derecha)
   - Captura: Enfoscado crema-beige (x≈900–1440).
   - Juego: Enfoscado blanco (x≈960–1440).
1380. [media] Huecos — planta baja de la casa nº 5 (izquierda)
   - Captura: Portón de madera marrón de dos hojas con aldabas (x≈310–425, y≈325–590) bajo un arco rebajado blanco (x≈265–445, y≈290–330).
   - Juego: Puerta de cochera con persiana enrollable beige (x≈75–375, y≈380–650) dentro de un recercado blanco grueso (x≈0–425, y≈340–693).
1381. [media] Huecos — planta alta de la casa nº 5 (izquierda)
   - Captura: Balcón de forja con contraventanas de madera marrón (x≈345–420, y≈75–245).
   - Juego: Ventanal ancho con marco de madera y sin balcón (x≈150–370, y≈0–135).
1382. [media] Huecos — planta baja de la casa nº 10 (derecha)
   - Captura: Puerta de madera marrón en hueco (x≈955–990, y≈315–500) y gran ventana con reja de forja ondulada (x≈1170–1440, y≈245–693).
   - Juego: Puerta doble verde claro (x≈1045–1120, y≈365–620); no hay reja grande.
1383. [media] Zócalo — casas de la izquierda
   - Captura: Zócalo gris desconchado a lo largo de la fachada (x≈0–590, y≈420–620).
   - Juego: Zócalo ocre-pardo solo en x≈425–610 (y≈430–600); en x≈0–425 no hay zócalo.
1384. [media] Calzada — pavimento de la calzada
   - Captura: Adoquinado de piedra (x≈450–1000, y≈350–693).
   - Juego: Asfalto gris liso (x≈480–990, y≈360–693).
1385. [baja] Detalles de fachada — recercado de la ventana de la casa nº 10
   - Captura: Recercado ancho de piedra gris alrededor de la reja (x≈1130–1440, y≈180–693).
   - Juego: Recercado blanco moteado alrededor de la puerta (x≈1005–1160, y≈340–693).
1386. [baja] Cubierta — remate de la casa nº 5
   - Captura: Barandilla blanca de terraza sobre la cornisa (x≈480–580, y≈85–190).
   - Juego: Alero de teja roja continuo, sin barandilla (x≈480–700, y≈0–290).
1387. [baja] Acera y bordillo — bordillo y acera izquierda
   - Captura: Bordillo pintado de amarillo y bandas de baldosa rojiza en la acera (x≈450–700, y≈380–693; banda x≈500–560, y≈490–500).
   - Juego: Bordillo blanco y acera de baldosa clara sin bandas (x≈420–720, y≈370–693).
1388. [baja] Acera y bordillo — bordillo y acera derecha
   - Captura: Bordillo pintado de amarillo y bandas de baldosa rojiza (x≈780–1000, y≈360–693; banda x≈950–1060, y≈590–630).
   - Juego: Bordillo blanco y acera de baldosa clara sin bandas (x≈770–1050, y≈365–693).
1389. [baja] Vegetación — macetas de la acera izquierda
   - Captura: Acera izquierda sin macetas (x≈450–700, y≈380–693).
   - Juego: Macetas con flores (x≈430–495, y≈535–620; x≈640–665, y≈395–430).
1390. [baja] Vegetación — macetas de la acera derecha
   - Captura: Acera derecha sin macetas (x≈780–1000, y≈360–693).
   - Juego: Macetas con flores y plantas (x≈870–960, y≈430–520).
1391. [baja] Mobiliario — farol de pared de la izquierda
   - Captura: Farol fernandino con brazo en la fachada (x≈595–628, y≈225–270).
   - Juego: No hay farol.
**Vista #136** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_136.jpg

1392. [alta] Cámara — encuadre completo
   - Captura: Calle con vista larga hacia el fondo: casas blancas con recercados ocres a la izquierda (x≈0–730), casas blancas con balcón a la derecha (x≈940–1440) y la calzada en el centro (x≈600–1200, y≈360–693).
   - Juego: La cámara está de cara a una fachada a pocos metros: pared blanca con puerta de madera marrón (x≈605–795, y≈375–693), ventanas (x≈225–350) y un balcón (x≈590–815, y≈60–230); a la derecha otra pared (x≈970–1440) con un bloque negro (x≈1075–1440, y≈405–693); no se ve la calle ni el cielo.
**Vista #137** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_137.jpg

1393. [alta] Cámara — encuadre completo
   - Captura: Calle con vista larga: gran pared blanca agrietada a la izquierda (x≈0–590), calzada en el centro (x≈550–1100, y≈350–693) y casas blancas con tejado de teja a la derecha (x≈790–1440, y≈150–420).
   - Juego: La cámara está pegada a una fachada blanca vista de frente: puerta de madera marrón (x≈65–315, y≈385–693), ventanas con reja (x≈660–855, y≈375–630; x≈1125–1275, y≈370–600), balcón (x≈45–335, y≈0–200) y macetas en las ventanas altas; zócalo ocre abajo (y≈590–693); no se ve la calle ni el cielo.

### Calle Nueva

**Vista #139** — 02_Entrada_desde_Medellin.jpg (mayo de 2024) · hoja a_139.jpg

1408. [alta] Color de fachada — bloque de pisos de la derecha
   - Captura: Bloque de ladrillo rojo con balcones (x≈800–940, y≈85–390).
   - Juego: En esa posición, bloque blanco (x≈785–965, y≈125–340); solo un bloque de ladrillo pequeño al fondo (x≈765–790, y≈220–345).
1409. [media] Geometría — bloque de pisos de la derecha
   - Captura: Cinco plantas (x≈800–940, y≈85–390).
   - Juego: Tres plantas (x≈785–965, y≈125–340).
1410. [media] Huecos — planta baja de la casa cercana izquierda
   - Captura: Portón de madera marrón con clavos bajo arco rebajado (x≈255–405, y≈360–640) y una ventana pequeña con reja (x≈535–565, y≈375–455).
   - Juego: Ventana ancha con reja (x≈75–230, y≈350–475) y puerta con barrotes dorados (x≈355–410, y≈345–445).
1411. [media] Huecos — planta alta de las casas cercanas de la izquierda
   - Captura: Una ventana pequeña con contraventana de madera (x≈340–375, y≈175–250); sin balcones en las casas cercanas (los balcones empiezan en x≈605).
   - Juego: Ventana ancha con contraventanas verdes (x≈0–270, y≈90–260) y balcones de forja (x≈345–565, y≈265–330).
1412. [media] Huecos — edificio blanco cercano de la derecha
   - Captura: Ventanas pequeñas con recercado gris (x≈1200–1305, y≈60–140; x≈1040–1080, y≈180–225) y un escaparate (x≈995–1090, y≈320–395).
   - Juego: Ventanas anchas con persiana (x≈1065–1185, y≈50–225; x≈1060–1185, y≈360–505) y contraventanas verdes (x≈835–985, y≈180–290).
1413. [media] Zócalo — casas cercanas de la izquierda
   - Captura: Zócalo gris claro/beige (x≈400–610, y≈500–620).
   - Juego: Zócalo gris oscuro casi negro (x≈0–440, y≈420–560).
1414. [media] Marcas viales — calzada
   - Captura: Calzada sin marcas viales.
   - Juego: Línea central continua (de x≈0,y≈690 a x≈700,y≈360) y línea derecha (x≈750–840, y≈370–693).
1415. [media] Acera y bordillo — acera izquierda
   - Captura: Baldosa en damero rojo y blanco (x≈250–700, y≈380–693).
   - Juego: Baldosa gris clara uniforme (x≈0–700, y≈380–600).
1416. [media] Vegetación — árbol del parterre de la derecha
   - Captura: Árbol pequeño de hoja ancha delante del edificio (x≈1125–1440, y≈260–445).
   - Juego: No hay árbol.
1417. [baja] Detalles de fachada — toldos de la derecha
   - Captura: Un toldo blanco liso sobre el escaparate (x≈965–1110, y≈300–325).
   - Juego: Toldos de rayas rojas y blancas (x≈800–975, y≈340–380).
1418. [baja] Calzada — firme de la calzada
   - Captura: Asfalto gris-pardo (x≈480–1100, y≈360–693).
   - Juego: Asfalto gris uniforme (x≈0–1000, y≈360–693).
1419. [baja] Vegetación — macetas en la acera izquierda
   - Captura: Acera izquierda sin macetas (x≈250–700, y≈380–693).
   - Juego: Macetas con flores y arbusto (x≈280–365, y≈430–480; x≈475–510, y≈395–420).
1420. [baja] Mobiliario — farol de pared de la derecha
   - Captura: Farol fernandino de forja en la fachada (x≈1085–1130, y≈195–250).
   - Juego: Farol blanco de pared en otra posición (x≈1400–1440, y≈310–385); ninguno en x≈1085–1130.
1421. [baja] Muros y vallas — barandilla del parterre de la derecha
   - Captura: Barandilla metálica baja a lo largo de la acera (x≈1010–1440, y≈380–470).
   - Juego: No hay barandilla.
**Vista #140** — 03_Cruce_con_Malfeitos.jpg (mayo de 2024) · hoja a_140.jpg

1422. [media] Geometría — edificio de la esquina derecha
   - Captura: Dos plantas (balcones en y≈250–330, planta baja en y≈340–495) con ventanucos en el remate (y≈195–225).
   - Juego: Tres plantas completas con balcones y ventanas (y≈55–160, y≈190–310, y≈340–440) (x≈810–1265).
1423. [media] Huecos — casa cercana de la izquierda
   - Captura: Cochera abierta con zócalo interior de azulejos (x≈435–575, y≈275–490) y ventana alta con persiana (x≈505–560, y≈100–235).
   - Juego: Puerta doble de madera (x≈275–380, y≈360–520) y ventanas (x≈275–375, y≈120–245; x≈460–545, y≈205–290 con contraventanas marrones).
1424. [media] Detalles de fachada — recercados de la casa cercana izquierda
   - Captura: Recercados y pilastras salmón-rosadas (x≈330–620, y≈0–480).
   - Juego: Recercado blanco moteado alrededor de la puerta (x≈250–400, y≈345–505); sin color.
1425. [media] Marcas viales — calzada
   - Captura: Paso de peatones (x≈725–870, y≈415–440) y sin líneas longitudinales.
   - Juego: Líneas longitudinales (x≈460–735 y x≈765–880, y≈370–610) y sin paso de peatones.
1426. [media] Acera y bordillo — acera izquierda
   - Captura: Baldosa en damero rojo y blanco (x≈380–745, y≈360–693).
   - Juego: Baldosa gris clara (x≈0–720, y≈380–693).
1427. [media] Mobiliario — farola en primer plano derecho
   - Captura: No hay farola en la acera derecha cercana.
   - Juego: Farola negra de báculo (x≈970–1180, y≈10–625).
1428. [baja] Vegetación — macetas en la acera izquierda
   - Captura: Acera izquierda sin macetas (x≈430–745, y≈360–693).
   - Juego: Macetas con flores y arbustos (x≈395–630, y≈400–490).
1429. [baja] Mobiliario — señal de estacionamiento de la esquina izquierda
   - Captura: Señal de prohibido estacionar con panel «del 1 de abril al 30 de septiembre» (x≈310–415, y≈290–420) sobre poste (x≈355–375, y≈420–693).
   - Juego: No hay señal.
1430. [baja] Mobiliario — señal de la acera derecha
   - Captura: Señal de prohibido estacionar sobre poste (x≈1085–1120, y≈335–465).
   - Juego: No hay señal.
1431. [baja] Otros — placa con el nombre de la calle
   - Captura: Placa «TRAVESÍA NUEVA» en la esquina izquierda (x≈160–235, y≈245–290).
   - Juego: Placa «CALLE NUEVA» (x≈0–145, y≈295–320).
1432. [baja] Otros — bombona en la acera izquierda
   - Captura: No hay bombona.
   - Juego: Bombona naranja al pie de la fachada (x≈235–280, y≈500–565).
**Vista #141** — 04_Sector_este_hacia_el_centro.jpg (mayo de 2024) · hoja a_141.jpg

1433. [alta] Cámara — encuadre completo
   - Captura: Calle abierta: a la izquierda casas con balcón, una casa baja con tejado de teja y bloques de ladrillo (x≈0–700); a la derecha una casa blanca con recercado de piedra y un edificio blanco con cochera gris (x≈855–1440); calzada con coches aparcados en el centro.
   - Juego: La mitad derecha (x≈720–1440) muestra la cámara metida bajo un voladizo: muro blanco de canto (x≈730–865), un techo de ladrillo encima (x≈865–1440, y≈0–330), una barandilla gris en primer plano (x≈725–830, y≈365–693) y un patio pavimentado (x≈1050–1440, y≈385–693); solo la mitad izquierda (x≈0–720) muestra la calle.

### Calle El Palomar

**Vista #142** — 02_Entrada_desde_Royo.jpg (mayo de 2024) · hoja a_142.jpg

1434. [alta] Geometría — edificio de la derecha
   - Captura: Tapia o nave blanca alta y continua, de remate plano (x≈780–1440, y≈0–693), con solo dos ventanucos altos (x≈905–970, y≈125–225; x≈808–822, y≈255–285).
   - Juego: Hilera de casas bajas de una planta con alero de teja roja (x≈730–1440, y≈170–693).
1435. [alta] Color de fachada — edificio del fondo izquierdo
   - Captura: Casas blancas y crema con balcones (x≈600–670, y≈160–380).
   - Juego: Bloque de ladrillo rojo de tres plantas (x≈530–670, y≈185–390).
1436. [media] Color de fachada — casas cercanas de la izquierda
   - Captura: Enfoscado crema-beige con recercados y bandas salmón (x≈0–600, y≈0–600).
   - Juego: Enfoscado blanco sin recercados de color (x≈0–610).
1437. [media] Color de fachada — edificio del fondo de la calle
   - Captura: Edificio crema con un portón gris grande de nave (x≈665–740, y≈315–380).
   - Juego: Edificio gris con ventanas (x≈665–810, y≈300–365).
1438. [media] Huecos — planta baja de la casa cercana izquierda
   - Captura: Ventana grande con reja de forja en recercado salmón (x≈105–305, y≈280–470), cajas de contadores (x≈210–300, y≈465–545) y puerta de madera marrón con clavos (x≈380–440, y≈340–520).
   - Juego: Puerta de cochera de lamas amarillas y blancas (x≈100–285, y≈370–630) y ventana con reja (x≈450–500, y≈350–440).
1439. [media] Huecos — balcón de la casa cercana izquierda
   - Captura: Balcón de forja negra (x≈100–355, y≈60–175).
   - Juego: Balcón con barandilla blanca (x≈30–370, y≈95–300).
1440. [media] Huecos — fachada de la derecha
   - Captura: Muro casi ciego, sin ventanas a la altura de la calle.
   - Juego: Ventanas con reja (x≈960–1090, y≈350–565; x≈850–885, y≈350–445), una puerta (x≈808–825, y≈355–430) y un farol (x≈798–828, y≈338–365).
1441. [media] Zócalo — casas de la izquierda
   - Captura: Zócalo salmón (x≈0–380, y≈500–600).
   - Juego: Zócalo ocre (x≈285–610, y≈400–550).
1442. [media] Zócalo — fachada de la derecha
   - Captura: Zócalo alto gris tipo granito (x≈780–1440, y≈400–680).
   - Juego: Zócalo ocre (x≈825–1290, y≈420–693).
1443. [media] Cubierta — remate de la derecha
   - Captura: Remate plano sin teja (x≈780–1440, y≈0–290).
   - Juego: Alero de teja roja (x≈735–1380, y≈170–335).
1444. [baja] Detalles de fachada — bajante en primer plano derecho
   - Captura: No hay bajante en la tapia (solo un cable).
   - Juego: Bajante blanca de arriba abajo (x≈1290–1340, y≈0–693).
1445. [baja] Calzada — firme de la calzada
   - Captura: Asfalto pardo-beige (x≈330–1000, y≈380–693).
   - Juego: Asfalto gris (x≈230–950, y≈370–693).
1446. [baja] Vegetación — macetas de la acera derecha
   - Captura: Acera derecha sin macetas (x≈740–1100, y≈380–693).
   - Juego: Macetas con flores (x≈760–850, y≈380–480).
**Vista #143** — 03_Tramo_central_hacia_el_este.jpg (mayo de 2024) · hoja a_143.jpg

1447. [alta] Cámara — encuadre completo
   - Captura: Calle abierta con cielo: casas blancas y crema con balcones de forja y farol fernandino a la izquierda (x≈0–650), casas crema con balcones a la derecha (x≈760–1440) y calzada con coches aparcados en el centro.
   - Juego: La cámara está bajo un techo de teja/ladrillo que tapa el cielo (x≈0–1440, y≈0–290), en un espacio cerrado con suelo de baldosa blanca (y≈380–693) y casas blancas alrededor (x≈65–590 y x≈745–1440); no se ve cielo ni calzada.
**Vista #144** — 04_Extremo_oriental_hacia_el_centro.jpg (mayo de 2024) · hoja a_144.jpg

1448. [alta] Geometría — casa cercana de la derecha
   - Captura: Casa de una sola planta con tejado de teja árabe visible (x≈855–1440, y≈90–330).
   - Juego: Casa de dos plantas con balcón blanco arriba (x≈1020–1440, y≈0–693).
1449. [alta] Color de fachada — casa ocre de la izquierda
   - Captura: Fachada ocre-amarilla con cochera blanca (x≈530–600, y≈250–390).
   - Juego: Fachadas blancas (x≈520–610).
1450. [media] Color de fachada — tramo cercano de la izquierda
   - Captura: Muro de cemento gris sin pintar con una cochera blanca (x≈0–275, y≈200–560).
   - Juego: Fachada blanca (x≈0–280).
1451. [media] Huecos — casas cercanas de la izquierda
   - Captura: Cochera blanca (x≈0–110, y≈375–560), puerta de madera marrón (x≈315–370, y≈345–490) y ventana con reja (x≈470–500, y≈345–405).
   - Juego: Ventana con reja y farol (x≈205–345, y≈335–480); sin cochera ni puerta de madera.
1452. [media] Huecos — planta baja de la casa cercana derecha
   - Captura: Ventana grande con reja de forja (x≈1110–1275, y≈345–600), puerta metálica gris-marrón (x≈968–1022, y≈345–495) y ventana con reja (x≈880–910, y≈345–440).
   - Juego: Gran persiana enrollable blanca (x≈1120–1440, y≈365–680) y puerta de madera (x≈888–925, y≈358–490).
1453. [media] Detalles de fachada — casa nº 69 de la izquierda
   - Captura: Recercados y zócalo granate en puerta y ventanas (x≈275–530, y≈140–500).
   - Juego: Huecos sin recercado de color.
1454. [media] Zócalo — casas cercanas de la izquierda
   - Captura: Zócalo granate bajo (x≈275–530, y≈450–500).
   - Juego: Zócalo de mampostería gris oscura (x≈0–380, y≈430–640).
1455. [media] Cubierta — aleros de la izquierda
   - Captura: Sin aleros intermedios: cornisa simple en lo alto (x≈275–530, y≈140–260).
   - Juego: Alero de teja sobre la planta baja (x≈0–400, y≈240–320) además del alero superior.
1456. [media] Cubierta — casas intermedias de la derecha
   - Captura: Remate plano con pretil (x≈780–1100, y≈180–260).
   - Juego: Aleros de teja naranja (x≈770–1000, y≈225–330).
1457. [baja] Calzada — firme de la calzada
   - Captura: Asfalto pardo-beige (x≈450–1100, y≈350–693).
   - Juego: Asfalto gris (x≈130–990, y≈360–693).
1458. [baja] Vegetación — macetas de la acera derecha
   - Captura: Acera derecha sin macetas (x≈800–1300, y≈400–693).
   - Juego: Macetas con flores y un cactus (x≈895–1010, y≈480–605; x≈805–830, y≈410–460).
1459. [baja] Vehículos — aparcamiento a ambos lados
   - Captura: Coches aparcados en cordón a ambos lados (izquierda x≈200–670; derecha x≈715–795).
   - Juego: Ningún coche.
1460. [baja] Otros — paneles solares de la izquierda
   - Captura: No se ven paneles solares.
   - Juego: Panel solar negro sobre el tejado (x≈60–220, y≈10–120).

### Travesía del Palomar

**Vista #145** — 02_Desde_un_extremo_hacia_el_otro.jpg (mayo de 2024) · hoja a_145.jpg

1461. [alta] Geometría — lado izquierdo de la calleja
   - Captura: Muro melocotón-salmón de una casa en primer plano (x≈0–360, y≈0–560) que cierra la calleja por la izquierda.
   - Juego: Espacio abierto: acera o plaza pavimentada (x≈0–455, y≈430–693) y calzada (x≈160–700), con casas lejanas al fondo (x≈0–690, y≈220–390).
1462. [alta] Color de fachada — edificio del otro lado del cruce (izquierda)
   - Captura: Casas blancas de dos plantas (x≈365–490, y≈235–380).
   - Juego: Bloque de ladrillo rojo (x≈340–530, y≈215–385).
1463. [media] Huecos — muro de la derecha
   - Captura: Muro ciego, sin huecos.
   - Juego: Ventana con reja de hierro (x≈1060–1440, y≈360–693) y contraventana verde arriba (x≈990–1090, y≈0–115).
1464. [media] Huecos — casa del otro lado del cruce (centro)
   - Captura: Balcones de forja y una puerta en arco (x≈490–700, y≈280–385).
   - Juego: Contraventanas verdes, ventanas con reja y una puerta azul (x≈680–940, y≈275–400).
1465. [media] Zócalo — muro de la derecha
   - Captura: Muro gris-blanquecino manchado con zócalo rosa (x≈845–1440, y≈440–693).
   - Juego: Fachada blanca lisa con zócalo gris (x≈940–1440).
1466. [media] Cubierta — casa del otro lado del cruce (centro)
   - Captura: Remate plano con pretil (x≈490–845, y≈250–275).
   - Juego: Tejado de teja naranja a cuatro aguas (x≈680–940, y≈235–275).
1467. [media] Marcas viales — cruce
   - Captura: Paso de peatones cebreado en el cruce (x≈360–560, y≈385–470).
   - Juego: No hay paso de peatones; solo líneas blancas sueltas (x≈0–280, y≈410–430; x≈845–940, y≈425–470).
1468. [media] Mobiliario — farola de la esquina
   - Captura: No hay farola en la esquina.
   - Juego: Farola negra de báculo en la acera de la derecha (x≈560–745, y≈0–625).
1469. [baja] Mobiliario — señal de ceda el paso
   - Captura: Señal triangular de ceda el paso en la esquina derecha (x≈805–860, y≈325–530).
   - Juego: No hay señal.
1470. [baja] Mobiliario — señal de dirección prohibida
   - Captura: Señal de dirección prohibida al otro lado del cruce (x≈710–722, y≈335–385).
   - Juego: No hay señal.
1471. [baja] Otros — poste y cables aéreos
   - Captura: Poste de tendido a la izquierda (x≈340–375, y≈60–550) con cables cruzando la calle (x≈360–845, y≈60–280).
   - Juego: No hay poste ni cables.
**Vista #146** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_146.jpg

1472. [alta] Cámara — encuadre completo
   - Captura: Calle estrecha con cielo: casas blancas con rejas, balcones y farol a la izquierda (x≈0–760), muro beige con ventanas enrejadas a la derecha (x≈865–1440) y la calzada en el centro hasta el fondo.
   - Juego: Espacio cerrado bajo un techo de teja que tapa el cielo (x≈400–1440, y≈0–160): paredes blancas a pocos metros (x≈0–540 y x≈540–1255) con ventanas y macetas, y suelo de baldosa blanca (y≈450–693); no se ve la calle.
**Vista #147** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_147.jpg

1473. [alta] Cámara — encuadre completo
   - Captura: Calle estrecha con cielo: casas bajas blancas y rosa con tejado de teja a la izquierda (x≈0–740), tapia blanca y casas a la derecha (x≈800–1440) y la calzada en el centro.
   - Juego: La mitad izquierda (x≈0–850) muestra el interior de un edificio: techo de teja por dentro con chimeneas colgando (y≈0–330) y suelo de baldosa (y≈380–693); en el centro un pilar blanco pegado a la cámara (x≈620–905); solo a la derecha (x≈905–1440) se ve una calle con una casa de ladrillo y otra blanca.

### Travesía Nueva

**Vista #148** — 02_Desde_un_extremo_hacia_el_otro.jpg (mayo de 2024) · hoja a_148.jpg

1474. [alta] Cámara — encuadre completo
   - Captura: Calle estrecha con cielo: fachada beige con aire acondicionado a la izquierda (x≈0–630), tapia blanca con balaustrada a la derecha (x≈820–1440) y la calzada hacia el fondo en el centro.
   - Juego: Espacio cerrado bajo un techo de teja (x≈270–1150, y≈0–100): paredes blancas a pocos metros con ventanas y persianas (x≈0–430), de frente una fachada con portón marrón (x≈745–955, y≈340–560), balcón y ventana con reja (x≈720–1440), y suelo de baldosa (y≈420–693); no se ve la calle.
**Vista #149** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_149.jpg

1475. [alta] Cámara — encuadre completo
   - Captura: Calle estrecha con cielo: fachadas blancas a ambos lados (x≈0–640 y x≈830–1440), farol en la izquierda (x≈605–640, y≈200–255) y la calzada hacia el fondo en el centro.
   - Juego: La cámara está de cara a una pared blanca a un metro: ventana con reja y macetas (x≈595–915, y≈370–665), otra ventana con contraventanas verdes arriba (x≈500–1050, y≈0–100) y esquinas de pared a ambos lados (x≈0–420; x≈1305–1440); no se ve la calle ni el cielo.
**Vista #150** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_150.jpg

1476. [media] Color de fachada — muro cercano de la izquierda
   - Captura: Muro de cemento gris sin pintar (x≈0–390, y≈0–693).
   - Juego: Fachada blanca (x≈0–640).
1477. [media] Color de fachada — tapia de la derecha
   - Captura: Tapia crema-beige (x≈920–1440, y≈50–693).
   - Juego: Casa blanca (x≈1005–1440, y≈195–693).
1478. [media] Huecos — fachadas cercanas de la izquierda
   - Captura: Muro gris y tapia blanca ciegos (x≈0–700, y≈0–470); solo una ventanita enrejada más allá (x≈668–682, y≈295–345).
   - Juego: Puerta doble verde en recercado de piedra (x≈235–585, y≈335–693), placa azul (x≈80–210, y≈475–560) y balcón de forja con flores (x≈195–640, y≈0–275).
1479. [media] Huecos — tapia de la derecha
   - Captura: Gran portón metálico verde-gris (x≈960–1035, y≈345–485).
   - Juego: Ventana con persiana blanca (x≈1090–1235, y≈350–500); sin portón.
1480. [media] Cubierta — remate de la tapia izquierda
   - Captura: Azotea con barandilla metálica sobre la tapia blanca (x≈470–695, y≈0–230).
   - Juego: Alero de teja naranja (x≈610–775, y≈190–330); sin barandilla.
1481. [media] Cubierta — remate de la tapia derecha
   - Captura: Remate recto sin teja (de x≈920,y≈280 a x≈1440,y≈50).
   - Juego: Alero de teja naranja (x≈1005–1440, y≈195–320).
1482. [baja] Calzada — firme de la calzada
   - Captura: Asfalto pardo-beige (x≈620–1150, y≈370–693).
   - Juego: Asfalto gris (x≈720–1200, y≈365–693).
1483. [baja] Vegetación — macetas en la acera izquierda
   - Captura: Acera izquierda sin macetas (x≈480–770, y≈380–693).
   - Juego: Macetas con flores (x≈715–770, y≈400–490).
1484. [baja] Mobiliario — farol de pared
   - Captura: Farol fernandino en la casa blanca de la derecha (x≈893–918, y≈265–300).
   - Juego: Farol en la fachada izquierda (x≈655–720, y≈330–390) y ninguno a la derecha.

### Travesía El Royo

**Vista #151** — 02_Desde_un_extremo_hacia_el_otro.jpg (mayo de 2024) · hoja a_151.jpg

1485. [alta] Geometría — casa de la esquina derecha con soportal
   - Captura: Casa blanca con soportal de arcos de medio punto en planta baja (x≈940–1045, y≈275–410), balcón de forja y ventanas en arco arriba (x≈940–1045, y≈195–265) y tejado de teja (x≈930–1050, y≈100–185).
   - Juego: En esa zona, fachada blanca lisa de tres plantas con persianas (x≈855–950, y≈100–440); no hay soportal ni arcos.
1486. [alta] Color de fachada — hilera de la izquierda
   - Captura: Enfoscado crema-amarillento con recercados ocres (x≈0–740).
   - Juego: Ladrillo visto rojo (x≈0–545).
1487. [media] Geometría — hilera de la izquierda
   - Captura: Hilera homogénea de casas de dos plantas (x≈0–740, y≈0–450).
   - Juego: Casa de tres plantas (x≈205–545, y≈80–415) junto a otra con alero de teja corrido sobre la planta baja (x≈0–410, y≈250–330).
1488. [media] Huecos — casas cercanas de la izquierda
   - Captura: Puerta de madera marrón (x≈0–90, y≈300–540), ventana con cristal verde en recercado ocre (x≈175–275, y≈290–430) y ventanas con reja (x≈355–430, y≈295–420; x≈460–510, y≈305–405).
   - Juego: Ventana con persiana blanca (x≈0–85, y≈355–460) y puertas blancas con rejilla (x≈265–330, y≈355–460; x≈498–522, y≈350–405).
1489. [media] Huecos — edificio grande de la derecha
   - Captura: Una gran puerta blanca de nave (x≈1090–1440, y≈280–450).
   - Juego: Ventana con persiana blanca (x≈960–1065, y≈340–440) y puerta gris (x≈1300–1440, y≈365–693).
1490. [media] Detalles de fachada — porches y toldos de la izquierda
   - Captura: Porches con arcos de medio punto y barandillas (x≈515–600, y≈310–405) y toldos blancos sobre las ventanas (x≈340–515, y≈240–310).
   - Juego: Sin porches, arcos ni toldos.
1491. [media] Cubierta — edificio grande de la derecha
   - Captura: Remate plano sin teja (x≈1060–1440, y≈80–220).
   - Juego: Alero voladizo de teja naranja (x≈910–1440, y≈80–320).
1492. [media] Marcas viales — calzada
   - Captura: Calzada sin marcas viales.
   - Juego: Línea central blanca continua (x≈715–830, y≈380–693) y línea izquierda (de x≈0,y≈615 a x≈720,y≈370).
1493. [media] Mobiliario — farola alta de la acera derecha
   - Captura: Farola alta de báculo gris en primer plano (x≈1185–1215, y≈0–460).
   - Juego: No hay farola.
1494. [baja] Calzada — firme de la calzada
   - Captura: Asfalto gris-pardo (x≈420–1100, y≈370–693).
   - Juego: Asfalto gris (x≈0–1000, y≈365–693).
1495. [baja] Mobiliario — farol de pared de la derecha
   - Captura: No hay farol en el edificio grande de la derecha.
   - Juego: Farol negro de pared con brazo (x≈970–1060, y≈330–400).
1496. [baja] Otros — panel solar de la izquierda
   - Captura: No se ven paneles solares.
   - Juego: Panel solar negro sobre el tejado (x≈40–220, y≈70–150).
**Vista #152** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_152.jpg

1497. [alta] Color de fachada — casa ocre de la izquierda
   - Captura: Fachada ocre-amarilla (x≈575–640, y≈200–400).
   - Juego: Fachada gris-blanca (x≈580–640).
1498. [alta] Color de fachada — casa azul de la izquierda
   - Captura: Fachada pintada de azul (x≈635–695, y≈245–370).
   - Juego: Fachada blanca (x≈640–695, y≈280–390).
1499. [alta] Color de fachada — casa de la esquina derecha
   - Captura: Enfoscado blanco con recercados y bandas ocre-amarillas (x≈885–1440, y≈110–415).
   - Juego: Ladrillo visto rojo (x≈905–1440, y≈130–470).
1500. [media] Geometría — casas de la izquierda
   - Captura: Casas de dos plantas (x≈0–700).
   - Juego: Edificio de tres plantas con balcones en dos niveles (x≈0–650, y≈0–540).
1501. [media] Huecos — casa cercana de la izquierda
   - Captura: Ventana grande con reja (x≈65–235, y≈285–475) y entrada en arco con cancela de forja (x≈275–410, y≈295–440).
   - Juego: Puerta doble de madera (x≈155–305, y≈360–540) y balcón de forja en la planta alta (x≈120–355, y≈190–300).
1502. [media] Huecos — casa de la esquina derecha
   - Captura: Ventanas con reja y cajón de toldo blanco (x≈995–1045, y≈225–275; x≈1200–1260, y≈215–270; x≈990–1045, y≈335–410; x≈1195–1265, y≈330–380) y puerta (x≈1090–1155, y≈330–410).
   - Juego: Ventanas con persiana blanca sin reja (x≈1030–1075, y≈240–280; x≈1170–1220, y≈235–290; x≈1340–1440, y≈355–420) y una cochera blanca (x≈1000–1080, y≈340–435).
1503. [media] Detalles de fachada — arcos de la izquierda
   - Captura: Entrada y ventana en arco de medio punto (x≈275–410, y≈295–340; x≈425–490, y≈310–345).
   - Juego: Huecos rectos sin arcos.
1504. [media] Marcas viales — calzada
   - Captura: Calzada sin marcas viales.
   - Juego: Línea central continua (x≈800–1000, y≈370–693) y línea curva a la derecha (de x≈840,y≈380 a x≈1440,y≈640).
1505. [media] Mobiliario — farola en primer plano derecho
   - Captura: Farola alta de báculo gris con base de hormigón (x≈965–1025, y≈0–540).
   - Juego: No hay farola en primer plano.
1506. [baja] Detalles de fachada — toldo de la casa cercana izquierda
   - Captura: Toldo de rayas rojas y blancas en la planta alta (x≈320–410, y≈120–240).
   - Juego: No hay toldo.
1507. [baja] Calzada — firme de la calzada
   - Captura: Asfalto gris-pardo (x≈420–1000, y≈360–693).
   - Juego: Asfalto gris (x≈430–1440, y≈365–693).
1508. [baja] Vegetación — macetas en la acera derecha
   - Captura: Acera derecha sin macetas (x≈830–1140, y≈380–500).
   - Juego: Macetas con flores y un arbusto cónico (x≈1185–1220, y≈410–440; x≈1355–1400, y≈405–465).
**Vista #153** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_153.jpg

1509. [alta] Cámara — encuadre completo
   - Captura: Calle abierta con cielo: solar y casa blanca de dos plantas con tejado de teja a la izquierda (x≈0–670), casa azul y adosados crema con toldos a la derecha (x≈800–1440), farola en primer plano (x≈475–500) y la calzada en el centro.
   - Juego: Espacio cerrado bajo un techo de teja que tapa el cielo (x≈715–1440, y≈0–300): muro blanco pegado a la cámara a la izquierda (x≈0–760), suelo de baldosa blanca (y≈360–693) y casas blancas alrededor (x≈900–1440); no se ve cielo ni calzada.

### Calle El Rollo

**Vista #154** — 02_Desde_un_extremo_hacia_el_otro.jpg (mayo de 2024) · hoja a_154.jpg

1510. [alta] Geometría — cruce y edificio de esquina del lado derecho
   - Captura: La cámara está en un cruce: en primer plano derecho hay una calle transversal asfaltada (x≈780–1440, mitad inferior) y el edificio de esquina queda al otro lado, con la esquina en x≈800–840 y la fachada frontal en x≈840–1440, a varios metros
   - Juego: No hay calle transversal: un edificio blanco ocupa toda la mitad derecha (x≈725–1440, de arriba abajo) pegado a la cámara, separado solo por una acera de baldosas (x≈735–920)
1511. [alta] Vegetación — hilera de árboles de la acera izquierda
   - Captura: Árboles alineados en la acera izquierda: uno de copa redonda (x≈535–605, y≈255–405) y otros de hoja morada (x≈585–655) que siguen hacia el fondo
   - Juego: Ningún árbol en la acera izquierda
1512. [alta] Muros y vallas — tapia del lado izquierdo
   - Captura: Tapia alta encalada y desconchada, con un portón de madera (x≈272–345), a lo largo de x≈0–505 (y≈245–460); detrás asoman tejados con chimeneas
   - Juego: En su lugar hay una casa blanca de dos plantas con tejado de teja y contraventanas verdes (x≈0–235) y una fila de naves de una planta con tejado de teja (x≈195–650)
1513. [media] Color de fachada — edificio de esquina de la derecha
   - Captura: Paredes crema/amarillo claro (x≈800–1440, y≈0–480)
   - Juego: Paredes blancas/gris muy claro (x≈725–1440)
1514. [media] Huecos — edificio de esquina de la derecha: balcones de la planta alta
   - Captura: Cuatro balcones de forja negra en la planta alta: x≈848–890, x≈1060–1150, x≈1175–1270, x≈1340–1405 (y≈210–290)
   - Juego: Un balcón de barandilla blanca con macetas en x≈795–905 (y≈125–300) y una reja blanca en la planta alta en x≈1245–1440 (y≈0–90)
1515. [media] Huecos — edificio de esquina de la derecha: rejas de la planta baja
   - Captura: Ventanas con rejas negras y marco salmón: x≈860–890, x≈1055–1125, x≈1315–1370 (y≈335–420)
   - Juego: Rejas blancas grandes: x≈835–890 (y≈350–540) y x≈1250–1440 (y≈360–660)
1516. [media] Detalles de fachada — edificio de esquina de la derecha: recercados, imposta y cornisa
   - Captura: Recercados salmón alrededor de ventanas y balcones, imposta salmón bajo los balcones (y≈265–300) y cornisa salmón (y≈70–110), x≈800–1440
   - Juego: Fachada lisa, sin recercados ni impostas ni cornisa de color (x≈725–1440)
1517. [media] Detalles de fachada — toldos del lado izquierdo
   - Captura: No hay toldos en el lado izquierdo
   - Juego: Toldos a rayas azules y blancas sobre la acera izquierda (x≈215–340 y x≈390–455, y≈340–360)
1518. [media] Cubierta — edificio de esquina de la derecha
   - Captura: Azotea plana con pretil y barandilla negra en lo alto (x≈850–1145, y≈0–55); no se ve tejado de teja
   - Juego: Tejado inclinado de teja roja con alero volado sobre la acera (x≈725–855, y≈0–235)
1519. [media] Marcas viales — calzada de la calle
   - Captura: Asfalto sin líneas pintadas
   - Juego: Líneas blancas longitudinales, una continua y varias discontinuas, a lo largo de la calzada (x≈0–700, y≈380–693)
1520. [media] Mobiliario — farolas de la acera izquierda
   - Captura: Farolas altas de báculo con doble brazo a lo largo de la acera izquierda (x≈515–578, y≈170–410; más al fondo en x≈632–690)
   - Juego: No hay farolas en la acera izquierda
1521. [baja] Detalles de fachada — bajante en la esquina del edificio derecho
   - Captura: No se ve bajante en la esquina del edificio
   - Juego: Bajante blanco vertical de arriba abajo en la esquina (x≈925–950)
1522. [baja] Zócalo — edificio de esquina de la derecha
   - Captura: Zócalo rosado/salmón claro y bajo (x≈835–1390, y≈410–490)
   - Juego: Zócalo ocre/beige (x≈770–1440, y≈420–693)
1523. [baja] Acera y bordillo — bordillo de la acera derecha
   - Captura: Bordillo gris de hormigón alrededor de la esquina (x≈820–1440, y≈470–520)
   - Juego: Bordillo blanco y redondeado (x≈730–790, y≈380–693)
1524. [baja] Vegetación — macetas en la acera y el balcón derecho
   - Captura: No hay macetas en la acera ni en los balcones
   - Juego: Maceta con flores rojas sobre la acera (x≈770–800, y≈445–490) y macetas colgadas en el balcón (x≈790–840, y≈130–230)
1525. [baja] Mobiliario — farol de pared en el edificio de esquina
   - Captura: Farol de forja negra con brazo sobre la fachada (x≈1270–1355, y≈200–275)
   - Juego: No hay farol en la fachada
1526. [baja] Mobiliario — señal en la esquina derecha
   - Captura: Señal octogonal de stop vista por detrás, en un poste junto a la esquina (x≈930–970, y≈335–495)
   - Juego: No hay señal en la esquina
1527. [baja] Mobiliario — señal azul de la acera izquierda
   - Captura: Señal redonda azul en un poste de la acera izquierda (x≈535–553, y≈340–360)
   - Juego: No hay señal
**Vista #155** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_155.jpg

1528. [alta] Cámara — encuadre completo
   - Captura: Calle El Rollo recta: plátano en primer plano izquierdo, bulevar con arbolitos en el centro (x≈450–680), calzada al centro y casas a la derecha, entre ellas una de dos plantas pintada de verde con cochera gris (x≈1010–1440)
   - Juego: La cámara está pegada a una pared blanca que ocupa x≈120–690 de arriba abajo, bajo un alero de teja que tapa la parte alta (x≈690–1440, y≈0–195); al fondo un patio o plaza enlosada rodeada de casas de una planta (x≈690–1440, y≈195–693); no se ve la calle
**Vista #156** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_156.jpg

1529. [alta] Cámara — encuadre completo
   - Captura: La calle recta con bulevar de arbolitos en el centro-derecha (x≈720–1100), nave de chapa azul a la izquierda (x≈0–335), casas de una y dos plantas a ambos lados y farolas de báculo
   - Juego: La cámara está dentro de un patio cerrado enlosado bajo un techo de teja (x≈0–930, y≈0–150), rodeada de fachadas blancas a pocos metros (x≈0–830) y con una pared blanca y una placa negra pegadas a la derecha (x≈830–1440); no se ve ninguna calle

### Calle Nuestra Señora de Guadalupe

**Vista #157** — 02_Desde_un_extremo_hacia_el_otro.jpg (Fecha de toma no indicada) · hoja a_157.jpg

1530. [alta] Geometría — edificio largo de la izquierda
   - Captura: Un único edificio largo de dos plantas retranqueado tras un patio vallado, que termina en un volumen blanco curvo (x≈455–670, y≈175–330); entre la valla y el edificio hay un patio de tierra (x≈0–680, y≈380–600)
   - Juego: Casas blancas de dos plantas alineadas justo detrás de la valla, sin patio ni volumen curvo (x≈0–665, y≈150–480)
1531. [alta] Color de fachada — edificio alto del primer plano derecho
   - Captura: Medianera blanca lisa (x≈1180–1440, y≈0–470)
   - Juego: Edificio de ladrillo rojo de varias plantas (x≈1255–1440, y≈0–460)
1532. [media] Geometría — trazado de la calle al fondo
   - Captura: La calle sigue recta hasta el fondo (x≈700–740, y≈320–360)
   - Juego: La calzada hace curvas en S al fondo (x≈700–790, y≈350–400)
1533. [media] Huecos — edificio largo de la izquierda
   - Captura: Planta alta con ventanas de persiana enrollable beige (x≈0–540, y≈60–290) y planta baja con ventanas anchas de lamas marrones (x≈0–600, y≈300–390)
   - Juego: Un balcón de barandilla blanca (x≈195–345, y≈240–310), ventanas sueltas con rejas blancas y una puerta con reja (x≈215–295, y≈360–440)
1534. [media] Huecos — edificio alto del primer plano derecho
   - Captura: Pared ciega, sin ventanas (x≈1180–1440)
   - Juego: Ventanas con persianas, un balcón con barandilla (x≈1340–1440, y≈120–180) y un portal acristalado (x≈1345–1440, y≈350–450)
1535. [media] Cubierta — edificio largo de la izquierda
   - Captura: Cubierta plana: el borde superior es un alero recto sin teja (x≈0–670, arriba)
   - Juego: Tejados de teja roja sobre las casas (x≈300–465, y≈150–230; x≈600–665, y≈265–295)
1536. [media] Vegetación — árboles del lado izquierdo
   - Captura: No hay árboles en el lado izquierdo
   - Juego: Dos árboles grandes de copa verde: uno en primer plano (x≈0–465, y≈0–570) y otro detrás de la valla (x≈440–615, y≈165–400)
1537. [media] Mobiliario — farola del lado derecho
   - Captura: Farola de báculo gris con luminaria de globo en primer plano derecho (x≈1195–1290, y≈110–480)
   - Juego: No hay farola en el lado derecho
1538. [media] Muros y vallas — valla del lado izquierdo
   - Captura: Paneles de malla metálica gris verdosa sobre un murete de hormigón, con un pilar de hormigón (x≈185–280), a lo largo de x≈0–680 (y≈340–690)
   - Juego: Barandilla de barrotes rojos sobre un murete blanco (x≈0–610, y≈360–640)
1539. [media] Otros — terreno del lado derecho
   - Captura: Solar de tierra con matorrales y un murete blanco bajo (x≈1060–1440, y≈350–520)
   - Juego: Plaza pavimentada con baldosas grises (x≈980–1440, y≈370–693)
1540. [baja] Marcas viales — línea derecha de la calzada
   - Captura: Línea derecha discontinua (x≈800–1030, y≈420–690)
   - Juego: Línea derecha continua (x≈780–1060, y≈380–693)
1541. [baja] Acera y bordillo — acera izquierda
   - Captura: Acera de hormigón liso con bordillo gris (x≈230–700, y≈350–693)
   - Juego: Acera de baldosas claras con bordillo blanco redondeado (x≈80–690, y≈370–693)
1542. [baja] Mobiliario — farola del lado izquierdo
   - Captura: No hay farola en la acera izquierda
   - Juego: Farola de brazo en la acera izquierda (x≈615–655, y≈265–410)
**Vista #158** — 03_Tramo_intermedio.jpg (Fecha de toma no indicada) · hoja a_158.jpg

1543. [alta] Color de fachada — edificio del primer plano izquierdo
   - Captura: Ladrillo rojo visto en la planta baja y parte de la alta (x≈0–575, y≈0–693); solo una franja alta enfoscada en blanco
   - Juego: Fachada enfoscada en blanco (x≈0–680)
1544. [media] Color de fachada — casa del primer plano derecho
   - Captura: Fachada rosa salmón claro (x≈985–1440, y≈0–500)
   - Juego: Fachada blanca (x≈1000–1440)
1545. [media] Huecos — edificio del primer plano izquierdo
   - Captura: Ventanas apaisadas corridas con persianas grises y marcos oxidados en la planta baja (x≈0–425, y≈260–470; x≈478–562, y≈318–385) y una rejilla de ventilación (x≈245–290, y≈580–625)
   - Juego: Ventanas sueltas con persianas, una gran reja gris abombada (x≈15–330, y≈355–645) y un balcón de forja negra (x≈555–600, y≈275–320)
1546. [media] Huecos — casa del primer plano derecho
   - Captura: Ventana alta con persiana blanca (x≈1085–1190, y≈110–230), ventana baja con persiana gris (x≈1025–1110, y≈345–440) y puerta abierta con cortina (x≈1350–1440, y≈300–600)
   - Juego: Balcón de forja negra en la planta alta (x≈1010–1200, y≈190–310) y puerta de marco beige con paneles gris azulado (x≈1060–1170, y≈360–530)
1547. [media] Detalles de fachada — casa del primer plano derecho: recercados
   - Captura: Recercados chapados de plaqueta gris alrededor de la ventana baja (x≈1015–1125, y≈325–445) y de la puerta (x≈1305–1440, y≈260–600)
   - Juego: Sin recercados chapados; la puerta tiene un marco beige liso (x≈1060–1170, y≈360–530)
1548. [media] Zócalo — casa del primer plano derecho
   - Captura: Zócalo alto chapado de plaqueta de piedra gris (x≈985–1440, y≈410–640)
   - Juego: Zócalo gris liso y bajo (x≈1170–1440, y≈470–600)
1549. [media] Cubierta — edificio del lado izquierdo
   - Captura: Cubierta plana con remate recto, sin teja (x≈260–680, borde superior)
   - Juego: Alero de teja roja a lo largo de toda la hilera (x≈360–680, y≈0–310)
1550. [baja] Detalles de fachada — toldo de la casa del primer plano derecho
   - Captura: No hay toldo
   - Juego: Toldo a rayas rojas y blancas sobre el balcón (x≈1000–1115, y≈120–195)
1551. [baja] Zócalo — edificio del lado izquierdo
   - Captura: Sin zócalo diferenciado: el ladrillo llega hasta el suelo
   - Juego: Zócalo gris corrido (x≈0–680, y≈390–560)
1552. [baja] Calzada — grieta en el centro de la calzada
   - Captura: Asfalto sin grieta longitudinal
   - Juego: Una grieta oscura serpenteante por el centro de la calzada (x≈715–830, y≈365–693)
1553. [baja] Marcas viales — líneas de la calzada
   - Captura: Una línea continua a la izquierda (x≈430–700, y≈360–693) y una línea discontinua a la derecha (x≈760–990, y≈380–693)
   - Juego: Dos líneas continuas (x≈575–710 y x≈750–1060)
1554. [baja] Acera y bordillo — acera izquierda
   - Captura: Acera de losetas grises con bordillo gris (x≈160–700, y≈360–693)
   - Juego: Acera de baldosas claras con bordillo blanco redondeado (x≈230–690)
1555. [baja] Vegetación — macetas de la acera izquierda
   - Captura: No hay plantas en la acera izquierda
   - Juego: Macetas grandes con flores en primer plano (x≈20–335, y≈560–693) y macetas a lo largo de la fachada (x≈530–660, y≈380–470)
1556. [baja] Vegetación — macetas de la acera derecha
   - Captura: No hay plantas en la acera derecha
   - Juego: Macetas con flores a lo largo de la acera derecha (x≈845–1340, y≈390–640)
1557. [baja] Mobiliario — farol de pared del lado derecho
   - Captura: No hay farol en las fachadas de la derecha
   - Juego: Farol de pared negro (x≈930–965, y≈325–355)
1558. [baja] Otros — bombona en la acera derecha
   - Captura: No hay bombona
   - Juego: Bombona de butano naranja junto a la fachada (x≈1010–1035, y≈455–495)
**Vista #159** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_159.jpg

1559. [alta] Geometría — nave tras la valla de la derecha
   - Captura: Nave grande de paredes crema con pilastras rosadas y portones oscuros (x≈930–1440, y≈0–420)
   - Juego: En su lugar una casa blanca de una planta con tejado de teja (x≈1110–1440, y≈235–520) y un edificio blanco de dos plantas con tejado de teja y contraventanas verdes (x≈735–1105, y≈260–390)
1560. [alta] Color de fachada — casa nº 22 del primer plano izquierdo
   - Captura: Fachada crema/beige claro (x≈0–455, y≈0–560)
   - Juego: Fachada de ladrillo rojo (x≈0–455, y≈0–600)
1561. [alta] Color de fachada — segunda casa de la izquierda
   - Captura: Fachada salmón/terracota con recercados blancos (x≈455–585, y≈190–450)
   - Juego: Fachada blanca (x≈455–590)
1562. [media] Color de fachada — casas del fondo izquierdo
   - Captura: Casas crema y blancas (x≈585–700)
   - Juego: Una casa de ladrillo rojo entre casas blancas (x≈590–630, y≈270–370)
1563. [media] Huecos — casa nº 22 del primer plano izquierdo
   - Captura: Puerta de madera oscura con el número 22 encima (x≈5–145, y≈350–560), ventana baja con reja gris (x≈340–420, y≈345–440) y una ventana pequeña arriba (x≈280–370, y≈180–250); sin balcones
   - Juego: Dos balcones con barandilla blanca en la planta alta (x≈0–165, y≈130–295; x≈320–450, y≈235–320), ventana baja con persiana blanca (x≈0–60, y≈365–520) y una reja gris (x≈335–410, y≈355–440)
1564. [media] Marcas viales — líneas de la calzada
   - Captura: Calzada sin líneas pintadas
   - Juego: Dos líneas blancas continuas (x≈450–665 y x≈720–1060)
1565. [media] Vegetación — jardín tras la valla de la derecha
   - Captura: Jardín con plantas verdes densas tras la valla (x≈960–1440, y≈420–600) y árboles (x≈780–945, y≈235–350; x≈1100–1440, y≈120–480)
   - Juego: Explanada pavimentada sin plantas, con un solo árbol (x≈850–1150, y≈95–420) y una copa en la esquina superior (x≈1135–1440, y≈0–160)
1566. [media] Muros y vallas — valla del lado derecho
   - Captura: Verja de barrotes oscuros (x≈825–920) y valla de malla gris con pilares de hormigón (x≈920–1440, y≈350–693) sobre un murete de hormigón
   - Juego: Barandilla de barrotes rojos sobre un murete blanco (x≈820–1440, y≈355–600)
1567. [baja] Detalles de fachada — toldo de la casa del primer plano izquierdo
   - Captura: No hay toldo
   - Juego: Toldo a rayas verdes y blancas (x≈335–455, y≈150–230)
1568. [baja] Calzada — grieta en el centro de la calzada
   - Captura: Asfalto sin grieta longitudinal
   - Juego: Una grieta oscura serpenteante por el centro (x≈695–740, y≈360–530)
1569. [baja] Acera y bordillo — acera derecha
   - Captura: Tramo de baldosa rojiza al fondo (x≈780–920, y≈380–495) y baldosa gris en primer plano (x≈830–1180, y≈480–693), con bordillo gris
   - Juego: Baldosa clara uniforme con bordillo blanco redondeado (x≈760–1440, y≈360–693)
1570. [baja] Vegetación — plantas en la acera izquierda
   - Captura: No hay plantas en la acera izquierda
   - Juego: Maceta con flores (x≈0–85, y≈550–650) y cactus en macetas (x≈255–345, y≈455–530)
1571. [baja] Mobiliario — señal en el lado derecho
   - Captura: No se ve señal
   - Juego: Señal triangular en un poste (x≈808–825, y≈325–350)

### Calle Alberquilla

**Vista #160** — 02_Desde_un_extremo_hacia_el_otro.jpg (mayo de 2024) · hoja a_160.jpg

1572. [media] Geometría — edificio ocre del lado izquierdo (tercero desde la cámara)
   - Captura: Edificio ocre de una sola planta alta (x≈415–560, remate en y≈290–300)
   - Juego: Edificio ocre de dos plantas (x≈440–560, remate en y≈232–270), con ventanas en ambas plantas
1573. [media] Color de fachada — casa de dos plantas del lado izquierdo tras el edificio ocre
   - Captura: Fachada blanca (x≈560–620, y≈280–390)
   - Juego: Fachada rosa salmón con contraventanas verdes (x≈555–615, y≈260–390)
1574. [media] Huecos — edificio ocre del lado izquierdo
   - Captura: Una cochera ancha con puerta blanca (x≈447–505, y≈335–395) y una puerta pequeña (x≈535–550)
   - Juego: Una puerta blanca estrecha (x≈462–490, y≈350–410) y ventanas en planta baja y alta (x≈465–490, y≈265–305; x≈525–545, y≈285–380)
1575. [media] Calzada — firme de la calle
   - Captura: Asfalto gris parduzco con parches (x≈0–1440, y≈360–693)
   - Juego: Superficie lisa color crema casi blanca
1576. [baja] Zócalo — casa de una planta del lado izquierdo
   - Captura: Zócalo de azulejos decorados con dibujo azul y marrón (x≈205–370, y≈410–480)
   - Juego: Zócalo de plaquetas cuadradas marrones lisas (x≈200–380, y≈400–475)
1577. [baja] Calzada — grietas de la calzada
   - Captura: No hay grietas largas en el centro de la calzada
   - Juego: Una grieta oscura longitudinal por el centro (x≈540–745, y≈355–693) y otra transversal (x≈265–650, y≈490–520)
1578. [baja] Marcas viales — línea en primer plano izquierdo
   - Captura: Sin marcas viales
   - Juego: Una línea discontinua tenue que cruza el primer plano izquierdo (x≈0–560, y≈610–650)
1579. [baja] Acera y bordillo — bordillo de la acera izquierda
   - Captura: Bordillo gris (x≈0–420, y≈450–560)
   - Juego: Bordillo blanco (x≈0–700, y≈360–580)
1580. [baja] Mobiliario — faroles de pared
   - Captura: Faroles de pared negros en las fachadas: a la derecha (x≈993–1010, y≈275–300) y a la izquierda (x≈615–630, y≈315–330)
   - Juego: No se ven faroles en esas fachadas
1581. [baja] Otros — antena de televisión del primer plano derecho
   - Captura: Antena de televisión sobre el tejado (x≈1215–1245, y≈180–245)
   - Juego: No hay antena
**Vista #161** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_161.jpg

1582. [media] Color de fachada — tercer edificio de la izquierda
   - Captura: Parte alta de ladrillo marrón rojizo y parte baja enfoscada gris beige (x≈470–540, y≈265–395)
   - Juego: Casa blanca de una planta con hastial de teja (x≈450–540, y≈295–395)
1583. [media] Color de fachada — segunda casa del lado derecho
   - Captura: Fachada blanca (x≈1050–1245, y≈215–350)
   - Juego: Fachada gris (x≈1060–1245, y≈160–460)
1584. [media] Huecos — casa del primer plano izquierdo
   - Captura: Balcón corrido de forja negra en toda la planta alta (x≈0–255, y≈200–290) y ventana baja con reja blanca (x≈100–210, y≈325–440)
   - Juego: Sin balcón: una ventana con persiana blanca en la planta alta (x≈150–235, y≈195–275) y una ventana baja con reja (x≈150–230, y≈355–400)
1585. [media] Huecos — segunda casa de la izquierda
   - Captura: Cochera con puerta blanca (x≈425–455, y≈335–400) y una ventana con reja (x≈340–385, y≈330–390)
   - Juego: Dos ventanas con reja (x≈320–365 y x≈410–440, y≈350–390), sin cochera
1586. [media] Huecos — casa amarilla del primer plano derecho
   - Captura: Balcón de forja negra en la planta alta (x≈1285–1440, y≈235–310) y ventana con persiana blanca encima (x≈1335–1440, y≈160–250)
   - Juego: Dos ventanas grandes con marco blanco, sin balcón (x≈1310–1440, y≈150–255 y y≈350–450)
1587. [media] Detalles de fachada — segunda casa de la izquierda: recercados
   - Captura: Recercados salmón/terracota alrededor de las ventanas (x≈335–385, y≈320–395) y esquina en el mismo color
   - Juego: Ventanas sin recercados de color; contraventanas marrones (x≈305–380, y≈235–295)
1588. [media] Calzada — firme de la calle
   - Captura: Asfalto gris parduzco con grietas (x≈0–1440, y≈360–693)
   - Juego: Superficie lisa color crema casi blanca
1589. [baja] Zócalo — segunda casa de la izquierda
   - Captura: Zócalo alto terracota (x≈275–470, y≈380–440)
   - Juego: Zócalo apenas marcado, gris/blanco con una franja marrón estrecha (x≈395–455, y≈390–415)
1590. [baja] Mobiliario — farol de pared en la esquina de la segunda casa
   - Captura: Farol de pared grande en la esquina (x≈295–335, y≈215–265)
   - Juego: No hay farol en esa esquina; hay uno más pequeño más adelante (x≈425–450, y≈300–315)
1591. [baja] Mobiliario — contenedores del lado izquierdo
   - Captura: No se ven contenedores (en ese punto hay un coche blanco aparcado, x≈595–635)
   - Juego: Contenedores de reciclaje verde, azul y amarillo junto a la acera (x≈585–645, y≈360–390)
**Vista #162** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_162.jpg

1592. [media] Geometría — edificio del fondo izquierdo
   - Captura: Edificio de dos plantas (x≈0–160, y≈255–400)
   - Juego: Edificio de tres plantas con franja ocre en la base (x≈0–130, y≈250–365)
1593. [media] Color de fachada — edificio largo de una planta de la izquierda
   - Captura: Fondo crema/blanco uniforme con molduras ocre
   - Juego: Un tramo de la fachada pintado de rosa salmón (x≈170–330, y≈340–395) y el resto blanco/gris
1594. [media] Color de fachada — nave grande del lado derecho
   - Captura: Muro de bloques de hormigón gris sin pintar con un portón metálico azul (x≈1035–1440, y≈200–410)
   - Juego: Nave blanca con puertas azules (x≈1300–1440, y≈245–390)
1595. [media] Detalles de fachada — edificio largo de una planta de la izquierda
   - Captura: Cornisa, pilastras y recercados ocre/salmón sobre fondo crema (x≈160–625, y≈290–395)
   - Juego: Fachada lisa sin cornisa ni pilastras ni recercados (x≈130–600, y≈315–400)
1596. [media] Cubierta — edificio largo de una planta de la izquierda
   - Captura: Pretil con frontón escalonado en el centro (x≈470–625, y≈275–310) y cornisa corrida
   - Juego: Cubierta plana con volúmenes cúbicos en la azotea (x≈245–450, y≈295–320), sin frontón
1597. [media] Cubierta — edificio bajo del lado derecho
   - Captura: Edificio alargado con tejado de teja a dos aguas y puerta oscura (x≈890–1035, y≈300–375)
   - Juego: Nave blanca de cubierta plana con puertas azules (x≈830–1155, y≈290–380)
1598. [media] Calzada — firme de la calle
   - Captura: Asfalto gris con grietas
   - Juego: Superficie lisa color crema claro
1599. [media] Marcas viales — marcas de la mitad derecha de la calzada
   - Captura: Líneas blancas discontinuas en la mitad derecha (x≈820–1180, y≈410–665) y una banda blanca transversal ancha (x≈890–1110, y≈458–475)
   - Juego: Sin marcas en la mitad derecha; solo líneas discontinuas tenues a la izquierda (x≈0–700, y≈380–450)
1600. [media] Acera y bordillo — esquina del primer plano derecho
   - Captura: Asfalto de la calzada con líneas discontinuas (x≈930–1440, y≈570–693)
   - Juego: Esquina de acera enlosada (x≈930–1440, y≈570–693)
1601. [media] Vegetación — árbol del lado derecho
   - Captura: No hay árbol en ese punto (muro de la nave)
   - Juego: Árbol grande de copa redonda (x≈1145–1345, y≈315–390)
1602. [media] Muros y vallas — seto de la acera izquierda
   - Captura: Seto alto y verde a lo largo de la acera izquierda (x≈520–680, y≈348–400)
   - Juego: No hay seto
1603. [baja] Mobiliario — farola de la acera izquierda
   - Captura: Farola en la acera izquierda junto al seto (x≈615–628, y≈297–400)
   - Juego: No hay farola en ese punto (solo una al fondo izquierdo, x≈40–95, y≈290–385)
1604. [baja] Mobiliario — señal de dirección prohibida en primer plano derecho
   - Captura: No hay señales en el primer plano derecho
   - Juego: Señal roja de dirección prohibida en un poste (x≈980–1060, y≈310–650)
1605. [baja] Mobiliario — segundo poste de señal en el borde derecho
   - Captura: No hay poste
   - Juego: Poste de señal visto por detrás (x≈1375–1440, y≈300–680)
1606. [baja] Mobiliario — farola del lado derecho
   - Captura: Farola con luminaria de globo junto a la nave (x≈1165–1185, y≈270–400)
   - Juego: No hay farola
1607. [baja] Mobiliario — contenedores del lado derecho
   - Captura: Contenedores azules y amarillos junto a la acera (x≈850–897, y≈352–370)
   - Juego: No hay contenedores
**Vista #163** — 05_Tramo_del_poligono_hacia_el_pueblo.jpg (mayo de 2024) · hoja a_163.jpg

1608. [alta] Geometría — trazado de la calzada respecto a la cámara
   - Captura: Calzada de asfalto en el centro de la imagen (x≈250–900 en primer plano, convergiendo en x≈700–740), con arcén de tierra a la derecha y una calle lateral con coches a la izquierda (x≈0–560, y≈380–450)
   - Juego: En el centro, un bordillo blanco con una franja naranja (x≈665–735) separa una gran explanada de losas de hormigón a la izquierda (x≈0–700, y≈355–693) de una calzada clara a la derecha (x≈705–1440)
1609. [media] Cubierta — naves del lado izquierdo
   - Captura: Cubiertas inclinadas granates bien visibles (x≈0–440, y≈280–330)
   - Juego: Nave de cubierta plana con solo un remate rojo en el borde (x≈0–465, y≈265–280)
1610. [media] Calzada — firme de la calle
   - Captura: Asfalto gris desgastado con parches y baches
   - Juego: Superficie lisa gris clara y losas de hormigón
1611. [media] Vegetación — setos y arbustos del lado izquierdo
   - Captura: Setos y arbustos altos delante de las naves (x≈195–640, y≈320–390)
   - Juego: No hay vegetación delante de las naves
1612. [media] Vegetación — campo del lado derecho
   - Captura: Rastrojo de cereal color paja con una franja de hierba verde junto a la calzada (x≈880–1440, y≈390–470)
   - Juego: Tierra naranja parda sin vegetación con una franja amarilla (x≈735–1440, y≈350–620)
1613. [media] Mobiliario — farolas del lado izquierdo
   - Captura: Farolas altas de brazo curvo: x≈90–175 (y≈235–460), un poste en primer plano (x≈210–225, y≈90–470), x≈570–608 y x≈633–652
   - Juego: No hay farolas
1614. [baja] Huecos — puertas de la nave izquierda
   - Captura: Puertas rojas en la fachada de la nave (x≈60–120, y≈360–385)
   - Juego: Puertas azules (x≈0–55, x≈255–275, x≈410–420, y≈345–380)
1615. [baja] Acera y bordillo — borde derecho de la calzada
   - Captura: Sin bordillo: el asfalto acaba en un arcén de tierra (x≈760–1440)
   - Juego: Bordillo blanco a lo largo del borde derecho (x≈890–1440, y≈425–660)
**Vista #164** — 06_Acceso_exterior_hacia_Guarena.jpg (mayo de 2024) · hoja a_164.jpg

1616. [media] Geometría — posición del camino respecto a la cámara
   - Captura: El camino de tierra va centrado bajo la cámara (x≈470–1100 en primer plano)
   - Juego: El camino queda desplazado a la izquierda (x≈100–710 en primer plano) y la cámara está sobre su borde derecho
1617. [media] Geometría — polígono en el horizonte izquierdo
   - Captura: Complejo industrial blanco con torres o silos altos (x≈220–340, y≈315–360) y un edificio alto blanco en el borde (x≈0–45, y≈300–365)
   - Juego: Solo naves blancas bajas (x≈0–740, y≈310–360), sin torres
1618. [media] Calzada — firme del camino
   - Captura: Tierra compactada marrón rojiza
   - Juego: Dos rodadas color tostado claro con una banda central blanquecina
1619. [media] Vegetación — cunetas del camino
   - Captura: Hierbas altas verdes, cardos y matorral a ambos lados del camino (x≈180–700 y x≈750–1300)
   - Juego: Sin vegetación: el campo llega hasta el camino
1620. [media] Vegetación — campo de la izquierda
   - Captura: Heno segado en hileras, verde parduzco (x≈0–640, y≈360–600)
   - Juego: Campo uniforme amarillo paja a franjas (x≈0–700, y≈355–693)
1621. [media] Vegetación — arbolado en el horizonte derecho
   - Captura: Hilera de árboles/olivar en el horizonte derecho (x≈1100–1440, y≈345–380)
   - Juego: Horizonte derecho llano sin árboles
1622. [baja] Otros — línea eléctrica
   - Captura: Torre metálica de celosía (x≈970–990, y≈315–350) con los cables subiendo hacia la derecha (x≈975–1230)
   - Juego: Un poste delgado (x≈955–965, y≈320–355) con los cables subiendo hacia la izquierda (x≈750–970)

### Calle Salsipuedes

**Vista #165** — 02_Desde_un_extremo_hacia_el_otro.jpg (mayo de 2024) · hoja a_165.jpg

1623. [media] Huecos — puerta del primer plano izquierdo
   - Captura: Puerta grande de madera oscura (x≈0–130, y≈150–620)
   - Juego: Hueco con cortina de tiras de colores verde, amarillo y blanco (x≈0–125, y≈380–693)
1624. [media] Huecos — casa del lado izquierdo: planta alta
   - Captura: Balcón de forja negra en la planta alta (x≈405–520, y≈40–200)
   - Juego: Ventana con persiana marrón, sin balcón (x≈430–495, y≈110–245)
1625. [media] Huecos — casa del lado izquierdo: ventana baja
   - Captura: Ventana con persiana de lamas de madera y marco de granito gris (x≈430–495, y≈270–510)
   - Juego: Ventana con reja oscura y marco blanco (x≈430–505, y≈350–480)
1626. [media] Huecos — casa nº 22 del lado derecho: puerta
   - Captura: Puerta doble de madera marrón oscura (x≈1065–1175, y≈325–530)
   - Juego: Hueco con cortina de tiras de colores (x≈1060–1145, y≈360–535)
1627. [media] Huecos — casa nº 22 del lado derecho: balcón
   - Captura: Balcón de forja negra sobre la puerta (x≈1040–1170, y≈180–280)
   - Juego: Ventana con persiana marrón, sin balcón (x≈1040–1160, y≈85–245)
1628. [media] Detalles de fachada — recercado de la puerta del primer plano izquierdo
   - Captura: Recercado y pilastra de granito gris (x≈130–260, y≈0–650)
   - Juego: Recercado liso blanco/gris claro (x≈0–215, y≈340–693)
1629. [media] Detalles de fachada — casa nº 22 del lado derecho: recercados y cornisa
   - Captura: Recercados salmón con orejetas en la ventana alta (x≈1045–1195, y≈20–160), en la puerta (x≈1025–1220, y≈290–350) y cornisa salmón; recercados iguales en las casas siguientes (x≈890–930, y≈200–330)
   - Juego: Marcos blancos lisos, sin recercados ni cornisa de color (x≈840–1440)
1630. [media] Zócalo — casa del lado izquierdo
   - Captura: Zócalo de granito gris en la parte baja de la fachada (x≈260–620, y≈450–600)
   - Juego: Sin zócalo: la fachada blanca llega al suelo (x≈215–680)
1631. [media] Acera y bordillo — acera izquierda
   - Captura: Solería en damero diagonal de baldosas terracota y blancas (x≈300–680, y≈370–693)
   - Juego: Baldosas blancas lisas (x≈240–680, y≈360–693)
1632. [media] Acera y bordillo — acera derecha
   - Captura: Solería en damero diagonal de baldosas terracota y blancas (x≈860–1440, y≈420–693)
   - Juego: Baldosas blancas lisas (x≈700–1440, y≈365–693)
1633. [baja] Zócalo — casas del lado derecho
   - Captura: Zócalo salmón claro (x≈870–1440, y≈420–620)
   - Juego: Zócalo ocre parduzco (x≈840–1440, y≈390–680)
1634. [baja] Calzada — grieta de la calzada
   - Captura: Asfalto sin grieta longitudinal
   - Juego: Grieta oscura en el centro de la calzada (x≈715–730, y≈545–693)
1635. [baja] Mobiliario — farol de pared del lado derecho
   - Captura: Farol de pared negro (x≈835–860, y≈245–285)
   - Juego: No hay farol
**Vista #166** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_166.jpg

1636. [media] Huecos — casa del primer plano izquierdo: planta alta
   - Captura: Ventana con persiana marrón, sin balcón (x≈265–330, y≈210–290)
   - Juego: Balcón ancho de forja oscura (x≈40–375, y≈130–305)
1637. [media] Huecos — casa del primer plano izquierdo: planta baja
   - Captura: Ventana con reja y persiana marrón (x≈245–345, y≈360–455) y un portal a la izquierda (x≈0–55, y≈335–560)
   - Juego: Cochera ancha con puerta doble de madera clara (x≈90–320, y≈360–610)
1638. [media] Huecos — segunda casa de la izquierda
   - Captura: Puerta blanca a la izquierda (x≈430–475, y≈350–430), ventana con reja a la derecha (x≈515–540) y ventana alta sin contraventanas (x≈490–510, y≈285–320)
   - Juego: Ventana alta con contraventanas verdes (x≈430–500, y≈190–280), ventana con reja a la izquierda (x≈450–490, y≈350–425) y puerta blanca a la derecha (x≈520–540)
1639. [media] Huecos — hilera de casas de la derecha: planta alta
   - Captura: Ventanas pequeñas con contraventana de madera (x≈1160–1200, y≈265–320), sin balcones
   - Juego: Ventanas grandes con contraventanas marrones (x≈1160–1440, y≈65–255) y un balcón de forja con ropa tendida (x≈995–1090, y≈260–320)
1640. [media] Detalles de fachada — hilera de casas de la derecha: imposta y cornisa
   - Captura: Imposta corrida entre plantas (x≈910–1440, y≈315–340) y cornisa en el remate
   - Juego: Fachada sin imposta ni cornisa
1641. [baja] Detalles de fachada — recercado de la puerta de la derecha
   - Captura: Recercado beige/piedra alrededor de la puerta (x≈1020–1095, y≈345–470)
   - Juego: Recercado blanco (x≈1015–1085, y≈345–440)
1642. [baja] Calzada — grieta de la calzada
   - Captura: Grietas cortas dispersas
   - Juego: Una grieta oscura larga y continua por el centro (x≈730–900, y≈360–693) y otra transversal (x≈545–830, y≈530–565)
1643. [baja] Otros — silla en la acera izquierda
   - Captura: No hay silla
   - Juego: Silla de anea junto a la fachada (x≈335–395, y≈450–530)
1644. [baja] Otros — cables en las fachadas de la izquierda
   - Captura: Cables negros grapados a lo largo de las fachadas (x≈0–560, y≈255–330)
   - Juego: No hay cables
**Vista #167** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_167.jpg

1645. [media] Color de fachada — casa del primer plano derecho
   - Captura: Enfoscado de cemento gris sin pintar (x≈950–1440, y≈60–540)
   - Juego: Fachada beige claro (x≈1000–1440, y≈30–510)
1646. [media] Huecos — casa del primer plano izquierdo: planta baja
   - Captura: Cochera ancha con puerta blanca de cuarterones en arco (x≈165–345, y≈365–565) y caja de contadores (x≈40–125, y≈425–470)
   - Juego: Ventana con persiana marrón y marco blanco (x≈140–305, y≈350–530)
1647. [media] Huecos — segunda casa de la izquierda
   - Captura: Ventana enmarcada con un panel de azulejos (x≈425–480, y≈345–430) y balcón de forja negra encima (x≈425–490, y≈265–320)
   - Juego: Ventana alta con contraventanas marrones (x≈385–485, y≈150–270) y ventana baja con reja y flores (x≈415–470, y≈350–440)
1648. [media] Huecos — casa del primer plano derecho: planta baja
   - Captura: Puerta doble de madera marrón (x≈1100–1180, y≈350–480) y ventana con reja (x≈985–1030, y≈345–405)
   - Juego: Puerta con panel de rejilla gris (x≈1040–1090, y≈350–430) y una ventana grande con reja y persiana marrón (x≈1205–1345, y≈350–460)
1649. [media] Detalles de fachada — casa del primer plano izquierdo: pilastras y recercados
   - Captura: Pilastras, cornisa y recercado de puerta en salmón (x≈0–365)
   - Juego: Sin molduras de color; solo un marco blanco en la ventana (x≈140–305)
1650. [baja] Zócalo — segunda casa de la izquierda
   - Captura: Zócalo de azulejos decorados (x≈365–600, y≈420–510)
   - Juego: Zócalo de plaqueta gris lisa (x≈370–590, y≈400–510)
1651. [baja] Zócalo — casa del primer plano derecho
   - Captura: Zócalo marrón de ladrillo/piedra (x≈950–1440, y≈400–540)
   - Juego: Franja beige parda (x≈1000–1440, y≈430–510)
1652. [baja] Calzada — tapa de registro
   - Captura: No se ve tapa cuadrada en primer plano
   - Juego: Contorno de una tapa cuadrada grande en primer plano (x≈455–735, y≈645–693)
1653. [baja] Acera y bordillo — acera izquierda
   - Captura: Pavimento gris texturado con bordillo gris (x≈240–690, y≈380–640)
   - Juego: Baldosas blancas con bordillo blanco (x≈40–640, y≈390–693)
1654. [baja] Mobiliario — farol de pared en la esquina derecha
   - Captura: Farol de pared en la esquina de la casa derecha (x≈928–950, y≈255–290)
   - Juego: No hay farol
1655. [baja] Otros — bicicleta en la acera derecha
   - Captura: No hay bicicleta
   - Juego: Bicicleta apoyada en la fachada (x≈1075–1170, y≈410–470)

### Calle de San Gregorio

**Vista #168** — 02_Desde_un_extremo_hacia_el_otro.jpg (mayo de 2024) · hoja a_168.jpg

1656. [media] Color de fachada — casa del primer plano izquierdo
   - Captura: Fachada crema/beige cálido (x≈75–430, y≈190–480)
   - Juego: Fachada blanca/gris claro (x≈0–410, y≈210–520)
1657. [media] Color de fachada — planta baja del supermercado (derecha)
   - Captura: Planta baja pintada de gris antracita (x≈880–1160, y≈255–520)
   - Juego: Planta baja con una franja morada y cierres metálicos gris claro (x≈775–1150, y≈300–530)
1658. [media] Huecos — planta baja del supermercado (derecha)
   - Captura: Escaparates de cristal (x≈905–940, y≈320–415; x≈990–1050, y≈310–445) y puertas (x≈820–870, y≈330–410)
   - Juego: Fila continua de locales con cierres enrollables (x≈775–1140, y≈330–530)
1659. [media] Huecos — edificio amarillo del primer plano derecho: planta baja
   - Captura: Pared amarilla ciega en la planta baja (x≈1160–1440, y≈290–470)
   - Juego: Ventana con persiana marrón y marco blanco (x≈1285–1440, y≈350–550)
1660. [media] Detalles de fachada — casa blanca con molduras azules del lado izquierdo
   - Captura: Cornisa, recercados y zócalo pintados de azul sobre fondo blanco (x≈430–505, y≈205–400)
   - Juego: Casas blancas sin ningún elemento azul (x≈380–625)
1661. [media] Detalles de fachada — toldos del lado derecho
   - Captura: No hay toldos
   - Juego: Toldos a rayas amarillas y blancas sobre los locales (x≈910–1120, y≈340–390; x≈775–815, y≈345–360) y otro en la planta alta (x≈950–1070, y≈140–215)
1662. [media] Detalles de fachada — ventanas de la planta alta del edificio del supermercado
   - Captura: Recercados blancos marcados alrededor de cada ventana alta (x≈840–1065, y≈95–300)
   - Juego: Ventanas sin recercados
1663. [baja] Huecos — reja de la ventana del primer plano izquierdo
   - Captura: Reja pintada de verde (x≈193–293, y≈365–455)
   - Juego: Reja gris oscura (x≈105–230, y≈350–465)
1664. [baja] Huecos — planta alta del edificio del supermercado
   - Captura: Ventanas altas con balcones individuales de forja negra, sin contraventanas
   - Juego: Contraventanas verdes (x≈825–860, y≈255–300) y ropa tendida en un balcón (x≈975–1055, y≈230–285)
1665. [baja] Detalles de fachada — letrero del supermercado
   - Captura: Letrero rojo de «Dia» en banderola (x≈1090–1150, y≈250–300)
   - Juego: No hay letrero rojo; hay unos cuadros de colores en el escaparate (x≈1095–1135, y≈370–440)
1666. [baja] Cubierta — edificio del supermercado (derecha)
   - Captura: Azotea con barandilla metálica sobre el pretil (x≈825–945, y≈85–200)
   - Juego: Remate liso sin barandilla (x≈715–1155, borde superior)
1667. [baja] Calzada — grieta y tapa de la calzada
   - Captura: Asfalto sin grieta longitudinal
   - Juego: Grieta oscura por el centro (x≈575–660, y≈370–693) y una tapa de registro (x≈490–550, y≈500–525)
1668. [baja] Acera y bordillo — acera derecha
   - Captura: Acera gris con bordillo gris (x≈790–1070, y≈390–530)
   - Juego: Baldosas grises con bordillo blanco (x≈690–1440, y≈360–693)
1669. [baja] Mobiliario — farol de pared del primer plano izquierdo
   - Captura: Farol de forja con brazo sobre la fachada (x≈280–360, y≈150–235)
   - Juego: No hay farol en esa fachada
1670. [baja] Mobiliario — señal de prohibido aparcar
   - Captura: Señal de prohibido aparcar con placa en un poste de la acera derecha (x≈1045–1085, y≈320–490)
   - Juego: No hay señal
**Vista #169** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_169.jpg

1671. [media] Color de fachada — casa del primer plano derecho
   - Captura: Fachada crema/marfil (x≈1050–1440, y≈0–450)
   - Juego: Fachada gris beige (x≈1080–1440)
1672. [media] Color de fachada — casas blancas del lado derecho (tramo medio)
   - Captura: Fachadas blancas (x≈900–1060, y≈160–430)
   - Juego: Fachada gris (x≈895–1080, y≈170–530)
1673. [media] Huecos — ventana grande del primer plano izquierdo
   - Captura: Reja de forja abombada con remate decorativo en la parte baja (x≈0–240, y≈305–580)
   - Juego: Reja recta más pequeña (x≈0–95, y≈355–525)
1674. [media] Huecos — puerta nº 27 del lado izquierdo
   - Captura: Puerta de madera marrón (x≈380–435, y≈330–470)
   - Juego: En ese tramo una ventana con persiana marrón (x≈280–345, y≈355–435) y una puerta clara más adelante (x≈435–470, y≈355–420)
1675. [media] Huecos — casa del primer plano derecho: planta baja
   - Captura: Ventana con reja blanca dentro de un recercado moldurado beige (x≈1130–1310, y≈330–450)
   - Juego: Cochera con puerta de lamas verticales gris azulado y marco beige (x≈1140–1420, y≈355–693)
1676. [media] Huecos — casas del lado derecho (tramo medio)
   - Captura: Puerta (x≈915–930, y≈345–425) y ventanas con reja (x≈970–995, y≈360–420)
   - Juego: Una puerta de reja ancha (x≈930–985, y≈360–480)
1677. [media] Detalles de fachada — casa nº 27 del primer plano izquierdo
   - Captura: Recercados y pilastra pintados de verde sobre fondo crema: alrededor de la ventana grande (x≈0–255, y≈285–530) y de la puerta (x≈370–470, y≈140–470)
   - Juego: Fachada beige lisa sin recercados verdes (x≈0–495)
1678. [baja] Detalles de fachada — balcón de la casa del primer plano derecho
   - Captura: Barandilla de forja con balaustres curvos y volutas sobre una cornisa moldurada (x≈1100–1345, y≈160–300)
   - Juego: Barandilla de barrotes rectos sobre losa lisa (x≈1085–1440, y≈55–295)
1679. [baja] Cubierta — segunda casa de la izquierda
   - Captura: Alero de teja con canecillos (x≈470–600, y≈160–245)
   - Juego: Alero de teja liso sin canecillos (x≈495–640, y≈215–300)
1680. [baja] Calzada — grieta y mancha de la calzada
   - Captura: Asfalto sin grieta longitudinal ni mancha
   - Juego: Grieta oscura por el centro (x≈610–720, y≈360–693) y una mancha húmeda (x≈430–530, y≈600–680)
1681. [baja] Acera y bordillo — acera derecha
   - Captura: Acera gris con bordillo gris
   - Juego: Baldosas grises con bordillo blanco (x≈760–1300, y≈360–693)
1682. [baja] Otros — cables que cruzan la calle
   - Captura: Cables que cruzan la calle (x≈690–830, y≈260–275)
   - Juego: No hay cables
**Vista #170** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_170.jpg

1683. [media] Huecos — edificio blanco del primer plano izquierdo
   - Captura: Pared ciega con un hueco de cochera oscuro y abierto en el borde (x≈0–75, y≈400–580)
   - Juego: Cochera con cierre enrollable blanco (x≈345–480, y≈335–515)
1684. [media] Huecos — casa del primer plano derecho: planta baja
   - Captura: Puerta doble metálica gris con barrotes verticales (x≈1155–1275, y≈325–580) y ventana con reja negra (x≈975–1030, y≈330–410)
   - Juego: Una ventana con reja y persiana marrón (x≈1050–1150, y≈350–480); no se ve puerta
1685. [media] Detalles de fachada — casa del primer plano derecho: recercados
   - Captura: Recercados y cornisa en rosa salmón alrededor de ventanas y balcones (x≈965–1300, y≈30–300)
   - Juego: Sin recercados de color (x≈910–1250)
1686. [media] Cubierta — edificio blanco del primer plano izquierdo
   - Captura: Fachada alta y lisa rematada con pretil plano, sin teja (x≈0–500, y≈110–590)
   - Juego: Alero de teja naranja a media altura (x≈0–500, y≈220–325) delante de un volumen blanco más alto
1687. [media] Cubierta — casa del primer plano derecho
   - Captura: Azotea con pretil plano (x≈925–1280, y≈0–180)
   - Juego: Alero de teja roja (x≈910–1200, y≈0–210)
1688. [baja] Zócalo — casa del primer plano derecho
   - Captura: Zócalo gris de textura pétrea (x≈925–1330, y≈410–600)
   - Juego: Zócalo beige (x≈920–1250, y≈410–590)
1689. [baja] Calzada — estado del asfalto
   - Captura: Asfalto muy agrietado en toda la calzada (x≈300–1200, y≈450–693)
   - Juego: Superficie lisa con una sola grieta central (x≈660–715, y≈400–693)
1690. [baja] Acera y bordillo — acera izquierda
   - Captura: Solería parda (x≈240–520, y≈470–693)
   - Juego: Baldosas grises con bordillo blanco (x≈60–620, y≈400–693)
1691. [baja] Vegetación — plantas al pie de la fachada ocre
   - Captura: No hay plantas
   - Juego: Matas con flores al pie de la fachada (x≈1255–1440, y≈580–693)
1692. [baja] Otros — ropa tendida en el balcón derecho
   - Captura: No hay ropa tendida
   - Juego: Toalla amarilla colgada del balcón (x≈1055–1125, y≈195–265)
1693. [baja] Otros — aparato de aire acondicionado
   - Captura: La fachada ocre del borde derecho no tiene aparato
   - Juego: Aparato de aire acondicionado en lo alto de la fachada ocre (x≈1265–1440, y≈0–80)

### Calle Don Benito

**Vista #171** — 02_Desde_un_extremo_hacia_el_otro.jpg (mayo de 2024) · hoja a_171.jpg

1694. [alta] Geometría — nave del lado izquierdo
   - Captura: Nave industrial blanca con grandes portones metálicos azul grisáceo (x≈370–445, y≈275–390; x≈530–560, y≈305–375) y cubierta plana
   - Juego: Casas blancas de una planta con tejado de teja naranja (x≈300–630, y≈275–410)
1695. [media] Geometría — bulevar central
   - Captura: Bulevar estrecho que empieza por delante de la cámara con un remate redondeado (x≈560–640, y≈455–485)
   - Juego: Bulevar ancho que llega hasta el primer plano, con bordillos blancos (x≈200–720, y≈360–693)
1696. [media] Huecos — planta baja de la casa del primer plano derecho
   - Captura: Pared ciega con zócalo de piedra gris, sin huecos (x≈1000–1440, y≈300–560)
   - Juego: Cochera con cierre enrollable blanco (x≈1245–1440, y≈335–650) y ventana con persiana blanca (x≈1060–1125, y≈355–450)
1697. [media] Detalles de fachada — casas del lado derecho: cornisa y balcones
   - Captura: Cornisa y bases de los balcones pintadas en salmón/ocre (x≈880–1240, y≈0–310)
   - Juego: Fachadas sin color en cornisa ni balcones (x≈820–1440)
1698. [media] Mobiliario — poste en primer plano izquierdo
   - Captura: No hay ningún poste delante de la cámara
   - Juego: Un poste blanco grueso ocupa de arriba abajo el primer plano izquierdo (x≈115–190, y≈0–693)
1699. [media] Mobiliario — farolas del bulevar
   - Captura: Farolas altas de doble brazo en el bulevar (x≈645–692, y≈205–400; x≈703–720, y≈295–330)
   - Juego: No hay farolas en el bulevar (solo el poste del primer plano)
1700. [media] Muros y vallas — valla de chapa del lado izquierdo
   - Captura: Valla de chapa ondulada gris a lo largo de la acera izquierda (x≈0–300, y≈350–445)
   - Juego: No hay valla; se ve la fachada blanca de un edificio (x≈0–200, y≈300–430)
1701. [baja] Detalles de fachada — celosía de la casa del primer plano derecho
   - Captura: Celosía de bloques blancos calados en la fachada (x≈1272–1310, y≈175–255)
   - Juego: No hay celosía
1702. [baja] Detalles de fachada — tejadillo sobre la cochera derecha
   - Captura: No hay tejadillo a media altura
   - Juego: Tejadillo de teja naranja sobre la cochera (x≈1165–1440, y≈225–305)
1703. [baja] Cubierta — pérgola en la azotea del lado derecho
   - Captura: Pérgola metálica sobre una azotea (x≈830–1010, y≈135–215)
   - Juego: No hay pérgola
1704. [baja] Marcas viales — bordillo derecho
   - Captura: Bordillo gris sin pintar
   - Juego: Línea amarilla pintada en el bordillo (x≈1140–1330, y≈580–693)
1705. [baja] Mobiliario — señal triangular en la acera derecha
   - Captura: Señal triangular de peligro en un poste (x≈930–960, y≈340–460)
   - Juego: No hay señal
**Vista #172** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_172.jpg

1706. [alta] Muros y vallas — verja de la nave izquierda
   - Captura: Verja de barrotes metálicos oscuros sobre un murete blanco a lo largo de la acera, con la nave retranqueada detrás (x≈0–500, y≈270–420)
   - Juego: No hay verja ni murete: la fachada de la nave da directamente a la acera (x≈0–520, y≈110–410)
1707. [media] Geometría — altura de la casa del primer plano derecho
   - Captura: Fachada alta: el alero va de y≈190 (x≈1240) a y≈130 (x≈1440)
   - Juego: Fachada más baja: el alero de teja va de y≈300 (x≈1240) a y≈250 (x≈1440)
1708. [media] Huecos — nave del lado izquierdo
   - Captura: Portones metálicos grises grandes (x≈155–325, y≈220–355)
   - Juego: Puertas azul verdoso (x≈0–135, y≈340–415; x≈210–280, y≈345–405)
1709. [media] Huecos — portón del lado derecho
   - Captura: Portón metálico gris azulado de arco rebajado (x≈1045–1185, y≈350–515)
   - Juego: Puerta con panel de rejilla y marco blanco (x≈1090–1195, y≈350–530)
1710. [media] Detalles de fachada — nave del lado izquierdo
   - Captura: Pilastras, franjas y marcos de ventana en ocre amarillo sobre fondo blanco (x≈0–500, y≈200–385)
   - Juego: Fachada blanca lisa con ventanas corridas grises (x≈0–520, y≈200–350)
1711. [media] Detalles de fachada — casa de dos plantas del lado derecho
   - Captura: Puerta en arco con recercado salmón (x≈895–950, y≈335–410) y recercado salmón en la ventana alta (x≈900–945, y≈235–300)
   - Juego: Puerta rectangular sin recercado de color (x≈920–945, y≈350–430)
1712. [baja] Marcas viales — bordillo derecho
   - Captura: Bordillo gris sin pintar
   - Juego: Línea amarilla pintada en el bordillo (x≈1155–1290, y≈610–693)
1713. [baja] Acera y bordillo — pavimento del bulevar
   - Captura: Losetas grises/beige con bordillo de granito (x≈480–700, y≈400–693)
   - Juego: Adoquín gris en espiga con bordillos blancos (x≈140–720, y≈360–693)
1714. [baja] Otros — cables en la fachada derecha
   - Captura: Cables grapados en lo alto de la fachada (x≈1230–1440, y≈180–230)
   - Juego: No hay cables
**Vista #173** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_173.jpg

1715. [alta] Muros y vallas — tapia del lado derecho
   - Captura: Tapia blanca larga a lo largo de la acera derecha (x≈840–1440, y≈355–460)
   - Juego: No hay tapia: delante de la nave hay una explanada pavimentada abierta (x≈1000–1440, y≈380–490)
1716. [media] Huecos — casa blanca larga del lado izquierdo
   - Captura: Ventana con reja decorativa granate (x≈360–430, y≈360–435) y una puerta marrón (x≈545–560, y≈360–435)
   - Juego: Cochera con cierre enrollable blanco (x≈165–385, y≈330–555) y una ventana pequeña con reja (x≈440–470, y≈355–375)
1717. [media] Cubierta — nave del lado derecho
   - Captura: Cubierta verde (x≈1175–1440, y≈135–215)
   - Juego: Nave blanca con cubierta blanca (x≈860–1440, y≈205–260)
1718. [media] Cubierta — casa blanca larga del lado izquierdo
   - Captura: Remate plano con pretil, sin teja (x≈130–600, y≈240–330)
   - Juego: Alero de teja naranja (x≈0–700, y≈180–340)
1719. [media] Vegetación — masa granate en primer plano derecho
   - Captura: No hay nada en ese punto (calzada y un coche plateado, x≈1255–1440, y≈440–510)
   - Juego: Una gran masa granate, como una copa de arbusto, ocupa el primer plano derecho (x≈1160–1440, y≈400–693)
1720. [media] Otros — cajas apiladas tras la tapia derecha
   - Captura: Pilas de cajas de plástico verdes, azules y blancas (x≈975–1440, y≈200–395)
   - Juego: No hay cajas
1721. [baja] Acera y bordillo — bordillo de la acera izquierda
   - Captura: Bordillo gris (x≈200–650, y≈420–693)
   - Juego: Bordillo blanco (x≈0–300, y≈520–693)
1722. [baja] Mobiliario — farola del bulevar
   - Captura: La farola más cercana está más adelante en el bulevar (x≈805–835, y≈190–405)
   - Juego: Una farola muy cerca de la cámara en el bulevar (x≈940–975, y≈0–560)

### Calle Luis Cernuda

**Vista #174** — 02_Desde_un_extremo_hacia_el_otro.jpg (Fecha de toma no indicada) · hoja a_174.jpg

1723. [alta] Color de fachada — casa del tramo medio derecho
   - Captura: Casa blanca con zócalo ocre (x≈810–940, y≈280–500)
   - Juego: Casa gris antracita con tejado de teja roja (x≈860–955, y≈190–440)
1724. [media] Geometría — casa del tramo medio derecho
   - Captura: Casa de una planta con pretil plano (x≈830–940, y≈240–500)
   - Juego: Casa de dos plantas (x≈860–955, y≈190–440)
1725. [media] Huecos — planta baja del bloque de la izquierda
   - Captura: Puerta acristalada de marco blanco dentro de un recercado beige (x≈345–425, y≈330–450)
   - Juego: Cochera con puerta doble blanca (x≈0–150, y≈365–610) y una ventana con persiana (x≈350–415, y≈355–440)
1726. [media] Huecos — edificio del primer plano derecho: planta baja
   - Captura: Ventana grande con reja abombada y persiana blanca (x≈1190–1440, y≈340–660)
   - Juego: Puerta doble de madera marrón (x≈1015–1100, y≈365–560)
1727. [media] Huecos — edificio del primer plano derecho: planta alta
   - Captura: Pared ciega con cables, sin balcón (x≈940–1440, y≈0–340)
   - Juego: Balcón de forja negra con macetas (x≈950–1125, y≈140–305) y ventana con persiana blanca (x≈1015–1090, y≈50–150)
1728. [media] Detalles de fachada — bloque de tres plantas de la izquierda
   - Captura: Recercados moldurados beige en las ventanas e imposta corrida entre plantas (x≈0–620, y≈90–300)
   - Juego: Fachada lisa sin recercados ni imposta
1729. [media] Zócalo — bloque de tres plantas de la izquierda
   - Captura: Zócalo alto chapado de piedra rosada con juntas verticales (x≈0–600, y≈390–640)
   - Juego: Zócalo pintado marrón claro (x≈200–600, y≈405–560)
1730. [media] Cubierta — edificio del primer plano derecho
   - Captura: Remate plano con pretil, sin teja (x≈940–1210, y≈0–80)
   - Juego: Alero de teja roja (x≈925–1030, y≈0–130)
1731. [baja] Huecos — balcones del bloque de la izquierda
   - Captura: Balcones de forja curvada con volutas en la base (x≈0–230, y≈60–225; x≈340–450, y≈195–290)
   - Juego: Balcones de barrotes rectos sobre losa lisa (x≈0–240, y≈120–295; x≈335–450, y≈230–310)
1732. [baja] Acera y bordillo — acera derecha
   - Captura: Baldosa gris cuadrada (x≈760–1150, y≈370–693)
   - Juego: Enlosado claro irregular de piedra (x≈780–960, y≈385–540)
1733. [baja] Vegetación — maceta en la acera derecha
   - Captura: No hay macetas
   - Juego: Maceta con planta junto a la puerta (x≈945–990, y≈470–530)
1734. [baja] Otros — ropa tendida en el bloque de la izquierda
   - Captura: No hay ropa tendida
   - Juego: Ropa colgada de un balcón de la segunda planta (x≈400–450, y≈60–120)
1735. [baja] Otros — cables en la fachada derecha
   - Captura: Cables grapados a lo largo de la fachada (x≈940–1440, y≈140–300)
   - Juego: No hay cables
**Vista #175** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_175.jpg

1736. [media] Color de fachada — edificio de mampostería del primer plano izquierdo
   - Captura: Muro de mampostería de piedra parda con un pilar de esquina (x≈0–200, y≈130–560)
   - Juego: Fachada blanca enfoscada que sigue hasta el borde izquierdo (x≈0–200, y≈270–580)
1737. [media] Huecos — casa larga de la izquierda
   - Captura: Ventana con reja en x≈365–400 (y≈355–435) y puertas pequeñas en x≈462–475
   - Juego: Ventana grande con reja en x≈160–280 (y≈350–470) y puerta de madera en x≈370–420 (y≈350–445)
1738. [media] Calzada — firme del cruce
   - Captura: Asfalto gris beige con tapas de registro (x≈530–620, y≈475–550)
   - Juego: Superficie lisa color crema muy claro
1739. [media] Marcas viales — paso de peatones del cruce
   - Captura: Paso de peatones de franjas blancas en la mitad derecha (x≈920–1440, y≈415–550)
   - Juego: No hay paso de peatones; solo una línea discontinua tenue (x≈1030–1440, y≈460–600)
1740. [media] Muros y vallas — cancela azul del primer plano izquierdo
   - Captura: Cancela metálica azul (x≈0–75, y≈350–580)
   - Juego: No hay cancela
1741. [baja] Cubierta — casa larga de la izquierda
   - Captura: Tejado de teja sin placas solares (x≈195–600, y≈205–300)
   - Juego: Placas solares negras sobre el tejado (x≈200–345, y≈245–285; x≈440–550, y≈305–315)
1742. [baja] Cubierta — casa blanca con canecillos del frente
   - Captura: Remate plano con cornisa de canecillos (x≈1065–1190, y≈210–225)
   - Juego: En ese tramo empieza un tejado de teja (x≈1065–1345, y≈225–245)
1743. [baja] Mobiliario — señales de la esquina izquierda
   - Captura: Señal de prohibido aparcar con placa en un poste (x≈225–280, y≈318–515), señal azul pequeña y placa blanca en la pared (x≈155–190, y≈345–380)
   - Juego: No hay señales
1744. [baja] Mobiliario — farol de la esquina del edificio del frente
   - Captura: Farol de pared en la esquina del edificio crema (x≈715–735, y≈245–285)
   - Juego: No hay farol en esa esquina
**Vista #176** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_176.jpg

1745. [alta] Geometría — tramo del lado derecho tras el primer plano
   - Captura: Valla de chapa gris oscura (x≈800–960, y≈290–530), un pilar blanco de ladrillo (x≈960–1060, y≈205–620) y muretes; no hay casas en ese tramo
   - Juego: Hilera de casas beige de dos plantas con ventanas y balcón (x≈760–965, y≈80–490)
1746. [media] Color de fachada — casas del tramo medio izquierdo
   - Captura: Fachadas blancas (x≈420–630, y≈220–440)
   - Juego: Fachadas beige (x≈460–640, y≈265–440)
1747. [media] Huecos — edificio del primer plano izquierdo
   - Captura: Cochera grande con puerta metálica gris (x≈130–345, y≈285–560)
   - Juego: Ventana con persiana blanca (x≈270–355, y≈355–480), sin cochera
1748. [media] Huecos — segunda casa de la izquierda
   - Captura: Cochera con puerta metálica gris (x≈462–510, y≈325–440)
   - Juego: Puerta de madera marrón (x≈485–510, y≈350–435)
1749. [media] Huecos — edificio del primer plano derecho: planta baja
   - Captura: Cochera grande con puerta de chapa gris bajo un dintel en arco (x≈1120–1440, y≈240–693)
   - Juego: Puerta doble blanca con ventanillos (x≈1080–1305, y≈370–640)
1750. [media] Huecos — edificio del primer plano derecho: planta alta
   - Captura: Planta alta blanca y ciega (x≈1050–1440, y≈0–250)
   - Juego: Balcón de forja negra (x≈1000–1400, y≈15–295) y ventana con persiana blanca (x≈1085–1255, y≈0–90)
1751. [media] Detalles de fachada — tejadillo verde del primer plano izquierdo
   - Captura: Tejadillo verde sobre una puerta en el borde izquierdo (x≈0–220, y≈260–410)
   - Juego: No hay tejadillo
1752. [media] Cubierta — edificio del primer plano izquierdo
   - Captura: Remate plano blanco sin teja (x≈0–420, y≈130–290)
   - Juego: Alero de teja naranja (x≈0–480, y≈220–325)
1753. [baja] Calzada — grieta de la calzada
   - Captura: Asfalto sin grieta longitudinal
   - Juego: Grieta oscura por el centro (x≈555–660, y≈380–693)
1754. [baja] Mobiliario — farol de pared de la izquierda
   - Captura: Farol de forja en la esquina de la segunda casa (x≈430–480, y≈220–275)
   - Juego: No hay farol
1755. [baja] Otros — bombona en la acera izquierda
   - Captura: No hay bombona
   - Juego: Bombona naranja junto a la puerta (x≈515–530, y≈405–425)

### Calle Rafael Alberti

**Vista #177** — 02_Desde_un_extremo_hacia_el_otro.jpg (mayo de 2024) · hoja a_177.jpg

1756. [alta] Geometría — edificio del primer plano izquierdo
   - Captura: Casa encalada de una planta con un muro de ladrillo visto rojo por encima y chimeneas (x≈0–560, y≈210–630)
   - Juego: Edificio blanco de dos plantas con balcón y ventanas en la planta alta (x≈0–515, y≈0–693)
1757. [media] Huecos — edificio del primer plano izquierdo: planta baja
   - Captura: Portón grande de madera marrón con jamba blanca/gris (x≈220–405, y≈360–640)
   - Juego: Ventana con persiana blanca (x≈405–470, y≈360–530) y una puerta de madera en el borde (x≈0–75, y≈395–693)
1758. [media] Huecos — edificio rojo de la derecha: planta baja
   - Captura: Cochera con puerta blanca (x≈1060–1195, y≈315–470), ventana con reja (x≈975–1020, y≈330–385) y puerta (x≈935–955, y≈335–415)
   - Juego: Dos puertas con panel de rejilla (x≈985–1020, y≈350–435; x≈1090–1165, y≈350–480) y una puerta marrón (x≈890–915, y≈350–405), sin cochera
1759. [media] Huecos — edificio rojo de la derecha: plantas altas
   - Captura: Un solo balcón de forja negra en la primera planta (x≈955–1105, y≈225–310); el resto, ventanas con persiana
   - Juego: Varios balcones (x≈1055–1175, y≈55–160; x≈1055–1175, y≈240–310; x≈960–1025, y≈275–320; x≈878–915, y≈220–260) y ropa tendida
1760. [media] Huecos — edificio blanco del primer plano derecho
   - Captura: Pared blanca ciega con un cable (x≈1250–1440, y≈0–550)
   - Juego: Puerta con cortina de tiras azules y blancas (x≈1390–1440, y≈370–560), ventana alta (x≈1385–1440, y≈80–210) y caja de contador (x≈1290–1345, y≈445–490)
1761. [media] Detalles de fachada — edificio rojo de tres plantas de la derecha
   - Captura: Pilastras, cornisas y recercados en amarillo ocre sobre el rojo (x≈870–1250, y≈0–470)
   - Juego: Fachada roja lisa, sin molduras amarillas (x≈875–1230)
1762. [media] Zócalo — edificio rojo de la derecha
   - Captura: Zócalo chapado de plaqueta de piedra (x≈870–1060, y≈375–445) y basamento de piedra (x≈1190–1255, y≈445–525)
   - Juego: Zócalo pintado verde oliva/marrón (x≈875–1230, y≈380–510)
1763. [baja] Cubierta — chimeneas del lado izquierdo
   - Captura: Dos chimeneas blancas sobre los tejados (x≈340–375, y≈225–245; x≈560–590, y≈235–290)
   - Juego: No se ven chimeneas
1764. [baja] Acera y bordillo — acera izquierda
   - Captura: Baldosa beige con bordillo gris (x≈300–700, y≈380–693)
   - Juego: Baldosa blanca con bordillo blanco (x≈370–745, y≈360–693)
1765. [baja] Mobiliario — contenedores de la acera izquierda
   - Captura: Contenedores amarillo y azul junto a la fachada (x≈635–680, y≈370–410)
   - Juego: No hay contenedores
1766. [baja] Mobiliario — farol del edificio rojo
   - Captura: Farol de pared en la esquina del edificio rojo (x≈850–870, y≈270–295)
   - Juego: No hay farol
**Vista #178** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_178.jpg

1767. [media] Color de fachada — edificio de tres plantas de la izquierda
   - Captura: Fachada rosa melocotón (x≈0–625, y≈0–620)
   - Juego: Fachada beige arena (x≈0–630)
1768. [media] Color de fachada — edificio del fondo de la calle
   - Captura: Casa blanca de dos plantas con tejado de teja (x≈640–710, y≈295–365)
   - Juego: Edificio de ladrillo rojo de dos plantas (x≈625–715, y≈300–365)
1769. [media] Huecos — edificio de la izquierda: planta baja
   - Captura: Escaparate grande con reja de tijera (x≈20–410, y≈345–565)
   - Juego: Cochera con cierre enrollable marrón (x≈0–300, y≈330–693) y una puerta con cortina de tiras verdes (x≈415–495, y≈350–530)
1770. [media] Huecos — casa blanca de una planta de la derecha
   - Captura: Una ventana alta con reja (x≈930–955, y≈235–280) y un ventanuco (x≈855–870, y≈280–300)
   - Juego: Dos ventanas con reja a la altura de la calle (x≈900–925 y x≈960–1000, y≈350–420) y una cochera blanca (x≈862–890, y≈340–410)
1771. [media] Detalles de fachada — toldo del edificio de la izquierda
   - Captura: Toldo a rayas rojas y blancas sobre el escaparate (x≈0–435, y≈270–345)
   - Juego: No hay toldo
1772. [media] Cubierta — casa blanca de una planta de la derecha
   - Captura: Remate plano sin teja (x≈840–1040, y≈190–290)
   - Juego: Tejado de teja naranja (x≈860–1040, y≈270–335)
1773. [media] Marcas viales — paso de peatones y línea de detención
   - Captura: Paso de peatones (x≈620–870, y≈415–440), línea de detención (x≈750–875, y≈450–460) y marca blanca (x≈655–690, y≈380–400)
   - Juego: Calzada sin marcas
1774. [media] Muros y vallas — tapia de la derecha
   - Captura: Tapia encalada desconchada con albardilla lisa, sin teja (x≈1030–1440, y≈80–630)
   - Juego: Muro con alero de teja naranja a media altura (x≈1035–1440, y≈250–320) y otro volumen blanco encima (y≈160–300)
1775. [baja] Mobiliario — farol de la casa de la derecha
   - Captura: Farol de forja en la fachada (x≈885–915, y≈232–275)
   - Juego: No hay farol
1776. [baja] Otros — banderines sobre la calle
   - Captura: Guirnalda de banderines azules cruzando la calle (x≈620–1200, y≈0–290)
   - Juego: No hay banderines
**Vista #179** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_179.jpg

1777. [alta] Geometría — lado izquierdo de la calle
   - Captura: Fachada blanca alta y continua con zócalo ocre, alineada con la calle desde el primer plano hasta x≈650 (y≈0–620), con una ventana de reja negra y marco ocre (x≈385–485, y≈335–445)
   - Juego: Solo la esquina de un edificio en primer plano (x≈0–235, y≈155–670); detrás, una explanada pavimentada (x≈200–600, y≈390–520) y casas de una planta retranqueadas (x≈200–600, y≈290–460)
1778. [media] Huecos — edificio de la derecha: planta baja
   - Captura: Tienda con escaparate y cartel «Lydria's» (x≈820–950, y≈290–400) y una ventana con reja en recercado de piedra (x≈975–1090, y≈270–360)
   - Juego: Fila continua de locales con cierres enrollables y franja azul encima (x≈810–1440, y≈235–693)
1779. [media] Detalles de fachada — edificio de la derecha: recercados
   - Captura: Recercados moldurados de piedra beige en las ventanas (x≈975–1090, y≈270–360; x≈990–1100, y≈40–190)
   - Juego: Ventanas sin recercado
1780. [baja] Zócalo — edificio de la derecha
   - Captura: Zócalo beige con paneles gris oscuro (x≈980–1440, y≈420–600)
   - Juego: Sin zócalo: los cierres llegan al suelo
1781. [baja] Cubierta — pérgola en la azotea derecha
   - Captura: Pérgola/tejadillo sobre la azotea (x≈840–945, y≈80–210)
   - Juego: No hay pérgola
1782. [baja] Calzada — grieta de la calzada
   - Captura: Asfalto sin grieta longitudinal
   - Juego: Grieta oscura por el centro (x≈545–720, y≈370–693)
1783. [baja] Marcas viales — línea transversal en primer plano
   - Captura: Línea blanca transversal en la calzada (x≈420–720, y≈605–635)
   - Juego: Calzada sin marcas
1784. [baja] Otros — banderines sobre la calle
   - Captura: Guirnalda de banderas verdes y blancas cruzando la calle (x≈450–800, y≈0–270)
   - Juego: No hay banderines

### Calle de Luis Chamizo

**Vista #180** — 02_Desde_un_extremo_hacia_el_otro.jpg (mayo de 2024) · hoja a_180.jpg

1785. [media] Huecos — casa blanca del lado izquierdo: planta baja
   - Captura: Puerta de madera con recercado terracota (x≈465–510, y≈305–430) y ventana grande con reja en recercado blanco (x≈315–390, y≈315–485)
   - Juego: Puerta con cortina de tiras verdes y amarillas (x≈385–470, y≈350–480) y ventana con reja más adelante (x≈535–565, y≈350–425)
1786. [media] Huecos — casa rosa del lado derecho: planta alta
   - Captura: Un balcón de forja negra (x≈1040–1170, y≈140–215) y una ventana (x≈955–985, y≈190–250)
   - Juego: Tres balcones (x≈950–1000, x≈1010–1100, x≈1155–1400; y≈190–320)
1787. [media] Huecos — casa rosa del lado derecho: planta baja
   - Captura: Cochera con cierre gris (x≈950–1005, y≈340–415), ventana con reja negra en recercado blanco (x≈1050–1165, y≈330–440) y puerta con recercado blanco (x≈1355–1440, y≈345–440)
   - Juego: Ventana pequeña (x≈965–1000), puerta (x≈1040–1095, y≈350–465) y ventana con persiana blanca (x≈1200–1380, y≈345–490)
1788. [media] Detalles de fachada — casa rosa del lado derecho: balaustrada y recercados
   - Captura: Balaustrada de balaustres torneados en lo alto (x≈1180–1440, y≈45–250) y recercados/pilastras blancos (x≈1040–1170, y≈60–250; x≈1255–1440, y≈290–440)
   - Juego: Sin balaustrada ni recercados: ventana con persiana y balcón de barrotes rectos (x≈1155–1400, y≈105–300)
1789. [media] Zócalo — casa blanca del lado izquierdo
   - Captura: Zócalo alto de plaqueta terracota (x≈110–480, y≈420–570)
   - Juego: Sin zócalo en el primer plano (x≈0–470); solo un zócalo de plaqueta marrón más adelante (x≈470–580, y≈410–460)
1790. [baja] Color de fachada — edificio del borde izquierdo
   - Captura: Fachada gris oscura (x≈0–100, y≈150–580)
   - Juego: Fachada blanca con una ventana grande enrejada (x≈0–125, y≈355–670)
1791. [baja] Detalles de fachada — bloque de cuatro plantas del lado derecho
   - Captura: Frentes de balcón del mismo color que la fachada de ladrillo/beige (x≈790–935, y≈60–330)
   - Juego: Frentes de balcón azul grisáceo y toldos rosas (x≈825–955, y≈100–340)
1792. [baja] Calzada — grieta de la calzada
   - Captura: Asfalto sin grieta longitudinal
   - Juego: Grieta oscura por el centro (x≈730–920, y≈370–693)
1793. [baja] Acera y bordillo — acera derecha (tramo visible al fondo)
   - Captura: Solería en damero de baldosas terracota y blancas (x≈830–930, y≈390–440)
   - Juego: Baldosa clara lisa con bordillo blanco (x≈760–1440, y≈360–650)
1794. [baja] Otros — banderines y cables sobre la calle
   - Captura: Guirnalda de banderas verdes y blancas (x≈600–735, y≈0–230) y cables cruzando la calle (x≈600–935, y≈180–250)
   - Juego: No hay banderines ni cables
**Vista #181** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_181.jpg

1795. [media] Huecos — casa del primer plano izquierdo
   - Captura: Portón grande de madera marrón en arco (x≈425–515, y≈295–470) y ventana grande con reja negra en recercado resaltado (x≈170–295, y≈310–525)
   - Juego: Dos cocheras con cierre enrollable blanco (x≈315–450, y≈335–525; x≈470–530, y≈340–455) y una puerta con panel de rejilla (x≈0–155, y≈370–650)
1796. [media] Huecos — casa del primer plano derecho: planta alta
   - Captura: Dos balcones de forja negra (x≈1150–1260, y≈260–320; x≈1360–1440, y≈225–305)
   - Juego: Un frente de balcón macizo gris oscuro corrido (x≈1075–1425, y≈195–310)
1797. [media] Huecos — casa del primer plano derecho: planta baja
   - Captura: Ventana con reja negra (x≈1175–1255, y≈360–445) y un portal (x≈1400–1440, y≈345–520)
   - Juego: Cochera con puerta gris (x≈1175–1325, y≈350–440)
1798. [media] Cubierta — casa del primer plano derecho
   - Captura: Tejado de teja con alero a la calle (x≈1105–1440, y≈140–250)
   - Juego: Hastial con tejado a dos aguas hacia la calle (x≈1070–1440, y≈0–200)
1799. [baja] Zócalo — casa beige del lado derecho
   - Captura: Zócalo de piedra/ladrillo pardo rojizo (x≈995–1105, y≈395–455)
   - Juego: Franja gris oscura en la base (x≈960–1090, y≈400–430)
1800. [baja] Marcas viales — bordillo izquierdo
   - Captura: Bordillo sin pintar
   - Juego: Línea amarilla en el bordillo izquierdo (x≈420–520, y≈465–530)
1801. [baja] Mobiliario — farol de pared del primer plano izquierdo
   - Captura: Farol de forja grande con brazo (x≈390–455, y≈145–245)
   - Juego: Solo un farol pequeño más adelante (x≈510–540, y≈280–300)
1802. [baja] Mobiliario — contenedores del lado derecho
   - Captura: Contenedores amarillo y gris junto a la acera derecha (x≈780–820, y≈360–390)
   - Juego: No hay contenedores
1803. [baja] Otros — cables y banderines
   - Captura: Cables grapados en la fachada izquierda (x≈220–540, y≈210–300) y guirnalda de banderines azules (x≈420–830, y≈80–300)
   - Juego: No hay cables ni banderines
1804. [baja] Otros — bicicleta en la acera derecha
   - Captura: No hay bicicleta
   - Juego: Bicicleta junto a la fachada (x≈1090–1145, y≈410–425)
1805. [baja] Otros — bombona en la acera derecha
   - Captura: No hay bombona
   - Juego: Bombona naranja junto a la casa beige (x≈975–985, y≈405–420)
**Vista #182** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_182.jpg

1806. [media] Geometría — casas del lado izquierdo
   - Captura: Casas altas de dos plantas con pretil (remate de y≈175 en x≈180 a y≈310 en x≈620)
   - Juego: Casas de una planta con tejado de teja naranja (x≈150–545, y≈250–390), más bajas
1807. [media] Color de fachada — edificio de la tienda
   - Captura: Fachada crema con molduras terracota (x≈860–1440, y≈0–300)
   - Juego: Fachada blanca/gris
1808. [media] Huecos — casas del lado izquierdo
   - Captura: Portón oscuro (x≈0–90, y≈290–560), ventana con reja decorativa en marco terracota (x≈310–370, y≈360–420) y puerta marrón (x≈435–465, y≈345–425)
   - Juego: Cochera con cierre verde (x≈205–385, y≈340–385), ventanuco con reja (x≈435–465, y≈350–375) y una ventana en una casa gris (x≈0–125, y≈320–370)
1809. [media] Huecos — tienda del primer plano derecho
   - Captura: Escaparate con productos expuestos (x≈930–1090, y≈310–510) y puerta abierta (x≈1095–1205, y≈300–580)
   - Juego: Grandes locales con cierres metálicos y marcos grises (x≈925–1440, y≈290–693)
1810. [media] Huecos — edificio de la tienda: planta alta
   - Captura: Balcón corrido de forja negra a lo largo de la fachada (x≈860–1270, y≈0–250) con ventana enrejada (x≈950–1030, y≈0–195)
   - Juego: Ventana con contraventana de madera (x≈1165–1285, y≈0–170) y ventana con persiana (x≈960–1025, y≈125–250), sin balcón
1811. [media] Detalles de fachada — casas del lado izquierdo: pilastras y recercados
   - Captura: Pilastras, recercados y cornisa en terracota sobre fondo blanco (x≈160–620, y≈200–430)
   - Juego: Fachadas lisas sin molduras de color
1812. [media] Detalles de fachada — letrero de la droguería
   - Captura: Gran letrero «DROGUERÍA-PERFUMERÍA PAREDECOR S.L.» sobre la tienda (x≈880–1340, y≈160–310)
   - Juego: No hay letrero
1813. [media] Zócalo — tienda del primer plano derecho
   - Captura: Zócalo pintado de azul (x≈875–1095, y≈420–570; x≈1260–1440, y≈610–680)
   - Juego: Solo una tira estrecha de azulejo azul (x≈1100–1125, y≈500–600)
1814. [media] Cubierta — casas del lado izquierdo
   - Captura: Remate plano con pretil, sin teja visible
   - Juego: Tejado de teja naranja (x≈150–545, y≈250–330)
1815. [baja] Calzada — grieta de la calzada
   - Captura: Asfalto sin grieta longitudinal
   - Juego: Grieta oscura en la calzada (x≈480–635, y≈460–693)
1816. [baja] Mobiliario — farol de pared del lado izquierdo
   - Captura: Farol de forja en la fachada (x≈215–270, y≈195–250)
   - Juego: No hay farol
1817. [baja] Mobiliario — señal triangular en la acera derecha
   - Captura: Señal triangular en un poste (x≈800–830, y≈325–480)
   - Juego: No hay señal
1818. [baja] Otros — banderines y cables
   - Captura: Guirnalda de banderines rojos y amarillos (x≈180–760, y≈200–330) y cables en las fachadas (x≈0–620, y≈230–310)
   - Juego: No hay banderines ni cables

### Calle Olivo

**Vista #183** — 02_Desde_un_extremo_hacia_el_otro.jpg (mayo de 2024) · hoja a_183.jpg

1819. [media] Huecos — casa del primer plano izquierdo: planta baja
   - Captura: Portón grande de madera marrón con recercado blanco (x≈0–330, y≈340–693)
   - Juego: Ventana grande con marco blanco y macetas en el alféizar (x≈190–335, y≈365–545)
1820. [media] Huecos — casa del primer plano izquierdo: planta alta
   - Captura: Planta alta casi ciega, con una sola ventana con barandilla (x≈530–560, y≈180–295)
   - Juego: Balcón ancho con barandilla verde (x≈110–425, y≈60–295) y toldo verde y blanco (x≈320–440, y≈0–95)
1821. [media] Huecos — casa de una planta del primer plano derecho
   - Captura: Fachada ciega hacia la calle, sin ventanas (x≈915–1440, y≈340–580)
   - Juego: Ventana con persiana blanca, marco blanco y macetas (x≈1065–1250, y≈365–640)
1822. [media] Zócalo — casa del primer plano izquierdo
   - Captura: Basamento de ladrillo junto al portón (x≈240–330, y≈580–693) y zócalo gris (x≈330–550, y≈470–693)
   - Juego: Sin zócalo: la fachada blanca llega al suelo (x≈0–540)
1823. [baja] Huecos — cochera de la izquierda
   - Captura: Cochera con puerta metálica gris (x≈550–595, y≈340–485)
   - Juego: Cochera con cierre verde (x≈475–520, y≈360–460)
1824. [baja] Calzada — grieta y tapa de la calzada
   - Captura: Asfalto sin grieta longitudinal
   - Juego: Grieta oscura por el centro (x≈730–780, y≈365–693) y una tapa redonda (x≈630–680, y≈505–525)
1825. [baja] Acera y bordillo — acera izquierda
   - Captura: Baldosa beige con bordillo gris (x≈340–720, y≈380–693)
   - Juego: Baldosa clara con bordillo blanco
1826. [baja] Vegetación — macetas de la acera izquierda
   - Captura: No hay plantas en la acera izquierda
   - Juego: Planta cónica verde en maceta y macetas con flores (x≈180–485, y≈495–693)
1827. [baja] Mobiliario — poste con crucetas arriba a la derecha
   - Captura: No hay poste (solo una antena sobre un tejado, x≈905–925, y≈200–245)
   - Juego: Poste de madera con crucetas (x≈1310–1345, y≈20–125)
1828. [baja] Otros — bicicleta y cubo en la acera izquierda
   - Captura: No hay bicicleta ni cubo
   - Juego: Cubo azul (x≈537–560, y≈440–475) y bicicleta (x≈595–625, y≈400–440) junto a las fachadas
1829. [baja] Otros — cables en la fachada izquierda
   - Captura: Cables grapados en la fachada (x≈0–615, y≈170–310)
   - Juego: No hay cables
1830. [baja] Otros — bombona en la acera derecha
   - Captura: No hay bombona
   - Juego: Bombona naranja junto a la puerta (x≈845–860, y≈435–465)
**Vista #184** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_184.jpg

1831. [media] Color de fachada — segunda casa del lado derecho
   - Captura: Fachada rosa/roja (x≈810–890, y≈195–385)
   - Juego: Fachada ocre amarilla continua (x≈755–900)
1832. [media] Huecos — casa del primer plano izquierdo: planta baja
   - Captura: Cochera con portón de barrotes metálicos gris/blanco en un hueco rehundido (x≈120–385, y≈330–693)
   - Juego: Ventana con persiana blanca y marco blanco (x≈0–150, y≈350–620) y puerta con panel de rejilla (x≈355–445, y≈350–550)
1833. [media] Huecos — casa del primer plano izquierdo: planta alta
   - Captura: Ventana con barras negras horizontales (x≈375–465, y≈40–245)
   - Juego: Balcón de forja negra con macetas (x≈345–490, y≈175–295)
1834. [media] Huecos — casa amarilla del primer plano derecho: planta alta
   - Captura: Balcón corrido de forja negra con plantas (x≈1075–1440, y≈0–225)
   - Juego: Ventanas con marco blanco y macetas, sin balcón (x≈1095–1440, y≈0–160)
1835. [media] Muros y vallas — verja de la casa amarilla del primer plano derecho
   - Captura: Gran verja de forja negra con remate curvo que cierra el porche de la planta baja (x≈985–1440, y≈210–650)
   - Juego: No hay verja: pared lisa con una ventana grande enrejada (x≈1090–1440, y≈350–693)
1836. [baja] Vegetación — plantas de la acera izquierda
   - Captura: No hay plantas
   - Juego: Planta cónica verde (x≈50–165, y≈575–693) y macetas con flores (x≈20–90, y≈575–615)
1837. [baja] Otros — aparatos de aire acondicionado
   - Captura: Aparatos de aire en la fachada izquierda (x≈495–570, y≈195–280; x≈585–610, y≈170–215); ninguno en la derecha
   - Juego: Ninguno en la fachada izquierda; aparatos en la fachada derecha (x≈825–900, y≈185–260)
**Vista #185** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_185.jpg

1838. [media] Color de fachada — casa del primer plano izquierdo
   - Captura: Fachada blanca (x≈0–445, y≈0–630)
   - Juego: Fachada ocre/beige (x≈0–370)
1839. [media] Huecos — casa del primer plano izquierdo: planta baja
   - Captura: Cochera con puerta metálica marrón (x≈0–250, y≈270–693)
   - Juego: Ventana grande con reja y persiana blanca (x≈0–205, y≈350–693)
1840. [media] Huecos — edificio del primer plano derecho
   - Captura: Cochera grande con puerta de chapa ondulada gris (x≈980–1440, y≈240–693); sin ventanas ni balcón
   - Juego: Puerta con cortina de tiras de colores (x≈1050–1200, y≈350–635), ventanas (x≈930–970) y balcón de forja negra (x≈1000–1230, y≈120–300)
1841. [media] Detalles de fachada — edificio del primer plano derecho: marco rojo
   - Captura: Banda granate/roja que enmarca la cochera (x≈930–1440, y≈90–490) sobre muro pardo
   - Juego: Sin banda roja; recercados rosas en puerta y ventanas (x≈930–1200)
1842. [baja] Detalles de fachada — segunda casa de la izquierda
   - Captura: Recercados de piedra alrededor de la ventana enrejada y de la puerta (x≈480–590, y≈330–440)
   - Juego: Recercados blancos (x≈450–600, y≈350–500)
1843. [baja] Detalles de fachada — bajantes en primer plano
   - Captura: No se ven bajantes en primer plano
   - Juego: Bajantes blancos de arriba abajo a ambos lados (x≈350–380 y x≈1290–1335)
1844. [baja] Zócalo — casa del primer plano izquierdo
   - Captura: Zócalo de plaqueta de ladrillo rojizo (x≈250–445, y≈450–630)
   - Juego: Zócalo pintado marrón (x≈160–370, y≈560–693)
1845. [baja] Zócalo — edificio del primer plano derecho
   - Captura: Zócalo chapado de piedra (x≈910–985, y≈470–580)
   - Juego: Sin zócalo
1846. [baja] Cubierta — tejadillo del edificio del primer plano derecho
   - Captura: Tejadillo de chapa en lo alto (x≈905–1030, y≈0–100)
   - Juego: No hay tejadillo
1847. [baja] Calzada — parche y grieta de la calzada
   - Captura: Asfalto sin parche rectangular
   - Juego: Parche rectangular oscuro (x≈730–825, y≈420–460) y grieta (x≈725–740, y≈360–415)
1848. [baja] Mobiliario — farol del lado derecho
   - Captura: Farol de forja con brazo (x≈770–805, y≈235–310)
   - Juego: No hay farol

### Calle Antonio Machado

**Vista #186** — 02_Desde_un_extremo_hacia_el_otro.jpg (mayo de 2024) · hoja a_186.jpg

1849. [media] Color de fachada — hilera de adosados de la izquierda
   - Captura: Fachadas salmón/rosadas con pilastras y franjas crema y blancas (x≈0–700, y≈60–520)
   - Juego: Fachadas beige arena uniformes (x≈0–700)
1850. [media] Color de fachada — hilera de adosados de la derecha
   - Captura: Fachadas que alternan salmón, crema y rosa (x≈760–1440, y≈100–600)
   - Juego: Fachadas beige arena uniformes (x≈740–1440)
1851. [media] Color de fachada — casa roja del lado derecho
   - Captura: Una fachada roja en la hilera (x≈820–865, y≈280–400)
   - Juego: No hay fachada roja en ese tramo
1852. [media] Detalles de fachada — hilera de adosados de la izquierda: arcos y pilastras
   - Captura: Arcos rebajados en relieve sobre las ventanas de la planta baja (x≈55–360, y≈340–380; x≈460–520, y≈345–360) y pilastras crema entre casas (x≈340–420, y≈130–470)
   - Juego: Ventanas rectangulares con marco blanco, sin arcos ni pilastras (x≈80–565)
1853. [media] Detalles de fachada — hilera de adosados de la derecha: arcos y pilastras
   - Captura: Arcos rebajados sobre las ventanas de la planta baja (x≈900–1225, y≈340–380) y pilastras/paños de color alterno
   - Juego: Ventanas rectangulares con marco blanco, sin arcos ni pilastras (x≈850–1170)
1854. [baja] Zócalo — casa de zócalo de piedra del lado derecho
   - Captura: Zócalo chapado de piedra clara (x≈880–985, y≈385–460)
   - Juego: Zócalo de plaqueta de ladrillo (x≈790–845, y≈375–410) y zócalo terracota liso en el primer plano (x≈985–1440, y≈450–693)
1855. [baja] Acera y bordillo — acera derecha
   - Captura: Baldosa gris/parda con bordillo gris (x≈850–1440, y≈420–693)
   - Juego: Baldosa beige clara con bordillo blanco (x≈740–1300, y≈360–693)
1856. [baja] Otros — ropa tendida en el balcón izquierdo
   - Captura: No hay ropa tendida
   - Juego: Toalla rosa colgada del balcón (x≈250–310, y≈210–265)
**Vista #187** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_187.jpg

1857. [media] Color de fachada — hilera de adosados de la izquierda
   - Captura: Fachadas salmón con pilastras y franjas crema (x≈0–560, y≈80–520)
   - Juego: Casa ocre en primer plano (x≈0–235) y fachadas beige grisáceo después (x≈235–640)
1858. [media] Color de fachada — casa del primer plano derecho
   - Captura: Fachada crema y salmón en dos tonos (x≈1030–1440, y≈50–600)
   - Juego: Fachada blanca grisácea (x≈970–1440)
1859. [media] Huecos — casa del primer plano izquierdo
   - Captura: Balcón con base blanca moldurada (x≈0–340, y≈205–300) y ventana con reja abombada en la planta baja (x≈110–290, y≈360–495)
   - Juego: Ventana alta con marco blanco (x≈0–125, y≈30–215) y una puerta con cortina de tiras de colores (x≈0–90, y≈370–590)
1860. [media] Huecos — casa del primer plano derecho: planta baja
   - Captura: Dos ventanas anchas con reja negra (x≈1105–1205, y≈360–450; x≈1275–1440, y≈365–500)
   - Juego: Puerta doble de madera con marco blanco (x≈1015–1135, y≈350–545)
1861. [media] Detalles de fachada — hilera de adosados de la izquierda: arcos
   - Captura: Arcos rebajados sobre las ventanas de la planta baja (x≈0–290, y≈330–380; x≈425–510, y≈340–360)
   - Juego: Ventanas rectangulares, sin arcos (x≈310–560)
1862. [media] Detalles de fachada — hilera de adosados de la derecha: arcos
   - Captura: Arcos rebajados sobre las ventanas de la planta baja (x≈840–1440, y≈335–380)
   - Juego: Ventanas rectangulares, sin arcos (x≈820–945)
1863. [baja] Zócalo — hilera de la izquierda
   - Captura: Zócalo de plaqueta imitación ladrillo (x≈370–520, y≈400–500)
   - Juego: Sin zócalo diferenciado en ese tramo
1864. [baja] Otros — bicicleta en la acera derecha
   - Captura: No hay bicicleta
   - Juego: Bicicleta azul apoyada en la fachada (x≈1095–1410, y≈515–693)
1865. [baja] Otros — aparatos de aire acondicionado en la fachada izquierda
   - Captura: Dos aparatos de aire en la planta alta izquierda (x≈485–540, y≈195–245)
   - Juego: No hay aparatos en esa fachada
**Vista #188** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_188.jpg

1866. [media] Geometría — casa tras la tapia de la izquierda
   - Captura: Casa de dos plantas con tejado de teja y chimeneas que sobresale por encima de la tapia, con ventana y aparato de aire en su lateral (x≈440–720, y≈180–420)
   - Juego: Solo asoma un tejado bajo al final de la tapia (x≈595–680, y≈293–335); por encima de la tapia solo se ven unas copas verdes (x≈310–530, y≈265–300)
1867. [media] Huecos — cochera en la tapia de la izquierda
   - Captura: La tapia es ciega, sin puertas
   - Juego: Cochera con cierre enrollable verde (x≈430–555, y≈335–495)
1868. [media] Muros y vallas — tapia larga de la izquierda
   - Captura: Tapia alta beige, lisa y con remate plano sin teja (x≈0–630, y≈170–600)
   - Juego: Tapia blanca con alero de teja naranja corrido (x≈0–680, y≈215–335)
1869. [baja] Calzada — grieta de la calzada
   - Captura: Asfalto sin grieta longitudinal
   - Juego: Grieta oscura por el centro (x≈685–760, y≈390–693)
1870. [baja] Acera y bordillo — acera izquierda
   - Captura: Baldosa gris con bordillo gris (x≈150–700, y≈410–693)
   - Juego: Baldosa beige clara con bordillo blanco (x≈0–690, y≈390–693)

### Calle El Chiriveje

**Vista #189** — 02_Desde_un_extremo_hacia_el_otro.jpg (mayo de 2024) · hoja a_189.jpg

1871. [media] Color de fachada — casa de ladrillo del fondo derecho
   - Captura: En ese tramo de la derecha, casas blancas de dos plantas (x≈785–835, y≈295–365)
   - Juego: Una fachada de ladrillo rojo (x≈800–835, y≈285–365)
1872. [media] Huecos — edificio industrial del primer plano izquierdo
   - Captura: Banda continua de grandes ventanales de cristal verdoso en la planta baja (x≈0–530, y≈260–490), sin puertas
   - Juego: Dos filas de ventanas pequeñas apaisadas (x≈0–455, y≈60–370) y una puerta azul verdosa (x≈225–335, y≈340–485)
1873. [media] Huecos — casa blanca del primer plano derecho
   - Captura: Ventana apaisada (x≈1140–1270, y≈150–230) y ventana vertical (x≈1320–1390, y≈95–280) con recercados beige, y cochera con puerta metálica gris (x≈1135–1280, y≈330–430)
   - Juego: Dos ventanas con marco blanco una encima de otra (x≈1160–1260, y≈180–275 y y≈350–430), sin cochera
1874. [media] Huecos — edificio crema de dos plantas de la derecha
   - Captura: Tres balcones de forja en la planta alta (x≈910–1045, y≈265–310) y ventanas altas con reja en la baja (x≈1005–1040, y≈320–410)
   - Juego: Un solo balcón (x≈940–985, y≈300–330), una puerta (x≈955–980, y≈350–410) y una cochera con cierre marrón (x≈1010–1095, y≈340–440)
1875. [media] Detalles de fachada — edificio crema de dos plantas de la derecha
   - Captura: Pilastras, imposta y cornisa moldurada en tono ocre (x≈900–1115, y≈130–430)
   - Juego: Fachada beige lisa sin molduras (x≈900–1110)
1876. [media] Cubierta — edificio industrial del primer plano izquierdo
   - Captura: Volumen blanco de remate plano y recto, sin alero (borde superior de x≈0, y≈60 a x≈530, y≈270)
   - Juego: Nave con cubierta inclinada y alero volado oscuro (x≈0–540, y≈0–245)
1877. [media] Cubierta — casa blanca del primer plano derecho
   - Captura: Remate plano con pretil (x≈1115–1440, y≈0–140)
   - Juego: Alero de teja naranja (x≈1110–1440, y≈60–190)
1878. [media] Cubierta — edificio crema de dos plantas de la derecha
   - Captura: Remate plano con cornisa (x≈900–1115, y≈130–240)
   - Juego: Tejado de teja naranja (x≈900–1110, y≈185–270)
1879. [media] Mobiliario — farola de la acera derecha
   - Captura: Farola alta de brazo curvo en la acera derecha (x≈950–1030, y≈90–430)
   - Juego: No hay farola en la acera derecha
1880. [baja] Detalles de fachada — letrero del edificio del fondo izquierdo
   - Captura: Letrero de empresa en lo alto de la fachada (x≈535–615, y≈270–310) y verja azul (x≈540–600, y≈345–385)
   - Juego: Naves blancas iguales con puertas azul verdoso, sin letrero (x≈490–620)
1881. [baja] Calzada — firme de la calle
   - Captura: Asfalto gris pardo con parches y grietas
   - Juego: Superficie lisa beige muy clara con una sola grieta central (x≈685–795, y≈360–693)
1882. [baja] Mobiliario — contenedores de la acera izquierda
   - Captura: Cuatro contenedores azules, verde y amarillo junto al bordillo (x≈440–610, y≈380–480)
   - Juego: No hay contenedores
1883. [baja] Otros — bicicleta en la acera derecha
   - Captura: No hay bicicleta
   - Juego: Bicicleta junto a la fachada (x≈920–945, y≈380–405)
**Vista #190** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_190.jpg

1884. [alta] Muros y vallas — verja de la nave de la izquierda
   - Captura: Verja larga de barrotes metálicos con pilares, delante de la nave retranqueada (x≈0–460, y≈340–505)
   - Juego: No hay verja: la nave da directamente a la acera (x≈0–510, y≈150–465)
1885. [media] Huecos — nave de la izquierda
   - Captura: Una fila de ventanas grandes (x≈0–155, y≈215–285; x≈280–360, y≈265–300; x≈440–470, y≈290–315), sin puertas a la calle
   - Juego: Dos filas de ventanas apaisadas (y≈200–245 y y≈335–355) y una puerta azul verdosa (x≈410–450, y≈345–400)
1886. [media] Huecos — casa de la ventana con reja (derecha, tramo medio)
   - Captura: Ventana alta con reja negra (x≈1025–1080, y≈230–335) y pared blanca sin puertas debajo (x≈1000–1135, y≈335–430)
   - Juego: Ventana grande con persiana y marco beige (x≈1040–1195, y≈125–295) y cochera con cierre gris (x≈1035–1205, y≈335–515)
1887. [media] Huecos — casa del primer plano derecho
   - Captura: Ventana grande con persiana dentro de un recercado ocre moldurado (x≈1190–1385, y≈100–330), sin balcón
   - Juego: Balcón con frente gris translúcido (x≈1205–1440, y≈150–305) y puerta gris con marco beige (x≈1365–1440, y≈340–580)
1888. [media] Detalles de fachada — letrero de la nave de la izquierda
   - Captura: Rótulo grande pintado «…ES Y GRANITOS» en lo alto de la fachada (x≈280–480, y≈180–270)
   - Juego: Fachada sin rótulo
1889. [media] Mobiliario — farola de la acera derecha
   - Captura: Farola alta de brazo curvo en la acera derecha (x≈775–820, y≈220–380)
   - Juego: No hay farola en la acera derecha
1890. [baja] Huecos — casas blancas del tramo medio derecho
   - Captura: Ventanas con marco blanco sin contraventanas (x≈885–970, y≈240–290) y una cochera blanca (x≈885–920, y≈345–395)
   - Juego: Contraventanas verdes (x≈885–920, y≈265–305), puerta blanca (x≈895–915, y≈350–410) y ventana con reja (x≈950–985, y≈350–405)
1891. [baja] Calzada — firme de la calle
   - Captura: Asfalto gris pardo con grietas
   - Juego: Superficie lisa beige muy clara
1892. [baja] Vegetación — árboles tras la verja de la izquierda
   - Captura: Árboles y arbustos verdes tras la verja (x≈460–550, y≈310–380)
   - Juego: No hay árboles: naves blancas (x≈510–670)
**Vista #191** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_191.jpg

1893. [alta] Muros y vallas — verja de la nave de la derecha
   - Captura: Verja metálica blanca con pilares de ladrillo blanco a lo largo de la acera derecha (x≈830–1440, y≈340–430)
   - Juego: No hay verja: la nave da directamente a la acera (x≈960–1440, y≈90–470)
1894. [media] Color de fachada — nave del primer plano derecho
   - Captura: Parte alta de ladrillo caravista crema, panel inferior blanco y franja roja (x≈1045–1440, y≈110–420)
   - Juego: Nave blanca uniforme (x≈960–1440)
1895. [media] Huecos — bloque de pisos de ladrillo de la izquierda
   - Captura: Terrazas con antepechos de lamas blancas horizontales (x≈0–400, y≈150–300) y franjas blancas corridas
   - Juego: Balcones de forja negra con macetas (x≈0–565, y≈80–335)
1896. [media] Huecos — nave del primer plano derecho
   - Captura: Fachada ciega de ladrillo, sin puertas ni ventanas a la calle
   - Juego: Puertas azul verdoso (x≈1060–1100, y≈345–405; x≈1275–1405, y≈340–460) y filas de ventanas apaisadas (x≈965–1430, y≈180–355)
1897. [media] Cubierta — segunda nave de la derecha
   - Captura: Nave con cubierta a dos aguas y portón oscuro (x≈825–995, y≈295–350)
   - Juego: Edificio blanco de cubierta plana (x≈835–960, y≈275–385)
1898. [media] Mobiliario — farola del primer plano izquierdo
   - Captura: Poste de farola en la acera izquierda en primer plano (x≈215–245, y≈0–525)
   - Juego: No hay poste en primer plano; la farola más cercana está más adelante (x≈600–650, y≈270–405)
1899. [baja] Calzada — firme de la calle
   - Captura: Asfalto gris pardo muy agrietado
   - Juego: Superficie lisa beige clara
1900. [baja] Marcas viales — bordillo izquierdo
   - Captura: Línea amarilla pintada en el bordillo izquierdo (x≈150–650, y≈360–600)
   - Juego: Bordillo blanco sin pintar
1901. [baja] Mobiliario — farol en la fachada de la nave derecha
   - Captura: Farol con brazo en la fachada de la nave (x≈1255–1310, y≈180–215)
   - Juego: No hay farol
1902. [baja] Mobiliario — contenedor de la acera derecha
   - Captura: Contenedor verde junto a la acera derecha (x≈808–825, y≈360–385)
   - Juego: No hay contenedor

### Calle Gerardo Diego

**Vista #192** — 02_Tramo_norte.jpg (mayo de 2024) · hoja a_192.jpg

1903. [alta] Geometría — bloque de pisos cercano, lado izquierdo
   - Captura: Bloque blanco de cuatro plantas: planta baja porticada con pilares y tres plantas de ventanas encima (filas en y≈60–115, 145–200 y 225–285 en x≈345–445); ocupa x≈0–490, primer plano y medio.
   - Juego: Bloque de tres plantas: planta baja y solo dos filas de ventanas encima (y≈30–130 y 195–275 en x≈180–265; y≈185–225 y 270–305 en x≈460–485); ocupa x≈0–510.
   - Después: corregido: el bloque tiene ya sus cuatro plantas.
1904. [alta] Geometría — segundo bloque de pisos del lado izquierdo (plano medio)
   - Captura: Bloque blanco de cuatro plantas (planta baja porticada con pilares color teja y tres plantas), alero en y≈150–165, en x≈485–690.
   - Juego: Bloque de tres plantas (planta baja color teja y dos plantas con balconcillos), más bajo: remate en y≈215–225, en x≈510–690.
   - Después: corregido: cuatro plantas.
1905. [alta] Geometría — anchura de la calzada / posición del bordillo izquierdo
   - Captura: El bordillo izquierdo baja de x≈715 (y≈385) a x≈480 en el borde inferior; a la altura y≈650 la calzada va de x≈490 a x≈1300 y la explanada izquierda ocupa x≈0–490.
   - Juego: El bordillo izquierdo baja de x≈690 (y≈375) hasta x≈0 (y≈680): a la altura y≈650 la calzada va de x≈90 a x≈1290, casi un 50 % más ancha, y la explanada izquierda queda reducida a una cuña.
1906. [alta] Geometría — nave industrial tras la tapia derecha
   - Captura: Por encima de la tapia blanca (cuyo remate está en y≈345 en x=1440) se levanta la fachada de una nave de chapa ondulada roja, de x≈860 a x=1440 y hasta el borde superior de la imagen, con un tejadillo metálico oscuro en x≈865–1050, y≈180–280.
   - Juego: No hay nave: la tapia blanca sube como un único paramento liso hasta y≈145 (en x=1440) – y≈320 (en x≈830), rematado por una franja de teja roja (x≈830–1440, y≈70–320); no hay chapa roja.
1907. [media] Color de fachada — cuerpo de ladrillo al principio de la nave (derecha, plano medio)
   - Captura: Volumen de ladrillo visto rojizo con ventanas de pavés, encima de la tapia, en x≈810–865, y≈185–345.
   - Juego: En x≈800–850 solo hay un edificio blanco bajo (y≈300–360); no hay ladrillo.
1908. [media] Huecos — planta baja del bloque cercano de la izquierda
   - Captura: Soportal abierto: entre los pilares (x≈0–290, y≈300–450) se ve a través un patio-jardín con arbustos redondos y ventanas con reja al fondo; más a la derecha (x≈320–470) muros rehundidos color teja, sin cocheras.
   - Juego: Planta baja cerrada detrás de los pilares, con dos cocheras de persiana marrón (x≈0–25 y x≈100–215, y≈340–460), una puerta (x≈280–300) y una ventana (x≈395–420); no se ve ningún patio.
   - Después: cambiado: bajo el soportal ya no hay cocheras y su fondo queda en sombra; sigue cerrado al fondo (en la captura se ve el patio a través).
1909. [media] Cubierta — tejado del bloque cercano de la izquierda
   - Captura: Tejado de teja roja con alero visible en la esquina superior del bloque (x≈390–495, y≈0–105).
   - Juego: Remate plano y redondeado, blanco, sin teja visible a lo largo de todo el borde superior (x≈280–580, y≈0–210).
1910. [media] Cubierta — tejado y chimenea del segundo bloque de la izquierda
   - Captura: Tejado de teja con alero y una chimenea de obra sobre la cubierta (x≈500–520, y≈130–160).
   - Juego: Remate plano blanco sin chimenea (x≈510–690, y≈215–230); solo asoma un trocito rojo en x≈660–685, y≈250–265.
1911. [media] Calzada — firme de la calzada
   - Captura: Asfalto gris oscuro con grietas (x≈480–1300, y≈380–693).
   - Juego: Firme beige claro, casi color arena (x≈0–1340, y≈370–693).
1912. [media] Vegetación — seto recortado delante de los bloques
   - Captura: Seto verde largo y recortado, paralelo a la calle, de x≈420 a x≈710 (y≈375–455).
   - Juego: No hay seto; en esa franja solo hay baldosa de la explanada y coches.
1913. [baja] Detalles de fachada — aparato de aire acondicionado del bloque cercano
   - Captura: Aparato de aire acondicionado colgado en la fachada (x≈265–310, y≈255–290).
   - Juego: Fachada sin aparato.
1914. [baja] Zócalo — base de la tapia derecha
   - Captura: Sin zócalo definido: manchas irregulares de humedad verdosas y oscuras en la parte baja (x≈1180–1440, y≈470–650).
   - Juego: Zócalo gris verdoso uniforme en franja continua a lo largo de toda la tapia (x≈820–1440, hasta y≈670 en x=1440).
1915. [baja] Acera y bordillo — bordillo izquierdo
   - Captura: Bordillo de hormigón gris, sin pintura (x≈480–715, y≈385–693).
   - Juego: Bordillo blanco con un tramo pintado de amarillo (x≈430–475, y≈465–490).
1916. [baja] Vegetación — arbustos con flores rojas al pie del segundo bloque
   - Captura: Arbustos con flores rojas junto a los pilares del segundo bloque (x≈600–660, y≈355–390).
   - Juego: No hay arbustos ahí; en cambio hay macetas con flores rojas al pie del bloque cercano (x≈255–290 y x≈345–390, y≈400–430), que la captura no tiene.
1917. [baja] Vegetación — franja de césped en la esquina inferior izquierda
   - Captura: Césped verde en x≈0–220, y≈535–693 (en parte tapado por el minimapa).
   - Juego: En esa zona hay calzada y bordillo blanco; no hay césped.
1918. [baja] Mobiliario — farola de la explanada
   - Captura: Farola de báculo con globo blanco junto al seto (x≈595–610, y≈305–385).
   - Juego: No hay farola en la explanada.
1919. [baja] Vehículos — lado de aparcamiento
   - Captura: Coches aparcados en fila pegados a la tapia derecha (x≈780–1165, y≈360–580); ninguno junto a la acera izquierda.
   - Juego: Coches aparcados junto al bordillo izquierdo (x≈470–730, y≈355–470); ninguno junto a la tapia derecha.
1920. [baja] Otros — cables aéreos
   - Captura: Cables eléctricos cruzan la calle de x≈620 a x≈860 (y≈250–290), del segundo bloque a la nave.
   - Juego: No hay cables.
**Vista #193** — 03_Cruce_con_Arroyo.jpg (mayo de 2024) · hoja a_193.jpg

1921. [media] Geometría — altura de la casa de una planta de la derecha
   - Captura: Alero en y≈285–295 sobre la acera (y≈455) en x≈1100: fachada de unos 165 px de alto.
   - Juego: Alero en y≈320–330 sobre la acera (y≈455): fachada de unos 130 px, más baja.
1922. [media] Color de fachada — casa blanca, segunda por la izquierda (x≈125–280)
   - Captura: Fachada blanca con zócalo gris.
   - Juego: Fachada beige rosada, del mismo color que el bloque contiguo (x≈110–270).
1923. [media] Huecos — planta baja de la casa blanca, segunda por la izquierda
   - Captura: Puerta metálica gris a la izquierda (x≈145–180, y≈345–420), ventana con reja negra a la derecha (x≈205–245, y≈340–410) y un cuadro de azulejo religioso (x≈133–157, y≈283–318).
   - Juego: Orden invertido: ventanal con reja blanca a la izquierda (x≈115–180, y≈340–420) y puerta gris a la derecha (x≈215–250, y≈345–432); sin azulejo religioso.
1924. [media] Huecos — casa beige de la esquina izquierda (x≈280–500)
   - Captura: Planta baja: puerta con recercado de azulejos (x≈290–340, y≈350–420) y ventana con reja (x≈385–415, y≈350–400); planta alta: dos balcones de forja individuales (x≈300–335 y x≈385–420, y≈250–315).
   - Juego: Planta baja: cochera con persiana gris (x≈283–352, y≈342–437) y ventana con persiana blanca (x≈375–440, y≈343–420); planta alta: un balcón corrido con antepecho macizo gris y ropa tendida (x≈237–445, y≈275–320).
1925. [media] Huecos — pared que se aleja por la izquierda de la calle de enfrente (x≈470–690)
   - Captura: Medianera ciega color crema de dos plantas, con hastial inclinado que baja de y≈228 (x≈600) a y≈310 (x≈650) y luego un muro bajo (x≈650–690); sin ventanas ni puertas.
   - Juego: Fachada de dos plantas con huecos: ventanas (x≈485–540, y≈235–290), balcón (x≈500–560, y≈285–325), ventana con reja (x≈490–540, y≈340–415) y puertas (x≈560–610), con alero de teja continuo hasta x≈640.
1926. [media] Huecos — puertas de la casa de una planta de la derecha
   - Captura: Fachada ciega de x≈880 a x=1440, sin ninguna puerta (solo una ventanita verde).
   - Juego: Dos puertas dobles marrones (x≈885–940 y x≈1190–1245, y≈355–450).
1927. [media] Huecos — extremo derecho de la casa de la derecha (x≈1325–1440)
   - Captura: Sigue la misma fachada encalada sin huecos.
   - Juego: Puerta de cochera de madera clara (x≈1325–1440, y≈340–460).
1928. [media] Zócalo — zócalo de la casa de la derecha
   - Captura: Zócalo de cemento gris oscuro a lo largo de la base (x≈870–1440, y≈425–460).
   - Juego: Sin zócalo diferenciado: el revoco beige llega hasta la acera.
1929. [media] Cubierta — tejado de la casa de la derecha
   - Captura: Teja vieja pardo-rojiza oscura, en un solo faldón continuo de x≈835 a x=1440 (cumbrera y≈232–250, alero y≈280–295).
   - Juego: Teja naranja viva; a partir de x≈1210 aparece un segundo tejado más alto (y≈255–300).
1930. [media] Calzada — firme del cruce y de la calle de enfrente
   - Captura: Asfalto claro ocre-grisáceo homogéneo en el cruce (primer plano) y en la calle de enfrente, sin cambio de material.
   - Juego: El cruce en primer plano es gris neutro y la calle de enfrente beige, separados por un borde recto (x≈310–600, y≈480–565).
1931. [media] Acera y bordillo — acera izquierda en primer plano
   - Captura: Acera estrecha de hormigón gris delante de las casas (x≈150–600, y≈420–460); por debajo, asfalto.
   - Juego: Explanada empedrada gris claro mucho más ancha, que baja hasta y≈490–515 (x≈0–420), con bordillo pintado de amarillo en x≈0–90.
1932. [media] Mobiliario — farol de la esquina derecha
   - Captura: Farol de forja sobre brazo alto en la esquina, a la altura del tejado (x≈885–920, y≈180–320).
   - Juego: No hay farol en la esquina; solo un aplique pequeño en mitad de la fachada (x≈1130–1175, y≈338–370).
1933. [baja] Huecos — ventana verde de la casa de la derecha
   - Captura: Ventanita cuadrada con postigo verde en x≈980–1020, y≈328–370.
   - Juego: Ventana mayor con persiana verde, más a la derecha y más baja (x≈1035–1090, y≈350–415).
1934. [baja] Detalles de fachada — casa de la izquierda del todo (x≈0–125)
   - Captura: Fachada sin toldo: balcones de forja en la planta alta (x≈0–40 y x≈50–110, y≈280–320) y farol de pared alto (x≈70–125, y≈232–275).
   - Juego: Toldo amarillo y blanco sobre el balcón (x≈0–80, y≈238–256); el farol está más bajo, en x≈85–135, y≈330–355.
1935. [baja] Acera y bordillo — acera derecha de la calle de enfrente
   - Captura: Baldosa rojiza (x≈780–850, y≈390–460).
   - Juego: Empedrado beige-gris.
1936. [baja] Mobiliario — señal de tráfico en la medianera izquierda
   - Captura: Señal triangular de borde rojo en la pared (x≈505–525, y≈338–358).
   - Juego: No hay señal.
1937. [baja] Otros — tapa de registro en el cruce
   - Captura: Tapa redonda de alcantarilla en la calzada (x≈805–865, y≈510–540).
   - Juego: No hay tapa.
1938. [baja] Otros — cables aéreos
   - Captura: Cables que cruzan la calle de enfrente (x≈500–890, y≈235–275).
   - Juego: No hay cables.
**Vista #194** — 04_Tramo_sur.jpg (mayo de 2024) · hoja a_194.jpg

1939. [alta] Geometría — edificio del fondo por encima de la casa izquierda
   - Captura: Edificio de ladrillo visto rojo, de unas dos plantas, solo en x≈475–665 (y≈200–320); en x≈280–470 por encima de la tapia solo hay cielo.
   - Juego: Bloque blanco de tres plantas con filas de ventanas de x≈280 a x≈675 (y≈190–340).
1940. [alta] Color de fachada — casa del borde derecho (x≈1300–1440)
   - Captura: Fachada blanca.
   - Juego: Fachada pintada de rojo teja/terracota (x≈1285–1440, y≈160–445).
1941. [media] Geometría — altura de la casa del borde derecho
   - Captura: Una sola planta: remate en y≈265, con una ventana con reja (x≈1340–1375, y≈350–395) y puerta oscura al borde (x≈1420–1440).
   - Juego: Dos plantas, remate en y≈160, con balcón de forja (x≈1325–1440, y≈265–310), ventana con persiana arriba y puerta gris abajo (x≈1330–1380, y≈355–410).
1942. [media] Huecos — reja de rombos de la casa de la izquierda
   - Captura: Gran reja negra de rombos sobre un hueco (x≈0–225, y≈360–600).
   - Juego: Pared blanca lisa con una plaquita azul (x≈125–170, y≈400–425) y una caja blanca (x≈70–185, y≈535–640); no hay reja.
1943. [media] Huecos — portón de cochera de la izquierda
   - Captura: Portón metálico negro de barrotes verticales en x≈440–550, y≈310–535.
   - Juego: En esa posición hay una ventana con reja (x≈495–540, y≈350–440); la cochera del juego está más cerca (x≈210–360, y≈365–640) y es gris azulada de lamas.
1944. [media] Huecos — planta baja de la casa de enfrente a la derecha
   - Captura: Ventana con reja (x≈1015–1065, y≈340–400), puerta blanca central (x≈1105–1145, y≈340–435) y otra ventana con reja (x≈1210–1260, y≈340–400).
   - Juego: Gran cochera con persiana blanca (x≈995–1115, y≈338–450) y una sola ventana con reja (x≈1175–1245, y≈348–417).
1945. [media] Huecos — costado izquierdo de la casa de enfrente (x≈840–990)
   - Captura: Medianera blanca ciega con remate escalonado (x≈850–975, y≈225–410) y un anexo bajo en x≈805–850.
   - Juego: Fachada de dos plantas con huecos: puerta azul (x≈840–860), cochera de persiana blanca (x≈905–950, y≈340–440), ventanas arriba y balcón (x≈835–885, y≈295–330).
1946. [media] Detalles de fachada — casa de dos plantas de enfrente a la derecha (recercados)
   - Captura: Fachada blanca con recercados, pilastras de esquina y cornisa pintados de ocre amarillo (x≈975–1300, y≈218–440).
   - Juego: Fachada blanca lisa, sin recercados ni pilastras de color (x≈840–1285).
1947. [media] Zócalo — zócalo de la casa de la izquierda
   - Captura: Zócalo de piedra/canto rodado pardo-grisáceo (x≈240–440, y≈505–690 y x≈550–590, y≈420–465).
   - Juego: Zócalo gris liso continuo (x≈0–580, y≈410–693).
1948. [media] Cubierta — remate de la casa/tapia larga de la izquierda
   - Captura: Remate recto con albardilla oscura, sin tejado visible (línea de x≈0, y≈130 a x≈665, y≈330).
   - Juego: Tejado de teja naranja con alero de tejas redondeadas muy marcado (x≈0–650, y≈85–335) y un depósito o placa gris encima (x≈0–255, y≈95–175).
1949. [media] Acera y bordillo — acera izquierda
   - Captura: Acera ancha de baldosa gris con bordillo gris: a la altura y≈650 va de x≈260 a x≈510.
   - Juego: Acera estrecha de adoquín gris: a la altura y≈650 va de x≈230 a x≈300, con un escalón blanco junto a la casa (x≈180–410, y≈550–693) y el bordillo pintado de amarillo al fondo (x≈590–690, y≈375–455).
1950. [baja] Detalles de fachada — toldo de la casa de enfrente a la derecha
   - Captura: Sin toldo sobre los balcones.
   - Juego: Toldo de rayas rojas y blancas sobre el balcón izquierdo (x≈1025–1125, y≈212–235).
1951. [baja] Vegetación — árboles al fondo de la calle
   - Captura: Masa de árboles verdes al final de la calle (x≈690–770, y≈315–360).
   - Juego: Al fondo hay un edificio gris bajo y cielo (x≈700–760, y≈335–355); solo un arbolito diminuto en x≈688–697.
1952. [baja] Mobiliario — farol de la izquierda
   - Captura: Farol de forja con brazo, alto, en la esquina del edificio de ladrillo (x≈585–625, y≈200–320).
   - Juego: Aplique pequeño a baja altura (x≈600–625, y≈340–360).
**Vista #195** — 05_Vista_en_sentido_contrario.jpg (mayo de 2024) · hoja a_195.jpg

1953. [alta] Geometría — tapia de la derecha
   - Captura: Tapia blanca ciega, sin puertas ni ventanas, de x≈850 a x=1440 (y≈265–450).
   - Juego: Edificio de una planta con cinco ventanas de marco marrón, una puerta doble (x≈845–885) y una cochera marrón (x≈1235–1310), de x≈780 a x≈1430 (y≈295–430).
1954. [alta] Color de fachada — edificio alto de la derecha, detrás de la tapia
   - Captura: Edificio de ladrillo visto rojo de dos o tres plantas (x≈790–1120, y≈170–310).
   - Juego: Bloque blanco cúbico de azoteas planas (x≈755–1060, y≈190–295).
1955. [media] Color de fachada — casa ocre de dos plantas (x≈480–590)
   - Captura: Ocre amarillo intenso.
   - Juego: Beige pálido apagado.
1956. [media] Huecos — planta baja de la casa cercana de la izquierda (nº 15)
   - Captura: Ventana con reja a la izquierda (x≈0–70, y≈350–480), puerta blanca de madera en el centro (x≈255–320, y≈350–505) y ventanita con reja a la derecha (x≈410–455, y≈345–415).
   - Juego: Ventanal con reja (x≈100–275, y≈350–500) donde la captura tiene la puerta, y una puerta con cortina de tiras de colores (x≈400–445, y≈345–455) donde la captura tiene la ventanita.
1957. [media] Huecos — planta alta de la casa nº 15
   - Captura: Un único balcón corrido de forja con macetas (x≈155–385, y≈205–300); a su derecha (x≈390–480, y≈200–320) pared lisa.
   - Juego: Balcón corrido (x≈60–315, y≈175–300) y un segundo balcón en x≈390–475, y≈260–315.
1958. [media] Huecos — casa ocre de dos plantas (x≈480–590)
   - Captura: Planta alta con dos ventanas de arco de medio punto (x≈495–560, y≈220–275) sobre un balcón de forja (x≈500–570, y≈270–315).
   - Juego: Ventanas rectangulares con balconcillos (x≈500–550 y x≈560–590, y≈290–330); sin arcos.
1959. [media] Detalles de fachada — recercados de piedra de la casa nº 15
   - Captura: Recercados gruesos de piedra gris (granito) alrededor de la puerta (x≈220–345, y≈330–510) y de las ventanas (x≈0–100 y x≈405–460).
   - Juego: Sin recercados de piedra; solo un marco blanco fino en la puerta.
1960. [media] Zócalo — zócalo y pilastras de la tapia de la derecha
   - Captura: Zócalo de plaqueta de ladrillo rojiza (x≈845–1440, y≈405–450) y pilastras de ladrillo (x≈1205–1225, y≈310–445).
   - Juego: Zócalo beige liso (x≈790–1425, y≈400–430), sin pilastras.
1961. [media] Acera y bordillo — explanada de la derecha
   - Captura: Explanada de baldosa de hormigón beige (x≈780–1440, y≈400–693).
   - Juego: Explanada de losas grandes gris claro casi blancas (x≈820–1440, y≈430–693).
1962. [media] Vegetación — palmera detrás de la derecha
   - Captura: No hay palmera; por encima de la tapia se ven casas y un mástil de antena (x≈1110–1160, y≈150–270).
   - Juego: Palmera grande detrás del edificio de la derecha (x≈1050–1210, y≈205–295).
1963. [baja] Detalles de fachada — toldo de la casa cercana de la izquierda (nº 15)
   - Captura: Toldo de rayas azules y blancas sobre el balcón (x≈320–380, y≈130–210).
   - Juego: Sin toldo.
1964. [baja] Acera y bordillo — franja de baldosa roja en la explanada
   - Captura: Franja de baldosa roja en primer plano (x≈860–1180, y≈540–693).
   - Juego: No existe; todo el suelo es gris claro.
1965. [baja] Acera y bordillo — bordillo derecho
   - Captura: Bordillo de hormigón gris (x≈760–950, y≈380–693).
   - Juego: Bordillo blanco por piezas (x≈740–1000).
1966. [baja] Muros y vallas — remate de la tapia de la derecha
   - Captura: Remate a dos aguas con albardilla de ladrillo: sube de y≈300 (x≈850) a y≈265 (x≈1060) y baja a y≈310 (x≈1215); luego sigue recto.
   - Juego: Remate recto horizontal en y≈295.

### Calle José de Echagaray

**Vista #196** — 02_Desde_un_extremo_hacia_el_otro.jpg (mayo de 2024) · hoja a_196.jpg

1967. [alta] Geometría — lado izquierdo en primer plano (tapia larga)
   - Captura: Tapia de unos dos metros sin huecos: primero de bloques de hormigón color crema con las hiladas marcadas (x≈0–370, y≈300–500) y luego enfoscado blanco rugoso (x≈370–625, y≈305–470).
   - Juego: Casa de una planta de revoco beige con tejado de teja roja, cinco ventanas con persiana gris y una puerta (x≈0–525, y≈315–410).
1968. [alta] Color de fachada — casa más cercana de la derecha (x≈1120–1440)
   - Captura: Fachada blanca/gris muy clara con un pilar chapado de piedra beige (x≈1095–1125, y≈340–500).
   - Juego: Fachada azul intenso de arriba abajo (x≈1255–1440, y≈90–470).
1969. [media] Color de fachada — chalé de dos plantas detrás de la tapia izquierda
   - Captura: Chalé de color salmón/rosado con balaustradas blancas en los balcones (x≈430–490 y x≈560–630, y≈295–320), chimenea (x≈515–527, y≈205–222) y buganvilla roja (x≈510–570, y≈295–325); ocupa x≈330–640, y≈205–330.
   - Juego: Casa de dos plantas beige grisácea con ventanas de persiana gris, sin balaustradas blancas, chimenea ni buganvilla (x≈280–560, y≈245–380).
1970. [media] Color de fachada — planta baja de la casa azul de la derecha
   - Captura: Planta baja chapada de piedra beige con pilares de piedra (x≈920–985) y cancelas correderas metálicas grises de lamas (x≈985–1100, y≈360–470).
   - Juego: Planta baja azul como el resto, con una puerta doble blanca (x≈1040–1115, y≈355–455).
1971. [media] Huecos — balcón de la planta alta de la casa azul
   - Captura: Balcón con barandilla de vidrio y acero (x≈1045–1135, y≈230–290) bajo una ventana con contraventana gris de lamas (x≈1075–1130, y≈175–235).
   - Juego: En esa posición, pared azul con una moldura horizontal; el único balcón está más a la izquierda (x≈910–945, y≈285–320).
1972. [media] Detalles de fachada — cuerpo volado de la casa azul
   - Captura: Cuerpo de la planta alta chapado en beige/arena con ventana de lamas grises (x≈930–1020, y≈195–315).
   - Juego: Esa zona es azul, con toldos de rayas rojas y blancas (x≈905–945 y x≈990–1055, y≈215–270) que la captura no tiene.
1973. [media] Cubierta — cubiertas de las casas de la derecha
   - Captura: Cubiertas planas, sin teja visible.
   - Juego: Alero de teja roja en la esquina superior derecha (x≈1230–1440, y≈85–180).
1974. [media] Vegetación — arbolado detrás de la tapia izquierda
   - Captura: Línea de árboles y arbustos de copa redondeada y densa (x≈0–300, y≈260–300).
   - Juego: Pinos piñoneros de copa plana en capas (x≈0–300, y≈260–320).
1975. [media] Mobiliario — farola alta de la acera izquierda en primer plano
   - Captura: Báculo alto gris de farola que cruza toda la imagen (x≈465–475, y≈0–440).
   - Juego: No hay farola en esa posición.
1976. [baja] Acera y bordillo — borde izquierdo en primer plano
   - Captura: Franja de hierba y tierra al pie de la tapia, sin pavimentar (x≈0–360, y≈500–580).
   - Juego: Acera empedrada gris (x≈165–340, y≈410–530).
**Vista #197** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_197.jpg

1977. [alta] Muros y vallas — cerramiento delantero de la casa nº 11 (izquierda)
   - Captura: Murete con zócalo color albero rematado por verja negra de forja con puntas de lanza (x≈100–440, y≈355–530) y pilar con el número 11 (x≈0–105, y≈360–560); la casa queda retranqueada detrás.
   - Juego: No hay verja ni murete: la fachada de la casa está en la línea de la acera.
1978. [media] Color de fachada — casa de dos plantas de la esquina izquierda (x≈340–600)
   - Captura: Toda la casa es gris azulada claro con recercados blancos (x≈340–600, y≈190–400).
   - Juego: En x≈375–520 la fachada es blanca; solo el tramo x≈520–590 es gris azulado.
1979. [media] Huecos — huecos de la casa nº 11
   - Captura: Planta alta con balcón corrido de forja (x≈0–300, y≈170–255); planta baja con ventana ancha de persiana gris y recercado blanco (x≈30–250, y≈280–430).
   - Juego: Planta alta con una ventana grande sin balcón (x≈165–310, y≈110–255); planta baja con una cochera gris de barrotes (x≈160–315, y≈350–460).
1980. [media] Huecos — huecos del edificio de ladrillo de la derecha
   - Captura: Edificio de ladrillo visto sin terminar: huecos oscuros vacíos, sin carpinterías ni persianas (x≈910–1380, y≈190–420), y una gran puerta de cochera blanca a la derecha (x≈1260–1440, y≈290–440).
   - Juego: Ventanas con marco blanco y persianas blancas enrollables (x≈1060–1115, y≈195–275; x≈1270–1425, y≈75–230 y 360–490), una puerta blanca (x≈970–995, y≈350–430); no hay puerta de cochera.
1981. [media] Vegetación — arbusto grande de la esquina izquierda
   - Captura: Arbusto verde grande y redondeado en la esquina (x≈500–615, y≈335–395).
   - Juego: No hay arbusto.
1982. [media] Mobiliario — farola alta de la acera derecha
   - Captura: Báculo alto de farola en la acera derecha (x≈1015–1030, y≈0–450).
   - Juego: No hay farola.
1983. [baja] Detalles de fachada — cornisa entre plantas de la casa nº 11
   - Captura: Cornisa blanca gruesa y moldurada entre plantas (x≈0–360, y≈215–295).
   - Juego: Fachada lisa sin cornisa.
1984. [baja] Detalles de fachada — bandas de forjado del edificio de ladrillo
   - Captura: Bandas horizontales grises de hormigón/enfoscado a la altura de los forjados (x≈900–1440, y≈240–330).
   - Juego: Ladrillo continuo sin bandas; solo una cornisa blanca bajo el alero.
1985. [baja] Muros y vallas — murete blanco de la casa gris azulada
   - Captura: Murete blanco con verja delante de la casa gris azulada (x≈455–615, y≈385–415).
   - Juego: Sin murete: fachada directamente sobre la acera.
**Vista #198** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_198.jpg

1986. [alta] Geometría — medianera vista del edificio contiguo a la derecha
   - Captura: Muro medianero desnudo, beige con un gran parche gris de enfoscado, más bajo que la casa blanca (x≈1135–1315, y≈240–415).
   - Juego: No existe: en su lugar se ve espacio abierto y, al fondo, una hilera baja de ladrillo con tejado (x≈1155–1420, y≈320–375).
1987. [alta] Color de fachada — edificio contiguo a la casa granate (x≈405–550)
   - Captura: Edificio de dos plantas de ladrillo visto rojo sin terminar, con huecos oscuros (x≈405–620, y≈230–410).
   - Juego: Casa de dos plantas de revoco beige crema (x≈415–550, y≈170–440); el ladrillo empieza más lejos (x≈550–635).
1988. [alta] Muros y vallas — cerramiento delantero de la casa granate (izquierda)
   - Captura: Muro blanco con pilares y verja negra de forja, con una cancela grande de hierro (x≈0–490, y≈340–580); la casa queda retranqueada detrás.
   - Juego: No hay cerramiento: la fachada granate está en la línea de la acera (x≈0–420).
1989. [alta] Otros — solar de la derecha
   - Captura: Solar de tierra rojiza con hierbas secas (x≈850–1440, y≈410–693).
   - Juego: Explanada pavimentada gris clara casi blanca (x≈1000–1440, y≈370–620).
1990. [media] Huecos — planta baja de la casa granate
   - Captura: Ventana con reja de forja en x≈255–345, y≈265–345 (sobre la verja).
   - Juego: Puerta con panel gris azulado en x≈295–380, y≈350–475 y una ventana con reja en x≈0–85.
1991. [media] Huecos — pared de la casa blanca de la derecha que mira a la cámara
   - Captura: Medianera blanca ciega, sin ningún hueco (x≈905–1140, y≈190–420).
   - Juego: Seis ventanas con macetas en dos filas (x≈950–1130, y≈290–390).
1992. [media] Cubierta — remate de la casa blanca de la derecha
   - Captura: Hastial blanco sin teja a la vista, con chimenea blanca (x≈1095–1115, y≈170–200) y antena.
   - Juego: Tejado de teja naranja con alero volado (x≈840–1200, y≈225–255), sin chimenea.
1993. [media] Vegetación — árboles del borde derecho
   - Captura: Árboles de hoja ancha, uno con flores moradas (x≈1315–1440, y≈260–380).
   - Juego: Pinos piñoneros de copa plana y un arbusto redondo (x≈1155–1440, y≈255–345).
1994. [media] Mobiliario — farola alta de la acera izquierda
   - Captura: Báculo alto de farola en primer plano (x≈395–430, y≈0–490).
   - Juego: No hay farola ahí; solo una farola negra más baja y lejana (x≈525–575, y≈255–420).
1995. [baja] Acera y bordillo — acera izquierda
   - Captura: Baldosa de hormigón gris con bordillo gris (x≈0–650, y≈400–600).
   - Juego: Adoquín blanquecino con bordillo blanco (x≈0–575, y≈400–640).
1996. [baja] Acera y bordillo — acera derecha en primer plano
   - Captura: Baldosa gris con una franja de baldosa roja al final (x≈1090–1250, y≈630–693).
   - Juego: Adoquín blanquecino sin franja roja.
1997. [baja] Mobiliario — farola de la acera derecha
   - Captura: Báculo alto de farola junto a la casa blanca (x≈810–825, y≈175–410).
   - Juego: No hay farola en la acera derecha.
1998. [baja] Muros y vallas — cerca de ladrillo del edificio sin terminar
   - Captura: Murete de ladrillo con cancela de hierro delante del edificio (x≈470–545, y≈345–420).
   - Juego: No hay cerca.

### Calle Juan Ramón Jiménez

**Vista #199** — 02_Desde_un_extremo_hacia_el_otro.jpg (mayo de 2024) · hoja a_199.jpg

1999. [alta] Geometría — anchura de la calzada / bordillo izquierdo
   - Captura: El bordillo izquierdo llega al borde inferior en x≈480 (sube hasta x≈690, y≈360); en el borde inferior la calzada va de x≈480 a x≈1190.
   - Juego: El bordillo izquierdo llega al borde inferior en x≈220: la calzada va de x≈220 a x≈1210, alrededor de un 40 % más ancha.
2000. [alta] Color de fachada — edificación detrás de los jardines de la izquierda
   - Captura: Casa blanca de dos plantas con tejado de teja, medio tapada por los árboles (x≈140–370, y≈220–300).
   - Juego: Edificios de ladrillo rojo de una planta con tejado de teja (x≈0–430, y≈255–420), más una casa blanca (x≈400–530) y otra rosada (x≈520–700) junto a la explanada.
2001. [alta] Vegetación — jardines arbolados del lado izquierdo
   - Captura: Vegetación densa en toda la mitad izquierda: seto alto y continuo (x≈0–580, y≈340–500), árbol de hoja ancha (x≈0–230, y≈90–400), conífera (x≈360–470, y≈170–330), árbol de hoja morada (x≈480–680, y≈195–345), adelfas en flor rosa (x≈380–560, y≈260–340) y buganvilla (x≈130–260, y≈290–350).
   - Juego: Un único árbol redondeado (x≈0–225, y≈185–365); el resto de la mitad izquierda es una explanada abierta sin seto ni árboles.
2002. [alta] Otros — suelo del primer plano izquierdo
   - Captura: Franja de tierra con hierbas, sin pavimentar, al pie del seto (x≈0–560, y≈470–693), separada de la calzada por la acera.
   - Juego: Gran explanada de losas gris claro casi blancas que llega hasta la calzada (x≈0–700, y≈380–693).
2003. [media] Geometría — altura de la casa cercana de la derecha
   - Captura: En x≈900 la fachada va de y≈140 (remate) a y≈410 (acera): unos 270 px.
   - Juego: En x≈900 la fachada va de y≈220 a y≈420: unos 200 px, más baja.
2004. [media] Huecos — casa adosada más cercana de la derecha (x≈1030–1440)
   - Captura: Paño beige casi ciego: solo una ventana pequeña arriba (x≈1055–1100, y≈45–125) y un aparato de aire acondicionado (x≈1050–1145, y≈262–315); planta baja sin puertas ni ventanas.
   - Juego: Ventanas con marco blanco en las dos plantas (x≈1005–1055, y≈180–270 y 350–430) y una gran puerta de cochera con marco blanco (x≈1200–1440, y≈350–590); sin aparato de aire.
2005. [media] Detalles de fachada — tejadillo sobre la planta baja de la casa cercana de la derecha
   - Captura: No hay tejadillo.
   - Juego: Tejadillo de teja naranja corrido sobre la planta baja (x≈1060–1440, y≈215–320).
2006. [media] Mobiliario — farola alta de la acera izquierda
   - Captura: Báculo alto de farola en la acera izquierda (x≈620–640, y≈105–440).
   - Juego: No hay farola en la acera izquierda.
2007. [media] Muros y vallas — muro de mampostería con verja de la izquierda
   - Captura: Murete de piedra con pilares y verja a lo largo de la acera (x≈530–670, y≈340–470).
   - Juego: No hay muro ni verja.
2008. [baja] Color de fachada — banda vertical de la casa cercana de la derecha
   - Captura: Banda vertical rehundida de color beige más oscuro/asalmonado (x≈915–1025, y≈45–410).
   - Juego: Fachada de un beige uniforme, sin banda.
**Vista #200** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_200.jpg

2009. [alta] Geometría — casa cercana de la izquierda
   - Captura: Casa de dos plantas (la planta alta ocupa x≈0–480, y≈0–330), retranqueada detrás de una verja.
   - Juego: Casa de una sola planta con tejado de teja de alero redondeado (x≈0–530, y≈205–630), en la línea de la acera.
2010. [alta] Color de fachada — casa cercana de la izquierda
   - Captura: Fachada blanca con la planta alta gris claro (x≈0–480).
   - Juego: Fachada color salmón anaranjado (x≈0–530).
2011. [alta] Muros y vallas — verja de la casa cercana de la izquierda
   - Captura: Verja larga de barrotes verticales metálicos grises sobre un murete blanco (x≈0–545, y≈330–693), en primer plano.
   - Juego: No hay verja: en su lugar la pared de la casa con una ventana enrejada (x≈125–315, y≈355–545).
2012. [alta] Muros y vallas — cerramientos de las casas adosadas de la derecha
   - Captura: Muretes beige con pilares de remate blanco (x≈840–1240, y≈335–470), cancelas negras de hierro (x≈1015–1235, y≈370–560) y un pilar beige grande en primer plano (x≈1235–1400, y≈360–640); las casas quedan retranqueadas tras pequeños patios.
   - Juego: No hay cerramientos: las puertas de las casas dan directamente a la acera.
2013. [media] Geometría — altura del edificio salmón de la izquierda (x≈550–680)
   - Captura: Edificio alto de cubierta plana: su remate baja de y≈170 (x≈550) a y≈300 (x≈680).
   - Juego: Casas de una planta con tejado de teja: el alero queda en y≈265–330 y por encima de y≈300 en x≈550–600 solo hay cielo.
2014. [media] Color de fachada — edificio de la izquierda en plano medio (x≈430–680)
   - Captura: Volumen blanco (x≈430–550) seguido de un edificio pintado de salmón/teja (x≈550–680) con ventanas enrejadas (x≈570–585 y x≈600–620, y≈335–395).
   - Juego: Colores invertidos: casa salmón en x≈380–530 y casa blanca grisácea en x≈530–670.
2015. [media] Huecos — huecos de las casas adosadas de la derecha
   - Captura: Planta alta con balcones de forja negra en cada casa (x≈930–970, y≈245–285; x≈990–1055, y≈215–270; x≈1160–1320, y≈110–215) y aparato de aire (x≈1105–1170, y≈130–180); planta baja con ventanas enrejadas (x≈1005–1050, y≈290–350; x≈1350–1440, y≈265–355).
   - Juego: Un solo balcón (x≈890–1010, y≈280–330); planta baja con puertas dobles grises (x≈965–1005, x≈1085–1145 y x≈1320–1440, y≈350–550) y sin rejas.
2016. [media] Detalles de fachada — tejadillos de las casas adosadas de la derecha
   - Captura: Sin tejadillos sobre la planta baja.
   - Juego: Tejadillos de teja naranja sobre las puertas de la planta baja (x≈1025–1440, y≈240–330; x≈835–885, y≈320–340).
2017. [media] Cubierta — tejados de las casas adosadas de la derecha
   - Captura: Cada casa remata en un hastial triangular de teja hacia la calle (x≈925–1100, y≈60–170).
   - Juego: Aleros de teja horizontales y continuos, sin hastiales (x≈880–1440, y≈95–270).
2018. [media] Mobiliario — farola alta de la acera derecha
   - Captura: Báculo alto de farola en la acera derecha (x≈895–925, y≈40–465).
   - Juego: No hay farola.
**Vista #201** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_201.jpg

2019. [alta] Acera y bordillo — isleta entre las dos ramas de la calle
   - Captura: Entre la calle de la izquierda y la de la derecha solo hay asfalto continuo, sin isleta (x≈700–1000, y≈420–600).
   - Juego: Mediana/isleta alargada con bordillos blancos que separa las dos calzadas (x≈760–1000, y≈350–580).
2020. [alta] Muros y vallas — cerramientos de las casas adosadas de la izquierda
   - Captura: Pilares beige con remate piramidal blanco (x≈85–175 y x≈355–435, y≈345–600) y cancelas metálicas oscuras (x≈175–355, y≈410–620; x≈460–545, y≈375–510) a lo largo de la acera; las casas quedan retranqueadas.
   - Juego: No hay cerramientos: las puertas de las casas dan a la acera.
2021. [alta] Muros y vallas — talud de mampostería junto a la calle de la derecha
   - Captura: Talud/muro de piedra en hiladas irregulares a lo largo de la calle de la derecha (x≈1030–1440, y≈350–530), con un seto encima (x≈1200–1440, y≈340–390).
   - Juego: No hay muro ni seto: un arcén plano blanco con palmeras (x≈1050–1440, y≈360–560).
2022. [media] Color de fachada — edificio de la esquina del fondo
   - Captura: Pintado de rojo almagre/teja oscuro.
   - Juego: Salmón claro.
2023. [media] Huecos — planta baja de las casas adosadas de la izquierda
   - Captura: Ventanas con reja de forja (x≈85–145 y x≈175–265, y≈260–350) detrás de los cerramientos.
   - Juego: Puertas con cortina de tiras de colores (x≈285–360, y≈355–500; x≈440–475, y≈350–445) y ventanas sin rejas.
2024. [media] Huecos — edificio de la esquina del fondo (x≈765–940)
   - Captura: Local comercial con escaparates acristalados (x≈820–930, y≈320–410).
   - Juego: Casa con ventanas pequeñas (x≈760–925, y≈305–405), sin escaparates.
2025. [media] Detalles de fachada — tejadillos de las casas adosadas de la izquierda
   - Captura: Sin tejadillos; en la planta alta hay balcones con barandilla de forja (x≈270–385, y≈120–225; x≈480–520, y≈230–275; x≈545–570, y≈260–290).
   - Juego: Tejadillos de teja naranja sobre las puertas (x≈165–515, y≈255–330) y un toldo rosa (x≈0–95, y≈135–235).
2026. [media] Cubierta — edificio de la esquina del fondo
   - Captura: Cubierta plana, remate recto (x≈765–940, y≈280–300).
   - Juego: Tejado de teja naranja a varias aguas (x≈760–925, y≈305–340).
2027. [media] Mobiliario — farola alta de la acera izquierda
   - Captura: Báculo alto de farola en primer plano (x≈500–520, y≈0–590).
   - Juego: No hay farola.
2028. [baja] Mobiliario — placa de la calle
   - Captura: Placa «Calle Juan Ramón Jiménez» en un pilar (x≈415–460, y≈380–410) y número 16 (x≈365–390, y≈415–430).
   - Juego: Sin placa ni número.
2029. [baja] Otros — tapa de registro en primer plano
   - Captura: Tapa redonda de alcantarilla (x≈750–830, y≈600–655).
   - Juego: No hay tapa.
**Vista #202** — 05_Rotulo_fisico_de_la_calle.jpg (mayo de 2024) · hoja a_202.jpg

2030. [alta] Muros y vallas — cerramientos de las casas adosadas
   - Captura: Toda la hilera tiene cerramiento a la acera: pilares beige con remate piramidal blanco (x≈95–180, x≈400–575, x≈740–800, x≈865–900…, y≈340–690) y cancelas metálicas oscuras con barrotes decorativos (x≈180–400, x≈575–740, x≈800–870); las casas quedan retranqueadas.
   - Juego: No hay cerramientos: las puertas dan a la acera.
2031. [media] Color de fachada — edificio del borde derecho, al otro lado de la calle
   - Captura: Edificio alto de ladrillo/tono rojizo con valla metálica delante (x≈1385–1440, y≈235–480).
   - Juego: Casas blancas con tejado de teja (x≈1365–1440, y≈280–450).
2032. [media] Huecos — planta alta de las casas adosadas
   - Captura: Cada casa tiene balcón con barandilla de forja negra sobre repisa (x≈300–445, y≈0–95; x≈610–695, y≈75–180; x≈740–800, y≈135–210; x≈805–855, y≈165–230; x≈870–905, y≈195–245; x≈930–955, y≈240–285…).
   - Juego: Ventanas lisas con marco blanco (x≈330–410, y≈95–230; x≈685–730, y≈130–245; x≈790–820, y≈170–260), sin balcones salvo en x≈0–105 y x≈930–990.
2033. [media] Huecos — planta baja de las casas adosadas
   - Captura: Ventanas con reja de forja (x≈95–150, y≈210–350; x≈180–285, y≈220–355; x≈745–780, y≈255–350; x≈810–835, y≈270–350).
   - Juego: Puertas con cortina de tiras de colores (x≈310–410, y≈370–635; x≈540–595, y≈365–560) y puertas grises (x≈685–725, y≈360–515), sin rejas.
2034. [media] Detalles de fachada — tejadillos sobre las puertas
   - Captura: Sin tejadillos.
   - Juego: Tejadillos de teja naranja sobre las puertas (x≈170–670, y≈185–310; x≈840–930, y≈285–325; x≈990–1140, y≈320–335).
2035. [media] Cubierta — tejados de las casas adosadas
   - Captura: Cada casa remata en un hastial triangular con borde de teja hacia la calle (x≈830–940, y≈0–75; x≈910–1090, y≈80–240).
   - Juego: Aleros de teja horizontales y continuos, sin hastiales (x≈210–1140, y≈0–330).
2036. [media] Mobiliario — farola en primer plano
   - Captura: Báculo gris de farola que cruza toda la imagen (x≈648–680, y≈0–693).
   - Juego: No hay farola ahí.
2037. [baja] Detalles de fachada — aparato de aire acondicionado
   - Captura: Aparato de aire en la fachada (x≈895–920, y≈140–165).
   - Juego: Sin aparato.
2038. [baja] Mobiliario — señal de STOP
   - Captura: Señal octogonal de STOP vista por detrás, colgada del báculo (x≈585–655, y≈265–400).
   - Juego: No está; solo hay un poste con señal redonda más lejos (x≈855–895, y≈285–510).
2039. [baja] Mobiliario — placa de la calle y número
   - Captura: Placa «Calle Juan Ramón Jiménez» (x≈498–555, y≈430–480) y número 16 (x≈412–455, y≈485–515) en el pilar del nº 16.
   - Juego: Sin placa ni número (no hay pilar).

### Calle Miguel Hernández

**Vista #203** — 02_Desde_un_extremo_hacia_el_otro.jpg (mayo de 2024) · hoja a_203.jpg

2040. [alta] Geometría — cuerpo bajo en primer plano a la izquierda
   - Captura: La fachada salmón de la izquierda es un paño continuo desde el alero (y≈145 en x≈320) hasta el zócalo, sin ningún cuerpo más bajo delante (x≈0–300, y≈200–590).
   - Juego: Delante de la casa aparece un cuerpo de una planta con su propio tejado de teja naranja (x≈0–260, y≈240–560).
2041. [alta] Geometría — edificio beige de cubierta plana a la derecha (plano medio)
   - Captura: Edificio beige de dos alturas con cubierta plana, ventanas pequeñas (x≈820–860, y≈340–365) y cancela oscura (x≈905–945, y≈345–395), en x≈800–950, y≈250–400.
   - Juego: No existe: en x≈800–900 se ve cielo, una farola, árboles y suelo blanco; el edificio de la derecha empieza en x≈895.
2042. [media] Geometría — altura del edificio cercano de la derecha
   - Captura: Fachada alta con ático: la cornisa superior sube de y≈245 (x≈940) a y≈40 (x=1440).
   - Juego: Más bajo: el remate sube solo de y≈310 (x≈895) a y≈195 (x=1440).
2043. [media] Color de fachada — casa de la izquierda
   - Captura: Salmón anaranjado vivo (con desconchones).
   - Juego: Beige apagado con tono rosado.
2044. [media] Color de fachada — edificio cercano de la derecha (color)
   - Captura: Paños blancos con ocre; zócalo ocre (x≈940–1440, y≈400–480).
   - Juego: Mitad izquierda blanca (x≈895–1100) y mitad derecha color melocotón/salmón claro (x≈1100–1440, y≈310–600).
2045. [media] Huecos — huecos de la casa salmón de la izquierda
   - Captura: Casi ciega: una sola ventana con toldo y persiana blanca arriba a la izquierda (x≈20–300, y≈200–300); el resto (x≈300–500) sin huecos, solo rejillas pequeñas.
   - Juego: Ventanas con macetas en la planta alta (x≈50–120 y x≈245–305, y≈205–280), balcones con barandilla (x≈415–510, y≈285–330), ventana con reja (x≈245–305, y≈350–395) y otra ventana (x≈420–450, y≈345–370).
2046. [media] Detalles de fachada — edificio cercano de la derecha (molduras ocres)
   - Captura: Paños blancos enmarcados por bandas, pilastras y cornisas ocres (x≈940–1440, y≈40–480) y recercados ocres con frontón alrededor de las ventanas (x≈990–1035 y x≈1200–1370, y≈290–440).
   - Juego: Fachada lisa sin bandas, pilastras ni recercados ocres; solo marcos blancos.
2047. [media] Zócalo — zócalo de la casa salmón de la izquierda
   - Captura: Zócalo alto de azulejo blanco con dibujo de sillares (x≈0–500, y≈380–590).
   - Juego: Sin zócalo blanco: la casa principal no tiene zócalo visible y el cuerpo bajo tiene una franja gris (x≈0–210, y≈455–555).
2048. [media] Calzada — firme de la calzada
   - Captura: Asfalto pardo-grisáceo de tono medio (x≈300–1000, y≈360–693).
   - Juego: Firme gris muy claro.
2049. [baja] Color de fachada — casa de dos plantas del fondo izquierdo (x≈500–620)
   - Captura: Beige.
   - Juego: Blanca grisácea (x≈510–640).
2050. [baja] Huecos — rejas de las ventanas del edificio de la derecha
   - Captura: Rejas negras de forja (x≈990–1035 y x≈1220–1340, y≈320–425).
   - Juego: Rejas blancas (x≈990–1050, y≈348–425; x≈1165–1340, y≈348–490).
2051. [baja] Detalles de fachada — toldo de la casa salmón de la izquierda
   - Captura: Toldo extendido sobre la ventana de arriba (x≈20–300, y≈200–300).
   - Juego: Sin toldo.
2052. [baja] Vegetación — árboles a la derecha en plano medio
   - Captura: No hay árboles en x≈840–900.
   - Juego: Árboles redondos verdes (x≈840–900, y≈320–375).
**Vista #204** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_204.jpg

2053. [alta] Geometría — longitud del bloque de pisos de la derecha
   - Captura: El bloque blanco de cuatro plantas sigue sin interrupción desde x≈815 hasta el borde derecho, con su cornisa en y≈20–40 en x≈1100–1400.
   - Juego: El bloque termina en x≈1270 (remate en y≈85); a la derecha se ven árboles redondos (x≈1265–1440, y≈300–400) y otro bloque blanco más bajo y lejano (y≈230–330).
2054. [alta] Geometría — planta baja del bloque de la derecha
   - Captura: Soportal abierto con pilares ocres y muros blancos rehundidos (x≈820–1400, y≈320–415).
   - Juego: Planta baja cerrada, un zócalo-muro ocre macizo con ventanas y rejillas (x≈930–1265, y≈330–410).
   - Después: cambiado: el fondo del soportal (2,4 m) queda en sombra y sin cocheras.
2055. [media] Color de fachada — casa adosada más cercana de la izquierda (x≈0–340)
   - Captura: Crema claro con la parte baja blanca.
   - Juego: Tostado/salmón oscuro uniforme con zócalo gris.
2056. [media] Color de fachada — segunda casa de la izquierda (x≈340–450)
   - Captura: Fachada blanca con puerta blanca bajo arco (x≈400–425, y≈350–440).
   - Juego: Tostado/salmón como el resto de la hilera.
2057. [media] Huecos — planta baja de la casa más cercana de la izquierda
   - Captura: Dos ventanas con reja blanca y recercado de arco rebajado (x≈105–240, y≈340–440; x≈265–345, y≈340–420).
   - Juego: Una sola ventana con reja de marco recto (x≈205–320, y≈345–455).
2058. [media] Detalles de fachada — tercera casa de la izquierda (x≈450–555)
   - Captura: Planta baja chapada de piedra gris oscura (x≈450–555, y≈300–430), planta alta blanca con balcón de vidrio y aparato de aire.
   - Juego: Tostado/salmón liso con balcón de barandilla blanca y toldo (x≈435–475, y≈240–260); sin chapado de piedra.
2059. [media] Calzada — firme de la calzada
   - Captura: Asfalto pardo oscuro (x≈350–1150, y≈360–693).
   - Juego: Firme gris muy claro.
2060. [media] Acera y bordillo — suelo delante del bloque de la derecha
   - Captura: Acera de hormigón gris y, tras el seto, una zona de tierra (x≈1220–1440, y≈450–530).
   - Juego: Explanada de losas blancas que llega hasta el bloque (x≈900–1440, y≈380–600).
2061. [media] Vegetación — seto y rosales delante del bloque de la derecha
   - Captura: Seto recortado continuo a lo largo de la acera (x≈930–1420, y≈390–460), rosales (x≈985–1030 y x≈1065–1100, y≈365–410) y un arbusto morado (x≈1360–1440, y≈360–440).
   - Juego: Sin seto ni arbustos: explanada blanca.
2062. [media] Mobiliario — farola delante del bloque de la derecha
   - Captura: Farola baja de globo blanco (x≈965–985, y≈300–395).
   - Juego: Farola negra de brazo en otra posición (x≈820–850, y≈285–390).
**Vista #205** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_205.jpg

2063. [alta] Geometría — bloques de pisos de la izquierda (nº de plantas)
   - Captura: Cuatro plantas: planta baja porticada y tres filas de ventanas encima (en x≈355–385: y≈145–180, 205–235 y 265–295), tejado de teja a varias aguas.
   - Juego: Tres plantas: planta baja y dos filas de ventanas (y≈200–255 y 275–310 en x≈300–330; y≈50–145 y 205–280 en x≈0–95).
   - Después: corregido: cuatro plantas.
2064. [alta] Geometría — planta baja de los bloques de la izquierda
   - Captura: Soportal abierto con pilares ocres/pardos (x≈0–600, y≈310–420).
   - Juego: Planta baja cerrada, muro ocre macizo con ventanas y rejillas (x≈0–610, y≈325–445).
   - Después: cambiado: el fondo del soportal queda en sombra y sin cocheras.
2065. [media] Huecos — casa adosada más cercana de la derecha (x≈1100–1440)
   - Captura: Planta alta con balcón corrido de forja negra (x≈1170–1440, y≈100–270); planta baja con dos ventanas de reja oscura y persianas verdes (x≈1110–1180, y≈340–430; x≈1240–1430, y≈335–465).
   - Juego: Planta alta lisa sin balcón (x≈1100–1440, y≈0–320); planta baja con un solo ventanal de reja blanca (x≈1120–1275, y≈348–490).
2066. [media] Huecos — casa nº 2 de la derecha (x≈985–1060)
   - Captura: Puerta gris con el número 2 bajo un recercado de arco (x≈1010–1045, y≈340–445).
   - Juego: Ventana con reja blanca (x≈965–1020, y≈345–425); sin puerta.
2067. [media] Calzada — firme de la calzada
   - Captura: Asfalto pardo oscuro (x≈380–1100, y≈350–693).
   - Juego: Firme gris muy claro.
2068. [media] Vegetación — seto delante de los bloques de la izquierda
   - Captura: Seto recortado continuo (x≈0–580, y≈375–450) con rosales (x≈285–330, y≈395–415).
   - Juego: Sin seto: explanada blanca (x≈0–660, y≈370–560).
2069. [media] Mobiliario — farola de la acera derecha en primer plano
   - Captura: Farola alta de cabeza en disco en primer plano (x≈1065–1160, y≈160–585).
   - Juego: No está; la farola de la derecha es negra, de brazo, y queda más lejos (x≈845–905, y≈230–440).
2070. [baja] Detalles de fachada — arcos sobre puertas y ventanas de las casas de la derecha
   - Captura: Recercados blancos de medio punto sobre puertas y ventanas (x≈940–975, x≈1000–1050 y x≈1180–1220, y≈325–345).
   - Juego: Huecos de dintel recto, sin arcos.
2071. [baja] Cubierta — cubierta del segundo bloque de la izquierda
   - Captura: Tejado de teja con chimenea (x≈345–370, y≈95–125); antenas parabólicas en la fachada (x≈300–330, y≈285–320).
   - Juego: Placa solar sobre el tejado (x≈330–405, y≈130–160), sin chimenea ni parabólicas.
2072. [baja] Mobiliario — farola de globo de la izquierda
   - Captura: Farola de globo blanco delante del bloque (x≈405–430, y≈290–390).
   - Juego: No está; solo hay una farola negra lejana (x≈620–630, y≈315–370).

### Calle Palacios

**Vista #206** — 02_Desde_un_extremo_hacia_el_otro.jpg (mayo de 2024) · hoja a_206.jpg

2073. [alta] Geometría — edificio de la esquina derecha
   - Captura: Edificio blanco de una planta con tejado de teja roja, alero en y≈260–300, una ventanita enrejada (x≈1050–1110, y≈320–345); ocupa x≈755–1180, y≈260–525.
   - Juego: Nave industrial alta gris-blanca sin teja, de remate recto mucho más alto (y≈110–245), con puertas azules (x≈850–930, y≈340–500; x≈1145–1225, y≈345–435) y bandas de ventanas (x≈970–1125, y≈330–360); ocupa x≈745–1240.
2074. [alta] Geometría — silos metálicos del fondo derecho
   - Captura: Grandes depósitos cilíndricos de acero inoxidable con pasarelas, por encima de los tejados (x≈995–1440, y≈90–290).
   - Juego: No hay silos: cielo.
2075. [media] Geometría — esquina de la acera en primer plano
   - Captura: La acera del árbol y la farola termina en una esquina redondeada en x≈645–840, y≈500–600; por delante cruza la calzada de la otra calle.
   - Juego: La acera con árboles llega hasta el borde inferior (x≈330–560, y≈600–693) y la esquina queda más cerca y más a la izquierda (x≈560–780, y≈590–693).
2076. [media] Color de fachada — edificio del fondo derecho (x≈1150–1440)
   - Captura: Edificio de tapia blanca con la parte alta pintada de salmón rosado (x≈1150–1340, y≈250–315) y borde de teja.
   - Juego: Nave gris blanquecina lejana (x≈1235–1440, y≈260–375).
2077. [media] Vegetación — árbol grande en primer plano a la izquierda
   - Captura: No hay árbol en primer plano: en x≈0–600 se ve la calzada, un coche y la nave; el único árbol cercano es esbelto y estrecho (x≈615–740, y≈125–505).
   - Juego: Árbol de copa ancha que tapa media imagen (x≈0–690, y≈0–620), con su alcorque en x≈370–535, y≈620–680.
2078. [media] Mobiliario — farola de la esquina
   - Captura: Báculo alto y curvo de farola junto al árbol (x≈655–690, y≈0–510).
   - Juego: Farola negra baja (x≈545–570, y≈315–520).
2079. [baja] Mobiliario — placa de calle y señal en la esquina del edificio derecho
   - Captura: Placa de la calle (x≈795–825, y≈305–320) y señal vista por detrás (x≈795–830, y≈320–370) en la esquina.
   - Juego: Sin placa ni señal.
2080. [baja] Otros — tendido eléctrico
   - Captura: Cables que cruzan el cielo (x≈820–1440, y≈0–200) y un poste (x≈1335–1360, y≈195–420).
   - Juego: Sin cables ni poste.
**Vista #207** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_207.jpg

2081. [alta] Geometría — edificación de la izquierda
   - Captura: Tras la valla, un patio industrial y, retranqueadas, una nave beige con marquesina (x≈0–480, y≈300–360) y una nave gris (x≈480–710, y≈280–385).
   - Juego: Casa blanca de una planta con tejado de teja roja y ventanas enrejadas, pegada a la acera (x≈0–550, y≈215–590), y detrás una nave gris (x≈455–700, y≈260–375).
2082. [alta] Geometría — calzada y lado derecho
   - Captura: Calzada de asfalto muy ancha: a la altura y≈650 va de x≈330 hasta el borde derecho, y a la derecha el asfalto llega hasta la acera estrecha al pie de la tapia (y≈440–455).
   - Juego: Calzada más estrecha (a la altura y≈650, de x≈180 a x≈1080) y toda la mitad derecha es una explanada elevada de losas blancas con bordillo (x≈780–1440, y≈360–693).
2083. [alta] Muros y vallas — valla metálica de la izquierda
   - Captura: Valla larga de barrotes metálicos gris oscuro sobre murete (x≈0–515, y≈350–600) con un pilar de hormigón (x≈510–540, y≈350–445).
   - Juego: No hay valla.
2084. [alta] Muros y vallas — tapia blanca de la derecha
   - Captura: Tapia blanca con pilares rematados (x≈960–1425, y≈330–445) y verja verde encima (x≈880–1360, y≈335–390); detrás, naves con tejado de teja (x≈880–1100, y≈305–345).
   - Juego: No hay tapia: explanada abierta y una nave gris lejana (x≈860–1095, y≈285–390).
2085. [media] Vegetación — árbol grande en primer plano a la izquierda
   - Captura: No hay árbol en primer plano (solo árboles esbeltos más lejos, x≈605–660).
   - Juego: Árbol de copa ancha en primer plano (x≈0–350, y≈0–460).
2086. [media] Vegetación — árbol grande en primer plano a la derecha
   - Captura: No hay árbol en primer plano a la derecha.
   - Juego: Árbol de copa ancha en primer plano (x≈1050–1440, y≈0–550).
2087. [media] Mobiliario — farolas de la acera derecha
   - Captura: Báculos altos de brazo curvo (x≈840–910, y≈180–410; x≈785–815, y≈285–375).
   - Juego: Farola negra baja (x≈795–835, y≈265–410).
2088. [media] Otros — valla publicitaria de la derecha
   - Captura: Gran panel publicitario blanco (x≈1065–1295, y≈240–325).
   - Juego: No existe.
2089. [baja] Otros — mástil de antenas
   - Captura: Mástil de telecomunicaciones (x≈1000–1015, y≈250–310).
   - Juego: No existe.
**Vista #208** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_208.jpg

2090. [alta] Geometría — caseta de transformador de la izquierda
   - Captura: Caseta de color gris oscuro con rejillas y señal de peligro (x≈0–150, y≈300–490).
   - Juego: No existe: explanada abierta.
2091. [alta] Geometría — anchura de la calzada
   - Captura: A la altura y≈600 la calzada va de x≈130 a x≈1240.
   - Juego: A la altura y≈600 la calzada va de x≈390 a x≈1150: bastante más estrecha.
2092. [alta] Muros y vallas — tapia con verja de la izquierda
   - Captura: Tapia blanca con pilares y verja de hierro encima a lo largo de la acera (x≈150–700, y≈320–470).
   - Juego: No hay tapia ni verja.
2093. [media] Color de fachada — naves del fondo izquierdo
   - Captura: Naves con cubierta y paramentos verdes (x≈160–460, y≈295–345).
   - Juego: Naves gris blanquecino con puertas azules (x≈0–480, y≈295–365).
2094. [media] Marcas viales — paso de peatones de la calle
   - Captura: Paso de cebra que cruza la calzada (x≈580–850, y≈390–410).
   - Juego: Sin paso de cebra.
2095. [media] Acera y bordillo — suelo del lado izquierdo
   - Captura: Acera gris estrecha al pie de la tapia (x≈0–560, y≈440–600); detrás, un patio con maquinaria agrícola (x≈250–520, y≈360–420).
   - Juego: Explanada enorme de losas blancas desde el bordillo hasta las naves del fondo (x≈0–620, y≈350–693).
2096. [media] Vegetación — árboles de la acera derecha
   - Captura: No hay árboles delante de la nave de la derecha.
   - Juego: Hilera de árboles redondos delante de la nave (x≈785–1055, y≈255–455).
2097. [media] Mobiliario — farola alta de la acera izquierda
   - Captura: Báculo alto de farola en primer plano (x≈390–415, y≈0–460).
   - Juego: No hay farola a la izquierda.
2098. [media] Vehículos — zona de la derecha tras la nave
   - Captura: Calle transversal con un solo coche circulando (x≈1160–1225, y≈350–380).
   - Juego: Aparcamiento lleno de coches (x≈1100–1440, y≈350–500).
2099. [baja] Detalles de fachada — nervios de la nave de la derecha
   - Captura: Pilastras/nervios verticales verde oscuro entre paneles (x≈940 y x≈1070–1095, y≈90–475) y una ventanita (x≈860–870, y≈270–290).
   - Juego: Paramento gris sin nervios verdes, con una banda de ventanas arriba (x≈970–1040, y≈200–250).
2100. [baja] Marcas viales — paso de peatones de la calle transversal derecha
   - Captura: Paso de cebra en la calle de la derecha (x≈1195–1440, y≈420–455).
   - Juego: Sin paso de cebra.
2101. [baja] Otros — torre eléctrica de celosía
   - Captura: Torre metálica de celosía tras la tapia (x≈375–395, y≈195–300).
   - Juego: No existe.

### Calle Severo Ochoa

**Vista #209** — 02_Desde_un_extremo_hacia_el_otro.jpg (mayo de 2024) · hoja a_209.jpg

2102. [alta] Geometría — casa de la esquina en primer plano a la izquierda
   - Captura: Casa de dos plantas que sube hasta el borde superior de la imagen (x≈0–380, y≈0–520), con su costado blanco en x≈300–380.
   - Juego: Casa de una sola planta: su alero queda en y≈215–320 y por encima solo hay cielo (x≈0–410, y≈215–610).
2103. [alta] Otros — solar de la derecha
   - Captura: Solar de hierba alta seca (x≈790–1440, y≈365–560).
   - Juego: Explanada pavimentada blanca con arbolitos redondos (x≈755–805, x≈940–1080) y un ciprés (x≈850–870, y≈280–365) (x≈720–1440, y≈360–560).
2104. [media] Huecos — casa amarilla de la derecha (planta alta)
   - Captura: Paño amarillo de la planta alta sin ventanas, solo un aparato de aire (x≈1180–1205, y≈335–345).
   - Juego: Fila de ventanas en la planta alta (x≈1045–1075, x≈1130–1170, x≈1245–1300, y≈265–330) y otra en la baja.
2105. [media] Cubierta — remate de la casa de la esquina izquierda
   - Captura: Pretil con balaustrada en lo alto del costado (x≈320–360, y≈120–250), sin tejado visible.
   - Juego: Tejado de teja naranja con alero de tejas redondeadas (x≈0–410, y≈215–320).
2106. [media] Vegetación — árboles y seto detrás de la farola izquierda
   - Captura: Conífera alta (x≈455–550, y≈200–370), árboles redondos (x≈520–625, y≈285–370) y seto (x≈390–640, y≈360–400).
   - Juego: No hay árboles ni seto: se ven casas blancas con tejado rojo (x≈400–620, y≈310–375).
2107. [media] Mobiliario — farola de la izquierda
   - Captura: Báculo alto y recto (x≈440–455, y≈0–380).
   - Juego: Farola negra de brazo, más baja y más a la derecha (x≈590–645, y≈240–425).
2108. [media] Muros y vallas — tapia de bloques al fondo del solar
   - Captura: Tapia de bloques de hormigón gris que cierra el solar (x≈875–1330, y≈345–390).
   - Juego: No hay tapia.
2109. [baja] Cubierta — tejado de la casa amarilla de la derecha
   - Captura: Placas solares (x≈1005–1085, y≈250–300), un cuerpo elevado con tejado propio (x≈1135–1255, y≈225–270), chimenea alta (x≈1350–1385, y≈180–255) y antena.
   - Juego: Faldón de teja liso, sin placas, sin cuerpo elevado ni chimenea.
2110. [baja] Marcas viales — bordillo derecho pintado
   - Captura: Bordillo pintado de amarillo a lo largo de la acera derecha (x≈800–1360, y≈380–620).
   - Juego: Sin pintura amarilla.
2111. [baja] Mobiliario — placa de la calle
   - Captura: Placa «Calle Severo Ochoa» en la fachada (x≈160–245, y≈205–235).
   - Juego: Sin placa.
2112. [baja] Mobiliario — contenedores
   - Captura: Contenedores de basura junto a la acera derecha (x≈735–760, y≈370–392).
   - Juego: Sin contenedores.
**Vista #210** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_210.jpg

2113. [alta] Otros — solar de la derecha en primer plano
   - Captura: Solar de tierra rojiza con hierbas (x≈870–1440, y≈410–693).
   - Juego: Explanada pavimentada blanca (x≈760–1440, y≈390–693).
2114. [media] Color de fachada — edificio del fondo de la calle
   - Captura: Nave de ladrillo rojo con rótulo (x≈705–795, y≈315–370).
   - Juego: Casas blancas con tejado rojo (x≈610–780, y≈315–355).
2115. [media] Huecos — segunda nave de la izquierda
   - Captura: Gran puerta corredera azul (x≈405–480, y≈310–385).
   - Juego: La nave de esa posición (x≈360–610) solo tiene bandas de ventanas; sin puerta azul grande.
2116. [media] Huecos — puerta del edificio de la esquina derecha
   - Captura: Puerta acristalada de local (x≈1015–1060, y≈340–385).
   - Juego: Puertas azules de nave (x≈960–990 y x≈1045–1075, y≈345–385).
2117. [media] Cubierta — edificio blanco de la esquina derecha
   - Captura: Edificio blanco de una planta con tejado de teja roja (x≈840–1095, y≈295–390) y un tejadillo metálico a su izquierda (x≈790–860, y≈310–330).
   - Juego: Nave gris de cubierta a dos aguas metálica, sin teja (x≈775–1105, y≈275–385).
2118. [media] Cubierta — edificio beige de dos plantas del fondo derecho
   - Captura: Cubierta plana, sin teja (x≈1150–1440, y≈295–375).
   - Juego: Tejado de teja roja (x≈1080–1440, y≈290–310) y toldos verdes (x≈1160–1260, y≈345–355).
2119. [media] Mobiliario — farola de la acera derecha en primer plano
   - Captura: Báculo alto de brazo (x≈835–850, y≈160–440).
   - Juego: Farola negra más baja y lejana (x≈800–820, y≈285–390).
2120. [media] Muros y vallas — valla de la izquierda
   - Captura: Valla de malla metálica con postes acodados y alambre de espino sobre un murete (x≈20–340, y≈355–490) y un pilar de cancela con remate de teja (x≈0–80, y≈260–480).
   - Juego: Sin valla: un bloque beige liso en el borde (x≈0–115, y≈255–495) y suelo abierto.
2121. [baja] Marcas viales — paso de peatones del fondo
   - Captura: Paso de cebra al final del tramo (x≈600–690, y≈393–402).
   - Juego: Sin paso de cebra.
2122. [baja] Acera y bordillo — acera derecha
   - Captura: Baldosa gris con el bordillo pintado de amarillo (x≈760–1010, y≈440–693).
   - Juego: Franja de baldosa rosa con bordillo blanco.
**Vista #211** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_211.jpg

2123. [alta] Otros — patio de tierra de la izquierda
   - Captura: Patio de tierra arenosa con camiones delante de la nave (x≈0–360, y≈420–600) y una acera gris estrecha (x≈200–380, y≈480–693).
   - Juego: Explanada pavimentada blanca (x≈0–560, y≈370–560) y una acera rosa ancha (x≈0–590, y≈380–693).
2124. [media] Huecos — ventanas de la nave de la derecha
   - Captura: Ventanas sueltas con reja oscura (x≈1215–1370, y≈165–260; x≈955–990, y≈260–300; x≈860–875, y≈290–315).
   - Juego: Banda continua de ventanas horizontales (x≈850–1440, y≈320–365).
2125. [media] Detalles de fachada — rótulo pintado de la nave de la derecha
   - Captura: Gran rótulo pintado en letras rojas «AUTO RECAMBIOS MARAÑA» a lo largo de la fachada (x≈845–1370, y≈95–290).
   - Juego: Fachada lisa sin rótulo.
2126. [media] Acera y bordillo — acera derecha
   - Captura: Baldosa gris (x≈750–1300, y≈380–693).
   - Juego: Baldosa rosa con bordillo blanco (x≈760–1440, y≈380–693).
2127. [media] Vegetación — franja de hierba al pie de la nave derecha
   - Captura: Franja de hierba y matas verdes entre la acera y la nave (x≈770–1440, y≈380–620).
   - Juego: Sin hierba: la acera llega hasta la pared.
2128. [media] Mobiliario — farola alta de la izquierda
   - Captura: Báculo alto de farola (x≈510–535, y≈95–390).
   - Juego: Farola negra baja y lejana (x≈535–545, y≈295–380).
2129. [baja] Vegetación — ciprés y árboles del fondo izquierdo
   - Captura: No hay ciprés; al fondo se ven casas y farolas.
   - Juego: Ciprés (x≈405–435, y≈250–370) y árboles redondos (x≈458–515 y x≈585–625, y≈330–365).

### Calle Vicente Aleixandre

**Vista #212** — 02_Desde_un_extremo_hacia_el_otro.jpg (mayo de 2024) · hoja a_212.jpg

2130. [alta] Geometría — posición de la calzada
   - Captura: La calzada es estrecha y queda en el centro: el bordillo izquierdo llega al borde inferior en x≈380 (sube hasta x≈690, y≈385) y a su izquierda hay acera gris (x≈180–690).
   - Juego: La calzada está desplazada a la derecha: el bordillo izquierdo está en x≈760–815 en la parte baja; todo lo que queda a su izquierda es explanada.
2131. [alta] Geometría — edificio de la derecha
   - Captura: Edificio comercial blanco: cuerpo de una planta con alero de teja roja (x≈845–1180, y≈145–295) y, a la derecha, un cuerpo blanco más alto que sale por arriba de la imagen (x≈1180–1440).
   - Juego: Nave industrial gris con cubierta metálica a dos aguas (x≈855–1440, y≈80–535), sin teja.
2132. [alta] Otros — solar de la izquierda
   - Captura: Solar de tierra con hierba seca (x≈0–680, y≈360–693), separado de la calle por una acera gris.
   - Juego: Gran explanada de losas blancas (x≈0–760, y≈370–693) que llega hasta el bordillo.
2133. [media] Huecos — entrada del edificio de la derecha
   - Captura: Entrada rehundida con puertas y ventanales de vidrio con carpintería blanca (x≈955–1170, y≈310–520) sobre un zócalo de ladrillo.
   - Juego: Portones azules de nave (x≈980–1045, y≈340–460; x≈1140–1265, y≈340–510; x≈865–885, y≈345–400), sin vidrio.
2134. [media] Vegetación — árboles de la izquierda
   - Captura: Solo una conífera lejana detrás del solar (x≈455–500, y≈280–350) y un arbolito (x≈395–415, y≈320–345).
   - Juego: Ciprés grande en mitad de la explanada (x≈440–525, y≈80–415), un árbol tipo olivo (x≈385–460, y≈310–400) y otro pequeño (x≈180–245, y≈345–375).
2135. [media] Mobiliario — farola de la acera izquierda
   - Captura: Báculo alto gris con luminaria pequeña en lo alto (x≈540–560, y≈0–490).
   - Juego: Farola negra de cabeza rectangular, más a la derecha, junto al bordillo (x≈715–840, y≈100–545).
2136. [media] Muros y vallas — tapia de bloques al fondo del solar
   - Captura: Tapia de bloques de hormigón gris (x≈0–225, y≈325–390).
   - Juego: No hay tapia: se ve directamente una casa amarilla (x≈0–135, y≈255–390).
2137. [baja] Color de fachada — primera casa de la hilera del fondo izquierdo
   - Captura: Casas beige/blancas con tejado de teja y placas solares (x≈0–300, y≈255–345).
   - Juego: La primera es amarilla intensa (x≈0–135, y≈255–390).
2138. [baja] Detalles de fachada — rótulo verde del edificio de la derecha
   - Captura: Letras verdes de un rótulo en lo alto del cuerpo alto (x≈1330–1440, y≈0–60).
   - Juego: Sin rótulo.
2139. [baja] Mobiliario — contenedores
   - Captura: Contenedores al fondo del solar (x≈370–425, y≈350–365).
   - Juego: Sin contenedores.
**Vista #213** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_213.jpg

2140. [alta] Geometría — muro alto de la izquierda
   - Captura: Muro encalado muy alto y ciego de una nave, pegado a la acera, que sale por arriba de la imagen (x≈120–635, y≈0–690), con desconchones y solo una cajita eléctrica (x≈340–385, y≈525–565).
   - Juego: Casa blanca de una planta con tejado de teja naranja y una ventana con macetas (x≈0–415, y≈170–680); detrás, una explanada abierta y naves lejanas (x≈320–690, y≈255–500).
2141. [media] Color de fachada — paramento del borde izquierdo
   - Captura: Pared pintada de gris azulado (x≈0–125, y≈210–693).
   - Juego: Pared blanca de la casa con bajante (x≈0–60).
2142. [media] Huecos — huecos de la nave de la derecha
   - Captura: Solo ventanas sueltas en lo alto (x≈1005–1120, y≈95–215; x≈870–905, y≈220–275; x≈815–835, y≈260–295); ninguna puerta.
   - Juego: Bandas de ventanas a media altura (x≈945–1155, y≈315–380; x≈1340–1440, y≈290–400) y puertas azules (x≈780–830, y≈345–430).
2143. [media] Mobiliario — farola de la derecha
   - Captura: Aplique con brazo colgado del muro de la nave (x≈800–850, y≈215–235).
   - Juego: Farola negra de pie en la acera (x≈775–870, y≈150–500).
**Vista #214** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_214.jpg

2144. [alta] Geometría — silos de la izquierda
   - Captura: Varios silos metálicos altos asomando por encima de la tapia (x≈370–670, y≈0–280).
   - Juego: Un único depósito blanco ancho y bajo (x≈0–305, y≈115–405); en x≈370–700 hay una nave baja (y≈275–375).
2145. [alta] Muros y vallas — tapia alta de la izquierda
   - Captura: Tapia encalada alta y continua con albardilla de teja a lo largo de todo el lado izquierdo (x≈0–710, y≈0–600).
   - Juego: No hay tapia: el lado izquierdo está abierto.
2146. [media] Geometría — nave de chapa del fondo derecho
   - Captura: Nave de chapa gris con cubierta metálica (x≈760–1070, y≈255–390).
   - Juego: Casa con tejado de teja naranja y toldos de rayas rojas y blancas (x≈745–905, y≈315–385) y una nave blanca pequeña (x≈905–1045, y≈300–410).
2147. [media] Color de fachada — edificio central de la derecha (x≈1040–1165)
   - Captura: Caseta prefabricada blanca y muro gris (x≈975–1200, y≈345–435).
   - Juego: Edificio de color ladrillo anaranjado con tejado de teja (x≈1040–1165, y≈285–395).
2148. [media] Detalles de fachada — edificio del borde derecho
   - Captura: Edificio blanco con rótulo y marquesina azul curva «CENTRO DE LA…» (x≈1210–1440, y≈275–320) y carteles en la fachada.
   - Juego: Nave gris con puerta azul (x≈1190–1250, y≈345–435) y banda de ventanas; sin rótulo ni marquesina.
2149. [media] Acera y bordillo — suelo del lado izquierdo
   - Captura: Acera gris estrecha al pie de la tapia (x≈330–710, y≈390–693).
   - Juego: Acera blanca y, detrás, una explanada muy ancha de losas grises (x≈0–680, y≈380–693).
2150. [baja] Mobiliario — farola
   - Captura: Aplique de brazo colgado de la tapia izquierda (x≈640–690, y≈190–280).
   - Juego: Farola negra de pie en la acera derecha (x≈785–820, y≈285–395).

### Camino del Gamero

**Vista #215** — 02_Desde_un_extremo_hacia_el_otro.jpg (mayo de 2024) · hoja a_215.jpg

2151. [alta] Geometría — anchura de calzada y aceras
   - Captura: Calzada muy ancha y aceras estrechas: a la altura y≈650 la acera izquierda va de x≈220 a x≈360 y el asfalto de x≈360 hasta pasado el borde derecho; la acera derecha es una franja estrecha al pie de la tapia (y≈500–560 en x=1440).
   - Juego: Calzada más estrecha (a la altura y≈650, de x≈625 a x≈1310) con aceras blancas muy anchas a ambos lados (izquierda x≈0–620; derecha desde x≈1310).
2152. [media] Geometría — nave blanca de la izquierda
   - Captura: Nave blanca cercana y alta: remate en y≈200–245, ocupa x≈0–460 (y≈200–360).
   - Juego: Nave gris más lejana y baja: remate en y≈280–300, ocupa x≈0–420 (y≈280–375).
2153. [media] Huecos — ventana en la tapia beige de la derecha
   - Captura: Tapia ciega salvo la puerta metálica gris (x≈970–1015, y≈345–410).
   - Juego: Además de la puerta, una ventana con persiana (x≈1055–1105, y≈350–405).
2154. [media] Cubierta — tapia beige de la derecha (x≈920–1185)
   - Captura: Tapia de remate plano, sin tejado; las casas de dos plantas quedan detrás.
   - Juego: Casa de una planta con tejado de teja naranja sobre ese tramo (x≈910–1195, y≈295–330).
2155. [media] Mobiliario — poste alto en primer plano a la izquierda
   - Captura: Poste/báculo grueso gris (x≈30–75, y≈0–355).
   - Juego: No hay poste.
2156. [media] Muros y vallas — cerca de placas de hormigón al pie de la nave
   - Captura: Cerca de placas de hormigón gris claro (x≈80–460, y≈300–360).
   - Juego: Sin cerca.
2157. [baja] Color de fachada — casa de dos plantas del borde derecho
   - Captura: Casa beige con tejado de teja, chimenea y calentador solar (x≈1230–1440, y≈165–300).
   - Juego: Casa blanca (x≈1185–1440, y≈165–450), sin chimenea.
2158. [baja] Huecos — portón de la derecha
   - Captura: Portón corredero marrón oscuro muy alto (x≈1240–1440, y≈315–500).
   - Juego: Puerta de cochera marrón más baja (x≈1215–1400, y≈345–410) con un balcón encima (x≈1245–1355, y≈285–320) que la captura no tiene.
**Vista #216** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_216.jpg

2159. [alta] Geometría — anchura de calzada y aceras
   - Captura: Calzada muy ancha: a la altura y≈650 va de x≈330 hasta el borde derecho; la acera izquierda es estrecha (x≈160–330) y la derecha también (y≈440–490 en x=1440).
   - Juego: Calzada más estrecha (a la altura y≈650, de x≈595 a x≈1330) y aceras blancas muy anchas (izquierda x≈0–595).
2160. [alta] Muros y vallas — tapia larga de la derecha
   - Captura: Tapia encalada larga con albardilla de teja y un gran portón metálico verde (x≈1015–1125, y≈305–405), a lo largo de la acera (x≈995–1440, y≈285–450).
   - Juego: No hay tapia: explanada blanca abierta con árboles y una nave retranqueada.
2161. [media] Color de fachada — edificio de ladrillo del fondo derecho
   - Captura: Muro/edificio de ladrillo rojo (x≈880–995, y≈320–375) junto a una nave gris pequeña (x≈830–880, y≈318–370).
   - Juego: Una sola nave gris grande con puertas azules (x≈810–1060, y≈285–380); sin ladrillo.
2162. [media] Vegetación — árboles de la derecha
   - Captura: No hay árboles a la derecha.
   - Juego: Ciprés (x≈1090–1150, y≈185–390) y árboles de copa redonda (x≈1185–1410, y≈265–375).
2163. [media] Vegetación — campo de la izquierda
   - Captura: Hierba verde y matas altas junto a la acera (x≈0–690, y≈420–600) y un camino de tierra rojiza (x≈0–560, y≈360–430).
   - Juego: Campo amarillo uniforme (x≈0–680, y≈345–610), sin hierba verde ni camino.
**Vista #217** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_217.jpg

2164. [alta] Geometría — edificación de la izquierda
   - Captura: Hilera de edificios bajos de una planta con cubierta inclinada (remate en y≈295–345), de x≈0 a x≈560.
   - Juego: Nave industrial mucho más alta (remate en y≈190–260) con bandas de ventanas y una puerta azul (x≈440–465, y≈345–405), de x≈0 a x≈535.
2165. [alta] Geometría — anchura de calzada y aceras
   - Captura: Acera izquierda estrecha (su bordillo llega a x=0 en y≈560), calzada ancha (a la altura y≈600, de x≈0 a x≈1120) y acera derecha ancha de baldosa con relieve (a la altura y≈650, x≈1150–1440).
   - Juego: Acera izquierda blanca muy ancha (a la altura y≈600, x≈0–440), calzada estrecha (x≈440–1060) y acera derecha estrecha (a la altura y≈650, x≈1100–1260).
2166. [alta] Color de fachada — edificio más cercano de la izquierda (x≈0–190)
   - Captura: Muro de ladrillo visto rojo (x≈0–190, y≈330–500).
   - Juego: Paramento gris-blanco de la nave.
2167. [media] Color de fachada — edificio central de la izquierda (x≈190–480)
   - Captura: Revoco beige con una puerta blanca (x≈385–405, y≈360–420) y bajante.
   - Juego: Paramento gris-blanco con bandas de ventanas.
2168. [media] Cubierta — cubiertas de la izquierda
   - Captura: Placas onduladas de fibrocemento inclinadas a la vista (x≈0–560, y≈295–345).
   - Juego: Remate plano de nave, sin placas visibles.
2169. [media] Marcas viales — paso de peatones
   - Captura: Paso de cebra que cruza la calzada (x≈425–700, y≈410–440).
   - Juego: Sin paso de cebra.
2170. [media] Vegetación — campo de la derecha
   - Captura: Campo con hierba verde y parda y un camino de tierra (x≈790–1440, y≈345–600).
   - Juego: Campo amarillo uniforme (x≈745–1440, y≈345–693).
2171. [media] Mobiliario — farolas de la derecha
   - Captura: Báculos altos de brazo curvo (x≈805–855, y≈200–405; x≈760–775, y≈290–360).
   - Juego: Farola negra de brazo recto, más baja (x≈765–805, y≈270–405).
2172. [baja] Otros — silos del fondo
   - Captura: Silos blancos junto a la nave del fondo (x≈1020–1080 y x≈1140–1160, y≈320–340).
   - Juego: Sin silos.

### Carretera de Guareña a Manchita

**Vista #218** — 02_Desde_un_extremo_hacia_el_otro.jpg (mayo de 2024) · hoja a_218.jpg

2173. [media] Marcas viales — líneas de la carretera
   - Captura: Línea continua blanca en ambos bordes (izquierda x≈90–690; derecha x≈735–890) y línea central discontinua (x≈630–720, y≈355–470).
   - Juego: Calzada sin ninguna marca.
2174. [media] Vegetación — seto bajo del borde izquierdo
   - Captura: Seto bajo continuo a lo largo del borde izquierdo de la calzada (x≈0–680, y≈420–560).
   - Juego: Sin seto: bordillo blanco y arena amarilla.
2175. [media] Vegetación — seto bajo del borde derecho
   - Captura: Seto bajo continuo a lo largo del borde derecho (x≈740–1300, y≈355–690) y arbustos redondos (x≈850–990, y≈360–450).
   - Juego: Sin seto ni arbustos.
2176. [media] Vegetación — árbol de la izquierda en primer plano
   - Captura: Árbol desmochado de copa pequeña y rala (x≈150–300, y≈235–460).
   - Juego: Árbol de copa redonda enorme que tapa media izquierda (x≈0–445, y≈45–555), con alcorque (x≈45–260, y≈525–580).
2177. [media] Vegetación — árbol de la derecha en primer plano
   - Captura: Árboles desmochados de copa pequeña, alejados de la calzada (x≈1085–1200 y x≈1280–1420, y≈300–500); junto al borde de la calzada solo hay seto.
   - Juego: Árbol de copa redonda enorme junto al bordillo (x≈700–1385, y≈5–590), con alcorque (x≈855–1000, y≈530–595).
2178. [media] Vegetación — seto alto ante la nave de la izquierda
   - Captura: Seto alto y denso verde y rojizo delante de la nave (x≈0–620, y≈300–420).
   - Juego: Sin seto alto.
2179. [media] Muros y vallas — murete y vía de servicio de la izquierda
   - Captura: Murete de hormigón (x≈0–560, y≈400–470) junto a una franja pavimentada (x≈0–620, y≈380–500).
   - Juego: Arena amarilla, sin murete ni franja pavimentada.
2180. [media] Otros — carril bici de la derecha
   - Captura: Carril bici verde (x≈990–1440, y≈410–540).
   - Juego: No existe.
2181. [baja] Vegetación — palmera del fondo izquierdo
   - Captura: Palmera (x≈600–630, y≈280–330).
   - Juego: Árboles redondos en esa posición.
2182. [baja] Otros — terreno de la derecha
   - Captura: Tierra parda con grava (x≈760–1440, y≈370–693).
   - Juego: Arena amarilla saturada (x≈760–1440, y≈365–693).
**Vista #219** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_219.jpg

2183. [alta] Color de fachada — parte alta del concesionario
   - Captura: Revestimiento de chapa azul intenso (x≈0–470, y≈90–270).
   - Juego: Paramento blanco grisáceo (x≈0–520, y≈100–340).
2184. [media] Huecos — concesionario de la izquierda
   - Captura: Gran escaparate acristalado con coches y motos dentro (x≈30–465, y≈220–440).
   - Juego: Muro ciego de nave con portones azules (x≈40–215, y≈340–500; x≈300–375, y≈345–440; x≈480–505, y≈350–400).
2185. [media] Detalles de fachada — rótulo del concesionario
   - Captura: Banda azul con el rótulo «BADAJOZ PORTU… Nº1 DEL SIN CARNET» (x≈240–440, y≈220–290).
   - Juego: Sin rótulo.
2186. [media] Marcas viales — líneas de la carretera
   - Captura: Líneas blancas de borde (izquierda x≈540–690; derecha x≈800–1300) y central discontinua (x≈760–790 y x≈850–940, y≈420–680).
   - Juego: Calzada sin marcas.
2187. [media] Acera y bordillo — explanada delante del concesionario
   - Captura: Explanada pavimentada gris clara (x≈0–620, y≈420–600).
   - Juego: Arena amarilla (x≈0–700, y≈360–693).
2188. [media] Vegetación — seto del borde izquierdo
   - Captura: Seto bajo continuo junto a la calzada (x≈230–665, y≈370–640).
   - Juego: Sin seto.
2189. [media] Vegetación — seto del borde derecho
   - Captura: Seto bajo continuo (x≈810–1440, y≈370–600) y arbustos redondos (x≈865–945, y≈350–400).
   - Juego: Sin seto ni arbustos.
2190. [media] Vegetación — árbol de la izquierda
   - Captura: Árbol desmochado de ramas desnudas y copa mínima (x≈420–510, y≈260–455).
   - Juego: Árbol de copa redonda grande (x≈340–700, y≈170–500).
2191. [media] Vegetación — árboles de la derecha
   - Captura: Árboles de copa moderada, separados de la calzada por el seto (x≈1015–1100, y≈290–400; x≈1180–1340, y≈265–475).
   - Juego: Árbol de copa redonda enorme junto al bordillo (x≈915–1440, y≈125–495).
2192. [media] Muros y vallas — valla azul ante el concesionario
   - Captura: Valla metálica azul (x≈30–560, y≈330–440) sobre un murete blanco (x≈0–560, y≈420–480).
   - Juego: Sin valla ni murete.
2193. [baja] Otros — carril bici de la derecha
   - Captura: Carril bici verde (x≈950–1440, y≈385–500).
   - Juego: Franja gris (x≈870–1440, y≈370–480).
**Vista #220** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_220.jpg

2194. [media] Marcas viales — líneas de la carretera
   - Captura: Línea central discontinua (x≈580–800, y≈380–693) y línea de borde izquierda continua (x≈200–740).
   - Juego: Calzada sin marcas.
2195. [media] Acera y bordillo — bordes de la calzada
   - Captura: Asfalto sin bordillos: a la izquierda termina en tierra y a la derecha sigue en un arcén ancho de asfalto hasta la cuneta (x≈850–1440, y≈400–693).
   - Juego: Bordillos blancos a ambos lados (izquierda x≈455–700; derecha x≈850–1120), un parterre de tierra con alcorques a la derecha (x≈880–1440, y≈385–575) y otra calzada en la esquina inferior derecha (x≈1100–1440, y≈575–693).
2196. [media] Vegetación — arbustos del lado izquierdo
   - Captura: Arbustos recortados en bola (x≈0–290, y≈400–560; x≈350–480, y≈360–450; x≈490–560, y≈370–420) y seto bajo junto a la calzada (x≈385–760, y≈390–490).
   - Juego: Sin arbustos ni seto: franjas de tierra arada, arena amarilla y prado verde.
2197. [media] Vegetación — árboles del lado izquierdo
   - Captura: Un solo árbol desmochado, lejos de la calzada (x≈230–345, y≈300–440).
   - Juego: Hilera de árboles de copa redonda junto al bordillo (x≈380–660, y≈215–460; x≈655–790, y≈290–395) con alcorques.
2198. [media] Vegetación — árboles del lado derecho
   - Captura: Sin árboles: cuneta con hierba seca y flores amarillas (x≈850–1440, y≈360–440) y la nave detrás.
   - Juego: Árbol de copa enorme en primer plano (x≈875–1440, y≈105–520) y otros detrás (x≈820–910).
2199. [baja] Otros — tendido eléctrico
   - Captura: No hay cables sobre la carretera.
   - Juego: Tendido de cables que cruza el cielo a la izquierda (x≈295–680, y≈0–340).

### Dámaso Fernández del Pozo

**Vista #221** — 02_Desde_un_extremo_hacia_el_otro.jpg (mayo de 2024) · hoja a_221.jpg

2200. [media] Geometría — longitud del pabellón hacia la derecha
   - Captura: El muro de bloques sigue hasta el borde derecho de la imagen (x=1440).
   - Juego: El edificio termina en x≈1340; a su derecha hay un árbol (x≈1340–1440, y≈130–380) y espacio abierto.
2201. [media] Color de fachada — paramento del pabellón de la derecha
   - Captura: Muro de bloques de hormigón color beige grisáceo con las hiladas a la vista (x≈345–1440, y≈0–560).
   - Juego: Paramento liso gris blanquecino (x≈355–1340, y≈0–565).
2202. [media] Huecos — ventanas y puertas del pabellón
   - Captura: Una sola fila alta de ventanales verticales, uno por crujía (x≈380–830, y≈0–270); parte baja ciega, sin puertas en el tramo visible.
   - Juego: Tres niveles de ventanas apaisadas en banda (x≈420–1245, y≈0–360) y puertas azules a ras de suelo (x≈500–770, y≈340–400).
2203. [media] Detalles de fachada — machón pintado en primer plano
   - Captura: Machón blanco con un motivo pintado de flores (tulipanes rojos y amarillos, flor azul) enmarcado en rojo y un rombo debajo (x≈905–1030, y≈0–600).
   - Juego: No existe; paramento liso.
2204. [media] Calzada — suelo delante del pabellón
   - Captura: Asfalto continuo desde la izquierda hasta la acera estrecha al pie del muro (x≈0–1440, y≈350–693).
   - Juego: Calzada solo en x≈0–640 con bordillo; todo lo demás, hasta el pabellón, es una franja de arena amarilla (x≈310–1440, y≈370–693).
2205. [baja] Detalles de fachada — pilastras del pabellón
   - Captura: Pilastras que separan las crujías (x≈470, 530, 590, 635…, y≈90–410).
   - Juego: Fachada plana sin pilastras.
2206. [baja] Detalles de fachada — extremo izquierdo del pabellón
   - Captura: Extremo del muro sin banderas ni rótulo (x≈345–420, y≈280–390).
   - Juego: Mástiles con banderas (x≈405–435, y≈235–410), rótulo «Pabellón municipal La Encina» (x≈425–490, y≈305–330) y entrada acristalada (x≈445–465, y≈340–390).
**Vista #222** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_222.jpg

2207. [alta] Cámara — posición de la cámara
   - Captura: Cámara sobre el asfalto de la calle tras San Roque, junto a una acera de baldosa roja, mirando una zona verde con un banco de madera (x≈720–830, y≈430–500), árboles desmochados, pinos piñoneros (x≈650–1270, y≈95–340), seto (x≈655–1440, y≈315–460) y farolas curvas; la calzada gira a la izquierda.
   - Juego: Cámara sobre un parterre de arena entre dos calzadas (arena en el borde inferior x≈330–960; el bordillo y la calzada quedan a su izquierda, x≈0–360, mientras que en la captura el bordillo de la acera queda a la derecha de la cámara, en x≈1000): un arbusto pegado a la cámara tapa el tercio derecho (x≈860–1440, y≈80–693), y el tronco de una palmera (x≈700–835, y≈15–650), su copa (x≈200–1040, y≈0–250) y una farola (x≈610–660, y≈0–585) ocupan el centro; el encuadre no corresponde al de la captura y no se puede comparar.
**Vista #223** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_223.jpg

2208. [media] Geometría — cuerpo de entrada del extremo izquierdo
   - Captura: Cuerpo blanco saliente de entrada con ventanas y acceso rehundido (x≈480–600, y≈245–385).
   - Juego: No existe: la fachada termina en un plano liso en x≈490.
2209. [media] Geometría — extremo derecho del edificio
   - Captura: Fachada plana con un gran ventanal de retícula rosada (x≈1235–1440, y≈80–340) sobre una banda blanca.
   - Juego: Torreón de esquina redondeada con ventanas en banda (x≈1185–1440, y≈0–490).
2210. [media] Color de fachada — paramento del Centro Integral Territorial
   - Captura: Muro de bloques de hormigón beige con las hiladas a la vista (x≈480–1440, y≈0–460).
   - Juego: Paramento liso gris blanquecino (x≈490–1440, y≈0–490).
2211. [media] Huecos — ventanas del Centro Integral Territorial
   - Captura: Fila de ventanales grandes enmarcados entre pilares en la planta alta (x≈515–985, y≈185–300) sobre una banda blanca, y ventanas con rejilla en la baja (x≈735–985, y≈330–390).
   - Juego: Tres niveles de ventanas apaisadas pequeñas en banda (x≈490–1440) y puertas azules a ras de suelo (x≈545–740, x≈925–990, x≈1050–1145, y≈345–395).
2212. [media] Marcas viales — líneas en la calzada
   - Captura: Calzada sin marcas pintadas.
   - Juego: Líneas blancas continuas curvas (x≈40–195, y≈385–693; x≈210–1150, y≈380–693).
2213. [media] Acera y bordillo — acera delante del edificio
   - Captura: Acera ancha de baldosa gris con bordillo (x≈350–1440, y≈385–560).
   - Juego: Franja de arena amarilla (x≈330–1440, y≈375–630).
2214. [media] Vegetación — arbolado de la izquierda
   - Captura: Árboles grandes de hoja ancha (x≈0–430, y≈235–375).
   - Juego: Una palmera (x≈275–360, y≈285–365), arbolitos redondos (x≈330–410) y hojas de palmera en la esquina superior izquierda (x≈0–125, y≈20–250); detrás, casas con tejado rojo.
2215. [baja] Detalles de fachada — cartel de la Diputación
   - Captura: Cartel morado «Diputación de Badajoz» en la fachada (x≈1040–1120, y≈255–340).
   - Juego: Sin cartel.

### Plaza de Abastos

**Vista #224** — 02_Acceso_desde_Pajares.jpg (abril de 2009) · hoja a_224.jpg

2216. [alta] Geometría — edificio del fondo izquierdo de la plaza (x≈0–425)
   - Captura: Edificio encalado de dos plantas con cornisa, de x≈0 a x≈655 (y≈180–390).
   - Juego: Bloque de tres plantas (x≈0–425, y≈110–420), seguido de un edificio de dos plantas color crema (x≈425–710).
2217. [media] Geometría — calle al fondo de la plaza
   - Captura: La explanada llega hasta las fachadas del fondo, con jardineras al pie (x≈290–600, y≈375–400); no hay calzada entre la plaza y las casas.
   - Juego: Una calzada de asfalto gris separa la plaza de los edificios del fondo (x≈0–700, y≈395–445).
2218. [media] Geometría — cúpula y espadaña sobre los tejados del fondo
   - Captura: Sobre los tejados del fondo solo hay cielo (x≈540–670, y≈240–290).
   - Juego: Cúpula roja (x≈545–590, y≈255–290) y espadaña (x≈630–660, y≈250–275) asomando.
2219. [media] Color de fachada — edificio del fondo izquierdo de la plaza (x≈0–425)
   - Captura: Encalado blanco.
   - Juego: Beige grisáceo.
2220. [media] Color de fachada — casa del fondo central (x≈710–750)
   - Captura: Casa blanca con balcones (x≈720–770, y≈305–365).
   - Juego: Edificio rojo (x≈710–750, y≈310–365).
2221. [media] Huecos — planta baja del edificio del fondo izquierdo
   - Captura: Portones de madera (x≈240–290, y≈325–385; x≈435–480, y≈330–380), una puerta azul (x≈105–160, y≈330–395) y balcones de forja en la planta alta (x≈85–175, 230–300 y 335–385, y≈260–305).
   - Juego: Cochera con persiana blanca (x≈20–185, y≈345–420) y ventana con reja (x≈240–300, y≈345–385); balcones solo en x≈235–410 de un bloque más alto.
2222. [media] Huecos — tramo derecho de la fachada del mercado
   - Captura: Arco ciego con recercado ocre y ventana de postigos verdes (x≈1365–1440, y≈190–310); sin cierres metálicos.
   - Juego: Persiana metálica enrollable (x≈1340–1440, y≈330–530) y ventana enrejada (x≈1225–1270, y≈350–435).
2223. [media] Detalles de fachada — fachada del mercado (derecha)
   - Captura: Encalado con pilastras, recercados de arcos ciegos y cornisa en ocre amarillo, con pináculos en el pretil (x≈980–1440, y≈95–600); pequeño frontón curvo con placa sobre la entrada (x≈1005–1060, y≈200–260).
   - Juego: Fachada beige lisa sin pilastras ni arcos ciegos; portada clásica de piedra con frontón triangular, puerta verde y montante en abanico (x≈1075–1290, y≈165–460).
2224. [media] Cubierta — remate del mercado
   - Captura: Pretil con cornisa ocre y pináculos, sin tejado visible (x≈1000–1440, y≈95–290).
   - Juego: Alero de teja roja (x≈1200–1440, y≈30–170).
2225. [media] Calzada — firme de la calle San Gregorio
   - Captura: Adoquinado gris de piedra (x≈550–1000, y≈380–693).
   - Juego: Asfalto gris liso (x≈520–1440, y≈365–693).
2226. [media] Vegetación — jardineras y arbolitos de la plaza
   - Captura: Parterre con arbolito y arbustos (x≈100–190, y≈390–520) y jardineras con arbustos al pie de las fachadas (x≈290–600, y≈375–400).
   - Juego: Plaza sin vegetación; solo un banco (x≈760–800, y≈385–410).
2227. [media] Mobiliario — farolas de la plaza
   - Captura: Farolas de fundición de varios brazos con faroles (x≈515–565, y≈265–390; x≈735–755, y≈300–365).
   - Juego: Farolas negras sencillas en otras posiciones (x≈870–905, y≈290–390; x≈420–430, y≈290–390).
2228. [baja] Zócalo — zócalo del mercado
   - Captura: Zócalo ocre alto a lo largo de toda la fachada (x≈980–1440, y≈380–600).
   - Juego: Zócalo ocre solo en x≈1225–1340 (y≈410–500).
2229. [baja] Mobiliario — fuente de hierro
   - Captura: Fuente/bomba de hierro fundido (x≈175–225, y≈390–465).
   - Juego: No existe.
2230. [baja] Mobiliario — bolardos
   - Captura: Bolardos en la plaza (x≈395–410, y≈545–580; x≈520–530, y≈500–525).
   - Juego: Sin bolardos.
2231. [baja] Otros — escalones de la entrada del mercado
   - Captura: Escalinata de acceso (x≈975–1050, y≈410–460).
   - Juego: Sin escalones.
**Vista #225** — 03_Fachada_del_mercado.jpg (abril de 2009) · hoja a_225.jpg

2232. [media] Huecos — planta baja del edificio junto al mercado
   - Captura: Puerta de aluminio blanca con recercado (x≈200–345, y≈340–535), paño con carteles y un solo bar con toldo pequeño y rótulo «Café Churrería Bar Amalia» (x≈690–860, y≈310–410).
   - Juego: Cuatro escaparates acristalados seguidos con toldos de rayas amarillas y blancas y una banda verde (x≈0–865, y≈305–530).
2233. [media] Huecos — fachada lateral del mercado (x≈865–1200)
   - Captura: Una sola planta alta con ventanas altas enrejadas (x≈945–1015, y≈245–305; x≈1170–1215, y≈245–335).
   - Juego: Dos filas de ventanas, una arriba (x≈900–950 y x≈1015–1060, y≈195–270) y otra abajo con rejas (y≈350–430).
2234. [media] Detalles de fachada — edificio de viviendas junto al mercado (x≈380–865)
   - Captura: Fachada blanca con pilastras y recercados color crema/ocre en balcones y ventanas.
   - Juego: Fachada beige lisa, sin pilastras ni recercados.
2235. [media] Detalles de fachada — molduras del mercado
   - Captura: Paramentos blancos con pilastras, cornisa y recercados ocres (x≈865–1440, y≈160–470).
   - Juego: Paramento beige liso sin pilastras ni cornisa ocre.
2236. [media] Detalles de fachada — portada del mercado
   - Captura: Entrada en arco con recercado ocre (x≈1275–1330, y≈245–370) bajo un remate con azulejos (x≈1240–1360, y≈125–195).
   - Juego: Portada clásica de piedra con frontón triangular, pilastras estriadas, montante en abanico y puerta verde (x≈1200–1440, y≈125–470).
2237. [media] Cubierta — remate del mercado
   - Captura: Pretil con cornisa ocre, sin teja visible (x≈865–1440, y≈160–200).
   - Juego: Alero de teja naranja (x≈1090–1440, y≈135–165).
2238. [media] Calzada — firme de la calle San Gregorio
   - Captura: Adoquinado de piedra gris oscuro (x≈880–1440, y≈520–693).
   - Juego: Asfalto gris liso (x≈0–1440, y≈500–693).
2239. [baja] Acera y bordillo — acera ante el mercado
   - Captura: Acera de adoquín gris oscuro (x≈880–1300, y≈450–580).
   - Juego: Acera blanca.
2240. [baja] Mobiliario — señal de dirección obligatoria
   - Captura: Señal azul redonda con flecha sobre poste (x≈75–160, y≈350–540).
   - Juego: Sin señal.
2241. [baja] Mobiliario — buzones
   - Captura: Buzón amarillo de Correos (x≈1055–1100, y≈390–470) y buzón negro (x≈900–920, y≈425–475).
   - Juego: Sin buzones.
2242. [baja] Otros — escalones de la entrada del mercado
   - Captura: Escalinata ante la entrada (x≈1250–1350, y≈395–460).
   - Juego: Sin escalones.
**Vista #226** — 04_Acceso_desde_Salsipuedes.jpg (abril de 2009) · hoja a_226.jpg

2243. [alta] Cámara — posición de la cámara
   - Captura: Cámara en el centro de la calle San Gregorio, estrecha y adoquinada; las fachadas de ambos lados se ven a distancia, con sus puertas, rótulos (Autoescuela Álvaro, x≈570–625) y balcones, y la calle fuga hacia x≈735.
   - Juego: Cámara pegada a la fachada izquierda: un escaparate y un pilar a menos de un metro ocupan toda la mitad izquierda (x≈0–700, y≈0–693) y la calzada queda desplazada a la derecha (x≈730–1440); la mitad izquierda no se puede comparar.
**Vista #227** — 05_Vista_general_desde_la_plaza.jpg (mayo de 2024) · hoja a_227.jpg

2244. [media] Huecos — planta baja de la casa cercana de la izquierda
   - Captura: Gran puerta de madera oscura con aldaba dorada (x≈0–190, y≈395–693) y ventana con reja (x≈500–575, y≈360–540).
   - Juego: Ventanal con reja de barrotes (x≈0–335, y≈355–693) en el lugar de la puerta y ventana con reja (x≈535–605, y≈350–475).
2245. [media] Huecos — planta alta de la casa cercana de la izquierda
   - Captura: Balcón con barandilla de forja (x≈490–605, y≈180–300).
   - Juego: Ventana con persiana blanca, sin balcón (x≈535–595, y≈105–245).
2246. [media] Huecos — planta baja de la casa de la derecha
   - Captura: Ventana grande con reja de forja (x≈1150–1375, y≈320–590) y portal; sin escaparates.
   - Juego: Escaparates acristalados corridos (x≈890–1440, y≈370–693).
2247. [media] Detalles de fachada — recercados de la casa cercana de la izquierda
   - Captura: Recercados anchos color salmón en puerta, ventana y balcón, y cornisa salmón (x≈0–630).
   - Juego: Recercados apenas marcados en un rosa muy claro.
2248. [media] Detalles de fachada — toldos de la casa de la derecha
   - Captura: Sin toldos.
   - Juego: Hilera de toldos de rayas amarillas y blancas (x≈885–1440, y≈340–470).
2249. [baja] Zócalo — zócalo de la casa cercana de la izquierda
   - Captura: Zócalo color salmón desconchado (x≈0–630, y≈480–693).
   - Juego: Zócalo color tostado/marrón claro (x≈0–630, y≈440–693).
2250. [baja] Zócalo — zócalo verde de la derecha
   - Captura: Zócalo pintado de verde (x≈975–1095, y≈400–540).
   - Juego: Sin zócalo verde.
2251. [baja] Cubierta — remate de la casa de la derecha
   - Captura: Cornisa de obra blanca sin teja visible (x≈945–1100, y≈0–200).
   - Juego: Alero de teja roja (x≈880–1190, y≈0–300).
2252. [baja] Otros — cables por las fachadas
   - Captura: Cables eléctricos y telefónicos por las fachadas y cruzando la calle (x≈0–1440, y≈180–340).
   - Juego: Sin cables.
**Vista #228** — 06_Vista_desde_el_lado_suroeste.jpg (mayo de 2024) · hoja a_228.jpg

2253. [alta] Geometría — casa cercana de la derecha (x≈1200–1440)
   - Captura: Fachada alta que sale por arriba de la imagen (remate de y≈85 a y≈0), con cochera blanca (x≈1290–1380, y≈300–500).
   - Juego: Casas de una planta con tejado de teja roja: remate en y≈200–300.
2254. [alta] Color de fachada — fachada del borde izquierdo
   - Captura: Fachada pintada de verde vivo (x≈0–285, y≈0–693).
   - Juego: Paramento blanco.
2255. [media] Color de fachada — planta baja de la oficina (x≈285–680)
   - Captura: Planta baja chapada de granito gris con un escaparate de carteles (x≈420–630, y≈290–660).
   - Juego: Revoco blanco con banda verde y cajones de persiana sobre escaparates (x≈0–940, y≈160–620).
2256. [media] Color de fachada — paño azul junto a la oficina
   - Captura: Tramo de planta baja pintado de azul (x≈675–800, y≈280–550).
   - Juego: Escaparate gris/blanco.
2257. [media] Huecos — planta alta de la izquierda
   - Captura: Balcones con barandilla de forja (x≈650–760, y≈75–230; x≈820–860, y≈200–280; x≈880–905, y≈245–300).
   - Juego: Ventanas sin balcón (x≈610–710, y≈0–190; x≈870–915) y una ventana enrejada (x≈800–835, y≈130–255).
2258. [media] Huecos — planta baja de la casa cercana de la derecha
   - Captura: Puerta de cochera blanca con recercado blanco (x≈1255–1420, y≈260–520) y zócalo gris (x≈1220–1440, y≈430–560).
   - Juego: Portal (x≈1250–1320, y≈335–455), toldo de rayas (x≈1320–1440, y≈355–415), puerta verde (x≈1400–1440, y≈410–520) y macetas.
2259. [media] Detalles de fachada — toldo en primer plano a la izquierda
   - Captura: Sin toldo.
   - Juego: Toldo grande de rayas rojas y blancas (x≈0–495, y≈335–693).
2260. [baja] Detalles de fachada — rótulo y aparato de aire de la oficina
   - Captura: Rótulo redondo azul «Pelayo» (x≈795–870, y≈290–345) y aparato de aire acondicionado (x≈675–770, y≈235–330).
   - Juego: Sin rótulo ni aparato.
2261. [baja] Vegetación — jardinera de la acera izquierda
   - Captura: Jardinera de madera con una planta tipo yuca (x≈775–860, y≈450–590).
   - Juego: Sin jardinera.

### Plaza Federico García Lorca

**Vista #229** — 03_Vista_desde_el_lado_oeste.jpg (mayo de 2024) · hoja a_229.jpg

2262. [media] Color de fachada — casa crema de la izquierda (segunda desde el borde)
   - Captura: Fachada crema/beige claro, x≈100–290, entre una casa blanca (x≈0–100) y otra blanca (x≈280–350).
   - Juego: Toda la hilera de la izquierda es de un gris blanquecino uniforme, x≈0–480; no hay fachada crema.
2263. [media] Huecos — balcones y rejas de las primeras casas de la izquierda
   - Captura: Barandillas de balcón y rejas de ventana negras: balcón x≈0–55 y x≈135–230 (planta alta), rejas x≈150–250 (planta baja).
   - Juego: Barandillas y rejas blancas: balcón x≈0–135, reja de planta baja x≈0–100, balcones x≈295–345.
2264. [media] Calzada — calzada del primer plano
   - Captura: Asfalto gris medio, x≈0–1440, y≈540–693.
   - Juego: Superficie gris muy clara, casi blanca, x≈0–1440, y≈500–693.
2265. [media] Acera y bordillo — acera de la esquina del jardín
   - Captura: Acera de adoquín rojizo-marrón en la esquina del jardín, x≈395–660, y≈390–560.
   - Juego: Acera de losas gris claro, x≈395–1440, y≈450–555.
2266. [media] Vegetación — seto perimetral del jardín (frente a la cámara)
   - Captura: Seto bajo recortado continuo a lo largo de todo el borde del jardín, plano medio x≈595–1440.
   - Juego: Solo hay un bloque alto y estrecho en la esquina (x≈585–625) y bloques sueltos a la derecha (x≈990–1440); entre x≈625 y 990 el borde queda abierto, sin seto.
2267. [media] Vegetación — arbolado del jardín
   - Captura: Árboles grandes de hoja caduca con copas densas e irregulares que se juntan y tapan casi todo el cielo de x≈470 a 1440 (hasta el borde superior), con coníferas oscuras a la derecha (x≈1150–1440).
   - Juego: Árboles redondos más pequeños y separados (x≈530–1080) con mucho cielo visible entre ellos, un pino alto de copa aparasolada (x≈770–1100) y un árbol a la derecha (x≈1050–1440); sin coníferas.
2268. [media] Mobiliario — contenedores de residuos en el borde de la plaza
   - Captura: Cuatro contenedores grandes en fila (verde, amarillo, azul y marrón) sobre la calzada, pegados al bordillo del jardín, primer plano centro-derecha x≈655–1145, y≈440–600.
   - Juego: No hay ningún contenedor en esa zona; se ve arena, un banco (x≈745–855) y el bordillo del jardín.
2269. [media] Otros — suelo del jardín
   - Captura: Tierra parda bajo los árboles, plano medio x≈600–1440.
   - Juego: Arena amarilla clara lisa en todo el jardín, x≈555–1440.
2270. [baja] Cubierta — placa solar en el tejado de la izquierda
   - Captura: Placa solar inclinada sobre el tejado, x≈320–380, y≈215–255.
   - Juego: Alero continuo de teja naranja sin ninguna placa solar.
2271. [baja] Marcas viales — línea en la calle de la izquierda
   - Captura: Calzada de la calle de la izquierda sin marcas visibles, x≈0–250, y≈470–560.
   - Juego: Línea discontinua oscura a lo largo de la calzada, x≈80–480, y≈465–500.
2272. [baja] Vegetación — arbustos de hoja roja dentro del jardín
   - Captura: Varios arbustos de hoja púrpura/roja detrás del seto: x≈620–670, 820–870, 975–1025, 1130–1220 y 1315–1380.
   - Juego: No hay ningún arbusto rojo; solo árboles verdes y arena.
2273. [baja] Vegetación — arbolitos en la acera de la esquina de la plaza
   - Captura: Dos árboles jóvenes de tronco fino en la acera junto a la calzada, x≈475–540 y x≈565–605, plano medio.
   - Juego: Ningún árbol en la esquina; solo la farola (x≈480–545) y el bloque de seto (x≈585–625).
2274. [baja] Mobiliario — señal de tráfico de la esquina
   - Captura: Señal redonda azul de glorieta sujeta al fuste de la farola de la esquina, x≈430–485, y≈305–360.
   - Juego: No hay ninguna señal en la esquina.
2275. [baja] Mobiliario — farola de la esquina
   - Captura: Farola de fuste gris claro con luminaria pequeña, x≈420–470, y≈240–540 (la que lleva la señal).
   - Juego: Farola de fuste negro con brazo y luminaria rectangular, x≈480–545, y≈230–430, sin señal.
2276. [baja] Mobiliario — banco en el borde del jardín
   - Captura: No hay banco en el borde del jardín; en x≈745–855 están el seto y los contenedores.
   - Juego: Banco de madera en primer plano del jardín, x≈745–855.
2277. [baja] Mobiliario — farola a la derecha del jardín
   - Captura: No hay farola en el borde derecho del jardín (x≈1140–1320 se ven seto y árboles).
   - Juego: Farola alta negra con brazo en el borde del jardín, x≈1145–1315, primer plano.
**Vista #230** — 04_Vista_desde_el_lado_sur.jpg (mayo de 2024) · hoja a_230.jpg

2278. [alta] Color de fachada — edificio del fondo a la derecha
   - Captura: Edificio de dos plantas de fachada rojiza/rosa intenso con recercados blancos, fondo derecha x≈1280–1440, y≈220–390.
   - Juego: En esa zona, casas de fachada gris blanquecina con balcones blancos, x≈1230–1440.
2279. [media] Geometría — extensión del jardín hacia la derecha
   - Captura: El jardín y su seto continúan hasta el borde derecho de la imagen (x≈545–1440; el seto llega a x≈1440 en y≈520).
   - Juego: El seto termina en x≈1360 y a su derecha, en primer plano, aparece una calle con un coche aparcado (x≈1195–1440, y≈370–425) y una hilera de casas (x≈950–1440).
2280. [media] Color de fachada — casas del fondo a la izquierda
   - Captura: Casas de dos plantas de fachada salmón/rosada con recercados blancos, x≈0–330, y≈255–395.
   - Juego: Casas de fachada gris claro/crema, x≈0–560, y≈260–390.
2281. [media] Calzada — calzada de la izquierda
   - Captura: Asfalto gris medio, x≈0–260, y≈400–560.
   - Juego: Superficie gris muy clara, casi blanca, x≈0–420, y≈400–690.
2282. [media] Acera y bordillo — acera entre el seto y el bordillo
   - Captura: Acera de adoquín/baldosa rojizo-marrón, x≈540–1440, y≈480–600.
   - Juego: Acera de losas gris muy claro, x≈410–1440, y≈410–560.
2283. [media] Vegetación — arbolado del jardín
   - Captura: Árboles altos de copa densa e irregular formando una masa continua de x≈230 a 1440, con una conífera oscura a la derecha (x≈1030–1300, y≈300–430).
   - Juego: Árboles de tronco moteado (tipo plátano) con copas redondas separadas (x≈210–1440) y otros redondos pequeños al fondo; ninguna conífera.
2284. [media] Mobiliario — farola del borde oeste del jardín
   - Captura: Farola de fuste gris con cabeza redonda tipo seta, x≈420–465, y≈235–430, con una placa pequeña en el fuste.
   - Juego: Farola de fuste negro con brazo horizontal y luminaria plana, x≈180–280.
2285. [media] Vehículos — aparcamiento junto a la plaza (izquierda)
   - Captura: Coches aparcados en línea, paralelos al bordillo del jardín: todoterreno x≈225–540 y turismo blanco en primer plano x≈680–1300.
   - Juego: Coches aparcados en batería (perpendiculares), con la trasera hacia la cámara: rojo, azul y pickup blanca x≈55–510, y otra pickup en primer plano x≈380–1440.
2286. [media] Otros — suelo del jardín
   - Captura: Tierra parda bajo los árboles, x≈650–1440, y≈370–470.
   - Juego: Arena amarilla clara, x≈420–1440, y≈360–510.
2287. [baja] Vegetación — arbustos de hoja roja
   - Captura: Arbustos púrpura/rojos en el jardín: x≈240–420 (borde oeste), 615–655, 760–800, 925–1000 y 1240–1340.
   - Juego: Ningún arbusto rojo.
2288. [baja] Vegetación — arbolito en la esquina oeste del jardín
   - Captura: Árbol joven podado en la esquina del jardín, x≈180–215, y≈320–410.
   - Juego: No hay árbol en esa posición.
2289. [baja] Otros — toldo en las casas de la izquierda
   - Captura: No se ve ningún toldo en las fachadas de la izquierda (x≈0–100).
   - Juego: Toldo de rayas verdes y blancas en la planta alta, x≈20–75, y≈290–305.
**Vista #231** — 05_Vista_desde_el_lado_este.jpg (mayo de 2024) · hoja a_231.jpg

2290. [media] Color de fachada — hilera de casas de la derecha (primera casa)
   - Captura: Fachada salmón/melocotón con pilastras y recercados de un salmón más oscuro, x≈1100–1440.
   - Juego: Fachada beige arena uniforme, x≈1100–1440.
2291. [media] Huecos — rejas y barandilla de la primera casa de la derecha
   - Captura: Balcón con barandilla negra (x≈1185–1305, y≈265–320) y rejas negras en las ventanas bajas (x≈1155–1285, y≈350–400).
   - Juego: Barandilla de balcón blanca (x≈1055–1125, y≈290–330) y rejas blancas (x≈1070–1120, y≈345–400).
2292. [media] Zócalo — primera casa de la derecha
   - Captura: La fachada salmón llega casi hasta la acera; solo en el extremo derecho hay un zócalo de piedra gris oscura, x≈1390–1440, y≈410–470.
   - Juego: Banda continua de zócalo marrón oscuro de x≈880 a 1440, y≈380–490.
2293. [media] Calzada — calzada de la calle de la derecha
   - Captura: Asfalto gris medio, x≈980–1440, y≈470–693.
   - Juego: Superficie gris muy clara, casi blanca, x≈900–1440, y≈400–693.
2294. [media] Acera y bordillo — acera de la esquina del jardín
   - Captura: Acera ancha de adoquín rojizo-marrón en la esquina, x≈680–980, y≈470–560.
   - Juego: No hay acera de adoquín: el seto (x≈0–920) está separado de la calzada solo por una franja estrecha de bordillo blanco (y≈500–520).
2295. [media] Mobiliario — zona de juegos infantiles del jardín
   - Captura: Tobogán rojo (x≈400–470, y≈355–410) y estructura de columpios (x≈560–650, y≈345–395) dentro del jardín.
   - Juego: No hay juegos infantiles; arena con árboles, un banco (x≈645–675) y una papelera (x≈540–550).
2296. [media] Mobiliario — farola de la esquina del jardín
   - Captura: Farola de fuste gris con cabeza redonda tipo seta, x≈520–565, y≈195–430, con una señal de prohibición sujeta al fuste (x≈540–560).
   - Juego: Farola de fuste negro con luminaria rectangular, x≈610–660, y≈95–440, sin señal.
2297. [media] Otros — suelo del jardín
   - Captura: Tierra/albero pardo claro bajo los árboles, x≈0–700, y≈390–440.
   - Juego: Arena amarilla clara, x≈30–790, y≈360–430.
2298. [baja] Huecos — contraventanas de la primera casa de la derecha
   - Captura: Ventana alta con persiana enrollable blanca (x≈1215–1285, y≈220–275); no hay contraventanas laterales.
   - Juego: Contraventanas de madera marrón a los lados de las ventanas altas, x≈1180–1205 y x≈1280–1330, y≈195–285.
2299. [baja] Cubierta — chimenea de la primera casa de la derecha
   - Captura: Chimenea sobre el tejado, x≈1150–1175, y≈185–215.
   - Juego: Alero de teja naranja continuo sin chimenea.
2300. [baja] Cubierta — placa solar en el tejado de la derecha
   - Captura: Placa solar sobre el tejado, x≈1035–1110, y≈200–255.
   - Juego: Ninguna placa solar en el tejado.
2301. [baja] Marcas viales — línea en la calzada
   - Captura: Calzada sin líneas visibles, x≈980–1440.
   - Juego: Línea oscura longitudinal en la calzada, x≈930–1210, y≈420–520.
2302. [baja] Vegetación — arbustos recortados en bola al fondo del jardín
   - Captura: Arbustos podados en forma de bola, x≈0–120 y x≈350–500, y≈350–390.
   - Juego: No hay arbustos en bola; solo árboles y arena.
2303. [baja] Vegetación — arbusto cónico de la esquina del jardín
   - Captura: Arbusto recortado alto, de forma cónica/ovoide, en la esquina del jardín junto a la calle, x≈705–790, y≈355–460.
   - Juego: En esa esquina solo hay los bloques bajos del seto (x≈640–920, y≈425–505).
2304. [baja] Vegetación — arbolito en la acera izquierda de la calle
   - Captura: Árbol joven en la acera, delante de los coches aparcados, x≈860–905, y≈330–420.
   - Juego: No hay árbol en esa acera.
2305. [baja] Mobiliario — farola en la acera de las casas (derecha)
   - Captura: No hay farola en la acera de la derecha (x≈1100–1200 es fachada).
   - Juego: Farola negra con brazo en la acera de la derecha, x≈1110–1190, y≈220–445.
2306. [baja] Mobiliario — señal en la esquina del jardín
   - Captura: Poste con señal en el borde de la acera de la esquina, x≈955–975, y≈325–510.
   - Juego: No hay ninguna señal en la esquina.

### Plaza Ramón y Cajal

**Vista #232** — 02_Acceso_norte_a_la_plaza.jpg (octubre de 2021) · hoja a_232.jpg

2307. [alta] Muros y vallas — cerramiento delantero de la casa de la derecha
   - Captura: Muro bajo de color terracota/salmón con barandilla negra encima y pilares, que cierra un patio delante de la casa, x≈905–1100 y x≈1235–1380, y≈355–415, con una cancela negra (x≈1030–1060).
   - Juego: No hay muro ni patio: la fachada de la casa da directamente a la acera, x≈905–1440.
2308. [media] Huecos — balcones de la planta alta de la casa de la derecha
   - Captura: Tres balcones con barandilla negra en la planta alta: x≈955–990, x≈1120–1175 y x≈1240–1345 (este con toldo y plantas).
   - Juego: Un solo balcón pequeño con barandilla negra, x≈1005–1060, y≈300–330.
2309. [media] Huecos — contraventanas de la casa de la derecha
   - Captura: Ventanas sin contraventanas de madera, con recercado salmón.
   - Juego: Contraventanas de madera marrón a ambos lados de las ventanas altas, x≈925–978 y x≈1098–1200, y≈255–305.
2310. [media] Huecos — cochera de la casa de la derecha
   - Captura: Puerta de cochera ancha de color oscuro (casi negro) en el centro, x≈1100–1210, y≈350–410.
   - Juego: Puerta de cochera de madera marrón en el extremo izquierdo de la casa, x≈920–980, y≈345–398; en el centro hay una puerta de rayas doradas (x≈1115–1175).
2311. [media] Detalles de fachada — recercados y bandas de la casa de la derecha
   - Captura: Fachada blanca/crema con recercados de ventanas, pilastras e imposta entre plantas de color salmón/terracota, x≈915–1440, y≈250–400.
   - Juego: Fachada beige con textura de piedra, sin recercados ni bandas de color; solo marcos blancos en las ventanas.
2312. [media] Calzada — calzada de la plaza
   - Captura: Asfalto gris medio con sombras de árboles, x≈700–1440, y≈400–693.
   - Juego: Superficie gris muy clara, casi blanca, x≈450–1440, y≈380–693.
2313. [media] Marcas viales — marcas en la calzada
   - Captura: Solo trazos blancos cortos discontinuos en el lado derecho (x≈1100–1390, y≈420–580) y una marca blanca en el borde inferior izquierdo (x≈200–330, y≈645–693); sin isleta cebreada ni líneas continuas.
   - Juego: Isleta de cebreado blanco en forma de V (x≈760–945, y≈460–690) y líneas blancas continuas largas (x≈600–1440).
2314. [media] Acera y bordillo — borde de la plaza junto a la calzada (izquierda)
   - Captura: El bordillo de hormigón de la plaza da directamente a un parterre de tierra con árboles; no hay acera a lo largo de la calzada, x≈250–680, y≈460–650.
   - Juego: Acera ancha de losas gris claro con una banda de ladrillo rojo junto al bordillo, x≈0–740, y≈390–693.
2315. [media] Acera y bordillo — acera de la casa de la derecha
   - Captura: Acera estrecha gris delante del muro de la casa, x≈1000–1440, y≈405–440.
   - Juego: Acera ancha de ladrillo rojo, x≈680–1440, y≈380–560.
2316. [media] Vegetación — setos en el borde de la plaza
   - Captura: No hay seto recortado en el borde de la plaza; solo matas bajas sueltas al fondo (x≈0–150 y x≈200–280, y≈385–420).
   - Juego: Hilera de bloques de seto grandes a lo largo del borde, x≈0–535, y≈365–600.
2317. [media] Vegetación — árboles junto a la calzada
   - Captura: Dos árboles altos junto al bordillo de la plaza: tronco en x≈450–475 con copa x≈330–650 y otro con copa x≈600–830, y≈140–410, que llegan hasta arriba de la imagen.
   - Juego: Entre x≈505 y 830 no hay ningún árbol (cielo abierto); los árboles del juego están a la izquierda (x≈0–505) y son más bajos.
2318. [media] Otros — interior de la plaza (izquierda)
   - Captura: Parterres de tierra parda con árboles, caminos de hormigón gris con bancos (x≈150–230 y x≈395–440) y bordillos, x≈0–680.
   - Juego: Arena amarilla clara lisa, x≈0–530, y≈360–600.
2319. [baja] Detalles de fachada — toldo de la casa de la derecha
   - Captura: Toldo grande amarillo/ocre sobre el balcón de la derecha, x≈1240–1345, y≈240–290.
   - Juego: Toldo pequeño de rayas rojas y blancas sobre el balcón de la izquierda, x≈1005–1060, y≈268–288; no hay toldo amarillo.
2320. [baja] Vegetación — palmera del fondo
   - Captura: No se ve ninguna palmera; en x≈765–840 hay copa de árbol de hoja ancha y casas.
   - Juego: Palmera en el fondo, x≈765–840, y≈285–385.
2321. [baja] Mobiliario — farola de la acera derecha
   - Captura: Farola alta de fuste gris en la acera derecha, x≈1325–1370, y≈100–420.
   - Juego: No hay farola en la acera derecha.
2322. [baja] Mobiliario — farola en la esquina de la plaza
   - Captura: En la esquina de la plaza (x≈555–600) no hay farola; solo troncos de árbol.
   - Juego: Farola negra con brazo en la esquina de la plaza, x≈555–600, y≈270–400.
**Vista #233** — 03_Lado_oeste.jpg (octubre de 2021) · hoja a_233.jpg

2323. [alta] Geometría — casa beige a la derecha de la casa roja
   - Captura: En x≈1050–1290 hay una valla de muro bajo blanco con barandilla negra y pilares blancos (y≈340–420) y, detrás, el edificio de ladrillo visto; no hay ninguna casa beige.
   - Juego: Casa beige de dos plantas con puerta y ventanas, x≈1085–1245, y≈218–415.
2324. [alta] Muros y vallas — jardín delantero de la casa roja de la esquina
   - Captura: Muro bajo blanco con barandilla negra encima y pilares blancos que rodea un jardín con plantas delante de las dos fachadas de la casa roja, x≈730–1000, y≈345–435, con cancela negra x≈1000–1050.
   - Juego: No hay muro ni jardín: la casa roja da directamente a la acera, x≈720–1090, y≈400–430.
2325. [media] Huecos — planta alta de la casa roja (fachada principal)
   - Captura: Tres ventanas con balcón de barandilla negra y recercado blanco: x≈855–905, 945–995 y 1030–1080.
   - Juego: Solo dos balcones (x≈920–985 y x≈1020–1080); la primera ventana (x≈815–860) es una ventana sin balcón con persiana blanca.
2326. [media] Huecos — planta baja de la casa roja (fachada principal)
   - Captura: Ventana con reja negra (x≈855–900), puerta en el centro entre plantas (x≈935–960) y ventana con reja negra (x≈1030–1070).
   - Juego: Puerta gris (x≈815–860), ventana con reja (x≈920–965) y otra puerta gris (x≈1020–1060): puertas donde la captura tiene ventanas.
2327. [media] Huecos — edificio de ladrillo visto de la derecha
   - Captura: Edificio de dos plantas de ladrillo visto con huecos vacíos sin carpintería ni marcos (x≈1250–1290, 1320–1360, 1365–1395), x≈1100–1440.
   - Juego: Fachada naranja-rojiza enfoscada con ventanas de marco blanco y persianas blancas, x≈1245–1440.
2328. [media] Detalles de fachada — imposta y cornisa de la casa roja de la esquina
   - Captura: Banda blanca horizontal entre plantas (y≈285–295) y cornisa blanca bajo el alero (y≈185–200), x≈730–1120, más recercados blancos.
   - Juego: Fachada roja lisa sin bandas ni cornisa blancas; solo marcos blancos en las ventanas.
2329. [media] Cubierta — tejado de la casa roja de la esquina
   - Captura: No se ve tejado: el remate es una cornisa blanca recta, x≈780–1120, y≈180–200.
   - Juego: Tejado a cuatro aguas de teja naranja con alero visible, x≈720–1100, y≈208–240.
2330. [media] Calzada — calzada del cruce
   - Captura: Asfalto gris medio, x≈0–1440, y≈430–693.
   - Juego: Superficie gris muy clara, casi blanca, x≈0–1440, y≈430–693.
2331. [media] Acera y bordillo — acera del lado de la plaza
   - Captura: Acera gris de hormigón, x≈0–460, y≈400–520.
   - Juego: Banda de ladrillo rojo a lo largo de la acera, x≈230–540, y≈380–465.
2332. [media] Vegetación — seto del borde de la plaza (izquierda)
   - Captura: Borde de la plaza sin seto recortado: jardinera baja de piedra con arbolitos (x≈300–460, y≈380–405) y árboles grandes.
   - Juego: Hilera continua de bloques de seto a lo largo del borde de la plaza, x≈0–540, y≈360–480.
2333. [media] Vehículos — aparcamiento en batería junto a la plaza
   - Captura: Fila de coches aparcados en batería a lo largo de la plaza (x≈430–600, y≈350–390) y más coches a la izquierda (x≈80–320).
   - Juego: Solo un coche (x≈545–590) y un patinete; no hay fila de coches en batería.
2334. [baja] Mobiliario — señales en la esquina
   - Captura: En la esquina (x≈672–692) no hay señales; solo la farola (x≈708–728).
   - Juego: Señal cuadrada azul de paso de peatones y señal redonda de prohibido aparcar sobre poste, x≈672–692, y≈318–355.
2335. [baja] Mobiliario — farolas
   - Captura: Farolas de fuste gris claro, muy altas y finas, x≈708–728 (y≈140–430) y x≈1130–1160 (y≈120–395).
   - Juego: Farolas de fuste negro con brazo, más bajas, x≈630–690 (y≈240–430) y x≈1200–1290 (y≈240–420).
**Vista #234** — 04_Lado_sur_y_centro_de_salud.jpg (mayo de 2024) · hoja a_234.jpg

2336. [alta] Geometría — centro de salud (edificio de la izquierda)
   - Captura: Edificio público de cubierta plana: cuerpo delantero oscuro revestido de barrotes/lamas verticales negros (x≈60–340) y cuerpo de fachada crema lisa con pocas ventanas pequeñas (x≈340–590).
   - Juego: Hilera de casas de dos plantas con tejado de teja, ventanas grandes con contraventanas de madera y bajos comerciales con toldos, x≈0–570.
2337. [alta] Geometría — edificio del fondo, centro-izquierda
   - Captura: Muros blancos bajos y construcciones blancas de una planta, x≈590–780, y≈330–385, con una cancela oscura (x≈735–775).
   - Juego: Edificio granate de tres plantas con balcones, x≈605–765, y≈265–385.
2338. [media] Huecos — planta alta del centro de salud
   - Captura: Pocas ventanas pequeñas y separadas de marco oscuro: x≈445–465, 505–515, 540–550 (y≈240–290).
   - Juego: Ventanas grandes con contraventanas de madera marrón muy seguidas: x≈0–90, 175–330, 360–420, 445–480, 490–520 (y≈90–300).
2339. [media] Huecos — planta baja del centro de salud
   - Captura: Barrotes verticales negros de suelo a techo en el cuerpo delantero (x≈60–340, y≈330–550) y, más allá, puertas con reja (x≈440–470 y x≈500–515).
   - Juego: Bajos comerciales con cierres enrollables grises continuos, x≈0–570, y≈320–550.
2340. [media] Detalles de fachada — toldos de rayas
   - Captura: No hay ningún toldo en la fachada de la izquierda.
   - Juego: Toldos de rayas verdes y blancas sobre los bajos, x≈0–390 y x≈520–570, y≈340–410.
2341. [media] Cubierta — cubierta del centro de salud
   - Captura: Cubierta plana con peto recto, sin teja visible, borde superior de x≈330 (y≈170) a x≈590 (y≈300).
   - Juego: Tejado de teja naranja con alero a lo largo de todo el edificio, x≈0–570, y≈10–300.
2342. [media] Calzada — calzada de la calle
   - Captura: Asfalto gris medio, x≈250–1000, y≈380–693.
   - Juego: Superficie gris muy clara, casi blanca, x≈150–1000, y≈400–693.
2343. [media] Marcas viales — marcas en la calzada
   - Captura: Líneas blancas de plazas de aparcamiento junto a la acera izquierda (x≈440–600, y≈390–460) y una marca blanca en ángulo abajo a la izquierda (x≈240–400, y≈565–640); sin líneas longitudinales.
   - Juego: Dos líneas blancas continuas longitudinales (x≈230–590, y≈420–693 y x≈695–750, y≈430–693) y una línea discontinua (x≈170–540, y≈590–610).
2344. [media] Vegetación — seto en el borde del jardín (derecha)
   - Captura: El jardín no tiene seto recortado: bordillo de hormigón con tierra y arbustos sueltos detrás, x≈880–1200.
   - Juego: Hilera de bloques de seto a lo largo del borde, x≈1040–1440, y≈365–465.
2345. [media] Otros — suelo del jardín (derecha)
   - Captura: Tierra parda, x≈890–1440, y≈420–650.
   - Juego: Arena amarilla clara, x≈1000–1440, y≈380–693.
2346. [baja] Detalles de fachada — rótulo del centro de salud
   - Captura: Rótulo blanco y verde «Centro de Salud Guareña» sobre la entrada, x≈80–335, y≈280–335.
   - Juego: No hay rótulo.
2347. [baja] Detalles de fachada — bandera en la fachada
   - Captura: Bandera de España en mástil inclinado sobre la fachada, x≈320–400, y≈95–215.
   - Juego: No hay bandera.
2348. [baja] Cubierta — placas solares de las casas del fondo
   - Captura: Placas solares sobre los tejados de la casa crema (x≈760–790, y≈270–290) y de la casa granate (x≈860–885, y≈275–295).
   - Juego: Tejados de teja sin placas solares.
2349. [baja] Vegetación — arbustos del jardín (derecha)
   - Captura: Arbustos de hoja roja/púrpura (x≈890–990, 1100–1240, 1240–1340), rosales (x≈1020–1100) y una mata redonda verde (x≈975–1055, y≈450–515).
   - Juego: No hay arbustos; arena y seto.
2350. [baja] Mobiliario — señal de aparcamiento de minusválidos
   - Captura: Señal azul con el símbolo de silla de ruedas en primer plano izquierda, x≈0–70, y≈320–390.
   - Juego: No hay señal.

### Avenida de la Constitución

**Vista #235** — 02_Tramo_oeste.jpg (mayo de 2024) · hoja a_235.jpg

2351. [alta] Geometría — posición de la calzada y explanada de la derecha
   - Captura: La cámara está en medio de la calzada (asfalto de x≈250 a 1050 en el borde inferior); a la derecha, una acera de baldosa gris de unos 3 m (x≈740–1300) y después un terreno con hierba.
   - Juego: La calzada queda a la izquierda (de x≈0 a 400 en el borde inferior) y toda la mitad derecha del primer plano es una gran explanada de losas blancas, x≈400–1440, y≈380–693.
2352. [alta] Color de fachada — edificio del fondo en el centro
   - Captura: Tapias y construcciones blancas/grises de cubierta plana (x≈700–815, y≈330–370) y una caseta blanca (x≈815–940, y≈310–400).
   - Juego: Casa de fachada de ladrillo rojo con tejado de teja naranja a cuatro aguas, x≈740–840, y≈320–368.
2353. [alta] Vegetación — arbolado del lado derecho
   - Captura: Fila de árboles junto a la acera derecha: palmera alta (x≈905–1060, y≈0–420), plátano de tronco blanco (x≈1050–1380, y≈80–510) y árbol desmochado (x≈850–900, y≈235–420).
   - Juego: Ningún árbol en el lado derecho cercano; solo la explanada blanca vacía.
2354. [alta] Muros y vallas — muro de piedra de la izquierda
   - Captura: Muro largo de mampostería gris a lo largo del lado izquierdo, x≈0–480, y≈345–445.
   - Juego: No hay muro: suelo blanco con matas y un coche amarillo (x≈0–60).
2355. [media] Acera y bordillo — paseo de la izquierda de la calzada
   - Captura: Paseo de ladrillo/adoquín rojizo con bordillos, x≈150–640, y≈370–693, con franja de césped (x≈170–400, y≈480–560).
   - Juego: Franja de suelo blanco con matas redondas, x≈0–560, y≈360–520; no hay paseo rojizo.
2356. [media] Vegetación — árboles del paseo de la izquierda
   - Captura: Plátanos desmochados de tronco grueso junto a la calzada (x≈480–560, 555–600 y 630–650) y un arbolito (x≈250–390, y≈370–495).
   - Juego: Matas redondas bajas con flores rosas (x≈30–270, y≈360–480) y matorrales al fondo; ningún árbol desmochado junto a la calzada.
2357. [media] Mobiliario — farolas del paseo de la izquierda
   - Captura: Farolas de fuste gris claro muy altas con brazo curvo de una luminaria: x≈410–440 (llega al borde superior), x≈430–525 (y≈135–415) y x≈600–645 (y≈235–380).
   - Juego: Farolas de fuste negro con brazo recto, una de ellas de dos brazos: x≈70–180, x≈350–445 y x≈555–630.
2358. [media] Otros — terreno con hierba del lado derecho
   - Captura: Franja de hierba y matorral seco entre la acera y un camino paralelo, x≈800–1440, y≈390–640.
   - Juego: Losas blancas; no hay hierba.
2359. [baja] Calzada — línea oscura en la calzada
   - Captura: Calzada sin marcas ni grietas largas, x≈250–1050.
   - Juego: Línea oscura larga en diagonal sobre el asfalto, x≈320–580, y≈410–560.
2360. [baja] Mobiliario — banco del paseo
   - Captura: Banco junto al paseo, x≈420–480, y≈400–450.
   - Juego: No hay banco.
**Vista #236** — 03_Curva_junto_a_Hornillos.jpg (octubre de 2021) · hoja a_236.jpg

2361. [alta] Cámara — encuadre de la vista
   - Captura: Cámara en medio de la calzada (asfalto de x≈480 a 1300 en el borde inferior); a la derecha, a varios metros, un muro/nave larga blanca con zócalo ocre y cubierta de chapa ondulada (x≈800–1440), con una acera de baldosa delante; a la izquierda, acera rojiza con árboles, papelera, coche rojo y edificios blancos.
   - Juego: Cámara sobre la acera derecha pegada a una fachada blanca con alero de teja naranja que ocupa x≈730–1440 de arriba abajo, con un farol de pared (x≈785–1030) y una puerta con cortina de rayas (x≈905–1055) a un metro; la calzada queda a la izquierda (x≈0–720).
**Vista #237** — 04_Rotonda_del_camino_de_Zarza.jpg (mayo de 2024) · hoja a_237.jpg

2362. [alta] Cámara — encuadre de la vista
   - Captura: Cámara en la calzada junto a una nave blanca a 2–3 m que ocupa x≈0–700 de arriba abajo (celosía de bloques x≈370–515, portón gris x≈620–675); la calzada sigue en curva hacia la derecha; a la derecha, acera rojiza con árboles desmochados y edificios blancos de una planta.
   - Juego: Cámara en medio de una gran explanada circular de losas blancas (x≈0–1440, y≈420–693); ningún edificio cerca: casa de dos plantas con un paño de madera y un gran ventanal (x≈0–405), hilera de casas de una planta con teja (x≈405–700) y una nave gris larga (x≈880–1440), todas a más de 20 m.
**Vista #238** — 05_Rotonda_del_Arroyo.jpg (mayo de 2024) · hoja a_238.jpg

2363. [alta] Cámara — encuadre de la vista
   - Captura: Cámara sobre una acera de baldosa junto a un muro curvo de piedra con pilares (x≈530–1440, y≈365–540) que cierra un parque de tierra con palmeras, árboles y columpios, a pocos metros; la calzada queda a la izquierda.
   - Juego: Cámara sobre un césped verde con un camino blanco (x≈0–1440, y≈420–693); la calzada cruza por delante (y≈380–470) y el parque con árboles y setos está al otro lado, a unos 40 m (x≈770–1370, y≈215–390); no hay muro de piedra.
**Vista #239** — 06_Tramo_sur.jpg (mayo de 2024) · hoja a_239.jpg

2364. [media] Huecos — planta alta de la primera casa de la izquierda
   - Captura: Balcón con barandilla negra en la planta alta, x≈40–95, y≈280–300.
   - Juego: Ventana con contraventanas verdes y macetas, sin balcón, x≈0–145, y≈240–300.
2365. [media] Huecos — portón del edificio de la derecha
   - Captura: Portón grande negro de dos hojas, x≈985–1075, y≈280–430.
   - Juego: No hay portón: pared blanca con una puerta pequeña (x≈1015–1040, y≈355–435).
2366. [media] Zócalo — segunda casa de la izquierda
   - Captura: Zócalo de ladrillo rojo visto, x≈135–290, y≈380–420.
   - Juego: Zócalo gris liso, x≈0–380, y≈390–435.
2367. [media] Zócalo — edificios de la derecha
   - Captura: Banda de zócalo ocre/amarilla continua a lo largo de toda la fachada, x≈870–1440, y≈380–450.
   - Juego: Zócalo gris en x≈1040–1265 y ocre solo en x≈1265–1440.
2368. [media] Cubierta — primera casa de la izquierda
   - Captura: Remate plano con peto blanco, sin teja visible, x≈0–135, y≈200–215.
   - Juego: Tejado de teja naranja con alero y una chimenea, x≈0–170, y≈160–235.
2369. [media] Cubierta — edificios de la derecha
   - Captura: Remate recto con peto y cornisa, sin teja visible, x≈950–1440, y≈235–290.
   - Juego: Tejados de teja naranja con alero en toda la hilera, x≈860–1440, y≈260–335.
2370. [media] Acera y bordillo — carril rojizo del bulevar (izquierda de la calzada)
   - Captura: Carril de pavimento rojizo/rosado a lo largo del bordillo izquierdo de la calzada, x≈230–690, y≈360–693.
   - Juego: Losas blancas continuas en todo el bulevar, x≈0–690; no hay carril rojizo.
2371. [media] Vegetación — árboles del bulevar
   - Captura: Plátanos desmochados de tronco grueso: x≈280–500 (y≈195–500) y x≈585–650 (y≈290–400).
   - Juego: Un árbol redondo con naranjas (x≈315–495, y≈315–450) y una palmera (x≈500–635, y≈215–395).
2372. [media] Vegetación — árboles y rosales de la acera derecha
   - Captura: Árboles en la acera derecha (x≈1165–1310, y≈230–500; naranjo x≈810–950, y≈285–400) y rosales junto a la fachada (x≈990–1050 y x≈1100–1440).
   - Juego: Acera derecha sin árboles ni rosales; solo una maceta pequeña (x≈950–965).
2373. [media] Mobiliario — farolas del bulevar
   - Captura: Farolas de fuste gris claro con un solo brazo curvo: x≈505–560 (y≈140–400) y x≈660–690.
   - Juego: Farola de fuste negro de dos brazos en primer plano, x≈205–440 (y≈0–475), y otras negras en x≈575–600 y x≈650–680.
2374. [media] Otros — franja terriza del bulevar
   - Captura: Franja de tierra parda con alcorques entre el carril rojizo y la calle paralela, x≈0–520, y≈400–693.
   - Juego: Losas blancas; no hay tierra.
2375. [baja] Huecos — puerta de la segunda casa de la izquierda
   - Captura: Puerta blanca, x≈235–265, y≈350–400.
   - Juego: Puerta doble de madera clara, x≈212–260, y≈350–402.
2376. [baja] Cubierta — placa solar a la derecha
   - Captura: No se ve ninguna placa solar sobre los edificios de la derecha.
   - Juego: Placa solar sobre el tejado, x≈1110–1260, y≈250–275.
2377. [baja] Acera y bordillo — acera de la derecha
   - Captura: Baldosa gris, x≈760–1250, y≈380–600.
   - Juego: Losas blancas, x≈740–1440.
2378. [baja] Vegetación — rosales del bulevar
   - Captura: Rosales con flores rojas en primer plano izquierda, x≈0–150, y≈490–600.
   - Juego: No hay rosales.
2379. [baja] Vegetación — palmera detrás de las casas de la derecha
   - Captura: No hay palmera sobre las casas de la derecha (cielo, antena y cables).
   - Juego: Palmera asomando sobre los tejados, x≈1235–1370, y≈170–270.
2380. [baja] Mobiliario — señal de peligro de la acera derecha
   - Captura: Señal triangular de resalto sobre poste, x≈1075–1130, y≈300–570.
   - Juego: No hay señal.
2381. [baja] Otros — antena de televisión
   - Captura: Mástil alto de antena sobre el edificio de la derecha, x≈1090–1155, y≈55–240.
   - Juego: No hay antena.
**Vista #240** — 07_Sentido_contrario_hacia_las_rotondas.jpg (mayo de 2024) · hoja a_240.jpg

2382. [alta] Geometría — edificio del primer plano izquierdo
   - Captura: Edificaciones blancas de una planta retranqueadas tras una acera ancha, con un portón grande marrón oscuro (x≈0–155, y≈345–500) y puertas marrones (x≈300–330, x≈430–460), x≈0–640, y≈280–500.
   - Juego: Casa de dos plantas con tejado de teja pegada a la cámara, que ocupa x≈0–420 desde el borde superior hasta y≈590 (ventana con persiana x≈90–210, balcón x≈320–410).
2383. [media] Huecos — edificio blanco del extremo derecho
   - Captura: Fachada blanca ciega, sin huecos, con zócalo gris, x≈1290–1440, y≈265–440.
   - Juego: Fachada con balcón de barandilla blanca (x≈1215–1280), contraventanas de madera (x≈1320–1435), puerta de madera (x≈1235–1270) y ventana con reja (x≈1340–1405).
2384. [media] Cubierta — edificio blanco del extremo derecho
   - Captura: Remate recto con peto, sin teja visible, x≈1290–1440, y≈265–280.
   - Juego: Tejado de teja naranja con alero, x≈1195–1440, y≈215–265.
2385. [media] Acera y bordillo — carril rojizo del bulevar (derecha de la calzada)
   - Captura: Carril de pavimento rojizo a lo largo del bordillo derecho, x≈700–1100, y≈370–693.
   - Juego: Losas blancas en todo el bulevar, x≈690–1440.
2386. [media] Vegetación — arbolitos y césped de la acera izquierda
   - Captura: Alcorques con arbolitos (x≈455–515, 535–575, 575–605, y≈290–410) y una franja de césped (x≈0–240, y≈520–580).
   - Juego: Acera de losas blancas sin árboles ni césped.
2387. [media] Vegetación — arbustos del bulevar
   - Captura: Arbustos sueltos sobre tierra: arbusto púrpura (x≈825–890, y≈340–440) y mata verde (x≈1055–1170, y≈410–550).
   - Juego: Árboles redondos con naranjas, x≈775–900 y x≈975–1160 (y≈315–450), sobre losas blancas.
2388. [media] Mobiliario — farola del bulevar
   - Captura: Farola de fuste gris claro muy alta (llega al borde superior), x≈850–870, y≈0–470.
   - Juego: Farola negra de dos brazos más baja, x≈815–855, y≈250–390.
2389. [baja] Calzada — estado de la calzada
   - Captura: Asfalto gris claro muy agrietado, x≈200–900, y≈380–693.
   - Juego: Asfalto gris liso sin grietas.
2390. [baja] Vegetación — palmera del bulevar
   - Captura: Palmera lejana y pequeña, x≈710–815, y≈260–390.
   - Juego: Palmera cercana y grande, x≈840–1120, y≈95–420.
2391. [baja] Mobiliario — banco del bulevar
   - Captura: Banco metálico en el bulevar, x≈880–1010, y≈445–560.
   - Juego: No hay banco en el bulevar.
2392. [baja] Mobiliario — señal en la calle paralela de la derecha
   - Captura: Señal sobre poste junto a la calle paralela, x≈1025–1040, y≈340–405.
   - Juego: No hay señal.
2393. [baja] Otros — antenas de televisión en los tejados de la izquierda
   - Captura: Dos mástiles de antena sobre los tejados de la izquierda, x≈95–115 y x≈210–250, y≈215–320.
   - Juego: No hay antenas.

### Calle de Don Diego López

**Vista #241** — 02_Desde_un_extremo_hacia_el_otro.jpg (mayo de 2024) · hoja a_241.jpg

2394. [alta] Calzada — suelo de la plaza en primer plano
   - Captura: Todo el primer plano es pavimento peatonal continuo de adoquín de piedra gris claro, x≈0–1440, y≈440–693, sin calzada de asfalto.
   - Juego: Una calzada de asfalto oscuro cruza el primer plano por la izquierda (x≈0–760, y≈400–640), separada de una zona de adoquín gris (x≈60–1440, y≈460–693).
2395. [media] Geometría — edificio de la esquina (banco), nº de plantas
   - Captura: Dos plantas más un ático: bajo comercial (y≈285–450), una planta alta de huecos altos con balcón (y≈115–245) y un remate con respiraderos pequeños (y≈90–100), x≈60–760.
   - Juego: Tres plantas completas: bajos comerciales (y≈330–420) y dos plantas de ventanas y balcones (y≈180–225 y y≈250–325), x≈325–770.
2396. [media] Huecos — bajo del edificio de la esquina
   - Captura: Fachada de banco con chapado de piedra gris, escaparates de cristal con carteles (x≈180–260, 470–540, 600–660) y puerta de entrada (x≈330–400).
   - Juego: Cierres metálicos enrollables grises con manchas de colores, x≈345–700, y≈345–420.
2397. [media] Huecos — bajo del edificio de la derecha
   - Captura: Escaparate grande de tienda, x≈1095–1260, y≈355–470.
   - Juego: Puerta con reja azul (x≈1115–1195, y≈360–465); no hay escaparate.
2398. [media] Detalles de fachada — faja roja del banco en el edificio de la esquina
   - Captura: Faja horizontal roja con el rótulo «Santander Agentes» a lo largo de todo el bajo, x≈60–760, y≈285–335.
   - Juego: No hay faja roja ni rótulo; hay toldos de rayas beige y blancas (x≈310–590, y≈345–365) y una banda verde.
2399. [media] Detalles de fachada — huecos en arco de la planta alta del edificio de la esquina
   - Captura: Huecos altos con recercado blanco rematado en arco y balcón de barandilla negra: x≈320–420, 460–550 y 600–670, y≈115–245.
   - Juego: Ventanas y balcones rectangulares sin arco, en dos plantas.
2400. [media] Detalles de fachada — edificio ornamentado de la derecha
   - Captura: Fachada crema muy decorada: recercados moldurados, pilastras, cornisa con adornos y un pináculo de piedra (x≈1040–1060, y≈40–80), x≈1040–1440, y≈0–330.
   - Juego: Fachada blanca lisa con alero de teja naranja simple, x≈830–1440.
2401. [media] Calzada — calle Don Diego López al fondo
   - Captura: Plataforma única de adoquín de piedra claro, sin bordillos, x≈760–1000, y≈370–520.
   - Juego: Calzada de asfalto oscuro con bordillos y aceras elevadas, x≈740–920, y≈365–470.
2402. [baja] Huecos — contraventanas del edificio de la esquina
   - Captura: Sin contraventanas de madera en la planta alta.
   - Juego: Ventana con contraventanas de madera marrón en la planta intermedia, x≈355–455, y≈250–295.
2403. [baja] Detalles de fachada — rótulo de la tienda de la derecha
   - Captura: Rótulo grande con letras rojas «BARRAU» sobre panel gris azulado, x≈1080–1440, y≈265–355.
   - Juego: No hay rótulo; pared blanca lisa.
2404. [baja] Marcas viales — hilera de rombos rojos en el pavimento
   - Captura: Hilera de baldosas rojas en rombo que cruza el pavimento en diagonal, x≈340–800, y≈510–670.
   - Juego: No hay rombos rojos.
2405. [baja] Vegetación — macetas en la calle
   - Captura: Macetas con plantas en la calle, x≈765–785 y x≈860–885, y≈375–410.
   - Juego: No hay macetas en la calle.
2406. [baja] Mobiliario — banco-jardinera de hormigón (abajo a la derecha)
   - Captura: Banco/jardinera de hormigón blanco con asiento de madera, x≈1205–1440, y≈575–693.
   - Juego: No hay banco; solo una bombona naranja (x≈1185–1220).
2407. [baja] Mobiliario — señales de la calle
   - Captura: Señal redonda azul de flecha en la fachada del banco (x≈678–703, y≈330–355) y señal de prohibido el paso en la fachada derecha (x≈990–1020, y≈345–370).
   - Juego: No hay ninguna de las dos señales.
2408. [baja] Otros — banderines sobre la calle
   - Captura: Cuerdas con banderines de España cruzando la calle, x≈380–960, y≈40–280.
   - Juego: No hay banderines.
**Vista #242** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_242.jpg

2409. [alta] Cámara — encuadre de la vista
   - Captura: Calle peatonal con edificio ornamentado de piedra crema con balaustradas a la izquierda (x≈0–470), supermercado DIA con toldo gris a la derecha (x≈810–1440), macetas, peatones y coches aparcados al fondo.
   - Juego: Cámara dentro de un recinto cerrado: paredes blancas con ventanas en los cuatro lados, suelo de losas y por encima la cara inferior de un tejado de teja naranja que ocupa toda la franja superior (x≈0–1035, y≈0–200); no se ve la calle.
**Vista #243** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_243.jpg

2410. [alta] Geometría — isleta central en primer plano
   - Captura: No hay isleta: asfalto continuo con una tapa de registro (x≈610–665, y≈540–575).
   - Juego: Isleta elevada con bordillos en el centro de la calzada y marca amarilla en Y, x≈390–620, y≈455–693.
2411. [alta] Color de fachada — primer edificio de la izquierda
   - Captura: Fachada crema/beige rosado, x≈0–340, y≈100–410.
   - Juego: Fachada de ladrillo rojo, x≈0–480, y≈105–470.
2412. [media] Geometría — edificio con torres al final de la calle
   - Captura: Al fondo de la calle se ve un edificio alto con torres/pináculos, x≈720–800, y≈270–350.
   - Juego: Al fondo solo hay casas blancas bajas, x≈640–720, y≈315–340.
2413. [media] Color de fachada — segundo edificio de la izquierda
   - Captura: Fachada rosa pálido con molduras blancas, x≈340–550.
   - Juego: Ladrillo rojo, x≈340–480.
2414. [media] Color de fachada — edificio de tres plantas de la derecha
   - Captura: Fachada salmón/rosada, x≈960–1440.
   - Juego: Fachada beige, x≈880–1440.
2415. [media] Huecos — planta alta del primer edificio de la izquierda
   - Captura: Tres balcones con barandilla negra en la planta alta: x≈45–130, 175–250 y 260–330, y≈245–290.
   - Juego: Ventana sin balcón (x≈75–170) y balcones solo en x≈290–365 y x≈385–435.
2416. [media] Huecos — bajo del segundo edificio de la izquierda
   - Captura: Escaparate de cristal con puerta, x≈410–520, y≈335–415.
   - Juego: Ventana pequeña (x≈390–415) y un árbol delante (x≈430–515); no hay escaparate.
2417. [media] Huecos — plantas altas del edificio de la derecha
   - Captura: Galerías acristaladas cerradas de carpintería blanca a lo ancho de las plantas altas, x≈965–1440, y≈0–240.
   - Juego: Balcones abiertos con barandilla blanca (x≈995–1165) y ventanas con persiana; ninguna galería acristalada.
2418. [media] Huecos — bajo del edificio de la derecha
   - Captura: Tienda con rótulo «TUCANO» (x≈970–1045, y≈303–323) y cierres metálicos de celosía gris (x≈1150–1440, y≈280–460).
   - Juego: Puerta con cortina de rayas verdes (x≈1035–1140, y≈360–505) y puerta de cochera blanca (x≈890–970); sin rótulo ni cierres de celosía.
2419. [media] Detalles de fachada — frontón curvo del segundo edificio de la izquierda
   - Captura: Remate barroco curvo con óculo ovalado sobre la fachada rosada, x≈350–545, y≈60–200.
   - Juego: No hay frontón: la fachada de ladrillo rojo termina en un alero recto de teja.
2420. [media] Calzada — color del asfalto
   - Captura: Asfalto gris claro desgastado, con parches, x≈300–1300, y≈420–693.
   - Juego: Asfalto gris medio-oscuro uniforme, x≈0–1150, y≈370–693.
2421. [media] Vehículos — coches aparcados a ambos lados
   - Captura: Coches aparcados en fila a ambos lados de toda la calle, x≈0–620 y x≈760–1440.
   - Juego: Ningún coche aparcado.
2422. [baja] Marcas viales — hilera de rombos rojos
   - Captura: Hilera de baldosas rojas en rombo a lo largo de la calzada, x≈700–870, y≈380–610.
   - Juego: No hay rombos rojos.
2423. [baja] Acera y bordillo — bordillo pintado de la acera izquierda
   - Captura: Bordillo pintado a franjas rojas y blancas, x≈420–530, y≈415–440.
   - Juego: Bordillos blancos sin pintar.
2424. [baja] Vegetación — árbol en la acera izquierda
   - Captura: Sin árboles en la acera izquierda.
   - Juego: Árbol redondo con naranjas, x≈430–515, y≈325–400.
2425. [baja] Vegetación — árbol en la acera derecha
   - Captura: Sin árboles en la acera derecha.
   - Juego: Árbol redondo, x≈655–715, y≈330–390.
2426. [baja] Mobiliario — farola de la acera izquierda
   - Captura: No hay farola en la acera izquierda (x≈330–405 se ve un coche rojo y la fachada).
   - Juego: Farola negra con brazo, x≈330–405, y≈210–455.
2427. [baja] Mobiliario — silla en la acera derecha
   - Captura: No hay silla en la acera.
   - Juego: Silla blanca junto a la puerta, x≈1115–1195, y≈475–560.
2428. [baja] Otros — banderines sobre la calle
   - Captura: Cuerda de banderines de España cruzando la calle, x≈730–900, y≈0–260.
   - Juego: No hay banderines.

### Calle de Hernán Cortés

**Vista #244** — 02_Desde_un_extremo_hacia_el_otro.jpg (mayo de 2024) · hoja a_244.jpg

2429. [alta] Cámara — encuadre de la vista
   - Captura: Calle recta al aire libre: casas de dos plantas crema y blancas a la izquierda (x≈0–560) y a la derecha (x≈700–1440), calzada de asfalto en el centro y un coche negro aparcado a la derecha (x≈830–1250).
   - Juego: Cámara dentro de un recinto cerrado: paredes blancas con ventanas a ambos lados (x≈0–430 y x≈1225–1440) y al fondo (x≈660–875), suelo de losas y la cara inferior de un tejado de teja que cubre toda la parte alta (x≈430–1225, y≈0–325); no se ve la calle ni el cielo.
**Vista #245** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_245.jpg

2430. [alta] Cámara — encuadre de la vista
   - Captura: Calle al aire libre: casa crema de dos plantas con balcones y rejas negras a la izquierda (x≈0–520), casa blanca con balcones, puerta negra y rejas a la derecha (x≈930–1440), calzada de asfalto y un coche blanco aparcado (x≈775–860).
   - Juego: Cámara bajo un tejado: alero y cara inferior de teja naranja ocupando toda la franja superior (x≈0–1440, y≈0–200) y paredes blancas con ventanas a la izquierda (x≈0–430), a la derecha (x≈1000–1440) y al fondo; suelo de losas; no se ve la calle.
**Vista #246** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_246.jpg

2431. [alta] Cámara — encuadre de la vista
   - Captura: Calle larga y recta al aire libre: casas de dos plantas crema/blancas con balcones, rejas y un farol de pared a la izquierda (x≈0–700); casas blancas de una planta con tejado de teja, portón verde (x≈920–985), puerta (x≈1040–1085) y ventana con reja (x≈1180–1270) a la derecha; calzada de asfalto.
   - Juego: Cámara dentro de un recinto cubierto: la cara inferior de un tejado de teja ocupa toda la parte superior (x≈0–1440, y≈0–300) y hay paredes blancas con ventanas en tres lados a pocos metros, suelo de losas; no se ve la calle ni el cielo.
**Vista #247** — 05_Acceso_oeste_desde_Constitucion.jpg (mayo de 2024) · hoja a_247.jpg

2432. [alta] Color de fachada — primer edificio de la izquierda (nave)
   - Captura: Gran paño de fachada pintado de verde que ocupa casi todo el frente visible, x≈110–530, y≈250–690, sobre muro encalado de piedra.
   - Juego: Fachada blanca lisa en todo el tramo, x≈0–700.
2433. [media] Huecos — puerta del primer edificio de la izquierda
   - Captura: Hueco de puerta ancho abierto y oscuro, sin hoja, dentro del paño verde, x≈380–470, y≈400–610.
   - Juego: En x≈380–470 solo hay pared y una bajante; más adelante, una puerta con barrotes azules y parte baja beige, x≈510–600, y≈345–600.
2434. [media] Zócalo — primer edificio de la izquierda
   - Captura: Sin zócalo diferenciado: el paño verde llega hasta la acera y el muro encalado (x≈530–630) es blanco hasta el suelo.
   - Juego: Zócalo de piedra gris a lo largo de todo el edificio, x≈0–700, y≈390–693.
2435. [media] Vegetación — árboles de la mediana
   - Captura: Plátanos desmochados de tronco blanco en la mediana: x≈950–1060 (y≈205–450) y x≈1060–1150 (y≈285–380), más un arbusto (x≈1065–1135, y≈410–490).
   - Juego: Una palmera (x≈1020–1165, y≈250–385) y un árbol redondo con naranjas (x≈1200–1410, y≈315–420).
2436. [media] Mobiliario — farola de la mediana
   - Captura: No hay farola en la mediana cercana; la farola visible es gris, alta y de brazo curvo, al otro lado de la calle paralela (x≈1255–1340, y≈135–330).
   - Juego: Farola negra de brazo recto en primer plano de la mediana, x≈940–1080, y≈105–540.
2437. [media] Otros — suelo de la mediana de la derecha
   - Captura: Mediana de tierra parda con matas bajas y plantas con flor, x≈830–1440, y≈380–693.
   - Juego: Mediana pavimentada de losas blancas, x≈780–1440, y≈360–693.
2438. [baja] Muros y vallas — marco metálico del borde izquierdo
   - Captura: En el borde izquierdo (x≈0–110) hay muro encalado de piedra.
   - Juego: Marco/barandilla metálica gris en primer plano, x≈0–90, y≈370–693.
2439. [baja] Otros — antenas de televisión en el tejado de la izquierda
   - Captura: Dos antenas sobre el tejado, x≈375–410 (y≈125–195) y x≈425–460 (y≈170–205).
   - Juego: No hay antenas.

### Calle del Arroyo

**Vista #248** — 02_Acceso_oeste_y_curva.jpg (mayo de 2024) · hoja a_248.jpg

2440. [alta] Cámara — encuadre de la vista
   - Captura: Calle estrecha: a la izquierda, a 1–2 m, un muro encalado blanco que ocupa x≈0–660 de arriba abajo; la calzada en el centro (x≈450–900); a la derecha, casas blancas de dos plantas con balcón negro (x≈905–1020), una puerta abierta con una persona (x≈925–985) y una ventana con reja (x≈1105–1220).
   - Juego: La calle con casas beige queda a la izquierda (x≈0–670), a varios metros; a la derecha la cámara está bajo un porche: pilar blanco (x≈670–745), balcón encima (x≈590–740, y≈0–280), alero de teja que cruza toda la parte alta (x≈740–1440, y≈0–85) y detrás un patio enlosado con paredes blancas y un edificio de ladrillo (x≈1180–1440); no hay muro encalado a la izquierda.
**Vista #249** — 03_Tramo_central.jpg (mayo de 2024) · hoja a_249.jpg

2441. [alta] Cámara — encuadre de la vista
   - Captura: Calle al aire libre con casas de una planta a ambos lados (izquierda x≈0–620 con puerta marrón x≈240–330; derecha x≈860–1440) y coches aparcados a los dos lados (gris x≈245–605, azul x≈800–890, negro x≈845–1100).
   - Juego: Cámara dentro de un espacio largo cubierto: la cara inferior de un tejado de teja ocupa la parte alta (x≈635–1270, y≈0–315), paredes blancas con ventanas a ambos lados y suelo de losas; no se ve la calle ni los coches.
**Vista #250** — 04_Tramo_este.jpg (mayo de 2024) · hoja a_250.jpg

2442. [alta] Muros y vallas — tapia de la izquierda
   - Captura: Tapia larga de bloques de hormigón/piedra a lo largo de todo el lado izquierdo, x≈70–530, y≈305–500, con un pilar alto de bloques en x≈0–75.
   - Juego: No hay tapia: terreno abierto blanco con un árbol, una farola y contenedores, x≈0–600.
2443. [media] Huecos — casas encaladas de la derecha
   - Captura: Dos portones grandes de madera verde (x≈912–955, y≈335–430 y x≈1125–1215, y≈350–525) y una ventana pequeña con postigo verde (x≈1020–1050); ninguna reja.
   - Juego: Una puerta verde estrecha (x≈980–1015), una puerta de cochera blanca (x≈905–945) y una ventana grande con reja negra (x≈1080–1155, y≈350–460).
2444. [media] Marcas viales — líneas de borde de la calzada
   - Captura: Calzada sin líneas longitudinales.
   - Juego: Líneas blancas continuas en ambos bordes de la calzada, x≈0–650 y x≈795–1190.
2445. [media] Mobiliario — contenedores del lado izquierdo
   - Captura: No hay contenedores; en esa zona está la tapia y el cruce (x≈430–600).
   - Juego: Fila de contenedores marrón, azul, amarillo y verde con bolsas, x≈435–585, y≈370–450.
2446. [baja] Cubierta — tejados de las casas de la derecha
   - Captura: Teja vieja de color pardo-grisáceo, x≈800–1440, y≈190–330.
   - Juego: Teja naranja intenso, x≈820–1440, y≈220–345.
2447. [baja] Calzada — estado del asfalto
   - Captura: Asfalto gris con muchas grietas ramificadas, x≈0–1300, y≈380–693.
   - Juego: Asfalto liso con una sola grieta oscura en el centro.
2448. [baja] Vegetación — árbol del primer plano izquierdo
   - Captura: No hay árbol en el lado izquierdo cercano (está la tapia).
   - Juego: Árbol redondo con naranjas, x≈0–365, y≈295–455.
2449. [baja] Mobiliario — farola del lado izquierdo
   - Captura: No hay farola en el lado izquierdo cercano.
   - Juego: Farola negra con brazo, x≈200–325, y≈135–515.
2450. [baja] Mobiliario — farol de pared de la derecha
   - Captura: Farol clásico negro sobre brazo de hierro en la fachada, x≈935–985, y≈225–345.
   - Juego: No hay farol en la fachada.
**Vista #251** — 05_Vista_hacia_el_oeste.jpg (mayo de 2024) · hoja a_251.jpg

2451. [alta] Geometría — isleta pavimentada del primer plano
   - Captura: La cámara está sobre la calzada: asfalto con marcas viales en todo el primer plano, x≈0–1250, y≈400–693.
   - Juego: La cámara está sobre una isleta/mediana de losas blancas con bordillo, x≈0–800, y≈380–693, entre dos calzadas.
2452. [alta] Geometría — primera casa de la izquierda
   - Captura: Casa de una planta con tejado de teja (x≈0–220, alero en y≈305–345) y ventana con reja (x≈35–75).
   - Juego: Casa de dos plantas (x≈0–270, alero en y≈150–235) con contraventanas de madera en la planta alta.
2453. [media] Geometría — isleta con seto de la derecha
   - Captura: Isleta triangular con seto bajo recortado, x≈960–1250, y≈490–693.
   - Juego: No hay isleta: calzada lisa con una tapa de registro (x≈1150–1290, y≈600–670).
2454. [media] Calzada — calzada de la derecha
   - Captura: Asfalto gris medio con líneas blancas, x≈700–1440, y≈420–693.
   - Juego: Superficie beige-gris muy clara sin marcas, x≈770–1440, y≈375–693.
2455. [media] Marcas viales — marcas de la calzada
   - Captura: Líneas discontinuas de carril (x≈540–660 y x≈780–910), paso de peatones al fondo (x≈630–840, y≈388–410) y cebreado diagonal a la izquierda (x≈0–520, y≈400–560).
   - Juego: Sin paso de peatones, sin cebreado ni líneas de carril; solo una línea blanca corta en la calzada izquierda.
2456. [media] Vegetación — árbol en el centro del primer plano
   - Captura: No hay árbol cerca de la cámara; al fondo, a unos 30 m, la mediana con árboles y una palmera (x≈480–700, y≈240–410).
   - Juego: Árbol grande redondo en un alcorque justo delante de la cámara, x≈485–935, y≈30–550, que tapa el fondo.
2457. [baja] Mobiliario — señales de la isleta derecha
   - Captura: Señal azul de paso de peatones (x≈980–1050, y≈340–530) y señal triangular de ceda el paso (x≈1115–1160, y≈370–495).
   - Juego: No hay señales.
2458. [baja] Otros — banderines sobre la calle
   - Captura: Cuerda de banderines de España cruzando el cielo, x≈680–930, y≈0–290.
   - Juego: No hay banderines.

### Calle el Pilar

**Vista #252** — 02_Desde_un_extremo_hacia_el_otro.jpg (mayo de 2024) · hoja a_252.jpg

2459. [media] Color de fachada — casa de dos plantas con chapado de piedra (izquierda)
   - Captura: Fachada chapada de piedra gris con puerta de cochera blanca (x≈515–545), x≈495–570, y≈225–420.
   - Juego: En esa posición, fachada blanca enfoscada (casa de una planta con puerta en x≈520–550 y casa blanca de dos plantas detrás).
2460. [media] Color de fachada — casa de dos plantas de la derecha (con balcón)
   - Captura: Fachada ocre/crema con manchas de piedra, x≈810–920, y≈230–420.
   - Juego: Fachada blanca, x≈830–920.
2461. [media] Huecos — primer edificio de la izquierda (portón metálico)
   - Captura: Portón grande de chapa ondulada gris que ocupa toda la fachada visible, x≈0–260, y≈235–590.
   - Juego: Pared blanca con una ventana de persiana blanca y macetas, x≈185–320, y≈355–490; no hay portón.
2462. [media] Huecos — puerta de la casa encalada de la derecha
   - Captura: Puerta grande de madera marrón de dos hojas con recercado, x≈1050–1130, y≈335–495.
   - Juego: Puerta con cortina de rayas verdes y amarillas, x≈1005–1050, y≈350–440.
2463. [media] Huecos — ventana del extremo derecho
   - Captura: Ventana grande con barrotes negros horizontales, x≈1295–1440, y≈355–510.
   - Juego: Puerta de cochera blanca en el borde (x≈1400–1440, y≈330–580) y ventana con reja negra en x≈1135–1250.
2464. [media] Zócalo — segundo edificio de la izquierda
   - Captura: Banda inferior de color rosa, x≈260–495, y≈380–500.
   - Juego: Zócalo ocre/marrón a lo largo de toda la fachada, x≈0–600, y≈430–690.
2465. [media] Cubierta — edificios del primer plano izquierdo
   - Captura: Remate recto con peto/cornisa, sin teja visible, x≈0–495, y≈235–290.
   - Juego: Tejado de teja naranja con alero, x≈0–590, y≈200–330.
2466. [media] Calzada — color del asfalto
   - Captura: Asfalto beige-grisáceo claro, x≈200–1300, y≈360–693.
   - Juego: Asfalto gris medio, x≈150–1400, y≈360–693.
2467. [media] Marcas viales — líneas de borde de la calzada
   - Captura: Calzada sin líneas.
   - Juego: Líneas blancas continuas en ambos bordes, x≈420–700 y x≈760–1350.
2468. [baja] Detalles de fachada — rótulo del segundo edificio de la izquierda
   - Captura: Rótulo amarillo «R. RODRIGUEZ» (x≈375–450, y≈300–325) y una placa roja pequeña (x≈318–330).
   - Juego: No hay rótulos.
2469. [baja] Cubierta — tejados de las casas de la derecha
   - Captura: Teja vieja de color pardo-grisáceo, x≈920–1440, y≈100–300.
   - Juego: Teja naranja intenso, x≈910–1440.
2470. [baja] Vegetación — macetas de la acera izquierda
   - Captura: Sin macetas en la acera ni en las ventanas de la izquierda.
   - Juego: Macetas con flores en el alféizar (x≈205–315) y un ciprés en maceta en la acera (x≈450–475, y≈420–480).
2471. [baja] Mobiliario — farol de pared de la derecha
   - Captura: Farol de pared negro sobre la casa de dos plantas de la derecha, x≈885–915, y≈235–275.
   - Juego: No hay farol en esa fachada.
**Vista #253** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_253.jpg

2472. [alta] Geometría — primera casa de la izquierda
   - Captura: Casa de una planta con tejado de teja (alero en y≈140–290), x≈0–490.
   - Juego: Casa de dos plantas que llega al borde superior, con ventana grande en la planta alta (x≈0–310, y≈40–250), x≈0–365.
2473. [alta] Color de fachada — planta alta de ladrillo de la derecha
   - Captura: Planta alta sin terminar de ladrillo rojo visto, x≈860–1165, y≈100–300.
   - Juego: Planta alta blanca enfoscada, x≈800–1230, y≈0–300.
2474. [media] Color de fachada — medianera gris del extremo derecho
   - Captura: Enfoscado de cemento gris sin pintar, x≈1165–1420, con zócalo de plaqueta de piedra oscura (y≈470–640).
   - Juego: Fachada blanca, x≈1150–1440.
2475. [media] Huecos — puerta de la primera casa de la izquierda
   - Captura: Puerta de madera marrón con recercado crema, x≈295–385, y≈335–480.
   - Juego: En x≈295–385 hay una bajante y pared; la puerta más cercana está en la casa siguiente (x≈480–500).
2476. [media] Huecos — medianera gris del extremo derecho
   - Captura: Pared alta ciega, sin ningún hueco, x≈1165–1420, y≈0–620.
   - Juego: Fachada con ventana grande en la planta alta (x≈1235–1385, y≈40–215) y puerta beige con barrotes azules (x≈1245–1390, y≈365–590).
2477. [media] Huecos — huecos de la planta alta de ladrillo (derecha)
   - Captura: Huecos vacíos y oscuros sin carpintería: x≈880–895, x≈925–955 (y≈245–300) y x≈1015–1075 (y≈195–275).
   - Juego: Ventanas con marco blanco y persiana, x≈1030–1080 (y≈180–265).
2478. [media] Huecos — postigo verde de la casa encalada de la derecha
   - Captura: Ventana/puerta con hoja de madera verde, x≈1025–1055, y≈355–435.
   - Juego: Ventana con reja negra, x≈1020–1080, y≈350–435.
2479. [media] Detalles de fachada — recercados de la primera casa de la izquierda
   - Captura: Recercados de color crema/ocre alrededor de la ventana (x≈55–180, y≈370–490) y de la puerta (x≈295–385, y≈335–480).
   - Juego: Ventana y paredes sin recercados.
2480. [media] Zócalo — casa encalada de la derecha
   - Captura: Zócalo ocre/crema continuo, x≈860–1165, y≈420–540.
   - Juego: Zócalo ocre solo en x≈900–1000 y de piedra gris en x≈995–1230.
2481. [media] Calzada — color del asfalto
   - Captura: Asfalto beige-grisáceo claro, x≈150–1200, y≈360–693.
   - Juego: Asfalto gris medio, x≈0–1400, y≈360–693.
2482. [media] Marcas viales — líneas de borde de la calzada
   - Captura: Calzada sin líneas.
   - Juego: Líneas blancas continuas en ambos bordes, x≈215–650 y x≈760–1115.
2483. [baja] Huecos — reja de la ventana de la primera casa de la izquierda
   - Captura: Reja blanca, x≈55–180, y≈370–490.
   - Juego: Reja verde, x≈80–265, y≈350–495.
**Vista #254** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_254.jpg

2484. [alta] Color de fachada — casa roja de la izquierda
   - Captura: Casa de dos plantas de fachada rojo coral con recercados crema y zócalo ocre, x≈480–605, y≈200–455.
   - Juego: En x≈480–605 continúa la fachada gris blanquecina de la primera casa (con un aparato de aire acondicionado).
2485. [media] Huecos — planta alta de la primera casa de la izquierda
   - Captura: Pared blanca lisa en la planta alta, con solo una ventana pequeña con persiana blanca (x≈385–425, y≈205–270); sin balcón.
   - Juego: Balcón grande con barandilla negra y toldo blanco, x≈0–265, y≈55–290, y ventana en x≈380–440.
2486. [media] Huecos — planta baja de la primera casa de la izquierda
   - Captura: Ventana grande con barrotes oscuros verticales, x≈115–270, y≈380–515.
   - Juego: Verja negra alta de suelo a techo, x≈0–190, y≈355–620, y pared lisa en x≈190–355.
2487. [media] Huecos — balcones de la casa roja de la izquierda
   - Captura: Tres balcones con barandilla negra en la planta alta, x≈510–600, y≈285–330.
   - Juego: Ventanas sin balcón en esa zona (x≈520–545).
2488. [media] Calzada — color del asfalto
   - Captura: Asfalto beige-grisáceo claro, x≈250–1300, y≈360–693.
   - Juego: Asfalto gris medio con un parche rectangular más claro (x≈605–860, y≈515–693).
2489. [media] Marcas viales — línea de borde de la calzada
   - Captura: Calzada sin líneas.
   - Juego: Línea blanca continua a lo largo del borde derecho, x≈780–1440, y≈370–693.
2490. [baja] Huecos — puerta de la primera casa de la izquierda
   - Captura: Puerta de madera marrón, x≈400–440, y≈350–480.
   - Juego: Puerta con barrotes negros, x≈380–435, y≈360–420.
2491. [baja] Huecos — ventanas de la casa de la derecha
   - Captura: Ventanas con persiana enrollable blanca, sin contraventanas (x≈1305–1370, y≈260–315 y x≈1265–1325, y≈390–450).
   - Juego: Contraventanas de madera marrón (x≈1245–1300, y≈140–245) y macetas en los alféizares.
2492. [baja] Detalles de fachada — peto de ladrillo de la casa baja de la derecha
   - Captura: Remate de ladrillo rojo visto sobre la fachada blanca, x≈900–1135, y≈280–330.
   - Juego: Remate blanco, sin ladrillo, x≈920–1225.
2493. [baja] Otros — toldo de la azotea de la derecha
   - Captura: Toldo de rayas azules y blancas en la azotea detrás de las casas, x≈1085–1320, y≈180–250.
   - Juego: No hay toldo.

### Calle Encina

**Vista #255** — 02_Desde_un_extremo_hacia_el_otro.jpg (octubre de 2021) · hoja a_255.jpg

2494. [alta] Geometría — espacio peatonal del primer plano derecho
   - Captura: Calle estrecha (asfalto de x≈430 a 880 en el borde inferior) y a la derecha una plaza pavimentada de losas con un banco de hormigón, x≈830–1440, y≈480–693.
   - Juego: Calzada ancha de asfalto que ocupa todo el primer plano derecho hasta x≈1440, con un cruce y un coche aparcado (x≈1075–1440); no hay plaza peatonal.
2495. [media] Color de fachada — casa de dos plantas de la izquierda
   - Captura: Fachada beige/crema con cornisa y recercados de piedra, x≈0–580, y≈0–600.
   - Juego: Fachada blanca, x≈0–590.
2496. [media] Huecos — planta baja de la casa de la izquierda (cochera)
   - Captura: Puerta de cochera ancha de madera marrón de lamas verticales, x≈0–405, y≈325–610.
   - Juego: Ventana grande con persiana enrollable (x≈240–415, y≈350–545) y pared lisa; no hay cochera.
2497. [media] Huecos — balcón de la planta alta de la casa de la izquierda
   - Captura: Balcón corrido con barandilla negra, x≈320–530, y≈65–265.
   - Juego: Ventana con persiana sin balcón (x≈240–415, y≈0–215) y otra ventana pequeña (x≈515–560).
2498. [media] Marcas viales — marcas de la calzada
   - Captura: Calzada sin marcas, agrietada.
   - Juego: Línea blanca central continua (x≈580–715, y≈405–693) y líneas blancas en el cruce de la derecha (x≈820–1440).
2499. [baja] Huecos — puerta de la casa de la izquierda
   - Captura: Puerta de madera marrón oscuro con recercado de granito, x≈440–495, y≈320–495.
   - Juego: Puerta de madera clara sin recercado de piedra, x≈515–560, y≈350–465.
2500. [baja] Cubierta — trozo de alero flotante
   - Captura: Fachada continua; no hay ningún alero suelto a la izquierda.
   - Juego: Trozo de alero de teja naranja suelto delante de la fachada, x≈0–130, y≈215–270.
2501. [baja] Mobiliario — farol de pared de la casa de la izquierda
   - Captura: Farol de pared sobre brazo, x≈560–600, y≈190–250.
   - Juego: No hay farol en esa fachada.
2502. [baja] Mobiliario — banco de hormigón y bolardo
   - Captura: Banco largo de hormigón (x≈920–1180, y≈540–693) y un bolardo (x≈925–950, y≈575–630).
   - Juego: No hay banco ni bolardo.
2503. [baja] Mobiliario — farola del fondo izquierdo
   - Captura: No hay farola en la acera izquierda al fondo (x≈650–690 son casas blancas).
   - Juego: Farola negra con brazo, x≈650–690, y≈275–400.
**Vista #256** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_256.jpg

2504. [alta] Color de fachada — muro de ladrillo de la derecha
   - Captura: Muro alto de ladrillo rojo visto sin revestir, x≈800–1440, y≈0–693.
   - Juego: Fachada blanca enfoscada, x≈780–1440.
2505. [media] Huecos — muro de ladrillo de la derecha
   - Captura: Sin puertas ni ventanas a la altura de la calle; solo un hueco vacío arriba, x≈1130–1205, y≈0–170.
   - Juego: Puerta con cortina de rayas en un recercado de piedra (x≈880–1015, y≈340–693) y ventana con reja verde (x≈810–840).
2506. [media] Huecos — portón de la primera casa de la izquierda
   - Captura: Portón grande de madera marrón con clavos, x≈0–270, y≈355–693.
   - Juego: Puerta con cortina de rayas, x≈130–240, y≈365–580.
2507. [media] Huecos — puerta acristalada de la casa de la izquierda
   - Captura: Puerta moderna de aluminio y cristal, x≈420–540, y≈320–520.
   - Juego: Ventana con reja (x≈370–425) y puerta estrecha (x≈470–500).
2508. [media] Huecos — planta alta de la casa de la izquierda
   - Captura: Ventana con reja en la planta alta, x≈490–540, y≈150–260; sin balcón.
   - Juego: Balcón con barandilla negra, x≈465–520, y≈270–320.
2509. [media] Cubierta — casas de la izquierda
   - Captura: Remates rectos encalados sin alero de teja visible, x≈0–575, y≈0–320.
   - Juego: Aleros de teja naranja a lo largo de las casas, x≈0–570, y≈165–325.
2510. [media] Calzada — suelo de la calle
   - Captura: Pavimento de hormigón/cemento beige claro, x≈300–1200, y≈380–693.
   - Juego: Asfalto gris, x≈300–950.
2511. [baja] Marcas viales — línea discontinua
   - Captura: Sin marcas.
   - Juego: Línea discontinua oscura transversal, x≈550–810, y≈515–520.
2512. [baja] Mobiliario — farol de pared de la izquierda
   - Captura: Farol de pared sobre brazo, x≈570–610, y≈190–250.
   - Juego: No hay farol en esa fachada.
2513. [baja] Mobiliario — farola del primer plano izquierdo
   - Captura: No hay farola en primer plano.
   - Juego: Fuste de farola gris oscuro en primer plano, x≈145–220, de arriba abajo.
2514. [baja] Mobiliario — silla en la acera izquierda
   - Captura: No hay silla.
   - Juego: Silla blanca en la acera, x≈295–365, y≈455–530.
2515. [baja] Muros y vallas — vallas de obra de la derecha
   - Captura: Vallas metálicas amarillas con cinta roja y blanca a lo largo del muro de ladrillo, x≈805–1300, y≈380–693.
   - Juego: No hay vallas.
**Vista #257** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_257.jpg

2516. [media] Color de fachada — pared de la izquierda
   - Captura: Pared blanca con recercado ocre y banda baja ocre (x≈505–600, y≈440–560).
   - Juego: Pared beige-grisácea con textura rugosa, x≈125–720.
2517. [media] Huecos — portón de la pared izquierda
   - Captura: Portón de madera marrón de dos hojas con recercado ocre/tostado, x≈360–535, y≈365–693.
   - Juego: Pared lisa sin portón; solo una ventana estrecha con persiana blanca más adelante (x≈645–670, y≈375–560).
2518. [media] Huecos — casas viejas de la derecha
   - Captura: Solo un hueco de puerta estrecho, x≈865–895, y≈375–520; sin ventanas visibles.
   - Juego: Puerta de cochera verde (x≈910–980, y≈340–470) y ventana grande con reja blanca (x≈1030–1140, y≈350–495).
2519. [media] Zócalo — casas viejas de la derecha
   - Captura: Encalado hasta el suelo con desconchones; solo una banda gris corta en x≈895–1000, y≈510–640.
   - Juego: Zócalo de bloques de piedra gris continuo, x≈985–1440, y≈430–693.
2520. [media] Cubierta — remate de la pared izquierda
   - Captura: Remate recto blanco sin teja, x≈0–600, y≈0–240.
   - Juego: Alero de teja naranja sobre la pared, x≈540–725, y≈0–320.
2521. [media] Calzada — suelo de la calle
   - Captura: Pavimento de cemento beige claro, x≈480–980, y≈340–693.
   - Juego: Asfalto gris, x≈690–1180.
2522. [media] Acera y bordillo — acera de la derecha
   - Captura: Sin acera elevada ni bordillo: el pavimento llega hasta las fachadas de la derecha.
   - Juego: Acera elevada con bordillo blanco a la derecha (x≈760–1340, y≈360–693) y bordillo pintado de amarillo (x≈840–900).
2523. [baja] Geometría — borde izquierdo de la imagen
   - Captura: La pared blanca ocupa todo el borde izquierdo (x≈0–360).
   - Juego: En x≈0–125 se ve un espacio cubierto con la cara inferior de un tejado, una puerta (x≈75–105) y una señal roja y azul (x≈0–60, y≈430–480).
2524. [baja] Color de fachada — encalado de las casas de la derecha
   - Captura: Encalado muy desconchado con grandes manchas pardas y grises, x≈810–1440, y≈330–693.
   - Juego: Pared blanca limpia y uniforme.
2525. [baja] Cubierta — tejado de las casas de la derecha
   - Captura: Teja vieja parda con líquenes, x≈810–1440, y≈190–345.
   - Juego: Teja naranja intenso, x≈760–1440, y≈185–345.

### Calle Espronceda

**Vista #258** — 02_Desde_un_extremo_hacia_el_otro.jpg (mayo de 2024) · hoja a_258.jpg

2526. [alta] Geometría — edificio del primer plano derecho
   - Captura: Edificio grande alineado con la acera estrecha, con un portón metálico ondulado gris (x≈1110–1440, y≈275–580); la calle es estrecha.
   - Juego: Una explanada pavimentada ancha (x≈870–1440, y≈420–620) delante de una casa blanca de dos plantas retranqueada (x≈870–1300, y≈215–430) y de un garaje blanco con tejado (x≈1235–1440, y≈310–455).
2527. [alta] Color de fachada — bloque de pisos de la izquierda (planta baja)
   - Captura: Planta baja blanca con zócalo y marcos de puerta rojo oscuro, x≈0–560, y≈200–693; plantas altas de color terracota/marrón rosado.
   - Juego: Todo el edificio, incluida la planta baja, de ladrillo rojo anaranjado, x≈0–650.
2528. [media] Color de fachada — edificio del primer plano derecho
   - Captura: Paño superior de color salmón/rosado, x≈930–1440, y≈30–300, sobre zócalo blanco.
   - Juego: Fachada blanca con contraventanas verdes, x≈870–1300.
2529. [media] Huecos — plantas altas del bloque de la izquierda
   - Captura: Balcones corridos con barandilla blanca en las plantas altas, x≈420–640, y≈0–230.
   - Juego: Ventanas sueltas con marco blanco y dos balcones pequeños (x≈605–645, y≈85–215); sin balcones corridos.
2530. [media] Acera y bordillo — acera de la izquierda
   - Captura: Baldosa en damero rojo y blanco, x≈300–660, y≈380–693.
   - Juego: Baldosa blanca/gris clara, x≈460–690.
2531. [media] Acera y bordillo — acera de la derecha
   - Captura: Baldosa en damero rojo y blanco junto al portón, x≈940–1440, y≈450–693.
   - Juego: Explanada de baldosa blanca/gris clara, x≈870–1440, y≈420–620.
2532. [baja] Marcas viales — plazas de aparcamiento de la derecha
   - Captura: Líneas blancas de plazas de aparcamiento junto a la acera derecha, x≈780–1000, y≈420–520.
   - Juego: Sin marcas; solo grietas en el asfalto.
2533. [baja] Mobiliario — farola de la derecha
   - Captura: No se ve farola en la acera derecha.
   - Juego: Farola negra con brazo, x≈815–865, y≈240–400.
**Vista #259** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_259.jpg

2534. [alta] Cámara — encuadre de la vista
   - Captura: Calle estrecha al aire libre: casa crema con portón de madera marrón (x≈372–504) y balcones de barandilla negra (x≈420–528) a la izquierda; casa salmón con balcón (x≈1062–1440, y≈0–205), puerta negra con clavos (x≈1230–1440) y ventana con reja (x≈948–1008) a la derecha; coche oscuro aparcado (x≈888–1440, y≈498–684).
   - Juego: Cámara dentro de un patio cerrado: paredes de ladrillo rojo a la izquierda (x≈0–528) y a la derecha (x≈1044–1440), un edificio blanco alargado al fondo y la cara inferior de un tejado de teja encima (x≈528–1044, y≈0–308); suelo de losas; no se ve la calle.
**Vista #260** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_260.jpg

2535. [media] Color de fachada — bloque alto del fondo a la derecha
   - Captura: Bloque de varias plantas de color beige claro con balcones blancos, x≈710–790, y≈190–330.
   - Juego: Edificio de tres plantas de ladrillo rojo, x≈710–810, y≈200–375.
2536. [media] Huecos — puerta de la casa de la derecha (nº 13)
   - Captura: Puerta grande de madera marrón de dos hojas con recercado crema, x≈960–1130, y≈295–600.
   - Juego: Puerta de cochera blanca de paneles (x≈1050–1440, y≈305–693) y una puerta beige con barrotes (x≈885–960, y≈345–530).
2537. [media] Huecos — ventana baja de la casa de la derecha
   - Captura: Ventana alta con reja negra, x≈850–890, y≈320–470.
   - Juego: Puerta de cochera blanca enrollable, x≈815–855, y≈335–460.
2538. [media] Huecos — planta alta de la casa de la derecha
   - Captura: Ventanas con barandilla negra: x≈990–1065 (y≈50–195) y x≈860–885 (y≈190–260).
   - Juego: Balcón con barandilla blanca y macetas (x≈860–965, y≈205–315) y ventana con persiana (x≈1165–1440, y≈0–125).
2539. [media] Huecos — planta alta de la primera casa de la izquierda
   - Captura: Balcón con barandilla negra ante una ventana con persiana, x≈370–430, y≈140–295.
   - Juego: Ventana sin balcón con macetas, x≈450–520, y≈160–270.
2540. [media] Detalles de fachada — recercados de la casa de la derecha
   - Captura: Recercados y pilastras de color crema/ocre alrededor de ventanas y puerta, x≈820–1440.
   - Juego: Paredes blancas lisas; solo la puerta beige tiene recercado de piedra (x≈880–965).
2541. [media] Calzada — color del asfalto
   - Captura: Asfalto beige-grisáceo claro, x≈250–1000, y≈360–693.
   - Juego: Asfalto gris oscuro, x≈230–1010.
2542. [media] Acera y bordillo — acera de la izquierda
   - Captura: Baldosa en damero rojo y blanco, x≈250–640, y≈380–693.
   - Juego: Baldosa blanca/gris clara, x≈150–640.
2543. [media] Acera y bordillo — acera de la derecha
   - Captura: Baldosa en damero rojo y blanco, x≈720–1100, y≈360–693.
   - Juego: Baldosa blanca/gris clara, x≈700–1150.
2544. [baja] Huecos — puerta de la primera casa de la izquierda (nº 12)
   - Captura: Puerta de madera marrón oscuro tallada, x≈360–425, y≈335–510.
   - Juego: Puerta de madera clara tipo cochera con dos ventanillos, x≈450–520, y≈350–490.
2545. [baja] Huecos — ventana baja de la primera casa de la izquierda
   - Captura: Ventana con reja oscura, x≈0–65, y≈360–580.
   - Juego: Ventana grande con reja verde, x≈0–280, y≈350–625.
2546. [baja] Detalles de fachada — toldo de la segunda casa de la izquierda
   - Captura: Toldo de rayas azules y blancas sobre el balcón, x≈550–600, y≈170–225.
   - Juego: No hay toldo.
2547. [baja] Marcas viales — marcas de la calzada
   - Captura: Línea discontinua blanca central (x≈620–660, y≈480–560) y línea transversal blanca (x≈560–660, y≈483–490).
   - Juego: Sin línea central; solo una línea discontinua oscura transversal (x≈410–740, y≈600–610).

### Calle Lumbreras

**Vista #261** — 02_Desde_un_extremo_hacia_el_otro.jpg (mayo de 2024) · hoja a_261.jpg

2548. [media] Color de fachada — casas de la izquierda
   - Captura: Fachadas de color beige/crema, x≈0–720, y≈0–693.
   - Juego: Fachadas blancas, x≈0–720.
2549. [media] Huecos — ventana de la planta baja de la primera casa de la izquierda
   - Captura: Una ventana mediana con reja negra a media altura, x≈420–530, y≈325–470; el resto del paño (x≈0–410) es pared lisa.
   - Juego: Ventana mucho mayor con reja gris y persiana que baja casi hasta el suelo, x≈170–465, y≈355–693.
2550. [media] Huecos — puerta de la casa de la izquierda
   - Captura: Puerta con recercado de piedra moldurado y escalones de subida, x≈570–630, y≈320–500.
   - Juego: Puerta beige con barrotes azules sin recercado de piedra ni escalones, x≈580–610, y≈360–500.
2551. [media] Huecos — casas de la derecha
   - Captura: Paredes altas encaladas sin huecos en el tramo cercano, x≈1000–1440, y≈130–693.
   - Juego: Ventana grande con reja y macetas (x≈1000–1125, y≈355–565), puerta (x≈890–915) y balcón con barandilla negra (x≈850–925, y≈235–310).
2552. [media] Zócalo — casas de la izquierda
   - Captura: Sin zócalo de piedra: la pintura beige llega al suelo, x≈0–720, y≈470–693.
   - Juego: Zócalo de bloques de piedra gris, x≈380–720, y≈430–693.
2553. [media] Cubierta — casas de la derecha
   - Captura: Remate recto encalado sin alero de teja, x≈760–1440, y≈0–270.
   - Juego: Aleros de teja naranja (x≈790–1250, y≈40–300) y un cuerpo alto con chimenea (x≈1210–1300, y≈75–200).
2554. [media] Calzada — suelo del callejón
   - Captura: Hormigón beige claro, x≈500–900, y≈370–693.
   - Juego: Asfalto gris oscuro, x≈560–990.
2555. [media] Acera y bordillo — acera de la derecha
   - Captura: Baldosa en damero rojo y blanco, x≈760–1050, y≈380–693.
   - Juego: Baldosa gris clara, x≈760–1130.
2556. [baja] Huecos — planta alta de la primera casa de la izquierda
   - Captura: Pared lisa en x≈230–440, y≈0–130; solo un aparato de aire acondicionado (x≈520–580, y≈50–130) y una ventana con persiana (x≈570–615, y≈110–195).
   - Juego: Ventana con persiana y macetas (x≈230–440, y≈0–130) y ventana con reja (x≈580–625, y≈125–260); sin aire acondicionado.
2557. [baja] Cubierta — trozo de alero flotante de la derecha
   - Captura: Pared continua; no hay ningún alero suelto.
   - Juego: Trozo de alero de teja naranja suelto que cruza delante de la pared, x≈935–1390, y≈195–310.
2558. [baja] Acera y bordillo — bordillo de la izquierda
   - Captura: Bordillo pintado de blanco con algunas baldosas rojas al pie, x≈400–720, y≈370–693.
   - Juego: Acera estrecha de losas grises con bordillo blanco, x≈430–720.
2559. [baja] Vegetación — macetas en la acera izquierda
   - Captura: Sin macetas en la acera.
   - Juego: Macetas con flores y un ciprés junto a la puerta, x≈620–680, y≈400–480.
2560. [baja] Mobiliario — farol de pared de la derecha
   - Captura: Farol clásico sobre brazo de hierro en la pared derecha, x≈920–1025, y≈0–130.
   - Juego: No hay farol en esa pared.
**Vista #262** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_262.jpg

2561. [alta] Geometría — casas de la derecha, nº de plantas
   - Captura: Casas de una planta con alero de teja que baja de y≈80 (x≈1160) a y≈300 (x≈800).
   - Juego: Casas de dos plantas con ventanas de contraventanas verdes en la planta alta, alero de y≈0 (x≈940) a y≈240 (x≈800).
2562. [media] Huecos — planta alta de las casas de la izquierda
   - Captura: Solo una ventana pequeña con reja negra en la planta alta, x≈585–612, y≈190–280.
   - Juego: Ventanas con contraventanas verdes y macetas, x≈515–610, y≈0–230, y un balcón (x≈625–670, y≈240–305).
2563. [media] Huecos — pared del primer plano izquierdo
   - Captura: Pared blanca ciega, sin huecos, x≈0–420, y≈0–693.
   - Juego: Reja grande (x≈0–295, y≈370–693) y ventana con contraventanas verdes y macetas (x≈70–430, y≈0–110).
2564. [media] Huecos — pared del primer plano derecho
   - Captura: Pared blanca ciega, x≈1160–1440, y≈0–693.
   - Juego: Puerta de cochera blanca, x≈1055–1440, y≈295–693, y una ventana alta (x≈1160–1300, y≈0–90).
2565. [media] Huecos — ventana de la casa de la derecha
   - Captura: Ventana con reja negra, x≈935–980, y≈380–500.
   - Juego: Ventana con persiana y marco verde, sin reja, x≈910–960, y≈355–470.
2566. [media] Calzada — suelo del callejón
   - Captura: Hormigón beige claro, x≈550–900, y≈375–693.
   - Juego: Asfalto gris oscuro, x≈600–990.
2567. [media] Acera y bordillo — acera de la derecha
   - Captura: Baldosa en damero rojo y blanco, x≈760–1000, y≈380–693.
   - Juego: Baldosa gris clara, x≈760–1080.
2568. [media] Acera y bordillo — acera de la izquierda
   - Captura: Baldosa en damero rojo y blanco, x≈480–700, y≈380–693.
   - Juego: Baldosa gris clara, x≈520–700.
2569. [baja] Color de fachada — desconchones de la casa de la derecha
   - Captura: Encalado con desconchones pardos en la parte baja, x≈890–1065, y≈450–640.
   - Juego: Pared blanca limpia.
2570. [baja] Detalles de fachada — bajante de la izquierda
   - Captura: No se ve bajante en la pared izquierda.
   - Juego: Bajante blanca de arriba abajo, x≈495–515.
2571. [baja] Cubierta — alero flotante de la izquierda
   - Captura: Sin ningún alero en la pared cercana de la izquierda.
   - Juego: Trozo de alero de teja naranja suelto cruzando la pared, x≈0–545, y≈30–285.
2572. [baja] Mobiliario — farol de pared de la derecha
   - Captura: Sin farol en la pared derecha.
   - Juego: Farol de pared, x≈820–860, y≈325–360.
2573. [baja] Otros — antena de televisión
   - Captura: Antena sobre el tejado de la derecha, x≈940–970, y≈110–200.
   - Juego: No hay antena.
**Vista #263** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_263.jpg

2574. [alta] Geometría — lado izquierdo del callejón
   - Captura: Muro alto continuo, a 1–2 m, de enfoscado sin pintar gris-beige con grafitis, x≈0–590, y≈0–693; el callejón sigue estrecho y cerrado por ambos lados hasta el fondo.
   - Juego: No hay muro: a la izquierda se abre una plaza ancha de losas blancas (x≈0–700, y≈400–693) con casas bajas exentas a 15–30 m (x≈160–700, y≈235–430) y una casa de dos plantas en el borde (x≈0–180).
2575. [media] Huecos — planta alta de la casa de la derecha
   - Captura: Pared blanca lisa con una ventana pequeña, x≈905–940, y≈60–130; sin balcón sobre la cámara.
   - Juego: Balcón grande en voladizo sobre la cámara, x≈870–1440, y≈0–170, y otro con barandilla verde (x≈695–775, y≈50–295).
2576. [media] Huecos — planta baja de la casa de la derecha
   - Captura: Ventana con reja y persiana dentro de un recercado gris, x≈875–955, y≈285–560, y puerta con recercado gris (x≈820–850, y≈300–450).
   - Juego: Pared lisa sin ventana en esa zona; solo un marco de puerta estrecho, x≈750–775, y≈350–595.
2577. [media] Zócalo — casa de la derecha
   - Captura: Zócalo de plaqueta de piedra beige, x≈1060–1230, y≈570–693.
   - Juego: Sin zócalo: pared beige-blanca lisa hasta el suelo.
2578. [media] Calzada — suelo del callejón
   - Captura: Hormigón beige claro, x≈430–900, y≈350–693.
   - Juego: Asfalto gris oscuro, x≈150–720.
2579. [media] Acera y bordillo — acera de la derecha
   - Captura: Acera estrecha con bordillo blanco y baldosas en damero rojo y blanco, x≈870–1000, y≈540–693.
   - Juego: Losas grises, x≈640–750.
2580. [baja] Mobiliario — farol de pared al fondo de la derecha
   - Captura: No hay farol en esa zona.
   - Juego: Farol de pared sobre brazo, x≈690–745, y≈310–365.
**Vista #264** — 05_Conexion_con_Alberquilla.jpg (mayo de 2024) · hoja a_264.jpg

2581. [alta] Cámara — encuadre de la vista
   - Captura: Fachadas blancas a varios metros: casa nº 12 con recercados y zócalo de azulejo de dibujos ocre y negro (x≈470–750, y≈290–610), ventana con persiana verde (x≈585–710), puerta de madera oscura (x≈790–890), puerta marrón (x≈340–415), y a la derecha casa nº 10 con balcón de barandilla negra (x≈970–1440, y≈30–275) y puerta de madera (x≈1050–1150).
   - Juego: Cámara pegada a una pared lisa que ocupa toda la imagen (esquina en x≈680), con solo un trozo de puerta con barrotes azules abajo a la izquierda (x≈0–430, y≈330–693) y una reja negra abajo a la derecha (x≈1160–1440, y≈370–693).

### Calle San Roque

**Vista #265** — 02_Desde_un_extremo_hacia_el_otro.jpg (mayo de 2024) · hoja a_265.jpg

2582. [alta] Geometría — separación entre la calzada y la acera de las casas
   - Captura: Una sola calzada que llega directamente al bordillo de la acera izquierda (bordillo de x≈300 a 620), sin ninguna mediana.
   - Juego: Una franja estrecha con dos líneas blancas (de x≈60 abajo a x≈720 al fondo) separa el carril de la cámara de otra calzada que discurre junto a la acera de las casas (x≈0–700).
2583. [alta] Geometría — lado derecho de la calzada
   - Captura: El asfalto sigue hacia la derecha hasta una avenida con mediana ajardinada al fondo (x≈850–1440, y≈350–500); el primer plano derecho es calzada.
   - Juego: Justo a la derecha del carril de la cámara (desde x≈870) empieza un paseo ancho de losas blancas, x≈860–1440, y≈370–693.
2584. [media] Huecos — primera casa de la izquierda (una planta)
   - Captura: Puerta de cochera metálica grande gris, x≈0–240, y≈330–600.
   - Juego: Ventana con reja, x≈0–120, y≈350–450; no hay cochera.
2585. [media] Huecos — cocheras de la casa de dos plantas de la izquierda
   - Captura: Dos puertas de cochera de madera marrón: x≈465–540 (y≈335–450) y x≈600–625 (y≈330–395).
   - Juego: Ninguna cochera: puerta verde (x≈245–325, y≈345–435) y ventanas con reja (x≈380–420 y x≈450–470).
2586. [media] Huecos — planta alta de la casa de dos plantas de la izquierda
   - Captura: Dos ventanas con balconcillo de barandilla negra, x≈385–445 (y≈240–300) y x≈510–540 (y≈280–315), sin contraventanas.
   - Juego: Balcón con ropa tendida (x≈240–345, y≈270–320), ventana con contraventanas verdes (x≈365–430, y≈250–300) y balcones pequeños (x≈485–515 y x≈535–555).
2587. [media] Zócalo — casas de la izquierda
   - Captura: Encalado hasta el suelo, sin zócalo, x≈240–560, y≈300–520.
   - Juego: Zócalo gris oscuro, x≈0–230 (y≈420–490) y x≈320–560 (y≈395–430).
2588. [media] Cubierta — casa de dos plantas de la izquierda
   - Captura: Remate recto con cornisa, sin teja visible, x≈240–560, y≈90–250.
   - Juego: Alero de teja naranja a lo largo de toda la fachada, x≈0–560, y≈165–290.
2589. [media] Calzada — color del asfalto
   - Captura: Asfalto beige-grisáceo con muchas grietas, x≈300–1440, y≈350–693.
   - Juego: Asfalto gris medio, x≈0–910.
2590. [media] Marcas viales — líneas de la calzada
   - Captura: Calzada sin marcas viales, agrietada.
   - Juego: Líneas blancas continuas (x≈60–900) y una línea discontinua (x≈380–700, y≈370–470).
2591. [media] Acera y bordillo — pavimento de la mediana de la derecha
   - Captura: Franja de pavimento rojizo y tierra en la mediana, x≈1150–1440, y≈400–500.
   - Juego: Losas blancas, x≈860–1440.
2592. [media] Vegetación — vegetación de la derecha
   - Captura: Arbustos de hoja púrpura (x≈940–1000, 1040–1080, 1220–1340) y verdes (x≈1000–1030, 1110–1185) y árboles de copa ancha (x≈1170–1440, y≈205–375) en la mediana.
   - Juego: Una palmera (x≈870–1100, y≈115–410) y un árbol redondo con naranjas (x≈1090–1440, y≈295–540).
2593. [media] Mobiliario — farolas
   - Captura: Farolas altas de fuste gris claro con un brazo curvo: x≈685–715 (y≈235–380), x≈900–925 y x≈1025–1065 (y≈215–355); poste gris alto en x≈1380–1400 (y≈0–470).
   - Juego: Farolas negras: una de dos brazos en primer plano (x≈975–1065, y≈135–430) y otras en x≈660–690 y x≈845–875.
2594. [baja] Mobiliario — banco y macetas de la acera izquierda
   - Captura: Sin banco ni macetas en la acera.
   - Juego: Banco blanco (x≈220–270, y≈415–455) y macetas (x≈0–60 y x≈330–360).
**Vista #266** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_266.jpg

2595. [alta] Geometría — volumen de dos plantas a la derecha
   - Captura: Las casas de la derecha son de una planta: tejado de teja (x≈950–1440, y≈180–310) con cielo por encima.
   - Juego: Un cuerpo de dos plantas con alero propio se alza detrás de las casas de la derecha, x≈1275–1440, y≈105–275.
2596. [media] Geometría — acera y pared de la izquierda
   - Captura: Acera izquierda ancha que en el borde inferior va de x≈150 a x≈380 (bordillo de x≈380 a 700); la pared queda separada de la cámara.
   - Juego: La pared izquierda llega hasta el borde inferior de la imagen (x≈0–640) y la acera es una franja estrecha, x≈610–740.
2597. [media] Huecos — pared encalada de la izquierda
   - Captura: Pared encalada ciega en el tramo cercano, sin puertas ni ventanas, x≈0–660, y≈80–600; solo una rejilla pequeña (x≈565–585, y≈438–446).
   - Juego: Puerta con cortina de rayas (x≈480–580, y≈375–693), placa azul (x≈400–445, y≈450–505) y ventana con reja (x≈660–685, y≈350–460).
2598. [media] Huecos — portón de madera rojiza de la derecha
   - Captura: Portón grande de madera rojiza, x≈905–945, y≈315–410.
   - Juego: En esa zona, una puerta estrecha (x≈890–905) y una ventana pequeña (x≈925–945, y≈350–380).
2599. [media] Zócalo — pared de la izquierda
   - Captura: Encalado hasta el suelo, sin zócalo, x≈0–700.
   - Juego: Zócalo ocre, x≈580–720, y≈470–640.
2600. [media] Zócalo — casas de la derecha
   - Captura: Zócalo ocre/amarillo, x≈950–1440, y≈420–560.
   - Juego: Zócalo de bloques de piedra gris, x≈1135–1440, y≈410–525.
2601. [media] Cubierta — volumen oscuro sobre el tejado de la izquierda
   - Captura: Sobre el tejado de la izquierda solo se ve cielo.
   - Juego: Un volumen azul oscuro asoma por encima del alero, x≈345–545, y≈25–190.
2602. [media] Calzada — color del asfalto
   - Captura: Asfalto beige-grisáceo claro, x≈380–1300, y≈350–693.
   - Juego: Asfalto gris medio, x≈740–1440.
2603. [media] Marcas viales — líneas de la calzada
   - Captura: Calzada sin líneas.
   - Juego: Dos líneas blancas continuas (x≈860–1020 y x≈810–1440) y una línea discontinua fina.
2604. [baja] Huecos — puerta de la casa de la derecha
   - Captura: Puerta de madera marrón, x≈1080–1130, y≈365–480.
   - Juego: Puerta beige con barrotes azules, x≈1060–1135, y≈345–445.
2605. [baja] Huecos — ventana de la casa de la derecha
   - Captura: Ventana con hoja de madera marrón, x≈1250–1290, y≈400–460.
   - Juego: Sin ventana en esa zona; solo una bajante (x≈1170–1180) y el zócalo.
2606. [baja] Cubierta — tejados de la derecha
   - Captura: Teja vieja pardo-grisácea, x≈950–1440, y≈180–310.
   - Juego: Teja naranja intenso, x≈810–1440, y≈265–335.
2607. [baja] Vegetación — macetas de la acera izquierda
   - Captura: Sin macetas.
   - Juego: Macetas con flores rojas junto a la pared, x≈670–720, y≈420–520.
2608. [baja] Mobiliario — farol de pared de la izquierda
   - Captura: Farol clásico sobre brazo de hierro en la pared, x≈560–620, y≈195–285.
   - Juego: No hay farol en ese tramo de la pared (solo uno lejano en x≈700–725).
**Vista #267** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_267.jpg

2609. [alta] Cámara — encuadre de la vista
   - Captura: Calle al aire libre: casas de una planta con tejado de teja a la izquierda (x≈0–700), con un coche plateado aparcado (x≈240–595, y≈430–693); a la derecha, casa de dos plantas con pilastras de piedra (x≈850–1060) y un portón metálico gris oscuro (x≈1165–1440, y≈260–635).
   - Juego: Cámara dentro de un recinto cerrado de paredes de ladrillo rojo con ventanas (x≈0–1430, y≈300–600), cubierto por la cara inferior de un tejado de teja (y≈0–300) y con suelo de losas; una puerta negra a la izquierda (x≈160–430, y≈360–693); no se ve la calle.

### Traseras de la Calle el Pilar

**Vista #268** — 02_Desde_un_extremo_hacia_el_otro.jpg (agosto de 2012) · hoja a_268.jpg

2610. [alta] Cámara — encuadre completo
   - Captura: Cámara en mitad de la calzada de hormigón: a la izquierda, a unos metros, una tapia de mampostería con remate de ladrillo (x≈0–440) con una casa blanca detrás, y la casa blanca de dos plantas con cochera marrón (x≈440–620); la calle se aleja hacia el centro (fuga en x≈720) y a la derecha se extiende el campo (x≈730–1440).
   - Juego: La mitad izquierda de la imagen (x≈0–775, de arriba abajo) es una pared blanca a un metro de la cámara (los granos del revoco se ven enormes); pegada a su borde hay una farola (x≈775–815) y solo a la derecha (x≈815–1440) asoman la calzada, una acera ancha y un campo amarillo.
**Vista #269** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_269.jpg

2611. [alta] Geometría — posición de la fachada izquierda respecto a la cámara
   - Captura: La cámara está en el centro de la calzada: la pared de ladrillo de la izquierda queda a unos metros, con la acera (x≈280–600 abajo) y parte de la calzada en medio; el bordillo izquierdo cae en x≈400 abajo y la calzada ocupa x≈380–1180 abajo.
   - Juego: La fachada izquierda pasa a un metro de la cámara: una reja de ventana ocupa el primer plano (x≈100–580, y≈370–693) y el bordillo izquierdo cae en el centro de la imagen (x≈735–785 abajo); la calzada solo ocupa x≈750–1200 abajo.
2612. [alta] Geometría — naves en el campo de la derecha
   - Captura: No hay edificios en la parcela: solo olivos.
   - Juego: Cinco naves blancas con puertas azules en medio del campo (x≈740–1310, y≈310–370).
2613. [alta] Color de fachada — primer edificio de la izquierda
   - Captura: Pared de ladrillo hueco rojo sin revocar, desde el alero hasta el suelo (x≈0–400, y≈150–693).
   - Juego: Fachada blanca revocada con una reja de ventana (x≈0–580).
2614. [alta] Acera y bordillo — margen derecho de la calle
   - Captura: No hay acera a la derecha: un bordillo de hormigón separa la calzada del olivar (de x≈760 al fondo a x≈1180 abajo).
   - Juego: Acera ancha de baldosa gris clara a lo largo de todo el margen derecho (x≈760–1440 en diagonal; abajo x≈1100–1440).
2615. [alta] Vegetación — parcela de la derecha
   - Captura: Olivar: olivos en filas sobre tierra rojiza con hierba (x≈780–1440, y≈290–693).
   - Juego: Campo llano amarillo sin ningún árbol (x≈760–1440, y≈345–620).
2616. [media] Color de fachada — casa de una planta con cochera (segunda a la izquierda)
   - Captura: Casa revocada en beige (x≈400–640, y≈280–590).
   - Juego: En esa zona de la fila (x≈580–720) la fachada es blanca.
2617. [media] Huecos — casa de una planta con cochera (segunda a la izquierda)
   - Captura: Portón seccional blanco de cochera muy grande (x≈445–540, y≈330–530).
   - Juego: No hay portón de cochera: solo una puerta oscura estrecha (x≈655–672, y≈365–555) y ventanas pequeñas (x≈690–705).
2618. [media] Zócalo — casa de una planta con cochera (segunda a la izquierda)
   - Captura: Aplacado de piedra en la parte baja, a la derecha del portón (x≈540–640, y≈375–470).
   - Juego: Zócalo liso marrón claro (x≈610–700, abajo).
2619. [media] Calzada — calzada
   - Captura: Hormigón claro, beige, con juntas y grietas (x≈380–1180 abajo).
   - Juego: Asfalto gris (x≈750–1200 abajo).
2620. [media] Mobiliario — farola de la acera derecha
   - Captura: No hay farolas en el lado derecho; la única visible está a la izquierda, junto a las casas (x≈637–675, y≈250–330).
   - Juego: Farola negra moderna en la acera derecha, en primer plano (x≈895–1005, y≈140–512).
2621. [baja] Cubierta — antenas de los tejados de la izquierda
   - Captura: Antenas de televisión sobre los tejados (x≈430–460, y≈235–265 y x≈575–615, y≈280–305).
   - Juego: No hay antenas.
2622. [baja] Otros — horizonte derecho
   - Captura: Lomas con monte en el horizonte derecho (x≈1000–1440, y≈270–330).
   - Juego: Horizonte llano.
**Vista #270** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_270.jpg

2623. [alta] Geometría — posición de la fachada derecha respecto a la cámara
   - Captura: La cámara está en el centro de la calzada: la tapia de la derecha queda a unos metros, con la acera (x≈740–1150 abajo) en medio; la calzada ocupa x≈380–1050 abajo.
   - Juego: La fachada derecha pasa a un metro de la cámara: una ventana enrejada ocupa el primer plano (x≈980–1440, y≈385–693); la acera derecha solo se ve en x≈720–880 y la calzada en x≈270–745 abajo.
2624. [alta] Acera y bordillo — margen izquierdo de la calle
   - Captura: No hay acera: la hierba del solar llega al borde de la calzada (x≈0–640).
   - Juego: Acera ancha de baldosa gris clara a lo largo de todo el margen izquierdo (x≈0–700 en diagonal).
2625. [media] Geometría — naves del fondo izquierdo
   - Captura: Naves bajas y abiertas con cubiertas rojizas, tras las tapias (x≈320–560, y≈320–360).
   - Juego: Naves blancas cerradas, más altas, con puertas azules (x≈285–690, y≈300–370).
2626. [media] Huecos — primer elemento de la derecha
   - Captura: Tapia encalada de bloques, ciega, sin ningún hueco (x≈880–1440, y≈320–693).
   - Juego: Fachada de casa con una ventana grande enrejada con recercado beige (x≈980–1440, y≈385–693).
2627. [media] Zócalo — casas de la derecha
   - Captura: La tapia y la casa siguiente están encaladas hasta el suelo, sin zócalo distinto (x≈770–1440).
   - Juego: Zócalo de piedra gris (x≈790–960, y≈450–693).
2628. [media] Cubierta — remate del primer elemento de la derecha
   - Captura: Sobre la tapia, placas onduladas grises de fibrocemento (x≈1070–1440, y≈300–350).
   - Juego: Alero de teja roja festoneado (x≈780–1440, y≈0–300).
2629. [media] Calzada — calzada
   - Captura: Hormigón beige con grietas (x≈380–1050 abajo).
   - Juego: Asfalto gris (x≈270–745 abajo).
2630. [media] Vegetación — solar de la izquierda
   - Captura: Hierba alta verde y matorral (x≈0–640, y≈350–693).
   - Juego: Campo llano amarillo sin hierba (x≈0–640, y≈350–610).
2631. [media] Mobiliario — farola de la acera izquierda
   - Captura: No hay farolas en el lado izquierdo (el del solar).
   - Juego: Farola negra moderna en la acera izquierda (x≈475–570, y≈160–495).
2632. [media] Muros y vallas — cerca del solar de la izquierda
   - Captura: Postes de madera con alambre y tramos de tapia de ladrillo rojo al fondo del solar (x≈0–330, y≈315–360).
   - Juego: No hay cerca ni tapias.
2633. [baja] Detalles de fachada — hilada de ladrillo de la tapia de la derecha
   - Captura: Hilada de ladrillo rojo visto a lo largo de la tapia (x≈1100–1400, y≈385–420).
   - Juego: No hay hilada de ladrillo: pared blanca lisa.
2634. [baja] Vegetación — macetas de la acera derecha
   - Captura: No se ven macetas en la acera derecha.
   - Juego: Macetas con flores rojas y rosas a lo largo de la acera derecha (x≈725–785, y≈380–495).
2635. [baja] Mobiliario — farola de brazo de la derecha
   - Captura: Farola de brazo sobre la casa de la derecha (x≈790–840, y≈215–290).
   - Juego: No hay farola en ese punto.
2636. [baja] Muros y vallas — muro blanco al final del solar
   - Captura: Muro blanco con pilares junto a la calzada, al final del solar (x≈640–690, y≈335–400).
   - Juego: No hay muro: siguen la acera y el campo.

### Travesía Luis Chamizo

**Vista #271** — 02_Desde_un_extremo_hacia_el_otro.jpg (mayo de 2024) · hoja a_271.jpg

2637. [alta] Color de fachada — edificio de tres plantas de la derecha
   - Captura: Fachada blanca revocada (x≈945–1440, y≈0–520).
   - Juego: Fachada de ladrillo rojo anaranjado (x≈900–1440, y≈0–620).
2638. [media] Color de fachada — casa de dos plantas de la izquierda
   - Captura: Paños de color beige rosado entre pilastras y bandas blancas (x≈0–640).
   - Juego: Fachada blanca lisa (x≈0–600).
2639. [media] Huecos — balcones del edificio de la derecha
   - Captura: Balcones con balaustrada blanca de obra (x≈970–1165, y≈180–290 y x≈1285–1440, y≈80–215).
   - Juego: Balcones con barandilla de hierro negra (x≈945–1010, y≈125–325 y x≈1275–1440, y≈145–295).
2640. [media] Huecos — planta baja del edificio de la derecha
   - Captura: Dos ventanas anchas con rejas de forja marrones (x≈985–1155, y≈325–445) y ninguna puerta en ese tramo.
   - Juego: Ventanas pequeñas con persiana blanca (x≈910–1000) y una puerta blanca con rejilla (x≈1085–1155, y≈355–505).
2641. [media] Huecos — persianas del edificio de la derecha
   - Captura: Ventanas de la planta segunda con persianas marrones (x≈1000–1150, y≈100–235).
   - Juego: Persianas enrollables blancas (x≈910–1150, y≈150–250).
2642. [media] Huecos — borde izquierdo de la planta baja
   - Captura: Pared beige sin hueco (x≈0–160, y≈355–600).
   - Juego: Puerta con marco metálico (x≈0–60, y≈355–693).
2643. [media] Detalles de fachada — pilastras y bandas de la casa de la izquierda
   - Captura: Pilastras y bandas blancas que enmarcan los paños de color (por ejemplo x≈290–320 y x≈445–465, de arriba abajo).
   - Juego: Sin pilastras ni bandas: paño blanco continuo.
2644. [media] Detalles de fachada — toldo naranja de la casa de la izquierda
   - Captura: No hay toldo: en esa zona (x≈0–355, y≈165–290) están la pared beige y el aparato de aire acondicionado.
   - Juego: Toldo naranja festoneado (x≈0–355, y≈165–290).
2645. [media] Zócalo — edificio de la derecha
   - Captura: Zócalo gris claro (x≈945–1440, y≈400–520).
   - Juego: Zócalo marrón oscuro (x≈900–1440, y≈400–620).
2646. [media] Acera y bordillo — acera izquierda
   - Captura: Baldosa de tono pardo con relieve de tacos (x≈340–690).
   - Juego: Baldosa gris clara con bordillo blanco (x≈260–680).
2647. [baja] Huecos — ventana de la planta baja de la casa de la izquierda
   - Captura: Ventana alta de remate en arco con reja negra (x≈320–445, y≈325–575).
   - Juego: Ventana rectangular más pequeña con reja (x≈415–500, y≈350–490).
2648. [baja] Detalles de fachada — toldo a rayas sobre el balcón izquierdo
   - Captura: No hay toldo sobre el balcón (x≈420–550, y≈95–185).
   - Juego: Toldo a rayas beige y blancas sobre el balcón (x≈420–550, y≈95–185).
2649. [baja] Zócalo — casa de la izquierda
   - Captura: Zócalo de placas de piedra gris clara, liso (x≈160–660, y≈455–693).
   - Juego: Zócalo de manchas gris oscuro (x≈300–560, y≈430–640).
2650. [baja] Cubierta — remate de la casa de la izquierda
   - Captura: Cornisa blanca con moldura ondulada, sin teja a la vista (x≈420–640, y≈0–200).
   - Juego: Alero de teja roja (x≈410–610, y≈0–225).
2651. [baja] Mobiliario — farol de pared de la izquierda
   - Captura: Farol negro de forja en la fachada izquierda (x≈640–665, y≈255–290).
   - Juego: No hay farol.
2652. [baja] Mobiliario — señales de la esquina derecha
   - Captura: Dos señales redondas rojas en la esquina de la derecha (x≈840–870, y≈335–360).
   - Juego: No hay señales.
2653. [baja] Otros — aire acondicionado de la casa de la izquierda
   - Captura: Gran unidad exterior de aire acondicionado LG (x≈0–330, y≈190–355).
   - Juego: No hay aparato.
2654. [baja] Otros — antena parabólica de la izquierda
   - Captura: No hay antena parabólica en la fachada izquierda (x≈565–595, y≈325–355 es pared).
   - Juego: Antena parabólica gris en la fachada (x≈565–595, y≈325–355).
**Vista #272** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_272.jpg

2655. [alta] Color de fachada — edificio detrás de la tapia izquierda
   - Captura: Edificio de ladrillo visto marrón oscuro (x≈80–435, y≈215–305).
   - Juego: Casa blanca de dos plantas (x≈0–440, y≈195–310).
2656. [media] Geometría — edificio de la esquina derecha
   - Captura: Un muro alto y ciego, de unas dos plantas de altura, cuyo borde superior baja desde y≈55 en x≈830 hasta y≈185 en x≈1440.
   - Juego: Casa de una sola planta (alero en y≈230–290) con un volumen blanco retranqueado encima (x≈925–1335, y≈115–265).
2657. [media] Color de fachada — edificio de la esquina derecha
   - Captura: Revoco crema-beige (x≈830–1440).
   - Juego: Blanco (x≈800–1440).
2658. [media] Huecos — edificio de la esquina derecha
   - Captura: Paño ciego, sin ventanas (x≈830–1440).
   - Juego: Dos ventanas grandes con reja negra (x≈980–1110, y≈355–585 y x≈1240–1330, y≈355–535) y otra en el borde (x≈1420–1440).
2659. [media] Huecos — frente izquierdo cercano
   - Captura: Tapia blanca baja y larga (x≈0–420, y≈300–500) con una sola puerta de madera (x≈105–180, y≈360–475).
   - Juego: Fachadas de casas de una planta con ventanas de persiana blanca (x≈175–235 y x≈355–395) y puertas (x≈450–475 y x≈540–552).
2660. [media] Zócalo — edificio de la esquina derecha
   - Captura: El muro grande llega liso hasta el suelo; solo el frente a la calle tiene una franja rojiza abajo (x≈750–830, y≈520–693).
   - Juego: Zócalo gris continuo (x≈800–1440, y≈500–693).
2661. [media] Cubierta — edificio de la esquina derecha
   - Captura: Remate de tejas en caballete del mismo color crema que el muro (x≈830–1440, y≈55–185).
   - Juego: Alero de teja roja festoneado (x≈800–1440, y≈230–290).
2662. [media] Cubierta — frente izquierdo cercano
   - Captura: La tapia no tiene tejado: remate plano (x≈0–420, y≈300–325).
   - Juego: Tejados de teja roja sobre las casas (x≈0–560, y≈300–330).
2663. [media] Cubierta — edificio detrás de la tapia izquierda
   - Captura: Cubierta plana (x≈80–435, y≈215–230).
   - Juego: Tejado de teja roja a dos aguas (x≈0–440, y≈195–290).
2664. [media] Marcas viales — calzada
   - Captura: Asfalto sin marcas.
   - Juego: Dos líneas blancas longitudinales (x≈275–610 y x≈525–670).
2665. [media] Acera y bordillo — acera derecha
   - Captura: Baldosa de tacos color terracota claro (x≈590–790 abajo).
   - Juego: Baldosa gris clara lisa con bordillo blanco (x≈610–800 abajo).
2666. [media] Acera y bordillo — acera izquierda
   - Captura: Acera estrecha junto a la tapia (x≈0–290, y≈460–540).
   - Juego: Acera ancha gris clara (x≈0–560, y≈400–550).
2667. [media] Mobiliario — contenedores de la izquierda
   - Captura: Fila de contenedores amarillos, uno azul y dos verdes junto al bordillo izquierdo (x≈275–520, y≈375–470).
   - Juego: No hay contenedores.
2668. [baja] Detalles de fachada — bajante de la esquina derecha
   - Captura: No hay bajante en la esquina.
   - Juego: Bajante blanca vertical en la esquina (x≈780–800, y≈280–660).
2669. [baja] Otros — cables aéreos
   - Captura: Haz de cables negros que baja desde arriba junto a la esquina derecha (x≈730–760, y≈0–260).
   - Juego: No hay cables.
**Vista #273** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_273.jpg

2670. [alta] Cámara — encuadre completo
   - Captura: Calle recta vista a lo largo: casas blancas a la izquierda (x≈0–720), muro gris de bloques con portón metálico a la derecha (x≈745–1440), coches aparcados y la calle que se aleja hacia el centro (fuga en x≈720).
   - Juego: La cámara está de cara a una pared blanca a menos de un metro que llena casi todo el encuadre (x≈0–1260), con una placa de calle azul y blanca («…LA CONSTITUCIÓN») arriba (x≈700–1130, y≈0–130); solo en la franja derecha (x≈1260–1440) se ven una calzada y casas blancas.
**Vista #274** — 05_Continuacion_sur.jpg (mayo de 2024) · hoja a_274.jpg

2671. [alta] Geometría — edificio del bar (izquierda) y cruce del primer plano
   - Captura: El edificio del bar corre junto a la cámara por la izquierda, desde el borde de la imagen hasta x≈690 (un balcón queda casi encima, x≈200–340, y≈85–220), con su acera en el primer plano izquierdo (x≈0–400, y≈540–693).
   - Juego: En el primer plano izquierdo hay una calle transversal (calzada x≈0–620, y≈470–693, con un coche en x≈0–85) y el edificio queda delante, con su esquina en x≈575; su fachada a la calle principal solo ocupa x≈575–770.
2672. [alta] Geometría — altura del edificio del bar
   - Captura: Dos plantas: el bajo del bar y una planta alta con ventanas, aire acondicionado y balcón (x≈330–690), con la cornisa justo encima (de y≈0 en x≈380 a y≈230 en x≈690).
   - Juego: Tres plantas: bajo con cierres metálicos y dos plantas de ventanas encima (x≈270–770, hasta el borde superior).
2673. [alta] Otros — terraza del bar
   - Captura: Terraza cubierta junto al bordillo: estructura de perfiles blancos con toldos y cortinas granates (x≈295–785, y≈265–660).
   - Juego: No hay terraza: solo un toldo a rayas verdes y blancas pegado a la fachada (x≈295–530, y≈340–400) y otro pequeño (x≈700–770, y≈345–370).
2674. [media] Color de fachada — edificio del bar
   - Captura: Planta alta revocada en beige grisáceo (x≈330–690, y≈0–300).
   - Juego: Todas las plantas blancas (x≈270–770).
2675. [media] Acera y bordillo — acera derecha
   - Captura: Acera de baldosa rojiza (x≈1180–1440, y≈430–510).
   - Juego: Acera gris clara con bordillo blanco (x≈990–1440, y≈380–560).
2676. [media] Vegetación — árbol grande de la derecha
   - Captura: Árbol grande y frondoso en el primer plano derecho (x≈1150–1440, y≈130–400).
   - Juego: Solo un arbolito redondo (x≈1250–1350, y≈330–370).
2677. [media] Mobiliario — poste del primer plano izquierdo
   - Captura: Poste metálico gris alto en la acera izquierda, en primer plano (x≈355–385, y≈0–570).
   - Juego: No hay poste ahí; en cambio hay una farola negra moderna en la esquina, en el centro de la imagen (x≈820–970, y≈55–545).
2678. [media] Mobiliario — farolas del fondo
   - Captura: Farolas grises de báculo con el brazo curvo (x≈770–800, y≈245–330; x≈1015–1030, y≈265–370; x≈1145–1170, y≈265–380).
   - Juego: Farolas negras de brazo recto horizontal (x≈990–1050, y≈290–390).
2679. [media] Muros y vallas — muretes de la acera derecha
   - Captura: Muretes bajos de mampostería a lo largo de la acera derecha (x≈1100–1440, y≈385–470).
   - Juego: Seto verde recortado (x≈1080–1440, y≈365–450), sin muretes.
2680. [baja] Calzada — calzada
   - Captura: Asfalto de tono pardo claro (x≈400–1440 abajo).
   - Juego: Asfalto gris (x≈880–1440 abajo).
2681. [baja] Mobiliario — contenedores verdes de la derecha
   - Captura: Dos contenedores verdes de reciclaje junto al bordillo derecho (x≈1020–1100, y≈370–425).
   - Juego: No hay contenedores; en esa zona hay seto.
2682. [baja] Mobiliario — señal de STOP
   - Captura: Señal de STOP al fondo a la derecha (x≈1033–1048, y≈352–365).
   - Juego: No hay señal.

### Calle Almendralejo

**Vista #275** — 02_Junto_al_parque.jpg (mayo de 2024) · hoja a_275.jpg

2683. [alta] Geometría — franja separadora de la izquierda
   - Captura: La cámara va por un vial separado de la carretera de la izquierda por una franja estrecha con bordillos y hierba seca (x≈240–520, y≈450–620).
   - Juego: No hay franja: la calzada sigue sin separación hasta el borde izquierdo (x≈0–600, y≈420–693).
2684. [alta] Geometría — casa de la derecha
   - Captura: Casa de dos plantas con terraza en la planta alta: balaustrada blanca y cubierta sobre pilares (x≈790–1090, y≈235–330); delante, a pie de calle, un muro alto ciego (x≈830–1160, y≈320–455).
   - Juego: Edificio de una planta con tejado de teja y locales (x≈945–1380, y≈295–435) y un bloque blanco de dos plantas detrás (x≈900–1230, y≈240–340); sin terraza ni balaustrada.
2685. [alta] Geometría — nave del fondo derecho
   - Captura: Nave industrial con cubierta clara (x≈1165–1440, y≈295–390).
   - Juego: No hay nave: tejados de teja de otras casas (x≈1290–1440, y≈305–340) y un muro gris (x≈1380–1440, y≈340–375).
2686. [alta] Otros — solar de la derecha
   - Captura: Solar con hierba y matorral (x≈900–1440, y≈410–693).
   - Juego: Explanada pavimentada de baldosa gris clara (x≈770–1440, y≈360–693).
2687. [media] Geometría — isleta del cruce de la izquierda
   - Captura: Isleta estrecha con bordillo pintado de rojo y blanco (x≈100–480, y≈390–420).
   - Juego: Gran isleta triangular pavimentada en piedra clara (x≈230–620, y≈385–460).
2688. [media] Color de fachada — casa de la derecha
   - Captura: Revoco crema-beige (x≈790–1160).
   - Juego: Blanco (x≈900–1380).
2689. [media] Huecos — frente a la calle de la casa de la derecha
   - Captura: Muro alto ciego a pie de calle (x≈830–1160, y≈320–455).
   - Juego: Cierres metálicos grises, ventanas y puertas de locales (x≈1040–1380, y≈330–435).
2690. [media] Cubierta — casa blanca del fondo central
   - Captura: Casa blanca de dos plantas rematada en azotea con pretil, sin teja (x≈475–590, y≈305–370).
   - Juego: Casa de dos plantas con tejado de teja roja (x≈555–710, y≈305–365).
2691. [media] Acera y bordillo — acera derecha
   - Captura: Acera estrecha de baldosa de tacos beige (de x≈800 al fondo a x≈1260 abajo).
   - Juego: Pavimento gris claro liso que se funde con la explanada (x≈770–1440).
2692. [media] Vegetación — árboles del parque
   - Captura: Árboles altos y frondosos de hoja ancha y coníferas oscuras y esbeltas (x≈0–500, y≈90–360).
   - Juego: Pinos piñoneros de copa plana y arbustos redondos (x≈0–560, y≈20–380).
2693. [media] Mobiliario — farolas del cruce
   - Captura: Farolas grises de doble brazo curvo (x≈400–470, y≈200–385 y x≈678–725, y≈252–370).
   - Juego: Farolas negras de un solo brazo recto (x≈480–500, y≈290–375 y x≈745–785, y≈270–405).
2694. [media] Mobiliario — báculo del primer plano derecho
   - Captura: Báculo gris alto en la acera derecha, en primer plano (x≈888–910, y≈0–520).
   - Juego: No hay poste en ese punto.
2695. [media] Muros y vallas — cerramiento del parque
   - Captura: Murete blanco bajo a lo largo del parque (x≈0–480, y≈355–400).
   - Juego: Seto verde (x≈0–470, y≈360–415), sin murete.
2696. [baja] Detalles de fachada — toldos de la derecha
   - Captura: No hay toldos.
   - Juego: Toldos a rayas rosas y blancas (x≈900–1030, y≈340–360).
2697. [baja] Cubierta — chimeneas de la casa de la derecha
   - Captura: Dos chimeneas: una de obra (x≈1045–1065, y≈220–265) y un tubo metálico (x≈1115–1135, y≈225–320).
   - Juego: Ninguna chimenea.
2698. [baja] Marcas viales — flechas del vial
   - Captura: Vial sin flechas pintadas.
   - Juego: Flechas blancas pintadas en la calzada (x≈630–740, y≈385–415).
2699. [baja] Mobiliario — señal de dirección prohibida
   - Captura: Señal roja de dirección prohibida en la isleta (x≈272–310, y≈310–405).
   - Juego: No hay señal.
2700. [baja] Mobiliario — sombrillas del fondo
   - Captura: No se ven sombrillas.
   - Juego: Sombrillas azules (x≈780–840, y≈345–355).
2701. [baja] Muros y vallas — muro de ladrillo del solar
   - Captura: Muro de ladrillo rojo medio caído junto al solar (x≈1155–1230, y≈320–410).
   - Juego: No existe.
**Vista #276** — 03_Curva_y_acceso_occidental.jpg (mayo de 2024) · hoja a_276.jpg

2702. [alta] Cámara — encuadre completo
   - Captura: Calle abierta: a la izquierda casas de dos plantas rosadas con cocheras (x≈0–620), la calzada al centro y a la derecha (x≈520–1440), y a la derecha un gran silo beige (x≈1000–1440) y una nave blanca con zócalo pintado.
   - Juego: La cámara está dentro de un edificio: paredes blancas interiores a ambos lados (x≈0–505 y x≈540–1440), la cara inferior de las tejas rojas hace de techo (y≈0–265) y solo una rendija (x≈505–540) deja ver el exterior.
**Vista #277** — 04_Hacia_San_Gines.jpg (mayo de 2024) · hoja a_277.jpg

2703. [alta] Geometría — anchura de la calzada
   - Captura: Calzada ancha, con coches aparcados a ambos lados: abajo va de x≈240 a x≈1250 (donde empieza el seto).
   - Juego: Calzada estrecha: abajo va de x≈220 a x≈800.
2704. [alta] Geometría — nave al otro lado de la mediana
   - Captura: Nave industrial con grandes portones azules y muro blanco (x≈1160–1440, y≈200–420).
   - Juego: Casas blancas de una planta con tejado de teja y ventanas con rejas verdes (x≈1160–1440, y≈295–440).
2705. [alta] Color de fachada — primera casa de la izquierda
   - Captura: Revoco beige crema (x≈0–445).
   - Juego: Ladrillo rojo visto (x≈0–445).
2706. [alta] Color de fachada — tercera casa de la izquierda
   - Captura: Blanca (x≈570–615).
   - Juego: Ladrillo rojo (x≈550–590).
2707. [alta] Vegetación — naranjos de la acera izquierda
   - Captura: No hay árboles en la acera izquierda.
   - Juego: Hilera de naranjos en alcorques (x≈0–425, x≈470–610, x≈615–680).
2708. [alta] Vegetación — seto de la mediana
   - Captura: Seto denso y continuo en la mediana (x≈740–1440, y≈365–680).
   - Juego: No hay seto: la mediana es una explanada pavimentada de baldosa clara (x≈720–1440, y≈360–693).
2709. [media] Color de fachada — segunda casa de la izquierda
   - Captura: Revoco color salmón (x≈445–570).
   - Juego: Blanca (x≈445–550).
2710. [media] Vegetación — árboles de la mediana
   - Captura: Árboles podados de tronco encalado (x≈830–1200, y≈170–495) y palmeras altas (x≈730–890, y≈220–360).
   - Juego: Naranjos de copa redonda (x≈785–1205, y≈320–440), sin palmeras.
2711. [baja] Marcas viales — bordillos pintados
   - Captura: Bordillos sin pintar.
   - Juego: Línea amarilla sobre los bordillos de ambos lados (x≈200–560 y x≈720–850).
2712. [baja] Otros — aire acondicionado de la primera casa de la izquierda
   - Captura: Aparato de aire acondicionado en la planta alta (x≈240–335, y≈215–275).
   - Juego: No hay aparato.
**Vista #278** — 05_Tramo_este_en_sentido_contrario.jpg (mayo de 2024) · hoja a_278.jpg

2713. [alta] Geometría — anchura de la calzada
   - Captura: Calzada ancha, con coches aparcados a ambos lados: abajo va de x≈230 a x≈1250.
   - Juego: Calzada estrecha: abajo va de x≈360 a x≈980, y la acera derecha es mucho más ancha (x≈980–1440).
2714. [alta] Geometría — nave al otro lado de la mediana
   - Captura: Nave larga blanca con zócalo azul y amarillo y puertas azules (x≈0–530, y≈240–445).
   - Juego: Casas blancas de una planta con tejado de teja y ventanas enrejadas (x≈0–575, y≈305–420).
2715. [alta] Color de fachada — casas del fondo derecho
   - Captura: Casas beige y blancas (x≈735–850).
   - Juego: Una casa de ladrillo rojo (x≈795–825) entre casas blancas.
2716. [alta] Vegetación — naranjos de la acera derecha
   - Captura: Ningún árbol en la acera derecha.
   - Juego: Naranjo grande en primer plano (x≈855–1300, y≈280–590) y más naranjos al fondo de la misma acera (x≈720–810).
2717. [alta] Vegetación — seto de la mediana
   - Captura: Seto denso y continuo en la mediana (x≈0–620, y≈380–620).
   - Juego: No hay seto: la mediana es una explanada pavimentada (x≈0–700, y≈360–693).
2718. [media] Color de fachada — primera casa de la derecha (planta baja)
   - Captura: Planta baja blanca (x≈935–1440, y≈180–545).
   - Juego: Planta baja revestida de verde claro con lamas horizontales (x≈1200–1440, y≈335–650).
2719. [media] Color de fachada — segunda casa de la derecha
   - Captura: Revoco salmón (x≈850–935, y≈140–410).
   - Juego: Ladrillo rojo visto con persianas blancas (x≈890–1150).
2720. [media] Huecos — primera casa de la derecha
   - Captura: Gran cierre blanco de barrotes ondulados en la planta baja (x≈1165–1440, y≈285–545) y un óculo redondo arriba (x≈1040–1075, y≈120–160).
   - Juego: Sin cierre de barrotes ni óculo; solo una ventana con marco marrón y macetas en la planta alta (x≈1290–1410, y≈20–190).
2721. [media] Vegetación — árboles de la mediana
   - Captura: Árboles podados de tronco encalado (x≈240–390 y x≈480–570) y palmeras altas (x≈485–690, y≈200–370).
   - Juego: Naranjos de copa redonda (x≈430–660, y≈330–395) y ninguna palmera en la mediana.
2722. [baja] Marcas viales — bordillos pintados
   - Captura: Bordillos sin pintar.
   - Juego: Línea amarilla sobre los bordillos (x≈500–600 y x≈820–900).
2723. [baja] Mobiliario — farol de la segunda casa de la derecha
   - Captura: Farol negro de forja en la fachada (x≈880–915, y≈210–260).
   - Juego: No hay farol.
2724. [baja] Otros — aire acondicionado de la primera casa de la derecha
   - Captura: Aparato de aire acondicionado (x≈1050–1130, y≈280–330).
   - Juego: No hay aparato.

### Calle Puerta del Sol

**Vista #279** — 02_Desde_un_extremo_hacia_el_otro.jpg (mayo de 2024) · hoja a_279.jpg

2725. [alta] Geometría — edificio largo del fondo izquierdo
   - Captura: Edificio largo de una planta con tejado de teja y muros de ladrillo (x≈0–290, y≈295–375).
   - Juego: No existe: en esa zona hay coches aparcados (x≈0–120) y la explanada.
2726. [alta] Acera y bordillo — margen derecho
   - Captura: No hay acera: bordillo y cuneta con hierba (x≈740–1440, y≈350–693).
   - Juego: Acera ancha de baldosa gris clara (x≈720–1440 en diagonal).
2727. [alta] Vegetación — huerto de la derecha
   - Captura: Huerto de árboles frutales en filas sobre tierra rojiza arada (x≈770–1440, y≈320–430), con un camino de tierra delante (x≈760–1440, y≈350–540).
   - Juego: Campo llano amarillo sin árboles (x≈740–1440, y≈350–660); solo una hilera de árboles en el horizonte (x≈1080–1440, y≈343–360).
2728. [alta] Otros — terreno de la izquierda
   - Captura: Campo de hierba seca y verde a la izquierda de una acera estrecha (x≈0–640, y≈360–600).
   - Juego: Explanada pavimentada de baldosa clara (x≈0–700, y≈360–680).
2729. [media] Color de fachada — casa de dos plantas del fondo izquierdo
   - Captura: Casa beige con placas solares en la cubierta (x≈230–380, y≈295–360).
   - Juego: Casa blanca con tejado de teja roja (x≈225–360, y≈305–360).
2730. [media] Vegetación — árboles de la izquierda
   - Captura: No hay árboles en el campo de la izquierda.
   - Juego: Naranjos en la explanada (x≈115–280, y≈310–405 y x≈465–515, y≈340–375).
2731. [media] Mobiliario — farola de la acera izquierda
   - Captura: Báculo gris alto en la acera izquierda, cerca de la cámara (x≈475–490, y≈0–455).
   - Juego: Farola negra de brazo recto, más baja y más lejos (x≈535–580, y≈260–412).
2732. [media] Muros y vallas — tapia de ladrillo del fondo
   - Captura: Tapia baja de ladrillo rojo al final del campo (x≈505–690, y≈335–358).
   - Juego: No hay tapia.
**Vista #280** — 03_Tramo_intermedio.jpg (mayo de 2024) · hoja a_280.jpg

2733. [alta] Geometría — posición de la calzada respecto a la cámara
   - Captura: La cámara está en la calzada: el asfalto ocupa todo el primer plano (abajo x≈230–1300) y el bordillo derecho pasa en diagonal por x≈930–1440.
   - Juego: Bajo la cámara y en toda la parte inferior derecha hay campo amarillo (x≈640–1440, y≈350–693); la calzada queda a la izquierda (abajo x≈0–500) y una franja de acera (x≈490–660, y≈510–693) aparece cortada por el campo.
2734. [alta] Otros — terreno de la izquierda
   - Captura: Solar de tierra con hierbas tras la esquina (x≈0–700, y≈370–440).
   - Juego: Explanada pavimentada de baldosa clara (x≈0–690, y≈360–425).
2735. [media] Geometría — edificios del fondo derecho
   - Captura: Edificio comercial oscuro con letrero, casa blanca con tejado de teja y silos (x≈1040–1350, y≈295–340).
   - Juego: Nave blanca larga con puertas azules (x≈1010–1405, y≈322–357).
2736. [media] Cubierta — edificio blanco del fondo
   - Captura: Volumen blanco ciego rematado en plano, sin teja (x≈520–700, y≈300–375).
   - Juego: Casa blanca de dos plantas con tejado de teja roja y ventanas (x≈510–655, y≈310–365).
2737. [media] Marcas viales — paso de peatones del cruce izquierdo
   - Captura: Paso de cebra en la calle transversal de la izquierda (x≈130–590, y≈450–530).
   - Juego: Sin paso de cebra; solo una línea blanca (x≈0–250, y≈445).
2738. [media] Marcas viales — líneas de la calzada del fondo
   - Captura: Sin marcas longitudinales.
   - Juego: Dos líneas blancas longitudinales en la calzada del fondo (x≈575–700, y≈365–410).
2739. [media] Vegetación — árboles de la izquierda
   - Captura: Sin árboles en el solar.
   - Juego: Árboles de copa redonda (x≈0–95, x≈100–240, x≈345–475), una palmera (x≈300–410, y≈285–330) y un ciprés (x≈600–620, y≈265–380).
2740. [media] Vegetación — terreno de la derecha
   - Captura: Pradera verde con flores amarillas y olivar al fondo (x≈1050–1440, y≈330–470).
   - Juego: Campo amarillo sin árboles (x≈700–1440, y≈350–693).
2741. [media] Mobiliario — farola de la esquina izquierda
   - Captura: Báculo gris alto en la esquina izquierda (x≈190–205, y≈170–440).
   - Juego: No hay farola en esa zona.
2742. [media] Muros y vallas — tapias del fondo izquierdo
   - Captura: Tapia larga de bloques de hormigón (x≈130–520, y≈330–380) y otra de ladrillo rojo (x≈0–130, y≈350–380).
   - Juego: No hay tapias: en su lugar, casas blancas de una planta con tejado de teja (x≈0–510, y≈315–365).
2743. [baja] Mobiliario — contenedor de la esquina izquierda
   - Captura: Contenedor verde en la esquina izquierda (x≈245–330, y≈398–460).
   - Juego: No hay contenedor.
2744. [baja] Mobiliario — señal de la esquina
   - Captura: Señal azul de paso de peatones (x≈605–620, y≈343–440).
   - Juego: Señal roja de dirección prohibida (x≈685–710, y≈335–435).
**Vista #281** — 04_Desde_el_extremo_opuesto.jpg (mayo de 2024) · hoja a_281.jpg

2745. [alta] Geometría — fondo derecho
   - Captura: Tapia larga de bloques de hormigón gris (x≈900–1440, y≈295–420), sin casas delante.
   - Juego: Fila de casas blancas de una planta con tejado de teja roja y puertas verdes (x≈880–1440, y≈315–410).
2746. [alta] Acera y bordillo — margen izquierdo
   - Captura: No hay acera: bordillo y campo de tierra (x≈0–700).
   - Juego: Acera de baldosa gris clara (x≈0–700 en diagonal; abajo x≈0–330).
2747. [alta] Otros — terreno de la derecha
   - Captura: Campo de hierbas verdes a la derecha de la acera (x≈780–1440, y≈360–693).
   - Juego: Explanada pavimentada de baldosa clara (x≈880–1440, y≈355–693).
2748. [media] Geometría — edificio del fondo izquierdo
   - Captura: Edificio bajo y largo con tejado rojizo (x≈0–190, y≈305–330).
   - Juego: Naves blancas con puertas azules (x≈0–225, y≈320–365).
2749. [media] Cubierta — edificio blanco del fondo derecho
   - Captura: Edificio blanco de muros ciegos rematado en plano (x≈760–900, y≈315–365).
   - Juego: Casa blanca de dos plantas con tejado de teja roja (x≈775–870, y≈320–360).
2750. [media] Marcas viales — líneas de la calzada
   - Captura: Asfalto sin marcas (solo una tapa de registro, x≈615–665, y≈525–555).
   - Juego: Dos líneas blancas longitudinales (x≈480–720 y x≈750–910 abajo).
2751. [media] Acera y bordillo — acera derecha
   - Captura: Acera de baldosa de tacos ocre con tapas de registro (x≈760–1220, y≈360–693).
   - Juego: Pavimento gris claro liso, continuo con una gran explanada (x≈760–1440).
2752. [media] Vegetación — campo de la izquierda
   - Captura: Tierra parda con hierbajos dispersos (x≈0–700, y≈345–693).
   - Juego: Campo llano amarillo uniforme (x≈0–690, y≈350–650).
2753. [media] Vegetación — árboles de la derecha
   - Captura: Ningún árbol a la derecha.
   - Juego: Árbol grande de copa redonda (x≈1200–1440, y≈255–425) y un pino (x≈1170–1220, y≈265–315).
2754. [media] Mobiliario — báculo del primer plano derecho
   - Captura: Báculo gris alto en primer plano a la derecha (x≈1185–1245, y≈0–680).
   - Juego: No hay poste ahí; hay una farola negra más lejos (x≈815–875, y≈235–435).

### Carretera de Don Benito a Portugal por Almendralejo

**Vista #282** — 02_Entrada_desde_el_oeste.jpg (mayo de 2024) · hoja a_282.jpg

2755. [media] Geometría — sección de la carretera
   - Captura: Carretera de dos carriles sin arcén: la cámara va por el carril derecho, la línea discontinua central pasa a su izquierda (abajo x≈440) y el asfalto acaba junto a la línea de borde derecha (abajo x≈870).
   - Juego: Carretera más ancha: la línea discontinua pasa justo bajo la cámara (abajo x≈715–750) y los bordes quedan en x≈150 y x≈1330 abajo.
2756. [media] Marcas viales — líneas de la carretera
   - Captura: Solo la línea central discontinua y dos líneas de borde continuas pegadas al borde del asfalto (izquierda hacia x≈0–660, derecha x≈720–860).
   - Juego: Línea central discontinua y dos líneas continuas separadas más de un metro de los bordillos, con arcenes anchos (abajo x≈440 y x≈1030).
2757. [media] Acera y bordillo — bordes de la carretera
   - Captura: Sin bordillos: el asfalto termina en márgenes de tierra y hierba.
   - Juego: Bordillos blancos elevados a ambos lados (de x≈150 a x≈660 y de x≈1330 a x≈760).
2758. [media] Vegetación — campo de la izquierda
   - Captura: Campo verde y amarillo de cereal y hierbas (x≈0–650, y≈340–600), con la cuneta verde.
   - Juego: Tierra desnuda anaranjada con una cuña amarilla (x≈0–660, y≈350–693).
2759. [media] Vegetación — margen derecho
   - Captura: Cuneta ancha de hierba verde junto al asfalto (x≈730–1440, y≈350–693) y detrás un campo arado pardo.
   - Juego: La tierra anaranjada llega hasta el bordillo, sin hierba (x≈780–1440).
2760. [media] Mobiliario — farolas
   - Captura: No hay farolas a lo largo de la carretera.
   - Juego: Farolas negras en el margen derecho y al fondo (x≈665–680, y≈320–360 y x≈760–785, y≈295–385).
2761. [baja] Calzada — firme
   - Captura: Asfalto gastado, lleno de grietas y parches (x≈0–870 abajo).
   - Juego: Asfalto gris liso y uniforme.
2762. [baja] Vegetación — árboles del campo izquierdo
   - Captura: No hay árboles en el campo de la izquierda.
   - Juego: Dos árboles de copa plana (x≈30–110, y≈325–355 y x≈330–365, y≈335–352).
2763. [baja] Mobiliario — señales del margen izquierdo
   - Captura: Señal redonda de espaldas en el margen izquierdo (x≈397–432, y≈333–430) y un cartel azul al fondo (x≈603–640, y≈337–365).
   - Juego: No hay señales.
2764. [baja] Otros — horizonte derecho
   - Captura: Sierras en el horizonte derecho (x≈1070–1440, y≈325–340).
   - Juego: Horizonte llano.
**Vista #283** — 03_Enlace_entre_rotondas.jpg (mayo de 2024) · hoja a_283.jpg

2765. [alta] Cámara — encuadre completo
   - Captura: La cámara va por la calzada de la EX-105: la carretera sale del primer plano (abajo x≈0–1200) y se aleja recta (fuga x≈680), con bionda y señales (triángulo de glorieta y límite 40) a la derecha (x≈965–1055, y≈250–530) y una nave blanca larga a la izquierda (x≈0–520, y≈305–400).
   - Juego: La cámara está en medio de un campo de surcos verdes con un camino amarillo (x≈0–1440, y≈355–693); la carretera no sale del primer plano sino que pasa lejos a la derecha (x≈760–1440, y≈350–455), con casas detrás; a la izquierda, una nave blanca larga (x≈0–600, y≈295–365).
**Vista #284** — 04_Entrada_a_la_travesia.jpg (mayo de 2024) · hoja a_284.jpg

2766. [alta] Color de fachada — segunda casa de la izquierda
   - Captura: Casa blanca de dos plantas (x≈295–500, y≈220–400).
   - Juego: Casa de ladrillo rojo de dos plantas con balcones (x≈230–515, y≈245–410).
2767. [alta] Acera y bordillo — margen derecho
   - Captura: No hay acera: el seto está pegado a la calzada (de x≈780 al fondo a x≈1100 abajo).
   - Juego: Acera ancha de baldosa gris clara entre la calzada y el seto (x≈800–1440, y≈370–693).
2768. [alta] Vegetación — seto de la mediana izquierda
   - Captura: Seto continuo en la mediana que separa la carretera del vial de servicio de la izquierda (x≈0–630, y≈365–560).
   - Juego: No hay seto: la mediana es una franja pavimentada (x≈270–700, y≈360–600).
2769. [media] Detalles de fachada — primera casa de la izquierda (ladrillo)
   - Captura: Fachada con recercados y pilastras de ladrillo visto, ventanas en arco (x≈130–270, y≈235–300) y balcón corrido con barandilla y macetas (x≈95–300, y≈285–320).
   - Juego: Fachada blanca lisa con ventanas rectangulares de persiana blanca y macetas (x≈60–155) y alero de teja; sin ladrillo, arcos ni balcón corrido (x≈0–245).
2770. [media] Cubierta — segunda casa de la izquierda
   - Captura: Tejado de teja roja con chimenea (x≈295–500, y≈220–265).
   - Juego: Cubierta plana, sin teja ni chimenea (x≈230–515, y≈245–270).
2771. [media] Marcas viales — línea central
   - Captura: Doble línea continua en el centro (de x≈430 abajo a x≈700 al fondo).
   - Juego: Línea central discontinua (x≈705–735) y dos líneas continuas a los lados (abajo x≈390–700 y x≈765–990).
2772. [media] Marcas viales — bandas transversales
   - Captura: Dos bandas transversales pintadas en damero cruzando la calzada (x≈330–920, y≈455–505).
   - Juego: No hay bandas transversales.
2773. [media] Vegetación — palmera de la mediana izquierda
   - Captura: Palmera alta en la mediana izquierda (x≈485–595, y≈120–380).
   - Juego: No hay palmera en la mediana; en su lugar, una farola.
2774. [media] Vegetación — seto del margen derecho
   - Captura: Seto alto y continuo junto al borde de la calzada (x≈780–1440, y≈365–680).
   - Juego: Seto bajo retirado tras la acera (x≈900–1440, y≈365–440).
2775. [media] Vegetación — árboles del parque de la derecha
   - Captura: Árboles frondosos de hoja ancha, altos y densos (x≈880–1340, y≈90–420).
   - Juego: Árboles de copa en sombrilla estilizada sobre césped (x≈1000–1440, y≈130–390).
2776. [media] Mobiliario — farolas de la mediana
   - Captura: Báculos grises altos con remate en T (x≈595–620, y≈245–365 y x≈795–820, y≈240–365).
   - Juego: Farolas negras de un brazo recto (x≈415–530, y≈155–495 y x≈585–620, y≈270–405).
2777. [baja] Mobiliario — señal triangular del fondo
   - Captura: Señal triangular de peligro al fondo a la derecha (x≈795–815, y≈325–345).
   - Juego: No hay señal.
2778. [baja] Muros y vallas — pilares de ladrillo del parque
   - Captura: Pilares de ladrillo rojo en la entrada del parque (x≈1285–1320, y≈385–455 y x≈895–910, y≈340–380).
   - Juego: No hay pilares.
**Vista #285** — 05_Vista_hacia_el_enlace_occidental.jpg (mayo de 2024) · hoja a_285.jpg

2779. [alta] Cámara — encuadre completo
   - Captura: La cámara va por la calzada de la EX-105, junto a la bionda de la izquierda: la carretera sale del primer plano (abajo x≈480–1300) y se aleja recta (fuga x≈680); a la izquierda, bionda, un gran cartel de espaldas (x≈475–600, y≈290–365) y un vial paralelo; a la derecha, un campo en hileras y una tapia blanca larga (x≈1160–1440, y≈300–410).
   - Juego: La cámara está dentro del campo de cultivo, a la derecha de la carretera: el primer plano es todo surcos verdes y pardos (x≈0–1440, y≈360–693); la carretera queda a la izquierda sin pasar bajo la cámara (su borde derecho va de x≈0, y≈600 a x≈650, y≈355) y a la derecha se alza una nave blanca enorme (x≈1130–1440, y≈185–405).
**Vista #286** — 06_Rotonda_del_noroeste.jpg (mayo de 2024) · hoja a_286.jpg

2780. [alta] Cámara — encuadre completo
   - Captura: La cámara va por la calzada de la EX-105, que sale del primer plano (abajo x≈0–1200) y gira a la izquierda (x≈590–700, y≈360–400); a la izquierda, una isleta cebreada con un cartel de dirección (x≈0–130, y≈400–480); a la derecha, una bionda curva (x≈590–1440) y un báculo alto (x≈780–795).
   - Juego: La cámara está en medio de unas parcelas de tierra amarilla y parda (x≈0–1440, y≈385–693); la carretera más cercana cruza lejos de lado a lado (y≈360–435), con unas letras grandes «GUAREÑA» a la izquierda (x≈220–450, y≈330–375) y una nave blanca a la derecha (x≈1180–1440, y≈310–365).
**Vista #287** — 07_Rotonda_junto_al_parque.jpg (mayo de 2024) · hoja a_287.jpg

2781. [alta] Cámara — encuadre completo
   - Captura: La cámara está en la calzada, a la entrada de la glorieta: asfalto en todo el primer plano (y≈400–693), una isleta pintada con cebreado blanco que divide la calzada (x≈455–840, y≈385–540) con una señal de dirección prohibida (x≈610–655), y al fondo un edificio blanco de dos plantas con balaustradas (x≈580–830, y≈240–380).
   - Juego: Toda la mitad inferior es un terreno de arena amarilla (x≈0–1440, y≈385–693), sin calzada bajo la cámara; las carreteras pasan de lado a lado en segundo plano (y≈350–460) y en el centro izquierda hay un edificio de ladrillo rojo de dos plantas (x≈380–635, y≈280–370).

### Carretera de Guareña a Oliva de Mérida

**Vista #288** — 02_Tramo_norte_junto_al_parque.jpg (mayo de 2024) · hoja a_288.jpg

2782. [media] Color de fachada — edificio de la derecha
   - Captura: Revoco beige-crema (x≈945–1440, y≈100–490).
   - Juego: Blanco (x≈980–1440, y≈80–485).
2783. [media] Huecos — casa de la esquina izquierda
   - Captura: Ventanas con rejas y un ventanuco redondo (x≈125–145, y≈270–285).
   - Juego: Ventanas con contraventanas de madera marrón (x≈340–630), un balcón con barandilla (x≈230–300, y≈300–330) y una puerta de madera (x≈250–295, y≈350–405).
2784. [media] Huecos — segunda casa de la izquierda
   - Captura: Puerta de cochera marrón (x≈535–570, y≈360–400).
   - Juego: En esa zona (x≈535–635) hay ventanas con contraventanas marrones y ninguna cochera.
2785. [media] Detalles de fachada — toldos del edificio de la derecha
   - Captura: Marquesinas grises sobre la planta baja (x≈1125–1440, y≈170–300).
   - Juego: Toldos a rayas rosas y blancas (x≈1020–1165, y≈345–360) y una franja rosa en la fachada (x≈1100–1440, y≈315–335).
2786. [media] Cubierta — casa de la esquina izquierda
   - Captura: Remate plano con pretil (azotea), sin teja a la vista (x≈80–635, y≈230–260).
   - Juego: Tejado de teja roja (x≈200–635, y≈250–300).
2787. [media] Marcas viales — paso de peatones sobreelevado
   - Captura: Paso de cebra sobreelevado con triángulos blancos y línea de detención delante (x≈640–910, y≈395–490).
   - Juego: No hay paso de cebra; solo líneas discontinuas de carril.
2788. [media] Vegetación — arbustos y palmera del fondo
   - Captura: Fila de arbustos junto a la acera izquierda (x≈570–840, y≈365–405) y una palmera en la isleta del fondo (x≈860–905, y≈330–380).
   - Juego: No hay arbustos ni palmera.
2789. [media] Vegetación — seto del primer plano derecho
   - Captura: Seto verde en el primer plano derecho (x≈1025–1440, y≈490–693).
   - Juego: Acera pavimentada sin seto.
2790. [media] Mobiliario — terraza de la derecha
   - Captura: No hay terraza en la acera derecha.
   - Juego: Terraza con una sombrilla azul grande (x≈1080–1440, y≈335–690) y mesas y bancos blancos (x≈1180–1440, y≈565–690); más sombrillas al fondo (x≈850–920, y≈345–355).
2791. [media] Mobiliario — cartel grande de la derecha
   - Captura: Dorso gris de un gran cartel de dirección en primer plano (x≈1245–1440, y≈265–590).
   - Juego: No hay cartel.
2792. [media] Mobiliario — báculo junto al bordillo derecho
   - Captura: Báculo gris alto junto al bordillo derecho (x≈945–985, y≈0–500).
   - Juego: No hay báculo en ese punto.
2793. [baja] Zócalo — casa de la esquina izquierda
   - Captura: Zócalo gris (x≈80–475, y≈380–425).
   - Juego: Zócalo marrón (x≈200–635, y≈385–405).
2794. [baja] Marcas viales — líneas del primer plano
   - Captura: Sin marcas en el primer plano de la calzada.
   - Juego: Líneas blancas discontinuas en primer plano (x≈95–380, y≈545–693 y x≈995–1150, y≈570–693).
2795. [baja] Mobiliario — señal de paso de peatones
   - Captura: Señal de paso de peatones con placa «PASO SOBREELEVADO» (x≈1010–1115, y≈330–440).
   - Juego: No hay esa señal.
2796. [baja] Mobiliario — bolardos de la acera derecha
   - Captura: Bolardos en la acera derecha (x≈1150–1160, y≈435–465).
   - Juego: No hay bolardos.
**Vista #289** — 03_Conexiones_del_centro.jpg (mayo de 2024) · hoja a_289.jpg

2797. [alta] Cámara — encuadre completo
   - Captura: La cámara va por la calzada, que sale del primer plano (abajo x≈240–1200) y curva a la derecha (fuga x≈1000); a la izquierda, pegadas a la acera, una casa blanca con un gran portón verde de chapa (x≈85–435, y≈275–520) y tapias y naves (x≈430–850); a la derecha, acera, un solar de tierra y una tapia larga lejana (x≈1135–1440, y≈240–410), con un báculo de brazo curvo (x≈935–1035, y≈110–445).
   - Juego: La cámara está fuera de la calzada, sobre un paseo pavimentado con naranjos (x≈220–1440, y≈360–693): la calzada pasa a la izquierda (x≈260–800, y≈360–620) con un muro largo gris detrás (x≈0–770, y≈100–415); un naranjo enorme tapa el primer plano izquierdo (x≈0–420) y a la derecha, a pocos metros, se alza la fachada blanca de una casa con rejas (x≈1025–1410, y≈160–620).
**Vista #290** — 04_Junto_a_la_piscina.jpg (mayo de 2024) · hoja a_290.jpg

2798. [alta] Geometría — calzada paralela a la derecha
   - Captura: A la derecha de la calzada solo hay una acera con barandilla delante del edificio de la piscina (x≈800–1440, y≈360–600).
   - Juego: Entre la calzada y el edificio hay una acera con farola, una franja pintada de amarillo (x≈760–1440, y≈365–693) y una segunda calzada (x≈780–1440, y≈365–620) con una fila de árboles.
2799. [alta] Vegetación — eucaliptos de la izquierda
   - Captura: Dos eucaliptos grandes en la cuneta izquierda (x≈150–460, y≈0–430 y x≈470–660, y≈120–385).
   - Juego: No hay árboles en el margen izquierdo (solo un ciprés lejano, x≈470–500, y≈265–370).
2800. [alta] Vegetación — fila de árboles de la derecha
   - Captura: No hay árboles entre la calzada y el edificio de la piscina.
   - Juego: Fila de árboles de tronco claro y copa redonda (x≈720–1440, y≈10–465).
2801. [alta] Otros — margen izquierdo
   - Captura: Sin acera: cuneta de tierra con hierbas (x≈0–700, y≈360–693).
   - Juego: Explanada pavimentada de baldosa clara con bordillo (x≈0–700, y≈365–693).
2802. [media] Geometría — edificio de la piscina municipal
   - Captura: Fachada de dos plantas con la esquina redondeada y un cuerpo alto curvo (x≈1070–1440, y≈150–260).
   - Juego: Fachada recta de dos plantas, sin curva (x≈965–1440, y≈210–440).
2803. [media] Color de fachada — edificio de la piscina municipal
   - Captura: Hormigón gris pardo (x≈985–1440, y≈150–400).
   - Juego: Blanco (x≈965–1440, y≈210–440).
2804. [media] Mobiliario — báculo de la derecha
   - Captura: Báculo gris alto con foco y cámara junto a la piscina (x≈1235–1265, y≈0–530).
   - Juego: No está; en su lugar hay una farola negra en la acera junto a la calzada (x≈735–880, y≈55–580).
2805. [media] Muros y vallas — barandilla de la acera derecha
   - Captura: Barandilla metálica negra con riostras diagonales a lo largo de la acera (x≈800–1440, y≈360–500).
   - Juego: No hay barandilla.
2806. [baja] Marcas viales — paso de cebra del fondo
   - Captura: Paso de cebra al fondo (x≈715–790, y≈365–375).
   - Juego: No hay paso de cebra.
2807. [baja] Mobiliario — señal de prohibido aparcar
   - Captura: No hay señal.
   - Juego: Señal de prohibido aparcar (x≈805–840, y≈330–495).
2808. [baja] Mobiliario — farolas del margen izquierdo
   - Captura: No hay farolas a la izquierda.
   - Juego: Farolas negras a lo largo de la explanada (x≈90–665, y≈300–390).
**Vista #291** — 05_Entrada_desde_el_sur.jpg (mayo de 2024) · hoja a_291.jpg

2809. [alta] Geometría — nave agrícola de la izquierda
   - Captura: Nave larga con cubierta verde (x≈403–598, y≈320–358).
   - Juego: No se ve ninguna nave; en esa zona hay árboles.
2810. [alta] Vegetación — árboles del margen izquierdo
   - Captura: No hay árboles junto a la carretera a la izquierda: campo de hierba seca.
   - Juego: Eucaliptos (tronco claro en primer plano, x≈80–300, y≈0–575; otros en x≈500–710) y árboles de copa redonda dispersos (x≈0–560, y≈270–445).
2811. [alta] Vegetación — margen derecho
   - Captura: Matorral y zarzas verdes densas a lo largo de la cuneta (x≈785–1440, y≈350–693) y un campo de cereal detrás.
   - Juego: Arboleda de árboles de copa redonda en hileras (x≈740–1440, y≈300–490) sobre un campo de surcos verdes, con una franja amarilla junto al bordillo (x≈920–1440, y≈450–693).
2812. [media] Geometría — sección de la carretera
   - Captura: Carretera de dos carriles sin arcén: la cámara va por el carril derecho; la doble línea central pasa a su izquierda (abajo x≈430–480) y el asfalto ocupa x≈240–910 abajo.
   - Juego: Carretera más ancha, con bordillos (abajo x≈320–1350), y la cámara a la izquierda de la línea discontinua central (abajo x≈770–860).
2813. [media] Marcas viales — línea central
   - Captura: Doble línea continua central (de x≈450 abajo a x≈690 al fondo) y líneas de borde junto al borde del asfalto.
   - Juego: Línea central discontinua (x≈720–860) y dos líneas continuas separadas de los bordillos (abajo x≈615–700 y x≈1000–1075).
2814. [media] Acera y bordillo — bordes de la carretera
   - Captura: Sin bordillos: el asfalto acaba en cunetas de tierra y hierba.
   - Juego: Bordillos blancos elevados a ambos lados (de x≈320 a x≈700 y de x≈1350 a x≈750).
2815. [media] Vegetación — suelo del margen izquierdo
   - Captura: Hierba seca amarilla (x≈0–660, y≈355–580).
   - Juego: Tierra desnuda anaranjada (x≈0–640, y≈360–693).
2816. [media] Muros y vallas — alambrada de la izquierda
   - Captura: Alambrada sobre postes a lo largo del campo (x≈0–600, y≈360–460).
   - Juego: No hay alambrada.
2817. [baja] Calzada — firme
   - Captura: Asfalto gastado con grietas y parches (x≈240–910 abajo).
   - Juego: Asfalto gris liso y uniforme.
2818. [baja] Otros — silueta del pueblo
   - Captura: Al fondo a la derecha, el pueblo con la torre de la iglesia (x≈760–1080, y≈310–350).
   - Juego: No se ve el pueblo: el horizonte lo ocupan árboles.

