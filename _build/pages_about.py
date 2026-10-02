# -*- coding: utf-8 -*-
"""Pagina About / Nosotros. El activo comercial mas fuerte del estudio es
la persona, asi que la pagina esta armada alrededor de las credenciales."""

import render
from chrome import ARROW_SVG, CHECK_SVG, cta_band
from site_cfg import SITE, url

COPY = {
    "en": {
        "title": "About SetUp Argentina | Leandro Agustín Sofía Liuzzi",
        "desc": ("Attorney admitted to the Buenos Aires Bar (CPACF) in 2021, with 10+ "
                 "years in the legal field and experience at Accenture and Biz Latin Hub."),
        "crumbs": [("Home", "/"), ("About", None)],
        "tag": "Your Advisor",
        "h1": "Meet Leandro Agustín Sofía Liuzzi",
        "lead": ("One firm for the whole journey, legal and accounting under one roof, "
                 "in your language."),
        "quote": ("Argentina's rules are hard to read from the outside. Our job "
                  "is to make sense of them, manage them and keep your company in "
                  "good standing, so that your only concern is growing your "
                  "business."),
        "quote_by": "Leandro Agustín Sofía Liuzzi, Founder, SetUp Argentina",
        "role": "Founder and Lead Advisor, SetUp Argentina",
        "bio": ("Attorney admitted to the Buenos Aires Bar (CPACF) in 2021, with over "
                "ten years in the legal field, first in the public sector and then in "
                "corporate services for international companies. Bar registration: CPACF "
                "Vol. 141, Fol. 71. Postgraduate studies at UCA, Universidad Austral and "
                "UCEMA, and experience at Accenture and Biz Latin Hub. He founded SetUp Argentina to give international and "
                "local clients a single, reliable partner for legal and accounting from "
                "day one. Bilingual in Spanish and English."),
        "cred_h": "Credentials",
        "creds": [
            ("Buenos Aires Bar Association",
             "Fully registered Attorney at Law (Colegio Público de Abogados de la "
             "Capital Federal)."),
            ("Postgraduate in Corporate Legal Advisory",
             "Pontificia Universidad Católica Argentina (UCA)."),
            ("Diploma in Capital Markets", "Universidad Austral."),
            ("Government and multinational experience",
             "Prior roles at the Buenos Aires City Government, Accenture and Biz Latin Hub."),
            ("Bilingual, Spanish and English",
             "Direct communication with clients, no intermediaries, no translation delays."),
        ],
        "photo_alt": "Leandro Agustín Sofía Liuzzi, founder of SetUp Argentina",
        "cta_text": ("Book a free initial consultation and get a personalized roadmap "
                     "for doing business in Argentina."),
        "cta_btn": "Book a Free Consultation",
    },
    "es": {
        "title": "Nosotros | Leandro Agustín Sofía Liuzzi | SetUp Argentina",
        "desc": ("Abogado matriculado en el CPACF desde 2021, con más de diez años en "
                 "el área legal y experiencia en Accenture y Biz Latin Hub."),
        "crumbs": [("Inicio", "/es/"), ("Nosotros", None)],
        "tag": "Tu asesor",
        "h1": "Leandro Agustín Sofía Liuzzi",
        "lead": ("Un solo estudio para todo el camino, lo legal y lo contable en un "
                 "mismo lugar."),
        "quote": ("Argentina tiene reglas difíciles de leer desde afuera. Nuestro "
                  "trabajo es digerirlas, manejarlas y mantener tu empresa en regla, "
                  "para que tu única preocupación sea hacer crecer tu negocio."),
        "quote_by": "Leandro Agustín Sofía Liuzzi, fundador de SetUp Argentina",
        "role": "Fundador y asesor principal, SetUp Argentina",
        "bio": ("Abogado matriculado en el Colegio Público de la Abogacía de la Capital "
                "Federal desde 2021, con más de diez años en el área legal, primero en el "
                "sector público y después en servicios corporativos para empresas "
                "internacionales. Matrícula: CPACF Tomo 141, Folio 71. Posgrados en UCA, "
                "Universidad Austral y UCEMA, y experiencia en Accenture y Biz Latin Hub. "
                "Fundó SetUp Argentina para dar a clientes "
                "locales e internacionales un único socio confiable para lo legal y lo "
                "contable desde el primer día. Bilingüe español-inglés."),
        "cred_h": "Credenciales",
        "creds": [
            ("Colegio Público de Abogados de la Capital Federal", "Abogado matriculado."),
            ("Posgrado en Asesoramiento Jurídico de Empresas", "UCA."),
            ("Diploma en Mercado de Capitales", "Universidad Austral."),
            ("Experiencia en gobierno y multinacionales",
             "Gobierno de la Ciudad, Accenture y Biz Latin Hub."),
            ("Bilingüe español-inglés",
             "Comunicación directa, sin intermediarios ni demoras de traducción."),
        ],
        "photo_alt": "Leandro Agustín Sofía Liuzzi, fundador de SetUp Argentina",
        "cta_text": ("Agendá una consulta inicial sin cargo y llevate una hoja de ruta "
                     "personalizada para tu empresa en Argentina."),
        "cta_btn": "Agendá una consulta sin cargo",
    },
}


def build():
    for lang in ("en", "es"):
        c = COPY[lang]
        creds = "\n".join(
            '        <li class="cred-item">%s<div><strong>%s</strong><span>%s</span></div></li>'
            % (CHECK_SVG, title, detail) for title, detail in c["creds"])

        body = f'''
<header class="page-hero">
  <div class="container">
    <span class="section-tag" data-animate="fadeInUp">{c["tag"]}</span>
    <h1 data-animate="fadeInUp">{c["h1"]}</h1>
    <p class="page-lead" data-animate="fadeInUp">{c["lead"]}</p>
  </div>
</header>

<section class="founder-section">
  <div class="container founder-layout">
    <div class="founder-photo" data-animate="fadeInLeft">
      <img src="/images/agustin-sofia.jpg" alt="{c["photo_alt"]}" width="520" height="640"
           loading="lazy" decoding="async">
    </div>
    <div class="founder-body" data-animate="fadeInRight">
      <blockquote class="founder-quote">
        <p>&ldquo;{c["quote"]}&rdquo;</p>
        <cite>{c["quote_by"]}</cite>
      </blockquote>
      <p class="founder-role">{c["role"]}</p>
      <p class="founder-bio">{c["bio"]}</p>
      <h2 class="cred-title">{c["cred_h"]}</h2>
      <ul class="cred-list">
{creds}
      </ul>
      <a href="{url("contact", lang)}" class="btn-primary">
        <span>{c["cta_btn"]}</span>{ARROW_SVG}</a>
    </div>
  </div>
</section>
'''
        schema = {
            "@context": "https://schema.org",
            "@type": "AboutPage",
            "url": SITE + url("about", lang),
            "inLanguage": "en" if lang == "en" else "es-AR",
            "mainEntity": {
                "@type": "Person",
                "name": "Leandro Agustín Sofía Liuzzi",
                "jobTitle": c["role"],
                "description": c["bio"],
                "image": SITE + "/images/agustin-sofia.jpg",
                "knowsLanguage": ["es", "en"],
                "alumniOf": [
                    {"@type": "Organization",
                     "name": "Pontificia Universidad Católica Argentina"},
                    {"@type": "Organization", "name": "Universidad Austral"},
                    {"@type": "Organization", "name": "UCEMA"},
                ],
                "worksFor": {"@type": "Organization", "name": "SetUp Argentina",
                             "url": SITE},
            },
        }
        yield "about", lang, render.page(
            "about", lang, title=c["title"], description=c["desc"],
            body=body + cta_band(lang, c["cta_text"], c["cta_btn"]),
            schema=schema, crumbs=c["crumbs"])
