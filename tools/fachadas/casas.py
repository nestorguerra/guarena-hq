# From the per-house notes (one JSON list per street: which building of the map each house of the captures is, and what
# it looks like — CASAS.md in the scratchpad) to the game's src/calles_casas.js. Only buildings identified with
# confidence «alta» or «media» come over; numbers and words only, nothing of the captures.
#   python3 tools/fachadas/casas.py <casas dir>
import json, os, re, sys
REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SRC = sys.argv[1]
ok = lambda h: h if isinstance(h, str) and re.fullmatch(r'#[0-9a-fA-F]{6}', h) else None
KINDS = {'granito', 'piedra', 'azulejo', 'cemento', 'pintado', 'ninguno'}
out, rank, n = {}, {}, 0
RANK = {'alta': 2, 'media': 1}
for f in sorted(os.listdir(SRC)):
    if not f.endswith('.json'): continue
    for h in json.load(open(os.path.join(SRC, f))):
        b = h.get('bid')
        if not isinstance(b, int) or (h.get('confidence') or 'media') == 'baja': continue
        o = {}
        if ok(h.get('wall_hex')): o['wall'] = ok(h['wall_hex'])
        sp = (h.get('special') or '') or None
        if sp in ('ladrillo', 'piedra', 'chapado', 'tapia', 'capilla'): o['special'] = sp
        p = h.get('plinth') or {}
        k = (p.get('kind') or '').split()[0].lower() if p.get('kind') else None
        if k in KINDS: o['plinth'] = {'kind': k, 'col': ok(p.get('hex')) or '#9a958e', 'h': round(float(p.get('height_m') or 0.9), 2)}
        s = h.get('surround') or {}
        if s.get('kind'): o['surround'] = {'kind': s['kind'] if s['kind'] in ('pintado', 'piedra', 'ninguno') else 'pintado', 'col': ok(s.get('hex')) or '#f6f3ec'}
        if isinstance(h.get('reja'), bool): o['reja'] = h['reja']
        if isinstance(h.get('reja_buche'), bool): o['buche'] = h['reja_buche']
        if isinstance(h.get('balconies'), bool): o['balc'] = h['balconies']
        if isinstance(h.get('pretil'), bool): o['pretil'] = h['pretil']
        if isinstance(h.get('floors'), int) and 1 <= h['floors'] <= 8: o['floors'] = h['floors']  # (as many as are seen: the Catastro's are sometimes not)
        for a, k2 in (('door_hex', 'door'), ('shutters_hex', 'shutters'), ('frames_hex', 'frames')):
            if ok(h.get(a)): o[k2] = ok(h[a])
        # (what the audit of 2026-10-13 asked for, when the notes give it: CORRECCIONES.md in the scratchpad)
        fz = h.get('fachada')
        if isinstance(fz, dict):
            fz = {k: v.upper() for k, v in fz.items() if re.fullmatch(r'p(b|[1-9])', k) and isinstance(v, str) and re.fullmatch(r'[PVCBT-]{1,40}', v.upper())}
            if fz: o['fachada'] = fz; o['frente'] = h['frente'] if isinstance(h.get('frente'), str) and h['frente'] else f[:-5]  # (its bays on the front to this street — or to the one of the map the notes name)
        for k in ('azotea', 'toldos', 'macetas', 'ciega', 'bajantes'):
            if isinstance(h.get(k), bool): o[k] = h[k]
        c = h.get('cerramiento')
        if isinstance(c, dict) and c.get('tipo') in ('verja', 'murete', 'malla', 'celosia'):
            o['cerramiento'] = {'tipo': c['tipo'], 'col': ok(c.get('hex') or c.get('col')) or '#1e1e1e', 'murete': ok(c.get('murete_hex') or c.get('murete')) or '#efede6',
                                'h': round(min(2.5, max(0.6, float(c.get('h') or c.get('height_m') or 1.5))), 2)}
            if isinstance(c.get('fondo'), (int, float)) and 0.4 <= c['fondo'] <= 8: o['cerramiento']['fondo'] = round(float(c['fondo']), 2)  # (its front garden that deep, m)
        for k in ('pilastras', 'impostas', 'cornisa', 'teja'):
            if ok(h.get(k)): o[k] = ok(h[k])
        if isinstance(h.get('alto'), (int, float)) and 2.2 <= h['alto'] <= 30: o['alto'] = round(float(h['alto']), 2)  # (its walls' height as seen, m: every part of it)
        if isinstance(h.get('placas'), bool): o['placas'] = h['placas']  # (solar panels on its roof, or none)
        sp2 = h.get('soportal')
        if isinstance(sp2, dict) and isinstance(sp2.get('fondo'), (int, float)) and 1 <= sp2['fondo'] <= 6: o['soportal'] = {'fondo': round(float(sp2['fondo']), 2), **({'arcos': True} if sp2.get('arcos') is True else {})}  # (its ground floor back behind pillars, m)
        # (and what the second round of 2026-10-14 asked for: its wall's colour on its front to another street, its air
        # conditioners, aerials, the wiring stapled along it, its shop's sign, its letter boxes)
        pi = h.get('pinturas')  # (one building of the map that is several houses: their paints left to right along its front, m)
        if isinstance(pi, list):
            pi = [{'m': round(float(q['metros']), 2), 'hex': ok(q.get('hex'))} for q in pi if isinstance(q, dict) and isinstance(q.get('metros'), (int, float)) and 0.5 <= q['metros'] <= 80 and ok(q.get('hex'))]
            if len(pi) >= 2: o['pinturas'] = pi
        mu = h.get('muros')
        if isinstance(mu, dict):
            mu = {k: ok(v) for k, v in mu.items() if isinstance(k, str) and ok(v)}
            if mu: o['muros'] = mu
        a = h.get('aires')
        if isinstance(a, bool) or (isinstance(a, (int, float)) and 0 <= a <= 1): o['aires'] = a
        if isinstance(h.get('antenas'), int) and 0 <= h['antenas'] <= 4: o['antenas'] = h['antenas']
        for k in ('parabolica', 'cables', 'buzones', 'atrezo'):
            if isinstance(h.get(k), bool): o[k] = h[k]
        ro = h.get('rotulo')
        if isinstance(ro, dict) and (ok(ro.get('fondo')) or ro.get('texto')):
            o['rotulo'] = {'texto': str(ro.get('texto') or '')[:28], 'fondo': ok(ro.get('fondo')) or '#2b4f7a', 'letra': ok(ro.get('letra')) or '#ffffff',
                           'donde': 'banderola' if ro.get('donde') == 'banderola' else 'fachada'}
            if isinstance(ro.get('pos'), (int, float)) and 0 <= ro['pos'] <= 1: o['rotulo']['pos'] = round(float(ro['pos']), 3)  # (along its front: 0 its left end, 1 its right)
        # (and the last round's, 14-oct night: its front moved where the Catastro has it out of place, its awnings' colour,
        # a glazed bay, a pergola on its roof, a lattice of pierced blocks, no laundry out, a painted panel)
        mf = h.get('mover_frente')
        if isinstance(mf, dict) and isinstance(mf.get('m'), (int, float)) and 0.05 <= abs(mf['m']) <= 4:
            o['mover_frente'] = {'m': round(float(mf['m']), 2), **({'calle': mf['calle']} if isinstance(mf.get('calle'), str) and mf['calle'] else {}), **({'rumbo': float(mf['rumbo'])} if isinstance(mf.get('rumbo'), (int, float)) else {})}
        tl = h.get('toldo')
        if ok(tl): o['toldo'] = {'hex': ok(tl), 'rayas': False}
        elif isinstance(tl, dict) and ok(tl.get('hex')): o['toldo'] = {'hex': ok(tl['hex']), 'rayas': bool(tl.get('rayas'))}
        num = lambda d, k, lo, hi, df: round(float(d[k]), 2) if isinstance(d.get(k), (int, float)) and lo <= d[k] <= hi else df
        for k, dims in (('cierro', (0.8, 6, 1.6)), ('celosia', (0.3, 8, 1.0)), ('mural', (0.5, 20, 3.0))):
            v = h.get(k)
            if isinstance(v, dict):
                q = {'planta': int(num(v, 'planta', 0, 6, 1 if k == 'cierro' else 0)), 'pos': num(v, 'pos', 0, 1, 0.5), 'ancho': num(v, 'ancho', dims[0], dims[1], dims[2]),
                     'alto': num(v, 'alto', 0.3, 12, 1.4 if k != 'mural' else 2.5)}
                if k == 'mural':
                    cols = [ok(c) for c in v.get('colores', []) if ok(c)]
                    if not cols: continue
                    q['colores'] = cols[:6]; q['y'] = num(v, 'y', 0, 15, 0.4)
                else: q['hex'] = ok(v.get('hex')) or ('#f2f0ea' if k == 'celosia' else '#2a2c2e')
                o[k] = q
        pg = h.get('pergola')
        if pg is True or (isinstance(pg, dict) and ok(pg.get('hex'))): o['pergola'] = {'hex': ok(pg.get('hex')) if isinstance(pg, dict) else '#3a3c3e'}
        if isinstance(h.get('ropa'), bool): o['ropa'] = h['ropa']
        if ok(h.get('cochera')): o['cochera'] = ok(h['cochera'])  # (its garage door's colour)
        if isinstance(h.get('arcos_ventanas'), bool): o['arcos_ventanas'] = h['arcos_ventanas']  # (arched tops over its windows and balcony doors)
        if h.get('barandilla') in ('balaustres', 'forja', 'barrotes'): o['barandilla'] = h['barandilla']
        if ok(h.get('reja_hex')): o['reja_hex'] = ok(h['reja_hex'])  # (its grilles' and railings' colour)
        if isinstance(h.get('chimeneas'), int) and 0 <= h['chimeneas'] <= 4: o['chimeneas'] = h['chimeneas']
        for k in ('todas_fachadas', 'nave'):  # (nave: false — a house the Catastro registers as a store or a workshop)
            if isinstance(h.get(k), bool): o[k] = h[k]
        if h.get('tejado') in ('dos_aguas', 'cuatro_aguas', 'hastial'): o['tejado'] = h['tejado']
        cn = h.get('canecillos')
        if cn is True or ok(cn): o['canecillos'] = ok(cn) or True
        pt = h.get('partir')  # (one building of the map that is two of different heights: cut square to its front, m from its left end)
        if isinstance(pt, dict) and all(isinstance(pt.get(k), (int, float)) for k in ('metros', 'alto_izq', 'alto_der')) and 0.5 <= pt['metros'] <= 100 and 2.2 <= pt['alto_izq'] <= 30 and 2.2 <= pt['alto_der'] <= 30:
            o['partir'] = {'metros': round(float(pt['metros']), 2), 'alto_izq': round(float(pt['alto_izq']), 2), 'alto_der': round(float(pt['alto_der']), 2), **({'calle': pt['calle']} if isinstance(pt.get('calle'), str) and pt['calle'] else {}), **({'rumbo': float(pt['rumbo'])} if isinstance(pt.get('rumbo'), (int, float)) else {})}
        if isinstance(h.get('arcos_puertas'), bool): o['arcos_puertas'] = h['arcos_puertas']  # (round arches over its doors and garages)
        d = h.get('desconchada')
        if isinstance(d, list) and len(d) == 2 and d[1] in ('ocre', 'gris', 'blanco'): o['desconchada'] = [max(1, min(3, int(d[0]))), d[1]]
        cb = h.get('cubierta')
        if isinstance(cb, dict) and ok(cb.get('col')): o['cubierta'] = {k: cb[k] for k in ('col', 'calle', 'una', 'alto') if k in cb}
        if isinstance(h.get('special'), str) and h['special'] in ('ladrillo', 'piedra', 'chapado', 'tapia', 'capilla'): o['special'] = h['special']
        # (a building seen from several streets: the surest sighting first, and of two as sure the first read; what the
        # others saw and it did not — its front to another street, its parapet, its panels — added from them)
        r = RANK.get(h.get('confidence') or 'media', 1)
        if b not in out: n += 1; out[b] = o; rank[b] = r; continue
        base, extra = (o, out[b]) if r > rank[b] else (out[b], o)
        # (its fronts to different streets, each read from its own: all of them, by street)
        if 'fachada' in extra and 'fachada' in base and extra.get('frente') != base.get('frente'):
            fs = base.setdefault('fachadas', {base.get('frente', ''): base['fachada']})
            fs.setdefault(extra.get('frente', ''), extra['fachada'])
        for k, val in extra.items():
            if k in ('frente', 'fachadas'): continue
            if k not in base:
                base[k] = val
                if k == 'fachada' and 'frente' in extra: base['frente'] = extra['frente']
        out[b] = base; rank[b] = max(r, rank[b])
# touched up by hand, after looking (kept through every regeneration): the hermitage of the Plaza Vieja, a chapel — blind
# whitewashed walls, its baroque portal and its bell-gable its own (landmarks.js ermitaPlazaVieja), one tall storey
MANUAL = {1260: {'special': 'capilla', 'floors': 2},
          # (the blocks of flats of 1983 on their arcades — soportales: the ground floor stands back behind square pillars,
          # pillars and wall painted as the plinth seen, as deep as the notes measure them: Gerardo Diego, Miguel Hernández)
          457: {'soportal': {'fondo': 2.6}}, 458: {'soportal': {'fondo': 2.4}},
          # (roofs of corrugated sheet painted red, as seen: Gerardo Diego's big shed behind its blind front of 4 m, its slope
          # towards the street seen over it — calle: its ridge along the street, the gable at its far end; the new sheds by
          # the Manchita road and on the Alberquilla's estate maroon, the one of Palacios reddish, the hut in the car park of
          # Santa María rust red)
          294: {'cubierta': {'col': '#a5584c', 'calle': True, 'alto': 4.0}, 'ciega': True}, 141: {'cubierta': {'col': '#a0625a'}}, 97: {'cubierta': {'col': '#8a4c48', 'calle': True}},  # (97: its ridge along the street, as seen: view 163)
          1914: {'cubierta': {'col': '#b06c5e'}}, 2783: {'cubierta': {'col': '#8a3b32', 'alto': 3.2}},
          # (the whitewash peeling off: how much — 1 along the foot of the wall, 2 patches, 3 big ones all over — and what shows
          # under it: 'ocre' the old ochre render and the earth, 'gris' grey mortar or masonry, 'blanco' white render under a
          # coat of colour — as the notes describe each)
          261: {'desconchada': [3, 'ocre']}, 2885: {'desconchada': [2, 'ocre']}, 1262: {'desconchada': [1, 'ocre']},
          1264: {'desconchada': [1, 'ocre']}, 1270: {'desconchada': [1, 'gris']}, 1410: {'desconchada': [3, 'gris']},
          1306: {'desconchada': [3, 'gris']}, 1730: {'desconchada': [3, 'ocre']}, 2731: {'desconchada': [3, 'blanco']},
          2727: {'desconchada': [2, 'gris']}, 1715: {'desconchada': [3, 'ocre']}, 3274: {'desconchada': [2, 'ocre']},
          3407: {'desconchada': [1, 'gris']}, 2915: {'desconchada': [2, 'gris']}, 2862: {'desconchada': [1, 'gris']}}
for b, o in MANUAL.items():
    if b not in out: n += 1
    out[b] = {**out.get(b, {}), **o}
js = ["// The houses of the town seen one by one in the user's Google Maps captures (2026-10-12/13): for each, which building",
      "// of the map it is and what it looks like — written by tools/fachadas/casas.py from the per-house notes (calles.js).",
      "// Nothing of the captures is in it: colours sampled and features read, as numbers and words.",
      'export const CASAS = {']
for b in sorted(out): js.append(f'  {b}: {json.dumps(out[b], ensure_ascii=False)},')
js.append('};')
open(os.path.join(REPO, 'src', 'calles_casas.js'), 'w').write('\n'.join(js) + '\n')
print(n, 'casas')
