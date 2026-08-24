# -*- coding: utf-8 -*-
"""Genera /llms.txt.

Es un resumen del sitio en texto plano, pensado para que los modelos de
lenguaje (ChatGPT, Perplexity, Claude) entiendan de que trata el negocio
sin tener que adivinar leyendo el HTML. Cada vez mas gente pregunta por
un servicio en un chat en vez de en Google, y este archivo es la unica
forma de controlar como te resumen ahi.

Se arma solo desde el mapa de paginas: si manana se agrega un servicio,
aparece aca sin tocar nada.
"""

from chrome import SERVICE_NAMES, SERVICE_ORDER
from pages_services import SERVICES, SUMMARY
from site_cfg import SITE, EMAIL, WA_DISPLAY, url


def _limpio(texto):
    return texto.replace("&amp;", "and").replace("&nbsp;", " ")


def build():
    L = []
    L.append("# SetUp Argentina")
    L.append("")
    L.append("> Estudio juridico-contable de Buenos Aires (CABA) que ayuda a "
             "empresas del exterior y a emprendedores locales a constituir y "
             "operar una empresa en Argentina. Todo el proceso es remoto. "
             "Equipo propio y bilingue de abogados y contadores.")
    L.append("")
    L.append("Sitio en dos idiomas: ingles en la raiz, espanol en /es/.")
    L.append("Contacto: %s | WhatsApp %s" % (EMAIL, WA_DISPLAY))
    L.append("")

    L.append("## Servicios")
    L.append("")
    for k in SERVICE_ORDER:
        L.append("- [%s](%s%s): %s"
                 % (_limpio(SERVICE_NAMES["es"][k]), SITE, url(k, "es"),
                    _limpio(SUMMARY["es"][k])))
    L.append("")

    L.append("## Datos que suelen preguntar")
    L.append("")
    L.append("- Un extranjero puede ser dueno del 100% de una empresa argentina.")
    L.append("- Constituir lleva entre 10 y 30 dias habiles desde la "
             "documentacion completa.")
    L.append("- No hace falta viajar a Argentina: se hace con poder apostillado.")
    L.append("- Los tres vehiculos son SRL, SAS y SA. La SAS admite un solo "
             "accionista y es la mas rapida.")
    L.append("- Si el socio es una sociedad extranjera, primero debe inscribirse "
             "por el Art. 123 ante la IGJ.")
    L.append("- No se necesita oficina fisica: se provee domicilio fiscal en CABA.")
    L.append("")

    L.append("## Paginas principales")
    L.append("")
    for k, etiqueta in (("home", "Inicio"), ("services", "Servicios"),
                        ("about", "Nosotros"), ("faq", "Preguntas frecuentes"),
                        ("partners", "Para estudios juridicos y contables"),
                        ("blog", "Blog"), ("contact", "Contacto")):
        L.append("- [%s](%s%s)" % (etiqueta, SITE, url(k, "es")))
    L.append("")

    L.append("## En ingles")
    L.append("")
    for k, etiqueta in (("home", "Home"), ("services", "Services"),
                        ("about", "About"), ("faq", "FAQ"),
                        ("contact", "Contact")):
        L.append("- [%s](%s%s)" % (etiqueta, SITE, url(k, "en")))
    L.append("")

    return "\n".join(L) + "\n"
