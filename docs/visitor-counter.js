document.addEventListener('DOMContentLoaded', () => {
  const counterEl = document.querySelector('[data-visit-counter]');
  if (!counterEl) {
    return;
  }

  const namespace = 'yanndanneelscoignard.fr';
  const key = 'site';
  const url = `https://api.countapi.xyz/hit/${encodeURIComponent(namespace)}/${encodeURIComponent(key)}`;

  fetch(url, { cache: 'no-store' })
    .then((response) => response.json())
    .then((data) => {
      if (typeof data.value === 'number') {
        counterEl.textContent = data.value.toLocaleString('fr-FR');
      } else {
        throw new Error('Invalid counter response');
      }
    })
    .catch(() => {
      const localKey = 'local-visit-count';
      const current = Number(window.localStorage.getItem(localKey) || '0') + 1;
      window.localStorage.setItem(localKey, String(current));
      counterEl.textContent = `${current.toLocaleString('fr-FR')} (local)`;
    });
});
