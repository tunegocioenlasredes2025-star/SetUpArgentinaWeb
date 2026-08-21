/* Datos del proyecto de Supabase.

   La clave publicable esta pensada para vivir en el navegador: Supabase
   la llama "publishable" justamente porque es publica. Lo que protege la
   base son las politicas de RLS del schema.sql, no esconder esta clave.
   Verificado: sin login, la base rechaza cualquier escritura (401).      */

window.SETUP_CONFIG = {
  url: 'https://tvxhhbonqzabnwwpayet.supabase.co',
  key: 'sb_publishable_M-qp7enm2WJrT2l1e1bL3g_N57jtYAH',
  bucket: 'blog',
};
