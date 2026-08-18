# -*- coding: utf-8 -*-
"""
Generador del sitio bilingue de SetUp Argentina.

    python _build/build.py

Escribe las paginas en la raiz del repo. El ingles va en la raiz y el
espanol bajo /es/. Todo lo compartido sale de chrome.py y las URLs de
site_cfg.py, asi que ninguna ruta se escribe dos veces.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from site_cfg import out_path     # noqa: E402

CSS_MARKER = "SITIO BILINGÜE — componentes nuevos"


def ensure_css():
    """Agrega los estilos nuevos a styles.css una sola vez."""
    styles = os.path.join(ROOT, "styles.css")
    with open(styles, "r", encoding="utf-8") as fh:
        current = fh.read()
    if CSS_MARKER in current:
        return False
    with open(os.path.join(HERE, "extra.css"), "r", encoding="utf-8") as fh:
        extra = fh.read()
    with open(styles, "a", encoding="utf-8") as fh:
        fh.write(extra)
    return True


def write_page(key, lang, html):
    dest = os.path.join(ROOT, out_path(key, lang))
    os.makedirs(os.path.dirname(dest) or ROOT, exist_ok=True)
    with open(dest, "w", encoding="utf-8") as fh:
        fh.write(html)
    return out_path(key, lang)


def main():
    import pages_contact

    if ensure_css():
        print("styles.css  <- estilos nuevos agregados")
    else:
        print("styles.css  ya tenia los estilos nuevos")

    written = []
    for module in (pages_contact,):
        for key, lang, html in module.build():
            written.append(write_page(key, lang, html))

    print("\n%d paginas generadas:" % len(written))
    for w in sorted(written):
        print("  ", w)


if __name__ == "__main__":
    main()
