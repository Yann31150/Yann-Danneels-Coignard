#!/usr/bin/env python3
"""
Script pour ajouter automatiquement le sélecteur de langue et le script translations.js
à toutes les pages HTML du site.
"""

import os
import re
from pathlib import Path

# Chemin vers le dossier docs
DOCS_DIR = Path(__file__).parent.parent / "docs"

# Navigation avec traductions
NAV_WITH_TRANSLATIONS = '''            <ul class="nav-links">
                <li><a href="index.html" data-translate="nav.accueil">Accueil</a></li>
                <li><a href="apropos.html" data-translate="nav.apropos">À propos</a></li>
                <li><a href="competences.html" data-translate="nav.competences">Compétences</a></li>
                <li><a href="outils.html" data-translate="nav.outils">Outils</a></li>
                <li><a href="passions.html" data-translate="nav.passions">Passions</a></li>
                <li><a href="projets.html" data-translate="nav.projets">Projets</a></li>
                <li><a href="cv.html" data-translate="nav.cv">Mon CV</a></li>
                <li><a href="databridge.html" data-translate="nav.databridge">Databridge</a></li>
                <li><a href="actualites-tech.html" data-translate="nav.actualites">Actualités Tech</a></li>
                <li><a href="cybersecurite.html" data-translate="nav.cybersecurite">Cybersécurité</a></li>
                <li><a href="contact.html" data-translate="nav.contact">Contact</a></li>
                <li>
                    <div class="language-selector">
                        <button class="lang-btn active" data-lang="fr" onclick="setLanguage('fr')">FR</button>
                        <button class="lang-btn" data-lang="en" onclick="setLanguage('en')">EN</button>
                    </div>
                </li>
            </ul>'''

# Pattern pour trouver la navigation
NAV_PATTERN = re.compile(
    r'<ul class="nav-links">.*?</ul>',
    re.DOTALL
)

# Script translations.js à ajouter
TRANSLATIONS_SCRIPT = '    <script src="translations.js"></script>\n'

def add_language_selector_to_file(file_path):
    """Ajoute le sélecteur de langue et le script translations.js à un fichier HTML."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Remplacer la navigation si elle n'a pas déjà les traductions
        if 'data-translate="nav.' not in content:
            content = NAV_PATTERN.sub(NAV_WITH_TRANSLATIONS, content, count=1)
        
        # Ajouter le script translations.js avant visitor-counter.js si pas déjà présent
        if 'translations.js' not in content and 'visitor-counter.js' in content:
            content = content.replace(
                '    <script src="visitor-counter.js" defer></script>',
                TRANSLATIONS_SCRIPT + '    <script src="visitor-counter.js" defer></script>'
            )
        
        # Écrire seulement si des changements ont été faits
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[OK] Mis a jour: {file_path.name}")
            return True
        else:
            print(f"[SKIP] Deja a jour: {file_path.name}")
            return False
    except Exception as e:
        print(f"[ERROR] Erreur sur {file_path.name}: {e}")
        return False

def main():
    """Traite tous les fichiers HTML dans le dossier docs."""
    html_files = list(DOCS_DIR.glob("*.html"))
    
    # Exclure guide-cybersecurite.html qui est un fichier spécial
    html_files = [f for f in html_files if f.name != "guide-cybersecurite.html"]
    
    print(f"Traitement de {len(html_files)} fichiers HTML...\n")
    
    updated_count = 0
    for html_file in html_files:
        if add_language_selector_to_file(html_file):
            updated_count += 1
    
    print(f"\n[OK] {updated_count} fichier(s) mis a jour sur {len(html_files)}")

if __name__ == "__main__":
    main()
