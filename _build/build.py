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

CSS_START = "/* ===== BILINGUE:START (generado, no editar a mano) ===== */"
CSS_END = "/* ===== BILINGUE:END ===== */"


def ensure_css():
    """Reescribe el bloque de estilos nuevos dentro de styles.css.

    Va delimitado para poder regenerarlo cuantas veces haga falta sin
    duplicar reglas ni pisar el CSS original de la landing.
    """
    styles = os.path.join(ROOT, "styles.css")
    with open(styles, "r", encoding="utf-8") as fh:
        current = fh.read()

    if CSS_START in current and CSS_END in current:
        head = current[:current.index(CSS_START)]
        tail = current[current.index(CSS_END) + len(CSS_END):]
        current = head.rstrip() + "\n" + tail.lstrip()

    with open(os.path.join(HERE, "extra.css"), "r", encoding="utf-8") as fh:
        extra = fh.read()

    with open(styles, "w", encoding="utf-8") as fh:
        fh.write(current.rstrip() + "\n\n" + CSS_START + "\n" + extra
                 + "\n" + CSS_END + "\n")
    return True


def write_page(key, lang, html):
    dest = os.path.join(ROOT, out_path(key, lang))
    os.makedirs(os.path.dirname(dest) or ROOT, exist_ok=True)
    with open(dest, "w", encoding="utf-8") as fh:
        fh.write(html)
    return out_path(key, lang)


def write_raw(path, html):
    """Escribe una pagina en una ruta arbitraria (notas del blog)."""
    dest = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(dest) or ROOT, exist_ok=True)
    with open(dest, "w", encoding="utf-8") as fh:
        fh.write(html)
    return path


def main():
    import pages_about
    import pages_blog
    import pages_home
    import pages_faq
    import pages_partners
    import pages_contact
    import pages_services

    if ensure_css():
        print("styles.css  <- estilos nuevos agregados")
    else:
        print("styles.css  ya tenia los estilos nuevos")

    written = []
    for module in (pages_home, pages_about, pages_services, pages_faq,
                   pages_blog,
                   pages_partners, pages_contact):
        for key, lang, html in module.build():
            written.append(write_page(key, lang, html))

    # Las notas del blog no estan en el mapa fijo de paginas: cada una
    # trae su propia ruta en los dos idiomas.
    for path, html in pages_blog.build_articles():
        written.append(write_raw(path, html))

    print("\n%d paginas generadas:" % len(written))
    for w in sorted(written):
        print("  ", w)


if __name__ == "__main__":
    main()
