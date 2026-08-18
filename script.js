/* ══════════════════════════════════════════
   SETUP ARGENTINA — script.js
   Scroll animations · Counters · Nav · FAQ · Form
══════════════════════════════════════════ */

document.addEventListener('DOMContentLoaded', () => {

  /* ─── NAVBAR — Scroll behavior ─────────── */
  const navbar = document.getElementById('navbar');

  const updateNav = () => {
    if (window.scrollY > 40) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  };
  window.addEventListener('scroll', updateNav, { passive: true });
  updateNav();

  /* ─── NAVBAR — Smooth scroll ────────────── */
  document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', e => {
      const id = link.getAttribute('href');
      if (id === '#') return;
      const target = document.querySelector(id);
      if (!target) return;
      e.preventDefault();
      const offset = 80;
      const top = target.getBoundingClientRect().top + window.scrollY - offset;
      window.scrollTo({ top, behavior: 'smooth' });
      closeMobileMenu();
    });
  });

  /* ─── MOBILE MENU ───────────────────────── */
  const navToggle  = document.getElementById('navToggle');
  const navLinks   = document.getElementById('navLinks');

  // Create overlay
  const overlay = document.createElement('div');
  overlay.className = 'mobile-menu-overlay';
  // El menu mobile se arma clonando el nav real de la pagina, para que
  // funcione igual en los dos idiomas y no queden links muertos al pasar
  // de la landing de una sola pagina al sitio multipagina.
  const menuList = navLinks ? navLinks.cloneNode(true) : document.createElement('ul');
  menuList.removeAttribute('id');
  const navCta   = document.querySelector('.nav-actions .btn-nav-cta');
  const navLang  = document.querySelector('.nav-actions .lang-switch');

  const closeBtn = document.createElement('button');
  closeBtn.className = 'mobile-menu-close';
  closeBtn.setAttribute('aria-label', 'Close menu');
  closeBtn.innerHTML = '<span></span><span></span>';

  overlay.appendChild(closeBtn);
  overlay.appendChild(menuList);
  if (navCta)  overlay.appendChild(navCta.cloneNode(true));
  if (navLang) overlay.appendChild(navLang.cloneNode(true));
  document.body.appendChild(overlay);

  const openMobileMenu  = () => {
    overlay.classList.add('open');
    document.body.style.overflow = 'hidden';
    navToggle.setAttribute('aria-expanded', 'true');
    const spans = navToggle.querySelectorAll('span');
    spans[0].style.transform = 'translateY(7px) rotate(45deg)';
    spans[1].style.opacity   = '0';
    spans[2].style.transform = 'translateY(-7px) rotate(-45deg)';
  };

  const closeMobileMenu = () => {
    overlay.classList.remove('open');
    document.body.style.overflow = '';
    navToggle.setAttribute('aria-expanded', 'false');
    const spans = navToggle.querySelectorAll('span');
    spans[0].style.transform = '';
    spans[1].style.opacity   = '';
    spans[2].style.transform = '';
  };

  navToggle.addEventListener('click', () => {
    if (overlay.classList.contains('open')) {
      closeMobileMenu();
    } else {
      openMobileMenu();
    }
  });

  // Close button inside overlay
  overlay.querySelector('.mobile-menu-close').addEventListener('click', closeMobileMenu);

  // Overlay links: smooth scroll + close menu
  overlay.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', e => {
      const id = link.getAttribute('href');
      if (id === '#') return;
      const target = document.querySelector(id);
      if (target) {
        e.preventDefault();
        const top = target.getBoundingClientRect().top + window.scrollY - 80;
        window.scrollTo({ top, behavior: 'smooth' });
      }
      closeMobileMenu();
    });
  });

  /* ─── SCROLL ANIMATIONS ─────────────────── */
  const animateObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el    = entry.target;
        const delay = parseInt(el.dataset.delay || 0);
        setTimeout(() => {
          el.classList.add('visible');
        }, delay);
        animateObserver.unobserve(el);
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -40px 0px'
  });

  document.querySelectorAll('[data-animate]').forEach(el => {
    animateObserver.observe(el);
  });

  /* ─── COUNTER ANIMATION ─────────────────── */
  const counters = document.querySelectorAll('.counter[data-target]');

  const animateCounter = (el) => {
    const target   = parseInt(el.dataset.target);
    const duration = 1800;
    const step     = 16;
    const increment = target / (duration / step);
    let current = 0;

    const timer = setInterval(() => {
      current += increment;
      if (current >= target) {
        el.textContent = target;
        clearInterval(timer);
      } else {
        el.textContent = Math.floor(current);
      }
    }, step);
  };

  const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animateCounter(entry.target);
        counterObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });

  counters.forEach(el => counterObserver.observe(el));

  /* ─── FAQ ACCORDION ─────────────────────── */
  const faqItems = document.querySelectorAll('.faq-item');

  faqItems.forEach(item => {
    const question = item.querySelector('.faq-question');
    const answer   = item.querySelector('.faq-answer');

    question.addEventListener('click', () => {
      const isOpen = item.classList.contains('open');

      // Close all
      faqItems.forEach(i => {
        i.classList.remove('open');
        i.querySelector('.faq-answer').style.maxHeight = null;
      });

      // Open clicked (if it was closed)
      if (!isOpen) {
        item.classList.add('open');
        answer.style.maxHeight = answer.scrollHeight + 'px';
      }
    });
  });

  // Open first FAQ by default
  if (faqItems.length > 0) {
    const first = faqItems[0];
    first.classList.add('open');
    const firstAnswer = first.querySelector('.faq-answer');
    firstAnswer.style.maxHeight = firstAnswer.scrollHeight + 'px';
  }

  /* ─── CONTACT FORM — Façade (activar backend después) ── */
  const form        = document.getElementById('contactForm');
  const formSuccess = document.getElementById('formSuccess');

  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();

      const name    = form.querySelector('#name').value.trim();
      const email   = form.querySelector('#email').value.trim();
      const country = form.querySelector('#country').value;

      if (!name || !email || !country) {
        shakeForm(form);
        highlightRequired(form);
        return;
      }
      if (!isValidEmail(email)) {
        form.querySelector('#email').style.borderColor = '#EF4444';
        return;
      }

      const submitBtn = form.querySelector('.btn-form-submit');
      const btnText   = submitBtn.querySelector('.btn-text');
      submitBtn.disabled = true;
      btnText.textContent = 'Sending...';

      const service  = form.querySelector('#service')?.value || '';
      const message  = form.querySelector('#message')?.value.trim() || '';
      const company  = form.querySelector('#company')?.value.trim() || '';
      const phone    = form.querySelector('#phone')?.value.trim() || '';

      const lines = [
        `Hi, my name is *${name}*${company ? ` from ${company}` : ''}.`,
        `Country: ${country}`,
        service  ? `Service needed: ${service}` : '',
        phone    ? `Phone: ${phone}` : '',
        message  ? `\n${message}` : '',
      ].filter(Boolean).join('\n');

      const waNumber = '5491125637925';
      const waUrl    = `https://wa.me/${waNumber}?text=${encodeURIComponent(lines)}`;

      setTimeout(() => {
        form.reset();
        submitBtn.disabled = false;
        btnText.textContent = 'Book Free Consultation';
        window.open(waUrl, '_blank');
      }, 800);
    });

    form.querySelectorAll('input, select, textarea').forEach(field => {
      field.addEventListener('input', () => {
        field.style.borderColor = '';
        field.style.boxShadow  = '';
      });
    });
  }

  const isValidEmail = (email) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);

  const shakeForm = (form) => {
    form.style.animation = 'none';
    form.offsetHeight;
    form.style.animation = 'shake 0.4s ease';
    setTimeout(() => { form.style.animation = ''; }, 400);
  };

  const highlightRequired = (form) => {
    ['name', 'email', 'country'].forEach(id => {
      const field = form.querySelector(`#${id}`);
      if (!field.value.trim()) {
        field.style.borderColor = '#EF4444';
        field.style.boxShadow = '0 0 0 3px rgba(239,68,68,0.12)';
      }
    });
  };

  /* ─── ACTIVE NAV LINK on scroll ─────────── */
  const sections = document.querySelectorAll('section[id]');
  const navAnchors = document.querySelectorAll('.nav-links a[href^="#"]');

  const activeObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.id;
        navAnchors.forEach(a => {
          a.classList.toggle('active', a.getAttribute('href') === `#${id}`);
        });
      }
    });
  }, {
    threshold: 0.35,
    rootMargin: '-80px 0px -60% 0px'
  });

  sections.forEach(s => activeObserver.observe(s));

  /* ─── SERVICE CARDS — Micro interaction ── */
  document.querySelectorAll('.service-card').forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect  = card.getBoundingClientRect();
      const x     = ((e.clientX - rect.left) / rect.width - 0.5) * 10;
      const y     = ((e.clientY - rect.top)  / rect.height - 0.5) * 10;
      card.style.transform = `translateY(-3px) rotateX(${-y * 0.4}deg) rotateY(${x * 0.4}deg)`;
    });
    card.addEventListener('mouseleave', () => {
      card.style.transform = '';
      card.style.transition = 'transform 0.3s ease';
    });
    card.addEventListener('mouseenter', () => {
      card.style.transition = 'transform 0.1s ease, border-color 0.3s ease, box-shadow 0.3s ease';
    });
  });

});

/* ─── CSS SHAKE ANIMATION (injected) ────── */
const shakeStyle = document.createElement('style');
shakeStyle.textContent = `
  @keyframes shake {
    0%, 100% { transform: translateX(0); }
    20%       { transform: translateX(-8px); }
    40%       { transform: translateX(8px); }
    60%       { transform: translateX(-5px); }
    80%       { transform: translateX(5px); }
  }
`;
document.head.appendChild(shakeStyle);

/* ─── SELECTOR DE IDIOMA ─────────────────────────────
   Se le OFRECE al visitante cambiar de idioma; nunca se lo
   redirige por su ubicacion. Redirigir por IP hace que el robot
   de Google, que rastrea desde Estados Unidos, vea siempre la
   misma version y nunca encuentre la otra.                      */
(function () {
  var KEY = 'setup_lang';
  var hint = document.getElementById('langHint');
  var html = document.documentElement.lang || 'en';
  var pageLang = html.slice(0, 2);

  // Si ya eligio un idioma antes, respetamos esa eleccion y no molestamos.
  document.querySelectorAll('.lang-switch, .lang-hint-go').forEach(function (a) {
    a.addEventListener('click', function () {
      try { localStorage.setItem(KEY, a.getAttribute('hreflang') ||
            (pageLang === 'en' ? 'es' : 'en')); } catch (e) {}
    });
  });

  if (!hint) return;

  var saved;
  try { saved = localStorage.getItem(KEY); } catch (e) {}
  if (saved) return;                       // ya decidio
  try { if (sessionStorage.getItem(KEY + '_dismissed')) return; } catch (e) {}

  var prefers = (navigator.languages || [navigator.language || 'en'])[0]
                  .slice(0, 2).toLowerCase();
  var target  = pageLang === 'en' ? 'es' : 'en';

  // Solo se muestra si el navegador pide justo el otro idioma.
  if (prefers !== target) return;

  hint.hidden = false;
  hint.querySelector('.lang-hint-close').addEventListener('click', function () {
    hint.hidden = true;
    try { sessionStorage.setItem(KEY + '_dismissed', '1'); } catch (e) {}
  });
})();
