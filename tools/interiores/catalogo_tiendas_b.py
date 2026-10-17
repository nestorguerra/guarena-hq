# The objects of the «tiendas_b» family (technical backlog, I-02 and X-01/X-02): small-town shops — a furniture showroom,
# household appliances, computers and phones, a bakery, a greengrocer, a perfumery, a hairdresser and a car workshop —
# each object a few primitives (boxes, cylinders, spheres, cones and textured planes, in metres), its class of
# interaction, mass, material and support. The script is the model: it writes data/objetos/tiendas_b.json. The shared
# pieces are in tb_base.py, the objects of each shop in tb_<tienda>.py. Their pictures: src/texturas/tiendas_b.js.
# Frame of an object: x across, y up from its foot, z out of its front (+z faces whoever uses it; its back at -z).
# Products are FACINGS: a row of identical units at the front of a shelf and a solid block behind (the stock).
# No real brand anywhere: invented names, plain colours.
#   python3 tools/interiores/catalogo_tiendas_b.py
import importlib, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tb_base
for m in ('tb_muebles', 'tb_electro', 'tb_informatica', 'tb_panaderia', 'tb_fruteria', 'tb_perfumeria', 'tb_peluqueria', 'tb_taller'):
    if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), m + '.py')): importlib.import_module(m)
tb_base.guardar()
