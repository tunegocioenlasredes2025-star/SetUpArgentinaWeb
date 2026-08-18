# -*- coding: utf-8 -*-
"""Pagina de contacto en los dos idiomas."""

import chrome
import render
from chrome import ARROW_SVG
from site_cfg import SITE, EMAIL, WA_NUMBER, WA_DISPLAY, CITY, url

MAIL_SVG = ('<svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden="true">'
            '<path d="M4 4H20C21.1 4 22 4.9 22 6V18C22 19.1 21.1 20 20 20H4C2.9 20 2 19.1 '
            '2 18V6C2 4.9 2.9 4 4 4Z" stroke="currentColor" stroke-width="1.5"/>'
            '<polyline points="22,6 12,13 2,6" stroke="currentColor" stroke-width="1.5" '
            'stroke-linecap="round"/></svg>')

PIN_SVG = ('<svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden="true">'
           '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z" stroke="currentColor" '
           'stroke-width="1.5"/><circle cx="12" cy="10" r="3" stroke="currentColor" '
           'stroke-width="1.5"/></svg>')

CLOCK_SVG = ('<svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden="true">'
             '<circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.5"/>'
             '<path d="M12 7v5l3 2" stroke="currentColor" stroke-width="1.5" '
             'stroke-linecap="round"/></svg>')

WA_ICON = ('<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" '
           'aria-hidden="true"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 '
           '3.45 1.32 4.95L2 22l5.25-1.38a9.9 9.9 0 004.79 1.22h.01c5.46 0 9.91-4.45 '
           '9.91-9.91C21.96 6.45 17.5 2 12.04 2zm0 18.15h-.01a8.2 8.2 0 01-4.19-1.15l-.3-.18'
           '-3.12.82.83-3.04-.2-.31a8.18 8.18 0 01-1.26-4.38c0-4.54 3.7-8.23 8.25-8.23a8.2 '
           '8.2 0 018.24 8.24c0 4.54-3.7 8.23-8.24 8.23z"/></svg>')

COPY = {
    "en": {
        "title": "Contact SetUp Argentina | Free Initial Consultation",
        "desc": ("Tell us about your project and we will reply within 24 business hours. "
                 "The initial consultation is free and handled directly by a licensed "
                 "professional in Buenos Aires."),
        "crumbs": [("Home", "/"), ("Contact", None)],
        "tag": "Contact",
        "h1": "Let's Talk About Your Business",
        "lead": ("Tell us about your project and we'll reply within 24 business hours. "
                 "The initial consultation is free."),
        "details_h": "Get in touch",
        "l_email": "Email",
        "l_wa": "WhatsApp",
        "l_loc": "Location",
        "l_time": "Response time",
        "v_time": "Within 24 business hours",
        "note": ("All inquiries are handled directly by a licensed professional. "
                 "Your information is never shared with third parties."),
        "form_h": "Book a free consultation",
        "f_name": "Full Name", "f_company": "Company Name",
        "f_email": "Email Address", "f_phone": "Phone / WhatsApp",
        "f_country": "Country", "f_service": "Service Needed",
        "f_message": "Tell Us About Your Project",
        "ph_name": "John Smith", "ph_company": "Acme Corp",
        "ph_email": "john@company.com", "ph_phone": "+1 555 000 0000",
        "ph_country": "United States",
        "ph_message": ("Briefly describe your situation and what you're looking to "
                       "achieve in Argentina..."),
        "opt_service": "Select a service",
        "services": ["Company Formation",
                     "Accounting, Tax and Compliance",
                     "Business and Legal Advisory",
                     "Legal Representation and Registered Office",
                     "Trademark registration",
                     "Visas for company directors",
                     "Not sure yet, I need advice"],
        "button": "Book a Free Consultation",
        "privacy": "We respond within 24 business hours. Your information is never shared.",
        "required": "required",
        "or_wa": "Prefer WhatsApp? Write to us directly",
    },
    "es": {
        "title": "Contacto | SetUp Argentina — Consulta inicial sin cargo",
        "desc": ("Contanos sobre tu proyecto y te respondemos dentro de las 24 horas "
                 "hábiles. La primera consulta es sin cargo y la atiende directamente "
                 "un profesional matriculado."),
        "crumbs": [("Inicio", "/es/"), ("Contacto", None)],
        "tag": "Contacto",
        "h1": "Hablemos de tu negocio",
        "lead": ("Contanos sobre tu proyecto y te respondemos dentro de las 24 horas "
                 "hábiles. La primera consulta es sin cargo."),
        "details_h": "Datos de contacto",
        "l_email": "Email",
        "l_wa": "WhatsApp",
        "l_loc": "Ubicación",
        "l_time": "Tiempo de respuesta",
        "v_time": "Dentro de las 24 horas hábiles",
        "note": ("Cada consulta la atiende directamente un profesional matriculado. "
                 "Tu información nunca se comparte con terceros."),
        "form_h": "Agendá tu consulta sin cargo",
        "f_name": "Nombre y apellido", "f_company": "Empresa",
        "f_email": "Email", "f_phone": "Teléfono / WhatsApp",
        "f_country": "País", "f_service": "Servicio",
        "f_message": "Mensaje",
        "ph_name": "Juan Pérez", "ph_company": "Acme S.R.L.",
        "ph_email": "juan@empresa.com", "ph_phone": "+54 11 0000 0000",
        "ph_country": "Argentina",
        "ph_message": "Contanos brevemente tu situación y qué necesitás resolver...",
        "opt_service": "Elegí un servicio",
        "services": ["Constitución de sociedades",
                     "Contabilidad, impuestos y cumplimiento",
                     "Asesoramiento empresarial y legal",
                     "Representación legal y domicilio fiscal",
                     "Registro de marcas",
                     "Visas para directores",
                     "Todavía no sé, necesito asesoramiento"],
        "button": "Agendá una consulta sin cargo",
        "privacy": "Respondemos dentro de las 24 horas hábiles. Tus datos no se comparten.",
        "required": "obligatorio",
        "or_wa": "¿Preferís WhatsApp? Escribinos directo",
    },
}


def _detail(icon, label, value, href=None):
    inner = ('<a href="%s" target="_blank" rel="noopener">%s</a>' % (href, value)
             if href else "<span>%s</span>" % value)
    return ('<div class="contact-detail">%s<div><div class="cd-label">%s</div>%s</div></div>'
            % (icon, label, inner))


def _text(fid, label, placeholder, kind="text", required=False):
    star = " *" if required else ""
    req = " required" if required else ""
    return ('<div class="form-group"><label for="%s">%s%s</label>'
            '<input type="%s" id="%s" name="%s" placeholder="%s"%s></div>'
            % (fid, label, star, kind, fid, fid, placeholder, req))


def _select(fid, label, prompt, options):
    opts = "".join("<option>%s</option>" % o for o in options)
    return ('<div class="form-group"><label for="%s">%s</label>'
            '<select id="%s" name="%s"><option value="" disabled selected>%s</option>'
            '%s</select></div>' % (fid, label, fid, fid, prompt, opts))


def _form(lang):
    c = COPY[lang]
    rows = [
        [_text("name", c["f_name"], c["ph_name"], required=True),
         _text("company", c["f_company"], c["ph_company"])],
        [_text("email", c["f_email"], c["ph_email"], kind="email", required=True),
         _text("phone", c["f_phone"], c["ph_phone"], kind="tel")],
    ]
    service = _select("service", c["f_service"], c["opt_service"], c["services"])
    if lang == "en":
        # En ingles preguntamos el pais: es lo que despues permite separar
        # las consultas del exterior por mercado.
        rows.append([_text("country", c["f_country"], c["ph_country"]), service])
    else:
        rows.append([service])
    grid = "\n          ".join(
        '<div class="form-row">%s</div>' % "".join(r) for r in rows)

    return f'''<form class="contact-form" id="contactForm" novalidate data-lang="{lang}">
          {grid}
          <div class="form-group"><label for="message">{c["f_message"]}</label>
            <textarea id="message" name="message" rows="4" placeholder="{c["ph_message"]}"></textarea></div>
          <button type="submit" class="btn-primary btn-form-submit">
            <span class="btn-text">{c["button"]}</span>{ARROW_SVG}</button>
          <p class="form-privacy">{c["privacy"]}</p>
        </form>'''


def build():
    for lang in ("en", "es"):
        c = COPY[lang]
        details = "".join([
            _detail(MAIL_SVG, c["l_email"], EMAIL, "mailto:" + EMAIL),
            _detail(WA_ICON, c["l_wa"], WA_DISPLAY, "https://wa.me/" + WA_NUMBER),
            _detail(PIN_SVG, c["l_loc"], CITY),
            _detail(CLOCK_SVG, c["l_time"], c["v_time"]),
        ])
        body = f'''
<header class="page-hero">
  <div class="container">
    <span class="section-tag" data-animate="fadeInUp">{c["tag"]}</span>
    <h1 data-animate="fadeInUp">{c["h1"]}</h1>
    <p class="page-lead" data-animate="fadeInUp">{c["lead"]}</p>
  </div>
</header>

<section class="section-contact">
  <div class="container contact-layout">
    <div class="contact-info" data-animate="fadeInLeft">
      <h2 class="contact-title">{c["details_h"]}</h2>
      {details}
      <p class="contact-note">{c["note"]}</p>
      <a class="contact-wa-link" href="https://wa.me/{WA_NUMBER}" target="_blank" rel="noopener">
        {c["or_wa"]} {ARROW_SVG}</a>
    </div>
    <div class="contact-form-wrap" data-animate="fadeInRight">
      <h2 class="contact-form-title">{c["form_h"]}</h2>
      {_form(lang)}
    </div>
  </div>
</section>
'''
        schema = {
            "@context": "https://schema.org",
            "@type": "ContactPage",
            "url": SITE + url("contact", lang),
            "name": c["h1"],
            "inLanguage": "en" if lang == "en" else "es-AR",
            "mainEntity": {
                "@type": "ProfessionalService",
                "name": "SetUp Argentina",
                "email": EMAIL,
                "telephone": "+" + WA_NUMBER,
                "address": {"@type": "PostalAddress", "addressLocality": "Buenos Aires",
                            "addressRegion": "CABA", "addressCountry": "AR"},
            },
        }

        yield "contact", lang, render.page(
            "contact", lang, title=c["title"], description=c["desc"],
            body=body, schema=schema, crumbs=c["crumbs"])
