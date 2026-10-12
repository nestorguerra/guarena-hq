# Santa María's furniture as church.js builds it — pews, altars and retablos, the pulpit, the confessionals, the organ,
# the doors' lobbies — exported from the game into one GLB in the church's own frame (x to the altar, z south), for the
# light's bake (tools/blender/interior.py --muebles): it casts its shadows there (the pews on the floor, the retablo on
# the apse) and is not part of the model. Its architecture is left out (h.archMats: the model replaces it), and so are
# the small lit things (lamps, candles, bulbs, glass) that would stand round the bake's lamps.
# Needs the HQ dev server (port 8920) and the muted headless Chrome (port 9333; see tools/perf/cdp.py):
#   python3 tools/hipermuebles.py [.cache/hq/interior/muebles.glb]
import sys, os, base64, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'perf'))
from cdp import Tab
out = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, '..', '.cache', 'hq', 'interior', 'muebles.glb'))
os.makedirs(os.path.dirname(out), exist_ok=True)
T = Tab(9333, 'http://localhost:8920/index.html?estilo=real')
try:
    r = json.loads(T.ev('''(async () => {
  const wait = (ms) => new Promise(r => setTimeout(r, ms));
  await new Promise((r, no) => { const c = () => (window.game && document.getElementById('loading') && document.getElementById('loading').hidden) ? r() : performance.now() > 150000 ? no(new Error('no carga')) : setTimeout(c, 50); c(); });
  { const nb = document.querySelector('#modeSeg button[data-mode="normal"]'); if (nb) nb.click(); await wait(300); }
  document.getElementById('bPlay').click(); await wait(1500);
  const sel = document.getElementById('select'); if (sel && !sel.hidden) { document.getElementById('bStart').click(); await wait(2500); }
  const g = game, I = g.interiors;
  const { buildChurch } = await import('/src/church.js');
  const THREE = await import('three');
  const { GLTFExporter } = await import('three/addons/exporters/GLTFExporter.js');
  // the church as church.js builds it, on its own (no people, no model in high definition)
  const h = buildChurch(7);
  h.group.updateMatrixWorld(true);
  const O = h.origin, root = new THREE.Group(), kept = [], left = {};
  const lit = (m) => m && (m.emissiveIntensity > 0.3 && m.emissive && m.emissive.getHex() !== 0 || m.transparent || m.isMeshBasicMaterial || m.isShaderMaterial);
  h.group.traverse((o) => {
    if (!o.isMesh || !o.visible) return;
    const mats = [].concat(o.material);
    if (mats.some((m) => h.archMats.has(m))) { left.arquitectura = (left.arquitectura || 0) + 1; return; }
    if (Object.values(h.furn || {}).some((G) => mats.some((m) => G.mats && G.mats.has(m)) || (G.tag && o.userData.hd === G.tag))) { left.alta = (left.alta || 0) + 1; return; } // (made in high definition: tools/blender/muebles.py)
    if (mats.some(lit) || (o.userData && (o.userData.lamp || o.userData.flame))) { left.luces = (left.luces || 0) + 1; return; }
    const geo = o.geometry.clone().applyMatrix4(o.matrixWorld).translate(-O.x, 0, -O.z);
    const m = new THREE.Mesh(geo, new THREE.MeshStandardMaterial({ color: 0x806040 }));
    m.name = (o.name || 'mueble') + '_' + kept.length;
    root.add(m); kept.push(m);
  });
  const glb = await new GLTFExporter().parseAsync(root, { binary: true });
  const u8 = new Uint8Array(glb); let s = ''; for (let i = 0; i < u8.length; i += 0x8000) s += String.fromCharCode.apply(null, u8.subarray(i, i + 0x8000));
  return JSON.stringify({ b64: btoa(s), n: u8.length, meshes: kept.length, fuera: left, errs: window.__errs });
})()''', 600))
    open(out, 'wb').write(base64.b64decode(r['b64']))
    print(out, r['n'] // 1024, 'KB,', r['meshes'], 'mallas; fuera:', r['fuera'], 'errores:', r['errs'])
finally:
    T.close()
