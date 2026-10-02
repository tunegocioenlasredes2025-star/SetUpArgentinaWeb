# -*- coding: utf-8 -*-
"""Trae las notas publicadas desde Supabase, en tiempo de build.

Esta es la pieza que hace que el blog posicione. El navegador NO le pide
las notas a la base: las pide este script cuando se genera el sitio, y
cada nota queda como una pagina HTML de verdad. Google la ve completa
apenas entra, sin tener que ejecutar JavaScript.

Si la base no responde, el build SE CAE a proposito. Antes seguia de
largo y generaba el sitio sin notas, que parece lo prudente pero es la
peor opcion: si Supabase esta pausado y alguien pushea cualquier cambio,
el blog se publica vacio, las notas ya indexadas empiezan a dar 404 y
nadie se entera hasta que Google las da de baja.

Al fallar el build, Vercel deja online el ultimo deploy que si funciono
y el sitio queda intacto, con todas sus notas. El error se ve en el
panel de Vercel y llega por mail. Es ruidoso a proposito.

Para una emergencia (hay que publicar un cambio urgente con la base
caida) se saltea con la variable de entorno BLOG_OPCIONAL=1, sabiendo
que ese deploy sale sin blog.

Ojo: "la base contesta y no hay ninguna nota" NO es un error. Eso es el
estado normal mientras el cliente todavia no publico nada.
"""

import json
import os
import re
import urllib.error
import urllib.request

SUPABASE_URL = "https://tvxhhbonqzabnwwpayet.supabase.co"
SUPABASE_KEY = "sb_publishable_M-qp7enm2WJrT2l1e1bL3g_N57jtYAH"

TIMEOUT = 12


class BlogNoDisponible(RuntimeError):
    """Supabase no contesto. Mejor no publicar que publicar el blog vacio."""


def _sin_base(error):
    """Corta el build, salvo que se pida explicitamente seguir sin blog."""
    if os.environ.get("BLOG_OPCIONAL") == "1":
        print("  aviso: Supabase no responde (%s)." % error)
        print("         BLOG_OPCIONAL=1: el sitio se genera SIN el blog.")
        return []
    raise BlogNoDisponible(
        "no se pudo leer el blog desde Supabase (%s).\n"
        "        El build se corta a proposito: si siguiera, el sitio se\n"
        "        publicaria con el blog vacio y las notas ya indexadas\n"
        "        empezarian a dar 404.\n"
        "        Vercel deja online el ultimo deploy que funciono, asi que\n"
        "        el sitio sigue intacto mientras tanto.\n"
        "        Revisa si el proyecto de Supabase esta pausado por\n"
        "        inactividad y despertalo desde el panel.\n"
        "        Para publicar igual, sin blog: BLOG_OPCIONAL=1" % error)


def _reading_minutes(html):
    texto = re.sub(r"<[^>]+>", " ", html or "")
    palabras = len([p for p in texto.split() if p])
    return max(1, round(palabras / 200))


def _normalizar(fila):
    """Pasa una fila de la base al formato que usan las plantillas."""
    salida = {
        "slug_en": fila.get("slug_en"),
        "slug_es": fila.get("slug_es"),
        "date": (fila.get("published_at") or "")[:10],
        "cover": fila.get("cover_url"),
    }
    for lang in ("en", "es"):
        titulo = fila.get("title_" + lang)
        if not titulo or not fila.get("slug_" + lang):
            salida[lang] = None          # la nota no existe en este idioma
            continue
        html = fila.get("body_" + lang) or ""
        extracto = fila.get("excerpt_" + lang) or ""
        salida[lang] = {
            "title": titulo,
            "excerpt": extracto,
            "html": html,
            "read": _reading_minutes(html),
            "cover_alt": fila.get("cover_alt_" + lang) or "",
            # Meta title y meta description propios, para cuando el titulo
            # que se ve en la pagina no es el que conviene en Google. Si la
            # base todavia no tiene estas columnas, el .get() devuelve None
            # y la nota sigue usando el titulo y el extracto de siempre.
            "meta_title": fila.get("meta_title_" + lang) or "",
            "meta_desc": fila.get("meta_desc_" + lang) or extracto,
        }
    return salida


def fetch_posts():
    """Notas publicadas y con fecha ya cumplida, de la mas nueva a la mas vieja.

    Devuelve [] si todavia no hay nada publicado. Si la base NO responde
    levanta BlogNoDisponible, salvo que BLOG_OPCIONAL=1.
    """
    url = (SUPABASE_URL + "/rest/v1/posts"
           "?select=*&status=eq.published&published_at=lte.now()"
           "&order=published_at.desc")
    req = urllib.request.Request(url, headers={
        "apikey": SUPABASE_KEY,
        "Authorization": "Bearer " + SUPABASE_KEY,
    })
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            filas = json.loads(resp.read().decode("utf-8"))
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError,
            OSError, ValueError) as e:
        return _sin_base(e)

    notas = [_normalizar(f) for f in filas]
    # Una nota sin ningun idioma completo no se publica.
    return [n for n in notas if n["en"] or n["es"]]
