/* Panel del blog de SetUp Argentina.
   Una nota = una fila, con los campos duplicados por idioma. Se puede
   publicar solo en un idioma: el sitio oculta la nota del otro listado
   en vez de mostrar un hueco vacio.                                     */

import { createClient } from 'https://esm.sh/@supabase/supabase-js@2';

const CFG = window.SETUP_CONFIG;
const db = createClient(CFG.url, CFG.key);

const $ = (id) => document.getElementById(id);
const on = (el, ev, fn) => el && el.addEventListener(ev, fn);

/* ── Estado ───────────────────────────────────────────── */
let lang = 'es';            // pestaña activa
let post = null;            // nota en edicion
let slugTocado = false;     // si el usuario edito el slug a mano

const VACIA = () => ({
  slug_en: '', slug_es: '', title_en: '', title_es: '',
  excerpt_en: '', excerpt_es: '', body_en: '', body_es: '',
  cover_url: null, cover_alt_en: '', cover_alt_es: '',
  status: 'draft', published_at: null,
});

/* ── Utilidades ───────────────────────────────────────── */
function slugify(texto) {
  return (texto || '')
    .normalize('NFD').replace(/[̀-ͯ]/g, '')   // saca acentos
    .toLowerCase()
    .replace(/[^a-z0-9\s-]/g, '')
    .trim()
    .replace(/\s+/g, '-')
    .replace(/-+/g, '-')
    .slice(0, 70);
}

function aviso(el, texto, tipo) {
  el.textContent = texto;
  el.className = 'msg show ' + (tipo || 'ok');
  if (tipo !== 'error') setTimeout(() => { el.className = 'msg'; }, 3500);
}

function hoyISO() {
  const d = new Date();
  return d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0')
         + '-' + String(d.getDate()).padStart(2, '0');
}

/* ── Sesion ───────────────────────────────────────────── */
async function arrancar() {
  const { data } = await db.auth.getSession();
  if (data.session) mostrarApp(data.session.user);
}

function mostrarApp(user) {
  $('loginView').classList.add('hidden');
  $('appView').classList.remove('hidden');
  $('who').textContent = user.email;
  cargarLista();
}

on($('loginForm'), 'submit', async (e) => {
  e.preventDefault();
  const btn = $('loginBtn');
  btn.disabled = true;
  btn.textContent = 'Entrando...';
  const { data, error } = await db.auth.signInWithPassword({
    email: $('email').value.trim(),
    password: $('password').value,
  });
  btn.disabled = false;
  btn.textContent = 'Entrar';
  if (error) {
    aviso($('loginMsg'), 'No pudimos entrar: ' + error.message, 'error');
    return;
  }
  mostrarApp(data.user);
});

on($('logoutBtn'), 'click', async () => {
  await db.auth.signOut();
  location.reload();
});

/* ── Listado ──────────────────────────────────────────── */
async function cargarLista() {
  const cont = $('postList');
  cont.innerHTML = '<p style="color:var(--text-3)">Cargando...</p>';

  const { data, error } = await db.from('posts')
    .select('*').order('updated_at', { ascending: false });

  if (error) {
    cont.innerHTML = '<div class="empty">No pudimos leer las notas: '
                   + error.message + '</div>';
    return;
  }
  if (!data.length) {
    cont.innerHTML = '<div class="empty"><strong>Todavía no hay notas.</strong>'
      + '<br>Tocá “Nueva nota” para escribir la primera.</div>';
    return;
  }

  cont.innerHTML = data.map((p) => {
    const titulo = p.title_es || p.title_en || '(sin título)';
    const programada = p.status === 'published' && p.published_at
                       && new Date(p.published_at) > new Date();
    const estado = programada ? 'scheduled' : p.status;
    const etiqueta = { draft: 'Borrador', published: 'Publicada',
                       scheduled: 'Programada' }[estado];
    const idiomas = [];
    if (p.title_es) idiomas.push('ES');
    if (p.title_en) idiomas.push('EN');
    const fecha = p.published_at
      ? new Date(p.published_at).toLocaleDateString('es-AR')
      : 'sin fecha';
    return `<div class="post-row">
      <div class="grow">
        <h3>${escapar(titulo)}</h3>
        <div class="meta"><span>${fecha}</span>
          ${idiomas.map((l) => `<span class="pill lang">${l}</span>`).join('')}</div>
      </div>
      <span class="pill ${estado}">${etiqueta}</span>
      <button class="btn btn-ghost" data-edit="${p.id}">Editar</button>
    </div>`;
  }).join('');

  cont.querySelectorAll('[data-edit]').forEach((b) => {
    on(b, 'click', () => abrir(data.find((p) => p.id === b.dataset.edit)));
  });
}

function escapar(s) {
  const d = document.createElement('div');
  d.textContent = s;
  return d.innerHTML;
}

/* ── Editor ───────────────────────────────────────────── */
on($('newBtn'), 'click', () => abrir(null));
on($('backBtn'), 'click', () => {
  $('editView').classList.add('hidden');
  $('listView').classList.remove('hidden');
  cargarLista();
});

function abrir(p) {
  post = p ? { ...p } : VACIA();
  slugTocado = !!p;
  lang = 'es';
  document.querySelectorAll('.tab').forEach((t) => {
    t.classList.toggle('active', t.dataset.lang === 'es');
  });
  $('deleteBtn').classList.toggle('hidden', !p);
  $('status').value = post.status;
  $('publishedAt').value = post.published_at
    ? post.published_at.slice(0, 10) : hoyISO();
  pintarPortada();
  volcar();
  $('listView').classList.add('hidden');
  $('editView').classList.remove('hidden');
  window.scrollTo(0, 0);
}

/* Pasa del objeto a los campos */
function volcar() {
  $('title').value = post['title_' + lang] || '';
  $('excerpt').value = post['excerpt_' + lang] || '';
  $('body').innerHTML = post['body_' + lang] || '';
  $('slug').value = post['slug_' + lang] || '';
  $('coverAlt').value = post['cover_alt_' + lang] || '';
  $('slugHint').textContent = (lang === 'es' ? '/es/blog/' : '/blog/')
    + ($('slug').value || '…') + '/';
  $('dotEs').classList.toggle('hidden', !post.title_es);
  $('dotEn').classList.toggle('hidden', !post.title_en);
}

/* Pasa de los campos al objeto */
function recoger() {
  post['title_' + lang] = $('title').value.trim();
  post['excerpt_' + lang] = $('excerpt').value.trim();
  post['body_' + lang] = $('body').innerHTML.trim();
  post['slug_' + lang] = $('slug').value.trim() || null;
  post['cover_alt_' + lang] = $('coverAlt').value.trim();
  post.status = $('status').value;
  post.published_at = $('publishedAt').value
    ? new Date($('publishedAt').value + 'T12:00:00').toISOString() : null;
}

document.querySelectorAll('.tab').forEach((t) => {
  on(t, 'click', () => {
    recoger();
    lang = t.dataset.lang;
    document.querySelectorAll('.tab').forEach((x) => x.classList.remove('active'));
    t.classList.add('active');
    slugTocado = !!post['slug_' + lang];
    volcar();
  });
});

on($('title'), 'input', () => {
  if (!slugTocado) {
    $('slug').value = slugify($('title').value);
    $('slugHint').textContent = (lang === 'es' ? '/es/blog/' : '/blog/')
      + ($('slug').value || '…') + '/';
  }
});
on($('slug'), 'input', () => {
  slugTocado = true;
  $('slug').value = slugify($('slug').value);
  $('slugHint').textContent = (lang === 'es' ? '/es/blog/' : '/blog/')
    + ($('slug').value || '…') + '/';
});

/* ── Barra de formato ─────────────────────────────────── */
document.querySelectorAll('.toolbar [data-cmd]').forEach((b) => {
  on(b, 'click', () => {
    $('body').focus();
    document.execCommand(b.dataset.cmd, false, null);
  });
});
document.querySelectorAll('.toolbar [data-block]').forEach((b) => {
  on(b, 'click', () => {
    $('body').focus();
    document.execCommand('formatBlock', false, b.dataset.block);
  });
});
on($('linkBtn'), 'click', () => {
  const url = prompt('¿A qué dirección lleva el link?', 'https://');
  if (url) {
    $('body').focus();
    document.execCommand('createLink', false, url);
  }
});

/* Pegar siempre como texto plano: evita que se cuele el formato de Word */
on($('body'), 'paste', (e) => {
  e.preventDefault();
  const texto = (e.clipboardData || window.clipboardData).getData('text/plain');
  document.execCommand('insertText', false, texto);
});

/* ── Imágenes ─────────────────────────────────────────── */
async function subirImagen(file) {
  const ext = (file.name.split('.').pop() || 'jpg').toLowerCase();
  const nombre = Date.now() + '-' + Math.random().toString(36).slice(2, 8) + '.' + ext;
  const { error } = await db.storage.from(CFG.bucket)
    .upload(nombre, file, { cacheControl: '31536000', upsert: false });
  if (error) throw error;
  const { data } = db.storage.from(CFG.bucket).getPublicUrl(nombre);
  return data.publicUrl;
}

on($('imgBtn'), 'click', () => {
  const inp = document.createElement('input');
  inp.type = 'file';
  inp.accept = 'image/*';
  inp.onchange = async () => {
    if (!inp.files[0]) return;
    aviso($('editMsg'), 'Subiendo imagen...', 'ok');
    try {
      const url = await subirImagen(inp.files[0]);
      $('body').focus();
      document.execCommand('insertHTML', false,
        '<img src="' + url + '" alt="">');
    } catch (e) {
      aviso($('editMsg'), 'No se pudo subir: ' + e.message, 'error');
    }
  };
  inp.click();
});

/* Arrastrar una imagen sobre el texto */
on($('body'), 'drop', async (e) => {
  const file = e.dataTransfer && e.dataTransfer.files[0];
  if (!file || !file.type.startsWith('image/')) return;
  e.preventDefault();
  aviso($('editMsg'), 'Subiendo imagen...', 'ok');
  try {
    const url = await subirImagen(file);
    document.execCommand('insertHTML', false, '<img src="' + url + '" alt="">');
  } catch (err) {
    aviso($('editMsg'), 'No se pudo subir: ' + err.message, 'error');
  }
});

on($('coverBtn'), 'click', () => $('coverInput').click());
on($('coverInput'), 'change', async () => {
  if (!$('coverInput').files[0]) return;
  try {
    post.cover_url = await subirImagen($('coverInput').files[0]);
    pintarPortada();
  } catch (e) {
    aviso($('editMsg'), 'No se pudo subir: ' + e.message, 'error');
  }
});
on($('coverRemove'), 'click', () => { post.cover_url = null; pintarPortada(); });

function pintarPortada() {
  const img = $('coverPreview');
  const hay = !!post.cover_url;
  img.classList.toggle('hidden', !hay);
  $('coverRemove').classList.toggle('hidden', !hay);
  if (hay) img.src = post.cover_url;
  $('coverBtn').textContent = hay ? 'Cambiar imagen' : 'Subir imagen';
}

/* ── Guardar ──────────────────────────────────────────── */
async function guardar(publicar) {
  recoger();
  if (publicar) post.status = 'published';

  if (!post.title_es && !post.title_en) {
    aviso($('editMsg'), 'Poné al menos un título, en español o en inglés.', 'error');
    return;
  }
  // Un idioma sin slug no puede tener direccion propia.
  ['es', 'en'].forEach((l) => {
    if (post['title_' + l] && !post['slug_' + l]) {
      post['slug_' + l] = slugify(post['title_' + l]);
    }
    if (!post['title_' + l]) post['slug_' + l] = null;
  });
  if (post.status === 'published' && !post.published_at) {
    post.published_at = new Date().toISOString();
  }

  const btn = publicar ? $('publishBtn') : $('saveBtn');
  const original = btn.textContent;
  btn.disabled = true;
  btn.textContent = 'Guardando...';

  const fila = { ...post };
  delete fila.created_at;
  delete fila.updated_at;

  let res;
  if (fila.id) {
    const id = fila.id;
    delete fila.id;
    res = await db.from('posts').update(fila).eq('id', id).select().single();
  } else {
    delete fila.id;
    res = await db.from('posts').insert(fila).select().single();
  }

  btn.disabled = false;
  btn.textContent = original;

  if (res.error) {
    const dup = res.error.code === '23505';
    aviso($('editMsg'), dup
      ? 'Ya existe otra nota con esa misma dirección web. Cambiá el slug.'
      : 'No se pudo guardar: ' + res.error.message, 'error');
    return;
  }
  post = res.data;
  $('deleteBtn').classList.remove('hidden');
  $('status').value = post.status;
  volcar();
  aviso($('editMsg'), publicar
    ? 'Publicada. En un minuto está online.'
    : 'Borrador guardado.', 'ok');
}

on($('saveBtn'), 'click', () => guardar(false));
on($('publishBtn'), 'click', () => guardar(true));

on($('deleteBtn'), 'click', async () => {
  if (!post.id) return;
  if (!confirm('¿Borrar esta nota? No se puede deshacer.')) return;
  const { error } = await db.from('posts').delete().eq('id', post.id);
  if (error) {
    aviso($('editMsg'), 'No se pudo borrar: ' + error.message, 'error');
    return;
  }
  $('editView').classList.add('hidden');
  $('listView').classList.remove('hidden');
  cargarLista();
});

arrancar();

/* ═══════════ CONSULTAS ═══════════
   Lo que entra por el formulario del sitio. La base solo deja leerlas a
   un usuario logueado: si fueran publicas, cualquiera con la clave del
   sitio se llevaria la lista de contactos del cliente.                  */

function vistaConsultas(mostrar) {
  $('leadsView').classList.toggle('hidden', !mostrar);
  $('listView').classList.toggle('hidden', mostrar);
  $('editView').classList.add('hidden');
  $('navLeads').classList.toggle('active', mostrar);
  $('navPosts').classList.toggle('active', !mostrar);
  if (mostrar) cargarConsultas();
  else cargarLista();
}

on($('navLeads'), 'click', () => vistaConsultas(true));
on($('navPosts'), 'click', () => vistaConsultas(false));

async function cargarConsultas() {
  const cont = $('leadList');
  cont.innerHTML = '<p style="color:var(--text-3)">Cargando...</p>';

  const { data, error } = await db.from('leads')
    .select('*').order('created_at', { ascending: false });

  if (error) {
    cont.innerHTML = '<div class="empty">No pudimos leer las consultas: '
                   + error.message + '</div>';
    return;
  }
  if (!data.length) {
    cont.innerHTML = '<div class="empty"><strong>Todavía no entró ninguna consulta.</strong>'
      + '<br>Cuando alguien complete el formulario del sitio, aparece acá.</div>';
    $('leadsBadge').textContent = '';
    return;
  }

  const nuevas = data.filter((l) => l.status === 'new').length;
  $('leadsBadge').textContent = nuevas || '';

  cont.innerHTML = data.map((l) => {
    const fecha = new Date(l.created_at).toLocaleString('es-AR',
      { day: '2-digit', month: '2-digit', year: 'numeric',
        hour: '2-digit', minute: '2-digit' });
    const meta = [fecha, l.lang ? l.lang.toUpperCase() : null, l.country,
                  l.company, l.source].filter(Boolean);
    const tel = (l.phone || '').replace(/[^0-9]/g, '');
    const etiqueta = { new: 'Nueva', contacted: 'Contactada',
                       archived: 'Archivada' }[l.status];
    return `<div class="lead ${l.status === 'new' ? 'is-new' : ''}">
      <div class="lead-head">
        <strong>${escapar(l.name)}</strong>
        <span class="pill ${l.status === 'new' ? 'scheduled' : 'draft'}">${etiqueta}</span>
        ${l.service ? `<span class="pill lang">${escapar(l.service)}</span>` : ''}
      </div>
      <div class="lead-meta">${meta.map(escapar).join(' · ')}</div>
      ${l.message ? `<div class="lead-msg">${escapar(l.message)}</div>` : ''}
      <div class="lead-actions">
        <a href="mailto:${escapar(l.email)}">${escapar(l.email)}</a>
        ${tel ? `<a href="https://wa.me/${tel}" target="_blank" rel="noopener">WhatsApp</a>` : ''}
        ${l.status === 'new'
          ? `<button data-contactada="${l.id}">Marcar como contactada</button>` : ''}
        <button data-archivar="${l.id}">Archivar</button>
      </div>
    </div>`;
  }).join('');

  cont.querySelectorAll('[data-contactada]').forEach((b) => {
    on(b, 'click', () => cambiarEstado(b.dataset.contactada, 'contacted'));
  });
  cont.querySelectorAll('[data-archivar]').forEach((b) => {
    on(b, 'click', () => cambiarEstado(b.dataset.archivar, 'archived'));
  });
}

async function cambiarEstado(id, estado) {
  const { error } = await db.from('leads').update({ status: estado }).eq('id', id);
  if (error) {
    alert('No se pudo actualizar: ' + error.message);
    return;
  }
  cargarConsultas();
}
