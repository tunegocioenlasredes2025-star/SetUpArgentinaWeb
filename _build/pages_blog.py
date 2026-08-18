# -*- coding: utf-8 -*-
"""Blog: listado + plantilla de articulo, en los dos idiomas.

Hoy no hay notas reales. Se generan dos notas de ejemplo, marcadas como
tales, para que se vea como queda el listado y como queda un articulo por
dentro. Cuando el panel de carga entre en funcionamiento, POSTS se llena
desde la base de datos y DEMO pasa a False.

Las notas de ejemplo salen con noindex para que Google no las levante.
"""

import render
from chrome import ARROW_SVG, cta_band
from site_cfg import SITE, url

DEMO = True

LABELS = {
    "en": {
        "title": "Blog | Doing Business in Argentina — SetUp Argentina",
        "desc": ("Practical articles on company formation, tax and compliance for "
                 "companies operating in Argentina, written by our team."),
        "tag": "Blog",
        "h1": "Doing Business in Argentina",
        "lead": ("Practical notes on company formation, tax and compliance, written "
                 "by the same people who handle the paperwork."),
        "crumbs": [("Home", "/"), ("Blog", None)],
        "empty_h": "The first articles are on their way",
        "empty_p": ("We are preparing the first notes. In the meantime, if you have a "
                    "question about setting up or running a company in Argentina, "
                    "ask us directly, the first consultation is free."),
        "read": "Read article",
        "min": "min read",
        "demo_badge": "Sample",
        "demo_note": ("This is a sample article, shown so you can see how a published "
                      "note will look. It is not indexed by search engines."),
        "back": "Back to the blog",
        "cta_text": "Have a question we have not covered yet? Just ask.",
        "cta_btn": "Book a Free Consultation",
    },
    "es": {
        "title": "Blog | Hacer negocios en Argentina — SetUp Argentina",
        "desc": ("Artículos prácticos sobre constitución de sociedades, impuestos y "
                 "cumplimiento para empresas que operan en Argentina."),
        "tag": "Blog",
        "h1": "Hacer negocios en Argentina",
        "lead": ("Notas prácticas sobre constitución, impuestos y cumplimiento, "
                 "escritas por los mismos que hacen los trámites."),
        "crumbs": [("Inicio", "/es/"), ("Blog", None)],
        "empty_h": "Las primeras notas están en camino",
        "empty_p": ("Estamos preparando los primeros artículos. Mientras tanto, si "
                    "tenés una duda sobre constituir u operar una empresa en Argentina, "
                    "escribinos: la primera consulta es sin cargo."),
        "read": "Leer nota",
        "min": "min de lectura",
        "demo_badge": "Ejemplo",
        "demo_note": ("Esta es una nota de ejemplo, puesta para que se vea cómo va a "
                      "quedar un artículo publicado. No la indexan los buscadores."),
        "back": "Volver al blog",
        "cta_text": "¿Tenés una duda que todavía no cubrimos? Escribinos.",
        "cta_btn": "Agendá una consulta sin cargo",
    },
}

# Notas de ejemplo. Cuando entre el panel, esto viene de la base de datos.
DEMO_POSTS = [
    {
        "slug_en": "srl-sas-or-sa-which-structure",
        "slug_es": "srl-sas-o-sa-que-estructura-conviene",
        "date": "2026-08-18",
        "en": {
            "title": "SRL, SAS or SA: which structure fits your business",
            "excerpt": ("The three vehicles compared on what actually matters: how many "
                        "partners, how fast, how much capital and what happens if you "
                        "want to bring in investors later."),
            "read": 6,
            "body": [
                ("h2", "The short answer"),
                ("p", "Most operating businesses end up in an SRL. Most founders in a "
                      "hurry end up in an SAS. The SA is for larger operations or for "
                      "companies that need to issue shares."),
                ("h2", "How many partners"),
                ("p", "The SRL takes between 2 and 50 partners and is the most solid "
                      "structure. The SAS admits a single shareholder, which matters if "
                      "you are setting up alone."),
                ("h2", "Capital"),
                ("p", "The SRL has no fixed minimum. The SAS requires the equivalent of "
                      "two minimum wages, currently around USD 500. The SA sits higher, "
                      "currently around USD 20,000."),
            ],
        },
        "es": {
            "title": "SRL, SAS o SA: qué estructura le conviene a tu negocio",
            "excerpt": ("Los tres vehículos comparados por lo que realmente importa: "
                        "cuántos socios, qué tan rápido, cuánto capital y qué pasa si "
                        "más adelante querés sumar inversores."),
            "read": 6,
            "body": [
                ("h2", "La respuesta corta"),
                ("p", "La mayoría de las empresas operativas termina en una SRL. Los "
                      "que tienen apuro terminan en una SAS. La SA es para operaciones "
                      "más grandes o para empresas que necesitan emitir acciones."),
                ("h2", "Cuántos socios"),
                ("p", "La SRL admite de 2 a 50 socios y es la estructura más sólida. La "
                      "SAS admite un solo accionista, algo que importa si estás "
                      "constituyendo en soledad."),
                ("h2", "Capital"),
                ("p", "La SRL no tiene mínimo fijo. La SAS requiere el equivalente a dos "
                      "salarios mínimos, hoy unos USD 500. La SA está más arriba, hoy "
                      "cerca de USD 20.000."),
            ],
        },
    },
    {
        "slug_en": "can-a-foreign-company-own-an-argentine-company",
        "slug_es": "puede-una-sociedad-extranjera-ser-socia",
        "date": "2026-08-12",
        "en": {
            "title": "Can a foreign company own an Argentine company?",
            "excerpt": ("Yes, and here is the part nobody explains: the Article 123 "
                        "registration that has to happen first, and how much time it "
                        "adds to your timeline."),
            "read": 5,
            "body": [
                ("h2", "The rule"),
                ("p", "Foreign individuals and companies can own 100% of an Argentine "
                      "company, with the same rights as a local shareholder and no "
                      "limits on repatriating profits."),
                ("h2", "What has to happen first"),
                ("p", "If the shareholder is a foreign company, it must register its "
                      "documentation with the companies registry under Section 123 of "
                      "the General Companies Law before it can hold shares."),
            ],
        },
        "es": {
            "title": "¿Puede una sociedad extranjera ser socia de una empresa argentina?",
            "excerpt": ("Sí, y acá va la parte que nadie explica: la inscripción por el "
                        "Art. 123 que tiene que pasar antes, y cuánto tiempo le suma "
                        "a tu plazo."),
            "read": 5,
            "body": [
                ("h2", "La regla"),
                ("p", "Las personas y sociedades extranjeras pueden ser dueñas del 100% "
                      "de una empresa argentina, con los mismos derechos que un socio "
                      "local y sin límites para repatriar utilidades."),
                ("h2", "Qué tiene que pasar antes"),
                ("p", "Si el socio es una sociedad del exterior, primero debe inscribir "
                      "su documentación ante la IGJ bajo el Art. 123 de la Ley General "
                      "de Sociedades para poder participar."),
            ],
        },
    },
]


def _post_paths(post):
    return ("/blog/%s/" % post["slug_en"], "/es/blog/%s/" % post["slug_es"])


def _post_url(post, lang):
    return _post_paths(post)[0 if lang == "en" else 1]


def _fmt_date(iso, lang):
    y, m, d = iso.split("-")
    months_en = ["January", "February", "March", "April", "May", "June", "July",
                 "August", "September", "October", "November", "December"]
    months_es = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
                 "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    if lang == "en":
        return "%s %d, %s" % (months_en[int(m) - 1], int(d), y)
    return "%d de %s de %s" % (int(d), months_es[int(m) - 1], y)


def _listing(lang):
    L = LABELS[lang]
    posts = DEMO_POSTS if DEMO else []

    if posts:
        cards = "\n".join(
            '''      <a href="{href}" class="post-card">
        <div class="post-meta"><span class="post-badge">{badge}</span>
          <time datetime="{iso}">{date}</time><span>·</span><span>{read} {min}</span></div>
        <h2>{title}</h2><p>{excerpt}</p>
        <span class="post-more">{read_lbl} {arrow}</span></a>'''.format(
                href=_post_url(p, lang), badge=L["demo_badge"], iso=p["date"],
                date=_fmt_date(p["date"], lang), read=p[lang]["read"], min=L["min"],
                title=p[lang]["title"], excerpt=p[lang]["excerpt"],
                read_lbl=L["read"], arrow=ARROW_SVG)
            for p in posts)
        inner = '    <div class="post-grid">\n%s\n    </div>' % cards
    else:
        inner = ('    <div class="blog-empty"><h2>%s</h2><p>%s</p>'
                 '<a href="%s" class="btn-primary"><span>%s</span>%s</a></div>'
                 % (L["empty_h"], L["empty_p"], url("contact", lang),
                    L["cta_btn"], ARROW_SVG))

    body = f'''
<header class="page-hero">
  <div class="container">
    <span class="section-tag" data-animate="fadeInUp">{L["tag"]}</span>
    <h1 data-animate="fadeInUp">{L["h1"]}</h1>
    <p class="page-lead" data-animate="fadeInUp">{L["lead"]}</p>
  </div>
</header>

<section class="blog-section">
  <div class="container">
{inner}
  </div>
</section>
'''
    schema = {
        "@context": "https://schema.org",
        "@type": "Blog",
        "url": SITE + url("blog", lang),
        "name": L["h1"],
        "description": L["desc"],
        "inLanguage": "en" if lang == "en" else "es-AR",
    }
    return render.page("blog", lang, title=L["title"], description=L["desc"],
                       body=body + cta_band(lang, L["cta_text"], L["cta_btn"]),
                       schema=schema, crumbs=L["crumbs"])


def _article(post, lang):
    L = LABELS[lang]
    c = post[lang]
    paths = _post_paths(post)
    content = "".join(
        ("<h2>%s</h2>" % text) if tag == "h2" else ("<p>%s</p>" % text)
        for tag, text in c["body"])

    demo_banner = ('<p class="demo-note">%s</p>' % L["demo_note"]) if DEMO else ""

    body = f'''
<article class="post">
  <header class="page-hero">
    <div class="container">
      <span class="section-tag">{L["demo_badge"] if DEMO else L["tag"]}</span>
      <h1>{c["title"]}</h1>
      <div class="post-meta">
        <time datetime="{post["date"]}">{_fmt_date(post["date"], lang)}</time>
        <span>·</span><span>{c["read"]} {L["min"]}</span>
      </div>
    </div>
  </header>
  <div class="container post-body">
    {demo_banner}
    <div class="prose">{content}</div>
    <a href="{url("blog", lang)}" class="post-back">{L["back"]}</a>
  </div>
</article>
'''
    schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": c["title"],
        "description": c["excerpt"],
        "datePublished": post["date"],
        "dateModified": post["date"],
        "inLanguage": "en" if lang == "en" else "es-AR",
        "author": {"@type": "Organization", "name": "SetUp Argentina", "url": SITE},
        "publisher": {"@type": "Organization", "name": "SetUp Argentina", "url": SITE},
        "mainEntityOfPage": SITE + paths[0 if lang == "en" else 1],
    }
    crumbs = [(L["crumbs"][0][0], url("home", lang)),
              ("Blog", url("blog", lang)), (c["title"], None)]
    return render.page(
        "blog", lang, title="%s | SetUp Argentina" % c["title"],
        description=c["excerpt"],
        body=body + cta_band(lang, L["cta_text"], L["cta_btn"]),
        schema=schema, crumbs=crumbs, paths=paths,
        # Las notas de ejemplo no deben entrar al indice de Google.
        robots="noindex, follow" if DEMO else "index, follow")


def build():
    for lang in ("en", "es"):
        yield "blog", lang, _listing(lang)


def build_articles():
    """Devuelve (ruta, html) porque las notas no estan en el mapa fijo."""
    out = []
    for post in (DEMO_POSTS if DEMO else []):
        for lang in ("en", "es"):
            path = _post_url(post, lang).strip("/") + "/index.html"
            out.append((path, _article(post, lang)))
    return out
