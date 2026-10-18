# T17 R2 — caso dirigido individual: FAIL preservado

Semilla solicitada **4**, primera optante literal del laboratorio (estudiante/joven, habitacion dorm); marco fijo **3,2×2,8×2,75 m**, puerta −0,75, reserva e inicio originales. No se cambió semilla, marco, perfil ni receta para buscar un positivo. Se cotejaron los47hashes del manifiesto R2 antes de ejecutar.

`buildLocal` real agotó sus12intentos: efectiva **1152023**, todos con entrada12/biblioteca ausente. `revisar` real, presupuesto real, devuelve exactamente **obligatorio: estancia/t17_biblioteca — 0 colocados, el kit pide 1**. Resultado no vacío: mesa+silla vinculada, bajo, ordenador apoyado sop0/sup0, libro sobre bajo sop2/sup0, póster y lámpara. Roles mesa/silla/comoda; falta estantería. Acciones registradas: salida y asiento con destino a la mesa; no se ejecutaron acciones y el laboratorio no materializa automáticamente lectura/cajones domésticos por rol.

Paso.80:2,98m² alcanzables de2,98m² libres;0flotantes,0interpenetraciones;11mallas/490triángulos/1luz en este laboratorio CPU. El conjunto incompleto no aprueba por esos otros resultados verdes. No es una medición del coste de casa completa.

Grupo3,27999993m frente a paredes3,2/2,8: no cabe. Primera tentativa conserva P, activas, guardias y3extracciones U exactamente frente a quitar sólo grupo_pared. La ruta individual real no gira en una esquina: junto_a mantiene orientación y sólo prueba derecha/izquierda. En el intento definitivo la biblioteca hacia el interior ocupa x[−.370,.630], penetrando mesa7,75cm (además ordenador); hacia el exterior ocupa x[1,610,2,610], fuera del límite1,6. si_no:false impide buscar otra pared. No es evidencia de azar insuficiente ni de que una reserva deba relajarse.

Puerta y ventana originales se construyeron mediante buildLocal: huecos de pared en coordenadas longitudinales[.27,1.57]y[1.92,2.87], alturas[0,2.35]y[.45,2.6]. Reserva doméstica original e inicio permanecen idénticos. No se inventó una reserva adicional.

**Decisión:** este caso refuta que la receta R2 actual garantice un programa individual completo cuando el frente no cabe. Mantiene vigente el criterio de diseño (aceptar una alternativa individual válida), pero no acredita su implementación para este marco. Conservar FAIL, no implementar ni buscar otra semilla. Raíz autoriza aparte un único control si_no:true, registrado en otra carpeta.

Evidencia: repro.cpu.mjs/resultado.json/repro.log y diagnostico.cpu.mjs/diagnostico.json. Three/HouseBuilder/colisiones/validador reales; Canvas de trazas y texturas de sustitución. Sin GPU, navegador, build, API ni cambios activos. No revisión artística ni garantía81/200.
