# -*- coding: utf-8 -*-
"""Pagina About / Nosotros. El activo comercial mas fuerte del estudio es
la persona, asi que la pagina esta armada alrededor de las credenciales."""

import render
from chrome import ARROW_SVG, CHECK_SVG, cta_band
from site_cfg import SITE, url

COPY = {
    "en": {
        "title": "About SetUp Argentina | Agustín Sofía, Founder and Lead Advisor",
        "desc": ("Corporate lawyer with over 10 years of experience, admitted to the "
                 "Buenos Aires City Bar Association, with postgraduate studies at UCA, "
                 "Universidad Austral and UCEMA, and experience at Accenture and Biz Latin Hub."),
        "crumbs": [("Home", "/"), ("About", None)],
        "tag": "Your Advisor",
        "h1": "Meet Agustín Sofía",
        "lead": ("One firm for the whole journey, legal and accounting under one roof, "
                 "in your language."),
        "quote": "We speak your language and understand your business.",
        "quote_by": "Agustín Sofía, Founder, SetUp Argentina",
        "role": "Founder and Lead Advisor, SetUp Argentina",
        "bio": ("Corporate lawyer with 10+ years of experience, admitted to the Buenos "
                "Aires City Bar Association (CPACF, Vol. 141, Fol. 71), with postgraduate "
                "studies at UCA, Universidad Austral and UCEMA, and experience at Accenture "
                "and Biz Latin Hub. He founded SetUp Argentina to give international and "
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
        "photo_alt": "Agustín Sofía, founder of SetUp Argentina",
        "cta_text": ("Book a free initial consultation and get a personalized roadmap "
                     "for doing business in Argentina."),
        "cta_btn": "Book a Free Consultation",
    },
    "es": {
        "title": "Nosotros | Agustín Sofía, fundador de SetUp Argentina",
        "desc": ("Abogado corporativo con más de 10 años de experiencia, matriculado en el "
                 "Colegio Público de Abogados de la Capital Federal, con posgrados en UCA, "
                 "Universidad Austral y UCEMA, y experiencia en Accenture y Biz Latin Hub."),
        "crumbs": [("Inicio", "/es/"), ("Nosotros", None)],
        "tag": "Tu asesor",
        "h1": "Agustín Sofía",
        "lead": ("Un solo estudio para todo el camino, lo legal y lo contable en un "
                 "mismo lugar."),
        "quote": "Hablamos tu idioma y entendemos tu negocio.",
        "quote_by": "Agustín Sofía, fundador de SetUp Argentina",
        "role": "Fundador y asesor principal, SetUp Argentina",
        "bio": ("Abogado corporativo con más de 10 años de experiencia, matriculado en el "
                "Colegio Público de Abogados de la Capital Federal (CPACF, Tomo 141, "
                "Folio 71), con posgrados en UCA, Universidad Austral y UCEMA, y experiencia "
                "en Accenture y Biz Latin Hub. Fundó SetUp Argentina para dar a clientes "
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
        "photo_alt": "Agustín Sofía, fundador de SetUp Argentina",
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
                "name": "Agustín Sofía",
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
