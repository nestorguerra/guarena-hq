# T20 R1 · revisión técnica independiente dirigida

**Sin P1/P2 confirmado en el alcance revisado; no bloqueo técnico para integrar esta candidata y ejecutar los gates finales.** No propone otra iteración. El usuario ha pedido detener mejoras y desplegar lo actual; la integración/publicación corresponde a raíz y esta revisión no sustituye sus gates.

Candidata examinada: `prototipo_r1/preparado.json`, SHA `74497e2dffde62ef6ce4975dcd01b218486c918110a8b691305977e0e6afbaf1`, **667 entradas cotejadas**. Los seis archivos de entrada de la prueba dirigida coinciden con el sello final. Producto activo y snapshot no se han escrito. Sólo se generaron estos instrumentos/recibos privados, sin GPU, navegador, API, build ni gates amplios.

## Camas, apoyos y alcance compartido

El catálogo B cambia exactamente `vb_cama_doble`, `vb_cama_individual` y `vb_cama_amplia`. Clase PUSH, masa, roles y demás metadatos funcionales permanecen idénticos; sólo cambian partes y nota. Las envolventes de los tres modelos mantienen sus seis extremos dentro de 1e−6 m. Los demás objetos B son estructuralmente idénticos, incluida la cama infantil: sus copias se crean antes de aplicar la transformación adulta.

La nueva vuelta de sábana apoya sobre la colcha real: nueve rayos por modelo contra geometría Three r170, 27 en total, muestran contacto con diferencia aproximada −2,2e−8 m. No se deduce apoyo sólo del AABB. Colchón y colcha conservan continuidad central y las uniones estructurales previas; no se presenta el modelo textil como un conjunto sin solapes. El colchón crema deja de recibir tinte; sólo el dormitorio aplica la nueva paleta de colcha por estilo. La geometría compartida de **cama individual** cambia también `vivienda_joven`. No hay referencias de doble/amplia en ese kit. Sus notas visuales previas no acreditan el modelo nuevo.

Annie conserva dormitorio propio y no consume el kit de dormitorio ni estos tres modelos. La rama de acabado excluye explícitamente perfil Annie. Es alcance comprobado por fuentes; no se ejecutó su casa en esta revisión.

## Colocación e interacciones

Las entradas de cama/mesitas/armario/cómoda preceden al programa nuevo y mantienen sus reglas. La receta introduce orejero enfrente, superficie/libro y biblioteca vinculados, con recuperaciones existentes; no introduce solver. La biblioteca puede recuperar contra pared si no cabe junto al asiento. No se promete composición agrupada universal ni igualdad de RNG: las entradas añadidas modifican consumo posterior y pueden desplazar escritorio/decoración legítimamente.

Se revisó el recibo de raíz `medidas/resultado_r1.json` y el código que lo genera: 22 construcciones del pueblo/28 dormitorios, cero errores de validar/revisarUso, camas de los mismos IDs/cantidades y ninguna pérdida por **tipo y multiplicidad** de acción en la sala. Ese comparador comprueba inclusión de los tipos anteriores; no prueba identidad, precio o ejecución de cada acción. Máximos declarados allí: 60 mallas y 65.948 triángulos. No se ha repetido ese barrido ni se transforma en validación universal.

La prueba independiente construye 3244, 2720 y 4685 con HouseBuilder, geometrías, agrupación y collider reales, Canvas/texturas de prueba. En las tres:

- El destino final de salida de cama está conectado en mapa de ancho .80, y el collider real con radio .34 devuelve delta/depth0.
- El destino final de la acción hide devuelve delta/depth0. Es el punto ajustado de houses que consume unhide, no el frente nominal del armario.
- Cada orejero y silla de escritorio tiene un único asiento registrado y al menos un punto alcanzable libre, donde es el asiento más próximo y su distancia es menor de1,25 m. Distancias encontradas: aproximadamente .63–.71 m.

En3244/4685 el frente de la silla de escritorio está ocupado por la mesa, como corresponde a una silla que la mira. La comprobación inicial de frente dio `map80:false` y se conserva en el recibo. El acceso lateral/trasero conectado existe y el collider lo confirma; no se corrigió una pose ni se declaró libre ese frente. La selección accesible no equivale a ejecutar sit/standUp ni a probar la animación.

Se revisaron las poses de los nuevos objetos sobre mesa auxiliar/biblioteca en el recibo de las22casas: ninguna penetración con su propio soporte supera .005m usando partes reales. Es relevante porque el motor excluye al padre de colisiones generales. Los controles de reservas, interior y paso del motor siguen vigentes; no se redujeron mínimos ni dimensiones.

## Acabado y caller

La lectura del diff confirma que dorm/dorm2 se revisten después de amueblar, pasando la estancia real, y su zócalo anterior se excluye. El acento elige la pared del cabecero mediante el giro de la cama y mantiene el recorte de huecos existente. Reutiliza la misma familia de material de salón/trofeos y los defines dependen del perfil de la casa, no de una selección tardía por habitación. No se cambian luz, cámara, arquitectura ni colisiones.

La alfombra `vb_alfombra` tiene tapas a .012/.014 m: ambas quedan por encima del acabado nuevo .0095 m. No reproduce el enterramiento de la antigua alfombra de salón. Esto se comprobó en cotas de fuente; no se hizo prueba de píxeles.

## Evidencia y límites

`dirigida.cpu.mjs`, `resultado.json` y `cierre.json` contienen la reproducción, entradas hash y resultados. El primer intento del instrumento asumió `h.levels` obligatorio; falló al llegar a una casa de planta única. Se conserva en `error_instrumento_levels.log`; se corrigió únicamente el acceso opcional y se repitió la prueba. No era un fallo de producto ni se contó como PASS.

**Declined to judge:** calidad visual/nota4, captura o shader WebGL, noche/Realista, acciones ejecutadas y persistencia, recorrido completo del jugador, autoguardado, rendimiento/FPS, 81laboratorios/200casas, CI/Pages/despliegue. La rama `entre` de alfombra obligatoria depende de que exista el sillón y usa el fallback existente cuando falla la colocación; su cobertura global queda a los gates, no al éxito de estas tres casas. No se han alterado umbrales ni añadido excepciones para obtener verde.

Los contratos T23 no se han preparado: no se amplía la tarea tras la orden de cerrar mejoras. Este informe acredita la revisión dirigida del sello indicado, sin presentar pruebas pendientes como terminadas.
