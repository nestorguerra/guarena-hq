// Acciones reales en una partida ficticia del navegador privado de pruebas.
(async () => {
  const g = game, seed = 2786;
  const door = g.interiors.doors.find(d => d.seed === seed);
  if (!door) throw Error('No existe la puerta de prueba 2786');
  await g.interiors.enter(door, { mode: 'visit', silent: true, seed });
  // Esta prueba aísla el selector de objetos de los diálogos de residentes.
  if (g.interiors.life) {
    g.interiors.life.dispose();
    g.interiors.life = null;
  }
  const h = g.interior, acciones = [];
  for (const id of ['joyero', 'lata']) {
    const item = h.loot.find(i => i.id === id && !i.taken);
    if (!item || !item.mesh?.visible) throw Error('Falta el objeto visible: ' + id);
    g.player.pos.set(item.x, item.y || 0, item.z);
    const inicio = { x: g.player.pos.x, z: g.player.pos.z };
    const collider = h.levels?.[Math.round((item.y || 0) / 3.1)] || h.collider;
    collider.resolveCircle(g.player.pos, .34);
    if (Math.hypot(g.player.pos.x - inicio.x, g.player.pos.z - inicio.z) > .05) {
      throw Error('Punto de interacción dentro de un obstáculo: ' + id);
    }
    const opcion = g.interiors.option();
    if (!opcion?.label?.toLowerCase().includes(item.def.name.toLowerCase())) {
      throw Error('Selector incorrecto para ' + id + ': ' + opcion?.label);
    }
    if (item.def.crack) throw Error('La prueba no adelanta cerraduras');
    const antes = { dinero: g.player.money, mochila: (g.player.bag || []).length };
    opcion.run();
    if (!item.taken || item.mesh.visible) throw Error('El objeto no desaparece: ' + id);
    const despues = { dinero: g.player.money, mochila: (g.player.bag || []).length };
    if (item.def.cash ? despues.dinero <= antes.dinero : despues.mochila !== antes.mochila + 1) {
      throw Error('No se recibe la recompensa: ' + id);
    }
    if (!item.def.cash) {
      const premio = g.player.bag[antes.mochila];
      if (premio.id !== id || premio.name !== item.def.name || !Number.isFinite(premio.value) || premio.value <= 0) {
        throw Error('La recompensa no corresponde al objeto recogido: ' + id);
      }
    }
    acciones.push({ id, etiqueta: opcion.label, antes, despues, malla_oculta: true });
  }
  return { acciones, dinero: g.player.money, mochila: g.player.bag || [], errores: window.__errs };
})()
