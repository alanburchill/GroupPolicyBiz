// Live search functionality for static WordPress-like site
(function() {
  let searchIndex = [];
  let searchInput = null;
  let searchResults = null;
  
  // Load search index
  async function loadSearchIndex() {
    try {
      // Determine base path from current URL
      // For GitHub Pages subdirectory deployment (e.g., /GroupPolicyBiz/)
      const basePath = window.location.pathname.match(/^\/[^\/]+\//)?.[0] || '/';
      const searchIndexUrl = `${basePath}search-index.json`.replace('//', '/');
      
      const response = await fetch(searchIndexUrl);
      searchIndex = await response.json();
      console.log(`Loaded ${searchIndex.length} posts for search`);
    } catch (error) {
      console.error('Failed to load search index:', error);
    }
  }
  
  // Create search results dropdown
  function createSearchResultsContainer() {
    const container = document.createElement('div');
    container.id = 'search-results';
    container.className = 'search-results-dropdown';
    container.style.display = 'none';
    return container;
  }
  
  // Perform search
  function performSearch(query) {
    if (!query || query.length < 2) {
      hideSearchResults();
      return;
    }
    
    query = query.toLowerCase();
    const results = searchIndex.filter(post => {
      return post.title.toLowerCase().includes(query) ||
             post.excerpt.toLowerCase().includes(query) ||
             post.categories.some(c => c.toLowerCase().includes(query)) ||
             post.tags.some(t => t.toLowerCase().includes(query));
    }).slice(0, 10); // Limit to 10 results
    
    displaySearchResults(results, query);
  }
  
  // Display search results
  function displaySearchResults(results, query) {
    if (!searchResults) return;
    
    if (results.length === 0) {
      searchResults.innerHTML = '<div class="search-no-results">No posts found</div>';
      searchResults.style.display = 'block';
      return;
    }
    
    const html = results.map(post => {
      const highlightedTitle = post.title.replace(
        new RegExp(`(${escapeRegex(query)})`, 'gi'),
        '<mark>$1</mark>'
      );
      return `
        <a href="${post.url}" class="search-result-item">
          <div class="search-result-title">${highlightedTitle}</div>
          <div class="search-result-meta">${post.date} • ${post.categories.join(', ')}</div>
        </a>
      `;
    }).join('');
    
    searchResults.innerHTML = html + `<div class="search-result-footer">${results.length} result${results.length > 1 ? 's' : ''}</div>`;
    searchResults.style.display = 'block';
  }
  
  // Hide search results
  function hideSearchResults() {
    if (searchResults) {
      searchResults.style.display = 'none';
    }
  }
  
  // Escape regex special characters
  function escapeRegex(str) {
    return str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  }
  
  // Initialize search
  function initSearch() {
    searchInput = document.getElementById('site-search');
    if (!searchInput) return;
    
    // Create results container
    searchResults = createSearchResultsContainer();
    const searchBox = searchInput.parentElement;
    searchBox.style.position = 'relative';
    searchBox.appendChild(searchResults);
    
    // Event listeners
    let searchTimeout;
    searchInput.addEventListener('input', (e) => {
      clearTimeout(searchTimeout);
      searchTimeout = setTimeout(() => {
        performSearch(e.target.value);
      }, 300); // Debounce 300ms
    });
    
    searchInput.addEventListener('focus', (e) => {
      if (e.target.value.length >= 2) {
        performSearch(e.target.value);
      }
    });
    
    // Close on click outside
    document.addEventListener('click', (e) => {
      if (!searchBox.contains(e.target)) {
        hideSearchResults();
      }
    });
    
    // Keyboard navigation
    searchInput.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        hideSearchResults();
        searchInput.blur();
      }
    });
  }
  
  // Theme toggle (reuse from existing code)
  function initThemeToggle() {
    const toggle = document.getElementById('theme-toggle');
    if (!toggle) return;
    
    const currentTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', currentTheme);
    toggle.textContent = currentTheme === 'dark' ? '☀️' : '🌙';
    
    toggle.addEventListener('click', () => {
      const theme = document.documentElement.getAttribute('data-theme');
      const newTheme = theme === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', newTheme);
      localStorage.setItem('theme', newTheme);
      toggle.textContent = newTheme === 'dark' ? '☀️' : '🌙';
    });
  }
  
  // Initialize on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
      loadSearchIndex();
      initSearch();
      initThemeToggle();
    });
  } else {
    loadSearchIndex();
    initSearch();
    initThemeToggle();
  }
})();
