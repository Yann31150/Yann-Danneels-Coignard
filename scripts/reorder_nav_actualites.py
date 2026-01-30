#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour mettre Actualités Tech en 2ème position dans la navigation
"""

import re
from pathlib import Path

DOCS_DIR = Path(__file__).parent.parent / "docs"

HTML_FILES = [
    "outils.html",
    "projets.html",
    "cv.html",
    "databridge.html",
    "actualites-tech.html",
    "cybersecurite.html",
    "contact.html",
    "guide-cybersecurite.html"
]

def update_nav(file_path):
    """Met à jour la navigation dans un fichier HTML"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Pattern pour trouver et remplacer la navigation
        # Chercher la ligne Actualités Tech et la retirer
        actualites_line = r'<li><a href="actualites-tech\.html"[^>]*>.*?</a></li>\s*'
        
        # Si Actualités Tech existe dans le fichier
        if re.search(actualites_line, content):
            # Retirer Actualités Tech de sa position actuelle
            content = re.sub(actualites_line, '', content)
            
            # L'ajouter juste après Accueil
            content = re.sub(
                r'(<li><a href="index\.html"[^>]*>.*?</a></li>\s*)',
                r'\1<li><a href="actualites-tech.html" data-translate="nav.actualites">Actualités Tech</a></li>\n                ',
                content
            )
        
        if content != original:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[OK] {file_path.name}")
            return True
        else:
            print(f"[SKIP] {file_path.name}")
            return False
            
    except Exception as e:
        print(f"[ERROR] {file_path.name}: {e}")
        return False

def main():
    print("Réorganisation navigation : Actualités Tech en 2ème position...")
    print("-" * 60)
    
    updated = 0
    for html_file in HTML_FILES:
        file_path = DOCS_DIR / html_file
        if file_path.exists():
            if update_nav(file_path):
                updated += 1
        else:
            print(f"[SKIP] {html_file} (introuvable)")
    
    print("-" * 60)
    print(f"Terminé : {updated} fichier(s) mis à jour")

if __name__ == "__main__":
    main()
