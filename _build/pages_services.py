# -*- coding: utf-8 -*-
"""Indice de servicios + las 4 paginas de servicio, en los dos idiomas.

Cada servicio tiene su propia URL porque es lo que le da a Google una
pagina distinta por cada busqueda con intencion de compra. Todo el texto
sale del documento de contenido del cliente; no se inventa nada.
"""

import render
from chrome import ARROW_SVG, CHECK_SVG, cta_band, SERVICE_NAMES, SERVICE_ORDER
from site_cfg import SITE, url

LABELS = {
    "en": {
        "svc_tag": "Service",
        "h_structures": "The structures",
        "h_foreign": "For foreign companies and shareholders",
        "h_included": "What is included",
        "h_who": "Who it is for",
        "cta_btn": "Request a Free Consultation",
        "cta_text": ("Book a free initial consultation and get a personalized roadmap "
                     "for doing business in Argentina."),
        "index_title": "Corporate Services in Argentina | SetUp Argentina",
        "index_desc": ("Company formation, accounting and tax compliance, ongoing legal "
                       "advisory and registered office. One firm, fully remote."),
        "index_tag": "What We Do",
        "index_h1": "End-to-End Corporate Services",
        "index_lead": ("From company registration to ongoing advisory, SetUp is your "
                       "one-stop solution, handling every step so you can focus entirely "
                       "on growing your business."),
        "index_note": ("We also handle trademark registration, visas for company directors "
                       "and other legal and tax matters, on request."),
        "read_more": "Learn more",
        "crumb_home": "Home",
        "crumb_services": "Services",
    },
    "es": {
        "svc_tag": "Servicio",
        "h_structures": "Las estructuras",
        "h_foreign": "Para socios y sociedades del exterior",
        "h_included": "Qué incluye",
        "h_who": "Para quién es",
        "cta_btn": "Agendá una consulta sin cargo",
        "cta_text": ("Agendá una consulta inicial sin cargo y llevate una hoja de ruta "
                     "personalizada para tu empresa en Argentina."),
        "index_title": "Servicios corporativos en Argentina | SetUp Argentina",
        "index_desc": ("Constitución de sociedades, contabilidad e impuestos, asesoramiento "
                       "continuo y domicilio fiscal. Un solo estudio, todo online."),
        "index_tag": "Qué hacemos",
        "index_h1": "Servicios corporativos de punta a punta",
        "index_lead": ("Desde la constitución hasta el acompañamiento continuo, SetUp es "
                       "tu solución integral, ocupándose de cada paso para que te enfoques "
                       "en tu negocio."),
        "index_note": ("También nos ocupamos del registro de marcas, visas para directores "
                       "y otros temas legales e impositivos, a pedido."),
        "read_more": "Ver más",
        "crumb_home": "Inicio",
        "crumb_services": "Servicios",
    },
}

# Resumen corto para el indice y para la home.
SUMMARY = {
    "en": {
        "formation": ("Incorporate an SRL, SAS or SA end to end, including your tax ID "
                      "and, for foreign company shareholders, the Article 123 or 118 "
                      "registration."),
        "accounting": ("Monthly filings (VAT, Turnover Tax, Income Tax), financial "
                       "statements, corporate compliance and payroll."),
        "advisory": ("Your ongoing corporate advisor: company law, labor law, contracts "
                     "and the day-to-day decisions of running a business."),
        "represent": ("Locally-resident legal representative and registered fiscal "
                      "domicile to keep your company compliant."),
        "trademark": ("Protect your brand in Argentina: availability search, filing "
                      "before the trademark office (INPI) and follow-up."),
    },
    "es": {
        "formation": ("Constituí una SRL, SAS o SA de punta a punta, incluido el CUIT y, "
                      "para socios del exterior, la inscripción del Art. 123 o 118."),
        "accounting": ("Presentaciones mensuales (IVA, Ingresos Brutos, Ganancias), "
                       "estados contables, cumplimiento societario y sueldos."),
        "advisory": ("Tu asesor societario continuo: derecho societario, laboral, "
                     "contratos y las decisiones del día a día."),
        "represent": ("Representante legal residente y domicilio fiscal para mantener "
                      "tu empresa en regla."),
        "trademark": ("Protegé tu marca en Argentina: búsqueda de antecedentes, "
                      "presentación ante el INPI y seguimiento del trámite."),
    },
}

SERVICES = {
    "formation": {
        "en": {
            "title": "Company Formation in Argentina (SRL, SAS, SA) | SetUp Argentina",
            "desc": ("Set up your company in Argentina 100% remotely. SRL, SAS and SA, "
                     "with tax registration and foreign shareholders handled."),
            "h1": "Company Formation in Argentina",
            "intro": ("Setting up a company in Argentina involves several moving parts: "
                      "choosing the right vehicle, drafting bylaws that comply with local "
                      "law, registering with the companies registry (IGJ), obtaining tax "
                      "IDs and opening a bank account. We manage the entire process end to "
                      "end and fully remotely, so you can incorporate without travelling "
                      "and start operating with everything in order from day one."),
            "structures": ("The three most common vehicles are the <strong>SRL</strong> "
                           "(limited liability company, the classic choice for operating "
                           "businesses), the <strong>SAS</strong> (simplified corporation, "
                           "the fastest and most flexible option) and the <strong>SA</strong> "
                           "(corporation, generally used by larger operations). Minimum "
                           "capital is modest: the SRL has no fixed minimum, the SAS requires "
                           "the equivalent of two minimum wages (currently around USD 500) "
                           "and the SA a higher figure (currently around USD 20,000). We "
                           "advise you on the structure that best fits your business, your "
                           "shareholders and your plans."),
            "foreign": ("Foreign individuals and companies can own 100% of an Argentine "
                        "company. If your shareholder is a foreign company, it must first "
                        "register locally under Article 123 (to hold shares in a subsidiary) "
                        "or operate through a branch under Article 118, and foreign "
                        "shareholders need an Argentine tax ID. We handle all of it, the "
                        "Article 123 or 118 registration, apostilled documents, sworn "
                        "translations and the tax IDs, as part of the formation, so you can "
                        "set up entirely from abroad."),
            "included": [
                "Advice on the right structure",
                "Drafting of bylaws",
                "Name reservation",
                "Official Gazette publication",
                "Registration with the companies registry",
                "Corporate and foreign-shareholder tax IDs",
                "Article 123 or 118 registration where applicable",
                "Digital corporate books",
                "Guidance to open a corporate bank account",
            ],
            "who": ("Local and international companies, investors and entrepreneurs, "
                    "from startups to established groups."),
        },
        "es": {
            "title": "Constitución de sociedades: SRL, SAS y SA | SetUp",
            "desc": ("Constituí tu empresa en Argentina 100% online. SRL, SAS y SA, con la "
                     "inscripción impositiva y los socios extranjeros resueltos. Primera "
                     "consulta sin cargo."),
            "h1": "Constitución de sociedades en Argentina",
            "intro": ("Constituir una empresa en Argentina tiene varias etapas: elegir el "
                      "vehículo adecuado, redactar un estatuto que cumpla con la normativa, "
                      "inscribir la sociedad ante la IGJ, obtener los identificadores "
                      "fiscales y abrir la cuenta bancaria. Gestionamos todo el proceso de "
                      "punta a punta y de forma remota, para que constituyas sin moverte y "
                      "empieces a operar con todo en regla desde el primer día."),
            "structures": ("Los tres vehículos más usados son la <strong>SRL</strong> "
                           "(responsabilidad limitada, la clásica para empresas operativas), "
                           "la <strong>SAS</strong> (por acciones simplificada, la más ágil "
                           "y rápida) y la <strong>SA</strong> (para operaciones más grandes). "
                           "El capital mínimo es accesible: la SRL no tiene mínimo fijo, la "
                           "SAS requiere el equivalente a dos salarios mínimos (hoy unos "
                           "USD 500) y la SA un monto mayor (hoy cerca de USD 20.000). Te "
                           "asesoramos sobre la estructura que mejor se adapta a tu caso."),
            "foreign": ("Las personas y sociedades extranjeras pueden ser dueñas del 100% "
                        "de una empresa argentina. Si tu socio es una sociedad del exterior, "
                        "primero debe inscribirse bajo el Art. 123 (para participar en una "
                        "filial) u operar como sucursal bajo el Art. 118, y los socios "
                        "extranjeros necesitan identificador fiscal argentino. Nos ocupamos "
                        "de todo, la inscripción del Art. 123 o 118, los documentos "
                        "apostillados, las traducciones públicas y los identificadores, "
                        "como parte de la constitución."),
            "included": [
                "Asesoramiento sobre la estructura",
                "Redacción del estatuto",
                "Reserva de nombre",
                "Publicación en el Boletín Oficial",
                "Inscripción ante la IGJ",
                "CUIT de la sociedad y CDI de los socios extranjeros",
                "Inscripción del Art. 123 o 118 cuando corresponde",
                "Libros societarios digitales",
                "Guía para abrir la cuenta bancaria",
            ],
            "who": ("Empresas, inversores y emprendedores, locales e internacionales, "
                    "desde startups hasta grupos consolidados."),
        },
    },
    "accounting": {
        "en": {
            "title": "Accounting, Tax and Compliance in Argentina | SetUp Argentina",
            "desc": ("Monthly accounting, tax filings and corporate compliance for your "
                     "Argentine company. VAT, Turnover Tax and Income Tax, handled."),
            "h1": "Accounting, Tax and Compliance in Argentina",
            "intro": ("Once your company is operating, staying compliant in Argentina is a "
                      "monthly job: VAT, Turnover Tax and Income Tax filings, bookkeeping, "
                      "financial statements and the annual obligations before the companies "
                      "registry (IGJ). Deadlines are strict and the rules change often. We "
                      "take the whole thing off your plate, keeping your accounting up to "
                      "date, filing every return on time and handling your annual corporate "
                      "compliance, all managed remotely with a single point of contact who "
                      "knows your case."),
            "included": [
                "Monthly bookkeeping",
                "VAT, Turnover Tax and Income Tax filings",
                "Financial statements",
                "Annual corporate compliance (corporate books, renewal of authorities "
                "and UBO filings)",
                "Payroll administration (optional)",
                "A single point of contact for every deadline",
            ],
            "who": ("Companies operating in Argentina that want reliable ongoing "
                    "accounting and tax compliance."),
        },
        "es": {
            "title": "Contabilidad, impuestos y cumplimiento | SetUp Argentina",
            "desc": ("Contabilidad mensual, impuestos y obligaciones societarias de tu "
                     "empresa. IVA, Ingresos Brutos, Ganancias e IGJ, todo al día. "
                     "Planes a medida."),
            "h1": "Contabilidad, impuestos y cumplimiento",
            "intro": ("Cuando tu empresa ya opera, mantenerse en regla en Argentina es un "
                      "trabajo mensual: IVA, Ingresos Brutos y Ganancias, contabilidad, "
                      "estados contables y las obligaciones anuales ante la IGJ. Los "
                      "vencimientos son estrictos y las normas cambian seguido. Nos ocupamos "
                      "de todo, todo remoto y con un único contacto que conoce tu caso."),
            "included": [
                "Contabilidad mensual",
                "Presentaciones de IVA, Ingresos Brutos y Ganancias",
                "Estados contables",
                "Cumplimiento societario anual (libros, renovación de autoridades, "
                "DDJJ de beneficiario final)",
                "Liquidación de sueldos (opcional)",
                "Un solo contacto para cada vencimiento",
            ],
            "who": ("Empresas que operan en Argentina y quieren contabilidad y "
                    "cumplimiento continuo confiable."),
        },
    },
    "advisory": {
        "en": {
            "title": "Business and Legal Advisory in Argentina | SetUp Argentina",
            "desc": ("An outsourced business and legal advisor for your Argentine company. "
                     "Corporate and shareholder matters, labor law, contracts and "
                     "day-to-day decisions."),
            "h1": "Business and Legal Advisory",
            "intro": ("This is the core of what we do. Beyond setting a company up, most of "
                      "our value is ongoing: acting as the outsourced business and legal "
                      "advisor for your operation in Argentina. From corporate and "
                      "shareholder matters to labor law, contracts and the day-to-day "
                      "decisions of running a business, you have a senior advisor who knows "
                      "your company and works alongside the accounting side, so your "
                      "business, legal and tax positions always stay aligned. It is the "
                      "difference between a provider that only incorporates your company "
                      "and a partner that helps you run it."),
            "included": [
                "Corporate and company law",
                "Labor and employment law",
                "Drafting and review of contracts",
                "Shareholder and board matters",
                "General ongoing business and legal consultations",
                "Available as part of a monthly plan",
            ],
            "who": ("Companies that want a continuous business and legal advisor, "
                    "not just one-off services."),
        },
        "es": {
            "title": "Asesoramiento empresarial y legal en Argentina | SetUp Argentina",
            "desc": ("Un asesor empresarial y legal externo para tu empresa. Temas "
                     "societarios y de socios, derecho laboral, contratos y las "
                     "decisiones del día a día."),
            "h1": "Asesoramiento empresarial y legal continuo",
            "intro": ("Este es el centro de lo que hacemos. Más allá de constituir, nuestro "
                      "mayor valor es el acompañamiento continuo: ser el asesor empresarial "
                      "y legal externo de tu operación en Argentina. Desde temas societarios "
                      "y de socios hasta derecho laboral, contratos y las decisiones del día "
                      "a día, tenés un asesor senior que conoce tu negocio y trabaja junto "
                      "con el área contable, para que tu situación empresarial, legal e "
                      "impositiva estén siempre alineadas. Es la diferencia entre un "
                      "proveedor que solo constituye tu empresa y un socio que te ayuda a "
                      "llevarla adelante."),
            "included": [
                "Derecho societario",
                "Derecho laboral",
                "Redacción y revisión de contratos",
                "Temas de socios y directorio",
                "Consultas empresariales y legales continuas",
                "Disponible como parte de un plan mensual",
            ],
            "who": ("Empresas que quieren un asesor empresarial y legal continuo, "
                    "no solo servicios puntuales."),
        },
    },
    "represent": {
        "en": {
            "title": "Legal Representative and Registered Office | SetUp",
            "desc": ("We provide the locally-resident legal representative and registered "
                     "office your Argentine company needs to stay compliant, with no local "
                     "staff required."),
            "h1": "Legal Representative and Registered Office in Argentina",
            "intro": ("Every company in Argentina needs a registered office where official "
                      "notices are served, and a foreign-owned company also needs a "
                      "locally-resident legal representative (required under Sections 123 "
                      "and 118 of the General Companies Law). For a business without its "
                      "own premises or local staff, meeting these requirements can be an "
                      "obstacle. We provide both: we act as, or appoint, your "
                      "locally-resident legal representative, and provide the registered "
                      "office and fiscal domicile, handling official notifications and "
                      "keeping your company in good standing before the companies registry "
                      "(IGJ) and the tax authority (ARCA)."),
            "included": [
                "Locally-resident legal representative",
                "Registered office and fiscal domicile in Buenos Aires (CABA)",
                "Handling of official notices",
                "Ongoing statutory compliance",
            ],
            "who": ("Companies, foreign or local, that need a compliant local presence "
                    "or an outsourced registered office and legal representative."),
        },
        "es": {
            "title": "Representación legal y domicilio fiscal | SetUp Argentina",
            "desc": ("Proveemos el representante legal residente y el domicilio fiscal que "
                     "tu empresa necesita para estar en regla, sin que necesites personal "
                     "local."),
            "h1": "Representación legal y domicilio fiscal",
            "intro": ("Toda empresa en Argentina necesita un domicilio donde se cursen las "
                      "notificaciones oficiales, y una empresa de capital extranjero además "
                      "necesita un representante legal residente (Art. 123 y 118 de la Ley "
                      "General de Sociedades). Para un negocio sin oficina propia ni personal "
                      "local, cumplir esto puede ser un obstáculo. Proveemos ambos: actuamos "
                      "como, o designamos, tu representante legal residente, y aportamos el "
                      "domicilio fiscal y la sede en CABA, gestionando las notificaciones y "
                      "manteniendo a tu empresa en regla ante la IGJ y ARCA."),
            "included": [
                "Representante legal residente",
                "Domicilio fiscal y sede social en CABA",
                "Gestión de notificaciones oficiales",
                "Cumplimiento societario continuo",
            ],
            "who": ("Empresas, extranjeras o locales, que necesitan una presencia local "
                    "en regla o un domicilio y representante legal tercerizados."),
        },
    },
    # OJO: este texto lo redactamos nosotros, porque el documento del cliente
    # solo mencionaba el registro de marcas al pasar. Antes de publicar tiene
    # que revisarlo Agustin, sobre todo lo que afirma sobre el tramite.
    "trademark": {
        "en": {
            "title": "Trademark Registration in Argentina | SetUp Argentina",
            "desc": ("Protect your brand in Argentina. Availability search, filing "
                     "before the trademark office (INPI) and follow-up through to "
                     "registration."),
            "h1": "Trademark Registration in Argentina",
            "intro": ("Your brand becomes legally yours when it is registered. In "
                      "Argentina the right over a trademark is acquired through "
                      "registration with the trademark office (INPI), which gives you "
                      "the exclusive right to use it in the classes you register and "
                      "the standing to act against anyone using it without your "
                      "permission. We handle the process end to end and remotely, from "
                      "the prior search to the follow-up of the file."),
            "included": [
                "Prior availability search, to know your real chances before spending",
                "Advice on which classes to register, according to what you actually sell",
                "Preparation and filing of the application before the trademark office",
                "Follow-up of the file and response to objections",
                "Handling of oppositions from third parties",
                "Reminder when the renewal falls due",
            ],
            "who": ("Companies and entrepreneurs that operate, or plan to operate, "
                    "under their own brand in Argentina."),
        },
        "es": {
            "title": "Registro de marcas en Argentina | SetUp Argentina",
            "desc": ("Protegé tu marca en Argentina. Búsqueda de antecedentes, "
                     "presentación ante el INPI y seguimiento del trámite hasta la "
                     "concesión."),
            "h1": "Registro de marcas en Argentina",
            "intro": ("Tu marca es legalmente tuya cuando está registrada. En Argentina "
                      "el derecho sobre una marca se adquiere con su registro ante el "
                      "INPI, que te da el uso exclusivo en las clases que registres y la "
                      "posibilidad de actuar contra quien la use sin tu permiso. "
                      "Gestionamos el trámite de punta a punta y de forma remota, desde "
                      "la búsqueda de antecedentes hasta el seguimiento del expediente."),
            "included": [
                "Búsqueda de antecedentes, para saber las chances reales antes de gastar",
                "Asesoramiento sobre en qué clases registrar, según lo que realmente vendés",
                "Preparación y presentación de la solicitud ante el INPI",
                "Seguimiento del expediente y respuesta a las vistas",
                "Gestión de oposiciones de terceros",
                "Aviso cuando corresponde renovar",
            ],
            "who": ("Empresas y emprendedores que operan, o van a operar, con marca "
                    "propia en Argentina."),
        },
    },
}

def _service_page(key, lang):
    c = SERVICES[key][lang]
    L = LABELS[lang]

    blocks = ['<p class="svc-intro">%s</p>' % c["intro"]]
    if c.get("structures"):
        blocks.append("<h2>%s</h2><p>%s</p>" % (L["h_structures"], c["structures"]))
    if c.get("foreign"):
        blocks.append("<h2>%s</h2><p>%s</p>" % (L["h_foreign"], c["foreign"]))
    items = "".join("<li>%s</li>" % i for i in c["included"])
    blocks.append("<h2>%s</h2><ul>%s</ul>" % (L["h_included"], items))
    blocks.append("<h2>%s</h2><p>%s</p>" % (L["h_who"], c["who"]))

    others = "\n".join(
        '        <a href="%s" class="related-card"><strong>%s</strong>'
        '<span>%s</span></a>' % (url(k, lang), SERVICE_NAMES[lang][k], SUMMARY[lang][k])
        for k in SERVICE_ORDER if k != key)

    body = f'''
<header class="page-hero">
  <div class="container">
    <span class="section-tag" data-animate="fadeInUp">{L["svc_tag"]}</span>
    <h1 data-animate="fadeInUp">{c["h1"]}</h1>
  </div>
</header>

<section class="svc-section">
  <div class="container">
    <div class="prose" data-animate="fadeInUp">
      {"".join(blocks)}
    </div>
    <a href="{url("contact", lang)}" class="btn-primary svc-cta" data-animate="fadeInUp">
      <span>{L["cta_btn"]}</span>{ARROW_SVG}</a>
  </div>
</section>

<section class="related-section">
  <div class="container">
    <h2 class="related-title">{L["crumb_services"]}</h2>
    <div class="related-grid">
{others}
    </div>
  </div>
</section>
'''
    schema = {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": c["h1"],
        "description": c["desc"],
        "serviceType": SERVICE_NAMES[lang][key].replace("&amp;", "and"),
        "url": SITE + url(key, lang),
        "areaServed": {"@type": "Country", "name": "Argentina"},
        "provider": {"@type": "ProfessionalService", "name": "SetUp Argentina",
                     "url": SITE},
        "audience": {"@type": "BusinessAudience", "description": c["who"]},
    }
    crumbs = [(LABELS[lang]["crumb_home"], url("home", lang)),
              (LABELS[lang]["crumb_services"], url("services", lang)),
              (SERVICE_NAMES[lang][key], None)]
    return render.page(key, lang, title=c["title"], description=c["desc"],
                       body=body + cta_band(lang, L["cta_text"], L["cta_btn"]),
                       schema=schema, crumbs=crumbs)


def _index_page(lang):
    L = LABELS[lang]
    cards = "\n".join(
        '''        <a href="%s" class="svc-card" data-animate="fadeInUp">
          <h3>%s</h3><p>%s</p><span class="svc-card-more">%s %s</span></a>'''
        % (url(k, lang), SERVICE_NAMES[lang][k], SUMMARY[lang][k],
           L["read_more"], ARROW_SVG)
        for k in SERVICE_ORDER)

    body = f'''
<header class="page-hero">
  <div class="container">
    <span class="section-tag" data-animate="fadeInUp">{L["index_tag"]}</span>
    <h1 data-animate="fadeInUp">{L["index_h1"]}</h1>
    <p class="page-lead" data-animate="fadeInUp">{L["index_lead"]}</p>
  </div>
</header>

<section class="svc-section">
  <div class="container">
    <div class="svc-grid">
{cards}
    </div>
    <p class="svc-note" data-animate="fadeInUp">{CHECK_SVG} {L["index_note"]}</p>
  </div>
</section>
'''
    schema = {
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "url": SITE + url("services", lang),
        "name": L["index_h1"],
        "inLanguage": "en" if lang == "en" else "es-AR",
        "hasPart": [{"@type": "Service",
                     "name": SERVICE_NAMES[lang][k].replace("&amp;", "and"),
                     "url": SITE + url(k, lang)} for k in SERVICE_ORDER],
    }
    return render.page("services", lang, title=L["index_title"],
                       description=L["index_desc"],
                       body=body + cta_band(lang, L["cta_text"], L["cta_btn"]),
                       schema=schema,
                       crumbs=[(L["crumb_home"], url("home", lang)),
                               (L["crumb_services"], None)])


def build():
    for lang in ("en", "es"):
        yield "services", lang, _index_page(lang)
        for key in SERVICE_ORDER:
            yield key, lang, _service_page(key, lang)
