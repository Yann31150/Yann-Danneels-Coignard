#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour mettre à jour la navigation dans tous les fichiers HTML
Retire les liens vers timeline.html, competences.html et passions.html
"""

import os
import re
from pathlib import Path

# Chemin vers le dossier docs
DOCS_DIR = Path(__file__).parent.parent / "docs"

# Fichiers HTML à mettre à jour (exclure apropos.html qui est déjà fait)
HTML_FILES = [
    "index.html",
    "outils.html",
    "projets.html",
    "cv.html",
    "databridge.html",
    "actualites-tech.html",
    "cybersecurite.html",
    "contact.html",
    "guide-cybersecurite.html"
]

# Patterns à retirer
PATTERNS_TO_REMOVE = [
    r'<li><a href="timeline\.html"[^>]*>.*?</a></li>\s*',
    r'<li><a href="competences\.html"[^>]*>.*?</a></li>\s*',
    r'<li><a href="passions\.html"[^>]*>.*?</a></li>\s*',
]

def update_navigation(file_path):
    """Met à jour la navigation dans un fichier HTML"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Retirer chaque pattern
        for pattern in PATTERNS_TO_REMOVE:
            content = re.sub(pattern, '', content, flags=re.DOTALL | re.IGNORECASE)
        
        # Si le contenu a changé, sauvegarder
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[OK] {file_path.name}")
            return True
        else:
            print(f"[SKIP] {file_path.name} (aucun changement)")
            return False
            
    except Exception as e:
        print(f"[ERROR] {file_path.name}: {e}")
        return False

def main():
    """Fonction principale"""
    print("Mise à jour de la navigation dans les fichiers HTML...")
    print("-" * 60)
    
    updated_count = 0
    
    for html_file in HTML_FILES:
        file_path = DOCS_DIR / html_file
        if file_path.exists():
            if update_navigation(file_path):
                updated_count += 1
        else:
            print(f"[SKIP] {html_file} (fichier introuvable)")
    
    print("-" * 60)
    print(f"Terminé : {updated_count} fichier(s) mis à jour")

if __name__ == "__main__":
    main()
