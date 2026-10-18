#!/bin/sh
# catalogue + kits + data for the game (the three steps the family's work needs after every change); datos.py's report is
# filtered to this family's objects and kits (another family's errors are not ours)
cd "$(dirname "$0")/../.." || exit 1
python3 tools/interiores/catalogo_tiendas_b.py && python3 tools/interiores/kits_tiendas_b.py "$@" || exit 1
python3 tools/interiores/datos.py > /dev/null
python3 -c "
import json, re
d = json.load(open('data/interiores/datos.json'))
mio = re.compile(r'^(tal|pel|per|fru|pan|mue|ele|inf)_|^(muebles|electro|informatica|panaderia|fruteria|perfumeria|peluqueria|taller)[:\s]')
print('avisos', [a for a in d['avisos'] if mio.match(a)][:20], 'errores', [e for e in d['errores'] if mio.match(e)][:20], '(de otros:', len([e for e in d['errores'] if not mio.match(e)]), ')')"
