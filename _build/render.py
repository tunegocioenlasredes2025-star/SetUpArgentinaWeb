# -*- coding: utf-8 -*-
"""Ensamblado de una pagina completa. Vive aparte de build.py para que los
modulos de contenido puedan importarlo sin ciclos."""

import chrome


def page(key, lang, *, title, description, body, schema=None, crumbs=None,
         paths=None, robots="index, follow"):
    html = chrome.head(lang=lang, key=key, title=title, description=description,
                       schema=schema, paths=paths, robots=robots)
    swap = paths[1 if lang == "en" else 0] if paths else None
    html += chrome.nav(lang, key, swap_to=swap)
    if crumbs:
        html += chrome.breadcrumb(lang, crumbs)
    html += '\n<main id="main">\n' + body + '\n</main>\n'
    html += chrome.footer(lang)
    return html
