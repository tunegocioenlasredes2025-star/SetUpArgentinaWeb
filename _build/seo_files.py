# -*- coding: utf-8 -*-
"""Sitemap y robots.

El sitemap declara las dos versiones de cada pagina con sus alternates.
Es la forma que recomienda Google para sitios internacionales: ademas de
las etiquetas en el HTML, el sitemap le dice explicitamente que /contact/
y /es/contacto/ son la misma pagina en dos idiomas.

Las notas de ejemplo no entran: van con noindex, y meter en el sitemap
algo que le pedis a Google que no indexe es mandarle una senal contradictoria.
"""

import pages_blog
from site_cfg import PAGES, SITE, BLOG_PUBLIC

# Cuanta prioridad relativa tiene cada pagina dentro del sitio.
PRIORIDAD = {
    "home": "1.0",
    "services": "0.9",
    "formation": "0.9", "accounting": "0.9", "advisory": "0.9", "represent": "0.9",
    "contact": "0.8",
    "about": "0.7",
    "partners": "0.7",
    "faq": "0.7",
    "blog": "0.6",
}


def _url_block(loc, alternates, prioridad=None, lastmod=None):
    lineas = ["  <url>", "    <loc>%s</loc>" % loc]
    for code, href in alternates:
        lineas.append('    <xhtml:link rel="alternate" hreflang="%s" href="%s"/>'
                      % (code, href))
    if lastmod:
        lineas.append("    <lastmod>%s</lastmod>" % lastmod)
    if prioridad:
        lineas.append("    <priority>%s</priority>" % prioridad)
    lineas.append("  </url>")
    return "\n".join(lineas)


def build_sitemap():
    bloques = []

    for key, (ruta_en, ruta_es) in PAGES.items():
        if key == "blog" and not BLOG_PUBLIC:
            continue
        abs_en, abs_es = SITE + ruta_en, SITE + ruta_es
        alt = [("en", abs_en), ("es", abs_es), ("x-default", abs_en)]
        for loc in (abs_en, abs_es):
            bloques.append(_url_block(loc, alt, PRIORIDAD.get(key, "0.5")))

    # Notas del blog: solo las reales, nunca las de ejemplo.
    if BLOG_PUBLIC and not pages_blog.DEMO:
        for post in pages_blog.POSTS:
            en_path, es_path = pages_blog._post_paths(post)
            alt = []
            if en_path:
                alt.append(("en", SITE + en_path))
            if es_path:
                alt.append(("es", SITE + es_path))
            # x-default a la version que exista; si estan las dos, al ingles.
            alt.append(("x-default", SITE + (en_path or es_path)))
            for ruta in (en_path, es_path):
                if ruta:
                    bloques.append(_url_block(SITE + ruta, alt, "0.6", post["date"]))

    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
            '        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
            + "\n".join(bloques)
            + "\n</urlset>\n")


ROBOTS = """User-agent: *
Allow: /

# El panel de carga no tiene por que estar en Google.
Disallow: /admin/

Sitemap: %s/sitemap.xml
""" % SITE


def build_files():
    """(ruta, contenido) de los archivos sueltos de SEO."""
    import llms_file
    return [("sitemap.xml", build_sitemap()),
            ("robots.txt", ROBOTS),
            ("llms.txt", llms_file.build())]
