document.addEventListener('DOMContentLoaded', () => {
  const counterEl = document.querySelector('[data-visit-counter]');
  if (!counterEl) {
    return;
  }

  const namespace = 'yanndanneelscoignard.fr';
  const key = 'site';
  const url = `https://api.countapi.xyz/hit/${encodeURIComponent(namespace)}/${encodeURIComponent(key)}`;

  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      if (typeof data.value === 'number') {
        counterEl.textContent = data.value.toLocaleString('fr-FR');
      } else {
        counterEl.textContent = '—';
      }
    })
    .catch(() => {
      counterEl.textContent = '—';
    });
});
