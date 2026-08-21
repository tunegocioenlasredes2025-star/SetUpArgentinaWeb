-- ═══════════════════════════════════════════════════════════════
-- SetUp Argentina — consultas del formulario
--
-- Hoy el formulario de la landing no guarda nada: arma un texto y abre
-- WhatsApp con window.open dentro de un setTimeout, cosa que los
-- navegadores bloquean por estar fuera del gesto del usuario. Si el
-- popup se bloquea, la consulta se pierde y nadie se entera.
--
-- Con esta tabla, la consulta queda guardada ANTES de mandar a nadie a
-- WhatsApp. Aunque la persona nunca termine de escribir por WhatsApp,
-- el contacto ya esta registrado.
-- ═══════════════════════════════════════════════════════════════

create table if not exists public.leads (
  id         uuid primary key default gen_random_uuid(),

  name       text not null,
  email      text not null,
  company    text,
  phone      text,
  country    text,
  service    text,
  message    text,

  lang       text,          -- en que idioma del sitio llego
  source     text,          -- desde que pagina se envio
  status     text not null default 'new'
             check (status in ('new', 'contacted', 'archived')),

  created_at timestamptz not null default now()
);

create index if not exists leads_created_idx on public.leads (created_at desc);

alter table public.leads enable row level security;

-- Cualquier visitante puede DEJAR una consulta...
drop policy if exists "el sitio deja consultas" on public.leads;
create policy "el sitio deja consultas"
  on public.leads for insert
  to anon, authenticated
  with check (true);

-- ...pero NADIE anonimo puede leerlas. Sin esta asimetria, cualquiera
-- con la clave publicable se llevaria la lista de contactos del cliente.
drop policy if exists "solo el panel lee las consultas" on public.leads;
create policy "solo el panel lee las consultas"
  on public.leads for select to authenticated using (true);

drop policy if exists "solo el panel actualiza consultas" on public.leads;
create policy "solo el panel actualiza consultas"
  on public.leads for update to authenticated using (true) with check (true);

drop policy if exists "solo el panel borra consultas" on public.leads;
create policy "solo el panel borra consultas"
  on public.leads for delete to authenticated using (true);

select count(*) as consultas from public.leads;
