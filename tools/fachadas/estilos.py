# From the street profiles (written from the user's Google Maps captures by looking and sampling: one JSON per street
# or square, ESQUEMA in the scratchpad) to the game's street styles: src/calles_estilos.js. Only numbers, colours and
# shares come over — nothing of the captures. Rules of thumb turn the profiles' words into the façade generator's
# parameters (which plinths, how many grilles, which kinds of house…); the file it writes is then worth reading and
# touching up by hand.
#   python3 tools/fachadas/estilos.py <profiles dir>
import json, os, re, sys
REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SRC = sys.argv[1]
def hexok(h, d='#f0eee8'):
    return h if isinstance(h, str) and re.fullmatch(r'#[0-9a-fA-F]{6}', h) else d
def has(t, *ws):
    t = (t or '').lower()
    return any(w in t for w in ws)
def plinth_kind(txt):
    t = (txt or '').lower()
    if has(t, 'sin zócalo', 'ninguno', 'sin zocalo') or (has(t, 'cal manchada', 'manchada de humedad') and not has(t, 'pintad')): return 'ninguno'
    if has(t, 'azulejo', 'plaqueta', 'cerámic', 'ceramic', 'gres'): return 'azulejo'
    if has(t, 'mampost', 'piedra vista', 'irregular', 'lajas', 'pizarra', 'rústic', 'rustic'): return 'piedra'
    if has(t, 'granito', 'piedra', 'mármol', 'marmol', 'chapado', 'sillar', 'abujard', 'placas'): return 'granito'
    if has(t, 'cemento', 'mortero', 'hormigón', 'hormigon', 'enfoscado gris', 'tirolesa', 'tirol'): return 'cemento'
    return 'pintado'
def number(txt, lo, hi, d):
    m = re.findall(r'(\d+(?:[.,]\d+)?)', txt or '')
    vals = [float(x.replace(',', '.')) for x in m]
    vals = [v for v in vals if lo <= v <= hi]
    return sum(vals) / len(vals) if vals else d
SPECIES = (('naranj', 'naranjo'), ('morera', 'morera'), ('plátano', 'platano'), ('platano', 'platano'), ('palmera', 'palmera'), ('olivo', 'olivo'))
# touched up by hand, after looking (kept through every regeneration)
MANUAL = {
    # (setts only on its west stretch, Plaza la Parada–Malfeitos; asphalt beyond)
    'Calle Estacada': {'road': 'asfalto', 'arboles': None, 'tramos': [{'x': 20, 'z': -74, 'r': 90, 'road': 'adoquin', 'col': '#b5aea4'},
                                                                  {'x': 371, 'z': -75, 'r': 70, 'arboles': {'kind': 'platano', 'every': 8}}]},  # (plane trees only at its Don Benito end)
    # (granite setts from the Plaza de España; its south stretch and the little square by the market one level of light
    # concrete setts, no kerbs)
    'Calle Pajares': {'road': 'adoquin', 'tramos': [{'x': 132, 'z': 20, 'r': 30, 'road': 'adoquin_plataforma', 'col': '#c4c0b6'}]},
    # (its pavements as its captures show them: the white and red diagonal chequer on its north stretch; red with a chain
    # of white diamonds by Correos (east side); white with two rows of red squares by the kerb on the east side of its
    # south stretch, grey on the west)
    'Calle Malfeitos': {'acera': {'col': '#efebe5', 'pat': 1}, 'tramos': [
        {'x': 110.5, 'z': -146, 'r': 11, 'lado': 'E', 'acera': {'col': '#efebe5', 'pat': 3}},
        {'x': 131, 'z': -42, 'r': 46, 'lado': 'E', 'acera': {'col': '#efebe5', 'pat': 2}},
        {'x': 131, 'z': -42, 'r': 46, 'lado': 'O', 'acera': {'col': '#9a948c', 'pat': 0}}]},
    # (its garden: packed albero, no grass; big broad-crowned trees — acacias or Japanese pagoda trees, here plane trees
    # and mulberries — a cedar, a low clipped privet hedge round it; no palms)
    'Plaza Federico García Lorca': {'parque': {'x': 911, 'z': 235, 'r': 40, 'suelo': 'albero', 'escala': 1.4, 'especies': [['morera', 0.45], ['platano', 0.4], ['pino', 0.15]]}},  # (10–12 m tall, their crowns meeting)
    # (its garden: bare dusty earth, light-crowned trees — chinaberries, here mulberries — wooden benches, a slab path; no
    # lawn, no ball hedges, no palms)
    'Plaza Ramón y Cajal': {'parque': {'x': 498, 'z': -185, 'r': 30, 'suelo': 'albero', 'escala': 1.1, 'especies': [['morera', 0.85], ['platano', 0.15]]}},
    # (the market's own square, as the Plaza de Abastos: open paving, no grove — the map names it apart)
    'Mercado de Abastos': {'arboles': None},
    # (slabs on its north stretch, granite setts on the south one)
    'Calle Túnel': {'road': 'losa', 'tramos': [{'x': -16, 'z': 14, 'r': 12, 'road': 'adoquin'}]},
    # (light concrete setts with pink pieces, almost level with the pavement, at its north access; grey setts at its
    # south end — the asphalt is its west branch's, a street of its own in the map)
    'Calle Cañadilla': {'road': 'adoquin', 'roadCol': '#b3a99c', 'tramos': [{'x': -69, 'z': -164, 'r': 20, 'road': 'adoquin', 'col': '#8f8a80'}]},
}
out = {}
for f in sorted(os.listdir(SRC)):
    if not f.endswith('.json'): continue
    d = json.load(open(os.path.join(SRC, f)))
    s = d.get('style', {})
    st = {}
    # paint: what is paint (brick, cladding and stone fronts are their own kinds)
    walls = []
    for w in s.get('walls', []):
        what = w.get('what', '')
        mat = 'ladrillo' if has(what, 'ladrillo') and not has(what, 'pintad') else 'piedra' if has(what, 'granito', 'sillería', 'mampost') and has(what, 'toda', 'fachada') else None
        walls.append([hexok(w.get('hex')), round(float(w.get('share', 0.1)), 3)] + ([mat] if mat else []))
    if walls: st['walls'] = walls
    # the kinds of house: blocks of three floors and more modern; carpentry in green, the old kind with green; the rest
    # old (dark wood) and renovated (aluminium, PVC) in the proportion the words suggest
    fl = s.get('floors', {}) or {}
    tall = sum(v for k, v in fl.items() if str(k).isdigit() and int(k) >= 4)
    win = s.get('windows', {}) or {}
    txt = ' '.join(str(v) for v in win.values()) + ' ' + json.dumps(s.get('doors', {}), ensure_ascii=False)
    green = 0.25 if has(txt, 'verde') else 0.04
    alu = 0.45 if has(txt, 'aluminio', 'pvc', 'enrollable') else 0.25
    old = max(0.1, 1 - tall - green - alu)
    st['kinds'] = {k: round(v, 3) for k, v in {'trad_ocre': old, 'trad_verde': green, 'renovada': alu * 0.7, 'color': alu * 0.3, 'moderna': tall}.items() if v > 0.005}
    # plinths: the kinds seen, and the houses without one
    pl = s.get('plinth', {}) or {}
    kinds = []
    for k in pl.get('kinds', []) or []:
        kd = plinth_kind(k.get('kind'))
        kinds.append({'kind': kd, 'col': hexok(k.get('hex'), '#9a958e'), 'h': round(float(k.get('height_m') or 0.9), 2), 'share': round(float(k.get('share', 0.1)), 3)})
    shp = float(pl.get('share', 0.7) or 0)
    tot = sum(k['share'] for k in kinds) or 1
    for k in kinds: k['share'] = round(k['share'] / tot * shp, 3)
    if shp < 0.99: kinds.append({'kind': None, 'share': round(1 - shp, 3)})
    if kinds: st['plinth'] = kinds
    # surrounds
    su = s.get('surrounds', {}) or {}
    if su:
        st['surround'] = {'share': round(float(su.get('share', 0.3) or 0), 3), 'col': hexok(su.get('hex'), '#f6f3ec')}
        if has(su.get('kind'), 'piedra', 'granito', 'sillar'): st['surround']['kind'] = 'piedra'
    # grilles
    rj = s.get('rejas', {}) or {}
    gtxt = (win.get('ground') or '') + ' ' + json.dumps(rj, ensure_ascii=False)
    share = rj.get('share')
    if share is None: share = 0.75 if has(gtxt, 'reja') else 0.3
    if has(win.get('ground'), 'sin reja') and share > 0.6: share = 0.55
    buche = rj.get('buche_share')
    if buche is None: buche = 0.4 if has(gtxt, 'panza', 'cajón', 'cajon', 'volada', 'buche', 'abombad') else 0.1
    st['reja'] = {'share': round(float(share), 3), 'col': hexok(rj.get('hex'), '#1e1e1e'), 'buche': round(float(buche), 3)}
    # balconies (of each upper window), garages (of each ground bay)
    bc = s.get('balconies', {}) or {}
    st['balc'] = round(min(0.7, 0.55 * float(bc.get('share_of_houses', 0.3) or 0)), 3)
    g = s.get('garages', '') or ''
    st['garage'] = 0.02 if has(g, 'ninguna', 'casi ninguna', 'no hay', 'no se ven') else 0.2 if has(g, 'frecuente', '1 de cada 4', 'muchas') else 0.06 if has(g, 'alguna', 'pocas', 'escasa', 'aislad') else 0.08
    # colours of the carpentry
    sh = (win.get('shutters') or '').lower()
    st['shutters'] = '#6b4a2e' if sh.startswith('persiana') and has(sh.split(';')[0], 'marrón', 'marron') else '#8a8d90' if has(sh.split(';')[0], 'gris') else '#f2f0ea'
    st['frames'] = hexok(win.get('frames_hex'), '#ece9e2')
    st['door'] = hexok((s.get('doors') or {}).get('hex'), '#5a3a24')
    # the fronts' tops: a parapet (pretil) before the roof, or the tile eaves
    co = s.get('cornice', {}) or {}
    ck = (co.get('kind') or '').lower()
    st['pretil'] = round(min(0.9, float(co.get('share') or 0.6)), 3) if has(ck, 'pretil', 'cornisa', 'peto') and not ck.startswith('teja') else 0.2
    # pots (the real streets have very few: never more than one doorstep in eight), lamps, cables
    ex = ' '.join(s.get('extras', []) or [])
    st['pots'] = 0.03 if has(ex, 'ninguna maceta', 'sin macetas', 'apenas macetas', 'pocas macetas') else 0.12 if has(ex, 'macetas') else 0.06
    lamps = s.get('lamps', '') or ''
    # (lanterns on the fronts, or lamp posts on the pavement — the newer quarters' — whichever the profile names first)
    lt = lamps.lower()
    ip = min([lt.find(w) for w in ('columna', 'báculo', 'baculo', 'farola de pie', 'poste') if lt.find(w) >= 0] or [10 ** 6])
    iw = min([lt.find(w) for w in ('ménsula', 'mensula', 'fachada', 'pared', 'brazo') if lt.find(w) >= 0] or [10 ** 6])
    st['lamps'] = {'every': round(number(lamps.split('cada')[1] if 'cada' in lamps else '', 6, 60, 22), 1), 'kind': 'columna' if ip < iw else 'pared'}
    if has(ex, 'cable'): st['cables'] = True
    # the road: granite setts, slabs (one level, no kerbs) or asphalt — the first the profile names
    rd = ((s.get('pavement') or {}).get('road') or '').lower()
    ia, il, ias = rd.find('adoqu'), min([i for i in (rd.find('losa'), rd.find('plataforma')) if i >= 0] or [-1]), rd.find('asfalt')
    firsts = sorted([(i, k) for i, k in ((ia, 'adoquin'), (il, 'losa'), (ias, 'asfalto')) if i >= 0])
    st['road'] = firsts[0][1] if firsts else 'asfalto'
    # the asphalt's colour, as measured (pale and warm where it is old: ground.js tints the street to it)
    rh = hexok((s.get('pavement') or {}).get('road_hex'), None)
    if rh: st['roadCol'] = rh
    # the pavement: its tiles' colour (the first the profile gives) and, for the hydraulic tiles in red and white, their
    # pattern — 1 a diagonal chequer, 2 two rows of squares along the kerb, 3 red with white diamonds, 4 all red
    pvm = s.get('pavement') or {}
    shx = pvm.get('sidewalk_hex'); shx = shx if isinstance(shx, list) else [shx] if shx else []
    main = hexok(shx[0], None) if shx else None
    sw = (pvm.get('sidewalk') or '').split(';')[0].lower()
    pat = 1 if 'damero' in sw else 2 if ('hilera' in sw and 'roj' in sw) else 3 if ('cadeneta' in sw or 'rombos blancos' in sw) else 4 if sw.startswith('baldosa roja') else 0
    if main and not has(sw, 'sin acera', 'no hay acera'): st['acera'] = {'col': main, 'pat': pat}
    # the paint on the road, where its captures show some (the old town's have none; the avenues of the newer quarters
    # a centre line, some a parking lane)
    rtxt = (pvm.get('road') or '').lower()
    no = has(rtxt, 'sin marcas', 'sin línea', 'sin linea', 'sin pintar', 'sin señaliz')
    centro = not no and has(rtxt, 'línea central', 'linea central', 'línea discontinua', 'linea discontinua', 'eje pintado', 'línea continua', 'doble línea', 'carriles pintados')
    aparc = has(rtxt, 'líneas de aparcamiento', 'lineas de aparcamiento', 'línea de aparcamiento', 'línea blanca de aparcamiento', 'plazas pintadas', 'plazas de aparcamiento pintadas', 'banda de aparcamiento')
    if centro or aparc: st['lineas'] = {'centro': centro, 'aparcamiento': aparc}
    # trees in pits along the pavement, where the captures show them: their species and how far apart (a median's, a
    # park's or a garden's are not the pavement's)
    for item in s.get('extras', []) or []:
        t = (item or '').lower()
        sp = next((k for w, k in SPECIES if w in t), None)
        if not sp or not has(t, 'alcorque', 'en la acera', 'alineados', 'alineadas', 'en hilera', 'cada') or has(t, 'mediana', 'parque', 'jardín', 'jardin', 'al fondo', 'patio', 'atrio'): continue
        st['arboles'] = {'kind': sp, 'every': round(number(t.split('cada')[1] if 'cada' in t else '', 4, 30, 8), 1),
                         'escala': 0.6 if has(t, 'joven', 'jóvenes', 'arbolito', 'pequeñ', 'recién plantad') else 1}
        break
    # a median between two carriageways, where the captures show one: its trees (species, how far apart, young or grown),
    # its lamp posts and benches
    alltxt = (d.get('summary_es') or '') + ' | ' + ' | '.join(s.get('extras', []) or [])
    mm = re.search(r'[^.|;]*mediana[^.|;]*', alltxt, re.I)
    if mm and not has(mm.group(0), 'avenida de la constitución', 'sin árboles'):
        t = mm.group(0).lower()
        sp = next((k for w, k in SPECIES if w in t), 'morera' if has(t, 'árbol', 'arbol', 'arbolito') else None)
        if sp:
            st['mediana'] = {'arbol': sp, 'cada': round(number(t.split('cada')[1] if 'cada' in t else '', 4, 20, 8), 1),
                             'escala': 0.7 if has(t, 'joven', 'jóvenes', 'arbolito', 'pequeñ') else 0.95,
                             'farolas': has(t, 'farola', 'báculo', 'baculo', 'columna'), 'bancos': has(t, 'banco')}
    # rows of terraced houses (adosados) the map has as one long building each: how wide each house is
    summ = (d.get('summary_es') or '') + ' ' + (s.get('vs_game') or '')
    if has(summ, 'adosad', 'hilera de casas', 'hileras de casas', 'misma promoción', 'misma promocion'):
        m = re.search(r'(\d+(?:[.,]\d+)?)\s*(?:[–-]\s*(\d+(?:[.,]\d+)?))?\s*m de fachada', summ)
        w = (float(m.group(1).replace(',', '.')) + float((m.group(2) or m.group(1)).replace(',', '.'))) / 2 if m else 6.5
        st['adosados'] = {'w': round(min(12, max(4, w)), 2)}
    name = d.get('street') or f[:-5]
    st.update(MANUAL.get(name, {}))
    out[name] = st
# (the touches for places without a profile of their own: the market's square, say)
for k, v in MANUAL.items():
    if k not in out: out[k] = dict(v)
js = ['// The styles of the town\'s streets and squares, written from the user\'s Google Maps captures of each (2026-10-12/13) — see',
      '// calles.js. Made by tools/fachadas/estilos.py from the street profiles, then read and touched up by hand. Nothing',
      '// of the captures is in it: colours sampled and measures read, as numbers.',
      'export const STYLES = {']
for k, v in out.items():
    js.append(f'  {json.dumps(k, ensure_ascii=False)}: {json.dumps(v, ensure_ascii=False)},')
js.append('};')
open(os.path.join(REPO, 'src', 'calles_estilos.js'), 'w').write('\n'.join(js) + '\n')
print(len(out), 'estilos:', ', '.join(out))
