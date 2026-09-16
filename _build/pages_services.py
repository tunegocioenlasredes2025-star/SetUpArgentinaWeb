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
        "resumen_h": "In short",
        "tabla_h": "The three vehicles compared",
        "cta_inline": "Not sure which structure fits? Ask us, the first consultation is free.",
        "cta_inline_btn": "Ask a question",
        "h_structures": "The structures",
        "h_clases": "One application per class",
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
        "resumen_h": "En resumen",
        "tabla_h": "Los tres vehículos, comparados",
        "cta_inline": "¿No sabés cuál te conviene? Preguntanos, la primera consulta es sin cargo.",
        "cta_inline_btn": "Hacer una consulta",
        "h_structures": "Las estructuras",
        "h_clases": "Una solicitud por clase",
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
        "formation": ("Legal advice and representation to incorporate an SRL, SAS or SA, "
                      "including the Article 123 or 118 filing for foreign company "
                      "shareholders."),
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
        "formation": ("Asesoramiento y representación legal para constituir una SRL, SAS "
                      "o SA, incluida la inscripción del Art. 123 o 118 para socios del exterior."),
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
            "desc": ("Legal and accounting advice to incorporate an SRL, SAS or SA in "
                     "Argentina, with registry filings signed by our attorney. Fully remote. "
                     "Free first consultation."),
            "h1": "Company Formation in Argentina",
            "intro": ("Company formation in Argentina is a legal process. Our attorney and "
                      "accounting team advise on the right structure, draft the bylaws, "
                      "file with the companies registry under the professional "
                      "pre-qualification opinion that IGJ regulations require, and complete "
                      "the post-incorporation tax and corporate steps as your legal "
                      "representatives. Fully remote."),
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
                        "shareholders need an Argentine tax ID. As your legal representatives, "
                        "we prepare and file the Article 123 or 118 registration. Documents "
                        "issued abroad must be notarized, apostilled and translated by a "
                        "sworn translator in Argentina. We review them before they are "
                        "issued so nothing has to be redone, and no shareholder needs to "
                        "travel."),
            "included": [
                "Advice on the right structure",
                "Drafting of bylaws",
                "Name reservation",
                "Official Gazette publication",
                ("Filing with the companies registry, with the professional "
                 "pre-qualification opinion required by IGJ regulations, signed by our "
                 "attorney"),
                ("Tax registration of the company and its foreign shareholders, completed "
                 "by our legal and accounting team as part of the engagement"),
                "Article 123 or 118 registration where applicable",
                "Digital corporate books",
                "Guidance to open a corporate bank account",
            ],
            "resumen": [
                'Three vehicles: SRL, SAS or SA. We advise which fits your case.',
                'Foreigners can own 100%, and we prepare and file the Article 123 or 118 registration.',
                'Fully remote: you never have to travel.',
                ('Includes legal advice, bylaws, professional filing with the registry, '
                 'post-incorporation tax and corporate compliance, and digital corporate books.'),
            ],
            "who": ("Local and international companies, investors and entrepreneurs, "
                    "from startups to established groups."),
            "credentials": ("Legal work on every engagement is performed by Leandro "
                            "Agustín Sofía, attorney admitted to the Buenos Aires Bar "
                            "(CPACF T° 141 F° 71), together with our accounting team."),
        },
        "es": {
            "title": "Constitución de sociedades: SRL, SAS y SA | SetUp",
            "desc": ("Asesoramiento legal y contable para constituir una SRL, SAS o SA en "
                     "Argentina, con la presentación firmada por nuestro abogado. Todo "
                     "online. Primera consulta sin cargo."),
            "h1": "Constitución de sociedades en Argentina",
            "intro": ("Constituir una sociedad en Argentina es un proceso jurídico. Nuestro "
                      "equipo de abogados y contadores te asesora sobre la estructura "
                      "adecuada, redacta el estatuto, presenta la inscripción ante el "
                      "Registro con el dictamen de precalificación profesional que exige la "
                      "normativa de IGJ y completa los pasos fiscales y societarios "
                      "posteriores como tus representantes legales. Todo en forma remota."),
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
                        "extranjeros necesitan identificador fiscal argentino. Como tus "
                        "representantes legales, preparamos y presentamos la inscripción "
                        "por el artículo 123 o 118. Los documentos emitidos en el exterior "
                        "deben estar certificados, apostillados y traducidos por traductor "
                        "público en Argentina. Los revisamos antes de su emisión para que "
                        "nada tenga que rehacerse, y ningún socio necesita viajar."),
            "included": [
                "Asesoramiento sobre la estructura",
                "Redacción del estatuto",
                "Reserva de nombre",
                "Publicación en el Boletín Oficial",
                ("Presentación ante el Registro de sociedades, con el dictamen de "
                 "precalificación profesional que exige la normativa de IGJ, firmado por "
                 "nuestro abogado"),
                ("Inscripción fiscal de la sociedad y de sus socios extranjeros, realizada "
                 "por nuestro equipo legal y contable como parte del servicio"),
                "Inscripción del Art. 123 o 118 cuando corresponde",
                "Libros societarios digitales",
                "Guía para abrir la cuenta bancaria",
            ],
            "resumen": [
                'Tres vehículos: SRL, SAS o SA. Te asesoramos cuál conviene en tu caso.',
                'Los extranjeros pueden ser dueños del 100%, y preparamos y presentamos la inscripción del Art. 123 o 118.',
                'Todo remoto: no tenés que viajar.',
                ('Incluye asesoramiento legal, estatuto, presentación profesional ante el '
                 'Registro, cumplimiento fiscal y societario posterior a la inscripción y '
                 'libros societarios digitales.'),
            ],
            "who": ("Empresas, inversores y emprendedores, locales e internacionales, "
                    "desde startups hasta grupos consolidados."),
            "credentials": ("El trabajo legal de cada encargo lo realiza Leandro Agustín "
                            "Sofía, abogado matriculado en el Colegio Público de la "
                            "Abogacía de la Capital Federal (CPACF T° 141 F° 71), junto "
                            "con nuestro equipo contable."),
        },
    },
    "accounting": {
        "en": {
            "title": "Monthly Accounting and Tax Filings in Argentina | SetUp",
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
            "resumen": [
                'Monthly VAT, Turnover Tax and Income Tax filings, on time.',
                'Financial statements and annual corporate compliance included.',
                'Payroll administration available as an add-on.',
                'One point of contact who knows your case.',
            ],
            "who": ("Companies operating in Argentina that want reliable ongoing "
                    "accounting and tax compliance."),
        },
        "es": {
            "title": "Contabilidad mensual e impuestos de tu empresa | SetUp",
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
            "resumen": [
                'IVA, Ingresos Brutos y Ganancias presentados en fecha, todos los meses.',
                'Estados contables y cumplimiento societario anual incluidos.',
                'Liquidación de sueldos disponible como adicional.',
                'Un solo contacto que conoce tu caso.',
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
                "Residence and work visas for foreign directors, shareholders and "
                "their families",
                "Available as part of a monthly plan",
            ],
            "resumen": [
                'An outsourced business and legal advisor, not one-off services.',
                'Company law, labor law, contracts and shareholder matters.',
                'Works alongside the accounting side, so nothing contradicts.',
                'Available as part of a monthly plan.',
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
                "Residencias y visas de trabajo para directores, socios extranjeros "
                "y sus familias",
                "Disponible como parte de un plan mensual",
            ],
            "resumen": [
                'Un asesor empresarial y legal externo, no servicios sueltos.',
                'Derecho societario, laboral, contratos y temas de socios.',
                'Trabaja junto al área contable, para que nada se contradiga.',
                'Disponible como parte de un plan mensual.',
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
            "resumen": [
                'Required by law for foreign-owned companies (Sections 123 and 118).',
                'We act as, or appoint, your locally-resident legal representative.',
                'Registered office and fiscal domicile in Buenos Aires (CABA).',
                'No local staff or premises needed on your side.',
            ],
            "who": ("Companies, foreign or local, that need a compliant local presence "
                    "or an outsourced registered office and legal representative."),
        },
        "es": {
            "title": "Representante legal y domicilio fiscal en CABA | SetUp",
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
            "resumen": [
                'Lo exige la ley para empresas de capital extranjero (Art. 123 y 118).',
                'Actuamos como, o designamos, tu representante legal residente.',
                'Domicilio fiscal y sede social en CABA.',
                'No necesitás personal ni oficina propia.',
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
            "title": "Register Your Trademark in Argentina (INPI) | SetUp",
            "desc": ("Protect your brand in Argentina. Availability search, filing "
                     "before the trademark office (INPI) and follow-up through to "
                     "registration."),
            "h1": "Trademark Registration in Argentina",
            "clases": ("Argentina does not allow multi-class filings: <strong>each "
                       "class you want to protect is a separate application</strong>, "
                       "with its own fee and its own file. That is why choosing the "
                       "classes matters. Registering more than you need multiplies the "
                       "cost; registering too few leaves gaps a competitor can use. We "
                       "advise on the smallest set of classes that actually covers what "
                       "you sell, and we file one application for each."),
            "intro": ("Your brand becomes legally yours when it is registered. In "
                      "Argentina the right over a trademark is acquired through "
                      "registration with the trademark office (INPI), which gives you "
                      "the exclusive right to use it in the classes you register and "
                      "the standing to act against anyone using it without your "
                      "permission. We handle the process end to end and remotely, from "
                      "the prior search to the follow-up of the file."),
            "included": [
                "Prior availability search, to know your real chances before spending",
                "Advice on which classes to register, and one application filed per class",
                "Preparation and filing of the application before the trademark office",
                "Follow-up of the file and response to objections",
                "Handling of oppositions from third parties",
                "Reminder when the renewal falls due",
            ],
            "resumen": [
                'In Argentina the right over a trademark comes from registering it.',
                'We run the prior search before you spend on a name you cannot use.',
   "Each class is a separate application: there is no multi-class filing in Argentina.",
                'We follow the file and handle objections and oppositions.',
            ],
            "who": ("Companies and entrepreneurs that operate, or plan to operate, "
                    "under their own brand in Argentina."),
        },
        "es": {
            "title": "Registrá tu marca ante el INPI | SetUp Argentina",
            "desc": ("Protegé tu marca en Argentina. Búsqueda de antecedentes, "
                     "presentación ante el INPI y seguimiento del trámite hasta la "
                     "concesión."),
            "h1": "Registro de marcas en Argentina",
            "clases": ("En Argentina no existe la solicitud multiclase: <strong>cada "
                       "clase que quieras proteger es una solicitud aparte</strong>, con "
                       "su propia tasa y su propio expediente. Por eso elegir bien las "
                       "clases importa. Registrar de más multiplica el costo; registrar "
                       "de menos te deja huecos que un competidor puede aprovechar. Te "
                       "asesoramos sobre el conjunto mínimo de clases que realmente "
                       "cubre lo que vendés, y presentamos una solicitud por cada una."),
            "intro": ("Tu marca es legalmente tuya cuando está registrada. En Argentina "
                      "el derecho sobre una marca se adquiere con su registro ante el "
                      "INPI, que te da el uso exclusivo en las clases que registres y la "
                      "posibilidad de actuar contra quien la use sin tu permiso. "
                      "Gestionamos el trámite de punta a punta y de forma remota, desde "
                      "la búsqueda de antecedentes hasta el seguimiento del expediente."),
            "included": [
                "Búsqueda de antecedentes, para saber las chances reales antes de gastar",
                "Asesoramiento sobre en qué clases registrar, y una solicitud presentada por clase",
                "Preparación y presentación de la solicitud ante el INPI",
                "Seguimiento del expediente y respuesta a las vistas",
                "Gestión de oposiciones de terceros",
                "Aviso cuando corresponde renovar",
            ],
            "resumen": [
                'En Argentina el derecho sobre la marca nace con el registro.',
                'Hacemos la búsqueda de antecedentes antes de que gastes en un nombre que no podés usar.',
   "Cada clase es una solicitud aparte: en Argentina no existe la multiclase.",
                'Seguimos el expediente y gestionamos vistas y oposiciones.',
            ],
            "who": ("Empresas y emprendedores que operan, o van a operar, con marca "
                    "propia en Argentina."),
        },
    },
}

# Tabla comparativa. Es el tipo de contenido que Google levanta como
# fragmento destacado, y responde de un vistazo la pregunta que mas
# hacen: cual de las tres me conviene.
TABLA_ESTRUCTURAS = {
    "en": {
        "cols": ["Vehicle", "Partners", "Minimum capital", "Typically used for"],
        "rows": [
            ["SRL", "2 to 50", "No fixed minimum",
             "Operating businesses. The most solid structure."],
            ["SAS", "From 1", "Two minimum wages (around USD 500)",
             "Setting up fast, or with a single shareholder."],
            ["SA", "From 2", "Around USD 20,000",
             "Larger operations, or issuing shares."],
        ],
    },
    "es": {
        "cols": ["Vehículo", "Socios", "Capital mínimo", "Cuándo se usa"],
        "rows": [
            ["SRL", "De 2 a 50", "Sin mínimo fijo",
             "Empresas operativas. La estructura más sólida."],
            ["SAS", "Desde 1", "Dos salarios mínimos (unos USD 500)",
             "Constituir rápido, o con un solo accionista."],
            ["SA", "Desde 2", "Cerca de USD 20.000",
             "Operaciones más grandes, o emitir acciones."],
        ],
    },
}


def _tabla(lang):
    t = TABLA_ESTRUCTURAS[lang]
    cab = "".join("<th>%s</th>" % c for c in t["cols"])
    filas = "".join(
        "<tr>" + "".join("<td>%s</td>" % celda for celda in fila) + "</tr>"
        for fila in t["rows"])
    return ('<div class="tabla-wrap"><table class="tabla-comparativa">'
            '<thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>'
            % (cab, filas))


def _service_page(key, lang):
    c = SERVICES[key][lang]
    L = LABELS[lang]

    blocks = ['<p class="svc-intro">%s</p>' % c["intro"]]

    # Resumen arriba de todo: el lector sabe en 10 segundos si esto es
    # para el, y Google tiene de donde sacar una respuesta directa.
    if c.get("resumen"):
        items = "".join("<li>%s</li>" % b for b in c["resumen"])
        blocks.append('<aside class="tldr"><h2>%s</h2><ul>%s</ul></aside>'
                      % (L["resumen_h"], items))

    # Llamada a la accion temprana, no solo al final: el que ya se
    # convencio leyendo el primer parrafo no tiene que buscar el boton.
    blocks.append('<p class="cta-inline">%s <a href="%s">%s %s</a></p>'
                  % (L["cta_inline"], url("contact", lang),
                     L["cta_inline_btn"], "&rarr;"))

    if c.get("clases"):
        blocks.append("<h2>%s</h2><p>%s</p>" % (L["h_clases"], c["clases"]))

    if c.get("structures"):
        blocks.append("<h2>%s</h2><p>%s</p>" % (L["h_structures"], c["structures"]))
        if key == "formation":
            blocks.append("<h3>%s</h3>%s" % (L["tabla_h"], _tabla(lang)))
    if c.get("foreign"):
        blocks.append("<h2>%s</h2><p>%s</p>" % (L["h_foreign"], c["foreign"]))
    items = "".join("<li>%s</li>" % i for i in c["included"])
    blocks.append("<h2>%s</h2><ul>%s</ul>" % (L["h_included"], items))
    blocks.append("<h2>%s</h2><p>%s</p>" % (L["h_who"], c["who"]))

    others = "\n".join(
        '        <a href="%s" class="related-card"><h3>%s</h3>'
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
    # Credenciales al final, antes del footer: quien firma el trabajo legal.
    creds = ""
    if c.get("credentials"):
        creds = ('\n<section class="svc-section svc-credentials"><div class="container">'
                 '<p class="prose">%s</p></div></section>\n' % c["credentials"])
    return render.page(key, lang, title=c["title"], description=c["desc"],
                       body=body + cta_band(lang, L["cta_text"], L["cta_btn"]) + creds,
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
