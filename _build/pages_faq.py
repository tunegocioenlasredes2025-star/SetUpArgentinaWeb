# -*- coding: utf-8 -*-
"""Preguntas frecuentes, en acordeon nativo y con FAQPage structured data.

Las preguntas bien respondidas pueden aparecer solas como resultado en
Google, asi que cada una va tambien en el JSON-LD. El JSON-LD lleva el
texto plano: los links internos de la respuesta se usan en la pagina,
pero en el dato estructurado van sin marcado.

Contenido revisado por el cliente en octubre de 2026 y actualizado a las
reformas de IGJ de ese ano. Las respuestas estan agrupadas por tema; el
agrupamiento es visual, el acordeon y el schema siguen siendo planos.
"""

import re
from urllib.parse import quote

import render
from chrome import ARROW_SVG
from pages_blog import POSTS
from site_cfg import SITE, WA_NUMBER, WA_TEXT, url

# Slug de la nota del blog a la que apuntan varias respuestas. Vive aca y
# no en site_cfg porque es una nota concreta, no una pagina fija del sitio.
NOTA_SLUG = {
    "en": "how-to-set-up-a-company-in-argentina",
    "es": "como-constituir-una-sociedad-en-argentina",
}
# Anclas dentro de la nota, por idioma.
ANCLA = {
    "en": {"checklist": "#checklist", "costos": "#costs", "cambios": "#what-changed"},
    "es": {"checklist": "#checklist", "costos": "#costos", "cambios": "#que-cambio"},
}


def _nota_publicada(lang):
    """Ruta de la nota, o None si todavia no esta publicada.

    El FAQ se publica igual aunque la nota no este cargada en la base: en
    ese caso la respuesta sale sin el link, en vez de mandar a la gente (y
    a Google) a una URL que todavia da 404. Cuando la nota entra, el sitio
    se reconstruye solo y los links aparecen.
    """
    slug = NOTA_SLUG[lang]
    for p in POSTS:
        if p.get("slug_" + lang) == slug and p.get(lang):
            return ("/blog/%s/" if lang == "en" else "/es/blog/%s/") % slug
    return None


def _link(href, label):
    return ' <a class="faq-link" href="%s">%s</a>' % (href, label)


def _nota(lang, label, ancla=None):
    base = _nota_publicada(lang)
    if not base:
        return ""
    return _link(base + (ANCLA[lang][ancla] if ancla else ""), label)


def _pagina(lang, key, label):
    return _link(url(key, lang), label)


def _qa(lang):
    """[(grupo, [(pregunta, respuesta_html), ...]), ...]"""
    if lang == "en":
        return [
            ("The process", [
                ("How long does it take to set up a company in Argentina?",
                 "An S.R.L. or S.A.S. with individual shareholders, around two weeks "
                 "from the moment the documentation from abroad is complete, apostilled "
                 "and translated. If a shareholder is a foreign company, its Article 123 "
                 "registration has been filed together with the incorporation since May "
                 "2026, and the timeline becomes two to four weeks. What takes longest "
                 "is not the registry, it is the paperwork produced in your own country."
                 + _nota(lang, "Read the 2026 guide")),

                ("Do I need to travel to Argentina?",
                 "No. The whole process is handled remotely through a power of attorney "
                 "granted in your country and apostilled there. You sign once, we do "
                 "the rest."),

                ("Which documents do I need?",
                 "If the shareholders are individuals, a certified passport and a power "
                 "of attorney, apostilled and translated. If the shareholder is a "
                 "company, add the bylaws, the certificate of incorporation, a good "
                 "standing certificate, the resolution approving the investment and the "
                 "power of attorney. We review the drafts before you apostille "
                 "anything, because a badly drafted power of attorney is the most "
                 "common cause of delay."
                 + _nota(lang, "See the document checklist", "checklist")),

                ("Can I use a translation done in my own country?",
                 "No. The translation has to be done by a sworn translator registered "
                 "in Argentina and is then legalized by the translators' association. "
                 "One detail that saves weeks: ask which language the apostille stamp "
                 "will be issued in, because if it comes in a third language you will "
                 "need two translations."),

                ("Are digitally apostilled documents accepted?",
                 "The 2026 rules allow it where the document's integrity and "
                 "authenticity can be verified, and practice is catching up with the "
                 "rules. It depends on what your country issues and on each document, "
                 "so it is worth asking before you commission anything rather than "
                 "assuming."),
            ]),

            ("The structure", [
                ("S.R.L., S.A.S. or S.A., which one is right for me?",
                 "S.R.L.: 2 to 50 quotaholders, the structure most foreign companies "
                 "use. S.A.S.: admits a single shareholder and is the most agile. S.A.: "
                 "for larger projects or if you plan to bring in investors. A "
                 "single-shareholder S.A. exists, but it requires the whole capital to "
                 "be paid in and a statutory auditor, so for a wholly-owned subsidiary "
                 "the S.A.S. is almost always the better choice. In the first "
                 "consultation we tell you which one applies to your case."),

                ("Can a foreigner own 100% of the company?",
                 "Yes. You do not need an Argentine partner or a minimum local "
                 "shareholding, and you do not need to be a resident to be a "
                 "shareholder. What the law requires is on the management side: at "
                 "least one representative domiciled in Argentina, which we can "
                 "provide. Profits from fiscal years closing from 2025 onwards can be "
                 "remitted abroad through the official exchange market, so for a new "
                 "company there is no obstacle on that point."),

                ("Can a foreign company be a shareholder?",
                 "Yes. It has to register with the IGJ under Article 123 of the "
                 "Companies Act, and since May 2026 that registration is filed together "
                 "with the incorporation, as a single procedure. It can even be the "
                 "sole shareholder of an S.A.S."),

                ("How much capital do I need to start?",
                 "The S.R.L. has no legal minimum, the S.A.S. requires two monthly "
                 "minimum wages (about USD 500 today) and the S.A. a minimum of "
                 "ARS 30,000,000 (about USD 19,500 today). In all three cases 25% is "
                 "paid in at incorporation and the balance within two years."),

                ("Do I need a physical office?",
                 "No. We provide a registered office and tax domicile in the City of "
                 "Buenos Aires that meets the legal requirement."
                 + _pagina(lang, "represent",
                           "Legal representation and registered office")),

                ("Do I need a resident director or manager?",
                 "Yes, at least one domiciled in Argentina. In an S.R.L. the majority "
                 "of the managers, in an S.A.S. at least one administrator. It is a "
                 "standard service we provide, with the guarantee the registry requires "
                 "included."),
            ]),

            ("Costs and taxes", [
                ("How much does it cost?",
                 "Incorporating a standard S.R.L. or S.A.S. starts at USD 3,000, "
                 "all-inclusive, fees and the registry, publication, notary and book "
                 "costs. If the shareholder is a foreign company, its Article 123 "
                 "registration adds USD 1,500, also all-inclusive. The only item quoted "
                 "separately is the sworn translation, because it depends on your "
                 "documents, and we give you the closed figure before you commit to "
                 "anything. No VAT, because it is an export of services."
                 + _nota(lang, "See the cost breakdown", "costos")),

                ("What taxes does my company pay?",
                 "Income tax on a scale from 25% to 35% depending on profit, VAT at "
                 "21%, turnover tax depending on the jurisdiction and activity, and "
                 "employer contributions if you hire. If your company exports services, "
                 "those exports are VAT-exempt."),

                ("How long does it take to open the bank account?",
                 "Between four and twelve weeks, and it depends on the bank, not on us. "
                 "We assist with the file and the follow-up, but the decision is the "
                 "bank's. It is the step clients underestimate most, so we start it as "
                 "soon as the tax ID is issued."),
            ]),

            ("Afterwards", [
                ("Do you only incorporate, or do you also provide ongoing support?",
                 "Both, and ongoing support is our strength. After incorporation we "
                 "handle the accounting, the taxes, the registry filings and act as "
                 "your ongoing legal advisor, all in one place and with a single point "
                 "of contact."
                 + _pagina(lang, "accounting", "Accounting, tax and compliance")),

                ("What obligations does the company have once incorporated?",
                 "Monthly and annual tax filings, annual financial statements with "
                 "their approval meeting, and registry filings every time something "
                 "changes, management, registered office, capital. A company that stops "
                 "filing does not fail loudly, it fails quietly, and you find out when "
                 "you need a certificate for a bank or an investor."),

                ("Do you handle other matters, such as trademarks?",
                 "Yes. We register trademarks with the INPI, with a prior search, the "
                 "filing and follow-up through to the certificate."
                 + _pagina(lang, "trademark", "Trademark registration")),

                ("What changed in 2026?",
                 "Quite a lot, and in your favour. The foreign parent's registration no "
                 "longer has to precede the incorporation, the professional "
                 "pre-qualification opinion is no longer required to incorporate, the "
                 "corporate purpose can be broad, capital no longer has to be justified "
                 "against the purpose, and the CDI for non-residents was replaced by "
                 "the CUIT. If you read a guide written before 2026, several of the "
                 "steps it describes no longer exist."
                 + _nota(lang, "See what changed in 2026", "cambios")),
            ]),
        ]

    return [
        ("Sobre el proceso", [
            ("¿Cuánto tarda constituir una empresa en Argentina?",
             "Una SRL o una SAS con socios personas físicas, alrededor de dos semanas "
             "desde que la documentación del exterior está completa, apostillada y "
             "traducida. Si un socio es una sociedad extranjera, su inscripción por el "
             "artículo 123 se presenta en simultáneo con la constitución desde mayo de "
             "2026 y el plazo pasa a ser de dos a cuatro semanas. Lo que más demora no "
             "es el registro, es la documentación que se produce en tu país."
             + _nota("es", "Leé la guía 2026")),

            ("¿Necesito viajar a Argentina?",
             "No. Todo el proceso se maneja de forma remota con un poder otorgado en tu "
             "país y apostillado allá. Vos firmás una vez, el resto lo hacemos "
             "nosotros."),

            ("¿Qué documentos necesito?",
             "Si los socios son personas físicas, pasaporte certificado y poder, "
             "apostillados y traducidos. Si el socio es una sociedad, además el "
             "estatuto, el certificado de constitución, un certificado de vigencia, la "
             "resolución que aprueba la inversión y el poder. Antes de que apostilles "
             "nada, revisamos los borradores, porque un poder mal redactado es la causa "
             "más común de demora."
             + _nota("es", "Ver el checklist de documentos", "checklist")),

            ("¿Sirve una traducción hecha en mi país?",
             "No. La traducción tiene que hacerla un traductor público matriculado en "
             "Argentina, y después se legaliza en el Colegio de Traductores. Un detalle "
             "que ahorra semanas: preguntá en qué idioma va a salir el sello de la "
             "apostilla, porque si está en un tercer idioma hacen falta dos "
             "traducciones."),

            ("¿Se aceptan documentos con apostilla digital?",
             "Las normas de 2026 lo permiten cuando se puede verificar la integridad y "
             "autenticidad del documento, y la práctica está acomodándose a las normas. "
             "Depende de lo que emita tu país y de cada documento, así que conviene "
             "preguntarlo antes de encargar nada en lugar de darlo por hecho."),
        ]),

        ("Sobre la estructura", [
            ("¿SRL, SAS o SA, cuál me conviene?",
             "SRL: de 2 a 50 socios, la estructura más usada por empresas extranjeras. "
             "SAS: admite un solo accionista y es la más ágil. SA: para proyectos más "
             "grandes o si vas a incorporar inversores. La SA con un solo accionista "
             "existe pero exige integrar todo el capital y tener sindicatura, así que "
             "para una filial al cien por ciento casi siempre conviene la SAS. En la "
             "primera consulta te decimos cuál aplica a tu caso."),

            ("¿Puede un extranjero ser dueño del 100%?",
             "Sí. No necesitás socio argentino ni participación local mínima, y no hace "
             "falta ser residente para ser socio. Lo que la ley exige es del lado de la "
             "administración: al menos un representante con domicilio en Argentina, que "
             "podemos proveer. Las utilidades de ejercicios cerrados desde 2025 en "
             "adelante pueden girarse al exterior por el mercado oficial, así que para "
             "una empresa nueva no hay traba en ese punto."),

            ("¿Puede una sociedad extranjera ser socia?",
             "Sí. Tiene que inscribirse ante la IGJ por el artículo 123 de la Ley "
             "General de Sociedades, y desde mayo de 2026 esa inscripción se presenta "
             "junto con la constitución, en un solo trámite. Puede ser incluso la única "
             "accionista de una SAS."),

            ("¿Cuánto capital necesito para empezar?",
             "La SRL no tiene mínimo legal, la SAS requiere dos salarios mínimos (hoy "
             "unos USD 500) y la SA un mínimo de ARS 30.000.000 (hoy cerca de "
             "USD 19.500). En los tres casos se integra el 25% al constituir y el resto "
             "dentro de los dos años."),

            ("¿Necesito una oficina física?",
             "No. Proveemos un domicilio legal y fiscal en la Ciudad de Buenos Aires "
             "que cumple con el requisito."
             + _pagina("es", "represent", "Representación legal y domicilio fiscal")),

            ("¿Necesito un director o gerente residente?",
             "Sí, al menos uno con domicilio en Argentina. En una SRL la mayoría de los "
             "gerentes, en una SAS al menos un administrador. Es un servicio habitual "
             "que prestamos nosotros, con la garantía que exige el registro incluida."),
        ]),

        ("Sobre costos e impuestos", [
            ("¿Cuánto cuesta?",
             "La constitución de una SRL o SAS estándar arranca en USD 3.000, todo "
             "incluido, honorarios y gastos de registro, publicación, escribanía y "
             "libros. Si el socio es una sociedad extranjera, su inscripción por el "
             "artículo 123 suma USD 1.500, también todo incluido. Lo único que se "
             "cotiza aparte es la traducción pública, porque depende de tus documentos, "
             "y te damos el número cerrado antes de que te comprometas a nada. Sin IVA, "
             "porque es exportación de servicios."
             + _nota("es", "Ver el detalle de costos", "costos")),

            ("¿Qué impuestos paga mi empresa?",
             "Impuesto a las Ganancias con una escala del 25 al 35% según la utilidad, "
             "IVA del 21%, Ingresos Brutos según la jurisdicción y la actividad, y "
             "cargas patronales si tenés empleados. Si tu empresa exporta servicios, "
             "las exportaciones no pagan IVA."),

            ("¿Cuánto tarda abrir la cuenta bancaria?",
             "Entre cuatro y doce semanas, y depende del banco, no de nosotros. Te "
             "asistimos con el legajo y el seguimiento, pero la decisión es del banco. "
             "Es el paso que más subestiman los clientes, así que lo arrancamos apenas "
             "sale el CUIT."),
        ]),

        ("Sobre el después", [
            ("¿Ofrecen solo constitución o también acompañamiento?",
             "Las dos cosas, y el acompañamiento es nuestro fuerte. Después de "
             "constituir, llevamos la contabilidad, los impuestos, las presentaciones "
             "ante el registro y somos tu asesor legal continuo, todo en un mismo lugar "
             "y con un solo interlocutor."
             + _pagina("es", "accounting", "Contabilidad, impuestos y cumplimiento")),

            ("¿Qué obligaciones tiene la empresa una vez constituida?",
             "Presentaciones fiscales mensuales y anuales, estados contables anuales "
             "con su reunión de aprobación, y trámites ante el registro cada vez que "
             "cambia algo, autoridades, sede, capital. Una empresa que deja de "
             "presentar no falla con ruido, falla en silencio, y uno se entera cuando "
             "necesita un certificado para el banco o para un inversor."),

            ("¿Se ocupan de otros temas, como marcas?",
             "Sí. Registramos marcas ante el INPI, con búsqueda previa, presentación y "
             "seguimiento hasta el título."
             + _pagina("es", "trademark", "Registro de marcas")),

            ("¿Qué cambió en 2026?",
             "Bastante, y a favor. La inscripción de la matriz extranjera ya no tiene "
             "que hacerse antes de la constitución, el dictamen profesional previo dejó "
             "de ser obligatorio para constituir, el objeto social puede ser amplio, el "
             "capital ya no tiene que justificarse frente al objeto y la CDI para no "
             "residentes fue reemplazada por el CUIT. Si leíste una guía anterior a "
             "2026, varios pasos que describe ya no existen."
             + _nota("es", "Ver qué cambió en 2026", "cambios")),
        ]),
    ]


COPY = {
    "en": {
        "title": "Setting Up a Company in Argentina: FAQ | SetUp Argentina",
        "desc": ("How long incorporation takes, which documents you need, which "
                 "structure to choose, costs and taxes. Updated for the 2026 reforms."),
        "crumbs": [("Home", "/"), ("FAQ", None)],
        "tag": "FAQ",
        "h1": "Setting up a company in Argentina: frequently asked questions",
        "lead": ("The questions we get asked most about incorporating and operating a "
                 "company in Argentina, updated for the 2026 reforms. If yours is not "
                 "here, write to us and you will have an answer the same day."),
        "cta_text": ("Still have a question? Tell us your case in two lines and you "
                     "will have an answer the same day. The first consultation is "
                     "free."),
        "cta_btn": "Book a free consultation",
        "cta_wa": "Message us on WhatsApp",
    },
    "es": {
        "title": "Constituir una empresa en Argentina: preguntas frecuentes | SetUp",
        "desc": ("Cuánto tarda constituir, qué documentos hacen falta, qué estructura "
                 "conviene, costos e impuestos. Actualizado a las reformas de 2026."),
        "crumbs": [("Inicio", "/es/"), ("Preguntas frecuentes", None)],
        "tag": "Preguntas frecuentes",
        "h1": "Constituir una empresa en Argentina: preguntas frecuentes",
        "lead": ("Las preguntas que más nos hacen sobre constituir y operar una "
                 "empresa en Argentina, actualizadas con las reformas de 2026. Si la "
                 "tuya no está, escribinos y te respondemos en el día."),
        "cta_text": ("¿Te quedó alguna duda? Contanos tu caso en dos líneas y te "
                     "respondemos en el día. La primera consulta es sin cargo."),
        "cta_btn": "Agendá una consulta sin cargo",
        "cta_wa": "Escribinos por WhatsApp",
    },
}


def _plano(html):
    """Texto de la respuesta para el JSON-LD.

    El link interno sale entero, no solo sus etiquetas: "Ver el detalle de
    costos" es un boton de la pagina, no parte de la respuesta, y en un
    resultado destacado de Google quedaria pegado al final de la frase.
    """
    sin_link = re.sub(r'\s*<a class="faq-link".*?</a>', "", html, flags=re.S)
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", sin_link)).strip()


def _cierre(lang, c):
    """Cierre con dos botones: la consulta y el WhatsApp."""
    wa = "https://wa.me/%s?text=%s" % (WA_NUMBER, quote(WA_TEXT[lang]))
    return f'''
<section class="cta-band">
  <div class="container">
    <p data-animate="fadeInUp">{c["cta_text"]}</p>
    <div class="cta-acciones" data-animate="fadeInUp">
      <a href="{url("contact", lang)}" class="btn-primary btn-large">
        <span>{c["cta_btn"]}</span>{ARROW_SVG}</a>
      <a href="{wa}" class="btn-ghost btn-large" target="_blank" rel="noopener">
        <span>{c["cta_wa"]}</span></a>
    </div>
  </div>
</section>
'''


def build():
    nl = "\n"
    for lang in ("en", "es"):
        c = COPY[lang]
        grupos = _qa(lang)

        bloques = []
        for titulo, preguntas in grupos:
            items = nl.join(
                '''      <details class="faq-acc">
        <summary>{q}</summary>
        <div class="faq-acc-body"><p>{a}</p></div>
      </details>'''.format(q=q, a=a) for q, a in preguntas)
            bloques.append(
                '    <h2 class="faq-grupo">%s</h2>\n'
                '    <div class="faq-list">\n%s\n    </div>' % (titulo, items))

        listado = nl.join(bloques)
        body = f'''
<header class="page-hero">
  <div class="container">
    <span class="section-tag" data-animate="fadeInUp">{c["tag"]}</span>
    <h1 data-animate="fadeInUp">{c["h1"]}</h1>
    <p class="page-lead" data-animate="fadeInUp">{c["lead"]}</p>
  </div>
</header>

<section class="faq-section">
  <div class="container" data-animate="fadeInUp">
{listado}
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
                 "acceptedAnswer": {"@type": "Answer", "text": _plano(a)}}
                for _, preguntas in grupos for q, a in preguntas
            ],
        }
        yield "faq", lang, render.page(
            "faq", lang, title=c["title"], description=c["desc"],
            body=body + _cierre(lang, c),
            schema=schema, crumbs=c["crumbs"])
