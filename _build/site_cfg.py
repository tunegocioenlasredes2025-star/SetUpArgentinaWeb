# -*- coding: utf-8 -*-
"""
Configuracion central del sitio bilingue de SetUp Argentina.

Una sola fuente de verdad para dominios, rutas y equivalencias entre idiomas.
Si cambia una URL, se cambia SOLO aca: el nav, el hreflang, el selector de
idioma, el sitemap y las migas de pan se rearman solos.
"""

SITE = "https://setupargentina.com"

EMAIL = "contact@setupargentina.com.ar"
WA_NUMBER = "5491125637925"
WA_DISPLAY = "+54 11 2563-7925"
CITY = "Buenos Aires, Argentina (CABA)"

WA_TEXT = {
    "en": "Hi, I would like to ask about your services.",
    "es": "Hola, queria consultar por sus servicios.",
}

# clave -> (ruta en ingles, ruta en espanol)
# El ingles vive en la raiz (mercado prioritario), el espanol bajo /es/.
PAGES = {
    "home":       ("/",  "/es/"),
    "about":      ("/about/", "/es/nosotros/"),
    "services":   ("/services/", "/es/servicios/"),
    "formation":  ("/services/company-formation/",
                   "/es/servicios/constitucion-de-sociedades/"),
    "accounting": ("/services/accounting-tax-and-compliance/",
                   "/es/servicios/contabilidad-impuestos-y-cumplimiento/"),
    "advisory":   ("/services/business-and-legal-advisory/",
                   "/es/servicios/asesoramiento-empresarial-y-legal/"),
    "represent":  ("/services/legal-representation-and-registered-office/",
                   "/es/servicios/representacion-legal-y-domicilio-fiscal/"),
    "faq":        ("/faq/", "/es/preguntas-frecuentes/"),
    "contact":    ("/contact/", "/es/contacto/"),
    "partners":   ("/partners/", "/es/partners/"),
    "blog":       ("/blog/", "/es/blog/"),
}

SERVICE_KEYS = ["formation", "accounting", "advisory", "represent"]

# El blog se construye pero todavia no se enlaza en el menu ni entra al
# sitemap: arranca sin notas y un /blog vacio juega en contra.
BLOG_PUBLIC = False

LANG_INDEX = {"en": 0, "es": 1}


def url(key, lang):
    """Ruta interna de una pagina en un idioma."""
    return PAGES[key][LANG_INDEX[lang]]


def abs_url(key, lang):
    return SITE + url(key, lang)


def other(lang):
    return "es" if lang == "en" else "en"


def out_path(key, lang):
    """Ruta del archivo a escribir, relativa a la raiz del repo."""
    u = url(key, lang).strip("/")
    return "index.html" if not u else u + "/index.html"


def depth_prefix(key, lang):
    """Prefijo relativo para llegar a la raiz desde una pagina (styles.css, etc)."""
    u = url(key, lang).strip("/")
    return "./" if not u else "../" * (u.count("/") + 1)
