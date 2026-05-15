"""Generate cropped previews from the 15 PDF pages."""
from PIL import Image
from pathlib import Path

ASSETS = Path(__file__).parent

def save_crop(src, box, dst, *, max_w=900):
    img = Image.open(ASSETS / src)
    crop = img.crop(box)
    if crop.width > max_w:
        ratio = max_w / crop.width
        crop = crop.resize((max_w, int(crop.height * ratio)), Image.LANCZOS)
    crop.save(ASSETS / dst, "PNG", optimize=True)
    print(f"{dst}: {crop.size}")

# Page 1 is 1654x2339 at 200dpi
# Hero illustration: bottom-right of cover
save_crop("page-01.png", (820, 1200, 1654, 2200), "hero-walter.png", max_w=700)

# Page 3 — Prototipos 1, 2, 3 (each card)
# Card layout: ~3 cards stacked vertically. Approx:
# card 1: y 200-650; card 2: y 720-1170; card 3: y 1240-1690
save_crop("page-03.png", (90, 200, 1580, 700), "proto-01-makinfo.png")
save_crop("page-03.png", (90, 760, 1580, 1260), "proto-02-siscomtur.png")
save_crop("page-03.png", (90, 1320, 1580, 1820), "proto-03-sirid.png")

# Page 4 — Prototipos 4, 5, 6
save_crop("page-04.png", (90, 200, 1580, 700), "proto-04-mesapartes-web.png")
save_crop("page-04.png", (90, 760, 1580, 1260), "proto-05-mesapartes-mov.png")
save_crop("page-04.png", (90, 1320, 1580, 1820), "proto-06-gscconvocatorias.png")

# Page 5 — Prototipos 7, 8, 9
save_crop("page-05.png", (90, 200, 1580, 700), "proto-07-combustible.png")
save_crop("page-05.png", (90, 760, 1580, 1260), "proto-08-visitasm.png")
save_crop("page-05.png", (90, 1320, 1580, 1820), "proto-09-presupuesto.png")

# Page 6 — Prototipo 10 (full page)
save_crop("page-06.png", (90, 200, 1580, 2100), "proto-10-gstramite.png", max_w=1100)

# Page 7 — Case study Siscomtur (full)
save_crop("page-07.png", (60, 100, 1600, 2250), "casestudy-full.png", max_w=1200)

# Page 8 — Diagramas de flujo (each)
save_crop("page-08.png", (90, 200, 1580, 1100), "diagrama-01-bim.png")
save_crop("page-08.png", (90, 1130, 1580, 2050), "diagrama-02-tupa.png")

# Page 9-11 — Dashboards
save_crop("page-09.png", (90, 200, 1580, 1100), "dash-01-bim.png")
save_crop("page-09.png", (90, 1130, 1580, 2050), "dash-02-financiero.png")
save_crop("page-10.png", (90, 200, 1580, 1100), "dash-03-mobiliario.png")
save_crop("page-10.png", (90, 1130, 1580, 2050), "dash-04-nacimientos.png")
save_crop("page-11.png", (90, 200, 1580, 1100), "dash-05-trafico.png")
save_crop("page-11.png", (90, 1130, 1580, 2050), "dash-06-mortalidad.png")

# Page 12 — Imagenes / Iconos / Logos
save_crop("page-12.png", (90, 200, 1580, 1100), "imagenes.png")
save_crop("page-12.png", (90, 1130, 850, 2150), "iconos.png")
save_crop("page-12.png", (850, 1130, 1580, 2150), "logos.png")

# Page 13 — Manuales
save_crop("page-13.png", (90, 200, 1580, 2200), "manuales.png", max_w=1100)

# Page 14 — Videos
save_crop("page-14.png", (90, 200, 1580, 1100), "video-01.png")
save_crop("page-14.png", (90, 1130, 1580, 2050), "video-02.png")

print("DONE")
