# Photographs of the rooms of the neighbours' houses (epic I, vivienda por estancia), as the game builds them: the houses
# of the town's doors that have a room of that kind (src/houses.js types: salon, cocina, bano, dorm, dorm2, ninos,
# dormJoven, comedor, estudio, despacho, musica, trofeos, taller, costura, despensa, trastero), entered in the game's page
# (a headless muted Chrome, tools/perf/cdp.py, port 9333) and shot from two corners of the room, looking across it.
# Writes .snaps/casa_<tipo>_<seed>_<k>.jpg and a sheet data/interiores/fichas/casa_<tipo>.jpg.
#   python3 tools/interiores/fotos_casa.py <tipo> [n]          (n houses, 3 by default; town doors first, then others)
import json, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'perf'))
from cdp import Tab
from PIL import Image

JS = r'''(async () => {
  const H = await import('/src/houses.js');
  const g = window.game, tipo = %s, n = %d, out = [];
  g.sky.hour = 12;
  const r = g.renderer; r.setSize(1280, 720, false); if (g.composer) g.composer.setSize(1280, 720);
  const cam = g.camera; cam.aspect = 16 / 9; cam.fov = 75; cam.updateProjectionMatrix();
  // the town's doors first, then any house: those with a room of that kind
  const seeds = [...g.interiors.doors.filter((d) => d.seed >= 1000).map((d) => d.seed)];
  for (let s = 1000; s < 9000 && seeds.length < 400; s += 37) seeds.push(s);
  for (const s of seeds) {
    if (out.length >= n) break;
    const prof = H.houseProfile(s);
    const h0 = H.buildVecino(s, { x: -9700, z: -9700 });
    const has = h0.rooms.some((q) => q.type === tipo);
    h0.group.traverse((o) => { if (o.isMesh) o.geometry.dispose(); });
    if (!has) continue;
    const door = g.interiors.doors.find((d) => d.seed === s) || { name: 'Casa', seed: s, x: g.player.pos.x, z: g.player.pos.z };
    await g.interiors.enter(door, { mode: 'visit', silent: true, seed: s });
    await new Promise((res) => setTimeout(res, 500));
    const h = g.interior, rm = h.rooms.find((q) => q.type === tipo), y = rm.lv ? 3.1 : 0;
    const body = g.player.char && g.player.char.object; if (body) body.visible = false;
    for (const [k, f] of [[0, 0.12], [1, 0.88]]) {
      const x = rm.x0 + (rm.x1 - rm.x0) * f, z = rm.z0 + (rm.z1 - rm.z0) * f, cx = (rm.x0 + rm.x1) / 2, cz = (rm.z0 + rm.z1) / 2;
      for (let i = 0; i < 3; i++) g.frame(1 / 30);
      cam.position.set(x, y + 1.6, z); cam.lookAt(2 * cx - x, y + 0.8, 2 * cz - z); cam.updateMatrixWorld(true);
      g.render();
      await fetch('/__snap?name=casa_' + tipo + '_' + s + '_' + k, { method: 'POST', body: r.domElement.toDataURL('image/jpeg', 0.86) });
    }
    out.push({ seed: s, perfil: prof.id, estilo: prof.style, plano: prof.layout, sala: [+(rm.x1 - rm.x0).toFixed(1), +(rm.z1 - rm.z0).toFixed(1)], planta: rm.lv });
    await g.interiors.exit();
    await new Promise((res) => setTimeout(res, 300));
  }
  return JSON.stringify(out);
})()'''

def main():
    tipo = sys.argv[1]
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    T = Tab(9333, 'http://localhost:8920/index.html?estilo=plastilina', w=1280, h=720, dpr=1)
    try:
        T.ev('''(async () => { const t0 = performance.now(); while (performance.now() - t0 < 180000) { if (window.game && window.game.state === 'play') break; await new Promise((r) => setTimeout(r, 250)); } })()''', timeout=240)
        res = json.loads(T.ev(JS % (json.dumps(tipo), n), timeout=600))
    finally:
        T.close()
    if not res: print('ninguna casa con', tipo); return
    hoja = Image.new('RGB', (1280, 360 * len(res)))
    for j, c in enumerate(res):
        for k in range(2): hoja.paste(Image.open(os.path.join(ROOT, '.snaps', f"casa_{tipo}_{c['seed']}_{k}.jpg")).resize((640, 360)), (k * 640, j * 360))
        print(c)
    os.makedirs(os.path.join(ROOT, 'data', 'interiores', 'fichas'), exist_ok=True)
    hoja.save(os.path.join(ROOT, 'data', 'interiores', 'fichas', f'casa_{tipo}.jpg'), quality=82)
    print('→ data/interiores/fichas/casa_%s.jpg' % tipo)

if __name__ == '__main__':
    main()
