# -*- coding: utf-8 -*-
"""Trae las notas publicadas desde Supabase, en tiempo de build.

Esta es la pieza que hace que el blog posicione. El navegador NO le pide
las notas a la base: las pide este script cuando se genera el sitio, y
cada nota queda como una pagina HTML de verdad. Google la ve completa
apenas entra, sin tener que ejecutar JavaScript.

Si la base no responde, el build no se cae: sigue con lo que haya y
avisa por consola. Preferimos publicar el sitio sin una nota nueva antes
que no publicar nada.
"""

import json
import re
import urllib.error
import urllib.request

SUPABASE_URL = "https://tvxhhbonqzabnwwpayet.supabase.co"
SUPABASE_KEY = "sb_publishable_M-qp7enm2WJrT2l1e1bL3g_N57jtYAH"

TIMEOUT = 12


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
        salida[lang] = {
            "title": titulo,
            "excerpt": fila.get("excerpt_" + lang) or "",
            "html": html,
            "read": _reading_minutes(html),
            "cover_alt": fila.get("cover_alt_" + lang) or "",
        }
    return salida


def fetch_posts():
    """Notas publicadas y con fecha ya cumplida, de la mas nueva a la mas vieja.

    Devuelve [] si la base no responde o todavia no hay nada publicado.
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
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError) as e:
        print("  aviso: no se pudo leer el blog desde Supabase (%s)." % e)
        print("         el sitio se genera igual, sin las notas nuevas.")
        return []
    except ValueError as e:
        print("  aviso: Supabase devolvio algo que no es JSON (%s)." % e)
        return []

    notas = [_normalizar(f) for f in filas]
    # Una nota sin ningun idioma completo no se publica.
    return [n for n in notas if n["en"] or n["es"]]
