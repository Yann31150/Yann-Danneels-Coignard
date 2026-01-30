#!/usr/bin/env python3
"""
Script pour ajouter le lien "Mon Parcours" (timeline.html) dans la navigation de toutes les pages.
"""

import re
from pathlib import Path

DOCS_DIR = Path(__file__).parent.parent / "docs"

# Pattern pour trouver la ligne "À propos" dans la navigation
PATTERN = re.compile(
    r'(<li><a href="apropos\.html" data-translate="nav\.apropos">À propos</a></li>\s*)'
    r'(<li><a href="competences\.html" data-translate="nav\.competences">Compétences</a></li>)',
    re.MULTILINE
)

REPLACEMENT = r'\1<li><a href="timeline.html" data-translate="nav.timeline">Mon Parcours</a></li>\n                \2'

def add_timeline_link(file_path):
    """Ajoute le lien timeline dans la navigation."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Vérifier si le lien timeline existe déjà
        if 'timeline.html' in content and 'data-translate="nav.timeline"' in content:
            print(f"[SKIP] Deja present: {file_path.name}")
            return False
        
        # Ajouter le lien timeline
        content = PATTERN.sub(REPLACEMENT, content)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[OK] Mis a jour: {file_path.name}")
            return True
        else:
            print(f"[SKIP] Pattern non trouve: {file_path.name}")
            return False
    except Exception as e:
        print(f"[ERROR] Erreur sur {file_path.name}: {e}")
        return False

def main():
    html_files = list(DOCS_DIR.glob("*.html"))
    html_files = [f for f in html_files if f.name != "guide-cybersecurite.html"]
    
    print(f"Ajout du lien Timeline dans {len(html_files)} fichiers HTML...\n")
    
    updated_count = 0
    for html_file in html_files:
        if add_timeline_link(html_file):
            updated_count += 1
    
    print(f"\n[OK] {updated_count} fichier(s) mis a jour sur {len(html_files)}")

if __name__ == "__main__":
    main()
