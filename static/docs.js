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
    const current = preference || document.documentElement.dataset.docsTheme;
    preference = current === 'dark' ? 'light' : 'dark';
    try { localStorage.setItem('group-policy-docs-theme', preference); } catch (_) {}
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const forcedColors = window.matchMedia('(forced-colors: active)').matches;
    if (!reduceMotion && !forcedColors && typeof document.startViewTransition === 'function') {
      // Cross-fade complete theme snapshots so text and its background change together.
      document.startViewTransition(applyTheme).finished.catch(() => {});
    } else {
      applyTheme();
    }
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
