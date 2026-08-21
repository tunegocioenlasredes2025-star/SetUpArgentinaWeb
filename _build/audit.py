# -*- coding: utf-8 -*-
"""Auditoria del sitio generado.

    python _build/audit.py

Revisa lo que no se ve mirando la pagina: que cada canonical apunte a si
misma, que los hreflang sean RECIPROCOS (si la inglesa dice "mi version
en espanol es esta", la espanola tiene que decir lo mismo al reves; si no,
Google ignora el par entero), que no haya titulos ni descripciones
repetidas, y que los links internos no apunten a paginas que no existen.
"""

import os
import re
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from site_cfg import SITE  # noqa: E402

SALTAR = {".git", "_build", "admin", "images", "icons", "assets", "node_modules"}

errores = []
avisos = []


def paginas():
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SALTAR]
        for f in files:
            if f.endswith(".html"):
                yield os.path.join(base, f)


def ruta_web(archivo):
    rel = os.path.relpath(archivo, ROOT).replace("\\", "/")
    if rel.endswith("index.html"):
        rel = rel[:-len("index.html")]
    return "/" + rel.lstrip("/")


def etiqueta(html, patron):
    m = re.search(patron, html, re.I | re.S)
    return m.group(1).strip() if m else None


def main():
    datos = {}

    for archivo in paginas():
        with open(archivo, "r", encoding="utf-8") as fh:
            html = fh.read()

        url = ruta_web(archivo)
        canonical = etiqueta(html, r'<link rel="canonical" href="([^"]+)"')
        titulo = etiqueta(html, r"<title>(.*?)</title>")
        desc = etiqueta(html, r'<meta name="description" content="([^"]*)"')
        robots = etiqueta(html, r'<meta name="robots" content="([^"]*)"') or ""
        alts = dict(re.findall(
            r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)"', html))
        lang = etiqueta(html, r'<html lang="([^"]+)"')

        datos[url] = {"canonical": canonical, "titulo": titulo, "desc": desc,
                      "alts": alts, "robots": robots, "lang": lang,
                      "html": html, "archivo": archivo}

    print("Paginas analizadas: %d\n" % len(datos))

    # ── 1. Canonical ──────────────────────────────────────
    for url, d in datos.items():
        if not d["canonical"]:
            errores.append("%s: sin canonical" % url)
        elif d["canonical"] != SITE + url:
            errores.append("%s: canonical apunta a %s (deberia ser %s)"
                           % (url, d["canonical"], SITE + url))

    # ── 2. hreflang reciproco ─────────────────────────────
    # Si A declara a B como su version en otro idioma, B tiene que
    # declarar a A. Un par que no cierra, Google lo descarta entero.
    for url, d in datos.items():
        if "noindex" in d["robots"]:
            continue
        alts = d["alts"]
        if not alts:
            errores.append("%s: sin etiquetas hreflang" % url)
            continue
        if "x-default" not in alts:
            avisos.append("%s: sin x-default" % url)
        for code in ("en", "es"):
            if code not in alts:
                errores.append("%s: le falta el hreflang '%s'" % (url, code))
                continue
            destino = alts[code].replace(SITE, "")
            otro = datos.get(destino)
            if otro is None:
                errores.append("%s: su hreflang '%s' apunta a %s, que no existe"
                               % (url, code, destino))
                continue
            vuelta = otro["alts"].get(d["lang"][:2] if d["lang"] else "")
            if vuelta and vuelta.replace(SITE, "") != url:
                errores.append("%s: el hreflang no es reciproco con %s" % (url, destino))

    # ── 3. Titulos y descripciones ────────────────────────
    por_titulo = defaultdict(list)
    por_desc = defaultdict(list)
    for url, d in datos.items():
        if "noindex" in d["robots"]:
            continue
        if not d["titulo"]:
            errores.append("%s: sin title" % url)
        else:
            por_titulo[d["titulo"]].append(url)
            if len(d["titulo"]) > 65:
                avisos.append("%s: title de %d caracteres (Google corta cerca de 60)"
                              % (url, len(d["titulo"])))
        if not d["desc"]:
            errores.append("%s: sin meta description" % url)
        else:
            por_desc[d["desc"]].append(url)
            if len(d["desc"]) > 165:
                avisos.append("%s: description de %d caracteres (se corta cerca de 160)"
                              % (url, len(d["desc"])))

    for titulo, urls in por_titulo.items():
        if len(urls) > 1:
            errores.append("title repetido en %s: %r" % (", ".join(urls), titulo[:50]))
    for desc, urls in por_desc.items():
        if len(urls) > 1:
            errores.append("description repetida en %s" % ", ".join(urls))

    # ── 4. Links internos rotos ───────────────────────────
    existentes = set(datos.keys())
    for url, d in datos.items():
        for href in set(re.findall(r'href="(/[^"#?]*)"', d["html"])):
            if href.startswith(("/images/", "/admin/", "/icons/", "/assets/")):
                continue
            if href.endswith((".css", ".js", ".xml", ".txt", ".ico", ".png",
                              ".jpg", ".webp", ".svg")):
                continue
            if not href.endswith("/"):
                href += "/"
            if href not in existentes:
                errores.append("%s: link interno roto -> %s" % (url, href))

    # ── 5. Un solo H1 por pagina ──────────────────────────
    for url, d in datos.items():
        n = len(re.findall(r"<h1[\s>]", d["html"], re.I))
        if n == 0:
            errores.append("%s: sin H1" % url)
        elif n > 1:
            avisos.append("%s: tiene %d H1 (deberia haber uno solo)" % (url, n))

    # ── Resultado ─────────────────────────────────────────
    if avisos:
        print("AVISOS (%d):" % len(avisos))
        for a in sorted(set(avisos)):
            print("  -", a)
        print()
    if errores:
        print("ERRORES (%d):" % len(errores))
        for e in sorted(set(errores)):
            print("  -", e)
        return 1
    print("Sin errores. Canonicals, hreflang reciprocos, titulos unicos, "
          "links internos y H1: todo en orden.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
