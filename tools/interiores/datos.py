# The interiors' data, checked and handed to the game (technical backlog, I-02, X-01, X-02):
#  - every object of data/objetos/*.json against data/interaction.schema.json; its mass inside its category's range
#    and its class the one its mass gives (data/mass_ranges.json) — or a reason written for the exception; a FIXED one
#    with its reason (anclado en la realidad, estructural, rendimiento, diseño);
#  - I-07: its id in the project's naming (lower case, digits, underscores), no more than 5,000 triangles (more would
#    need levels of detail), and the colours of its parts a physical albedo (warnings: very dark or very bright paint);
#  - its surfaces at the height of a part's top (what stands on it, on it: not in it, not above it), and nothing of it
#    below its foot unless it hangs from the ceiling;
#  - every kit of data/kits/*.json against data/kits/kit.schema.json; every object it names in the catalogue; as many
#    different objects as its typology asks (40 small shops, 60 restaurants and homes, 80 gyms and supermarkets); its
#    moodboard of 10 real photographs at least, with their author and licence (reference only: never in the game);
#  - and writes src/interiores_datos.js (OBJETOS, KITS) for the game.
#   python3 tools/interiores/datos.py           (exit 1 on any blocking error; the report: data/interiores/datos.json)
import glob, json, math, os, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'rotulos'))
from entidades import check  # (the JSON Schema checker the signs use)

def alto(p):
    # a part's half height and centre height in its object's frame (turned about x or z: the box round it)
    d, sc = p['d'], p.get('s', [1, 1, 1])
    f = p['f']
    hw, hh, hd = ((d[0] / 2, d[1] / 2, d[2] / 2) if f == 'caja' else (max(d[0], d[1]), d[2] / 2, max(d[0], d[1])) if f == 'cil' else
                  (d[0], d[0], d[0]) if f == 'esfera' else (d[0], d[1] / 2, d[0]) if f == 'cono' else (d[0] / 2, d[1] / 2, 0.002))
    hw, hh, hd = hw * sc[0], hh * sc[1], hd * sc[2]
    r = p.get('r') or [0, 0, 0]
    if r[0] or r[2]:
        rx, rz = math.radians(r[0]), math.radians(r[2])
        hh = abs(hh * math.cos(rx) * math.cos(rz)) + abs(hd * math.sin(rx)) + abs(hw * math.sin(rz))
    return hh, p['p'][1]

def triangulos(p):
    # (as src/objetos.js builds them: three.js' boxes, cylinders of `seg` sides, spheres 12 × 8, cones of `seg`)
    f, seg = p['f'], p.get('seg')
    return {'caja': 12, 'cil': 4 * (seg or 12), 'esfera': 2 * 12 * 8, 'cono': 2 * (seg or 14), 'plano': 2}[f]

def albedo(hexc):
    # the part's colour as linear reflectance (the mean of its channels)
    c = [int(hexc[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    lin = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return sum(lin) / 3

def main():
    errs, avisos = [], []
    schema_o = json.load(open(os.path.join(ROOT, 'data', 'interaction.schema.json')))
    schema_k = json.load(open(os.path.join(ROOT, 'data', 'kits', 'kit.schema.json')))
    MR = json.load(open(os.path.join(ROOT, 'data', 'mass_ranges.json')))
    OBJ = {}
    fams = [json.load(open(f)) for f in sorted(glob.glob(os.path.join(ROOT, 'data', 'objetos', '*.json')))]
    for fam in fams: # (a family may bring categories of its own, with their mass ranges)
        for c, rg in fam.get('categorias', {}).items():
            if c in MR['categorias'] and MR['categorias'][c] != rg: errs.append(f'categoría «{c}» con dos rangos de masa')
            MR['categorias'].setdefault(c, rg)
    for fam in fams:
        for o in fam['objetos']:
            e = check(o, schema_o, o.get('id', '?'))
            if e: errs += e; continue
            if o['id'] in OBJ: errs.append(f'{o["id"]}: repetido'); continue
            OBJ[o['id']] = o
            lo, hi = MR['categorias'].get(o['categoria'], [None, None])
            if lo is None: errs.append(f'{o["id"]}: categoría sin rango de masa «{o["categoria"]}»')
            elif not (lo <= o['masa'] <= hi) and not o.get('motivo_clase'): errs.append(f'{o["id"]}: masa {o["masa"]} kg fuera de {o["categoria"]} [{lo}, {hi}]')
            if o['masa'] <= 0: errs.append(f'{o["id"]}: masa ≤ 0')
            if o['clase'] == 'FIXED':
                if not o.get('motivo_fijo'): errs.append(f'{o["id"]}: FIXED sin motivo')
            else:
                a, b = MR['clases'][o['clase']]
                if not (a <= o['masa'] < b) and not o.get('motivo_clase'): errs.append(f'{o["id"]}: clase {o["clase"]} con {o["masa"]} kg sin motivo de sobrescritura')
            if 'SEAT' in o.get('modificadores', []) and not o.get('asientos'): errs.append(f'{o["id"]}: SEAT sin asientos')
            if not re.match(r'^[a-z0-9_]+$', o['id']): errs.append(f'{o["id"]}: el id no sigue la convención (minúsculas, cifras y _)')
            tri = sum(triangulos(p) for p in o['partes'])
            if tri > 5000: errs.append(f'{o["id"]}: {tri} triángulos (> 5.000: necesitaría niveles de detalle, I-07)')
            for p in o['partes']:
                if p.get('luz') or p.get('tex') or p['m'] in ('cristal', 'metal'): continue
                a_ = albedo(p.get('c', '#888888'))
                if a_ < 0.012 or a_ > 0.92: avisos.append(f'{o["id"]}: color {p.get("c")} fuera del albedo físico ({a_:.3f})'); break
            ext = [alto(p) for p in o['partes']]
            for k, sup in enumerate(o.get('superficies', [])):
                if not any(abs(c + h - sup['y']) <= 0.005 for h, c in ext): errs.append(f'{o["id"]}: la superficie {k} (y {sup["y"]}) no está en lo alto de ninguna pieza')
            if o['soporte'] != 'techo' and min(c - h for h, c in ext) < -0.002: errs.append(f'{o["id"]}: baja {-min(c - h for h, c in ext) * 100:.1f} cm por debajo de su pie')
    MIN = {'tienda_especializada': 40, 'tienda_ropa': 40, 'farmacia': 40, 'sucursal_bancaria': 40, 'oficina': 40, 'restaurante': 60, 'bar': 60, 'cafeteria': 60,
           'salon': 60, 'cocina': 60, 'dormitorio': 60, 'bano': 60, 'gimnasio': 80, 'alimentacion': 80,
           'otra_estancia': 30}  # (the lesser rooms of a home: pantry, box room, workshop, sewing room…)
    KITS, informe = {}, {}
    for f in sorted(glob.glob(os.path.join(ROOT, 'data', 'kits', '*.json'))):
        if f.endswith('.schema.json'): continue
        k = json.load(open(f))
        kid = os.path.basename(f)[:-5]
        e = check(k, schema_k, os.path.basename(f))
        if e: errs += e; continue
        ids = set()
        for i, it in enumerate(k['objetos']):
            for oid in ([it['obj']] if it.get('obj') else []) + it.get('variantes', []) + it.get('en', []) + it.get('sillas', {}).get('variantes', []):
                if oid not in OBJ: errs.append(f'{kid}: objeto {i} nombra «{oid}», que no está en el catálogo')
                elif not it.get('en') or oid not in it.get('en', []): ids.add(oid)
            if it['zona'] not in {z['id'] for z in k['zonas']}: errs.append(f'{kid}: objeto {i} en una zona que no existe «{it["zona"]}»')
        for it in k['objetos']:
            for oid in it.get('en', []): ids.add(oid)
        n_min = max(k['minimo_objetos_distintos'], MIN.get(k['tipologia'], 40))
        if len(ids) < n_min: errs.append(f'{kid}: {len(ids)} objetos distintos, la tipología pide {n_min}')
        mood = k['moodboard']
        if len(mood) < 10: errs.append(f'{kid}: moodboard con {len(mood)} fotografías (pide 10, con autor y licencia)')
        KITS[kid] = k
        informe[kid] = {'tipologia': k['tipologia'], 'objetos_distintos': len(ids), 'minimo': n_min, 'moodboard': len(mood), 'zonas': len(k['zonas'])}
    # (the game reads the objects the kits use, and the kits)
    js = ['// The interiors\' objects and kits (technical backlog, epic I), from data/objetos/*.json and data/kits/*.json —',
          '// written by tools/interiores/datos.py, checked against their schemas. Do not edit by hand.',
          'export const OBJETOS = ' + json.dumps(OBJ, ensure_ascii=False, separators=(',', ':')) + ';',
          'export const KITS = ' + json.dumps({t: {kk: vv for kk, vv in k.items() if kk not in ('moodboard', 'nota')} for t, k in KITS.items()}, ensure_ascii=False, separators=(',', ':')) + ';']
    open(os.path.join(ROOT, 'src', 'interiores_datos.js'), 'w').write('\n'.join(js) + '\n')
    os.makedirs(os.path.join(ROOT, 'data', 'interiores'), exist_ok=True)
    rep = {'objetos': len(OBJ), 'kits': informe, 'errores': errs, 'avisos': avisos}
    if avisos: print(f'{len(avisos)} avisos (data/interiores/datos.json)')
    json.dump(rep, open(os.path.join(ROOT, 'data', 'interiores', 'datos.json'), 'w'), ensure_ascii=False, indent=1)
    print(json.dumps({'objetos': len(OBJ), 'kits': informe, 'errores': errs[:30]}, ensure_ascii=False, indent=1))
    return not errs

if __name__ == '__main__':
    sys.exit(0 if main() else 1)
