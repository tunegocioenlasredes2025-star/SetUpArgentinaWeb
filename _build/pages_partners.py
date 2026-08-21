# -*- coding: utf-8 -*-
"""Pagina de partners: dirigida a estudios juridicos y contables del exterior
que necesitan ejecucion local en Argentina.

El documento del cliente todavia no trae logos ni fichas de partners, asi
que la pagina se arma como invitacion a asociarse, con el mismo texto que
el cliente escribio. Cuando lleguen los logos se suma la grilla.
"""

import render
from chrome import ARROW_SVG, CHECK_SVG, cta_band, SERVICE_NAMES, SERVICE_ORDER
from pages_services import SUMMARY
from site_cfg import SITE, url

COPY = {
    "en": {
        "title": "Partner With Us | Local Execution in Argentina",
        "desc": ("If your clients are expanding into Argentina, partner with a reliable "
                 "local team. We handle the local execution, you keep the client."),
        "crumbs": [("Home", "/"), ("Partners", None)],
        "tag": "Partners",
        "h1": "Are you a law or accounting firm?",
        "lead": ("If your clients are expanding into Argentina, partner with a reliable "
                 "local team. We handle the local execution, company formation, tax, "
                 "compliance and legal advisory, while you keep the relationship with "
                 "your client."),
        "h_we": "What we handle",
        "h_you": "What stays with you",
        "you": [
            "The relationship with your client, start to finish",
            "Your fee arrangement and your billing",
            "The strategic advice on your side of the border",
            "A single, named local contact instead of a switchboard",
        ],
        "h_why": "Why firms work with us",
        "why": [
            ("In-house, bilingual team",
             "Licensed lawyers and accountants under one roof (CPACF), not a referral "
             "middleman passing your client along."),
            ("Cross-border experience",
             "Specialists in foreign companies entering Argentina, with prior experience "
             "at Accenture and Biz Latin Hub."),
            ("Fully remote",
             "Your client incorporates and operates in Argentina without travelling or "
             "renting an office."),
            ("One point of contact",
             "Formation, tax ID, legal representation, accounting, payroll and "
             "compliance, all through the same person."),
        ],
        "cta_text": ("If your clients are expanding into Argentina, let's talk about "
                     "working together."),
        "cta_btn": "Partner with us",
    },
    "es": {
        "title": "Trabajemos juntos | Ejecución local en Argentina para estudios",
        "desc": ("Si tus clientes se expanden a Argentina, sumate a un equipo local "
                 "confiable. Nos ocupamos de la ejecución local, vos del cliente."),
        "crumbs": [("Inicio", "/es/"), ("Partners", None)],
        "tag": "Partners",
        "h1": "¿Sos un estudio jurídico o contable?",
        "lead": ("Si tus clientes se expanden a Argentina, sumate a un equipo local "
                 "confiable. Nos ocupamos de la ejecución local, constitución, impuestos, "
                 "cumplimiento y asesoramiento, mientras vos mantenés la relación con "
                 "tu cliente."),
        "h_we": "De qué nos ocupamos",
        "h_you": "Qué queda de tu lado",
        "you": [
            "La relación con tu cliente, de punta a punta",
            "Tus honorarios y tu facturación",
            "El asesoramiento estratégico de tu lado de la frontera",
            "Un contacto local con nombre y apellido, no una mesa de entradas",
        ],
        "h_why": "Por qué los estudios trabajan con nosotros",
        "why": [
            ("Equipo propio y bilingüe",
             "Abogados y contadores matriculados (CPACF) en un mismo lugar, no un "
             "intermediario que deriva a tu cliente."),
            ("Experiencia cross-border",
             "Especialistas en empresas extranjeras que entran a Argentina, con "
             "experiencia previa en Accenture y Biz Latin Hub."),
            ("100% online",
             "Tu cliente constituye y opera en Argentina sin viajar ni alquilar "
             "una oficina."),
            ("Un solo punto de contacto",
             "Constitución, CUIT, representación legal, contabilidad, sueldos y "
             "cumplimiento, todo por la misma persona."),
        ],
        "cta_text": ("Si tus clientes se expanden a Argentina, hablemos de trabajar "
                     "juntos."),
        "cta_btn": "Trabajemos juntos",
    },
}


def build():
    for lang in ("en", "es"):
        c = COPY[lang]
        we = "\n".join(
            '        <li>%s<div><strong>%s</strong><span>%s</span></div></li>'
            % (CHECK_SVG, SERVICE_NAMES[lang][k], SUMMARY[lang][k])
            for k in SERVICE_ORDER)
        you = "\n".join(
            '        <li>%s<div><strong>%s</strong></div></li>' % (CHECK_SVG, item)
            for item in c["you"])
        why = "\n".join(
            '''        <div class="pw-card"><h3>%s</h3><p>%s</p></div>'''
            % (title, text) for title, text in c["why"])

        body = f'''
<header class="page-hero">
  <div class="container">
    <span class="section-tag" data-animate="fadeInUp">{c["tag"]}</span>
    <h1 data-animate="fadeInUp">{c["h1"]}</h1>
    <p class="page-lead" data-animate="fadeInUp">{c["lead"]}</p>
  </div>
</header>

<section class="partners-split">
  <div class="container split-layout">
    <div data-animate="fadeInLeft">
      <h2 class="split-title">{c["h_we"]}</h2>
      <ul class="split-list">
{we}
      </ul>
    </div>
    <div data-animate="fadeInRight">
      <h2 class="split-title">{c["h_you"]}</h2>
      <ul class="split-list">
{you}
      </ul>
    </div>
  </div>
</section>

<section class="why-section">
  <div class="container">
    <h2 class="related-title" data-animate="fadeInUp">{c["h_why"]}</h2>
    <div class="pw-grid" data-animate="fadeInUp">
{why}
    </div>
    <a href="{url("contact", lang)}" class="btn-primary svc-cta" data-animate="fadeInUp">
      <span>{c["cta_btn"]}</span>{ARROW_SVG}</a>
  </div>
</section>
'''
        schema = {
            "@context": "https://schema.org",
            "@type": "WebPage",
            "url": SITE + url("partners", lang),
            "name": c["h1"],
            "description": c["desc"],
            "inLanguage": "en" if lang == "en" else "es-AR",
            "about": {"@type": "ProfessionalService", "name": "SetUp Argentina",
                      "url": SITE},
        }
        yield "partners", lang, render.page(
            "partners", lang, title=c["title"], description=c["desc"],
            body=body + cta_band(lang, c["cta_text"], c["cta_btn"]),
            schema=schema, crumbs=c["crumbs"])
