# T17 — cuarto contrato de tela, entrega privada

Preparado `contratos_tela.fragment.js`, guard tanda>=20. Requiere imports ya presentes en el harness: HouseBuilder, THREE, H, OBJETOS y partes; usa caso/exigir/tirar existentes. No modifica los tres callbacks de raíz ni producto.

Captura cada geometría curtain con clone antes de HouseBuilder.add; aplica rotación y origen de ese builder a la copia. Tras buildVecino real selecciona paños que intersectan el marco de la única estancia estudio, exige primero mesa por rol y ordenador apoyado; después diferencia ventana real de estancia interior. Incluye paneles vb_panel_estudio_ cuando existen. Usa triángulos reales de posición/índice y transformación inversa exacta de cada OBB de partes del puesto/ordenador/panel. Repliegue de1mm hacia dentro: evita contar mero contacto; las piezas de espesor≤2mm quedan vacías y no se usan como sólido. No utiliza reserva de ventana, cámara, bbox global de la tela ni una comparación de alturas como sustituto de la intersección.

Positivo exigido: no intersecciones, donde existen ventanas reales, al menos dos paños cortos con top2.225/bajo1.28 por planta. Negativo dirigido3244: sólo copia de sus triángulos cortos se estira verticalmente a2.05 conservando top y x/z; debe recuperar una colisión. No muta geometría viva ni restaura producto artificialmente. Limpia clones incluso ante excepción y restaura prototype.add en finally.

CPU ejecutada: callback literal contra R2 sellada, con reales buildVecino/HouseBuilder/Three/partes y Canvas de trazas. RED3244: tela cruza partes0/3/6/7 de t17_mesa_amplio. Se detiene en ese primer caso; no presentar1594/1481 ni negativo largo como ejecutados. Verificado prototype restaurado y27clones observados/27eventos dispose (contador global de clone durante este caso). Recibo tela_RED_R2.json, reproducción tela_RED_R2.cpu.mjs.

El GREEN de modelos finales y su negativo largo siguen pendientes del sello del autor y de la ejecución del callback. La copia final_r1 aún mutable no se usó para afirmar PASS. Un revisor independiente debe revisar este contrato de autoría propia junto al candidato final; no autoaprobación. No GPU/API/build/CI ni fuentes activas modificadas.

## Corrección R2: estudio interior1594

La versión inicial asumía erróneamente una ventana en cada estudio. Se conserva completa en revision_contratos_estudio/tela_historico_r1/. Versión actual SHA a25a4816c5c02f335e53c6c5ac7831f4bca39bf106c53163a183a39e6d97f2a4.

h.rooms no expone open en producto. El contrato usa sus bounds reales para asignar h.views, que son huecos físicos exteriores registrados por HouseBuilder.view, y su cota inferior para excluir puertas. No son reservas ni cámaras modificadas. Se cotejó esta clasificación contra room.open de la extracción literal CPU de las tres fichas:3244/A2=1ventana/2paños;1594/A1=0/0;1481/A2=1/2. En estancia sin ventanas exige también ausencia de tela y continúa; mesa/ordenador y apoyo ya se comprobaron antes. No añade una ventana ni una semilla especial a producto.

Región exacta del guard PASS en tres construcciones reales. Negativos: quitar paños de los dos estudios con ventana falla; introducir un paño en1594 sin ventana falla. Recibos tela_ventanas.cpu.mjs/tela_ventanas_cpu.json. Callback completo actualizado conserva RED3244 por las cuatro intersecciones y libera27/27clones/restaura prototype. La condición física final y el negativo alargando cortos siguen pendientes del candidato sellado. Los tres fragmentos de raíz no se han editado.
