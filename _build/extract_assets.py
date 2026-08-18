# -*- coding: utf-8 -*-
"""Snapshotea del index.html original las piezas visuales que no conviene
retipear (el skyline del hero y los iconos de las tarjetas).

Se corre UNA vez: la home generada sobrescribe index.html, asi que despues
de eso el original ya no esta disponible. El resultado queda versionado en
legacy_assets.py.

    python _build/extract_assets.py
"""

import io
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

src = io.open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()

# ── Bloque visual del hero (skyline + tarjetas flotantes) ────────────
i = src.index('<div class="hero-visual"')
j = src.index('</div>\n  </div>\n  <div class="hero-scroll-indicator"')
hero_visual = src[i:j + len("</div>")]

# ── Iconos, en el orden en que aparecen ──────────────────────────────
def icons(css_class):
    pat = re.compile(r'<div class="%s">(<svg.*?</svg>)</div>' % css_class, re.S)
    return pat.findall(src)

why_icons = icons("why-icon")
service_icons = icons("service-icon")
chip_icons = re.findall(
    r'<div class="industry-chip"[^>]*>(<svg.*?</svg>)', src, re.S)

out = io.StringIO()
out.write("# -*- coding: utf-8 -*-\n")
out.write('"""GENERADO por extract_assets.py — piezas visuales rescatadas de la\n')
out.write('landing original para que el sitio nuevo se vea exactamente igual.\n')
out.write('No editar a mano."""\n\n')
out.write("HERO_VISUAL = %r\n\n" % hero_visual)
out.write("WHY_ICONS = %r\n\n" % why_icons)
out.write("SERVICE_ICONS = %r\n\n" % service_icons)
out.write("CHIP_ICONS = %r\n" % chip_icons)

io.open(os.path.join(HERE, "legacy_assets.py"), "w", encoding="utf-8").write(
    out.getvalue())

print("hero_visual: %d caracteres" % len(hero_visual))
print("why icons: %d | service icons: %d | chips: %d"
      % (len(why_icons), len(service_icons), len(chip_icons)))
