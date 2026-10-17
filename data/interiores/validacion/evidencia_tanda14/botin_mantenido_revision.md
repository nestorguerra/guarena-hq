# Adenda final v3

**Aceptación estática sin P1/P2 abiertos.** JS final revisado SHA256 `db203601f501d8871789acaca700120a5cab0b1f0036d153200ca4a9abf30f6f`; los otros tres hashes del informe siguen iguales. Raíz añadió cotejo de ID/nombre y valor finito positivo en el objeto incorporado a la mochila. Ya no se acepta la recompensa incorrecta documentada abajo.

Reejecución propia CPU (`botin_mantenido_revision_cpu_v3.mjs/json`): positivo PASS; mutante de acción sin persistencia rechazado; mutante `{id:wrong,name:wrong,value:-1}` rechazado con «La recompensa no corresponde al objeto recogido: joyero». Sintaxis JS correcta. V2 y sus recibos se conservan. La validación no exige un importe exacto aleatorio; no se amplía el alcance a otras recompensas. Runtime v2 fuente comunicado PASS por raíz; v3 fuente/paquete aún pendientes, no acreditados por esta revisión.

---

# Revisión independiente del contrato mantenido de botín

Dictamen: **aceptación estática de la versión corregida**, sin P1/P2 abiertos en el alcance anunciado. El P2 encontrado durante esta revisión se ha subsanado por raíz. No se han ejecutado Chrome, GPU, build ni modificado fuentes de producto por este revisor. Fuente/paquete y CI efectivos corresponden a las ejecuciones de raíz; esta aceptación no las sustituye.

## Identidad revisada

- `tools/interiores/botin_pruebas.py`: `9be625ef4be6bbb4be683162b2a322eed1637de1bfa3e402d53f8ebf26c14485`.
- `tools/interiores/botin_pruebas.js` corregido: `bf43d68b7bdca9f91fc8e0c7ea4d74d8a236c5df8dc55d12b0829627e7dd17d4`.
- `.github/workflows/validar.yml`: `1410730ef848877da54811ec112dd29a6d0954fbd7ef63746f96b6d70760795e`.
- `src/interiors.js`: `ceb6c3bcad9db507fe633a22c3f69d0ccfadae11607bf46681b943d91f85c0af`.

## Hallazgo subsanado

**P2 — el test reparaba el guardado que debía comprobar.** JS inicial SHA `4a9cbfb7af06c8321bb2933394374bc953b64c64270efe29b6648213591091fe`, línea37, llamaba `g.persist()` tras recoger ambos objetos. Si `finishLoot` perdía su guardado, el instrumento escribía la recompensa antes de recargar y daba PASS. Raíz retiró esa llamada; el JS corregido devuelve el estado directamente después de las acciones.

Demostración propia CPU en `botin_mantenido_revision_cpu.mjs/json`: ejecuta el JS exacto del contrato y los cuerpos reales de `option`/`finishLoot`, con dobles declarados de jugador, collider, entrada y almacenamiento. Positivo PASS; mutante sin `g.persist()` dentro de la acción: falso PASS con guardado artificial, rechazo con versión corregida. No simula que se haya ejecutado Page.reload real.

## Lectura de integración

- `PrivateTab` crea un BrowserContext nuevo y un target propio; al salir elimina ese contexto. La fixture no lee partidas del usuario. Se retiran residentes para aislar el selector, y el informe lo declara.
- Fixture instalada antes de navegar. El marcador en sessionStorage impide sobrescribir la partida al recargar el mismo documento/origen; la partida se carga desde localStorage en el documento nuevo. El marcador JS de documento anterior evita confundir el juego antiguo con el reiniciado. LISTO se vuelve a esperar tras confirmar el documento nuevo.
- Se comparan dinero y mochila completos antes/después de recarga, además de dos claves testigo ajenas a HQ y errores de ambas cargas. Fallos del contrato o recarga producen FAIL y exit1; no hay captura silenciosa que convierta una excepción en PASS.
- Se llama `option().run()` real; no se marca tomado ni se recompensa desde el instrumento. Se exige objeto visible, punto de interacción libre, etiqueta correcta, cambio tomado/oculto y recompensa.
- El guard de `interiors.js:1158` sólo excluye `type === loot && taken` antes de escoger el más próximo. Conserva filtros por planta/asiento, ramas de horror y tipos no loot. La revisión CPU previa de siete casos permanece en `selector_botin_revision_cpu.json`.
- CI ejecuta la prueba sobre **fuente**, después de contratos funcionales. El job que construye dist es separado; no se afirma que este paso cubra paquete. `--paquete` permite esa comprobación local independiente. El JS no importa módulos bare ni depende de una ruta .cache.
- AST Python y `node --check` del JS pasan en esta revisión.

## Cobertura pendiente, sin bloqueo del alcance actual

1. **Identidad/valor de la recompensa:** JS:28–34 sólo exige +1 en longitud de mochila para joyero y aumento de dinero para lata. Una recompensa equivocada pero persistida pasa. Mutante CPU explícito `{id:wrong,name:wrong,value:-1}` confirmado. Recomendación acotada: cotejar el nuevo ID/nombre y valor finito dentro del rango con los PERK efectivos, y verificar que el dinero no cambia para joyero. No se ha detectado ese defecto en `finishLoot` actual.
2. **Permanencia de la geometría de regresión:** la semilla2786 reproduce el fallo real documentado por raíz, pero el contrato no exige que el botín tomado siga interfiriendo en el segundo punto bajo el selector antiguo. Una futura receta podría separar los objetos y perder esa cobertura sin fallar. Conviene conservar una guarda de interferencia o mutación dirigida del selector. La cercanía no se deduce sólo del nombre del test.
3. **Diagnóstico CI:** `/tmp/botin-ci.json` no se sube como artefacto y stdout sólo muestra FAIL, sin la causa. El exit1 es correcto, pero imprimir `errores` al fallar o conservar el JSON facilitaría diagnosticarlo. No exige otro timeout.
4. El arranque ficticio no comprueba explícitamente dinero321/mochila vacía antes de actuar; el contexto es nuevo y el script visible lo instala, pero esa aserción mejoraría la detección de futuros cambios en la carga de partidas.

## Declined to judge

Persistencia del objeto tomado al volver a entrar en la casa (fuera del alcance declarado), diálogos/IA/residentes, navegación completa hasta el botín, condena/crimen, cerraduras, otras recompensas/armas, geometría de todas las semillas, calidad visual, FPS, ejecución real de CI/fuente/paquete y publicación. El resultado CPU no acredita ninguno de esos puntos.
