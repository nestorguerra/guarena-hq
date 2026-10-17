"""Recoger dos objetos próximos y comprobar su recompensa tras una recarga real.

Usa el Chrome sin sonido de pruebas y un contexto privado; no carga partidas del usuario.
No mide rendimiento ni comprueba diálogos o reaparición del botín al volver a una casa.
"""
import argparse
from contextlib import ExitStack
import json
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools/perf'))
from beta import PrivateTab
from integracion import LISTO

RENDER = r"""(()=>{const g=window.game,r=g?.renderer,gl=r?.getContext(),d=gl?.getExtension('WEBGL_debug_renderer_info');return {calidad:g?.qKey,automatica:g?.autoQuality,dpr:r?.getPixelRatio(),tamano:r?[r.domElement.width,r.domElement.height]:null,renderer:d?gl.getParameter(d.UNMASKED_RENDERER_WEBGL):null};})()"""


def diagnosticar(tab, informe):
    if informe['estado'] != 'FAIL':
        return
    try:
        informe['diagnostico'] = tab.ev("({documento:document.readyState,estado:window.game?.state,carga:document.getElementById('loading')?.textContent,carga_oculta:document.getElementById('loading')?.hidden,jugador:!!window.game?.player,personaje:!!window.game?.player?.char,intro:window.guarenaIntroTimes,vuelo:window.guarenaIntro?.flying,cinematica:!!window.game?.cam?.cinematic,renderizado:" + RENDER + ",errores:window.__errs})", timeout=5)
    except Exception as exc:
        informe['diagnostico_error'] = type(exc).__name__ + ': ' + str(exc)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    origen = parser.add_mutually_exclusive_group()
    origen.add_argument('--url')
    origen.add_argument('--paquete', action='store_true')
    parser.add_argument('--calidad', choices=['alta', 'baja'], default='alta', help='Perfil de render para la prueba funcional; no puntúa calidad visual')
    parser.add_argument('--informe', default='data/interiores/validacion/botin.json')
    args = parser.parse_args()
    url = args.url or ('http://localhost:8920/' + ('dist/test.html' if args.paquete else 'index.html') + '?estilo=plastilina')
    informe = dict(estado='FAIL', url=url, alcance='selector real, recompensa y recarga; residentes retirados', errores=[])
    fixture = dict(quality=args.calidad, qualityMode='manual', dynRes=False, weatherLive=False, pick='annie', money=321, bag=[])
    inicio = "if(!sessionStorage.getItem('botin_fixture')){localStorage.setItem('guarena_hq_save'," + json.dumps(json.dumps(fixture)) + ");localStorage.setItem('guarena_evo_save','testigo_evo');localStorage.setItem('guarena_save','testigo_fija');sessionStorage.setItem('botin_fixture','1');}"
    try:
        with ExitStack() as cierre:
            tab = cierre.enter_context(PrivateTab())
            cierre.callback(diagnosticar, tab, informe)
            informe['etapa'] = 'arranque inicial'
            tab.call('Emulation.setDeviceMetricsOverride', dict(width=1280, height=720, deviceScaleFactor=1, mobile=False))
            tab.call('Page.addScriptToEvaluateOnNewDocument', dict(source=inicio))
            tab.call('Page.navigate', dict(url=url))
            tab.ev(LISTO, timeout=240)
            informe['renderizado'] = tab.ev(RENDER)
            if informe['renderizado']['calidad'] != args.calidad or informe['renderizado']['automatica']:
                raise RuntimeError('No se ha aplicado el perfil manual solicitado')
            informe['etapa'] = 'recogida'
            recogida = tab.ev((ROOT / 'tools/interiores/botin_pruebas.js').read_text(), timeout=120)
            informe['recogida'] = recogida
            informe['etapa'] = 'documento de recarga'
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
            informe['etapa'] = 'arranque tras recarga'
            tab.ev(LISTO, timeout=240)
            informe['renderizado_tras_recarga'] = tab.ev(RENDER)
            if informe['renderizado_tras_recarga']['calidad'] != args.calidad or informe['renderizado_tras_recarga']['automatica']:
                raise RuntimeError('No se conserva el perfil manual al recargar')
            informe['etapa'] = 'persistencia'
            recarga = tab.ev("({dinero:game.player.money,mochila:game.player.bag||[],evo:localStorage.getItem('guarena_evo_save'),fija:localStorage.getItem('guarena_save'),errores:window.__errs})")
            informe['recarga'] = recarga
            if recarga['dinero'] != recogida['dinero'] or recarga['mochila'] != recogida['mochila']:
                raise RuntimeError('La recompensa no persiste al recargar')
            if recarga['evo'] != 'testigo_evo' or recarga['fija'] != 'testigo_fija':
                raise RuntimeError('Se ha alterado una partida ajena a HQ')
            if recogida['errores'] or recarga['errores']:
                raise RuntimeError('Errores de consola en la prueba')
            informe['estado'] = 'PASS'
            informe['etapa'] = 'completado'
    except Exception as exc:
        informe['estado'] = 'FAIL'
        informe['errores'].append(type(exc).__name__ + ': ' + str(exc))
    destino = ROOT / args.informe
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(json.dumps(informe, ensure_ascii=False, indent=1) + '\n')
    print('Botín:', informe['estado'], '· dos recogidas, recompensa y recarga')
    if informe['estado'] == 'FAIL':
        print(json.dumps({k: informe[k] for k in ('etapa', 'errores', 'diagnostico', 'diagnostico_error') if k in informe}, ensure_ascii=False))
    return 0 if informe['estado'] == 'PASS' else 1


if __name__ == '__main__':
    sys.exit(main())
