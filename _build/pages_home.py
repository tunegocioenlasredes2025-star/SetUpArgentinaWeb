# -*- coding: utf-8 -*-
"""Home en los dos idiomas.

Reusa las clases y los iconos de la landing original, asi que se ve igual
que el sitio que el cliente ya aprobo. La diferencia es que ahora cada
servicio linkea a su pagina propia en vez de a un ancla.

La version en espanol omite "Why Argentina" y la cobertura geografica:
segun el documento del cliente, esas dos secciones estan pensadas solo
para el mercado del exterior.
"""

import render
from chrome import ARROW_SVG, CHECK_SVG, SERVICE_NAMES, SERVICE_ORDER
from legacy_assets import HERO_VISUAL, WHY_ICONS, SERVICE_ICONS, CHIP_ICONS
from pages_services import SUMMARY
from site_cfg import SITE, EMAIL, url

COPY = {
    "en": {
        "title": "Company Formation, Legal and Accounting Services in Argentina | SetUp",
        "desc": ("Set up and run your company in Argentina 100% remotely. Company "
                 "formation, tax, accounting and ongoing business and legal advisory. "
                 "Specialists in foreign companies."),
        "eyebrow": "Buenos Aires, Argentina &nbsp;·&nbsp; Bilingual Advisory",
        "h1": ["Your Trusted Partner", "For Doing Business", "In Argentina"],
        "sub": ("SetUp Argentina handles company formation, tax, accounting and ongoing "
                "business and legal advisory, for foreign investors and local companies "
                "alike. Full legal and accounting support from day one, 100% remote, so "
                "you can focus on growing your business."),
        "points": ["In-house bilingual team of licensed lawyers and accountants",
                   "50+ foreign companies incorporated", "Fully remote"],
        "cta1": "Book a Free Consultation",
        "cta2": "Explore Services",
        "tags": ["Company Formation", "Tax ID", "Legal Representation", "Ongoing Compliance"],
        "scroll": "Scroll to explore",
        "stats": [
            ("50", "+", "Companies Incorporated",
             "Foreign companies successfully established in Argentina to date."),
            ("24–48", "h", "Response Time",
             "All inquiries handled directly by a licensed professional."),
            ("10–30", "d", "Formation Timeline",
             "From complete documentation to fully registered company."),
            ("100", "%", "Remote Process",
             "No travel required, the entire process handled from anywhere."),
        ],
        "why_label": "Market Opportunity",
        "why_h2": "Why Expand Into Argentina?",
        "why_sub": ("Argentina is Latin America's third-largest economy. Its legal "
                    "framework allows full ownership by foreign individuals and companies "
                    "as well as local residents, with predictable incorporation timelines "
                    "and competitive start-up costs compared with the rest of the region. "
                    "A single local partner for legal and accounting removes the friction "
                    "of operating from abroad, or of formalizing a business at home."),
        "why": [
            ("Full Foreign Ownership",
             "Argentina's legal framework allows full ownership by foreign individuals "
             "and companies, with the same rights as local residents and predictable "
             "corporate structures."),
            ("Competitive Start-Up Costs",
             "Competitive incorporation timelines and start-up costs compared with the "
             "rest of the region, one of the most accessible entry points in Latin America."),
            ("World-Class Talent Pool",
             "One of Latin America's highest literacy rates and a deep pool of highly "
             "educated professionals in technology, law, finance and creative industries, "
             "at competitive salaries."),
            ("Established Legal Framework",
             "A sophisticated legal and corporate system based on civil law, with "
             "predictable entity structures (SRL, SAS, SA) and well-established compliance "
             "procedures through the companies registry (IGJ) and the tax authority (ARCA)."),
            ("Thriving Tech and Services Ecosystem",
             "Buenos Aires is home to a booming tech and professional services sector, "
             "with Argentina exporting over USD 3B annually in software and digital services."),
            ("One Partner, Zero Friction",
             "Operating from abroad is complex. A single local partner for legal and "
             "accounting removes the friction, whether you are formalizing remotely or "
             "scaling on the ground."),
        ],
        "svc_label": "What We Do",
        "svc_h2": "End-to-End Corporate Services",
        "svc_sub": ("From company registration to ongoing advisory, SetUp is your one-stop "
                    "solution, handling every step so you can focus entirely on growing "
                    "your business."),
        "svc_note": ("We also handle trademark registration, visas for company directors "
                     "and other legal and tax matters, on request."),
        "svc_cta": "Not sure which services you need? Let's talk.",
        "proc_label": "Simple Process",
        "proc_h2": "From First Contact to Fully Operational",
        "proc_sub": ("A clear, guided path, with SetUp managing every step so you never "
                     "navigate Argentine bureaucracy alone."),
        "steps": [
            ("Free Consultation",
             "We map your goals, the right entity type and a realistic timeline.",
             "Same-day response"),
            ("Documentation and Powers of Attorney",
             "We prepare everything; apostilled POAs if you are abroad, so you never "
             "have to travel.", "2-3 business days"),
            ("Incorporation",
             "Bylaws, name reservation, Official Gazette publication and final "
             "registration with the companies registry.", "10-30 business days"),
            ("Tax ID",
             "Tax registration and your company tax ID, so you can invoice, open a bank "
             "account and operate.", "~5 business days"),
            ("Up and Running",
             "Corporate books, ongoing accounting and compliance handled for you.",
             "Continuous"),
        ],
        "proc_cta": "Start the Process",
        "ind_label": "Industries We Serve",
        "ind_h2": "Expertise Across Sectors",
        "ind_sub": ("We work with companies across all major industries entering or "
                    "operating in the Argentine market."),
        "industries": ["Technology &amp; SaaS", "Software Development", "Manufacturing",
                       "Logistics &amp; Supply Chain", "Retail &amp; E-commerce",
                       "Financial Services", "Healthcare &amp; Biotech",
                       "Startups &amp; Scaleups", "Professional Services",
                       "Media &amp; Entertainment", "Real Estate",
                       "AgTech &amp; Agriculture"],
        "wu_label": "Why SetUp",
        "wu_h2": "What Sets Us Apart",
        "wu_sub": ("One firm for the whole journey, legal and accounting under one roof, "
                   "in your language."),
        "wu": [
            ("In-House Bilingual Team",
             "In-house, bilingual team of licensed lawyers and accountants (CPACF), "
             "not a referral middleman."),
            ("Cross-Border Specialists",
             "Specialists in foreign companies entering Argentina, with cross-border "
             "experience."),
            ("Fully Remote",
             "Incorporate and operate in Argentina without travelling or renting an office."),
            ("One Dedicated Professional",
             "One dedicated professional per client: direct contact, senior attention, "
             "no intermediaries."),
            ("A Single Point of Contact",
             "One point of contact for everything: formation, tax ID, legal representation, "
             "accounting, payroll and compliance."),
            ("Deep Local Knowledge",
             "Deep local knowledge of the companies registry (IGJ), the tax authority "
             "(ARCA) and Argentine corporate law, with multinational experience "
             "(Accenture, Biz Latin Hub)."),
        ],
        "geo_label": "Global Reach",
        "geo_h2": "We Serve Companies From Every Corner of the World",
        "regions": [
            ("The Americas",
             "United States · Canada · Mexico · Brazil · Colombia · Chile · Peru"),
            ("Europe",
             "Spain · Germany · France · Italy · United Kingdom · Netherlands · Portugal"),
            ("Asia and Rest of World",
             "China · Japan · India · UAE · Israel · Australia, and beyond"),
        ],
        "part_h2": "Are you a law or accounting firm?",
        "part_text": ("If your clients are expanding into Argentina, partner with a "
                      "reliable local team. We handle the local execution, company "
                      "formation, tax, compliance and legal advisory, while you keep "
                      "the relationship with your client."),
        "part_btn": "Partner with us",
        "close_text": ("Book a free initial consultation and get a personalized roadmap "
                       "for doing business in Argentina."),
        "learn": "Learn more",
    },
    "es": {
        "title": "Constitución de empresas, servicios legales y contables | SetUp Argentina",
        "desc": ("Constituí tu empresa, llevá tu contabilidad y contá con asesoramiento "
                 "empresarial y legal continuo. Estudio jurídico-contable, todo online. "
                 "Consulta sin cargo."),
        "eyebrow": "Buenos Aires, Argentina &nbsp;·&nbsp; Estudio jurídico-contable",
        "h1": ["Tu socio de confianza", "para hacer negocios", "en Argentina"],
        "sub": ("SetUp Argentina se ocupa de la constitución, los impuestos, la "
                "contabilidad y el asesoramiento empresarial y legal continuo, para "
                "empresas locales e inversores del exterior. Acompañamiento jurídico y "
                "contable desde el primer día, todo online, para que te enfoques en "
                "tu negocio."),
        "points": ["Equipo propio y bilingüe de abogados y contadores",
                   "+50 empresas constituidas", "100% online"],
        "cta1": "Agendá una consulta sin cargo",
        "cta2": "Ver servicios",
        "tags": ["Constitución", "CUIT", "Representación legal", "Cumplimiento"],
        "scroll": "Deslizá para explorar",
        "stats": [
            ("50", "+", "Empresas constituidas",
             "Empresas establecidas en Argentina a la fecha."),
            ("24–48", "h", "Tiempo de respuesta",
             "Cada consulta la atiende directamente un profesional."),
            ("10–30", "d", "Plazo de constitución",
             "Desde la documentación completa hasta la empresa inscripta."),
            ("100", "%", "Online",
             "Sin necesidad de traslados, todo el proceso a distancia."),
        ],
        "svc_label": "Qué hacemos",
        "svc_h2": "Servicios corporativos de punta a punta",
        "svc_sub": ("Desde la constitución hasta el acompañamiento continuo, SetUp es tu "
                    "solución integral, ocupándose de cada paso para que te enfoques en "
                    "tu negocio."),
        "svc_note": ("También nos ocupamos del registro de marcas, visas para directores "
                     "y otros temas legales e impositivos, a pedido."),
        "svc_cta": "¿No sabés qué servicio necesitás? Hablemos.",
        "proc_label": "Proceso simple",
        "proc_h2": "Del primer contacto a estar operativo",
        "proc_sub": ("Un camino claro y guiado, con SetUp ocupándose de cada paso para "
                     "que no navegues la burocracia argentina solo."),
        "steps": [
            ("Consulta sin cargo",
             "Definimos tus objetivos, el tipo de sociedad y un plazo realista.",
             "Respuesta en el día"),
            ("Documentación y poderes",
             "Preparamos todo; poderes apostillados si estás en el exterior, para que "
             "no tengas que viajar.", "2-3 días hábiles"),
            ("Constitución",
             "Estatuto, reserva de nombre, publicación en el Boletín Oficial e "
             "inscripción ante la IGJ.", "10-30 días hábiles"),
            ("CUIT",
             "Inscripción impositiva y CUIT, para que puedas facturar, abrir cuenta "
             "y operar.", "~5 días hábiles"),
            ("En marcha",
             "Libros societarios, contabilidad y cumplimiento continuo a cargo nuestro.",
             "Continuo"),
        ],
        "proc_cta": "Empezar el proceso",
        "ind_label": "Industrias",
        "ind_h2": "Experiencia en todos los rubros",
        "ind_sub": ("Trabajamos con empresas de todos los rubros que entran u operan en "
                    "el mercado argentino."),
        "industries": ["Tecnología y SaaS", "Desarrollo de software", "Industria",
                       "Logística", "Retail y e-commerce", "Servicios financieros",
                       "Salud y biotecnología", "Startups", "Servicios profesionales",
                       "Medios y entretenimiento", "Real estate", "AgTech y agro"],
        "wu_label": "Por qué SetUp",
        "wu_h2": "Lo que nos distingue",
        "wu_sub": ("Un solo estudio para todo el camino, lo legal y lo contable en un "
                   "mismo lugar."),
        "wu": [
            ("Equipo propio y bilingüe",
             "Equipo propio y bilingüe de abogados y contadores (CPACF), no un "
             "intermediario que deriva."),
            ("Especialistas cross-border",
             "Especialistas en empresas extranjeras que entran a Argentina, con "
             "experiencia cross-border."),
            ("100% online",
             "Constituí y operá sin viajar ni alquilar una oficina."),
            ("Un profesional dedicado",
             "Un profesional dedicado por cliente: contacto directo, atención senior, "
             "sin intermediarios."),
            ("Un único punto de contacto",
             "Un solo contacto para todo: constitución, CUIT, representación legal, "
             "contabilidad, sueldos y cumplimiento."),
            ("Conocimiento local profundo",
             "Conocimiento profundo de la IGJ, ARCA y el derecho societario argentino, "
             "con experiencia en multinacionales (Accenture, Biz Latin Hub)."),
        ],
        "part_h2": "¿Sos un estudio jurídico o contable?",
        "part_text": ("Si tus clientes se expanden a Argentina, sumate a un equipo local "
                      "confiable. Nos ocupamos de la ejecución local, constitución, "
                      "impuestos, cumplimiento y asesoramiento, mientras vos mantenés "
                      "la relación con tu cliente."),
        "part_btn": "Trabajemos juntos",
        "close_text": ("Agendá una consulta inicial sin cargo y llevate una hoja de ruta "
                       "personalizada para tu empresa en Argentina."),
        "learn": "Ver más",
    },
}


def _hero(lang, c):
    points = "".join("<span>%s%s</span>" % (CHECK_SVG, p) for p in c["points"])
    tags = "".join("<span>%s</span>" % t for t in c["tags"])
    h1 = ('%s<br><span class="gradient-text">%s</span><br>%s'
          % (c["h1"][0], c["h1"][1], c["h1"][2]))
    return f'''
<section id="hero">
  <div class="hero-bg-gradient"></div>
  <div class="hero-particles"></div>
  <div class="container hero-layout">
    <div class="hero-content" data-animate="fadeInLeft">
      <div class="hero-eyebrow"><span class="dot-pulse"></span>{c["eyebrow"]}</div>
      <h1 class="hero-title">{h1}</h1>
      <p class="hero-subtitle">{c["sub"]}</p>
      <div class="hero-trust-line">{points}</div>
      <div class="hero-buttons">
        <a href="{url("contact", lang)}" class="btn-primary btn-lg">{c["cta1"]}</a>
        <a href="{url("services", lang)}" class="btn-ghost btn-lg">{c["cta2"]}</a>
      </div>
      <div class="hero-tags">{tags}</div>
    </div>
    {HERO_VISUAL}
  </div>
  <div class="hero-scroll-indicator"><span>{c["scroll"]}</span><div class="scroll-line"></div></div>
</section>
'''


def _stats(c):
    out = []
    for i, (num, unit, label, desc) in enumerate(c["stats"]):
        if num == "50":
            number = ('<div class="stat-number"><span class="counter" data-target="50">0'
                      '</span><span class="stat-suffix">+</span></div>')
        else:
            number = ('<div class="stat-number">%s<span class="stat-unit">%s</span></div>'
                      % (num, unit))
        out.append('<div class="stat-item" data-animate="fadeInUp" data-delay="%d">%s'
                   '<div class="stat-label">%s</div><div class="stat-desc">%s</div></div>'
                   % (i * 100, number, label, desc))
    return ('<section class="section-trust"><div class="container"><div class="stats-grid">'
            + '<div class="stat-divider"></div>'.join(out)
            + "</div></div></section>")


def _section(label, h2, sub, inner, css="section-dark", sid=""):
    ident = ' id="%s"' % sid if sid else ""
    return f'''
<section{ident} class="{css}">
  <div class="container">
    <div class="section-label" data-animate="fadeInUp">{label}</div>
    <h2 class="section-title" data-animate="fadeInUp">{h2}</h2>
    <p class="section-subtitle" data-animate="fadeInUp">{sub}</p>
{inner}
  </div>
</section>
'''


def _why_argentina(c):
    cards = "\n".join(
        '      <div class="why-card" data-animate="fadeInUp" data-delay="%d">'
        '<div class="why-icon">%s</div><h3>%s</h3><p>%s</p></div>'
        % ((i % 3) * 100, WHY_ICONS[i], t, d)
        for i, (t, d) in enumerate(c["why"]))
    return _section(c["why_label"], c["why_h2"], c["why_sub"],
                    '    <div class="why-grid">\n%s\n    </div>' % cards,
                    sid="why-argentina")


def _services(lang, c):
    cards = "\n".join(
        '      <a href="%s" class="service-card" data-animate="fadeInUp" data-delay="%d">'
        '<div class="service-icon">%s</div><h3>%s</h3><p>%s</p>'
        '<div class="service-tag">%s %s</div></a>'
        % (url(k, lang), i * 80, SERVICE_ICONS[i], SERVICE_NAMES[lang][k],
           SUMMARY[lang][k], c["learn"], ARROW_SVG)
        for i, k in enumerate(SERVICE_ORDER))
    inner = ('    <div class="services-grid">\n%s\n    </div>\n'
             '    <p class="svc-note" data-animate="fadeInUp">%s %s</p>\n'
             '    <div class="services-cta" data-animate="fadeInUp"><p>%s</p>'
             '<a href="%s" class="btn-primary">%s</a></div>'
             % (cards, CHECK_SVG, c["svc_note"], c["svc_cta"],
                url("contact", lang), c["cta1"]))
    return _section(c["svc_label"], c["svc_h2"], c["svc_sub"], inner,
                    css="section-light", sid="services")


def _process(lang, c):
    steps = "\n".join(
        '      <div class="process-step" data-animate="fadeInUp" data-delay="%d">'
        '<div class="step-number">%02d</div><div class="step-content"><h3>%s</h3>'
        '<p>%s</p><div class="step-duration">%s</div></div></div>'
        % (i * 80, i + 1, t, d, dur)
        for i, (t, d, dur) in enumerate(c["steps"]))
    inner = ('    <div class="process-timeline">\n%s\n    </div>\n'
             '    <div class="section-cta" data-animate="fadeInUp">'
             '<a href="%s" class="btn-primary">%s</a></div>'
             % (steps, url("contact", lang), c["proc_cta"]))
    return _section(c["proc_label"], c["proc_h2"], c["proc_sub"], inner, sid="process")


def _industries(c):
    chips = "\n".join(
        '      <div class="industry-chip" data-animate="fadeInUp" data-delay="%d">%s%s</div>'
        % ((i % 4) * 50, CHIP_ICONS[i], name)
        for i, name in enumerate(c["industries"]))
    return _section(c["ind_label"], c["ind_h2"], c["ind_sub"],
                    '    <div class="industries-grid">\n%s\n    </div>' % chips,
                    css="section-light")


def _why_us(c):
    cards = "\n".join(
        '      <div class="why-us-card%s" data-animate="fadeInUp" data-delay="%d">'
        '<div class="wu-number">%02d</div><h3>%s</h3><p>%s</p></div>'
        % (" featured" if i == 0 else "", (i % 3) * 100, i + 1, t, d)
        for i, (t, d) in enumerate(c["wu"]))
    return _section(c["wu_label"], c["wu_h2"], c["wu_sub"],
                    '    <div class="why-us-grid">\n%s\n    </div>' % cards)


def _regions(c):
    regs = "\n".join(
        '        <div class="region"><div class="region-label">%s</div>'
        '<div class="region-countries">%s</div></div>' % (label, countries)
        for label, countries in c["regions"])
    return f'''
<section class="section-light global-reach">
  <div class="container">
    <div class="section-label" data-animate="fadeInUp">{c["geo_label"]}</div>
    <h2 class="section-title" data-animate="fadeInUp">{c["geo_h2"]}</h2>
    <div class="regions-grid" data-animate="fadeInUp">
{regs}
    </div>
  </div>
</section>
'''


def _partners(lang, c):
    return f'''
<section class="cta-band">
  <div class="container">
    <h2 class="section-title" data-animate="fadeInUp">{c["part_h2"]}</h2>
    <p data-animate="fadeInUp">{c["part_text"]}</p>
    <a href="{url("partners", lang)}" class="btn-primary btn-large" data-animate="fadeInUp">
      <span>{c["part_btn"]}</span>{ARROW_SVG}</a>
  </div>
</section>
'''


def _closing(lang, c):
    return f'''
<section class="section-dark home-closing">
  <div class="container">
    <h2 class="section-title" data-animate="fadeInUp">{c["close_text"]}</h2>
    <div class="section-cta" data-animate="fadeInUp">
      <a href="{url("contact", lang)}" class="btn-primary btn-lg">{c["cta1"]}</a></div>
  </div>
</section>
'''


def build():
    for lang in ("en", "es"):
        c = COPY[lang]
        parts = [_hero(lang, c), _stats(c)]
        if lang == "en":
            # Solo para el mercado del exterior, segun el documento del cliente.
            parts.append(_why_argentina(c))
        parts += [_services(lang, c), _process(lang, c), _industries(c), _why_us(c)]
        if lang == "en":
            parts.append(_regions(c))
        parts += [_partners(lang, c), _closing(lang, c)]

        schema = [
            {
                "@context": "https://schema.org",
                "@type": "ProfessionalService",
                "@id": SITE + "/#organization",
                "name": "SetUp Argentina",
                "description": c["desc"],
                "url": SITE,
                "email": EMAIL,
                "areaServed": {"@type": "Country", "name": "Argentina"},
                "address": {"@type": "PostalAddress", "addressLocality": "Buenos Aires",
                            "addressRegion": "CABA", "addressCountry": "AR"},
                "founder": {"@type": "Person", "name": "Agustín Sofía"},
                "knowsLanguage": ["es", "en"],
                "hasOfferCatalog": {
                    "@type": "OfferCatalog",
                    "name": c["svc_h2"],
                    "itemListElement": [
                        {"@type": "Offer",
                         "itemOffered": {
                             "@type": "Service",
                             "name": SERVICE_NAMES[lang][k].replace("&amp;", "and"),
                             "url": SITE + url(k, lang)}}
                        for k in SERVICE_ORDER],
                },
            },
            {
                "@context": "https://schema.org",
                "@type": "WebSite",
                "url": SITE,
                "name": "SetUp Argentina",
                "inLanguage": "en" if lang == "en" else "es-AR",
            },
        ]
        yield "home", lang, render.page(
            "home", lang, title=c["title"], description=c["desc"],
            body="\n".join(parts), schema=schema)
