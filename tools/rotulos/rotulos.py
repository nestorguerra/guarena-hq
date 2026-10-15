# The names on the signs (technical backlog, epic R): one registry, data/rotulos/marcas.json, gives every brand and
# business the game would name its public name — a parody of a brand (never its logo), a generic for a local shop or a
# person's name —, and this tool keeps the published game to it:
#   python3 tools/rotulos/rotulos.py                 → src/rotulos_datos.js (public names only, the game reads it) and
#                                                      data/rotulos/reales.local.json (the real ones: never committed —
#                                                      only a local copy of the game shows them)
#   python3 tools/rotulos/rotulos.py validar FILE    → R-07: no real brand or business name in that build (dist/test.html);
#                                                      V-02: no placeholder text among the texts it shows. Exit 1 if any.
# tools/build.py calls sanear_mapa() on the map it packs: the OpenStreetMap names of shops, bars, banks… become the
# generic of their kind (the game never shows them, but a published copy must not carry them either).
import json, os, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
REG = json.load(open(os.path.join(ROOT, 'data', 'rotulos', 'marcas.json'), encoding='utf-8'))
ENT = REG['entidades']
GEN = REG['genericos_por_tipo']
PUB = set(REG['publicos'])
# (texts no sign, plate or label may show: V-02)
MARCADORES = re.compile(r'\b(TODO|TBD|Lorem|PLACEHOLDER|SIGN_\d+|XXX|Texto)\b')

def titulo(t):
    small = {'de', 'del', 'la', 'las', 'el', 'los', 'y'}
    w = t.lower().split(' ')
    return ' '.join(x if (i and x in small) else x[:1].upper() + x[1:] for i, x in enumerate(w))

def generar():
    pub, real = {}, {}
    for e in ENT:
        if e.get('autorizacion') == 'si':
            pub[e['id']] = {'r': e['real'][0], 'n': e['real'][-1] if e['real'][-1] != e['real'][0] else titulo(e['real'][0])}
            continue
        pub[e['id']] = {'r': e['publico'], 'n': titulo(e['publico'])}
        real[e['id']] = {'r': e['real'][0], 'n': e['real'][-1] if e['real'][-1] != e['real'][0] else titulo(e['real'][0])}
    js = ["// The names on the signs, as the published game shows them (tools/rotulos/rotulos.py from data/rotulos/marcas.json):",
          "// a parody of a brand, a generic for a local business. r: as the sign reads, n: as it is said. Nothing else here:",
          "// a local copy of the game puts the real ones over these (src/rotulos.js, data/rotulos/reales.local.json).",
          'export const ROTULOS = {']
    for k in sorted(pub): js.append(f'  {json.dumps(k)}: {json.dumps(pub[k], ensure_ascii=False)},')
    js.append('};')
    open(os.path.join(ROOT, 'src', 'rotulos_datos.js'), 'w', encoding='utf-8').write('\n'.join(js) + '\n')
    with open(os.path.join(ROOT, 'data', 'rotulos', 'reales.local.json'), 'w', encoding='utf-8') as f:
        json.dump(real, f, ensure_ascii=False, indent=1)
    print('rótulos: %d entidades (%d con nombre real solo en local)' % (len(pub), len(real)))

def entidad_de(texto):
    """the registry's entity whose real name a sign reads (upper case, as the captures show it), or None"""
    t = (texto or '').strip().upper()
    for e in ENT:
        if any(t == r.upper() for r in e['real']): return e
    return None

def _quitar_marcas(s):
    for e in ENT:
        if e.get('autorizacion') == 'si': continue
        for r in sorted(e['real'], key=len, reverse=True):
            s = re.sub(r'(?<![\wÁÉÍÓÚÑáéíóúñ])' + re.escape(r) + r'(?![\wÁÉÍÓÚÑáéíóúñ])', e['publico'] if r.isupper() else titulo(e['publico']), s)
    return s

def sanear_mapa(text):
    """the map packed into a published copy: the names of its shops, bars, banks, offices and works their kind's generic
    (a cooperative stays a cooperative), a brand inside a public place's name its parody; names no longer used, empty"""
    M = json.loads(text)
    names = M['names']
    used_by_edges = {e['n'] for e in M['edges'] if e.get('n', -1) >= 0} | {l['n'] for l in M.get('lines', []) if l.get('n', -1) >= 0}
    extra = {}
    def nuevo(s):
        if s not in extra: extra[s] = len(names) + len(extra)
        return extra[s]
    for coll in ('pois', 'areas'):
        for p in M.get(coll, []):
            n = p.get('n', -1)
            if n is None or n < 0: continue
            nm, k = names[n], p['k']
            if k in PUB:
                s = _quitar_marcas(nm)
                if s != nm: p['n'] = nuevo(s)
            elif re.search('cooperativa', nm, re.I):
                p['n'] = nuevo('Cooperativa agrícola')
            else:
                p['n'] = nuevo(GEN.get(k, 'Comercio'))
    names = names + [s for s, _ in sorted(extra.items(), key=lambda kv: kv[1])]
    used = used_by_edges | {p['n'] for coll in ('pois', 'areas') for p in M.get(coll, []) if p.get('n', -1) >= 0}
    M['names'] = [s if i in used else '' for i, s in enumerate(names)]
    return json.dumps(M, ensure_ascii=False, separators=(',', ':'))

def validar(path):
    page = open(path, encoding='utf-8').read()
    errs = []
    # R-07: no real name of a brand or business, as a word, anywhere in the page
    for e in ENT:
        if e.get('autorizacion') == 'si': continue
        for r in e['real']:
            pat = (r'(?<![\wÁÉÍÓÚÑáéíóúñ])' if r[0].isalnum() else '') + re.escape(r) + r'(?![\wÁÉÍÓÚÑáéíóúñ])'
            # (not inside the packed binary files: there a name can turn up by chance among the encoded bytes)
            def texto(m):  # (a word among words, or a whole string: not a run of packed bytes)
                a, b = page[m.start() - 1:m.start()], page[m.end():m.end() + 1]
                return (a in '"\'' and b in '"\'') or ' ' in page[max(0, m.start() - 12):m.end() + 12]
            n = sum(1 for m in re.finditer(pat, page) if texto(m))
            if n: errs.append(f'R-07 marca «{r}» ({e["id"]}): {n} veces')
    # (and none of the map's own business names, as the strings of its data)
    M = json.load(open(os.path.join(ROOT, 'data', 'map.json'), encoding='utf-8'))
    comerciales = {M['names'][p['n']] for coll in ('pois', 'areas') for p in M.get(coll, []) if p.get('n', -1) >= 0 and p['k'] not in PUB}
    for nm in sorted(comerciales):
        if nm and nm not in GEN.values() and json.dumps(nm, ensure_ascii=False) in page:
            errs.append(f'R-07 comercio del mapa «{nm}» en los datos')
    # V-02: no placeholder among the texts the signs and plates show
    shown = []
    for m in re.finditer(r'"(?:texto|r|n)":\s*"([^"]*)"', page): shown.append(m.group(1))
    for t in shown:
        if MARCADORES.search(t): errs.append(f'V-02 texto de marcador: «{t}»')
    print(json.dumps({'fichero': os.path.relpath(path, ROOT), 'textos_revisados': len(shown), 'errores': errs}, ensure_ascii=False, indent=1))
    return not errs

if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[1] == 'validar':
        sys.exit(0 if validar(sys.argv[2]) else 1)
    generar()
