# -*- coding: utf-8 -*-
"""Preguntas frecuentes, en acordeon nativo y con FAQPage structured data.

Las preguntas bien respondidas pueden aparecer solas como resultado en
Google, asi que cada una va tambien en el JSON-LD.
"""

import render
from chrome import cta_band
from site_cfg import SITE, url

COPY = {
    "en": {
        "title": "Company Formation FAQ: Timelines, Capital and Taxes | SetUp",
        "desc": ("How long incorporation takes, whether you need to travel, which "
                 "structure to choose, capital and taxes. The questions we get most."),
        "crumbs": [("Home", "/"), ("FAQ", None)],
        "tag": "FAQ",
        "h1": "Frequently Asked Questions",
        "lead": ("The questions we get asked most often about setting up and running "
                 "a company in Argentina. If yours is not here, just ask."),
        "cta_text": "Still have questions? The first consultation is free.",
        "cta_btn": "Book a Free Consultation",
        "qa": [
            ("How long does it take to incorporate a company in Argentina?",
             "Between 10 and 30 business days from submission of complete documentation, "
             "depending on the entity type and processing times. If a foreign company is "
             "a shareholder, its prior Article 123 registration adds several weeks."),
            ("Do I need to travel to Argentina?",
             "No. The whole process can be handled remotely with notarized, apostilled "
             "documentation. You grant us a power of attorney and we take care of "
             "everything on your behalf."),
            ("SRL, SAS or SA, which one should I choose?",
             "SRL: 2 to 50 partners, the most solid structure. SAS: single shareholder "
             "possible, the fastest to set up. SA: for larger projects or issuing shares. "
             "We recommend the best fit in a free consultation."),
            ("Can a foreigner own 100% of a company in Argentina?",
             "Yes. Argentina places no restrictions on foreign ownership in most sectors, "
             "with the same rights as a local shareholder and no limits on repatriating "
             "profits."),
            ("Can a foreign company be a partner?",
             "Yes. It must first register its documentation with the companies registry "
             "under Section 123 of the General Companies Law, which we handle together "
             "with the incorporation."),
            ("Do I need a physical office in Argentina?",
             "No. We provide a registered fiscal domicile in Buenos Aires (CABA) that "
             "satisfies the legal requirement."),
            ("How much does it cost?",
             "It depends on the service, the structure and the complexity of your case. "
             "We give you a clear, all-in quote before we start, with no surprises."),
            ("How much capital do I need to start?",
             "The SRL has no fixed minimum, the SAS requires the equivalent of two minimum "
             "wages (currently around USD 500) and the SA a higher minimum (currently "
             "around USD 20,000)."),
            ("What taxes will my company pay?",
             "Income Tax (35%), VAT (21%), Turnover Tax (variable by jurisdiction) and "
             "employer contributions if you have staff."),
            ("Do you only do company formation, or also ongoing support?",
             "Both, and the ongoing part is our strength. Beyond incorporation we handle "
             "accounting and tax compliance and act as your ongoing business and legal "
             "advisor, all under one roof."),
            ("Do you handle other matters, like trademarks or visas?",
             "Yes. On request we also register trademarks and assist with residence and "
             "work visas for company directors, among other legal and tax matters."),
        ],
    },
    "es": {
        "title": "Constituir en Argentina: dudas frecuentes | SetUp",
        "desc": ("Cuánto tarda constituir, si hace falta viajar, qué estructura conviene, "
                 "capital mínimo e impuestos. Las preguntas que más nos hacen."),
        "crumbs": [("Inicio", "/es/"), ("Preguntas frecuentes", None)],
        "tag": "Preguntas frecuentes",
        "h1": "Preguntas frecuentes",
        "lead": ("Las preguntas que más nos hacen sobre constituir y operar una empresa "
                 "en Argentina. Si la tuya no está, escribinos."),
        "cta_text": "¿Te quedó alguna duda? La primera consulta es sin cargo.",
        "cta_btn": "Agendá una consulta sin cargo",
        "qa": [
            ("¿Cuánto tarda constituir una empresa en Argentina?",
             "Entre 10 y 30 días hábiles desde la documentación completa, según el tipo de "
             "sociedad y los tiempos de trámite. Si un socio es una sociedad del exterior, "
             "su inscripción previa por el Art. 123 suma algunas semanas."),
            ("¿Necesito viajar a Argentina?",
             "No. Todo el proceso se maneja de forma remota con documentación apostillada. "
             "Nos das un poder y hacemos todo por vos."),
            ("¿SRL, SAS o SA, cuál me conviene?",
             "SRL: de 2 a 50 socios, la estructura más sólida. SAS: admite un solo "
             "accionista, la más rápida de constituir. SA: para proyectos más grandes o "
             "emitir acciones. En una consulta te recomendamos la mejor."),
            ("¿Puede un extranjero ser dueño del 100%?",
             "Sí. Argentina no tiene restricciones a la propiedad extranjera en la mayoría "
             "de los sectores, con los mismos derechos que un socio local y sin límites "
             "para repatriar utilidades."),
            ("¿Puede una sociedad extranjera ser socia?",
             "Sí. Primero debe inscribir su documentación ante la IGJ bajo el Art. 123 de "
             "la Ley General de Sociedades, algo que hacemos junto con la constitución."),
            ("¿Necesito una oficina física?",
             "No. Proveemos un domicilio fiscal en CABA que cumple con el requisito legal."),
            ("¿Cuánto cuesta?",
             "Depende del servicio y la complejidad de tu caso. Te pasamos un presupuesto "
             "claro antes de empezar, sin sorpresas."),
            ("¿Cuánto capital necesito para empezar?",
             "La SRL no tiene mínimo fijo, la SAS requiere el equivalente a dos salarios "
             "mínimos (hoy unos USD 500) y la SA un mínimo mayor (hoy cerca de USD 20.000)."),
            ("¿Qué impuestos paga mi empresa?",
             "Ganancias (35%), IVA (21%), Ingresos Brutos (variable por jurisdicción) y "
             "cargas patronales si tenés empleados."),
            ("¿Ofrecen solo constitución o también acompañamiento?",
             "Las dos cosas, y el acompañamiento es nuestro fuerte. Además de constituir, "
             "llevamos la contabilidad y somos tu asesor empresarial y legal continuo, "
             "todo en un mismo lugar."),
            ("¿Se ocupan de otros temas, como marcas o visas?",
             "Sí. A pedido también registramos marcas y asistimos con residencias y visas "
             "de trabajo para directores, entre otros temas."),
        ],
    },
}


def build():
    for lang in ("en", "es"):
        c = COPY[lang]
        items = "\n".join(
            '''      <details class="faq-acc">
        <summary>{q}</summary>
        <div class="faq-acc-body"><p>{a}</p></div>
      </details>'''.format(q=q, a=a) for q, a in c["qa"])

        body = f'''
<header class="page-hero">
  <div class="container">
    <span class="section-tag" data-animate="fadeInUp">{c["tag"]}</span>
    <h1 data-animate="fadeInUp">{c["h1"]}</h1>
    <p class="page-lead" data-animate="fadeInUp">{c["lead"]}</p>
  </div>
</header>

<section class="faq-section">
  <div class="container">
    <div class="faq-list" data-animate="fadeInUp">
{items}
    </div>
  </div>
</section>
'''
        schema = {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "url": SITE + url("faq", lang),
            "inLanguage": "en" if lang == "en" else "es-AR",
            "mainEntity": [
                {"@type": "Question", "name": q,
                 "acceptedAnswer": {"@type": "Answer", "text": a}}
                for q, a in c["qa"]
            ],
        }
        yield "faq", lang, render.page(
            "faq", lang, title=c["title"], description=c["desc"],
            body=body + cta_band(lang, c["cta_text"], c["cta_btn"]),
            schema=schema, crumbs=c["crumbs"])
