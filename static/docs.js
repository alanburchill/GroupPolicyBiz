document.addEventListener('DOMContentLoaded', () => {
  const themeButton = document.querySelector('.docs-theme-toggle');
  const systemTheme = window.matchMedia('(prefers-color-scheme: dark)');
  let preference = null;
  try { preference = localStorage.getItem('group-policy-docs-theme'); } catch (_) {}
  const applyTheme = () => {
    const dark = preference ? preference === 'dark' : systemTheme.matches;
    document.documentElement.dataset.docsTheme = dark ? 'dark' : 'light';
    if (themeButton) {
      themeButton.textContent = dark ? '☀ Light theme' : '☾ Dark theme';
      themeButton.setAttribute('aria-label', dark ? 'Switch to light theme' : 'Switch to dark theme');
    }
  };
  applyTheme();
  systemTheme.addEventListener('change', () => { if (!preference) applyTheme(); });
  if (themeButton) themeButton.addEventListener('click', () => {
    preference = document.documentElement.dataset.docsTheme === 'dark' ? 'light' : 'dark';
    try { localStorage.setItem('group-policy-docs-theme', preference); } catch (_) {}
    applyTheme();
  });
  const toggle = document.querySelector('.menu-toggle');
  const sidebar = document.querySelector('.docs-sidebar');
  if (toggle && sidebar) toggle.addEventListener('click', () => {
    const open = sidebar.classList.toggle('is-open');
    toggle.setAttribute('aria-expanded', String(open));
  });
  document.querySelectorAll('.docs-sidebar nav a').forEach(link => {
    if (link.pathname === location.pathname) link.setAttribute('aria-current', 'page');
  });
});
