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
        # (a building seen from several streets: the surest sighting, and of two as sure the first)
        r = RANK.get(h.get('confidence') or 'media', 1)
        if b in out and rank[b] >= r: continue
        if b not in out: n += 1
        out[b] = o; rank[b] = r
# touched up by hand, after looking (kept through every regeneration): the hermitage of the Plaza Vieja, a chapel — blind
# whitewashed walls, its baroque portal and its bell-gable its own (landmarks.js ermitaPlazaVieja), one tall storey
MANUAL = {1260: {'special': 'capilla', 'floors': 2}}
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
