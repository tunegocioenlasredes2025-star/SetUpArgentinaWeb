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
from posts_source import fetch_posts
from site_cfg import SITE, url

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
        "share": "Share this article",
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
        "share": "Compartir esta nota",
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




def _demo_normalizadas():
    """Las notas de ejemplo, en el mismo formato que las que vienen de la base."""
    salida = []
    for p in DEMO_POSTS:
        nota = {"slug_en": p["slug_en"], "slug_es": p["slug_es"],
                "date": p["date"], "cover": None}
        for lang in ("en", "es"):
            c = p[lang]
            html = "".join(
                ("<h2>%s</h2>" % t) if tag == "h2" else ("<p>%s</p>" % t)
                for tag, t in c["body"])
            nota[lang] = {"title": c["title"], "excerpt": c["excerpt"],
                          "html": html, "read": c["read"], "cover_alt": ""}
        salida.append(nota)
    return salida


# Las notas reales mandan. Si todavia no hay ninguna publicada, se muestran
# las de ejemplo para que se vea como queda el blog; en cuanto Agustin
# publique la primera, las de ejemplo desaparecen solas.
POSTS = fetch_posts()
DEMO = not POSTS
if DEMO:
    POSTS = _demo_normalizadas()


def _post_paths(post):
    return ("/blog/%s/" % post["slug_en"] if post["slug_en"] else None,
            "/es/blog/%s/" % post["slug_es"] if post["slug_es"] else None)


def _post_url(post, lang):
    return _post_paths(post)[0 if lang == "en" else 1]


def _fmt_date(iso, lang):
    if not iso:
        return ""
    y, m, d = iso.split("-")
    meses_en = ["January", "February", "March", "April", "May", "June", "July",
                "August", "September", "October", "November", "December"]
    meses_es = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
                "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    if lang == "en":
        return "%s %d, %s" % (meses_en[int(m) - 1], int(d), y)
    return "%d de %s de %s" % (int(d), meses_es[int(m) - 1], y)


def _en_idioma(lang):
    """Notas que existen en ese idioma. Una nota que solo esta en ingles no
    aparece en el listado en espanol: se oculta en vez de dejar un hueco."""
    return [p for p in POSTS if p.get(lang) and _post_url(p, lang)]


def _listing(lang):
    L = LABELS[lang]
    posts = _en_idioma(lang)

    if posts:
        tarjetas = []
        for p in posts:
            c = p[lang]
            badge = ('<span class="post-badge">%s</span>' % L["demo_badge"]) if DEMO else ""
            tarjetas.append(
                '      <a href="%s" class="post-card">\n'
                '        <div class="post-meta">%s<time datetime="%s">%s</time>'
                '<span>·</span><span>%s %s</span></div>\n'
                '        <h2>%s</h2><p>%s</p>\n'
                '        <span class="post-more">%s %s</span></a>'
                % (_post_url(p, lang), badge, p["date"], _fmt_date(p["date"], lang),
                   c["read"], L["min"], c["title"], c["excerpt"], L["read"], ARROW_SVG))
        inner = '    <div class="post-grid">\n%s\n    </div>' % "\n".join(tarjetas)
    else:
        inner = ('    <div class="blog-empty"><h2>%s</h2><p>%s</p>'
                 '<a href="%s" class="btn-primary"><span>%s</span>%s</a></div>'
                 % (L["empty_h"], L["empty_p"], url("contact", lang),
                    L["cta_btn"], ARROW_SVG))

    body = '''
<header class="page-hero">
  <div class="container">
    <span class="section-tag" data-animate="fadeInUp">{tag}</span>
    <h1 data-animate="fadeInUp">{h1}</h1>
    <p class="page-lead" data-animate="fadeInUp">{lead}</p>
  </div>
</header>

<section class="blog-section">
  <div class="container">
{inner}
  </div>
</section>
'''.format(tag=L["tag"], h1=L["h1"], lead=L["lead"], inner=inner)

    schema = {
        "@context": "https://schema.org",
        "@type": "Blog",
        "url": SITE + url("blog", lang),
        "name": L["h1"],
        "description": L["desc"],
        "inLanguage": "en" if lang == "en" else "es-AR",
        "blogPost": [{"@type": "BlogPosting", "headline": p[lang]["title"],
                      "url": SITE + _post_url(p, lang), "datePublished": p["date"]}
                     for p in posts],
    }
    return render.page("blog", lang, title=L["title"], description=L["desc"],
                       body=body + cta_band(lang, L["cta_text"], L["cta_btn"]),
                       schema=schema, crumbs=L["crumbs"])


def _compartir(post, lang, L):
    """Botones de compartir. Son links normales, no widgets: no cargan
    scripts de terceros ni ralentizan la pagina."""
    from urllib.parse import quote
    url_abs = SITE + _post_url(post, lang)
    titulo = post[lang]["title"]
    wa = "https://wa.me/?text=" + quote(titulo + " " + url_abs)
    li = "https://www.linkedin.com/sharing/share-offsite/?url=" + quote(url_abs)
    x = ("https://twitter.com/intent/tweet?text=" + quote(titulo)
         + "&url=" + quote(url_abs))
    mail = ("mailto:?subject=" + quote(titulo) + "&body=" + quote(url_abs))
    return ('<div class="compartir"><span>%s</span>'
            '<a href="%s" target="_blank" rel="noopener">WhatsApp</a>'
            '<a href="%s" target="_blank" rel="noopener">LinkedIn</a>'
            '<a href="%s" target="_blank" rel="noopener">X</a>'
            '<a href="%s">Email</a></div>'
            % (L["share"], wa, li, x, mail))


def _article(post, lang):
    L = LABELS[lang]
    c = post[lang]
    en_path, es_path = _post_paths(post)
    # Si la nota existe en un solo idioma, el hreflang apunta a la unica
    # version que hay, en vez de prometer una traduccion que no existe.
    paths = (en_path or es_path, es_path or en_path)

    portada = ""
    if post.get("cover"):
        portada = ('<img class="post-cover" src="%s" alt="%s" loading="lazy">'
                   % (post["cover"], c.get("cover_alt", "")))
    aviso = ('<p class="demo-note">%s</p>' % L["demo_note"]) if DEMO else ""

    body = '''
<article class="post">
  <header class="page-hero">
    <div class="container">
      <span class="section-tag">{badge}</span>
      <h1>{titulo}</h1>
      <div class="post-meta">
        <time datetime="{iso}">{fecha}</time>
        <span>·</span><span>{read} {min}</span>
      </div>
    </div>
  </header>
  <div class="container post-body">
    {portada}
    {aviso}
    <div class="prose">{contenido}</div>
    {compartir}
    <a href="{blog}" class="post-back">{volver}</a>
  </div>
</article>
'''.format(badge=L["demo_badge"] if DEMO else L["tag"], titulo=c["title"],
           iso=post["date"], fecha=_fmt_date(post["date"], lang),
           read=c["read"], min=L["min"], portada=portada, aviso=aviso,
           contenido=c["html"], blog=url("blog", lang), volver=L["back"],
           compartir=_compartir(post, lang, L))

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
        "mainEntityOfPage": SITE + _post_url(post, lang),
    }
    if post.get("cover"):
        schema["image"] = post["cover"]

    crumbs = [(L["crumbs"][0][0], url("home", lang)),
              ("Blog", url("blog", lang)), (c["title"], None)]
    return render.page(
        "blog", lang, title="%s | SetUp Argentina" % c["title"],
        description=c["excerpt"],
        body=body + cta_band(lang, L["cta_text"], L["cta_btn"]),
        schema=schema, crumbs=crumbs, paths=paths,
        robots="noindex, follow" if DEMO else "index, follow")


def build():
    for lang in ("en", "es"):
        yield "blog", lang, _listing(lang)


def build_articles():
    """(ruta, html) por nota: no estan en el mapa fijo de paginas."""
    salida = []
    for post in POSTS:
        for lang in ("en", "es"):
            if not post.get(lang) or not _post_url(post, lang):
                continue
            ruta = _post_url(post, lang).strip("/") + "/index.html"
            salida.append((ruta, _article(post, lang)))
    return salida
