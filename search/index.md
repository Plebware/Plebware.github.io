---
layout: default
title: Search
---

# 🔎 Search

<form id="search-form">
  <input type="text" id="search-input" placeholder="Type to search..." style="width: 100%; padding: 0.5rem; font-size: 1rem;">
</form>

<div id="search-results"></div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/lunr.js/2.3.9/lunr.min.js"></script>
<script>
  (function() {
    const searchInput = document.getElementById('search-input');
    const resultsContainer = document.getElementById('search-results');

    // Build the Lunr index
    let index;
    let store = [];

    fetch('/search.json')
      .then(response => response.json())
      .then(posts => {
        store = posts;

        // Build the Lunr index
        index = lunr(function() {
          this.field('title', { boost: 10 });
          this.field('content');
          this.field('excerpt');
          this.field('categories');
          this.ref('url');

          posts.forEach(post => {
            this.add(post);
          });
        });

        // If there's a query in the URL, run search
        const urlParams = new URLSearchParams(window.location.search);
        const query = urlParams.get('q');
        if (query) {
          searchInput.value = query;
          performSearch(query);
        }
      });

    // Perform search
    function performSearch(query) {
      if (!query || query.trim() === '') {
        resultsContainer.innerHTML = '<p>Enter a search term to find posts.</p>';
        return;
      }

      try {
        const results = index.search(query);

        if (results.length === 0) {
          resultsContainer.innerHTML = '<p>No results found for <strong>' + query + '</strong>.</p>';
          return;
        }

        // Display results
        let html = '<ul style="list-style: none; padding-left: 0;">';
        results.forEach(result => {
          const post = store.find(p => p.url === result.ref);
          if (post) {
            html += `
              <li style="margin-bottom: 1rem; padding: 0.5rem; border-bottom: 1px solid #eee;">
                <a href="${post.url}" style="font-weight: bold; font-size: 1.1rem;">${post.title}</a>
                <span style="display: block; font-size: 0.85rem; color: #666;">${post.date}${post.categories && post.categories.length > 0 ? ' · ' + post.categories.join(', ') : ''}</span>
                <span style="display: block; font-size: 0.9rem; margin-top: 0.2rem;">${post.excerpt}</span>
              </li>
            `;
          }
        });
        html += '</ul>';
        resultsContainer.innerHTML = html;
      } catch (e) {
        resultsContainer.innerHTML = '<p>Search error: ' + e.message + '</p>';
      }
    }

    // Handle input events
    searchInput.addEventListener('input', function() {
      const query = this.value;
      // Update URL without reloading
      if (window.history && window.history.replaceState) {
        const url = new URL(window.location);
        if (query) {
          url.searchParams.set('q', query);
        } else {
          url.searchParams.delete('q');
        }
        window.history.replaceState({}, '', url);
      }
      performSearch(query);
    });

    // Handle form submission
    document.getElementById('search-form').addEventListener('submit', function(e) {
      e.preventDefault();
      const query = searchInput.value;
      if (query) {
        performSearch(query);
      }
    });
  })();
</script>

<style>
  #search-input {
    width: 100%;
    padding: 0.8rem;
    font-size: 1.1rem;
    border: 1px solid var(--border);
    border-radius: 4px;
    background: var(--bg);
    color: var(--text);
  }
  #search-results {
    margin-top: 1.5rem;
  }
  #search-results li {
    margin-bottom: 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid var(--border);
  }
  #search-results a {
    color: var(--link);
    text-decoration: none;
  }
  #search-results a:hover {
    color: var(--link-hover);
    text-decoration: underline;
  }
</style>
