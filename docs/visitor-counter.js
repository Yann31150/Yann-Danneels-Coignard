document.addEventListener('DOMContentLoaded', () => {
  // Clé secrète pour afficher le compteur (vous pouvez la changer)
  const SECRET_KEY = 'admin2026';
  
  // Vérifier si le paramètre URL contient la clé secrète
  const urlParams = new URLSearchParams(window.location.search);
  const urlKey = urlParams.get('key');
  const showStats = urlParams.get('stats') === '1' || urlKey === SECRET_KEY;
  
  // Vérifier aussi dans localStorage si l'utilisateur a déjà activé l'affichage
  const statsEnabled = localStorage.getItem('showVisitorStats') === 'true';
  
  // Afficher le compteur si la clé est correcte OU si déjà activé
  if (showStats || statsEnabled) {
    // Sauvegarder la préférence dans localStorage
    if (showStats) {
      localStorage.setItem('showVisitorStats', 'true');
    }
    
    // Afficher le compteur
    const visitorCountEl = document.querySelector('.visitor-count');
    if (visitorCountEl) {
      visitorCountEl.classList.add('show');
    }
    
    // Charger et afficher le compteur
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
  } else {
    // Masquer le compteur si pas de clé
    const visitorCountEl = document.querySelector('.visitor-count');
    if (visitorCountEl) {
      visitorCountEl.style.display = 'none';
    }
  }
});
