# -*- coding: utf-8 -*-
"""Head, navegacion, footer y piezas compartidas por todas las paginas."""

import json
from urllib.parse import quote

from site_cfg import (SITE, EMAIL, WA_NUMBER, WA_DISPLAY, CITY, WA_TEXT,
                      BLOG_PUBLIC, url, abs_url, other)

FONTS = ("https://fonts.googleapis.com/css2?family=Playfair+Display:"
         "ital,wght@0,400;0,500;0,600;0,700;1,400&family=Inter:"
         "wght@300;400;500;600;700&display=swap")

CHECK_SVG = ('<svg width="14" height="14" viewBox="0 0 24 24" fill="none">'
             '<path d="M9 12L11 14L15 10M21 12C21 16.9706 16.9706 21 12 21C7.02944 '
             '21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z" '
             'stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>')

ARROW_SVG = ('<svg width="16" height="16" viewBox="0 0 24 24" fill="none" aria-hidden="true">'
             '<path d="M5 12H19M12 5L19 12L12 19" stroke="currentColor" '
             'stroke-width="2" stroke-linecap="round"/></svg>')

WA_SVG = ('<svg viewBox="0 0 24 24" fill="currentColor" width="26" height="26" aria-hidden="true">'
          '<path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15'
          '-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39'
          '-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298'
          '-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669'
          '-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52'
          '.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149'
          '.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118'
          '.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198'
          '-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998'
          '-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 '
          '0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 '
          '9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096'
          '.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 '
          '0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>')

ACTIVE = ' class="active"'

T = {
    "en": {
        "nav": [("services", "Services"), ("about", "About"),
                ("faq", "FAQ"), ("contact", "Contact")],
        "nav_blog": "Blog",
        "cta": "Book a Free Consultation",
        "cta_short": "Book Consultation",
        "switch": "ES",
        "switch_label": "Ver en español",
        "menu": "Menu",
        "home_crumb": "Home",
        "wa_aria": "Chat on WhatsApp",
        "hint_text": "This page is also available in Spanish.",
        "hint_go": "View in Spanish",
        "f_tagline": ("Your trusted partner for legal, tax and corporate services in "
                      "Buenos Aires, helping foreign companies and local entrepreneurs "
                      "establish and operate in Argentina, efficiently and in full compliance."),
        "f_services": "Services",
        "f_company": "Company",
        "f_contact": "Contact",
        "f_rights": "All rights reserved.",
        "f_by": "Website by",
        "skip": "Skip to content",
    },
    "es": {
        "nav": [("services", "Servicios"), ("about", "Nosotros"),
                ("faq", "Preguntas frecuentes"), ("contact", "Contacto")],
        "nav_blog": "Blog",
        "cta": "Agendá una consulta sin cargo",
        "cta_short": "Consulta sin cargo",
        "switch": "EN",
        "switch_label": "View in English",
        "menu": "Menú",
        "home_crumb": "Inicio",
        "wa_aria": "Escribinos por WhatsApp",
        "hint_text": "Esta página también está en inglés.",
        "hint_go": "Ver en inglés",
        "f_tagline": ("Tu socio de confianza para lo legal, lo impositivo y lo societario "
                      "en Buenos Aires. Acompañamos a empresas del exterior y a "
                      "emprendedores locales a constituir y operar en Argentina, "
                      "de forma eficiente y en regla."),
        "f_services": "Servicios",
        "f_company": "Estudio",
        "f_contact": "Contacto",
        "f_rights": "Todos los derechos reservados.",
        "f_by": "Sitio desarrollado por",
        "skip": "Ir al contenido",
    },
}

SERVICE_NAMES = {
    "en": {
        "formation": "Company Formation",
        "accounting": "Accounting, Tax &amp; Compliance",
        "advisory": "Business &amp; Legal Advisory",
        "represent": "Legal Representation &amp; Registered Office",
        "trademark": "Trademark Registration",
    },
    "es": {
        "formation": "Constitución de sociedades",
        "accounting": "Contabilidad, impuestos y cumplimiento",
        "advisory": "Asesoramiento empresarial y legal",
        "represent": "Representación legal y domicilio fiscal",
        "trademark": "Registro de marcas",
    },
}

SERVICE_ORDER = ["formation", "accounting", "advisory", "represent", "trademark"]


def head(*, lang, key, title, description, schema=None, robots="index, follow",
         paths=None):
    """Head completo, con hreflang reciproco y x-default apuntando al ingles.

    paths: (ruta_en, ruta_es) explicitas, para paginas que no estan en el
    mapa fijo (por ejemplo cada nota del blog).
    """
    def _abs(code):
        if paths:
            return SITE + paths[0 if code == "en" else 1]
        return abs_url(key, code)

    canonical = _abs(lang)
    alt_lines = []
    for code in ("en", "es"):
        alt_lines.append('  <link rel="alternate" hreflang="%s" href="%s">'
                         % (code, _abs(code)))
    alt_lines.append('  <link rel="alternate" hreflang="x-default" href="%s">'
                     % _abs("en"))
    alts = "\n".join(alt_lines)

    blocks = ""
    if schema:
        for s in (schema if isinstance(schema, list) else [schema]):
            blocks += ('\n  <script type="application/ld+json">'
                       + json.dumps(s, ensure_ascii=False, separators=(",", ":"))
                       + "</script>")

    html_lang = "en" if lang == "en" else "es-AR"
    og_locale = "en_US" if lang == "en" else "es_AR"

    return f'''<!DOCTYPE html>
<html lang="{html_lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="robots" content="{robots}">
  <link rel="canonical" href="{canonical}">
{alts}
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="SetUp Argentina">
  <meta property="og:locale" content="{og_locale}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:image" content="{SITE}/images/og-{lang}.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="{SITE}/images/og-{lang}.jpg">
  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <meta name="theme-color" content="#060C1C">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="{FONTS}" rel="stylesheet">
  <link rel="stylesheet" href="/styles.css">{blocks}
</head>
<body>
<a href="#main" class="skip-link">{T[lang]["skip"]}</a>
'''


def nav(lang, key, swap_to=None):
    t = T[lang]
    items = list(t["nav"])
    if BLOG_PUBLIC:
        items.insert(3, ("blog", t["nav_blog"]))
    lis = "\n".join(
        '        <li><a href="%s"%s>%s</a></li>'
        % (url(k, lang), ACTIVE if k == key else "", label)
        for k, label in items)
    swap = swap_to or url(key, other(lang))
    return f'''
<nav id="navbar">
  <div class="nav-container">
    <a href="{url("home", lang)}" class="nav-logo" aria-label="SetUp Argentina">
      <span class="logo-mark">Set<em>UP</em></span><span class="logo-country">Argentina</span></a>
    <ul class="nav-links" id="navLinks">
{lis}
    </ul>
    <div class="nav-actions">
      <a href="{swap}" class="lang-switch" hreflang="{other(lang)}"
         aria-label="{t["switch_label"]}">{t["switch"]}</a>
      <a href="{url("contact", lang)}" class="btn-nav-cta">{t["cta_short"]}</a>
      <button class="nav-toggle" id="navToggle" aria-label="{t["menu"]}" aria-expanded="false">
        <span></span><span></span><span></span></button>
    </div>
  </div>
</nav>
<div class="lang-hint" id="langHint" data-target="{swap}" hidden>
  <span>{t["hint_text"]}</span>
  <a href="{swap}" class="lang-hint-go">{t["hint_go"]}</a>
  <button class="lang-hint-close" aria-label="Close">&times;</button>
</div>
'''


def breadcrumb(lang, trail):
    """trail: lista de (texto, href o None). El ultimo elemento va sin href."""
    lis, items = [], []
    for i, (name, href) in enumerate(trail, start=1):
        if href:
            lis.append('<li><a href="%s">%s</a></li>' % (href, name))
            items.append({"@type": "ListItem", "position": i, "name": name,
                          "item": SITE + href})
        else:
            lis.append('<li><span aria-current="page">%s</span></li>' % name)
            items.append({"@type": "ListItem", "position": i, "name": name})
    ld = json.dumps({"@context": "https://schema.org", "@type": "BreadcrumbList",
                     "itemListElement": items},
                    ensure_ascii=False, separators=(",", ":"))
    return ('<nav class="breadcrumb" aria-label="breadcrumb"><div class="container"><ol>'
            + "".join(lis)
            + '</ol></div></nav>\n<script type="application/ld+json">' + ld + '</script>')


def wa_float(lang):
    href = "https://wa.me/%s?text=%s" % (WA_NUMBER, quote(WA_TEXT[lang]))
    return ('<a class="wa-float" target="_blank" rel="noopener" aria-label="%s" href="%s">%s</a>'
            % (T[lang]["wa_aria"], href, WA_SVG))


def cta_band(lang, text, button):
    return f'''
<section class="cta-band">
  <div class="container">
    <p data-animate="fadeInUp">{text}</p>
    <a href="{url("contact", lang)}" class="btn-primary btn-large" data-animate="fadeInUp">
      <span>{button}</span>{ARROW_SVG}</a>
  </div>
</section>
'''


def footer(lang, year=2026):
    t = T[lang]
    svc = "\n".join(
        '          <li><a href="%s">%s</a></li>' % (url(k, lang), SERVICE_NAMES[lang][k])
        for k in SERVICE_ORDER)
    company = [("about", "About us" if lang == "en" else "Nosotros"),
               ("partners", "Partners"),
               ("faq", "FAQ" if lang == "en" else "Preguntas frecuentes"),
               ("contact", "Contact" if lang == "en" else "Contacto")]
    if BLOG_PUBLIC:
        company.insert(2, ("blog", "Blog"))
    comp = "\n".join(
        '          <li><a href="%s">%s</a></li>' % (url(k, lang), label)
        for k, label in company)
    return f'''
<footer id="footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="{url("home", lang)}" class="nav-logo footer-logo">
          <span class="logo-mark">Set<em>UP</em></span><span class="logo-country">Argentina</span></a>
        <p class="footer-tagline">{t["f_tagline"]}</p>
      </div>
      <div class="footer-col">
        <h4>{t["f_services"]}</h4>
        <ul>
{svc}
        </ul>
      </div>
      <div class="footer-col">
        <h4>{t["f_company"]}</h4>
        <ul>
{comp}
        </ul>
      </div>
      <div class="footer-col footer-contact-col">
        <h4>{t["f_contact"]}</h4>
        <ul>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="https://wa.me/{WA_NUMBER}" target="_blank" rel="noopener">{WA_DISPLAY}</a></li>
          <li><span>{CITY}</span></li>
        </ul>
        <a href="{url("contact", lang)}" class="btn-primary btn-footer-cta">
          <span>{t["cta"]}</span>{ARROW_SVG}</a>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; {year} SetUp Argentina. {t["f_rights"]}</p>
      <p>{t["f_by"]} <a href="https://www.tunegocioenlasredes.com.ar" target="_blank"
         rel="noopener">Tu Negocio En Las Redes</a></p>
    </div>
  </div>
</footer>
{wa_float(lang)}
<script src="/script.js"></script>
</body>
</html>
'''
