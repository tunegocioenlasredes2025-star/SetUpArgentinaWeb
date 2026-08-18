# -*- coding: utf-8 -*-
"""Ensamblado de una pagina completa. Vive aparte de build.py para que los
modulos de contenido puedan importarlo sin ciclos."""

import chrome


def page(key, lang, *, title, description, body, schema=None, crumbs=None):
    html = chrome.head(lang=lang, key=key, title=title,
                       description=description, schema=schema)
    html += chrome.nav(lang, key)
    if crumbs:
        html += chrome.breadcrumb(lang, crumbs)
    html += '\n<main id="main">\n' + body + '\n</main>\n'
    html += chrome.footer(lang)
    return html
