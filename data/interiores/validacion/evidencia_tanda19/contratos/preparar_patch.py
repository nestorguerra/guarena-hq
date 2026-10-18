"""Regenera sólo el artefacto privado; no escribe fuentes activas."""
from pathlib import Path
import difflib
p=Path(__file__).parent
base=(p/'base.js').read_text()
s=base.replace('espacioFrontal, mapaPaso, rot','espacioFrontal, mapaPaso, rot, superficie')
assert s!=base
needle='  return { pruebas, errores };'
assert s.count(needle)==1
s=s.replace(needle,(p/'contrato.fragment.js').read_text()+needle)
(p/'candidata.js').write_text(s)
(p/'contratos.patch').write_text(''.join(difflib.unified_diff(base.splitlines(True),s.splitlines(True),fromfile='a/tools/interiores/casas_pruebas.js',tofile='b/tools/interiores/casas_pruebas.js')))
