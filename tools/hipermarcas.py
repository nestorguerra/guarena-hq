# The reference photo's landmarks drawn over the game's picture taken from the same camera (tools/hipershots.js,
# 'noroeste'), so the church can be judged against the photo without a pixel of it: where each crosshair falls is where
# that feature is in the photo.
#   python3 tools/hipermarcas.py .snaps/hq_noroeste_<tag>.jpg .snaps/hq_noroeste_<tag>_marcas.jpg
# The photo: Wikimedia Commons, «Iglesia Parroquial de Santa María (Guareña, España).jpg», by El tiu Cancho, CC BY-SA
# 4.0. The positions were picked by eye on its 1920 × 1280 version (2026-10-11), each checked on the photo enlarged
# (a wrong one misled both the camera's fit and the reviewer once): only these numbers come from it.
import sys
from PIL import Image, ImageDraw

MARKS = [  # (what, u, v) on the 1920 × 1280 photo
    ('esquina NO (cornisa)', 1194, 169), ('esquina NO (suelo)', 1304, 1200),
    ('muro N, extremo O', 940, 228), ('muro N, extremo E', 272, 676), ('retranqueo', 1000, 260),
    ('remate 1', 716, 360), ('remate 2', 556, 472), ('remate 3', 434, 552),
    ('óculo grande', 1485, 792), ('óculo pequeño', 1435, 430), ('portada (umbral)', 1541, 1205), ('portada (frontón)', 1541, 920),
    ('fachada O, extremo S', 1680, 800), ('torre: cruz', 1393, 12),
    ('campanario NE', 1313, 237), ('campanario NO', 1467, 168), ('campanario SO', 1543, 233), ('cuerpo alto NE', 1365, 133), ('cuerpo alto NO', 1432, 109),
    ('ventanal 1', 804, 450), ('ventanal 1 alféizar', 804, 586), ('ventanal 2', 598, 578), ('ventanal 2 alféizar', 598, 696),
    ('ventanal 3', 458, 655), ('ventanal 3 alféizar', 458, 770), ('ventanal 4', 342, 721), ('ventanal 4 alféizar', 342, 820),
    ('torreón: frontón', 1208, 72), ('torreón: pináculo NO', 1168, 51), ('gárgola 1', 845, 385), ('gárgola 2', 725, 455),
]

# the photo's lens: 18 mm on APS-C (EXIF) → f = 1545 px on the 1920 × 1280 copy, with a slight barrel (k1 −0,03), which
# the game's pinhole camera has not: the marks are undistorted to where a perfect lens would have put them
F, K1 = 640 / 0.41421356, -0.03
def undistort(u, v):
    xd, yd = (u - 960) / F, (v - 640) / F
    x, y = xd, yd
    for _ in range(8):
        s = 1 + K1 * (x * x + y * y); x, y = xd / s, yd / s
    return 960 + x * F, 640 + y * F

if __name__ == '__main__':
    src, out = sys.argv[1], sys.argv[2]
    im = Image.open(src).convert('RGB')
    k = im.width / 1920
    d = ImageDraw.Draw(im)
    for name, u, v in MARKS:
        u, v = undistort(u, v)
        x, y = u * k, v * k
        d.line([x - 9, y, x + 9, y], fill=(255, 0, 200), width=2)
        d.line([x, y - 9, x, y + 9], fill=(255, 0, 200), width=2)
        d.text((x + 6, y + 4), name, fill=(255, 0, 200))
    im.save(out, quality=90)
