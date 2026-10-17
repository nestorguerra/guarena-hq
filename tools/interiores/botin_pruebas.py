"""Recoger dos objetos próximos y comprobar su recompensa tras una recarga real.

Usa el Chrome sin sonido de pruebas y un contexto privado; no carga partidas del usuario.
No mide rendimiento ni comprueba diálogos o reaparición del botín al volver a una casa.
"""
import argparse
import json
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools/perf'))
from beta import PrivateTab
from integracion import LISTO


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    origen = parser.add_mutually_exclusive_group()
    origen.add_argument('--url')
    origen.add_argument('--paquete', action='store_true')
    parser.add_argument('--informe', default='data/interiores/validacion/botin.json')
    args = parser.parse_args()
    url = args.url or ('http://localhost:8920/' + ('dist/test.html' if args.paquete else 'index.html') + '?estilo=plastilina')
    informe = dict(estado='FAIL', url=url, alcance='selector real, recompensa y recarga; residentes retirados', errores=[])
    fixture = dict(quality='alta', qualityMode='manual', dynRes=False, weatherLive=False, pick='annie', money=321, bag=[])
    inicio = "if(!sessionStorage.getItem('botin_fixture')){localStorage.setItem('guarena_hq_save'," + json.dumps(json.dumps(fixture)) + ");localStorage.setItem('guarena_evo_save','testigo_evo');localStorage.setItem('guarena_save','testigo_fija');sessionStorage.setItem('botin_fixture','1');}"
    try:
        with PrivateTab() as tab:
            tab.call('Emulation.setDeviceMetricsOverride', dict(width=1280, height=720, deviceScaleFactor=1, mobile=False))
            tab.call('Page.addScriptToEvaluateOnNewDocument', dict(source=inicio))
            tab.call('Page.navigate', dict(url=url))
            tab.ev(LISTO, timeout=240)
            recogida = tab.ev((ROOT / 'tools/interiores/botin_pruebas.js').read_text(), timeout=120)
            informe['recogida'] = recogida
            tab.ev('window.__documentoAnterior=true;')
            tab.call('Page.reload', {})
            for _ in range(1000):
                try:
                    if tab.ev('!window.__documentoAnterior&&!!window.game'):
                        break
                except RuntimeError as exc:
                    if 'context' not in str(exc).lower():
                        raise
                time.sleep(.1)
            else:
                raise RuntimeError('No se confirma un documento nuevo tras recargar')
            tab.ev(LISTO, timeout=240)
            recarga = tab.ev("({dinero:game.player.money,mochila:game.player.bag||[],evo:localStorage.getItem('guarena_evo_save'),fija:localStorage.getItem('guarena_save'),errores:window.__errs})")
            informe['recarga'] = recarga
            if recarga['dinero'] != recogida['dinero'] or recarga['mochila'] != recogida['mochila']:
                raise RuntimeError('La recompensa no persiste al recargar')
            if recarga['evo'] != 'testigo_evo' or recarga['fija'] != 'testigo_fija':
                raise RuntimeError('Se ha alterado una partida ajena a HQ')
            if recogida['errores'] or recarga['errores']:
                raise RuntimeError('Errores de consola en la prueba')
            informe['estado'] = 'PASS'
    except Exception as exc:
        informe['errores'].append(type(exc).__name__ + ': ' + str(exc))
    destino = ROOT / args.informe
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(json.dumps(informe, ensure_ascii=False, indent=1) + '\n')
    print('Botín:', informe['estado'], '· dos recogidas, recompensa y recarga')
    return 0 if informe['estado'] == 'PASS' else 1


if __name__ == '__main__':
    sys.exit(main())
