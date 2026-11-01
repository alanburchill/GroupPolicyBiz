// Search uses ordinary links so results work with Tab and screen readers.
(function () {
  let searchIndex = [];
  let loadState = 'loading';
  let searchInput, searchResults, searchStatus, searchBox;
  let searchTimeout;
  let suppressFocusSearch = false;

  function getBasePath() {
    let base = (window.__SITE_CONFIG__ || {}).basePath || '/';
    if (!base.startsWith('/')) base = '/' + base;
    return base.endsWith('/') ? base : base + '/';
  }

  function announce(message) {
    searchStatus.textContent = message;
  }

  function hideResults() {
    searchResults.hidden = true;
    announce('');
  }

  function renderSearch() {
    const query = searchInput.value.trim().toLowerCase();
    if (query.length < 2) { hideResults(); return; }
    searchResults.replaceChildren();
    if (loadState !== 'ready') {
      const message = loadState === 'loading' ? 'Loading search results.' : 'Search is unavailable. Please try again later.';
      searchResults.textContent = message;
      searchResults.hidden = false;
      announce(message);
      return;
    }
    const results = searchIndex.filter(post =>
      [post.title, post.excerpt, ...(post.categories || []), ...(post.tags || [])]
        .some(value => String(value || '').toLowerCase().includes(query))
    ).slice(0, 10);
    for (const post of results) {
      let target;
      try { target = new URL(post.url, location.origin); } catch (_) { continue; }
      if (target.origin !== location.origin || !/^https?:$/.test(target.protocol)) continue;
      const link = document.createElement('a');
      link.className = 'search-result-item';
      link.href = target.href;
      const title = document.createElement('div');
      title.className = 'search-result-title';
      title.textContent = post.title;
      const meta = document.createElement('div');
      meta.className = 'search-result-meta';
      meta.textContent = [post.date, (post.categories || []).join(', ')].filter(Boolean).join(' • ');
      link.append(title, meta);
      searchResults.append(link);
    }
    const count = searchResults.childElementCount;
    const message = count ? `${count} result${count === 1 ? '' : 's'}. Use Tab to browse results.` : 'No posts found.';
    const footer = document.createElement('div');
    footer.className = count ? 'search-result-footer' : 'search-no-results';
    footer.textContent = count ? `${count} result${count === 1 ? '' : 's'}` : 'No posts found';
    searchResults.append(footer);
    searchResults.hidden = false;
    announce(message);
  }

  async function loadSearchIndex() {
    try {
      const response = await fetch(`${getBasePath()}search-index.json`);
      if (!response.ok) throw new Error('Search index unavailable');
      const data = await response.json();
      if (!Array.isArray(data)) throw new Error('Invalid search index');
      searchIndex = data;
      loadState = 'ready';
    } catch (_) { loadState = 'error'; }
    if (searchBox.contains(document.activeElement)) renderSearch();
  }

  function initSearch() {
    searchInput = document.getElementById('site-search');
    if (!searchInput) return;
    searchBox = searchInput.parentElement;
    searchBox.style.position = 'relative';
    searchInput.setAttribute('aria-controls', 'search-results');
    searchResults = document.createElement('div');
    searchResults.id = 'search-results';
    searchResults.className = 'search-results-dropdown';
    searchResults.setAttribute('role', 'region');
    searchResults.setAttribute('aria-label', 'Search results');
    searchResults.hidden = true;
    searchStatus = document.createElement('div');
    searchStatus.className = 'search-status';
    searchStatus.setAttribute('role', 'status');
    searchStatus.setAttribute('aria-atomic', 'true');
    searchBox.append(searchResults, searchStatus);
    searchInput.addEventListener('input', () => {
      clearTimeout(searchTimeout);
      searchTimeout = setTimeout(renderSearch, 300);
    });
    searchInput.addEventListener('focus', () => {
      if (!suppressFocusSearch) renderSearch();
    });
    searchBox.addEventListener('keydown', event => {
      if (event.key === 'Escape' && !searchResults.hidden) {
        clearTimeout(searchTimeout);
        hideResults();
        suppressFocusSearch = true;
        searchInput.focus();
        suppressFocusSearch = false;
        event.preventDefault();
      }
    });
    searchBox.addEventListener('focusout', event => {
      if (!searchBox.contains(event.relatedTarget)) { clearTimeout(searchTimeout); hideResults(); }
    });
    document.addEventListener('click', event => {
      if (!searchBox.contains(event.target)) hideResults();
    });
    loadSearchIndex();
  }

  function initThemeToggle() {
    const toggle = document.getElementById('theme-toggle');
    if (!toggle) return;
    const currentTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', currentTheme);
    toggle.textContent = currentTheme === 'dark' ? '☀️' : '🌙';
    toggle.addEventListener('click', () => {
      const theme = document.documentElement.getAttribute('data-theme');
      const next = theme === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('theme', next);
      toggle.textContent = next === 'dark' ? '☀️' : '🌙';
    });
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => { initSearch(); initThemeToggle(); });
  } else { initSearch(); initThemeToggle(); }
})();
