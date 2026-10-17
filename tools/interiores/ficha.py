# The card of each kit (technical backlog, I-04): four shots from the fixed cameras (tools/interiores/lab.js) of the
# kit built with its reference seed, next to three photographs of its moodboard (links: never the pictures). In the
# game's page in a headless Chrome (muted: tools/perf/cdp.py, port 9333) on the development server. Writes
# data/interiores/fichas/<kit>_<k>.jpg (640×360) for the panel (tools/interiores/panel.html) and the reviewers.
#   python3 tools/interiores/ficha.py [kit …] [--semilla 1]
import glob, io, json, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'perf'))
from cdp import Tab
from PIL import Image

def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--') and not a.isdigit()]
    seed = int(sys.argv[sys.argv.index('--semilla') + 1]) if '--semilla' in sys.argv else 1
    kits = args or sorted(os.path.basename(f)[:-5] for f in glob.glob(os.path.join(ROOT, 'data', 'kits', '*.json')) if not f.endswith('.schema.json'))
    out = os.path.join(ROOT, 'data', 'interiores', 'fichas')
    os.makedirs(out, exist_ok=True)
    T = Tab(9333, 'http://localhost:8920/index.html?estilo=plastilina', w=1280, h=720, dpr=1)
    try:
        T.ev('''(async () => { const t0 = performance.now(); while (performance.now() - t0 < 180000) { if (window.game && window.game.state === 'play') break; await new Promise((r) => setTimeout(r, 250)); } })()''', timeout=240)
        for k in kits:
            r = json.loads(T.ev('(async () => { const L = await import("/tools/interiores/lab.js?" + Date.now()); window.game.sky.hour = 12; return JSON.stringify(await L.fotos(%s, %d, "ficha")); })()' % (json.dumps(k), seed), timeout=300))
            for i, name in enumerate(r['fotos']):
                im = Image.open(os.path.join(ROOT, '.snaps', name + '.jpg')).convert('RGB').resize((640, 360), Image.LANCZOS)
                im.save(os.path.join(out, f'{k}_{i}.jpg'), quality=82)
            print(k, '·', r['n'], 'objetos ·', f"{r['W']:.1f} × {r['D']:.1f} m ·", r['luces'], 'luces')
    finally:
        T.close()

if __name__ == '__main__':
    main()
