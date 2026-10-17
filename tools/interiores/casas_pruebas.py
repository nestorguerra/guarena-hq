"""Pruebas funcionales de vivienda, en el navegador de pruebas sin sonido."""
import json, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'perf'))
from cdp import Tab

def main():
    tab = Tab(9333, 'http://localhost:8920/tools/interiores/validar.html', w=1280, h=720, dpr=1)
    try:
        result = json.loads(tab.ev('''(async () => {
          const P = await import('/tools/interiores/casas_pruebas.js');
          return JSON.stringify(await P.probarCasas({tanda: %d}));
        })()''' % (int(sys.argv[sys.argv.index('--tanda')+1]) if '--tanda' in sys.argv else 0), timeout=900))
    finally:
        tab.close()
    for p in result['pruebas']:
        print(p['estado'], p['nombre'], p.get('motivo', ''))
    print(len(result['pruebas']), 'pruebas,', len(result['errores']), 'fallos')
    if '--informe' in sys.argv:
        dest = sys.argv[sys.argv.index('--informe') + 1]
        with open(dest, 'w') as f: json.dump(result, f, ensure_ascii=False, indent=2)
    return not result['errores']

if __name__ == '__main__':
    sys.exit(0 if main() else 1)
