-- ═══════════════════════════════════════════════════════════════
-- SetUp Argentina — base del blog
-- Pegar entero en Supabase → SQL Editor → Run.
-- Es idempotente: se puede correr de nuevo sin romper nada.
-- ═══════════════════════════════════════════════════════════════

-- ── La tabla de notas ─────────────────────────────────────────
-- Una fila por nota, con las columnas duplicadas por idioma. Asi una
-- nota puede existir solo en ingles: el sitio simplemente la oculta
-- del listado en espanol en vez de mostrar un hueco vacio.
create table if not exists public.posts (
  id           uuid primary key default gen_random_uuid(),

  slug_en      text unique,
  slug_es      text unique,

  title_en     text,
  title_es     text,
  excerpt_en   text,
  excerpt_es   text,
  body_en      text,          -- HTML generado por el editor
  body_es      text,

  cover_url    text,
  cover_alt_en text,
  cover_alt_es text,

  status       text not null default 'draft'
               check (status in ('draft', 'published')),
  published_at timestamptz,   -- puede ser futura: la nota queda programada

  created_at   timestamptz not null default now(),
  updated_at   timestamptz not null default now()
);

-- El listado ordena por fecha de publicacion, con filtro por estado.
create index if not exists posts_published_idx
  on public.posts (status, published_at desc);

-- updated_at se mantiene solo
create or replace function public.touch_updated_at()
returns trigger language plpgsql as $$
begin
  new.updated_at = now();
  return new;
end $$;

drop trigger if exists posts_touch_updated_at on public.posts;
create trigger posts_touch_updated_at
  before update on public.posts
  for each row execute function public.touch_updated_at();


-- ── Seguridad ─────────────────────────────────────────────────
-- La clave anon del sitio es publica por diseno, asi que la unica
-- proteccion real son estas politicas. Sin ellas, cualquiera con la
-- clave podria escribir en el blog.
alter table public.posts enable row level security;

-- Cualquiera puede LEER, pero solo las notas ya publicadas y cuya
-- fecha ya llego. Las programadas a futuro y los borradores no salen.
drop policy if exists "lectura publica de notas publicadas" on public.posts;
create policy "lectura publica de notas publicadas"
  on public.posts for select
  to anon, authenticated
  using (status = 'published' and published_at <= now());

-- Escribir, editar y borrar: solo usuarios logueados (el panel).
drop policy if exists "el panel lee todo" on public.posts;
create policy "el panel lee todo"
  on public.posts for select to authenticated using (true);

drop policy if exists "el panel escribe" on public.posts;
create policy "el panel escribe"
  on public.posts for insert to authenticated with check (true);

drop policy if exists "el panel edita" on public.posts;
create policy "el panel edita"
  on public.posts for update to authenticated using (true) with check (true);

drop policy if exists "el panel borra" on public.posts;
create policy "el panel borra"
  on public.posts for delete to authenticated using (true);


-- ── Imagenes ──────────────────────────────────────────────────
insert into storage.buckets (id, name, public)
values ('blog', 'blog', true)
on conflict (id) do update set public = true;

drop policy if exists "imagenes del blog visibles" on storage.objects;
create policy "imagenes del blog visibles"
  on storage.objects for select
  to anon, authenticated
  using (bucket_id = 'blog');

drop policy if exists "el panel sube imagenes" on storage.objects;
create policy "el panel sube imagenes"
  on storage.objects for insert
  to authenticated
  with check (bucket_id = 'blog');

drop policy if exists "el panel borra imagenes" on storage.objects;
create policy "el panel borra imagenes"
  on storage.objects for delete
  to authenticated
  using (bucket_id = 'blog');


-- ── Chequeo ───────────────────────────────────────────────────
-- Deberia devolver 0 filas y ningun error.
select count(*) as notas from public.posts;
